#!/usr/bin/env python3
"""Grade 9, Days 91-100 -- extends Grade 9 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade9.json):
allegory, definition essays, gerunds/infinitives/verbals, euphemism and
doublespeak, allusion, writing a scene (dialogue and stage directions),
memes and internet culture, cohesion and transitional phrases, circular and
non-linear narrative structure; zero and negative exponents, graphing
quadratics in vertex form, mean/median/mode, income tax basics, angle of
elevation and depression, converting between forms of a linear equation,
independent and dependent probability events, interval notation, solving
systems graphically; physical vs chemical changes, conservation of mass,
taxonomy and classification, series and parallel circuits, biodiversity and
ecosystem stability, earthquakes and seismic waves, GMOs in agriculture,
metallic bonding and alloys, fossil fuel formation and impact; special
economic zones, border walls and migration control, urban gentrification,
critical mineral mining for batteries, data centres and cloud computing
geography, urban agriculture and vertical farming, air pollution and smog,
international aid and development, and cultural diffusion of cuisine.

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


def _rebalance_answer_positions(days, seed=20260928):
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


g9_91_100 = [
day(91, [
L('Reading: Analyzing Allegory in Literature',
  'Grade 9 Language strand: an allegory is a narrative in which characters, settings, and events symbolically represent deeper moral, political, or social meanings beyond the literal story.',
  [('What is an allegory?', ['A narrative whose characters and events symbolically represent deeper meanings', 'A concept unrelated to reading', 'A type of poem with no symbolic meaning', 'A factual news report'], 0),
   ('Does an allegory operate on both a literal and a symbolic level at the same time?', ['Yes', 'No, an allegory only ever has one literal meaning', 'A concept unrelated to allegory', 'Symbolic meaning has no connection to allegory'], 0),
   ('Which of these is an example of an allegorical story?', ['A story where farm animals represent political leaders and social classes', 'A weather report describing tomorrow’s forecast', 'A textbook chapter on cell biology', 'A grocery list of items to buy'], 0),
   ('Why might an author choose allegory instead of stating a message directly?', ['It allows complex political or moral ideas to be explored indirectly through symbolic story elements', 'Allegory never allows an author to explore any idea indirectly', 'This concept has no connection to literature', 'Allegories always state their message directly with no symbolism at all'], 0),
   ('Why is recognizing allegory useful when analyzing classic literature?', ['It reveals a deeper layer of commentary the author intends beyond the surface-level plot', 'Allegory never adds any deeper meaning to a story', 'This concept has no relevance to reading comprehension', 'Every story is an allegory with no distinction between literal and symbolic meaning'], 0)]),
M('Exponent Laws: Zero and Negative Exponents',
  'Grade 9 Math strand: any nonzero base raised to the exponent zero equals 1, and a negative exponent indicates the reciprocal of the base raised to the corresponding positive exponent.',
  [('What does any nonzero number raised to the exponent zero equal?', ['1', '0', 'The base itself', 'A concept unrelated to exponents'], 0),
   ('Does a negative exponent indicate the reciprocal of the base raised to the positive exponent?', ['Yes', 'No, negative exponents never involve a reciprocal', 'A concept unrelated to negative exponents', 'A negative exponent always makes the result negative'], 0),
   ('What is the value of 5 to the power of 0?', ['1', '5', '0', 'A concept unrelated to exponents'], 0),
   ('What is the value of 2 to the power of negative 3?', ['1/8', '-8', '8', '-1/8'], 0),
   ('Why is understanding zero and negative exponents useful when simplifying algebraic expressions?', ['It allows expressions with any integer exponent to be simplified consistently using the same exponent rules', 'Zero and negative exponents never appear in algebraic expressions', 'This concept has no connection to math', 'Negative exponents always make an expression impossible to simplify'], 0)]),
Sc('Science: Chemical vs Physical Changes: Identifying the Difference',
   'Grade 9 Science strand: a physical change alters a substance’s form without changing its chemical composition, while a chemical change produces one or more new substances with different properties.',
   [('What happens to a substance’s chemical composition during a physical change?', ['It stays the same', 'It always changes completely', 'A concept unrelated to physical changes', 'It is destroyed entirely'], 0),
    ('Does a chemical change produce one or more new substances?', ['Yes', 'No, chemical changes never produce any new substance', 'A concept unrelated to chemical changes', 'New substances only ever form during a physical change'], 0),
    ('Which of these is an example of a chemical change?', ['Burning a piece of paper', 'Melting an ice cube', 'Cutting a sheet of paper in half', 'Dissolving sugar in water'], 0),
    ('Why is the rusting of iron considered a chemical change rather than a physical change?', ['Iron reacts with oxygen to form a new substance, iron oxide, with different properties', 'Rusting never changes the chemical composition of iron', 'This concept has no connection to chemistry', 'Rust and iron are always exactly the same substance'], 0),
    ('Why is it useful for scientists to distinguish between physical and chemical changes when studying a reaction?', ['It helps identify whether a new substance has actually formed or whether the material has simply changed form', 'Distinguishing between the two types of change never provides any useful information', 'This concept has no relevance to science', 'Physical and chemical changes are always identical with no real difference'], 0)]),
SS('Social Studies: Economic Geography: Special Economic Zones (SEZs)',
   'Grade 9 Social Studies strand: a Special Economic Zone is a designated area within a country that offers reduced taxes and looser regulations to attract foreign investment and boost trade and manufacturing.',
   [('What is a Special Economic Zone?', ['A designated area offering reduced taxes and looser regulations to attract investment', 'A region with no economic activity at all', 'A concept unrelated to geography', 'An area where all trade is banned'], 0),
    ('Are Special Economic Zones often designed to attract foreign investment?', ['Yes', 'No, Special Economic Zones never attract any investment', 'A concept unrelated to economic geography', 'Foreign investment has no connection to Special Economic Zones'], 0),
    ('Do Special Economic Zones typically offer reduced taxes compared to the rest of the country?', ['Yes', 'No, taxes are always higher inside a Special Economic Zone', 'A concept unrelated to Special Economic Zones', 'Tax rates never differ between an SEZ and the rest of a country'], 0),
    ('Why might a country establish a Special Economic Zone near a major port?', ['Proximity to a port can make it easier and cheaper to import materials and export manufactured goods', 'Ports have no connection to how a Special Economic Zone functions', 'This concept has no connection to geography', 'Special Economic Zones are never located near ports or trade routes'], 0),
    ('Why might critics raise concerns about labour conditions in some Special Economic Zones?', ['Looser regulations designed to attract business could sometimes result in weaker protections for workers', 'Special Economic Zones always have the strongest labour protections in a country', 'This concept has no relevance to social studies', 'Labour conditions are never affected by regulatory differences in an SEZ'], 0)]),
]),

day(92, [
L('Writing: The Definition Essay',
  'Grade 9 Language strand: a definition essay explores the meaning of a complex or abstract term in depth, often using examples, comparisons, and context to clarify what the term truly means.',
  [('What does a definition essay explore in depth?', ['The meaning of a complex or abstract term', 'A step-by-step recipe', 'A concept unrelated to writing', 'A weather forecast'], 0),
   ('Might a definition essay use examples and comparisons to clarify a term’s meaning?', ['Yes', 'No, definition essays never use examples', 'A concept unrelated to definition essays', 'Examples are never useful for defining a term'], 0),
   ('Which of these terms would be a strong subject for a definition essay?', ['Courage', 'The number 7', 'A grocery list', 'A recipe for soup'], 0),
   ('Why might a writer use a personal anecdote when writing a definition essay about a term like resilience?', ['A real example can make an abstract concept more concrete and relatable for readers', 'Personal anecdotes never help explain an abstract term', 'This concept has no connection to writing', 'Definition essays should never include any examples or stories'], 0),
   ('Why can defining an abstract term like justice be more challenging than defining a concrete term like chair?', ['Abstract terms can carry different meanings and interpretations depending on context and perspective', 'Abstract terms always have exactly one universally agreed meaning', 'This concept has no connection to writing', 'Concrete and abstract terms are always equally easy to define'], 0)]),
M('Graphing Quadratic Functions in Vertex Form',
  'Grade 9 Math strand: a quadratic function written in vertex form, y = a(x-h)^2 + k, reveals the vertex of the parabola at the point (h,k), making it easy to graph transformations directly.',
  [('In vertex form, y = a(x-h)^2 + k, what point does (h,k) represent?', ['The vertex of the parabola', 'The y-intercept only', 'A concept unrelated to quadratics', 'The x-intercepts only'], 0),
   ('Does the value of a in vertex form affect whether a parabola opens upward or downward?', ['Yes', 'No, the value of a never affects the direction a parabola opens', 'A concept unrelated to vertex form', 'A parabola always opens upward no matter the value of a'], 0),
   ('What is the vertex of the parabola y = (x-3)^2 + 4?', ['(3, 4)', '(-3, 4)', '(3, -4)', '(4, 3)'], 0),
   ('If a is negative in vertex form, which direction does the parabola open?', ['Downward', 'Upward', 'A concept unrelated to vertex form', 'Sideways'], 0),
   ('Why is vertex form useful for quickly graphing a quadratic function compared to standard form?', ['It directly shows the vertex coordinates, making it easier to plot the parabola’s key point right away', 'Vertex form never makes graphing a parabola any easier', 'This concept has no connection to math', 'Standard form and vertex form always require exactly the same amount of work to graph'], 0)]),
Sc('Science: The Law of Conservation of Mass',
   'Grade 9 Science strand: the law of conservation of mass states that mass is neither created nor destroyed in a chemical reaction, so the total mass of reactants equals the total mass of products.',
   [('What does the law of conservation of mass state?', ['Mass is neither created nor destroyed in a chemical reaction', 'Mass always increases during a chemical reaction', 'A concept unrelated to chemistry', 'Mass always disappears completely during a reaction'], 0),
    ('Should the total mass of reactants equal the total mass of products in a chemical reaction?', ['Yes', 'No, the mass of products is always different from reactants', 'A concept unrelated to conservation of mass', 'Mass is never conserved in any chemical reaction'], 0),
    ('If 10 grams of reactants are used in a closed chemical reaction, what should the total mass of products equal?', ['10 grams', '5 grams', '20 grams', '0 grams'], 0),
    ('Why might a reaction that produces gas appear to lose mass if conducted in an open container?', ['The gas produced can escape into the air, so its mass is no longer measured within the container', 'Gas produced in a reaction never actually has any mass', 'This concept has no connection to conservation of mass', 'Mass is only conserved in reactions that happen in an open container'], 0),
    ('Why is the law of conservation of mass important when balancing chemical equations?', ['It ensures the same number of atoms of each element appears on both sides of the equation', 'Balancing equations has no connection to the conservation of mass', 'This concept has no relevance to science', 'Chemical equations never need to account for the mass of atoms involved'], 0)]),
SS('Social Studies: The Geography of Border Walls and Migration Control',
   'Grade 9 Social Studies strand: countries sometimes construct physical border walls or barriers to control the movement of people and goods, raising geographic questions about security, economics, and human rights.',
   [('What is one reason a country might construct a physical border wall?', ['To control the movement of people and goods across a border', 'To increase tourism in a neighbouring country', 'A concept unrelated to geography', 'To eliminate the need for any border at all'], 0),
    ('Do border walls raise questions about security, economics, and human rights?', ['Yes', 'No, border walls raise no questions of any kind', 'A concept unrelated to border geography', 'Human rights have no connection to border policy'], 0),
    ('Can the geography of a border, such as mountains or rivers, affect where a wall or barrier is built?', ['Yes', 'No, geography never affects where a border barrier is placed', 'A concept unrelated to border walls', 'Every border barrier is built in a perfectly flat, identical landscape'], 0),
    ('Why might building a border wall across a natural landscape, like a desert or forest, create environmental concerns?', ['It can disrupt wildlife migration routes and fragment natural ecosystems', 'Border walls never have any effect on the surrounding environment', 'This concept has no connection to geography', 'Wildlife is never affected by human-made structures at a border'], 0),
    ('Why do geographers study the economic impact of border walls on communities living near a boundary?', ['Restricted movement can affect trade, jobs, and daily life for people living in border communities', 'Border walls never have any economic effect on nearby communities', 'This concept has no relevance to social studies', 'Communities near a border are never affected by changes in border policy'], 0)]),
]),

day(93, [
L('Grammar: Gerunds, Infinitives, and Verbals',
  'Grade 9 Language strand: a verbal is a word formed from a verb that functions as another part of speech, including gerunds (verb + ing acting as a noun) and infinitives (to + verb acting as a noun, adjective, or adverb).',
  [('What is a verbal?', ['A word formed from a verb that functions as another part of speech', 'A word that can never be formed from a verb', 'A concept unrelated to grammar', 'A punctuation mark used at the end of a sentence'], 0),
   ('Does a gerund typically end in the letters -ing and function as a noun?', ['Yes', 'No, a gerund never ends in -ing', 'A concept unrelated to gerunds', 'A gerund always functions as a verb, never as a noun'], 0),
   ('In the sentence Swimming is my favourite hobby, which word is the gerund?', ['Swimming', 'Favourite', 'Hobby', 'Is'], 0),
   ('In the sentence She wants to travel next summer, which words form the infinitive?', ['To travel', 'She wants', 'Next summer', 'Wants to'], 0),
   ('Why is understanding verbals like gerunds and infinitives useful for writing varied, sophisticated sentences?', ['It allows a writer to use verb forms flexibly as nouns, adjectives, or adverbs for greater sentence variety', 'Verbals never add any variety to a sentence', 'This concept has no connection to grammar', 'Every sentence must use a verbal in exactly the same way'], 0)]),
M('Measures of Central Tendency: Mean, Median, and Mode',
  'Grade 9 Math strand: mean, median, and mode are three measures of central tendency used to describe the typical or central value of a data set, each useful in different situations.',
  [('What are mean, median, and mode examples of?', ['Measures of central tendency', 'Measures of angle size', 'A concept unrelated to statistics', 'Measures of area only'], 0),
   ('Is the mean of a data set calculated by adding all values and dividing by the number of values?', ['Yes', 'No, the mean is never calculated this way', 'A concept unrelated to the mean', 'The mean is always the largest value in a data set'], 0),
   ('What is the median of the data set 3, 7, 9, 12, 15?', ['9', '7', '12', '3'], 0),
   ('What is the mode of the data set 2, 4, 4, 6, 8?', ['4', '2', '6', '8'], 0),
   ('Why might the median be a more useful measure than the mean for a data set with an extreme outlier?', ['The median is not affected by extreme values the way the mean can be, giving a more typical picture of the data', 'The median is always affected more by outliers than the mean', 'This concept has no connection to statistics', 'Outliers never affect any measure of central tendency'], 0)]),
Sc('Science: Taxonomy and Classification of Living Things',
   'Grade 9 Science strand: taxonomy is the scientific system for classifying living things into a hierarchy of groups, from broad categories like kingdom down to specific species, based on shared characteristics.',
   [('What is taxonomy?', ['The scientific system for classifying living things into groups', 'A method for measuring the speed of chemical reactions', 'A concept unrelated to biology', 'A system for naming rock formations'], 0),
    ('Does taxonomy classify living things based on shared characteristics?', ['Yes', 'No, taxonomy classifies living things completely randomly', 'A concept unrelated to taxonomy', 'Shared characteristics have no connection to classification'], 0),
    ('Which of these is the broadest, most general level in the taxonomic hierarchy?', ['Kingdom', 'Species', 'Genus', 'Family'], 0),
    ('Why might two organisms be placed in the same genus but different species?', ['They may share many characteristics but still have enough differences to be considered distinct species', 'Organisms in the same genus are always identical with no differences at all', 'This concept has no connection to taxonomy', 'Genus and species always refer to exactly the same classification level'], 0),
    ('Why is a standardized taxonomic classification system useful for scientists around the world?', ['It allows scientists from different countries and languages to consistently identify and communicate about the same organism', 'A standardized classification system provides no benefit to scientific communication', 'This concept has no relevance to science', 'Every scientist uses a completely different, incompatible naming system'], 0)]),
SS('Social Studies: Urban Gentrification and Neighbourhood Change',
   'Grade 9 Social Studies strand: gentrification is a process in which rising property values and new investment in a lower-income urban neighbourhood attract wealthier residents, often displacing long-time residents.',
   [('What is gentrification?', ['A process where rising property values and investment attract wealthier residents to a lower-income neighbourhood', 'A process that always lowers property values in a neighbourhood', 'A concept unrelated to geography', 'A government policy that bans any new construction'], 0),
    ('Can gentrification sometimes lead to the displacement of long-time residents?', ['Yes', 'No, gentrification never displaces any residents', 'A concept unrelated to gentrification', 'Long-time residents are never affected by rising property values'], 0),
    ('Does gentrification typically involve new investment flowing into a neighbourhood?', ['Yes', 'No, gentrification always involves less investment', 'A concept unrelated to gentrification', 'Investment has no connection to gentrification'], 0),
    ('Why might long-time, lower-income residents struggle to remain in a gentrifying neighbourhood?', ['Rising rents and property taxes driven by new investment can make housing unaffordable for them', 'Gentrification always makes housing cheaper for existing residents', 'This concept has no connection to geography', 'Rent and property taxes never change as a neighbourhood gentrifies'], 0),
    ('Why is gentrification considered a complex geographic and social issue?', ['It can bring new investment and amenities while also raising concerns about fairness and displacement of existing communities', 'Gentrification has no positive or negative effects of any kind', 'This concept has no relevance to social studies', 'Every resident of a gentrifying neighbourhood is affected in exactly the same way'], 0)]),
]),

day(94, [
L('Vocabulary: Euphemism and Doublespeak',
  'Grade 9 Language strand: a euphemism is a mild or indirect word used in place of a harsher or blunter one, while doublespeak intentionally uses vague or misleading language to obscure an unpleasant truth.',
  [('What is a euphemism?', ['A mild or indirect word used in place of a harsher one', 'A word that always makes something sound more shocking', 'A concept unrelated to vocabulary', 'A type of punctuation mark'], 0),
   ('Does doublespeak intentionally use vague or misleading language?', ['Yes', 'No, doublespeak is always perfectly clear and direct', 'A concept unrelated to doublespeak', 'Doublespeak has no connection to language at all'], 0),
   ('Which of these phrases is an example of a euphemism for being fired from a job?', ['Let go', 'Promoted to manager', 'Given a raise', 'Hired full-time'], 0),
   ('Why might a company use doublespeak, like calling layoffs a rightsizing initiative, in an official announcement?', ['It can soften or obscure an unpleasant truth to make it sound less negative to the audience', 'Doublespeak never changes how an announcement is perceived', 'This concept has no connection to vocabulary', 'Rightsizing initiative is always a completely literal, transparent phrase'], 0),
   ('Why is it important for readers to recognize euphemism and doublespeak in media and political language?', ['Recognizing these techniques helps readers understand the true meaning behind carefully chosen words', 'Euphemism and doublespeak never affect how a message is understood', 'This concept has no relevance to vocabulary study', 'Every word in the English language carries exactly one meaning with no nuance'], 0)]),
M('Financial Literacy: Understanding Income Tax Basics',
  'Grade 9 Math strand: income tax is a percentage of a person’s earnings paid to the government, often calculated using a progressive system where higher portions of income are taxed at higher rates.',
  [('What is income tax?', ['A percentage of a person’s earnings paid to the government', 'A fee charged only when purchasing groceries', 'A concept unrelated to financial literacy', 'A one-time payment made only once in a lifetime'], 0),
   ('In a progressive tax system, do higher portions of income get taxed at higher rates?', ['Yes', 'No, every portion of income is always taxed at exactly the same rate', 'A concept unrelated to progressive taxation', 'Higher income is always taxed at a lower rate than lower income'], 0),
   ('If a person earns 40000 dollars and pays 15 percent in income tax, roughly how much tax do they owe?', ['6000 dollars', '4000 dollars', '15000 dollars', '400 dollars'], 0),
   ('Why might understanding your gross income versus your net (after-tax) income be important when creating a budget?', ['Net income reflects the actual amount available to spend after taxes are deducted', 'Gross and net income always refer to the exact same amount', 'This concept has no connection to financial literacy', 'Taxes never affect how much money a person actually receives'], 0),
   ('Why is understanding how income tax works useful for planning personal finances as a young adult?', ['It helps a person accurately estimate how much of their earnings they will actually take home to spend or save', 'Income tax never has any effect on how much money a person can spend', 'This concept has no connection to financial literacy', 'Every person pays the exact same fixed amount of tax regardless of income'], 0)]),
Sc('Science: Series and Parallel Circuits',
   'Grade 9 Science strand: in a series circuit, components are connected along a single path so current flows through each in turn, while in a parallel circuit, components are connected along multiple paths, each with the same voltage.',
   [('In a series circuit, are components connected along a single path?', ['Yes', 'No, series circuits always have multiple separate paths', 'A concept unrelated to circuits', 'A series circuit has no path for current at all'], 0),
    ('In a parallel circuit, do components each receive the same voltage?', ['Yes', 'No, voltage is never the same across components in a parallel circuit', 'A concept unrelated to parallel circuits', 'Parallel circuits never allow current to flow through more than one path'], 0),
    ('If one light bulb burns out in a series circuit, what typically happens to the other bulbs?', ['They also stop working, since the single path is broken', 'They continue working normally with no change at all', 'A concept unrelated to series circuits', 'They immediately become brighter'], 0),
    ('Why do most household electrical outlets use parallel circuits rather than series circuits?', ['Parallel circuits allow each device to operate independently, so one device turning off does not affect the others', 'Parallel circuits always cause every device in a home to stop working together', 'This concept has no connection to circuits', 'Series circuits are always used in household wiring instead of parallel circuits'], 0),
    ('Why is understanding the difference between series and parallel circuits important for designing electrical systems?', ['It helps engineers choose the right circuit type based on how components should function independently or together', 'The type of circuit used never has any effect on how a device functions', 'This concept has no relevance to science', 'Series and parallel circuits always behave in exactly the same way'], 0)]),
SS('Social Studies: The Geography of Critical Mineral Mining for Batteries and EVs',
   'Grade 9 Social Studies strand: critical minerals such as lithium and cobalt are essential for manufacturing batteries used in electric vehicles, and their mining is concentrated in specific regions of the world, raising geographic and economic questions.',
   [('Name one critical mineral used in manufacturing electric vehicle batteries.', ['Lithium', 'A concept unrelated to critical minerals', 'Oxygen', 'Table salt'], 0),
    ('Is the mining of critical minerals like lithium and cobalt concentrated in specific regions of the world?', ['Yes', 'No, critical minerals are mined evenly across every country in the world', 'A concept unrelated to critical mineral geography', 'Mining location has no connection to critical minerals'], 0),
    ('Are critical minerals essential for manufacturing batteries used in electric vehicles?', ['Yes', 'No, electric vehicle batteries require no critical minerals at all', 'A concept unrelated to critical minerals', 'Electric vehicles never use any type of battery'], 0),
    ('Why might a country with large deposits of critical minerals gain significant economic and geopolitical influence?', ['Global demand for battery technology creates strong reliance on countries that supply these essential minerals', 'Countries with critical mineral deposits never gain any economic advantage from them', 'This concept has no connection to geography', 'Critical minerals have no connection to global battery production'], 0),
    ('Why might the mining of critical minerals raise environmental and social concerns in some regions?', ['Mining operations can disrupt local ecosystems and communities near extraction sites', 'Mining critical minerals never has any environmental or social impact', 'This concept has no relevance to social studies', 'Extraction sites are always located far from any ecosystem or community'], 0)]),
]),

day(95, [
L('Reading: Analyzing Allusion in Literature',
  'Grade 9 Language strand: an allusion is a brief, indirect reference to a person, event, or work from history, mythology, or another text, adding layers of meaning for readers who recognize the connection.',
  [('What is an allusion?', ['A brief, indirect reference to a person, event, or work from history or another text', 'A detailed, direct explanation of a topic', 'A concept unrelated to reading', 'A type of punctuation mark'], 0),
   ('Can recognizing an allusion add layers of meaning to a reader’s understanding of a text?', ['Yes', 'No, recognizing an allusion never adds any meaning', 'A concept unrelated to allusion', 'Allusions never connect to anything outside the text itself'], 0),
   ('Which of these sentences contains an allusion to Greek mythology?', ['His pride was his Achilles’ heel.', 'She walked quickly to the store.', 'The weather was cold and rainy.', 'He ate breakfast before school.'], 0),
   ('Why might an author use an allusion to a well-known historical event instead of explaining the idea in full detail?', ['It can efficiently convey complex meaning by relying on a reader’s existing knowledge', 'Allusions always require lengthy additional explanation to be understood', 'This concept has no connection to literature', 'Allusions never help an author communicate an idea efficiently'], 0),
   ('Why might a reader unfamiliar with the Bible or Greek mythology miss the full meaning of certain allusions in classic literature?', ['Understanding an allusion depends on recognizing the reference it is drawing from', 'Allusions never depend on any outside knowledge to be understood', 'This concept has no relevance to reading comprehension', 'Every reader automatically understands every allusion regardless of their background knowledge'], 0)]),
M('Trigonometry: Angle of Elevation and Depression',
  'Grade 9 Math strand: the angle of elevation is the angle measured upward from a horizontal line to an object, while the angle of depression is measured downward, both used to solve real-world trigonometry problems.',
  [('What is the angle of elevation measured from?', ['A horizontal line upward to an object', 'A vertical line downward to an object', 'A concept unrelated to trigonometry', 'The ground directly below an object'], 0),
   ('Is the angle of depression measured downward from a horizontal line?', ['Yes', 'No, the angle of depression is always measured upward', 'A concept unrelated to angle of depression', 'The angle of depression has no connection to horizontal lines'], 0),
   ('If a person looks up at a bird flying above them, are they measuring an angle of elevation or depression?', ['Angle of elevation', 'Angle of depression', 'A concept unrelated to trigonometry', 'Neither type of angle'], 0),
   ('If a person standing on a cliff looks down at a boat in the water, are they measuring an angle of elevation or depression?', ['Angle of depression', 'Angle of elevation', 'A concept unrelated to trigonometry', 'Neither type of angle'], 0),
   ('Why are angle of elevation and depression problems useful for calculating the height of a tall object, like a building?', ['They allow trigonometric ratios to be used to find an unknown height or distance using a known angle and distance', 'These angles are never useful for calculating height or distance', 'This concept has no connection to math', 'Height can only ever be measured with a direct physical measurement, never trigonometry'], 0)]),
Sc('Science: Biodiversity and Ecosystem Stability',
   'Grade 9 Science strand: biodiversity refers to the variety of species within an ecosystem, and higher biodiversity generally makes an ecosystem more resilient and stable in the face of environmental change.',
   [('What does biodiversity refer to?', ['The variety of species within an ecosystem', 'The total number of rocks in an ecosystem', 'A concept unrelated to biology', 'The average temperature of an ecosystem'], 0),
    ('Does higher biodiversity generally make an ecosystem more resilient to environmental change?', ['Yes', 'No, biodiversity never affects an ecosystem’s resilience', 'A concept unrelated to biodiversity', 'Higher biodiversity always makes an ecosystem less stable'], 0),
    ('If a forest has many different species of plants, animals, and insects, is it considered to have high or low biodiversity?', ['High biodiversity', 'Low biodiversity', 'A concept unrelated to biodiversity', 'No biodiversity at all'], 0),
    ('Why might an ecosystem with low biodiversity be more vulnerable to collapse if one species disappears?', ['Fewer species means the ecosystem may rely heavily on a small number of species to maintain balance', 'Low biodiversity always makes an ecosystem more stable and resilient', 'This concept has no connection to biodiversity', 'The number of species in an ecosystem never affects its stability'], 0),
    ('Why do conservationists prioritize protecting areas with high biodiversity, such as rainforests?', ['These areas support a wide range of species and ecological functions that are difficult to replace once lost', 'High biodiversity areas provide no ecological benefit worth protecting', 'This concept has no relevance to science', 'Every ecosystem in the world has exactly the same level of biodiversity'], 0)]),
SS('Social Studies: The Geography of Data Centres and Cloud Computing Infrastructure',
   'Grade 9 Social Studies strand: data centres are large facilities that store and process the world’s digital information, and their physical location is influenced by factors like climate, energy availability, and internet connectivity.',
   [('What do data centres store and process?', ['The world’s digital information', 'Only physical paper documents', 'A concept unrelated to geography', 'Only handwritten letters'], 0),
    ('Can climate influence where a data centre is built?', ['Yes', 'No, climate has no connection to data centre location', 'A concept unrelated to data centre geography', 'Every data centre is built in exactly the same climate'], 0),
    ('Does energy availability play a role in choosing a location for a data centre?', ['Yes', 'No, data centres require no energy at all', 'A concept unrelated to data centres', 'Energy availability has no connection to geography'], 0),
    ('Why might a data centre be built in a region with a naturally cool climate?', ['Cooler temperatures can reduce the energy needed to keep servers from overheating', 'A cool climate has no effect on how much energy a data centre uses', 'This concept has no connection to geography', 'Data centres never generate any heat that needs to be managed'], 0),
    ('Why is reliable internet connectivity an important geographic factor when selecting a location for a data centre?', ['Data centres need fast, stable connections to transmit information efficiently to users around the world', 'Internet connectivity never affects how well a data centre can operate', 'This concept has no relevance to social studies', 'Data centres can function perfectly without any internet connection at all'], 0)]),
]),

day(96, [
L('Writing: Writing a Scene: Dialogue and Stage Directions',
  'Grade 9 Language strand: writing a scene for a play or script requires realistic dialogue and clear stage directions that tell actors how to move, speak, or express emotion.',
  [('What do stage directions tell actors?', ['How to move, speak, or express emotion', 'What the audience should eat during the show', 'A concept unrelated to writing', 'The exact ticket price for the performance'], 0),
   ('Does a well-written scene typically include both dialogue and stage directions?', ['Yes', 'No, scenes never include stage directions', 'A concept unrelated to script writing', 'Dialogue is never included in a script'], 0),
   ('Which of these is an example of a stage direction?', ['(She crosses the room and slams the door.)', 'I cannot believe you did that!', 'Once upon a time, in a small village.', 'The chemical formula for water is H2O.'], 0),
   ('Why is it important for dialogue in a scene to sound realistic and natural?', ['Realistic dialogue helps an audience believe in the characters and become engaged in the story', 'Dialogue never needs to sound realistic to be effective', 'This concept has no connection to writing', 'Audiences are never affected by how dialogue sounds in a scene'], 0),
   ('Why might a playwright use stage directions sparingly, allowing actors some room for interpretation?', ['It gives actors creative freedom to bring their own choices to a performance', 'Stage directions must always describe every single movement in exact detail', 'This concept has no connection to writing', 'Actors are never allowed to make any of their own creative choices'], 0)]),
M('Converting Between Forms of a Linear Equation',
  'Grade 9 Math strand: a linear equation can be written in slope-intercept form (y = mx + b), standard form (Ax + By = C), or point-slope form, and converting between these forms uses algebraic manipulation.',
  [('In slope-intercept form, y = mx + b, what does the value of b represent?', ['The y-intercept', 'The x-intercept', 'A concept unrelated to linear equations', 'The slope of the line'], 0),
   ('In slope-intercept form, does the value of m represent the slope of the line?', ['Yes', 'No, m never represents the slope', 'A concept unrelated to slope-intercept form', 'The slope is always represented by b, not m'], 0),
   ('What is the slope-intercept form of the equation 2x + y = 8?', ['y = -2x + 8', 'y = 2x + 8', 'y = -2x - 8', 'y = 2x - 8'], 0),
   ('What is the y-intercept of the line y = 3x - 5?', ['-5', '3', '5', '-3'], 0),
   ('Why might converting a linear equation from standard form to slope-intercept form be useful when graphing?', ['Slope-intercept form directly shows the slope and y-intercept, making it easier to plot the line', 'Converting between forms never makes graphing a line any easier', 'This concept has no connection to math', 'Standard form and slope-intercept form always require the exact same steps to graph'], 0)]),
Sc('Science: Earthquakes and Seismic Waves',
   'Grade 9 Science strand: an earthquake occurs when built-up stress along a fault line is suddenly released, generating seismic waves that travel through the Earth and are measured using instruments like seismographs.',
   [('What causes an earthquake?', ['Built-up stress along a fault line being suddenly released', 'A sudden increase in ocean temperature', 'A concept unrelated to earth science', 'The moon passing in front of the sun'], 0),
    ('Do seismic waves travel through the Earth during an earthquake?', ['Yes', 'No, seismic waves never travel through the Earth', 'A concept unrelated to earthquakes', 'Earthquakes never produce any type of wave'], 0),
    ('What instrument is used to measure seismic waves during an earthquake?', ['A seismograph', 'A concept unrelated to earthquakes', 'A thermometer', 'A barometer'], 0),
    ('Why do earthquakes often occur along fault lines near tectonic plate boundaries?', ['Stress builds up as tectonic plates push, pull, or slide against each other at these boundaries', 'Fault lines never experience any buildup of geological stress', 'This concept has no connection to earthquakes', 'Tectonic plate boundaries never generate any earthquakes'], 0),
    ('Why is studying seismic waves useful for scientists trying to understand the Earth’s interior structure?', ['The way seismic waves travel and change speed through different materials reveals information about the layers beneath the surface', 'Seismic waves never provide any information about the Earth’s interior', 'This concept has no relevance to science', 'The Earth’s interior structure has already been fully mapped with no further study needed'], 0)]),
SS('Social Studies: Urban Agriculture and Vertical Farming',
   'Grade 9 Social Studies strand: urban agriculture involves growing food within city environments, including vertical farms that stack crops in layers to maximize food production in limited urban space.',
   [('What does urban agriculture involve?', ['Growing food within city environments', 'Growing food only in remote rural areas', 'A concept unrelated to geography', 'Building shopping malls in cities'], 0),
    ('Do vertical farms stack crops in layers to maximize food production?', ['Yes', 'No, vertical farms never stack crops in layers', 'A concept unrelated to vertical farming', 'Vertical farms only ever grow crops underground'], 0),
    ('Is limited space a challenge that urban agriculture and vertical farming aim to address?', ['Yes', 'No, cities always have unlimited space for traditional farming', 'A concept unrelated to urban agriculture', 'Space availability has no connection to urban agriculture'], 0),
    ('Why might vertical farming be an appealing solution for growing food in a densely populated city?', ['It allows more food to be grown within a small physical footprint by using vertical space efficiently', 'Vertical farming always requires more land than traditional farming', 'This concept has no connection to geography', 'Cities never face any challenges related to growing or accessing food'], 0),
    ('Why might urban agriculture help reduce the distance food travels from farm to consumer?', ['Growing food directly within a city can shorten the transportation distance compared to importing from distant rural farms', 'Urban agriculture always increases the distance food must travel', 'This concept has no relevance to social studies', 'Food transportation distance never has any connection to where it is grown'], 0)]),
]),

day(97, [
L('Media Literacy: Analyzing Memes and Internet Culture',
  'Grade 9 Language strand: memes spread ideas, humour, or commentary through images, text, or videos that are rapidly shared and remixed online, making them a powerful and fast-evolving form of media communication.',
  [('What do memes typically spread through images, text, or video?', ['Ideas, humour, or commentary', 'Only official government announcements', 'A concept unrelated to media literacy', 'Only formal academic research'], 0),
   ('Are memes often rapidly shared and remixed online?', ['Yes', 'No, memes are never shared or remixed', 'A concept unrelated to memes', 'Memes only exist in printed newspapers'], 0),
   ('Which of these best describes a meme?', ['A humorous image with text that is widely shared and often remixed online', 'A lengthy academic research paper', 'A formal legal document', 'A weather forecast report'], 0),
   ('Why might a meme be an effective way to spread a political or social message quickly?', ['Its simple, humorous format can be easily understood and shared widely across social media', 'Memes are never used to communicate any kind of message', 'This concept has no connection to media literacy', 'Memes always take a long time to understand and share'], 0),
   ('Why is it important to think critically about the message or bias behind a meme before sharing it?', ['Memes can spread misinformation or oversimplify complex issues despite their casual, humorous tone', 'Memes never contain any bias or misleading information', 'This concept has no relevance to media literacy', 'Every meme is always completely accurate and unbiased'], 0)]),
M('Probability: Independent and Dependent Events',
  'Grade 9 Math strand: two events are independent if the outcome of one does not affect the other, while events are dependent if the outcome of one event changes the probability of the other.',
  [('What does it mean for two events to be independent?', ['The outcome of one event does not affect the other', 'The outcome of one event always determines the other', 'A concept unrelated to probability', 'Independent events can never both occur'], 0),
   ('Does the outcome of one dependent event change the probability of the other event occurring?', ['Yes', 'No, dependent events never affect each other’s probability', 'A concept unrelated to dependent events', 'Dependent events are always identical to independent events'], 0),
   ('Is flipping a coin twice in a row an example of independent or dependent events?', ['Independent events', 'Dependent events', 'A concept unrelated to probability', 'Neither type of event'], 0),
   ('Is drawing two cards from a deck without replacing the first card an example of independent or dependent events?', ['Dependent events', 'Independent events', 'A concept unrelated to probability', 'Neither type of event'], 0),
   ('Why is it important to determine whether events are independent or dependent before calculating their combined probability?', ['The correct method for calculating combined probability differs depending on whether events affect one another', 'Whether events are independent or dependent never affects how probability is calculated', 'This concept has no connection to math', 'Independent and dependent events are always calculated using the exact same method'], 0)]),
Sc('Science: Genetically Modified Organisms in Agriculture',
   'Grade 9 Science strand: a genetically modified organism (GMO) has had its DNA altered using biotechnology, often to increase crop yield, resist pests, or improve nutritional content in agriculture.',
   [('What is a genetically modified organism?', ['An organism that has had its DNA altered using biotechnology', 'An organism that has never had any change to its DNA', 'A concept unrelated to biology', 'An organism found only in the ocean'], 0),
    ('Are GMO crops sometimes modified to resist pests?', ['Yes', 'No, GMO crops are never modified to resist pests', 'A concept unrelated to genetically modified organisms', 'Pest resistance has no connection to genetic modification'], 0),
    ('Can genetic modification be used to improve the nutritional content of a crop?', ['Yes', 'No, genetic modification never affects nutritional content', 'A concept unrelated to GMOs', 'Nutritional content is never connected to a crop’s genetics'], 0),
    ('Why might a farmer choose to plant a genetically modified crop that is resistant to a specific pest?', ['It could reduce crop loss and the need for certain pesticides', 'GMO crops always require significantly more pesticide use', 'This concept has no connection to agriculture', 'Pest resistance has no effect on a farmer’s crop yield'], 0),
    ('Why do GMOs remain a topic of ongoing public debate and scientific research?', ['Questions about long-term environmental effects, food safety, and ethics continue to be studied and discussed', 'GMOs have no connection to any public debate or scientific research', 'This concept has no relevance to science', 'Every question about GMOs has already been completely and permanently resolved'], 0)]),
SS('Social Studies: The Geography of Air Pollution and Smog in Cities',
   'Grade 9 Social Studies strand: air pollution and smog often accumulate in cities due to vehicle emissions, industrial activity, and geographic factors like surrounding mountains that trap polluted air.',
   [('Name one source of air pollution in a city, such as vehicle emissions.', ['Vehicle emissions', 'A concept unrelated to air pollution', 'Fresh mountain air', 'Rainfall'], 0),
    ('Can geographic factors, such as surrounding mountains, contribute to trapping polluted air in a city?', ['Yes', 'No, geography never affects how air pollution accumulates', 'A concept unrelated to air pollution geography', 'Mountains always disperse polluted air instantly'], 0),
    ('Is industrial activity a common contributor to air pollution in urban areas?', ['Yes', 'No, industrial activity has no connection to air pollution', 'A concept unrelated to urban air pollution', 'Industrial activity always improves air quality'], 0),
    ('Why might a city located in a valley surrounded by mountains experience worse smog than a city on an open plain?', ['Surrounding mountains can trap polluted air, preventing it from dispersing as easily', 'Valleys always have better air quality than open plains', 'This concept has no connection to geography', 'Mountains never have any effect on how air pollution spreads or settles'], 0),
    ('Why is understanding the geographic causes of smog important for city planners trying to improve air quality?', ['It helps identify effective strategies, such as regulating traffic or industry, based on local geographic conditions', 'Geographic causes of smog never provide any useful information for city planning', 'This concept has no relevance to social studies', 'Every city experiences air pollution in exactly the same way regardless of geography'], 0)]),
]),

day(98, [
L('Grammar: Cohesion and Transitional Phrases',
  'Grade 9 Language strand: cohesion refers to how smoothly ideas connect within and between paragraphs, often achieved through transitional phrases like however, therefore, and in addition.',
  [('What does cohesion refer to in writing?', ['How smoothly ideas connect within and between paragraphs', 'The exact number of words in a sentence', 'A concept unrelated to grammar', 'The font size used in a document'], 0),
   ('Can transitional phrases like however and therefore help create cohesion in writing?', ['Yes', 'No, transitional phrases never help connect ideas', 'A concept unrelated to cohesion', 'Cohesion has no connection to transitional phrases'], 0),
   ('Which of these words could be used as a transitional phrase to show contrast between two ideas?', ['However', 'And', 'Also', 'Additionally'], 0),
   ('Why might a writer add the transitional phrase therefore before a conclusion in a paragraph?', ['It signals to the reader that a logical conclusion follows from the previous evidence or reasoning', 'Therefore never signals any kind of logical connection between ideas', 'This concept has no connection to grammar', 'Transitional phrases always confuse readers rather than helping them'], 0),
   ('Why is strong cohesion important for helping a reader follow an essay’s argument from paragraph to paragraph?', ['It creates a clear, logical flow that helps the reader understand how ideas relate to one another', 'Cohesion never affects how easily a reader can follow an argument', 'This concept has no relevance to writing', 'Paragraphs never need to connect logically to one another'], 0)]),
M('Interval Notation and Number Lines',
  'Grade 9 Math strand: interval notation is a concise way to represent a range of values on a number line, using brackets to show whether endpoints are included or excluded from the set.',
  [('What does interval notation represent?', ['A range of values on a number line', 'A single, exact numerical value', 'A concept unrelated to math', 'The angle measure of a triangle'], 0),
   ('In interval notation, does a square bracket indicate that an endpoint is included in the set?', ['Yes', 'No, a square bracket always indicates an endpoint is excluded', 'A concept unrelated to interval notation', 'Brackets have no connection to whether an endpoint is included'], 0),
   ('What does the interval notation (2, 5] represent?', ['All numbers greater than 2 and up to and including 5', 'All numbers less than 2 and greater than 5', 'Only the numbers 2 and 5', 'All numbers greater than or equal to 2 and less than 5'], 0),
   ('Which type of bracket is used in interval notation to show that an endpoint is excluded from the set?', ['A round parenthesis', 'A square bracket', 'A concept unrelated to interval notation', 'A curly brace'], 0),
   ('Why is interval notation useful for describing the solution to an inequality, such as x is greater than 3?', ['It provides a clear, standardized way to represent a continuous range of solutions', 'Interval notation never helps represent the solution to an inequality', 'This concept has no connection to math', 'Inequalities can never be represented using interval notation'], 0)]),
Sc('Science: Chemical Bonding: Metallic Bonds and Alloys',
   'Grade 9 Science strand: a metallic bond forms when metal atoms share a sea of freely moving electrons, giving metals properties like conductivity and malleability, and an alloy is a mixture of two or more metals with enhanced properties.',
   [('What forms a metallic bond?', ['Metal atoms sharing a sea of freely moving electrons', 'Two nonmetal atoms sharing a single electron pair', 'A concept unrelated to chemistry', 'A metal atom completely losing all of its electrons permanently'], 0),
    ('Do metallic bonds help explain why metals conduct electricity well?', ['Yes', 'No, metallic bonds have no connection to electrical conductivity', 'A concept unrelated to metallic bonding', 'Metals never conduct electricity under any circumstances'], 0),
    ('What is an alloy?', ['A mixture of two or more metals with enhanced properties', 'A single, pure metal element with no mixture at all', 'A concept unrelated to metallic bonding', 'A type of gas found in the atmosphere'], 0),
    ('Why might steel, an alloy of iron and carbon, be stronger than pure iron alone?', ['Adding carbon can disrupt the arrangement of metal atoms, making it harder for layers to slide past each other', 'Alloys are always weaker than the pure metals used to create them', 'This concept has no connection to chemistry', 'Steel and pure iron always have exactly the same physical properties'], 0),
    ('Why is the malleability of metals, allowing them to be shaped without breaking, explained by the structure of metallic bonding?', ['The freely moving electrons allow metal atoms to shift position relative to each other without breaking the overall bond', 'Malleability has no connection to how metallic bonds are structured', 'This concept has no relevance to science', 'Metals are never able to be shaped or bent under any circumstances'], 0)]),
SS('Social Studies: The Geography of International Aid and Development',
   'Grade 9 Social Studies strand: international aid involves the transfer of resources, funding, or expertise from wealthier countries or organizations to support development in lower-income regions, shaped by geographic need and access.',
   [('What does international aid involve transferring to support development?', ['Resources, funding, or expertise', 'Nothing at all connected to development', 'A concept unrelated to geography', 'Only military equipment'], 0),
    ('Is international aid often directed toward lower-income regions with significant development needs?', ['Yes', 'No, international aid is never directed toward any specific region', 'A concept unrelated to international aid', 'Development needs have no connection to where aid is sent'], 0),
    ('Can geographic factors, such as accessibility, affect how effectively aid reaches a region?', ['Yes', 'No, geography never affects how aid is delivered', 'A concept unrelated to international aid geography', 'Every region is equally accessible for delivering aid'], 0),
    ('Why might aid delivery be more challenging in a remote, mountainous region compared to a well-connected urban area?', ['Limited infrastructure and difficult terrain can make transporting resources and expertise more difficult', 'Remote regions are always easier to deliver aid to than urban areas', 'This concept has no connection to geography', 'Terrain and infrastructure never affect how aid is delivered'], 0),
    ('Why do geographers study the effectiveness of international aid programs in different regions?', ['Understanding what works in different geographic and social contexts helps improve future aid efforts', 'The effectiveness of aid programs never depends on geographic context', 'This concept has no relevance to social studies', 'Every aid program works in exactly the same way regardless of location'], 0)]),
]),

day(99, [
L('Reading: Analyzing Circular and Non-Linear Narrative Structure',
  'Grade 9 Language strand: a non-linear narrative presents events out of chronological order, and a circular narrative structure returns to its opening scene or idea by the end, shaping how readers interpret meaning.',
  [('What does a non-linear narrative present events out of?', ['Chronological order', 'Alphabetical order', 'A concept unrelated to reading', 'Numerical order only'], 0),
   ('Does a circular narrative structure return to its opening scene or idea by the end of the story?', ['Yes', 'No, circular narratives never return to their opening scene', 'A concept unrelated to circular narratives', 'Circular narratives always end in a completely random place with no connection to the start'], 0),
   ('Which of these describes a non-linear narrative structure?', ['A story that jumps between different points in time rather than moving straight from beginning to end', 'A story told in perfect chronological order from start to finish', 'A story with absolutely no plot of any kind', 'A recipe listing steps in order'], 0),
   ('Why might an author use a non-linear structure to tell a story about a character’s memory or trauma?', ['It can mimic how memories are often experienced out of order, adding psychological depth', 'A non-linear structure never adds any depth to how a story is understood', 'This concept has no connection to literature', 'Stories about memory must always be told in strict chronological order'], 0),
   ('Why might a circular narrative structure leave a reader with a different understanding of the opening scene once they reach the end?', ['New information revealed throughout the story can change how the reader interprets the earlier scene', 'A circular structure never changes how a reader understands the opening scene', 'This concept has no relevance to reading comprehension', 'The ending of a circular narrative never connects back to its beginning'], 0)]),
M('Solving Systems of Equations Graphically',
  'Grade 9 Math strand: a system of two linear equations can be solved graphically by plotting both lines and identifying the point where they intersect, which represents the solution that satisfies both equations.',
  [('When solving a system of equations graphically, what does the point of intersection represent?', ['The solution that satisfies both equations', 'The y-intercept of only one equation', 'A concept unrelated to systems of equations', 'A point that satisfies neither equation'], 0),
   ('If two lines in a system are parallel and never intersect, does the system have a solution?', ['No', 'Yes, parallel lines always have exactly one solution', 'A concept unrelated to systems of equations', 'Parallel lines always have infinitely many solutions'], 0),
   ('If two lines intersect at the point (3, 2), what is the solution to that system of equations?', ['x = 3, y = 2', 'x = 2, y = 3', 'x = 0, y = 0', 'A concept unrelated to systems of equations'], 0),
   ('If two equations in a system produce the exact same line when graphed, how many solutions does the system have?', ['Infinitely many solutions', 'Exactly one solution', 'No solution at all', 'A concept unrelated to systems of equations'], 0),
   ('Why might solving a system of equations graphically be a useful way to check an answer found using substitution or elimination?', ['Seeing the point of intersection visually can confirm whether the algebraic solution is accurate', 'Graphing a system never helps verify an algebraic solution', 'This concept has no connection to math', 'Graphical and algebraic methods always produce different answers for the same system'], 0)]),
Sc('Science: Fossil Fuels: Formation and Environmental Impact',
   'Grade 9 Science strand: fossil fuels such as coal, oil, and natural gas form over millions of years from the remains of ancient organisms, and burning them releases greenhouse gases that contribute to climate change.',
   [('What do fossil fuels form from?', ['The remains of ancient organisms', 'Freshly grown plants harvested this year', 'A concept unrelated to earth science', 'Pure water evaporated from the ocean'], 0),
    ('Does burning fossil fuels release greenhouse gases into the atmosphere?', ['Yes', 'No, burning fossil fuels never releases any gases', 'A concept unrelated to fossil fuels', 'Greenhouse gases have no connection to fossil fuel combustion'], 0),
    ('Name one example of a fossil fuel.', ['Coal', 'A concept unrelated to fossil fuels', 'Solar energy', 'Wind energy'], 0),
    ('Why does it take millions of years for fossil fuels to form?', ['They form from ancient organic material subjected to heat and pressure underground over an extremely long time', 'Fossil fuels can form within just a few days under any conditions', 'This concept has no connection to earth science', 'Fossil fuels are not related to any ancient organic material at all'], 0),
    ('Why are scientists concerned about the long-term environmental impact of continuing to burn fossil fuels?', ['The greenhouse gases released can trap heat in the atmosphere, contributing to long-term climate change', 'Burning fossil fuels has no connection to climate change of any kind', 'This concept has no relevance to science', 'Greenhouse gases released from fossil fuels have no effect on global temperatures'], 0)]),
SS('Social Studies: Cultural Diffusion and the Globalization of Cuisine',
   'Grade 9 Social Studies strand: cultural diffusion is the spread of cultural elements, such as food, from one region to another, and globalization has accelerated how cuisines from around the world blend and spread internationally.',
   [('What is cultural diffusion?', ['The spread of cultural elements, such as food, from one region to another', 'A process that only ever occurs within a single isolated village', 'A concept unrelated to geography', 'A method for measuring rainfall'], 0),
    ('Has globalization accelerated how cuisines from different regions blend and spread internationally?', ['Yes', 'No, globalization has no connection to how cuisine spreads', 'A concept unrelated to cultural diffusion', 'Cuisine never spreads between different regions or cultures'], 0),
    ('Which of these is an example of cultural diffusion through food?', ['A pizza restaurant from Italy becoming popular in many countries around the world', 'A single family cooking a meal only for themselves', 'A recipe that has never left its country of origin', 'A dish that no one has ever eaten outside of one household'], 0),
    ('Why might immigration contribute significantly to the cultural diffusion of cuisine in a city?', ['Immigrants often bring traditional recipes and cooking practices that can become part of the local food culture', 'Immigration never has any connection to how food culture develops in a city', 'This concept has no connection to geography', 'Cuisine never changes as a result of new people moving into a region'], 0),
    ('Why might some critics raise concerns about the loss of authenticity as a traditional cuisine becomes globalized?', ['Adapting a dish for new markets can sometimes change or simplify its original ingredients, methods, or meaning', 'Globalized cuisine is always identical to its original, traditional form with no changes at all', 'This concept has no relevance to social studies', 'Authenticity has no connection to how a cuisine spreads internationally'], 0)]),
]),

day(100, [
L('Review: Allegory, Grammar, Vocabulary, and Narrative Structure (Days 91-99)',
  'Grade 9 Language strand review: students revisit allegory, gerunds and infinitives, allusion, memes and internet culture, and non-linear narrative structure.',
  [('What is an allegory?', ['A narrative whose characters and events symbolically represent deeper meanings', 'A concept unrelated to reading', 'A type of poem with no symbolic meaning', 'A factual news report'], 0),
   ('What is a verbal?', ['A word formed from a verb that functions as another part of speech', 'A word that can never be formed from a verb', 'A concept unrelated to grammar', 'A punctuation mark used at the end of a sentence'], 0),
   ('What is an allusion?', ['A brief, indirect reference to a person, event, or work from history or another text', 'A detailed, direct explanation of a topic', 'A concept unrelated to reading', 'A type of punctuation mark'], 0),
   ('Are memes often rapidly shared and remixed online?', ['Yes', 'No, memes are never shared or remixed', 'A concept unrelated to memes', 'Memes only exist in printed newspapers'], 0),
   ('What does a non-linear narrative present events out of?', ['Chronological order', 'Alphabetical order', 'A concept unrelated to reading', 'Numerical order only'], 0)]),
M('Review: Exponents, Quadratics, Statistics, and Systems (Days 91-99)',
  'Grade 9 Math strand review: students revisit zero and negative exponents, vertex form of quadratics, mean/median/mode, independent and dependent events, and solving systems graphically.',
  [('What does any nonzero number raised to the exponent zero equal?', ['1', '0', 'The base itself', 'A concept unrelated to exponents'], 0),
   ('In vertex form, y = a(x-h)^2 + k, what point does (h,k) represent?', ['The vertex of the parabola', 'The y-intercept only', 'A concept unrelated to quadratics', 'The x-intercepts only'], 0),
   ('What are mean, median, and mode examples of?', ['Measures of central tendency', 'Measures of angle size', 'A concept unrelated to statistics', 'Measures of area only'], 0),
   ('What does it mean for two events to be independent?', ['The outcome of one event does not affect the other', 'The outcome of one event always determines the other', 'A concept unrelated to probability', 'Independent events can never both occur'], 0),
   ('When solving a system of equations graphically, what does the point of intersection represent?', ['The solution that satisfies both equations', 'The y-intercept of only one equation', 'A concept unrelated to systems of equations', 'A point that satisfies neither equation'], 0)]),
Sc('Review: Chemistry, Biology, Physics, and Earth Science (Days 91-99)',
   'Grade 9 Science strand review: students revisit physical vs chemical changes, taxonomy and classification, biodiversity and ecosystem stability, GMOs in agriculture, and fossil fuel formation and impact.',
   [('What happens to a substance’s chemical composition during a physical change?', ['It stays the same', 'It always changes completely', 'A concept unrelated to physical changes', 'It is destroyed entirely'], 0),
    ('What is taxonomy?', ['The scientific system for classifying living things into groups', 'A method for measuring the speed of chemical reactions', 'A concept unrelated to biology', 'A system for naming rock formations'], 0),
    ('What does biodiversity refer to?', ['The variety of species within an ecosystem', 'The total number of rocks in an ecosystem', 'A concept unrelated to biology', 'The average temperature of an ecosystem'], 0),
    ('What is a genetically modified organism?', ['An organism that has had its DNA altered using biotechnology', 'An organism that has never had any change to its DNA', 'A concept unrelated to biology', 'An organism found only in the ocean'], 0),
    ('What do fossil fuels form from?', ['The remains of ancient organisms', 'Freshly grown plants harvested this year', 'A concept unrelated to earth science', 'Pure water evaporated from the ocean'], 0)]),
SS('Review: Economic and Urban Geography (Days 91-99)',
   'Grade 9 Social Studies strand review: students revisit Special Economic Zones, urban gentrification, data centres and cloud computing, urban agriculture, and cultural diffusion of cuisine.',
   [('What is a Special Economic Zone?', ['A designated area offering reduced taxes and looser regulations to attract investment', 'A region with no economic activity at all', 'A concept unrelated to geography', 'An area where all trade is banned'], 0),
    ('What is gentrification?', ['A process where rising property values and investment attract wealthier residents to a lower-income neighbourhood', 'A process that always lowers property values in a neighbourhood', 'A concept unrelated to geography', 'A government policy that bans any new construction'], 0),
    ('What do data centres store and process?', ['The world’s digital information', 'Only physical paper documents', 'A concept unrelated to geography', 'Only handwritten letters'], 0),
    ('What does urban agriculture involve?', ['Growing food within city environments', 'Growing food only in remote rural areas', 'A concept unrelated to geography', 'Building shopping malls in cities'], 0),
    ('What is cultural diffusion?', ['The spread of cultural elements, such as food, from one region to another', 'A process that only ever occurs within a single isolated village', 'A concept unrelated to geography', 'A method for measuring rainfall'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_91_100)
    append_to(9, g9_91_100)
