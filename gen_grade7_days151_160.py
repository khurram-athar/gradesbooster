#!/usr/bin/env python3
"""Grade 7, Days 151-160 -- extends Grade 7 from 150 to 160 days. Topics
chosen after dumping the full (subject, title) list for Days 1-150 from
data/grade7.json to confirm zero overlap, since Grade 7's earlier 150 days
already cover an unusually exhaustive range of subject matter across all
four subjects.

Fresh, non-duplicate topics picked this batch:
Language: compound-complex sentences, clipped words and word shortening,
analyzing static and dynamic characters, writing an autobiographical
narrative (memoir writing), analyzing product placement in media, the
imperative mood and giving clear instructions, analyzing the structure of
a persuasive speech, anagrams and wordplay, writing a restaurant or
product review.
Math: calculating speed/distance/time, the triangle inequality theorem,
graphing linear inequalities in two variables, percentiles and quartiles,
understanding GST/PST/HST, solving proportions using cross-multiplication,
classifying quadrilaterals by properties, calculating percent change and
percent error, volume and capacity (litres and cubic centimetres).
Science: factors that affect the rate of a chemical reaction, transverse
and longitudinal waves, element families and trends in the periodic
table, plant adaptations to extreme climates, how encryption protects
digital information, understanding pressure (atmospheric and fluid), how
our solar system formed, distillation and separating mixtures, renewable
vs nonrenewable resources.
SocialStudies: the Battle of Vimy Ridge, the creation of the Canadian
National Railway, the 1950 Winnipeg Flood and disaster response, the
history of Canadian currency and the Royal Canadian Mint, the Metis
Nation and modern recognition of rights, the history of Canada Post, the
2010 Vancouver Winter Olympics and national identity, the Newfoundland
confederation debate and joining Canada in 1949, the Ontario Human Rights
Code.

None of these titles or underlying topics duplicate anything appearing in
Days 1-150 of data/grade7.json (verified by dumping every existing
(subject, title) pair before writing this file). Day 160 is a
cross-subject review day drawing quiz content from Days 151-159 of this
batch, with review titles kept textually distinct from every earlier
review day (including Day 150's four review titles).

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are dropped entirely, matching the convention established in
gen_grade7_days111_120.py through gen_grade7_days141_150.py (e.g.
"Canadas" not "Canada's").

Usage:
  cd ~/gradesbooster && python3 gen_grade7_days151_160.py
  cd ~/gradesbooster && python3 build_json.py --grade 7
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science and Technology',
    'TVO Learn: Grade 7 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L7, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M7, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S7, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS7, q)


def _rebalance_answer_positions(days, seed=20260809):
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


g7_151_160 = [
day(151, [
L('Grammar: Compound-Complex Sentences',
  'Grade 7 Language strand: a compound-complex sentence combines at least two independent clauses with at least one dependent clause, allowing a writer to link multiple related ideas of differing importance within a single sentence.',
  [('What is a compound-complex sentence?', ['A sentence with at least two independent clauses and one dependent clause', 'A sentence with only one clause and no punctuation', 'A concept unrelated to grammar', 'A sentence that never contains a verb'], 0),
   ('Which part of a compound-complex sentence expresses a complete thought on its own?', ['An independent clause', 'A dependent clause', 'A concept unrelated to compound-complex sentences', 'A single noun with no verb'], 0),
   ('Which sentence is an example of a compound-complex sentence?', ['Although it was raining, we went outside, and we still had fun.', 'It was raining outside.', 'Raining fun outside we went.', 'Fun we had outside, raining.'], 0),
   ('Why might a writer use a compound-complex sentence rather than several short sentences?', ['To show how multiple related ideas connect and depend on one another', 'Compound-complex sentences always make writing harder to understand', 'A concept unrelated to grammar', 'Short sentences can never be combined into a longer one'], 0),
   ('What is one risk of overusing compound-complex sentences in a piece of writing?', ['The writing can become difficult to follow if clauses are not organized clearly', 'Compound-complex sentences are always the clearest possible option', 'This concept has no relevance to grammar', 'Overusing them always makes writing shorter'], 0)]),
M('Measurement: Calculating Speed, Distance, and Time',
  'Grade 7 Math strand: speed can be calculated by dividing the distance travelled by the time taken, and rearranging this relationship allows a person to solve for distance or time when the other two values are known.',
  [('What formula is used to calculate speed?', ['Distance divided by time', 'Time divided by distance', 'A concept unrelated to measurement', 'Distance multiplied by time'], 0),
   ('If a car travels 150 kilometres in 3 hours, what is its average speed?', ['50 km/h', '450 km/h', '3 km/h', '147 km/h'], 0),
   ('If speed equals distance divided by time, how would you rearrange the formula to solve for distance?', ['Distance equals speed multiplied by time', 'Distance equals speed divided by time', 'A concept unrelated to speed and distance', 'Distance equals time divided by speed'], 0),
   ('If a cyclist travels at 20 km/h for 2 hours, how far do they travel?', ['40 km', '10 km', '22 km', '18 km'], 0),
   ('Why is average speed sometimes different from an objects speed at any single moment during a trip?', ['Speed can vary throughout a trip, and average speed represents the overall rate', 'Average speed is always identical to the speed at every single moment', 'A concept unrelated to measurement', 'Speed can never change once a trip has begun'], 0)]),
Sc('Chemistry: Factors That Affect the Rate of a Chemical Reaction',
   'Grade 7 Science strand: the rate of a chemical reaction can be increased by raising the temperature, increasing the concentration of reactants, increasing surface area, or adding a catalyst, each of which increases how often and how effectively particles collide.',
   [('What generally happens to a reaction rate when temperature is increased?', ['It generally increases', 'It always stays exactly the same', 'A concept unrelated to chemistry', 'It always decreases sharply'], 0),
    ('What is a catalyst?', ['A substance that speeds up a reaction without being permanently used up', 'A substance that always slows down every reaction', 'A concept unrelated to chemical reactions', 'A substance that can never be involved in a reaction'], 0),
    ('Why does increasing surface area often speed up a reaction?', ['More particles are exposed and available to collide and react', 'Increasing surface area always slows every reaction down', 'A concept unrelated to reaction rates', 'Surface area has no effect on how particles collide'], 0),
    ('How does increasing the concentration of reactants generally affect reaction rate?', ['It generally increases the rate because particles collide more often', 'It always decreases the rate of a reaction', 'This concept has no connection to chemistry', 'Concentration has no effect on collision frequency'], 0),
    ('Why do refrigerators slow down the rate at which food spoils?', ['Lower temperatures slow the chemical reactions that cause spoilage', 'Refrigerators speed up every reaction that causes spoilage', 'This concept has no relevance to science', 'Temperature has no effect on the rate of any reaction'], 0)]),
SS('Social Studies: The Battle of Vimy Ridge and Its Legacy',
   'Grade 7 Social Studies strand: in April 1917 Canadian troops fought together as a unified force for the first time to capture Vimy Ridge during the First World War, and the victory is remembered as a defining moment in the development of Canadian national identity.',
   [('In what year did the Battle of Vimy Ridge take place?', ['1917', '1867', '1949', '1885'], 0),
    ('What made the Canadian effort at Vimy Ridge significant militarily?', ['Canadian troops fought together as a unified force for the first time', 'No Canadian troops were involved in the battle at all', 'A concept unrelated to Canadian history', 'The battle involved no coordinated planning of any kind'], 0),
    ('Why is Vimy Ridge often described as a defining moment for Canadian identity?', ['The victory became a symbol of national pride and unity', 'The battle had no lasting significance for Canada', 'A concept unrelated to the Battle of Vimy Ridge', 'It caused Canada to permanently withdraw from world affairs'], 0),
    ('During which larger conflict did the Battle of Vimy Ridge take place?', ['The First World War', 'The Second World War', 'The Korean War', 'The Boer War'], 0),
    ('What is one way Canada continues to commemorate the Battle of Vimy Ridge today?', ['Through memorials and annual remembrance ceremonies', 'The battle is never mentioned or commemorated in any way', 'This concept has no relevance to social studies', 'By ignoring the event entirely in official history'], 0)]),
]),
day(152, [
L('Vocabulary: Clipped Words and Word Shortening',
  'Grade 7 Language strand: a clipped word is a shortened form of a longer word that keeps the same meaning, such as gym from gymnasium or phone from telephone, and clipping is a common way English vocabulary evolves over time.',
  [('What is a clipped word?', ['A shortened form of a longer word that keeps the same meaning', 'A word that is always longer than its original form', 'A concept unrelated to vocabulary', 'A word with no connection to any other word'], 0),
   ('Which of these is an example of a clipped word?', ['Gym', 'Elephant', 'A concept unrelated to clipping', 'Umbrella'], 0),
   ('What longer word does the clipped word phone come from?', ['Telephone', 'Photograph', 'A concept unrelated to word shortening', 'Microphone'], 0),
   ('Why might speakers use a clipped word instead of the full original word?', ['It is quicker and more convenient to say in everyday conversation', 'Clipped words are always more difficult to pronounce', 'This concept has no connection to vocabulary', 'Clipped words always confuse listeners completely'], 0),
   ('How does clipping differ from creating an entirely new word?', ['Clipping shortens an existing word rather than inventing a brand-new one', 'Clipping and inventing a new word are always exactly the same process', 'This concept has no relevance to vocabulary', 'Clipping always adds extra letters to a word'], 0)]),
M('Geometry: The Triangle Inequality Theorem',
  'Grade 7 Math strand: the triangle inequality theorem states that the sum of the lengths of any two sides of a triangle must be greater than the length of the third side, which determines whether three given lengths can actually form a triangle.',
  [('What does the triangle inequality theorem state?', ['The sum of any two sides must be greater than the third side', 'The sum of any two sides must always be less than the third side', 'A concept unrelated to geometry', 'All three sides of a triangle must always be equal'], 0),
   ('Can side lengths of 2, 3, and 10 form a triangle?', ['No, because 2 plus 3 is not greater than 10', 'Yes, any three lengths can always form a triangle', 'A concept unrelated to the triangle inequality theorem', 'It is impossible to determine without more information'], 0),
   ('Can side lengths of 5, 6, and 7 form a triangle?', ['Yes, because each pair of sides sums to more than the third side', 'No, because these lengths could never form a triangle', 'A concept unrelated to triangles', 'It is impossible to determine without more information'], 0),
   ('Why is the triangle inequality theorem useful when checking measurements before building a triangular structure?', ['It confirms whether the given lengths can actually form a closed triangle', 'It has no practical use in construction or design', 'A concept unrelated to geometry', 'It only applies to shapes that are not triangles'], 0),
   ('If two sides of a triangle measure 4 and 9, which of these could NOT be the length of the third side?', ['3', '6', '10', '12'], 0)]),
Sc('Physics: Transverse and Longitudinal Waves',
   'Grade 7 Science strand: a transverse wave moves particles up and down at right angles to the direction the wave travels, as in a wave on a rope, while a longitudinal wave moves particles back and forth in the same direction as the wave, as in a sound wave.',
   [('In a transverse wave, how do particles move relative to the direction of the wave?', ['At right angles, or perpendicular, to the direction of the wave', 'In exactly the same direction as the wave travels', 'A concept unrelated to waves', 'Particles never move at all in a transverse wave'], 0),
    ('In a longitudinal wave, how do particles move relative to the direction of the wave?', ['Back and forth in the same direction as the wave', 'At right angles to the direction the wave travels', 'A concept unrelated to longitudinal waves', 'Particles never move at all in a longitudinal wave'], 0),
    ('Which of these is an example of a longitudinal wave?', ['A sound wave travelling through air', 'A wave travelling along a shaken rope', 'A concept unrelated to physics', 'Light reflecting off a still pond'], 0),
    ('Which of these is an example of a transverse wave?', ['A wave travelling along a shaken rope', 'A sound wave travelling through air', 'A concept unrelated to transverse waves', 'A wave that has no particles involved at all'], 0),
    ('Why can sound waves travel through air but not through a vacuum?', ['Sound waves need particles of matter to compress and transmit the vibration', 'Sound waves travel equally well with or without any particles present', 'This concept has no relevance to science', 'A vacuum always transmits sound better than air does'], 0)]),
SS('Social Studies: The Creation of the Canadian National Railway',
   'Grade 7 Social Studies strand: the Canadian National Railway was formed in 1919 when the federal government combined several financially struggling private railways into a single publicly owned company, helping stabilize rail service across the country.',
   [('In what year was the Canadian National Railway formed?', ['1919', '1867', '1885', '1949'], 0),
    ('Why did the federal government create the Canadian National Railway?', ['To combine struggling private railways into one stable, publicly owned company', 'To eliminate all rail service across the country permanently', 'A concept unrelated to Canadian history', 'To sell Canadian rail lines to a foreign government'], 0),
    ('How did the Canadian National Railway differ from the earlier Canadian Pacific Railway?', ['It was publicly owned rather than a private company', 'It was built entirely by a foreign government', 'A concept unrelated to Canadian railways', 'It never connected any regions of the country'], 0),
    ('What problem among private railway companies led to the creation of CNR?', ['Several private railways were financially struggling and at risk of failing', 'Private railways were far too profitable and needed government limits', 'A concept unrelated to the Canadian National Railway', 'There were no private railway companies operating in Canada at the time'], 0),
    ('Why was reliable national rail service considered important for Canada in the early twentieth century?', ['It helped connect distant regions for trade, transportation, and communication', 'Rail service had no impact on trade or communication', 'This concept has no relevance to social studies', 'Canada relied entirely on other countries for all transportation'], 0)]),
]),
day(153, [
L('Reading: Analyzing Static and Dynamic Characters',
  'Grade 7 Language strand: a static character remains essentially the same throughout a story, while a dynamic character undergoes a significant, lasting change in personality, beliefs, or outlook as a result of the events in the plot.',
  [('What is a static character?', ['A character who remains essentially the same throughout a story', 'A character who is never mentioned again after the introduction', 'A concept unrelated to reading', 'A character who changes completely every single page'], 0),
   ('What is a dynamic character?', ['A character who undergoes a significant, lasting change during the story', 'A character who never appears in more than one scene', 'A concept unrelated to dynamic characters', 'A character who remains identical from beginning to end'], 0),
   ('What might cause a dynamic character to change?', ['Events or challenges faced during the plot of the story', 'Dynamic characters never change for any reason', 'A concept unrelated to reading', 'A change in the font used to print the story'], 0),
   ('Which best describes a story featuring a dynamic protagonist?', ['A character who starts selfish but learns to care about others by the end', 'A character who behaves identically in the first and final scenes', 'A concept unrelated to character analysis', 'A character who never interacts with anyone else in the story'], 0),
   ('Why might an author include both static and dynamic characters in the same story?', ['Static characters can highlight, by contrast, how much the dynamic character has changed', 'Including both types of characters is always considered a writing mistake', 'This concept has no relevance to reading', 'Static and dynamic characters can never appear in the same story'], 0)]),
M('Algebra: Graphing Linear Inequalities in Two Variables on the Cartesian Plane',
  'Grade 7 Math strand: graphing a linear inequality in two variables involves drawing the boundary line for the related equation, then shading the region of the Cartesian plane that contains all the points satisfying the inequality.',
  [('What is the first step in graphing a linear inequality in two variables?', ['Draw the boundary line for the related linear equation', 'Immediately shade the entire coordinate plane', 'A concept unrelated to algebra', 'Erase the x-axis and y-axis completely'], 0),
   ('What does shading a region of the graph represent?', ['All the points that satisfy the inequality', 'A single point that satisfies the inequality', 'A concept unrelated to graphing inequalities', 'The boundary line itself and nothing else'], 0),
   ('When graphing y is greater than 2x plus 1, would the boundary line typically be solid or dashed?', ['Dashed, because points on the line itself are not included', 'Solid, because points on the line are always included', 'A concept unrelated to linear inequalities', 'Neither, because no boundary line is ever drawn'], 0),
   ('When graphing y is greater than or equal to 2x plus 1, would the boundary line be solid or dashed?', ['Solid, because points on the line are included', 'Dashed, because points on the line are never included', 'A concept unrelated to graphing inequalities', 'Neither, because the inequality has no boundary line'], 0),
   ('Why might a business use a graphed linear inequality to represent a budget constraint?', ['It shows every possible combination of purchases that stays within the budget', 'Graphed inequalities have no practical business application', 'A concept unrelated to algebra', 'It shows only a single, fixed combination of purchases'], 0)]),
Sc('Chemistry: Element Families and Trends in the Periodic Table',
   'Grade 7 Science strand: elements in the periodic table are organized into families, or groups, that share similar chemical properties, such as the highly reactive alkali metals in the first column and the unreactive noble gases in the final column.',
   [('What do elements within the same family, or group, of the periodic table generally share?', ['Similar chemical properties', 'Completely unrelated chemical properties', 'A concept unrelated to chemistry', 'Identical physical appearances with no exceptions'], 0),
    ('Which family of elements is known for being highly reactive metals found in the first column?', ['Alkali metals', 'Noble gases', 'A concept unrelated to the periodic table', 'Halogens'], 0),
    ('Which family of elements is known for being largely unreactive gases?', ['Noble gases', 'Alkali metals', 'A concept unrelated to element families', 'Transition metals'], 0),
    ('How are elements typically arranged in the periodic table?', ['By increasing atomic number, in rows and columns based on properties', 'In alphabetical order with no other pattern', 'A concept unrelated to chemistry', 'Randomly, with no organizing pattern at all'], 0),
    ('Why is the periodic table considered a useful tool for predicting how an element will behave?', ['Its position reveals patterns in properties shared with other elements in the same family', 'The periodic table has no connection to how elements behave', 'This concept has no relevance to science', 'Every element behaves identically regardless of its position'], 0)]),
SS('Social Studies: The 1950 Winnipeg Flood and Disaster Response in Canada',
   'Grade 7 Social Studies strand: the 1950 Winnipeg Flood was one of the most severe floods in Manitoba history, forcing tens of thousands of residents to evacuate and prompting the later construction of the Red River Floodway to help protect the city from future flooding.',
   [('In what year did the major Winnipeg Flood take place?', ['1950', '1917', '1867', '1985'], 0),
    ('In which province did the 1950 flood occur?', ['Manitoba', 'Ontario', 'Alberta', 'Quebec'], 0),
    ('What large infrastructure project was later built to help protect Winnipeg from future floods?', ['The Red River Floodway', 'The Rideau Canal', 'A concept unrelated to the Winnipeg Flood', 'The St. Lawrence Seaway'], 0),
    ('What was one immediate effect of the 1950 Winnipeg Flood on residents?', ['Tens of thousands of residents were forced to evacuate their homes', 'The flood had no effect on any residents of the city', 'A concept unrelated to the Winnipeg Flood', 'Residents were required to relocate permanently to another province'], 0),
    ('Why do governments often invest in infrastructure like floodways after a major natural disaster?', ['To reduce the damage and risk caused by similar disasters in the future', 'Infrastructure investment never reduces the risk of future disasters', 'This concept has no relevance to social studies', 'Governments are legally forbidden from responding to natural disasters'], 0)]),
]),
day(154, [
L('Writing: Writing an Autobiographical Narrative (Memoir Writing)',
  'Grade 7 Language strand: an autobiographical narrative, or memoir, tells a true story from the writers own life, focusing on a meaningful event or period and reflecting on what the experience taught them.',
  [('What is an autobiographical narrative, or memoir?', ['A true story told from the writers own life experience', 'A completely fictional story with invented characters', 'A concept unrelated to writing', 'A story written entirely by someone else about a stranger'], 0),
   ('What does a memoir typically focus on?', ['A meaningful event or period from the writers life', 'A random collection of unrelated facts', 'A concept unrelated to memoir writing', 'Events that never actually happened'], 0),
   ('Why might a memoir include the writers reflections on an experience?', ['To share what the experience taught them or how it changed their perspective', 'Reflections are never included in a memoir', 'A concept unrelated to writing', 'To completely avoid discussing the writers own feelings'], 0),
   ('How does a memoir generally differ from a purely fictional short story?', ['A memoir is based on true events from the writers own life', 'A memoir and a fictional short story are always identical', 'This concept has no connection to writing', 'A memoir must always be written by someone other than the author'], 0),
   ('Which opening sounds most like the start of a memoir?', ['The summer I turned eleven, my grandmother taught me a lesson I have never forgotten.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Data Management: Percentiles and Quartiles in Data Analysis',
  'Grade 7 Math strand: percentiles and quartiles divide a data set into equal parts to show how one value compares to the rest of the set, with quartiles splitting data into four equal parts and the median forming the boundary between the second and third quartiles.',
  [('What do quartiles do to a data set?', ['Divide it into four equal parts', 'Divide it into exactly two equal parts', 'A concept unrelated to data management', 'Combine every value into a single number with no divisions'], 0),
   ('What does it mean if a students test score is in the 90th percentile?', ['The score is higher than about 90 percent of the other scores in the set', 'The score is exactly 90 out of 100 on the test', 'A concept unrelated to percentiles', 'The score is lower than every other score in the set'], 0),
   ('Which quartile does the median of a data set correspond to?', ['The boundary between the second and third quartiles', 'The boundary between the first and second quartiles only', 'A concept unrelated to quartiles', 'The median has no connection to quartiles at all'], 0),
   ('Why might percentiles be useful when comparing an individual value to a large data set?', ['They show how that value ranks relative to the rest of the data', 'Percentiles never provide any useful comparison information', 'A concept unrelated to data management', 'Percentiles can only be calculated for very small data sets'], 0),
   ('What is the interquartile range generally based on?', ['The difference between the first and third quartiles', 'The difference between the highest and lowest values only', 'A concept unrelated to interquartile range', 'The single largest value in the entire data set'], 0)]),
Sc('Biology: Plant Adaptations to Extreme Climates',
   'Grade 7 Science strand: plants living in extreme climates develop specialized adaptations, such as thick waxy leaves and deep roots in desert plants to conserve water, or low, cushion-like growth in arctic plants to survive wind and cold.',
   [('Why do many desert plants have thick, waxy leaves?', ['To reduce water loss in a dry climate', 'To attract as many insects as possible', 'A concept unrelated to biology', 'Thick waxy leaves have no connection to water conservation'], 0),
    ('Why might a desert plant develop very deep roots?', ['To reach water stored far below the surface', 'Deep roots have no effect on a plants access to water', 'A concept unrelated to plant adaptations', 'To avoid absorbing any water from the soil at all'], 0),
    ('Why do many arctic plants grow low to the ground?', ['To avoid damage from strong winds and stay insulated near the warmer ground', 'Growing low to the ground has no survival benefit in the arctic', 'A concept unrelated to plant adaptations', 'To reach sunlight that only exists deep underground'], 0),
    ('Which adaptation would most likely help a plant survive in a desert environment?', ['Storing water in thick stems or leaves', 'Growing extremely large, thin leaves that lose water quickly', 'A concept unrelated to desert adaptations', 'Having no roots of any kind'], 0),
    ('Why do plants in extreme climates generally need different adaptations than plants in a mild, temperate climate?', ['Extreme climates present unique survival challenges like extreme heat, cold, or lack of water', 'All climates present the exact same survival challenges for plants', 'This concept has no relevance to science', 'Plants never need to adapt to their surrounding climate'], 0)]),
SS('Social Studies: The History of Canadian Currency and the Royal Canadian Mint',
   'Grade 7 Social Studies strand: the Royal Canadian Mint, established in 1908, produces Canadas coins and has issued circulating currency featuring evolving designs and security features, reflecting the countrys changing economy and identity over time.',
   [('In what year was the Royal Canadian Mint established?', ['1908', '1867', '1949', '1982'], 0),
    ('What is the main role of the Royal Canadian Mint?', ['Producing Canadas coins', 'Printing newspapers for the federal government', 'A concept unrelated to Canadian history', 'Regulating interprovincial trade agreements'], 0),
    ('Why might currency designs change over time?', ['To reflect the countrys changing identity, history, or security needs', 'Currency designs are legally required to remain identical forever', 'A concept unrelated to Canadian currency', 'Currency designs have no connection to a countrys history'], 0),
    ('What is one reason governments add security features to currency?', ['To make currency more difficult to counterfeit', 'Security features have no practical purpose on currency', 'A concept unrelated to the Royal Canadian Mint', 'To make currency easier for anyone to copy'], 0),
    ('Why is a reliable national currency important for a countrys economy?', ['It gives people a trusted, standard way to exchange goods and services', 'A reliable currency has no effect on a countrys economy', 'This concept has no relevance to social studies', 'Currency is never used in everyday economic exchanges'], 0)]),
]),
day(155, [
L('Media Literacy: Analyzing Product Placement in Media',
  'Grade 7 Language strand: product placement is the practice of featuring a brand or product within a movie, show, or video in a way that appears natural, allowing companies to advertise without a traditional, clearly labeled commercial.',
  [('What is product placement?', ['Featuring a brand or product within media content in a way that appears natural', 'A commercial that clearly interrupts a show to advertise a product', 'A concept unrelated to media literacy', 'A product that is never shown in any media of any kind'], 0),
   ('Why might a company prefer product placement over a traditional commercial?', ['It can advertise without a clearly labeled break, making the promotion feel less obvious', 'Product placement is always far more expensive with no added benefit', 'A concept unrelated to product placement', 'Traditional commercials are always more effective than product placement'], 0),
   ('Which situation is an example of product placement?', ['A character in a movie visibly drinks from a branded soda can during a scene', 'A thirty-second commercial break shown between two television programs', 'A concept unrelated to media literacy', 'A billboard advertisement seen along a highway'], 0),
   ('Why might product placement be harder for viewers to recognize than a traditional advertisement?', ['It is woven into the story or content rather than clearly separated as an ad', 'Product placement is always labeled clearly with the word advertisement', 'This concept has no connection to media literacy', 'Viewers are always told in advance exactly when product placement occurs'], 0),
   ('Why is it useful for media-literate viewers to notice product placement?', ['It helps them recognize when they are being advertised to, even subtly', 'Noticing product placement serves no useful purpose for viewers', 'This concept has no relevance to media literacy', 'Product placement has no influence on viewer behaviour or opinions'], 0)]),
M('Financial Literacy: Understanding GST, PST, and HST',
  'Grade 7 Math strand: GST is a federal sales tax applied across Canada, PST is a separate provincial sales tax charged in some provinces, and HST combines the federal and provincial portions into a single blended tax rate in provinces that use it.',
  [('What does GST stand for?', ['Goods and Services Tax', 'General Spending Tariff', 'A concept unrelated to financial literacy', 'Government Savings Trust'], 0),
   ('What is the main difference between GST and PST?', ['GST is a federal tax while PST is a separate provincial tax', 'GST and PST are always exactly the same tax under different names', 'A concept unrelated to sales tax', 'PST is charged only outside of Canada'], 0),
   ('What does HST combine into a single rate?', ['The federal and provincial sales tax portions', 'Two completely unrelated types of income tax', 'A concept unrelated to HST', 'Property tax and income tax combined'], 0),
   ('If an item costs 100 dollars before tax and the HST rate is 13 percent, what is the total cost including tax?', ['113 dollars', '100 dollars', '130 dollars', '87 dollars'], 0),
   ('Why might sales tax rates differ from one province to another?', ['Each province sets its own provincial tax rate or chooses whether to use HST', 'Every province in Canada is legally required to charge an identical tax rate', 'A concept unrelated to financial literacy', 'Sales tax rates are decided entirely by individual retail stores'], 0)]),
Sc('Technology: How Encryption Protects Digital Information',
   'Grade 7 Science strand: encryption converts readable data into a coded format using a mathematical algorithm, so that only someone with the correct key can convert it back into its original, readable form, helping protect private information sent online.',
   [('What does encryption do to readable data?', ['Converts it into a coded format that is difficult to read without a key', 'Deletes the data permanently so nobody can ever read it', 'A concept unrelated to technology', 'Makes the data easier for anyone to read instantly'], 0),
    ('What is needed to convert encrypted data back into its original, readable form?', ['The correct decryption key', 'A completely different, unrelated set of data', 'A concept unrelated to encryption', 'Nothing at all is needed to reverse encryption'], 0),
    ('Why is encryption important when sending private information over the internet?', ['It helps prevent unauthorized people from reading the information if it is intercepted', 'Encryption makes private information easier for anyone to access', 'A concept unrelated to digital security', 'Encryption has no effect on the privacy of transmitted data'], 0),
    ('Which of these is an example of a situation where encryption is commonly used?', ['Sending a password during a secure online banking login', 'Reading a printed newspaper at home', 'A concept unrelated to encryption', 'Watching a movie with no internet connection involved'], 0),
    ('Why might a hacker have a very difficult time reading properly encrypted data without the key?', ['The coded data is scrambled using complex mathematical operations that are hard to reverse without it', 'Encrypted data is always left completely unprotected and easy to read', 'This concept has no relevance to science', 'Hackers automatically receive the decryption key for any encrypted data'], 0)]),
SS('Social Studies: The Metis Nation and Modern Recognition of Rights',
   'Grade 7 Social Studies strand: the Metis Nation, formed from historic unions between First Nations and European peoples, gained formal recognition as one of Canadas Aboriginal peoples under the 1982 Constitution, with later court decisions clarifying and strengthening Metis rights.',
   [('What historical unions led to the formation of the Metis Nation?', ['Unions between First Nations and European peoples', 'Unions between two entirely European nations', 'A concept unrelated to Canadian history', 'Unions that took place outside of North America'], 0),
    ('Under which document did the Metis gain formal recognition as one of Canadas Aboriginal peoples?', ['The 1982 Constitution', 'The Halibut Treaty of 1923', 'A concept unrelated to the Metis Nation', 'The Statute of Westminster'], 0),
    ('What role have court decisions played in Metis rights since 1982?', ['They have clarified and strengthened the legal recognition of Metis rights', 'Court decisions have completely eliminated all Metis rights', 'A concept unrelated to social studies', 'No court decisions have ever addressed Metis rights'], 0),
    ('Why is formal recognition in the Constitution significant for the Metis Nation?', ['It establishes legal acknowledgment of their status and rights as an Aboriginal people', 'It removes any legal recognition of the Metis Nation entirely', 'A concept unrelated to the Metis Nation', 'It has no connection to the rights of the Metis people'], 0),
    ('How does the history of the Metis Nation connect to earlier events like the Red River Resistance?', ['Metis identity and rights have been shaped by a long history including these earlier events', 'The Metis Nation has no historical connection to the Red River Resistance', 'This concept has no relevance to social studies', 'The Red River Resistance involved a completely unrelated group of people'], 0)]),
]),
day(156, [
L('Grammar: The Imperative Mood and Giving Clear Instructions',
  'Grade 7 Language strand: the imperative mood is used to give commands, instructions, or requests, typically beginning with a verb and often leaving the subject you implied rather than stated directly.',
  [('What is the imperative mood used for?', ['Giving commands, instructions, or requests', 'Describing a series of past events only', 'A concept unrelated to grammar', 'Asking a question about the future'], 0),
   ('In an imperative sentence, which word is typically left unstated but implied?', ['You', 'They', 'A concept unrelated to the imperative mood', 'It'], 0),
   ('Which sentence uses the imperative mood?', ['Close the door before you leave.', 'She closed the door before she left.', 'Did you close the door before you left?', 'The door was closed before anyone left.'], 0),
   ('Why might a recipe use imperative sentences?', ['To give clear, direct instructions for each step', 'Recipes never use imperative sentences of any kind', 'A concept unrelated to grammar', 'Imperative sentences always confuse the reader of a recipe'], 0),
   ('How does an imperative sentence generally begin?', ['With a verb', 'With a question mark', 'A concept unrelated to imperative sentences', 'With the word therefore'], 0)]),
M('Algebra: Solving Proportions Using Cross-Multiplication',
  'Grade 7 Math strand: cross-multiplication is a method for solving a proportion by multiplying the numerator of one ratio by the denominator of the other, setting the two products equal to each other, and solving for the unknown value.',
  [('What does cross-multiplication involve?', ['Multiplying the numerator of one ratio by the denominator of the other and setting the products equal', 'Adding the numerators of both ratios together', 'A concept unrelated to algebra', 'Dividing both ratios by the same unrelated number'], 0),
   ('If 3/4 equals x/12, what is the value of x?', ['9', '16', '3', '4'], 0),
   ('Why is cross-multiplication a useful method for solving proportions?', ['It turns the proportion into a simple equation that can be solved directly', 'Cross-multiplication never produces a solvable equation', 'A concept unrelated to proportions', 'It only works for proportions with no unknown values'], 0),
   ('If 5/x equals 15/9, what is the value of x?', ['3', '5', '15', '9'], 0),
   ('Why must both ratios in a proportion represent the same relationship for cross-multiplication to give a meaningful answer?', ['The method assumes the two ratios are equal to begin with', 'Cross-multiplication works correctly even when the ratios are unrelated', 'This concept has no relevance to algebra', 'Proportions never require the two ratios to be equal'], 0)]),
Sc('Physics: Understanding Pressure — Atmospheric and Fluid',
   'Grade 7 Science strand: pressure is the amount of force applied over a given area, and it can be exerted by the atmosphere pressing down on Earths surface or by a fluid such as water pressing on an object submerged within it.',
   [('What is pressure?', ['The amount of force applied over a given area', 'The total weight of an object regardless of area', 'A concept unrelated to physics', 'The speed at which an object moves through air'], 0),
    ('What is atmospheric pressure?', ['The force exerted by the weight of air pressing down on Earths surface', 'The force exerted only by water on a submerged object', 'A concept unrelated to atmospheric pressure', 'A force that exists only in outer space'], 0),
    ('How does water pressure generally change as depth increases?', ['It increases as depth increases', 'It decreases as depth increases', 'A concept unrelated to fluid pressure', 'It always stays exactly the same at every depth'], 0),
    ('Why might your ears feel pressure changes when diving deep underwater?', ['Increasing water pressure pushes against your eardrums as you go deeper', 'Water pressure has no effect on the human body at any depth', 'This concept has no connection to science', 'Ears only respond to changes in atmospheric pressure, never water pressure'], 0),
    ('Why is pressure calculated using both force and area rather than force alone?', ['The same force spread over a smaller area produces greater pressure', 'Area has no effect on the amount of pressure produced', 'This concept has no relevance to physics', 'Force alone always produces the exact same pressure regardless of area'], 0)]),
SS('Social Studies: The History of Canada Post and Postal Service',
   'Grade 7 Social Studies strand: Canada Post traces its roots to colonial mail services established in the 1700s, was formally organized as a federal department after Confederation, and became a Crown corporation in 1981, connecting communities across a vast country.',
   [('When did Canada Post become a Crown corporation?', ['1981', '1867', '1949', '1917'], 0),
    ('What did colonial mail services in Canada trace their roots back to?', ['The 1700s', 'The 1950s', 'A concept unrelated to Canadian postal history', 'The 1980s'], 0),
    ('What happened to the postal service after Confederation?', ['It was formally organized as a federal department', 'It was immediately shut down and never operated again', 'A concept unrelated to Canada Post', 'It was transferred entirely to another country'], 0),
    ('Why has reliable postal service historically been important in a country as large as Canada?', ['It connects distant and often remote communities across a vast country', 'Postal service has never played any role in connecting communities', 'A concept unrelated to social studies', 'Canada has always relied on other countries to deliver its mail'], 0),
    ('What is one way Canada Post has changed the way it operates in the digital age?', ['It has adapted to handle more package deliveries as online shopping increased', 'It has stopped delivering any packages or mail entirely', 'This concept has no relevance to social studies', 'Canada Post has remained completely unchanged since the 1700s'], 0)]),
]),
day(157, [
L('Reading: Analyzing the Structure of a Persuasive Speech',
  'Grade 7 Language strand: a persuasive speech typically opens with an attention-getting introduction, develops supporting arguments organized logically, addresses potential counterarguments, and closes with a strong call to action.',
  [('What does a persuasive speech typically open with?', ['An attention-getting introduction', 'A detailed list of unrelated statistics', 'A concept unrelated to reading', 'A summary of the opposing viewpoint only'], 0),
   ('Why might a persuasive speech address potential counterarguments?', ['To strengthen the argument by showing the speaker has considered opposing views', 'Addressing counterarguments always weakens a persuasive speech', 'A concept unrelated to persuasive speeches', 'Persuasive speeches are required to ignore any opposing views'], 0),
   ('What does a persuasive speech typically end with?', ['A strong call to action', 'A list of unrelated facts with no clear purpose', 'A concept unrelated to reading', 'An open-ended question with no clear conclusion'], 0),
   ('Why is logical organization of supporting arguments important in a persuasive speech?', ['It helps the audience follow and be convinced by the reasoning', 'Logical organization has no effect on how convincing a speech is', 'This concept has no connection to reading', 'Persuasive speeches are more effective when arguments are randomly ordered'], 0),
   ('Which ending best fits the structure of a persuasive speech?', ['So today, I ask each of you to join this effort and make a difference.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Data Management: Calculating Percent Change and Percent Error',
  'Grade 7 Math strand: percent change measures how much a value has increased or decreased relative to its original amount, while percent error measures how far a measured or estimated value is from the actual, correct value.',
  [('What does percent change measure?', ['How much a value has increased or decreased relative to its original amount', 'The exact difference between two unrelated data sets', 'A concept unrelated to data management', 'The total number of values in a data set'], 0),
   ('If a price rises from 40 dollars to 50 dollars, what is the percent increase?', ['25 percent', '10 percent', '50 percent', '20 percent'], 0),
   ('What does percent error measure?', ['How far a measured or estimated value is from the actual, correct value', 'The total number of measurements taken during an experiment', 'A concept unrelated to percent error', 'The exact value of a measurement with no comparison involved'], 0),
   ('If the actual value is 50 and the measured value is 45, what is the percent error?', ['10 percent', '5 percent', '50 percent', '90 percent'], 0),
   ('Why might scientists calculate percent error after an experiment?', ['To evaluate how accurate their measurement was compared to the true value', 'Percent error has no useful purpose in scientific experiments', 'A concept unrelated to data management', 'Percent error can only be calculated before an experiment begins'], 0)]),
Sc('Astronomy: How Our Solar System Formed',
   'Grade 7 Science strand: scientists believe the solar system formed about 4.6 billion years ago from a giant, collapsing cloud of gas and dust, with most of the material forming the sun at the centre and the remaining material gradually clumping together to form the planets.',
   [('About how long ago do scientists believe the solar system formed?', ['About 4.6 billion years ago', 'About 4.6 thousand years ago', 'A concept unrelated to astronomy', 'About 100 years ago'], 0),
    ('What is the leading scientific explanation for how the solar system formed?', ['A giant, collapsing cloud of gas and dust gradually formed the sun and planets', 'The solar system has always existed exactly as it is today', 'A concept unrelated to how the solar system formed', 'A single planet split apart to create the sun and all other planets'], 0),
    ('What formed at the centre of the collapsing cloud of gas and dust?', ['The sun', 'The moon', 'A concept unrelated to solar system formation', 'A comet'], 0),
    ('How did the planets form according to this model?', ['Remaining material gradually clumped together through repeated collisions', 'Planets appeared instantly with no process of formation at all', 'A concept unrelated to astronomy', 'Planets formed entirely separately from the sun in unrelated events'], 0),
    ('Why do scientists study meteorites when researching how the solar system formed?', ['Some meteorites contain material largely unchanged since the solar systems early formation', 'Meteorites have no connection to the history of the solar system', 'This concept has no relevance to science', 'Meteorites always form long after a solar system has finished developing'], 0)]),
SS('Social Studies: The 2010 Vancouver Winter Olympics and National Identity',
   'Grade 7 Social Studies strand: the 2010 Winter Olympics held in Vancouver brought major international attention to Canada, showcased Canadian athletes on home soil, and became a widely remembered moment of shared national pride and identity.',
   [('In which Canadian city were the 2010 Winter Olympics held?', ['Vancouver', 'Toronto', 'Montreal', 'Calgary'], 0),
    ('Why might hosting the Olympics bring international attention to a country?', ['Athletes and audiences from around the world focus on the host country', 'Hosting the Olympics has no effect on international attention', 'A concept unrelated to the Vancouver Olympics', 'Only local residents are ever aware that the Olympics are taking place'], 0),
    ('What effect did the 2010 Olympics have on many Canadians sense of national pride?', ['It created a widely remembered moment of shared national pride and identity', 'It had no effect on how Canadians felt about their country', 'A concept unrelated to social studies', 'It caused most Canadians to lose interest in the Olympics entirely'], 0),
    ('What is one advantage for athletes competing in an Olympics held in their own country?', ['They get to compete in front of a home crowd and familiar conditions', 'Competing at home always provides no advantage of any kind', 'A concept unrelated to the Olympics', 'Athletes are never allowed to compete in their home country'], 0),
    ('Why might a country invest significant resources into hosting an event like the Olympics?', ['It can boost tourism, infrastructure, and international recognition', 'Hosting the Olympics never has any economic or social impact', 'This concept has no relevance to social studies', 'Countries are required by international law to host the Olympics'], 0)]),
]),
day(158, [
L('Vocabulary: Anagrams and Wordplay',
  'Grade 7 Language strand: an anagram is a word or phrase formed by rearranging the letters of another word or phrase, and anagrams are one form of wordplay that writers and puzzle creators use to explore language creatively.',
  [('What is an anagram?', ['A word or phrase formed by rearranging the letters of another word or phrase', 'A word that always means the exact opposite of another word', 'A concept unrelated to vocabulary', 'A word that can never be rearranged in any way'], 0),
   ('Which of these is an anagram of the word listen?', ['Silent', 'Loudly', 'A concept unrelated to anagrams', 'Quietly'], 0),
   ('Why might a puzzle creator use anagrams?', ['To challenge readers to find hidden words by rearranging letters', 'Anagrams are never used in puzzles of any kind', 'A concept unrelated to wordplay', 'To make a puzzle impossible for anyone to solve'], 0),
   ('What is one reason wordplay like anagrams can be useful for building vocabulary?', ['It encourages close attention to spelling and letter patterns', 'Wordplay has no connection to spelling or vocabulary at all', 'This concept has no relevance to vocabulary', 'Anagrams always ignore the letters of the original word'], 0),
   ('Which of these best describes wordplay in general?', ['Creative and playful use of language, such as puns, anagrams, or rhymes', 'A strictly formal style used only in legal documents', 'A concept unrelated to vocabulary', 'Language that avoids any creativity or playfulness'], 0)]),
M('Geometry: Classifying Quadrilaterals by Properties',
  'Grade 7 Math strand: quadrilaterals can be classified by properties such as side length, angle measure, and parallel sides, distinguishing shapes like parallelograms, rectangles, rhombuses, squares, and trapezoids from one another.',
  [('What property defines a parallelogram?', ['Both pairs of opposite sides are parallel', 'All four sides are always different lengths', 'A concept unrelated to geometry', 'It has no parallel sides at all'], 0),
   ('What distinguishes a rectangle from a general parallelogram?', ['A rectangle has four right angles', 'A rectangle never has any parallel sides', 'A concept unrelated to quadrilaterals', 'A rectangle always has four unequal angles'], 0),
   ('What distinguishes a rhombus from a general parallelogram?', ['A rhombus has four sides of equal length', 'A rhombus always has four unequal sides', 'A concept unrelated to rhombuses', 'A rhombus never has any parallel sides'], 0),
   ('What property must a trapezoid have?', ['Exactly one pair of parallel sides', 'Two pairs of parallel sides', 'A concept unrelated to trapezoids', 'No parallel sides of any kind'], 0),
   ('Why is a square considered both a rectangle and a rhombus?', ['It has four right angles and four equal sides, satisfying both definitions', 'A square shares no properties with either shape', 'This concept has no relevance to geometry', 'A square has neither right angles nor equal sides'], 0)]),
Sc('Chemistry: Distillation and Separating Mixtures',
   'Grade 7 Science strand: distillation separates the components of a mixture based on differences in boiling point, heating the mixture so the substance with the lower boiling point evaporates first and can then be cooled and collected separately.',
   [('What property does distillation use to separate a mixture?', ['Differences in boiling point', 'Differences in colour only', 'A concept unrelated to chemistry', 'Differences in the smell of each substance'], 0),
    ('During distillation, which substance in a mixture typically evaporates first?', ['The substance with the lower boiling point', 'The substance with the higher boiling point', 'A concept unrelated to distillation', 'Both substances always evaporate at exactly the same time'], 0),
    ('What happens to the evaporated substance after it rises during distillation?', ['It is cooled and condensed back into a liquid, then collected separately', 'It disappears permanently and is never collected', 'A concept unrelated to distillation', 'It immediately recombines with the original mixture'], 0),
    ('Which of these processes could distillation be used for?', ['Separating salt from water by evaporating and then condensing the water', 'Separating two identical substances that have the exact same boiling point', 'A concept unrelated to separating mixtures', 'Combining two liquids into a single new substance'], 0),
    ('Why is distillation considered a physical rather than a chemical process?', ['The substances involved are only separated, not chemically changed into new substances', 'Distillation always creates a brand-new chemical substance', 'This concept has no relevance to science', 'Physical and chemical processes are always exactly the same thing'], 0)]),
SS('Social Studies: The Newfoundland Confederation Debate and Joining Canada in 1949',
   'Grade 7 Social Studies strand: after years of economic hardship, Newfoundland held referendums in 1948 on whether to join Canada, remain a British colony, or seek independence, ultimately voting narrowly to become Canadas tenth province in 1949.',
   [('In what year did Newfoundland officially join Canada as a province?', ['1949', '1867', '1917', '1982'], 0),
    ('What method did Newfoundland use to decide its political future before joining Canada?', ['A series of referendums held in 1948', 'A decision made entirely by the British monarch', 'A concept unrelated to Newfoundlands history', 'A private vote held only among government officials'], 0),
    ('What were some of the options Newfoundlanders voted on in the referendums?', ['Joining Canada, remaining a British colony, or seeking independence', 'Joining the United States or joining France', 'A concept unrelated to the Newfoundland referendums', 'Only whether to change their official flag'], 0),
    ('Why might economic hardship have influenced Newfoundlands decision to join Canada?', ['Joining Canada offered access to greater economic support and stability', 'Economic hardship had no influence on the decision at all', 'A concept unrelated to Newfoundlands confederation debate', 'Newfoundland was economically stronger than Canada at the time'], 0),
    ('What number province did Newfoundland become when it joined Canada?', ['The tenth province', 'The first province', 'A concept unrelated to Canadian confederation', 'The fourth province'], 0)]),
]),
day(159, [
L('Writing: Writing a Restaurant or Product Review',
  'Grade 7 Language strand: a restaurant or product review describes a personal experience with specific details, evaluates strengths and weaknesses using clear criteria, and often ends with a recommendation to help other readers decide.',
  [('What does a restaurant or product review typically describe?', ['A personal experience with specific supporting details', 'A completely unrelated topic with no personal experience involved', 'A concept unrelated to writing', 'A review always avoids describing any specific details'], 0),
   ('Why might a review evaluate both strengths and weaknesses?', ['To give readers a fair, balanced picture before they decide', 'Reviews are required to mention only strengths and no weaknesses', 'A concept unrelated to writing a review', 'Balanced evaluation has no value in a review'], 0),
   ('What does a review often include at the end?', ['A recommendation to help readers decide', 'A list of unrelated topics with no connection to the review', 'A concept unrelated to reviews', 'A review never reaches any kind of conclusion'], 0),
   ('Why are specific details, such as exact dishes or features, useful in a review?', ['They help readers understand exactly what to expect', 'Specific details always confuse readers of a review', 'This concept has no connection to writing', 'Reviews are more effective when they avoid all specific details'], 0),
   ('Which sentence sounds most like part of a product review?', ['The battery lasted almost two full days, which was longer than I expected.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Measurement: Volume and Capacity — Litres and Cubic Centimetres',
  'Grade 7 Math strand: volume measures the amount of space an object occupies, while capacity measures how much a container can hold, and the two are connected by the fact that one litre is equal to exactly one thousand cubic centimetres.',
  [('How many cubic centimetres are in one litre?', ['1000', '100', 'A concept unrelated to measurement', '10'], 0),
   ('What does capacity measure?', ['How much a container can hold', 'The total mass of an object', 'A concept unrelated to volume and capacity', 'The exact temperature of a liquid'], 0),
   ('If a container has a volume of 2000 cubic centimetres, how many litres can it hold?', ['2 litres', '20 litres', '200 litres', '0.2 litres'], 0),
   ('Why are litres a convenient unit for measuring liquids in everyday life?', ['They directly relate to cubic centimetres, making conversions straightforward', 'Litres have no mathematical connection to cubic centimetres', 'A concept unrelated to measurement', 'Litres can never be used to measure any liquid'], 0),
   ('If a box measures 10 cm by 10 cm by 10 cm, what is its volume in cubic centimetres, and how many litres is that?', ['1000 cubic centimetres, which equals 1 litre', '100 cubic centimetres, which equals 1 litre', '10 cubic centimetres, which equals 1 litre', '10000 cubic centimetres, which equals 1 litre'], 0)]),
Sc('Earth Science: Renewable vs Nonrenewable Resources',
   'Grade 7 Science strand: renewable resources, such as sunlight and wind, can be replenished naturally within a short time, while nonrenewable resources, such as coal and oil, take millions of years to form and are being used far faster than they are replaced.',
   [('What makes a resource renewable?', ['It can be replenished naturally within a relatively short time', 'It takes millions of years to form and can never be replaced', 'A concept unrelated to earth science', 'It is always found only underground'], 0),
    ('What makes a resource nonrenewable?', ['It takes an extremely long time to form and is not easily replaced', 'It can be replenished naturally within a single day', 'A concept unrelated to renewable and nonrenewable resources', 'It is always replenished faster than it is used'], 0),
    ('Which of these is an example of a renewable resource?', ['Wind', 'Coal', 'A concept unrelated to earth science', 'Oil'], 0),
    ('Which of these is an example of a nonrenewable resource?', ['Coal', 'Wind', 'A concept unrelated to nonrenewable resources', 'Sunlight'], 0),
    ('Why are governments and industries increasingly interested in renewable resources?', ['Renewable resources can be replenished and produce fewer long-term supply concerns', 'Renewable resources are always more difficult to access than nonrenewable ones', 'This concept has no relevance to science', 'Nonrenewable resources can be replenished just as quickly as renewable ones'], 0)]),
SS('Social Studies: The Ontario Human Rights Code and Its Historical Development',
   'Grade 7 Social Studies strand: the Ontario Human Rights Code, passed in 1962, was the first law of its kind in Canada to combine various anti-discrimination protections into a single code, laying groundwork later reflected in the Canadian Charter of Rights and Freedoms.',
   [('In what year was the Ontario Human Rights Code passed?', ['1962', '1867', '1982', '1949'], 0),
    ('What made the Ontario Human Rights Code significant in Canadian history?', ['It was the first law of its kind in Canada to combine various anti-discrimination protections into one code', 'It was the last province to introduce any human rights protections', 'A concept unrelated to Canadian history', 'It removed all existing anti-discrimination protections in Ontario'], 0),
    ('What later national document reflected similar rights-based principles?', ['The Canadian Charter of Rights and Freedoms', 'The Halibut Treaty of 1923', 'A concept unrelated to the Ontario Human Rights Code', 'The Statute of Westminster'], 0),
    ('What is the general purpose of a human rights code?', ['To protect people from discrimination based on specific protected grounds', 'To eliminate all legal protections for citizens', 'A concept unrelated to social studies', 'To regulate international trade agreements'], 0),
    ('Why might provinces have developed their own human rights codes before a national charter existed?', ['Provinces have jurisdiction over many areas of daily life where discrimination protections were needed', 'Provinces have never had any authority over human rights protections', 'This concept has no relevance to social studies', 'A national charter existed long before any provincial human rights code'], 0)]),
]),
day(160, [
L('Language Review: Compound-Complex Sentences, Memoir Writing, and Wordplay',
  'Grade 7 Language strand review: students revisit compound-complex sentences, static and dynamic characters, memoir writing, the imperative mood, and anagrams and wordplay.',
  [('What is a compound-complex sentence?', ['A sentence with at least two independent clauses and one dependent clause', 'A sentence with only one clause and no punctuation', 'A concept unrelated to grammar', 'A sentence that never contains a verb'], 0),
   ('What is a dynamic character?', ['A character who undergoes a significant, lasting change during the story', 'A character who never appears in more than one scene', 'A concept unrelated to dynamic characters', 'A character who remains identical from beginning to end'], 0),
   ('What is an autobiographical narrative, or memoir?', ['A true story told from the writers own life experience', 'A completely fictional story with invented characters', 'A concept unrelated to writing', 'A story written entirely by someone else about a stranger'], 0),
   ('What is the imperative mood used for?', ['Giving commands, instructions, or requests', 'Describing a series of past events only', 'A concept unrelated to grammar', 'Asking a question about the future'], 0),
   ('What is an anagram?', ['A word or phrase formed by rearranging the letters of another word or phrase', 'A word that always means the exact opposite of another word', 'A concept unrelated to vocabulary', 'A word that can never be rearranged in any way'], 0)]),
M('Math Review: Speed, Inequalities, Percent Change, and Capacity',
  'Grade 7 Math strand review: students revisit speed/distance/time, graphing linear inequalities in two variables, percentiles and quartiles, percent change and percent error, and volume/capacity.',
  [('What formula is used to calculate speed?', ['Distance divided by time', 'Time divided by distance', 'A concept unrelated to measurement', 'Distance multiplied by time'], 0),
   ('What does shading a region of the graph represent when graphing a linear inequality?', ['All the points that satisfy the inequality', 'A single point that satisfies the inequality', 'A concept unrelated to graphing inequalities', 'The boundary line itself and nothing else'], 0),
   ('What do quartiles do to a data set?', ['Divide it into four equal parts', 'Divide it into exactly two equal parts', 'A concept unrelated to data management', 'Combine every value into a single number with no divisions'], 0),
   ('What does percent change measure?', ['How much a value has increased or decreased relative to its original amount', 'The exact difference between two unrelated data sets', 'A concept unrelated to data management', 'The total number of values in a data set'], 0),
   ('How many cubic centimetres are in one litre?', ['1000', '100', 'A concept unrelated to measurement', '10'], 0)]),
Sc('Science Review: Reaction Rates, Waves, Periodic Trends, and Plant Adaptations',
   'Grade 7 Science strand review: students revisit factors affecting reaction rate, transverse and longitudinal waves, periodic table families and trends, plant adaptations to extreme climates, and how the solar system formed.',
   [('What generally happens to a reaction rate when temperature is increased?', ['It generally increases', 'It always stays exactly the same', 'A concept unrelated to chemistry', 'It always decreases sharply'], 0),
    ('In a transverse wave, how do particles move relative to the direction of the wave?', ['At right angles, or perpendicular, to the direction of the wave', 'In exactly the same direction as the wave travels', 'A concept unrelated to waves', 'Particles never move at all in a transverse wave'], 0),
    ('What do elements within the same family, or group, of the periodic table generally share?', ['Similar chemical properties', 'Completely unrelated chemical properties', 'A concept unrelated to chemistry', 'Identical physical appearances with no exceptions'], 0),
    ('Why do many desert plants have thick, waxy leaves?', ['To reduce water loss in a dry climate', 'To attract as many insects as possible', 'A concept unrelated to biology', 'Thick waxy leaves have no connection to water conservation'], 0),
    ('What is the leading scientific explanation for how the solar system formed?', ['A giant, collapsing cloud of gas and dust gradually formed the sun and planets', 'The solar system has always existed exactly as it is today', 'A concept unrelated to how the solar system formed', 'A single planet split apart to create the sun and all other planets'], 0)]),
SS('Social Studies Review: Vimy Ridge, Railways, Currency, and Indigenous Rights',
   'Grade 7 Social Studies strand review: students revisit the Battle of Vimy Ridge, the creation of the Canadian National Railway, Canadian currency and the Royal Canadian Mint, the Metis Nation, and the Ontario Human Rights Code.',
   [('In what year did the Battle of Vimy Ridge take place?', ['1917', '1867', '1949', '1885'], 0),
    ('Why did the federal government create the Canadian National Railway?', ['To combine struggling private railways into one stable, publicly owned company', 'To eliminate all rail service across the country permanently', 'A concept unrelated to Canadian history', 'To sell Canadian rail lines to a foreign government'], 0),
    ('What is the main role of the Royal Canadian Mint?', ['Producing Canadas coins', 'Printing newspapers for the federal government', 'A concept unrelated to Canadian history', 'Regulating interprovincial trade agreements'], 0),
    ('Under which document did the Metis gain formal recognition as one of Canadas Aboriginal peoples?', ['The 1982 Constitution', 'The Halibut Treaty of 1923', 'A concept unrelated to the Metis Nation', 'The Statute of Westminster'], 0),
    ('What made the Ontario Human Rights Code significant in Canadian history?', ['It was the first law of its kind in Canada to combine various anti-discrimination protections into one code', 'It was the last province to introduce any human rights protections', 'A concept unrelated to Canadian history', 'It removed all existing anti-discrimination protections in Ontario'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_151_160)
    append_to(7, g7_151_160)
