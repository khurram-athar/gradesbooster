#!/usr/bin/env python3
"""Grade 3, Days 91-100 -- extends Grade 3 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade3.json):
tone and mood, irregular plural nouns, homographs, writing a persuasive
poster, author’s craft (word choice), possessive nouns, storytelling with
expression, portmanteau (blended) words, text features (table of contents
and index), primary and secondary data sources, classifying quadrilaterals,
comparing ways to pay, fact families for addition and subtraction, ordering
numbers to 10 000, estimating length in centimetres and metres, estimating
products, probability with a spinner, perimeter of regular polygons, the
life cycle of a frog, freshwater habitats in Ontario, desert adaptations,
structures that withstand earthquakes, ferns and mosses, insects versus
spiders, coral reefs, deciduous versus coniferous trees, how roots, stems,
and leaves work together, United Empire Loyalists, the War of 1812, Black
Loyalists, religious diversity in Ontario, trade with the United States,
recycling and waste management, public libraries, sports and recreation,
and Ontario’s population growth over time.

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


g3_91_100 = [
day(91, [
L('Reading: Understanding Tone and Mood',
  'Grade 3 Language strand: tone is the author’s attitude toward a topic, and mood is the feeling a story creates in the reader; word choice and description often shape both.',
  [('What do we call the author’s attitude toward a topic in a piece of writing?', ['Tone', 'A concept unrelated to reading', 'The title of the book', 'The page number'], 0),
   ('What do we call the feeling a story creates in the reader?', ['Mood', 'Tone', 'A concept unrelated to reading', 'The glossary'], 0),
   ('If a story uses words like gloomy, dark, and silent, what kind of mood is it likely creating?', ['A sad or eerie mood', 'A cheerful, sunny mood', 'A concept unrelated to mood', 'No mood at all'], 0),
   ('Why might an author choose words like sparkling and joyful to describe a scene?', ['To create a happy, cheerful mood for the reader', 'Word choice never affects a story’s mood', 'This concept has no connection to storytelling', 'To make the scene feel sad and gloomy'], 0),
   ('Why is it useful for readers to notice an author’s tone?', ['It helps them understand how the author feels about the topic', 'Tone never adds any meaning to a text', 'This concept has no connection to reading comprehension', 'Readers should always ignore an author’s tone'], 0)]),
M('Data: Primary and Secondary Data Sources',
  'Grade 3 Math strand: primary data is collected firsthand, such as through a survey you conduct yourself, while secondary data is collected by someone else and found in another source, like a book or website.',
  [('What do we call data you collect yourself, such as through your own survey?', ['Primary data', 'Secondary data', 'A concept unrelated to data', 'Estimated data'], 0),
   ('What do we call data that was already collected by someone else, such as in a book?', ['Secondary data', 'Primary data', 'A concept unrelated to data', 'Estimated data'], 0),
   ('If you count how many students in your class like pizza, is that primary or secondary data?', ['Primary data', 'Secondary data', 'Neither kind of data', 'Cannot tell'], 0),
   ('If you look up the population of Toronto in an encyclopedia, is that primary or secondary data?', ['Secondary data', 'Primary data', 'Neither kind of data', 'Cannot tell'], 0),
   ('Why might a scientist choose to collect primary data instead of using secondary data?', ['To get information that directly answers their specific question', 'Primary data is never useful for answering questions', 'This concept has no connection to data collection', 'Secondary data is always more accurate than primary data'], 0)]),
Sc('Science: Life Cycle of a Frog: From Egg to Adult',
   'Grade 3 Science strand: a frog’s life cycle includes several stages -- egg, tadpole, tadpole with legs, and adult frog -- a process called metamorphosis.',
   [('What is the first stage of a frog’s life cycle?', ['Egg', 'Tadpole', 'Adult frog', 'A concept unrelated to life cycles'], 0),
    ('What do we call a baby frog that lives in water and has a tail?', ['A tadpole', 'An adult frog', 'A concept unrelated to frogs', 'A larva of a butterfly'], 0),
    ('What is the name for the process of major body changes a frog goes through?', ['Metamorphosis', 'Photosynthesis', 'A concept unrelated to frogs', 'Hibernation'], 0),
    ('Why does a tadpole need to live in water while a fully grown frog can live on land?', ['A tadpole breathes with gills like a fish, while an adult frog develops lungs', 'Tadpoles and adult frogs breathe in exactly the same way', 'This concept has no connection to a frog’s life cycle', 'Adult frogs can never leave the water'], 0),
    ('Why is understanding a frog’s life cycle useful for protecting wetland habitats?', ['It helps us know what conditions frogs need at each stage to survive', 'A frog’s life cycle has no connection to its habitat', 'This concept has no relevance to protecting wetlands', 'Frogs never actually need any specific habitat'], 0)]),
SS('Social Studies: United Empire Loyalists and the Founding of Ontario',
   'Grade 3 Social Studies strand: United Empire Loyalists were settlers who remained loyal to Britain during the American Revolution and moved north to what is now Ontario, helping to found many early communities.',
   [('What do we call settlers who stayed loyal to Britain during the American Revolution and moved north?', ['United Empire Loyalists', 'A concept unrelated to Canadian history', 'Confederation delegates', 'Early trading partners'], 0),
    ('Where did many United Empire Loyalists settle after leaving the newly formed United States?', ['In what is now Ontario', 'In what is now Mexico', 'A concept unrelated to settlement', 'Nowhere, they all returned to Britain'], 0),
    ('Did the United Empire Loyalists help found many early communities in Ontario?', ['Yes', 'No, they never settled anywhere in Ontario', 'A concept unrelated to Ontario’s history', 'They only settled in another country'], 0),
    ('Why did United Empire Loyalists leave their homes to move north?', ['They wanted to remain part of Britain rather than join the new United States', 'They were forced to leave for no particular reason', 'This concept has no connection to the American Revolution', 'They wanted to join the new United States government'], 0),
    ('Why is the story of the United Empire Loyalists an important part of Ontario’s history?', ['It explains why and how many of Ontario’s earliest communities were founded', 'The United Empire Loyalists have no connection to Ontario’s history', 'This event never actually affected Ontario', 'This concept has no relevance to social studies'], 0)]),
]),

day(92, [
L('Grammar: Irregular Plural Nouns',
  'Grade 3 Language strand: most nouns become plural by adding -s or -es, but irregular plural nouns change in unusual ways, such as child becoming children or mouse becoming mice.',
  [('What is the plural form of the word child?', ['Children', 'Childs', 'Childes', 'Childies'], 0),
   ('What is the plural form of the word mouse?', ['Mice', 'Mouses', 'Mices', 'Mousies'], 0),
   ('What is the plural form of the word foot?', ['Feet', 'Foots', 'Footes', 'Feets'], 0),
   ('Most nouns become plural by adding which ending?', ['-s or -es', '-ing', '-ed', 'A concept unrelated to plural nouns'], 0),
   ('Why do irregular plural nouns need to be memorized rather than following the usual -s rule?', ['Because they change in unusual ways that don’t follow the normal pattern', 'Irregular plural nouns always follow the -s rule perfectly', 'This concept has no connection to grammar', 'All nouns become plural in exactly the same way'], 0)]),
M('Geometry: Classifying Quadrilaterals',
  'Grade 3 Math strand: a quadrilateral is any shape with four sides, and can be classified into types such as squares, rectangles, rhombuses, and trapezoids based on their side lengths and angles.',
  [('How many sides does a quadrilateral have?', ['4', '3', '5', '6'], 0),
   ('Which of these is a quadrilateral with four equal sides and four right angles?', ['A square', 'A triangle', 'A pentagon', 'A circle'], 0),
   ('Which of these is a quadrilateral with two pairs of equal opposite sides and four right angles?', ['A rectangle', 'A triangle', 'A pentagon', 'A hexagon'], 0),
   ('Which of these shapes is NOT a quadrilateral?', ['A triangle', 'A square', 'A rectangle', 'A trapezoid'], 0),
   ('Why might a trapezoid be classified differently from a square?', ['A trapezoid only has one pair of parallel sides, unlike a square', 'A trapezoid and a square are always the exact same shape', 'This concept has no connection to classifying shapes', 'A trapezoid has five sides while a square has four'], 0)]),
Sc('Science: Freshwater Habitats in Ontario: Lakes and Wetlands',
   'Grade 3 Science strand: Ontario has many freshwater habitats, including lakes, rivers, and wetlands, that provide homes for fish, birds, insects, and plants.',
   [('Name one type of freshwater habitat found in Ontario, such as a lake.', ['A lake', 'A concept unrelated to habitats', 'A desert', 'A coral reef'], 0),
    ('Do wetlands provide homes for fish, birds, and insects?', ['Yes', 'No, wetlands support no living things', 'A concept unrelated to habitats', 'Only fish can live in wetlands'], 0),
    ('What do we call an area of land that is covered by shallow water for at least part of the year?', ['A wetland', 'A desert', 'A concept unrelated to habitats', 'A mountain'], 0),
    ('Why are wetlands important for many different kinds of living things?', ['They provide food, water, and shelter for a wide variety of species', 'Wetlands never provide any resources for living things', 'This concept has no connection to habitats', 'Only one single species can ever live in a wetland'], 0),
    ('Why might pollution in a lake harm many different kinds of living things at once?', ['Many species depend on the same water for food, shelter, and survival', 'Pollution in a lake never affects any living things', 'This concept has no connection to freshwater habitats', 'Only plants are ever affected by water pollution'], 0)]),
SS('Social Studies: The War of 1812 in Upper Canada',
   'Grade 3 Social Studies strand: the War of 1812 was a conflict between Britain and the United States, fought partly in Upper Canada (now Ontario), where settlers and Indigenous allies helped defend the colony.',
   [('What do we call the war fought between Britain and the United States that took place partly in Upper Canada?', ['The War of 1812', 'The American Revolution', 'A concept unrelated to Canadian history', 'World War One'], 0),
    ('What was Ontario called during the time of the War of 1812?', ['Upper Canada', 'New France', 'A concept unrelated to Ontario’s history', 'Lower Canada'], 0),
    ('Did settlers and Indigenous allies help defend Upper Canada during the War of 1812?', ['Yes', 'No, no one defended Upper Canada', 'A concept unrelated to the War of 1812', 'Only soldiers from another country defended it'], 0),
    ('Why was Upper Canada an important location during the War of 1812?', ['It bordered the United States and was the site of several battles', 'Upper Canada was located far away from any fighting', 'This concept has no connection to the War of 1812', 'Upper Canada had no border with the United States'], 0),
    ('Why is the War of 1812 still remembered as an important event in Ontario’s history?', ['It helped shape the border and identity of the colony that later became Ontario', 'The War of 1812 has no connection to Ontario’s history', 'This event never actually affected Upper Canada', 'This concept has no relevance to social studies'], 0)]),
]),

day(93, [
L('Vocabulary: Homographs',
  'Grade 3 Language strand: a homograph is a word that is spelled the same as another word but has a different meaning, such as bat (the animal) and bat (used in baseball).',
  [('What do we call two words that are spelled the same but have different meanings?', ['Homographs', 'Synonyms', 'Antonyms', 'A concept unrelated to vocabulary'], 0),
   ('Which of these is an example of a homograph?', ['Bat', 'Happy', 'Slowly', 'Jump'], 0),
   ('In the sentence I saw a bat fly at night, which meaning of bat is being used?', ['A flying animal', 'A piece of sports equipment', 'A concept unrelated to the sentence', 'A type of hat'], 0),
   ('In the sentence She swung the bat and hit the ball, which meaning of bat is being used?', ['A piece of sports equipment', 'A flying animal', 'A concept unrelated to the sentence', 'A type of hat'], 0),
   ('Why is it important to use context clues when reading a homograph?', ['Context clues help you figure out which meaning of the word is intended', 'Context clues never help with understanding homographs', 'This concept has no connection to reading comprehension', 'Homographs only ever have one possible meaning'], 0)]),
M('Financial Literacy: Comparing Ways to Pay',
  'Grade 3 Math strand: people can pay for goods and services in different ways, such as cash, debit cards, or e-transfers, and each method has its own advantages.',
  [('Name one way people can pay for something, such as cash.', ['Cash', 'A concept unrelated to paying for things', 'A math equation', 'A weather forecast'], 0),
   ('What do we call a card that takes money directly from your bank account when you pay?', ['A debit card', 'A concept unrelated to paying for things', 'A library card', 'A birthday card'], 0),
   ('What do we call sending money electronically from one bank account to another?', ['An e-transfer', 'A concept unrelated to paying for things', 'A phone call', 'A text message'], 0),
   ('Why might someone choose to pay with a debit card instead of cash?', ['It can be more convenient and does not require carrying paper money', 'Debit cards are never accepted anywhere', 'This concept has no connection to paying for things', 'Cash is always the only way to pay for something'], 0),
   ('Why is it useful to understand different ways to pay for things?', ['It helps people choose the payment method that works best for a situation', 'Understanding payment methods is never useful', 'This concept has no connection to financial literacy', 'There is only ever one way to pay for anything'], 0)]),
Sc('Science: Desert Adaptations: Surviving Extreme Heat and Dryness',
   'Grade 3 Science strand: desert plants and animals have special adaptations, such as storing water or being active at night, that help them survive extreme heat and very little rainfall.',
   [('Name one challenge desert plants and animals must survive, such as extreme heat.', ['Extreme heat', 'A concept unrelated to deserts', 'Constant flooding', 'Extremely cold winters only'], 0),
    ('Why might a cactus have thick, waxy skin?', ['To help it store and retain water', 'To attract more rainfall', 'This concept has no connection to desert plants', 'Thick skin has no purpose for a cactus'], 0),
    ('Why might many desert animals be active mainly at night?', ['To avoid the extreme heat of the day', 'Desert animals are never active at any time', 'This concept has no connection to desert adaptations', 'Nighttime in the desert is hotter than daytime'], 0),
    ('Why do desert plants often have very long or wide-spreading roots?', ['To collect as much of the limited rainfall as possible', 'Desert plants never actually need water', 'This concept has no connection to desert adaptations', 'Long roots have no connection to finding water'], 0),
    ('Why is it important for desert organisms to have adaptations for surviving with little water?', ['Because deserts receive very little rainfall, and water is hard to find', 'Deserts actually receive more rainfall than any other habitat', 'This concept has no relevance to desert ecosystems', 'Desert organisms never actually need water to survive'], 0)]),
SS('Social Studies: Black Loyalists and Early Black Communities in Ontario',
   'Grade 3 Social Studies strand: Black Loyalists were formerly enslaved and free Black people who supported Britain during the American Revolution and settled in early Canadian communities, including areas of what is now Ontario.',
   [('What do we call formerly enslaved and free Black people who supported Britain during the American Revolution?', ['Black Loyalists', 'A concept unrelated to Canadian history', 'Confederation delegates', 'Fur traders'], 0),
    ('Did some Black Loyalists settle in communities in what is now Ontario?', ['Yes', 'No, none ever settled in Ontario', 'A concept unrelated to Ontario’s history', 'They only settled in another country'], 0),
    ('Black Loyalists mainly arrived in Canada around the time of which event?', ['The American Revolution', 'The building of the railway', 'A concept unrelated to Canadian history', 'World War Two'], 0),
    ('Why did Black Loyalists choose to leave the newly formed United States?', ['They were promised freedom and land for supporting Britain', 'They were forced to leave for no particular reason', 'This concept has no connection to the American Revolution', 'They wanted to join the new United States government'], 0),
    ('Why is learning about Black Loyalists important for understanding Ontario’s early history?', ['It shows the diverse groups of people who helped build early communities in the region', 'Black Loyalists have no connection to Ontario’s history', 'This event never actually affected Ontario', 'This concept has no relevance to social studies'], 0)]),
]),

day(94, [
L('Writing: Writing a Persuasive Poster',
  'Grade 3 Language strand: a persuasive poster uses a strong slogan, bold images, and convincing reasons to make the reader take action or agree with an idea.',
  [('What kind of writing uses a slogan and images to convince someone to take action?', ['A persuasive poster', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('What do we call a short, catchy phrase used on a poster to grab attention?', ['A slogan', 'A concept unrelated to writing', 'A footnote', 'A glossary'], 0),
   ('Should a persuasive poster include convincing reasons to support its message?', ['Yes', 'No, a poster should never give any reasons', 'A concept unrelated to persuasive writing', 'Reasons never belong on a poster'], 0),
   ('Why might a persuasive poster use bold images along with words?', ['Images can quickly grab attention and support the poster’s message', 'Images never add anything to a persuasive poster', 'This concept has no connection to persuasive writing', 'Words alone are always more persuasive than images'], 0),
   ('Which of these would most likely appear on a persuasive poster about recycling?', ['Save our planet — recycle today!', 'The water cycle has three main stages.', 'Add 4 and 5 to get 9.', 'A triangle has three sides.'], 0)]),
M('Number: Fact Families for Addition and Subtraction',
  'Grade 3 Math strand: a fact family is a group of related addition and subtraction facts that use the same three numbers, such as 4 + 5 = 9, 5 + 4 = 9, 9 - 4 = 5, and 9 - 5 = 4.',
  [('What do we call a group of related addition and subtraction facts using the same three numbers?', ['A fact family', 'A concept unrelated to number sense', 'A number line', 'A place value chart'], 0),
   ('If 6 + 3 = 9 is part of a fact family, which of these also belongs to that same fact family?', ['9 - 3 = 6', '9 + 3 = 12', '6 - 3 = 9', '3 - 6 = 9'], 0),
   ('Which three numbers make up the fact family that includes 7 + 2 = 9?', ['7, 2, and 9', '7, 2, and 14', '9, 2, and 11', '7, 9, and 16'], 0),
   ('Why are fact families useful for learning subtraction facts?', ['Knowing an addition fact can help you quickly find its related subtraction facts', 'Fact families never help with subtraction', 'This concept has no connection to number sense', 'Addition and subtraction facts are never related to each other'], 0),
   ('Which equation completes this fact family: 8 + 5 = 13, 5 + 8 = 13, 13 - 5 = 8, ___?', ['13 - 8 = 5', '13 + 8 = 21', '8 - 5 = 13', '5 - 8 = 13'], 0)]),
Sc('Science: Structures That Withstand Earthquakes',
   'Grade 3 Science strand: engineers design structures with special features, such as flexible materials and strong foundations, to help buildings withstand the shaking caused by earthquakes.',
   [('What natural event can cause the ground and buildings to shake suddenly?', ['An earthquake', 'A tide', 'A concept unrelated to structures', 'Photosynthesis'], 0),
    ('Name one feature engineers might use to help a building withstand an earthquake, such as a strong ___.', ['Foundation', 'A concept unrelated to structures', 'Paint colour', 'Window curtain'], 0),
    ('Might flexible materials help a building bend slightly instead of breaking during an earthquake?', ['Yes', 'No, flexible materials always make buildings weaker', 'A concept unrelated to structures', 'Buildings can never bend at all'], 0),
    ('Why do engineers test building designs before constructing them in earthquake-prone areas?', ['To make sure the structure can safely withstand shaking and protect people inside', 'Testing building designs is never necessary', 'This concept has no connection to structures', 'Engineers never need to consider earthquakes'], 0),
    ('Why might a taller building need different earthquake protection than a short one?', ['Taller buildings sway more during shaking and need special design features to stay stable', 'Taller buildings never sway during an earthquake', 'This concept has no connection to structures', 'Short buildings always need more protection than tall ones'], 0)]),
SS('Social Studies: Religious Diversity in Ontario Communities',
   'Grade 3 Social Studies strand: Ontario communities include people who practise many different religions, such as Christianity, Islam, Judaism, Hinduism, Sikhism, and Buddhism, reflecting the province’s diversity.',
   [('Name one religion practised by people in Ontario communities, such as Christianity.', ['Christianity', 'A concept unrelated to religion', 'A type of government', 'A sport'], 0),
    ('Does Ontario include people who practise many different religions?', ['Yes', 'No, everyone in Ontario practises the exact same religion', 'A concept unrelated to Ontario’s communities', 'Religion has no connection to Ontario’s communities'], 0),
    ('What word describes a community that includes people of many different religions?', ['Religiously diverse', 'A concept unrelated to community', 'Uniform', 'Isolated'], 0),
    ('Why might a city have places of worship from several different religions?', ['Because the community includes people from many different religious backgrounds', 'Cities never include people from different religious backgrounds', 'This concept has no connection to Ontario’s communities', 'Only one religion is ever allowed in a city'], 0),
    ('Why is it important for communities to respect religious diversity?', ['So everyone feels welcome and free to practise their own beliefs', 'Respecting religious diversity has no benefit to a community', 'Communities function better when only one religion is allowed', 'This concept has no relevance to social studies'], 0)]),
]),

day(95, [
L('Reading: Author’s Craft — Word Choice',
  'Grade 3 Language strand: word choice, also called diction, is how an author selects specific words to create meaning, feeling, or imagery in a text.',
  [('What do we call an author’s choice of specific words to create meaning or feeling?', ['Word choice', 'A concept unrelated to reading', 'The table of contents', 'The index'], 0),
   ('If an author writes the puppy scampered instead of the puppy walked, what feeling does the word scampered add?', ['A sense of playfulness or energy', 'A sense of boredom', 'A concept unrelated to word choice', 'No feeling at all'], 0),
   ('Why might an author choose the word enormous instead of the word big?', ['To create a stronger, more vivid image for the reader', 'Word choice never affects how a reader imagines a scene', 'This concept has no connection to an author’s craft', 'Enormous and big always mean completely different things'], 0),
   ('Why is word choice an important part of an author’s craft?', ['Specific words can create a clearer or more powerful image than general words', 'Word choice never affects a piece of writing', 'This concept has no connection to reading or writing', 'All words create the exact same feeling in a reader'], 0),
   ('Which sentence uses the most vivid word choice?', ['The thunder roared across the dark sky.', 'The weather was bad outside.', 'It was not a nice day.', 'The sky had some clouds.'], 0)]),
M('Measurement: Estimating Length in Centimetres and Metres',
  'Grade 3 Math strand: students estimate the length of everyday objects using centimetres and metres before measuring, building a sense of these units.',
  [('Which unit would you most likely use to measure the length of a pencil?', ['Centimetres', 'Metres', 'Kilometres', 'Litres'], 0),
   ('Which unit would you most likely use to measure the length of a classroom?', ['Metres', 'Centimetres', 'Millilitres', 'Kilograms'], 0),
   ('About how long is a standard door, roughly 2 ___?', ['Metres', 'Centimetres', 'Kilometres', 'Litres'], 0),
   ('Estimating a measurement before you measure helps you ___.', ['Check whether your final measurement makes sense', 'Avoid ever measuring the object at all', 'A concept unrelated to measurement', 'Guarantee the exact measurement without a tool'], 0),
   ('Which is the better estimate for the length of a paperclip: 3 centimetres or 3 metres?', ['3 centimetres', '3 metres', 'Both are equally good estimates', 'Neither is a reasonable estimate'], 0)]),
Sc('Science: Ferns and Mosses: Plants Without Seeds',
   'Grade 3 Science strand: not all plants grow from seeds; ferns and mosses reproduce using tiny spores instead, and they thrive in damp, shady environments.',
   [('Do ferns and mosses reproduce using seeds or spores?', ['Spores', 'Seeds', 'A concept unrelated to plant reproduction', 'Neither seeds nor spores'], 0),
    ('What kind of environment do ferns and mosses usually thrive in?', ['Damp, shady environments', 'Dry, sunny deserts', 'A concept unrelated to plant habitats', 'The ocean floor'], 0),
    ('Name one type of plant that reproduces without seeds, such as a ___.', ['Fern', 'Sunflower', 'Apple tree', 'A concept unrelated to plants'], 0),
    ('Why might mosses commonly be found growing on the shady side of rocks or trees?', ['Because mosses thrive in damp, shady conditions', 'Mosses only grow in extremely sunny, dry places', 'This concept has no connection to how mosses grow', 'Mosses never actually need moisture'], 0),
    ('Why is it useful for scientists to classify plants by how they reproduce?', ['It helps them understand the different ways plants have adapted to grow and spread', 'How a plant reproduces has no connection to classifying it', 'This concept has no relevance to plant science', 'All plants reproduce in exactly the same way'], 0)]),
SS('Social Studies: Trade Between Ontario and the United States',
   'Grade 3 Social Studies strand: Ontario trades many goods and services with the United States, its neighbouring country, exchanging products like cars, food, and machinery across the border.',
   [('Name the country that borders Ontario and trades goods with it.', ['The United States', 'A concept unrelated to trade', 'France', 'Australia'], 0),
    ('Name one type of good Ontario might trade with the United States, such as cars.', ['Cars', 'A concept unrelated to trade', 'Wild animals', 'Ocean water'], 0),
    ('Does Ontario exchange goods and services with the United States across the border?', ['Yes', 'No, Ontario never trades with the United States', 'A concept unrelated to Ontario’s economy', 'Only one single product is ever traded'], 0),
    ('Why is trade with the United States important for Ontario’s economy?', ['It creates jobs and allows goods to be bought and sold across the border', 'Trade with the United States has no connection to Ontario’s economy', 'Ontario never actually trades with any other country', 'This concept has no relevance to Ontario’s economy'], 0),
    ('Why might Ontario and the United States trade so many goods with each other?', ['They share a long border, making transportation of goods easier and faster', 'Ontario and the United States do not share any border', 'This concept has no connection to trade', 'Sharing a border makes trade impossible'], 0)]),
]),

day(96, [
L('Grammar: Possessive Nouns',
  'Grade 3 Language strand: a possessive noun shows ownership, usually formed by adding an apostrophe and an -s, as in the dog’s bone, meaning the bone belongs to the dog.',
  [('What does a possessive noun show?', ['Ownership', 'A question', 'A concept unrelated to grammar', 'A silent letter'], 0),
   ('How do you usually form a possessive noun for a singular noun?', ['Add an apostrophe and an -s', 'Add -ing', 'Add -ed', 'A concept unrelated to grammar'], 0),
   ('Which of these correctly shows that the ball belongs to the girl?', ['The girl’s ball', 'The girls ball', 'The girl ball’s', 'Girl the ball’s'], 0),
   ('In the phrase the cat’s tail, what does the apostrophe and s show?', ['That the tail belongs to the cat', 'That there are many cats', 'A concept unrelated to grammar', 'That the cat is running'], 0),
   ('Why is it important to place the apostrophe correctly in a possessive noun?', ['Incorrect placement can confuse who owns what, or make the noun look plural instead', 'Apostrophe placement never matters in writing', 'This concept has no connection to grammar', 'Possessive nouns never actually use an apostrophe'], 0)]),
M('Number: Ordering Numbers to 10 000',
  'Grade 3 Math strand: students order a set of numbers up to 10 000 from least to greatest or greatest to least, using place value to compare digits.',
  [('Which of these numbers is the smallest: 4 502, 4 250, 4 025?', ['4 025', '4 502', '4 250', 'They are all equal'], 0),
   ('Put these numbers in order from least to greatest: 6 300, 6 030, 6 003.', ['6 003, 6 030, 6 300', '6 300, 6 030, 6 003', '6 030, 6 003, 6 300', '6 003, 6 300, 6 030'], 0),
   ('Which of these numbers is the greatest: 8 900, 8 090, 8 009?', ['8 900', '8 090', '8 009', 'They are all equal'], 0),
   ('When ordering numbers, which digit should you compare first?', ['The digit with the highest place value', 'The digit with the lowest place value', 'A concept unrelated to place value', 'The last digit only'], 0),
   ('Why is understanding place value important when ordering large numbers?', ['It helps you correctly compare digits to find which number is greater or smaller', 'Place value has no connection to ordering numbers', 'This concept has no relevance to number sense', 'Numbers can be ordered without ever comparing digits'], 0)]),
Sc('Science: The Difference Between Insects and Spiders',
   'Grade 3 Science strand: insects have six legs and three body parts, while spiders (arachnids) have eight legs and two body parts, helping scientists classify them into different animal groups.',
   [('How many legs does an insect have?', ['Six', 'Eight', 'Four', 'Ten'], 0),
    ('How many legs does a spider have?', ['Eight', 'Six', 'Four', 'Ten'], 0),
    ('How many main body parts does an insect have?', ['Three', 'Two', 'Four', 'Five'], 0),
    ('Is a spider classified as an insect or an arachnid?', ['An arachnid', 'An insect', 'A concept unrelated to classification', 'A mammal'], 0),
    ('Why is the number of legs a useful clue for classifying an animal as an insect or a spider?', ['It is an easy, visible feature that reliably tells the two groups apart', 'The number of legs never helps classify an animal', 'This concept has no connection to classifying animals', 'Insects and spiders always have the exact same number of legs'], 0)]),
SS('Social Studies: Recycling and Waste Management Programs in Ontario',
   'Grade 3 Social Studies strand: Ontario municipalities run recycling and waste management programs, such as blue box and green bin collection, to help reduce the amount of garbage sent to landfills.',
   [('What do we call the coloured bin many Ontario homes use to collect recyclable materials?', ['The blue box', 'The green bin', 'A concept unrelated to recycling', 'The red bin'], 0),
    ('What is one purpose of a municipal recycling program?', ['To reduce the amount of garbage sent to landfills', 'To increase the amount of garbage sent to landfills', 'A concept unrelated to municipal programs', 'To stop people from throwing anything away'], 0),
    ('Name one program that helps manage food waste in some Ontario communities.', ['The green bin program', 'The blue box program', 'A concept unrelated to waste management', 'The library program'], 0),
    ('Why do municipalities organize waste management programs instead of leaving it up to each household?', ['It ensures waste is handled safely, consistently, and effectively for the whole community', 'Waste management has no connection to municipal government', 'Households always manage waste better without any program', 'This concept has no relevance to communities'], 0),
    ('Why is reducing the amount of garbage sent to landfills beneficial for the environment?', ['It helps conserve land and reduces pollution from decomposing waste', 'Reducing garbage has no benefit to the environment', 'This concept has no connection to waste management', 'Landfills never actually cause any pollution'], 0)]),
]),

day(97, [
L('Oral Communication: Storytelling with Expression',
  'Grade 3 Language strand: effective storytelling uses expression, such as changing your voice, volume, and pace, to bring characters and events to life for listeners.',
  [('Name one way a storyteller can use expression, such as changing their ___.', ['Voice', 'A concept unrelated to storytelling', 'Homework', 'Math equation'], 0),
   ('Why might a storyteller speak more quietly during a suspenseful moment?', ['To build tension and keep listeners engaged', 'Quiet speaking never adds anything to a story', 'This concept has no connection to storytelling', 'Suspenseful moments should always be spoken loudly'], 0),
   ('Why might a storyteller change the pace of their speech during an exciting chase scene?', ['To make the moment feel faster and more exciting for listeners', 'Changing pace never affects how a story feels', 'This concept has no connection to oral storytelling', 'A chase scene should always be told very slowly'], 0),
   ('Why is using expression important when telling a story aloud?', ['It helps bring characters and events to life for the listener', 'Expression never adds anything to a story told aloud', 'This concept has no connection to oral communication', 'Storytellers should always speak in a flat, unchanging voice'], 0),
   ('Which of these best shows a storyteller using expression?', ['Speaking in an excited, quick voice during an action scene', 'Speaking in the exact same flat tone the whole time', 'Reading silently without saying anything aloud', 'Whispering the entire story from start to finish'], 0)]),
M('Multiplication: Estimating Products',
  'Grade 3 Math strand: students estimate the product of a multiplication problem by rounding numbers first, giving a quick sense of whether an answer is reasonable.',
  [('To estimate a product, what should you do to the numbers first?', ['Round them', 'Divide them', 'A concept unrelated to estimating', 'Ignore them completely'], 0),
   ('Which is the best estimate for 29 times 4, after rounding 29 to the nearest ten?', ['120', '100', '150', '90'], 0),
   ('Which is the best estimate for 6 times 51, after rounding 51 to the nearest ten?', ['300', '250', '350', '200'], 0),
   ('Why is estimating a product before solving useful?', ['It helps you check whether your final answer is reasonable', 'Estimating a product is never useful', 'This concept has no connection to multiplication', 'Estimating always gives the exact correct answer'], 0),
   ('If you estimate 19 times 3 by rounding 19 to 20, what is your estimate?', ['60', '57', '50', '63'], 0)]),
Sc('Science: Coral Reefs: Ocean Ecosystems Full of Life',
   'Grade 3 Science strand: coral reefs are ocean ecosystems built by tiny living animals called coral polyps, providing habitat for a huge variety of fish and other sea creatures.',
   [('What tiny living animals build coral reefs?', ['Coral polyps', 'Fish', 'A concept unrelated to ocean ecosystems', 'Seaweed'], 0),
    ('Do coral reefs provide habitat for many fish and other sea creatures?', ['Yes', 'No, coral reefs support no living things', 'A concept unrelated to ocean ecosystems', 'Only one single fish can ever live on a reef'], 0),
    ('Where are coral reefs found, in fresh water or salt water?', ['Salt water, in the ocean', 'Fresh water, in lakes', 'A concept unrelated to coral reefs', 'Neither fresh nor salt water'], 0),
    ('Why are coral reefs sometimes called the rainforests of the ocean?', ['They support an enormous variety of living things, similar to a rainforest on land', 'Coral reefs actually contain trees just like a rainforest', 'This concept has no connection to coral reefs', 'Coral reefs support almost no living things at all'], 0),
    ('Why might warmer ocean water be harmful to coral reefs?', ['It can stress the coral and cause a harmful process called coral bleaching', 'Warmer water always helps coral grow faster with no downside', 'This concept has no connection to coral reefs', 'Ocean temperature never actually affects coral reefs'], 0)]),
SS('Social Studies: Public Libraries as Community Spaces',
   'Grade 3 Social Studies strand: public libraries are free community spaces that offer books, technology, and programs, supporting learning and connection for people of all ages.',
   [('What do we call a free community space that offers books and programs to the public?', ['A public library', 'A concept unrelated to community spaces', 'A private office', 'A factory'], 0),
    ('Name one thing a public library might offer besides books, such as ___.', ['Computers', 'A concept unrelated to libraries', 'Farm animals', 'Sports cars'], 0),
    ('Can people of all ages use a public library?', ['Yes', 'No, only adults are allowed', 'A concept unrelated to public libraries', 'Only children are allowed'], 0),
    ('Why are public libraries valuable to a community?', ['They offer free access to information, technology, and learning for everyone', 'Public libraries have no value to a community', 'This concept has no connection to community spaces', 'Libraries only benefit one single person'], 0),
    ('Why might a public library host programs like storytime or homework help?', ['To support learning and connection for different members of the community', 'Libraries never offer any programs at all', 'This concept has no relevance to community spaces', 'Programs at a library never help anyone learn'], 0)]),
]),

day(98, [
L('Vocabulary: Portmanteau (Blended) Words',
  'Grade 3 Language strand: a portmanteau, or blended word, is created by combining parts of two words to make a new word with a combined meaning, such as brunch from breakfast and lunch.',
  [('What do we call a word made by blending parts of two other words together?', ['A portmanteau, or blended word', 'A synonym', 'A concept unrelated to vocabulary', 'A homophone'], 0),
   ('The word brunch is a blend of which two words?', ['Breakfast and lunch', 'Bread and lunch', 'Breakfast and dinner', 'A concept unrelated to blended words'], 0),
   ('The word smog is a blend of which two words?', ['Smoke and fog', 'Smoke and frog', 'Small and fog', 'A concept unrelated to blended words'], 0),
   ('Why might people create a blended word like brunch instead of using two separate words?', ['It is a quick way to describe something that combines both ideas', 'Blended words never actually mean anything', 'This concept has no connection to vocabulary', 'Blended words always confuse the reader with no purpose'], 0),
   ('Which of these is an example of a blended word?', ['Motel, from motor and hotel', 'Happy, meaning glad', 'Slowly, describing how something moves', 'Jump, meaning to leap'], 0)]),
M('Probability: Predicting and Testing Outcomes with a Spinner',
  'Grade 3 Math strand: students make predictions about the likely outcome of spinning a spinner, then test their predictions by spinning it many times and recording the results.',
  [('What tool can be used to test predictions about chance, such as a ___?', ['Spinner', 'A concept unrelated to probability', 'A calendar', 'A ruler'], 0),
   ('If a spinner has 4 equal sections coloured red, blue, green, and yellow, is each colour equally likely?', ['Yes', 'No, red is always more likely', 'A concept unrelated to probability', 'Only blue can ever be spun'], 0),
   ('If you spin a spinner 20 times, is it likely that every single spin will land on the exact same colour?', ['No, it is unlikely', 'Yes, it is guaranteed', 'A concept unrelated to probability', 'The spinner will always stop working'], 0),
   ('Why do we test a prediction by spinning many times instead of just once?', ['Testing many times gives a better idea of the true likelihood of each outcome', 'Testing multiple times is never useful', 'This concept has no connection to probability', 'One single spin always gives a perfectly accurate result'], 0),
   ('If a spinner has 3 equal sections and 2 are blue while 1 is red, which colour is more likely to be spun?', ['Blue', 'Red', 'They are equally likely', 'Neither colour can ever be spun'], 0)]),
Sc('Science: The Difference Between Deciduous and Coniferous Trees',
   'Grade 3 Science strand: deciduous trees lose their broad leaves each fall, while coniferous trees keep their needle-like leaves year-round and often produce cones.',
   [('Do deciduous trees lose their leaves in the fall?', ['Yes', 'No, deciduous trees keep every leaf all year', 'A concept unrelated to trees', 'Only coniferous trees lose their leaves'], 0),
    ('Do coniferous trees usually keep their leaves year-round?', ['Yes', 'No, coniferous trees lose all their leaves every fall', 'A concept unrelated to trees', 'Coniferous trees have no leaves at all'], 0),
    ('What shape are the leaves of most coniferous trees?', ['Needle-like', 'Broad and flat', 'A concept unrelated to trees', 'Round like a circle'], 0),
    ('Name one thing coniferous trees often produce, such as ___.', ['Cones', 'A concept unrelated to trees', 'Flowers only', 'Nothing at all'], 0),
    ('Why might coniferous trees be better suited to survive harsh winters than deciduous trees?', ['Their needle-like leaves lose less water and can stay on the tree through winter', 'Coniferous trees always die during winter', 'This concept has no connection to tree adaptations', 'Needle-like leaves have no connection to surviving winter'], 0)]),
SS('Social Studies: Sports and Recreation in Ontario Communities',
   'Grade 3 Social Studies strand: sports and recreation programs, such as community sports leagues and public parks, help bring Ontario communities together and support healthy, active living.',
   [('Name one type of recreation program a community might offer, such as a ___.', ['Sports league', 'A concept unrelated to recreation', 'A tax form', 'A traffic law'], 0),
    ('Do public parks give community members a place for recreation?', ['Yes', 'No, parks have no connection to recreation', 'A concept unrelated to communities', 'Parks are only for looking at, never for playing'], 0),
    ('What is one benefit of community sports and recreation programs?', ['They support healthy, active living', 'They have no benefit to a community', 'A concept unrelated to recreation', 'They discourage people from being active'], 0),
    ('Why might a municipality build public parks and recreation centres?', ['To give community members places to be active and connect with each other', 'Municipalities never build any recreation spaces', 'This concept has no connection to community planning', 'Parks and recreation centres serve no purpose at all'], 0),
    ('Why can joining a community sports team help someone feel more connected to their community?', ['It creates opportunities to meet neighbours and build friendships through shared activities', 'Joining a sports team never helps anyone feel connected', 'This concept has no relevance to community life', 'Sports teams always keep people apart from each other'], 0)]),
]),

day(99, [
L('Reading: Text Features — Table of Contents and Index',
  'Grade 3 Language strand: a table of contents lists the sections of a book in order at the front, while an index at the back lists topics alphabetically with page numbers to help readers find information quickly.',
  [('Where would you usually find a table of contents in a book, the front or the back?', ['The front', 'The back', 'A concept unrelated to books', 'In the middle only'], 0),
   ('Where would you usually find an index in a book, the front or the back?', ['The back', 'The front', 'A concept unrelated to books', 'In the middle only'], 0),
   ('Is an index organized alphabetically?', ['Yes', 'No, it is organized randomly', 'A concept unrelated to text features', 'It is organized by page length'], 0),
   ('Why might a reader use a table of contents before reading a whole non-fiction book?', ['To quickly see what sections are inside and find a specific one', 'A table of contents never helps a reader find information', 'This concept has no connection to reading non-fiction', 'Readers should never look at a table of contents'], 0),
   ('Why is an index especially useful when looking for information on one specific topic?', ['It lists topics alphabetically with page numbers, so you can find them quickly', 'An index never lists any useful information', 'This concept has no connection to text features', 'An index is always identical to the table of contents'], 0)]),
M('Geometry: Perimeter of Regular Polygons',
  'Grade 3 Math strand: a regular polygon has sides that are all the same length, so its perimeter can be found by multiplying the length of one side by the number of sides.',
  [('What do we call a polygon whose sides are all the same length?', ['A regular polygon', 'An irregular polygon', 'A concept unrelated to geometry', 'A circle'], 0),
   ('If a regular pentagon has sides of 4 cm each, what is its perimeter?', ['20 cm', '16 cm', '24 cm', '9 cm'], 0),
   ('If a regular hexagon has sides of 3 cm each, what is its perimeter?', ['18 cm', '15 cm', '21 cm', '9 cm'], 0),
   ('To find the perimeter of a regular polygon, you can multiply the side length by the ___.', ['Number of sides', 'Number of angles only', 'Area of the shape', 'A concept unrelated to perimeter'], 0),
   ('If a square (a regular polygon) has a perimeter of 24 cm, how long is each side?', ['6 cm', '12 cm', '24 cm', '4 cm'], 0)]),
Sc('Science: How Roots, Stems, and Leaves Work Together',
   'Grade 3 Science strand: a plant’s roots, stem, and leaves work together as a system, with roots absorbing water, stems transporting it, and leaves using sunlight to make food.',
   [('What part of a plant absorbs water from the soil?', ['The roots', 'The leaves', 'The flower', 'A concept unrelated to plants'], 0),
    ('What part of a plant transports water from the roots to the leaves?', ['The stem', 'The flower', 'The seed', 'A concept unrelated to plants'], 0),
    ('What part of a plant uses sunlight to make food?', ['The leaves', 'The roots', 'The stem', 'A concept unrelated to plants'], 0),
    ('Why do roots, stems, and leaves need to work together as a system?', ['Each part depends on the others to help the whole plant survive and grow', 'The parts of a plant never actually depend on each other', 'This concept has no connection to plant biology', 'A plant can survive with only one of these parts working'], 0),
    ('Why might a plant wilt if its stem is damaged?', ['A damaged stem cannot properly transport water from the roots to the leaves', 'A damaged stem has no connection to how a plant gets water', 'This concept has no relevance to plant biology', 'Stems never actually transport anything in a plant'], 0)]),
SS('Social Studies: How Ontario’s Population Has Grown Over Time',
   'Grade 3 Social Studies strand: Ontario’s population has grown significantly over time due to factors such as immigration, higher birth rates, and people moving to cities for jobs.',
   [('Name one factor that can cause a province’s population to grow, such as ___.', ['Immigration', 'A concept unrelated to population', 'A math equation', 'A weather pattern'], 0),
    ('Has Ontario’s population grown significantly over time?', ['Yes', 'No, Ontario’s population has never changed', 'A concept unrelated to population growth', 'Ontario’s population has only ever shrunk'], 0),
    ('Why might people move to Ontario’s cities in search of jobs?', ['Cities often offer more job opportunities in different industries', 'Cities never offer any job opportunities', 'This concept has no connection to population growth', 'Jobs are never found in cities'], 0),
    ('Why is understanding population growth useful for planning a community’s future?', ['It helps governments plan for schools, housing, and services that a growing population will need', 'Population growth has no connection to community planning', 'This concept has no relevance to Ontario', 'Governments never need to plan for population changes'], 0),
    ('Why might a growing population lead to the building of more schools and hospitals in a community?', ['More people means a greater need for services like education and healthcare', 'A growing population never affects the need for services', 'This concept has no connection to community planning', 'Schools and hospitals are never built due to population growth'], 0)]),
]),

day(100, [
L('Review: Tone, Grammar, and Vocabulary',
  'Grade 3 Language strand review: students revisit tone and mood, irregular plural nouns, homographs, possessive nouns, and portmanteau words.',
  [('What do we call the author’s attitude toward a topic in a piece of writing?', ['Tone', 'A concept unrelated to reading', 'The title of the book', 'The page number'], 0),
   ('What is the plural form of the word child?', ['Children', 'Childs', 'Childes', 'Childies'], 0),
   ('What do we call two words that are spelled the same but have different meanings?', ['Homographs', 'Synonyms', 'Antonyms', 'A concept unrelated to vocabulary'], 0),
   ('What does a possessive noun show?', ['Ownership', 'A question', 'A concept unrelated to grammar', 'A silent letter'], 0),
   ('What do we call a word made by blending parts of two other words together?', ['A portmanteau, or blended word', 'A synonym', 'A concept unrelated to vocabulary', 'A homophone'], 0)]),
M('Review: Data, Geometry, and Number Sense',
  'Grade 3 Math strand review: students revisit primary and secondary data, classifying quadrilaterals, fact families, ordering numbers to 10 000, and perimeter of regular polygons.',
  [('What do we call data you collect yourself, such as through your own survey?', ['Primary data', 'Secondary data', 'A concept unrelated to data', 'Estimated data'], 0),
   ('How many sides does a quadrilateral have?', ['4', '3', '5', '6'], 0),
   ('What do we call a group of related addition and subtraction facts using the same three numbers?', ['A fact family', 'A concept unrelated to number sense', 'A number line', 'A place value chart'], 0),
   ('Which of these numbers is the smallest: 4 502, 4 250, 4 025?', ['4 025', '4 502', '4 250', 'They are all equal'], 0),
   ('What do we call a polygon whose sides are all the same length?', ['A regular polygon', 'An irregular polygon', 'A concept unrelated to geometry', 'A circle'], 0)]),
Sc('Review: Life Cycles, Habitats, and Plant Science',
   'Grade 3 Science strand review: students revisit frog life cycles, desert adaptations, insects versus spiders, deciduous versus coniferous trees, and how plant parts work together.',
   [('What is the first stage of a frog’s life cycle?', ['Egg', 'Tadpole', 'Adult frog', 'A concept unrelated to life cycles'], 0),
    ('Name one challenge desert plants and animals must survive, such as extreme heat.', ['Extreme heat', 'A concept unrelated to deserts', 'Constant flooding', 'Extremely cold winters only'], 0),
    ('How many legs does an insect have?', ['Six', 'Eight', 'Four', 'Ten'], 0),
    ('Do deciduous trees lose their leaves in the fall?', ['Yes', 'No, deciduous trees keep every leaf all year', 'A concept unrelated to trees', 'Only coniferous trees lose their leaves'], 0),
    ('What part of a plant absorbs water from the soil?', ['The roots', 'The leaves', 'The flower', 'A concept unrelated to plants'], 0)]),
SS('Review: Ontario History and Community Life',
   'Grade 3 Social Studies strand review: students revisit United Empire Loyalists, Black Loyalists, recycling programs, public libraries, and Ontario’s population growth.',
   [('What do we call settlers who stayed loyal to Britain during the American Revolution and moved north?', ['United Empire Loyalists', 'A concept unrelated to Canadian history', 'Confederation delegates', 'Early trading partners'], 0),
    ('What do we call formerly enslaved and free Black people who supported Britain during the American Revolution?', ['Black Loyalists', 'A concept unrelated to Canadian history', 'Confederation delegates', 'Fur traders'], 0),
    ('What do we call the coloured bin many Ontario homes use to collect recyclable materials?', ['The blue box', 'The green bin', 'A concept unrelated to recycling', 'The red bin'], 0),
    ('What do we call a free community space that offers books and programs to the public?', ['A public library', 'A concept unrelated to community spaces', 'A private office', 'A factory'], 0),
    ('Name one factor that can cause a province’s population to grow, such as ___.', ['Immigration', 'A concept unrelated to population', 'A math equation', 'A weather pattern'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_91_100)
    append_to(3, g3_91_100)
