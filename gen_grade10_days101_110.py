#!/usr/bin/env python3
"""Grade 10, Days 101-110 -- extends Grade 10 from 100 to 110 days (the
second batch of the full-year expansion beyond the original 90-day
program). Topics chosen to avoid any overlap with the existing Day 1-100
set (see data/grade10.json): analyzing archetypes and the hero's journey,
the Gothic tradition in fiction, the feature article, commonly confused
words, the job interview, allegory and fable, the epic hero, speculative
fiction, and photojournalism; conic sections, trig sum and difference
identities, sampling methods and bias, the binomial probability
distribution, matrix transformations, an introduction to the derivative,
the vector cross product, the complex plane and polar form, and modular
arithmetic; percent yield and limiting reagents, the skeletal and
muscular systems, momentum and collisions, the nitrogen cycle, plant
reproduction and pollination, calorimetry and specific heat capacity,
naming ionic and molecular compounds, genetic mutations and variation,
and volcanoes/igneous rock formation; the War of 1812, the Rebellions of
1837-38, the Durham Report and responsible government, the road to
Confederation, the United Empire Loyalists, the Numbered Treaties, the
Acadian Expulsion, enemy alien internment in WWI, and the Selkirk
Settlement.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E10 = 'https://tvolearn.com/pages/grade-10-english'
M10 = 'https://tvolearn.com/pages/grade-10-mathematics'
S10 = 'https://tvolearn.com/pages/grade-10-science'
H10 = 'https://tvolearn.com/pages/grade-10-history'
RE, RM, RS, RH = (
    'TVO Learn: Grade 10 English',
    'TVO Learn: Grade 10 Mathematics',
    'TVO Learn: Grade 10 Science',
    'TVO Learn: Grade 10 History',
)


def E(t, s, q):
    return sub('English', t, s, RE, E10, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M10, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S10, q)


def H(t, s, q):
    return sub('History', t, s, RH, H10, q)


def _rebalance_answer_positions(days, seed=20260723):
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


g10_101_110 = [
day(101, [
E('Reading: Analyzing Archetypes and the Hero’s Journey',
  'Grade 10 English strand: an archetype is a recurring character, symbol, or pattern found across literature and cultures, and the hero’s journey traces a protagonist’s call to adventure, trials, and eventual transformation.',
  [('What is an archetype?', ['A recurring character, symbol, or pattern found across literature and cultures', 'A single unique word invented by one author', 'A concept unrelated to reading', 'A type of punctuation mark'], 0),
   ('What does the hero’s journey typically trace?', ['A protagonist’s call to adventure, trials, and eventual transformation', 'A list of unrelated historical dates', 'A concept unrelated to literature', 'A story with no central character at all'], 0),
   ('Is the wise mentor a commonly recognized archetype in literature?', ['Yes', 'No, mentors never appear as a recurring archetype', 'A concept unrelated to archetypes', 'Archetypes never include any character roles'], 0),
   ('Why might recognizing an archetype help a reader predict how a character or story might develop?', ['Familiar patterns across many stories can suggest likely roles, conflicts, or outcomes for that type of character', 'Archetypes never provide any useful insight into how a story might unfold', 'This concept has no connection to reading', 'Every archetype behaves in a completely unpredictable, unique way each time'], 0),
   ('Why do archetypes and the hero’s journey appear across many different cultures and time periods?', ['They reflect universal human experiences and values that resonate across different societies', 'Archetypes only ever appear in one single culture and never anywhere else', 'This concept has no relevance to literature', 'The hero’s journey was invented recently and has no connection to older traditions'], 0)]),
M('Analytic Geometry: Introduction to Conic Sections (Ellipses and Hyperbolas)',
  'Grade 10 Math strand: conic sections are curves formed by slicing a cone, including circles, ellipses, parabolas, and hyperbolas, each with a distinct equation and shape.',
  [('What are conic sections?', ['Curves formed by slicing a cone, including circles, ellipses, parabolas, and hyperbolas', 'A type of algebraic expression with no geometric meaning', 'A concept unrelated to geometry', 'Only straight lines drawn on a graph'], 0),
   ('What shape does an ellipse resemble?', ['A stretched or squashed circle', 'A single straight line', 'A concept unrelated to conic sections', 'Two separate curves opening away from each other'], 0),
   ('Does a hyperbola consist of two separate curves opening in opposite directions?', ['Yes', 'No, a hyperbola is always a single closed curve', 'A concept unrelated to hyperbolas', 'A hyperbola is identical in shape to a circle'], 0),
   ('Why is it useful to recognize which conic section an equation represents before graphing it?', ['Identifying the conic type reveals its general shape and key features, making an accurate sketch much easier', 'The type of conic section never affects how an equation should be graphed', 'This concept has no connection to math', 'All conic sections are graphed using the exact same method regardless of type'], 0),
   ('Why do engineers and astronomers find ellipses and hyperbolas useful for modelling real-world phenomena, such as planetary orbits?', ['These curves accurately describe many natural paths and shapes, including the elliptical orbits of planets', 'Ellipses and hyperbolas have no real-world applications outside of pure mathematics', 'This concept has no relevance to geometry', 'Planetary orbits are always perfectly circular, never elliptical'], 0)]),
Sc('Chemistry: Percent Yield and Limiting Reagents',
   'Grade 10 Science strand: the limiting reagent in a reaction is used up first and determines the maximum possible product, while percent yield compares the actual product obtained to the theoretical amount predicted.',
   [('What does the limiting reagent in a chemical reaction determine?', ['The maximum amount of product that can be formed', 'The colour of the final product', 'A concept unrelated to chemistry', 'The temperature at which the reaction occurs'], 0),
    ('What does percent yield compare?', ['The actual product obtained to the theoretical amount predicted', 'The mass of reactants only', 'A concept unrelated to percent yield', 'The number of atoms in a single molecule'], 0),
    ('Is the limiting reagent the reactant that runs out first in a chemical reaction?', ['Yes', 'No, the limiting reagent is never used up first', 'A concept unrelated to limiting reagents', 'All reactants are always used up at exactly the same time'], 0),
    ('Why is a percent yield of less than 100 percent common in real laboratory experiments?', ['Factors such as incomplete reactions, side reactions, or loss of product during handling often reduce the actual yield', 'Real experiments always produce exactly the theoretical yield predicted by calculations', 'This concept has no connection to chemistry', 'Percent yield is never affected by anything that happens during an experiment'], 0),
    ('Why must the limiting reagent be identified before calculating a reaction’s theoretical yield?', ['The limiting reagent determines the maximum amount of product possible, so calculations based on the excess reagent would overestimate the yield', 'The limiting reagent has no effect on the theoretical yield calculation', 'This concept has no relevance to chemistry', 'Theoretical yield can always be calculated without knowing which reagent is limiting'], 0)]),
H('The War of 1812 and the Defence of British North America',
  'Grade 10 History strand: the War of 1812 between the United States and Britain, fought partly on Canadian soil from 1812 to 1814, involved British, Canadian militia, and Indigenous allies defending British North America from American invasion.',
  [('Between which two countries was the War of 1812 primarily fought?', ['The United States and Britain', 'A concept unrelated to Canadian history', 'France and Britain', 'Canada and the United States, acting entirely alone'], 0),
   ('Where was much of the War of 1812 fought?', ['On Canadian soil', 'Entirely in Europe', 'A concept unrelated to the War of 1812', 'Entirely at sea, with no land battles at all'], 0),
   ('Did Indigenous allies, such as those led by Tecumseh, play a role in defending British North America during the war?', ['Yes', 'No, Indigenous peoples played no role in the war at all', 'A concept unrelated to the War of 1812', 'Indigenous nations only fought on the American side'], 0),
   ('Why might the successful defence of British North America during the War of 1812 have contributed to a growing sense of colonial identity?', ['Repelling an American invasion together gave settlers, militia, and Indigenous allies a shared experience of defending their home territory', 'The war had no effect on colonial identity in British North America', 'This concept has no relevance to Canadian history', 'The war ended in a decisive American conquest of all of British North America'], 0),
   ('Why is the War of 1812 often described as an important early chapter in the story of Canadian nationhood?', ['It is remembered as a formative moment when the colonies successfully resisted annexation, later linked to a growing distinct identity', 'The War of 1812 has no connection to later Canadian history', 'This concept has no relevance to history', 'Canada did not exist in any form before or after the War of 1812'], 0)]),
]),

day(102, [
E('Literature: The Gothic Tradition in Fiction',
  'Grade 10 English strand: Gothic fiction combines elements of horror, romance, and the supernatural, typically featuring dark or decaying settings, mystery, and a mood of dread or suspense.',
  [('What mood does Gothic fiction typically create?', ['Dread or suspense', 'Light-hearted comedy with no tension at all', 'A concept unrelated to literature', 'Complete calm with no conflict present'], 0),
   ('What kind of setting is commonly associated with Gothic fiction?', ['A dark or decaying setting, such as an old mansion or castle', 'A brightly lit modern shopping mall', 'A concept unrelated to Gothic fiction', 'A setting with no description at all'], 0),
   ('Does Gothic fiction often include supernatural or mysterious elements?', ['Yes', 'No, Gothic fiction never includes supernatural elements', 'A concept unrelated to Gothic fiction', 'Supernatural elements are exclusive to science fiction, not Gothic fiction'], 0),
   ('Why might an author choose a decaying, isolated setting for a Gothic story?', ['Such settings can reinforce feelings of unease, mystery, and psychological tension central to the genre', 'The setting of a Gothic story never affects its mood or tension', 'This concept has no connection to literature', 'Gothic stories are always set in cheerful, well-maintained modern settings'], 0),
   ('Why has the Gothic tradition remained influential in later genres such as horror and psychological thriller fiction?', ['Its focus on atmosphere, dread, and the unknown continues to shape how later writers build suspense and unease', 'The Gothic tradition has had no lasting influence on any later genre', 'This concept has no relevance to literature', 'Horror and psychological thriller fiction developed with no connection to earlier Gothic conventions'], 0)]),
M('Trigonometry: Sum and Difference Identities',
  'Grade 10 Math strand: sum and difference identities express trigonometric functions of the sum or difference of two angles, such as sin(A+B) equals sin(A)cos(B) plus cos(A)sin(B), in terms of the original angles.',
  [('What do sum and difference identities express?', ['Trigonometric functions of the sum or difference of two angles', 'Only the value of a single angle', 'A concept unrelated to trigonometry', 'The area of a triangle'], 0),
   ('What is the identity for sin(A+B)?', ['sin(A)cos(B) + cos(A)sin(B)', 'sin(A) + sin(B)', 'sin(A)cos(B) - cos(A)sin(B)', 'cos(A)cos(B) - sin(A)sin(B)'], 0),
   ('Can sum and difference identities help evaluate the exact trigonometric value of an angle like 75 degrees, using 45 and 30 degrees?', ['Yes', 'No, sum and difference identities never help evaluate exact trigonometric values', 'A concept unrelated to sum and difference identities', 'Only a calculator can ever find such a value, with no formula available'], 0),
   ('Why are sum and difference identities useful when a trigonometric equation involves an angle that is not a common reference angle?', ['They allow an uncommon angle to be rewritten as a sum or difference of angles with known exact trigonometric values', 'These identities never help simplify equations involving uncommon angles', 'This concept has no connection to math', 'Every angle already has a memorized exact trigonometric value without needing any identity'], 0),
   ('Why are sum and difference identities considered a foundation for deriving other identities, such as the double-angle formulas?', ['Setting the two angles equal to each other in a sum identity directly produces the corresponding double-angle formula', 'Sum and difference identities have no mathematical connection to double-angle formulas', 'This concept has no relevance to trigonometry', 'Double-angle formulas were developed with no connection to any other identity'], 0)]),
Sc('Biology: The Skeletal and Muscular Systems',
   'Grade 10 Science strand: the skeletal system provides structure, protection, and support through bones and joints, while the muscular system works with the skeleton to produce movement through contraction.',
   [('What does the skeletal system provide the body?', ['Structure, protection, and support', 'Only colour and texture', 'A concept unrelated to biology', 'Digestive enzymes'], 0),
    ('How do muscles typically produce movement?', ['By contracting', 'By dissolving completely', 'A concept unrelated to the muscular system', 'By absorbing nutrients directly from food'], 0),
    ('Do bones meet at joints to allow for movement?', ['Yes', 'No, joints never allow for any movement', 'A concept unrelated to the skeletal system', 'Bones never connect to one another in the body'], 0),
    ('Why do the skeletal and muscular systems need to work together to produce movement?', ['Muscles provide the contracting force, while bones and joints act as the levers and pivot points that movement requires', 'The skeletal and muscular systems function completely independently with no interaction at all', 'This concept has no connection to biology', 'Movement occurs with no involvement from either the skeletal or muscular system'], 0),
    ('Why might a fracture in a major bone significantly limit a person’s ability to move a limb, even if the surrounding muscles are healthy?', ['Muscles rely on a stable, intact bone structure to act as a lever, so a break disrupts the mechanical system needed for movement', 'A bone fracture never has any effect on a person’s ability to move a limb', 'This concept has no relevance to biology', 'Muscles can produce normal movement entirely independently of bone structure'], 0)]),
H('The Rebellions of 1837-38 in Upper and Lower Canada',
  'Grade 10 History strand: the Rebellions of 1837-38, led by figures such as William Lyon Mackenzie in Upper Canada and Louis-Joseph Papineau in Lower Canada, protested against the undemocratic control of colonial government by a small elite.',
  [('Who led the rebellion in Upper Canada in 1837?', ['William Lyon Mackenzie', 'A concept unrelated to Canadian history', 'A figure with no connection to Upper Canada', 'A British monarch'], 0),
   ('Who led the rebellion in Lower Canada in 1837?', ['Louis-Joseph Papineau', 'A concept unrelated to the rebellions', 'A figure with no connection to Lower Canada', 'An American general'], 0),
   ('Were the rebels protesting against undemocratic control of colonial government by a small elite?', ['Yes', 'No, the rebels had no complaints about colonial government at all', 'A concept unrelated to the Rebellions of 1837-38', 'The rebellions had no connection to how the colonies were governed'], 0),
   ('Why might frustration with a small, unelected elite controlling government decisions have led reformers to consider rebellion?', ['Many colonists felt they had little real political voice despite paying taxes and living under laws they could not influence', 'Colonists in Upper and Lower Canada had no grievances about how they were governed', 'This concept has no relevance to Canadian history', 'The rebellions occurred with no connection to any political grievance'], 0),
   ('Why are the Rebellions of 1837-38 often linked to the later development of responsible government in Canada?', ['Although the rebellions themselves failed, they helped prompt a British review of colonial governance that eventually led to reform', 'The rebellions have no connection to any later political changes in the colonies', 'This concept has no relevance to history', 'Responsible government was established with no connection to earlier unrest'], 0)]),
]),

day(103, [
E('Writing: The Feature Article',
  'Grade 10 English strand: a feature article explores a topic in greater depth than a straight news report, often combining research, interviews, and narrative techniques to engage and inform readers.',
  [('How does a feature article typically differ from a straight news report?', ['It explores a topic in greater depth, often combining research, interviews, and narrative techniques', 'It contains no factual information whatsoever', 'A concept unrelated to writing', 'It is always shorter than a news report'], 0),
   ('Might a feature article include an interview with someone connected to its topic?', ['Yes', 'No, feature articles never include interviews', 'A concept unrelated to feature articles', 'Interviews are only used in fiction writing'], 0),
   ('Why might a feature writer open with an anecdote about a specific person before presenting broader facts on a topic?', ['A personal story can draw readers in emotionally before introducing wider context and information', 'Opening with an anecdote never has any effect on how readers engage with an article', 'This concept has no connection to writing', 'Feature articles should always begin with a list of statistics and nothing else'], 0),
   ('Which of these best reflects the tone of a feature article, compared to a brief news brief?', ['A longer, more descriptive piece exploring the human impact of a local recycling program through interviews and detail.', 'A single sentence reporting only the date of an event.', 'A list of numbers with no explanation.', 'A one-line weather update with no elaboration.'], 0),
   ('Why is thorough research especially important when writing a feature article on a complex or sensitive topic?', ['Well-researched, accurate information builds credibility and ensures the article fairly represents the topic', 'Research is never necessary when writing a feature article', 'This concept has no relevance to writing', 'A feature article can rely entirely on the writer’s personal opinion with no research at all'], 0)]),
M('Statistics: Sampling Methods and Bias in Data Collection',
  'Grade 10 Math strand: a sample is a subset of a population used to make inferences about the whole, and sampling methods such as random, stratified, or convenience sampling can introduce different types of bias if not carefully designed.',
  [('What is a sample in statistics?', ['A subset of a population used to make inferences about the whole', 'The entire population being studied', 'A concept unrelated to statistics', 'A single number with no connection to a population'], 0),
   ('Name one type of sampling method, such as random sampling.', ['Random sampling', 'A concept unrelated to sampling methods', 'Guessing without any method', 'Ignoring the population entirely'], 0),
   ('Can a poorly designed sampling method introduce bias into collected data?', ['Yes', 'No, sampling methods never introduce bias', 'A concept unrelated to sampling bias', 'Bias can only occur when studying an entire population, never a sample'], 0),
   ('Why might convenience sampling, such as surveying only people at a single mall, lead to biased results about an entire city?', ['The sample may not represent the diversity of opinions, backgrounds, or locations found across the whole city', 'Convenience sampling always produces results identical to studying the entire population', 'This concept has no connection to statistics', 'Sampling method never has any effect on how representative collected data is'], 0),
   ('Why is stratified sampling, which divides a population into subgroups before sampling, sometimes preferred over simple random sampling?', ['It can help ensure that important subgroups within a population are proportionally represented in the sample', 'Stratified sampling never provides any advantage over other sampling methods', 'This concept has no relevance to statistics', 'Subgroups within a population never need to be considered when designing a sample'], 0)]),
Sc('Physics: Momentum and Collisions',
   'Grade 10 Science strand: momentum is the product of an object’s mass and velocity, and in a closed system, total momentum is conserved before and after a collision.',
   [('How is momentum calculated?', ['Mass multiplied by velocity', 'Mass divided by velocity', 'A concept unrelated to physics', 'Velocity multiplied by time only'], 0),
    ('In a closed system, is total momentum conserved before and after a collision?', ['Yes', 'No, momentum is never conserved in any collision', 'A concept unrelated to momentum', 'Momentum conservation only applies to objects at rest'], 0),
    ('Which quantity increases an object’s momentum if its velocity is doubled while its mass stays the same?', ['Momentum doubles as well', 'Momentum stays exactly the same', 'A concept unrelated to momentum', 'Momentum decreases by half'], 0),
    ('Why is momentum conservation useful for analyzing what happens when two vehicles collide?', ['It allows the combined motion after the collision to be predicted using only the masses and velocities before the collision', 'Momentum conservation never provides any useful information about a collision', 'This concept has no connection to physics', 'Vehicle collisions cannot be analyzed using any physical law'], 0),
    ('Why do collision safety features like crumple zones and airbags help reduce injury, in terms of momentum and force?', ['They extend the time over which momentum changes during a collision, reducing the force experienced by passengers', 'Crumple zones and airbags have no connection to the physics of a collision', 'This concept has no relevance to physics', 'The force experienced in a collision never depends on the time over which momentum changes'], 0)]),
H('The Durham Report and the Rise of Responsible Government',
  'Grade 10 History strand: Lord Durham’s 1839 report, written in response to the Rebellions of 1837-38, recommended uniting Upper and Lower Canada and introducing responsible government, in which the executive is accountable to elected representatives.',
  [('What event prompted Lord Durham to write his 1839 report?', ['The Rebellions of 1837-38', 'A concept unrelated to Canadian history', 'A war with the United States', 'A dispute over the national anthem'], 0),
   ('What form of government did the Durham Report recommend?', ['Responsible government, where the executive is accountable to elected representatives', 'A monarchy with no elected representatives at all', 'A concept unrelated to the Durham Report', 'A government with no connection to elections'], 0),
   ('Did the Durham Report recommend uniting Upper and Lower Canada?', ['Yes', 'No, it recommended keeping them permanently separate', 'A concept unrelated to the Durham Report', 'Uniting the two colonies was never proposed by anyone'], 0),
   ('Why might responsible government have addressed some of the grievances that led to the Rebellions of 1837-38?', ['It gave elected representatives real accountability over the executive, addressing complaints about a small, unaccountable elite', 'Responsible government had no connection to the grievances that caused the rebellions', 'This concept has no relevance to Canadian history', 'The rebellions had nothing to do with how the colonies were governed'], 0),
   ('Why is the Durham Report often considered a turning point in the development of Canadian self-government?', ['It set in motion reforms that gradually shifted political power from an appointed elite toward elected representatives', 'The Durham Report had no lasting influence on the development of Canadian government', 'This concept has no relevance to history', 'Canadian self-government developed with no connection to any earlier report or reform'], 0)]),
]),

day(104, [
E('Grammar: Commonly Confused Words and Word Choice',
  'Grade 10 English strand: precise word choice requires distinguishing between commonly confused words, such as affect and effect or its and it’s, to communicate meaning clearly and accurately.',
  [('Why is distinguishing between commonly confused words, like affect and effect, important in writing?', ['It helps communicate meaning clearly and accurately', 'It has no impact on how clearly a piece of writing communicates', 'A concept unrelated to grammar', 'Confused words are always interchangeable with no difference in meaning'], 0),
   ('Which sentence uses its and it’s correctly?', ['The dog wagged its tail because it’s excited to see you.', 'The dog wagged it’s tail because its excited to see you.', 'The dog wagged its tail because its excited to see you.', 'The dog wagged it’s tail because it’s excited to see you.'], 0),
   ('Does effect typically function as a noun, while affect typically functions as a verb?', ['Yes', 'No, affect and effect always mean exactly the same thing', 'A concept unrelated to commonly confused words', 'Effect is always a verb and affect is always a noun'], 0),
   ('Why might a reader be confused if a writer mixes up their, there, and they’re throughout a piece of writing?', ['Each word has a distinct meaning and grammatical function, so swapping them can obscure the intended meaning', 'These three words are always completely interchangeable with no risk of confusion', 'This concept has no connection to writing', 'Readers never notice or care about word choice errors like this'], 0),
   ('Why is proofreading specifically for commonly confused words an important step in the writing process?', ['Spell-check often does not catch these errors, since the misused word is usually spelled correctly, just used incorrectly', 'Spell-check always catches every commonly confused word automatically', 'This concept has no relevance to writing', 'Proofreading has no effect on catching this type of error'], 0)]),
M('Probability: The Binomial Probability Distribution',
  'Grade 10 Math strand: a binomial probability distribution models the number of successes in a fixed number of independent trials, each with the same probability of success, such as repeated coin flips.',
  [('What does a binomial probability distribution model?', ['The number of successes in a fixed number of independent trials', 'The average of a single continuous measurement', 'A concept unrelated to probability', 'A relationship between two unrelated variables'], 0),
   ('In a binomial setting, must each trial have the same probability of success?', ['Yes', 'No, each trial’s probability of success is always different', 'A concept unrelated to binomial distributions', 'Probability of success never applies to a binomial trial'], 0),
   ('Which of these is a classic example of a binomial experiment?', ['Flipping a fair coin 10 times and counting the number of heads', 'Measuring the exact height of every student in a class', 'A concept unrelated to binomial distributions', 'Recording the colour of a single object one time only'], 0),
   ('Why must the trials in a binomial distribution be independent of one another?', ['Independence ensures the outcome of one trial does not change the probability of success on another trial, keeping the model accurate', 'Independence between trials has no effect on whether a binomial model applies', 'This concept has no connection to math', 'A binomial distribution can be applied even when one trial always determines the outcome of the next'], 0),
   ('Why is the binomial distribution useful for quality control, such as estimating the number of defective items in a batch?', ['It allows a company to estimate the probability of a certain number of defects, given a known defect rate and sample size', 'The binomial distribution has no application to quality control processes', 'This concept has no relevance to probability', 'Defect rates can never be modelled using any probability distribution'], 0)]),
Sc('Earth Science: The Nitrogen Cycle',
   'Grade 10 Science strand: the nitrogen cycle describes how nitrogen moves between the atmosphere, soil, and living organisms through processes such as nitrogen fixation, nitrification, and denitrification.',
   [('What does the nitrogen cycle describe?', ['How nitrogen moves between the atmosphere, soil, and living organisms', 'How electricity flows through a circuit', 'A concept unrelated to earth science', 'How rocks form deep underground only'], 0),
    ('Name one process involved in the nitrogen cycle, such as nitrogen fixation.', ['Nitrogen fixation', 'A concept unrelated to the nitrogen cycle', 'Photosynthesis only', 'Refraction'], 0),
    ('Do certain bacteria convert atmospheric nitrogen into a form plants can use during nitrogen fixation?', ['Yes', 'No, bacteria play no role in the nitrogen cycle', 'A concept unrelated to nitrogen fixation', 'Plants absorb atmospheric nitrogen directly with no help from bacteria'], 0),
    ('Why is nitrogen fixation an essential step in the nitrogen cycle, given that most organisms cannot use atmospheric nitrogen directly?', ['It converts nitrogen gas into a chemical form that plants can absorb and use to build proteins and other molecules', 'Nitrogen fixation has no connection to how plants obtain nitrogen', 'This concept has no connection to earth science', 'All organisms can absorb atmospheric nitrogen gas directly without any conversion'], 0),
    ('Why might excessive use of nitrogen-based fertilizers disrupt the natural balance of the nitrogen cycle in nearby ecosystems?', ['Excess nitrogen can run off into waterways, causing algal blooms and other ecological imbalances', 'Fertilizer use never has any effect on the nitrogen cycle or nearby ecosystems', 'This concept has no relevance to earth science', 'The nitrogen cycle is entirely unaffected by any human agricultural activity'], 0)]),
H('The Road to Confederation: The Charlottetown and Quebec Conferences',
  'Grade 10 History strand: the Charlottetown Conference of 1864 and the Quebec Conference of 1864 brought together colonial leaders to negotiate the terms of a union that would become Canada in 1867.',
  [('In what year did the Charlottetown and Quebec Conferences take place?', ['1864', 'A concept unrelated to Canadian history', '1812', '1900'], 0),
   ('What did the conferences of 1864 negotiate the terms of?', ['A union of British North American colonies that would become Canada', 'A trade agreement with France', 'A concept unrelated to Confederation', 'A treaty ending a war with the United States'], 0),
   ('Did colonial leaders meet at these conferences to discuss uniting several colonies?', ['Yes', 'No, the conferences had no connection to uniting the colonies', 'A concept unrelated to the Charlottetown and Quebec Conferences', 'The colonies were already fully united before these meetings took place'], 0),
   ('Why might colonial leaders have seen practical advantages, such as economic and defence benefits, in uniting into a larger union?', ['A larger union could build stronger infrastructure, trade networks, and a more coordinated defence than separate small colonies', 'Uniting into a larger colony offered no practical advantages to colonial leaders at the time', 'This concept has no relevance to Canadian history', 'Individual colonies were always more secure and prosperous than a united one'], 0),
   ('Why are the Charlottetown and Quebec Conferences considered foundational events leading to Confederation in 1867?', ['The discussions and resolutions from these conferences formed the basis for the terms eventually written into the British North America Act', 'These conferences had no connection to the eventual creation of Canada in 1867', 'This concept has no relevance to history', 'Confederation in 1867 occurred with no prior negotiation among colonial leaders'], 0)]),
]),

day(105, [
E('Oral Communication: The Job Interview',
  'Grade 10 English strand: preparing for a job interview involves researching the employer, anticipating common questions, and communicating clearly and confidently about one’s skills and experience.',
  [('What is one important step in preparing for a job interview?', ['Researching the employer', 'Arriving without any preparation at all', 'A concept unrelated to oral communication', 'Avoiding eye contact throughout the interview'], 0),
   ('Should a candidate typically anticipate and prepare for common interview questions?', ['Yes', 'No, preparing for common questions never helps in an interview', 'A concept unrelated to job interviews', 'Interview questions are always completely unpredictable and impossible to anticipate'], 0),
   ('Why might practising answers to common interview questions out loud improve a candidate’s performance?', ['Practising helps a candidate speak more clearly, confidently, and concisely when the actual interview happens', 'Practising answers out loud never has any effect on interview performance', 'This concept has no connection to oral communication', 'Candidates should always read their answers directly from a script during the interview'], 0),
   ('Which of these best reflects an effective way to answer a job interview question about a challenge you overcame?', ['Describing a specific situation, the actions you took, and the positive result, using clear and concise language.', 'Giving a vague one-word answer with no explanation at all.', 'Talking only about a coworker’s unrelated problem.', 'Refusing to answer the question at all.'], 0),
   ('Why is researching an employer beforehand considered a valuable interview preparation strategy?', ['It allows a candidate to tailor their answers and ask informed questions that show genuine interest in the role', 'Researching an employer never provides any advantage in a job interview', 'This concept has no relevance to oral communication', 'Employers never expect candidates to know anything about the company beforehand'], 0)]),
M('Matrices: Applications to Geometric Transformations',
  'Grade 10 Math strand: transformation matrices can represent geometric operations such as rotations, reflections, and scaling, which are applied to coordinate points through matrix multiplication.',
  [('What can transformation matrices represent?', ['Geometric operations such as rotations, reflections, and scaling', 'Only the temperature of a physical object', 'A concept unrelated to matrices', 'A single fixed number with no geometric meaning'], 0),
   ('How is a transformation matrix typically applied to a coordinate point?', ['Through matrix multiplication', 'By adding the point to a random number', 'A concept unrelated to transformation matrices', 'By ignoring the coordinates entirely'], 0),
   ('Can a scaling matrix be used to enlarge or shrink a shape on a coordinate plane?', ['Yes', 'No, scaling matrices never affect the size of a shape', 'A concept unrelated to transformation matrices', 'Scaling matrices only affect the colour of a shape'], 0),
   ('Why might representing a rotation as a matrix be useful when applying the same rotation to many different points?', ['The same transformation matrix can be multiplied by each point’s coordinates, applying the rotation consistently and efficiently', 'Representing a rotation as a matrix never simplifies applying it to multiple points', 'This concept has no connection to math', 'Each point would need a completely different, unrelated calculation method'], 0),
   ('Why are transformation matrices considered valuable tools in fields like computer graphics and animation?', ['They allow complex sequences of rotations, reflections, and scalings to be combined and applied efficiently to digital objects', 'Transformation matrices have no application outside of pure mathematics', 'This concept has no relevance to matrices', 'Computer graphics never involve any geometric transformations'], 0)]),
Sc('Biology: Plant Reproduction and Pollination',
   'Grade 10 Science strand: flowering plants reproduce sexually through pollination, where pollen is transferred from the male anther to the female stigma, often with the help of pollinators such as bees.',
   [('What is pollination?', ['The transfer of pollen from the male anther to the female stigma', 'The process of a plant absorbing water through its roots', 'A concept unrelated to biology', 'The process of a leaf changing colour in fall'], 0),
    ('Name one common pollinator, such as bees.', ['Bees', 'A concept unrelated to pollination', 'Rocks', 'Clouds'], 0),
    ('Can pollinators like bees help transfer pollen between flowers?', ['Yes', 'No, pollinators play no role in pollination', 'A concept unrelated to plant reproduction', 'Pollen is never transferred between flowers by any organism'], 0),
    ('Why might a decline in pollinator populations, such as bees, threaten the reproduction of many flowering plant species?', ['Many flowering plants rely on pollinators to transfer pollen for fertilization, so fewer pollinators can reduce successful reproduction', 'Pollinator populations have no connection to how flowering plants reproduce', 'This concept has no connection to biology', 'Flowering plants can always reproduce successfully with no pollinators present'], 0),
    ('Why do many flowers have bright colours and strong scents, in terms of their reproductive strategy?', ['These features attract pollinators, increasing the chances that pollen will be transferred between flowers for successful reproduction', 'Bright colours and scents have no connection to a flower’s reproductive success', 'This concept has no relevance to biology', 'Flower colour and scent are entirely random with no functional purpose'], 0)]),
H('United Empire Loyalists and the Settlement of British North America',
  'Grade 10 History strand: United Empire Loyalists, colonists who remained loyal to Britain during the American Revolution, migrated north into British North America in the 1780s, shaping the settlement and development of regions including Ontario and New Brunswick.',
  [('Who were the United Empire Loyalists?', ['Colonists who remained loyal to Britain during the American Revolution', 'A concept unrelated to Canadian history', 'A group with no connection to the American Revolution', 'Soldiers from France who settled in Quebec'], 0),
   ('When did the Loyalists largely migrate to British North America?', ['In the 1780s', 'A concept unrelated to the Loyalists', 'In the 1950s', 'Before Confederation had any colonies at all'], 0),
   ('Did the Loyalists’ settlement significantly shape the development of regions including Ontario and New Brunswick?', ['Yes', 'No, the Loyalists had no lasting effect on any Canadian region', 'A concept unrelated to United Empire Loyalists', 'Ontario and New Brunswick were fully settled long before the Loyalists arrived'], 0),
   ('Why might tens of thousands of Loyalists choosing to migrate north have significantly increased the population of British North America?', ['A large, organized wave of settlers arriving at once substantially added to the existing colonial population', 'Loyalist migration had no measurable effect on the population of British North America', 'This concept has no relevance to Canadian history', 'The Loyalists represented only a handful of individuals with no real impact'], 0),
   ('Why is Loyalist settlement often studied as a key factor in the early development of English-speaking communities in Canada?', ['Loyalist communities established new towns, institutions, and a lasting cultural presence in regions like Ontario and the Maritimes', 'Loyalist settlement had no connection to the development of English-speaking communities in Canada', 'This concept has no relevance to history', 'English-speaking communities in Canada developed with no connection to Loyalist migration'], 0)]),
]),

day(106, [
E('Reading: Analyzing Allegory and Fable',
  'Grade 10 English strand: an allegory is a narrative in which characters and events represent broader ideas or moral lessons, while a fable is a brief allegorical story, often featuring animals, that teaches a specific moral.',
  [('What do the characters and events in an allegory typically represent?', ['Broader ideas or moral lessons', 'Only literal, unrelated events with no deeper meaning', 'A concept unrelated to reading', 'A random collection of unconnected facts'], 0),
   ('What does a fable typically teach?', ['A specific moral lesson', 'Only historical facts with no lesson at all', 'A concept unrelated to fables', 'Nothing at all; fables have no purpose'], 0),
   ('Do fables often feature animals that behave and speak like humans?', ['Yes', 'No, fables never feature animals of any kind', 'A concept unrelated to fables', 'Fables exclusively feature only human characters'], 0),
   ('Why might a writer use an allegory instead of stating a moral or political idea directly?', ['A narrative can make an abstract idea more engaging, memorable, and open to interpretation than a direct statement', 'An allegory never communicates any idea more effectively than a direct statement', 'This concept has no connection to reading', 'Allegories are always less effective than simply stating an idea directly'], 0),
   ('Why is recognizing the symbolic layer of an allegory important for fully understanding a text like Animal Farm?', ['Without recognizing the symbolic representation of real people or events, a reader would miss the story’s deeper intended meaning', 'The symbolic layer of an allegory never adds anything to a reader’s understanding of a text', 'This concept has no relevance to reading comprehension', 'Every allegory is intended to be understood only on a purely literal level'], 0)]),
M('Calculus Foundations: Introduction to the Derivative and the Power Rule',
  'Grade 10 Math strand: the derivative of a function represents its instantaneous rate of change, and the power rule provides a shortcut for finding derivatives of functions in the form x to the power of n.',
  [('What does the derivative of a function represent?', ['Its instantaneous rate of change', 'The total area under its graph', 'A concept unrelated to calculus', 'The exact value of the function at x equals zero only'], 0),
   ('According to the power rule, what is the derivative of x cubed?', ['3x squared', 'x squared', 'A concept unrelated to the power rule', '3x'], 0),
   ('Does the power rule provide a shortcut for finding derivatives of functions like x to the power of n?', ['Yes', 'No, the power rule has no connection to finding derivatives', 'A concept unrelated to derivatives', 'The power rule only applies to functions with no exponents at all'], 0),
   ('Why is understanding instantaneous rate of change useful for describing the speed of a moving object at a single exact moment?', ['The derivative gives the exact rate of change at one instant, unlike an average rate calculated over an interval of time', 'Instantaneous rate of change has no connection to describing the motion of an object', 'This concept has no connection to math', 'Average rate of change and instantaneous rate of change always give identical results'], 0),
   ('Why is the power rule considered a foundational tool before studying more advanced calculus techniques?', ['It provides an efficient, reliable method for differentiating a wide range of polynomial functions used throughout calculus', 'The power rule has no practical use in later calculus topics', 'This concept has no relevance to calculus', 'Polynomial functions can never be differentiated using any consistent rule'], 0)]),
Sc('Physics: Calorimetry and Specific Heat Capacity',
   'Grade 10 Science strand: specific heat capacity is the amount of energy needed to raise the temperature of one gram of a substance by one degree Celsius, and calorimetry uses this concept to measure heat transfer between substances.',
   [('What does specific heat capacity measure?', ['The energy needed to raise the temperature of one gram of a substance by one degree Celsius', 'The total mass of a substance', 'A concept unrelated to physics', 'The colour of a substance when heated'], 0),
    ('What is calorimetry used to measure?', ['Heat transfer between substances', 'The electrical charge of an object', 'A concept unrelated to calorimetry', 'The exact chemical formula of a compound'], 0),
    ('Does water have a relatively high specific heat capacity compared to many other common substances?', ['Yes', 'No, water has an unusually low specific heat capacity', 'A concept unrelated to specific heat capacity', 'Specific heat capacity does not apply to water at all'], 0),
    ('Why does a substance with a high specific heat capacity, like water, take longer to heat up than a substance with a lower specific heat capacity?', ['More energy is required to raise its temperature by the same amount, so it absorbs more heat before its temperature changes noticeably', 'Specific heat capacity has no effect on how quickly a substance heats up', 'This concept has no connection to physics', 'All substances require exactly the same amount of energy to raise their temperature by one degree'], 0),
    ('Why is water’s high specific heat capacity important for regulating coastal climates?', ['Large bodies of water absorb and release heat slowly, moderating nearby air temperatures throughout the seasons', 'Water’s specific heat capacity has no connection to regional climate patterns', 'This concept has no relevance to physics', 'Coastal climates are entirely unaffected by any property of nearby water'], 0)]),
H('The Numbered Treaties and Indigenous-Crown Relations',
  'Grade 10 History strand: the Numbered Treaties, signed between 1871 and 1921 between the Crown and Indigenous nations, addressed land, resources, and rights, though their terms have long been a source of dispute over interpretation and fulfillment.',
  [('Between which two parties were the Numbered Treaties signed?', ['The Crown and Indigenous nations', 'A concept unrelated to Canadian history', 'Two provincial governments', 'Canada and the United States'], 0),
   ('Over roughly what period were the Numbered Treaties signed?', ['1871 to 1921', 'A concept unrelated to the Numbered Treaties', '1600 to 1650', '1950 to 1970'], 0),
   ('Have the terms of the Numbered Treaties long been a source of dispute over interpretation and fulfillment?', ['Yes', 'No, the treaties have never been disputed in any way', 'A concept unrelated to the Numbered Treaties', 'Every treaty term has always been interpreted identically by all parties'], 0),
   ('Why might differing understandings of land, sovereignty, and treaty promises have led to long-standing disputes between Indigenous nations and the Crown?', ['Indigenous nations and government negotiators often had different oral and written understandings of what the treaties actually promised', 'There has never been any disagreement about the meaning of the Numbered Treaties', 'This concept has no relevance to Canadian history', 'All parties involved always agreed completely on every treaty term'], 0),
   ('Why is understanding the Numbered Treaties important for understanding present-day Indigenous rights and land claims discussions in Canada?', ['Many current legal and political discussions about land, resources, and rights are directly connected to how these historic treaties are interpreted today', 'The Numbered Treaties have no connection to any present-day discussion of Indigenous rights', 'This concept has no relevance to history', 'Indigenous rights and land claims issues have no historical basis at all'], 0)]),
]),

day(107, [
E('Literature: The Epic Hero and Epic Conventions',
  'Grade 10 English strand: an epic hero is a larger-than-life protagonist who undertakes a grand quest, often possessing exceptional strength or courage, within a narrative that follows established epic conventions.',
  [('What kind of protagonist is typically found at the centre of an epic?', ['A larger-than-life epic hero', 'A character with no notable traits at all', 'A concept unrelated to literature', 'A character who never faces any challenge'], 0),
   ('What does an epic hero typically undertake?', ['A grand quest', 'A short errand with no obstacles', 'A concept unrelated to epic conventions', 'An activity with no goal at all'], 0),
   ('Does an epic hero often possess exceptional strength or courage?', ['Yes', 'No, epic heroes are always ordinary in every way', 'A concept unrelated to epic heroes', 'Exceptional traits are never part of the epic hero convention'], 0),
   ('Why might ancient cultures have valued stories about epic heroes and their grand quests?', ['Such stories could reflect and reinforce a culture’s values, such as courage, honour, or loyalty', 'Epic hero stories never reflect or reinforce any cultural values', 'This concept has no connection to literature', 'Epic heroes were only ever created for pure entertainment with no cultural meaning'], 0),
   ('Why do epic conventions, such as invoking a muse or beginning in medias res, remain useful for identifying the epic genre today?', ['Recognizing these recurring structural and stylistic patterns helps readers identify and compare epics across different cultures and eras', 'Epic conventions never help readers identify or compare works within the epic genre', 'This concept has no relevance to literature', 'Every epic is written using a completely unique structure unrelated to any other epic'], 0)]),
M('Vectors: The Cross Product and Applications',
  'Grade 10 Math strand: the cross product of two three-dimensional vectors produces a new vector perpendicular to both original vectors, with a magnitude related to the area of the parallelogram they form.',
  [('What does the cross product of two vectors produce?', ['A new vector perpendicular to both original vectors', 'A single scalar number with no direction', 'A concept unrelated to vectors', 'The exact sum of the two original vectors'], 0),
   ('Does the cross product apply to two-dimensional or three-dimensional vectors?', ['Three-dimensional vectors', 'Only zero-dimensional points', 'A concept unrelated to cross products', 'Only vectors with a magnitude of exactly one'], 0),
   ('Is the magnitude of the cross product related to the area of the parallelogram formed by the two original vectors?', ['Yes', 'No, the magnitude of the cross product has no geometric meaning at all', 'A concept unrelated to the cross product', 'The cross product is always exactly zero regardless of the vectors used'], 0),
   ('Why is the cross product useful for finding a vector that is perpendicular to a surface defined by two other vectors?', ['Since the cross product is always perpendicular to both input vectors, it directly identifies a normal direction to that surface', 'The cross product never produces a vector that is perpendicular to anything', 'This concept has no connection to math', 'Perpendicular vectors can never be found using vector operations'], 0),
   ('Why might the cross product be a useful tool in physics for calculating torque, given a force applied at a distance from a pivot point?', ['Torque depends on both the magnitude of the force and its perpendicular relationship to the position vector, which the cross product captures', 'The cross product has no application to calculating torque in physics', 'This concept has no relevance to vectors', 'Torque can never be calculated using any vector operation'], 0)]),
Sc('Chemistry: Naming Ionic and Molecular Compounds',
   'Grade 10 Science strand: ionic compounds are named using the cation followed by the anion, often with a suffix such as -ide, while molecular compounds use prefixes such as mono-, di-, and tri- to indicate the number of atoms.',
   [('How are ionic compounds typically named?', ['Using the cation followed by the anion, often ending in -ide', 'Using only Roman numerals with no other words', 'A concept unrelated to chemistry', 'Using the compound’s exact colour'], 0),
    ('What kind of prefixes are used in naming molecular compounds, such as carbon dioxide?', ['Prefixes such as mono-, di-, and tri- to indicate the number of atoms', 'Prefixes indicating the compound’s temperature', 'A concept unrelated to naming compounds', 'No prefixes are ever used for molecular compounds'], 0),
    ('Is sodium chloride an example of an ionic compound?', ['Yes', 'No, sodium chloride is never considered an ionic compound', 'A concept unrelated to naming compounds', 'Ionic compounds never involve sodium or chlorine'], 0),
    ('Why is a consistent naming system important when communicating about chemical compounds?', ['It allows scientists worldwide to identify the exact composition of a compound from its name alone, avoiding confusion', 'A consistent naming system has no benefit for scientific communication', 'This concept has no connection to chemistry', 'Chemical compounds can always be identified without any naming system at all'], 0),
    ('Why does the naming convention differ between ionic compounds and molecular compounds, such as using prefixes only for molecular compounds?', ['Molecular compounds can form in multiple ratios of the same elements, so prefixes are needed to distinguish them, unlike most ionic compounds', 'There is no actual difference between how ionic and molecular compounds are named', 'This concept has no relevance to chemistry', 'Prefixes are used identically for both ionic and molecular compound names'], 0)]),
H('The Acadian Expulsion (Le Grand Dérangement)',
  'Grade 10 History strand: the Acadian Expulsion of 1755, ordered by British colonial authorities, forcibly removed thousands of French-speaking Acadians from their homes in the Maritimes, scattering families and causing lasting hardship.',
  [('In what year did the British order the expulsion of the Acadians?', ['1755', 'A concept unrelated to Canadian history', '1867', '1900'], 0),
   ('Who ordered the Acadian Expulsion?', ['British colonial authorities', 'A concept unrelated to the Acadian Expulsion', 'French colonial authorities', 'The government of the United States'], 0),
   ('Did the expulsion forcibly remove Acadians from their homes in the Maritimes?', ['Yes', 'No, Acadians were never forced to leave their homes', 'A concept unrelated to the Acadian Expulsion', 'The Acadians voluntarily chose to relocate with no external pressure'], 0),
   ('Why might British authorities have viewed the Acadian population as a perceived security concern during a period of conflict with France?', ['Acadians’ French heritage and reluctance to pledge full loyalty to the British Crown raised suspicion during ongoing tensions with France', 'The Acadians had no connection to France and posed no perceived concern to British authorities', 'This concept has no relevance to Canadian history', 'There was no conflict between Britain and France at any point during this period'], 0),
   ('Why is the Acadian Expulsion remembered as a significant and tragic event in Canadian history?', ['It caused widespread suffering, death, and the permanent separation of many Acadian families and communities', 'The Acadian Expulsion had no lasting impact on Acadian communities', 'This concept has no relevance to history', 'The event is remembered only as a minor, insignificant occurrence'], 0)]),
]),

day(108, [
E('Writing: The Speculative Fiction Short Story',
  'Grade 10 English strand: speculative fiction imagines alternative realities, such as future technologies, altered histories, or fantastical worlds, to explore ideas and possibilities beyond our current world.',
  [('What does speculative fiction typically imagine?', ['Alternative realities, such as future technologies or altered histories', 'Only strictly factual accounts of real historical events', 'A concept unrelated to writing', 'A story with no imaginative elements at all'], 0),
   ('Can speculative fiction include fantastical worlds that do not exist in reality?', ['Yes', 'No, speculative fiction is never allowed to depart from reality', 'A concept unrelated to speculative fiction', 'Fantastical worlds are exclusive to non-fiction writing'], 0),
   ('Why might a writer use a speculative future setting to comment on a present-day issue, such as technology or climate change?', ['An imagined future can explore the potential consequences of current trends in a vivid, thought-provoking way', 'A speculative future setting never allows a writer to comment on any present-day issue', 'This concept has no connection to writing', 'Speculative fiction is always disconnected from any real-world concern'], 0),
   ('Which of these best reflects a speculative fiction premise?', ['A city where citizens’ memories can be legally traded as currency.', 'A step-by-step recipe for baking bread.', 'A factual biography of a real historical figure with no invented events.', 'A weather report for tomorrow.'], 0),
   ('Why might writing a speculative fiction short story require careful attention to internal logic and consistent world-building?', ['Even an imaginative or unrealistic premise needs consistent rules so that readers can follow and believe in the story’s world', 'Internal logic and consistency are never important in speculative fiction', 'This concept has no relevance to writing', 'Speculative fiction worlds never require any explanation or consistent rules'], 0)]),
M('Complex Numbers: The Complex Plane and Polar Form',
  'Grade 10 Math strand: complex numbers can be plotted on the complex plane using a real and imaginary axis, and expressed in polar form using a magnitude and angle instead of standard rectangular coordinates.',
  [('What two axes make up the complex plane?', ['A real axis and an imaginary axis', 'Two identical real axes', 'A concept unrelated to complex numbers', 'A single axis representing only magnitude'], 0),
   ('What two values are used to express a complex number in polar form?', ['A magnitude and an angle', 'Only two real numbers with no imaginary component', 'A concept unrelated to polar form', 'The sum of the real and imaginary parts only'], 0),
   ('Can a complex number be represented as a point on the complex plane?', ['Yes', 'No, complex numbers can never be represented graphically', 'A concept unrelated to the complex plane', 'Only real numbers can ever be plotted on any plane'], 0),
   ('Why might polar form be more convenient than rectangular form when multiplying two complex numbers?', ['In polar form, magnitudes are multiplied and angles are added, which is often simpler than expanding rectangular expressions', 'Polar form never simplifies any operation involving complex numbers', 'This concept has no connection to math', 'Rectangular form and polar form always require identical calculation steps for multiplication'], 0),
   ('Why is visualizing complex numbers on the complex plane useful for understanding their magnitude and direction?', ['Plotting a complex number as a point makes its distance from the origin and its angle immediately visible, similar to vectors', 'Visualizing complex numbers on a plane provides no useful information about them', 'This concept has no relevance to complex numbers', 'Complex numbers have no meaningful magnitude or direction to visualize'], 0)]),
Sc('Biology: Genetic Mutations and Variation',
   'Grade 10 Science strand: a genetic mutation is a change in an organism’s DNA sequence that can arise spontaneously or from environmental factors, contributing to genetic variation within a population.',
   [('What is a genetic mutation?', ['A change in an organism’s DNA sequence', 'A change in an organism’s diet only', 'A concept unrelated to biology', 'A change in the weather affecting an organism'], 0),
    ('Can mutations arise from environmental factors, such as radiation or certain chemicals?', ['Yes', 'No, mutations are never caused by environmental factors', 'A concept unrelated to genetic mutations', 'Environmental factors have no connection to an organism’s DNA'], 0),
    ('Do mutations contribute to genetic variation within a population?', ['Yes', 'No, mutations never contribute to genetic variation', 'A concept unrelated to genetic variation', 'Genetic variation only ever comes from an organism’s diet'], 0),
    ('Why are most mutations considered neutral or harmful, while a small number can be beneficial to an organism?', ['Random changes to a functioning genetic sequence are more likely to disrupt existing function than to improve it, though occasionally a change proves advantageous', 'Every mutation is always equally beneficial to the organism that has it', 'This concept has no connection to biology', 'Mutations never have any effect on an organism’s traits or survival'], 0),
    ('Why is genetic variation produced by mutations considered important for a species’ ability to adapt over time?', ['Variation provides the raw material that natural selection can act upon, allowing populations to adapt to changing environments', 'Genetic variation has no connection to a species’ ability to adapt to its environment', 'This concept has no relevance to biology', 'Species can adapt to changing environments with no genetic variation present at all'], 0)]),
H('Enemy Alien Internment in Canada during the First World War',
  'Grade 10 History strand: during the First World War, thousands of Ukrainian, German, and other immigrants from countries at war with Britain were classified as enemy aliens and interned in camps under the War Measures Act.',
  [('Under what legislation were enemy aliens interned during the First World War?', ['The War Measures Act', 'A concept unrelated to Canadian history', 'The Charter of Rights and Freedoms', 'The National Policy'], 0),
   ('Which groups were among those classified as enemy aliens and interned during WWI?', ['Ukrainian and German immigrants, among others', 'A concept unrelated to enemy alien internment', 'Only British-born citizens', 'Only Indigenous peoples'], 0),
   ('Were thousands of immigrants interned in camps during this period based on their country of origin?', ['Yes', 'No, no internment of immigrants occurred during the First World War', 'A concept unrelated to this topic', 'Internment only ever occurred during the Second World War'], 0),
   ('Why might immigrants from countries at war with Britain have faced suspicion and restricted freedoms in Canada during WWI?', ['Wartime fears about loyalty and espionage led authorities to view immigrants connected to enemy nations with suspicion, despite most having no involvement in the conflict', 'Immigrants from any country were always treated with equal freedom during the First World War', 'This concept has no relevance to Canadian history', 'No country was ever at war with Britain during the First World War'], 0),
   ('Why is the internment of enemy aliens during WWI often studied alongside other examples of wartime civil liberties restrictions in Canadian history?', ['It illustrates a recurring pattern in which wartime fear led governments to restrict the rights of specific groups, as also seen with Japanese Canadian internment', 'This event has no connection to any other instance of wartime civil liberties restriction in Canada', 'This concept has no relevance to history', 'Civil liberties have never been restricted in Canada under any circumstances'], 0)]),
]),

day(109, [
E('Media Literacy: Analyzing Photojournalism',
  'Grade 10 English strand: photojournalism uses photographs to document and communicate news events, requiring viewers to consider framing, context, and the photographer’s choices when interpreting an image.',
  [('What does photojournalism use to document and communicate news events?', ['Photographs', 'Only spoken interviews with no visual component', 'A concept unrelated to media literacy', 'Fictional illustrations with no basis in real events'], 0),
   ('Should viewers consider framing and context when interpreting a news photograph?', ['Yes', 'No, framing and context never matter when interpreting a photograph', 'A concept unrelated to photojournalism', 'A photograph always shows the complete, unbiased truth with no need for interpretation'], 0),
   ('Why might the specific moment a photographer chooses to capture affect how viewers interpret an event?', ['A single chosen moment can shape the emotional impact and narrative viewers take away, even though it is only part of a larger event', 'The moment captured in a photograph never has any effect on how it is interpreted', 'This concept has no connection to media literacy', 'Every photograph captures an entire event completely and equally regardless of timing'], 0),
   ('Why is it important to consider what is left outside the frame of a news photograph?', ['Elements outside the frame are not shown, so a photograph may unintentionally or intentionally present an incomplete picture of an event', 'Everything relevant to an event is always fully visible within a single photograph’s frame', 'This concept has no connection to photojournalism', 'The frame of a photograph never limits what information is presented to a viewer'], 0),
   ('Why do many news organizations maintain codes of ethics specifically for photojournalism, such as rules against staging images?', ['Maintaining honesty and accuracy in photographs helps preserve public trust in visual journalism as a truthful record of events', 'Ethics codes for photojournalism have no connection to public trust in the media', 'This concept has no relevance to media literacy', 'Staging images has no effect on how truthfully a photograph represents an event'], 0)]),
M('Number Theory: Modular Arithmetic and Applications',
  'Grade 10 Math strand: modular arithmetic describes a system where numbers wrap around after reaching a fixed value called the modulus, similar to how a clock resets after reaching 12.',
  [('What is modular arithmetic based on?', ['Numbers wrapping around after reaching a fixed value called the modulus', 'Numbers that always increase without any limit', 'A concept unrelated to number theory', 'A system with no repeating pattern at all'], 0),
   ('What everyday example is often used to explain modular arithmetic?', ['A clock resetting after reaching 12', 'A ruler that never repeats any measurement', 'A concept unrelated to modular arithmetic', 'A scale that always shows an increasing weight'], 0),
   ('In modulo 5 arithmetic, what is 7 mod 5?', ['2', '7', '5', '12'], 0),
   ('Why is modular arithmetic often described using the phrase clock arithmetic?', ['Like a 12-hour clock resetting after 12, values in modular arithmetic wrap back to zero after reaching the modulus', 'Modular arithmetic has no connection to how a clock displays time', 'This concept has no connection to math', 'Clocks and modular arithmetic have completely unrelated numerical systems'], 0),
   ('Why is modular arithmetic considered useful in fields such as computer science and cryptography?', ['It provides a reliable way to work with numbers that cycle or reset, which is useful for tasks like data encoding and encryption algorithms', 'Modular arithmetic has no practical application outside of pure mathematics', 'This concept has no relevance to number theory', 'Computer science and cryptography never involve any numerical calculations'], 0)]),
Sc('Earth Science: Volcanoes and Igneous Rock Formation',
   'Grade 10 Science strand: volcanoes form when molten rock, or magma, rises to the surface and erupts as lava, which cools and solidifies to form igneous rock.',
   [('What is magma called once it erupts onto the surface as lava?', ['Lava', 'Sediment', 'A concept unrelated to earth science', 'Metamorphic rock'], 0),
    ('What type of rock forms when lava cools and solidifies?', ['Igneous rock', 'Sedimentary rock only', 'A concept unrelated to volcanoes', 'A type of soil with no rock formation involved'], 0),
    ('Do volcanoes form when molten rock rises to the surface and erupts?', ['Yes', 'No, volcanoes have no connection to molten rock', 'A concept unrelated to volcanic activity', 'Volcanoes form only from surface weathering, never from molten rock'], 0),
    ('Why might lava that cools quickly at the surface produce rock with smaller crystals than magma that cools slowly underground?', ['Rapid cooling gives crystals less time to grow, while slow cooling underground allows larger crystals to form over time', 'The cooling rate of molten rock never affects the size of the crystals that form', 'This concept has no connection to earth science', 'All igneous rocks form with exactly the same crystal size regardless of cooling rate'], 0),
    ('Why are volcanoes often found near tectonic plate boundaries?', ['Plate boundaries are where magma can more easily rise toward the surface, due to processes like subduction or seafloor spreading', 'Volcanoes and tectonic plate boundaries have no geological connection to one another', 'This concept has no relevance to earth science', 'Volcanoes occur with equal frequency in the middle of tectonic plates and at their boundaries'], 0)]),
H('The Selkirk Settlement and the Battle of Seven Oaks',
  'Grade 10 History strand: the Selkirk Settlement, established in 1812 in the Red River area, created tension with the North West Company and Métis traders, culminating in the 1816 Battle of Seven Oaks.',
  [('In what year was the Selkirk Settlement established?', ['1812', 'A concept unrelated to Canadian history', '1867', '1950'], 0),
   ('In what region was the Selkirk Settlement located?', ['The Red River area', 'A concept unrelated to the Selkirk Settlement', 'The Arctic coastline', 'Southern Ontario'], 0),
   ('Did tensions between the settlement and the North West Company and Métis traders lead to a violent confrontation in 1816?', ['Yes', 'No, the settlement caused no tension with any other group', 'A concept unrelated to the Selkirk Settlement', 'The Battle of Seven Oaks never actually took place'], 0),
   ('Why might the arrival of Selkirk’s settlers have created tension with the Métis and the North West Company operating in the Red River area?', ['The settlers competed for land, resources, and control of the fur trade with groups who were already established in the region', 'The arrival of new settlers never creates any tension with existing communities or trading companies', 'This concept has no relevance to Canadian history', 'The Métis and the North West Company had no presence in the Red River area before the settlement arrived'], 0),
   ('Why is the Battle of Seven Oaks often studied as an early example of conflict over land and resources in the Canadian West?', ['It highlights early competing claims to land and trade in the region, foreshadowing later tensions such as the Riel Rebellions', 'The Battle of Seven Oaks has no connection to any later conflict over land in the Canadian West', 'This concept has no relevance to history', 'Conflicts over land and resources never occurred anywhere in the Canadian West'], 0)]),
]),

day(110, [
E('Review: Archetypes, Genre, and Communication (Days 101-109)',
  'Grade 10 English strand review: students revisit archetypes and the hero’s journey, the Gothic tradition, the feature article, commonly confused words, the job interview, allegory and fable, the epic hero, speculative fiction, and photojournalism.',
  [('What is an archetype?', ['A recurring character, symbol, or pattern found across literature and cultures', 'A single unique word invented by one author', 'A concept unrelated to reading', 'A type of punctuation mark'], 0),
   ('What mood does Gothic fiction typically create?', ['Dread or suspense', 'Light-hearted comedy with no tension at all', 'A concept unrelated to literature', 'Complete calm with no conflict present'], 0),
   ('What does a fable typically teach?', ['A specific moral lesson', 'Only historical facts with no lesson at all', 'A concept unrelated to fables', 'Nothing at all; fables have no purpose'], 0),
   ('What does an epic hero typically undertake?', ['A grand quest', 'A short errand with no obstacles', 'A concept unrelated to epic conventions', 'An activity with no goal at all'], 0),
   ('What does photojournalism use to document and communicate news events?', ['Photographs', 'Only spoken interviews with no visual component', 'A concept unrelated to media literacy', 'Fictional illustrations with no basis in real events'], 0)]),
M('Review: Conics, Statistics, Matrices, and Number Systems (Days 101-109)',
  'Grade 10 Math strand review: students revisit conic sections, sum and difference identities, sampling methods, the binomial distribution, matrix transformations, derivatives, the cross product, the complex plane, and modular arithmetic.',
  [('What are conic sections?', ['Curves formed by slicing a cone, including circles, ellipses, parabolas, and hyperbolas', 'A type of algebraic expression with no geometric meaning', 'A concept unrelated to geometry', 'Only straight lines drawn on a graph'], 0),
   ('What is a sample in statistics?', ['A subset of a population used to make inferences about the whole', 'The entire population being studied', 'A concept unrelated to statistics', 'A single number with no connection to a population'], 0),
   ('What does the derivative of a function represent?', ['Its instantaneous rate of change', 'The total area under its graph', 'A concept unrelated to calculus', 'The exact value of the function at x equals zero only'], 0),
   ('What does the cross product of two vectors produce?', ['A new vector perpendicular to both original vectors', 'A single scalar number with no direction', 'A concept unrelated to vectors', 'The exact sum of the two original vectors'], 0),
   ('What is modular arithmetic based on?', ['Numbers wrapping around after reaching a fixed value called the modulus', 'Numbers that always increase without any limit', 'A concept unrelated to number theory', 'A system with no repeating pattern at all'], 0)]),
Sc('Review: Chemistry, Biology, Physics, and Earth Science (Days 101-109)',
   'Grade 10 Science strand review: students revisit percent yield, the skeletal and muscular systems, momentum, the nitrogen cycle, plant reproduction, calorimetry, naming compounds, genetic mutations, and volcanoes.',
   [('What does the limiting reagent in a chemical reaction determine?', ['The maximum amount of product that can be formed', 'The colour of the final product', 'A concept unrelated to chemistry', 'The temperature at which the reaction occurs'], 0),
    ('How is momentum calculated?', ['Mass multiplied by velocity', 'Mass divided by velocity', 'A concept unrelated to physics', 'Velocity multiplied by time only'], 0),
    ('What does the nitrogen cycle describe?', ['How nitrogen moves between the atmosphere, soil, and living organisms', 'How electricity flows through a circuit', 'A concept unrelated to earth science', 'How rocks form deep underground only'], 0),
    ('What is a genetic mutation?', ['A change in an organism’s DNA sequence', 'A change in an organism’s diet only', 'A concept unrelated to biology', 'A change in the weather affecting an organism'], 0),
    ('What type of rock forms when lava cools and solidifies?', ['Igneous rock', 'Sedimentary rock only', 'A concept unrelated to volcanoes', 'A type of soil with no rock formation involved'], 0)]),
H('Review: Pre-Confederation Canadian History (Days 101-109)',
  'Grade 10 History strand review: students revisit the War of 1812, the Rebellions of 1837-38, the Durham Report, the road to Confederation, the United Empire Loyalists, the Numbered Treaties, the Acadian Expulsion, WWI internment, and the Selkirk Settlement.',
  [('Between which two countries was the War of 1812 primarily fought?', ['The United States and Britain', 'A concept unrelated to Canadian history', 'France and Britain', 'Canada and the United States, acting entirely alone'], 0),
   ('Who led the rebellion in Upper Canada in 1837?', ['William Lyon Mackenzie', 'A concept unrelated to Canadian history', 'A figure with no connection to Upper Canada', 'A British monarch'], 0),
   ('In what year did the Charlottetown and Quebec Conferences take place?', ['1864', 'A concept unrelated to Canadian history', '1812', '1900'], 0),
   ('Who were the United Empire Loyalists?', ['Colonists who remained loyal to Britain during the American Revolution', 'A concept unrelated to Canadian history', 'A group with no connection to the American Revolution', 'Soldiers from France who settled in Quebec'], 0),
   ('In what year was the Selkirk Settlement established?', ['1812', 'A concept unrelated to Canadian history', '1867', '1950'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_101_110)
    append_to(10, g10_101_110)
