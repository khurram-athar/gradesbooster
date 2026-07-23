#!/usr/bin/env python3
"""Grade 9, Days 101-110 -- extends Grade 9 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade9.json): personification and pathetic fallacy, structuring a
formal debate speech, comma splices and fused sentences, loaded language
and propaganda techniques, hyperbole and understatement, the bildungsroman
coming-of-age narrative, apostrophes for possession and contraction,
juxtaposition in literature, fact vs opinion in news reporting; factoring
trinomials of the form x^2+bx+c, exponent laws for multiplying and
dividing powers, frequency tables and histograms, percent change, solving
multi-step equations with fractions and decimals, the number of solutions
to a linear system, multiplying and dividing rational expressions, scale
diagrams and scale factor, simplifying cube roots and higher-order
radicals; volcanoes and volcanic activity, naming chemical compounds
(ionic and molecular nomenclature), cell transport (diffusion and
osmosis), food chains/food webs/energy pyramids, the particle theory of
matter and changes of state, lenses and image formation, weather systems
(air masses and fronts), the excretory system, mitosis and meiosis;
ecological footprint, the geography of hydroelectric power and dams,
aging populations and the dependency ratio, the informal economy,
separatist movements and political geography, the resource curse, smart
cities, ocean plastic pollution, and the geography of wind energy siting.

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 9 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-english'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science'
SS9 = 'https://tvolearn.com/pages/grade-9-geography'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 English',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science',
    'TVO Learn: Grade 9 Geography',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


def _rebalance_answer_positions(days, seed=20260722):
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


g9_101_110 = [
day(101, [
L('Reading: Analyzing Personification and Pathetic Fallacy',
  'Grade 9 Language strand: personification gives human qualities to non-human things, and pathetic fallacy is a specific form of personification in which nature or the weather reflects a character’s emotions.',
  [('What is personification?', ['A literary device that gives human qualities to non-human things', 'A device that removes all emotion from a poem', 'A concept unrelated to reading', 'A type of formal persuasive essay'], 0),
   ('Is pathetic fallacy a specific form of personification involving nature or weather?', ['Yes', 'No, pathetic fallacy never involves nature or weather', 'A concept unrelated to pathetic fallacy', 'Personification has no connection to pathetic fallacy'], 0),
   ('Which sentence is an example of pathetic fallacy?', ['The angry storm clashed against the windows.', 'She walked quickly to the store.', 'The thermometer read twenty degrees.', 'He finished his homework before dinner.'], 0),
   ('Why might an author use pathetic fallacy to describe a storm during a character’s moment of grief?', ['It can mirror the character’s internal emotional state through the external natural world', 'Pathetic fallacy never connects a character’s emotions to the setting', 'This concept has no connection to literature', 'Weather description is always completely unrelated to a character’s feelings'], 0),
   ('Why is recognizing personification useful when analyzing a poem’s mood?', ['It reveals how the poet uses human traits to shape how readers feel about a scene or object', 'Personification never affects how a reader feels about a scene', 'This concept has no relevance to reading comprehension', 'Every poem uses personification in exactly the same way'], 0)]),
M('Factoring Trinomials of the Form x^2 + bx + c',
  'Grade 9 Math strand: a trinomial of the form x^2 + bx + c can be factored into two binomials by finding two numbers that multiply to c and add to b.',
  [('When factoring x^2 + bx + c, what must the two numbers multiply to?', ['c', 'b', 'A concept unrelated to factoring', 'x'], 0),
   ('Must the two numbers used to factor x^2 + bx + c also add to b?', ['Yes', 'No, the two numbers never need to add to b', 'A concept unrelated to factoring trinomials', 'The two numbers must always add to c instead'], 0),
   ('What is the factored form of x^2 + 5x + 6?', ['(x+2)(x+3)', '(x+1)(x+6)', '(x-2)(x-3)', '(x+2)(x+4)'], 0),
   ('What is the factored form of x^2 - 7x + 12?', ['(x-3)(x-4)', '(x+3)(x+4)', '(x-2)(x-6)', '(x-1)(x-12)'], 0),
   ('Why is checking a factored answer by expanding it back out useful?', ['It confirms the product matches the original trinomial, catching arithmetic errors', 'Expanding a factored answer never reveals any errors', 'This concept has no connection to math', 'Factored expressions never need to be checked for accuracy'], 0)]),
Sc('Science: Volcanoes and Volcanic Activity',
   'Grade 9 Science strand: a volcano forms when magma from within the Earth rises to the surface, often at tectonic plate boundaries, and erupts as lava, ash, or gas.',
   [('What is magma called once it reaches the Earth’s surface?', ['Lava', 'Sediment', 'A concept unrelated to volcanoes', 'Ash only'], 0),
    ('Do volcanoes often form at tectonic plate boundaries?', ['Yes', 'No, volcanoes never form near plate boundaries', 'A concept unrelated to volcanic activity', 'Tectonic plates have no connection to volcanoes'], 0),
    ('Which of these is commonly released during a volcanic eruption?', ['Lava, ash, and gas', 'Only fresh water', 'A concept unrelated to volcanoes', 'Only oxygen'], 0),
    ('Why might a volcano near a subduction zone erupt more explosively than one at a hot spot?', ['Thicker, gas-rich magma at subduction zones can build up more pressure before erupting', 'Subduction zone volcanoes never build up any pressure at all', 'This concept has no connection to volcanoes', 'Hot spot volcanoes always erupt more explosively than subduction zone volcanoes'], 0),
    ('Why do scientists monitor volcanic activity closely in densely populated regions?', ['Monitoring helps predict eruptions and protect nearby communities from lava, ash, and gas hazards', 'Monitoring volcanic activity provides no useful information for public safety', 'This concept has no relevance to science', 'Volcanic eruptions never pose any risk to nearby communities'], 0)]),
SS('Social Studies: Ecological Footprint: Measuring Human Impact on the Planet',
   'Grade 9 Social Studies strand: an ecological footprint measures the amount of land and resources required to support a person’s lifestyle and absorb their waste, allowing comparisons of environmental impact.',
   [('What does an ecological footprint measure?', ['The land and resources required to support a lifestyle and absorb its waste', 'The total population of a country', 'A concept unrelated to geography', 'The average temperature of a region'], 0),
    ('Can ecological footprints be used to compare environmental impact between countries?', ['Yes', 'No, ecological footprints can never be compared between countries', 'A concept unrelated to ecological footprint', 'Environmental impact has no connection to ecological footprint'], 0),
    ('Which of these would likely increase a person’s ecological footprint?', ['Frequent air travel and high meat consumption', 'Walking instead of driving', 'Growing your own vegetables', 'Using public transit regularly'], 0),
    ('Why might people in wealthier countries generally have larger ecological footprints than people in lower-income countries?', ['Higher consumption of resources, energy, and goods increases the demand placed on the environment', 'Wealthier countries always have smaller ecological footprints than lower-income countries', 'This concept has no connection to geography', 'Wealth has no effect on how many resources a person consumes'], 0),
    ('Why is understanding ecological footprint useful for planning sustainable communities?', ['It helps identify areas where resource consumption and waste can be reduced', 'Ecological footprint provides no useful information for sustainability planning', 'This concept has no relevance to social studies', 'Sustainable communities never need to consider resource consumption'], 0)]),
]),

day(102, [
L('Writing: Structuring a Formal Debate Speech',
  'Grade 9 Language strand: a formal debate speech presents a clear claim supported by evidence and reasoning, while also anticipating and addressing counter-arguments from the opposing side.',
  [('What must a formal debate speech present?', ['A clear claim supported by evidence and reasoning', 'A list of unrelated facts with no argument', 'A concept unrelated to writing', 'A summary of the opposing team’s schedule'], 0),
   ('Should a debate speech anticipate counter-arguments from the opposing side?', ['Yes', 'No, a debate speech should never consider the opposing side', 'A concept unrelated to debate speeches', 'Counter-arguments have no connection to a formal debate'], 0),
   ('Which of these best opens a formal debate speech?', ['A clear statement of the position being argued', 'A list of unrelated statistics with no context', 'A joke with no connection to the topic', 'A description of the debate venue'], 0),
   ('Why might a debater address a counter-argument before the opposing side raises it?', ['It demonstrates the speaker has considered other views, strengthening their credibility', 'Addressing counter-arguments always weakens a debater’s position', 'This concept has no connection to writing', 'Debaters should never acknowledge any opposing viewpoint'], 0),
   ('Why is using credible evidence important in a formal debate speech?', ['It makes the argument more persuasive and trustworthy to the audience and judges', 'Credible evidence never strengthens a persuasive argument', 'This concept has no relevance to writing', 'A debate speech never requires any supporting evidence'], 0)]),
M('Exponent Laws: Multiplying and Dividing Powers with the Same Base',
  'Grade 9 Math strand: when multiplying powers with the same base, add the exponents; when dividing powers with the same base, subtract the exponents.',
  [('When multiplying powers with the same base, what operation is performed on the exponents?', ['They are added', 'They are subtracted', 'A concept unrelated to exponents', 'They are multiplied together'], 0),
   ('When dividing powers with the same base, are the exponents subtracted?', ['Yes', 'No, exponents are never subtracted when dividing powers', 'A concept unrelated to dividing powers', 'The exponents are always added instead when dividing'], 0),
   ('What is x^4 multiplied by x^3 equal to?', ['x^7', 'x^12', 'x^1', 'x^43'], 0),
   ('What is x^8 divided by x^3 equal to?', ['x^5', 'x^11', 'x^2', 'x^24'], 0),
   ('Why must the bases be the same before adding or subtracting exponents using these laws?', ['These exponent laws only apply when multiplying or dividing identical bases', 'The bases never need to match to use these exponent laws', 'This concept has no connection to math', 'Exponent laws work identically regardless of whether the bases match'], 0)]),
Sc('Science: Naming Chemical Compounds: Ionic and Molecular Nomenclature',
   'Grade 9 Science strand: ionic compounds are named using the metal name followed by the nonmetal name with an -ide ending, while molecular compounds use prefixes to indicate the number of atoms of each element.',
   [('How is an ionic compound like sodium chloride typically named?', ['Metal name followed by the nonmetal name with an -ide ending', 'Two nonmetal names joined with no ending change', 'A concept unrelated to chemistry', 'Only the chemical formula, with no written name'], 0),
    ('Do molecular compound names use prefixes like mono-, di-, and tri- to show the number of atoms?', ['Yes', 'No, molecular compound names never use prefixes', 'A concept unrelated to molecular nomenclature', 'Prefixes are only ever used for ionic compounds'], 0),
    ('What is the correct molecular name for CO2?', ['Carbon dioxide', 'Carbon oxide', 'Dicarbon oxide', 'Carbon monoxide'], 0),
    ('Why does table salt use the ending -ide rather than the element’s usual name chlorine?', ['The -ide ending is the naming convention for the negative ion formed from chlorine in a compound', 'The -ide ending is never used when naming a compound', 'This concept has no connection to chemistry', 'Chlorine and chloride always refer to exactly the same thing with no naming difference'], 0),
    ('Why is a standardized naming system important for chemical compounds?', ['It ensures scientists everywhere can identify the same compound regardless of language', 'A standardized naming system provides no benefit to scientific communication', 'This concept has no relevance to science', 'Every scientist uses a completely different, incompatible naming system'], 0)]),
SS('Social Studies: The Geography of Hydroelectric Power and Dam Construction',
   'Grade 9 Social Studies strand: hydroelectric power generates electricity by using flowing or falling water to turn turbines, and building large dams to harness this resource can reshape rivers, ecosystems, and communities.',
   [('What does hydroelectric power use to generate electricity?', ['Flowing or falling water turning turbines', 'Burning coal to heat water into steam', 'A concept unrelated to geography', 'Wind passing over large blades'], 0),
    ('Can constructing a large dam reshape ecosystems and displace nearby communities?', ['Yes', 'No, dam construction never affects ecosystems or communities', 'A concept unrelated to hydroelectric geography', 'Communities are never affected by the construction of a dam'], 0),
    ('Which geographic feature is generally required to generate significant hydroelectric power?', ['A river with sufficient flow and elevation change', 'A flat desert with no water source', 'A concept unrelated to hydroelectric power', 'A calm lake with no water movement at all'], 0),
    ('Why might a hydroelectric dam be built in a mountainous region rather than a flat plain?', ['Steep elevation change provides more force to generate power as water falls', 'Mountainous regions never provide any advantage for generating hydroelectric power', 'This concept has no connection to geography', 'Flat plains always generate more hydroelectric power than mountainous regions'], 0),
    ('Why do some communities oppose the construction of large hydroelectric dams?', ['Dams can flood land, displace residents, and disrupt fish and wildlife habitats', 'Hydroelectric dams never have any impact on land or wildlife', 'This concept has no relevance to social studies', 'Communities are always in favour of every dam project with no concerns'], 0)]),
]),

day(103, [
L('Grammar: Comma Splices and Fused Sentences',
  'Grade 9 Language strand: a comma splice incorrectly joins two independent clauses with only a comma, and a fused sentence joins two independent clauses with no punctuation at all; both can be corrected with a period, semicolon, or coordinating conjunction.',
  [('What is a comma splice?', ['Two independent clauses joined incorrectly by only a comma', 'A sentence with no punctuation errors at all', 'A concept unrelated to grammar', 'A single independent clause with a period at the end'], 0),
   ('Does a fused sentence join two independent clauses with no punctuation at all?', ['Yes', 'No, a fused sentence always includes a semicolon', 'A concept unrelated to fused sentences', 'Fused sentences never join two independent clauses'], 0),
   ('Which sentence is an example of a comma splice?', ['I love reading, I read every night.', 'I love reading, and I read every night.', 'I love reading. I read every night.', 'I love reading; I read every night.'], 0),
   ('Which of these correctly fixes a comma splice?', ['Replacing the comma with a semicolon or period, or adding a coordinating conjunction', 'Adding a second comma right after the first one', 'Removing all punctuation from the sentence entirely', 'Replacing the comma with a colon in every case'], 0),
   ('Why is recognizing comma splices and fused sentences important for clear writing?', ['It helps readers see where one complete thought ends and another begins', 'These errors never affect how clearly a reader understands a sentence', 'This concept has no connection to grammar', 'Every sentence must contain a comma splice to be grammatically correct'], 0)]),
M('Data Management: Frequency Tables and Histograms',
  'Grade 9 Math strand: a frequency table organizes data into intervals and counts how many values fall in each interval, and a histogram displays this data as connected bars with no gaps between them.',
  [('What does a frequency table organize?', ['Data into intervals with a count of how many values fall in each', 'A single value repeated many times with no intervals', 'A concept unrelated to data management', 'Only the largest and smallest values in a data set'], 0),
   ('Do the bars in a histogram touch with no gaps between them?', ['Yes', 'No, histogram bars always have gaps between them', 'A concept unrelated to histograms', 'Histograms never use bars of any kind'], 0),
   ('In a frequency table with test scores grouped in intervals of 10, which interval would a score of 85 belong to?', ['80-89', '70-79', '90-99', '60-69'], 0),
   ('How does a histogram differ from a bar graph of categorical data?', ['Histogram bars touch to show continuous numerical intervals, while bar graph bars are usually separated for distinct categories', 'Histograms and bar graphs are always exactly identical with no differences', 'This concept has no connection to math', 'Bar graphs are always used for continuous numerical data instead of histograms'], 0),
   ('Why is a histogram useful for visualizing the distribution of a large data set?', ['It shows the shape and spread of the data at a glance, including where most values cluster', 'A histogram never reveals any information about how data is distributed', 'This concept has no connection to math', 'Histograms can only be used for data sets with fewer than five values'], 0)]),
Sc('Science: Cell Transport: Diffusion and Osmosis',
   'Grade 9 Science strand: diffusion is the movement of particles from an area of higher concentration to lower concentration, and osmosis is the diffusion of water specifically across a semi-permeable membrane.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles from lower to higher concentration only', 'A concept unrelated to biology', 'A process that only occurs inside solid rocks'], 0),
    ('Is osmosis specifically the diffusion of water across a semi-permeable membrane?', ['Yes', 'No, osmosis never involves the movement of water', 'A concept unrelated to osmosis', 'Osmosis only ever involves the movement of oxygen gas'], 0),
    ('Which of these is an example of diffusion?', ['Perfume scent gradually spreading through a room', 'A rock sitting motionless on the ground', 'A book resting on a shelf', 'A car parked in a driveway'], 0),
    ('Why might a plant cell placed in salty water lose water through osmosis?', ['Water moves from inside the cell, where water concentration is higher, to the saltier solution outside, where it is lower', 'Water always moves into a cell placed in salty water', 'This concept has no connection to biology', 'Salt concentration never affects the movement of water across a membrane'], 0),
    ('Why is diffusion important for cells to obtain oxygen and nutrients?', ['It allows particles to move passively across cell membranes without requiring extra cellular energy', 'Diffusion never allows any particles to cross a cell membrane', 'This concept has no relevance to science', 'Cells always require large amounts of energy to move oxygen and nutrients in by diffusion'], 0)]),
SS('Social Studies: Aging Populations and the Dependency Ratio',
   'Grade 9 Social Studies strand: an aging population has a growing proportion of older residents, which raises the dependency ratio, the comparison of dependents (young and elderly) to the working-age population.',
   [('What does the dependency ratio compare?', ['The number of dependents to the working-age population', 'The number of cities to the number of provinces', 'A concept unrelated to population geography', 'The total land area to the total population'], 0),
    ('Does an aging population increase the elderly portion of the dependency ratio?', ['Yes', 'No, an aging population never affects the dependency ratio', 'A concept unrelated to aging populations', 'The dependency ratio has no connection to a country’s age structure'], 0),
    ('Which of these countries would likely have a high dependency ratio due to an aging population?', ['A country with a large elderly population and a low birth rate', 'A country with mostly working-age adults and few elderly residents', 'A concept unrelated to dependency ratio', 'A country with no population data available'], 0),
    ('Why might a country with an aging population face economic challenges related to healthcare and pensions?', ['Fewer working-age people are left to support the costs of a larger elderly population needing services', 'Aging populations never create any additional economic demands', 'This concept has no connection to geography', 'Elderly populations never require healthcare or pension support'], 0),
    ('Why do some countries with aging populations encourage immigration of working-age people?', ['It can help balance the dependency ratio and support continued economic productivity', 'Immigration never affects a country’s dependency ratio', 'This concept has no relevance to social studies', 'Working-age immigrants never contribute to a country’s workforce'], 0)]),
]),

day(104, [
L('Vocabulary: Loaded Language and Propaganda Techniques',
  'Grade 9 Language strand: loaded language uses emotionally charged words to influence opinion, and propaganda techniques such as bandwagon and glittering generalities use loaded language to persuade audiences beyond logical argument.',
  [('What does loaded language use to influence opinion?', ['Emotionally charged words', 'Neutral, factual statistics only', 'A concept unrelated to vocabulary', 'Only formal, technical terminology'], 0),
   ('Does the bandwagon propaganda technique appeal to a desire to join the majority?', ['Yes', 'No, the bandwagon technique never appeals to a sense of belonging', 'A concept unrelated to propaganda techniques', 'The bandwagon technique only ever appeals to logic'], 0),
   ('Which phrase is an example of loaded language?', ['The criminal regime', 'The government', 'The elected officials', 'The national leadership'], 0),
   ('Why might an advertisement use the glittering generalities technique, pairing a product with vague positive words like freedom or greatness?', ['It can create positive associations with the product without providing specific evidence', 'Glittering generalities always provide detailed factual evidence for a claim', 'This concept has no connection to vocabulary', 'This technique never has any persuasive effect on an audience'], 0),
   ('Why is it important to identify loaded language and propaganda techniques when evaluating a persuasive text?', ['It helps readers separate emotional appeal from factual evidence and sound reasoning', 'Loaded language and propaganda techniques never affect how a message is perceived', 'This concept has no relevance to vocabulary study', 'Every persuasive text relies exclusively on factual evidence with no emotional appeal'], 0)]),
M('Percent Change: Increase and Decrease Applications',
  'Grade 9 Math strand: percent change measures the relative increase or decrease between an original value and a new value, calculated as the difference divided by the original value and expressed as a percent.',
  [('How is percent change generally calculated?', ['The difference between the new and original value, divided by the original value, times 100', 'The new value divided by 100', 'A concept unrelated to percent change', 'The original value divided by the new value'], 0),
   ('Does a positive percent change indicate an increase from the original value?', ['Yes', 'No, a positive percent change always indicates a decrease', 'A concept unrelated to percent change', 'Percent change is never positive or negative'], 0),
   ('If a shirt’s price rises from 40 dollars to 50 dollars, what is the percent increase?', ['25 percent', '10 percent', '20 percent', '50 percent'], 0),
   ('If a population drops from 200 to 150, what is the percent decrease?', ['25 percent', '50 percent', '75 percent', '33 percent'], 0),
   ('Why is percent change more useful than the raw numerical difference when comparing changes across data sets of different sizes?', ['It expresses change relative to the original size, making comparisons fair across different scales', 'Percent change never provides a fair way to compare data sets of different sizes', 'This concept has no connection to math', 'The raw numerical difference always gives a more accurate comparison than percent change'], 0)]),
Sc('Science: Food Chains, Food Webs, and Energy Pyramids',
   'Grade 9 Science strand: a food chain shows a single path of energy transfer between organisms, a food web connects multiple interlinked food chains, and an energy pyramid shows that available energy decreases at each higher trophic level.',
   [('What does a food chain show?', ['A single path of energy transfer between organisms', 'The total mass of every organism in an ecosystem', 'A concept unrelated to biology', 'The temperature changes within an ecosystem'], 0),
    ('Does a food web connect multiple interlinked food chains?', ['Yes', 'No, a food web never connects more than one food chain', 'A concept unrelated to food webs', 'Food webs and food chains always refer to exactly the same single path'], 0),
    ('In an energy pyramid, does available energy decrease or increase at each higher trophic level?', ['It decreases', 'It increases', 'A concept unrelated to energy pyramids', 'It stays exactly the same at every level'], 0),
    ('Why do food webs give a more accurate picture of ecosystem relationships than a single food chain?', ['Most organisms eat and are eaten by more than one species, so multiple interconnected paths exist', 'A single food chain always shows every relationship in an ecosystem accurately', 'This concept has no connection to biology', 'Food webs never provide any more detail than a single food chain'], 0),
    ('Why does only a small fraction of energy transfer from one trophic level to the next in an energy pyramid?', ['Most energy is lost as heat through life processes like movement and metabolism at each level', 'All of the energy at one trophic level is always transferred completely to the next', 'This concept has no relevance to science', 'Energy pyramids never involve any loss of energy between levels'], 0)]),
SS('Social Studies: The Informal Economy in Developing Regions',
   'Grade 9 Social Studies strand: the informal economy consists of unregulated, untaxed economic activity, such as street vending or unlicensed labour, which forms a significant part of the workforce in many developing regions.',
   [('What is the informal economy made up of?', ['Unregulated, untaxed economic activity', 'Only large, government-registered corporations', 'A concept unrelated to economic geography', 'Only activity that occurs in wealthy countries'], 0),
    ('Is street vending a common example of informal economic activity?', ['Yes', 'No, street vending is always formally regulated and taxed', 'A concept unrelated to the informal economy', 'Street vending has no connection to informal economic activity'], 0),
    ('Which of these best describes informal economic work?', ['Unlicensed, untaxed labour that operates outside government regulation', 'Fully licensed work with complete government oversight', 'A concept unrelated to economic geography', 'Work performed only within large multinational corporations'], 0),
    ('Why might informal economy workers lack access to benefits like healthcare or pensions?', ['Their work is unregistered and untaxed, placing it outside formal labour protections', 'Informal economy workers always receive the same benefits as formal employees', 'This concept has no connection to geography', 'Benefits like healthcare are never connected to a worker’s employment status'], 0),
    ('Why does the informal economy make it difficult for governments to accurately measure a country’s total economic activity?', ['Informal transactions go unreported and untaxed, so they are excluded from official statistics', 'The informal economy is always fully included in official government statistics', 'This concept has no relevance to social studies', 'Governments never face any difficulty measuring economic activity'], 0)]),
]),

day(105, [
L('Reading: Understanding Hyperbole and Understatement',
  'Grade 9 Language strand: hyperbole is deliberate exaggeration for emphasis or effect, while understatement deliberately minimizes the importance of something, often for ironic or humorous effect.',
  [('What is hyperbole?', ['Deliberate exaggeration for emphasis or effect', 'A precise, literal description with no exaggeration', 'A concept unrelated to reading', 'A type of formal citation'], 0),
   ('Does understatement deliberately minimize the importance of something?', ['Yes', 'No, understatement always exaggerates the importance of something', 'A concept unrelated to understatement', 'Understatement has no connection to how a statement is expressed'], 0),
   ('Which of these sentences is an example of hyperbole?', ['I have told you a million times to clean your room.', 'I have told you twice to clean your room.', 'Please clean your room today.', 'Your room needs some tidying.'], 0),
   ('Which of these sentences is an example of understatement?', ['Describing a hurricane as a bit of a breeze', 'Describing a hurricane as an extremely dangerous storm', 'Describing a light rain shower as a torrential downpour', 'Describing a calm day as a hurricane'], 0),
   ('Why might a writer use understatement to describe a serious or tragic event?', ['It can create an ironic contrast that highlights the event’s true severity through restraint', 'Understatement always makes a serious event seem more dramatic and exaggerated', 'This concept has no connection to reading', 'Understatement never affects how a reader perceives a described event'], 0)]),
M('Solving Multi-Step Linear Equations with Fractions and Decimals',
  'Grade 9 Math strand: solving multi-step linear equations containing fractions or decimals often requires clearing them first by multiplying every term by a common denominator or power of ten before isolating the variable.',
  [('What is a common first step when solving an equation containing fractions?', ['Multiply every term by the common denominator to clear the fractions', 'Immediately divide every term by zero', 'A concept unrelated to solving equations', 'Ignore the fractions and solve only with the whole numbers present'], 0),
   ('Can multiplying every term of an equation with decimals by a power of ten clear the decimals?', ['Yes', 'No, decimals in an equation can never be cleared', 'A concept unrelated to solving equations', 'Multiplying by a power of ten always creates more decimals'], 0),
   ('Solve for x: x/2 + 3 = 7.', ['x = 8', 'x = 4', 'x = 10', 'x = 2'], 0),
   ('Solve for x: 0.5x - 1 = 4.', ['x = 10', 'x = 5', 'x = 8', 'x = 3'], 0),
   ('Why is clearing fractions or decimals from an equation before solving often helpful?', ['It simplifies the equation into whole numbers, reducing the chance of arithmetic errors', 'Clearing fractions or decimals always makes an equation harder to solve', 'This concept has no connection to math', 'Equations with fractions or decimals can never be solved using this method'], 0)]),
Sc('Science: The Particle Theory of Matter and Changes of State',
   'Grade 9 Science strand: the particle theory of matter states that all matter is made of tiny particles in constant motion with spaces between them, and changes of state occur as energy is added or removed, altering particle motion and spacing.',
   [('According to the particle theory of matter, what is all matter made of?', ['Tiny particles in constant motion', 'A single continuous substance with no particles', 'A concept unrelated to chemistry', 'Only visible solid chunks with no motion'], 0),
    ('Do particles have spaces between them according to the particle theory of matter?', ['Yes', 'No, particles are always packed with absolutely no space between them', 'A concept unrelated to the particle theory', 'Spacing between particles has no connection to the particle theory'], 0),
    ('What happens to particle motion when energy is added to a solid, causing it to melt?', ['Particles move faster and spread further apart', 'Particles stop moving completely', 'A concept unrelated to changes of state', 'Particles move closer together and slow down'], 0),
    ('Why do gas particles have more space between them than particles in a solid?', ['Gas particles have much more energy and move more freely, spreading further apart', 'Gas particles always have less energy than particles in a solid', 'This concept has no connection to chemistry', 'The spacing between particles never changes between different states of matter'], 0),
    ('Why is the particle theory of matter useful for explaining why gases can be compressed but solids generally cannot?', ['Gas particles have large spaces between them that can be pushed closer together, while solid particles are already tightly packed', 'Gases and solids always compress in exactly the same way', 'This concept has no relevance to science', 'Solids can always be compressed far more easily than gases'], 0)]),
SS('Social Studies: Separatist Movements and Political Geography',
   'Grade 9 Social Studies strand: a separatist movement seeks independence or greater autonomy for a region within a larger country, often rooted in a distinct cultural, linguistic, or economic identity.',
   [('What does a separatist movement typically seek for a region within a larger country?', ['Independence or greater autonomy', 'Complete elimination of all regional governments', 'A concept unrelated to political geography', 'Total merger with a neighbouring country’s government'], 0),
    ('Can separatist movements be rooted in a region’s distinct cultural or linguistic identity?', ['Yes', 'No, separatist movements never relate to culture or language', 'A concept unrelated to separatist movements', 'Cultural identity has no connection to political geography'], 0),
    ('Which of these is a factor that commonly motivates a separatist movement?', ['A region having a distinct language, culture, or history from the rest of the country', 'A region having identical culture and language to the rest of the country', 'A concept unrelated to political geography', 'A region having no population of its own'], 0),
    ('Why might a region with strong economic resources support a separatist movement?', ['Residents may feel they contribute more wealth than they receive back in return', 'Economically strong regions never support separatist movements', 'This concept has no connection to geography', 'Separatist movements only occur in regions with no economic resources'], 0),
    ('Why do political geographers study separatist movements around the world?', ['Understanding regional identity and autonomy conflicts helps explain how national borders and governance can change over time', 'Separatist movements never provide any useful information to political geographers', 'This concept has no relevance to social studies', 'National borders never change as a result of separatist movements'], 0)]),
]),

day(106, [
L('Writing: The Bildungsroman — Coming-of-Age Narrative Elements',
  'Grade 9 Language strand: a bildungsroman is a coming-of-age narrative that traces a young protagonist’s psychological and moral growth from youth to maturity, often through a formative experience or journey.',
  [('What does a bildungsroman trace?', ['A young protagonist’s psychological and moral growth from youth to maturity', 'The complete history of a fictional nation', 'A concept unrelated to writing', 'A detailed scientific report'], 0),
   ('Does a bildungsroman typically follow a formative experience or journey?', ['Yes', 'No, a bildungsroman never involves any kind of journey or experience', 'A concept unrelated to bildungsroman', 'Formative experiences have no connection to this narrative form'], 0),
   ('Which of these best describes a bildungsroman’s central protagonist?', ['A young character who grows and changes significantly over the story', 'A fully mature adult who never changes throughout the story', 'A concept unrelated to writing', 'A minor character with no role in the plot'], 0),
   ('Why might a coming-of-age story often include a mentor figure who guides the protagonist?', ['Mentors can provide wisdom or challenges that support the protagonist’s growth and self-discovery', 'Mentor figures never appear in coming-of-age stories', 'This concept has no connection to writing', 'A mentor always prevents a protagonist from growing or changing'], 0),
   ('Why is the ending of a bildungsroman important for showing the protagonist’s development?', ['It typically reveals how the character has matured or changed compared to who they were at the beginning', 'The ending of a bildungsroman never reflects any character growth', 'This concept has no relevance to writing', 'A bildungsroman’s protagonist is always exactly the same at the end as at the beginning'], 0)]),
M('The Number of Solutions to a Linear System (None, One, or Infinite)',
  'Grade 9 Math strand: a system of two linear equations can have exactly one solution, no solution, or infinitely many solutions, depending on whether the lines intersect, are parallel, or are identical.',
  [('How many solutions does a linear system have if the two lines intersect at a single point?', ['One solution', 'No solution', 'A concept unrelated to systems of equations', 'Infinitely many solutions'], 0),
   ('Does a system with two parallel, non-identical lines have no solution?', ['Yes', 'No, parallel non-identical lines always have exactly one solution', 'A concept unrelated to parallel lines', 'Parallel lines always produce infinitely many solutions'], 0),
   ('How many solutions exist if both equations in a system graph as the exact same line?', ['Infinitely many solutions', 'Exactly one solution', 'No solution at all', 'A concept unrelated to systems of equations'], 0),
   ('If two lines in a system have the same slope but different y-intercepts, how many solutions does the system have?', ['No solution', 'Exactly one solution', 'Infinitely many solutions', 'A concept unrelated to systems of equations'], 0),
   ('Why is it useful to compare the slopes and y-intercepts of two equations before graphing them to solve a system?', ['It allows you to predict how many solutions the system will have without graphing', 'Comparing slopes and y-intercepts never provides any useful information about a system', 'This concept has no connection to math', 'The number of solutions to a system can never be predicted before graphing'], 0)]),
Sc('Science: Lenses and the Formation of Images (Concave and Convex)',
   'Grade 9 Science strand: a convex lens curves outward and converges light rays to form an image, while a concave lens curves inward and diverges light rays, and a lens’s shape determines how it bends light.',
   [('Does a convex lens curve outward?', ['Yes', 'No, a convex lens always curves inward', 'A concept unrelated to lenses', 'Convex lenses have no defined curvature'], 0),
    ('Does a concave lens diverge light rays?', ['Yes', 'No, a concave lens always converges light rays', 'A concept unrelated to concave lenses', 'Concave lenses never affect the path of light'], 0),
    ('Which type of lens is commonly used to correct farsightedness by converging light?', ['A convex lens', 'A concave lens', 'A concept unrelated to lenses', 'Neither type of lens is ever used for vision correction'], 0),
    ('Why does a convex lens cause light rays passing through it to converge at a focal point?', ['Its outward curve bends parallel light rays inward toward a common point', 'A convex lens always spreads light rays further apart', 'This concept has no connection to science', 'Convex lenses never bend light rays in any direction'], 0),
    ('Why might a concave lens be used to correct nearsightedness?', ['It diverges light rays before they enter the eye, adjusting where the image comes into focus on the retina', 'Concave lenses never have any effect on how light enters the eye', 'This concept has no relevance to science', 'Concave lenses always converge light exactly like a convex lens'], 0)]),
SS('Social Studies: The Resource Curse: Natural Wealth and Economic Underdevelopment',
   'Grade 9 Social Studies strand: the resource curse describes a phenomenon in which countries rich in valuable natural resources sometimes experience slower economic growth, corruption, or conflict rather than widespread prosperity.',
   [('What does the resource curse describe?', ['Countries rich in natural resources sometimes experiencing slower growth, corruption, or conflict', 'Countries with no natural resources always becoming extremely wealthy', 'A concept unrelated to geography', 'A curse placed on a country by a foreign government'], 0),
    ('Can the resource curse involve increased corruption in a resource-rich country?', ['Yes', 'No, the resource curse never involves any corruption', 'A concept unrelated to the resource curse', 'Corruption has no connection to natural resource wealth'], 0),
    ('Which of these outcomes is commonly associated with the resource curse?', ['Wealth becoming concentrated among a small elite rather than benefiting the wider population', 'Natural resource wealth always being distributed equally among all citizens', 'A concept unrelated to the resource curse', 'Resource-rich countries always avoiding any economic instability'], 0),
    ('Why might a country overly dependent on exporting a single natural resource, like oil, be vulnerable to economic instability?', ['Its economy can be heavily affected by global price fluctuations for that resource', 'Global price changes never affect a country’s economy in any way', 'This concept has no connection to geography', 'Countries exporting a single resource are always more economically stable'], 0),
    ('Why do some resource-rich countries pursue economic diversification to avoid the resource curse?', ['Reducing dependence on a single resource and its volatile market value promotes more stable growth', 'Economic diversification never helps a country avoid instability', 'This concept has no relevance to social studies', 'Countries dependent on a single resource are always the most economically stable'], 0)]),
]),

day(107, [
L('Grammar: Apostrophes for Possession and Contraction',
  'Grade 9 Language strand: an apostrophe shows possession by adding an apostrophe and s to a singular noun or just an apostrophe after a plural noun ending in s, and it also marks the missing letters in a contraction.',
  [('How is possession typically shown for a singular noun?', ['Add an apostrophe and s', 'Add only an s with no apostrophe', 'A concept unrelated to grammar', 'Add an apostrophe at the very start of the word'], 0),
   ('Does an apostrophe in a contraction mark missing letters?', ['Yes', 'No, apostrophes in contractions never mark missing letters', 'A concept unrelated to contractions', 'Contractions never contain an apostrophe'], 0),
   ('Which of these correctly shows possession for a plural noun ending in s, like the dogs?', ['The dogs’ toys', 'The dog’s toys', 'The dogs’s toys', 'The dogs toys’'], 0),
   ('What does the contraction it’s stand for?', ['It is', 'Belonging to it', 'A concept unrelated to contractions', 'It was'], 0),
   ('Why is it important to distinguish between its (possessive) and it’s (contraction) in formal writing?', ['Using the wrong form changes the meaning and signals a grammatical error to careful readers', 'The two words are always completely interchangeable with no difference in meaning', 'This concept has no connection to grammar', 'Formal writing never requires distinguishing between these two words'], 0)]),
M('Multiplying and Dividing Rational Expressions',
  'Grade 9 Math strand: multiplying rational expressions involves multiplying numerators and denominators and then simplifying common factors, while dividing rational expressions involves multiplying by the reciprocal of the divisor.',
  [('When multiplying rational expressions, what should be done after multiplying the numerators and denominators?', ['Simplify by cancelling common factors', 'Immediately add the two denominators together', 'A concept unrelated to rational expressions', 'Discard the denominators entirely'], 0),
   ('When dividing rational expressions, do you multiply by the reciprocal of the divisor?', ['Yes', 'No, dividing rational expressions never involves a reciprocal', 'A concept unrelated to dividing rational expressions', 'Division of rational expressions always requires finding a common denominator instead'], 0),
   ('Simplify: (x/2) multiplied by (4/x).', ['2', 'x', '4', '8/x'], 0),
   ('Simplify: (x/3) divided by (x/6).', ['2', '1/2', '6', '3'], 0),
   ('Why is factoring often a necessary first step before multiplying or dividing rational expressions?', ['Factoring reveals common factors that can be cancelled to simplify the expression', 'Factoring never helps simplify a rational expression', 'This concept has no connection to math', 'Rational expressions can never be simplified through factoring'], 0)]),
Sc('Science: Weather Systems: Air Masses and Fronts',
   'Grade 9 Science strand: an air mass is a large body of air with fairly uniform temperature and humidity, and a front forms where two different air masses meet, often producing changes in weather.',
   [('What is an air mass?', ['A large body of air with fairly uniform temperature and humidity', 'A single raindrop falling from a cloud', 'A concept unrelated to earth science', 'A small pocket of gas found underground'], 0),
    ('Does a front form where two different air masses meet?', ['Yes', 'No, a front never forms where air masses meet', 'A concept unrelated to weather fronts', 'Air masses never interact with one another'], 0),
    ('What type of front forms when a cold air mass pushes under and lifts a warm air mass?', ['A cold front', 'A warm front', 'A concept unrelated to weather systems', 'A stationary front'], 0),
    ('Why do fronts often bring precipitation and changing weather conditions?', ['Warm air rising over cooler air can cool and condense, forming clouds and precipitation', 'Fronts never have any effect on precipitation or weather conditions', 'This concept has no connection to earth science', 'Air masses always have exactly the same temperature and humidity when they meet'], 0),
    ('Why might meteorologists track the movement of air masses to forecast upcoming weather?', ['The temperature and humidity of an approaching air mass strongly influence future weather conditions', 'Air masses never provide any information useful for forecasting weather', 'This concept has no relevance to science', 'Weather conditions are never influenced by the movement of air masses'], 0)]),
SS('Social Studies: Smart Cities: Technology and Urban Planning Innovation',
   'Grade 9 Social Studies strand: a smart city uses digital technology and data collection, such as sensors and connected infrastructure, to improve services like transportation, energy use, and public safety.',
   [('What does a smart city use to improve urban services?', ['Digital technology and data collection', 'Only traditional paper-based record keeping', 'A concept unrelated to urban geography', 'A complete absence of any infrastructure'], 0),
    ('Can smart city sensors help manage traffic flow and energy use?', ['Yes', 'No, smart city sensors never have any connection to traffic or energy use', 'A concept unrelated to smart cities', 'Traffic flow and energy use are never influenced by technology'], 0),
    ('Which of these is an example of smart city technology?', ['Traffic lights that adjust automatically based on real-time congestion data', 'A traditional printed city map with no digital features', 'A concept unrelated to smart cities', 'A city with no connected infrastructure of any kind'], 0),
    ('Why might a smart city use connected sensors to monitor water or energy usage across the city?', ['It allows planners to identify inefficiencies and respond quickly to problems like leaks or outages', 'Monitoring water and energy usage never provides any useful information to city planners', 'This concept has no connection to geography', 'Smart city sensors are never used to monitor resource usage'], 0),
    ('Why do some critics raise privacy concerns about smart city technology?', ['Extensive data collection about residents’ movements and habits could be misused or inadequately protected', 'Smart city technology never collects any data about residents', 'This concept has no relevance to social studies', 'Privacy concerns have no connection to how smart city technology operates'], 0)]),
]),

day(108, [
L('Reading: Analyzing Juxtaposition in Literature',
  'Grade 9 Language strand: juxtaposition places two contrasting ideas, characters, or images side by side to highlight their differences and create deeper meaning for the reader.',
  [('What does juxtaposition place side by side?', ['Two contrasting ideas, characters, or images', 'Two identical, unrelated grammar rules', 'A concept unrelated to reading', 'A single idea repeated multiple times'], 0),
   ('Can juxtaposition highlight differences to create deeper meaning?', ['Yes', 'No, juxtaposition never highlights any differences', 'A concept unrelated to juxtaposition', 'Contrasting ideas placed together never create additional meaning'], 0),
   ('Which of these is an example of juxtaposition?', ['Describing a wealthy character’s mansion right after describing a poor character’s shack', 'Describing the same character’s mansion twice in a row', 'Listing a character’s daily schedule in chronological order', 'Describing the weather with no reference to any character'], 0),
   ('Why might an author juxtapose a peaceful setting with a violent event?', ['The contrast can intensify the emotional impact of the violent event on the reader', 'Juxtaposing a peaceful setting with a violent event never affects a reader’s emotional response', 'This concept has no connection to literature', 'Peaceful and violent scenes can never be placed near each other in a story'], 0),
   ('Why is recognizing juxtaposition useful when analyzing a text’s themes?', ['The contrast between two elements often reveals the author’s underlying commentary or message', 'Juxtaposition never reveals any deeper meaning about a text’s themes', 'This concept has no relevance to reading comprehension', 'Every element in a story is always presented in complete isolation with no contrast'], 0)]),
M('Scale Diagrams and Scale Factor',
  'Grade 9 Math strand: a scale diagram represents a real object using a proportional scale factor, and the scale factor is the ratio between the diagram’s dimensions and the actual object’s dimensions.',
  [('What does a scale diagram use to represent a real object?', ['A proportional scale factor', 'A completely random, unrelated set of dimensions', 'A concept unrelated to measurement', 'An object drawn without any consistent proportions'], 0),
   ('Is the scale factor the ratio between a diagram’s dimensions and the actual object’s dimensions?', ['Yes', 'No, the scale factor never compares a diagram to the real object', 'A concept unrelated to scale factor', 'Scale factor only ever applies to three-dimensional objects'], 0),
   ('If a map has a scale of 1 cm to 5 km, how many kilometres does 3 cm on the map represent?', ['15 km', '8 km', '3 km', '5 km'], 0),
   ('If a model car has a scale factor of 1:20, and the model is 10 cm long, how long is the real car?', ['200 cm', '20 cm', '10 cm', '2000 cm'], 0),
   ('Why is understanding scale factor important when reading a blueprint or map?', ['It allows accurate real-world measurements to be calculated from a smaller proportional drawing', 'Scale factor never allows any real-world measurements to be calculated', 'This concept has no connection to math', 'Blueprints and maps never use a consistent scale factor'], 0)]),
Sc('Science: The Excretory System and Waste Removal',
   'Grade 9 Science strand: the excretory system removes metabolic waste products from the body, with the kidneys filtering blood to remove urea and excess water, forming urine.',
   [('What does the excretory system remove from the body?', ['Metabolic waste products', 'Only undigested food particles', 'A concept unrelated to biology', 'Only oxygen from the lungs'], 0),
    ('Do the kidneys filter blood to remove urea and excess water?', ['Yes', 'No, the kidneys never filter blood', 'A concept unrelated to the excretory system', 'Urea and water are never removed by the kidneys'], 0),
    ('What waste product do the kidneys filter out of the blood to form urine?', ['Urea', 'Glucose', 'A concept unrelated to the excretory system', 'Oxygen'], 0),
    ('Why is the excretory system important for maintaining homeostasis in the body?', ['It removes waste and helps regulate water and ion balance, keeping internal conditions stable', 'The excretory system never has any connection to maintaining stable internal conditions', 'This concept has no connection to biology', 'Homeostasis is maintained entirely without any involvement from the excretory system'], 0),
    ('Why might dehydration affect how concentrated a person’s urine appears?', ['With less water available, the kidneys conserve water, producing more concentrated urine', 'Dehydration never affects the concentration of a person’s urine', 'This concept has no relevance to science', 'The kidneys always produce urine of exactly the same concentration regardless of hydration'], 0)]),
SS('Social Studies: Ocean Plastic Pollution and Marine Debris',
   'Grade 9 Social Studies strand: ocean plastic pollution accumulates as human waste enters waterways and travels via ocean currents, often collecting in large garbage patches that harm marine ecosystems and coastal economies.',
   [('How does plastic pollution often enter the ocean?', ['Waste travelling through waterways and rivers into the sea', 'Plastic materializing directly within ocean water with no outside source', 'A concept unrelated to geography', 'Only through direct dumping from ships and nothing else'], 0),
    ('Do ocean currents help transport plastic debris into large collection zones?', ['Yes', 'No, ocean currents never transport any debris', 'A concept unrelated to marine debris', 'Plastic debris always stays exactly where it entered the ocean'], 0),
    ('What term describes a large area where ocean currents accumulate floating plastic debris?', ['A garbage patch', 'A coral reef', 'A concept unrelated to marine pollution', 'A continental shelf'], 0),
    ('Why might marine plastic pollution be especially harmful to sea turtles and seabirds?', ['They can mistake plastic debris for food, ingesting it, or become entangled in it', 'Sea turtles and seabirds are never affected by plastic debris in the ocean', 'This concept has no connection to geography', 'Plastic debris always sinks immediately and never affects marine wildlife'], 0),
    ('Why is ocean plastic pollution considered a geographic issue that crosses national borders?', ['Ocean currents can carry debris far from its original source, affecting coastlines and countries far away', 'Ocean plastic pollution always stays within the borders of the country where it originated', 'This concept has no relevance to social studies', 'Ocean currents never carry pollution beyond the country where it entered the water'], 0)]),
]),

day(109, [
L('Media Literacy: Fact vs Opinion in News Reporting',
  'Grade 9 Language strand: a fact is a statement that can be verified as true or false with evidence, while an opinion expresses a personal belief or judgment, and distinguishing them is essential for evaluating news reporting.',
  [('What can a fact be verified with?', ['Evidence', 'Personal feelings alone', 'A concept unrelated to media literacy', 'A guess with no supporting information'], 0),
   ('Does an opinion express a personal belief or judgment?', ['Yes', 'No, an opinion never expresses a personal belief', 'A concept unrelated to opinions', 'Opinions are always identical to verifiable facts'], 0),
   ('Which of these is a fact rather than an opinion?', ['The meeting started at 9 a.m.', 'The meeting was far too long and boring.', 'That was the best meeting ever held.', 'The meeting should have been shorter.'], 0),
   ('Why might a news article blend fact and opinion in a way that misleads readers?', ['Presenting opinion using confident, factual-sounding language can make it seem more objective than it is', 'Blending fact and opinion never affects how a reader interprets a news article', 'This concept has no connection to media literacy', 'News articles are always required by law to separate fact and opinion clearly'], 0),
   ('Why is distinguishing fact from opinion an important media literacy skill?', ['It helps readers evaluate the reliability and objectivity of the information they consume', 'Distinguishing fact from opinion never helps a reader evaluate information', 'This concept has no relevance to media literacy', 'Every statement in a news report is always either entirely fact or entirely opinion with no ambiguity'], 0)]),
M('Simplifying Cube Roots and Higher-Order Radicals',
  'Grade 9 Math strand: a cube root asks what number multiplied by itself three times equals the radicand, and higher-order radicals extend this idea to nth roots, simplified by identifying perfect nth-power factors.',
  [('What does a cube root ask you to find?', ['A number that, multiplied by itself three times, equals the radicand', 'A number that, multiplied by itself twice, equals the radicand', 'A concept unrelated to radicals', 'The largest factor of a given number'], 0),
   ('Can higher-order radicals be simplified by identifying perfect nth-power factors?', ['Yes', 'No, higher-order radicals can never be simplified', 'A concept unrelated to higher-order radicals', 'Simplifying radicals only ever applies to square roots'], 0),
   ('What is the cube root of 27?', ['3', '9', '6', '27'], 0),
   ('What is the cube root of 64?', ['4', '8', '16', '32'], 0),
   ('Why can a cube root produce a negative result while a square root of a positive number cannot?', ['A negative number multiplied by itself an odd number of times remains negative, unlike squaring which always gives a positive result', 'Cube roots and square roots always behave in exactly the same way with negative numbers', 'This concept has no connection to math', 'A cube root can never produce a negative result under any circumstances'], 0)]),
Sc('Science: Cell Division: Mitosis and Meiosis',
   'Grade 9 Science strand: mitosis produces two genetically identical daughter cells for growth and repair, while meiosis produces four genetically unique reproductive cells (gametes) with half the chromosome number.',
   [('What does mitosis produce?', ['Two genetically identical daughter cells', 'Four genetically unique reproductive cells', 'A concept unrelated to biology', 'A single cell with double the original chromosome number'], 0),
    ('Does meiosis produce reproductive cells with half the chromosome number?', ['Yes', 'No, meiosis never changes the number of chromosomes', 'A concept unrelated to meiosis', 'Meiosis always doubles the chromosome number instead'], 0),
    ('Which type of cell division is used for growth and tissue repair?', ['Mitosis', 'Meiosis', 'A concept unrelated to cell division', 'Neither mitosis nor meiosis is ever used for growth'], 0),
    ('Why does meiosis produce four genetically unique cells rather than two identical ones?', ['It involves genetic recombination and independent assortment, creating unique combinations of chromosomes', 'Meiosis always produces cells that are perfectly identical to one another', 'This concept has no connection to biology', 'Genetic recombination never occurs during meiosis'], 0),
    ('Why is it important that gametes produced by meiosis have half the normal chromosome number?', ['So that when two gametes combine during fertilization, the resulting offspring has the correct full chromosome number', 'Gametes never need to have a reduced chromosome number for reproduction to work', 'This concept has no relevance to science', 'Fertilization always results in offspring with double the normal chromosome number'], 0)]),
SS('Social Studies: The Geography of Renewable Wind Energy Siting',
   'Grade 9 Social Studies strand: wind energy generation depends heavily on geographic siting factors such as consistent wind speed, open land or offshore location, and proximity to transmission infrastructure.',
   [('What geographic factor is essential for effective wind energy generation?', ['Consistent wind speed', 'A region with no wind at all', 'A concept unrelated to geography', 'A densely forested valley with no open space'], 0),
    ('Can wind turbines be sited offshore to take advantage of strong, consistent ocean winds?', ['Yes', 'No, wind turbines can never be placed offshore', 'A concept unrelated to wind energy siting', 'Offshore locations never provide any advantage for wind energy'], 0),
    ('Which of these locations would likely be well-suited for a wind farm?', ['An open plain or coastal area with strong, steady winds', 'A sheltered valley with little to no wind', 'A concept unrelated to wind energy', 'A densely populated downtown core with tall buildings'], 0),
    ('Why might wind turbines be sited far from residential areas despite being a clean energy source?', ['Concerns about noise, visual impact, and effects on local wildlife can make nearby communities hesitant', 'Wind turbines never raise any concerns among nearby residents', 'This concept has no connection to geography', 'Wind turbines are always required by law to be built next to residential neighbourhoods'], 0),
    ('Why is proximity to transmission infrastructure an important siting consideration for a wind farm?', ['Electricity generated must be efficiently transported to where it will be consumed, requiring nearby grid connections', 'Transmission infrastructure never affects where a wind farm should be built', 'This concept has no relevance to social studies', 'Wind farms never need to be connected to any electrical grid'], 0)]),
]),

day(110, [
L('Review: Personification, Grammar, Figurative Language, and Media Literacy (Days 101-109)',
  'Grade 9 Language strand review: students revisit personification and pathetic fallacy, comma splices and fused sentences, hyperbole and understatement, apostrophes for possession and contraction, and fact vs opinion in news reporting.',
  [('What is personification?', ['A literary device that gives human qualities to non-human things', 'A device that removes all emotion from a poem', 'A concept unrelated to reading', 'A type of formal persuasive essay'], 0),
   ('What is a comma splice?', ['Two independent clauses joined incorrectly by only a comma', 'A sentence with no punctuation errors at all', 'A concept unrelated to grammar', 'A single independent clause with a period at the end'], 0),
   ('What is hyperbole?', ['Deliberate exaggeration for emphasis or effect', 'A precise, literal description with no exaggeration', 'A concept unrelated to reading', 'A type of formal citation'], 0),
   ('How is possession typically shown for a singular noun?', ['Add an apostrophe and s', 'Add only an s with no apostrophe', 'A concept unrelated to grammar', 'Add an apostrophe at the very start of the word'], 0),
   ('What can a fact be verified with?', ['Evidence', 'Personal feelings alone', 'A concept unrelated to media literacy', 'A guess with no supporting information'], 0)]),
M('Review: Factoring, Data Management, Equations, and Radicals (Days 101-109)',
  'Grade 9 Math strand review: students revisit factoring trinomials, frequency tables and histograms, solving multi-step equations with fractions and decimals, multiplying and dividing rational expressions, and simplifying cube roots.',
  [('When factoring x^2 + bx + c, what must the two numbers multiply to?', ['c', 'b', 'A concept unrelated to factoring', 'x'], 0),
   ('What does a frequency table organize?', ['Data into intervals with a count of how many values fall in each', 'A single value repeated many times with no intervals', 'A concept unrelated to data management', 'Only the largest and smallest values in a data set'], 0),
   ('What is a common first step when solving an equation containing fractions?', ['Multiply every term by the common denominator to clear the fractions', 'Immediately divide every term by zero', 'A concept unrelated to solving equations', 'Ignore the fractions and solve only with the whole numbers present'], 0),
   ('When multiplying rational expressions, what should be done after multiplying the numerators and denominators?', ['Simplify by cancelling common factors', 'Immediately add the two denominators together', 'A concept unrelated to rational expressions', 'Discard the denominators entirely'], 0),
   ('What does a cube root ask you to find?', ['A number that, multiplied by itself three times, equals the radicand', 'A number that, multiplied by itself twice, equals the radicand', 'A concept unrelated to radicals', 'The largest factor of a given number'], 0)]),
Sc('Review: Earth Science, Biology, Chemistry, and Physics (Days 101-109)',
   'Grade 9 Science strand review: students revisit volcanoes and volcanic activity, cell transport by diffusion and osmosis, the particle theory of matter, weather systems, and cell division by mitosis and meiosis.',
   [('What is magma called once it reaches the Earth’s surface?', ['Lava', 'Sediment', 'A concept unrelated to volcanoes', 'Ash only'], 0),
    ('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The movement of particles from lower to higher concentration only', 'A concept unrelated to biology', 'A process that only occurs inside solid rocks'], 0),
    ('According to the particle theory of matter, what is all matter made of?', ['Tiny particles in constant motion', 'A single continuous substance with no particles', 'A concept unrelated to chemistry', 'Only visible solid chunks with no motion'], 0),
    ('What is an air mass?', ['A large body of air with fairly uniform temperature and humidity', 'A single raindrop falling from a cloud', 'A concept unrelated to earth science', 'A small pocket of gas found underground'], 0),
    ('What does mitosis produce?', ['Two genetically identical daughter cells', 'Four genetically unique reproductive cells', 'A concept unrelated to biology', 'A single cell with double the original chromosome number'], 0)]),
SS('Review: Geography and Global Issues (Days 101-109)',
   'Grade 9 Social Studies strand review: students revisit ecological footprint, aging populations and the dependency ratio, separatist movements, smart cities, and the geography of wind energy siting.',
   [('What does an ecological footprint measure?', ['The land and resources required to support a lifestyle and absorb its waste', 'The total population of a country', 'A concept unrelated to geography', 'The average temperature of a region'], 0),
    ('What does the dependency ratio compare?', ['The number of dependents to the working-age population', 'The number of cities to the number of provinces', 'A concept unrelated to population geography', 'The total land area to the total population'], 0),
    ('What does a separatist movement typically seek for a region within a larger country?', ['Independence or greater autonomy', 'Complete elimination of all regional governments', 'A concept unrelated to political geography', 'Total merger with a neighbouring country’s government'], 0),
    ('What does a smart city use to improve urban services?', ['Digital technology and data collection', 'Only traditional paper-based record keeping', 'A concept unrelated to urban geography', 'A complete absence of any infrastructure'], 0),
    ('What geographic factor is essential for effective wind energy generation?', ['Consistent wind speed', 'A region with no wind at all', 'A concept unrelated to geography', 'A densely forested valley with no open space'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_101_110)
    append_to(9, g9_101_110)
