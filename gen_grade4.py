#!/usr/bin/env python3
import sys
sys.path.insert(0,'/sessions/wonderful-keen-tesla/mnt/gradesbooster')
from gen_curriculum import sub,day,write_new,append_to,lbl,WK

L4='https://tvolearn.com/pages/grade-4-language'
M4='https://tvolearn.com/pages/grade-4-mathematics'
S4='https://tvolearn.com/pages/grade-4-science-and-technology'
SS4='https://tvolearn.com/pages/grade-4-social-studies'
RL='TVO Learn: Grade 4 Language'
RM='TVO Learn: Grade 4 Mathematics'
RS='TVO Learn: Grade 4 Science & Technology'
RSS='TVO Learn: Grade 4 Social Studies'

def L(t,s,q): return sub('Language',t,s,RL,L4,q)
def M(t,s,q): return sub('Math',t,s,RM,M4,q)
def Sc(t,s,q): return sub('Science',t,s,RS,S4,q)
def SS(t,s,q): return sub('SocialStudies',t,s,RSS,SS4,q)

g4=[
day(1,[
L('Parts of Speech','Grade 4 Language strand: nouns name people/places/things, verbs show actions, adjectives describe nouns, adverbs describe verbs.',[
  ('A noun names a person, place, or ___.',['action','thing','description','conjunction'],1),
  ('Which word is a verb in: The quick dog ran?',['The','quick','dog','ran'],3),
  ('Which is an adjective?',['run','slowly','happy','eat'],2),
  ('Adverbs often tell ___ about a verb.',['colour','size','how/when/where','what kind'],2),
  ('Which is an adverb?',['dog','blue','quickly','house'],2)]),
M('Multiplication Facts to 10×10','Grade 4 Number strand: students recall multiplication facts to 10×10 fluently and use them to solve problems.',[
  ('7 × 8 = ?',['48','54','56','64'],2),
  ('6 × 9 = ?',['48','54','56','63'],1),
  ('4 × 7 = ?',['24','28','32','21'],1),
  ('9 × 9 = ?',['72','81','80','90'],1),
  ('8 × 6 = ?',['42','46','48','54'],2)]),
Sc('Habitats and Communities','Grade 4 Science Life Systems strand: a habitat is where organisms live; a community is all the organisms sharing a habitat and interacting.',[
  ('A habitat provides food, water, shelter, and ___.',['money','space','television','electricity'],1),
  ('A community includes ___.',['only plants','only animals','all living things in an area','only predators'],2),
  ('Which is a freshwater habitat?',['Ocean','Desert','Pond','Tundra'],2),
  ('Organisms in a community ___.',['never interact','depend on and interact with each other','live separately','eat only plants'],1),
  ('A forest habitat includes trees, soil, water, and ___.',['buildings','roads','animals and plants that live there','factories'],2)]),
SS('Ancient Civilizations Overview','Grade 4 Social Studies Heritage strand: ancient civilizations developed organized societies with government, art, writing, and technology.',[
  ('An ancient civilization is ___.',['a modern city','a society from thousands of years ago','a type of government','a geography term'],1),
  ('Which of these is NOT an ancient civilization?',['Egypt','Greece','Rome','Canada (modern)'],3),
  ('Ancient civilizations contributed ___.',['nothing to modern life','writing, government, and architecture still used today','only myths and legends','only farming'],1),
  ('What is archaeology?',['The study of stars','The study of rocks','The study of human history through artifacts','A type of government'],2),
  ('Why do we study ancient civilizations?',['We do not','To understand how human societies developed','Only for fun','Only for geography'],1)])]),
day(2,[
L('Sentence Types','Grade 4 Language strand: the four sentence types are declarative (statement), interrogative (question), imperative (command), and exclamatory.',[
  ('A declarative sentence ___.',['asks a question','gives a command','makes a statement','shows surprise'],2),
  ('An interrogative sentence ends with a ___.',['period','exclamation mark','question mark','comma'],2),
  ('An imperative sentence gives a ___.',['fact','question','command or request','strong feeling'],2),
  ('An exclamatory sentence expresses ___.',['a fact','a question','a command','strong emotion'],3),
  ('"Close the door!" is a ___ sentence.',['declarative','interrogative','imperative','exclamatory'],2)]),
M('Division Basics','Grade 4 Number strand: division is sharing equally or grouping. Students divide with dividends to 100 using multiplication facts.',[
  ('35 ÷ 7 = ?',['4','5','6','7'],1),
  ('48 ÷ 6 = ?',['7','8','9','6'],1),
  ('Division is the inverse (opposite) of ___.',['addition','subtraction','multiplication','fractions'],2),
  ('63 ÷ 9 = ?',['6','7','8','9'],1),
  ('If 8 × 7 = 56, then 56 ÷ 8 = ?',['6','7','8','9'],1)]),
Sc('Food Chains and Webs','Grade 4 Science Life Systems: a food chain shows energy flow from producer to consumer. A food web shows interconnected food chains.',[
  ('Producers in a food chain are ___.',['animals that eat plants','plants that make their own food','carnivores','decomposers'],1),
  ('A herbivore is an animal that eats ___.',['only meat','only plants','both plants and meat','nothing'],1),
  ('In a food web, arrows show ___.',['friendship','the direction energy flows','movement','habitat'],1),
  ('What happens if one species in a food web disappears?',['Nothing changes','Other species are affected because they are connected','Only predators notice','Only prey notice'],1),
  ('A decomposer ___.',['eats only plants','eats only animals','breaks down dead matter and recycles nutrients','makes its own food'],2)]),
SS('Ancient Egypt','Grade 4 Social Studies: Ancient Egypt flourished along the Nile River, developing writing (hieroglyphics), monumental architecture, and complex government.',[
  ('Ancient Egypt was located in ___.',['Asia','Europe','Africa','South America'],2),
  ('The Nile River was important because ___.',['it was the longest river','it provided fertile soil and water for farming','it separated Egypt from enemies','it had gold'],1),
  ('Egyptian hieroglyphics were ___.',['a form of mathematics','a type of building','a writing system using pictures','a religious ceremony'],2),
  ('The pyramids were built as ___.',['palaces for living pharaohs','tombs for pharaohs','temples for worship only','storage facilities'],1),
  ('Who ruled Ancient Egypt?',['A president','An elected prime minister','A pharaoh (king/queen)','A group of priests'],2)])]),
day(3,[
L('Synonyms and Antonyms','Grade 4 Language strand: synonyms are words with similar meanings; antonyms have opposite meanings. Using them enriches vocabulary and writing.',[
  ('A synonym for "happy" is ___.',['sad','joyful','angry','tired'],1),
  ('An antonym for "ancient" is ___.',['old','historic','modern','past'],2),
  ('Which pair are synonyms?',['hot/cold','big/large','fast/slow','night/day'],1),
  ('Which pair are antonyms?',['glad/happy','quick/fast','bright/dim','small/tiny'],2),
  ('Using synonyms in writing helps to ___.',['confuse the reader','avoid repetition and add variety','shorten writing','change the topic'],1)]),
M('2-Digit × 1-Digit Multiplication','Grade 4 Number strand: multiply 2-digit numbers by 1-digit numbers using the distributive property and place value.',[
  ('23 × 4 = ?',['82','92','72','102'],1),
  ('45 × 3 = ?',['125','135','145','115'],1),
  ('67 × 2 = ?',['124','134','114','144'],1),
  ('To solve 34 × 5, you can think 30×5 + 4×5 = ?',['160','170','180','150'],1),
  ('Which is correct: 58 × 3 = ?',['164','174','154','184'],1)]),
Sc('Adaptations','Grade 4 Science Life Systems: adaptations are physical or behavioural features that help organisms survive in their habitat.',[
  ('An adaptation is ___.',['a type of habitat','a feature that helps an organism survive','a food chain stage','a community interaction'],1),
  ('A polar bear\'s white fur is an adaptation that helps it ___.',['attract mates','camouflage in snowy environments','swim faster','stay warmer in summer'],1),
  ('A cactus stores water in its thick stem as an adaptation to ___.',['rainy environments','cold climates','desert environments with little rain','forest life'],2),
  ('Which is a behavioural adaptation?',['Duck\'s webbed feet','Bird\'s hollow bones','Birds migrating south in winter','Fish gills'],2),
  ('Camouflage is an adaptation that helps animals ___.',['run faster','stay hidden from predators or prey','find water','digest food better'],1)]),
SS('Ancient Greece','Grade 4 Social Studies: Ancient Greece developed democracy, philosophy, the Olympics, and architecture that influenced the Western world.',[
  ('Ancient Greece was located in ___.',['Africa','Asia','Southern Europe','North America'],2),
  ('Democracy was developed in ___.',['Ancient Egypt','Ancient Rome','Ancient China','Ancient Greece (Athens)'],3),
  ('The Olympic Games began in ___.',['Rome','Greece','Egypt','China'],1),
  ('Greek philosophers like Socrates were known for ___.',['building pyramids','writing hieroglyphics','asking deep questions about life and knowledge','fighting wars only'],2),
  ('Ancient Greek architecture featured ___.',['mud brick walls','igloos','columns and temples like the Parthenon','underground cities'],2)])]),
day(4,[
L('Prefixes and Suffixes','Grade 4 Language strand: a prefix is added before a root word to change its meaning; a suffix is added after. Examples: un-, re-, -ful, -less.',[
  ('What does the prefix "un-" mean?',['again','before','not','after'],2),
  ('What does "unhappy" mean?',['very happy','not happy','happy again','before happy'],1),
  ('What does the suffix "-ful" mean?',['without','full of','before','again'],1),
  ('Which word means "without hope"?',['hopeful','hopefully','hopeless','rehope'],2),
  ('What does "redo" mean?',['not do','do before','do again','do after'],2)]),
M('Introduction to Long Division','Grade 4 Number strand: students divide 2-digit dividends by 1-digit divisors, understanding quotient and remainder.',[
  ('In division, the number being divided is the ___.',['divisor','quotient','remainder','dividend'],3),
  ('In division, the number dividing is the ___.',['dividend','quotient','remainder','divisor'],3),
  ('27 ÷ 4 = 6 remainder ___.',['2','3','4','1'],1),
  ('37 ÷ 5 = ?',['7 r2','7 r3','8 r1','6 r7'],0),
  ('A remainder in division is ___.',['the answer','how many are left over','the divisor','the quotient'],1)]),
Sc('Biodiversity','Grade 4 Science Life Systems: biodiversity means the variety of living organisms in an ecosystem. Greater biodiversity usually means a healthier ecosystem.',[
  ('Biodiversity means ___.',['only one type of organism','the variety of living organisms in an area','the number of plants only','the size of an ecosystem'],1),
  ('Greater biodiversity usually means ___.',['a less stable ecosystem','a healthier, more stable ecosystem','fewer species','only large animals'],1),
  ('Which habitat has the greatest biodiversity?',['A parking lot','A single-crop farm','A tropical rainforest','An empty field'],2),
  ('How does biodiversity benefit humans?',['It does not','It provides food, medicine, and clean air and water','Only scientists benefit','Only animals benefit'],1),
  ('What threatens biodiversity?',['Too much rain','Habitat destruction, pollution, and invasive species','More trees','Clean water'],1)]),
SS('Ancient Rome','Grade 4 Social Studies: Ancient Rome built a vast empire, developing law, engineering, and governance that influenced modern Western civilization.',[
  ('Ancient Rome was centred in what is now ___.',['Spain','France','Italy','Greece'],2),
  ('The Roman Republic had a system of ___.',['absolute monarchy','representative government with a Senate','complete democracy','religious rule'],1),
  ('Roman engineering achievements include ___.',['pyramids','hieroglyphics','roads, aqueducts, and the arch','the Great Wall'],2),
  ('The Roman Empire fell in ___.',['100 AD','476 AD','1492 AD','1066 AD'],1),
  ('What is one way ancient Rome influences us today?',['No influence','Latin words in English and legal/government systems','Egyptian architecture','Greek food'],1)])]),
day(5,[
L('Reading: Main Idea and Supporting Details','Grade 4 Reading strand: the main idea is what a text is mostly about. Supporting details give more information and evidence for the main idea.',[
  ('The main idea is ___.',['a small detail','the topic sentence only','what the entire text is mostly about','the last sentence'],2),
  ('Supporting details ___.',['are unrelated to the main idea','explain or prove the main idea','are always at the beginning','are more important than the main idea'],1),
  ('Where is the main idea often found?',['Only in the middle','In a caption','Often in the first or last paragraph as the topic sentence','Only at the end'],2),
  ('How do you identify the main idea?',['Read only the title','Ask "What is this MOSTLY about?"','Count the paragraphs','Read only the last line'],1),
  ('Which is a main idea sentence?',['The cat was orange.','She walked to the store.','Recycling has many benefits for the environment.','He ate lunch at noon.'],2)]),
M('Fractions: Equal Parts','Grade 4 Number strand: a fraction represents equal parts of a whole. The numerator shows how many parts are selected; the denominator shows total equal parts.',[
  ('In the fraction 3/4, the denominator is ___.',['3','4','7','1'],1),
  ('In the fraction 3/4, the numerator is ___.',['3','4','7','1'],0),
  ('Which fraction represents half?',['1/3','1/4','1/2','2/3'],2),
  ('A pizza is cut into 8 equal slices. You eat 3. What fraction did you eat?',['3/8','8/3','5/8','3/5'],0),
  ('The denominator in a fraction tells you ___.',['how many parts you have','the total number of equal parts','the size of each part','whether the fraction is big'],1)]),
Sc('Human Impact on Ecosystems','Grade 4 Science Life Systems: human activities such as deforestation, pollution, and urbanization negatively affect ecosystems; conservation actions help protect them.',[
  ('Which human activity HARMS ecosystems?',['Planting trees','Creating nature reserves','Dumping waste in rivers','Composting'],2),
  ('Deforestation means ___.',['planting forests','cutting down forests','protecting forests','studying forests'],1),
  ('Which action helps PROTECT ecosystems?',['Littering','Polluting water','Creating national parks and reducing emissions','Building factories near rivers'],2),
  ('How does pollution affect wildlife?',['It helps wildlife','It destroys habitats and harms organisms','Only fish are affected','Only birds are affected'],1),
  ('What can individuals do to reduce environmental impact?',['Use more plastic','Reduce, reuse, recycle and conserve energy','Drive more cars','Cut down more trees'],1)]),
SS('Indigenous Peoples of North America','Grade 4 Social Studies: Indigenous peoples of North America include many diverse nations, each with unique cultures, languages, and governance systems.',[
  ('Indigenous peoples of North America ___.',['arrived recently','have lived here for thousands of years','all speak the same language','are a single unified group'],1),
  ('There are ___ Indigenous cultures in North America.',['only 1','only 2 or 3','many hundreds of diverse nations','only 5'],2),
  ('Traditional Indigenous knowledge includes ___.',['only crafts','only language','ecological knowledge, governance, and cultural practices','only dance'],2),
  ('Why is it important to learn about Indigenous cultures?',['It is not important','They are part of Canada\'s history, heritage, and identity','Only in Ontario','Only for adults'],1),
  ('The Indian Act (1876) was ___.',['a celebration of Indigenous cultures','a law that restricted the rights of Indigenous peoples in Canada','a trade agreement','A school curriculum'],1)])]),
day(6,[
L('Reading: Inference','Grade 4 Reading strand: inference means using evidence from the text plus your own knowledge to understand something not directly stated.',[
  ('An inference is ___.',['directly stated in the text','a guess with no evidence','a conclusion drawn from evidence in the text plus prior knowledge','the main idea'],2),
  ('What clues help you make an inference?',['Only pictures','Text evidence plus what you already know','Random guessing','The book cover only'],1),
  ('Maria grabbed her umbrella before leaving. You can infer ___.',['She is going swimming','It was probably raining or she expected rain','She likes umbrellas','She forgot her coat'],1),
  ('The book\'s cover shows a spaceship. You can infer the story is about ___.',['Farming','Space/science fiction','Cooking','History'],1),
  ('After making an inference, a good reader ___.',['Ignores it','Reads on to confirm or revise the inference','Tells others','Stops reading'],1)]),
M('Comparing Fractions','Grade 4 Number strand: to compare fractions with the same denominator, compare numerators. To compare different denominators, find equivalent fractions.',[
  ('Which is greater: 3/5 or 1/5?',['1/5','3/5','Equal','Cannot tell'],1),
  ('Which fraction is closest to 1 (whole)?',['1/4','2/4','3/4','0/4'],2),
  ('1/2 is ___ 1/4.',['less than','equal to','greater than','not comparable to'],2),
  ('Order from least to greatest: 3/8, 1/8, 7/8',['7/8, 3/8, 1/8','1/8, 3/8, 7/8','3/8, 1/8, 7/8','1/8, 7/8, 3/8'],1),
  ('Which is the largest fraction?',['2/3','1/3','1/6','5/6'],3)]),
Sc('Rocks and Minerals','Grade 4 Science Earth strand: rocks are made of minerals. The three rock types are igneous, sedimentary, and metamorphic, each formed by different processes.',[
  ('The three types of rocks are igneous, sedimentary, and ___.',['volcanic','metamorphic','crystal','fossil'],1),
  ('Igneous rock forms from ___.',['compressed sediment','plant material','cooled magma or lava','other rocks under pressure'],2),
  ('Sedimentary rock forms from ___.',['magma','layers of sediment compressed over time','magma and pressure','only volcanic activity'],1),
  ('Metamorphic rock forms when ___.',['lava cools','sediment is compressed','existing rock is changed by heat and pressure','glaciers melt'],2),
  ('Fossils are most often found in ___.',['igneous rock','metamorphic rock','sedimentary rock','granite'],2)]),
SS('Early Canadian History','Grade 4 Social Studies: Canada\'s early history includes Indigenous peoples, European exploration, New France, and British colonization.',[
  ('Who were the first people to live in what is now Canada?',['French settlers','British settlers','Indigenous peoples','American explorers'],2),
  ('New France was a colony established by ___.',['England','France','Spain','Portugal'],1),
  ('Jacques Cartier was significant because ___.',['He built the first railway','He was the first European to sail the St. Lawrence River','He discovered gold','He founded Toronto'],1),
  ('British and French competition for control of Canada led to ___.',['immediate peace','trade agreements','conflict including the Seven Years\' War','no conflict'],1),
  ('The Battle of the Plains of Abraham (1759) resulted in ___.',['French victory','A draw','British victory and control of New France','Indigenous victory'],2)])]),
day(7,[
L('Writing: Paragraphs','Grade 4 Writing strand: a well-organized paragraph has a topic sentence, supporting details, and a concluding sentence. All sentences relate to one main idea.',[
  ('The topic sentence in a paragraph ___.',['gives a detail','ends the paragraph','states the main idea of the paragraph','is unrelated to the other sentences'],2),
  ('Supporting sentences in a paragraph ___.',['introduce new topics','give details, reasons, or examples that support the topic sentence','end the paragraph','are optional'],1),
  ('A concluding sentence ___.',['introduces the topic','adds a new idea','wraps up the paragraph and restates the main idea','asks a question'],2),
  ('How many main ideas should one paragraph have?',['As many as possible','Two or three','One','None'],2),
  ('Which would make a good topic sentence for a paragraph about dogs?',['Dogs are brown.','Dogs can run.','Dogs make excellent pets for many reasons.','My dog is named Rex.'],2)]),
M('Adding Fractions with Same Denominator','Grade 4 Number strand: to add fractions with the same denominator, add the numerators and keep the denominator the same.',[
  ('1/5 + 2/5 = ?',['2/10','3/5','3/10','1/5'],1),
  ('2/7 + 3/7 = ?',['5/14','5/7','6/7','1/7'],1),
  ('3/8 + 4/8 = ?',['7/16','6/8','7/8','1/8'],2),
  ('When adding fractions with the same denominator, the denominator ___.',['doubles','adds too','stays the same','becomes 0'],2),
  ('1/4 + 2/4 = ?',['3/4','3/8','2/4','1/2'],0)]),
Sc('Rock Cycle','Grade 4 Science Earth strand: rocks cycle continuously between igneous, sedimentary, and metamorphic forms through geological processes.',[
  ('What drives the rock cycle?',['The moon\'s gravity','Heat and pressure from Earth\'s interior, and weathering at the surface','Wind and rain only','Only volcanic eruptions'],1),
  ('Weathering and erosion break rocks into ___.',['magma','sediment','crystals','lava'],1),
  ('Sediment that is compressed and cemented forms ___.',['igneous rock','metamorphic rock','sedimentary rock','lava'],2),
  ('When magma cools it forms ___.',['sedimentary rock','metamorphic rock','igneous rock','sediment'],2),
  ('The rock cycle shows that rocks ___.',['never change','are always igneous','can be transformed from one type to another over time','only come from volcanoes'],2)]),
SS('European Explorers','Grade 4 Social Studies: European explorers from the 1400s–1600s sailed to North America, changing the world and affecting Indigenous peoples significantly.',[
  ('Why did Europeans explore the world in the 1400s–1600s?',['They were lost','They sought new trade routes and resources','They were looking for Canada specifically','They wanted to meet Indigenous peoples'],1),
  ('Christopher Columbus (1492) sailed for ___.',['England','France','Portugal','Spain'],3),
  ('John Cabot claimed land for ___.',['Spain','France','England','Portugal'],2),
  ('The arrival of Europeans had a ___ impact on Indigenous peoples.',['mostly positive','completely neutral','devastating — disease, displacement, and loss of culture','no impact'],2),
  ('Samuel de Champlain is known for ___.',['Discovering North America','Finding gold','Founding Quebec City in 1608','Winning the Seven Years\' War'],2)])]),
day(8,[
L('Writing: Descriptive Writing','Grade 4 Writing strand: descriptive writing uses sensory details (sight, sound, smell, touch, taste) and vivid language to create a clear picture for the reader.',[
  ('Descriptive writing uses ___.',['only facts and numbers','sensory details and vivid language','only dialogue','only action verbs'],1),
  ('Which is a more descriptive sentence?',['The flower was nice.','The flower was red.','The velvety crimson rose filled the air with a sweet perfume.','I saw a flower.'],2),
  ('Sensory details include descriptions of ___.',['mathematics','sight, sound, smell, touch, and taste','grammar rules only','sentence structure'],1),
  ('Vivid adjectives make writing ___.',['harder to read','more boring','more specific and engaging','shorter'],2),
  ('Which word is more vivid?',['happy','okay','fine','ecstatic'],3)]),
M('Decimals: Tenths','Grade 4 Number strand: a decimal is another way to write a fraction. Tenths represent parts of a whole divided into 10 equal parts (e.g., 0.3 = 3/10).',[
  ('0.7 means ___.',['7 ones','7 hundredths','7 tenths','70 ones'],2),
  ('Which decimal equals 3/10?',['0.03','3.0','0.3','30.0'],2),
  ('What is 6 tenths as a decimal?',['6.0','0.06','0.6','60.0'],2),
  ('0.1 + 0.4 = ?',['0.5','0.3','0.04','5.0'],0),
  ('Which is less than 0.5?',['0.6','0.8','0.3','0.9'],2)]),
Sc('Soil Formation','Grade 4 Science Earth strand: soil forms over thousands of years by weathering of rock and addition of organic matter. It has layers called horizons.',[
  ('Soil forms from ___.',['only sand','only plants','weathered rock and organic matter','water alone'],2),
  ('The top layer of soil is ___.',['bedrock','parent material','subsoil','topsoil (humus-rich)'],3),
  ('Topsoil is important because ___.',['it is the hardest layer','it is richest in nutrients for plant growth','it contains no water','it is made of solid rock'],1),
  ('How long does it take to form good soil?',['A few days','A few years','Hundreds to thousands of years','Only in rainy seasons'],2),
  ('What does humus in soil come from?',['Rocks only','Decayed plants and animals','Water','Sand and gravel'],1)]),
SS('Government: Democracy and Monarchy','Grade 4 Social Studies: governments organize society and make laws. A democracy gives citizens a voice; a monarchy is led by a king or queen.',[
  ('In a democracy, leaders are ___.',['inherited through family','appointed by religious leaders','chosen by the citizens through voting','selected by the military'],2),
  ('Canada is a ___.',['republic','absolute monarchy','constitutional monarchy and parliamentary democracy','dictatorship'],2),
  ('Parliament makes ___.',['food','laws','buildings','schools'],1),
  ('A constitutional monarchy means ___.',['the monarch has unlimited power','the monarch\'s power is limited by a constitution and elected government','only the monarch rules','there is no elected government'],1),
  ('Voting is important because ___.',['it is not important','only wealthy people vote','citizens have a voice in choosing their government','the government decides everything anyway'],1)])]),
day(9,[
L('Writing: Persuasive Writing','Grade 4 Writing strand: persuasive writing argues for a position using reasons, evidence, and a call to action. It has a clear opinion statement.',[
  ('The purpose of persuasive writing is to ___.',['tell a story','describe something','convince the reader to agree or take action','explain how to do something'],2),
  ('A persuasive text should include ___.',['a clear opinion, reasons, and evidence','only opinions with no evidence','only facts with no opinion','a fictional story'],0),
  ('Which is a good opinion statement for a persuasive text?',['Dogs exist.','Dogs can run.','Schools should have longer lunch breaks.','Some students eat lunch.'],2),
  ('Counter-arguments in persuasive writing ___.',['weaken your argument','acknowledge opposing views and then refute them, strengthening your argument','are unrelated to the topic','should always be avoided'],1),
  ('A call to action at the end of a persuasive text asks the reader to ___.',['stop reading','do something or change their view','summarize what they read','find more information'],1)]),
M('Decimals: Hundredths','Grade 4 Number strand: hundredths represent parts of a whole divided into 100 equal parts. 0.23 = 23/100 = 2 tenths + 3 hundredths.',[
  ('0.47 means ___.',['47 tenths','47 hundredths','4 tenths 7 ones','47 ones'],1),
  ('Which decimal equals 15/100?',['1.5','0.015','0.15','15.0'],2),
  ('What is 8 hundredths as a decimal?',['8.0','0.8','0.08','80.0'],2),
  ('0.25 + 0.50 = ?',['0.75','0.25','0.70','0.55'],0),
  ('Which is greater: 0.3 or 0.30?',['0.3','0.30','Equal — they are the same','Cannot compare'],2)]),
Sc('Properties of Light: Reflection','Grade 4 Science Energy strand: light travels in straight lines and reflects off surfaces. The angle of incidence equals the angle of reflection.',[
  ('Light travels in ___.',['curves','circles','straight lines','zigzags'],2),
  ('Reflection occurs when light ___.',['is absorbed by a surface','bends as it passes through','bounces off a surface','disappears into an object'],2),
  ('Which surface reflects light best?',['Black velvet','Dark wood','A mirror','A sponge'],2),
  ('The angle of incidence is ___.',['always 90 degrees','equal to the angle of reflection','greater than the angle of reflection','less than the angle of reflection'],1),
  ('Why does a mirror show your reflection?',['It glows','It is transparent','Its smooth surface reflects light at the same angle it hits','It absorbs light'],2)]),
SS('Trade and Commerce in History','Grade 4 Social Studies: trade is the exchange of goods and services. Ancient and early modern civilizations developed trade routes that spread culture and ideas.',[
  ('Trade is the exchange of ___.',['soldiers','goods and services','land only','animals only'],1),
  ('The Silk Road connected ___.',['North and South America','Africa and Australia','Europe, the Middle East, and Asia','Canada and the USA'],2),
  ('Why did civilizations trade with each other?',['For entertainment','To access goods they could not produce themselves','Only for war','Only for art'],1),
  ('Trade often led to ___.',['isolation of cultures','conflict only','spreading of ideas, technology, and culture between civilizations','only economic profit'],2),
  ('The fur trade in early Canada involved ___.',['only European settlers','only Indigenous peoples','both Indigenous peoples and European settlers','only French traders'],2)])]),
day(10,[
L('Spelling: ie/ei Words','Grade 4 Language strand: the "i before e except after c" rule helps spell many words, but has exceptions. Students apply this pattern in context.',[
  ('Which spelling is correct?',['recieve','recieve','receive','receve'],2),
  ('"I before E except after C" means in the word BELIEVE you write ___.',['ei','ie','e only','i only'],1),
  ('Which is spelled correctly?',['freind','friend','freind','frend'],1),
  ('After the letter C, you usually write ___ (not ei).',['ie','ei','only e','only i'],1),
  ('Which word follows the "i before e except after c" rule?',['their','weird','believe','neither'],2)]),
M('Money: Making Change','Grade 4 Number strand: students calculate change by subtracting the price from the amount paid, using coins and bills up to $20.',[
  ('An item costs $3.75. You pay $5.00. Your change is ___.',['$1.25','$1.75','$2.25','$1.00'],0),
  ('An item costs $12.49. You pay $15.00. Your change is ___.',['$2.41','$2.51','$3.51','$2.61'],1),
  ('To calculate change, you ___.',['add price and amount paid','subtract the price from the amount paid','multiply the price','divide the price'],1),
  ('An item costs $7.89. You pay $10.00. Your change is ___.',['$2.11','$3.11','$2.21','$3.21'],0),
  ('You have $20. You buy items for $14.37. Change = ?',['$5.63','$6.63','$5.37','$6.37'],0)]),
Sc('Properties of Light: Refraction','Grade 4 Science Energy strand: refraction is the bending of light as it passes from one medium to another (e.g., from air to water).',[
  ('Refraction is the ___ of light.',['speeding up','slowing down','bending','absorption'],2),
  ('Refraction occurs when light passes from one ___ to another.',['colour','direction','medium (material)','source'],2),
  ('A straw in a glass of water appears to be bent because of ___.',['reflection','refraction','absorption','diffusion'],1),
  ('A prism separates white light into its colours because different colours ___ at different angles.',['absorb','emit','refract','reflect'],2),
  ('A rainbow is an example of ___.',['only reflection','only absorption','refraction and dispersion of sunlight through water droplets','diffraction only'],2)]),
SS('Human Rights','Grade 4 Social Studies: human rights are basic rights all people deserve. The Universal Declaration of Human Rights (UDHR, 1948) protects these rights globally.',[
  ('Human rights are rights that ___.',['only wealthy people have','all people have equally, regardless of background','only adults have','only citizens have'],1),
  ('The Universal Declaration of Human Rights was adopted in ___.',['1776','1867','1948','2000'],2),
  ('Which is a basic human right?',['Owning luxury goods','Freedom of speech and freedom from torture','Never going to school','Unlimited money'],1),
  ('Who is responsible for upholding human rights?',['No one','Governments, organizations, and individuals','Only the United Nations','Only wealthy nations'],1),
  ('Why are human rights important?',['They are not','They protect the dignity and equality of every person','Only politicians care about them','They only apply in certain countries'],1)])]),
day(11,[
L('Grammar: Adverbs','Grade 4 Language strand: adverbs modify verbs, adjectives, or other adverbs. They tell how, when, where, or to what degree something happens.',[
  ('An adverb modifies a ___.',['noun only','verb, adjective, or another adverb','pronoun only','preposition only'],1),
  ('Which word is an adverb in: She spoke softly?',['She','spoke','softly','(no adverb)'],2),
  ('Adverbs of manner tell ___.',['when','where','how','to what degree'],2),
  ('Adverbs of time tell ___.',['how','where','to what degree','when'],3),
  ('Many adverbs end in ___.',['–er','–ing','–ly','–tion'],2)]),
M('Patterns: Numeric and Geometric','Grade 4 Algebra and Patterning strand: numeric patterns follow a mathematical rule; geometric patterns involve shapes. Students identify rules and extend patterns.',[
  ('What is the rule? 3, 6, 9, 12...',['add 2','add 3','add 4','multiply by 2'],1),
  ('What comes next? 1, 2, 4, 8, 16, ___',['18','24','32','20'],2),
  ('A geometric pattern uses ___.',['numbers only','repeating or growing shapes','only colours','only lines'],1),
  ('What is the rule? 100, 90, 80, 70...',['subtract 5','subtract 10','subtract 20','add 10'],1),
  ('Which is an example of a geometric pattern?',['2,4,6,8','triangle, square, triangle, square','red, blue, green, red','A,B,C,A,B,C'],1)]),
Sc('Sound: Vibration and Frequency','Grade 4 Science Energy strand: sounds are made by vibrations. Frequency determines pitch — higher frequency = higher pitch. Amplitude determines volume.',[
  ('Sound is caused by ___.',['light waves','electrical signals','vibrations','magnetic fields'],2),
  ('Frequency refers to ___.',['how loud a sound is','how many vibrations per second (determines pitch)','how far sound travels','the speed of light'],1),
  ('A high-frequency sound has a ___ pitch.',['low','medium','high','no'],2),
  ('Amplitude of a sound wave determines its ___.',['pitch','speed','volume (loudness)','frequency'],2),
  ('In which medium does sound travel fastest?',['Vacuum (space)','Air','Water','Solid materials (like steel)'],3)]),
SS('Canadian Geography: Provinces and Territories','Grade 4 Social Studies: Canada has 10 provinces and 3 territories. Each has a capital city and distinct geographic features.',[
  ('How many provinces does Canada have?',['8','9','10','12'],2),
  ('How many territories does Canada have?',['1','2','3','4'],2),
  ('What is the largest province in Canada by area?',['Ontario','British Columbia','Alberta','Quebec'],3),
  ('What is Canada\'s capital city?',['Toronto','Ottawa','Montreal','Vancouver'],1),
  ('Which territory is the newest, created in 1999?',['Yukon','Northwest Territories','Nunavut','British Columbia'],2)])]),
day(12,[
L('Vocabulary: Context Clues','Grade 4 Language strand: context clues are words and phrases near an unknown word that help you determine its meaning without a dictionary.',[
  ('Context clues are ___.',['definitions found in the glossary','words and ideas near an unknown word that suggest its meaning','only synonyms','only antonyms'],1),
  ('Which type of context clue gives a definition within the text?',['Synonym clue','Restatement clue: "X, which means..."','Antonym clue','Inference clue'],1),
  ('Using context clues helps readers ___.',['skip unknown words','look up every word in a dictionary','figure out word meanings while reading continuously','memorize vocabulary lists'],2),
  ('In "The magnanimous king gave generously to the poor," magnanimous means ___.',['cruel','stingy','generous and kind','quiet'],2),
  ('Which strategy helps most with a word you do not know?',['Ignore it','Read the surrounding sentences for clues','Skip to the next chapter','Ask someone immediately'],1)]),
M('Geometry: Angles','Grade 4 Geometry strand: an angle is formed by two rays with a common endpoint. A right angle = 90°, acute angle < 90°, obtuse angle > 90°.',[
  ('A right angle measures exactly ___.',['45°','60°','90°','180°'],2),
  ('An acute angle measures ___.',['exactly 90°','more than 90°','less than 90°','180°'],2),
  ('An obtuse angle measures ___.',['less than 90°','exactly 90°','between 90° and 180°','more than 180°'],2),
  ('A straight angle measures ___.',['90°','45°','180°','270°'],2),
  ('Which tool measures angles?',['Ruler','Compass','Protractor','Scale'],2)]),
Sc('Pulleys and Gears','Grade 4 Science Energy strand: pulleys and gears are simple machines that redirect or change force. Gears can speed up or slow down motion and change direction.',[
  ('A pulley is used to ___.',['generate electricity','make objects glow','lift or move loads by redirecting force','increase temperature'],2),
  ('In a fixed pulley, the force needed to lift a load ___.',['doubles','stays the same (only direction changes)','halves','triples'],1),
  ('A moveable pulley ___ the force needed.',['doubles','keeps the same','reduces by about half','triples'],2),
  ('When two gears mesh, they rotate in ___ directions.',['the same','opposite','random','no'],1),
  ('A larger gear turning a smaller gear makes the smaller gear rotate ___.',['slower','at the same speed','faster','backwards only'],2)]),
SS('Ontario Geography','Grade 4 Social Studies: Ontario is Canada\'s most populous province with diverse geography including the Great Lakes, Canadian Shield, and Great Lakes–St. Lawrence Lowlands.',[
  ('Ontario borders how many of the Great Lakes?',['2','3','4','5'],2),
  ('The Canadian Shield in Ontario is characterized by ___.',['flat prairies','ancient rock, forests, and lakes','mountain ranges','dry desert'],1),
  ('The most populous city in Ontario is ___.',['Ottawa','Hamilton','London','Toronto'],3),
  ('Ontario\'s provincial capital is ___.',['Ottawa','Toronto','Hamilton','Kingston'],1),
  ('Which region of Ontario is most suited for farming?',['Canadian Shield','Northern Ontario','Great Lakes–St. Lawrence Lowlands','Hudson Bay Lowlands'],2)])]),
day(13,[
L('Reading: Compare and Contrast','Grade 4 Reading strand: comparing shows how two things are alike; contrasting shows how they differ. Signal words: both, similarly, however, but, in contrast.',[
  ('Comparing means finding how things are ___.',['different','the same or similar','unrelated','bigger'],1),
  ('Contrasting means finding how things are ___.',['the same','similar','different','related'],2),
  ('Which signal word shows a contrast?',['Similarly','Also','Both','However'],3),
  ('A Venn diagram helps ___.',['add numbers','compare and contrast two or more things','write paragraphs','draw maps'],1),
  ('Which text type often uses comparison and contrast?',['A recipe','A poem','A report about two animals','A personal diary'],2)]),
M('Area and Perimeter','Grade 4 Measurement strand: perimeter is the distance around a shape; area is the space inside. Area of a rectangle = length × width; perimeter = 2(l + w).',[
  ('Perimeter is the ___.',['space inside a shape','distance around the outside of a shape','weight of a shape','height of a shape'],1),
  ('Area is measured in ___.',['linear units (cm)','square units (cm²)','cubic units (cm³)','grams'],1),
  ('A rectangle is 5 cm long and 3 cm wide. Area = ?',['8 cm²','15 cm²','16 cm²','10 cm²'],1),
  ('A rectangle is 6 cm long and 4 cm wide. Perimeter = ?',['10 cm','20 cm','24 cm','48 cm'],1),
  ('Area of a square with side 7 cm = ?',['28 cm²','49 cm²','14 cm²','21 cm²'],1)]),
Sc('Electricity: Static and Current','Grade 4 Science Energy strand: static electricity is a build-up of charge; current electricity is a flow of electrons through a conductor.',[
  ('Static electricity is caused by ___.',['a flow of electrons in a circuit','a build-up of electric charge on a surface','burning fuel','magnetism'],1),
  ('Current electricity flows through ___.',['insulators','a vacuum','conductors in a circuit','non-metals only'],2),
  ('Which is a good conductor of electricity?',['Rubber','Wood','Copper wire','Glass'],2),
  ('An insulator ___.',['allows electricity to flow freely','blocks the flow of electricity','creates static electricity','has no electrical properties'],1),
  ('Which is an example of static electricity?',['Turning on a light bulb','A lightning bolt and rubbing a balloon on hair','Using a toaster','Charging a phone'],1)]),
SS('Maps: Physical Features','Grade 4 Social Studies: physical maps show natural features like mountains, rivers, lakes, and plains. They use colour and symbols to represent terrain.',[
  ('A physical map shows ___.',['roads and cities','political boundaries','natural features like mountains and rivers','population density'],2),
  ('On most physical maps, blue represents ___.',['land','water (rivers, lakes, oceans)','mountains','grasslands'],1),
  ('What is a legend (key) on a map?',['The title','A table that explains the symbols used on the map','North arrow','Scale bar'],1),
  ('Which tool on a map shows distance?',['Legend','North arrow','Scale bar','Title'],2),
  ('The Rocky Mountains in Canada are located in ___.',['Eastern Canada','Atlantic provinces','Western Canada','Central Ontario'],2)])]),
day(14,[
L('Figurative Language: Similes','Grade 4 Language strand: a simile compares two unlike things using "like" or "as". Example: "brave as a lion," "runs like the wind".',[
  ('A simile compares two things using ___.',['and/but','is/was','like or as','metaphor words'],2),
  ('Which is a simile?',['The car is a beast.','Time flies.','She ran like the wind.','The moon smiled.'],2),
  ('What does "brave as a lion" mean?',['The person is a lion','The person is extremely brave','Lions are brave animals','A comparison without meaning'],1),
  ('Similes make writing more ___.',['difficult','confusing','boring','vivid and relatable'],3),
  ('Which is NOT a simile?',['white as snow','quiet as a mouse','The thunder roared','cold as ice'],2)]),
M('Metric Measurement: Length','Grade 4 Measurement strand: the metric system uses kilometres (km), metres (m), centimetres (cm), and millimetres (mm). 1 m = 100 cm; 1 km = 1000 m.',[
  ('1 metre = ___ centimetres.',['10','100','1000','1'],1),
  ('1 kilometre = ___ metres.',['10','100','1000','10000'],2),
  ('Which unit would you use to measure the length of a pencil?',['Kilometres','Metres','Centimetres','Grams'],2),
  ('Which unit would you use to measure the distance between two cities?',['Centimetres','Millimetres','Metres','Kilometres'],3),
  ('Convert 3 m to cm.',['3 cm','30 cm','300 cm','3000 cm'],2)]),
Sc('Electric Circuits','Grade 4 Science Energy strand: a complete circuit allows electricity to flow. It needs a power source, conductors, and a load (device). Circuits can be series or parallel.',[
  ('For electricity to flow, a circuit must be ___.',['open','broken','complete (closed)','very long'],2),
  ('Which is NOT needed in a basic circuit?',['Power source (battery)','Wire (conductor)','Load (light bulb)','A magnet'],3),
  ('In a series circuit, components are connected ___.',['in parallel paths','one after another in one loop','randomly','in a grid'],1),
  ('In a parallel circuit, each branch has ___.',['the same current as all others','its own direct path to the power source','no power at all','only one component'],1),
  ('If a bulb in a series circuit burns out, the other bulbs ___.',['keep working','get brighter','also go out (circuit is broken)','explode'],2)]),
SS('Canada\'s Natural Resources','Grade 4 Social Studies: Canada is rich in natural resources including forests, minerals, freshwater, oil, and agricultural land. These support the economy but must be managed sustainably.',[
  ('Which of these is NOT a natural resource?',['Fresh water','Gold','A car','Timber/wood'],2),
  ('Why are Canada\'s forests valuable?',['Only for scenery','They provide lumber, paper, habitat, and help regulate climate','They are not valuable','Only for tourism'],1),
  ('What energy resource does Alberta have in large quantities?',['Coal only','Iron ore','Oil and natural gas','Gold'],2),
  ('Sustainable use of resources means ___.',['using them as fast as possible','never using them','using them in a way that does not deplete them for future generations','only using what you can carry'],2),
  ('Which province is known for potash mining?',['Ontario','Nova Scotia','Saskatchewan','Newfoundland'],2)])]),
day(15,[
L('Figurative Language: Metaphors','Grade 4 Language strand: a metaphor directly states that one thing IS another unlike thing, without using "like" or "as". Example: "Life is a journey."',[
  ('A metaphor says one thing ___ another.',['is similar to','is like/as','IS directly','is bigger than'],2),
  ('Which is a metaphor?',['She ran like a cheetah.','He is as strong as an ox.','The world is a stage.','The rain fell like tears.'],2),
  ('What does "Time is money" mean?',['Time is currency','Time is valuable and should not be wasted','Clocks cost money','Time is free'],1),
  ('A metaphor differs from a simile because it ___.',['uses "like" or "as"','makes no comparison','directly states one thing is another','is only used in poetry'],2),
  ('Which is a metaphor?',['quiet as a mouse','brave as a lion','Her voice was music to my ears.','He runs like a gazelle.'],2)]),
M('Mass and Volume Measurement','Grade 4 Measurement strand: mass is measured in grams (g) and kilograms (kg). Volume is measured in litres (L) and millilitres (mL). 1 kg = 1000 g; 1 L = 1000 mL.',[
  ('1 kilogram = ___ grams.',['10','100','1000','10000'],2),
  ('1 litre = ___ millilitres.',['10','100','1000','10000'],2),
  ('Which unit measures how heavy something is?',['Litre','Millilitre','Kilometre','Kilogram'],3),
  ('Which unit measures the amount of liquid in a bottle?',['Kilogram','Kilometre','Millilitre/Litre','Centimetre'],2),
  ('A bag weighs 2500 g. How many kilograms is that?',['0.25 kg','2.5 kg','25 kg','250 kg'],1)]),
Sc('Forces: Gravity and Friction','Grade 4 Science Energy strand: gravity is the force that pulls objects toward Earth. Friction is the force that resists movement between surfaces in contact.',[
  ('Gravity is a force that ___.',['pushes objects upward','pulls objects toward each other (especially toward Earth)','stops all motion','only exists in space'],1),
  ('Friction is a force that ___.',['speeds objects up','pulls objects down','resists sliding motion between surfaces','pushes objects sideways'],2),
  ('Which surface creates MORE friction?',['Ice','A polished marble floor','Rough sandpaper','A wet road'],2),
  ('Friction produces ___.',['cold temperatures','heat and slows objects down','more gravity','electrical charge'],1),
  ('Without gravity, objects on Earth would ___.',['fall faster','stay in one place forever','float away into space','get heavier'],2)]),
SS('Environment: Conservation','Grade 4 Social Studies: conservation means protecting and managing natural resources wisely to prevent their depletion and preserve environments for future generations.',[
  ('Conservation means ___.',['using all resources immediately','protecting and wisely managing natural resources','never using resources','only saving money'],1),
  ('Which is an example of conservation?',['Leaving taps running','Wasting paper','Planting trees and reducing waste','Building more factories'],2),
  ('Canada Day (July 1) celebrates ___.',['The founding of Ontario','Canada becoming a nation in 1867','Conservation week','Indigenous peoples\' day'],1),
  ('Why should we conserve freshwater?',['Water is unlimited','Only 3% of Earth\'s water is fresh and accessible for drinking','Freshwater is dirty','Only fish need freshwater'],1),
  ('Which action MOST helps conserve forests?',['Cutting down all old trees','Paper recycling and sustainable forestry','Never entering forests','Using more wood products'],1)])]),
day(16,[
L('Reading: Sequencing','Grade 4 Reading strand: sequence is the order in which events happen. Signal words: first, then, next, after, finally, before.',[
  ('Sequence means ___.',['the main idea','the order in which events occur','a comparison','a cause-and-effect relationship'],1),
  ('Which signal word shows a sequence?',['However','In contrast','Next','Because'],2),
  ('Why is sequence important in a how-to text?',['It is not','Steps must be in order to be followed correctly','Only the first step matters','All steps can be done in any order'],1),
  ('Which goes last in a story\'s sequence?',['The problem','The beginning','The introduction','The resolution/ending'],3),
  ('"First mix the batter, then bake it" shows ___.',['contrast','cause and effect','sequence','comparison'],2)]),
M('Data: Bar Graphs','Grade 4 Data strand: a bar graph uses horizontal or vertical bars to compare quantities across categories. Students read, create, and interpret bar graphs.',[
  ('A bar graph is used to ___.',['show sequence','compare quantities across categories','measure angles','calculate perimeter'],1),
  ('The vertical axis of a bar graph usually shows ___.',['categories','frequency or quantity','colours','dates'],1),
  ('If the "Dogs" bar reaches 12 and "Cats" bar reaches 8, there are ___ more dogs.',['2','3','4','5'],2),
  ('What is the title of a graph used for?',['Decoration','To tell what data the graph shows','To label the axes','To list all data'],1),
  ('A bar graph differs from a pictograph because ___.',['bar graphs use bars instead of pictures/symbols','bar graphs are less accurate','only bar graphs have titles','pictographs are always better'],0)]),
Sc('Properties of Liquids and Solids','Grade 4 Science Materials strand: solids have definite shape and volume; liquids have definite volume but take the shape of their container.',[
  ('A solid has ___.',['definite shape and definite volume','definite volume but no definite shape','no definite shape or volume','only colour'],0),
  ('A liquid has ___.',['definite shape and volume','no volume','definite volume but takes the shape of its container','no mass'],2),
  ('Which is a solid at room temperature?',['Water','Air','Wood','Mercury'],2),
  ('The property of viscosity describes ___.',['how heavy a liquid is','how thick or resistant to flow a liquid is','the colour of a liquid','how hot a liquid is'],1),
  ('Which liquid has higher viscosity (is thicker)?',['Water','Air','Vinegar','Honey'],3)]),
SS('Canadian Culture and Arts','Grade 4 Social Studies: Canadian culture reflects Indigenous traditions and the contributions of people from many nations, expressed through music, art, literature, and celebrations.',[
  ('Canada\'s culture is ___.',['uniform and the same everywhere','shaped by Indigenous peoples and immigrants from around the world','only British and French','only Indigenous'],1),
  ('Which is a famous Canadian author?',['William Shakespeare','L.M. Montgomery (Anne of Green Gables)','Charles Dickens','Mark Twain'],1),
  ('The Group of Seven were known for ___.',['writing novels','composing music','painting Canadian landscapes in a distinct style','playing hockey'],2),
  ('Indigenous art often features ___.',['only abstract shapes','cultural symbols, animals, and stories of the artist\'s nation','only portraits','only landscapes'],1),
  ('Why is celebrating cultural arts important?',['It is not important','Arts preserve culture, identity, and history','Only professional artists need it','Only for entertainment'],1)])]),
day(17,[
L('Writing: Narrative Writing','Grade 4 Writing strand: narrative writing tells a story with a clear beginning (characters/setting), middle (problem/rising action), and end (resolution).',[
  ('Narrative writing tells a ___.',['fact-based report','persuasive argument','story with characters and events','set of instructions'],2),
  ('The beginning of a narrative should introduce ___.',['the solution','the climax','the characters and setting','the conclusion'],2),
  ('The climax of a story is ___.',['the beginning','the most exciting moment or turning point','the setting','the introduction of characters'],1),
  ('The resolution of a narrative is ___.',['the problem','how the story begins','how the problem is solved','the climax'],2),
  ('Which makes a narrative more engaging?',['No descriptions','Dialogue and vivid sensory details','Only telling (no showing)','Short, boring sentences'],1)]),
M('Data: Line Graphs','Grade 4 Data strand: a line graph shows how data changes over time. Points are connected by a line to show trends: increasing, decreasing, or stable.',[
  ('A line graph is best used to show ___.',['categories compared at one time','data that changes over time','fractions','angles'],1),
  ('The horizontal axis of a line graph usually shows ___.',['quantities','time (days, months, years)','colours','categories'],1),
  ('An upward-sloping line on a graph shows ___.',['data is decreasing','data is staying the same','data is increasing','data is random'],2),
  ('Which data set is best shown in a line graph?',['Favourite sports of 30 students','Daily temperature over one week','Number of each type of fruit in a bowl','Animal habitats'],1),
  ('Points on a line graph are connected to show ___.',['exact values only','trends and changes over time','the average','separate categories'],1)]),
Sc('Mixtures and Solutions','Grade 4 Science Materials strand: a mixture is made of two or more substances combined physically. A solution is a mixture where one substance dissolves completely in another.',[
  ('A mixture contains ___.',['only one substance','two or more substances combined','only chemicals','a single compound'],1),
  ('In a solution, the dissolved substance is called the ___.',['solvent','solute','mixture','residue'],1),
  ('What is a solvent?',['The substance that is dissolved','The substance that does the dissolving','A type of magnet','A type of acid'],1),
  ('Which is an example of a solution?',['Sand and water (sand settles)','Salad (mixed vegetables)','Salt dissolved in water','Oil and water (they separate)'],2),
  ('How can you separate a salt-and-water solution?',['Using a filter','Using a magnet','Evaporating the water','Freezing it and removing salt'],2)]),
SS('Citizenship: Rights and Responsibilities','Grade 4 Social Studies: in a democratic society, citizens have rights (freedoms) and responsibilities (duties). Being an active citizen benefits everyone.',[
  ('Rights give citizens ___.',['unlimited power','freedoms and protections','no rules','only advantages'],1),
  ('Responsibilities require citizens to ___.',['ignore rules','fulfill duties such as obeying laws and respecting others','only benefit themselves','do nothing'],1),
  ('Voting is both a right and a ___.',['punishment','reward','responsibility','privilege only for adults'],2),
  ('Why is community involvement important?',['It is not','Active citizenship makes communities stronger and more just','Only politicians should be involved','It costs too much'],1),
  ('Which is an example of civic responsibility?',['Littering','Ignoring elections','Paying taxes and following laws','Only caring about yourself'],2)])]),
day(18,[
L('Grammar: Conjunctions','Grade 4 Language strand: conjunctions join words, phrases, or clauses. Coordinating conjunctions: for, and, nor, but, or, yet, so (FANBOYS). Subordinating: because, since, although.',[
  ('A conjunction joins ___.',['only nouns','only verbs','words, phrases, or clauses','only sentences'],2),
  ('Which is a coordinating conjunction?',['because','although','but','since'],2),
  ('Which is a subordinating conjunction?',['and','or','but','because'],3),
  ('"I wanted to go, ___ it was raining." Which conjunction fits?',['and','but','or','nor'],1),
  ('FANBOYS stands for the ___ conjunctions.',['subordinating','correlative','coordinating','preposition'],2)]),
M('Probability: Likely and Unlikely','Grade 4 Data and Probability strand: probability describes the likelihood of an event: certain, likely, unlikely, or impossible.',[
  ('If an event is "impossible," the probability is ___.',['1','close to 1','0','close to 0'],2),
  ('If an event is "certain," the probability is ___.',['0','close to 0','close to 1','1'],3),
  ('A bag has 4 red and 1 blue marble. Picking red is ___.',['impossible','unlikely','likely','certain'],2),
  ('Which outcome is "impossible" when rolling a 6-sided die?',['Rolling a 3','Rolling a 6','Rolling a 7','Rolling a 1'],2),
  ('Probability can be expressed as a fraction. If 3 of 10 marbles are yellow, P(yellow) = ?',['7/10','1/3','3/10','10/3'],2)]),
Sc('Physical and Chemical Changes','Grade 4 Science Materials strand: a physical change alters the form but not the substance (e.g., cutting). A chemical change produces a new substance (e.g., burning).',[
  ('A physical change ___.',['creates a new substance','is irreversible','changes the form but not the substance','involves burning'],1),
  ('A chemical change ___.',['is always reversible','produces a new substance with different properties','only changes shape','is the same as melting'],1),
  ('Which is a PHYSICAL change?',['Burning wood','Rusting iron','Baking a cake','Cutting paper'],3),
  ('Which is a CHEMICAL change?',['Melting ice','Dissolving salt in water','Tearing paper','Burning candle wax'],3),
  ('Which observation suggests a CHEMICAL change has occurred?',['Change in shape','Change in size','Colour change, gas produced, or heat released','Change in location'],2)]),
SS('First Nations Treaties in Canada','Grade 4 Social Studies: treaties are agreements between the Crown and First Nations peoples. They were meant to share land but were often not honoured by the government.',[
  ('A treaty is ___.',['a type of building','a formal agreement between two or more parties','a style of artwork','a type of land'],1),
  ('Treaties between First Nations and the Crown involved ___.',['only sharing food','sharing land and defining rights and responsibilities','only money','only religion'],1),
  ('Many treaties were NOT honoured by the government, which led to ___.',['peace and prosperity','displacement and loss of land and rights for First Nations peoples','stronger First Nations communities','more treaties being made quickly'],1),
  ('Today, treaties are ___.',['forgotten documents','still legally binding and relevant to land and resource rights','only museum pieces','only used in schools'],1),
  ('Learning about treaties helps Canadians ___.',['ignore Indigenous history','understand shared history and work toward reconciliation','focus only on recent history','avoid the topic'],1)])]),
day(19,[
L('Grammar: Pronouns and Antecedents','Grade 4 Language strand: a pronoun replaces a noun (the antecedent). The pronoun must agree with its antecedent in number and gender.',[
  ('A pronoun takes the place of a ___.',['verb','noun','adjective','conjunction'],1),
  ('The word a pronoun refers back to is called the ___.',['subject','object','antecedent','predicate'],2),
  ('In "Maria took her book," "her" refers to ___.',['the book','a third person','Maria','another girl'],2),
  ('Which pronoun agrees with "students" (plural)?',['he','she','they','it'],2),
  ('Pronouns must agree with their antecedent in ___ and ___.',['size and colour','number and gender','place and time','subject and object'],1)]),
M('3-Digit × 1-Digit Multiplication','Grade 4 Number strand: multiply 3-digit numbers by 1-digit numbers using expanded form and the standard algorithm.',[
  ('213 × 3 = ?',['609','639','639','619'],1),
  ('145 × 4 = ?',['560','580','620','580'],1),
  ('To solve 234 × 5, you can expand: (200×5) + (30×5) + (4×5) = ?',['1140','1170','1200','1070'],1),
  ('326 × 3 = ?',['968','978','958','998'],1),
  ('Which strategy helps check a multiplication answer?',['Guessing','Dividing the answer by the same number to get back to the start','Adding','Subtracting'],1)]),
Sc('Weather Patterns and Water Cycle','Grade 4 Science Earth strand: the water cycle involves evaporation, condensation, and precipitation. Weather is caused by movements of air masses.',[
  ('What powers the water cycle?',['The moon\'s gravity','The wind alone','The sun\'s energy evaporating water','Human activity'],2),
  ('Evaporation is when water changes from a liquid to a ___.',['solid','gas','plasma','crystal'],1),
  ('Condensation is when water vapour changes to ___.',['ice','liquid water (forming clouds and dew)','rock','salt'],1),
  ('Precipitation includes ___.',['only rain','rain, snow, sleet, and hail','only snow','evaporation and condensation'],1),
  ('Which instrument measures precipitation?',['Thermometer','Barometer','Rain gauge','Anemometer'],2)]),
SS('Colonial Canada','Grade 4 Social Studies: colonial Canada (1600s–1867) was shaped by French and British settlers, the fur trade, and conflicts with and among Indigenous peoples.',[
  ('New France was the name for ___.',['British settlements in Canada','French colonial territory in North America','Indigenous territories','Modern Quebec only'],1),
  ('The fur trade was important because ___.',['Only Indigenous peoples benefited','It was the main economic activity connecting Indigenous peoples and Europeans','Only Europeans benefited','It was only about clothing'],1),
  ('The Acadian people were ___.',['British settlers in Nova Scotia','French-speaking settlers in Atlantic Canada','Indigenous peoples','American colonists'],1),
  ('When did Canada become a country?',['1492','1759','1867','1914'],2),
  ('The British North America Act (1867) created ___.',['New France','The Dominion of Canada (Confederation)','The Indian Act','The fur trade'],1)])]),
day(20,[
L('Reading: Text Features in Non-Fiction','Grade 4 Reading strand: non-fiction text features include headings, subheadings, captions, text boxes, bold words, table of contents, index, and glossary.',[
  ('A subheading in a text ___.',['introduces the whole article','organizes information by labelling a sub-section','is the author\'s name','is unrelated to the text'],1),
  ('A glossary provides ___.',['pictures','an index of pages','definitions of key words used in the text','the author\'s biography'],2),
  ('An index helps readers ___.',['find where specific topics are discussed (page numbers)','understand definitions','see the table of contents','read captions'],0),
  ('Bold words in a text usually indicate ___.',['errors','important vocabulary terms','the author\'s favourite words','unrelated information'],1),
  ('Text boxes in non-fiction ___.',['are errors','provide extra or supplementary information related to the topic','replace the main text','are always statistics'],1)]),
M('Elapsed Time','Grade 4 Measurement strand: elapsed time is the amount of time that passes between a start time and an end time.',[
  ('A movie starts at 2:15 p.m. and ends at 4:45 p.m. How long is it?',['2 hours 15 min','2 hours 30 min','2 hours 45 min','3 hours'],1),
  ('School starts at 8:30 a.m. and ends at 3:15 p.m. Total school time = ?',['6 h 45 min','7 h 15 min','6 h 15 min','7 h 45 min'],0),
  ('3:00 p.m. + 2 hours 40 minutes = ?',['5:00 p.m.','5:40 p.m.','6:00 p.m.','4:40 p.m.'],1),
  ('A task starts at 10:45 a.m. and takes 1 h 30 min. It ends at?',['11:15 a.m.','12:15 p.m.','12:45 p.m.','11:45 a.m.'],1),
  ('How many minutes are in 2 hours 15 minutes?',['115','135','145','125'],1)]),
Sc('Space: The Solar System','Grade 4 Science Earth strand: our solar system has the Sun at its centre and 8 planets, plus moons, asteroids, and comets orbiting it.',[
  ('How many planets are in our solar system?',['7','8','9','10'],1),
  ('What is at the centre of our solar system?',['Earth','The Moon','Jupiter','The Sun'],3),
  ('Which is the largest planet?',['Saturn','Earth','Jupiter','Neptune'],2),
  ('Planets closer to the Sun are generally ___.',['colder','warmer','made of gas','invisible'],1),
  ('Which planet is closest to the Sun?',['Venus','Earth','Mercury','Mars'],2)]),
SS('Confederation and Canadian Identity','Grade 4 Social Studies: Confederation (1867) united four provinces into the Dominion of Canada. Canadian identity includes bilingualism, multiculturalism, and respect for Indigenous peoples.',[
  ('Confederation in 1867 united which four provinces?',['BC, AB, ON, QC','ON, QC, NB, NS','NL, PE, NB, NS','MB, SK, AB, BC'],1),
  ('Canadian identity is shaped by ___.',['only one cultural group','English and French heritage, Indigenous cultures, and immigration from around the world','only British traditions','only geography'],1),
  ('What does "bilingual" mean in Canada\'s context?',['Speaking three languages','Canada has two official languages: English and French','Everyone speaks English','Only Quebec speaks French'],1),
  ('Canada became officially multicultural by law in ___.',['1867','1931','1971 (Multiculturalism Policy) / 1988 (Act)','2000'],2),
  ('Canadian identity includes ___.',['only hockey and maple syrup','kindness, diversity, democracy, rule of law, and Indigenous heritage','only British traditions','only French culture'],1)])]),
day(21,[
L('Writing: Summary Writing','Grade 4 Writing strand: a summary is a brief restatement of the most important ideas in a text, using your own words. It does not include personal opinions.',[
  ('A summary ___.',['retells every detail of a text','is longer than the original','briefly restates the most important ideas in your own words','includes your personal opinions'],2),
  ('When writing a summary, you should ___.',['copy the original text word for word','include all details','include only the main points and key supporting ideas','add your own new ideas'],1),
  ('A summary should be ___.',['longer than the original text','the same length as the original','shorter than the original','any length'],2),
  ('Which is NOT appropriate in a summary?',['The main idea','Key supporting details','The author\'s conclusion','Your personal opinion or new information'],3),
  ('To summarize means to ___.',['analyze in depth','evaluate critically','state briefly and in your own words','copy directly'],2)]),
M('Equivalent Fractions','Grade 4 Number strand: equivalent fractions represent the same value even though they have different numerators and denominators. Example: 1/2 = 2/4 = 4/8.',[
  ('Which fraction is equivalent to 1/2?',['1/3','2/3','2/4','3/4'],2),
  ('Which fraction is equivalent to 2/3?',['4/9','3/4','4/6','6/8'],2),
  ('To find an equivalent fraction, multiply or divide the numerator and denominator by the ___.',['0','1','same number','different numbers'],2),
  ('Is 3/4 equivalent to 6/8?',['No','Yes','Cannot tell','Only sometimes'],1),
  ('Simplify 6/9 to its lowest terms.',['3/4','2/3','1/2','3/9'],1)]),
Sc('Space: Moon Phases','Grade 4 Science Earth strand: the Moon has no light of its own; it reflects sunlight. As it orbits Earth, we see different amounts of its lit side — the phases.',[
  ('The Moon produces its own light.',['True','False','Only at night','Only in summer'],1),
  ('The Moon phases are caused by ___.',['Earth blocking sunlight (eclipse)','The Moon moving in and out of shadow','Different portions of the Moon\'s sunlit side being visible from Earth','The Moon changing shape'],2),
  ('A "full moon" occurs when ___.',['The Moon is between Earth and the Sun','We see the entire sunlit face of the Moon','The Moon is in shadow','The Moon is at its farthest from Earth'],1),
  ('A "new moon" is when ___.',['We see the entire lit face','The Moon is invisible (lit side faces away from Earth)','The Moon is smallest','It is a new month'],1),
  ('The Moon completes one full orbit around Earth in about ___.',['7 days','14 days','28–29 days','365 days'],2)]),
SS('Economics: Needs, Wants, Supply, and Demand','Grade 4 Social Studies: needs are essentials (food, shelter); wants are desires. Supply is how much is available; demand is how much people want.',[
  ('A "need" is ___.',['something desirable but not essential','a luxury item','something essential for survival','something you want but cannot have'],2),
  ('A "want" is ___.',['essential for survival','something desirable but not necessary for survival','the same as a need','only food and water'],1),
  ('When demand for a product increases and supply stays the same, prices usually ___.',['fall','stay the same','rise','disappear'],2),
  ('Supply means ___.',['the desire for a product','how much of a product is available','the cost of making something','the price charged'],1),
  ('Which is a NEED?',['A new video game','Clean drinking water','Designer clothing','A vacation'],1)])]),
day(22,[
L('Writing: Procedural Texts','Grade 4 Writing strand: a procedural text (how-to) explains how to do something in step-by-step order. It uses numbered steps, imperative verbs, and clear language.',[
  ('The purpose of a procedural text is to ___.',['entertain with a story','persuade the reader','explain how to do or make something','compare two ideas'],2),
  ('Procedural texts use ___ verbs.',['past tense','passive','imperative (command)','subjunctive'],2),
  ('What is essential in a procedural text?',['Opinions and feelings','Steps in chronological (sequential) order','Descriptive language only','Characters and a plot'],1),
  ('A materials or ingredients list in a procedural text comes ___.',['after all the steps','in the middle','before the steps','at the end'],2),
  ('Which sentence from a procedural text uses correct style?',['I add the flour.','Add the flour.','The flour was added.','She could add the flour.'],1)]),
M('Geometry: 3D Figures','Grade 4 Geometry strand: 3D figures have length, width, and height. Key figures: cube, rectangular prism, cylinder, cone, sphere, pyramid.',[
  ('How many faces does a cube have?',['4','5','6','8'],2),
  ('A rectangular prism has ___ vertices.',['4','6','8','12'],2),
  ('Which 3D figure has no edges or vertices?',['Cube','Cylinder','Sphere','Cone'],2),
  ('A cone has how many curved surface(s)?',['0','1','2','3'],1),
  ('A triangular pyramid (tetrahedron) has ___ faces.',['3','4','5','6'],1)]),
Sc('Conservation of Energy','Grade 4 Science Energy strand: energy cannot be created or destroyed; it can only change form. Examples: electrical → light, chemical (food) → kinetic.',[
  ('The law of conservation of energy states that energy ___.',['is always used up','can be created from nothing','cannot be created or destroyed, only changed in form','disappears when used'],2),
  ('When you eat food, chemical energy converts to ___.',['electrical energy','light energy','kinetic (movement) and heat energy','nuclear energy'],2),
  ('A light bulb converts electrical energy into ___.',['chemical energy','sound energy','light and heat energy','mechanical energy'],2),
  ('Solar panels convert ___ energy to ___ energy.',['chemical, electrical','sound, light','light (solar), electrical','kinetic, nuclear'],2),
  ('Which is an example of energy transformation?',['Doing nothing','Turning off all lights','A windmill converting wind (kinetic) to electrical energy','Using a non-electric candle'],2)]),
SS('Heritage Celebrations','Grade 4 Social Studies: cultural celebrations reflect the heritage and identity of communities. Understanding different celebrations builds respect and inclusion.',[
  ('A heritage celebration reflects ___.',['only modern pop culture','the traditions and history of a cultural community','only government events','only sports'],1),
  ('Diwali is the Festival of Lights celebrated primarily by ___.',['Chinese communities','Celtic communities','Hindu, Sikh, and Jain communities','Indigenous communities'],2),
  ('Chinese New Year is celebrated with ___.',['parades and fireworks to mark the lunar new year','Thanksgiving food','Summer solstice','Building snowmen'],0),
  ('Why is it important to acknowledge multiple cultural celebrations?',['It is not important','It promotes understanding, respect, and inclusion in a multicultural society','Only tourists need to know','It causes confusion'],1),
  ('What is Remembrance Day (November 11)?',['Canada\'s birthday','A day to honour veterans who served in wars','A harvest festival','A cultural celebration'],1)])]),
day(23,[
L('Grammar: Prepositions','Grade 4 Language strand: prepositions show the relationship between a noun and another word. Common prepositions: in, on, at, by, under, over, between, through.',[
  ('A preposition shows the ___ between words.',['colour','relationship (especially location or time)','sound','size'],1),
  ('Which is a preposition in: "The cat sat on the mat"?',['The','cat','on','mat'],2),
  ('Which sentence uses a preposition?',['Dogs run fast.','She is happy.','The book is on the table.','He jumped high.'],2),
  ('Which is NOT a preposition?',['under','through','happy','between'],2),
  ('A preposition is usually followed by a ___.',['verb','adjective','noun or pronoun (the object of the preposition)','adverb'],2)]),
M('Division: 2-Digit Divisor Introduction','Grade 4 Number strand: students divide larger dividends by 1-digit divisors and are introduced to estimation with division.',[
  ('84 ÷ 4 = ?',['19','20','21','22'],2),
  ('96 ÷ 8 = ?',['10','11','12','13'],2),
  ('75 ÷ 5 = ?',['13','14','15','16'],2),
  ('To check your division, you can ___.',['guess again','multiply the quotient by the divisor to get the dividend','add the divisor and quotient','subtract the divisor'],1),
  ('Estimate: 78 ÷ 4 is approximately?',['10','20','30','40'],1)]),
Sc('Sustainable Practices','Grade 4 Science Life Systems/Materials strand: sustainable practices reduce waste and protect the environment. The 3 Rs: Reduce, Reuse, Recycle.',[
  ('Sustainable means ___.',['using as much as possible','meeting present needs without compromising future generations\' ability to meet theirs','never using resources','spending less money'],1),
  ('Which is a sustainable practice?',['Buying single-use plastics','Leaving lights on','Composting organic waste','Printing one page per word'],2),
  ('"Reduce" means ___.',['finding new uses for old items','recycling materials','using less of something','throwing away more'],2),
  ('"Reuse" means ___.',['throwing items away after one use','finding new uses for old items','melting and reforming materials','burning waste'],1),
  ('Composting converts food scraps into ___.',['plastic','electricity','nutrient-rich soil','medicine'],2)]),
SS('Immigration: Building Canada','Grade 4 Social Studies: immigrants have come to Canada from all over the world, contributing to its economy, culture, and identity. Immigration continues today.',[
  ('Why have people immigrated to Canada?',['Canada forced them','Looking for safety, better opportunities, family reunification, or adventure','Canada is not a destination','Only recently has anyone come to Canada'],1),
  ('What is a refugee?',['A wealthy immigrant','Someone fleeing persecution, war, or disaster','A tourist who stays','A student studying abroad'],1),
  ('Immigrants have contributed to Canada by ___.',['causing problems','building communities, founding businesses, enriching culture, and serving in the military','only working in farms','only speaking one language'],1),
  ('What is multiculturalism?',['Everyone having the same culture','A policy recognizing and valuing cultural diversity','Only two cultures existing','Ignoring different cultures'],1),
  ('Why is Canada\'s multicultural heritage considered a strength?',['It is a weakness','Diverse perspectives, skills, and ideas make Canada more innovative and resilient','Only some Canadians benefit','Only in cities'],1)])]),
day(24,[
L('Reading Comprehension Strategies Review','Grade 4 Reading strand: skilled readers use multiple strategies: predicting, visualising, asking questions, making connections, summarising, and synthesising.',[
  ('Visualising while reading means ___.',['drawing pictures in a book','creating mental images of the text','looking at the illustrations only','writing notes'],1),
  ('Asking questions before and during reading helps ___.',['slow down your reading','set a purpose and deepen understanding','avoid the text entirely','only find main ideas'],1),
  ('A text-to-world connection is ___.',['connecting the text to another book','connecting the text to your personal experience','connecting the text to what you know about the world','connecting to a film'],2),
  ('Synthesising information means ___.',['copying text exactly','creating a new understanding by combining information from multiple sources','only summarising','restating information unchanged'],1),
  ('Which strategy is best for an unfamiliar word?',['Skip it','Use context clues and prior knowledge to figure out the meaning','Stop reading','Ask someone immediately without trying'],1)]),
M('Review: Number Sense and Operations','Grade 4 Number strand review: students demonstrate fluency with multiplication, division, fractions, and decimals.',[
  ('345 × 4 = ?',['1370','1380','1390','1360'],1),
  ('96 ÷ 6 = ?',['14','15','16','17'],2),
  ('1/2 + 1/2 = ?',['1/4','1/2','1','2'],2),
  ('0.3 + 0.6 = ?',['0.8','0.9','1.0','0.7'],1),
  ('Which fraction is between 1/4 and 3/4?',['1/8','1/2','7/8','1/4'],1)]),
Sc('Year Review: Science Concepts','Grade 4 Science strand review: habitats, rocks, energy (light, sound, electricity), weather, and space.',[
  ('A food web shows ___.',['the structure of rock layers','how energy flows through interconnected food chains','the water cycle','the rock cycle'],1),
  ('Igneous rock forms from ___.',['compressed sediment','cooled magma/lava','heat and pressure on existing rock','sediment layers'],1),
  ('Which is a chemical change?',['Melting ice','Cutting paper','Burning wood','Dissolving sugar in water'],2),
  ('The Moon reflects ___.',['its own light','sunlight','starlight','earthlight'],1),
  ('Sound travels fastest through ___.',['a vacuum','air','water','solid materials'],3)]),
SS('Social Studies Year Review','Grade 4 Social Studies review: ancient civilizations, Canadian history, geography, government, economics, and citizenship.',[
  ('Which ancient civilization developed democracy?',['Egypt','Rome','China','Greece'],3),
  ('Confederation in 1867 formed which country?',['New France','The British Empire','The Dominion of Canada','The United States'],2),
  ('Canada has ___ provinces and ___ territories.',['9, 4','10, 3','8, 4','10, 4'],1),
  ('What is the main purpose of a government?',['Entertain citizens','Organize society, make laws, and provide services','Only collect taxes','Only fight wars'],1),
  ('Which is a right of Canadian citizens?',['Destroying property','Free speech and equality under the law','Ignoring all rules','Having unlimited money'],1)])]),
day(25,[
L('Vocabulary Review and Word Study','Grade 4 Language strand review: students apply knowledge of synonyms, antonyms, prefixes, suffixes, context clues, and figurative language.',[
  ('The prefix "un-" in "unhappy" means ___.',['again','very','not','before'],2),
  ('The suffix "-less" in "hopeless" means ___.',['full of','not/without','again','before'],1),
  ('A simile uses ___ to compare.',['is/was','like or as','only nouns','verb to be'],1),
  ('A metaphor ___ uses like or as.',['always','sometimes','never','rarely'],2),
  ('Synonym for "ancient" = ?',['modern','new','old/historic','young'],2)]),
M('Coordinate Grid','Grade 4 Geometry strand: students locate and plot points on a coordinate grid using ordered pairs (x, y). The x-axis is horizontal; y-axis is vertical.',[
  ('In an ordered pair (3, 5), which number is the x-coordinate?',['5','3','Neither','Both'],1),
  ('The x-axis is ___.',['vertical','horizontal','diagonal','curved'],1),
  ('To plot the point (4, 2), you move ___ right and ___ up.',['2 right, 4 up','4 right, 2 up','4 up, 2 right','2 up, 4 right'],1),
  ('The origin of a coordinate grid is at ___.',['(1, 1)','(0, 0)','(1, 0)','(0, 1)'],1),
  ('Which point is on the y-axis?',['(3, 0)','(0, 4)','(2, 2)','(5, 1)'],1)]),
Sc('Review: Ecosystems and Life Systems','Grade 4 Science review: habitats, communities, adaptations, biodiversity, human impact, and conservation.',[
  ('All the organisms in a shared habitat form a ___.',['food chain','population','community','ecosystem only'],2),
  ('An adaptation helps an organism ___.',['leave its habitat','stay sick','survive in its environment','avoid reproduction'],2),
  ('Biodiversity is important because ___.',['it is not','diverse ecosystems are more stable and resilient','only scientists care','it wastes resources'],1),
  ('Which action BEST protects biodiversity?',['Building highways through forests','Draining wetlands','Creating wildlife corridors and protected areas','Introducing invasive species'],2),
  ('The rock cycle shows that rock can transform from ___.',['only igneous to metamorphic','only sedimentary to igneous','any rock type to another over time','nothing changes'],2)]),
SS('Review: Government and Citizenship','Grade 4 Social Studies review: types of government, rights, responsibilities, Canadian law, and civic participation.',[
  ('A democracy is a government where ___.',['the monarch holds all power','leaders are chosen by citizens through elections','religious leaders rule','the military runs everything'],1),
  ('The Canadian Charter of Rights and Freedoms protects ___.',['only French Canadians','only English Canadians','fundamental rights and freedoms of all people in Canada','only the rights of the government'],2),
  ('Civic responsibility includes ___.',['voting and following laws','ignoring local issues','never volunteering','only paying taxes when asked'],0),
  ('Why is an independent judiciary important?',['It is not','It ensures laws are applied fairly and governments cannot abuse power','Only lawyers care','It makes laws more expensive'],1),
  ('Canada\'s head of government is ___.',['The King/Queen','The Governor General','The Prime Minister','The Chief Justice'],2)])]),
day(26,[
L('Reading: Author\'s Purpose','Grade 4 Reading strand: the author\'s purpose is the reason for writing — to persuade, inform, or entertain (PIE). Identifying it helps comprehension.',[
  ('The three common author\'s purposes are ___.',['past, present, future','fact, fiction, opinion','persuade, inform, entertain','beginning, middle, end'],2),
  ('A newspaper article about a hurricane has the purpose to ___.',['entertain','persuade','inform','only describe'],2),
  ('A commercial trying to sell shoes has the purpose to ___.',['inform','entertain','persuade','describe'],2),
  ('A funny picture book has the purpose to ___.',['inform','persuade','entertain','instruct'],2),
  ('Identifying author\'s purpose helps readers ___.',['read faster','evaluate information and understand why it was written','skip reading strategies','find the plot'],1)]),
M('Review: Measurement','Grade 4 Measurement review: length, mass, volume, elapsed time, area, and perimeter.',[
  ('Area of a rectangle 9 cm × 5 cm = ?',['40 cm²','45 cm²','14 cm²','50 cm²'],1),
  ('Perimeter of a square with side 8 cm = ?',['8 cm','16 cm','32 cm','64 cm'],2),
  ('1 kg = ___ g.',['10','100','1000','10000'],2),
  ('A task from 9:20 a.m. to 11:05 a.m. takes?',['1 h 45 min','2 h 15 min','1 h 35 min','2 h 5 min'],0),
  ('Convert 4500 mL to litres.',['4.5 L','45 L','0.45 L','450 L'],0)]),
Sc('Review: Energy Forms and Changes','Grade 4 Science Energy review: light, sound, electricity, circuits, forces, simple machines.',[
  ('Which is an example of electrical energy converting to light?',['A fan spinning','Burning a candle','A light bulb glowing','Falling water'],2),
  ('Friction creates ___.',['cold','heat and slows objects','more gravity','static only'],1),
  ('A complete circuit needs a power source, ___, and a load.',['water','insulator','conductor/wire','vacuum'],2),
  ('Refraction occurs when light passes from one ___ to another.',['colour','direction','medium','source'],2),
  ('Sound travels as ___ waves.',['light','compression (longitudinal)','electromagnetic','transverse'],1)]),
SS('Review: Ancient Civilizations','Grade 4 Social Studies review: Egypt, Greece, Rome, and their contributions to modern society.',[
  ('Hieroglyphics were used in ___.',['Rome','Greece','Egypt','China'],2),
  ('Democracy was developed in ___.',['Egypt','Mesopotamia','Rome','Athens, Greece'],3),
  ('The Roman contribution of ___ influences modern law and government.',['hieroglyphics','the Olympic Games','legal and governmental systems','papyrus'],2),
  ('Which civilization used the Silk Road for trade?',['Ancient Egypt','Ancient Greece','Ancient Rome','Ancient China and Rome both used it'],3),
  ('Which ancient civilization was located in present-day Italy?',['Greece','Egypt','Rome','Mesopotamia'],2)])]),
day(27,[
L('Writing: Editing and Proofreading','Grade 4 Writing strand: editing focuses on content and organization; proofreading focuses on spelling, grammar, and punctuation. Both improve the final piece.',[
  ('Editing involves ___.',['fixing spelling mistakes','improving the content, structure, and clarity of writing','only punctuation','copying neatly'],1),
  ('Proofreading involves ___.',['rewriting the whole piece','checking for spelling, grammar, and punctuation errors','adding new ideas','only capitals'],2),
  ('The acronym COPS (Capitals, Organization, Punctuation, Spelling) is a ___.',['writing style','proofreading checklist','paragraph structure','story type'],1),
  ('Why is revising and editing important?',['It is not','It improves the quality and clarity of writing for the reader','Only teachers need to edit','Writing is always perfect first time'],1),
  ('Which should you do first: edit content or proofread?',['Proofread first','Edit content first (big picture before details)','Do both at exactly the same time','Do neither'],1)]),
M('Review: Data and Probability','Grade 4 Data review: tally charts, bar graphs, line graphs, pictographs, and probability.',[
  ('Which graph is BEST for showing change over time?',['Bar graph','Pictograph','Line graph','Tally chart'],2),
  ('Which graph is BEST for comparing categories at one time?',['Line graph','Bar graph','None','Scatter plot'],1),
  ('P(rolling 6 on a fair die) = ?',['1/6','1/3','1/2','2/6'],0),
  ('P(picking red from 3 red and 7 blue) = ?',['7/10','3/7','3/10','10/3'],2),
  ('The mode of a data set is ___.',['the middle value','the most frequent value','the average','the range'],1)]),
Sc('Review: Materials and Earth','Grade 4 Science review: rocks, minerals, soil, mixtures, solutions, physical/chemical changes, and the rock cycle.',[
  ('The three rock types are ___.',['granite, marble, slate','igneous, sedimentary, metamorphic','hard, soft, medium','volcanic, beach, mountain'],1),
  ('A solution differs from a mixture because ___.',['they are the same','in a solution the solute dissolves completely and cannot be seen','solutions always involve water','mixtures are permanent'],1),
  ('Which is a physical change?',['Burning paper','Rusting iron','Baking bread','Tearing paper into smaller pieces'],3),
  ('Soil is made of ___.',['only sand','rock particles, organic matter, air, and water','only clay','only compost'],1),
  ('The rock cycle is driven by ___.',['the water cycle','heat and pressure from Earth\'s interior plus weathering at the surface','only volcanoes','only wind and rain'],1)]),
SS('Review: Canada\'s History and Geography','Grade 4 Social Studies review: Canadian geography, exploration, Indigenous peoples, Confederation, and citizenship.',[
  ('Confederation year?',['1776','1759','1867','1914'],2),
  ('Canada has ___ official languages.',['1','2','3','4'],1),
  ('The largest province by area is ___.',['Ontario','British Columbia','Alberta','Quebec'],3),
  ('Treaties between the Crown and First Nations are ___.',['old and irrelevant','still legally binding','fiction','only about money'],1),
  ('What is the Canadian Charter of Rights and Freedoms?',['A children\'s story','A trading document','A document protecting fundamental rights of all people in Canada','A municipal bylaw'],2)])]),
day(28,[
L('Grammar Review','Grade 4 Language strand comprehensive grammar review: parts of speech, sentence types, punctuation, and sentence construction.',[
  ('Which sentence is a compound sentence?',['The dog runs.','She is happy.','I wanted to go, but it was raining.','Running fast.'],2),
  ('A complex sentence contains ___.',['two independent clauses','one independent clause and one dependent clause','only a dependent clause','no verbs'],1),
  ('Which punctuation separates items in a list?',['Period','Comma','Exclamation mark','Question mark'],1),
  ('What is a clause?',['A type of word','A word with a prefix','A group of words with a subject and verb','Only a dependent phrase'],2),
  ('An independent clause ___.',['cannot stand alone','depends on another clause','can stand alone as a complete sentence','has no verb'],2)]),
M('Math Review: All Strands','Grade 4 Mathematics comprehensive review covering number, geometry, measurement, patterning, and data.',[
  ('7 × 9 = ?',['54','56','63','64'],2),
  ('Area of 6 cm × 8 cm rectangle = ?',['28 cm²','48 cm²','14 cm²','42 cm²'],1),
  ('What is the next number? 3, 6, 12, 24, ___',['30','36','48','42'],2),
  ('Which fraction is greater: 3/4 or 5/8?',['5/8','3/4','Equal','Cannot tell'],1),
  ('0.45 + 0.35 = ?',['0.70','0.80','0.75','0.90'],1)]),
Sc('Science Review: All Strands','Grade 4 Science comprehensive review across life, earth, materials, and energy strands.',[
  ('What is biodiversity?',['A type of rock','The variety of living organisms in an ecosystem','A food chain','A weather pattern'],1),
  ('Which rock forms from cooled magma?',['Sedimentary','Metamorphic','Igneous','Limestone'],2),
  ('A complete circuit requires ___.',['only a battery','power source, conductor, and a load','only wires','a magnet'],1),
  ('The Moon\'s phases are caused by ___.',['the Moon changing shape','Earth\'s shadow','Different portions of the Moon\'s sunlit side being visible from Earth','The Sun moving'],2),
  ('Conservation of energy means energy ___.',['disappears when used','is created by machines','cannot be created or destroyed, only transformed','increases when heated'],2)]),
SS('Social Studies Review: All Topics','Grade 4 Social Studies comprehensive review across heritage, identity, government, and geography strands.',[
  ('Which ancient civilization developed the Olympic Games?',['Egypt','Rome','China','Greece'],3),
  ('Canada became a country through ___.',['winning a war','being given independence','Confederation in 1867','a revolution'],2),
  ('Why are treaties important today?',['They are not','They define rights to land and resources and are legally binding','Only in Quebec','Only in the 1800s'],1),
  ('Sustainable resource use means ___.',['using all resources now','never using resources','using resources so future generations can also benefit','only using renewable energy'],2),
  ('Canada\'s multicultural heritage is ___.',['a weakness','a strength that enriches society with diverse ideas and cultures','only for big cities','irrelevant today'],1)])]),
day(29,[
L('Language Arts: Oral Communication','Grade 4 Language strand: oral communication includes speaking clearly, listening actively, presenting ideas, and participating respectfully in discussions.',[
  ('Active listening means ___.',['waiting for your turn to talk only','paying attention, making eye contact, and showing you understand the speaker','looking away','interrupting to add ideas'],1),
  ('When presenting to a class, you should ___.',['speak very quietly','read directly from notes without looking up','speak clearly, make eye contact, and organize your ideas','go as fast as possible'],1),
  ('Constructive feedback is ___.',['only negative comments','specific, kind, and helpful suggestions for improvement','only positive comments','ignoring what someone said'],1),
  ('A debate involves ___.',['one person speaking alone','choosing sides and presenting arguments and counter-arguments','only asking questions','sharing feelings only'],1),
  ('Why is oral communication important?',['Only writing matters','Strong speaking and listening skills help in school, work, and daily life','Only for presentations','Computers do all communication now'],1)]),
M('Math: Problem Solving Strategies','Grade 4 Mathematics: students apply strategies like drawing diagrams, making tables, working backwards, and looking for patterns to solve multi-step problems.',[
  ('Working backwards is a useful strategy when you know ___.',['the starting conditions','a middle step','the final result and need to find the beginning','nothing about the problem'],2),
  ('Making a table helps to ___.',['avoid solving a problem','organize data to find a pattern or answer','draw a picture','multiply numbers'],1),
  ('A multi-step problem requires ___.',['only one operation','two or more steps to solve','a calculator always','reading once and guessing'],1),
  ('Drawing a diagram helps to ___.',['decorate your work','visualize the problem and make it easier to solve','skip the calculation','only geometry problems'],1),
  ('Looking for a pattern helps you ___.',['guess randomly','predict what will come next based on what has happened so far','skip the work','only in number sense'],1)]),
Sc('Science: Inquiry and STEM Connections','Grade 4 Science: scientific inquiry involves asking questions, making hypotheses, testing, recording, and forming conclusions. STEM connects science, technology, engineering, and math.',[
  ('A hypothesis is ___.',['a proven fact','a best guess/prediction about the answer to a question, based on prior knowledge','a question','a conclusion'],1),
  ('In an experiment, the variable you change is the ___.',['controlled variable','independent variable','dependent variable','constant'],1),
  ('The dependent variable is ___.',['what you change','what you keep the same','what you measure (the result)','the materials list'],2),
  ('A conclusion should ___.',['introduce a new idea','state whether the hypothesis was supported and what was learned','list materials','be written before the experiment'],1),
  ('STEM stands for ___.',['Science, Teaching, Energy, Mathematics','Science, Technology, Engineering, Mathematics','Society, Technology, Economics, Medicine','Science, Tests, Experiments, Methods'],1)]),
SS('Culminating Task: Community Action Plan','Grade 4 Social Studies: students apply knowledge of communities, environment, rights, and citizenship to develop a local action plan addressing a community issue.',[
  ('A community action plan addresses ___.',['only global issues','a local issue by identifying problems and proposing realistic solutions','only government problems','only school issues'],1),
  ('When presenting a community plan, you should include ___.',['only problems with no solutions','the problem, proposed solutions, and who is responsible for each action','only pictures','only historical information'],1),
  ('Effective community action involves ___.',['only one person deciding','collaboration and input from community members','ignoring different viewpoints','only money'],1),
  ('Which is a real example of community action?',['Ignoring local pollution','A petition to create a new park in a neighbourhood','Waiting for others to fix issues','Only complaining'],1),
  ('Why do citizens need to be active in their community?',['They do not','Active citizens make their communities safer, healthier, and more equitable','Only politicians should act','Change is impossible'],1)])]),
day(30,[
L('Year Review: Language Arts','Grade 4 Language Arts comprehensive review covering reading, writing, oral communication, grammar, and media literacy.',[
  ('The main idea is ___.',['a small detail','what the whole text is mostly about','the last sentence','the title only'],1),
  ('A simile uses ___ to compare.',['is/was','like or as','metaphor','adjective'],1),
  ('An inferring reader ___.',['only reads the words on the page','uses text evidence plus prior knowledge to understand unstated ideas','guesses randomly','reads very slowly'],1),
  ('The purpose of a summary is to ___.',['retell every detail','include opinions','briefly restate the main ideas in your own words','make the text longer'],2),
  ('Editing focuses on ___, while proofreading focuses on ___ .',['spelling, content','content/ideas, mechanics (spelling/grammar/punctuation)','grammar, length','length, style'],1)]),
M('Year Review: Mathematics','Grade 4 Mathematics comprehensive review: all strands.',[
  ('7 × 8 + 4 = ?',['55','60','52','56'],1),
  ('3/4 is equivalent to ___.',['6/10','6/8','9/16','5/6'],1),
  ('0.6 + 0.7 = ?',['1.2','1.3','1.0','0.13'],1),
  ('Area of a 7 cm × 4 cm rectangle = ?',['22 cm²','28 cm²','14 cm²','11 cm²'],1),
  ('The probability of rolling an even number on a 6-sided die = ?',['1/6','1/3','1/2','2/3'],2)]),
Sc('Year Review: Science','Grade 4 Science comprehensive review across all strands.',[
  ('The three rock types are ___.',['granite, marble, sandstone','igneous, sedimentary, metamorphic','volcanic, riverbed, mountain','hard, soft, medium'],1),
  ('A food chain starts with a ___.',['herbivore','carnivore','producer (plant)','decomposer'],2),
  ('Refraction is the ___ of light.',['reflection','absorption','bending (change of direction)','speeding up'],2),
  ('The Moon\'s phases are caused by ___.',['clouds','different amounts of the Moon\'s sunlit side visible from Earth','the Moon glowing itself','seasons'],1),
  ('Biodiversity means ___.',['all animals being the same','the variety of organisms in an ecosystem','only plants in a habitat','one type of rock'],1)]),
SS('Year Review: Social Studies','Grade 4 Social Studies comprehensive review.',[
  ('Confederation year = ?',['1776','1867','1900','1931'],1),
  ('Ancient civilization that developed democracy = ?',['Rome','Egypt','China','Greece'],3),
  ('Canada has ___ official languages.',['1','2','3','4'],1),
  ('Rights and responsibilities in a democracy ___.',['are opposite','go together: rights give freedom; responsibilities ensure respect for others','are unrelated','only adults have them'],1),
  ('Conservation means ___.',['wasting resources','using resources wisely for future generations','never using natural resources','only saving money'],1)])]),
]

write_new(4, g4)
print('Grade 4 done.')
