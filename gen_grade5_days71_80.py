#!/usr/bin/env python3
"""Phase 3 extension: Grade 5, Days 71-80 (continuing past the Day 70
milestone toward the full 157-day year). Topics chosen to avoid any
overlap with the existing Day 1-70 set (see data/grade5.json):
heat transfer, simple machines (wheel/axle, inclined plane), electrical
conductors/insulators, vertebrates/invertebrates, soil formation, sound
pitch/frequency, cloud types, insects, groundwater, plus Language and
Math topics such as irony, subject-verb agreement, diary-entry writing,
homophones/homographs, multi-digit multiplication, LCM/GCF, volume of
rectangular prisms, and Social Studies topics such as the Klondike Gold
Rush, bilingualism, the Governor General, Canadian currency, the history
of transportation, provincial legislatures, the Atlantic fishing
industry, charities, and the Franklin Expedition.

Subject keys for Grade 5 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 5 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
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


g5_71_80 = [
day(71, [
L('Reading: Understanding Irony',
  'Grade 5 Language strand: irony occurs when there is a difference between what is expected to happen and what actually happens, or between what is said and what is truly meant.',
  [('Irony occurs when there is a difference between what is expected and ___.', ['What actually happens', 'What always happens exactly as planned', 'A concept unrelated to irony', 'A synonym for exactly what is expected'], 0),
   ('Which is an example of irony?', ['A fire station burning down', 'A fire station opening on time', 'A concept unrelated to irony', 'A weather report that is always accurate'], 0),
   ('Verbal irony occurs when a speaker says ___.', ['The opposite of what they truly mean', 'Exactly what they truly mean', 'A concept unrelated to verbal irony', 'Nothing at all'], 0),
   ('Why might an author use irony in a story?', ['To create humour or emphasize a surprising contrast', 'Irony never affects how a reader experiences a story', 'A reason unrelated to irony', 'To make the plot completely predictable'], 0),
   ('How is irony different from simply describing an unexpected event?', ['Irony highlights a meaningful contrast between expectation and reality', 'Irony and unexpected events are exactly the same thing', 'A concept unrelated to irony', 'Irony only occurs in nonfiction texts'], 0)]),
M('Multiplying Two-Digit Numbers',
  'Grade 5 Math strand: multiplying two two-digit numbers involves breaking the numbers into tens and ones, multiplying each part, and adding the partial products together.',
  [('When multiplying two two-digit numbers using the standard algorithm, each digit of one number is multiplied by ___.', ['Each digit of the other number', 'Only the ones digit of the other number', 'A concept unrelated to multiplication', 'Only the first digit of the same number'], 0),
   ('What is 23 x 14?', ['322', '312', 'A value unrelated to the calculation', '342'], 0),
   ('What is 32 x 21?', ['672', '662', 'A value unrelated to the calculation', '640'], 0),
   ('What are the partial products of 12 x 13 when broken into tens and ones (10+2) x (10+3)?', ['100, 30, 20, and 6', 'Only one product with no breakdown', 'A concept unrelated to partial products', '12 and 13 added together'], 0),
   ('Why might breaking a multiplication problem into tens and ones make it easier to solve?', ['It turns one large multiplication into smaller, simpler steps', 'Breaking numbers apart never makes multiplication easier', 'A reason unrelated to multiplication strategies', 'It changes the answer to the problem'], 0)]),
Sc('Heat Transfer: Conduction, Convection, and Radiation',
   'Grade 5 Science strand: heat energy moves from warmer objects to cooler ones through conduction, convection, and radiation, each involving a different method of transfer.',
   [('Conduction is the transfer of heat through ___.', ['Direct contact between objects', 'Empty space with no matter involved', 'A concept unrelated to heat transfer', 'Sound waves travelling through air'], 0),
    ('Convection is the transfer of heat through the movement of ___.', ['A liquid or a gas', 'A solid object only', 'A concept unrelated to convection', 'Light rays only'], 0),
    ('Radiation is the transfer of heat through ___.', ['Waves that can travel through empty space', 'Direct contact between two solids only', 'A concept unrelated to radiation', 'Only cold objects'], 0),
    ('Which is an example of conduction?', ['Heat moving from a hot stove into a metal pot touching it', 'Heat from the sun reaching Earth through space', 'A concept unrelated to conduction', 'Warm air rising in a room'], 0),
    ('Why does heat generally move from a warmer object to a cooler one?', ['Heat naturally flows toward areas with less thermal energy until they balance out', 'Heat never moves between objects of different temperatures', 'A reason unrelated to heat transfer', 'Cooler objects always transfer heat to warmer ones'], 0)]),
SS('The Klondike Gold Rush',
   'Grade 5 Social Studies strand: the Klondike Gold Rush of the late 1890s drew thousands of prospectors to the Yukon in search of gold, shaping the growth and history of northern Canada.',
   [('The Klondike Gold Rush drew thousands of prospectors to the ___.', ['Yukon', 'Prairies', 'A region unrelated to the Klondike Gold Rush', 'Atlantic coast'], 0),
    ('What resource were prospectors searching for during the Klondike Gold Rush?', ['Gold', 'Oil', 'A resource unrelated to the Klondike Gold Rush', 'Coal'], 0),
    ('The Klondike Gold Rush mainly took place during which decade?', ['The 1890s', 'The 1950s', 'A decade unrelated to the Klondike Gold Rush', 'The 1700s'], 0),
    ('How did the Klondike Gold Rush affect the growth of towns in the Yukon?', ['It caused towns such as Dawson City to grow quickly as prospectors arrived', 'The Gold Rush had no effect on any towns in the Yukon', 'A reason unrelated to the Klondike Gold Rush', 'It caused every town in the Yukon to shrink and disappear'], 0),
    ('Why is the Klondike Gold Rush an important event in Canadian history?', ['It shaped the settlement and development of northern Canada', 'The event had no lasting impact on Canadian history', 'A reason unrelated to Canadian history', 'It only affected countries outside of Canada'], 0)])]),
day(72, [
L('Grammar: Subject-Verb Agreement',
  'Grade 5 Language strand: subject-verb agreement means a singular subject takes a singular verb, and a plural subject takes a plural verb, so the two match in a sentence.',
  [('Subject-verb agreement means the subject and verb in a sentence must ___.', ['Match in number, singular or plural', 'Always be in the past tense', 'A concept unrelated to subject-verb agreement', 'Always start with a capital letter'], 0),
   ('Which sentence shows correct subject-verb agreement?', ['The dogs run in the park.', 'The dogs runs in the park.', 'A sentence unrelated to subject-verb agreement', 'The dog run in the park.'], 0),
   ('In the sentence “She ___ to school every day,” which verb correctly completes it?', ['Walks', 'Walk', 'A word unrelated to this sentence', 'Walking'], 0),
   ('Why is subject-verb agreement important in writing?', ['It helps sentences read clearly and sound grammatically correct', 'Subject-verb agreement has no effect on how a sentence reads', 'A reason unrelated to grammar', 'Verbs never need to match their subject'], 0),
   ('Which subject requires a plural verb?', ['The children', 'The child', 'A subject unrelated to subject-verb agreement', 'One student'], 0)]),
M('Long Division: Interpreting Remainders',
  'Grade 5 Math strand: when a division problem does not divide evenly, the leftover amount is called the remainder, and how it is interpreted depends on the real-world context of the problem.',
  [('A remainder is the amount left over when a number ___.', ['Does not divide evenly into equal groups', 'Divides evenly with nothing left over', 'A concept unrelated to remainders', 'Is multiplied by another number'], 0),
   ('What is 17 divided by 5, expressed with a remainder?', ['3 remainder 2', '3 remainder 5', 'A value unrelated to the calculation', '4 remainder 1'], 0),
   ('If 23 stickers are shared equally among 4 friends, how many whole stickers does each friend get, and how many are left over?', ['5 stickers each, with 3 left over', '4 stickers each, with 5 left over', 'A result unrelated to the calculation', '6 stickers each, with 1 left over'], 0),
   ('If 26 students need to travel in vans that hold 6 students each, how many vans are needed to fit everyone, including the leftover students?', ['5 vans', '4 vans', 'A number unrelated to the calculation', '6 vans'], 0),
   ('Why might a remainder sometimes need to be rounded up in a real-world problem, such as the vans example?', ['Because the leftover people or items still need to be accounted for', 'Remainders should always be ignored in real-world problems', 'A reason unrelated to interpreting remainders', 'Rounding up always gives an incorrect answer'], 0)]),
Sc('Simple Machines: The Wheel and Axle and the Inclined Plane',
   'Grade 5 Science strand: a wheel and axle reduces the force needed to move an object by rotating together, while an inclined plane is a sloped surface that reduces the force needed to raise an object.',
   [('A wheel and axle reduces the force needed to move an object by ___.', ['Rotating together as a single unit', 'Staying completely still', 'A concept unrelated to the wheel and axle', 'Cutting the object into smaller pieces'], 0),
    ('An inclined plane is best described as a ___.', ['Sloped surface that makes it easier to raise a load', 'Flat surface with no slope at all', 'A concept unrelated to inclined planes', 'Wheel that spins around an axle'], 0),
    ('Which of these is an example of a wheel and axle?', ['A doorknob', 'A ramp leading up to a doorway', 'A concept unrelated to the wheel and axle', 'A pair of scissors'], 0),
    ('Which of these is an example of an inclined plane?', ['A ramp used to load a truck', 'A steering wheel on a car', 'A concept unrelated to inclined planes', 'A pair of pliers'], 0),
    ('Why might a ramp make it easier to move a heavy object to a higher place?', ['It spreads the work over a longer distance, reducing the force needed at any moment', 'A ramp always requires more force than lifting straight up', 'A reason unrelated to inclined planes', 'Ramps have no effect on the force needed to move an object'], 0)]),
SS('Bilingualism and Canada’s Official Languages',
   'Grade 5 Social Studies strand: Canada has two official languages, English and French, and government services at the federal level are available in both languages.',
   [('Canada’s two official languages are ___.', ['English and French', 'English and Spanish', 'A pair of languages unrelated to Canada’s official languages', 'French and Mandarin'], 0),
    ('Federal government services in Canada must be available in ___.', ['Both official languages', 'Only one official language', 'A concept unrelated to bilingualism', 'No particular language'], 0),
    ('Which Canadian province is officially bilingual?', ['New Brunswick', 'A province unrelated to official bilingualism', 'British Columbia', 'Alberta'], 0),
    ('Why might a country choose to have more than one official language?', ['To reflect and respect the languages and history of its diverse population', 'Having more than one official language offers no benefit to a country', 'A reason unrelated to bilingualism', 'Countries are never allowed to have more than one official language'], 0),
    ('Why is it useful for students to learn about Canada’s official languages?', ['It helps them understand an important part of Canadian identity and government', 'Official languages have no connection to Canadian identity', 'A reason unrelated to social studies learning', 'Canada has never had more than one language spoken'], 0)])]),
day(73, [
L('Writing: Writing a Diary Entry from a Character’s Perspective',
  'Grade 5 Language strand: a diary entry written from a character’s perspective uses first-person voice to express that character’s thoughts, feelings, and experiences about events in a story.',
  [('A diary entry written from a character’s perspective is written in ___.', ['First-person voice', 'Third-person voice', 'A concept unrelated to diary entries', 'A voice with no clear perspective at all'], 0),
   ('What might a diary entry from a character’s perspective include?', ['The character’s private thoughts and feelings about events', 'Only a list of facts with no personal feelings included', 'A concept unrelated to diary entries', 'Information the character could not possibly know'], 0),
   ('Why is writing in first person useful for a diary entry?', ['It allows the writer to express a character’s personal thoughts directly', 'First person can never be used for diary entries', 'A reason unrelated to writing a diary entry', 'First person always describes events from an outside narrator'], 0),
   ('Which is an example of a sentence that might appear in a character’s diary entry?', ['Today I felt nervous walking into the new school for the first time.', 'The character walked into the new school on Monday morning.', 'A sentence unrelated to diary entries', 'The story takes place in a small town.'], 0),
   ('Why might writing a diary entry from a character’s point of view help a reader understand a story better?', ['It offers insight into the character’s inner thoughts and emotions', 'Diary entries never help a reader understand a character better', 'A reason unrelated to writing diary entries', 'Diary entries only describe events with no personal feelings'], 0)]),
M('Comparing and Ordering Decimals',
  'Grade 5 Math strand: comparing and ordering decimals involves lining up the decimal points and comparing digits from left to right, starting with the largest place value.',
  [('When comparing decimals, it helps to first ___.', ['Line up the decimal points', 'Ignore the decimal points completely', 'A step unrelated to comparing decimals', 'Round every decimal to a whole number'], 0),
   ('Which decimal is greater: 0.45 or 0.5?', ['0.5', '0.45', 'Both are exactly equal', 'A value unrelated to the comparison'], 0),
   ('Which list of decimals is ordered from least to greatest?', ['0.2, 0.35, 0.8', '0.8, 0.35, 0.2', 'A list unrelated to the comparison', '0.35, 0.2, 0.8'], 0),
   ('Which decimal is smaller: 0.6 or 0.09?', ['0.09', '0.6', 'Both are exactly equal', 'A value unrelated to the comparison'], 0),
   ('Why might someone need to compare decimals in real life?', ['To compare prices or measurements that include cents or fractional units', 'Comparing decimals never applies to real-life situations', 'A reason unrelated to decimals', 'Decimals are only used in advanced scientific research'], 0)]),
Sc('Electrical Conductors and Insulators',
   'Grade 5 Science strand: an electrical conductor allows electric current to pass through it easily, such as metal, while an insulator resists the flow of electric current, such as rubber or plastic.',
   [('An electrical conductor is a material that ___.', ['Allows electric current to pass through it easily', 'Blocks electric current from passing through', 'A concept unrelated to conductors', 'Has no connection to electricity at all'], 0),
    ('An electrical insulator is a material that ___.', ['Resists the flow of electric current', 'Allows electric current to flow through it easily', 'A concept unrelated to insulators', 'Always generates its own electricity'], 0),
    ('Which of these materials is a good electrical conductor?', ['Copper', 'Rubber', 'A material unrelated to electrical conductivity', 'Wood'], 0),
    ('Which of these materials is a good electrical insulator?', ['Plastic', 'Copper', 'A material unrelated to electrical insulation', 'Aluminum'], 0),
    ('Why are electrical cords often covered in a material like rubber or plastic?', ['To insulate the wire and protect people from electric shock', 'Rubber and plastic make the wire conduct more electricity', 'A reason unrelated to electrical safety', 'Covering a cord has no effect on electrical safety'], 0)]),
SS('The Role of the Governor General',
   'Grade 5 Social Studies strand: the Governor General is the representative of the Crown in Canada, performing ceremonial duties and formally approving new laws passed by Parliament.',
   [('The Governor General is the representative of ___ in Canada.', ['The Crown', 'A foreign government', 'A concept unrelated to the Governor General', 'A political party'], 0),
    ('One duty of the Governor General is to ___.', ['Formally approve new laws passed by Parliament', 'Vote in every federal election', 'A concept unrelated to the Governor General', 'Lead a political party in Parliament'], 0),
    ('Which of these best describes the Governor General’s role?', ['Largely ceremonial, representing the Crown at official events', 'A role with no connection to Canadian government', 'The elected leader of the government', 'A role identical to the Prime Minister’s'], 0),
    ('Who recommends the appointment of the Governor General?', ['The Prime Minister', 'A vote from all Canadian citizens', 'A concept unrelated to this appointment', 'A foreign country’s leader'], 0),
    ('Why is it useful for students to learn about the role of the Governor General?', ['It helps them understand Canada’s system of government and its ties to the Crown', 'The Governor General has no connection to Canadian government', 'A reason unrelated to social studies learning', 'The role of Governor General no longer exists'], 0)])]),
day(74, [
L('Vocabulary: Homophones and Homographs',
  'Grade 5 Language strand: homophones are words that sound alike but have different spellings and meanings, while homographs are spelled the same but can have different meanings and sometimes different pronunciations.',
  [('Homophones are words that ___.', ['Sound alike but have different spellings and meanings', 'Are spelled exactly the same and mean the same thing', 'A concept unrelated to homophones', 'Always begin with the same letter'], 0),
   ('Which pair of words are homophones?', ['Their and there', 'Happy and sad', 'A pair of words unrelated to homophones', 'Run and running'], 0),
   ('Homographs are words that ___.', ['Are spelled the same but can have different meanings', 'Always sound completely different from each other', 'A concept unrelated to homographs', 'Are always opposite in meaning'], 0),
   ('Which sentence uses the word “bow” as a homograph, where its meaning depends on context?', ['She wore a bow in her hair, then took a bow after the play.', 'A sentence unrelated to homographs', 'She ran quickly to the store.', 'He read the entire book in one day.'], 0),
   ('Why is it important for readers to understand homophones and homographs?', ['To choose the correct spelling and meaning based on context', 'These words never cause any confusion for readers', 'A reason unrelated to vocabulary', 'Homophones and homographs mean exactly the same thing'], 0)]),
M('Least Common Multiple and Greatest Common Factor',
  'Grade 5 Math strand: the least common multiple is the smallest number that two numbers both divide into evenly, while the greatest common factor is the largest number that divides evenly into both numbers.',
  [('The least common multiple of two numbers is the smallest number that ___.', ['Both numbers divide into evenly', 'Is smaller than both numbers', 'A concept unrelated to least common multiple', 'Only one of the numbers divides into evenly'], 0),
   ('What is the least common multiple of 4 and 6?', ['12', '24', 'A value unrelated to the calculation', '10'], 0),
   ('The greatest common factor of two numbers is the largest number that ___.', ['Divides evenly into both numbers', 'Is greater than both numbers', 'A concept unrelated to greatest common factor', 'Cannot divide into either number'], 0),
   ('What is the greatest common factor of 12 and 18?', ['6', '3', 'A value unrelated to the calculation', '12'], 0),
   ('Why might the greatest common factor be useful when simplifying a fraction?', ['It shows the largest number that can divide both the numerator and denominator evenly', 'The greatest common factor has no connection to simplifying fractions', 'A reason unrelated to this math skill', 'It can only be used with even numbers'], 0)]),
Sc('Vertebrates and Invertebrates',
   'Grade 5 Science strand: vertebrates are animals with a backbone, such as fish and mammals, while invertebrates are animals without a backbone, such as insects and worms.',
   [('A vertebrate is an animal that has a ___.', ['Backbone', 'Shell only', 'A concept unrelated to vertebrates', 'Set of wings'], 0),
    ('An invertebrate is an animal that ___.', ['Does not have a backbone', 'Always has a backbone', 'A concept unrelated to invertebrates', 'Cannot move at all'], 0),
    ('Which of these animals is a vertebrate?', ['A fish', 'A worm', 'A concept unrelated to vertebrates', 'An insect'], 0),
    ('Which of these animals is an invertebrate?', ['A spider', 'A bird', 'A concept unrelated to invertebrates', 'A reptile'], 0),
    ('Why might scientists group animals into vertebrates and invertebrates?', ['It helps organize and compare animals based on a shared physical feature', 'This grouping provides no useful information about animals', 'A reason unrelated to classifying animals', 'All animals belong to exactly the same group'], 0)]),
SS('Canada’s Currency and Its Symbols',
   'Grade 5 Social Studies strand: Canada’s currency includes coins and bills featuring symbols such as the loon on the one-dollar coin, reflecting the country’s history, wildlife, and identity.',
   [('Canada’s one-dollar coin is nicknamed the ___ because of the bird pictured on it.', ['Loonie', 'Toonie', 'A name unrelated to Canadian currency', 'Beaver dollar'], 0),
    ('Canadian currency includes coins and ___.', ['Paper or polymer bills', 'Only gold bars', 'A concept unrelated to Canadian currency', 'Items with no value at all'], 0),
    ('Why might Canadian currency feature images such as wildlife or historical figures?', ['To reflect the country’s history, culture, and identity', 'Currency images have no connection to a country’s identity', 'A reason unrelated to Canadian currency', 'Currency designs are chosen completely at random'], 0),
    ('What is the name of Canada’s central bank, responsible for issuing currency?', ['The Bank of Canada', 'A bank unrelated to Canadian currency', 'A private company with no government connection', 'A bank located in another country'], 0),
    ('Why is it useful for students to learn about the symbols on Canadian currency?', ['It helps them understand how currency reflects national identity and history', 'Currency symbols have no meaning behind them', 'A reason unrelated to social studies learning', 'Canadian currency has never featured any symbols'], 0)])]),
day(75, [
L('Reading: Main Idea and Supporting Details',
  'Grade 5 Language strand: the main idea is the central point a text is making, while supporting details are the specific facts, examples, or reasons that explain and back up that main idea.',
  [('The main idea of a text is ___.', ['The central point the text is making', 'A minor detail mentioned only once', 'A concept unrelated to reading comprehension', 'The very last sentence of the text, always'], 0),
   ('Supporting details in a text ___.', ['Provide facts or examples that explain the main idea', 'Have no connection to the main idea at all', 'A concept unrelated to supporting details', 'Always contradict the main idea'], 0),
   ('Which is an example of a supporting detail for the main idea “Recycling helps protect the environment”?', ['Recycling paper reduces the number of trees that need to be cut down', 'A sentence with no connection to recycling', 'A concept unrelated to supporting details', 'The weather was sunny on Tuesday'], 0),
   ('Why is it useful for readers to identify the main idea of a text?', ['It helps them understand the central point the author is making', 'Identifying the main idea never helps with understanding a text', 'A reason unrelated to reading comprehension', 'The main idea is always stated in the title only'], 0),
   ('How can a reader use supporting details to find the main idea?', ['By noticing what several details have in common and what point they support', 'Supporting details never provide any clues about the main idea', 'A reason unrelated to identifying the main idea', 'By ignoring all the details in the text'], 0)]),
M('Data Management: Surveys, Tally Charts, and Frequency Tables',
  'Grade 5 Math strand: a survey collects information by asking people questions, and the results can be recorded using tally charts and organized into frequency tables before being displayed as a graph.',
  [('A survey collects information by ___.', ['Asking people questions', 'Measuring temperature with a thermometer', 'A concept unrelated to surveys', 'Reading a story from beginning to end'], 0),
   ('A tally chart is used to ___.', ['Record how many times each response occurs', 'Show only the final average of the data', 'A concept unrelated to tally charts', 'Draw a picture of the data collected'], 0),
   ('A frequency table organizes data by showing ___.', ['How often each value or category occurs', 'Only the largest value collected', 'A concept unrelated to frequency tables', 'A single result with no other information'], 0),
   ('If a tally chart shows 10 marks grouped in fives plus 2 more marks for a category, how many responses does that represent?', ['12', '10', 'A value unrelated to the calculation', '9'], 0),
   ('Why might someone organize survey data into a frequency table before making a graph?', ['It makes the data easier to read and turn into a graph', 'Organizing data into a table never helps with making a graph', 'A reason unrelated to data management', 'Frequency tables can only be used with numbers larger than 100'], 0)]),
Sc('Soil Composition and Formation',
   'Grade 5 Science strand: soil forms over long periods of time as rock breaks down through weathering and mixes with decayed plant and animal matter, called humus.',
   [('Soil forms as rock breaks down through a process called ___.', ['Weathering', 'Photosynthesis', 'A concept unrelated to soil formation', 'Evaporation'], 0),
    ('Humus, an important part of soil, is made up of ___.', ['Decayed plant and animal matter', 'Pure water with no other materials', 'A concept unrelated to soil composition', 'Melted rock from a volcano'], 0),
    ('Why does soil formation typically take a very long time?', ['Rock breaks down gradually through weathering over many years', 'Soil forms instantly with no time required at all', 'A reason unrelated to soil formation', 'Weathering has no connection to how soil forms'], 0),
    ('Which of these is a component commonly found in soil?', ['Minerals from broken-down rock', 'Only liquid water with nothing else mixed in', 'A component unrelated to soil', 'Pure oxygen gas'], 0),
    ('Why is healthy soil important for growing plants?', ['It provides nutrients, water, and support for plant roots', 'Soil has no connection to how plants grow', 'A reason unrelated to soil health', 'Plants can grow equally well with no soil at all'], 0)]),
SS('The History of Transportation in Canada',
   'Grade 5 Social Studies strand: transportation in Canada has changed over time, from canoes and horse-drawn wagons to railways, automobiles, and airplanes, shaping how people and goods move across the country.',
   [('Before railways and cars, Indigenous peoples and early settlers in Canada often travelled by ___.', ['Canoe', 'Airplane', 'A method unrelated to early transportation', 'Subway'], 0),
    ('How did railways change transportation in Canada?', ['They allowed people and goods to travel long distances more quickly', 'Railways made travel across Canada impossible', 'A reason unrelated to Canadian transportation history', 'Railways had no effect on how goods were moved'], 0),
    ('Which mode of transportation became common in Canada during the twentieth century, changing how people travelled locally?', ['The automobile', 'The canoe', 'A mode unrelated to twentieth-century transportation', 'The horse-drawn wagon, exclusively'], 0),
    ('Why is transportation important to Canada’s development as a country?', ['It connects communities and helps move people and goods across long distances', 'Transportation has no connection to how a country develops', 'A reason unrelated to Canadian history', 'Canada has never needed methods of transportation'], 0),
    ('Why might studying the history of transportation help students understand Canada’s growth?', ['It shows how new technology changed how people lived, worked, and travelled', 'The history of transportation has no connection to a country’s growth', 'A reason unrelated to social studies learning', 'Transportation methods have never changed throughout Canadian history'], 0)])]),
day(76, [
L('Figurative Language: Imagery',
  'Grade 5 Language strand: imagery is descriptive language that appeals to the five senses, helping readers picture, hear, smell, taste, or feel what is happening in a text.',
  [('Imagery is descriptive language that appeals to ___.', ['The five senses', 'Only the sense of sight', 'A concept unrelated to imagery', 'Only numbers and statistics'], 0),
   ('Which sentence is a strong example of imagery?', ['The crisp autumn air smelled of woodsmoke and fallen leaves.', 'The season was autumn.', 'A sentence unrelated to imagery', 'It was a certain time of year.'], 0),
   ('Why might a writer use imagery in a story?', ['To help readers vividly picture or experience a scene', 'Imagery never helps a reader picture a scene', 'A reason unrelated to imagery', 'To make a text shorter and less detailed'], 0),
   ('Which sense does the phrase “the rough bark of the old oak tree” appeal to?', ['Touch', 'Taste', 'A sense unrelated to this phrase', 'Hearing'], 0),
   ('How is imagery different from simply stating a fact?', ['Imagery uses descriptive, sensory language rather than a plain statement', 'Imagery and stating a fact are exactly the same thing', 'A concept unrelated to imagery', 'Facts always include vivid sensory description'], 0)]),
M('Multiplying Decimals by Powers of Ten',
  'Grade 5 Math strand: multiplying a decimal by a power of ten, such as 10, 100, or 1000, moves the decimal point to the right the same number of places as there are zeros.',
  [('When multiplying a decimal by 10, the decimal point moves ___.', ['One place to the right', 'One place to the left', 'A direction unrelated to this rule', 'Two places to the left'], 0),
   ('What is 3.4 x 10?', ['34', '3.4', 'A value unrelated to the calculation', '340'], 0),
   ('What is 2.75 x 100?', ['275', '27.5', 'A value unrelated to the calculation', '2.75'], 0),
   ('What is 0.6 x 1000?', ['600', '60', 'A value unrelated to the calculation', '6'], 0),
   ('Why is it useful to know the pattern for multiplying decimals by powers of ten?', ['It allows for quick mental math without needing long multiplication', 'This pattern never applies to multiplying decimals', 'A reason unrelated to this math skill', 'It only works with whole numbers, not decimals'], 0)]),
Sc('Sound: Pitch and Frequency',
   'Grade 5 Science strand: pitch is how high or low a sound seems, and it is determined by frequency, the number of sound wave vibrations that occur each second.',
   [('Pitch describes how ___ a sound seems.', ['High or low', 'Loud or quiet', 'A concept unrelated to pitch', 'Long or short'], 0),
    ('Frequency refers to ___.', ['The number of sound wave vibrations occurring each second', 'The loudness of a sound only', 'A concept unrelated to frequency', 'The colour of a sound wave'], 0),
    ('A sound with a higher frequency has a ___ pitch.', ['Higher', 'Lower', 'A description unrelated to pitch', 'Completely silent'], 0),
    ('Which of these is likely to produce a higher-pitched sound?', ['A small, tightly stretched guitar string', 'A large, loosely stretched guitar string', 'A concept unrelated to pitch', 'An object that is not vibrating at all'], 0),
    ('Why might a shorter vibrating object generally produce a higher pitch than a longer one?', ['It vibrates faster, producing a higher frequency', 'Shorter objects always vibrate more slowly than longer ones', 'A reason unrelated to pitch and frequency', 'The length of an object never affects the pitch it produces'], 0)]),
SS('Provincial Legislatures and the Role of the Premier',
   'Grade 5 Social Studies strand: each Canadian province has its own legislature that makes provincial laws, led by a premier, the head of the provincial government.',
   [('A provincial legislature is responsible for making laws at the ___ level.', ['Provincial', 'Federal', 'A level unrelated to provincial legislatures', 'International'], 0),
    ('The head of a provincial government is called the ___.', ['Premier', 'Prime Minister', 'A title unrelated to provincial government', 'Governor General'], 0),
    ('Which of these is typically a responsibility handled at the provincial level in Canada?', ['Education and healthcare', 'National defence', 'A responsibility unrelated to provincial government', 'Printing national currency'], 0),
    ('How does the role of a premier differ from the role of the Prime Minister?', ['A premier leads a provincial government, while the Prime Minister leads the federal government', 'A premier and the Prime Minister have exactly the same role', 'A concept unrelated to Canadian government', 'The Prime Minister only leads one province'], 0),
    ('Why does Canada have both federal and provincial levels of government?', ['To divide responsibilities between national and regional issues', 'Having multiple levels of government serves no purpose', 'A reason unrelated to Canadian government', 'Only one level of government exists in Canada'], 0)])]),
day(77, [
L('Writing: Procedural Writing (How-To Instructions)',
  'Grade 5 Language strand: procedural writing gives step-by-step instructions in a clear sequence, often using numbered steps and precise, action-oriented language so a reader can complete a task.',
  [('Procedural writing gives instructions in ___.', ['A clear, step-by-step sequence', 'A random order with no particular sequence', 'A concept unrelated to procedural writing', 'A single long paragraph with no steps'], 0),
   ('Why do procedural texts often use numbered steps?', ['To show the reader the exact order actions should be completed', 'Numbered steps make instructions harder to follow', 'A reason unrelated to procedural writing', 'Numbers are never used in procedural writing'], 0),
   ('Which sentence is an example of procedural writing?', ['First, pour the flour into a large bowl.', 'The bakery was famous for its fresh bread.', 'A sentence unrelated to procedural writing', 'The bread smelled wonderful as it baked.'], 0),
   ('Why is precise, action-oriented language important in procedural writing?', ['It helps the reader understand exactly what action to take', 'Precise language makes instructions more confusing', 'A reason unrelated to procedural writing', 'Procedural writing should always be vague'], 0),
   ('Which of these is a common example of procedural writing?', ['A recipe explaining how to bake a cake', 'A poem describing a sunset', 'A concept unrelated to procedural writing', 'A diary entry about a school day'], 0)]),
M('Comparing and Ordering Fractions',
  'Grade 5 Math strand: comparing and ordering fractions involves finding a common denominator or using benchmarks, such as one-half, to determine which fraction is greater or smaller.',
  [('One way to compare two fractions with different denominators is to first find a ___.', ['Common denominator', 'Common numerator only', 'A concept unrelated to comparing fractions', 'Whole number with no fraction involved'], 0),
   ('Which fraction is greater: 3/4 or 1/2?', ['3/4', '1/2', 'Both are exactly equal', 'A value unrelated to the comparison'], 0),
   ('Which fraction is smaller: 2/5 or 3/5?', ['2/5', '3/5', 'Both are exactly equal', 'A value unrelated to the comparison'], 0),
   ('Which list of fractions is ordered from least to greatest?', ['1/4, 1/2, 3/4', '3/4, 1/2, 1/4', 'A list unrelated to the comparison', '1/2, 1/4, 3/4'], 0),
   ('Why might using a benchmark such as one-half help when comparing fractions?', ['It gives a quick reference point to judge whether a fraction is greater or less than half', 'Benchmarks never help when comparing fractions', 'A reason unrelated to comparing fractions', 'One-half can only be used when comparing whole numbers'], 0)]),
Sc('Types of Clouds and Weather Prediction',
   'Grade 5 Science strand: different cloud types, such as cumulus, stratus, and cirrus, form in different conditions and can give clues about upcoming weather.',
   [('Cumulus clouds are typically described as ___.', ['Puffy and cotton-like', 'Thin and wispy', 'A description unrelated to cumulus clouds', 'Flat sheets covering the entire sky'], 0),
    ('Stratus clouds typically form as ___.', ['Flat, grey layers covering much of the sky', 'Tall, narrow columns reaching into space', 'A description unrelated to stratus clouds', 'Bright, colourful patches'], 0),
    ('Cirrus clouds are typically found ___.', ['High in the atmosphere and appear thin and wispy', 'Very close to the ground', 'A description unrelated to cirrus clouds', 'Only during a thunderstorm'], 0),
    ('Which cloud type is often associated with an approaching storm?', ['Dark, towering cumulonimbus clouds', 'Thin, wispy cirrus clouds', 'A cloud type unrelated to storms', 'Clear skies with no clouds at all'], 0),
    ('Why might observing clouds help people predict upcoming weather?', ['Different cloud types are linked to different weather conditions', 'Clouds have no connection to weather conditions', 'A reason unrelated to weather prediction', 'Weather can never be predicted by observing the sky'], 0)]),
SS('The Fishing Industry in Atlantic Canada',
   'Grade 5 Social Studies strand: the Atlantic provinces have long relied on the fishing industry, harvesting species such as cod and lobster from the ocean, which has shaped the region’s economy and communities.',
   [('The fishing industry has long been an important part of the economy in ___.', ['Atlantic Canada', 'The Prairie provinces', 'A region unrelated to the fishing industry', 'Northern Ontario'], 0),
    ('Which of these is a species commonly harvested by the Atlantic fishing industry?', ['Lobster', 'A species unrelated to Atlantic fishing', 'Wheat', 'Corn'], 0),
    ('Why might a decline in fish populations, such as cod, seriously affect Atlantic coastal communities?', ['Many jobs and local economies depend on the fishing industry', 'A decline in fish populations has no effect on coastal communities', 'A reason unrelated to the fishing industry', 'Coastal communities never rely on fishing for their economy'], 0),
    ('The fishing industry is considered part of which type of industry?', ['A primary industry that gathers a natural resource', 'A secondary industry that manufactures goods', 'A concept unrelated to fishing', 'A tertiary industry that only provides services'], 0),
    ('Why is it useful for students to learn about the fishing industry in Atlantic Canada?', ['It helps them understand how geography shapes a region’s economy and communities', 'The fishing industry has no connection to Atlantic Canada', 'A reason unrelated to social studies learning', 'Fishing has never taken place in Atlantic Canada'], 0)])]),
day(78, [
L('Reading: Skimming and Scanning for Information',
  'Grade 5 Language strand: skimming means quickly reading a text to get a general idea of its content, while scanning means quickly looking through a text to find specific information.',
  [('Skimming a text means reading it quickly to ___.', ['Get a general idea of its content', 'Memorize every single word', 'A concept unrelated to skimming', 'Find one specific fact only'], 0),
   ('Scanning a text means looking through it quickly to ___.', ['Find specific information', 'Understand every detail in depth', 'A concept unrelated to scanning', 'Read the text extremely slowly'], 0),
   ('Which situation is a good example of scanning?', ['Looking through a phone book to find one specific name', 'Reading a novel slowly from cover to cover', 'A concept unrelated to scanning', 'Memorizing an entire poem word for word'], 0),
   ('Why might a reader skim a chapter before reading it in detail?', ['To get a general sense of what the chapter is about before reading closely', 'Skimming never helps a reader prepare to read a text', 'A reason unrelated to skimming', 'Skimming always replaces the need to read a text closely'], 0),
   ('Why are skimming and scanning useful research skills?', ['They help readers find and understand information quickly and efficiently', 'These skills never help with finding information quickly', 'A reason unrelated to research skills', 'Skimming and scanning mean exactly the same thing'], 0)]),
M('Rounding Whole Numbers to a Given Place Value',
  'Grade 5 Math strand: rounding a whole number to a given place value involves looking at the digit to the right of that place to decide whether to round up or keep the digit the same.',
  [('When rounding a number, you look at the digit ___ the place value you are rounding to.', ['Immediately to the right of', 'Immediately to the left of', 'A position unrelated to rounding', 'Two places to the left of'], 0),
   ('What is 452 rounded to the nearest ten?', ['450', '460', 'A value unrelated to the calculation', '400'], 0),
   ('What is 3,675 rounded to the nearest hundred?', ['3,700', '3,600', 'A value unrelated to the calculation', '3,680'], 0),
   ('What is 8,249 rounded to the nearest thousand?', ['8,000', '9,000', 'A value unrelated to the calculation', '8,200'], 0),
   ('Why might someone round a large number instead of using its exact value?', ['To make the number easier to work with or estimate quickly', 'Rounding a number always makes a problem harder to solve', 'A reason unrelated to rounding', 'Rounding is only useful for very small numbers'], 0)]),
Sc('Insects and Their Characteristics',
   'Grade 5 Science strand: insects are a group of invertebrates with three main body parts -- the head, thorax, and abdomen -- along with six legs and, in most species, wings.',
   [('An insect’s body is divided into three main parts: the head, thorax, and ___.', ['Abdomen', 'Backbone', 'A body part unrelated to insects', 'Shell'], 0),
    ('How many legs does a typical insect have?', ['Six', 'Eight', 'A number unrelated to insects', 'Four'], 0),
    ('Which of these is classified as an insect?', ['An ant', 'A spider', 'A concept unrelated to insects', 'A worm'], 0),
    ('Why are spiders not classified as insects, even though both are invertebrates?', ['Spiders have eight legs and two main body parts, unlike an insect’s six legs and three body parts', 'Spiders and insects have exactly the same body structure', 'A reason unrelated to classifying insects', 'Spiders are actually a type of vertebrate'], 0),
    ('Why might scientists study the characteristics that define an insect?', ['It helps them accurately classify and compare different invertebrate species', 'Studying insect characteristics provides no useful scientific information', 'A reason unrelated to classifying living things', 'All invertebrates are classified as insects'], 0)]),
SS('Charities and Non-Profit Organizations in Canada',
   'Grade 5 Social Studies strand: charities and non-profit organizations work to support communities by addressing needs such as poverty, health, and education, relying on donations and volunteers rather than earning profit for owners.',
   [('A non-profit organization is one that ___.', ['Does not earn profit for owners, instead using funds to support its cause', 'Exists only to earn as much profit as possible', 'A concept unrelated to non-profit organizations', 'Is required to shut down after one year'], 0),
    ('Charities often rely on ___ to fund their work.', ['Donations and volunteers', 'Only government-owned businesses', 'A concept unrelated to charities', 'Money earned exclusively from selling stocks'], 0),
    ('Which of these is an example of a cause a charity might support?', ['Providing food for families in need', 'Increasing profits for a private company’s shareholders', 'A concept unrelated to charitable causes', 'Selling products for maximum personal gain'], 0),
    ('Why might volunteers be important to the work of a non-profit organization?', ['They provide time and effort to help the organization carry out its mission', 'Volunteers have no role in how a non-profit organization operates', 'A reason unrelated to non-profit organizations', 'Non-profit organizations never rely on the help of others'], 0),
    ('Why is it useful for students to learn about charities and non-profit organizations?', ['It helps them understand how communities support people in need', 'Charities have no connection to supporting communities', 'A reason unrelated to social studies learning', 'Non-profit organizations do not exist in Canada'], 0)])]),
day(79, [
L('Grammar: Pronoun-Antecedent Agreement',
  'Grade 5 Language strand: an antecedent is the noun a pronoun refers to, and pronoun-antecedent agreement means the pronoun must match its antecedent in number and gender.',
  [('An antecedent is the noun that a ___ refers to.', ['Pronoun', 'Verb', 'A part of speech unrelated to antecedents', 'Adjective'], 0),
   ('Pronoun-antecedent agreement means the pronoun must match its antecedent in ___.', ['Number and gender', 'Only its spelling', 'A concept unrelated to pronoun-antecedent agreement', 'Only the number of syllables'], 0),
   ('In the sentence “Maria lost her book,” what is the antecedent of the pronoun “her”?', ['Maria', 'Book', 'A word unrelated to this sentence', 'Lost'], 0),
   ('Which sentence shows correct pronoun-antecedent agreement?', ['The students packed their bags.', 'The students packed his bag.', 'A sentence unrelated to pronoun-antecedent agreement', 'The student packed their bags, referring incorrectly to only one student.'], 0),
   ('Why is pronoun-antecedent agreement important in writing?', ['It helps make sentences clear by matching pronouns correctly to the nouns they replace', 'This agreement has no effect on how clear a sentence is', 'A reason unrelated to grammar', 'Pronouns never need to match the nouns they replace'], 0)]),
M('Volume of Rectangular Prisms',
  'Grade 5 Math strand: the volume of a rectangular prism is found by multiplying its length, width, and height, giving the amount of space inside the three-dimensional shape.',
  [('The volume of a rectangular prism is found by multiplying its ___.', ['Length, width, and height', 'Length and width only', 'A concept unrelated to volume', 'Only its height'], 0),
   ('What is the volume of a rectangular prism with a length of 4 cm, a width of 3 cm, and a height of 2 cm?', ['24 cubic centimetres', '9 cubic centimetres', 'A value unrelated to the calculation', '12 cubic centimetres'], 0),
   ('Volume is measured in ___.', ['Cubic units', 'Square units', 'A unit unrelated to volume', 'Linear units only'], 0),
   ('What is the volume of a rectangular prism with a length of 5 m, a width of 2 m, and a height of 3 m?', ['30 cubic metres', '10 cubic metres', 'A value unrelated to the calculation', '15 cubic metres'], 0),
   ('Why might knowing how to calculate volume be useful in real life?', ['It helps determine how much space is inside a container or room', 'Calculating volume never applies to real-life situations', 'A reason unrelated to volume', 'Volume can only be used for two-dimensional shapes'], 0)]),
Sc('Groundwater and the Water Table',
   'Grade 5 Science strand: groundwater is water stored beneath the Earth’s surface in soil and rock, and the water table is the upper level at which the ground becomes saturated with water.',
   [('Groundwater is water stored ___.', ['Beneath the Earth’s surface in soil and rock', 'Only in oceans and lakes', 'A concept unrelated to groundwater', 'Only inside clouds'], 0),
    ('The water table is the upper level at which the ground becomes ___.', ['Saturated with water', 'Completely dry', 'A concept unrelated to the water table', 'Covered in ice'], 0),
    ('A well is used to access ___.', ['Groundwater stored beneath the surface', 'Only rainwater falling from the sky', 'A concept unrelated to wells', 'Water located in outer space'], 0),
    ('Why might the level of the water table change over time?', ['Amounts of rainfall and water usage can cause it to rise or fall', 'The water table always stays at exactly the same level', 'A reason unrelated to groundwater', 'The water table has no connection to rainfall'], 0),
    ('Why is groundwater an important resource for many communities?', ['It can be a source of drinking water and water for farming', 'Groundwater has no practical use for communities', 'A reason unrelated to groundwater', 'Communities never rely on groundwater for any purpose'], 0)]),
SS('The Franklin Expedition and Arctic Exploration',
   'Grade 5 Social Studies strand: the Franklin Expedition of the 1840s was a British attempt to find a Northwest Passage through the Arctic that ended in disaster, and its story remains an important part of Arctic exploration history.',
   [('The Franklin Expedition set out in the 1840s to search for a ___.', ['Northwest Passage through the Arctic', 'A gold mine in the Yukon', 'A concept unrelated to the Franklin Expedition', 'New farming region in the Prairies'], 0),
    ('What ultimately happened to the ships and crew of the Franklin Expedition?', ['They became trapped in ice and the entire crew was lost', 'The expedition successfully returned home with no difficulties', 'A concept unrelated to the Franklin Expedition', 'The crew immediately turned back before entering the Arctic'], 0),
    ('Why is the Northwest Passage significant to explorers historically?', ['It was seen as a possible shipping route connecting the Atlantic and Pacific oceans through the Arctic', 'It has no connection to trade or exploration', 'A reason unrelated to Arctic exploration', 'It was believed to be located in Europe'], 0),
    ('How did Inuit oral history contribute to understanding the fate of the Franklin Expedition?', ['Inuit accounts provided important clues that helped later searches locate the wrecked ships', 'Inuit oral history had no connection to the Franklin Expedition', 'A reason unrelated to Arctic exploration', 'Only written British records were ever used to study the expedition'], 0),
    ('Why is the story of the Franklin Expedition still studied today?', ['It offers insight into the risks of Arctic exploration and Canada’s Arctic history', 'The expedition has no lasting significance to Canadian history', 'A reason unrelated to Arctic exploration', 'The expedition took place outside of Arctic Canada'], 0)])]),
day(80, [
L('Review: Irony, Subject-Verb Agreement, Imagery, and Pronoun Agreement',
  'Grade 5 Language strand: this review lesson revisits key ideas from Days 71-79, including irony, subject-verb agreement, imagery, and pronoun-antecedent agreement.',
  [('Irony occurs when there is a difference between what is expected and ___.', ['What actually happens', 'What always happens exactly as planned', 'A concept unrelated to irony', 'A synonym for exactly what is expected'], 0),
   ('Subject-verb agreement means the subject and verb in a sentence must ___.', ['Match in number, singular or plural', 'Always be in the past tense', 'A concept unrelated to subject-verb agreement', 'Always start with a capital letter'], 0),
   ('Imagery is descriptive language that appeals to ___.', ['The five senses', 'Only the sense of sight', 'A concept unrelated to imagery', 'Only numbers and statistics'], 0),
   ('Pronoun-antecedent agreement means the pronoun must match its antecedent in ___.', ['Number and gender', 'Only its spelling', 'A concept unrelated to pronoun-antecedent agreement', 'Only the number of syllables'], 0),
   ('Why is it useful to review reading and grammar skills like these together?', ['It reinforces how different language skills support clear reading and writing', 'These skills have no connection to each other', 'A reason unrelated to reviewing language', 'Review never helps strengthen understanding of a subject'], 0)]),
M('Review: Multiplication, Factors, Decimals, and Volume',
  'Grade 5 Math strand: this review lesson revisits key ideas from Days 71-79, including multiplying two-digit numbers, least common multiple and greatest common factor, multiplying decimals by powers of ten, and volume of rectangular prisms.',
  [('When multiplying two two-digit numbers using the standard algorithm, each digit of one number is multiplied by ___.', ['Each digit of the other number', 'Only the ones digit of the other number', 'A concept unrelated to multiplication', 'Only the first digit of the same number'], 0),
   ('The least common multiple of two numbers is the smallest number that ___.', ['Both numbers divide into evenly', 'Is smaller than both numbers', 'A concept unrelated to least common multiple', 'Only one of the numbers divides into evenly'], 0),
   ('When multiplying a decimal by 10, the decimal point moves ___.', ['One place to the right', 'One place to the left', 'A direction unrelated to this rule', 'Two places to the left'], 0),
   ('The volume of a rectangular prism is found by multiplying its ___.', ['Length, width, and height', 'Length and width only', 'A concept unrelated to volume', 'Only its height'], 0),
   ('Why is it useful to review multiplication, factors, decimals, and volume together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Heat Transfer, Electricity, Sound, and Groundwater',
   'Grade 5 Science strand: this review lesson revisits key ideas from Days 71-79, including heat transfer, electrical conductors and insulators, sound pitch and frequency, and groundwater and the water table.',
   [('Conduction is the transfer of heat through ___.', ['Direct contact between objects', 'Empty space with no matter involved', 'A concept unrelated to heat transfer', 'Sound waves travelling through air'], 0),
    ('An electrical conductor is a material that ___.', ['Allows electric current to pass through it easily', 'Blocks electric current from passing through', 'A concept unrelated to conductors', 'Has no connection to electricity at all'], 0),
    ('Pitch describes how ___ a sound seems.', ['High or low', 'Loud or quiet', 'A concept unrelated to pitch', 'Long or short'], 0),
    ('The water table is the upper level at which the ground becomes ___.', ['Saturated with water', 'Completely dry', 'A concept unrelated to the water table', 'Covered in ice'], 0),
    ('Why is it useful to review heat, electricity, sound, and water together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: The Klondike, Government Roles, and Arctic Exploration',
   'Grade 5 Social Studies strand: this review lesson revisits key ideas from Days 71-79, including the Klondike Gold Rush, the Governor General, provincial premiers, and the Franklin Expedition.',
   [('The Klondike Gold Rush drew thousands of prospectors to the ___.', ['Yukon', 'Prairies', 'A region unrelated to the Klondike Gold Rush', 'Atlantic coast'], 0),
    ('The Governor General is the representative of ___ in Canada.', ['The Crown', 'A foreign government', 'A concept unrelated to the Governor General', 'A political party'], 0),
    ('The head of a provincial government is called the ___.', ['Premier', 'Prime Minister', 'A title unrelated to provincial government', 'Governor General'], 0),
    ('The Franklin Expedition set out in the 1840s to search for a ___.', ['Northwest Passage through the Arctic', 'A gold mine in the Yukon', 'A concept unrelated to the Franklin Expedition', 'New farming region in the Prairies'], 0),
    ('Why is it useful to review these events and roles in Canadian history and government together?', ['It reinforces how these Social Studies concepts connect to build understanding of Canada', 'These topics have no connection to each other', 'A reason unrelated to reviewing social studies', 'Review never helps strengthen understanding of a subject'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260812):
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
    _rebalance_answer_positions(g5_71_80, seed=20260903)
    append_to(5, g5_71_80)
