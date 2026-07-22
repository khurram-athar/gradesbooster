#!/usr/bin/env python3
"""Grade 6, Days 91-100 -- extends Grade 6 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade6.json):
verbal/situational/dramatic irony, gerunds and infinitives, persuasive
speeches, hyperbole and understatement, propaganda techniques, character
motivation, paraphrasing and avoiding plagiarism, myths and legends across
cultures, formal vs informal register; adding and subtracting integers on a
number line, box-and-whisker plots, congruent figures and congruence
transformations, sales tax and total cost, independent vs dependent
probability events, converting units of capacity and mass, choosing the
best graph to display data, line graphs and trends, representing patterns
with tables/graphs/expressions; the endocrine system, world biomes,
extinction and endangered species, the excretory system, recycling and
waste reduction, camouflage and mimicry, igneous/sedimentary/metamorphic
rocks, wind energy and turbine design, biomimicry; the Truth and
Reconciliation Commission of Canada, UNESCO World Heritage Sites, ancient
Nubia, the Canadian Senate, global population growth, Canada's national
parks, the spread of world religions, the role of NGOs in global aid, and
Canada's role in international development and foreign aid.

Subject keys for Grade 6 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 6 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science and Technology',
    'TVO Learn: Grade 6 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L6, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M6, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S6, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS6, q)


def _rebalance_answer_positions(days, seed=20260925):
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


g6_91_100 = [
day(91, [
L('Reading: Understanding Verbal, Situational, and Dramatic Irony',
  'Grade 6 Language strand: irony occurs when there is a gap between what is expected and what actually happens, and can take the form of verbal irony (saying the opposite of what is meant), situational irony (an unexpected outcome), or dramatic irony (the audience knows something a character does not).',
  [('What is irony?', ['A gap between what is expected and what actually happens', 'A concept unrelated to reading', 'A type of punctuation mark', 'A synonym for a simile'], 0),
   ('If a character says Great weather! during a thunderstorm, what type of irony is this?', ['Verbal irony', 'Situational irony', 'Dramatic irony', 'A concept unrelated to irony'], 0),
   ('If the audience knows a character is walking into a trap but the character does not, what type of irony is this?', ['Dramatic irony', 'Verbal irony', 'Situational irony', 'A concept unrelated to irony'], 0),
   ('A fire station burning down would be an example of which type of irony?', ['Situational irony', 'Verbal irony', 'Dramatic irony', 'A concept unrelated to irony'], 0),
   ('Why might an author use dramatic irony to build suspense in a story?', ['Knowing more than a character does can make readers anxious about what will happen next', 'Dramatic irony never creates any suspense for readers', 'This concept has no connection to reading comprehension', 'Readers should never know more than a character in a story'], 0)]),
M('Adding and Subtracting Integers on a Number Line',
  'Grade 6 Math strand: adding and subtracting integers can be modelled on a number line, where adding a positive number moves right and adding a negative number, or subtracting a positive number, moves left.',
  [('On a number line, which direction does adding a positive number move you?', ['Right', 'Left', 'A concept unrelated to integers', 'It does not move you at all'], 0),
   ('On a number line, which direction does adding a negative number move you?', ['Left', 'Right', 'A concept unrelated to integers', 'It does not move you at all'], 0),
   ('What is negative 3 plus 5?', ['2', '-2', '8', '-8'], 0),
   ('What is 4 minus 7?', ['-3', '3', '11', '-11'], 0),
   ('Why can a number line be a useful tool for adding and subtracting integers?', ['It gives a visual way to track movement in a positive or negative direction', 'Number lines never help with understanding integer operations', 'This concept has no connection to math', 'Integers can never be represented on a number line'], 0)]),
Sc('Science: The Endocrine System and Hormones',
   'Grade 6 Science strand: the endocrine system is made up of glands that release hormones, chemical messengers that travel through the blood to control body processes such as growth, energy use, and mood.',
   [('What does the endocrine system release into the body?', ['Hormones', 'Only blood cells', 'A concept unrelated to the human body', 'Only oxygen'], 0),
    ('How do hormones travel through the body?', ['Through the blood', 'Through the digestive system only', 'A concept unrelated to hormones', 'Hormones never travel anywhere in the body'], 0),
    ('Can hormones affect processes like growth and mood?', ['Yes', 'No, hormones have no effect on the body', 'A concept unrelated to hormones', 'Hormones only affect breathing'], 0),
    ('Why might a gland releasing too much or too little of a hormone cause health problems?', ['Hormones help regulate important body processes, so an imbalance can disrupt how the body functions', 'Hormone levels never affect health in any way', 'This concept has no connection to biology', 'The body works exactly the same no matter the hormone levels'], 0),
    ('Why do scientists describe hormones as chemical messengers?', ['They carry signals from glands to other parts of the body that need to respond', 'Hormones never carry any kind of signal', 'This concept has no relevance to science', 'Hormones are identical to nerve cells'], 0)]),
SS('Social Studies: The Truth and Reconciliation Commission of Canada',
   'Grade 6 Social Studies strand: the Truth and Reconciliation Commission was established to document the experiences of Indigenous survivors of residential schools and to make recommendations, known as Calls to Action, toward reconciliation in Canada.',
   [('What did the Truth and Reconciliation Commission document?', ['The experiences of Indigenous survivors of residential schools', 'The history of Canadian sports', 'A concept unrelated to Canadian history', 'The founding of Canadian cities'], 0),
    ('What are the Commission’s recommendations for reconciliation known as?', ['Calls to Action', 'Trade Agreements', 'A concept unrelated to the Commission', 'Provincial Laws'], 0),
    ('Was the Truth and Reconciliation Commission focused on Indigenous experiences in Canada?', ['Yes', 'No, it focused only on international trade', 'A concept unrelated to Canadian history', 'It had no connection to Indigenous peoples'], 0),
    ('Why might listening to survivor testimonies have been an important part of the Commission’s work?', ['It helped create an accurate record of history and acknowledge the harm experienced by survivors', 'Survivor testimonies were never included in the Commission’s work', 'This concept has no connection to social studies', 'The Commission ignored the experiences of survivors entirely'], 0),
    ('Why is reconciliation described as an ongoing process rather than a single completed event?', ['Rebuilding trust and addressing historical harms takes sustained effort over time', 'Reconciliation was fully completed the moment the Commission ended', 'This concept has no relevance to social studies', 'Reconciliation has no connection to Indigenous and non-Indigenous relationships'], 0)]),
]),

day(92, [
L('Grammar: Gerunds and Infinitives',
  'Grade 6 Language strand: a gerund is a verb form ending in -ing that acts as a noun, such as swimming in Swimming is fun, while an infinitive is the word to plus a verb, such as to swim, which can also act as a noun.',
  [('What is a gerund?', ['A verb form ending in -ing that acts as a noun', 'A concept unrelated to grammar', 'A word that describes a noun', 'A punctuation mark'], 0),
   ('What is an infinitive?', ['The word to plus a verb', 'A verb form ending in -ing only', 'A concept unrelated to grammar', 'A type of punctuation mark'], 0),
   ('In the sentence Swimming is fun, what part of speech is swimming acting as?', ['A noun', 'An adjective', 'A concept unrelated to grammar', 'A preposition'], 0),
   ('Which sentence correctly uses an infinitive?', ['She wants to read every night.', 'She wants reading every night to.', 'To she wants read every night.', 'She wants read to every night.'], 0),
   ('Why might a writer use a gerund instead of a regular verb in a sentence?', ['A gerund allows an action to function as the subject or object of a sentence', 'Gerunds can never function as a subject or object', 'This concept has no connection to grammar', 'Regular verbs and gerunds are always exactly the same'], 0)]),
M('Data: Box-and-Whisker Plots and Data Spread',
  'Grade 6 Math strand: a box-and-whisker plot displays how data is spread out using five key values: the minimum, first quartile, median, third quartile, and maximum.',
  [('What does a box-and-whisker plot display?', ['How data is spread out', 'Only the mean of a data set', 'A concept unrelated to data management', 'Nothing about a data set'], 0),
   ('Name one of the five key values shown in a box-and-whisker plot.', ['The median', 'A concept unrelated to box-and-whisker plots', 'The colour of the data', 'The name of the data set'], 0),
   ('In a box-and-whisker plot, what does the line inside the box represent?', ['The median', 'The minimum only', 'A concept unrelated to box-and-whisker plots', 'The maximum only'], 0),
   ('If a box-and-whisker plot has a very long whisker on one side, what might that suggest?', ['There may be some values spread far from the rest of the data', 'The data is always perfectly even on both sides', 'This concept has no connection to data spread', 'A long whisker means there is no data at all'], 0),
   ('Why might a box-and-whisker plot be useful for comparing two data sets?', ['It shows the spread and middle values of each set side by side for easy comparison', 'Box-and-whisker plots can never be used to compare data sets', 'This concept has no connection to math', 'Box-and-whisker plots only work with a single data value'], 0)]),
Sc('Science: Biomes of the World: Desert, Tundra, Rainforest, and Grassland',
   'Grade 6 Science strand: a biome is a large region with a distinct climate, plants, and animals, such as a desert with little rainfall, a tundra with frozen ground, a rainforest with dense vegetation, or a grassland with wide open plains.',
   [('What is a biome?', ['A large region with a distinct climate, plants, and animals', 'A single type of rock', 'A concept unrelated to Earth science', 'A single species of animal'], 0),
    ('Which biome typically has very little rainfall?', ['Desert', 'Rainforest', 'A concept unrelated to biomes', 'Wetland'], 0),
    ('Which biome has permanently frozen ground called permafrost?', ['Tundra', 'Rainforest', 'A concept unrelated to biomes', 'Desert'], 0),
    ('Why do plants and animals in a rainforest differ so much from those in a desert?', ['Each biome’s climate and available resources shape which living things can survive there', 'Every biome has the exact same plants and animals', 'This concept has no connection to biology', 'Climate has no effect on which living things survive in a region'], 0),
    ('Why is understanding biomes important for conservation efforts?', ['Different biomes require different strategies to protect their unique species and habitats', 'All biomes require the exact same conservation strategy', 'This concept has no relevance to science', 'Biomes never need any kind of conservation effort'], 0)]),
SS('Social Studies: UNESCO World Heritage Sites and Cultural Preservation',
   'Grade 6 Social Studies strand: a UNESCO World Heritage Site is a place recognized for its outstanding cultural, historical, or natural significance, and is protected to help preserve it for future generations.',
   [('What is a UNESCO World Heritage Site?', ['A place recognized for outstanding cultural, historical, or natural significance', 'A place with no historical significance at all', 'A concept unrelated to global heritage', 'A type of modern shopping centre'], 0),
    ('Why are World Heritage Sites given special protection?', ['To help preserve them for future generations', 'To make them harder for anyone to visit', 'A concept unrelated to cultural preservation', 'Protection has no connection to World Heritage Sites'], 0),
    ('Can a World Heritage Site be a natural landmark rather than a human-made structure?', ['Yes', 'No, only human-made structures can be listed', 'A concept unrelated to World Heritage Sites', 'Natural landmarks are never recognized in any way'], 0),
    ('Why might countries around the world choose to work together to identify and protect these sites?', ['Cultural and natural heritage is considered valuable to all of humanity, not just one country', 'Countries never cooperate on protecting heritage sites', 'This concept has no connection to social studies', 'Heritage sites only matter to the country where they are located'], 0),
    ('Why might tourism at a World Heritage Site present both benefits and challenges?', ['Tourism can support the local economy but may also put pressure on fragile sites', 'Tourism never has any effect on a heritage site', 'This concept has no relevance to social studies', 'Heritage sites are never visited by tourists'], 0)]),
]),

day(93, [
L('Writing: Crafting a Persuasive Speech',
  'Grade 6 Language strand: a persuasive speech uses a clear position, strong evidence, and rhetorical techniques to convince a live audience to agree with the speaker’s viewpoint or take a specific action.',
  [('What is the main goal of a persuasive speech?', ['To convince a live audience to agree with a viewpoint or take action', 'To simply describe an event with no opinion', 'A concept unrelated to writing', 'To entertain an audience with no message at all'], 0),
   ('Should a persuasive speech include supporting evidence?', ['Yes', 'No, persuasive speeches never include evidence', 'A concept unrelated to persuasive writing', 'Evidence is only used in fictional stories'], 0),
   ('Why might a persuasive speech benefit from a strong, memorable opening?', ['It can quickly capture the audience’s attention and set up the main argument', 'A strong opening never affects how an audience responds', 'This concept has no connection to writing', 'Persuasive speeches should always begin with unrelated information'], 0),
   ('Which of these is most likely a strong closing line for a persuasive speech?', ['Join me in making our school a greener place, starting today.', 'The weather today is sunny with a chance of clouds.', 'Chapter one begins with a young girl in a forest.', 'The recipe calls for two cups of flour.'], 0),
   ('Why might a speaker use repetition of a key phrase throughout a persuasive speech?', ['Repeating a phrase can help the main message stick in the audience’s memory', 'Repetition never has any effect on an audience', 'This concept has no connection to persuasive writing', 'Persuasive speeches should never repeat any words or phrases'], 0)]),
M('Congruent Figures and Congruence Transformations',
  'Grade 6 Math strand: congruent figures are shapes that are exactly the same size and shape, and can be shown to be congruent using transformations like translations, reflections, and rotations that do not change size.',
  [('What does it mean for two figures to be congruent?', ['They are exactly the same size and shape', 'They are the same shape but different sizes', 'A concept unrelated to geometry', 'They share only one matching side'], 0),
   ('Name one type of transformation that can show two figures are congruent.', ['A reflection', 'A concept unrelated to congruence', 'A resizing that changes area', 'A colour change'], 0),
   ('Does a translation, reflection, or rotation change the size of a figure?', ['No', 'Yes, it always doubles the size', 'A concept unrelated to transformations', 'Yes, it always halves the size'], 0),
   ('If a triangle is reflected across a line, is the resulting triangle congruent to the original?', ['Yes', 'No, reflections always change a shape’s size', 'A concept unrelated to congruence', 'Reflections never produce a matching shape'], 0),
   ('Why is understanding congruence useful in fields like construction or design?', ['It helps ensure that parts made to the same specifications will fit together correctly', 'Congruence has no real-world application at all', 'This concept has no connection to geometry', 'Construction never requires identical shapes or parts'], 0)]),
Sc('Science: Extinction and Endangered Species Conservation',
   'Grade 6 Science strand: extinction occurs when a species no longer exists anywhere on Earth, and conservation efforts aim to protect endangered species, those at serious risk of extinction, through habitat protection and other measures.',
   [('What does extinction mean for a species?', ['It no longer exists anywhere on Earth', 'It has moved to a new habitat', 'A concept unrelated to biology', 'It has grown in population everywhere'], 0),
    ('What do we call a species at serious risk of extinction?', ['An endangered species', 'A concept unrelated to conservation', 'A dominant species', 'An invasive species'], 0),
    ('Can habitat protection help prevent a species from becoming extinct?', ['Yes', 'No, habitat protection has no effect on extinction', 'A concept unrelated to conservation', 'Habitat protection always increases extinction risk'], 0),
    ('Why might the loss of a single species affect an entire ecosystem?', ['Species are often interconnected, so losing one can disrupt food webs and other relationships', 'Losing one species never affects any other living things', 'This concept has no connection to biology', 'Ecosystems never depend on more than one species'], 0),
    ('Why do conservationists study the causes of a species’ decline before creating a protection plan?', ['Understanding the specific threats helps target the most effective conservation strategies', 'The causes of decline are never relevant to conservation planning', 'This concept has no relevance to science', 'Every endangered species faces exactly the same threats'], 0)]),
SS('Social Studies: Ancient Nubia: Kingdoms Along the Nile',
   'Grade 6 Social Studies strand: ancient Nubia was home to a series of powerful kingdoms south of Egypt along the Nile River, known for skilled ironworking, extensive trade networks, and, during the Kingdom of Kush, even ruling over Egypt itself.',
   [('Where was ancient Nubia located?', ['South of Egypt along the Nile River', 'North of Rome', 'A concept unrelated to ancient history', 'In present-day South America'], 0),
    ('What skill was ancient Nubia known for?', ['Ironworking', 'Building skyscrapers', 'A concept unrelated to Nubia', 'Manufacturing cars'], 0),
    ('Did the Kingdom of Kush, a Nubian kingdom, ever rule over Egypt?', ['Yes', 'No, Nubia never had any connection to Egypt', 'A concept unrelated to Nubian history', 'Egypt and Nubia never interacted at all'], 0),
    ('Why might Nubia’s location along the Nile River have supported extensive trade networks?', ['The river provided a natural route for transporting goods and connecting distant regions', 'Rivers never provide any benefit for trade', 'This concept has no connection to Nubian history', 'Nubia had no access to any waterways at all'], 0),
    ('Why is it important for students to learn about African civilizations like ancient Nubia alongside better-known ones like ancient Egypt?', ['It gives a fuller and more accurate picture of the achievements of ancient African societies', 'Ancient Nubia had no notable achievements of its own', 'This concept has no relevance to social studies', 'Only ancient Egypt is worth studying in African history'], 0)]),
]),

day(94, [
L('Vocabulary: Hyperbole and Understatement',
  'Grade 6 Language strand: hyperbole is exaggeration used for emphasis or humour, such as I have told you a million times, while understatement makes something seem less significant than it is, such as calling a hurricane a bit windy.',
  [('What is hyperbole?', ['Exaggeration used for emphasis or humour', 'A concept unrelated to vocabulary', 'A word that sounds like its meaning', 'A comparison using like or as'], 0),
   ('What is understatement?', ['Making something seem less significant than it is', 'Making something seem more significant than it is', 'A concept unrelated to vocabulary', 'A word borrowed from another language'], 0),
   ('Which of these is an example of hyperbole?', ['I have told you a million times.', 'The sky is blue today.', 'She walked to the store.', 'The book has 200 pages.'], 0),
   ('Which of these is an example of understatement?', ['Calling a hurricane a bit windy', 'Calling a hurricane the worst storm in history', 'Describing a hurricane using only exact wind speeds', 'A concept unrelated to understatement'], 0),
   ('Why might a writer use hyperbole or understatement instead of a literal description?', ['They can create humour, emphasis, or a particular tone that a literal description might not achieve', 'Hyperbole and understatement never affect the tone of a text', 'This concept has no connection to writing', 'Literal descriptions and exaggerations always create the exact same effect'], 0)]),
M('Financial Literacy: Calculating Sales Tax and Total Cost',
  'Grade 6 Math strand: sales tax is a percentage added to the price of goods or services at the time of purchase, and the total cost is found by adding the tax amount to the original price.',
  [('What is sales tax?', ['A percentage added to the price of goods or services', 'A discount subtracted from the price', 'A concept unrelated to shopping', 'A fee charged only once a year'], 0),
   ('To find the total cost of an item, what do you add to the original price?', ['The sales tax amount', 'Nothing at all', 'A concept unrelated to sales tax', 'The store’s address'], 0),
   ('If an item costs 20 dollars and the sales tax is 10 percent, how much is the tax amount?', ['2 dollars', '10 dollars', '20 dollars', '22 dollars'], 0),
   ('If an item costs 20 dollars and the sales tax is 10 percent, what is the total cost?', ['22 dollars', '20 dollars', '2 dollars', '30 dollars'], 0),
   ('Why is it useful to estimate sales tax before making a purchase?', ['It helps shoppers know the actual amount they will need to pay, not just the listed price', 'Sales tax never affects the final amount paid', 'This concept has no connection to financial literacy', 'The listed price is always exactly what a shopper pays'], 0)]),
Sc('Science: The Excretory System and Waste Removal in the Body',
   'Grade 6 Science strand: the excretory system, including the kidneys, removes waste products and excess water from the blood, forming urine, which helps keep the body’s internal environment balanced.',
   [('What is the job of the excretory system?', ['To remove waste products and excess water from the blood', 'To pump blood throughout the body', 'A concept unrelated to the human body', 'To digest food'], 0),
    ('Name one organ that is part of the excretory system.', ['The kidneys', 'A concept unrelated to the excretory system', 'The lungs only', 'The brain'], 0),
    ('Does the excretory system help form urine?', ['Yes', 'No, urine has no connection to the excretory system', 'A concept unrelated to the excretory system', 'Urine is formed by the digestive system instead'], 0),
    ('Why is it important for the body to remove waste products from the blood?', ['Built-up waste could become harmful if it is not regularly filtered out', 'Waste products in the blood never cause any harm', 'This concept has no connection to biology', 'The blood never contains any waste products'], 0),
    ('Why might drinking enough water support the excretory system’s function?', ['Water helps the kidneys filter waste efficiently and helps form urine', 'Water has no effect on how the kidneys function', 'This concept has no relevance to science', 'The excretory system works better without any water at all'], 0)]),
SS('Social Studies: The Structure and Role of the Canadian Senate',
   'Grade 6 Social Studies strand: the Canadian Senate is the upper house of Parliament, made up of appointed members who review, debate, and can propose changes to bills before they become law.',
   [('What is the Canadian Senate?', ['The upper house of Parliament', 'A provincial court', 'A concept unrelated to government', 'A municipal council'], 0),
    ('Are members of the Senate appointed or elected?', ['Appointed', 'Elected', 'A concept unrelated to the Senate', 'Neither appointed nor elected'], 0),
    ('Can the Senate review and debate bills before they become law?', ['Yes', 'No, the Senate has no role in reviewing bills', 'A concept unrelated to the Senate', 'Only the House of Commons is allowed to review bills'], 0),
    ('Why might having a Senate review bills already passed by the House of Commons be useful?', ['It provides an additional layer of scrutiny that could catch problems before a bill becomes law', 'A second review of a bill never serves any purpose', 'This concept has no connection to Canadian government', 'Bills never need to be reviewed more than once'], 0),
    ('Why do some Canadians debate whether Senators should be appointed or elected?', ['People have different views on which method best ensures the Senate is fair and accountable', 'No one in Canada has ever discussed how Senators are chosen', 'This concept has no relevance to social studies', 'The method of choosing Senators has never changed or been debated'], 0)]),
]),

day(95, [
L('Media Literacy: Recognizing Propaganda Techniques',
  'Grade 6 Language strand: propaganda uses techniques such as emotional appeals, repetition, and bandwagon messaging (suggesting everyone else is doing something) to influence people’s opinions, often without presenting balanced information.',
  [('What is propaganda used to do?', ['Influence people’s opinions', 'Provide only balanced, neutral information', 'A concept unrelated to media literacy', 'Entertain readers with no persuasive goal'], 0),
   ('Name one technique used in propaganda, such as repetition or emotional appeals.', ['Repetition', 'A concept unrelated to propaganda', 'Footnotes', 'Page numbers'], 0),
   ('What is bandwagon messaging?', ['Suggesting everyone else is doing something to encourage you to join in', 'A method of presenting only balanced facts', 'A concept unrelated to propaganda', 'A technique used only in fictional stories'], 0),
   ('Does propaganda typically present a fully balanced view of an issue?', ['No', 'Yes, propaganda always presents every side equally', 'A concept unrelated to propaganda', 'Propaganda never expresses any kind of viewpoint'], 0),
   ('Why is it important for readers to recognize propaganda techniques in media?', ['Recognizing these techniques helps readers think critically instead of being easily persuaded', 'Propaganda techniques never actually influence how people think', 'This concept has no connection to media literacy', 'Readers never need to evaluate the messages they encounter'], 0)]),
M('Probability: Independent and Dependent Events',
  'Grade 6 Math strand: an independent event is one where the outcome does not affect another event, like flipping a coin twice, while a dependent event is one where the outcome does affect another, like drawing cards without replacement.',
  [('What is an independent event?', ['An event whose outcome does not affect another event', 'An event that always affects another event', 'A concept unrelated to probability', 'An event that never has any outcome'], 0),
   ('What is a dependent event?', ['An event whose outcome does affect another event', 'An event that never affects anything else', 'A concept unrelated to probability', 'An event with no possible outcomes'], 0),
   ('Is flipping a coin twice an example of independent or dependent events?', ['Independent', 'Dependent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0),
   ('Is drawing two cards from a deck without replacing the first card an example of independent or dependent events?', ['Dependent', 'Independent', 'A concept unrelated to probability', 'Neither independent nor dependent'], 0),
   ('Why does removing a card from a deck without replacing it change the probability of the next draw?', ['There are fewer total cards left, so the chances for each remaining card change', 'Removing a card never affects the probability of future draws', 'This concept has no connection to probability', 'The deck always has the exact same number of cards no matter what'], 0)]),
Sc('Science: The Science of Recycling and Waste Reduction',
   'Grade 6 Science strand: recycling processes used materials like paper, glass, and plastic so they can be made into new products, reducing the need for new raw materials and helping lower the amount of waste sent to landfills.',
   [('What does recycling do with used materials?', ['Processes them so they can be made into new products', 'Destroys them completely with no further use', 'A concept unrelated to waste management', 'Buries them permanently underground'], 0),
    ('Name one material that can commonly be recycled, such as paper or glass.', ['Paper', 'A concept unrelated to recycling', 'Food scraps only', 'Nothing can be recycled'], 0),
    ('Can recycling help reduce the need for new raw materials?', ['Yes', 'No, recycling never reduces the need for raw materials', 'A concept unrelated to recycling', 'Recycling always increases the need for raw materials'], 0),
    ('Why might reducing the amount of waste sent to landfills be beneficial for the environment?', ['Landfills can take up land and release harmful substances as waste breaks down', 'Landfills have no impact on the environment at all', 'This concept has no connection to science', 'Reducing landfill waste always harms the environment more'], 0),
    ('Why do some products carry a recycling symbol showing what type of material they are made of?', ['It helps people sort materials correctly so they can be properly recycled', 'The recycling symbol has no connection to sorting materials', 'This concept has no relevance to science', 'Products are never labelled with any information about their materials'], 0)]),
SS('Social Studies: Global Population Growth and Demographic Change',
   'Grade 6 Social Studies strand: global population growth refers to the increasing number of people living on Earth over time, and demographic change describes shifts in factors like age, location, and family size within populations.',
   [('What does global population growth refer to?', ['The increasing number of people living on Earth over time', 'A decrease in the number of people on Earth', 'A concept unrelated to geography', 'The number of animals living on Earth'], 0),
    ('What does demographic change describe?', ['Shifts in factors like age, location, and family size within populations', 'A concept unrelated to population studies', 'Changes in the weather only', 'Changes in ocean currents only'], 0),
    ('Can demographic change include shifts in where people choose to live?', ['Yes', 'No, demographic change never involves where people live', 'A concept unrelated to demographic change', 'People never move to new locations'], 0),
    ('Why might rapid population growth in a region create challenges for resources like housing and water?', ['A larger population increases demand for limited resources, which can strain supply', 'Population growth never affects the demand for resources', 'This concept has no connection to social studies', 'Resources are always unlimited no matter the population size'], 0),
    ('Why do governments and organizations study demographic trends when planning for the future?', ['Understanding population changes helps plan for needs like schools, healthcare, and infrastructure', 'Demographic trends have no use in planning for the future', 'This concept has no relevance to social studies', 'Population data is never used for any kind of planning'], 0)]),
]),

day(96, [
L('Reading: Analyzing Character Motivation',
  'Grade 6 Language strand: character motivation refers to the reasons behind a character’s actions and decisions in a story, which readers can infer from the character’s words, thoughts, and behaviour.',
  [('What does character motivation refer to?', ['The reasons behind a character’s actions and decisions', 'The setting where a story takes place', 'A concept unrelated to reading', 'The title of a story'], 0),
   ('Can readers infer a character’s motivation from their words and actions?', ['Yes', 'No, motivation can never be inferred from a story', 'A concept unrelated to character motivation', 'Only the author can ever know a character’s motivation'], 0),
   ('Why might understanding a character’s motivation help readers predict what they will do next?', ['Knowing what a character wants can help explain and anticipate their future choices', 'Character motivation never affects a character’s future choices', 'This concept has no connection to reading comprehension', 'Predicting a character’s actions never requires understanding motivation'], 0),
   ('If a character steals food because their family is starving, what might this reveal about their motivation?', ['They are acting out of desperation to help their family survive', 'They have no reason at all for their actions', 'This concept has no connection to character motivation', 'The character is acting purely for entertainment'], 0),
   ('Why might two characters react differently to the same event in a story?', ['Each character may have different motivations, values, or experiences shaping their response', 'All characters always react in exactly the same way to any event', 'This concept has no relevance to reading comprehension', 'A character’s motivation never influences how they react to events'], 0)]),
M('Measurement: Converting Between Units of Capacity and Mass',
  'Grade 6 Math strand: converting between units of capacity, such as millilitres and litres, and units of mass, such as grams and kilograms, requires multiplying or dividing by powers of ten, since the metric system is based on tens.',
  [('How many millilitres are in 1 litre?', ['1000', '100', '10', '10000'], 0),
   ('How many grams are in 1 kilogram?', ['1000', '100', '10', '10000'], 0),
   ('To convert from litres to millilitres, do you multiply or divide?', ['Multiply', 'Divide', 'A concept unrelated to unit conversion', 'Neither multiply nor divide'], 0),
   ('If a bottle holds 2 litres of water, how many millilitres does it hold?', ['2000 millilitres', '200 millilitres', '20 millilitres', '20000 millilitres'], 0),
   ('Why is it useful to be able to convert between units like grams and kilograms in everyday life, such as cooking?', ['Recipes and packaging often use different units, so conversion helps measure ingredients accurately', 'Unit conversion never applies to everyday tasks like cooking', 'This concept has no connection to math', 'Every recipe always uses the exact same unit of measurement'], 0)]),
Sc('Science: Camouflage and Mimicry as Survival Adaptations',
   'Grade 6 Science strand: camouflage allows an animal to blend into its surroundings to avoid predators or sneak up on prey, while mimicry occurs when one species evolves to resemble another, often to gain protection.',
   [('What does camouflage allow an animal to do?', ['Blend into its surroundings', 'Change its species completely', 'A concept unrelated to biology', 'Grow larger than its predators'], 0),
    ('What is mimicry?', ['When one species evolves to resemble another', 'When an animal changes colour permanently', 'A concept unrelated to survival adaptations', 'When a species disappears completely'], 0),
    ('Can camouflage help an animal avoid predators?', ['Yes', 'No, camouflage has no connection to avoiding predators', 'A concept unrelated to camouflage', 'Camouflage only helps an animal find food, never avoid danger'], 0),
    ('Why might a harmless insect evolve to resemble a dangerous or bad-tasting species?', ['Predators may avoid it, mistaking it for the dangerous species it resembles', 'Resembling another species never provides any protection', 'This concept has no connection to biology', 'Mimicry always makes an animal more visible to predators'], 0),
    ('Why are camouflage and mimicry considered examples of adaptations that develop over generations?', ['These traits are gradually shaped by natural selection because they improve survival and reproduction', 'These traits appear instantly in a single animal with no connection to generations', 'This concept has no relevance to science', 'Camouflage and mimicry never provide any survival advantage'], 0)]),
SS('Social Studies: Canada’s National Parks and Conservation History',
   'Grade 6 Social Studies strand: Canada’s national parks system, including Banff, the first national park established in 1885, protects significant natural areas for conservation, recreation, and future generations to enjoy.',
   [('What was Canada’s first national park, established in 1885?', ['Banff', 'A concept unrelated to Canadian geography', 'Algonquin', 'Jasper'], 0),
    ('What is one purpose of Canada’s national parks?', ['Conservation of significant natural areas', 'Only industrial development', 'A concept unrelated to national parks', 'Removing wildlife permanently'], 0),
    ('Are national parks intended to be protected for future generations?', ['Yes', 'No, national parks have no connection to future generations', 'A concept unrelated to conservation', 'National parks are meant to be temporary only'], 0),
    ('Why might governments choose to set aside land as a protected national park instead of allowing it to be developed?', ['Protecting the land can preserve unique ecosystems and natural beauty for the public to enjoy', 'Setting aside protected land never has any environmental benefit', 'This concept has no connection to social studies', 'National parks are never connected to protecting the environment'], 0),
    ('Why might a national park need rules limiting activities like hunting or building?', ['Rules can help protect wildlife and habitats from being damaged or disturbed', 'National parks never need any kind of rules', 'This concept has no relevance to social studies', 'Hunting and building never have any impact on a natural area'], 0)]),
]),

day(97, [
L('Writing: Paraphrasing and Avoiding Plagiarism',
  'Grade 6 Language strand: paraphrasing means restating information from a source in your own words while keeping the original meaning, and is an important skill for avoiding plagiarism, which is presenting someone else’s work as your own.',
  [('What does paraphrasing mean?', ['Restating information from a source in your own words', 'Copying a source word for word with no changes', 'A concept unrelated to writing', 'Deleting information from a source entirely'], 0),
   ('What is plagiarism?', ['Presenting someone else’s work as your own', 'Properly crediting a source for information used', 'A concept unrelated to writing', 'Summarizing a text in your own words with credit given'], 0),
   ('Does paraphrasing require keeping the original meaning of the source?', ['Yes', 'No, paraphrasing always changes the original meaning', 'A concept unrelated to paraphrasing', 'Meaning is never important when paraphrasing'], 0),
   ('Why is paraphrasing considered an important skill for avoiding plagiarism?', ['It allows a writer to use information from a source while expressing it in their own words', 'Paraphrasing never actually helps avoid plagiarism', 'This concept has no connection to writing', 'The only way to avoid plagiarism is to never use any outside sources'], 0),
   ('Why should a writer still credit a source, even after paraphrasing its information?', ['The ideas still originally came from another source and deserve proper credit', 'Paraphrased information never needs to be credited to anyone', 'This concept has no relevance to writing', 'Crediting a source is only necessary when copying it word for word'], 0)]),
M('Data Management: Choosing the Best Graph to Display Data',
  'Grade 6 Math strand: choosing an appropriate graph, such as a bar graph for comparing categories, a line graph for showing change over time, or a circle graph for showing parts of a whole, helps data be communicated clearly.',
  [('Which type of graph is best for comparing categories, such as favourite fruits among students?', ['A bar graph', 'A line graph', 'A concept unrelated to graphs', 'No graph is ever useful for this purpose'], 0),
   ('Which type of graph is best for showing change over time, such as temperature across a week?', ['A line graph', 'A bar graph', 'A concept unrelated to graphs', 'No graph is ever useful for this purpose'], 0),
   ('Which type of graph is best for showing parts of a whole, such as percentages of a budget?', ['A circle graph', 'A line graph', 'A concept unrelated to graphs', 'No graph is ever useful for this purpose'], 0),
   ('Why might choosing the wrong type of graph make data harder to understand?', ['Some graphs are not designed to clearly show certain kinds of patterns or comparisons', 'The type of graph chosen never affects how clearly data is understood', 'This concept has no connection to data management', 'Every type of graph works equally well for any kind of data'], 0),
   ('Why is it important to think about your audience when choosing how to display data?', ['A well-chosen graph can make the data’s message clear and easy for the audience to interpret', 'The audience never affects which graph should be chosen', 'This concept has no relevance to data management', 'Graphs are never meant to communicate information to an audience'], 0)]),
Sc('Science: Igneous, Sedimentary, and Metamorphic Rocks',
   'Grade 6 Science strand: rocks are classified into three types based on how they form: igneous rocks form from cooled magma or lava, sedimentary rocks form from compressed layers of sediment, and metamorphic rocks form when existing rock is changed by heat and pressure.',
   [('How do igneous rocks form?', ['From cooled magma or lava', 'From compressed layers of sediment', 'A concept unrelated to geology', 'From existing rock changed by heat and pressure'], 0),
    ('How do sedimentary rocks form?', ['From compressed layers of sediment', 'From cooled magma or lava', 'A concept unrelated to geology', 'From existing rock changed by heat and pressure'], 0),
    ('How do metamorphic rocks form?', ['From existing rock changed by heat and pressure', 'From cooled magma or lava', 'A concept unrelated to geology', 'From compressed layers of sediment'], 0),
    ('Why might a sedimentary rock sometimes contain visible layers?', ['It forms as sediment is deposited and compressed over time, often in distinct layers', 'Sedimentary rocks never contain any layers', 'This concept has no connection to geology', 'Layers only ever appear in igneous rocks'], 0),
    ('Why do geologists study the type of rock found in a region?', ['The rock type can reveal information about the area’s geological history and processes', 'The type of rock found in a region never reveals any useful information', 'This concept has no relevance to science', 'All rocks are identical no matter how or where they formed'], 0)]),
SS('Social Studies: The Spread of World Religions Through Trade and Migration',
   'Grade 6 Social Studies strand: major world religions, such as Buddhism, Christianity, and Islam, spread to new regions over centuries through trade routes, migration, and cultural exchange, shaping societies far from where each religion began.',
   [('Name one way that world religions have historically spread to new regions.', ['Trade routes', 'A concept unrelated to religious history', 'Religions have never spread anywhere', 'Only through modern air travel'], 0),
    ('Did trade routes play a role in spreading religions like Buddhism and Islam?', ['Yes', 'No, trade routes never had any connection to religion', 'A concept unrelated to world religions', 'Religions have only ever spread within a single region'], 0),
    ('Can migration contribute to the spread of a religion to a new area?', ['Yes', 'No, migration never spreads religious beliefs', 'A concept unrelated to migration', 'Religions can only be spread through conquest'], 0),
    ('Why might merchants travelling along trade routes have helped spread religious beliefs to new regions?', ['As they traded goods, they also shared ideas, customs, and beliefs with the people they met', 'Merchants only ever traded goods with no exchange of ideas', 'This concept has no connection to social studies', 'Trade routes were only ever used to transport food'], 0),
    ('Why is understanding the spread of world religions helpful for understanding global cultures today?', ['Many modern societies were shaped by religious traditions that arrived through historical trade and migration', 'World religions have no connection to any modern society', 'This concept has no relevance to social studies', 'Religious beliefs never had any influence on culture'], 0)]),
]),

day(98, [
L('Reading: Myths and Legends Across Cultures',
  'Grade 6 Language strand: myths are traditional stories, often involving gods or supernatural events, used to explain the natural world or cultural beliefs, while legends are stories based on real people or events that have grown to include exaggerated details.',
  [('What is a myth?', ['A traditional story often involving gods or supernatural events', 'A factual news report', 'A concept unrelated to reading', 'A type of scientific textbook'], 0),
   ('What is a legend?', ['A story based on real people or events that has grown to include exaggerated details', 'A story with absolutely no connection to real events', 'A concept unrelated to reading', 'A type of grammar rule'], 0),
   ('Are myths and legends found across many different cultures around the world?', ['Yes', 'No, only one single culture has ever created any myths', 'A concept unrelated to myths and legends', 'Myths and legends only exist in modern stories'], 0),
   ('Why might ancient cultures have used myths to explain natural events, like thunderstorms?', ['Myths offered an understandable explanation for events that were not yet scientifically understood', 'Myths never attempted to explain any natural events', 'This concept has no connection to reading comprehension', 'Ancient cultures never told any kind of story'], 0),
   ('Why might comparing myths and legends from different cultures reveal shared human values?', ['Many cultures create stories that reflect similar hopes, fears, or lessons despite being separate from one another', 'Myths and legends from different cultures never share anything in common', 'This concept has no relevance to reading comprehension', 'Every culture’s stories are always completely unrelated in theme'], 0)]),
M('Patterning and Algebra: Line Graphs and Analyzing Trends Over Time',
  'Grade 6 Math strand: a line graph shows how a quantity changes over time, and analyzing its trend, whether it is increasing, decreasing, or staying steady, helps identify patterns in the data.',
  [('What does a line graph typically show?', ['How a quantity changes over time', 'Only a single number with no time element', 'A concept unrelated to graphs', 'The colours of different categories'], 0),
   ('If a line graph is sloping upward from left to right, what trend does this show?', ['An increasing trend', 'A decreasing trend', 'A concept unrelated to line graphs', 'No trend at all'], 0),
   ('If a line graph is sloping downward from left to right, what trend does this show?', ['A decreasing trend', 'An increasing trend', 'A concept unrelated to line graphs', 'No trend at all'], 0),
   ('If a line graph stays flat over a period of time, what does this suggest about the data?', ['The quantity stayed roughly steady during that period', 'The quantity increased dramatically during that period', 'A concept unrelated to line graphs', 'The quantity decreased dramatically during that period'], 0),
   ('Why might a scientist use a line graph to track data like daily temperature over a month?', ['It makes it easy to visually identify trends and changes in the data over time', 'Line graphs never help identify any trends in data', 'This concept has no connection to math', 'Temperature data can never be tracked using a graph'], 0)]),
Sc('Science: Wind Energy and Turbine Design',
   'Grade 6 Science strand: wind turbines convert the kinetic energy of moving air into electricity, using blades shaped to spin efficiently and a generator that transforms this spinning motion into usable electrical power.',
   [('What do wind turbines convert into electricity?', ['The kinetic energy of moving air', 'The heat energy of sunlight', 'A concept unrelated to renewable energy', 'The chemical energy of coal'], 0),
    ('What part of a wind turbine transforms spinning motion into electrical power?', ['The generator', 'The blades alone, with no other part needed', 'A concept unrelated to wind turbines', 'The tower foundation'], 0),
    ('Are wind turbine blades specially shaped to help them spin efficiently?', ['Yes', 'No, the shape of the blades has no effect on efficiency', 'A concept unrelated to turbine design', 'Blades are always shaped like perfect squares'], 0),
    ('Why might wind turbines be placed in open areas with strong, consistent winds?', ['Stronger and steadier wind allows turbines to generate more electricity efficiently', 'Wind speed has no effect on how much electricity a turbine generates', 'This concept has no connection to renewable energy', 'Wind turbines work equally well in areas with no wind at all'], 0),
    ('Why is wind energy considered a renewable resource?', ['Wind is naturally and continuously produced by weather patterns, so it does not run out', 'Wind energy relies on a limited resource that will eventually run out', 'This concept has no relevance to science', 'Wind energy has no connection to renewable resources'], 0)]),
SS('Social Studies: The Role of Non-Governmental Organizations in Global Aid',
   'Grade 6 Social Studies strand: non-governmental organizations, or NGOs, are independent groups that work to provide aid, support development, or advocate for causes such as health, education, or human rights around the world.',
   [('What does NGO stand for?', ['Non-governmental organization', 'National Government Office', 'A concept unrelated to global aid', 'New Global Organization'], 0),
    ('Are NGOs typically run by governments or independent of them?', ['Independent of governments', 'Directly run by governments', 'A concept unrelated to NGOs', 'NGOs do not exist anywhere'], 0),
    ('Name one cause an NGO might work to support, such as health or education.', ['Health', 'A concept unrelated to NGOs', 'Only entertainment', 'Only sports competitions'], 0),
    ('Why might an NGO be able to respond quickly to a crisis, such as a natural disaster, in another country?', ['Many NGOs are organized specifically to mobilize resources and volunteers for urgent humanitarian needs', 'NGOs never respond to any kind of crisis', 'This concept has no connection to social studies', 'Only national governments are ever allowed to help during a crisis'], 0),
    ('Why might NGOs work alongside governments rather than replacing them entirely?', ['Governments and NGOs can each bring different resources and strengths to addressing a problem', 'NGOs and governments never work together on anything', 'This concept has no relevance to social studies', 'NGOs always operate completely independently with no cooperation from anyone'], 0)]),
]),

day(99, [
L('Grammar: Formal and Informal Register',
  'Grade 6 Language strand: register refers to the level of formality in language, with formal register used in situations like essays or speeches to a large audience, and informal register used in casual conversations with friends.',
  [('What does register refer to in language?', ['The level of formality in language', 'The number of words in a sentence', 'A concept unrelated to grammar', 'The topic of a piece of writing'], 0),
   ('Which register would most likely be used in a formal essay?', ['Formal register', 'Informal register', 'A concept unrelated to register', 'Neither formal nor informal register'], 0),
   ('Which register would most likely be used in a text message to a close friend?', ['Informal register', 'Formal register', 'A concept unrelated to register', 'Neither formal nor informal register'], 0),
   ('Which sentence uses a more formal register?', ['I would like to request additional information regarding this matter.', 'Hey, can you fill me in on this?', 'What’s up with this thing?', 'Gimme the details, please.'], 0),
   ('Why is it important to choose the appropriate register for a given audience and purpose?', ['Using the right level of formality helps communicate effectively and appropriately for the situation', 'Register never affects how a message is received by an audience', 'This concept has no connection to grammar', 'The same exact register should always be used in every situation'], 0)]),
M('Patterning and Algebra: Representing Patterns with Tables, Graphs, and Expressions',
  'Grade 6 Math strand: a pattern can be represented in multiple ways, using a table of values, a graph, or an algebraic expression, and being able to move between these representations builds a deeper understanding of the relationship.',
  [('Name one way a pattern can be represented, besides a list of numbers.', ['A table of values', 'A concept unrelated to patterning', 'A grocery list', 'A dictionary definition'], 0),
   ('If a pattern increases by 3 each time starting at 2, what is the algebraic expression for the nth term, using n starting at 1?', ['3n minus 1', '3n plus 1', 'n plus 3', '3n'], 0),
   ('Using the expression 3n minus 1, what is the value of the pattern when n equals 4?', ['11', '12', '9', '13'], 0),
   ('Why might representing a pattern as a graph be helpful, in addition to a table of values?', ['A graph can visually show how quickly or in what way the pattern is changing', 'Graphs never provide any additional information about a pattern', 'This concept has no connection to math', 'A table and a graph always show completely different information'], 0),
   ('Why is it useful to be able to write an algebraic expression for a pattern instead of only listing terms?', ['An expression allows you to quickly calculate any term in the pattern without listing every value', 'Algebraic expressions never help with finding pattern terms', 'This concept has no connection to patterning', 'Listing every term is always faster than using an expression'], 0)]),
Sc('Science: Biomimicry: Nature-Inspired Technology and Design',
   'Grade 6 Science strand: biomimicry is the practice of studying nature’s designs, such as how a bird’s wing or a shark’s skin works, and applying those ideas to solve human engineering and design challenges.',
   [('What is biomimicry?', ['The practice of studying nature’s designs to solve human engineering challenges', 'A process of creating entirely artificial materials with no natural inspiration', 'A concept unrelated to science', 'A method of destroying natural habitats for research'], 0),
    ('Name one natural feature that has inspired human technology, such as a bird’s wing.', ['A bird’s wing', 'A concept unrelated to biomimicry', 'A brick wall', 'A plastic bottle'], 0),
    ('Does biomimicry involve studying how living things solve problems in nature?', ['Yes', 'No, biomimicry has no connection to living things', 'A concept unrelated to biomimicry', 'Biomimicry only studies non-living objects'], 0),
    ('Why might engineers study how a shark’s skin reduces drag in water?', ['This natural design could inspire more efficient materials for swimsuits or ship hulls', 'A shark’s skin has no possible engineering application', 'This concept has no connection to biomimicry', 'Sharks have no unique physical features worth studying'], 0),
    ('Why might biomimicry be considered a valuable approach for solving modern design challenges?', ['Nature has developed efficient solutions to many problems over millions of years of evolution', 'Nature has never developed any efficient solutions to any problem', 'This concept has no relevance to science', 'Human-made designs are always better than anything found in nature'], 0)]),
SS('Social Studies: Canada’s Role in International Development and Foreign Aid',
   'Grade 6 Social Studies strand: Canada provides international development assistance and foreign aid to support other countries with challenges such as poverty, education, and health care, often working with international partners.',
   [('What is one purpose of Canada’s international development assistance?', ['To support other countries facing challenges like poverty or health care needs', 'To prevent any country from receiving help', 'A concept unrelated to Canadian foreign policy', 'To increase poverty in other countries'], 0),
    ('Does Canada often work with international partners when providing foreign aid?', ['Yes', 'No, Canada never works with any other countries or organizations', 'A concept unrelated to foreign aid', 'Canada only provides aid within its own borders'], 0),
    ('Name one challenge that foreign aid might help address, such as poverty or education.', ['Poverty', 'A concept unrelated to foreign aid', 'Weather patterns', 'Space exploration'], 0),
    ('Why might Canada choose to provide foreign aid to countries facing a humanitarian crisis?', ['Supporting other nations in times of need can save lives and reflects a commitment to global cooperation', 'Foreign aid never actually helps any country in need', 'This concept has no connection to social studies', 'Canada has no reason to ever help another country'], 0),
    ('Why might critics debate how foreign aid should be spent or distributed?', ['People may have different views on which approaches most effectively and fairly help those in need', 'No one has ever debated how foreign aid should be used', 'This concept has no relevance to social studies', 'Foreign aid is always spent in exactly the same way in every situation'], 0)]),
]),

day(100, [
L('Review: Irony, Grammar, Speeches, and Media Literacy (Days 91-99)',
  'Grade 6 Language strand review: students revisit irony, gerunds and infinitives, persuasive speeches, hyperbole and understatement, propaganda techniques, character motivation, paraphrasing, myths and legends, and formal versus informal register.',
  [('What is irony?', ['A gap between what is expected and what actually happens', 'A concept unrelated to reading', 'A type of punctuation mark', 'A synonym for a simile'], 0),
   ('What is a gerund?', ['A verb form ending in -ing that acts as a noun', 'A concept unrelated to grammar', 'A word that describes a noun', 'A punctuation mark'], 0),
   ('What is the main goal of a persuasive speech?', ['To convince a live audience to agree with a viewpoint or take action', 'To simply describe an event with no opinion', 'A concept unrelated to writing', 'To entertain an audience with no message at all'], 0),
   ('What does paraphrasing mean?', ['Restating information from a source in your own words', 'Copying a source word for word with no changes', 'A concept unrelated to writing', 'Deleting information from a source entirely'], 0),
   ('What does register refer to in language?', ['The level of formality in language', 'The number of words in a sentence', 'A concept unrelated to grammar', 'The topic of a piece of writing'], 0)]),
M('Review: Integers, Data, Geometry, and Patterning (Days 91-99)',
  'Grade 6 Math strand review: students revisit adding and subtracting integers, box-and-whisker plots, congruent figures, sales tax, independent and dependent events, unit conversion, choosing graphs, line graphs, and representing patterns.',
  [('What is negative 3 plus 5?', ['2', '-2', '8', '-8'], 0),
   ('What does a box-and-whisker plot display?', ['How data is spread out', 'Only the mean of a data set', 'A concept unrelated to data management', 'Nothing about a data set'], 0),
   ('What does it mean for two figures to be congruent?', ['They are exactly the same size and shape', 'They are the same shape but different sizes', 'A concept unrelated to geometry', 'They share only one matching side'], 0),
   ('What is an independent event?', ['An event whose outcome does not affect another event', 'An event that always affects another event', 'A concept unrelated to probability', 'An event that never has any outcome'], 0),
   ('What does a line graph typically show?', ['How a quantity changes over time', 'Only a single number with no time element', 'A concept unrelated to graphs', 'The colours of different categories'], 0)]),
Sc('Review: Body Systems, Biomes, and Sustainability (Days 91-99)',
   'Grade 6 Science strand review: students revisit the endocrine system, world biomes, extinction and endangered species, the excretory system, recycling, camouflage and mimicry, rock types, wind energy, and biomimicry.',
   [('What does the endocrine system release into the body?', ['Hormones', 'Only blood cells', 'A concept unrelated to the human body', 'Only oxygen'], 0),
    ('What is a biome?', ['A large region with a distinct climate, plants, and animals', 'A single type of rock', 'A concept unrelated to Earth science', 'A single species of animal'], 0),
    ('What does extinction mean for a species?', ['It no longer exists anywhere on Earth', 'It has moved to a new habitat', 'A concept unrelated to biology', 'It has grown in population everywhere'], 0),
    ('What do wind turbines convert into electricity?', ['The kinetic energy of moving air', 'The heat energy of sunlight', 'A concept unrelated to renewable energy', 'The chemical energy of coal'], 0),
    ('What is biomimicry?', ['The practice of studying nature’s designs to solve human engineering challenges', 'A process of creating entirely artificial materials with no natural inspiration', 'A concept unrelated to science', 'A method of destroying natural habitats for research'], 0)]),
SS('Review: Canadian Government, Global Heritage, and International Cooperation (Days 91-99)',
   'Grade 6 Social Studies strand review: students revisit the Truth and Reconciliation Commission, UNESCO World Heritage Sites, ancient Nubia, the Canadian Senate, global population growth, national parks, world religions, NGOs, and foreign aid.',
   [('What did the Truth and Reconciliation Commission document?', ['The experiences of Indigenous survivors of residential schools', 'The history of Canadian sports', 'A concept unrelated to Canadian history', 'The founding of Canadian cities'], 0),
    ('What is a UNESCO World Heritage Site?', ['A place recognized for outstanding cultural, historical, or natural significance', 'A place with no historical significance at all', 'A concept unrelated to global heritage', 'A type of modern shopping centre'], 0),
    ('What is the Canadian Senate?', ['The upper house of Parliament', 'A provincial court', 'A concept unrelated to government', 'A municipal council'], 0),
    ('What was Canada’s first national park, established in 1885?', ['Banff', 'A concept unrelated to Canadian geography', 'Algonquin', 'Jasper'], 0),
    ('What does NGO stand for?', ['Non-governmental organization', 'National Government Office', 'A concept unrelated to global aid', 'New Global Organization'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_91_100)
    append_to(6, g6_91_100)
