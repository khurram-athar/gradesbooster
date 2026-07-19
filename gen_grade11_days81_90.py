#!/usr/bin/env python3
"""Grade 11, Days 81-90 -- extends Grade 11 from 80 to 90 days. Topics
chosen to avoid any overlap with the existing Day 1-80 set (see
data/grade11.json): the Kunstlerroman, eulogies and occasional speech,
deepfake and synthetic media analysis, the subjunctive mood, ecocriticism,
personal essays of place, Socratic seminars, free indirect discourse, and
the verse novel; logarithmic scales, recursive sequences and Fibonacci,
absolute value equations and inequalities, double/half-angle formulas,
the binomial distribution, slant asymptotes, modular arithmetic,
piecewise modelling, and vector projections/cross product; photoperiodism,
the skeletal system, symbiotic relationships, epigenetics, vaccines and
herd immunity, coral reef bleaching, the human microbiome, genetic
counselling, and biogeography; buffer capacity and Henderson-Hasselbalch,
industrial catalysis, radiometric dating, biodegradable plastics,
pyrotechnic chemistry, superconductivity, battery chemistry, forensic
trace evidence, and cosmetic chemistry.

Subject keys for Grade 11 are "English", "Functions", "Biology",
"Chemistry" (same as all earlier Grade 11 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E11 = 'https://tvolearn.com/pages/grade-11-english'
F11 = 'https://tvolearn.com/pages/grade-11-functions'
B11 = 'https://tvolearn.com/pages/grade-11-biology'
C11 = 'https://tvolearn.com/pages/grade-11-chemistry'
RE, RF, RB, RC = (
    'TVO Learn: Grade 11 English',
    'TVO Learn: Grade 11 Functions',
    'TVO Learn: Grade 11 Biology',
    'TVO Learn: Grade 11 Chemistry',
)


def E(t, s, q):
    return sub('English', t, s, RE, E11, q)


def F(t, s, q):
    return sub('Functions', t, s, RF, F11, q)


def B(t, s, q):
    return sub('Biology', t, s, RB, B11, q)


def C(t, s, q):
    return sub('Chemistry', t, s, RC, C11, q)


def _rebalance_answer_positions(days, seed=20260930):
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


g11_81_90 = [
day(81, [
E('Literature: The Kunstlerroman — The Artist’s Coming-of-Age Novel',
  'Grade 11 English strand: a Kunstlerroman is a novel that traces the development of an artist from childhood or youth into their mature creative identity.',
  [('What does a Kunstlerroman trace the development of?', ['An artist, from youth into their mature creative identity', 'A political leader’s rise to power', 'A concept unrelated to literature', 'A scientific discovery over several decades'], 0),
   ('Is a Kunstlerroman a specific type of coming-of-age novel?', ['Yes', 'No, it has no connection to coming-of-age narratives', 'A concept unrelated to the Kunstlerroman', 'It only ever describes a story with no central character'], 0),
   ('Why might a Kunstlerroman focus heavily on a protagonist’s internal creative struggles?', ['The novel’s core interest is how the character develops as an artist, which requires exploring their inner life', 'A Kunstlerroman never focuses on any internal struggle', 'This concept has no connection to literature', 'Artistic development is never relevant to this type of novel'], 0),
   ('Which of these would most likely appear in a Kunstlerroman?', ['A young painter gradually finding her unique artistic voice despite early self-doubt.', 'A detailed recipe for baking bread.', 'A weather report for the upcoming week.', 'A user manual for assembling furniture.'], 0),
   ('Why might readers interested in creativity and self-discovery be drawn to the Kunstlerroman genre?', ['It offers an intimate look at the challenges and growth involved in becoming an artist', 'This genre has no connection to themes of creativity or self-discovery', 'This concept has no relevance to literature', 'The Kunstlerroman genre focuses only on unrelated historical events'], 0)]),
F('Functions: Logarithmic Scales — pH, Richter, and Decibels',
  'Grade 11 Functions strand: logarithmic scales, such as pH, the Richter scale, and the decibel scale, compress a huge range of values into a more manageable set of numbers.',
  [('What do logarithmic scales like pH and the Richter scale help do?', ['Compress a huge range of values into a more manageable set of numbers', 'Expand small numbers into much larger ones with no practical use', 'A concept unrelated to functions', 'Convert numbers into fractions only'], 0),
   ('Is the Richter scale used to measure the magnitude of earthquakes?', ['Yes', 'No, the Richter scale has no connection to measuring earthquakes', 'A concept unrelated to logarithmic scales', 'The Richter scale only measures ocean tides'], 0),
   ('If an earthquake measures one full point higher on the Richter scale, is its intensity ten times greater?', ['Yes', 'No, the intensity remains exactly the same', 'A concept unrelated to logarithmic scales', 'The intensity would only double'], 0),
   ('Why is the decibel scale for sound considered logarithmic rather than linear?', ['A logarithmic scale can represent an enormous range of sound intensities using much smaller, more manageable numbers', 'The decibel scale is not actually related to logarithms in any way', 'This concept has no connection to functions', 'Sound intensity never varies enough to require any special type of scale'], 0),
   ('Why is a lower pH number associated with a more acidic solution?', ['The pH scale is logarithmic and inversely related to hydrogen ion concentration', 'A lower pH number always indicates a more basic, not acidic, solution', 'This concept has no connection to logarithmic functions', 'pH has no mathematical relationship to hydrogen ion concentration'], 0)]),
B('Biology: Photoperiodism and Plant Flowering Responses',
  'Grade 11 Biology strand: photoperiodism describes how plants respond to the relative length of day and night, often triggering processes like flowering at specific times of year.',
  [('What does photoperiodism describe in plants?', ['How plants respond to the relative length of day and night', 'How plants absorb water through their roots', 'A concept unrelated to biology', 'How plants convert sugar into starch'], 0),
   ('Can photoperiodism trigger flowering at specific times of year?', ['Yes', 'No, flowering is never connected to day length', 'A concept unrelated to photoperiodism', 'Flowering only depends on soil temperature, never light exposure'], 0),
   ('Why might a plant that flowers only in response to shorter days fail to bloom if kept under constant artificial light?', ['Continuous light would prevent the plant from experiencing the shorter day length needed to trigger flowering', 'Artificial light never has any effect on a plant’s flowering response', 'This concept has no connection to biology', 'All plants flower at the exact same time regardless of light conditions'], 0),
   ('Why is understanding photoperiodism useful for farmers growing crops on a commercial schedule?', ['It can help them control lighting conditions to influence when crops flower and produce yield', 'Photoperiodism has no practical application for commercial farming', 'This concept has no relevance to biology', 'Farmers never need to consider day length when growing crops'], 0),
   ('Why might plants native to different latitudes have evolved different photoperiodic responses?', ['Day length patterns vary significantly with latitude and season, favouring different flowering strategies', 'Photoperiodic responses never vary between plants from different regions', 'This concept has no relevance to biology', 'Latitude has no connection to day length or plant biology'], 0)]),
C('Chemistry: Buffer Capacity and the Henderson-Hasselbalch Equation',
  'Grade 11 Chemistry strand: buffer capacity describes how much acid or base a buffer solution can absorb before its pH changes significantly, calculated using the Henderson-Hasselbalch equation.',
  [('What does buffer capacity describe?', ['How much acid or base a buffer can absorb before its pH changes significantly', 'The exact colour of a buffer solution', 'A concept unrelated to chemistry', 'The temperature at which a buffer solution freezes'], 0),
   ('What equation is used to calculate the pH of a buffer solution?', ['The Henderson-Hasselbalch equation', 'A concept unrelated to buffer chemistry', 'The ideal gas law', 'Newton’s second law'], 0),
   ('Does a buffer solution resist significant changes in pH when small amounts of acid or base are added?', ['Yes', 'No, buffer solutions never resist any change in pH', 'A concept unrelated to buffer capacity', 'Buffer solutions only work with strong acids, never bases'], 0),
   ('Why might a buffer solution eventually fail to resist a pH change if too much acid is added?', ['Once the buffer’s capacity is exceeded, it can no longer neutralize the added acid effectively', 'Buffer solutions can resist an unlimited amount of added acid with no limit at all', 'This concept has no connection to chemistry', 'Buffer capacity has no connection to how much acid or base is added'], 0),
   ('Why are buffer solutions important in biological systems, such as human blood?', ['They help maintain a stable pH despite small chemical changes, which is essential for proper cell function', 'Buffer solutions have no role in maintaining stable conditions in biological systems', 'This concept has no relevance to chemistry', 'Human blood never requires any pH regulation at all'], 0)]),
]),

day(82, [
E('Writing: The Eulogy and Occasional Speech',
  'Grade 11 English strand: a eulogy or occasional speech is written to mark a significant event, often balancing personal reflection, respect for the audience, and a clear central message.',
  [('What is a eulogy typically written to mark?', ['A significant event, often honouring someone’s life', 'A routine weekly meeting', 'A concept unrelated to writing', 'A scientific experiment result'], 0),
   ('Should an occasional speech balance personal reflection with respect for the audience?', ['Yes', 'No, occasional speeches never need to consider the audience', 'A concept unrelated to occasional speeches', 'Personal reflection has no place in this type of speech'], 0),
   ('Why might a eulogy include specific, personal anecdotes about the person being honoured?', ['Specific details can make the tribute feel genuine and help the audience connect with the person’s memory', 'Eulogies should never include any personal anecdotes', 'This concept has no connection to writing', 'General statements are always more effective than specific details in a eulogy'], 0),
   ('Which of these would most likely appear in a eulogy?', ['She always found a way to make everyone in the room feel welcome.', 'The chemical formula for methane is CH4.', 'Add 12 and 8 to get 20.', 'The train departs at exactly noon.'], 0),
   ('Why is finding a clear central message important when writing an occasional speech?', ['A clear focus helps unify personal stories and reflections into a coherent, memorable speech', 'A central message never helps organize an occasional speech', 'This concept has no connection to writing', 'Occasional speeches are always more effective with no clear focus at all'], 0)]),
F('Discrete Math: Recursive Sequences and the Fibonacci Sequence',
  'Grade 11 Functions strand: the Fibonacci sequence is a recursive sequence where each term is the sum of the two preceding terms, beginning with 0 and 1.',
  [('How is each term of the Fibonacci sequence generated?', ['By adding the two preceding terms', 'By multiplying the term’s position by two', 'A concept unrelated to sequences', 'By subtracting one from the previous term'], 0),
   ('What are the first two terms of the Fibonacci sequence?', ['0 and 1', '1 and 2', 'A concept unrelated to the Fibonacci sequence', '2 and 3'], 0),
   ('What is the sixth term of the Fibonacci sequence, given it begins 0, 1, 1, 2, 3?', ['5', '3', '2', '8'], 0),
   ('Why is the Fibonacci sequence considered a recursive sequence rather than an explicit one?', ['Each term depends directly on the values of previous terms rather than being calculated straight from its position', 'The Fibonacci sequence never depends on any previous terms', 'This concept has no connection to sequences', 'Recursive and explicit sequences are always identical in how they are defined'], 0),
   ('Why might the Fibonacci sequence be of interest to biologists studying patterns in nature, like spiral shells?', ['Certain natural growth patterns closely resemble the proportions found within the Fibonacci sequence', 'The Fibonacci sequence has no connection to any patterns observed in nature', 'This concept has no relevance to functions', 'Natural growth patterns are always completely random with no mathematical structure'], 0)]),
B('Biology: The Skeletal System — Bone Structure and Remodelling',
  'Grade 11 Biology strand: bones are living tissue that continuously undergo remodelling, a process where old bone is broken down and new bone is formed to maintain strength and repair damage.',
  [('What process do bones continuously undergo to maintain strength?', ['Remodelling', 'Complete replacement every single day', 'A concept unrelated to biology', 'A process that never actually occurs in bones'], 0),
   ('Is bone considered living tissue?', ['Yes', 'No, bone is entirely non-living material', 'A concept unrelated to the skeletal system', 'Bone tissue has no biological activity at all'], 0),
   ('Does bone remodelling involve breaking down old bone and forming new bone?', ['Yes', 'No, remodelling never involves breaking down any existing bone', 'A concept unrelated to bone remodelling', 'New bone is never formed during this process'], 0),
   ('Why might weight-bearing exercise help strengthen bones over time?', ['Mechanical stress can stimulate the bone remodelling process, encouraging the formation of stronger bone tissue', 'Exercise has no effect on bone remodelling or strength', 'This concept has no connection to biology', 'Bones never respond to mechanical stress in any way'], 0),
   ('Why is bone remodelling important for repairing a fracture?', ['It allows damaged bone tissue to be broken down and replaced with new, healthy bone over time', 'Bone remodelling has no role in healing a fracture', 'This concept has no relevance to biology', 'Fractures heal without any involvement of bone tissue remodelling'], 0)]),
C('Chemistry: Industrial Catalysis',
  'Grade 11 Chemistry strand: industrial catalysis uses catalysts to speed up large-scale chemical processes, reducing energy costs and increasing efficiency in manufacturing.',
  [('What does industrial catalysis use to speed up large-scale chemical processes?', ['Catalysts', 'Only extremely high pressure with no chemical additives', 'A concept unrelated to chemistry', 'Nothing at all beyond raw materials'], 0),
   ('Can using a catalyst in an industrial process reduce energy costs?', ['Yes', 'No, catalysts never have any effect on energy costs', 'A concept unrelated to industrial catalysis', 'Catalysts always increase the energy required for a reaction'], 0),
   ('Is a catalyst consumed during an industrial chemical reaction?', ['No', 'Yes, catalysts are always fully consumed in industrial reactions', 'A concept unrelated to industrial catalysis', 'Catalysts are never actually involved in industrial processes'], 0),
   ('Why might a chemical company invest in developing a more effective catalyst for a manufacturing process?', ['A better catalyst could increase reaction speed and efficiency, potentially lowering overall production costs', 'Catalysts never have any effect on the cost or speed of manufacturing', 'This concept has no connection to chemistry', 'Manufacturing processes never rely on any catalytic reactions'], 0),
   ('Why is catalysis considered important for reducing the environmental impact of some industrial processes?', ['More efficient reactions can require less energy and produce less waste overall', 'Catalysis has no connection to the environmental impact of industrial chemistry', 'This concept has no relevance to chemistry', 'Industrial processes always produce the same amount of waste regardless of catalyst use'], 0)]),
]),

day(83, [
E('Media Literacy: Analyzing Deepfake Technology and Synthetic Media',
  'Grade 11 English strand: deepfake technology uses artificial intelligence to create highly realistic but fabricated images, audio, or video, raising serious concerns about trust and misinformation.',
  [('What does deepfake technology use to create fabricated media?', ['Artificial intelligence', 'Only traditional hand-drawn animation', 'A concept unrelated to media literacy', 'A simple photo filter with no advanced technology'], 0),
   ('Can deepfake technology create highly realistic but fabricated video content?', ['Yes', 'No, deepfake content is always obviously fake and unconvincing', 'A concept unrelated to deepfakes', 'Deepfakes only ever apply to still images, never video'], 0),
   ('Does deepfake technology raise concerns about trust and misinformation?', ['Yes', 'No, deepfakes have no connection to misinformation concerns', 'A concept unrelated to deepfake technology', 'Trust in media is never affected by synthetic content'], 0),
   ('Why might a realistic deepfake video be particularly dangerous if shared without context on social media?', ['Viewers might believe a fabricated event actually occurred, spreading false information quickly', 'Deepfake videos never have the potential to mislead viewers', 'This concept has no connection to media literacy', 'Fabricated videos are always immediately recognized as fake by every viewer'], 0),
   ('Why is developing critical media literacy skills increasingly important as synthetic media technology improves?', ['As fabricated content becomes harder to detect, viewers need stronger tools to evaluate what they see and hear', 'Media literacy skills have no connection to identifying synthetic or fabricated content', 'This concept has no relevance to media literacy', 'Improved technology has made synthetic media easier to detect than ever before'], 0)]),
F('Functions: Solving Absolute Value Equations and Inequalities',
  'Grade 11 Functions strand: solving an absolute value equation or inequality requires considering both the positive and negative cases of the expression inside the absolute value bars.',
  [('When solving an absolute value equation, how many cases must typically be considered?', ['Two, the positive and negative cases', 'Only one single case', 'A concept unrelated to absolute value', 'Four separate cases'], 0),
   ('If the absolute value of x minus 3 equals 5, what are the two possible values of x?', ['8 and -2', '5 and -5', '3 and -3', '2 and 8'], 0),
   ('When solving an absolute value inequality like the absolute value of x is less than 4, what is the resulting range?', ['-4 is less than x, and x is less than 4', 'x is greater than 4 only', 'A concept unrelated to absolute value inequalities', 'x is less than -4 only'], 0),
   ('Why does solving an absolute value equation typically produce two possible solutions instead of one?', ['The expression inside the absolute value bars could be either positive or negative and still yield the same absolute value', 'Absolute value equations always produce exactly one single solution', 'This concept has no connection to functions', 'Absolute value has no mathematical relationship to positive and negative numbers'], 0),
   ('Why might it be important to check both solutions when solving an absolute value equation?', ['One of the two possible solutions could turn out to be extraneous and not satisfy the original equation', 'Checking solutions is never necessary when solving absolute value equations', 'This concept has no connection to functions', 'Both solutions are always automatically valid with no need for verification'], 0)]),
B('Biology: Symbiotic Relationships — Mutualism, Commensalism, Parasitism',
  'Grade 11 Biology strand: symbiotic relationships describe close, long-term interactions between different species, classified as mutualism, commensalism, or parasitism depending on how each species is affected.',
  [('What do symbiotic relationships describe?', ['Close, long-term interactions between different species', 'Only interactions between members of the exact same species', 'A concept unrelated to biology', 'Random, one-time encounters between organisms'], 0),
   ('In mutualism, do both species involved benefit from the relationship?', ['Yes', 'No, only one species ever benefits in mutualism', 'A concept unrelated to symbiotic relationships', 'Neither species benefits in a mutualistic relationship'], 0),
   ('In parasitism, does one species benefit while harming the other?', ['Yes', 'No, parasitism never involves any harm to either species', 'A concept unrelated to symbiotic relationships', 'Both species always benefit equally in parasitism'], 0),
   ('Why might bees and flowering plants be considered an example of mutualism?', ['Bees gain nectar for food while plants benefit from pollination, helping both species survive and reproduce', 'Bees and flowering plants never interact in any beneficial way', 'This concept has no connection to biology', 'Only the plant benefits in this relationship, with no advantage to the bee'], 0),
   ('Why is commensalism sometimes considered more difficult to identify in nature than mutualism or parasitism?', ['One species benefits while the other is neither helped nor harmed, which can be subtle to observe and confirm', 'Commensalism always produces dramatic, easily observable effects on both species involved', 'This concept has no relevance to biology', 'Commensalism has no connection to how species interact with one another'], 0)]),
C('Chemistry: Radiometric Dating and Isotopes',
  'Grade 11 Chemistry strand: radiometric dating uses the known decay rate of radioactive isotopes to estimate the age of rocks, fossils, and other materials.',
  [('What does radiometric dating use to estimate the age of a material?', ['The known decay rate of radioactive isotopes', 'The colour of the material’s surface', 'A concept unrelated to chemistry', 'The material’s exact weight in kilograms'], 0),
   ('Do radioactive isotopes decay at a predictable, known rate?', ['Yes', 'No, radioactive decay happens at a completely random, unpredictable rate', 'A concept unrelated to radiometric dating', 'Decay rates change dramatically based on outside temperature'], 0),
   ('Can radiometric dating be used to estimate the age of a fossil?', ['Yes', 'No, radiometric dating only applies to living organisms', 'A concept unrelated to radiometric dating', 'Fossils cannot be dated using any scientific method'], 0),
   ('Why is the half-life of an isotope an important concept in radiometric dating?', ['Half-life describes the time it takes for half of a sample to decay, allowing scientists to calculate elapsed time', 'Half-life has no connection to how radiometric dating calculations are performed', 'This concept has no connection to chemistry', 'Half-life only applies to isotopes that never actually decay'], 0),
   ('Why might scientists choose a specific isotope with a particular half-life to date a very old rock formation?', ['An isotope with a longer half-life remains measurable over much greater spans of time, suiting very old samples', 'The choice of isotope never matters when dating a rock formation', 'This concept has no relevance to chemistry', 'Only isotopes with extremely short half-lives can ever be used for dating rocks'], 0)]),
]),

day(84, [
E('Grammar: The Subjunctive Mood',
  'Grade 11 English strand: the subjunctive mood expresses wishes, hypothetical situations, or demands, often appearing in clauses beginning with if or that.',
  [('What does the subjunctive mood express?', ['Wishes, hypothetical situations, or demands', 'Only simple statements of fact', 'A concept unrelated to grammar', 'Questions about the future only'], 0),
   ('Which sentence correctly uses the subjunctive mood?', ['If I were rich, I would travel the world.', 'If I was rich, I would travel the world.', 'If I am rich, I would travel the world.', 'If I will be rich, I would travel the world.'], 0),
   ('Does the subjunctive mood often appear in clauses beginning with if or that?', ['Yes', 'No, the subjunctive mood never appears in these types of clauses', 'A concept unrelated to grammar', 'The subjunctive mood only ever appears in questions'], 0),
   ('Why might a writer use the subjunctive mood in the sentence I suggest that she be on time?', ['The subjunctive expresses a recommendation or demand rather than a simple statement of fact', 'The subjunctive mood never expresses any kind of recommendation or demand', 'This concept has no connection to grammar', 'This sentence would be identical in meaning without the subjunctive mood'], 0),
   ('Why is understanding the subjunctive mood useful for expressing hypothetical or contrary-to-fact situations clearly?', ['It signals to the reader that a statement describes something imagined or not currently true', 'The subjunctive mood never helps clarify whether a statement is hypothetical', 'This concept has no connection to grammar', 'Hypothetical situations are always expressed using the exact same verb forms as factual statements'], 0)]),
F('Trigonometry: Double-Angle and Half-Angle Formulas',
  'Grade 11 Functions strand: double-angle and half-angle formulas allow trigonometric functions of an angle to be rewritten in terms of functions of double or half that angle.',
  [('What do double-angle formulas allow trigonometric functions to be rewritten in terms of?', ['Functions of double the original angle', 'Only the original angle itself with no transformation', 'A concept unrelated to trigonometry', 'Functions of an entirely unrelated angle'], 0),
   ('What is the double-angle formula for sine, in terms of sine and cosine of the original angle?', ['2 times sine of the angle times cosine of the angle', 'Sine of the angle plus cosine of the angle', 'A concept unrelated to trigonometric identities', 'Sine of the angle divided by cosine of the angle'], 0),
   ('Do half-angle formulas allow trigonometric functions to be expressed in terms of half of a given angle?', ['Yes', 'No, half-angle formulas never involve half of any angle', 'A concept unrelated to half-angle formulas', 'Half-angle formulas only apply to angles greater than 180 degrees'], 0),
   ('Why might double-angle formulas be useful for simplifying an expression involving sine of two times an unknown angle?', ['They allow the expression to be rewritten using only functions of the original single angle, which can simplify solving', 'Double-angle formulas never simplify any trigonometric expression', 'This concept has no connection to trigonometry', 'Double-angle formulas only apply to angles measured in degrees, never radians'], 0),
   ('Why are double-angle and half-angle formulas considered useful tools when solving certain trigonometric equations?', ['They allow equations with double or half angles to be rewritten in terms of a single common angle, simplifying the solving process', 'These formulas never assist in solving any trigonometric equation', 'This concept has no relevance to trigonometry', 'Every trigonometric equation can only ever be solved using a graphing calculator'], 0)]),
B('Biology: Epigenetics — Gene Expression Beyond DNA Sequence',
  'Grade 11 Biology strand: epigenetics studies how environmental factors can influence whether specific genes are turned on or off, without altering the underlying DNA sequence itself.',
  [('What does epigenetics study?', ['How environmental factors influence whether genes are turned on or off', 'How DNA sequences are physically rewritten', 'A concept unrelated to biology', 'How cells divide during mitosis'], 0),
   ('Does epigenetics involve changing the underlying DNA sequence?', ['No', 'Yes, it always changes the DNA sequence', 'A concept unrelated to epigenetics', 'DNA sequence has no connection to epigenetics'], 0),
   ('Name one environmental factor that could influence gene expression, such as diet.', ['Diet', 'A concept unrelated to epigenetics', 'A favourite hobby', 'A random guess with no scientific basis'], 0),
   ('Why might identical twins, who share the same DNA, develop some different traits over their lives?', ['Different environmental experiences could lead to different epigenetic changes affecting gene expression', 'Identical twins can never develop any different traits', 'This concept has no connection to epigenetics', 'DNA sequence alone always determines every trait with no other influence'], 0),
   ('Why is epigenetics considered a valuable area of modern biological research?', ['It helps explain how environment and genetics interact to influence health and traits', 'Epigenetics has no connection to health or biology', 'This concept has no relevance to science', 'Genes are the only factor that ever influences an organism’s traits'], 0)]),
C('Chemistry: Biodegradable Plastics and Green Materials',
  'Grade 11 Chemistry strand: biodegradable plastics are designed to break down more readily in the environment than traditional plastics, often made from renewable, plant-based sources.',
  [('What are biodegradable plastics designed to do?', ['Break down more readily in the environment than traditional plastics', 'Last forever without ever breaking down', 'A concept unrelated to chemistry', 'Dissolve instantly the moment they are made'], 0),
   ('Are biodegradable plastics often made from renewable, plant-based sources?', ['Yes', 'No, biodegradable plastics are always made from petroleum only', 'A concept unrelated to biodegradable plastics', 'Plant-based sources have no connection to biodegradable plastics'], 0),
   ('Do biodegradable plastics generally break down faster than traditional plastics?', ['Yes', 'No, biodegradable plastics never break down at all', 'A concept unrelated to green materials', 'Traditional plastics always break down faster than biodegradable ones'], 0),
   ('Why might a biodegradable plastic still require specific environmental conditions, like industrial composting, to break down effectively?', ['Certain biodegradable materials need particular temperature, moisture, or microbial conditions to decompose efficiently', 'Biodegradable plastics always break down instantly regardless of environmental conditions', 'This concept has no connection to chemistry', 'Environmental conditions never have any effect on how quickly a material decomposes'], 0),
   ('Why is developing biodegradable plastics considered an important goal for reducing environmental plastic waste?', ['Materials that break down more readily could reduce the long-term accumulation of plastic waste in landfills and oceans', 'Biodegradable plastics have no connection to reducing environmental waste', 'This concept has no relevance to chemistry', 'Plastic waste accumulation is entirely unrelated to the type of plastic used'], 0)]),
]),

day(85, [
E('Literature: Ecocriticism — Reading Nature and the Environment in Text',
  'Grade 11 English strand: ecocriticism examines how literature represents nature and the environment, exploring the relationship between human culture and the natural world.',
  [('What does ecocriticism examine in literature?', ['How literature represents nature and the environment', 'Only the grammar and punctuation used in a text', 'A concept unrelated to literary study', 'The exact publication date of a text'], 0),
   ('Does ecocriticism explore the relationship between human culture and the natural world?', ['Yes', 'No, ecocriticism never considers any relationship between culture and nature', 'A concept unrelated to ecocriticism', 'Human culture and the natural world are never connected in this approach'], 0),
   ('Why might an ecocritical reading of a novel focus on how a character interacts with a natural landscape?', ['These interactions can reveal deeper attitudes toward nature, and how humans understand their place within it', 'A character’s interaction with landscape is never significant in an ecocritical reading', 'This concept has no connection to literature', 'Ecocriticism only ever focuses on characters, never on setting or landscape'], 0),
   ('Which of these questions would an ecocritic likely ask about a text?', ['How does this novel portray humanity’s relationship with the natural environment?', 'What font was used in the original printed edition?', 'How many chapters does this novel contain?', 'What year was the author born?'], 0),
   ('Why might ecocriticism be considered an increasingly relevant approach to studying literature today?', ['Growing awareness of environmental issues has made how literature represents nature more significant to modern readers', 'Ecocriticism has no connection to any contemporary concerns or issues', 'This concept has no relevance to literature', 'Environmental themes have never appeared in any literary work'], 0)]),
F('Statistics: The Binomial Probability Distribution',
  'Grade 11 Functions strand: the binomial probability distribution models the number of successes in a fixed number of independent trials, each with the same probability of success.',
  [('What does the binomial probability distribution model?', ['The number of successes in a fixed number of independent trials', 'The average outcome of a single unrepeated event', 'A concept unrelated to statistics', 'The exact outcome of every possible experiment'], 0),
   ('In a binomial distribution, must each trial have the same probability of success?', ['Yes', 'No, each trial can have a completely different probability of success', 'A concept unrelated to binomial distributions', 'Probability of success is never a factor in this distribution'], 0),
   ('If a fair coin is flipped 10 times, could the number of heads be modelled using a binomial distribution?', ['Yes', 'No, coin flips can never be modelled using a binomial distribution', 'A concept unrelated to binomial distributions', 'Binomial distributions only apply to dice rolls, never coin flips'], 0),
   ('Why must the trials in a binomial distribution be independent of one another?', ['If one trial’s outcome affected another’s probability, the binomial model would no longer accurately apply', 'Independence between trials is never a requirement for a binomial distribution', 'This concept has no connection to statistics', 'Binomial distributions work identically whether or not trials are independent'], 0),
   ('Why might a quality control inspector use a binomial distribution to model the number of defective items in a batch?', ['Each item can be checked independently, and each check has the same probability of being defective', 'A binomial distribution has no application in quality control or inspection', 'This concept has no relevance to statistics', 'Defective items can never be modelled using any probability distribution'], 0)]),
B('Biology: Vaccine Development and Herd Immunity',
  'Grade 11 Biology strand: vaccines train the immune system to recognize specific pathogens, and widespread vaccination within a population can produce herd immunity that slows disease spread.',
  [('What do vaccines train the immune system to recognize?', ['Specific pathogens', 'Only harmless substances with no medical purpose', 'A concept unrelated to vaccines', 'Nothing at all related to disease'], 0),
   ('What term describes the protection a population gains when enough individuals are immune to a disease?', ['Herd immunity', 'A concept unrelated to vaccines', 'Individual immunity only', 'Passive immunity exclusively'], 0),
   ('Can widespread vaccination help slow the spread of a disease through a population?', ['Yes', 'No, vaccination has no connection to how a disease spreads through a population', 'A concept unrelated to herd immunity', 'Disease spread is never affected by how many people are vaccinated'], 0),
   ('Why might herd immunity help protect individuals who cannot receive a vaccine themselves, such as those with certain medical conditions?', ['If enough of the surrounding population is immune, a disease has fewer opportunities to spread to vulnerable individuals', 'Herd immunity never provides any protection to unvaccinated individuals', 'This concept has no connection to biology', 'Vaccinated individuals provide no benefit to anyone besides themselves'], 0),
   ('Why is the percentage of a population that needs to be vaccinated to achieve herd immunity different for different diseases?', ['More contagious diseases generally require a higher percentage of immune individuals to effectively stop transmission', 'The vaccination threshold for herd immunity is always exactly the same for every disease', 'This concept has no relevance to biology', 'Herd immunity has no connection to how contagious a particular disease is'], 0)]),
C('Chemistry: The Chemistry of Fireworks and Pyrotechnics',
  'Grade 11 Chemistry strand: fireworks rely on metal salts to produce specific colours when heated, along with oxidizers and fuels that drive the combustion reactions that create their bursts.',
  [('What do fireworks use to produce specific colours when heated?', ['Metal salts', 'Only plain water', 'A concept unrelated to chemistry', 'Ordinary table sugar'], 0),
   ('Do fireworks rely on oxidizers and fuels to drive their combustion reactions?', ['Yes', 'No, fireworks require no combustion reaction at all', 'A concept unrelated to pyrotechnic chemistry', 'Combustion has no connection to how fireworks work'], 0),
   ('Can different metal salts produce different colours in a firework display?', ['Yes', 'No, every metal salt produces exactly the same colour', 'A concept unrelated to fireworks chemistry', 'Colour has no connection to the chemical composition of a firework'], 0),
   ('Why might a firework containing copper salts appear blue-green when it explodes?', ['Copper salts emit light at wavelengths associated with blue-green colours when heated to high temperatures', 'Copper salts never produce any visible colour when heated', 'This concept has no connection to chemistry', 'Firework colour is determined only by the shape of the firework shell, not its chemical contents'], 0),
   ('Why do chemists carefully control the ratio of fuel to oxidizer when designing a firework?', ['The correct ratio ensures a controlled, safe combustion reaction that produces the desired visual effect', 'The ratio of fuel to oxidizer has no effect on how a firework performs', 'This concept has no relevance to chemistry', 'Fireworks never actually involve any chemical reaction between fuel and oxidizer'], 0)]),
]),

day(86, [
E('Writing: The Personal Essay of Place',
  'Grade 11 English strand: a personal essay of place explores how a specific location has shaped the writer’s identity, memories, or understanding of the world.',
  [('What does a personal essay of place explore?', ['How a specific location has shaped the writer’s identity or memories', 'Only unrelated statistics about a city’s population', 'A concept unrelated to writing', 'A step-by-step travel itinerary with no reflection'], 0),
   ('Might a personal essay of place include vivid sensory details about a specific location?', ['Yes', 'No, sensory details are never included in this type of essay', 'A concept unrelated to personal essays', 'This type of essay never focuses on any specific location'], 0),
   ('Why might a writer choose to focus an essay on their childhood home rather than a location they have never visited?', ['A personally meaningful location allows for richer reflection and emotional connection', 'Writers should always choose completely unfamiliar locations for this type of essay', 'This concept has no connection to writing', 'The writer’s personal connection to a place is never relevant to this essay form'], 0),
   ('Which of these sentences reflects a personal essay of place?', ['The old porch of my grandmother’s house still smells like the summer afternoons of my childhood.', 'The recipe calls for two cups of sugar and one egg.', 'The chemical symbol for sodium is Na.', 'The train departs the station at nine o’clock.'], 0),
   ('Why might reflecting on a meaningful location help a writer better understand their own personal growth?', ['Examining how a place shaped past experiences can reveal insights about how the writer has changed over time', 'Reflecting on a location never reveals anything about personal growth', 'This concept has no connection to writing', 'Personal growth has no connection to any specific location a writer has experienced'], 0)]),
F('Functions: Rational Functions — Slant Asymptotes',
  'Grade 11 Functions strand: a rational function has a slant, or oblique, asymptote when the degree of the numerator is exactly one more than the degree of the denominator.',
  [('When does a rational function have a slant asymptote?', ['When the numerator’s degree is exactly one more than the denominator’s degree', 'When the numerator and denominator have the exact same degree', 'A concept unrelated to rational functions', 'When the denominator’s degree is always higher than the numerator’s'], 0),
   ('What is another name for a slant asymptote?', ['An oblique asymptote', 'A vertical asymptote', 'A concept unrelated to asymptotes', 'A horizontal asymptote'], 0),
   ('Can polynomial long division be used to find the equation of a slant asymptote?', ['Yes', 'No, long division can never be used to find a slant asymptote', 'A concept unrelated to slant asymptotes', 'Slant asymptotes can only be found using a graphing calculator'], 0),
   ('Why does a rational function have only a slant asymptote, and not a horizontal asymptote, when the numerator’s degree exceeds the denominator’s degree by exactly one?', ['As x grows very large, the function behaves like a linear expression rather than approaching a constant value', 'A rational function can never have a slant asymptote under any circumstances', 'This concept has no connection to functions', 'The degrees of the numerator and denominator never affect the type of asymptote present'], 0),
   ('Why is finding the slant asymptote useful when sketching the graph of a rational function?', ['It shows the function’s long-term behaviour as x approaches positive or negative infinity', 'The slant asymptote never provides any useful information about a graph’s behaviour', 'This concept has no connection to functions', 'Graphing a rational function never requires any information about asymptotes'], 0)]),
B('Biology: Coral Reef Ecosystems and Bleaching',
  'Grade 11 Biology strand: coral reefs are built by colonies of coral organisms living in a mutualistic relationship with algae, and rising ocean temperatures can trigger coral bleaching, threatening the ecosystem.',
  [('What builds a coral reef?', ['Colonies of coral organisms', 'Large boulders that fall from cliffs', 'A concept unrelated to biology', 'Sand deposited by ocean currents'], 0),
   ('Do coral organisms live in a mutualistic relationship with algae?', ['Yes', 'No, coral organisms never interact with any algae', 'A concept unrelated to coral reef ecosystems', 'This relationship only ever harms the coral, never benefits it'], 0),
   ('What can rising ocean temperatures cause in coral reefs?', ['Coral bleaching', 'Increased coral growth with no negative effects', 'A concept unrelated to coral reefs', 'No change of any kind'], 0),
   ('Why does coral bleaching occur when ocean water becomes too warm?', ['Heat stress causes coral to expel the colourful algae that provide them with food and colour', 'Warmer water always makes coral healthier and more colourful', 'This concept has no connection to marine biology', 'Coral reefs are never affected by ocean temperature'], 0),
   ('Why is protecting coral reefs considered important for global marine biodiversity?', ['They support a huge variety of marine species that depend on the reef ecosystem for habitat and food', 'Coral reefs have no connection to marine biodiversity', 'This concept has no relevance to biology', 'Marine species never depend on coral reefs for survival'], 0)]),
C('Chemistry: Superconductivity and Low-Temperature Chemistry',
  'Grade 11 Chemistry strand: a superconductor conducts electricity with zero resistance when cooled below a critical temperature, a phenomenon studied within low-temperature chemistry and physics.',
  [('What is a superconductor?', ['A material that conducts electricity with zero resistance below a critical temperature', 'A material that always blocks electricity completely', 'A concept unrelated to chemistry', 'A material that only conducts electricity at room temperature'], 0),
   ('Does a superconductor need to be cooled below a certain temperature to achieve zero resistance?', ['Yes', 'No, superconductors work the same at any temperature', 'A concept unrelated to superconductors', 'Temperature has no connection to superconductivity'], 0),
   ('Does electric current flow through a superconductor without losing energy?', ['Yes', 'No, superconductors always lose significant energy', 'A concept unrelated to superconductors', 'Superconductors never actually conduct any electricity'], 0),
   ('Why might superconducting magnets be used in medical MRI machines?', ['They can generate strong, stable magnetic fields efficiently without energy loss from resistance', 'Superconductors have no connection to medical imaging technology', 'This concept has no relevance to chemistry', 'MRI machines never use any superconducting technology'], 0),
   ('Why is finding a superconductor that works at higher, more practical temperatures an active area of chemical research?', ['Current superconductors often require expensive, complex cooling systems to function', 'Superconductors already work perfectly at room temperature with no research needed', 'This concept has no relevance to chemistry', 'Cooling temperature has no connection to how superconductors are used'], 0)]),
]),

day(87, [
E('Oral Communication: Facilitating a Socratic Seminar',
  'Grade 11 English strand: facilitating a Socratic seminar involves guiding open-ended discussion through thoughtful questioning, encouraging participants to build on one another’s ideas rather than simply presenting opinions.',
  [('What does facilitating a Socratic seminar involve?', ['Guiding open-ended discussion through thoughtful questioning', 'Reading a prepared lecture with no discussion at all', 'A concept unrelated to oral communication', 'Grading participants silently with no interaction'], 0),
   ('Does a Socratic seminar encourage participants to build on one another’s ideas?', ['Yes', 'No, participants are never expected to respond to each other’s ideas', 'A concept unrelated to Socratic seminars', 'Only the facilitator is ever allowed to speak during this format'], 0),
   ('Why might a facilitator ask an open-ended question rather than one with a single correct answer?', ['Open-ended questions encourage deeper discussion and multiple perspectives rather than a single, quick response', 'Open-ended questions never encourage any deeper discussion', 'This concept has no connection to oral communication', 'A single correct answer always produces more valuable discussion than an open-ended question'], 0),
   ('Which of these best describes a facilitator’s role in a Socratic seminar?', ['Guiding the discussion with probing questions while allowing participants to explore ideas together', 'Providing every answer directly so participants do not need to think for themselves', 'Remaining completely silent and uninvolved throughout the entire discussion', 'Grading each participant’s response immediately after they speak'], 0),
   ('Why is active listening an important skill for participants in a Socratic seminar?', ['Responding thoughtfully to others’ ideas requires genuinely understanding what they have said', 'Active listening has no role in a successful Socratic seminar discussion', 'This concept has no relevance to oral communication', 'Participants never need to listen to each other in this type of discussion'], 0)]),
F('Discrete Math: Introduction to Modular Arithmetic',
  'Grade 11 Functions strand: modular arithmetic involves working with remainders after division, often described as clock arithmetic, since numbers wrap around after reaching a fixed value called the modulus.',
  [('What does modular arithmetic involve working with?', ['Remainders after division', 'Only whole, undivided numbers', 'A concept unrelated to functions', 'Only negative numbers'], 0),
   ('Why is modular arithmetic sometimes called clock arithmetic?', ['Numbers wrap around after reaching a fixed value, similar to how a clock resets after 12', 'Modular arithmetic has no connection to clocks or wrapping numbers', 'This concept has no connection to functions', 'Clocks and modular arithmetic have never been compared to each other'], 0),
   ('What is 23 mod 7, meaning the remainder when 23 is divided by 7?', ['2', '23', '7', '3'], 0),
   ('What is 17 mod 5, meaning the remainder when 17 is divided by 5?', ['2', '17', '5', '3'], 0),
   ('Why might modular arithmetic be useful for solving problems involving repeating cycles, like days of the week?', ['It naturally models patterns that repeat after a fixed number of steps', 'Modular arithmetic never applies to any repeating or cyclical pattern', 'This concept has no connection to functions', 'Days of the week have no connection to modular arithmetic'], 0)]),
B('Biology: The Human Microbiome',
  'Grade 11 Biology strand: the human microbiome consists of trillions of bacteria and other microorganisms living in and on the body, playing important roles in digestion, immunity, and overall health.',
  [('What does the human microbiome consist of?', ['Trillions of bacteria and other microorganisms living in and on the body', 'Only harmful pathogens with no beneficial function', 'A concept unrelated to biology', 'A single type of bacteria found only in the stomach'], 0),
   ('Can the human microbiome play a role in digestion?', ['Yes', 'No, the microbiome has no connection to digestion', 'A concept unrelated to the human microbiome', 'Digestion never involves any microorganisms at all'], 0),
   ('Can the human microbiome play a role in immune system function?', ['Yes', 'No, the microbiome has no connection to immunity', 'A concept unrelated to the human microbiome', 'The immune system never interacts with microorganisms in the body'], 0),
   ('Why might taking antibiotics sometimes disrupt a person’s digestive health, even while treating an infection?', ['Antibiotics can kill beneficial bacteria in the microbiome along with the harmful bacteria causing the infection', 'Antibiotics only ever target harmful bacteria and never affect beneficial ones', 'This concept has no connection to biology', 'Antibiotics have no effect on any bacteria living within the human body'], 0),
   ('Why is ongoing research into the human microbiome considered valuable for understanding overall health?', ['A growing body of evidence links microbiome balance to digestion, immunity, and even other aspects of health', 'The human microbiome has no connection to any aspect of a person’s overall health', 'This concept has no relevance to biology', 'Scientists have already fully understood every aspect of the human microbiome with no ongoing questions'], 0)]),
C('Chemistry: Battery Chemistry and Energy Storage',
  'Grade 11 Chemistry strand: batteries store chemical energy and convert it into electrical energy through a reaction between two electrodes separated by an electrolyte.',
  [('What type of energy do batteries store?', ['Chemical energy', 'Only light energy', 'A concept unrelated to batteries', 'Only sound energy'], 0),
   ('What are the two materials in a battery where a chemical reaction occurs, called?', ['Electrodes', 'A concept unrelated to batteries', 'Circuits', 'Insulators'], 0),
   ('What separates the two electrodes in a battery?', ['An electrolyte', 'A concept unrelated to batteries', 'A simple wire only', 'Nothing at all'], 0),
   ('Why might a rechargeable battery be able to reverse its chemical reaction?', ['Applying an external electrical current can reverse the chemical process, restoring the battery’s charge', 'Rechargeable batteries never actually reverse any chemical reaction', 'This concept has no connection to battery chemistry', 'All batteries work in exactly the same non-reversible way'], 0),
   ('Why is improving battery technology considered important for the wider adoption of electric vehicles?', ['Better batteries could allow vehicles to store more energy and travel farther on a single charge', 'Battery technology has no connection to electric vehicle range', 'This concept has no relevance to chemistry', 'Electric vehicles never actually rely on any battery technology'], 0)]),
]),

day(88, [
E('Reading: Analyzing Narrative Unreliability Through Free Indirect Discourse',
  'Grade 11 English strand: free indirect discourse blends a character’s inner thoughts with the narrator’s voice, often making it harder for readers to fully trust the perspective being presented.',
  [('What does free indirect discourse blend?', ['A character’s inner thoughts with the narrator’s voice', 'Only stage directions in a play', 'A concept unrelated to reading', 'A list of unrelated footnotes'], 0),
   ('Can free indirect discourse make it harder for readers to fully trust the perspective being presented?', ['Yes', 'No, this technique always makes a text’s perspective perfectly clear and reliable', 'A concept unrelated to free indirect discourse', 'Reader trust is never affected by this narrative technique'], 0),
   ('Why might free indirect discourse blur the line between a character’s subjective view and objective narration?', ['The technique merges a character’s thoughts into the narrative voice, without clearly marking them as separate', 'Free indirect discourse always keeps a character’s thoughts completely separate from the narration', 'This concept has no connection to reading comprehension', 'This technique never involves any blending of perspectives'], 0),
   ('Which of these best illustrates free indirect discourse?', ['She walked home slowly. Why did everyone always expect so much of her?', 'She said, I am walking home now.', 'The character walked home at six o’clock.', 'Chapter one begins with a description of the weather.'], 0),
   ('Why is recognizing free indirect discourse important when analyzing an unreliable narrator?', ['It helps readers identify when a character’s biased perspective is shaping the narration itself', 'Free indirect discourse has no connection to analyzing narrator reliability', 'This concept has no relevance to reading comprehension', 'Unreliable narration never involves any blending of character and narrator perspective'], 0)]),
F('Functions: Piecewise-Defined Function Modelling',
  'Grade 11 Functions strand: a piecewise-defined function uses different expressions or rules for different intervals of the domain, often modelling real-world situations that change under different conditions.',
  [('What does a piecewise-defined function use for different intervals of the domain?', ['Different expressions or rules', 'Only a single expression across the entire domain', 'A concept unrelated to functions', 'No defined rule at all'], 0),
   ('Might a piecewise function be used to model a cell phone plan with different rates depending on data usage?', ['Yes', 'No, cell phone plans can never be modelled using a piecewise function', 'A concept unrelated to piecewise functions', 'Piecewise functions only apply to purely mathematical, non-real-world situations'], 0),
   ('Does the domain of a piecewise function need to be divided into separate intervals?', ['Yes', 'No, the domain of a piecewise function is never divided into intervals', 'A concept unrelated to piecewise functions', 'Piecewise functions always use exactly the same rule across their entire domain'], 0),
   ('Why might a shipping company use a piecewise function to model delivery costs based on package weight?', ['Shipping costs often change at specific weight thresholds, which piecewise functions can accurately represent', 'Piecewise functions can never be used to model real-world pricing structures', 'This concept has no connection to functions', 'Shipping costs are always calculated using a single, unchanging formula regardless of weight'], 0),
   ('Why is it important to clearly define the boundaries between intervals when creating a piecewise function?', ['Overlapping or unclear boundaries could make the function ambiguous or produce more than one output for a single input', 'The boundaries between intervals never matter when defining a piecewise function', 'This concept has no connection to functions', 'A piecewise function can always safely ignore its interval boundaries with no issue'], 0)]),
B('Biology: Genetic Counselling and Inherited Disease Risk',
  'Grade 11 Biology strand: genetic counselling helps individuals and families understand their risk of inherited genetic conditions, using family history and genetic testing to inform decisions.',
  [('What does genetic counselling help individuals and families understand?', ['Their risk of inherited genetic conditions', 'Only unrelated dietary recommendations', 'A concept unrelated to biology', 'General exercise routines with no genetic connection'], 0),
   ('Might a genetic counsellor use family history to assess inherited disease risk?', ['Yes', 'No, family history is never considered in genetic counselling', 'A concept unrelated to genetic counselling', 'Genetic risk is never connected to a person’s family history'], 0),
   ('Can genetic testing be used as part of the genetic counselling process?', ['Yes', 'No, genetic testing has no connection to genetic counselling', 'A concept unrelated to genetic counselling', 'Testing is never involved in assessing inherited disease risk'], 0),
   ('Why might a couple planning to have children consult a genetic counsellor if a hereditary condition runs in their family?', ['A counsellor can help them understand the probability of passing on the condition and explore their options', 'Genetic counselling provides no useful information for family planning decisions', 'This concept has no connection to biology', 'Hereditary conditions never affect the probability of a child inheriting a genetic disorder'], 0),
   ('Why is genetic counselling considered valuable even when a genetic test result is uncertain or inconclusive?', ['A counsellor can help interpret the meaning and limitations of the results and guide informed next steps', 'Uncertain genetic test results provide no useful information worth discussing with a counsellor', 'This concept has no relevance to biology', 'Genetic counselling only ever applies when a test result is completely certain'], 0)]),
C('Chemistry: Forensic Chemistry — Trace Evidence Analysis',
  'Grade 11 Chemistry strand: forensic chemists analyze trace evidence, such as fibres, residues, and chemical compounds, using techniques like chromatography and spectroscopy to support criminal investigations.',
  [('What does forensic chemistry analyze to support criminal investigations?', ['Trace evidence, such as fibres, residues, and chemical compounds', 'Only witness testimony with no physical evidence', 'A concept unrelated to chemistry', 'Nothing at all connected to physical evidence'], 0),
   ('Name one technique forensic chemists use to analyze trace evidence, such as chromatography.', ['Chromatography', 'A concept unrelated to forensic chemistry', 'A weather forecast', 'A random guess with no scientific basis'], 0),
   ('Can spectroscopy help identify the chemical composition of an unknown substance?', ['Yes', 'No, spectroscopy has no connection to identifying chemical composition', 'A concept unrelated to forensic chemistry', 'Spectroscopy is never used in forensic analysis'], 0),
   ('Why might chromatography be useful for separating a mixture of chemical compounds found at a crime scene?', ['It separates individual components of a mixture based on their differing physical or chemical properties', 'Chromatography never separates any components of a chemical mixture', 'This concept has no connection to chemistry', 'Chemical mixtures found at a crime scene can never be separated or analyzed'], 0),
   ('Why is precise chemical analysis important in forensic investigations?', ['Accurate identification of trace evidence can provide critical, reliable information used in legal proceedings', 'Chemical analysis has no relevance to forensic investigations or legal proceedings', 'This concept has no relevance to chemistry', 'Trace evidence never provides any useful information in a criminal investigation'], 0)]),
]),

day(89, [
E('Literature: The Verse Novel',
  'Grade 11 English strand: a verse novel tells an extended narrative using poetic form and structure rather than traditional prose, blending storytelling with the compression and imagery of poetry.',
  [('What form does a verse novel use to tell its narrative?', ['Poetic form and structure', 'Only traditional prose paragraphs', 'A concept unrelated to literature', 'A screenplay format with no narration'], 0),
   ('Does a verse novel blend storytelling with the compression and imagery of poetry?', ['Yes', 'No, verse novels never use any poetic techniques', 'A concept unrelated to verse novels', 'Poetry has no connection to how a verse novel is written'], 0),
   ('Why might an author choose to tell a story through verse rather than traditional prose?', ['The compressed, rhythmic qualities of verse can create emotional intensity and a distinct reading experience', 'Verse never adds anything distinct to how a story is told', 'This concept has no connection to literature', 'Verse novels are always identical in style and effect to traditional prose novels'], 0),
   ('Which of these best describes a defining feature of the verse novel form?', ['An extended narrative told through poetic lines and stanzas rather than paragraphs', 'A story told entirely through dialogue with no narration at all', 'A collection of unrelated short poems with no connecting narrative', 'A textbook chapter formatted with bullet points'], 0),
   ('Why might white space and line breaks in a verse novel affect how a reader experiences the pacing of the story?', ['These structural choices can control rhythm and emphasis, shaping how quickly or slowly a reader moves through events', 'White space and line breaks never have any effect on how a reader experiences a story', 'This concept has no relevance to literature', 'Pacing in a verse novel is never influenced by its poetic structure'], 0)]),
F('Geometry: Vector Projections and the Cross Product',
  'Grade 11 Functions strand: the vector projection finds the component of one vector in the direction of another, while the cross product produces a new vector perpendicular to both original vectors.',
  [('What does a vector projection find?', ['The component of one vector in the direction of another', 'The exact length of a vector with no direction considered', 'A concept unrelated to vectors', 'A completely unrelated scalar with no geometric meaning'], 0),
   ('What kind of result does the cross product of two vectors produce?', ['A new vector perpendicular to both original vectors', 'A single scalar number only', 'A concept unrelated to vector operations', 'Two vectors that are always identical to the originals'], 0),
   ('Is the cross product typically defined for vectors in three-dimensional space?', ['Yes', 'No, the cross product is never used in three-dimensional space', 'A concept unrelated to the cross product', 'The cross product is only defined for two-dimensional vectors'], 0),
   ('Why might an engineer use the cross product to find a vector representing torque?', ['Torque is naturally represented as a vector perpendicular to both the force and the position vector involved', 'The cross product has no application in calculating torque', 'This concept has no connection to vectors', 'Torque can only ever be represented using a simple scalar quantity'], 0),
   ('Why might a vector projection be useful for calculating the amount of work done by a force acting at an angle?', ['It isolates the component of the force acting in the direction of motion, which determines the work performed', 'Vector projections have no connection to calculating work done by a force', 'This concept has no relevance to functions', 'Work is never affected by the direction of an applied force'], 0)]),
B('Biology: Biogeography and Continental Drift’s Effect on Species Distribution',
  'Grade 11 Biology strand: biogeography studies how species are distributed across the world, and the movement of continents over millions of years has significantly shaped where related species are found today.',
  [('What does biogeography study?', ['How species are distributed across the world', 'Only the chemical composition of rocks', 'A concept unrelated to biology', 'The exact population size of a single city'], 0),
   ('Has the movement of continents over millions of years shaped where related species are found today?', ['Yes', 'No, continental movement has no connection to species distribution', 'A concept unrelated to biogeography', 'Species distribution has never changed throughout Earth’s history'], 0),
   ('Might closely related species be found on continents that were once connected but have since drifted apart?', ['Yes', 'No, related species are never found on separated continents', 'A concept unrelated to biogeography', 'Continents have never actually moved throughout Earth’s history'], 0),
   ('Why might finding similar fossil species on continents that are now far apart support the theory of continental drift?', ['It suggests these continents were once joined, allowing related species to exist in the same original location', 'Similar fossils on separate continents provide no evidence about continental movement', 'This concept has no connection to biology', 'Fossil evidence has no connection to theories about continental drift'], 0),
   ('Why is biogeography considered valuable for understanding the evolutionary history of a group of species?', ['Patterns in species distribution can reveal how populations became separated and evolved independently over time', 'Biogeography has no connection to understanding evolutionary history', 'This concept has no relevance to biology', 'Species distribution never provides any insight into evolutionary processes'], 0)]),
C('Chemistry: The Chemistry of Cosmetics and Personal Care Products',
  'Grade 11 Chemistry strand: cosmetics and personal care products rely on chemistry to combine ingredients like emulsifiers, preservatives, and active compounds into stable, effective formulations.',
  [('What do cosmetics and personal care products rely on to combine their ingredients?', ['Chemistry', 'Only random mixing with no scientific process', 'A concept unrelated to chemistry', 'Nothing at all related to chemical formulation'], 0),
   ('Name one type of ingredient commonly used in cosmetic formulations, such as an emulsifier.', ['An emulsifier', 'A concept unrelated to cosmetic chemistry', 'A random unrelated household item', 'A type of rock formation'], 0),
   ('Do preservatives help keep personal care products stable and safe over time?', ['Yes', 'No, preservatives have no effect on product stability or safety', 'A concept unrelated to cosmetic chemistry', 'Preservatives are never actually used in personal care products'], 0),
   ('Why might an emulsifier be necessary in a lotion that combines both water-based and oil-based ingredients?', ['Water and oil do not naturally mix, so an emulsifier helps keep the mixture stable and evenly combined', 'Water and oil always mix naturally without requiring any special ingredient', 'This concept has no connection to chemistry', 'Emulsifiers have no connection to combining different types of ingredients'], 0),
   ('Why is understanding the chemistry behind personal care products useful for evaluating their safety and effectiveness?', ['It helps consumers and scientists understand how ingredients interact and what role each one plays in the final product', 'The chemistry of these products has no connection to their safety or effectiveness', 'This concept has no relevance to chemistry', 'Personal care products contain no chemical ingredients worth understanding'], 0)]),
]),

day(90, [
E('Review: Genre, Rhetoric, and Narrative Technique (Days 81-89)',
  'Grade 11 English strand review: students revisit the Kunstlerroman, eulogies, deepfake media analysis, the subjunctive mood, ecocriticism, personal essays of place, Socratic seminars, free indirect discourse, and the verse novel.',
  [('What does a Kunstlerroman trace the development of?', ['An artist, from youth into their mature creative identity', 'A political leader’s rise to power', 'A concept unrelated to literature', 'A scientific discovery over several decades'], 0),
   ('What does ecocriticism examine in literature?', ['How literature represents nature and the environment', 'Only the grammar and punctuation used in a text', 'A concept unrelated to literary study', 'The exact publication date of a text'], 0),
   ('Which sentence correctly uses the subjunctive mood?', ['If I were rich, I would travel the world.', 'If I was rich, I would travel the world.', 'If I am rich, I would travel the world.', 'If I will be rich, I would travel the world.'], 0),
   ('What does free indirect discourse blend?', ['A character’s inner thoughts with the narrator’s voice', 'Only stage directions in a play', 'A concept unrelated to reading', 'A list of unrelated footnotes'], 0),
   ('What form does a verse novel use to tell its narrative?', ['Poetic form and structure', 'Only traditional prose paragraphs', 'A concept unrelated to literature', 'A screenplay format with no narration'], 0)]),
F('Review: Functions, Trigonometry, and Discrete Math (Days 81-89)',
  'Grade 11 Functions strand review: students revisit logarithmic scales, recursive sequences, absolute value equations, double-angle formulas, the binomial distribution, slant asymptotes, modular arithmetic, piecewise modelling, and vector projections.',
  [('What do logarithmic scales like pH and the Richter scale help do?', ['Compress a huge range of values into a more manageable set of numbers', 'Expand small numbers into much larger ones with no practical use', 'A concept unrelated to functions', 'Convert numbers into fractions only'], 0),
   ('How is each term of the Fibonacci sequence generated?', ['By adding the two preceding terms', 'By multiplying the term’s position by two', 'A concept unrelated to sequences', 'By subtracting one from the previous term'], 0),
   ('When does a rational function have a slant asymptote?', ['When the numerator’s degree is exactly one more than the denominator’s degree', 'When the numerator and denominator have the exact same degree', 'A concept unrelated to rational functions', 'When the denominator’s degree is always higher than the numerator’s'], 0),
   ('What does a piecewise-defined function use for different intervals of the domain?', ['Different expressions or rules', 'Only a single expression across the entire domain', 'A concept unrelated to functions', 'No defined rule at all'], 0),
   ('What does a vector projection find?', ['The component of one vector in the direction of another', 'The exact length of a vector with no direction considered', 'A concept unrelated to vectors', 'A completely unrelated scalar with no geometric meaning'], 0)]),
B('Review: Genetics, Ecology, and Human Health (Days 81-89)',
  'Grade 11 Biology strand review: students revisit photoperiodism, the skeletal system, symbiotic relationships, epigenetics, vaccines and herd immunity, coral reef bleaching, the human microbiome, genetic counselling, and biogeography.',
  [('What does photoperiodism describe in plants?', ['How plants respond to the relative length of day and night', 'How plants absorb water through their roots', 'A concept unrelated to biology', 'How plants convert sugar into starch'], 0),
   ('What process do bones continuously undergo to maintain strength?', ['Remodelling', 'Complete replacement every single day', 'A concept unrelated to biology', 'A process that never actually occurs in bones'], 0),
   ('What term describes the protection a population gains when enough individuals are immune to a disease?', ['Herd immunity', 'A concept unrelated to vaccines', 'Individual immunity only', 'Passive immunity exclusively'], 0),
   ('What does the human microbiome consist of?', ['Trillions of bacteria and other microorganisms living in and on the body', 'Only harmful pathogens with no beneficial function', 'A concept unrelated to biology', 'A single type of bacteria found only in the stomach'], 0),
   ('What does biogeography study?', ['How species are distributed across the world', 'Only the chemical composition of rocks', 'A concept unrelated to biology', 'The exact population size of a single city'], 0)]),
C('Review: Equilibrium, Materials, and Applied Chemistry (Days 81-89)',
  'Grade 11 Chemistry strand review: students revisit buffer capacity, industrial catalysis, radiometric dating, biodegradable plastics, pyrotechnic chemistry, superconductivity, battery chemistry, forensic trace evidence, and cosmetic chemistry.',
  [('What does buffer capacity describe?', ['How much acid or base a buffer can absorb before its pH changes significantly', 'The exact colour of a buffer solution', 'A concept unrelated to chemistry', 'The temperature at which a buffer solution freezes'], 0),
   ('What does radiometric dating use to estimate the age of a material?', ['The known decay rate of radioactive isotopes', 'The colour of the material’s surface', 'A concept unrelated to chemistry', 'The material’s exact weight in kilograms'], 0),
   ('What do fireworks use to produce specific colours when heated?', ['Metal salts', 'Only plain water', 'A concept unrelated to chemistry', 'Ordinary table sugar'], 0),
   ('What is a superconductor?', ['A material that conducts electricity with zero resistance below a critical temperature', 'A material that always blocks electricity completely', 'A concept unrelated to chemistry', 'A material that only conducts electricity at room temperature'], 0),
   ('What do cosmetics and personal care products rely on to combine their ingredients?', ['Chemistry', 'Only random mixing with no scientific process', 'A concept unrelated to chemistry', 'Nothing at all related to chemical formulation'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_81_90)
    append_to(11, g11_81_90)
