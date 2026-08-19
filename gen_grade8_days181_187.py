#!/usr/bin/env python3
"""Grade 8, Days 181-187 -- extends Grade 8 from 180 to 187 days, completing
the full 187-day Ontario curriculum target for this grade (the final batch
for Grade 8). This batch is only 7 days, not the usual 9 or 10, because
180 + 7 = 187. It is structured as 6 new content days (181-186, one new
topic per subject per day) plus Day 187, a final cross-subject review day.

Topics chosen after dumping the existing Day 1-180 title list
(data/grade8.json) in full to avoid any overlap:

Language (181-186): the serial (Oxford) comma and clarity in lists;
jargon and technical language across fields; circular structure and
full-circle endings in narrative; the debate rebuttal and
counterargument; distinguishing satire from misinformation online; and
recognizing and avoiding comma splices.

Math (181-186): variance; the Sieve of Eratosthenes; partial fraction
decomposition; the Coupon Collectors Problem; the centroid, circumcenter,
and orthocenter of a triangle; and the coefficient of variation.

Science (181-186): the chemistry of baking and leavening agents; the
physics of optical illusions and visual perception; fossils and the
fossil record; camouflage and animal defense mechanisms; the search for
water on Mars; and how water desalination works.

History (181-186): the discovery of insulin by Banting and Best; the
Great Canadian Flag Debate and the maple leaf flag of 1965; the
construction of the CN Tower; the Manitoba flood of 1950 and the
building of the Winnipeg Floodway; the Confederation Bridge linking
Prince Edward Island by land; and O Canada becoming Canadas official
national anthem in 1980.

None of these topics or titles duplicate any Day 1-180 subject or title
(cross-checked against the full title dump of data/grade8.json). Day 187
is the final cross-subject review day of the entire 187-day K-12
curriculum build for this grade. Following the exact mechanical
review-day pattern established in gen_grade8_days171_180.py, each review
section draws its five questions from the first question of each of the
first five new days (181-185), while each review title covers the full
new-day range (Days 181-186), matching how Day 180 covered Days 171-179
in its title while sourcing questions only from Days 171-175. Each
review title uses wording distinct from every earlier review days title,
and each review summary briefly notes that this is the final review of
the K-12 curriculum build for this grade.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches; Grade 8 uses History, not
SocialStudies, as its fourth subject).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
apostrophe or double-quote characters are used anywhere in
title/question/summary/option text; apostrophes are dropped entirely,
matching the convention used in gen_grade8_days171_180.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-history'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science and Technology',
    'TVO Learn: Grade 8 History',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L8, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M8, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S8, q)


def H(t, s, q):
    return sub('History', t, s, RH, H8, q)


def _rebalance_answer_positions(days, seed=20260818):
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


g8_181_187 = [
day(181, [
L('Grammar: The Serial Comma and Clarity in Lists',
  'Grade 8 Language strand: the serial comma, also known as the Oxford comma, is the comma placed before the coordinating conjunction in a list of three or more items, and using it consistently can prevent a sentence from being misread.',
  [('What is another common name for the serial comma?', ['The Oxford comma', 'The Cambridge comma', 'The London comma', 'The Harvard colon'], 0),
   ('Where does a serial comma appear in a list?', ['Before the coordinating conjunction that joins the final two items', 'After the very first item only', 'At the start of the sentence', 'Only after numbers'], 0),
   ('How many items does a list typically need before a serial comma becomes relevant?', ['Three or more', 'Exactly two', 'Only one', 'At least ten'], 0),
   ('What problem can omitting the serial comma sometimes cause in a sentence?', ['The final two items in a list may seem to be grouped together as one item', 'The sentence becomes automatically grammatically incorrect', 'The sentence loses its subject entirely', 'All punctuation in the sentence is removed'], 0),
   ('Why do many style guides recommend using the serial comma consistently?', ['Consistent use avoids ambiguity no matter how a particular list is phrased', 'It is required in every language on earth', 'It eliminates the need for periods', 'It changes the meaning of every noun in a sentence'], 0)]),
M('Statistics: An Introduction to Variance',
  'Grade 8 Math strand: variance measures how far a set of data values are spread out from their mean by averaging the squared differences between each value and the mean, giving more weight to values that are farther away.',
  [('What does variance measure about a data set?', ['How far the data values are spread out from the mean', 'The exact largest value in the data set', 'The total number of values in the data set', 'The order in which data was collected'], 0),
   ('How is variance calculated from a data set?', ['By averaging the squared differences between each value and the mean', 'By adding all the values together only', 'By counting how many values are above zero', 'By multiplying every value by two'], 0),
   ('Why are the differences from the mean squared when calculating variance?', ['Squaring prevents negative and positive differences from cancelling out and emphasizes larger gaps', 'Squaring makes every difference equal to zero', 'Squaring removes the need for a mean', 'Squaring always produces a negative number'], 0),
   ('What does a very small variance suggest about a data set?', ['The values are clustered closely around the mean', 'The values are spread across a huge range', 'The mean cannot be calculated', 'The data set has no numerical values'], 0),
   ('Why is variance a useful measure alongside the mean when describing a data set?', ['It shows how consistent or spread out the data is, which the mean alone cannot show', 'It always equals the mean in every data set', 'It replaces the need to ever calculate a mean', 'It can only be used with exactly two data points'], 0)]),
Sc('Chemistry: The Chemistry of Baking and Leavening Agents',
   'Grade 8 Science strand: leavening agents such as baking soda and baking powder release carbon dioxide gas through chemical reactions, creating bubbles that cause dough or batter to rise during baking.',
   [('What gas do leavening agents such as baking soda release during baking?', ['Carbon dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'], 0),
    ('What causes dough or batter to rise when a leavening agent is used?', ['Bubbles of gas forming and expanding within the mixture', 'The mixture freezing solid', 'The mixture losing all of its water instantly', 'The oven light being turned on'], 0),
    ('What ingredient must be combined with baking soda to trigger its chemical reaction?', ['An acidic ingredient such as buttermilk or vinegar', 'A metal spoon', 'Only cold water', 'Only oil'], 0),
    ('How does baking powder differ from baking soda?', ['Baking powder already contains its own acidic ingredient built in', 'Baking powder contains no chemical compounds at all', 'Baking powder can never react with liquid', 'Baking soda always requires more sugar to work'], 0),
    ('Why is understanding the chemistry of leavening agents useful for a baker?', ['It helps explain why a recipe rises properly and how substituting ingredients might change the result', 'Leavening agents have no effect on how baked goods turn out', 'Chemical reactions never occur during baking', 'Baking never involves any chemical changes'], 0)]),
H('The Discovery of Insulin by Banting and Best',
  'Grade 8 History strand: in 1921 at the University of Toronto, Frederick Banting and Charles Best isolated insulin, a hormone that allowed people with diabetes to survive, becoming one of Canadas most celebrated medical achievements.',
  [('In what year was insulin discovered in Toronto?', ['1921', '1867', '1939', '1949'], 0),
   ('At which Canadian university was insulin discovered?', ['The University of Toronto', 'McGill University', 'The University of British Columbia', 'Dalhousie University'], 0),
   ('Who were the two researchers most closely associated with isolating insulin?', ['Frederick Banting and Charles Best', 'John Grierson and Lester Pearson', 'John A Macdonald and George Cartier', 'Igor Gouzenko and Tommy Douglas'], 0),
   ('What medical condition did the discovery of insulin help treat?', ['Diabetes', 'The common cold', 'Broken bones', 'Seasonal allergies'], 0),
   ('Why is the discovery of insulin considered one of Canadas most significant contributions to medicine?', ['It gave people with diabetes a life-saving treatment that had not existed before', 'It had no effect on medical treatment anywhere in the world', 'It was discovered outside of Canada by a different research team', 'It cured every known disease immediately'], 0)]),
]),
day(182, [
L('Vocabulary: Jargon and Technical Language Across Fields',
  'Grade 8 Language strand: jargon is specialized vocabulary used within a particular field, profession, or group, such as medicine or computer science, that can communicate precisely among experts but may confuse outside readers.',
  [('What is jargon?', ['Specialized vocabulary used within a particular field or group', 'A word with no real meaning', 'A synonym for slang used only by teenagers', 'A type of punctuation mark'], 0),
   ('Why might a doctor use jargon when speaking with another doctor?', ['It allows precise, efficient communication between people who share the same specialized knowledge', 'It is required by law in every conversation', 'It prevents any information from being shared', 'It replaces the need for medical training'], 0),
   ('What problem can jargon create for a general audience?', ['Readers unfamiliar with the field may find the text confusing or hard to understand', 'Jargon always makes writing easier for everyone to understand', 'Jargon removes all meaning from a sentence', 'Jargon is illegal to use in professional writing'], 0),
   ('Which of these is an example of computer science jargon?', ['Algorithm', 'Bicycle', 'Sandwich', 'Umbrella'], 0),
   ('Why should a writer consider their audience before using jargon?', ['Effective writing matches its vocabulary to what the intended audience is likely to understand', 'Audience has no effect on what vocabulary a writer should choose', 'Jargon should always be used regardless of who is reading', 'Every reader understands specialized vocabulary from every field equally well'], 0)]),
M('Number Theory: The Sieve of Eratosthenes',
  'Grade 8 Math strand: the Sieve of Eratosthenes is an ancient method for finding all prime numbers up to a given limit by systematically crossing out the multiples of each prime, leaving only primes uncrossed.',
  [('What does the Sieve of Eratosthenes help find?', ['All prime numbers up to a given limit', 'The exact square root of a number', 'The sum of an arithmetic sequence', 'The greatest common factor of two numbers'], 0),
   ('How does the Sieve of Eratosthenes identify prime numbers?', ['By systematically crossing out the multiples of each prime number', 'By randomly selecting numbers from a list', 'By adding every number in a range together', 'By dividing every number by exactly two'], 0),
   ('What is left uncrossed after completing the Sieve of Eratosthenes process?', ['The prime numbers within the chosen range', 'Only even numbers', 'Only numbers divisible by ten', 'No numbers remain uncrossed'], 0),
   ('Roughly how old is the method known as the Sieve of Eratosthenes?', ['It dates back to ancient Greece, over two thousand years ago', 'It was invented within the past ten years', 'It was invented during the twentieth century', 'It has no known origin in history'], 0),
   ('Why is the Sieve of Eratosthenes considered an efficient way to find many primes at once?', ['It eliminates multiples systematically instead of testing each number for divisibility one at a time', 'It requires checking every possible divisor of every number individually', 'It can only ever find a single prime number', 'It works by guessing numbers at random until a prime appears'], 0)]),
Sc('Physics: The Physics of Optical Illusions and Visual Perception',
   'Grade 8 Science strand: optical illusions occur when the brain interprets visual information from the eyes in a way that differs from physical reality, often due to how light, contrast, and patterns are processed by the visual system.',
   [('What is an optical illusion?', ['A situation where the brain interprets visual information differently from physical reality', 'A type of camera lens', 'A disease that affects only the eyes', 'A tool used to measure light intensity'], 0),
    ('What part of the body is primarily responsible for interpreting the visual information that creates an illusion?', ['The brain', 'The stomach', 'The lungs', 'The skeletal muscles'], 0),
    ('What visual factors can contribute to creating an optical illusion?', ['Light, contrast, and patterns', 'Only sound waves', 'Only the temperature of a room', 'Only the weight of an object'], 0),
    ('Why can two identical shapes sometimes appear to be different sizes in certain illusions?', ['Surrounding patterns and context can cause the brain to misjudge relative size', 'The shapes are always physically different sizes in reality', 'Light has no effect on how size is perceived', 'The eyes physically change shape when viewing an illusion'], 0),
    ('Why do scientists study optical illusions?', ['They reveal how the brain processes and sometimes misinterprets visual information', 'Optical illusions have no connection to how the brain works', 'Studying illusions provides no scientific insight of any kind', 'Illusions only occur in printed photographs, never in real life'], 0)]),
H('The Great Canadian Flag Debate and the Maple Leaf Flag of 1965',
  'Grade 8 History strand: after months of heated parliamentary debate led by Prime Minister Lester Pearson, Canada adopted the red and white maple leaf flag on February 15, 1965, replacing the Red Ensign as the countrys official national flag.',
  [('In what year did Canada officially adopt the maple leaf flag?', ['1965', '1867', '1949', '1988'], 0),
   ('Which prime minister led the push to adopt a new Canadian flag?', ['Lester Pearson', 'John A Macdonald', 'Pierre Trudeau', 'William Lyon Mackenzie King'], 0),
   ('What flag did the maple leaf flag replace as Canadas official flag?', ['The Red Ensign', 'The Union Jack of Britain', 'The flag of France', 'The flag of the United States'], 0),
   ('What colours appear on the Canadian maple leaf flag?', ['Red and white', 'Blue and white', 'Green and gold', 'Black and yellow'], 0),
   ('Why was the flag debate considered significant in Canadian history?', ['It reflected a growing sense of independent Canadian identity separate from British symbols', 'It had no connection to Canadian identity at all', 'It resulted in Canada keeping the exact same flag as before', 'It took place before Canada became a country'], 0)]),
]),
day(183, [
L('Reading: Analyzing Circular Structure and Full-Circle Endings in Narrative',
  'Grade 8 Language strand: a circular structure returns a narrative to its opening image, setting, or line by its conclusion, inviting readers to notice how characters or circumstances have changed since the story began.',
  [('What does a circular structure in a narrative do?', ['Returns the story to its opening image, setting, or line by the end', 'Tells events in a completely random order', 'Removes the ending of a story entirely', 'Only ever occurs in poetry, never in prose'], 0),
   ('What might a reader notice when a story uses a circular structure?', ['How characters or circumstances have changed since the beginning', 'That nothing in the story has changed at all', 'That the story has no characters', 'That the setting is described only once'], 0),
   ('Which is an example of a circular structure?', ['A story that opens and closes with the same image, described differently', 'A story with only one paragraph', 'A story with no setting described', 'A story told entirely through dialogue'], 0),
   ('Why might an author choose to end a story with a line similar to its opening line?', ['To highlight change or growth by contrasting the same moment at two points in time', 'To confuse the reader on purpose', 'To indicate the story has no theme', 'To avoid writing a conclusion altogether'], 0),
   ('Why is recognizing circular structure a useful reading skill?', ['It helps readers see how an author uses repetition to emphasize a storys central meaning', 'It has no effect on how a story can be interpreted', 'It only applies to stories written before the twentieth century', 'It prevents a reader from understanding the plot'], 0)]),
M('Algebra: An Introduction to Partial Fractions',
  'Grade 8 Math strand: partial fraction decomposition rewrites a complicated rational expression as a sum of simpler fractions with lower-degree denominators, making the expression easier to analyze or combine.',
  [('What does partial fraction decomposition do to a rational expression?', ['Rewrites it as a sum of simpler fractions with lower-degree denominators', 'Turns it into a whole number with no fraction at all', 'Removes the denominator from the expression entirely', 'Converts the expression into a single very large fraction'], 0),
   ('Why might someone want to break a complicated fraction into simpler partial fractions?', ['Simpler fractions can be easier to analyze, add, or work with', 'Doing so always makes an expression undefined', 'It removes the need for a numerator', 'It only applies to whole numbers, never expressions'], 0),
   ('What kind of expression is typically decomposed using partial fractions?', ['A rational expression, meaning one polynomial divided by another', 'A single whole number', 'A geometric shape', 'A statement of pure text with no numbers'], 0),
   ('What must be true about the denominators of the simpler fractions produced by partial fraction decomposition?', ['They generally have a lower degree than the original denominator', 'They must always be equal to zero', 'They must always be negative numbers', 'They must always be exactly the same as the original denominator'], 0),
   ('Why is partial fraction decomposition considered a useful algebraic technique?', ['It can simplify expressions that would otherwise be difficult to combine, differentiate, or interpret', 'It has no practical use in mathematics', 'It only works on expressions with no variables', 'It always produces an expression that is more complicated than the original'], 0)]),
Sc('Earth Science: Fossils and the Fossil Record',
   'Grade 8 Science strand: fossils are the preserved remains or traces of ancient organisms found in sedimentary rock, and together they form the fossil record, which scientists use to study how life on Earth has changed over time.',
   [('What is a fossil?', ['The preserved remains or traces of an ancient organism', 'A type of modern rock formed only underwater', 'A living organism found only in caves', 'A tool used to measure earthquakes'], 0),
    ('In what type of rock are fossils most commonly found?', ['Sedimentary rock', 'Igneous rock formed from lava', 'Only metamorphic rock', 'Only rock found on other planets'], 0),
    ('What is the fossil record?', ['The overall collection of fossils that document changes in life on Earth over time', 'A single fossil found in one location', 'A list of currently living species only', 'A record of modern weather patterns'], 0),
    ('What can scientists learn by studying the fossil record?', ['How life on Earth has changed and evolved over long periods of time', 'Nothing useful about the history of life on Earth', 'Only the current population of living species', 'Only information about the modern climate'], 0),
    ('Why are fossils considered valuable evidence for scientists studying the history of life?', ['They provide physical evidence of organisms that lived long before written history began', 'Fossils only form from organisms that are still alive today', 'Fossils provide no information about the past', 'Fossils can only be found in outer space'], 0)]),
H('The Construction of the CN Tower',
  'Grade 8 History strand: completed in Toronto in 1976 after more than three years of construction, the CN Tower stood as the worlds tallest free-standing structure for over three decades and became an internationally recognized symbol of Canadian engineering.',
  [('In what year was the CN Tower completed?', ['1976', '1967', '1949', '1988'], 0),
   ('In which Canadian city is the CN Tower located?', ['Toronto', 'Montreal', 'Vancouver', 'Ottawa'], 0),
   ('For roughly how long did the CN Tower hold the title of the worlds tallest free-standing structure?', ['Over three decades', 'A single year', 'Less than one month', 'It never held this title'], 0),
   ('What was the CN Tower originally built to support, in addition to being a landmark?', ['Communication and broadcast antennas', 'Farming equipment', 'A shopping mall roof only', 'A railway bridge'], 0),
   ('Why is the CN Tower considered an important symbol of Canadian engineering?', ['It demonstrated advanced construction techniques and became internationally recognized as a Canadian landmark', 'It was built entirely outside of Canada', 'It had no impact on how Canada was viewed internationally', 'It was demolished shortly after being completed'], 0)]),
]),
day(184, [
L('Writing: The Debate Rebuttal and Counterargument',
  'Grade 8 Language strand: a rebuttal responds directly to an opponents argument in a debate by identifying its weaknesses and offering counter-evidence or reasoning, strengthening a speakers own position without simply repeating it.',
  [('What is the purpose of a rebuttal in a debate?', ['To respond directly to an opponents argument by identifying its weaknesses', 'To repeat your own argument without addressing the opponent', 'To end the debate immediately', 'To agree completely with the opposing side'], 0),
   ('What should an effective rebuttal include?', ['Counter-evidence or reasoning that challenges the opposing argument', 'Only compliments directed at the opponent', 'A completely unrelated new topic', 'No reference to the opposing argument at all'], 0),
   ('Why is it important to listen carefully to an opponents argument before writing a rebuttal?', ['A rebuttal must accurately address the specific points the opponent actually made', 'Listening has no effect on the quality of a rebuttal', 'A rebuttal never needs to reference the opposing side', 'Debates do not allow any listening at all'], 0),
   ('What is a counterargument?', ['An argument that opposes or challenges another argument', 'A summary of your own opening statement', 'A question with no answer', 'A rule used only in written essays, never in speech'], 0),
   ('Why can a strong rebuttal make a debater more persuasive?', ['It shows the audience that weaknesses in the opposing argument have been carefully identified and addressed', 'It always weakens the speakers own position', 'It removes the need for any evidence in a debate', 'It guarantees the audience will ignore both sides'], 0)]),
M('Probability: An Introduction to the Coupon Collectors Problem',
  'Grade 8 Math strand: the Coupon Collectors Problem asks, on average, how many random draws with repetition are needed to collect every distinct item in a set, such as collecting all the different prizes in a cereal box promotion.',
  [('What does the Coupon Collectors Problem ask?', ['On average, how many random draws are needed to collect every distinct item in a set', 'How to calculate the area of a circle', 'How many primes exist below one hundred', 'How to solve a system of linear equations'], 0),
   ('What everyday situation is often used to illustrate the Coupon Collectors Problem?', ['Collecting all the different prizes from a cereal box promotion', 'Measuring the temperature outside', 'Calculating a mortgage payment', 'Finding the volume of a cone'], 0),
   ('As a collector gets closer to having every distinct item, what generally happens to the expected number of draws needed to find a brand-new item?', ['It tends to increase, since duplicates become more likely', 'It always decreases to zero immediately', 'It stays exactly the same throughout the entire process', 'It becomes impossible to calculate at all'], 0),
   ('What type of draws does the Coupon Collectors Problem assume, allowing the same item to be drawn more than once?', ['Random draws with repetition allowed', 'Draws where every item can only ever be drawn once', 'Draws that always follow a fixed, predictable order', 'Draws that never involve any randomness'], 0),
   ('Why is the Coupon Collectors Problem a useful example in the study of probability?', ['It shows how expected values can be used to answer a practical, real-world collecting question', 'It has no real-world application of any kind', 'It proves that probability can never be applied to games or collecting', 'It only applies to situations with exactly two possible items'], 0)]),
Sc('Biology: Camouflage and Animal Defense Mechanisms',
   'Grade 8 Science strand: camouflage allows an animal to blend into its surroundings through colouration, pattern, or shape, serving as one of several defense mechanisms, alongside mimicry and warning colouration, that help animals avoid predators.',
   [('What is camouflage?', ['A way for an animal to blend into its surroundings through colour, pattern, or shape', 'A loud sound used to scare away predators', 'A type of animal migration', 'A method animals use to find food only'], 0),
    ('What is one purpose of camouflage for many animals?', ['To help the animal avoid being detected by predators', 'To make the animal easier for predators to find', 'To help the animal grow larger', 'To change the animals diet'], 0),
    ('What is mimicry, as a defense mechanism?', ['When one species evolves to resemble another species, often one that is dangerous or unpleasant', 'When an animal copies the sound of a car engine', 'When an animal changes its diet to match another species', 'When two unrelated animals live in the exact same location'], 0),
    ('What is warning colouration, sometimes called aposematism?', ['Bright colouration that signals to predators that an animal may be toxic or dangerous', 'Colouration that has no effect on predators at all', 'Colouration used only to attract mates, never to warn predators', 'A colour pattern found only in plants'], 0),
    ('Why have defense mechanisms such as camouflage and mimicry become common across many animal species?', ['They increase an individual animals chances of survival, making these traits more likely to be passed on', 'They have no connection to an animals survival', 'They are found only in animals living in zoos', 'They always make an animal more visible to predators'], 0)]),
H('The Manitoba Flood of 1950 and the Building of the Winnipeg Floodway',
  'Grade 8 History strand: the massive flood of 1950 forced roughly one hundred thousand people from their homes in and around Winnipeg, prompting the later construction of the Winnipeg Floodway, a major engineering project designed to protect the city from future flooding.',
  [('In what year did the major flood affecting Winnipeg occur?', ['1950', '1917', '1939', '1967'], 0),
   ('Approximately how many people were displaced by the 1950 flood?', ['Roughly one hundred thousand', 'About ten', 'Roughly one million', 'About one thousand'], 0),
   ('What engineering project was later built to help protect Winnipeg from future flooding?', ['The Winnipeg Floodway', 'The Canadarm', 'The Confederation Bridge', 'The Trans-Canada Highway'], 0),
   ('What is the main purpose of the Winnipeg Floodway?', ['To divert floodwater around the city and reduce flood damage', 'To provide drinking water to nearby farms', 'To generate electricity for the entire province', 'To serve as a railway line'], 0),
   ('Why is the 1950 flood considered an important event in Manitoba history?', ['It was one of the most damaging floods in the regions history and led to major infrastructure changes', 'It had no lasting impact on the region', 'It resulted in no changes to how the city managed flooding', 'It occurred in a province other than Manitoba'], 0)]),
]),
day(185, [
L('Media Literacy: Distinguishing Satire from Misinformation Online',
  'Grade 8 Language strand: satire uses humour and exaggeration to critique or comment on real issues, while misinformation presents false claims as genuine fact, and media-literate readers learn to tell the two apart by checking sources, tone, and intent.',
  [('What is the main purpose of satire?', ['To use humour and exaggeration to critique or comment on real issues', 'To spread false information disguised as fact', 'To replace all serious journalism', 'To eliminate the need for fact-checking'], 0),
   ('How does misinformation differ from satire?', ['Misinformation presents false claims as if they were genuine fact, without the intent of being understood as a joke', 'Misinformation is always clearly labeled as a joke', 'Misinformation and satire are always exactly the same thing', 'Misinformation only appears in printed newspapers'], 0),
   ('What is one strategy a media-literate reader can use to tell satire apart from misinformation?', ['Checking the source, tone, and stated intent of the content', 'Believing every headline without question', 'Ignoring where the information came from', 'Assuming all online content is equally reliable'], 0),
   ('Why can satire sometimes be mistaken for real news?', ['Its exaggerated claims can resemble real headlines if a reader misses the humorous or critical intent', 'Satire always states clearly that it is completely false', 'Satire never resembles real news in any way', 'Satire is only ever published in academic journals'], 0),
   ('Why is distinguishing satire from misinformation an important media literacy skill?', ['Misreading either one can lead to spreading false beliefs or missing an intended critique', 'This distinction has no effect on how information spreads', 'Satire and misinformation always have identical goals', 'Only professional journalists need to make this distinction'], 0)]),
M('Geometry: The Centroid, Circumcenter, and Orthocenter of a Triangle',
  'Grade 8 Math strand: a triangle has several notable points, including the centroid, where its medians intersect, the circumcenter, where perpendicular bisectors of its sides meet, and the orthocenter, where its altitudes intersect.',
  [('What is the centroid of a triangle?', ['The point where the triangles medians intersect', 'The point where all three sides meet', 'The midpoint of only one side', 'The point farthest from the triangles interior'], 0),
   ('What is the circumcenter of a triangle?', ['The point where the perpendicular bisectors of the triangles sides meet', 'The point where the triangles angles are largest', 'The midpoint of the longest side only', 'A point that never exists for any triangle'], 0),
   ('What is the orthocenter of a triangle?', ['The point where the triangles altitudes intersect', 'The point where two sides of the triangle cross', 'The exact center of the triangles perimeter', 'A point located outside every triangle'], 0),
   ('What is a median of a triangle?', ['A line segment from a vertex to the midpoint of the opposite side', 'A line segment connecting two midpoints of the same side', 'A line that never touches the triangle', 'The longest side of the triangle'], 0),
   ('Why do mathematicians study special points such as the centroid, circumcenter, and orthocenter?', ['These points reveal structural properties and symmetries within every triangle', 'These points have no mathematical significance', 'Triangles cannot contain more than one special point', 'These points only exist in three-dimensional shapes'], 0)]),
Sc('Space Science: The Search for Water on Mars',
   'Grade 8 Science strand: scientists have found evidence of ancient rivers, lake beds, and underground ice on Mars, and searching for water is a key part of exploring whether the planet could have once supported, or might still support, microbial life.',
   [('What kind of evidence have scientists found suggesting water once existed on Mars?', ['Ancient rivers, lake beds, and underground ice', 'Living dinosaurs still roaming the surface', 'Oceans of liquid gold', 'Active volcanoes erupting constantly'], 0),
    ('Why is searching for water on Mars important to scientists studying the possibility of life there?', ['Water is considered essential for life as we understand it', 'Water has no connection to the possibility of life', 'Mars is already known to be completely lifeless with certainty', 'Water searches are unrelated to any scientific goal'], 0),
    ('In what form does much of the water on modern-day Mars likely exist?', ['Underground ice', 'Large flowing rivers on the surface', 'Boiling oceans', 'Rain falling constantly'], 0),
    ('What kind of spacecraft have been used to study evidence of water on Mars?', ['Robotic rovers and orbiting spacecraft', 'Only telescopes located on the Moon', 'Manned spacecraft that have already landed astronauts on Mars', 'Weather balloons launched from Earth'], 0),
    ('Why does the possible presence of ancient water make Mars a major focus of space exploration?', ['It raises the possibility that Mars could have once supported simple forms of life', 'Water has never been detected anywhere on Mars', 'Mars is known to have no connection to questions about life', 'Searching for water on Mars provides no scientific value'], 0)]),
H('The Confederation Bridge and Linking Prince Edward Island by Land',
  'Grade 8 History strand: opened in 1997, the Confederation Bridge spans the Northumberland Strait to connect Prince Edward Island with mainland New Brunswick, fulfilling an 1873 promise of a permanent land link made when the island joined Confederation.',
  [('In what year did the Confederation Bridge open?', ['1997', '1967', '1873', '1949'], 0),
   ('What body of water does the Confederation Bridge cross?', ['The Northumberland Strait', 'The Bay of Fundy', 'The Strait of Georgia', 'Lake Ontario'], 0),
   ('Which two regions does the Confederation Bridge connect?', ['Prince Edward Island and mainland New Brunswick', 'Ontario and Quebec', 'British Columbia and Alberta', 'Nova Scotia and Newfoundland'], 0),
   ('What earlier promise did the completion of the Confederation Bridge fulfill?', ['An 1873 promise of a permanent land link made when Prince Edward Island joined Confederation', 'A promise made during the Second World War', 'A promise made at the original 1867 Confederation meetings', 'A promise related to the construction of the CN Tower'], 0),
   ('Why is the Confederation Bridge considered a significant piece of Canadian infrastructure?', ['It provided Prince Edward Island with a permanent, reliable land connection to the rest of Canada', 'It disconnected Prince Edward Island from the rest of Canada', 'It was never actually completed', 'It has no connection to Prince Edward Islands history with Confederation'], 0)]),
]),
day(186, [
L('Grammar: Recognizing and Avoiding Comma Splices',
  'Grade 8 Language strand: a comma splice occurs when two independent clauses are joined by only a comma instead of a coordinating conjunction, semicolon, or period, and correcting it strengthens sentence clarity.',
  [('What is a comma splice?', ['Two independent clauses joined by only a comma', 'A sentence with no punctuation at all', 'A single word repeated twice in a row', 'A question that has no answer'], 0),
   ('What is one way to correct a comma splice?', ['Replace the comma with a semicolon or a period', 'Remove all punctuation from the sentence', 'Add a second comma directly after the first', 'Delete the entire second clause'], 0),
   ('What could also be added, along with a comma, to correctly join two independent clauses?', ['A coordinating conjunction such as and or but', 'A silent letter', 'A question mark placed mid-sentence', 'An extra subject with no verb'], 0),
   ('Why are comma splices considered a common but avoidable error in writing?', ['Writers sometimes sense a pause is needed but choose the wrong punctuation to show it', 'Comma splices are always considered correct in formal writing', 'A comma splice can never be identified or corrected', 'Comma splices only occur in poetry, never prose'], 0),
   ('Why is it important to correct comma splices in formal writing?', ['Correcting them improves clarity and helps readers see where one complete idea ends and another begins', 'Comma splices always make a sentence easier to understand', 'Formal writing does not require correct punctuation', 'Comma splices are required in academic essays'], 0)]),
M('Statistics: An Introduction to the Coefficient of Variation',
  'Grade 8 Math strand: the coefficient of variation expresses a data sets standard deviation as a percentage of its mean, allowing the relative spread of two data sets with different units or averages to be compared fairly.',
  [('What does the coefficient of variation express?', ['A data sets standard deviation as a percentage of its mean', 'The total number of values in a data set', 'The largest value found in a data set', 'The exact median of a data set'], 0),
   ('Why is the coefficient of variation useful when comparing two very different data sets?', ['It allows their relative spread to be compared fairly, even if their units or averages differ', 'It removes the need to ever calculate a mean', 'It only works when two data sets have identical values', 'It always produces the number zero'], 0),
   ('What two values are needed to calculate the coefficient of variation?', ['The standard deviation and the mean', 'Only the largest and smallest values', 'Only the total number of data points', 'The mode and the range'], 0),
   ('A higher coefficient of variation generally suggests what about a data set?', ['Greater relative spread compared to its own mean', 'A data set with only one possible value', 'A data set that cannot be measured', 'A data set with a mean of exactly zero'], 0),
   ('Why might a researcher choose the coefficient of variation instead of the standard deviation alone?', ['It provides a way to compare variability between data sets measured in different units', 'Standard deviation and coefficient of variation always give identical results', 'The coefficient of variation cannot be calculated from real data', 'It removes the need to collect any data at all'], 0)]),
Sc('Technology: How Water Desalination Works',
   'Grade 8 Science strand: desalination removes salt and other minerals from seawater to produce fresh drinking water, most commonly through reverse osmosis, which forces seawater through a membrane that blocks salt while allowing water molecules through.',
   [('What is the main goal of water desalination?', ['Removing salt and minerals from seawater to produce fresh drinking water', 'Adding extra salt to fresh water', 'Freezing seawater permanently', 'Removing all water from the ocean'], 0),
    ('What is the most common method used for large-scale desalination today?', ['Reverse osmosis', 'Simple boiling in an open pot', 'Freezing the entire ocean', 'Adding chemicals that create more salt'], 0),
    ('In reverse osmosis, what does a special membrane do?', ['Blocks salt while allowing water molecules to pass through', 'Blocks water while allowing salt to pass through freely', 'Removes all molecules, including water, completely', 'Has no effect on water or salt at all'], 0),
    ('Why might desalination be especially important for regions with limited fresh water?', ['It can provide an additional source of drinking water from the ocean', 'It removes the need for any water at all in that region', 'It makes seawater completely unusable for any purpose', 'It has no practical application for water-scarce regions'], 0),
    ('What is one challenge associated with large-scale desalination?', ['The process can require a significant amount of energy to operate', 'Desalination requires no energy whatsoever', 'Desalination immediately solves every water shortage with no drawbacks', 'Desalination cannot be performed anywhere on Earth'], 0)]),
H('O Canada Becomes Canadas Official National Anthem in 1980',
  'Grade 8 History strand: although O Canada was first performed in Quebec City in 1880, it was not officially proclaimed as Canadas national anthem until July 1, 1980, on the one hundred and thirteenth anniversary of Confederation.',
  [('In what year did O Canada become Canadas official national anthem?', ['1980', '1880', '1967', '1949'], 0),
   ('In what year and city was O Canada first performed?', ['1880, in Quebec City', '1980, in Ottawa', '1867, in Toronto', '1945, in Vancouver'], 0),
   ('On what date in 1980 was O Canada officially proclaimed the national anthem?', ['July 1', 'January 1', 'December 25', 'October 31'], 0),
   ('What anniversary did the 1980 proclamation coincide with?', ['The one hundred and thirteenth anniversary of Confederation', 'The very first year of Confederation', 'The two hundredth anniversary of Confederation', 'The fiftieth anniversary of the Second World War'], 0),
   ('Why is the gap between O Canadas first performance and its official proclamation notable to historians?', ['It shows how long a widely sung and recognized song can exist before receiving official status', 'O Canada was written and proclaimed as the anthem on the exact same day', 'O Canada was never actually proclaimed as an official anthem', 'Canada had no anthem of any kind before 1980'], 0)]),
]),
day(187, [
L('Language Review: Grammar, Vocabulary, and Narrative Reading (Days 181-186)',
  'Grade 8 Language strand review, and the final Language review of the K-12 curriculum build for this grade: students revisit the serial comma, jargon and technical language, circular structure in narrative, the debate rebuttal, and distinguishing satire from misinformation.',
  [('What is another common name for the serial comma?', ['The Oxford comma', 'The Cambridge comma', 'The London comma', 'The Harvard colon'], 0),
   ('What is jargon?', ['Specialized vocabulary used within a particular field or group', 'A word with no real meaning', 'A synonym for slang used only by teenagers', 'A type of punctuation mark'], 0),
   ('What does a circular structure in a narrative do?', ['Returns the story to its opening image, setting, or line by the end', 'Tells events in a completely random order', 'Removes the ending of a story entirely', 'Only ever occurs in poetry, never in prose'], 0),
   ('What is the purpose of a rebuttal in a debate?', ['To respond directly to an opponents argument by identifying its weaknesses', 'To repeat your own argument without addressing the opponent', 'To end the debate immediately', 'To agree completely with the opposing side'], 0),
   ('What is the main purpose of satire?', ['To use humour and exaggeration to critique or comment on real issues', 'To spread false information disguised as fact', 'To replace all serious journalism', 'To eliminate the need for fact-checking'], 0)]),
M('Math Review: Statistics, Probability, and Geometry (Days 181-186)',
  'Grade 8 Math strand review, and the final Math review of the K-12 curriculum build for this grade: students revisit variance, the Sieve of Eratosthenes, partial fraction decomposition, the Coupon Collectors Problem, and special triangle centers.',
  [('What does variance measure about a data set?', ['How far the data values are spread out from the mean', 'The exact largest value in the data set', 'The total number of values in the data set', 'The order in which data was collected'], 0),
   ('What does the Sieve of Eratosthenes help find?', ['All prime numbers up to a given limit', 'The exact square root of a number', 'The sum of an arithmetic sequence', 'The greatest common factor of two numbers'], 0),
   ('What does partial fraction decomposition do to a rational expression?', ['Rewrites it as a sum of simpler fractions with lower-degree denominators', 'Turns it into a whole number with no fraction at all', 'Removes the denominator from the expression entirely', 'Converts the expression into a single very large fraction'], 0),
   ('What does the Coupon Collectors Problem ask?', ['On average, how many random draws are needed to collect every distinct item in a set', 'How to calculate the area of a circle', 'How many primes exist below one hundred', 'How to solve a system of linear equations'], 0),
   ('What is the centroid of a triangle?', ['The point where the triangles medians intersect', 'The point where all three sides meet', 'The midpoint of only one side', 'The point farthest from the triangles interior'], 0)]),
Sc('Science Review: Chemistry, Biology, and Space Science (Days 181-186)',
   'Grade 8 Science strand review, and the final Science review of the K-12 curriculum build for this grade: students revisit the chemistry of baking, optical illusions, fossils and the fossil record, camouflage and animal defenses, and the search for water on Mars.',
   [('What gas do leavening agents such as baking soda release during baking?', ['Carbon dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'], 0),
    ('What is an optical illusion?', ['A situation where the brain interprets visual information differently from physical reality', 'A type of camera lens', 'A disease that affects only the eyes', 'A tool used to measure light intensity'], 0),
    ('What is a fossil?', ['The preserved remains or traces of an ancient organism', 'A type of modern rock formed only underwater', 'A living organism found only in caves', 'A tool used to measure earthquakes'], 0),
    ('What is camouflage?', ['A way for an animal to blend into its surroundings through colour, pattern, or shape', 'A loud sound used to scare away predators', 'A type of animal migration', 'A method animals use to find food only'], 0),
    ('What kind of evidence have scientists found suggesting water once existed on Mars?', ['Ancient rivers, lake beds, and underground ice', 'Living dinosaurs still roaming the surface', 'Oceans of liquid gold', 'Active volcanoes erupting constantly'], 0)]),
H('History Review: Canadian Landmarks and National Symbols (Days 181-186)',
  'Grade 8 History strand review, and the final History review completing the full 187-day K-12 curriculum build for this grade: students revisit the discovery of insulin, the Great Flag Debate, the CN Tower, the Manitoba flood of 1950, and the Confederation Bridge.',
  [('In what year was insulin discovered in Toronto?', ['1921', '1867', '1939', '1949'], 0),
   ('In what year did Canada officially adopt the maple leaf flag?', ['1965', '1867', '1949', '1988'], 0),
   ('In what year was the CN Tower completed?', ['1976', '1967', '1949', '1988'], 0),
   ('In what year did the major flood affecting Winnipeg occur?', ['1950', '1917', '1939', '1967'], 0),
   ('In what year did the Confederation Bridge open?', ['1997', '1967', '1873', '1949'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_181_187)
    append_to(8, g8_181_187)
