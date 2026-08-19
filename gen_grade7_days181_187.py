#!/usr/bin/env python3
"""Grade 7, Days 181-187 -- final batch, extending Grade 7 from 180 to 187
days, completing the full 187-day Ontario curriculum target for this grade.
Topics chosen after dumping the full (subject, title) list for Days 1-180
from data/grade7.json (720 (subject, title) pairs, zero duplicates) and
grepping every candidate title/keyword below against that dump to confirm
zero overlap, since Grade 7's earlier 180 days already cover an extremely
exhaustive range of subject matter across all four subjects.

This batch is only 7 days (not the usual 10), since 180 + 7 = 187, the
full-year target: 6 new content days (181-186, one new topic per subject
per day) plus Day 187, a final cross-subject review day.

Fresh, non-duplicate topics picked this batch:
Language: prepositional phrases as adjectives and adverbs, contronyms
(words that are their own opposite), analyzing setup and payoff in plot
(Chekhovs Gun), writing a choose your own adventure story, analyzing
documentary filmmaking techniques, capitalization rules for titles and
proper nouns.
Math: the area and circumference of sectors of a circle, the Fibonacci
sequence and patterns in nature, solving age and number word problems,
comparing renting and buying a home, classifying polyhedra by faces,
edges, and vertices (Eulers formula), constructing and interpreting
radar charts.
Science: renewable energy storage and grid-scale batteries, pollinator
decline and colony collapse disorder, deltas, estuaries, and river mouth
ecosystems, how refrigerators and heat pumps move heat, how wastewater
treatment plants clean water, how sunscreen works to block UV radiation.
SocialStudies: the Franklin Expedition and nineteenth-century Arctic
exploration, Terry Fox and the Marathon of Hope, the Alberta oil sands
and Canadas energy economy, the Atlantic cod moratorium and its impact
on Newfoundland, Expo 86 and Vancouvers growth as a Pacific gateway
city, Inuit traditional knowledge and life in the Arctic.

None of these titles or underlying topics duplicate anything appearing in
Days 1-180 of data/grade7.json (verified both by reading the full title
dump and by grepping every candidate title keyword against it before
writing this file). Day 187 is the final cross-subject review day of the
entire 187-day Grade 7 curriculum, drawing quiz content from Days 181-186
of this batch, with review titles ("Capstone Review") kept textually
distinct from every earlier review day (including Day 180's four review
titles and all earlier "(Days NN-NN)" review titles), while following the
exact mechanical review-day format used in every prior batch. Since this
is the very last day of the entire K-12 curriculum build for Grade 7, the
Day 187 review summaries acknowledge this is a capstone/end-of-program
review closing out the full 187-day Grade 7 curriculum.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are dropped entirely, matching the convention established in
gen_grade7_days111_120.py through gen_grade7_days171_180.py (e.g.
"Canadas" not "Canada's", "Chekhovs" not "Chekhov's").

Usage:
  cd ~/gradesbooster && python3 gen_grade7_days181_187.py
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


def _rebalance_answer_positions(days, seed=20260818187):
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


g7_181_187 = [
day(181, [
L('Grammar: Prepositional Phrases as Adjectives and Adverbs',
  'Grade 7 Language strand: a prepositional phrase begins with a preposition and ends with a noun or pronoun called the object of the preposition, and the whole phrase can function as an adjective, describing a noun, or as an adverb, describing a verb, adjective, or another adverb.',
  [('What does a prepositional phrase begin with?', ['A preposition', 'A verb', 'A concept unrelated to grammar', 'A conjunction'], 0),
   ('What is the object of the preposition?', ['The noun or pronoun that ends the prepositional phrase', 'The subject of the sentence', 'A concept unrelated to prepositional phrases', 'The main verb of the sentence'], 0),
   ('In the sentence, The book on the table belongs to Maria, which words form a prepositional phrase acting as an adjective?', ['on the table', 'belongs to Maria', 'A concept unrelated to grammar', 'The book'], 0),
   ('In the sentence, She walked into the room, what does the prepositional phrase into the room modify?', ['The verb walked, functioning as an adverb', 'The noun she, functioning as an adjective', 'A concept unrelated to prepositional phrases', 'Nothing, since prepositional phrases never modify anything'], 0),
   ('Why might a writer use a prepositional phrase instead of a single adjective or adverb?', ['To add specific detail about location, time, or manner that a single word cannot capture', 'Prepositional phrases can never add any detail to a sentence', 'A concept unrelated to grammar', 'Single words always provide more detail than a phrase'], 0)]),
M('Geometry: The Area and Circumference of Sectors of a Circle',
  'Grade 7 Math strand: a sector of a circle is a pie-shaped region bounded by two radii and an arc, and its area and arc length can be found by taking the same fraction of the circles central angle out of 360 degrees and applying that fraction to the full circles area or circumference.',
  [('What is a sector of a circle?', ['A pie-shaped region bounded by two radii and an arc', 'A straight line segment across the circle', 'A concept unrelated to geometry', 'The single point at the centre of the circle'], 0),
   ('What fraction of a full circle does a sector with a 90 degree central angle represent?', ['One quarter of the circle', 'One half of the circle', 'A concept unrelated to sectors', 'The entire circle'], 0),
   ('If a circle has an area of 100 square centimetres, what is the area of a sector with a 90 degree central angle?', ['25 square centimetres', '50 square centimetres', '100 square centimetres', '10 square centimetres'], 0),
   ('What two straight edges bound a sector of a circle?', ['Two radii', 'Two diameters', 'A concept unrelated to circles', 'Two tangent lines'], 0),
   ('Why does finding a sectors area involve first finding what fraction the central angle represents out of 360 degrees?', ['Because a sector is a proportional slice of the whole circle, based on how much of the 360 degree circle its angle covers', 'Sector area has no relationship to the central angle at all', 'A concept unrelated to geometry', 'Every sector always has exactly the same area regardless of its angle'], 0)]),
Sc('Technology: Renewable Energy Storage and Grid-Scale Batteries',
   'Grade 7 Science strand: because solar and wind power generation varies with weather and time of day, energy storage technologies such as large rechargeable batteries store surplus electricity when supply is high so it can be released back into the grid when demand rises or generation drops.',
   [('Why is energy storage important for solar and wind power?', ['Solar and wind generation varies with weather and time of day, so storage helps balance supply and demand', 'Solar and wind power always generate exactly the same amount of electricity at every moment', 'A concept unrelated to renewable energy', 'Energy storage has no connection to renewable power sources'], 0),
    ('What is one common technology used to store surplus electricity from renewable sources?', ['Large rechargeable batteries', 'A single household lightbulb', 'A concept unrelated to energy storage', 'A basic hand-crank generator'], 0),
    ('When does a grid-scale battery typically release its stored electricity?', ['When demand rises or renewable generation drops', 'Only during a full moon', 'A concept unrelated to grid-scale storage', 'Batteries never release stored electricity once charged'], 0),
    ('Why might a region with a lot of solar power installed also invest heavily in battery storage?', ['To store excess daytime solar power for use after the sun sets', 'Solar power never produces any excess electricity to store', 'A concept unrelated to renewable energy', 'Battery storage has no relationship to solar power generation'], 0),
    ('Why is grid-scale energy storage considered a key part of expanding renewable energy use?', ['It helps make variable renewable sources more reliable by smoothing out supply throughout the day', 'Energy storage always makes renewable power less reliable', 'A concept unrelated to technology', 'Grid-scale storage has no effect on renewable energy reliability'], 0)]),
SS('Social Studies: The Franklin Expedition and Nineteenth-Century Arctic Exploration',
   'Grade 7 Social Studies strand: in 1845 British explorer John Franklin led an expedition with two ships to chart the Northwest Passage through the Canadian Arctic, but the ships became trapped in ice and the entire crew was lost, and the mystery of what happened, along with Inuit oral history about the disaster, helped guide the eventual discovery of the wrecks more than 150 years later.',
   [('What was the goal of the Franklin Expedition when it set out in 1845?', ['To chart the Northwest Passage through the Canadian Arctic', 'To build a permanent city in the Arctic', 'A concept unrelated to Canadian history', 'To establish a trade route across the Pacific Ocean'], 0),
    ('What ultimately happened to the ships and crew of the Franklin Expedition?', ['The ships became trapped in ice and the entire crew was lost', 'The expedition successfully returned home with no losses', 'A concept unrelated to Arctic exploration', 'The crew settled permanently in the Arctic and thrived'], 0),
    ('What kind of knowledge helped guide the eventual discovery of the Franklin Expedition wrecks?', ['Inuit oral history passed down about the disaster', 'Satellite photographs taken in the 1840s', 'A concept unrelated to the Franklin Expedition', 'Weather reports broadcast on the radio at the time'], 0),
    ('Roughly how long after the expedition were the wrecks of Franklins ships eventually found?', ['More than 150 years later', 'The very next year', 'A concept unrelated to Canadian history', 'Only a few weeks later'], 0),
    ('Why might the story of the Franklin Expedition still be significant to understanding Arctic exploration and Indigenous knowledge today?', ['It shows how combining historical records with Inuit oral history can solve long-standing mysteries', 'The Franklin Expedition has no connection to Arctic history or Indigenous knowledge', 'This concept has no relevance to social studies', 'Inuit oral history played no role in locating the wrecks'], 0)]),
]),
day(182, [
L('Vocabulary: Contronyms, Words That Are Their Own Opposite',
  'Grade 7 Language strand: a contronym is a single word that has two opposite meanings depending on context, such as the word dust, which can mean to remove fine particles or to sprinkle fine particles onto something, so a reader must rely on surrounding context to determine which meaning applies.',
  [('What is a contronym?', ['A single word that has two opposite meanings depending on context', 'A word that always has exactly one fixed meaning', 'A concept unrelated to vocabulary', 'A word borrowed directly from a foreign language with no change'], 0),
   ('Which of these words is commonly used as a contronym, meaning both to remove fine particles and to sprinkle them on?', ['Dust', 'Jump', 'A concept unrelated to contronyms', 'Walk'], 0),
   ('How can a reader determine which of the two opposite meanings a contronym is being used with?', ['By relying on the surrounding context of the sentence', 'Contronyms can never be understood through context', 'A concept unrelated to vocabulary', 'By ignoring the rest of the sentence entirely'], 0),
   ('If someone says the referee will sanction the rule violation, and sanction here means to penalize, what does it mean if a company sanctions a new policy instead?', ['It approves or officially allows the new policy', 'It also means to penalize the new policy', 'A concept unrelated to contronyms', 'Sanction can never mean approve in any context'], 0),
   ('Why can contronyms be especially challenging for someone learning English as a new language?', ['The exact same word can signal opposite meanings, so context becomes essential to avoid misunderstanding', 'Contronyms always have identical meanings no matter the context', 'A concept unrelated to vocabulary', 'English contains no words with more than one meaning'], 0)]),
M('Number Theory: The Fibonacci Sequence and Patterns in Nature',
  'Grade 7 Math strand: the Fibonacci sequence is a pattern of numbers in which each term is the sum of the two terms before it, beginning 0, 1, 1, 2, 3, 5, 8, 13, and this pattern appears repeatedly in nature, such as in the spiral arrangement of seeds in a sunflower head or the branching of certain plants.',
  [('How is each term in the Fibonacci sequence generated?', ['By adding together the two terms that came before it', 'By multiplying the previous term by two', 'A concept unrelated to number theory', 'By subtracting one from the previous term'], 0),
   ('What are the first six terms of the Fibonacci sequence, starting from 0?', ['0, 1, 1, 2, 3, 5', '1, 2, 3, 4, 5, 6', '0, 2, 4, 6, 8, 10', '1, 1, 2, 4, 8, 16'], 0),
   ('What is the next term in the sequence after 3, 5, 8, 13?', ['21', '18', 'A concept unrelated to the Fibonacci sequence', '16'], 0),
   ('Where might the Fibonacci pattern appear in nature?', ['In the spiral arrangement of seeds in a sunflower head', 'In the exact colour of every flower petal', 'A concept unrelated to patterns in nature', 'Fibonacci numbers never appear anywhere in nature'], 0),
   ('Why might mathematicians find it interesting that a simple number pattern like the Fibonacci sequence appears repeatedly across unrelated living things?', ['It suggests an underlying mathematical structure may influence how certain natural growth patterns form', 'Repeating patterns in nature have no connection to mathematics at all', 'A concept unrelated to number theory', 'The Fibonacci sequence has never been observed in any living thing'], 0)]),
Sc('Biology: Pollinator Decline and Colony Collapse Disorder',
   'Grade 7 Science strand: pollinators such as bees, butterflies, and some birds carry pollen between flowers, enabling many plants to reproduce, but declining pollinator populations, including sudden bee losses known as colony collapse disorder, threaten both wild ecosystems and the crops that depend on pollination for food production.',
   [('What role do pollinators such as bees and butterflies play for many plants?', ['They carry pollen between flowers, enabling the plants to reproduce', 'They remove pollen from flowers with no other effect', 'A concept unrelated to biology', 'They prevent flowers from ever reproducing'], 0),
    ('What is colony collapse disorder?', ['A phenomenon involving sudden, unexplained losses of honeybee colonies', 'A disorder that only affects individual flowers, never bees', 'A concept unrelated to pollinator decline', 'A condition in which bee populations always increase rapidly'], 0),
    ('Why does pollinator decline matter for human food production?', ['Many crops depend on pollination to produce fruits, seeds, or vegetables', 'Crops never depend on pollinators for any part of their growth', 'A concept unrelated to pollinator decline', 'Human food production has no connection to pollinating insects'], 0),
    ('Besides bees, what is another example of an animal that can act as a pollinator?', ['Certain birds, such as hummingbirds', 'A concept unrelated to pollination', 'A fish living entirely underwater', 'A rock formation in a garden'], 0),
    ('Why might scientists be especially concerned about factors such as pesticide use and habitat loss affecting pollinators?', ['These factors can reduce pollinator populations, threatening both wild ecosystems and agricultural food supplies', 'Pesticide use and habitat loss have no effect on pollinator populations', 'This concept has no relevance to science', 'Pollinators are completely unaffected by changes to their environment'], 0)]),
SS('Social Studies: Terry Fox and the Marathon of Hope',
   'Grade 7 Social Studies strand: after losing part of his leg to cancer, Canadian athlete Terry Fox began the Marathon of Hope in 1980, an attempt to run across Canada to raise money and awareness for cancer research, and although illness forced him to stop before completing the run, his effort inspired an ongoing annual fundraising run held in his name across Canada and the world.',
   [('Why did Terry Fox begin the Marathon of Hope in 1980?', ['To run across Canada and raise money and awareness for cancer research', 'To compete in the Olympic Games', 'A concept unrelated to Canadian history', 'To promote a new type of running shoe'], 0),
    ('What physical challenge did Terry Fox face while attempting his run?', ['He had lost part of his leg to cancer', 'He had never faced any physical challenge at all', 'A concept unrelated to Terry Fox', 'He was unable to walk at any point in his life'], 0),
    ('What eventually forced Terry Fox to stop before completing his run across Canada?', ['His illness returned, forcing him to stop', 'He decided the run was no longer meaningful to him', 'A concept unrelated to the Marathon of Hope', 'He successfully completed the entire run with no interruption'], 0),
    ('What continues to happen each year in Terry Foxs name?', ['An annual fundraising run held across Canada and the world', 'Nothing at all, since his effort was quickly forgotten', 'A concept unrelated to social studies', 'A yearly ban on all charitable fundraising events'], 0),
    ('Why might Terry Foxs Marathon of Hope be considered an important part of Canadian identity and culture?', ['It reflects values of perseverance and generosity that continue to inspire ongoing charitable action nationwide', 'The Marathon of Hope has no lasting cultural or historical significance', 'This concept has no relevance to social studies', 'Terry Fox is remembered only outside of Canada, not within it'], 0)]),
]),
day(183, [
L('Reading: Analyzing Setup and Payoff in Plot (Chekhovs Gun)',
  'Grade 7 Language strand: setup and payoff is a storytelling principle, often summarized by the phrase Chekhovs Gun, which holds that a significant detail introduced early in a story, such as a gun mentioned in an early scene, should eventually play a meaningful role later in the plot, or it should not have been included at all.',
  [('What does the storytelling principle known as Chekhovs Gun suggest?', ['A significant detail introduced early in a story should eventually play a meaningful role later', 'Every detail in a story should be forgotten immediately after it appears', 'A concept unrelated to reading', 'Stories should never introduce any specific objects or details'], 0),
   ('What is setup in a story?', ['An early detail or event that prepares the reader for something significant later', 'The final sentence of a story with no connection to earlier events', 'A concept unrelated to plot structure', 'A detail that is only ever mentioned once and never matters again'], 0),
   ('What is payoff in a story?', ['The moment later in the story when an earlier setup becomes meaningful', 'The very first sentence of the story', 'A concept unrelated to setup and payoff', 'A detail that contradicts everything set up earlier for no reason'], 0),
   ('If a story carefully describes a locked door early on, what would be a satisfying payoff for that setup?', ['A character later needing to open or deal with that same locked door', 'The door being mentioned once and never appearing again', 'A concept unrelated to Chekhovs Gun', 'A completely different, unrelated door appearing instead'], 0),
   ('Why might a writer be careful about including unnecessary specific details that are never used again later in the story?', ['Unused specific details can mislead readers into expecting significance that never arrives', 'Unnecessary details always improve a story with no downside', 'A concept unrelated to reading', 'Readers never notice or expect payoff from specific details'], 0)]),
M('Algebra: Solving Age and Number Word Problems',
  'Grade 7 Math strand: age and number word problems can be solved by assigning a variable to an unknown quantity, such as a persons current age, then translating the relationships described in words, such as being twice as old in a certain number of years, into an algebraic equation that can be solved for the variable.',
  [('What is the first general step in solving an age or number word problem algebraically?', ['Assigning a variable to represent the unknown quantity', 'Guessing an answer with no calculation at all', 'A concept unrelated to algebra', 'Ignoring the relationships described in the problem'], 0),
   ('If a persons current age is represented by x, how would you represent their age in 5 years?', ['x plus 5', 'x minus 5', 'A concept unrelated to age problems', '5x'], 0),
   ('If a number problem states that a number plus 7 equals 15, what is the value of the number?', ['8', '7', '15', '22'], 0),
   ('If Sam is currently twice as old as Alex, and Alex is x years old, how can Sams current age be represented?', ['2x', 'x plus 2', 'A concept unrelated to algebra', 'x divided by 2'], 0),
   ('Why is translating a word problem into an algebraic equation a useful strategy for solving age and number problems?', ['It turns a description in words into a precise mathematical statement that can be solved using algebra', 'Word problems can never be translated into algebraic equations', 'A concept unrelated to algebra', 'Algebraic equations always make word problems more confusing with no benefit'], 0)]),
Sc('Earth Science: Deltas, Estuaries, and River Mouth Ecosystems',
   'Grade 7 Science strand: a delta forms where a river deposits sediment as it slows down and meets a larger body of water, often spreading into fan-shaped land, while an estuary is the area where fresh river water mixes with salty ocean water, creating a unique, nutrient-rich habitat for many species.',
   [('What causes a river delta to form?', ['A river depositing sediment as it slows down and meets a larger body of water', 'A river suddenly speeding up as it leaves the ocean', 'A concept unrelated to earth science', 'Sediment being removed entirely from a river mouth'], 0),
    ('What is an estuary?', ['An area where fresh river water mixes with salty ocean water', 'A region located entirely underground with no connection to water', 'A concept unrelated to river mouth ecosystems', 'A body of water containing only fresh water with no ocean influence'], 0),
    ('Why are estuaries often considered nutrient-rich habitats?', ['The mixing of fresh and salt water, along with sediment from the river, supports abundant plant and animal life', 'Estuaries never contain any nutrients that support living things', 'A concept unrelated to estuaries', 'Nutrient levels in estuaries have no connection to the mixing of water sources'], 0),
    ('What shape do many river deltas take as sediment spreads out at a river mouth?', ['A fan-like shape', 'A perfectly straight line', 'A concept unrelated to deltas', 'A shape with no relationship to the flow of sediment'], 0),
    ('Why might deltas and estuaries be considered ecologically important but also vulnerable to human activity?', ['They support diverse species and food sources, but pollution, damming, and development can disrupt their delicate balance', 'Deltas and estuaries are never affected by any human activity', 'This concept has no relevance to science', 'These ecosystems support no living things and require no protection'], 0)]),
SS('Social Studies: The Alberta Oil Sands and Canadas Energy Economy',
   'Grade 7 Social Studies strand: the Alberta oil sands contain one of the largest deposits of bitumen, a thick, heavy form of petroleum, in the world, and their development has made Canada a major energy exporter while also raising ongoing debates about environmental impact, Indigenous land rights, and the future of fossil fuel dependence.',
   [('What resource is found in large quantities in the Alberta oil sands?', ['Bitumen, a thick, heavy form of petroleum', 'Fresh water suitable for drinking', 'A concept unrelated to Canadian geography', 'Coal deposits used only for heating homes'], 0),
    ('How has the development of the Alberta oil sands affected Canadas economy?', ['It has made Canada a major energy exporter', 'It has had no effect on Canadas economy at all', 'A concept unrelated to social studies', 'It has eliminated Canadas involvement in the energy sector entirely'], 0),
    ('What is one ongoing debate connected to oil sands development?', ['Its environmental impact', 'Whether Canada has any natural resources at all', 'A concept unrelated to the Alberta oil sands', 'Whether Alberta is located within Canada'], 0),
    ('Whose land rights are sometimes raised as a concern in discussions about oil sands development?', ['Indigenous peoples land rights', 'The land rights of countries outside North America only', 'A concept unrelated to the oil sands', 'No land rights are ever discussed in connection with the oil sands'], 0),
    ('Why might the future of the Alberta oil sands be tied to broader questions about fossil fuel dependence?', ['As countries look to reduce reliance on fossil fuels, demand for oil sands products may shift over time', 'Fossil fuel dependence has no connection to the future of the oil sands', 'This concept has no relevance to social studies', 'The oil sands are entirely unrelated to any energy or environmental discussion'], 0)]),
]),
day(184, [
L('Writing: Writing a Choose Your Own Adventure Story',
  'Grade 7 Language strand: a choose your own adventure story presents the reader with decision points throughout the narrative, each leading to a different branch of the plot, requiring the writer to plan multiple possible paths and endings rather than a single fixed sequence of events.',
  [('What is a defining feature of a choose your own adventure story?', ['It presents the reader with decision points that lead to different branches of the plot', 'It follows a single fixed sequence of events with no reader input', 'A concept unrelated to writing', 'It never includes more than one possible ending'], 0),
   ('What must a writer plan for when creating a choose your own adventure story?', ['Multiple possible paths and endings', 'Only a single unchangeable outcome', 'A concept unrelated to choose your own adventure writing', 'A story with no decision points of any kind'], 0),
   ('What happens at a decision point in this kind of story?', ['The reader chooses between different options that lead to different parts of the story', 'The story ends immediately with no further reading', 'A concept unrelated to writing', 'The writer removes all choices from the reader entirely'], 0),
   ('Why might planning a story map or flowchart be helpful before writing a choose your own adventure story?', ['It helps the writer keep track of the many branching paths and how they connect', 'Story maps are never useful for planning branching narratives', 'A concept unrelated to writing', 'A flowchart removes the need for the story to have any plot at all'], 0),
   ('How does writing a choose your own adventure story differ from writing a traditional short story with one storyline?', ['It requires creating several connected storylines instead of just one straightforward sequence of events', 'Both formats require exactly the same single, unbranching storyline', 'This concept has no relevance to writing', 'A choose your own adventure story can never include more than one scene'], 0)]),
M('Financial Literacy: Comparing Renting and Buying a Home',
  'Grade 7 Math strand: renting a home typically involves regular payments to a landlord with fewer upfront costs, while buying a home usually requires a larger upfront down payment and ongoing mortgage payments, so comparing the total costs and benefits of each option over time is an important financial literacy skill.',
  [('What does renting a home typically involve?', ['Regular payments to a landlord with fewer upfront costs', 'A single one-time payment with no future payments ever required', 'A concept unrelated to financial literacy', 'Owning the property outright from the very first payment'], 0),
   ('What does buying a home usually require upfront?', ['A larger upfront down payment', 'No payment of any kind at any point', 'A concept unrelated to buying a home', 'A single payment covering the entire cost of the home instantly'], 0),
   ('If a monthly rent payment is 1500 dollars, what is the total rent paid over 12 months?', ['18000 dollars', '1500 dollars', '15000 dollars', '12000 dollars'], 0),
   ('What ongoing payments are typically required after buying a home with a loan?', ['Mortgage payments', 'No payments are ever required again', 'A concept unrelated to buying a home', 'Only a single rent payment per year'], 0),
   ('Why is comparing the total costs and benefits of renting versus buying over time considered an important financial literacy skill?', ['It helps a person make an informed decision based on their financial situation and long-term goals', 'Renting and buying always cost exactly the same amount with no differences', 'A concept unrelated to financial literacy', 'Financial literacy has no connection to housing decisions'], 0)]),
Sc('Physics: How Refrigerators and Heat Pumps Move Heat',
   'Grade 7 Science strand: refrigerators and heat pumps do not create cold directly, but instead use a circulating refrigerant fluid and a compressor to absorb heat from one area and release it into another, effectively moving heat from a cooler space to a warmer one using energy input.',
   [('What do refrigerators and heat pumps primarily do?', ['Move heat from one area to another using a circulating refrigerant and compressor', 'Create cold temperatures directly with no movement of heat involved', 'A concept unrelated to physics', 'Destroy heat energy completely so it no longer exists'], 0),
    ('What is used to help move heat within a refrigerator or heat pump system?', ['A circulating refrigerant fluid and a compressor', 'A single stationary block of ice with no moving parts', 'A concept unrelated to refrigeration', 'A wooden box with no mechanical components'], 0),
    ('In a refrigerator, from where is heat generally absorbed?', ['From inside the refrigerator, where food is stored', 'From outside the kitchen entirely, unrelated to the refrigerator', 'A concept unrelated to how refrigerators work', 'From the compressor only, and nowhere else'], 0),
    ('Why does moving heat from a cooler space to a warmer one require energy input?', ['Heat naturally flows from warm to cool areas, so reversing that flow requires added energy, such as electricity', 'Heat always flows on its own from cool areas to warm areas with no energy needed', 'A concept unrelated to physics', 'Moving heat in any direction never requires any energy at all'], 0),
    ('Why might a heat pump be considered an efficient way to both heat and cool a home?', ['The same system can move heat into a home in winter or out of a home in summer, using less energy than generating heat directly', 'Heat pumps can only ever be used to cool a space, never to heat one', 'This concept has no relevance to science', 'Heat pumps require far more energy than any other heating or cooling method'], 0)]),
SS('Social Studies: The Atlantic Cod Moratorium and Its Impact on Newfoundland',
   'Grade 7 Social Studies strand: in 1992 the Canadian government declared a moratorium, or temporary ban, on cod fishing off the coast of Newfoundland after decades of overfishing caused the cod population to collapse, resulting in the sudden loss of tens of thousands of fishing jobs and lasting economic change across many coastal communities.',
   [('What did the Canadian government declare in 1992 regarding cod fishing off Newfoundland?', ['A moratorium, or temporary ban, on cod fishing', 'A permanent increase in cod fishing quotas', 'A concept unrelated to Canadian history', 'A brand new fishing industry with no restrictions at all'], 0),
    ('What caused the collapse of the cod population off Newfoundland?', ['Decades of overfishing', 'A sudden, unrelated drop in ocean temperature with no human cause', 'A concept unrelated to the cod moratorium', 'A deliberate decision to remove all cod from the ocean at once'], 0),
    ('What was one immediate economic effect of the cod moratorium?', ['The sudden loss of tens of thousands of fishing jobs', 'An immediate and permanent increase in fishing jobs', 'A concept unrelated to social studies', 'No economic effect of any kind on coastal communities'], 0),
    ('What kind of communities were most directly affected by the cod moratorium?', ['Coastal communities in Newfoundland that depended on the fishing industry', 'Communities located entirely inland with no connection to fishing', 'A concept unrelated to the Atlantic cod moratorium', 'Communities located outside of Canada entirely'], 0),
    ('Why is the Atlantic cod moratorium often cited as an example of the risks of overfishing?', ['It shows how unsustainable resource use can lead to both ecological collapse and long-term economic hardship', 'Overfishing never has any effect on fish populations or local economies', 'This concept has no relevance to social studies', 'The cod moratorium had no connection to overfishing of any kind'], 0)]),
]),
day(185, [
L('Media Literacy: Analyzing Documentary Filmmaking Techniques',
  'Grade 7 Language strand: documentary filmmakers use techniques such as selective interview footage, background music, narration, and the order in which scenes are arranged to shape how an audience understands real events, meaning even nonfiction films reflect the choices and perspective of their creators.',
  [('What is one technique documentary filmmakers use to shape how an audience understands events?', ['Selective interview footage', 'A completely blank screen with no footage of any kind', 'A concept unrelated to media literacy', 'Randomly generated, unrelated images with no purpose'], 0),
   ('How can background music influence a viewers response to a documentary scene?', ['It can create a particular mood or emotional reaction to the events being shown', 'Background music has no effect on how a viewer responds to a scene', 'A concept unrelated to documentary filmmaking', 'Music is never included in documentary films of any kind'], 0),
   ('Why does the order in which scenes are arranged in a documentary matter?', ['It can shape the narrative and influence how the audience interprets cause and effect', 'Scene order has no impact on how a documentary is understood', 'A concept unrelated to media literacy', 'Documentaries are required to present scenes in a single fixed order with no creative choice'], 0),
   ('What does it mean to say a documentary reflects the perspective of its creators?', ['The choices made in filming and editing shape a particular version of events, rather than a purely neutral record', 'Documentaries always present every possible perspective equally with no bias', 'A concept unrelated to documentary filmmaking', 'A documentary can never involve any creative or editorial choices'], 0),
   ('Why is media literacy important when watching a documentary, even though it presents real events?', ['It helps viewers recognize that editing and framing choices still shape how those real events are presented', 'Media literacy is only relevant to fictional films, never documentaries', 'This concept has no relevance to media literacy', 'Documentaries present events with no editing or framing choices involved'], 0)]),
M('Geometry: Classifying Polyhedra by Faces, Edges, and Vertices',
  'Grade 7 Math strand: a polyhedron is a three-dimensional solid with flat polygonal faces, straight edges, and vertices where edges meet, and Eulers formula states that for many polyhedra, the number of faces plus the number of vertices minus the number of edges equals two.',
  [('What is a polyhedron?', ['A three-dimensional solid with flat polygonal faces, straight edges, and vertices', 'A two-dimensional shape with no edges or vertices', 'A concept unrelated to geometry', 'A curved solid with no flat surfaces at all'], 0),
   ('What is a vertex of a polyhedron?', ['A point where edges of the polyhedron meet', 'A flat polygonal surface of the polyhedron', 'A concept unrelated to polyhedra', 'A curved line running along the outside of the solid'], 0),
   ('According to Eulers formula, what does the number of faces plus the number of vertices minus the number of edges equal for many polyhedra?', ['2', '0', '1', '10'], 0),
   ('A cube has 6 faces and 8 vertices. According to Eulers formula, how many edges does it have?', ['12', '6', '8', '14'], 0),
   ('Why might Eulers formula be a useful tool for checking whether a described three-dimensional shape is a valid polyhedron?', ['If the counted faces, vertices, and edges do not satisfy the formula, the shape may not be a standard polyhedron', 'Eulers formula can never be used to check any property of a polyhedron', 'A concept unrelated to geometry', 'The number of faces, edges, and vertices never has any mathematical relationship'], 0)]),
Sc('Technology: How Wastewater Treatment Plants Clean Water',
   'Grade 7 Science strand: wastewater treatment plants clean used water from homes and businesses through stages such as removing large solids, using bacteria to break down organic waste, and disinfecting the water before it is safely released back into the environment or reused.',
   [('What is the general purpose of a wastewater treatment plant?', ['To clean used water from homes and businesses before it is released or reused', 'To make water more polluted before releasing it into rivers', 'A concept unrelated to technology', 'To generate electricity with no connection to water treatment'], 0),
    ('What is one of the early stages of wastewater treatment?', ['Removing large solids from the water', 'Adding large solids directly into the water', 'A concept unrelated to wastewater treatment', 'Immediately releasing the water untreated'], 0),
    ('What role do bacteria often play in wastewater treatment?', ['They help break down organic waste in the water', 'They have no role in wastewater treatment at all', 'A concept unrelated to wastewater treatment plants', 'They are used only to add colour to the water'], 0),
    ('Why is disinfecting water an important step before it is released back into the environment?', ['It helps kill harmful microorganisms that could spread disease', 'Disinfecting water always makes it more dangerous', 'A concept unrelated to wastewater treatment', 'Disinfection has no effect on the safety of released water'], 0),
    ('Why might a growing city need to invest in expanding or upgrading its wastewater treatment infrastructure?', ['A larger population produces more wastewater, requiring greater treatment capacity to protect water quality', 'Population growth has no connection to the amount of wastewater a city produces', 'This concept has no relevance to technology or science', 'Wastewater treatment needs never change regardless of population size'], 0)]),
SS('Social Studies: Expo 86 and Vancouvers Growth as a Pacific Gateway City',
   'Grade 7 Social Studies strand: Expo 86, a world exposition held in Vancouver in 1986 focused on transportation and communication themes, attracted millions of visitors and left behind lasting infrastructure and international attention that helped fuel Vancouvers growth into a major Pacific gateway city for trade and immigration.',
   [('What event was held in Vancouver in 1986?', ['Expo 86, a world exposition', 'The Winter Olympic Games', 'A concept unrelated to Canadian history', 'A national election for prime minister'], 0),
    ('What themes did Expo 86 focus on?', ['Transportation and communication', 'Only agriculture and farming', 'A concept unrelated to Expo 86', 'Only ancient history with no modern focus'], 0),
    ('What did Expo 86 leave behind for the city of Vancouver?', ['Lasting infrastructure and international attention', 'No lasting effect of any kind on the city', 'A concept unrelated to social studies', 'A complete loss of all existing city infrastructure'], 0),
    ('What role has Vancouver grown into regarding trade with the Pacific region?', ['A major Pacific gateway city for trade and immigration', 'A city with no connection to Pacific trade whatsoever', 'A concept unrelated to Expo 86', 'A landlocked city with no access to any coastline'], 0),
    ('Why might hosting a major international event like Expo 86 help a city attract long-term economic growth?', ['It can showcase the city globally, attracting future investment, tourism, and trade connections', 'International events never have any lasting economic effect on a host city', 'This concept has no relevance to social studies', 'Hosting Expo 86 caused Vancouvers economy to shrink permanently'], 0)]),
]),
day(186, [
L('Grammar: Capitalization Rules for Titles and Proper Nouns',
  'Grade 7 Language strand: proper nouns, which name specific people, places, or organizations, are always capitalized, and in titles of books, movies, and articles, the first and last words along with all major words are typically capitalized, while short articles, conjunctions, and prepositions are usually left lowercase unless they begin the title.',
  [('What is always capitalized in a proper noun?', ['The first letter, since proper nouns name specific people, places, or organizations', 'Every single letter of the word is capitalized', 'A concept unrelated to grammar', 'Proper nouns are never capitalized under any circumstance'], 0),
   ('Which of these is an example of a proper noun that should be capitalized?', ['Toronto', 'city', 'A concept unrelated to capitalization', 'river'], 0),
   ('In the title of a book or movie, which words are typically capitalized?', ['The first and last words, along with all major words', 'Only the very last word of the title', 'A concept unrelated to capitalization rules', 'No words in a title are ever capitalized'], 0),
   ('In a title, which types of words are usually left lowercase unless they begin the title?', ['Short articles, conjunctions, and prepositions', 'All nouns appearing anywhere in the title', 'A concept unrelated to grammar', 'Every single word in the title without exception'], 0),
   ('Why do capitalization rules for titles typically capitalize major words but not short connecting words?', ['It helps visually highlight the most meaningful words while keeping small connecting words unobtrusive', 'Capitalization rules for titles have no consistent pattern of any kind', 'A concept unrelated to grammar', 'Every word in a title must always be treated exactly the same way'], 0)]),
M('Data Management: Constructing and Interpreting Radar Charts',
  'Grade 7 Math strand: a radar chart, also called a spider chart, displays multiple related variables on axes that radiate outward from a central point, connecting the plotted values with lines to form a shape that makes it easy to compare several categories for one or more subjects at once.',
  [('What is another common name for a radar chart?', ['A spider chart', 'A pie chart', 'A concept unrelated to data management', 'A bar chart'], 0),
   ('How are the axes of a radar chart arranged?', ['They radiate outward from a central point', 'They are all arranged in a single straight horizontal line', 'A concept unrelated to radar charts', 'There are no axes at all in a radar chart'], 0),
   ('What is formed when the plotted values on a radar chart are connected with lines?', ['A shape that represents the pattern of values across categories', 'A single straight line with no enclosed shape', 'A concept unrelated to data management', 'The values are never connected with any lines'], 0),
   ('Why might a radar chart be useful for comparing a students scores across five different subjects?', ['It allows all five subject scores to be viewed together on one chart, showing relative strengths and weaknesses', 'A radar chart can only ever display a single category of data at a time', 'A concept unrelated to radar charts', 'Radar charts cannot be used to compare more than one value at once'], 0),
   ('What could it mean if the shape on a radar chart is very lopsided, with some axes reaching far out and others staying close to the centre?', ['The subject performs strongly in some categories and weakly in others', 'The subject performs identically well in every single category', 'A concept unrelated to interpreting radar charts', 'A lopsided shape always indicates an error in the data with no other explanation'], 0)]),
Sc('Chemistry: How Sunscreen Works to Block UV Radiation',
   'Grade 7 Science strand: sunscreen works using chemical compounds that either absorb ultraviolet radiation and convert it into a small amount of heat, or physical mineral compounds that reflect and scatter UV rays away from the skin, both approaches helping to reduce skin damage caused by prolonged sun exposure.',
   [('What is one way that sunscreen can protect skin from ultraviolet radiation?', ['Chemical compounds can absorb UV radiation and convert it into a small amount of heat', 'Sunscreen has no effect whatsoever on ultraviolet radiation', 'A concept unrelated to chemistry', 'Sunscreen works only by adding colour to the skin'], 0),
    ('What do physical mineral sunscreen compounds do to UV rays?', ['Reflect and scatter UV rays away from the skin', 'Attract additional UV rays directly onto the skin', 'A concept unrelated to sunscreen', 'Physical mineral compounds have no effect on UV rays at all'], 0),
    ('What type of radiation does sunscreen primarily help protect skin against?', ['Ultraviolet radiation', 'Radio waves', 'A concept unrelated to chemistry', 'Microwave radiation'], 0),
    ('Why can prolonged sun exposure without protection be harmful to skin?', ['Ultraviolet radiation can damage skin cells over time', 'Ultraviolet radiation has no effect on skin cells whatsoever', 'A concept unrelated to sunscreen chemistry', 'Sun exposure only ever affects hair, never skin'], 0),
    ('Why might sunscreen need to be reapplied periodically to remain effective?', ['Its protective compounds can break down or wash away over time and with exposure to water or sweat', 'Sunscreen compounds always remain fully effective forever once applied', 'This concept has no relevance to chemistry', 'Reapplying sunscreen has no effect on how well it protects the skin'], 0)]),
SS('Social Studies: Inuit Traditional Knowledge and Life in the Arctic',
   'Grade 7 Social Studies strand: Inuit peoples have lived in the Arctic regions of what is now northern Canada for thousands of years, developing traditional knowledge, often called Inuit Qaujimajatuqangit, about survival, navigation, and sustainable use of Arctic resources that continues to inform environmental science and community life today.',
   [('For roughly how long have Inuit peoples lived in the Arctic regions of what is now northern Canada?', ['Thousands of years', 'Only the past 50 years', 'A concept unrelated to Canadian history', 'Since the year 2000'], 0),
    ('What is Inuit Qaujimajatuqangit?', ['Traditional Inuit knowledge about survival, navigation, and sustainable resource use', 'A style of modern architecture found only in southern Canada', 'A concept unrelated to Inuit culture', 'A type of Canadian currency used only in the Arctic'], 0),
    ('What kinds of knowledge does Inuit traditional knowledge commonly include?', ['Knowledge about survival, navigation, and sustainable use of Arctic resources', 'Knowledge unrelated to the Arctic environment in any way', 'A concept unrelated to social studies', 'Only knowledge about activities found outside the Arctic'], 0),
    ('How is Inuit traditional knowledge sometimes used today?', ['It continues to inform environmental science and community life', 'It has no continued relevance to modern life at all', 'A concept unrelated to Inuit traditional knowledge', 'It is only recorded in historical documents and never applied today'], 0),
    ('Why might combining Inuit traditional knowledge with modern scientific research be valuable for understanding the Arctic environment?', ['Traditional knowledge developed over generations can offer detailed, long-term observations that complement modern scientific methods', 'Traditional knowledge and modern science can never be meaningfully combined', 'This concept has no relevance to social studies', 'Only modern scientific methods provide any useful understanding of the Arctic'], 0)]),
]),
day(187, [
L('Language Capstone Review: Grammar, Vocabulary, Reading, and Media Literacy (Days 181-186)',
  'Grade 7 Language strand review: this final review of the 187-day Grade 7 curriculum revisits prepositional phrases, contronyms, setup and payoff in plot structure, writing a choose your own adventure story, documentary filmmaking techniques, and capitalization rules, closing out the complete Grade 7 language program.',
  [('What does a prepositional phrase begin with?', ['A preposition', 'A verb', 'A concept unrelated to grammar', 'A conjunction'], 0),
   ('What is a contronym?', ['A single word that has two opposite meanings depending on context', 'A word that always has exactly one fixed meaning', 'A concept unrelated to vocabulary', 'A word borrowed directly from a foreign language with no change'], 0),
   ('What does the storytelling principle known as Chekhovs Gun suggest?', ['A significant detail introduced early in a story should eventually play a meaningful role later', 'Every detail in a story should be forgotten immediately after it appears', 'A concept unrelated to reading', 'Stories should never introduce any specific objects or details'], 0),
   ('What is a defining feature of a choose your own adventure story?', ['It presents the reader with decision points that lead to different branches of the plot', 'It follows a single fixed sequence of events with no reader input', 'A concept unrelated to writing', 'It never includes more than one possible ending'], 0),
   ('What is one technique documentary filmmakers use to shape how an audience understands events?', ['Selective interview footage', 'A completely blank screen with no footage of any kind', 'A concept unrelated to media literacy', 'Randomly generated, unrelated images with no purpose'], 0),
   ('What is always capitalized in a proper noun?', ['The first letter, since proper nouns name specific people, places, or organizations', 'Every single letter of the word is capitalized', 'A concept unrelated to grammar', 'Proper nouns are never capitalized under any circumstance'], 0)]),
M('Math Capstone Review: Geometry, Number Theory, Algebra, and Data Management (Days 181-186)',
  'Grade 7 Math strand review: this final review of the 187-day Grade 7 curriculum revisits sectors of a circle, the Fibonacci sequence, age and number word problems, comparing renting and buying a home, classifying polyhedra, and radar charts, closing out the complete Grade 7 math program.',
  [('What is a sector of a circle?', ['A pie-shaped region bounded by two radii and an arc', 'A straight line segment across the circle', 'A concept unrelated to geometry', 'The single point at the centre of the circle'], 0),
   ('How is each term in the Fibonacci sequence generated?', ['By adding together the two terms that came before it', 'By multiplying the previous term by two', 'A concept unrelated to number theory', 'By subtracting one from the previous term'], 0),
   ('What is the first general step in solving an age or number word problem algebraically?', ['Assigning a variable to represent the unknown quantity', 'Guessing an answer with no calculation at all', 'A concept unrelated to algebra', 'Ignoring the relationships described in the problem'], 0),
   ('What does renting a home typically involve?', ['Regular payments to a landlord with fewer upfront costs', 'A single one-time payment with no future payments ever required', 'A concept unrelated to financial literacy', 'Owning the property outright from the very first payment'], 0),
   ('What is a polyhedron?', ['A three-dimensional solid with flat polygonal faces, straight edges, and vertices', 'A two-dimensional shape with no edges or vertices', 'A concept unrelated to geometry', 'A curved solid with no flat surfaces at all'], 0),
   ('What is another common name for a radar chart?', ['A spider chart', 'A pie chart', 'A concept unrelated to data management', 'A bar chart'], 0)]),
Sc('Science Capstone Review: Technology, Biology, Earth Science, and Chemistry (Days 181-186)',
   'Grade 7 Science strand review: this final review of the 187-day Grade 7 curriculum revisits renewable energy storage, pollinator decline, deltas and estuaries, refrigerators and heat pumps, wastewater treatment, and how sunscreen blocks UV radiation, closing out the complete Grade 7 science program.',
   [('Why is energy storage important for solar and wind power?', ['Solar and wind generation varies with weather and time of day, so storage helps balance supply and demand', 'Solar and wind power always generate exactly the same amount of electricity at every moment', 'A concept unrelated to renewable energy', 'Energy storage has no connection to renewable power sources'], 0),
    ('What role do pollinators such as bees and butterflies play for many plants?', ['They carry pollen between flowers, enabling the plants to reproduce', 'They remove pollen from flowers with no other effect', 'A concept unrelated to biology', 'They prevent flowers from ever reproducing'], 0),
    ('What causes a river delta to form?', ['A river depositing sediment as it slows down and meets a larger body of water', 'A river suddenly speeding up as it leaves the ocean', 'A concept unrelated to earth science', 'Sediment being removed entirely from a river mouth'], 0),
    ('What do refrigerators and heat pumps primarily do?', ['Move heat from one area to another using a circulating refrigerant and compressor', 'Create cold temperatures directly with no movement of heat involved', 'A concept unrelated to physics', 'Destroy heat energy completely so it no longer exists'], 0),
    ('What is the general purpose of a wastewater treatment plant?', ['To clean used water from homes and businesses before it is released or reused', 'To make water more polluted before releasing it into rivers', 'A concept unrelated to technology', 'To generate electricity with no connection to water treatment'], 0),
    ('What is one way that sunscreen can protect skin from ultraviolet radiation?', ['Chemical compounds can absorb UV radiation and convert it into a small amount of heat', 'Sunscreen has no effect whatsoever on ultraviolet radiation', 'A concept unrelated to chemistry', 'Sunscreen works only by adding colour to the skin'], 0)]),
SS('Social Studies Capstone Review: Arctic History, Canadian Icons, and Economic Geography (Days 181-186)',
   'Grade 7 Social Studies strand review: this final review of the 187-day Grade 7 curriculum revisits the Franklin Expedition, Terry Fox and the Marathon of Hope, the Alberta oil sands, the Atlantic cod moratorium, Expo 86, and Inuit traditional knowledge, closing out the complete Grade 7 social studies program and the full K-12 Grade 7 curriculum build.',
   [('What was the goal of the Franklin Expedition when it set out in 1845?', ['To chart the Northwest Passage through the Canadian Arctic', 'To build a permanent city in the Arctic', 'A concept unrelated to Canadian history', 'To establish a trade route across the Pacific Ocean'], 0),
    ('Why did Terry Fox begin the Marathon of Hope in 1980?', ['To run across Canada and raise money and awareness for cancer research', 'To compete in the Olympic Games', 'A concept unrelated to Canadian history', 'To promote a new type of running shoe'], 0),
    ('What resource is found in large quantities in the Alberta oil sands?', ['Bitumen, a thick, heavy form of petroleum', 'Fresh water suitable for drinking', 'A concept unrelated to Canadian geography', 'Coal deposits used only for heating homes'], 0),
    ('What did the Canadian government declare in 1992 regarding cod fishing off Newfoundland?', ['A moratorium, or temporary ban, on cod fishing', 'A permanent increase in cod fishing quotas', 'A concept unrelated to Canadian history', 'A brand new fishing industry with no restrictions at all'], 0),
    ('What event was held in Vancouver in 1986?', ['Expo 86, a world exposition', 'The Winter Olympic Games', 'A concept unrelated to Canadian history', 'A national election for prime minister'], 0),
    ('For roughly how long have Inuit peoples lived in the Arctic regions of what is now northern Canada?', ['Thousands of years', 'Only the past 50 years', 'A concept unrelated to Canadian history', 'Since the year 2000'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_181_187)
    append_to(7, g7_181_187)
