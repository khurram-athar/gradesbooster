#!/usr/bin/env python3
"""Grade 3, Days 101-110 -- extends Grade 3 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade3.json): commas in dates and addresses, suffixes -ful and -less,
text features (bold print and glossary), writing a thank-you note, body
language and tone of voice, plural possessive nouns, making inferences
from illustrations, alliteration, writing a personal narrative (memoir),
rounding to the nearest 1000, comparing fractions with the same numerator,
comparing angles to a right angle, calculating sales tax, introducing
volume with non-standard units, finding the mode of a data set,
multiplying by 0 and 1, the core of a repeating pattern, fair and unfair
games, bird adaptations for flight, ocean habitats, herbivores/carnivores/
omnivores, rainforest ecosystems, mimicry, simple machines in the human
body, complete vs incomplete metamorphosis, groundwater and soil
filtration, fungi, the Niagara Escarpment, Canada’s two official
languages, Ontario’s provincial parks, the Trans-Canada Highway,
emergency services, wind and solar energy projects, air travel and
Ontario’s airports, oral history, and the building of the railway.

Subject keys for Grade 3 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 3 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
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


def _rebalance_answer_positions(days, seed=20260922):
    import random
    rng = random.Random(seed)
    all_quizzes = [quiz for _, subs in days for *_, quiz in subs]
    idx_targets = [i % 4 for i in range(sum(len(quiz) for _, quiz in [(None, q) for q in all_quizzes]))]
    # flatten properly
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


g3_101_110 = [
day(101, [
L('Grammar: Commas in Dates and Addresses',
  'Grade 3 Language strand: commas are used to separate the day and year in a date, and to separate parts of an address, such as a city and province.',
  [('In the date July 22, 2026, where should the comma be placed?', ['Between the day and the year', 'Between the month and the day', 'At the very end', 'Nowhere, dates never use commas'], 0),
   ('Which of these addresses uses a comma correctly?', ['Toronto, Ontario', 'Toronto Ontario,', 'Toronto Ontario', ', Toronto Ontario'], 0),
   ('When writing a full date with a month, day, and year, which two parts are separated by a comma?', ['The day and the year', 'The month and the day', 'The year and itself', 'Commas are never used in dates'], 0),
   ('Why do writers use a comma between a city and a province in an address?', ['To clearly separate the two different pieces of information', 'Commas never belong in an address', 'This concept has no connection to writing', 'A comma changes the meaning of the city name'], 0),
   ('Which sentence uses commas correctly?', ['My birthday is May 3, 2017.', 'My birthday is May, 3 2017.', 'My birthday is May 3 2017,.', 'My birthday is, May 3 2017.'], 0)]),
M('Number: Rounding to the Nearest 1000',
  'Grade 3 Math strand: to round a number to the nearest 1000, look at the hundreds digit -- if it is 5 or more, round up to the next 1000; if it is less than 5, round down.',
  [('Which digit do you look at to round a number to the nearest 1000?', ['The hundreds digit', 'The ones digit', 'The tens digit', 'A concept unrelated to rounding'], 0),
   ('Round 3 621 to the nearest 1000.', ['4 000', '3 000', '3 600', '3 700'], 0),
   ('Round 5 289 to the nearest 1000.', ['5 000', '6 000', '5 300', '5 900'], 0),
   ('Round 7 950 to the nearest 1000.', ['8 000', '7 000', '7 900', '8 100'], 0),
   ('Why is rounding to the nearest 1000 useful when working with large numbers?', ['It gives a quick, simpler estimate that is easier to work with', 'Rounding never makes large numbers easier to understand', 'This concept has no connection to number sense', 'Rounding always gives the exact same number you started with'], 0)]),
Sc('Science: Bird Adaptations for Flight',
   'Grade 3 Science strand: birds have special adaptations for flight, such as lightweight hollow bones, feathers, and strong wing muscles, that help them fly efficiently.',
   [('What kind of bones do birds have that help them fly?', ['Lightweight hollow bones', 'Heavy solid bones', 'A concept unrelated to birds', 'No bones at all'], 0),
    ('What covers a bird’s body and helps it fly?', ['Feathers', 'Fur', 'Scales', 'A concept unrelated to birds'], 0),
    ('What do birds need strong muscles for, besides walking?', ['Flapping their wings to fly', 'A concept unrelated to birds', 'Swimming underwater only', 'Digging burrows'], 0),
    ('Why do hollow bones help birds fly more easily?', ['They make a bird’s body lighter, which makes flying easier', 'Hollow bones make a bird’s body much heavier', 'This concept has no connection to flight', 'Hollow bones have no effect on a bird’s weight'], 0),
    ('Why might a bird’s wing shape affect how well it can fly?', ['Different wing shapes help birds fly in different ways, such as gliding or quick turns', 'Wing shape never affects how a bird flies', 'This concept has no connection to bird adaptations', 'All birds have the exact same wing shape'], 0)]),
SS('Social Studies: The Niagara Escarpment — A Unique Ontario Landform',
   'Grade 3 Social Studies strand: the Niagara Escarpment is a long, rocky ridge that stretches across parts of Ontario, providing habitats for many plants and animals and including well-known sites such as Niagara Falls.',
   [('What do we call a long, rocky ridge of land such as the Niagara Escarpment?', ['A landform', 'A concept unrelated to geography', 'A type of government', 'A type of currency'], 0),
    ('Does the Niagara Escarpment provide habitats for plants and animals?', ['Yes', 'No, nothing lives on the Niagara Escarpment', 'A concept unrelated to Ontario’s geography', 'Only fish live there'], 0),
    ('Which well-known waterfall is connected to the Niagara Escarpment?', ['Niagara Falls', 'A concept unrelated to Ontario landmarks', 'A waterfall in another country only', 'No waterfall is connected to it'], 0),
    ('Why might the Niagara Escarpment be an important area to protect?', ['It provides habitat for many species and includes unique natural features', 'The Niagara Escarpment has no connection to Ontario’s environment', 'This concept has no relevance to Ontario’s geography', 'Protecting landforms is never important'], 0),
    ('Why is the Niagara Escarpment considered a special landform in Ontario?', ['It stretches a long distance and includes unique rock formations and habitats not found everywhere', 'It is exactly the same as every other piece of land in Ontario', 'This concept has no relevance to Ontario’s geography', 'The Niagara Escarpment does not actually exist in Ontario'], 0)]),
]),

day(102, [
L('Vocabulary: Suffixes -ful and -less',
  'Grade 3 Language strand: the suffix -ful means full of, as in joyful, while the suffix -less means without, as in fearless.',
  [('What does the suffix -ful mean?', ['Full of', 'Without', 'Before', 'After'], 0),
   ('What does the suffix -less mean?', ['Without', 'Full of', 'Again', 'Not yet'], 0),
   ('What does the word fearless mean?', ['Without fear', 'Full of fear', 'A concept unrelated to suffixes', 'Before fear'], 0),
   ('What does the word joyful mean?', ['Full of joy', 'Without joy', 'A concept unrelated to suffixes', 'After joy'], 0),
   ('Why is it helpful to know that -ful means full of and -less means without?', ['It helps you figure out the meaning of new words that use these suffixes', 'These suffixes never change a word’s meaning', 'This concept has no connection to vocabulary', 'All words ending in -ful or -less mean the same thing'], 0)]),
M('Fractions: Comparing Fractions with the Same Numerator',
  'Grade 3 Math strand: when two fractions have the same numerator, the fraction with the smaller denominator is greater, because the whole is divided into fewer, larger pieces.',
  [('Which fraction is greater: 1/3 or 1/5?', ['1/3', '1/5', 'They are equal', 'Cannot tell'], 0),
   ('Which fraction is greater: 2/4 or 2/6?', ['2/4', '2/6', 'They are equal', 'Cannot tell'], 0),
   ('When two fractions have the same numerator, which one is larger?', ['The one with the smaller denominator', 'The one with the larger denominator', 'They are always equal', 'A concept unrelated to fractions'], 0),
   ('Which fraction is greater: 3/8 or 3/10?', ['3/8', '3/10', 'They are equal', 'Cannot tell'], 0),
   ('Why is 1/4 greater than 1/8 even though 8 is a bigger number than 4?', ['A whole divided into 4 pieces makes each piece bigger than a whole divided into 8 pieces', '1/4 and 1/8 are always exactly equal', 'This concept has no connection to fractions', 'A bigger denominator always means a bigger fraction'], 0)]),
Sc('Science: Ocean Habitats and Life in the Open Sea',
   'Grade 3 Science strand: the open ocean is a vast saltwater habitat where organisms such as fish, whales, and plankton live at different depths, each adapted to its own conditions.',
   [('Is ocean water salt water or fresh water?', ['Salt water', 'Fresh water', 'A concept unrelated to oceans', 'Neither salt nor fresh water'], 0),
    ('Name one animal that lives in the open ocean, such as a ___.', ['Whale', 'A concept unrelated to oceans', 'A desert lizard', 'A forest owl'], 0),
    ('What do we call the tiny floating organisms that many ocean animals eat?', ['Plankton', 'Coral', 'A concept unrelated to oceans', 'Seaweed only'], 0),
    ('Why might ocean animals be adapted to living at different depths of water?', ['Conditions like light and pressure change at different depths, so animals adapt to survive there', 'Every part of the ocean has the exact same conditions', 'This concept has no connection to ocean habitats', 'Depth never affects where an ocean animal can live'], 0),
    ('Why is the open ocean considered a huge habitat?', ['It covers a large area and supports many different kinds of living things', 'The open ocean supports no living things at all', 'This concept has no relevance to habitats', 'The open ocean is smaller than a single lake'], 0)]),
SS('Social Studies: Canada’s Two Official Languages — English and French',
   'Grade 3 Social Studies strand: Canada has two official languages, English and French, meaning federal government services must be offered in both languages across the country.',
   [('What are Canada’s two official languages?', ['English and French', 'English and Spanish', 'A concept unrelated to Canada', 'French and German'], 0),
    ('Must federal government services in Canada be offered in both official languages?', ['Yes', 'No, only in English', 'A concept unrelated to Canada’s government', 'Only in French'], 0),
    ('What word describes a country, like Canada, that has two official languages?', ['Bilingual', 'Monolingual', 'A concept unrelated to language', 'Multilingual'], 0),
    ('Why does Canada have two official languages instead of just one?', ['It reflects the country’s history with English- and French-speaking communities', 'Canada has never had any connection to the French language', 'This concept has no relevance to Canadian identity', 'Only one language has ever been spoken in Canada'], 0),
    ('Why might a federal government office in Ottawa print documents in both English and French?', ['So that all citizens can access information in an official language they understand', 'Printing documents in two languages is never useful', 'This concept has no connection to Canada’s official languages', 'Only English speakers are allowed to access government documents'], 0)]),
]),

day(103, [
L('Reading: Text Features — Bold Print and Glossary',
  'Grade 3 Language strand: bold print highlights important words in a non-fiction text, and a glossary at the back of the book explains what those words mean.',
  [('What do we call print that is darker and thicker than the rest of the text?', ['Bold print', 'Italics', 'A footnote', 'A caption'], 0),
   ('Where would you look to find the meaning of a bold word in a book?', ['The glossary', 'The cover', 'The table of contents', 'A concept unrelated to text features'], 0),
   ('Where is a glossary usually found in a book?', ['At the back', 'At the front', 'In the middle only', 'A concept unrelated to books'], 0),
   ('Why might an author use bold print for certain words in a text?', ['To show the reader that those words are especially important', 'Bold print never highlights anything important', 'This concept has no connection to reading non-fiction', 'Bold print is only ever used by accident'], 0),
   ('Why is a glossary a useful text feature for readers?', ['It explains the meaning of difficult or important words in the book', 'A glossary never explains any words', 'This concept has no connection to text features', 'A glossary is always identical to the index'], 0)]),
M('Geometry: Comparing Angles to a Right Angle',
  'Grade 3 Math strand: an angle can be described as smaller than, equal to, or greater than a right angle -- angles smaller than a right angle are acute, and angles greater than a right angle are obtuse.',
  [('What do we call an angle that is exactly the same size as a right angle?', ['A right angle', 'An acute angle', 'An obtuse angle', 'A concept unrelated to angles'], 0),
   ('What do we call an angle that is smaller than a right angle?', ['An acute angle', 'An obtuse angle', 'A right angle', 'A concept unrelated to angles'], 0),
   ('What do we call an angle that is greater than a right angle?', ['An obtuse angle', 'An acute angle', 'A right angle', 'A concept unrelated to angles'], 0),
   ('A right angle looks like the corner of a ___.', ['Square', 'Circle', 'A concept unrelated to angles', 'Cone'], 0),
   ('Why is comparing an angle to a right angle a useful way to describe it?', ['A right angle is an easy, familiar reference for judging whether other angles are smaller or larger', 'Right angles are never useful for comparing shapes', 'This concept has no connection to geometry', 'All angles are always exactly the same size'], 0)]),
Sc('Science: Herbivores, Carnivores, and Omnivores',
   'Grade 3 Science strand: animals can be classified by what they eat -- herbivores eat only plants, carnivores eat only other animals, and omnivores eat both plants and animals.',
   [('What do we call an animal that eats only plants?', ['A herbivore', 'A carnivore', 'An omnivore', 'A concept unrelated to animal diets'], 0),
    ('What do we call an animal that eats only other animals?', ['A carnivore', 'A herbivore', 'An omnivore', 'A concept unrelated to animal diets'], 0),
    ('What do we call an animal that eats both plants and animals?', ['An omnivore', 'A herbivore', 'A carnivore', 'A concept unrelated to animal diets'], 0),
    ('Is a rabbit, which eats only plants, a herbivore or a carnivore?', ['A herbivore', 'A carnivore', 'An omnivore', 'A concept unrelated to animal diets'], 0),
    ('Why is classifying animals by their diet useful to scientists?', ['It helps scientists understand an animal’s role in its ecosystem and food chain', 'An animal’s diet has no connection to its role in an ecosystem', 'This concept has no relevance to classifying animals', 'All animals eat exactly the same things'], 0)]),
SS('Social Studies: Ontario’s Provincial Parks and Conservation Areas',
   'Grade 3 Social Studies strand: Ontario has many provincial parks and conservation areas that protect natural habitats while offering people places to camp, hike, and learn about nature.',
   [('What is one purpose of a provincial park?', ['To protect natural habitats', 'To build more factories', 'A concept unrelated to conservation', 'To remove all trees and plants'], 0),
    ('Name one activity people might do in a provincial park.', ['Hiking', 'A concept unrelated to parks', 'Filing taxes', 'Voting in an election'], 0),
    ('Do provincial parks help protect wildlife habitats?', ['Yes', 'No, provincial parks harm all wildlife', 'A concept unrelated to conservation', 'Provincial parks have no habitats at all'], 0),
    ('Why might Ontario set aside land as protected provincial parks instead of allowing all land to be developed?', ['To preserve natural habitats and give people a place to enjoy nature', 'Protecting land is never beneficial to a province', 'This concept has no relevance to conservation', 'Provincial parks serve no purpose at all'], 0),
    ('Why are conservation areas important for future generations?', ['They help make sure natural spaces and wildlife are protected for people to enjoy in the future', 'Conservation areas have no connection to future generations', 'This concept has no relevance to Ontario’s environment', 'Protecting nature today has no effect on the future'], 0)]),
]),

day(104, [
L('Writing: Writing a Thank-You Note',
  'Grade 3 Language strand: a thank-you note is a short, polite piece of writing that names the gift or favour, explains why the writer is grateful, and includes a friendly closing.',
  [('What is the purpose of a thank-you note?', ['To politely express gratitude for a gift or favour', 'To ask someone a question', 'A concept unrelated to writing', 'To complain about something'], 0),
   ('What should a thank-you note usually name?', ['The gift or favour received', 'A concept unrelated to thank-you notes', 'A math problem', 'The weather'], 0),
   ('Which of these is a friendly closing you might use at the end of a thank-you note?', ['Sincerely, Maya', 'A concept unrelated to closings', '4 + 4 = 8', 'The end'], 0),
   ('Why is it important to explain why you are grateful in a thank-you note?', ['It shows the other person that their gift or favour truly mattered to you', 'Explaining your gratitude never matters', 'This concept has no connection to writing a thank-you note', 'A thank-you note should never mention the gift'], 0),
   ('Which sentence would fit well in a thank-you note?', ['Thank you for the book — I loved reading it!', 'Add 5 and 3 to get 8.', 'A triangle has three sides.', 'The water cycle has several stages.'], 0)]),
M('Financial Literacy: Calculating Sales Tax on Purchases',
  'Grade 3 Math strand: sales tax is a small extra amount added to the price of many goods and services, and shoppers can estimate the total cost by adding the tax to the price.',
  [('What do we call the extra amount added to the price of many purchases?', ['Sales tax', 'A concept unrelated to shopping', 'A discount', 'A refund'], 0),
   ('If an item costs 10 dollars and the tax adds 1 dollar, what is the total cost?', ['11 dollars', '9 dollars', '10 dollars', '12 dollars'], 0),
   ('Is sales tax added before or after the price of an item?', ['After (it is added to the price)', 'Before (it is subtracted from the price)', 'A concept unrelated to sales tax', 'Sales tax is never related to price'], 0),
   ('If an item costs 5 dollars and the tax adds 65 cents, about how much will you pay in total?', ['About 5 dollars and 65 cents', 'About 4 dollars', 'About 6 dollars and 65 cents', 'Exactly 5 dollars'], 0),
   ('Why is it useful to estimate the total cost, including tax, before buying something?', ['It helps you make sure you have enough money to pay for the item', 'Estimating the total cost is never useful', 'This concept has no connection to financial literacy', 'Sales tax never actually changes the total you pay'], 0)]),
Sc('Science: Rainforest Ecosystems and Biodiversity',
   'Grade 3 Science strand: rainforests are warm, wet ecosystems with tall trees and dense plant growth that support an extremely high biodiversity, or variety of living things.',
   [('What kind of climate does a rainforest usually have?', ['Warm and wet', 'Cold and dry', 'A concept unrelated to rainforests', 'Cold and wet'], 0),
    ('What word describes the huge variety of living things found in a rainforest?', ['Biodiversity', 'A concept unrelated to ecosystems', 'Uniformity', 'Scarcity'], 0),
    ('Do rainforests usually have tall trees and dense plant growth?', ['Yes', 'No, rainforests have no plants', 'A concept unrelated to rainforests', 'Rainforests only have short grass'], 0),
    ('Why do rainforests support such a high biodiversity of plants and animals?', ['Their warm, wet climate provides ideal conditions for many species to thrive', 'Rainforests provide the worst possible conditions for living things', 'This concept has no connection to biodiversity', 'Rainforests never actually support any living things'], 0),
    ('Why is protecting rainforests important for the whole planet?', ['Rainforests are home to a huge number of species and help regulate the Earth’s climate', 'Rainforests have no effect on the rest of the planet', 'This concept has no relevance to ecosystems', 'Protecting rainforests has never been considered important'], 0)]),
SS('Social Studies: The Trans-Canada Highway and Travel Across the Country',
   'Grade 3 Social Studies strand: the Trans-Canada Highway is a long road system that connects communities across the entire country, making it possible to travel by car from coast to coast.',
   [('What is the Trans-Canada Highway?', ['A long road system connecting communities across Canada', 'A type of railway', 'A concept unrelated to transportation', 'A waterway used only by boats'], 0),
    ('Does the Trans-Canada Highway connect communities from coast to coast?', ['Yes', 'No, it only connects two cities', 'A concept unrelated to transportation', 'It exists in only one province'], 0),
    ('What kind of vehicles mainly use the Trans-Canada Highway?', ['Cars and trucks', 'Boats', 'A concept unrelated to transportation', 'Airplanes'], 0),
    ('Why is the Trans-Canada Highway important for connecting communities?', ['It allows people and goods to travel by road across long distances between provinces', 'The Trans-Canada Highway has no connection to travel', 'This concept has no relevance to Canadian communities', 'It only connects communities within one single city'], 0),
    ('Why might a trucking company rely on the Trans-Canada Highway to deliver goods?', ['It provides a direct road route to transport goods to communities across the country', 'Trucking companies never use highways to deliver goods', 'This concept has no connection to trade and transportation', 'The Trans-Canada Highway does not allow trucks to use it'], 0)]),
]),

day(105, [
L('Oral Communication: Understanding Body Language and Tone of Voice',
  'Grade 3 Language strand: listeners can understand a speaker’s feelings not just from their words, but also from body language, such as facial expressions and gestures, and tone of voice.',
  [('What do we call the way a speaker uses their face and gestures to communicate?', ['Body language', 'A concept unrelated to communication', 'A glossary', 'A footnote'], 0),
   ('What do we call how a speaker’s voice sounds, such as happy or angry?', ['Tone of voice', 'A concept unrelated to communication', 'A caption', 'A table of contents'], 0),
   ('If a speaker crosses their arms and frowns, what might this body language suggest?', ['That they feel upset or unhappy', 'That they feel excited and joyful', 'A concept unrelated to body language', 'Nothing at all'], 0),
   ('Why is it useful to pay attention to a speaker’s tone of voice, not just their words?', ['Tone of voice can reveal feelings that the words alone might not show', 'Tone of voice never adds any meaning to speech', 'This concept has no connection to oral communication', 'Words always mean the exact same thing no matter the tone'], 0),
   ('Which of these is an example of positive body language while listening?', ['Nodding and making eye contact', 'Turning away and looking at the floor', 'Talking over the speaker', 'Walking out of the room'], 0)]),
M('Measurement: Introducing Volume with Non-Standard Units',
  'Grade 3 Math strand: volume is the amount of space an object takes up, and students can compare and measure volume using non-standard units, such as counting how many small cubes fill a container.',
  [('What do we call the amount of space an object takes up?', ['Volume', 'Perimeter', 'Area', 'A concept unrelated to measurement'], 0),
   ('Which of these could be used as a non-standard unit to measure volume?', ['Small cubes', 'A concept unrelated to measurement', 'A calendar', 'A thermometer'], 0),
   ('If it takes 12 small cubes to fill Box A and 20 small cubes to fill Box B, which box has a greater volume?', ['Box B', 'Box A', 'They have equal volume', 'Cannot tell'], 0),
   ('Why might you count how many cubes fit inside a container to measure its volume?', ['It shows how much space is inside the container', 'Counting cubes never tells you anything about volume', 'This concept has no connection to measurement', 'Cubes can only be used to measure length'], 0),
   ('Why is it useful to compare volume using the same-sized unit each time?', ['It makes the comparison fair and accurate between different containers', 'Using the same-sized unit is never useful', 'This concept has no connection to measuring volume', 'Different-sized units always give the exact same result'], 0)]),
Sc('Science: Mimicry in the Animal Kingdom',
   'Grade 3 Science strand: mimicry is an adaptation in which one species evolves to look like another species, often to avoid being eaten by predators.',
   [('What do we call it when one species evolves to look like another species?', ['Mimicry', 'Camouflage', 'A concept unrelated to adaptations', 'Hibernation'], 0),
    ('Why might a harmless insect evolve to look like a dangerous, stinging insect?', ['To trick predators into leaving it alone', 'To attract more predators', 'A concept unrelated to mimicry', 'It has no effect on predators at all'], 0),
    ('Is mimicry an example of an adaptation that helps an animal survive?', ['Yes', 'No, mimicry never helps an animal survive', 'A concept unrelated to adaptations', 'Mimicry always harms the animal that uses it'], 0),
    ('What is the main difference between mimicry and camouflage?', ['Mimicry means looking like another species, while camouflage means blending into the surroundings', 'Mimicry and camouflage always mean the exact same thing', 'This concept has no connection to animal adaptations', 'Camouflage means looking like another species'], 0),
    ('Why is mimicry considered a helpful survival adaptation?', ['It can fool predators into avoiding an animal that is actually harmless', 'Mimicry never affects whether a predator attacks an animal', 'This concept has no relevance to survival', 'Mimicry always makes an animal easier for predators to catch'], 0)]),
SS('Social Studies: Emergency Services That Keep Communities Safe',
   'Grade 3 Social Studies strand: emergency services, such as police, firefighters, and paramedics, respond quickly to keep people safe during emergencies in their community.',
   [('Name one type of emergency service, such as ___.', ['Firefighters', 'A concept unrelated to emergency services', 'A librarian', 'A cashier'], 0),
    ('What is the main job of paramedics?', ['To provide emergency medical care', 'To fix roads', 'A concept unrelated to emergency services', 'To teach students'], 0),
    ('What number can people in Canada call in an emergency to reach police, fire, or paramedics?', ['911', 'A concept unrelated to emergency services', '123', '555'], 0),
    ('Why do communities need emergency services to be able to respond quickly?', ['Fast responses can help protect people’s safety and even save lives', 'Emergency services never need to respond quickly', 'This concept has no relevance to community safety', 'Emergencies never require any kind of help'], 0),
    ('Why might a community train many different kinds of emergency responders, such as police, firefighters, and paramedics?', ['Different emergencies need different kinds of help and expertise', 'Every emergency requires the exact same kind of help', 'This concept has no connection to community safety', 'Communities never actually need emergency responders'], 0)]),
]),

day(106, [
L('Grammar: Plural Possessive Nouns',
  'Grade 3 Language strand: a plural possessive noun shows that something belongs to more than one owner, usually formed by adding an apostrophe after the -s, as in the dogs’ bones.',
  [('How do you usually form a possessive noun for a plural noun that already ends in -s?', ['Add an apostrophe after the s', 'Add an apostrophe and another s', 'Add -ing', 'A concept unrelated to grammar'], 0),
   ('Which of these correctly shows that a ball belongs to more than one girl?', ['The girls’ ball', 'The girl’s ball', 'The girls’s ball', 'Girls ball'], 0),
   ('In the phrase the dogs’ bones, how many dogs own the bones?', ['More than one dog', 'Exactly one dog', 'A concept unrelated to grammar', 'No dogs at all'], 0),
   ('Why does the apostrophe placement change between a singular and a plural possessive noun?', ['It shows whether one owner or more than one owner possesses something', 'Apostrophe placement never changes for possessive nouns', 'This concept has no connection to grammar', 'Plural possessive nouns never actually use an apostrophe'], 0),
   ('Which sentence correctly shows that a toy belongs to more than one child?', ['The children’s toy was on the floor.', 'The childs’ toy was on the floor.', 'The child’s toy belongs to many children.', 'The childrens toy was on the floor.'], 0)]),
M('Data: Finding the Mode of a Data Set',
  'Grade 3 Math strand: the mode of a data set is the value that appears most often, which can help describe what is most common or typical in a set of data.',
  [('What do we call the value that appears most often in a data set?', ['The mode', 'The range', 'A concept unrelated to data', 'The total'], 0),
   ('In the data set 2, 3, 3, 5, 3, 7, what is the mode?', ['3', '5', '7', '2'], 0),
   ('In the data set 4, 4, 6, 8, 8, 8, what is the mode?', ['8', '4', '6', 'There is no mode'], 0),
   ('If every value in a data set appears exactly once, does the data set have a mode?', ['No, there is no mode', 'Yes, the mode is the first number', 'Yes, the mode is the last number', 'A concept unrelated to data'], 0),
   ('Why is the mode a useful piece of information about a data set?', ['It shows which value is the most common or popular in the data', 'The mode never tells us anything useful about data', 'This concept has no connection to data management', 'The mode is always the same as the total of all the numbers'], 0)]),
Sc('Science: How Our Bodies Use Simple Machines',
   'Grade 3 Science strand: the human body uses simple machines, such as levers, in everyday movement -- for example, the arm acts like a lever when bending at the elbow to lift something.',
   [('What simple machine does your arm act like when you bend it to lift something?', ['A lever', 'A pulley', 'A wheel-and-axle', 'A concept unrelated to simple machines'], 0),
    ('What body part acts as the pivot point, or fulcrum, when your arm bends like a lever?', ['The elbow', 'The fingertip', 'A concept unrelated to the body', 'The hair'], 0),
    ('Which simple machine can be compared to the way your jaw works when you bite and chew?', ['A lever', 'A wheel-and-axle', 'A pulley', 'A concept unrelated to simple machines'], 0),
    ('Why is it useful to compare parts of the human body to simple machines?', ['It helps us understand how our bodies use force to move and do work', 'Comparing the body to machines never helps us understand movement', 'This concept has no connection to simple machines', 'The human body never actually uses any force to move'], 0),
    ('Why might understanding your arm as a lever help you lift objects more easily?', ['It can help you understand how bending your elbow changes the force needed to lift something', 'Understanding levers never helps with lifting objects', 'This concept has no relevance to simple machines', 'Levers always make lifting an object more difficult'], 0)]),
SS('Social Studies: Wind and Solar Energy Projects in Ontario',
   'Grade 3 Social Studies strand: Ontario uses natural resources like wind and sunlight to generate renewable energy, building wind turbines and solar panels that provide power to communities.',
   [('Name one natural resource used to generate renewable energy in Ontario.', ['Wind', 'A concept unrelated to energy', 'Plastic', 'Concrete'], 0),
    ('What structure captures wind to generate electricity?', ['A wind turbine', 'A concept unrelated to energy', 'A library', 'A bridge'], 0),
    ('What captures sunlight to generate electricity?', ['A solar panel', 'A concept unrelated to energy', 'A garbage truck', 'A subway train'], 0),
    ('Why might Ontario communities build wind and solar energy projects?', ['To generate power using renewable resources instead of resources that can run out', 'Wind and solar energy projects have no benefit to communities', 'This concept has no relevance to natural resources', 'Ontario has no access to wind or sunlight'], 0),
    ('Why is renewable energy, like wind and solar power, valuable for the future?', ['It can be used again and again without running out, unlike some other resources', 'Renewable energy runs out permanently after a single use', 'This concept has no relevance to Ontario’s resources', 'Renewable energy has no connection to the future'], 0)]),
]),

day(107, [
L('Reading: Making Inferences from Illustrations',
  'Grade 3 Language strand: readers can make inferences, or educated guesses, about a story by looking closely at illustrations and combining clues from the pictures with the words in the text.',
  [('What do we call an educated guess based on clues in a text or picture?', ['An inference', 'A concept unrelated to reading', 'A glossary', 'A footnote'], 0),
   ('What can readers use, besides the words, to help make an inference about a story?', ['Illustrations', 'A concept unrelated to reading', 'The back cover price', 'The publisher’s name'], 0),
   ('If an illustration shows a character smiling and holding a trophy, what might you infer about how the character feels?', ['That the character feels proud or happy', 'That the character feels sad', 'A concept unrelated to inferences', 'That the character feels nothing at all'], 0),
   ('Why might a reader look closely at an illustration instead of just reading the words?', ['Illustrations can give extra clues about characters, setting, and mood', 'Illustrations never add extra information to a story', 'This concept has no connection to reading comprehension', 'Words always tell you everything a picture shows'], 0),
   ('Why is making inferences an important reading skill?', ['It helps readers understand ideas that are not directly stated in the text', 'Making inferences is never useful while reading', 'This concept has no connection to reading strategies', 'Every detail in a story is always stated directly'], 0)]),
M('Multiplication: Properties of Multiplying by 0 and 1',
  'Grade 3 Math strand: any number multiplied by 1 stays the same, and any number multiplied by 0 equals 0 -- these are called the identity property and the zero property of multiplication.',
  [('What is 7 multiplied by 1?', ['7', '0', '8', '1'], 0),
   ('What is 9 multiplied by 0?', ['0', '9', '1', '90'], 0),
   ('What do we call the rule that any number times 1 equals that same number?', ['The identity property of multiplication', 'The zero property of multiplication', 'A concept unrelated to multiplication', 'The distributive property'], 0),
   ('What do we call the rule that any number times 0 equals 0?', ['The zero property of multiplication', 'The identity property of multiplication', 'A concept unrelated to multiplication', 'The commutative property'], 0),
   ('Why does multiplying any number by 0 always give a result of 0?', ['Multiplying by 0 means taking that number zero times, leaving nothing', 'Multiplying by 0 always doubles the original number', 'This concept has no connection to multiplication', 'Multiplying by 0 always gives the exact same number you started with'], 0)]),
Sc('Science: Complete vs Incomplete Metamorphosis in Insects',
   'Grade 3 Science strand: insects such as butterflies undergo complete metamorphosis with four distinct stages, while insects such as grasshoppers undergo incomplete metamorphosis, which has fewer, less dramatic stages.',
   [('How many main stages does complete metamorphosis have?', ['Four', 'Two', 'Three', 'Five'], 0),
    ('Which insect is an example of complete metamorphosis, going through a pupa stage?', ['A butterfly', 'A grasshopper', 'A concept unrelated to metamorphosis', 'Neither insect changes at all'], 0),
    ('Which insect is an example of incomplete metamorphosis, without a pupa stage?', ['A grasshopper', 'A butterfly', 'A concept unrelated to metamorphosis', 'Neither insect changes at all'], 0),
    ('What is the main difference between complete and incomplete metamorphosis?', ['Complete metamorphosis includes a pupa stage with dramatic change, while incomplete metamorphosis does not', 'Complete and incomplete metamorphosis are always exactly the same', 'This concept has no connection to insect life cycles', 'Incomplete metamorphosis always has more stages than complete metamorphosis'], 0),
    ('Why do young grasshoppers already look similar to adult grasshoppers?', ['Because they go through incomplete metamorphosis, with gradual changes instead of a dramatic pupa stage', 'Grasshoppers actually go through complete metamorphosis like butterflies', 'This concept has no relevance to insect life cycles', 'Young grasshoppers never resemble adult grasshoppers at all'], 0)]),
SS('Social Studies: Air Travel and Ontario’s Airports',
   'Grade 3 Social Studies strand: airports in Ontario, such as Toronto Pearson, connect the province to destinations across Canada and around the world, supporting travel and trade.',
   [('Name one large airport located in Ontario.', ['Toronto Pearson', 'A concept unrelated to airports', 'A bus terminal', 'A subway station'], 0),
    ('What can airports help transport, besides passengers?', ['Cargo and goods', 'A concept unrelated to airports', 'Only letters', 'Nothing else'], 0),
    ('Do Ontario’s airports connect the province to places around the world?', ['Yes', 'No, airports never connect places', 'A concept unrelated to travel', 'Airports only connect one single city'], 0),
    ('Why are airports important for Ontario’s economy?', ['They support travel and trade by connecting Ontario to other places quickly', 'Airports have no connection to Ontario’s economy', 'This concept has no relevance to transportation', 'Airports only exist for entertainment purposes'], 0),
    ('Why might air travel be faster than other forms of transportation for long distances?', ['Airplanes can travel very quickly through the sky, covering long distances in less time', 'Air travel is always slower than travelling by car', 'This concept has no connection to transportation', 'Airplanes cannot travel long distances'], 0)]),
]),

day(108, [
L('Vocabulary: Alliteration',
  'Grade 3 Language strand: alliteration is the repetition of the same beginning consonant sound in a series of nearby words, such as slippery silver snakes slithered.',
  [('What do we call the repetition of the same beginning sound in nearby words?', ['Alliteration', 'A concept unrelated to vocabulary', 'A homograph', 'A synonym'], 0),
   ('Which of these phrases is an example of alliteration?', ['Big blue balloons bounced', 'The sky is blue', 'A concept unrelated to alliteration', 'The cat sat on the mat'], 0),
   ('Which sound repeats in the phrase Peter Piper picked peppers?', ['The P sound', 'The S sound', 'A concept unrelated to alliteration', 'The M sound'], 0),
   ('Why might an author use alliteration in a poem or story?', ['To create a fun, rhythmic sound that catches the reader’s attention', 'Alliteration never adds anything to a piece of writing', 'This concept has no connection to an author’s craft', 'Alliteration always makes a sentence harder to understand'], 0),
   ('Which of these sentences uses alliteration?', ['Sammy the snake slithered silently.', 'Sammy the snake moved quietly.', 'The snake was long and green.', 'A snake has no legs.'], 0)]),
M('Patterning: Identifying the Core of a Repeating Pattern',
  'Grade 3 Math strand: the core of a repeating pattern is the smallest part that repeats over and over, such as the red, blue core in the pattern red, blue, red, blue.',
  [('What do we call the smallest part of a pattern that repeats over and over?', ['The core', 'The rule', 'A concept unrelated to patterning', 'The total'], 0),
   ('What is the core of the pattern red, blue, red, blue, red, blue?', ['Red, blue', 'Red, blue, red', 'Blue, red, blue', 'Red only'], 0),
   ('What is the core of the pattern 2, 4, 6, 2, 4, 6, 2, 4, 6?', ['2, 4, 6', '2, 4', '4, 6', '6, 2'], 0),
   ('If a pattern’s core is triangle, square, circle, what shape comes next after ...circle, triangle, square, circle, ___?', ['Triangle', 'Square', 'Circle', 'A concept unrelated to patterning'], 0),
   ('Why is identifying the core of a pattern useful for predicting what comes next?', ['Once you know the core, you can repeat it to extend the pattern', 'Identifying the core never helps predict a pattern', 'This concept has no connection to patterning', 'Every pattern has a completely different core each time it repeats'], 0)]),
Sc('Science: Groundwater and How Soil Filters Water',
   'Grade 3 Science strand (Soils in the Environment): as rain seeps into the ground, soil filters the water, and it collects underground in spaces between soil and rock particles, forming groundwater.',
   [('What do we call water that collects underground in the spaces between soil and rock?', ['Groundwater', 'A concept unrelated to soil', 'Rainwater on the surface', 'Ocean water'], 0),
    ('What happens to rainwater as it seeps down through layers of soil?', ['The soil filters it', 'The soil turns it into a solid', 'A concept unrelated to soil', 'Nothing happens to it at all'], 0),
    ('Does soil play a role in cleaning water as it moves underground?', ['Yes', 'No, soil never affects water quality', 'A concept unrelated to soil', 'Soil only makes water dirtier'], 0),
    ('Why might sandy soil allow water to soak through more quickly than clay soil?', ['Sandy soil has larger spaces between particles, letting water pass through more easily', 'Sandy soil and clay soil always let water pass through at the exact same rate', 'This concept has no connection to soil properties', 'Clay soil always lets water pass through fastest'], 0),
    ('Why is groundwater an important resource for many communities?', ['Many communities pump groundwater from wells to use as drinking water', 'Groundwater is never used by any community', 'This concept has no relevance to soils in the environment', 'Groundwater only exists in the ocean'], 0)]),
SS('Social Studies: Oral History — Learning from Elders and Storytellers',
   'Grade 3 Social Studies strand: oral history is knowledge and stories passed down by speaking rather than writing, and many communities, including Indigenous communities, use storytelling from elders to preserve their history and traditions.',
   [('What do we call history and knowledge that is passed down by speaking rather than writing?', ['Oral history', 'Written history', 'A concept unrelated to history', 'A map'], 0),
    ('Who often shares oral history and traditions within a community?', ['Elders and storytellers', 'A concept unrelated to oral history', 'Only strangers', 'Only young children'], 0),
    ('Do many Indigenous communities use storytelling to pass down their history and traditions?', ['Yes', 'No, storytelling is never used to pass down history', 'A concept unrelated to Indigenous communities', 'Only written books are ever used'], 0),
    ('Why is oral history an important way of preserving a community’s knowledge?', ['It allows stories, traditions, and lessons to be passed from generation to generation', 'Oral history never preserves any useful knowledge', 'This concept has no relevance to communities', 'Oral history is always less accurate than any other kind of history'], 0),
    ('Why might listening carefully to an elder’s story help you learn about the past?', ['Elders often have firsthand knowledge and experiences that are not written down anywhere else', 'Elders never know anything about the past', 'This concept has no connection to oral history', 'Listening to a story never teaches anyone anything'], 0)]),
]),

day(109, [
L('Writing: Writing a Personal Narrative (Memoir)',
  'Grade 3 Language strand: a personal narrative, or memoir, is a true story about something that happened to the writer, told in the first person and often including personal feelings and details.',
  [('What is a personal narrative mainly about?', ['A true event from the writer’s own life', 'A made-up fantasy story', 'A concept unrelated to writing', 'Facts about animals only'], 0),
   ('A personal narrative is usually told from which point of view?', ['First person (using I and me)', 'Third person (using he or she)', 'A concept unrelated to point of view', 'Second person (using you)'], 0),
   ('What might a writer include in a personal narrative besides events?', ['Their own feelings and thoughts', 'A concept unrelated to personal narratives', 'Only numbers and dates', 'Nothing besides a list of events'], 0),
   ('Why might a writer include personal feelings in a memoir?', ['It helps readers understand how the event affected the writer', 'Personal feelings never belong in a memoir', 'This concept has no connection to writing a personal narrative', 'Memoirs should never mention the writer’s own experience'], 0),
   ('Which sentence would most likely begin a personal narrative?', ['Last summer, I learned to ride my bike for the first time.', 'A triangle has three sides.', 'The water cycle has several stages.', 'Add 6 and 2 to get 8.'], 0)]),
M('Probability: Fair and Unfair Games',
  'Grade 3 Math strand: a game is fair when every player has an equal chance of winning, and unfair when one player or outcome is more likely than another.',
  [('What do we call a game where every player has an equal chance of winning?', ['A fair game', 'An unfair game', 'A concept unrelated to probability', 'A losing game'], 0),
   ('If a spinner has 3 sections for Player A and 1 section for Player B, is the game fair or unfair?', ['Unfair', 'Fair', 'A concept unrelated to probability', 'Cannot tell'], 0),
   ('If a coin toss game gives heads to Player A and tails to Player B, is this game fair or unfair?', ['Fair', 'Unfair', 'A concept unrelated to probability', 'Cannot tell'], 0),
   ('What might make a dice game unfair?', ['If one player wins on more numbers than the other player', 'If both players have an equal chance of winning', 'A concept unrelated to probability', 'If the dice has six sides'], 0),
   ('Why is it important for a game to be fair?', ['So that every player has an equal opportunity to win', 'Fairness never matters in a game', 'This concept has no connection to probability', 'Unfair games are always more fun for everyone'], 0)]),
Sc('Science: Fungi — Neither Plant Nor Animal',
   'Grade 3 Science strand: fungi, such as mushrooms and moulds, form their own separate group of living things -- unlike plants, they cannot make their own food, and unlike animals, most cannot move on their own.',
   [('Are fungi classified in the same group as plants?', ['No, fungi form their own separate group', 'Yes, fungi are always classified as plants', 'A concept unrelated to classification', 'Fungi are classified as animals'], 0),
    ('Name one example of a fungus, such as a ___.', ['Mushroom', 'A concept unrelated to fungi', 'An oak tree', 'A house cat'], 0),
    ('Can most fungi make their own food from sunlight the way plants do?', ['No', 'Yes, exactly like plants', 'A concept unrelated to fungi', 'Fungi never need any food at all'], 0),
    ('Why are fungi classified separately from plants and animals?', ['They have their own unique features, such as not making their own food and not moving like most animals', 'Fungi are always exactly the same as plants', 'This concept has no connection to classifying living things', 'Fungi and animals are always identical to each other'], 0),
    ('Why are fungi important decomposers in many ecosystems?', ['They help break down dead plants and animals, returning nutrients to the soil', 'Fungi never break down anything in an ecosystem', 'This concept has no relevance to ecosystems', 'Fungi only exist in ecosystems with no other living things'], 0)]),
SS('Social Studies: Building the Railway and Its Impact on Ontario',
   'Grade 3 Social Studies strand: the building of railways across Canada in the late 1800s helped connect communities, including many in Ontario, making it faster to transport people and goods across long distances.',
   [('What form of transportation was built across Canada to connect communities in the late 1800s?', ['The railway', 'The airplane', 'A concept unrelated to transportation', 'The subway'], 0),
    ('Did the railway help transport people and goods faster across long distances?', ['Yes', 'No, the railway made travel much slower', 'A concept unrelated to transportation', 'The railway only carried mail'], 0),
    ('Which of these communities could have been connected by the growing railway network in Ontario?', ['Towns along the rail line', 'A concept unrelated to railways', 'Only communities with no roads at all', 'No communities were ever connected by rail'], 0),
    ('Why was building the railway such an important achievement for connecting communities?', ['It made travel and trade across long distances much faster than before', 'The railway had no effect on how communities were connected', 'This concept has no relevance to Ontario’s history', 'Communities were already perfectly connected before the railway'], 0),
    ('Why might a new town have grown up along a railway line in Ontario?', ['The railway brought people, goods, and opportunities for trade to that location', 'Railways never attracted people or trade to a location', 'This concept has no connection to Ontario’s history', 'Towns never form near transportation routes'], 0)]),
]),

day(110, [
L('Review: Grammar, Vocabulary, and Reading Strategies',
  'Grade 3 Language strand review: students revisit commas in dates and addresses, suffixes -ful and -less, bold print and glossary, plural possessive nouns, and alliteration.',
  [('In the date July 22, 2026, where should the comma be placed?', ['Between the day and the year', 'Between the month and the day', 'At the very end', 'Nowhere, dates never use commas'], 0),
   ('What does the suffix -ful mean?', ['Full of', 'Without', 'Before', 'After'], 0),
   ('What do we call print that is darker and thicker than the rest of the text?', ['Bold print', 'Italics', 'A footnote', 'A caption'], 0),
   ('How do you usually form a possessive noun for a plural noun that already ends in -s?', ['Add an apostrophe after the s', 'Add an apostrophe and another s', 'Add -ing', 'A concept unrelated to grammar'], 0),
   ('What do we call the repetition of the same beginning sound in nearby words?', ['Alliteration', 'A concept unrelated to vocabulary', 'A homograph', 'A synonym'], 0)]),
M('Review: Number, Geometry, and Data',
  'Grade 3 Math strand review: students revisit rounding to the nearest 1000, comparing fractions with the same numerator, comparing angles to a right angle, finding the mode, and multiplying by 0 and 1.',
  [('Which digit do you look at to round a number to the nearest 1000?', ['The hundreds digit', 'The ones digit', 'The tens digit', 'A concept unrelated to rounding'], 0),
   ('When two fractions have the same numerator, which one is larger?', ['The one with the smaller denominator', 'The one with the larger denominator', 'They are always equal', 'A concept unrelated to fractions'], 0),
   ('What do we call an angle that is exactly the same size as a right angle?', ['A right angle', 'An acute angle', 'An obtuse angle', 'A concept unrelated to angles'], 0),
   ('What do we call the value that appears most often in a data set?', ['The mode', 'The range', 'A concept unrelated to data', 'The total'], 0),
   ('What is 7 multiplied by 1?', ['7', '0', '8', '1'], 0)]),
Sc('Review: Adaptations, Ecosystems, and Classification',
   'Grade 3 Science strand review: students revisit bird adaptations for flight, herbivores/carnivores/omnivores, biodiversity in rainforests, complete versus incomplete metamorphosis, and fungi classification.',
   [('What kind of bones do birds have that help them fly?', ['Lightweight hollow bones', 'Heavy solid bones', 'A concept unrelated to birds', 'No bones at all'], 0),
    ('What do we call an animal that eats only plants?', ['A herbivore', 'A carnivore', 'An omnivore', 'A concept unrelated to animal diets'], 0),
    ('What word describes the huge variety of living things found in a rainforest?', ['Biodiversity', 'A concept unrelated to ecosystems', 'Uniformity', 'Scarcity'], 0),
    ('How many main stages does complete metamorphosis have?', ['Four', 'Two', 'Three', 'Five'], 0),
    ('Are fungi classified in the same group as plants?', ['No, fungi form their own separate group', 'Yes, fungi are always classified as plants', 'A concept unrelated to classification', 'Fungi are classified as animals'], 0)]),
SS('Review: Ontario’s Landmarks, Government, and Trade',
   'Grade 3 Social Studies strand review: students revisit the Niagara Escarpment, Canada’s official languages, emergency services, Ontario’s airports, and the building of the railway.',
   [('What do we call a long, rocky ridge of land such as the Niagara Escarpment?', ['A landform', 'A concept unrelated to geography', 'A type of government', 'A type of currency'], 0),
    ('What are Canada’s two official languages?', ['English and French', 'English and Spanish', 'A concept unrelated to Canada', 'French and German'], 0),
    ('What number can people in Canada call in an emergency to reach police, fire, or paramedics?', ['911', 'A concept unrelated to emergency services', '123', '555'], 0),
    ('Name one large airport located in Ontario.', ['Toronto Pearson', 'A concept unrelated to airports', 'A bus terminal', 'A subway station'], 0),
    ('What form of transportation was built across Canada to connect communities in the late 1800s?', ['The railway', 'The airplane', 'A concept unrelated to transportation', 'The subway'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_101_110)
    append_to(3, g3_101_110)
