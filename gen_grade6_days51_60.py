#!/usr/bin/env python3
"""Phase 3 extension: Grade 6, Days 51-60 (first batch past the Day 50
milestone, pushing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-50 set (see
data/grade6.json): connotation/denotation, exponents, density and
buoyancy, and the Industrial Revolution through the Berlin Wall.

Subject keys for Grade 6 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 6 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science & Technology',
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


g6_51_60 = [
day(51, [
L('Reading: Comparing Perspectives Across Genres',
  'Grade 6 Language strand: comparing perspectives across genres means examining how the same topic or event is presented differently in a news article, a poem, a memoir, or a piece of fiction.',
  [('Comparing perspectives across genres means examining how a topic is presented ___.', ['Differently depending on the genre used to present it', 'Identically in every genre, with no variation at all', 'A concept unrelated to reading', 'Only in fictional stories, never in nonfiction'], 0),
   ('How might a news article about a storm differ from a poem about the same storm?', ['The article focuses on facts, while the poem may focus on emotion and imagery', 'They would always be written in exactly the same style', 'A concept unrelated to genre comparison', 'A poem can never be written about a real event'], 0),
   ('Why might a memoir about an event feel different from a textbook account of it?', ['A memoir reflects personal experience and emotion, while a textbook focuses on objective facts', 'Memoirs and textbooks always present information identically', 'A reason unrelated to genre', 'A memoir can never include any factual details'], 0),
   ('Why is it valuable to compare how different genres treat the same topic?', ['It builds a fuller, more nuanced understanding of the topic', 'Comparing genres provides no additional understanding', 'A reason unrelated to reading comprehension', 'Only one genre can ever accurately represent a topic'], 0),
   ('Which genre would most likely present information using persuasive, emotional language?', ['A poem or personal essay', 'A strictly factual news report', 'A concept unrelated to genre', 'A dictionary entry'], 0)]),
M('Exponents and Powers',
  'Grade 6 Math strand: an exponent shows how many times a base number is multiplied by itself, such as 2³ meaning 2 × 2 × 2.',
  [('An exponent shows ___.', ['How many times a base number is multiplied by itself', 'How many times a number is added to itself', 'A concept unrelated to exponents', 'The number of digits in a value'], 0),
   ('What is 2³?', ['8', '6', 'A value unrelated to the calculation', '9'], 0),
   ('What is 5²?', ['25', '10', 'A value unrelated to the calculation', '52'], 0),
   ('In the expression 4², what is the base and what is the exponent?', ['4 is the base and 2 is the exponent', '2 is the base and 4 is the exponent', 'A description unrelated to the expression', 'There is no base or exponent in this expression'], 0),
   ('What is 3⁴?', ['81', '12', 'A value unrelated to the calculation', '34'], 0)]),
Sc('Density and Buoyancy',
   'Grade 6 Science strand: density describes how much mass is packed into a given volume, and buoyancy explains why some objects float while others sink in a fluid.',
   [('Density describes ___.', ['How much mass is packed into a given volume', 'The colour of an object', 'A concept unrelated to density', 'How heavy an object feels when held'], 0),
    ('An object will float in water if its density is ___ the density of water.', ['Less than', 'Greater than', 'A comparison unrelated to density', 'Exactly double'], 0),
    ('Why does a large ship made of steel float, even though steel is denser than water?', ['Its overall shape displaces enough water to make its average density lower than water', 'Steel always floats, regardless of shape', 'A reason unrelated to buoyancy', 'Ships are not actually denser than water in any way'], 0),
    ('Buoyancy is best described as ___.', ['The upward force a fluid exerts on an object', 'The downward force of gravity alone', 'A concept unrelated to fluids', 'The temperature of a liquid'], 0),
    ('Why might a helium balloon rise into the air?', ['Helium is less dense than the surrounding air', 'Helium is denser than the surrounding air', 'A reason unrelated to density', 'Balloons rise due to their colour'], 0)]),
SS('The Industrial Revolution: Causes and Effects',
   'Grade 6 Social Studies strand: the Industrial Revolution was a period of rapid technological and economic change, beginning in the late 1700s, that transformed how goods were produced and how people lived and worked.',
   [('The Industrial Revolution brought major changes to how ___.', ['Goods were produced and how people lived and worked', 'Ancient civilizations first began, thousands of years earlier', 'A concept unrelated to this historical period', 'Countries interacted before any trade existed'], 0),
    ('Which of these was a major effect of the Industrial Revolution?', ['The growth of factories and cities', 'The complete disappearance of all cities', 'A concept unrelated to the Industrial Revolution', 'A return to purely agricultural societies with no factories'], 0),
    ('New machines and factories during the Industrial Revolution changed work by ___.', ['Making production faster and often moving it away from homes and farms', 'Having no effect on how goods were produced', 'A reason unrelated to this period', 'Making handcrafted goods more common than ever before'], 0),
    ('Which of these might be considered a negative effect of the Industrial Revolution?', ['Difficult working conditions in early factories', 'An increase in leisure time for every single worker', 'A concept unrelated to this period', 'A decrease in the population of cities'], 0),
    ('Why do historians consider the Industrial Revolution a major turning point?', ['It fundamentally changed economies, technology, and daily life for many people', 'It had no lasting effect on how societies developed', 'A reason unrelated to its historical significance', 'It only affected a single small village with no wider impact'], 0)])]),
day(52, [
L('Grammar: Active Voice vs Passive Voice',
  'Grade 6 Language strand: in active voice, the subject performs the action (“The dog chased the ball”), while in passive voice, the subject receives the action (“The ball was chased by the dog”).',
  [('In active voice, the subject ___.', ['Performs the action', 'Receives the action', 'A concept unrelated to active voice', 'Is always left out of the sentence'], 0),
   ('In passive voice, the subject ___.', ['Receives the action', 'Performs the action', 'A concept unrelated to passive voice', 'Is always the one doing the action'], 0),
   ('Which sentence is written in active voice?', ['The chef cooked the meal.', 'The meal was cooked by the chef.', 'A sentence unrelated to voice', 'The meal, cooked by the chef, sat on the table.'], 0),
   ('Which sentence is written in passive voice?', ['The trophy was won by the team.', 'The team won the trophy.', 'A sentence unrelated to voice', 'The team is winning the trophy.'], 0),
   ('Why might a writer choose active voice over passive voice?', ['Active voice is often clearer and more direct', 'Passive voice is always clearer than active voice', 'A reason unrelated to grammar', 'Active voice is never appropriate in formal writing'], 0)]),
M('Square Roots and Perfect Squares',
  'Grade 6 Math strand: a perfect square is the product of a whole number multiplied by itself, and its square root is the number that produces that product.',
  [('A perfect square is the result of ___.', ['A whole number multiplied by itself', 'A whole number divided by itself', 'A concept unrelated to perfect squares', 'Any two different numbers added together'], 0),
   ('What is the square root of 25?', ['5', '10', 'A value unrelated to the calculation', '25'], 0),
   ('What is the square root of 49?', ['7', '14', 'A value unrelated to the calculation', '9'], 0),
   ('Which of these is a perfect square?', ['36', '20', 'A number unrelated to perfect squares', '15'], 0),
   ('What is the square root of 81?', ['9', '18', 'A value unrelated to the calculation', '8'], 0)]),
Sc('Acids, Bases, and pH',
   'Grade 6 Science strand: acids and bases are types of chemical substances measured on the pH scale, where lower numbers indicate acids, higher numbers indicate bases, and 7 is neutral.',
   [('On the pH scale, a substance with a pH below 7 is considered ___.', ['An acid', 'A base', 'A term unrelated to the pH scale', 'Neutral'], 0),
    ('On the pH scale, a substance with a pH above 7 is considered ___.', ['A base', 'An acid', 'A term unrelated to the pH scale', 'Neutral'], 0),
    ('A substance with a pH of exactly 7 is considered ___.', ['Neutral', 'A strong acid', 'A term unrelated to the pH scale', 'A strong base'], 0),
    ('Which of these is an example of an acidic substance?', ['Lemon juice', 'Pure water', 'A substance unrelated to the pH scale', 'Baking soda'], 0),
    ('Why is it useful to know the pH of a substance?', ['It helps identify whether the substance is acidic, basic, or neutral, and how it may react with other materials', 'The pH scale provides no useful information about a substance', 'A reason unrelated to chemistry', 'pH only applies to solid substances, never liquids'], 0)]),
SS('Canada’s Role in NATO and International Alliances',
   'Grade 6 Social Studies strand: Canada is a founding member of NATO, an alliance of countries that agree to support one another for collective defence and international security.',
   [('NATO is an alliance of countries that agree to ___.', ['Support one another for collective defence and security', 'Never cooperate with one another on any issue', 'A concept unrelated to international alliances', 'Compete against each other militarily'], 0),
    ('Canada’s role in NATO is best described as ___.', ['A founding member that participates in collective defence efforts', 'A country with no connection to NATO at all', 'A concept unrelated to Canada’s foreign policy', 'A country that has never joined any international alliance'], 0),
    ('Why might countries choose to join an alliance like NATO?', ['To strengthen their collective security and support one another if needed', 'Joining an alliance provides no security benefits', 'A reason unrelated to international relations', 'Alliances are formed with no purpose or benefit at all'], 0),
    ('Which of these best describes the idea of “collective defence”?', ['An attack on one member is treated as an attack on all members', 'Each country must defend itself with no support from others', 'A concept unrelated to alliances', 'Only the largest country in an alliance provides any defence'], 0),
    ('Why is it useful to learn about Canada’s international alliances?', ['It helps explain Canada’s role and responsibilities in global security', 'Canada’s international alliances have no effect on its foreign policy', 'A reason unrelated to social studies learning', 'Canada operates independently with no international partnerships'], 0)])]),
day(53, [
L('Writing: Writing a Feature Article',
  'Grade 6 Language strand: a feature article explores a topic in depth, often combining facts, interviews, and storytelling to engage readers beyond a simple news report.',
  [('A feature article is different from a basic news report because it ___.', ['Explores a topic in more depth, often blending facts and storytelling', 'Only reports the most basic facts with no additional detail', 'A concept unrelated to writing', 'Never includes any factual information at all'], 0),
   ('Which is an example of a technique used in a feature article?', ['Including a quote from an interview with someone connected to the topic', 'Listing only statistics with no context or storytelling', 'A concept unrelated to feature articles', 'Avoiding any research on the topic'], 0),
   ('Why might a feature article include a personal story related to its topic?', ['To make the topic feel more engaging and relatable to readers', 'Personal stories are never included in feature articles', 'A reason unrelated to feature writing', 'To confuse readers about the article’s main topic'], 0),
   ('What might a strong feature article headline do?', ['Capture attention while giving a sense of the article’s focus', 'Have no connection to the article’s content at all', 'A concept unrelated to headlines', 'Always be written as a single word'], 0),
   ('Why do feature articles often take longer to research than a short news brief?', ['They typically require deeper investigation, interviews, and context', 'Feature articles require no research at all', 'A reason unrelated to feature writing', 'They are always shorter than a typical news brief'], 0)]),
M('Solving Inequalities',
  'Grade 6 Math strand: an inequality compares two values using symbols like < or >, and solving one shows the range of values that make the statement true.',
  [('An inequality compares two values using symbols such as ___.', ['< or >', '= only', 'A symbol unrelated to inequalities', '+ or -'], 0),
   ('If x > 3, which of these values could be a solution?', ['5', '2', 'A value unrelated to the inequality', '3'], 0),
   ('If x < 6, which of these values could be a solution?', ['4', '7', 'A value unrelated to the inequality', '6'], 0),
   ('Solve for x: x + 2 > 7.', ['x > 5', 'x > 9', 'A solution unrelated to the inequality', 'x > 2'], 0),
   ('Why might inequalities be useful in real life?', ['They can represent situations with a range of possible values, like a budget limit', 'Inequalities have no real-world use', 'A reason unrelated to inequalities', 'They can only represent one exact value, never a range'], 0)]),
Sc('Erosion and Weathering: Shaping the Land',
   'Grade 6 Science strand: weathering breaks down rock into smaller pieces, while erosion moves those pieces from one place to another, together shaping landforms over time.',
   [('Weathering is the process of ___.', ['Breaking down rock into smaller pieces', 'Moving broken rock pieces from one place to another', 'A process unrelated to weathering', 'Building up new rock formations from nothing'], 0),
    ('Erosion is the process of ___.', ['Moving broken-down rock pieces from one place to another', 'Breaking rock down into smaller pieces in place', 'A process unrelated to erosion', 'Preventing any movement of rock or soil'], 0),
    ('Which of these is an example of a cause of erosion?', ['Wind and flowing water', 'A rock sitting completely still with no forces acting on it', 'A process unrelated to erosion', 'A rock’s colour changing over time'], 0),
    ('Why might a river canyon form over thousands of years?', ['Flowing water gradually erodes and carves away rock and soil', 'Canyons form instantly, with no gradual process involved', 'A reason unrelated to erosion', 'Rivers have no effect on the land around them'], 0),
    ('Why is it useful to understand weathering and erosion together?', ['They work together to shape many of the landforms we see today', 'These two processes have no connection to one another', 'A reason unrelated to science', 'Landforms are never affected by weathering or erosion'], 0)]),
SS('The Rise and Fall of the Ottoman Empire',
   'Grade 6 Social Studies strand: the Ottoman Empire was a powerful state that lasted for centuries, controlling large parts of the Middle East, North Africa, and southeastern Europe before its eventual decline.',
   [('The Ottoman Empire controlled large parts of ___.', ['The Middle East, North Africa, and southeastern Europe', 'Only a single small city with no wider territory', 'A region unrelated to the Ottoman Empire', 'Only North America'], 0),
    ('The Ottoman Empire lasted for ___.', ['Several centuries', 'Only a few days', 'A length of time unrelated to the Ottoman Empire', 'Less than one year'], 0),
    ('Which of these contributed to the eventual decline of the Ottoman Empire?', ['Internal struggles and pressure from rival powers over time', 'The empire never faced any challenges throughout its history', 'A reason unrelated to the Ottoman Empire', 'A sudden disappearance with no historical cause'], 0),
    ('Why is the Ottoman Empire an important part of world history to study?', ['It shaped politics, trade, and culture across a vast region for centuries', 'It had no influence on the regions it controlled', 'A reason unrelated to its historical significance', 'It existed for too short a time to have any lasting impact'], 0),
    ('Which of these was a significant city within the Ottoman Empire?', ['Constantinople (Istanbul)', 'A city unrelated to the Ottoman Empire', 'A city that has never existed', 'A city located only in South America'], 0)])]),
day(54, [
L('Vocabulary: Connotation and Denotation',
  'Grade 6 Language strand: denotation is a word’s literal dictionary meaning, while connotation is the emotional or cultural association a word carries beyond its literal definition.',
  [('Denotation refers to ___.', ['A word’s literal dictionary meaning', 'The emotional feeling a word creates', 'A concept unrelated to vocabulary', 'The number of syllables in a word'], 0),
   ('Connotation refers to ___.', ['The emotional or cultural association a word carries', 'A word’s exact literal dictionary meaning only', 'A concept unrelated to vocabulary', 'The spelling pattern of a word'], 0),
   ('Which word has a more positive connotation than “cheap”?', ['Affordable', 'Stingy', 'A word unrelated to positive connotation', 'Worthless'], 0),
   ('The words “childish” and “youthful” have similar denotations but different ___.', ['Connotations', 'Spellings', 'A concept unrelated to word meaning', 'Pronunciations'], 0),
   ('Why is understanding connotation important for a writer?', ['It helps convey the right tone and feeling through careful word choice', 'Connotation has no effect on how a reader interprets a word', 'A reason unrelated to writing', 'Connotation only matters when writing dictionaries'], 0)]),
M('Scale Drawings and Similar Figures',
  'Grade 6 Math strand: similar figures have the same shape but different sizes, and a scale drawing uses a consistent ratio to represent a real object at a different size.',
  [('Similar figures have ___.', ['The same shape but different sizes', 'The same size but different shapes', 'A concept unrelated to similar figures', 'No relationship to one another at all'], 0),
   ('In similar figures, corresponding side lengths are ___.', ['Proportional to one another', 'Always exactly equal', 'A relationship unrelated to similar figures', 'Never related in any way'], 0),
   ('If a scale drawing uses a ratio of 1:50, one unit on the drawing represents ___ units in real life.', ['50', '1', 'A number unrelated to the scale', '5'], 0),
   ('If a rectangle with sides 2 and 4 is enlarged by a scale factor of 3, what are the new side lengths?', ['6 and 12', '5 and 7', 'Dimensions unrelated to the calculation', '4 and 8'], 0),
   ('Why are similar figures useful in fields like architecture?', ['They allow designs to be scaled up or down while keeping proportions accurate', 'Similar figures have no practical use in design', 'A reason unrelated to similar figures', 'They only apply to shapes with exactly the same size'], 0)]),
Sc('The Skeletal and Muscular Systems',
   'Grade 6 Science strand: the skeletal system provides structure and protection for the body, while the muscular system works with it to allow movement.',
   [('The skeletal system’s main functions include ___.', ['Providing structure and protecting internal organs', 'Digesting food for energy', 'A function unrelated to the skeletal system', 'Pumping blood throughout the body'], 0),
    ('The muscular system works with the skeletal system to ___.', ['Allow movement of the body', 'Filter waste from the blood', 'A function unrelated to the muscular system', 'Produce hormones for the body'], 0),
    ('Which is an example of a bone protecting an internal organ?', ['The ribcage protecting the heart and lungs', 'A muscle protecting the skin', 'A concept unrelated to the skeletal system', 'A bone with no protective function at all'], 0),
    ('How do muscles typically work in pairs to create movement?', ['One muscle contracts while the opposing muscle relaxes', 'Both muscles always contract at exactly the same time', 'A description unrelated to how muscles work', 'Muscles never work together in pairs'], 0),
    ('Why do the skeletal and muscular systems need to work together?', ['Bones provide the structure that muscles pull against to create movement', 'These two systems have no connection to one another', 'A reason unrelated to body systems', 'Movement occurs with no involvement from bones or muscles'], 0)]),
SS('Women’s Suffrage Movements Around the World',
   'Grade 6 Social Studies strand: women’s suffrage movements were organized efforts, occurring in many countries during the 19th and 20th centuries, to win women the right to vote.',
   [('Women’s suffrage movements worked to secure ___.', ['The right for women to vote', 'The right for men to vote for the first time', 'A concept unrelated to suffrage movements', 'A ban on all future elections'], 0),
    ('Suffrage movements were active in ___.', ['Many countries during the 19th and 20th centuries', 'Only a single country, with no movement elsewhere', 'A time period unrelated to suffrage movements', 'Only during ancient times, thousands of years ago'], 0),
    ('Why might suffragists have organized marches and public campaigns?', ['To raise awareness and pressure governments to grant women voting rights', 'Public campaigns never played a role in suffrage movements', 'A reason unrelated to suffrage movements', 'To prevent women from ever gaining the right to vote'], 0),
    ('Why is the history of women’s suffrage still studied today?', ['It highlights an important step toward greater equality and civic participation', 'This history has no connection to rights and equality today', 'A reason unrelated to social studies learning', 'Suffrage movements had no lasting impact on society'], 0),
    ('Which of these best describes the overall goal of suffrage movements?', ['Expanding voting rights to include women', 'Removing voting rights from all citizens', 'A concept unrelated to suffrage movements', 'Limiting who could run for political office'], 0)])]),
day(55, [
L('Reading: Analyzing Symbolism in Literature',
  'Grade 6 Language strand: symbolism is when an author uses an object, character, or image to represent a deeper idea or meaning beyond its literal sense.',
  [('Symbolism is when an author uses something to ___.', ['Represent a deeper idea or meaning', 'Describe only its literal, surface-level meaning', 'A concept unrelated to literature', 'Confuse the reader with no real purpose'], 0),
   ('In many stories, a dove is often used to symbolize ___.', ['Peace', 'Conflict', 'A concept unrelated to common symbols', 'Confusion'], 0),
   ('Why might an author use symbolism instead of stating an idea directly?', ['It can add depth and invite readers to think more deeply about a text', 'Symbolism never adds meaning to a story', 'A reason unrelated to symbolism', 'Authors are required to always state ideas directly'], 0),
   ('Which is an example of symbolism in a story?', ['A wilting flower representing a character’s fading hope', 'A character simply describing the weather', 'A concept unrelated to symbolism', 'A list of ingredients in a recipe'], 0),
   ('Why might different readers interpret a symbol differently?', ['Symbols can carry different meanings depending on a reader’s own experiences and perspective', 'Every reader is required to interpret a symbol in exactly the same way', 'A reason unrelated to symbolism', 'Symbols always have only one possible meaning'], 0)]),
M('Volume and Surface Area of Composite Shapes',
  'Grade 6 Math strand: a composite shape is made up of two or more simple shapes combined, and finding its volume or surface area involves calculating each part separately and combining the results.',
  [('A composite shape is made up of ___.', ['Two or more simple shapes combined', 'Only a single, simple shape', 'A concept unrelated to composite shapes', 'A shape with no measurable dimensions'], 0),
   ('To find the volume of a composite shape, you generally ___.', ['Calculate the volume of each part separately and add them together', 'Multiply only the largest dimension by itself', 'A method unrelated to composite shapes', 'Ignore all but one part of the shape'], 0),
   ('If a composite shape is made of a rectangular prism with volume 20 and a cube with volume 8, what is its total volume?', ['28', '12', 'A value unrelated to the calculation', '160'], 0),
   ('Why might a real object, like a house, be modelled as a composite shape?', ['Combining simple shapes helps estimate the volume or surface area of complex objects', 'Composite shapes have no real-world application', 'A reason unrelated to composite shapes', 'Real objects can never be broken into simple shapes'], 0),
   ('When finding the surface area of a composite shape, why is it important to check for shared faces?', ['Faces that are joined together are not part of the outer surface and should not be counted', 'Every face should always be counted, whether shared or not', 'A reason unrelated to surface area', 'Shared faces always double the total surface area'], 0)]),
Sc('Energy Transfer and Conservation of Energy',
   'Grade 6 Science strand: energy can transfer between objects and change form, but the law of conservation of energy states that the total amount of energy in a closed system stays the same.',
   [('Energy transfer means energy ___.', ['Moves from one object or place to another', 'Is destroyed completely with no trace', 'A concept unrelated to energy', 'Never moves or changes in any way'], 0),
    ('The law of conservation of energy states that energy ___.', ['Cannot be created or destroyed, only transformed or transferred', 'Is constantly being created out of nothing', 'A concept unrelated to conservation of energy', 'Disappears completely once it is used'], 0),
    ('Which is an example of energy transfer?', ['Heat moving from a hot cup of tea into the surrounding air', 'A rock sitting perfectly still with no changes', 'A concept unrelated to energy transfer', 'An object that has no energy at all'], 0),
    ('When a moving ball hits another ball and transfers motion to it, this demonstrates ___.', ['Energy transfer', 'The destruction of energy', 'A concept unrelated to energy', 'The creation of new energy from nothing'], 0),
    ('Why is the law of conservation of energy important in science?', ['It helps explain how energy moves and changes form without ever disappearing', 'This law has no connection to how energy behaves', 'A reason unrelated to physics', 'Energy is never conserved in any system'], 0)]),
SS('The Partition of India and Decolonization in South Asia',
   'Grade 6 Social Studies strand: the Partition of India in 1947 divided British India into India and Pakistan as both gained independence, a major event in the broader 20th-century decolonization of South Asia.',
   [('The Partition of India in 1947 divided British India into ___.', ['India and Pakistan', 'India and China', 'A division unrelated to the Partition of India', 'Two entirely different, unrelated countries'], 0),
    ('The Partition of India took place as part of the broader process of ___.', ['Decolonization in South Asia', 'The founding of the Ottoman Empire', 'A process unrelated to the Partition of India', 'European colonization beginning for the first time'], 0),
    ('Why is the Partition of India considered a significant, and often difficult, historical event?', ['It caused mass migration and hardship for millions of people during the division', 'It had no impact on the people living in the region', 'A reason unrelated to the Partition of India', 'It occurred with no historical consequences at all'], 0),
    ('Decolonization generally refers to the process by which ___.', ['Colonies gain independence from the countries that once controlled them', 'Countries expand their control over new colonies', 'A concept unrelated to decolonization', 'Independent countries willingly become colonies again'], 0),
    ('Why is it valuable to study events like the Partition of India?', ['It helps build understanding of how independence movements shaped the modern world', 'This event has no connection to understanding global history', 'A reason unrelated to social studies learning', 'Only Canadian history is relevant to social studies learning'], 0)])]),
day(56, [
L('Media Literacy: Understanding Clickbait and Headlines',
  'Grade 6 Language strand: clickbait uses sensational or misleading headlines designed to attract clicks, often exaggerating or leaving out important information from a story.',
  [('Clickbait headlines are designed to ___.', ['Attract clicks, often through sensational or exaggerated wording', 'Give a completely accurate summary of every detail in a story', 'A concept unrelated to media literacy', 'Provide no information about the article at all'], 0),
   ('Which is a common feature of a clickbait headline?', ['Leaving out key information to create curiosity', 'Providing a full and accurate summary of the story', 'A concept unrelated to clickbait', 'Using only plain, unemotional language'], 0),
   ('Why should readers be cautious of clickbait headlines?', ['They can be misleading and may not accurately represent the full story', 'Clickbait headlines are always completely accurate', 'A reason unrelated to media literacy', 'Headlines never affect how a reader understands a story'], 0),
   ('What is one strategy for evaluating a headline before sharing an article?', ['Reading the full article to check whether the headline is accurate', 'Sharing the article immediately without reading it', 'A concept unrelated to media literacy', 'Assuming every headline is completely truthful'], 0),
   ('Why do some websites rely on clickbait headlines?', ['Sensational headlines can attract more clicks and views', 'Clickbait headlines never attract any additional attention', 'A reason unrelated to media literacy', 'Websites are required by law to use clickbait headlines'], 0)]),
M('Venn Diagrams and Set Notation (Intro)',
  'Grade 6 Math strand: a Venn diagram uses overlapping circles to show relationships between sets, such as items that belong to one group, another group, or both.',
  [('A Venn diagram uses overlapping circles to show ___.', ['Relationships between different sets of items', 'A single unrelated number', 'A concept unrelated to Venn diagrams', 'A list with no visual organization at all'], 0),
   ('The overlapping section of two circles in a Venn diagram represents ___.', ['Items that belong to both sets', 'Items that belong to neither set', 'A concept unrelated to Venn diagrams', 'Items that appear only outside both circles'], 0),
   ('If Set A is even numbers and Set B is multiples of 3, where would the number 6 appear?', ['In the overlapping section of both circles', 'Outside both circles entirely', 'A location unrelated to the Venn diagram', 'Only in Set A’s circle'], 0),
   ('A set is best described as ___.', ['A collection of distinct items or numbers', 'A single number with no other values', 'A concept unrelated to sets', 'A type of geometric shape only'], 0),
   ('Why are Venn diagrams useful for organizing information?', ['They visually show similarities and differences between groups', 'Venn diagrams provide no useful way to organize information', 'A reason unrelated to Venn diagrams', 'They can only be used with numbers, never with other data'], 0)]),
Sc('Classification of Matter: Elements, Compounds, and Mixtures',
   'Grade 6 Science strand: matter can be classified as an element (a single pure substance), a compound (two or more elements chemically combined), or a mixture (substances combined without a chemical reaction).',
   [('An element is best described as ___.', ['A single pure substance made of only one type of atom', 'A combination of two or more different substances', 'A concept unrelated to matter', 'A substance found only in outer space'], 0),
    ('A compound is formed when ___.', ['Two or more elements are chemically combined', 'A single element exists completely on its own', 'A concept unrelated to compounds', 'Substances are physically combined with no chemical reaction'], 0),
    ('A mixture is formed when ___.', ['Substances are combined without a chemical reaction taking place', 'Elements are chemically bonded together permanently', 'A concept unrelated to mixtures', 'A single pure substance changes into a different element'], 0),
    ('Which of these is an example of a mixture?', ['A salad made of several different ingredients', 'A single pure gold coin', 'A concept unrelated to mixtures', 'A single atom of oxygen'], 0),
    ('Why is it useful to classify matter into elements, compounds, and mixtures?', ['It helps scientists understand and predict how different substances behave', 'Classifying matter provides no useful scientific information', 'A reason unrelated to chemistry', 'All matter behaves in exactly the same way regardless of classification'], 0)]),
SS('The Berlin Wall and a Divided Germany',
   'Grade 6 Social Studies strand: the Berlin Wall was built in 1961 to divide East and West Berlin during the Cold War, becoming a powerful symbol of a divided Germany until it fell in 1989.',
   [('The Berlin Wall was built to divide ___.', ['East and West Berlin', 'North and South Korea', 'A division unrelated to the Berlin Wall', 'Two cities located in Canada'], 0),
    ('The Berlin Wall was built during the historical period known as ___.', ['The Cold War', 'The Industrial Revolution', 'A period unrelated to the Berlin Wall', 'The Renaissance'], 0),
    ('The Berlin Wall became a powerful symbol of ___.', ['A divided Germany and the broader Cold War conflict', 'International cooperation and unity', 'A concept unrelated to the Berlin Wall', 'A period with no political tension at all'], 0),
    ('In what year did the Berlin Wall fall?', ['1989', '1945', 'A year unrelated to the Berlin Wall', '1961'], 0),
    ('Why is the fall of the Berlin Wall considered a significant historical event?', ['It symbolized the end of a divided Germany and eased Cold War tensions', 'It had no effect on Germany or the wider world', 'A reason unrelated to its historical significance', 'It marked the beginning of the Cold War, not its easing'], 0)])]),
day(57, [
L('Writing: Writing a Formal Letter of Request',
  'Grade 6 Language strand: a formal letter of request politely and clearly asks for information, action, or assistance, using proper greetings, structure, and a respectful tone.',
  [('A formal letter of request is written to ___.', ['Politely and clearly ask for information, action, or assistance', 'Simply share a casual story with a friend', 'A concept unrelated to writing', 'Complain without offering any clear request'], 0),
   ('Which of these is an important feature of a formal letter?', ['A polite greeting and a respectful, clear tone', 'Casual slang and informal abbreviations', 'A concept unrelated to formal letters', 'No greeting or closing of any kind'], 0),
   ('Why should a formal letter of request state its purpose clearly near the beginning?', ['It helps the reader quickly understand what is being asked for', 'Formal letters should never state their purpose', 'A reason unrelated to formal letters', 'Clarity is not important in formal writing'], 0),
   ('Which of these would be an appropriate way to close a formal letter?', ['“Sincerely,” followed by the writer’s name', 'A casual “See ya later!”', 'A concept unrelated to formal letters', 'No closing at all'], 0),
   ('Why might someone write a formal letter instead of a text message to request something important?', ['A formal letter conveys seriousness and provides a clear, professional record of the request', 'Formal letters are never appropriate for making a request', 'A reason unrelated to formal writing', 'Text messages are always considered more formal than letters'], 0)]),
M('Combinations and Permutations (Intro)',
  'Grade 6 Math strand: a combination is a selection of items where order does not matter, while a permutation is an arrangement of items where order does matter.',
  [('In a combination, the order of items ___.', ['Does not matter', 'Always matters', 'A concept unrelated to combinations', 'Determines whether the answer is correct or incorrect'], 0),
   ('In a permutation, the order of items ___.', ['Matters', 'Never matters', 'A concept unrelated to permutations', 'Has no effect on the outcome'], 0),
   ('If you are choosing 2 toppings for a pizza from a list, and the order you choose them does not matter, this is an example of a ___.', ['Combination', 'Permutation', 'A term unrelated to this scenario', 'Neither a combination nor a permutation'], 0),
   ('If you are arranging 3 books in a specific order on a shelf, this is an example of a ___.', ['Permutation', 'Combination', 'A term unrelated to this scenario', 'Neither a combination nor a permutation'], 0),
   ('Why might understanding combinations and permutations be useful?', ['They help count possible outcomes in situations like games, passwords, or scheduling', 'These concepts have no real-world use', 'A reason unrelated to combinations and permutations', 'They can only be used with numbers less than 10'], 0)]),
Sc('Nutrient Cycles in Ecosystems',
   'Grade 6 Science strand: nutrient cycles, such as the nitrogen and carbon cycles, describe how essential elements move through living things and the environment, supporting life in an ecosystem.',
   [('A nutrient cycle describes how essential elements move ___.', ['Through living things and the environment', 'Only through the atmosphere, with no connection to living things', 'A concept unrelated to nutrient cycles', 'In a single direction, never returning to the environment'], 0),
    ('Which of these is an example of a nutrient cycle?', ['The nitrogen cycle', 'A cycle with no connection to nutrients', 'The water park cycle', 'A concept unrelated to ecosystems'], 0),
    ('Why are nutrient cycles important for supporting life in an ecosystem?', ['They allow essential elements to be reused and made available to living things', 'Nutrient cycles have no connection to supporting life', 'A reason unrelated to ecosystems', 'Nutrients are used once and never return to the ecosystem'], 0),
    ('Decomposers play a role in nutrient cycles by ___.', ['Breaking down dead organisms and returning nutrients to the soil', 'Removing all nutrients from an ecosystem permanently', 'A role unrelated to nutrient cycles', 'Preventing nutrients from ever being reused'], 0),
    ('Why might disrupting a nutrient cycle affect an entire ecosystem?', ['Many living things depend on the steady availability of these essential elements', 'Nutrient cycles have no effect on the organisms in an ecosystem', 'A reason unrelated to ecosystems', 'Ecosystems are never affected by changes to nutrient availability'], 0)]),
SS('Apartheid and the Fight for Equality in South Africa',
   'Grade 6 Social Studies strand: apartheid was a system of racial segregation enforced by law in South Africa, and the long struggle to end it became a global symbol of the fight for equality.',
   [('Apartheid was a system that ___.', ['Enforced racial segregation by law in South Africa', 'Guaranteed equal rights for all South African citizens', 'A concept unrelated to South African history', 'Existed with no connection to law or government'], 0),
    ('The fight to end apartheid became a symbol of ___.', ['The global struggle for equality and human rights', 'A conflict with no connection to human rights', 'A concept unrelated to South African history', 'A movement that had no international attention'], 0),
    ('Which of these was a key outcome of the movement to end apartheid?', ['The eventual dismantling of legal racial segregation in South Africa', 'The strengthening of apartheid laws over time', 'A concept unrelated to this movement', 'No change to South Africa’s laws or society'], 0),
    ('Why did apartheid attract international attention and criticism?', ['Many people around the world viewed its racial segregation as a violation of human rights', 'The rest of the world had no awareness of apartheid', 'A reason unrelated to this history', 'Apartheid received no international attention at all'], 0),
    ('Why is the history of apartheid still studied today?', ['It offers important lessons about equality, human rights, and social change', 'This history has no relevance to understanding equality today', 'A reason unrelated to social studies learning', 'Apartheid had no lasting effect on South African society'], 0)])]),
day(58, [
L('Grammar: Correcting Sentence Fragments and Run-On Sentences',
  'Grade 6 Language strand: a sentence fragment is an incomplete thought missing a subject or verb, while a run-on sentence incorrectly joins two or more complete sentences without proper punctuation.',
  [('A sentence fragment is ___.', ['An incomplete thought missing a subject or verb', 'A complete sentence with proper punctuation', 'A concept unrelated to grammar', 'Always longer than a complete sentence'], 0),
   ('A run-on sentence incorrectly joins ___.', ['Two or more complete sentences without proper punctuation', 'A single word with no other words at all', 'A concept unrelated to run-on sentences', 'Only fragments, never complete sentences'], 0),
   ('Which of these is a sentence fragment?', ['Running through the park.', 'She was running through the park.', 'A phrase unrelated to sentence fragments', 'The park was full of runners.'], 0),
   ('Which of these is a run-on sentence?', ['I love reading books I read every night before bed.', 'I love reading books, and I read every night before bed.', 'A sentence unrelated to run-on sentences', 'I love reading books. I read every night before bed.'], 0),
   ('Why is it important to correct sentence fragments and run-ons in writing?', ['It helps make writing clear and easier for readers to understand', 'These errors never affect how clearly a sentence communicates an idea', 'A reason unrelated to clear writing', 'Fragments and run-ons are always considered correct grammar'], 0)]),
M('Negative Number Operations in Real-World Contexts',
  'Grade 6 Math strand: negative numbers can represent real-world situations such as temperatures below zero, debts, or elevations below sea level, and operations with them follow the same integer rules.',
  [('A temperature of -5°C could be represented using ___.', ['A negative number', 'Only a positive number', 'A concept unrelated to negative numbers', 'A fraction with no connection to temperature'], 0),
   ('If a person owes $20, this debt could be represented as ___.', ['-20', '20', 'A value unrelated to representing debt', '0'], 0),
   ('If the temperature is -3°C and it rises by 8 degrees, what is the new temperature?', ['5°C', '-11°C', 'A temperature unrelated to the calculation', '11°C'], 0),
   ('An elevation of 400 metres below sea level could be represented as ___.', ['-400', '400', 'A value unrelated to representing elevation', '0'], 0),
   ('Why are negative numbers useful for representing real-world situations?', ['They can show values below a reference point, like zero or sea level', 'Negative numbers have no real-world use', 'A reason unrelated to negative numbers', 'They can only represent values above a reference point'], 0)]),
Sc('Magnetism and Electromagnets',
   'Grade 6 Science strand: magnetism is a force that attracts certain metals, and an electromagnet is created when an electric current flows through a coiled wire, producing a controllable magnetic field.',
   [('Magnetism is a force that ___.', ['Attracts certain metals, such as iron', 'Attracts every material equally', 'A concept unrelated to magnetism', 'Has no effect on any type of material'], 0),
    ('An electromagnet is created when ___.', ['An electric current flows through a coiled wire', 'A permanent magnet is heated to a high temperature', 'A concept unrelated to electromagnets', 'Two magnets are placed far apart from each other'], 0),
    ('What is one advantage of an electromagnet compared to a permanent magnet?', ['Its magnetic field can be turned on and off using an electric current', 'It can never be turned off once created', 'A reason unrelated to electromagnets', 'It has no practical uses at all'], 0),
    ('Which of these is an everyday use of electromagnets?', ['Speakers in headphones or electric motors', 'A concept unrelated to electromagnets', 'A material with no connection to electricity or magnetism', 'A tool used only for measuring temperature'], 0),
    ('Why might increasing the number of coils in an electromagnet’s wire increase its strength?', ['More coils can increase the magnetic field produced by the electric current', 'The number of coils has no effect on an electromagnet’s strength', 'A reason unrelated to electromagnets', 'Fewer coils always produce a stronger magnetic field'], 0)]),
SS('Canada’s Peacekeeping Missions Abroad',
   'Grade 6 Social Studies strand: Canada has a long history of contributing peacekeeping forces to United Nations missions aimed at maintaining stability in regions affected by conflict.',
   [('Canada has historically contributed forces to peacekeeping missions organized by ___.', ['The United Nations', 'A group unrelated to peacekeeping', 'No international organization at all', 'Only its own domestic government'], 0),
    ('The main goal of a peacekeeping mission is generally to ___.', ['Help maintain stability in regions affected by conflict', 'Start new conflicts in a region', 'A concept unrelated to peacekeeping', 'Remove all international involvement from a conflict'], 0),
    ('Why might Canada choose to participate in international peacekeeping missions?', ['To support global stability and demonstrate a commitment to international cooperation', 'Participating in peacekeeping missions serves no useful purpose', 'A reason unrelated to Canada’s foreign policy', 'Canada is required to participate with no choice involved'], 0),
    ('Which of these best describes the role of peacekeeping forces?', ['Helping maintain a ceasefire or supporting stability in a conflict-affected region', 'Starting new wars in regions with existing peace', 'A concept unrelated to peacekeeping', 'Replacing the government of the country they are sent to'], 0),
    ('Why is Canada’s peacekeeping history often discussed as part of its national identity?', ['It reflects a long-standing value Canada has placed on international cooperation', 'Peacekeeping has no connection to Canadian identity', 'A reason unrelated to Canadian history', 'Canada has never taken part in any international missions'], 0)])]),
day(59, [
L('Reading: Comparing Print and Digital Texts',
  'Grade 6 Language strand: print and digital texts can present the same information differently, with digital texts often including hyperlinks, videos, and interactive features not found in print.',
  [('One key difference between print and digital texts is that digital texts often include ___.', ['Hyperlinks, videos, and other interactive features', 'No additional features of any kind', 'A concept unrelated to digital texts', 'Only handwritten notes'], 0),
   ('Which of these is an advantage of a digital text over a print text?', ['It can be updated quickly with new information', 'It can never be changed once it is published', 'A concept unrelated to digital texts', 'It has no connection to the internet at all'], 0),
   ('Which of these is a potential advantage of a print text over a digital text?', ['It does not require a device or internet connection to read', 'It can include embedded video content', 'A concept unrelated to print texts', 'It can be instantly updated with new information'], 0),
   ('Why might a reader need different strategies for reading a digital text compared to a print text?', ['Digital texts can include distractions like links and ads that require extra focus to navigate', 'Reading strategies are always identical for print and digital texts', 'A reason unrelated to reading comprehension', 'Digital texts never include any additional content beyond words'], 0),
   ('Why is it useful to compare how the same story might appear in print versus digital form?', ['It highlights how format can affect how a reader experiences and understands a text', 'The format of a text never affects how it is understood', 'A reason unrelated to reading comprehension', 'Print and digital texts always present identical experiences'], 0)]),
M('Graphing Linear Relationships',
  'Grade 6 Math strand: a linear relationship shows a constant rate of change between two variables, and when graphed, it forms a straight line.',
  [('A linear relationship shows ___.', ['A constant rate of change between two variables', 'A rate of change that is always different at every point', 'A concept unrelated to linear relationships', 'No connection between two variables at all'], 0),
   ('When graphed, a linear relationship forms ___.', ['A straight line', 'A curved line', 'A shape unrelated to linear relationships', 'A single isolated point'], 0),
   ('If a plant grows 2 cm every week starting at 0 cm, this relationship is ___.', ['Linear', 'Not a relationship at all', 'A concept unrelated to graphing', 'Impossible to graph'], 0),
   ('On a graph of a linear relationship, the x-axis and y-axis typically represent ___.', ['The two variables being compared', 'Only a single unrelated number', 'A concept unrelated to graphing', 'The title of the graph only'], 0),
   ('Why are linear relationships useful for making predictions?', ['Their constant rate of change allows future values to be estimated', 'Linear relationships cannot be used to predict anything', 'A reason unrelated to linear relationships', 'They only apply to relationships with no consistent pattern'], 0)]),
Sc('The Nervous System and Reflexes',
   'Grade 6 Science strand: the nervous system controls the body’s responses to its environment, and a reflex is a fast, automatic reaction that happens without conscious thought.',
   [('The nervous system’s main role is to ___.', ['Control the body’s responses to its environment', 'Digest food for energy', 'A role unrelated to the nervous system', 'Pump blood throughout the body'], 0),
    ('A reflex is best described as ___.', ['A fast, automatic reaction that happens without conscious thought', 'A slow, carefully planned response to a situation', 'A concept unrelated to reflexes', 'An action that always requires conscious decision-making'], 0),
    ('Which of these is an example of a reflex?', ['Quickly pulling your hand away from something hot', 'Deciding what to eat for dinner', 'A concept unrelated to reflexes', 'Reading a book from start to finish'], 0),
    ('Why are reflexes useful for the body?', ['They allow for quick protective responses to potential danger', 'Reflexes serve no useful purpose for the body', 'A reason unrelated to reflexes', 'Reflexes always take longer than a conscious decision'], 0),
    ('The brain and spinal cord together make up the ___.', ['Central nervous system', 'Muscular system', 'A system unrelated to the nervous system', 'Digestive system'], 0)]),
SS('The Marshall Plan and Post-War Reconstruction',
   'Grade 6 Social Studies strand: the Marshall Plan was a program launched by the United States after World War II to provide economic aid to help rebuild war-torn European countries.',
   [('The Marshall Plan was launched to help ___.', ['Rebuild war-torn European countries after World War II', 'Begin a brand new war in Europe', 'A concept unrelated to the Marshall Plan', 'End all trade between European countries'], 0),
    ('The Marshall Plan primarily provided ___.', ['Economic aid to European countries', 'Military weapons with no economic support', 'A type of support unrelated to the Marshall Plan', 'No support of any kind'], 0),
    ('Why might economic aid have been especially important for Europe after World War II?', ['Many countries faced widespread destruction and needed support to rebuild their economies', 'European countries faced no economic challenges after the war', 'A reason unrelated to post-war reconstruction', 'Economic aid had no effect on rebuilding efforts'], 0),
    ('Which country launched the Marshall Plan?', ['The United States', 'A country unrelated to the Marshall Plan', 'Canada', 'A country that no longer exists'], 0),
    ('Why is the Marshall Plan still studied as an example of post-war reconstruction?', ['It shows how international aid can help rebuild economies and stability after conflict', 'The Marshall Plan had no lasting effect on Europe’s recovery', 'A reason unrelated to its historical significance', 'It focused only on military strategy, with no economic component'], 0)])]),
day(60, [
L('Writing: Writing an Effective Summary',
  'Grade 6 Language strand: an effective summary condenses a text’s main ideas into a shorter form, using the writer’s own words and leaving out minor details and personal opinions.',
  [('An effective summary should ___.', ['Condense a text’s main ideas into a shorter form', 'Include every single detail from the original text', 'A concept unrelated to writing', 'Be longer than the original text'], 0),
   ('A summary should generally be written ___.', ['In the writer’s own words', 'Using the exact same wording as the original text', 'A concept unrelated to summarizing', 'Without any reference to the original text’s main ideas'], 0),
   ('Which of these should typically be left out of a summary?', ['Minor details and the writer’s personal opinions', 'The most important main ideas of the text', 'A concept unrelated to summarizing', 'Any reference to the topic of the text'], 0),
   ('Why is it useful to be able to write an effective summary?', ['It shows understanding of a text’s key ideas and helps others quickly grasp its content', 'Summaries provide no useful information about a text', 'A reason unrelated to summarizing', 'Summarizing a text is never a useful skill'], 0),
   ('Which is an example of a well-written summary sentence?', ['The article explains three ways communities can reduce waste.', 'The article was seven pages long.', 'A sentence unrelated to summarizing', 'The article uses blue text on a white background.'], 0)]),
M('Review: Exponents, Inequalities, and Graphing',
  'Grade 6 Math strand: this review lesson revisits key ideas from Days 51-60, including exponents, square roots, inequalities, scale drawings, and graphing linear relationships.',
  [('An exponent shows ___.', ['How many times a base number is multiplied by itself', 'How many times a number is added to itself', 'A concept unrelated to exponents', 'The number of digits in a value'], 0),
   ('An inequality compares two values using symbols such as ___.', ['< or >', '= only', 'A symbol unrelated to inequalities', '+ or -'], 0),
   ('Similar figures have ___.', ['The same shape but different sizes', 'The same size but different shapes', 'A concept unrelated to similar figures', 'No relationship to one another at all'], 0),
   ('When graphed, a linear relationship forms ___.', ['A straight line', 'A curved line', 'A shape unrelated to linear relationships', 'A single isolated point'], 0),
   ('Why is it useful to review exponents, inequalities, and graphing together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Matter, Energy, and Body Systems',
   'Grade 6 Science strand: this review lesson revisits key ideas from Days 51-60, including density, acids and bases, erosion, energy transfer, and the skeletal, muscular, and nervous systems.',
   [('Density describes ___.', ['How much mass is packed into a given volume', 'The colour of an object', 'A concept unrelated to density', 'How heavy an object feels when held'], 0),
    ('On the pH scale, a substance with a pH below 7 is considered ___.', ['An acid', 'A base', 'A term unrelated to the pH scale', 'Neutral'], 0),
    ('The law of conservation of energy states that energy ___.', ['Cannot be created or destroyed, only transformed or transferred', 'Is constantly being created out of nothing', 'A concept unrelated to conservation of energy', 'Disappears completely once it is used'], 0),
    ('A reflex is best described as ___.', ['A fast, automatic reaction that happens without conscious thought', 'A slow, carefully planned response to a situation', 'A concept unrelated to reflexes', 'An action that always requires conscious decision-making'], 0),
    ('Why is it useful to review matter, energy, and body systems together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Revolutions, Rights, and Global Change',
   'Grade 6 Social Studies strand: this review lesson revisits key ideas from Days 51-60, including the Industrial Revolution, women’s suffrage, the Berlin Wall, apartheid, and post-war reconstruction.',
   [('The Industrial Revolution brought major changes to how ___.', ['Goods were produced and how people lived and worked', 'Ancient civilizations first began, thousands of years earlier', 'A concept unrelated to this historical period', 'Countries interacted before any trade existed'], 0),
    ('Women’s suffrage movements worked to secure ___.', ['The right for women to vote', 'The right for men to vote for the first time', 'A concept unrelated to suffrage movements', 'A ban on all future elections'], 0),
    ('The Berlin Wall became a powerful symbol of ___.', ['A divided Germany and the broader Cold War conflict', 'International cooperation and unity', 'A concept unrelated to the Berlin Wall', 'A period with no political tension at all'], 0),
    ('Apartheid was a system that ___.', ['Enforced racial segregation by law in South Africa', 'Guaranteed equal rights for all South African citizens', 'A concept unrelated to South African history', 'Existed with no connection to law or government'], 0),
    ('Why is it useful to review revolutions, rights movements, and global change together?', ['It reinforces how these interconnected historical events shaped rights and societies over time', 'These events have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260801):
    """Same technique used for the earlier Phase 3 batches -- reassigns
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
    _rebalance_answer_positions(g6_51_60)
    append_to(6, g6_51_60)
