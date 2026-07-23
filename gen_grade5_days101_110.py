#!/usr/bin/env python3
"""Grade 5, Days 101-110 -- extends Grade 5 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade5.json): active listening and effective speaking, apostrophes for
possession and contractions, problem-and-solution text structure, compound
words, writing a formal letter or email, comma usage in lists/dates/
addresses, recognizing an unreliable narrator, point of view and bias in
news media, types of adverbs; place value to one million, range and
outliers, sales tax and discounts, converting metric capacity and mass,
pattern rules in words, representing 3D objects using top/front/side views,
double bar graphs, reading Celsius thermometers, estimating products and
quotients; tension and compression forces, the screw and the wedge,
migration and hibernation, how body systems work together, the role of
foundations in buildings, properties of recyclable materials, how fossil
fuels form, symbiotic relationships, how materials absorb or reflect
sound; provincial flags and coats of arms, the Canadian Senate, the role
of Lieutenant Governors, the Canadian Shield, the boreal forest region,
how federal elections work (Elections Canada), the Canadian Coast Guard,
free trade agreements (NAFTA and CUSMA), and Canada's forestry industry.

Subject keys for Grade 5 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 5 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260722):
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


g5_101_110 = [
day(101, [
L('Oral Communication: Active Listening and Effective Speaking',
  'Grade 5 Language strand: active listening means giving full attention, avoiding interruptions, and asking clarifying questions, while effective speaking includes clear volume, appropriate pacing, and eye contact with an audience.',
  [('What is one key habit of an active listener during a conversation?', ['Giving full attention to the speaker', 'Looking at a phone while someone talks', 'Interrupting to share your own story', 'Thinking only about your next turn to speak'], 0),
   ('Which of these is an example of a clarifying question a listener might ask?', ['Could you explain what you meant by that?', 'I already know everything you are saying.', 'Why are you even talking to me?', 'That has nothing to do with anything.'], 0),
   ('Does making eye contact with an audience usually help hold their attention during a speech?', ['Yes', 'No, eye contact never affects an audience', 'A concept unrelated to speaking', 'Audiences prefer speakers who never look at them'], 0),
   ('Why might a speaker practise adjusting their volume and pacing before giving a speech?', ['It helps the audience hear and understand the ideas clearly', 'Volume and pacing never affect how a speech is understood', 'This concept has no connection to oral communication', 'A speech is always understood no matter how it is delivered'], 0),
   ('Why is active listening considered an important skill during a class discussion?', ['It helps you understand others’ ideas and respond thoughtfully', 'Active listening never helps anyone understand a discussion', 'This concept has no relevance to oral communication', 'A good listener never needs to pay attention to a speaker'], 0)]),
M('Number Sense: Reading and Writing Numbers to One Million',
  'Grade 5 Math strand: students read, write, and represent whole numbers up to one million, understanding that each digit’s place value, from ones to hundred thousands, determines its worth.',
  [('In the number 452,367, what is the value of the digit 4?', ['400,000', '4,000', '40,000', '4'], 0),
   ('How is the number four hundred thousand, two hundred fifteen written using digits?', ['400,215', '40,215', '4,215', '4,000,215'], 0),
   ('Which number is greater: 356,204 or 356,240?', ['356,240', '356,204', 'They are equal', 'A concept unrelated to place value'], 0),
   ('Why is a comma often used when writing numbers like 1,000,000?', ['It helps separate groups of thousands, making large numbers easier to read', 'Commas never make large numbers easier to read', 'This concept has no connection to number sense', 'A comma always changes the value of a number'], 0),
   ('Why is understanding place value important when comparing very large numbers?', ['It shows which digits carry the most value, making comparisons accurate', 'Place value never affects how numbers compare to each other', 'This concept has no relevance to number sense', 'Large numbers can never actually be compared to one another'], 0)]),
Sc('Structures: Tension and Compression Forces',
   'Grade 5 Science strand: structures experience tension, a pulling or stretching force, and compression, a pushing or squeezing force, and engineers design structures to withstand both.',
   [('What do we call a force that pulls or stretches a material?', ['Tension', 'Compression', 'A concept unrelated to structures', 'Friction'], 0),
    ('What do we call a force that pushes or squeezes a material?', ['Compression', 'Tension', 'A concept unrelated to structures', 'Gravity'], 0),
    ('When you stretch a rubber band, is it experiencing tension?', ['Yes', 'No, a stretched rubber band experiences no force', 'A concept unrelated to structures', 'Stretching only ever causes compression'], 0),
    ('Why might an engineer need to consider both tension and compression when designing a bridge?', ['Different parts of a bridge experience different forces, and materials must withstand both', 'Bridges never experience tension or compression', 'This concept has no relevance to science', 'Only tension ever affects a bridge, never compression'], 0),
    ('Why might a material that resists compression well still fail under tension?', ['A material can respond differently to pulling forces than to pushing forces', 'Every material resists tension and compression in exactly the same way', 'This concept has no connection to structures', 'Tension and compression are always identical forces'], 0)]),
SS('Provincial Flags, Coats of Arms, and Emblems Across Canada',
   'Grade 5 Social Studies strand: each Canadian province and territory has its own flag, coat of arms, and emblems, such as an official flower or bird, that reflect its unique history and identity.',
   [('Does each Canadian province have its own official flag?', ['Yes', 'No, all provinces share one identical flag', 'A concept unrelated to Canadian identity', 'Only some provinces are allowed to have flags'], 0),
    ('What is a coat of arms used to represent?', ['A province, territory, or country’s identity and history', 'A type of Canadian currency', 'A concept unrelated to Canadian symbols', 'A federal law'], 0),
    ('Which of these is an example of a provincial emblem?', ['An official provincial flower', 'A national anthem', 'A federal tax rate', 'A type of currency'], 0),
    ('Why might a province choose specific symbols, like a flower or bird, to represent it?', ['These symbols can reflect the province’s natural environment, history, or values', 'Provincial symbols never have any meaning behind them', 'This concept has no relevance to social studies', 'Every province is required to use the exact same symbols'], 0),
    ('Why might comparing provincial flags and emblems help students understand Canada’s diversity?', ['Each province’s unique symbols can reflect its distinct history and regional identity', 'Provincial symbols never reveal anything about a region', 'This concept has no connection to Canadian identity', 'All provinces have always had identical histories and symbols'], 0)]),
]),

day(102, [
L('Grammar: Apostrophes for Possession and Contractions',
  'Grade 5 Language strand: an apostrophe can show possession, as in the dog’s bone, or form a contraction by replacing missing letters, as in do not becoming don’t.',
  [('What does an apostrophe show in the phrase the cat’s toy?', ['Possession, that the toy belongs to the cat', 'A contraction of two words', 'A concept unrelated to grammar', 'That the sentence is a question'], 0),
   ('What is the contraction for do not?', ['Don’t', 'Dont', 'Do’nt', 'Do not’'], 0),
   ('Which sentence correctly shows possession?', ['The girls’ backpacks were left on the bus.', 'The girls backpack’s were left on the bus.', 'The girl’s’s backpacks were left on the bus.', 'The girls backpacks were left on the bus, apostrophe.'], 0),
   ('Why is it important to place an apostrophe correctly when showing possession for a plural noun, like the students’ books?', ['It shows that the books belong to more than one student', 'Apostrophe placement never changes the meaning of a sentence', 'This concept has no connection to grammar', 'Apostrophes are never used with plural nouns'], 0),
   ('Why might mixing up its and it’s be a common grammar mistake?', ['Its shows possession while it’s is a contraction for it is, and they sound identical', 'Its and it’s always mean the exact same thing', 'This concept has no relevance to grammar', 'Apostrophes never change the meaning of the word its'], 0)]),
M('Data Management: Range and Outliers in a Data Set',
  'Grade 5 Math strand: the range of a data set is the difference between its greatest and least values, and an outlier is a value that is much higher or lower than the rest of the data.',
  [('How do you calculate the range of a data set?', ['Subtract the least value from the greatest value', 'Add all the values together', 'Multiply the greatest and least values', 'A concept unrelated to data management'], 0),
   ('What is the range of this data set: 4, 7, 9, 12, 15?', ['11', '15', '4', '9'], 0),
   ('What do we call a value in a data set that is much higher or lower than the rest?', ['An outlier', 'The mean', 'The mode', 'A concept unrelated to data management'], 0),
   ('In the data set 2, 3, 5, 4, 50, which value is most likely an outlier?', ['50', '2', '3', '4'], 0),
   ('Why might an outlier affect how accurately the mean represents a data set?', ['A very high or low value can pull the mean away from where most of the data actually falls', 'Outliers never have any effect on the mean of a data set', 'This concept has no connection to data management', 'The mean is always identical whether or not an outlier is present'], 0)]),
Sc('Simple Machines: The Screw and the Wedge',
   'Grade 5 Science strand: the screw is a simple machine made of an inclined plane wrapped around a cylinder, and the wedge is two inclined planes joined together, both used to make work easier.',
   [('What simple machine is made of an inclined plane wrapped around a cylinder?', ['A screw', 'A wedge', 'A lever', 'A pulley'], 0),
    ('What simple machine is made of two inclined planes joined back to back?', ['A wedge', 'A screw', 'A lever', 'A wheel and axle'], 0),
    ('Is an axe blade an example of a wedge?', ['Yes', 'No, an axe blade is never considered a wedge', 'A concept unrelated to simple machines', 'An axe blade is always classified as a lever'], 0),
    ('Why might a screw be useful for holding two pieces of wood together?', ['Its spiral shape grips the wood tightly as it turns, resisting being pulled out', 'A screw never actually holds materials together', 'This concept has no relevance to science', 'A screw and a nail work in exactly the same way'], 0),
    ('Why might a wedge, such as a doorstop, be effective at holding something in place?', ['Its angled shape converts a small push into a strong force that resists movement', 'A wedge never applies any force to an object', 'This concept has no connection to simple machines', 'A wedge only works when it is shaped like a circle'], 0)]),
SS('The Canadian Senate and Its Role in Parliament',
   'Grade 5 Social Studies strand: the Senate is the appointed upper house of Canada’s Parliament that reviews, debates, and can amend bills passed by the elected House of Commons before they become law.',
   [('What is the name of the appointed upper house of Canada’s Parliament?', ['The Senate', 'The House of Commons', 'A concept unrelated to Canadian government', 'The Supreme Court'], 0),
    ('Are members of the Senate elected by the public in the same way as Members of Parliament?', ['No, senators are appointed', 'Yes, senators are elected the exact same way', 'A concept unrelated to Canadian government', 'Senators are chosen by a public lottery'], 0),
    ('What is one task the Senate performs with bills passed by the House of Commons?', ['Reviewing and debating the bills', 'Ignoring the bills completely', 'A concept unrelated to the Senate', 'Cancelling all federal elections'], 0),
    ('Why might Canada’s Parliament have two separate houses, the Senate and the House of Commons, to review laws?', ['Having two houses allows for extra review and debate before a bill becomes law', 'Two houses never add any extra review to the law-making process', 'This concept has no relevance to social studies', 'Only one house is ever involved in passing a law in Canada'], 0),
    ('Why might it matter that senators are appointed rather than elected?', ['It can shape the way the public views their role compared to elected representatives', 'Whether senators are appointed or elected never has any significance', 'This concept has no connection to Canadian government', 'Appointed and elected officials always have identical public roles'], 0)]),
]),

day(103, [
L('Reading: Problem-and-Solution Text Structure',
  'Grade 5 Language strand: problem-and-solution is a nonfiction text structure in which an author presents a problem and then describes one or more solutions to address it.',
  [('What does a problem-and-solution text structure present to the reader?', ['A problem and one or more ways to solve it', 'Only a list of unrelated facts', 'A concept unrelated to text structure', 'A story with no real conflict'], 0),
   ('Which of these sentences signals a problem-and-solution structure?', ['Plastic pollution harms oceans, but recycling programs can help reduce it.', 'The sun rose over the calm lake.', 'She woke up and ate breakfast.', 'Yesterday was sunny and warm.'], 0),
   ('Might a nonfiction article about a city’s traffic problems describe possible solutions, like new bus routes?', ['Yes', 'No, articles about problems never mention any solutions', 'A concept unrelated to text structure', 'Solutions are never included in nonfiction writing'], 0),
   ('Why might recognizing a problem-and-solution structure help a reader understand a nonfiction article?', ['It helps the reader see how the issue is connected to proposed fixes', 'Recognizing this structure never helps with understanding a text', 'This concept has no connection to reading comprehension', 'Problems and solutions are never related to each other in a text'], 0),
   ('Why might an author choose a problem-and-solution structure instead of simply describing events in order?', ['It can clearly show why an issue matters and what might be done about it', 'This structure never helps communicate an idea clearly', 'This concept has no relevance to reading', 'Describing events in order is the only structure an author can ever use'], 0)]),
M('Financial Literacy: Calculating Sales Tax and Discounts',
  'Grade 5 Math strand: students calculate sales tax as a percentage added to a purchase price, and calculate a discount as a percentage subtracted from the original price of an item.',
  [('If an item costs 20 dollars and the sales tax is 10 percent, how much tax is added?', ['2 dollars', '10 dollars', '20 dollars', '1 dollar'], 0),
   ('If a 40 dollar item is discounted by 25 percent, how much is the discount?', ['10 dollars', '25 dollars', '15 dollars', '4 dollars'], 0),
   ('After a 25 percent discount on a 40 dollar item, what is the new price?', ['30 dollars', '25 dollars', '15 dollars', '35 dollars'], 0),
   ('Why is it useful to know how to calculate sales tax before making a purchase?', ['It helps you know the total amount you will actually need to pay', 'Sales tax never changes the total amount owed', 'This concept has no connection to financial literacy', 'Sales tax is always exactly the same as the original price'], 0),
   ('Why might a store advertise a discount as a percentage rather than a fixed dollar amount?', ['A percentage discount can apply proportionally to items of any original price', 'Percentages never actually represent a real discount', 'This concept has no relevance to financial literacy', 'A percentage discount always means the item becomes free'], 0)]),
Sc('Life Systems: Migration and Hibernation as Survival Strategies',
   'Grade 5 Science strand: some animals survive seasonal changes through migration, traveling to a different location, or hibernation, entering a deep, energy-saving sleep during cold months.',
   [('What do we call it when an animal travels to a different location to survive seasonal changes?', ['Migration', 'Hibernation', 'A concept unrelated to survival strategies', 'Metamorphosis'], 0),
    ('What do we call a deep, energy-saving sleep some animals enter during cold months?', ['Hibernation', 'Migration', 'A concept unrelated to survival strategies', 'Pollination'], 0),
    ('Do many Canada geese migrate south for the winter?', ['Yes', 'No, Canada geese never migrate', 'A concept unrelated to migration', 'Canada geese hibernate instead of migrating'], 0),
    ('Why might hibernation help an animal, like a bear, survive winter when food is scarce?', ['Slowing the body’s functions during hibernation reduces the need for food and energy', 'Hibernation never helps an animal conserve energy', 'This concept has no relevance to science', 'Animals need more food while hibernating than while active'], 0),
    ('Why might migration be a risky but necessary survival strategy for some animals?', ['Traveling long distances uses energy and faces dangers, but it leads to better food or climate conditions', 'Migration never involves any risk or benefit to an animal', 'This concept has no connection to survival strategies', 'Animals that migrate always stay in exactly the same location'], 0)]),
SS('The Role of Lieutenant Governors in the Provinces',
   'Grade 5 Social Studies strand: a Lieutenant Governor is the monarch’s representative in a province, performing ceremonial duties and formally granting royal assent to provincial laws.',
   [('What is the title of the monarch’s representative in a Canadian province?', ['The Lieutenant Governor', 'The Premier', 'The Governor General', 'The Prime Minister'], 0),
    ('Does a Lieutenant Governor formally grant royal assent to provincial laws?', ['Yes', 'No, a Lieutenant Governor has no role in provincial laws', 'A concept unrelated to Canadian government', 'Only the Prime Minister can approve provincial laws'], 0),
    ('Is the role of Lieutenant Governor mainly ceremonial rather than a role that makes daily political decisions?', ['Yes', 'No, the Lieutenant Governor makes every daily political decision', 'A concept unrelated to Canadian government', 'The Lieutenant Governor has no duties at all'], 0),
    ('Why might a province have a Lieutenant Governor as well as a Premier?', ['The Lieutenant Governor represents the monarch while the Premier leads the elected government', 'These two roles are always exactly identical', 'This concept has no relevance to social studies', 'A province never needs any representative of the monarch'], 0),
    ('Why is it useful to compare the role of a Lieutenant Governor with the role of Canada’s Governor General?', ['It helps show how similar ceremonial roles exist at both the federal and provincial levels', 'Comparing these roles never reveals anything about Canadian government', 'This concept has no connection to social studies', 'The Lieutenant Governor and Governor General have completely unrelated jobs with no similarities'], 0)]),
]),

day(104, [
L('Vocabulary: Compound Words and Their Meanings',
  'Grade 5 Language strand: a compound word is formed by joining two smaller words together, such as sunflower or backpack, and its meaning is often related to the meanings of both original words.',
  [('What do we call a word formed by joining two smaller words together?', ['A compound word', 'A synonym', 'An antonym', 'A concept unrelated to vocabulary'], 0),
   ('Which of these is an example of a compound word?', ['Backpack', 'Running', 'Happier', 'Careful'], 0),
   ('Is the word sunflower formed by joining the words sun and flower?', ['Yes', 'No, sunflower is not a compound word', 'A concept unrelated to compound words', 'Sunflower has no connection to the words sun or flower'], 0),
   ('Why might understanding the two smaller words in a compound word help you figure out its meaning?', ['The meanings of the smaller words often relate to the meaning of the whole compound word', 'The smaller words in a compound word never relate to its meaning', 'This concept has no connection to vocabulary', 'Compound words never have any connection to the words that form them'], 0),
   ('Why might the compound word butterfly be a tricky example of this pattern?', ['Its meaning is not simply butter plus fly, so context and memorization also matter', 'Butterfly is not actually a compound word at all', 'This concept has no relevance to vocabulary', 'Every compound word’s meaning is always completely obvious from its parts'], 0)]),
M('Measurement: Converting Between Metric Units of Capacity and Mass',
  'Grade 5 Math strand: students convert between metric units of capacity, such as millilitres and litres, and mass, such as grams and kilograms, using the relationship that 1000 of the smaller unit equals 1 of the larger unit.',
  [('How many millilitres are in 1 litre?', ['1000', '100', '10', '10000'], 0),
   ('How many grams are in 1 kilogram?', ['1000', '100', '10', '10000'], 0),
   ('How many litres is 3000 millilitres?', ['3 litres', '30 litres', '300 litres', '0.3 litres'], 0),
   ('How many kilograms is 5000 grams?', ['5 kilograms', '50 kilograms', '500 kilograms', '0.5 kilograms'], 0),
   ('Why is it useful to know that 1000 millilitres equals 1 litre when solving measurement problems?', ['It allows you to convert between the two units quickly and accurately', 'This relationship never helps with converting between units', 'This concept has no connection to measurement', 'Millilitres and litres are never actually related to each other'], 0)]),
Sc('Life Systems: How the Body’s Systems Work Together',
   'Grade 5 Science strand: the body’s organ systems, such as the circulatory, respiratory, and digestive systems, work together so that one system’s output often becomes another system’s input, keeping the whole body functioning.',
   [('Which two body systems work closely together to deliver oxygen to the blood?', ['The circulatory and respiratory systems', 'The digestive and skeletal systems', 'A concept unrelated to body systems', 'The nervous and excretory systems only'], 0),
    ('Does the digestive system provide nutrients that the circulatory system then carries to the rest of the body?', ['Yes', 'No, these two systems never interact', 'A concept unrelated to body systems', 'The circulatory system only carries oxygen, never nutrients'], 0),
    ('Can a problem in one body system sometimes affect how another system functions?', ['Yes', 'No, body systems always function completely independently', 'A concept unrelated to body systems', 'Body systems never have any connection to one another'], 0),
    ('Why might scientists describe the human body as a system of interconnected systems rather than separate parts?', ['Each system depends on others to carry out its job, so they must work together', 'Body systems never actually depend on one another', 'This concept has no relevance to science', 'Every body system works in complete isolation from the others'], 0),
    ('Why might understanding how body systems work together help explain why exercise affects more than just the muscles?', ['Exercise can also increase heart rate and breathing, showing multiple systems responding together', 'Exercise never has any effect beyond the muscular system', 'This concept has no connection to body systems', 'Only one single body system is ever involved in physical activity'], 0)]),
SS('The Canadian Shield: Geography and Geology',
   'Grade 5 Social Studies strand: the Canadian Shield is a vast region of ancient rock covering much of central and northern Canada, rich in minerals and shaped by glaciers during the last ice age.',
   [('What do we call the vast region of ancient rock covering much of central and northern Canada?', ['The Canadian Shield', 'The Rocky Mountains', 'A concept unrelated to Canadian geography', 'The Great Plains'], 0),
    ('Is the Canadian Shield known for containing valuable mineral deposits?', ['Yes', 'No, the Canadian Shield contains no valuable resources', 'A concept unrelated to Canadian geography', 'Minerals are only ever found outside the Canadian Shield'], 0),
    ('Did glaciers help shape the landscape of the Canadian Shield during the last ice age?', ['Yes', 'No, glaciers never affected the Canadian Shield', 'A concept unrelated to Canadian geography', 'The Canadian Shield formed only in the last hundred years'], 0),
    ('Why might mining be an important economic activity in areas of the Canadian Shield?', ['The region contains rich mineral deposits that can be extracted and used', 'Mining has no connection to the Canadian Shield’s geology', 'This concept has no relevance to social studies', 'The Canadian Shield has never had any economic importance'], 0),
    ('Why is the Canadian Shield considered one of the oldest geological regions on Earth?', ['Its rock formations date back billions of years, among the oldest known rock on the planet', 'The Canadian Shield formed only very recently, geologically speaking', 'This concept has no connection to Canadian geography', 'Rock in the Canadian Shield is no different in age from anywhere else'], 0)]),
]),

day(105, [
L('Writing: Writing a Formal Letter or Email',
  'Grade 5 Language strand: a formal letter or email follows conventions such as a polite greeting, clear purpose, respectful tone, and formal closing, and is used when writing to someone like a principal or a company.',
  [('Which greeting would be most appropriate to open a formal letter to a principal?', ['Dear Principal Smith,', 'Hey there,', 'Yo,', 'What’s up,'], 0),
   ('Which of these would be an appropriate formal closing for a letter?', ['Sincerely,', 'Later,', 'Bye for now,', 'See ya,'], 0),
   ('Should a formal letter to a company generally use a respectful, polite tone?', ['Yes', 'No, formal letters should always sound rude', 'A concept unrelated to writing', 'Tone never matters in a formal letter'], 0),
   ('Why is it important to clearly state your purpose near the beginning of a formal letter or email?', ['It helps the reader quickly understand why you are writing and what you need', 'Stating a purpose never helps a reader understand a letter', 'This concept has no connection to writing', 'A formal letter should never explain why it was written'], 0),
   ('Why might a student choose to write a formal email instead of a casual message when contacting a teacher about a serious concern?', ['A formal tone shows respect and helps the message be taken seriously', 'Formal writing is never appropriate for contacting a teacher', 'This concept has no relevance to writing', 'Casual and formal writing are always treated exactly the same way'], 0)]),
M('Algebra: Describing and Extending Pattern Rules in Words',
  'Grade 5 Math strand: a pattern rule describes in words how a sequence changes from one term to the next, such as start at 3 and add 4 each time, and can be used to extend or predict future terms.',
  [('What is the pattern rule for the sequence 3, 7, 11, 15?', ['Start at 3 and add 4 each time', 'Start at 3 and add 3 each time', 'Start at 3 and multiply by 4 each time', 'Start at 3 and subtract 4 each time'], 0),
   ('Using the rule start at 2 and add 5 each time, what are the first four terms?', ['2, 7, 12, 17', '2, 5, 10, 15', '2, 7, 14, 21', '5, 10, 15, 20'], 0),
   ('What is the next term in the sequence 4, 8, 12, 16, ___?', ['20', '18', '24', '22'], 0),
   ('Why is it useful to describe a pattern rule in words rather than just listing numbers?', ['A word rule can be used to predict any future term without listing every number first', 'A word rule never helps predict future terms', 'This concept has no connection to algebra', 'Number sequences can never be described using words'], 0),
   ('Why might two different pattern rules sometimes produce the same first few terms but different later terms?', ['Different rules can coincidentally match for a few terms before the patterns diverge', 'Two different pattern rules can never share the same first terms', 'This concept has no relevance to algebra', 'All pattern rules always produce identical sequences forever'], 0)]),
Sc('Structures: The Role of Foundations in Buildings',
   'Grade 5 Science strand: a foundation is the base of a structure that transfers its weight safely into the ground, providing stability and preventing sinking, shifting, or collapse.',
   [('What do we call the base of a structure that transfers its weight into the ground?', ['A foundation', 'A truss', 'A beam', 'A concept unrelated to structures'], 0),
    ('Does a strong foundation help prevent a building from sinking or shifting over time?', ['Yes', 'No, a foundation never affects a building’s stability', 'A concept unrelated to structures', 'Foundations only ever make a building weaker'], 0),
    ('Would a building on soft, unstable ground typically need a stronger foundation than one on solid rock?', ['Yes', 'No, ground type never affects foundation strength', 'A concept unrelated to structures', 'All buildings need exactly the same foundation regardless of ground type'], 0),
    ('Why might engineers dig deep into the ground before laying a building’s foundation?', ['Reaching stable ground helps ensure the structure will not sink or shift over time', 'Digging deep never has any effect on a building’s stability', 'This concept has no relevance to science', 'Foundations are always built directly on top of loose soil with no digging'], 0),
    ('Why is a strong foundation especially important for a tall building, like a skyscraper?', ['A taller, heavier structure places greater pressure on the ground, requiring more support', 'Tall buildings need less foundation support than short ones', 'This concept has no connection to structures', 'The height of a building never affects how much foundation support it needs'], 0)]),
SS('Canada’s Boreal Forest Region',
   'Grade 5 Social Studies strand: the boreal forest is a vast region of coniferous trees stretching across much of northern Canada, providing habitat for wildlife and supporting the forestry industry.',
   [('What type of trees mostly make up Canada’s boreal forest?', ['Coniferous trees', 'Only cactus plants', 'A concept unrelated to Canadian geography', 'Only tropical palm trees'], 0),
    ('Does the boreal forest stretch across a large part of northern Canada?', ['Yes', 'No, the boreal forest covers only a tiny area', 'A concept unrelated to Canadian geography', 'The boreal forest does not exist in Canada'], 0),
    ('Can the boreal forest provide habitat for wildlife, such as moose and wolves?', ['Yes', 'No, the boreal forest supports no wildlife at all', 'A concept unrelated to the boreal forest', 'Only fish live in the boreal forest region'], 0),
    ('Why might the forestry industry be closely connected to Canada’s boreal forest region?', ['The vast coniferous forest provides a major source of wood and forest products', 'The forestry industry has no connection to the boreal forest at all', 'This concept has no relevance to social studies', 'The boreal forest contains no trees suitable for forestry'], 0),
    ('Why is it important to manage the boreal forest sustainably, considering both wildlife and industry?', ['Balancing resource use with habitat protection helps the forest support people and wildlife long term', 'Sustainable management never affects wildlife or industry', 'This concept has no connection to Canadian geography', 'The boreal forest requires no management at all'], 0)]),
]),

day(106, [
L('Grammar: Comma Usage in Lists, Dates, and Addresses',
  'Grade 5 Language strand: commas are used to separate items in a list, to separate the day from the year in a date, and to separate parts of an address, such as a city from a province.',
  [('Where should a comma be placed in the list apples, oranges and bananas to correctly separate all three items?', ['Apples, oranges, and bananas', 'Apples oranges, and bananas', 'Apples, oranges and, bananas', 'Apples oranges and bananas'], 0),
   ('Which of these correctly uses a comma in a date?', ['July 1, 2026', 'July, 1 2026', 'July 1 2026,', 'July, 1, 2026,'], 0),
   ('Which of these correctly uses a comma in an address?', ['Toronto, Ontario', 'Toronto Ontario,', 'Toronto, Ontario,,', ',Toronto Ontario'], 0),
   ('Why is it important to use commas correctly when listing several items in a sentence?', ['It helps the reader clearly tell where one item ends and the next begins', 'Commas never make a list of items easier to read', 'This concept has no connection to grammar', 'Lists are always clear whether or not commas are used'], 0),
   ('Why might leaving out a comma in a date or address make a sentence confusing?', ['Without the comma, the different parts of the information can blend together unclearly', 'Missing commas never cause any confusion in a sentence', 'This concept has no relevance to grammar', 'Dates and addresses never actually require any commas'], 0)]),
M('Geometry: Representing 3D Objects Using Top, Front, and Side Views',
  'Grade 5 Math strand: a three-dimensional object can be represented on paper by drawing its top view, front view, and side view, showing what the shape looks like from each direction.',
  [('What do we call the drawing that shows what a 3D object looks like when viewed from directly above?', ['The top view', 'The front view', 'The side view', 'A concept unrelated to geometry'], 0),
   ('How many different standard views are typically used to represent a 3D object on paper: top, front, and ___?', ['Side', 'Back', 'Diagonal', 'Bottom'], 0),
   ('Would the top view of a cube typically look like a square?', ['Yes', 'No, the top view of a cube is never a square', 'A concept unrelated to geometry', 'A cube has no top view at all'], 0),
   ('Why might an engineer use top, front, and side views instead of just one drawing to represent an object?', ['Multiple views together give a complete and accurate picture of the object’s shape', 'Using multiple views never provides any extra information about a shape', 'This concept has no connection to geometry', 'One single view always shows every detail of a 3D object'], 0),
   ('Why might two different 3D objects have the same top view but different front views?', ['Objects can share the same outline from one direction while differing in shape from another', 'Two different objects can never share the same view from any direction', 'This concept has no relevance to geometry', 'The top view of an object always reveals its entire three-dimensional shape'], 0)]),
Sc('Matter and Energy: Properties of Recyclable Materials',
   'Grade 5 Science strand: materials such as paper, plastic, metal, and glass have different properties that determine how they can be recycled and reused, helping conserve natural resources.',
   [('Which of these materials can typically be recycled?', ['Glass', 'A concept unrelated to recycling', 'Nothing can ever be recycled', 'Materials are never separated by type'], 0),
    ('Why might metal be a material that can be recycled many times without losing quality?', ['Metal can often be melted down and reshaped repeatedly without breaking down', 'Metal can never be melted down or reshaped', 'This concept has no relevance to science', 'Metal loses all of its properties the first time it is recycled'], 0),
    ('Does sorting recyclable materials, like separating glass from plastic, help the recycling process?', ['Yes', 'No, sorting materials never helps with recycling', 'A concept unrelated to recyclable materials', 'All materials are recycled using the exact same process regardless of type'], 0),
    ('Why is understanding the properties of different materials important for recycling programs?', ['Different materials require different recycling processes based on their properties', 'Material properties never affect how something is recycled', 'This concept has no connection to matter and energy', 'All materials are processed in an identical way no matter their properties'], 0),
    ('Why might recycling paper help conserve natural resources, such as trees?', ['Reusing paper fibres reduces the need to cut down new trees to make paper', 'Recycling paper never has any effect on how many trees are used', 'This concept has no relevance to science', 'Paper can never actually be made from recycled materials'], 0)]),
SS('How Federal Elections Work: The Role of Elections Canada',
   'Grade 5 Social Studies strand: Elections Canada is the independent agency responsible for organizing federal elections, ensuring eligible voters can cast ballots and that results are counted fairly.',
   [('What is the name of the independent agency responsible for organizing federal elections in Canada?', ['Elections Canada', 'The Bank of Canada', 'A concept unrelated to Canadian government', 'The Supreme Court of Canada'], 0),
    ('Is Elections Canada responsible for making sure federal election results are counted fairly?', ['Yes', 'No, Elections Canada has no role in counting votes', 'A concept unrelated to elections', 'Election results are never actually counted in Canada'], 0),
    ('Must a person typically be a certain age and a Canadian citizen to vote in a federal election?', ['Yes', 'No, anyone of any age or citizenship can vote', 'A concept unrelated to Canadian elections', 'Voting rules are never enforced in Canada'], 0),
    ('Why might it be important for an agency like Elections Canada to be independent from any political party?', ['Independence helps ensure elections are run fairly, without favouring one party over another', 'An independent agency never has any advantage in running elections fairly', 'This concept has no relevance to social studies', 'Elections in Canada are always run directly by political parties themselves'], 0),
    ('Why does Elections Canada work to make voting accessible, such as through advance polls or mail-in ballots?', ['Making voting more accessible helps more eligible citizens participate in choosing their government', 'Accessible voting options never help more people participate in elections', 'This concept has no connection to Canadian government', 'Elections Canada only allows voting on a single specific day with no other options'], 0)]),
]),

day(107, [
L('Reading: Recognizing an Unreliable Narrator',
  'Grade 5 Language strand: an unreliable narrator is a storyteller whose account of events may be incomplete, biased, or inaccurate, requiring readers to think critically about what is really happening.',
  [('What do we call a narrator whose account of events may be biased or inaccurate?', ['An unreliable narrator', 'A reliable narrator', 'A concept unrelated to reading', 'A third-person narrator only'], 0),
   ('Might a narrator’s young age or strong emotions be a reason readers should question what they say?', ['Yes', 'No, a narrator’s age or emotions never affect how believable they are', 'A concept unrelated to reading', 'Narrators are always completely truthful no matter what'], 0),
   ('Should readers sometimes compare a narrator’s claims with other clues in the story to check accuracy?', ['Yes', 'No, readers should never question anything a narrator says', 'A concept unrelated to reading comprehension', 'Clues in a story never reveal anything about a narrator'], 0),
   ('Why might an author choose to use an unreliable narrator instead of a completely truthful one?', ['It can create suspense or surprise as readers piece together the real story', 'Unreliable narrators never add anything interesting to a story', 'This concept has no connection to reading comprehension', 'A narrator’s reliability never affects how a reader experiences a story'], 0),
   ('Why is it important for readers to think critically when a story is told from only one character’s point of view?', ['That character’s perspective might leave out details or show bias that affects the full picture', 'A single point of view always shows every important detail with no bias', 'This concept has no relevance to reading', 'Readers never need to think critically about who is telling a story'], 0)]),
M('Data Management: Constructing and Interpreting Double Bar Graphs',
  'Grade 5 Math strand: a double bar graph displays two related sets of data side by side for each category, making it easy to compare values, such as sales in two different months.',
  [('What is the purpose of a double bar graph?', ['To compare two related sets of data side by side', 'To show only one set of data', 'A concept unrelated to data management', 'To display data as a single line'], 0),
   ('In a double bar graph comparing rainfall in two cities, how many bars would typically appear for each month?', ['2', '1', '4', '3'], 0),
   ('Would a double bar graph be a good choice for comparing test scores between two different classes?', ['Yes', 'No, double bar graphs cannot compare two groups', 'A concept unrelated to data management', 'Double bar graphs can only show one number at a time'], 0),
   ('Why might a double bar graph be more useful than two separate single bar graphs when comparing data?', ['It allows for an easier direct comparison between related values side by side', 'A double bar graph never makes comparing data easier', 'This concept has no connection to data management', 'Two separate graphs always show information more clearly than one combined graph'], 0),
   ('Why is a clear legend important when reading a double bar graph?', ['It helps the reader know which colour or pattern represents which set of data', 'A legend never helps explain what a graph is showing', 'This concept has no relevance to data management', 'Double bar graphs never actually need a legend to be understood'], 0)]),
Sc('Earth and Space Systems: How Fossil Fuels Form Over Time',
   'Grade 5 Science strand: fossil fuels, such as coal, oil, and natural gas, form over millions of years from the buried remains of ancient plants and animals under heat and pressure.',
   [('Approximately how long does it take for fossil fuels to form underground?', ['Millions of years', 'A few days', 'One year', 'A few weeks'], 0),
    ('What are fossil fuels formed from?', ['The buried remains of ancient plants and animals', 'Freshly cut wood', 'A concept unrelated to fossil fuels', 'Rainwater and snow'], 0),
    ('Name one example of a fossil fuel.', ['Coal', 'A concept unrelated to fossil fuels', 'Wind', 'Sunlight'], 0),
    ('Why are fossil fuels considered a non-renewable resource?', ['They take millions of years to form, far longer than they can be replaced through use', 'Fossil fuels can be created again within a few days', 'This concept has no relevance to science', 'Fossil fuels are never actually used up once extracted'], 0),
    ('Why might heat and pressure underground be important parts of how fossil fuels form?', ['They gradually transform buried organic remains into coal, oil, or natural gas over time', 'Heat and pressure never play any role in forming fossil fuels', 'This concept has no connection to Earth and Space systems', 'Fossil fuels form instantly with no heat or pressure required'], 0)]),
SS('The Canadian Coast Guard and Maritime Safety',
   'Grade 5 Social Studies strand: the Canadian Coast Guard is a federal agency responsible for maritime safety, search and rescue at sea, and protecting Canada’s waterways along its coasts and inland lakes.',
   [('What is the name of the federal agency responsible for maritime safety in Canada?', ['The Canadian Coast Guard', 'The Royal Canadian Mounted Police', 'A concept unrelated to Canadian government', 'The Bank of Canada'], 0),
    ('Is search and rescue at sea one of the responsibilities of the Canadian Coast Guard?', ['Yes', 'No, the Coast Guard has no role in search and rescue', 'A concept unrelated to maritime safety', 'Search and rescue is handled only by private companies'], 0),
    ('Does the Canadian Coast Guard help protect Canada’s waterways, including inland lakes?', ['Yes', 'No, the Coast Guard only ever operates on land', 'A concept unrelated to the Coast Guard', 'Canada has no inland lakes to protect'], 0),
    ('Why might Canada need a Coast Guard given its long coastlines and many waterways?', ['Its vast coastlines and waterways require an agency dedicated to safety and emergency response on the water', 'Canada has no coastlines or waterways that need protecting', 'This concept has no relevance to social studies', 'Maritime safety is never actually a concern for a country like Canada'], 0),
    ('Why is it useful for the Coast Guard to work separately from, but alongside, other agencies like the RCMP?', ['Different agencies can focus on their specific areas of responsibility, such as maritime safety versus policing', 'Separate agencies never need to work together in any way', 'This concept has no connection to Canadian government', 'The Coast Guard and the RCMP always perform the exact same duties'], 0)]),
]),

day(108, [
L('Media Literacy: Point of View and Bias in News Media',
  'Grade 5 Language strand: news media can present information from a particular point of view, and recognizing bias means noticing when word choice, story selection, or tone favours one perspective over another.',
  [('What does it mean when a news story shows bias?', ['It favours one perspective over another', 'It presents every viewpoint with perfect balance', 'A concept unrelated to media literacy', 'It contains no opinions of any kind'], 0),
   ('Which of these might be a sign of bias in a news article?', ['Using strongly emotional words to describe only one side of an issue', 'Including facts and multiple viewpoints', 'Citing several different reliable sources', 'Presenting statistics from a study'], 0),
   ('Can two different news sources report on the same event but present it from different points of view?', ['Yes', 'No, all news sources always report events identically', 'A concept unrelated to media literacy', 'News sources are never allowed to have different perspectives'], 0),
   ('Why is it helpful to compare multiple news sources when researching a topic?', ['It can reveal different perspectives and help identify potential bias in any single source', 'Comparing sources never reveals anything useful about a topic', 'This concept has no connection to media literacy', 'Every news source always reports the exact same information in the exact same way'], 0),
   ('Why might word choice, like calling a group protesters versus rioters, reveal a media source’s point of view?', ['Different words can create very different impressions of the same event for readers', 'Word choice never affects how a reader interprets a news story', 'This concept has no relevance to media literacy', 'All words used in news stories carry the exact same meaning'], 0)]),
M('Measurement: Reading Thermometers and Temperature in Celsius',
  'Grade 5 Math strand: students read temperatures on a Celsius thermometer, understanding that water freezes at 0 degrees Celsius and boils at 100 degrees Celsius, and can calculate temperature changes.',
  [('At what temperature does water freeze on the Celsius scale?', ['0 degrees Celsius', '32 degrees Celsius', '100 degrees Celsius', '212 degrees Celsius'], 0),
   ('At what temperature does water boil on the Celsius scale?', ['100 degrees Celsius', '0 degrees Celsius', '50 degrees Celsius', '212 degrees Celsius'], 0),
   ('If the temperature rises from 12 degrees Celsius to 19 degrees Celsius, by how many degrees did it increase?', ['7 degrees', '5 degrees', '9 degrees', '12 degrees'], 0),
   ('If the temperature is 3 degrees Celsius and drops by 8 degrees, what is the new temperature?', ['-5 degrees Celsius', '5 degrees Celsius', '-11 degrees Celsius', '11 degrees Celsius'], 0),
   ('Why is it useful to know key reference points, like water’s freezing and boiling points, when reading a Celsius thermometer?', ['They give helpful benchmarks for estimating and understanding other temperature readings', 'These reference points never help with reading a thermometer', 'This concept has no connection to measurement', 'Water freezes and boils at the exact same temperature'], 0)]),
Sc('Life Systems: Symbiotic Relationships in Nature',
   'Grade 5 Science strand: symbiosis describes close relationships between different species, including mutualism where both benefit, commensalism where one benefits without harming the other, and parasitism where one benefits at the other’s expense.',
   [('What do we call a close relationship between two different species in nature?', ['A symbiotic relationship', 'A food chain', 'A concept unrelated to ecosystems', 'A migration pattern'], 0),
    ('What type of symbiotic relationship benefits both species involved?', ['Mutualism', 'Parasitism', 'A concept unrelated to symbiosis', 'Commensalism only harms both species'], 0),
    ('In a parasitic relationship, does one organism typically benefit at the expense of the other?', ['Yes', 'No, both organisms are always harmed equally', 'A concept unrelated to symbiosis', 'Neither organism is ever affected in a parasitic relationship'], 0),
    ('Why might bees and flowers be considered an example of a mutualistic relationship?', ['Bees get nectar for food while flowers get help spreading pollen to reproduce', 'Bees and flowers never actually interact with each other', 'This concept has no relevance to science', 'Only the flower benefits while the bee is harmed'], 0),
    ('Why might understanding symbiotic relationships help explain how removing one species can affect an entire ecosystem?', ['Species that depend on each other closely can be strongly affected if one of them disappears', 'Species in an ecosystem are never actually connected to one another', 'This concept has no connection to life systems', 'Removing one species never has any effect on other species'], 0)]),
SS('Free Trade Agreements: NAFTA and CUSMA',
   'Grade 5 Social Studies strand: Canada, the United States, and Mexico have signed free trade agreements, first NAFTA and later CUSMA, which reduce trade barriers and shape how goods move between the three countries.',
   [('What does NAFTA stand for?', ['The North American Free Trade Agreement', 'The National Fair Trade Association', 'A concept unrelated to Canadian trade', 'The New American Farming and Trade Act'], 0),
    ('Which three countries are part of the trade agreement known as CUSMA?', ['Canada, the United States, and Mexico', 'Canada, France, and the United States', 'Canada, Mexico, and Brazil', 'The United States, Mexico, and China'], 0),
    ('Does a free trade agreement generally aim to reduce barriers to trade between countries, such as tariffs?', ['Yes', 'No, free trade agreements always increase trade barriers', 'A concept unrelated to trade agreements', 'Trade agreements never affect how goods move between countries'], 0),
    ('Why might Canada benefit from having a free trade agreement with its neighbouring countries?', ['It can make it easier and more affordable to buy and sell goods across borders', 'Free trade agreements never provide any economic benefit', 'This concept has no relevance to social studies', 'Trade agreements always make goods more expensive for everyone'], 0),
    ('Why did CUSMA eventually replace NAFTA as the trade agreement between the three countries?', ['The countries renegotiated updated terms that better reflected current trade needs', 'CUSMA and NAFTA are actually the exact same unchanged agreement', 'This concept has no connection to Canadian trade', 'Trade agreements between countries are never renegotiated or replaced'], 0)]),
]),

day(109, [
L('Grammar: Types of Adverbs and Their Functions',
  'Grade 5 Language strand: adverbs can describe manner, such as quickly, time, such as yesterday, place, such as outside, or frequency, such as often, and typically modify a verb, adjective, or another adverb.',
  [('What type of adverb does the word quickly describe?', ['Manner', 'Time', 'Place', 'Frequency'], 0),
   ('What type of adverb does the word yesterday describe?', ['Time', 'Manner', 'Place', 'Frequency'], 0),
   ('In the sentence She often sings loudly, which word is an adverb of frequency?', ['Often', 'Sings', 'Loudly', 'She'], 0),
   ('Why might a writer use an adverb of manner, like carefully, to describe an action?', ['It gives the reader a clearer picture of how the action is being performed', 'Adverbs of manner never add any detail to a sentence', 'This concept has no connection to grammar', 'Describing how an action happens is never useful in writing'], 0),
   ('Why is it useful to know that adverbs can modify adjectives, not just verbs, such as in extremely tall?', ['It shows adverbs can add detail to many different parts of a sentence, not only actions', 'Adverbs can only ever modify verbs and nothing else', 'This concept has no relevance to grammar', 'Adjectives are never modified by any other part of speech'], 0)]),
M('Number Sense: Estimating Products and Quotients',
  'Grade 5 Math strand: students estimate products and quotients by rounding numbers to a convenient value before multiplying or dividing, helping check whether an exact answer is reasonable.',
  [('To estimate the product of 48 times 22, which rounded numbers might you use?', ['50 times 20', '48 times 22 exactly', '40 times 30', '50 times 30'], 0),
   ('Using the estimate 50 times 20, what is the estimated product?', ['1000', '100', '10000', '500'], 0),
   ('To estimate 396 divided by 4, which rounded number might you use for 396?', ['400', '390', '300', '500'], 0),
   ('Why is estimating useful before solving a multiplication or division problem with exact numbers?', ['It helps you check whether your final exact answer seems reasonable', 'Estimating never helps determine whether an answer makes sense', 'This concept has no connection to number sense', 'An estimate is always identical to the exact answer'], 0),
   ('Why might rounding both numbers in a multiplication problem make estimation quicker, even though it changes the exact values?', ['Rounded numbers are easier to multiply mentally while still giving a reasonably close answer', 'Rounding numbers never makes a calculation easier', 'This concept has no relevance to number sense', 'An estimate must always use the exact original numbers'], 0)]),
Sc('Matter and Energy: How Materials Absorb or Reflect Sound',
   'Grade 5 Science strand: soft, porous materials like foam tend to absorb sound waves and reduce echo, while hard, smooth surfaces like glass or tile tend to reflect sound waves, which can create echoes.',
   [('What type of material tends to absorb sound waves and reduce echo?', ['Soft, porous materials like foam', 'Hard, smooth surfaces like glass', 'A concept unrelated to sound', 'Materials never affect how sound behaves'], 0),
    ('What type of surface tends to reflect sound waves, sometimes creating an echo?', ['Hard, smooth surfaces like tile or glass', 'Soft, porous materials like foam', 'A concept unrelated to sound', 'No surfaces ever reflect sound'], 0),
    ('Would a room with soft carpets and curtains typically have less echo than a room with bare walls and tile floors?', ['Yes', 'No, soft materials never reduce echo', 'A concept unrelated to sound', 'Echo is unaffected by the materials in a room'], 0),
    ('Why might recording studios use soft, foam panels on their walls?', ['The foam absorbs sound waves, reducing unwanted echo during recordings', 'Foam panels have no effect on sound in a room', 'This concept has no relevance to science', 'Foam panels are used only for decoration and never affect sound'], 0),
    ('Why might a large, empty gymnasium with hard walls and floors sound especially echoey?', ['The hard, smooth surfaces reflect sound waves repeatedly instead of absorbing them', 'Hard surfaces always absorb sound completely, preventing any echo', 'This concept has no connection to matter and energy', 'Echo is never affected by the surfaces or size of a room'], 0)]),
SS('Canada’s Forestry Industry and Its Economic Importance',
   'Grade 5 Social Studies strand: Canada’s forestry industry harvests wood from its vast forests to produce products like lumber and paper, providing jobs and economic activity in many regions, especially in British Columbia and Quebec.',
   [('What does Canada’s forestry industry primarily harvest from its forests?', ['Wood', 'Fish', 'Minerals', 'A concept unrelated to forestry'], 0),
    ('Name one product made from wood harvested by the forestry industry.', ['Lumber', 'A concept unrelated to forestry', 'Steel', 'Plastic'], 0),
    ('Does the forestry industry provide jobs and economic activity in regions like British Columbia and Quebec?', ['Yes', 'No, the forestry industry provides no jobs anywhere in Canada', 'A concept unrelated to forestry', 'Forestry has no economic importance in Canada'], 0),
    ('Why might the forestry industry be especially important to communities located near large forested areas?', ['Nearby forests can provide a steady source of jobs and resources for local economies', 'The forestry industry never has any connection to nearby communities', 'This concept has no relevance to social studies', 'Forested regions never provide any economic opportunities'], 0),
    ('Why is sustainable forest management, such as replanting trees, important for the long-term future of the forestry industry?', ['It helps ensure forests can continue producing wood resources for future generations', 'Sustainable management never affects the future of an industry', 'This concept has no connection to Canada’s forestry industry', 'Forests regrow instantly with no need for replanting or management'], 0)]),
]),

day(110, [
L('Review: Oral Communication, Grammar, and Reading (Days 101-109)',
  'Grade 5 Language strand review: students revisit active listening and speaking, apostrophes, problem-and-solution text structure, compound words, formal letters, comma usage, unreliable narrators, media bias, and types of adverbs.',
  [('What is one key habit of an active listener during a conversation?', ['Giving full attention to the speaker', 'Looking at a phone while someone talks', 'Interrupting to share your own story', 'Thinking only about your next turn to speak'], 0),
   ('What is the contraction for do not?', ['Don’t', 'Dont', 'Do’nt', 'Do not’'], 0),
   ('What does a problem-and-solution text structure present to the reader?', ['A problem and one or more ways to solve it', 'Only a list of unrelated facts', 'A concept unrelated to text structure', 'A story with no real conflict'], 0),
   ('What do we call a word formed by joining two smaller words together?', ['A compound word', 'A synonym', 'An antonym', 'A concept unrelated to vocabulary'], 0),
   ('What do we call a narrator whose account of events may be biased or inaccurate?', ['An unreliable narrator', 'A reliable narrator', 'A concept unrelated to reading', 'A third-person narrator only'], 0)]),
M('Review: Number Sense, Data, Financial Literacy, and Geometry (Days 101-109)',
  'Grade 5 Math strand review: students revisit place value to one million, range and outliers, sales tax and discounts, converting metric capacity and mass, pattern rules, 3D object views, double bar graphs, Celsius thermometers, and estimation.',
  [('In the number 452,367, what is the value of the digit 4?', ['400,000', '4,000', '40,000', '4'], 0),
   ('How do you calculate the range of a data set?', ['Subtract the least value from the greatest value', 'Add all the values together', 'Multiply the greatest and least values', 'A concept unrelated to data management'], 0),
   ('If an item costs 20 dollars and the sales tax is 10 percent, how much tax is added?', ['2 dollars', '10 dollars', '20 dollars', '1 dollar'], 0),
   ('How many millilitres are in 1 litre?', ['1000', '100', '10', '10000'], 0),
   ('At what temperature does water freeze on the Celsius scale?', ['0 degrees Celsius', '32 degrees Celsius', '100 degrees Celsius', '212 degrees Celsius'], 0)]),
Sc('Review: Structures, Life Systems, and Matter and Energy (Days 101-109)',
   'Grade 5 Science strand review: students revisit tension and compression, the screw and the wedge, migration and hibernation, fossil fuel formation, and symbiotic relationships.',
   [('What do we call a force that pulls or stretches a material?', ['Tension', 'Compression', 'A concept unrelated to structures', 'Friction'], 0),
    ('What simple machine is made of an inclined plane wrapped around a cylinder?', ['A screw', 'A wedge', 'A lever', 'A pulley'], 0),
    ('What do we call it when an animal travels to a different location to survive seasonal changes?', ['Migration', 'Hibernation', 'A concept unrelated to survival strategies', 'Metamorphosis'], 0),
    ('Approximately how long does it take for fossil fuels to form underground?', ['Millions of years', 'A few days', 'One year', 'A few weeks'], 0),
    ('What do we call a close relationship between two different species in nature?', ['A symbiotic relationship', 'A food chain', 'A concept unrelated to ecosystems', 'A migration pattern'], 0)]),
SS('Review: Government Structures, Geography, and Economy (Days 101-109)',
   'Grade 5 Social Studies strand review: students revisit provincial symbols, the Senate, the Canadian Shield, Elections Canada, and Canada’s forestry industry.',
   [('Does each Canadian province have its own official flag?', ['Yes', 'No, all provinces share one identical flag', 'A concept unrelated to Canadian identity', 'Only some provinces are allowed to have flags'], 0),
    ('What is the name of the appointed upper house of Canada’s Parliament?', ['The Senate', 'The House of Commons', 'A concept unrelated to Canadian government', 'The Supreme Court'], 0),
    ('What do we call the vast region of ancient rock covering much of central and northern Canada?', ['The Canadian Shield', 'The Rocky Mountains', 'A concept unrelated to Canadian geography', 'The Great Plains'], 0),
    ('What is the name of the independent agency responsible for organizing federal elections in Canada?', ['Elections Canada', 'The Bank of Canada', 'A concept unrelated to Canadian government', 'The Supreme Court of Canada'], 0),
    ('What does Canada’s forestry industry primarily harvest from its forests?', ['Wood', 'Fish', 'Minerals', 'A concept unrelated to forestry'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_101_110)
    append_to(5, g5_101_110)
