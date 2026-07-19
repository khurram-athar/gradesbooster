#!/usr/bin/env python3
"""Grade 3, Days 81-90 -- extends Grade 3 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade3.json):
foreshadowing, interjections, prefixes re- and pre-, writing an invitation,
character motivation, comparative and superlative adjectives, antonyms in
context, supporting interpretations with text evidence, newspaper articles,
multiplying by 11 and 12, finding missing side lengths, surveys, numbers to
10 000, fraction word problems, multiplying by powers of ten, range in data,
converting units of time, profit and loss, winter adaptations,
photosynthesis basics, symbiosis, sustainable building materials, layers of
the atmosphere, tides, bird migration, sound through materials, density and
floating, Ontario manufacturing, municipal budgets, comparing provinces,
Indigenous place names, local non-profits, the Underground Railroad, water
conservation, weather and the economy, and civic participation.

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


g3_81_90 = [
day(81, [
L('Reading: Understanding Foreshadowing',
  'Grade 3 Language strand: foreshadowing is when an author gives a small hint early in a story about something that will happen later, building suspense for the reader.',
  [('Foreshadowing is when an author gives a small ___ early in a story about something that will happen later.', ['Hint', 'Summary of the whole ending', 'Concept unrelated to storytelling', 'List of every character’s name'], 0),
   ('What does foreshadowing help build for the reader?', ['Suspense', 'Confusion with no purpose', 'A concept unrelated to reading', 'A list of unrelated facts'], 0),
   ('If a story mentions dark storm clouds before a scary event, this is an example of ___.', ['Foreshadowing', 'A concept unrelated to storytelling', 'A grammar rule', 'A math pattern'], 0),
   ('Why might an author use foreshadowing instead of simply stating what will happen next?', ['It builds suspense and keeps readers curious about what comes next', 'Foreshadowing never adds anything to a story', 'This concept has no connection to storytelling', 'Authors should always reveal every event immediately'], 0),
   ('Why is it useful for readers to notice foreshadowing while reading?', ['It helps them make predictions and feel more engaged with the story', 'Noticing foreshadowing never helps a reader understand a story', 'Foreshadowing has no connection to predicting events', 'Readers should ignore every hint an author gives'], 0)]),
M('Multiplication: Multiplying by 11 and 12',
  'Grade 3 Math strand: students learn multiplication facts for the 11 and 12 times tables, building on earlier facts up to 10, using patterns to help memorize them.',
  [('What is 11 times 4?', ['44', '40', '48', '54'], 0),
   ('What is 12 times 3?', ['36', '32', '40', '24'], 0),
   ('What is 11 times 6?', ['66', '60', '72', '56'], 0),
   ('What pattern helps with multiplying single digits by 11, like 11 times 4?', ['The digit repeats twice, like 4 and 4 making 44', 'There is no pattern at all for multiplying by 11', 'The answer is always an odd number', 'The digit is always cut in half'], 0),
   ('What is 12 times 8?', ['96', '84', '108', '88'], 0)]),
Sc('Science: Adaptations for Winter Survival',
   'Grade 3 Science strand: animals survive cold winters using adaptations such as growing thicker fur, storing body fat, migrating to warmer places, or hibernating until spring.',
   [('Name one adaptation animals use to survive winter, such as growing thicker fur.', ['Growing thicker fur', 'Ignoring winter completely', 'A concept unrelated to survival', 'Losing all their fur'], 0),
    ('What do we call animals traveling to a warmer place for the winter?', ['Migrating', 'Hibernating', 'A concept unrelated to winter survival', 'Photosynthesizing'], 0),
    ('What do we call animals going into a deep sleep for the winter?', ['Hibernating', 'Migrating', 'A concept unrelated to winter survival', 'Evaporating'], 0),
    ('Why might storing body fat help an animal survive winter?', ['The fat provides stored energy when food is harder to find', 'Body fat has no connection to surviving winter', 'Storing fat makes animals colder', 'This concept has no relevance to winter survival'], 0),
    ('Why do different animals use different winter survival strategies, such as migrating versus hibernating?', ['Different species have different needs and abilities suited to their environment', 'All animals use the exact same winter strategy', 'Winter survival strategies have no connection to a species’ needs', 'This concept has no relevance to biology'], 0)]),
SS('Social Studies: Ontario’s Manufacturing Industry',
   'Grade 3 Social Studies strand: manufacturing is an important industry in Ontario, where factories produce goods such as cars, food products, and machinery that are sold across Canada and the world.',
   [('What do we call factories producing goods like cars and machinery?', ['Manufacturing', 'A concept unrelated to industry', 'Farming', 'Mining'], 0),
    ('Name one good that might be produced by Ontario manufacturing, such as cars.', ['Cars', 'A concept unrelated to manufacturing', 'Wild animals', 'Ocean water'], 0),
    ('Are goods made in Ontario manufacturing sold across Canada and the world?', ['Yes', 'No, they are never sold anywhere', 'A concept unrelated to manufacturing', 'Only sold to one single person'], 0),
    ('Why is manufacturing an important industry for Ontario’s economy?', ['It creates jobs and produces goods that can be sold locally and internationally', 'Manufacturing has no connection to Ontario’s economy', 'Manufacturing never creates any jobs', 'This concept has no relevance to Ontario'], 0),
    ('Why might a manufacturing plant choose to locate near a major highway or port?', ['It makes shipping goods to other places easier and faster', 'Location has no connection to how goods are shipped', 'Manufacturing plants never need to ship goods anywhere', 'This concept has no relevance to industry'], 0)]),
]),

day(82, [
L('Grammar: Interjections and Exclamations',
  'Grade 3 Language strand: an interjection is a short word or phrase that shows strong feeling, such as Wow! or Oh no!, often followed by an exclamation mark.',
  [('An interjection is a short word or phrase that shows ___.', ['Strong feeling', 'A math equation', 'A concept unrelated to grammar', 'A silent letter'], 0),
   ('Which of these is an example of an interjection?', ['Wow!', 'The', 'Cat', 'Run'], 0),
   ('An interjection is often followed by which punctuation mark?', ['An exclamation mark', 'A comma only', 'A concept unrelated to punctuation', 'Nothing at all'], 0),
   ('Why might a writer use an interjection like Oh no! in a story?', ['It quickly shows a character’s strong feeling or reaction', 'Interjections never add any meaning to writing', 'This concept has no connection to storytelling', 'Interjections always confuse the reader'], 0),
   ('Which sentence correctly uses an interjection?', ['Ouch! That really hurt.', 'That really Ouch hurt.', 'Hurt that Ouch really.', 'That hurt really Ouch.'], 0)]),
M('Geometry: Finding Missing Side Lengths',
  'Grade 3 Math strand: if you know the perimeter of a shape and the length of some of its sides, you can find a missing side length by subtracting the known sides from the total perimeter.',
  [('If a rectangle has a perimeter of 20 cm and three known sides add up to 14 cm, what is the missing side?', ['6 cm', '14 cm', '20 cm', '34 cm'], 0),
   ('If a square has a perimeter of 24 cm, what is the length of each side?', ['6 cm', '24 cm', '12 cm', '4 cm'], 0),
   ('If a shape’s perimeter is 30 cm and one side is missing while the rest total 22 cm, what is the missing side?', ['8 cm', '22 cm', '30 cm', '52 cm'], 0),
   ('To find a missing side length, you can subtract the known side lengths from the ___.', ['Total perimeter', 'Area of the shape', 'Number of vertices', 'Number of angles'], 0),
   ('Why is finding a missing side length a useful real-world skill?', ['It helps figure out unknown measurements when building or designing something', 'This concept has no real-world use at all', 'Missing side lengths can never be figured out', 'This concept only applies to circles'], 0)]),
Sc('Science: How Plants Make Their Own Food',
   'Grade 3 Science strand: plants make their own food through a process called photosynthesis, using sunlight, water, and air to produce the energy they need to grow.',
   [('What is the process called when plants make their own food using sunlight?', ['Photosynthesis', 'Migration', 'A concept unrelated to plants', 'Hibernation'], 0),
    ('Name one thing a plant needs for photosynthesis, such as sunlight.', ['Sunlight', 'A concept unrelated to photosynthesis', 'Only darkness', 'Only sand'], 0),
    ('Does photosynthesis give a plant the energy it needs to grow?', ['Yes', 'No, it has no connection to growth', 'A concept unrelated to plants', 'It only affects animals'], 0),
    ('Why do plants need sunlight for photosynthesis?', ['Sunlight provides the energy plants use to make their own food', 'Sunlight has no connection to how plants make food', 'Plants never actually need sunlight to grow', 'This concept has no relevance to plant biology'], 0),
    ('Why is photosynthesis important not just for plants, but for other living things too?', ['Photosynthesis produces oxygen that many living things need to breathe', 'Photosynthesis has no connection to other living things', 'Only plants benefit from photosynthesis in any way', 'This concept has no relevance to ecosystems'], 0)]),
SS('Social Studies: How Municipal Budgets Are Spent',
   'Grade 3 Social Studies strand: a municipal budget is a plan for how a local government spends the tax money it collects, often on services like roads, parks, libraries, and emergency services.',
   [('What do we call a plan for how a local government spends its money?', ['A municipal budget', 'A concept unrelated to government', 'A grocery list', 'A weather forecast'], 0),
    ('Name one service a municipal budget might fund, such as parks or libraries.', ['Parks', 'A concept unrelated to municipal budgets', 'Private vacations', 'Video games'], 0),
    ('Does a municipal government use tax money to plan its budget?', ['Yes', 'No, budgets never use tax money', 'A concept unrelated to government', 'Only businesses use budgets'], 0),
    ('Why must a municipal government carefully plan how it spends its budget?', ['So tax money is used fairly and effectively for shared community needs', 'Budgets have no connection to community needs', 'Municipal governments never need to plan spending', 'This concept has no relevance to local government'], 0),
    ('What might happen if a municipal government spent its whole budget on only one single service?', ['Other important services, like roads or libraries, might not get enough funding', 'Every other service would automatically get more funding instead', 'Municipal budgets have no effect on services', 'This concept has no connection to how communities are run'], 0)]),
]),

day(83, [
L('Vocabulary: Prefixes re- and pre-',
  'Grade 3 Language strand: the prefix re- often means again, as in rewrite meaning to write again, while the prefix pre- often means before, as in preview meaning to view before.',
  [('The prefix re- often means ___.', ['Again', 'Before', 'Never', 'A concept unrelated to prefixes'], 0),
   ('The prefix pre- often means ___.', ['Before', 'Again', 'Never', 'A concept unrelated to prefixes'], 0),
   ('Add the prefix re- to the word write. What new word do you make?', ['Rewrite', 'Prewrite', 'Written', 'Writing'], 0),
   ('Add the prefix pre- to the word view. What new word do you make?', ['Preview', 'Review', 'Viewing', 'Viewed'], 0),
   ('Why is it useful to know that pre- means before?', ['It helps you figure out the meaning of new words, like predict or prepare', 'Prefixes never help with understanding new words', 'This concept has no connection to vocabulary', 'The prefix pre- always means the opposite of before'], 0)]),
M('Data: Making a Survey and Analyzing Results',
  'Grade 3 Math strand: students learn to create a simple survey question, collect answers from classmates, organize the results in a chart or graph, and then analyze what the data shows.',
  [('What is the first step in conducting a survey?', ['Creating a survey question', 'Analyzing the results before asking anything', 'A concept unrelated to data collection', 'Throwing away all the answers'], 0),
   ('After collecting survey answers, what should you do next?', ['Organize the results in a chart or graph', 'Ignore all the answers completely', 'A concept unrelated to data', 'Ask the exact same question again with no purpose'], 0),
   ('If a survey shows 12 students prefer apples and 8 prefer oranges, which fruit is more popular?', ['Apples', 'Oranges', 'They are equally popular', 'Cannot tell from the data'], 0),
   ('Why might organizing survey results in a graph be helpful?', ['It makes the data easier to compare and understand at a glance', 'Graphs never help with understanding data', 'This concept has no connection to surveys', 'Organizing data always makes it more confusing'], 0),
   ('What does it mean to analyze survey results?', ['To look closely at the data and figure out what it shows', 'To immediately throw away the results', 'A concept unrelated to data collection', 'To ignore every answer collected'], 0)]),
Sc('Science: Symbiosis: How Living Things Help Each Other',
   'Grade 3 Science strand: symbiosis is a close relationship between two different living things, such as a bee and a flower, where both may benefit from helping each other survive.',
   [('What do we call a close relationship between two different living things?', ['Symbiosis', 'Migration', 'A concept unrelated to living things', 'Photosynthesis'], 0),
    ('Name one example of two living things helping each other, such as bees and flowers.', ['Bees and flowers', 'A concept unrelated to symbiosis', 'Rocks and sand', 'Clouds and rain'], 0),
    ('In a symbiotic relationship, can both living things benefit from helping each other?', ['Yes', 'No, only one living thing ever benefits', 'A concept unrelated to symbiosis', 'Living things never interact with each other'], 0),
    ('How does a bee help a flower in their symbiotic relationship?', ['The bee helps pollinate the flower as it collects nectar', 'The bee has no connection to how flowers grow', 'Bees never interact with flowers at all', 'This concept has no relevance to plant biology'], 0),
    ('Why is symbiosis an important concept for understanding ecosystems?', ['It shows how living things depend on and support one another', 'Symbiosis has no connection to how ecosystems work', 'Living things in an ecosystem never depend on each other', 'This concept has no relevance to science'], 0)]),
SS('Social Studies: Comparing Ontario to Other Provinces',
   'Grade 3 Social Studies strand: comparing Ontario to other Canadian provinces, such as British Columbia or Nova Scotia, shows differences in geography, industries, and population size.',
   [('Name one Canadian province other than Ontario, such as British Columbia.', ['British Columbia', 'A concept unrelated to Canadian provinces', 'A city in another country', 'An ocean'], 0),
    ('Do different provinces have different geography and industries?', ['Yes', 'No, every province is identical', 'A concept unrelated to provinces', 'Provinces never have any industries'], 0),
    ('Is Ontario one of the provinces that make up Canada?', ['Yes', 'No, Ontario is a separate country', 'A concept unrelated to Canada', 'Ontario is a city in another province'], 0),
    ('Why might comparing Ontario to another province help students understand Canada better?', ['It highlights how diverse Canada’s geography and communities really are', 'Comparing provinces never teaches anything useful', 'Every province in Canada is exactly the same in every way', 'This concept has no relevance to social studies'], 0),
    ('Which of these could be a reason two provinces have different major industries?', ['Differences in natural resources and geography', 'Every province has the exact same natural resources', 'Industries have no connection to geography', 'This concept has no relevance to Canada'], 0)]),
]),

day(84, [
L('Writing: Writing an Invitation',
  'Grade 3 Language strand: an invitation is a short piece of writing that tells the reader about an event, including the date, time, location, and what the event is for.',
  [('What kind of writing tells the reader about an event, including the date and time?', ['An invitation', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Name one detail an invitation should include, such as the date or location.', ['The date', 'A concept unrelated to invitations', 'A random unrelated fact', 'A math equation'], 0),
   ('Should an invitation clearly explain what the event is for?', ['Yes', 'No, invitations should never explain anything', 'A concept unrelated to invitations', 'Only the guest’s name matters'], 0),
   ('Why is it important for an invitation to include the exact time and location of an event?', ['So guests know exactly when and where to go', 'Time and location never matter for an invitation', 'This concept has no connection to writing an invitation', 'Guests should always guess the details themselves'], 0),
   ('Which of these would most likely appear in an invitation?', ['You are invited to a birthday party on Saturday at 2 p.m.', 'The water cycle has three main stages.', 'Add 4 and 5 to get 9.', 'A triangle has three sides.'], 0)]),
M('Number Sense: Numbers to 10 000',
  'Grade 3 Math strand: students extend their understanding of place value to read, write, and compare numbers up to 10 000, using knowledge of thousands, hundreds, tens, and ones.',
  [('What number comes right after 9 999?', ['10 000', '9 998', '10 100', '1 000'], 0),
   ('What digit is in the thousands place in the number 4 652?', ['4', '6', '5', '2'], 0),
   ('Which number is greater, 8 245 or 8 425?', ['8 425', '8 245', 'They are equal', 'Cannot tell'], 0),
   ('How many hundreds are in the number 3 720?', ['7', '3', '2', '0'], 0),
   ('Reading numbers up to 10 000 builds on our understanding of ___.', ['Place value', 'Only colours', 'Only shapes', 'Only time'], 0)]),
Sc('Science: Renewable Building Materials and Sustainable Design',
   'Grade 3 Science strand: sustainable design uses renewable or recycled materials, such as bamboo or reclaimed wood, to build things in ways that reduce harm to the environment.',
   [('What do we call design that uses renewable or recycled materials to reduce harm to the environment?', ['Sustainable design', 'A concept unrelated to building', 'A weather pattern', 'A math formula'], 0),
    ('Name one renewable building material, such as bamboo.', ['Bamboo', 'A concept unrelated to sustainable design', 'A rare metal that never regrows', 'A liquid found only in oceans'], 0),
    ('Does sustainable design try to reduce harm to the environment?', ['Yes', 'No, it tries to increase harm to the environment', 'A concept unrelated to building materials', 'It has no connection to the environment'], 0),
    ('Why might builders choose bamboo instead of a slower-growing tree for building materials?', ['Bamboo grows back quickly, making it a more renewable resource', 'Bamboo takes hundreds of years to regrow', 'This concept has no connection to sustainable design', 'Slow-growing trees are always more renewable than bamboo'], 0),
    ('Why is sustainable design becoming more important for builders today?', ['It helps protect natural resources and reduce environmental harm', 'Sustainable design has no benefit to the environment', 'Builders never need to consider the environment', 'This concept has no relevance to science'], 0)]),
SS('Social Studies: Indigenous Place Names in Ontario',
   'Grade 3 Social Studies strand: many places in Ontario, including lakes, rivers, and towns, have names that come from Indigenous languages and reflect a long history of Indigenous presence on the land.',
   [('Do many places in Ontario have names that come from Indigenous languages?', ['Yes', 'No, no places have Indigenous names', 'A concept unrelated to Ontario', 'Only cities in other countries have this feature'], 0),
    ('Name one type of place that might have an Indigenous name, such as a lake or river.', ['A lake', 'A concept unrelated to place names', 'A planet', 'A cartoon character'], 0),
    ('Do Indigenous place names reflect a long history of Indigenous presence on the land?', ['Yes', 'No, they have no connection to history', 'A concept unrelated to Indigenous Peoples', 'They were created only last year'], 0),
    ('Why is it valuable to learn the meanings behind Indigenous place names?', ['It helps us understand and respect the deep history of the land', 'Place names never have any real meaning', 'This concept has no connection to Ontario’s history', 'Learning place names is not worthwhile at all'], 0),
    ('What might an Indigenous place name for a lake tell us about that location?', ['It might describe a feature of the land or its importance to the people who named it', 'Place names never describe anything about a location', 'This concept has no connection to geography', 'Indigenous place names are always chosen randomly'], 0)]),
]),

day(85, [
L('Reading: Character Motivation — Why Characters Act',
  'Grade 3 Language strand: character motivation is the reason behind a character’s actions in a story, helping readers understand why a character makes certain choices.',
  [('What do we call the reason behind a character’s actions in a story?', ['Character motivation', 'A concept unrelated to reading', 'The book’s title', 'The illustrator’s name'], 0),
   ('Does understanding character motivation help readers know why a character makes certain choices?', ['Yes', 'No, motivation has no connection to choices', 'A concept unrelated to stories', 'Motivation only applies to real people, never characters'], 0),
   ('If a character shares their lunch because they are kind, what is their motivation?', ['Kindness', 'A concept unrelated to motivation', 'The book’s page number', 'The weather in the story'], 0),
   ('Why might two characters react differently to the same problem in a story?', ['They may have different motivations or feelings driving their actions', 'All characters always react in exactly the same way', 'Motivation never affects how a character behaves', 'This concept has no connection to storytelling'], 0),
   ('How does understanding character motivation deepen a reader’s enjoyment of a story?', ['It helps readers connect with why characters do what they do', 'Motivation never adds anything to a story', 'This concept has no relevance to reading comprehension', 'Readers should never think about why characters act'], 0)]),
M('Fractions: Fraction Word Problems',
  'Grade 3 Math strand: students solve word problems involving fractions, such as figuring out how much pizza is left after a fraction of it has been eaten.',
  [('If a pizza is cut into 8 slices and 3 slices are eaten, what fraction of the pizza is left?', ['5 eighths', '3 eighths', '8 eighths', '1 eighth'], 0),
   ('If a class has 12 students and 1 fourth of them wear glasses, how many students wear glasses?', ['3', '4', '6', '12'], 0),
   ('If a garden has 10 flowers and 2 tenths of them are red, how many flowers are red?', ['2', '10', '5', '8'], 0),
   ('Solving fraction word problems helps us understand fractions as ___.', ['Parts of a real, whole amount', 'Numbers with no real meaning', 'A concept unrelated to math', 'Only decimals, never fractions'], 0),
   ('If a ribbon is cut into 6 equal pieces and 4 pieces are used, what fraction of the ribbon is left?', ['2 sixths', '4 sixths', '6 sixths', '1 sixth'], 0)]),
Sc('Science: The Layers of the Atmosphere',
   'Grade 3 Science strand: Earth’s atmosphere has different layers, including the troposphere near the ground where weather happens, and higher layers that stretch into space.',
   [('What is the name of the atmosphere’s layer closest to the ground, where weather happens?', ['The troposphere', 'A concept unrelated to the atmosphere', 'The rock cycle', 'The water cycle'], 0),
    ('Does the atmosphere have more than one layer?', ['Yes', 'No, it is a single layer', 'A concept unrelated to Earth', 'The atmosphere does not exist'], 0),
    ('Do the higher layers of the atmosphere stretch into space?', ['Yes', 'No, the atmosphere never reaches space', 'A concept unrelated to layers', 'Only the ocean reaches space'], 0),
    ('Why does most of our weather happen in the troposphere?', ['It is the lowest layer, closest to Earth’s surface and its water and heat', 'Weather never happens in the troposphere', 'This concept has no connection to Earth’s atmosphere', 'The troposphere is the layer farthest from Earth'], 0),
    ('Why is it useful for scientists to study the different layers of the atmosphere?', ['It helps them understand weather, climate, and conditions in space', 'Studying atmosphere layers has no scientific value', 'The atmosphere has no connection to weather or climate', 'This concept has no relevance to Earth science'], 0)]),
SS('Social Studies: The Role of Non-Profits and Charities Locally',
   'Grade 3 Social Studies strand: local non-profits and charities work to help people in the community, such as providing food, shelter, or support, often relying on volunteers and donations.',
   [('What do we call organizations that help people in the community using donations, not profit?', ['Non-profits or charities', 'A concept unrelated to community help', 'Grocery stores', 'Banks'], 0),
    ('Name one thing a local charity might provide, such as food or shelter.', ['Food', 'A concept unrelated to charities', 'Video games', 'Sports cars'], 0),
    ('Do non-profits and charities often rely on volunteers and donations?', ['Yes', 'No, they never need any help', 'A concept unrelated to charities', 'They only rely on selling products'], 0),
    ('Why might a community rely on local charities to help people in need?', ['Charities can provide support that fills gaps in the community', 'Charities never actually help anyone', 'This concept has no connection to community support', 'Communities never need any extra support'], 0),
    ('How can volunteering at a local charity benefit both the volunteer and the community?', ['The volunteer helps others while also building skills and connections', 'Volunteering never benefits anyone involved', 'This concept has no relevance to community life', 'Charities never accept help from volunteers'], 0)]),
]),

day(86, [
L('Grammar: Comparative and Superlative Adjectives',
  'Grade 3 Language strand: a comparative adjective, like taller, compares two things, while a superlative adjective, like tallest, compares three or more things to show the most extreme.',
  [('A comparative adjective, like taller, compares how many things?', ['Two', 'Three or more', 'Zero', 'A concept unrelated to grammar'], 0),
   ('A superlative adjective, like tallest, compares how many things?', ['Three or more', 'Only two', 'Zero', 'A concept unrelated to grammar'], 0),
   ('Which word is the comparative form of tall?', ['Taller', 'Tallest', 'Tall', 'Talling'], 0),
   ('Which word is the superlative form of tall?', ['Tallest', 'Taller', 'Tall', 'Talling'], 0),
   ('Why might a writer use the superlative biggest instead of the comparative bigger?', ['Superlatives compare three or more things to show the most extreme', 'Superlatives and comparatives always mean the exact same thing', 'This concept has no connection to grammar', 'Comparatives always compare more things than superlatives'], 0)]),
M('Multiplication: Multiplying by Powers of Ten',
  'Grade 3 Math strand: students learn a pattern for multiplying whole numbers by 10 or 100, noticing that one or two zeros are added to the original number.',
  [('What is 5 times 10?', ['50', '5', '500', '15'], 0),
   ('What is 5 times 100?', ['500', '50', '5 000', '15'], 0),
   ('What is 23 times 10?', ['230', '23', '2 300', '233'], 0),
   ('When multiplying a whole number by 10, what pattern happens to the digits?', ['One zero is added to the end of the number', 'The number is cut in half', 'A concept unrelated to multiplication patterns', 'The digits are rearranged randomly'], 0),
   ('What is 40 times 100?', ['4 000', '400', '40 000', '440'], 0)]),
Sc('Science: Tides and the Moon’s Pull',
   'Grade 3 Science strand: tides are the rise and fall of ocean water levels, caused mostly by the pull of the Moon’s gravity on Earth’s oceans.',
   [('What do we call the rise and fall of ocean water levels?', ['Tides', 'A concept unrelated to oceans', 'Erosion', 'Precipitation'], 0),
    ('What mostly causes tides to happen?', ['The pull of the Moon’s gravity', 'The colour of the ocean', 'A concept unrelated to tides', 'The temperature of the sand'], 0),
    ('Does the Moon’s gravity pull on Earth’s oceans?', ['Yes', 'No, the Moon has no gravity at all', 'A concept unrelated to tides', 'Only the Sun affects tides'], 0),
    ('Why do coastal communities need to understand the timing of tides?', ['It can affect activities like fishing, boating, and beach safety', 'Tides never affect anything near the coast', 'This concept has no connection to coastal communities', 'Tides only happen once a year'], 0),
    ('Why is it the Moon, rather than a nearby mountain, that has the biggest effect on ocean tides?', ['The Moon’s gravity, though it is far away, is strong enough and close enough to pull on the huge mass of ocean water', 'Mountains have a much stronger gravitational pull than the Moon', 'Gravity has no connection to the Moon at all', 'This concept has no relevance to science'], 0)]),
SS('Social Studies: Ontario’s Role in the Underground Railroad',
   'Grade 3 Social Studies strand: the Underground Railroad was a network of secret routes and safe houses that helped freedom seekers escape enslavement, with many settling in communities across Ontario.',
   [('What do we call the secret network of routes that helped freedom seekers escape enslavement?', ['The Underground Railroad', 'A concept unrelated to Canadian history', 'A modern subway system', 'A type of farm equipment'], 0),
    ('Did many freedom seekers settle in communities across Ontario?', ['Yes', 'No, none ever settled in Ontario', 'A concept unrelated to history', 'They only settled in a different country'], 0),
    ('Was the Underground Railroad an actual railroad with trains?', ['No, it was a network of secret routes and safe houses', 'Yes, it used real trains and tracks', 'A concept unrelated to history', 'It was a type of highway'], 0),
    ('Why is the Underground Railroad an important part of Ontario’s history?', ['It shows how communities in Ontario provided safety and new beginnings for freedom seekers', 'The Underground Railroad has no connection to Ontario', 'This event never actually affected Ontario', 'This concept has no relevance to social studies'], 0),
    ('Why might learning about the Underground Railroad help students understand Ontario’s diversity today?', ['It helps explain part of the history behind some communities in Ontario', 'This history has no connection to Ontario’s communities today', 'Ontario’s diversity has no connection to its history', 'This concept has no relevance to social studies'], 0)]),
]),

day(87, [
L('Vocabulary: Antonyms in Context',
  'Grade 3 Language strand: an antonym is a word that means the opposite of another word, and understanding antonyms in context can help readers understand contrasts within a sentence.',
  [('What do we call a word that means the opposite of another word?', ['An antonym', 'A synonym', 'A concept unrelated to vocabulary', 'A homophone'], 0),
   ('What is an antonym for the word happy?', ['Sad', 'Joyful', 'Cheerful', 'Glad'], 0),
   ('What is an antonym for the word fast?', ['Slow', 'Quick', 'Speedy', 'Rapid'], 0),
   ('In the sentence The weather was hot yesterday but cold today, which two words are antonyms?', ['Hot and cold', 'Weather and today', 'Yesterday and today', 'Was and but'], 0),
   ('Why is understanding antonyms useful when reading a sentence with the word but?', ['The word but often signals a contrast, which antonyms can help show', 'Antonyms never appear near the word but', 'This concept has no connection to reading comprehension', 'The word but never signals any kind of contrast'], 0)]),
M('Data: Understanding Range in a Data Set',
  'Grade 3 Math strand: the range of a data set is the difference between the highest and lowest values, found by subtracting the smallest number from the largest number.',
  [('What do we call the difference between the highest and lowest values in a data set?', ['The range', 'The mode', 'A concept unrelated to data', 'The average'], 0),
   ('If a data set has a highest value of 15 and a lowest value of 5, what is the range?', ['10', '20', '15', '5'], 0),
   ('If a data set has a highest value of 30 and a lowest value of 12, what is the range?', ['18', '42', '30', '12'], 0),
   ('To find the range, you subtract the ___ value from the ___ value.', ['Smallest, largest', 'Largest, smallest', 'Middle, largest', 'Smallest, middle'], 0),
   ('Why might knowing the range of a data set be useful?', ['It shows how spread out the data values are', 'The range never tells us anything useful', 'This concept has no connection to data', 'The range only applies to fractions'], 0)]),
Sc('Science: Migration Patterns of Canadian Birds',
   'Grade 3 Science strand: many Canadian birds migrate, or travel long distances, each year to find warmer weather and more available food during the winter months.',
   [('What do we call birds traveling long distances each year to find warmer weather?', ['Migrating', 'Hibernating', 'A concept unrelated to birds', 'Photosynthesizing'], 0),
    ('Why do many Canadian birds migrate during the winter?', ['To find warmer weather and more available food', 'To find colder weather with less food', 'A concept unrelated to migration', 'Birds never actually migrate'], 0),
    ('Do birds migrate the same route every single year?', ['Often, yes, many birds follow similar migration routes', 'No, migration routes are always completely random', 'A concept unrelated to migration', 'Birds never repeat any behaviour'], 0),
    ('Why might migrating long distances be a risky journey for birds?', ['They may face bad weather, predators, or a lack of food along the way', 'Migration is never risky for any bird', 'This concept has no connection to bird migration', 'Birds never face any challenges while migrating'], 0),
    ('Why is understanding bird migration patterns helpful for conservation efforts?', ['It helps scientists protect the habitats birds depend on throughout their journey', 'Migration patterns have no connection to conservation', 'Birds never need any habitats to be protected', 'This concept has no relevance to science'], 0)]),
SS('Social Studies: Water Conservation in Ontario Communities',
   'Grade 3 Social Studies strand: water conservation means using fresh water carefully and avoiding waste, an important practice for Ontario communities to protect this valuable resource.',
   [('What word describes using fresh water carefully and avoiding waste?', ['Water conservation', 'A concept unrelated to resources', 'Water pollution', 'Water evaporation'], 0),
    ('Name one way a community might practise water conservation, such as fixing leaky pipes.', ['Fixing leaky pipes', 'A concept unrelated to water conservation', 'Leaving taps running all day', 'Wasting water on purpose'], 0),
    ('Is fresh water a valuable resource that Ontario communities should protect?', ['Yes', 'No, fresh water has no value at all', 'A concept unrelated to resources', 'Fresh water can never run low'], 0),
    ('Why is it important for communities to conserve water even though Ontario has many lakes?', ['Clean, usable fresh water still requires careful management and can become limited', 'Ontario has no lakes at all', 'Water conservation is never necessary near lakes', 'This concept has no relevance to Ontario communities'], 0),
    ('Which of these is an example of good water conservation?', ['Turning off the tap while brushing your teeth', 'Leaving a hose running all day for no reason', 'Wasting water on purpose to see what happens', 'Ignoring a leaking pipe for as long as possible'], 0)]),
]),

day(88, [
L('Reading: Supporting Interpretations with Evidence from the Text',
  'Grade 3 Language strand: when readers share an idea about a story, they should support it with evidence, specific details or quotes from the text that back up their thinking.',
  [('When sharing an idea about a story, what should readers use to support it?', ['Evidence from the text', 'A concept unrelated to reading', 'A completely unrelated topic', 'Their own made-up facts with no connection to the story'], 0),
   ('What do we call specific details or quotes from a text used to support an idea?', ['Evidence', 'A concept unrelated to reading', 'A grammar rule', 'A math formula'], 0),
   ('If you think a character is brave, what should you do to support that idea?', ['Point to a specific action or detail from the story', 'Ignore the story completely', 'A concept unrelated to reading comprehension', 'Make up a fact with no connection to the story'], 0),
   ('Why is it important to support an interpretation with evidence from the text?', ['It shows the idea is based on what actually happens in the story', 'Evidence never helps explain an idea about a story', 'This concept has no connection to reading comprehension', 'Interpretations never need any support at all'], 0),
   ('Which of these is an example of using evidence to support an idea?', ['The character must be kind because she shared her lunch with a hungry classmate', 'The character is kind because kindness is a nice word', 'The character is kind because the book has a blue cover', 'The character is kind because the story is five pages long'], 0)]),
M('Time: Converting Between Units of Time',
  'Grade 3 Math strand: students learn to convert between units of time, such as figuring out how many days are in two weeks or how many months are in a year.',
  [('How many days are in one week?', ['7', '5', '10', '30'], 0),
   ('How many days are in two weeks?', ['14', '7', '21', '10'], 0),
   ('How many months are in one year?', ['12', '10', '52', '365'], 0),
   ('If a project takes 3 weeks, how many days is that?', ['21', '14', '7', '28'], 0),
   ('Converting between units of time, like weeks and days, helps us understand ___.', ['How different measures of time relate to each other', 'Only how to tell time on a clock', 'A concept unrelated to time', 'Only how to read a calendar'], 0)]),
Sc('Science: How Sound Travels Through Different Materials',
   'Grade 3 Science strand: sound can travel through solids, liquids, and gases, but it travels at different speeds depending on the material, often moving fastest through solids.',
   [('Can sound travel through solids, liquids, and gases?', ['Yes', 'No, sound can only travel through air', 'A concept unrelated to sound', 'Sound cannot travel at all'], 0),
    ('Does sound often travel fastest through solids, liquids, or gases?', ['Solids', 'Gases', 'A concept unrelated to sound', 'Sound travels at the same speed everywhere'], 0),
    ('If you put your ear against a table, might you hear a tap on the other end travel through the solid wood?', ['Yes', 'No, sound cannot travel through solids at all', 'A concept unrelated to sound', 'Only liquids can carry sound'], 0),
    ('Why might sound travel differently through water compared to air?', ['Water and air have different properties that affect how sound waves move through them', 'Sound never travels through water at all', 'This concept has no connection to how sound works', 'Water and air are exactly identical for sound travel'], 0),
    ('Why is it useful for scientists to understand how sound travels through different materials?', ['It helps with technology like sonar, hearing aids, and soundproofing', 'This concept has no real-world use at all', 'Sound never actually needs to travel through anything', 'This concept has no relevance to science'], 0)]),
SS('Social Studies: How Weather Affects Ontario’s Economy',
   'Grade 3 Social Studies strand: weather can affect Ontario’s economy in many ways, such as impacting farming harvests, winter tourism, and how goods are transported.',
   [('Name one part of Ontario’s economy that weather can affect, such as farming.', ['Farming', 'A concept unrelated to weather', 'The alphabet', 'A math equation'], 0),
    ('Can weather impact how goods are transported across Ontario?', ['Yes', 'No, weather never affects transportation', 'A concept unrelated to the economy', 'Transportation never depends on weather'], 0),
    ('Might winter weather affect tourism in Ontario, such as ski resorts?', ['Yes', 'No, tourism is never affected by weather', 'A concept unrelated to weather', 'Weather has no connection to tourism'], 0),
    ('Why might a poor harvest season due to bad weather affect Ontario’s economy?', ['Farmers may produce and sell less, affecting jobs and food supply', 'Weather never has any effect on farming', 'This concept has no connection to the economy', 'Harvests are never affected by weather at all'], 0),
    ('Why is it important for businesses to plan for different kinds of weather?', ['Weather can affect how goods are made, transported, and sold', 'Weather never has any impact on businesses', 'This concept has no relevance to the economy', 'Businesses never need to plan for anything'], 0)]),
]),

day(89, [
L('Writing: Writing a Newspaper Article',
  'Grade 3 Language strand: a newspaper article reports facts about a real event, usually answering who, what, when, where, and why, often starting with the most important information first.',
  [('What kind of writing reports facts about a real event?', ['A newspaper article', 'A concept unrelated to writing', 'A grocery list', 'A birthday invitation'], 0),
   ('Name one question a newspaper article often answers, such as who or what.', ['Who', 'A concept unrelated to newspaper articles', 'A random unrelated question', 'A math question'], 0),
   ('Does a newspaper article usually start with the most important information first?', ['Yes', 'No, it always starts with the least important detail', 'A concept unrelated to writing', 'It never has any order at all'], 0),
   ('Why might a newspaper article put the most important information at the very beginning?', ['So readers can quickly learn the key facts even if they stop reading early', 'Important information should always be hidden until the very end', 'This concept has no connection to writing a newspaper article', 'Order has no effect on how an article is understood'], 0),
   ('Which of these questions would most likely be answered in a newspaper article about a local event?', ['Who attended the event and why did it happen?', 'What is your favourite colour?', 'How do you spell the word cat?', 'What is two plus two?'], 0)]),
M('Financial Literacy: Simple Profit and Loss in a Lemonade Stand',
  'Grade 3 Math strand: students learn that profit is the money left over after subtracting the cost of supplies from the money earned, while a loss happens if costs are higher than earnings.',
  [('What do we call the money left over after subtracting costs from earnings?', ['Profit', 'A concept unrelated to money', 'A loss', 'Interest'], 0),
   ('If a lemonade stand earns 20 dollars and supplies cost 8 dollars, what is the profit?', ['12 dollars', '28 dollars', '8 dollars', '20 dollars'], 0),
   ('If a lemonade stand earns 10 dollars but supplies cost 15 dollars, is that a profit or a loss?', ['A loss', 'A profit', 'Neither a profit nor a loss', 'Cannot tell'], 0),
   ('To find profit, you subtract the cost of supplies from the ___.', ['Money earned', 'Number of cups sold', 'Number of customers', 'Price of one single lemonade'], 0),
   ('Why is it useful for someone running a lemonade stand to track their costs and earnings?', ['It helps them see whether they made a profit or a loss', 'Tracking money never helps anyone understand a business', 'This concept has no connection to running a stand', 'Profit and loss have no connection to money'], 0)]),
Sc('Science: Investigating Density: Why Some Things Float',
   'Grade 3 Science strand: density describes how tightly packed the matter is inside an object, and objects less dense than water will float, while denser objects will sink.',
   [('What word describes how tightly packed the matter is inside an object?', ['Density', 'A concept unrelated to matter', 'Gravity', 'Friction'], 0),
    ('Will an object less dense than water float or sink?', ['Float', 'Sink', 'A concept unrelated to density', 'It disappears completely'], 0),
    ('Will an object denser than water float or sink?', ['Sink', 'Float', 'A concept unrelated to density', 'It disappears completely'], 0),
    ('Why does a large, heavy boat make of metal float, even though metal itself can sink?', ['The boat’s shape spreads out its weight so its overall density is less than water', 'Metal always floats no matter its shape', 'This concept has no connection to density', 'Boats never actually float on water'], 0),
    ('Why is understanding density a useful science concept?', ['It helps explain why some objects float and others sink', 'Density has no connection to floating or sinking', 'This concept has no relevance to science', 'Every object has the exact same density'], 0)]),
SS('Social Studies: Volunteering and Civic Participation',
   'Grade 3 Social Studies strand: civic participation means taking an active part in your community, such as volunteering, voting when old enough, or attending community meetings.',
   [('What word describes taking an active part in your community?', ['Civic participation', 'A concept unrelated to community', 'A math term', 'A weather pattern'], 0),
    ('Name one example of civic participation, such as volunteering.', ['Volunteering', 'A concept unrelated to civic participation', 'Ignoring your community', 'Refusing to help others'], 0),
    ('Is voting when old enough considered a form of civic participation?', ['Yes', 'No, voting has no connection to civic participation', 'A concept unrelated to community', 'Only adults can ever participate in a community'], 0),
    ('Why is civic participation important for a healthy community?', ['It helps community members have a voice and contribute to shared decisions', 'Civic participation has no benefit to a community', 'Communities function better with no participation at all', 'This concept has no relevance to social studies'], 0),
    ('Which of these is an example of a young person practising civic participation?', ['Volunteering to help clean up a local park', 'Refusing to help with any community event', 'Ignoring opportunities to help others', 'Avoiding all community activities'], 0)]),
]),

day(90, [
L('Review: Foreshadowing, Grammar, and Vocabulary',
  'Grade 3 Language strand review: students revisit foreshadowing, interjections, prefixes re- and pre-, invitations, character motivation, comparative and superlative adjectives, antonyms, evidence from text, and newspaper articles.',
  [('Foreshadowing is when an author gives a small ___ early in a story about something that will happen later.', ['Hint', 'Summary of the whole ending', 'Concept unrelated to storytelling', 'List of every character’s name'], 0),
   ('Which of these is an example of an interjection?', ['Wow!', 'The', 'Cat', 'Run'], 0),
   ('The prefix re- often means ___.', ['Again', 'Before', 'Never', 'A concept unrelated to prefixes'], 0),
   ('What do we call the reason behind a character’s actions in a story?', ['Character motivation', 'A concept unrelated to reading', 'The book’s title', 'The illustrator’s name'], 0),
   ('What do we call a word that means the opposite of another word?', ['An antonym', 'A synonym', 'A concept unrelated to vocabulary', 'A homophone'], 0)]),
M('Review: Multiplication, Fractions, and Data',
  'Grade 3 Math strand review: students revisit multiplying by 11 and 12, missing side lengths, surveys, numbers to 10 000, fraction word problems, powers of ten, range, time conversions, and profit and loss.',
  [('What is 11 times 4?', ['44', '40', '48', '54'], 0),
   ('If a rectangle has a perimeter of 20 cm and three known sides add up to 14 cm, what is the missing side?', ['6 cm', '14 cm', '20 cm', '34 cm'], 0),
   ('What number comes right after 9 999?', ['10 000', '9 998', '10 100', '1 000'], 0),
   ('If a pizza is cut into 8 slices and 3 slices are eaten, what fraction of the pizza is left?', ['5 eighths', '3 eighths', '8 eighths', '1 eighth'], 0),
   ('What is 5 times 100?', ['500', '50', '5 000', '15'], 0)]),
Sc('Review: Ecosystems, Earth Science, and Physical Science',
   'Grade 3 Science strand review: students revisit winter adaptations, photosynthesis, symbiosis, sustainable materials, atmosphere layers, tides, bird migration, sound through materials, and density.',
   [('Name one adaptation animals use to survive winter, such as growing thicker fur.', ['Growing thicker fur', 'Ignoring winter completely', 'A concept unrelated to survival', 'Losing all their fur'], 0),
    ('What is the process called when plants make their own food using sunlight?', ['Photosynthesis', 'Migration', 'A concept unrelated to plants', 'Hibernation'], 0),
    ('What do we call a close relationship between two different living things?', ['Symbiosis', 'Migration', 'A concept unrelated to living things', 'Photosynthesis'], 0),
    ('What mostly causes tides to happen?', ['The pull of the Moon’s gravity', 'The colour of the ocean', 'A concept unrelated to tides', 'The temperature of the sand'], 0),
    ('Will an object less dense than water float or sink?', ['Float', 'Sink', 'A concept unrelated to density', 'It disappears completely'], 0)]),
SS('Review: Industry, History, and Civic Life',
   'Grade 3 Social Studies strand review: students revisit Ontario manufacturing, municipal budgets, comparing provinces, Indigenous place names, local charities, the Underground Railroad, water conservation, weather and the economy, and civic participation.',
   [('What do we call factories producing goods like cars and machinery?', ['Manufacturing', 'A concept unrelated to industry', 'Farming', 'Mining'], 0),
    ('What do we call a plan for how a local government spends its money?', ['A municipal budget', 'A concept unrelated to government', 'A grocery list', 'A weather forecast'], 0),
    ('What do we call the secret network of routes that helped freedom seekers escape enslavement?', ['The Underground Railroad', 'A concept unrelated to Canadian history', 'A modern subway system', 'A type of farm equipment'], 0),
    ('What word describes using fresh water carefully and avoiding waste?', ['Water conservation', 'A concept unrelated to resources', 'Water pollution', 'Water evaporation'], 0),
    ('What word describes taking an active part in your community?', ['Civic participation', 'A concept unrelated to community', 'A math term', 'A weather pattern'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g3_81_90)
    append_to(3, g3_81_90)
