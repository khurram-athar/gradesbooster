#!/usr/bin/env python3
"""Grade 5, Days 151-160 -- extends Grade 5 from 150 to 160 days. Modeled
exactly on gen_grade5_days141_150.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 5 Days 1-150
topics (see data/grade5.json), which already densely cover nearly the
entire grade 5 curriculum across all four subjects. New topics: euphemisms,
formal versus informal language registers, writing a mystery story with
clues, dangling and misplaced modifiers, understanding tone versus mood,
using hyphens correctly, evaluating online reviews for reliability, writing
a comparison shopping report, and paraphrasing versus plagiarizing for
Language; tessellations, dividing three-digit numbers by two-digit numbers,
solving equations with variables on both sides, capacity and displacement,
nets of triangular prisms, probability trees for two events, unit
conversions within the metric system, mean absolute deviation, and
budgeting for a school fundraiser for Math; the rock-paper-scissors of food
webs (producers, consumers, and decomposers as a system), the greenhouse
gases behind climate change, simple pulleys and mechanical advantage
revisited through block and tackle systems, bioluminescent deep-sea
creatures, the properties of sound insulation, plate boundaries and
mountain formation, the process of pasteurization, migratory bird corridors,
and renewable energy in focus: hydrogen fuel cells for Science; and the
role of the Auditor Generals reports, Canadas equalization program in
practice, the Underground Railroads Ontario terminus communities, treaty
rights and natural resource sharing, the role of the Chief Electoral
Officer, Canadas supply management system, the history of Canadian
currency design, interprovincial migration patterns, and the role of civic
volunteers and community associations for Social Studies -- none of those
exact ideas appear in Days 1-150. Day 160 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior 10-day
batch (drawing one representative quiz question per subject from each of
the first five days of the batch, Days 151-155, exactly as Day 150 drew
from Days 141-145).
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are dropped entirely, matching
the rest of Grade 5 Days 1-150 (e.g. "Canadas" not "Canada's",
"governments" not "government's").
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


def _rebalance_answer_positions(days, seed=20260809):
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


g5_151_160 = [
day(151, [
L('Figurative Language: Euphemisms',
  'Grade 5 Language strand: a euphemism is a mild or indirect word or phrase used in place of a harsher or more blunt one, such as passed away instead of died, to soften a difficult idea.',
  [('What is a euphemism?', ['A mild or indirect word or phrase used in place of a harsher one', 'A word that rhymes with another word', 'A word borrowed from another language', 'A sentence with no verb'], 0),
   ('Which phrase is a euphemism for died?', ['Passed away', 'Ran quickly', 'Jumped high', 'Ate lunch'], 0),
   ('Why might a speaker choose a euphemism instead of a blunt word?', ['To soften a difficult or uncomfortable idea', 'Euphemisms always make an idea sound harsher', 'This concept has no connection to figurative language', 'A euphemism always confuses the reader with no purpose'], 0),
   ('Which of these phrases is most likely a euphemism for being fired from a job?', ['Let go', 'Promoted quickly', 'Given a raise', 'Hired again'], 0),
   ('Why is it useful for a reader to recognize euphemisms in a text?', ['It helps the reader understand the true meaning behind softened language', 'Euphemisms never carry any hidden meaning', 'This concept has no relevance to reading', 'Euphemisms always state ideas in the bluntest way possible'], 0)]),
M('Geometry: Tessellations — Tiling a Plane with Shapes',
  'Grade 5 Math strand: a tessellation is a pattern of one or more shapes that repeats to cover a flat surface completely, with no gaps or overlaps.',
  [('What is a tessellation?', ['A pattern of shapes that covers a surface with no gaps or overlaps', 'A single shape drawn once on paper', 'A pattern that always leaves large gaps', 'A three-dimensional solid shape'], 0),
   ('Which shape is well known for tessellating a flat surface on its own?', ['A regular hexagon', 'A circle', 'A regular pentagon', 'A cone'], 0),
   ('Why can a circle not tessellate a plane by itself?', ['Circles always leave gaps between them when placed together', 'Circles fit together perfectly with no gaps', 'This concept has no connection to geometry', 'A circle is not considered a shape'], 0),
   ('What must be true at every point where tessellating shapes meet?', ['The shapes must fit together with no gaps or overlaps', 'The shapes must overlap significantly', 'The shapes must leave large empty spaces', 'The shapes must all be different colours'], 0),
   ('Why might artists and designers use tessellations?', ['To create repeating patterns that are visually pleasing and mathematically precise', 'Tessellations are never used outside of mathematics', 'This concept has no relevance to geometry', 'Tessellations can only be made using circles'], 0)]),
Sc('Food Webs: Producers, Consumers, and Decomposers Working Together',
   'Grade 5 Science strand: a food web shows how producers, consumers, and decomposers are connected as energy and nutrients move through an ecosystem, with each group playing a distinct role.',
   [('What role do producers play in a food web?', ['They make their own food, usually using sunlight', 'They break down dead organisms', 'They only eat other animals', 'They provide no energy to the ecosystem'], 0),
    ('What role do decomposers play in a food web?', ['They break down dead plants and animals, returning nutrients to the soil', 'They make food using sunlight', 'They only eat living plants', 'They remove energy from the ecosystem permanently'], 0),
    ('How are consumers different from producers in a food web?', ['Consumers must eat other organisms for energy, while producers make their own food', 'Consumers and producers play the exact same role', 'Consumers always make their own food using sunlight', 'This concept has no connection to food webs'], 0),
    ('Why is a food web considered more accurate than a single food chain?', ['A food web shows the many overlapping feeding connections in an ecosystem, not just one path', 'A food web only ever shows one single path of energy', 'Food chains and food webs are always identical', 'This concept has no relevance to science'], 0),
    ('What might happen to a food web if decomposers were removed entirely?', ['Dead material would build up and nutrients would not return to the soil', 'Nothing would change in the ecosystem', 'Producers would immediately disappear', 'This concept has no connection to ecosystems'], 0)]),
SS('The Auditor Generals Reports — Reviewing Government Spending',
   'Grade 5 Social Studies strand: the Auditor General examines how government departments spend public money and publishes reports that highlight waste, inefficiency, or good practices for elected officials and citizens to review.',
   [('What does the Auditor General examine?', ['How government departments spend public money', 'The weather across Canada', 'The results of sports competitions', 'Private business decisions only'], 0),
    ('What does the Auditor General produce after an examination?', ['Reports that highlight findings about government spending', 'A list of new laws', 'A national holiday calendar', 'A private letter seen by no one'], 0),
    ('Why might a report from the Auditor General matter to citizens?', ['It helps citizens understand whether public money is being used responsibly', 'These reports are never shared with the public', 'This concept has no connection to government', 'The Auditor General has no connection to public spending'], 0),
    ('What might an Auditor Generals report reveal about a government department?', ['Wasteful spending or inefficient use of public money', 'Only positive information with no criticism ever included', 'Information unrelated to money or spending', 'The department private employee schedules only'], 0),
    ('Why is an independent Auditor General considered important in government?', ['Independence helps ensure spending is reviewed fairly, without political influence', 'Independence has no effect on how a report is written', 'This concept has no relevance to social studies', 'An Auditor General is chosen by a single company'], 0)]),
]),
day(152, [
L('Vocabulary: Formal versus Informal Language Registers',
  'Grade 5 Language strand: a register is the level of formality in language, with formal register used in essays and speeches and informal register used in casual conversation with friends.',
  [('What is a language register?', ['The level of formality used in language', 'A type of punctuation mark', 'A list of vocabulary words in a dictionary', 'A grammar rule about verb tenses'], 0),
   ('Where would formal register most likely be used?', ['In a business letter or academic essay', 'In a casual text to a friend', 'In a note passed during recess', 'In a joke shared with a sibling'], 0),
   ('Where would informal register most likely be used?', ['In a casual conversation with friends', 'In a formal research report', 'In an official government document', 'In a court proceeding'], 0),
   ('Why might a writer switch between formal and informal register in different situations?', ['Matching the register to the audience and purpose helps communicate effectively', 'Register never needs to change based on audience', 'This concept has no connection to vocabulary', 'Formal register is always required in every situation'], 0),
   ('Which sentence uses a more formal register?', ['I would like to request additional information regarding this matter.', 'Hey, can you tell me more about this?', 'Gimme more info please.', 'Whats up with this thing?'], 0)]),
M('Number Sense: Dividing Three-Digit Numbers by Two-Digit Numbers',
  'Grade 5 Math strand: dividing a three-digit number by a two-digit number can be done using long division, estimating how many times the divisor fits into each part of the dividend.',
  [('What strategy is commonly used to divide a three-digit number by a two-digit number?', ['Long division', 'Skip counting by ones only', 'Adding the two numbers together', 'Rounding both numbers to the nearest thousand'], 0),
   ('What is 348 divided by 12?', ['29', '28', '30', '27'], 0),
   ('What is 195 divided by 15?', ['13', '12', '14', '15'], 0),
   ('Why is estimating useful before dividing a three-digit number by a two-digit number?', ['It provides a reasonable target to check the final quotient against', 'Estimating always gives the exact same value as the real quotient', 'Estimation is never useful when dividing larger numbers', 'This concept has no connection to number sense'], 0),
   ('What is 432 divided by 16?', ['27', '26', '28', '25'], 0)]),
Sc('The Greenhouse Gases Behind Climate Change',
   'Grade 5 Science strand: greenhouse gases, such as carbon dioxide and methane, trap heat in Earths atmosphere, and human activities like burning fossil fuels have increased their levels, contributing to climate change.',
   [('What do greenhouse gases do in Earths atmosphere?', ['Trap heat, warming the planet', 'Remove all heat from the atmosphere instantly', 'Block sunlight from ever reaching Earth', 'Have no effect on temperature at all'], 0),
    ('Which of these is an example of a greenhouse gas?', ['Carbon dioxide', 'Pure oxygen only', 'Argon', 'Helium'], 0),
    ('What human activity has increased the amount of greenhouse gases in the atmosphere?', ['Burning fossil fuels', 'Planting more trees only', 'Drinking more water', 'Wearing warmer clothing'], 0),
    ('Why are scientists concerned about rising levels of greenhouse gases?', ['Higher levels can lead to a warmer climate and related environmental changes', 'Greenhouse gases have no connection to climate at all', 'Rising levels of greenhouse gases always cool the planet', 'This concept has no relevance to science'], 0),
    ('What is one action that could help reduce greenhouse gas emissions?', ['Using renewable energy sources instead of fossil fuels', 'Burning more coal and oil', 'Cutting down more forests', 'This concept has no connection to climate change'], 0)]),
SS('Canadas Equalization Program — Sharing Wealth in Practice',
   'Grade 5 Social Studies strand: equalization is a federal program that transfers money to provinces with less economic capacity so that all provinces can offer comparable public services, such as health care and education, at similar tax rates.',
   [('What is the goal of Canadas equalization program?', ['To help provinces offer comparable public services at similar tax rates', 'To eliminate all provincial governments', 'To give every province exactly the same population', 'To end all interprovincial trade'], 0),
    ('Which level of government provides equalization payments?', ['The federal government', 'Only municipal governments', 'A private company', 'A foreign government'], 0),
    ('Which provinces are more likely to receive equalization payments?', ['Provinces with less economic capacity relative to others', 'Only the province with the most oil reserves', 'Only provinces bordering the United States', 'Every province receives the exact same amount regardless of need'], 0),
    ('Why might equalization payments matter for services like health care and education?', ['They help ensure residents across provinces can access similar levels of public services', 'Equalization payments only fund national parks', 'Equalization has no connection to public services', 'This concept has no relevance to social studies'], 0),
    ('Why might this program be considered part of Canadian federalism?', ['It reflects cooperation between federal and provincial governments to share resources fairly', 'Federalism has no connection to how money is shared between governments', 'Provinces never interact with the federal government', 'This concept has no connection to Canadian government'], 0)]),
]),
day(153, [
L('Writing: Writing a Mystery Story with Clues',
  'Grade 5 Language strand: a mystery story presents a puzzle for readers to solve, using carefully placed clues, red herrings, and a satisfying resolution that ties the clues together.',
  [('What is the main purpose of clues in a mystery story?', ['To help readers piece together the solution to the puzzle', 'To confuse the reader with no possible solution', 'To end the story immediately', 'To describe the weather in detail'], 0),
   ('What is a red herring in a mystery story?', ['A misleading clue meant to distract the reader from the real solution', 'The main character of the story', 'The setting where the story takes place', 'The title of the mystery'], 0),
   ('Why might a writer plan the ending of a mystery before writing the clues?', ['Planning backward helps ensure the clues logically lead to the solution', 'Planning is never useful for mystery writing', 'This concept has no connection to writing', 'A mystery story never needs an ending'], 0),
   ('What might happen if a mystery story includes no clues at all?', ['Readers would have no fair way to solve the puzzle themselves', 'The story would automatically become nonfiction', 'The story would need no characters', 'The mystery would always be easier to solve'], 0),
   ('Why do readers often enjoy mystery stories?', ['They can actively try to solve the puzzle alongside the characters', 'Readers never enjoy stories with puzzles', 'This concept has no relevance to writing', 'Mystery stories never include a solution'], 0)]),
M('Algebra: Solving Equations with Variables on Both Sides',
  'Grade 5 Math strand: some equations have a variable on both sides, and solving them involves combining like terms and using inverse operations to get the variable alone on one side.',
  [('What does it mean when an equation has a variable on both sides?', ['The unknown letter appears in terms on both sides of the equals sign', 'The equation has no numbers at all', 'The equation cannot be solved under any circumstances', 'The variable only appears once in the entire equation'], 0),
   ('If 2n + 3 = n + 7, what is the value of n?', ['4', '3', '5', '10'], 0),
   ('What is a helpful first step when solving an equation with variables on both sides?', ['Moving all the variable terms to one side of the equation', 'Multiplying every term by zero', 'Ignoring the variable terms completely', 'Removing all the numbers from the equation'], 0),
   ('If 3n + 1 = n + 9, what is the value of n?', ['4', '5', '3', '8'], 0),
   ('Why is it useful to check a solution by substituting it back into the original equation?', ['It confirms both sides of the equation are equal with that value', 'Checking a solution never actually confirms it is correct', 'This concept has no connection to algebra', 'Substituting a value always makes both sides unequal'], 0)]),
Sc('Pulleys and Mechanical Advantage: Block and Tackle Systems',
   'Grade 5 Science strand: a block and tackle system uses multiple pulleys working together to multiply the force applied, making it easier to lift heavy loads, though more rope must be pulled to move the load a given distance.',
   [('What is a block and tackle system?', ['A system that uses multiple pulleys working together to lift heavy loads', 'A single wheel with no rope', 'A tool used only for cutting wood', 'A type of lever with no wheel'], 0),
    ('What is the main benefit of using multiple pulleys instead of just one?', ['It multiplies the force applied, making heavy loads easier to lift', 'It always makes lifting a load harder', 'Multiple pulleys have no effect on the force needed', 'This concept has no relevance to simple machines'], 0),
    ('What is a tradeoff of using a block and tackle system to gain mechanical advantage?', ['More rope must be pulled to move the load the same distance', 'The load becomes impossible to lift at all', 'No rope is needed at all in this system', 'The system always requires less rope than lifting directly'], 0),
    ('Where might a block and tackle system be used in real life?', ['On a sailboat or a construction crane to lift heavy loads', 'Only inside a kitchen refrigerator', 'Only in a musical instrument', 'This concept has no real-world application'], 0),
    ('Why do engineers consider mechanical advantage when designing lifting systems?', ['It helps them determine how much force is needed to move a given load', 'Mechanical advantage has no connection to lifting systems', 'This concept has no relevance to science', 'Mechanical advantage always requires more force, never less'], 0)]),
SS('The Underground Railroads Ontario Terminus Communities',
   'Grade 5 Social Studies strand: many freedom seekers who escaped enslavement in the United States settled in southern Ontario communities such as Windsor, Chatham, and Buxton, which became important terminus points of the Underground Railroad.',
   [('What was a terminus community along the Underground Railroad?', ['A settlement where freedom seekers arrived and often settled permanently', 'A place where enslaved people were recaptured', 'A city located only in the southern United States', 'A type of railway station for trains'], 0),
    ('Which of these is an example of an Ontario terminus community for the Underground Railroad?', ['Chatham', 'Vancouver', 'Winnipeg', 'Halifax'], 0),
    ('Why did many freedom seekers choose to settle in southern Ontario?', ['It was close to the border and offered freedom under British law', 'It was located far from the United States border', 'Ontario had no connection to the Underground Railroad', 'This concept has no relevance to Canadian history'], 0),
    ('What did many of these Ontario communities become known for after settlement?', ['Vibrant communities that contributed to local economic and cultural life', 'Places where no lasting communities were ever formed', 'Areas that immediately became abandoned', 'This concept has no connection to social studies'], 0),
    ('Why is it important for students to learn about these terminus communities today?', ['They highlight an important part of Canadian and Black history', 'These communities have no historical significance', 'This concept has no relevance to social studies', 'They only ever existed in the United States'], 0)]),
]),
day(154, [
L('Grammar: Dangling and Misplaced Modifiers',
  'Grade 5 Language strand: a misplaced modifier is positioned too far from the word it describes, causing confusion, while a dangling modifier describes a word that is missing entirely from the sentence.',
  [('What is a misplaced modifier?', ['A descriptive word or phrase positioned too far from the word it describes', 'A verb that shows action', 'A word that joins two sentences', 'A type of punctuation mark'], 0),
   ('What is a dangling modifier?', ['A modifier that describes a word missing entirely from the sentence', 'A modifier placed correctly next to the word it describes', 'A modifier that only appears in questions', 'A word with no meaning at all'], 0),
   ('Which sentence contains a misplaced modifier?', ['Running quickly, the finish line was reached by the tired runner.', 'The tired runner reached the finish line quickly.', 'The finish line was reached quickly by the tired runner.', 'Running quickly, the tired runner reached the finish line.'], 0),
   ('Why can a misplaced or dangling modifier confuse a reader?', ['It can make a sentence seem to describe the wrong person or thing', 'Modifiers never affect the clarity of a sentence', 'This concept has no connection to grammar', 'A misplaced modifier always makes a sentence clearer'], 0),
   ('How can a writer fix a dangling modifier?', ['By adding or repositioning words so the modifier clearly describes something in the sentence', 'By removing all punctuation from the sentence', 'Dangling modifiers can never be fixed', 'By adding more dangling modifiers to the sentence'], 0)]),
M('Measurement: Capacity and Displacement',
  'Grade 5 Math strand: the capacity of a container can be found by measuring how much liquid it holds, and displacement is a method that measures an objects volume by observing how much liquid it pushes aside when submerged.',
  [('What does capacity measure?', ['How much liquid a container can hold', 'The weight of an object', 'The length of an object', 'The temperature of a liquid'], 0),
   ('What is displacement used to measure?', ['The volume of an object by observing liquid it pushes aside', 'The exact weight of a solid object', 'The colour of a liquid', 'The temperature of an object'], 0),
   ('If a container holds 250 millilitres of water and an object is submerged causing the water level to rise to 300 millilitres, what is the volume of the object?', ['50 millilitres', '250 millilitres', '300 millilitres', '550 millilitres'], 0),
   ('Why might displacement be a useful way to measure the volume of an irregularly shaped object?', ['It does not require knowing a specific formula for the objects shape', 'Displacement only works for perfectly cubed objects', 'Displacement can never measure irregular objects', 'This concept has no connection to measurement'], 0),
   ('What unit might commonly be used to measure capacity?', ['Millilitres or litres', 'Kilograms only', 'Degrees Celsius', 'Metres only'], 0)]),
Sc('Bioluminescent Deep-Sea Creatures',
   'Grade 5 Science strand: some deep-sea creatures produce their own light through a chemical reaction called bioluminescence, which they use to attract prey, communicate, or avoid predators in the dark ocean depths.',
   [('What is bioluminescence?', ['The ability of living things to produce their own light through a chemical reaction', 'The ability to see in complete darkness without any light', 'A type of camouflage using colour changes only', 'A method fish use to breathe underwater'], 0),
    ('Why might a deep-sea creature use bioluminescence to attract prey?', ['The light can lure curious prey close enough to catch', 'Light never attracts other sea creatures', 'This concept has no connection to bioluminescence', 'Bioluminescence only works in bright sunlight'], 0),
    ('Why is the deep ocean an environment where bioluminescence is especially useful?', ['Little to no sunlight reaches those depths, so producing light offers an advantage', 'The deep ocean is always brightly lit by the sun', 'Bioluminescence has no advantage in darkness', 'This concept has no relevance to science'], 0),
    ('Besides attracting prey, what else might bioluminescence help deep-sea creatures do?', ['Communicate with others of their species or startle predators', 'Bioluminescent creatures never interact with predators', 'This concept has no other possible use', 'Only attract prey and nothing else'], 0),
    ('Why do scientists study bioluminescent organisms?', ['To better understand adaptations to extreme deep-sea environments', 'Bioluminescent organisms provide no useful scientific information', 'This concept has no connection to life science', 'Bioluminescence cannot be observed or studied'], 0)]),
SS('Treaty Rights and Natural Resource Sharing',
   'Grade 5 Social Studies strand: treaty rights are the rights held by Indigenous peoples under historic and modern treaties, and they often include agreements about how natural resources such as land, water, and wildlife are used and shared.',
   [('What are treaty rights?', ['Rights held by Indigenous peoples under historic and modern treaties', 'Rights that apply only to non-Indigenous Canadians', 'Rights that were never written down or recorded', 'A type of municipal bylaw'], 0),
    ('What kinds of resources might treaty agreements address?', ['Land, water, and wildlife use', 'Only the naming of new cities', 'Only decisions about national sports teams', 'Only decisions about school curriculum'], 0),
    ('Why might treaty rights be important when discussing natural resource use in Canada today?', ['They can affect decisions about how land and resources are managed and shared', 'Treaty rights have no connection to modern resource use', 'This concept has no relevance to social studies', 'Treaties were never made regarding natural resources'], 0),
    ('Why do governments and Indigenous communities sometimes need to discuss treaty rights together?', ['To ensure resource decisions respect agreements made in treaties', 'Treaty rights never require any discussion', 'This concept has no connection to Canadian history', 'Only non-Indigenous communities are affected by treaties'], 0),
    ('Why is understanding treaty rights considered important for all Canadians?', ['It helps Canadians understand the historic agreements that shape the country today', 'Treaty rights only matter to a small number of people', 'This concept has no relevance to social studies', 'Treaty rights have no connection to Canadian history'], 0)]),
]),
day(155, [
L('Reading: Understanding Tone versus Mood',
  'Grade 5 Language strand: tone is the authors attitude toward a subject, shown through word choice, while mood is the feeling or atmosphere a reader experiences while reading the text.',
  [('What is tone in a piece of writing?', ['The authors attitude toward the subject, shown through word choice', 'The feeling a reader experiences while reading', 'The title of the story', 'The setting where the story takes place'], 0),
   ('What is mood in a piece of writing?', ['The feeling or atmosphere a reader experiences while reading', 'The authors attitude toward the subject', 'A list of characters in the story', 'The exact page count of a book'], 0),
   ('How are tone and mood related but different?', ['Tone comes from the author, while mood is experienced by the reader', 'Tone and mood are always exactly the same thing', 'Mood comes from the author, while tone is experienced by the reader', 'Neither tone nor mood is created through word choice'], 0),
   ('If a story uses words like gloomy, silent, and cold, what mood might it create?', ['A dark or eerie mood', 'A cheerful and bright mood', 'An exciting and energetic mood', 'A mood has nothing to do with word choice'], 0),
   ('Why might recognizing tone help a reader understand an authors purpose?', ['Tone can reveal whether the author is being serious, humorous, critical, or sincere', 'Tone never reveals anything about an authors purpose', 'This concept has no relevance to reading', 'Tone and purpose are always unrelated concepts'], 0)]),
M('Data Management: Probability Trees for Two Events',
  'Grade 5 Math strand: a probability tree diagram shows all possible outcomes of two events happening in sequence, with branches representing each possible choice and its probability.',
  [('What does a probability tree diagram show?', ['All possible outcomes of two events happening in sequence', 'Only the outcome of a single event', 'The average of a set of numbers', 'A single bar representing one data value'], 0),
   ('If you flip a coin twice, how many possible outcomes are shown on a probability tree?', ['Four', 'Two', 'Six', 'Eight'], 0),
   ('What does each branch of a probability tree usually represent?', ['A possible choice or outcome of an event', 'The final answer to the whole problem', 'A single number with no meaning', 'The title of the experiment'], 0),
   ('Why might a probability tree be useful when finding the probability of two events happening together?', ['It helps organize and visualize every possible combination of outcomes', 'It only shows one outcome and ignores the rest', 'This concept has no connection to probability', 'Probability trees can only be used for a single event'], 0),
   ('If a spinner has two equally likely colours and is spun twice, how many total outcomes are possible?', ['Four', 'Two', 'Three', 'Eight'], 0)]),
Sc('The Properties of Sound Insulation',
   'Grade 5 Science strand: sound insulation involves materials that absorb or block sound waves, reducing how much noise passes through walls, floors, or ceilings, often through soft, dense, or thick construction.',
   [('What does sound insulation do?', ['Absorbs or blocks sound waves, reducing noise transmission', 'Increases how loudly sound travels through a wall', 'Has no effect on how sound travels at all', 'Only works for blocking light, not sound'], 0),
    ('Which type of material generally makes better sound insulation?', ['Soft, dense materials', 'Thin, hard, hollow materials', 'Materials that are see-through', 'Materials with no mass at all'], 0),
    ('Why might soft materials, like foam, help absorb sound?', ['They can trap sound waves and convert some of their energy into heat', 'Soft materials always reflect all sound perfectly', 'Soft materials have no effect on sound at all', 'This concept has no connection to science'], 0),
    ('Where might sound insulation commonly be used?', ['In recording studios or between apartment walls', 'Only inside a swimming pool', 'Only on the outside of a car tire', 'This concept has no real-world application'], 0),
    ('Why might engineers consider sound insulation when designing a building?', ['To help reduce unwanted noise between rooms or from outside', 'Sound insulation has no benefit in building design', 'This concept has no relevance to science', 'Sound insulation always increases noise levels'], 0)]),
SS('The Role of the Chief Electoral Officer',
   'Grade 5 Social Studies strand: the Chief Electoral Officer leads Elections Canada, the independent agency responsible for administering federal elections fairly and ensuring the voting process follows Canadian law.',
   [('What agency does the Chief Electoral Officer lead?', ['Elections Canada', 'The Senate', 'The Supreme Court', 'The Bank of Canada'], 0),
    ('What is the Chief Electoral Officers main responsibility?', ['Administering federal elections fairly', 'Writing all federal laws', 'Managing the countrys currency', 'Leading the Canadian Armed Forces'], 0),
    ('Why is it important for the Chief Electoral Officer to be independent from political parties?', ['Independence helps ensure elections are conducted fairly and without political bias', 'Independence has no connection to fair elections', 'The Chief Electoral Officer is always a member of one political party', 'This concept has no relevance to social studies'], 0),
    ('What might Elections Canada help ensure during a federal election?', ['That voting procedures follow Canadian law and are accessible to eligible voters', 'That only one political party is allowed to participate', 'That elections are cancelled if too many people want to vote', 'This concept has no connection to Canadian government'], 0),
    ('Why do Canadians rely on an independent body to oversee elections?', ['It helps maintain public trust in the fairness of the democratic process', 'An independent body has no effect on public trust', 'This concept has no relevance to democracy', 'Elections do not require any oversight at all'], 0)]),
]),
day(156, [
L('Grammar: Using Hyphens Correctly',
  'Grade 5 Language strand: a hyphen joins parts of certain compound words and compound modifiers, such as well-known or six-year-old, helping clarify meaning when words work together to describe something.',
  [('What is one common use of a hyphen?', ['Joining parts of a compound word or compound modifier', 'Ending every sentence in a paragraph', 'Replacing all commas in a text', 'Showing that a word is misspelled'], 0),
   ('Which of these correctly uses a hyphen in a compound modifier?', ['A well-known author wrote the book.', 'A well known author wrote the book, hyphen missing.', 'A well, known author wrote the book.', 'A wellknown author wrote the book.'], 0),
   ('Why might a hyphen be needed in the phrase six-year-old child?', ['It clarifies that the words together describe the childs age as one idea', 'A hyphen is never needed in this type of phrase', 'This concept has no connection to grammar', 'Hyphens only appear at the end of a sentence'], 0),
   ('Which sentence uses a hyphen correctly?', ['She bought a state-of-the-art computer.', 'She bought a state of the art, computer.', 'She bought a state-of the-art computer.', 'She bought a state of-the-art computer.'], 0),
   ('Why might leaving out a needed hyphen sometimes cause confusion?', ['Without the hyphen, a compound modifier might be misread as separate, unrelated words', 'Leaving out a hyphen never changes the meaning of a phrase', 'This concept has no connection to grammar', 'Hyphens are only decorative and never affect meaning'], 0)]),
M('Measurement: Converting Units Within the Metric System',
  'Grade 5 Math strand: the metric system is based on powers of ten, so converting between units, such as millimetres to centimetres or grams to kilograms, involves multiplying or dividing by 10, 100, or 1000.',
  [('What is the metric system based on?', ['Powers of ten', 'Powers of two', 'Random conversion factors', 'The imperial system'], 0),
   ('How many centimetres are in one metre?', ['100', '10', '1000', '10000'], 0),
   ('How many grams are in one kilogram?', ['1000', '100', '10', '10000'], 0),
   ('If a ribbon is 250 centimetres long, how many metres is that?', ['2.5 metres', '25 metres', '0.25 metres', '250 metres'], 0),
   ('Why is converting units within the metric system generally simpler than converting within the imperial system?', ['Metric conversions involve multiplying or dividing by powers of ten', 'Metric conversions require completely random calculations', 'The metric system uses no consistent pattern between units', 'This concept has no connection to measurement'], 0)]),
Sc('Plate Boundaries and Mountain Formation',
   'Grade 5 Science strand: mountains often form at plate boundaries where tectonic plates collide, pushing rock upward over millions of years to create ranges such as the Rocky Mountains.',
   [('What is a plate boundary?', ['The edge where two tectonic plates meet', 'The centre of a single tectonic plate', 'A type of ocean current', 'A layer of the atmosphere'], 0),
    ('How can colliding tectonic plates lead to mountain formation?', ['The collision pushes rock upward over a very long period of time', 'Colliding plates always create flat plains instead of mountains', 'Tectonic plates never interact with each other', 'This concept has no connection to Earth science'], 0),
    ('About how long can it take for a mountain range to form through plate collisions?', ['Millions of years', 'A single day', 'A few weeks', 'One century'], 0),
    ('Which mountain range is an example of one formed by colliding tectonic plates?', ['The Rocky Mountains', 'A sand dune in a desert', 'A small hill in a backyard', 'An artificial ski hill'], 0),
    ('Why do scientists study plate boundaries?', ['To better understand mountain formation, earthquakes, and other geological processes', 'Plate boundaries provide no useful scientific information', 'This concept has no connection to Earth science', 'Plate boundaries never move or change over time'], 0)]),
SS('Canadas Supply Management System',
   'Grade 5 Social Studies strand: supply management is a Canadian system that controls the production of certain farm products, such as dairy and eggs, to help stabilize prices for farmers and maintain a steady supply for consumers.',
   [('What does Canadas supply management system control?', ['The production of certain farm products, such as dairy and eggs', 'The number of students allowed in schools', 'The amount of snow that falls each winter', 'The number of cars manufactured in Canada'], 0),
    ('What is one goal of supply management?', ['To help stabilize prices for farmers', 'To make farm products more expensive with no limit', 'To eliminate farming in Canada entirely', 'To increase imports of every product'], 0),
    ('Which of these products is commonly associated with Canadas supply management system?', ['Dairy', 'Steel', 'Automobiles', 'Electronics'], 0),
    ('Why might a steady supply of certain farm products matter to consumers?', ['It can help ensure product availability and more predictable prices', 'A steady supply has no effect on consumers at all', 'This concept has no connection to social studies', 'Supply management always leads to product shortages'], 0),
    ('Why might farmers support a supply management system?', ['It can provide more predictable income by managing production and pricing', 'Supply management always reduces farmer income to zero', 'Farmers are never affected by how much they produce', 'This concept has no relevance to social studies'], 0)]),
]),
day(157, [
L('Media Literacy: Evaluating Online Reviews for Reliability',
  'Grade 5 Language strand: online reviews can be helpful, but readers should check for signs of reliability, such as detailed explanations, a mix of ratings, and reviewer patterns, since some reviews may be biased or fake.',
  [('What is one sign that an online review might be reliable?', ['It includes detailed, specific explanations for its rating', 'It only uses very short, vague statements', 'It contains no explanation at all', 'It always gives a perfect rating'], 0),
   ('Why might a reader be cautious of a product with only five-star reviews and no negative feedback?', ['A complete lack of criticism can be a sign of fake or filtered reviews', 'Every five-star review is always completely trustworthy', 'This concept has no connection to media literacy', 'Products with only positive reviews are always reliable'], 0),
   ('What might multiple reviews using nearly identical wording suggest?', ['The reviews may not be genuine and could be fake or copied', 'The reviews are always written by different real customers', 'Identical wording has no connection to reliability', 'This concept has no relevance to online reviews'], 0),
   ('Why is it useful to read a mix of positive and negative reviews before making a decision?', ['It can provide a more balanced and realistic understanding of a product', 'Negative reviews are never useful to consider', 'This concept has no connection to media literacy', 'Reading only positive reviews always gives the full picture'], 0),
   ('Why might understanding how to evaluate reviews be an important media literacy skill?', ['It helps consumers make more informed decisions and avoid being misled', 'Reviews never influence how people make decisions', 'This concept has no relevance to media literacy', 'All online reviews are equally reliable no matter the source'], 0)]),
M('Financial Literacy: Budgeting for a School Fundraiser',
  'Grade 5 Math strand: planning a school fundraiser budget involves estimating expected income from sales, subtracting expected costs, and calculating the projected profit to reach a fundraising goal.',
  [('What does a fundraiser budget typically estimate?', ['Expected income and expected costs', 'Only the weather on the day of the event', 'The names of every student in the school', 'The colour of the fundraiser posters'], 0),
   ('If a bake sale expects to earn 300 dollars in sales and spend 80 dollars on supplies, what is the projected profit?', ['220 dollars', '380 dollars', '300 dollars', '80 dollars'], 0),
   ('Why might organizers estimate costs before a fundraiser begins?', ['It helps them understand how much profit they can realistically expect to raise', 'Estimating costs has no effect on planning a fundraiser', 'This concept has no connection to financial literacy', 'Costs are always exactly zero for every fundraiser'], 0),
   ('If a fundraiser goal is 500 dollars and the projected profit is only 350 dollars, what might organizers need to do?', ['Increase sales or reduce costs to reach the goal', 'Ignore the goal completely since it can never be reached', 'Immediately cancel the fundraiser with no adjustments', 'This concept has no connection to budgeting'], 0),
   ('Why is tracking both income and expenses important when planning a fundraiser?', ['It helps ensure the event actually raises money instead of losing money', 'Tracking income and expenses is never useful for a fundraiser', 'This concept has no relevance to financial literacy', 'A fundraiser can never lose money regardless of planning'], 0)]),
Sc('The Process of Pasteurization',
   'Grade 5 Science strand: pasteurization is a process that heats liquids like milk to a specific temperature for a set time to kill harmful bacteria, making the liquid safer to drink without changing it drastically.',
   [('What is the main purpose of pasteurization?', ['To kill harmful bacteria in a liquid, making it safer to consume', 'To freeze a liquid completely solid', 'To remove all colour from a liquid', 'To add more bacteria to a liquid'], 0),
    ('What is commonly pasteurized to make it safer to drink?', ['Milk', 'Sand', 'Air', 'Rocks'], 0),
    ('How does pasteurization typically kill harmful bacteria?', ['By heating the liquid to a specific temperature for a set amount of time', 'By freezing the liquid for several days', 'By exposing the liquid to bright sunlight only', 'By adding large amounts of salt only'], 0),
    ('Why might pasteurization be considered an important food safety process?', ['It helps reduce the risk of illness caused by harmful bacteria in food and drinks', 'Pasteurization has no effect on food safety at all', 'This concept has no connection to science', 'Pasteurization always makes a liquid more dangerous to drink'], 0),
    ('Who is credited with developing the process that led to pasteurization?', ['Louis Pasteur', 'A modern-day chef', 'An ancient Roman farmer', 'A recent Canadian inventor'], 0)]),
SS('The History of Canadian Currency Design',
   'Grade 5 Social Studies strand: Canadian currency has changed over time, featuring different portraits, symbols, and security features on coins and bank notes that reflect the countrys history and values.',
   [('What might Canadian currency feature on its coins and bank notes?', ['Portraits, symbols, and security features reflecting Canadas history', 'Only blank spaces with no images at all', 'Foreign leaders exclusively', 'Random unrelated images chosen by chance'], 0),
    ('Why might security features be added to Canadian bank notes?', ['To help prevent counterfeiting', 'Security features have no purpose on currency', 'To make bank notes easier to lose', 'This concept has no connection to currency'], 0),
    ('How has the design of Canadian currency changed over time?', ['New portraits, images, and security features have been introduced across different eras', 'Canadian currency design has never changed since Confederation', 'Only the size of coins has ever changed', 'This concept has no relevance to social studies'], 0),
    ('Why might studying currency design tell us something about a countrys history?', ['The images and symbols chosen often reflect important people, places, or values', 'Currency design has no connection to a countrys history or identity', 'This concept has no relevance to social studies', 'Currency images are chosen completely at random'], 0),
    ('What government institution is closely connected to the design and issuing of Canadian bank notes?', ['The Bank of Canada', 'A private international company', 'A local school board', 'A municipal government'], 0)]),
]),
day(158, [
L('Writing: Writing a Comparison Shopping Report',
  'Grade 5 Language strand: a comparison shopping report presents information about similar products, comparing features such as price, quality, and value, to help a reader make an informed purchasing decision.',
  [('What is the main purpose of a comparison shopping report?', ['To help a reader make an informed decision by comparing similar products', 'To describe a single product with no comparison at all', 'To tell a fictional story about shopping', 'To list random facts unrelated to any product'], 0),
   ('Which of these might a comparison shopping report typically compare?', ['Price, quality, and features of similar products', 'The weather forecast for the week', 'A list of unrelated historical events', 'The plot of a favourite novel'], 0),
   ('Why might a writer use a table or chart in a comparison shopping report?', ['It can organize information clearly, making it easy to compare items side by side', 'Tables and charts are never useful in this kind of writing', 'This concept has no connection to writing', 'A comparison report must never include any organized information'], 0),
   ('What might a writer include after comparing several products in a report?', ['A recommendation based on the comparison', 'A completely unrelated topic with no connection to the report', 'No conclusion of any kind', 'A description of an unrelated fictional character'], 0),
   ('Why might this type of writing be useful in everyday life?', ['It helps develop the skill of making informed decisions before spending money', 'This type of writing serves no real purpose', 'This concept has no relevance to writing', 'Comparison reports are never useful for making decisions'], 0)]),
M('Geometry: Nets of Triangular Prisms',
  'Grade 5 Math strand: a net is a two-dimensional pattern that can be folded to form a three-dimensional shape, and the net of a triangular prism includes two triangular faces and three rectangular faces.',
  [('What is a net in geometry?', ['A two-dimensional pattern that can be folded into a three-dimensional shape', 'A three-dimensional shape with no flat faces', 'A type of graph used for data', 'A tool used only for measuring angles'], 0),
   ('How many triangular faces does the net of a triangular prism include?', ['Two', 'One', 'Three', 'Four'], 0),
   ('How many rectangular faces does the net of a triangular prism include?', ['Three', 'Two', 'Four', 'One'], 0),
   ('Why might building a net help you understand a three-dimensional shape better?', ['It shows how the flat faces connect and fold together to form the solid', 'Building a net never helps with understanding three-dimensional shapes', 'This concept has no connection to geometry', 'A net always has the exact same number of faces as any other net'], 0),
   ('If you fold the net of a triangular prism correctly, what shape results?', ['A triangular prism', 'A cube', 'A cone', 'A sphere'], 0)]),
Sc('Migratory Bird Corridors',
   'Grade 5 Science strand: a migratory bird corridor is a route that birds travel along during seasonal migration, often following coastlines, rivers, or mountain ranges to find food and suitable stopover habitats.',
   [('What is a migratory bird corridor?', ['A route birds travel along during seasonal migration', 'A cage used to keep birds indoors', 'A type of birdhouse built for nesting', 'A permanent home where birds never move'], 0),
    ('What might a migratory corridor commonly follow?', ['Coastlines, rivers, or mountain ranges', 'Random paths with no consistent pattern', 'Only underground tunnels', 'Only city streets'], 0),
    ('Why do birds use stopover habitats along a migration corridor?', ['To rest and find food during their long journey', 'Stopover habitats have no purpose for migrating birds', 'Birds never need to rest during migration', 'This concept has no connection to science'], 0),
    ('Why might protecting migratory bird corridors be important for conservation?', ['Losing habitat along these routes can threaten bird populations that depend on them', 'Protecting these corridors has no effect on bird populations', 'This concept has no relevance to science', 'Migratory birds never rely on specific habitats'], 0),
    ('Why might birds migrate seasonally in the first place?', ['To find better food sources or breeding conditions as seasons change', 'Birds never migrate for any reason', 'This concept has no connection to living things', 'Migration only happens during the summer season'], 0)]),
SS('Interprovincial Migration Patterns in Canada',
   'Grade 5 Social Studies strand: interprovincial migration refers to Canadians moving from one province or territory to another, often influenced by factors such as job opportunities, cost of living, or climate.',
   [('What does interprovincial migration mean?', ['Canadians moving from one province or territory to another', 'People moving between different countries', 'Animals migrating between provinces', 'A type of government election'], 0),
    ('What is one factor that might influence someones decision to move to a different province?', ['Job opportunities', 'The colour of the provincial flag', 'The name of the provincial capital', 'The number of letters in the province name'], 0),
    ('Why might the cost of living affect interprovincial migration?', ['People may move to provinces where housing and daily expenses are more affordable', 'Cost of living has no connection to where people choose to live', 'This concept has no relevance to social studies', 'The cost of living is always identical in every province'], 0),
    ('Why might governments track interprovincial migration patterns?', ['To understand population changes and plan services like schools and housing', 'Tracking migration patterns serves no purpose for governments', 'This concept has no connection to social studies', 'Population data is never useful for planning services'], 0),
    ('Why might a province experiencing population growth need to plan carefully?', ['Growth can increase demand for housing, schools, and other public services', 'Population growth never affects the need for public services', 'This concept has no relevance to social studies', 'Provinces never experience changes in population'], 0)]),
]),
day(159, [
L('Writing: Paraphrasing versus Plagiarizing',
  'Grade 5 Language strand: paraphrasing means restating someone elses ideas in your own words while giving credit to the original source, while plagiarizing means using someone elses words or ideas without permission or credit.',
  [('What does paraphrasing mean?', ['Restating someone elses ideas in your own words while giving credit', 'Copying text directly without any changes or credit', 'Making up new ideas with no connection to a source', 'Translating a text into a different language only'], 0),
   ('What does plagiarizing mean?', ['Using someone elses words or ideas without permission or credit', 'Properly citing every source used in a report', 'Restating an idea using entirely original wording', 'Writing an entirely original piece with no outside sources'], 0),
   ('Why is it important to give credit to the original source when paraphrasing?', ['It shows honesty about where the ideas came from and avoids plagiarism', 'Giving credit is never necessary when paraphrasing', 'This concept has no connection to writing', 'Paraphrasing always removes the need to credit a source'], 0),
   ('Which of these is an example of paraphrasing rather than plagiarizing?', ['Restating a sources main idea in your own words with a citation', 'Copying a paragraph word for word with no citation', 'Submitting someone elses report as your own', 'Using another persons exact words without any credit'], 0),
   ('Why might a writer choose to paraphrase instead of directly quoting a source?', ['It can help the writer show understanding of the ideas in their own voice', 'Paraphrasing is never useful when writing a report', 'This concept has no relevance to writing', 'Paraphrasing always requires copying text exactly'], 0)]),
M('Data Management: Mean Absolute Deviation',
  'Grade 5 Math strand: mean absolute deviation measures how spread out a set of data is from its mean, by finding the average distance of each data point from the mean value.',
  [('What does mean absolute deviation measure?', ['How spread out a set of data is from its mean', 'The single largest value in a data set', 'The exact number of values in a data set', 'The mode of a data set'], 0),
   ('What is the first step in finding the mean absolute deviation of a data set?', ['Finding the mean of the data set', 'Finding the largest value in the data set only', 'Multiplying every value by ten', 'Removing half of the values from the data set'], 0),
   ('If a data sets values are very close to the mean, what would you expect about its mean absolute deviation?', ['It would be relatively small', 'It would always be extremely large', 'Mean absolute deviation cannot be calculated in this case', 'This concept has no connection to data management'], 0),
   ('Why might a smaller mean absolute deviation suggest more consistent data?', ['It shows that data points are generally closer to the mean value', 'A smaller mean absolute deviation always means the data is completely random', 'Mean absolute deviation never reflects consistency in data', 'This concept has no relevance to data management'], 0),
   ('Why might comparing the mean absolute deviation of two data sets be useful?', ['It helps show which data set has values that are more spread out', 'Comparing mean absolute deviation never provides useful information', 'This concept has no connection to data management', 'Mean absolute deviation is identical for every data set'], 0)]),
Sc('Renewable Energy in Focus: Hydrogen Fuel Cells',
   'Grade 5 Science strand: a hydrogen fuel cell produces electricity through a chemical reaction between hydrogen and oxygen, releasing mainly water vapour as a byproduct, offering a clean alternative energy source.',
   [('What does a hydrogen fuel cell produce through a chemical reaction?', ['Electricity', 'Only heat with no electricity produced', 'Solid rock', 'Sound waves only'], 0),
    ('What two substances react inside a hydrogen fuel cell?', ['Hydrogen and oxygen', 'Carbon and nitrogen', 'Sodium and chlorine', 'Iron and sulfur'], 0),
    ('What is the main byproduct released by a hydrogen fuel cell?', ['Water vapour', 'Thick black smoke', 'Solid ash', 'Liquid oil'], 0),
    ('Why might hydrogen fuel cells be considered a clean energy source?', ['They produce mainly water vapour rather than harmful pollutants', 'They always release large amounts of harmful pollution', 'Hydrogen fuel cells have no connection to clean energy', 'This concept has no relevance to renewable energy'], 0),
    ('Where might hydrogen fuel cells be used as a source of power?', ['In some vehicles or buildings as an alternative to fossil fuels', 'Only inside a household refrigerator', 'Only in outer space with no other applications', 'This concept has no real-world application'], 0)]),
SS('The Role of Civic Volunteers and Community Associations',
   'Grade 5 Social Studies strand: civic volunteers and community associations are residents and groups who contribute time and effort to improve their neighbourhoods, organize events, and advocate for local needs.',
   [('What do civic volunteers typically contribute to their community?', ['Their time and effort to improve their neighbourhood', 'Only money with no personal involvement', 'Nothing, since volunteers have no impact', 'Only formal government services'], 0),
    ('What is a community association?', ['A group of residents who work together to organize events and advocate for local needs', 'A branch of the federal government', 'A private international corporation', 'A type of national sports league'], 0),
    ('What might a community association organize for local residents?', ['Neighbourhood clean-up days or community events', 'National elections', 'International trade agreements', 'Federal court cases'], 0),
    ('Why might civic volunteers be considered an important part of a healthy community?', ['They help address local needs that might otherwise go unmet', 'Civic volunteers have no positive effect on a community', 'This concept has no connection to social studies', 'Communities never benefit from volunteer efforts'], 0),
    ('Why might a community association advocate to local government on behalf of residents?', ['To help ensure the concerns and needs of the community are heard', 'Community associations are never allowed to contact local government', 'This concept has no relevance to social studies', 'Local government never considers input from residents'], 0)]),
]),
day(160, [
L('Language Review: Figurative Language, Grammar, Reading, and Media Literacy',
  'Grade 5 Language strand review: students revisit euphemisms, formal versus informal register, mystery story writing, dangling and misplaced modifiers, and tone versus mood.',
  [('What is a euphemism?', ['A mild or indirect word or phrase used in place of a harsher one', 'A word that rhymes with another word', 'A word borrowed from another language', 'A sentence with no verb'], 0),
   ('What is a language register?', ['The level of formality used in language', 'A type of punctuation mark', 'A list of vocabulary words in a dictionary', 'A grammar rule about verb tenses'], 0),
   ('What is a red herring in a mystery story?', ['A misleading clue meant to distract the reader from the real solution', 'The main character of the story', 'The setting where the story takes place', 'The title of the mystery'], 0),
   ('What is a misplaced modifier?', ['A descriptive word or phrase positioned too far from the word it describes', 'A verb that shows action', 'A word that joins two sentences', 'A type of punctuation mark'], 0),
   ('What is tone in a piece of writing?', ['The authors attitude toward the subject, shown through word choice', 'The feeling a reader experiences while reading', 'The title of the story', 'The setting where the story takes place'], 0)]),
M('Math Review: Geometry, Number Sense, Algebra, and Measurement',
  'Grade 5 Math strand review: students revisit tessellations, dividing three-digit by two-digit numbers, equations with variables on both sides, capacity and displacement, and probability trees.',
  [('What is a tessellation?', ['A pattern of shapes that covers a surface with no gaps or overlaps', 'A single shape drawn once on paper', 'A pattern that always leaves large gaps', 'A three-dimensional solid shape'], 0),
   ('What strategy is commonly used to divide a three-digit number by a two-digit number?', ['Long division', 'Skip counting by ones only', 'Adding the two numbers together', 'Rounding both numbers to the nearest thousand'], 0),
   ('If 2n + 3 = n + 7, what is the value of n?', ['4', '3', '5', '10'], 0),
   ('What does displacement measure?', ['The volume of an object by observing liquid it pushes aside', 'The exact weight of a solid object', 'The colour of a liquid', 'The temperature of an object'], 0),
   ('What does a probability tree diagram show?', ['All possible outcomes of two events happening in sequence', 'Only the outcome of a single event', 'The average of a set of numbers', 'A single bar representing one data value'], 0)]),
Sc('Science Review: Ecosystems, Climate, Simple Machines, and Ocean Life',
   'Grade 5 Science strand review: students revisit food webs, greenhouse gases, block and tackle pulley systems, bioluminescent deep-sea creatures, and sound insulation.',
   [('What role do producers play in a food web?', ['They make their own food, usually using sunlight', 'They break down dead organisms', 'They only eat other animals', 'They provide no energy to the ecosystem'], 0),
    ('What do greenhouse gases do in Earths atmosphere?', ['Trap heat, warming the planet', 'Remove all heat from the atmosphere instantly', 'Block sunlight from ever reaching Earth', 'Have no effect on temperature at all'], 0),
    ('What is the main benefit of using multiple pulleys instead of just one?', ['It multiplies the force applied, making heavy loads easier to lift', 'It always makes lifting a load harder', 'Multiple pulleys have no effect on the force needed', 'This concept has no relevance to simple machines'], 0),
    ('What is bioluminescence?', ['The ability of living things to produce their own light through a chemical reaction', 'The ability to see in complete darkness without any light', 'A type of camouflage using colour changes only', 'A method fish use to breathe underwater'], 0),
    ('What does sound insulation do?', ['Absorbs or blocks sound waves, reducing noise transmission', 'Increases how loudly sound travels through a wall', 'Has no effect on how sound travels at all', 'Only works for blocking light, not sound'], 0)]),
SS('Social Studies Review: Government Oversight, History, and Community',
   'Grade 5 Social Studies strand review: students revisit the Auditor General, equalization payments, Underground Railroad terminus communities, treaty rights, and the Chief Electoral Officer.',
   [('What does the Auditor General examine?', ['How government departments spend public money', 'The weather across Canada', 'The results of sports competitions', 'Private business decisions only'], 0),
    ('What is the goal of Canadas equalization program?', ['To help provinces offer comparable public services at similar tax rates', 'To eliminate all provincial governments', 'To give every province exactly the same population', 'To end all interprovincial trade'], 0),
    ('What was a terminus community along the Underground Railroad?', ['A settlement where freedom seekers arrived and often settled permanently', 'A place where enslaved people were recaptured', 'A city located only in the southern United States', 'A type of railway station for trains'], 0),
    ('What are treaty rights?', ['Rights held by Indigenous peoples under historic and modern treaties', 'Rights that apply only to non-Indigenous Canadians', 'Rights that were never written down or recorded', 'A type of municipal bylaw'], 0),
    ('What agency does the Chief Electoral Officer lead?', ['Elections Canada', 'The Senate', 'The Supreme Court', 'The Bank of Canada'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_151_160)
    append_to(5, g5_151_160)
