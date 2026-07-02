#!/usr/bin/env python3
"""Full Grade 3 — all 30 days."""
import sys
sys.path.insert(0,'/sessions/wonderful-keen-tesla/mnt/gradesbooster')
from gen_curriculum import sub,day,write_new

U='https://tvolearn.com/pages/grade-3'
R='TVO Learn: Grade 3'

def L(t,s,q): return sub('Language',t,s,R,U,q)
def M(t,s,q): return sub('Math',t,s,R,U,q)
def Sc(t,s,q): return sub('Science',t,s,R,U,q)
def SS(t,s,q): return sub('SocialStudies',t,s,R,U,q)

g3=[
# ── DAYS 1-15 ──────────────────────────────────────────────────────────
day(1,[
L('Reading Comprehension: Main Idea','Students identify the main idea and supporting details in short non-fiction texts. The main idea is what the whole passage is mostly about; details explain or support it.',[
  ('The main idea of a passage is ___.',['one small detail','what the whole passage is mostly about','the last sentence','a random fact'],1),
  ('Supporting details ___.',['introduce new topics unrelated to the main idea','explain or give examples that support the main idea','are always the first sentence','are always in brackets'],1),
  ('Where is the main idea often found?',['Only in the last paragraph','In the middle of the text','Often in the first or last sentence of a paragraph','Only in illustrations'],2),
  ('Which question helps find the main idea?',['Who wrote this?','When was this written?','What is this mostly about?','How long is this?'],2),
  ('A passage about how bees make honey is mostly about ___.',['flowers','trees','the honey-making process of bees','weather patterns'],2)]),
M('Place Value: Ones, Tens, Hundreds','Students identify the value of digits in numbers up to 999. In 347, the 3 is in the hundreds place (300), the 4 in the tens place (40), and the 7 in the ones place (7).',[
  ('In 456, the digit in the tens place is ___.',['4','5','6','45'],1),
  ('What is the value of the 3 in 382?',['3','30','300','3000'],2),
  ('Which number has 5 hundreds, 2 tens, and 8 ones?',['258','528','582','825'],1),
  ('In 709, which digit is in the ones place?',['7','0','9','70'],2),
  ('What is 600 + 40 + 3?',['463','634','643','364'],2)]),
Sc('Growth and Changes in Animals','Students explore how animals change as they grow, including complete and incomplete metamorphosis in insects, and growth in mammals, birds, and reptiles.',[
  ('Complete metamorphosis has ___ stages.',['2','3','4','5'],2),
  ('The four stages of complete metamorphosis are ___.',['egg, larva, pupa, adult','egg, baby, teen, adult','birth, growth, death, rebirth','seed, sprout, plant, flower'],0),
  ('A caterpillar is the ___ stage of a butterfly.',['egg','larva','pupa','adult'],1),
  ('Incomplete metamorphosis does NOT have a ___ stage.',['egg','nymph','adult','pupa'],3),
  ('Which animal goes through complete metamorphosis?',['Dog','Frog (it goes through stages but it is incomplete)','Butterfly','Snake'],2)]),
SS('Types of Communities: Urban and Rural','Students compare urban (city) and rural (countryside/farm) communities in Ontario. They examine population, land use, and services available.',[
  ('An urban community is best described as ___.',['a small farming village','a large city with many people and buildings','a forest with no residents','a single-family home'],1),
  ('A rural community is best described as ___.',['a skyscraper district','a densely populated city','a farming area or small town with fewer people','an underground settlement'],2),
  ('Which service is more common in urban areas?',['Large hospital with specialists','Grain elevator','Crop fields','Ranch'],0),
  ('What do rural communities often have that urban ones typically lack?',['Subway systems','Large amounts of open farmland and natural space','Skyscrapers','Airports'],1),
  ('Which Ontario city is an example of a major urban community?',['A small northern village','Toronto','A rural township','An island cottage community'],1)])]),
day(2,[
L('Text Features: Headings, Captions, Diagrams','Students identify and use text features in non-fiction books and articles to navigate text and understand content better.',[
  ('A heading in a non-fiction text ___.',['tells a story','gives the author\'s name','shows what a section is about','is the same as a caption'],2),
  ('A caption is ___.',['a type of heading','a large title','the words under a picture explaining what it shows','a table of contents'],2),
  ('A diagram with labels helps readers ___.',['enjoy the story more','see and understand how something works or is structured','find the author','read faster'],1),
  ('Why do non-fiction books use text features?',['To make the book longer','To help readers find and understand information more easily','Only for decoration','Only for young readers'],1),
  ('A table of contents tells you ___.',['the definition of words','where chapters and sections start','who wrote the book','what pictures look like'],1)]),
M('Addition with Regrouping','Students add 2- and 3-digit numbers with regrouping (carrying). They understand that when a column totals 10 or more, they carry 1 to the next column.',[
  ('47 + 35 = ?',['72','82','73','83'],1),
  ('When a column in addition totals 10 or more, you ___.',['write the full number','subtract 10 and carry 1 to the next column','start over','ignore the extra'],1),
  ('256 + 138 = ?',['394','384','494','494'],0),
  ('What does "regrouping" mean in addition?',['Starting over','Carrying a group of 10 to the next place value column','Subtracting','Multiplying'],1),
  ('149 + 67 = ?',['206','216','226','196'],1)]),
Sc('Habitats and Ecosystems','Students learn that a habitat provides the living and non-living things an animal needs to survive: food, water, shelter, and space. Ecosystems include all living and non-living parts of an environment.',[
  ('A habitat is ___.',['a type of weather','the environment where an organism lives and finds what it needs to survive','only a forest','only an ocean'],1),
  ('Which is a non-living part of an ecosystem?',['Tree','Rabbit','Rock and water','Mushroom'],2),
  ('An ecosystem includes ___.',['only animals','only plants','all living and non-living things in an area and their interactions','only soil'],2),
  ('Why do different animals live in different habitats?',['They do not; all animals live in the same habitat','Because different habitats provide different food, shelter, and conditions each animal needs','Only for territory','Only for warmth'],1),
  ('Destroying a habitat by cutting down a forest would most likely ___.',['help the animals there','have no effect','force animals to find new habitats, often leading to population decline','make habitats larger'],2)]),
SS('Physical Features of Ontario','Students identify and locate major physical features of Ontario on a map: Great Lakes, Canadian Shield, Niagara Falls, Lake Simcoe, and major rivers.',[
  ('The Great Lakes are ___.',['mountain ranges','rivers in northern Ontario','a chain of five large freshwater lakes on Ontario\'s southern border','a type of Canadian animal'],2),
  ('The Canadian Shield is ___.',['a hockey shield','a flat farming region','a vast ancient rock formation covering much of northern Ontario and Canada','an ocean region'],2),
  ('Niagara Falls is located between ___.',['Lake Superior and Lake Huron','Lake Erie and Lake Ontario','Lake Ontario and Lake Huron','Lake Huron and Lake Michigan'],1),
  ('Which is Ontario\'s capital city?',['Ottawa','Montreal','Toronto','Hamilton'],2),
  ('Which direction is northern Ontario relative to southern Ontario?',['South','East','West','North'],3)])]),
day(3,[
L('Vocabulary: Context Clues','Students use context clues — the surrounding words and sentences — to figure out the meaning of unfamiliar words without a dictionary.',[
  ('Context clues are ___.',['clues found in a picture only','words and information surrounding an unfamiliar word that help explain its meaning','a type of dictionary','always found in the title'],1),
  ('In "The enormous elephant, nearly as tall as a house, walked slowly," enormous means ___.',['tiny','fast','very large','colourful'],2),
  ('In "She was famished and couldn\'t wait to eat dinner," famished means ___.',['excited','very hungry','tired','late'],1),
  ('Why are context clues useful?',['They are not useful','They let readers figure out word meanings from the text without stopping to use a dictionary','Only for hard books','Only for adults'],1),
  ('Which strategy uses context clues?',['Skipping the word','Looking at how the word is used in the sentence and paragraph to guess its meaning','Only using a dictionary','Sounding out letters'],1)]),
M('Subtraction with Regrouping','Students subtract 2- and 3-digit numbers using regrouping (borrowing). They understand borrowing from the next column when the top digit is smaller.',[
  ('84 - 37 = ?',['47','57','53','43'],0),
  ('When the top digit in a column is smaller than the bottom, you ___.',['skip the subtraction','regroup (borrow) from the next column to the left','add them','multiply'],1),
  ('352 - 176 = ?',['276','176','186','176'],1),
  ('Which is the first step in 503 - 248?',['Subtract hundreds first','Subtract 8 from 3, regrouping from the tens (then hundreds) column','Add the numbers','Multiply'],1),
  ('427 - 189 = ?',['238','248','228','268'],0)]),
Sc('Soils in the Environment','Students investigate types of soil (sand, clay, loam) and their properties. They explore how soil supports plant growth and is important to ecosystems.',[
  ('Which type of soil drains water the fastest?',['Clay','Loam','Sand','Silt'],2),
  ('Clay soil is described as ___.',['gritty and fast-draining','very fertile and balanced','dense, heavy, and slow-draining','dark and crumbly'],2),
  ('Loam is considered ideal for growing plants because ___.',['it has no nutrients','it drains instantly','it has a balanced mix of sand, silt, and clay with good nutrients and drainage','it is always wet'],2),
  ('Soil is important because ___.',['it only comes in one type','it supports plant growth and is home to many organisms like earthworms and bacteria','only farmers need it','it has no nutrients'],1),
  ('What lives in soil and helps break down organic matter?',['Only rocks','Earthworms, bacteria, and fungi','Only large animals','Only plants'],1)]),
SS('Government: Federal, Provincial, Municipal','Students learn the three levels of government in Canada and their responsibilities.',[
  ('The federal government of Canada is responsible for ___.',['collecting garbage','fixing local roads','national defence, immigration, and the currency','setting school hours'],2),
  ('The provincial government of Ontario is responsible for ___.',['the national army','international affairs','education, health care, and provincial roads','the city\'s parks'],2),
  ('The municipal (city/town) government is responsible for ___.',['immigration law','national defence','local roads, parks, garbage collection, and local bylaws','provincial health care'],2),
  ('Who is the leader of the federal government of Canada?',['The Premier','The Mayor','The Prime Minister','The Governor General'],2),
  ('A school in Ontario falls under ___ government responsibility.',['federal','provincial','municipal','international'],1)])]),
day(4,[
L('Fiction vs Non-Fiction','Students distinguish fiction (invented stories with characters, plot, and setting) from non-fiction (factual, real-world information).',[
  ('A fiction text ___.',['only contains facts','is based on real events','contains invented stories and characters','is always about animals'],2),
  ('A non-fiction text ___.',['contains made-up stories','is always a novel','provides factual information about real topics','is always written by scientists'],2),
  ('Which is an example of fiction?',['A science textbook','A newspaper article','A story about a talking dragon who saves a kingdom','A biography of a real person'],2),
  ('Which is an example of non-fiction?',['A story about a magical school','A fairy tale','A book about how volcanoes form','A book about an imaginary city'],2),
  ('How can you tell if a book is fiction or non-fiction?',['By the number of pages','Fiction has invented events and characters; non-fiction has real facts and information','Only by the cover colour','Only by the title'],1)]),
M('Multiplication: Concept and Arrays','Students learn multiplication as repeated addition and model it with arrays. 3 × 4 means 3 groups of 4 (or 4 + 4 + 4 = 12).',[
  ('3 × 4 = ?',['7','10','12','14'],2),
  ('Multiplication is the same as ___.',['taking away','repeated addition','dividing','guessing'],1),
  ('An array of 2 rows and 5 columns has how many items?',['7','8','9','10'],3),
  ('5 × 3 can be shown as ___.',['5 groups of 5','3 groups of 5','5 groups of 3 (or 3 groups of 5 — both equal 15)','only 5 + 3'],2),
  ('Which number sentence shows 3 groups of 6?',['3 + 6 = 9','3 − 6','3 × 6 = 18','6 − 3 = 3'],2)]),
Sc('Forces Causing Movement','Students learn that forces (push, pull, gravity, friction, magnetism) can cause objects to start, stop, speed up, or change direction.',[
  ('A force is ___.',['a type of animal','a push or pull that can change an object\'s motion','only wind','only gravity'],1),
  ('Gravity is a force that ___.',['pushes things sideways','pulls objects toward Earth (or any large mass)','only affects large objects','only works in space'],1),
  ('Friction is a force that ___.',['speeds objects up always','acts between moving surfaces to slow motion','only affects liquids','only exists in water'],1),
  ('Which force keeps planets orbiting the Sun?',['Friction','Air resistance','Magnetism','Gravity'],3),
  ('A magnet can ___ a metal object without touching it.',['break','paint','attract or repel','melt'],2)]),
SS('Natural Resources','Students identify Ontario\'s natural resources (water, forests, minerals, farmland) and how they are used sustainably.',[
  ('A natural resource is ___.',['something made in a factory','something found in nature that humans use','only a type of animal','only oil and gas'],1),
  ('Which is an example of a natural resource?',['Plastic','Steel beam','Fresh water','Nylon'],2),
  ('Forestry in Ontario provides ___.',['steel and iron','timber for lumber and paper products','crude oil','electronics'],1),
  ('Sustainable use of resources means ___.',['using as much as possible as fast as possible','using resources in ways that don\'t permanently deplete them for future generations','never using any resources','only using human-made resources'],1),
  ('Ontario\'s Great Lakes are an important natural resource because ___.',['they are in the mountains','they provide drinking water, fishing, transportation, and hydroelectric power','only for recreation','they are very small'],1)])]),
day(5,[
L('Writing: Paragraphs','Students learn to write a paragraph with a topic sentence, at least three supporting detail sentences, and a concluding sentence.',[
  ('The topic sentence of a paragraph ___.',['ends the paragraph','introduces the main idea of the paragraph','is always the longest sentence','only gives one detail'],1),
  ('Supporting sentences in a paragraph ___.',['change the topic','give details, examples, or reasons that support the topic sentence','are always questions','are written randomly'],1),
  ('A concluding sentence ___.',['introduces a new idea','copies the topic sentence word for word','wraps up the paragraph\'s ideas','is optional'],2),
  ('A paragraph about dogs should NOT include ___.',['details about dogs\' loyalty','facts about dog breeds','information about dog training','unrelated facts about cars'],3),
  ('A good paragraph has ___.',['only one sentence','a topic sentence, supporting details, and a conclusion','only questions','no main idea'],1)]),
M('Multiplication: Facts to 5','Students learn and practise multiplication facts with factors up to 5.',[
  ('2 × 5 = ?',['7','8','9','10'],3),
  ('4 × 3 = ?',['9','10','11','12'],3),
  ('5 × 5 = ?',['20','22','25','30'],2),
  ('3 × 3 = ?',['6','7','8','9'],3),
  ('What multiplication fact is shown by: ●●●●, ●●●●, ●●●●?',['3 + 4','3 × 4 = 12','4 + 3','4 × 4'],1)]),
Sc('Simple Machines: Lever and Inclined Plane','Students explore levers (a bar that pivots on a fulcrum) and inclined planes (a ramp) as simple machines that make work easier.',[
  ('A lever is a ___.',['type of wheel','bar or plank that pivots on a fulcrum to lift or move things','type of screw','type of pulley'],1),
  ('The fulcrum is ___.',['the load','the effort force','the pivot point of a lever','the ramp'],2),
  ('An inclined plane is ___.',['a flat surface','a slanted surface (ramp) that reduces the force needed to move an object upward','a wheel on an axle','a wedge only'],1),
  ('A ramp makes it easier to ___.',['multiply numbers','push objects to a higher level without lifting the full weight straight up','run faster','make noise'],1),
  ('A seesaw is an example of a ___.',['wedge','screw','pulley','lever'],3)]),
SS('Using Maps: Scale and Direction','Students read and use simple maps, understanding cardinal directions, a compass rose, map legend/key, and basic scale.',[
  ('Cardinal directions are ___.',['up, down, left, right','north, south, east, west','large, small, medium, tiny','spring, summer, fall, winter'],1),
  ('A map legend (key) tells you ___.',['the map\'s author','what the symbols and colours on the map mean','how large the country is','who made the map'],1),
  ('A compass rose on a map shows ___.',['the scale','distances','direction (north, south, east, west and intermediate directions)','symbols'],2),
  ('Map scale tells you ___.',['the population of cities','what symbols mean','the relationship between distances on the map and real-world distances','who drew the map'],2),
  ('On most maps, north is located ___.',['at the bottom','on the right','at the top','on the left'],2)])]),
day(6,[
L('Punctuation: Commas and Apostrophes','Students use commas in lists (I have a cat, a dog, and a bird) and apostrophes for contractions (don\'t, can\'t) and possessives (Tom\'s book).',[
  ('In a list of three items, where do commas go?',['Only after the last item','Between each item (and before "and" in the series)','Only at the start','Nowhere'],1),
  ('Which sentence uses commas correctly in a list?',['I bought apples oranges and bananas.','I bought apples, oranges, and bananas.','I bought, apples, oranges and bananas.','I bought apples, oranges and, bananas.'],1),
  ('An apostrophe in "don\'t" shows ___.',['possession','a missing letter (contraction of "do not")','a question','a list'],1),
  ('An apostrophe in "Maria\'s backpack" shows ___.',['a contraction','a question','that the backpack belongs to Maria (possession)','a list'],2),
  ('Which word is a contraction?',['Cannot','Can\'t','Cant','Cannt'],1)]),
M('Division: Sharing and Grouping','Students explore division as fair sharing and as grouping. 12 ÷ 3 means sharing 12 into 3 equal groups (4 each) or making groups of 3 from 12 (4 groups).',[
  ('12 ÷ 4 = ?',['3','4','5','6'],0),
  ('Division can be thought of as ___.',['repeated multiplication','fair sharing into equal groups','random sorting','only subtraction'],1),
  ('15 ÷ 3 = ?',['4','5','6','7'],1),
  ('If 20 students are divided into groups of 5, how many groups are there?',['3','4','5','6'],1),
  ('8 ÷ 8 = ?',['0','1','8','64'],1)]),
Sc('Simple Machines: Wheel-and-Axle and Pulley','Students explore how wheels with axles and pulleys reduce friction and redirect force to make work easier.',[
  ('A wheel-and-axle consists of ___.',['two levers','a large wheel attached to a smaller rod (axle)','a rope and a groove','a ramp and a slope'],1),
  ('The wheel reduces ___.',['speed always','friction, making it easier to move heavy loads','weight','gravity'],1),
  ('A pulley is used to ___.',['pry things apart','join pieces of wood','lift or lower loads using a rope and a grooved wheel','push objects up a ramp'],2),
  ('Which everyday object uses a wheel-and-axle?',['Scissors','A nail','A bicycle wheel and its axle','A ramp at a loading dock'],2),
  ('A fixed pulley changes the ___ of a force.',['size','colour','direction','weight'],2)]),
SS('Indigenous Communities in Ontario','Students learn about the diversity of Indigenous communities in Ontario (First Nations, Métis, Inuit) and their relationship to the land.',[
  ('Which groups are Indigenous peoples of Canada?',['French and English','First Nations, Métis, and Inuit','Only European settlers','Immigrants from other countries'],1),
  ('Indigenous peoples\' relationship to the land includes ___.',['only farming the land for profit','deep spiritual, cultural, and practical connections to the land, water, and animals','ignoring the land','only using the land for buildings'],1),
  ('A key principle of many Indigenous cultures is ___.',['owning as much land as possible','respecting and living in balance with the natural world','never sharing resources','separating from nature'],1),
  ('The Haudenosaunee (Iroquois) are an example of ___.',['a French settlement','a European explorer group','First Nations peoples of what is now Ontario and New York State','a recent immigrant community'],2),
  ('Why is it important to learn about Indigenous cultures?',['It is not','To understand and respect the original peoples of the land and their continuing contributions','Only for history class','Only for Indigenous students'],1)])]),
day(7,[
L('Reading: Cause and Effect','Students identify cause and effect relationships in texts. A cause is why something happened; an effect is what happened as a result.',[
  ('A cause is ___.',['what happened','where something happened','why something happened','who did something'],2),
  ('An effect is ___.',['why something happened','the result of something that happened','when something happened','who caused it'],1),
  ('Signal words for cause include ___.',['so, therefore, as a result','because, since, due to','but, however, although','first, then, finally'],1),
  ('Signal words for effect include ___.',['because, since, due to','but, although, however','so, therefore, as a result','if, when, while'],2),
  ('It rained heavily. Because of this, the game was cancelled. What is the effect?',['It rained heavily','The clouds formed','The game was cancelled','The players got wet'],2)]),
M('Fractions: Halves, Thirds, Quarters','Students identify, read, and write fractions as equal parts of a whole (1/2, 1/3, 1/4). They understand that the denominator shows total equal parts.',[
  ('In the fraction 3/4, the denominator is ___.',['3','4','3/4','7'],1),
  ('1/2 means ___.',['1 part out of 3 equal parts','1 part out of 2 equal parts','2 parts out of 1 equal part','1 part out of 4 equal parts'],1),
  ('If a pizza is cut into 4 equal slices and you eat 1, you ate ___.',['1/2','1/3','1/4','1/8'],2),
  ('Which fraction is the largest?',['1/4','1/3','1/2','1/8'],2),
  ('What does the numerator tell you?',['The total equal parts','How many equal parts we have','The size of the whole','The shape of the fraction'],1)]),
Sc('Air and Water in the Environment','Students explore the properties of air (invisible but real, exerts pressure) and water in its three states. They learn about the water cycle.',[
  ('Air is ___.',['visible like smoke','invisible but takes up space and exerts pressure','only oxygen','only found in balloons'],1),
  ('The water cycle includes ___.',['only rain','evaporation, condensation, and precipitation, cycling water through air, land, and sea','only the ocean','only rivers and lakes'],1),
  ('Evaporation is when water ___.',['falls as rain','freezes into ice','changes from liquid to water vapour (gas) when heated','becomes solid'],2),
  ('Precipitation includes ___.',['only rain','rain, snow, sleet, and hail — any water that falls from clouds','only snow','only fog'],1),
  ('Why is the water cycle important?',['It is not','It continuously distributes fresh water to ecosystems around the world','Only for rain forests','Only for oceans'],1)]),
SS('Early Settlers in Ontario','Students learn how early European settlers came to Ontario, the challenges they faced, and how they built communities on the land.',[
  ('Early European settlers came to Ontario mainly from ___.',['Asia and Africa','Britain and France (and other European countries)','South America','Australia'],1),
  ('What was one major challenge early settlers in Ontario faced?',['Too many schools','Clearing dense forest to build farms and homes in a harsh climate','Too many roads','Too much food'],1),
  ('Loyalists were ___.',['Indigenous peoples','People who remained loyal to the British Crown and came to Ontario after the American Revolution','French farmers','Early traders from Asia'],1),
  ('Early settlers and Indigenous peoples sometimes ___.',['never interacted','traded goods and Indigenous peoples shared knowledge of the land','always fought','only competed'],1),
  ('What is one legacy of early settlers in Ontario?',['None','The network of towns, farms, and roads that form the basis of modern Ontario communities','Only conflict','Only poverty'],1)])]),
day(8,[
L('Writing: Narrative — Beginning, Middle, End','Students write short narratives (personal or fictional) with a clear beginning that introduces characters and setting, a middle with the main event/problem, and an end that resolves it.',[
  ('The beginning of a narrative should ___.',['solve the problem','introduce the characters, setting, and situation','summarize everything','be the longest part'],1),
  ('The middle of a narrative contains ___.',['the resolution','the credits','the main events and problem the character faces','the title'],2),
  ('The end of a narrative should ___.',['introduce new characters','resolve the problem or bring the story to a satisfying close','start a new problem','be a cliffhanger always'],1),
  ('A narrative is a ___.',['set of facts','story or personal account of events','list of instructions','type of graph'],1),
  ('Which word signals the beginning of a sequence?',['Finally','Then','First','However'],2)]),
M('Measurement: Perimeter','Students find the perimeter of 2D shapes by adding all side lengths. They understand that perimeter is the total distance around a shape.',[
  ('Perimeter is ___.',['the area inside a shape','the total distance around the outside of a shape','the weight of a shape','the height of a shape'],1),
  ('A square has sides of 4 cm each. Its perimeter is ___.',['4 cm','8 cm','12 cm','16 cm'],3),
  ('A rectangle has length 6 m and width 3 m. Its perimeter is ___.',['9 m','12 m','18 m','24 m'],2),
  ('To find the perimeter you ___.',['multiply length × width','add all the side lengths together','divide length by 2','subtract one side from another'],1),
  ('A triangle has sides 5 cm, 7 cm, and 8 cm. Perimeter = ?',['12 cm','15 cm','20 cm','22 cm'],2)]),
Sc('Rocks and Minerals','Students identify properties of rocks and minerals (colour, lustre, hardness, streak, shape) and understand that rocks are made of one or more minerals.',[
  ('A mineral is ___.',['any rock','a naturally occurring, non-living solid with a specific chemical composition','only found underground','only found in water'],1),
  ('A rock is ___.',['a single mineral only','a pure element','made up of one or more minerals bonded together','made of living material'],2),
  ('Hardness of a mineral measures ___.',['how shiny it is','how heavy it is','how resistant it is to being scratched','its colour'],2),
  ('The Mohs scale measures ___.',['weight','temperature','mineral hardness','mineral colour'],2),
  ('Igneous rocks form from ___.',['pressed layers of sediment','living organisms','cooled magma or lava','wind erosion'],2)]),
SS('Early Trading and Economy in Ontario','Students explore how early Indigenous and settler communities traded goods and how the fur trade shaped Ontario\'s early economy.',[
  ('The fur trade was important in early Ontario because ___.',['it provided animal companions','furs were highly valued in Europe for clothing and hats, driving exploration and trade','it only helped Indigenous peoples','it had no lasting effects'],1),
  ('Early Indigenous peoples traded ___.',['electronics','furs, food, and knowledge of the land','manufactured goods','cars'],1),
  ('A trading post was ___.',['a type of mail delivery','a location where Indigenous peoples and European traders exchanged goods','a school building','a government office'],1),
  ('The Hudson\'s Bay Company was ___.',['a fishing company','a major European fur-trading company that operated across Canada','an Indigenous organization','a government agency'],1),
  ('How did the fur trade affect Indigenous communities?',['It had no effect','It brought wealth and trade goods but also conflict, disease, and disruption to traditional ways of life','It only helped them','It only damaged them'],1)])]),
day(9,[
L('Grammar: Nouns, Verbs, Adjectives','Students identify nouns (person, place, thing, animal), verbs (action or state words), and adjectives (describing words) in sentences.',[
  ('A noun names a ___.',['feeling or action','person, place, thing, or animal','movement or sound','only a building'],1),
  ('A verb is a word that describes ___.',['a person or place','a colour or size','an action or state of being','only running'],2),
  ('An adjective ___.',['names a person','shows an action','describes a noun','tells when'],2),
  ('In "The tall girl ran quickly", the adjective is ___.',['girl','ran','quickly','tall'],3),
  ('In "The dog barked loudly", the verb is ___.',['The','dog','barked','loudly'],2)]),
M('Multiplication: Facts 6 to 10','Students practise multiplication facts with factors from 6 to 10.',[
  ('6 × 7 = ?',['40','42','44','46'],1),
  ('8 × 9 = ?',['62','70','72','76'],2),
  ('7 × 7 = ?',['42','46','49','51'],2),
  ('10 × 6 = ?',['56','60','66','70'],1),
  ('9 × 4 = ?',['32','34','36','40'],2)]),
Sc('Structures: Types and Properties','Students explore natural and human-made structures. They investigate properties like stability, strength, and function.',[
  ('A structure is ___.',['a type of weather event','something built or constructed to serve a purpose','only a building','only a bridge'],1),
  ('Which is a natural structure?',['A bridge','A skyscraper','A bird\'s nest','A dam built by engineers'],2),
  ('A triangular shape is used in structures because ___.',['it looks nice','triangles are very stable and resist forces without changing shape','it is easy to build','it uses less material'],1),
  ('The base of a structure should be ___.',['narrow and unstable','wide and stable for better balance','flexible always','high off the ground'],1),
  ('Which material is usually strongest for building?',['Paper','Foam','Balsa wood','Concrete or steel'],3)]),
SS('Immigration and Cultural Diversity in Ontario','Students learn how immigration has shaped Ontario\'s diverse population and culture throughout history and today.',[
  ('Immigration means ___.',['moving to another city in the same country','moving to a new country to live permanently','travelling for vacation','going to school in a different province'],1),
  ('Why do people immigrate to Ontario?',['Only for bad reasons','For opportunities, safety, family reunification, and a better quality of life','Only for the weather','They are forced to always'],1),
  ('Cultural diversity means ___.',['everyone is the same','a mix of people with different backgrounds, languages, traditions, and perspectives','only different food','only different clothing'],1),
  ('How has immigration benefited Ontario?',['It has not','It has enriched Ontario with diverse skills, cultures, foods, arts, and economic contributions','Only economically','Only culturally'],1),
  ('Which city in Ontario is one of the most culturally diverse cities in the world?',['A small northern town','Ottawa','Toronto','Thunder Bay'],2)])]),
day(10,[
L('Non-Fiction Reading: Compare and Contrast','Students identify similarities and differences between two topics in a text using compare-and-contrast structure.',[
  ('To compare means to ___.',['only list differences','identify similarities between two or more things','describe only one thing','count all the differences'],1),
  ('To contrast means to ___.',['identify similarities','describe one thing','identify differences between two or more things','combine two things'],2),
  ('Signal words for comparison include ___.',['however, but, unlike','both, also, similarly','first, then, finally','because, so, therefore'],1),
  ('Signal words for contrast include ___.',['both, also, in the same way','however, but, on the other hand, unlike','first, then, after that','because, since, due to'],1),
  ('A Venn diagram is useful for ___.',['multiplying fractions','solving equations','showing similarities and differences between two topics','ordering events in time'],2)]),
M('Measurement: Area','Students find the area of rectangles by counting square units or using the formula length × width.',[
  ('Area is ___.',['the distance around a shape','the weight of a shape','the amount of space inside a 2D shape','the length of one side'],2),
  ('A rectangle 4 cm long and 3 cm wide has an area of ___.',['7 cm','10 cm','12 cm²','14 cm'],2),
  ('Area is measured in ___.',['only centimetres','square units (cm², m², etc.)','grams','degrees'],1),
  ('To find the area of a rectangle, you ___.',['add all sides','subtract length from width','divide length by width','multiply length × width'],3),
  ('A square with side 5 m has an area of ___.',['10 m²','20 m²','25 m²','30 m²'],2)]),
Sc('Pulleys, Gears, and Compound Machines','Students learn how pulleys change the direction of a force, how gears transfer motion, and how compound machines combine two or more simple machines.',[
  ('A pulley uses a ___ to redirect or reduce force needed to lift a load.',['wedge','screw','rope and grooved wheel','lever and fulcrum'],2),
  ('Gears are used to ___.',['hold things together like nails','change the speed or direction of motion','measure weight','only decorate machines'],1),
  ('A compound machine is ___.',['a very simple tool','one that combines two or more simple machines','only a bicycle','only a computer'],1),
  ('A bicycle is a compound machine because it uses ___.',['only pedals','wheels and axles, a chain system (gears), and levers (brakes)','only gears','only a seat'],1),
  ('Which is an example of a simple machine inside a compound machine?',['A computer chip','A wheel on a bicycle','An electric motor','A battery'],1)]),
SS('Ontario\'s Relationship with the Rest of Canada','Students explore how Ontario is connected to other provinces through trade, shared government, geography, and culture.',[
  ('Ontario is connected to other provinces through ___.',['only highways','trade, shared national government, transportation, and cultural ties','no connections','only weather'],1),
  ('Which province borders Ontario to the west?',['Quebec','Manitoba','British Columbia','Nova Scotia'],1),
  ('Products made in Ontario are often ___.',['kept only in Ontario','traded to other provinces and countries','never used elsewhere','only sold locally'],1),
  ('The Trans-Canada Highway connects ___.',['only Ontario and Quebec','provinces and territories across Canada','only British Columbia and Alberta','only southern cities'],1),
  ('Why is Ontario important to Canada\'s economy?',['It is not','Ontario has a large population, a major financial centre (Toronto), and significant manufacturing and agricultural output','Only for its weather','Only for its size'],1)])]),
day(11,[
L('Reading: Point of View','Students identify the narrator\'s point of view (first person: I, me; third person: he, she, they) and consider how different perspectives shape the telling of a story.',[
  ('First-person point of view uses the pronouns ___.',['he, she, they','I, me, my, we','you, your','it, its'],1),
  ('Third-person point of view uses the pronouns ___.',['I, me, my','you, your','he, she, they, his, her, their','we, us'],2),
  ('The point of view affects ___.',['only the length of the story','what information the reader receives and how connected they feel to the narrator','only the setting','only the font'],1),
  ('In "I ran as fast as I could," the narrator is speaking in ___.',['third person','second person','first person','no person'],2),
  ('In "She grabbed her bag and ran," the narrator is speaking in ___.',['first person','second person','third person','fourth person'],2)]),
M('Data: Tally Charts and Bar Graphs','Students collect data using tally marks and represent it in a bar graph. They read and interpret graphs to answer questions.',[
  ('In a tally chart, a group of 5 is shown as ___.',['IIIII','||||','|||||  (four vertical lines with one diagonal line through)','VVVVV'],2),
  ('A bar graph shows data using ___.',['dots','lines only','bars (rectangles) of different heights or lengths','only circles'],2),
  ('What does the y-axis (vertical axis) of a bar graph typically show?',['Labels (categories)','Only colours','The quantity or amount','Only time'],2),
  ('If the bar for "apples" reaches 8 on the graph, how many apples were counted?',['4','6','8','10'],2),
  ('Why do we organise data in charts and graphs?',['To make it confusing','To make it easier to read, compare, and draw conclusions','Only for decoration','Only for adults'],1)]),
Sc('Weathering and Erosion','Students learn how wind, water, ice, and plants break down and move rocks (weathering and erosion), shaping the landscape over time.',[
  ('Weathering is the process of ___.',['building up rocks','plants growing','the breaking down of rocks and minerals by wind, water, ice, and chemicals','flooding only'],2),
  ('Erosion is ___.',['the build-up of sediment in one place','breaking rocks into minerals','the movement of weathered material (soil, rock) from one place to another','plant growth'],2),
  ('Which agent of erosion is responsible for the Grand Canyon?',['Ice','Wind','Water (the Colorado River)','Roots'],2),
  ('How do plant roots affect rocks?',['They smooth them','They have no effect','Roots can grow into rock cracks, widening them (biological weathering)','They melt rocks'],2),
  ('Which human activity can speed up erosion?',['Planting trees','Removing vegetation from slopes through logging or construction','Building stone walls','Using underground water'],1)]),
SS('Mapping Skills: Grid References','Students use a grid (using letters and numbers) to locate places on a map and practise reading coordinates.',[
  ('A map grid uses ___ and ___ to name locations.',['colours and shapes','letters and numbers','symbols and pictures','flags and icons'],1),
  ('If a city is at B3 on a grid map, where is it?',['Row A, column 3','Row B, column 3','Row 3, column B','Row C, column 2'],1),
  ('Why do maps use grids?',['Only for decoration','To make maps look better','To help locate specific places quickly and accurately','Only for large maps'],2),
  ('In a grid reference "C5", the letter usually refers to the ___.',['column','row','scale','compass direction'],1),
  ('Which tool would you use to find grid coordinates on a map?',['A thermometer','A ruler and map index','A scale model','A photograph'],1)])]),
day(12,[
L('Spelling Strategies','Students apply phonics, word patterns, and the "look-cover-write-check" strategy to spell words accurately.',[
  ('The "look, cover, write, check" strategy helps you ___.',['read faster','do maths','practise spelling by seeing, hiding, writing, and verifying the word','draw pictures'],1),
  ('A word family shares the same ___.',['first letter','word origin and spelling pattern (e.g., -at: cat, bat, hat)','number of syllables','only vowels'],1),
  ('To spell "because," you could remember ___.',['the letters B-E-C-A-U-S-E','only the first letter','it has 3 syllables','it starts with a vowel'],0),
  ('Looking for smaller words inside bigger words helps ___.',['make words longer','you remember how to spell longer words (e.g., "there" contains "here")','nothing','replace spelling practice'],1),
  ('Which of these is spelled correctly?',['Becaus','Becawse','Because','Becaze'],2)]),
M('Fractions: Comparing and Equivalent','Students compare fractions with the same denominator and explore simple equivalent fractions (1/2 = 2/4).',[
  ('Which is larger: 3/5 or 1/5?',['1/5','3/5','They are equal','Cannot tell'],1),
  ('Equivalent fractions are ___.',['fractions with the same numerator','different fractions that represent the same amount','only whole numbers','always improper'],1),
  ('1/2 is equivalent to ___.',['2/3','2/4','3/4','2/8'],1),
  ('Which fraction is equivalent to 2/3?',['3/4','4/6','3/5','4/5'],1),
  ('To compare fractions with the same denominator, compare ___.',['denominators','numerators','the size of the paper','the colours'],1)]),
Sc('Animals and Their Habitats (Ontario Focus)','Students study specific Ontario habitats (boreal forest, Great Lakes wetlands, grasslands) and animals adapted to each.',[
  ('The boreal forest in Ontario is characterized by ___.',['palm trees and warm weather','dense coniferous (evergreen) trees and cold winters','sandy deserts','tropical animals'],1),
  ('A wetland habitat provides ___.',['only open water','shallow water, dense vegetation, and rich nutrients supporting many birds, fish, and amphibians','no wildlife','only fish'],1),
  ('Which Ontario animal is well adapted to aquatic environments (ponds and rivers)?',['Prairie dog','Beaver','Desert tortoise','Coyote'],1),
  ('Why are Ontario\'s wetlands important?',['They are not','They filter water, absorb flood water, and provide habitat for many species','Only for fishing','Only for tourism'],1),
  ('The Canadian Shield in northern Ontario is home to ___.',['mainly tropical animals','mainly boreal forest wildlife including moose, black bears, and wolves','only birds','only fish'],1)]),
SS('Settlement Patterns in Ontario','Students explore why early communities developed where they did — near rivers, lakes, trade routes — and how settlement patterns continue to evolve.',[
  ('Early Ontario communities were most often built ___.',['in the middle of dense forests far from water','near rivers and lakes for water, transportation, and food','in deserts','on mountain tops'],1),
  ('Why was access to water important for early settlements?',['It was not','Rivers and lakes provided drinking water, fish, transportation routes, and power for mills','Only for bathing','Only for hunting'],1),
  ('Toronto became a major city partly because ___.',['it has the coldest winters','it is located on Lake Ontario, providing a natural harbour for trade','it has no rivers','it is in the mountains'],1),
  ('As transportation improved, settlements ___.',['shrank','spread further from waterways along roads and railways','stopped growing','moved to northern areas only'],1),
  ('Which factor still influences where cities grow today?',['Only weather','Access to transportation, employment, resources, and services','Only water like in the past','Only government decisions'],1)])]),
day(13,[
L('Reading: Asking Questions','Students learn to ask questions before, during, and after reading to monitor comprehension and engage deeply with texts.',[
  ('Asking questions before reading helps you ___.',['finish the book faster','activate prior knowledge and set a purpose for reading','write better','skip the hard parts'],1),
  ('Asking questions DURING reading helps you ___.',['read faster','think more deeply and check your understanding as you go','avoid the confusing parts','copy the text'],1),
  ('After reading, you might ask ___.',['What is this book\'s font?','Why did this happen? What would I do differently? What does this teach me?','How many pages did I read?','Who published this?'],1),
  ('A "thick question" is one ___.',['with a yes/no answer','with a one-word answer','that requires thinking and discussion — no single right answer','about the author'],2),
  ('Asking questions about a text is a sign of ___.',['poor reading','active and engaged reading','not understanding at all','skimming only'],1)]),
M('Time: Hours, Minutes, and Elapsed Time','Students tell time to the nearest minute using an analogue clock and calculate elapsed time.',[
  ('On an analogue clock, the short hand shows ___.',['minutes','seconds','hours','days'],2),
  ('On an analogue clock, the long hand shows ___.',['hours','seconds','days','minutes'],3),
  ('It is 2:15. What time is it 45 minutes later?',['2:45','3:00','3:15','2:60'],1),
  ('What does "elapsed time" mean?',['The time on the clock','How much time passes between a start and end time','The time zone','The exact time right now'],1),
  ('A movie starts at 1:30 pm and ends at 3:00 pm. How long is the movie?',['1 hour','1.5 hours','2 hours','2.5 hours'],1)]),
Sc('Energy: Forms and Sources','Students explore forms of energy (light, heat, sound, electrical, mechanical) and sources (Sun, wind, water, fossil fuels).',[
  ('Energy is defined as ___.',['a type of matter','the ability to do work or cause change','only electricity','only heat'],1),
  ('The Sun is a source of ___ energy.',['only sound','only mechanical','light and heat','only electrical'],2),
  ('Which is a renewable energy source?',['Coal','Natural gas','Oil','Wind'],3),
  ('A non-renewable energy source is ___.',['solar power','wind energy','fossil fuels (coal, oil, natural gas)','hydroelectric power'],2),
  ('Electrical energy can be transformed into ___.',['nothing','light, heat, and sound (e.g., in a light bulb, a toaster, a speaker)','only movement','only light'],1)]),
SS('Ontario\'s Economy Today','Students explore Ontario\'s major industries: manufacturing, agriculture, technology, finance, and mining.',[
  ('Which industry produces cars and vehicles in Ontario?',['Forestry','Fishing','Manufacturing','Only farming'],2),
  ('Ontario\'s Bay Street in Toronto is known for ___.',['beaches','forests','financial services and banking','mining'],2),
  ('Agriculture in Ontario produces ___.',['cars and trucks','grains, fruits, vegetables, dairy, and meat products','electronics','only wheat'],1),
  ('Ontario is Canada\'s ___ most populous province.',['least','second','largest and most','fourth'],2),
  ('Why is technology a growing industry in Ontario?',['It is not','Toronto and Waterloo have become major tech hubs attracting companies and talent globally','Only in the last month','Only one company exists'],1)])]),
day(14,[
L('Writing: Procedural Texts','Students write how-to instructions with a clear title, list of materials, numbered steps, and sequence words (first, next, then, finally).',[
  ('A procedural text tells you ___.',['a fictional story','how to do or make something step by step','a poem','a persuasive essay'],1),
  ('Sequence words in procedural writing include ___.',['however, although, but','first, next, then, finally','because, since, therefore','only nouns and verbs'],1),
  ('Why are numbered steps important in instructions?',['They are not','They tell the reader the exact order to follow','They only look nice','They replace the materials list'],1),
  ('A procedural text usually begins with ___.',['a plot twist','a conclusion','a title and a list of materials needed','a character description'],2),
  ('Which is an example of a procedural text?',['A fairy tale','A poem about rain','Step-by-step instructions on how to plant a seed','A chapter from a novel'],2)]),
M('3D Geometry: Faces, Edges, Vertices','Students identify faces, edges, and vertices on 3D shapes (cube, rectangular prism, triangular prism, cylinder, cone, sphere, pyramid).',[
  ('A cube has ___ faces.',['4','5','6','8'],2),
  ('A vertex (vertices) of a shape is ___.',['a flat surface','a straight edge','a corner where edges meet','a curved surface'],2),
  ('How many edges does a cube have?',['6','8','12','24'],2),
  ('A sphere has ___ faces, ___ edges, and ___ vertices.',['1, 0, 0','0, 0, 0','2, 1, 0','1, 1, 1'],1),
  ('A triangular prism has ___ triangular faces.',['1','2','3','4'],1)]),
Sc('Light: Reflection and Shadows','Students explore how light travels in straight lines, reflects off surfaces (mirrors), refracts (bends) when passing through water or glass, and creates shadows.',[
  ('Light travels in ___.',['curves','spirals','waves that bend easily','straight lines'],3),
  ('A shadow forms when an object ___.',['reflects all light','blocks light from passing through','absorbs all heat','only moves'],1),
  ('Reflection of light occurs when ___.',['light is absorbed completely','light passes through an object','light bounces off a surface back toward your eyes','light slows down'],2),
  ('Refraction is when light ___.',['travels in a straight line through air','bends as it passes from one medium to another (e.g., air to water)','creates a shadow','reflects off a mirror'],1),
  ('A smooth, shiny surface like a mirror gives ___.',['a blurry, scattered reflection','a clear, regular reflection','no reflection','only a shadow'],2)]),
SS('Canadian Citizenship','Students learn what it means to be a responsible citizen: following laws, voting, contributing to the community, and respecting others.',[
  ('A citizen is ___.',['only a government official','a legal member of a country who has rights and responsibilities','only an adult','only a voter'],1),
  ('Which right do Canadian citizens have?',['To break any law','To vote in federal elections','To ignore community rules','To be exempt from taxes'],1),
  ('Which is a responsibility of citizenship?',['Doing whatever you want','Obeying laws, paying taxes, and contributing positively to the community','Only voting','Only working'],1),
  ('Volunteering in your community is an example of ___.',['poor citizenship','active, responsible citizenship','only professional work','only for adults'],1),
  ('Why is respecting others\' rights important?',['It is not','A fair and safe community depends on everyone respecting each other\'s rights and dignity','Only for politicians','Only in schools'],1)])]),
day(15,[
L('Reading Strategies Review','Students review and consolidate key reading strategies: predicting, questioning, making connections, visualising, and summarising.',[
  ('Predicting while reading means ___.',['skipping ahead','using clues to guess what will happen next','always being right','only looking at pictures'],1),
  ('Making a connection to the text means ___.',['ignoring the text','relating what you read to your own experiences, other books, or the world','only memorising it','only summarising'],1),
  ('Visualising while reading means ___.',['looking at the illustrations only','creating a mental image of what the text describes','drawing your own story','skipping descriptions'],1),
  ('Summarising means ___.',['copying the whole text','retelling every tiny detail','expressing the main points and key events concisely in your own words','only reading the first line'],2),
  ('Which strategy helps when a word is confusing?',['Give up','Read on for context clues or reread the sentence','Skip it permanently','Ask someone else to read for you'],1)]),
M('Probability: Likely, Unlikely, Certain, Impossible','Students use probability language to describe the likelihood of events.',[
  ('An event is "certain" if ___.',['it will never happen','it happens by chance','it will definitely happen every time','it sometimes happens'],2),
  ('An event is "impossible" if ___.',['it might happen','it will definitely happen','it has never happened before','it cannot possibly happen'],3),
  ('Rolling a number between 1 and 6 on a standard die is ___.',['impossible','unlikely','likely','certain'],3),
  ('Getting tails on a fair coin flip is ___.',['certain','impossible','equally likely as getting heads','always impossible'],2),
  ('Drawing a red marble from a bag of only blue marbles is ___.',['certain','likely','unlikely','impossible'],3)]),
Sc('Habitats Review and Biodiversity','Students review Ontario habitats and learn that biodiversity — the variety of living things — is essential for healthy ecosystems.',[
  ('Biodiversity means ___.',['having only one type of animal','having only plants','the variety of living things in an ecosystem','only counting species'],2),
  ('High biodiversity is a sign of ___.',['an unhealthy ecosystem','a healthy ecosystem where many species interact','too many animals','too few plants'],1),
  ('Which human activity threatens biodiversity?',['Planting native gardens','Creating nature reserves','Habitat destruction through deforestation and urban sprawl','Protecting endangered species'],2),
  ('An endangered species is one that ___.',['is very common','is at risk of becoming extinct','has already gone extinct','only lives in zoos'],1),
  ('Why is protecting biodiversity important?',['It is not','Ecosystems with many species are more resilient, and all species play a role in keeping ecosystems balanced','Only for rare animals','Only for scientists'],1)]),
SS('Community Celebrations and Heritage','Students explore how Ontario communities celebrate cultural heritage through festivals, traditions, and public holidays.',[
  ('Heritage is ___.',['only old buildings','the traditions, language, values, and history passed from earlier generations','only museums','only food'],1),
  ('Canada Day (July 1) celebrates ___.',['the end of winter','Canada becoming a self-governing country in 1867','Ontario\'s founding only','a sports victory'],1),
  ('Remembrance Day (November 11) honours ___.',['Canada\'s birthday','Indigenous peoples only','Canadian soldiers who served and died in wars and peacekeeping missions','a famous inventor'],2),
  ('How do multicultural festivals contribute to Ontario communities?',['They cause conflict','They allow communities to share and celebrate diverse cultural traditions, building mutual respect','Only for food vendors','Only for tourists'],1),
  ('Why is it important to celebrate and preserve heritage?',['It is not','It connects people to their roots, builds identity, and helps communities understand their shared history','Only in museums','Only for old people'],1)])]),
# ── DAYS 16-30 ─────────────────────────────────────────────────────────
day(16,[
L('Verb Tenses: Past, Present, Future','Students identify and use past, present, and future tenses. They understand that tense tells when an action happens.',[
  ('Which sentence is in the PAST tense?',['I walk to school.','She is running.','He ate his lunch.','They will play tomorrow.'],2),
  ('Which sentence is in the PRESENT tense?',['She ran yesterday.','They will come soon.','We are playing now.','He had left already.'],2),
  ('Future tense uses the word ___.',['was','is','are','will'],3),
  ('Change "I run" to past tense.',['I will run','I am running','I ran','I running'],2),
  ('Which word signals the past tense?',['Tomorrow','Now','Yesterday','Soon'],2)]),
M('Multiplication Facts: Review to 10×10','Students consolidate multiplication facts up to 10×10 and use strategies to solve unknown facts.',[
  ('7 × 8 = ?',['54','56','58','60'],1),
  ('9 × 6 = ?',['48','52','54','58'],2),
  ('6 × 6 = ?',['32','34','36','40'],2),
  ('What strategy helps remember 9× facts?',['Count by 5s','The "10× minus 1 group" strategy: 9×7 = 70−7 = 63','Random guessing','Skip by 4s'],1),
  ('10 × 10 = ?',['10','20','100','1000'],2)]),
Sc('Magnets','Students explore properties of magnets: poles (N/S), attraction, repulsion, magnetic fields, and everyday uses.',[
  ('Opposite poles of magnets ___.',['repel','attract','do nothing','break apart'],1),
  ('Like poles of magnets ___.',['attract strongly','repel (push away)','have no reaction','stick together always'],1),
  ('A magnetic field is ___.',['visible lines you can see','the region around a magnet where magnetic forces act','only at the poles','only inside iron'],1),
  ('Which material is attracted to a magnet?',['Wood','Glass','Plastic','Iron/Steel'],3),
  ('Magnets are used in ___.',['only refrigerators','many devices including compasses, speakers, motors, and credit cards','nothing modern','only toys'],1)]),
SS('Urban and Rural Communities: Services','Students compare the services available in urban and rural communities, exploring how geography and population affect service availability.',[
  ('Which service is more commonly found in large urban areas?',['A small one-room schoolhouse','A major hospital with specialist care','A grain elevator','A logging camp'],1),
  ('A rural community might rely on ___.',['subway systems','long-distance travel to access specialised medical and retail services','skyscrapers','a packed public transit system'],1),
  ('Which statement about population is true?',['Urban areas have fewer people than rural areas','Urban areas have more people per square kilometre than rural areas','Both have the same population density','Rural areas are always more populated'],1),
  ('What is one advantage of rural communities?',['More restaurants','Closer to nature, lower cost of living, quieter environments','More hospitals','Faster internet access always'],1),
  ('What is one challenge of rural communities in Ontario?',['Too many people','Limited access to certain services and employment opportunities','Too much traffic','Too many schools'],1)])]),
day(17,[
L('Summarising: Non-Fiction','Students summarise non-fiction texts by identifying the main idea, key details, and omitting unnecessary information.',[
  ('To summarise a non-fiction text, you should ___.',['copy every sentence','include only the main idea and key supporting details in your own words','make up new information','only write the first paragraph'],1),
  ('Which information should be OMITTED in a summary?',['The main idea','Key supporting facts','Interesting minor details that do not support the main idea','The topic of the text'],2),
  ('A good summary is ___.',['as long as the original','longer than the original','much shorter than the original while keeping the key ideas','exactly one word'],2),
  ('The first sentence of a summary should ___.',['be a question','state the main idea of the text','give a personal opinion','list all the details'],1),
  ('Why is summarising an important reading skill?',['It is not','It shows you understood the key ideas and helps you remember and discuss what you read','Only for tests','Only for non-fiction'],1)]),
M('Fractions on a Number Line','Students place fractions on a number line between 0 and 1, understanding that fractions represent parts between whole numbers.',[
  ('On a number line, 1/2 is located ___.',['at 0','at 1','halfway between 0 and 1','past 1'],2),
  ('Which fraction is closer to 1 on a number line?',['1/4','1/8','3/4','1/2'],2),
  ('Where would 1/4 be placed on a number line from 0 to 1?',['At 0','One quarter of the way between 0 and 1','At 1','Three quarters of the way between 0 and 1'],1),
  ('Which fraction is closest to 0?',['3/4','1/2','1/4','1/8'],3),
  ('On a number line from 0 to 1, 3/4 is ___.',['before 1/2','after 1/2 but before 1','after 1','at 1'],1)]),
Sc('Forces: Gravity and Friction','Students investigate gravity as a downward force and friction as a resistance force. They explore how these affect motion.',[
  ('Gravity is a force that ___.',['pushes objects upward','pulls objects toward the centre of the Earth','has no effect on motion','only affects large objects'],1),
  ('Friction is a force that ___.',['speeds objects up','pulls objects downward','resists the motion of surfaces sliding against each other','has no effect on objects'],2),
  ('A smooth surface causes ___ friction than a rough surface.',['more','the same','less','no'],2),
  ('Without friction, it would be very difficult to ___.',['fly a kite','walk, drive, or grip anything (friction is essential for traction)','swim','see clearly'],1),
  ('Gravity pulls all objects downward at the same rate regardless of ___.',['their colour','their size and mass (in a vacuum)','their shape','their temperature'],1)]),
SS('Ontario and the Environment','Students explore environmental issues in Ontario: pollution, conservation, and the role citizens and government play in protecting natural spaces.',[
  ('The Greenbelt in Ontario is ___.',['a type of vegetable garden','a protected area of farmland, forests, and wetlands around the Greater Toronto Area','a sports field','a government building'],1),
  ('Water pollution in the Great Lakes is caused by ___.',['natural processes only','industrial discharge, agricultural runoff, and urban sewage','only rain','only wildlife'],1),
  ('Conservation means ___.',['using resources as fast as possible','careful management and protection of natural resources','only recycling paper','only planting trees'],1),
  ('How can citizens help protect Ontario\'s environment?',['By doing nothing','Reducing waste, using less energy, supporting conservation efforts, and making sustainable choices','Only by voting','Only through protests'],1),
  ('An Ontario Provincial Park is ___.',['a city park','a protected natural area where wildlife and ecosystems are preserved','a private farm','a golf course'],1)])]),
day(18,[
L('Poetry: Reading and Interpreting','Students read various poem forms (haiku, cinquain, limerick) and identify poetic elements: rhyme, rhythm, stanza, simile, and metaphor.',[
  ('Rhyme in poetry means ___.',['repeating the same word','ending lines with words that have the same ending sound','making lines very long','using no punctuation'],1),
  ('A simile compares two things using "like" or "as." Which is a simile?',['The moon is a lantern in the sky','He ran like the wind','She is a shining star','The thunder spoke to the rain'],1),
  ('A metaphor compares two things WITHOUT "like" or "as." Which is a metaphor?',['She runs like a deer','He is as tall as a tree','Life is a journey','The rain falls like tears'],2),
  ('A haiku has ___ syllables in the pattern 5-7-5.',['15','17','19','21'],1),
  ('A stanza in a poem is like a ___ in prose writing.',['sentence','paragraph','chapter','word'],1)]),
M('Money: Counting and Making Change','Students identify Canadian coins and bills, count amounts of money, and calculate simple change.',[
  ('How many cents are in one dollar?',['10','50','100','1000'],2),
  ('Which coin is worth 25 cents?',['Nickel','Dime','Quarter','Loonie'],2),
  ('$2.50 + $1.75 = ?',['$3.25','$4.00','$4.25','$4.50'],2),
  ('You have $5.00 and spend $3.25. How much change do you get?',['$1.75','$2.75','$1.25','$2.25'],0),
  ('A toonie is worth ___.',['$1.00','$0.25','$2.00','$0.50'],2)]),
Sc('Rocks: Igneous, Sedimentary, Metamorphic','Students classify rocks into three types and understand how each forms.',[
  ('Igneous rocks form from ___.',['pressed sediment layers','living organisms','metamorphism','cooled magma or lava'],3),
  ('Sedimentary rocks form from ___.',['cooled lava','metamorphism','layers of sediment (sand, silt, shells) compressed over time','volcanic eruptions'],2),
  ('Metamorphic rocks form when existing rocks are ___.',['erupted from a volcano','washed by the sea','changed by extreme heat and pressure deep in the Earth','dissolved in water'],2),
  ('Granite is an example of an ___ rock.',['sedimentary','metamorphic','igneous','fossil'],2),
  ('Fossils are most commonly found in ___ rock.',['igneous','metamorphic','sedimentary','volcanic'],2)]),
SS('Economy: Goods and Services','Students explore the difference between goods (physical products) and services (activities that meet needs), and how they are exchanged.',[
  ('Goods are ___.',['things people do for you','physical products you can hold and buy','only free things','only natural resources'],1),
  ('Services are ___.',['only food','activities that someone does for you that meet a need','physical objects you buy','only government actions'],1),
  ('Which is a GOOD?',['A haircut','A doctor\'s appointment','A new pair of shoes','A music lesson'],2),
  ('Which is a SERVICE?',['A chocolate bar','A bicycle','A plumber fixing a pipe','A book'],2),
  ('Why is trade (buying and selling goods and services) important?',['It is not','Trade allows communities to get things they need that they cannot produce themselves','Only for large countries','Only in cities'],1)])]),
day(19,[
L('Non-Fiction: Cause and Effect in Science Texts','Students practise identifying cause-and-effect relationships in non-fiction science texts using text clues and structure.',[
  ('In a science text, "because" often signals ___.',['a sequence of events','an effect','a cause coming next','the main idea'],2),
  ('In a science text, "therefore" often signals ___.',['a cause','an effect or result','a new topic','an example'],1),
  ('Which sentence contains a cause-and-effect relationship?',['The sky is blue.','Dogs are mammals.','Because the temperature dropped, water in the pond froze.','Animals need food.'],2),
  ('The cause in "The plant died because it had no water" is ___.',['The plant died','it had no water','The plant','because'],1),
  ('The effect in "The animal population declined because the habitat was destroyed" is ___.',['the habitat was destroyed','because','The animal population declined','The habitat'],0)]),
M('Patterns: Growing and Shrinking','Students identify and extend growing (increasing) and shrinking (decreasing) patterns using numbers, shapes, and objects.',[
  ('A growing pattern is one that ___.',['stays the same','decreases with each term','increases with each term','repeats in a cycle'],2),
  ('Identify the pattern: 2, 4, 6, 8... It is ___.',['shrinking by 2','growing by 2','random','staying the same'],1),
  ('What comes next in: 20, 17, 14, 11, ___?',['8','9','10','7'],0),
  ('What is the rule for: 3, 6, 9, 12...?',['Add 2','Add 3','Subtract 3','Multiply by 2'],1),
  ('Which is a growing pattern?',['10, 10, 10, 10','10, 8, 6, 4','5, 10, 15, 20','10, 9, 8, 7'],2)]),
Sc('Electricity: Static and Current','Students explore static electricity (build-up of charge) and current electricity (flowing charge that powers devices). They identify conductors and insulators.',[
  ('Static electricity is caused by ___.',['flowing electrons in a wire','a build-up of electric charge on a surface (often from friction)','magnetism only','sound waves'],1),
  ('Current electricity is ___.',['stationary charge','a flow of electrons through a conductor (like a wire)','only from batteries','only for large machines'],1),
  ('A conductor allows ___.',['no electricity to pass','only static electricity','electricity to flow through it easily','light to pass through'],2),
  ('An insulator ___.',['allows electricity to flow freely','blocks or resists the flow of electricity','attracts magnets','produces electricity'],1),
  ('Which is a good conductor of electricity?',['Rubber','Plastic','Wood','Copper wire'],3)]),
SS('Rights of Children: UNCRC','Students learn about the United Nations Convention on the Rights of the Child (UNCRC) and key rights: education, protection, participation, and health.',[
  ('The UNCRC is ___.',['a type of food','a Canadian law only','an international agreement on children\'s rights signed by most countries','a school rule'],2),
  ('According to the UNCRC, all children have the right to ___.',['only education','only health care','education, protection from harm, health care, and participation in decisions affecting them','only play'],2),
  ('Which right is described: "No child should be made to work in dangerous conditions."',['Right to education','Right to play','Right to protection from exploitation and harm','Right to a name'],2),
  ('Which right is described: "Children should be able to share their views on matters affecting them."',['Right to food','Right to health','Right to protection','Right to participate and be heard'],3),
  ('Why is knowing your rights important?',['It is not','It empowers children to recognise when rights are being violated and to seek help','Only for lawyers','Only for adults'],1)])]),
day(20,[
L('Writing: Opinion','Students write opinion paragraphs stating a clear position, giving reasons supported by evidence or examples, and using opinion language.',[
  ('An opinion is ___.',['a proven fact','a belief or view that reflects a personal perspective, not universal fact','only a complaint','only a question'],1),
  ('Opinion writing should include ___.',['only facts with no personal stance','a clear position and reasons or evidence to support it','only questions','random information'],1),
  ('Which is an opinion sentence?',['Water freezes at 0°C.','Canada is in North America.','Recess should be 30 minutes because it improves focus and wellbeing.','The Sun rises in the east.'],2),
  ('Opinion signal phrases include ___.',['first, next, finally','I believe, in my opinion, I think, it seems to me','because, since, therefore','however, although, but'],1),
  ('A conclusion in opinion writing should ___.',['start a new argument','restate your opinion and summarise your main reasons','apologise for your opinion','list new facts'],1)]),
M('Division Facts: Linking to Multiplication','Students use their knowledge of multiplication to solve division problems (fact families).',[
  ('If 4 × 5 = 20, then 20 ÷ 4 = ?',['4','5','10','20'],1),
  ('Which multiplication fact helps solve 36 ÷ 6?',['5 × 6 = 30','6 × 6 = 36','7 × 6 = 42','6 × 4 = 24'],1),
  ('A fact family for 3, 7, 21 includes ___.',['3 + 7 = 10','3 × 7 = 21 and 21 ÷ 7 = 3','3 × 7 = 21 and 3 ÷ 7 = 21','3 + 7 = 21'],1),
  ('21 ÷ 3 = ?',['6','7','8','9'],1),
  ('45 ÷ 9 = ?',['4','5','6','7'],1)]),
Sc('The Water Cycle','Students explore how water moves through the water cycle: evaporation, condensation, and precipitation. They understand how the cycle distributes fresh water.',[
  ('The water cycle is powered mainly by ___.',['wind','the Moon\'s gravity','energy from the Sun','Earth\'s rotation'],2),
  ('Evaporation is when ___.',['liquid water falls as rain','water vapour turns into liquid droplets','liquid water changes to water vapour and rises into the atmosphere','water freezes'],2),
  ('Condensation happens when ___.',['water evaporates','water vapour cools and turns into liquid water droplets (forming clouds)','it rains','water freezes into ice'],1),
  ('Precipitation includes ___.',['only rain','only snow','only fog','rain, snow, sleet, or hail falling from clouds'],3),
  ('Why is the water cycle important?',['It creates lightning','It continuously moves and purifies water, distributing fresh water to land ecosystems','Only for rivers','Only for oceans'],1)]),
SS('Cultural Practices in Ontario Communities','Students explore how cultural practices — food, clothing, music, art, language — contribute to the identity of Ontario\'s diverse communities.',[
  ('Cultural practices are ___.',['only government rules','traditions, arts, language, food, and customs that are part of a group\'s identity','only found in other countries','only for elderly people'],1),
  ('How do different cultural practices enrich Ontario communities?',['They cause confusion','They bring diverse perspectives, art, food, and ideas that make communities more vibrant','Only if everyone agrees','They do not'],1),
  ('Which is an example of a cultural practice?',['A government law','Celebrating Diwali, Eid, or Chinese New Year with traditional foods, clothing, and rituals','A traffic sign','A school timetable'],1),
  ('Respecting cultural practices means ___.',['only following your own culture','learning about and showing appreciation for the traditions of others','ignoring differences','only eating the same food'],1),
  ('Why is language part of cultural identity?',['It is not','Language carries stories, values, and worldviews of a culture — preserving it helps keep the culture alive','Only for old languages','Only for writing'],1)])]),
day(21,[
L('Reading: Inference','Students make inferences — use clues from the text plus their own knowledge to figure out what the author implies but does not state directly.',[
  ('An inference is ___.',['something stated directly in the text','a guess with no evidence','a conclusion drawn from text clues plus prior knowledge','only for non-fiction'],2),
  ('When you infer, you use ___.',['only pictures','only the title','text clues plus what you already know','only the last paragraph'],2),
  ('In "She grabbed her umbrella and slammed the door," we can infer ___.',['She is happy','She is going swimming','She might be upset and it could be raining','She has a new umbrella'],2),
  ('Inference helps readers ___.',['only read faster','understand meaning beyond what is directly stated','only for tests','only for long books'],1),
  ('Which question requires an inference?',['How many pages is this book?','Who is the author?','Why did the character act so nervously?','What is the title?'],2)]),
M('3D Shapes: Nets','Students identify and create nets — flat shapes that can be folded to make 3D shapes — for cubes, rectangular prisms, and triangular prisms.',[
  ('A net of a 3D shape is ___.',['the weight of the shape','a flat pattern that folds up to form a 3D shape','a shadow of the shape','only for squares'],1),
  ('A cube\'s net has ___ squares.',['4','5','6','8'],2),
  ('If you fold a cross-shaped net, it forms a ___.',['sphere','cylinder','triangular prism','cube'],3),
  ('A net helps students understand ___.',['the weight of objects','the 2D faces that make up a 3D shape','only area','only volume'],1),
  ('A rectangular prism has ___ rectangular faces.',['4','6','8','2'],1)]),
Sc('Ecosystems and Food Chains','Students explore simple food chains in Ontario ecosystems: producer → primary consumer → secondary consumer, and the concept of the food web.',[
  ('In a food chain, a producer is ___.',['an animal that hunts','a plant that makes its own food using sunlight (photosynthesis)','a decomposer','a top predator'],1),
  ('A primary consumer eats ___.',['other animals','only decomposers','plants (producers)','nothing'],2),
  ('A secondary consumer eats ___.',['only plants','primary consumers (herbivores) or omnivores','decomposers only','sunlight'],1),
  ('What happens when one link in a food chain is removed?',['Nothing changes','The whole chain is affected — populations of other organisms rise or fall','Only the bottom level changes','Only predators are affected'],1),
  ('A food web is ___.',['a single line of feeding relationships','a network of interconnected food chains showing multiple feeding relationships in an ecosystem','only for aquatic animals','only for plants'],1)]),
SS('Comparing Communities Around the World','Students compare communities in different countries with Ontario communities, exploring similarities and differences in climate, culture, economy, and geography.',[
  ('Comparing communities from different countries helps us ___.',['avoid learning about others','understand and appreciate diverse ways of living and the challenges different communities face','feel superior','only find differences'],1),
  ('A community in a desert region would face ___ challenges compared to one in Ontario.',['the same','different challenges like water scarcity and extreme heat','easier challenges','no challenges'],1),
  ('What do most communities around the world have in common?',['The same language','The same food','Basic needs like shelter, food, water, and community connections','The same government'],2),
  ('How does geography affect a community\'s economy?',['It does not','A community near the ocean may rely on fishing; one with forests may rely on forestry','Only in Canada','Only in ancient times'],1),
  ('Cultural exchange between communities ___.',['causes problems','enriches both communities through shared ideas, technologies, and traditions','only benefits tourists','only benefits one side'],1)])]),
day(22,[
L('Grammar: Adverbs and Prepositions','Students identify adverbs (modify verbs: how, when, where) and prepositions (show relationship in space/time: in, on, under, after).',[
  ('An adverb modifies a ___.',['noun','pronoun','adjective only','verb, adjective, or other adverb'],3),
  ('In "She sang beautifully," the adverb is ___.',['She','sang','beautifully','is'],2),
  ('A preposition shows ___.',['an action','a description of a noun','a relationship between a noun and another word (position, time, direction)','only movement'],2),
  ('In "The cat sat under the table," the preposition is ___.',['cat','sat','under','table'],2),
  ('Which word is an adverb?',['Happy','Quickly','Dog','Soft'],1)]),
M('Geometry: Congruence and Symmetry','Students identify congruent shapes (same size and shape) and lines of symmetry. They recognise symmetrical shapes by folding.',[
  ('Congruent shapes are ___.',['the same colour','the same size AND shape','only the same size','only the same colour'],1),
  ('A line of symmetry divides a shape into ___.',['unequal parts','two random pieces','two mirror-image halves','only triangles'],2),
  ('How many lines of symmetry does a square have?',['1','2','3','4'],3),
  ('A circle has ___ lines of symmetry.',['1','4','none','infinite (unlimited)'],3),
  ('Which shape has exactly one line of symmetry?',['Square','Circle','Equilateral triangle','Isosceles triangle'],3)]),
Sc('Sound: Vibration, Pitch, Volume','Students explore how sound is produced (vibration), transmitted, and detected. They investigate pitch (high/low) and volume (loud/soft).',[
  ('Sound is produced by ___.',['magnetism','heat','light','vibration of an object'],3),
  ('Pitch describes how ___ or ___ a sound is.',['loud or soft','fast or slow','long or short','high or low'],3),
  ('Volume describes how ___ or ___ a sound is.',['high or low in pitch','fast or slow','loud or soft','short or long'],2),
  ('A tighter or shorter string on a guitar produces ___.',['a lower pitch','the same pitch','a higher pitch','no sound'],2),
  ('Sound travels as ___.',['light waves','magnetic fields','vibrations through a medium (air, water, or solid material)','electrical current'],2)]),
SS('Confederation and Canada\'s History','Students learn about Confederation (1867) when four provinces joined to form Canada, and how the country grew to its current size.',[
  ('Confederation happened in ___.',['1776','1812','1867','1900'],2),
  ('The first four provinces to join Confederation were ___.',['Ontario, Quebec, Nova Scotia, and New Brunswick','British Columbia, Alberta, Saskatchewan, Manitoba','Ontario, Quebec, British Columbia, Manitoba','All ten provinces at once'],0),
  ('Canada\'s first Prime Minister was ___.',['Pierre Trudeau','Wilfrid Laurier','John A. Macdonald','Alexander Mackenzie'],2),
  ('How many provinces and territories does Canada have today?',['10 provinces and 2 territories','10 provinces and 3 territories','9 provinces and 3 territories','12 provinces and territories'],1),
  ('Why is Confederation important in Canadian history?',['It is not','It united separate British colonies into a new country with a federal government and shared laws','Only for Quebec','Only for Ontario'],1)])]),
day(23,[
L('Research Skills: Finding Information','Students practise using books, encyclopedias, and reliable websites to find information. They evaluate source reliability.',[
  ('A reliable source of information is one that ___.',['anyone can edit without verification','is authored by experts, fact-checked, and cites evidence','is only on social media','only contains pictures'],1),
  ('An index in a non-fiction book helps you ___.',['read faster','find specific topics alphabetically at the back of the book','find the author\'s biography','draw pictures'],1),
  ('Why should you look at multiple sources?',['You should not','To get a fuller picture and check that information is accurate and consistent across sources','Only for school projects','Only if you are unsure'],1),
  ('When using the internet for research, you should ___.',['click any link','use only social media','check that the website is reputable and that information is current','copy and paste everything'],2),
  ('Which is a signal that a website may be unreliable?',['It has a known author and institution','It cites other reliable sources','It looks professional','It has no author, no sources, and makes extreme claims'],3)]),
M('Area and Perimeter: Problem Solving','Students solve real-world problems involving area and perimeter of rectangles.',[
  ('A garden is 8 m long and 5 m wide. What is its area?',['13 m²','26 m²','40 m²','45 m²'],2),
  ('A garden is 8 m long and 5 m wide. What is its perimeter?',['13 m','26 m','40 m','45 m'],1),
  ('A room has a perimeter of 24 m. If it is 8 m long, how wide is it?',['3 m','4 m','6 m','8 m'],1),
  ('A square has an area of 36 cm². What is the side length?',['6 cm','7 cm','8 cm','9 cm'],0),
  ('Two rectangles have the same perimeter but different areas. This is ___.',['impossible','always false','possible — shapes can have the same perimeter but different areas','only for squares'],2)]),
Sc('Human Impact on the Environment','Students explore positive and negative human impacts on natural environments. They understand stewardship and sustainability.',[
  ('Which is a NEGATIVE human impact on the environment?',['Planting trees','Creating wildlife corridors','Dumping toxic waste in a river','Setting up nature reserves'],2),
  ('Which is a POSITIVE human impact on the environment?',['Burning fossil fuels','Overfishing','Urban sprawl replacing forests','Reforestation and habitat restoration'],3),
  ('Stewardship means ___.',['exploiting resources for maximum profit','responsible management and care of the environment for future generations','only recycling','only for governments'],1),
  ('Why is reducing plastic waste important?',['It is not','Plastic persists in ecosystems for hundreds of years and harms wildlife and waterways','Only for marine animals','Only in cities'],1),
  ('How can Grade 3 students help the environment?',['They cannot','By reducing, reusing, and recycling; planting gardens; and raising awareness','Only by getting older first','Only by donating money'],1)]),
SS('Human Rights and Equity','Students explore the concept of human rights and equity — ensuring everyone gets what they need to thrive, not just equal treatment.',[
  ('Human rights are ___.',['privileges earned by good behaviour','basic rights that every person has simply because they are human','only for citizens of wealthy countries','only for adults'],1),
  ('Equity means ___.',['everyone gets exactly the same','everyone gets what they specifically need to have a fair chance','only equality of opportunity','never helping anyone extra'],1),
  ('Which is an example of promoting equity at school?',['Giving everyone exactly the same assignment with no accommodations','Providing extra support to students who need it to achieve the same outcomes','Ignoring differences','Only helping top students'],1),
  ('Why are human rights important?',['They are not','They protect every person\'s dignity and ensure people can live free from oppression','Only for some people','Only in democracies'],1),
  ('The Charter of Rights and Freedoms protects ___.',['only government officials','only adults','the rights of people in Canada including freedom of expression, equality, and mobility','only citizens by birth'],2)])]),
day(24,[
L('Oral Communication: Presentations','Students learn how to plan and deliver a short oral presentation. Key skills: clear voice, eye contact, staying on topic, and responding to questions.',[
  ('When presenting, you should ___.',['mumble quietly','speak clearly and project your voice so the audience can hear','read directly from a paper without looking up','talk as fast as possible'],1),
  ('Eye contact with the audience shows ___.',['nervousness only','confidence and engagement with your listeners','aggression','lack of preparation'],1),
  ('Good presentations are ___.',['as long as possible','always very short','organised with a clear beginning, middle, and end','only done by teachers'],2),
  ('When someone in the audience asks a question, you should ___.',['ignore it','get upset','listen carefully and give a thoughtful answer','only repeat what you already said'],2),
  ('Practising before a presentation ___.',['makes it worse','wastes time','helps you feel more confident and speak more fluently','only works for adults'],2)]),
M('Multiplication in Context: Word Problems','Students apply multiplication to solve real-world problems.',[
  ('There are 6 bags with 8 apples in each. How many apples in all?',['14','36','48','54'],2),
  ('A box has 5 rows of 7 chocolates. How many chocolates?',['25','30','35','40'],2),
  ('3 classes each have 24 students. How many students in all?',['60','66','72','78'],2),
  ('Each of 8 shelves holds 9 books. How many books total?',['63','72','81','54'],1),
  ('An orchard has 7 rows of 6 trees. How many trees?',['36','42','48','54'],1)]),
Sc('Technology and Science: Inventions','Students explore how scientific understanding leads to inventions that solve human problems. They investigate examples like the telephone, electricity, and vaccines.',[
  ('An invention is ___.',['a discovery of something already existing','a newly created device, process, or idea that solves a problem','only for scientists','only for adults'],1),
  ('Alexander Graham Bell invented the ___.',['light bulb','telephone','printing press','car'],1),
  ('A vaccine helps the body ___.',['become ill on purpose permanently','recognise and fight a specific disease without full infection','only treat illnesses after they occur','cure all diseases at once'],1),
  ('The scientific method involves ___.',['only guessing','observing, questioning, hypothesising, experimenting, and drawing conclusions','only reading books','only performing experiments'],1),
  ('Why is STEM (Science, Technology, Engineering, Math) important?',['It is not','STEM skills drive innovation, problem-solving, and advancements that improve people\'s lives','Only for boys','Only for university'],1)]),
SS('Communities in the Past vs Today','Students compare life in an Ontario community 100 years ago with life today, focusing on changes in transportation, communication, and daily life.',[
  ('One hundred years ago, most Ontarians communicated over long distances by ___.',['text message','email','telegraph and letter (and the early telephone)','video call'],2),
  ('Transportation in Ontario has changed from ___.',['cars to horses','horses and steam trains to cars, planes, and high-speed rail','exactly the same','random changes'],1),
  ('Which technology did NOT exist 100 years ago?',['A telephone','A telegraph','The internet and smartphones','A train'],2),
  ('Schools 100 years ago in rural Ontario ___.',['had computers and internet','often had one room with students of all ages taught by one teacher','were exactly the same as today','only taught reading'],1),
  ('What has stayed the same between Ontario communities 100 years ago and today?',['Technology','The basic need for shelter, food, community, and connection to others','Government structure','Exact same buildings'],1)])]),
day(25,[
L('Spelling: Prefixes and Suffixes','Students learn how prefixes (un-, re-, pre-) and suffixes (-ful, -less, -ness) change a word\'s meaning. They build vocabulary by applying these patterns.',[
  ('A prefix is added to the ___ of a base word.',['end','middle','beginning','random position'],2),
  ('What does the prefix "un-" mean?',['Again','Before','Not or the opposite','After'],2),
  ('What does "unhappy" mean?',['Very happy','Happy again','Not happy','About to be happy'],2),
  ('A suffix is added to the ___ of a word.',['beginning','middle','end','random position'],2),
  ('What does "careful" mean?',['Without care','Full of care','Before care','Not care'],1)]),
M('Data: Pictographs and Surveys','Students conduct simple surveys, organise data in a pictograph, and draw conclusions.',[
  ('A pictograph uses ___ to represent data.',['only numbers','pictures or symbols to represent quantities','only bars','only lines'],1),
  ('In a pictograph where each symbol = 2, four symbols represent ___.',['4','6','8','10'],2),
  ('A survey collects ___.',['only written information','information by asking people questions','only numerical data','only test scores'],1),
  ('Why do we represent data visually?',['It is not useful','Graphs and charts make it easier to compare, analyse, and communicate data','Only for younger students','Only for numbers'],1),
  ('If 15 students prefer soccer and 9 prefer basketball, how many more prefer soccer?',['5','6','7','8'],1)]),
Sc('Properties of Light','Students explore reflection, refraction, and absorption of light, and how prisms separate white light into the visible spectrum.',[
  ('A prism separates white light into ___.',['only two colours','radio waves','the colours of the visible spectrum (ROYGBIV)','sound waves'],2),
  ('The colours of the visible spectrum in order are ___.',['Random','Red, Orange, Yellow, Green, Blue, Indigo, Violet','Blue, Green, Yellow, Orange, Red, Purple','Only three colours'],1),
  ('An opaque object ___.',['lets all light through','lets some light through','does not let light through at all','produces its own light'],2),
  ('A transparent object ___.',['blocks all light','lets most light pass through clearly','only lets some light through','produces light'],1),
  ('A translucent object ___.',['blocks all light','lets all light through clearly','allows some light through but scatters it','produces light'],2)]),
SS('Making a Difference: Local Action','Students explore how individuals and groups make positive changes in their communities through volunteering, activism, and sustainable choices.',[
  ('Volunteering means ___.',['being paid to work','freely giving your time to help others or the community','only cleaning up','only for adults'],1),
  ('A community garden is an example of ___.',['a negative action','people working together to grow food and strengthen community bonds','only for farmers','a government project always'],1),
  ('Young people can make a difference by ___.',['doing nothing','doing nothing until they are adults','raising awareness, organising fundraisers, or starting community projects','only voting'],1),
  ('An example of environmental local action is ___.',['buying more products','participating in a neighbourhood clean-up or tree-planting event','watching documentaries','ignoring litter'],1),
  ('Why does individual action matter?',['It does not','Each person\'s choices add up: individual actions collectively create significant change','Only large organisations matter','Only governments can make change'],1)])]),
day(26,[
L('Book Report Writing','Students write a structured book report including: title and author, brief plot summary, favourite part, and a recommendation.',[
  ('A book report begins with ___.',['your opinion only','the title, author, and genre of the book','only a summary','only a recommendation'],1),
  ('A plot summary in a book report ___.',['spoils everything in detail','tells the main events without giving away the ending','only describes characters','is never included'],1),
  ('In a book report, a recommendation is ___.',['a list of other books','a statement saying whether or not you think others should read the book and why','only a grade','only a summary'],1),
  ('Why are book reports useful?',['They are not','They develop summarising, evaluation, and communication skills','Only for teachers','Only for long books'],1),
  ('Which is NOT typically in a book report?',['Title and author','Personal opinion and recommendation','The author\'s full biography and childhood','A brief summary of the plot'],2)]),
M('Addition and Subtraction Review: 3-Digit Numbers','Students solve multi-step word problems using addition and subtraction of 3-digit numbers.',[
  ('345 + 278 = ?',['613','623','633','623'],1),
  ('800 − 356 = ?',['444','454','344','454'],0),
  ('A school has 425 students. 178 are in junior grades. How many in senior grades?',['247','247','257','237'],0),
  ('642 + 189 = ?',['821','831','841','811'],1),
  ('503 − 167 = ?',['336','346','326','356'],0)]),
Sc('Forces Review and Engineering Design','Students review forces and apply engineering design principles: identify a problem, brainstorm, design, build, test, and improve.',[
  ('The engineering design process begins with ___.',['building immediately','identifying and defining the problem','testing the solution','evaluating results only'],1),
  ('After brainstorming solutions you ___.',['stop the process','select the best design and build a prototype','start over','test without designing'],1),
  ('Testing a prototype helps you ___.',['skip to the end','identify what works and what needs to be improved','guarantee the design is perfect','only look at it'],1),
  ('A prototype is ___.',['the final, perfect product','an early model used to test a design concept','only a drawing','a computer simulation only'],1),
  ('Why is the "improve" step important in engineering design?',['It is not','Real-world designs rarely work perfectly the first time; testing and improving leads to better solutions','Only for professional engineers','Only for complex machines'],1)]),
SS('Ontario\'s Geography: Lakes and Rivers','Students identify Ontario\'s major lakes (Great Lakes) and rivers (Ottawa, St. Lawrence, Thames) and their importance.',[
  ('Which are the five Great Lakes?',['Superior, Huron, Michigan, Erie, Ontario','Superior, Huron, Ontario, Georgian, Erie','Superior, Michigan, Erie, Ontario, Simcoe','Superior, Huron, Erie, Ontario, Nipigon'],0),
  ('The St. Lawrence River connects the Great Lakes to ___.',['the Arctic Ocean','Hudson Bay','the Atlantic Ocean','the Pacific Ocean'],2),
  ('The Ottawa River forms part of the border between ___.',['Ontario and Manitoba','Ontario and Quebec','Quebec and New Brunswick','British Columbia and Alberta'],1),
  ('Why are the Great Lakes important to Ontario?',['They are not','They provide fresh water, shipping routes, fishing, hydroelectric power, and recreation','Only for tourism','Only for the US side'],1),
  ('The St. Lawrence Seaway allows ___.',['only small boats','ocean-going ships to travel from the Atlantic Ocean deep into the Great Lakes via the St. Lawrence River','only Canadian ships','only fishing boats'],1)])]),
day(27,[
L('Writing: Letters (Formal and Informal)','Students learn to write friendly (informal) letters and formal letters. They practise letter format: greeting, body, and closing.',[
  ('A friendly letter is written to ___.',['a company or official','someone you know personally','only government officials','only strangers'],1),
  ('A formal letter is written to ___.',['a best friend','a family member','a company, official, or someone you don\'t know personally','only neighbours'],2),
  ('All letters include ___.',['only a body','a greeting (salutation), a body, and a closing','only a closing','only a return address'],1),
  ('In a friendly letter, the greeting might be ___.',['To Whom It May Concern,','Dear Sir or Madam,','Hey! or Dear [Name],','Only numbers'],2),
  ('In a formal letter, the closing should be ___.',['Love,','See ya!','Sincerely, or Yours truly,','Only your name'],2)]),
M('Multiplication and Division: Word Problems','Students solve two-step word problems using multiplication and division.',[
  ('There are 4 boxes with 12 crayons each. How many crayons in all?',['40','44','48','52'],2),
  ('A bag has 24 apples divided equally into 6 boxes. How many apples per box?',['3','4','5','6'],1),
  ('Each of 7 shelves has 9 books. How many books are there?',['54','56','63','72'],2),
  ('56 children are split into equal teams of 7. How many teams?',['6','7','8','9'],2),
  ('You buy 5 notebooks at $3 each and spend $15 in total. If you paid $20, how much change do you get?',['$3','$5','$6','$7'],1)]),
Sc('Properties of Soil Review and Composting','Students revisit soil types and learn about composting as a way to enrich soil and reduce organic waste.',[
  ('Composting is ___.',['burning organic waste','the decomposition of organic waste (food scraps, leaves) into nutrient-rich material for soil','only for farms','mixing soil with plastic'],1),
  ('What goes in a compost bin?',['Metal and plastic','Fruit and vegetable scraps, leaves, and paper','Only grass clippings','Old electronics'],1),
  ('Compost improves soil by ___.',['making it wetter always','adding nutrients and improving drainage and structure','making it acidic only','only changing colour'],1),
  ('Earthworms help composting by ___.',['eating the metal','breaking down organic matter and aerating the soil as they move through it','creating chemical reactions','only moving soil'],1),
  ('Why is composting good for the environment?',['It is not','It reduces organic waste in landfills and creates valuable fertiliser for gardens','Only for farmers','Only if you have a garden'],1)]),
SS('Canadian Charter of Rights and Freedoms','Students learn about the Charter (1982) and key rights it protects: fundamental freedoms, democratic rights, equality rights.',[
  ('The Canadian Charter of Rights and Freedoms was signed in ___.',['1867','1945','1965','1982'],3),
  ('Which freedom is protected by the Charter?',['Freedom to break laws','Freedom of expression (speech, writing, art)','Freedom from all taxes','Freedom to ignore others\' rights'],1),
  ('Equality rights in the Charter mean ___.',['only men have equal rights','only citizens have equal rights','all people in Canada are equal under the law regardless of race, sex, age, or disability','only adults'],2),
  ('Democratic rights in the Charter include ___.',['the right to own any property','the right of citizens to vote in elections','the right to free housing','the right to drive'],1),
  ('Why is the Charter important?',['It is not','It is the supreme law that protects individual rights and limits what the government can do to people','Only for lawyers','Only for politicians'],1)])]),
day(28,[
L('Reading Long Texts: Chapter Books','Students develop strategies for reading longer texts: using chapter titles, making predictions, tracking characters and plot, and taking notes.',[
  ('Before reading a chapter, reading the chapter title helps you ___.',['predict what the chapter will be about and activate relevant prior knowledge','skip the chapter','write the ending','only look at pictures'],0),
  ('Tracking character changes throughout a chapter book means ___.',['memorising every word','noting how a character grows, changes, or faces challenges as the story progresses','only listing characters','ignoring the plot'],1),
  ('When you lose track of a chapter book, you should ___.',['start from the beginning every time','reread the last few pages or a chapter summary to reorient yourself','stop reading','skip ahead'],1),
  ('Taking reading notes helps you ___.',['forget the text','remember key events, characters, and ideas for discussion or assignments','write more words','read faster'],1),
  ('Why is reading chapter books important?',['It is not','It develops vocabulary, attention span, comprehension, and a love of literature','Only for gifted readers','Only for older students'],1)]),
M('Review: All Strands','Students review and consolidate key Grade 3 math concepts: number sense, measurement, geometry, patterning, and data.',[
  ('256 + 399 = ?',['645','655','665','675'],1),
  ('7 × 9 = ?',['56','63','72','81'],1),
  ('Find the area of a 6×7 rectangle.',['13 sq units','36 sq units','42 sq units','48 sq units'],2),
  ('Which fraction is equivalent to 1/2?',['2/3','3/6','2/5','1/3'],1),
  ('Which event is certain?',['Rolling a 7 on a 6-sided die','Drawing a red card from a deck with only blue cards','Getting either heads or tails on a coin flip','It raining on a sunny day'],2)]),
Sc('Science Year Review','Students review all Grade 3 science strands: growth and changes in animals, soils, forces, and structures.',[
  ('The four stages of complete metamorphosis are ___.',['egg, larva, pupa, adult','egg, nymph, adult, elder','birth, growth, reproduction, death','seed, sprout, plant, fruit'],0),
  ('Which soil is best for most plant growth?',['Sand','Clay','Loam','Gravel'],1),
  ('A simple machine makes work ___.',['harder','impossible','easier by reducing force or changing direction','more expensive'],2),
  ('Which is NOT a simple machine?',['A lever','An inclined plane','A computer','A pulley'],2),
  ('Friction is a force that ___.',['pulls objects toward Earth','is the same as gravity','resists the motion of objects sliding over surfaces','always helps motion'],2)]),
SS('Social Studies Year Review','Students review Ontario communities, government, economy, natural resources, and citizenship.',[
  ('Which level of government runs local parks and garbage collection?',['Federal','Provincial','Municipal','International'],2),
  ('What are Ontario\'s two major physical regions?',['Desert and rainforest','Canadian Shield and Great Lakes–St. Lawrence Lowlands','Prairies and mountains','Ocean coast and tundra'],1),
  ('What does "sustainable" use of resources mean?',['Use as fast as possible','Only use renewable resources','Use resources in a way that preserves them for future generations','Never use any resources'],2),
  ('Confederation took place in ___.',['1776','1812','1867','1982'],2),
  ('A responsible citizen in Canada ___.',['ignores community needs','follows laws, pays taxes, participates, and contributes to the community','only votes','only obeys rules they like'],1)])]),
day(29,[
L('Creative Writing: Narrative Revision','Students revise a narrative draft by improving word choice, adding sensory details, varying sentence structure, and ensuring the story makes sense.',[
  ('Revising a piece of writing means ___.',['correcting only spelling errors','checking and improving content, organization, word choice, and style','rewriting the whole text from scratch','only fixing punctuation'],1),
  ('Sensory details appeal to the ___.',['only visual sense','five senses (sight, sound, smell, taste, touch)','only hearing','only imagination'],1),
  ('Varying sentence length means ___.',['making all sentences the same length','sometimes writing short, punchy sentences and sometimes longer, more descriptive ones','only writing long sentences','only writing short sentences'],1),
  ('Strong verbs like "sprinted" and "whispered" are better than "ran" and "said" because ___.',['they are longer','they add more precise, vivid meaning and make the writing more engaging','they are always correct','they use more punctuation'],1),
  ('After revising for content, you should ___ your writing.',['stop working','edit/proofread for spelling, grammar, and punctuation errors','rewrite entirely','submit immediately'],1)]),
M('Financial Literacy: Saving and Spending','Students learn the basics of saving, spending, and the concept of earning money through work.',[
  ('Saving money means ___.',['spending everything you earn','setting aside money to use later for a goal or emergency','only putting money in a bank','only for adults'],1),
  ('The difference between a need and a want is ___.',['they are the same','needs are necessary for survival; wants are extras we desire','wants are more important','needs are optional'],1),
  ('If you earn $10 and spend $6, how much can you save?',['$3','$4','$6','$2'],1),
  ('A simple budget helps you ___.',['spend all your money immediately','track income and expenses to ensure you live within your means','only save money','only spend money'],1),
  ('Why is it good to save some of your money?',['It is not','Savings give you a financial cushion for emergencies and future goals','Only for adults','You should spend everything to enjoy life'],1)]),
Sc('Environmental Science: Climate and Ecosystems','Students explore how climate affects ecosystems, and how climate change is altering habitats and biodiversity globally and in Ontario.',[
  ('Climate is ___.',['today\'s weather','the average weather patterns of a region over a long period','only temperature','only rainfall'],1),
  ('Climate change is causing ___.',['no changes','more extreme weather events, rising temperatures, melting ice, and shifting seasons globally','only ocean changes','only desert expansion'],1),
  ('How does climate change affect Ontario wildlife?',['It does not','Warmer temperatures shift the ranges of many species, affecting when birds migrate, when plants bloom, and which species survive','Only for tropical animals','Only for marine animals'],1),
  ('Which gas is a major contributor to climate change?',['Nitrogen','Oxygen','Carbon dioxide (CO₂) from burning fossil fuels','Helium'],2),
  ('One way to reduce carbon emissions is to ___.',['use more fossil fuels','burn more forests','use renewable energy, reduce waste, and drive less','plant more lawns only'],2)]),
SS('Looking Forward: My Community in 2050','Students use their learning to imagine what their community might look like in 2050 given current trends in technology, population, and environment.',[
  ('In 2050, Ontario\'s population will likely ___.',['shrink to zero','grow, requiring more housing, services, and infrastructure','stay exactly the same','move to the Moon'],1),
  ('Technology in 2050 might help communities by ___.',['causing more problems','solving challenges like clean energy, efficient transportation, and better health care','doing nothing new','only creating entertainment'],1),
  ('Environmental challenges in 2050 will likely include ___.',['no challenges','effects of climate change such as more extreme weather, changed habitats, and pressure on water resources','nothing new','only space issues'],1),
  ('What can students today do to help the communities of 2050?',['Nothing','Learn, innovate, make sustainable choices, and be active citizens committed to a better future','Only wait','Only vote when older'],1),
  ('The most important lesson from Grade 3 Social Studies is ___.',['memorising province names','Communities are connected through geography, history, people, and shared responsibilities','Only facts about Ontario','Only about government'],1)])]),
day(30,[
L('Year End Celebration: Favourite Books and Reading Reflections','Students share favourite books, reflect on their reading growth, and set reading goals for Grade 4.',[
  ('Reflecting on your reading means ___.',['forgetting everything','thinking about how your skills and enjoyment of reading have grown throughout the year','copying a book report','only choosing new books'],1),
  ('A reading goal for Grade 4 might be ___.',['never reading again','trying a new genre, reading longer books, or reading a set number of books','only reading the same books','giving up on hard books'],1),
  ('Why is reading important beyond school?',['It is not','Reading develops vocabulary, knowledge, empathy, and lifelong learning skills','Only for school marks','Only for English class'],1),
  ('What is one thing you enjoyed about reading this year?',['Nothing','Discovering a new favourite genre, author, or story that made me think or feel something new','Only tests','Only grammar'],1),
  ('A book recommendation should include ___.',['only the title','the title, author, what you loved about it, and who you think would enjoy it','only your name','only a grade out of ten'],1)]),
M('Grade 3 Math Celebration: Challenge Problems','Students tackle fun, mixed challenge problems drawing on all Grade 3 math concepts.',[
  ('A rectangle has a perimeter of 28 cm and a length of 9 cm. What is its width?',['4 cm','5 cm','6 cm','7 cm'],1),
  ('If 8 students each have 7 stickers and share equally in 4 groups, how many stickers per group?',['12','14','16','18'],1),
  ('A bag has 30 apples. 1/3 are red. How many red apples?',['5','10','12','15'],1),
  ('What is 485 + 367?',['842','852','862','872'],1),
  ('A square field has an area of 81 m². What is each side length?',['7 m','8 m','9 m','10 m'],2)]),
Sc('Grade 3 Science Celebration: Science All Around Us','Students connect science learning to everyday life and explore how curiosity and observation drive scientific discovery.',[
  ('A simple machine that helps you open a paint can lid with a coin is a ___.',['pulley','wheel-and-axle','lever','inclined plane'],2),
  ('Which soil type is best for growing vegetables?',['Clay','Sand','Gravel','Loam'],3),
  ('An eagle is a secondary consumer. What does it most likely eat?',['Only plants','Only soil','Smaller animals like fish, rabbits, and other birds','Only fungi'],2),
  ('Renewable energy sources include ___.',['coal and oil','natural gas and propane','solar, wind, and hydroelectric power','only nuclear power'],2),
  ('The engineering design process helps people ___.',['give up easily','solve real problems by designing, testing, and improving their ideas','only build bridges','only for space programs'],1)]),
SS('Grade 3 Social Studies Celebration: Our Community, Our World','Students celebrate their learning by connecting Ontario communities to communities around the world and to the future.',[
  ('What do all communities around the world have in common?',['Exact same food','Same language','Same government','People working together to meet basic needs and live good lives'],3),
  ('How is Ontario connected to communities around the world?',['It is not','Through trade, immigration, cultural exchange, international agreements, and shared global challenges','Only through geography','Only through the internet'],1),
  ('What makes a community strong?',['Only money','Cooperation, respect, diversity, shared responsibility, and a sense of belonging','Only large buildings','Only famous people'],1),
  ('What is one thing you can do to make your community better?',['Nothing','Be kind, participate, volunteer, make sustainable choices, and treat everyone with respect','Only vote at 18','Only pay taxes'],1),
  ('The most important thing I learned in Grade 3 Social Studies is ___.',['Nothing was important','Communities are built by people working together and respecting each other, the land, and the future','Only province names','Only about the government'],1)])])
]

write_new(3, g3)
print('Grade 3 (30 days) done.')
