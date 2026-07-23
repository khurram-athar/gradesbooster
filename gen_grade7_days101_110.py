#!/usr/bin/env python3
"""Grade 7, Days 101-110 -- extends Grade 7 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade7.json): participial phrases, onomatopoeia and sound devices,
allusion in literature, descriptive essays and sensory details, political
cartoons, ellipses and parentheses, colloquialisms and regional dialects,
genre conventions in mystery fiction, letters to the editor; multiplying
a monomial by a polynomial, central angles and arcs of a circle, solving
equations with the distributive property, unit rates and comparison
shopping, histograms and grouped frequency data, the exterior angle
theorem, mutually exclusive events, perfect cubes and cube roots, scatter
plots and line of best fit; the electromagnetic spectrum and visible
light, cloud types and precipitation, biomass and biofuels, enzymes as
biological catalysts, mineral identification, pendulums and periodic
motion, biomagnification of toxins, animal migration and navigation,
soil composition and horizons; the Winnipeg General Strike, the Halifax
Explosion, Japanese Canadian internment during World War II, the
Canadian Bill of Rights, the Indian Act, the Numbered Treaties, the St.
Lawrence Seaway, Canada's peacekeeping mission in Rwanda, and the
Canadian Shield.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260926):
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


g7_101_110 = [
day(101, [
L('Grammar: Participial Phrases',
  'Grade 7 Language strand: a participial phrase begins with a present or past participle, a verb ending in -ing or -ed, and acts as an adjective to describe a noun, such as Laughing loudly, the children ran across the yard.',
  [('What does a participial phrase begin with?', ['A present or past participle', 'A coordinating conjunction', 'A concept unrelated to grammar', 'A prepositional phrase only'], 0),
   ('In the sentence Exhausted from the race, Maria collapsed on the couch, what is the participial phrase?', ['Exhausted from the race', 'Maria collapsed', 'On the couch', 'A concept unrelated to participial phrases'], 0),
   ('Does a participial phrase function as an adjective, describing a noun?', ['Yes', 'No, it always functions as a verb', 'A concept unrelated to participial phrases', 'It always functions as an adverb only'], 0),
   ('Why might a writer use a participial phrase instead of two separate short sentences?', ['It can combine related ideas smoothly and add descriptive detail', 'Participial phrases always make writing choppier', 'This concept has no connection to grammar', 'Two short sentences are always clearer than one combined sentence'], 0),
   ('Which sentence correctly uses a participial phrase?', ['Running down the hill, the dog chased the ball.', 'Running down the hill the dog the ball chased.', 'The dog running chased down hill the ball.', 'Down the hill running chased the dog ball.'], 0)]),
M('Multiplying a Monomial by a Polynomial',
  'Grade 7 Math strand: to multiply a monomial by a polynomial, the distributive property is applied so that the monomial multiplies every term inside the polynomial, such as 3x times (2x plus 5) equals 6x squared plus 15x.',
  [('What property is applied when multiplying a monomial by a polynomial?', ['The distributive property', 'The associative property only', 'A concept unrelated to algebra', 'The property of subtraction'], 0),
   ('What is 3x times (2x plus 5)?', ['6x squared plus 15x', '5x squared plus 15', '6x plus 15x', '2x squared plus 5x'], 0),
   ('Does the monomial need to multiply every single term inside the polynomial?', ['Yes', 'No, only the first term needs to be multiplied', 'A concept unrelated to multiplying polynomials', 'Only the last term needs to be multiplied'], 0),
   ('Why is it important to keep track of signs when multiplying a monomial by a polynomial containing subtraction?', ['A missed negative sign can change the value of a term in the result', 'Signs never affect the result of multiplication', 'This concept has no connection to algebra', 'Subtraction is never involved in this type of problem'], 0),
   ('What is 4y times (y minus 3)?', ['4y squared minus 12y', '4y squared minus 3', 'y squared minus 12y', '4y minus 12y'], 0)]),
Sc('Science: The Electromagnetic Spectrum and Visible Light',
   'Grade 7 Science strand: the electromagnetic spectrum is the full range of electromagnetic waves, from radio waves to gamma rays, and visible light is only the small portion of that spectrum that human eyes can detect.',
   [('What is the electromagnetic spectrum?', ['The full range of electromagnetic waves, from radio waves to gamma rays', 'A single type of visible light only', 'A concept unrelated to science', 'A tool used only to measure temperature'], 0),
    ('Is visible light only a small portion of the entire electromagnetic spectrum?', ['Yes', 'No, visible light makes up the entire spectrum', 'A concept unrelated to the electromagnetic spectrum', 'Visible light and the spectrum are unrelated ideas'], 0),
    ('Which of these has a longer wavelength than visible light?', ['Radio waves', 'Gamma rays', 'X-rays', 'Ultraviolet light'], 0),
    ('Why can humans see visible light but not other parts of the electromagnetic spectrum, like radio waves?', ['Human eyes contain receptors that only respond to a narrow range of wavelengths', 'Human eyes can detect every part of the electromagnetic spectrum equally', 'This concept has no connection to biology', 'Radio waves and visible light are exactly the same thing'], 0),
    ('Why might doctors use X-rays, a higher-energy part of the spectrum, to see inside the human body?', ['X-rays can pass through soft tissue but are absorbed by denser material like bone, creating an image', 'X-rays are never able to pass through any part of the human body', 'This concept has no relevance to science', 'X-rays and visible light behave in exactly the same way inside the body'], 0)]),
SS('Social Studies: The Winnipeg General Strike of 1919',
   'Grade 7 Social Studies strand: the Winnipeg General Strike of 1919 was a massive labour strike in which tens of thousands of workers walked off their jobs to demand better wages, working conditions, and the right to collective bargaining.',
   [('What was the Winnipeg General Strike of 1919?', ['A massive labour strike where tens of thousands of workers walked off their jobs', 'A sports competition held across the prairies', 'A concept unrelated to Canadian history', 'A festival celebrating the founding of Winnipeg'], 0),
    ('In what year did the Winnipeg General Strike take place?', ['1919', '1867', '1931', '1867'], 0),
    ('Did workers in the strike demand better wages and working conditions?', ['Yes', 'No, workers had no demands at all', 'A concept unrelated to the Winnipeg General Strike', 'Workers were protesting a change to the school calendar'], 0),
    ('Why might the Winnipeg General Strike be considered an important moment in Canadian labour history?', ['It showed the scale of worker frustration and helped shape future labour rights movements in Canada', 'It had no lasting effect on labour rights in Canada', 'This concept has no relevance to social studies', 'The strike involved only a handful of workers with no impact'], 0),
    ('Why might a strike involving tens of thousands of workers have significantly disrupted the city of Winnipeg?', ['Essential services and businesses could not operate normally without workers on the job', 'A strike of this size never affects how a city functions', 'This concept has no connection to Canadian history', 'Only a single business in Winnipeg was affected by the strike'], 0)]),
]),

day(102, [
L('Vocabulary: Onomatopoeia and Sound Devices',
  'Grade 7 Language strand: onomatopoeia is a word that imitates the sound it describes, such as buzz or crash, and is one of several sound devices writers use, along with alliteration and assonance, to create vivid imagery.',
  [('What is onomatopoeia?', ['A word that imitates the sound it describes', 'A word with no connection to sound at all', 'A concept unrelated to vocabulary', 'A word that always rhymes with another word'], 0),
   ('Which of these words is an example of onomatopoeia?', ['Buzz', 'Happy', 'Quickly', 'Beautiful'], 0),
   ('Is alliteration another example of a sound device used in writing?', ['Yes', 'No, alliteration is never considered a sound device', 'A concept unrelated to sound devices', 'Alliteration only appears in mathematics texts'], 0),
   ('Why might a poet use onomatopoeia when describing a thunderstorm?', ['It can help readers imagine the actual sounds of the storm more vividly', 'Onomatopoeia never adds any vividness to writing', 'This concept has no connection to vocabulary', 'Onomatopoeia is only used in scientific writing'], 0),
   ('Which sentence uses onomatopoeia?', ['The bacon sizzled in the pan.', 'The bacon cooked in the pan.', 'The bacon was on the pan.', 'The bacon smelled good.'], 0)]),
M('Central Angles and Arcs of a Circle',
  'Grade 7 Math strand: a central angle is an angle whose vertex is at the centre of a circle, and the arc it creates has a measure equal to the central angle, allowing students to relate angle measure to a fraction of the circle.',
  [('Where is the vertex of a central angle located?', ['At the centre of a circle', 'On the outer edge of a circle', 'A concept unrelated to circles', 'Outside of the circle entirely'], 0),
   ('Is the measure of an arc equal to the measure of its corresponding central angle?', ['Yes', 'No, an arc and its central angle are never related', 'A concept unrelated to central angles', 'An arc is always twice the measure of its central angle'], 0),
   ('If a central angle measures 90 degrees, what fraction of the full circle does its arc represent?', ['One quarter', 'One half', 'One third', 'One eighth'], 0),
   ('Why might understanding central angles help when calculating the length of an arc?', ['The central angle tells you what fraction of the full circle’s circumference the arc represents', 'Central angles never relate to the length of an arc', 'This concept has no connection to geometry', 'Arc length can only be measured using a ruler, never an angle'], 0),
   ('If a full circle is 360 degrees and a central angle measures 60 degrees, what fraction of the circle does that angle represent?', ['One sixth', 'One third', 'One quarter', 'One half'], 0)]),
Sc('Science: Cloud Types and Precipitation',
   'Grade 7 Science strand: clouds form when water vapour condenses around tiny particles in the air, and different cloud types, such as cumulus, stratus, and cirrus, can indicate different weather patterns and types of precipitation.',
   [('What happens when water vapour condenses around tiny particles in the air?', ['Clouds form', 'The air becomes completely dry', 'A concept unrelated to weather', 'The temperature always drops to freezing'], 0),
    ('Which cloud type is often associated with fair weather and a puffy, cotton-like appearance?', ['Cumulus', 'Cirrus', 'Stratus', 'Nimbus only'], 0),
    ('Can different cloud types indicate different weather patterns?', ['Yes', 'No, cloud type never relates to weather patterns', 'A concept unrelated to clouds', 'Every cloud type always predicts the exact same weather'], 0),
    ('Why might dark, thick clouds often signal an approaching storm?', ['Thicker clouds can hold more moisture, which may fall as rain or other precipitation', 'Dark clouds never contain any moisture at all', 'This concept has no connection to weather', 'Cloud thickness has no relationship to precipitation'], 0),
    ('Why do cirrus clouds, found high in the atmosphere, often look thin and wispy?', ['They are made mostly of ice crystals at a high altitude where temperatures are very cold', 'Cirrus clouds are always found at ground level', 'This concept has no relevance to science', 'Cirrus clouds are made entirely of liquid water droplets'], 0)]),
SS('Social Studies: The Halifax Explosion of 1917',
   'Grade 7 Social Studies strand: the Halifax Explosion of 1917 occurred when two ships collided in Halifax Harbour, one carrying wartime explosives, causing a massive blast that devastated the city and killed nearly 2,000 people.',
   [('What caused the Halifax Explosion of 1917?', ['Two ships collided in Halifax Harbour, one carrying wartime explosives', 'A severe winter storm destroyed the harbour', 'A concept unrelated to Canadian history', 'A fire started in a downtown bakery'], 0),
    ('In what year did the Halifax Explosion occur?', ['1917', '1867', '1931', '1990'], 0),
    ('Did the explosion cause significant devastation to the city of Halifax?', ['Yes', 'No, the city was completely unaffected', 'A concept unrelated to the Halifax Explosion', 'Only a small area outside the city was affected'], 0),
    ('Why might the Halifax Explosion be considered one of the largest man-made explosions before the nuclear age?', ['The blast released an enormous amount of energy that flattened much of the city’s north end', 'The explosion released almost no energy at all', 'This concept has no relevance to social studies', 'The explosion had no lasting effect on the city'], 0),
    ('Why might communities across Canada and beyond have sent aid to Halifax after the explosion?', ['The scale of destruction and loss of life created an urgent need for emergency support', 'No aid was ever sent to Halifax after the explosion', 'This concept has no connection to Canadian history', 'The explosion caused no injuries or damage requiring aid'], 0)]),
]),

day(103, [
L('Reading: Analyzing Allusion in Literature',
  'Grade 7 Language strand: an allusion is a brief reference to a person, place, event, or work of literature that a writer expects the reader to recognize, adding deeper meaning without lengthy explanation.',
  [('What is an allusion?', ['A brief reference to a person, place, event, or work of literature', 'A long, detailed explanation of an idea', 'A concept unrelated to reading', 'A footnote that defines a difficult word'], 0),
   ('Does an allusion typically rely on the reader already recognizing the reference?', ['Yes', 'No, allusions never require any background knowledge', 'A concept unrelated to allusion', 'Allusions always explain themselves in full detail'], 0),
   ('If a story describes a character’s difficult journey as an odyssey, what classic work is likely being alluded to?', ['Homer’s Odyssey', 'A modern comic book', 'A concept unrelated to allusion', 'A recent news article'], 0),
   ('Why might a writer use allusion instead of explaining an idea in full detail?', ['It can add deeper meaning quickly by connecting to something readers already know', 'Allusion never adds any meaning to a text', 'This concept has no connection to literature', 'Explaining an idea in full detail is always more effective than allusion'], 0),
   ('Why might an allusion fail to add meaning for a reader unfamiliar with the reference?', ['The reader may miss the deeper connection the writer intended to create', 'Allusions always work regardless of a reader’s background knowledge', 'This concept has no relevance to reading comprehension', 'Every reader automatically recognizes every allusion in a text'], 0)]),
M('Solving Equations Using the Distributive Property',
  'Grade 7 Math strand: some equations require applying the distributive property to remove brackets before combining like terms and isolating the variable, such as solving 2 times (x plus 3) equals 10.',
  [('What must often be applied before combining like terms in an equation with brackets?', ['The distributive property', 'The commutative property only', 'A concept unrelated to algebra', 'A random guess at the variable value'], 0),
   ('What is 2 times (x plus 3) after distributing?', ['2x plus 6', '2x plus 3', 'x plus 6', '2x plus 5'], 0),
   ('After distributing, does solving the equation usually involve isolating the variable?', ['Yes', 'No, the variable should always stay mixed with other terms', 'A concept unrelated to solving equations', 'Isolating the variable is never necessary in algebra'], 0),
   ('Why might skipping the distributive property lead to an incorrect solution when solving an equation with brackets?', ['Terms inside the brackets would not be properly multiplied by the number outside', 'Skipping this step never changes the final answer', 'This concept has no connection to algebra', 'Brackets never affect how an equation should be solved'], 0),
   ('Solve for x: 3 times (x minus 2) equals 12.', ['x equals 6', 'x equals 4', 'x equals 10', 'x equals 2'], 0)]),
Sc('Science: Renewable Energy: Biomass and Biofuels',
   'Grade 7 Science strand: biomass energy comes from burning or converting organic material, such as plants and waste, into usable energy, and biofuels are liquid fuels made from that organic material as a renewable alternative to fossil fuels.',
   [('What does biomass energy come from?', ['Organic material, such as plants and waste', 'Only fossil fuels like coal and oil', 'A concept unrelated to renewable energy', 'Nuclear reactions inside a reactor'], 0),
    ('What are biofuels?', ['Liquid fuels made from organic material', 'Solid rocks used to generate heat', 'A concept unrelated to biofuels', 'A type of non-renewable fossil fuel'], 0),
    ('Are biofuels considered a renewable alternative to fossil fuels?', ['Yes', 'No, biofuels are considered non-renewable', 'A concept unrelated to biofuels', 'Biofuels have no connection to renewable energy'], 0),
    ('Why might crop waste be a useful source of biomass energy?', ['It can be converted into energy instead of being discarded, reducing waste', 'Crop waste can never be converted into usable energy', 'This concept has no connection to renewable energy', 'Crop waste always has to be sent directly to a landfill'], 0),
    ('Why might some critics raise concerns about using food crops to produce large amounts of biofuel?', ['Using farmland for fuel crops instead of food crops could affect food supply and prices', 'Growing crops for fuel never has any effect on food supply', 'This concept has no relevance to science', 'Biofuels are always produced without using any farmland'], 0)]),
SS('Social Studies: Japanese Canadian Internment During World War II',
   'Grade 7 Social Studies strand: during World War II, the Canadian government forcibly relocated and interned thousands of Japanese Canadians, confiscating their property, an event now recognized as a serious violation of civil rights.',
   [('What happened to thousands of Japanese Canadians during World War II?', ['They were forcibly relocated and interned by the Canadian government', 'They were given additional land and property', 'A concept unrelated to Canadian history', 'They were granted full voting rights for the first time'], 0),
    ('During which conflict did the internment of Japanese Canadians take place?', ['World War II', 'World War I', 'The Korean War', 'The Cold War'], 0),
    ('Did the Canadian government confiscate property belonging to interned Japanese Canadians?', ['Yes', 'No, all property was left untouched', 'A concept unrelated to Japanese Canadian internment', 'Property was only confiscated from other countries, not Canada'], 0),
    ('Why is the internment of Japanese Canadians now recognized as a serious violation of civil rights?', ['Citizens were imprisoned and stripped of their property without being charged with any crime', 'Every interned person had committed a serious crime', 'This concept has no relevance to social studies', 'Internment had no effect on the rights of those involved'], 0),
    ('Why might the Canadian government’s later formal apology for this event be considered significant?', ['It acknowledged the historical injustice and aimed to provide some measure of restitution to survivors', 'An apology for this event would have no significance at all', 'This concept has no relevance to Canadian history', 'The government has never acknowledged this event in any way'], 0)]),
]),

day(104, [
L('Writing: Writing a Descriptive Essay Using Sensory Details',
  'Grade 7 Language strand: a descriptive essay uses sensory details, appealing to sight, sound, smell, taste, and touch, to help readers vividly picture a person, place, or experience.',
  [('What does a descriptive essay primarily use to help readers picture something vividly?', ['Sensory details', 'Only statistics and numbers', 'A concept unrelated to writing', 'A list of dictionary definitions'], 0),
   ('Which of these senses might a descriptive essay appeal to?', ['Smell', 'A concept unrelated to the senses', 'Only sight, never any other sense', 'None of the five senses'], 0),
   ('Should a descriptive essay generally include specific, vivid language rather than vague statements?', ['Yes', 'No, vague statements are always preferred', 'A concept unrelated to descriptive writing', 'Specific language should always be avoided in essays'], 0),
   ('Why might a writer describe the crunch of leaves underfoot rather than simply saying it was fall?', ['Specific sensory details create a more vivid and memorable picture for the reader', 'Sensory details never make writing more vivid', 'This concept has no connection to writing', 'General statements always create a stronger image than specific details'], 0),
   ('Which sentence best demonstrates a sensory detail in descriptive writing?', ['The salty ocean breeze stung my cheeks as waves crashed nearby.', 'I went to the beach yesterday.', 'The beach was nice.', 'I like going outside.'], 0)]),
M('Financial Literacy: Unit Rates and Comparison Shopping',
  'Grade 7 Math strand: a unit rate expresses a cost or quantity per single unit, such as price per 100 grams, allowing shoppers to compare products of different sizes to determine the better value.',
  [('What does a unit rate express?', ['A cost or quantity per single unit', 'The total price of every item combined', 'A concept unrelated to financial literacy', 'The weight of a product only'], 0),
   ('Why are unit rates useful when comparison shopping?', ['They allow shoppers to compare products of different sizes fairly', 'Unit rates make it impossible to compare products', 'This concept has no connection to shopping', 'Unit rates only apply to a single specific store'], 0),
   ('If a 500 g box of cereal costs 5 dollars, what is the unit rate per 100 g?', ['1 dollar per 100 g', '5 dollars per 100 g', '50 cents per 100 g', '2 dollars per 100 g'], 0),
   ('Between a 2 L bottle of juice for 4 dollars and a 3 L bottle for 5 dollars, which has the lower unit rate per litre?', ['The 3 L bottle for 5 dollars', 'The 2 L bottle for 4 dollars', 'They have the exact same unit rate', 'It cannot be determined from this information'], 0),
   ('Why might calculating unit rates help a shopper make a more informed decision than simply comparing total prices?', ['Total price alone does not account for differences in package size', 'Total price always gives the exact same information as a unit rate', 'This concept has no connection to financial literacy', 'Unit rates are never useful for making shopping decisions'], 0)]),
Sc('Science: Enzymes as Biological Catalysts',
   'Grade 7 Science strand: enzymes are proteins that act as biological catalysts, speeding up chemical reactions in the body, such as breaking down food during digestion, without being used up in the process.',
   [('What are enzymes?', ['Proteins that act as biological catalysts', 'Minerals found only in rocks', 'A concept unrelated to biology', 'A type of carbohydrate found in bread'], 0),
    ('What do enzymes do to chemical reactions in the body?', ['Speed them up', 'Slow them down permanently', 'A concept unrelated to enzymes', 'Stop them from happening entirely'], 0),
    ('Is an enzyme used up during the chemical reaction it speeds up?', ['No', 'Yes, enzymes are always used up completely', 'A concept unrelated to enzymes', 'Enzymes disappear entirely after a single reaction'], 0),
    ('Why might enzymes in saliva help begin the digestion of food before it even reaches the stomach?', ['They start breaking down certain molecules, like starches, as soon as food is chewed', 'Saliva never contains any enzymes at all', 'This concept has no connection to biology', 'Digestion only begins after food reaches the stomach'], 0),
    ('Why might a change in temperature affect how well an enzyme functions?', ['Enzymes often work best within a specific temperature range, and extreme temperatures can change their shape', 'Temperature never has any effect on how an enzyme works', 'This concept has no relevance to science', 'Enzymes always function identically at any temperature'], 0)]),
SS('Social Studies: The Canadian Bill of Rights (1960)',
   'Grade 7 Social Studies strand: the Canadian Bill of Rights, passed in 1960, was one of the first federal laws to protect individual rights and freedoms in Canada, later influencing the creation of the Charter of Rights and Freedoms in 1982.',
   [('In what year was the Canadian Bill of Rights passed?', ['1960', '1867', '1931', '1982'], 0),
    ('What did the Canadian Bill of Rights aim to protect?', ['Individual rights and freedoms', 'Provincial boundaries', 'A concept unrelated to Canadian history', 'Foreign trade agreements'], 0),
    ('Did the Canadian Bill of Rights later influence the creation of the Charter of Rights and Freedoms?', ['Yes', 'No, the two documents are completely unrelated', 'A concept unrelated to the Canadian Bill of Rights', 'The Charter was created decades before the Bill of Rights'], 0),
    ('Why might the Canadian Bill of Rights be considered an important step even though it had some limitations compared to the later Charter?', ['It was one of the first federal laws to formally recognize the protection of individual rights in Canada', 'It had no impact whatsoever on Canadian law', 'This concept has no relevance to social studies', 'It removed all individual rights that existed before 1960'], 0),
    ('Why might a law that only applied to federal matters have been seen as limited protection for all Canadians?', ['Provincial laws and matters were not covered, leaving some rights issues unaddressed', 'Provincial laws were always automatically covered by federal legislation', 'This concept has no connection to Canadian history', 'Every Canadian law applies equally to federal and provincial matters'], 0)]),
]),

day(105, [
L('Media Literacy: Analyzing Political Cartoons',
  'Grade 7 Language strand: a political cartoon uses images, symbols, and exaggeration to express an opinion about a current event or issue, requiring readers to interpret visual clues alongside any text.',
  [('What does a political cartoon use to express an opinion?', ['Images, symbols, and exaggeration', 'Only long paragraphs of formal text', 'A concept unrelated to media literacy', 'A detailed bibliography of sources'], 0),
   ('Does interpreting a political cartoon often require understanding symbols?', ['Yes', 'No, symbols are never used in political cartoons', 'A concept unrelated to political cartoons', 'Political cartoons never contain any hidden meaning'], 0),
   ('Why might a cartoonist use exaggeration when drawing a political figure?', ['It can emphasize a particular trait or point of view for humorous or critical effect', 'Exaggeration never adds meaning to a cartoon', 'This concept has no connection to media literacy', 'Cartoonists are required to draw figures with total realism'], 0),
   ('Why is background knowledge of a current event often necessary to fully understand a political cartoon?', ['The cartoon’s meaning often depends on recognizing the specific issue or people being referenced', 'Political cartoons never reference any real events', 'This concept has no relevance to media literacy', 'Every viewer understands a political cartoon in exactly the same way regardless of context'], 0),
   ('Which of these is most likely a feature found in a political cartoon?', ['A caricature of a public figure with exaggerated features', 'A detailed scientific diagram', 'A recipe for a meal', 'A weather forecast map'], 0)]),
M('Data: Histograms and Grouped Frequency Data',
  'Grade 7 Math strand: a histogram displays grouped numerical data as adjacent bars, where each bar represents a range of values, making it useful for showing the distribution of continuous data such as test scores or heights.',
  [('What does a histogram display?', ['Grouped numerical data as adjacent bars', 'A single number with no other data', 'A concept unrelated to data', 'Only categorical data with no numerical values'], 0),
   ('In a histogram, what does each bar typically represent?', ['A range of values', 'A single exact value only', 'A concept unrelated to histograms', 'A completely unrelated category'], 0),
   ('Are the bars in a histogram usually drawn touching each other, without gaps?', ['Yes', 'No, histogram bars always have large gaps between them', 'A concept unrelated to histograms', 'Histograms never use bars of any kind'], 0),
   ('Why might a histogram be useful for displaying a large set of continuous data, like the heights of 100 students?', ['Grouping the data into ranges makes patterns easier to see than listing every individual value', 'Histograms make large data sets impossible to interpret', 'This concept has no connection to data analysis', 'Continuous data can never be displayed using a histogram'], 0),
   ('Why is a histogram different from a bar graph that compares separate categories?', ['A histogram groups continuous numerical data into ranges rather than comparing distinct categories', 'A histogram and a bar graph are always exactly the same thing', 'This concept has no relevance to math', 'A histogram can only display a single data value at a time'], 0)]),
Sc('Science: Mineral Identification and Properties',
   'Grade 7 Science strand: minerals can be identified by testing physical properties such as hardness, streak colour, and lustre, allowing scientists to distinguish between different minerals even when they look similar.',
   [('What can be tested to help identify a mineral?', ['Physical properties such as hardness, streak colour, and lustre', 'Only the mineral’s exact weight in grams', 'A concept unrelated to earth science', 'The mineral’s distance from the ocean'], 0),
    ('What is streak colour?', ['The colour of the powder left when a mineral is scratched across a rough surface', 'The colour of a mineral only when wet', 'A concept unrelated to minerals', 'The colour of a mineral seen from a distance'], 0),
    ('Can two minerals that look similar in colour sometimes be told apart using a hardness test?', ['Yes', 'No, hardness never helps distinguish between minerals', 'A concept unrelated to mineral identification', 'Colour is the only property that ever matters'], 0),
    ('Why might a geologist use the Mohs hardness scale when identifying an unknown mineral?', ['It provides a standard way to compare how easily a mineral can be scratched', 'The Mohs scale has no connection to identifying minerals', 'This concept has no relevance to science', 'Hardness can only be measured using a microscope'], 0),
    ('Why is testing multiple properties, rather than just one, often necessary to correctly identify a mineral?', ['Some minerals can share one property, like colour, but differ in others, like hardness or lustre', 'A single property is always enough to identify any mineral', 'This concept has no connection to earth science', 'Minerals never share any properties with one another'], 0)]),
SS('Social Studies: The Indian Act and Its Historical Impact',
   'Grade 7 Social Studies strand: the Indian Act, first passed in 1876, is Canadian federal legislation that has controlled many aspects of the lives of First Nations peoples, and its ongoing impact remains an important part of understanding Indigenous rights today.',
   [('What is the Indian Act?', ['Canadian federal legislation that has controlled many aspects of the lives of First Nations peoples', 'A trade agreement between Canada and another country', 'A concept unrelated to Canadian history', 'A provincial law about highway construction'], 0),
    ('In what year was the Indian Act first passed?', ['1876', '1931', '1995', '1756'], 0),
    ('Does the Indian Act continue to have an impact on Indigenous rights today?', ['Yes', 'No, the Indian Act was repealed long ago and has no impact', 'A concept unrelated to the Indian Act', 'The Indian Act has never affected Indigenous peoples in any way'], 0),
    ('Why might the Indian Act be considered a controversial piece of legislation in Canadian history?', ['It gave the federal government significant control over the lives of First Nations peoples without their consent', 'It was created entirely by First Nations peoples for their own benefit', 'This concept has no relevance to social studies', 'It had no effect on the daily lives of First Nations peoples'], 0),
    ('Why is understanding the Indian Act important for learning about the relationship between the Canadian government and Indigenous peoples?', ['It helps explain many of the historical policies and ongoing issues affecting Indigenous rights and self-government', 'The Indian Act has no connection to Indigenous rights or self-government', 'This concept has no relevance to Canadian history', 'The relationship between the government and Indigenous peoples has never involved any legislation'], 0)]),
]),

day(106, [
L('Grammar: Using Ellipses and Parentheses',
  'Grade 7 Language strand: an ellipsis, three spaced dots, shows that words have been omitted or a thought trails off, while parentheses set off extra, non-essential information within a sentence.',
  [('What does an ellipsis show?', ['That words have been omitted or a thought trails off', 'That a sentence must always end immediately', 'A concept unrelated to grammar', 'That a word has been spelled incorrectly'], 0),
   ('What do parentheses set off in a sentence?', ['Extra, non-essential information', 'The single most important word in a sentence', 'A concept unrelated to parentheses', 'A sentence’s subject only'], 0),
   ('Is an ellipsis typically made up of three spaced dots?', ['Yes', 'No, an ellipsis is always a single dash', 'A concept unrelated to ellipses', 'An ellipsis is always exactly five dots'], 0),
   ('Why might a writer use parentheses to add a brief fact instead of writing a whole new sentence?', ['It can add relevant detail without interrupting the main flow of the sentence', 'Parentheses always make a sentence harder to understand', 'This concept has no connection to grammar', 'Parentheses should never be used to add extra information'], 0),
   ('Which sentence correctly uses parentheses?', ['My favourite city (which I have visited twice) is Vancouver.', 'My favourite city which I have visited twice is Vancouver (.)', 'My (favourite) city which I have visited twice is Vancouver.', 'My favourite city (is Vancouver which I have visited twice)'], 0)]),
M('The Exterior Angle Theorem for Triangles',
  'Grade 7 Math strand: the exterior angle theorem states that an exterior angle of a triangle is equal to the sum of the two non-adjacent interior angles, providing a shortcut for solving certain angle problems.',
  [('What does the exterior angle theorem state?', ['An exterior angle of a triangle equals the sum of the two non-adjacent interior angles', 'All exterior angles of a triangle are always equal to 90 degrees', 'A concept unrelated to geometry', 'An exterior angle is always smaller than any interior angle'], 0),
   ('If the two non-adjacent interior angles of a triangle measure 50 degrees and 60 degrees, what is the exterior angle?', ['110 degrees', '120 degrees', '100 degrees', '130 degrees'], 0),
   ('Is an exterior angle formed by extending one side of a triangle?', ['Yes', 'No, an exterior angle is never formed this way', 'A concept unrelated to exterior angles', 'An exterior angle is always located inside the triangle'], 0),
   ('Why might the exterior angle theorem be a useful shortcut instead of always using the fact that interior angles sum to 180 degrees?', ['It allows a missing angle to be found directly without extra subtraction steps', 'The exterior angle theorem never simplifies solving for a missing angle', 'This concept has no connection to geometry', 'The interior angles of a triangle never actually sum to 180 degrees'], 0),
   ('If an exterior angle measures 130 degrees and one non-adjacent interior angle measures 70 degrees, what is the other non-adjacent interior angle?', ['60 degrees', '50 degrees', '70 degrees', '80 degrees'], 0)]),
Sc('Science: Pendulums and Periodic Motion',
   'Grade 7 Science strand: a pendulum swings back and forth in a repeating pattern called periodic motion, and the time it takes to complete one full swing, called its period, depends mainly on the length of the pendulum.',
   [('What is periodic motion?', ['A repeating pattern of motion, like a pendulum swinging back and forth', 'Motion that only ever happens once', 'A concept unrelated to physics', 'Motion that never follows any pattern'], 0),
    ('What is the period of a pendulum?', ['The time it takes to complete one full swing', 'The exact height of the pendulum’s swing', 'A concept unrelated to pendulums', 'The colour of the pendulum’s string'], 0),
    ('Does the length of a pendulum mainly affect its period?', ['Yes', 'No, the length of a pendulum never affects its period', 'A concept unrelated to pendulums', 'Only the colour of a pendulum affects its period'], 0),
    ('Why might a longer pendulum take more time to complete one full swing than a shorter pendulum?', ['A longer pendulum has farther to travel in each swing, increasing the time of its period', 'A longer pendulum always swings at exactly the same speed as a shorter one', 'This concept has no connection to physics', 'Pendulum length has no effect on how far it must travel'], 0),
    ('Why do old mechanical clocks sometimes use a pendulum to help keep accurate time?', ['A pendulum’s period stays fairly consistent, allowing it to reliably mark equal intervals of time', 'A pendulum’s period changes randomly and cannot be relied upon', 'This concept has no relevance to science', 'Pendulums have never been used in any type of clock'], 0)]),
SS('Social Studies: The Numbered Treaties and Treaty Rights',
   'Grade 7 Social Studies strand: the Numbered Treaties were a series of agreements made between the Canadian government and First Nations between 1871 and 1921, addressing land use and rights, though their interpretation and fulfillment remain important ongoing issues.',
   [('What were the Numbered Treaties?', ['A series of agreements made between the Canadian government and First Nations', 'A list of provincial highway numbers', 'A concept unrelated to Canadian history', 'A set of trade tariffs with the United States'], 0),
    ('Between what years were the Numbered Treaties signed?', ['1871 and 1921', '1600 and 1700', '1980 and 2000', '1812 and 1815'], 0),
    ('Did the Numbered Treaties address issues related to land use and rights?', ['Yes', 'No, the treaties had no connection to land at all', 'A concept unrelated to the Numbered Treaties', 'The treaties only addressed matters of foreign trade'], 0),
    ('Why do questions about the interpretation and fulfillment of the Numbered Treaties remain important today?', ['Disagreements about what was originally promised continue to affect Indigenous rights and land claims', 'Every detail of the treaties has already been fully resolved with no disagreement', 'This concept has no relevance to social studies', 'The Numbered Treaties have no connection to Indigenous rights today'], 0),
    ('Why might First Nations and the Canadian government sometimes have different understandings of what a treaty promised?', ['Oral agreements and written text may not have fully matched the original spoken intentions of all parties', 'Every treaty was always understood in exactly the same way by all parties', 'This concept has no connection to Canadian history', 'Treaties were always written and agreed upon with no possibility of misunderstanding'], 0)]),
]),

day(107, [
L('Vocabulary: Colloquialisms and Regional Dialects',
  'Grade 7 Language strand: a colloquialism is an informal word or expression used in everyday conversation that may be specific to a particular region or dialect, such as pop versus soda for a carbonated drink.',
  [('What is a colloquialism?', ['An informal word or expression used in everyday conversation', 'A formal term used only in academic writing', 'A concept unrelated to vocabulary', 'A word that has only one possible meaning'], 0),
   ('Can a colloquialism vary depending on the region or dialect where it is used?', ['Yes', 'No, colloquialisms are always identical everywhere', 'A concept unrelated to colloquialisms', 'Colloquialisms never change based on location'], 0),
   ('Which of these word pairs is an example of regional colloquial variation for the same object?', ['Pop and soda', 'Book and pencil', 'Run and jump', 'Happy and sad'], 0),
   ('Why might a colloquialism be considered less appropriate in a formal essay than in casual conversation?', ['Formal writing typically favours standard, widely understood language over informal regional expressions', 'Colloquialisms are always required in formal essays', 'This concept has no connection to vocabulary', 'Formal writing never has any expectations about word choice'], 0),
   ('Why might understanding colloquialisms help someone communicate more naturally with people from a different region?', ['Recognizing regional expressions can help avoid confusion and connect more easily with local speech patterns', 'Colloquialisms never affect how people understand each other', 'This concept has no relevance to vocabulary', 'Every region of the world uses identical colloquial expressions'], 0)]),
M('Probability: Mutually Exclusive Events',
  'Grade 7 Math strand: two events are mutually exclusive if they cannot both happen at the same time, such as rolling a single die and getting both an even number and a 5, and their combined probability is found by adding their individual probabilities.',
  [('What does it mean for two events to be mutually exclusive?', ['They cannot both happen at the same time', 'They always happen at the exact same time', 'A concept unrelated to probability', 'They have no connection to each other whatsoever'], 0),
   ('If you roll a single die, can rolling an even number and rolling a 5 happen at the same time?', ['No', 'Yes, they can always happen together', 'A concept unrelated to mutually exclusive events', 'Rolling a die never produces an even number'], 0),
   ('How do you find the probability of two mutually exclusive events happening?', ['Add their individual probabilities', 'Multiply their individual probabilities together', 'A concept unrelated to probability', 'Subtract one probability from the other'], 0),
   ('On a single die roll, what is the probability of rolling a 2 or a 3?', ['2 out of 6', '1 out of 6', '3 out of 6', '4 out of 6'], 0),
   ('Why might drawing a red card or a black card from a standard deck be considered mutually exclusive events?', ['A single card cannot be both red and black at the same time', 'A single card is always both red and black at once', 'This concept has no connection to probability', 'Red and black cards never appear in a standard deck'], 0)]),
Sc('Science: Biomagnification of Toxins in Food Chains',
   'Grade 7 Science strand: biomagnification is the process by which the concentration of a toxin increases at each higher level of a food chain, meaning top predators often accumulate the highest levels of harmful substances.',
   [('What is biomagnification?', ['The process by which the concentration of a toxin increases at each higher level of a food chain', 'The process by which a toxin disappears completely from an ecosystem', 'A concept unrelated to biology', 'A process that only affects plants, never animals'], 0),
    ('Which organisms in a food chain often accumulate the highest levels of a toxin through biomagnification?', ['Top predators', 'The smallest organisms only', 'A concept unrelated to biomagnification', 'Organisms that never eat any other living things'], 0),
    ('Does the concentration of a toxin generally increase as it moves up a food chain?', ['Yes', 'No, toxin concentration always decreases up a food chain', 'A concept unrelated to biomagnification', 'Toxin concentration never changes throughout a food chain'], 0),
    ('Why might a small amount of a pollutant in water become a much bigger problem for a large predator fish?', ['Each organism the predator eats may already contain some of the toxin, so the amount adds up over time', 'Pollutants in water never affect any organism in a food chain', 'This concept has no connection to biology', 'Predator fish are always immune to any toxin in their environment'], 0),
    ('Why is biomagnification an important concept for understanding the effects of pollution on ecosystems?', ['It shows how even low levels of pollution can seriously harm organisms higher up the food chain', 'Biomagnification has no connection to the effects of pollution', 'This concept has no relevance to science', 'Pollution only ever affects the very first organism it touches'], 0)]),
SS('Social Studies: The St. Lawrence Seaway and Its Economic Impact',
   'Grade 7 Social Studies strand: the St. Lawrence Seaway is a system of canals and locks that allows ocean-going ships to travel deep into the interior of North America, greatly boosting trade and industry along the Great Lakes region.',
   [('What is the St. Lawrence Seaway?', ['A system of canals and locks that allows ships to travel deep into the interior of North America', 'A mountain range along the Canada-US border', 'A concept unrelated to Canadian history', 'A national park located in northern Ontario'], 0),
    ('Does the St. Lawrence Seaway allow ocean-going ships to reach the Great Lakes region?', ['Yes', 'No, ships can never reach the Great Lakes from the ocean', 'A concept unrelated to the St. Lawrence Seaway', 'The Great Lakes are not connected to the seaway in any way'], 0),
    ('What effect has the St. Lawrence Seaway had on trade and industry in the Great Lakes region?', ['It greatly boosted trade and industry', 'It had no effect on trade or industry at all', 'A concept unrelated to the St. Lawrence Seaway', 'It caused trade and industry in the region to disappear entirely'], 0),
    ('Why might locks be a necessary part of the St. Lawrence Seaway’s design?', ['Locks allow ships to be raised or lowered to different water levels along the waterway', 'Locks are only used to prevent ships from entering the waterway', 'This concept has no connection to social studies', 'Water levels along the seaway are always exactly the same everywhere'], 0),
    ('Why might the St. Lawrence Seaway be considered an important joint project between Canada and the United States?', ['Both countries share the waterway and benefit economically from the trade it supports', 'Only one country benefits from the seaway, with no involvement from the other', 'This concept has no relevance to social studies', 'The seaway was built entirely without any international cooperation'], 0)]),
]),

day(108, [
L('Reading: Understanding Genre Conventions in Mystery Fiction',
  'Grade 7 Language strand: mystery fiction follows certain genre conventions, such as a central puzzle or crime, clues planted throughout the story, red herrings, and a detective or investigator who solves the case.',
  [('What is often at the centre of a mystery story?', ['A puzzle or crime to be solved', 'A detailed description of the weather', 'A concept unrelated to reading', 'A recipe that characters follow'], 0),
   ('What is a red herring in a mystery story?', ['A clue meant to mislead the reader or investigator', 'The final solution to the mystery', 'A concept unrelated to mystery fiction', 'The main setting of the story'], 0),
   ('Does mystery fiction typically include clues planted throughout the story?', ['Yes', 'No, clues are never included in mystery fiction', 'A concept unrelated to mystery fiction', 'Clues only ever appear at the very end of the story'], 0),
   ('Why might an author include a red herring in a mystery story?', ['It can build suspense by making readers suspect the wrong solution', 'A red herring always reveals the true solution immediately', 'This concept has no connection to literature', 'Red herrings are never used in mystery fiction'], 0),
   ('Why is recognizing genre conventions, like clues and red herrings, helpful when reading a mystery story?', ['It helps readers actively look for evidence and try to solve the puzzle alongside the characters', 'Genre conventions never help a reader understand a mystery story', 'This concept has no relevance to reading comprehension', 'Mystery stories never follow any recognizable conventions'], 0)]),
M('Number Theory: Perfect Cubes and Cube Roots',
  'Grade 7 Math strand: a perfect cube is a number produced by multiplying an integer by itself three times, such as 8 being 2 cubed, and the cube root reverses that operation to find the original number.',
  [('What is a perfect cube?', ['A number produced by multiplying an integer by itself three times', 'Any number that is divisible by 3', 'A concept unrelated to number theory', 'A number that can never be divided evenly'], 0),
   ('What is 2 cubed?', ['8', '6', '4', '9'], 0),
   ('What does the cube root of a number find?', ['The original number that was multiplied by itself three times', 'The sum of a number added to itself three times', 'A concept unrelated to cube roots', 'The number doubled and then tripled'], 0),
   ('What is the cube root of 27?', ['3', '9', '27', '6'], 0),
   ('Why is 10 not a perfect cube?', ['No whole number multiplied by itself three times equals 10', 'Every number is automatically considered a perfect cube', 'This concept has no connection to math', '10 is always considered both a perfect cube and a perfect square'], 0)]),
Sc('Science: Animal Migration Patterns and Navigation',
   'Grade 7 Science strand: many animals migrate long distances between habitats on a seasonal basis, using natural cues such as the position of the sun, Earth’s magnetic field, and landmarks to navigate accurately.',
   [('What is animal migration?', ['Movement of animals over long distances between habitats on a seasonal basis', 'A permanent move to a single habitat with no return', 'A concept unrelated to biology', 'Movement that only ever happens within a single small area'], 0),
    ('Name one natural cue animals may use to navigate during migration.', ['Earth’s magnetic field', 'A concept unrelated to migration', 'Random guessing with no natural cues', 'Following a printed map'], 0),
    ('Can the position of the sun help some animals navigate during migration?', ['Yes', 'No, the position of the sun never helps with navigation', 'A concept unrelated to animal migration', 'Only artificial light can help animals navigate'], 0),
    ('Why might birds migrate south for the winter?', ['To find warmer temperatures and more available food sources', 'Birds never migrate for any reason', 'This concept has no connection to biology', 'Migrating south always makes conditions colder for birds'], 0),
    ('Why might scientists study animal migration patterns to help with conservation efforts?', ['Understanding migration routes can help protect the habitats animals depend on along their journey', 'Migration patterns have no connection to conservation efforts', 'This concept has no relevance to science', 'Protecting habitats never requires understanding where animals travel'], 0)]),
SS('Social Studies: Canada’s Peacekeeping Mission in Rwanda',
   'Grade 7 Social Studies strand: in 1994, Canadian General Roméo Dallaire led a United Nations peacekeeping mission in Rwanda during a devastating genocide, an experience that later shaped important conversations about the limits and responsibilities of peacekeeping.',
   [('Who led the United Nations peacekeeping mission in Rwanda in 1994?', ['Canadian General Roméo Dallaire', 'A Canadian prime minister', 'A concept unrelated to Canadian history', 'A member of the Canadian Senate'], 0),
    ('In what year did the Rwandan genocide and the peacekeeping mission take place?', ['1994', '1917', '1931', '1960'], 0),
    ('Did the peacekeeping mission in Rwanda take place during a devastating genocide?', ['Yes', 'No, the mission had no connection to any genocide', 'A concept unrelated to the Rwanda mission', 'The mission took place decades after the genocide ended'], 0),
    ('Why might the events in Rwanda have shaped later conversations about the responsibilities of international peacekeeping?', ['The mission highlighted the challenges peacekeepers faced when given limited resources and authority to prevent mass violence', 'The mission had no impact on how peacekeeping is discussed today', 'This concept has no relevance to social studies', 'Peacekeeping missions never face any challenges or limitations'], 0),
    ('Why might learning about Canada’s role in Rwanda be important for understanding the history of Canadian peacekeeping?', ['It shows both the significant challenges and the moral responsibility involved in international peacekeeping efforts', 'Canada has never played any role in international peacekeeping', 'This concept has no relevance to Canadian history', 'Peacekeeping missions have no connection to Canadian history at all'], 0)]),
]),

day(109, [
L('Writing: Writing a Letter to the Editor',
  'Grade 7 Language strand: a letter to the editor expresses a writer’s opinion on a current issue in a newspaper or publication, using a clear argument, supporting evidence, and a respectful, persuasive tone.',
  [('What does a letter to the editor typically express?', ['A writer’s opinion on a current issue', 'A recipe for a favourite meal', 'A concept unrelated to writing', 'The plot summary of a novel'], 0),
   ('Should a letter to the editor generally include supporting evidence for its argument?', ['Yes', 'No, evidence should never be included', 'A concept unrelated to letters to the editor', 'Only opinions with no evidence should ever be included'], 0),
   ('Is a respectful, persuasive tone generally appropriate for a letter to the editor?', ['Yes', 'No, an angry, disrespectful tone is always preferred', 'A concept unrelated to tone in writing', 'Tone never matters when writing a letter to the editor'], 0),
   ('Why might someone write a letter to the editor instead of only discussing an issue with friends?', ['It can reach a wider audience and potentially influence public opinion or policy', 'A letter to the editor never reaches anyone beyond the writer’s friends', 'This concept has no connection to writing', 'Discussing an issue with friends always has a bigger impact than publishing a letter'], 0),
   ('Which of these sentences sounds most like the opening of a letter to the editor?', ['I am writing to express my concern about the proposed changes to our local park.', 'Once upon a time, in a faraway kingdom.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.'], 0)]),
M('Data: Scatter Plots and Line of Best Fit',
  'Grade 7 Math strand: a scatter plot displays the relationship between two numerical variables as points on a graph, and a line of best fit can be drawn to estimate the overall trend in the data.',
  [('What does a scatter plot display?', ['The relationship between two numerical variables as points on a graph', 'A single category with no numerical data', 'A concept unrelated to data', 'A list of names with no numbers at all'], 0),
   ('What does a line of best fit help estimate?', ['The overall trend in the data', 'The exact value of every single data point', 'A concept unrelated to scatter plots', 'The colour used to display the data'], 0),
   ('Can a scatter plot help reveal whether two variables have a positive, negative, or no relationship?', ['Yes', 'No, scatter plots never reveal any relationship between variables', 'A concept unrelated to scatter plots', 'Scatter plots can only display a single variable at a time'], 0),
   ('Why might a line of best fit not pass through every single point on a scatter plot?', ['It represents the general trend of the data rather than every exact value', 'A line of best fit is required to pass through every single point', 'This concept has no connection to data analysis', 'Scatter plots never contain more than one data point'], 0),
   ('If a scatter plot shows that as study time increases, test scores tend to increase, what kind of relationship does this suggest?', ['A positive relationship', 'A negative relationship', 'No relationship at all', 'An impossible relationship to determine'], 0)]),
Sc('Science: Soil Composition and Horizons',
   'Grade 7 Science strand: soil is composed of weathered rock, organic matter, water, and air, and is typically organized into distinct layers called horizons, each with different composition and properties.',
   [('What is soil composed of?', ['Weathered rock, organic matter, water, and air', 'Only solid rock with nothing else', 'A concept unrelated to earth science', 'Purely liquid water with no solid material'], 0),
    ('What are the distinct layers of soil called?', ['Horizons', 'Strata clouds', 'A concept unrelated to soil', 'Tectonic plates'], 0),
    ('Do different soil horizons typically have different composition and properties?', ['Yes', 'No, every soil horizon is always identical', 'A concept unrelated to soil horizons', 'Soil horizons never differ from one region to another'], 0),
    ('Why is the topmost layer of soil, often rich in organic matter, especially important for plant growth?', ['It typically contains the most nutrients that plants need to grow', 'The topmost layer never contains any nutrients at all', 'This concept has no connection to biology', 'Plants only ever get nutrients from deep underground layers'], 0),
    ('Why might soil composition vary significantly between different regions?', ['Differences in climate, parent rock material, and organic activity affect how soil forms in each region', 'Soil composition is always exactly the same everywhere on Earth', 'This concept has no relevance to science', 'Climate and rock material never have any effect on soil formation'], 0)]),
SS('Social Studies: The Canadian Shield: Geology and Geography',
   'Grade 7 Social Studies strand: the Canadian Shield is a vast region of ancient rock covering much of central and eastern Canada, rich in minerals but generally poor for large-scale farming due to its thin, rocky soil.',
   [('What is the Canadian Shield?', ['A vast region of ancient rock covering much of central and eastern Canada', 'A mountain range along the Pacific coast', 'A concept unrelated to Canadian geography', 'A large freshwater lake in northern Ontario'], 0),
    ('Is the Canadian Shield generally rich in minerals?', ['Yes', 'No, the Canadian Shield contains no minerals at all', 'A concept unrelated to the Canadian Shield', 'Minerals are only found outside of the Canadian Shield'], 0),
    ('Is the Canadian Shield generally well suited for large-scale farming?', ['No', 'Yes, it is considered ideal for large-scale farming', 'A concept unrelated to the Canadian Shield', 'Farming has never been attempted anywhere near the Canadian Shield'], 0),
    ('Why might the Canadian Shield’s thin, rocky soil make large-scale farming difficult in that region?', ['Thin soil provides limited nutrients and depth for crops to grow successfully', 'Thin soil always provides unlimited nutrients for crops', 'This concept has no connection to geography', 'Rocky soil has no effect on how well crops can grow'], 0),
    ('Why is the Canadian Shield considered economically important despite its limitations for farming?', ['Its mineral resources support significant mining industries across the region', 'The Canadian Shield has no economic importance of any kind', 'This concept has no relevance to social studies', 'Mining has never taken place anywhere within the Canadian Shield'], 0)]),
]),

day(110, [
L('Review: Grammar, Vocabulary, and Reading (Days 101-109)',
  'Grade 7 Language strand review: students revisit participial phrases, allusion, political cartoons, colloquialisms, and letters to the editor.',
  [('What does a participial phrase begin with?', ['A present or past participle', 'A coordinating conjunction', 'A concept unrelated to grammar', 'A prepositional phrase only'], 0),
   ('What is an allusion?', ['A brief reference to a person, place, event, or work of literature', 'A long, detailed explanation of an idea', 'A concept unrelated to reading', 'A footnote that defines a difficult word'], 0),
   ('What does a political cartoon use to express an opinion?', ['Images, symbols, and exaggeration', 'Only long paragraphs of formal text', 'A concept unrelated to media literacy', 'A detailed bibliography of sources'], 0),
   ('What is a colloquialism?', ['An informal word or expression used in everyday conversation', 'A formal term used only in academic writing', 'A concept unrelated to vocabulary', 'A word that has only one possible meaning'], 0),
   ('What does a letter to the editor typically express?', ['A writer’s opinion on a current issue', 'A recipe for a favourite meal', 'A concept unrelated to writing', 'The plot summary of a novel'], 0)]),
M('Review: Algebra, Geometry, and Data (Days 101-109)',
  'Grade 7 Math strand review: students revisit multiplying a monomial by a polynomial, the distributive property, histograms, mutually exclusive events, and scatter plots.',
  [('What property is applied when multiplying a monomial by a polynomial?', ['The distributive property', 'The associative property only', 'A concept unrelated to algebra', 'The property of subtraction'], 0),
   ('What must often be applied before combining like terms in an equation with brackets?', ['The distributive property', 'The commutative property only', 'A concept unrelated to algebra', 'A random guess at the variable value'], 0),
   ('What does a histogram display?', ['Grouped numerical data as adjacent bars', 'A single number with no other data', 'A concept unrelated to data', 'Only categorical data with no numerical values'], 0),
   ('What does it mean for two events to be mutually exclusive?', ['They cannot both happen at the same time', 'They always happen at the exact same time', 'A concept unrelated to probability', 'They have no connection to each other whatsoever'], 0),
   ('What does a scatter plot display?', ['The relationship between two numerical variables as points on a graph', 'A single category with no numerical data', 'A concept unrelated to data', 'A list of names with no numbers at all'], 0)]),
Sc('Review: Physics, Chemistry, and Earth Science (Days 101-109)',
   'Grade 7 Science strand review: students revisit the electromagnetic spectrum, biomass and biofuels, mineral identification, biomagnification, and soil composition.',
   [('What is the electromagnetic spectrum?', ['The full range of electromagnetic waves, from radio waves to gamma rays', 'A single type of visible light only', 'A concept unrelated to science', 'A tool used only to measure temperature'], 0),
    ('What does biomass energy come from?', ['Organic material, such as plants and waste', 'Only fossil fuels like coal and oil', 'A concept unrelated to renewable energy', 'Nuclear reactions inside a reactor'], 0),
    ('What can be tested to help identify a mineral?', ['Physical properties such as hardness, streak colour, and lustre', 'Only the mineral’s exact weight in grams', 'A concept unrelated to earth science', 'The mineral’s distance from the ocean'], 0),
    ('What is biomagnification?', ['The process by which the concentration of a toxin increases at each higher level of a food chain', 'The process by which a toxin disappears completely from an ecosystem', 'A concept unrelated to biology', 'A process that only affects plants, never animals'], 0),
    ('What is soil composed of?', ['Weathered rock, organic matter, water, and air', 'Only solid rock with nothing else', 'A concept unrelated to earth science', 'Purely liquid water with no solid material'], 0)]),
SS('Review: Canadian History and Society (Days 101-109)',
   'Grade 7 Social Studies strand review: students revisit the Winnipeg General Strike, Japanese Canadian internment, the Indian Act, the St. Lawrence Seaway, and the Canadian Shield.',
   [('What was the Winnipeg General Strike of 1919?', ['A massive labour strike where tens of thousands of workers walked off their jobs', 'A sports competition held across the prairies', 'A concept unrelated to Canadian history', 'A festival celebrating the founding of Winnipeg'], 0),
    ('What happened to thousands of Japanese Canadians during World War II?', ['They were forcibly relocated and interned by the Canadian government', 'They were given additional land and property', 'A concept unrelated to Canadian history', 'They were granted full voting rights for the first time'], 0),
    ('What is the Indian Act?', ['Canadian federal legislation that has controlled many aspects of the lives of First Nations peoples', 'A trade agreement between Canada and another country', 'A concept unrelated to Canadian history', 'A provincial law about highway construction'], 0),
    ('What is the St. Lawrence Seaway?', ['A system of canals and locks that allows ships to travel deep into the interior of North America', 'A mountain range along the Canada-US border', 'A concept unrelated to Canadian history', 'A national park located in northern Ontario'], 0),
    ('What is the Canadian Shield?', ['A vast region of ancient rock covering much of central and eastern Canada', 'A mountain range along the Pacific coast', 'A concept unrelated to Canadian geography', 'A large freshwater lake in northern Ontario'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_101_110)
    append_to(7, g7_101_110)
