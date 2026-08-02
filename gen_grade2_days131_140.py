#!/usr/bin/env python3
"""Grade 2, Days 131-140 -- eleventh batch, extending Grade 2 past Day 130
toward the full ~187-day school year. Uses the sub()/day()/append_to()
helpers imported directly from gen_curriculum.py (no worksheet field):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by the video-backfill task)

Topics chosen to avoid overlap with existing Grade 2 Days 1-130 (dumped
and checked against data/grade2.json before writing, which already
densely covers nearly the full grade 2 ELA, math, science, and social
studies curriculum, including multiplication facts through 12s, division
with remainders, fraction numerator/denominator, and Earth's layers):
three-letter blends spl/str/scr, text feature sidebars, writing a
postcard, rereading as a strategy, debate writing, adages and proverbs,
author study, compound sentences with yet, and editorial cartoons for
Language. Multiplying by 4 via doubling twice, dividing using arrays,
elapsed time on a number line, comparing fractions with the same
numerator, double bar graphs, mixed numbers, converting metres to
centimetres, spinner probability, and skip counting by 25s for Math.
The human eye, ocean tides, the water table, genetics basics, simple
chemical reactions, atmosphere layers, whales and dolphins, migratory
birds, and coral polyps for Science. Sir John A Macdonald, the Bank of
Canada, the Coast Guard, the metric system, Truth and Reconciliation Day,
the Charter of Rights and Freedoms, the Klondike Gold Rush, O Canada, and
the Governor General for Social Studies -- none of those exact ideas
appear in Days 1-130. Day 140 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch. No
embedded ASCII double-quote or straight apostrophe characters are used
anywhere in title/summary/quiz text -- contractions and possessives are
avoided entirely (or rewritten without the apostrophe) to keep the
generated .ts string literals valid. The sensitive historical topic of
Truth and Reconciliation Day is handled with age-appropriate, respectful,
factual framing suitable for a Grade 2 audience.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to


def mk(subject_key, title, summary, quiz):
    rl = f'YouTube: {title}'
    ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{title} grade 2 educational')
    return sub(subject_key, title, summary, rl, ru, quiz)


def L(t, s, q):
    return mk('Language', t, s, q)


def M(t, s, q):
    return mk('Math', t, s, q)


def Sc(t, s, q):
    return mk('Science', t, s, q)


def SS(t, s, q):
    return mk('SocialStudies', t, s, q)


def _rebalance_answer_positions(days, seed=20260802):
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
    return days


g2_131_140 = [
day(131, [
L('Blends: spl, str, and scr',
  'Grade 2 Language strand: three-letter consonant blends like spl, str, and scr appear at the start of words such as splash, street, and scream.',
  [('Which word begins with the spl blend?', ['Splash', 'Street', 'Scream', 'Sun'], 0),
   ('Which word begins with the str blend?', ['Splash', 'Street', 'Scream', 'Sit'], 1),
   ('Which word begins with the scr blend?', ['Splash', 'Street', 'Scream', 'Stop'], 2),
   ('How many letters are in a three-letter blend like str?', ['Two', 'Three', 'Four', 'Five'], 1),
   ('Which of these words has a three-letter blend?', ['Scrape', 'Cat', 'Sun', 'Dog'], 0)]),
M('Multiplying by 4: Doubling Twice',
  'Grade 2 Math strand: multiplying a number by 4 can be done by doubling it twice, such as doubling 6 to get 12, then doubling 12 to get 24.',
  [('What is 6 x 4 using the double twice strategy?', ['20', '22', '24', '26'], 2),
   ('What is double 5?', ['8', '9', '10', '12'], 2),
   ('What is 5 x 4 using the double twice strategy?', ['18', '20', '22', '25'], 1),
   ('To multiply by 4 using this strategy, you double a number ___.', ['Once', 'Twice', 'Three times', 'Four times'], 1),
   ('What is 3 x 4 using the double twice strategy?', ['10', '11', '12', '14'], 2)]),
Sc('The Human Eye: How We See',
   'Grade 2 Science strand: the eye is the organ we use to see, taking in light and sending signals to the brain so we can understand what we are looking at.',
   [('What organ do we use to see?', ['The eye', 'The ear', 'The nose', 'The skin'], 0),
    ('What does the eye take in to help us see?', ['Light', 'Sound', 'Smell', 'Taste'], 0),
    ('After the eye takes in light, where does it send a signal?', ['The brain', 'The stomach', 'The lungs', 'The heart'], 0),
    ('Which of these could damage our eyes if we are not careful?', ['Looking directly at the sun', 'Reading a book', 'Wearing sunglasses', 'Blinking'], 0),
    ('Why is it helpful to have two eyes instead of one?', ['It helps us judge distance and see depth', 'It has no benefit', 'It only helps us hear better', 'It helps us smell better'], 0)]),
SS('Sir John A Macdonald: Canadas First Prime Minister',
   'Grade 2 Social Studies strand: Sir John A Macdonald became Canadas first prime minister in 1867, leading the new country after Confederation.',
   [('Who was Canadas first prime minister?', ['Sir John A Macdonald', 'Terry Fox', 'A mayor', 'A premier'], 0),
    ('In what year did Sir John A Macdonald become prime minister?', ['1867', '1965', '1812', '2000'], 0),
    ('What major event happened around the same time he became prime minister?', ['Confederation', 'A hockey championship', 'A school opening', 'A snowstorm'], 0),
    ('What is the main job of a prime minister?', ['Leading the whole country', 'Leading one school', 'Leading one town', 'Leading one street'], 0),
    ('Why do students learn about Canadas first prime minister?', ['To understand how Canada was led as a new country', 'It has no importance', 'It is a made-up story', 'It only matters in other countries'], 0)]),
]),
day(132, [
L('Text Features: Sidebars and Fun Facts',
  'Grade 2 Language strand: sidebars are small boxes of extra information placed beside the main text, often sharing fun facts related to the topic.',
  [('What is a sidebar?', ['A small box of extra information beside the main text', 'The books cover', 'The last page', 'The table of contents'], 0),
   ('What kind of information might a sidebar contain?', ['Fun facts related to the topic', 'The books price', 'A random unrelated story', 'Nothing at all'], 0),
   ('Where is a sidebar usually placed on a page?', ['Beside the main text', 'Only on the cover', 'Only on the last page', 'Inside the main paragraph'], 0),
   ('Why might an author include a sidebar?', ['To share extra, interesting information', 'To confuse the reader', 'It has no purpose', 'To replace the whole chapter'], 0),
   ('Which text feature is most similar to a sidebar in purpose?', ['A caption', 'A table of contents', 'The title page', 'The back cover'], 0)]),
M('Dividing Using Arrays',
  'Grade 2 Math strand: an array of equal rows and columns can help students divide a total into equal groups, showing how many are in each row.',
  [('If 12 objects are arranged in an array with 3 rows, how many are in each row?', ['3', '4', '5', '6'], 1),
   ('If 20 objects are arranged in an array with 4 rows, how many are in each row?', ['4', '5', '6', '7'], 1),
   ('An array can help us divide a total into ___.', ['Equal groups', 'Random groups', 'One giant group', 'No groups at all'], 0),
   ('If 15 objects are arranged in an array with 5 rows, how many are in each row?', ['2', '3', '4', '5'], 1),
   ('Using an array to divide is helpful because it shows ___.', ['Equal rows and columns', 'Only the total, not the groups', 'Colours', 'Fractions only'], 0)]),
Sc('Ocean Tides: The Rise and Fall of the Sea',
   'Grade 2 Science strand: ocean tides are the regular rising and falling of sea water along the shore, caused mainly by the pull of the moons gravity.',
   [('What are ocean tides?', ['The regular rising and falling of sea water', 'A type of ocean animal', 'A kind of storm', 'A colour of the ocean'], 0),
    ('What mainly causes ocean tides?', ['The pull of the moons gravity', 'The wind alone', 'The sun disappearing', 'Fish swimming'], 0),
    ('About how often do tides usually rise and fall each day?', ['Once a year', 'A few times a day', 'Once a month', 'Never'], 1),
    ('At low tide, the water level along the shore is ___.', ['Higher than usual', 'Lower than usual', 'Frozen', 'Boiling'], 1),
    ('Tides are an example of how the ocean ___.', ['Never changes', 'Changes in a regular pattern', 'Disappears completely', 'Turns to ice daily'], 1)]),
SS('The Bank of Canada: Where Our Money Comes From',
   'Grade 2 Social Studies strand: the Bank of Canada is the national bank that designs and issues Canadian money and helps manage the countrys economy.',
   [('What does the Bank of Canada do?', ['Designs and issues Canadian money', 'Sells groceries', 'Teaches school', 'Delivers mail'], 0),
    ('Is the Bank of Canada the same as a regular bank you visit in town?', ['No, it has a different, national role', 'Yes, exactly the same', 'It does not exist', 'It only exists in one city'], 0),
    ('Which of these is a job of the Bank of Canada?', ['Helping manage the countrys economy', 'Coaching sports teams', 'Growing crops', 'Building roads'], 0),
    ('Where does the design of Canadian bills and coins come from?', ['The Bank of Canada and the Royal Canadian Mint', 'A random guess', 'Another country', 'No one designs them'], 0),
    ('Learning about the Bank of Canada helps students understand ___.', ['How money is managed in the country', 'Nothing about money', 'Only foreign banks', 'A made-up story'], 0)]),
]),
day(133, [
L('Writing a Postcard: Sharing News in a Short Message',
  'Grade 2 Language strand: a postcard is a short, friendly message that shares quick news or a memory, often written while traveling.',
  [('What is a postcard?', ['A short, friendly message sharing quick news', 'A long formal report', 'A legal document', 'A math worksheet'], 0),
   ('When might someone write a postcard?', ['While traveling, to share news with someone at home', 'During a math test', 'While sleeping', 'During a fire drill'], 0),
   ('Which of these is typical postcard content?', ['A quick update about a fun trip', 'A detailed scientific report', 'A legal contract', 'A grocery list only'], 0),
   ('How is a postcard different from a long letter?', ['A postcard is much shorter', 'A postcard is always longer', 'They are the same length always', 'A postcard has no message'], 0),
   ('A postcard usually includes ___.', ['A short message and the senders name', 'A full novel', 'A math equation', 'A legal signature only'], 0)]),
M('Elapsed Time on a Number Line',
  'Grade 2 Math strand: students use a number line to find elapsed time, jumping forward in minutes or hours from a start time to an end time.',
  [('If you start at 2:00 and jump forward 30 minutes on a number line, what time do you reach?', ['2:15', '2:30', '2:45', '3:00'], 1),
   ('If you start at 5:00 and jump forward 1 hour on a number line, what time do you reach?', ['5:15', '5:30', '6:00', '6:30'], 2),
   ('A number line can help us find elapsed time by showing ___.', ['Jumps forward in time', 'Only colours', 'Only shapes', 'Random numbers'], 0),
   ('If you start at 10:00 and jump forward 45 minutes, what time do you reach?', ['10:15', '10:30', '10:45', '11:15'], 2),
   ('Using a number line to solve elapsed time problems is a way to ___.', ['Visualize the passage of time', 'Ignore the problem', 'Avoid using numbers', 'Skip counting altogether'], 0)]),
Sc('The Water Table: Water Beneath Our Feet',
   'Grade 2 Science strand: the water table is the underground level where the soil and rock are completely filled with water, an important source for wells.',
   [('What is the water table?', ['The underground level filled with water', 'A kitchen table', 'A type of cloud', 'A frozen lake'], 0),
    ('Where is the water table located?', ['Underground', 'In the sky', 'On the surface of the ocean', 'Inside a plant'], 0),
    ('What can people dig to reach the water table?', ['A well', 'A tunnel to space', 'A sandcastle', 'A birdhouse'], 0),
    ('Why is the water table important?', ['It is a source of water for wells', 'It has no importance', 'It causes storms', 'It stops all rain'], 0),
    ('The water table can rise or fall depending on ___.', ['How much rain falls and is used', 'The colour of the sky', 'The day of the week', 'The type of music played'], 0)]),
SS('Our Coast Guard: Keeping People Safe on the Water',
   'Grade 2 Social Studies strand: the Canadian Coast Guard helps keep people safe on lakes, rivers, and oceans, responding to emergencies and helping ships navigate safely.',
   [('What does the Coast Guard help keep people safe on?', ['The water', 'The road', 'The playground', 'The classroom'], 0),
    ('What might the Coast Guard do during a water emergency?', ['Respond and help people in danger', 'Ignore the emergency', 'Only work on land', 'Close all the water'], 0),
    ('Which of these might the Coast Guard help with?', ['Guiding ships safely', 'Teaching math class', 'Growing crops', 'Building houses'], 0),
    ('Why is the Coast Guard an important community helper?', ['It helps keep people safe on the water', 'It has no purpose', 'It only helps on land', 'It works only one day a year'], 0),
    ('The Coast Guard is an example of a ___.', ['Public safety service', 'Type of weather', 'Kind of food', 'Type of vehicle only'], 0)]),
]),
day(134, [
L('Reading Strategy: Rereading for Understanding',
  'Grade 2 Language strand: rereading a confusing sentence or paragraph is a helpful strategy that gives readers a second chance to understand tricky parts of a text.',
  [('What is rereading as a reading strategy?', ['Reading a confusing part again to understand it better', 'Skipping confusing parts forever', 'Reading the whole book backwards', 'Reading only the last page'], 0),
   ('When might a reader use the rereading strategy?', ['When a part of the text is confusing', 'Only after finishing the whole book', 'Never', 'Only during recess'], 0),
   ('Why is rereading a helpful strategy?', ['It gives readers another chance to understand', 'It wastes time with no benefit', 'It replaces reading completely', 'It confuses readers further'], 0),
   ('Which is an example of using the rereading strategy?', ['Going back to reread a confusing sentence', 'Throwing the book away', 'Skipping to the end immediately', 'Reading a different book instead'], 0),
   ('Rereading is especially useful for understanding ___.', ['Difficult or confusing parts of a text', 'The books cover colour', 'The price of the book', 'The authors birthday'], 0)]),
M('Comparing Fractions with the Same Numerator',
  'Grade 2 Math strand: when two fractions have the same numerator, the fraction with the smaller denominator is greater, since its parts are larger.',
  [('Which is greater, 1/3 or 1/5?', ['1/3', '1/5', 'They are equal', 'Cannot tell'], 0),
   ('Which is greater, 2/4 or 2/8?', ['2/4', '2/8', 'They are equal', 'Cannot tell'], 0),
   ('When two fractions have the same numerator, which one is greater?', ['The one with the smaller denominator', 'The one with the larger denominator', 'They are always equal', 'Neither is greater'], 0),
   ('Which is greater, 3/5 or 3/10?', ['3/5', '3/10', 'They are equal', 'Cannot tell'], 0),
   ('A smaller denominator with the same numerator means ___.', ['Larger, fewer parts, so each part is bigger', 'Smaller parts always', 'No difference at all', 'The fraction equals zero'], 0)]),
Sc('Genetics Basics: Why We Look Like Our Family',
   'Grade 2 Science strand: living things inherit traits, like eye colour or height, from their parents, which is why children often look similar to their families.',
   [('What are traits passed down from parents called?', ['Inherited traits', 'Random traits', 'Fake traits', 'Borrowed traits'], 0),
    ('Give an example of a trait a child might inherit from a parent.', ['Eye colour', 'Favourite toy', 'A pet', 'A school subject'], 0),
    ('Why do children often look similar to their parents?', ['They inherit traits from their parents', 'It is always a coincidence', 'Children copy their parents on purpose', 'There is no reason'], 0),
    ('Which of these is an inherited trait, not a learned skill?', ['Hair colour', 'Riding a bike', 'Speaking a language', 'Playing a sport'], 0),
    ('Inherited traits come from a living things ___.', ['Parents', 'Friends', 'Teachers', 'Neighbours'], 0)]),
SS('Why Canada Uses the Metric System',
   'Grade 2 Social Studies strand: Canada officially switched to the metric system in the 1970s, using units like metres and litres instead of feet and gallons.',
   [('What measurement system does Canada officially use?', ['The metric system', 'A made-up system', 'No system at all', 'A different system every year'], 0),
    ('Which of these is a metric unit used in Canada?', ['Metres', 'Feet', 'Miles', 'Gallons'], 0),
    ('When did Canada officially switch to the metric system?', ['In the 1970s', 'In 1867', 'In 1812', 'Last year'], 0),
    ('Why might a country choose to use one standard measurement system?', ['To make measuring consistent for everyone', 'It has no benefit', 'To confuse people on purpose', 'To avoid using numbers'], 0),
    ('Which of these is measured using the metric system in Canada?', ['Distance in kilometres', 'Distance in miles', 'Weight in pounds', 'Temperature in Fahrenheit'], 0)]),
]),
day(135, [
L('Debate Writing: Presenting Two Sides of an Argument',
  'Grade 2 Language strand: debate writing presents two different sides of an argument, helping readers understand different viewpoints before forming their own opinion.',
  [('What does debate writing present?', ['Two different sides of an argument', 'Only one opinion with no other side', 'A made-up fantasy story', 'A recipe'], 0),
   ('Why is it useful to consider both sides of an argument?', ['It helps readers understand different viewpoints', 'It has no use', 'It confuses readers on purpose', 'It replaces facts with opinions only'], 0),
   ('Which is an example of presenting two sides of a topic?', ['Some people think recess should be longer, while others disagree.', 'Recess is definitely the best part of school.', 'I love recess.', 'Recess starts at noon.'], 0),
   ('Debate writing is often used to help people ___.', ['Form their own opinion after hearing both sides', 'Ignore all opinions', 'Only hear one side of a topic', 'Avoid thinking about a topic'], 0),
   ('Which skill is important when writing about both sides of an argument?', ['Being fair to each viewpoint', 'Only supporting one side unfairly', 'Ignoring all evidence', 'Refusing to explain either side'], 0)]),
M('Data: Creating a Double Bar Graph',
  'Grade 2 Math strand: a double bar graph shows two sets of data side by side for each category, making it easy to compare them.',
  [('What does a double bar graph show?', ['Two sets of data side by side', 'Only one set of data', 'No data at all', 'Only colours'], 0),
   ('Why might someone use a double bar graph?', ['To compare two sets of data easily', 'It has no purpose', 'To hide information', 'To make a graph harder to read'], 0),
   ('If a double bar graph compares boys and girls favourite fruit, how many bars would there be for each fruit?', ['One', 'Two', 'Three', 'Four'], 1),
   ('A double bar graph is especially useful for ___.', ['Comparing two groups at once', 'Showing only one number', 'Hiding data', 'Avoiding comparisons'], 0),
   ('In a double bar graph, each category usually has ___ bars.', ['One', 'Two', 'Zero', 'Ten'], 1)]),
Sc('Simple Chemical Reactions: Baking Soda and Vinegar',
   'Grade 2 Science strand: mixing baking soda and vinegar causes a chemical reaction that creates bubbles of gas, showing how mixing certain materials can create something new.',
   [('What happens when you mix baking soda and vinegar?', ['They react and create bubbles of gas', 'Nothing happens at all', 'They turn into ice', 'They disappear completely'], 0),
    ('What is created when baking soda and vinegar react?', ['Bubbles of gas', 'A new solid rock', 'A rainbow', 'Sound only'], 0),
    ('Is mixing baking soda and vinegar an example of a chemical reaction?', ['Yes', 'No', 'Only sometimes', 'Never'], 0),
    ('A chemical reaction happens when materials combine to ___.', ['Create something new', 'Stay exactly the same', 'Disappear with no trace', 'Become invisible'], 0),
    ('Which of these is a sign that a chemical reaction is happening?', ['Bubbles or fizzing', 'Complete silence with no change', 'The object turning invisible', 'Nothing changing at all'], 0)]),
SS('Truth and Reconciliation Day: Learning and Remembering',
   'Grade 2 Social Studies strand: Truth and Reconciliation Day, on September 30, is a day when Canadians learn about and remember Indigenous children and communities, and work toward a fairer future together.',
   [('When is Truth and Reconciliation Day observed in Canada?', ['September 30', 'December 25', 'July 1', 'February 14'], 0),
    ('What is the purpose of Truth and Reconciliation Day?', ['To learn about and remember Indigenous children and communities', 'To ignore Canadian history', 'To celebrate a sports team', 'To mark the start of school'], 0),
    ('What colour is often worn on this day to show support and remembrance?', ['Orange', 'Blue', 'Green', 'Purple'], 0),
    ('Why is it important for schools to teach about Truth and Reconciliation Day?', ['To help students understand history and work toward fairness', 'It is not important', 'Only adults need to know about it', 'To avoid learning about Canada'], 0),
    ('Truth and Reconciliation Day encourages Canadians to work toward ___.', ['A fairer future together', 'Forgetting the past completely', 'Ignoring each other', 'Avoiding important conversations'], 0)]),
]),
day(136, [
L('Adages and Proverbs: Wise Sayings',
  'Grade 2 Language strand: adages and proverbs are short, wise sayings passed down over time, such as look before you leap, that teach a lesson in just a few words.',
  [('What is an adage or proverb?', ['A short, wise saying that teaches a lesson', 'A type of punctuation', 'A math equation', 'A characters name'], 0),
   ('What does the proverb look before you leap teach us?', ['To think carefully before acting', 'To jump as high as possible', 'To never look at anything', 'To leap without thinking'], 0),
   ('Why do people use proverbs?', ['To share wisdom in a short, memorable way', 'They have no meaning', 'To confuse listeners on purpose', 'To replace all other kinds of speech'], 0),
   ('Which of these is an example of a proverb?', ['Better late than never.', 'The sky is blue.', 'I have a red bike.', 'What time is it?'], 0),
   ('Proverbs are often passed down through ___.', ['Generations of people', 'A single scientific study', 'A math textbook only', 'A weather report'], 0)]),
M('Fractions Greater Than One: Introducing Mixed Numbers',
  'Grade 2 Math strand: a mixed number combines a whole number and a fraction, such as 1 and 1/2, to show an amount greater than one whole.',
  [('What is a mixed number?', ['A whole number combined with a fraction', 'A fraction with no whole number', 'A whole number only', 'A decimal only'], 0),
   ('What does the mixed number 1 and 1/2 represent?', ['One whole and half of another', 'Two wholes', 'Half of one whole only', 'Three halves as a whole number'], 0),
   ('If you have one whole pizza and half of another, how would you write this as a mixed number?', ['1 and 1/2', '1/2', '2', '3/2 only, no mixed form'], 0),
   ('A mixed number is used when an amount is ___.', ['Greater than one whole', 'Always less than one', 'Always exactly one', 'Never a fraction'], 0),
   ('Which of these is an example of a mixed number?', ['2 and 1/4', '1/4', '4', '0'], 0)]),
Sc('The Layers of the Atmosphere: Air Above Us',
   'Grade 2 Science strand: the atmosphere is made of layers of air surrounding the Earth, protecting us from the suns strong rays and giving us air to breathe.',
   [('What is the atmosphere?', ['Layers of air surrounding the Earth', 'A type of ocean', 'A layer of rock', 'A kind of cloud only'], 0),
    ('What does the atmosphere give living things to breathe?', ['Air', 'Water', 'Sunlight only', 'Sand'], 0),
    ('How does the atmosphere help protect Earth?', ['It blocks some of the suns strong rays', 'It has no protective purpose', 'It causes all storms', 'It blocks all sunlight completely'], 0),
    ('Which of these is part of the atmosphere?', ['The air we breathe', 'The rocky crust', 'The ocean floor', 'The core of the Earth'], 0),
    ('Without the atmosphere, Earth would not have ___ for living things to breathe.', ['Air', 'Sound', 'Colour', 'Gravity'], 0)]),
SS('Our Charter of Rights and Freedoms: Protecting Our Rights',
   'Grade 2 Social Studies strand: the Canadian Charter of Rights and Freedoms is a document that protects important rights for everyone in Canada, such as freedom of speech and equality.',
   [('What does the Charter of Rights and Freedoms protect?', ['Important rights for everyone in Canada', 'Only the rights of adults', 'Nothing important', 'Only the rights of one city'], 0),
    ('Which of these is a right the Charter protects?', ['Freedom of speech', 'The right to skip school', 'The right to ignore rules', 'The right to be unfair'], 0),
    ('Why is the Charter of Rights and Freedoms important?', ['It helps protect fairness and rights for everyone', 'It has no importance', 'It only protects a few people', 'It removes everyones rights'], 0),
    ('The Charter of Rights and Freedoms is part of ___.', ['Canadian law', 'A fictional story', 'A foreign countrys rules', 'A school rulebook only'], 0),
    ('Learning about the Charter helps students understand ___.', ['Their rights as Canadians', 'Nothing useful', 'Only rules for teachers', 'A made-up idea'], 0)]),
]),
day(137, [
L('Author Study: Learning About a Writers Style',
  'Grade 2 Language strand: an author study looks closely at one writer, exploring the special style, topics, or techniques that make their books recognizable.',
  [('What is an author study?', ['A close look at one writer and their style', 'A study of math facts', 'A study of weather patterns', 'A study of maps'], 0),
   ('What might students explore during an author study?', ['The writers style, topics, and techniques', 'The price of the book', 'Random unrelated facts', 'Nothing about the author'], 0),
   ('Why is it helpful to study one author closely?', ['It helps readers notice patterns in their writing', 'It has no benefit', 'It replaces reading their books', 'It confuses readers on purpose'], 0),
   ('Which of these might you notice during an author study?', ['The author often uses humour in their stories', 'The books exact weight', 'The books price', 'The number of pages only'], 0),
   ('An author study can help readers ___.', ['Understand what makes a writer unique', 'Ignore all books by that author', 'Avoid reading altogether', 'Only look at pictures'], 0)]),
M('Measurement: Converting Metres to Centimetres',
  'Grade 2 Math strand: students convert between metres and centimetres, remembering that one metre equals one hundred centimetres.',
  [('How many centimetres are in 1 metre?', ['10', '50', '100', '1000'], 2),
   ('How many centimetres are in 2 metres?', ['20', '100', '200', '2000'], 2),
   ('If an object is 150 centimetres long, how many metres is that?', ['1 metre', '1.5 metres', '15 metres', '150 metres'], 1),
   ('To convert metres to centimetres, we ___.', ['Multiply by 100', 'Divide by 100', 'Add 100', 'Subtract 100'], 0),
   ('How many centimetres are in 3 metres?', ['30', '300', '3000', '3'], 1)]),
Sc('Whales and Dolphins: Ocean Mammals',
   'Grade 2 Science strand: whales and dolphins are mammals that live in the ocean, breathe air through blowholes, and give birth to live young rather than laying eggs.',
   [('Are whales and dolphins classified as mammals or fish?', ['Fish', 'Mammals', 'Reptiles', 'Amphibians'], 1),
    ('How do whales and dolphins breathe air?', ['Through gills', 'Through a blowhole', 'Through their skin', 'They do not breathe'], 1),
    ('Do whales lay eggs or give birth to live young?', ['Lay eggs', 'Give birth to live young', 'Neither', 'Both equally'], 1),
    ('Why are whales and dolphins considered mammals and not fish?', ['They breathe air and give birth to live young', 'They live in water', 'They are large', 'They swim fast'], 0),
    ('Which of these is an ocean mammal?', ['Dolphin', 'Shark', 'Starfish', 'Jellyfish'], 0)]),
SS('The Klondike Gold Rush: A Canadian Adventure',
   'Grade 2 Social Studies strand: the Klondike Gold Rush was a time in the late 1800s when thousands of people travelled to the Yukon hoping to find gold.',
   [('What did people search for during the Klondike Gold Rush?', ['Gold', 'Silver', 'Oil', 'Coal'], 0),
    ('In which part of Canada did the Klondike Gold Rush happen?', ['The Yukon', 'Ontario', 'Nova Scotia', 'Quebec'], 0),
    ('When did the Klondike Gold Rush take place?', ['The late 1800s', 'The 1600s', 'Last year', 'The future'], 0),
    ('Why did so many people travel to the Yukon during this time?', ['They hoped to find gold and become wealthy', 'They wanted to visit the ocean', 'They were forced to move', 'There was no reason'], 0),
    ('Learning about the Klondike Gold Rush helps us understand ___.', ['An exciting part of Canadian history', 'Nothing about Canada', 'Only modern events', 'A fictional tale'], 0)]),
]),
day(138, [
L('Compound Sentences: Joining Ideas with Yet',
  'Grade 2 Language strand: compound sentences can join two ideas using the word yet to show contrast, similar to but, as in the game was long, yet exciting.',
  [('What does the word yet usually show when joining two ideas?', ['Contrast', 'Choice', 'Addition', 'Time order'], 0),
   ('Which sentence correctly uses yet to join two ideas?', ['The soup was hot, yet delicious.', 'The soup was hot, delicious.', 'The soup was hot yet.', 'Was hot yet the soup delicious.'], 0),
   ('Is yet similar in meaning to but?', ['Yes', 'No', 'They are opposites', 'Yet has no meaning'], 0),
   ('Which word could replace yet in a sentence showing contrast?', ['But', 'And', 'Or', 'So'], 0),
   ('Compound sentences join two complete ideas using words such as ___.', ['And, but, or, yet', 'The, a, an', 'Run, jump, skip', 'Red, blue, green'], 0)]),
M('Probability: Predicting with a Spinner',
  'Grade 2 Math strand: students use a spinner divided into sections to make predictions about which colour or number is more likely to be landed on.',
  [('If a spinner has 3 red sections and 1 blue section, which colour is more likely to be landed on?', ['Red', 'Blue', 'Both equally likely', 'Neither'], 0),
   ('If a spinner is divided into equal sections of red and blue, are the outcomes equally likely?', ['Yes', 'No', 'Red is always more likely', 'Blue is always more likely'], 0),
   ('What does a larger section on a spinner usually mean?', ['A greater chance of landing there', 'A smaller chance of landing there', 'No chance at all', 'It has no effect on chance'], 0),
   ('If a spinner has only one colour, what is the chance of landing on that colour?', ['Certain', 'Impossible', 'Unlikely', 'Never'], 0),
   ('Using a spinner to explore chance is an example of studying ___.', ['Probability', 'Perimeter', 'Area', 'Symmetry'], 0)]),
Sc('Migratory Birds: Long Journeys Across Continents',
   'Grade 2 Science strand: migratory birds travel very long distances each year between their summer and winter homes, often flying across countries or even continents.',
   [('What are migratory birds known for doing?', ['Traveling long distances between homes each year', 'Staying in one place forever', 'Never flying', 'Sleeping all year'], 0),
    ('Why might birds migrate to a different area?', ['To find better weather or food', 'For no reason at all', 'To avoid flying', 'To stay cold all year'], 0),
    ('How far might some migratory birds travel?', ['Across countries or even continents', 'Only a few steps', 'Never more than their nest', 'Only underwater'], 0),
    ('Which season might trigger some birds to begin migrating?', ['The changing of seasons, like fall approaching', 'A birthday', 'A holiday', 'A full moon only'], 0),
    ('Migration helps birds find ___ throughout the year.', ['Better food and weather', 'Nothing useful', 'More danger', 'Less food'], 0)]),
SS('O Canada: The Story of Our National Anthem',
   'Grade 2 Social Studies strand: O Canada is our national anthem, a special song that represents pride in and respect for our country, sung at many events across Canada.',
   [('What is the name of Canadas national anthem?', ['O Canada', 'God Save the King', 'This Land Is Your Land', 'True North'], 0),
    ('Why do people sing the national anthem?', ['To show pride and respect for their country', 'It is required with no meaning', 'To warm up before recess', 'It has no reason'], 0),
    ('Where might you hear O Canada being sung?', ['At a school assembly or hockey game', 'Only in outer space', 'Never anywhere', 'Only in other countries'], 0),
    ('A national anthem is a special ___ for a country.', ['Song', 'Food', 'Building', 'Animal'], 0),
    ('Singing O Canada is one way people show they ___ their country.', ['Care about', 'Ignore', 'Dislike', 'Forget'], 0)]),
]),
day(139, [
L('Editorial Cartoons: Pictures That Share an Opinion',
  'Grade 2 Language strand: an editorial cartoon uses pictures and few words to share an opinion about a topic or event, often in a funny or exaggerated way.',
  [('What does an editorial cartoon share?', ['An opinion about a topic or event', 'Only facts with no opinion', 'A math problem', 'A weather forecast only'], 0),
   ('How does an editorial cartoon usually share its message?', ['Through pictures and few words', 'Through a long essay', 'Through numbers only', 'Through silence'], 0),
   ('Editorial cartoons are often drawn in a ___ way.', ['Funny or exaggerated', 'Completely serious with no humour', 'Invisible', 'Blank'], 0),
   ('Why might someone create an editorial cartoon?', ['To share an opinion in a quick, visual way', 'It has no purpose', 'To share only facts with no viewpoint', 'To confuse the reader completely'], 0),
   ('Editorial cartoons are most similar to ___.', ['Persuasive writing in picture form', 'A recipe', 'A math worksheet', 'A dictionary entry'], 0)]),
M('Skip Counting by 25s to Count Money',
  'Grade 2 Math strand: students skip count by 25s to quickly find the value of a group of quarters, such as 25, 50, 75, and 100 cents.',
  [('What comes next: 25, 50, 75, ___?', ['85', '90', '100', '110'], 2),
   ('What is the value of four quarters skip counted by 25s?', ['50 cents', '75 cents', '90 cents', '100 cents'], 3),
   ('Skip counting by 25s helps us count ___ quickly.', ['Pennies', 'Quarters', 'Nickels', 'Dimes'], 1),
   ('What comes next: 100, 125, 150, ___?', ['160', '165', '175', '200'], 2),
   ('Three quarters together are worth ___.', ['50 cents', '65 cents', '75 cents', '100 cents'], 2)]),
Sc('Coral Polyps: The Tiny Animals That Build Reefs',
   'Grade 2 Science strand: coral reefs are built by tiny animals called coral polyps, which live together in large colonies and form hard skeletons over time.',
   [('What tiny animals build coral reefs?', ['Coral polyps', 'Fish', 'Jellyfish', 'Crabs'], 0),
    ('How do coral polyps live?', ['Together in large colonies', 'Completely alone', 'Underground', 'In trees'], 0),
    ('What do coral polyps form over time?', ['Hard skeletons that build up the reef', 'Soft feathers', 'Fur', 'Leaves'], 0),
    ('Why are coral reefs important?', ['They provide a home for many ocean creatures', 'They have no purpose', 'They harm ocean life', 'They only exist on land'], 0),
    ('Coral reefs grow very ___ over many years.', ['Slowly', 'Instantly', 'Never', 'Backwards'], 0)]),
SS('Our Governor General: A Ceremonial Role in Canada',
   'Grade 2 Social Studies strand: the Governor General represents the King or Queen in Canada, performing ceremonial duties such as welcoming important visitors and opening Parliament.',
   [('Who does the Governor General represent in Canada?', ['The mayor', 'The King or Queen', 'A foreign president', 'A local business'], 1),
    ('Which of these might be a duty of the Governor General?', ['Welcoming important visitors', 'Driving a school bus', 'Teaching a classroom', 'Selling groceries'], 0),
    ('The role of the Governor General is mostly ___.', ['Ceremonial', 'Related to farming', 'About sports', 'About cooking'], 0),
    ('Is the Governor General the same as the Prime Minister?', ['Yes, exactly the same', 'No, they have different roles', 'They never exist at the same time', 'Canada has neither'], 1),
    ('Learning about the Governor General helps us understand ___.', ['Part of how Canada is organized', 'Nothing useful', 'Only foreign countries', 'A made-up story'], 0)]),
]),
day(140, [
L('Language Review: Blends, Text Features, and Persuasive Forms',
  'Grade 2 Language strand review: students revisit three-letter blends, sidebars, postcards, rereading, debate writing, proverbs, author study, and editorial cartoons.',
  [('Which word begins with the str blend?', ['Splash', 'Street', 'Scream', 'Sit'], 1),
   ('What is a sidebar?', ['A small box of extra information beside the main text', 'The books cover', 'The last page', 'The table of contents'], 0),
   ('What does debate writing present?', ['Two different sides of an argument', 'Only one opinion with no other side', 'A made-up fantasy story', 'A recipe'], 0),
   ('What does the proverb look before you leap teach us?', ['To think carefully before acting', 'To jump as high as possible', 'To never look at anything', 'To leap without thinking'], 0),
   ('What does an editorial cartoon share?', ['An opinion about a topic or event', 'Only facts with no opinion', 'A math problem', 'A weather forecast only'], 0)]),
M('Math Review: Multiplication, Fractions, and Data',
  'Grade 2 Math strand review: students revisit multiplying by 4, arrays for division, comparing fractions, mixed numbers, converting metres, and spinner probability.',
  [('What is 6 x 4 using the double twice strategy?', ['20', '22', '24', '26'], 2),
   ('If 12 objects are arranged in an array with 3 rows, how many are in each row?', ['3', '4', '5', '6'], 1),
   ('Which is greater, 1/3 or 1/5?', ['1/3', '1/5', 'They are equal', 'Cannot tell'], 0),
   ('What does the mixed number 1 and 1/2 represent?', ['One whole and half of another', 'Two wholes', 'Half of one whole only', 'Three halves as a whole number'], 0),
   ('How many centimetres are in 1 metre?', ['10', '50', '100', '1000'], 2)]),
Sc('Science Review: Bodies, Oceans, and the Sky',
   'Grade 2 Science strand review: students revisit the human eye, ocean tides, the water table, genetics, chemical reactions, the atmosphere, and ocean mammals.',
   [('What organ do we use to see?', ['The eye', 'The ear', 'The nose', 'The skin'], 0),
    ('What mainly causes ocean tides?', ['The pull of the moons gravity', 'The wind alone', 'The sun disappearing', 'Fish swimming'], 0),
    ('What are traits passed down from parents called?', ['Inherited traits', 'Random traits', 'Fake traits', 'Borrowed traits'], 0),
    ('What is created when baking soda and vinegar react?', ['Bubbles of gas', 'A new solid rock', 'A rainbow', 'Sound only'], 0),
    ('Are whales and dolphins classified as mammals or fish?', ['Fish', 'Mammals', 'Reptiles', 'Amphibians'], 1)]),
SS('Social Studies Review: Leaders, Money, and Our History',
   'Grade 2 Social Studies strand review: students revisit Sir John A Macdonald, the Bank of Canada, the Coast Guard, Truth and Reconciliation Day, the Charter of Rights, and the Klondike Gold Rush.',
   [('Who was Canadas first prime minister?', ['Sir John A Macdonald', 'Terry Fox', 'A mayor', 'A premier'], 0),
    ('What does the Bank of Canada do?', ['Designs and issues Canadian money', 'Sells groceries', 'Teaches school', 'Delivers mail'], 0),
    ('What does the Coast Guard help keep people safe on?', ['The water', 'The road', 'The playground', 'The classroom'], 0),
    ('When is Truth and Reconciliation Day observed in Canada?', ['September 30', 'December 25', 'July 1', 'February 14'], 0),
    ('What did people search for during the Klondike Gold Rush?', ['Gold', 'Silver', 'Oil', 'Coal'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_131_140)
    append_to(2, g2_131_140)
