#!/usr/bin/env python3
"""Grade 8, Days 101-110 -- extends Grade 8 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade8.json): round vs flat characters, the memoir, perfect and
progressive verb tenses, loanwords, product placement and branded content,
setting as a literary device, the feature article, coordinating
conjunctions and compound sentences, suspense and tension in narrative;
imaginary and complex numbers, graphing absolute value functions, set
theory (union/intersection/complement), the binomial theorem and Pascal's
Triangle, number bases (binary and hexadecimal), geometric series and
sigma notation, the pigeonhole principle, trigonometric identities, polar
coordinates; the circulatory system, population ecology and carrying
capacity, the ozone layer, taxonomy, cellular respiration, geothermal
energy, viruses versus bacteria, tides, renewable versus nonrenewable
resources; the Conscription Crisis of 1917, the Alaska Boundary Dispute,
the On-to-Ottawa Trek, the British Commonwealth Air Training Plan, the
Naval Service Act of 1910, the St. Lawrence Seaway, the Massey Commission,
the Bomarc Missile Crisis, and the Métis scrip system.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260927):
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


g8_101_110 = [
day(101, [
L('Reading: Analyzing Round and Flat Characters',
  'Grade 8 Language strand: a round character is complex and multidimensional with a fully developed personality, while a flat character is simple, one-dimensional, and often defined by a single trait or role.',
  [('What defines a round character?', ['A complex, multidimensional character with a fully developed personality', 'A character who never appears more than once', 'A concept unrelated to reading', 'A character with no name given in the text'], 0),
   ('Is a flat character usually simple and defined by a single trait?', ['Yes', 'No, flat characters are always the most complex in a story', 'A concept unrelated to flat characters', 'Flat characters never appear in any story'], 0),
   ('Which of these best describes a flat character in a story?', ['A minor character who serves a single function, like a store clerk with no personality explored', 'The most emotionally complex character in the entire story', 'A concept unrelated to characterization', 'A character whose thoughts are explored in great depth'], 0),
   ('Why might an author use flat characters for minor roles rather than developing them fully?', ['It keeps focus on the main characters while still moving the plot forward efficiently', 'Flat characters always confuse readers with no clear purpose', 'This concept has no connection to writing', 'Every character in a story must always be fully developed'], 0),
   ('Why is understanding the round/flat distinction useful when analyzing a novel’s cast of characters?', ['It helps readers see which characters are meant to feel true-to-life and which serve a simpler narrative purpose', 'This distinction never helps readers understand a story’s characters', 'This concept has no relevance to reading comprehension', 'All characters in every novel are always equally complex'], 0)]),
M('Introduction to Imaginary and Complex Numbers',
  'Grade 8 Math strand: an imaginary number is defined using i, where i squared equals negative one, and a complex number combines a real part with an imaginary part in the form a + bi.',
  [('What does i represent in the imaginary number system?', ['The square root of negative one', 'The square root of one', 'A concept unrelated to math', 'A number that is always equal to zero'], 0),
   ('Is a complex number written in the form a + bi?', ['Yes', 'No, complex numbers never combine a real and imaginary part', 'A concept unrelated to complex numbers', 'Complex numbers only ever contain real numbers'], 0),
   ('What is i squared?', ['-1', '1', '0', '2'], 0),
   ('Why were imaginary numbers introduced when working with square roots?', ['They allow mathematicians to define a square root for negative numbers, which have no real square root', 'Imaginary numbers were never actually needed for any mathematical purpose', 'This concept has no connection to algebra', 'Negative numbers always have a real, positive square root'], 0),
   ('Why might complex numbers be useful in fields like electrical engineering?', ['They can represent quantities with two components, such as magnitude and phase, in a single number', 'Complex numbers have no real-world applications of any kind', 'This concept has no relevance to math', 'Electrical engineers never use any form of advanced mathematics'], 0)]),
Sc('Science: The Circulatory System and Blood Flow',
   'Grade 8 Science strand: the circulatory system moves blood through the body using the heart as a pump, carrying oxygen and nutrients to cells through arteries, veins, and capillaries.',
   [('What organ pumps blood through the circulatory system?', ['The heart', 'The lungs', 'A concept unrelated to biology', 'The stomach'], 0),
    ('Do arteries generally carry blood away from the heart?', ['Yes', 'No, arteries never carry blood away from the heart', 'A concept unrelated to the circulatory system', 'Arteries only ever carry blood toward the lungs'], 0),
    ('Which blood vessels are the smallest and allow exchange of oxygen and nutrients with cells?', ['Capillaries', 'A concept unrelated to the circulatory system', 'Tendons', 'Bronchioles'], 0),
    ('Why is it important that capillaries have very thin walls?', ['Thin walls allow oxygen, nutrients, and waste to pass easily between blood and body cells', 'Thin walls never have any effect on how substances move in the body', 'This concept has no connection to biology', 'Capillary walls are always thicker than any other blood vessel'], 0),
    ('Why does the body need a continuous flow of blood to survive?', ['Cells constantly need a fresh supply of oxygen and nutrients and need waste removed', 'The body never actually needs blood to flow continuously', 'This concept has no relevance to science', 'Cells can survive indefinitely with no oxygen or nutrients at all'], 0)]),
H('The Conscription Crisis of 1917',
  'Grade 8 History strand: the Conscription Crisis of 1917 arose when Prime Minister Robert Borden’s government passed the Military Service Act to draft soldiers for World War I, sparking deep divisions between English and French Canada.',
  [('In what year did the Conscription Crisis take place?', ['1917', '1867', '1945', '1970'], 0),
   ('Did the Military Service Act introduce mandatory military service for World War I?', ['Yes', 'No, the Military Service Act had no connection to military service', 'A concept unrelated to the Conscription Crisis', 'The Military Service Act made military service illegal'], 0),
   ('Who was the Canadian Prime Minister during the Conscription Crisis?', ['Robert Borden', 'Wilfrid Laurier', 'A concept unrelated to Canadian history', 'John A. Macdonald'], 0),
   ('Why did conscription cause deep divisions between English and French Canada?', ['Many French Canadians felt less connected to a war fought primarily for British imperial interests and opposed being forced to fight', 'Conscription was equally popular in every region of Canada with no disagreement', 'This concept has no connection to Canadian history', 'French Canadians were never affected by the Military Service Act in any way'], 0),
   ('Why is the Conscription Crisis considered an important event in Canadian political history?', ['It revealed lasting regional and cultural tensions that shaped Canadian politics for decades afterward', 'The Conscription Crisis had no lasting effect on Canadian politics', 'This concept has no relevance to History', 'English and French Canada always agreed completely on every wartime policy'], 0)]),
]),

day(102, [
L('Writing: The Memoir',
  'Grade 8 Language strand: a memoir is a nonfiction narrative in which a writer recounts personal experiences and reflects on their meaning, typically focusing on a specific period, relationship, or theme rather than an entire life.',
  [('What is a memoir?', ['A nonfiction narrative in which a writer recounts personal experiences and reflects on their meaning', 'A fictional story with invented characters and events', 'A concept unrelated to writing', 'A set of instructions for completing a task'], 0),
   ('Does a memoir typically cover an entire life story from birth to the present?', ['No, a memoir usually focuses on a specific period, relationship, or theme', 'Yes, a memoir always covers an entire life from birth onward', 'A concept unrelated to memoirs', 'A memoir never focuses on any specific period or theme'], 0),
   ('Which of these is most memoir-like?', ['A writer reflecting on the summer they learned to sail', 'A textbook chapter about ocean currents', 'A concept unrelated to writing', 'A fictional tale about a dragon and a knight'], 0),
   ('Why might a memoirist include their own reflections and feelings about past events rather than just listing what happened?', ['Reflection helps readers understand the meaning and impact the experience had on the writer', 'Reflections never add any meaning to a piece of personal writing', 'This concept has no connection to writing', 'Memoirs should never include the writer’s own thoughts or feelings'], 0),
   ('Why might a memoir differ from a full autobiography?', ['A memoir zooms in on a particular theme or period rather than covering an entire life span', 'A memoir and an autobiography are always exactly identical in scope', 'This concept has no relevance to writing', 'An autobiography can never cover more than a single event'], 0)]),
M('Graphing Absolute Value Functions',
  'Grade 8 Math strand: the absolute value function f(x) = |x| produces a distinctive V-shaped graph, since it outputs the non-negative distance of x from zero regardless of the sign of the input.',
  [('What shape does the graph of f(x) = |x| produce?', ['A V shape', 'A straight diagonal line', 'A concept unrelated to functions', 'A perfect circle'], 0),
   ('Does the absolute value function always output a non-negative number?', ['Yes', 'No, absolute value can output a negative number', 'A concept unrelated to absolute value functions', 'Absolute value only ever outputs zero'], 0),
   ('What is the absolute value of -5?', ['5', '-5', '0', '10'], 0),
   ('Why does the graph of an absolute value function have a sharp corner at its vertex?', ['The function’s slope switches direction abruptly at the point where the expression inside equals zero', 'The graph of an absolute value function is always a smooth, unbroken curve with no corners', 'This concept has no connection to math', 'The vertex of an absolute value graph never has any special features'], 0),
   ('Why might absolute value be useful for describing real-world distances, like how far a value is from a target?', ['Distance is always non-negative, matching how absolute value strips away the sign of a number', 'Absolute value never has any connection to measuring distance', 'This concept has no relevance to math', 'Real-world distances are always expressed using negative numbers'], 0)]),
Sc('Science: Population Ecology and Carrying Capacity',
   'Grade 8 Science strand: carrying capacity is the maximum population size an environment can sustainably support given the availability of resources such as food, water, and space.',
   [('What is carrying capacity?', ['The maximum population size an environment can sustainably support', 'The total number of species found in an ecosystem', 'A concept unrelated to ecology', 'The average lifespan of an individual organism'], 0),
    ('Can limited resources like food and water affect an environment’s carrying capacity?', ['Yes', 'No, resources never have any effect on carrying capacity', 'A concept unrelated to carrying capacity', 'Carrying capacity is always exactly the same in every environment'], 0),
    ('What might happen if a population grows beyond its environment’s carrying capacity?', ['Resources become scarce and the population may decline', 'The population will continue growing forever with no limit', 'A concept unrelated to carrying capacity', 'The environment will automatically produce unlimited new resources'], 0),
    ('Why might a population’s growth rate slow down as it approaches carrying capacity?', ['Competition for limited resources increases, making survival and reproduction more difficult', 'Growth rate never changes as a population approaches carrying capacity', 'This concept has no connection to ecology', 'Populations always grow at exactly the same rate no matter the resources available'], 0),
    ('Why is understanding carrying capacity important for wildlife conservation?', ['It helps scientists predict how many individuals of a species an ecosystem can support long-term', 'Carrying capacity has no connection to wildlife conservation efforts', 'This concept has no relevance to science', 'Ecosystems can always support an unlimited number of any species'], 0)]),
H('The Alaska Boundary Dispute of 1903',
  'Grade 8 History strand: the Alaska Boundary Dispute of 1903 was a disagreement between Canada and the United States over the exact border of the Alaska Panhandle, ultimately settled by a tribunal in a decision seen as favouring American interests.',
  [('In what year was the Alaska Boundary Dispute settled?', ['1903', '1867', '1945', '1970'], 0),
   ('Was the dispute between Canada and the United States over the location of a border?', ['Yes', 'No, the dispute had no connection to any border', 'A concept unrelated to the Alaska Boundary Dispute', 'The dispute was between Canada and France instead'], 0),
   ('What geographic area was at the center of the dispute?', ['The Alaska Panhandle', 'The Prairies', 'A concept unrelated to the Alaska Boundary Dispute', 'Vancouver Island'], 0),
   ('Why did many Canadians view the tribunal’s decision as unfair to Canada?', ['A British representative sided with the American position, and Britain was seen as prioritizing its relationship with the United States over Canadian interests', 'The tribunal’s decision was universally seen as entirely fair to Canada', 'This concept has no connection to Canadian history', 'Canada was never involved in the tribunal’s decision-making process'], 0),
   ('Why is the Alaska Boundary Dispute considered significant in Canada’s path toward greater independence?', ['It made many Canadians question relying on Britain to represent Canadian interests in international disputes', 'The dispute had no lasting effect on how Canadians viewed Britain’s role', 'This concept has no relevance to History', 'Canada gained full control over its foreign policy immediately after this dispute'], 0)]),
]),

day(103, [
L('Grammar: Perfect and Progressive Verb Tenses',
  'Grade 8 Language strand: perfect tenses, such as had walked, show a completed action relative to another point in time, while progressive tenses, such as was walking, show an action in progress.',
  [('What does a perfect tense typically show?', ['A completed action relative to another point in time', 'An action that will never happen', 'A concept unrelated to grammar', 'A question rather than a statement'], 0),
   ('Does a progressive tense show an action that is or was in progress?', ['Yes', 'No, progressive tenses never show an ongoing action', 'A concept unrelated to progressive tenses', 'Progressive tenses only describe actions that have not started yet'], 0),
   ('Which sentence uses the present perfect tense?', ['She has finished her homework.', 'She finishes her homework.', 'She is finishing her homework.', 'She will finish her homework.'], 0),
   ('Why might a writer use the past perfect tense, such as had walked, when describing two past events?', ['It clarifies which of the two past events happened first', 'The past perfect tense never clarifies the order of past events', 'This concept has no connection to grammar', 'Past events can never be placed in any particular order using verb tense'], 0),
   ('Why is the progressive tense useful for showing an ongoing action?', ['It signals that an action was or is still happening rather than already complete', 'The progressive tense never indicates whether an action is ongoing', 'This concept has no relevance to grammar', 'Ongoing actions can only ever be described using the simple past tense'], 0)]),
M('Set Theory: Union, Intersection, and Complement',
  'Grade 8 Math strand: in set theory, the union of two sets combines all their elements, the intersection includes only elements common to both sets, and the complement includes elements not in a given set.',
  [('What does the union of two sets include?', ['All elements from both sets combined', 'Only elements found in neither set', 'A concept unrelated to math', 'Only elements found in exactly one set'], 0),
   ('Does the intersection of two sets include only elements common to both?', ['Yes', 'No, the intersection includes every element from both sets', 'A concept unrelated to set theory', 'The intersection is always an empty set'], 0),
   ('If Set A = {1,2,3} and Set B = {2,3,4}, what is the intersection of A and B?', ['{2,3}', '{1,2,3,4}', '{1,4}', '{}'], 0),
   ('Why might a Venn diagram be a useful tool for visualizing set operations like union and intersection?', ['It visually shows overlapping and non-overlapping regions between sets', 'Venn diagrams never help visualize any relationship between sets', 'This concept has no connection to math', 'Sets can never be represented using any kind of diagram'], 0),
   ('Why is understanding set notation useful when studying probability?', ['Probability often relies on describing outcomes as sets and analyzing how those sets overlap', 'Set notation has no connection to probability in any way', 'This concept has no relevance to math', 'Probability never involves grouping outcomes together in any way'], 0)]),
Sc('Science: The Ozone Layer and Atmospheric Protection',
   'Grade 8 Science strand: the ozone layer is a region of Earth’s stratosphere containing a high concentration of ozone molecules that absorbs most of the sun’s harmful ultraviolet radiation.',
   [('What does the ozone layer absorb?', ['Most of the sun’s harmful ultraviolet radiation', 'Most of Earth’s oxygen supply', 'A concept unrelated to earth science', 'All visible light from the sun'], 0),
    ('Is the ozone layer located in Earth’s stratosphere?', ['Yes', 'No, the ozone layer has no fixed location in the atmosphere', 'A concept unrelated to the ozone layer', 'The ozone layer is located deep underground'], 0),
    ('What human-made chemicals were found to significantly deplete the ozone layer?', ['Chlorofluorocarbons (CFCs)', 'A concept unrelated to the ozone layer', 'Table salt', 'Carbon monoxide only'], 0),
    ('Why was international action taken to phase out CFCs starting in the 1980s?', ['Scientists discovered CFCs were breaking down ozone molecules, thinning the protective layer', 'CFCs were found to have no effect on the ozone layer whatsoever', 'This concept has no connection to earth science', 'International cooperation on environmental issues never actually occurs'], 0),
    ('Why is protecting the ozone layer important for living things on Earth?', ['Excess ultraviolet radiation can increase risks like skin cancer and harm ecosystems', 'The ozone layer has no effect on the health of living things', 'This concept has no relevance to science', 'Ultraviolet radiation is always completely harmless to living organisms'], 0)]),
H('The On-to-Ottawa Trek of 1935',
  'Grade 8 History strand: the On-to-Ottawa Trek of 1935 was a protest march by unemployed men from federal relief camps who rode freight trains toward Ottawa to demand better wages and conditions during the Great Depression, ending in violence at the Regina Riot.',
  [('In what year did the On-to-Ottawa Trek take place?', ['1935', '1867', '1945', '1970'], 0),
   ('Were the participants of the trek primarily unemployed men from federal relief camps?', ['Yes', 'No, the trek was organized entirely by wealthy business owners', 'A concept unrelated to the On-to-Ottawa Trek', 'The trek had no connection to unemployment or relief camps'], 0),
   ('In which city did the trek come to a violent end?', ['Regina', 'Toronto', 'A concept unrelated to the On-to-Ottawa Trek', 'Halifax'], 0),
   ('Why were relief camp workers frustrated enough to organize the On-to-Ottawa Trek?', ['They faced low pay, poor conditions, and few opportunities during the Great Depression and wanted the government to address their concerns', 'Relief camp workers were completely satisfied with their pay and conditions', 'This concept has no connection to Canadian history', 'The Great Depression had no effect on relief camp workers at all'], 0),
   ('Why is the On-to-Ottawa Trek significant in understanding Canadian labour history?', ['It reflects the deep economic hardship of the Depression and how workers organized to demand change from the government', 'The trek had no lasting significance in Canadian labour history', 'This concept has no relevance to History', 'Workers during the Great Depression never organized to demand any changes'], 0)]),
]),

day(104, [
L('Vocabulary: Loanwords and Borrowed Terms',
  'Grade 8 Language strand: a loanword is a word borrowed from one language and adopted into another, often keeping much of its original spelling and meaning, such as café from French or tsunami from Japanese.',
  [('What is a loanword?', ['A word borrowed from one language and adopted into another', 'A word that only ever exists in one single language', 'A concept unrelated to vocabulary', 'A grammatical rule with no connection to words'], 0),
   ('Do loanwords often keep much of their original spelling?', ['Yes', 'No, loanwords always change their spelling completely', 'A concept unrelated to loanwords', 'Loanwords never retain any part of their original form'], 0),
   ('Which of these English words is a loanword from Japanese?', ['Tsunami', 'Table', 'Run', 'Happy'], 0),
   ('Why might English contain so many loanwords from other languages?', ['English has a long history of contact with other cultures through trade, exploration, and immigration', 'English has never had any contact with other languages or cultures', 'This concept has no connection to vocabulary', 'Loanwords are never actually adopted into the English language'], 0),
   ('Why is recognizing loanwords useful when studying vocabulary and etymology?', ['It helps explain irregular spelling and reveals connections between English and other languages', 'Recognizing loanwords never reveals any useful information about a language', 'This concept has no relevance to vocabulary', 'Etymology has no connection to how words are borrowed between languages'], 0)]),
M('The Binomial Theorem and Pascal’s Triangle',
  'Grade 8 Math strand: the binomial theorem provides a formula for expanding expressions like (a + b) raised to a power, and the coefficients in this expansion match the numbers found in Pascal’s Triangle.',
  [('What does the binomial theorem help you do?', ['Expand expressions like (a + b) raised to a power', 'Find the square root of a number', 'A concept unrelated to algebra', 'Simplify a fraction to lowest terms'], 0),
   ('Do the coefficients in a binomial expansion match the numbers in Pascal’s Triangle?', ['Yes', 'No, the two have no connection to each other', 'A concept unrelated to the binomial theorem', 'Pascal’s Triangle has no connection to any mathematical expansion'], 0),
   ('What are the numbers in the third row of Pascal’s Triangle, starting the top row as row 0?', ['1, 2, 1', '1, 3, 3, 1', '1, 1', '1'], 0),
   ('Why is each number in Pascal’s Triangle equal to the sum of the two numbers above it?', ['This pattern reflects how each expanded term combines contributions from the two terms in the row above', 'Pascal’s Triangle numbers are always chosen completely at random', 'This concept has no connection to algebra', 'The numbers in Pascal’s Triangle never follow any predictable pattern'], 0),
   ('Why might the binomial theorem be useful for expanding an expression like (x + y) to a high power without multiplying it out repeatedly?', ['It provides a direct formula for the coefficients and terms, saving significant repeated multiplication', 'The binomial theorem never helps with expanding any algebraic expression', 'This concept has no relevance to math', 'Expanding expressions to a high power can never be simplified using any formula'], 0)]),
Sc('Science: Classification of Living Things (Taxonomy)',
   'Grade 8 Science strand: taxonomy is the branch of science that classifies living things into hierarchical groups, such as kingdom, phylum, class, order, family, genus, and species, based on shared characteristics.',
   [('What is taxonomy?', ['The branch of science that classifies living things into hierarchical groups', 'The study of rocks and minerals', 'A concept unrelated to biology', 'The study of weather patterns'], 0),
    ('Is species considered the most specific level of classification in taxonomy?', ['Yes', 'No, species is always the broadest possible classification level', 'A concept unrelated to taxonomy', 'Species has no connection to how living things are classified'], 0),
    ('Which of these is the broadest taxonomic category listed?', ['Kingdom', 'Species', 'A concept unrelated to taxonomy', 'Genus'], 0),
    ('Why do scientists classify living things based on shared characteristics?', ['It organizes the diversity of life and reveals evolutionary relationships between organisms', 'Classifying living things never reveals any useful scientific information', 'This concept has no connection to biology', 'Living things are never grouped or organized in any systematic way'], 0),
    ('Why is a standardized classification system useful for scientists around the world?', ['It allows scientists from different countries and languages to consistently identify and refer to the same organism', 'A standardized classification system provides no benefit to scientists anywhere', 'This concept has no relevance to science', 'Scientists in different countries never need to communicate about the same organisms'], 0)]),
H('The British Commonwealth Air Training Plan',
  'Grade 8 History strand: the British Commonwealth Air Training Plan was a massive World War II program based mainly in Canada that trained tens of thousands of Allied pilots and aircrew from across the Commonwealth, earning Canada the nickname the aerodrome of democracy.',
  [('What did the British Commonwealth Air Training Plan train?', ['Allied pilots and aircrew', 'Naval submarine crews only', 'A concept unrelated to World War II', 'Farmers and factory workers'], 0),
   ('Was Canada the primary location for this training program during World War II?', ['Yes', 'No, this program was based entirely in Britain', 'A concept unrelated to the British Commonwealth Air Training Plan', 'This program was based entirely in Australia'], 0),
   ('What nickname did Canada earn for hosting this program?', ['The aerodrome of democracy', 'The workshop of the world', 'A concept unrelated to Canadian history', 'The breadbasket of the Commonwealth'], 0),
   ('Why might Canada have been chosen as the main location for this training program?', ['Its geography offered wide open spaces and relative safety from enemy attack compared to Britain', 'Canada was chosen for entirely random reasons with no strategic advantage', 'This concept has no connection to Canadian history', 'Britain had far more available land and safety than Canada during the war'], 0),
   ('Why is the British Commonwealth Air Training Plan considered an important Canadian contribution to World War II?', ['It provided crucial trained personnel for the Allied war effort in the air', 'This program had no real impact on the Allied war effort', 'This concept has no relevance to History', 'Air power played no significant role in World War II'], 0)]),
]),

day(105, [
L('Media Literacy: Analyzing Product Placement and Branded Content',
  'Grade 8 Language strand: product placement is the practice of featuring a brand or product within a movie, show, or video game in exchange for payment, often blending advertising subtly into entertainment.',
  [('What is product placement?', ['Featuring a brand or product within entertainment content in exchange for payment', 'A type of advertisement shown only between television programs', 'A concept unrelated to media literacy', 'A free product given away with no advertising purpose'], 0),
   ('Is product placement usually meant to blend subtly into entertainment rather than stand out as an obvious ad?', ['Yes', 'No, product placement is always presented as an obvious, separate advertisement', 'A concept unrelated to product placement', 'Product placement never appears within entertainment content'], 0),
   ('Which of these is an example of product placement?', ['A character in a movie visibly drinking a named brand of soda', 'A blank screen with no visual content at all', 'A concept unrelated to product placement', 'A news report with no mention of any brand'], 0),
   ('Why might companies pay for product placement instead of only using traditional commercials?', ['It can reach audiences in a way that feels less like an obvious advertisement', 'Companies never choose to use product placement for any reason', 'This concept has no connection to media literacy', 'Traditional commercials and product placement are always identical in effect'], 0),
   ('Why should viewers think critically about brands they see featured in their favourite shows or games?', ['Recognizing paid placement helps viewers understand it is a form of advertising, not a neutral choice', 'Brands shown in entertainment are never connected to any form of advertising', 'This concept has no relevance to media literacy', 'Viewers never need to consider why a specific brand appears on screen'], 0)]),
M('Introduction to Number Bases: Binary and Hexadecimal',
  'Grade 8 Math strand: a number base determines how many unique digits are used before a new place value begins, with binary (base 2) using only 0 and 1, and hexadecimal (base 16) using digits 0 to 9 and letters A to F.',
  [('How many unique digits does binary (base 2) use?', ['2', '10', '16', '8'], 0),
   ('Does hexadecimal use letters as well as numbers to represent digits?', ['Yes', 'No, hexadecimal only ever uses numbers, never letters', 'A concept unrelated to hexadecimal', 'Hexadecimal only ever uses a single digit'], 0),
   ('What is the binary number 101 equal to in base 10?', ['5', '3', '7', '10'], 0),
   ('Why is binary used as the foundation for how computers store and process information?', ['Binary’s two states, 0 and 1, correspond naturally to a circuit being off or on', 'Computers never actually use binary to store or process any information', 'This concept has no connection to math', 'Binary has no relationship to how electronic circuits function'], 0),
   ('Why might programmers use hexadecimal instead of binary when working with large values, like colour codes?', ['Hexadecimal represents the same values more compactly and is easier for people to read', 'Hexadecimal never provides any advantage over binary for representing values', 'This concept has no relevance to math', 'Binary is always more compact and readable than hexadecimal'], 0)]),
Sc('Science: Cellular Respiration and Energy Production',
   'Grade 8 Science strand: cellular respiration is the process by which cells break down glucose in the presence of oxygen to release usable energy, producing carbon dioxide and water as byproducts.',
   [('What does cellular respiration break down to release energy?', ['Glucose', 'Oxygen only, with nothing else involved', 'A concept unrelated to biology', 'Carbon dioxide'], 0),
    ('Does cellular respiration typically require oxygen?', ['Yes', 'No, cellular respiration never requires oxygen', 'A concept unrelated to cellular respiration', 'Oxygen has no connection to how cells produce energy'], 0),
    ('What are two byproducts of cellular respiration?', ['Carbon dioxide and water', 'Oxygen and glucose', 'A concept unrelated to cellular respiration', 'Nitrogen and salt'], 0),
    ('Why is cellular respiration often described as the opposite process of photosynthesis?', ['Photosynthesis uses carbon dioxide and water to store energy, while respiration releases that stored energy using oxygen', 'Cellular respiration and photosynthesis are always exactly identical processes', 'This concept has no connection to biology', 'Photosynthesis and cellular respiration never occur in any living organism'], 0),
    ('Why do cells need a constant supply of energy from cellular respiration?', ['Energy is required to power essential functions like growth, repair, and movement', 'Cells never actually require any energy to carry out their functions', 'This concept has no relevance to science', 'Cellular functions like growth and repair never require any energy'], 0)]),
H('The Naval Service Act of 1910 and the Creation of the Royal Canadian Navy',
  'Grade 8 History strand: the Naval Service Act of 1910, passed under Prime Minister Wilfrid Laurier, created the Royal Canadian Navy, sparking political controversy over whether Canada should build its own navy or contribute funds directly to Britain’s Royal Navy.',
  [('In what year was the Naval Service Act passed?', ['1910', '1867', '1945', '1970'], 0),
   ('Did the Naval Service Act create the Royal Canadian Navy?', ['Yes', 'No, this act had no connection to any Canadian navy', 'A concept unrelated to the Naval Service Act', 'This act actually disbanded an existing Canadian navy'], 0),
   ('Who was the Canadian Prime Minister when the Naval Service Act was passed?', ['Wilfrid Laurier', 'Robert Borden', 'A concept unrelated to Canadian history', 'John A. Macdonald'], 0),
   ('Why did the Naval Service Act spark political controversy in Canada?', ['Some Canadians wanted to directly fund Britain’s navy, while others wanted an independent Canadian navy, reflecting differing views on ties to Britain', 'The Naval Service Act was supported unanimously with no disagreement at all', 'This concept has no connection to Canadian history', 'Canadians had no opinions at all about naval policy in this period'], 0),
   ('Why is the creation of the Royal Canadian Navy considered a step in Canada’s development as an independent nation?', ['It showed Canada beginning to take responsibility for its own defence rather than relying entirely on Britain', 'The creation of the Royal Canadian Navy had no connection to Canadian independence', 'This concept has no relevance to History', 'Canada’s defence policy never changed as a result of this act'], 0)]),
]),

day(106, [
L('Reading: Analyzing Setting as a Literary Device',
  'Grade 8 Language strand: setting is the time and place in which a story occurs, and skilled authors use setting to establish mood, reflect a character’s emotional state, or influence the plot.',
  [('What does setting refer to in a story?', ['The time and place in which a story occurs', 'The main character’s personality traits', 'A concept unrelated to reading', 'The title and author of a story'], 0),
   ('Can setting help establish a story’s mood?', ['Yes', 'No, setting never has any effect on a story’s mood', 'A concept unrelated to setting', 'Mood is never connected to time or place in a story'], 0),
   ('Which best shows setting influencing mood?', ['A dark, stormy night making a scene feel tense', 'A character’s name being mentioned once', 'A concept unrelated to setting', 'A list of ingredients in a recipe'], 0),
   ('Why might an author choose to set a story in a specific historical period?', ['The time period can shape characters’ choices, conflicts, and worldview in ways that feel authentic', 'A story’s historical period never has any effect on its characters or plot', 'This concept has no connection to writing', 'Historical periods are always interchangeable with no effect on a story'], 0),
   ('Why is analyzing setting useful when interpreting a story’s larger themes?', ['Setting often reflects or reinforces the ideas and emotions the author wants readers to notice', 'Setting never connects to a story’s larger themes in any way', 'This concept has no relevance to reading comprehension', 'Themes in a story are always completely unrelated to where or when it takes place'], 0)]),
M('Geometric Series and Sigma Notation',
  'Grade 8 Math strand: a geometric series is the sum of terms in a geometric sequence, where each term is found by multiplying the previous term by a constant ratio, and sigma notation provides a compact way to write such sums.',
  [('In a geometric series, how is each term related to the one before it?', ['It is multiplied by a constant ratio', 'It is always added to a fixed constant', 'A concept unrelated to math', 'It is always divided by zero'], 0),
   ('Does sigma notation provide a compact way to write a sum of terms?', ['Yes', 'No, sigma notation has no connection to writing sums', 'A concept unrelated to sigma notation', 'Sigma notation can only ever represent a single term'], 0),
   ('What is the sum of the geometric series 1 + 2 + 4 + 8?', ['15', '14', '16', '8'], 0),
   ('Why is knowing the common ratio important for finding the sum of a geometric series?', ['The ratio determines how quickly the terms grow or shrink, which affects the total sum', 'The common ratio never has any effect on the sum of a geometric series', 'This concept has no connection to math', 'Geometric series never actually have a common ratio between terms'], 0),
   ('Why might sigma notation be useful when working with a series that has many terms?', ['It compactly expresses the pattern and range of a sum without writing out every individual term', 'Sigma notation never simplifies how a sum of terms is written', 'This concept has no relevance to math', 'Every term in a long series must always be written out individually'], 0)]),
Sc('Science: Geothermal Energy and Earth’s Heat',
   'Grade 8 Science strand: geothermal energy is heat generated within the Earth, primarily from the decay of radioactive elements, that can be harnessed as a renewable energy source in regions with accessible heat sources.',
   [('Where does most of Earth’s internal geothermal heat come from?', ['The decay of radioactive elements', 'Sunlight absorbed by the oceans', 'A concept unrelated to earth science', 'Wind currents in the atmosphere'], 0),
    ('Is geothermal energy considered a renewable energy source?', ['Yes', 'No, geothermal energy is always classified as nonrenewable', 'A concept unrelated to geothermal energy', 'Geothermal energy has no connection to renewable energy at all'], 0),
    ('Which of these best describes how geothermal power plants generate electricity?', ['They use heat from within the Earth, often via steam, to turn turbines', 'They burn coal to generate steam for turbines', 'A concept unrelated to geothermal energy', 'They rely entirely on sunlight to generate electricity'], 0),
    ('Why is geothermal energy more accessible in some regions, like areas near tectonic plate boundaries, than others?', ['Heat from the Earth’s interior is closer to the surface in these geologically active regions', 'Geothermal heat is always exactly the same distance from the surface everywhere on Earth', 'This concept has no connection to earth science', 'Tectonic plate boundaries have no connection to the availability of geothermal heat'], 0),
    ('Why might geothermal energy be considered a more reliable renewable source than solar or wind in some cases?', ['Earth’s internal heat is available continuously, regardless of weather or time of day', 'Geothermal energy is never available on a continuous basis', 'This concept has no relevance to science', 'Solar and wind energy are always more reliable than any other renewable source'], 0)]),
H('The St. Lawrence Seaway',
  'Grade 8 History strand: the St. Lawrence Seaway, completed in 1959 through a joint Canada-United States effort, is a system of canals and locks that allows ocean-going ships to travel from the Atlantic Ocean into the Great Lakes.',
  [('In what year was the St. Lawrence Seaway completed?', ['1959', '1867', '1945', '1970'], 0),
   ('Was the St. Lawrence Seaway built through a joint effort between Canada and the United States?', ['Yes', 'No, the Seaway was built entirely by Canada alone', 'A concept unrelated to the St. Lawrence Seaway', 'The Seaway was built entirely by the United States alone'], 0),
   ('What does the St. Lawrence Seaway allow ocean-going ships to reach?', ['The Great Lakes', 'The Arctic Ocean', 'A concept unrelated to the St. Lawrence Seaway', 'The Pacific Ocean'], 0),
   ('Why was building a system of canals and locks necessary to connect the Atlantic Ocean to the Great Lakes?', ['Natural obstacles like rapids and differences in water level needed to be overcome for large ships to pass through', 'No natural obstacles existed between the Atlantic Ocean and the Great Lakes', 'This concept has no connection to Canadian history', 'Ships could already travel this route freely with no assistance before the Seaway was built'], 0),
   ('Why is the St. Lawrence Seaway considered economically significant for both Canada and the United States?', ['It opened a major shipping route that allows goods to move efficiently between inland industrial regions and international markets', 'The Seaway had no lasting economic significance for either country', 'This concept has no relevance to History', 'Goods have never been transported between Canada and the United States by ship'], 0)]),
]),

day(107, [
L('Writing: The Feature Article',
  'Grade 8 Language strand: a feature article is a piece of journalistic writing that explores a topic, person, or event in greater depth and with more creative style than a straightforward news report.',
  [('What does a feature article do?', ['Explores a topic, person, or event in greater depth than a straightforward news report', 'Reports only the most basic facts of a breaking event', 'A concept unrelated to writing', 'Lists a set of unrelated numerical statistics'], 0),
   ('Does a feature article typically use more creative style than a hard news report?', ['Yes', 'No, a feature article always uses the exact same style as a hard news report', 'A concept unrelated to feature articles', 'Feature articles are never written with any creative style'], 0),
   ('Which of these topics would suit a feature article?', ['An in-depth profile of a local community volunteer', 'A single sentence announcing a road closure', 'A concept unrelated to writing', 'A blank page with no written content'], 0),
   ('Why might a feature article include quotes, anecdotes, and descriptive details?', ['These elements help engage readers and bring the subject to life', 'Quotes and anecdotes never add anything meaningful to an article', 'This concept has no connection to writing', 'Feature articles should never include any descriptive details'], 0),
   ('Why is a feature article usually less time-sensitive than breaking news?', ['It focuses on depth and human interest rather than reporting the latest fast-moving events', 'Feature articles are always exactly as time-sensitive as breaking news', 'This concept has no relevance to writing', 'Breaking news stories are never time-sensitive in any way'], 0)]),
M('The Pigeonhole Principle',
  'Grade 8 Math strand: the pigeonhole principle states that if more items are placed into containers than there are containers, at least one container must hold more than one item, a simple idea used to prove certain outcomes must occur.',
  [('What does the pigeonhole principle state?', ['If more items are placed into containers than there are containers, at least one container holds more than one item', 'Every container must always hold the exact same number of items', 'A concept unrelated to math', 'Items can never be placed into more than one container'], 0),
   ('Can the pigeonhole principle be used to prove that a certain outcome must occur?', ['Yes', 'No, the pigeonhole principle can never be used to prove anything', 'A concept unrelated to the pigeonhole principle', 'The pigeonhole principle only applies to physical pigeons'], 0),
   ('If 13 people are in a room, how many of them must share the same birth month?', ['At least 2', 'At least 13', 'A concept unrelated to the pigeonhole principle', 'None of them, since sharing a month is impossible'], 0),
   ('Why does the pigeonhole principle guarantee that two people in a group of 13 must share a birth month?', ['There are only 12 months, so with 13 people at least one month must be repeated', 'There are more than 13 months in a year, so no repeats are guaranteed', 'This concept has no connection to math', 'Birth months are never something that can repeat among a group of people'], 0),
   ('Why is the pigeonhole principle a useful tool in mathematical proofs even though it seems like a simple idea?', ['It can prove that a certain outcome is guaranteed without needing to check every possible case individually', 'The pigeonhole principle never actually helps prove anything in mathematics', 'This concept has no relevance to math', 'Every possible case must always be checked individually with no shortcuts'], 0)]),
Sc('Science: Viruses versus Bacteria',
   'Grade 8 Science strand: bacteria are single-celled living organisms that can reproduce independently, while viruses are not made of cells and can only reproduce by infecting and hijacking a host organism’s cells.',
   [('Are bacteria made up of a single cell?', ['Yes', 'No, bacteria are always made up of many cells', 'A concept unrelated to biology', 'Bacteria are never considered living organisms'], 0),
    ('Can viruses reproduce on their own without a host cell?', ['No', 'Yes, viruses can always reproduce completely independently', 'A concept unrelated to viruses', 'Viruses never reproduce in any way, even with a host'], 0),
    ('Which of these can be treated effectively with antibiotics?', ['Bacterial infections', 'Viral infections', 'A concept unrelated to biology', 'Neither bacterial nor viral infections'], 0),
    ('Why are antibiotics generally ineffective against viral infections?', ['Antibiotics target processes found in living bacterial cells, which viruses do not have', 'Antibiotics are always equally effective against both bacteria and viruses', 'This concept has no connection to biology', 'Viral infections never actually require any kind of medical treatment'], 0),
    ('Why do scientists classify viruses differently from bacteria despite both being able to cause disease?', ['Viruses lack cellular structure and cannot carry out life processes independently the way bacteria can', 'Viruses and bacteria are always classified as exactly the same type of organism', 'This concept has no relevance to science', 'Bacteria are never able to cause any kind of disease'], 0)]),
H('The Massey Commission and Canadian Culture',
  'Grade 8 History strand: the Massey Commission, held from 1949 to 1951, studied the state of arts, letters, and sciences in Canada, leading to recommendations that strengthened Canadian cultural institutions, including the eventual creation of the Canada Council for the Arts.',
  [('In what years did the Massey Commission take place?', ['1949 to 1951', '1867 to 1870', '1939 to 1945', '1980 to 1985'], 0),
   ('Did the Massey Commission study the state of Canadian arts and culture?', ['Yes', 'No, the Commission focused entirely on Canadian agriculture', 'A concept unrelated to the Massey Commission', 'The Commission had no connection to arts or culture at all'], 0),
   ('What later institution was created partly as a result of the Massey Commission’s recommendations?', ['The Canada Council for the Arts', 'The Royal Canadian Navy', 'A concept unrelated to the Massey Commission', 'The Supreme Court of Canada'], 0),
   ('Why might the Massey Commission have been concerned about American cultural influence on Canada?', ['Officials worried that Canadian culture and identity could be overshadowed without support for homegrown arts and media', 'American culture was never seen as having any influence on Canada', 'This concept has no connection to Canadian history', 'The Massey Commission had no concerns about culture or identity of any kind'], 0),
   ('Why is the Massey Commission considered significant in Canadian cultural history?', ['It helped establish long-term government support for the arts, shaping Canadian cultural institutions for decades afterward', 'The Massey Commission had no lasting effect on Canadian cultural institutions', 'This concept has no relevance to History', 'Government support for the arts in Canada began long before the Massey Commission and was unrelated to it'], 0)]),
]),

day(108, [
L('Grammar: Coordinating Conjunctions and Compound Sentences',
  'Grade 8 Language strand: coordinating conjunctions, such as for, and, nor, but, or, yet, and so, join two independent clauses of equal importance to form a compound sentence.',
  [('What do coordinating conjunctions join?', ['Two independent clauses of equal importance', 'A single word with no other words attached', 'A concept unrelated to grammar', 'Only questions, never statements'], 0),
   ('Is but an example of a coordinating conjunction?', ['Yes', 'No, but is never considered a coordinating conjunction', 'A concept unrelated to coordinating conjunctions', 'But can only ever appear at the very start of a sentence'], 0),
   ('Which sentence is a compound sentence?', ['I wanted to go outside, but it started raining.', 'I wanted to go outside.', 'Raining outside started it.', 'Outside, raining, wanted, I.'], 0),
   ('Why is a comma usually placed before a coordinating conjunction that joins two independent clauses?', ['It signals the boundary between two complete ideas being joined together', 'Commas are never used near coordinating conjunctions', 'This concept has no connection to grammar', 'Coordinating conjunctions never join two complete ideas together'], 0),
   ('Why might a writer combine two short sentences into one compound sentence?', ['It can improve sentence flow and show a clearer relationship between the two ideas', 'Combining sentences never improves the flow or clarity of writing', 'This concept has no connection to grammar', 'Short sentences should never be combined for any reason'], 0)]),
M('Introduction to Trigonometric Identities',
  'Grade 8 Math strand: a trigonometric identity is an equation involving trigonometric ratios that holds true for all valid angle values, such as the Pythagorean identity, sine squared theta plus cosine squared theta equals one.',
  [('What is a trigonometric identity?', ['An equation involving trigonometric ratios that holds true for all valid angle values', 'An equation that is only true for a single specific angle', 'A concept unrelated to math', 'A formula used only for measuring area'], 0),
   ('Does the Pythagorean identity state that sine squared theta plus cosine squared theta equals one?', ['Yes', 'No, this identity has no connection to sine or cosine', 'A concept unrelated to trigonometric identities', 'This identity states that the result always equals zero'], 0),
   ('Which formula represents the Pythagorean identity?', ['sin squared theta + cos squared theta = 1', 'sin theta + cos theta = 0', 'A concept unrelated to trigonometric identities', 'sin theta times cos theta = 1'], 0),
   ('Why is the Pythagorean identity called by that name?', ['It comes directly from applying the Pythagorean theorem to a right triangle inside the unit circle', 'The identity has no connection to the Pythagorean theorem at all', 'This concept has no connection to math', 'The Pythagorean theorem and this identity were developed completely independently with no link'], 0),
   ('Why are trigonometric identities useful for simplifying complex trigonometric expressions?', ['They allow one trigonometric expression to be rewritten as an equivalent, often simpler, expression', 'Trigonometric identities never help simplify any kind of expression', 'This concept has no relevance to math', 'Complex trigonometric expressions can never be rewritten in any other form'], 0)]),
Sc('Science: Tides and the Moon’s Gravitational Pull',
   'Grade 8 Science strand: tides are the regular rise and fall of ocean water levels caused primarily by the gravitational pull of the Moon, and to a lesser extent the Sun, on Earth’s oceans.',
   [('What is the primary cause of ocean tides?', ['The gravitational pull of the Moon', 'The rotation of Earth’s core', 'A concept unrelated to earth science', 'Wind patterns over the ocean surface'], 0),
    ('Does the Sun also have some influence on Earth’s tides?', ['Yes', 'No, the Sun has absolutely no effect on tides', 'A concept unrelated to tides', 'The Sun is the only factor that ever affects tides'], 0),
    ('What term describes especially high tides that occur when the Sun, Moon, and Earth are aligned?', ['Spring tides', 'Neap tides', 'A concept unrelated to tides', 'Summer tides'], 0),
    ('Why do most coastal areas experience two high tides and two low tides each day?', ['Earth’s rotation moves different points through the two tidal bulges created by the Moon’s gravity', 'Tides never actually follow any predictable daily pattern', 'This concept has no connection to earth science', 'Earth’s rotation has no connection to how tides occur'], 0),
    ('Why is understanding tidal patterns important for activities like navigation and coastal ecosystems?', ['Predictable tide timing and height affect boat travel safety and the habitats of many coastal organisms', 'Tidal patterns never have any effect on navigation or coastal ecosystems', 'This concept has no relevance to science', 'Coastal organisms are never affected by changes in tide levels'], 0)]),
H('The Bomarc Missile Crisis and Cold War Defence',
  'Grade 8 History strand: the Bomarc Missile Crisis of the early 1960s was a Cold War controversy over whether Canada should accept American nuclear warheads for the Bomarc missiles installed on Canadian soil, a dispute that contributed to the fall of Prime Minister John Diefenbaker’s government.',
  [('What Cold War weapon system was at the center of the Bomarc Missile Crisis?', ['Nuclear-armed Bomarc missiles', 'Long-range naval submarines', 'A concept unrelated to the Bomarc Missile Crisis', 'Conventional artillery cannons'], 0),
   ('Was this crisis connected to whether Canada should accept nuclear warheads from the United States?', ['Yes', 'No, the crisis had no connection to nuclear weapons at all', 'A concept unrelated to the Bomarc Missile Crisis', 'The crisis was about accepting warheads from the Soviet Union instead'], 0),
   ('Which Canadian Prime Minister’s government was significantly affected by this crisis?', ['John Diefenbaker', 'Wilfrid Laurier', 'A concept unrelated to Canadian history', 'Robert Borden'], 0),
   ('Why did the Bomarc Missile Crisis create political controversy in Canada?', ['Canadians were divided over whether accepting nuclear weapons aligned with Canada’s values and independent foreign policy', 'All Canadians agreed completely on how to handle the missile crisis', 'This concept has no connection to Canadian history', 'Nuclear weapons were never a topic of discussion in Canada during the Cold War'], 0),
   ('Why is the Bomarc Missile Crisis considered an important Cold War era event in Canadian history?', ['It highlighted the tension between Canada’s alliance commitments and a desire to maintain independent control over decisions like nuclear weapons', 'The crisis had no lasting significance for Canada’s Cold War history', 'This concept has no relevance to History', 'Canada’s alliance commitments were never affected by any Cold War era decisions'], 0)]),
]),

day(109, [
L('Reading: Analyzing Suspense and Tension in Narrative',
  'Grade 8 Language strand: suspense is a feeling of anticipation or uncertainty that authors build through pacing, foreshadowing, and withheld information to keep readers emotionally invested in what happens next.',
  [('What is suspense?', ['A feeling of anticipation or uncertainty', 'A summary of a story’s main events', 'A concept unrelated to reading', 'A type of punctuation mark'], 0),
   ('Can withholding information from readers help build suspense?', ['Yes', 'No, withholding information never has any effect on suspense', 'A concept unrelated to suspense', 'Suspense can only ever be created by revealing every detail immediately'], 0),
   ('Which technique might an author use to build suspense?', ['Ending a chapter right before a major event is revealed', 'Explaining the entire ending in the first paragraph', 'A concept unrelated to suspense', 'Listing every character’s name in alphabetical order'], 0),
   ('Why might an author slow down the pacing right before a climactic moment?', ['Slower pacing can heighten tension and anticipation before a big reveal', 'Pacing never has any effect on how tense a scene feels', 'This concept has no connection to writing', 'Climactic moments are always paced exactly the same as the rest of a story'], 0),
   ('Why is suspense an effective tool for keeping readers engaged in a story?', ['It creates emotional investment by making readers want to know what happens next', 'Suspense never has any effect on how engaged a reader feels', 'This concept has no relevance to reading comprehension', 'Readers are always equally engaged no matter how a story is paced'], 0)]),
M('Introduction to Polar Coordinates',
  'Grade 8 Math strand: polar coordinates describe a point’s location using a distance from the origin, r, and an angle, theta, measured from a fixed direction, offering an alternative to the Cartesian (x, y) coordinate system.',
  [('What two values describe a point in polar coordinates?', ['A distance from the origin and an angle', 'Two separate distances with no angle involved', 'A concept unrelated to math', 'A single number with no other information'], 0),
   ('Is the Cartesian (x, y) system an alternative way to describe the same points as polar coordinates?', ['Yes', 'No, Cartesian coordinates and polar coordinates describe entirely different points', 'A concept unrelated to polar coordinates', 'The Cartesian system has no connection to describing location at all'], 0),
   ('In polar coordinates, what does r represent?', ['The distance from the origin', 'The angle from a fixed direction', 'A concept unrelated to polar coordinates', 'The total area of a circle'], 0),
   ('Why might polar coordinates be more convenient than Cartesian coordinates for describing circular motion?', ['Circular paths can be described simply using a constant radius and a changing angle', 'Polar coordinates never offer any advantage when describing circular motion', 'This concept has no connection to math', 'Circular motion can never be described using any coordinate system'], 0),
   ('Why is the angle, theta, an essential part of identifying a point’s location in polar coordinates?', ['Without a specified direction, a distance alone cannot pinpoint a unique location around the origin', 'The angle never has any effect on identifying a point’s location', 'This concept has no relevance to math', 'A distance alone is always sufficient to identify a unique point in polar coordinates'], 0)]),
Sc('Science: Renewable versus Nonrenewable Resources',
   'Grade 8 Science strand: renewable resources, such as solar and wind energy, can naturally replenish over a short time, while nonrenewable resources, such as coal and oil, take millions of years to form and exist in limited supply.',
   [('What defines a renewable resource?', ['A resource that can naturally replenish over a short time', 'A resource that takes millions of years to form', 'A concept unrelated to science', 'A resource that never occurs naturally on Earth'], 0),
    ('Do nonrenewable resources take millions of years to form?', ['Yes', 'No, nonrenewable resources form again within a few days', 'A concept unrelated to nonrenewable resources', 'Nonrenewable resources are never actually formed by any natural process'], 0),
    ('Which of these is a nonrenewable resource?', ['Coal', 'Sunlight', 'A concept unrelated to natural resources', 'Wind'], 0),
    ('Why are fossil fuels like oil and natural gas considered nonrenewable?', ['They form over millions of years from ancient organic material and are being used far faster than they can regenerate', 'Fossil fuels are actually replenished within a single human lifetime', 'This concept has no connection to earth science', 'Fossil fuels are classified as renewable resources, not nonrenewable ones'], 0),
    ('Why might a society choose to invest in renewable energy sources over the long term?', ['Renewable sources can supply energy indefinitely without depleting a limited natural supply', 'Renewable energy sources always run out faster than nonrenewable ones', 'This concept has no relevance to science', 'There is never any advantage to using a renewable energy source'], 0)]),
H('The Métis Scrip System and Land Grants',
  'Grade 8 History strand: the Métis scrip system was a government program following the Manitoba Act that was intended to grant Métis people land or money in recognition of their claims, but was often implemented in ways that left many Métis without land, fuelling ongoing grievances.',
  [('What was Métis scrip intended to grant recipients?', ['Land or money in recognition of their claims', 'Free university education', 'A concept unrelated to the Métis scrip system', 'Government jobs with no other benefits'], 0),
   ('Did the scrip system often fail to actually secure land for many Métis people?', ['Yes', 'No, the scrip system always successfully secured land for every recipient', 'A concept unrelated to the Métis scrip system', 'The scrip system had no connection to land at all'], 0),
   ('What earlier legislation was the scrip system connected to?', ['The Manitoba Act', 'The Naval Service Act', 'A concept unrelated to the Métis scrip system', 'The Indian Act'], 0),
   ('Why did many Métis end up losing access to land despite the scrip system?', ['Scrip was often difficult to redeem for actual land, and many recipients were pressured into selling their scrip to speculators for far less than its value', 'Every Métis scrip recipient successfully kept their land with no issues', 'This concept has no connection to Canadian history', 'Speculators never had any involvement in the scrip system'], 0),
   ('Why is the Métis scrip system considered an important and troubling part of Canadian history to study?', ['It shows how a policy intended to address Métis claims often failed to provide lasting benefit and contributed to long-term grievances', 'The scrip system had no lasting effect on Métis communities', 'This concept has no relevance to History', 'The scrip system is considered one of the most successful land policies in Canadian history'], 0)]),
]),

day(110, [
L('Review: Language Arts and Grammar (Days 101-109)',
  'Grade 8 Language strand review: students revisit round and flat characters, the memoir, perfect and progressive verb tenses, loanwords, product placement, setting as a literary device, the feature article, coordinating conjunctions, and suspense.',
  [('What defines a round character?', ['A complex, multidimensional character with a fully developed personality', 'A character who never appears more than once', 'A concept unrelated to reading', 'A character with no name given in the text'], 0),
   ('What is a memoir?', ['A nonfiction narrative in which a writer recounts personal experiences and reflects on their meaning', 'A fictional story with invented characters and events', 'A concept unrelated to writing', 'A set of instructions for completing a task'], 0),
   ('What is a loanword?', ['A word borrowed from one language and adopted into another', 'A word that only ever exists in one single language', 'A concept unrelated to vocabulary', 'A grammatical rule with no connection to words'], 0),
   ('What does setting refer to in a story?', ['The time and place in which a story occurs', 'The main character’s personality traits', 'A concept unrelated to reading', 'The title and author of a story'], 0),
   ('What is suspense?', ['A feeling of anticipation or uncertainty', 'A summary of a story’s main events', 'A concept unrelated to reading', 'A type of punctuation mark'], 0)]),
M('Review: Advanced Numbers, Algebra, and Geometry (Days 101-109)',
  'Grade 8 Math strand review: students revisit imaginary and complex numbers, absolute value functions, set theory, the binomial theorem, number bases, geometric series, the pigeonhole principle, trigonometric identities, and polar coordinates.',
  [('What does i represent in the imaginary number system?', ['The square root of negative one', 'The square root of one', 'A concept unrelated to math', 'A number that is always equal to zero'], 0),
   ('What shape does the graph of f(x) = |x| produce?', ['A V shape', 'A straight diagonal line', 'A concept unrelated to functions', 'A perfect circle'], 0),
   ('What does the union of two sets include?', ['All elements from both sets combined', 'Only elements found in neither set', 'A concept unrelated to math', 'Only elements found in exactly one set'], 0),
   ('How many unique digits does binary (base 2) use?', ['2', '10', '16', '8'], 0),
   ('What two values describe a point in polar coordinates?', ['A distance from the origin and an angle', 'Two separate distances with no angle involved', 'A concept unrelated to math', 'A single number with no other information'], 0)]),
Sc('Review: Human Biology, Ecology, and Earth Science (Days 101-109)',
   'Grade 8 Science strand review: students revisit the circulatory system, carrying capacity, the ozone layer, taxonomy, cellular respiration, geothermal energy, viruses versus bacteria, tides, and renewable versus nonrenewable resources.',
   [('What organ pumps blood through the circulatory system?', ['The heart', 'The lungs', 'A concept unrelated to biology', 'The stomach'], 0),
    ('What is carrying capacity?', ['The maximum population size an environment can sustainably support', 'The total number of species found in an ecosystem', 'A concept unrelated to ecology', 'The average lifespan of an individual organism'], 0),
    ('What is taxonomy?', ['The branch of science that classifies living things into hierarchical groups', 'The study of rocks and minerals', 'A concept unrelated to biology', 'The study of weather patterns'], 0),
    ('What is the primary cause of ocean tides?', ['The gravitational pull of the Moon', 'The rotation of Earth’s core', 'A concept unrelated to earth science', 'Wind patterns over the ocean surface'], 0),
    ('What defines a renewable resource?', ['A resource that can naturally replenish over a short time', 'A resource that takes millions of years to form', 'A concept unrelated to science', 'A resource that never occurs naturally on Earth'], 0)]),
H('Review: Canadian History and Government (Days 101-109)',
  'Grade 8 History strand review: students revisit the Conscription Crisis, the Alaska Boundary Dispute, the On-to-Ottawa Trek, the British Commonwealth Air Training Plan, the Naval Service Act, the St. Lawrence Seaway, the Massey Commission, the Bomarc Missile Crisis, and the Métis scrip system.',
  [('In what year did the Conscription Crisis take place?', ['1917', '1867', '1945', '1970'], 0),
   ('In what year was the Alaska Boundary Dispute settled?', ['1903', '1867', '1945', '1970'], 0),
   ('In what year did the On-to-Ottawa Trek take place?', ['1935', '1867', '1945', '1970'], 0),
   ('In what year was the St. Lawrence Seaway completed?', ['1959', '1867', '1945', '1970'], 0),
   ('What was Métis scrip intended to grant recipients?', ['Land or money in recognition of their claims', 'Free university education', 'A concept unrelated to the Métis scrip system', 'Government jobs with no other benefits'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_101_110)
    append_to(8, g8_101_110)
