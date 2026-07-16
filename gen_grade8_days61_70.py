#!/usr/bin/env python3
"""Phase 4: Grade 8, Days 61-70 (fourth Grade 8 batch, extending the school
year past the Day 60 milestone). Topics chosen to avoid any overlap with
the existing Day 1-60 set (see data/grade8.ts): foreshadowing/flashback,
allegory, graphic novels, and filter bubbles in Language; coordinate
geometry, statistics, absolute value equations, and box-and-whisker plots
in Math; the Water Systems earth-and-space strand, simple machines,
density/buoyancy, acids/bases, and planetary motion in Science; and the
Red River Resistance through Terry Fox and the Marathon of Hope in
History.

Grade 8's fourth subject key remains "History" (not "SocialStudies"),
consistent with the Days 31-40, 41-50, and 51-60 batches and the
pre-existing data/grade8.ts.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes and quotation marks
use the curly Unicode form (’ “ ”) so they never collide with the
double-quoted TS string literals the generator embeds them in.
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-social-studies'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science & Technology',
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


g8_61_70 = [
day(61, [
L('Reading: Analyzing Foreshadowing and Flashback',
  'Grade 8 Reading strand: foreshadowing is when an author hints at events that will happen later in a story, while flashback interrupts the present narrative to show an earlier moment, both shaping how readers understand plot and character.',
  [('Foreshadowing is a literary technique in which ___.', ['An author hints at events that will happen later in the story', 'An author only describes events that already occurred', 'A concept unrelated to foreshadowing', 'A story never contains any hints about future events'], 0),
   ('Flashback is a literary technique in which ___.', ['The narrative interrupts the present to show an earlier moment', 'The narrative only moves forward in time', 'A concept unrelated to flashback', 'A character predicts a future event with certainty'], 0),
   ('Which is an example of foreshadowing?', ['A character noticing dark storm clouds before a tragedy occurs', 'A character remembering their childhood home', 'A concept unrelated to foreshadowing', 'A narrator describing a character’s appearance'], 0),
   ('Why might an author use a flashback in a story?', ['To provide background information that helps explain a character’s present actions', 'Flashbacks never provide any useful information to readers', 'A reason unrelated to flashback', 'A flashback always confuses readers with no purpose'], 0),
   ('Why is recognizing foreshadowing useful when reading a novel?', ['It can build suspense and prepare readers for upcoming events', 'Foreshadowing has no effect on how a story is understood', 'A reason unrelated to reading comprehension', 'Foreshadowing always reveals the ending immediately with no suspense'], 0)]),
M('Coordinate Geometry: Midpoint and Distance Formulas',
  'Grade 8 Math strand: the midpoint formula finds the point exactly halfway between two coordinates, while the distance formula, derived from the Pythagorean theorem, calculates the straight-line distance between two points on a coordinate plane.',
  [('The midpoint formula finds ___.', ['The point exactly halfway between two given coordinates', 'The total distance between two given coordinates', 'A concept unrelated to the midpoint formula', 'The slope of the line connecting two coordinates'], 0),
   ('The distance formula is derived from ___.', ['The Pythagorean theorem', 'The slope formula', 'A concept unrelated to the distance formula', 'The order of operations'], 0),
   ('Find the midpoint of the segment connecting (2, 4) and (6, 8).', ['(4, 6)', '(8, 12)', 'A value unrelated to the calculation', '(2, 4)'], 0),
   ('Using the distance formula, what is the distance between (0, 0) and (3, 4)?', ['5', '7', 'A value unrelated to the calculation', '12'], 0),
   ('Why might the distance formula be useful when solving a real-world problem?', ['It can calculate the straight-line distance between two locations plotted on a coordinate grid', 'The distance formula has no practical, real-world applications', 'A reason unrelated to coordinate geometry', 'It only works for points located on the same axis'], 0)]),
Sc('Water Systems: Watersheds and the Water Cycle',
   'Grade 8 Science strand: a watershed is an area of land where all water drains into a common river, lake, or ocean, and the water cycle describes the continuous movement of water through evaporation, condensation, precipitation, and collection.',
   [('A watershed is best described as ___.', ['An area of land where all water drains into a common river, lake, or ocean', 'A single isolated pond with no connection to surrounding land', 'A concept unrelated to watersheds', 'A structure built specifically to store drinking water'], 0),
    ('Evaporation in the water cycle occurs when ___.', ['Liquid water is heated and changes into water vapour', 'Water vapour cools and changes into liquid water', 'A process unrelated to the water cycle', 'Water falls from clouds as precipitation'], 0),
    ('Condensation in the water cycle occurs when ___.', ['Water vapour cools and changes into liquid water droplets', 'Liquid water changes into water vapour', 'A process unrelated to the water cycle', 'Water soaks into the ground'], 0),
    ('Precipitation refers to ___.', ['Water falling from clouds as rain, snow, sleet, or hail', 'Water vapour rising into the atmosphere', 'A concept unrelated to precipitation', 'Water flowing underground through soil'], 0),
    ('Why is understanding watersheds important for managing water resources?', ['Activities anywhere within a watershed can affect the water quality of connected rivers and lakes', 'Watersheds have no connection to water quality anywhere', 'A reason unrelated to water systems', 'Land activities never affect nearby bodies of water'], 0)]),
H('The Red River Resistance and the Métis Nation',
  'Grade 8 History strand: the Red River Resistance of 1869-70 was led by Louis Riel and the Métis to protect their land and rights as Canada moved to annex the Red River Settlement, ultimately leading to the creation of Manitoba.',
  [('The Red River Resistance was led primarily by ___.', ['Louis Riel and the Métis', 'John A. Macdonald and the federal government', 'A group unrelated to the Red River Resistance', 'British colonial troops'], 0),
   ('The Red River Resistance occurred in response to ___.', ['Canada’s plan to annex the Red River Settlement without consulting its residents', 'A request from the Métis to join the United States', 'A cause unrelated to the Red River Resistance', 'A dispute over fishing rights on the Atlantic coast'], 0),
   ('The Red River Resistance took place in ___.', ['1869-70', '1885', 'A time period unrelated to the Red River Resistance', '1812'], 0),
   ('A key result of the Red River Resistance was ___.', ['The creation of the province of Manitoba', 'The permanent removal of all Métis rights', 'A result unrelated to the Red River Resistance', 'Canada’s decision to abandon westward expansion entirely'], 0),
   ('Why is the Red River Resistance considered a significant event in Canadian history?', ['It demonstrated the Métis Nation’s determination to protect their land and rights', 'It had no lasting influence on Canadian history', 'A reason unrelated to its historical significance', 'It resulted in no negotiations or political change of any kind'], 0)])]),
day(62, [
L('Writing: The Compare-and-Contrast Essay',
  'Grade 8 Writing strand: a compare-and-contrast essay examines the similarities and differences between two subjects, organized using either a point-by-point or block structure to help readers see clear connections.',
  [('A compare-and-contrast essay examines ___.', ['The similarities and differences between two subjects', 'Only the similarities between two subjects, with no differences', 'A concept unrelated to this essay type', 'A single subject with no comparison involved'], 0),
   ('In a block structure compare-and-contrast essay, a writer ___.', ['Discusses all points about the first subject, then all points about the second', 'Alternates between subjects for every single point', 'A concept unrelated to essay structure', 'Discusses only one subject for the entire essay'], 0),
   ('In a point-by-point structure compare-and-contrast essay, a writer ___.', ['Alternates between both subjects for each point of comparison', 'Discusses one subject completely before mentioning the other at all', 'A concept unrelated to essay structure', 'Never directly compares the two subjects'], 0),
   ('Which transition word signals a similarity in a compare-and-contrast essay?', ['Likewise', 'However', 'A word unrelated to transitions', 'Although'], 0),
   ('Why might a writer choose a point-by-point structure over a block structure?', ['It allows readers to see direct comparisons on each point immediately', 'Point-by-point structure always confuses readers with no benefit', 'A reason unrelated to essay structure', 'Block structure and point-by-point structure are always identical'], 0)]),
M('Statistics: Mean, Median, Mode, and Range',
  'Grade 8 Math strand: mean, median, and mode are measures of central tendency that describe a typical value in a data set, while range describes the spread between the highest and lowest values.',
  [('The mean of a data set is calculated by ___.', ['Adding all the values and dividing by the number of values', 'Selecting only the highest value in the set', 'A concept unrelated to measures of central tendency', 'Selecting the value that appears most often'], 0),
   ('The median of a data set is ___.', ['The middle value when the data is arranged in order', 'The value that appears most frequently', 'A concept unrelated to measures of central tendency', 'The difference between the highest and lowest values'], 0),
   ('The mode of a data set is ___.', ['The value that appears most frequently', 'The middle value when the data is arranged in order', 'A concept unrelated to measures of central tendency', 'The sum of all values divided by the count'], 0),
   ('Find the range of this data set: 4, 9, 15, 22, 30.', ['26', '15', 'A value unrelated to the calculation', '30'], 0),
   ('Why might an outlier significantly affect the mean of a data set but not the median?', ['An extreme value changes the sum used in the mean, while the median depends only on order', 'Outliers never have any effect on the mean or the median', 'A reason unrelated to outliers', 'The median always changes more than the mean when an outlier is present'], 0)]),
Sc('Water Systems: Groundwater and Aquifers',
   'Grade 8 Science strand: groundwater is water stored beneath Earth’s surface in soil and rock, and an aquifer is a layer of permeable rock or sediment that can store and transmit significant amounts of groundwater.',
   [('Groundwater is water that is stored ___.', ['Beneath Earth’s surface in soil and rock', 'Only in rivers and lakes above the surface', 'A concept unrelated to groundwater', 'Exclusively inside glaciers and ice caps'], 0),
    ('An aquifer is best described as ___.', ['A layer of permeable rock or sediment that stores and transmits groundwater', 'A completely solid layer of rock through which no water can pass', 'A concept unrelated to aquifers', 'A large body of water located entirely above ground'], 0),
    ('The water table refers to ___.', ['The upper boundary of the saturated zone underground', 'The surface of a lake or river', 'A concept unrelated to the water table', 'A device used to measure rainfall'], 0),
    ('How does water typically enter an aquifer?', ['It infiltrates the ground and percolates downward through permeable layers', 'It flows directly from the ocean at high speed', 'A process unrelated to aquifers', 'It is pumped in artificially at all times'], 0),
    ('Why might overuse of groundwater from an aquifer be a concern?', ['It can be depleted faster than it naturally recharges, causing long-term shortages', 'Aquifers recharge instantly with no possibility of depletion', 'A reason unrelated to groundwater', 'Groundwater use has no effect on aquifer levels'], 0)]),
H('The Canadian Pacific Railway and Nation-Building',
  'Grade 8 History strand: completed in 1885, the Canadian Pacific Railway connected the country from coast to coast, fulfilling a promise made to British Columbia and relying heavily on the labour of Chinese workers who faced dangerous conditions and discrimination.',
  [('The Canadian Pacific Railway was completed in ___.', ['1885', '1867', 'A year unrelated to the Canadian Pacific Railway', '1914'], 0),
   ('The completion of the Canadian Pacific Railway fulfilled a promise made to ___.', ['British Columbia, to join Confederation', 'The United States, to share a rail line', 'A promise unrelated to the Canadian Pacific Railway', 'France, to maintain trade routes'], 0),
   ('Which group of workers played a major role in building the Canadian Pacific Railway, often under dangerous conditions?', ['Chinese labourers', 'Only salaried government engineers', 'A group unrelated to the Canadian Pacific Railway', 'Volunteer workers from Europe with equal pay to others'], 0),
   ('The Canadian Pacific Railway helped unify Canada by ___.', ['Connecting the country from coast to coast', 'Dividing the provinces into separate, disconnected regions', 'A result unrelated to the Canadian Pacific Railway', 'Preventing any further westward settlement'], 0),
   ('Why is the treatment of Chinese railway workers an important part of understanding the Canadian Pacific Railway’s history?', ['It reveals the discrimination and hardship faced by workers who helped build the nation', 'Chinese workers faced no hardship or discrimination while building the railway', 'A reason unrelated to this history', 'Their contribution had no connection to the railway’s completion'], 0)])]),
day(63, [
L('Grammar: Conditional Sentences and Subjunctive Mood',
  'Grade 8 Language strand: conditional sentences express a condition and its result using if-clauses, and the subjunctive mood expresses wishes, hypothetical situations, or statements contrary to fact.',
  [('A conditional sentence expresses ___.', ['A condition and its result, often using an if-clause', 'A statement with no possible condition attached', 'A concept unrelated to conditional sentences', 'A command with no connection to any condition'], 0),
   ('The subjunctive mood is used to express ___.', ['Wishes, hypothetical situations, or statements contrary to fact', 'Only statements that are completely factual and certain', 'A concept unrelated to the subjunctive mood', 'Commands given directly to another person'], 0),
   ('Which sentence correctly uses the subjunctive mood?', ['If I were taller, I would join the team.', 'If I was taller, I would join the team.', 'A sentence unrelated to the subjunctive mood', 'If I am taller, I would join the team.'], 0),
   ('In the sentence “If it rains, we will cancel the picnic,” the if-clause states ___.', ['The condition that must occur for the result to happen', 'The result of an already completed action', 'A concept unrelated to conditional sentences', 'A wish that is impossible to fulfil'], 0),
   ('Why is understanding conditional sentences useful in formal writing?', ['It allows a writer to clearly express cause-and-effect relationships and hypothetical outcomes', 'Conditional sentences have no real use in formal writing', 'A reason unrelated to grammar', 'Every sentence must contain a conditional clause'], 0)]),
M('Algebra: Solving Absolute Value Equations',
  'Grade 8 Math strand (pre-high-school extension): an absolute value equation can have two possible solutions, since the expression inside the absolute value bars can be either positive or negative and still produce the same result.',
  [('The absolute value of a number represents ___.', ['Its distance from zero on a number line, always expressed as positive', 'The number itself, whether positive or negative', 'A concept unrelated to absolute value', 'Only negative numbers on a number line'], 0),
   ('An absolute value equation can have ___ solutions.', ['Two possible', 'Exactly zero, always', 'A number of solutions unrelated to absolute value equations', 'Exactly one, always'], 0),
   ('Solve for x: |x| = 7.', ['x = 7 or x = -7', 'x = 7 only', 'A value unrelated to the calculation', 'x = -7 only'], 0),
   ('Solve for x: |x - 3| = 5.', ['x = 8 or x = -2', 'x = 8 only', 'A value unrelated to the calculation', 'x = 2 or x = -8'], 0),
   ('Why must both a positive and negative case be considered when solving an absolute value equation?', ['Because the expression inside the bars could equal either the positive or negative value', 'Absolute value equations never require considering more than one case', 'A reason unrelated to absolute value equations', 'The negative case is always impossible and can be ignored'], 0)]),
Sc('Water Systems: Water Pollution and Conservation',
   'Grade 8 Science strand: water pollution occurs when harmful substances such as chemicals, waste, or excess nutrients enter water systems, and conservation practices like reducing water use and preventing runoff help protect water quality.',
   [('Water pollution occurs when ___.', ['Harmful substances enter water systems and degrade their quality', 'Water systems remain completely free of any outside substances', 'A concept unrelated to water pollution', 'Water naturally purifies itself with no outside factors involved'], 0),
    ('Which of these is a common source of water pollution?', ['Agricultural runoff containing fertilizers and pesticides', 'Rainfall collecting in a clean reservoir', 'A source unrelated to water pollution', 'Water evaporating from a lake on a hot day'], 0),
    ('Excess nutrients in a lake, such as from fertilizer runoff, can cause ___.', ['Algal blooms that deplete oxygen and harm aquatic life', 'Immediate improvement in water clarity and quality', 'A result unrelated to water pollution', 'A permanent increase in fish populations with no negative effects'], 0),
    ('Which of these is an effective water conservation practice?', ['Fixing leaky faucets and taking shorter showers', 'Leaving taps running continuously throughout the day', 'A practice unrelated to water conservation', 'Increasing the use of fertilizers near waterways'], 0),
    ('Why is protecting water quality important for both ecosystems and human communities?', ['Clean water supports aquatic life and is essential for drinking, agriculture, and health', 'Water quality has no connection to ecosystems or human health', 'A reason unrelated to water systems', 'Polluted water has no effect on the organisms that depend on it'], 0)]),
H('Residential Schools and Their Legacy',
  'Grade 8 History strand: residential schools were government-funded, church-run institutions that forcibly separated Indigenous children from their families in an effort to assimilate them, causing lasting intergenerational harm that Canada continues to address through truth and reconciliation efforts.',
  [('Residential schools were institutions that ___.', ['Forcibly separated Indigenous children from their families to assimilate them', 'Were voluntarily attended by Indigenous families with no pressure involved', 'A description unrelated to residential schools', 'Taught only Indigenous languages and traditions with government support'], 0),
   ('Residential schools in Canada were funded by ___.', ['The government and operated in partnership with churches', 'Indigenous communities themselves, with no outside involvement', 'A group unrelated to residential schools', 'International organizations with no connection to Canada'], 0),
   ('The legacy of residential schools includes ___.', ['Lasting intergenerational harm to Indigenous families and communities', 'No lasting effects on Indigenous communities whatsoever', 'A legacy unrelated to residential schools', 'Immediate and complete healing with no ongoing impact'], 0),
   ('What has Canada undertaken in recent years to address the legacy of residential schools?', ['Truth and reconciliation efforts, including formal apologies and commissions', 'A complete refusal to acknowledge that residential schools existed', 'An action unrelated to reconciliation efforts', 'A decision to reopen residential schools using the same model'], 0),
   ('Why is learning about residential schools an important part of understanding Canadian history?', ['It helps Canadians understand past injustices and supports ongoing reconciliation', 'This history has no relevance to understanding Canada today', 'A reason unrelated to its historical significance', 'Residential schools are a topic unrelated to Indigenous history'], 0)])]),
day(64, [
L('Media Literacy: Understanding Algorithms and Filter Bubbles',
  'Grade 8 Language strand: online algorithms select and prioritize content based on a user’s past activity, which can create a filter bubble that limits exposure to differing viewpoints and reinforces existing beliefs.',
  [('An online algorithm selects and prioritizes content based on ___.', ['A user’s past activity and preferences', 'A completely random selection with no pattern', 'A concept unrelated to algorithms', 'A fixed list that never changes for any user'], 0),
   ('A filter bubble occurs when ___.', ['A user is repeatedly shown content that reinforces their existing beliefs', 'A user is shown a perfectly balanced range of every possible viewpoint', 'A concept unrelated to filter bubbles', 'All users see identical content regardless of their activity'], 0),
   ('Which is a potential risk of living inside a filter bubble?', ['Reduced exposure to differing perspectives and opinions', 'Guaranteed exposure to every possible viewpoint', 'A risk unrelated to filter bubbles', 'Filter bubbles have no effect on the content people see'], 0),
   ('Why might understanding algorithms help someone evaluate their social media feed?', ['It reveals that the content shown is curated rather than a neutral sample of information', 'Algorithms have no influence on what content a person sees', 'A reason unrelated to media literacy', 'All social media feeds show identical, unfiltered content'], 0),
   ('Which action could help someone break out of a filter bubble?', ['Deliberately seeking out sources with differing perspectives', 'Only interacting with content that confirms existing beliefs', 'An action unrelated to filter bubbles', 'Avoiding all forms of media entirely'], 0)]),
M('Financial Literacy: Currency Exchange and Unit Pricing',
  'Grade 8 Math strand: currency exchange rates determine how much one currency is worth in another, while unit pricing calculates the cost per single unit of an item, helping consumers compare value between different package sizes.',
  [('A currency exchange rate determines ___.', ['How much one currency is worth in terms of another', 'The total amount of money a country has printed', 'A concept unrelated to currency exchange', 'The interest rate charged by a bank'], 0),
   ('Unit pricing calculates ___.', ['The cost per single unit of an item', 'The total cost of an entire package regardless of size', 'A concept unrelated to unit pricing', 'The tax applied to a purchase'], 0),
   ('If 1 CAD = 0.75 USD, how many USD would you receive for 200 CAD?', ['150 USD', '266.67 USD', 'A value unrelated to the calculation', '200 USD'], 0),
   ('A 500 g box of cereal costs 5 dollars, and a 750 g box costs 6 dollars. Which has the lower unit price per gram?', ['The 750 g box', 'The 500 g box', 'A result unrelated to the calculation', 'They have exactly the same unit price'], 0),
   ('Why is unit pricing useful for consumers when shopping?', ['It allows a fair comparison of value between differently sized packages', 'Unit pricing provides no useful information for comparing products', 'A reason unrelated to unit pricing', 'Larger packages are always the better value regardless of price'], 0)]),
Sc('Water Systems: Water Treatment and Purification Technology',
   'Grade 8 Science strand: water treatment facilities use processes such as filtration, sedimentation, and disinfection to remove contaminants and make water safe for drinking and other uses.',
   [('Filtration in water treatment involves ___.', ['Passing water through materials that remove suspended particles', 'Adding contaminants directly into the water supply', 'A process unrelated to filtration', 'Heating water until it completely evaporates'], 0),
    ('Sedimentation in water treatment allows ___.', ['Heavier particles to settle to the bottom of a container over time', 'All particles to remain suspended evenly throughout the water', 'A process unrelated to sedimentation', 'Water to instantly become completely pure with no further steps'], 0),
    ('Disinfection in water treatment is used to ___.', ['Kill or inactivate harmful microorganisms in the water', 'Add more microorganisms to the water supply', 'A process unrelated to disinfection', 'Remove all minerals from the water permanently'], 0),
    ('Which of these is commonly used as a disinfectant in municipal water treatment?', ['Chlorine', 'Table salt', 'A substance unrelated to water treatment', 'Vegetable oil'], 0),
    ('Why are multiple stages, such as filtration, sedimentation, and disinfection, used in water treatment?', ['Each stage removes different types of contaminants, resulting in safer water overall', 'A single stage always removes every possible contaminant', 'A reason unrelated to water treatment', 'Additional stages have no effect on water safety'], 0)]),
H('The Sixties Scoop',
  'Grade 8 History strand: the Sixties Scoop refers to the mass removal of Indigenous children from their families by child welfare authorities, beginning in the 1960s, and placing them into non-Indigenous foster or adoptive homes, often severing ties to their culture and identity.',
  [('The Sixties Scoop refers to ___.', ['The mass removal of Indigenous children from their families by child welfare authorities', 'A government program that returned Indigenous children to their families', 'A description unrelated to the Sixties Scoop', 'A voluntary relocation chosen by Indigenous families'], 0),
   ('The Sixties Scoop began primarily in the ___.', ['1960s', '1920s', 'A time period unrelated to the Sixties Scoop', '1990s'], 0),
   ('Children removed during the Sixties Scoop were typically placed into ___.', ['Non-Indigenous foster or adoptive homes', 'Homes within their own Indigenous communities', 'A placement unrelated to the Sixties Scoop', 'Government-run boarding schools exclusively'], 0),
   ('A significant effect of the Sixties Scoop on affected children was ___.', ['The severing of ties to their Indigenous culture and identity', 'A strengthened connection to their Indigenous culture and identity', 'An effect unrelated to the Sixties Scoop', 'No effect on their sense of identity at all'], 0),
   ('Why is the Sixties Scoop often discussed alongside residential schools in Canadian history?', ['Both involved the separation of Indigenous children from their families and culture', 'The two events have no connection to one another', 'A reason unrelated to Indigenous history', 'Only residential schools affected Indigenous children’s identity'], 0)])]),
day(65, [
L('Reading: Analyzing Allegory',
  'Grade 8 Reading strand: an allegory is a narrative in which characters, settings, and events symbolically represent a deeper moral, political, or social meaning beyond the literal story.',
  [('An allegory is a narrative in which ___.', ['Characters and events symbolically represent a deeper meaning', 'Every character and event should be read only literally', 'A concept unrelated to allegory', 'A story contains absolutely no symbolic meaning at all'], 0),
   ('Allegories are often used to convey ___.', ['A moral, political, or social message', 'No message of any kind', 'A concept unrelated to allegory', 'Only factual, historical information with no deeper meaning'], 0),
   ('Why might an author choose to write an allegory instead of stating a message directly?', ['It allows readers to engage with complex ideas through story and symbolism', 'Allegories always make a message harder to understand for no reason', 'A reason unrelated to allegory', 'Direct statements are always more powerful than allegorical stories'], 0),
   ('In an allegorical story, a character representing greed would likely ___.', ['Make choices driven by a desire for wealth or possessions', 'Make choices with no connection to any theme', 'A concept unrelated to allegory', 'Represent kindness and generosity throughout the story'], 0),
   ('Why is background knowledge often helpful when interpreting an allegory?', ['It can reveal the historical or social context the symbolic story is commenting on', 'Background knowledge never affects how an allegory is understood', 'A reason unrelated to reading comprehension', 'Allegories require no interpretation of any kind'], 0)]),
M('Probability: Theoretical vs Experimental Probability',
  'Grade 8 Math strand: theoretical probability is calculated using known possible outcomes, while experimental probability is calculated from the actual results of repeated trials, and the two often converge as the number of trials increases.',
  [('Theoretical probability is calculated using ___.', ['The known possible outcomes of an event', 'The actual results collected from repeated trials', 'A concept unrelated to theoretical probability', 'A random guess with no calculation involved'], 0),
   ('Experimental probability is calculated using ___.', ['The actual results collected from repeated trials', 'Only the known possible outcomes of an event', 'A concept unrelated to experimental probability', 'A value that never changes no matter how many trials occur'], 0),
   ('The theoretical probability of rolling a 4 on a standard six-sided die is ___.', ['1/6', '1/4', 'A value unrelated to the calculation', '4/6'], 0),
   ('If a coin is flipped 50 times and lands on heads 28 times, the experimental probability of heads is ___.', ['28/50', '1/2', 'A value unrelated to the calculation', '22/50'], 0),
   ('Why might experimental probability differ from theoretical probability in a small number of trials?', ['Random chance can cause actual results to vary from expected outcomes in the short term', 'Experimental and theoretical probability are always exactly identical', 'A reason unrelated to probability', 'Theoretical probability changes based on the number of trials conducted'], 0)]),
Sc('Systems in Action: Simple Machines and Mechanical Advantage',
   'Grade 8 Science strand: a simple machine, such as a lever, pulley, or inclined plane, makes work easier by changing the amount or direction of force needed, and mechanical advantage compares the output force to the input force.',
   [('A simple machine makes work easier by ___.', ['Changing the amount or direction of force needed', 'Eliminating the need for any force entirely', 'A concept unrelated to simple machines', 'Always requiring more force than doing the task by hand'], 0),
    ('Mechanical advantage compares ___.', ['The output force of a machine to the input force applied', 'The colour of a machine to its size', 'A concept unrelated to mechanical advantage', 'The weight of a machine to its cost'], 0),
    ('Which of these is an example of a simple machine?', ['A lever', 'A smartphone', 'A device unrelated to simple machines', 'A television'], 0),
    ('An inclined plane makes moving a heavy object easier by ___.', ['Allowing the force to be applied over a longer distance', 'Increasing the object’s actual weight', 'A concept unrelated to inclined planes', 'Requiring the object to be lifted straight up with no assistance'], 0),
    ('Why might engineers combine multiple simple machines into a compound machine?', ['To achieve a greater mechanical advantage or perform a more complex task', 'Combining simple machines always reduces their overall usefulness', 'A reason unrelated to mechanical systems', 'Compound machines can never accomplish more than a single simple machine'], 0)]),
H('Pier 21 and Post-War Immigration to Canada',
  'Grade 8 History strand: Pier 21 in Halifax served as a major immigration gateway to Canada from 1928 to 1971, welcoming hundreds of thousands of newcomers, especially refugees and immigrants arriving after the Second World War.',
  [('Pier 21 was located in ___.', ['Halifax', 'Toronto', 'A city unrelated to Pier 21', 'Vancouver'], 0),
   ('Pier 21 served as a major immigration gateway to Canada between ___.', ['1928 and 1971', '1867 and 1900', 'A time period unrelated to Pier 21', '1980 and 2000'], 0),
   ('Many newcomers who arrived through Pier 21 after the Second World War were ___.', ['Refugees and immigrants seeking a new life in Canada', 'Exclusively tourists visiting for a short stay', 'A group unrelated to Pier 21', 'Government officials with no connection to immigration'], 0),
   ('Pier 21 is significant in Canadian history because it ___.', ['Welcomed hundreds of thousands of immigrants, shaping Canada’s post-war population', 'Prevented any immigration to Canada during this period', 'A reason unrelated to its historical significance', 'Was used only for exporting goods, with no connection to immigration'], 0),
   ('Why is Pier 21 today commemorated as a national museum?', ['To preserve the history and stories of the immigrants who passed through it', 'To celebrate a location with no historical importance to Canada', 'A reason unrelated to Pier 21', 'Because it has no connection to Canadian immigration history'], 0)])]),
day(66, [
L('Writing: The Cover Letter and Resume',
  'Grade 8 Writing strand: a resume summarizes a person’s skills, experience, and education in a structured format, while a cover letter introduces the applicant and explains why they are suited to a specific opportunity.',
  [('A resume is a document that summarizes ___.', ['A person’s skills, experience, and education', 'Only a person’s personal opinions with no factual information', 'A concept unrelated to resumes', 'A completely fictional account of a person’s life'], 0),
   ('A cover letter is written to ___.', ['Introduce the applicant and explain why they are suited to an opportunity', 'Replace the need for a resume entirely', 'A concept unrelated to cover letters', 'List a person’s skills in a structured table with no explanation'], 0),
   ('Which of these would typically appear on a resume?', ['A list of relevant skills and past experiences', 'A detailed story about an unrelated childhood memory', 'A concept unrelated to resumes', 'A persuasive argument with no factual information'], 0),
   ('Why is it important to tailor a cover letter to a specific opportunity?', ['It shows the reader how the applicant’s skills connect directly to that role', 'Tailoring a cover letter never affects how it is received', 'A reason unrelated to cover letters', 'A single generic cover letter is always the most effective approach'], 0),
   ('Why might a resume use bullet points rather than full paragraphs?', ['It allows a reader to quickly scan key information', 'Bullet points always make information harder to read', 'A reason unrelated to resumes', 'Full paragraphs are required on every resume'], 0)]),
M('Algebra: Solving Literal Equations (Formulas)',
  'Grade 8 Math strand (pre-high-school extension): a literal equation contains multiple variables, and solving it for a specific variable involves isolating that variable using the same inverse operations used in solving numerical equations.',
  [('A literal equation is an equation that contains ___.', ['Multiple variables, often representing a formula', 'Only a single numerical value with no variables', 'A concept unrelated to literal equations', 'No variables of any kind'], 0),
   ('Solving a literal equation for a specific variable involves ___.', ['Isolating that variable using inverse operations', 'Ignoring all other variables in the equation entirely', 'A concept unrelated to literal equations', 'Replacing every variable with a fixed number'], 0),
   ('Solve the formula for length: A = lw, for l.', ['l = A/w', 'l = A - w', 'A value unrelated to the calculation', 'l = Aw'], 0),
   ('Solve the formula for temperature conversion for C: F = (9/5)C + 32.', ['C = (5/9)(F - 32)', 'C = (9/5)(F - 32)', 'A value unrelated to the calculation', 'C = (5/9)F + 32'], 0),
   ('Why is it useful to rearrange a formula to solve for a different variable?', ['It allows a specific unknown value to be calculated directly when others are known', 'Rearranging a formula never changes how it can be used', 'A reason unrelated to literal equations', 'Formulas can only ever be solved for the original isolated variable'], 0)]),
Sc('Matter and Energy: Density and Buoyancy (Archimedes’ Principle)',
   'Grade 8 Science strand: density is the amount of mass contained in a given volume, and Archimedes’ principle explains that an object floats or sinks depending on whether it displaces a weight of fluid greater than, equal to, or less than its own weight.',
   [('Density is best described as ___.', ['The amount of mass contained in a given volume', 'The total weight of an object regardless of its size', 'A concept unrelated to density', 'The temperature of an object’s surroundings'], 0),
    ('An object will float in water if its density is ___.', ['Less than the density of water', 'Greater than the density of water', 'A concept unrelated to buoyancy', 'Exactly equal to the density of air'], 0),
    ('Archimedes’ principle states that the buoyant force on an object equals ___.', ['The weight of the fluid the object displaces', 'The total weight of the object itself', 'A concept unrelated to Archimedes’ principle', 'Zero, regardless of the object’s size or shape'], 0),
    ('Why can a large steel ship float, even though steel is denser than water?', ['Its overall shape displaces enough water to support its weight', 'Steel is actually less dense than water in every situation', 'A reason unrelated to buoyancy', 'Ships never displace any water while floating'], 0),
    ('Why is understanding density and buoyancy important when designing submarines?', ['Submarines must control their density to rise, sink, or remain at a steady depth', 'Density and buoyancy have no connection to submarine design', 'A reason unrelated to matter and energy', 'Submarines always float regardless of their density'], 0)]),
H('The Patriation of the Constitution and the Charter of Rights and Freedoms',
  'Grade 8 History strand: in 1982, Canada patriated its Constitution, gaining full authority to amend it without approval from Britain, and simultaneously introduced the Canadian Charter of Rights and Freedoms, guaranteeing fundamental rights to all Canadians.',
  [('Patriating the Constitution in 1982 meant that Canada ___.', ['Gained full authority to amend its own Constitution without approval from Britain', 'Lost all authority to make changes to its own laws', 'A meaning unrelated to patriation', 'Became a colony of Britain once again'], 0),
   ('The Canadian Charter of Rights and Freedoms was introduced in ___.', ['1982', '1867', 'A year unrelated to the Charter of Rights and Freedoms', '1950'], 0),
   ('The Charter of Rights and Freedoms guarantees ___.', ['Fundamental rights and freedoms to all Canadians', 'Rights only to citizens holding a specific political office', 'A concept unrelated to the Charter of Rights and Freedoms', 'No legal protections of any kind'], 0),
   ('Before patriation, amendments to Canada’s Constitution required approval from ___.', ['The British Parliament', 'The United Nations', 'A body unrelated to patriation', 'The United States government'], 0),
   ('Why is the introduction of the Charter of Rights and Freedoms considered a landmark moment in Canadian history?', ['It formally enshrined fundamental rights and freedoms into Canada’s highest law', 'It removed all legal rights previously held by Canadians', 'A reason unrelated to its historical significance', 'It had no lasting impact on Canadian law or society'], 0)])]),
day(67, [
L('Vocabulary: Idioms and Figurative Expressions',
  'Grade 8 Language strand: an idiom is a phrase whose meaning cannot be understood from the literal definitions of its individual words, and recognizing idioms supports fluent reading and clear communication.',
  [('An idiom is a phrase whose meaning ___.', ['Cannot be understood from the literal definitions of its individual words', 'Is always identical to its literal, word-for-word meaning', 'A concept unrelated to idioms', 'Never appears in everyday spoken or written language'], 0),
   ('What does the idiom “break the ice” mean?', ['To ease tension or begin a conversation in a new social situation', 'To literally shatter a piece of ice', 'A concept unrelated to idioms', 'To end a friendship permanently'], 0),
   ('What does the idiom “under the weather” mean?', ['Feeling ill or unwell', 'Standing outside during a storm', 'A concept unrelated to idioms', 'Feeling extremely happy and energetic'], 0),
   ('Why can idioms be challenging for readers learning a new language?', ['Their meaning cannot be determined by translating each word literally', 'Idioms always have an obvious, literal meaning', 'A reason unrelated to idioms', 'Idioms are never used in everyday conversation'], 0),
   ('Why is recognizing idioms useful when reading a novel with informal dialogue?', ['It helps a reader understand the intended meaning behind a character’s words', 'Idioms never affect how dialogue is interpreted', 'A reason unrelated to reading comprehension', 'All dialogue in novels is written only in literal language'], 0)]),
M('Geometry: Congruence and Geometric Constructions',
  'Grade 8 Math strand: congruent figures have exactly the same size and shape, and geometric constructions use tools such as a compass and straightedge to accurately create congruent segments, angles, and bisectors.',
  [('Two figures are congruent if they have ___.', ['Exactly the same size and shape', 'The same shape but different sizes', 'A concept unrelated to congruence', 'The same size but different shapes'], 0),
   ('A geometric construction traditionally uses ___.', ['A compass and straightedge', 'A calculator and protractor only', 'A set of tools unrelated to geometric constructions', 'No tools of any kind'], 0),
   ('A perpendicular bisector divides a line segment into ___.', ['Two equal parts at a 90-degree angle', 'Three unequal parts at a random angle', 'A result unrelated to perpendicular bisectors', 'Two unequal parts at a 45-degree angle'], 0),
   ('An angle bisector divides an angle into ___.', ['Two congruent angles', 'Three congruent angles', 'A result unrelated to angle bisectors', 'Two angles of different measures'], 0),
   ('Why are precise geometric constructions important in fields like architecture and engineering?', ['They ensure measurements and shapes are accurate and consistent', 'Precise constructions have no real-world importance', 'A reason unrelated to geometric constructions', 'Architecture and engineering never require any accuracy'], 0)]),
Sc('Chemistry: Acids, Bases, and pH',
   'Grade 8 Science strand: acids and bases are chemical substances with contrasting properties, measured on the pH scale, where values below 7 indicate an acid, values above 7 indicate a base, and 7 is neutral.',
   [('On the pH scale, a value below 7 indicates ___.', ['An acid', 'A base', 'A concept unrelated to the pH scale', 'A completely neutral substance'], 0),
    ('On the pH scale, a value above 7 indicates ___.', ['A base', 'An acid', 'A concept unrelated to the pH scale', 'A substance with no measurable pH'], 0),
    ('Pure water has a pH of approximately ___.', ['7, which is neutral', '0, which is highly acidic', 'A value unrelated to the pH scale', '14, which is highly basic'], 0),
    ('Which of these is a common example of an acid?', ['Lemon juice', 'Baking soda', 'A substance unrelated to acids and bases', 'Soap'], 0),
    ('Why is testing the pH of soil or water important in agriculture and environmental science?', ['It helps determine whether conditions are suitable for specific plants or organisms', 'pH has no effect on plant growth or environmental conditions', 'A reason unrelated to chemistry', 'All soil and water naturally have the exact same pH'], 0)]),
H('The Canadian Bill of Rights of 1960',
  'Grade 8 History strand: the Canadian Bill of Rights, passed in 1960, was the country’s first federal law to formally protect fundamental rights and freedoms, though it applied only to federal law and lacked the constitutional authority later given to the Charter.',
  [('The Canadian Bill of Rights was passed in ___.', ['1960', '1982', 'A year unrelated to the Canadian Bill of Rights', '1867'], 0),
   ('The Canadian Bill of Rights was significant because it was ___.', ['The country’s first federal law to formally protect fundamental rights and freedoms', 'The first law in Canadian history of any kind', 'A description unrelated to the Canadian Bill of Rights', 'A law that eliminated all previously existing rights'], 0),
   ('A key limitation of the Canadian Bill of Rights was that it ___.', ['Applied only to federal law, not provincial law', 'Applied equally and automatically to every level of government', 'A limitation unrelated to the Canadian Bill of Rights', 'Had no limitations of any kind'], 0),
   ('Compared to the Canadian Bill of Rights, the Charter of Rights and Freedoms has ___.', ['Greater constitutional authority and broader legal protection', 'Exactly the same legal authority with no differences', 'A comparison unrelated to these two documents', 'Less legal authority than the Bill of Rights'], 0),
   ('Why is the Canadian Bill of Rights often viewed as a precursor to the Charter of Rights and Freedoms?', ['It represented an early step toward formally protecting rights before the Charter expanded those protections', 'It has no historical connection to the later Charter of Rights and Freedoms', 'A reason unrelated to its historical significance', 'It was created after the Charter and had no influence on it'], 0)])]),
day(68, [
L('Reading: Graphic Novels and Visual Storytelling',
  'Grade 8 Reading strand: a graphic novel tells a story through a combination of images and text, using panels, gutters, and visual cues to convey action, emotion, and the passage of time.',
  [('A graphic novel tells a story through ___.', ['A combination of images and text', 'Text alone, with no images included', 'A concept unrelated to graphic novels', 'Images alone, with no text of any kind'], 0),
   ('In a graphic novel, a panel is best described as ___.', ['A single framed image representing one moment in the story', 'The blank space between two images', 'A concept unrelated to graphic novels', 'The title printed on the cover of the book'], 0),
   ('In a graphic novel, the gutter refers to ___.', ['The space between panels', 'The main character of the story', 'A concept unrelated to graphic novels', 'The text found inside a speech bubble'], 0),
   ('Why might a graphic novel use varying panel sizes throughout a story?', ['To emphasize important moments or control the pacing of the narrative', 'Panel size never has any effect on how a story is read', 'A reason unrelated to visual storytelling', 'Every panel in a graphic novel must be exactly the same size'], 0),
   ('Why can visual storytelling in a graphic novel convey emotion effectively?', ['Facial expressions, colour, and imagery can communicate feeling without relying only on words', 'Graphic novels are unable to convey any emotion at all', 'A reason unrelated to visual storytelling', 'Only written dialogue can ever communicate a character’s emotions'], 0)]),
M('Geometry: Tessellations and Symmetry',
  'Grade 8 Math strand: a tessellation is a repeating pattern of shapes that covers a plane with no gaps or overlaps, and symmetry describes how a shape can be reflected, rotated, or translated while still appearing unchanged.',
  [('A tessellation is a repeating pattern of shapes that ___.', ['Covers a plane with no gaps or overlaps', 'Always leaves gaps between each shape', 'A concept unrelated to tessellations', 'Uses only a single shape placed one time'], 0),
   ('Which regular polygon can tessellate a plane on its own?', ['A square', 'A regular pentagon', 'A shape unrelated to tessellations', 'A regular heptagon'], 0),
   ('A shape has line symmetry if ___.', ['It can be folded along a line so both halves match exactly', 'It looks completely different after being folded in half', 'A concept unrelated to symmetry', 'It has no possible line of symmetry at all'], 0),
   ('Rotational symmetry occurs when a shape ___.', ['Can be rotated around a central point and still look the same', 'Can never be rotated without changing its appearance', 'A concept unrelated to rotational symmetry', 'Has no central point of any kind'], 0),
   ('Why might tessellations be used in art and design, such as in the work of M.C. Escher?', ['They create visually striking, seamless repeating patterns', 'Tessellations have no practical use in art or design', 'A reason unrelated to tessellations', 'Tessellations always leave large gaps in a pattern'], 0)]),
Sc('Chemistry: Chemical vs Physical Changes',
   'Grade 8 Science strand: a physical change alters the form or appearance of a substance without changing its chemical composition, while a chemical change produces a new substance with different properties.',
   [('A physical change alters ___.', ['The form or appearance of a substance without changing its chemical composition', 'The chemical composition of a substance into an entirely new substance', 'A concept unrelated to physical changes', 'Nothing at all about a substance'], 0),
    ('A chemical change results in ___.', ['A new substance with different properties than the original', 'The exact same substance with no properties changed', 'A concept unrelated to chemical changes', 'Only a change in the temperature of a substance'], 0),
    ('Which of these is an example of a physical change?', ['Melting an ice cube into water', 'Rusting of iron', 'A change unrelated to physical vs chemical changes', 'Burning a piece of paper'], 0),
    ('Which of these is an example of a chemical change?', ['Burning wood into ash and smoke', 'Cutting a piece of paper into smaller pieces', 'A change unrelated to physical vs chemical changes', 'Freezing liquid water into ice'], 0),
    ('Which of these is a reliable sign that a chemical change has occurred?', ['The production of gas bubbles, a colour change, or a new odour', 'An object simply changing shape with no other effects', 'A sign unrelated to chemical changes', 'A substance returning to its original form with no lasting change'], 0)]),
H('The Statute of Westminster and Canadian Autonomy',
  'Grade 8 History strand: the Statute of Westminster of 1931 granted Canada and other British dominions full legal independence from Britain in most matters, marking a major step toward Canadian sovereignty while still allowing ties to the monarchy to continue.',
  [('The Statute of Westminster was passed in ___.', ['1931', '1867', 'A year unrelated to the Statute of Westminster', '1982'], 0),
   ('The Statute of Westminster granted Canada ___.', ['Full legal independence from Britain in most matters', 'Complete separation from the British monarchy', 'A concept unrelated to the Statute of Westminster', 'No additional legal authority of any kind'], 0),
   ('The Statute of Westminster applied to Canada and ___.', ['Other British dominions', 'Only countries outside the British Empire', 'A group unrelated to the Statute of Westminster', 'The United States exclusively'], 0),
   ('After the Statute of Westminster, Canada could ___.', ['Pass its own laws without approval from the British Parliament', 'No longer pass any laws of its own', 'A result unrelated to the Statute of Westminster', 'Only pass laws related to trade'], 0),
   ('Why is the Statute of Westminster considered a major milestone in Canadian sovereignty?', ['It marked a significant step toward Canada governing itself independently', 'It had no effect on Canada’s relationship with Britain', 'A reason unrelated to its historical significance', 'It returned more legal authority to Britain rather than to Canada'], 0)])]),
day(69, [
L('Grammar: Transitional Words and Cohesion',
  'Grade 8 Language strand: transitional words and phrases connect ideas within and between sentences, creating cohesion that helps a reader follow the logical flow of a piece of writing.',
  [('Transitional words and phrases function to ___.', ['Connect ideas within and between sentences', 'Separate every sentence with no connection at all', 'A concept unrelated to transitions', 'Replace the need for punctuation entirely'], 0),
   ('Which transition word signals a contrast between two ideas?', ['However', 'Furthermore', 'A word unrelated to transitions', 'Similarly'], 0),
   ('Which transition word signals a cause-and-effect relationship?', ['Therefore', 'Meanwhile', 'A word unrelated to transitions', 'In contrast'], 0),
   ('A piece of writing with strong cohesion ___.', ['Flows logically, helping the reader follow the connections between ideas', 'Contains ideas with no logical connection to one another', 'A concept unrelated to cohesion', 'Never uses any transitional words or phrases'], 0),
   ('Why might a writer revise a paragraph to add transitional words?', ['To make the relationships between ideas clearer for the reader', 'Transitional words always make a paragraph more confusing', 'A reason unrelated to revising writing', 'Cohesion has no impact on how a reader understands a text'], 0)]),
M('Data Management: Box-and-Whisker Plots',
  'Grade 8 Math strand: a box-and-whisker plot displays the distribution of a data set using five key values — minimum, first quartile, median, third quartile, and maximum — making it easy to visualize spread and identify outliers.',
  [('A box-and-whisker plot displays a data set using ___.', ['Five key values, including the minimum, quartiles, median, and maximum', 'Only a single average value with no other information', 'A concept unrelated to box-and-whisker plots', 'Every individual data point with no summary values'], 0),
   ('In a box-and-whisker plot, the line inside the box represents ___.', ['The median of the data set', 'The minimum value of the data set', 'A concept unrelated to box-and-whisker plots', 'The maximum value of the data set'], 0),
   ('The whiskers of a box-and-whisker plot extend to ___.', ['The minimum and maximum values of the data set', 'Only the first and third quartiles', 'A concept unrelated to box-and-whisker plots', 'The mean of the data set only'], 0),
   ('The interquartile range is calculated as ___.', ['The third quartile minus the first quartile', 'The maximum value minus the minimum value', 'A concept unrelated to interquartile range', 'The median minus the mean'], 0),
   ('Why are box-and-whisker plots useful for comparing two data sets?', ['They make it easy to visually compare spread, median, and potential outliers', 'Box-and-whisker plots provide no useful information for comparison', 'A reason unrelated to box-and-whisker plots', 'They can only display a single data set at a time with no comparison possible'], 0)]),
Sc('Astronomy: The Solar System and Planetary Motion',
   'Grade 8 Science strand: the solar system consists of the Sun and the objects that orbit it, including planets held in elliptical orbits by the Sun’s gravitational pull, with orbital period increasing as distance from the Sun increases.',
   [('The solar system consists of the Sun and ___.', ['The objects, including planets, that orbit it', 'Only the stars located outside our galaxy', 'A concept unrelated to the solar system', 'A single planet with no other orbiting bodies'], 0),
    ('Planets remain in orbit around the Sun primarily due to ___.', ['The Sun’s gravitational pull', 'The complete absence of any force acting on them', 'A cause unrelated to planetary motion', 'Magnetic attraction between planets'], 0),
    ('The shape of a planet’s orbit around the Sun is best described as ___.', ['Elliptical', 'A perfect square', 'A shape unrelated to orbital shape', 'A straight line'], 0),
    ('Compared to planets closer to the Sun, planets farther from the Sun generally have ___.', ['Longer orbital periods', 'Shorter orbital periods', 'A concept unrelated to orbital periods', 'Exactly the same orbital period'], 0),
    ('Why do planets closer to the Sun experience shorter years than planets farther away?', ['They travel a shorter orbital distance and experience a stronger gravitational pull', 'Distance from the Sun has no effect on the length of a planet’s year', 'A reason unrelated to planetary motion', 'Planets closer to the Sun always orbit more slowly than distant planets'], 0)]),
H('Terry Fox and the Marathon of Hope',
  'Grade 8 History strand: in 1980, Terry Fox began the Marathon of Hope, an attempt to run across Canada to raise money and awareness for cancer research after losing his leg to the disease, inspiring a legacy that continues through annual fundraising runs.',
  [('Terry Fox began the Marathon of Hope in ___.', ['1980', '1960', 'A year unrelated to Terry Fox', '2000'], 0),
   ('The purpose of the Marathon of Hope was to ___.', ['Raise money and awareness for cancer research', 'Promote a new sporting event with no charitable purpose', 'A purpose unrelated to the Marathon of Hope', 'Celebrate the anniversary of Confederation'], 0),
   ('Terry Fox began his run after ___.', ['Losing his leg to cancer', 'Winning a national athletic competition', 'An event unrelated to Terry Fox', 'Completing a university degree in medicine'], 0),
   ('Although Terry Fox was unable to complete his run across Canada, his effort ___.', ['Inspired a lasting legacy of annual fundraising runs held in his honour', 'Was quickly forgotten with no lasting impact', 'A result unrelated to his legacy', 'Led to the cancellation of all future cancer research funding'], 0),
   ('Why is Terry Fox remembered as an important figure in Canadian history?', ['His courage and determination inspired ongoing national support for cancer research', 'He has no lasting significance in Canadian history', 'A reason unrelated to his historical significance', 'His actions had no connection to raising awareness for any cause'], 0)])]),
day(70, [
L('Review: Days 61-69 Language Arts',
  'Grade 8 Language strand: this review lesson revisits key ideas from Days 61-69, including foreshadowing and flashback, compare-and-contrast essays, conditional sentences, filter bubbles, allegory, cover letters, idioms, graphic novels, and transitional words.',
  [('Foreshadowing is a literary technique in which ___.', ['An author hints at events that will happen later in the story', 'An author only describes events that already occurred', 'A concept unrelated to literary devices', 'A story never contains any hints about future events'], 0),
   ('A compare-and-contrast essay examines ___.', ['The similarities and differences between two subjects', 'Only the similarities between two subjects, with no differences', 'A concept unrelated to this essay type', 'A single subject with no comparison involved'], 0),
   ('A filter bubble occurs when ___.', ['A user is repeatedly shown content that reinforces their existing beliefs', 'A user is shown a perfectly balanced range of every possible viewpoint', 'A concept unrelated to filter bubbles', 'All users see identical content regardless of their activity'], 0),
   ('An idiom is a phrase whose meaning ___.', ['Cannot be understood from the literal definitions of its individual words', 'Is always identical to its literal, word-for-word meaning', 'A concept unrelated to idioms', 'Never appears in everyday spoken or written language'], 0),
   ('Why is it useful to review reading strategies, writing forms, grammar, and media literacy together?', ['It reinforces how these language and literacy skills connect and support one another', 'These topics have no connection to one another', 'A reason unrelated to reviewing language arts', 'Review never helps strengthen understanding of language skills'], 0)]),
M('Review: Days 61-69 Math Concepts',
  'Grade 8 Math strand review: this lesson revisits the midpoint and distance formulas, measures of central tendency, absolute value equations, theoretical versus experimental probability, and box-and-whisker plots from recent lessons.',
  [('The midpoint formula finds ___.', ['The point exactly halfway between two given coordinates', 'The total distance between two given coordinates', 'A concept unrelated to the midpoint formula', 'The slope of the line connecting two coordinates'], 0),
   ('The mean of a data set is calculated by ___.', ['Adding all the values and dividing by the number of values', 'Selecting only the highest value in the set', 'A concept unrelated to measures of central tendency', 'Selecting the value that appears most often'], 0),
   ('An absolute value equation can have ___ solutions.', ['Two possible', 'Exactly zero, always', 'A number of solutions unrelated to absolute value equations', 'Exactly one, always'], 0),
   ('Theoretical probability is calculated using ___.', ['The known possible outcomes of an event', 'The actual results collected from repeated trials', 'A concept unrelated to theoretical probability', 'A random guess with no calculation involved'], 0),
   ('Why is it useful to review coordinate geometry, statistics, algebra, and probability together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other in mathematics', 'A reason unrelated to reviewing math', 'Review is never useful in math'], 0)]),
Sc('Review: Days 61-69 Science Concepts',
   'Grade 8 Science strand review: this lesson revisits watersheds and the water cycle, groundwater and aquifers, simple machines, density and buoyancy, acids and bases, chemical versus physical changes, and planetary motion from recent lessons.',
   [('A watershed is best described as ___.', ['An area of land where all water drains into a common river, lake, or ocean', 'A single isolated pond with no connection to surrounding land', 'A concept unrelated to watersheds', 'A structure built specifically to store drinking water'], 0),
    ('Mechanical advantage compares ___.', ['The output force of a machine to the input force applied', 'The colour of a machine to its size', 'A concept unrelated to mechanical advantage', 'The weight of a machine to its cost'], 0),
    ('An object will float in water if its density is ___.', ['Less than the density of water', 'Greater than the density of water', 'A concept unrelated to buoyancy', 'Exactly equal to the density of air'], 0),
    ('On the pH scale, a value below 7 indicates ___.', ['An acid', 'A base', 'A concept unrelated to the pH scale', 'A completely neutral substance'], 0),
    ('Why is it useful to review earth science, physics, and chemistry topics together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing science', 'Each topic must be studied with no connection to the others'], 0)]),
H('Review: Days 61-69 Canadian History',
  'Grade 8 History strand review: this lesson revisits the Red River Resistance, the Canadian Pacific Railway, residential schools, the Sixties Scoop, Pier 21, the patriation of the Constitution, and the Statute of Westminster from recent lessons.',
  [('The Red River Resistance was led primarily by ___.', ['Louis Riel and the Métis', 'John A. Macdonald and the federal government', 'A group unrelated to the Red River Resistance', 'British colonial troops'], 0),
   ('The completion of the Canadian Pacific Railway fulfilled a promise made to ___.', ['British Columbia, to join Confederation', 'The United States, to share a rail line', 'A promise unrelated to the Canadian Pacific Railway', 'France, to maintain trade routes'], 0),
   ('Residential schools were institutions that ___.', ['Forcibly separated Indigenous children from their families to assimilate them', 'Were voluntarily attended by Indigenous families with no pressure involved', 'A description unrelated to residential schools', 'Taught only Indigenous languages and traditions with government support'], 0),
   ('Patriating the Constitution in 1982 meant that Canada ___.', ['Gained full authority to amend its own Constitution without approval from Britain', 'Lost all authority to make changes to its own laws', 'A meaning unrelated to patriation', 'Became a colony of Britain once again'], 0),
   ('Why is it useful to review these events in Canadian history together?', ['It reinforces how these events shaped Canadian identity, rights, and nationhood over time', 'These topics have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history and policy'], 0)])]),
]


def _rebalance_answer_positions(days, seed=20260815):
    """Same technique used for the earlier Grade 8 batches -- reassigns
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
    _rebalance_answer_positions(g8_61_70)
    append_to(8, g8_61_70)
