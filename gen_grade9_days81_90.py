#!/usr/bin/env python3
"""Grade 9, Days 81-90 -- extends Grade 9 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade9.json):
epistolary narratives, op-ed rebuttals, nominalization, neologisms, the
uncanny in Gothic literature, personal manifestos, AI-generated content,
absolute phrases, comparing translations; solving systems by
substitution, box-and-whisker plots, direct/partial variation, correlation
vs causation, comparing loan options, weighted averages, composite solids
with curved surfaces, modular arithmetic; epigenetics, superconductivity,
coral reef bleaching, quantum mechanics, immunology, bioplastics, black
holes and general relativity, epidemiology, battery technology; renewable
energy grids, undersea internet cables, language extinction and
preservation, supply chain disruptions, desalination, megacities and
informal settlements, climate adaptation strategies, commercial
spaceflight, and global health disparities.

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 9 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-english'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science'
SS9 = 'https://tvolearn.com/pages/grade-9-geography'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 English',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science',
    'TVO Learn: Grade 9 Geography',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


def _rebalance_answer_positions(days, seed=20260928):
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


g9_81_90 = [
day(81, [
L('Reading: Analyzing Epistolary Narratives',
  'Grade 9 Language strand: an epistolary narrative tells a story through letters, diary entries, or other documents, giving readers a direct, personal window into a character’s voice and perspective.',
  [('What do we call a narrative told through letters or diary entries?', ['An epistolary narrative', 'A concept unrelated to reading', 'A biography', 'A recipe'], 0),
   ('Does an epistolary narrative give readers a direct window into a character’s voice?', ['Yes', 'No, this format never reveals a character’s voice', 'A concept unrelated to epistolary narratives', 'This format only ever uses a third-person narrator'], 0),
   ('Why might an author choose an epistolary format to tell a story?', ['It can create intimacy and immediacy by presenting events directly through a character’s own words', 'Epistolary narratives never create any sense of intimacy', 'This concept has no connection to literature', 'This format always distances readers from the characters'], 0),
   ('Why might reading multiple letters from different characters in an epistolary novel be useful?', ['It can reveal multiple perspectives on the same events', 'Multiple letters never add any new perspective to a story', 'This concept has no connection to reading comprehension', 'Only one single perspective is ever possible in this format'], 0),
   ('Which of these is an example of an epistolary structure?', ['A novel told entirely through a character’s diary entries', 'A novel narrated by an all-knowing narrator', 'A textbook chapter on chemistry', 'A newspaper weather report'], 0)]),
M('Solving Systems of Equations by Substitution',
  'Grade 9 Math strand: the substitution method solves a system of two linear equations by isolating one variable in one equation, then substituting that expression into the other equation.',
  [('In the substitution method, what is the first step?', ['Isolate one variable in one equation', 'Graph both equations immediately', 'A concept unrelated to systems of equations', 'Add both equations together without isolating anything'], 0),
   ('After isolating a variable, what do you do with that expression?', ['Substitute it into the other equation', 'Ignore it completely', 'A concept unrelated to substitution', 'Divide it by zero'], 0),
   ('If y equals 2x plus 1, and this is substituted into another equation, what are you solving for first?', ['The value of x', 'The value of y only', 'A concept unrelated to substitution', 'Nothing at all'], 0),
   ('Why might substitution be a useful method when one equation is already solved for a variable?', ['It saves time by allowing direct substitution instead of additional algebraic manipulation', 'Substitution is never useful in this situation', 'This concept has no connection to algebra', 'Substitution only works when no variable is isolated'], 0),
   ('If x plus y equals 12 and y equals 5, what is the value of x?', ['7', '5', '12', '17'], 0)]),
Sc('Science: Epigenetics: Gene Expression and Environment',
   'Grade 9 Science strand: epigenetics studies how environmental factors can influence whether specific genes are turned on or off, without altering the underlying DNA sequence itself.',
   [('What does epigenetics study?', ['How environmental factors influence whether genes are turned on or off', 'How DNA sequences are physically rewritten', 'A concept unrelated to biology', 'How cells divide during mitosis'], 0),
    ('Does epigenetics involve changing the underlying DNA sequence?', ['No', 'Yes, it always changes the DNA sequence', 'A concept unrelated to epigenetics', 'DNA sequence has no connection to epigenetics'], 0),
    ('Name one environmental factor that could influence gene expression, such as diet.', ['Diet', 'A concept unrelated to epigenetics', 'A favourite hobby', 'A random guess with no scientific basis'], 0),
    ('Why might identical twins, who share the same DNA, develop some different traits over their lives?', ['Different environmental experiences could lead to different epigenetic changes affecting gene expression', 'Identical twins can never develop any different traits', 'This concept has no connection to epigenetics', 'DNA sequence alone always determines every trait with no other influence'], 0),
    ('Why is epigenetics considered a valuable area of modern biological research?', ['It helps explain how environment and genetics interact to influence health and traits', 'Epigenetics has no connection to health or biology', 'This concept has no relevance to science', 'Genes are the only factor that ever influences an organism’s traits'], 0)]),
SS('Social Studies: The Geography of Renewable Energy Grids',
   'Grade 9 Social Studies strand: renewable energy grids connect power sources like wind and solar farms to homes and businesses, requiring careful geographic planning to manage energy where it is generated and used.',
   [('What do renewable energy grids connect power sources to?', ['Homes and businesses', 'Only remote, unpopulated areas', 'A concept unrelated to geography', 'Nothing at all'], 0),
    ('Name one renewable power source that might connect to an energy grid, such as wind or solar.', ['Wind', 'A concept unrelated to renewable energy', 'Coal', 'Oil'], 0),
    ('Does building a renewable energy grid require careful geographic planning?', ['Yes', 'No, energy grids require no planning at all', 'A concept unrelated to renewable energy grids', 'Geography has no connection to energy grids'], 0),
    ('Why might a region with strong, consistent winds be an ideal location for a wind farm connected to the grid?', ['Consistent wind can generate more reliable and efficient electricity', 'Wind speed has no connection to how much electricity a turbine generates', 'This concept has no connection to geography', 'Wind farms work equally well in every location regardless of wind patterns'], 0),
    ('Why might connecting renewable energy sources across a large geographic area help balance electricity supply?', ['If one area lacks sun or wind, energy from another connected region can help meet demand', 'Connecting energy sources across regions never has any benefit', 'This concept has no relevance to geography', 'Renewable energy grids only ever work within a single small area'], 0)]),
]),

day(82, [
L('Writing: The Persuasive Op-Ed Rebuttal',
  'Grade 9 Language strand: an op-ed rebuttal responds directly to a previously published opinion piece, presenting a counterargument backed by evidence and clear reasoning.',
  [('What does an op-ed rebuttal respond to?', ['A previously published opinion piece', 'A math textbook chapter', 'A concept unrelated to writing', 'A weather forecast'], 0),
   ('Should an op-ed rebuttal be backed by evidence and clear reasoning?', ['Yes', 'No, rebuttals never require any evidence', 'A concept unrelated to writing', 'Only vague opinions are allowed, with no reasoning at all'], 0),
   ('Why might a writer directly quote the original article when writing a rebuttal?', ['It ensures the counterargument accurately addresses the original claims', 'Quoting an article never helps strengthen a rebuttal', 'This concept has no connection to writing', 'Rebuttals should never reference the original argument at all'], 0),
   ('Which of these would most likely appear in an op-ed rebuttal?', ['Contrary to the original article’s claim, recent data actually shows a different trend.', 'Once upon a time, in a faraway kingdom.', 'Add 8 and 7 to get 15.', 'The chemical symbol for gold is Au.'], 0),
   ('Why is tone important to consider when writing a persuasive rebuttal?', ['A respectful, reasoned tone can make an argument more credible and persuasive', 'Tone never affects how persuasive an argument seems', 'This concept has no connection to writing', 'An aggressive tone always makes a rebuttal more convincing'], 0)]),
M('Scientific Notation: Operations',
  'Grade 9 Math strand: students multiply and divide numbers written in scientific notation by combining the exponents of 10 while multiplying or dividing the decimal coefficients.',
  [('When multiplying two numbers in scientific notation, what happens to the exponents of 10?', ['They are added together', 'They are subtracted', 'A concept unrelated to scientific notation', 'They are multiplied together'], 0),
   ('When dividing two numbers in scientific notation, what happens to the exponents of 10?', ['They are subtracted', 'They are added together', 'A concept unrelated to scientific notation', 'They are divided'], 0),
   ('What is the result of multiplying (3 times 10 to the 4th) by (2 times 10 to the 3rd)?', ['6 times 10 to the 7th', '6 times 10 to the 12th', '5 times 10 to the 7th', '6 times 10 to the 1st'], 0),
   ('Why is scientific notation useful when calculating with very large astronomical distances?', ['It simplifies extremely large numbers into a compact, manageable form', 'Scientific notation never simplifies any large numbers', 'This concept has no connection to math', 'Scientific notation only works with small, simple numbers'], 0),
   ('What is the result of dividing (9 times 10 to the 6th) by (3 times 10 to the 2nd)?', ['3 times 10 to the 4th', '3 times 10 to the 8th', '6 times 10 to the 4th', '3 times 10 to the 3rd'], 0)]),
Sc('Science: The Physics of Superconductivity',
   'Grade 9 Science strand: a superconductor is a material that conducts electricity with zero resistance when cooled below a critical temperature, allowing electric current to flow without energy loss.',
   [('What is a superconductor?', ['A material that conducts electricity with zero resistance below a critical temperature', 'A material that always blocks electricity completely', 'A concept unrelated to physics', 'A material that only conducts electricity at room temperature'], 0),
    ('Does a superconductor need to be cooled below a certain temperature to achieve zero resistance?', ['Yes', 'No, superconductors work the same at any temperature', 'A concept unrelated to superconductors', 'Temperature has no connection to superconductivity'], 0),
    ('Does electric current flow through a superconductor without losing energy?', ['Yes', 'No, superconductors always lose significant energy', 'A concept unrelated to superconductors', 'Superconductors never actually conduct any electricity'], 0),
    ('Why might superconducting magnets be used in medical MRI machines?', ['They can generate strong, stable magnetic fields efficiently without energy loss from resistance', 'Superconductors have no connection to medical imaging technology', 'This concept has no relevance to science', 'MRI machines never use any superconducting technology'], 0),
    ('Why is finding a superconductor that works at higher, more practical temperatures an active area of research?', ['Current superconductors often require expensive, complex cooling systems to function', 'Superconductors already work perfectly at room temperature with no research needed', 'This concept has no relevance to physics', 'Cooling temperature has no connection to how superconductors are used'], 0)]),
SS('Social Studies: The Geography of Undersea Internet Cables',
   'Grade 9 Social Studies strand: most global internet traffic travels through undersea fibre-optic cables laid across ocean floors, connecting continents and shaping the geography of modern communication.',
   [('What do undersea internet cables carry across ocean floors?', ['Global internet traffic', 'Only local phone calls within one country', 'A concept unrelated to geography', 'Ocean water for desalination'], 0),
    ('Do undersea cables connect different continents?', ['Yes', 'No, undersea cables never connect separate continents', 'A concept unrelated to internet infrastructure', 'Undersea cables only exist within a single country’s borders'], 0),
    ('Does most global internet traffic travel through undersea cables?', ['Yes', 'No, internet traffic only ever travels through satellites', 'A concept unrelated to internet geography', 'Undersea cables have no connection to internet traffic at all'], 0),
    ('Why might damage to an undersea internet cable significantly disrupt communication in a region?', ['A large amount of a region’s internet traffic could depend on a limited number of cable routes', 'Damage to undersea cables never has any effect on internet access', 'This concept has no connection to geography', 'Every region has unlimited alternative routes for internet traffic'], 0),
    ('Why is the geography of undersea cable routes an important consideration for global communication infrastructure?', ['Cable routes must navigate ocean depths, geopolitical boundaries, and geographic obstacles', 'Geography has no connection to how undersea cables are planned', 'This concept has no relevance to social studies', 'Undersea cables can be placed anywhere with no geographic planning needed'], 0)]),
]),

day(83, [
L('Grammar: Nominalization and Formal Register',
  'Grade 9 Language strand: nominalization turns a verb or adjective into a noun, such as changing analyze into analysis, often used to create a more formal, academic register in writing.',
  [('What does nominalization do to a verb or adjective?', ['Turns it into a noun', 'Turns it into a question', 'A concept unrelated to grammar', 'Removes it from the sentence entirely'], 0),
   ('Which word is the nominalized form of the verb analyze?', ['Analysis', 'Analyzing', 'Analytical', 'Analyzed'], 0),
   ('Is nominalization commonly associated with a formal or informal writing register?', ['A formal register', 'An informal register only', 'A concept unrelated to nominalization', 'Neither a formal nor an informal register'], 0),
   ('Which sentence uses nominalization?', ['The team’s analysis revealed a surprising trend.', 'The team analyzed the data quickly.', 'They will analyze it tomorrow.', 'Analyzing takes a long time sometimes.'], 0),
   ('Why might a writer use nominalization in a formal academic essay?', ['It can create a more objective, abstract, and formal tone', 'Nominalization always makes writing sound more casual', 'This concept has no connection to writing style', 'Formal essays never use any nominalized words'], 0)]),
M('Data: Box-and-Whisker Plots and Quartiles',
  'Grade 9 Math strand: a box-and-whisker plot displays a data set’s distribution using five key values: the minimum, first quartile, median, third quartile, and maximum.',
  [('How many key values does a box-and-whisker plot use to display data?', ['Five', 'Two', 'Three', 'Ten'], 0),
   ('What is the middle value of a data set called, shown in a box-and-whisker plot?', ['The median', 'The minimum', 'The maximum', 'A concept unrelated to data'], 0),
   ('What does the first quartile represent in a data set?', ['The value below which 25 percent of the data falls', 'The exact average of the entire data set', 'A concept unrelated to quartiles', 'The single highest value in the data set'], 0),
   ('Why might a box-and-whisker plot be useful for comparing test scores between two different classes?', ['It shows the spread and central values clearly, making comparison easier', 'Box-and-whisker plots never help with comparing data sets', 'This concept has no connection to data management', 'Test scores can never be organized into a box-and-whisker plot'], 0),
   ('What is the highest value in a data set called, shown in a box-and-whisker plot?', ['The maximum', 'The minimum', 'The median', 'The first quartile'], 0)]),
Sc('Science: Marine Biology: Coral Reefs and Bleaching',
   'Grade 9 Science strand: coral reefs are built by colonies of tiny coral organisms and support enormous marine biodiversity, but rising ocean temperatures can cause coral bleaching, threatening these ecosystems.',
   [('What builds a coral reef?', ['Colonies of tiny coral organisms', 'Large boulders that fall from cliffs', 'A concept unrelated to marine biology', 'Sand deposited by ocean currents'], 0),
    ('Do coral reefs support enormous marine biodiversity?', ['Yes', 'No, coral reefs support no marine life at all', 'A concept unrelated to coral reefs', 'Only one single species can ever live near a coral reef'], 0),
    ('What can rising ocean temperatures cause in coral reefs?', ['Coral bleaching', 'Increased coral growth with no negative effects', 'A concept unrelated to coral reefs', 'No change of any kind'], 0),
    ('Why does coral bleaching occur when ocean water becomes too warm?', ['Heat stress causes coral to expel the colourful algae that provide them with food and colour', 'Warmer water always makes coral healthier and more colourful', 'This concept has no connection to marine biology', 'Coral reefs are never affected by ocean temperature'], 0),
    ('Why is protecting coral reefs considered important for global biodiversity?', ['They support a huge variety of marine species that depend on the reef ecosystem', 'Coral reefs have no connection to global biodiversity', 'This concept has no relevance to science', 'Marine species never depend on coral reefs for survival'], 0)]),
SS('Social Studies: The Geography of Language Extinction and Preservation',
   'Grade 9 Social Studies strand: many of the world’s languages are at risk of disappearing as fewer speakers remain, prompting geographic and cultural efforts to document and preserve endangered languages.',
   [('What is happening to many of the world’s languages as fewer speakers remain?', ['They are at risk of disappearing', 'They are all becoming more widely spoken', 'A concept unrelated to geography', 'They are being replaced instantly with no loss of any kind'], 0),
    ('Are efforts being made to document and preserve endangered languages?', ['Yes', 'No, no effort has ever been made to preserve any language', 'A concept unrelated to language preservation', 'Preservation efforts have no connection to endangered languages'], 0),
    ('Can geography play a role in why certain languages become endangered?', ['Yes', 'No, geography has no connection to language survival', 'A concept unrelated to language extinction', 'Every language faces the exact same risk regardless of location'], 0),
    ('Why might a remote community’s language be at particular risk of disappearing?', ['Smaller, more isolated populations may have fewer remaining speakers passing on the language', 'Remote communities never face any risk of losing their language', 'This concept has no connection to geography', 'Language risk has no connection to the size of a speaker population'], 0),
    ('Why is language preservation considered an important cultural and geographic issue?', ['Language carries unique knowledge, history, and identity tied to a specific place and people', 'Preserving a language never has any cultural value', 'This concept has no relevance to social studies', 'Every language in the world carries the exact same information'], 0)]),
]),

day(84, [
L('Vocabulary: Neologisms in Modern Language',
  'Grade 9 Language strand: a neologism is a newly coined word or phrase, often created to describe new technology, trends, or ideas, such as podcast or crowdfunding.',
  [('What do we call a newly coined word or phrase?', ['A neologism', 'A concept unrelated to vocabulary', 'A synonym', 'A homophone'], 0),
   ('Which of these is an example of a neologism related to modern technology?', ['Podcast', 'Apple', 'Book', 'Tree'], 0),
   ('Are neologisms often created to describe new technology, trends, or ideas?', ['Yes', 'No, neologisms are never connected to new ideas', 'A concept unrelated to neologisms', 'Neologisms only ever describe ancient concepts'], 0),
   ('Why might a neologism like crowdfunding become widely used in everyday language?', ['It fills a need to describe a new activity or concept that did not previously have a common name', 'Neologisms are never actually adopted into everyday language', 'This concept has no connection to vocabulary', 'New words are never created to describe modern activities'], 0),
   ('Why do dictionaries sometimes add neologisms years after they were first coined?', ['Dictionaries aim to reflect language as it is actually used once a word becomes widely adopted', 'Dictionaries never add any new words at all', 'This concept has no connection to vocabulary', 'Neologisms are always immediately removed from language'], 0)]),
M('Direct and Partial Variation Applications',
  'Grade 9 Math strand: direct variation describes a relationship where one quantity is a constant multiple of another, while partial variation includes an additional fixed starting amount.',
  [('In direct variation, is one quantity always a constant multiple of another?', ['Yes', 'No, direct variation never involves a constant multiple', 'A concept unrelated to variation', 'The relationship is always completely random'], 0),
   ('Does partial variation include an additional fixed starting amount?', ['Yes', 'No, partial variation never includes a fixed amount', 'A concept unrelated to partial variation', 'A fixed amount only appears in direct variation, never partial'], 0),
   ('If a taxi charges a flat fee plus a rate per kilometre, is this direct or partial variation?', ['Partial variation', 'Direct variation', 'A concept unrelated to variation', 'Neither type of variation'], 0),
   ('If the cost of apples is directly proportional to the number bought, with no flat fee, is this direct or partial variation?', ['Direct variation', 'Partial variation', 'A concept unrelated to variation', 'Neither type of variation'], 0),
   ('Why is it useful to recognize whether a real-world situation follows direct or partial variation?', ['It helps set up the correct equation to model and solve the situation', 'Recognizing the type of variation never helps with solving a problem', 'This concept has no connection to math', 'Direct and partial variation are always modelled with the exact same equation'], 0)]),
Sc('Science: Quantum Mechanics: An Introduction',
   'Grade 9 Science strand: quantum mechanics is the branch of physics that studies the behaviour of extremely small particles, which can behave in ways that differ significantly from everyday, large-scale objects.',
   [('What does quantum mechanics study?', ['The behaviour of extremely small particles', 'The behaviour of extremely large objects only', 'A concept unrelated to physics', 'Only objects visible to the naked eye'], 0),
    ('Can small particles studied in quantum mechanics behave differently than large, everyday objects?', ['Yes', 'No, small particles always behave exactly like large objects', 'A concept unrelated to quantum mechanics', 'Particles never behave in any predictable pattern'], 0),
    ('Why do scientists need quantum mechanics instead of only classical physics to describe particles like electrons?', ['Classical physics rules do not fully apply at the extremely small scale of particles like electrons', 'Classical physics fully explains the behaviour of every particle with no exceptions', 'This concept has no connection to quantum mechanics', 'Electrons behave in exactly the same way as everyday objects like balls'], 0),
    ('Why is quantum mechanics considered important for developing modern technology, like computer processors?', ['Understanding particle behaviour at this scale has enabled major advances in electronics', 'Quantum mechanics has no connection to modern technology', 'This concept has no relevance to science', 'Computer processors are built with no reliance on quantum mechanics'], 0),
    ('Why might quantum mechanics be considered one of the more challenging areas of physics to fully grasp?', ['Its behaviour can seem counterintuitive compared to everyday physical experiences', 'Quantum mechanics is always simpler to understand than everyday physics', 'This concept has no relevance to physics', 'Quantum mechanics involves no unusual or unexpected behaviour at all'], 0)]),
SS('Social Studies: The Geography of Global Supply Chain Disruptions',
   'Grade 9 Social Studies strand: a global supply chain connects the production, transportation, and sale of goods across many countries, and disruptions, such as extreme weather or port closures, can affect availability worldwide.',
   [('What does a global supply chain connect across many countries?', ['The production, transportation, and sale of goods', 'Only a single country’s local farmers markets', 'A concept unrelated to geography', 'Nothing at all connected to goods or trade'], 0),
    ('Name one event that could disrupt a global supply chain, such as extreme weather.', ['Extreme weather', 'A concept unrelated to supply chains', 'A calm, sunny day with no unusual events', 'A holiday celebrated locally'], 0),
    ('Can a supply chain disruption affect the availability of goods worldwide?', ['Yes', 'No, disruptions never affect availability anywhere', 'A concept unrelated to supply chains', 'Only a single store is ever affected by any disruption'], 0),
    ('Why might a port closure in one country have effects on stores in a completely different country?', ['Goods often pass through multiple countries and ports before reaching their final destination', 'Port closures never have any effect beyond their own local area', 'This concept has no connection to geography', 'Every country only ever relies on goods produced within its own borders'], 0),
    ('Why is understanding the geography of supply chains useful for predicting how global events might affect local availability of goods?', ['It helps identify how disruptions in one region can ripple outward to affect other places', 'Supply chain geography never has any connection to local availability of goods', 'This concept has no relevance to social studies', 'Global events never have any effect on what is available in local stores'], 0)]),
]),

day(85, [
L('Reading: Analyzing the Uncanny in Gothic Literature',
  'Grade 9 Language strand: the uncanny refers to something eerily familiar yet strange, a feeling often used in Gothic literature to create unease, such as a lifelike doll or an unusually quiet house.',
  [('What does the uncanny refer to in literature?', ['Something eerily familiar yet strange', 'Something completely ordinary with no unusual qualities', 'A concept unrelated to reading', 'A cheerful, comforting feeling'], 0),
   ('Is the uncanny often used in Gothic literature to create unease?', ['Yes', 'No, the uncanny is never used to create unease', 'A concept unrelated to Gothic literature', 'The uncanny only ever creates a calm, relaxed feeling'], 0),
   ('Which of these is an example of the uncanny?', ['A lifelike doll that seems to move on its own', 'A sunny park full of children playing', 'A calm, quiet library', 'A friendly conversation between neighbours'], 0),
   ('Why might Gothic authors use the uncanny to unsettle readers?', ['Something familiar turned strange can create deep, lingering discomfort', 'The uncanny never has any effect on how a reader feels', 'This concept has no connection to Gothic literature', 'Familiar objects never create any sense of unease'], 0),
   ('Why is the uncanny considered a powerful literary tool for building suspense?', ['It plays on the tension between what feels familiar and what feels wrong, unsettling the reader', 'The uncanny never contributes to suspense in a story', 'This concept has no relevance to reading comprehension', 'Suspense is never connected to feelings of familiarity or strangeness'], 0)]),
M('Data: Correlation vs Causation',
  'Grade 9 Math strand: correlation describes a relationship between two variables, while causation means one variable directly causes a change in another, a stronger claim requiring more rigorous evidence.',
  [('What does correlation describe?', ['A relationship between two variables', 'A concept unrelated to data', 'The exact cause of an event', 'A single, unrelated fact'], 0),
   ('What does causation mean?', ['One variable directly causes a change in another', 'Two variables have absolutely no connection at all', 'A concept unrelated to data analysis', 'Correlation and causation always mean the exact same thing'], 0),
   ('Does correlation alone prove that one variable causes another?', ['No', 'Yes, correlation always proves causation', 'A concept unrelated to data', 'Correlation and causation are identical concepts'], 0),
   ('If sales of umbrellas and sales of raincoats both increase on rainy days, does that mean umbrellas cause raincoat sales?', ['No, both are likely related to a third factor, the rainy weather', 'Yes, umbrellas directly cause an increase in raincoat sales', 'A concept unrelated to correlation and causation', 'This proves a direct cause-and-effect relationship'], 0),
   ('Why is it important to understand the difference between correlation and causation when interpreting statistics?', ['Mistaking correlation for causation could lead to incorrect conclusions about a relationship', 'The two concepts are always interchangeable with no real difference', 'This concept has no connection to data analysis', 'Correlation and causation never need to be distinguished from each other'], 0)]),
Sc('Science: Vaccines and Immunology',
   'Grade 9 Science strand: immunology studies how the immune system protects the body from pathogens, and vaccines work by training the immune system to recognize specific pathogens before an actual infection occurs.',
   [('What does immunology study?', ['How the immune system protects the body from pathogens', 'How plants convert sunlight into food', 'A concept unrelated to biology', 'How rocks form over long periods of time'], 0),
    ('What do vaccines train the immune system to recognize?', ['Specific pathogens', 'Only harmless substances with no medical purpose', 'A concept unrelated to vaccines', 'Nothing at all related to disease'], 0),
    ('Do vaccines typically work by preparing the immune system before an actual infection occurs?', ['Yes', 'No, vaccines only work after a person is already infected', 'A concept unrelated to vaccines', 'Timing has no connection to how vaccines work'], 0),
    ('Why might a vaccine include a small, harmless piece of a pathogen rather than a full, dangerous version?', ['It allows the immune system to learn and build a defense safely, without causing the actual illness', 'Vaccines always include the full, dangerous version of a pathogen', 'This concept has no connection to immunology', 'A harmless piece of a pathogen provides no useful immune response'], 0),
    ('Why is widespread vaccination in a community sometimes linked to protecting people through herd immunity?', ['When enough people are immune, a disease has a harder time spreading, protecting those who cannot be vaccinated', 'Vaccinating a community never has any effect on how a disease spreads', 'This concept has no relevance to science', 'Herd immunity has no connection to vaccination at all'], 0)]),
SS('Social Studies: The Geography of Desalination',
   'Grade 9 Social Studies strand: desalination is the process of removing salt from seawater to produce fresh water, an increasingly important technology in regions facing water scarcity.',
   [('What is desalination?', ['The process of removing salt from seawater to produce fresh water', 'A process that adds salt to fresh water', 'A concept unrelated to geography', 'A method of purifying air, not water'], 0),
    ('Is desalination an increasingly important technology in regions facing water scarcity?', ['Yes', 'No, desalination has no connection to water scarcity', 'A concept unrelated to desalination', 'Water scarcity never affects any region in the world'], 0),
    ('Does desalination help produce fresh water from seawater?', ['Yes', 'No, desalination has no connection to producing fresh water', 'A concept unrelated to desalination', 'Desalination only ever removes fresh water from the ocean'], 0),
    ('Why might a coastal region facing limited fresh water resources invest in desalination technology?', ['It provides access to an abundant source of seawater that can be converted into usable fresh water', 'Desalination provides no benefit to a region facing water scarcity', 'This concept has no connection to geography', 'Coastal regions never face any water scarcity challenges'], 0),
    ('Why might the cost and energy requirements of desalination be an important consideration for a region deciding whether to build a plant?', ['Desalination can require significant energy and infrastructure investment, affecting its overall feasibility', 'Desalination never requires any energy or cost considerations', 'This concept has no relevance to social studies', 'Every region can build a desalination plant with no resource considerations at all'], 0)]),
]),

day(86, [
L('Writing: The Personal Manifesto',
  'Grade 9 Language strand: a personal manifesto expresses an individual’s core beliefs, values, and goals, often written with a confident, declarative tone to clarify one’s own convictions.',
  [('What kind of writing expresses an individual’s core beliefs and values?', ['A personal manifesto', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Is a personal manifesto often written with a confident, declarative tone?', ['Yes', 'No, it is always written in a hesitant, uncertain tone', 'A concept unrelated to writing', 'Tone never matters in a personal manifesto'], 0),
   ('Why might someone write a personal manifesto?', ['To clarify and express what they believe in and value most', 'Personal manifestos serve no real purpose', 'This concept has no connection to writing', 'Manifestos are only ever written by famous historical figures'], 0),
   ('Which of these sentences sounds most like it belongs in a personal manifesto?', ['I believe curiosity should guide how I approach every challenge.', 'The chemical symbol for iron is Fe.', 'Add 6 and 3 to get 9.', 'The capital of France is Paris.'], 0),
   ('Why might writing a personal manifesto help someone clarify their goals for the future?', ['Putting beliefs and values into words can help someone reflect on what truly matters to them', 'Writing a manifesto never helps clarify anyone’s goals', 'This concept has no connection to writing', 'Personal manifestos have no connection to future goals'], 0)]),
M('Financial Literacy: Comparing Loan Options',
  'Grade 9 Math strand: students compare different loan options by examining interest rates, repayment terms, and total cost over time to determine which option is more affordable.',
  [('What is one factor to examine when comparing loan options?', ['Interest rates', 'The colour of the lender’s logo', 'A concept unrelated to financial literacy', 'The lender’s office location only'], 0),
   ('Does a higher interest rate generally mean paying more over the life of a loan?', ['Yes', 'No, interest rates never affect total repayment cost', 'A concept unrelated to loans', 'A higher interest rate always means paying less overall'], 0),
   ('What is one reason a loan with a longer repayment term might cost more overall, even with smaller monthly payments?', ['Interest accumulates over a longer period of time', 'Longer repayment terms never affect the total cost of a loan', 'This concept has no connection to financial literacy', 'Monthly payments have no connection to total loan cost'], 0),
   ('Why is comparing the total cost of a loan more useful than just comparing monthly payments alone?', ['A lower monthly payment could still result in a higher total cost due to a longer term or higher interest', 'Monthly payments always give a complete picture of a loan’s true cost', 'This concept has no connection to financial literacy', 'Total cost is never affected by a loan’s length or interest rate'], 0),
   ('Why might someone choose a loan with a shorter term despite higher monthly payments?', ['It could result in paying less interest overall and paying off the debt sooner', 'Shorter loan terms always cost more overall than longer terms', 'This concept has no connection to financial literacy', 'Loan term length never affects the total amount paid'], 0)]),
Sc('Science: Bioplastics and Sustainable Materials',
   'Grade 9 Science strand: bioplastics are materials made from renewable sources, such as corn starch or sugarcane, offering a potential alternative to traditional plastics made from petroleum.',
   [('What are bioplastics made from?', ['Renewable sources, such as corn starch or sugarcane', 'Only petroleum, just like traditional plastic', 'A concept unrelated to materials science', 'Only metal and glass'], 0),
    ('Are bioplastics considered a potential alternative to traditional petroleum-based plastics?', ['Yes', 'No, bioplastics have no connection to traditional plastics', 'A concept unrelated to bioplastics', 'Bioplastics are exactly the same as petroleum-based plastics'], 0),
    ('Name one renewable source that can be used to make bioplastics, such as corn starch.', ['Corn starch', 'A concept unrelated to bioplastics', 'Crude oil', 'Coal'], 0),
    ('Why might bioplastics be considered a more sustainable option than some traditional plastics?', ['They can be made from renewable resources rather than a limited, non-renewable resource like petroleum', 'Bioplastics have no environmental benefit compared to traditional plastics', 'This concept has no connection to materials science', 'Traditional plastics are always more sustainable than bioplastics'], 0),
    ('Why do scientists continue researching how bioplastics break down in different environments?', ['Understanding decomposition helps evaluate whether bioplastics truly reduce environmental waste', 'Bioplastic decomposition has already been fully studied with nothing left to learn', 'This concept has no relevance to science', 'Bioplastics never actually decompose under any circumstances'], 0)]),
SS('Social Studies: The Geography of Megacities and Informal Settlements',
   'Grade 9 Social Studies strand: rapid urban growth in some regions has led to megacities with populations over 10 million, often including informal settlements that develop without official planning or infrastructure.',
   [('What is a megacity?', ['A city with a population over 10 million people', 'A small rural village', 'A concept unrelated to geography', 'A city with no residents at all'], 0),
    ('What is an informal settlement?', ['An area that develops without official planning or infrastructure', 'A carefully planned suburb with full infrastructure', 'A concept unrelated to urban geography', 'A rural farming community'], 0),
    ('Can informal settlements often develop within or near megacities?', ['Yes', 'No, informal settlements never occur near any megacity', 'A concept unrelated to megacities', 'Megacities always have complete, formal planning throughout'], 0),
    ('Why might informal settlements develop as a result of rapid urban population growth?', ['Infrastructure and housing development may not keep pace with the speed of population growth', 'Rapid population growth never leads to any housing challenges', 'This concept has no connection to geography', 'Informal settlements only ever appear in areas with no population growth at all'], 0),
    ('Why might residents of informal settlements face particular challenges with access to services like clean water or electricity?', ['These areas often lack the official infrastructure planning that formal neighbourhoods receive', 'Informal settlements always have exactly the same infrastructure as formal neighbourhoods', 'This concept has no relevance to social studies', 'Access to services has no connection to how a settlement developed'], 0)]),
]),

day(87, [
L('Media Literacy: Analyzing AI-Generated Content',
  'Grade 9 Language strand: AI-generated content, including text, images, and video created by artificial intelligence, raises questions about authenticity, authorship, and how audiences can verify what they see or read.',
  [('What does AI-generated content include, besides text?', ['Images and video', 'Only handwritten letters', 'A concept unrelated to media literacy', 'Only printed newspapers'], 0),
   ('Does AI-generated content raise questions about authenticity and authorship?', ['Yes', 'No, AI-generated content raises no questions at all', 'A concept unrelated to AI-generated content', 'Authenticity has no connection to AI-generated content'], 0),
   ('Why might it be difficult to tell whether an image was created by AI or a human artist?', ['AI tools can produce highly realistic images that closely mimic human-created work', 'AI-generated images are always obviously different from human-created ones', 'This concept has no connection to media literacy', 'AI-generated content never resembles anything created by a person'], 0),
   ('Why is it important for audiences to consider the source and authorship of content they encounter online?', ['Understanding whether content is AI-generated can affect how much they trust or verify its accuracy', 'The source of content never affects how it should be evaluated', 'This concept has no connection to media literacy', 'All online content is always completely reliable regardless of its source'], 0),
   ('Why might questions about authorship become more complex as AI-generated content becomes more common?', ['It can become harder to determine who or what is truly responsible for creating a piece of content', 'AI-generated content never raises any questions about who created it', 'This concept has no relevance to media literacy', 'Authorship has always been perfectly clear with no complexity at all'], 0)]),
M('Weighted Averages',
  'Grade 9 Math strand: a weighted average accounts for the relative importance of each value, such as a final grade calculated from assignments, tests, and exams that each carry a different percentage weight.',
  [('What does a weighted average account for that a simple average does not?', ['The relative importance of each value', 'Only the largest value in a set', 'A concept unrelated to averages', 'Only the smallest value in a set'], 0),
   ('If a final grade includes assignments worth 30 percent and an exam worth 70 percent, is this an example of a weighted average?', ['Yes', 'No, this has no connection to weighted averages', 'A concept unrelated to grading', 'Percentages are never used in weighted averages'], 0),
   ('If a test is worth twice as much as a quiz in a weighted average, does the test count more or less toward the final grade?', ['More', 'Less', 'A concept unrelated to weighted averages', 'The same amount as the quiz'], 0),
   ('Why might a weighted average give a more accurate reflection of a student’s overall performance than a simple average?', ['It reflects that some assessments, like exams, may matter more than others, like homework', 'A weighted average never gives a more accurate reflection of performance', 'This concept has no connection to math', 'Every assessment should always count exactly the same amount'], 0),
   ('If assignments are worth 40 percent and a final exam is worth 60 percent, which part has a greater impact on the final grade?', ['The final exam', 'The assignments', 'A concept unrelated to weighted averages', 'They always have an equal impact'], 0)]),
Sc('Science: Black Holes and General Relativity Basics',
   'Grade 9 Science strand: a black hole is a region in space with gravity so strong that nothing, not even light, can escape, and its existence is explained by Einstein’s theory of general relativity.',
   [('What is a black hole?', ['A region in space with gravity so strong nothing can escape it', 'A bright star that never changes', 'A concept unrelated to astronomy', 'An empty area of space with no gravity at all'], 0),
    ('Can light escape from a black hole?', ['No', 'Yes, light easily escapes a black hole', 'A concept unrelated to black holes', 'Only some types of light can escape'], 0),
    ('Which scientific theory helps explain the existence of black holes?', ['Einstein’s theory of general relativity', 'A concept unrelated to black holes', 'The theory of evolution', 'The germ theory of disease'], 0),
    ('Why can’t scientists directly see a black hole, even with powerful telescopes?', ['A black hole itself emits no light, since even light cannot escape its gravity', 'Black holes are actually very easy to see directly with the naked eye', 'This concept has no connection to how black holes work', 'Black holes emit extremely bright light that can always be seen'], 0),
    ('Why do scientists study the effects of black holes on nearby stars and matter?', ['Observing these effects can provide indirect evidence about black holes since they cannot be seen directly', 'Nearby stars are never affected in any way by a black hole', 'This concept has no relevance to science', 'Black holes have no measurable effect on their surroundings'], 0)]),
SS('Social Studies: The Geography of Climate Adaptation Strategies',
   'Grade 9 Social Studies strand: climate adaptation strategies, such as building sea walls or developing drought-resistant crops, help communities adjust to the effects of a changing climate in their specific region.',
   [('What do climate adaptation strategies help communities do?', ['Adjust to the effects of a changing climate', 'Ignore climate change completely', 'A concept unrelated to geography', 'Reverse climate change entirely on their own'], 0),
    ('Name one example of a climate adaptation strategy, such as building sea walls.', ['Building sea walls', 'A concept unrelated to climate adaptation', 'Ignoring rising sea levels', 'Removing all environmental protections'], 0),
    ('Do climate adaptation strategies often depend on a community’s specific region and needs?', ['Yes', 'No, every community uses the exact same strategy regardless of location', 'A concept unrelated to climate adaptation', 'Region has no connection to which strategies are useful'], 0),
    ('Why might a coastal community invest in sea walls as a climate adaptation strategy?', ['Rising sea levels could threaten coastal areas, and sea walls can help reduce flooding risk', 'Sea walls have no connection to protecting coastal communities', 'This concept has no connection to geography', 'Coastal communities are never affected by rising sea levels'], 0),
    ('Why might a farming region develop drought-resistant crops as part of its climate adaptation strategy?', ['Changing rainfall patterns could make traditional crops harder to grow reliably', 'Drought-resistant crops have no connection to climate adaptation', 'This concept has no relevance to social studies', 'Rainfall patterns never change due to a shifting climate'], 0)]),
]),

day(88, [
L('Grammar: Absolute Phrases and Sentence Variety',
  'Grade 9 Language strand: an absolute phrase modifies an entire sentence rather than a single word, often combining a noun with a participle, adding descriptive detail and sentence variety.',
  [('What does an absolute phrase modify?', ['An entire sentence', 'Only a single word', 'A concept unrelated to grammar', 'Nothing at all'], 0),
   ('An absolute phrase often combines a noun with what other type of word?', ['A participle', 'A preposition only', 'A concept unrelated to absolute phrases', 'A conjunction only'], 0),
   ('In the sentence Her hands trembling, she opened the letter, what is the absolute phrase?', ['Her hands trembling', 'She opened the letter', 'The letter', 'Opened'], 0),
   ('Which sentence correctly uses an absolute phrase?', ['His voice shaking, he delivered the speech.', 'His voice he shaking delivered speech the.', 'Shaking his voice he the speech delivered.', 'He delivered his voice shaking the speech.'], 0),
   ('Why might a writer use an absolute phrase to add sentence variety?', ['It can add vivid, descriptive detail while breaking up repetitive sentence patterns', 'Absolute phrases never add any variety to writing', 'This concept has no connection to grammar', 'Absolute phrases always make sentences less descriptive'], 0)]),
M('Geometry: Volume of Composite Solids with Curved Surfaces',
  'Grade 9 Math strand: students find the volume of composite solids that combine shapes with curved surfaces, such as a cylinder topped with a hemisphere, by calculating the volume of each part and adding them together.',
  [('To find the volume of a composite solid made of a cylinder and a hemisphere, what should you do?', ['Find the volume of each part and add them together', 'Only calculate the volume of the cylinder', 'A concept unrelated to composite solids', 'Only calculate the volume of the hemisphere'], 0),
   ('If a cylinder’s volume is 50 cubic cm and a hemisphere on top has a volume of 20 cubic cm, what is the total volume?', ['70 cubic cm', '50 cubic cm', '20 cubic cm', '30 cubic cm'], 0),
   ('Why is it useful to break a composite solid into simpler shapes before finding its volume?', ['It makes the calculation more manageable by using known volume formulas for each simple shape', 'Breaking a solid into simpler shapes never helps calculate its volume', 'This concept has no connection to geometry', 'Composite solids can never be broken into simpler shapes'], 0),
   ('If a composite solid is made of two cones with volumes of 12 and 8 cubic cm, what is the total volume?', ['20 cubic cm', '12 cubic cm', '8 cubic cm', '4 cubic cm'], 0),
   ('Why might understanding composite solid volume be useful for designing a real object, like a storage silo?', ['Many real objects combine simple shapes, so this skill helps calculate their total capacity', 'Composite solid volume never applies to any real-world object', 'This concept has no connection to geometry', 'Storage silos are always made of a single, simple shape'], 0)]),
Sc('Science: Epidemiology and Disease Modelling',
   'Grade 9 Science strand: epidemiology studies how diseases spread through populations, using mathematical models to predict outbreaks and help guide effective public health responses.',
   [('What does epidemiology study?', ['How diseases spread through populations', 'How rocks form over millions of years', 'A concept unrelated to science', 'How plants convert sunlight into food'], 0),
    ('Do epidemiologists use mathematical models to predict outbreaks?', ['Yes', 'No, epidemiology never uses any mathematical models', 'A concept unrelated to epidemiology', 'Disease outbreaks can never be predicted in any way'], 0),
    ('Can disease modelling help guide effective public health responses?', ['Yes', 'No, disease modelling has no connection to public health decisions', 'A concept unrelated to epidemiology', 'Public health responses never rely on any scientific modelling'], 0),
    ('Why might epidemiologists track how quickly a disease spreads from person to person?', ['This information helps predict future spread and guide public health responses', 'Tracking disease spread never provides any useful information', 'This concept has no connection to epidemiology', 'Diseases always spread at the exact same rate in every situation'], 0),
    ('Why is epidemiology considered an important field during a public health emergency?', ['It provides critical data to help guide decisions that protect public health', 'Epidemiology has no relevance during a public health emergency', 'This concept has no relevance to science', 'Public health emergencies never require any scientific data'], 0)]),
SS('Social Studies: The Geography of Commercial Spaceflight',
   'Grade 9 Social Studies strand: commercial spaceflight companies are developing launch sites and infrastructure around the world, raising new geographic questions about location, safety, and access to space.',
   [('What are commercial spaceflight companies developing around the world?', ['Launch sites and infrastructure', 'Only underwater research stations', 'A concept unrelated to geography', 'Nothing at all connected to space'], 0),
    ('Does the growth of commercial spaceflight raise new geographic questions?', ['Yes', 'No, commercial spaceflight raises no geographic questions at all', 'A concept unrelated to spaceflight', 'Geography has no connection to spaceflight infrastructure'], 0),
    ('Might location and safety be important considerations when building a spaceflight launch site?', ['Yes', 'No, location and safety are never considered for launch sites', 'A concept unrelated to commercial spaceflight', 'Launch sites can be built anywhere with no special considerations'], 0),
    ('Why might a launch site be built near a coastline rather than in a densely populated inland area?', ['It can allow rockets to launch over open water, reducing risk to populated areas', 'Coastlines have no advantage for launching spacecraft', 'This concept has no connection to geography', 'Launch sites are never influenced by nearby population density'], 0),
    ('Why might the growth of commercial spaceflight raise questions about equitable access to space exploration opportunities?', ['Not every country or region has the resources or infrastructure to participate equally in space activities', 'Every country has exactly the same access to space exploration resources', 'This concept has no relevance to social studies', 'Commercial spaceflight has no connection to global equity issues'], 0)]),
]),

day(89, [
L('Reading: Comparing Translations of a Text',
  'Grade 9 Language strand: comparing different translations of the same text can reveal how word choice, tone, and cultural context shape meaning, since no translation is a perfectly neutral copy of the original.',
  [('What can comparing different translations of the same text reveal?', ['How word choice, tone, and cultural context shape meaning', 'Nothing useful about the original text', 'A concept unrelated to reading', 'Only the exact number of pages in each version'], 0),
   ('Is a translation ever a perfectly neutral copy of the original text?', ['No', 'Yes, every translation is always perfectly neutral', 'A concept unrelated to translation', 'Translations never differ from one another in any way'], 0),
   ('Why might two translators choose different words for the same original sentence?', ['Each translator may interpret tone, culture, or meaning slightly differently', 'Translators always choose the exact same words with no variation', 'This concept has no connection to translation', 'Word choice never affects how a translation is understood'], 0),
   ('Why might comparing translations deepen a reader’s understanding of a classic work of literature?', ['It can reveal different interpretive choices and highlight aspects of meaning that a single translation might miss', 'Comparing translations never reveals anything new about a text', 'This concept has no connection to reading comprehension', 'Every translation of a classic work is always identical'], 0),
   ('Why might cultural context be an important factor for a translator to consider?', ['Certain words or expressions may carry meanings specific to a culture that do not directly translate', 'Cultural context never affects how a text should be translated', 'This concept has no relevance to reading comprehension', 'Every language shares identical cultural expressions with no differences'], 0)]),
M('Introduction to Modular Arithmetic',
  'Grade 9 Math strand: modular arithmetic involves working with remainders after division, often described as clock arithmetic, since numbers wrap around after reaching a fixed value called the modulus.',
  [('What does modular arithmetic involve working with?', ['Remainders after division', 'Only whole, undivided numbers', 'A concept unrelated to math', 'Only negative numbers'], 0),
   ('Why is modular arithmetic sometimes called clock arithmetic?', ['Numbers wrap around after reaching a fixed value, similar to how a clock resets after 12', 'Modular arithmetic has no connection to clocks or wrapping numbers', 'This concept has no connection to math', 'Clocks and modular arithmetic have never been compared to each other'], 0),
   ('What is 14 mod 5, meaning the remainder when 14 is divided by 5?', ['4', '14', '5', '9'], 0),
   ('What is 20 mod 6, meaning the remainder when 20 is divided by 6?', ['2', '20', '6', '3'], 0),
   ('Why might modular arithmetic be useful for solving problems involving repeating cycles, like days of the week?', ['It naturally models patterns that repeat after a fixed number of steps', 'Modular arithmetic never applies to any repeating or cyclical pattern', 'This concept has no connection to math', 'Days of the week have no connection to modular arithmetic'], 0)]),
Sc('Science: Battery Technology and Energy Storage',
   'Grade 9 Science strand: batteries store chemical energy and convert it into electrical energy through a reaction between two electrodes separated by an electrolyte, powering everything from phones to electric vehicles.',
   [('What type of energy do batteries store?', ['Chemical energy', 'Only light energy', 'A concept unrelated to batteries', 'Only sound energy'], 0),
    ('What are the two materials in a battery where a chemical reaction occurs, called?', ['Electrodes', 'A concept unrelated to batteries', 'Circuits', 'Insulators'], 0),
    ('What separates the two electrodes in a battery?', ['An electrolyte', 'A concept unrelated to batteries', 'A simple wire only', 'Nothing at all'], 0),
    ('Why might a rechargeable battery be able to reverse its chemical reaction?', ['Applying an external electrical current can reverse the chemical process, restoring the battery’s charge', 'Rechargeable batteries never actually reverse any chemical reaction', 'This concept has no connection to battery chemistry', 'All batteries work in exactly the same non-reversible way'], 0),
    ('Why is improving battery technology considered important for the wider adoption of electric vehicles?', ['Better batteries could allow vehicles to store more energy and travel farther on a single charge', 'Battery technology has no connection to electric vehicle range', 'This concept has no relevance to science', 'Electric vehicles never actually rely on any battery technology'], 0)]),
SS('Social Studies: The Geography of Global Health Disparities',
   'Grade 9 Social Studies strand: access to health care and health outcomes vary significantly across the world, influenced by geographic factors such as income, infrastructure, and distance to medical facilities.',
   [('Do access to health care and health outcomes vary across the world?', ['Yes', 'No, every region has exactly the same access to health care', 'A concept unrelated to global health', 'Health outcomes never depend on any geographic factor'], 0),
    ('Name one geographic factor that could influence health outcomes, such as distance to medical facilities.', ['Distance to medical facilities', 'A concept unrelated to health disparities', 'A community’s favourite sport', 'The average temperature on a random day'], 0),
    ('Can income level in a region influence access to health care?', ['Yes', 'No, income has no connection to health care access', 'A concept unrelated to global health', 'Every region has exactly the same income level'], 0),
    ('Why might a rural community far from a hospital face greater health challenges than an urban community?', ['Longer travel times and limited infrastructure could delay access to needed medical care', 'Distance to a hospital never has any effect on health outcomes', 'This concept has no connection to geography', 'Rural and urban communities always have identical access to health care'], 0),
    ('Why is understanding the geography of global health disparities useful for organizations working to improve health outcomes?', ['It helps identify which regions most need investment in health care infrastructure and resources', 'Global health disparities have no connection to geography', 'This concept has no relevance to social studies', 'Every region in the world requires the exact same health resources'], 0)]),
]),

day(90, [
L('Review: Narrative Analysis, Grammar, and Media Literacy (Days 81-89)',
  'Grade 9 Language strand review: students revisit epistolary narratives, op-ed rebuttals, nominalization, neologisms, the uncanny, personal manifestos, AI-generated content, absolute phrases, and comparing translations.',
  [('What do we call a narrative told through letters or diary entries?', ['An epistolary narrative', 'A concept unrelated to reading', 'A biography', 'A recipe'], 0),
   ('What does nominalization do to a verb or adjective?', ['Turns it into a noun', 'Turns it into a question', 'A concept unrelated to grammar', 'Removes it from the sentence entirely'], 0),
   ('What does the uncanny refer to in literature?', ['Something eerily familiar yet strange', 'Something completely ordinary with no unusual qualities', 'A concept unrelated to reading', 'A cheerful, comforting feeling'], 0),
   ('Does AI-generated content raise questions about authenticity and authorship?', ['Yes', 'No, AI-generated content raises no questions at all', 'A concept unrelated to AI-generated content', 'Authenticity has no connection to AI-generated content'], 0),
   ('Is a translation ever a perfectly neutral copy of the original text?', ['No', 'Yes, every translation is always perfectly neutral', 'A concept unrelated to translation', 'Translations never differ from one another in any way'], 0)]),
M('Review: Algebra, Statistics, and Financial Literacy (Days 81-89)',
  'Grade 9 Math strand review: students revisit solving systems by substitution, scientific notation operations, box-and-whisker plots, direct and partial variation, correlation vs causation, comparing loans, weighted averages, composite solid volume, and modular arithmetic.',
  [('In the substitution method, what is the first step?', ['Isolate one variable in one equation', 'Graph both equations immediately', 'A concept unrelated to systems of equations', 'Add both equations together without isolating anything'], 0),
   ('How many key values does a box-and-whisker plot use to display data?', ['Five', 'Two', 'Three', 'Ten'], 0),
   ('Does partial variation include an additional fixed starting amount?', ['Yes', 'No, partial variation never includes a fixed amount', 'A concept unrelated to partial variation', 'A fixed amount only appears in direct variation, never partial'], 0),
   ('What does a weighted average account for that a simple average does not?', ['The relative importance of each value', 'Only the largest value in a set', 'A concept unrelated to averages', 'Only the smallest value in a set'], 0),
   ('What is 14 mod 5, meaning the remainder when 14 is divided by 5?', ['4', '14', '5', '9'], 0)]),
Sc('Review: Physics, Biology, and Emerging Science (Days 81-89)',
   'Grade 9 Science strand review: students revisit epigenetics, superconductivity, coral reef bleaching, quantum mechanics, immunology, bioplastics, black holes, epidemiology, and battery technology.',
   [('What does epigenetics study?', ['How environmental factors influence whether genes are turned on or off', 'How DNA sequences are physically rewritten', 'A concept unrelated to biology', 'How cells divide during mitosis'], 0),
    ('What can rising ocean temperatures cause in coral reefs?', ['Coral bleaching', 'Increased coral growth with no negative effects', 'A concept unrelated to coral reefs', 'No change of any kind'], 0),
    ('What does quantum mechanics study?', ['The behaviour of extremely small particles', 'The behaviour of extremely large objects only', 'A concept unrelated to physics', 'Only objects visible to the naked eye'], 0),
    ('Which scientific theory helps explain the existence of black holes?', ['Einstein’s theory of general relativity', 'A concept unrelated to black holes', 'The theory of evolution', 'The germ theory of disease'], 0),
    ('What type of energy do batteries store?', ['Chemical energy', 'Only light energy', 'A concept unrelated to batteries', 'Only sound energy'], 0)]),
SS('Review: Global Geography and Modern Issues (Days 81-89)',
   'Grade 9 Social Studies strand review: students revisit renewable energy grids, undersea cables, language preservation, supply chain disruptions, desalination, megacities, climate adaptation, commercial spaceflight, and global health disparities.',
   [('What do renewable energy grids connect power sources to?', ['Homes and businesses', 'Only remote, unpopulated areas', 'A concept unrelated to geography', 'Nothing at all'], 0),
    ('What do undersea internet cables carry across ocean floors?', ['Global internet traffic', 'Only local phone calls within one country', 'A concept unrelated to geography', 'Ocean water for desalination'], 0),
    ('What is desalination?', ['The process of removing salt from seawater to produce fresh water', 'A process that adds salt to fresh water', 'A concept unrelated to geography', 'A method of purifying air, not water'], 0),
    ('What is a megacity?', ['A city with a population over 10 million people', 'A small rural village', 'A concept unrelated to geography', 'A city with no residents at all'], 0),
    ('Do access to health care and health outcomes vary across the world?', ['Yes', 'No, every region has exactly the same access to health care', 'A concept unrelated to global health', 'Health outcomes never depend on any geographic factor'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_81_90)
    append_to(9, g9_81_90)
