#!/usr/bin/env python3
"""Grade 6, Days 141-150 -- extends Grade 6 from 140 to 150 days. Modeled
exactly on gen_grade6_days131_140.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-140
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics:
interjections and exclamatory sentences, theme versus topic, writing an
acrostic poem, sponsored content and native advertising, compound-complex
sentences, delivering an elevator pitch, jargon and technical vocabulary,
writing a letter to the editor, and setting and mood for Language;
combining like terms, adding/subtracting mixed numbers with regrouping,
surface area of cones, midpoint and length of a line segment, naming
polygons from pentagons through decagons, identifying misleading graphs,
expected value, comparing subscription plans, and precision versus
accuracy for Math; biomass and biofuels, carrying capacity, the wheel and
axle, nuclear energy, monarch butterfly migration, hydrothermal vents,
sunscreen and UV radiation, earthquake-resistant building design, and
blood types for Science; and residential schools in Canada, the Order of
Canada, the Canadian Museum for Human Rights, Canadas provinces and
territories, how the federal government creates a budget, the numbered
treaties, the Canadian Coast Guard, Black Loyalists, and Canadas role in
the Korean War for Social Studies -- none of those exact ideas appear in
Days 1-140. Day 150 is a review day across all four subjects, matching
the end-of-batch pattern used in every prior 10-day batch; its four
review titles are worded distinctly from Day 140's review titles even
though both are review days. No embedded ASCII apostrophe or double-quote
characters are used anywhere in title/summary/question/option text --
apostrophes are dropped entirely (e.g. "Canadas" not "Canada's"),
matching the rest of Grade 6.

Usage: python3 gen_grade6_days141_150.py
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


g6_141_150 = [
day(141, [
L('Grammar: Interjections and Exclamatory Sentences',
  'Grade 6 Language strand: an interjection is a word or phrase that expresses strong or sudden emotion, such as surprise, joy, or pain, and is often followed by an exclamation mark, while an exclamatory sentence expresses strong feeling as a complete sentence.',
  [('What is an interjection?', ['A word or phrase that expresses strong or sudden emotion', 'A word that joins two clauses together', 'A pronoun that replaces a noun', 'A verb that shows action'], 0),
   ('Which of these is an example of an interjection?', ['Wow', 'Because', 'Under', 'Quickly'], 0),
   ('What punctuation mark most often follows a strong interjection?', ['An exclamation mark', 'A comma only', 'A question mark', 'A colon'], 0),
   ('Which sentence is exclamatory?', ['What an amazing goal that was', 'Please pass the ball.', 'Did you see the goal?', 'The game starts at noon.'], 0),
   ('Why might a writer use an interjection in dialogue?', ['To show a characters sudden emotion in a natural, realistic way', 'To replace the need for any punctuation', 'To make a sentence grammatically incomplete', 'To remove all emotion from the writing'], 0)]),
M('Algebra: Combining Like Terms',
  'Grade 6 Math strand: like terms have the same variable raised to the same power, and combining like terms means adding or subtracting their coefficients to simplify an algebraic expression.',
  [('What are like terms?', ['Terms that have the same variable raised to the same power', 'Terms that always have the same numerical coefficient', 'Any two terms found in the same expression', 'Terms that contain no variables at all'], 0),
   ('Which pair of terms are like terms?', ['3x and 7x', '3x and 7y', '3x and 7x squared', '3 and x'], 0),
   ('What is the simplified form of 4x plus 5x?', ['9x', '20x', '9x squared', '4x plus 5'], 0),
   ('Why can 6y and 2 not be combined as like terms?', ['One term has a variable and the other does not', 'Both terms have the exact same variable', 'Both terms are already fully simplified', 'Numbers can never appear in algebraic expressions'], 0),
   ('Why is combining like terms a useful first step when simplifying an expression?', ['It reduces the expression to its simplest form, making it easier to work with', 'It always makes an expression longer and more complex', 'Combining like terms changes the value of the expression', 'Like terms must always be kept separate in every expression'], 0)]),
Sc('Renewable Energy: Biomass and Biofuels',
   'Grade 6 Science strand: biomass energy comes from burning or converting organic material such as wood, crop waste, or plant matter into usable energy, and biofuels are liquid fuels made from these renewable organic sources.',
   [('What is biomass energy made from?', ['Organic material such as wood, crop waste, or plant matter', 'Only fossil fuels formed over millions of years', 'Nuclear reactions inside a power plant', 'Wind passing through a turbine'], 0),
    ('What is a biofuel?', ['A liquid fuel made from renewable organic sources', 'A fuel made only from crude oil', 'A type of nuclear fuel rod', 'A fuel that can never be renewed'], 0),
    ('Why is biomass considered a renewable energy source?', ['The organic materials it uses can be regrown or replenished over time', 'It can never be replenished once it is used', 'It relies entirely on materials formed over millions of years', 'It requires no natural resources at all'], 0),
    ('What is one way biomass energy is commonly produced?', ['By burning organic material to generate heat or electricity', 'By splitting atoms inside a reactor', 'By capturing sunlight with solar panels', 'By harnessing the power of moving water'], 0),
    ('What is one potential drawback of relying heavily on biomass energy?', ['Growing crops for fuel could compete with land needed for growing food', 'Biomass energy produces no usable heat or electricity', 'Biomass sources can never be regrown', 'Biomass energy has no environmental impact whatsoever'], 0)]),
SS('Social Studies: Residential Schools in Canada — A History',
   'Grade 6 Social Studies strand: from the 1800s until 1996, the Canadian government and churches operated residential schools that forcibly removed Indigenous children from their families, banning their languages and cultures, a system now recognized as a deeply harmful chapter in Canadian history.',
   [('What were residential schools in Canada designed to do?', ['Forcibly remove Indigenous children from their families and assimilate them', 'Provide optional after-school tutoring for all Canadian children', 'Teach Indigenous languages and cultural traditions', 'Offer free summer camps for Canadian families'], 0),
    ('Approximately when did the last residential school in Canada close?', ['1996', '1867', '1945', '2010'], 0),
    ('What were Indigenous children at residential schools often forbidden from doing?', ['Speaking their own languages and practicing their own cultures', 'Attending classes of any kind', 'Living in Canada', 'Wearing school uniforms'], 0),
    ('Why is the history of residential schools an important part of understanding Canadian history today?', ['It helps explain ongoing effects on Indigenous communities and the importance of reconciliation', 'It has no connection to present-day Canada', 'Residential schools had no lasting impact on families', 'This history is not taught or discussed in Canada'], 0),
    ('Why might learning about residential schools be connected to the work of the Truth and Reconciliation Commission?', ['The commission was created to document this history and support healing and reconciliation', 'The two topics have no relationship to each other', 'The commission was created before residential schools existed', 'Truth and reconciliation only apply to unrelated international events'], 0)]),
]),
day(142, [
L('Reading: Distinguishing Theme from Topic',
  'Grade 6 Language strand: a topic is what a text is about in a word or phrase, while a theme is the deeper message or lesson about life that the author conveys through the topic.',
  [('What is the difference between a topic and a theme?', ['A topic is what a text is about, while a theme is the deeper message the text conveys', 'A topic and a theme always mean exactly the same thing', 'A theme is only found in nonfiction texts', 'A topic is always longer than a theme'], 0),
   ('Which of these is most likely a topic rather than a theme?', ['Friendship', 'Loyalty grows through shared hardship', 'Courage often comes from unexpected places', 'True friendship requires honesty'], 0),
   ('In a story about a fox who learns to trust others, what would be the theme?', ['Trust can grow even after being hurt', 'Foxes', 'A forest setting', 'Animals in winter'], 0),
   ('How can a reader usually identify the theme of a story?', ['By considering what lesson the characters learn by the end', 'By counting the number of pages in the text', 'By looking only at the title of the story', 'By ignoring the characters actions entirely'], 0),
   ('Why might two different readers describe the theme of the same story in slightly different ways?', ['Readers can interpret the deeper meaning of a text differently based on their own perspective', 'Every reader must always identify the exact same theme', 'Theme is a fixed fact stated directly in every text', 'Only the author can correctly identify a theme'], 0)]),
M('Number Sense: Adding and Subtracting Mixed Numbers with Regrouping',
  'Grade 6 Math strand: adding or subtracting mixed numbers sometimes requires regrouping, which means converting a whole number into a fraction (or combining a fraction greater than one back into a whole number) to complete the calculation.',
  [('What does it mean to regroup when subtracting mixed numbers?', ['To convert a whole number into a fraction so subtraction is possible', 'To multiply both mixed numbers together', 'To ignore the fractional part of a mixed number', 'To round both mixed numbers to the nearest whole number'], 0),
   ('When might regrouping be necessary while subtracting mixed numbers?', ['When the fraction being subtracted is larger than the fraction it is subtracted from', 'When both fractions have the exact same denominator already', 'When mixed numbers are being multiplied, not subtracted', 'Regrouping is never needed with mixed numbers'], 0),
   ('What must be true of the denominators before adding two mixed numbers?', ['They must be the same, or converted to a common denominator', 'They must always be different from each other', 'They must always be equal to the whole number part', 'Denominators do not matter when adding mixed numbers'], 0),
   ('If adding the fractional parts of two mixed numbers produces a fraction greater than one, what should be done?', ['Convert the extra amount into a whole number and add it to the whole number part', 'Ignore the extra amount entirely', 'Discard the whole number parts of both mixed numbers', 'Multiply the result by two'], 0),
   ('Why is understanding regrouping important when working with mixed numbers?', ['It allows accurate addition and subtraction even when fractions do not divide evenly', 'Regrouping is only useful for whole numbers, never fractions', 'It removes the need to ever use fractions', 'Mixed numbers cannot be added or subtracted without a calculator'], 0)]),
Sc('Ecosystems: Carrying Capacity and Population Limits',
   'Grade 6 Science strand: carrying capacity is the maximum population size an ecosystem can support long-term based on available resources such as food, water, and shelter, and populations that exceed this limit often decline.',
   [('What is carrying capacity?', ['The maximum population size an ecosystem can support long-term', 'The total number of species living on Earth', 'The exact number of predators in an ecosystem', 'A measurement of how tall plants grow in an ecosystem'], 0),
    ('What factors help determine an ecosystems carrying capacity?', ['Available food, water, and shelter', 'Only the number of predators present', 'Only the size of the ecosystem in square kilometres', 'The colour of the animals living there'], 0),
    ('What often happens when a population exceeds an ecosystems carrying capacity?', ['The population tends to decline due to limited resources', 'The population grows forever with no limits', 'The ecosystem automatically creates more resources', 'Carrying capacity has no effect on population size'], 0),
    ('How might a drought affect the carrying capacity of a grassland ecosystem?', ['It could lower the carrying capacity by reducing available food and water', 'It would always increase the carrying capacity', 'Droughts have no effect on carrying capacity', 'It would only affect predators, not prey'], 0),
    ('Why is understanding carrying capacity important for wildlife management?', ['It helps determine how many animals an ecosystem can sustainably support', 'Carrying capacity has no practical use for managing wildlife', 'Wildlife populations never need to be managed', 'It only applies to ecosystems with no animals present'], 0)]),
SS('Social Studies: The Order of Canada — Honouring Outstanding Canadians',
   'Grade 6 Social Studies strand: the Order of Canada is one of the countrys highest civilian honours, awarded to individuals who have made outstanding contributions to the nation in fields such as the arts, science, community service, and public life.',
   [('What is the Order of Canada?', ['One of the countrys highest civilian honours', 'A branch of the Canadian military', 'A type of Canadian currency', 'A federal government department'], 0),
    ('Who typically receives the Order of Canada?', ['Individuals who have made outstanding contributions to Canada', 'Only elected members of Parliament', 'Only professional athletes', 'Only citizens of other countries'], 0),
    ('In what kinds of fields might someone earn the Order of Canada?', ['The arts, science, community service, and public life', 'Only professional cooking', 'Only video game design', 'Only weather forecasting'], 0),
    ('Why might a country create an honour like the Order of Canada?', ['To publicly recognize and celebrate significant contributions to society', 'Honours like this have no real purpose', 'To replace the need for elections', 'To reward only government employees'], 0),
    ('Why could receiving the Order of Canada inspire other Canadians?', ['It highlights meaningful ways ordinary people can make a lasting difference', 'Such honours discourage people from contributing to their communities', 'The award is never publicized to the Canadian public', 'It only recognizes achievements made outside of Canada'], 0)]),
]),
day(143, [
L('Writing: Writing an Acrostic Poem',
  'Grade 6 Language strand: an acrostic poem uses the letters of a word spelled vertically down the page, with each letter beginning a line that relates to the overall topic.',
  [('What is an acrostic poem?', ['A poem in which the first letters of each line spell out a word when read vertically', 'A poem that must rhyme in every line', 'A poem with exactly fourteen lines', 'A poem written entirely in one long sentence'], 0),
   ('If the word OCEAN is used for an acrostic poem, how many lines would the poem likely have?', ['Five', 'Three', 'Ten', 'Two'], 0),
   ('What should each line of an acrostic poem generally relate to?', ['The overall topic or subject of the poem', 'A completely unrelated random idea', 'Only the alphabet in order', 'Another poems title'], 0),
   ('Why might a writer choose an acrostic poem to describe a person?', ['It creatively highlights different qualities of that person using each letter of their name', 'It removes the need for any descriptive words', 'It always requires a strict rhyme scheme', 'It can only be used to describe objects, not people'], 0),
   ('What is one challenge a writer might face when composing an acrostic poem?', ['Finding words that both start with the correct letter and fit the poems meaning', 'Acrostic poems never present any challenge', 'Acrostic poems cannot include descriptive language', 'Every line must be exactly the same length'], 0)]),
M('Geometry: Surface Area of Cones',
  'Grade 6 Math strand: the surface area of a cone is the sum of the area of its circular base and the area of its curved lateral surface, giving the total area of all the surfaces that cover the shape.',
  [('What two parts make up the surface area of a cone?', ['The circular base and the curved lateral surface', 'Only the circular base, with no other surface', 'Only the apex point of the cone', 'The volume and the radius'], 0),
   ('What shape is the base of a cone?', ['A circle', 'A square', 'A triangle', 'A rectangle'], 0),
   ('What is the curved surface of a cone called?', ['The lateral surface', 'The base', 'The vertex', 'The diameter'], 0),
   ('Why is the surface area of a cone always measured in square units?', ['Because surface area measures a two-dimensional covering over a three-dimensional shape', 'Because cones have no measurable surface', 'Because square units apply only to volume', 'Because a cone has no circular base'], 0),
   ('Why might an ice cream cone wrapper need to be shaped to match the cones lateral surface?', ['So the flat wrapper can fold to cover the curved surface without gaps or overlap', 'Wrappers never need to match the shape they cover', 'Cones do not have a lateral surface to wrap', 'Surface area has no connection to real-world wrapping'], 0)]),
Sc('Simple Machines: The Wheel and Axle',
   'Grade 6 Science strand: a wheel and axle is a simple machine made of a large wheel attached to a smaller rod called an axle, which reduces the force needed to move or lift objects by rotating together.',
   [('What two parts make up a wheel and axle?', ['A large wheel attached to a smaller rod called an axle', 'Two identical wheels with no connecting rod', 'A ramp and a lever combined together', 'A rope threaded through a wheel'], 0),
    ('How does a wheel and axle make work easier?', ['It reduces the force needed to move or lift objects by rotating together', 'It always increases the total distance an object must travel', 'It removes the need for any force at all', 'It only works when lifting objects straight up'], 0),
    ('Which everyday object uses a wheel and axle?', ['A doorknob', 'A seesaw', 'A ramp leading into a building', 'A pair of scissors'], 0),
    ('Why does turning a large wheel make it easier to rotate a smaller axle?', ['A small force applied over a larger distance on the wheel creates a greater force on the axle', 'The wheel and axle always require the exact same amount of force', 'Turning the wheel has no effect on the axle', 'A wheel and axle cannot multiply force in any way'], 0),
    ('Why might a steering wheel in a car be considered a wheel and axle?', ['Turning the large wheel makes it easier to rotate the smaller steering column', 'A steering wheel has no connection to a rotating axle', 'Steering wheels never require any force to turn', 'A steering wheel is an example of a lever, not a wheel and axle'], 0)]),
SS('Social Studies: The Canadian Museum for Human Rights',
   'Grade 6 Social Studies strand: located in Winnipeg, the Canadian Museum for Human Rights is the first museum in the world solely dedicated to the evolution, celebration, and future of human rights, featuring exhibits on both Canadian and global human rights issues.',
   [('In which Canadian city is the Canadian Museum for Human Rights located?', ['Winnipeg', 'Toronto', 'Vancouver', 'Halifax'], 0),
    ('What makes the Canadian Museum for Human Rights unique in the world?', ['It was the first museum solely dedicated to the topic of human rights', 'It is the oldest museum in North America', 'It only displays objects related to Canadian sports history', 'It focuses exclusively on ancient civilizations'], 0),
    ('What kinds of topics might visitors learn about at the museum?', ['Canadian and global human rights issues', 'Only the history of Canadian currency', 'Only outer space exploration', 'Only ancient Egyptian artifacts'], 0),
    ('Why might a country choose to build a museum dedicated to human rights?', ['To educate the public and encourage reflection on rights and responsibilities', 'Museums have no role in educating the public', 'Human rights are not considered an important topic to teach', 'To avoid discussing difficult parts of history'], 0),
    ('Why might learning about human rights history help visitors understand present-day issues?', ['Understanding past struggles can provide context for ongoing human rights challenges', 'Past events have no connection to issues happening today', 'Human rights issues have never changed throughout history', 'Museums cannot connect historical and current events'], 0)]),
]),
day(144, [
L('Media Literacy: Recognizing Sponsored Content and Native Advertising',
  'Grade 6 Language strand: sponsored content and native advertising are paid promotions designed to look like regular articles or posts, making it important for readers to identify labels such as sponsored or ad before trusting the information.',
  [('What is sponsored content?', ['Paid promotional material designed to look like a regular article or post', 'A news story written without any payment involved', 'A government report on public spending', 'A personal diary entry shared online'], 0),
   ('What label might indicate that a post is native advertising?', ['Sponsored or Ad', 'Breaking News', 'Opinion', 'Editorial'], 0),
   ('Why is native advertising sometimes hard for readers to identify?', ['It is designed to blend in with the regular content around it', 'It is always printed in a bright red font', 'It only ever appears on television', 'It never contains any images'], 0),
   ('Why should a critical reader check whether an online article is sponsored?', ['Sponsored content may be biased toward promoting a product or service', 'Sponsored content is always more accurate than regular articles', 'Sponsored labels have no effect on how a reader should judge content', 'Only textbooks can ever be considered sponsored'], 0),
   ('What might motivate a company to pay for native advertising instead of a traditional ad?', ['It can reach readers who might otherwise ignore an obvious advertisement', 'Native advertising is always more expensive with no added benefit', 'Companies are legally required to disguise every advertisement', 'Native advertising cannot appear on social media'], 0)]),
M('Geometry: Finding the Midpoint and Length of a Line Segment',
  'Grade 6 Math strand: the midpoint of a line segment on a coordinate grid is the point exactly halfway between its two endpoints, and the length of a horizontal or vertical segment can be found by counting units or subtracting coordinates.',
  [('What is the midpoint of a line segment?', ['The point exactly halfway between the two endpoints', 'The point farthest from both endpoints', 'Either one of the two endpoints', 'A point that is never on the segment itself'], 0),
   ('What is the midpoint of a segment with endpoints at 2 and 8 on a number line?', ['5', '6', '4', '10'], 0),
   ('How can you find the length of a horizontal segment on a coordinate grid?', ['Subtract the smaller x-coordinate from the larger x-coordinate', 'Add both y-coordinates together', 'Multiply the two x-coordinates together', 'Count only the y-coordinates'], 0),
   ('What is the length of a horizontal segment from x equals 3 to x equals 9?', ['6 units', '12 units', '3 units', '9 units'], 0),
   ('Why is finding a midpoint a useful skill in coordinate geometry?', ['It helps locate the exact centre of a segment for tasks like bisecting or designing', 'Midpoints have no real use in mathematics', 'Midpoints can only be found using a ruler', 'Midpoints are identical to endpoints'], 0)]),
Sc('Nuclear Energy: How Nuclear Power Plants Generate Electricity',
   'Grade 6 Science strand: nuclear power plants generate electricity by splitting uranium atoms in a process called fission, which releases heat used to produce steam that spins turbines connected to generators.',
   [('What process do nuclear power plants use to release energy?', ['Fission, the splitting of uranium atoms', 'Photosynthesis, the process plants use to make food', 'Combustion of large amounts of coal', 'Evaporation of water in a cooling tower'], 0),
    ('What does the heat released during nuclear fission produce?', ['Steam, which is used to spin turbines', 'Sunlight, which powers solar panels', 'Wind, which spins wind turbines', 'Electricity directly, with no other steps'], 0),
    ('What connects the spinning turbines in a nuclear power plant to electricity production?', ['A generator', 'A wind vane', 'A solar panel', 'A battery'], 0),
    ('What is one advantage of nuclear energy compared to fossil fuels?', ['It produces electricity without directly releasing greenhouse gases during generation', 'It always requires burning large amounts of coal', 'It relies entirely on sunlight to function', 'It cannot generate large amounts of electricity'], 0),
    ('What is one challenge associated with nuclear power plants?', ['Safely storing and disposing of radioactive waste', 'Nuclear plants never produce any waste at all', 'Nuclear plants cannot generate electricity efficiently', 'Nuclear energy relies entirely on wind conditions'], 0)]),
SS('Social Studies: Canadas Provinces and Territories — Capitals and Regions',
   'Grade 6 Social Studies strand: Canada is made up of ten provinces and three territories, each with its own capital city, and understanding their locations and regional groupings helps build a clearer picture of the countrys geography.',
   [('How many provinces does Canada have?', ['Ten', 'Eight', 'Twelve', 'Thirteen'], 0),
    ('How many territories does Canada have?', ['Three', 'One', 'Five', 'Ten'], 0),
    ('What is the capital city of Ontario?', ['Toronto', 'Ottawa', 'Hamilton', 'Kingston'], 0),
    ('Which territory has Yellowknife as its capital?', ['The Northwest Territories', 'Yukon', 'Nunavut', 'British Columbia'], 0),
    ('Why is it useful to understand the regional groupings of Canadas provinces and territories?', ['It helps show patterns in geography, climate, and shared history across regions', 'Regional groupings have no connection to geography or history', 'Every province and territory is identical in climate and geography', 'Canada does not have any distinct regions'], 0)]),
]),
day(145, [
L('Grammar: Compound-Complex Sentences',
  'Grade 6 Language strand: a compound-complex sentence combines at least two independent clauses with at least one dependent clause, allowing writers to express multiple related ideas with varying levels of importance in a single sentence.',
  [('What makes a sentence compound-complex?', ['It combines at least two independent clauses with at least one dependent clause', 'It contains only a single independent clause', 'It never contains any punctuation', 'It always begins with a conjunction'], 0),
   ('Which sentence is compound-complex?', ['Although it was raining, we went outside, and we still had fun.', 'We went outside.', 'It was raining outside.', 'We had fun playing outside.'], 0),
   ('How many independent clauses does a compound-complex sentence need at minimum?', ['Two', 'Zero', 'Four', 'One'], 0),
   ('Why might a writer use a compound-complex sentence?', ['To connect several related ideas smoothly while showing their relative importance', 'To make writing shorter and less detailed', 'To avoid using any conjunctions', 'To remove all subordinate ideas from a sentence'], 0),
   ('What could happen if a compound-complex sentence is missing correct punctuation?', ['The sentence could become confusing or difficult for a reader to follow', 'The sentence would automatically become a simple sentence', 'The meaning of the sentence would always stay perfectly clear', 'Punctuation has no effect on compound-complex sentences'], 0)]),
M('Geometry: Naming and Classifying Polygons (Pentagons Through Decagons)',
  'Grade 6 Math strand: polygons are named according to their number of sides, ranging from a pentagon with five sides to a decagon with ten sides, and can be classified as regular or irregular based on whether all sides and angles are equal.',
  [('How many sides does a pentagon have?', ['Five', 'Four', 'Six', 'Eight'], 0),
   ('How many sides does a decagon have?', ['Ten', 'Seven', 'Nine', 'Twelve'], 0),
   ('What makes a polygon regular?', ['All of its sides and angles are equal', 'It has an odd number of sides', 'It cannot have any straight sides', 'It must always be a triangle'], 0),
   ('What is a polygon with seven sides called?', ['A heptagon', 'A hexagon', 'An octagon', 'A nonagon'], 0),
   ('Why might classifying polygons by their number of sides be useful in geometry?', ['It allows shapes to be identified and compared using a consistent naming system', 'Naming polygons has no practical use in geometry', 'All polygons must be named using the same single term', 'Polygons cannot be classified by their sides'], 0)]),
Sc('Monarch Butterfly Migration: A Multi-Generation Journey',
   'Grade 6 Science strand: monarch butterflies migrate thousands of kilometres between North America and central Mexico each year, with the return journey often completed across several generations of butterflies rather than by a single individual.',
   [('Where do monarch butterflies from eastern North America typically migrate to for the winter?', ['Central Mexico', 'Northern Canada', 'Antarctica', 'The Arctic Ocean'], 0),
    ('How is monarch migration different from many bird migrations?', ['The return journey is often completed across several generations of butterflies', 'A single monarch always completes the entire round-trip migration alone', 'Monarchs never migrate more than a few kilometres', 'Monarch migration happens underwater'], 0),
    ('Why do monarch butterflies migrate south for the winter?', ['To escape cold temperatures that they cannot survive', 'To find colder climates for hibernation', 'Monarchs do not actually migrate at all', 'To avoid sunlight during the winter months'], 0),
    ('What plant do monarch caterpillars depend on for food?', ['Milkweed', 'Oak leaves', 'Pine needles', 'Wheat'], 0),
    ('Why is the loss of milkweed habitat a concern for monarch populations?', ['Without milkweed, monarch caterpillars lose their only food source', 'Milkweed has no connection to monarch survival', 'Monarchs can survive equally well on any plant', 'Losing milkweed only affects adult butterflies, not caterpillars'], 0)]),
SS('Social Studies: How the Federal Government Creates a Budget',
   'Grade 6 Social Studies strand: each year, the federal government creates a budget that outlines planned spending and expected revenue, deciding how tax dollars will be used to fund programs such as healthcare, education, and infrastructure.',
   [('What does a federal budget outline?', ['Planned government spending and expected revenue', 'Only the salaries of elected officials', 'The results of the most recent election', 'A list of upcoming national holidays'], 0),
    ('Where does most of the money in a federal budget come from?', ['Taxes collected from individuals and businesses', 'Donations from other countries', 'Money borrowed exclusively from banks in other nations', 'Sales of government-owned artwork'], 0),
    ('What are examples of programs that a federal budget might help fund?', ['Healthcare, education, and infrastructure', 'Only professional sports teams', 'Only private businesses', 'Only entertainment television programs'], 0),
    ('Why might government departments compete for a share of the federal budget?', ['There is a limited amount of money to be divided among many important priorities', 'Every department automatically receives an unlimited amount of funding', 'Federal budgets do not need to divide money between departments', 'Budgets are created without any spending limits'], 0),
    ('Why is it important for citizens to understand how a federal budget is created?', ['It helps them understand how public money is raised and spent on their behalf', 'Citizens have no connection to how government money is spent', 'Federal budgets are always kept completely secret from the public', 'Understanding budgets has no relevance to everyday life'], 0)]),
]),
day(146, [
L('Oral Communication: Delivering an Elevator Pitch',
  'Grade 6 Language strand: an elevator pitch is a brief, persuasive speech that clearly and quickly explains an idea, project, or product, typically lasting no longer than the length of a short elevator ride.',
  [('What is an elevator pitch?', ['A brief, persuasive speech that quickly explains an idea', 'A lengthy formal report delivered over several days', 'A silent presentation with no spoken words', 'A private letter sent only to one person'], 0),
   ('About how long should an elevator pitch typically last?', ['Under a minute', 'Over an hour', 'A full school day', 'Several days'], 0),
   ('What is the main goal of an elevator pitch?', ['To quickly capture interest and clearly explain the key idea', 'To describe every possible detail of a topic', 'To confuse the listener with technical language', 'To avoid making eye contact with the listener'], 0),
   ('Why might a speaker practice an elevator pitch multiple times before delivering it?', ['To make the delivery sound confident, clear, and concise', 'Practicing makes a pitch longer and less clear', 'Elevator pitches should never be rehearsed', 'Practice has no effect on how a pitch sounds'], 0),
   ('Which of these would be most important to include in an elevator pitch about a new school club?', ['A clear, exciting summary of what the club does and why to join', 'A complete history of every club at the school', 'An unrelated story about an unrelated topic', 'A long list of unrelated statistics'], 0)]),
M('Data Management: Identifying Misleading Graphs',
  'Grade 6 Math strand: a graph can be misleading if its scale is manipulated, its axes are not labelled clearly, or only part of the data is shown, so critical readers should check these features before drawing conclusions.',
  [('What is one way a graph can be made misleading?', ['By manipulating the scale of the axis to exaggerate differences', 'By always starting the y-axis at exactly zero', 'By including a clear title and labelled axes', 'By showing all of the relevant data honestly'], 0),
   ('Why might a bar graph appear misleading if its y-axis does not start at zero?', ['It can make small differences between bars look much larger than they really are', 'It always makes every bar look exactly the same size', 'Starting an axis above zero never affects how a graph looks', 'It has no effect on how the data is perceived'], 0),
   ('What should a critical reader check before trusting a graph?', ['The scale, labels, and source of the data', 'Only the colours used in the graph', 'Only the title of the graph, ignoring all other features', 'Nothing, since all graphs are equally accurate'], 0),
   ('Why might someone intentionally create a misleading graph?', ['To make data appear to support a particular claim or opinion', 'Misleading graphs are always created purely by accident', 'Graphs cannot be used to support a claim or opinion', 'Every graph is required by law to be completely accurate'], 0),
   ('What is one way to make a graph more trustworthy and accurate?', ['Clearly label the axes and use a consistent, honest scale', 'Remove all labels from the axes', 'Choose a scale that exaggerates the data as much as possible', 'Leave out the source of the data entirely'], 0)]),
Sc('Deep-Sea Ecosystems and Hydrothermal Vents',
   'Grade 6 Science strand: hydrothermal vents are openings on the ocean floor that release heated, mineral-rich water, supporting unique deep-sea ecosystems where organisms rely on chemosynthesis instead of sunlight for energy.',
   [('What is a hydrothermal vent?', ['An opening on the ocean floor that releases heated, mineral-rich water', 'A type of underwater volcano that no longer produces heat', 'A structure built by humans to study the ocean', 'A shallow pool found along a beach'], 0),
    ('What process do organisms near hydrothermal vents use to produce energy instead of photosynthesis?', ['Chemosynthesis', 'Respiration', 'Evaporation', 'Condensation'], 0),
    ('Why cannot organisms near hydrothermal vents rely on photosynthesis?', ['Sunlight does not reach the deep ocean floor where vents are located', 'Photosynthesis requires no sunlight at all', 'Hydrothermal vents block all forms of energy production', 'Deep-sea organisms do not require any energy source'], 0),
    ('What is released from a hydrothermal vent that helps support nearby life?', ['Heated water rich in minerals and chemicals', 'Cold, mineral-free water', 'Sunlight reflected from the ocean surface', 'Oxygen produced by nearby plants'], 0),
    ('Why are hydrothermal vent ecosystems considered scientifically significant?', ['They show that life can thrive without relying on sunlight for energy', 'They prove that no life can survive in the deep ocean', 'They are identical to ecosystems found near the ocean surface', 'They contain no living organisms of any kind'], 0)]),
SS('Social Studies: The Numbered Treaties — Agreements Between Canada and First Nations',
   'Grade 6 Social Studies strand: between 1871 and 1921, the Canadian government signed a series of numbered treaties with First Nations across much of the country, agreements that involved land, resources, and promises that have shaped relationships between Canada and Indigenous peoples ever since.',
   [('What were the numbered treaties?', ['A series of agreements signed between the Canadian government and First Nations', 'A list of Canadian provinces in order of population', 'A set of laws about Canadian currency', 'An agreement between Canada and another country'], 0),
    ('During roughly what time period were the numbered treaties signed?', ['1871 to 1921', '1600 to 1650', '1950 to 1975', '2000 to 2010'], 0),
    ('What kinds of issues did the numbered treaties often address?', ['Land, resources, and promises made to First Nations', 'Only trade rules with other countries', 'Only immigration policy', 'Only rules about national holidays'], 0),
    ('Why do the numbered treaties continue to matter in Canada today?', ['They continue to shape legal and political relationships between Canada and Indigenous peoples', 'They have no ongoing effect on modern Canada', 'They were fully replaced by new agreements soon after being signed', 'Treaties from this period were never legally binding'], 0),
    ('Why might understanding the numbered treaties help explain present-day Indigenous rights discussions?', ['Many current rights and land discussions trace back to promises made in these treaties', 'These treaties have no connection to modern rights discussions', 'Indigenous rights issues began only in the twenty-first century', 'The numbered treaties were purely symbolic with no real terms'], 0)]),
]),
day(147, [
L('Vocabulary: Understanding Jargon and Technical Vocabulary',
  'Grade 6 Language strand: jargon refers to specialized words or phrases used within a particular field or group, and while it helps experts communicate precisely, it can confuse readers who are unfamiliar with the subject.',
  [('What is jargon?', ['Specialized vocabulary used within a particular field or group', 'Vocabulary that everyone understands equally well', 'Words that have no real meaning at all', 'Language used only in casual conversation'], 0),
   ('Which of these is an example of medical jargon?', ['Cardiovascular', 'Happy', 'Quickly', 'Table'], 0),
   ('Why might jargon confuse a general audience?', ['Readers unfamiliar with the field may not know the specialized meaning of the words', 'Jargon is always identical to everyday language', 'Every reader automatically understands all jargon', 'Jargon never appears in written texts'], 0),
   ('What might a writer do to help a general audience understand necessary jargon?', ['Define or explain the term clearly the first time it is used', 'Use as much unexplained jargon as possible', 'Avoid explaining any specialized terms', 'Remove all vocabulary related to the topic'], 0),
   ('Why might experts in a field continue to use jargon among themselves?', ['It allows them to communicate complex ideas precisely and efficiently', 'Jargon always slows down communication between experts', 'Experts are required by law to avoid jargon', 'Jargon has no useful purpose among experts'], 0)]),
M('Probability: Calculating Expected Value',
  'Grade 6 Math strand: expected value is the average outcome of a probability experiment if it were repeated many times, calculated by multiplying each possible outcome by its probability and adding the results together.',
  [('What does expected value represent?', ['The average outcome of an experiment if it were repeated many times', 'The single outcome that will always occur every time', 'The largest possible outcome in an experiment', 'A value that has no connection to probability'], 0),
   ('How is expected value calculated?', ['By multiplying each outcome by its probability and adding the results', 'By adding all possible outcomes without using probability', 'By dividing the number of outcomes by two', 'By choosing the most frequent outcome only'], 0),
   ('If a game has a fifty percent chance of winning ten points and a fifty percent chance of winning zero points, what is the expected value?', ['Five points', 'Ten points', 'Zero points', 'Twenty points'], 0),
   ('Why might a business use expected value when making decisions?', ['To estimate the average result of a decision involving uncertain outcomes', 'Expected value has no use in real-world decision making', 'Expected value only applies to games with dice', 'Businesses never need to consider probability'], 0),
   ('Why does expected value not need to match any single actual outcome?', ['It represents an average over many repeated trials, not one single result', 'Expected value must always match the very first outcome observed', 'Expected value is only calculated after an experiment ends', 'Every trial of an experiment always produces the expected value exactly'], 0)]),
Sc('The Science of Sunscreen and UV Radiation',
   'Grade 6 Science strand: sunscreen works by absorbing or reflecting ultraviolet (UV) radiation from the Sun, helping protect skin from sunburn and long-term damage caused by overexposure to UV rays.',
   [('What does sunscreen help protect the skin from?', ['Ultraviolet (UV) radiation from the Sun', 'Ordinary visible light only', 'Sound waves in the environment', 'Changes in air pressure'], 0),
    ('How does sunscreen generally work?', ['By absorbing or reflecting UV radiation before it damages the skin', 'By completely blocking all forms of light from reaching the skin', 'By increasing the skins exposure to UV radiation', 'By changing the colour of UV radiation'], 0),
    ('What can happen to skin after too much unprotected exposure to UV radiation?', ['Sunburn and long-term skin damage', 'Immediate and permanent healing of the skin', 'No effect on the skin whatsoever', 'A decrease in skin temperature'], 0),
    ('What part of the electromagnetic spectrum does UV radiation belong to?', ['A range with more energy than visible light', 'A range with less energy than radio waves only', 'Sound waves, not electromagnetic waves', 'A form of radiation invented by humans'], 0),
    ('Why might sunscreen need to be reapplied throughout the day?', ['Its protective effectiveness can decrease over time or wash away with water and sweat', 'Sunscreen protection lasts permanently after a single application', 'Reapplying sunscreen has no effect on its protection', 'UV radiation only exists in the morning hours'], 0)]),
SS('Social Studies: The Canadian Coast Guard and Maritime Safety',
   'Grade 6 Social Studies strand: the Canadian Coast Guard is a federal agency responsible for maritime search and rescue, icebreaking, and ensuring safe navigation along Canadas extensive coastlines and waterways.',
   [('What is the main role of the Canadian Coast Guard?', ['Maritime search and rescue and ensuring safe navigation', 'Enforcing traffic laws on highways', 'Managing national parks and forests', 'Collecting federal income taxes'], 0),
    ('What service does the Coast Guard provide in icy northern waters?', ['Icebreaking to keep waterways clear for ships', 'Building bridges across rivers', 'Constructing new highways', 'Managing airport security'], 0),
    ('Why does Canada need a strong coast guard presence?', ['Canada has an extensive coastline that requires monitoring and safety support', 'Canada has no coastline requiring protection', 'Ships never travel through Canadian waters', 'Maritime safety is not a concern in Canada'], 0),
    ('What might the Coast Guard do if a boat gets into trouble at sea?', ['Conduct a search and rescue operation to help those in danger', 'Ignore the situation entirely', 'Only respond if requested by another country', 'Wait several weeks before responding'], 0),
    ('Why is icebreaking an important service for northern Canadian communities?', ['It helps keep shipping routes open for supplies and transportation', 'Icebreaking has no benefit for northern communities', 'Ice never affects shipping routes in Canada', 'Northern communities do not rely on shipping routes'], 0)]),
]),
day(148, [
L('Writing: Writing a Letter to the Editor',
  'Grade 6 Language strand: a letter to the editor is a persuasive letter written to a newspaper or magazine expressing an opinion on a current issue, aiming to inform or influence public opinion.',
  [('What is the purpose of a letter to the editor?', ['To express an opinion on a current issue and influence public opinion', 'To report neutral sports scores with no opinion included', 'To summarize an entire novel chapter by chapter', 'To provide a private message meant for only one reader'], 0),
   ('Where is a letter to the editor typically published?', ['In a newspaper or magazine', 'In a private diary', 'On a restaurant menu', 'In a phone book'], 0),
   ('What should a strong letter to the editor include?', ['A clear opinion supported with reasons and evidence', 'Only vague statements with no supporting details', 'A list of unrelated random facts', 'No clear opinion at all'], 0),
   ('Why might a writer include a call to action at the end of a letter to the editor?', ['To encourage readers to think about or respond to the issue', 'Calls to action are never included in persuasive writing', 'A call to action always weakens a persuasive letter', 'Letters to the editor cannot include suggestions'], 0),
   ('Why do newspapers often publish letters to the editor from members of the public?', ['To share a range of community perspectives on current issues', 'Newspapers are required to publish every letter they receive unchanged', 'Letters to the editor are always written by professional journalists', 'Public opinion has no place in a newspaper'], 0)]),
M('Financial Literacy: Comparing Cell Phone and Subscription Plans',
  'Grade 6 Math strand: comparing cell phone or subscription plans involves analyzing monthly costs, included features, and extra fees to determine which option offers the best value over time.',
  [('What should be compared when choosing between two subscription plans?', ['Monthly costs, included features, and extra fees', 'Only the colour of the companys logo', 'Only how many advertisements a company shows', 'Nothing, since all plans always cost the same'], 0),
   ('If Plan A costs 20 dollars a month and Plan B costs 15 dollars a month with the same features, which plan offers better value?', ['Plan B', 'Plan A', 'Both plans offer identical value', 'Neither plan offers any value'], 0),
   ('Why might a plan with a lower monthly price not always be the best deal?', ['It may include fewer features or have hidden extra fees', 'Lower monthly prices always guarantee the best possible deal', 'Extra fees never affect the total cost of a plan', 'Features included in a plan never vary between companies'], 0),
   ('How could you calculate the total yearly cost of a monthly subscription plan?', ['Multiply the monthly cost by twelve', 'Divide the monthly cost by twelve', 'Add twelve to the monthly cost', 'Subtract twelve from the monthly cost'], 0),
   ('Why is it useful to compare the cost per feature when evaluating subscription plans?', ['It helps determine which plan provides more value for the money spent', 'Cost per feature is impossible to calculate', 'Every subscription plan provides the exact same features', 'Comparing costs has no impact on making a wise financial choice'], 0)]),
Sc('Earthquake-Resistant Building Design',
   'Grade 6 Science strand: engineers design earthquake-resistant buildings using features such as flexible materials, deep foundations, and shock-absorbing systems that allow a structure to move and absorb energy during an earthquake instead of collapsing.',
   [('What is the main goal of earthquake-resistant building design?', ['To allow a structure to absorb energy and move without collapsing', 'To make a building completely immovable during an earthquake', 'To prevent all buildings from ever being built in earthquake zones', 'To increase the amount of damage caused during an earthquake'], 0),
    ('What type of materials are often used in earthquake-resistant buildings?', ['Flexible materials that can bend and absorb energy', 'Materials that are as rigid and brittle as possible', 'Materials that shatter easily under stress', 'Materials that cannot be reinforced in any way'], 0),
    ('What is one feature that helps a building absorb shock during an earthquake?', ['Shock-absorbing systems built into the structure', 'Removing the buildings foundation entirely', 'Building with the tallest possible unsupported walls', 'Using only glass for every wall'], 0),
    ('Why might engineers design deep foundations for buildings in earthquake-prone areas?', ['To help anchor and stabilize the structure during ground movement', 'Deep foundations have no effect on a buildings stability', 'Foundations are not necessary for earthquake resistance', 'Deep foundations make a building more likely to collapse'], 0),
    ('Why is earthquake-resistant design especially important for hospitals and schools?', ['These buildings must remain safe and functional to protect large numbers of people during a disaster', 'Hospitals and schools are never affected by earthquakes', 'Earthquake design only matters for very tall skyscrapers', 'Public buildings do not require special safety design'], 0)]),
SS('Social Studies: Black Loyalists and Early Black Settlement in Canada',
   'Grade 6 Social Studies strand: after the American Revolution, thousands of Black Loyalists, many of whom had been formerly enslaved, resettled in British North America, particularly Nova Scotia, forming some of the earliest free Black communities in what is now Canada.',
   [('Who were the Black Loyalists?', ['Black settlers, many formerly enslaved, who resettled in British North America after the American Revolution', 'A group of soldiers who fought only in the War of 1812', 'Explorers who first mapped the Canadian Arctic', 'A group of settlers who arrived only in the twentieth century'], 0),
    ('Which region became a major destination for Black Loyalists?', ['Nova Scotia', 'Alberta', 'The Northwest Territories', 'Yukon'], 0),
    ('What historical event led many Black Loyalists to resettle in British North America?', ['The American Revolution', 'The Klondike Gold Rush', 'The Confederation of Canada', 'The construction of the Canadian Pacific Railway'], 0),
    ('What significance did early Black Loyalist communities have in Canadian history?', ['They formed some of the earliest free Black communities in what is now Canada', 'They had no lasting impact on Canadian history', 'They settled exclusively in present-day Quebec', 'They arrived after Canada became a country'], 0),
    ('Why is learning about Black Loyalist history important to understanding Canadas early settlement patterns?', ['It highlights the diverse groups of people who shaped early Canadian communities', 'Early Canadian settlement involved only one group of people', 'Black Loyalist history has no connection to Canadian settlement', 'This history took place entirely outside of Canada'], 0)]),
]),
day(149, [
L('Reading: Analyzing Setting and Its Effect on Mood',
  'Grade 6 Language strand: setting includes the time and place of a story, and a skilled author uses details about setting to create a particular mood, the emotional atmosphere a reader feels while reading.',
  [('What is the setting of a story?', ['The time and place in which the story occurs', 'The main problem the characters must solve', 'The list of characters in the story', 'The authors personal opinion about the story'], 0),
   ('What is mood in a story?', ['The emotional atmosphere a reader feels while reading', 'The exact number of pages in a story', 'The grammatical structure of a sentence', 'The publishing date of a book'], 0),
   ('A story set in a dark, abandoned house at midnight would most likely create what mood?', ['A tense or eerie mood', 'A cheerful, sunny mood', 'A calm, relaxing mood', 'A humorous, silly mood'], 0),
   ('How might an author use setting details to build mood?', ['By choosing descriptive words about the time and place that evoke a certain feeling', 'By avoiding any description of the storys location', 'By listing only the characters names', 'By removing the setting from the story entirely'], 0),
   ('Why might the same event feel different to a reader depending on its setting?', ['The details of a setting can shape the emotional tone surrounding an event', 'Setting never has any impact on how an event feels', 'Every setting creates the exact same mood in every story', 'Only characters, not settings, can influence mood'], 0)]),
M('Measurement: Precision and Accuracy in Measurement',
  'Grade 6 Math strand: accuracy describes how close a measurement is to the true value, while precision describes how consistent repeated measurements are with each other, and both depend on the tools and care used when measuring.',
  [('What does accuracy describe in measurement?', ['How close a measurement is to the true value', 'How many times a measurement is repeated', 'The colour of the measuring tool used', 'The units used to record a measurement'], 0),
   ('What does precision describe in measurement?', ['How consistent repeated measurements are with each other', 'How close a single measurement is to the true value', 'The total number of measuring tools available', 'The exact date a measurement was taken'], 0),
   ('Can a set of measurements be precise but not accurate?', ['Yes, if the measurements are consistent with each other but far from the true value', 'No, precision and accuracy always mean exactly the same thing', 'No, precise measurements are always accurate as well', 'Yes, but only when using a digital tool'], 0),
   ('What might cause a measurement to be inaccurate even if it is precise?', ['A measuring tool that is not properly calibrated', 'Using the exact same tool for every measurement', 'Recording measurements in consistent units', 'Repeating a measurement multiple times'], 0),
   ('Why is it important for scientists to use both accurate and precise measurements?', ['Reliable data depends on measurements that are both close to the true value and consistent', 'Only accuracy matters in scientific measurement, never precision', 'Only precision matters in scientific measurement, never accuracy', 'Accuracy and precision have no effect on the reliability of data'], 0)]),
Sc('Blood Types and Blood Donation',
   'Grade 6 Science strand: human blood is classified into different types, such as A, B, AB, and O, based on markers on red blood cells, and understanding blood types is essential for safe blood transfusions and donation.',
   [('What are the four main human blood types?', ['A, B, AB, and O', 'X, Y, Z, and W', 'Red, blue, green, and yellow', 'One, two, three, and four'], 0),
    ('What determines a persons blood type?', ['Markers found on the surface of red blood cells', 'The colour of a persons skin', 'The persons age at the time of testing', 'The amount of water in a persons body'], 0),
    ('Why is it important to match blood types before a transfusion?', ['Mismatched blood types can cause a dangerous immune reaction in the body', 'Blood type has no effect on the safety of a transfusion', 'All blood types are always compatible with each other', 'Transfusions never require checking blood type'], 0),
    ('Which blood type is often referred to as a universal donor?', ['O negative', 'AB positive', 'B negative', 'A positive'], 0),
    ('Why do hospitals rely on regular blood donations from healthy volunteers?', ['Blood cannot be manufactured artificially and is needed for patient transfusions', 'Hospitals never require blood donations from the public', 'Donated blood is only ever used for scientific research', 'Blood donation has no medical purpose'], 0)]),
SS('Social Studies: Canadas Role in the Korean War',
   'Grade 6 Social Studies strand: Canada sent thousands of troops as part of a United Nations force during the Korean War from 1950 to 1953, helping defend South Korea, a conflict now sometimes called Canadas Forgotten War.',
   [('What international organization led the coalition Canada joined during the Korean War?', ['The United Nations', 'The League of Nations', 'The European Union', 'The British Commonwealth alone'], 0),
    ('During which years did the Korean War take place?', ['1950 to 1953', '1914 to 1918', '1939 to 1945', '1960 to 1965'], 0),
    ('Which country did Canadian troops help defend during the Korean War?', ['South Korea', 'North Korea', 'Japan', 'China'], 0),
    ('Why is the Korean War sometimes called Canadas Forgotten War?', ['It received less public attention and recognition than the World Wars', 'It is the most well-remembered war in Canadian history', 'No Canadian soldiers took part in the conflict', 'The war lasted only a single day'], 0),
    ('Why might it be important to remember Canadian involvement in conflicts like the Korean War?', ['It honours the service and sacrifice of Canadian soldiers often overlooked in history', 'Remembering past conflicts serves no educational purpose', 'Canada has never participated in any international conflicts', 'Only World Wars are worth studying in Canadian history'], 0)]),
]),
day(150, [
L('Language Review: Sentences, Style, and Reading Skills',
  'Grade 6 Language strand review: students revisit interjections, theme versus topic, acrostic poems, compound-complex sentences, and how setting shapes mood.',
  [('What is an interjection?', ['A word or phrase that expresses strong or sudden emotion', 'A word that joins two clauses together', 'A pronoun that replaces a noun', 'A verb that shows action'], 0),
   ('What is the difference between a topic and a theme?', ['A topic is what a text is about, while a theme is the deeper message the text conveys', 'A topic and a theme always mean exactly the same thing', 'A theme is only found in nonfiction texts', 'A topic is always longer than a theme'], 0),
   ('What is an acrostic poem?', ['A poem in which the first letters of each line spell out a word when read vertically', 'A poem that must rhyme in every line', 'A poem with exactly fourteen lines', 'A poem written entirely in one long sentence'], 0),
   ('What makes a sentence compound-complex?', ['It combines at least two independent clauses with at least one dependent clause', 'It contains only a single independent clause', 'It never contains any punctuation', 'It always begins with a conjunction'], 0),
   ('What is mood in a story?', ['The emotional atmosphere a reader feels while reading', 'The exact number of pages in a story', 'The grammatical structure of a sentence', 'The publishing date of a book'], 0)]),
M('Math Review: Algebra, Geometry, and Data',
  'Grade 6 Math strand review: students revisit combining like terms, surface area of cones, the midpoint of a line segment, naming polygons, and identifying misleading graphs.',
  [('What are like terms?', ['Terms that have the same variable raised to the same power', 'Terms that always have the same numerical coefficient', 'Any two terms found in the same expression', 'Terms that contain no variables at all'], 0),
   ('What two parts make up the surface area of a cone?', ['The circular base and the curved lateral surface', 'Only the circular base, with no other surface', 'Only the apex point of the cone', 'The volume and the radius'], 0),
   ('What is the midpoint of a line segment?', ['The point exactly halfway between the two endpoints', 'The point farthest from both endpoints', 'Either one of the two endpoints', 'A point that is never on the segment itself'], 0),
   ('How many sides does a decagon have?', ['Ten', 'Seven', 'Nine', 'Twelve'], 0),
   ('What is one way a graph can be made misleading?', ['By manipulating the scale of the axis to exaggerate differences', 'By always starting the y-axis at exactly zero', 'By including a clear title and labelled axes', 'By showing all of the relevant data honestly'], 0)]),
Sc('Science Review: Energy, Ecosystems, and Human Body',
   'Grade 6 Science strand review: students revisit biomass energy, carrying capacity, the wheel and axle, nuclear energy, and human blood types.',
   [('What is biomass energy made from?', ['Organic material such as wood, crop waste, or plant matter', 'Only fossil fuels formed over millions of years', 'Nuclear reactions inside a power plant', 'Wind passing through a turbine'], 0),
    ('What is carrying capacity?', ['The maximum population size an ecosystem can support long-term', 'The total number of species living on Earth', 'The exact number of predators in an ecosystem', 'A measurement of how tall plants grow in an ecosystem'], 0),
    ('What two parts make up a wheel and axle?', ['A large wheel attached to a smaller rod called an axle', 'Two identical wheels with no connecting rod', 'A ramp and a lever combined together', 'A rope threaded through a wheel'], 0),
    ('What process do nuclear power plants use to release energy?', ['Fission, the splitting of uranium atoms', 'Photosynthesis, the process plants use to make food', 'Combustion of large amounts of coal', 'Evaporation of water in a cooling tower'], 0),
    ('What are the four main human blood types?', ['A, B, AB, and O', 'X, Y, Z, and W', 'Red, blue, green, and yellow', 'One, two, three, and four'], 0)]),
SS('Social Studies Review: Reconciliation, Government, and Canadian History',
   'Grade 6 Social Studies strand review: students revisit residential schools, the Order of Canada, federal budgets, the numbered treaties, and Canadas role in the Korean War.',
   [('What were residential schools in Canada designed to do?', ['Forcibly remove Indigenous children from their families and assimilate them', 'Provide optional after-school tutoring for all Canadian children', 'Teach Indigenous languages and cultural traditions', 'Offer free summer camps for Canadian families'], 0),
    ('What is the Order of Canada?', ['One of the countrys highest civilian honours', 'A branch of the Canadian military', 'A type of Canadian currency', 'A federal government department'], 0),
    ('What does a federal budget outline?', ['Planned government spending and expected revenue', 'Only the salaries of elected officials', 'The results of the most recent election', 'A list of upcoming national holidays'], 0),
    ('What were the numbered treaties?', ['A series of agreements signed between the Canadian government and First Nations', 'A list of Canadian provinces in order of population', 'A set of laws about Canadian currency', 'An agreement between Canada and another country'], 0),
    ('What international organization led the coalition Canada joined during the Korean War?', ['The United Nations', 'The League of Nations', 'The European Union', 'The British Commonwealth alone'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_141_150)
    append_to(6, g6_141_150)
