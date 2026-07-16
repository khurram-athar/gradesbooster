#!/usr/bin/env python3
"""Phase 3 extension: Grade 7, Days 61-70 (second batch past the Day 50
milestone, continuing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-60 set (see data/grade7.json
and gen_grade7_days51_60.py): the nervous system, fractions operations,
the fur trade, and internet culture through Canada's electoral system.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science & Technology',
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


g7_61_70 = [
day(61, [
L('Reading: Analyzing Author’s Purpose and Craft',
  'Grade 7 Language strand: analyzing an author’s purpose and craft means identifying why a writer chose specific words, structures, or techniques to inform, persuade, or entertain readers.',
  [('An author’s purpose for writing is often to ___.', ['Inform, persuade, or entertain readers', 'Confuse readers with no clear goal', 'A concept unrelated to author’s purpose', 'Avoid any communication with readers'], 0),
   ('Craft in writing refers to ___.', ['The deliberate techniques and choices a writer uses', 'Random word choices with no purpose', 'A concept unrelated to writing craft', 'Only the length of a piece of writing'], 0),
   ('Which is an example of analyzing an author’s craft?', ['Noticing why a writer repeats a phrase for emphasis', 'Ignoring all of the author’s word choices', 'A concept unrelated to analyzing craft', 'Only counting the number of paragraphs'], 0),
   ('If a text mainly explains how something works, its primary purpose is likely to ___.', ['Inform', 'Persuade', 'A purpose unrelated to explanatory texts', 'Entertain'], 0),
   ('Why is it useful for readers to consider an author’s purpose?', ['It helps readers understand why the text was written and how to interpret it', 'Purpose never affects how a text should be read', 'A reason unrelated to reading comprehension', 'Every text has exactly the same purpose'], 0)]),
M('Adding and Subtracting Fractions with Unlike Denominators',
  'Grade 7 Math strand: adding or subtracting fractions with unlike denominators requires finding a common denominator before combining the numerators.',
  [('To add or subtract fractions with unlike denominators, you must first ___.', ['Find a common denominator', 'Add the denominators together', 'A concept unrelated to fraction operations', 'Ignore the denominators completely'], 0),
   ('What is 1/4 + 1/2?', ['3/4', '2/6', 'A value unrelated to the calculation', '1/6'], 0),
   ('What is 2/3 - 1/6?', ['1/2', '1/3', 'A value unrelated to the calculation', '3/9'], 0),
   ('What is the least common denominator of 1/3 and 1/4?', ['12', '7', 'A value unrelated to the calculation', '3'], 0),
   ('Why is a common denominator needed when adding fractions?', ['It ensures the fractions represent equal-sized parts that can be combined accurately', 'Common denominators are never needed for this operation', 'A reason unrelated to fraction operations', 'Denominators never affect how fractions are added'], 0)]),
Sc('The Nervous System: Brain, Spinal Cord, and Neurons',
   'Grade 7 Science strand: the nervous system, made up of the brain, spinal cord, and neurons, controls the body by sending and receiving electrical signals to coordinate actions and responses.',
   [('The nervous system is primarily made up of the brain, spinal cord, and ___.', ['Neurons', 'Red blood cells', 'A structure unrelated to the nervous system', 'Muscle fibres'], 0),
    ('The main function of the nervous system is to ___.', ['Send and receive signals to control the body’s actions and responses', 'Pump blood throughout the body', 'A function unrelated to the nervous system', 'Break down food for digestion'], 0),
    ('A neuron is a specialized cell that ___.', ['Transmits electrical signals throughout the body', 'Produces digestive enzymes', 'A function unrelated to neurons', 'Stores fat for energy'], 0),
    ('Which part of the nervous system acts as the body’s main control centre?', ['The brain', 'The stomach', 'An organ unrelated to the nervous system', 'The skin'], 0),
    ('Why is the spinal cord considered a critical part of the nervous system?', ['It carries signals between the brain and the rest of the body', 'The spinal cord has no connection to sending signals', 'A reason unrelated to the nervous system', 'The spinal cord only affects digestion'], 0)]),
SS('The Fur Trade and Its Impact on Indigenous Peoples and Settlers',
   'Grade 7 Social Studies strand: the fur trade was an early economic system in Canada built on the exchange of furs, which relied heavily on partnerships and knowledge shared between Indigenous peoples and European settlers.',
   [('The fur trade was primarily built on the exchange of ___.', ['Furs, especially beaver pelts, for goods', 'Modern currency for stocks', 'A concept unrelated to the fur trade', 'Land for gold'], 0),
    ('The fur trade relied heavily on partnerships between ___.', ['Indigenous peoples and European settlers', 'Only European countries with each other', 'A concept unrelated to the fur trade', 'Groups with no connection to trade at all'], 0),
    ('Which skill did Indigenous peoples often contribute to the success of the fur trade?', ['Knowledge of the land and trapping techniques', 'No useful skills or knowledge at all', 'A concept unrelated to the fur trade', 'Knowledge of overseas shipping routes only'], 0),
    ('Why did the fur trade have such a significant impact on early Canada?', ['It shaped economic relationships, exploration, and settlement patterns', 'The fur trade had no effect on Canada’s early development', 'A reason unrelated to the fur trade', 'The fur trade only affected European countries directly'], 0),
    ('Why do historians study the fur trade today?', ['It helps explain early relationships between Indigenous peoples and European settlers', 'The fur trade has no historical significance', 'A reason unrelated to Canadian history', 'The fur trade never actually took place in Canada'], 0)])]),
day(62, [
L('Writing: Writing a Business Letter of Complaint or Request',
  'Grade 7 Language strand: a business letter of complaint or request uses formal language and a clear structure to address an issue or ask for action from a company or organization.',
  [('A business letter of complaint should use ___.', ['Formal, polite, and clear language', 'Casual slang and abbreviations', 'A concept unrelated to business letters', 'No greeting or closing at all'], 0),
   ('Which is an appropriate opening for a business letter?', ['Dear Customer Service Manager,', 'Hey there!', 'A greeting unrelated to formal letters', 'Yo,'], 0),
   ('A letter of complaint should clearly state ___.', ['The problem and what resolution is being requested', 'Only compliments about the company', 'A concept unrelated to letters of complaint', 'Nothing specific at all'], 0),
   ('Which closing is appropriate for a formal business letter?', ['Sincerely,', 'See ya,', 'A closing unrelated to formal letters', 'Later,'], 0),
   ('Why is a clear, specific description of the problem important in a complaint letter?', ['It helps the reader understand exactly what needs to be fixed', 'Vague complaints are always more effective', 'A reason unrelated to letter writing', 'Specific details only confuse the reader'], 0)]),
M('Multiplying and Dividing Fractions and Mixed Numbers',
  'Grade 7 Math strand: multiplying fractions involves multiplying numerators and denominators directly, while dividing fractions involves multiplying by the reciprocal of the divisor.',
  [('To multiply two fractions, you ___.', ['Multiply the numerators together and the denominators together', 'Find a common denominator first', 'A concept unrelated to multiplying fractions', 'Add the numerators together'], 0),
   ('What is 1/2 x 2/3?', ['1/3', '2/6', 'A value unrelated to the calculation', '3/5'], 0),
   ('To divide by a fraction, you multiply by its ___.', ['Reciprocal', 'Numerator only', 'A concept unrelated to dividing fractions', 'Denominator squared'], 0),
   ('What is 3/4 ÷ 1/2?', ['3/2', '3/8', 'A value unrelated to the calculation', '1/2'], 0),
   ('How do you convert a mixed number like 2 1/3 into an improper fraction?', ['Multiply the whole number by the denominator and add the numerator', 'Add the whole number and denominator together', 'A method unrelated to mixed numbers', 'Multiply the whole number by the numerator only'], 0)]),
Sc('Volcanoes and Earthquakes: Causes and Effects',
   'Grade 7 Science strand: volcanoes and earthquakes are often caused by the movement of tectonic plates, releasing built-up pressure and energy that can dramatically reshape the Earth’s surface.',
   [('Volcanoes and earthquakes are often caused by ___.', ['The movement of tectonic plates', 'A sudden increase in ocean temperature', 'A concept unrelated to volcanoes and earthquakes', 'Changes in the moon’s orbit'], 0),
    ('An earthquake occurs when ___.', ['Built-up pressure along a fault is suddenly released', 'The Earth’s surface remains perfectly still', 'A concept unrelated to earthquakes', 'Ocean currents shift direction'], 0),
    ('A volcano erupts when ___.', ['Magma and gases escape from beneath the Earth’s surface', 'The Earth’s crust cools and hardens completely', 'A concept unrelated to volcanic eruptions', 'Water evaporates from the ocean'], 0),
    ('Which of these regions is most likely to experience frequent earthquakes and volcanic activity?', ['An area located along a tectonic plate boundary', 'An area located far from any plate boundary', 'A region unrelated to plate boundaries', 'An area with no connection to plate boundaries at all'], 0),
    ('Why do scientists monitor volcanoes and fault lines?', ['To help predict potential eruptions or earthquakes and protect nearby communities', 'Monitoring these areas provides no useful information', 'A reason unrelated to Earth science', 'Volcanoes and fault lines never pose any risk to communities'], 0)]),
SS('The War of 1812: Causes and Consequences',
   'Grade 7 Social Studies strand: the War of 1812 was fought between the United States and Britain (with its colonies, including present-day Canada), shaping early Canadian identity and border relations.',
   [('The War of 1812 was fought between the United States and ___.', ['Britain, including its colonies such as present-day Canada', 'France, alone, with no other countries involved', 'A country unrelated to the War of 1812', 'Spain, alone, with no other countries involved'], 0),
    ('Which of these was a cause of the War of 1812?', ['Trade restrictions and disputes over territory and shipping rights', 'A complete absence of any tension between the countries', 'A cause unrelated to the War of 1812', 'A disagreement about a sporting event'], 0),
    ('How did the War of 1812 affect the identity of early Canadians?', ['It helped strengthen a shared sense of identity in defending their homeland', 'It had no effect on how Canadians viewed themselves', 'A reason unrelated to Canadian identity', 'It caused Canada to become part of the United States'], 0),
    ('Which of these was a result of the War of 1812?', ['The border between the United States and British North America remained largely unchanged', 'The United States gained full control over all of British North America', 'A result unrelated to the War of 1812', 'All trade between the two nations ended permanently'], 0),
    ('Why is the War of 1812 an important event in Canadian history?', ['It played a role in shaping early Canadian identity and relations with the United States', 'The War of 1812 has no connection to Canadian history', 'A reason unrelated to its historical significance', 'The war had no lasting effects of any kind'], 0)])]),
day(63, [
L('Grammar: Correcting Run-on Sentences and Comma Splices',
  'Grade 7 Language strand: a run-on sentence incorrectly joins two independent clauses with no punctuation, while a comma splice incorrectly joins them with only a comma; both can be fixed with a period, semicolon, or conjunction.',
  [('A run-on sentence occurs when ___.', ['Two independent clauses are joined with no punctuation', 'A sentence is too short to make sense', 'A concept unrelated to run-on sentences', 'A sentence has only one clause'], 0),
   ('A comma splice occurs when ___.', ['Two independent clauses are joined by only a comma', 'A sentence uses too many commas correctly', 'A concept unrelated to comma splices', 'A sentence has no clauses at all'], 0),
   ('Which is a correct way to fix a comma splice?', ['Replace the comma with a semicolon or add a conjunction', 'Remove all punctuation from the sentence', 'A method unrelated to fixing comma splices', 'Add another comma splice'], 0),
   ('Which sentence is a run-on?', ['I finished my homework I went outside to play', 'I finished my homework, and I went outside to play.', 'A sentence unrelated to run-ons', 'I finished my homework before I went outside.'], 0),
   ('Why is it important to fix run-on sentences and comma splices?', ['They can confuse readers about where one idea ends and another begins', 'These errors never affect a reader’s understanding', 'A reason unrelated to grammar', 'Run-on sentences are always the correct way to write'], 0)]),
M('Order of Operations with Integers and Exponents (BEDMAS Deeper Dive)',
  'Grade 7 Math strand: the order of operations (BEDMAS) determines the sequence for evaluating expressions with brackets, exponents, division, multiplication, addition, and subtraction, including those with integers.',
  [('BEDMAS stands for the order: ___.', ['Brackets, Exponents, Division/Multiplication, Addition/Subtraction', 'Addition, Subtraction, Multiplication, Division', 'An order unrelated to BEDMAS', 'Exponents, Brackets, Subtraction, Addition'], 0),
   ('Evaluate: 3 + 4 x 2.', ['11', '14', 'A value unrelated to the calculation', '10'], 0),
   ('Evaluate: (2 + 3)².', ['25', '13', 'A value unrelated to the calculation', '10'], 0),
   ('Evaluate: -2 + (-3) x 2.', ['-8', '-10', 'A value unrelated to the calculation', '2'], 0),
   ('Why must operations be completed in a specific order?', ['Without a consistent order, the same expression could give multiple different, incorrect answers', 'Order of operations never affects the result of a calculation', 'A reason unrelated to BEDMAS', 'Expressions can be solved in any order with the same result'], 0)]),
Sc('Magnetism and Electromagnets',
   'Grade 7 Science strand: magnetism is a force that attracts certain materials, such as iron, and an electromagnet is a temporary magnet created when electric current flows through a coiled wire.',
   [('Magnetism is a force that attracts materials such as ___.', ['Iron', 'Wood', 'A material unrelated to magnetism', 'Plastic'], 0),
    ('An electromagnet is created when ___.', ['Electric current flows through a coiled wire', 'A permanent magnet is placed in water', 'A concept unrelated to electromagnets', 'A material is heated to a very high temperature'], 0),
    ('Unlike a permanent magnet, an electromagnet’s magnetism can be ___.', ['Turned on and off by controlling the electric current', 'Never changed once created', 'A concept unrelated to electromagnets', 'Increased only by cooling it down'], 0),
    ('Which of these could increase the strength of an electromagnet?', ['Increasing the number of coils of wire', 'Removing the electric current entirely', 'A concept unrelated to electromagnets', 'Using a material that does not conduct electricity'], 0),
    ('Why are electromagnets useful in devices like electric motors and doorbells?', ['Their magnetism can be controlled and adjusted using electricity', 'Electromagnets provide no practical use in technology', 'A reason unrelated to electromagnets', 'Electromagnets cannot be used in any electrical device'], 0)]),
SS('The Red River Resistance and Louis Riel',
   'Grade 7 Social Studies strand: the Red River Resistance was led by Louis Riel and the Métis people to protect their land, rights, and way of life as Canada expanded westward in the late 1800s.',
   [('The Red River Resistance was led by ___.', ['Louis Riel and the Métis people', 'A group with no connection to the Métis', 'A group unrelated to the Red River Resistance', 'A group opposed to protecting any land rights'], 0),
    ('The Red River Resistance occurred largely in response to ___.', ['Canada’s westward expansion threatening Métis land and rights', 'A sudden decrease in Canada’s population', 'A cause unrelated to the Red River Resistance', 'An unrelated international conflict'], 0),
    ('The Métis people are often described as having ___.', ['Mixed Indigenous and European ancestry', 'No connection to Indigenous or European heritage', 'Ancestry unrelated to Canadian history', 'Ancestry entirely unrelated to Canada’s history'], 0),
    ('Why is Louis Riel considered a significant figure in Canadian history?', ['He led efforts to protect Métis rights and land during a period of major change', 'He played no role in Canadian history', 'A reason unrelated to his historical significance', 'He opposed all forms of Métis representation'], 0),
    ('Why do students study the Red River Resistance today?', ['It highlights the struggles for Indigenous and Métis rights during Canada’s expansion', 'This event has no connection to understanding Canadian history', 'A reason unrelated to social studies learning', 'The Red River Resistance never actually took place'], 0)])]),
day(64, [
L('Vocabulary: Homophones and Homographs',
  'Grade 7 Language strand: homophones are words that sound alike but have different meanings and spellings, while homographs are spelled the same but may have different meanings and pronunciations.',
  [('Homophones are words that ___.', ['Sound alike but have different meanings and spellings', 'Are spelled identically but sound different', 'A concept unrelated to homophones', 'Have the exact same meaning as one another'], 0),
   ('Which pair of words are homophones?', ['There and their', 'Run and jog', 'A pair unrelated to homophones', 'Happy and sad'], 0),
   ('A homograph is a word that ___.', ['Is spelled the same as another word but may differ in meaning or pronunciation', 'Always sounds completely different from other words', 'A concept unrelated to homographs', 'Has only one possible meaning'], 0),
   ('Which word is a homograph, having two different pronunciations and meanings?', ['Lead (to guide) and lead (the metal)', 'Cat and dog', 'A pair unrelated to homographs', 'Happy and joyful'], 0),
   ('Why can homophones be tricky for writers?', ['They are easy to confuse because they sound the same but are spelled differently', 'Homophones are always spelled identically', 'A reason unrelated to vocabulary', 'Homophones never cause any confusion in writing'], 0)]),
M('Volume and Surface Area of Pyramids and Cones',
  'Grade 7 Math strand: the volume of a pyramid or cone is one-third the volume of a prism or cylinder with the same base and height, and their surface area includes the base plus the slanted lateral surface.',
  [('The volume of a pyramid or cone is ___ the volume of a prism or cylinder with the same base and height.', ['One-third', 'Exactly the same as', 'A fraction unrelated to this relationship', 'Three times'], 0),
   ('The formula for the volume of a cone is ___.', ['(1/3)πr²h', 'πr²h', 'A formula unrelated to the volume of a cone', '2πrh'], 0),
   ('The surface area of a pyramid includes ___.', ['The base plus the area of its triangular faces', 'Only the base, with no other surfaces', 'A concept unrelated to surface area', 'Only the height of the pyramid'], 0),
   ('If a cone and a cylinder share the same base and height, and the cylinder’s volume is 90 cm³, what is the cone’s volume?', ['30 cm³', '90 cm³', 'A value unrelated to the calculation', '270 cm³'], 0),
   ('Why might understanding cone and pyramid volume be useful in real life?', ['It helps calculate the capacity of objects like ice cream cones or tents', 'These calculations have no real-world use', 'A reason unrelated to volume', 'Cones and pyramids never have a measurable volume'], 0)]),
Sc('The Greenhouse Effect and Global Climate Change',
   'Grade 7 Science strand: the greenhouse effect occurs when gases in the atmosphere trap heat from the sun, and an increase in these gases from human activity is linked to global climate change.',
   [('The greenhouse effect occurs when gases in the atmosphere ___.', ['Trap heat from the sun near the Earth’s surface', 'Block all sunlight from reaching the Earth', 'A concept unrelated to the greenhouse effect', 'Remove all heat from the atmosphere'], 0),
    ('Which of these is considered a greenhouse gas?', ['Carbon dioxide', 'Oxygen', 'A gas unrelated to the greenhouse effect', 'Nitrogen'], 0),
    ('Which human activity is commonly linked to increased greenhouse gas emissions?', ['Burning fossil fuels', 'Planting large numbers of trees', 'An activity unrelated to greenhouse gases', 'Drinking water'], 0),
    ('A natural greenhouse effect is important because it ___.', ['Keeps the Earth warm enough to support life', 'Makes the Earth too cold to support life', 'A reason unrelated to the greenhouse effect', 'Has no effect on Earth’s temperature'], 0),
    ('Why are scientists concerned about an increase in greenhouse gases from human activity?', ['It can lead to rising global temperatures and significant climate changes', 'Increased greenhouse gases have no effect on global temperatures', 'A reason unrelated to climate change', 'Greenhouse gases only affect a single, isolated location'], 0)]),
SS('Canada’s Territorial Evolution: How the Provinces and Territories Joined',
   'Grade 7 Social Studies strand: Canada’s provinces and territories joined Confederation at different times, gradually expanding the country’s borders from the original four provinces in 1867 to the ten provinces and three territories of today.',
   [('Canada began Confederation in 1867 with how many original provinces?', ['Four', 'Ten', 'A number unrelated to Confederation', 'Thirteen'], 0),
    ('Canada’s territorial evolution refers to ___.', ['How provinces and territories gradually joined the country over time', 'A single event where all provinces joined at once', 'A concept unrelated to Canada’s territorial evolution', 'A process unrelated to Canada’s formation'], 0),
    ('Why might a region have chosen to join Confederation?', ['Economic, political, or security benefits of joining a larger country', 'No benefit was ever offered to any region', 'A reason unrelated to Confederation', 'Regions were required to remain isolated forever'], 0),
    ('How many provinces and territories make up Canada today?', ['Ten provinces and three territories', 'Four provinces and no territories', 'A number unrelated to Canada today', 'Twenty provinces and five territories'], 0),
    ('Why is it useful to study how Canada’s provinces and territories joined over time?', ['It helps explain the country’s political development and regional differences', 'This history has no connection to understanding Canada today', 'A reason unrelated to social studies learning', 'Canada’s borders have never changed since 1867'], 0)])]),
day(65, [
L('Reading: Analyzing Internal and External Conflict',
  'Grade 7 Language strand: internal conflict is a struggle within a character’s own mind, while external conflict is a struggle between a character and an outside force, such as another character or nature.',
  [('Internal conflict is a struggle ___.', ['Within a character’s own mind', 'Between two separate characters', 'A concept unrelated to internal conflict', 'Between a character and the weather'], 0),
   ('External conflict is a struggle between a character and ___.', ['An outside force, such as another character or nature', 'Only their own thoughts and feelings', 'A concept unrelated to external conflict', 'Nothing at all'], 0),
   ('Which is an example of internal conflict?', ['A character struggling to decide between telling the truth or a lie', 'A character fighting against a storm at sea', 'A concept unrelated to internal conflict', 'Two characters arguing over a game'], 0),
   ('Which is an example of external conflict?', ['A character competing against a rival in a race', 'A character silently doubting their own abilities', 'A concept unrelated to external conflict', 'A character reflecting quietly alone'], 0),
   ('Why might an author include both internal and external conflict in a story?', ['It adds depth by showing a character’s inner struggles alongside outside challenges', 'Conflict never adds depth to a story', 'A reason unrelated to narrative writing', 'Stories are always more interesting with no conflict at all'], 0)]),
M('Probability: Combinations and Permutations (Intro)',
  'Grade 7 Math strand: a permutation counts the number of ways items can be arranged when order matters, while a combination counts the number of ways items can be selected when order does not matter.',
  [('A permutation counts arrangements where ___.', ['Order matters', 'Order does not matter at all', 'A concept unrelated to permutations', 'Only one arrangement is ever possible'], 0),
   ('A combination counts selections where ___.', ['Order does not matter', 'Order always matters', 'A concept unrelated to combinations', 'No selection is ever possible'], 0),
   ('How many ways can you arrange the letters A, B, and C in order?', ['6', '3', 'A value unrelated to the calculation', '9'], 0),
   ('If you are choosing 2 fruits from a bowl of apples, bananas, and oranges, and order does not matter, this is an example of a ___.', ['Combination', 'Permutation', 'A concept unrelated to this scenario', 'Ratio'], 0),
   ('Why might the number of permutations of a set be larger than the number of combinations of the same set?', ['Permutations count every different order separately, while combinations group the same items together regardless of order', 'Permutations and combinations always produce the exact same count', 'A reason unrelated to probability', 'Combinations always count more possibilities than permutations'], 0)]),
Sc('Density and Buoyancy',
   'Grade 7 Science strand: density is the amount of mass in a given volume of a substance, and buoyancy explains why objects less dense than a fluid float while denser objects sink.',
   [('Density is defined as ___.', ['The amount of mass in a given volume of a substance', 'The total weight of an object with no reference to volume', 'A concept unrelated to density', 'The temperature of a substance'], 0),
    ('An object will float in water if it is ___.', ['Less dense than water', 'More dense than water', 'A concept unrelated to buoyancy', 'Exactly the same temperature as water'], 0),
    ('An object will sink in water if it is ___.', ['More dense than water', 'Less dense than water', 'A concept unrelated to sinking', 'Perfectly round in shape'], 0),
    ('Which formula correctly represents density?', ['Mass divided by volume', 'Volume divided by mass', 'A formula unrelated to density', 'Mass multiplied by temperature'], 0),
    ('Why can a large steel ship float, even though steel is denser than water?', ['Its overall shape displaces enough water to make its average density less than water', 'Steel always floats regardless of its shape', 'A reason unrelated to buoyancy', 'Ships are not affected by buoyancy at all'], 0)]),
SS('Human Rights: The Universal Declaration and Canadian Protections',
   'Grade 7 Social Studies strand: the Universal Declaration of Human Rights outlines fundamental rights meant to be protected for all people, and Canada upholds many of these rights through its own laws and protections.',
   [('The Universal Declaration of Human Rights outlines rights meant to be protected for ___.', ['All people', 'Only citizens of a single country', 'A group unrelated to human rights', 'Only government leaders'], 0),
    ('Which of these is an example of a fundamental human right?', ['The right to freedom of expression', 'The right to control every other person’s beliefs', 'A concept unrelated to human rights', 'The right to ignore all laws'], 0),
    ('Canada protects many human rights through laws such as ___.', ['The Canadian Charter of Rights and Freedoms', 'A law with no connection to human rights', 'A law unrelated to Canadian rights protections', 'A law that removes protections for citizens'], 0),
    ('Why was the Universal Declaration of Human Rights created after World War II?', ['To help prevent future atrocities by establishing shared international standards for human dignity', 'It was created with no connection to global events', 'A reason unrelated to its historical origins', 'It aimed to reduce cooperation between countries'], 0),
    ('Why is it valuable for students to learn about human rights?', ['It helps them understand the protections and responsibilities that support a fair society', 'Human rights have no connection to understanding society', 'A reason unrelated to social studies learning', 'Human rights are a concept limited to only one country'], 0)])]),
day(66, [
L('Media Literacy: Analyzing Memes and Internet Culture',
  'Grade 7 Language strand: memes use images, text, and humour to quickly spread ideas online, and analyzing them involves considering their intended message, audience, and potential impact.',
  [('A meme typically combines ___.', ['Images, text, and humour to spread an idea quickly', 'Only long paragraphs of formal text', 'A concept unrelated to memes', 'Silence with no message at all'], 0),
   ('When analyzing a meme, it is useful to consider ___.', ['Its intended message, audience, and potential impact', 'Only how many colours it uses', 'A concept unrelated to analyzing memes', 'Nothing, since memes have no meaning'], 0),
   ('Why can memes spread ideas quickly online?', ['They are easy to share, understand, and relate to at a glance', 'Memes are always difficult to understand quickly', 'A reason unrelated to internet culture', 'Memes cannot be shared online'], 0),
   ('Which is a potential concern when analyzing internet culture and memes?', ['Memes can spread misinformation or biased ideas quickly', 'Memes never influence how people think', 'A concept unrelated to media literacy', 'Internet culture has no connection to media literacy'], 0),
   ('Why is media literacy important when engaging with internet culture?', ['It helps people think critically about the messages behind online content', 'Critical thinking is never needed online', 'A reason unrelated to media literacy', 'All online content is equally accurate and reliable'], 0)]),
M('Algebra: Solving Equations Involving Fractions and Decimals',
  'Grade 7 Math strand: solving equations involving fractions or decimals often involves multiplying through by a common denominator or power of ten to clear the fractions or decimals before isolating the variable.',
  [('One strategy for solving an equation with fractions is to ___.', ['Multiply every term by a common denominator to clear the fractions', 'Ignore the fractions completely', 'A concept unrelated to solving equations', 'Add the denominators together first'], 0),
   ('Solve for x: x/2 + 3 = 7.', ['x = 8', 'x = 5', 'A value unrelated to the calculation', 'x = 20'], 0),
   ('Solve for x: 0.5x = 10.', ['x = 20', 'x = 5', 'A value unrelated to the calculation', 'x = 10.5'], 0),
   ('Solve for x: x/3 = 4.', ['x = 12', 'x = 7', 'A value unrelated to the calculation', 'x = 1.33'], 0),
   ('Why might clearing fractions or decimals make an equation easier to solve?', ['It allows the equation to be solved using simpler whole-number operations', 'Clearing fractions or decimals always makes an equation harder to solve', 'A reason unrelated to solving equations', 'Fractions and decimals never affect how an equation is solved'], 0)]),
Sc('Invasive Species and Their Impact on Ecosystems',
   'Grade 7 Science strand: an invasive species is a non-native organism introduced to an ecosystem, often causing harm by outcompeting native species for resources.',
   [('An invasive species is a ___.', ['Non-native organism introduced to an ecosystem', 'Native organism that has always lived in an ecosystem', 'A concept unrelated to invasive species', 'Organism that has no effect on any ecosystem'], 0),
    ('Invasive species often harm ecosystems by ___.', ['Outcompeting native species for food, space, or resources', 'Providing extra resources for every native species', 'A concept unrelated to invasive species', 'Having no interaction with native species at all'], 0),
    ('Which of these is a way an invasive species might be introduced to a new ecosystem?', ['Accidentally transported through international shipping or trade', 'Evolving naturally within that same ecosystem over time', 'A method unrelated to species introduction', 'Appearing with no possible explanation'], 0),
    ('Why can invasive species be especially difficult to control once established?', ['They often lack natural predators in their new environment', 'Invasive species always disappear naturally within a few days', 'A reason unrelated to invasive species', 'Invasive species are never able to survive in a new environment'], 0),
    ('Why do scientists study the impact of invasive species on ecosystems?', ['To better understand and manage the risks they pose to native biodiversity', 'Invasive species have no real impact on ecosystems worth studying', 'A reason unrelated to ecology', 'Studying invasive species provides no useful environmental information'], 0)]),
SS('Canada’s Electoral System and the Voting Process',
   'Grade 7 Social Studies strand: Canada’s electoral system allows citizens to vote for representatives in federal, provincial, and municipal elections, playing a key role in how government leaders are chosen.',
   [('Canada’s electoral system allows citizens to ___.', ['Vote for representatives in government elections', 'Choose their own laws with no representatives at all', 'A concept unrelated to Canada’s electoral system', 'Vote only once in their entire lifetime'], 0),
    ('In a federal election, Canadians vote for a representative in their ___.', ['Riding or constituency', 'Entire province at once', 'A concept unrelated to federal elections', 'Household only'], 0),
    ('Which level of government holds elections for a mayor and city council?', ['Municipal government', 'Federal government', 'A level of government unrelated to city elections', 'No level of government holds these elections'], 0),
    ('Why is voting considered an important civic responsibility?', ['It allows citizens to have a voice in choosing their government representatives', 'Voting has no effect on who leads the government', 'A reason unrelated to civic responsibility', 'Citizens have no role in choosing government leaders'], 0),
    ('Why might it be important for citizens to understand the voting process before an election?', ['It helps ensure they can participate confidently and effectively in choosing their representatives', 'Understanding the voting process has no effect on participation', 'A reason unrelated to voting', 'The voting process is not open to input from citizens'], 0)])]),
day(67, [
L('Writing: Writing a Public Service Announcement (PSA) Script',
  'Grade 7 Language strand: a public service announcement (PSA) script delivers a brief, persuasive message about an important issue, using clear language and a strong call to action aimed at a specific audience.',
  [('A public service announcement (PSA) is designed to ___.', ['Deliver a brief, persuasive message about an important issue', 'Sell a specific product for profit', 'A concept unrelated to PSAs', 'Tell a long fictional story with no clear message'], 0),
   ('A strong PSA typically includes a clear ___.', ['Call to action', 'Random collection of unrelated facts', 'A concept unrelated to PSAs', 'Long list of characters'], 0),
   ('Why should a PSA be written for a specific audience?', ['Tailoring the message helps it connect and resonate with that audience', 'PSAs are always exactly the same for every audience', 'A reason unrelated to writing a PSA', 'Audience has no effect on how a PSA is written'], 0),
   ('Which is an appropriate topic for a PSA?', ['Encouraging people to recycle to protect the environment', 'A fictional adventure story with dragons', 'A concept unrelated to PSA topics', 'A private diary entry with no public message'], 0),
   ('Why is concise, clear language important in a PSA script?', ['PSAs are often short, so the message must be understood quickly', 'PSAs are always very long with no time limit', 'A reason unrelated to writing a PSA', 'Clarity is never important in this type of writing'], 0)]),
M('Data: Line Graphs and Analyzing Trends Over Time',
  'Grade 7 Math strand: a line graph displays how data changes over time, and analyzing its trend involves identifying whether values are increasing, decreasing, or staying constant.',
  [('A line graph is especially useful for showing ___.', ['How data changes over time', 'Only a single data point with no comparison', 'A concept unrelated to line graphs', 'Data with no connection to time at all'], 0),
   ('If a line graph slopes upward from left to right, the trend is ___.', ['Increasing', 'Decreasing', 'A trend unrelated to this description', 'Staying exactly constant'], 0),
   ('If a line graph slopes downward from left to right, the trend is ___.', ['Decreasing', 'Increasing', 'A trend unrelated to this description', 'Impossible to determine'], 0),
   ('A flat, horizontal section of a line graph indicates that the data is ___.', ['Staying constant over that period', 'Increasing rapidly', 'A concept unrelated to line graphs', 'Missing entirely'], 0),
   ('Why might a business analyze trends on a line graph of monthly sales?', ['It helps identify patterns that can inform future planning and decisions', 'Trends on a line graph provide no useful information', 'A reason unrelated to analyzing data', 'Line graphs cannot be used to analyze sales data'], 0)]),
Sc('Biotechnology and Genetic Engineering (Intro)',
   'Grade 7 Science strand: biotechnology uses living organisms or their processes to develop useful products, and genetic engineering involves directly modifying an organism’s DNA for a specific purpose.',
   [('Biotechnology uses ___.', ['Living organisms or their processes to develop useful products', 'Only non-living materials with no biological component', 'A concept unrelated to biotechnology', 'A process unrelated to living organisms'], 0),
    ('Genetic engineering involves ___.', ['Directly modifying an organism’s DNA for a specific purpose', 'Studying an organism’s DNA with no modifications at all', 'A concept unrelated to genetic engineering', 'Removing all DNA from an organism'], 0),
    ('Which of these is an example of a biotechnology application?', ['Developing crops that are more resistant to disease', 'Building a bridge using steel and concrete', 'A concept unrelated to biotechnology', 'Painting a picture of a landscape'], 0),
    ('Why might scientists genetically engineer certain crops?', ['To improve traits like disease resistance or nutritional value', 'Genetic engineering has no effect on a crop’s traits', 'A reason unrelated to genetic engineering', 'To make crops less nutritious on purpose'], 0),
    ('Why is biotechnology an important and sometimes debated topic in science?', ['It raises both potential benefits and ethical questions about modifying living organisms', 'Biotechnology has no real-world applications or implications', 'A reason unrelated to biotechnology', 'Biotechnology is a topic with no connection to ethics or society'], 0)]),
SS('Income Inequality and Wealth Distribution',
   'Grade 7 Social Studies strand: income inequality refers to the uneven distribution of income and wealth within a society, and studying it helps explain economic challenges and opportunities faced by different groups.',
   [('Income inequality refers to ___.', ['The uneven distribution of income and wealth within a society', 'A society where everyone earns exactly the same amount', 'A concept unrelated to income inequality', 'A concept unrelated to economics'], 0),
    ('Which of these could be a cause of income inequality?', ['Unequal access to education and job opportunities', 'Every person having identical access to resources', 'A cause unrelated to income inequality', 'A cause unrelated to economic factors'], 0),
    ('Which of these is a potential effect of significant income inequality?', ['Unequal access to healthcare, housing, or education', 'No effect on any aspect of society', 'An effect unrelated to income inequality', 'Complete economic equality for all citizens'], 0),
    ('Which of these is a policy some governments use to help address income inequality?', ['Progressive taxation, where higher earners pay a higher tax rate', 'A policy that increases inequality on purpose', 'A policy unrelated to income or taxation', 'A policy unrelated to reducing inequality'], 0),
    ('Why is income inequality an important topic to study in social studies?', ['It connects to economics, fairness, and the well-being of communities', 'Income inequality has no connection to social studies topics', 'A reason unrelated to this unit', 'Income inequality is a concern only in fictional scenarios'], 0)])]),
day(68, [
L('Grammar: Using Transitional Phrases to Link Ideas',
  'Grade 7 Language strand: transitional phrases, such as “in addition” or “as a result,” connect ideas within and between paragraphs, helping writing flow logically and clearly.',
  [('Transitional phrases help writing by ___.', ['Connecting ideas logically within and between paragraphs', 'Making ideas more confusing and disconnected', 'A concept unrelated to transitional phrases', 'Removing the need for paragraphs entirely'], 0),
   ('Which phrase could signal a cause-and-effect relationship?', ['As a result', 'In contrast', 'A phrase unrelated to cause and effect', 'For example'], 0),
   ('Which phrase could signal a contrast between two ideas?', ['On the other hand', 'In addition', 'A phrase unrelated to signalling contrast', 'Similarly'], 0),
   ('Which phrase could be used to add a similar or additional idea?', ['In addition', 'However', 'A phrase unrelated to adding ideas', 'Nevertheless'], 0),
   ('Why might a writer use transitional phrases throughout an essay?', ['They guide the reader smoothly from one idea to the next', 'Transitional phrases always make an essay harder to follow', 'A reason unrelated to transitional phrases', 'Ideas never need to be connected in writing'], 0)]),
M('Financial Literacy: Income, Expenses, and Net Worth',
  'Grade 7 Math strand: net worth is calculated by subtracting total expenses or debts from total income or assets, helping individuals understand and track their overall financial position.',
  [('Net worth is calculated by ___.', ['Subtracting total debts from total assets', 'Adding income and expenses together', 'A concept unrelated to net worth', 'Multiplying income by a fixed rate'], 0),
   ('Income refers to ___.', ['Money earned or received, such as from a job', 'Money spent on goods and services', 'A concept unrelated to income', 'A type of debt owed to a bank'], 0),
   ('Expenses refer to ___.', ['Money spent on goods, services, or bills', 'Money earned from working', 'A concept unrelated to expenses', 'A type of savings account'], 0),
   ('If a person has $5,000 in assets and $2,000 in debts, what is their net worth?', ['$3,000', '$7,000', 'A value unrelated to the calculation', '$2,500'], 0),
   ('Why is tracking income and expenses important for financial literacy?', ['It helps individuals understand their financial position and make informed spending decisions', 'Tracking income and expenses provides no useful financial information', 'A reason unrelated to financial literacy', 'Net worth has no connection to income or expenses'], 0)]),
Sc('Groundwater and the Water Table',
   'Grade 7 Science strand: groundwater is water stored beneath the Earth’s surface in soil and rock, and the water table marks the upper boundary of the area saturated with this water.',
   [('Groundwater is water that is stored ___.', ['Beneath the Earth’s surface, in soil and rock', 'Only on the surface of oceans and lakes', 'A concept unrelated to groundwater', 'In clouds high in the atmosphere'], 0),
    ('The water table marks ___.', ['The upper boundary of the area saturated with groundwater', 'The exact centre of the Earth', 'A concept unrelated to the water table', 'The boundary between two oceans'], 0),
    ('Which of these could cause the water table to drop?', ['Excessive pumping of groundwater for human use', 'A significant increase in annual rainfall', 'A cause unrelated to the water table', 'A process unrelated to groundwater levels'], 0),
    ('A well is typically drilled deep enough to reach ___.', ['Below the water table, where groundwater is present', 'Only the very surface of the soil', 'A concept unrelated to wells', 'A location with no connection to groundwater'], 0),
    ('Why is groundwater an important resource to protect from pollution?', ['Many communities rely on it as a source of drinking water', 'Groundwater has no connection to drinking water supplies', 'A reason unrelated to groundwater', 'Pollution never affects groundwater quality'], 0)]),
SS('Urban vs. Rural Life in Canada',
   'Grade 7 Social Studies strand: urban areas are densely populated with access to many services, while rural areas have lower population density and often rely more on agriculture or natural resources, creating distinct lifestyles across Canada.',
   [('Urban areas are generally characterized by ___.', ['Dense populations and many available services', 'Very low populations with few services', 'A concept unrelated to urban areas', 'A complete absence of any people'], 0),
    ('Rural areas often rely more heavily on ___.', ['Agriculture or natural resources', 'Only large corporate offices', 'A concept unrelated to rural economies', 'A resource unrelated to rural economies'], 0),
    ('Which of these might be a challenge faced by people living in rural areas?', ['Longer travel distances to access certain services', 'An overwhelming number of nearby services', 'A challenge unrelated to rural areas', 'No connection to distance or access at all'], 0),
    ('Which of these might be a challenge faced by people living in urban areas?', ['Higher cost of living and traffic congestion', 'A complete absence of any nearby services', 'A challenge unrelated to urban areas', 'No population at all'], 0),
    ('Why is it useful to compare urban and rural life in Canada?', ['It helps explain how geography and population affect people’s daily lives and opportunities', 'Urban and rural life are always identical in every way', 'A reason unrelated to social studies learning', 'Comparing these areas has no relevance to social studies'], 0)])]),
day(69, [
L('Reading: Evaluating an Author’s Credentials and Expertise',
  'Grade 7 Language strand: evaluating an author’s credentials and expertise involves considering their background, training, and experience to judge how reliable their claims about a topic might be.',
  [('An author’s credentials refer to their ___.', ['Background, training, and experience related to a topic', 'Favourite hobbies with no connection to the topic', 'A concept unrelated to author credentials', 'Physical appearance'], 0),
   ('Why might a reader check an author’s expertise before trusting their claims?', ['Expertise can indicate how reliable and well-informed the author’s claims are likely to be', 'An author’s background never affects how reliable their claims are', 'A reason unrelated to evaluating sources', 'All authors are equally reliable regardless of expertise'], 0),
   ('Which is an example of a credential that might support an author’s expertise on a medical topic?', ['Years of experience working as a doctor', 'A hobby unrelated to medicine', 'A concept unrelated to medical expertise', 'No connection to the medical field at all'], 0),
   ('Why might a text written by someone with no relevant expertise be viewed with more caution?', ['The claims may be less informed or less reliable without proper background knowledge', 'Expertise never matters when evaluating a text', 'A reason unrelated to evaluating a text', 'A lack of expertise always makes a text more trustworthy'], 0),
   ('Why is evaluating an author’s credentials an important reading skill?', ['It helps readers judge how much trust to place in a text’s claims', 'This skill has no effect on understanding a text', 'A reason unrelated to reading comprehension', 'Every author’s claims should be trusted equally without question'], 0)]),
M('Geometry: Constructing Triangles and Angle Bisectors',
  'Grade 7 Math strand: triangles can be constructed using given side lengths or angles, and an angle bisector is a line that divides an angle into two equal parts.',
  [('An angle bisector divides an angle into ___.', ['Two equal parts', 'Three equal parts', 'A concept unrelated to angle bisectors', 'Four unequal parts'], 0),
   ('To construct a triangle given three side lengths, a compass is often used to ___.', ['Mark equal distances from given points', 'Measure the temperature of the triangle', 'A concept unrelated to triangle construction', 'Draw a circle unrelated to the triangle'], 0),
   ('If an angle measures 60 degrees, its bisector creates two angles of ___ each.', ['30 degrees', '60 degrees', 'A value unrelated to the calculation', '15 degrees'], 0),
   ('Which set of side lengths could NOT form a triangle?', ['2 cm, 2 cm, and 10 cm', '5 cm, 6 cm, and 7 cm', 'A set unrelated to triangle construction', '3 cm, 4 cm, and 5 cm'], 0),
   ('Why might construction tools like a compass and straightedge be used in geometry?', ['They allow for precise, accurate constructions of shapes and angles', 'These tools never help with accuracy in geometry', 'A reason unrelated to geometric construction', 'Constructions can always be done more accurately by estimating'], 0)]),
Sc('The Integumentary System: Skin, Hair, and Nails',
   'Grade 7 Science strand: the integumentary system, made up of the skin, hair, and nails, protects the body from injury and infection while helping regulate body temperature.',
   [('The integumentary system is made up of the skin, hair, and ___.', ['Nails', 'Bones', 'A structure unrelated to the integumentary system', 'Blood vessels only'], 0),
    ('One main function of the skin is to ___.', ['Protect the body from injury and infection', 'Pump blood throughout the body', 'A function unrelated to the skin', 'Digest food for the body'], 0),
    ('The skin helps regulate body temperature through processes such as ___.', ['Sweating', 'Digesting food', 'A process unrelated to temperature regulation', 'Filtering air for the lungs'], 0),
    ('Which of these is a function of hair on the human body?', ['Providing some protection and insulation', 'Pumping blood through the body', 'A function unrelated to hair', 'Breaking down food in the stomach'], 0),
    ('Why is the integumentary system considered the body’s first line of defence?', ['It forms a protective barrier between the body and the outside environment', 'This system has no protective function at all', 'A reason unrelated to the integumentary system', 'The integumentary system is located entirely inside the body'], 0)]),
SS('Canada’s Mining and Natural Resource Industries',
   'Grade 7 Social Studies strand: Canada’s mining and natural resource industries extract valuable materials like minerals and metals, playing a significant role in the economy while raising important questions about environmental impact.',
   [('Canada’s mining industry primarily focuses on extracting ___.', ['Minerals and metals', 'Only water resources', 'A concept unrelated to mining', 'A resource unrelated to mining'], 0),
    ('Why are mining and natural resource industries significant to Canada’s economy?', ['They provide jobs and generate significant economic activity', 'These industries provide no economic benefit at all', 'A reason unrelated to Canada’s economy', 'They have no connection to Canada’s economy'], 0),
    ('Which of these is a potential environmental concern related to mining?', ['Disruption of ecosystems and habitats near mining sites', 'Mining always improves the surrounding environment', 'A concern unrelated to mining', 'Mining has no possible environmental impact'], 0),
    ('Why might governments regulate mining and resource extraction?', ['To help balance economic benefits with environmental and community protection', 'Regulations provide no benefit to the environment or communities', 'A reason unrelated to resource regulation', 'Mining requires no regulation of any kind'], 0),
    ('Why is it useful for students to learn about Canada’s natural resource industries?', ['It helps them understand economic development alongside environmental responsibility', 'Natural resource industries have no connection to understanding Canada', 'A reason unrelated to social studies learning', 'This topic is not relevant to social studies learning'], 0)])]),
day(70, [
L('Review: Language Skills (Days 61-69)',
  'Grade 7 Language strand: this review lesson revisits key ideas from Days 61-69, including author’s purpose, business letters, run-on sentences, homophones, conflict, memes, PSAs, transitions, and author credibility.',
  [('An author’s purpose for writing is often to ___.', ['Inform, persuade, or entertain readers', 'Confuse readers with no clear goal', 'A concept unrelated to author’s purpose', 'Avoid any communication with readers'], 0),
   ('A run-on sentence occurs when ___.', ['Two independent clauses are joined with no punctuation', 'A sentence is too short to make sense', 'A concept unrelated to run-on sentences', 'A sentence has only one clause'], 0),
   ('Internal conflict is a struggle ___.', ['Within a character’s own mind', 'Between two separate characters', 'A concept unrelated to internal conflict', 'Between a character and the weather'], 0),
   ('Transitional phrases help writing by ___.', ['Connecting ideas logically within and between paragraphs', 'Making ideas more confusing and disconnected', 'A concept unrelated to transitional phrases', 'Removing the need for paragraphs entirely'], 0),
   ('Why is it useful to review purpose, structure, grammar, and evaluation skills together?', ['It reinforces how these language skills work together for effective reading and writing', 'These skills have no connection to each other', 'A reason unrelated to reviewing language skills', 'Review never helps strengthen understanding of language'], 0)]),
M('Review: Math Skills (Days 61-69)',
  'Grade 7 Math strand: this review lesson revisits key ideas from Days 61-69, including fraction operations, order of operations, pyramid and cone volume, combinations and permutations, and financial literacy.',
  [('What is 1/4 + 1/2?', ['3/4', '2/6', 'A value unrelated to the calculation', '1/6'], 0),
   ('Evaluate: 3 + 4 x 2.', ['11', '14', 'A value unrelated to the calculation', '10'], 0),
   ('A permutation counts arrangements where ___.', ['Order matters', 'Order does not matter at all', 'A concept unrelated to permutations', 'Only one arrangement is ever possible'], 0),
   ('Net worth is calculated by ___.', ['Subtracting total debts from total assets', 'Adding income and expenses together', 'A concept unrelated to net worth', 'Multiplying income by a fixed rate'], 0),
   ('Why is it useful to review fraction operations, order of operations, geometry, probability, and finance together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of math'], 0)]),
Sc('Review: Science Skills (Days 61-69)',
   'Grade 7 Science strand: this review lesson revisits key ideas from Days 61-69, including the nervous system, volcanoes and earthquakes, magnetism, the greenhouse effect, and biotechnology.',
   [('The nervous system is primarily made up of the brain, spinal cord, and ___.', ['Neurons', 'Red blood cells', 'A structure unrelated to the nervous system', 'Muscle fibres'], 0),
    ('Volcanoes and earthquakes are often caused by ___.', ['The movement of tectonic plates', 'A sudden increase in ocean temperature', 'A concept unrelated to volcanoes and earthquakes', 'Changes in the moon’s orbit'], 0),
    ('The greenhouse effect occurs when gases in the atmosphere ___.', ['Trap heat from the sun near the Earth’s surface', 'Block all sunlight from reaching the Earth', 'A concept unrelated to the greenhouse effect', 'Remove all heat from the atmosphere'], 0),
    ('Genetic engineering involves ___.', ['Directly modifying an organism’s DNA for a specific purpose', 'Studying an organism’s DNA with no modifications at all', 'A concept unrelated to genetic engineering', 'Removing all DNA from an organism'], 0),
    ('Why is it useful to review body systems, Earth processes, and emerging technologies together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing science', 'Review is never useful in science'], 0)]),
SS('Review: Social Studies Skills (Days 61-69)',
   'Grade 7 Social Studies strand: this review lesson revisits key ideas from Days 61-69, including the fur trade, the War of 1812, the Red River Resistance, Confederation’s expansion, human rights, and Canada’s electoral system.',
   [('The fur trade was primarily built on the exchange of ___.', ['Furs, especially beaver pelts, for goods', 'Modern currency for stocks', 'A concept unrelated to the fur trade', 'Land for gold'], 0),
    ('The Red River Resistance was led by ___.', ['Louis Riel and the Métis people', 'A group with no connection to the Métis', 'A group unrelated to the Red River Resistance', 'A group opposed to protecting any land rights'], 0),
    ('The Universal Declaration of Human Rights outlines rights meant to be protected for ___.', ['All people', 'Only citizens of a single country', 'A group unrelated to human rights', 'Only government leaders'], 0),
    ('Canada’s electoral system allows citizens to ___.', ['Vote for representatives in government elections', 'Choose their own laws with no representatives at all', 'A concept unrelated to Canada’s electoral system', 'Vote only once in their entire lifetime'], 0),
    ('Why is it useful to review Canadian history, rights, and government together?', ['It reinforces how these interconnected historical and political topics shaped modern Canada', 'These topics have no connection to one another', 'A reason unrelated to reviewing social studies', 'Review is never useful when studying history and government'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260814):
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
    _rebalance_answer_positions(g7_61_70)
    append_to(7, g7_61_70)
