#!/usr/bin/env python3
"""Grade 5, Days 111-120 -- extends Grade 5 from 110 to 120 days. Modeled
exactly on gen_grade5_days101_110.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 5 Days 1-110
topics (see data/grade5.json), which already densely cover nearly the
entire grade 5 curriculum across all four subjects. New topics: modal
verbs, biography/memoir writing, primary/secondary sources, website
credibility, formal debate, interview writing, parody, and number
prefixes for Language; scatter plots, compound interest, cylinder surface
area, cone/pyramid volume, the four-quadrant coordinate plane,
combinations, writing algebraic expressions, 12/24-hour time conversion,
and similar triangles for Math; comets/asteroids, eclipses, tides,
photosynthesis, dental health, DNA, cells, and renewable energy in focus
(solar, then wind/hydro) for Science; and the census, sister cities,
Indigenous language revitalization, the Auditor General, the national
debt/deficit, electoral ridings, equalization payments, national historic
sites, and the Magna Carta's influence on Canadian law for Social Studies
-- none of those exact ideas appear in Days 1-110. Day 120 is a review
day across all four subjects, matching the end-of-batch pattern used in
every prior 10-day batch. No embedded ASCII double-quote characters are
used anywhere in question/summary/option text; apostrophes are avoided or
use the curly Unicode form, matching the rest of Grade 5.
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


def _rebalance_answer_positions(days, seed=20260730):
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


g5_111_120 = [
day(111, [
L('Grammar: Modal Verbs',
  'Grade 5 Language strand: modal verbs like can, could, should, must, and might express ability, possibility, permission, or necessity, and change the meaning of the main verb they accompany.',
  [('Which of these is a modal verb?', ['Should', 'Running', 'Quickly', 'Happy'], 0),
   ('What does the modal verb must often express?', ['Necessity or strong obligation', 'Pure possibility', 'Past tense only', 'A question mark'], 0),
   ('What does the modal verb might express?', ['Possibility', 'Certainty', 'A command', 'A greeting'], 0),
   ('In the sentence You should study tonight, what does should express?', ['Advice or recommendation', 'Absolute certainty', 'A question', 'Past action'], 0),
   ('Which sentence uses a modal verb correctly?', ['She can swim very well.', 'She cans swim very well.', 'She canning swim.', 'She swum can well.'], 0)]),
M('Data Management: Scatter Plots and Correlation',
  'Grade 5 Math strand: a scatter plot displays pairs of related data as points on a graph, helping students see whether there is a correlation, or relationship, between the two variables.',
  [('What does a scatter plot show?', ['Pairs of related data as points on a graph', 'A single number', 'Only categories', 'A list of names'], 0),
   ('What does correlation mean in data?', ['A relationship between two variables', 'A single isolated fact', 'The colour of a graph', 'The title of a graph'], 0),
   ('If points on a scatter plot trend upward together, what kind of correlation is shown?', ['A positive correlation', 'A negative correlation', 'No correlation', 'An impossible correlation'], 0),
   ('If one variable increases while the other decreases, what correlation is shown?', ['A negative correlation', 'A positive correlation', 'No correlation', 'A perfect match'], 0),
   ('Why are scatter plots useful?', ['They help identify trends and relationships between two variables', 'They only show a single value', 'They cannot show any trend', 'They are used only for shapes'], 0)]),
Sc('Comets and Asteroids — Visitors from Space',
   'Grade 5 Science strand: comets are icy space objects that develop a glowing tail near the sun, while asteroids are rocky objects, and both orbit the sun like planets.',
   [('What is a comet mostly made of?', ['Ice and dust', 'Solid metal only', 'Water alone', 'Living organisms'], 0),
    ('What forms a comets glowing tail?', ['Ice and dust heated by the sun', 'Reflected moonlight only', 'Fire from the comets core', 'Nothing, comets have no tail'], 0),
    ('What is an asteroid mostly made of?', ['Rock and metal', 'Ice only', 'Gas only', 'Water only'], 0),
    ('Where are many asteroids found in our solar system?', ['In a belt between Mars and Jupiter', 'Inside the sun', 'On Earths surface', 'Inside the Moon'], 0),
    ('Do comets and asteroids orbit the sun?', ['Yes', 'No, they float randomly', 'Only comets do', 'Only asteroids do'], 0)]),
SS('The Census — Counting Everyone in Canada',
   'Grade 5 Social Studies strand: a census is an official count of everyone living in Canada, conducted regularly to help the government plan services and understand the population.',
   [('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('Why does the Canadian government conduct a census?', ['To help plan services and understand the population', 'To sell products', 'To have no reason', 'To confuse citizens'], 0),
    ('How often is the Canadian census typically taken?', ['At regular intervals, such as every five years', 'Every single day', 'Only once ever', 'Never'], 0),
    ('Which service might benefit from census information?', ['Planning new schools and hospitals', 'Painting a fence', 'Selling candy', 'Playing a game'], 0),
    ('A census helps a government understand ___.', ['How many people live in different areas', 'The weather forecast', 'Sports scores', 'Movie ratings'], 0)]),
]),
day(112, [
L('Writing: Writing a Biography',
  'Grade 5 Language strand: a biography tells the true story of a real persons life, written by someone else, organized chronologically and focused on key achievements and events.',
  [('What is a biography?', ['The true story of a real persons life written by someone else', 'A made-up story', 'A story about yourself', 'A type of poem'], 0),
   ('How is a biography typically organized?', ['Chronologically, following the persons life in order', 'Randomly, with no order', 'Backwards from death to birth only', 'Alphabetically by topic'], 0),
   ('What does a biography usually focus on?', ['Key achievements and important events in a persons life', 'Only their childhood', 'Only their favourite foods', 'Fictional adventures'], 0),
   ('Who writes a biography?', ['Someone other than the subject of the biography', 'Always the subject themselves', 'No one, it is never written', 'Only historians who knew the person personally'], 0),
   ('Which is an example of a biography topic?', ['The life story of a famous scientist', 'A recipe for cookies', 'A weather report', 'A grocery list'], 0)]),
M('Financial Literacy: Compound Interest — How Money Grows Faster',
  'Grade 5 Math strand: compound interest means earning interest not just on the original amount saved, but also on the interest already earned, helping savings grow faster over time.',
  [('What is compound interest?', ['Interest earned on both the original amount and previously earned interest', 'Interest earned only once', 'A type of tax', 'Money that is lost over time'], 0),
   ('How does compound interest differ from simple interest?', ['It grows on both the principal and prior interest', 'It never grows', 'It is always smaller than simple interest', 'It only applies to loans'], 0),
   ('Why might compound interest help savings grow faster over time?', ['Interest is continually added to a growing balance', 'It removes money from an account', 'It stays the same value always', 'It cancels out any savings'], 0),
   ('If you leave money in an account longer with compound interest, what generally happens?', ['It grows more', 'It always shrinks', 'It stays exactly the same', 'It disappears'], 0),
   ('Compound interest is often used to describe how ___ can grow over time.', ['Savings accounts', 'Weather patterns', 'Sports scores', 'Traffic patterns'], 0)]),
Sc('Eclipses — Solar and Lunar',
   'Grade 5 Science strand: a solar eclipse occurs when the Moon passes between the sun and Earth, while a lunar eclipse occurs when Earth passes between the sun and the Moon.',
   [('What happens during a solar eclipse?', ['The Moon passes between the sun and Earth', 'Earth passes between the sun and the Moon', 'The sun disappears forever', 'Nothing unusual happens'], 0),
    ('What happens during a lunar eclipse?', ['Earth passes between the sun and the Moon', 'The Moon passes between the sun and Earth', 'The Moon disappears forever', 'The sun moves closer to Earth'], 0),
    ('Why does a solar eclipse only happen occasionally?', ['The Moon, sun, and Earth must align precisely', 'It happens every single day', 'It never actually happens', 'The Moon controls when it happens randomly'], 0),
    ('During a total lunar eclipse, the Moon can appear ___.', ['Reddish, sometimes called a blood moon', 'Completely invisible with no colour', 'Bright blue', 'Twice its normal size'], 0),
    ('Why should people avoid looking directly at a solar eclipse without protection?', ['It can damage their eyes', 'It has no effect on the eyes', 'It makes the eclipse disappear', 'It is required to look directly at it'], 0)]),
SS('Sister Cities — Twin Communities Around the World',
   'Grade 5 Social Studies strand: sister cities are communities in different countries that form a special partnership to share culture, ideas, and friendship, strengthening global connections.',
   [('What is a sister city?', ['A partner community in another country', 'A city with no people', 'A type of building', 'A kind of holiday'], 0),
    ('Why might two cities become sister cities?', ['To share culture, ideas, and friendship', 'To compete against each other', 'To ignore one another', 'To close their borders'], 0),
    ('What might sister cities share with each other?', ['Cultural events and ideas', 'Nothing at all', 'Only complaints', 'Weather patterns only'], 0),
    ('How can a sister city partnership benefit a community?', ['It builds global connections and cultural understanding', 'It has no benefits', 'It isolates the community further', 'It replaces local government'], 0),
    ('Sister city partnerships can help students learn about ___.', ['Other cultures and communities around the world', 'Only their own city', 'Nothing new', 'Weather forecasting'], 0)]),
]),
day(113, [
L('Writing: Writing a Memoir',
  'Grade 5 Language strand: a memoir is a personal narrative in which the author reflects on a meaningful memory or period of their own life, focusing on emotions and personal significance.',
  [('What is a memoir?', ['A personal narrative reflecting on a meaningful memory from the authors own life', 'A made-up fantasy story', 'A biography of someone else', 'A dictionary entry'], 0),
   ('What does a memoir typically focus on?', ['Emotions and personal significance of a memory', 'Only historical dates', 'Only scientific facts', 'A stranger'], 0),
   ('Who writes a memoir?', ['The person about their own life', 'Always someone else about another person', 'No one', 'Only professional historians'], 0),
   ('How is a memoir different from an autobiography?', ['A memoir often focuses on a specific period or theme rather than an entire life', 'They are always identical', 'A memoir is always fictional', 'An autobiography is always shorter'], 0),
   ('Which is an example of a memoir topic?', ['A meaningful summer spent with a grandparent', 'A math formula', 'A weather chart', 'An imaginary dragon'], 0)]),
M('Geometry: Surface Area of a Cylinder',
  'Grade 5 Math strand: the surface area of a cylinder is found by adding the areas of its two circular ends and the area of its curved side, which unrolls into a rectangle.',
  [('What shape are the two ends of a cylinder?', ['Circles', 'Squares', 'Triangles', 'Rectangles'], 0),
   ('What shape does the curved side of a cylinder become when unrolled?', ['A rectangle', 'A triangle', 'A circle', 'A pentagon'], 0),
   ('To find the surface area of a cylinder, you need the areas of ___.', ['Both circular ends and the curved side', 'Only one circular end', 'Only the curved side', 'Only the height'], 0),
   ('What two measurements are needed to calculate a cylinders surface area?', ['Radius and height', 'Only the radius', 'Only the height', 'Only the diameter'], 0),
   ('Surface area is measured in ___.', ['Square units', 'Cubic units', 'Linear units only', 'No units at all'], 0)]),
Sc('Tides — The Moons Pull on Earths Oceans',
   'Grade 5 Science strand: tides are the rise and fall of ocean water levels, caused mainly by the gravitational pull of the Moon on Earths oceans.',
   [('What causes most of Earths tides?', ['The gravitational pull of the Moon', 'The wind alone', 'The colour of the ocean', 'Fish swimming'], 0),
    ('What are tides?', ['The rise and fall of ocean water levels', 'A type of storm', 'A kind of current only', 'A type of fish migration'], 0),
    ('What do we call the highest point of a tide?', ['High tide', 'Low tide', 'No tide', 'Flat tide'], 0),
    ('What do we call the lowest point of a tide?', ['Low tide', 'High tide', 'Full tide', 'Middle tide'], 0),
    ('Besides the Moon, what else can influence tides?', ['The suns gravity, to a lesser extent', 'Only clouds', 'Only wind direction', 'Only fish populations'], 0)]),
SS('Revitalizing Indigenous Languages',
   'Grade 5 Social Studies strand: many Indigenous communities in Canada are working to revitalize their traditional languages, which were historically suppressed, through education and community programs.',
   [('What does it mean to revitalize a language?', ['To help it grow stronger and be used again', 'To erase it completely', 'To translate it into another language only', 'To forget it entirely'], 0),
    ('Why are some Indigenous languages at risk today?', ['Historical policies suppressed their use', 'They were never spoken', 'They are too easy to learn', 'No one ever spoke them'], 0),
    ('How are some communities working to revitalize Indigenous languages?', ['Through education and community programs', 'By ignoring the issue', 'By banning all languages', 'By avoiding schools entirely'], 0),
    ('Why is language revitalization important to a culture?', ['Language carries traditions, knowledge, and identity', 'Language has no connection to culture', 'Only written language matters', 'Culture does not need language'], 0),
    ('Which of these could help revitalize a language?', ['Language classes and immersion programs', 'Refusing to teach it to anyone', 'Erasing historical records', 'Ignoring elders who speak it'], 0)]),
]),
day(114, [
L('Reading: Distinguishing Primary and Secondary Sources',
  'Grade 5 Language strand: a primary source is a firsthand account or original document, like a diary or photograph, while a secondary source, like a textbook, interprets or describes primary sources.',
  [('What is a primary source?', ['A firsthand account or original document', 'A summary written by someone else', 'A textbook only', 'A type of punctuation'], 0),
   ('Which is an example of a primary source?', ['A diary entry written at the time of an event', 'A textbook chapter written later', 'An encyclopedia article', 'A documentary made years later'], 0),
   ('What is a secondary source?', ['A source that interprets or describes primary sources', 'The original document itself', 'A photograph taken during an event', 'A firsthand letter'], 0),
   ('Which is an example of a secondary source?', ['A history textbook', 'An original letter from the 1800s', 'A photograph from the event', 'A diary from that time'], 0),
   ('Why is it useful to know the difference between primary and secondary sources?', ['It helps evaluate the reliability and origin of information', 'It has no research value', 'Sources are always the same', 'It only matters for fiction'], 0)]),
M('Geometry: Volume of Cones and Pyramids',
  'Grade 5 Math strand: the volume of a cone or pyramid is one-third the volume of a cylinder or prism with the same base and height.',
  [('The volume of a cone is what fraction of a cylinder with the same base and height?', ['One-third', 'One-half', 'Two-thirds', 'The same as the cylinder'], 0),
   ('The volume of a pyramid is what fraction of a prism with the same base and height?', ['One-third', 'One-half', 'Three-quarters', 'The same as the prism'], 0),
   ('If a cylinder has a volume of 90 cubic units, what is the volume of a cone with the same base and height?', ['30', '45', '60', '90'], 0),
   ('What two measurements are typically needed to find the volume of a cone?', ['Base area and height', 'Only the height', 'Only the base area', 'Only the radius of the top'], 0),
   ('Why might it be useful to compare cone and pyramid volumes to cylinders and prisms?', ['It helps us understand and remember the volume relationship', 'They have no relationship at all', 'Cones and cylinders are the same shape', 'Volume never relates between shapes'], 0)]),
Sc('Photosynthesis — How Plants Make Their Own Food',
   'Grade 5 Science strand: photosynthesis is the process plants use to make their own food from sunlight, water, and carbon dioxide, releasing oxygen as a byproduct.',
   [('What is photosynthesis?', ['The process plants use to make their own food from sunlight', 'A type of animal digestion', 'A weather pattern', 'A rock-forming process'], 0),
    ('What three things do plants need for photosynthesis?', ['Sunlight, water, and carbon dioxide', 'Only soil', 'Only darkness', 'Only sound'], 0),
    ('What gas do plants release during photosynthesis?', ['Oxygen', 'Carbon dioxide only', 'Nitrogen only', 'Helium'], 0),
    ('Where in the plant does photosynthesis mainly occur?', ['In the leaves', 'In the roots only', 'In the flower only', 'In the seed only'], 0),
    ('Why is photosynthesis important for other living things?', ['It produces the oxygen many organisms need to breathe', 'It has no effect on other organisms', 'It removes all oxygen from the air', 'It only matters to plants'], 0)]),
SS('The Auditor General — Watching How Government Spends Money',
   'Grade 5 Social Studies strand: the Auditor General is an independent officer who reviews how the federal government spends public money, reporting on waste, mismanagement, or inefficiency.',
   [('What is the Auditor Generals main job?', ['Reviewing how the government spends public money', 'Teaching in schools', 'Running a business', 'Managing a hospital'], 0),
    ('Why is it important for the Auditor General to be independent?', ['So the review is unbiased and not controlled by the government being reviewed', 'Independence does not matter', 'The government should review itself only', 'Independence makes the reports less accurate'], 0),
    ('What might the Auditor Generals reports reveal?', ['Waste, mismanagement, or inefficiency in spending', 'Only good news', 'Nothing useful', 'Sports statistics'], 0),
    ('Who does the Auditor General typically report to?', ['Parliament', 'A single citizen', 'A private company', 'No one'], 0),
    ('Why might citizens care about the Auditor Generals reports?', ['They show how tax dollars are being used', 'Citizens have no interest in government spending', 'The reports are always secret', 'Reports never affect citizens'], 0)]),
]),
day(115, [
L('Media Literacy: Evaluating Website Credibility',
  'Grade 5 Language strand: evaluating a websites credibility means checking who wrote it, when it was published, and whether the information is supported by evidence before trusting it.',
  [('What should you check to evaluate a websites credibility?', ['Who wrote it and when it was published', 'Only the background colour', 'Only the font style', 'Nothing, all websites are equally reliable'], 0),
   ('Why is it important to check who wrote a website?', ['To judge whether the author is a reliable source', 'The author never matters', 'Authors are always experts', 'It has no effect on trust'], 0),
   ('What is a sign that a website might be less credible?', ['It provides no evidence or sources for its claims', 'It cites clear sources', 'It has a recent publish date', 'It is written by an expert'], 0),
   ('Why might the publish date of a website matter?', ['Information can become outdated over time', 'Dates never matter online', 'Older websites are always more accurate', 'Publish dates are always fake'], 0),
   ('Which is a good habit when researching online?', ['Comparing information across multiple credible sources', 'Trusting the very first result blindly', 'Ignoring all sources', 'Believing everything without checking'], 0)]),
M('Geometry: The Coordinate Plane — All Four Quadrants',
  'Grade 5 Math strand: the coordinate plane extends beyond the first quadrant to include four quadrants, using positive and negative x and y values to plot any point.',
  [('How many quadrants make up a full coordinate plane?', ['Four', 'Two', 'One', 'Eight'], 0),
   ('In which quadrant would you find a point with a positive x and positive y value?', ['Quadrant I', 'Quadrant II', 'Quadrant III', 'Quadrant IV'], 0),
   ('In which quadrant would you find a point with a negative x and positive y value?', ['Quadrant II', 'Quadrant I', 'Quadrant III', 'Quadrant IV'], 0),
   ('What are the two number lines called that form the coordinate plane?', ['The x-axis and y-axis', 'The a-axis and b-axis', 'The height and width lines', 'The top and bottom lines'], 0),
   ('The point where the x-axis and y-axis cross is called the ___.', ['Origin', 'Quadrant', 'Vertex', 'Endpoint'], 0)]),
Sc('Dental Health — Caring for Our Teeth',
   'Grade 5 Science strand: teeth help us chew and speak, and good dental habits like brushing, flossing, and limiting sugary foods help prevent cavities and gum disease.',
   [('What are two important functions of our teeth?', ['Chewing and speaking', 'Only breathing', 'Only smelling', 'Only hearing'], 0),
    ('What dental habit helps remove food particles between teeth?', ['Flossing', 'Sleeping', 'Running', 'Drinking soda'], 0),
    ('Why might limiting sugary foods help dental health?', ['Sugar can contribute to tooth decay', 'Sugar always strengthens teeth', 'Sugar has no effect on teeth', 'Sugar removes cavities'], 0),
    ('What can happen if teeth are not cared for properly?', ['Cavities and gum disease', 'Teeth automatically become stronger', 'Nothing happens at all', 'Teeth turn into bone'], 0),
    ('How often do dentists typically recommend brushing teeth?', ['At least twice a day', 'Once a month', 'Never', 'Only before holidays'], 0)]),
SS('Understanding Canadas National Debt and Deficit',
   'Grade 5 Social Studies strand: a deficit occurs when the government spends more money than it collects in a year, while debt is the total amount owed from accumulated deficits over time.',
   [('What is a government deficit?', ['When spending is more than money collected in a year', 'When spending equals income exactly', 'A type of tax', 'A kind of currency'], 0),
    ('What is national debt?', ['The total amount owed from accumulated deficits over time', 'A single years spending only', 'A type of holiday', 'A kind of election'], 0),
    ('How does a deficit relate to debt?', ['Repeated deficits add up to increase the total debt', 'They are completely unrelated concepts', 'A deficit always reduces debt', 'Debt causes deficits to disappear'], 0),
    ('Why might a government choose to run a deficit in some years?', ['To fund important programs or respond to emergencies', 'Deficits are never intentional', 'To make the economy invisible', 'Governments never spend money'], 0),
    ('Why is understanding government debt and deficits useful for citizens?', ['It helps citizens understand economic decisions and their effects', 'It has no relevance to citizens', 'Only banks need this understanding', 'It is a secret citizens cannot learn about'], 0)]),
]),
day(116, [
L('Oral Communication: Preparing for a Formal Debate',
  'Grade 5 Language strand: preparing for a formal debate involves researching both sides of an issue, organizing clear arguments with evidence, and anticipating counterarguments.',
  [('What is an important first step in preparing for a debate?', ['Researching both sides of the issue', 'Refusing to research anything', 'Only listening to one opinion', 'Ignoring the topic completely'], 0),
   ('Why should debaters anticipate counterarguments?', ['To prepare strong responses to opposing points', 'Counterarguments never matter', 'To avoid the topic entirely', 'To agree with everything said'], 0),
   ('What should support a debaters argument?', ['Evidence and clear reasoning', 'Only personal opinions with no evidence', 'Loud volume alone', 'Interruptions'], 0),
   ('What does it mean to organize an argument clearly?', ['Presenting points in a logical, easy-to-follow order', 'Mixing up points randomly', 'Speaking without any structure', 'Avoiding all evidence'], 0),
   ('A formal debate typically requires participants to ___.', ['Respect turn-taking and formal structure', 'Interrupt whenever they want', 'Ignore the rules', 'Refuse to listen to the other side'], 0)]),
M('Data Management: Combinations — Counting Possible Outcomes',
  'Grade 5 Math strand: combinations help count the number of different ways items can be grouped together when order does not matter, such as choosing 2 toppings from 4 options.',
  [('What does a combination count?', ['The number of ways to group items when order does not matter', 'Only ordered arrangements', 'A single fixed outcome', 'A type of fraction'], 0),
   ('If you can choose 2 toppings from 4 options (A, B, C, D), how many different combinations are possible?', ['6', '4', '8', '12'], 0),
   ('In combinations, does choosing A then B count differently than choosing B then A?', ['No, they are the same combination', 'Yes, they are always different', 'Only sometimes', 'It depends on the colour'], 0),
   ('Why are combinations useful in real life?', ['They help count possible groupings, like meal or outfit choices', 'They have no real-world use', 'They only apply to sports scores', 'They cannot be calculated'], 0),
   ('Which situation involves finding a combination?', ['Choosing 3 books to bring on a trip from a shelf of 5', 'Lining up 5 people in order', 'Assigning first, second, and third place', 'Arranging letters into a specific word'], 0)]),
Sc('DNA — The Blueprint of Life',
   'Grade 5 Science strand: DNA is a molecule found in the cells of living things that carries the instructions, or blueprint, for how an organism grows and functions.',
   [('What is DNA?', ['A molecule that carries instructions for how an organism grows and functions', 'A type of rock', 'A kind of weather pattern', 'A form of light'], 0),
    ('Where is DNA found in living things?', ['In the cells', 'Only in the air around them', 'Only in water', 'Nowhere, it does not exist'], 0),
    ('What does DNA help determine?', ['Traits like eye colour and other inherited features', 'The weather', 'The price of food', 'The time of day'], 0),
    ('Why do children often resemble their parents?', ['They inherit DNA from both parents', 'DNA has no role in resemblance', 'Resemblance is completely random', 'Only appearance matters, not DNA'], 0),
    ('DNA is sometimes described as a ___ because it holds instructions for life.', ['Blueprint', 'Weather forecast', 'Recipe for bread', 'Type of rock'], 0)]),
SS('Electoral Ridings — How Canada Divides Voting Districts',
   'Grade 5 Social Studies strand: Canada is divided into electoral ridings, each represented by one Member of Parliament elected by the voters living in that riding.',
   [('What is an electoral riding?', ['A voting district represented by one Member of Parliament', 'A type of currency', 'A national holiday', 'A kind of map legend'], 0),
    ('Who represents each electoral riding?', ['One elected Member of Parliament', 'The Prime Minister alone', 'No one', 'Every citizen in Canada'], 0),
    ('Why is Canada divided into ridings?', ['So different regions have local representation in government', 'Ridings serve no purpose', 'To confuse voters', 'To eliminate elections'], 0),
    ('How do voters in a riding choose their representative?', ['By voting in an election', 'By random selection only', 'Representatives are never chosen by voters', 'By coin flip'], 0),
    ('The number of ridings in Canada can change over time mainly due to ___.', ['Changes in population', 'The weather', 'Sports results', 'The price of goods'], 0)]),
]),
day(117, [
L('Writing: Writing an Interview',
  'Grade 5 Language strand: writing an interview involves preparing thoughtful, open-ended questions, then recording and organizing the subjects responses clearly for readers.',
  [('What is an important step before conducting an interview?', ['Preparing thoughtful, open-ended questions', 'Skipping preparation entirely', 'Asking only yes-or-no questions', 'Ignoring the topic'], 0),
   ('What is an open-ended question?', ['A question that invites a detailed response, not just yes or no', 'A question with only one correct answer', 'A question that cannot be answered', 'A rhetorical question'], 0),
   ('Why is it important to organize interview responses clearly?', ['So readers can easily follow the conversation', 'Organization does not matter', 'To confuse the reader on purpose', 'To remove all of the subjects words'], 0),
   ('Which is an example of a good interview question?', ['What inspired you to pursue this career?', 'Do you like your job?', 'Are you busy?', 'Is today Monday?'], 0),
   ('An interview article typically includes ___.', ['The interviewers questions and the subjects answers', 'Only the interviewers opinions', 'No questions at all', 'A list of unrelated facts'], 0)]),
M('Algebra: Writing Expressions from Word Problems',
  'Grade 5 Math strand: students translate word problems into algebraic expressions by identifying the unknown quantity and representing the relationships with numbers, variables, and operations.',
  [('What is the first step in writing an algebraic expression from a word problem?', ['Identifying the unknown quantity', 'Ignoring the numbers', 'Guessing the final answer', 'Skipping the problem'], 0),
   ('Which expression represents 5 more than a number n?', ['n + 5', 'n - 5', '5n', 'n / 5'], 0),
   ('Which expression represents a number n divided by 3?', ['n / 3', 'n + 3', '3n', 'n - 3'], 0),
   ('Which expression represents three times a number n, decreased by 2?', ['3n - 2', 'n - 2', '3(n - 2)', '2n - 3'], 0),
   ('Why is it useful to write expressions from word problems?', ['It helps solve real-world problems using math', 'Expressions have no real-world connection', 'It only applies to shapes', 'It replaces the need for numbers'], 0)]),
Sc('Cells — The Building Blocks of Life',
   'Grade 5 Science strand: cells are the tiny building blocks that make up all living things, and different types of cells have different jobs within an organism.',
   [('What are cells?', ['The tiny building blocks that make up all living things', 'A type of rock', 'A kind of weather', 'A form of light'], 0),
    ('Do all living things have cells?', ['Yes', 'No, only animals do', 'Only plants have cells', 'Only humans have cells'], 0),
    ('Can different types of cells have different jobs?', ['Yes', 'No, all cells do the exact same job', 'Cells never have jobs', 'Only one cell exists in each organism'], 0),
    ('What tool do scientists often use to see cells?', ['A microscope', 'A telescope', 'A thermometer', 'A compass'], 0),
    ('Cells are considered the basic unit of ___.', ['Life', 'Weather', 'Sound', 'Light'], 0)]),
SS('Equalization Payments — Sharing Wealth Across Provinces',
   'Grade 5 Social Studies strand: equalization payments are federal transfers of money to less wealthy provinces, helping ensure Canadians across the country have access to similar public services.',
   [('What are equalization payments?', ['Federal transfers of money to less wealthy provinces', 'A type of provincial tax', 'A tourist attraction', 'A kind of national holiday'], 0),
    ('Why does the federal government make equalization payments?', ['To help ensure similar public services across provinces', 'To punish wealthy provinces', 'To eliminate all provinces', 'They serve no purpose'], 0),
    ('Which provinces might receive equalization payments?', ['Provinces with relatively lower revenue-generating capacity', 'Only the wealthiest provinces', 'No province ever receives them', 'Only territories'], 0),
    ('Equalization payments are an example of ___.', ['Federal government policy', 'A type of sport', 'A kind of weather pattern', 'A private business decision'], 0),
    ('Why might Canadians across different provinces value equalization payments?', ['They help ensure fairer access to services nationwide', 'They have no benefit to anyone', 'They only benefit one province', 'They increase inequality'], 0)]),
]),
day(118, [
L('Reading: Understanding Parody',
  'Grade 5 Language strand: a parody imitates the style of another work in an exaggerated or humorous way, often to poke fun at it or make a point.',
  [('What is a parody?', ['A humorous imitation of another works style', 'A type of punctuation', 'A serious historical account', 'A grammar rule'], 0),
   ('Why do writers create parodies?', ['To entertain or make a point through humorous imitation', 'To copy a work exactly with no changes', 'To remove all humour', 'To avoid referencing other works'], 0),
   ('What does a parody typically exaggerate?', ['Recognizable features of the original work', 'Nothing at all', 'Only the title', 'Only punctuation marks'], 0),
   ('Which is an example of parody?', ['A funny retelling of a famous fairy tale with silly changes', 'A word-for-word copy of a textbook', 'A weather report', 'A dictionary definition'], 0),
   ('Parody is closely related to which literary technique?', ['Satire', 'Rhyme', 'Alliteration', 'Onomatopoeia'], 0)]),
M('Measurement: Converting Between 12-Hour and 24-Hour Time',
  'Grade 5 Math strand: 24-hour time, also called military time, avoids the need for AM and PM by numbering hours from 00 to 23 across a full day.',
  [('How many hours are numbered in a full 24-hour time system?', ['00 to 23', '1 to 24', '0 to 24', '1 to 12'], 0),
   ('What is 3:00 PM in 24-hour time?', ['15:00', '03:00', '13:00', '17:00'], 0),
   ('What is 9:00 AM in 24-hour time?', ['09:00', '19:00', '21:00', '90:00'], 0),
   ('What is 18:00 in 12-hour time?', ['6:00 PM', '6:00 AM', '8:00 PM', '18:00 AM'], 0),
   ('Why might 24-hour time be useful in schedules like transportation?', ['It avoids confusion between AM and PM', 'It is always less accurate', 'It removes the need for numbers', 'It only works for mornings'], 0)]),
Sc('Renewable Energy in Focus: Solar Power',
   'Grade 5 Science strand: solar power converts sunlight directly into electricity using solar panels, offering a clean, renewable source of energy.',
   [('What does solar power convert into electricity?', ['Sunlight', 'Wind', 'Coal', 'Ocean waves'], 0),
    ('What device is commonly used to capture solar energy?', ['Solar panels', 'Windmills', 'Dams', 'Furnaces'], 0),
    ('Why is solar power considered a renewable energy source?', ['Sunlight is naturally replenished and will not run out', 'Sunlight runs out permanently', 'It requires burning fossil fuels', 'It cannot be reused'], 0),
    ('What is one advantage of solar power over fossil fuels?', ['It produces energy without burning fuel or creating pollution', 'It always costs more with no benefits', 'It only works at night', 'It requires no sunlight at all'], 0),
    ('Where might solar panels commonly be installed?', ['On rooftops or open fields with sunlight', 'Underground with no light', 'Inside sealed boxes', 'Underwater'], 0)]),
SS('Canadas National Historic Sites — Preserving Our Heritage',
   'Grade 5 Social Studies strand: national historic sites are places recognized for their importance to Canadian history, preserved so future generations can learn about the past.',
   [('What is a national historic site?', ['A place recognized for its importance to Canadian history', 'A type of amusement park', 'A modern shopping mall', 'A weather station'], 0),
    ('Why are national historic sites preserved?', ['So future generations can learn about the past', 'To be demolished eventually', 'They have no educational value', 'To be ignored by the public'], 0),
    ('Who might visit a national historic site?', ['Students, tourists, and researchers interested in history', 'No one is allowed to visit', 'Only government officials', 'Only people from other countries'], 0),
    ('How are national historic sites different from national parks?', ['They focus on historical or cultural significance rather than natural landscapes', 'They are exactly the same thing', 'National historic sites have no buildings', 'National parks are always historic sites too'], 0),
    ('Visiting a national historic site can help people understand ___.', ['Events and people that shaped Canadas past', 'Nothing about history', 'Only current events', 'Only future predictions'], 0)]),
]),
day(119, [
L('Vocabulary: Number Prefixes',
  'Grade 5 Language strand: number prefixes like uni-, bi-, tri-, and quad- indicate quantity within a word, such as unicycle (one wheel) or quadrilateral (four sides).',
  [('What does the prefix uni- mean?', ['One', 'Two', 'Three', 'Four'], 0),
   ('What does the prefix bi- mean?', ['Two', 'One', 'Three', 'Four'], 0),
   ('What does the prefix tri- mean?', ['Three', 'One', 'Two', 'Four'], 0),
   ('What does the prefix quad- mean?', ['Four', 'One', 'Two', 'Three'], 0),
   ('Which word contains a prefix meaning two?', ['Bicycle', 'Unicycle', 'Triangle', 'Quadrilateral'], 0)]),
M('Geometry: Similar Triangles and Proportional Sides',
  'Grade 5 Math strand: similar triangles have the same shape but may differ in size, with corresponding sides that are proportional, or in the same ratio, to each other.',
  [('What does it mean for two triangles to be similar?', ['They have the same shape but may differ in size', 'They must be identical in size', 'They have no matching angles', 'They cannot share any properties'], 0),
   ('What is true about the corresponding sides of similar triangles?', ['They are proportional to each other', 'They are always exactly equal', 'They have no relationship', 'They must be different shapes'], 0),
   ('If one triangle has sides twice as long as a similar triangle, the scale factor is ___.', ['2', '1', '4', '0.5'], 0),
   ('What is true about the corresponding angles of similar triangles?', ['They are equal', 'They are always different', 'They cannot be measured', 'They must add up to 90 degrees'], 0),
   ('Why are similar triangles useful in real life?', ['They help with tasks like measuring height using shadows', 'They have no real-world use', 'They only apply to art', 'They cannot be used for measurement'], 0)]),
Sc('Renewable Energy in Focus: Wind and Hydro Power',
   'Grade 5 Science strand: wind power uses turbines to capture the energy of moving air, while hydro power uses flowing or falling water, both offering clean, renewable electricity.',
   [('What does wind power use to generate electricity?', ['Wind turbines', 'Solar panels', 'Burning coal', 'Underground heat'], 0),
    ('What does hydro power use to generate electricity?', ['Flowing or falling water', 'Sunlight', 'Wind', 'Coal'], 0),
    ('Why are wind and hydro power considered renewable?', ['Wind and water are naturally replenished sources', 'They will run out permanently soon', 'They require burning fossil fuels', 'They cannot be reused'], 0),
    ('What structure is commonly used to generate hydro power?', ['A dam', 'A greenhouse', 'A mine', 'A furnace'], 0),
    ('Which of these is an advantage shared by wind and hydro power?', ['They produce electricity without burning fossil fuels', 'They always require sunlight', 'They only work indoors', 'They cannot generate electricity'], 0)]),
SS('The Magna Cartas Influence on Canadian Law',
   'Grade 5 Social Studies strand: the Magna Carta, signed in England in 1215, established early principles like the rule of law that influenced legal systems, including Canadas, centuries later.',
   [('What was the Magna Carta?', ['An early document establishing principles like the rule of law', 'A modern Canadian law', 'A type of currency', 'A national holiday'], 0),
    ('Roughly when was the Magna Carta signed?', ['In the 1200s', 'Last year', 'In the 1900s', 'It has not happened yet'], 0),
    ('What important principle did the Magna Carta help establish?', ['The rule of law, meaning even rulers must follow the law', 'That only kings make all decisions with no limits', 'That laws do not apply to anyone', 'That courts should not exist'], 0),
    ('How did the Magna Carta influence legal systems like Canadas?', ['Its principles shaped ideas about law and rights over centuries', 'It has no connection to modern law', 'Canada copied it word for word', 'It was immediately forgotten'], 0),
    ('Why do historians and legal scholars still study the Magna Carta today?', ['It laid early groundwork for modern legal principles', 'It has no historical significance', 'It was written very recently', 'It only applied for one day'], 0)]),
]),
day(120, [
L('Language Review: Grammar, Writing Forms, and Media Literacy',
  'Grade 5 Language strand review: students revisit modal verbs, biography and memoir writing, primary and secondary sources, evaluating website credibility, formal debate, and parody.',
  [('Which of these is a modal verb?', ['Should', 'Running', 'Quickly', 'Happy'], 0),
   ('What is a biography?', ['The true story of a real persons life written by someone else', 'A made-up story', 'A story about yourself', 'A type of poem'], 0),
   ('What is a memoir?', ['A personal narrative reflecting on a meaningful memory from the authors own life', 'A made-up fantasy story', 'A biography of someone else', 'A dictionary entry'], 0),
   ('What is a primary source?', ['A firsthand account or original document', 'A summary written by someone else', 'A textbook only', 'A type of punctuation'], 0),
   ('What is a parody?', ['A humorous imitation of another works style', 'A type of punctuation', 'A serious historical account', 'A grammar rule'], 0)]),
M('Math Review: Data, Geometry, and Algebra',
  'Grade 5 Math strand review: students revisit scatter plots, compound interest, cylinder surface area, cone and pyramid volume, four-quadrant coordinate planes, combinations, and similar triangles.',
  [('What does a scatter plot show?', ['Pairs of related data as points on a graph', 'A single number', 'Only categories', 'A list of names'], 0),
   ('What is compound interest?', ['Interest earned on both the original amount and previously earned interest', 'Interest earned only once', 'A type of tax', 'Money that is lost over time'], 0),
   ('The volume of a cone is what fraction of a cylinder with the same base and height?', ['One-third', 'One-half', 'Two-thirds', 'The same as the cylinder'], 0),
   ('How many quadrants make up a full coordinate plane?', ['Four', 'Two', 'One', 'Eight'], 0),
   ('What does it mean for two triangles to be similar?', ['They have the same shape but may differ in size', 'They must be identical in size', 'They have no matching angles', 'They cannot share any properties'], 0)]),
Sc('Science Review: Space, Body Science, and Renewable Energy',
   'Grade 5 Science strand review: students revisit comets and asteroids, eclipses, tides, photosynthesis, dental health, DNA, cells, and renewable energy from solar, wind, and hydro power.',
   [('What forms a comets glowing tail?', ['Ice and dust heated by the sun', 'Reflected moonlight only', 'Fire from the comets core', 'Nothing, comets have no tail'], 0),
    ('What happens during a solar eclipse?', ['The Moon passes between the sun and Earth', 'Earth passes between the sun and the Moon', 'The sun disappears forever', 'Nothing unusual happens'], 0),
    ('What is photosynthesis?', ['The process plants use to make their own food from sunlight', 'A type of animal digestion', 'A weather pattern', 'A rock-forming process'], 0),
    ('What is DNA?', ['A molecule that carries instructions for how an organism grows and functions', 'A type of rock', 'A kind of weather pattern', 'A form of light'], 0),
    ('What does hydro power use to generate electricity?', ['Flowing or falling water', 'Sunlight', 'Wind', 'Coal'], 0)]),
SS('Social Studies Review: Government, Economy, and Canadian History',
   'Grade 5 Social Studies strand review: students revisit the census, sister cities, Indigenous language revitalization, the Auditor General, national debt, electoral ridings, equalization payments, and the Magna Carta.',
   [('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A sports event'], 0),
    ('What is the Auditor Generals main job?', ['Reviewing how the government spends public money', 'Teaching in schools', 'Running a business', 'Managing a hospital'], 0),
    ('What is national debt?', ['The total amount owed from accumulated deficits over time', 'A single years spending only', 'A type of holiday', 'A kind of election'], 0),
    ('What is an electoral riding?', ['A voting district represented by one Member of Parliament', 'A type of currency', 'A national holiday', 'A kind of map legend'], 0),
    ('What was the Magna Carta?', ['An early document establishing principles like the rule of law', 'A modern Canadian law', 'A type of currency', 'A national holiday'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_111_120)
    append_to(5, g5_111_120)
