import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"Language", title:"Reading Comprehension: Main Idea", summary:"Students identify the main idea and supporting details in short non-fiction texts. The main idea is what the whole passage is mostly about; details explain or support it.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The main idea of a passage is ___.", options:["one small detail","what the whole passage is mostly about","the last sentence","a random fact"], answer:1},
     {q:"Supporting details ___.", options:["introduce new topics unrelated to the main idea","explain or give examples that support the main idea","are always the first sentence","are always in brackets"], answer:1},
     {q:"Where is the main idea often found?", options:["Only in the last paragraph","In the middle of the text","Often in the first or last sentence of a paragraph","Only in illustrations"], answer:2},
     {q:"Which question helps find the main idea?", options:["Who wrote this?","When was this written?","What is this mostly about?","How long is this?"], answer:2},
     {q:"A passage about how bees make honey is mostly about ___.", options:["flowers","trees","the honey-making process of bees","weather patterns"], answer:2}
   ]},
  {subject:"Math", title:"Place Value: Ones, Tens, Hundreds", summary:"Students identify the value of digits in numbers up to 999. In 347, the 3 is in the hundreds place (300), the 4 in the tens place (40), and the 7 in the ones place (7).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In 456, the digit in the tens place is ___.", options:["4","5","6","45"], answer:1},
     {q:"What is the value of the 3 in 382?", options:["3","30","300","3000"], answer:2},
     {q:"Which number has 5 hundreds, 2 tens, and 8 ones?", options:["258","528","582","825"], answer:1},
     {q:"In 709, which digit is in the ones place?", options:["7","0","9","70"], answer:2},
     {q:"What is 600 + 40 + 3?", options:["463","634","643","364"], answer:2}
   ]},
  {subject:"Science", title:"Growth and Changes in Animals", summary:"Students explore how animals change as they grow, including complete and incomplete metamorphosis in insects, and growth in mammals, birds, and reptiles.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Complete metamorphosis has ___ stages.", options:["2","3","4","5"], answer:2},
     {q:"The four stages of complete metamorphosis are ___.", options:["egg, larva, pupa, adult","egg, baby, teen, adult","birth, growth, death, rebirth","seed, sprout, plant, flower"], answer:0},
     {q:"A caterpillar is the ___ stage of a butterfly.", options:["egg","larva","pupa","adult"], answer:1},
     {q:"Incomplete metamorphosis does NOT have a ___ stage.", options:["egg","nymph","adult","pupa"], answer:3},
     {q:"Which animal goes through complete metamorphosis?", options:["Dog","Frog (it goes through stages but it is incomplete)","Butterfly","Snake"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Types of Communities: Urban and Rural", summary:"Students compare urban (city) and rural (countryside/farm) communities in Ontario. They examine population, land use, and services available.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"An urban community is best described as ___.", options:["a small farming village","a large city with many people and buildings","a forest with no residents","a single-family home"], answer:1},
     {q:"A rural community is best described as ___.", options:["a skyscraper district","a densely populated city","a farming area or small town with fewer people","an underground settlement"], answer:2},
     {q:"Which service is more common in urban areas?", options:["Large hospital with specialists","Grain elevator","Crop fields","Ranch"], answer:0},
     {q:"What do rural communities often have that urban ones typically lack?", options:["Subway systems","Large amounts of open farmland and natural space","Skyscrapers","Airports"], answer:1},
     {q:"Which Ontario city is an example of a major urban community?", options:["A small northern village","Toronto","A rural township","An island cottage community"], answer:1}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"Language", title:"Text Features: Headings, Captions, Diagrams", summary:"Students identify and use text features in non-fiction books and articles to navigate text and understand content better.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A heading in a non-fiction text ___.", options:["tells a story","gives the author's name","shows what a section is about","is the same as a caption"], answer:2},
     {q:"A caption is ___.", options:["a type of heading","a large title","the words under a picture explaining what it shows","a table of contents"], answer:2},
     {q:"A diagram with labels helps readers ___.", options:["enjoy the story more","see and understand how something works or is structured","find the author","read faster"], answer:1},
     {q:"Why do non-fiction books use text features?", options:["To make the book longer","To help readers find and understand information more easily","Only for decoration","Only for young readers"], answer:1},
     {q:"A table of contents tells you ___.", options:["the definition of words","where chapters and sections start","who wrote the book","what pictures look like"], answer:1}
   ]},
  {subject:"Math", title:"Addition with Regrouping", summary:"Students add 2- and 3-digit numbers with regrouping (carrying). They understand that when a column totals 10 or more, they carry 1 to the next column.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"47 + 35 = ?", options:["72","82","73","83"], answer:1},
     {q:"When a column in addition totals 10 or more, you ___.", options:["write the full number","subtract 10 and carry 1 to the next column","start over","ignore the extra"], answer:1},
     {q:"256 + 138 = ?", options:["394","384","494","494"], answer:0},
     {q:"What does "regrouping" mean in addition?", options:["Starting over","Carrying a group of 10 to the next place value column","Subtracting","Multiplying"], answer:1},
     {q:"149 + 67 = ?", options:["206","216","226","196"], answer:1}
   ]},
  {subject:"Science", title:"Habitats and Ecosystems", summary:"Students learn that a habitat provides the living and non-living things an animal needs to survive: food, water, shelter, and space. Ecosystems include all living and non-living parts of an environment.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A habitat is ___.", options:["a type of weather","the environment where an organism lives and finds what it needs to survive","only a forest","only an ocean"], answer:1},
     {q:"Which is a non-living part of an ecosystem?", options:["Tree","Rabbit","Rock and water","Mushroom"], answer:2},
     {q:"An ecosystem includes ___.", options:["only animals","only plants","all living and non-living things in an area and their interactions","only soil"], answer:2},
     {q:"Why do different animals live in different habitats?", options:["They do not; all animals live in the same habitat","Because different habitats provide different food, shelter, and conditions each animal needs","Only for territory","Only for warmth"], answer:1},
     {q:"Destroying a habitat by cutting down a forest would most likely ___.", options:["help the animals there","have no effect","force animals to find new habitats, often leading to population decline","make habitats larger"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Physical Features of Ontario", summary:"Students identify and locate major physical features of Ontario on a map: Great Lakes, Canadian Shield, Niagara Falls, Lake Simcoe, and major rivers.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The Great Lakes are ___.", options:["mountain ranges","rivers in northern Ontario","a chain of five large freshwater lakes on Ontario's southern border","a type of Canadian animal"], answer:2},
     {q:"The Canadian Shield is ___.", options:["a hockey shield","a flat farming region","a vast ancient rock formation covering much of northern Ontario and Canada","an ocean region"], answer:2},
     {q:"Niagara Falls is located between ___.", options:["Lake Superior and Lake Huron","Lake Erie and Lake Ontario","Lake Ontario and Lake Huron","Lake Huron and Lake Michigan"], answer:1},
     {q:"Which is Ontario's capital city?", options:["Ottawa","Montreal","Toronto","Hamilton"], answer:2},
     {q:"Which direction is northern Ontario relative to southern Ontario?", options:["South","East","West","North"], answer:3}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"Language", title:"Vocabulary: Context Clues", summary:"Students use context clues — the surrounding words and sentences — to figure out the meaning of unfamiliar words without a dictionary.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Context clues are ___.", options:["clues found in a picture only","words and information surrounding an unfamiliar word that help explain its meaning","a type of dictionary","always found in the title"], answer:1},
     {q:"In "The enormous elephant, nearly as tall as a house, walked slowly," enormous means ___.", options:["tiny","fast","very large","colourful"], answer:2},
     {q:"In "She was famished and couldn't wait to eat dinner," famished means ___.", options:["excited","very hungry","tired","late"], answer:1},
     {q:"Why are context clues useful?", options:["They are not useful","They let readers figure out word meanings from the text without stopping to use a dictionary","Only for hard books","Only for adults"], answer:1},
     {q:"Which strategy uses context clues?", options:["Skipping the word","Looking at how the word is used in the sentence and paragraph to guess its meaning","Only using a dictionary","Sounding out letters"], answer:1}
   ]},
  {subject:"Math", title:"Subtraction with Regrouping", summary:"Students subtract 2- and 3-digit numbers using regrouping (borrowing). They understand borrowing from the next column when the top digit is smaller.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"84 - 37 = ?", options:["47","57","53","43"], answer:0},
     {q:"When the top digit in a column is smaller than the bottom, you ___.", options:["skip the subtraction","regroup (borrow) from the next column to the left","add them","multiply"], answer:1},
     {q:"352 - 176 = ?", options:["276","176","186","176"], answer:1},
     {q:"Which is the first step in 503 - 248?", options:["Subtract hundreds first","Subtract 8 from 3, regrouping from the tens (then hundreds) column","Add the numbers","Multiply"], answer:1},
     {q:"427 - 189 = ?", options:["238","248","228","268"], answer:0}
   ]},
  {subject:"Science", title:"Soils in the Environment", summary:"Students investigate types of soil (sand, clay, loam) and their properties. They explore how soil supports plant growth and is important to ecosystems.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which type of soil drains water the fastest?", options:["Clay","Loam","Sand","Silt"], answer:2},
     {q:"Clay soil is described as ___.", options:["gritty and fast-draining","very fertile and balanced","dense, heavy, and slow-draining","dark and crumbly"], answer:2},
     {q:"Loam is considered ideal for growing plants because ___.", options:["it has no nutrients","it drains instantly","it has a balanced mix of sand, silt, and clay with good nutrients and drainage","it is always wet"], answer:2},
     {q:"Soil is important because ___.", options:["it only comes in one type","it supports plant growth and is home to many organisms like earthworms and bacteria","only farmers need it","it has no nutrients"], answer:1},
     {q:"What lives in soil and helps break down organic matter?", options:["Only rocks","Earthworms, bacteria, and fungi","Only large animals","Only plants"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Government: Federal, Provincial, Municipal", summary:"Students learn the three levels of government in Canada and their responsibilities.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The federal government of Canada is responsible for ___.", options:["collecting garbage","fixing local roads","national defence, immigration, and the currency","setting school hours"], answer:2},
     {q:"The provincial government of Ontario is responsible for ___.", options:["the national army","international affairs","education, health care, and provincial roads","the city's parks"], answer:2},
     {q:"The municipal (city/town) government is responsible for ___.", options:["immigration law","national defence","local roads, parks, garbage collection, and local bylaws","provincial health care"], answer:2},
     {q:"Who is the leader of the federal government of Canada?", options:["The Premier","The Mayor","The Prime Minister","The Governor General"], answer:2},
     {q:"A school in Ontario falls under ___ government responsibility.", options:["federal","provincial","municipal","international"], answer:1}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"Language", title:"Fiction vs Non-Fiction", summary:"Students distinguish fiction (invented stories with characters, plot, and setting) from non-fiction (factual, real-world information).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A fiction text ___.", options:["only contains facts","is based on real events","contains invented stories and characters","is always about animals"], answer:2},
     {q:"A non-fiction text ___.", options:["contains made-up stories","is always a novel","provides factual information about real topics","is always written by scientists"], answer:2},
     {q:"Which is an example of fiction?", options:["A science textbook","A newspaper article","A story about a talking dragon who saves a kingdom","A biography of a real person"], answer:2},
     {q:"Which is an example of non-fiction?", options:["A story about a magical school","A fairy tale","A book about how volcanoes form","A book about an imaginary city"], answer:2},
     {q:"How can you tell if a book is fiction or non-fiction?", options:["By the number of pages","Fiction has invented events and characters; non-fiction has real facts and information","Only by the cover colour","Only by the title"], answer:1}
   ]},
  {subject:"Math", title:"Multiplication: Concept and Arrays", summary:"Students learn multiplication as repeated addition and model it with arrays. 3 × 4 means 3 groups of 4 (or 4 + 4 + 4 = 12).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"3 × 4 = ?", options:["7","10","12","14"], answer:2},
     {q:"Multiplication is the same as ___.", options:["taking away","repeated addition","dividing","guessing"], answer:1},
     {q:"An array of 2 rows and 5 columns has how many items?", options:["7","8","9","10"], answer:3},
     {q:"5 × 3 can be shown as ___.", options:["5 groups of 5","3 groups of 5","5 groups of 3 (or 3 groups of 5 — both equal 15)","only 5 + 3"], answer:2},
     {q:"Which number sentence shows 3 groups of 6?", options:["3 + 6 = 9","3 − 6","3 × 6 = 18","6 − 3 = 3"], answer:2}
   ]},
  {subject:"Science", title:"Forces Causing Movement", summary:"Students learn that forces (push, pull, gravity, friction, magnetism) can cause objects to start, stop, speed up, or change direction.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A force is ___.", options:["a type of animal","a push or pull that can change an object's motion","only wind","only gravity"], answer:1},
     {q:"Gravity is a force that ___.", options:["pushes things sideways","pulls objects toward Earth (or any large mass)","only affects large objects","only works in space"], answer:1},
     {q:"Friction is a force that ___.", options:["speeds objects up always","acts between moving surfaces to slow motion","only affects liquids","only exists in water"], answer:1},
     {q:"Which force keeps planets orbiting the Sun?", options:["Friction","Air resistance","Magnetism","Gravity"], answer:3},
     {q:"A magnet can ___ a metal object without touching it.", options:["break","paint","attract or repel","melt"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Natural Resources", summary:"Students identify Ontario's natural resources (water, forests, minerals, farmland) and how they are used sustainably.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A natural resource is ___.", options:["something made in a factory","something found in nature that humans use","only a type of animal","only oil and gas"], answer:1},
     {q:"Which is an example of a natural resource?", options:["Plastic","Steel beam","Fresh water","Nylon"], answer:2},
     {q:"Forestry in Ontario provides ___.", options:["steel and iron","timber for lumber and paper products","crude oil","electronics"], answer:1},
     {q:"Sustainable use of resources means ___.", options:["using as much as possible as fast as possible","using resources in ways that don't permanently deplete them for future generations","never using any resources","only using human-made resources"], answer:1},
     {q:"Ontario's Great Lakes are an important natural resource because ___.", options:["they are in the mountains","they provide drinking water, fishing, transportation, and hydroelectric power","only for recreation","they are very small"], answer:1}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"Language", title:"Writing: Paragraphs", summary:"Students learn to write a paragraph with a topic sentence, at least three supporting detail sentences, and a concluding sentence.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The topic sentence of a paragraph ___.", options:["ends the paragraph","introduces the main idea of the paragraph","is always the longest sentence","only gives one detail"], answer:1},
     {q:"Supporting sentences in a paragraph ___.", options:["change the topic","give details, examples, or reasons that support the topic sentence","are always questions","are written randomly"], answer:1},
     {q:"A concluding sentence ___.", options:["introduces a new idea","copies the topic sentence word for word","wraps up the paragraph's ideas","is optional"], answer:2},
     {q:"A paragraph about dogs should NOT include ___.", options:["details about dogs' loyalty","facts about dog breeds","information about dog training","unrelated facts about cars"], answer:3},
     {q:"A good paragraph has ___.", options:["only one sentence","a topic sentence, supporting details, and a conclusion","only questions","no main idea"], answer:1}
   ]},
  {subject:"Math", title:"Multiplication: Facts to 5", summary:"Students learn and practise multiplication facts with factors up to 5.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"2 × 5 = ?", options:["7","8","9","10"], answer:3},
     {q:"4 × 3 = ?", options:["9","10","11","12"], answer:3},
     {q:"5 × 5 = ?", options:["20","22","25","30"], answer:2},
     {q:"3 × 3 = ?", options:["6","7","8","9"], answer:3},
     {q:"What multiplication fact is shown by: ●●●●, ●●●●, ●●●●?", options:["3 + 4","3 × 4 = 12","4 + 3","4 × 4"], answer:1}
   ]},
  {subject:"Science", title:"Simple Machines: Lever and Inclined Plane", summary:"Students explore levers (a bar that pivots on a fulcrum) and inclined planes (a ramp) as simple machines that make work easier.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A lever is a ___.", options:["type of wheel","bar or plank that pivots on a fulcrum to lift or move things","type of screw","type of pulley"], answer:1},
     {q:"The fulcrum is ___.", options:["the load","the effort force","the pivot point of a lever","the ramp"], answer:2},
     {q:"An inclined plane is ___.", options:["a flat surface","a slanted surface (ramp) that reduces the force needed to move an object upward","a wheel on an axle","a wedge only"], answer:1},
     {q:"A ramp makes it easier to ___.", options:["multiply numbers","push objects to a higher level without lifting the full weight straight up","run faster","make noise"], answer:1},
     {q:"A seesaw is an example of a ___.", options:["wedge","screw","pulley","lever"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Using Maps: Scale and Direction", summary:"Students read and use simple maps, understanding cardinal directions, a compass rose, map legend/key, and basic scale.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Cardinal directions are ___.", options:["up, down, left, right","north, south, east, west","large, small, medium, tiny","spring, summer, fall, winter"], answer:1},
     {q:"A map legend (key) tells you ___.", options:["the map's author","what the symbols and colours on the map mean","how large the country is","who made the map"], answer:1},
     {q:"A compass rose on a map shows ___.", options:["the scale","distances","direction (north, south, east, west and intermediate directions)","symbols"], answer:2},
     {q:"Map scale tells you ___.", options:["the population of cities","what symbols mean","the relationship between distances on the map and real-world distances","who drew the map"], answer:2},
     {q:"On most maps, north is located ___.", options:["at the bottom","on the right","at the top","on the left"], answer:2}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"Language", title:"Punctuation: Commas and Apostrophes", summary:"Students use commas in lists (I have a cat, a dog, and a bird) and apostrophes for contractions (don't, can't) and possessives (Tom's book).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In a list of three items, where do commas go?", options:["Only after the last item","Between each item (and before "and" in the series)","Only at the start","Nowhere"], answer:1},
     {q:"Which sentence uses commas correctly in a list?", options:["I bought apples oranges and bananas.","I bought apples, oranges, and bananas.","I bought, apples, oranges and bananas.","I bought apples, oranges and, bananas."], answer:1},
     {q:"An apostrophe in "don't" shows ___.", options:["possession","a missing letter (contraction of "do not")","a question","a list"], answer:1},
     {q:"An apostrophe in "Maria's backpack" shows ___.", options:["a contraction","a question","that the backpack belongs to Maria (possession)","a list"], answer:2},
     {q:"Which word is a contraction?", options:["Cannot","Can't","Cant","Cannt"], answer:1}
   ]},
  {subject:"Math", title:"Division: Sharing and Grouping", summary:"Students explore division as fair sharing and as grouping. 12 ÷ 3 means sharing 12 into 3 equal groups (4 each) or making groups of 3 from 12 (4 groups).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"12 ÷ 4 = ?", options:["3","4","5","6"], answer:0},
     {q:"Division can be thought of as ___.", options:["repeated multiplication","fair sharing into equal groups","random sorting","only subtraction"], answer:1},
     {q:"15 ÷ 3 = ?", options:["4","5","6","7"], answer:1},
     {q:"If 20 students are divided into groups of 5, how many groups are there?", options:["3","4","5","6"], answer:1},
     {q:"8 ÷ 8 = ?", options:["0","1","8","64"], answer:1}
   ]},
  {subject:"Science", title:"Simple Machines: Wheel-and-Axle and Pulley", summary:"Students explore how wheels with axles and pulleys reduce friction and redirect force to make work easier.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A wheel-and-axle consists of ___.", options:["two levers","a large wheel attached to a smaller rod (axle)","a rope and a groove","a ramp and a slope"], answer:1},
     {q:"The wheel reduces ___.", options:["speed always","friction, making it easier to move heavy loads","weight","gravity"], answer:1},
     {q:"A pulley is used to ___.", options:["pry things apart","join pieces of wood","lift or lower loads using a rope and a grooved wheel","push objects up a ramp"], answer:2},
     {q:"Which everyday object uses a wheel-and-axle?", options:["Scissors","A nail","A bicycle wheel and its axle","A ramp at a loading dock"], answer:2},
     {q:"A fixed pulley changes the ___ of a force.", options:["size","colour","direction","weight"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Indigenous Communities in Ontario", summary:"Students learn about the diversity of Indigenous communities in Ontario (First Nations, Métis, Inuit) and their relationship to the land.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which groups are Indigenous peoples of Canada?", options:["French and English","First Nations, Métis, and Inuit","Only European settlers","Immigrants from other countries"], answer:1},
     {q:"Indigenous peoples' relationship to the land includes ___.", options:["only farming the land for profit","deep spiritual, cultural, and practical connections to the land, water, and animals","ignoring the land","only using the land for buildings"], answer:1},
     {q:"A key principle of many Indigenous cultures is ___.", options:["owning as much land as possible","respecting and living in balance with the natural world","never sharing resources","separating from nature"], answer:1},
     {q:"The Haudenosaunee (Iroquois) are an example of ___.", options:["a French settlement","a European explorer group","First Nations peoples of what is now Ontario and New York State","a recent immigrant community"], answer:2},
     {q:"Why is it important to learn about Indigenous cultures?", options:["It is not","To understand and respect the original peoples of the land and their continuing contributions","Only for history class","Only for Indigenous students"], answer:1}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"Language", title:"Reading: Cause and Effect", summary:"Students identify cause and effect relationships in texts. A cause is why something happened; an effect is what happened as a result.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A cause is ___.", options:["what happened","where something happened","why something happened","who did something"], answer:2},
     {q:"An effect is ___.", options:["why something happened","the result of something that happened","when something happened","who caused it"], answer:1},
     {q:"Signal words for cause include ___.", options:["so, therefore, as a result","because, since, due to","but, however, although","first, then, finally"], answer:1},
     {q:"Signal words for effect include ___.", options:["because, since, due to","but, although, however","so, therefore, as a result","if, when, while"], answer:2},
     {q:"It rained heavily. Because of this, the game was cancelled. What is the effect?", options:["It rained heavily","The clouds formed","The game was cancelled","The players got wet"], answer:2}
   ]},
  {subject:"Math", title:"Fractions: Halves, Thirds, Quarters", summary:"Students identify, read, and write fractions as equal parts of a whole (1/2, 1/3, 1/4). They understand that the denominator shows total equal parts.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In the fraction 3/4, the denominator is ___.", options:["3","4","3/4","7"], answer:1},
     {q:"1/2 means ___.", options:["1 part out of 3 equal parts","1 part out of 2 equal parts","2 parts out of 1 equal part","1 part out of 4 equal parts"], answer:1},
     {q:"If a pizza is cut into 4 equal slices and you eat 1, you ate ___.", options:["1/2","1/3","1/4","1/8"], answer:2},
     {q:"Which fraction is the largest?", options:["1/4","1/3","1/2","1/8"], answer:2},
     {q:"What does the numerator tell you?", options:["The total equal parts","How many equal parts we have","The size of the whole","The shape of the fraction"], answer:1}
   ]},
  {subject:"Science", title:"Air and Water in the Environment", summary:"Students explore the properties of air (invisible but real, exerts pressure) and water in its three states. They learn about the water cycle.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Air is ___.", options:["visible like smoke","invisible but takes up space and exerts pressure","only oxygen","only found in balloons"], answer:1},
     {q:"The water cycle includes ___.", options:["only rain","evaporation, condensation, and precipitation, cycling water through air, land, and sea","only the ocean","only rivers and lakes"], answer:1},
     {q:"Evaporation is when water ___.", options:["falls as rain","freezes into ice","changes from liquid to water vapour (gas) when heated","becomes solid"], answer:2},
     {q:"Precipitation includes ___.", options:["only rain","rain, snow, sleet, and hail — any water that falls from clouds","only snow","only fog"], answer:1},
     {q:"Why is the water cycle important?", options:["It is not","It continuously distributes fresh water to ecosystems around the world","Only for rain forests","Only for oceans"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Early Settlers in Ontario", summary:"Students learn how early European settlers came to Ontario, the challenges they faced, and how they built communities on the land.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Early European settlers came to Ontario mainly from ___.", options:["Asia and Africa","Britain and France (and other European countries)","South America","Australia"], answer:1},
     {q:"What was one major challenge early settlers in Ontario faced?", options:["Too many schools","Clearing dense forest to build farms and homes in a harsh climate","Too many roads","Too much food"], answer:1},
     {q:"Loyalists were ___.", options:["Indigenous peoples","People who remained loyal to the British Crown and came to Ontario after the American Revolution","French farmers","Early traders from Asia"], answer:1},
     {q:"Early settlers and Indigenous peoples sometimes ___.", options:["never interacted","traded goods and Indigenous peoples shared knowledge of the land","always fought","only competed"], answer:1},
     {q:"What is one legacy of early settlers in Ontario?", options:["None","The network of towns, farms, and roads that form the basis of modern Ontario communities","Only conflict","Only poverty"], answer:1}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"Language", title:"Writing: Narrative — Beginning, Middle, End", summary:"Students write short narratives (personal or fictional) with a clear beginning that introduces characters and setting, a middle with the main event/problem, and an end that resolves it.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The beginning of a narrative should ___.", options:["solve the problem","introduce the characters, setting, and situation","summarize everything","be the longest part"], answer:1},
     {q:"The middle of a narrative contains ___.", options:["the resolution","the credits","the main events and problem the character faces","the title"], answer:2},
     {q:"The end of a narrative should ___.", options:["introduce new characters","resolve the problem or bring the story to a satisfying close","start a new problem","be a cliffhanger always"], answer:1},
     {q:"A narrative is a ___.", options:["set of facts","story or personal account of events","list of instructions","type of graph"], answer:1},
     {q:"Which word signals the beginning of a sequence?", options:["Finally","Then","First","However"], answer:2}
   ]},
  {subject:"Math", title:"Measurement: Perimeter", summary:"Students find the perimeter of 2D shapes by adding all side lengths. They understand that perimeter is the total distance around a shape.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Perimeter is ___.", options:["the area inside a shape","the total distance around the outside of a shape","the weight of a shape","the height of a shape"], answer:1},
     {q:"A square has sides of 4 cm each. Its perimeter is ___.", options:["4 cm","8 cm","12 cm","16 cm"], answer:3},
     {q:"A rectangle has length 6 m and width 3 m. Its perimeter is ___.", options:["9 m","12 m","18 m","24 m"], answer:2},
     {q:"To find the perimeter you ___.", options:["multiply length × width","add all the side lengths together","divide length by 2","subtract one side from another"], answer:1},
     {q:"A triangle has sides 5 cm, 7 cm, and 8 cm. Perimeter = ?", options:["12 cm","15 cm","20 cm","22 cm"], answer:2}
   ]},
  {subject:"Science", title:"Rocks and Minerals", summary:"Students identify properties of rocks and minerals (colour, lustre, hardness, streak, shape) and understand that rocks are made of one or more minerals.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A mineral is ___.", options:["any rock","a naturally occurring, non-living solid with a specific chemical composition","only found underground","only found in water"], answer:1},
     {q:"A rock is ___.", options:["a single mineral only","a pure element","made up of one or more minerals bonded together","made of living material"], answer:2},
     {q:"Hardness of a mineral measures ___.", options:["how shiny it is","how heavy it is","how resistant it is to being scratched","its colour"], answer:2},
     {q:"The Mohs scale measures ___.", options:["weight","temperature","mineral hardness","mineral colour"], answer:2},
     {q:"Igneous rocks form from ___.", options:["pressed layers of sediment","living organisms","cooled magma or lava","wind erosion"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Early Trading and Economy in Ontario", summary:"Students explore how early Indigenous and settler communities traded goods and how the fur trade shaped Ontario's early economy.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The fur trade was important in early Ontario because ___.", options:["it provided animal companions","furs were highly valued in Europe for clothing and hats, driving exploration and trade","it only helped Indigenous peoples","it had no lasting effects"], answer:1},
     {q:"Early Indigenous peoples traded ___.", options:["electronics","furs, food, and knowledge of the land","manufactured goods","cars"], answer:1},
     {q:"A trading post was ___.", options:["a type of mail delivery","a location where Indigenous peoples and European traders exchanged goods","a school building","a government office"], answer:1},
     {q:"The Hudson's Bay Company was ___.", options:["a fishing company","a major European fur-trading company that operated across Canada","an Indigenous organization","a government agency"], answer:1},
     {q:"How did the fur trade affect Indigenous communities?", options:["It had no effect","It brought wealth and trade goods but also conflict, disease, and disruption to traditional ways of life","It only helped them","It only damaged them"], answer:1}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"Language", title:"Grammar: Nouns, Verbs, Adjectives", summary:"Students identify nouns (person, place, thing, animal), verbs (action or state words), and adjectives (describing words) in sentences.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A noun names a ___.", options:["feeling or action","person, place, thing, or animal","movement or sound","only a building"], answer:1},
     {q:"A verb is a word that describes ___.", options:["a person or place","a colour or size","an action or state of being","only running"], answer:2},
     {q:"An adjective ___.", options:["names a person","shows an action","describes a noun","tells when"], answer:2},
     {q:"In "The tall girl ran quickly", the adjective is ___.", options:["girl","ran","quickly","tall"], answer:3},
     {q:"In "The dog barked loudly", the verb is ___.", options:["The","dog","barked","loudly"], answer:2}
   ]},
  {subject:"Math", title:"Multiplication: Facts 6 to 10", summary:"Students practise multiplication facts with factors from 6 to 10.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"6 × 7 = ?", options:["40","42","44","46"], answer:1},
     {q:"8 × 9 = ?", options:["62","70","72","76"], answer:2},
     {q:"7 × 7 = ?", options:["42","46","49","51"], answer:2},
     {q:"10 × 6 = ?", options:["56","60","66","70"], answer:1},
     {q:"9 × 4 = ?", options:["32","34","36","40"], answer:2}
   ]},
  {subject:"Science", title:"Structures: Types and Properties", summary:"Students explore natural and human-made structures. They investigate properties like stability, strength, and function.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A structure is ___.", options:["a type of weather event","something built or constructed to serve a purpose","only a building","only a bridge"], answer:1},
     {q:"Which is a natural structure?", options:["A bridge","A skyscraper","A bird's nest","A dam built by engineers"], answer:2},
     {q:"A triangular shape is used in structures because ___.", options:["it looks nice","triangles are very stable and resist forces without changing shape","it is easy to build","it uses less material"], answer:1},
     {q:"The base of a structure should be ___.", options:["narrow and unstable","wide and stable for better balance","flexible always","high off the ground"], answer:1},
     {q:"Which material is usually strongest for building?", options:["Paper","Foam","Balsa wood","Concrete or steel"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Immigration and Cultural Diversity in Ontario", summary:"Students learn how immigration has shaped Ontario's diverse population and culture throughout history and today.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Immigration means ___.", options:["moving to another city in the same country","moving to a new country to live permanently","travelling for vacation","going to school in a different province"], answer:1},
     {q:"Why do people immigrate to Ontario?", options:["Only for bad reasons","For opportunities, safety, family reunification, and a better quality of life","Only for the weather","They are forced to always"], answer:1},
     {q:"Cultural diversity means ___.", options:["everyone is the same","a mix of people with different backgrounds, languages, traditions, and perspectives","only different food","only different clothing"], answer:1},
     {q:"How has immigration benefited Ontario?", options:["It has not","It has enriched Ontario with diverse skills, cultures, foods, arts, and economic contributions","Only economically","Only culturally"], answer:1},
     {q:"Which city in Ontario is one of the most culturally diverse cities in the world?", options:["A small northern town","Ottawa","Toronto","Thunder Bay"], answer:2}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"Language", title:"Non-Fiction Reading: Compare and Contrast", summary:"Students identify similarities and differences between two topics in a text using compare-and-contrast structure.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"To compare means to ___.", options:["only list differences","identify similarities between two or more things","describe only one thing","count all the differences"], answer:1},
     {q:"To contrast means to ___.", options:["identify similarities","describe one thing","identify differences between two or more things","combine two things"], answer:2},
     {q:"Signal words for comparison include ___.", options:["however, but, unlike","both, also, similarly","first, then, finally","because, so, therefore"], answer:1},
     {q:"Signal words for contrast include ___.", options:["both, also, in the same way","however, but, on the other hand, unlike","first, then, after that","because, since, due to"], answer:1},
     {q:"A Venn diagram is useful for ___.", options:["multiplying fractions","solving equations","showing similarities and differences between two topics","ordering events in time"], answer:2}
   ]},
  {subject:"Math", title:"Measurement: Area", summary:"Students find the area of rectangles by counting square units or using the formula length × width.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Area is ___.", options:["the distance around a shape","the weight of a shape","the amount of space inside a 2D shape","the length of one side"], answer:2},
     {q:"A rectangle 4 cm long and 3 cm wide has an area of ___.", options:["7 cm","10 cm","12 cm²","14 cm"], answer:2},
     {q:"Area is measured in ___.", options:["only centimetres","square units (cm², m², etc.)","grams","degrees"], answer:1},
     {q:"To find the area of a rectangle, you ___.", options:["add all sides","subtract length from width","divide length by width","multiply length × width"], answer:3},
     {q:"A square with side 5 m has an area of ___.", options:["10 m²","20 m²","25 m²","30 m²"], answer:2}
   ]},
  {subject:"Science", title:"Pulleys, Gears, and Compound Machines", summary:"Students learn how pulleys change the direction of a force, how gears transfer motion, and how compound machines combine two or more simple machines.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A pulley uses a ___ to redirect or reduce force needed to lift a load.", options:["wedge","screw","rope and grooved wheel","lever and fulcrum"], answer:2},
     {q:"Gears are used to ___.", options:["hold things together like nails","change the speed or direction of motion","measure weight","only decorate machines"], answer:1},
     {q:"A compound machine is ___.", options:["a very simple tool","one that combines two or more simple machines","only a bicycle","only a computer"], answer:1},
     {q:"A bicycle is a compound machine because it uses ___.", options:["only pedals","wheels and axles, a chain system (gears), and levers (brakes)","only gears","only a seat"], answer:1},
     {q:"Which is an example of a simple machine inside a compound machine?", options:["A computer chip","A wheel on a bicycle","An electric motor","A battery"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ontario's Relationship with the Rest of Canada", summary:"Students explore how Ontario is connected to other provinces through trade, shared government, geography, and culture.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Ontario is connected to other provinces through ___.", options:["only highways","trade, shared national government, transportation, and cultural ties","no connections","only weather"], answer:1},
     {q:"Which province borders Ontario to the west?", options:["Quebec","Manitoba","British Columbia","Nova Scotia"], answer:1},
     {q:"Products made in Ontario are often ___.", options:["kept only in Ontario","traded to other provinces and countries","never used elsewhere","only sold locally"], answer:1},
     {q:"The Trans-Canada Highway connects ___.", options:["only Ontario and Quebec","provinces and territories across Canada","only British Columbia and Alberta","only southern cities"], answer:1},
     {q:"Why is Ontario important to Canada's economy?", options:["It is not","Ontario has a large population, a major financial centre (Toronto), and significant manufacturing and agricultural output","Only for its weather","Only for its size"], answer:1}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"Language", title:"Reading: Point of View", summary:"Students identify the narrator's point of view (first person: I, me; third person: he, she, they) and consider how different perspectives shape the telling of a story.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"First-person point of view uses the pronouns ___.", options:["he, she, they","I, me, my, we","you, your","it, its"], answer:1},
     {q:"Third-person point of view uses the pronouns ___.", options:["I, me, my","you, your","he, she, they, his, her, their","we, us"], answer:2},
     {q:"The point of view affects ___.", options:["only the length of the story","what information the reader receives and how connected they feel to the narrator","only the setting","only the font"], answer:1},
     {q:"In "I ran as fast as I could," the narrator is speaking in ___.", options:["third person","second person","first person","no person"], answer:2},
     {q:"In "She grabbed her bag and ran," the narrator is speaking in ___.", options:["first person","second person","third person","fourth person"], answer:2}
   ]},
  {subject:"Math", title:"Data: Tally Charts and Bar Graphs", summary:"Students collect data using tally marks and represent it in a bar graph. They read and interpret graphs to answer questions.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In a tally chart, a group of 5 is shown as ___.", options:["IIIII","||||","|||||  (four vertical lines with one diagonal line through)","VVVVV"], answer:2},
     {q:"A bar graph shows data using ___.", options:["dots","lines only","bars (rectangles) of different heights or lengths","only circles"], answer:2},
     {q:"What does the y-axis (vertical axis) of a bar graph typically show?", options:["Labels (categories)","Only colours","The quantity or amount","Only time"], answer:2},
     {q:"If the bar for "apples" reaches 8 on the graph, how many apples were counted?", options:["4","6","8","10"], answer:2},
     {q:"Why do we organise data in charts and graphs?", options:["To make it confusing","To make it easier to read, compare, and draw conclusions","Only for decoration","Only for adults"], answer:1}
   ]},
  {subject:"Science", title:"Weathering and Erosion", summary:"Students learn how wind, water, ice, and plants break down and move rocks (weathering and erosion), shaping the landscape over time.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Weathering is the process of ___.", options:["building up rocks","plants growing","the breaking down of rocks and minerals by wind, water, ice, and chemicals","flooding only"], answer:2},
     {q:"Erosion is ___.", options:["the build-up of sediment in one place","breaking rocks into minerals","the movement of weathered material (soil, rock) from one place to another","plant growth"], answer:2},
     {q:"Which agent of erosion is responsible for the Grand Canyon?", options:["Ice","Wind","Water (the Colorado River)","Roots"], answer:2},
     {q:"How do plant roots affect rocks?", options:["They smooth them","They have no effect","Roots can grow into rock cracks, widening them (biological weathering)","They melt rocks"], answer:2},
     {q:"Which human activity can speed up erosion?", options:["Planting trees","Removing vegetation from slopes through logging or construction","Building stone walls","Using underground water"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Mapping Skills: Grid References", summary:"Students use a grid (using letters and numbers) to locate places on a map and practise reading coordinates.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A map grid uses ___ and ___ to name locations.", options:["colours and shapes","letters and numbers","symbols and pictures","flags and icons"], answer:1},
     {q:"If a city is at B3 on a grid map, where is it?", options:["Row A, column 3","Row B, column 3","Row 3, column B","Row C, column 2"], answer:1},
     {q:"Why do maps use grids?", options:["Only for decoration","To make maps look better","To help locate specific places quickly and accurately","Only for large maps"], answer:2},
     {q:"In a grid reference "C5", the letter usually refers to the ___.", options:["column","row","scale","compass direction"], answer:1},
     {q:"Which tool would you use to find grid coordinates on a map?", options:["A thermometer","A ruler and map index","A scale model","A photograph"], answer:1}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"Language", title:"Spelling Strategies", summary:"Students apply phonics, word patterns, and the "look-cover-write-check" strategy to spell words accurately.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The "look, cover, write, check" strategy helps you ___.", options:["read faster","do maths","practise spelling by seeing, hiding, writing, and verifying the word","draw pictures"], answer:1},
     {q:"A word family shares the same ___.", options:["first letter","word origin and spelling pattern (e.g., -at: cat, bat, hat)","number of syllables","only vowels"], answer:1},
     {q:"To spell "because," you could remember ___.", options:["the letters B-E-C-A-U-S-E","only the first letter","it has 3 syllables","it starts with a vowel"], answer:0},
     {q:"Looking for smaller words inside bigger words helps ___.", options:["make words longer","you remember how to spell longer words (e.g., "there" contains "here")","nothing","replace spelling practice"], answer:1},
     {q:"Which of these is spelled correctly?", options:["Becaus","Becawse","Because","Becaze"], answer:2}
   ]},
  {subject:"Math", title:"Fractions: Comparing and Equivalent", summary:"Students compare fractions with the same denominator and explore simple equivalent fractions (1/2 = 2/4).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which is larger: 3/5 or 1/5?", options:["1/5","3/5","They are equal","Cannot tell"], answer:1},
     {q:"Equivalent fractions are ___.", options:["fractions with the same numerator","different fractions that represent the same amount","only whole numbers","always improper"], answer:1},
     {q:"1/2 is equivalent to ___.", options:["2/3","2/4","3/4","2/8"], answer:1},
     {q:"Which fraction is equivalent to 2/3?", options:["3/4","4/6","3/5","4/5"], answer:1},
     {q:"To compare fractions with the same denominator, compare ___.", options:["denominators","numerators","the size of the paper","the colours"], answer:1}
   ]},
  {subject:"Science", title:"Animals and Their Habitats (Ontario Focus)", summary:"Students study specific Ontario habitats (boreal forest, Great Lakes wetlands, grasslands) and animals adapted to each.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The boreal forest in Ontario is characterized by ___.", options:["palm trees and warm weather","dense coniferous (evergreen) trees and cold winters","sandy deserts","tropical animals"], answer:1},
     {q:"A wetland habitat provides ___.", options:["only open water","shallow water, dense vegetation, and rich nutrients supporting many birds, fish, and amphibians","no wildlife","only fish"], answer:1},
     {q:"Which Ontario animal is well adapted to aquatic environments (ponds and rivers)?", options:["Prairie dog","Beaver","Desert tortoise","Coyote"], answer:1},
     {q:"Why are Ontario's wetlands important?", options:["They are not","They filter water, absorb flood water, and provide habitat for many species","Only for fishing","Only for tourism"], answer:1},
     {q:"The Canadian Shield in northern Ontario is home to ___.", options:["mainly tropical animals","mainly boreal forest wildlife including moose, black bears, and wolves","only birds","only fish"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Settlement Patterns in Ontario", summary:"Students explore why early communities developed where they did — near rivers, lakes, trade routes — and how settlement patterns continue to evolve.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Early Ontario communities were most often built ___.", options:["in the middle of dense forests far from water","near rivers and lakes for water, transportation, and food","in deserts","on mountain tops"], answer:1},
     {q:"Why was access to water important for early settlements?", options:["It was not","Rivers and lakes provided drinking water, fish, transportation routes, and power for mills","Only for bathing","Only for hunting"], answer:1},
     {q:"Toronto became a major city partly because ___.", options:["it has the coldest winters","it is located on Lake Ontario, providing a natural harbour for trade","it has no rivers","it is in the mountains"], answer:1},
     {q:"As transportation improved, settlements ___.", options:["shrank","spread further from waterways along roads and railways","stopped growing","moved to northern areas only"], answer:1},
     {q:"Which factor still influences where cities grow today?", options:["Only weather","Access to transportation, employment, resources, and services","Only water like in the past","Only government decisions"], answer:1}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"Language", title:"Reading: Asking Questions", summary:"Students learn to ask questions before, during, and after reading to monitor comprehension and engage deeply with texts.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Asking questions before reading helps you ___.", options:["finish the book faster","activate prior knowledge and set a purpose for reading","write better","skip the hard parts"], answer:1},
     {q:"Asking questions DURING reading helps you ___.", options:["read faster","think more deeply and check your understanding as you go","avoid the confusing parts","copy the text"], answer:1},
     {q:"After reading, you might ask ___.", options:["What is this book's font?","Why did this happen? What would I do differently? What does this teach me?","How many pages did I read?","Who published this?"], answer:1},
     {q:"A "thick question" is one ___.", options:["with a yes/no answer","with a one-word answer","that requires thinking and discussion — no single right answer","about the author"], answer:2},
     {q:"Asking questions about a text is a sign of ___.", options:["poor reading","active and engaged reading","not understanding at all","skimming only"], answer:1}
   ]},
  {subject:"Math", title:"Time: Hours, Minutes, and Elapsed Time", summary:"Students tell time to the nearest minute using an analogue clock and calculate elapsed time.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"On an analogue clock, the short hand shows ___.", options:["minutes","seconds","hours","days"], answer:2},
     {q:"On an analogue clock, the long hand shows ___.", options:["hours","seconds","days","minutes"], answer:3},
     {q:"It is 2:15. What time is it 45 minutes later?", options:["2:45","3:00","3:15","2:60"], answer:1},
     {q:"What does "elapsed time" mean?", options:["The time on the clock","How much time passes between a start and end time","The time zone","The exact time right now"], answer:1},
     {q:"A movie starts at 1:30 pm and ends at 3:00 pm. How long is the movie?", options:["1 hour","1.5 hours","2 hours","2.5 hours"], answer:1}
   ]},
  {subject:"Science", title:"Energy: Forms and Sources", summary:"Students explore forms of energy (light, heat, sound, electrical, mechanical) and sources (Sun, wind, water, fossil fuels).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Energy is defined as ___.", options:["a type of matter","the ability to do work or cause change","only electricity","only heat"], answer:1},
     {q:"The Sun is a source of ___ energy.", options:["only sound","only mechanical","light and heat","only electrical"], answer:2},
     {q:"Which is a renewable energy source?", options:["Coal","Natural gas","Oil","Wind"], answer:3},
     {q:"A non-renewable energy source is ___.", options:["solar power","wind energy","fossil fuels (coal, oil, natural gas)","hydroelectric power"], answer:2},
     {q:"Electrical energy can be transformed into ___.", options:["nothing","light, heat, and sound (e.g., in a light bulb, a toaster, a speaker)","only movement","only light"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ontario's Economy Today", summary:"Students explore Ontario's major industries: manufacturing, agriculture, technology, finance, and mining.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which industry produces cars and vehicles in Ontario?", options:["Forestry","Fishing","Manufacturing","Only farming"], answer:2},
     {q:"Ontario's Bay Street in Toronto is known for ___.", options:["beaches","forests","financial services and banking","mining"], answer:2},
     {q:"Agriculture in Ontario produces ___.", options:["cars and trucks","grains, fruits, vegetables, dairy, and meat products","electronics","only wheat"], answer:1},
     {q:"Ontario is Canada's ___ most populous province.", options:["least","second","largest and most","fourth"], answer:2},
     {q:"Why is technology a growing industry in Ontario?", options:["It is not","Toronto and Waterloo have become major tech hubs attracting companies and talent globally","Only in the last month","Only one company exists"], answer:1}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"Language", title:"Writing: Procedural Texts", summary:"Students write how-to instructions with a clear title, list of materials, numbered steps, and sequence words (first, next, then, finally).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A procedural text tells you ___.", options:["a fictional story","how to do or make something step by step","a poem","a persuasive essay"], answer:1},
     {q:"Sequence words in procedural writing include ___.", options:["however, although, but","first, next, then, finally","because, since, therefore","only nouns and verbs"], answer:1},
     {q:"Why are numbered steps important in instructions?", options:["They are not","They tell the reader the exact order to follow","They only look nice","They replace the materials list"], answer:1},
     {q:"A procedural text usually begins with ___.", options:["a plot twist","a conclusion","a title and a list of materials needed","a character description"], answer:2},
     {q:"Which is an example of a procedural text?", options:["A fairy tale","A poem about rain","Step-by-step instructions on how to plant a seed","A chapter from a novel"], answer:2}
   ]},
  {subject:"Math", title:"3D Geometry: Faces, Edges, Vertices", summary:"Students identify faces, edges, and vertices on 3D shapes (cube, rectangular prism, triangular prism, cylinder, cone, sphere, pyramid).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A cube has ___ faces.", options:["4","5","6","8"], answer:2},
     {q:"A vertex (vertices) of a shape is ___.", options:["a flat surface","a straight edge","a corner where edges meet","a curved surface"], answer:2},
     {q:"How many edges does a cube have?", options:["6","8","12","24"], answer:2},
     {q:"A sphere has ___ faces, ___ edges, and ___ vertices.", options:["1, 0, 0","0, 0, 0","2, 1, 0","1, 1, 1"], answer:1},
     {q:"A triangular prism has ___ triangular faces.", options:["1","2","3","4"], answer:1}
   ]},
  {subject:"Science", title:"Light: Reflection and Shadows", summary:"Students explore how light travels in straight lines, reflects off surfaces (mirrors), refracts (bends) when passing through water or glass, and creates shadows.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Light travels in ___.", options:["curves","spirals","waves that bend easily","straight lines"], answer:3},
     {q:"A shadow forms when an object ___.", options:["reflects all light","blocks light from passing through","absorbs all heat","only moves"], answer:1},
     {q:"Reflection of light occurs when ___.", options:["light is absorbed completely","light passes through an object","light bounces off a surface back toward your eyes","light slows down"], answer:2},
     {q:"Refraction is when light ___.", options:["travels in a straight line through air","bends as it passes from one medium to another (e.g., air to water)","creates a shadow","reflects off a mirror"], answer:1},
     {q:"A smooth, shiny surface like a mirror gives ___.", options:["a blurry, scattered reflection","a clear, regular reflection","no reflection","only a shadow"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canadian Citizenship", summary:"Students learn what it means to be a responsible citizen: following laws, voting, contributing to the community, and respecting others.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A citizen is ___.", options:["only a government official","a legal member of a country who has rights and responsibilities","only an adult","only a voter"], answer:1},
     {q:"Which right do Canadian citizens have?", options:["To break any law","To vote in federal elections","To ignore community rules","To be exempt from taxes"], answer:1},
     {q:"Which is a responsibility of citizenship?", options:["Doing whatever you want","Obeying laws, paying taxes, and contributing positively to the community","Only voting","Only working"], answer:1},
     {q:"Volunteering in your community is an example of ___.", options:["poor citizenship","active, responsible citizenship","only professional work","only for adults"], answer:1},
     {q:"Why is respecting others' rights important?", options:["It is not","A fair and safe community depends on everyone respecting each other's rights and dignity","Only for politicians","Only in schools"], answer:1}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"Language", title:"Reading Strategies Review", summary:"Students review and consolidate key reading strategies: predicting, questioning, making connections, visualising, and summarising.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Predicting while reading means ___.", options:["skipping ahead","using clues to guess what will happen next","always being right","only looking at pictures"], answer:1},
     {q:"Making a connection to the text means ___.", options:["ignoring the text","relating what you read to your own experiences, other books, or the world","only memorising it","only summarising"], answer:1},
     {q:"Visualising while reading means ___.", options:["looking at the illustrations only","creating a mental image of what the text describes","drawing your own story","skipping descriptions"], answer:1},
     {q:"Summarising means ___.", options:["copying the whole text","retelling every tiny detail","expressing the main points and key events concisely in your own words","only reading the first line"], answer:2},
     {q:"Which strategy helps when a word is confusing?", options:["Give up","Read on for context clues or reread the sentence","Skip it permanently","Ask someone else to read for you"], answer:1}
   ]},
  {subject:"Math", title:"Probability: Likely, Unlikely, Certain, Impossible", summary:"Students use probability language to describe the likelihood of events.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"An event is "certain" if ___.", options:["it will never happen","it happens by chance","it will definitely happen every time","it sometimes happens"], answer:2},
     {q:"An event is "impossible" if ___.", options:["it might happen","it will definitely happen","it has never happened before","it cannot possibly happen"], answer:3},
     {q:"Rolling a number between 1 and 6 on a standard die is ___.", options:["impossible","unlikely","likely","certain"], answer:3},
     {q:"Getting tails on a fair coin flip is ___.", options:["certain","impossible","equally likely as getting heads","always impossible"], answer:2},
     {q:"Drawing a red marble from a bag of only blue marbles is ___.", options:["certain","likely","unlikely","impossible"], answer:3}
   ]},
  {subject:"Science", title:"Habitats Review and Biodiversity", summary:"Students review Ontario habitats and learn that biodiversity — the variety of living things — is essential for healthy ecosystems.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Biodiversity means ___.", options:["having only one type of animal","having only plants","the variety of living things in an ecosystem","only counting species"], answer:2},
     {q:"High biodiversity is a sign of ___.", options:["an unhealthy ecosystem","a healthy ecosystem where many species interact","too many animals","too few plants"], answer:1},
     {q:"Which human activity threatens biodiversity?", options:["Planting native gardens","Creating nature reserves","Habitat destruction through deforestation and urban sprawl","Protecting endangered species"], answer:2},
     {q:"An endangered species is one that ___.", options:["is very common","is at risk of becoming extinct","has already gone extinct","only lives in zoos"], answer:1},
     {q:"Why is protecting biodiversity important?", options:["It is not","Ecosystems with many species are more resilient, and all species play a role in keeping ecosystems balanced","Only for rare animals","Only for scientists"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Community Celebrations and Heritage", summary:"Students explore how Ontario communities celebrate cultural heritage through festivals, traditions, and public holidays.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Heritage is ___.", options:["only old buildings","the traditions, language, values, and history passed from earlier generations","only museums","only food"], answer:1},
     {q:"Canada Day (July 1) celebrates ___.", options:["the end of winter","Canada becoming a self-governing country in 1867","Ontario's founding only","a sports victory"], answer:1},
     {q:"Remembrance Day (November 11) honours ___.", options:["Canada's birthday","Indigenous peoples only","Canadian soldiers who served and died in wars and peacekeeping missions","a famous inventor"], answer:2},
     {q:"How do multicultural festivals contribute to Ontario communities?", options:["They cause conflict","They allow communities to share and celebrate diverse cultural traditions, building mutual respect","Only for food vendors","Only for tourists"], answer:1},
     {q:"Why is it important to celebrate and preserve heritage?", options:["It is not","It connects people to their roots, builds identity, and helps communities understand their shared history","Only in museums","Only for old people"], answer:1}
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"Language", title:"Verb Tenses: Past, Present, Future", summary:"Students identify and use past, present, and future tenses. They understand that tense tells when an action happens.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which sentence is in the PAST tense?", options:["I walk to school.","She is running.","He ate his lunch.","They will play tomorrow."], answer:2},
     {q:"Which sentence is in the PRESENT tense?", options:["She ran yesterday.","They will come soon.","We are playing now.","He had left already."], answer:2},
     {q:"Future tense uses the word ___.", options:["was","is","are","will"], answer:3},
     {q:"Change "I run" to past tense.", options:["I will run","I am running","I ran","I running"], answer:2},
     {q:"Which word signals the past tense?", options:["Tomorrow","Now","Yesterday","Soon"], answer:2}
   ]},
  {subject:"Math", title:"Multiplication Facts: Review to 10×10", summary:"Students consolidate multiplication facts up to 10×10 and use strategies to solve unknown facts.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"7 × 8 = ?", options:["54","56","58","60"], answer:1},
     {q:"9 × 6 = ?", options:["48","52","54","58"], answer:2},
     {q:"6 × 6 = ?", options:["32","34","36","40"], answer:2},
     {q:"What strategy helps remember 9× facts?", options:["Count by 5s","The "10× minus 1 group" strategy: 9×7 = 70−7 = 63","Random guessing","Skip by 4s"], answer:1},
     {q:"10 × 10 = ?", options:["10","20","100","1000"], answer:2}
   ]},
  {subject:"Science", title:"Magnets", summary:"Students explore properties of magnets: poles (N/S), attraction, repulsion, magnetic fields, and everyday uses.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Opposite poles of magnets ___.", options:["repel","attract","do nothing","break apart"], answer:1},
     {q:"Like poles of magnets ___.", options:["attract strongly","repel (push away)","have no reaction","stick together always"], answer:1},
     {q:"A magnetic field is ___.", options:["visible lines you can see","the region around a magnet where magnetic forces act","only at the poles","only inside iron"], answer:1},
     {q:"Which material is attracted to a magnet?", options:["Wood","Glass","Plastic","Iron/Steel"], answer:3},
     {q:"Magnets are used in ___.", options:["only refrigerators","many devices including compasses, speakers, motors, and credit cards","nothing modern","only toys"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Urban and Rural Communities: Services", summary:"Students compare the services available in urban and rural communities, exploring how geography and population affect service availability.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which service is more commonly found in large urban areas?", options:["A small one-room schoolhouse","A major hospital with specialist care","A grain elevator","A logging camp"], answer:1},
     {q:"A rural community might rely on ___.", options:["subway systems","long-distance travel to access specialised medical and retail services","skyscrapers","a packed public transit system"], answer:1},
     {q:"Which statement about population is true?", options:["Urban areas have fewer people than rural areas","Urban areas have more people per square kilometre than rural areas","Both have the same population density","Rural areas are always more populated"], answer:1},
     {q:"What is one advantage of rural communities?", options:["More restaurants","Closer to nature, lower cost of living, quieter environments","More hospitals","Faster internet access always"], answer:1},
     {q:"What is one challenge of rural communities in Ontario?", options:["Too many people","Limited access to certain services and employment opportunities","Too much traffic","Too many schools"], answer:1}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"Language", title:"Summarising: Non-Fiction", summary:"Students summarise non-fiction texts by identifying the main idea, key details, and omitting unnecessary information.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"To summarise a non-fiction text, you should ___.", options:["copy every sentence","include only the main idea and key supporting details in your own words","make up new information","only write the first paragraph"], answer:1},
     {q:"Which information should be OMITTED in a summary?", options:["The main idea","Key supporting facts","Interesting minor details that do not support the main idea","The topic of the text"], answer:2},
     {q:"A good summary is ___.", options:["as long as the original","longer than the original","much shorter than the original while keeping the key ideas","exactly one word"], answer:2},
     {q:"The first sentence of a summary should ___.", options:["be a question","state the main idea of the text","give a personal opinion","list all the details"], answer:1},
     {q:"Why is summarising an important reading skill?", options:["It is not","It shows you understood the key ideas and helps you remember and discuss what you read","Only for tests","Only for non-fiction"], answer:1}
   ]},
  {subject:"Math", title:"Fractions on a Number Line", summary:"Students place fractions on a number line between 0 and 1, understanding that fractions represent parts between whole numbers.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"On a number line, 1/2 is located ___.", options:["at 0","at 1","halfway between 0 and 1","past 1"], answer:2},
     {q:"Which fraction is closer to 1 on a number line?", options:["1/4","1/8","3/4","1/2"], answer:2},
     {q:"Where would 1/4 be placed on a number line from 0 to 1?", options:["At 0","One quarter of the way between 0 and 1","At 1","Three quarters of the way between 0 and 1"], answer:1},
     {q:"Which fraction is closest to 0?", options:["3/4","1/2","1/4","1/8"], answer:3},
     {q:"On a number line from 0 to 1, 3/4 is ___.", options:["before 1/2","after 1/2 but before 1","after 1","at 1"], answer:1}
   ]},
  {subject:"Science", title:"Forces: Gravity and Friction", summary:"Students investigate gravity as a downward force and friction as a resistance force. They explore how these affect motion.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Gravity is a force that ___.", options:["pushes objects upward","pulls objects toward the centre of the Earth","has no effect on motion","only affects large objects"], answer:1},
     {q:"Friction is a force that ___.", options:["speeds objects up","pulls objects downward","resists the motion of surfaces sliding against each other","has no effect on objects"], answer:2},
     {q:"A smooth surface causes ___ friction than a rough surface.", options:["more","the same","less","no"], answer:2},
     {q:"Without friction, it would be very difficult to ___.", options:["fly a kite","walk, drive, or grip anything (friction is essential for traction)","swim","see clearly"], answer:1},
     {q:"Gravity pulls all objects downward at the same rate regardless of ___.", options:["their colour","their size and mass (in a vacuum)","their shape","their temperature"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ontario and the Environment", summary:"Students explore environmental issues in Ontario: pollution, conservation, and the role citizens and government play in protecting natural spaces.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The Greenbelt in Ontario is ___.", options:["a type of vegetable garden","a protected area of farmland, forests, and wetlands around the Greater Toronto Area","a sports field","a government building"], answer:1},
     {q:"Water pollution in the Great Lakes is caused by ___.", options:["natural processes only","industrial discharge, agricultural runoff, and urban sewage","only rain","only wildlife"], answer:1},
     {q:"Conservation means ___.", options:["using resources as fast as possible","careful management and protection of natural resources","only recycling paper","only planting trees"], answer:1},
     {q:"How can citizens help protect Ontario's environment?", options:["By doing nothing","Reducing waste, using less energy, supporting conservation efforts, and making sustainable choices","Only by voting","Only through protests"], answer:1},
     {q:"An Ontario Provincial Park is ___.", options:["a city park","a protected natural area where wildlife and ecosystems are preserved","a private farm","a golf course"], answer:1}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"Language", title:"Poetry: Reading and Interpreting", summary:"Students read various poem forms (haiku, cinquain, limerick) and identify poetic elements: rhyme, rhythm, stanza, simile, and metaphor.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Rhyme in poetry means ___.", options:["repeating the same word","ending lines with words that have the same ending sound","making lines very long","using no punctuation"], answer:1},
     {q:"A simile compares two things using "like" or "as." Which is a simile?", options:["The moon is a lantern in the sky","He ran like the wind","She is a shining star","The thunder spoke to the rain"], answer:1},
     {q:"A metaphor compares two things WITHOUT "like" or "as." Which is a metaphor?", options:["She runs like a deer","He is as tall as a tree","Life is a journey","The rain falls like tears"], answer:2},
     {q:"A haiku has ___ syllables in the pattern 5-7-5.", options:["15","17","19","21"], answer:1},
     {q:"A stanza in a poem is like a ___ in prose writing.", options:["sentence","paragraph","chapter","word"], answer:1}
   ]},
  {subject:"Math", title:"Money: Counting and Making Change", summary:"Students identify Canadian coins and bills, count amounts of money, and calculate simple change.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"How many cents are in one dollar?", options:["10","50","100","1000"], answer:2},
     {q:"Which coin is worth 25 cents?", options:["Nickel","Dime","Quarter","Loonie"], answer:2},
     {q:"$2.50 + $1.75 = ?", options:["$3.25","$4.00","$4.25","$4.50"], answer:2},
     {q:"You have $5.00 and spend $3.25. How much change do you get?", options:["$1.75","$2.75","$1.25","$2.25"], answer:0},
     {q:"A toonie is worth ___.", options:["$1.00","$0.25","$2.00","$0.50"], answer:2}
   ]},
  {subject:"Science", title:"Rocks: Igneous, Sedimentary, Metamorphic", summary:"Students classify rocks into three types and understand how each forms.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Igneous rocks form from ___.", options:["pressed sediment layers","living organisms","metamorphism","cooled magma or lava"], answer:3},
     {q:"Sedimentary rocks form from ___.", options:["cooled lava","metamorphism","layers of sediment (sand, silt, shells) compressed over time","volcanic eruptions"], answer:2},
     {q:"Metamorphic rocks form when existing rocks are ___.", options:["erupted from a volcano","washed by the sea","changed by extreme heat and pressure deep in the Earth","dissolved in water"], answer:2},
     {q:"Granite is an example of an ___ rock.", options:["sedimentary","metamorphic","igneous","fossil"], answer:2},
     {q:"Fossils are most commonly found in ___ rock.", options:["igneous","metamorphic","sedimentary","volcanic"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Economy: Goods and Services", summary:"Students explore the difference between goods (physical products) and services (activities that meet needs), and how they are exchanged.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Goods are ___.", options:["things people do for you","physical products you can hold and buy","only free things","only natural resources"], answer:1},
     {q:"Services are ___.", options:["only food","activities that someone does for you that meet a need","physical objects you buy","only government actions"], answer:1},
     {q:"Which is a GOOD?", options:["A haircut","A doctor's appointment","A new pair of shoes","A music lesson"], answer:2},
     {q:"Which is a SERVICE?", options:["A chocolate bar","A bicycle","A plumber fixing a pipe","A book"], answer:2},
     {q:"Why is trade (buying and selling goods and services) important?", options:["It is not","Trade allows communities to get things they need that they cannot produce themselves","Only for large countries","Only in cities"], answer:1}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"Language", title:"Non-Fiction: Cause and Effect in Science Texts", summary:"Students practise identifying cause-and-effect relationships in non-fiction science texts using text clues and structure.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In a science text, "because" often signals ___.", options:["a sequence of events","an effect","a cause coming next","the main idea"], answer:2},
     {q:"In a science text, "therefore" often signals ___.", options:["a cause","an effect or result","a new topic","an example"], answer:1},
     {q:"Which sentence contains a cause-and-effect relationship?", options:["The sky is blue.","Dogs are mammals.","Because the temperature dropped, water in the pond froze.","Animals need food."], answer:2},
     {q:"The cause in "The plant died because it had no water" is ___.", options:["The plant died","it had no water","The plant","because"], answer:1},
     {q:"The effect in "The animal population declined because the habitat was destroyed" is ___.", options:["the habitat was destroyed","because","The animal population declined","The habitat"], answer:0}
   ]},
  {subject:"Math", title:"Patterns: Growing and Shrinking", summary:"Students identify and extend growing (increasing) and shrinking (decreasing) patterns using numbers, shapes, and objects.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A growing pattern is one that ___.", options:["stays the same","decreases with each term","increases with each term","repeats in a cycle"], answer:2},
     {q:"Identify the pattern: 2, 4, 6, 8... It is ___.", options:["shrinking by 2","growing by 2","random","staying the same"], answer:1},
     {q:"What comes next in: 20, 17, 14, 11, ___?", options:["8","9","10","7"], answer:0},
     {q:"What is the rule for: 3, 6, 9, 12...?", options:["Add 2","Add 3","Subtract 3","Multiply by 2"], answer:1},
     {q:"Which is a growing pattern?", options:["10, 10, 10, 10","10, 8, 6, 4","5, 10, 15, 20","10, 9, 8, 7"], answer:2}
   ]},
  {subject:"Science", title:"Electricity: Static and Current", summary:"Students explore static electricity (build-up of charge) and current electricity (flowing charge that powers devices). They identify conductors and insulators.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Static electricity is caused by ___.", options:["flowing electrons in a wire","a build-up of electric charge on a surface (often from friction)","magnetism only","sound waves"], answer:1},
     {q:"Current electricity is ___.", options:["stationary charge","a flow of electrons through a conductor (like a wire)","only from batteries","only for large machines"], answer:1},
     {q:"A conductor allows ___.", options:["no electricity to pass","only static electricity","electricity to flow through it easily","light to pass through"], answer:2},
     {q:"An insulator ___.", options:["allows electricity to flow freely","blocks or resists the flow of electricity","attracts magnets","produces electricity"], answer:1},
     {q:"Which is a good conductor of electricity?", options:["Rubber","Plastic","Wood","Copper wire"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Rights of Children: UNCRC", summary:"Students learn about the United Nations Convention on the Rights of the Child (UNCRC) and key rights: education, protection, participation, and health.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The UNCRC is ___.", options:["a type of food","a Canadian law only","an international agreement on children's rights signed by most countries","a school rule"], answer:2},
     {q:"According to the UNCRC, all children have the right to ___.", options:["only education","only health care","education, protection from harm, health care, and participation in decisions affecting them","only play"], answer:2},
     {q:"Which right is described: "No child should be made to work in dangerous conditions."", options:["Right to education","Right to play","Right to protection from exploitation and harm","Right to a name"], answer:2},
     {q:"Which right is described: "Children should be able to share their views on matters affecting them."", options:["Right to food","Right to health","Right to protection","Right to participate and be heard"], answer:3},
     {q:"Why is knowing your rights important?", options:["It is not","It empowers children to recognise when rights are being violated and to seek help","Only for lawyers","Only for adults"], answer:1}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"Language", title:"Writing: Opinion", summary:"Students write opinion paragraphs stating a clear position, giving reasons supported by evidence or examples, and using opinion language.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"An opinion is ___.", options:["a proven fact","a belief or view that reflects a personal perspective, not universal fact","only a complaint","only a question"], answer:1},
     {q:"Opinion writing should include ___.", options:["only facts with no personal stance","a clear position and reasons or evidence to support it","only questions","random information"], answer:1},
     {q:"Which is an opinion sentence?", options:["Water freezes at 0°C.","Canada is in North America.","Recess should be 30 minutes because it improves focus and wellbeing.","The Sun rises in the east."], answer:2},
     {q:"Opinion signal phrases include ___.", options:["first, next, finally","I believe, in my opinion, I think, it seems to me","because, since, therefore","however, although, but"], answer:1},
     {q:"A conclusion in opinion writing should ___.", options:["start a new argument","restate your opinion and summarise your main reasons","apologise for your opinion","list new facts"], answer:1}
   ]},
  {subject:"Math", title:"Division Facts: Linking to Multiplication", summary:"Students use their knowledge of multiplication to solve division problems (fact families).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"If 4 × 5 = 20, then 20 ÷ 4 = ?", options:["4","5","10","20"], answer:1},
     {q:"Which multiplication fact helps solve 36 ÷ 6?", options:["5 × 6 = 30","6 × 6 = 36","7 × 6 = 42","6 × 4 = 24"], answer:1},
     {q:"A fact family for 3, 7, 21 includes ___.", options:["3 + 7 = 10","3 × 7 = 21 and 21 ÷ 7 = 3","3 × 7 = 21 and 3 ÷ 7 = 21","3 + 7 = 21"], answer:1},
     {q:"21 ÷ 3 = ?", options:["6","7","8","9"], answer:1},
     {q:"45 ÷ 9 = ?", options:["4","5","6","7"], answer:1}
   ]},
  {subject:"Science", title:"The Water Cycle", summary:"Students explore how water moves through the water cycle: evaporation, condensation, and precipitation. They understand how the cycle distributes fresh water.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The water cycle is powered mainly by ___.", options:["wind","the Moon's gravity","energy from the Sun","Earth's rotation"], answer:2},
     {q:"Evaporation is when ___.", options:["liquid water falls as rain","water vapour turns into liquid droplets","liquid water changes to water vapour and rises into the atmosphere","water freezes"], answer:2},
     {q:"Condensation happens when ___.", options:["water evaporates","water vapour cools and turns into liquid water droplets (forming clouds)","it rains","water freezes into ice"], answer:1},
     {q:"Precipitation includes ___.", options:["only rain","only snow","only fog","rain, snow, sleet, or hail falling from clouds"], answer:3},
     {q:"Why is the water cycle important?", options:["It creates lightning","It continuously moves and purifies water, distributing fresh water to land ecosystems","Only for rivers","Only for oceans"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Cultural Practices in Ontario Communities", summary:"Students explore how cultural practices — food, clothing, music, art, language — contribute to the identity of Ontario's diverse communities.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Cultural practices are ___.", options:["only government rules","traditions, arts, language, food, and customs that are part of a group's identity","only found in other countries","only for elderly people"], answer:1},
     {q:"How do different cultural practices enrich Ontario communities?", options:["They cause confusion","They bring diverse perspectives, art, food, and ideas that make communities more vibrant","Only if everyone agrees","They do not"], answer:1},
     {q:"Which is an example of a cultural practice?", options:["A government law","Celebrating Diwali, Eid, or Chinese New Year with traditional foods, clothing, and rituals","A traffic sign","A school timetable"], answer:1},
     {q:"Respecting cultural practices means ___.", options:["only following your own culture","learning about and showing appreciation for the traditions of others","ignoring differences","only eating the same food"], answer:1},
     {q:"Why is language part of cultural identity?", options:["It is not","Language carries stories, values, and worldviews of a culture — preserving it helps keep the culture alive","Only for old languages","Only for writing"], answer:1}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"Language", title:"Reading: Inference", summary:"Students make inferences — use clues from the text plus their own knowledge to figure out what the author implies but does not state directly.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"An inference is ___.", options:["something stated directly in the text","a guess with no evidence","a conclusion drawn from text clues plus prior knowledge","only for non-fiction"], answer:2},
     {q:"When you infer, you use ___.", options:["only pictures","only the title","text clues plus what you already know","only the last paragraph"], answer:2},
     {q:"In "She grabbed her umbrella and slammed the door," we can infer ___.", options:["She is happy","She is going swimming","She might be upset and it could be raining","She has a new umbrella"], answer:2},
     {q:"Inference helps readers ___.", options:["only read faster","understand meaning beyond what is directly stated","only for tests","only for long books"], answer:1},
     {q:"Which question requires an inference?", options:["How many pages is this book?","Who is the author?","Why did the character act so nervously?","What is the title?"], answer:2}
   ]},
  {subject:"Math", title:"3D Shapes: Nets", summary:"Students identify and create nets — flat shapes that can be folded to make 3D shapes — for cubes, rectangular prisms, and triangular prisms.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A net of a 3D shape is ___.", options:["the weight of the shape","a flat pattern that folds up to form a 3D shape","a shadow of the shape","only for squares"], answer:1},
     {q:"A cube's net has ___ squares.", options:["4","5","6","8"], answer:2},
     {q:"If you fold a cross-shaped net, it forms a ___.", options:["sphere","cylinder","triangular prism","cube"], answer:3},
     {q:"A net helps students understand ___.", options:["the weight of objects","the 2D faces that make up a 3D shape","only area","only volume"], answer:1},
     {q:"A rectangular prism has ___ rectangular faces.", options:["4","6","8","2"], answer:1}
   ]},
  {subject:"Science", title:"Ecosystems and Food Chains", summary:"Students explore simple food chains in Ontario ecosystems: producer → primary consumer → secondary consumer, and the concept of the food web.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In a food chain, a producer is ___.", options:["an animal that hunts","a plant that makes its own food using sunlight (photosynthesis)","a decomposer","a top predator"], answer:1},
     {q:"A primary consumer eats ___.", options:["other animals","only decomposers","plants (producers)","nothing"], answer:2},
     {q:"A secondary consumer eats ___.", options:["only plants","primary consumers (herbivores) or omnivores","decomposers only","sunlight"], answer:1},
     {q:"What happens when one link in a food chain is removed?", options:["Nothing changes","The whole chain is affected — populations of other organisms rise or fall","Only the bottom level changes","Only predators are affected"], answer:1},
     {q:"A food web is ___.", options:["a single line of feeding relationships","a network of interconnected food chains showing multiple feeding relationships in an ecosystem","only for aquatic animals","only for plants"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Comparing Communities Around the World", summary:"Students compare communities in different countries with Ontario communities, exploring similarities and differences in climate, culture, economy, and geography.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Comparing communities from different countries helps us ___.", options:["avoid learning about others","understand and appreciate diverse ways of living and the challenges different communities face","feel superior","only find differences"], answer:1},
     {q:"A community in a desert region would face ___ challenges compared to one in Ontario.", options:["the same","different challenges like water scarcity and extreme heat","easier challenges","no challenges"], answer:1},
     {q:"What do most communities around the world have in common?", options:["The same language","The same food","Basic needs like shelter, food, water, and community connections","The same government"], answer:2},
     {q:"How does geography affect a community's economy?", options:["It does not","A community near the ocean may rely on fishing; one with forests may rely on forestry","Only in Canada","Only in ancient times"], answer:1},
     {q:"Cultural exchange between communities ___.", options:["causes problems","enriches both communities through shared ideas, technologies, and traditions","only benefits tourists","only benefits one side"], answer:1}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"Language", title:"Grammar: Adverbs and Prepositions", summary:"Students identify adverbs (modify verbs: how, when, where) and prepositions (show relationship in space/time: in, on, under, after).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"An adverb modifies a ___.", options:["noun","pronoun","adjective only","verb, adjective, or other adverb"], answer:3},
     {q:"In "She sang beautifully," the adverb is ___.", options:["She","sang","beautifully","is"], answer:2},
     {q:"A preposition shows ___.", options:["an action","a description of a noun","a relationship between a noun and another word (position, time, direction)","only movement"], answer:2},
     {q:"In "The cat sat under the table," the preposition is ___.", options:["cat","sat","under","table"], answer:2},
     {q:"Which word is an adverb?", options:["Happy","Quickly","Dog","Soft"], answer:1}
   ]},
  {subject:"Math", title:"Geometry: Congruence and Symmetry", summary:"Students identify congruent shapes (same size and shape) and lines of symmetry. They recognise symmetrical shapes by folding.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Congruent shapes are ___.", options:["the same colour","the same size AND shape","only the same size","only the same colour"], answer:1},
     {q:"A line of symmetry divides a shape into ___.", options:["unequal parts","two random pieces","two mirror-image halves","only triangles"], answer:2},
     {q:"How many lines of symmetry does a square have?", options:["1","2","3","4"], answer:3},
     {q:"A circle has ___ lines of symmetry.", options:["1","4","none","infinite (unlimited)"], answer:3},
     {q:"Which shape has exactly one line of symmetry?", options:["Square","Circle","Equilateral triangle","Isosceles triangle"], answer:3}
   ]},
  {subject:"Science", title:"Sound: Vibration, Pitch, Volume", summary:"Students explore how sound is produced (vibration), transmitted, and detected. They investigate pitch (high/low) and volume (loud/soft).",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Sound is produced by ___.", options:["magnetism","heat","light","vibration of an object"], answer:3},
     {q:"Pitch describes how ___ or ___ a sound is.", options:["loud or soft","fast or slow","long or short","high or low"], answer:3},
     {q:"Volume describes how ___ or ___ a sound is.", options:["high or low in pitch","fast or slow","loud or soft","short or long"], answer:2},
     {q:"A tighter or shorter string on a guitar produces ___.", options:["a lower pitch","the same pitch","a higher pitch","no sound"], answer:2},
     {q:"Sound travels as ___.", options:["light waves","magnetic fields","vibrations through a medium (air, water, or solid material)","electrical current"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Confederation and Canada's History", summary:"Students learn about Confederation (1867) when four provinces joined to form Canada, and how the country grew to its current size.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Confederation happened in ___.", options:["1776","1812","1867","1900"], answer:2},
     {q:"The first four provinces to join Confederation were ___.", options:["Ontario, Quebec, Nova Scotia, and New Brunswick","British Columbia, Alberta, Saskatchewan, Manitoba","Ontario, Quebec, British Columbia, Manitoba","All ten provinces at once"], answer:0},
     {q:"Canada's first Prime Minister was ___.", options:["Pierre Trudeau","Wilfrid Laurier","John A. Macdonald","Alexander Mackenzie"], answer:2},
     {q:"How many provinces and territories does Canada have today?", options:["10 provinces and 2 territories","10 provinces and 3 territories","9 provinces and 3 territories","12 provinces and territories"], answer:1},
     {q:"Why is Confederation important in Canadian history?", options:["It is not","It united separate British colonies into a new country with a federal government and shared laws","Only for Quebec","Only for Ontario"], answer:1}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"Language", title:"Research Skills: Finding Information", summary:"Students practise using books, encyclopedias, and reliable websites to find information. They evaluate source reliability.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A reliable source of information is one that ___.", options:["anyone can edit without verification","is authored by experts, fact-checked, and cites evidence","is only on social media","only contains pictures"], answer:1},
     {q:"An index in a non-fiction book helps you ___.", options:["read faster","find specific topics alphabetically at the back of the book","find the author's biography","draw pictures"], answer:1},
     {q:"Why should you look at multiple sources?", options:["You should not","To get a fuller picture and check that information is accurate and consistent across sources","Only for school projects","Only if you are unsure"], answer:1},
     {q:"When using the internet for research, you should ___.", options:["click any link","use only social media","check that the website is reputable and that information is current","copy and paste everything"], answer:2},
     {q:"Which is a signal that a website may be unreliable?", options:["It has a known author and institution","It cites other reliable sources","It looks professional","It has no author, no sources, and makes extreme claims"], answer:3}
   ]},
  {subject:"Math", title:"Area and Perimeter: Problem Solving", summary:"Students solve real-world problems involving area and perimeter of rectangles.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A garden is 8 m long and 5 m wide. What is its area?", options:["13 m²","26 m²","40 m²","45 m²"], answer:2},
     {q:"A garden is 8 m long and 5 m wide. What is its perimeter?", options:["13 m","26 m","40 m","45 m"], answer:1},
     {q:"A room has a perimeter of 24 m. If it is 8 m long, how wide is it?", options:["3 m","4 m","6 m","8 m"], answer:1},
     {q:"A square has an area of 36 cm². What is the side length?", options:["6 cm","7 cm","8 cm","9 cm"], answer:0},
     {q:"Two rectangles have the same perimeter but different areas. This is ___.", options:["impossible","always false","possible — shapes can have the same perimeter but different areas","only for squares"], answer:2}
   ]},
  {subject:"Science", title:"Human Impact on the Environment", summary:"Students explore positive and negative human impacts on natural environments. They understand stewardship and sustainability.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which is a NEGATIVE human impact on the environment?", options:["Planting trees","Creating wildlife corridors","Dumping toxic waste in a river","Setting up nature reserves"], answer:2},
     {q:"Which is a POSITIVE human impact on the environment?", options:["Burning fossil fuels","Overfishing","Urban sprawl replacing forests","Reforestation and habitat restoration"], answer:3},
     {q:"Stewardship means ___.", options:["exploiting resources for maximum profit","responsible management and care of the environment for future generations","only recycling","only for governments"], answer:1},
     {q:"Why is reducing plastic waste important?", options:["It is not","Plastic persists in ecosystems for hundreds of years and harms wildlife and waterways","Only for marine animals","Only in cities"], answer:1},
     {q:"How can Grade 3 students help the environment?", options:["They cannot","By reducing, reusing, and recycling; planting gardens; and raising awareness","Only by getting older first","Only by donating money"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Human Rights and Equity", summary:"Students explore the concept of human rights and equity — ensuring everyone gets what they need to thrive, not just equal treatment.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Human rights are ___.", options:["privileges earned by good behaviour","basic rights that every person has simply because they are human","only for citizens of wealthy countries","only for adults"], answer:1},
     {q:"Equity means ___.", options:["everyone gets exactly the same","everyone gets what they specifically need to have a fair chance","only equality of opportunity","never helping anyone extra"], answer:1},
     {q:"Which is an example of promoting equity at school?", options:["Giving everyone exactly the same assignment with no accommodations","Providing extra support to students who need it to achieve the same outcomes","Ignoring differences","Only helping top students"], answer:1},
     {q:"Why are human rights important?", options:["They are not","They protect every person's dignity and ensure people can live free from oppression","Only for some people","Only in democracies"], answer:1},
     {q:"The Charter of Rights and Freedoms protects ___.", options:["only government officials","only adults","the rights of people in Canada including freedom of expression, equality, and mobility","only citizens by birth"], answer:2}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"Language", title:"Oral Communication: Presentations", summary:"Students learn how to plan and deliver a short oral presentation. Key skills: clear voice, eye contact, staying on topic, and responding to questions.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"When presenting, you should ___.", options:["mumble quietly","speak clearly and project your voice so the audience can hear","read directly from a paper without looking up","talk as fast as possible"], answer:1},
     {q:"Eye contact with the audience shows ___.", options:["nervousness only","confidence and engagement with your listeners","aggression","lack of preparation"], answer:1},
     {q:"Good presentations are ___.", options:["as long as possible","always very short","organised with a clear beginning, middle, and end","only done by teachers"], answer:2},
     {q:"When someone in the audience asks a question, you should ___.", options:["ignore it","get upset","listen carefully and give a thoughtful answer","only repeat what you already said"], answer:2},
     {q:"Practising before a presentation ___.", options:["makes it worse","wastes time","helps you feel more confident and speak more fluently","only works for adults"], answer:2}
   ]},
  {subject:"Math", title:"Multiplication in Context: Word Problems", summary:"Students apply multiplication to solve real-world problems.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"There are 6 bags with 8 apples in each. How many apples in all?", options:["14","36","48","54"], answer:2},
     {q:"A box has 5 rows of 7 chocolates. How many chocolates?", options:["25","30","35","40"], answer:2},
     {q:"3 classes each have 24 students. How many students in all?", options:["60","66","72","78"], answer:2},
     {q:"Each of 8 shelves holds 9 books. How many books total?", options:["63","72","81","54"], answer:1},
     {q:"An orchard has 7 rows of 6 trees. How many trees?", options:["36","42","48","54"], answer:1}
   ]},
  {subject:"Science", title:"Technology and Science: Inventions", summary:"Students explore how scientific understanding leads to inventions that solve human problems. They investigate examples like the telephone, electricity, and vaccines.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"An invention is ___.", options:["a discovery of something already existing","a newly created device, process, or idea that solves a problem","only for scientists","only for adults"], answer:1},
     {q:"Alexander Graham Bell invented the ___.", options:["light bulb","telephone","printing press","car"], answer:1},
     {q:"A vaccine helps the body ___.", options:["become ill on purpose permanently","recognise and fight a specific disease without full infection","only treat illnesses after they occur","cure all diseases at once"], answer:1},
     {q:"The scientific method involves ___.", options:["only guessing","observing, questioning, hypothesising, experimenting, and drawing conclusions","only reading books","only performing experiments"], answer:1},
     {q:"Why is STEM (Science, Technology, Engineering, Math) important?", options:["It is not","STEM skills drive innovation, problem-solving, and advancements that improve people's lives","Only for boys","Only for university"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Communities in the Past vs Today", summary:"Students compare life in an Ontario community 100 years ago with life today, focusing on changes in transportation, communication, and daily life.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"One hundred years ago, most Ontarians communicated over long distances by ___.", options:["text message","email","telegraph and letter (and the early telephone)","video call"], answer:2},
     {q:"Transportation in Ontario has changed from ___.", options:["cars to horses","horses and steam trains to cars, planes, and high-speed rail","exactly the same","random changes"], answer:1},
     {q:"Which technology did NOT exist 100 years ago?", options:["A telephone","A telegraph","The internet and smartphones","A train"], answer:2},
     {q:"Schools 100 years ago in rural Ontario ___.", options:["had computers and internet","often had one room with students of all ages taught by one teacher","were exactly the same as today","only taught reading"], answer:1},
     {q:"What has stayed the same between Ontario communities 100 years ago and today?", options:["Technology","The basic need for shelter, food, community, and connection to others","Government structure","Exact same buildings"], answer:1}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"Language", title:"Spelling: Prefixes and Suffixes", summary:"Students learn how prefixes (un-, re-, pre-) and suffixes (-ful, -less, -ness) change a word's meaning. They build vocabulary by applying these patterns.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A prefix is added to the ___ of a base word.", options:["end","middle","beginning","random position"], answer:2},
     {q:"What does the prefix "un-" mean?", options:["Again","Before","Not or the opposite","After"], answer:2},
     {q:"What does "unhappy" mean?", options:["Very happy","Happy again","Not happy","About to be happy"], answer:2},
     {q:"A suffix is added to the ___ of a word.", options:["beginning","middle","end","random position"], answer:2},
     {q:"What does "careful" mean?", options:["Without care","Full of care","Before care","Not care"], answer:1}
   ]},
  {subject:"Math", title:"Data: Pictographs and Surveys", summary:"Students conduct simple surveys, organise data in a pictograph, and draw conclusions.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A pictograph uses ___ to represent data.", options:["only numbers","pictures or symbols to represent quantities","only bars","only lines"], answer:1},
     {q:"In a pictograph where each symbol = 2, four symbols represent ___.", options:["4","6","8","10"], answer:2},
     {q:"A survey collects ___.", options:["only written information","information by asking people questions","only numerical data","only test scores"], answer:1},
     {q:"Why do we represent data visually?", options:["It is not useful","Graphs and charts make it easier to compare, analyse, and communicate data","Only for younger students","Only for numbers"], answer:1},
     {q:"If 15 students prefer soccer and 9 prefer basketball, how many more prefer soccer?", options:["5","6","7","8"], answer:1}
   ]},
  {subject:"Science", title:"Properties of Light", summary:"Students explore reflection, refraction, and absorption of light, and how prisms separate white light into the visible spectrum.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A prism separates white light into ___.", options:["only two colours","radio waves","the colours of the visible spectrum (ROYGBIV)","sound waves"], answer:2},
     {q:"The colours of the visible spectrum in order are ___.", options:["Random","Red, Orange, Yellow, Green, Blue, Indigo, Violet","Blue, Green, Yellow, Orange, Red, Purple","Only three colours"], answer:1},
     {q:"An opaque object ___.", options:["lets all light through","lets some light through","does not let light through at all","produces its own light"], answer:2},
     {q:"A transparent object ___.", options:["blocks all light","lets most light pass through clearly","only lets some light through","produces light"], answer:1},
     {q:"A translucent object ___.", options:["blocks all light","lets all light through clearly","allows some light through but scatters it","produces light"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Making a Difference: Local Action", summary:"Students explore how individuals and groups make positive changes in their communities through volunteering, activism, and sustainable choices.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Volunteering means ___.", options:["being paid to work","freely giving your time to help others or the community","only cleaning up","only for adults"], answer:1},
     {q:"A community garden is an example of ___.", options:["a negative action","people working together to grow food and strengthen community bonds","only for farmers","a government project always"], answer:1},
     {q:"Young people can make a difference by ___.", options:["doing nothing","doing nothing until they are adults","raising awareness, organising fundraisers, or starting community projects","only voting"], answer:1},
     {q:"An example of environmental local action is ___.", options:["buying more products","participating in a neighbourhood clean-up or tree-planting event","watching documentaries","ignoring litter"], answer:1},
     {q:"Why does individual action matter?", options:["It does not","Each person's choices add up: individual actions collectively create significant change","Only large organisations matter","Only governments can make change"], answer:1}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"Language", title:"Book Report Writing", summary:"Students write a structured book report including: title and author, brief plot summary, favourite part, and a recommendation.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A book report begins with ___.", options:["your opinion only","the title, author, and genre of the book","only a summary","only a recommendation"], answer:1},
     {q:"A plot summary in a book report ___.", options:["spoils everything in detail","tells the main events without giving away the ending","only describes characters","is never included"], answer:1},
     {q:"In a book report, a recommendation is ___.", options:["a list of other books","a statement saying whether or not you think others should read the book and why","only a grade","only a summary"], answer:1},
     {q:"Why are book reports useful?", options:["They are not","They develop summarising, evaluation, and communication skills","Only for teachers","Only for long books"], answer:1},
     {q:"Which is NOT typically in a book report?", options:["Title and author","Personal opinion and recommendation","The author's full biography and childhood","A brief summary of the plot"], answer:2}
   ]},
  {subject:"Math", title:"Addition and Subtraction Review: 3-Digit Numbers", summary:"Students solve multi-step word problems using addition and subtraction of 3-digit numbers.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"345 + 278 = ?", options:["613","623","633","623"], answer:1},
     {q:"800 − 356 = ?", options:["444","454","344","454"], answer:0},
     {q:"A school has 425 students. 178 are in junior grades. How many in senior grades?", options:["247","247","257","237"], answer:0},
     {q:"642 + 189 = ?", options:["821","831","841","811"], answer:1},
     {q:"503 − 167 = ?", options:["336","346","326","356"], answer:0}
   ]},
  {subject:"Science", title:"Forces Review and Engineering Design", summary:"Students review forces and apply engineering design principles: identify a problem, brainstorm, design, build, test, and improve.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The engineering design process begins with ___.", options:["building immediately","identifying and defining the problem","testing the solution","evaluating results only"], answer:1},
     {q:"After brainstorming solutions you ___.", options:["stop the process","select the best design and build a prototype","start over","test without designing"], answer:1},
     {q:"Testing a prototype helps you ___.", options:["skip to the end","identify what works and what needs to be improved","guarantee the design is perfect","only look at it"], answer:1},
     {q:"A prototype is ___.", options:["the final, perfect product","an early model used to test a design concept","only a drawing","a computer simulation only"], answer:1},
     {q:"Why is the "improve" step important in engineering design?", options:["It is not","Real-world designs rarely work perfectly the first time; testing and improving leads to better solutions","Only for professional engineers","Only for complex machines"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ontario's Geography: Lakes and Rivers", summary:"Students identify Ontario's major lakes (Great Lakes) and rivers (Ottawa, St. Lawrence, Thames) and their importance.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which are the five Great Lakes?", options:["Superior, Huron, Michigan, Erie, Ontario","Superior, Huron, Ontario, Georgian, Erie","Superior, Michigan, Erie, Ontario, Simcoe","Superior, Huron, Erie, Ontario, Nipigon"], answer:0},
     {q:"The St. Lawrence River connects the Great Lakes to ___.", options:["the Arctic Ocean","Hudson Bay","the Atlantic Ocean","the Pacific Ocean"], answer:2},
     {q:"The Ottawa River forms part of the border between ___.", options:["Ontario and Manitoba","Ontario and Quebec","Quebec and New Brunswick","British Columbia and Alberta"], answer:1},
     {q:"Why are the Great Lakes important to Ontario?", options:["They are not","They provide fresh water, shipping routes, fishing, hydroelectric power, and recreation","Only for tourism","Only for the US side"], answer:1},
     {q:"The St. Lawrence Seaway allows ___.", options:["only small boats","ocean-going ships to travel from the Atlantic Ocean deep into the Great Lakes via the St. Lawrence River","only Canadian ships","only fishing boats"], answer:1}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"Language", title:"Writing: Letters (Formal and Informal)", summary:"Students learn to write friendly (informal) letters and formal letters. They practise letter format: greeting, body, and closing.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A friendly letter is written to ___.", options:["a company or official","someone you know personally","only government officials","only strangers"], answer:1},
     {q:"A formal letter is written to ___.", options:["a best friend","a family member","a company, official, or someone you don't know personally","only neighbours"], answer:2},
     {q:"All letters include ___.", options:["only a body","a greeting (salutation), a body, and a closing","only a closing","only a return address"], answer:1},
     {q:"In a friendly letter, the greeting might be ___.", options:["To Whom It May Concern,","Dear Sir or Madam,","Hey! or Dear [Name],","Only numbers"], answer:2},
     {q:"In a formal letter, the closing should be ___.", options:["Love,","See ya!","Sincerely, or Yours truly,","Only your name"], answer:2}
   ]},
  {subject:"Math", title:"Multiplication and Division: Word Problems", summary:"Students solve two-step word problems using multiplication and division.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"There are 4 boxes with 12 crayons each. How many crayons in all?", options:["40","44","48","52"], answer:2},
     {q:"A bag has 24 apples divided equally into 6 boxes. How many apples per box?", options:["3","4","5","6"], answer:1},
     {q:"Each of 7 shelves has 9 books. How many books are there?", options:["54","56","63","72"], answer:2},
     {q:"56 children are split into equal teams of 7. How many teams?", options:["6","7","8","9"], answer:2},
     {q:"You buy 5 notebooks at $3 each and spend $15 in total. If you paid $20, how much change do you get?", options:["$3","$5","$6","$7"], answer:1}
   ]},
  {subject:"Science", title:"Properties of Soil Review and Composting", summary:"Students revisit soil types and learn about composting as a way to enrich soil and reduce organic waste.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Composting is ___.", options:["burning organic waste","the decomposition of organic waste (food scraps, leaves) into nutrient-rich material for soil","only for farms","mixing soil with plastic"], answer:1},
     {q:"What goes in a compost bin?", options:["Metal and plastic","Fruit and vegetable scraps, leaves, and paper","Only grass clippings","Old electronics"], answer:1},
     {q:"Compost improves soil by ___.", options:["making it wetter always","adding nutrients and improving drainage and structure","making it acidic only","only changing colour"], answer:1},
     {q:"Earthworms help composting by ___.", options:["eating the metal","breaking down organic matter and aerating the soil as they move through it","creating chemical reactions","only moving soil"], answer:1},
     {q:"Why is composting good for the environment?", options:["It is not","It reduces organic waste in landfills and creates valuable fertiliser for gardens","Only for farmers","Only if you have a garden"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Canadian Charter of Rights and Freedoms", summary:"Students learn about the Charter (1982) and key rights it protects: fundamental freedoms, democratic rights, equality rights.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The Canadian Charter of Rights and Freedoms was signed in ___.", options:["1867","1945","1965","1982"], answer:3},
     {q:"Which freedom is protected by the Charter?", options:["Freedom to break laws","Freedom of expression (speech, writing, art)","Freedom from all taxes","Freedom to ignore others' rights"], answer:1},
     {q:"Equality rights in the Charter mean ___.", options:["only men have equal rights","only citizens have equal rights","all people in Canada are equal under the law regardless of race, sex, age, or disability","only adults"], answer:2},
     {q:"Democratic rights in the Charter include ___.", options:["the right to own any property","the right of citizens to vote in elections","the right to free housing","the right to drive"], answer:1},
     {q:"Why is the Charter important?", options:["It is not","It is the supreme law that protects individual rights and limits what the government can do to people","Only for lawyers","Only for politicians"], answer:1}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"Language", title:"Reading Long Texts: Chapter Books", summary:"Students develop strategies for reading longer texts: using chapter titles, making predictions, tracking characters and plot, and taking notes.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Before reading a chapter, reading the chapter title helps you ___.", options:["predict what the chapter will be about and activate relevant prior knowledge","skip the chapter","write the ending","only look at pictures"], answer:0},
     {q:"Tracking character changes throughout a chapter book means ___.", options:["memorising every word","noting how a character grows, changes, or faces challenges as the story progresses","only listing characters","ignoring the plot"], answer:1},
     {q:"When you lose track of a chapter book, you should ___.", options:["start from the beginning every time","reread the last few pages or a chapter summary to reorient yourself","stop reading","skip ahead"], answer:1},
     {q:"Taking reading notes helps you ___.", options:["forget the text","remember key events, characters, and ideas for discussion or assignments","write more words","read faster"], answer:1},
     {q:"Why is reading chapter books important?", options:["It is not","It develops vocabulary, attention span, comprehension, and a love of literature","Only for gifted readers","Only for older students"], answer:1}
   ]},
  {subject:"Math", title:"Review: All Strands", summary:"Students review and consolidate key Grade 3 math concepts: number sense, measurement, geometry, patterning, and data.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"256 + 399 = ?", options:["645","655","665","675"], answer:1},
     {q:"7 × 9 = ?", options:["56","63","72","81"], answer:1},
     {q:"Find the area of a 6×7 rectangle.", options:["13 sq units","36 sq units","42 sq units","48 sq units"], answer:2},
     {q:"Which fraction is equivalent to 1/2?", options:["2/3","3/6","2/5","1/3"], answer:1},
     {q:"Which event is certain?", options:["Rolling a 7 on a 6-sided die","Drawing a red card from a deck with only blue cards","Getting either heads or tails on a coin flip","It raining on a sunny day"], answer:2}
   ]},
  {subject:"Science", title:"Science Year Review", summary:"Students review all Grade 3 science strands: growth and changes in animals, soils, forces, and structures.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"The four stages of complete metamorphosis are ___.", options:["egg, larva, pupa, adult","egg, nymph, adult, elder","birth, growth, reproduction, death","seed, sprout, plant, fruit"], answer:0},
     {q:"Which soil is best for most plant growth?", options:["Sand","Clay","Loam","Gravel"], answer:1},
     {q:"A simple machine makes work ___.", options:["harder","impossible","easier by reducing force or changing direction","more expensive"], answer:2},
     {q:"Which is NOT a simple machine?", options:["A lever","An inclined plane","A computer","A pulley"], answer:2},
     {q:"Friction is a force that ___.", options:["pulls objects toward Earth","is the same as gravity","resists the motion of objects sliding over surfaces","always helps motion"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Social Studies Year Review", summary:"Students review Ontario communities, government, economy, natural resources, and citizenship.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Which level of government runs local parks and garbage collection?", options:["Federal","Provincial","Municipal","International"], answer:2},
     {q:"What are Ontario's two major physical regions?", options:["Desert and rainforest","Canadian Shield and Great Lakes–St. Lawrence Lowlands","Prairies and mountains","Ocean coast and tundra"], answer:1},
     {q:"What does "sustainable" use of resources mean?", options:["Use as fast as possible","Only use renewable resources","Use resources in a way that preserves them for future generations","Never use any resources"], answer:2},
     {q:"Confederation took place in ___.", options:["1776","1812","1867","1982"], answer:2},
     {q:"A responsible citizen in Canada ___.", options:["ignores community needs","follows laws, pays taxes, participates, and contributes to the community","only votes","only obeys rules they like"], answer:1}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"Language", title:"Creative Writing: Narrative Revision", summary:"Students revise a narrative draft by improving word choice, adding sensory details, varying sentence structure, and ensuring the story makes sense.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Revising a piece of writing means ___.", options:["correcting only spelling errors","checking and improving content, organization, word choice, and style","rewriting the whole text from scratch","only fixing punctuation"], answer:1},
     {q:"Sensory details appeal to the ___.", options:["only visual sense","five senses (sight, sound, smell, taste, touch)","only hearing","only imagination"], answer:1},
     {q:"Varying sentence length means ___.", options:["making all sentences the same length","sometimes writing short, punchy sentences and sometimes longer, more descriptive ones","only writing long sentences","only writing short sentences"], answer:1},
     {q:"Strong verbs like "sprinted" and "whispered" are better than "ran" and "said" because ___.", options:["they are longer","they add more precise, vivid meaning and make the writing more engaging","they are always correct","they use more punctuation"], answer:1},
     {q:"After revising for content, you should ___ your writing.", options:["stop working","edit/proofread for spelling, grammar, and punctuation errors","rewrite entirely","submit immediately"], answer:1}
   ]},
  {subject:"Math", title:"Financial Literacy: Saving and Spending", summary:"Students learn the basics of saving, spending, and the concept of earning money through work.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Saving money means ___.", options:["spending everything you earn","setting aside money to use later for a goal or emergency","only putting money in a bank","only for adults"], answer:1},
     {q:"The difference between a need and a want is ___.", options:["they are the same","needs are necessary for survival; wants are extras we desire","wants are more important","needs are optional"], answer:1},
     {q:"If you earn $10 and spend $6, how much can you save?", options:["$3","$4","$6","$2"], answer:1},
     {q:"A simple budget helps you ___.", options:["spend all your money immediately","track income and expenses to ensure you live within your means","only save money","only spend money"], answer:1},
     {q:"Why is it good to save some of your money?", options:["It is not","Savings give you a financial cushion for emergencies and future goals","Only for adults","You should spend everything to enjoy life"], answer:1}
   ]},
  {subject:"Science", title:"Environmental Science: Climate and Ecosystems", summary:"Students explore how climate affects ecosystems, and how climate change is altering habitats and biodiversity globally and in Ontario.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Climate is ___.", options:["today's weather","the average weather patterns of a region over a long period","only temperature","only rainfall"], answer:1},
     {q:"Climate change is causing ___.", options:["no changes","more extreme weather events, rising temperatures, melting ice, and shifting seasons globally","only ocean changes","only desert expansion"], answer:1},
     {q:"How does climate change affect Ontario wildlife?", options:["It does not","Warmer temperatures shift the ranges of many species, affecting when birds migrate, when plants bloom, and which species survive","Only for tropical animals","Only for marine animals"], answer:1},
     {q:"Which gas is a major contributor to climate change?", options:["Nitrogen","Oxygen","Carbon dioxide (CO₂) from burning fossil fuels","Helium"], answer:2},
     {q:"One way to reduce carbon emissions is to ___.", options:["use more fossil fuels","burn more forests","use renewable energy, reduce waste, and drive less","plant more lawns only"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Looking Forward: My Community in 2050", summary:"Students use their learning to imagine what their community might look like in 2050 given current trends in technology, population, and environment.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"In 2050, Ontario's population will likely ___.", options:["shrink to zero","grow, requiring more housing, services, and infrastructure","stay exactly the same","move to the Moon"], answer:1},
     {q:"Technology in 2050 might help communities by ___.", options:["causing more problems","solving challenges like clean energy, efficient transportation, and better health care","doing nothing new","only creating entertainment"], answer:1},
     {q:"Environmental challenges in 2050 will likely include ___.", options:["no challenges","effects of climate change such as more extreme weather, changed habitats, and pressure on water resources","nothing new","only space issues"], answer:1},
     {q:"What can students today do to help the communities of 2050?", options:["Nothing","Learn, innovate, make sustainable choices, and be active citizens committed to a better future","Only wait","Only vote when older"], answer:1},
     {q:"The most important lesson from Grade 3 Social Studies is ___.", options:["memorising province names","Communities are connected through geography, history, people, and shared responsibilities","Only facts about Ontario","Only about government"], answer:1}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"Language", title:"Year End Celebration: Favourite Books and Reading Reflections", summary:"Students share favourite books, reflect on their reading growth, and set reading goals for Grade 4.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"Reflecting on your reading means ___.", options:["forgetting everything","thinking about how your skills and enjoyment of reading have grown throughout the year","copying a book report","only choosing new books"], answer:1},
     {q:"A reading goal for Grade 4 might be ___.", options:["never reading again","trying a new genre, reading longer books, or reading a set number of books","only reading the same books","giving up on hard books"], answer:1},
     {q:"Why is reading important beyond school?", options:["It is not","Reading develops vocabulary, knowledge, empathy, and lifelong learning skills","Only for school marks","Only for English class"], answer:1},
     {q:"What is one thing you enjoyed about reading this year?", options:["Nothing","Discovering a new favourite genre, author, or story that made me think or feel something new","Only tests","Only grammar"], answer:1},
     {q:"A book recommendation should include ___.", options:["only the title","the title, author, what you loved about it, and who you think would enjoy it","only your name","only a grade out of ten"], answer:1}
   ]},
  {subject:"Math", title:"Grade 3 Math Celebration: Challenge Problems", summary:"Students tackle fun, mixed challenge problems drawing on all Grade 3 math concepts.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A rectangle has a perimeter of 28 cm and a length of 9 cm. What is its width?", options:["4 cm","5 cm","6 cm","7 cm"], answer:1},
     {q:"If 8 students each have 7 stickers and share equally in 4 groups, how many stickers per group?", options:["12","14","16","18"], answer:1},
     {q:"A bag has 30 apples. 1/3 are red. How many red apples?", options:["5","10","12","15"], answer:1},
     {q:"What is 485 + 367?", options:["842","852","862","872"], answer:1},
     {q:"A square field has an area of 81 m². What is each side length?", options:["7 m","8 m","9 m","10 m"], answer:2}
   ]},
  {subject:"Science", title:"Grade 3 Science Celebration: Science All Around Us", summary:"Students connect science learning to everyday life and explore how curiosity and observation drive scientific discovery.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"A simple machine that helps you open a paint can lid with a coin is a ___.", options:["pulley","wheel-and-axle","lever","inclined plane"], answer:2},
     {q:"Which soil type is best for growing vegetables?", options:["Clay","Sand","Gravel","Loam"], answer:3},
     {q:"An eagle is a secondary consumer. What does it most likely eat?", options:["Only plants","Only soil","Smaller animals like fish, rabbits, and other birds","Only fungi"], answer:2},
     {q:"Renewable energy sources include ___.", options:["coal and oil","natural gas and propane","solar, wind, and hydroelectric power","only nuclear power"], answer:2},
     {q:"The engineering design process helps people ___.", options:["give up easily","solve real problems by designing, testing, and improving their ideas","only build bridges","only for space programs"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Grade 3 Social Studies Celebration: Our Community, Our World", summary:"Students celebrate their learning by connecting Ontario communities to communities around the world and to the future.",
   resourceLabel:"TVO Learn: Grade 3", resourceUrl:"https://tvolearn.com/pages/grade-3",
   quiz:[
     {q:"What do all communities around the world have in common?", options:["Exact same food","Same language","Same government","People working together to meet basic needs and live good lives"], answer:3},
     {q:"How is Ontario connected to communities around the world?", options:["It is not","Through trade, immigration, cultural exchange, international agreements, and shared global challenges","Only through geography","Only through the internet"], answer:1},
     {q:"What makes a community strong?", options:["Only money","Cooperation, respect, diversity, shared responsibility, and a sense of belonging","Only large buildings","Only famous people"], answer:1},
     {q:"What is one thing you can do to make your community better?", options:["Nothing","Be kind, participate, volunteer, make sustainable choices, and treat everyone with respect","Only vote at 18","Only pay taxes"], answer:1},
     {q:"The most important thing I learned in Grade 3 Social Studies is ___.", options:["Nothing was important","Communities are built by people working together and respecting each other, the land, and the future","Only province names","Only about the government"], answer:1}
   ]},
]},
];

export default curriculum;