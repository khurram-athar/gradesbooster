#!/usr/bin/env python3
"""Grade 3, Days 141-150 -- extends Grade 3 from 140 to 150 days. Modeled
exactly on gen_grade3_days131_140.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task),
and the same title convention used throughout Grade 3 of a category
prefix baked into the title itself (Grammar:, Vocabulary:, Reading:,
Writing:, Oral Communication: for Language; Science: for Science; Social
Studies: for SocialStudies).

Topics chosen to avoid any overlap with the existing Grade 3 Days 1-140
topics (see data/grade3.json), which already densely cover nearly the
entire grade 3 Ontario curriculum, including all eight named physical
regions of Canada, several body systems (circulatory, nervous,
skeletal, respiratory, muscular), and most Canadian habitats. New
topics for this batch: semicolons, regional dialects, satire and
irony, movie reviews, debating, active/passive voice, sidebars and
pull quotes, eponyms, and adventure story openings for Language;
writing numbers in word form, classifying polygons by number of
sides, perimeter of composite figures, metric vs imperial units, the
median of a data set, comparing fractions with different denominators,
multiplying money amounts, dividing money amounts, and simple loans
and repayment for Math; the immune system, dinosaurs and extinction,
solar and lunar eclipses, cave habitats, sharks, bridge engineering,
water treatment plants, ants, and the excretory system for Science;
and National Indigenous Peoples Day, Orange Shirt Day and Truth and
Reconciliation, school boards and trustees, farmers markets, the
history of the Maple Leaf flag, public health units, provincial and
territorial flags, natural disaster preparedness, and the history of
the Canadian passport for Social Studies -- none of those exact ideas
appear in Days 1-140. Day 150 is a review day across all four
subjects, matching the end-of-batch pattern used in every prior
10-day batch, with review titles written to be textually distinct
from every earlier review days title (e.g. Day 140s). No embedded
ASCII double-quote or straight apostrophe characters are used anywhere
in title/summary/question/option text; apostrophes are dropped
entirely (e.g. Canadas instead of Canada with an apostrophe s),
matching the convention established in Days 111-140.

Invocation (matches the 131-140 script):
  cd ~/gradesbooster && python3 gen_grade3_days141_150.py
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


g3_141_150 = [
day(141, [
L('Grammar: Using Semicolons to Join Related Ideas',
  'Grade 3 Language strand: a semicolon can join two closely related independent clauses into a single sentence without using a conjunction such as and or but.',
  [('What can a semicolon join?', ['Two closely related independent clauses', 'Only a single word', 'Two unrelated paragraphs', 'A title and a page number'], 0),
   ('Which sentence correctly uses a semicolon?', ['The rain stopped; the sun came out.', 'The rain stopped; and the sun came out.', 'The rain stopped the sun came out.', 'The rain, stopped the sun came out.'], 0),
   ('A semicolon can sometimes replace which punctuation between two related sentences?', ['A period', 'A question mark', 'An exclamation mark', 'A hyphen'], 0),
   ('Why might a writer choose a semicolon instead of starting a new sentence?', ['To show the two ideas are closely connected', 'To make the sentence impossible to read', 'To remove the need for capital letters', 'To end the sentence early'], 0),
   ('The clauses joined by a semicolon should each be able to ___.', ['Stand alone as a complete sentence', 'Contain no verb', 'Contain no subject', 'Be a single word only'], 0)]),
M('Number: Writing Large Numbers in Word Form',
  'Grade 3 Math strand: students write whole numbers up to 100 000 in word form, using place value names such as thousand, hundred, and ten to express a number in words.',
  [('How do you write 5 342 in word form?', ['Five thousand, three hundred forty-two', 'Five hundred thirty-four', 'Fifty-three thousand forty-two', 'Five thousand, three hundred four'], 0),
   ('Which place value name is used when writing 12 000 in words?', ['Thousand', 'Hundred', 'Ten', 'One'], 0),
   ('How do you write 108 in word form?', ['One hundred eight', 'One thousand eight', 'Eighteen', 'One hundred eighty'], 0),
   ('Writing a number in word form means writing it using ___.', ['Words instead of digits', 'Only digits', 'Roman numerals', 'A picture'], 0),
   ('How do you write 90 015 in word form?', ['Ninety thousand, fifteen', 'Nine thousand, fifteen', 'Ninety thousand, one hundred five', 'Nine hundred fifteen'], 0)]),
Sc('Science: The Immune System — How Our Bodies Fight Germs',
   'Grade 3 Science strand: the immune system helps the body defend itself against harmful germs, using parts of the body such as white blood cells to fight infection and keep us healthy.',
   [('What is the main job of the immune system?', ['To help the body fight off harmful germs', 'To pump blood through the body', 'To digest food', 'To help us hear sounds'], 0),
    ('Which blood cells help fight germs in the body?', ['White blood cells', 'Red blood cells only', 'Skin cells only', 'Hair cells'], 0),
    ('What might happen if germs enter the body?', ['The immune system works to fight the germs off', 'Nothing ever happens', 'The body immediately stops working', 'The bones grow instantly'], 0),
    ('Which habit can help support a healthy immune system?', ['Washing hands regularly', 'Never washing hands', 'Avoiding sleep completely', 'Eating only sugar'], 0),
    ('Why is the immune system important to overall health?', ['It helps protect the body from illness', 'It has no real purpose', 'It only affects eye colour', 'It only affects hair growth'], 0)]),
SS('Social Studies: National Indigenous Peoples Day and Its Importance',
   'Grade 3 Social Studies strand: National Indigenous Peoples Day is celebrated each year to recognize and celebrate the cultures, achievements, and contributions of First Nations, Inuit, and Metis peoples in Canada.',
   [('What does National Indigenous Peoples Day celebrate?', ['The cultures and contributions of First Nations, Inuit, and Metis peoples', 'A single sports team', 'A type of weather pattern', 'A foreign holiday'], 0),
    ('Which groups are recognized on National Indigenous Peoples Day?', ['First Nations, Inuit, and Metis peoples', 'Only recent immigrants', 'Only government workers', 'Only explorers'], 0),
    ('Why might communities hold events on National Indigenous Peoples Day?', ['To honour and learn about Indigenous cultures and history', 'To ignore Indigenous history completely', 'To close all schools permanently', 'To cancel all celebrations'], 0),
    ('Learning about National Indigenous Peoples Day helps students understand ___.', ['The importance of Indigenous peoples to Canada', 'That Indigenous cultures no longer exist', 'That Canada has only one culture', 'That the day has no meaning'], 0),
    ('What kind of activities might take place on this day?', ['Cultural celebrations, storytelling, and educational events', 'No activities at all', 'Only silence and no events', 'Only private business meetings'], 0)]),
]),
day(142, [
L('Vocabulary: Regional Dialects and Word Choice',
  'Grade 3 Language strand: a dialect is a way of speaking used by people in a particular region, and speakers of different dialects may use different words or expressions for the same thing.',
  [('What is a dialect?', ['A way of speaking used by people in a particular region', 'A type of punctuation mark', 'A silent letter in a word', 'A rule for capitalization'], 0),
   ('Why might two people from different regions use different words for the same object?', ['Because they speak different regional dialects', 'Because one of them is wrong about the object', 'Because words never change between places', 'Because dialects do not exist'], 0),
   ('Which is an example of dialect differences?', ['One region calls it soda while another calls it pop', 'Every region uses identical words always', 'Dialects only affect punctuation', 'Dialects only affect spelling of names'], 0),
   ('Studying regional dialects helps readers understand ___.', ['That language can vary between places and communities', 'That there is only one correct way to speak', 'That dialects are always mistakes', 'That all English speakers sound identical'], 0),
   ('A dialect can include differences in ___.', ['Word choice, pronunciation, and expressions', 'Only handwriting style', 'Only the alphabet used', 'Only page numbers'], 0)]),
M('Geometry: Classifying Polygons by Number of Sides',
  'Grade 3 Math strand: polygons can be classified and named by their number of sides, such as a pentagon with five sides, a hexagon with six sides, and an octagon with eight sides.',
  [('How many sides does a pentagon have?', ['Five', 'Four', 'Six', 'Eight'], 0),
   ('How many sides does a hexagon have?', ['Six', 'Five', 'Seven', 'Four'], 0),
   ('How many sides does an octagon have?', ['Eight', 'Six', 'Five', 'Ten'], 0),
   ('A polygon is classified mainly by its ___.', ['Number of sides', 'Colour', 'Weight', 'Location on a page'], 0),
   ('Which shape is a quadrilateral?', ['A shape with four sides', 'A shape with three sides', 'A shape with five sides', 'A shape with six sides'], 0)]),
Sc('Science: Dinosaurs and Why They Went Extinct',
   'Grade 3 Science strand: dinosaurs were reptiles that lived on Earth millions of years ago, and scientists believe most dinosaurs went extinct after a major event, such as an asteroid impact, drastically changed their environment.',
   [('What were dinosaurs?', ['A group of reptiles that lived on Earth millions of years ago', 'A type of modern bird only', 'A type of modern fish', 'A type of plant'], 0),
    ('What does extinct mean?', ['A type of living thing no longer exists anywhere on Earth', 'A living thing that lives forever', 'A living thing that only lives in water', 'A living thing that never grows'], 0),
    ('What do many scientists believe caused most dinosaurs to go extinct?', ['A major event, such as an asteroid impact, changed their environment', 'They all decided to hide underground forever', 'They turned into modern birds overnight', 'Nothing happened to change their environment'], 0),
    ('How do scientists learn about dinosaurs today?', ['By studying fossils dinosaurs left behind', 'By interviewing dinosaurs directly', 'By guessing with no evidence', 'By reading modern newspapers only'], 0),
    ('Why do scientists continue to study dinosaur extinction?', ['To better understand how major events can change life on Earth', 'Because it has no scientific value', 'Because dinosaurs still exist today', 'Because it explains modern weather only'], 0)]),
SS('Social Studies: Orange Shirt Day and Truth and Reconciliation',
   'Grade 3 Social Studies strand: Orange Shirt Day is observed each year to honour residential school survivors and remember children who were affected, supporting truth and reconciliation between Indigenous peoples and other Canadians.',
   [('What does Orange Shirt Day honour?', ['Residential school survivors and the children affected by residential schools', 'A sports championship', 'A type of harvest festival', 'A national election'], 0),
    ('What colour shirt is worn to mark this day?', ['Orange', 'Blue', 'Green', 'Purple'], 0),
    ('What does reconciliation mean in this context?', ['Working to repair and improve relationships between Indigenous peoples and other Canadians', 'Ignoring history completely', 'Ending all communication between groups', 'Removing history from schools'], 0),
    ('Why is it important for students to learn about this history?', ['To understand this part of Canadas history and support reconciliation', 'Because the history has no importance', 'To avoid ever discussing it', 'Because it only affects one province'], 0),
    ('Orange Shirt Day encourages Canadians to reflect on ___.', ['The experiences of Indigenous children in residential schools', 'A type of weather pattern', 'A foreign countrys history only', 'A sports rivalry'], 0)]),
]),
day(143, [
L('Reading: Understanding Satire and Irony',
  'Grade 3 Language strand: satire uses humour or exaggeration to point out a problem, while irony happens when the actual result is different from what was expected, often creating a surprising or humorous effect.',
  [('What does satire often use to point out a problem?', ['Humour or exaggeration', 'Only silence', 'Only numbers', 'Only maps'], 0),
   ('What is irony?', ['When the actual result is different from what was expected', 'When everything happens exactly as expected', 'A type of punctuation mark', 'A type of rhyme scheme'], 0),
   ('Which is an example of irony?', ['A fire station burning down', 'A fire station being repaired on schedule', 'A fire station opening a new door', 'A fire station being painted red'], 0),
   ('Why might an author use satire in a story?', ['To point out a problem in a humorous or exaggerated way', 'To remove all humour from the story', 'To make the story impossible to understand', 'To avoid making any point at all'], 0),
   ('Recognizing irony helps readers ___.', ['Notice when the outcome differs from what was expected', 'Ignore the ending of a story', 'Avoid understanding the plot', 'Skip every sentence in a text'], 0)]),
M('Geometry: Finding the Perimeter of Composite Figures',
  'Grade 3 Math strand: the perimeter of a composite figure, made from two or more simple shapes joined together, can be found by adding the lengths of all its outer sides.',
  [('How can you find the perimeter of a composite figure?', ['Add the lengths of all its outer sides', 'Multiply the length by the width only', 'Count the number of shapes used', 'Subtract the smallest side from the largest'], 0),
   ('What is the perimeter of a composite figure with outer sides of 3, 4, 3, 2, and 2 cm?', ['14 cm', '12 cm', '10 cm', '16 cm'], 0),
   ('Why might you need to find missing side lengths first when calculating perimeter?', ['Some sides of a composite figure may not be labelled directly', 'Perimeter never requires side lengths', 'All composite figures have no sides', 'Composite figures never have missing lengths'], 0),
   ('Perimeter measures the distance ___.', ['Around the outside of a shape', 'Through the middle of a shape', 'Above a shape only', 'Below a shape only'], 0),
   ('A composite figure made of a rectangle and a triangle would have a perimeter equal to ___.', ['The sum of all its outer edge lengths', 'Only the rectangles perimeter', 'Only the triangles perimeter', 'Zero, since it is not a real shape'], 0)]),
Sc('Science: Eclipses — Solar and Lunar',
   'Grade 3 Science strand: a solar eclipse happens when the Moon passes between the Sun and Earth, blocking sunlight, while a lunar eclipse happens when Earth passes between the Sun and Moon, casting a shadow on the Moon.',
   [('What happens during a solar eclipse?', ['The Moon passes between the Sun and Earth, blocking sunlight', 'The Sun disappears forever', 'The Moon turns into a star', 'Earth stops spinning completely'], 0),
    ('What happens during a lunar eclipse?', ['Earth passes between the Sun and Moon, casting a shadow on the Moon', 'The Moon blocks all sunlight from Earth', 'The Sun passes between Earth and the Moon', 'The Moon disappears permanently'], 0),
    ('Why should people avoid looking directly at the Sun during a solar eclipse?', ['Looking directly at the Sun can harm the eyes', 'It is not safe to ever look at the sky', 'The Sun becomes invisible during an eclipse', 'It has no effect on the eyes at all'], 0),
    ('Which object casts a shadow during a lunar eclipse?', ['Earth', 'A distant star', 'A comet', 'A satellite'], 0),
    ('Eclipses occur because of the positions of the ___.', ['Sun, Earth, and Moon', 'Sun and a comet only', 'Moon and a distant planet only', 'Earth and a satellite only'], 0)]),
SS('Social Studies: The Role of School Boards and Trustees',
   'Grade 3 Social Studies strand: a school board oversees schools in a region, and elected trustees represent the community by making decisions about education, such as budgets and school programs.',
   [('What does a school board oversee?', ['Schools in a region', 'A single countrys military', 'A national sports league', 'A private business only'], 0),
    ('Who represents the community on a school board?', ['Elected trustees', 'Only the mayor', 'Only the Prime Minister', 'Only a single teacher'], 0),
    ('What kinds of decisions might a school board make?', ['Decisions about budgets and school programs', 'Decisions about a countrys foreign policy', 'Decisions about international trade', 'Decisions about national parks'], 0),
    ('How does someone typically become a school trustee?', ['Through a local election', 'Through a random lottery only', 'By inheriting the position', 'By being appointed by a business'], 0),
    ('Why is it useful for communities to have a school board?', ['It helps ensure schools meet the needs of local students', 'It has no purpose', 'It replaces the need for teachers', 'It only manages sports teams'], 0)]),
]),
day(144, [
L('Writing: Writing a Movie Review',
  'Grade 3 Language strand: a movie review shares an opinion about a film, giving reasons and examples to support the opinion and helping readers decide whether they might want to watch it.',
  [('What does a movie review share?', ['An opinion about a film, supported by reasons', 'Only the films runtime', 'Only the actors names', 'Nothing at all'], 0),
   ('Why might a movie review include specific examples from the film?', ['To support the reviewers opinion with evidence', 'To confuse the reader on purpose', 'To avoid discussing the film at all', 'To make the review shorter than one sentence'], 0),
   ('What might a reader do after reading a helpful movie review?', ['Decide whether they want to watch the movie', 'Immediately forget about the movie', 'Refuse to read any more reviews', 'Stop watching movies forever'], 0),
   ('A movie review often includes the reviewers opinion about which parts of a film?', ['The story, acting, and other key elements', 'Only the ticket price', 'Only the theatre location', 'Only the release date'], 0),
   ('Why is it helpful for a review to explain reasons behind an opinion?', ['So readers understand why the reviewer feels that way', 'So readers cannot understand the opinion at all', 'So the review has no purpose', 'So the film cannot be discussed further'], 0)]),
M('Measurement: Comparing Metric and Imperial Units',
  'Grade 3 Math strand: the metric system uses units such as metres and kilograms, while the imperial system uses units such as feet and pounds, and both systems can be used to measure length, mass, and capacity.',
  [('Which unit belongs to the metric system?', ['Metre', 'Foot', 'Pound', 'Inch'], 0),
   ('Which unit belongs to the imperial system?', ['Foot', 'Metre', 'Kilogram', 'Litre'], 0),
   ('Which system is commonly used for official measurements in Canada?', ['The metric system', 'The imperial system only', 'Neither system is ever used', 'A system with no units'], 0),
   ('Which pair of units both measure mass?', ['Kilogram and pound', 'Metre and litre', 'Foot and litre', 'Second and metre'], 0),
   ('Why is it useful to know both metric and imperial units?', ['Because both systems are still used in different situations', 'Because only one system has ever existed', 'Because units never need converting', 'Because imperial units measure time only'], 0)]),
Sc('Science: Cave Habitats and the Creatures That Live There',
   'Grade 3 Science strand: caves are dark, often damp habitats where specially adapted creatures such as bats, blind fish, and certain insects live, many of which have adaptations suited to little or no light.',
   [('What is a common feature of most cave habitats?', ['They are dark and often damp', 'They are always bright and sunny', 'They are always underwater oceans', 'They are always covered in snow'], 0),
    ('Which animal commonly lives in caves?', ['Bats', 'Polar bears', 'Camels', 'Penguins'], 0),
    ('Why might some cave-dwelling fish have no working eyes?', ['They have adapted to living in an environment with little or no light', 'They never needed eyes to begin with anywhere', 'Caves always have bright sunlight', 'Fish never adapt to their environment'], 0),
    ('What sense might cave animals rely on more than sight?', ['Hearing or touch', 'Taste only', 'Colour vision only', 'Sight is always their strongest sense'], 0),
    ('Why are cave habitats considered unique ecosystems?', ['Their conditions require special adaptations different from most habitats', 'They are identical to a desert habitat', 'They have no living creatures at all', 'They are always the warmest habitat on Earth'], 0)]),
SS('Social Studies: Farmers Markets and Local Food Systems',
   'Grade 3 Social Studies strand: a farmers market is a place where local farmers sell fresh produce and other goods directly to community members, supporting local food systems and the local economy.',
   [('What is a farmers market?', ['A place where local farmers sell fresh produce directly to the community', 'A large factory that makes cars', 'A government office building', 'A type of national holiday'], 0),
    ('What might someone buy at a farmers market?', ['Fresh fruits and vegetables grown locally', 'Airplane parts', 'Office furniture only', 'Foreign currency'], 0),
    ('How do farmers markets support the local economy?', ['They allow money to be spent directly with local farmers and producers', 'They remove all money from a community', 'They only benefit farmers in other countries', 'They have no effect on the economy'], 0),
    ('Why might buying local food reduce the distance food travels?', ['Because the food is grown and sold within the same community', 'Because local food is always imported from overseas', 'Because farmers markets ship goods around the world first', 'Because local food never comes from farms'], 0),
    ('What is one benefit of a local food system?', ['It can support local farmers and provide fresh food to the community', 'It removes the need for any farming', 'It only benefits large international companies', 'It has no impact on communities'], 0)]),
]),
day(145, [
L('Oral Communication: Debating Two Sides of an Issue',
  'Grade 3 Language strand: a debate involves presenting arguments for and against an issue, listening respectfully to other points of view, and supporting a position with reasons and evidence.',
  [('What does a debate involve?', ['Presenting arguments for and against an issue', 'Refusing to listen to anyone else', 'Ignoring all evidence', 'Avoiding any discussion at all'], 0),
   ('Why is it important to listen respectfully during a debate?', ['To understand other points of view even when you disagree', 'To ignore everyone else completely', 'To avoid ever changing your opinion', 'To interrupt every speaker'], 0),
   ('What should support a position in a debate?', ['Reasons and evidence', 'Random guesses only', 'Silence', 'Unrelated stories only'], 0),
   ('What are the two sides of a debate sometimes called?', ['For and against', 'Left and right only', 'Up and down', 'Loud and quiet'], 0),
   ('Why might students practise debating in class?', ['To build skills in reasoning, listening, and public speaking', 'To avoid learning how to communicate', 'To argue without any evidence', 'To eliminate the need for teamwork'], 0)]),
M('Data: Finding the Median of a Data Set',
  'Grade 3 Math strand: the median of a data set is the middle value when the numbers are arranged in order from least to greatest, and it is another way, along with mean and mode, to describe a set of data.',
  [('What is the median of a data set?', ['The middle value when the numbers are arranged in order', 'The largest value in the data set', 'The smallest value in the data set', 'The sum of all the values'], 0),
   ('What is the median of the data set 2, 5, 7?', ['5', '2', '7', '14'], 0),
   ('Before finding the median, what should you do with the data?', ['Arrange the numbers in order from least to greatest', 'Multiply every number by two', 'Remove all the numbers', 'Add all the numbers together'], 0),
   ('What is the median of the data set 1, 3, 3, 6, 9?', ['3', '6', '9', '1'], 0),
   ('Median, mean, and mode are all ways to describe ___.', ['A data set', 'A single shape', 'A type of map', 'A calendar'], 0)]),
Sc('Science: Sharks and Their Adaptations for Ocean Life',
   'Grade 3 Science strand: sharks are fish with skeletons made of cartilage instead of bone, and they have adaptations such as sharp teeth and a strong sense of smell that help them survive as ocean predators.',
   [('What is a sharks skeleton made of?', ['Cartilage', 'Bone', 'Wood', 'Metal'], 0),
    ('What adaptation helps sharks catch prey?', ['Sharp teeth', 'Feathers', 'Fur', 'Wings'], 0),
    ('Which sense is especially strong in many sharks?', ['Smell', 'Taste only', 'Sight only', 'Touch only'], 0),
    ('What type of animal is a shark?', ['A fish', 'A mammal', 'A reptile', 'An amphibian'], 0),
    ('Why are sharks considered important predators in ocean ecosystems?', ['They help keep populations of other ocean animals balanced', 'They have no role in the ocean at all', 'They only live on land', 'They never eat other animals'], 0)]),
SS('Social Studies: How Canada Chose Its Maple Leaf Flag in 1965',
   'Grade 3 Social Studies strand: Canada adopted its red and white maple leaf flag in 1965, after a national discussion about choosing a flag design that would represent the whole country.',
   [('In what year did Canada adopt its maple leaf flag?', ['1965', '1867', '1812', '2000'], 0),
    ('What are the colours of the Canadian flag?', ['Red and white', 'Blue and yellow', 'Green and gold', 'Black and orange'], 0),
    ('What symbol is at the centre of the Canadian flag?', ['A maple leaf', 'A beaver', 'A crown', 'A star'], 0),
    ('Why did Canada hold a national discussion before choosing a flag design?', ['To choose a design that would represent the whole country', 'To avoid ever having a flag', 'To copy another countrys flag exactly', 'To remove all symbols from Canada'], 0),
    ('Why is the story of the flags design important to learn?', ['It shows how Canadians worked together to create a national symbol', 'It has no connection to Canadian history', 'It only matters to one province', 'It explains a foreign countrys history'], 0)]),
]),
day(146, [
L('Grammar: Active and Passive Voice',
  'Grade 3 Language strand: in an active voice sentence, the subject performs the action, while in a passive voice sentence, the subject receives the action, often making active voice clearer and more direct.',
  [('In an active voice sentence, who performs the action?', ['The subject', 'The object', 'No one', 'The verb itself'], 0),
   ('Which sentence is written in active voice?', ['The dog chased the ball.', 'The ball was chased by the dog.', 'The ball was thrown.', 'The game was played.'], 0),
   ('Which sentence is written in passive voice?', ['The cake was baked by the chef.', 'The chef baked the cake.', 'The chef bakes cakes daily.', 'The chef enjoys baking.'], 0),
   ('Why might a writer prefer active voice in most writing?', ['It is often clearer and more direct', 'It always makes writing confusing', 'It removes the subject from every sentence', 'It hides who performed the action'], 0),
   ('In passive voice, the subject of the sentence ___.', ['Receives the action', 'Always performs the action', 'Is always missing entirely', 'Cannot exist'], 0)]),
M('Fractions: Comparing Fractions with Different Denominators',
  'Grade 3 Math strand: to compare fractions with different denominators, students can find equivalent fractions with a common denominator or use a model such as a number line or fraction strip.',
  [('Which fraction is greater: 1/2 or 1/3?', ['1/2', '1/3', 'They are equal', 'Cannot be determined'], 0),
   ('To compare fractions with different denominators, it can help to first find a ___.', ['Common denominator', 'Common numerator only', 'Larger whole number', 'Smaller whole number'], 0),
   ('Which fraction is greater: 2/5 or 2/3?', ['2/3', '2/5', 'They are equal', 'Cannot be determined'], 0),
   ('What tool can help visually compare two fractions?', ['A fraction strip or number line', 'A thermometer', 'A calendar', 'A compass rose'], 0),
   ('Which fraction is smaller: 3/4 or 1/4?', ['1/4', '3/4', 'They are equal', 'Cannot be determined'], 0)]),
Sc('Science: Engineering Bridges — Beam, Arch, and Suspension',
   'Grade 3 Science strand: engineers design different types of bridges, such as beam, arch, and suspension bridges, choosing a design based on the distance to be crossed and the forces the bridge must withstand.',
   [('What is a beam bridge?', ['A simple bridge supported by beams resting on piers', 'A bridge made entirely of rope', 'A bridge with no supports at all', 'A bridge that floats on water only'], 0),
    ('What shape gives an arch bridge much of its strength?', ['A curved arch shape', 'A flat rectangle', 'A perfect circle', 'A straight line only'], 0),
    ('What holds up the road on a suspension bridge?', ['Cables hung from tall towers', 'Nothing at all', 'A single wooden beam', 'Balloons'], 0),
    ('Why might engineers choose different bridge designs?', ['Based on the distance to be crossed and forces the bridge must withstand', 'Because all bridges must look identical', 'Because bridge design does not matter', 'Because only one bridge design has ever existed'], 0),
    ('What is one important goal when engineering a bridge?', ['Making sure it can safely support weight and withstand forces', 'Making sure it collapses quickly', 'Making sure it is invisible', 'Making sure it has no purpose'], 0)]),
SS('Social Studies: Public Health Units and Keeping Communities Well',
   'Grade 3 Social Studies strand: a public health unit works to protect and promote the health of a community, offering services such as vaccination programs and health education.',
   [('What does a public health unit work to protect?', ['The health of a community', 'Only the health of one household', 'A countrys military strength', 'A private companys profits'], 0),
    ('Which is an example of a service a public health unit might offer?', ['Vaccination programs', 'Selling groceries', 'Fixing roads', 'Delivering mail'], 0),
    ('Why might a public health unit provide health education?', ['To help community members make informed health decisions', 'To confuse the public on purpose', 'To prevent people from learning about health', 'To replace all doctors'], 0),
    ('Public health units are an example of a service that benefits ___.', ['The whole community', 'Only one single person', 'Only government workers', 'No one at all'], 0),
    ('Why is community health considered a shared responsibility?', ['Because the health of individuals can affect the wellbeing of the whole community', 'Because health has no effect on communities', 'Because only doctors need to think about health', 'Because communities never need health services'], 0)]),
]),
day(147, [
L('Reading: Text Features — Sidebars and Pull Quotes',
  'Grade 3 Language strand: sidebars provide extra information related to a main article, while pull quotes highlight an important sentence from the text in larger print to draw a readers attention.',
  [('What does a sidebar provide?', ['Extra information related to the main article', 'The entire main article only', 'A blank page', 'A table of contents only'], 0),
   ('What is a pull quote?', ['An important sentence from the text highlighted in larger print', 'A footnote at the bottom of a page', 'The title of the article', 'A list of page numbers'], 0),
   ('Why might a writer include a sidebar in a nonfiction article?', ['To share extra details without interrupting the main text', 'To remove information from the article', 'To replace the entire article', 'To confuse the reader on purpose'], 0),
   ('Why might a pull quote be printed in larger text?', ['To draw the readers attention to an important idea', 'To make the text harder to notice', 'To hide the quote from readers', 'To replace the main article entirely'], 0),
   ('Sidebars and pull quotes are both examples of ___.', ['Text features that support a main article', 'Types of punctuation marks', 'Types of verbs', 'Types of vowels'], 0)]),
M('Multiplication: Multiplying Money Amounts',
  'Grade 3 Math strand: students multiply money amounts by a whole number, such as finding the total cost of several identical items, using the same strategies used for multiplying whole numbers.',
  [('If one notebook costs 4 dollars, how much do 3 notebooks cost?', ['12 dollars', '9 dollars', '15 dollars', '10 dollars'], 0),
   ('What is 6 dollars multiplied by 5?', ['30 dollars', '25 dollars', '35 dollars', '20 dollars'], 0),
   ('When multiplying money amounts, the strategies used are ___.', ['The same strategies used for multiplying whole numbers', 'Completely different from whole number multiplication', 'Never useful for money', 'Only useful for division'], 0),
   ('If one ticket costs 8 dollars, what is the cost of 4 tickets?', ['32 dollars', '28 dollars', '24 dollars', '36 dollars'], 0),
   ('Why might someone multiply money amounts in everyday life?', ['To find the total cost of buying several of the same item', 'To avoid ever shopping', 'To subtract prices instead', 'To ignore the cost of items'], 0)]),
Sc('Science: How Water Treatment Plants Clean Our Water',
   'Grade 3 Science strand: a water treatment plant cleans water by removing dirt, germs, and other impurities through steps such as filtering and adding safe chemicals, making the water safe to drink.',
   [('What is the main job of a water treatment plant?', ['To clean water and make it safe to drink', 'To make water dirtier', 'To remove all water from a city', 'To turn water into ice permanently'], 0),
    ('Which step might a water treatment plant use to clean water?', ['Filtering out dirt and impurities', 'Adding more dirt to the water', 'Removing all water molecules', 'Freezing all the water forever'], 0),
    ('Why is it important for water to be treated before people drink it?', ['To remove germs and impurities that could make people sick', 'Because untreated water is always perfectly safe', 'Because treatment makes water undrinkable', 'Because water never needs cleaning'], 0),
    ('Where does the water used in a water treatment plant often come from?', ['Rivers, lakes, or underground sources', 'Only from outer space', 'Only from clouds directly', 'Only from a single well in one city'], 0),
    ('Why might scientists test water quality after it is treated?', ['To make sure the water is safe before people use it', 'Because testing water is unnecessary', 'To make the water less safe', 'Because water never needs to be tested'], 0)]),
SS('Social Studies: Canadas Provincial and Territorial Flags',
   'Grade 3 Social Studies strand: each Canadian province and territory has its own flag, often featuring symbols that represent the regions history, geography, or identity.',
   [('What does each Canadian province and territory have?', ['Its own flag', 'No symbols at all', 'Only one shared flag for all of Canada', 'A flag identical to another country'], 0),
    ('What might symbols on a provincial flag represent?', ['The regions history, geography, or identity', 'Nothing meaningful at all', 'Only a sports team', 'Only a private business'], 0),
    ('Why might different provinces choose different flag designs?', ['To reflect their own unique history and identity', 'Because all provinces are required to look the same', 'Because flags have no meaning', 'Because provinces are not allowed to have flags'], 0),
    ('Where might you see a provincial or territorial flag displayed?', ['On government buildings within that province or territory', 'Only inside a private home', 'Only in another country', 'Nowhere at all'], 0),
    ('Learning about provincial and territorial flags helps students understand ___.', ['The diversity of Canadas regions', 'That Canada has no regional differences', 'That flags are unimportant', 'That only the national flag exists'], 0)]),
]),
day(148, [
L('Vocabulary: Eponyms — Words Named After People',
  'Grade 3 Language strand: an eponym is a word that comes from the name of a real or fictional person, such as the sandwich, which is said to be named after the Earl of Sandwich.',
  [('What is an eponym?', ['A word that comes from the name of a person', 'A word with no meaning at all', 'A type of punctuation mark', 'A word that rhymes with another word'], 0),
   ('The word sandwich is said to be named after ___.', ['The Earl of Sandwich', 'A type of bread only', 'A famous river', 'A type of vegetable'], 0),
   ('Why might learning about eponyms be interesting to readers?', ['It reveals surprising stories behind everyday words', 'It removes all meaning from words', 'It has nothing to do with word origins', 'It only applies to made-up words'], 0),
   ('An eponym can come from either a real or a ___ person.', ['Fictional', 'Silent', 'Punctuated', 'Numbered'], 0),
   ('Studying eponyms is related to the study of ___.', ['Etymology, or where words come from', 'Handwriting only', 'Grammar rules only', 'Punctuation marks only'], 0)]),
M('Division: Dividing Money Amounts Evenly',
  'Grade 3 Math strand: students divide money amounts evenly among a group, such as sharing the cost of an item or splitting an amount of money into equal parts.',
  [('If 12 dollars is shared evenly among 3 friends, how much does each friend get?', ['4 dollars', '3 dollars', '6 dollars', '9 dollars'], 0),
   ('What is 20 dollars divided evenly among 5 people?', ['4 dollars', '5 dollars', '10 dollars', '15 dollars'], 0),
   ('If 4 people share the cost of a 24 dollar pizza equally, how much does each person pay?', ['6 dollars', '4 dollars', '8 dollars', '12 dollars'], 0),
   ('Dividing money evenly means each part receives ___.', ['An equal share of the total amount', 'A different amount each time', 'Nothing at all', 'The entire total amount'], 0),
   ('What is 18 dollars divided evenly among 3 people?', ['6 dollars', '9 dollars', '3 dollars', '15 dollars'], 0)]),
Sc('Science: Ants and Their Underground Colonies',
   'Grade 3 Science strand: ants are social insects that live in large underground colonies, with different ants performing different roles, such as workers, soldiers, and a queen who lays eggs.',
   [('Where do many ant colonies live?', ['Underground', 'Underwater only', 'High in the clouds', 'Inside solid rock only'], 0),
    ('What role does the queen ant play in a colony?', ['She lays eggs for the colony', 'She builds every tunnel alone', 'She never stays in the colony', 'She has no role at all'], 0),
    ('What term describes insects like ants that live and work together in large groups?', ['Social insects', 'Solitary insects', 'Silent insects', 'Aquatic insects'], 0),
    ('Which ants often gather food for the colony?', ['Worker ants', 'Only the queen', 'No ants gather food', 'Only soldier ants sleep instead'], 0),
    ('Why might soldier ants be important to a colony?', ['They help defend the colony from threats', 'They never help the colony', 'They only eat and do nothing else', 'They replace the queen every day'], 0)]),
SS('Social Studies: How Communities Prepare for Natural Disasters',
   'Grade 3 Social Studies strand: communities prepare for natural disasters such as floods, storms, and forest fires by creating emergency plans, stocking supplies, and practising safety drills.',
   [('What is one way communities prepare for natural disasters?', ['Creating emergency plans', 'Ignoring the possibility of any disaster', 'Removing all safety equipment', 'Avoiding any preparation at all'], 0),
    ('Which is an example of a natural disaster?', ['A flood', 'A birthday party', 'A school assembly', 'A sports game'], 0),
    ('Why might a community stock emergency supplies?', ['To be ready to respond quickly if a disaster occurs', 'Because supplies are never needed', 'To use them for everyday shopping only', 'Because disasters never happen'], 0),
    ('What is the purpose of practising a safety drill?', ['To help people know what to do if an emergency happens', 'To confuse people during an emergency', 'To waste time with no purpose', 'To prevent people from ever learning safety steps'], 0),
    ('Why is disaster preparedness considered a shared community effort?', ['Everyone benefits when a community is ready to respond safely', 'Only one person needs to prepare for everyone', 'Disaster preparedness never involves communities', 'Preparation only matters for large cities'], 0)]),
]),
day(149, [
L('Writing: Writing an Adventure Story Opening',
  'Grade 3 Language strand: an adventure story opening introduces an exciting setting or situation, often using vivid details and action to capture the readers interest right away.',
  [('What should an adventure story opening do?', ['Capture the readers interest right away', 'Bore the reader immediately', 'Avoid describing any setting', 'Skip introducing any characters or setting'], 0),
   ('Which is a strong opening line for an adventure story?', ['The old map crackled as Maya unrolled it in the dark cave.', 'It was a day.', 'Nothing happened at all.', 'The end.'], 0),
   ('Why might a writer use vivid details in a story opening?', ['To help readers picture the setting and feel drawn into the story', 'To make the story impossible to imagine', 'To remove all imagery from the writing', 'To confuse the reader on purpose'], 0),
   ('An exciting adventure story opening often introduces ___.', ['An exciting setting or situation', 'Only a list of facts', 'Only a table of contents', 'Only a glossary of terms'], 0),
   ('Why is the opening of a story especially important?', ['It helps decide whether a reader wants to keep reading', 'It has no effect on the reader at all', 'It should always be left blank', 'It should always come after the ending'], 0)]),
M('Financial Literacy: Understanding Simple Loans and Repayment',
  'Grade 3 Math strand: a loan is money borrowed that must be paid back over time, often in equal payments, and understanding loans helps students see how borrowing and repaying money works.',
  [('What is a loan?', ['Money that is borrowed and must be paid back', 'Money that never needs to be returned', 'A type of savings account only', 'A gift with no conditions'], 0),
   ('If you borrow 100 dollars and repay it in 4 equal payments, how much is each payment?', ['25 dollars', '20 dollars', '30 dollars', '40 dollars'], 0),
   ('Why might someone take out a loan?', ['To pay for something now and repay the amount over time', 'To avoid ever spending money', 'To give money away permanently', 'To remove the need for saving'], 0),
   ('What does it mean to repay a loan?', ['To pay back the money that was borrowed', 'To borrow even more money', 'To ignore the amount owed', 'To spend the loan on something else only'], 0),
   ('Why is it important to repay a loan responsibly?', ['To meet the agreement made when borrowing the money', 'Because repayment is never expected', 'Because loans do not need to be repaid', 'Because lenders never track repayment'], 0)]),
Sc('Science: The Excretory System — Removing Waste from the Body',
   'Grade 3 Science strand: the excretory system removes waste products from the body, with organs such as the kidneys filtering waste from the blood so the body can stay healthy.',
   [('What is the main job of the excretory system?', ['To remove waste products from the body', 'To pump blood through the body', 'To help the body think', 'To help the body hear sounds'], 0),
    ('Which organ filters waste from the blood?', ['The kidneys', 'The eyes', 'The tongue', 'The ears'], 0),
    ('Why is it important for the body to remove waste?', ['To keep the body healthy and functioning properly', 'Waste removal has no benefit to the body', 'It only affects hair growth', 'It only affects eyesight'], 0),
    ('The excretory system works together with which other body system to keep the body healthy?', ['The circulatory system', 'The system that controls hearing only', 'A system that does not exist', 'The system that controls taste only'], 0),
    ('What might happen if the excretory system did not work properly?', ['Waste could build up in the body and cause health problems', 'Nothing would ever change in the body', 'The body would immediately grow taller', 'The body would stop needing food'], 0)]),
SS('Social Studies: The History of the Canadian Passport',
   'Grade 3 Social Studies strand: a passport is an official document that allows a person to travel internationally and proves their identity and citizenship, and Canadas passport has changed in design over many years.',
   [('What is a passport?', ['An official document that proves identity and citizenship for travel', 'A type of currency', 'A type of map', 'A type of holiday'], 0),
    ('Why might someone need a passport?', ['To travel internationally and prove their citizenship', 'To buy groceries locally', 'To attend a local school', 'To ride a citys public bus'], 0),
    ('What information does a passport typically confirm?', ['A persons identity and citizenship', 'Only a persons favourite colour', 'Only a persons favourite food', 'Only a persons height'], 0),
    ('How has the Canadian passport changed over many years?', ['Its design and security features have been updated over time', 'It has never changed since it was first created', 'It has never included any personal information', 'It has always looked identical to every other countrys passport'], 0),
    ('Why might governments update passport security features over time?', ['To help prevent fraud and keep travel documents secure', 'To make passports easier to forge', 'To remove all security from travel documents', 'Because security has no importance'], 0)]),
]),
day(150, [
L('Language Review: Semicolons, Satire, and Debate Skills',
  'Grade 3 Language strand review: students revisit using semicolons, regional dialects, satire and irony, writing a movie review, debating two sides of an issue, active and passive voice, sidebars and pull quotes, eponyms, and writing an adventure story opening.',
  [('What can a semicolon join?', ['Two closely related independent clauses', 'Only a single word', 'Two unrelated paragraphs', 'A title and a page number'], 0),
   ('What is irony?', ['When the actual result is different from what was expected', 'When everything happens exactly as expected', 'A type of punctuation mark', 'A type of rhyme scheme'], 0),
   ('What does a debate involve?', ['Presenting arguments for and against an issue', 'Refusing to listen to anyone else', 'Ignoring all evidence', 'Avoiding any discussion at all'], 0),
   ('In an active voice sentence, who performs the action?', ['The subject', 'The object', 'No one', 'The verb itself'], 0),
   ('What is an eponym?', ['A word that comes from the name of a person', 'A word with no meaning at all', 'A type of punctuation mark', 'A word that rhymes with another word'], 0)]),
M('Math Review: Polygons, Fractions, and Financial Literacy',
  'Grade 3 Math strand review: students revisit writing numbers in word form, classifying polygons by number of sides, perimeter of composite figures, metric versus imperial units, the median of a data set, comparing fractions with different denominators, multiplying money, dividing money, and simple loans.',
  [('How many sides does a hexagon have?', ['Six', 'Five', 'Seven', 'Four'], 0),
   ('How can you find the perimeter of a composite figure?', ['Add the lengths of all its outer sides', 'Multiply the length by the width only', 'Count the number of shapes used', 'Subtract the smallest side from the largest'], 0),
   ('What is the median of a data set?', ['The middle value when the numbers are arranged in order', 'The largest value in the data set', 'The smallest value in the data set', 'The sum of all the values'], 0),
   ('Which fraction is greater: 1/2 or 1/3?', ['1/2', '1/3', 'They are equal', 'Cannot be determined'], 0),
   ('What is a loan?', ['Money that is borrowed and must be paid back', 'Money that never needs to be returned', 'A type of savings account only', 'A gift with no conditions'], 0)]),
Sc('Science Review: Body Systems, Space, and Engineering',
   'Grade 3 Science strand review: students revisit the immune system, dinosaurs and extinction, solar and lunar eclipses, cave habitats, sharks, bridge engineering, water treatment plants, ants, and the excretory system.',
   [('What is the main job of the immune system?', ['To help the body fight off harmful germs', 'To pump blood through the body', 'To digest food', 'To help us hear sounds'], 0),
    ('What does extinct mean?', ['A type of living thing no longer exists anywhere on Earth', 'A living thing that lives forever', 'A living thing that only lives in water', 'A living thing that never grows'], 0),
    ('What happens during a solar eclipse?', ['The Moon passes between the Sun and Earth, blocking sunlight', 'The Sun disappears forever', 'The Moon turns into a star', 'Earth stops spinning completely'], 0),
    ('What is a sharks skeleton made of?', ['Cartilage', 'Bone', 'Wood', 'Metal'], 0),
    ('Which organ filters waste from the blood?', ['The kidneys', 'The eyes', 'The tongue', 'The ears'], 0)]),
SS('Social Studies Review: Reconciliation, Civics, and Canadian Symbols',
   'Grade 3 Social Studies strand review: students revisit National Indigenous Peoples Day, Orange Shirt Day and truth and reconciliation, school boards and trustees, farmers markets, the history of the Maple Leaf flag, public health units, provincial and territorial flags, natural disaster preparedness, and the Canadian passport.',
   [('What does National Indigenous Peoples Day celebrate?', ['The cultures and contributions of First Nations, Inuit, and Metis peoples', 'A single sports team', 'A type of weather pattern', 'A foreign holiday'], 0),
    ('What does Orange Shirt Day honour?', ['Residential school survivors and the children affected by residential schools', 'A sports championship', 'A type of harvest festival', 'A national election'], 0),
    ('In what year did Canada adopt its maple leaf flag?', ['1965', '1867', '1812', '2000'], 0),
    ('What does a public health unit work to protect?', ['The health of a community', 'Only the health of one household', 'A countrys military strength', 'A private companys profits'], 0),
    ('What is a passport?', ['An official document that proves identity and citizenship for travel', 'A type of currency', 'A type of map', 'A type of holiday'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_141_150, seed=20260807)
    append_to(3, g3_141_150)
