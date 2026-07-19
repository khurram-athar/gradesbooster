#!/usr/bin/env python3
"""Grade 10, Days 81-90 -- extends Grade 10 from 80 to 90 days. Topics
chosen to avoid any overlap with the existing Day 1-80 set (see
data/grade10.json): existentialist themes in fiction, rhetorical analysis
essays, nominalization, podcast journalism, unreliable framing in memoir,
op-ed rebuttals, the chorus in Greek tragedy, storytelling in public
speaking, comparing book-to-film adaptations; inverse of quadratic
functions, box-and-whisker plots, volume of composite solids, combined
substitution/elimination systems, recursive sequences, the ambiguous case
of the sine law, the complement rule in probability, transformations of
absolute value functions, currency exchange and international finance;
Le Chatelier's principle, photosynthesis light and dark reactions, torque
and rotational equilibrium, ocean currents and climate, solubility and
precipitation reactions, the lymphatic system, sound waves and the
Doppler effect, groundwater and aquifers, catalysts and reaction rates;
the Vietnam War era and Canadian draft dodgers, the founding of the
Canada Pension Plan, the Berlin Wall and Canadian Cold War diplomacy, the
Green Revolution and Canadian agricultural policy, the founding of VIA
Rail, the 1980 Quebec referendum, Canada's role in the Gulf War, the 1988
Free Trade Agreement debate, and Canada's peacekeeping mission in Rwanda.

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


def _rebalance_answer_positions(days, seed=20260929):
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


g10_81_90 = [
day(81, [
E('Literature: Existentialist Themes in Fiction',
  'Grade 10 English strand: existentialist fiction explores themes of individual freedom, choice, and the search for meaning in a world that offers no inherent answers.',
  [('What do existentialist themes in fiction often explore?', ['Individual freedom, choice, and the search for meaning', 'Only fairy tale settings with no deeper themes', 'A concept unrelated to literature', 'Recipes and cooking instructions'], 0),
   ('Does existentialist fiction often suggest the world offers no inherent, built-in meaning?', ['Yes', 'No, existentialist fiction always presents a clear, given meaning', 'A concept unrelated to existentialism', 'Meaning is never a concern in existentialist fiction'], 0),
   ('Why might a character in an existentialist novel struggle with the weight of their own choices?', ['If no external force dictates meaning, characters must create their own purpose through their choices', 'Characters in existentialist novels never face any struggle', 'This concept has no connection to literature', 'Existentialist novels always provide characters with a predetermined purpose'], 0),
   ('Which of these sentences reflects an existentialist theme?', ['She realized that no one could tell her who to become; she alone would decide.', 'The recipe called for two cups of flour and one egg.', 'The train departs the station at exactly nine o’clock.', 'The chemical formula for water is H2O.'], 0),
   ('Why might existentialist fiction appeal to readers wrestling with questions about purpose and identity?', ['It directly engages with the challenge of creating meaning without relying on predetermined answers', 'Existentialist fiction never engages with questions of purpose or identity', 'This concept has no connection to literature', 'Readers never relate to characters who question their own purpose'], 0)]),
M('Functions: Inverse of Quadratic Functions',
  'Grade 10 Math strand: finding the inverse of a quadratic function involves switching the roles of x and y and solving for y, often restricting the domain so the inverse remains a function.',
  [('When finding the inverse of a function, what roles are switched?', ['The roles of x and y', 'The roles of the slope and intercept', 'A concept unrelated to inverse functions', 'Nothing is switched at all'], 0),
   ('Why is the domain of a quadratic function often restricted before finding its inverse?', ['A full parabola fails the horizontal line test, so restricting the domain keeps the inverse a true function', 'Quadratic functions never need any domain restriction for their inverse', 'This concept has no connection to inverse functions', 'The domain is restricted only for linear functions, never quadratics'], 0),
   ('If a function passes through the point (2, 5), what point must its inverse pass through?', ['(5, 2)', '(2, 5)', '(-2, -5)', '(5, -2)'], 0),
   ('Why is it useful to graph a function and its inverse together on the same axes?', ['It shows the reflective symmetry between the two graphs across the line y equals x', 'Graphing a function with its inverse never reveals any useful pattern', 'This concept has no connection to math', 'A function and its inverse never share any graphical relationship'], 0),
   ('What is the inverse relationship of y equals x squared, before restricting the domain?', ['x equals y squared', 'y equals negative x squared', 'x equals negative y', 'y equals the square root of x only'], 0)]),
Sc('Chemistry: Le Chatelier’s Principle',
   'Grade 10 Science strand: Le Chatelier’s principle states that when a system at equilibrium is disturbed, it shifts to counteract the disturbance and establish a new equilibrium.',
   [('What does Le Chatelier’s principle describe?', ['How a system at equilibrium shifts to counteract a disturbance', 'How atoms are structured inside a nucleus', 'A concept unrelated to chemistry', 'How light travels through a vacuum'], 0),
    ('Does a system at equilibrium respond to a disturbance by shifting to a new equilibrium?', ['Yes', 'No, systems at equilibrium never respond to any disturbance', 'A concept unrelated to Le Chatelier’s principle', 'Equilibrium always remains completely unchanged no matter what happens'], 0),
    ('If more reactant is added to a reaction at equilibrium, which direction does the reaction shift?', ['Toward the products, to use up the added reactant', 'Toward the reactants, away from the products', 'A concept unrelated to equilibrium', 'The reaction does not shift in any direction'], 0),
    ('Why might increasing the temperature of an exothermic reaction at equilibrium shift it toward the reactants?', ['Added heat acts like an extra product, so the system shifts to counteract that increase', 'Temperature changes never have any effect on a reaction at equilibrium', 'This concept has no connection to chemistry', 'Exothermic reactions never reach any state of equilibrium'], 0),
    ('Why is Le Chatelier’s principle useful for industrial chemists producing a specific chemical?', ['It helps them adjust conditions like pressure and temperature to maximize the yield of a desired product', 'Le Chatelier’s principle has no practical industrial application', 'This concept has no relevance to chemistry', 'Industrial processes never rely on chemical equilibrium at all'], 0)]),
H('Canada and the Vietnam War Era: Draft Dodgers',
  'Grade 10 History strand: during the Vietnam War, Canada did not join the conflict and became a destination for thousands of American draft resisters and deserters seeking refuge.',
  [('Did Canada officially join the Vietnam War?', ['No', 'Yes, Canada sent combat troops to fight in Vietnam', 'A concept unrelated to Canadian history', 'Canada declared war on Vietnam directly'], 0),
   ('What did Canada become for many American draft resisters during the Vietnam War?', ['A destination seeking refuge', 'A place that actively rejected all American immigrants', 'A concept unrelated to the Vietnam War era', 'A country that sent its own citizens to fight in Vietnam'], 0),
   ('Did thousands of Americans move to Canada to avoid being drafted into the Vietnam War?', ['Yes', 'No, no Americans ever moved to Canada during this era', 'A concept unrelated to Canadian history', 'Draft resisters were all turned away at the border'], 0),
   ('Why might Canada’s decision not to join the Vietnam War have shaped its identity separate from the United States?', ['It reflected an independent foreign policy stance distinct from its powerful neighbour', 'This decision had no connection to Canadian identity or independence', 'This concept has no relevance to history', 'Canada’s foreign policy was always identical to that of the United States'], 0),
   ('Why might the arrival of draft resisters have influenced Canadian society and culture in the following decades?', ['Many resisters settled permanently, contributing to communities and cultural life across the country', 'Draft resisters never had any lasting impact on Canadian society', 'This concept has no relevance to history', 'All draft resisters returned to the United States within a few months'], 0)]),
]),

day(82, [
E('Writing: The Rhetorical Analysis Essay',
  'Grade 10 English strand: a rhetorical analysis essay examines how a speaker or writer uses appeals to ethos, pathos, and logos, along with stylistic devices, to persuade an audience.',
  [('What does a rhetorical analysis essay examine?', ['How a speaker or writer uses appeals and devices to persuade an audience', 'Only the biography of the author', 'A concept unrelated to writing', 'A list of unrelated grammar rules'], 0),
   ('Name one of the three classical appeals examined in rhetorical analysis, such as ethos.', ['Ethos', 'A concept unrelated to rhetorical analysis', 'Photosynthesis', 'Osmosis'], 0),
   ('Does pathos refer to an appeal to emotion?', ['Yes', 'No, pathos refers only to an appeal to credibility', 'A concept unrelated to rhetorical analysis', 'Pathos has no connection to persuasive appeals'], 0),
   ('Why might a rhetorical analysis essay focus on how an argument is made rather than whether it is correct?', ['The goal is to understand the persuasive techniques used, not to judge the argument’s validity', 'Rhetorical analysis only ever evaluates whether an argument is factually true', 'This concept has no connection to writing', 'Persuasive techniques are never relevant to rhetorical analysis'], 0),
   ('Why is identifying an author’s intended audience important in a rhetorical analysis essay?', ['Understanding the audience helps explain why certain appeals or strategies were chosen', 'The intended audience never affects how a speech or text is analyzed', 'This concept has no connection to writing', 'Every audience responds to persuasive techniques in exactly the same way'], 0)]),
M('Data Management: Box-and-Whisker Plots and Quartiles',
  'Grade 10 Math strand: a box-and-whisker plot displays a data set’s distribution using the minimum, first quartile, median, third quartile, and maximum.',
  [('How many key values does a box-and-whisker plot display?', ['Five', 'Two', 'Three', 'Ten'], 0),
   ('What is the middle value of an ordered data set called?', ['The median', 'The minimum', 'The maximum', 'A concept unrelated to data'], 0),
   ('What does the first quartile represent in a data set?', ['The value below which 25 percent of the data falls', 'The exact average of the entire data set', 'A concept unrelated to quartiles', 'The single highest value in the data set'], 0),
   ('Why might a box-and-whisker plot be useful for comparing two data sets, like exam scores from two classes?', ['It visually shows the spread and central tendency, making comparison straightforward', 'Box-and-whisker plots never help with comparing data sets', 'This concept has no connection to data management', 'Exam scores can never be represented in a box-and-whisker plot'], 0),
   ('What is the range between the first and third quartiles called?', ['The interquartile range', 'The mean absolute deviation', 'A concept unrelated to quartiles', 'The standard deviation'], 0)]),
Sc('Biology: Photosynthesis in Depth: Light and Dark Reactions',
   'Grade 10 Science strand: photosynthesis consists of two stages, the light-dependent reactions that capture solar energy, and the light-independent (dark) reactions that use that energy to build sugars.',
   [('How many main stages does photosynthesis consist of?', ['Two', 'One', 'Five', 'A concept unrelated to biology'], 0),
    ('What do the light-dependent reactions of photosynthesis capture?', ['Solar energy', 'Only carbon dioxide from the air', 'A concept unrelated to photosynthesis', 'Nothing at all related to energy'], 0),
    ('Do the light-independent, or dark, reactions use energy captured earlier to build sugars?', ['Yes', 'No, the dark reactions never use any captured energy', 'A concept unrelated to photosynthesis', 'Sugars are never produced during photosynthesis'], 0),
    ('Why are the light-independent reactions sometimes called dark reactions, even though they can occur during the day?', ['They do not directly require light, unlike the light-dependent reactions', 'The dark reactions only ever occur at night, never during the day', 'This concept has no connection to photosynthesis', 'Dark reactions require intense direct sunlight at all times'], 0),
    ('Why is understanding both stages of photosynthesis important for understanding plant growth?', ['Both stages work together to convert light energy into the chemical energy plants use to grow', 'The two stages of photosynthesis have no connection to how plants grow', 'This concept has no relevance to biology', 'Only one of the two stages actually contributes to a plant’s growth'], 0)]),
H('The Founding of the Canada Pension Plan',
  'Grade 10 History strand: the Canada Pension Plan was established in 1965 to provide retirement, disability, and survivor benefits, forming a key part of Canada’s social safety net.',
  [('In what decade was the Canada Pension Plan established?', ['The 1960s', 'The 1920s', 'A concept unrelated to Canadian history', 'The 1990s'], 0),
   ('Name one type of benefit the Canada Pension Plan provides, such as retirement benefits.', ['Retirement benefits', 'A concept unrelated to the Canada Pension Plan', 'Free university tuition', 'Unlimited paid vacation days'], 0),
   ('Is the Canada Pension Plan considered a key part of Canada’s social safety net?', ['Yes', 'No, the Canada Pension Plan has no connection to Canada’s social safety net', 'A concept unrelated to Canadian history', 'Social safety nets never include any pension programs'], 0),
   ('Why might the introduction of the Canada Pension Plan have been significant for older Canadians?', ['It provided a more reliable source of income security for people after they stopped working', 'The Canada Pension Plan never provided any income security for Canadians', 'This concept has no relevance to Canadian history', 'Older Canadians had no need for any retirement income support'], 0),
   ('Why might a national pension program be considered an important part of a country’s approach to social welfare?', ['It can help reduce poverty among retirees and provide financial stability across the population', 'National pension programs never have any effect on poverty or financial stability', 'This concept has no relevance to history', 'Social welfare programs never include any form of retirement support'], 0)]),
]),

day(83, [
E('Grammar: Nominalization and Formal Register',
  'Grade 10 English strand: nominalization turns a verb or adjective into a noun, such as changing decide into decision, often used to create a more formal, academic register in writing.',
  [('What does nominalization do to a verb or adjective?', ['Turns it into a noun', 'Turns it into a question', 'A concept unrelated to grammar', 'Removes it from the sentence entirely'], 0),
   ('Which word is the nominalized form of the verb decide?', ['Decision', 'Deciding', 'Decisive', 'Decided'], 0),
   ('Is nominalization commonly associated with a formal or informal writing register?', ['A formal register', 'An informal register only', 'A concept unrelated to nominalization', 'Neither a formal nor an informal register'], 0),
   ('Which sentence uses nominalization?', ['The committee’s decision surprised everyone in the room.', 'The committee decided quickly.', 'They will decide tomorrow.', 'Deciding takes a long time sometimes.'], 0),
   ('Why might a writer use nominalization in a formal academic essay?', ['It can create a more objective, abstract, and formal tone', 'Nominalization always makes writing sound more casual', 'This concept has no connection to writing style', 'Formal essays never use any nominalized words'], 0)]),
M('Geometry: Volume of Composite Solids',
  'Grade 10 Math strand: students find the volume of composite solids by breaking the shape into simpler solids, such as prisms, cylinders, cones, and spheres, then adding their individual volumes.',
  [('To find the volume of a composite solid, what should you do first?', ['Break the shape into simpler solids', 'Only measure the outer surface area', 'A concept unrelated to composite solids', 'Ignore the individual parts entirely'], 0),
   ('If a composite solid is made of a cone with volume 15 cubic cm and a cylinder with volume 40 cubic cm, what is the total volume?', ['55 cubic cm', '40 cubic cm', '15 cubic cm', '25 cubic cm'], 0),
   ('Why is it useful to identify simple shapes within a composite solid before calculating volume?', ['It allows the use of known volume formulas for each individual shape', 'Identifying simple shapes never helps calculate the volume of a composite solid', 'This concept has no connection to geometry', 'Composite solids can never be broken into simpler shapes'], 0),
   ('If a composite solid is made of two rectangular prisms with volumes of 24 and 18 cubic cm, what is the total volume?', ['42 cubic cm', '24 cubic cm', '18 cubic cm', '6 cubic cm'], 0),
   ('Why might understanding composite solid volume be useful for architects designing a building?', ['Many buildings combine simple geometric shapes, so this skill helps calculate total material or space needs', 'Composite solid volume never applies to any real-world architectural design', 'This concept has no connection to geometry', 'Buildings are always made of a single, simple geometric shape'], 0)]),
Sc('Physics: Torque and Rotational Equilibrium',
   'Grade 10 Science strand: torque measures the turning effect of a force around a pivot point, and an object is in rotational equilibrium when the net torque acting on it is zero.',
   [('What does torque measure?', ['The turning effect of a force around a pivot point', 'The total mass of an object', 'A concept unrelated to physics', 'The temperature of an object'], 0),
    ('When is an object in rotational equilibrium?', ['When the net torque acting on it is zero', 'When it is moving at a constant speed in a straight line', 'A concept unrelated to torque', 'When no force acts on it at all'], 0),
    ('Does increasing the distance from the pivot point increase the torque produced by a given force?', ['Yes', 'No, distance from the pivot has no effect on torque', 'A concept unrelated to torque', 'Torque only depends on the mass of an object'], 0),
    ('Why might a longer wrench make it easier to loosen a tight bolt compared to a shorter one?', ['A longer wrench increases the distance from the pivot, producing greater torque for the same applied force', 'Wrench length never has any effect on the torque applied to a bolt', 'This concept has no connection to physics', 'A shorter wrench always produces more torque than a longer one'], 0),
    ('Why is understanding rotational equilibrium important when designing a seesaw or balance scale?', ['It helps ensure the torques on each side balance so the object remains stable and level', 'Rotational equilibrium has no connection to how a seesaw or balance scale works', 'This concept has no relevance to physics', 'Seesaws and balance scales never rely on any torque balance'], 0)]),
H('The Berlin Wall and Canadian Cold War Diplomacy',
  'Grade 10 History strand: the construction and eventual fall of the Berlin Wall shaped global Cold War tensions, with Canada playing a supporting diplomatic role within NATO throughout the period.',
  [('What structure divided the city of Berlin during the Cold War?', ['The Berlin Wall', 'A concept unrelated to Canadian history', 'The Great Wall', 'The Iron Curtain railway'], 0),
   ('Did Canada play a diplomatic role within NATO during the Cold War period?', ['Yes', 'No, Canada had no involvement in NATO during the Cold War', 'A concept unrelated to the Berlin Wall', 'Canada left NATO entirely during this period'], 0),
   ('Did the Berlin Wall eventually fall, symbolizing the end of Cold War divisions?', ['Yes', 'No, the Berlin Wall still stands today', 'A concept unrelated to Canadian history', 'The Berlin Wall was never actually removed'], 0),
   ('Why might Canada’s NATO membership have connected it to events surrounding the Berlin Wall, even though it was not physically in Europe?', ['NATO alliance commitments linked member countries’ security and diplomatic interests across the Atlantic', 'NATO membership never connected Canada to any European Cold War events', 'This concept has no relevance to Canadian history', 'Canada’s foreign policy was completely disconnected from its NATO membership'], 0),
   ('Why is the fall of the Berlin Wall often seen as a significant turning point in twentieth-century history?', ['It symbolized the collapse of Cold War divisions between Eastern and Western Europe', 'The fall of the Berlin Wall had no broader historical significance', 'This concept has no relevance to history', 'Cold War tensions actually increased immediately after the wall fell'], 0)]),
]),

day(84, [
E('Media Literacy: Analyzing Podcast Journalism',
  'Grade 10 English strand: podcast journalism uses audio storytelling techniques, such as interviews, narration, and sound design, to investigate and report on real events and issues.',
  [('What does podcast journalism use to investigate and report on real events?', ['Audio storytelling techniques', 'Only printed newspaper articles', 'A concept unrelated to media literacy', 'Silent, text-only reports'], 0),
   ('Name one audio storytelling technique used in podcast journalism, such as narration.', ['Narration', 'A concept unrelated to podcast journalism', 'A silent film reel', 'A printed photograph'], 0),
   ('Can sound design help shape the mood or emphasis of a podcast story?', ['Yes', 'No, sound design never affects how a podcast story feels', 'A concept unrelated to podcast journalism', 'Sound design has no connection to storytelling'], 0),
   ('Why might a podcast journalist include a direct interview clip rather than only paraphrasing what someone said?', ['A direct clip preserves the speaker’s own voice, tone, and exact words, adding authenticity', 'Direct interview clips never add anything valuable to a podcast story', 'This concept has no connection to media literacy', 'Paraphrasing always conveys more meaning than an original recording'], 0),
   ('Why is critically evaluating sources important when listening to investigative podcast journalism?', ['Understanding who is speaking and their potential bias helps listeners assess the reliability of the reporting', 'Source evaluation never matters when listening to a podcast', 'This concept has no connection to media literacy', 'All podcasts are always completely unbiased and equally reliable'], 0)]),
M('Algebra: Systems by Combined Substitution and Elimination',
  'Grade 10 Math strand: some systems of equations are most efficiently solved using a combination of substitution and elimination, choosing whichever method suits the structure of each equation.',
  [('When solving a system of equations, is it possible to combine substitution and elimination methods?', ['Yes', 'No, only one single method can ever be used', 'A concept unrelated to systems of equations', 'Combining methods always produces an incorrect answer'], 0),
   ('If one equation is already solved for a variable, which method might be most efficient to use first?', ['Substitution', 'Elimination only', 'A concept unrelated to solving systems', 'Neither method would ever apply here'], 0),
   ('If two equations have matching coefficients for one variable, which method might be most efficient to use first?', ['Elimination', 'Substitution only', 'A concept unrelated to solving systems', 'Neither method would ever apply here'], 0),
   ('Why might a student choose to eliminate one variable first, then substitute to find the second?', ['Eliminating a variable simplifies the system, making it easier to substitute back and solve for the remaining variable', 'Combining elimination and substitution never simplifies a system of equations', 'This concept has no connection to math', 'Substitution and elimination always require completely separate systems'], 0),
   ('If x plus y equals 10 and 2x minus y equals 2, what is the value of x after adding the equations together?', ['4', '10', '2', '8'], 0)]),
Sc('Earth Science: Ocean Currents and Climate',
   'Grade 10 Science strand: ocean currents circulate warm and cold water around the globe, significantly influencing regional climate patterns, such as keeping coastal areas milder than inland regions.',
   [('What do ocean currents circulate around the globe?', ['Warm and cold water', 'Only sand and sediment', 'A concept unrelated to earth science', 'Nothing at all connected to climate'], 0),
    ('Can ocean currents significantly influence regional climate patterns?', ['Yes', 'No, ocean currents have no connection to regional climate', 'A concept unrelated to ocean currents', 'Climate is never affected by any ocean process'], 0),
    ('Might a coastal region tend to have a milder climate than an inland region at a similar latitude?', ['Yes', 'No, coastal and inland regions always have identical climates', 'A concept unrelated to ocean currents', 'Ocean currents never affect coastal temperatures'], 0),
    ('Why might a warm ocean current flowing along a coastline lead to milder winters in that region?', ['The warm water can transfer heat to the nearby air, moderating the local temperature', 'Warm ocean currents never have any effect on nearby air temperature', 'This concept has no connection to earth science', 'Ocean currents only affect temperatures far out at sea, never along coastlines'], 0),
    ('Why is studying ocean currents considered important for understanding long-term climate patterns?', ['Currents help distribute heat around the planet, playing a major role in shaping global climate systems', 'Ocean currents have no connection to global climate systems', 'This concept has no relevance to earth science', 'Global climate patterns are entirely unrelated to ocean processes'], 0)]),
H('The Green Revolution and Canadian Agricultural Policy',
  'Grade 10 History strand: the Green Revolution introduced high-yield crop varieties and modern farming techniques worldwide in the mid-twentieth century, influencing Canadian agricultural policy and food production.',
  [('What did the Green Revolution introduce worldwide in the mid-twentieth century?', ['High-yield crop varieties and modern farming techniques', 'A ban on all agricultural technology', 'A concept unrelated to Canadian history', 'A worldwide halt to food production'], 0),
   ('Did the Green Revolution influence Canadian agricultural policy and food production?', ['Yes', 'No, the Green Revolution had no connection to Canadian agriculture', 'A concept unrelated to the Green Revolution', 'Canadian agriculture was never affected by any global agricultural trend'], 0),
   ('Were modern farming techniques part of the changes introduced during the Green Revolution?', ['Yes', 'No, farming techniques remained completely unchanged during this period', 'A concept unrelated to the Green Revolution', 'The Green Revolution had no connection to farming methods'], 0),
   ('Why might higher-yield crop varieties have allowed farmers to produce more food using the same amount of land?', ['These varieties were bred to produce a greater quantity of crop per plant or per acre', 'Higher-yield crops never produce more food than traditional varieties', 'This concept has no connection to agricultural history', 'Crop yield has no connection to how food production changed over time'], 0),
   ('Why might the Green Revolution have raised questions about the environmental effects of intensive modern farming?', ['Practices like heavy fertilizer and pesticide use raised new concerns about soil and water impacts', 'The Green Revolution never raised any environmental questions or concerns', 'This concept has no relevance to history', 'Modern farming techniques have no connection to environmental impact'], 0)]),
]),

day(85, [
E('Reading: Analyzing Unreliable Framing in Memoir',
  'Grade 10 English strand: memoirists shape their own life stories through selective memory and personal perspective, meaning readers must consider how this framing affects the reliability of the account.',
  [('What do memoirists shape their life stories through?', ['Selective memory and personal perspective', 'A completely objective, unfiltered record of events', 'A concept unrelated to reading', 'Only facts checked by an outside historian'], 0),
   ('Should readers consider how a memoirist’s framing might affect the reliability of their account?', ['Yes', 'No, memoirs should always be treated as entirely objective', 'A concept unrelated to memoir', 'Reliability is never a consideration when reading memoir'], 0),
   ('Why might two people who experienced the same event write very different memoirs about it?', ['Personal perspective and memory can shape how each person interprets and recalls the same experience', 'Two people always remember and describe an event in exactly the same way', 'This concept has no connection to memoir writing', 'Memoirs are never influenced by personal perspective'], 0),
   ('Why might a memoirist choose to include some memories and leave out others?', ['They may select details that best serve the story or message they want to convey', 'Memoirists always include every single detail from their life with no selection at all', 'This concept has no connection to reading comprehension', 'Selective memory never plays a role in how a memoir is written'], 0),
   ('Why is critical reading important when studying a memoir as a historical or personal source?', ['It helps readers recognize that a memoir reflects one person’s shaped perspective, not an absolute record', 'Critical reading never matters when studying a memoir', 'This concept has no relevance to reading comprehension', 'Every memoir is always a perfectly objective account of events'], 0)]),
M('Sequences: Recursive Formulas',
  'Grade 10 Math strand: a recursive formula defines each term of a sequence based on the value of one or more previous terms, rather than directly from the term’s position.',
  [('What does a recursive formula use to define each term of a sequence?', ['The value of one or more previous terms', 'Only the term’s position number', 'A concept unrelated to sequences', 'A completely random number each time'], 0),
   ('In the sequence defined by a(n) equals a(n-1) plus 3, with a(1) equals 2, what is a(2)?', ['5', '2', '3', '6'], 0),
   ('In the sequence defined by a(n) equals a(n-1) plus 3, with a(1) equals 2, what is a(3)?', ['8', '5', '2', '9'], 0),
   ('Why might a recursive formula be a natural way to describe a savings account that grows by a fixed amount each month?', ['Each month’s balance depends directly on the previous month’s balance plus the fixed deposit', 'Recursive formulas never apply to situations that grow over time', 'This concept has no connection to sequences', 'A savings account balance never depends on any previous value'], 0),
   ('Why might it take longer to find the 50th term of a sequence using a recursive formula compared to an explicit formula?', ['A recursive formula requires calculating every earlier term in order, while an explicit formula can be evaluated directly', 'Recursive formulas always calculate any term faster than an explicit formula', 'This concept has no connection to sequences', 'Explicit and recursive formulas always require exactly the same number of steps'], 0)]),
Sc('Chemistry: Solubility Rules and Precipitation Reactions',
   'Grade 10 Science strand: solubility rules predict whether an ionic compound will dissolve in water, and a precipitation reaction occurs when two soluble solutions combine to form an insoluble solid.',
   [('What do solubility rules help predict?', ['Whether an ionic compound will dissolve in water', 'The exact colour of every chemical compound', 'A concept unrelated to chemistry', 'The temperature at which water boils'], 0),
    ('What is formed in a precipitation reaction?', ['An insoluble solid', 'Only a colourless gas', 'A concept unrelated to precipitation reactions', 'Nothing at all is formed'], 0),
    ('Does a precipitation reaction typically occur when two soluble solutions are combined?', ['Yes', 'No, precipitation reactions never involve combining two solutions', 'A concept unrelated to precipitation reactions', 'Precipitation reactions only occur with solid reactants, never solutions'], 0),
    ('Why might chemists use solubility rules before mixing two solutions in the laboratory?', ['These rules help predict whether a solid precipitate will form, guiding safe and informed experimentation', 'Solubility rules never provide any useful prediction about a reaction’s outcome', 'This concept has no connection to chemistry', 'Mixing solutions always produces the exact same result regardless of the substances used'], 0),
    ('Why might a precipitation reaction be used to test for the presence of a specific ion in a water sample?', ['If a known reagent forms a visible precipitate with a particular ion, its formation can confirm that ion is present', 'Precipitation reactions can never be used to detect ions in a water sample', 'This concept has no relevance to chemistry', 'Water samples never contain any dissolved ions that could react'], 0)]),
H('The Founding of VIA Rail and National Transportation',
  'Grade 10 History strand: VIA Rail was created in the 1970s to operate Canada’s intercity passenger rail service, reflecting the federal government’s role in connecting communities across a vast country.',
  [('In what decade was VIA Rail created?', ['The 1970s', 'The 1920s', 'A concept unrelated to Canadian history', 'The 1990s'], 0),
   ('What type of transportation service does VIA Rail operate?', ['Intercity passenger rail service', 'Only local city bus routes', 'A concept unrelated to VIA Rail', 'Air travel between provinces'], 0),
   ('Does VIA Rail reflect the federal government’s role in connecting communities across Canada?', ['Yes', 'No, VIA Rail has no connection to connecting Canadian communities', 'A concept unrelated to Canadian transportation history', 'Passenger rail service has no connection to national infrastructure'], 0),
   ('Why might a national passenger rail service have been considered important for a country as large and geographically spread out as Canada?', ['It could connect distant communities that might otherwise lack convenient transportation options', 'A national rail service has no benefit for a large, spread-out country', 'This concept has no relevance to Canadian history', 'Distance between communities never affects the need for transportation infrastructure'], 0),
   ('Why might government involvement in a passenger rail service be considered different from a private airline network?', ['A government-run service can prioritize connecting smaller or less profitable communities over pure profit', 'Government and private transportation services always operate with the exact same priorities', 'This concept has no relevance to history', 'Passenger rail and airline networks are never compared in terms of their priorities'], 0)]),
]),

day(86, [
E('Writing: The Op-Ed Rebuttal',
  'Grade 10 English strand: an op-ed rebuttal responds directly to a previously published opinion piece, presenting a counterargument backed by evidence and clear reasoning.',
  [('What does an op-ed rebuttal respond to?', ['A previously published opinion piece', 'A math textbook chapter', 'A concept unrelated to writing', 'A weather forecast'], 0),
   ('Should an op-ed rebuttal be backed by evidence and clear reasoning?', ['Yes', 'No, rebuttals never require any evidence', 'A concept unrelated to writing', 'Only vague opinions are allowed, with no reasoning at all'], 0),
   ('Why might a writer directly quote the original article when writing a rebuttal?', ['It ensures the counterargument accurately addresses the original claims', 'Quoting an article never helps strengthen a rebuttal', 'This concept has no connection to writing', 'Rebuttals should never reference the original argument at all'], 0),
   ('Which of these would most likely appear in an op-ed rebuttal?', ['Contrary to the original article’s claim, recent data actually shows a different trend.', 'Once upon a time, in a faraway kingdom.', 'Add 8 and 7 to get 15.', 'The chemical symbol for gold is Au.'], 0),
   ('Why is tone important to consider when writing a persuasive rebuttal?', ['A respectful, reasoned tone can make an argument more credible and persuasive', 'Tone never affects how persuasive an argument seems', 'This concept has no connection to writing', 'An aggressive tone always makes a rebuttal more convincing'], 0)]),
M('Trigonometry: The Ambiguous Case of the Sine Law',
  'Grade 10 Math strand: the ambiguous case of the sine law occurs when given information about a triangle produces two possible triangles, one, or no valid triangle at all.',
  [('What does the ambiguous case of the sine law describe?', ['A situation where given information can produce two, one, or no valid triangles', 'A situation where only one triangle is ever possible', 'A concept unrelated to trigonometry', 'A rule that never applies to real triangles'], 0),
   ('Can the ambiguous case sometimes result in zero valid triangles?', ['Yes', 'No, a valid triangle can always be formed no matter the given information', 'A concept unrelated to the ambiguous case', 'Every set of given measurements always produces exactly one triangle'], 0),
   ('Does the ambiguous case typically arise when given two sides and a non-included angle?', ['Yes', 'No, the ambiguous case never arises from two sides and a non-included angle', 'A concept unrelated to trigonometry', 'The ambiguous case only arises when given three sides'], 0),
   ('Why is it important to check for the ambiguous case when solving a triangle using the sine law?', ['Failing to check could lead to missing a valid second triangle or assuming an impossible one exists', 'The ambiguous case never affects how a triangle problem should be solved', 'This concept has no connection to trigonometry', 'Every triangle problem produces the exact same single answer regardless of the case'], 0),
   ('Why might a real-world surveying problem require checking for the ambiguous case of the sine law?', ['Multiple valid triangle configurations could represent different possible locations or distances', 'Surveying problems never involve solving triangles using the sine law', 'This concept has no relevance to trigonometry', 'Real-world measurements always eliminate the possibility of an ambiguous case'], 0)]),
Sc('Biology: The Lymphatic System',
   'Grade 10 Science strand: the lymphatic system drains excess fluid from body tissues, transports immune cells, and plays a key role in defending the body against infection.',
   [('What does the lymphatic system drain from body tissues?', ['Excess fluid', 'Only oxygenated blood', 'A concept unrelated to biology', 'Solid waste from digestion'], 0),
    ('Does the lymphatic system transport immune cells throughout the body?', ['Yes', 'No, the lymphatic system never transports any immune cells', 'A concept unrelated to the lymphatic system', 'Immune cells are only ever found in the bloodstream, never the lymphatic system'], 0),
    ('Does the lymphatic system play a role in defending the body against infection?', ['Yes', 'No, the lymphatic system has no connection to fighting infection', 'A concept unrelated to the lymphatic system', 'Infection defense is handled only by the digestive system'], 0),
    ('Why might swollen lymph nodes be a sign that the body is fighting an infection?', ['Lymph nodes contain immune cells that multiply and become active when responding to a threat', 'Swollen lymph nodes never have any connection to fighting an infection', 'This concept has no connection to biology', 'Lymph nodes never change in size or activity for any reason'], 0),
    ('Why is the lymphatic system sometimes described as working alongside the circulatory system?', ['Both systems help move fluids through the body, though they serve different specific roles', 'The lymphatic system operates completely independently with no connection to circulation', 'This concept has no relevance to biology', 'The circulatory and lymphatic systems never interact in the human body'], 0)]),
H('The 1980 Quebec Referendum',
  'Grade 10 History strand: in 1980, Quebec voters rejected a referendum question on pursuing sovereignty-association with Canada, setting the stage for further constitutional debate in the following decades.',
  [('In what year did Quebec hold this early referendum on sovereignty-association?', ['1980', '1995', 'A concept unrelated to Canadian history', '1970'], 0),
   ('Did Quebec voters approve or reject the 1980 referendum question?', ['They rejected it', 'They approved it overwhelmingly', 'A concept unrelated to the 1980 referendum', 'No vote actually took place'], 0),
   ('Did the outcome of the 1980 referendum set the stage for further constitutional debate?', ['Yes', 'No, the 1980 referendum ended all future debate on the topic', 'A concept unrelated to the 1980 referendum', 'Constitutional debate had no connection to this referendum'], 0),
   ('Why might the 1980 referendum result have been significant for Canada’s constitutional discussions in the years that followed?', ['It highlighted ongoing questions about Quebec’s place within Confederation that continued to shape national politics', 'The 1980 referendum had no lasting effect on Canadian constitutional discussions', 'This concept has no relevance to Canadian history', 'Quebec’s role within Confederation was completely settled after this vote'], 0),
   ('Why might comparing the 1980 and 1995 Quebec referendums help students understand shifts in public opinion over time?', ['Examining both votes shows how support for sovereignty-related questions changed across a fifteen-year period', 'Comparing these two referendums never reveals any useful historical information', 'This concept has no relevance to history', 'Public opinion on this issue never changed between 1980 and 1995'], 0)]),
]),

day(87, [
E('Literature: The Role of the Chorus in Greek Tragedy',
  'Grade 10 English strand: the chorus in Greek tragedy comments on the action, offers moral perspective, and helps guide the audience’s emotional response to events on stage.',
  [('What does the chorus do in a Greek tragedy?', ['Comments on the action and offers moral perspective', 'Performs the entire play alone with no other actors', 'A concept unrelated to literature', 'Sells tickets to the audience before the show'], 0),
   ('Can the chorus help guide the audience’s emotional response to events on stage?', ['Yes', 'No, the chorus never has any effect on the audience’s response', 'A concept unrelated to Greek tragedy', 'The chorus is always completely silent throughout the play'], 0),
   ('Why might a playwright use the chorus to comment on a character’s actions rather than having another character do so?', ['The chorus can offer a broader, communal perspective that stands somewhat outside the main plot', 'The chorus never comments on any character’s actions in a Greek tragedy', 'This concept has no connection to literature', 'Only the main characters are ever allowed to comment on the plot'], 0),
   ('Which of these best describes a function of the chorus in Greek tragedy?', ['Providing background information and reflecting on the moral significance of events', 'Building the physical sets used in the theatre', 'Selling refreshments during intermission', 'Writing reviews of the play after it ends'], 0),
   ('Why might modern readers find studying the role of the chorus useful for understanding classical Greek theatre conventions?', ['It reveals how ancient audiences experienced a play differently than audiences do today', 'The chorus has no connection to how ancient Greek theatre worked', 'This concept has no relevance to literature', 'Greek theatre conventions have remained completely unchanged since ancient times'], 0)]),
M('Probability: The Complement Rule',
  'Grade 10 Math strand: the complement rule states that the probability of an event not happening equals one minus the probability of the event happening.',
  [('What does the complement rule calculate?', ['The probability of an event not happening', 'Only the probability of an event definitely happening', 'A concept unrelated to probability', 'The average of two unrelated probabilities'], 0),
   ('If the probability of rain tomorrow is 0.3, what is the probability it does not rain, using the complement rule?', ['0.7', '0.3', '1.3', '0.0'], 0),
   ('Does the complement rule require subtracting a probability from the number one?', ['Yes', 'No, the complement rule never involves subtracting from one', 'A concept unrelated to probability', 'The complement rule only involves adding two probabilities together'], 0),
   ('Why might the complement rule be useful for calculating the probability of at least one success in multiple trials?', ['It can be easier to first find the probability of no successes at all, then subtract from one', 'The complement rule is never useful for problems involving multiple trials', 'This concept has no connection to math', 'At least one success can only ever be calculated by listing every possible outcome'], 0),
   ('If the probability of winning a game is 0.25, what is the probability of not winning?', ['0.75', '0.25', '1.25', '0.5'], 0)]),
Sc('Physics: Sound Waves and the Doppler Effect',
   'Grade 10 Science strand: the Doppler effect describes how the pitch of a sound wave appears to change as its source moves toward or away from an observer.',
   [('What does the Doppler effect describe?', ['How the pitch of a sound appears to change as its source moves', 'How light bends when passing through water', 'A concept unrelated to physics', 'How solid objects melt when heated'], 0),
    ('Does a sound’s pitch appear higher as its source moves toward an observer?', ['Yes', 'No, pitch never changes based on the motion of a sound source', 'A concept unrelated to the Doppler effect', 'Pitch only changes when the observer moves, never the source'], 0),
    ('Does a sound’s pitch appear lower as its source moves away from an observer?', ['Yes', 'No, moving away from an observer never lowers a sound’s apparent pitch', 'A concept unrelated to the Doppler effect', 'Pitch remains completely unchanged regardless of motion'], 0),
    ('Why does an ambulance siren sound higher in pitch as it approaches and lower as it moves away?', ['The sound waves compress as the source approaches and stretch out as it recedes, changing the perceived pitch', 'An ambulance siren’s pitch never actually changes regardless of its motion', 'This concept has no connection to physics', 'The siren’s actual frequency changes based on the driver’s speed'], 0),
    ('Why is the Doppler effect useful for astronomers studying the movement of distant stars and galaxies?', ['Shifts in the light or sound waves from an object can reveal whether it is moving toward or away from Earth', 'The Doppler effect has no application in studying distant stars or galaxies', 'This concept has no relevance to physics', 'Astronomers never use wave behaviour to study the motion of celestial objects'], 0)]),
H('Canada’s Role in the Gulf War',
  'Grade 10 History strand: Canada contributed naval and air forces to the multinational coalition that responded to Iraq’s invasion of Kuwait in the early 1990s Gulf War.',
  [('What did Canada contribute to the multinational coalition during the Gulf War?', ['Naval and air forces', 'No forces of any kind', 'A concept unrelated to Canadian history', 'Only humanitarian food aid'], 0),
   ('What event triggered the multinational coalition’s response during the Gulf War?', ['Iraq’s invasion of Kuwait', 'A concept unrelated to the Gulf War', 'A trade dispute between Canada and the United States', 'An earthquake in the Middle East'], 0),
   ('Did the Gulf War take place in the early 1990s?', ['Yes', 'No, it took place in the 1960s', 'A concept unrelated to the Gulf War', 'The Gulf War never actually occurred'], 0),
   ('Why might Canada’s participation in the Gulf War coalition reflect its broader approach to international conflicts?', ['Canada often contributes to multinational efforts rather than acting alone in international conflicts', 'Canada has never participated in any multinational military coalition', 'This concept has no relevance to Canadian history', 'Canada’s foreign policy never involves cooperating with other countries'], 0),
   ('Why might studying Canada’s role in the Gulf War help students understand the country’s modern military involvement abroad?', ['It shows an example of Canada balancing military contribution with a broader coalition-based approach', 'Canada’s military history has no connection to understanding its modern involvement abroad', 'This concept has no relevance to history', 'Canada has never contributed forces to any international coalition effort'], 0)]),
]),

day(88, [
E('Oral Communication: Storytelling Techniques in Public Speaking',
  'Grade 10 English strand: effective public speakers often use storytelling techniques, such as vivid detail, a clear narrative arc, and personal connection, to engage and persuade an audience.',
  [('What technique do effective public speakers often use to engage an audience?', ['Storytelling techniques', 'Reading directly from a textbook with no eye contact', 'A concept unrelated to oral communication', 'Speaking as quietly as possible'], 0),
   ('Name one storytelling technique a speaker might use, such as vivid detail.', ['Vivid detail', 'A concept unrelated to public speaking', 'A blank, expressionless face', 'Complete silence throughout the entire speech'], 0),
   ('Can a clear narrative arc help an audience follow and stay engaged with a speech?', ['Yes', 'No, a narrative arc never affects audience engagement', 'A concept unrelated to storytelling', 'Audiences are never affected by how a story is structured'], 0),
   ('Why might a speaker share a brief personal story before making a broader persuasive point?', ['A relatable personal story can build an emotional connection before presenting a larger argument', 'Personal stories never help build any connection with an audience', 'This concept has no connection to public speaking', 'A persuasive point is always more effective without any personal story'], 0),
   ('Why is storytelling considered a powerful tool in speeches meant to inspire or motivate an audience?', ['Stories can make abstract ideas feel concrete and emotionally resonant for listeners', 'Storytelling has no effect on how an audience receives a speech', 'This concept has no relevance to oral communication', 'Motivational speeches never rely on any storytelling techniques'], 0)]),
M('Functions: Transformations of Absolute Value Functions',
  'Grade 10 Math strand: transformations of the absolute value function shift, stretch, compress, or reflect its characteristic V-shaped graph.',
  [('What is the characteristic shape of the graph of an absolute value function?', ['A V-shape', 'A straight diagonal line', 'A concept unrelated to functions', 'A circle'], 0),
   ('Does adding a constant outside the absolute value expression shift the graph vertically?', ['Yes', 'No, adding a constant outside never shifts the graph vertically', 'A concept unrelated to transformations', 'Vertical shifts are never possible for absolute value functions'], 0),
   ('Does adding a constant inside the absolute value expression shift the graph horizontally?', ['Yes', 'No, adding a constant inside never shifts the graph horizontally', 'A concept unrelated to transformations', 'Horizontal shifts only apply to quadratic functions, never absolute value functions'], 0),
   ('If the coefficient in front of the absolute value expression is negative, what happens to the graph?', ['It reflects over the x-axis, opening downward', 'The graph disappears completely', 'A concept unrelated to transformations', 'The graph becomes a straight horizontal line'], 0),
   ('Why is understanding transformations of the absolute value function useful for graphing more complex functions quickly?', ['Recognizing the base shape and its shifts allows a graph to be sketched without plotting every point', 'Understanding transformations never helps graph a function more efficiently', 'This concept has no connection to math', 'Every absolute value function must be graphed by plotting each point individually with no shortcuts'], 0)]),
Sc('Earth Science: Groundwater and Aquifers',
   'Grade 10 Science strand: groundwater is stored underground in aquifers, permeable rock or sediment layers that supply wells and springs and can become depleted or contaminated over time.',
   [('Where is groundwater stored?', ['In aquifers', 'Only in visible surface lakes', 'A concept unrelated to earth science', 'Nowhere; groundwater does not actually exist'], 0),
    ('What type of material makes up an aquifer, such as permeable rock or sediment?', ['Permeable rock or sediment layers', 'A concept unrelated to aquifers', 'Solid, impermeable granite only', 'Only ice and snow'], 0),
    ('Can an aquifer become depleted if water is withdrawn faster than it is naturally replenished?', ['Yes', 'No, aquifers can never be depleted under any circumstances', 'A concept unrelated to groundwater', 'Aquifers are always replenished instantly regardless of usage'], 0),
    ('Why might overpumping groundwater from an aquifer cause long-term problems for a community that relies on it?', ['If water is removed faster than it naturally recharges, the aquifer’s supply could decline over time', 'Overpumping groundwater never has any long-term effect on an aquifer’s supply', 'This concept has no connection to earth science', 'Aquifers refill at the exact same rate no matter how much water is removed'], 0),
    ('Why is protecting aquifers from contamination considered important for communities that rely on well water?', ['Contamination can make groundwater unsafe to drink and difficult to clean up once it enters the aquifer', 'Aquifer contamination never affects the safety of well water', 'This concept has no relevance to earth science', 'Groundwater contamination is always immediately and easily reversed'], 0)]),
H('The Canada-US Free Trade Agreement Debate of 1988',
  'Grade 10 History strand: the 1988 federal election became a referendum on the proposed Canada-US Free Trade Agreement, sparking national debate over economic sovereignty and integration.',
  [('What proposed agreement was central to the 1988 federal election debate?', ['The Canada-US Free Trade Agreement', 'A concept unrelated to Canadian history', 'A treaty ending Canada’s membership in NATO', 'An agreement to abolish the Canadian dollar'], 0),
   ('Did the 1988 election spark national debate over economic sovereignty and integration?', ['Yes', 'No, the 1988 election generated no public debate at all', 'A concept unrelated to the Free Trade Agreement debate', 'Economic sovereignty was never a topic of discussion in 1988'], 0),
   ('Was the proposed Free Trade Agreement a major issue in the 1988 federal election?', ['Yes', 'No, trade policy was never discussed during that election', 'A concept unrelated to Canadian history', 'The 1988 election focused only on unrelated environmental policy'], 0),
   ('Why might some Canadians have opposed the Free Trade Agreement out of concern for economic sovereignty?', ['They worried that closer economic ties with the United States could reduce Canada’s independent control over its own economy', 'Concerns about economic sovereignty had no connection to the Free Trade Agreement debate', 'This concept has no relevance to Canadian history', 'Every Canadian citizen agreed completely on this issue with no opposition at all'], 0),
   ('Why might supporters of the Free Trade Agreement have argued it would benefit the Canadian economy?', ['They believed easier access to the large American market could boost Canadian trade and economic growth', 'Supporters of the agreement believed it would have no effect on the Canadian economy at all', 'This concept has no relevance to history', 'Trade agreements never have any connection to a country’s economic growth'], 0)]),
]),

day(89, [
E('Reading: Comparing Book-to-Film Adaptations',
  'Grade 10 English strand: comparing a novel to its film adaptation reveals how different mediums make distinct choices about pacing, visual detail, and which parts of a story to emphasize or cut.',
  [('What can comparing a novel to its film adaptation reveal?', ['How different mediums make distinct choices about pacing and emphasis', 'Nothing useful about either the book or the film', 'A concept unrelated to reading', 'Only the release date of each version'], 0),
   ('Might a film adaptation cut certain scenes or details found in the original novel?', ['Yes', 'No, film adaptations always include every single detail from the novel', 'A concept unrelated to book-to-film adaptations', 'Films are always identical in length and content to the original novel'], 0),
   ('Why might a director choose to condense several chapters of a novel into a single film scene?', ['Film has time constraints that require careful choices about which details to prioritize', 'Directors never make any changes when adapting a novel into a film', 'This concept has no connection to reading comprehension', 'Every novel translates into a film with no need for any changes'], 0),
   ('Why might visual imagery in a film adaptation differ from a reader’s own imagination while reading the novel?', ['A film presents one specific visual interpretation, while a novel allows each reader to imagine details differently', 'Film adaptations always match every reader’s imagined version exactly', 'This concept has no connection to reading comprehension', 'Visual imagery has no connection to how a story is experienced'], 0),
   ('Why is comparing a novel and its film adaptation a valuable exercise for studying storytelling techniques?', ['It highlights how different mediums use distinct tools to convey meaning, pacing, and emotion', 'Comparing a novel and its film adaptation never reveals anything about storytelling techniques', 'This concept has no relevance to reading comprehension', 'Novels and films always use identical storytelling techniques with no differences'], 0)]),
M('Financial Literacy: Currency Exchange and International Finance',
  'Grade 10 Math strand: currency exchange rates determine how much one country’s currency is worth in terms of another, affecting the cost of international travel, trade, and investment.',
  [('What do currency exchange rates determine?', ['How much one country’s currency is worth in terms of another', 'The exact weather conditions in a foreign country', 'A concept unrelated to financial literacy', 'The population size of a country'], 0),
   ('If 1 Canadian dollar equals 0.75 US dollars, how many US dollars would 100 Canadian dollars be worth?', ['75 US dollars', '100 US dollars', '133 US dollars', '25 US dollars'], 0),
   ('Can exchange rates affect the cost of international travel?', ['Yes', 'No, exchange rates never affect the cost of travelling to another country', 'A concept unrelated to currency exchange', 'Travel costs are never influenced by currency values'], 0),
   ('Why might a Canadian traveller pay more for the same hotel room if the Canadian dollar weakens against the local currency?', ['A weaker Canadian dollar buys less of the foreign currency, increasing the cost when converted', 'A weaker currency always makes purchases cheaper when travelling abroad', 'This concept has no connection to financial literacy', 'Currency strength never affects how much a traveller pays for goods or services'], 0),
   ('Why is understanding currency exchange important for a business that imports goods from another country?', ['Exchange rate changes can directly affect how much the business pays for imported goods over time', 'Currency exchange rates never affect the cost of importing goods', 'This concept has no connection to financial literacy', 'International businesses never need to consider currency values at all'], 0)]),
Sc('Chemistry: Catalysts and Reaction Rates',
   'Grade 10 Science strand: a catalyst speeds up a chemical reaction by providing an alternative pathway with lower activation energy, without being consumed in the reaction itself.',
   [('What does a catalyst do to a chemical reaction?', ['Speeds it up', 'Always slows it down significantly', 'A concept unrelated to chemistry', 'Stops the reaction from occurring at all'], 0),
    ('Is a catalyst consumed during the chemical reaction it speeds up?', ['No', 'Yes, a catalyst is always fully consumed', 'A concept unrelated to catalysts', 'Catalysts are never involved in any chemical reaction'], 0),
    ('Does a catalyst provide an alternative pathway with lower activation energy?', ['Yes', 'No, catalysts always increase the activation energy required', 'A concept unrelated to catalysts', 'Activation energy has no connection to how catalysts work'], 0),
    ('Why might enzymes in the human body be considered a type of biological catalyst?', ['They speed up biochemical reactions in the body without being permanently changed or used up', 'Enzymes have no connection to speeding up chemical reactions in the body', 'This concept has no connection to chemistry', 'Enzymes always slow down every biochemical reaction they are involved in'], 0),
    ('Why are catalysts widely used in industrial chemical processes?', ['They can make reactions proceed faster and more efficiently, often reducing energy costs', 'Catalysts have no practical benefit in industrial chemical processes', 'This concept has no relevance to chemistry', 'Industrial processes never make use of any catalysts'], 0)]),
H('Canada’s Peacekeeping Mission in Rwanda',
  'Grade 10 History strand: Canadian general Roméo Dallaire led the United Nations peacekeeping mission in Rwanda during the 1994 genocide, drawing attention to the limits and challenges of international intervention.',
  [('What role did Canadian general Roméo Dallaire hold in Rwanda in 1994?', ['He led the United Nations peacekeeping mission', 'He served only as a diplomatic translator', 'A concept unrelated to Canadian history', 'He had no involvement in Rwanda at all'], 0),
   ('Did the events in Rwanda in 1994 draw attention to challenges facing international intervention?', ['Yes', 'No, the events in Rwanda raised no questions about international intervention', 'A concept unrelated to peacekeeping history', 'International intervention has no connection to the Rwanda mission'], 0),
   ('Was the mission Dallaire led part of a United Nations peacekeeping effort?', ['Yes', 'No, it had no connection to the United Nations', 'A concept unrelated to Canadian history', 'The mission was organized entirely by Canada alone with no UN involvement'], 0),
   ('Why might Dallaire’s experience in Rwanda have shaped later discussions about the limits of peacekeeping missions?', ['His accounts highlighted how peacekeeping forces sometimes lacked the resources or mandate to prevent mass violence', 'His experience in Rwanda had no influence on later peacekeeping discussions', 'This concept has no relevance to Canadian history', 'Peacekeeping missions were never discussed or reconsidered after these events'], 0),
   ('Why is studying Canada’s peacekeeping history, including difficult missions like Rwanda, valuable for understanding the country’s international role?', ['It shows both the contributions and the real limitations of peacekeeping as a tool for international conflict response', 'Studying difficult historical missions provides no insight into a country’s international role', 'This concept has no relevance to history', 'Peacekeeping missions have no connection to how a country is perceived internationally'], 0)]),
]),

day(90, [
E('Review: Rhetoric, Media, and Literary Analysis (Days 81-89)',
  'Grade 10 English strand review: students revisit existentialist themes, rhetorical analysis, nominalization, podcast journalism, unreliable memoir framing, op-ed rebuttals, the Greek chorus, storytelling in public speaking, and comparing adaptations.',
  [('What do existentialist themes in fiction often explore?', ['Individual freedom, choice, and the search for meaning', 'Only fairy tale settings with no deeper themes', 'A concept unrelated to literature', 'Recipes and cooking instructions'], 0),
   ('What does a rhetorical analysis essay examine?', ['How a speaker or writer uses appeals and devices to persuade an audience', 'Only the biography of the author', 'A concept unrelated to writing', 'A list of unrelated grammar rules'], 0),
   ('What does nominalization do to a verb or adjective?', ['Turns it into a noun', 'Turns it into a question', 'A concept unrelated to grammar', 'Removes it from the sentence entirely'], 0),
   ('What does the chorus do in a Greek tragedy?', ['Comments on the action and offers moral perspective', 'Performs the entire play alone with no other actors', 'A concept unrelated to literature', 'Sells tickets to the audience before the show'], 0),
   ('What can comparing a novel to its film adaptation reveal?', ['How different mediums make distinct choices about pacing and emphasis', 'Nothing useful about either the book or the film', 'A concept unrelated to reading', 'Only the release date of each version'], 0)]),
M('Review: Functions, Geometry, and Probability (Days 81-89)',
  'Grade 10 Math strand review: students revisit inverse quadratic functions, box-and-whisker plots, composite solid volume, combined systems methods, recursive sequences, the ambiguous case, the complement rule, absolute value transformations, and currency exchange.',
  [('When finding the inverse of a function, what roles are switched?', ['The roles of x and y', 'The roles of the slope and intercept', 'A concept unrelated to inverse functions', 'Nothing is switched at all'], 0),
   ('How many key values does a box-and-whisker plot display?', ['Five', 'Two', 'Three', 'Ten'], 0),
   ('What does a recursive formula use to define each term of a sequence?', ['The value of one or more previous terms', 'Only the term’s position number', 'A concept unrelated to sequences', 'A completely random number each time'], 0),
   ('What does the complement rule calculate?', ['The probability of an event not happening', 'Only the probability of an event definitely happening', 'A concept unrelated to probability', 'The average of two unrelated probabilities'], 0),
   ('What is the characteristic shape of the graph of an absolute value function?', ['A V-shape', 'A straight diagonal line', 'A concept unrelated to functions', 'A circle'], 0)]),
Sc('Review: Chemistry, Biology, Physics, and Earth Science (Days 81-89)',
   'Grade 10 Science strand review: students revisit Le Chatelier’s principle, photosynthesis stages, torque, ocean currents, precipitation reactions, the lymphatic system, the Doppler effect, aquifers, and catalysts.',
   [('What does Le Chatelier’s principle describe?', ['How a system at equilibrium shifts to counteract a disturbance', 'How atoms are structured inside a nucleus', 'A concept unrelated to chemistry', 'How light travels through a vacuum'], 0),
    ('How many main stages does photosynthesis consist of?', ['Two', 'One', 'Five', 'A concept unrelated to biology'], 0),
    ('What does torque measure?', ['The turning effect of a force around a pivot point', 'The total mass of an object', 'A concept unrelated to physics', 'The temperature of an object'], 0),
    ('What is formed in a precipitation reaction?', ['An insoluble solid', 'Only a colourless gas', 'A concept unrelated to precipitation reactions', 'Nothing at all is formed'], 0),
    ('What does a catalyst do to a chemical reaction?', ['Speeds it up', 'Always slows it down significantly', 'A concept unrelated to chemistry', 'Stops the reaction from occurring at all'], 0)]),
H('Review: Cold War Era to Modern Canada (Days 81-89)',
  'Grade 10 History strand review: students revisit draft dodgers, the Canada Pension Plan, the Berlin Wall, the Green Revolution, VIA Rail, the 1980 referendum, the Gulf War, the Free Trade Agreement debate, and the Rwanda peacekeeping mission.',
  [('What did Canada become for many American draft resisters during the Vietnam War?', ['A destination seeking refuge', 'A place that actively rejected all American immigrants', 'A concept unrelated to the Vietnam War era', 'A country that sent its own citizens to fight in Vietnam'], 0),
   ('In what decade was the Canada Pension Plan established?', ['The 1960s', 'The 1920s', 'A concept unrelated to Canadian history', 'The 1990s'], 0),
   ('What structure divided the city of Berlin during the Cold War?', ['The Berlin Wall', 'A concept unrelated to Canadian history', 'The Great Wall', 'The Iron Curtain railway'], 0),
   ('What proposed agreement was central to the 1988 federal election debate?', ['The Canada-US Free Trade Agreement', 'A concept unrelated to Canadian history', 'A treaty ending Canada’s membership in NATO', 'An agreement to abolish the Canadian dollar'], 0),
   ('What role did Canadian general Roméo Dallaire hold in Rwanda in 1994?', ['He led the United Nations peacekeeping mission', 'He served only as a diplomatic translator', 'A concept unrelated to Canadian history', 'He had no involvement in Rwanda at all'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_81_90)
    append_to(10, g10_81_90)
