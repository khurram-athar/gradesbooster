#!/usr/bin/env python3
"""Grade 3, Days 161-170 -- extends Grade 3 from 160 to 170 days. Modeled
exactly on gen_grade3_days151_160.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-160
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum many times over. Every (subject, title)
pair below was checked against a full dump of Days 1-160 and confirmed to
be new. New topics for this batch: using parentheses for extra
information, jargon, following multi-step instructions, writing a
limerick, using visual aids during a presentation, correlative
conjunctions, identifying an authors intended audience, writing a
weather report, and clipped words for Language; rounding to the nearest
10 000, parallel and perpendicular lines, reading a bar graph with a
scale of more than one, finding missing factors, ordering fractions with
the same denominator, dividing using repeated subtraction, choosing the
right unit of measurement, creating a number pattern using a rule, and
making a simple budget for a class event for Math; penguins, kangaroos
and marsupial adaptations, the aurora borealis, spiders and their webs,
sonar, the forest canopy, igloos and snow insulation, chameleons, and
woodpeckers for Science; and the Canadian Border Services Agency,
Indigenous languages of Canada, Ontarios Lieutenant Governor, the
Canadian Armed Forces, the Canada-US border, ferries and water
transportation, the Ontario Legislature at Queens Park, national
wildlife areas and migratory bird sanctuaries, and the Trans-Canada
Trail for Social Studies -- none of those exact ideas appear in Days
1-160. Day 170 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch, with review
titles written to be textually distinct from every earlier review days
title (e.g. Day 150s and Day 160s). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in
title/summary/question/option text; apostrophes are dropped entirely
(e.g. Canadas instead of Canada with an apostrophe s), matching the
convention established in Days 111-160.

Invocation (matches the 151-160 script):
  cd ~/gradesbooster && python3 gen_grade3_days161_170.py
followed by:
  cd ~/gradesbooster && python3 build_json.py --grade 3
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L3 = 'https://tvolearn.com/pages/grade-3-language'
M3 = 'https://tvolearn.com/pages/grade-3-mathematics'
S3 = 'https://tvolearn.com/pages/grade-3-science-and-technology'
SS3 = 'https://tvolearn.com/pages/grade-3-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 3 Language',
    'TVO Learn: Grade 3 Mathematics',
    'TVO Learn: Grade 3 Science and Technology',
    'TVO Learn: Grade 3 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L3, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M3, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S3, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS3, q)


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


g3_161_170 = [
day(161, [
L('Grammar: Using Parentheses for Extra Information',
  'Grade 3 Language strand: parentheses are used to add extra information or a side comment to a sentence without changing its main meaning.',
  [('What do parentheses add to a sentence?', ['Extra information or a side comment', 'A brand new subject', 'A completely different sentence', 'A silent letter'], 0),
   ('Which sentence correctly uses parentheses?', ['My dog (a small brown terrier) loves to run.', 'My dog a small brown terrier loves to run.', 'My dog, (a small brown terrier loves to run.', 'My dog a small brown terrier) loves to run.'], 0),
   ('Does the information inside parentheses usually change the main meaning of a sentence?', ['No, it adds extra detail without changing the main meaning', 'Yes, it always changes the meaning completely', 'It removes the meaning entirely', 'It replaces the subject of the sentence'], 0),
   ('What kind of punctuation mark are parentheses?', ['A pair of marks that wrap around extra information', 'A single mark placed only at the end of a sentence', 'A mark used only in titles', 'A mark that replaces a period'], 0),
   ('Why might a writer choose to use parentheses instead of writing a whole new sentence?', ['To add a quick extra detail without interrupting the flow', 'To remove all detail from the writing', 'To make the sentence impossible to read', 'To end the sentence early'], 0)]),
M('Number: Rounding to the Nearest 10 000',
  'Grade 3 Math strand: to round a number to the nearest 10 000, look at the thousands digit; if it is 5 or more, round up, and if it is less than 5, round down.',
  [('What is 47 000 rounded to the nearest 10 000?', ['50 000', '40 000', '47 000', '45 000'], 0),
   ('What is 32 000 rounded to the nearest 10 000?', ['30 000', '40 000', '32 000', '35 000'], 0),
   ('Which digit do you look at to round a number to the nearest 10 000?', ['The thousands digit', 'The ones digit', 'The tens digit', 'The hundreds digit'], 0),
   ('If the thousands digit is 5 or more, what should you do when rounding to the nearest 10 000?', ['Round up', 'Round down', 'Leave the number unchanged', 'Round to the nearest 100 instead'], 0),
   ('What is 85 400 rounded to the nearest 10 000?', ['90 000', '80 000', '85 000', '85 400'], 0)]),
Sc('Science: Penguins and Their Adaptations for Cold Ocean Habitats',
   'Grade 3 Science strand: penguins are flightless birds with thick layers of fat and tightly packed feathers that help them stay warm in icy ocean habitats.',
   [('What helps penguins stay warm in cold water?', ['A thick layer of fat and tightly packed feathers', 'A layer of fur like a bear', 'Hollow bones filled with air only', 'A shell covering their whole body'], 0),
    ('Can penguins fly?', ['No, penguins are flightless birds', 'Yes, penguins fly long distances every day', 'Only baby penguins can fly', 'Penguins fly only underwater'], 0),
    ('What do penguins use their wings for instead of flying?', ['Swimming through water', 'Digging burrows underground', 'Building nests in trees', 'Carrying food in their wings'], 0),
    ('Where do many penguins live?', ['Cold ocean habitats, often near Antarctica', 'Hot deserts', 'Rainforests', 'Mountain caves'], 0),
    ('Why might penguins huddle together in large groups?', ['To share warmth and stay protected from the cold', 'To confuse predators with noise only', 'To build a single giant nest', 'To find food faster in the ocean'], 0)]),
SS('Social Studies: The Canadian Border Services Agency and Keeping Our Borders Safe',
   'Grade 3 Social Studies strand: the Canadian Border Services Agency helps keep the country safe by checking travellers and goods entering Canada at airports, land crossings, and ports.',
   [('What does the Canadian Border Services Agency help do?', ['Keep the country safe by checking travellers and goods entering Canada', 'Deliver mail across the country', 'Build roads and highways', 'Run public libraries'], 0),
    ('Where might border services officers work?', ['Airports, land crossings, and ports', 'Only inside schools', 'Only inside grocery stores', 'Only inside hospitals'], 0),
    ('Why might officers check goods entering the country?', ['To make sure items are allowed and safe', 'To remove all goods from the country', 'To avoid ever checking anything', 'To slow down every traveller with no reason'], 0),
    ('What might a traveller be asked to show when entering Canada?', ['Identification, such as a passport', 'A grocery list', 'A library card only', 'Nothing at all is ever required'], 0),
    ('Why is border security important to a country?', ['It helps protect the safety and rules of the country', 'It has no importance at all', 'It only matters for one city', 'It prevents any travel from happening'], 0)]),
]),
day(162, [
L('Vocabulary: Jargon — Special Words Used in a Job or Hobby',
  'Grade 3 Language strand: jargon is special vocabulary used by people in a particular job or hobby, such as words doctors, athletes, or musicians use that may be unfamiliar to others.',
  [('What is jargon?', ['Special vocabulary used by people in a particular job or hobby', 'A word with no meaning at all', 'A type of punctuation mark', 'A word used only in poetry'], 0),
   ('Which is an example of jargon a doctor might use?', ['A specific medical term unfamiliar to most people', 'A common greeting like hello', 'A simple colour word', 'A basic counting word'], 0),
   ('Why might jargon be confusing to someone outside a particular job or hobby?', ['The words are specific to that group and not commonly used elsewhere', 'The words are used by everyone every day', 'Jargon words never have any meaning', 'Jargon is always the same as slang'], 0),
   ('Why might people in the same job use jargon with each other?', ['It allows them to communicate quickly and precisely about their work', 'It prevents them from ever communicating', 'It is required by law in every job', 'It has no purpose in the workplace'], 0),
   ('Learning about jargon helps readers understand ___.', ['That different groups have their own specialized vocabulary', 'That every word means the same thing to everyone', 'That vocabulary never changes between groups', 'That only writers use special words'], 0)]),
M('Geometry: Parallel and Perpendicular Lines',
  'Grade 3 Math strand: parallel lines never meet and stay the same distance apart, while perpendicular lines cross each other at a right angle.',
  [('What is true about parallel lines?', ['They never meet and stay the same distance apart', 'They always cross at a right angle', 'They always meet at one point', 'They are always curved'], 0),
   ('What is true about perpendicular lines?', ['They cross each other at a right angle', 'They never meet at all', 'They are always the same length', 'They only exist in circles'], 0),
   ('Which pair of lines would form the letter T?', ['Perpendicular lines', 'Parallel lines', 'Curved lines', 'Diagonal lines that never touch'], 0),
   ('Do parallel lines ever cross?', ['No, they never cross', 'Yes, they always cross', 'They cross only at right angles', 'They cross only in 3D shapes'], 0),
   ('What angle is formed where two perpendicular lines meet?', ['A right angle', 'A curved angle', 'No angle at all', 'An angle that changes size'], 0)]),
Sc('Science: Kangaroos and Marsupial Adaptations',
   'Grade 3 Science strand: kangaroos are marsupials, meaning their young are born tiny and undeveloped and continue growing inside a pouch on their mothers body.',
   [('What type of animal is a kangaroo?', ['A marsupial', 'A reptile', 'A fish', 'An insect'], 0),
    ('Where do baby kangaroos continue growing after birth?', ['Inside a pouch on their mothers body', 'Inside an egg buried in sand', 'Underwater in a nest', 'Inside a burrow with no parent nearby'], 0),
    ('What is a baby kangaroo called?', ['A joey', 'A cub', 'A calf', 'A kit'], 0),
    ('How do kangaroos usually move around?', ['By hopping on their strong back legs', 'By slithering on the ground', 'By flying short distances', 'By swimming through rivers'], 0),
    ('Why might a pouch be an important adaptation for a marsupial?', ['It protects and nourishes the underdeveloped young as they grow', 'It has no real purpose for the animal', 'It only helps the animal find food', 'It is used only for storing water'], 0)]),
SS('Social Studies: Indigenous Languages of Canada',
   'Grade 3 Social Studies strand: Canada is home to many Indigenous languages, and communities and schools work to preserve and revitalize these languages for future generations.',
   [('What does it mean to revitalize a language?', ['To help bring it back into more common use and keep it alive', 'To remove it from use completely', 'To translate it into a foreign language only', 'To replace it with a different language entirely'], 0),
    ('Why might communities want to preserve Indigenous languages?', ['To protect an important part of their culture and identity', 'Because languages have no connection to culture', 'To avoid teaching anything about history', 'Because preserving languages is not valuable'], 0),
    ('How many Indigenous languages are spoken across Canada?', ['Many different Indigenous languages', 'Only one single language', 'None are spoken today', 'Exactly two languages only'], 0),
    ('Which groups might help teach and preserve Indigenous languages?', ['Communities, elders, and schools', 'Only foreign governments', 'Only large corporations', 'No one works to preserve languages'], 0),
    ('Why is language considered an important part of culture?', ['It carries traditions, stories, and ways of understanding the world', 'It has no connection to traditions or stories', 'Language and culture are always unrelated', 'Only written language matters to culture'], 0)]),
]),
day(163, [
L('Reading: Following Multi-Step Instructions',
  'Grade 3 Language strand: multi-step instructions must be read carefully and followed in order, since skipping or reordering a step can lead to a mistake.',
  [('Why should multi-step instructions be followed in order?', ['Skipping or reordering a step can lead to a mistake', 'The order never matters at all', 'Steps are always identical to each other', 'Instructions have no particular order'], 0),
   ('What should a reader do before starting to follow instructions?', ['Read all the steps carefully first', 'Skip straight to the last step', 'Ignore the instructions completely', 'Guess what to do with no reading'], 0),
   ('If a recipe says to mix ingredients before baking, what happens if you bake first?', ['The steps would be out of order and the result may not work', 'Nothing would change at all', 'The recipe would always turn out perfectly', 'Baking first is always the correct order'], 0),
   ('Why might numbered steps be helpful in instructions?', ['They show the exact order the steps should be completed', 'They make the instructions impossible to follow', 'They remove the need to read carefully', 'They are only used in fiction stories'], 0),
   ('What is a good strategy if you are unsure about a step in the instructions?', ['Reread the step carefully before continuing', 'Skip the step entirely and move on', 'Guess randomly what the step means', 'Stop reading instructions altogether'], 0)]),
M('Data: Reading a Bar Graph with a Scale of More Than One',
  'Grade 3 Math strand: some bar graphs use a scale where each line represents more than one unit, such as 2 or 5, so students must multiply to find the value a bar represents.',
  [('If each line on a bar graph represents 2 units and a bar reaches 6 lines, what value does the bar show?', ['12', '6', '8', '10'], 0),
   ('Why might a bar graph use a scale of more than one?', ['To represent larger amounts of data in a smaller space', 'To make the graph impossible to read', 'To remove the need for a scale entirely', 'Because every bar graph must use a scale of one'], 0),
   ('If the scale is 5 and a bar reaches 4 lines, what value does the bar show?', ['20', '9', '15', '25'], 0),
   ('What should you check first before reading the value of a bar on a graph?', ['The scale being used', 'The colour of the bar', 'The title of the graph only', 'The shape of the bar only'], 0),
   ('Why is it important to read the scale carefully on a bar graph?', ['Misreading the scale can lead to the wrong value being reported', 'The scale never affects the value of a bar', 'Bar graphs never include a scale', 'The scale only matters for line graphs'], 0)]),
Sc('Science: The Aurora Borealis — Northern Lights',
   'Grade 3 Science strand: the aurora borealis, or northern lights, is a colourful display in the night sky caused by particles from the Sun interacting with Earths atmosphere near the poles.',
   [('What is another name for the aurora borealis?', ['The northern lights', 'The morning star', 'The evening tide', 'The falling stars'], 0),
    ('What causes the aurora borealis?', ['Particles from the Sun interacting with Earths atmosphere', 'Reflections from the Moon only', 'Lightning during a storm', 'Sunlight passing through raindrops'], 0),
    ('Where is the aurora borealis most often seen?', ['Near the North Pole, in places with northern latitudes', 'Near the equator', 'Only in deserts', 'Only over the ocean at noon'], 0),
    ('What does the aurora borealis look like in the sky?', ['Colourful, moving lights', 'A single still white dot', 'A dark empty patch of sky', 'A solid grey cloud'], 0),
    ('Why might scientists study the aurora borealis?', ['To better understand how the Sun affects Earths atmosphere', 'Because it has no scientific value', 'Because it only appears in stories', 'Because it never actually happens'], 0)]),
SS('Social Studies: The Role of Ontarios Lieutenant Governor',
   'Grade 3 Social Studies strand: the Lieutenant Governor represents the Crown in Ontario, performing ceremonial duties such as opening the legislature and giving royal assent to new provincial laws.',
   [('Who does the Lieutenant Governor represent in Ontario?', ['The Crown', 'A foreign country', 'A single city only', 'A private business'], 0),
    ('Which is a duty of the Lieutenant Governor?', ['Giving royal assent to new provincial laws', 'Running a local grocery store', 'Coaching a sports team', 'Driving a school bus'], 0),
    ('What kind of role is the Lieutenant Governor mainly considered?', ['A ceremonial role', 'A role with no responsibilities at all', 'A role only in the military', 'A role limited to one school'], 0),
    ('Which event might the Lieutenant Governor take part in?', ['Opening a new session of the provincial legislature', 'Coaching a hockey game', 'Running a bakery', 'Repairing a highway'], 0),
    ('Why does Ontario have a Lieutenant Governor?', ['To represent the Crown at the provincial level', 'To replace the need for any government', 'Because every store needs one', 'To manage a single school board'], 0)]),
]),
day(164, [
L('Writing: Writing a Limerick',
  'Grade 3 Language strand: a limerick is a five-line humorous poem with a bouncy rhythm and an AABBA rhyme pattern, often ending with a funny or surprising line.',
  [('How many lines does a limerick have?', ['Five', 'Three', 'Seven', 'Ten'], 0),
   ('What is the rhyme pattern of a limerick?', ['AABBA', 'ABAB', 'AAAA', 'ABCD'], 0),
   ('What tone do limericks often have?', ['Humorous', 'Extremely serious', 'Silent, with no words', 'Always sad'], 0),
   ('Which lines in a limerick usually rhyme with each other?', ['Lines 1, 2, and 5', 'Lines 1 and 4 only', 'Every line rhymes with no pattern', 'No lines rhyme at all'], 0),
   ('Why might a writer choose to write a limerick?', ['To create a short, funny poem with a bouncy rhythm', 'To write a long, serious essay', 'To remove all rhythm from a poem', 'To avoid using any rhyme'], 0)]),
M('Multiplication: Finding Missing Factors',
  'Grade 3 Math strand: to find a missing factor in a multiplication sentence, such as 6 x ___ = 42, students can use known multiplication facts or division to solve for the unknown number.',
  [('What is the missing factor in 6 x ___ = 42?', ['7', '6', '8', '9'], 0),
   ('What operation can help find a missing factor?', ['Division', 'Subtraction only', 'Rounding', 'Estimating only'], 0),
   ('What is the missing factor in ___ x 4 = 28?', ['7', '6', '8', '9'], 0),
   ('In the sentence 5 x ___ = 45, what is the missing number?', ['9', '8', '7', '10'], 0),
   ('Why might finding a missing factor be useful?', ['It helps solve problems where only the product and one factor are known', 'It removes the need for multiplication entirely', 'It only works with even numbers', 'It has no real use in math'], 0)]),
Sc('Science: Spiders and How They Spin Their Webs',
   'Grade 3 Science strand: spiders produce silk from special glands and use it to spin webs that trap insects for food, with different spiders building different web shapes.',
   [('What do spiders use to spin their webs?', ['Silk produced from special glands', 'Leaves glued together', 'Mud and small stones', 'Feathers from birds'], 0),
    ('Why do many spiders build webs?', ['To trap insects for food', 'To block sunlight completely', 'To store water for drinking', 'To build a home for fish'], 0),
    ('Do all spiders build the same shaped web?', ['No, different spiders build different web shapes', 'Yes, every spider builds an identical web', 'Spiders never build webs at all', 'Only baby spiders build webs'], 0),
    ('Where does a spiders silk come from?', ['Special glands in its body', 'The leaves of a tree', 'Its stomach after eating', 'Another animals fur'], 0),
    ('Why might a web help a spider catch food without chasing it?', ['The web traps insects that fly or crawl into it', 'The web scares insects away from the area', 'The web has no connection to catching food', 'Spiders never eat insects caught in webs'], 0)]),
SS('Social Studies: The Canadian Armed Forces and National Defence',
   'Grade 3 Social Studies strand: the Canadian Armed Forces work to defend Canada and support Canadians during emergencies, both within the country and alongside allies abroad.',
   [('What is a main role of the Canadian Armed Forces?', ['To defend Canada', 'To deliver mail across the country', 'To run public libraries', 'To manage grocery stores'], 0),
    ('Besides defence, what else might the Canadian Armed Forces help with?', ['Supporting Canadians during emergencies', 'Selling groceries to families', 'Building shopping malls', 'Running television stations'], 0),
    ('Might the Canadian Armed Forces work with other countries?', ['Yes, alongside allies abroad', 'No, they never leave Canada for any reason', 'Only during sporting events', 'Only to sell products overseas'], 0),
    ('Why is national defence important to a country?', ['It helps keep the country and its people safe', 'It has no importance to a country', 'It only matters during a holiday', 'It replaces the need for any government'], 0),
    ('Which is an example of a branch within a countrys armed forces?', ['An army, navy, or air force', 'A school board', 'A public library system', 'A postal service'], 0)]),
]),
day(165, [
L('Oral Communication: Using Visual Aids During a Presentation',
  'Grade 3 Language strand: visual aids, such as posters, pictures, or slides, can help a speaker explain ideas more clearly and keep an audience engaged during a presentation.',
  [('What is a visual aid?', ['Something like a poster, picture, or slide used to support a presentation', 'A type of punctuation mark', 'A silent letter in a word', 'A rule for capitalization'], 0),
   ('Why might a speaker use a visual aid?', ['To help explain ideas more clearly and keep the audience engaged', 'To confuse the audience on purpose', 'To avoid speaking at all during a presentation', 'To make a presentation longer with no purpose'], 0),
   ('Which is an example of a visual aid?', ['A poster with pictures and labels', 'A blank sheet of paper', 'Complete silence', 'A closed book with no pictures'], 0),
   ('When should a visual aid be shown during a presentation?', ['At the point in the talk where it supports what is being said', 'Only after the presentation has completely ended', 'Before the presentation begins and never again', 'Visual aids should never be shown at all'], 0),
   ('Why might a visual aid help an audience understand a topic?', ['It gives the audience something to see alongside what they hear', 'It removes all information from the presentation', 'It replaces the need for the speaker entirely', 'It has no effect on audience understanding'], 0)]),
M('Division: Dividing Using Repeated Subtraction',
  'Grade 3 Math strand: repeated subtraction is a division strategy where the divisor is subtracted from the dividend again and again until reaching zero, and the number of subtractions equals the quotient.',
  [('In repeated subtraction, what number equals the quotient?', ['The number of times the divisor was subtracted', 'The first number in the problem', 'The remainder left at the end', 'The sum of all the numbers subtracted'], 0),
   ('To divide 20 by 5 using repeated subtraction, how many times would you subtract 5?', ['4 times', '3 times', '5 times', '20 times'], 0),
   ('What should the result be after subtracting the divisor the correct number of times?', ['Zero', 'The original dividend', 'A negative number always', 'The divisor itself'], 0),
   ('Why might repeated subtraction help someone understand division?', ['It shows division as splitting a total into equal groups one at a time', 'It removes the need to ever understand division', 'It only works with fractions', 'It replaces multiplication entirely'], 0),
   ('To divide 15 by 3 using repeated subtraction, how many times would you subtract 3?', ['5 times', '3 times', '4 times', '15 times'], 0)]),
Sc('Science: Sonar — How Sound Helps Animals and Submarines See Underwater',
   'Grade 3 Science strand: sonar uses sound waves that bounce off objects and return as echoes, helping animals such as dolphins and vehicles such as submarines detect objects underwater.',
   [('What does sonar use to detect objects underwater?', ['Sound waves that bounce off objects and return as echoes', 'Light beams that shine through water', 'Magnets that attract metal objects', 'Radio signals sent to outer space'], 0),
    ('Which animal is known for using a form of sonar called echolocation?', ['A dolphin', 'A cow', 'A chicken', 'A rabbit'], 0),
    ('Which underwater vehicle might use sonar?', ['A submarine', 'A bicycle', 'A school bus', 'A hot air balloon'], 0),
    ('Why might sonar be useful underwater where it is hard to see?', ['It allows objects to be detected using sound instead of sight', 'It removes the need to detect any objects', 'It works only in complete darkness on land', 'It replaces the need for water entirely'], 0),
    ('What happens to a sound wave when it hits an object underwater?', ['It bounces back as an echo', 'It disappears completely with no trace', 'It turns into a beam of light', 'It stops moving forever'], 0)]),
SS('Social Studies: The Canada-US Border — The Longest Undefended Border in the World',
   'Grade 3 Social Studies strand: the border between Canada and the United States is known as the longest undefended border in the world, and it supports close trade and travel between the two countries.',
   [('What is the border between Canada and the United States often called?', ['The longest undefended border in the world', 'The shortest border in the world', 'A border that does not actually exist', 'A border found only on old maps'], 0),
    ('What does undefended mean in this context?', ['The border has no military forces stationed to guard it', 'The border is guarded by soldiers at every metre', 'No one is allowed to cross the border ever', 'The border changes location every year'], 0),
    ('Why might close trade happen between Canada and the United States?', ['They share a long border and strong economic ties', 'They have no connection to each other at all', 'Trade between the two countries is against the law', 'They are located on different continents'], 0),
    ('What might a traveller need to cross the Canada-US border?', ['Identification, such as a passport', 'A library card only', 'Nothing at all is ever required', 'A grocery receipt'], 0),
    ('Why is the Canada-US border considered unique among world borders?', ['It is long and peaceful, without military defence along it', 'It is the only border that has ever existed', 'It is completely closed at all times', 'It only allows animals to cross'], 0)]),
]),
day(166, [
L('Grammar: Correlative Conjunctions (Either/Or, Neither/Nor)',
  'Grade 3 Language strand: correlative conjunctions such as either/or and neither/nor are pairs of words that work together to connect related ideas in a sentence.',
  [('What are correlative conjunctions?', ['Pairs of words that work together to connect related ideas', 'A single silent letter in a word', 'A type of punctuation mark used only in titles', 'A word that has no meaning at all'], 0),
   ('Which is an example of a correlative conjunction pair?', ['Either/or', 'Run/jump', 'Happy/sad', 'Quick/slow'], 0),
   ('Which sentence correctly uses a correlative conjunction pair?', ['Either you clean your room, or you cannot go outside.', 'Either you clean your room, but you cannot go outside.', 'Neither you clean your room, or you cannot go outside.', 'You clean your room, either or not go outside.'], 0),
   ('What is another correlative conjunction pair besides either/or?', ['Neither/nor', 'Fast/slow', 'Big/small', 'Loud/quiet'], 0),
   ('Why might a writer use correlative conjunctions?', ['To clearly connect two related choices or ideas in one sentence', 'To remove all connections between ideas', 'To make a sentence impossible to understand', 'To avoid ever using conjunctions'], 0)]),
M('Measurement: Choosing the Right Unit to Measure Everyday Objects',
  'Grade 3 Math strand: choosing an appropriate unit of measurement, such as centimetres for a pencil or metres for a hallway, depends on the size of the object being measured.',
  [('Which unit would be best to measure the length of a pencil?', ['Centimetres', 'Kilometres', 'Metres', 'Litres'], 0),
   ('Which unit would be best to measure the length of a hallway?', ['Metres', 'Millimetres', 'Grams', 'Litres'], 0),
   ('Why is it important to choose an appropriate unit for measuring an object?', ['It makes the measurement accurate and easy to understand', 'It has no effect on the measurement at all', 'It always makes the number larger', 'It removes the need for measuring altogether'], 0),
   ('Which unit would be best to measure the mass of an apple?', ['Grams', 'Kilometres', 'Litres', 'Metres'], 0),
   ('Which unit would be best to measure the capacity of a bathtub?', ['Litres', 'Centimetres', 'Grams', 'Kilometres'], 0)]),
Sc('Science: The Forest Canopy — Layers of a Forest Ecosystem',
   'Grade 3 Science strand: a forest ecosystem has distinct layers, including the forest floor, understory, canopy, and emergent layer, each providing a different habitat for plants and animals.',
   [('What is the canopy of a forest?', ['The layer formed by the leafy tops of tall trees', 'The layer of soil deep underground', 'A single flower found only in spring', 'A layer made entirely of rocks'], 0),
    ('Which layer of a forest is closest to the ground?', ['The forest floor', 'The canopy', 'The emergent layer', 'The upper atmosphere'], 0),
    ('Why might different animals live in different layers of a forest?', ['Each layer offers different food, light, and shelter', 'Every layer of a forest is exactly the same', 'Animals never choose where they live', 'Forests only have a single layer'], 0),
    ('Which forest layer receives the most sunlight?', ['The canopy or emergent layer', 'The forest floor', 'The layer of soil underground', 'A layer found only at night'], 0),
    ('Why do scientists study the layers of a forest ecosystem?', ['To understand how plants and animals use different parts of the habitat', 'Because forest layers have no scientific value', 'Because forests never have more than one layer', 'Because layers only exist in oceans'], 0)]),
SS('Social Studies: Ferries and Water Transportation Across Canada',
   'Grade 3 Social Studies strand: ferries carry passengers, vehicles, and goods across lakes, rivers, and coastal waters, connecting communities that are separated by water.',
   [('What do ferries carry across bodies of water?', ['Passengers, vehicles, and goods', 'Only letters and postcards', 'Only farm animals', 'Nothing at all'], 0),
    ('Why might a community rely on a ferry?', ['The community is separated from other areas by water', 'The community has no roads anywhere nearby', 'Ferries are required by every community', 'The community is located on a mountain'], 0),
    ('Which type of body of water might a ferry cross?', ['A lake, river, or coastal water', 'A dry desert', 'A forest with no water', 'A city sidewalk'], 0),
    ('Why is water transportation important in some parts of Canada?', ['It connects communities that would otherwise be hard to reach by road', 'It has no importance to any community', 'It replaces the need for all other transportation everywhere', 'It only matters in one province'], 0),
    ('What is one benefit of a ferry service for a coastal community?', ['It provides a reliable way to travel and transport goods across the water', 'It prevents any travel between communities', 'It only operates once every ten years', 'It has no connection to the local economy'], 0)]),
]),
day(167, [
L('Reading: Identifying an Authors Intended Audience',
  'Grade 3 Language strand: an authors intended audience is the group of readers a text is written for, and recognizing the audience helps readers understand the authors word choice and tone.',
  [('What is an authors intended audience?', ['The group of readers a text is written for', 'The title of the text', 'The setting of the story', 'A single word in the text'], 0),
   ('Why might recognizing the audience help a reader understand a text?', ['It explains the authors word choice and tone', 'It removes all meaning from the text', 'It has no connection to how a text is written', 'It only matters for poetry'], 0),
   ('Which audience might a picture book with simple words be written for?', ['Young children', 'Only university professors', 'Only scientists', 'Only engineers'], 0),
   ('Which audience might a technical manual with complex vocabulary be written for?', ['Adults with specialized knowledge', 'Toddlers learning to talk', 'Babies who cannot yet read', 'Animals'], 0),
   ('Why might an author change their writing style depending on the audience?', ['To make sure the text is clear and appropriate for those readers', 'Authors never consider who will read their writing', 'To make every text confusing on purpose', 'Because writing style never needs to change'], 0)]),
M('Fractions: Ordering Three or More Fractions with the Same Denominator',
  'Grade 3 Math strand: when fractions share the same denominator, they can be ordered from least to greatest by comparing their numerators.',
  [('To order fractions with the same denominator, what should you compare?', ['The numerators', 'The denominators only', 'The colours of the fractions', 'The number of fractions given'], 0),
   ('Which list correctly orders 2/8, 5/8, and 1/8 from least to greatest?', ['1/8, 2/8, 5/8', '5/8, 2/8, 1/8', '2/8, 1/8, 5/8', '8/8, 2/8, 1/8'], 0),
   ('Which fraction is the greatest: 3/6, 5/6, or 1/6?', ['5/6', '3/6', '1/6', '6/6'], 0),
   ('Why can you order fractions with the same denominator just by looking at the numerators?', ['The parts are the same size, so a larger numerator means a larger fraction', 'The denominators always change between fractions', 'Numerators never affect the size of a fraction', 'Fractions with the same denominator cannot be compared'], 0),
   ('Which list correctly orders 4/10, 7/10, and 2/10 from greatest to least?', ['7/10, 4/10, 2/10', '2/10, 4/10, 7/10', '4/10, 7/10, 2/10', '2/10, 7/10, 4/10'], 0)]),
Sc('Science: How Igloos and Snow Insulate Against Cold',
   'Grade 3 Science strand: snow contains trapped air that acts as insulation, and an igloo is built from packed snow blocks that use this trapped air to keep the inside warmer than the freezing air outside.',
   [('What does snow contain that helps it act as insulation?', ['Trapped air', 'Melted ice only', 'Solid rock', 'Liquid water only'], 0),
    ('What is an igloo built from?', ['Packed snow blocks', 'Wooden logs', 'Bricks and cement', 'Sheets of glass'], 0),
    ('Why can the inside of an igloo be warmer than the freezing air outside?', ['The trapped air in the snow blocks helps insulate the inside', 'Igloos are always heated by fire inside', 'Snow blocks remove all warmth completely', 'Igloos are built only in warm climates'], 0),
    ('What does insulation help do?', ['Slow down the movement of heat, keeping warmth in or cold out', 'Speed up the loss of heat completely', 'Turn cold air into warm air instantly', 'Remove the need for any shelter'], 0),
    ('Why might Arctic peoples have used igloos for shelter?', ['They provided warmth using materials available in a cold environment', 'Igloos have no connection to survival in the cold', 'Igloos were only ever used for storage', 'Igloos require materials found only in deserts'], 0)]),
SS('Social Studies: The Ontario Legislature at Queens Park',
   'Grade 3 Social Studies strand: the Ontario Legislature, located at Queens Park in Toronto, is where elected members debate and pass provincial laws for Ontario.',
   [('Where is the Ontario Legislature located?', ['Queens Park in Toronto', 'A small town in northern Ontario', 'A building in another province', 'A building outside of Canada'], 0),
    ('What happens at the Ontario Legislature?', ['Elected members debate and pass provincial laws', 'Local sports games are played', 'Groceries are bought and sold', 'Mail is sorted and delivered'], 0),
    ('Who works at the Ontario Legislature to represent their communities?', ['Elected members of provincial parliament', 'Only unelected volunteers', 'Only foreign diplomats', 'Only school principals'], 0),
    ('Why is the Ontario Legislature an important building?', ['It is where decisions about provincial laws are made', 'It has no real purpose in Ontario', 'It is only used for storing furniture', 'It is closed to all government activity'], 0),
    ('What kind of laws are passed at the Ontario Legislature?', ['Provincial laws for Ontario', 'Laws for every country in the world', 'Laws for a single street only', 'No laws are ever passed there'], 0)]),
]),
day(168, [
L('Writing: Writing a Weather Report',
  'Grade 3 Language strand: a weather report shares current or upcoming weather conditions using clear, factual language, often including details such as temperature, precipitation, and wind.',
  [('What does a weather report share?', ['Current or upcoming weather conditions', 'A list of favourite foods', 'A summary of a sports game', 'A description of a math problem'], 0),
   ('Which detail might a weather report include?', ['Temperature, precipitation, or wind', 'A characters name in a story', 'The title of a song', 'A list of math facts'], 0),
   ('What kind of language does a weather report usually use?', ['Clear, factual language', 'Confusing, made-up language', 'Language with no real information', 'Language written only in rhyme'], 0),
   ('Why is it useful for a weather report to be factual and clear?', ['So readers or listeners can plan their day based on accurate information', 'So no one can understand the report at all', 'Because facts are never useful in a report', 'So the weather can be kept a secret'], 0),
   ('Which is an example of information found in a weather report?', ['A forecast of rain expected in the afternoon', 'A list of homework assignments', 'The rules of a board game', 'A recipe for dinner'], 0)]),
M('Patterning: Creating Your Own Number Pattern Using a Rule',
  'Grade 3 Math strand: students can create their own number pattern by choosing a starting number and a rule, such as adding 4 each time, then applying the rule repeatedly to generate the pattern.',
  [('What two things do you need to create a number pattern?', ['A starting number and a rule', 'Only a calculator', 'Only a ruler', 'A list of random letters'], 0),
   ('If the starting number is 3 and the rule is add 4, what are the first four terms?', ['3, 7, 11, 15', '3, 4, 5, 6', '3, 6, 9, 12', '4, 8, 12, 16'], 0),
   ('If the starting number is 20 and the rule is subtract 5, what is the third term?', ['10', '15', '5', '20'], 0),
   ('Why is it important to apply the same rule every time when creating a pattern?', ['It keeps the pattern consistent and predictable', 'It makes the pattern impossible to predict', 'Rules should change with every term', 'Patterns never need a consistent rule'], 0),
   ('If the rule is multiply by 2 starting at 1, what are the first four terms?', ['1, 2, 4, 8', '1, 3, 5, 7', '2, 4, 6, 8', '1, 2, 3, 4'], 0)]),
Sc('Science: Chameleons and How They Change Colour',
   'Grade 3 Science strand: chameleons can change the colour of their skin using special cells, which helps them communicate, regulate temperature, and sometimes blend into their surroundings.',
   [('What helps a chameleon change the colour of its skin?', ['Special cells in its skin', 'A layer of fur', 'Feathers on its back', 'A shell around its body'], 0),
    ('Which is one reason a chameleon might change colour?', ['To help regulate its body temperature', 'To grow additional legs', 'To stop breathing completely', 'To become a different animal entirely'], 0),
    ('Can changing colour help a chameleon communicate?', ['Yes, colour changes can send signals to other chameleons', 'No, colour has no connection to communication', 'Only humans can understand colour changes', 'Chameleons never interact with each other'], 0),
    ('Does a chameleon only change colour to hide from predators?', ['No, it changes colour for several reasons, not only hiding', 'Yes, hiding is the only reason', 'Chameleons never change colour at all', 'Colour change only happens once in a lifetime'], 0),
    ('What body part do many chameleons have that helps them see in different directions at once?', ['Their eyes, which can move independently', 'Their tail, which can see in the dark', 'Their skin, which replaces their eyes', 'Their feet, which sense colour'], 0)]),
SS('Social Studies: Canadas National Wildlife Areas and Migratory Bird Sanctuaries',
   'Grade 3 Social Studies strand: Canada protects important habitats through national wildlife areas and migratory bird sanctuaries, helping conserve species and the places they depend on.',
   [('What do national wildlife areas and bird sanctuaries help protect?', ['Important habitats for wildlife', 'Shopping malls and parking lots', 'City streets and sidewalks', 'Factories and warehouses'], 0),
    ('Why might a migratory bird sanctuary be created?', ['To protect birds that travel long distances between habitats', 'To prevent birds from ever migrating', 'To remove birds from the environment completely', 'Because birds never need protected habitats'], 0),
    ('What is one benefit of protecting these areas?', ['It helps conserve species and the places they depend on', 'It has no benefit to wildlife at all', 'It only benefits a single business', 'It removes the need for any habitat'], 0),
    ('Who might help manage a national wildlife area?', ['Government agencies and conservation organizations', 'No one manages these areas at all', 'Only private shopping companies', 'Only foreign militaries'], 0),
    ('Why is habitat protection important for migrating animals?', ['They need safe places to rest and feed along their journey', 'Migrating animals never need to rest', 'Habitat protection has no effect on migration', 'Animals that migrate do not need any habitat'], 0)]),
]),
day(169, [
L('Vocabulary: Clipped Words — Shortened Forms of Longer Words',
  'Grade 3 Language strand: a clipped word is a shortened form of a longer word, such as phone from telephone, gym from gymnasium, and photo from photograph.',
  [('What is a clipped word?', ['A shortened form of a longer word', 'A word with no meaning at all', 'A type of punctuation mark', 'A word borrowed from another language'], 0),
   ('The word phone is a clipped form of which longer word?', ['Telephone', 'Photograph', 'Gymnasium', 'Advertisement'], 0),
   ('The word gym is a clipped form of which longer word?', ['Gymnasium', 'Telephone', 'Photograph', 'Automobile'], 0),
   ('Why might people use clipped words in everyday speech?', ['They are quicker and easier to say than the full word', 'They are always longer than the original word', 'They have no connection to the original word', 'They are only used in formal writing'], 0),
   ('Which is an example of a clipped word?', ['Photo, from photograph', 'Balcony, from Italian', 'Canoe, from an Indigenous language', 'Kindergarten, from German'], 0)]),
M('Financial Literacy: Making a Simple Budget for a Class Event',
  'Grade 3 Math strand: a budget lists expected costs for an event and compares them to the money available, helping planners decide what they can afford and where to adjust spending.',
  [('What does a budget list?', ['Expected costs and the money available', 'Only the date of an event', 'Only the guest list for an event', 'Only the weather forecast'], 0),
   ('Why might a class create a budget before planning an event?', ['To make sure they do not spend more money than they have', 'To avoid ever planning any event', 'Because budgets have no real purpose', 'To remove the need for any money at all'], 0),
   ('If a class has 50 dollars and plans to spend 20 dollars on decorations and 15 dollars on snacks, how much money remains?', ['15 dollars', '20 dollars', '35 dollars', '5 dollars'], 0),
   ('What might a class do if their planned costs are more than their budget allows?', ['Adjust spending or find ways to reduce costs', 'Ignore the budget completely', 'Spend money they do not have', 'Cancel all future events permanently'], 0),
   ('Why is budgeting a useful skill for planning any event?', ['It helps ensure spending stays within the money that is available', 'It has no connection to planning an event', 'It only applies to large businesses', 'It removes the need to plan at all'], 0)]),
Sc('Science: Woodpeckers and Their Special Adaptations',
   'Grade 3 Science strand: woodpeckers have strong beaks, shock-absorbing skulls, and gripping feet that allow them to peck into tree trunks to find insects and create nesting holes.',
   [('What do woodpeckers use their strong beaks for?', ['Pecking into tree trunks', 'Swimming through rivers', 'Digging burrows underground', 'Catching fish in the ocean'], 0),
    ('Why might a woodpecker peck into a tree trunk?', ['To find insects or create a nesting hole', 'To make the tree grow faster', 'To remove all the leaves from a tree', 'To build a home underwater'], 0),
    ('What adaptation helps protect a woodpeckers brain while pecking?', ['A shock-absorbing skull', 'A layer of thick fur', 'A hard outer shell', 'Extra feathers on its wings'], 0),
    ('What helps a woodpecker grip onto a tree trunk?', ['Its strong, gripping feet', 'A sticky substance on its beak', 'Wheels on its feet', 'A long tail that anchors into soil'], 0),
    ('Why are woodpeckers considered well adapted to life in trees?', ['Their bodies have special features suited to pecking and climbing trees', 'They have no special features at all', 'They never interact with trees', 'They live only underground'], 0)]),
SS('Social Studies: The Trans-Canada Trail — Canadas Cross-Country Recreational Trail',
   'Grade 3 Social Studies strand: the Trans-Canada Trail is a network of recreational trails stretching across the country, connecting communities and offering space for walking, cycling, and other outdoor activities.',
   [('What is the Trans-Canada Trail?', ['A network of recreational trails stretching across the country', 'A single highway for cars only', 'A railway used only for cargo', 'A canal used only for shipping'], 0),
    ('Which activities might people do on the Trans-Canada Trail?', ['Walking, cycling, and other outdoor activities', 'Only driving large trucks', 'Only flying airplanes', 'Only sailing large ships'], 0),
    ('How does the Trans-Canada Trail connect Canada?', ['It links communities across the country with connected trails', 'It separates communities from each other completely', 'It only exists within a single city', 'It has no connection between any communities'], 0),
    ('Why might communities value having a section of the Trans-Canada Trail nearby?', ['It offers recreational space and connects them to other communities', 'It removes all outdoor space from the community', 'It has no benefit to nearby communities', 'It is closed to the public at all times'], 0),
    ('What kind of trail is the Trans-Canada Trail, compared to a highway?', ['A recreational trail meant for walking, cycling, and similar activities', 'A trail meant only for large trucks', 'A trail meant only for airplanes', 'A trail meant only for trains'], 0)]),
]),
day(170, [
L('Language Review: Parentheses, Jargon, and Presentation Skills',
  'Grade 3 Language strand review: students revisit using parentheses for extra information, jargon, following multi-step instructions, writing a limerick, using visual aids during a presentation, correlative conjunctions, identifying an authors intended audience, writing a weather report, and clipped words.',
  [('What do parentheses add to a sentence?', ['Extra information or a side comment', 'A brand new subject', 'A completely different sentence', 'A silent letter'], 0),
   ('What is jargon?', ['Special vocabulary used by people in a particular job or hobby', 'A word with no meaning at all', 'A type of punctuation mark', 'A word used only in poetry'], 0),
   ('How many lines does a limerick have?', ['Five', 'Three', 'Seven', 'Ten'], 0),
   ('What are correlative conjunctions?', ['Pairs of words that work together to connect related ideas', 'A single silent letter in a word', 'A type of punctuation mark used only in titles', 'A word that has no meaning at all'], 0),
   ('What is a clipped word?', ['A shortened form of a longer word', 'A word with no meaning at all', 'A type of punctuation mark', 'A word borrowed from another language'], 0)]),
M('Math Review: Rounding, Parallel Lines, and Budgeting',
  'Grade 3 Math strand review: students revisit rounding to the nearest 10 000, parallel and perpendicular lines, reading a bar graph with a scale of more than one, finding missing factors, ordering fractions with the same denominator, dividing using repeated subtraction, choosing the right unit of measurement, creating a number pattern using a rule, and making a simple budget.',
  [('Which digit do you look at to round a number to the nearest 10 000?', ['The thousands digit', 'The ones digit', 'The tens digit', 'The hundreds digit'], 0),
   ('What is true about parallel lines?', ['They never meet and stay the same distance apart', 'They always cross at a right angle', 'They always meet at one point', 'They are always curved'], 0),
   ('What is the missing factor in 6 x ___ = 42?', ['7', '6', '8', '9'], 0),
   ('To order fractions with the same denominator, what should you compare?', ['The numerators', 'The denominators only', 'The colours of the fractions', 'The number of fractions given'], 0),
   ('What does a budget list?', ['Expected costs and the money available', 'Only the date of an event', 'Only the guest list for an event', 'Only the weather forecast'], 0)]),
Sc('Science Review: Animal Adaptations, Sound, and the Night Sky',
   'Grade 3 Science strand review: students revisit penguins, kangaroos, the aurora borealis, spiders, sonar, the forest canopy, igloos and insulation, chameleons, and woodpeckers.',
   [('What helps penguins stay warm in cold water?', ['A thick layer of fat and tightly packed feathers', 'A layer of fur like a bear', 'Hollow bones filled with air only', 'A shell covering their whole body'], 0),
    ('What type of animal is a kangaroo?', ['A marsupial', 'A reptile', 'A fish', 'An insect'], 0),
    ('What causes the aurora borealis?', ['Particles from the Sun interacting with Earths atmosphere', 'Reflections from the Moon only', 'Lightning during a storm', 'Sunlight passing through raindrops'], 0),
    ('What does sonar use to detect objects underwater?', ['Sound waves that bounce off objects and return as echoes', 'Light beams that shine through water', 'Magnets that attract metal objects', 'Radio signals sent to outer space'], 0),
    ('What helps a chameleon change the colour of its skin?', ['Special cells in its skin', 'A layer of fur', 'Feathers on its back', 'A shell around its body'], 0)]),
SS('Social Studies Review: Borders, Government, and Transportation',
   'Grade 3 Social Studies strand review: students revisit the Canadian Border Services Agency, Indigenous languages of Canada, the Lieutenant Governor, the Canadian Armed Forces, the Canada-US border, ferries, the Ontario Legislature, national wildlife areas, and the Trans-Canada Trail.',
   [('What does the Canadian Border Services Agency help do?', ['Keep the country safe by checking travellers and goods entering Canada', 'Deliver mail across the country', 'Build roads and highways', 'Run public libraries'], 0),
    ('Why might communities want to preserve Indigenous languages?', ['To protect an important part of their culture and identity', 'Because languages have no connection to culture', 'To avoid teaching anything about history', 'Because preserving languages is not valuable'], 0),
    ('Who does the Lieutenant Governor represent in Ontario?', ['The Crown', 'A foreign country', 'A single city only', 'A private business'], 0),
    ('What is a main role of the Canadian Armed Forces?', ['To defend Canada', 'To deliver mail across the country', 'To run public libraries', 'To manage grocery stores'], 0),
    ('What is the Trans-Canada Trail?', ['A network of recreational trails stretching across the country', 'A single highway for cars only', 'A railway used only for cargo', 'A canal used only for shipping'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_161_170, seed=20260813)
    append_to(3, g3_161_170)
