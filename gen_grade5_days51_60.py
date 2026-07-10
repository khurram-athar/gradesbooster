#!/usr/bin/env python3
"""Phase 3 extension: Grade 5, Days 51-60 (first batch past the Day 50
milestone, pushing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-50 set (see
data/grade5.json): author's style, integers, scale drawings, the
immune system, pulleys, and residential schools.

Subject keys for Grade 5 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 5 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science & Technology',
    'TVO Learn: Grade 5 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L5, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M5, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S5, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS5, q)


g5_51_60 = [
day(51, [
L('Reading: Analyzing an Author’s Style and Word Choice',
  'Grade 5 Language strand: an author’s style is shaped by their word choice, sentence length, and tone, and analyzing it helps readers understand how a writer creates a particular effect.',
  [('An author’s style is shaped by their ___.', ['Word choice, sentence length, and tone', 'Only the number of pages in the book', 'A concept unrelated to reading', 'The colour of the book cover'], 0),
   ('Why might an author use short, choppy sentences in a story?', ['To create a sense of tension or urgency', 'Short sentences never affect how a story feels', 'A reason unrelated to author’s style', 'Only to fill space on the page'], 0),
   ('What does it mean to analyze an author’s word choice?', ['Considering why the author chose specific words and what effect they create', 'Counting how many words appear on each page', 'A concept unrelated to analyzing style', 'Ignoring the words the author actually used'], 0),
   ('Why is it useful for readers to notice an author’s tone?', ['It reveals the author’s attitude toward the subject or characters', 'Tone has no connection to how a text is understood', 'A reason unrelated to reading comprehension', 'Tone only matters in poetry, never in prose'], 0),
   ('Which is an example of analyzing an author’s style?', ['Noticing that an author uses a lot of vivid, descriptive language', 'Counting the total number of chapters in a book', 'A concept unrelated to author’s style', 'Ignoring how the text is written altogether'], 0)]),
M('Adding and Subtracting Integers',
  'Grade 5 Math strand: integers include positive and negative whole numbers, and adding or subtracting them can be modelled on a number line.',
  [('An integer can be ___.', ['A positive or negative whole number', 'Only a positive whole number', 'A concept unrelated to integers', 'Only a fraction or decimal'], 0),
   ('What is -3 + 5?', ['2', '-8', 'A value unrelated to the calculation', '8'], 0),
   ('What is 4 + (-6)?', ['-2', '10', 'A value unrelated to the calculation', '2'], 0),
   ('What is -2 - 3?', ['-5', '5', 'A value unrelated to the calculation', '1'], 0),
   ('On a number line, adding a negative integer means moving ___.', ['To the left', 'To the right', 'A direction unrelated to integers', 'Straight up'], 0)]),
Sc('Structures: Types of Bridges and Load Distribution',
   'Grade 5 Science strand: different bridge designs, such as beam, arch, and suspension bridges, distribute the load (weight and forces) in different ways to stay stable.',
   [('Load distribution in a bridge refers to how a structure ___.', ['Spreads out weight and forces to remain stable', 'Ignores all forces acting on it', 'A concept unrelated to structures', 'Adds unnecessary weight to itself'], 0),
    ('A beam bridge is best described as ___.', ['A simple, rigid structure supported at both ends', 'A bridge that hangs entirely from cables', 'A concept unrelated to bridge design', 'A bridge with no support at all'], 0),
    ('An arch bridge distributes weight by ___.', ['Curving the load outward and down into its supports', 'Removing all weight from the structure', 'A concept unrelated to bridge design', 'Hanging the roadway from tall towers'], 0),
    ('A suspension bridge uses ___ to help support its load.', ['Cables and towers', 'Only a single wooden beam', 'A concept unrelated to bridge design', 'No support structures of any kind'], 0),
    ('Why do engineers test different bridge designs before building them?', ['To find out which design distributes load safely and stays stable', 'Testing designs provides no useful information', 'A reason unrelated to engineering', 'Bridges never need to support any weight'], 0)]),
SS('Residential Schools and Their Legacy',
   'Grade 5 Social Studies strand: residential schools were institutions in Canada that separated Indigenous children from their families and cultures, and their legacy continues to affect Indigenous communities today.',
   [('Residential schools were institutions that ___.', ['Separated Indigenous children from their families and cultures', 'Celebrated and protected Indigenous languages and traditions', 'A concept unrelated to Canadian history', 'Had no lasting impact on Indigenous communities'], 0),
    ('Why is it important for Canadians to learn about residential schools?', ['It helps build understanding of this history and supports reconciliation', 'This history has no relevance to Canada today', 'A reason unrelated to Canadian history', 'Learning about the past never helps understand the present'], 0),
    ('What does “legacy” mean in the context of residential schools?', ['The lasting effects that continue to be felt today', 'A concept unrelated to history', 'An event that had no effect on the future', 'A term unrelated to schools of any kind'], 0),
    ('Which of these is a way Canadians can learn more about this history?', ['Listening to the experiences shared by residential school survivors', 'Ignoring this part of Canadian history entirely', 'A concept unrelated to reconciliation', 'Assuming this history has no connection to the present'], 0),
    ('Why is understanding this history connected to the idea of reconciliation?', ['Acknowledging past harms is an important step toward healing and better relationships', 'Reconciliation has no connection to understanding history', 'A reason unrelated to Indigenous history', 'The past has no bearing on relationships in the present'], 0)])]),
day(52, [
L('Grammar: Parallel Structure in Sentences',
  'Grade 5 Language strand: parallel structure means using the same grammatical pattern for items in a list or comparison, such as “I like reading, writing, and drawing.”',
  [('Parallel structure means using ___.', ['The same grammatical pattern for items in a list or comparison', 'A different grammatical pattern for every item in a sentence', 'A concept unrelated to grammar', 'No consistent pattern at all'], 0),
   ('Which sentence uses correct parallel structure?', ['She likes hiking, swimming, and biking.', 'She likes hiking, to swim, and biking.', 'A sentence unrelated to parallel structure', 'She likes hiking, swims, and to bike.'], 0),
   ('Which sentence uses correct parallel structure?', ['He wanted to run, jump, and climb.', 'He wanted to run, jumping, and climb.', 'A sentence unrelated to parallel structure', 'He wanted running, to jump, and climbed.'], 0),
   ('Why is parallel structure important in writing?', ['It makes sentences clearer and easier to read', 'It has no effect on how a sentence reads', 'A concept unrelated to clear writing', 'It only matters in poetry, never in prose'], 0),
   ('Which phrase breaks parallel structure?', ['“to swim, biking, and to run”', '“swimming, biking, and running”', 'A phrase unrelated to parallel structure', '“to swim, to bike, and to run”'], 0)]),
M('Scale Drawings and Scale Factor',
  'Grade 5 Math strand: a scale drawing represents a real object at a smaller or larger size, and the scale factor tells how much the drawing has been reduced or enlarged.',
  [('A scale drawing represents a real object ___.', ['At a smaller or larger size while keeping proportions the same', 'At exactly the same size with no changes', 'A concept unrelated to scale drawings', 'With no connection to the real object at all'], 0),
   ('If a scale factor is 1:100, one unit on the drawing represents ___ units in real life.', ['100', '1', 'A number unrelated to the scale factor', '10'], 0),
   ('On a map with a scale of 1 cm = 5 km, how many kilometres does 3 cm represent?', ['15 km', '5 km', 'A distance unrelated to the calculation', '8 km'], 0),
   ('Why are scale drawings useful for architects and mapmakers?', ['They allow large objects or areas to be represented accurately on paper', 'Scale drawings provide no useful information', 'A reason unrelated to scale drawings', 'They are only used for decoration, not measurement'], 0),
   ('A scale factor greater than 1 means the drawing is ___ the real object.', ['Larger than', 'Smaller than', 'A comparison unrelated to scale factor', 'Exactly the same size as'], 0)]),
Sc('The Immune System and Fighting Illness',
   'Grade 5 Science strand: the immune system is the body’s defence network, using white blood cells and other tools to fight off germs and illness.',
   [('The immune system’s main job is to ___.', ['Defend the body against germs and illness', 'Digest food for energy', 'A concept unrelated to the immune system', 'Pump blood throughout the body'], 0),
    ('White blood cells help the body by ___.', ['Fighting off harmful germs', 'Carrying oxygen throughout the body', 'A function unrelated to white blood cells', 'Breaking down food in the stomach'], 0),
    ('Which is an example of something that can trigger an immune response?', ['A virus entering the body', 'A concept unrelated to the immune system', 'Drinking a glass of water', 'Taking a short nap'], 0),
    ('Why are vaccines useful for the immune system?', ['They help the body learn to recognize and fight specific germs', 'Vaccines have no connection to the immune system', 'A reason unrelated to immunity', 'Vaccines remove the immune system’s ability to function'], 0),
    ('Why might a fever occur when the body is fighting an infection?', ['It can be part of the immune system’s response to fight off germs', 'A fever has no connection to the immune system', 'A reason unrelated to illness', 'Fevers only occur when a person is completely healthy'], 0)]),
SS('Canada’s Peacekeeping Role Internationally',
   'Grade 5 Social Studies strand: Canada has historically contributed peacekeeping forces to United Nations missions aimed at maintaining peace and stability in conflict areas around the world.',
   [('Peacekeeping generally involves ___.', ['Helping maintain peace and stability in areas affected by conflict', 'Starting new conflicts between countries', 'A concept unrelated to international relations', 'Ignoring conflicts happening around the world'], 0),
    ('Canada has historically contributed peacekeeping forces to missions organized by ___.', ['The United Nations', 'A group unrelated to peacekeeping', 'No international organization at all', 'Only its own domestic government'], 0),
    ('Why might a country choose to participate in international peacekeeping?', ['To help support global stability and assist regions affected by conflict', 'Participating in peacekeeping serves no useful purpose', 'A reason unrelated to international cooperation', 'Countries are required to participate with no choice involved'], 0),
    ('Which of these best describes a peacekeeping mission?', ['International forces helping maintain a ceasefire or stability in a region', 'A mission with no connection to conflict or stability', 'A concept unrelated to peacekeeping', 'A group of soldiers sent to start a new war'], 0),
    ('Why is Canada’s peacekeeping history often discussed as part of its national identity?', ['It reflects a long-standing value Canada has placed on international cooperation', 'Peacekeeping has no connection to Canadian identity', 'A reason unrelated to Canadian history', 'Canada has never taken part in any international missions'], 0)])]),
day(53, [
L('Writing: Writing a Personal Essay',
  'Grade 5 Language strand: a personal essay explores the writer’s own thoughts, experiences, or opinions on a topic, often blending storytelling with reflection.',
  [('A personal essay explores ___.', ['The writer’s own thoughts, experiences, or opinions', 'Only facts with no personal reflection at all', 'A concept unrelated to writing', 'A topic the writer has no connection to'], 0),
   ('A personal essay often blends storytelling with ___.', ['Reflection on what the experience meant to the writer', 'No reflection of any kind', 'A concept unrelated to personal essays', 'Instructions for completing a task'], 0),
   ('Which is an example of a good topic for a personal essay?', ['A challenge you overcame and what you learned from it', 'A set of directions for baking a cake', 'A concept unrelated to personal essays', 'A topic with no connection to your own life'], 0),
   ('Why might a writer choose to write in first person for a personal essay?', ['It reflects the writer’s own perspective and experience', 'First person is never used in personal essays', 'A reason unrelated to personal essays', 'First person makes an essay less personal'], 0),
   ('What is one key difference between a personal essay and a research report?', ['A personal essay focuses on the writer’s own experience and reflection', 'A personal essay never includes the writer’s own thoughts', 'A concept unrelated to these two writing forms', 'A research report is always written in first person'], 0)]),
M('Surface Area of Rectangular Prisms',
  'Grade 5 Math strand: the surface area of a rectangular prism is the total area of all six faces, found by calculating and adding the area of each face.',
  [('The surface area of a rectangular prism is ___.', ['The total area of all six faces added together', 'The volume of the prism', 'A concept unrelated to surface area', 'The length of just one edge'], 0),
   ('How many faces does a rectangular prism have?', ['6', '4', 'A number unrelated to rectangular prisms', '8'], 0),
   ('What is the area of one face of a rectangular prism measuring 4 by 3?', ['12 square units', '7 square units', 'A value unrelated to the calculation', '24 square units'], 0),
   ('Surface area is measured in ___.', ['Square units', 'Cubic units', 'A unit unrelated to surface area', 'Linear units'], 0),
   ('Why might someone need to calculate surface area in real life?', ['To determine how much material is needed to cover or wrap an object', 'Surface area has no real-world use', 'A reason unrelated to surface area', 'To measure how much a box can hold inside it'], 0)]),
Sc('Pulleys and Gear Ratios',
   'Grade 5 Science strand: pulleys use a wheel and rope to change the direction or amount of force needed to lift a load, and gear ratios describe how connected gears affect speed and force.',
   [('A pulley changes the ___ needed to lift a load.', ['Direction or amount of force', 'Colour of the load', 'A concept unrelated to pulleys', 'Weight of the load itself'], 0),
    ('A gear ratio describes the relationship between ___.', ['The number of teeth on two connected gears', 'The colour of two connected gears', 'A concept unrelated to gears', 'The temperature of a machine’s parts'], 0),
    ('Why might a system use multiple pulleys together?', ['To reduce the amount of force needed to lift a heavy load', 'Multiple pulleys always make lifting a load harder', 'A reason unrelated to pulleys', 'Multiple pulleys serve no mechanical purpose'], 0),
    ('If a small gear turns a much larger gear, the larger gear will generally turn ___.', ['More slowly', 'More quickly', 'A description unrelated to gear ratios', 'At exactly the same speed'], 0),
    ('Why are pulleys and gears useful in everyday machines?', ['They make lifting, moving, or turning objects easier or more efficient', 'They make every task more difficult to complete', 'A reason unrelated to simple machines', 'They have no practical use in real machines'], 0)]),
SS('The Métis Nation and the Red River Resistance',
   'Grade 5 Social Studies strand: the Métis Nation, formed from Indigenous and European ancestry, played a key role in the Red River Resistance, led by Louis Riel, to defend Métis rights and land.',
   [('The Métis Nation formed from a blending of ___.', ['Indigenous and European ancestry and culture', 'Only European settlers with no Indigenous connection', 'A concept unrelated to the Métis Nation', 'Only Indigenous peoples with no European connection'], 0),
    ('The Red River Resistance was primarily focused on ___.', ['Defending Métis rights and land', 'Building new railways across the country', 'A concept unrelated to the Red River Resistance', 'Establishing a new international trade agreement'], 0),
    ('Who was a key leader of the Red River Resistance?', ['Louis Riel', 'A person unrelated to the Red River Resistance', 'A leader from a completely different country', 'A leader with no connection to Métis history'], 0),
    ('Why is the Red River Resistance an important event in Canadian history?', ['It highlights the Métis Nation’s efforts to protect their rights and way of life', 'This event has no significance in Canadian history', 'A reason unrelated to Métis history', 'It had no lasting effect on Canada’s development'], 0),
    ('Why is it valuable for students to learn about the Métis Nation’s history?', ['It builds a fuller understanding of the diverse peoples who shaped Canada', 'The Métis Nation has no connection to Canadian history', 'A reason unrelated to social studies learning', 'Only one group’s history is relevant to understanding Canada'], 0)])]),
day(54, [
L('Vocabulary: Analogies',
  'Grade 5 Language strand: an analogy compares two pairs of words that share a similar relationship, such as “hot is to cold as up is to down.”',
  [('An analogy compares ___.', ['Two pairs of words that share a similar relationship', 'Two completely unrelated words with no connection', 'A concept unrelated to vocabulary', 'Only the spelling of two words'], 0),
   ('Complete the analogy: Bird is to nest as bee is to ___.', ['Hive', 'Wing', 'A word unrelated to the analogy', 'Sky'], 0),
   ('Complete the analogy: Author is to book as painter is to ___.', ['Painting', 'Brush', 'A word unrelated to the analogy', 'Museum'], 0),
   ('What relationship does the analogy “up is to down as hot is to cold” show?', ['Opposites', 'Synonyms', 'A relationship unrelated to analogies', 'Items from the same category'], 0),
   ('Why are analogies a useful vocabulary tool?', ['They help readers understand relationships between words and ideas', 'Analogies never help with understanding vocabulary', 'A concept unrelated to vocabulary building', 'Analogies only apply to numbers, not words'], 0)]),
M('Probability: Theoretical vs. Experimental',
  'Grade 5 Math strand: theoretical probability predicts an outcome based on possible results, while experimental probability is based on the actual results of repeated trials.',
  [('Theoretical probability is based on ___.', ['What is possible, calculated before any trials happen', 'Only the results of trials that have already happened', 'A concept unrelated to probability', 'A random guess with no calculation involved'], 0),
   ('Experimental probability is based on ___.', ['The actual results of repeated trials', 'What is possible before any trials happen', 'A concept unrelated to probability', 'A number with no connection to any trials'], 0),
   ('What is the theoretical probability of flipping heads on a fair coin?', ['1/2', '1/4', 'A value unrelated to the calculation', '1/3'], 0),
   ('If you flip a coin 20 times and get heads 12 times, what is the experimental probability of heads?', ['12/20', '1/2', 'A value unrelated to the calculation', '8/20'], 0),
   ('Why might experimental probability differ from theoretical probability?', ['Real trials can vary due to chance, especially with a small number of trials', 'Experimental and theoretical probability are always identical', 'A reason unrelated to probability', 'Experimental probability never involves any real trials'], 0)]),
Sc('Climate vs. Weather',
   'Grade 5 Science strand: weather describes short-term atmospheric conditions like today’s temperature or rain, while climate describes the average weather patterns of a region over a long period of time.',
   [('Weather describes ___.', ['Short-term atmospheric conditions, such as today’s temperature', 'The average conditions of a region over many years', 'A concept unrelated to weather', 'A concept found only in science fiction'], 0),
    ('Climate describes ___.', ['The average weather patterns of a region over a long period of time', 'Only the weather happening right now', 'A concept unrelated to climate', 'A single day’s temperature and rainfall'], 0),
    ('Which statement is an example of describing weather?', ['It is raining outside today.', 'This region has cold winters and warm summers on average.', 'A statement unrelated to weather or climate', 'This area has a desert climate.'], 0),
    ('Which statement is an example of describing climate?', ['This region typically has hot, dry summers.', 'It is sunny outside right now.', 'A statement unrelated to weather or climate', 'The temperature today is 22 degrees.'], 0),
    ('Why is it important to understand the difference between weather and climate?', ['It helps people make sense of both short-term forecasts and long-term environmental patterns', 'Weather and climate are always exactly the same thing', 'A reason unrelated to science', 'This distinction has no practical use'], 0)]),
SS('Canada’s Supreme Court and Landmark Cases',
   'Grade 5 Social Studies strand: the Supreme Court of Canada is the highest court in the country, and its landmark cases have shaped Canadian law and rights over time.',
   [('The Supreme Court of Canada is ___.', ['The highest court in the country', 'A court that only handles local disputes', 'A concept unrelated to Canadian government', 'A court found only at the municipal level'], 0),
    ('A landmark case is one that ___.', ['Sets an important precedent that shapes future law', 'Has no lasting effect on Canadian law', 'A concept unrelated to the legal system', 'Is always immediately forgotten after the ruling'], 0),
    ('Why is the Supreme Court considered the highest court in Canada?', ['Its decisions are final and cannot be appealed to a higher court', 'It only handles cases involving traffic violations', 'A reason unrelated to Canada’s court system', 'Its decisions can always be overturned by any other court'], 0),
    ('How can a Supreme Court ruling affect all of Canada?', ['It can set a legal precedent that applies across the whole country', 'Supreme Court rulings only apply to a single province', 'A reason unrelated to how courts function', 'Rulings from the Supreme Court have no effect on Canadian law'], 0),
    ('Why is it useful for students to learn about landmark court cases?', ['It helps them understand how laws and rights have developed over time', 'Landmark cases provide no useful information about Canadian history', 'A reason unrelated to social studies learning', 'Court cases have no connection to how rights are protected'], 0)])]),
day(55, [
L('Reading: Understanding Foreshadowing',
  'Grade 5 Language strand: foreshadowing is a writing technique where an author hints at events that will happen later in a story.',
  [('Foreshadowing is a technique where an author ___.', ['Hints at events that will happen later in the story', 'Reveals the entire ending at the very beginning', 'A concept unrelated to reading', 'Removes all clues about what might happen next'], 0),
   ('Why might an author use foreshadowing?', ['To build suspense and prepare readers for upcoming events', 'Foreshadowing never affects how a reader experiences a story', 'A reason unrelated to storytelling', 'To confuse readers with no clear purpose'], 0),
   ('Which is an example of foreshadowing?', ['A character noticing dark storm clouds before a disaster occurs later in the story', 'A character simply describing their breakfast', 'A concept unrelated to foreshadowing', 'A story with absolutely no hints about future events'], 0),
   ('How is foreshadowing different from a flashback?', ['Foreshadowing hints at future events, while a flashback shows past events', 'Foreshadowing and flashback mean exactly the same thing', 'A concept unrelated to these techniques', 'A flashback hints at future events instead'], 0),
   ('Why might noticing foreshadowing make reading more enjoyable?', ['It can build anticipation and reward careful readers with connections', 'Noticing foreshadowing never adds anything to the reading experience', 'A reason unrelated to reading enjoyment', 'Foreshadowing always reveals the ending immediately'], 0)]),
M('Algebraic Expressions: Variables and Terms',
  'Grade 5 Math strand: an algebraic expression uses variables (letters representing unknown numbers) and terms to represent a mathematical relationship, such as “3x + 5.”',
  [('A variable in an algebraic expression is ___.', ['A letter that represents an unknown number', 'Always a fixed number that never changes', 'A concept unrelated to algebra', 'A symbol with no mathematical meaning'], 0),
   ('In the expression “3x + 5,” what is the variable?', ['x', '3', 'A part of the expression unrelated to variables', '5'], 0),
   ('In the expression “2y + 7,” what does “2y” represent?', ['2 multiplied by the variable y', '2 added to the variable y', 'A part unrelated to the expression', 'The value 27'], 0),
   ('If x = 4, what is the value of 3x + 5?', ['17', '12', 'A value unrelated to the calculation', '9'], 0),
   ('Why are algebraic expressions useful in math?', ['They let us represent unknown or changing quantities in a general way', 'They have no practical use in solving problems', 'A reason unrelated to algebra', 'They can only be used with specific, known numbers'], 0)]),
Sc('Life Cycles of Plants and Pollination',
   'Grade 5 Science strand: plants go through a life cycle from seed to mature plant, and pollination -- often carried out by insects or wind -- is a key step that allows plants to reproduce.',
   [('Pollination is the process by which ___.', ['Pollen is transferred to allow a plant to reproduce', 'A plant absorbs water through its roots', 'A concept unrelated to plant life cycles', 'A seed is planted in the soil'], 0),
    ('Which of these commonly helps carry out pollination?', ['Bees and other insects', 'Rocks and soil alone', 'A concept unrelated to pollination', 'Only artificial machines'], 0),
    ('What is the first stage in a plant’s life cycle?', ['A seed', 'A fully grown, flowering plant', 'A stage unrelated to plant life cycles', 'A fruit'], 0),
    ('Why is pollination important for many plants?', ['It allows plants to produce seeds and reproduce', 'Pollination has no connection to how plants reproduce', 'A reason unrelated to plant biology', 'Pollination only affects the colour of a plant’s leaves'], 0),
    ('Wind pollination is common in plants that ___.', ['Produce large amounts of light, airborne pollen', 'Rely entirely on insects for reproduction', 'A description unrelated to pollination', 'Never produce any pollen at all'], 0)]),
SS('Globalization and Its Effects on Canada',
   'Grade 5 Social Studies strand: globalization is the increasing connection between countries through trade, technology, and culture, and it has significant effects on Canada’s economy and society.',
   [('Globalization refers to ___.', ['The increasing connection between countries through trade, technology, and culture', 'Countries becoming completely isolated from one another', 'A concept unrelated to international relations', 'A process that only affects a single country'], 0),
    ('Which is an example of globalization affecting Canada?', ['Canadians buying products manufactured in other countries', 'Canada having no trade relationships with any other country', 'A concept unrelated to globalization', 'Canada being completely self-sufficient with no imports'], 0),
    ('How has technology contributed to globalization?', ['It has made communication and trade between countries faster and easier', 'Technology has no connection to how countries interact', 'A reason unrelated to globalization', 'Technology has made international communication impossible'], 0),
    ('Which is a potential effect of globalization on Canada’s economy?', ['Increased trade opportunities with other countries', 'A complete end to all trade with other countries', 'A concept unrelated to globalization', 'No effect on Canada’s economy at all'], 0),
    ('Why is it useful for students to understand globalization?', ['It helps explain how connected Canada is to the rest of the world', 'Globalization has no relevance to understanding Canada today', 'A reason unrelated to social studies learning', 'Canada operates with no connection to other countries'], 0)])]),
day(56, [
L('Figurative Language: Alliteration and Assonance',
  'Grade 5 Language strand: alliteration repeats consonant sounds at the start of nearby words, while assonance repeats vowel sounds within nearby words, both creating rhythm and emphasis.',
  [('Alliteration repeats ___.', ['Consonant sounds at the start of nearby words', 'Vowel sounds within nearby words', 'A concept unrelated to figurative language', 'The same word over and over with no variation'], 0),
   ('Assonance repeats ___.', ['Vowel sounds within nearby words', 'Consonant sounds at the start of nearby words', 'A concept unrelated to figurative language', 'Only the final letter of a word'], 0),
   ('Which phrase is an example of alliteration?', ['Sally sells seashells by the seashore.', 'The cat sat on the mat.', 'A phrase unrelated to alliteration', 'She walked to the store.'], 0),
   ('Which phrase is an example of assonance?', ['The rain in Spain falls mainly on the plain.', 'Peter Piper picked a peck.', 'A phrase unrelated to assonance', 'The dog ran quickly down the street.'], 0),
   ('Why might a poet use alliteration or assonance?', ['To create rhythm, emphasis, or a musical quality in the writing', 'These techniques never affect how a poem sounds', 'A reason unrelated to figurative language', 'To make a poem harder to read aloud'], 0)]),
M('Comparing and Ordering Integers',
  'Grade 5 Math strand: integers can be compared and ordered on a number line, where numbers further to the right are greater than numbers further to the left.',
  [('On a number line, a number further to the right is ___.', ['Greater than a number to its left', 'Always smaller than a number to its left', 'A concept unrelated to comparing integers', 'Exactly equal to every other number'], 0),
   ('Which integer is greater: -3 or 2?', ['2', '-3', 'A value unrelated to the comparison', 'They are equal'], 0),
   ('Which integer is less: -8 or -2?', ['-8', '-2', 'A value unrelated to the comparison', 'They are equal'], 0),
   ('Order these integers from least to greatest: 3, -5, 0, -1.', ['-5, -1, 0, 3', '3, 0, -1, -5', 'An order unrelated to these integers', '0, -1, -5, 3'], 0),
   ('Why is understanding negative numbers useful in real life?', ['They can represent things like temperatures below zero or amounts owed', 'Negative numbers have no real-world use', 'A reason unrelated to integers', 'Negative numbers are only used in advanced mathematics'], 0)]),
Sc('Static Electricity and Charge',
   'Grade 5 Science strand: static electricity occurs when electric charges build up on the surface of an object, often from friction, and can cause objects to attract or repel each other.',
   [('Static electricity often builds up because of ___.', ['Friction between two objects', 'Water flowing through a pipe', 'A concept unrelated to static electricity', 'The temperature of the air alone'], 0),
    ('Objects with the same type of electric charge will ___ each other.', ['Repel', 'Attract', 'An interaction unrelated to charge', 'Have no effect on'], 0),
    ('Objects with opposite electric charges will ___ each other.', ['Attract', 'Repel', 'An interaction unrelated to charge', 'Have no effect on'], 0),
    ('Which is an everyday example of static electricity?', ['A balloon sticking to a wall after being rubbed on hair', 'Water boiling in a kettle', 'A concept unrelated to static electricity', 'A magnet attracting metal from across a room'], 0),
    ('Why might your hair stand up after rubbing a balloon on it?', ['The balloon transfers a static charge that causes the hair strands to repel each other', 'Hair naturally stands up with no connection to electric charge', 'A reason unrelated to static electricity', 'The balloon removes all charge from the hair'], 0)]),
SS('Population Distribution and Density in Canada',
   'Grade 5 Social Studies strand: Canada’s population is unevenly distributed, with most people living in southern regions near the border, resulting in varying population density across the country.',
   [('Population density refers to ___.', ['The number of people living in a given area', 'The total land area of a country', 'A concept unrelated to population', 'The number of cities in a country'], 0),
    ('Most of Canada’s population lives ___.', ['In southern regions, close to the border with the United States', 'In the far northern Arctic regions', 'A location unrelated to population distribution', 'Equally spread across every region of the country'], 0),
    ('Why might a region with a mild climate and good farmland have a higher population density?', ['It can better support agriculture and comfortable living conditions', 'Climate and farmland have no effect on where people choose to live', 'A reason unrelated to population distribution', 'Population is distributed with no connection to geography'], 0),
    ('Which of these would likely have a lower population density?', ['A remote northern territory', 'A large southern city', 'A concept unrelated to population density', 'A densely built urban downtown'], 0),
    ('Why is it useful to study population distribution across Canada?', ['It helps explain patterns in where services, cities, and resources are located', 'Population distribution provides no useful information', 'A reason unrelated to geography', 'Every region of Canada has an identical population'], 0)])]),
day(57, [
L('Writing: Writing a Literary Response',
  'Grade 5 Language strand: a literary response shares the writer’s thoughts and reactions to a text, supported by specific evidence and examples from the reading.',
  [('A literary response shares ___.', ['The writer’s thoughts and reactions to a text, supported by evidence', 'Only a summary of the plot with no personal reaction', 'A concept unrelated to writing', 'A completely new, unrelated story'], 0),
   ('Why is it important to include evidence in a literary response?', ['It supports the writer’s ideas with specific details from the text', 'Evidence is never needed when responding to a text', 'A reason unrelated to writing a literary response', 'Evidence makes a response less convincing'], 0),
   ('Which is an example of evidence a writer might use in a literary response?', ['A specific quote or event from the story', 'A completely unrelated fact about a different book', 'A concept unrelated to literary responses', 'The writer’s opinion with no connection to the text'], 0),
   ('What might a literary response include besides a summary of events?', ['The writer’s personal reaction and interpretation of the text', 'Only a list of characters with no further detail', 'A concept unrelated to literary responses', 'Instructions for how to read the book'], 0),
   ('Why might two readers write very different literary responses to the same book?', ['Readers can have different reactions, interpretations, and connections to a text', 'All readers are required to respond to a text in exactly the same way', 'A reason unrelated to literary responses', 'Literary responses never include any personal interpretation'], 0)]),
M('Converting Between Fractions, Decimals, and Percents',
  'Grade 5 Math strand: fractions, decimals, and percents are different ways to represent the same value, and converting between them uses division, multiplication, or place value.',
  [('What is 1/2 written as a decimal?', ['0.5', '0.2', 'A value unrelated to the conversion', '1.5'], 0),
   ('What is 0.75 written as a percent?', ['75%', '7.5%', 'A value unrelated to the conversion', '750%'], 0),
   ('What is 3/4 written as a percent?', ['75%', '34%', 'A value unrelated to the conversion', '43%'], 0),
   ('To convert a decimal to a percent, you ___.', ['Multiply by 100', 'Divide by 100', 'A method unrelated to converting decimals', 'Add 100 to the decimal'], 0),
   ('What is 25% written as a fraction in lowest terms?', ['1/4', '1/2', 'A fraction unrelated to the conversion', '2/5'], 0)]),
Sc('Natural Disasters and Their Causes',
   'Grade 5 Science strand: natural disasters such as earthquakes, floods, and tornadoes are caused by natural processes in the Earth’s systems, including shifting tectonic plates and extreme weather.',
   [('An earthquake is often caused by ___.', ['Shifting tectonic plates beneath the Earth’s surface', 'A sudden change in air temperature', 'A concept unrelated to earthquakes', 'The movement of ocean currents alone'], 0),
    ('A flood can be caused by ___.', ['Excessive rainfall or rapid snowmelt', 'A lack of rainfall over a long period', 'A concept unrelated to floods', 'A sudden drop in temperature'], 0),
    ('A tornado forms when ___.', ['Warm and cold air masses collide, creating strong rotating winds', 'The ground shifts suddenly beneath the surface', 'A concept unrelated to tornadoes', 'Ocean water rises unusually high'], 0),
    ('Why do scientists study natural disasters?', ['To better predict them and help keep communities safe', 'Studying natural disasters provides no useful information', 'A reason unrelated to science', 'Natural disasters cannot be studied or understood'], 0),
    ('Which of these is a way communities can prepare for natural disasters?', ['Creating emergency plans and warning systems', 'Ignoring the possibility of a natural disaster entirely', 'A concept unrelated to disaster preparedness', 'Assuming natural disasters never occur'], 0)]),
SS('Canada’s Relationship with the United States',
   'Grade 5 Social Studies strand: Canada and the United States share the world’s longest international border and have close economic, cultural, and political ties.',
   [('Canada and the United States share ___.', ['The world’s longest international border', 'No border at all', 'A concept unrelated to their relationship', 'A border that is closed to all trade'], 0),
    ('Which is an example of the close economic ties between Canada and the United States?', ['A large amount of trade in goods and services between the two countries', 'A complete absence of any trade between the two countries', 'A concept unrelated to their relationship', 'Canada trading only with countries outside North America'], 0),
    ('Why might close cultural ties exist between Canada and the United States?', ['The two countries share similar media, language, and geographic closeness', 'The two countries have no shared culture or media of any kind', 'A reason unrelated to their relationship', 'Canada and the United States have never interacted culturally'], 0),
    ('Which of these is an example of political cooperation between the two countries?', ['Working together on shared border and trade agreements', 'Refusing to communicate on any shared issues', 'A concept unrelated to their relationship', 'Having completely separate, unconnected governments with no interaction'], 0),
    ('Why is Canada’s relationship with the United States significant for Canadians?', ['It affects trade, travel, and many parts of daily life due to their close connection', 'This relationship has no effect on Canadians’ daily lives', 'A reason unrelated to Canadian geography', 'Canada and the United States operate with no connection to one another'], 0)])]),
day(58, [
L('Reading: Evaluating Arguments and Counterarguments',
  'Grade 5 Language strand: evaluating an argument means judging whether the reasons and evidence support the claim, while a counterargument presents an opposing point of view.',
  [('Evaluating an argument means judging whether ___.', ['The reasons and evidence actually support the claim', 'The argument is written in complete sentences', 'A concept unrelated to reading', 'The text is a certain length'], 0),
   ('A counterargument presents ___.', ['An opposing point of view to the main argument', 'The exact same point of view as the main argument', 'A concept unrelated to argumentation', 'A summary of the entire text'], 0),
   ('Why might a writer include a counterargument in a persuasive text?', ['To show they have considered other perspectives and strengthen their own argument', 'Counterarguments always weaken a writer’s position', 'A reason unrelated to persuasive writing', 'Counterarguments are never included in persuasive writing'], 0),
   ('What should a reader look for when evaluating whether an argument is strong?', ['Solid evidence and logical reasoning that supports the claim', 'Whether the argument uses the most exciting language', 'A concept unrelated to evaluating arguments', 'The number of paragraphs in the text'], 0),
   ('Which is an example of evaluating an argument critically?', ['Checking whether the evidence used actually supports the claim being made', 'Believing every claim in a text without question', 'A concept unrelated to critical reading', 'Ignoring the reasons given for a claim entirely'], 0)]),
M('Line Plots and Stem-and-Leaf Plots',
  'Grade 5 Math strand: a line plot displays data using marks above a number line, while a stem-and-leaf plot organizes numerical data by splitting each value into a “stem” and a “leaf.”',
  [('A line plot displays data using ___.', ['Marks placed above a number line', 'Slices of a circle', 'A concept unrelated to line plots', 'Bars of different heights only'], 0),
   ('In a stem-and-leaf plot, the “stem” usually represents ___.', ['The leading digit(s) of a number', 'The exact value of a single data point', 'A concept unrelated to stem-and-leaf plots', 'The total number of data points'], 0),
   ('In a stem-and-leaf plot, the “leaf” usually represents ___.', ['The last digit of a number', 'The leading digit(s) of a number', 'A concept unrelated to stem-and-leaf plots', 'The total sum of all data points'], 0),
   ('Why might someone use a line plot to display data?', ['It shows how often each value occurs in a simple, visual way', 'Line plots cannot display any type of data', 'A reason unrelated to graphing data', 'Line plots only work with non-numerical data'], 0),
   ('In the stem-and-leaf entry “3 | 4,” what value does this represent?', ['34', '3.4', 'A value unrelated to the plot', '43'], 0)]),
Sc('Structures: Materials Engineering and Testing',
   'Grade 5 Science strand: engineers test different materials for strength, flexibility, and durability to determine the best choice for building a stable structure.',
   [('Materials engineering involves testing materials for qualities such as ___.', ['Strength, flexibility, and durability', 'Only their colour and appearance', 'A concept unrelated to engineering', 'Their price alone, with no other testing'], 0),
    ('Why might an engineer test a material’s flexibility before using it in a structure?', ['To see whether it can bend without breaking under stress', 'Flexibility has no connection to how a structure performs', 'A reason unrelated to materials engineering', 'Flexibility testing is never done in engineering'], 0),
    ('Which of these is an example of testing a material’s strength?', ['Applying weight to a beam to see how much it can hold before bending', 'Painting a beam a different colour', 'A concept unrelated to materials testing', 'Measuring the temperature of the room'], 0),
    ('Why is durability an important quality for building materials?', ['Durable materials can withstand wear and last longer over time', 'Durability has no connection to how well a structure lasts', 'A reason unrelated to materials engineering', 'Materials never need to withstand any wear over time'], 0),
    ('Why do engineers compare multiple materials before choosing one for a project?', ['To select the material best suited to the structure’s needs and conditions', 'Comparing materials provides no useful information', 'A reason unrelated to engineering design', 'Only one material has ever been used to build anything'], 0)]),
SS('Land Acknowledgements and Treaty Territories',
   'Grade 5 Social Studies strand: a land acknowledgement recognizes the Indigenous peoples who have traditionally lived on and cared for a particular territory, often defined by historic treaties.',
   [('A land acknowledgement recognizes ___.', ['The Indigenous peoples who have traditionally lived on a territory', 'A country’s entire history, with no focus on any specific group', 'A concept unrelated to Indigenous history', 'A modern boundary with no historical significance'], 0),
    ('A treaty territory is often defined by ___.', ['A historic agreement between Indigenous nations and the government', 'A boundary drawn with no historical basis', 'A concept unrelated to treaties', 'A region that has never had any agreements in place'], 0),
    ('Why might a school or organization begin an event with a land acknowledgement?', ['To show respect for the Indigenous peoples connected to that land', 'Land acknowledgements have no purpose or meaning', 'A reason unrelated to Indigenous history', 'To ignore the history of the land entirely'], 0),
    ('Why is it useful for students to learn about the treaty territory they live on?', ['It builds understanding of the land’s history and the people connected to it', 'This knowledge has no relevance to understanding local history', 'A reason unrelated to social studies learning', 'Treaty territories have no connection to where people live today'], 0),
    ('What is one purpose of historic treaties between Indigenous nations and governments?', ['To establish agreements about land, rights, and relationships', 'Treaties have never included any agreements about land', 'A reason unrelated to treaties', 'Treaties exist with no real purpose or effect'], 0)])]),
day(59, [
L('Writing: Writing an Effective Conclusion',
  'Grade 5 Language strand: an effective conclusion sums up the main ideas of a piece of writing and leaves the reader with a final thought, without simply repeating the introduction word for word.',
  [('An effective conclusion should ___.', ['Sum up the main ideas and leave the reader with a final thought', 'Introduce a completely new topic with no connection to the writing', 'A concept unrelated to writing', 'Repeat the introduction word for word'], 0),
   ('Why should a conclusion avoid simply repeating the introduction?', ['A strong conclusion should add a sense of closure or new insight', 'Conclusions are never meant to add anything new', 'A reason unrelated to writing conclusions', 'Repeating the introduction always makes a conclusion stronger'], 0),
   ('Which is an example of a strong closing thought in a conclusion?', ['A reflection on why the topic matters to the reader', 'A brand new fact with no connection to the essay', 'A concept unrelated to conclusions', 'A random change of topic'], 0),
   ('Why is a strong conclusion important in a piece of writing?', ['It leaves a lasting impression and reinforces the writer’s main point', 'A conclusion has no effect on how a piece of writing is remembered', 'A reason unrelated to writing structure', 'Conclusions are an optional part of writing that can be skipped'], 0),
   ('Which of these belongs in a conclusion rather than an introduction?', ['A final thought that ties the main ideas together', 'The very first sentence that introduces the topic', 'A concept unrelated to conclusions', 'A hook meant to grab the reader’s attention at the start'], 0)]),
M('Multiplying and Dividing Integers',
  'Grade 5 Math strand: when multiplying or dividing integers, two numbers with the same sign give a positive result, while two numbers with different signs give a negative result.',
  [('What is -3 × 4?', ['-12', '12', 'A value unrelated to the calculation', '-7'], 0),
   ('What is -6 × -2?', ['12', '-12', 'A value unrelated to the calculation', '-8'], 0),
   ('What is -10 ÷ 2?', ['-5', '5', 'A value unrelated to the calculation', '-8'], 0),
   ('What is -12 ÷ -4?', ['3', '-3', 'A value unrelated to the calculation', '-16'], 0),
   ('When multiplying two integers with different signs, the result is ___.', ['Negative', 'Positive', 'A result unrelated to integer multiplication', 'Always zero'], 0)]),
Sc('The Carbon Cycle',
   'Grade 5 Science strand: the carbon cycle describes how carbon moves between the atmosphere, living things, and the Earth, through processes like photosynthesis, respiration, and decomposition.',
   [('The carbon cycle describes how carbon moves between ___.', ['The atmosphere, living things, and the Earth', 'Only the ocean, with no other locations involved', 'A concept unrelated to the carbon cycle', 'Nowhere at all, since carbon never moves'], 0),
    ('During photosynthesis, plants take in ___ from the atmosphere.', ['Carbon dioxide', 'Oxygen only', 'A gas unrelated to photosynthesis', 'Nitrogen only'], 0),
    ('During respiration, living things release ___ back into the atmosphere.', ['Carbon dioxide', 'Oxygen only', 'A gas unrelated to respiration', 'Nitrogen only'], 0),
    ('Decomposition contributes to the carbon cycle by ___.', ['Releasing carbon stored in dead plants and animals back into the environment', 'Removing all carbon permanently from the environment', 'A process unrelated to the carbon cycle', 'Having no connection to carbon at all'], 0),
    ('Why is understanding the carbon cycle important?', ['It helps explain how carbon supports life and connects to environmental issues like climate change', 'The carbon cycle has no connection to living things or the environment', 'A reason unrelated to science', 'Carbon never plays a role in supporting life on Earth'], 0)]),
SS('Municipal vs. Provincial Elections',
   'Grade 5 Social Studies strand: municipal elections choose local leaders like mayors and councillors, while provincial elections choose representatives who make decisions for the whole province.',
   [('A municipal election chooses leaders who make decisions for ___.', ['A local community or city', 'The entire country', 'A concept unrelated to elections', 'Every province in Canada at once'], 0),
    ('A provincial election chooses representatives who make decisions for ___.', ['The whole province', 'A single neighbourhood only', 'A concept unrelated to elections', 'Every country in the world'], 0),
    ('Which of these would most likely be decided in a municipal election?', ['Who will serve as the city’s mayor', 'Who will serve as the country’s prime minister', 'A concept unrelated to municipal elections', 'Who will represent Canada internationally'], 0),
    ('Which of these would most likely be decided in a provincial election?', ['Who will represent a riding in the provincial legislature', 'Who will be the mayor of a single town', 'A concept unrelated to provincial elections', 'Who will lead a local school council'], 0),
    ('Why is it useful to understand the difference between municipal and provincial elections?', ['It helps citizens understand which level of government handles which responsibilities', 'These two types of elections are always identical in every way', 'A reason unrelated to understanding government', 'Elections have no connection to how decisions are made'], 0)])]),
day(60, [
L('Grammar: Semicolons and Colons',
  'Grade 5 Language strand: a semicolon can join two related independent clauses, while a colon is often used to introduce a list, explanation, or quotation.',
  [('A semicolon can be used to ___.', ['Join two closely related independent clauses', 'Separate every word in a sentence', 'A concept unrelated to punctuation', 'Replace a period at the end of every sentence'], 0),
   ('A colon is often used to ___.', ['Introduce a list, explanation, or quotation', 'Replace a comma in every sentence', 'A concept unrelated to punctuation', 'End a question'], 0),
   ('Which sentence correctly uses a semicolon?', ['I love reading; it helps me relax.', 'I love reading, it helps me relax.', 'A sentence unrelated to semicolon use', 'I love reading; And it helps me relax.'], 0),
   ('Which sentence correctly uses a colon?', ['Bring these items: a pencil, a notebook, and a ruler.', 'Bring these items, a pencil, a notebook, and a ruler.', 'A sentence unrelated to colon use', 'Bring these items; a pencil, a notebook, and a ruler.'], 0),
   ('Why might a writer choose a semicolon instead of starting a new sentence?', ['To show that two ideas are closely connected', 'A semicolon always separates completely unrelated ideas', 'A reason unrelated to punctuation', 'Semicolons are never used to connect ideas'], 0)]),
M('Review: Integers, Algebra, and Data Displays',
  'Grade 5 Math strand: this review lesson revisits key ideas from Days 51-60, including integers, scale drawings, surface area, algebraic expressions, and stem-and-leaf plots.',
  [('An integer can be ___.', ['A positive or negative whole number', 'Only a positive whole number', 'A concept unrelated to integers', 'Only a fraction or decimal'], 0),
   ('A variable in an algebraic expression is ___.', ['A letter that represents an unknown number', 'Always a fixed number that never changes', 'A concept unrelated to algebra', 'A symbol with no mathematical meaning'], 0),
   ('The surface area of a rectangular prism is ___.', ['The total area of all six faces added together', 'The volume of the prism', 'A concept unrelated to surface area', 'The length of just one edge'], 0),
   ('In a stem-and-leaf plot, the “leaf” usually represents ___.', ['The last digit of a number', 'The leading digit(s) of a number', 'A concept unrelated to stem-and-leaf plots', 'The total sum of all data points'], 0),
   ('Why is it useful to review integers, algebra, and data displays together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Body Systems, Structures, and Earth Processes',
   'Grade 5 Science strand: this review lesson revisits key ideas from Days 51-60, including the immune system, bridges, static electricity, plant pollination, and natural disasters.',
   [('The immune system’s main job is to ___.', ['Defend the body against germs and illness', 'Digest food for energy', 'A concept unrelated to the immune system', 'Pump blood throughout the body'], 0),
    ('Load distribution in a bridge refers to how a structure ___.', ['Spreads out weight and forces to remain stable', 'Ignores all forces acting on it', 'A concept unrelated to structures', 'Adds unnecessary weight to itself'], 0),
    ('Objects with the same type of electric charge will ___ each other.', ['Repel', 'Attract', 'An interaction unrelated to charge', 'Have no effect on'], 0),
    ('Pollination is the process by which ___.', ['Pollen is transferred to allow a plant to reproduce', 'A plant absorbs water through its roots', 'A concept unrelated to plant life cycles', 'A seed is planted in the soil'], 0),
    ('Why is it useful to review body systems, structures, and Earth processes together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Culminating Task: A Timeline of Canadian Milestones',
   'Grade 5 Social Studies strand: this culminating task asks students to apply Days 51-60 learning about residential schools, peacekeeping, the Métis Nation, and Canadian government to build a timeline of significant milestones.',
   [('Why might a student include residential schools on a timeline of Canadian milestones?', ['It represents a significant and difficult part of Canada’s history that continues to affect communities today', 'Residential schools have no connection to Canadian history', 'A reason unrelated to this unit', 'Timelines should only include positive events'], 0),
    ('Why might a student include the Red River Resistance on a timeline of Canadian milestones?', ['It reflects an important moment when the Métis Nation defended their rights and land', 'This event has no significance in Canadian history', 'A reason unrelated to this unit', 'Only events from the last ten years belong on a timeline'], 0),
    ('Why might a student include Canada’s peacekeeping missions on a timeline of Canadian milestones?', ['They reflect Canada’s long-standing role in supporting international stability', 'Peacekeeping missions have no connection to Canadian history', 'A reason unrelated to this unit', 'Peacekeeping has never been part of Canada’s history'], 0),
    ('Why might a student include a Supreme Court landmark case on a timeline of Canadian milestones?', ['Landmark cases can shape Canadian law and rights for the whole country', 'Court cases have no lasting effect on Canadian history', 'A reason unrelated to this unit', 'The Supreme Court has never influenced Canadian law'], 0),
    ('Why is building a timeline a valuable way to end this set of Social Studies lessons?', ['It helps students see how different events connect and build Canada’s history over time', 'Timelines never help show connections between historical events', 'A reason unrelated to social studies learning', 'Organizing events chronologically provides no educational benefit'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260731):
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
    _rebalance_answer_positions(g5_51_60)
    append_to(5, g5_51_60)
