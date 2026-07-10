#!/usr/bin/env python3
"""Phase 3 extension: Grade 3, Days 51-60 (first batch past the Day 50
milestone, pushing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-50 set (see
data/grade3.json): comparing texts, 2-digit multiplication/division,
the rock cycle, simple circuits, local government decisions, and
Canada's national parks.

Subject keys for Grade 3 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 3 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
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


g3_51_60 = [
day(51, [
L('Reading: Comparing Texts on the Same Topic',
  'Grade 3 Language strand: comparing two texts on the same topic means noticing how each one presents information differently, such as using different facts, pictures, or points of view.',
  [('Comparing two texts on the same topic means noticing ___.', ['How each text presents information differently', 'That every text is always exactly the same', 'A skill unrelated to reading comprehension', 'Only the number of pages in each text'], 0),
   ('Which is something you might compare between two texts about the same animal?', ['The facts each text chooses to include', 'The colour of the book cover only', 'A detail unrelated to the topic itself', 'The price of each book'], 0),
   ('Why might two authors write about the same topic in different ways?', ['They may have different purposes, audiences, or opinions about the topic', 'Every author always writes about a topic in exactly the same way', 'Authors never make different choices about what to include', 'This concept has no connection to how texts are written'], 0),
   ('Why is comparing texts a useful reading skill?', ['It helps readers build a fuller, more complete understanding of a topic', 'Comparing texts never adds anything useful to understanding a topic', 'Readers should only ever read a single text about any topic', 'This skill has no connection to understanding a subject well'], 0),
   ('If one text about bees says they are helpful and another says they can be dangerous, what could a reader do?', ['Think about both ideas together to get a fuller picture', 'Assume one of the texts must be completely wrong', 'Ignore both texts entirely', 'Decide the topic is not worth learning about'], 0)]),
M('Introduction to Multiplying 2-Digit Numbers',
  'Grade 3 Math strand: multiplying a 2-digit number by a 1-digit number can be done by breaking the 2-digit number into tens and ones, multiplying each part, and adding the results together.',
  [('To multiply a 2-digit number by a 1-digit number, you can break the 2-digit number into ___.', ['Tens and ones', 'Only hundreds, with no other place value considered', 'A method unrelated to place value', 'Fractions, with no connection to whole numbers'], 0),
   ('What is 23 × 3?', ['69', '63', '66', '73'], 0),
   ('When multiplying 34 × 2, you can first multiply 30 × 2 and then ___.', ['4 × 2, and add the two results', 'Ignore the ones digit entirely', 'Multiply by zero instead', 'Subtract 4 × 2 from the first result'], 0),
   ('Why is breaking a 2-digit number into tens and ones a helpful strategy for multiplication?', ['It turns one harder problem into two easier ones that can be added together', 'This strategy always makes multiplication more difficult', 'Breaking numbers apart has no connection to solving multiplication problems', 'This method only works for numbers less than ten'], 0),
   ('If a classroom has 4 rows of 12 chairs, how many chairs are there in total?', ['48', '44', '52', '16'], 0)]),
Sc('Science: Food Chains and Food Webs',
   'Grade 3 Science strand: a food web shows how multiple food chains connect and overlap within an ecosystem, illustrating that most animals eat and are eaten by more than one other living thing.',
   [('A food web shows how multiple food chains ___.', ['Connect and overlap within an ecosystem', 'Never have any connection to one another', 'A concept unrelated to how animals eat', 'Always form a single, straight line'], 0),
    ('Most animals in an ecosystem eat and are eaten by ___.', ['More than one other living thing', 'Only a single other living thing, with no other connections', 'No other living things at all', 'A concept unrelated to feeding relationships'], 0),
    ('Why might a food web give a more complete picture of an ecosystem than a single food chain?', ['A food web shows the many different feeding connections that exist, not just one simple path', 'A food web always shows less information than a single food chain', 'Food chains and food webs are always exactly identical', 'This concept has no connection to understanding ecosystems'], 0),
    ('If one type of plant in a food web disappeared, why might several different animals be affected?', ['Many different animals could rely on that plant as a food source within the web', 'Removing a plant from an ecosystem never affects any animals', 'Food webs have no connection between different living things', 'Only a single animal could ever be affected by this kind of change'], 0),
    ('Why is understanding food webs important for protecting ecosystems?', ['It helps show how changes to one living thing can ripple out and affect many others', 'Food webs have no connection to protecting the environment', 'Understanding feeding relationships provides no useful information', 'Ecosystems are never affected by changes to any single living thing'], 0)]),
SS('Social Studies: Local Government -- How Decisions Are Made',
   'Grade 3 Social Studies strand: local (municipal) governments make decisions about community services like parks, roads, and libraries, often by discussing options and then voting.',
   [('Local, or municipal, governments make decisions about community services like ___.', ['Parks, roads, and libraries', 'Only decisions that affect other countries', 'A topic unrelated to community services', 'Decisions with no connection to daily community life'], 0),
    ('Local government decisions are often made by discussing options and then ___.', ['Voting', 'Flipping a coin with no discussion involved', 'A method entirely unrelated to decision-making', 'Ignoring all community input completely'], 0),
    ('Why might a local government hold a public meeting before making a decision about a new park?', ['It allows community members to share their opinions and concerns before a final decision is made', 'Public meetings have no connection to how decisions are made', 'Local governments never consider input from the community', 'This process has no relevance to how communities are run'], 0),
    ('Which is an example of a decision a local government might make?', ['Where to build a new playground', 'A decision about another country’s laws', 'A choice entirely unrelated to community services', 'A decision made only by a single individual with no process involved'], 0),
    ('Why is it useful for students to understand how local government decisions are made?', ['It helps them understand how their own community works and how they might participate in it someday', 'This understanding has no connection to being part of a community', 'Local government decisions never affect students or their families', 'This topic has no relevance to social studies learning'], 0)])]),

day(52, [
L('Writing: The How-To Guide',
  'Grade 3 Language strand: a how-to guide gives clear, step-by-step instructions in the correct order, often using numbered steps and precise action words so a reader can successfully complete a task.',
  [('A how-to guide gives instructions in ___.', ['The correct order, step by step', 'A completely random, mixed-up order', 'A style unrelated to giving instructions', 'Only a single step, with no further detail'], 0),
   ('Why might a how-to guide use numbered steps?', ['Numbers help the reader clearly follow the correct order of actions', 'Numbers have no effect on how easy a guide is to follow', 'A how-to guide should never be organized using numbers', 'This concept has no connection to giving clear instructions'], 0),
   ('Which is an example of a precise action word that might appear in a how-to guide?', ['Fold', 'Thing', 'Stuff', 'A word unrelated to any specific action'], 0),
   ('Why is it important for a how-to guide to list steps in the correct order?', ['Skipping or reordering steps could make the instructions confusing or impossible to follow correctly', 'The order of steps never matters when writing instructions', 'A how-to guide is always equally clear no matter what order the steps are in', 'This concept has no connection to writing effective instructions'], 0),
   ('Why might a writer include a list of needed materials at the beginning of a how-to guide?', ['It helps the reader gather everything they need before starting the task', 'A materials list has no useful purpose in this type of writing', 'How-to guides should never mention any needed materials', 'This concept has no connection to helping a reader complete a task'], 0)]),
M('Dividing 2-Digit Numbers by 1-Digit Numbers',
  'Grade 3 Math strand: dividing a 2-digit number by a 1-digit number can be approached by sharing the tens and ones separately, or by thinking about which multiplication fact matches the division problem.',
  [('Dividing a 2-digit number by a 1-digit number can be approached by sharing the ___ separately.', ['Tens and ones', 'Only the ones digit, with no connection to tens', 'A concept unrelated to place value', 'Hundreds, with no connection to the given number'], 0),
   ('What is 48 ÷ 4?', ['12', '10', '14', '16'], 0),
   ('Thinking about which multiplication fact matches a division problem can help because ___.', ['Multiplication and division are related, or inverse, operations', 'Multiplication and division have no connection to each other', 'This strategy never actually helps solve a division problem', 'Division problems can never be solved using multiplication facts'], 0),
   ('If 6 friends share 66 stickers equally, how many stickers does each friend get?', ['11', '10', '12', '6'], 0),
   ('Why might breaking a 2-digit number into tens and ones make a division problem easier to solve?', ['Sharing smaller, more manageable amounts separately can simplify the overall problem', 'Breaking a number apart always makes a division problem more difficult', 'This strategy has no connection to solving division problems', 'Division problems can only ever be solved with the entire number at once'], 0)]),
Sc('Science: The Rock Cycle',
   'Grade 3 Science strand: the rock cycle describes how rocks slowly change from one type to another over long periods of time through processes like heat, pressure, and erosion.',
   [('The rock cycle describes how rocks slowly ___ over long periods of time.', ['Change from one type to another', 'Always remain exactly the same, with no change at all', 'A concept unrelated to how rocks form', 'Disappear completely with no trace remaining'], 0),
    ('Which is a process that can cause rocks to change over time?', ['Heat and pressure', 'A process entirely unrelated to how rocks form', 'Only the passage of a single day', 'A change that has no connection to natural processes'], 0),
    ('Why might a rock that was once at the bottom of a mountain eventually become a different type of rock?', ['Natural processes like heat, pressure, or erosion can slowly transform one rock type into another', 'Rocks are never affected by any natural processes', 'This transformation has no connection to the rock cycle', 'Rocks always remain completely unchanged no matter what happens around them'], 0),
    ('Why is the rock cycle considered a very slow process?', ['These natural changes typically take an extremely long time, often thousands or millions of years', 'The rock cycle always happens within a single day', 'This process has no connection to the passage of time', 'Rocks change instantly with no gradual process involved'], 0),
    ('Why is understanding the rock cycle useful for scientists studying Earth’s history?', ['Rocks can reveal clues about the processes and conditions Earth experienced over a very long time', 'The rock cycle has no connection to understanding Earth’s history', 'Rocks provide no useful scientific information about the past', 'This concept has no relevance to studying our planet'], 0)]),
SS('Social Studies: Community Helpers and Their Roles',
   'Grade 3 Social Studies strand: community helpers, such as firefighters, doctors, and teachers, each play a specific role that helps keep a community safe, healthy, and running smoothly.',
   [('Community helpers each play a specific role that helps keep a community ___.', ['Safe, healthy, and running smoothly', 'Completely disorganized with no structure at all', 'A concept unrelated to how communities function', 'Isolated from any outside help or support'], 0),
    ('Which is an example of a community helper?', ['A firefighter', 'A role entirely unrelated to helping a community', 'A person who provides no service to others', 'A job with no connection to community wellbeing'], 0),
    ('Why might a community rely on many different types of helpers, rather than just one kind?', ['Different helpers address different needs, like safety, health, and education', 'A community only ever needs a single type of helper', 'Different types of community helpers have no connection to each other', 'This concept has no relevance to how communities function'], 0),
    ('Why might students be encouraged to learn about the roles of community helpers?', ['It helps them understand and appreciate the different ways people contribute to a community', 'Learning about community helpers provides no useful understanding', 'Community helpers have no real impact on daily life', 'This topic has no connection to social studies learning'], 0),
    ('Why might a community helper need special training for their job?', ['Their role often requires specific skills and knowledge to safely and effectively help others', 'Community helpers never require any special training', 'Training has no connection to being a community helper', 'This concept has no relevance to understanding community roles'], 0)])]),

day(53, [
L('Grammar: Simple and Compound Sentences',
  'Grade 3 Language strand: a simple sentence expresses one complete idea, while a compound sentence joins two related simple sentences together using a joining word like “and,” “but,” or “or.”',
  [('A simple sentence expresses ___.', ['One complete idea', 'Two or more completely unrelated ideas', 'A concept unrelated to complete thoughts', 'No complete idea at all'], 0),
   ('A compound sentence joins two related simple sentences using a ___.', ['Joining word, like “and,” “but,” or “or”', 'A random collection of unrelated words', 'A method unrelated to connecting sentences', 'A number, with no connection to words'], 0),
   ('Which is an example of a compound sentence?', ['I like apples, and my sister likes oranges.', 'I like apples.', 'Apples.', 'A sentence with no complete idea at all.'], 0),
   ('Why might a writer choose to combine two simple sentences into a compound sentence?', ['It can show a connection between two related ideas and improve the flow of writing', 'Combining sentences always makes writing more confusing', 'A compound sentence never has any advantage over two simple sentences', 'This concept has no connection to effective sentence writing'], 0),
   ('Why is “but” considered a joining word that can create a compound sentence?', ['It connects two complete ideas while showing a contrast between them', '“But” has no connection to joining two sentences together', 'Joining words are never used to create compound sentences', 'This word only appears in simple sentences, never in compound ones'], 0)]),
M('Geometry: Classifying 2D Shapes by Properties',
  'Grade 3 Math strand: 2D shapes can be classified by properties such as the number of sides, the number of angles, or whether their sides are equal in length.',
  [('2D shapes can be classified by properties such as the number of ___.', ['Sides', 'Colours used to draw the shape', 'A property unrelated to a shape’s structure', 'People who have drawn the shape before'], 0),
   ('A shape with three sides is called a ___.', ['Triangle', 'Square', 'Pentagon', 'Hexagon'], 0),
   ('Why might two shapes with the same number of sides still be classified differently?', ['Other properties, like whether the sides are equal length or the angles are the same, can also matter', 'Shapes with the same number of sides are always classified identically with no exceptions', 'The number of sides is the only property that could ever matter', 'This concept has no connection to how shapes are classified'], 0),
   ('A shape where all sides are equal in length is described as ___.', ['Regular', 'Irregular, with no connection to equal sides', 'A concept unrelated to side length', 'Impossible to classify'], 0),
   ('Why is classifying shapes by their properties a useful math skill?', ['It helps identify and describe shapes clearly, using specific, shared characteristics', 'Classifying shapes provides no useful information about them', 'Shapes can never be meaningfully grouped or described', 'This concept has no connection to understanding geometry'], 0)]),
Sc('Science: Simple Circuits and Conductors',
   'Grade 3 Science strand: a simple circuit is a complete loop that allows electricity to flow, and a conductor is a material, like metal, that allows electricity to pass through it easily.',
   [('A simple circuit is a complete loop that allows ___ to flow.', ['Electricity', 'Water, with no connection to electricity', 'Air, with no connection to a circuit', 'A concept unrelated to circuits'], 0),
    ('A conductor is a material that allows electricity to ___.', ['Pass through it easily', 'Never pass through it at all', 'A property unrelated to electricity', 'Change into a completely different form of energy'], 0),
    ('Which is an example of a material that is a good conductor of electricity?', ['Metal', 'Rubber, which does not conduct electricity well', 'Wood, which does not conduct electricity well', 'A material entirely unrelated to electricity'], 0),
    ('Why must a circuit form a complete loop for electricity to flow?', ['A break anywhere in the loop stops the electric current from being able to travel all the way around', 'A circuit does not need to be complete for electricity to flow through it', 'The shape of a circuit has no connection to whether electricity flows', 'This concept has no relevance to how simple circuits work'], 0),
    ('Why are materials like rubber and plastic often used to cover electrical wires?', ['These insulating materials do not conduct electricity well, helping keep people safe from electric shock', 'Rubber and plastic are excellent conductors of electricity', 'These materials have no connection to electrical safety', 'This concept has no relevance to how circuits are designed'], 0)]),
SS('Social Studies: Comparing Life in Rural and Urban Canada Long Ago',
   'Grade 3 Social Studies strand: comparing rural and urban communities in Canada long ago reveals differences in daily life, work, and available services during that time period.',
   [('Comparing rural and urban communities long ago reveals differences in daily life, work, and ___.', ['Available services', 'A concept unrelated to how communities differed', 'Only the colour of buildings', 'The exact number of residents, with no other differences considered'], 0),
    ('Why might work in a rural community long ago have often centred around farming?', ['Rural areas typically had more available land suited to agriculture', 'Farming had no connection to rural communities in the past', 'Rural communities long ago never engaged in any form of work', 'This concept has no relevance to understanding communities long ago'], 0),
    ('Why might an urban community long ago have had more access to certain services than a rural one?', ['A higher concentration of people and businesses could support more specialized services in one place', 'Urban and rural communities always had access to identical services', 'The size or density of a community has no connection to available services', 'This concept has no relevance to comparing communities'], 0),
    ('Why is comparing rural and urban life long ago a useful way to understand Canadian history?', ['It highlights how geography and community type shaped different ways of living', 'Comparing these two types of communities provides no useful historical understanding', 'Rural and urban communities long ago were always exactly identical', 'This concept has no connection to studying Canadian history'], 0),
    ('Which is an example of something that might have looked different between a rural and an urban community long ago?', ['The types of jobs available to residents', 'A detail entirely unrelated to how communities functioned', 'Something that would be identical in every possible community', 'A concept unrelated to comparing communities'], 0)])]),

day(54, [
L('Vocabulary: Building Word Families',
  'Grade 3 Language strand: a word family is a group of words that share a common base word or root, such as “play,” “player,” and “playful,” which can help build vocabulary and spelling skills.',
  [('A word family is a group of words that share a common ___.', ['Base word or root', 'Colour, with no connection to spelling or meaning', 'Number of letters exclusively, with no other connection', 'Font, with no connection to word meaning'], 0),
   ('Which is an example of a word family based on the word “play”?', ['Player, playful, playground', 'Cat, dog, bird', 'Words with no connection to “play”', 'A random group of unrelated words'], 0),
   ('Why might learning word families help build vocabulary?', ['Recognizing a shared base word can help figure out the meaning of related new words', 'Word families have no connection to understanding new vocabulary', 'Learning related words never helps expand a reader’s vocabulary', 'This concept has no relevance to vocabulary development'], 0),
   ('Why might understanding word families also help with spelling?', ['Words in the same family often share similar spelling patterns based on their common base', 'Word families have no connection to how words are spelled', 'Every word in a word family is always spelled in a completely different way', 'This concept has no relevance to spelling skills'], 0),
   ('If you know the word “teach,” which word might belong to the same word family?', ['Teacher', 'Bicycle', 'A word entirely unrelated to “teach”', 'Elephant'], 0)]),
M('Data: Interpreting Double Bar Graphs',
  'Grade 3 Math strand: a double bar graph compares two related sets of data side by side using pairs of bars, making it easier to see differences and similarities between the two groups.',
  [('A double bar graph compares two related sets of data using ___.', ['Pairs of bars', 'A single line with no bars at all', 'A concept unrelated to comparing data', 'Only one bar per category, with no comparison possible'], 0),
   ('Why might a double bar graph be more useful than two separate single bar graphs for comparing data?', ['It allows for an easier, more direct comparison since related bars are shown side by side', 'A double bar graph is always harder to read than two separate graphs', 'Double bar graphs provide no advantage for comparing related data', 'This concept has no connection to interpreting data'], 0),
   ('Which is an example of data that might be shown using a double bar graph?', ['The number of boys and girls who chose each favourite sport', 'A single, unrelated number with no comparison involved', 'Data that cannot be organized or compared in any way', 'A concept unrelated to comparing two groups'], 0),
   ('Why is a clear legend or key important when reading a double bar graph?', ['It helps the reader understand what each of the two different colours or bars represents', 'A legend has no useful purpose on a double bar graph', 'Double bar graphs never require any additional explanation', 'This concept has no connection to correctly interpreting a graph'], 0),
   ('If a double bar graph shows more students prefer summer over winter, what could you conclude?', ['Summer is the more popular season among the students surveyed', 'The graph shows no meaningful information at all', 'Winter must be more popular, regardless of what the graph shows', 'This conclusion cannot be determined from a double bar graph'], 0)]),
Sc('Science: Properties of Air',
   'Grade 3 Science strand: air is a form of matter that takes up space and has mass, even though it cannot usually be seen, and it plays an important role in supporting life and various natural processes.',
   [('Air is a form of matter that takes up space and has ___.', ['Mass', 'No physical properties whatsoever', 'A concept unrelated to matter', 'Only colour, with no other physical properties'], 0),
    ('Although air usually cannot be seen, it can still be described as a form of ___.', ['Matter', 'Energy exclusively, with no connection to matter', 'A concept unrelated to physical substances', 'Light, with no connection to physical matter'], 0),
    ('Which is an example of evidence that air takes up space?', ['A balloon expanding as it is filled with air', 'A situation with no connection to air at all', 'An event that has nothing to do with physical space', 'A concept unrelated to demonstrating air’s properties'], 0),
    ('Why is air considered important for supporting life?', ['Many living things, including humans, rely on air for the oxygen needed to survive', 'Air has no connection to how living things survive', 'Living things never actually require air in any way', 'This concept has no relevance to understanding air’s importance'], 0),
    ('Why might scientists say that air has mass, even though we usually cannot feel it directly?', ['Careful experiments and measurements have shown that air, like other forms of matter, has a measurable mass', 'Air has never been shown to have any mass at all', 'Mass only applies to solid objects, never to air', 'This concept has no scientific basis'], 0)]),
SS('Social Studies: Trade Between Communities Today',
   'Grade 3 Social Studies strand: communities today trade goods and services with one another because no single community can produce everything it needs, allowing everyone to benefit from what each community does well.',
   [('Communities today trade goods and services because no single community can ___.', ['Produce everything it needs', 'Ever benefit from working with another community', 'A concept unrelated to trade', 'Survive using only its own limited resources, with no exceptions'], 0),
    ('Trade between communities allows everyone to benefit from ___.', ['What each community does well', 'A concept entirely unrelated to specialization or skill', 'Only the largest, most powerful community involved', 'Nothing at all, since trade provides no benefit'], 0),
    ('Which is an example of a good that one community might trade with another?', ['Crops grown on local farms', 'A concept unrelated to goods or trade', 'Something that has no value to any community', 'An item that could never be exchanged between communities'], 0),
    ('Why might a community that grows a lot of a certain crop choose to trade with a community that produces a different resource?', ['Trading allows each community to access resources they may not easily produce themselves', 'Trade never benefits any of the communities involved', 'Communities never need any resources beyond what they can produce themselves', 'This concept has no relevance to understanding trade'], 0),
    ('Why is trade between communities considered an important part of how societies function today?', ['It allows for a wider variety of goods and services to be available to everyone', 'Trade has no meaningful impact on how communities access goods and services', 'Societies could function identically with no trade between communities at all', 'This concept has no relevance to social studies learning'], 0)])]),

day(55, [
L('Reading: Story Elements -- Setting and Plot',
  'Grade 3 Language strand: the setting of a story is the time and place where it happens, and the plot is the sequence of events that make up the story, often including a problem and its solution.',
  [('The setting of a story is the ___ where it happens.', ['Time and place', 'Only the main character’s name', 'A concept unrelated to a story’s structure', 'The book’s exact page count'], 0),
   ('The plot of a story is the sequence of ___ that make up the story.', ['Events', 'Colours used in the story’s illustrations', 'A concept unrelated to how a story unfolds', 'Only the title and author’s name'], 0),
   ('A story’s plot often includes a problem and its ___.', ['Solution', 'A concept unrelated to how a story resolves', 'Only the very beginning of the story, with no further development', 'A detail with no connection to the story’s events'], 0),
   ('Why might understanding a story’s setting help a reader better understand the plot?', ['The time and place can influence what happens and why characters make certain choices', 'Setting has no connection to a story’s plot or events', 'A story’s plot is never affected by where or when it takes place', 'This concept has no relevance to understanding a story'], 0),
   ('If a story is set in a snowy mountain village, how might this setting affect the plot?', ['Characters might face challenges or events related to cold weather or mountain life', 'The setting would have no effect on the events of the story', 'Setting never influences the challenges characters might face', 'This concept has no connection to how a story’s plot might develop'], 0)]),
M('Fractions: Mixed Numbers',
  'Grade 3 Math strand: a mixed number combines a whole number and a fraction together, representing an amount that is more than a whole but not a complete additional whole.',
  [('A mixed number combines a whole number and a ___.', ['Fraction', 'A concept unrelated to numbers', 'Only a decimal, with no connection to fractions', 'A completely different whole number, with no fractional part'], 0),
   ('A mixed number represents an amount that is ___.', ['More than a whole but not a complete additional whole', 'Always exactly equal to zero', 'Less than one whole in every case', 'A concept unrelated to whole numbers or fractions'], 0),
   ('Which is an example of a mixed number?', ['2 and 1/2', 'Only the number 2, with no fractional part', 'Only the fraction 1/2, with no whole number', 'A number entirely unrelated to fractions'], 0),
   ('If you have one whole pizza and half of another pizza, how could this amount be written as a mixed number?', ['1 and 1/2', '2', '1/2', 'A value that cannot be represented as a mixed number'], 0),
   ('Why might mixed numbers be useful for describing real-world amounts, like a recipe calling for 2 and 1/4 cups of flour?', ['They can precisely represent an amount that is more than a whole number but includes a fractional part', 'Mixed numbers have no real-world usefulness', 'Recipes never need to describe amounts using mixed numbers', 'This concept has no connection to everyday measurements'], 0)]),
Sc('Science: Living Things and Their Basic Needs',
   'Grade 3 Science strand: all living things share certain basic needs, including food, water, air, and a suitable habitat, which they require in order to survive and grow.',
   [('All living things share certain basic needs, including food, water, and ___.', ['Air', 'Only sunlight, with no other needs required', 'A concept unrelated to survival', 'Money, which is not a basic need of living things'], 0),
    ('Living things require a suitable ___ in order to survive and grow.', ['Habitat', 'Colour, with no connection to survival', 'A concept unrelated to where living things live', 'Only a single specific temperature, with no other factors mattering'], 0),
    ('Why might a plant struggle to survive if it does not receive enough water?', ['Water is one of the basic needs required for a plant’s survival and growth', 'Plants never actually require water to survive', 'Water has no connection to a plant’s basic needs', 'This concept has no relevance to understanding living things'], 0),
    ('Why do different living things sometimes need different specific habitats to meet their basic needs?', ['Different species have adapted to survive best under particular environmental conditions', 'All living things always require the exact same specific habitat', 'Habitat has no connection to a living thing’s basic needs', 'This concept has no relevance to understanding biodiversity'], 0),
    ('Why is understanding the basic needs of living things important for scientists studying ecosystems?', ['It helps explain why certain living things are found in particular environments and how they might be affected by change', 'Basic needs have no connection to understanding ecosystems', 'Scientists never need to understand the needs of living things', 'This concept has no relevance to environmental science'], 0)]),
SS('Social Studies: Canada’s National Parks and Protected Spaces',
   'Grade 3 Social Studies strand: Canada has many national parks and protected spaces set aside to preserve natural environments, wildlife habitats, and important cultural or historical sites for future generations.',
   [('Canada’s national parks and protected spaces are set aside to preserve natural environments and ___.', ['Wildlife habitats', 'A concept unrelated to conservation', 'Only urban buildings, with no connection to nature', 'Areas with no environmental or cultural significance'], 0),
    ('These protected spaces help preserve important cultural or historical sites for ___.', ['Future generations', 'No one at all, since these spaces serve no purpose', 'Only the current generation, with no consideration of the future', 'A concept unrelated to preservation'], 0),
    ('Why might a national park be created to protect a specific area of land?', ['To preserve its natural environment and wildlife from being permanently changed or destroyed', 'National parks are never created for any particular reason', 'Protecting land has no connection to preserving wildlife or nature', 'This concept has no relevance to understanding conservation'], 0),
    ('Which is an example of something a national park might help protect?', ['A habitat for endangered animals', 'A concept entirely unrelated to conservation', 'Something with no environmental value', 'A structure unrelated to natural or cultural preservation'], 0),
    ('Why is it valuable for Canadians to learn about the country’s national parks and protected spaces?', ['It builds appreciation for the importance of conservation and Canada’s natural and cultural heritage', 'National parks have no relevance to understanding Canadian identity', 'Learning about protected spaces provides no educational value', 'This concept has no connection to social studies learning'], 0)])]),

day(56, [
L('Writing: Writing a Book Review',
  'Grade 3 Language strand: a book review shares a reader’s opinion about a book, including what they liked or disliked, and gives reasons to support that opinion so others can decide if they might enjoy it too.',
  [('A book review shares a reader’s ___ about a book.', ['Opinion', 'A completely factual summary with no personal opinion at all', 'A concept unrelated to a reader’s thoughts on a book', 'Only the exact number of pages'], 0),
   ('A book review should include reasons that support the reader’s ___.', ['Opinion', 'Favourite colour, with no connection to the book', 'A concept unrelated to explaining their view', 'The price of the book only'], 0),
   ('Why might a book review help other readers decide whether to read a book?', ['It offers an honest opinion and specific reasons that can help others predict if they would enjoy it too', 'A book review never provides any useful information to other readers', 'Readers should never consider another person’s opinion about a book', 'This concept has no connection to helping others make reading choices'], 0),
   ('Which is an example of a reason that might support a positive book review?', ['The characters felt relatable and the story kept me interested', 'A reason entirely unrelated to the book’s content', 'A sentence with no connection to the reader’s opinion', 'Simply saying “it was fine” with no further explanation'], 0),
   ('Why is it helpful for a book review to be specific, rather than vague?', ['Specific details help the reader understand exactly what the reviewer liked or disliked and why', 'Vague reviews are always more helpful than specific ones', 'Specificity has no connection to how useful a book review is', 'This concept has no relevance to writing an effective review'], 0)]),
M('Measurement: Converting Units of Length',
  'Grade 3 Math strand: converting units of length involves changing a measurement from one unit, like centimetres, to another, like metres, using the relationship between the two units.',
  [('Converting units of length involves changing a measurement from one unit to ___.', ['Another', 'A concept unrelated to measurement', 'Only the exact same unit, with no actual change', 'A completely unrelated type of measurement, like time'], 0),
   ('How many centimetres are in 1 metre?', ['100', '10', '1000', '50'], 0),
   ('If a ribbon is 200 centimetres long, how many metres is that?', ['2 metres', '20 metres', '200 metres', '0.2 metres'], 0),
   ('Why is it useful to know how to convert between units like centimetres and metres?', ['It allows measurements to be expressed in whichever unit is most useful or appropriate for a given situation', 'Converting between units of length is never useful in any situation', 'All measurements should always be expressed using the exact same unit', 'This concept has no connection to real-world measurement'], 0),
   ('Why might a scientist choose to measure a very small object in millimetres rather than metres?', ['Millimetres provide a more precise and appropriately sized unit for measuring very small objects', 'The choice of unit has no effect on how a measurement is expressed', 'Millimetres and metres are always exactly the same size', 'This concept has no connection to choosing an appropriate unit'], 0)]),
Sc('Science: Camouflage and Survival',
   'Grade 3 Science strand: camouflage is an adaptation that helps an animal blend into its surroundings, making it harder for predators to see them or for prey to notice them approaching.',
   [('Camouflage is an adaptation that helps an animal ___.', ['Blend into its surroundings', 'Always stand out brightly against its surroundings', 'A concept unrelated to survival', 'Change its entire body shape permanently'], 0),
    ('Camouflage can make it harder for predators to ___.', ['See their prey', 'Always immediately catch their prey with no effort', 'A concept unrelated to hunting or survival', 'Find any food source whatsoever'], 0),
    ('Which is an example of an animal using camouflage?', ['A stick insect that resembles a twig', 'An animal with no connection to blending into its environment', 'A concept unrelated to adaptation or survival', 'An animal that always stands out clearly no matter its surroundings'], 0),
    ('Why might camouflage be helpful for a prey animal trying to avoid predators?', ['Blending into the environment can make it harder for a predator to spot and catch them', 'Camouflage has no effect on whether a prey animal is noticed', 'Predators are never affected by how well a prey animal blends in', 'This concept has no connection to survival in the wild'], 0),
    ('Why might camouflage also be a useful adaptation for a predator, and not just prey?', ['It can help a predator sneak up on prey without being noticed until it is too late', 'Camouflage is never useful for predators, only for prey', 'Predators never need to hide or blend into their surroundings', 'This concept has no connection to how camouflage functions'], 0)]),
SS('Social Studies: Indigenous Peoples’ Contributions to Canada',
   'Grade 3 Social Studies strand: Indigenous Peoples have made significant and lasting contributions to Canada, including knowledge of the land, agricultural practices, and cultural traditions that continue to be valued today.',
   [('Indigenous Peoples have made significant contributions to Canada, including knowledge of ___.', ['The land', 'A concept entirely unrelated to Canadian history or culture', 'Only recent technology, with no historical significance', 'Nothing of lasting value'], 0),
    ('These contributions include agricultural practices and ___ traditions.', ['Cultural', 'A concept unrelated to Indigenous knowledge or heritage', 'Only foreign, with no connection to Indigenous communities', 'Nonexistent, since no traditions have been passed down'], 0),
    ('Why is it important to recognize Indigenous Peoples’ contributions when learning about Canadian history?', ['It provides a fuller and more accurate understanding of how Canada developed', 'Indigenous contributions have no connection to Canadian history', 'A complete understanding of Canadian history requires no recognition of Indigenous Peoples', 'This concept has no relevance to social studies learning'], 0),
    ('Which is an example of a contribution Indigenous Peoples have made to Canada?', ['Knowledge of sustainable land and resource use', 'A concept entirely unrelated to Indigenous knowledge', 'A contribution with no lasting significance today', 'Something that has no connection to Canadian history or culture'], 0),
    ('Why do these contributions continue to be valued in Canada today?', ['Indigenous knowledge and traditions remain relevant and important to many aspects of Canadian life and identity', 'These contributions have no relevance to modern Canadian society', 'Indigenous knowledge and traditions are never considered valuable today', 'This concept has no connection to understanding contemporary Canada'], 0)])]),

day(57, [
L('Media Literacy: Understanding Misinformation',
  'Grade 3 Language strand: misinformation is false or misleading information, and learning to check whether something seems true, especially online, is an important skill for young readers today.',
  [('Misinformation is information that is ___.', ['False or misleading', 'Always completely accurate and trustworthy', 'A concept unrelated to accuracy or truth', 'Only ever found in printed books, never online'], 0),
   ('Why is it important for young readers to check whether information seems true, especially online?', ['Not everything found online, especially without checking, is accurate or trustworthy', 'Everything found online is always completely true', 'Checking information online is never a useful skill', 'This concept has no connection to responsible reading habits'], 0),
   ('Which is a strategy that might help someone figure out if information could be misinformation?', ['Checking if other trusted sources say the same thing', 'Believing anything without ever questioning it', 'Ignoring where the information came from entirely', 'Assuming every single source is always correct'], 0),
   ('Why might a picture or video sometimes be used to spread misinformation?', ['Images and videos can sometimes be edited or shared without proper context, making false information seem believable', 'Pictures and videos can never be used to spread false information', 'Misinformation only ever appears in written text, never in images', 'This concept has no connection to how misinformation spreads'], 0),
   ('Why is learning to recognize misinformation considered an important media literacy skill today?', ['So much information is shared quickly, especially online, making it important to think carefully before believing or sharing it', 'Misinformation has no real impact on how people understand the world', 'This skill has no relevance to how young people use information today', 'Media literacy has no connection to recognizing false information'], 0)]),
M('Patterning: Number Patterns with Multiplication and Division',
  'Grade 3 Math strand: number patterns can be created using multiplication and division, where each term relates to the one before it by a consistent multiplying or dividing rule.',
  [('Number patterns using multiplication and division follow a consistent ___.', ['Rule', 'Completely random sequence with no rule involved', 'A concept unrelated to how patterns are formed', 'Set of unrelated numbers with no connection to each other'], 0),
   ('In the pattern 2, 4, 8, 16..., what rule is being used?', ['Multiply by 2 each time', 'Add 2 each time', 'Divide by 2 each time', 'Subtract 2 each time'], 0),
   ('What is the next number in the pattern 3, 6, 9, 12, ___?', ['15', '14', '13', '16'], 0),
   ('Why might identifying the rule of a number pattern help predict future numbers in the sequence?', ['Once the rule is known, it can be applied consistently to figure out what comes next', 'Identifying a pattern’s rule never helps predict future numbers', 'Number patterns can never be predicted using any kind of rule', 'This concept has no connection to understanding patterns'], 0),
   ('Why might multiplication and division patterns grow or shrink faster than patterns based on addition or subtraction?', ['Multiplying or dividing by a number can change a value more dramatically than simply adding or subtracting the same amount', 'Multiplication and division patterns always change at exactly the same rate as addition patterns', 'The type of operation used has no effect on how quickly a pattern grows or shrinks', 'This concept has no connection to understanding number patterns'], 0)]),
Sc('Science: Renewable Energy in Everyday Life',
   'Grade 3 Science strand: renewable energy sources, such as sunlight and wind, can be used in everyday life to power homes, schools, and communities in ways that do not run out over time.',
   [('Renewable energy sources, like sunlight and wind, can be used to power homes, schools, and ___.', ['Communities', 'A concept unrelated to energy use', 'Only vehicles from long ago, with no modern use', 'Nothing at all, since renewable energy has no practical use'], 0),
    ('A key feature of renewable energy sources is that they ___ over time.', ['Do not run out', 'Always run out very quickly', 'A concept unrelated to energy sources', 'Become completely unusable within a single day'], 0),
    ('Which is an example of a renewable energy source used in everyday life?', ['Solar panels on a rooftop', 'A source of energy that will eventually run out completely', 'A concept unrelated to renewable energy', 'Something with no connection to power or electricity'], 0),
    ('Why might a school choose to install solar panels to help power its building?', ['Solar panels can provide a source of energy that does not run out and may reduce reliance on other energy sources', 'Solar panels have no practical use for powering a school', 'Renewable energy sources are never used in real-world buildings', 'This concept has no connection to everyday energy use'], 0),
    ('Why is learning about renewable energy considered valuable for young students today?', ['Understanding these energy sources can help build awareness of sustainable ways to power everyday life', 'Renewable energy has no relevance to students’ everyday lives', 'This topic has no connection to science learning', 'Learning about energy sources provides no useful understanding'], 0)]),
SS('Social Studies: Immigration Stories -- Then and Now',
   'Grade 3 Social Studies strand: comparing immigration stories from the past and present helps show both how reasons for immigrating to Canada have stayed similar and how the experience has changed over time.',
   [('Comparing immigration stories from the past and present can show how reasons for immigrating have ___.', ['Stayed similar in some ways', 'Never had any connection to each other', 'A concept unrelated to immigration history', 'Been completely different in every possible way'], 0),
    ('This comparison can also show how the experience of immigrating has ___ over time.', ['Changed', 'Remained exactly identical in every detail', 'A concept unrelated to immigration experiences', 'Had no connection to any historical changes'], 0),
    ('Why might someone immigrate to a new country, both long ago and today?', ['Reasons like seeking better opportunities or safety have remained common across different time periods', 'People have never had any reasons to immigrate to a new country', 'Immigration has no connection to seeking opportunity or safety', 'This concept has no relevance to understanding immigration history'], 0),
    ('Which is an example of something that might be different about immigrating to Canada today compared to long ago?', ['Modern methods of travel, like airplanes, compared to earlier methods like ships', 'A detail with no connection to how immigration has changed', 'Something that has remained exactly identical throughout history', 'A concept unrelated to comparing different time periods'], 0),
    ('Why is learning about immigration stories, both past and present, valuable for understanding Canada?', ['It helps build appreciation for the diverse experiences that have shaped Canadian communities over time', 'Immigration stories have no connection to understanding Canadian history or identity', 'This topic provides no useful understanding of Canadian communities', 'This concept has no relevance to social studies learning'], 0)])]),

day(58, [
L('Reading: Skimming and Scanning for Information',
  'Grade 3 Language strand: skimming means quickly looking over a text to get a general idea of what it is about, while scanning means quickly searching for a specific piece of information within a text.',
  [('Skimming means quickly looking over a text to get a ___ idea of what it is about.', ['General', 'Extremely detailed, word-by-word', 'A concept unrelated to reading quickly', 'Completely incorrect, with no useful information at all'], 0),
   ('Scanning means quickly searching for a ___ within a text.', ['Specific piece of information', 'Completely unrelated topic', 'A concept unrelated to finding information', 'The exact number of words in the entire text'], 0),
   ('Why might a reader skim a text before deciding whether to read it fully?', ['Skimming can quickly reveal whether the text’s general topic matches what the reader is looking for', 'Skimming never provides any useful information about a text', 'A reader should always read every single word before deciding anything about a text', 'This concept has no connection to efficient reading strategies'], 0),
   ('Which is an example of a situation where scanning would be a useful strategy?', ['Looking for a specific date mentioned in a long article', 'Reading a story purely for enjoyment with no specific goal', 'A situation with no connection to searching for information', 'Memorizing an entire book word for word'], 0),
   ('Why are skimming and scanning considered useful reading strategies, especially for research?', ['They allow a reader to quickly find relevant information without needing to read every single word carefully', 'These strategies are never useful for finding information efficiently', 'Skimming and scanning always take longer than reading a text in full detail', 'This concept has no relevance to effective research skills'], 0)]),
M('Financial Literacy: Comparing Prices and Value',
  'Grade 3 Math strand: comparing prices and value involves looking at cost alongside quantity or quality to determine which option gives the best overall value for money.',
  [('Comparing prices and value involves looking at cost alongside ___.', ['Quantity or quality', 'A concept unrelated to making a purchasing decision', 'Only the colour of the packaging', 'The exact time of day an item was purchased'], 0),
   ('If two bags of apples cost the same but one has more apples, which is generally the better value?', ['The bag with more apples', 'The bag with fewer apples', 'Both bags always provide exactly the same value', 'Value cannot be determined in this situation'], 0),
   ('Why might comparing the price per item be a useful strategy when shopping?', ['It provides a fair way to compare value between items sold in different quantities or sizes', 'Comparing price per item never provides any useful information', 'Price per item has no connection to determining overall value', 'This strategy is only useful for very large purchases'], 0),
   ('Why is it important to consider quality, not just price, when comparing value?', ['A cheaper item that does not work well or last long may not actually be the better overall value', 'Quality never has any connection to an item’s overall value', 'Price is always the only factor that matters when comparing value', 'This concept has no relevance to making informed purchasing decisions'], 0),
   ('If a $10 toy breaks quickly but a $15 toy lasts much longer, which might be considered the better value over time?', ['The $15 toy, since it lasts longer', 'The $10 toy, regardless of how quickly it breaks', 'Both toys always provide exactly the same value', 'Value can never be determined in this type of situation'], 0)]),
Sc('Science: Forces in Sports and Play',
   'Grade 3 Science strand: forces like push, pull, and friction play an important role in everyday sports and play activities, affecting how objects like balls move, speed up, slow down, or change direction.',
   [('Forces like push, pull, and friction play an important role in everyday ___ activities.', ['Sports and play', 'A concept entirely unrelated to physical activity', 'Only activities that involve no movement whatsoever', 'Situations with no connection to forces at all'], 0),
    ('These forces can affect how a ball ___.', ['Moves, speeds up, slows down, or changes direction', 'Always stays perfectly still with no movement at all', 'A concept unrelated to how objects behave', 'Changes into a completely different object'], 0),
    ('Which is an example of a push force used in a sport?', ['Kicking a soccer ball', 'A concept unrelated to force or motion', 'An action that involves no physical force whatsoever', 'A situation where no object is set in motion'], 0),
    ('Why might friction cause a rolling ball to eventually slow down and stop?', ['Friction between the ball and the surface it rolls on acts as a resisting force against its motion', 'Friction has no effect on the motion of a rolling ball', 'A ball would roll forever with no force ever causing it to stop', 'This concept has no connection to how forces affect motion'], 0),
    ('Why might understanding forces be useful for someone trying to improve their performance in a sport like basketball?', ['Understanding how forces affect a ball’s motion can help a player make more accurate and controlled shots', 'Forces have no connection to how well someone might perform in a sport', 'Understanding physics never has any practical application in sports', 'This concept has no relevance to playing or improving at a sport'], 0)]),
SS('Social Studies: How Ontario Uses Its Resources',
   'Grade 3 Social Studies strand: Ontario uses its natural resources, such as forests, minerals, and freshwater, to support industries and communities, while also facing the responsibility of managing these resources sustainably.',
   [('Ontario uses natural resources like forests, minerals, and freshwater to support ___.', ['Industries and communities', 'A concept unrelated to how resources are used', 'Only industries in other provinces, with no benefit to Ontario', 'Nothing at all, since these resources have no practical use'], 0),
    ('Along with using its resources, Ontario also faces the responsibility of managing them ___.', ['Sustainably', 'Without any consideration for the future', 'A concept unrelated to responsible resource use', 'In a way that has no connection to long-term planning'], 0),
    ('Which is an example of a natural resource used by industries in Ontario?', ['Freshwater', 'A concept entirely unrelated to natural resources', 'Something with no connection to Ontario’s economy', 'A resource that does not actually exist in Ontario'], 0),
    ('Why might it be important for Ontario to manage its natural resources sustainably?', ['Sustainable management helps ensure these resources remain available for future generations', 'Sustainability has no connection to managing natural resources', 'Ontario’s natural resources will always be available no matter how they are used', 'This concept has no relevance to understanding Ontario’s economy'], 0),
    ('Why might different communities in Ontario rely on different natural resources based on their location?', ['The specific resources available often depend on a region’s geography and environment', 'Every community in Ontario always relies on the exact same natural resources', 'Location has no connection to which natural resources are available', 'This concept has no relevance to understanding Ontario’s geography'], 0)])]),

day(59, [
L('Oral Communication: Retelling a Story',
  'Grade 3 Language strand: retelling a story involves summarizing the key events in the correct order, using your own words while still including the most important details from the original story.',
  [('Retelling a story involves summarizing the key events in ___.', ['The correct order', 'A completely random, mixed-up order', 'A concept unrelated to how a story unfolds', 'Only the very last event, with no other details included'], 0),
   ('When retelling a story, it is important to use ___.', ['Your own words, while including important details', 'The exact same words as the original text, with no changes at all', 'A concept unrelated to summarizing a story', 'No details from the original story whatsoever'], 0),
   ('Why is retelling a story in the correct order important?', ['It helps the listener understand how the events of the story logically connect to one another', 'The order of events has no effect on how well a retelling is understood', 'A story can always be retold in a completely random order with no issue', 'This concept has no connection to effective oral communication'], 0),
   ('Which is an example of an important detail to include when retelling a story?', ['The main problem the character faced', 'A minor detail that has no connection to the main story', 'Every single word from the original text, with nothing left out', 'A detail entirely unrelated to the story’s events'], 0),
   ('Why is retelling a story a valuable skill for building reading comprehension?', ['It requires understanding and organizing the key events, which shows a deeper understanding of the text', 'Retelling a story never helps demonstrate understanding of a text', 'This skill has no connection to reading comprehension', 'A reader can retell a story without any understanding of its events'], 0)]),
M('Geometry: Area of Irregular Shapes',
  'Grade 3 Math strand: the area of an irregular shape can be estimated by breaking it into smaller, more familiar shapes, like squares and rectangles, and adding their areas together.',
  [('The area of an irregular shape can be estimated by breaking it into smaller, more familiar shapes like ___.', ['Squares and rectangles', 'A concept unrelated to geometry', 'Only circles, with no other shapes considered', 'Numbers with no connection to shapes at all'], 0),
   ('After breaking an irregular shape into smaller shapes, you find the total area by ___.', ['Adding their areas together', 'Ignoring all of the smaller shapes completely', 'A method unrelated to finding area', 'Subtracting the areas from each other'], 0),
   ('Why might breaking an irregular shape into smaller, familiar shapes make finding its area easier?', ['Calculating the area of simple shapes like squares and rectangles is often more straightforward', 'Breaking a shape apart always makes finding its area more difficult', 'This strategy has no connection to calculating area', 'Irregular shapes can never have their area estimated using any method'], 0),
   ('If an irregular shape is broken into a rectangle with an area of 12 and a square with an area of 4, what is the shape’s total estimated area?', ['16', '8', '48', '12'], 0),
   ('Why is estimating the area of irregular shapes a useful real-world math skill?', ['Many real objects and spaces are not perfectly regular shapes, so this skill helps measure them practically', 'Irregular shapes never appear in real-world situations', 'This concept has no useful, practical application', 'Only perfectly regular shapes ever need to have their area calculated'], 0)]),
Sc('Science: Investigating Matter -- Mixtures and Solutions',
   'Grade 3 Science strand: a mixture combines two or more substances that keep their own properties, and a solution is a special type of mixture where one substance dissolves completely into another.',
   [('A mixture combines two or more substances that ___.', ['Keep their own properties', 'Always completely change into an entirely new substance', 'A concept unrelated to combining substances', 'Cannot ever be separated again under any circumstances'], 0),
    ('A solution is a special type of mixture where one substance ___.', ['Dissolves completely into another', 'Always remains completely separate and visible', 'A concept unrelated to mixtures', 'Changes into a solid with no connection to the original substance'], 0),
    ('Which is an example of a solution?', ['Sugar dissolved completely in water', 'A concept unrelated to mixtures or solutions', 'Two substances that never combine in any way', 'Sand mixed with small pebbles, with both remaining clearly visible'], 0),
    ('Why might sand and water be considered a mixture, but not a true solution?', ['The sand does not dissolve and can still be seen and separated from the water', 'Sand and water always form a true, completely dissolved solution', 'This combination has no connection to the concept of mixtures', 'Mixtures and solutions are always exactly identical concepts'], 0),
    ('Why is understanding the difference between mixtures and solutions useful in everyday life, such as when cooking?', ['It can help explain why some ingredients blend smoothly together while others remain visibly separate', 'This distinction has no connection to everyday activities like cooking', 'Mixtures and solutions never behave differently from one another', 'This concept has no relevance to understanding how substances combine'], 0)]),
SS('Review: Government, Trade, and Community',
   'Grade 3 Social Studies strand review: this lesson revisits local government decision-making, community helpers, trade between communities, and Ontario’s use of natural resources.',
   [('Local, or municipal, governments make decisions about community services like ___.', ['Parks, roads, and libraries', 'Only decisions that affect other countries', 'A topic unrelated to community services', 'Decisions with no connection to daily community life'], 0),
    ('Why might a community rely on many different types of helpers, rather than just one kind?', ['Different helpers address different needs, like safety, health, and education', 'A community only ever needs a single type of helper', 'Different types of community helpers have no connection to each other', 'This concept has no relevance to how communities function'], 0),
    ('Trade between communities allows everyone to benefit from ___.', ['What each community does well', 'A concept entirely unrelated to specialization or skill', 'Only the largest, most powerful community involved', 'Nothing at all, since trade provides no benefit'], 0),
    ('Why might it be important for Ontario to manage its natural resources sustainably?', ['Sustainable management helps ensure these resources remain available for future generations', 'Sustainability has no connection to managing natural resources', 'Ontario’s natural resources will always be available no matter how they are used', 'This concept has no relevance to understanding Ontario’s economy'], 0),
    ('Why is it useful to review government, trade, and community topics together?', ['It reinforces how these related social studies concepts connect to how communities function', 'These topics have no connection to each other', 'Review is never useful in social studies', 'Each topic must be studied with no connection to the others'], 0)])]),

day(60, [
L('Writing: Editing and Proofreading Checklist',
  'Grade 3 Language strand: using a checklist while editing and proofreading helps writers systematically check their work for issues like spelling, punctuation, capitalization, and complete sentences before sharing it.',
  [('Using a checklist while editing and proofreading helps writers ___ their work.', ['Systematically check', 'Never actually review or improve', 'A concept unrelated to reviewing writing', 'Completely rewrite from scratch every single time'], 0),
   ('Which is an example of something a proofreading checklist might include?', ['Checking for correct punctuation', 'A step entirely unrelated to reviewing written work', 'Only checking the length of the piece, with no other consideration', 'Ignoring spelling errors completely'], 0),
   ('Why might using a checklist help a writer catch mistakes they might otherwise miss?', ['A checklist provides a clear, organized way to review specific types of errors one at a time', 'A checklist never actually helps identify any mistakes', 'Writers always catch every mistake without needing any kind of checklist', 'This concept has no connection to effective proofreading'], 0),
   ('Why is checking for complete sentences an important part of proofreading?', ['Incomplete sentences can be confusing or unclear for a reader to understand', 'Complete sentences have no effect on how clearly writing communicates', 'Every sentence is always automatically complete, with no need to check', 'This concept has no relevance to editing written work'], 0),
   ('Why might a writer proofread their work after taking a short break, rather than immediately after finishing?', ['Stepping away can help a writer notice mistakes more easily with fresh eyes', 'Taking a break before proofreading never has any benefit', 'A writer should always proofread immediately with no break at all', 'This concept has no connection to effective revision strategies'], 0)]),
M('Review: Multiplication, Division, and Geometry',
  'Grade 3 Math strand review: this lesson revisits multiplying and dividing 2-digit numbers, classifying 2D shapes, converting units of length, and finding the area of irregular shapes.',
  [('What is 23 × 3?', ['69', '63', '66', '73'], 0),
   ('What is 48 ÷ 4?', ['12', '10', '14', '16'], 0),
   ('A shape with three sides is called a ___.', ['Triangle', 'Square', 'Pentagon', 'Hexagon'], 0),
   ('How many centimetres are in 1 metre?', ['100', '10', '1000', '50'], 0),
   ('Why is it useful to review multiplication, division, and geometry skills together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Rocks, Energy, and Living Things',
   'Grade 3 Science strand review: this lesson revisits the rock cycle, simple circuits, renewable energy, camouflage, and the basic needs of living things.',
   [('The rock cycle describes how rocks slowly ___ over long periods of time.', ['Change from one type to another', 'Always remain exactly the same, with no change at all', 'A concept unrelated to how rocks form', 'Disappear completely with no trace remaining'], 0),
    ('A conductor is a material that allows electricity to ___.', ['Pass through it easily', 'Never pass through it at all', 'A property unrelated to electricity', 'Change into a completely different form of energy'], 0),
    ('Camouflage is an adaptation that helps an animal ___.', ['Blend into its surroundings', 'Always stand out brightly against its surroundings', 'A concept unrelated to survival', 'Change its entire body shape permanently'], 0),
    ('All living things share certain basic needs, including food, water, and ___.', ['Air', 'Only sunlight, with no other needs required', 'A concept unrelated to survival', 'Money, which is not a basic need of living things'], 0),
    ('Why is it useful to review rocks, energy, and living things together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Grade 3 Social Studies: Extending Our Community Knowledge',
   'Grade 3 Social Studies strand: this lesson celebrates and extends the Days 51-60 learning about local government, community helpers, trade, national parks, Indigenous contributions, immigration, and Ontario’s resources.',
   [('Why is it valuable for students to understand how local government decisions are made?', ['It helps them understand how their own community works and how they might participate in it someday', 'This understanding has no connection to being part of a community', 'Local government decisions never affect students or their families', 'This topic has no relevance to social studies learning'], 0),
    ('Why is it valuable for Canadians to learn about the country’s national parks and protected spaces?', ['It builds appreciation for the importance of conservation and Canada’s natural and cultural heritage', 'National parks have no relevance to understanding Canadian identity', 'Learning about protected spaces provides no educational value', 'This concept has no connection to social studies learning'], 0),
    ('Why is it important to recognize Indigenous Peoples’ contributions when learning about Canadian history?', ['It provides a fuller and more accurate understanding of how Canada developed', 'Indigenous contributions have no connection to Canadian history', 'A complete understanding of Canadian history requires no recognition of Indigenous Peoples', 'This concept has no relevance to social studies learning'], 0),
    ('Why is learning about immigration stories, both past and present, valuable for understanding Canada?', ['It helps build appreciation for the diverse experiences that have shaped Canadian communities over time', 'Immigration stories have no connection to understanding Canadian history or identity', 'This topic provides no useful understanding of Canadian communities', 'This concept has no relevance to social studies learning'], 0),
    ('Why is it useful to bring together lessons about government, culture, and resources at this point in the year?', ['It helps students see how these different aspects of a community and country connect and support one another', 'These topics have no meaningful connection to each other', 'Bringing lessons together never provides any additional understanding', 'Each topic must always be learned with no connection to any other'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260729):
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
    _rebalance_answer_positions(g3_51_60)
    append_to(3, g3_51_60)
