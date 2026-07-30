#!/usr/bin/env python3
"""Grade 2, Days 111-120 -- ninth batch, extending Grade 2 past Day 110
toward the full ~187-day school year. Uses the sub()/day()/append_to()
helpers imported directly from gen_curriculum.py (no worksheet field):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by fetch_video_ids.py)

Topics chosen to avoid overlap with existing Grade 2 Days 1-110 (see
data/grade2.ts / data/grade2.json, which already densely covers nearly the
full grade 2 ELA, math, science, and social studies curriculum): apostrophe
uses, syllable division, text-to-text/world connections, graphic novels,
oral discussion, peer editing, story sequels, word origins, and list
poems for Language; multiplication facts to 12, two-digit x one-digit
multiplication, exact-minute time, expanded form, multiples of ten,
data range, 3D nets, estimating quotients, and multi-step word problems
for Math; water conservation, composting, air quality, sound through
materials, birds of prey, plant defenses, coral reefs, bee colonies, and
comparing animal senses for Science; and the War of 1812, the justice
system, Canadian media, Canadian astronauts, weather records, the census,
time capsules, sister cities, and public signs for Social Studies --
none of those exact ideas appear in Days 1-110. Day 120 is a review day
across all four subjects, matching the end-of-batch pattern used in every
prior 10-day batch. No embedded ASCII double-quote or straight apostrophe
characters are used anywhere in title/summary/quiz text -- contractions
and possessives are avoided entirely (or rewritten without the apostrophe)
to keep the generated .ts string literals valid.
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


def _rebalance_answer_positions(days, seed=20260726):
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


g2_111_120 = [
day(111, [
L('Apostrophes: Contractions vs Possessives',
  'Grade 2 Language strand: an apostrophe can either join two words into a contraction, like do not becoming dont, or show ownership in a possessive noun, like the dogs bone.',
  [('In dont, why is an apostrophe used?', ['To join two words into one', 'It shows a contraction is being made', 'To end a sentence', 'It has no purpose'], 1),
   ('In the dogs bone, why is an apostrophe used?', ['To show the bone belongs to the dog', 'To join two words', 'To make a plural', 'To end the sentence'], 0),
   ('Which of these is a contraction?', ['Cats', 'Cannot', 'Cant', 'Cat'], 2),
   ('Which of these shows possession?', ['Girls run.', 'The girls shoes are new.', 'Girls play.', 'Two girls.'], 1),
   ('An apostrophe used in a possessive noun shows ___.', ['Ownership', 'A question', 'A plural only', 'The end of a sentence'], 0)]),
M('Multiplication Facts: 11s and 12s',
  'Grade 2 Math strand: students extend their multiplication fact fluency to include the 11 times table and the 12 times table.',
  [('What is 11 x 3?', ['30', '31', '33', '32'], 2),
   ('What is 12 x 2?', ['22', '24', '26', '20'], 1),
   ('What is 11 x 5?', ['50', '55', '60', '45'], 1),
   ('What is 12 x 4?', ['44', '46', '48', '42'], 2),
   ('What is 11 x 11?', ['111', '121', '110', '112'], 1)]),
Sc('Water Conservation: Using Water Wisely',
   'Grade 2 Science strand: water conservation means using water carefully and avoiding waste, such as turning off taps and fixing leaks, so there is enough clean water for everyone.',
   [('What does water conservation mean?', ['Using water carefully and not wasting it', 'Using as much water as possible', 'Never using water', 'Wasting water on purpose'], 0),
    ('Which action helps conserve water?', ['Leaving the tap running', 'Turning off the tap while brushing teeth', 'Taking very long baths daily', 'Ignoring leaks'], 1),
    ('Why is it important to fix a leaky tap?', ['To stop wasting water', 'Leaks help save water', 'Leaks are good for pipes', 'It does not matter'], 0),
    ('Why do we need to be careful with our water use?', ['So there is enough clean water for everyone', 'Water is not important', 'There is unlimited water everywhere', 'Only oceans matter'], 0),
    ('Which of these is a water-saving habit?', ['Taking shorter showers', 'Letting the hose run all day', 'Leaving taps dripping', 'Filling a pool every day'], 0)]),
SS('The War of 1812: A Conflict That Shaped Canada',
   'Grade 2 Social Studies strand: the War of 1812 was a conflict between the United States and British North America, and it helped shape the identity of what would later become Canada.',
   [('Who fought in the War of 1812?', ['The United States and British North America', 'France and Spain', 'Canada and Mexico', 'No one, it never happened'], 0),
    ('When did the War of 1812 take place?', ['In the early 1800s', 'Last year', 'In the 1900s', 'It has not happened yet'], 0),
    ('Why do people still learn about the War of 1812 today?', ['It helped shape early Canadian identity', 'It has no importance', 'It happened in another country only', 'It was not a real event'], 0),
    ('What area was involved in the War of 1812 that later became part of Canada?', ['British North America', 'South America', 'Australia', 'Africa'], 0),
    ('Learning about historical conflicts like the War of 1812 helps us understand ___.', ['How our country developed over time', 'Nothing about Canada', 'Only foreign history', 'Modern technology'], 0)]),
]),
day(112, [
L('Syllable Division: Breaking Words into Parts',
  'Grade 2 Language strand: dividing a word into syllables, or beats, helps readers sound out and spell longer words, such as splitting rabbit into rab-bit.',
  [('How many syllables are in the word rabbit?', ['One', 'Two', 'Three', 'Four'], 1),
   ('How many syllables are in the word butterfly?', ['One', 'Two', 'Three', 'Four'], 2),
   ('Why is dividing a word into syllables helpful?', ['It helps us sound out and spell longer words', 'It makes words shorter', 'It removes vowels', 'It has no purpose'], 0),
   ('How many syllables are in the word cat?', ['One', 'Two', 'Three', 'Four'], 0),
   ('Where is rabbit divided into syllables?', ['rab-bit', 'ra-bbit', 'r-abbit', 'rabb-it'], 0)]),
M('Multiplying Two-Digit Numbers by a One-Digit Number',
  'Grade 2 Math strand: students learn to multiply a two-digit number by a one-digit number, such as 23 x 3, by breaking the two-digit number into tens and ones.',
  [('What is 12 x 4?', ['46', '48', '50', '44'], 1),
   ('What is 21 x 3?', ['61', '63', '65', '60'], 1),
   ('What is 14 x 2?', ['26', '28', '30', '24'], 1),
   ('What is 32 x 3?', ['92', '94', '96', '90'], 2),
   ('To multiply 23 x 3, you can break 23 into ___.', ['20 and 3', '2 and 3', '23 and 0', '20 and 30'], 0)]),
Sc('Composting: Recycling Food Scraps Into Soil',
   'Grade 2 Science strand: composting is a natural process where food scraps and plant materials break down over time into rich soil that helps new plants grow.',
   [('What is composting?', ['A natural process turning food scraps into soil', 'Throwing food away', 'Freezing food scraps', 'Burning garbage'], 0),
    ('What can be added to a compost pile?', ['Food scraps and plant materials', 'Plastic bags', 'Metal cans', 'Glass bottles'], 0),
    ('What does compost eventually become?', ['Rich soil', 'Clean water', 'Plastic', 'Sand'], 0),
    ('Why is composting good for the environment?', ['It reduces waste and helps plants grow', 'It creates more garbage', 'It pollutes the water', 'It has no benefit'], 0),
    ('What breaks down food scraps in a compost pile over time?', ['Tiny organisms and time', 'Fire', 'Ice', 'Sunlight alone'], 0)]),
SS('Canadas Justice System: Judges and Courts',
   'Grade 2 Social Studies strand: the justice system uses courts and judges to make fair decisions when people disagree or when someone breaks a law.',
   [('Who makes decisions in a courtroom?', ['A judge', 'A mayor', 'A teacher', 'A doctor'], 0),
    ('What is the justice system used for?', ['To make fair decisions when laws are broken or people disagree', 'To sell products', 'To teach math', 'To build houses'], 0),
    ('Where do judges usually work?', ['In a court', 'In a hospital', 'In a school', 'In a farm'], 0),
    ('Why is it important for a justice system to be fair?', ['So everyone is treated equally under the law', 'Fairness does not matter', 'Only some people deserve fairness', 'Judges should be unfair'], 0),
    ('What might happen in a courtroom?', ['A judge helps resolve a disagreement or legal case', 'A birthday party', 'A sports game', 'A cooking class'], 0)]),
]),
day(113, [
L('Making Connections: Text to Text and Text to World',
  'Grade 2 Language strand: readers make connections not only to their own lives but also between two texts (text to text) and between a text and events in the real world (text to world).',
  [('What does text-to-text mean?', ['Connecting one text to another text', 'Connecting a text to your own life', 'Ignoring the text', 'Reading only one book'], 0),
   ('What does text-to-world mean?', ['Connecting a text to real events in the world', 'Connecting a text to another text', 'Skipping the text', 'Memorizing the text'], 0),
   ('Why do readers make connections while reading?', ['It helps deepen understanding of the text', 'It makes reading harder', 'It has no benefit', 'It replaces reading'], 0),
   ('If a story about weather reminds you of a real storm in the news, this is an example of ___.', ['Text to self', 'Text to text', 'Text to world', 'No connection'], 2),
   ('If a story reminds you of another book you read, this is an example of ___.', ['Text to text', 'Text to world', 'Text to self', 'No connection'], 0)]),
M('Telling Time: Reading to the Exact Minute',
  'Grade 2 Math strand: students read an analog clock to tell the exact minute, not just the nearest five minutes, such as 3:47 or 8:12.',
  [('If the minute hand points between the 9 and the 10, closer to 9, what might the time show?', ['Something like :46 or :47', 'Exactly :50', 'Exactly :00', 'Exactly :30'], 0),
   ('How many minutes are in one hour?', ['50', '55', '60', '65'], 2),
   ('If a clock shows 4:23, what hour is it?', ['3', '4', '5', '23'], 1),
   ('If a clock shows 7:58, how many minutes until 8:00?', ['1', '2', '3', '4'], 1),
   ('Reading a clock to the exact minute means checking ___.', ['Only the hour hand', 'Every individual minute mark', 'Only the date', 'Only whether it is day or night'], 1)]),
Sc('Air Quality: Keeping Our Air Clean',
   'Grade 2 Science strand: air quality describes how clean or polluted the air is, and clean air is important for the health of people, animals, and plants.',
   [('What does air quality describe?', ['How clean or polluted the air is', 'How hot the air is', 'How loud the air is', 'How colourful the air is'], 0),
    ('Why is clean air important?', ['It keeps people, animals, and plants healthy', 'It has no importance', 'Only plants need clean air', 'Clean air is not real'], 0),
    ('Which of these can lower air quality?', ['Smoke and pollution', 'Trees', 'Rain', 'Fresh wind'], 0),
    ('What can help improve air quality in a community?', ['Planting trees and reducing pollution', 'Burning more fuel', 'Ignoring pollution', 'Adding more smoke'], 0),
    ('Which living things benefit from clean air?', ['People, animals, and plants', 'Only rocks', 'Nothing benefits', 'Only machines'], 0)]),
SS('Canadian Media: Newspapers, TV, and Online News',
   'Grade 2 Social Studies strand: Canadians learn about their communities and the world through media such as newspapers, television, and online news sources.',
   [('Name one form of media people use to learn the news.', ['Newspapers', 'A dictionary', 'A recipe book', 'A road sign'], 0),
    ('What is the purpose of news media?', ['To inform people about events', 'To confuse people', 'To sell only toys', 'To have no purpose'], 0),
    ('Has the way Canadians get news changed over time?', ['Yes, it has changed with new technology', 'No, it has never changed', 'News did not exist before', 'Only newspapers have ever existed'], 0),
    ('Which is an example of online news?', ['A news website or app', 'A paper map', 'A comic book', 'A cookbook'], 0),
    ('Why is it helpful to know about current events through the media?', ['It helps us understand our community and the world', 'It is not helpful at all', 'News has no value', 'Only adults should know about events'], 0)]),
]),
day(114, [
L('Reading Graphic Novels and Comics: Visual Storytelling',
  'Grade 2 Language strand: graphic novels and comics tell stories using both pictures and words together, with speech bubbles showing what characters say.',
  [('What two things do graphic novels use together to tell a story?', ['Pictures and words', 'Only numbers', 'Only sound', 'Only colours'], 0),
   ('What do speech bubbles show in a comic?', ['What a character is saying', 'The setting of the story', 'The title of the book', 'The page number'], 0),
   ('How is a graphic novel different from a chapter book?', ['It relies heavily on pictures to tell the story', 'It has no pictures at all', 'It has no story', 'It is always shorter'], 0),
   ('Why might pictures help tell a story in a comic?', ['They show action and emotion visually', 'Pictures have no effect on stories', 'Pictures replace all words always', 'They make reading impossible'], 0),
   ('Which of these is a feature of comics?', ['Speech bubbles', 'Footnotes only', 'A table of contents only', 'No pictures'], 0)]),
M('Expanded Form: Writing Numbers by Place Value',
  'Grade 2 Math strand: expanded form shows a number broken apart by place value, such as writing 456 as 400 + 50 + 6.',
  [('What is 456 written in expanded form?', ['400 + 50 + 6', '4 + 5 + 6', '456 + 0', '45 + 6'], 0),
   ('What is 372 written in expanded form?', ['300 + 70 + 2', '3 + 7 + 2', '372 + 0', '37 + 2'], 0),
   ('What number does 200 + 30 + 5 represent?', ['235', '2035', '253', '325'], 0),
   ('What number does 600 + 40 + 1 represent?', ['641', '604', '461', '146'], 0),
   ('Expanded form helps us understand ___.', ['The value of each digit in a number', 'Only the first digit', 'Only the last digit', 'Nothing about the number'], 0)]),
Sc('Sound Waves: How Sound Travels Through Different Materials',
   'Grade 2 Science strand: sound travels as vibrations through materials like air, water, and solids, though it travels differently depending on the material.',
   [('What causes sound to travel?', ['Vibrations', 'Light', 'Colour', 'Temperature'], 0),
    ('Name one material sound can travel through.', ['Air', 'Outer space vacuum', 'Nothingness', 'A total void'], 0),
    ('Does sound need vibrations to travel?', ['Yes', 'No', 'Only in water', 'Only in space'], 0),
    ('Which of these best describes how sound moves?', ['As vibrations through a material', 'As a solid object', 'As a smell', 'As a colour'], 0),
    ('Sound generally cannot travel through ___.', ['Empty space with no matter', 'Air', 'Water', 'Solid walls'], 0)]),
SS('Canadian Astronauts and Space Achievements',
   'Grade 2 Social Studies strand: Canada has sent astronauts into space to conduct research and represent Canada on international space missions.',
   [('What is an astronaut?', ['A person who travels into space', 'A person who fixes cars', 'A person who teaches school', 'A person who bakes bread'], 0),
    ('Has Canada sent astronauts into space?', ['Yes', 'No', 'Only in movies', 'Canada has no astronauts'], 0),
    ('Why might a country be proud of its astronauts?', ['They represent the country and add to scientific research', 'They do nothing important', 'Space travel has no value', 'Astronauts never leave the ground'], 0),
    ('What might an astronaut do on a space mission?', ['Conduct scientific research', 'Sell products', 'Teach history only', 'Grow crops on Earth'], 0),
    ('Canadian achievements in space help show ___.', ['That Canada contributes to science and exploration', 'That Canada has no scientists', 'That space travel is impossible', 'Nothing important'], 0)]),
]),
day(115, [
L('Oral Language: Sharing Ideas in a Discussion',
  'Grade 2 Language strand: strong oral communication involves speaking clearly, listening to others, taking turns, and building on the ideas of classmates during a discussion.',
  [('What is one important part of a good discussion?', ['Listening to others', 'Talking over everyone', 'Ignoring classmates', 'Never sharing ideas'], 0),
   ('Why should you take turns speaking in a discussion?', ['So everyone gets a chance to share ideas', 'So only one person ever talks', 'Turns are not important', 'To confuse the group'], 0),
   ('What does it mean to build on someone elses idea?', ['Adding to or expanding what they said', 'Ignoring what they said', 'Repeating it exactly', 'Arguing without listening'], 0),
   ('Which is a respectful way to disagree in a discussion?', ['Explaining your thinking politely', 'Yelling at others', 'Refusing to listen', 'Walking away'], 0),
   ('Good oral communication includes speaking ___.', ['Clearly and respectfully', 'As loudly as possible', 'Only when forced', 'Without listening to others'], 0)]),
M('Multiplying by Multiples of Ten',
  'Grade 2 Math strand: multiplying a number by a multiple of ten, like 3 x 20, can be solved by multiplying the basic fact and then adding a zero.',
  [('What is 3 x 20?', ['60', '23', '6', '600'], 0),
   ('What is 4 x 30?', ['120', '34', '43', '12'], 0),
   ('What is 5 x 40?', ['200', '45', '54', '20'], 0),
   ('What is 2 x 60?', ['120', '62', '26', '12'], 0),
   ('To find 6 x 20, you can first solve 6 x 2, then ___.', ['Add a zero to the answer', 'Subtract a zero', 'Multiply by zero', 'Ignore the tens'], 0)]),
Sc('Birds of Prey: Owls, Hawks, and Eagles',
   'Grade 2 Science strand: birds of prey, such as owls, hawks, and eagles, are skilled hunters with sharp talons, strong beaks, and excellent eyesight.',
   [('Name a bird of prey.', ['Owl', 'Hawk', 'Eagle']),
    ('What body part helps birds of prey grab their food?', ['Sharp talons', 'talons']),
    ('What sense is especially strong in birds of prey?', ['excellent eyesight', 'eyesight'])] if False else
   [('Which of these is a bird of prey?', ['Eagle', 'Chicken', 'Duck', 'Penguin'], 0),
    ('What body part helps a bird of prey grab its food?', ['Sharp talons', 'Webbed feet', 'A long tail', 'Soft fur'], 0),
    ('Which sense is especially sharp in birds of prey?', ['Eyesight', 'Smell', 'Taste', 'Touch'], 0),
    ('Why do birds of prey need a strong, hooked beak?', ['To tear apart food', 'To swim faster', 'To build large nests only', 'To sing loudly'], 0),
    ('Owls are birds of prey that hunt mostly ___.', ['At night', 'Underwater', 'Only in winter', 'Never'], 0)]),
SS('Canadian Weather Records: Hottest, Coldest, and Snowiest Places',
   'Grade 2 Social Studies strand: different regions of Canada hold weather records, such as the coldest recorded temperature or the snowiest city, showing how varied Canadian climate can be.',
   [('Does all of Canada have the same weather?', ['No', 'Yes', 'Weather does not exist in Canada', 'Only one city has weather'], 0),
    ('What might a weather record show?', ['The coldest or snowiest place recorded', 'A type of food', 'A famous painting', 'A type of animal'], 0),
    ('Why does Canada have such varied weather records?', ['Canada is a very large country with many regions', 'Canada is very small', 'Weather never changes anywhere', 'Canada has only one climate'], 0),
    ('Which part of Canada is often known for extremely cold winters?', ['The far north', 'The equator', 'Only cities near the ocean', 'Nowhere in Canada'], 0),
    ('Learning about weather records helps us understand ___.', ['How diverse Canadas geography and climate are', 'Nothing about Canada', 'That Canada has no weather', 'Only one type of weather exists'], 0)]),
]),
day(116, [
L('Peer Editing: Giving Helpful Feedback on Writing',
  'Grade 2 Language strand: peer editing means reading a classmates writing and giving kind, helpful suggestions to make it clearer or stronger.',
  [('What is peer editing?', ['Giving helpful feedback on a classmates writing', 'Ignoring a classmates writing', 'Copying a classmates writing', 'Erasing a classmates writing'], 0),
   ('Why should feedback during peer editing be kind?', ['So it helps the writer improve without feeling bad', 'Kindness does not matter', 'To make the writer upset', 'Feedback should always be harsh'], 0),
   ('Which is an example of helpful peer editing feedback?', ['This part is confusing, can you explain more?', 'Your writing is bad.', 'I will not read this.', 'This makes no sense at all.'], 0),
   ('What is one goal of peer editing?', ['To help make writing clearer and stronger', 'To criticize without helping', 'To rewrite the whole piece yourself', 'To ignore the writer completely'], 0),
   ('When receiving peer feedback, a writer should ___.', ['Listen and consider the suggestions', 'Ignore all feedback', 'Get upset and stop writing', 'Argue with every comment'], 0)]),
M('Finding the Range of a Data Set',
  'Grade 2 Math strand: the range of a data set is the difference between the largest and smallest values, found by subtracting the smallest from the largest.',
  [('What is the range of the data set 3, 7, 9, 2?', ['7', '9', '2', '5'], 1),
   ('How do you find the range of a data set?', ['Subtract the smallest value from the largest', 'Add all the values', 'Multiply the values', 'Count the values'], 0),
   ('What is the range of the data set 10, 15, 20, 5?', ['15', '10', '20', '5'], 0),
   ('What is the range of the data set 4, 4, 4, 4?', ['0', '4', '8', '16'], 0),
   ('The range tells us about the ___ of a data set.', ['Spread between highest and lowest values', 'Average value', 'Most common value', 'Total number of values'], 0)]),
Sc('Plant Defenses: Thorns, Poison, and Bad Smells',
   'Grade 2 Science strand: many plants have special defenses, such as sharp thorns, poisonous parts, or bad smells, that help protect them from being eaten by animals.',
   [('Name one way a plant might defend itself.', ['Thorns', 'Poison', 'Bad smell']),
    ('Why do plants develop defenses?', ['to protect themselves from being eaten', 'so animals leave them alone']),
    ('Are all plant defenses the same?', ['no', 'no they vary'])] if False else
   [('Which of these is a plant defense?', ['Sharp thorns', 'Bright petals only', 'Soft leaves only', 'Tall height only'], 0),
    ('Why might a plant produce a bad smell?', ['To keep animals from eating it', 'To attract more rain', 'To grow faster', 'For no reason'], 0),
    ('What is one purpose of a plants defenses?', ['To protect it from being eaten', 'To help it grow taller', 'To change its colour', 'To make more seeds instantly'], 0),
    ('Which plant part often has thorns for protection?', ['The stem', 'The root only', 'The flower petal only', 'The seed only'], 0),
    ('Some plants are poisonous mainly to ___.', ['Discourage animals from eating them', 'Help animals grow', 'Attract more predators', 'Make themselves weaker'], 0)]),
SS('The Role of a Census: Counting Everyone in Canada',
   'Grade 2 Social Studies strand: a census is an official count of everyone living in a country, helping the government plan services like schools, hospitals, and roads.',
   [('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A weather report'], 0),
    ('Why does the government take a census?', ['To help plan services like schools and hospitals', 'To sell products', 'To have no reason', 'To confuse citizens'], 0),
    ('How often is a census usually taken?', ['At regular intervals, such as every few years', 'Every single day', 'Only once ever', 'Never'], 0),
    ('Which service might benefit from census information?', ['Planning new schools', 'Making candy', 'Painting a fence', 'Playing a game'], 0),
    ('A census helps a government understand ___.', ['How many people live in different areas', 'The weather forecast', 'Sports scores', 'Movie ratings'], 0)]),
]),
day(117, [
L('Story Sequels: Imagining What Happens Next',
  'Grade 2 Language strand: a sequel continues the story after the original ending, and writers use what they know about the characters and setting to imagine new events.',
  [('What is a sequel?', ['A story that continues after the original', 'The very first story', 'A story with no characters', 'A dictionary'], 0),
   ('What should a writer consider when writing a sequel?', ['The characters and setting from the original story', 'Nothing from the original', 'Only new characters', 'A different language'], 0),
   ('Why might a reader enjoy a sequel?', ['To find out what happens to characters they liked', 'Sequels are always boring', 'Sequels ignore the original story', 'Sequels have no connection to the first story'], 0),
   ('A sequel usually takes place ___ the events of the original story.', ['After', 'Before', 'During the exact same moment', 'In a completely unrelated book'], 0),
   ('Which is an example of writing a sequel?', ['Imagining what a character does the next day', 'Copying the same story exactly', 'Ignoring the characters completely', 'Writing about a math problem'], 0)]),
M('Estimating Quotients: Rounding Before Dividing',
  'Grade 2 Math strand: to estimate a quotient, students round the numbers involved to make the division easier before finding an approximate answer.',
  [('To estimate 42 divided by 7, you could round 42 to ___.', ['40', '42', '50', '100'], 0),
   ('Estimating a quotient means finding ___.', ['An approximate answer to a division problem', 'The exact answer only', 'The largest possible number', 'A completely unrelated number'], 0),
   ('About what is 29 divided by 5, rounded first?', ['About 6', 'About 60', 'About 600', 'About 0.6'], 0),
   ('About what is 61 divided by 10?', ['About 6', 'About 60', 'About 16', 'About 600'], 0),
   ('Why do we estimate before dividing exactly?', ['To quickly check if our exact answer seems reasonable', 'Estimating replaces the need to divide at all', 'It makes math harder', 'It has no purpose'], 0)]),
Sc('Coral Reefs: A Colourful Underwater Habitat',
   'Grade 2 Science strand: coral reefs are colourful ocean habitats built by tiny living creatures called coral polyps, and they provide homes for many kinds of fish and sea animals.',
   [('What builds a coral reef?', ['Tiny living creatures called coral polyps', 'Fish', 'Rocks alone', 'Seaweed alone'], 0),
    ('Where are coral reefs found?', ['In the ocean', 'In deserts', 'In forests', 'On mountains'], 0),
    ('What lives among the coral in a reef?', ['Many fish and sea animals', 'Only birds', 'Only insects', 'Nothing lives there'], 0),
    ('Why are coral reefs considered important habitats?', ['They provide homes for a huge variety of sea life', 'They are empty and unimportant', 'They only exist on land', 'They harm ocean life'], 0),
    ('Coral reefs are known for being especially ___.', ['Colourful and full of life', 'Grey and lifeless', 'Located only in deserts', 'Made of plastic'], 0)]),
SS('Time Capsules: Preserving Memories for the Future',
   'Grade 2 Social Studies strand: a time capsule is a container filled with objects and messages that is sealed and opened many years later, helping future generations learn about the past.',
   [('What is a time capsule?', ['A sealed container of objects opened later', 'A type of clock', 'A kind of vehicle', 'A weather tool'], 0),
    ('Why do people create time capsules?', ['To help future generations learn about the past', 'To throw things away', 'To confuse people', 'For no reason'], 0),
    ('What might someone put inside a time capsule?', ['Photos, letters, or small objects', 'Nothing at all', 'Only garbage', 'Only liquids'], 0),
    ('When is a time capsule usually opened?', ['Many years after it was sealed', 'The very next day', 'It is never opened', 'Before it is sealed'], 0),
    ('A time capsule helps connect ___.', ['The past to the future', 'Only two friends', 'Different countries oceans apart', 'Nothing important'], 0)]),
]),
day(118, [
L('Word Origins: Where Some English Words Come From',
  'Grade 2 Language strand: many English words originally came from other languages, and learning simple word origins can help readers understand and remember new vocabulary.',
  [('Do all English words come only from English?', ['No, many come from other languages', 'Yes, always', 'Words have no origin', 'English has no history'], 0),
   ('Why might learning about word origins be helpful?', ['It can help us understand and remember new words', 'It makes words harder to learn', 'It has no benefit', 'It changes the spelling randomly'], 0),
   ('What do we call the study of where words come from?', ['Word origin study', 'Word origin study, sometimes called etymology', 'Punctuation', 'Grammar'], 1),
   ('Learning word origins is part of building strong ___.', ['Vocabulary', 'Math skills', 'Athletic skills', 'Art skills'], 0),
   ('Which is an example of curiosity about word origins?', ['Asking where the word school first came from', 'Ignoring new words completely', 'Refusing to learn vocabulary', 'Avoiding reading'], 0)]),
M('Multi-Step Word Problems: Multiplication and Addition Together',
  'Grade 2 Math strand: some word problems require more than one step, such as multiplying to find a total and then adding another amount to solve the problem.',
  [('If you buy 3 bags of 4 apples, then get 2 more apples, how many apples in all?', ['12', '13', '14', '10'], 1),
   ('If there are 5 rows of 2 chairs, then 3 more chairs are added, how many chairs total?', ['10', '11', '12', '13'], 3),
   ('A multi-step problem requires you to ___.', ['Solve more than one operation to find the answer', 'Only add numbers', 'Only look at the first number', 'Skip a step'], 0),
   ('If 4 boxes have 6 toys each, then 5 toys are added, how many toys in total?', ['24', '25', '29', '30'], 2),
   ('When solving a multi-step problem, it helps to ___.', ['Solve one step at a time in order', 'Skip straight to the final answer', 'Ignore some of the numbers', 'Guess randomly'], 0)]),
Sc('Bees and Their Hives: Working Together in a Colony',
   'Grade 2 Science strand: bees live together in large groups called colonies inside a hive, where each bee has a job that helps the whole group survive.',
   [('What do we call a large group of bees living together?', ['A colony', 'A pack', 'A herd', 'A flock'], 0),
    ('Where do bees in a colony live?', ['In a hive', 'In a nest', 'In a burrow', 'In a den'], 0),
    ('Do all bees in a hive have the same job?', ['No, different bees have different jobs', 'Yes, they all do the exact same thing', 'Bees do not have jobs', 'Only one bee works'], 0),
    ('Why is teamwork important in a bee colony?', ['It helps the whole group survive', 'Teamwork does not matter to bees', 'Bees work completely alone', 'It has no purpose'], 0),
    ('Which of these might be a job of a worker bee?', ['Collecting nectar', 'Driving a car', 'Reading a book', 'Building a house for people'], 0)]),
SS('Sister Cities: Twin Communities Around the World',
   'Grade 2 Social Studies strand: sister cities are communities in different countries that form a special partnership to share culture, ideas, and friendship.',
   [('What is a sister city?', ['A partner community in another country', 'A city with no people', 'A type of building', 'A kind of holiday'], 0),
    ('Why might two cities become sister cities?', ['To share culture, ideas, and friendship', 'To compete against each other', 'To ignore one another', 'To close their borders'], 0),
    ('What might sister cities share with each other?', ['Cultural events and ideas', 'Nothing at all', 'Only complaints', 'Weather patterns only'], 0),
    ('Is a sister city partnership an example of global friendship?', ['Yes', 'No', 'Only if in the same country', 'It has no purpose'], 0),
    ('Sister city partnerships can help people learn about ___.', ['Other cultures and communities', 'Only their own city', 'Nothing new', 'Weather forecasting'], 0)]),
]),
day(119, [
L('List Poems: Writing Poetry Without Rhyme',
  'Grade 2 Language strand: a list poem is a simple form of poetry that lists ideas, things, or feelings related to a topic, without needing to rhyme.',
  [('Does a list poem need to rhyme?', ['No', 'Yes, always', 'Only sometimes required', 'Rhyme is the only rule'], 0),
   ('What does a list poem usually do?', ['Lists ideas or things related to a topic', 'Tells a long complicated story', 'Uses only numbers', 'Has no topic at all'], 0),
   ('Why might a list poem be a good choice for a beginner poet?', ['It does not require rhyming, making it simpler to write', 'It is the hardest form of poetry', 'It requires perfect rhyme', 'It has strict rules about length'], 0),
   ('Which is an example of a list poem topic?', ['Things I love about summer', 'A math equation', 'A grocery receipt', 'A phone number'], 0),
   ('A list poem is a type of ___.', ['Poetry', 'Math problem', 'Science experiment', 'Map'], 0)]),
M('3D Shapes: Nets and Unfolding',
  'Grade 2 Math strand: a net is a flat pattern that can be folded to make a 3D shape, such as unfolding a cube into six connected squares.',
  [('What is a net in geometry?', ['A flat pattern that folds into a 3D shape', 'A tool for catching fish', 'A type of graph', 'A kind of clock'], 0),
   ('How many squares make up the net of a cube?', ['Four', 'Five', 'Six', 'Eight'], 2),
   ('What 3D shape can a net of six squares fold into?', ['A cube', 'A sphere', 'A cone', 'A cylinder'], 0),
   ('When you fold a net, what do you create?', ['A 3D shape', 'A 2D shape', 'A number line', 'A graph'], 0),
   ('Understanding nets helps us see how ___ relate to 3D shapes.', ['2D flat shapes', 'Colours', 'Sounds', 'Smells'], 0)]),
Sc('Comparing Animal Senses: Who Sees, Hears, or Smells Best?',
   'Grade 2 Science strand: different animals have different strong senses -- some see very well, some hear extremely well, and some have an excellent sense of smell.',
   [('Name an animal known for excellent eyesight.', ['An eagle', 'A hawk']),
    ('Name an animal known for excellent smell.', ['A dog', 'A bear']),
    ('Do all animals have the same strongest sense?', ['no', 'no different animals'])] if False else
   [('Which animal is known for excellent eyesight?', ['An eagle', 'A worm', 'A snail', 'A jellyfish'], 0),
    ('Which animal is known for having an excellent sense of smell?', ['A dog', 'A butterfly', 'A fish', 'A frog'], 0),
    ('Do all animals rely most on the same sense?', ['No, different animals rely on different strong senses', 'Yes, all animals are identical', 'Animals have no senses', 'Only humans have senses'], 0),
    ('Why might a bat rely heavily on hearing instead of sight?', ['It often navigates in the dark', 'Bats cannot hear at all', 'Bats never move', 'Hearing is not useful to bats'], 0),
    ('Comparing animal senses helps scientists understand ___.', ['How animals are adapted to their environment', 'Nothing important', 'That all animals are the same', 'That senses do not matter'], 0)]),
SS('Public Signs and Symbols: Reading the World Around Us',
   'Grade 2 Social Studies strand: public signs use symbols and simple pictures, such as a red octagon for stop or a wheelchair icon for accessibility, to communicate quickly across different languages.',
   [('What shape is a stop sign?', ['An octagon', 'A circle', 'A square', 'A triangle'], 0),
    ('Why do public signs often use symbols instead of only words?', ['Symbols can be understood quickly across languages', 'Words are always better', 'Symbols have no meaning', 'Signs never need symbols'], 0),
    ('What does a wheelchair symbol on a sign usually indicate?', ['An accessible entrance or space', 'A parking fee', 'A type of food', 'A weather warning'], 0),
    ('Why is it useful to recognize common public signs?', ['It helps keep us safe and informed', 'Signs are never useful', 'Only adults need to know signs', 'Signs have no purpose'], 0),
    ('Which colour is often used on signs to warn of danger?', ['Red', 'Pink', 'Light blue', 'Beige'], 0)]),
]),
day(120, [
L('Language Review: Apostrophes, Connections, and Word Study',
  'Grade 2 Language strand review: students revisit apostrophes in contractions and possessives, syllable division, text-to-text and text-to-world connections, peer editing, and word origins.',
  [('In dont, why is an apostrophe used?', ['To join two words into one', 'It shows a contraction is being made', 'To end a sentence', 'It has no purpose'], 1),
   ('What does text-to-text mean?', ['Connecting one text to another text', 'Connecting a text to your own life', 'Ignoring the text', 'Reading only one book'], 0),
   ('What is peer editing?', ['Giving helpful feedback on a classmates writing', 'Ignoring a classmates writing', 'Copying a classmates writing', 'Erasing a classmates writing'], 0),
   ('How many syllables are in the word butterfly?', ['One', 'Two', 'Three', 'Four'], 2),
   ('Why might learning about word origins be helpful?', ['It can help us understand and remember new words', 'It makes words harder to learn', 'It has no benefit', 'It changes the spelling randomly'], 0)]),
M('Math Review: Multiplication, Place Value, and Data',
  'Grade 2 Math strand review: students revisit multiplication facts to 12, two-digit multiplication, expanded form, multiples of ten, data range, and 3D shape nets.',
  [('What is 11 x 5?', ['50', '55', '60', '45'], 1),
   ('What is 12 x 4?', ['46', '48', '50', '44'], 1),
   ('What is 456 written in expanded form?', ['400 + 50 + 6', '4 + 5 + 6', '456 + 0', '45 + 6'], 0),
   ('What is 3 x 20?', ['60', '23', '6', '600'], 0),
   ('What is the range of the data set 3, 7, 9, 2?', ['7', '9', '2', '5'], 1)]),
Sc('Science Review: Environment, Sound, and Living Things',
   'Grade 2 Science strand review: students revisit water conservation, composting, sound waves, birds of prey, plant defenses, coral reefs, bee colonies, and comparing animal senses.',
   [('What does water conservation mean?', ['Using water carefully and not wasting it', 'Using as much water as possible', 'Never using water', 'Wasting water on purpose'], 0),
    ('What causes sound to travel?', ['Vibrations', 'Light', 'Colour', 'Temperature'], 0),
    ('Which of these is a bird of prey?', ['Eagle', 'Chicken', 'Duck', 'Penguin'], 0),
    ('What builds a coral reef?', ['Tiny living creatures called coral polyps', 'Fish', 'Rocks alone', 'Seaweed alone'], 0),
    ('What do we call a large group of bees living together?', ['A colony', 'A pack', 'A herd', 'A flock'], 0)]),
SS('Social Studies Review: History, Government, and Community',
   'Grade 2 Social Studies strand review: students revisit the War of 1812, the justice system, Canadian astronauts, the census, time capsules, and public signs.',
   [('Who fought in the War of 1812?', ['The United States and British North America', 'France and Spain', 'Canada and Mexico', 'No one, it never happened'], 0),
    ('Who makes decisions in a courtroom?', ['A judge', 'A mayor', 'A teacher', 'A doctor'], 0),
    ('What is a census?', ['An official count of everyone in a country', 'A type of holiday', 'A kind of map', 'A weather report'], 0),
    ('What is a time capsule?', ['A sealed container of objects opened later', 'A type of clock', 'A kind of vehicle', 'A weather tool'], 0),
    ('What shape is a stop sign?', ['An octagon', 'A circle', 'A square', 'A triangle'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_111_120)
    append_to(2, g2_111_120)
