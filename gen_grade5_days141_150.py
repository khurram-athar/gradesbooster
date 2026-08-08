#!/usr/bin/env python3
"""Grade 5, Days 141-150 -- extends Grade 5 from 140 to 150 days. Modeled
exactly on gen_grade5_days131_140.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 5 Days 1-140
topics (see data/grade5.json), which already densely cover nearly the
entire grade 5 curriculum across all four subjects. New topics: oxymorons,
colloquialisms and slang, writing a choose-your-own-adventure story,
subject complements and predicate adjectives, understanding motif,
ellipses and em dashes, sponsored content and advertising disclosures,
writing a reflective journal entry, and giving and receiving constructive
feedback for Language; Venn diagrams, rotational symmetry, multiplying
three-digit by two-digit numbers, function machines and input-output
tables, same perimeter/different area, comparing interest rates, choosing
the most appropriate graph, sum of interior angles, and dividing decimals
by two-digit whole numbers for Math; mineral properties, ocean currents
and climate, how airplanes fly, tidal and wave power, rusting and
corrosion, adaptations for flight, earthquakes, distillation, and
herbivores/carnivores/omnivores for Science; and Canadas national parks
system, the role of political parties, Crown land, the Canadian Armed
Forces, how government budgets are planned, referendums, the Fathers of
Confederation, school boards and trustees, and interest groups and
lobbying for Social Studies -- none of those exact ideas appear in Days
1-140. Day 150 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch (drawing one
representative quiz question per subject from each of the first five days
of the batch, Days 141-145, exactly as Day 140 drew from Days 131-135).
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are dropped entirely, matching
the rest of Grade 5 Days 111-140 (e.g. "Canadas" not "Canada's",
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


def _rebalance_answer_positions(days, seed=20260807):
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


g5_141_150 = [
day(141, [
L('Figurative Language: Oxymorons',
  'Grade 5 Language strand: an oxymoron combines two contradictory or opposite words, such as jumbo shrimp or deafening silence, to create a striking or thought-provoking effect.',
  [('What is an oxymoron?', ['A figure of speech that combines two contradictory or opposite words', 'A word that rhymes with another word', 'A word borrowed from another language', 'A sentence with no verb'], 0),
   ('Which pair of words is an oxymoron?', ['Deafening silence', 'Bright sunshine', 'Tall building', 'Happy puppy'], 0),
   ('Which sentence contains an oxymoron?', ['The jumbo shrimp appetizer was delicious.', 'The bright sun was shining today.', 'The tall building was very old.', 'The small kitten was very cute.'], 0),
   ('Why might a writer use an oxymoron?', ['To create a striking contrast that draws attention to an idea', 'Oxymorons never add any meaning to writing', 'This concept has no connection to figurative language', 'An oxymoron always confuses the reader with no purpose'], 0),
   ('Which of these phrases is most likely an oxymoron?', ['Act naturally', 'Run quickly', 'Jump high', 'Read carefully'], 0)]),
M('Data Management: Venn Diagrams for Sorting and Comparing Data',
  'Grade 5 Math strand: a Venn diagram uses overlapping circles to sort and compare data, showing which items belong to one group, another group, or both groups at once.',
  [('What does a Venn diagram use to sort and compare data?', ['Overlapping circles', 'A single straight line', 'A pie-shaped wedge only', 'A list with no visual shapes'], 0),
   ('What does the overlapping section of two circles in a Venn diagram represent?', ['Items that belong to both groups', 'Items that belong to neither group', 'Items that belong to only the first group', 'Items that belong to only the second group'], 0),
   ('If a Venn diagram compares students who like soccer and students who like basketball, where would a student who likes both sports be placed?', ['In the overlapping section of both circles', 'Outside both circles entirely', 'Only in the soccer circle', 'Only in the basketball circle'], 0),
   ('Why might a Venn diagram be useful for organizing information?', ['It visually shows similarities and differences between two or more groups', 'It can only display a single group of data', 'This concept has no connection to data management', 'A Venn diagram never shows any overlap between groups'], 0),
   ('How many circles does a basic Venn diagram comparing two groups usually have?', ['Two', 'One', 'Four', 'Zero'], 0)]),
Sc('Minerals and Their Properties — Hardness, Streak, and Luster',
   'Grade 5 Science strand: minerals are identified using physical properties such as hardness, which measures resistance to scratching, streak, which is the colour of a minerals powder, and luster, which describes how a mineral reflects light.',
   [('What does the hardness of a mineral measure?', ['Its resistance to being scratched', 'Its exact weight in grams', 'Its temperature at all times', 'Its ability to conduct electricity only'], 0),
    ('What is streak in mineral identification?', ['The colour of a minerals powder', 'The shape of a mineral', 'The smell of a mineral', 'The exact age of a mineral'], 0),
    ('What does luster describe?', ['How a mineral reflects light', 'How heavy a mineral is', 'How a mineral tastes', 'How loud a mineral sounds when dropped'], 0),
    ('Why might scientists use several different properties to identify a mineral?', ['Comparing multiple properties gives a more reliable identification than using just one', 'A single property always identifies a mineral with complete certainty', 'Mineral properties are never useful for identification', 'This concept has no relevance to science'], 0),
    ('Which property would help you tell the difference between a shiny mineral and a dull one?', ['Luster', 'Streak', 'Hardness', 'Colour of the powder only'], 0)]),
SS('Canadas National Parks System — Protecting Natural Spaces',
   'Grade 5 Social Studies strand: Canadas national parks are protected natural areas managed by the federal government to conserve wildlife, ecosystems, and landscapes for future generations to enjoy.',
   [('What is the purpose of a national park?', ['To protect wildlife, ecosystems, and landscapes for future generations', 'To build as many new roads as possible', 'To sell natural resources as quickly as possible', 'To prevent anyone from ever visiting the area'], 0),
    ('Who generally manages Canadas national parks?', ['The federal government', 'A single private company', 'Individual students', 'Foreign governments'], 0),
    ('Why might a country choose to set aside land as a national park instead of developing it?', ['To preserve natural beauty and biodiversity for the future', 'Protecting land is never valuable to a country', 'National parks provide no benefit to wildlife', 'This concept has no relevance to social studies'], 0),
    ('What might visitors typically do in a national park?', ['Hike, camp, and observe wildlife responsibly', 'Build permanent factories', 'Remove protected plants and animals', 'Ignore all posted park rules'], 0),
    ('Why is it important to follow rules, such as staying on marked trails, in a national park?', ['Following rules helps protect fragile ecosystems from damage', 'Rules in national parks are never important', 'This concept has no connection to conservation', 'Trails have no effect on the surrounding environment'], 0)]),
]),
day(142, [
L('Vocabulary: Colloquialisms and Slang',
  'Grade 5 Language strand: a colloquialism is an informal word or expression used in everyday casual speech, while slang is very informal language often used by a particular group, both of which are usually avoided in formal writing.',
  [('What is a colloquialism?', ['An informal word or expression used in everyday casual speech', 'A formal word used only in academic writing', 'A word with no meaning at all', 'A type of punctuation mark'], 0),
   ('What is slang?', ['Very informal language often used by a particular group of people', 'A formal citation style', 'A word that always appears in a dictionary as standard usage', 'A type of grammar rule'], 0),
   ('Where would a colloquialism or slang term be least appropriate?', ['In a formal essay or business letter', 'In a casual conversation with friends', 'In an informal text message', 'In a friendly chat at lunch'], 0),
   ('Why might slang change quickly over time?', ['New informal expressions are often created and popularized by different groups', 'Slang words are always identical from generation to generation', 'This concept has no connection to vocabulary', 'Formal language changes more quickly than slang'], 0),
   ('Which of these is most likely an example of a colloquialism?', ['Gonna instead of going to', 'Photosynthesis', 'Metropolis', 'Encyclopedia'], 0)]),
M('Geometry: Rotational Symmetry',
  'Grade 5 Math strand: a shape has rotational symmetry if it can be turned less than a full circle around its centre and still look exactly the same as it did before turning.',
  [('What is rotational symmetry?', ['When a shape can be turned less than a full circle and still look the same', 'When a shape can only be folded in half to match', 'When a shape has no symmetry of any kind', 'When a shape has straight sides only'], 0),
   ('Around what point is a shape rotated when checking for rotational symmetry?', ['Its centre', 'Its longest edge', 'One of its corners only', 'A point outside the shape'], 0),
   ('Does a square have rotational symmetry?', ['Yes, it looks the same after turning it 90 degrees', 'No, a square never has rotational symmetry', 'Only if it is coloured red', 'Only if it is cut into triangles'], 0),
   ('How is rotational symmetry different from line symmetry?', ['Rotational symmetry involves turning a shape, while line symmetry involves folding it', 'The two types of symmetry are always identical', 'Line symmetry involves turning a shape around its centre', 'Rotational symmetry only applies to circles'], 0),
   ('Why might an equilateral triangle have rotational symmetry?', ['Turning it one third of a full circle makes it look the same as before', 'An equilateral triangle never looks the same after any turn', 'Only shapes with four sides can have rotational symmetry', 'This concept has no connection to geometry'], 0)]),
Sc('Ocean Currents and Their Effect on Climate',
   'Grade 5 Science strand: ocean currents are large-scale movements of water through the ocean that can carry warm or cool water long distances, influencing the climate of coastal regions.',
   [('What is an ocean current?', ['A large-scale movement of water through the ocean', 'A type of underwater mountain', 'A sudden storm at sea', 'A small wave near the shore'], 0),
    ('How can ocean currents affect climate?', ['They carry warm or cool water that can influence the temperature of coastal regions', 'Ocean currents have no effect on climate at all', 'Ocean currents only affect the depth of the ocean', 'Ocean currents remain in exactly the same spot forever'], 0),
    ('What might happen to a coastal regions climate if it is near a warm ocean current?', ['The region may experience milder temperatures than expected for its latitude', 'The region always becomes colder than any other location', 'The current has no impact on the regions weather', 'The region immediately freezes over completely'], 0),
    ('Why do scientists study ocean currents?', ['To better understand weather patterns, climate, and marine ecosystems', 'Ocean currents provide no useful scientific information', 'This concept has no connection to Earth science', 'Ocean currents never interact with marine life'], 0),
    ('What might cause ocean currents to move?', ['Factors such as wind, water temperature, and the rotation of the Earth', 'Ocean currents move for no reason at all', 'Ocean currents are caused only by boats passing through', 'This concept has no relevance to science'], 0)]),
SS('The Role of Political Parties in Canadian Government',
   'Grade 5 Social Studies strand: a political party is a group of people who share similar ideas about how the government should be run, and parties compete in elections to try to form the government.',
   [('What is a political party?', ['A group of people who share similar ideas about how government should be run', 'A single elected official with no supporters', 'A type of national holiday', 'A branch of the court system'], 0),
    ('What do political parties typically do during an election?', ['Compete to win seats and try to form the government', 'Refuse to select any candidates', 'Avoid sharing any ideas with voters', 'Cancel the election entirely'], 0),
    ('What might a political party publish to explain its ideas to voters?', ['A platform outlining its goals and policies', 'A private diary with no public access', 'A grocery list', 'A weather report'], 0),
    ('Why might having more than one political party be useful in a democracy?', ['It gives voters a choice between different ideas and approaches to government', 'Having more than one party is never useful', 'Political parties always share identical ideas', 'This concept has no connection to social studies'], 0),
    ('What happens to the political party that wins the most seats in a Canadian federal election?', ['It typically forms the government', 'It is immediately dissolved', 'It loses the right to participate in future elections', 'It automatically becomes a monarchy'], 0)]),
]),
day(143, [
L('Writing: Writing a Choose-Your-Own-Adventure Story',
  'Grade 5 Language strand: a choose-your-own-adventure story lets the reader make decisions for the main character at key points, branching into different paths that lead to different endings.',
  [('What makes a choose-your-own-adventure story different from a typical story?', ['The reader makes decisions that lead to different paths and endings', 'It has only one possible ending', 'It contains no characters at all', 'It must be written in poem form'], 0),
   ('What happens at a decision point in a choose-your-own-adventure story?', ['The reader chooses what the character should do next', 'The story automatically ends', 'The author picks a random new topic', 'Nothing changes in the story'], 0),
   ('Why might a writer plan a story map before writing a choose-your-own-adventure story?', ['It helps organize the different branching paths and endings', 'Planning is never useful for this kind of writing', 'This concept has no connection to writing', 'A story map only works for poetry'], 0),
   ('What might happen if a choose-your-own-adventure story has too few decision points?', ['The reader may have little sense of control over the story', 'The story becomes too long to read', 'The story can no longer have any characters', 'The story automatically becomes nonfiction'], 0),
   ('Why might readers enjoy choose-your-own-adventure stories?', ['They can actively shape how the story unfolds', 'Readers never enjoy stories with choices', 'This concept has no relevance to writing', 'These stories always have exactly one path'], 0)]),
M('Number Sense: Multiplying Three-Digit by Two-Digit Numbers',
  'Grade 5 Math strand: multiplying a three-digit number by a two-digit number can be done by breaking the two-digit number into tens and ones, multiplying each part separately, and adding the partial products together.',
  [('What is one strategy for multiplying a three-digit number by a two-digit number?', ['Breaking the two-digit number into tens and ones and adding the partial products', 'Only multiplying the ones digits of each number', 'Dividing both numbers before multiplying', 'Ignoring the tens digit of the two-digit number'], 0),
   ('What is 213 multiplied by 4?', ['852', '842', '862', '824'], 0),
   ('When multiplying 326 by 12, what could you calculate first using the partial products strategy?', ['326 multiplied by 10 and 326 multiplied by 2, then add the results', '326 divided by 12', '326 added to 12', '12 multiplied by itself'], 0),
   ('Why is it useful to check a multiplication answer with estimation?', ['Estimation helps confirm the final answer is reasonable', 'Estimation always gives the exact same answer as multiplying', 'This concept has no connection to number sense', 'Checking answers is never useful in mathematics'], 0),
   ('What is 145 multiplied by 3?', ['435', '425', '445', '415'], 0)]),
Sc('How Airplanes Fly — Lift, Thrust, Drag, and Weight',
   'Grade 5 Science strand: an airplane flies because of four forces acting on it, lift pushing it upward, weight pulling it downward, thrust moving it forward, and drag slowing it down, that must be balanced for controlled flight.',
   [('Which force pushes an airplane upward, allowing it to fly?', ['Lift', 'Weight', 'Thrust', 'Drag'], 0),
    ('Which force pulls an airplane downward toward Earth?', ['Weight', 'Lift', 'Thrust', 'Drag'], 0),
    ('Which force moves an airplane forward through the air?', ['Thrust', 'Lift', 'Weight', 'Drag'], 0),
    ('Which force acts against an airplanes motion, slowing it down?', ['Drag', 'Lift', 'Thrust', 'Weight'], 0),
    ('Why must these four forces be balanced for controlled flight?', ['If the forces are unbalanced, the airplane may climb, descend, speed up, or slow down unexpectedly', 'The four forces never actually affect an airplanes flight', 'An airplane can fly with only one of the four forces present', 'This concept has no relevance to science'], 0)]),
SS('Crown Land — Public Land Owned by the Government',
   'Grade 5 Social Studies strand: Crown land is public land owned by the federal or provincial government on behalf of all Canadians, often used for purposes such as forestry, conservation, or recreation.',
   [('What is Crown land?', ['Public land owned by the federal or provincial government', 'Land owned only by private individuals', 'Land that belongs to a foreign country', 'Land that no one is allowed to use for any purpose'], 0),
    ('On whose behalf is Crown land generally held?', ['All Canadians', 'A single wealthy family', 'Only the Prime Minister', 'A private international company'], 0),
    ('Which of these might Crown land be used for?', ['Forestry, conservation, or recreation', 'Only building private mansions', 'Selling to a foreign government', 'Nothing at all'], 0),
    ('Roughly what portion of Canadas land is often described as Crown land?', ['A very large portion, much more than half', 'None of Canadas land', 'Only a single city block', 'Exactly one percent'], 0),
    ('Why might it matter whether land is Crown land or privately owned?', ['It affects who can make decisions about how the land is used', 'Ownership of land never affects how it can be used', 'This concept has no connection to social studies', 'Crown land and private land are always treated identically'], 0)]),
]),
day(144, [
L('Grammar: Subject Complements and Predicate Adjectives',
  'Grade 5 Language strand: a subject complement follows a linking verb and renames or describes the subject, and a predicate adjective is a subject complement that describes the subject using an adjective.',
  [('What does a subject complement do?', ['It follows a linking verb and renames or describes the subject', 'It always shows an action taking place', 'It replaces the subject entirely', 'It only appears at the start of a sentence'], 0),
   ('What is a predicate adjective?', ['A subject complement that describes the subject using an adjective', 'A verb that shows action', 'A word that joins two sentences', 'A type of punctuation mark'], 0),
   ('In the sentence The soup is hot, which word is the predicate adjective?', ['Hot', 'Soup', 'Is', 'The'], 0),
   ('Which verb usually connects a subject to its subject complement?', ['A linking verb, such as is or seems', 'An action verb, such as run or jump', 'A helping verb used alone', 'A verb is never needed in this kind of sentence'], 0),
   ('Why is recognizing subject complements useful when checking a sentence?', ['It helps confirm that the sentence correctly describes or renames its subject', 'Subject complements never appear in complete sentences', 'This concept has no connection to grammar', 'Subject complements always come before the subject'], 0)]),
M('Algebra: Function Machines and Input-Output Tables',
  'Grade 5 Math strand: a function machine applies a rule to an input number to produce an output number, and recording several input-output pairs in a table can help reveal the rule being used.',
  [('What does a function machine do to an input number?', ['It applies a rule to produce an output number', 'It always leaves the number completely unchanged', 'It deletes the number entirely', 'It only works with letters, never numbers'], 0),
   ('If the rule of a function machine is add 5, what is the output when the input is 3?', ['8', '5', '3', '15'], 0),
   ('An input-output table shows 2 leads to 6, 3 leads to 9, and 4 leads to 12. What is the rule?', ['Multiply the input by 3', 'Add 3 to the input', 'Subtract 3 from the input', 'Divide the input by 3'], 0),
   ('Why might recording several input-output pairs in a table help find a rule?', ['Comparing multiple pairs makes a repeating pattern easier to identify', 'A single input-output pair always reveals the entire rule', 'Tables never help identify number patterns', 'This concept has no connection to algebra'], 0),
   ('If the rule is multiply by 2 then add 1, what is the output for an input of 4?', ['9', '8', '5', '10'], 0)]),
Sc('Renewable Energy in Focus: Tidal and Wave Power',
   'Grade 5 Science strand: tidal power captures energy from the rise and fall of ocean tides, while wave power captures energy from the motion of surface waves, both offering renewable sources of electricity.',
   [('What does tidal power capture energy from?', ['The rise and fall of ocean tides', 'The heat of the Sun', 'The wind blowing over land', 'Underground heat from the Earth'], 0),
    ('What does wave power capture energy from?', ['The motion of surface waves', 'The burning of coal', 'The rotation of the Moon around the Sun', 'The melting of glaciers'], 0),
    ('Why are tidal and wave power considered renewable sources of energy?', ['The motion of tides and waves is naturally and continuously replenished', 'Tides and waves will eventually run out permanently', 'Renewable energy always comes from burning fuels', 'This concept has no connection to renewable energy'], 0),
    ('Where would tidal and wave power technology most likely be located?', ['Along coastlines or in the ocean', 'In the middle of a desert', 'Deep underground in a mine', 'On top of a tall mountain'], 0),
    ('What is one possible advantage of tidal power compared with some other renewable sources?', ['Ocean tides follow a predictable daily pattern', 'Tides never follow any kind of pattern', 'Tidal power always produces more pollution than fossil fuels', 'This concept has no relevance to renewable energy'], 0)]),
SS('The Canadian Armed Forces — Structure and Roles',
   'Grade 5 Social Studies strand: the Canadian Armed Forces are made up of the Army, Navy, and Air Force, and they work to defend Canada, support international peace efforts, and assist during domestic emergencies.',
   [('What are the three main branches of the Canadian Armed Forces?', ['The Army, Navy, and Air Force', 'The Senate, House of Commons, and Courts', 'The Police, Fire Department, and Coast Guard', 'The Federal, Provincial, and Municipal governments'], 0),
    ('What is one role of the Canadian Armed Forces?', ['Defending Canada and supporting international peace efforts', 'Collecting income taxes from citizens', 'Passing new federal laws', 'Running Canadas school system'], 0),
    ('How might the Canadian Armed Forces help during a domestic emergency, such as a flood?', ['By assisting with evacuation, rescue, and recovery efforts', 'They are never involved in emergencies within Canada', 'They only operate outside of Canada', 'This concept has no relevance to social studies'], 0),
    ('What does it mean for the Canadian Armed Forces to support international peace efforts?', ['They may take part in peacekeeping missions in other countries', 'They are not permitted to work outside Canada under any circumstances', 'International peace efforts have no connection to the military', 'They replace the governments of other countries'], 0),
    ('Why might a country maintain armed forces even during peaceful times?', ['To be prepared to defend the country and respond to emergencies if needed', 'Armed forces serve no purpose during peaceful times', 'This concept has no connection to government', 'Armed forces are only useful during a declared war'], 0)]),
]),
day(145, [
L('Reading: Understanding Motif in a Story',
  'Grade 5 Language strand: a motif is an image, idea, or symbol that repeats throughout a story, helping to reinforce its theme or central message.',
  [('What is a motif?', ['An image, idea, or symbol that repeats throughout a story', 'A single event that happens only once', 'The title of a story', 'A list of characters in a story'], 0),
   ('What does a motif often help reinforce in a story?', ['The theme or central message', 'The page numbers of the book', 'The name of the publisher', 'The font used in printing'], 0),
   ('If the image of light appears again and again in a story about hope, what might that be an example of?', ['A motif', 'A footnote', 'A glossary', 'An index'], 0),
   ('How is a motif different from a single symbol that appears only once?', ['A motif repeats multiple times throughout the story, reinforcing its importance', 'A motif always appears exactly one time', 'A motif and a symbol are never related in any way', 'A motif only appears in the title of a story'], 0),
   ('Why might recognizing a motif help a reader understand a story more deeply?', ['It can reveal a pattern connected to the storys deeper meaning', 'Motifs never connect to a storys meaning', 'This concept has no relevance to reading', 'Motifs only appear in nonfiction texts'], 0)]),
M('Measurement: Same Perimeter, Different Area — Exploring Rectangles',
  'Grade 5 Math strand: two rectangles can have the same perimeter but different areas, showing that perimeter and area measure different things and do not always change together.',
  [('Can two rectangles have the same perimeter but different areas?', ['Yes, changing the shape while keeping the perimeter the same can change the area', 'No, rectangles with the same perimeter always have the same area', 'Only if both rectangles are squares', 'This is impossible for any pair of rectangles'], 0),
   ('A rectangle with sides 2 and 8 has a perimeter of 20. What is its area?', ['16 square units', '20 square units', '10 square units', '32 square units'], 0),
   ('A rectangle with sides 5 and 5 also has a perimeter of 20. What is its area?', ['25 square units', '20 square units', '10 square units', '16 square units'], 0),
   ('Comparing the two rectangles above, what do you notice?', ['Equal perimeters can still produce different areas', 'Equal perimeters always produce equal areas', 'Area and perimeter are always exactly the same number', 'Neither rectangle actually has a perimeter of 20'], 0),
   ('Why is it useful to understand that perimeter and area measure different things?', ['It helps avoid assuming that a larger perimeter always means a larger area', 'Perimeter and area always increase or decrease together', 'This concept has no connection to measurement', 'Area can never be calculated once perimeter is known'], 0)]),
Sc('Rusting and Corrosion — A Common Chemical Change',
   'Grade 5 Science strand: rusting is a chemical change that occurs when iron reacts with oxygen and moisture in the air, gradually forming a reddish-brown substance called rust that weakens the metal.',
   [('What is rusting?', ['A chemical change that occurs when iron reacts with oxygen and moisture', 'A physical change that only affects the shape of an object', 'A process that only happens to wood', 'A type of change that always requires heat from fire'], 0),
    ('What two things does iron react with to form rust?', ['Oxygen and moisture', 'Sunlight and sand', 'Heat and salt water only', 'Electricity and glass'], 0),
    ('What colour is rust typically?', ['Reddish-brown', 'Bright blue', 'Pure white', 'Deep purple'], 0),
    ('Why is rusting considered a chemical change rather than a physical change?', ['A new substance, rust, forms that has different properties from the original iron', 'Rusting never actually changes the properties of a material', 'Chemical changes never involve forming a new substance', 'Rusting is identical to melting or freezing'], 0),
    ('Why might people try to prevent metal objects from rusting?', ['Rust can weaken metal and damage its structure over time', 'Rust always makes metal objects stronger', 'Preventing rust has no benefit at all', 'This concept has no relevance to science'], 0)]),
SS('How Government Budgets Are Planned and Passed',
   'Grade 5 Social Studies strand: a government budget outlines planned spending and expected revenue for the year, and it must typically be proposed, debated, and approved before it can take effect.',
   [('What does a government budget outline?', ['Planned spending and expected revenue for the year', 'The names of every citizen in the country', 'The exact weather forecast for the year', 'A list of every book in a library'], 0),
    ('What usually happens to a budget before it can take effect?', ['It must be proposed, debated, and approved', 'It is automatically approved with no discussion', 'It is decided by a single citizen chosen at random', 'It never requires any kind of approval'], 0),
    ('Why might elected officials debate a proposed budget?', ['To discuss whether the planned spending reflects the needs and priorities of citizens', 'Debating a budget serves no purpose at all', 'Budgets are never discussed before being passed', 'This concept has no connection to government'], 0),
    ('What might happen if a government spends more money than it collects in revenue?', ['It may need to borrow money, leading to a budget deficit', 'The government always has extra money left over', 'Overspending never has any effect on a government', 'This concept has no relevance to social studies'], 0),
    ('Why is planning a budget an important responsibility of government?', ['It helps ensure public money is used responsibly to meet the needs of citizens', 'Budgets have no connection to how a government functions', 'This concept has no relevance to social studies', 'A government never needs to plan how it spends money'], 0)]),
]),
day(146, [
L('Grammar: Using Ellipses and Em Dashes',
  'Grade 5 Language strand: an ellipsis, three dots, shows a pause, trailing thought, or omitted words, while an em dash marks a sudden break or emphasizes extra information in a sentence.',
  [('What does an ellipsis usually show in a sentence?', ['A pause, trailing thought, or omitted words', 'The end of a formal letter', 'A list of exactly three items', 'A question being asked'], 0),
   ('How many dots make up an ellipsis?', ['Three', 'Two', 'Four', 'One'], 0),
   ('What can an em dash be used for in a sentence?', ['To mark a sudden break or emphasize extra information', 'To end every sentence in a paragraph', 'To replace all commas in a text', 'To show that a word is misspelled'], 0),
   ('Which sentence correctly uses an em dash to add emphasis?', ['The trip — long and exhausting — finally ended.', 'The trip, long, and, exhausting, finally ended.', 'The trip long and exhausting finally, ended.', 'The, trip, long and exhausting finally ended.'], 0),
   ('Why might a writer choose an ellipsis instead of finishing a sentence completely?', ['To show hesitation, suspense, or an unfinished thought', 'An ellipsis always completes every idea fully', 'This concept has no connection to grammar', 'An ellipsis is required at the end of every sentence'], 0)]),
M('Financial Literacy: Comparing Interest Rates and Choosing a Savings Account',
  'Grade 5 Math strand: an interest rate shows how much extra money a savings account earns over time, and comparing rates from different accounts can help someone decide where their savings will grow the most.',
  [('What does an interest rate tell you about a savings account?', ['How much extra money the account earns over time', 'The exact date the account was opened', 'The colour of the bank card', 'The number of transactions allowed per day'], 0),
   ('If Account A offers 2 percent interest and Account B offers 4 percent interest, which account will generally grow savings faster?', ['Account B', 'Account A', 'They will grow at exactly the same rate', 'Neither account can ever earn any interest'], 0),
   ('Why might someone compare interest rates before opening a savings account?', ['To choose the account that will help their money grow the most over time', 'Interest rates are always identical at every bank', 'Comparing rates has no effect on savings', 'This concept has no connection to financial literacy'], 0),
   ('If you save 100 dollars in an account with 5 percent interest for one year, about how much interest would you earn?', ['5 dollars', '10 dollars', '50 dollars', '1 dollar'], 0),
   ('Besides the interest rate, what else might be important to consider when choosing a savings account?', ['Fees or rules the bank may charge or require', 'The interest rate is the only factor that ever matters', 'The account colour available at the bank', 'This concept has no relevance to financial literacy'], 0)]),
Sc('Adaptations for Flight — How Birds and Insects Take to the Air',
   'Grade 5 Science strand: birds and insects have special adaptations for flight, such as lightweight bodies, wings shaped to create lift, and strong muscles, that allow them to move efficiently through the air.',
   [('What is one adaptation that helps birds fly?', ['Lightweight, hollow bones', 'Extremely heavy, solid bones', 'Bodies that cannot move at all', 'An inability to flap their wings'], 0),
    ('How are bird and insect wings generally shaped to help with flight?', ['Shaped to help create lift as air moves over and under them', 'Shaped only to block sunlight', 'Shaped so that no air can pass around them at all', 'Shaped exactly like a flat rectangle with no curve'], 0),
    ('What kind of muscles do flying animals typically need?', ['Strong muscles to power their wings', 'No muscles are needed for flight', 'Only muscles located in their legs', 'Muscles that never contract or move'], 0),
    ('Why might a lightweight body be an advantage for a flying animal?', ['Less weight makes it easier to become airborne and stay in the air', 'A heavier body always makes flying easier', 'Body weight has no connection to flight', 'This concept has no relevance to science'], 0),
    ('Why do insects and birds both have adaptations suited to flight, even though they are very different animals?', ['Both types of animals evolved features that help them succeed in a similar environment, the air', 'Insects and birds share the exact same body structure', 'Adaptations for flight only apply to birds, never insects', 'This concept has no connection to living things'], 0)]),
SS('Referendums — Direct Democracy in Canada',
   'Grade 5 Social Studies strand: a referendum is a direct vote in which citizens decide on a specific question or issue, rather than electing a representative to decide on their behalf.',
   [('What is a referendum?', ['A direct vote in which citizens decide on a specific question or issue', 'An election to choose a new Prime Minister', 'A private meeting held only by government officials', 'A type of criminal court trial'], 0),
    ('How is a referendum different from a typical election?', ['In a referendum, citizens vote directly on an issue rather than electing a representative', 'A referendum and an election are always exactly the same thing', 'A referendum never involves any voting at all', 'Only elected officials are allowed to vote in a referendum'], 0),
    ('What might a referendum ask citizens to decide?', ['A specific question, such as whether to approve a new law or policy', 'The winner of a sports championship', 'The weather forecast for the next election', 'A private business decision'], 0),
    ('Why might a government hold a referendum on an important issue?', ['To directly involve citizens in a major decision affecting their community or country', 'Referendums are never used to gather public opinion', 'This concept has no connection to social studies', 'A referendum removes the need for citizens to vote at all'], 0),
    ('Why is a referendum considered an example of direct democracy?', ['Citizens vote directly on the issue itself instead of through a representative', 'Direct democracy means only one person makes every decision', 'A referendum always cancels the need for any government', 'This concept has no relevance to Canadian government'], 0)]),
]),
day(147, [
L('Media Literacy: Understanding Sponsored Content and Advertising Disclosures',
  'Grade 5 Language strand: sponsored content is material paid for by a company or organization to promote a product or message, and it is often required to include a disclosure so readers know it is an advertisement.',
  [('What is sponsored content?', ['Material paid for by a company or organization to promote a product or message', 'A completely unbiased news report with no sponsor', 'A story written entirely by a random reader', 'A government safety announcement'], 0),
   ('What is the purpose of an advertising disclosure?', ['To let readers know that content is actually an advertisement', 'To hide the fact that content is paid for', 'To replace the need for real information', 'To make an advertisement look like a private diary entry'], 0),
   ('Why might a company pay for sponsored content instead of a traditional advertisement?', ['It can blend more naturally into regular articles or posts, reaching readers in a different way', 'Sponsored content is always clearly separated from all other content', 'Companies never pay for content of any kind', 'This concept has no connection to media literacy'], 0),
   ('Why is it important for readers to notice a sponsored content label?', ['It helps readers understand that the content may be biased toward promoting a product', 'Labels on sponsored content never provide any useful information', 'Sponsored content is always completely neutral', 'This concept has no relevance to media literacy'], 0),
   ('Which of these is most likely a sign of sponsored content?', ['A label reading Promoted or Paid Partnership next to an article', 'A byline listing a professional news reporter', 'A dateline showing when a news event occurred', 'A correction printed at the bottom of an article'], 0)]),
M('Data Management: Choosing the Most Appropriate Type of Graph for a Data Set',
  'Grade 5 Math strand: different types of graphs, such as bar graphs, line graphs, and circle graphs, are each best suited to displaying certain kinds of data, so choosing the right graph makes information clearer.',
  [('Why might different graphs be better suited to different kinds of data?', ['Each type of graph highlights a data set in a different, more effective way', 'All graphs display every kind of data in exactly the same way', 'Only one type of graph exists for any kind of data', 'This concept has no connection to data management'], 0),
   ('Which type of graph is generally best for showing change over time?', ['A line graph', 'A circle graph', 'A single bar with no scale', 'A list with no visual display'], 0),
   ('Which type of graph is generally best for comparing parts of a whole as percentages?', ['A circle graph', 'A line graph', 'A scatter plot', 'A number line'], 0),
   ('Which type of graph is generally best for comparing separate categories, such as favourite fruits?', ['A bar graph', 'A line graph showing change over time', 'A circle graph only', 'A Venn diagram only'], 0),
   ('Why might choosing the wrong type of graph make data harder to understand?', ['The chosen graph may not clearly highlight the patterns or comparisons in the data', 'Every type of graph always communicates data equally well', 'The type of graph never affects how clear the data appears', 'This concept has no relevance to data management'], 0)]),
Sc('Earthquakes — Causes and Measuring Magnitude',
   'Grade 5 Science strand: an earthquake occurs when built-up stress along a fault in Earths crust is suddenly released, and scientists measure the strength of an earthquake using a magnitude scale.',
   [('What causes an earthquake?', ['Built-up stress along a fault being suddenly released', 'A sudden drop in air temperature', 'The Moon passing in front of the Sun', 'Ocean waves crashing onto the shore'], 0),
    ('What is a fault in Earths crust?', ['A crack or fracture where rock has moved or may move', 'A type of cloud formation', 'A layer of the atmosphere', 'A kind of ocean current'], 0),
    ('What do scientists use to measure the strength of an earthquake?', ['A magnitude scale', 'A thermometer', 'A rain gauge', 'A wind vane'], 0),
    ('Why might a higher magnitude earthquake cause more damage than a lower magnitude one?', ['A higher magnitude generally releases more energy, causing stronger shaking', 'Magnitude has no connection to the strength of shaking', 'Lower magnitude earthquakes always cause more damage', 'This concept has no relevance to Earth science'], 0),
    ('Why do scientists study earthquakes and their causes?', ['To better understand and prepare for the risks earthquakes pose to people and buildings', 'Studying earthquakes provides no useful information', 'This concept has no connection to science', 'Earthquakes cannot be measured or studied in any way'], 0)]),
SS('The Fathers of Confederation',
   'Grade 5 Social Studies strand: the Fathers of Confederation were the political leaders who worked together in the 1860s to negotiate and establish the union of provinces that became Canada in 1867.',
   [('Who were the Fathers of Confederation?', ['The political leaders who negotiated and established the union that became Canada', 'A group of early explorers who mapped Canada', 'The first monarchs to rule over Canada', 'A group of modern-day Canadian athletes'], 0),
    ('In what decade did the Fathers of Confederation do most of their negotiating?', ['The 1860s', 'The 1700s', 'The 1930s', 'The 1990s'], 0),
    ('What major event did the work of the Fathers of Confederation lead to?', ['The formation of Canada in 1867', 'The building of the Canadian Pacific Railway', 'The signing of the Charter of Rights and Freedoms', 'The start of the Second World War'], 0),
    ('Why might representatives from different colonies have needed to negotiate before Confederation could happen?', ['Each colony had its own interests and concerns that needed to be addressed', 'All colonies always agreed on everything without any discussion', 'Negotiation was never necessary to form Canada', 'This concept has no connection to Canadian history'], 0),
    ('Why do Canadians still study the Fathers of Confederation today?', ['Their decisions helped shape the foundation of the country and its government', 'Their work has no connection to modern Canada', 'This concept has no relevance to social studies', 'Confederation happened without any planning or leadership'], 0)]),
]),
day(148, [
L('Writing: Writing a Reflective Journal Entry',
  'Grade 5 Language strand: a reflective journal entry describes a personal experience and explores the writers thoughts, feelings, and what they learned from it.',
  [('What does a reflective journal entry mainly explore?', ['The writers thoughts, feelings, and what they learned from an experience', 'Only the weather on a given day', 'A list of unrelated facts', 'A formal scientific procedure'], 0),
   ('Which of these is most likely found in a reflective journal entry?', ['A description of what the writer learned from a personal experience', 'A list of ingredients for a recipe', 'Step-by-step instructions for building something', 'A formal business proposal'], 0),
   ('Why might a writer include their feelings in a reflective journal entry?', ['Feelings help show how the experience personally affected the writer', 'Feelings are never relevant to reflective writing', 'This concept has no connection to writing', 'A reflective entry must avoid all personal opinions'], 0),
   ('What is one benefit of writing reflective journal entries regularly?', ['It can help a writer notice patterns in their thoughts and personal growth over time', 'Reflective writing never helps a person understand themselves', 'This concept has no relevance to language arts', 'Regular writing always weakens a writers thinking skills'], 0),
   ('How is a reflective journal entry different from a procedural How-To text?', ['A reflective entry explores personal thoughts and feelings rather than giving step-by-step instructions', 'A reflective entry always gives step-by-step instructions', 'The two types of writing are identical in purpose', 'A reflective entry never includes any personal thoughts'], 0)]),
M('Geometry: Sum of Interior Angles in Triangles and Quadrilaterals',
  'Grade 5 Math strand: the interior angles of any triangle always add up to 180 degrees, and the interior angles of any quadrilateral always add up to 360 degrees.',
  [('What do the interior angles of any triangle always add up to?', ['180 degrees', '90 degrees', '360 degrees', '270 degrees'], 0),
   ('What do the interior angles of any quadrilateral always add up to?', ['360 degrees', '180 degrees', '90 degrees', '450 degrees'], 0),
   ('A triangle has angles measuring 60 degrees and 70 degrees. What is the measure of the third angle?', ['50 degrees', '60 degrees', '70 degrees', '40 degrees'], 0),
   ('A quadrilateral has three angles measuring 90, 90, and 90 degrees. What is the measure of the fourth angle?', ['90 degrees', '80 degrees', '100 degrees', '180 degrees'], 0),
   ('Why is knowing the interior angle sum of a triangle useful?', ['It lets you find a missing angle when the other two angles are known', 'It has no use when solving geometry problems', 'This concept has no connection to angles', 'The interior angle sum of a triangle changes with every triangle'], 0)]),
Sc('The Process of Distillation — Separating Mixtures',
   'Grade 5 Science strand: distillation is a method of separating a mixture by heating it until part of it evaporates, then cooling the vapour so it condenses back into a liquid, leaving other substances behind.',
   [('What is distillation?', ['A method of separating a mixture by evaporating and then condensing part of it', 'A method of freezing an entire mixture solid', 'A method of adding more substances to a mixture', 'A method that only works on solid objects'], 0),
    ('What happens first during distillation?', ['Part of the mixture is heated until it evaporates', 'The entire mixture instantly freezes', 'The mixture is buried underground', 'The mixture is exposed to strong magnets'], 0),
    ('What happens to the vapour produced during distillation?', ['It is cooled so it condenses back into a liquid', 'It disappears completely and is never seen again', 'It turns directly into a solid without cooling', 'It is ignored for the rest of the process'], 0),
    ('Why is distillation a useful way to separate a mixture, such as salt water?', ['It can separate substances with different boiling points, leaving one behind', 'Distillation never actually separates any substances', 'This concept has no connection to science', 'Distillation only works on mixtures of two solids'], 0),
    ('Why might distillation be used to help purify drinking water?', ['It can help remove certain dissolved substances from water', 'Distillation always makes water less safe to drink', 'This concept has no relevance to science', 'Distillation cannot be used with water at all'], 0)]),
SS('School Boards and Trustees — Local Education Governance',
   'Grade 5 Social Studies strand: a school board is a locally elected body responsible for overseeing public schools in a region, and trustees are the elected members who help make decisions about education in their community.',
   [('What is a school board responsible for?', ['Overseeing public schools in a region', 'Running the federal government', 'Managing a countrys national defence', 'Printing national currency'], 0),
    ('What is a trustee?', ['An elected member who helps make decisions about education in their community', 'A judge in a criminal court', 'A member of the Senate', 'A leader of a national political party'], 0),
    ('How do most trustees become part of a school board?', ['They are elected by voters in their local area', 'They are chosen randomly with no vote', 'They inherit the position from a family member', 'They are appointed by a foreign government'], 0),
    ('What kinds of decisions might a school board make?', ['Decisions about school budgets, programs, and policies', 'Decisions about international trade agreements', 'Decisions about national holidays', 'Decisions about provincial court cases'], 0),
    ('Why is local governance of education, such as through school boards, considered important?', ['It allows decisions about schools to reflect the needs of the local community', 'Local governance of education has no benefit to communities', 'This concept has no connection to social studies', 'School boards are never involved in decisions about education'], 0)]),
]),
day(149, [
L('Oral Communication: Giving and Receiving Constructive Feedback',
  'Grade 5 Language strand: constructive feedback offers specific, respectful suggestions to help someone improve their work, focusing on both strengths and areas for growth.',
  [('What is constructive feedback?', ['Specific, respectful suggestions that help someone improve their work', 'Feedback that only criticizes without any suggestions', 'A response that ignores the persons work entirely', 'Feedback given without ever listening to the speaker'], 0),
   ('What should constructive feedback usually include?', ['Both strengths and areas for growth', 'Only negative comments', 'Only compliments with no suggestions', 'A completely unrelated topic'], 0),
   ('Why is it helpful to be specific when giving feedback?', ['Specific feedback helps the person understand exactly what to improve', 'Vague feedback is always more helpful than specific feedback', 'This concept has no connection to oral communication', 'Specific feedback always discourages the listener'], 0),
   ('How should a person typically respond when receiving feedback?', ['By listening carefully and considering the suggestions respectfully', 'By ignoring the feedback completely', 'By arguing with every comment immediately', 'By refusing to make eye contact with the speaker'], 0),
   ('Why might giving feedback in a respectful tone matter?', ['A respectful tone helps the listener feel comfortable and open to improving', 'Tone never affects how feedback is received', 'This concept has no relevance to communication', 'A harsh tone always leads to the best results'], 0)]),
M('Number Sense: Dividing Decimals by Two-Digit Whole Numbers',
  'Grade 5 Math strand: dividing a decimal by a two-digit whole number follows the same steps as whole number division, keeping careful track of the decimal point in the quotient.',
  [('When dividing a decimal by a whole number, what must you keep careful track of?', ['The placement of the decimal point in the quotient', 'The colour of the numbers', 'The order the numbers were written in the problem', 'The number of letters in the problem'], 0),
   ('What is 8.4 divided by 12?', ['0.7', '7', '0.07', '70'], 0),
   ('What is 39.6 divided by 12?', ['3.3', '33', '0.33', '330'], 0),
   ('Why might it help to estimate before dividing a decimal by a two-digit number?', ['Estimating gives a reasonable target to check your final answer against', 'Estimating always gives the exact same value as the real answer', 'Estimation is never useful when dividing decimals', 'This concept has no connection to number sense'], 0),
   ('What is 15.5 divided by 5?', ['3.1', '3.5', '2.1', '31'], 0)]),
Sc('Herbivores, Carnivores, and Omnivores — Comparing Diets',
   'Grade 5 Science strand: animals can be classified by diet as herbivores, which eat only plants, carnivores, which eat only other animals, or omnivores, which eat both plants and animals.',
   [('What does a herbivore eat?', ['Only plants', 'Only other animals', 'Both plants and animals', 'Nothing at all'], 0),
    ('What does a carnivore eat?', ['Only other animals', 'Only plants', 'Both plants and animals', 'Rocks and soil'], 0),
    ('What does an omnivore eat?', ['Both plants and animals', 'Only plants', 'Only other animals', 'Neither plants nor animals'], 0),
    ('Which of these animals is most likely a carnivore?', ['A lion', 'A rabbit', 'A deer', 'A cow'], 0),
    ('Why might an animals teeth shape give a clue about its diet?', ['Sharp teeth often suit eating meat, while flatter teeth often suit grinding plants', 'Teeth shape never has any connection to what an animal eats', 'All animals have exactly the same teeth regardless of diet', 'This concept has no relevance to life science'], 0)]),
SS('Interest Groups and Lobbying in Canadian Politics',
   'Grade 5 Social Studies strand: an interest group is an organization that tries to influence government decisions on a specific issue, often through lobbying, which means directly encouraging lawmakers to support their cause.',
   [('What is an interest group?', ['An organization that tries to influence government decisions on a specific issue', 'A group that has no opinion on any issue', 'A branch of the federal court system', 'A type of national election'], 0),
    ('What does lobbying involve?', ['Directly encouraging lawmakers to support a particular cause', 'Refusing to communicate with any government official', 'Running in a federal election', 'Writing a new national anthem'], 0),
    ('What might an interest group focus on, such as an environmental organization?', ['Encouraging government action on a specific issue, like protecting the environment', 'Selling unrelated products to the public', 'Managing a countrys currency', 'Running a public school system'], 0),
    ('Why might interest groups try to communicate with elected officials?', ['To share information and try to influence decisions that affect their cause', 'Interest groups are never allowed to contact elected officials', 'This concept has no connection to social studies', 'Elected officials never listen to any outside opinions'], 0),
    ('Why is it important for citizens to understand how interest groups and lobbying work?', ['It helps citizens understand different influences on government decision-making', 'Interest groups have no effect on government decisions', 'This concept has no relevance to social studies', 'Lobbying is illegal in Canada and never takes place'], 0)]),
]),
day(150, [
L('Language Review: Vocabulary, Grammar, Writing, and Oral Communication',
  'Grade 5 Language strand review: students revisit oxymorons, colloquialisms and slang, choose-your-own-adventure stories, subject complements, and motif.',
  [('What is an oxymoron?', ['A figure of speech that combines two contradictory or opposite words', 'A word that rhymes with another word', 'A word borrowed from another language', 'A sentence with no verb'], 0),
   ('What is a colloquialism?', ['An informal word or expression used in everyday casual speech', 'A formal word used only in academic writing', 'A word with no meaning at all', 'A type of punctuation mark'], 0),
   ('What makes a choose-your-own-adventure story different from a typical story?', ['The reader makes decisions that lead to different paths and endings', 'It has only one possible ending', 'It contains no characters at all', 'It must be written in poem form'], 0),
   ('What does a subject complement do?', ['It follows a linking verb and renames or describes the subject', 'It always shows an action taking place', 'It replaces the subject entirely', 'It only appears at the start of a sentence'], 0),
   ('What is a motif?', ['An image, idea, or symbol that repeats throughout a story', 'A single event that happens only once', 'The title of a story', 'A list of characters in a story'], 0)]),
M('Math Review: Data, Symmetry, Algebra, and Decimals',
  'Grade 5 Math strand review: students revisit Venn diagrams, rotational symmetry, multiplying three-digit by two-digit numbers, function machines, and same perimeter/different area.',
  [('What does a Venn diagram use to sort and compare data?', ['Overlapping circles', 'A single straight line', 'A pie-shaped wedge only', 'A list with no visual shapes'], 0),
   ('What is rotational symmetry?', ['When a shape can be turned less than a full circle and still look the same', 'When a shape can only be folded in half to match', 'When a shape has no symmetry of any kind', 'When a shape has straight sides only'], 0),
   ('What is one strategy for multiplying a three-digit number by a two-digit number?', ['Breaking the two-digit number into tens and ones and adding the partial products', 'Only multiplying the ones digits of each number', 'Dividing both numbers before multiplying', 'Ignoring the tens digit of the two-digit number'], 0),
   ('What does a function machine do to an input number?', ['It applies a rule to produce an output number', 'It always leaves the number completely unchanged', 'It deletes the number entirely', 'It only works with letters, never numbers'], 0),
   ('Can two rectangles have the same perimeter but different areas?', ['Yes, changing the shape while keeping the perimeter the same can change the area', 'No, rectangles with the same perimeter always have the same area', 'Only if both rectangles are squares', 'This is impossible for any pair of rectangles'], 0)]),
Sc('Science Review: Earth Science, Physical Science, and Living Things',
   'Grade 5 Science strand review: students revisit mineral properties, ocean currents, the four forces of flight, tidal and wave power, and rusting.',
   [('What does the hardness of a mineral measure?', ['Its resistance to being scratched', 'Its exact weight in grams', 'Its temperature at all times', 'Its ability to conduct electricity only'], 0),
    ('What is an ocean current?', ['A large-scale movement of water through the ocean', 'A type of underwater mountain', 'A sudden storm at sea', 'A small wave near the shore'], 0),
    ('Which force pushes an airplane upward, allowing it to fly?', ['Lift', 'Weight', 'Thrust', 'Drag'], 0),
    ('What does tidal power capture energy from?', ['The rise and fall of ocean tides', 'The heat of the Sun', 'The wind blowing over land', 'Underground heat from the Earth'], 0),
    ('What is rusting?', ['A chemical change that occurs when iron reacts with oxygen and moisture', 'A physical change that only affects the shape of an object', 'A process that only happens to wood', 'A type of change that always requires heat from fire'], 0)]),
SS('Social Studies Review: Parks, Government, and Canadian History',
   'Grade 5 Social Studies strand review: students revisit national parks, political parties, Crown land, the Canadian Armed Forces, and government budgets.',
   [('What is the purpose of a national park?', ['To protect wildlife, ecosystems, and landscapes for future generations', 'To build as many new roads as possible', 'To sell natural resources as quickly as possible', 'To prevent anyone from ever visiting the area'], 0),
    ('What is a political party?', ['A group of people who share similar ideas about how government should be run', 'A single elected official with no supporters', 'A type of national holiday', 'A branch of the court system'], 0),
    ('What is Crown land?', ['Public land owned by the federal or provincial government', 'Land owned only by private individuals', 'Land that belongs to a foreign country', 'Land that no one is allowed to use for any purpose'], 0),
    ('What are the three main branches of the Canadian Armed Forces?', ['The Army, Navy, and Air Force', 'The Senate, House of Commons, and Courts', 'The Police, Fire Department, and Coast Guard', 'The Federal, Provincial, and Municipal governments'], 0),
    ('What does a government budget outline?', ['Planned spending and expected revenue for the year', 'The names of every citizen in the country', 'The exact weather forecast for the year', 'A list of every book in a library'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_141_150)
    append_to(5, g5_141_150)
