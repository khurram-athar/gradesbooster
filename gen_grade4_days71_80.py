#!/usr/bin/env python3
"""Phase 3 extension: Grade 4, Days 71-80 (third batch past the Day 70
milestone, pushing toward the full 157-day year). Topics chosen to avoid
any overlap with the existing Day 1-70 set (see data/grade4.json and
gen_grade4_days61_70.py): proverbs and adages, onomatopoeia, compound and
complex sentences, character traits and motivation, opinion writing,
contractions, adjective order, setting and mood, media literacy;
comparing/ordering numbers, the distributive property, long division of
3-digit numbers, fraction of a set, nets of 3D figures, double bar
graphs, converting metric units of length, congruent shapes, and
shopping/estimating totals; freshwater habitats, migration and
hibernation, fossils, mechanical advantage, shadows, weathering,
pollination, renewable energy, and structural foundations; ancient
Persia, the Vikings, early farming, the Great Lakes, Canadian capital
cities, Arctic communities, transportation networks, rivers and early
civilizations, and ancient trade routes. Day 80 of every subject is a
review lesson synthesizing that subject's Days 71-79 topics.

Subject keys for Grade 4 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 4 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L4 = 'https://tvolearn.com/pages/grade-4-language'
M4 = 'https://tvolearn.com/pages/grade-4-mathematics'
S4 = 'https://tvolearn.com/pages/grade-4-science-and-technology'
SS4 = 'https://tvolearn.com/pages/grade-4-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 4 Language',
    'TVO Learn: Grade 4 Mathematics',
    'TVO Learn: Grade 4 Science and Technology',
    'TVO Learn: Grade 4 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L4, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M4, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S4, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS4, q)


g4_71_80 = [
day(71, [
L('Vocabulary: Proverbs and Adages',
  'Grade 4 Language strand: a proverb or adage is a short, well-known saying that expresses a piece of traditional wisdom or advice, such as look before you leap.',
  [('A proverb or adage is best described as a short saying that expresses ___.', ['Traditional wisdom or advice', 'A character’s exact name', 'X unrelated to proverbs', 'A story’s complete plot'], 0),
   ('Which saying is an example of a proverb?', ['Look before you leap', 'The sky is blue today', 'X unrelated to proverbs', 'My shoes are red'], 0),
   ('The proverb the early bird catches the worm suggests that ___.', ['Acting early often brings success', 'Birds only eat worms in the morning', 'X unrelated to this proverb', 'Waiting is always the best choice'], 0),
   ('Why do people still use proverbs that are hundreds of years old?', ['Their advice about life often still applies today', 'Old sayings have no meaning today', 'X unrelated to using proverbs', 'Proverbs are only used in ancient texts'], 0),
   ('Which proverb best warns against judging something only by its outward appearance?', ['Don’t judge a book by its cover', 'The early bird catches the worm', 'X unrelated to this proverb', 'Practice makes perfect'], 0)]),
M('Comparing and Ordering Numbers to 10,000',
  'Grade 4 Math strand: comparing and ordering numbers to 10,000 means using place value to decide whether one number is greater than, less than, or equal to another, and arranging numbers from least to greatest or greatest to least.',
  [('To compare two numbers, you should first look at the digit with the greatest ___.', ['Place value', 'Colour', 'X unrelated to comparing numbers', 'Font size'], 0),
   ('Which symbol means greater than?', ['>', '<', 'X unrelated to comparing numbers', '='], 0),
   ('Which number is greater: 4,562 or 4,265?', ['4,562', '4,265', 'X unrelated to this comparison', 'They are equal'], 0),
   ('Which of these lists correctly orders the numbers from least to greatest?', ['3,021; 3,120; 3,201', '3,201; 3,120; 3,021', 'X unrelated to this ordering', '3,120; 3,201; 3,021'], 0),
   ('Why is comparing and ordering numbers a useful skill in everyday life?', ['It helps make sense of amounts, scores, or measurements', 'Comparing numbers serves no everyday purpose', 'X unrelated to comparing numbers', 'Every number is always considered equal in size'], 0)]),
Sc('Freshwater Habitats: Ponds, Lakes, and Rivers',
   'Grade 4 Science strand: freshwater habitats, such as ponds, lakes, and rivers, contain low levels of salt and support plants and animals, such as frogs, fish, and cattails, that are adapted to living in fresh water.',
   [('A freshwater habitat contains water with ___.', ['Very low levels of salt', 'Very high levels of salt', 'X unrelated to freshwater habitats', 'No water at all'], 0),
    ('Which of these is an example of a freshwater habitat?', ['A pond', 'An ocean', 'X unrelated to freshwater habitats', 'A salt marsh'], 0),
    ('Which plant commonly grows along the edges of ponds and marshes?', ['Cattails', 'Cactus', 'X unrelated to freshwater plants', 'Seaweed'], 0),
    ('Rivers differ from lakes and ponds mainly because river water ___.', ['Flows continuously in one direction', 'Never moves at all', 'X unrelated to comparing freshwater habitats', 'Is always frozen solid'], 0),
    ('Why are freshwater habitats important to many communities?', ['They provide drinking water and support diverse plants and animals', 'Freshwater habitats provide no benefit to communities', 'X unrelated to freshwater habitats', 'Only ocean habitats support living things'], 0)]),
SS('Ancient Persia',
   'Grade 4 Social Studies strand: the ancient Persian Empire, centred in what is now Iran, grew to become one of the largest empires in the ancient world, known for its royal roads, diverse cultures, and organized system of governing distant provinces.',
   [('The ancient Persian Empire was centred in the region that is now known as ___.', ['Iran', 'Central America', 'X unrelated to Persia', 'Northern Europe'], 0),
    ('The Persian Empire became known for building an extensive network of ___.', ['Roads connecting distant parts of the empire', 'Underwater tunnels', 'X unrelated to Persian achievements', 'Modern highways'], 0),
    ('To govern such a large empire, Persian rulers divided their land into ___.', ['Provinces, each managed by an appointed governor', 'A single small village', 'X unrelated to Persian government', 'Independent countries with no ruler'], 0),
    ('The Persian Empire is remembered for allowing conquered peoples to ___.', ['Keep many of their own customs and beliefs', 'Speak only the Persian language', 'X unrelated to Persian rule', 'Live with no laws at all'], 0),
    ('Why do historians consider ancient Persia to be one of the largest empires of the ancient world?', ['It controlled a vast amount of land and many diverse peoples', 'Persia never expanded beyond a single city', 'X unrelated to studying ancient Persia', 'Ancient Persia had no organized government'], 0)])]),
day(72, [
L('Figurative Language: Onomatopoeia',
  'Grade 4 Language strand: onomatopoeia is a word that imitates the sound it describes, such as buzz, crash, or sizzle.',
  [('Onomatopoeia is a word that ___.', ['Imitates the sound it describes', 'Always rhymes with another word', 'X unrelated to onomatopoeia', 'Has the opposite meaning of another word'], 0),
   ('Which word is an example of onomatopoeia?', ['Buzz', 'Table', 'X unrelated to onomatopoeia', 'Happy'], 0),
   ('Which word is an example of onomatopoeia?', ['Sizzle', 'Chair', 'X unrelated to onomatopoeia', 'Quickly'], 0),
   ('Why might an author use onomatopoeia in a story?', ['To help readers imagine the sounds happening in the scene', 'Onomatopoeia has no effect on how a reader imagines a scene', 'X unrelated to figurative language', 'To make a sentence longer with no other purpose'], 0),
   ('Which sentence uses onomatopoeia?', ['The bacon sizzled loudly in the pan', 'The bacon cooked in the pan', 'X unrelated to onomatopoeia', 'The pan was on the stove'], 0)]),
M('Multiplication Strategies: The Distributive Property',
  'Grade 4 Math strand: the distributive property is a multiplication strategy that breaks one factor into smaller parts, multiplies each part separately, and then adds the results together, such as 6 x 14 = (6 x 10) + (6 x 4).',
  [('The distributive property breaks a factor into ___ before multiplying.', ['Smaller parts', 'Negative numbers', 'X unrelated to the distributive property', 'Larger, more complicated numbers'], 0),
   ('Using the distributive property, 6 x 14 can be broken into ___.', ['(6 x 10) + (6 x 4)', '(6 x 10) - (6 x 4)', 'X unrelated to this calculation', '(6 + 10) x (6 + 4)'], 0),
   ('What is 7 x 13 using the distributive property: (7 x 10) + (7 x 3)?', ['91', '81', 'X unrelated to the calculation', '101'], 0),
   ('What is 5 x 24 using the distributive property: (5 x 20) + (5 x 4)?', ['120', '110', 'X unrelated to the calculation', '130'], 0),
   ('Why is the distributive property a useful multiplication strategy?', ['It breaks a hard multiplication problem into smaller, simpler steps', 'It makes multiplication problems impossible to solve', 'X unrelated to multiplication strategies', 'It only works for adding two numbers together'], 0)]),
Sc('Animal Behaviours: Migration and Hibernation',
   'Grade 4 Science strand: some animals survive seasonal changes through migration, travelling long distances to a different climate, while others survive through hibernation, a long period of deep rest during which their body slows down.',
   [('Migration is best described as an animal ___.', ['Travelling long distances to reach a different climate', 'Sleeping through the entire winter without moving', 'X unrelated to migration', 'Changing colour to match its surroundings'], 0),
    ('Hibernation is best described as a long period during which an animal’s body ___.', ['Slows down and enters a deep, resting state', 'Moves faster than usual', 'X unrelated to hibernation', 'Grows a completely new set of fur'], 0),
    ('Which of these animals is well known for migrating long distances each year?', ['The Canada goose', 'A garden snail', 'X unrelated to migration', 'A pet goldfish'], 0),
    ('Which of these animals is well known for hibernating through the winter?', ['The black bear', 'The Canada goose', 'X unrelated to hibernation', 'A migrating whale'], 0),
    ('Why might migration and hibernation both help animals survive cold winters?', ['They help animals avoid harsh conditions or a shortage of food', 'These behaviours make survival more difficult for animals', 'X unrelated to animal survival strategies', 'All animals behave the exact same way in winter'], 0)]),
SS('The Vikings: Explorers and Traders',
   'Grade 4 Social Studies strand: the Vikings were seafaring people from Scandinavia who, between about 800 and 1050 CE, explored, traded, and settled across parts of Europe and even reached North America in their longships.',
   [('The Vikings originally came from the region known today as ___.', ['Scandinavia', 'Central America', 'X unrelated to the Vikings', 'Southern Africa'], 0),
    ('Vikings travelled across the seas using long, narrow boats known as ___.', ['Longships', 'Submarines', 'X unrelated to Viking travel', 'Steamships'], 0),
    ('Besides raiding, Vikings were also skilled ___.', ['Traders who exchanged goods across long distances', 'Astronauts who explored space', 'X unrelated to Viking activities', 'Builders of ancient pyramids'], 0),
    ('Evidence suggests Vikings reached which part of North America long before other Europeans?', ['A settlement in what is now Newfoundland', 'A settlement in what is now Mexico', 'X unrelated to Viking exploration', 'A settlement in what is now Hawaii'], 0),
    ('Why are the Vikings remembered as skilled sailors?', ['They travelled vast distances across open ocean using their longships', 'Vikings never travelled far from home', 'X unrelated to Viking sailing skills', 'Vikings avoided water travel completely'], 0)])]),
day(73, [
L('Grammar: Compound and Complex Sentences',
  'Grade 4 Language strand: a compound sentence joins two complete sentences with a joining word, such as and or but, while a complex sentence joins a complete sentence with an incomplete idea using a word such as because or although.',
  [('A compound sentence joins two complete sentences using a ___.', ['Joining word, such as and or but', 'Silent letter', 'X unrelated to compound sentences', 'Question mark only'], 0),
   ('Which sentence is a compound sentence?', ['I finished my homework, and I played outside', 'I finished my homework quickly', 'X unrelated to compound sentences', 'I like homework'], 0),
   ('A complex sentence joins a complete sentence with an incomplete idea using a word such as ___.', ['Because or although', 'And or but', 'X unrelated to complex sentences', 'Wow or ouch'], 0),
   ('Which sentence is a complex sentence?', ['Because it was raining, we stayed inside', 'We stayed inside and read books', 'X unrelated to complex sentences', 'We stayed inside'], 0),
   ('Why might a writer combine short sentences into compound or complex sentences?', ['To show how ideas connect and to make writing flow more smoothly', 'Combining sentences always confuses the reader', 'X unrelated to sentence combining', 'Short sentences can never be combined'], 0)]),
M('Long Division: Dividing 3-Digit Numbers by a 1-Digit Divisor',
  'Grade 4 Math strand: dividing a 3-digit number by a 1-digit divisor uses the same long division steps as smaller problems -- divide, multiply, subtract, and bring down -- one digit at a time from left to right.',
  [('When dividing a 3-digit number by a 1-digit divisor, you work through the digits from ___.', ['Left to right, one digit at a time', 'Right to left, all at once', 'X unrelated to long division', 'The middle digit outward'], 0),
   ('What is 936 divided by 3?', ['312', '322', 'X unrelated to the calculation', '302'], 0),
   ('What is 848 divided by 4?', ['212', '202', 'X unrelated to the calculation', '222'], 0),
   ('What is 639 divided by 3?', ['213', '203', 'X unrelated to the calculation', '223'], 0),
   ('Why is it helpful to divide, multiply, subtract, and bring down one step at a time?', ['It breaks a large division problem into smaller, more manageable steps', 'It makes the division problem impossible to complete', 'X unrelated to long division steps', 'It changes the value of the original number being divided'], 0)]),
Sc('Fossils: Clues to Earth’s Past',
   'Grade 4 Science strand: a fossil is the preserved remains or trace of a plant or animal that lived long ago, and studying fossils helps scientists learn what life on Earth was like millions of years ago.',
   [('A fossil is best described as the preserved ___ of a living thing from long ago.', ['Remains or trace', 'Modern-day photograph', 'X unrelated to fossils', 'Recorded voice'], 0),
    ('Fossils are most commonly found in which type of rock?', ['Sedimentary rock', 'Igneous rock formed from lava', 'X unrelated to where fossils form', 'Freshly poured concrete'], 0),
    ('Which of these could be preserved as a fossil?', ['A dinosaur’s footprint pressed into mud', 'A cloud passing overhead', 'X unrelated to fossils', 'A sound made yesterday'], 0),
    ('Why do scientists study fossils?', ['To learn what plants, animals, and environments were like long ago', 'Fossils provide no information about the past', 'X unrelated to studying fossils', 'Fossils only reveal information about modern life'], 0),
    ('About how long can it take for a fossil to form?', ['Thousands to millions of years', 'A single day', 'X unrelated to fossil formation', 'A few minutes'], 0)]),
SS('Early Societies: Farming and Food Production',
   'Grade 4 Social Studies strand: early societies developed farming methods, such as planting crops and raising animals, that allowed them to produce a reliable food supply and settle in permanent communities.',
   [('Farming allowed early societies to produce a more reliable ___.', ['Food supply', 'Amount of rainfall', 'X unrelated to early farming', 'Number of holidays'], 0),
    ('Before farming, many early people found food mainly by ___.', ['Hunting animals and gathering wild plants', 'Growing crops in large fields', 'X unrelated to early food gathering', 'Shopping at a market'], 0),
    ('How did farming change where early people chose to live?', ['It allowed them to settle in permanent communities near their fields', 'It forced people to move constantly with no fixed home', 'X unrelated to early settlement patterns', 'Farming had no effect on where people lived'], 0),
    ('Which of these is an example of an early farming activity?', ['Raising animals such as goats or cattle', 'Building a modern factory', 'X unrelated to early farming', 'Sending an email'], 0),
    ('Why is the development of farming considered such an important change in early societies?', ['It allowed populations to grow and communities to become more settled', 'Farming made it harder for communities to find food', 'X unrelated to the importance of early farming', 'Farming had no impact on how societies developed'], 0)])]),
day(74, [
L('Reading: Character Traits and Motivation',
  'Grade 4 Language strand: a character trait describes what a character is like, such as brave or curious, while motivation explains the reasons behind a character’s actions in a story.',
  [('A character trait describes ___.', ['What a character is like', 'Where a story takes place', 'X unrelated to character traits', 'The number of pages in a book'], 0),
   ('A character’s motivation explains ___.', ['The reasons behind a character’s actions', 'The colour of a character’s clothing', 'X unrelated to motivation', 'The title of the book'], 0),
   ('If a character shares their lunch with a hungry classmate, this shows the trait of ___.', ['Kindness', 'Laziness', 'X unrelated to this character trait', 'Dishonesty'], 0),
   ('Why might a character in a story act bravely even when they are afraid?', ['Their motivation, such as protecting a friend, drives them to act despite fear', 'Characters never have reasons for their actions', 'X unrelated to character motivation', 'Fear always stops a character from acting'], 0),
   ('How can a reader figure out a character’s traits?', ['By paying attention to what the character says, does, and thinks', 'By only reading the book’s title', 'X unrelated to identifying character traits', 'By ignoring the character’s actions completely'], 0)]),
M('Fraction of a Set (Finding a Fractional Part of a Whole Number)',
  'Grade 4 Math strand: finding a fraction of a set means dividing a group of objects into equal parts and taking a certain number of those parts, such as finding 1/4 of 12 by dividing 12 into 4 equal groups.',
  [('To find a fraction of a set, you first divide the set into ___.', ['Equal parts based on the denominator', 'Random, uneven parts', 'X unrelated to finding a fraction of a set', 'Exactly two parts every time'], 0),
   ('What is 1/4 of 12?', ['3', '4', 'X unrelated to the calculation', '6'], 0),
   ('What is 1/3 of 15?', ['5', '3', 'X unrelated to the calculation', '45'], 0),
   ('What is 2/5 of 20?', ['8', '10', 'X unrelated to the calculation', '4'], 0),
   ('Why is it helpful to know how to find a fraction of a set?', ['It helps solve real-world problems, such as sharing a group of items equally', 'Finding a fraction of a set is never useful in real life', 'X unrelated to fractions of a set', 'Fractions can only describe parts of a single whole object'], 0)]),
Sc('Simple Machines: Mechanical Advantage',
   'Grade 4 Science strand: mechanical advantage is the benefit a simple machine provides by making a task require less effort force, even though the distance or direction of the force may change.',
   [('Mechanical advantage refers to how a simple machine ___.', ['Makes a task require less effort force', 'Always makes a task take longer to complete', 'X unrelated to mechanical advantage', 'Removes the need for any force at all'], 0),
    ('Using a lever to lift a heavy rock is easier because the lever ___.', ['Provides mechanical advantage by reducing the effort needed', 'Makes the rock lighter in actual weight', 'X unrelated to how levers work', 'Has no effect on the force required'], 0),
    ('A ramp provides mechanical advantage by allowing a heavy object to be moved ___.', ['Using less effort over a longer distance', 'With more effort over a shorter distance', 'X unrelated to how ramps work', 'Without any force at all'], 0),
    ('Why might a longer lever arm provide a greater mechanical advantage?', ['It further reduces the amount of effort force needed to lift a load', 'A longer lever arm always makes lifting an object harder', 'X unrelated to lever length', 'Lever length has no effect on mechanical advantage'], 0),
    ('Why do engineers consider mechanical advantage when designing tools and machines?', ['It helps them design tools that make tasks easier to complete', 'Mechanical advantage has no role in designing tools', 'X unrelated to engineering design', 'Machines are always designed to make tasks harder'], 0)]),
SS('The Great Lakes: Geography and Importance to Canada',
   'Grade 4 Social Studies strand: the Great Lakes are a group of five large freshwater lakes along the border between Canada and the United States, important for transportation, drinking water, and trade.',
   [('The Great Lakes are located along the border between Canada and ___.', ['The United States', 'Mexico', 'X unrelated to the Great Lakes', 'France'], 0),
    ('How many lakes make up the Great Lakes?', ['Five', 'Two', 'X unrelated to the Great Lakes', 'Ten'], 0),
    ('The Great Lakes contain ___.', ['Fresh water', 'Salt water', 'X unrelated to the Great Lakes', 'No water at all'], 0),
    ('Why are the Great Lakes important for trade in Canada?', ['Ships can transport goods across the lakes to different communities', 'The Great Lakes have no connection to trade', 'X unrelated to the importance of the Great Lakes', 'No ships are able to travel on the Great Lakes'], 0),
    ('Besides transportation and trade, the Great Lakes also provide many communities with ___.', ['Drinking water', 'Volcanic rock', 'X unrelated to the Great Lakes', 'Ocean tides'], 0)])]),
day(75, [
L('Writing: Opinion Writing with Reasons and Evidence',
  'Grade 4 Language strand: opinion writing states a clear position on a topic and supports it with reasons and evidence, helping to convince the reader that the opinion is well thought out.',
  [('Opinion writing begins by clearly stating a writer’s ___.', ['Position on a topic', 'Favourite colour only', 'X unrelated to opinion writing', 'List of unrelated facts'], 0),
   ('A strong opinion piece supports its position with ___.', ['Reasons and evidence', 'Random, unrelated sentences', 'X unrelated to supporting an opinion', 'No explanation at all'], 0),
   ('Which sentence is an example of an opinion?', ['Recess should be longer because students need more time to be active', 'The school day starts at nine o’clock', 'X unrelated to opinion writing', 'The classroom has twenty desks'], 0),
   ('Why should a writer include evidence when writing an opinion piece?', ['Evidence helps convince readers that the opinion is well supported', 'Evidence has no effect on convincing a reader', 'X unrelated to opinion writing', 'Opinions never need any support'], 0),
   ('Which is the best way to conclude an opinion piece?', ['Restating the opinion and summarizing the strongest reasons', 'Introducing a brand new, unrelated topic', 'X unrelated to concluding opinion writing', 'Ending in the middle of an unfinished idea'], 0)]),
M('Geometry: Nets of 3D Figures',
  'Grade 4 Math strand: a net is a two-dimensional shape that can be folded to form a three-dimensional figure, showing all of the flat faces that make up that solid.',
  [('A net is a two-dimensional shape that can be folded to form a ___.', ['Three-dimensional figure', 'One-dimensional line', 'X unrelated to nets', 'Two-dimensional figure only'], 0),
   ('The net of a cube is made up of ___ identical squares.', ['Six', 'Four', 'X unrelated to a cube’s net', 'Eight'], 0),
   ('Which 3D figure is formed by folding a net made of two triangles and three rectangles connected correctly?', ['A triangular prism', 'A cube', 'X unrelated to this net', 'A sphere'], 0),
   ('Why do the faces shown in a net need to match the faces of the solid figure exactly?', ['So the net can be folded to correctly form that specific 3D figure', 'The shape of the faces has no effect on the folded figure', 'X unrelated to how nets work', 'A net never needs to match its 3D figure'], 0),
   ('Why might a net be a useful tool for understanding 3D figures?', ['It shows all the flat faces of a solid figure in one flattened view', 'Nets provide no information about a 3D figure’s faces', 'X unrelated to using nets', 'A net can only represent a 2D shape with no connection to 3D figures'], 0)]),
Sc('Light: How Shadows Are Formed',
   'Grade 4 Science strand: a shadow forms when an opaque object blocks the path of light, creating a dark area where the light cannot reach.',
   [('A shadow forms when an opaque object ___.', ['Blocks the path of light', 'Produces its own light', 'X unrelated to shadows', 'Bends light around itself'], 0),
    ('An opaque object is one that light ___.', ['Cannot pass through at all', 'Passes through completely', 'X unrelated to opaque objects', 'Only partly passes through'], 0),
    ('What happens to the size of a shadow as a light source moves closer to an object?', ['The shadow generally becomes larger', 'The shadow disappears completely', 'X unrelated to how shadows change size', 'The shadow always stays exactly the same size'], 0),
    ('Why can you not see a shadow in a completely dark room?', ['There is no light source to be blocked by an object', 'Shadows only form in rooms with no light at all', 'X unrelated to how shadows form', 'Darkness always creates its own shadow'], 0),
    ('Why do shadows change position throughout the day outdoors?', ['The position of the Sun in the sky changes throughout the day', 'Shadows never change position during the day', 'X unrelated to how outdoor shadows change', 'The ground moves underneath the shadow'], 0)]),
SS('Canada’s Political Map: Capital Cities and Their Roles',
   'Grade 4 Social Studies strand: each Canadian province and territory has a capital city, where the provincial or territorial government meets and makes important decisions, and Ottawa serves as the capital of Canada as a whole.',
   [('The capital city of a province is where its ___.', ['Government meets and makes important decisions', 'Professional sports teams always play', 'X unrelated to capital cities', 'Tallest mountain is located'], 0),
    ('Which city is the capital of Canada?', ['Ottawa', 'Toronto', 'X unrelated to Canada’s capital', 'Vancouver'], 0),
    ('Which city is the capital of Ontario?', ['Toronto', 'Ottawa', 'X unrelated to Ontario’s capital', 'Montreal'], 0),
    ('Why does every province and territory have its own capital city?', ['Each has its own government that needs a central place to meet and govern', 'Capital cities serve no purpose for a province', 'X unrelated to why provinces have capitals', 'Only the federal government is allowed to make decisions'], 0),
    ('How is Canada’s capital city different from a provincial capital?', ['Canada’s capital is where the federal government meets to govern the whole country', 'Canada’s capital has no connection to government at all', 'X unrelated to comparing capital cities', 'A provincial capital governs the entire country'], 0)])]),
day(76, [
L('Spelling: Contractions and Apostrophes',
  'Grade 4 Language strand: a contraction combines two words into one shorter word, using an apostrophe to show where letters have been left out, such as do not becoming don’t.',
  [('A contraction combines two words into ___.', ['One shorter word, using an apostrophe', 'Two completely new, unrelated words', 'X unrelated to contractions', 'A single letter'], 0),
   ('In a contraction, the apostrophe shows where ___.', ['Letters have been left out', 'A new sentence begins', 'X unrelated to apostrophes in contractions', 'A word has been repeated'], 0),
   ('What is the contraction for do not?', ['Don’t', 'Doesn’t', 'X unrelated to this contraction', 'Didn’t'], 0),
   ('What is the contraction for they are?', ['They’re', 'Their', 'X unrelated to this contraction', 'There'], 0),
   ('Why might a writer use contractions in a story’s dialogue?', ['To make characters sound more natural, the way people actually speak', 'Contractions make dialogue sound less natural', 'X unrelated to using contractions', 'Contractions are never used in spoken language'], 0)]),
M('Data: Double Bar Graphs',
  'Grade 4 Math strand: a double bar graph compares two related sets of data side by side using pairs of bars, making it easy to see differences between the two groups.',
  [('A double bar graph compares ___ sets of related data.', ['Two', 'Four', 'X unrelated to double bar graphs', 'Zero'], 0),
   ('In a double bar graph, each category is represented by ___.', ['A pair of bars, side by side', 'A single, isolated dot', 'X unrelated to double bar graphs', 'A single pie-shaped slice'], 0),
   ('A double bar graph would be most useful for comparing ___.', ['This year’s and last year’s rainfall totals for each month', 'A single number with no comparison', 'X unrelated to using a double bar graph', 'Only one category with no comparison group'], 0),
   ('Why is a legend often included with a double bar graph?', ['It shows which colour or pattern represents each of the two data sets', 'A legend has no purpose on a double bar graph', 'X unrelated to reading double bar graphs', 'A legend always replaces the need for bars'], 0),
   ('Why might a double bar graph be more useful than a single bar graph for comparing two classes’ test scores?', ['It lets you see both classes’ data side by side for easy comparison', 'A double bar graph can only show one class’s data', 'X unrelated to comparing data with graphs', 'Single bar graphs always show more information'], 0)]),
Sc('Weathering: How Rocks Break Down Over Time',
   'Grade 4 Science strand: weathering is the process by which wind, water, ice, and changes in temperature slowly break rocks down into smaller pieces without moving them from their original location.',
   [('Weathering is the process of rocks being ___.', ['Broken down into smaller pieces over time', 'Instantly transformed into soil', 'X unrelated to weathering', 'Formed deep underground from magma'], 0),
    ('Which of these can cause weathering?', ['Repeated freezing and thawing of water in cracks', 'A rock sitting in complete darkness', 'X unrelated to causes of weathering', 'A rock being weighed on a scale'], 0),
    ('How is weathering different from erosion?', ['Weathering breaks rock down in place, while erosion moves the broken pieces elsewhere', 'Weathering and erosion always mean exactly the same thing', 'X unrelated to comparing weathering and erosion', 'Erosion breaks rock down while weathering moves it'], 0),
    ('Why might a rock exposed to wind and rain break apart faster than a rock kept sheltered indoors?', ['Wind and rain speed up the process of weathering', 'Wind and rain have no effect on rocks', 'X unrelated to weathering conditions', 'Sheltered rocks weather more quickly than exposed rocks'], 0),
    ('Why is weathering an important process to study in earth science?', ['It helps explain how landscapes and landforms slowly change over time', 'Weathering has no effect on Earth’s landscapes', 'X unrelated to studying weathering', 'Rocks never change once they are formed'], 0)]),
SS('Exploring Life in Canada’s Arctic Communities',
   'Grade 4 Social Studies strand: communities in Canada’s Arctic, home to many Inuit peoples, have adapted to a cold climate, long winters, and remote locations, developing unique ways of travelling, hunting, and staying connected.',
   [('Canada’s Arctic region is home to many communities of ___ peoples.', ['Inuit', 'Only recent immigrants', 'X unrelated to Arctic communities', 'Ancient Roman'], 0),
    ('Communities in the Arctic have adapted to a climate that is ___.', ['Cold, with long winters', 'Warm and tropical all year', 'X unrelated to the Arctic climate', 'Rainy with no snow at all'], 0),
    ('Because many Arctic communities are remote, transportation often relies on ___.', ['Planes and snowmobiles', 'Subway trains', 'X unrelated to Arctic transportation', 'City buses only'], 0),
    ('Traditional Inuit knowledge and skills, such as hunting and travelling on ice, have been passed down through ___.', ['Generations of families and communities', 'Written textbooks only', 'X unrelated to passing down traditional knowledge', 'A single individual with no connection to others'], 0),
    ('Why is it important to learn about life in Canada’s Arctic communities?', ['It shows how people adapt and thrive in one of Canada’s most challenging climates', 'Arctic communities have no connection to the rest of Canada', 'X unrelated to learning about Arctic life', 'No one has ever lived in Canada’s Arctic region'], 0)])]),
day(77, [
L('Grammar: Adjective Order',
  'Grade 4 Language strand: when a sentence uses more than one adjective before a noun, the adjectives usually follow a typical order, such as opinion, size, and colour, as in a beautiful, small, red bird.',
  [('When more than one adjective describes a noun, the adjectives usually follow a typical ___.', ['Order', 'Rhyme scheme', 'X unrelated to adjective order', 'Number of syllables'], 0),
   ('Which sentence follows the typical order for adjectives?', ['She wore a beautiful, small, red hat', 'She wore a red, small, beautiful hat', 'X unrelated to adjective order', 'She wore a hat beautiful, small, red'], 0),
   ('In the phrase a large, old, wooden table, which category comes first?', ['Size', 'Material', 'X unrelated to this phrase’s adjective order', 'Age'], 0),
   ('Why might a sentence sound unusual if adjectives are placed in the wrong order?', ['English speakers are used to hearing adjectives follow a familiar pattern', 'Adjective order never affects how a sentence sounds', 'X unrelated to adjective order', 'Every possible order sounds exactly the same'], 0),
   ('Which phrase correctly places an opinion adjective before a colour adjective?', ['A lovely blue bicycle', 'A blue lovely bicycle', 'X unrelated to this phrase’s adjective order', 'A bicycle lovely blue'], 0)]),
M('Converting Between Metric Units of Length',
  'Grade 4 Math strand: converting between metric units of length involves multiplying or dividing by powers of ten, such as changing between millimetres, centimetres, metres, and kilometres.',
  [('Converting between metric units of length involves multiplying or dividing by ___.', ['Powers of ten', 'Random, unrelated numbers', 'X unrelated to metric conversions', 'Only the number one'], 0),
   ('How many centimetres are in 1 metre?', ['100 centimetres', '10 centimetres', 'X unrelated to this conversion', '1,000 centimetres'], 0),
   ('How many metres are in 1 kilometre?', ['1,000 metres', '100 metres', 'X unrelated to this conversion', '10 metres'], 0),
   ('How many millimetres are in 5 centimetres?', ['50 millimetres', '5 millimetres', 'X unrelated to this conversion', '500 millimetres'], 0),
   ('Why is it useful to convert between metric units of length?', ['It allows you to choose the most appropriate unit for measuring something', 'Metric units can never be converted from one to another', 'X unrelated to converting metric units', 'Every metric unit always measures the exact same distance'], 0)]),
Sc('Pollination and the Role of Insects in Ecosystems',
   'Grade 4 Science strand: pollination occurs when pollen is carried from one flower to another, often by insects such as bees and butterflies, allowing many plants to produce seeds and fruit.',
   [('Pollination occurs when pollen is carried ___.', ['From one flower to another', 'Deep underground into the soil', 'X unrelated to pollination', 'Directly into the air with no destination'], 0),
    ('Which insect is especially well known for pollinating flowers?', ['The bee', 'The housefly', 'X unrelated to pollination', 'The ant'], 0),
    ('Pollination allows many plants to produce ___.', ['Seeds and fruit', 'More sunlight', 'X unrelated to pollination', 'Additional roots only'], 0),
    ('Why are pollinators, such as bees, important to ecosystems and food production?', ['Many plants, including food crops, rely on pollinators to reproduce', 'Pollinators have no effect on plant reproduction', 'X unrelated to the importance of pollinators', 'Plants never need help reproducing'], 0),
    ('What might happen to a plant if pollinating insects disappeared from its ecosystem?', ['The plant could struggle to produce seeds and fruit', 'The plant would be completely unaffected', 'X unrelated to the effects of losing pollinators', 'The plant would immediately grow larger'], 0)]),
SS('Canada’s Transportation Networks: Connecting Communities',
   'Grade 4 Social Studies strand: Canada relies on transportation networks, including roads, railways, airports, and shipping routes, to connect communities, move goods, and support trade across a vast country.',
   [('Transportation networks help connect communities by allowing people and goods to ___.', ['Move between different places', 'Remain in exactly one location forever', 'X unrelated to transportation networks', 'Disappear from a community entirely'], 0),
    ('Which of these is an example of a transportation network in Canada?', ['A railway system', 'A single garden path', 'X unrelated to transportation networks', 'A backyard fence'], 0),
    ('Why are transportation networks especially important in a large country like Canada?', ['They connect communities that may be very far apart from one another', 'Every Canadian community is located right next to every other one', 'X unrelated to Canada’s transportation needs', 'Transportation has no importance in a large country'], 0),
    ('Which transportation method would most likely be used to move goods long distances between remote northern communities?', ['An airplane', 'A city subway', 'X unrelated to northern transportation', 'A bicycle'], 0),
    ('How do transportation networks support trade within Canada?', ['They allow goods to be moved efficiently between producers and consumers', 'Transportation networks have no connection to trade', 'X unrelated to supporting trade', 'Goods can only be sold in the community where they are made'], 0)])]),
day(78, [
L('Reading: Setting and Mood',
  'Grade 4 Language strand: the setting of a story is when and where it takes place, and details about the setting often help create the story’s mood, or the overall feeling it gives the reader.',
  [('The setting of a story refers to ___.', ['When and where the story takes place', 'The main character’s personality', 'X unrelated to setting', 'The number of chapters in a book'], 0),
   ('The mood of a story is best described as ___.', ['The overall feeling the story gives the reader', 'The exact number of pages in the book', 'X unrelated to mood', 'A list of every character’s name'], 0),
   ('A story set in a dark, abandoned house on a stormy night likely creates a mood of ___.', ['Suspense or fear', 'Cheerful excitement', 'X unrelated to this story’s mood', 'Calm relaxation'], 0),
   ('How might a sunny beach setting affect the mood of a story?', ['It could help create a relaxed or cheerful mood', 'A sunny beach always creates a frightening mood', 'X unrelated to how setting affects mood', 'Setting never has any effect on mood'], 0),
   ('Why do authors carefully choose details about setting?', ['Setting details can help shape the mood and feeling of a story', 'Setting details have no connection to a story’s mood', 'X unrelated to choosing setting details', 'Every setting creates the exact same mood'], 0)]),
M('Congruent Shapes and Sizes',
  'Grade 4 Math strand: two shapes are congruent when they have exactly the same size and shape, even if one has been turned, flipped, or moved to a different position.',
  [('Two shapes are congruent when they have exactly the same ___.', ['Size and shape', 'Colour only', 'X unrelated to congruent shapes', 'Number of sides only, regardless of size'], 0),
   ('If one triangle is flipped and moved but is still the exact same size and shape as another, the two triangles are ___.', ['Congruent', 'Never related to one another', 'X unrelated to congruent shapes', 'Always different shapes entirely'], 0),
   ('Which of these pairs of shapes would be considered congruent?', ['Two identical squares, each with 4 cm sides', 'A small square and a large square', 'X unrelated to congruent shapes', 'A triangle and a circle'], 0),
   ('Does rotating a shape change whether it is congruent to its original form?', ['No, rotating a shape does not change its size or shape', 'Yes, rotating a shape always makes it larger', 'X unrelated to rotating congruent shapes', 'Yes, rotating a shape always changes its number of sides'], 0),
   ('Why is understanding congruence useful in geometry?', ['It helps identify when shapes are truly identical in size and shape', 'Congruence has no useful purpose in geometry', 'X unrelated to congruent shapes', 'Every shape is automatically congruent to every other shape'], 0)]),
Sc('Renewable Energy: Solar, Wind, and Hydro Power',
   'Grade 4 Science strand: renewable energy sources, such as solar, wind, and hydro power, use natural resources that are continually replenished to generate electricity without running out.',
   [('Renewable energy sources are ones that ___.', ['Are continually replenished by nature', 'Run out permanently after a single use', 'X unrelated to renewable energy', 'Can never be used to generate electricity'], 0),
    ('Solar power generates electricity using energy from the ___.', ['Sun', 'Ocean tides only', 'X unrelated to solar power', 'Underground coal deposits'], 0),
    ('Wind power uses turbines that are turned by ___.', ['Moving air', 'Flowing water', 'X unrelated to wind power', 'Burning fuel'], 0),
    ('Hydro power generates electricity using the energy of ___.', ['Moving or falling water', 'Sunlight only', 'X unrelated to hydro power', 'Burning wood'], 0),
    ('Why are solar, wind, and hydro power considered better for the environment than burning fossil fuels?', ['They produce electricity without releasing the pollution fossil fuels create', 'These renewable sources always create more pollution than fossil fuels', 'X unrelated to comparing energy sources', 'Renewable energy sources cannot generate electricity at all'], 0)]),
SS('The Role of Rivers in the Growth of Early Civilizations',
   'Grade 4 Social Studies strand: many early civilizations, such as those along the Nile, Tigris-Euphrates, Indus, and Yellow rivers, developed near rivers because the water supported farming, transportation, and trade.',
   [('Many early civilizations developed near rivers mainly because rivers provided ___.', ['Water for farming, drinking, and transportation', 'No useful resources at all', 'X unrelated to why civilizations settled near rivers', 'A barrier that prevented any settlement'], 0),
    ('Ancient Egypt developed along which river?', ['The Nile River', 'The Yellow River', 'X unrelated to Ancient Egypt’s location', 'The Amazon River'], 0),
    ('Ancient Mesopotamia developed between which two rivers?', ['The Tigris and Euphrates rivers', 'The Nile and Amazon rivers', 'X unrelated to Mesopotamia’s location', 'The Mississippi and Missouri rivers'], 0),
    ('How did rivers support trade in early civilizations?', ['Boats could carry goods and people along the river between communities', 'Rivers made it impossible for goods to be transported', 'X unrelated to rivers and trade', 'Trade never happened near rivers'], 0),
    ('Why might farmland near a river be especially fertile?', ['Flooding rivers often deposit nutrient-rich soil along their banks', 'Rivers remove all nutrients from nearby soil', 'X unrelated to fertile farmland near rivers', 'Land near rivers is always too dry for farming'], 0)])]),
day(79, [
L('Media Literacy: Comparing Print, Digital, and Video Media',
  'Grade 4 Language strand: information can be shared through different media forms, such as print, digital text, and video, and each form has its own strengths for informing or entertaining an audience.',
  [('Print, digital, and video are all examples of different ___.', ['Forms of media', 'Types of punctuation', 'X unrelated to media literacy', 'Genres of poetry only'], 0),
   ('Which of these is an example of print media?', ['A newspaper', 'An online video', 'X unrelated to print media', 'A podcast'], 0),
   ('A strength of video media is that it can combine ___.', ['Moving images and sound together', 'Only plain black-and-white text', 'X unrelated to video media', 'Nothing but silence'], 0),
   ('Why might someone choose to read a digital article instead of a printed one?', ['Digital articles can often be accessed instantly and updated easily', 'Digital articles can never be updated once published', 'X unrelated to comparing print and digital media', 'Printed articles are always the fastest way to get new information'], 0),
   ('Why is it useful to understand the differences between media forms?', ['It helps you choose or evaluate the best source for a specific purpose', 'Every media form works exactly the same way', 'X unrelated to comparing media forms', 'Understanding media forms serves no useful purpose'], 0)]),
M('Financial Literacy: Comparing Costs and Estimating Totals While Shopping',
  'Grade 4 Math strand: comparing costs and estimating totals while shopping involves rounding prices to quickly add them up and predict whether a purchase stays within a set budget.',
  [('Estimating a shopping total usually involves ___ prices before adding them.', ['Rounding', 'Ignoring', 'X unrelated to estimating totals', 'Multiplying by zero'], 0),
   ('If items cost 4.85 dollars and 2.10 dollars, which is the best estimate of the total?', ['About 7 dollars', 'About 3 dollars', 'X unrelated to this estimate', 'About 15 dollars'], 0),
   ('Why might a shopper estimate a total before reaching the checkout?', ['To check whether the purchase will stay within their budget', 'Estimating a total is never useful while shopping', 'X unrelated to estimating shopping totals', 'Estimating always gives a completely wrong answer'], 0),
   ('Which strategy would help you compare the cost of two different-sized boxes of cereal?', ['Finding the unit price, or cost per item, for each box', 'Only looking at the total price on each box', 'X unrelated to comparing shopping costs', 'Choosing the box with the biggest picture'], 0),
   ('Why is estimating totals a useful skill even when a calculator is available?', ['It helps quickly check whether a calculated total seems reasonable', 'Estimating serves no purpose when a calculator is available', 'X unrelated to estimating shopping totals', 'A calculator always removes the need to think about numbers'], 0)]),
Sc('Structures: Foundations and Stability',
   'Grade 4 Science strand: a foundation is the base that supports a structure, and a stable structure is designed with a wide, strong base and an even distribution of weight to help it resist tipping or collapsing.',
   [('A foundation is best described as the ___ that supports a structure.', ['Base', 'Roof', 'X unrelated to foundations', 'Topmost floor'], 0),
    ('A structure is more likely to be stable when it has a ___.', ['Wide, strong base', 'Extremely narrow, weak base', 'X unrelated to structural stability', 'No base at all'], 0),
    ('Why might a tall tower with a wide base be more stable than one with a narrow base?', ['A wide base better distributes weight and resists tipping over', 'A narrow base always provides more stability than a wide one', 'X unrelated to comparing structural stability', 'The width of a base has no effect on stability'], 0),
    ('Why do builders dig deep, strong foundations before constructing large buildings?', ['A strong foundation helps support the weight of the building above it', 'Foundations have no effect on how well a building is supported', 'X unrelated to why foundations matter', 'Buildings are always built with no foundation at all'], 0),
    ('Why might engineers test the stability of a structure’s foundation before construction begins?', ['To ensure the structure will be safe and unlikely to collapse or tip', 'Testing a foundation provides no useful information', 'X unrelated to testing structural stability', 'Every foundation is equally stable regardless of design'], 0)]),
SS('Trade Routes of the Ancient World (Silk Road and Beyond)',
   'Grade 4 Social Studies strand: ancient trade routes, such as the Silk Road, connected distant civilizations across Asia, Europe, and Africa, allowing goods, ideas, and cultures to be exchanged over long distances.',
   [('The Silk Road was a network of ancient trade routes connecting ___.', ['Distant civilizations across Asia, Europe, and Africa', 'Only two neighbouring villages', 'X unrelated to the Silk Road', 'Cities located entirely underwater'], 0),
    ('The Silk Road gets its name from a valuable good, ___, that was traded along the route.', ['Silk', 'Plastic', 'X unrelated to the Silk Road’s name', 'Rubber'], 0),
    ('Besides goods, what else spread between civilizations along ancient trade routes?', ['Ideas and cultural practices', 'Nothing besides physical goods', 'X unrelated to ancient trade routes', 'Only modern technology'], 0),
    ('Why were ancient trade routes, such as the Silk Road, important to the civilizations they connected?', ['They allowed distant societies to exchange goods, ideas, and culture', 'Trade routes prevented any contact between civilizations', 'X unrelated to the importance of trade routes', 'Ancient civilizations never exchanged goods with one another'], 0),
    ('Why do historians study ancient trade routes like the Silk Road today?', ['They reveal how ancient civilizations were connected to one another', 'Ancient trade routes provide no useful historical information', 'X unrelated to studying ancient trade routes', 'Ancient civilizations were always completely isolated from each other'], 0)])]),
day(80, [
L('Review: Vocabulary, Grammar, and Reading Skills (Days 71-79)',
  'Grade 4 Language strand: this review lesson revisits key ideas from Days 71-79, including proverbs and adages, onomatopoeia, compound and complex sentences, character traits, and setting and mood.',
  [('A proverb or adage is best described as a short saying that expresses ___.', ['Traditional wisdom or advice', 'A character’s exact name', 'X unrelated to proverbs', 'A story’s complete plot'], 0),
   ('Onomatopoeia is a word that ___.', ['Imitates the sound it describes', 'Always rhymes with another word', 'X unrelated to onomatopoeia', 'Has the opposite meaning of another word'], 0),
   ('A compound sentence joins two complete sentences using a ___.', ['Joining word, such as and or but', 'Silent letter', 'X unrelated to compound sentences', 'Question mark only'], 0),
   ('A character trait describes ___.', ['What a character is like', 'Where a story takes place', 'X unrelated to character traits', 'The number of pages in a book'], 0),
   ('Why is it useful to review vocabulary, grammar, and reading strategies together?', ['It reinforces how these language skills support clear reading and writing', 'These skills have no connection to each other', 'X unrelated to reviewing language arts', 'Reviewing past learning never helps strengthen understanding'], 0)]),
M('Review: Number Sense, Geometry, and Data (Days 71-79)',
  'Grade 4 Math strand: this review lesson revisits key ideas from Days 71-79, including comparing numbers, the distributive property, long division, fractions of a set, and congruent shapes.',
  [('Which symbol means greater than?', ['>', '<', 'X unrelated to comparing numbers', '='], 0),
   ('Using the distributive property, 6 x 14 can be broken into ___.', ['(6 x 10) + (6 x 4)', '(6 x 10) - (6 x 4)', 'X unrelated to this calculation', '(6 + 10) x (6 + 4)'], 0),
   ('What is 936 divided by 3?', ['312', '322', 'X unrelated to the calculation', '302'], 0),
   ('What is 1/4 of 12?', ['3', '4', 'X unrelated to the calculation', '6'], 0),
   ('Why is it useful to review number sense, geometry, and data together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'X unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Habitats, Earth Science, and Structures (Days 71-79)',
   'Grade 4 Science strand: this review lesson revisits key ideas from Days 71-79, including freshwater habitats, migration and hibernation, fossils, shadows, weathering, pollination, renewable energy, and structural stability.',
   [('A freshwater habitat contains water with ___.', ['Very low levels of salt', 'Very high levels of salt', 'X unrelated to freshwater habitats', 'No water at all'], 0),
    ('Migration is best described as an animal ___.', ['Travelling long distances to reach a different climate', 'Sleeping through the entire winter without moving', 'X unrelated to migration', 'Changing colour to match its surroundings'], 0),
    ('A fossil is best described as the preserved ___ of a living thing from long ago.', ['Remains or trace', 'Modern-day photograph', 'X unrelated to fossils', 'Recorded voice'], 0),
    ('A shadow forms when an opaque object ___.', ['Blocks the path of light', 'Produces its own light', 'X unrelated to shadows', 'Bends light around itself'], 0),
    ('Why is it useful to review ecosystems, earth science, and structures together?', ['It reinforces how these science concepts each explain different parts of the natural world', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Early Societies and Canadian Geography (Days 71-79)',
   'Grade 4 Social Studies strand: this review lesson revisits key ideas from Days 71-79, including ancient Persia, the Vikings, early farming, the Great Lakes, capital cities, Arctic communities, transportation networks, rivers, and trade routes.',
   [('The ancient Persian Empire was centred in the region that is now known as ___.', ['Iran', 'Central America', 'X unrelated to Persia', 'Northern Europe'], 0),
    ('Vikings travelled across the seas using long, narrow boats known as ___.', ['Longships', 'Submarines', 'X unrelated to Viking travel', 'Steamships'], 0),
    ('The Great Lakes are located along the border between Canada and ___.', ['The United States', 'Mexico', 'X unrelated to the Great Lakes', 'France'], 0),
    ('Which city is the capital of Canada?', ['Ottawa', 'Toronto', 'X unrelated to Canada’s capital', 'Vancouver'], 0),
    ('Why is it useful to review early societies alongside Canadian geography?', ['It helps compare how different societies and regions have developed over time', 'These topics have no connection to social studies', 'X unrelated to reviewing social studies', 'Early societies and Canadian geography are exactly the same topic'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260902):
    """Same technique used for the earlier Phase 3 batches -- reassigns
    each question's correct-answer slot via a shuffled round-robin (even
    across 0-3) and shuffles the wrong options into the remaining slots.
    Question and option TEXT is never changed. Mutates `days` in place."""
    import random
    rng = random.Random(seed)
    all_quizzes = [quiz for _, subs in days for *_, quiz in subs]
    n = sum(len(quiz) for quiz in all_quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in all_quizzes:
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


if __name__ == '__main__':
    _rebalance_answer_positions(g4_71_80)
    append_to(4, g4_71_80)
