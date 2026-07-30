#!/usr/bin/env python3
"""Grade 4, Days 121-130 -- extends Grade 4 from 120 to 130 days. Modeled
exactly on gen_grade4_days111_120.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-120
topics (see data/grade4.json), which already densely cover nearly the
entire grade 4 curriculum, including (as of Days 111-120) the skeletal,
muscular, circulatory, respiratory, and nervous body systems. New topics:
comma rules, plural noun rules, prepositional phrases, analyzing poetry
(stanzas/rhyme scheme/meter), identifying tone, loanwords, writing an
autobiography, writing a mystery story, and writing a fable for Language;
adding fractions with unlike denominators, square numbers and square
roots, divisibility rules for 3/6/9, tessellations, same-perimeter-
different-area shapes, Venn diagrams, probability as a percent,
discounts and sale prices, and double line graphs for Math; the
digestive system, the skin, the immune system, the five senses, insect
metamorphosis, fossil fuels, the carbon cycle, geothermal/biomass energy,
and coral reefs for Science; and ancient Japan, the Prime Minister, the
Canadian Coast Guard, Remembrance Day, the boreal forest, the mining
industry, Canada-United States trade, the history of O Canada, and
volunteers/charities for Social Studies -- none of those exact ideas
appear in Days 1-120. Day 130 is a review day across all four subjects,
matching the end-of-batch pattern used in every prior 10-day batch. No
embedded ASCII double-quote or apostrophe characters are used anywhere
in title/summary/question/option text, matching the convention used in
gen_grade4_days111_120.py (apostrophes dropped entirely, e.g. "Canadas"
not "Canada's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


g4_121_130 = [
day(121, [
L('Grammar: Comma Rules — Series, Introductory Phrases, and Compound Sentences',
  'Grade 4 Language strand: commas separate items in a series, follow introductory phrases at the start of a sentence, and join two independent clauses before a coordinating conjunction in a compound sentence.',
  [('Which sentence uses commas correctly in a series?', ['I packed apples, oranges, and grapes.', 'I packed apples oranges, and grapes.', 'I packed, apples oranges and grapes.', 'I packed apples, oranges and, grapes.'], 0),
   ('Where does a comma usually go after an introductory phrase?', ['Right after the introductory phrase', 'At the very end of the sentence', 'Before the subject only', 'Commas are never used with introductory phrases'], 0),
   ('Which sentence correctly uses a comma in a compound sentence?', ['I finished my homework, and I watched a movie.', 'I finished my homework and, I watched a movie.', 'I finished, my homework and I watched a movie.', 'I finished my homework and I, watched a movie.'], 0),
   ('What does a comma do when separating items in a list?', ['Shows where one item ends and the next begins', 'Ends the sentence', 'Joins two full sentences without a conjunction', 'Replaces a period'], 0),
   ('In the sentence After the storm passed, we went outside, what is being set off by the comma?', ['An introductory phrase', 'A list of items', 'A quotation', 'A title'], 0)]),
M('Fractions: Adding Fractions with Unlike Denominators',
  'Grade 4 Math strand: to add fractions with unlike denominators, students find a common denominator, rewrite each fraction as an equivalent fraction, then add the numerators.',
  [('What must fractions have before they can be added directly?', ['A common denominator', 'The same numerator', 'The same sign', 'Different denominators'], 0),
   ('What is 1/2 + 1/4?', ['3/4', '2/6', '1/6', '2/4'], 0),
   ('What is 1/3 + 1/6?', ['1/2', '2/9', '1/9', '7/6'], 0),
   ('What is the first step in adding fractions with unlike denominators?', ['Find a common denominator', 'Add the denominators', 'Multiply the numerators', 'Subtract the fractions'], 0),
   ('Why cant we add fraction numerators directly when denominators differ?', ['Because the pieces are different sizes until denominators match', 'Fractions can never be added', 'Numerators are always equal', 'Denominators do not matter'], 0)]),
Sc('Science: The Human Digestive System — Breaking Down Food for Energy',
   'Grade 4 Science strand: the digestive system breaks down food into nutrients the body can absorb and use for energy, involving organs such as the stomach, small intestine, and large intestine.',
   [('What is the main job of the digestive system?', ['Breaking down food into nutrients the body can use', 'Pumping blood', 'Sending nerve signals', 'Filtering air'], 0),
    ('Which organ mixes food with acid to help break it down?', ['The stomach', 'The brain', 'The heart', 'The lungs'], 0),
    ('Where are nutrients mostly absorbed into the blood?', ['The small intestine', 'The mouth', 'The lungs', 'The skin'], 0),
    ('What happens to food waste after nutrients are absorbed?', ['It passes through the large intestine to be removed from the body', 'It turns into oxygen', 'It becomes bone', 'It is stored in the brain'], 0),
    ('Why does the body need to digest food?', ['To break it into nutrients that provide energy and building blocks for the body', 'Digestion has no purpose', 'To make food heavier', 'To stop the body from growing'], 0)]),
SS('Social Studies: Ancient Japan — Early Society and Culture',
   'Grade 4 Social Studies strand: ancient Japan developed a unique early society influenced by its island geography, featuring farming communities, emperors, and rich traditions in art and religion.',
   [('What type of geography influenced ancient Japans development?', ['Its island location', 'A vast desert', 'A landlocked plain', 'A mountain range with no coast'], 0),
    ('What role did an emperor typically hold in ancient Japan?', ['A central figure of authority and tradition', 'A random villager', 'A foreign visitor', 'No role at all'], 0),
    ('What was a common economic activity in early Japanese society?', ['Farming, especially rice cultivation', 'Only fishing', 'Only mining', 'Only trading with no farming'], 0),
    ('Why is Japans island geography significant to its early history?', ['It shaped trade, culture, and how the society developed somewhat separately', 'It made no difference to society', 'It prevented any culture from forming', 'It caused constant flooding with no benefits'], 0),
    ('What aspect of ancient Japanese culture became influential in art and religion?', ['Traditions passed down and refined over centuries', 'A complete absence of art', 'Modern technology only', 'European traditions only'], 0)]),
]),
day(122, [
L('Grammar: Plural Noun Rules — Regular and Irregular Forms',
  'Grade 4 Language strand: most nouns form plurals by adding -s or -es, but irregular nouns change form in other ways, such as child to children or mouse to mice.',
  [('What is the plural of dog?', ['Dogs', 'Dogies', 'Doges', 'Dogen'], 0),
   ('What is the plural of box?', ['Boxes', 'Boxs', 'Box', 'Boxies'], 0),
   ('What is the irregular plural of child?', ['Children', 'Childs', 'Childes', 'Childrens'], 0),
   ('What is the irregular plural of mouse?', ['Mice', 'Mouses', 'Mices', 'Meese'], 0),
   ('Which rule usually applies to nouns ending in a consonant plus y, like baby?', ['Change the y to i and add es', 'Just add s', 'Add es only', 'The word never changes'], 0)]),
M('Number Sense: Square Numbers and Square Roots',
  'Grade 4 Math strand: a square number is the product of a whole number multiplied by itself, such as 4 x 4 = 16, and the square root is the number that produces it, such as the square root of 16 is 4.',
  [('What is a square number?', ['A number multiplied by itself', 'Any even number', 'A number divided by itself', 'A number added to itself'], 0),
   ('What is 5 squared (5 x 5)?', ['25', '10', '20', '15'], 0),
   ('What is the square root of 16?', ['4', '8', '2', '16'], 0),
   ('What is the square root of 9?', ['3', '9', '6', '18'], 0),
   ('Square numbers can be shown as ___.', ['Arrays forming a perfect square shape', 'Only odd numbers', 'Only prime numbers', 'Numbers divided by zero'], 0)]),
Sc('Science: The Skin — Our Bodys Protective Organ',
   'Grade 4 Science strand: the skin is the bodys largest organ, protecting against germs and injury, helping regulate temperature, and containing nerve endings that sense touch.',
   [('What is the skin often described as?', ['The bodys largest organ', 'The smallest organ', 'A type of bone', 'A type of muscle only'], 0),
    ('What is one job of the skin?', ['Protecting the body from germs and injury', 'Pumping blood', 'Digesting food', 'Sending only sound signals'], 0),
    ('How does skin help regulate body temperature?', ['Through sweating and changes in blood flow near the surface', 'By growing hair only', 'By changing colour permanently', 'Skin does not affect temperature'], 0),
    ('What allows skin to sense touch?', ['Nerve endings in the skin', 'Bones beneath the skin', 'Muscles only', 'Blood vessels only'], 0),
    ('Why is it important to protect skin from cuts and injuries?', ['Skin acts as a barrier against germs entering the body', 'Skin has no protective function', 'Cuts never affect health', 'Skin cannot be injured'], 0)]),
SS('Social Studies: The Role of the Prime Minister in Canada',
   'Grade 4 Social Studies strand: the Prime Minister is the head of the Canadian federal government, leading the Cabinet and overseeing the passage of laws and national policy.',
   [('What is the Prime Minister the head of?', ['The Canadian federal government', 'A single province', 'A city council', 'A private company'], 0),
    ('What group does the Prime Minister lead?', ['The Cabinet', 'The Supreme Court', 'The RCMP only', 'The Senate only'], 0),
    ('How does someone usually become Prime Minister of Canada?', ['Their political party wins the most seats in a federal election', 'They are born into the role', 'They are appointed by another country', 'They win a local election only'], 0),
    ('What is one responsibility of the Prime Minister?', ['Overseeing national policy and the passage of laws', 'Coaching sports teams', 'Running a single business', 'Teaching in schools'], 0),
    ('Where does the Prime Minister typically work while serving?', ['In Ottawa, the national capital', 'In a different country', 'In a province chosen at random', 'Nowhere in particular'], 0)]),
]),
day(123, [
L('Grammar: Prepositional Phrases',
  'Grade 4 Language strand: a prepositional phrase begins with a preposition and ends with a noun or pronoun, showing relationships such as location, time, or direction, as in under the table or before dinner.',
  [('What does a prepositional phrase begin with?', ['A preposition', 'A verb', 'A conjunction', 'An adjective'], 0),
   ('Which is a prepositional phrase?', ['Under the table', 'Ran quickly', 'Happy dog', 'And then'], 0),
   ('In the sentence The cat slept on the couch, what is the prepositional phrase?', ['On the couch', 'The cat', 'Slept', 'The cat slept'], 0),
   ('What can a prepositional phrase show?', ['Location, time, or direction', 'Only colour', 'Only size', 'Only sound'], 0),
   ('Which word could begin a prepositional phrase?', ['Before', 'Quickly', 'Happy', 'Run'], 0)]),
M('Number Sense: Divisibility Rules for 3, 6, and 9',
  'Grade 4 Math strand: a number is divisible by 3 if the sum of its digits is divisible by 3, by 9 if the digit sum is divisible by 9, and by 6 if it is divisible by both 2 and 3.',
  [('A number is divisible by 3 if ___.', ['The sum of its digits is divisible by 3', 'It ends in 0', 'It ends in an even digit', 'It is a prime number'], 0),
   ('Is 123 divisible by 3?', ['Yes, because 1+2+3=6 is divisible by 3', 'No, because it is an odd number', 'No, because it ends in 3', 'Yes, because it has three digits'], 0),
   ('A number is divisible by 9 if ___.', ['The sum of its digits is divisible by 9', 'It ends in 9', 'It is divisible by 3 only', 'It is an odd number'], 0),
   ('For a number to be divisible by 6, it must be divisible by ___.', ['Both 2 and 3', 'Only 2', 'Only 3', 'Neither 2 nor 3'], 0),
   ('Is 42 divisible by 6?', ['Yes, because it is divisible by both 2 and 3', 'No, because it is odd', 'No, because its digit sum is not divisible by 3', 'Yes, but only by 2'], 0)]),
Sc('Science: The Immune System — How Our Body Fights Germs',
   'Grade 4 Science strand: the immune system defends the body against harmful germs using white blood cells and other defenses that identify and destroy invaders.',
   [('What is the main job of the immune system?', ['Defending the body against harmful germs', 'Pumping blood through the body', 'Breaking down food', 'Sending messages to muscles'], 0),
    ('What blood cells help fight germs?', ['White blood cells', 'Red blood cells only', 'Bone cells', 'Skin cells only'], 0),
    ('What is a germ?', ['A tiny organism that can cause illness', 'A type of bone', 'A large animal', 'A kind of rock'], 0),
    ('Why might a fever occur when the body is fighting an infection?', ['It can help the immune system fight germs more effectively', 'Fevers have no connection to illness', 'Fevers always mean the body is healthy', 'Fevers stop the immune system from working'], 0),
    ('How do vaccines help the immune system?', ['They help the body learn to recognize and fight specific germs', 'They remove the immune system entirely', 'They have no effect on immunity', 'They only affect the skin'], 0)]),
SS('Social Studies: The Canadian Coast Guard',
   'Grade 4 Social Studies strand: the Canadian Coast Guard is a federal service that ensures safe navigation, responds to search and rescue emergencies, and protects Canadas waters.',
   [('What does the Canadian Coast Guard help ensure?', ['Safe navigation on Canadas waters', 'Safe travel on highways only', 'Safe air travel only', 'Safe travel through forests'], 0),
    ('What is one major responsibility of the Coast Guard?', ['Responding to search and rescue emergencies at sea', 'Teaching in schools', 'Growing crops', 'Building houses'], 0),
    ('What level of government operates the Canadian Coast Guard?', ['Federal', 'Municipal', 'Provincial only', 'No government involvement'], 0),
    ('Why is protecting Canadas waters important?', ['Canada has extensive coastlines and waterways vital to trade and safety', 'Canada has no coastline', 'Water protection is unnecessary', 'Only oceans exist, no coastlines to protect'], 0),
    ('The Coast Guard is an example of a service that ___.', ['Keeps people and shipping safe on the water', 'Has no purpose', 'Only exists in other countries', 'Focuses solely on farming'], 0)]),
]),
day(124, [
L('Reading: Analyzing Poetry — Stanzas, Rhyme Scheme, and Meter',
  'Grade 4 Language strand: poems are organized into stanzas, may follow a rhyme scheme such as ABAB, and use meter, a pattern of rhythm, to create musicality.',
  [('What is a stanza?', ['A group of lines in a poem, like a paragraph', 'A single word', 'A type of punctuation', 'The title of a poem'], 0),
   ('What does rhyme scheme describe?', ['The pattern of rhyming sounds at the ends of lines', 'The number of stanzas', 'The authors name', 'The poems length'], 0),
   ('In an ABAB rhyme scheme, which lines rhyme with each other?', ['Lines 1 and 3, and lines 2 and 4', 'All four lines rhyme', 'No lines rhyme', 'Only lines 1 and 2'], 0),
   ('What is meter in poetry?', ['A pattern of rhythm created by stressed and unstressed syllables', 'A measurement of length', 'A type of comma rule', 'A kind of prefix'], 0),
   ('Why might a poet use a strong rhyme scheme and meter?', ['To create a musical, memorable feeling', 'To make the poem confusing', 'To remove all structure', 'To avoid using any words'], 0)]),
M('Geometry: Tessellations — Tiling a Plane with Transformations',
  'Grade 4 Math strand: a tessellation is a repeating pattern of shapes that covers a flat surface with no gaps or overlaps, often created using translations, reflections, and rotations.',
  [('What is a tessellation?', ['A repeating pattern of shapes covering a surface with no gaps or overlaps', 'A single isolated shape', 'A shape with curved sides only', 'A 3D solid figure'], 0),
   ('Which shape is well known for tessellating easily?', ['A regular hexagon', 'A circle', 'An oval', 'A cone'], 0),
   ('Which transformations are often used to create tessellations?', ['Translations, reflections, and rotations', 'Only enlarging shapes', 'Only colouring shapes', 'Only measuring angles'], 0),
   ('Why can circles not tessellate on their own?', ['They leave gaps between them when repeated', 'They are too small', 'They have too many sides', 'They are always the same colour'], 0),
   ('Where can tessellations be found in real life?', ['Floor tiles and honeycomb patterns', 'Only in outer space', 'Only in liquids', 'Nowhere in real life'], 0)]),
Sc('Science: The Five Senses and Sensory Organs',
   'Grade 4 Science strand: humans perceive the world through five senses -- sight, hearing, smell, taste, and touch -- each detected by a specialized sensory organ.',
   [('How many main senses do humans have?', ['Five', 'Three', 'Seven', 'Two'], 0),
    ('Which organ is responsible for the sense of sight?', ['The eyes', 'The ears', 'The nose', 'The tongue'], 0),
    ('Which organ is responsible for the sense of hearing?', ['The ears', 'The eyes', 'The nose', 'The skin'], 0),
    ('Which organ is mainly responsible for the sense of taste?', ['The tongue', 'The ears', 'The eyes', 'The nose'], 0),
    ('Why are the five senses important?', ['They help us gather information about our environment', 'They have no useful purpose', 'Only sight matters for survival', 'Senses only work in the dark'], 0)]),
SS('Social Studies: Remembrance Day and Canadas Military History',
   'Grade 4 Social Studies strand: Remembrance Day, observed on November 11, honours Canadians who served and sacrificed in military conflicts, marked by moments of silence and wearing poppies.',
   [('On what date is Remembrance Day observed in Canada?', ['November 11', 'July 1', 'December 25', 'October 31'], 0),
    ('What does Remembrance Day honour?', ['Canadians who served and sacrificed in military conflicts', 'A sports championship', 'A harvest festival', 'A new years celebration'], 0),
    ('What symbol is commonly worn on Remembrance Day?', ['A poppy', 'A maple leaf pin', 'A red ribbon', 'A small flag pin'], 0),
    ('What tradition is observed at 11 a.m. on Remembrance Day?', ['A moment of silence', 'A parade with loud music', 'A fireworks display', 'A public holiday with no observance'], 0),
    ('Why is it important for students to learn about Remembrance Day?', ['It helps them understand and honour sacrifices made in Canadas history', 'It has no historical importance', 'It is only about modern events', 'It celebrates a sports victory'], 0)]),
]),
day(125, [
L('Reading: Identifying Tone in a Text',
  'Grade 4 Language strand: tone is the authors attitude toward a subject, revealed through word choice and details, such as a humorous, serious, or sorrowful tone.',
  [('What is tone in a piece of writing?', ['The authors attitude toward the subject', 'The setting of the story', 'The main character', 'The title of the text'], 0),
   ('How can readers identify an authors tone?', ['By examining word choice and details', 'By counting the pages', 'By looking at the cover only', 'Tone cannot be identified'], 0),
   ('Which words might signal a humorous tone?', ['Playful and silly language', 'Formal legal terms', 'Only sad words', 'Only angry words'], 0),
   ('Which words might signal a serious tone?', ['Formal, weighty language about an important topic', 'Silly jokes', 'Random nonsense words', 'Bright, playful exclamations'], 0),
   ('Why is understanding tone important for readers?', ['It helps readers understand how the author feels about the topic', 'It has no effect on understanding a text', 'Tone only matters in poetry', 'Tone is the same as plot'], 0)]),
M('Measurement: Exploring Shapes with the Same Perimeter but Different Area',
  'Grade 4 Math strand: two shapes can share the same perimeter yet enclose different areas, showing that perimeter and area measure different properties of a shape.',
  [('What does perimeter measure?', ['The distance around a shape', 'The space inside a shape', 'The number of sides only', 'The weight of a shape'], 0),
   ('What does area measure?', ['The space inside a shape', 'The distance around a shape', 'The height only', 'The number of corners'], 0),
   ('A 2 by 8 rectangle and a 5 by 5 square both have a perimeter of 20 -- which shape has a greater area?', ['The square (25) has a greater area than the rectangle (16)', 'The rectangle always has more area', 'They always have equal area', 'Area cannot be compared this way'], 0),
   ('Why is it useful to know that shapes can share a perimeter but differ in area?', ['It shows perimeter and area are independent measurements', 'It proves perimeter and area are the same thing', 'It means area never changes', 'It means perimeter is not useful'], 0),
   ('Which shape generally maximizes area for a given perimeter?', ['A shape closer to a square or circle', 'A very long, thin rectangle', 'A shape with many sharp points', 'Any triangle'], 0)]),
Sc('Science: Insect Life Cycles — Complete and Incomplete Metamorphosis',
   'Grade 4 Science strand: insects such as butterflies undergo complete metamorphosis with four distinct stages, while insects such as grasshoppers undergo incomplete metamorphosis with fewer, more gradual stages.',
   [('What are the four stages of complete metamorphosis?', ['Egg, larva, pupa, and adult', 'Egg, adult, larva, and nymph', 'Larva, egg, nymph, and pupa', 'Adult, egg, and larva only'], 0),
    ('Which insect is a well-known example of complete metamorphosis?', ['Butterfly', 'Grasshopper', 'Cockroach', 'Dragonfly nymph only'], 0),
    ('What stage in complete metamorphosis involves a protective casing?', ['Pupa', 'Egg', 'Larva', 'Adult'], 0),
    ('What is different about incomplete metamorphosis?', ['It has fewer stages and the young resemble smaller versions of adults', 'It always has five stages', 'There is no egg stage', 'The larva looks nothing like the adult'], 0),
    ('Which insect is an example of incomplete metamorphosis?', ['Grasshopper', 'Butterfly', 'Moth', 'Ladybug'], 0)]),
SS('Social Studies: Canadas Boreal Forest — Geography and Importance',
   'Grade 4 Social Studies strand: the boreal forest is a vast forest region stretching across much of northern Canada, providing habitat for wildlife, storing carbon, and supporting industries such as forestry.',
   [('What is the boreal forest?', ['A vast forest region across much of northern Canada', 'A small forest in southern Canada', 'A desert region', 'An underwater ecosystem'], 0),
    ('What kind of trees are common in the boreal forest?', ['Coniferous trees such as spruce and pine', 'Only palm trees', 'Only cactus plants', 'No trees grow there'], 0),
    ('What role does the boreal forest play for wildlife?', ['It provides important habitat for many animal species', 'It has no wildlife', 'It only supports fish', 'It destroys animal habitats'], 0),
    ('Why is the boreal forest important for storing carbon?', ['Its trees and soil absorb and store large amounts of carbon', 'It releases carbon with no absorption', 'It has no effect on carbon levels', 'It only exists to be cut down'], 0),
    ('Which industry commonly operates in the boreal forest?', ['Forestry', 'Fishing exclusively', 'Desert tourism', 'Underwater mining'], 0)]),
]),
day(126, [
L('Vocabulary: Loanwords — Words Borrowed from Other Languages',
  'Grade 4 Language strand: a loanword is a word English has borrowed from another language, such as ballet from French or spaghetti from Italian, enriching English vocabulary.',
  [('What is a loanword?', ['A word borrowed from another language', 'A word with no meaning', 'A type of punctuation mark', 'A word that is always spelled wrong'], 0),
   ('Which word is a loanword borrowed from French?', ['Ballet', 'Table', 'Run', 'Happy'], 0),
   ('Which word is a loanword borrowed from Italian?', ['Spaghetti', 'House', 'Book', 'Tree'], 0),
   ('Why does English contain so many loanwords?', ['English has borrowed words through trade, travel, and cultural contact over time', 'English never changes', 'Loanwords are recent inventions with no history', 'English has no connection to other languages'], 0),
   ('Learning about loanwords can help readers understand ___.', ['How languages influence each other', 'Only math vocabulary', 'Only science vocabulary', 'Nothing useful'], 0)]),
M('Data Management: Using a Venn Diagram to Sort and Compare Data',
  'Grade 4 Math strand: a Venn diagram uses overlapping circles to sort data into categories, showing items that belong to one group, another group, or both.',
  [('What is a Venn diagram used for?', ['Sorting and comparing data using overlapping circles', 'Measuring angles', 'Finding the area of a shape', 'Recording elapsed time'], 0),
   ('What does the overlapping section of a Venn diagram show?', ['Items that belong to both categories', 'Items that belong to neither category', 'The total number of items only', 'Items outside both circles'], 0),
   ('If an item belongs to only one circle in a Venn diagram, what does that mean?', ['It fits only that one category', 'It fits both categories', 'It fits no category', 'It is an error'], 0),
   ('Why are Venn diagrams useful for organizing data?', ['They visually show relationships and overlaps between groups', 'They only work with numbers', 'They cannot show overlapping information', 'They replace the need for any data at all'], 0),
   ('A Venn diagram comparing students who like apples and students who like oranges would place students who like both ___.', ['In the overlapping section', 'Outside both circles', 'In neither circle', 'In a separate diagram'], 0)]),
Sc('Science: Fossil Fuels — Formation, Use, and Environmental Impact',
   'Grade 4 Science strand: fossil fuels such as coal, oil, and natural gas formed over millions of years from ancient organisms and are burned for energy, though their use releases pollution and greenhouse gases.',
   [('What are fossil fuels?', ['Energy sources formed over millions of years from ancient organisms', 'Sources of energy made from sunlight instantly', 'A type of rock with no energy use', 'A renewable energy source'], 0),
    ('Which of these is an example of a fossil fuel?', ['Coal', 'Wind', 'Sunlight', 'Water'], 0),
    ('How long does it take for fossil fuels to form?', ['Millions of years', 'A few days', 'One year', 'A few hours'], 0),
    ('What is one environmental concern with burning fossil fuels?', ['It releases pollution and greenhouse gases', 'It has no environmental effects', 'It cools the planet permanently', 'It creates more fossil fuels instantly'], 0),
    ('Why are fossil fuels considered non-renewable?', ['They take far too long to reform once used up', 'They can be remade in seconds', 'They are unlimited in supply', 'They never run out'], 0)]),
SS('Social Studies: Canadas Mining Industry',
   'Grade 4 Social Studies strand: Canadas mining industry extracts valuable resources such as nickel, gold, and potash from the ground, contributing significantly to the national economy and employment.',
   [('What does the mining industry extract from the ground?', ['Valuable resources such as minerals and metals', 'Only water', 'Only trees', 'Only soil'], 0),
    ('Name one resource commonly mined in Canada.', ['Nickel', 'Bananas', 'Cotton', 'Rice'], 0),
    ('How does mining contribute to Canadas economy?', ['It creates jobs and generates income through resource sales', 'It has no economic impact', 'It only costs money with no benefit', 'It replaces all other industries'], 0),
    ('Why might mining be an important industry in certain Canadian regions?', ['Those regions have rich mineral deposits underground', 'Mining only occurs in cities', 'Mining requires no natural resources', 'All regions have identical resources'], 0),
    ('What is one environmental consideration related to mining?', ['Balancing resource extraction with protecting the environment', 'Mining has no environmental effects', 'Mining always improves the environment', 'Environmental impact is never considered'], 0)]),
]),
day(127, [
L('Writing: Writing an Autobiography',
  'Grade 4 Language strand: an autobiography is a true account of a persons own life written by that person, often organized in chronological order and including important events and reflections.',
  [('What is an autobiography?', ['A true account of a persons life written by that person', 'A fictional story about someone else', 'A biography written by another author', 'A type of poem'], 0),
   ('How are autobiographies usually organized?', ['In chronological order', 'Randomly with no order', 'Backwards from the end to beginning always', 'Alphabetically by topic'], 0),
   ('What point of view is typically used in an autobiography?', ['First person (I, me, my)', 'Third person only', 'Second person only', 'No point of view is used'], 0),
   ('What might an autobiography include besides events?', ['The writers reflections and feelings', 'Only dates and numbers', 'Only pictures with no words', 'Nothing personal at all'], 0),
   ('How is an autobiography different from a biography?', ['An autobiography is written by the subject about themselves, while a biography is written by someone else', 'There is no difference', 'A biography is always fictional', 'An autobiography is always about someone else'], 0)]),
M('Data Management: Expressing Probability as a Percent',
  'Grade 4 Math strand: probability can be expressed as a fraction, decimal, or percent, showing the likelihood of an event, such as a 1/2 chance being expressed as 50%.',
  [('Probability can be expressed as a fraction, decimal, or ___.', ['Percent', 'Ratio only', 'Whole number only', 'Negative number'], 0),
   ('What percent represents a probability of 1/2?', ['50%', '25%', '100%', '10%'], 0),
   ('What percent represents a probability of 1/4?', ['25%', '50%', '75%', '100%'], 0),
   ('If an event is certain to happen, what is its probability as a percent?', ['100%', '0%', '50%', '25%'], 0),
   ('If an event is impossible, what is its probability as a percent?', ['0%', '100%', '50%', '25%'], 0)]),
Sc('Science: The Carbon Cycle — How Carbon Moves Through Earths Systems',
   'Grade 4 Science strand: the carbon cycle describes how carbon moves between the air, plants, animals, oceans, and soil, such as plants absorbing carbon dioxide and animals releasing it through breathing.',
   [('What does the carbon cycle describe?', ['How carbon moves between air, plants, animals, and soil', 'How water moves through clouds only', 'How rocks form over time', 'How electricity flows through circuits'], 0),
    ('What gas do plants absorb from the air as part of the carbon cycle?', ['Carbon dioxide', 'Oxygen only', 'Nitrogen only', 'Helium'], 0),
    ('How do animals release carbon back into the environment?', ['Through breathing out carbon dioxide', 'Through drinking water', 'Through walking', 'Through sleeping'], 0),
    ('Where can carbon be stored for long periods of time?', ['In oceans, soil, and fossil fuels', 'Only in the air', 'Only in animals', 'Nowhere, it disappears'], 0),
    ('Why is the carbon cycle important for life on Earth?', ['It helps regulate the balance of gases that support living things', 'It has no importance to living things', 'It only affects rocks', 'It stops all plant growth'], 0)]),
SS('Social Studies: Canada-United States Trade Relationship',
   'Grade 4 Social Studies strand: Canada and the United States share one of the largest trading relationships in the world, exchanging goods such as vehicles, energy, and agricultural products across the border.',
   [('Canada shares one of the largest trading relationships in the world with which country?', ['The United States', 'Australia', 'Japan', 'Brazil'], 0),
    ('What might Canada and the United States exchange through trade?', ['Vehicles, energy, and agricultural products', 'Only artwork', 'Nothing at all', 'Only historical documents'], 0),
    ('Why is trade between neighbouring countries often significant?', ['Shared borders make transporting goods easier and more efficient', 'Neighbouring countries never trade', 'Distance has no effect on trade', 'Trade only happens between distant countries'], 0),
    ('What is one benefit of strong trade relationships between countries?', ['Access to a wider variety of goods and economic growth', 'Countries lose all their resources', 'Trade always harms both countries', 'No goods are exchanged'], 0),
    ('Trade agreements between countries like Canada and the United States help ___.', ['Set clear rules for how goods are exchanged', 'Prevent any trade from happening', 'Eliminate all industries', 'Stop economic growth'], 0)]),
]),
day(128, [
L('Writing: Writing a Mystery Story',
  'Grade 4 Language strand: a mystery story presents a puzzling problem, such as a crime or disappearance, and follows characters as they gather clues to solve it before a satisfying resolution.',
  [('What is a key feature of a mystery story?', ['A puzzling problem that needs to be solved', 'A recipe for a meal', 'A list of vocabulary words', 'A weather report'], 0),
   ('What do characters in a mystery often gather to solve the problem?', ['Clues', 'Money only', 'Random objects with no purpose', 'Nothing at all'], 0),
   ('Who is often the main character trying to solve the mystery?', ['A detective or curious character', 'A narrator with no role', 'A random stranger never mentioned again', 'The weather'], 0),
   ('What usually happens at the end of a mystery story?', ['The mystery is solved and explained', 'Nothing is ever resolved', 'The story restarts from the beginning', 'All characters disappear'], 0),
   ('Why do writers include red herrings, or misleading clues, in mysteries?', ['To create suspense and mislead readers temporarily', 'To confuse readers with no purpose', 'Red herrings are never used in mysteries', 'To end the story early'], 0)]),
M('Financial Literacy: Calculating Discounts and Sale Prices',
  'Grade 4 Math strand: a discount reduces the original price of an item by a percent, and the sale price is found by subtracting the discount amount from the original price.',
  [('What does a discount do to the original price of an item?', ['Reduces it', 'Increases it', 'Keeps it the same', 'Doubles it'], 0),
   ('If a $20 item has a 10% discount, how much is the discount?', ['$2', '$10', '$18', '$20'], 0),
   ('If a $20 item has a 10% discount, what is the sale price?', ['$18', '$2', '$22', '$10'], 0),
   ('To find the sale price, you should ___.', ['Subtract the discount amount from the original price', 'Add the discount to the original price', 'Multiply the original price by 100', 'Ignore the discount'], 0),
   ('Why might stores offer discounts?', ['To encourage customers to buy items', 'To make prices permanently higher', 'Discounts are never offered', 'To confuse shoppers'], 0)]),
Sc('Science: Alternative Energy — Geothermal and Biomass Power',
   'Grade 4 Science strand: geothermal energy harnesses heat from deep within the Earth, while biomass energy comes from burning organic material such as wood or plant waste, offering renewable alternatives to fossil fuels.',
   [('What is geothermal energy?', ['Energy harnessed from heat within the Earth', 'Energy from ocean waves', 'Energy from the sun only', 'Energy from wind only'], 0),
    ('What is biomass energy made from?', ['Organic material such as wood or plant waste', 'Only sunlight', 'Only metal', 'Only water'], 0),
    ('Why are geothermal and biomass energy considered renewable?', ['Their sources can be naturally replenished over time', 'They come from fossil fuels', 'They cannot be replenished at all', 'They only work for a single day'], 0),
    ('Where does geothermal energy typically come from underground?', ['Heat from deep within the Earth', 'Cold air pockets', 'Frozen ice layers', 'Empty caves with no heat'], 0),
    ('What is one benefit of using alternative energy sources like geothermal and biomass?', ['They can reduce reliance on fossil fuels', 'They always pollute more than fossil fuels', 'They cannot produce electricity', 'They are identical to fossil fuels'], 0)]),
SS('Social Studies: The History of O Canada — Canadas National Anthem',
   'Grade 4 Social Studies strand: O Canada, written in the 19th century, became Canadas official national anthem in 1980 and is sung at ceremonies and events across the country.',
   [('What is the title of Canadas national anthem?', ['O Canada', 'The Maple Leaf Forever', 'God Save the King', 'True North Strong'], 0),
    ('In what century was O Canada originally written?', ['The 19th century', 'The 21st century', 'The 15th century', 'The 10th century'], 0),
    ('In what year did O Canada officially become Canadas national anthem?', ['1980', '1867', '1920', '2000'], 0),
    ('When is O Canada commonly sung?', ['At ceremonies, events, and the start of school days', 'Only during elections', 'Only in courtrooms', 'Never in public settings'], 0),
    ('Why do countries have national anthems?', ['To express national pride and unity', 'To confuse citizens', 'They serve no purpose', 'Only for private use'], 0)]),
]),
day(129, [
L('Writing: Writing a Fable with a Moral',
  'Grade 4 Language strand: a fable is a short story, often featuring animal characters, that teaches a lesson called a moral, such as honesty is the best policy.',
  [('What is a fable?', ['A short story that teaches a lesson', 'A type of poem with no message', 'A factual news report', 'A grammar rule'], 0),
   ('What are fable characters often depicted as?', ['Animals that act like people', 'Only humans', 'Robots', 'Inanimate objects with no personality'], 0),
   ('What is a moral in a fable?', ['The lesson the story teaches', 'The title of the story', 'The setting', 'The main characters name'], 0),
   ('Which is an example of a common fable moral?', ['Honesty is the best policy', 'Numbers can be added together', 'Water boils at 100 degrees', 'Nouns name people, places, or things'], 0),
   ('Why do writers use animal characters in fables?', ['To represent human behaviours and teach lessons in an engaging way', 'Animals cannot be characters in stories', 'To avoid teaching any lesson', 'Animals only appear in nonfiction'], 0)]),
M('Data Management: Interpreting Double Line Graphs',
  'Grade 4 Math strand: a double line graph displays two related sets of data over the same time period using two separate lines, making it easy to compare trends.',
  [('What does a double line graph show?', ['Two related sets of data over the same time period', 'Only one set of data', 'Data with no time period', 'A single point of data'], 0),
   ('Why might someone use a double line graph instead of a single line graph?', ['To compare two trends at once', 'To hide information', 'To show only categories with no numbers', 'Double line graphs cannot be compared'], 0),
   ('What do the two lines in a double line graph usually represent?', ['Two different data sets being compared', 'The same data twice', 'Random unrelated numbers', 'Nothing meaningful'], 0),
   ('If two lines on a graph cross, what does that suggest?', ['The two data sets were equal at that point', 'The graph is incorrect', 'Data cannot cross', 'The lines will never move again'], 0),
   ('Double line graphs are especially useful for comparing ___.', ['Trends over time between two groups', 'Only one number', 'Angles in a shape', 'The area of a rectangle'], 0)]),
Sc('Science: Coral Reefs — Diverse Underwater Ecosystems',
   'Grade 4 Science strand: coral reefs are diverse underwater ecosystems built by tiny animals called coral polyps, providing habitat for a huge variety of ocean life.',
   [('What builds a coral reef?', ['Tiny animals called coral polyps', 'Large fish', 'Ocean currents alone', 'Underwater volcanoes only'], 0),
    ('Why are coral reefs important ecosystems?', ['They provide habitat for a huge variety of ocean life', 'They have no living things', 'They destroy ocean life', 'They only exist on land'], 0),
    ('What conditions do coral reefs typically need to grow?', ['Warm, shallow, clear water', 'Cold, deep, dark water', 'Fresh water only', 'No water at all'], 0),
    ('What is one threat to coral reefs today?', ['Rising ocean temperatures causing coral bleaching', 'Too much cold water', 'Too many fish protecting them', 'Nothing threatens coral reefs'], 0),
    ('Coral reefs are sometimes called the ___ of the sea because of their rich biodiversity.', ['Rainforests', 'Deserts', 'Glaciers', 'Volcanoes'], 0)]),
SS('Social Studies: The Role of Volunteers and Charities in Canadian Communities',
   'Grade 4 Social Studies strand: volunteers and charities support Canadian communities by providing services such as food banks, shelters, and fundraising for causes that governments may not fully cover.',
   [('What do volunteers offer to their communities?', ['Their time and effort to help others without pay', 'Only money with no time given', 'Nothing of value', 'Only government services'], 0),
    ('What is a charity?', ['An organization that raises money or resources to help a cause', 'A government department', 'A type of school', 'A branch of the military'], 0),
    ('Name one service a charity might provide.', ['Operating a food bank', 'Building highways', 'Collecting taxes', 'Running elections'], 0),
    ('Why are volunteers and charities important in a community?', ['They provide support that governments may not fully cover', 'They have no effect on communities', 'They replace all government services', 'They only exist in large cities'], 0),
    ('How can students contribute to their community as volunteers?', ['By helping with local events or fundraising efforts', 'Only by paying taxes', 'By ignoring community needs', 'Students cannot volunteer'], 0)]),
]),
day(130, [
L('Language Review: Grammar, Poetry, and Writing Forms',
  'Grade 4 Language strand review: students revisit comma rules, plural noun rules, prepositional phrases, analyzing poetry, and identifying tone.',
  [('Which sentence uses commas correctly in a series?', ['I packed apples, oranges, and grapes.', 'I packed apples oranges, and grapes.', 'I packed, apples oranges and grapes.', 'I packed apples, oranges and, grapes.'], 0),
   ('What is the plural of dog?', ['Dogs', 'Dogies', 'Doges', 'Dogen'], 0),
   ('What does a prepositional phrase begin with?', ['A preposition', 'A verb', 'A conjunction', 'An adjective'], 0),
   ('What is a stanza?', ['A group of lines in a poem, like a paragraph', 'A single word', 'A type of punctuation', 'The title of a poem'], 0),
   ('What is tone in a piece of writing?', ['The authors attitude toward the subject', 'The setting of the story', 'The main character', 'The title of the text'], 0)]),
M('Math Review: Fractions, Number Sense, and Data',
  'Grade 4 Math strand review: students revisit adding fractions with unlike denominators, square numbers and square roots, divisibility rules, tessellations, and same-perimeter-different-area shapes.',
  [('What must fractions have before they can be added directly?', ['A common denominator', 'The same numerator', 'The same sign', 'Different denominators'], 0),
   ('What is a square number?', ['A number multiplied by itself', 'Any even number', 'A number divided by itself', 'A number added to itself'], 0),
   ('A number is divisible by 3 if ___.', ['The sum of its digits is divisible by 3', 'It ends in 0', 'It ends in an even digit', 'It is a prime number'], 0),
   ('What is a tessellation?', ['A repeating pattern of shapes covering a surface with no gaps or overlaps', 'A single isolated shape', 'A shape with curved sides only', 'A 3D solid figure'], 0),
   ('What does perimeter measure?', ['The distance around a shape', 'The space inside a shape', 'The number of sides only', 'The weight of a shape'], 0)]),
Sc('Science Review: Body Systems, Energy, and Ecosystems',
   'Grade 4 Science strand review: students revisit the digestive system, the skin, the immune system, the five senses, and insect life cycles.',
   [('What is the main job of the digestive system?', ['Breaking down food into nutrients the body can use', 'Pumping blood', 'Sending nerve signals', 'Filtering air'], 0),
    ('What is the skin often described as?', ['The bodys largest organ', 'The smallest organ', 'A type of bone', 'A type of muscle only'], 0),
    ('What is the main job of the immune system?', ['Defending the body against harmful germs', 'Pumping blood through the body', 'Breaking down food', 'Sending messages to muscles'], 0),
    ('How many main senses do humans have?', ['Five', 'Three', 'Seven', 'Two'], 0),
    ('What are the four stages of complete metamorphosis?', ['Egg, larva, pupa, and adult', 'Egg, adult, larva, and nymph', 'Larva, egg, nymph, and pupa', 'Adult, egg, and larva only'], 0)]),
SS('Social Studies Review: Ancient Societies, Government, and Canadian Geography',
   'Grade 4 Social Studies strand review: students revisit ancient Japan, the role of the Prime Minister, the Canadian Coast Guard, Remembrance Day, and the boreal forest.',
   [('What type of geography influenced ancient Japans development?', ['Its island location', 'A vast desert', 'A landlocked plain', 'A mountain range with no coast'], 0),
    ('What is the Prime Minister the head of?', ['The Canadian federal government', 'A single province', 'A city council', 'A private company'], 0),
    ('What does the Canadian Coast Guard help ensure?', ['Safe navigation on Canadas waters', 'Safe travel on highways only', 'Safe air travel only', 'Safe travel through forests'], 0),
    ('On what date is Remembrance Day observed in Canada?', ['November 11', 'July 1', 'December 25', 'October 31'], 0),
    ('What is the boreal forest?', ['A vast forest region across much of northern Canada', 'A small forest in southern Canada', 'A desert region', 'An underwater ecosystem'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_121_130)
    append_to(4, g4_121_130)
