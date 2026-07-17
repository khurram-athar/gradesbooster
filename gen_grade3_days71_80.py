#!/usr/bin/env python3
"""Phase 3 extension: Grade 3, Days 71-80 (pushes Grade 3 from 70 to 80
days, continuing toward the full 157-day year). Topics chosen to avoid
any overlap with the existing Day 1-70 set (see data/grade3.json):
similes and metaphors, the four sentence types, multiple-meaning words,
comic strips, flashbacks, commas in a series, root words, giving clear
directions, onomatopoeia, multiplying three factors, estimating
quotients, classifying triangles, input-output tables, analog/digital
clocks, probability experiments, the distributive property, Venn
diagrams, needs vs wants, butterfly metamorphosis, nocturnal/diurnal
animals, fossils, volcanoes and earthquakes, decomposers, insect body
parts, Earth's magnetic field, severe weather safety, plant
adaptations, laws and bylaws, taxes, mining and forestry, the Great
Lakes, local media, Francophone communities, treaties, Remembrance
Day, and tourism in Ontario.

Subject keys for Grade 3 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 3 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
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


g3_71_80 = [
day(71, [
L('Reading: Figurative Language — Similes and Metaphors',
  'Grade 3 Language strand: figurative language uses words in imaginative ways, and a simile compares two things using “like” or “as,” while a metaphor says one thing is another thing without using those words.',
  [('A simile compares two things using ___.', ['“Like” or “as”', 'Only exact numbers', 'A concept unrelated to comparing things', 'No comparison words at all'], 0),
   ('A metaphor says one thing is another thing ___.', ['Without using “like” or “as”', 'Only while using “like” or “as”', 'A concept unrelated to figurative language', 'While comparing numbers instead of ideas'], 0),
   ('Which sentence is an example of a simile?', ['Her smile was as bright as the sun.', 'Her smile was the sun.', 'A sentence with no comparison at all', 'Her smile was very nice today.'], 0),
   ('Why might a writer use a metaphor instead of stating a plain fact?', ['A metaphor can create a vivid picture in the reader’s mind that a plain fact cannot', 'Metaphors never add any meaning to writing', 'This concept has no connection to descriptive writing', 'A metaphor always makes writing harder to understand with no benefit'], 0),
   ('Why is it useful for readers to recognize similes and metaphors while reading a story?', ['It helps readers understand the vivid comparisons an author is making rather than taking them literally', 'Similes and metaphors never appear in stories written for children', 'Recognizing figurative language has no connection to understanding a story', 'A reader should always take every sentence in a story literally'], 0)]),
M('Multiplication: Multiplying Three Factors',
  'Grade 3 Math strand: when multiplying three numbers together, you can multiply any two of the factors first and then multiply that answer by the third factor, and the product will stay the same.',
  [('When multiplying three factors, you can multiply any two of them first and then multiply by ___.', ['The third factor', 'Only the largest factor, ignoring the others', 'A concept unrelated to multiplying three numbers', 'Zero, regardless of the actual factors'], 0),
   ('What is 2 × 3 × 4?', ['24', '9', '20', '12'], 0),
   ('What is 5 × 2 × 3?', ['30', '10', '15', '25'], 0),
   ('Why does multiplying (2 × 3) × 4 give the same answer as multiplying 2 × (3 × 4)?', ['Changing the grouping of the factors does not change the final product', 'Grouping factors differently always changes the final answer', 'This concept has no connection to how multiplication works', 'Only addition allows numbers to be grouped in different ways'], 0),
   ('If a classroom has 3 rows of desks, each row has 2 groups, and each group has 4 desks, how many desks are there in total?', ['24', '9', '14', '20'], 0)]),
Sc('Science: Life Cycle of a Butterfly: Metamorphosis',
   'Grade 3 Science strand: a butterfly goes through complete metamorphosis, changing from an egg to a larva (caterpillar), then to a pupa (chrysalis), and finally into an adult butterfly.',
   [('A butterfly goes through complete metamorphosis, changing from an egg to a larva, then to a pupa, and finally to ___.', ['An adult butterfly', 'A completely different insect species', 'A concept unrelated to a butterfly’s life cycle', 'Nothing at all, since the process stops at the pupa stage'], 0),
    ('The larva stage of a butterfly’s life cycle is also known as a ___.', ['Caterpillar', 'Chrysalis, which is the pupa stage instead', 'Concept unrelated to a butterfly’s life cycle', 'Adult butterfly, which is the final stage instead'], 0),
    ('Which is the correct order of a butterfly’s life cycle?', ['Egg, larva, pupa, adult', 'Adult, pupa, larva, egg', 'Pupa, egg, adult, larva', 'A random order with no set sequence at all'], 0),
    ('Why do scientists call a butterfly’s life cycle “complete metamorphosis”?', ['The insect’s body changes dramatically through four very different stages', 'The insect looks exactly the same during every stage of its life', 'This concept has no connection to how butterflies grow and change', 'Complete metamorphosis means the insect never changes at all'], 0),
    ('Why might the caterpillar stage be important for a butterfly’s growth?', ['The caterpillar eats large amounts of food to gain the energy needed for its later stages', 'The caterpillar stage has no connection to how a butterfly develops', 'Caterpillars never eat any food during this stage of life', 'This concept has no relevance to understanding insect life cycles'], 0)]),
SS('Social Studies: How Laws and Bylaws Keep Communities Safe',
   'Grade 3 Social Studies strand: laws are rules made by governments, and bylaws are rules made by a municipal government, both of which help keep people safe and communities running smoothly.',
   [('Bylaws are rules made by a ___ government.', ['Municipal', 'Provincial, with no connection to local rules', 'A concept unrelated to how communities are governed', 'Federal, with no connection to local community rules'], 0),
    ('Laws and bylaws both help keep ___ safe and communities running smoothly.', ['People', 'A concept unrelated to community safety', 'Only government buildings, with no connection to people', 'Nothing at all, since laws serve no real purpose'], 0),
    ('Which is an example of a municipal bylaw?', ['A rule about how loud noise can be late at night', 'A concept unrelated to local community rules', 'A rule that applies only to a different country', 'A rule with no connection to community life at all'], 0),
    ('Why might a community create a bylaw about keeping dogs on a leash in public parks?', ['It helps keep both people and pets safe while sharing public spaces', 'Bylaws about pets have no connection to community safety', 'Leash rules never affect how people use a public park', 'This concept has no relevance to understanding local government'], 0),
    ('Why do communities need laws and bylaws instead of letting everyone decide their own rules?', ['Shared rules help keep everyone safe and ensure the community works fairly for all its members', 'Laws and bylaws never actually apply to anyone in a community', 'Communities function better with absolutely no shared rules at all', 'This concept has no relevance to social studies learning'], 0)])]),

day(72, [
L('Grammar: The Four Types of Sentences',
  'Grade 3 Language strand: there are four types of sentences: a statement gives information, a question asks something, a command gives an instruction, and an exclamation shows strong feeling.',
  [('A statement is a sentence that ___.', ['Gives information', 'Always asks a question', 'A concept unrelated to types of sentences', 'Shows no meaning at all'], 0),
   ('A command is a sentence that ___.', ['Gives an instruction', 'Always shows strong feeling only', 'A concept unrelated to types of sentences', 'Only ever asks a question'], 0),
   ('Which sentence is an exclamation?', ['Watch out for that puddle!', 'Please pass the salt.', 'What time is it.', 'The sky is blue.'], 0),
   ('Why might a writer choose to end a sentence with an exclamation mark instead of a period?', ['An exclamation mark shows strong feeling or excitement that a period does not convey', 'An exclamation mark and a period always mean exactly the same thing', 'This concept has no connection to how sentences are punctuated', 'Exclamation marks are never used to show emotion in writing'], 0),
   ('Why is it useful to know the four types of sentences when writing a story with dialogue?', ['It helps a writer choose the right punctuation and tone for what a character is saying', 'The type of sentence used never affects how a story is written', 'A story can only ever use one single type of sentence throughout', 'This concept has no relevance to understanding grammar'], 0)]),
M('Division: Estimating Quotients',
  'Grade 3 Math strand: estimating a quotient means using rounding or friendly numbers to quickly find an approximate answer to a division problem before, or instead of, calculating the exact answer.',
  [('Estimating a quotient means using rounding or friendly numbers to find an ___ answer.', ['Approximate', 'Exact, with no rounding involved at all', 'A concept unrelated to solving division problems', 'Completely random, with no connection to the original numbers'], 0),
   ('To estimate 41 ÷ 5, which friendly number could 41 be rounded to?', ['40', '41', '5', '45'], 0),
   ('What is a reasonable estimate for 62 ÷ 8?', ['About 8', 'About 80', 'About 800', 'About 2'], 0),
   ('Why might someone estimate a quotient before solving a division problem exactly?', ['An estimate helps check that the final answer is reasonable', 'Estimating a quotient never helps with checking division', 'This concept has no connection to solving division problems', 'An estimate is always the same as the exact answer'], 0),
   ('Why is it helpful to round to a friendly number, like 40 instead of 41, when estimating a quotient?', ['Friendly numbers are easier to divide mentally, making the estimate quicker to find', 'Rounding to a friendly number never makes a calculation easier', 'This concept has no relevance to solving division problems', 'Friendly numbers always change the actual value being divided'], 0)]),
Sc('Science: Nocturnal vs Diurnal Animals',
   'Grade 3 Science strand: nocturnal animals, like owls and bats, are active mainly at night, while diurnal animals, like squirrels and robins, are active mainly during the day.',
   [('Nocturnal animals are active mainly ___.', ['At night', 'During the day, with no connection to nighttime', 'A concept unrelated to when animals are active', 'Only underwater, with no connection to time of day'], 0),
    ('Diurnal animals are active mainly ___.', ['During the day', 'At night, with no connection to daytime activity', 'A concept unrelated to when animals are active', 'Only while hibernating, with no daytime activity'], 0),
    ('Which animal is typically nocturnal?', ['An owl', 'A robin, which is typically diurnal', 'A squirrel, which is typically diurnal', 'A concept unrelated to animal activity patterns'], 0),
    ('Why might an owl’s excellent night vision help it as a nocturnal hunter?', ['It allows the owl to see and catch prey clearly even in low light', 'Night vision has no connection to how an owl hunts', 'Owls never actually hunt for food at any time', 'This concept has no relevance to understanding nocturnal animals'], 0),
    ('Why might being active at different times of day help nocturnal and diurnal animals share the same habitat?', ['Being active at different times can reduce competition for food and space between the two groups', 'Nocturnal and diurnal animals are never found in the same habitat', 'The time an animal is active has no connection to sharing a habitat', 'This concept has no relevance to understanding animal behaviour'], 0)]),
SS('Social Studies: Taxes: How Communities Pay for Shared Services',
   'Grade 3 Social Studies strand: taxes are money that people and businesses pay to the government, which uses that money to pay for shared services like schools, roads, and libraries.',
   [('Taxes are money that people and businesses pay to the ___.', ['Government', 'A concept unrelated to funding shared services', 'Only a single private company, with no public purpose', 'Nothing at all, since taxes serve no real purpose'], 0),
    ('Governments use tax money to pay for shared services like schools, roads, and ___.', ['Libraries', 'A concept unrelated to community services', 'Only private vacations for government workers', 'Nothing useful at all, since taxes provide no benefit'], 0),
    ('Which is an example of a service that tax money often helps pay for?', ['A public library', 'A concept unrelated to shared community services', 'A private toy that only one family owns', 'An item unrelated to how communities are funded'], 0),
    ('Why might a community be unable to keep its parks and libraries running without collecting taxes?', ['These shared services need ongoing funding, and taxes are a main way governments raise that money', 'Taxes have no connection to how public services are funded', 'Parks and libraries never actually require any money to operate', 'This concept has no relevance to understanding community government'], 0),
    ('Why might people see taxes as an important part of living in a community, even though they must give up some money?', ['Taxes fund shared services that benefit the whole community, including the people who pay them', 'Taxes never provide any benefit to the people who pay them', 'This concept has no connection to understanding how communities function', 'Shared community services could exist with no funding at all'], 0)])]),

day(73, [
L('Vocabulary: Multiple-Meaning Words',
  'Grade 3 Language strand: a multiple-meaning word is a single word that has more than one meaning, such as “bat,” which can mean a flying animal or equipment used to hit a ball.',
  [('A multiple-meaning word is a single word that has ___.', ['More than one meaning', 'Only one meaning that never changes', 'A concept unrelated to how words work', 'No meaning at all, regardless of context'], 0),
   ('The word “bat” can mean a flying animal or ___.', ['Equipment used to hit a ball', 'A concept unrelated to the word “bat”', 'A type of vegetable grown in a garden', 'A word unrelated to any of “bat”’s real meanings'], 0),
   ('Which sentence uses the word “bank” to mean the side of a river?', ['We sat on the bank and watched the water flow.', 'She put her money in the bank.', 'A sentence unrelated to either meaning of “bank”', 'The plane will bank sharply to the left.'], 0),
   ('Why is it helpful to look at the rest of a sentence when you find a multiple-meaning word?', ['The surrounding words can show which specific meaning is being used', 'The rest of a sentence never helps determine a word’s meaning', 'Multiple-meaning words never actually appear in real sentences', 'This concept has no connection to understanding vocabulary'], 0),
   ('Why might multiple-meaning words sometimes make a sentence tricky to understand at first?', ['A reader has to think about context to determine which meaning of the word is being used', 'Multiple-meaning words always have only one possible interpretation', 'Context never has any effect on understanding a multiple-meaning word', 'This concept has no relevance to reading comprehension'], 0)]),
M('Geometry: Classifying Triangles by Side Length',
  'Grade 3 Math strand: triangles can be classified by their side lengths as equilateral, with three equal sides, isosceles, with two equal sides, or scalene, with no equal sides.',
  [('A triangle with three equal sides is called ___.', ['Equilateral', 'Isosceles, which has only two equal sides', 'A concept unrelated to classifying triangles', 'Scalene, which has no equal sides at all'], 0),
   ('A triangle with two equal sides is called ___.', ['Isosceles', 'Equilateral, which has three equal sides', 'A concept unrelated to classifying triangles', 'Scalene, which has no equal sides at all'], 0),
   ('A triangle with no equal sides is called ___.', ['Scalene', 'Equilateral, which has three equal sides', 'Isosceles, which has two equal sides', 'A concept unrelated to classifying triangles'], 0),
   ('Why might measuring the sides of a triangle help you classify it correctly?', ['Comparing the side lengths shows exactly how many sides are equal, which determines the triangle’s type', 'Measuring the sides of a triangle never helps classify its type', 'A triangle’s side lengths have no connection to how it is classified', 'This concept has no relevance to understanding geometry'], 0),
   ('If a triangle has sides measuring 5 cm, 5 cm, and 5 cm, how would it be classified?', ['Equilateral', 'Isosceles', 'Scalene', 'A concept unrelated to classifying triangles'], 0)]),
Sc('Science: Fossils: Clues to the Past',
   'Grade 3 Science strand: a fossil is the preserved remains or trace of a living thing from long ago, and scientists study fossils to learn what plants and animals were like in the distant past.',
   [('A fossil is the preserved remains or trace of a living thing from ___.', ['Long ago', 'Only the present day, with no connection to the past', 'A concept unrelated to Earth’s history', 'The near future, with no connection to past living things'], 0),
    ('Scientists study fossils to learn what plants and animals were like ___.', ['In the distant past', 'Only in the present moment, with no connection to history', 'A concept unrelated to studying living things', 'On a completely different planet'], 0),
    ('Which is an example of something that could become a fossil?', ['An animal’s bones preserved in rock over a very long time', 'A concept unrelated to how fossils form', 'A living animal that is walking around today', 'An object that has never existed in any form'], 0),
    ('Why are fossils useful to scientists studying life from millions of years ago, like dinosaurs?', ['Fossils provide physical evidence of what these ancient living things looked like and how they may have lived', 'Fossils provide no useful information about ancient living things', 'Scientists never study fossils to learn about the past', 'This concept has no relevance to understanding Earth’s history'], 0),
    ('Why might it take a very long time for a fossil to form?', ['The process usually involves remains being slowly buried and replaced by minerals over thousands of years', 'Fossils always form within just a few minutes', 'The formation of a fossil has no connection to time at all', 'This concept has no relevance to understanding how fossils are created'], 0)]),
SS('Social Studies: Ontario’s Mining and Forestry Industries',
   'Grade 3 Social Studies strand: mining and forestry are important industries in Ontario, providing minerals like nickel and gold, and wood products, that support jobs and the province’s economy.',
   [('Mining and forestry are important industries in Ontario that support jobs and the province’s ___.', ['Economy', 'A concept unrelated to how industries support Ontario', 'Weather patterns, with no connection to industries', 'Population of animals, with no connection to industry'], 0),
    ('Mining in Ontario provides minerals such as nickel and ___.', ['Gold', 'A concept unrelated to minerals found through mining', 'Only water, which is not a mined mineral', 'Nothing useful at all, since mining provides no resources'], 0),
    ('Which is an example of a product that comes from Ontario’s forestry industry?', ['Wood used to build furniture', 'A concept unrelated to forestry products', 'A mineral dug from underground mines', 'An item unrelated to trees or forests'], 0),
    ('Why might mining and forestry be especially important industries in northern parts of Ontario?', ['These regions often have large forests and mineral deposits that support jobs and local economies', 'Mining and forestry have no connection to northern Ontario’s landscape', 'These industries never provide any jobs to communities in Ontario', 'This concept has no relevance to understanding Ontario’s economy'], 0),
    ('Why might communities need to balance mining and forestry activities with protecting the environment?', ['These industries can affect forests and land, so careful planning helps protect natural resources for the future', 'Mining and forestry never have any effect on the environment', 'Protecting the environment has no connection to how industries operate', 'This concept has no relevance to understanding Ontario’s resources'], 0)])]),

day(74, [
L('Writing: Writing a Comic Strip',
  'Grade 3 Language strand: a comic strip tells a story using a sequence of small pictures called panels, often combined with short dialogue in speech bubbles to show what characters are saying.',
  [('A comic strip tells a story using a sequence of small pictures called ___.', ['Panels', 'Chapters, with no connection to pictures', 'A concept unrelated to how a comic strip is organized', 'Paragraphs, with no connection to a comic strip’s format'], 0),
   ('In a comic strip, short dialogue is often shown inside a ___.', ['Speech bubble', 'A concept unrelated to how dialogue is shown', 'A footnote at the bottom of the page', 'A completely blank panel with no words at all'], 0),
   ('Which is an important part of planning a comic strip before drawing it?', ['Deciding what happens in each panel of the story', 'A concept unrelated to planning a comic strip', 'Skipping the story completely and drawing randomly', 'Ignoring the order in which events happen'], 0),
   ('Why might a comic strip use pictures along with words to tell its story?', ['Pictures can show actions, expressions, and settings quickly, working together with the words', 'Pictures never add any meaning to a comic strip’s story', 'A comic strip can only ever use words, with no pictures allowed', 'This concept has no connection to how comic strips are created'], 0),
   ('Why is it important for the panels in a comic strip to be arranged in a clear order?', ['A clear order helps the reader understand how the story’s events unfold from beginning to end', 'The order of panels never affects how a comic strip’s story is understood', 'A comic strip’s panels can be arranged in any random order with no effect', 'This concept has no relevance to writing a comic strip'], 0)]),
M('Patterning: Input-Output Tables',
  'Grade 3 Math strand: an input-output table shows a set of starting numbers, called inputs, and the numbers you get after applying the same rule to each one, called outputs.',
  [('An input-output table shows starting numbers, called inputs, and the numbers you get after applying the same rule, called ___.', ['Outputs', 'A concept unrelated to how the table works', 'Remainders, with no connection to input-output tables', 'Factors, with no connection to applying a rule'], 0),
   ('If the rule is “add 3” and the input is 5, what is the output?', ['8', '5', '3', '15'], 0),
   ('If the rule is “multiply by 2” and the input is 6, what is the output?', ['12', '6', '3', '8'], 0),
   ('Why must the same rule be applied to every input in an input-output table?', ['Using the same rule keeps the pattern between the inputs and outputs consistent', 'Changing the rule for each input never affects the table’s pattern', 'An input-output table never actually follows any specific rule', 'This concept has no connection to understanding number patterns'], 0),
   ('If an input-output table shows inputs of 2, 4, and 6 producing outputs of 4, 8, and 12, what rule is being used?', ['Multiply by 2', 'Add 2', 'Divide by 2', 'Subtract 2'], 0)]),
Sc('Science: Volcanoes and Earthquakes',
   'Grade 3 Science strand: volcanoes and earthquakes are powerful events caused by movements deep within the Earth, and studying them helps scientists understand how the Earth’s surface can change quickly.',
   [('Volcanoes and earthquakes are powerful events caused by movements deep within the ___.', ['Earth', 'Ocean, with no connection to the Earth’s interior', 'A concept unrelated to how these events occur', 'Sky, with no connection to the ground shifting'], 0),
    ('A volcano is an opening in the Earth’s surface through which melted rock, called ___, can escape.', ['Lava', 'A concept unrelated to how volcanoes work', 'Ice, which is not connected to volcanic eruptions', 'Sand, which is not connected to volcanic eruptions'], 0),
    ('Which is an example of what might happen during an earthquake?', ['The ground shakes suddenly', 'A concept unrelated to earthquakes', 'The weather instantly becomes sunny', 'Nothing at all happens to the ground'], 0),
    ('Why do scientists study volcanoes and earthquakes, even though these events can be dangerous?', ['Understanding these events can help predict them and keep people safer when they occur', 'Studying volcanoes and earthquakes provides no useful information at all', 'These events never actually pose any danger to people', 'This concept has no relevance to understanding the Earth'], 0),
    ('Why might scientists say that volcanoes and earthquakes show that the Earth’s surface is always changing?', ['These events reveal that forces beneath the surface can reshape the land, even though the changes are not always visible', 'The Earth’s surface never changes in any way', 'Volcanoes and earthquakes have no connection to the Earth’s surface', 'This concept has no relevance to understanding Earth science'], 0)]),
SS('Social Studies: The Great Lakes: Shipping and Trade',
   'Grade 3 Social Studies strand: the Great Lakes are used as an important shipping route, allowing large ships to carry goods like grain and steel between cities in Canada and the United States.',
   [('The Great Lakes are used as an important ___ route.', ['Shipping', 'A concept unrelated to how goods are transported', 'Only walking, with no connection to large-scale trade', 'Underground, with no connection to lakes at all'], 0),
    ('Large ships on the Great Lakes can carry goods like grain and ___.', ['Steel', 'A concept unrelated to goods carried by ship', 'Only mail, with no connection to large cargo', 'Nothing at all, since ships carry no goods'], 0),
    ('Which is an example of a good that might be transported by ship on the Great Lakes?', ['Iron ore', 'A concept unrelated to shipping and trade', 'An item that has never been transported by ship', 'A good unrelated to Great Lakes trade'], 0),
    ('Why might shipping goods across the Great Lakes be an efficient way to move large amounts of cargo?', ['A single ship can carry very large loads across long distances at once', 'Shipping by water is always slower and less efficient than any other method', 'The Great Lakes have no connection to transporting goods', 'This concept has no relevance to understanding trade routes'], 0),
    ('Why might cities along the Great Lakes, like Toronto and Hamilton, benefit from being located near this shipping route?', ['Easy access to shipping can support trade and industry, helping the local economy grow', 'Being located near the Great Lakes provides no benefit to a city’s economy', 'Shipping routes have no connection to how cities develop', 'This concept has no relevance to understanding Ontario’s geography'], 0)])]),

day(75, [
L('Reading: Understanding Flashbacks in Stories',
  'Grade 3 Language strand: a flashback is a part of a story that interrupts the present action to show an event that happened earlier, helping readers understand something about a character or event.',
  [('A flashback is a part of a story that interrupts the present action to show an event that happened ___.', ['Earlier', 'In the future, with no connection to the past', 'A concept unrelated to how stories are organized', 'At the exact same moment as the present action'], 0),
   ('A flashback can help readers understand something about a ___.', ['Character or event', 'A concept unrelated to why flashbacks are used', 'Only the book’s cover, with no connection to the story', 'Nothing at all, since flashbacks add no meaning'], 0),
   ('Which is a clue that a story might be using a flashback?', ['A character suddenly remembers something that happened long ago', 'A concept unrelated to identifying a flashback', 'A sentence with no connection to time at all', 'An event that is happening in the present moment only'], 0),
   ('Why might an author use a flashback instead of simply telling events in the order they happened?', ['A flashback can reveal important background information at a moment when it helps the reader understand the story better', 'Flashbacks never provide any useful information to a reader', 'An author is never allowed to change the order of events in a story', 'This concept has no relevance to understanding story structure'], 0),
   ('Why is it important for a reader to notice when a story shifts into a flashback?', ['Recognizing the shift helps the reader keep track of when different events in the story are happening', 'Noticing a flashback never helps a reader understand a story', 'A flashback always happens in the exact same time as the rest of the story', 'This concept has no relevance to reading comprehension'], 0)]),
M('Time: Telling Time on Analog and Digital Clocks',
  'Grade 3 Math strand: an analog clock uses moving hands to show the hour and minute, while a digital clock displays the time using only numbers, and both tools show the exact same time in different ways.',
  [('An analog clock uses moving hands to show the hour and ___.', ['Minute', 'A concept unrelated to how an analog clock works', 'Only the day of the week, with no connection to time', 'Season, with no connection to telling time'], 0),
   ('A digital clock displays the time using only ___.', ['Numbers', 'Moving hands, which is how an analog clock works instead', 'A concept unrelated to how a digital clock works', 'Pictures, with no connection to displaying numbers'], 0),
   ('If an analog clock shows the short hand near the 3 and the long hand on the 12, what time is it?', ['3:00', '12:03', '12:15', '3:12'], 0),
   ('Why might it take more practice to read an analog clock than a digital clock?', ['An analog clock requires understanding what both the hour hand and minute hand represent together', 'An analog clock always shows the exact same information as a digital clock with no extra steps', 'Digital clocks are never easier for anyone to read', 'This concept has no relevance to understanding how clocks work'], 0),
   ('Why do both analog and digital clocks show the same time, even though they look very different?', ['Both types of clocks are simply different ways of representing the same passage of time', 'Analog and digital clocks always show two completely different times', 'The way a clock displays time has no connection to the actual time', 'This concept has no relevance to understanding how time is measured'], 0)]),
Sc('Science: Decomposers and the Food Cycle',
   'Grade 3 Science strand: decomposers, like fungi, worms, and bacteria, break down dead plants and animals, returning important nutrients to the soil so new living things can grow.',
   [('Decomposers break down dead plants and animals, returning important nutrients to the ___.', ['Soil', 'Sky, with no connection to how decomposers work', 'A concept unrelated to what decomposers do', 'Ocean floor exclusively, with no connection to soil'], 0),
    ('Which is an example of a decomposer?', ['A fungus', 'A concept unrelated to breaking down dead matter', 'A sunflower, which is a producer, not a decomposer', 'A rabbit, which is a consumer, not a decomposer'], 0),
    ('Decomposers help return nutrients to the soil so that ___.', ['New living things can grow', 'Nothing at all can ever grow again', 'A concept unrelated to how nutrients support growth', 'The soil becomes permanently unusable'], 0),
    ('Why are decomposers an important part of an ecosystem’s food cycle?', ['They recycle nutrients from dead organisms, allowing new plants and animals to use them to grow', 'Decomposers never actually play any role in an ecosystem', 'Nutrients from dead organisms are never reused by other living things', 'This concept has no relevance to understanding food cycles'], 0),
    ('Why might an ecosystem struggle if it had no decomposers at all?', ['Dead plants and animals would not break down, and important nutrients would not be returned to the soil', 'An ecosystem would function exactly the same with or without decomposers', 'Decomposers have no connection to how nutrients move through an ecosystem', 'This concept has no relevance to understanding living systems'], 0)]),
SS('Social Studies: Newspapers and Local Media: Staying Informed',
   'Grade 3 Social Studies strand: newspapers and local media, such as community websites and radio stations, help keep citizens informed about events, decisions, and news happening in their community.',
   [('Newspapers and local media help keep citizens ___ about events happening in their community.', ['Informed', 'Confused, with no connection to sharing news', 'A concept unrelated to how communities share information', 'Unaware, with no connection to staying informed'], 0),
    ('Which is an example of local media?', ['A community radio station', 'A concept unrelated to sharing local news', 'A private letter sent to only one person', 'An item unrelated to informing citizens'], 0),
    ('Local media might report on events such as ___.', ['A new park opening in the community', 'A concept unrelated to local community news', 'A story with no connection to the community at all', 'Nothing at all, since local media reports no real events'], 0),
    ('Why might it be helpful for citizens to read local news about decisions made by their municipal government?', ['Staying informed helps citizens understand how decisions might affect their community', 'Local news never provides any useful information about government decisions', 'Citizens never need to know about decisions made in their community', 'This concept has no relevance to understanding local government'], 0),
    ('Why might a community newspaper report on a wide variety of topics, including sports, events, and local government?', ['Covering many topics keeps the whole community informed about the different things happening around them', 'A community newspaper should only ever report on one single topic', 'Reporting on a variety of topics never actually informs a community', 'This concept has no relevance to understanding local media'], 0)])]),

day(76, [
L('Grammar: Commas in a Series',
  'Grade 3 Language strand: a comma is used to separate three or more items in a series, or list, within a sentence, making the sentence easier to read and understand.',
  [('A comma is used to separate three or more items in a ___ within a sentence.', ['Series, or list', 'A concept unrelated to how commas are used', 'Question, with no connection to listing items', 'Title, with no connection to listing items in a sentence'], 0),
   ('Using commas in a series makes a sentence ___.', ['Easier to read and understand', 'Much harder to read and understand', 'A concept unrelated to sentence punctuation', 'Impossible to understand at all'], 0),
   ('Which sentence correctly uses commas in a series?', ['I packed apples, bananas, and grapes for the trip.', 'I packed apples bananas and grapes for the trip.', 'I packed apples, bananas and, grapes for the trip.', 'A sentence with no items listed at all'], 0),
   ('Why might a sentence listing four items be confusing without any commas separating them?', ['Without commas, it can be hard to tell where one item ends and the next one begins', 'Commas never actually help separate items in a list', 'A sentence with multiple items is always clear with no punctuation at all', 'This concept has no connection to writing clear sentences'], 0),
   ('Why is it a common rule to place a comma before the word “and” in a series of three or more items?', ['It clearly separates the final item from the rest of the list, keeping the sentence organized', 'A comma before “and” always changes the meaning of a sentence', 'This concept has no connection to how commas are used in a series', 'The word “and” should never appear in a list of items'], 0)]),
M('Probability: Conducting a Simple Experiment',
  'Grade 3 Math strand: a probability experiment, like flipping a coin or rolling a die many times, involves recording results to see how often each outcome actually happens.',
  [('A probability experiment involves recording results to see how often each ___ actually happens.', ['Outcome', 'A concept unrelated to conducting an experiment', 'Coin, with no connection to recording results', 'Rule, with no connection to observing outcomes'], 0),
   ('Which is an example of a simple probability experiment?', ['Flipping a coin 20 times and recording the results', 'A concept unrelated to probability', 'Reading a book with no connection to chance', 'Drawing a picture with no connection to recording outcomes'], 0),
   ('If a coin is flipped many times, roughly how often would you expect it to land on heads?', ['About half the time', 'Every single time, with no exceptions', 'Never, since heads is an impossible outcome', 'Exactly one time only, no matter how many flips occur'], 0),
   ('Why is it useful to repeat a probability experiment many times, rather than just once?', ['Repeating the experiment gives a clearer picture of how often each outcome actually tends to happen', 'Repeating an experiment never provides any additional useful information', 'A single trial always gives the exact same result as many trials', 'This concept has no relevance to understanding probability'], 0),
   ('Why might the actual results of rolling a die 30 times not exactly match what you predicted beforehand?', ['Chance can cause real results to vary somewhat from what is expected, especially with a limited number of trials', 'The results of a probability experiment are always identical to the prediction', 'Rolling a die never actually produces any unpredictable results', 'This concept has no relevance to understanding probability experiments'], 0)]),
Sc('Science: Insect Body Parts and Characteristics',
   'Grade 3 Science strand: insects share certain characteristics, including three main body parts — the head, thorax, and abdomen — as well as six legs and, often, wings.',
   [('Insects share certain characteristics, including three main body parts and ___ legs.', ['Six', 'Four, with no connection to insect characteristics', 'A concept unrelated to how insects are classified', 'Eight, which is the number of legs a spider has instead'], 0),
    ('The three main body parts of an insect are the head, thorax, and ___.', ['Abdomen', 'A concept unrelated to insect body parts', 'Tail, with no connection to an insect’s body structure', 'Fin, which is not a body part found on insects'], 0),
    ('Which is an example of an insect?', ['An ant', 'A spider, which has eight legs instead of six', 'A worm, which has no legs at all', 'A concept unrelated to classifying insects'], 0),
    ('Why might counting an animal’s legs help you determine whether it is an insect?', ['Insects have exactly six legs, which is a defining characteristic scientists use for classification', 'The number of legs an animal has never helps with classifying it', 'All animals with legs are always classified as insects', 'This concept has no relevance to understanding animal classification'], 0),
    ('Why might many insects have wings attached to their thorax?', ['The thorax is the body part that provides strength and support for flight muscles', 'Wings have no connection to any part of an insect’s body', 'Insects never actually use their wings for flying', 'This concept has no relevance to understanding insect characteristics'], 0)]),
SS('Social Studies: Francophone Communities in Ontario',
   'Grade 3 Social Studies strand: Ontario is home to many Francophone communities, where people speak French as their first language and celebrate French-Canadian culture and traditions.',
   [('In a Francophone community, people speak ___ as their first language.', ['French', 'A concept unrelated to language in a community', 'Only English, with no connection to Francophone identity', 'A language unrelated to French-Canadian culture'], 0),
    ('Francophone communities in Ontario celebrate French-Canadian ___ and traditions.', ['Culture', 'A concept unrelated to community identity', 'Only sports, with no connection to culture', 'Nothing at all, since traditions have no importance'], 0),
    ('Which is an example of something a Francophone community in Ontario might celebrate?', ['A French-Canadian cultural festival', 'A concept unrelated to Francophone culture', 'An event with no connection to any community’s traditions', 'A celebration entirely unrelated to language or culture'], 0),
    ('Why is it important for Ontario to recognize and support its Francophone communities?', ['These communities are an important part of Ontario’s history and cultural diversity', 'Francophone communities have no connection to Ontario’s identity', 'Ontario has no communities where French is spoken', 'This concept has no relevance to understanding Ontario’s population'], 0),
    ('Why might learning about Francophone communities help students understand Ontario’s diversity?', ['It shows that Ontario includes people with many different languages, cultures, and traditions', 'Learning about Francophone communities provides no useful understanding of Ontario', 'Ontario has only ever had a single shared culture and language', 'This concept has no relevance to social studies learning'], 0)])]),

day(77, [
L('Vocabulary: Root Words and Base Words',
  'Grade 3 Language strand: a root word, or base word, is the simplest form of a word before prefixes or suffixes are added, and it carries the word’s core meaning.',
  [('A root word, or base word, is the simplest form of a word before ___ are added.', ['Prefixes or suffixes', 'Punctuation marks, with no connection to word parts', 'A concept unrelated to how words are built', 'Nothing at all, since words never have any added parts'], 0),
   ('A root word carries the word’s ___.', ['Core meaning', 'A concept unrelated to how a word’s meaning works', 'Spelling only, with no connection to meaning', 'Pronunciation exclusively, with no connection to meaning'], 0),
   ('What is the root word in “unhappiness”?', ['Happy', 'Un', 'Ness', 'A word unrelated to “unhappiness”'], 0),
   ('Why might knowing the root word of an unfamiliar word help a reader figure out its meaning?', ['The root word often carries the core meaning, giving a clue even before considering any prefixes or suffixes', 'The root word of a word never provides any clue about its meaning', 'Unfamiliar words can never be understood using their root word', 'This concept has no connection to building vocabulary'], 0),
   ('Why might the words “teacher,” “teaching,” and “taught” all be related to the same root word?', ['They all connect back to the root word “teach,” which carries the shared core meaning', 'These three words have completely unrelated meanings from each other', 'Root words never connect different forms of a word together', 'This concept has no relevance to understanding vocabulary'], 0)]),
M('Multiplication: The Distributive Property',
  'Grade 3 Math strand: the distributive property lets you break apart one factor into smaller parts, multiply each part separately, and then add the results together to find the total product.',
  [('The distributive property lets you break apart one factor into smaller parts, multiply each part separately, and then ___.', ['Add the results together', 'Subtract the results from each other', 'A concept unrelated to multiplying numbers', 'Ignore one of the results completely'], 0),
   ('Using the distributive property, 6 × 7 can be broken apart as (6 × 5) + (6 × ___).', ['2', '7', '5', '12'], 0),
   ('What is (4 × 3) + (4 × 2), which is the same as 4 × 5?', ['20', '14', '12', '9'], 0),
   ('Why might the distributive property make a difficult multiplication fact easier to solve?', ['Breaking a large factor into smaller, more familiar parts can make the multiplication simpler to calculate mentally', 'Breaking apart a factor always makes a multiplication problem more difficult', 'This concept has no connection to solving multiplication problems', 'The distributive property never actually changes how a problem is solved'], 0),
   ('Using the distributive property, how could 8 × 9 be broken apart to make it easier to solve?', ['(8 × 10) − (8 × 1)', '(8 × 9) + (8 × 9)', '(8 × 1) − (8 × 10)', 'A method unrelated to breaking apart a factor'], 0)]),
Sc('Science: Earth’s Magnetic Field and Compasses',
   'Grade 3 Science strand: the Earth has its own magnetic field, and a compass uses a small magnetized needle that lines up with this field to always point toward magnetic north.',
   [('The Earth has its own ___, which a compass needle lines up with.', ['Magnetic field', 'A concept unrelated to how a compass works', 'Ocean current, with no connection to magnetism', 'Weather pattern, with no connection to magnetism'], 0),
    ('A compass needle always points toward ___.', ['Magnetic north', 'A random direction that constantly changes', 'A concept unrelated to how a compass functions', 'The nearest large city, with no connection to magnetism'], 0),
    ('Which describes how a compass needle behaves?', ['It lines up with the Earth’s magnetic field to show direction', 'A concept unrelated to the function of a compass', 'It spins randomly with no consistent direction at all', 'It never actually points in any particular direction'], 0),
    ('Why might a compass be a useful tool for someone exploring an unfamiliar area?', ['It helps a person figure out which direction they are facing, even without landmarks', 'A compass provides no useful information about direction', 'Compasses never actually work in unfamiliar areas', 'This concept has no relevance to understanding navigation tools'], 0),
    ('Why does a compass needle continue to point in the same direction no matter where you are standing?', ['The Earth’s magnetic field surrounds the whole planet, so the needle lines up with it wherever you go', 'The Earth’s magnetic field only exists in a few specific locations', 'A compass needle points in a completely different direction depending on the weather', 'This concept has no relevance to understanding magnetism'], 0)]),
SS('Social Studies: Treaties Between Canada and Indigenous Peoples',
   'Grade 3 Social Studies strand: a treaty is a formal agreement between the government and Indigenous peoples, often involving land, rights, and responsibilities that both groups agreed to follow.',
   [('A treaty is a formal ___ between the government and Indigenous peoples.', ['Agreement', 'A concept unrelated to how groups make decisions together', 'Argument, with no connection to reaching an agreement', 'Nothing at all, since treaties have no real purpose'], 0),
    ('Treaties often involve land, rights, and ___ that both groups agreed to follow.', ['Responsibilities', 'A concept unrelated to what a treaty includes', 'Only decorations, with no connection to an agreement', 'Weather forecasts, with no connection to treaties'], 0),
    ('Which best describes the purpose of a treaty?', ['To formally record an agreement between two or more groups', 'A concept unrelated to reaching an agreement', 'A story with no real historical importance', 'An event with no connection to government or Indigenous peoples'], 0),
    ('Why is it important for students to learn about treaties between Canada and Indigenous peoples?', ['Treaties are an important part of Canada’s history and continue to affect relationships and rights today', 'Treaties have no connection to understanding Canada’s history', 'Learning about treaties provides no useful understanding of Canada', 'This concept has no relevance to social studies learning'], 0),
    ('Why might it be important for all parties involved in a treaty to understand and respect its terms?', ['A treaty is only meaningful if the groups involved follow the agreement they made together', 'Treaties never need to be understood or followed by anyone', 'The terms of a treaty have no real effect on the people involved', 'This concept has no relevance to understanding historical agreements'], 0)])]),

day(78, [
L('Oral Communication: Giving Clear Directions',
  'Grade 3 Language strand: giving clear directions means explaining steps in the correct order, using specific details, so that a listener can easily understand and follow along.',
  [('Giving clear directions means explaining steps in the correct ___.', ['Order', 'A concept unrelated to explaining a process', 'Colour, with no connection to giving directions', 'Volume, with no connection to the order of steps'], 0),
   ('Clear directions use specific details so that a listener can ___.', ['Easily understand and follow along', 'Become confused about what to do next', 'A concept unrelated to giving directions', 'Ignore the instructions completely'], 0),
   ('Which is an example of a clear direction?', ['Turn left at the red house, then walk two blocks.', 'A statement with no connection to giving directions', 'Go somewhere, eventually, at some point.', 'A sentence unrelated to explaining a path or process'], 0),
   ('Why might leaving out a step when giving directions cause confusion for the listener?', ['A missing step can leave a gap in the instructions, making it hard to know what to do next', 'Leaving out a step never causes any confusion at all', 'Directions are always clear no matter which steps are included', 'This concept has no connection to giving effective directions'], 0),
   ('Why is it helpful to use specific, descriptive words when giving someone directions to a new place?', ['Specific words reduce confusion and help the listener picture exactly where to go', 'Specific words never make directions any clearer', 'Vague directions are always just as helpful as specific ones', 'This concept has no relevance to effective oral communication'], 0)]),
M('Data: Venn Diagrams for Sorting',
  'Grade 3 Math strand: a Venn diagram uses overlapping circles to sort items into groups, showing which items belong to only one group and which items share characteristics of both groups.',
  [('A Venn diagram uses overlapping circles to sort items, showing which items share characteristics of ___.', ['Both groups', 'Neither group at all', 'A concept unrelated to sorting items', 'Only a single group, with no overlap possible'], 0),
   ('In a Venn diagram, the overlapping section in the middle shows items that ___.', ['Belong to both groups', 'Belong to no group at all', 'A concept unrelated to how a Venn diagram works', 'Have been removed from the diagram entirely'], 0),
   ('If one circle in a Venn diagram is “Has four legs” and another is “Can swim,” where would a frog likely be placed?', ['In the overlapping section, since a frog has four legs and can swim', 'Outside both circles entirely, with no connection to either group', 'A concept unrelated to sorting animals by characteristics', 'Only in the “Has four legs” circle, with no connection to swimming'], 0),
   ('Why is a Venn diagram a useful tool for comparing and sorting two groups of items?', ['It visually shows what items have in common and what makes each group different', 'A Venn diagram never actually helps compare or sort items', 'This concept has no connection to organizing information', 'Overlapping circles never show any useful relationship between groups'], 0),
   ('Why might an item be placed outside of both circles in a Venn diagram?', ['The item does not share the characteristics being used to define either group', 'Every single item must always belong to at least one of the two circles', 'Items placed outside both circles are placed there completely at random', 'This concept has no relevance to understanding how Venn diagrams work'], 0)]),
Sc('Science: Severe Weather: Storms and Safety',
   'Grade 3 Science strand: severe weather, such as thunderstorms and blizzards, can create dangerous conditions, so it is important to know safety steps like staying indoors and away from windows.',
   [('Severe weather, such as thunderstorms and blizzards, can create ___ conditions.', ['Dangerous', 'A concept unrelated to how severe weather affects safety', 'Always perfectly calm, with no risk involved', 'Completely predictable, with no danger at all'], 0),
    ('During a thunderstorm, an important safety step is to stay indoors and away from ___.', ['Windows', 'A concept unrelated to storm safety', 'Only the kitchen, with no other connection to safety', 'Nothing in particular, since no precautions are needed'], 0),
    ('Which is an example of severe weather?', ['A blizzard', 'A clear, sunny day with no wind', 'A concept unrelated to weather conditions', 'A calm evening with a gentle breeze'], 0),
    ('Why is it important for people to know safety steps for severe weather, like thunderstorms?', ['Following safety steps can help reduce the risk of injury during dangerous weather conditions', 'Safety steps never actually reduce the risk of injury from severe weather', 'Severe weather never poses any danger to people at all', 'This concept has no relevance to understanding weather'], 0),
    ('Why might communities use warning systems, like weather alerts, before a severe storm arrives?', ['Early warnings give people time to prepare and take safety precautions before the storm hits', 'Weather alerts never provide any useful information to a community', 'Communities never need advance notice of severe weather', 'This concept has no relevance to understanding severe weather safety'], 0)]),
SS('Social Studies: Remembrance Day and Canada’s Veterans',
   'Grade 3 Social Studies strand: Remembrance Day, held on November 11th, is a day when Canadians honour veterans and remember those who served in the armed forces to protect their country.',
   [('Remembrance Day is held on ___.', ['November 11th', 'A concept unrelated to a specific date', 'January 1st, with no connection to Remembrance Day', 'July 1st, which is Canada Day instead'], 0),
    ('On Remembrance Day, Canadians honour ___ who served in the armed forces.', ['Veterans', 'A concept unrelated to who is honoured on this day', 'Only current government leaders, with no military connection', 'Nobody in particular, since the day has no real purpose'], 0),
    ('Which is a symbol commonly worn to honour Remembrance Day?', ['A poppy', 'A concept unrelated to Remembrance Day symbols', 'An item with no connection to remembering veterans', 'A symbol unrelated to Canadian history'], 0),
    ('Why do many Canadians choose to wear a poppy in the days leading up to Remembrance Day?', ['Wearing a poppy is a way to show respect and remembrance for those who served in the armed forces', 'The poppy has no connection to honouring veterans', 'Wearing a poppy is never actually connected to Remembrance Day', 'This concept has no relevance to understanding Canadian traditions'], 0),
    ('Why is it important for students to learn about Remembrance Day and the sacrifices made by veterans?', ['It helps students understand and appreciate an important part of Canada’s history', 'Learning about Remembrance Day provides no useful understanding of Canada', 'Veterans have no connection to Canada’s history', 'This concept has no relevance to social studies learning'], 0)])]),

day(79, [
L('Vocabulary: Onomatopoeia and Sound Words',
  'Grade 3 Language strand: onomatopoeia is a word that imitates the actual sound it describes, such as “buzz,” “crash,” or “sizzle,” helping writing feel more vivid and alive.',
  [('Onomatopoeia is a word that imitates the actual ___ it describes.', ['Sound', 'A concept unrelated to how a word is formed', 'Colour, with no connection to sound at all', 'Shape, with no connection to how a word sounds'], 0),
   ('Which word is an example of onomatopoeia?', ['Buzz', 'Happy, which describes a feeling rather than a sound', 'A word unrelated to describing any sound', 'Table, which is an object rather than a sound'], 0),
   ('Onomatopoeia can help writing feel more ___.', ['Vivid and alive', 'Boring and lifeless', 'A concept unrelated to descriptive writing', 'Confusing, with no connection to the reader’s experience'], 0),
   ('Why might an author use the word “crash” instead of simply writing “a loud noise happened”?', ['“Crash” imitates the actual sound, helping the reader imagine the moment more vividly', 'Onomatopoeia never adds any extra meaning to a sentence', 'The word “crash” has no connection to describing a sound', 'This concept has no relevance to descriptive writing'], 0),
   ('Why might onomatopoeia be especially useful in a story describing a thunderstorm?', ['Sound words like “boom” or “crack” can help the reader imagine the noise of the storm', 'Onomatopoeia has no connection to describing weather in a story', 'A thunderstorm never actually makes any sound worth describing', 'This concept has no relevance to using vivid language in writing'], 0)]),
M('Financial Literacy: Needs vs Wants',
  'Grade 3 Math strand: a need is something a person must have to survive, like food and shelter, while a want is something a person would like to have but does not require to live.',
  [('A need is something a person must have to ___.', ['Survive', 'Simply enjoy their free time, with no connection to survival', 'A concept unrelated to basic requirements for living', 'Impress other people, with no connection to survival'], 0),
   ('A want is something a person would like to have but does not require to ___.', ['Live', 'A concept unrelated to the difference between needs and wants', 'Spend money, with no connection to survival', 'Travel, with no connection to basic requirements'], 0),
   ('Which is an example of a need rather than a want?', ['Food', 'A video game', 'A concept unrelated to needs and wants', 'A toy unrelated to basic survival'], 0),
   ('Why might it be important for a family to prioritize needs, like housing, before spending money on wants?', ['Meeting basic needs first helps ensure a family’s safety and well-being before spending on extras', 'Needs are never actually more important than wants', 'Wants should always be purchased before any needs are met', 'This concept has no relevance to understanding financial literacy'], 0),
   ('Why might a toy be considered a want rather than a need, even though a child might really enjoy it?', ['A toy is not required for a person’s basic survival, even though it can bring enjoyment', 'Toys are always classified as needs rather than wants', 'The classification of needs and wants has no connection to survival', 'This concept has no relevance to understanding financial literacy'], 0)]),
Sc('Science: Plant Adaptations Around the World',
   'Grade 3 Science strand: plants have adaptations that help them survive in different environments, such as thick stems in the desert, tall canopies in the rainforest, and short growth close to the ground in the Arctic.',
   [('Plants have adaptations that help them survive in different ___.', ['Environments', 'A concept unrelated to how plants grow', 'Colours, with no connection to survival', 'Time zones, with no connection to plant survival'], 0),
    ('A cactus growing in the desert often has a thick stem to help it ___.', ['Store water', 'A concept unrelated to desert plant adaptations', 'Attract more rainfall directly to its stem', 'Grow taller than every other type of plant'], 0),
    ('Which is an adaptation that helps plants survive in the cold Arctic environment?', ['Growing short and close to the ground', 'A concept unrelated to Arctic plant adaptations', 'Growing extremely tall to reach more sunlight', 'Growing without any roots at all'], 0),
    ('Why might rainforest trees grow very tall with wide canopies at the top?', ['Growing tall helps the trees reach sunlight above the dense forest canopy', 'Height has no connection to how rainforest trees access sunlight', 'Rainforest trees never actually need any sunlight to survive', 'This concept has no relevance to understanding plant adaptations'], 0),
    ('Why do plants in different environments, like deserts and rainforests, develop such different adaptations?', ['Each environment presents different challenges, so plants develop features suited to survive those specific conditions', 'All environments present the exact same challenges for every plant', 'Plant adaptations have no connection to the environment a plant grows in', 'This concept has no relevance to understanding plant survival'], 0)]),
SS('Social Studies: Tourism in Ontario: Visiting Our Province',
   'Grade 3 Social Studies strand: tourism is an industry built around people visiting interesting places, and Ontario attracts tourists with attractions like Niagara Falls, provincial parks, and vibrant cities.',
   [('Tourism is an industry built around people ___ interesting places.', ['Visiting', 'A concept unrelated to how tourism works', 'Ignoring completely, with no connection to travel', 'Destroying, with no connection to tourism at all'], 0),
    ('Ontario attracts tourists with attractions like Niagara Falls and provincial ___.', ['Parks', 'A concept unrelated to Ontario’s tourist attractions', 'Only office buildings, with no connection to tourism', 'Nothing at all, since Ontario has no notable attractions'], 0),
    ('Which is an example of a popular tourist attraction in Ontario?', ['Niagara Falls', 'A concept unrelated to Ontario’s attractions', 'A location that does not actually exist in Ontario', 'An attraction found only in a different province'], 0),
    ('Why might tourism be an important part of Ontario’s economy?', ['Visitors spend money on hotels, food, and attractions, which can support many local jobs and businesses', 'Tourism never actually benefits Ontario’s economy in any way', 'Tourists never spend any money while visiting a province', 'This concept has no relevance to understanding Ontario’s economy'], 0),
    ('Why might Ontario work to protect natural attractions, like its provincial parks, for tourism?', ['Well-preserved natural attractions can continue drawing visitors and supporting the tourism industry for years to come', 'Protecting natural attractions has no connection to supporting tourism', 'Provincial parks never actually attract any visitors to Ontario', 'This concept has no relevance to understanding Ontario’s economy'], 0)])]),

day(80, [
L('Review: Figurative Language, Sentences, and Vocabulary',
  'Grade 3 Language strand review: this lesson revisits similes and metaphors, the four types of sentences, multiple-meaning words, root words, and onomatopoeia.',
  [('Which sentence is an example of a simile?', ['Her smile was as bright as the sun.', 'Her smile was the sun.', 'A sentence with no comparison at all', 'Her smile was very nice today.'], 0),
   ('Which sentence is an exclamation?', ['Watch out for that puddle!', 'Please pass the salt.', 'What time is it.', 'The sky is blue.'], 0),
   ('The word “bat” can mean a flying animal or ___.', ['Equipment used to hit a ball', 'A concept unrelated to the word “bat”', 'A type of vegetable grown in a garden', 'A word unrelated to any of “bat”’s real meanings'], 0),
   ('What is the root word in “unhappiness”?', ['Happy', 'Un', 'Ness', 'A word unrelated to “unhappiness”'], 0),
   ('Why is it useful to review figurative language, sentence types, and vocabulary skills together?', ['These skills all help writers and readers communicate and understand language more clearly', 'These skills have no connection to each other', 'Review is never useful for language learning', 'Each skill must always be learned with no connection to any other'], 0)]),
M('Review: Multiplication, Geometry, and Data Strategies',
  'Grade 3 Math strand review: this lesson revisits multiplying three factors, classifying triangles by side length, input-output tables, the distributive property, and Venn diagrams.',
  [('What is 2 × 3 × 4?', ['24', '9', '20', '12'], 0),
   ('A triangle with three equal sides is called ___.', ['Equilateral', 'Isosceles, which has only two equal sides', 'A concept unrelated to classifying triangles', 'Scalene, which has no equal sides at all'], 0),
   ('If the rule is “add 3” and the input is 5, what is the output?', ['8', '5', '3', '15'], 0),
   ('Using the distributive property, 6 × 7 can be broken apart as (6 × 5) + (6 × ___).', ['2', '7', '5', '12'], 0),
   ('Why is it useful to review multiplication strategies, geometry, and data tools together?', ['These related math skills reinforce each other for a stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Life Cycles, Earth Science, and Adaptations',
   'Grade 3 Science strand review: this lesson revisits the butterfly life cycle, nocturnal and diurnal animals, fossils, volcanoes and earthquakes, and plant adaptations around the world.',
   [('Which is the correct order of a butterfly’s life cycle?', ['Egg, larva, pupa, adult', 'Adult, pupa, larva, egg', 'Pupa, egg, adult, larva', 'A random order with no set sequence at all'], 0),
    ('Which animal is typically nocturnal?', ['An owl', 'A robin, which is typically diurnal', 'A squirrel, which is typically diurnal', 'A concept unrelated to animal activity patterns'], 0),
    ('A fossil is the preserved remains or trace of a living thing from ___.', ['Long ago', 'Only the present day, with no connection to the past', 'A concept unrelated to Earth’s history', 'The near future, with no connection to past living things'], 0),
    ('Volcanoes and earthquakes are powerful events caused by movements deep within the ___.', ['Earth', 'Ocean, with no connection to the Earth’s interior', 'A concept unrelated to how these events occur', 'Sky, with no connection to the ground shifting'], 0),
    ('Why is it useful to review life cycles, Earth science, and adaptations together?', ['It reinforces how living things and the Earth itself change and adapt over time', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Laws, Industry, and Communities',
   'Grade 3 Social Studies strand review: this lesson revisits laws and bylaws, taxes, mining and forestry, treaties, and tourism in Ontario.',
   [('Bylaws are rules made by a ___ government.', ['Municipal', 'Provincial, with no connection to local rules', 'A concept unrelated to how communities are governed', 'Federal, with no connection to local community rules'], 0),
    ('Taxes are money that people and businesses pay to the ___.', ['Government', 'A concept unrelated to funding shared services', 'Only a single private company, with no public purpose', 'Nothing at all, since taxes serve no real purpose'], 0),
    ('Mining in Ontario provides minerals such as nickel and ___.', ['Gold', 'A concept unrelated to minerals found through mining', 'Only water, which is not a mined mineral', 'Nothing useful at all, since mining provides no resources'], 0),
    ('A treaty is a formal ___ between the government and Indigenous peoples.', ['Agreement', 'A concept unrelated to how groups make decisions together', 'Argument, with no connection to reaching an agreement', 'Nothing at all, since treaties have no real purpose'], 0),
    ('Why is it useful to review laws, industry, and community topics together at this point in the year?', ['It helps students see how government, economy, and community life connect and support one another', 'These topics have no meaningful connection to each other', 'Bringing lessons together never provides any additional understanding', 'Each topic must always be learned with no connection to any other'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260901):
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
    _rebalance_answer_positions(g3_71_80)
    append_to(3, g3_71_80)
