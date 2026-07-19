#!/usr/bin/env python3
"""Grade 5, Days 81-90 -- extends Grade 5 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade5.json):
tone, gerunds and participles, compare-and-contrast essays, allusion,
satire, appositives, Greek and Latin roots, letters to the editor,
multiple perspectives; proportional reasoning with recipes, volume of
cylinders, box-and-whisker plots, two-step equations, loans and debt,
converting imperial and metric units, Fibonacci-like sequences,
misleading graphs, independent vs dependent events; genetics basics, the
lymphatic system, sustainable forestry, satellites, acids and bases,
wetlands, earthquake-resistant design, batteries, hurricanes and
tornadoes; Canada's space program, the CFL and sports culture, world time
zones, refugees, postal history, the national anthem, NGOs, mining,
and the history of Canadian universities.

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


def _rebalance_answer_positions(days, seed=20260924):
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


g5_81_90 = [
day(81, [
L('Reading: Analyzing Tone in a Text',
  'Grade 5 Language strand: tone is the author’s attitude toward a subject, expressed through word choice, such as a playful tone, a serious tone, or a sarcastic tone.',
  [('What do we call the author’s attitude toward a subject, shown through word choice?', ['Tone', 'A concept unrelated to reading', 'The setting', 'The plot'], 0),
   ('Which of these words could describe a serious tone?', ['Solemn', 'Playful', 'Silly', 'Goofy'], 0),
   ('Which of these words could describe a playful tone?', ['Lighthearted', 'Solemn', 'Grim', 'Mournful'], 0),
   ('Why might an author’s word choice reveal their tone toward a topic?', ['Certain words carry feelings that hint at the author’s attitude', 'Word choice never has any connection to tone', 'This concept has no connection to reading comprehension', 'Every word in every text carries the exact same tone'], 0),
   ('Why is recognizing tone helpful when reading a persuasive article?', ['It can reveal how the author truly feels about the topic, beyond the facts alone', 'Tone never affects how a persuasive article should be understood', 'This concept has no relevance to reading comprehension', 'Tone and persuasion have no connection to each other'], 0)]),
M('Proportional Reasoning: Scaling Recipes Up and Down',
  'Grade 5 Math strand: students use proportional reasoning to scale a recipe up or down, such as doubling every ingredient amount to serve twice as many people.',
  [('If a recipe needs 2 cups of flour to serve 4 people, how much flour is needed to serve 8 people?', ['4 cups', '2 cups', '8 cups', '1 cup'], 0),
   ('If a recipe needs 3 eggs to serve 6 people, how many eggs are needed to serve 3 people?', ['1 and a half eggs', '3 eggs', '6 eggs', '2 eggs'], 0),
   ('If doubling a recipe means doubling every ingredient, what happens if you triple a recipe?', ['Every ingredient amount is tripled', 'Only one ingredient changes', 'A concept unrelated to proportional reasoning', 'The recipe stays exactly the same'], 0),
   ('Why is proportional reasoning useful when adjusting a recipe for a different number of people?', ['It helps keep the same ratio between ingredients so the recipe still works', 'Proportional reasoning never helps with adjusting recipes', 'This concept has no connection to math', 'Recipes never need any ingredient adjustments'], 0),
   ('If a recipe needs 1 cup of sugar to serve 2 people, how much sugar is needed to serve 10 people?', ['5 cups', '2 cups', '10 cups', '1 cup'], 0)]),
Sc('Science: Genetics Basics: Why Offspring Resemble Parents',
   'Grade 5 Science strand: offspring often resemble their parents because they inherit traits, such as eye colour or height tendencies, through genetic information passed down from both parents.',
   [('Why do offspring often resemble their parents?', ['They inherit traits through genetic information', 'A concept unrelated to genetics', 'Offspring never resemble their parents at all', 'Resemblance is always completely random'], 0),
    ('Name one trait that can be inherited from parents, such as eye colour.', ['Eye colour', 'A concept unrelated to genetics', 'A learned skill like riding a bike', 'A favourite food'], 0),
    ('Is genetic information passed down from both parents?', ['Yes', 'No, only one parent ever passes down genetic information', 'A concept unrelated to genetics', 'Genetic information is never passed down at all'], 0),
    ('Why might siblings look similar to each other but not identical?', ['They inherit a similar, but not identical, mix of traits from their parents', 'Siblings never share any inherited traits', 'This concept has no connection to genetics', 'Siblings always look completely identical'], 0),
    ('Why is understanding genetics useful for studying how living things are related?', ['It helps explain why traits are passed down between generations', 'Genetics has no connection to how living things are related', 'This concept has no relevance to science', 'Traits are never passed down between generations'], 0)]),
SS('Social Studies: Canada’s Space Program and Astronauts',
   'Grade 5 Social Studies strand: Canada has its own space program, the Canadian Space Agency, which has trained astronauts, such as Chris Hadfield, who have travelled to the International Space Station.',
   [('What is the name of Canada’s space agency?', ['The Canadian Space Agency', 'A concept unrelated to Canada', 'A private space company only', 'A branch of a different country’s space program'], 0),
    ('Name one Canadian astronaut, such as Chris Hadfield.', ['Chris Hadfield', 'A concept unrelated to space exploration', 'A fictional character', 'A historical explorer from centuries ago'], 0),
    ('Have Canadian astronauts travelled to the International Space Station?', ['Yes', 'No, Canadian astronauts have never travelled to space', 'A concept unrelated to Canada', 'Only astronauts from one other country can travel to space'], 0),
    ('Why might Canada’s participation in space exploration be a source of national pride?', ['It shows Canada’s contributions to scientific achievement on a global stage', 'Space exploration has no connection to national pride', 'This concept has no relevance to Canadian identity', 'Canada has never contributed anything to space exploration'], 0),
    ('Why might studying space exploration help students understand international cooperation?', ['Space missions often involve astronauts and scientists from many countries working together', 'Space exploration is always done by a single country alone', 'This concept has no connection to international cooperation', 'Countries never work together on space missions'], 0)]),
]),

day(82, [
L('Grammar: Gerunds and Participles',
  'Grade 5 Language strand: a gerund is a verb form ending in -ing that acts as a noun, such as swimming in I enjoy swimming, while a participle is a verb form used as an adjective, such as running in the running water.',
  [('A gerund is a verb form ending in -ing that acts as a ___.', ['Noun', 'Adjective', 'Adverb', 'Preposition'], 0),
   ('A participle is a verb form that can act as a ___.', ['Adjective', 'Noun only', 'A concept unrelated to grammar', 'A conjunction'], 0),
   ('In the sentence I enjoy swimming, what role does swimming play?', ['A noun, the gerund', 'A verb showing action right now', 'A concept unrelated to grammar', 'An adjective describing water'], 0),
   ('In the phrase the running water, what role does running play?', ['An adjective, a participle', 'A noun, a gerund', 'A concept unrelated to grammar', 'A preposition'], 0),
   ('Why might a writer use a gerund like reading as the subject of a sentence?', ['It allows an action to be discussed as a thing, like a noun', 'Gerunds can never act as the subject of a sentence', 'This concept has no connection to grammar', 'Gerunds are always used only as adjectives'], 0)]),
M('Geometry: Volume of Cylinders',
  'Grade 5 Math strand: students learn to find the volume of a cylinder by multiplying the area of its circular base by its height.',
  [('To find the volume of a cylinder, you multiply the area of its base by its ___.', ['Height', 'Circumference', 'Diameter', 'Radius only'], 0),
   ('What shape is the base of a cylinder?', ['A circle', 'A square', 'A triangle', 'A pentagon'], 0),
   ('If a cylinder’s base area is 10 square cm and its height is 5 cm, what is its volume?', ['50 cubic cm', '15 cubic cm', '10 cubic cm', '5 cubic cm'], 0),
   ('If a cylinder’s base area is 20 square cm and its height is 3 cm, what is its volume?', ['60 cubic cm', '23 cubic cm', '17 cubic cm', '20 cubic cm'], 0),
   ('Why is it useful to know how to calculate the volume of a cylinder?', ['It helps figure out how much a cylindrical container, like a can, can hold', 'Volume calculations never apply to real objects', 'This concept has no connection to geometry', 'Cylinders never have any measurable volume'], 0)]),
Sc('Science: The Lymphatic System',
   'Grade 5 Science strand: the lymphatic system is a network of vessels and nodes that helps fight infection and remove waste from the body, working closely with the immune system.',
   [('What body system helps fight infection and remove waste, working with the immune system?', ['The lymphatic system', 'A concept unrelated to the body', 'The digestive system', 'The skeletal system'], 0),
    ('Does the lymphatic system work closely with the immune system?', ['Yes', 'No, they have no connection to each other', 'A concept unrelated to the body', 'They are exactly the same system'], 0),
    ('What does the lymphatic system help remove from the body?', ['Waste', 'Only food', 'A concept unrelated to the lymphatic system', 'Nothing at all'], 0),
    ('Why might swollen lymph nodes be a sign that your body is fighting an infection?', ['The lymphatic system becomes more active when fighting off germs', 'Swollen lymph nodes never indicate anything about the body', 'This concept has no connection to the lymphatic system', 'Lymph nodes never change no matter what is happening in the body'], 0),
    ('Why is the lymphatic system considered an important part of the body’s defense against illness?', ['It helps filter out harmful substances and supports the immune response', 'The lymphatic system has no connection to fighting illness', 'This concept has no relevance to science', 'The body has no natural defenses against illness'], 0)]),
SS('Social Studies: The Canadian Football League and National Sports Culture',
   'Grade 5 Social Studies strand: the Canadian Football League, or CFL, is a professional sports league that plays a role in Canadian culture, bringing communities together through shared national pride in sports.',
   [('What does CFL stand for?', ['Canadian Football League', 'Canadian Fishing League', 'A concept unrelated to sports', 'Canadian Farming League'], 0),
    ('Is the CFL a professional sports league?', ['Yes', 'No, it is only for amateur players', 'A concept unrelated to Canadian culture', 'It is not a real organization'], 0),
    ('Can sports leagues like the CFL bring communities together?', ['Yes', 'No, sports never bring communities together', 'A concept unrelated to national culture', 'Sports only divide communities'], 0),
    ('Why might a national sports league be considered part of a country’s culture?', ['It reflects shared traditions and can build a sense of national pride', 'Sports leagues have no connection to culture at all', 'This concept has no relevance to social studies', 'National pride never has any connection to sports'], 0),
    ('Why might cities across Canada be excited to host a CFL championship game?', ['It can bring economic activity, tourism, and community excitement', 'Hosting a sports championship never benefits a city', 'This concept has no connection to social studies', 'Sports events never attract any visitors'], 0)]),
]),

day(83, [
L('Writing: Writing a Compare-and-Contrast Essay',
  'Grade 5 Language strand: a compare-and-contrast essay examines the similarities and differences between two subjects, often organizing ideas point-by-point or subject-by-subject.',
  [('What kind of essay examines the similarities and differences between two subjects?', ['A compare-and-contrast essay', 'A concept unrelated to writing', 'A persuasive essay only', 'A grocery list'], 0),
   ('Name one way a compare-and-contrast essay can be organized, such as point-by-point.', ['Point-by-point', 'A concept unrelated to essay structure', 'Randomly with no organization', 'Alphabetically by author name'], 0),
   ('Does a compare-and-contrast essay look at both similarities and differences?', ['Yes', 'No, it only looks at similarities', 'A concept unrelated to writing', 'It only looks at differences, never similarities'], 0),
   ('Why might a writer choose the subject-by-subject method for a compare-and-contrast essay?', ['It allows the writer to fully discuss one subject before moving to the next', 'This method never helps organize an essay', 'This concept has no connection to writing', 'Subject-by-subject essays never mention any differences'], 0),
   ('Which of these is an example of a compare-and-contrast topic?', ['Comparing life in a city versus life in the countryside', 'Describing your favourite meal', 'Writing a story about a dragon', 'Making a simple grocery list'], 0)]),
M('Data: Box-and-Whisker Plots',
  'Grade 5 Math strand: a box-and-whisker plot displays a data set’s spread using five key values: the minimum, first quartile, median, third quartile, and maximum.',
  [('How many key values does a box-and-whisker plot use to display data?', ['Five', 'Two', 'Three', 'Ten'], 0),
   ('What is the middle value of a data set called, shown in a box-and-whisker plot?', ['The median', 'The minimum', 'The maximum', 'A concept unrelated to data'], 0),
   ('What does the whisker part of a box-and-whisker plot usually show?', ['The range toward the minimum and maximum values', 'Only the exact average of the data', 'A concept unrelated to data', 'Nothing meaningful about the data'], 0),
   ('Why might a box-and-whisker plot be useful for comparing two data sets?', ['It shows the spread and middle values clearly, making comparison easier', 'Box-and-whisker plots never help with comparing data', 'This concept has no connection to data management', 'Data sets can never be compared to each other'], 0),
   ('What is the highest value in a data set called, shown in a box-and-whisker plot?', ['The maximum', 'The minimum', 'The median', 'The first quartile'], 0)]),
Sc('Science: Sustainable Forestry Practices',
   'Grade 5 Science strand: sustainable forestry practices, such as replanting trees and selective logging, aim to harvest wood while maintaining a healthy forest ecosystem for the future.',
   [('What is one goal of sustainable forestry practices?', ['Maintaining a healthy forest ecosystem for the future', 'Removing every tree from a forest permanently', 'A concept unrelated to forestry', 'Ignoring the health of a forest completely'], 0),
    ('Name one sustainable forestry practice, such as replanting trees.', ['Replanting trees', 'A concept unrelated to sustainable forestry', 'Cutting down every tree with no replanting', 'Burning an entire forest'], 0),
    ('What is selective logging?', ['Carefully choosing which trees to harvest, rather than cutting down everything', 'Cutting down every single tree in a forest at once', 'A concept unrelated to forestry', 'Never harvesting any trees at all'], 0),
    ('Why might replanting trees be an important part of sustainable forestry?', ['It helps ensure the forest can regrow and continue supporting wildlife', 'Replanting trees has no effect on a forest’s health', 'This concept has no connection to sustainability', 'Forests never actually need any trees replanted'], 0),
    ('Why do forestry companies today often use sustainable practices instead of just cutting down as many trees as possible?', ['Sustainable practices help protect forests for future generations and industries', 'Sustainable practices have no benefit to a forest', 'This concept has no relevance to science', 'Cutting down every tree at once always benefits a forest'], 0)]),
SS('Social Studies: Comparing Time Zones Around the World',
   'Grade 5 Social Studies strand: the world is divided into time zones based on longitude, meaning it can be a different time of day in different countries at the exact same moment.',
   [('What is the world divided into, based on longitude, that affects the time of day?', ['Time zones', 'A concept unrelated to geography', 'Provinces only', 'Oceans only'], 0),
    ('Can it be a different time of day in different countries at the exact same moment?', ['Yes', 'No, it is always the same time everywhere', 'A concept unrelated to time zones', 'Time zones do not actually exist'], 0),
    ('Are time zones based on longitude or on population size?', ['Longitude', 'Population size', 'A concept unrelated to time zones', 'Neither, time zones are chosen randomly'], 0),
    ('Why might someone need to know about time zones before scheduling an international video call?', ['So both people can find a time that works for their own local time of day', 'Time zones never matter for scheduling a call', 'This concept has no connection to time zones', 'International calls never require any time zone planning'], 0),
    ('Why is understanding time zones useful for understanding global communication and travel?', ['It helps explain why the time can differ so much between countries', 'Time zones have no connection to travel or communication', 'This concept has no relevance to social studies', 'Every country in the world shares the exact same time zone'], 0)]),
]),

day(84, [
L('Figurative Language: Allusion',
  'Grade 5 Language strand: an allusion is a brief reference to a well-known person, event, or work, such as calling someone a Scrooge to suggest they are stingy, without fully explaining the reference.',
  [('What do we call a brief reference to a well-known person, event, or work?', ['An allusion', 'A concept unrelated to figurative language', 'A metaphor', 'A homophone'], 0),
   ('If someone is called a Scrooge, what quality does this allusion suggest?', ['Being stingy', 'Being generous', 'A concept unrelated to allusion', 'Being extremely cheerful'], 0),
   ('Does an allusion usually fully explain the reference it is making?', ['No, it assumes the reader already understands the reference', 'Yes, it always explains everything in full detail', 'A concept unrelated to allusion', 'Allusions never reference anything at all'], 0),
   ('Why might a writer use an allusion instead of directly describing something in detail?', ['It can quickly convey a complex idea using a familiar reference', 'Allusions never add any meaning to writing', 'This concept has no connection to figurative language', 'Allusions always make writing less meaningful'], 0),
   ('Why might an allusion be confusing to a reader who does not recognize the reference?', ['The reader may not understand the meaning the writer intended', 'Allusions are always understood by every single reader', 'This concept has no connection to figurative language', 'Recognizing a reference never changes how a reader understands a text'], 0)]),
M('Algebra: Solving Two-Step Equations',
  'Grade 5 Math strand: students learn to solve a two-step equation, such as 2n plus 3 equals 11, by first undoing addition or subtraction, then undoing multiplication or division.',
  [('To solve 2n plus 3 equals 11, what should you do first?', ['Subtract 3 from both sides', 'Divide both sides by 2 first', 'A concept unrelated to solving equations', 'Add 3 to both sides'], 0),
   ('After subtracting 3 from both sides of 2n plus 3 equals 11, what equation do you have?', ['2n equals 8', '2n equals 14', 'n equals 8', 'n equals 3'], 0),
   ('If 2n equals 8, what is the value of n?', ['4', '8', '2', '16'], 0),
   ('To solve a two-step equation, in what order should you typically undo the operations?', ['Undo addition or subtraction first, then multiplication or division', 'Undo multiplication or division first, then addition or subtraction only', 'A concept unrelated to solving equations', 'The order never matters at all'], 0),
   ('If 3n minus 2 equals 13, what is the value of n?', ['5', '3', '11', '15'], 0)]),
Sc('Science: Satellites and Their Uses',
   'Grade 5 Science strand: satellites orbit Earth and are used for purposes such as weather forecasting, communication, and navigation systems like GPS.',
   [('What do satellites orbit?', ['Earth', 'The Moon only', 'A concept unrelated to space', 'Nothing at all'], 0),
    ('Name one use of satellites, such as weather forecasting.', ['Weather forecasting', 'A concept unrelated to satellites', 'Baking bread', 'Growing plants'], 0),
    ('Do satellites help power navigation systems like GPS?', ['Yes', 'No, GPS has no connection to satellites', 'A concept unrelated to satellites', 'Satellites have no practical uses'], 0),
    ('Why might satellites be especially useful for forecasting weather over large areas?', ['They can observe wide areas of Earth from high above, tracking storms and patterns', 'Satellites can never observe weather patterns', 'This concept has no connection to satellites', 'Weather can only be observed from the ground'], 0),
    ('Why has satellite technology become important for everyday communication, like phone calls and internet access?', ['Satellites can relay signals across long distances, including remote areas', 'Satellites have no connection to communication technology', 'This concept has no relevance to science', 'Communication never relies on any satellite technology'], 0)]),
SS('Social Studies: Refugees and Canada’s Humanitarian Role',
   'Grade 5 Social Studies strand: a refugee is someone who has fled their home country due to danger, such as war or persecution, and Canada has a history of welcoming refugees seeking safety.',
   [('What do we call someone who has fled their home country due to danger?', ['A refugee', 'A concept unrelated to migration', 'A tourist', 'A student on vacation'], 0),
    ('Name one reason a person might become a refugee, such as war.', ['War', 'A concept unrelated to refugees', 'Going on a fun vacation', 'Visiting family for a holiday'], 0),
    ('Has Canada historically welcomed refugees seeking safety?', ['Yes', 'No, Canada has never welcomed any refugees', 'A concept unrelated to Canada', 'Only tourists are ever welcomed into Canada'], 0),
    ('Why might a country like Canada choose to welcome refugees?', ['To offer safety and support to people facing danger in their home country', 'Welcoming refugees never has any humanitarian purpose', 'This concept has no connection to Canada’s history', 'Refugees are never actually in any danger'], 0),
    ('Why might communities benefit from welcoming refugees and helping them settle?', ['New community members can bring diverse skills, perspectives, and contributions', 'Refugees never contribute anything to a community', 'This concept has no relevance to social studies', 'Welcoming refugees always harms a community'], 0)]),
]),

day(85, [
L('Reading: Understanding Satire',
  'Grade 5 Language strand: satire uses humour, irony, or exaggeration to criticize or point out flaws in people, society, or ideas, often found in cartoons or comedic writing.',
  [('What literary technique uses humour or exaggeration to criticize flaws in society?', ['Satire', 'A concept unrelated to reading', 'A biography', 'A recipe'], 0),
   ('Where might satire commonly be found, such as in cartoons?', ['Cartoons', 'A concept unrelated to satire', 'A phone book', 'A dictionary'], 0),
   ('Does satire often use exaggeration to make its point?', ['Yes', 'No, satire never uses exaggeration', 'A concept unrelated to reading', 'Satire only uses plain, literal facts'], 0),
   ('Why might a writer use satire instead of directly stating criticism?', ['Humour and exaggeration can make a criticism more memorable and engaging', 'Satire never actually criticizes anything', 'This concept has no connection to writing', 'Direct criticism is always more effective than satire'], 0),
   ('Why can satire sometimes be misunderstood by readers?', ['Readers might take the exaggerated or ironic statements literally', 'Satire is always understood exactly the same way by everyone', 'This concept has no connection to reading comprehension', 'Satire never contains any exaggeration or irony at all'], 0)]),
M('Measurement: Converting Between Imperial and Metric Units',
  'Grade 5 Math strand: students learn approximate conversions between imperial and metric units, such as knowing that 1 inch is about 2.5 centimetres and 1 mile is about 1.6 kilometres.',
  [('About how many centimetres are in 1 inch?', ['2.5', '1', '10', '100'], 0),
   ('About how many kilometres are in 1 mile?', ['1.6', '1', '10', '0.5'], 0),
   ('About how many centimetres are in 4 inches?', ['10', '4', '2.5', '40'], 0),
   ('Why is it useful to know approximate conversions between imperial and metric units?', ['Some countries use different systems, so conversions help compare measurements', 'Imperial and metric units can never be compared to each other', 'This concept has no connection to measurement', 'Every country in the world uses the exact same measurement system'], 0),
   ('If a recipe from another country uses cups instead of millilitres, why might a Canadian cook need a conversion?', ['Canada primarily uses the metric system, so a conversion helps measure ingredients correctly', 'Conversions are never needed when following a recipe', 'This concept has no connection to measurement', 'Cups and millilitres are always exactly the same amount'], 0)]),
Sc('Science: Acids and Bases',
   'Grade 5 Science strand: acids and bases are two types of chemical substances that can be measured on the pH scale, with acids like lemon juice below 7 and bases like baking soda above 7.',
   [('What scale is used to measure whether a substance is an acid or a base?', ['The pH scale', 'A concept unrelated to chemistry', 'The Celsius scale', 'The Richter scale'], 0),
    ('Is lemon juice an example of an acid or a base?', ['An acid', 'A base', 'A concept unrelated to chemistry', 'Neither an acid nor a base'], 0),
    ('Is baking soda an example of an acid or a base?', ['A base', 'An acid', 'A concept unrelated to chemistry', 'Neither an acid nor a base'], 0),
    ('On the pH scale, do acids typically measure above or below 7?', ['Below 7', 'Above 7', 'Exactly at 7 always', 'A concept unrelated to pH'], 0),
    ('Why might scientists use the pH scale to classify substances?', ['It gives a standard way to measure and compare how acidic or basic something is', 'The pH scale has no connection to classifying substances', 'This concept has no relevance to science', 'Acids and bases can never actually be measured'], 0)]),
SS('Social Studies: The History of Canadian Postal Services',
   'Grade 5 Social Studies strand: Canada Post has a long history of connecting communities across the country, evolving from horse-drawn mail delivery to modern sorting facilities and delivery trucks.',
   [('What is the name of Canada’s national postal service?', ['Canada Post', 'A concept unrelated to Canadian history', 'A private courier company only', 'A branch of a different country’s postal system'], 0),
    ('Did early mail delivery in Canada sometimes rely on horse-drawn transportation?', ['Yes', 'No, horses were never used for mail delivery', 'A concept unrelated to postal history', 'Only airplanes have ever delivered mail in Canada'], 0),
    ('Has Canada’s postal system changed over time?', ['Yes', 'No, it has always been exactly the same', 'A concept unrelated to Canadian history', 'Postal systems never change in any country'], 0),
    ('Why might it have been especially challenging to deliver mail across Canada in its early history?', ['Canada’s vast size and rugged geography made transportation difficult', 'Delivering mail across Canada was never a challenge', 'This concept has no connection to Canadian history', 'Canada has always had a very small land area'], 0),
    ('Why is a reliable postal service important for connecting communities across a large country like Canada?', ['It helps people and businesses across distant regions stay connected', 'A postal service has no connection to connecting communities', 'This concept has no relevance to social studies', 'Communities never need to send or receive mail'], 0)]),
]),

day(86, [
L('Grammar: Appositives',
  'Grade 5 Language strand: an appositive is a noun or phrase placed next to another noun to rename or explain it, such as in my friend Maria, the artist, painted a mural, where the artist explains Maria.',
  [('What do we call a noun or phrase placed next to another noun to rename or explain it?', ['An appositive', 'A concept unrelated to grammar', 'A verb', 'A preposition'], 0),
   ('In the sentence Maria, the artist, painted a mural, what is the appositive?', ['The artist', 'Maria', 'Painted', 'A mural'], 0),
   ('Does an appositive usually rename or explain the noun next to it?', ['Yes', 'No, it always changes the noun’s meaning completely', 'A concept unrelated to grammar', 'An appositive never has any connection to the noun beside it'], 0),
   ('Which sentence correctly uses an appositive?', ['My dog, a golden retriever, loves to swim.', 'My dog a golden retriever loves to swim she is happy.', 'A golden retriever my dog loves to swim.', 'My dog loves golden retriever to swim.'], 0),
   ('Why might a writer use an appositive instead of writing two separate sentences?', ['It can combine related information smoothly into one sentence', 'Appositives never combine any information', 'This concept has no connection to writing', 'Two separate sentences are always clearer than using an appositive'], 0)]),
M('Patterning: Fibonacci-like Sequences',
  'Grade 5 Math strand: in a Fibonacci-like sequence, each number is the sum of the two numbers before it, such as 1, 1, 2, 3, 5, 8, where 5 is the sum of 2 and 3.',
  [('In the sequence 1, 1, 2, 3, 5, 8, what number comes next?', ['13', '10', '11', '9'], 0),
   ('In a Fibonacci-like sequence, how is each number found?', ['By adding the two numbers before it', 'By multiplying the two numbers before it', 'A concept unrelated to patterns', 'By subtracting the two numbers before it'], 0),
   ('In the sequence 2, 2, 4, 6, 10, what number comes next?', ['16', '14', '12', '10'], 0),
   ('Why might this type of sequence be called Fibonacci-like?', ['It follows the same rule as the famous Fibonacci sequence, adding the two previous numbers', 'It has no connection to the Fibonacci sequence at all', 'This concept has no connection to patterns', 'Every number sequence is automatically Fibonacci-like'], 0),
   ('In the sequence 1, 3, 4, 7, 11, what number comes next?', ['18', '15', '14', '10'], 0)]),
Sc('Science: Wetlands and Their Importance',
   'Grade 5 Science strand: wetlands are areas of land covered in water for part or all of the year, providing important habitats for wildlife and helping filter and store water.',
   [('What do we call an area of land covered in water for part or all of the year?', ['A wetland', 'A desert', 'A concept unrelated to ecosystems', 'A mountain range'], 0),
    ('Do wetlands provide important habitats for wildlife?', ['Yes', 'No, wetlands provide no habitat for any wildlife', 'A concept unrelated to ecosystems', 'Wetlands are completely empty of living things'], 0),
    ('Can wetlands help filter and store water?', ['Yes', 'No, wetlands have no connection to water filtration', 'A concept unrelated to wetlands', 'Wetlands only ever release polluted water'], 0),
    ('Why might wetlands be especially important during periods of heavy rain?', ['They can absorb and store excess water, helping to reduce flooding', 'Wetlands have no effect on flooding at all', 'This concept has no connection to wetlands', 'Wetlands always cause more flooding during heavy rain'], 0),
    ('Why is it important to protect wetlands from being drained or developed?', ['They provide valuable habitat and environmental benefits that are hard to replace', 'Wetlands provide no value to protect', 'This concept has no relevance to science', 'Draining wetlands never has any negative effect'], 0)]),
SS('Social Studies: Canada’s National Anthem and Its History',
   'Grade 5 Social Studies strand: O Canada became Canada’s official national anthem in 1980, though the song was first performed over a century earlier and has been translated into both English and French.',
   [('What is the name of Canada’s national anthem?', ['O Canada', 'A concept unrelated to Canadian symbols', 'The Maple Leaf Song', 'A concept with no real name'], 0),
    ('In what year did O Canada officially become Canada’s national anthem?', ['1980', '1867', '1900', '1950'], 0),
    ('Has O Canada been translated into both English and French?', ['Yes', 'No, it exists only in one single language', 'A concept unrelated to Canada’s anthem', 'It has never been translated at all'], 0),
    ('Why might a national anthem be an important symbol for a country?', ['It represents shared identity, history, and pride among citizens', 'National anthems have no connection to a country’s identity', 'This concept has no relevance to social studies', 'National anthems serve no purpose at all'], 0),
    ('Why might it be significant that O Canada existed for many years before officially becoming the national anthem?', ['It shows how a song can become an important national symbol over time', 'The timing of when a song became an anthem never matters', 'This concept has no connection to Canadian history', 'O Canada was written the same year it became the anthem'], 0)]),
]),

day(87, [
L('Vocabulary: Words with Greek and Latin Roots',
  'Grade 5 Language strand: many English words come from Greek and Latin roots, such as the root bio, meaning life, found in words like biology and biography.',
  [('What does the root bio mean, found in words like biology?', ['Life', 'Water', 'A concept unrelated to roots', 'Light'], 0),
   ('Which word contains the root bio, meaning life?', ['Biography', 'Geography', 'Telephone', 'Automobile'], 0),
   ('Do many English words come from Greek and Latin roots?', ['Yes', 'No, English words never come from other languages', 'A concept unrelated to vocabulary', 'English has no connection to Greek or Latin'], 0),
   ('Why might knowing that the root aqua means water help you understand new words?', ['You could guess that a word with aqua relates to water, like aquarium', 'Root words never provide any clues about a word’s meaning', 'This concept has no connection to vocabulary', 'The root aqua always means fire, not water'], 0),
   ('Which of these words likely contains a root related to writing, based on graph meaning to write?', ['Autograph', 'Telephone', 'Aquarium', 'Bicycle'], 0)]),
M('Data: Interpreting Misleading Graphs',
  'Grade 5 Math strand: students learn to spot misleading graphs, such as ones with a truncated y-axis or an uneven scale, which can make differences in data look larger or smaller than they really are.',
  [('What is a truncated y-axis on a graph?', ['A y-axis that does not start at zero', 'A y-axis that always starts at zero', 'A concept unrelated to graphs', 'A graph with no y-axis at all'], 0),
   ('Can a truncated y-axis make differences in data appear larger than they really are?', ['Yes', 'No, it never affects how data appears', 'A concept unrelated to misleading graphs', 'A truncated y-axis always makes data look smaller only'], 0),
   ('Why might someone intentionally create a misleading graph?', ['To make their argument or data appear more dramatic than it really is', 'Misleading graphs are never created on purpose', 'This concept has no connection to data management', 'Graphs can never be used to mislead anyone'], 0),
   ('What should you check on a graph to see if its scale might be misleading?', ['Whether the axis starts at zero and uses even intervals', 'Only the colour of the bars', 'A concept unrelated to reading graphs', 'Only the title of the graph'], 0),
   ('Why is it important to critically examine graphs in the news or advertisements?', ['Some graphs may be designed to mislead or exaggerate the data', 'All graphs in the news are always completely accurate', 'This concept has no relevance to data literacy', 'Graphs never appear in the news or advertisements'], 0)]),
Sc('Science: Earthquake-Resistant Design',
   'Grade 5 Science strand: engineers use earthquake-resistant design, such as flexible foundations and reinforced materials, to help buildings withstand the shaking caused by earthquakes.',
   [('What do engineers use to help buildings withstand earthquakes?', ['Earthquake-resistant design', 'A concept unrelated to structures', 'No special design at all', 'Only decorative features'], 0),
    ('Name one feature of earthquake-resistant design, such as a flexible foundation.', ['A flexible foundation', 'A concept unrelated to earthquake-resistant design', 'A completely rigid structure with no flexibility', 'A building made only of glass'], 0),
    ('Can reinforced materials help a building withstand shaking during an earthquake?', ['Yes', 'No, reinforced materials have no effect on earthquake resistance', 'A concept unrelated to structures', 'Reinforced materials always make buildings weaker'], 0),
    ('Why might a flexible foundation help a building survive an earthquake better than a rigid one?', ['Flexibility can allow a building to absorb and adjust to shaking rather than crack', 'A flexible foundation always makes a building collapse faster', 'This concept has no connection to earthquake-resistant design', 'Rigid foundations always survive earthquakes better than flexible ones'], 0),
    ('Why is earthquake-resistant design especially important for cities located near fault lines?', ['These areas have a higher risk of experiencing earthquakes', 'Earthquake-resistant design has no connection to fault lines', 'This concept has no relevance to science', 'Cities near fault lines never actually experience earthquakes'], 0)]),
SS('Social Studies: The Role of Non-Governmental Organizations',
   'Grade 5 Social Studies strand: a non-governmental organization, or NGO, is a group that works independently from government to address issues like poverty, health, or the environment, often across many countries.',
   [('What does NGO stand for?', ['Non-governmental organization', 'National government office', 'A concept unrelated to organizations', 'New government order'], 0),
    ('Does an NGO work independently from government?', ['Yes', 'No, an NGO is always run directly by a government', 'A concept unrelated to NGOs', 'NGOs do not actually exist'], 0),
    ('Name one issue an NGO might address, such as poverty or health.', ['Poverty', 'A concept unrelated to NGOs', 'A local school’s lunch menu', 'A single family’s vacation plans'], 0),
    ('Why might an NGO choose to work across many different countries?', ['Global issues, like poverty or health crises, often require cooperation beyond one country', 'NGOs never work in more than one country', 'This concept has no connection to social studies', 'Global issues never require any international cooperation'], 0),
    ('Why might NGOs sometimes be able to respond to a crisis more quickly than a government?', ['They may have specialized resources and can act independently of government processes', 'NGOs are never able to respond to any crisis', 'This concept has no relevance to social studies', 'Governments always respond faster than NGOs in every situation'], 0)]),
]),

day(88, [
L('Writing: Writing a Letter to the Editor',
  'Grade 5 Language strand: a letter to the editor expresses an opinion about a current issue, often published in a newspaper, and typically includes a clear position along with supporting reasons.',
  [('What kind of letter expresses an opinion about a current issue, often published in a newspaper?', ['A letter to the editor', 'A concept unrelated to writing', 'A grocery list', 'A birthday invitation'], 0),
   ('Should a letter to the editor include a clear position along with supporting reasons?', ['Yes', 'No, it should never include any reasons', 'A concept unrelated to writing', 'Only facts are allowed, with no opinion at all'], 0),
   ('Where is a letter to the editor often published?', ['In a newspaper', 'In a private diary only', 'A concept unrelated to letters to the editor', 'It is never published anywhere'], 0),
   ('Why might someone write a letter to the editor about a local issue?', ['To share their opinion and try to influence public discussion on the issue', 'Letters to the editor never discuss any real issues', 'This concept has no connection to writing', 'Letters to the editor are always about fictional topics'], 0),
   ('Which of these would most likely appear in a letter to the editor?', ['I believe our town needs more sidewalks for pedestrian safety.', 'Once upon a time, there was a dragon.', 'Add 5 and 6 to get 11.', 'The chemical symbol for oxygen is O.'], 0)]),
M('Probability: Independent vs Dependent Events',
  'Grade 5 Math strand: an independent event, like flipping a coin twice, does not affect the outcome of another event, while a dependent event, like drawing cards without replacement, changes the probability of what happens next.',
  [('Does flipping a coin twice count as an independent or dependent event?', ['Independent', 'Dependent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0),
   ('Does drawing a card and not replacing it before drawing again count as an independent or dependent event?', ['Dependent', 'Independent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0),
   ('In an independent event, does the first outcome affect the probability of the second outcome?', ['No', 'Yes, always', 'A concept unrelated to probability', 'Only sometimes, with no clear rule'], 0),
   ('Why is drawing cards without replacement considered a dependent event?', ['Removing a card changes the number and type of cards left, affecting the next probability', 'Removing a card never changes any future probability', 'This concept has no connection to probability', 'Dependent events never involve any changes in probability'], 0),
   ('If you roll a die and then flip a coin, are these two events independent or dependent?', ['Independent', 'Dependent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0)]),
Sc('Science: How a Battery Stores and Releases Energy',
   'Grade 5 Science strand: a battery stores chemical energy and converts it into electrical energy when connected in a circuit, powering devices like flashlights and remote controls.',
   [('What type of energy does a battery store?', ['Chemical energy', 'Only sound energy', 'A concept unrelated to batteries', 'Only light energy'], 0),
    ('What does a battery convert its stored energy into when connected in a circuit?', ['Electrical energy', 'Only heat energy', 'A concept unrelated to batteries', 'Nothing at all'], 0),
    ('Name one device that a battery might power, such as a flashlight.', ['A flashlight', 'A concept unrelated to batteries', 'A wooden chair', 'A glass of water'], 0),
    ('Why might a battery eventually stop working and need to be replaced or recharged?', ['Its stored chemical energy gradually runs out as it is used', 'Batteries never run out of energy', 'This concept has no connection to how batteries work', 'Batteries generate infinite energy with no limit'], 0),
    ('Why are batteries an important part of many portable devices, like remote controls?', ['They allow devices to work without being plugged directly into a wall outlet', 'Batteries have no connection to portable devices', 'This concept has no relevance to science', 'Portable devices never actually need any power source'], 0)]),
SS('Social Studies: Canada’s Mining Industry and Its Impact',
   'Grade 5 Social Studies strand: Canada’s mining industry extracts valuable resources, such as nickel, gold, and potash, supporting jobs and the economy while also raising environmental considerations.',
   [('Name one resource extracted by Canada’s mining industry, such as nickel or gold.', ['Nickel', 'A concept unrelated to mining', 'Fresh fruit', 'Ocean water'], 0),
    ('Does Canada’s mining industry support jobs and the economy?', ['Yes', 'No, mining has no connection to jobs or the economy', 'A concept unrelated to Canada', 'Mining never provides any economic benefit'], 0),
    ('Can mining raise environmental considerations that communities must think about?', ['Yes', 'No, mining never has any environmental impact', 'A concept unrelated to mining', 'Environmental considerations are never relevant to mining'], 0),
    ('Why might a mining company need to plan carefully to reduce its environmental impact?', ['Mining can affect land, water, and wildlife, so careful planning helps minimize harm', 'Mining never has any effect on the environment', 'This concept has no connection to social studies', 'Environmental impact never needs to be considered in industry'], 0),
    ('Why is Canada’s mining industry considered an important part of its economy?', ['It provides valuable resources and jobs across many regions of the country', 'Mining has no connection to Canada’s economy', 'This concept has no relevance to social studies', 'Mining provides no resources of any real value'], 0)]),
]),

day(89, [
L('Reading: Analyzing Multiple Perspectives in a Text',
  'Grade 5 Language strand: some texts present multiple perspectives, showing an issue or event from more than one point of view, helping readers understand a fuller, more balanced picture.',
  [('What does it mean for a text to present multiple perspectives?', ['It shows an issue from more than one point of view', 'It only ever shows one single point of view', 'A concept unrelated to reading', 'It shows no point of view at all'], 0),
   ('Can analyzing multiple perspectives help readers understand a more balanced picture of an issue?', ['Yes', 'No, multiple perspectives never help with understanding', 'A concept unrelated to reading comprehension', 'Balanced understanding never requires multiple perspectives'], 0),
   ('If a text discusses a historical event from both sides involved, is that an example of multiple perspectives?', ['Yes', 'No, this would only be a single perspective', 'A concept unrelated to reading', 'This has no connection to perspectives at all'], 0),
   ('Why might reading only one perspective on a controversial issue be limiting?', ['It could leave out important viewpoints needed for a full understanding', 'Reading one perspective always provides a complete understanding', 'This concept has no connection to reading comprehension', 'Perspectives never affect how well a reader understands an issue'], 0),
   ('Why is it valuable for students to practise identifying multiple perspectives in what they read?', ['It builds critical thinking skills and a more thoughtful understanding of issues', 'Identifying perspectives never builds any useful skills', 'This concept has no relevance to reading comprehension', 'There is always only one correct perspective on every issue'], 0)]),
M('Review Preparation: Applying Ratios, Volume, and Probability',
  'Grade 5 Math strand: students apply recent skills, including scaling recipes, finding cylinder volume, and probability of independent events, to solve multi-part problems that combine these ideas.',
  [('If a recipe is scaled from serving 4 people to serving 12 people, by what factor was it scaled?', ['3', '4', '12', '2'], 0),
   ('If a cylinder’s base area is 15 square cm and height is 4 cm, what is its volume?', ['60 cubic cm', '19 cubic cm', '15 cubic cm', '4 cubic cm'], 0),
   ('Is rolling a die twice in a row an example of independent or dependent events?', ['Independent', 'Dependent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0),
   ('If a recipe needs 4 cups of water to serve 8 people, how much water is needed for 4 people?', ['2 cups', '4 cups', '8 cups', '1 cup'], 0),
   ('Why is it useful to combine multiple math skills, like ratios and volume, to solve a real-world problem?', ['Real-world problems often require more than one math concept to solve completely', 'Combining skills never helps solve any problem', 'This concept has no connection to math', 'Every real-world problem only ever needs one single skill'], 0)]),
Sc('Science: Hurricanes and Tornadoes',
   'Grade 5 Science strand: hurricanes are large, rotating storms that form over warm ocean water, while tornadoes are smaller, fast-spinning columns of air that can form quickly over land during severe thunderstorms.',
   [('Where do hurricanes typically form?', ['Over warm ocean water', 'Over cold mountain peaks', 'A concept unrelated to weather', 'Only over deserts'], 0),
    ('Are tornadoes generally larger or smaller than hurricanes?', ['Smaller', 'Larger', 'A concept unrelated to storms', 'Exactly the same size'], 0),
    ('Can tornadoes form quickly over land during severe thunderstorms?', ['Yes', 'No, tornadoes never form quickly', 'A concept unrelated to tornadoes', 'Tornadoes only ever form over the ocean'], 0),
    ('Why do hurricanes need warm ocean water to form and grow stronger?', ['Warm water provides the heat and moisture that fuel the storm’s energy', 'Warm ocean water has no connection to hurricanes', 'This concept has no relevance to science', 'Hurricanes actually form over cold ocean water instead'], 0),
    ('Why is it important for communities in tornado-prone areas to have a safety plan?', ['Tornadoes can form and strike with very little warning', 'Tornadoes are never dangerous to any community', 'This concept has no connection to severe weather safety', 'Communities never need any plan for severe weather'], 0)]),
SS('Social Studies: The History of Canadian Universities and Education',
   'Grade 5 Social Studies strand: Canada’s system of higher education has grown over time, from its earliest universities in the 1800s to today’s wide network of colleges and universities across the country.',
   [('Has Canada’s system of higher education grown and changed over time?', ['Yes', 'No, it has always been exactly the same', 'A concept unrelated to Canadian history', 'Canada has never had any universities'], 0),
    ('Around what century did Canada’s earliest universities begin?', ['The 1800s', 'The 2000s', 'A concept unrelated to Canadian history', 'The 1600s'], 0),
    ('Does Canada today have a wide network of colleges and universities?', ['Yes', 'No, Canada has only ever had one single university', 'A concept unrelated to education', 'Higher education does not exist in Canada'], 0),
    ('Why might access to higher education be important for a country’s development?', ['It can help build a skilled workforce and support innovation', 'Higher education has no connection to a country’s development', 'This concept has no relevance to social studies', 'Higher education never benefits a country in any way'], 0),
    ('Why might studying the history of education help students understand how opportunities have changed over time?', ['It shows how access to schooling and universities has expanded for more people over the years', 'The history of education never changes over time', 'This concept has no connection to social studies', 'Educational opportunities have always been identical throughout history'], 0)]),
]),

day(90, [
L('Review: Tone, Grammar, and Figurative Language (Days 81-89)',
  'Grade 5 Language strand review: students revisit tone, gerunds and participles, compare-and-contrast essays, allusion, satire, appositives, Greek and Latin roots, letters to the editor, and multiple perspectives.',
  [('What do we call the author’s attitude toward a subject, shown through word choice?', ['Tone', 'A concept unrelated to reading', 'The setting', 'The plot'], 0),
   ('A gerund is a verb form ending in -ing that acts as a ___.', ['Noun', 'Adjective', 'Adverb', 'Preposition'], 0),
   ('What do we call a brief reference to a well-known person, event, or work?', ['An allusion', 'A concept unrelated to figurative language', 'A metaphor', 'A homophone'], 0),
   ('What literary technique uses humour or exaggeration to criticize flaws in society?', ['Satire', 'A concept unrelated to reading', 'A biography', 'A recipe'], 0),
   ('What do we call a noun or phrase placed next to another noun to rename or explain it?', ['An appositive', 'A concept unrelated to grammar', 'A verb', 'A preposition'], 0)]),
M('Review: Proportions, Geometry, and Probability (Days 81-89)',
  'Grade 5 Math strand review: students revisit scaling recipes, cylinder volume, box-and-whisker plots, two-step equations, unit conversions, Fibonacci-like sequences, misleading graphs, and independent versus dependent events.',
  [('If a recipe needs 2 cups of flour to serve 4 people, how much flour is needed to serve 8 people?', ['4 cups', '2 cups', '8 cups', '1 cup'], 0),
   ('To find the volume of a cylinder, you multiply the area of its base by its ___.', ['Height', 'Circumference', 'Diameter', 'Radius only'], 0),
   ('How many key values does a box-and-whisker plot use to display data?', ['Five', 'Two', 'Three', 'Ten'], 0),
   ('If 2n equals 8, what is the value of n?', ['4', '8', '2', '16'], 0),
   ('Does drawing a card and not replacing it before drawing again count as an independent or dependent event?', ['Dependent', 'Independent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0)]),
Sc('Review: Body Systems, Earth Science, and Physical Science (Days 81-89)',
   'Grade 5 Science strand review: students revisit genetics, the lymphatic system, sustainable forestry, satellites, acids and bases, wetlands, earthquake-resistant design, batteries, and hurricanes and tornadoes.',
   [('Why do offspring often resemble their parents?', ['They inherit traits through genetic information', 'A concept unrelated to genetics', 'Offspring never resemble their parents at all', 'Resemblance is always completely random'], 0),
    ('What body system helps fight infection and remove waste, working with the immune system?', ['The lymphatic system', 'A concept unrelated to the body', 'The digestive system', 'The skeletal system'], 0),
    ('Is lemon juice an example of an acid or a base?', ['An acid', 'A base', 'A concept unrelated to chemistry', 'Neither an acid nor a base'], 0),
    ('What do engineers use to help buildings withstand earthquakes?', ['Earthquake-resistant design', 'A concept unrelated to structures', 'No special design at all', 'Only decorative features'], 0),
    ('Where do hurricanes typically form?', ['Over warm ocean water', 'Over cold mountain peaks', 'A concept unrelated to weather', 'Only over deserts'], 0)]),
SS('Review: Canadian Identity, Global Roles, and Education (Days 81-89)',
   'Grade 5 Social Studies strand review: students revisit Canada’s space program, the CFL, world time zones, refugees, postal history, the national anthem, NGOs, mining, and Canadian higher education.',
   [('What is the name of Canada’s space agency?', ['The Canadian Space Agency', 'A concept unrelated to Canada', 'A private space company only', 'A branch of a different country’s space program'], 0),
    ('What do we call someone who has fled their home country due to danger?', ['A refugee', 'A concept unrelated to migration', 'A tourist', 'A student on vacation'], 0),
    ('In what year did O Canada officially become Canada’s national anthem?', ['1980', '1867', '1900', '1950'], 0),
    ('What does NGO stand for?', ['Non-governmental organization', 'National government office', 'A concept unrelated to organizations', 'New government order'], 0),
    ('Around what century did Canada’s earliest universities begin?', ['The 1800s', 'The 2000s', 'A concept unrelated to Canadian history', 'The 1600s'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_81_90)
    append_to(5, g5_81_90)
