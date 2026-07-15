import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"Language", title:"Parts of Speech", summary:"Grade 4 Language strand: nouns name people/places/things, verbs show actions, adjectives describe nouns, adverbs describe verbs.",
   resourceLabel:"YouTube: Parts of Speech", resourceUrl:"https://www.youtube.com/results?search_query=Parts%20of%20Speech%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ZqLeGm4k6CU",
   quiz:[
     {q:"A noun names a person, place, or ___.", options:["conjunction","thing","description","action"], answer:1},
     {q:"Which word is a verb in: The quick dog ran?", options:["ran","quick","The","dog"], answer:0},
     {q:"Which is an adjective?", options:["happy","run","eat","slowly"], answer:0},
     {q:"Adverbs often tell ___ about a verb.", options:["what kind","size","how/when/where","colour"], answer:2},
     {q:"Which is an adverb?", options:["house","dog","quickly","blue"], answer:2}
   ]},
  {subject:"Math", title:"Multiplication Facts to 10×10", summary:"Grade 4 Number strand: students recall multiplication facts to 10×10 fluently and use them to solve problems.",
   resourceLabel:"YouTube: Multiplication Facts to 10×10", resourceUrl:"https://www.youtube.com/results?search_query=Multiplication%20Facts%20to%2010%C3%9710%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=6owKqFWej-w",
   quiz:[
     {q:"7 × 8 = ?", options:["54","48","56","64"], answer:2},
     {q:"6 × 9 = ?", options:["48","56","54","63"], answer:2},
     {q:"4 × 7 = ?", options:["28","32","24","21"], answer:0},
     {q:"9 × 9 = ?", options:["72","80","90","81"], answer:3},
     {q:"8 × 6 = ?", options:["54","46","48","42"], answer:2}
   ]},
  {subject:"Science", title:"Habitats and Communities", summary:"Grade 4 Science Life Systems strand: a habitat is where organisms live; a community is all the organisms sharing a habitat and interacting.",
   resourceLabel:"YouTube: Habitats and Communities", resourceUrl:"https://www.youtube.com/results?search_query=Habitats%20and%20Communities%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=p3PX1x6scbA",
   quiz:[
     {q:"A habitat provides food, water, shelter, and ___.", options:["space","money","electricity","television"], answer:0},
     {q:"A community includes ___.", options:["only predators","all living things in an area","only plants","only animals"], answer:1},
     {q:"Which is a freshwater habitat?", options:["Desert","Ocean","Tundra","Pond"], answer:3},
     {q:"Organisms in a community ___.", options:["eat only plants","never interact","depend on and interact with each other","live separately"], answer:2},
     {q:"A forest habitat includes trees, soil, water, and ___.", options:["roads","factories","buildings","animals and plants that live there"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Ancient Civilizations Overview", summary:"Grade 4 Social Studies Heritage strand: ancient civilizations developed organized societies with government, art, writing, and technology.",
   resourceLabel:"YouTube: Ancient Civilizations Overview", resourceUrl:"https://www.youtube.com/results?search_query=Ancient%20Civilizations%20Overview%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Kepp9g9Ccqk",
   quiz:[
     {q:"An ancient civilization is ___.", options:["a modern city","a type of government","a geography term","a society from thousands of years ago"], answer:3},
     {q:"Which of these is NOT an ancient civilization?", options:["Egypt","Canada (modern)","Rome","Greece"], answer:1},
     {q:"Ancient civilizations contributed ___.", options:["writing and government","only myths and legends","only farming","nothing to modern life"], answer:0},
     {q:"What is archaeology?", options:["The study of stars","A type of government","Studying history through artifacts","The study of rocks"], answer:2},
     {q:"Why do we study ancient civilizations?", options:["Only for fun","Only for geography","We do not","To learn how societies developed"], answer:3}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"Language", title:"Sentence Types", summary:"Grade 4 Language strand: the four sentence types are declarative (statement), interrogative (question), imperative (command), and exclamatory.",
   resourceLabel:"YouTube: Sentence Types", resourceUrl:"https://www.youtube.com/results?search_query=Sentence%20Types%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=WYnpf44ojFU",
   quiz:[
     {q:"A declarative sentence ___.", options:["gives a command","makes a statement","asks a question","shows surprise"], answer:1},
     {q:"An interrogative sentence ends with a ___.", options:["exclamation mark","comma","question mark","period"], answer:2},
     {q:"An imperative sentence gives a ___.", options:["question","fact","command or request","strong feeling"], answer:2},
     {q:"An exclamatory sentence expresses ___.", options:["a command","strong emotion","a fact","a question"], answer:1},
     {q:"'Close the door!' is a ___ sentence.", options:["exclamatory","declarative","imperative","interrogative"], answer:2}
   ]},
  {subject:"Math", title:"Division Basics", summary:"Grade 4 Number strand: division is sharing equally or grouping. Students divide with dividends to 100 using multiplication facts.",
   resourceLabel:"YouTube: Division Basics", resourceUrl:"https://www.youtube.com/results?search_query=Division%20Basics%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2-sP854NMLw",
   quiz:[
     {q:"35 ÷ 7 = ?", options:["4","6","5","7"], answer:2},
     {q:"48 ÷ 6 = ?", options:["6","7","8","9"], answer:2},
     {q:"Division is the inverse (opposite) of ___.", options:["addition","fractions","subtraction","multiplication"], answer:3},
     {q:"63 ÷ 9 = ?", options:["7","9","6","8"], answer:0},
     {q:"If 8 × 7 = 56, then 56 ÷ 8 = ?", options:["9","8","6","7"], answer:3}
   ]},
  {subject:"Science", title:"Food Chains and Webs", summary:"Grade 4 Science Life Systems: a food chain shows energy flow from producer to consumer. A food web shows interconnected food chains.",
   resourceLabel:"YouTube: Food Chains and Webs", resourceUrl:"https://www.youtube.com/results?search_query=Food%20Chains%20and%20Webs%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ZbqCDUOygXg",
   quiz:[
     {q:"Producers in a food chain are ___.", options:["animals that eat plants","carnivores","plants that make their own food","decomposers"], answer:2},
     {q:"A herbivore is an animal that eats ___.", options:["only meat","nothing","both plants and meat","only plants"], answer:3},
     {q:"In a food web, arrows show ___.", options:["movement","the direction energy flows","friendship","habitat"], answer:1},
     {q:"What happens if one species in a food web disappears?", options:["Nothing changes","Only prey notice","Only predators notice","Other connected species are affected"], answer:3},
     {q:"A decomposer ___.", options:["eats only animals","makes its own food","breaks down dead matter","eats only plants"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Ancient Egypt", summary:"Grade 4 Social Studies: Ancient Egypt flourished along the Nile River, developing writing (hieroglyphics), monumental architecture, and complex government.",
   resourceLabel:"YouTube: Ancient Egypt", resourceUrl:"https://www.youtube.com/results?search_query=Ancient%20Egypt%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zYxC14pCaJ0",
   quiz:[
     {q:"Ancient Egypt was located in ___.", options:["Africa","Europe","Asia","South America"], answer:0},
     {q:"The Nile River was important because ___.", options:["it had gold","it provided soil and water for farming","it was the longest river","it separated Egypt from enemies"], answer:1},
     {q:"Egyptian hieroglyphics were ___.", options:["a writing system using pictures","a religious ceremony","a form of mathematics","a type of building"], answer:0},
     {q:"The pyramids were built as ___.", options:["storage facilities","tombs for pharaohs","palaces for living pharaohs","temples for worship only"], answer:1},
     {q:"Who ruled Ancient Egypt?", options:["A pharaoh (king/queen)","A president","A group of priests","An elected prime minister"], answer:0}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"Language", title:"Synonyms and Antonyms", summary:"Grade 4 Language strand: synonyms are words with similar meanings; antonyms have opposite meanings. Using them enriches vocabulary and writing.",
   resourceLabel:"YouTube: Synonyms and Antonyms", resourceUrl:"https://www.youtube.com/results?search_query=Synonyms%20and%20Antonyms%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PDI2xlOBcM4",
   quiz:[
     {q:"A synonym for 'happy' is ___.", options:["joyful","angry","sad","tired"], answer:0},
     {q:"An antonym for 'ancient' is ___.", options:["historic","modern","past","old"], answer:1},
     {q:"Which pair are synonyms?", options:["big/large","fast/slow","night/day","hot/cold"], answer:0},
     {q:"Which pair are antonyms?", options:["quick/fast","bright/dim","small/tiny","glad/happy"], answer:1},
     {q:"Using synonyms in writing helps to ___.", options:["shorten writing","avoid repetition and add variety","change the topic","confuse the reader"], answer:1}
   ]},
  {subject:"Math", title:"2-Digit × 1-Digit Multiplication", summary:"Grade 4 Number strand: multiply 2-digit numbers by 1-digit numbers using the distributive property and place value.",
   resourceLabel:"YouTube: 2-Digit × 1-Digit Multiplication", resourceUrl:"https://www.youtube.com/results?search_query=2-Digit%20%C3%97%201-Digit%20Multiplication%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=6owKqFWej-w",
   quiz:[
     {q:"23 × 4 = ?", options:["92","72","102","82"], answer:0},
     {q:"45 × 3 = ?", options:["115","135","125","145"], answer:1},
     {q:"67 × 2 = ?", options:["144","134","114","124"], answer:1},
     {q:"To solve 34 × 5, you can think 30×5 + 4×5 = ?", options:["170","160","150","180"], answer:0},
     {q:"Which is correct: 58 × 3 = ?", options:["184","164","154","174"], answer:3}
   ]},
  {subject:"Science", title:"Adaptations", summary:"Grade 4 Science Life Systems: adaptations are physical or behavioural features that help organisms survive in their habitat.",
   resourceLabel:"YouTube: Adaptations", resourceUrl:"https://www.youtube.com/results?search_query=Adaptations%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=QVyOrRDsD38",
   quiz:[
     {q:"An adaptation is ___.", options:["a feature that helps an organism survive","a food chain stage","a type of habitat","a community interaction"], answer:0},
     {q:"A polar bear's white fur is an adaptation that helps it ___.", options:["stay warmer in summer","swim faster","camouflage in snowy environments","attract mates"], answer:2},
     {q:"A cactus stores water in its thick stem as an adaptation to ___.", options:["cold climates","rainy environments","desert environments with little rain","forest life"], answer:2},
     {q:"Which is a behavioural adaptation?", options:["Bird's hollow bones","Birds migrating south in winter","Duck's webbed feet","Fish gills"], answer:1},
     {q:"Camouflage is an adaptation that helps animals ___.", options:["stay hidden from predators or prey","find water","run faster","digest food better"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Ancient Greece", summary:"Grade 4 Social Studies: Ancient Greece developed democracy, philosophy, the Olympics, and architecture that influenced the Western world.",
   resourceLabel:"YouTube: Ancient Greece", resourceUrl:"https://www.youtube.com/results?search_query=Ancient%20Greece%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=RchSJSJAbc0",
   quiz:[
     {q:"Ancient Greece was located in ___.", options:["North America","Asia","Africa","Southern Europe"], answer:3},
     {q:"Democracy was developed in ___.", options:["Ancient Egypt","Ancient China","Ancient Rome","Ancient Greece (Athens)"], answer:3},
     {q:"The Olympic Games began in ___.", options:["Greece","China","Egypt","Rome"], answer:0},
     {q:"Greek philosophers like Socrates were known for ___.", options:["writing hieroglyphics","building pyramids","fighting wars only","asking deep questions about life"], answer:3},
     {q:"Ancient Greek architecture featured ___.", options:["underground cities","mud brick walls","columns and temples like the Parthenon","igloos"], answer:2}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"Language", title:"Prefixes and Suffixes", summary:"Grade 4 Language strand: a prefix is added before a root word to change its meaning; a suffix is added after. Examples: un-, re-, -ful, -less.",
   resourceLabel:"YouTube: Prefixes and Suffixes", resourceUrl:"https://www.youtube.com/results?search_query=Prefixes%20and%20Suffixes%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=yRwmr7CqnrY",
   quiz:[
     {q:"What does the prefix 'un-' mean?", options:["again","before","after","not"], answer:3},
     {q:"What does 'unhappy' mean?", options:["before happy","happy again","very happy","not happy"], answer:3},
     {q:"What does the suffix '-ful' mean?", options:["full of","without","before","again"], answer:0},
     {q:"Which word means 'without hope'?", options:["hopeless","hopeful","rehope","hopefully"], answer:0},
     {q:"What does 'redo' mean?", options:["not do","do again","do before","do after"], answer:1}
   ]},
  {subject:"Math", title:"Introduction to Long Division", summary:"Grade 4 Number strand: students divide 2-digit dividends by 1-digit divisors, understanding quotient and remainder.",
   resourceLabel:"YouTube: Introduction to Long Division", resourceUrl:"https://www.youtube.com/results?search_query=Introduction%20to%20Long%20Division%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2-sP854NMLw",
   quiz:[
     {q:"In division, the number being divided is the ___.", options:["dividend","divisor","quotient","remainder"], answer:0},
     {q:"In division, the number dividing is the ___.", options:["dividend","remainder","divisor","quotient"], answer:2},
     {q:"27 ÷ 4 = 6 remainder ___.", options:["4","2","3","1"], answer:2},
     {q:"37 ÷ 5 = ?", options:["7 r2","7 r3","8 r1","6 r7"], answer:0},
     {q:"A remainder in division is ___.", options:["the divisor","the answer","how many are left over","the quotient"], answer:2}
   ]},
  {subject:"Science", title:"Biodiversity", summary:"Grade 4 Science Life Systems: biodiversity means the variety of living organisms in an ecosystem. Greater biodiversity usually means a healthier ecosystem.",
   resourceLabel:"YouTube: Biodiversity", resourceUrl:"https://www.youtube.com/results?search_query=Biodiversity%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=rVZktiOxsww",
   quiz:[
     {q:"Biodiversity means ___.", options:["the size of an ecosystem","the number of plants only","the variety of living organisms in an area","only one type of organism"], answer:2},
     {q:"Greater biodiversity usually means ___.", options:["a healthier, more stable ecosystem","only large animals","a less stable ecosystem","fewer species"], answer:0},
     {q:"Which habitat has the greatest biodiversity?", options:["A single-crop farm","An empty field","A parking lot","A tropical rainforest"], answer:3},
     {q:"How does biodiversity benefit humans?", options:["It provides food and medicine","Only animals benefit","Only scientists benefit","It does not"], answer:0},
     {q:"What threatens biodiversity?", options:["More trees","Habitat loss","Clean water","Too much rain"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ancient Rome", summary:"Grade 4 Social Studies: Ancient Rome built a vast empire, developing law, engineering, and governance that influenced modern Western civilization.",
   resourceLabel:"YouTube: Ancient Rome", resourceUrl:"https://www.youtube.com/results?search_query=Ancient%20Rome%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Wo0KujQEJ_s",
   quiz:[
     {q:"Ancient Rome was centred in what is now ___.", options:["Spain","Greece","France","Italy"], answer:3},
     {q:"The Roman Republic had a system of ___.", options:["complete democracy","absolute monarchy","religious rule","representative government with a Senate"], answer:3},
     {q:"Roman engineering achievements include ___.", options:["roads, aqueducts, and the arch","hieroglyphics","the Great Wall","pyramids"], answer:0},
     {q:"The Roman Empire fell in ___.", options:["100 AD","476 AD","1492 AD","1066 AD"], answer:1},
     {q:"What is one way ancient Rome influences us today?", options:["Greek food","Latin words in English","Egyptian architecture","No influence"], answer:1}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"Language", title:"Reading: Main Idea and Supporting Details", summary:"Grade 4 Reading strand: the main idea is what a text is mostly about. Supporting details give more information and evidence for the main idea.",
   resourceLabel:"YouTube: Reading: Main Idea and Supporting Details", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Main%20Idea%20and%20Supporting%20Details%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=F6wvArMBZIo",
   quiz:[
     {q:"The main idea is ___.", options:["the last sentence","what the entire text is mostly about","a small detail","the topic sentence only"], answer:1},
     {q:"Supporting details ___.", options:["explain or prove the main idea","are unrelated to the main idea","are always at the beginning","are more important than the main idea"], answer:0},
     {q:"Where is the main idea often found?", options:["In a caption","Only in the middle","First or last sentence","Only at the end"], answer:2},
     {q:"How do you identify the main idea?", options:["Count the paragraphs","Read only the title","Read only the last line","Ask 'What is this MOSTLY about?'"], answer:3},
     {q:"Which is a main idea sentence?", options:["She walked to the store.","The cat was orange.","He ate lunch at noon.","Recycling helps the environment."], answer:3}
   ]},
  {subject:"Math", title:"Fractions: Equal Parts", summary:"Grade 4 Number strand: a fraction represents equal parts of a whole. The numerator shows how many parts are selected; the denominator shows total equal parts.",
   resourceLabel:"YouTube: Fractions: Equal Parts", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%3A%20Equal%20Parts%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=362JVVvgYPE",
   quiz:[
     {q:"In the fraction 3/4, the denominator is ___.", options:["1","7","4","3"], answer:2},
     {q:"In the fraction 3/4, the numerator is ___.", options:["7","1","4","3"], answer:3},
     {q:"Which fraction represents half?", options:["1/2","1/3","2/3","1/4"], answer:0},
     {q:"A pizza is cut into 8 equal slices. You eat 3. What fraction did you eat?", options:["3/5","3/8","5/8","8/3"], answer:1},
     {q:"The denominator in a fraction tells you ___.", options:["whether the fraction is big","the size of each part","the total number of equal parts","how many parts you have"], answer:2}
   ]},
  {subject:"Science", title:"Human Impact on Ecosystems", summary:"Grade 4 Science Life Systems: human activities such as deforestation, pollution, and urbanization negatively affect ecosystems; conservation actions help protect them.",
   resourceLabel:"YouTube: Human Impact on Ecosystems", resourceUrl:"https://www.youtube.com/results?search_query=Human%20Impact%20on%20Ecosystems%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Um-bo2MWDsQ",
   quiz:[
     {q:"Which human activity HARMS ecosystems?", options:["Composting","Dumping waste in rivers","Creating nature reserves","Planting trees"], answer:1},
     {q:"Deforestation means ___.", options:["studying forests","planting forests","protecting forests","cutting down forests"], answer:3},
     {q:"Which action helps PROTECT ecosystems?", options:["Littering","Building factories near rivers","Polluting water","Creating national parks"], answer:3},
     {q:"How does pollution affect wildlife?", options:["Only fish are affected","Only birds are affected","It destroys habitats and harms organisms","It helps wildlife"], answer:2},
     {q:"What can individuals do to reduce environmental impact?", options:["Drive more cars","Cut down more trees","Use more plastic","Reduce, reuse, and recycle"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Indigenous Peoples of North America", summary:"Grade 4 Social Studies: Indigenous peoples of North America include many diverse nations, each with unique cultures, languages, and governance systems.",
   resourceLabel:"YouTube: Indigenous Peoples of North America", resourceUrl:"https://www.youtube.com/results?search_query=Indigenous%20Peoples%20of%20North%20America%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=YqU9kKEgJag",
   quiz:[
     {q:"Indigenous peoples of North America ___.", options:["all speak the same language","have lived here for thousands of years","are a single unified group","arrived recently"], answer:1},
     {q:"There are ___ Indigenous cultures in North America.", options:["only 5","only 1","only 2 or 3","many hundreds of diverse nations"], answer:3},
     {q:"Traditional Indigenous knowledge includes ___.", options:["only dance","many different things","only language","only crafts"], answer:1},
     {q:"Why is it important to learn about Indigenous cultures?", options:["It is not important","They shape Canada's identity","Only for adults","Only in Ontario"], answer:1},
     {q:"The Indian Act (1876) was ___.", options:["a law restricting Indigenous rights","a celebration of Indigenous cultures","a trade agreement","A school curriculum"], answer:0}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"Language", title:"Reading: Inference", summary:"Grade 4 Reading strand: inference means using evidence from the text plus your own knowledge to understand something not directly stated.",
   resourceLabel:"YouTube: Reading: Inference", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Inference%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=JdaD2FZQFEY",
   quiz:[
     {q:"An inference is ___.", options:["the main idea","a conclusion from clues and knowledge","directly stated in the text","a guess with no evidence"], answer:1},
     {q:"What clues help you make an inference?", options:["The book cover only","Only pictures","Random guessing","Text evidence plus what you already know"], answer:3},
     {q:"Maria grabbed her umbrella before leaving. You can infer ___.", options:["She forgot her coat","She likes umbrellas","She is going swimming","It was probably raining"], answer:3},
     {q:"The book's cover shows a spaceship. You can infer the story is about ___.", options:["History","Farming","Cooking","Space/science fiction"], answer:3},
     {q:"After making an inference, a good reader ___.", options:["Reads on to check the inference","Ignores it","Stops reading","Tells others"], answer:0}
   ]},
  {subject:"Math", title:"Comparing Fractions", summary:"Grade 4 Number strand: to compare fractions with the same denominator, compare numerators. To compare different denominators, find equivalent fractions.",
   resourceLabel:"YouTube: Comparing Fractions", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Fractions%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=KNdUJQ_qd4U",
   quiz:[
     {q:"Which is greater: 3/5 or 1/5?", options:["1/5","Equal","Cannot tell","3/5"], answer:3},
     {q:"Which fraction is closest to 1 (whole)?", options:["0/4","3/4","1/4","2/4"], answer:1},
     {q:"1/2 is ___ 1/4.", options:["equal to","not comparable to","less than","greater than"], answer:3},
     {q:"Order from least to greatest: 3/8, 1/8, 7/8", options:["7/8, 3/8, 1/8","3/8, 1/8, 7/8","1/8, 7/8, 3/8","1/8, 3/8, 7/8"], answer:3},
     {q:"Which is the largest fraction?", options:["1/3","5/6","2/3","1/6"], answer:1}
   ]},
  {subject:"Science", title:"Rocks and Minerals", summary:"Grade 4 Science Earth strand: rocks are made of minerals. The three rock types are igneous, sedimentary, and metamorphic, each formed by different processes.",
   resourceLabel:"YouTube: Rocks and Minerals", resourceUrl:"https://www.youtube.com/results?search_query=Rocks%20and%20Minerals%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=XvVvfPnrhd0",
   quiz:[
     {q:"The three types of rocks are igneous, sedimentary, and ___.", options:["metamorphic","fossil","volcanic","crystal"], answer:0},
     {q:"Igneous rock forms from ___.", options:["cooled magma or lava","compressed sediment","plant material","other rocks under pressure"], answer:0},
     {q:"Sedimentary rock forms from ___.", options:["magma","only volcanic activity","layers of sediment compressed over time","magma and pressure"], answer:2},
     {q:"Metamorphic rock forms when ___.", options:["lava cools","sediment is compressed","glaciers melt","rock changed by heat and pressure"], answer:3},
     {q:"Fossils are most often found in ___.", options:["sedimentary rock","granite","metamorphic rock","igneous rock"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Early Canadian History", summary:"Grade 4 Social Studies: Canada's early history includes Indigenous peoples, European exploration, New France, and British colonization.",
   resourceLabel:"YouTube: Early Canadian History", resourceUrl:"https://www.youtube.com/results?search_query=Early%20Canadian%20History%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zz440EuFK8Q",
   quiz:[
     {q:"Who were the first people to live in what is now Canada?", options:["Indigenous peoples","American explorers","British settlers","French settlers"], answer:0},
     {q:"New France was a colony established by ___.", options:["Spain","France","Portugal","England"], answer:1},
     {q:"Jacques Cartier was significant because ___.", options:["He first sailed the St. Lawrence River","He built the first railway","He discovered gold","He founded Toronto"], answer:0},
     {q:"British and French competition for control of Canada led to ___.", options:["no conflict","trade agreements","conflict including the Seven Years' War","immediate peace"], answer:1},
     {q:"The Battle of the Plains of Abraham (1759) resulted in ___.", options:["French victory","Indigenous victory","A draw","British victory over New France"], answer:3}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"Language", title:"Writing: Paragraphs", summary:"Grade 4 Writing strand: a well-organized paragraph has a topic sentence, supporting details, and a concluding sentence. All sentences relate to one main idea.",
   resourceLabel:"YouTube: Writing: Paragraphs", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Paragraphs%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=hhyMVd-tISU",
   quiz:[
     {q:"The topic sentence in a paragraph ___.", options:["ends the paragraph","is unrelated to the other sentences","gives a detail","states the main idea of the paragraph"], answer:3},
     {q:"Supporting sentences in a paragraph ___.", options:["end the paragraph","are optional","support the topic sentence with details","introduce new topics"], answer:2},
     {q:"A concluding sentence ___.", options:["asks a question","introduces the topic","adds a new idea","wraps up the main idea"], answer:3},
     {q:"How many main ideas should one paragraph have?", options:["One","Two or three","None","As many as possible"], answer:0},
     {q:"Which would make a good topic sentence for a paragraph about dogs?", options:["Dogs can run.","My dog is named Rex.","Dogs make excellent pets.","Dogs are brown."], answer:2}
   ]},
  {subject:"Math", title:"Adding Fractions with Same Denominator", summary:"Grade 4 Number strand: to add fractions with the same denominator, add the numerators and keep the denominator the same.",
   resourceLabel:"YouTube: Adding Fractions with Same Denominator", resourceUrl:"https://www.youtube.com/results?search_query=Adding%20Fractions%20with%20Same%20Denominator%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=rLCheqJh_rQ",
   quiz:[
     {q:"1/5 + 2/5 = ?", options:["3/10","2/10","1/5","3/5"], answer:3},
     {q:"2/7 + 3/7 = ?", options:["1/7","6/7","5/7","5/14"], answer:2},
     {q:"3/8 + 4/8 = ?", options:["7/16","1/8","7/8","6/8"], answer:2},
     {q:"When adding fractions with the same denominator, the denominator ___.", options:["doubles","stays the same","adds too","becomes 0"], answer:1},
     {q:"1/4 + 2/4 = ?", options:["1/2","3/8","3/4","2/4"], answer:2}
   ]},
  {subject:"Science", title:"Rock Cycle", summary:"Grade 4 Science Earth strand: rocks cycle continuously between igneous, sedimentary, and metamorphic forms through geological processes.",
   resourceLabel:"YouTube: Rock Cycle", resourceUrl:"https://www.youtube.com/results?search_query=Rock%20Cycle%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=VByCLpj-I_s",
   quiz:[
     {q:"What drives the rock cycle?", options:["Heat, pressure, and surface weathering","The moon's gravity","Only volcanic eruptions","Wind and rain only"], answer:0},
     {q:"Weathering and erosion break rocks into ___.", options:["sediment","lava","magma","crystals"], answer:0},
     {q:"Sediment that is compressed and cemented forms ___.", options:["sedimentary rock","metamorphic rock","lava","igneous rock"], answer:0},
     {q:"When magma cools it forms ___.", options:["sediment","igneous rock","sedimentary rock","metamorphic rock"], answer:1},
     {q:"The rock cycle shows that rocks ___.", options:["are always igneous","only come from volcanoes","can transform from one type to another","never change"], answer:2}
   ]},
  {subject:"SocialStudies", title:"European Explorers", summary:"Grade 4 Social Studies: European explorers from the 1400s–1600s sailed to North America, changing the world and affecting Indigenous peoples significantly.",
   resourceLabel:"YouTube: European Explorers", resourceUrl:"https://www.youtube.com/results?search_query=European%20Explorers%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=a8hDKU_bAec",
   quiz:[
     {q:"Why did Europeans explore the world in the 1400s–1600s?", options:["They were lost","They wanted to meet Indigenous peoples","They sought new trade routes and resources","They were looking for Canada specifically"], answer:2},
     {q:"Christopher Columbus (1492) sailed for ___.", options:["Portugal","England","France","Spain"], answer:3},
     {q:"John Cabot claimed land for ___.", options:["France","England","Portugal","Spain"], answer:1},
     {q:"The arrival of Europeans had a ___ impact on Indigenous peoples.", options:["no impact","devastating — disease and displacement","mostly positive","completely neutral"], answer:1},
     {q:"Samuel de Champlain is known for ___.", options:["Finding gold","Founding Quebec City in 1608","Winning the Seven Years' War","Discovering North America"], answer:1}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"Language", title:"Writing: Descriptive Writing", summary:"Grade 4 Writing strand: descriptive writing uses sensory details (sight, sound, smell, touch, taste) and vivid language to create a clear picture for the reader.",
   resourceLabel:"YouTube: Writing: Descriptive Writing", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Descriptive%20Writing%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=DQpIG_M_I-A",
   quiz:[
     {q:"Descriptive writing uses ___.", options:["only facts and numbers","sensory details and vivid language","only dialogue","only action verbs"], answer:1},
     {q:"Which is a more descriptive sentence?", options:["I saw a flower.","The crimson rose smelled sweet.","The flower was nice.","The flower was red."], answer:1},
     {q:"Sensory details include descriptions of ___.", options:["mathematics","sight, sound, smell, touch, and taste","grammar rules only","sentence structure"], answer:1},
     {q:"Vivid adjectives make writing ___.", options:["more boring","harder to read","shorter","more specific and engaging"], answer:3},
     {q:"Which word is more vivid?", options:["ecstatic","okay","happy","fine"], answer:0}
   ]},
  {subject:"Math", title:"Decimals: Tenths", summary:"Grade 4 Number strand: a decimal is another way to write a fraction. Tenths represent parts of a whole divided into 10 equal parts (e.g., 0.3 = 3/10).",
   resourceLabel:"YouTube: Decimals: Tenths", resourceUrl:"https://www.youtube.com/results?search_query=Decimals%3A%20Tenths%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=KrAQneGhyuE",
   quiz:[
     {q:"0.7 means ___.", options:["7 tenths","7 ones","7 hundredths","70 ones"], answer:0},
     {q:"Which decimal equals 3/10?", options:["0.03","30.0","0.3","3.0"], answer:2},
     {q:"What is 6 tenths as a decimal?", options:["0.06","6.0","60.0","0.6"], answer:3},
     {q:"0.1 + 0.4 = ?", options:["0.5","0.04","0.3","5.0"], answer:0},
     {q:"Which is less than 0.5?", options:["0.9","0.3","0.6","0.8"], answer:1}
   ]},
  {subject:"Science", title:"Soil Formation", summary:"Grade 4 Science Earth strand: soil forms over thousands of years by weathering of rock and addition of organic matter. It has layers called horizons.",
   resourceLabel:"YouTube: Soil Formation", resourceUrl:"https://www.youtube.com/results?search_query=Soil%20Formation%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=og9A_Apr534",
   quiz:[
     {q:"Soil forms from ___.", options:["weathered rock and organic matter","only sand","water alone","only plants"], answer:0},
     {q:"The top layer of soil is ___.", options:["bedrock","parent material","topsoil (humus-rich)","subsoil"], answer:2},
     {q:"Topsoil is important because ___.", options:["it contains no water","it is the hardest layer","it is rich in nutrients for plants","it is made of solid rock"], answer:2},
     {q:"How long does it take to form good soil?", options:["Hundreds to thousands of years","Only in rainy seasons","A few days","A few years"], answer:0},
     {q:"What does humus in soil come from?", options:["Water","Decayed plants and animals","Rocks only","Sand and gravel"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Government: Democracy and Monarchy", summary:"Grade 4 Social Studies: governments organize society and make laws. A democracy gives citizens a voice; a monarchy is led by a king or queen.",
   resourceLabel:"YouTube: Government: Democracy and Monarchy", resourceUrl:"https://www.youtube.com/results?search_query=Government%3A%20Democracy%20and%20Monarchy%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=hLzXOA6FBX8",
   quiz:[
     {q:"In a democracy, leaders are ___.", options:["appointed by religious leaders","inherited through family","chosen by the citizens through voting","selected by the military"], answer:2},
     {q:"Canada is a ___.", options:["dictatorship","republic","absolute monarchy","a constitutional monarchy"], answer:3},
     {q:"Parliament makes ___.", options:["food","laws","buildings","schools"], answer:1},
     {q:"A constitutional monarchy means ___.", options:["the monarch has unlimited power","there is no elected government","only the monarch rules","the monarch's power is limited by law"], answer:3},
     {q:"Voting is important because ___.", options:["only wealthy people vote","it is not important","citizens have a voice in choosing their government","the government decides everything anyway"], answer:0}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"Language", title:"Writing: Persuasive Writing", summary:"Grade 4 Writing strand: persuasive writing argues for a position using reasons, evidence, and a call to action. It has a clear opinion statement.",
   resourceLabel:"YouTube: Writing: Persuasive Writing", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Persuasive%20Writing%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=hD9arWXIddM",
   quiz:[
     {q:"The purpose of persuasive writing is to ___.", options:["tell a story","describe something","convince the reader to act","explain how to do something"], answer:2},
     {q:"A persuasive text should include ___.", options:["a clear opinion, reasons, and evidence","a fictional story","only opinions with no evidence","only facts with no opinion"], answer:0},
     {q:"Which is a good opinion statement for a persuasive text?", options:["Some students eat lunch.","Dogs exist.","Schools should have longer lunch breaks.","Dogs can run."], answer:2},
     {q:"Counter-arguments in persuasive writing ___.", options:["are unrelated to the topic","should always be avoided","weaken your argument","acknowledge and refute opposing views"], answer:3},
     {q:"A call to action at the end of a persuasive text asks the reader to ___.", options:["do something or change their view","summarize what they read","stop reading","find more information"], answer:0}
   ]},
  {subject:"Math", title:"Decimals: Hundredths", summary:"Grade 4 Number strand: hundredths represent parts of a whole divided into 100 equal parts. 0.23 = 23/100 = 2 tenths + 3 hundredths.",
   resourceLabel:"YouTube: Decimals: Hundredths", resourceUrl:"https://www.youtube.com/results?search_query=Decimals%3A%20Hundredths%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=KrAQneGhyuE",
   quiz:[
     {q:"0.47 means ___.", options:["47 hundredths","4 tenths 7 ones","47 tenths","47 ones"], answer:0},
     {q:"Which decimal equals 15/100?", options:["0.15","1.5","15.0","0.015"], answer:0},
     {q:"What is 8 hundredths as a decimal?", options:["8.0","0.08","80.0","0.8"], answer:1},
     {q:"0.25 + 0.50 = ?", options:["0.55","0.25","0.75","0.70"], answer:2},
     {q:"Which is greater: 0.3 or 0.30?", options:["Cannot compare","Equal — they are the same","0.3","0.30"], answer:1}
   ]},
  {subject:"Science", title:"Properties of Light: Reflection", summary:"Grade 4 Science Energy strand: light travels in straight lines and reflects off surfaces. The angle of incidence equals the angle of reflection.",
   resourceLabel:"YouTube: Properties of Light: Reflection", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Light%3A%20Reflection%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=DzpHXtnXFCI",
   quiz:[
     {q:"Light travels in ___.", options:["circles","zigzags","straight lines","curves"], answer:2},
     {q:"Reflection occurs when light ___.", options:["bounces off a surface","bends as it passes through","disappears into an object","is absorbed by a surface"], answer:0},
     {q:"Which surface reflects light best?", options:["A sponge","Dark wood","Black velvet","A mirror"], answer:3},
     {q:"The angle of incidence is ___.", options:["less than the angle of reflection","greater than the angle of reflection","equal to the angle of reflection","always 90 degrees"], answer:2},
     {q:"Why does a mirror show your reflection?", options:["It is transparent","It glows","It absorbs light","It reflects light at the same angle"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Trade and Commerce in History", summary:"Grade 4 Social Studies: trade is the exchange of goods and services. Ancient and early modern civilizations developed trade routes that spread culture and ideas.",
   resourceLabel:"YouTube: Trade and Commerce in History", resourceUrl:"https://www.youtube.com/results?search_query=Trade%20and%20Commerce%20in%20History%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=HfN8BnRJryQ",
   quiz:[
     {q:"Trade is the exchange of ___.", options:["animals only","soldiers","goods and services","land only"], answer:2},
     {q:"The Silk Road connected ___.", options:["Europe, the Middle East, and Asia","North and South America","Canada and the USA","Africa and Australia"], answer:0},
     {q:"Why did civilizations trade with each other?", options:["To get goods they couldn't produce","Only for art","For entertainment","Only for war"], answer:0},
     {q:"Trade often led to ___.", options:["isolation of cultures","spreading ideas and culture","conflict only","only economic profit"], answer:1},
     {q:"The fur trade in early Canada involved ___.", options:["only Indigenous peoples","only French traders","only European settlers","both Indigenous and European people"], answer:3}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"Language", title:"Spelling: ie/ei Words", summary:"Grade 4 Language strand: the 'i before e except after c' rule helps spell many words, but has exceptions. Students apply this pattern in context.",
   resourceLabel:"YouTube: Spelling: ie/ei Words", resourceUrl:"https://www.youtube.com/results?search_query=Spelling%3A%20ie%2Fei%20Words%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=SoCfScr9VM8",
   quiz:[
     {q:"Which spelling is correct?", options:["recieve","receive","receeve","receve"], answer:1},
     {q:"'I before E except after C' means in the word BELIEVE you write ___.", options:["i only","ei","ie","e only"], answer:2},
     {q:"Which is spelled correctly?", options:["freind","frend","friend","frennd"], answer:2},
     {q:"After the letter C, you usually write ___ (not ei).", options:["ie","only e","only i","ei"], answer:3},
     {q:"Which word follows the 'i before e except after c' rule?", options:["weird","believe","their","neither"], answer:1}
   ]},
  {subject:"Math", title:"Money: Making Change", summary:"Grade 4 Number strand: students calculate change by subtracting the price from the amount paid, using coins and bills up to $20.",
   resourceLabel:"YouTube: Money: Making Change", resourceUrl:"https://www.youtube.com/results?search_query=Money%3A%20Making%20Change%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=DbYbIB4m3RM",
   quiz:[
     {q:"An item costs $3.75. You pay $5.00. Your change is ___.", options:["$1.25","$1.75","$2.25","$1.00"], answer:0},
     {q:"An item costs $12.49. You pay $15.00. Your change is ___.", options:["$2.61","$2.41","$2.51","$3.51"], answer:2},
     {q:"To calculate change, you ___.", options:["subtract the price from the amount paid","divide the price","add price and amount paid","multiply the price"], answer:0},
     {q:"An item costs $7.89. You pay $10.00. Your change is ___.", options:["$2.21","$3.11","$2.11","$3.21"], answer:2},
     {q:"You have $20. You buy items for $14.37. Change = ?", options:["$5.37","$6.63","$5.63","$6.37"], answer:2}
   ]},
  {subject:"Science", title:"Properties of Light: Refraction", summary:"Grade 4 Science Energy strand: refraction is the bending of light as it passes from one medium to another (e.g., from air to water).",
   resourceLabel:"YouTube: Properties of Light: Refraction", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Light%3A%20Refraction%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=DzpHXtnXFCI",
   quiz:[
     {q:"Refraction is the ___ of light.", options:["speeding up","slowing down","bending","absorption"], answer:2},
     {q:"Refraction occurs when light passes from one ___ to another.", options:["source","medium (material)","direction","colour"], answer:1},
     {q:"A straw in a glass of water appears to be bent because of ___.", options:["absorption","refraction","reflection","diffusion"], answer:1},
     {q:"A prism separates white light into its colours because different colours ___ at different angles.", options:["refract","reflect","absorb","emit"], answer:0},
     {q:"A rainbow is an example of ___.", options:["only reflection","only absorption","light bending through water droplets","diffraction only"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Human Rights", summary:"Grade 4 Social Studies: human rights are basic rights all people deserve. The Universal Declaration of Human Rights (UDHR, 1948) protects these rights globally.",
   resourceLabel:"YouTube: Human Rights", resourceUrl:"https://www.youtube.com/results?search_query=Human%20Rights%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=FWwEMFSY1r0",
   quiz:[
     {q:"Human rights are rights that ___.", options:["all people have equally","only adults have","only citizens have","only wealthy people have"], answer:0},
     {q:"The Universal Declaration of Human Rights was adopted in ___.", options:["1867","2000","1948","1776"], answer:2},
     {q:"Which is a basic human right?", options:["Unlimited money","Never going to school","Owning luxury goods","Freedom of speech and safety"], answer:3},
     {q:"Who is responsible for upholding human rights?", options:["Governments and individuals","Only wealthy nations","Only the United Nations","No one"], answer:0},
     {q:"Why are human rights important?", options:["They only apply in certain countries","They protect everyone's dignity","They are not","Only politicians care about them"], answer:1}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"Language", title:"Grammar: Adverbs", summary:"Grade 4 Language strand: adverbs modify verbs, adjectives, or other adverbs. They tell how, when, where, or to what degree something happens.",
   resourceLabel:"YouTube: Grammar: Adverbs", resourceUrl:"https://www.youtube.com/results?search_query=Grammar%3A%20Adverbs%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=cAHgn61uXog",
   quiz:[
     {q:"An adverb modifies a ___.", options:["preposition only","verb, adjective, or another adverb","noun only","pronoun only"], answer:1},
     {q:"Which word is an adverb in: She spoke softly?", options:["She","spoke","(no adverb)","softly"], answer:3},
     {q:"Adverbs of manner tell ___.", options:["how","when","to what degree","where"], answer:0},
     {q:"Adverbs of time tell ___.", options:["how","where","to what degree","when"], answer:3},
     {q:"Many adverbs end in ___.", options:["–ly","–er","–tion","–ing"], answer:0}
   ]},
  {subject:"Math", title:"Patterns: Numeric and Geometric", summary:"Grade 4 Algebra and Patterning strand: numeric patterns follow a mathematical rule; geometric patterns involve shapes. Students identify rules and extend patterns.",
   resourceLabel:"YouTube: Patterns: Numeric and Geometric", resourceUrl:"https://www.youtube.com/results?search_query=Patterns%3A%20Numeric%20and%20Geometric%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=vV7C7bXm4VI",
   quiz:[
     {q:"What is the rule? 3, 6, 9, 12...", options:["add 2","add 3","add 4","multiply by 2"], answer:1},
     {q:"What comes next? 1, 2, 4, 8, 16, ___", options:["24","18","20","32"], answer:3},
     {q:"A geometric pattern uses ___.", options:["only colours","only lines","numbers only","repeating or growing shapes"], answer:3},
     {q:"What is the rule? 100, 90, 80, 70...", options:["subtract 10","subtract 20","subtract 5","add 10"], answer:0},
     {q:"Which is an example of a geometric pattern?", options:["A,B,C,A,B,C","triangle, square, triangle, square","2,4,6,8","red, blue, green, red"], answer:1}
   ]},
  {subject:"Science", title:"Sound: Vibration and Frequency", summary:"Grade 4 Science Energy strand: sounds are made by vibrations. Frequency determines pitch — higher frequency = higher pitch. Amplitude determines volume.",
   resourceLabel:"YouTube: Sound: Vibration and Frequency", resourceUrl:"https://www.youtube.com/results?search_query=Sound%3A%20Vibration%20and%20Frequency%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=fe2DAWI7ZM4",
   quiz:[
     {q:"Sound is caused by ___.", options:["magnetic fields","light waves","electrical signals","vibrations"], answer:3},
     {q:"Frequency refers to ___.", options:["how loud a sound is","how many vibrations per second","the speed of light","how far sound travels"], answer:1},
     {q:"A high-frequency sound has a ___ pitch.", options:["medium","high","no","low"], answer:1},
     {q:"Amplitude of a sound wave determines its ___.", options:["pitch","volume (loudness)","speed","frequency"], answer:1},
     {q:"In which medium does sound travel fastest?", options:["Air","Vacuum (space)","Solid materials (like steel)","Water"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canadian Geography: Provinces and Territories", summary:"Grade 4 Social Studies: Canada has 10 provinces and 3 territories. Each has a capital city and distinct geographic features.",
   resourceLabel:"YouTube: Canadian Geography: Provinces and Territories", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Geography%3A%20Provinces%20and%20Territories%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Qo7aTFHyhPE",
   quiz:[
     {q:"How many provinces does Canada have?", options:["12","10","9","8"], answer:1},
     {q:"How many territories does Canada have?", options:["2","4","3","1"], answer:2},
     {q:"What is the largest province in Canada by area?", options:["Ontario","Alberta","Quebec","British Columbia"], answer:2},
     {q:"What is Canada's capital city?", options:["Vancouver","Toronto","Montreal","Ottawa"], answer:3},
     {q:"Which territory is the newest, created in 1999?", options:["Nunavut","Yukon","British Columbia","Northwest Territories"], answer:0}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"Language", title:"Vocabulary: Context Clues", summary:"Grade 4 Language strand: context clues are words and phrases near an unknown word that help you determine its meaning without a dictionary.",
   resourceLabel:"YouTube: Vocabulary: Context Clues", resourceUrl:"https://www.youtube.com/results?search_query=Vocabulary%3A%20Context%20Clues%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=CiNggzdWkIo",
   quiz:[
     {q:"Context clues are ___.", options:["words nearby that hint at meaning","only antonyms","only synonyms","definitions found in the glossary"], answer:0},
     {q:"Which type of context clue gives a definition within the text?", options:["Restatement clue: 'X, which means...'","Inference clue","Synonym clue","Antonym clue"], answer:0},
     {q:"Using context clues helps readers ___.", options:["figure out meanings while reading","look up every word in a dictionary","memorize vocabulary lists","skip unknown words"], answer:0},
     {q:"In 'The magnanimous king gave generously to the poor,' magnanimous means ___.", options:["generous and kind","cruel","quiet","stingy"], answer:0},
     {q:"Which strategy helps most with a word you do not know?", options:["Skip to the next chapter","Read the surrounding sentences for clues","Ignore it","Ask someone immediately"], answer:1}
   ]},
  {subject:"Math", title:"Geometry: Angles", summary:"Grade 4 Geometry strand: an angle is formed by two rays with a common endpoint. A right angle = 90°, acute angle < 90°, obtuse angle > 90°.",
   resourceLabel:"YouTube: Geometry: Angles", resourceUrl:"https://www.youtube.com/results?search_query=Geometry%3A%20Angles%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=aOipc02LUpo",
   quiz:[
     {q:"A right angle measures exactly ___.", options:["180°","45°","60°","90°"], answer:3},
     {q:"An acute angle measures ___.", options:["180°","less than 90°","more than 90°","exactly 90°"], answer:1},
     {q:"An obtuse angle measures ___.", options:["more than 180°","between 90° and 180°","exactly 90°","less than 90°"], answer:1},
     {q:"A straight angle measures ___.", options:["270°","90°","45°","180°"], answer:3},
     {q:"Which tool measures angles?", options:["Scale","Protractor","Ruler","Compass"], answer:1}
   ]},
  {subject:"Science", title:"Pulleys and Gears", summary:"Grade 4 Science Energy strand: pulleys and gears are simple machines that redirect or change force. Gears can speed up or slow down motion and change direction.",
   resourceLabel:"YouTube: Pulleys and Gears", resourceUrl:"https://www.youtube.com/results?search_query=Pulleys%20and%20Gears%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=t5zJ80OWLUk",
   quiz:[
     {q:"A pulley is used to ___.", options:["generate electricity","increase temperature","lift or move loads by redirecting force","make objects glow"], answer:2},
     {q:"In a fixed pulley, the force needed to lift a load ___.", options:["halves","doubles","triples","stays the same (only direction changes)"], answer:3},
     {q:"A moveable pulley ___ the force needed.", options:["triples","keeps the same","doubles","reduces by about half"], answer:3},
     {q:"When two gears mesh, they rotate in ___ directions.", options:["opposite","no","the same","random"], answer:0},
     {q:"A larger gear turning a smaller gear makes the smaller gear rotate ___.", options:["faster","slower","at the same speed","backwards only"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Ontario Geography", summary:"Grade 4 Social Studies: Ontario is Canada's most populous province with diverse geography including the Great Lakes, Canadian Shield, and Great Lakes–St. Lawrence Lowlands.",
   resourceLabel:"YouTube: Ontario Geography", resourceUrl:"https://www.youtube.com/results?search_query=Ontario%20Geography%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=QBQ5ZhHlkkY",
   quiz:[
     {q:"Ontario borders how many of the Great Lakes?", options:["2","3","5","4"], answer:3},
     {q:"The Canadian Shield in Ontario is characterized by ___.", options:["ancient rock, forests, and lakes","mountain ranges","dry desert","flat prairies"], answer:0},
     {q:"The most populous city in Ontario is ___.", options:["Hamilton","London","Ottawa","Toronto"], answer:3},
     {q:"Ontario's provincial capital is ___.", options:["Toronto","Ottawa","Hamilton","Kingston"], answer:0},
     {q:"Which region of Ontario is most suited for farming?", options:["Great Lakes–St. Lawrence Lowlands","Canadian Shield","Hudson Bay Lowlands","Northern Ontario"], answer:0}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"Language", title:"Reading: Compare and Contrast", summary:"Grade 4 Reading strand: comparing shows how two things are alike; contrasting shows how they differ. Signal words: both, similarly, however, but, in contrast.",
   resourceLabel:"YouTube: Reading: Compare and Contrast", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Compare%20and%20Contrast%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2enr-yY68tg",
   quiz:[
     {q:"Comparing means finding how things are ___.", options:["unrelated","different","bigger","the same or similar"], answer:3},
     {q:"Contrasting means finding how things are ___.", options:["different","similar","the same","related"], answer:0},
     {q:"Which signal word shows a contrast?", options:["However","Similarly","Also","Both"], answer:0},
     {q:"A Venn diagram helps ___.", options:["draw maps","add numbers","compare and contrast two or more things","write paragraphs"], answer:2},
     {q:"Which text type often uses comparison and contrast?", options:["A report about two animals","A personal diary","A recipe","A poem"], answer:0}
   ]},
  {subject:"Math", title:"Area and Perimeter", summary:"Grade 4 Measurement strand: perimeter is the distance around a shape; area is the space inside. Area of a rectangle = length × width; perimeter = 2(l + w).",
   resourceLabel:"YouTube: Area and Perimeter", resourceUrl:"https://www.youtube.com/results?search_query=Area%20and%20Perimeter%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=AAY1bsazcgM",
   quiz:[
     {q:"Perimeter is the ___.", options:["space inside a shape","weight of a shape","distance around the outside of a shape","height of a shape"], answer:2},
     {q:"Area is measured in ___.", options:["linear units (cm)","grams","cubic units (cm³)","square units (cm²)"], answer:3},
     {q:"A rectangle is 5 cm long and 3 cm wide. Area = ?", options:["8 cm²","10 cm²","16 cm²","15 cm²"], answer:3},
     {q:"A rectangle is 6 cm long and 4 cm wide. Perimeter = ?", options:["10 cm","20 cm","24 cm","48 cm"], answer:1},
     {q:"Area of a square with side 7 cm = ?", options:["28 cm²","49 cm²","14 cm²","21 cm²"], answer:1}
   ]},
  {subject:"Science", title:"Electricity: Static and Current", summary:"Grade 4 Science Energy strand: static electricity is a build-up of charge; current electricity is a flow of electrons through a conductor.",
   resourceLabel:"YouTube: Electricity: Static and Current", resourceUrl:"https://www.youtube.com/results?search_query=Electricity%3A%20Static%20and%20Current%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PC4PteRt3A4",
   quiz:[
     {q:"Static electricity is caused by ___.", options:["burning fuel","magnetism","a build-up of electric charge","a flow of electrons in a circuit"], answer:2},
     {q:"Current electricity flows through ___.", options:["a vacuum","conductors in a circuit","insulators","non-metals only"], answer:1},
     {q:"Which is a good conductor of electricity?", options:["Rubber","Wood","Glass","Copper wire"], answer:3},
     {q:"An insulator ___.", options:["creates static electricity","blocks the flow of electricity","allows electricity to flow freely","has no electrical properties"], answer:1},
     {q:"Which is an example of static electricity?", options:["Turning on a light bulb","Charging a phone","A lightning bolt or a rubbed balloon","Using a toaster"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Maps: Physical Features", summary:"Grade 4 Social Studies: physical maps show natural features like mountains, rivers, lakes, and plains. They use colour and symbols to represent terrain.",
   resourceLabel:"YouTube: Maps: Physical Features", resourceUrl:"https://www.youtube.com/results?search_query=Maps%3A%20Physical%20Features%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mSugSh7z8MM",
   quiz:[
     {q:"A physical map shows ___.", options:["natural features like mountains","population density","roads and cities","political boundaries"], answer:0},
     {q:"On most physical maps, blue represents ___.", options:["water (rivers, lakes, oceans)","land","grasslands","mountains"], answer:0},
     {q:"What is a legend (key) on a map?", options:["A table explaining the map's symbols","Scale bar","North arrow","The title"], answer:0},
     {q:"Which tool on a map shows distance?", options:["Scale bar","Title","Legend","North arrow"], answer:0},
     {q:"The Rocky Mountains in Canada are located in ___.", options:["Eastern Canada","Western Canada","Central Ontario","Atlantic provinces"], answer:1}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"Language", title:"Figurative Language: Similes", summary:"Grade 4 Language strand: a simile compares two unlike things using 'like' or 'as'. Example: 'brave as a lion,' 'runs like the wind'.",
   resourceLabel:"YouTube: Figurative Language: Similes", resourceUrl:"https://www.youtube.com/results?search_query=Figurative%20Language%3A%20Similes%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=iLw5DSyYsaI",
   quiz:[
     {q:"A simile compares two things using ___.", options:["is/was","and/but","like or as","metaphor words"], answer:2},
     {q:"Which is a simile?", options:["The car is a beast.","Time flies.","She ran like the wind.","The moon smiled."], answer:2},
     {q:"What does 'brave as a lion' mean?", options:["A comparison without meaning","Lions are brave animals","The person is a lion","The person is extremely brave"], answer:3},
     {q:"Similes make writing more ___.", options:["boring","difficult","vivid and relatable","confusing"], answer:2},
     {q:"Which is NOT a simile?", options:["white as snow","cold as ice","The thunder roared","quiet as a mouse"], answer:2}
   ]},
  {subject:"Math", title:"Metric Measurement: Length", summary:"Grade 4 Measurement strand: the metric system uses kilometres (km), metres (m), centimetres (cm), and millimetres (mm). 1 m = 100 cm; 1 km = 1000 m.",
   resourceLabel:"YouTube: Metric Measurement: Length", resourceUrl:"https://www.youtube.com/results?search_query=Metric%20Measurement%3A%20Length%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=AVC-426M6V0",
   quiz:[
     {q:"1 metre = ___ centimetres.", options:["1","1000","10","100"], answer:3},
     {q:"1 kilometre = ___ metres.", options:["100","10000","10","1000"], answer:3},
     {q:"Which unit would you use to measure the length of a pencil?", options:["Metres","Kilometres","Grams","Centimetres"], answer:3},
     {q:"Which unit would you use to measure the distance between two cities?", options:["Metres","Centimetres","Millimetres","Kilometres"], answer:3},
     {q:"Convert 3 m to cm.", options:["3000 cm","300 cm","3 cm","30 cm"], answer:1}
   ]},
  {subject:"Science", title:"Electric Circuits", summary:"Grade 4 Science Energy strand: a complete circuit allows electricity to flow. It needs a power source, conductors, and a load (device). Circuits can be series or parallel.",
   resourceLabel:"YouTube: Electric Circuits", resourceUrl:"https://www.youtube.com/results?search_query=Electric%20Circuits%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=wYE24otiwVQ",
   quiz:[
     {q:"For electricity to flow, a circuit must be ___.", options:["very long","broken","open","complete (closed)"], answer:3},
     {q:"Which is NOT needed in a basic circuit?", options:["A magnet","Power source (battery)","Load (light bulb)","Wire (conductor)"], answer:0},
     {q:"In a series circuit, components are connected ___.", options:["in a grid","in parallel paths","one after another in one loop","randomly"], answer:2},
     {q:"In a parallel circuit, each branch has ___.", options:["only one component","no power at all","the same current as all others","its own direct path to the power source"], answer:3},
     {q:"If a bulb in a series circuit burns out, the other bulbs ___.", options:["explode","keep working","also go out (circuit is broken)","get brighter"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canada's Natural Resources", summary:"Grade 4 Social Studies: Canada is rich in natural resources including forests, minerals, freshwater, oil, and agricultural land. These support the economy but must be managed sustainably.",
   resourceLabel:"YouTube: Canada's Natural Resources", resourceUrl:"https://www.youtube.com/results?search_query=Canada%27s%20Natural%20Resources%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ajk-pvm5vfQ",
   quiz:[
     {q:"Which of these is NOT a natural resource?", options:["Fresh water","A car","Gold","Timber/wood"], answer:1},
     {q:"Why are Canada's forests valuable?", options:["Lumber, paper, habitat, and climate help","They are not valuable","Only for tourism","Only for scenery"], answer:0},
     {q:"What energy resource does Alberta have in large quantities?", options:["Gold","Coal only","Iron ore","Oil and natural gas"], answer:3},
     {q:"Sustainable use of resources means ___.", options:["only using what you can carry","using them as fast as possible","never using them","using them without depleting them"], answer:3},
     {q:"Which province is known for potash mining?", options:["Saskatchewan","Newfoundland","Nova Scotia","Ontario"], answer:0}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"Language", title:"Figurative Language: Metaphors", summary:"Grade 4 Language strand: a metaphor directly states that one thing IS another unlike thing, without using 'like' or 'as'. Example: 'Life is a journey.'",
   resourceLabel:"YouTube: Figurative Language: Metaphors", resourceUrl:"https://www.youtube.com/results?search_query=Figurative%20Language%3A%20Metaphors%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=35PzoZWJpIM",
   quiz:[
     {q:"A metaphor says one thing ___ another.", options:["is like/as","is similar to","is bigger than","IS directly"], answer:3},
     {q:"Which is a metaphor?", options:["He is as strong as an ox.","She ran like a cheetah.","The rain fell like tears.","The world is a stage."], answer:3},
     {q:"What does 'Time is money' mean?", options:["Clocks cost money","Time is free","Time is currency","Time is valuable, don't waste it"], answer:3},
     {q:"A metaphor differs from a simile because it ___.", options:["is only used in poetry","directly states one thing is another","makes no comparison","uses 'like' or 'as'"], answer:1},
     {q:"Which is a metaphor?", options:["Her voice was music to my ears.","quiet as a mouse","brave as a lion","He runs like a gazelle."], answer:0}
   ]},
  {subject:"Math", title:"Mass and Volume Measurement", summary:"Grade 4 Measurement strand: mass is measured in grams (g) and kilograms (kg). Volume is measured in litres (L) and millilitres (mL). 1 kg = 1000 g; 1 L = 1000 mL.",
   resourceLabel:"YouTube: Mass and Volume Measurement", resourceUrl:"https://www.youtube.com/results?search_query=Mass%20and%20Volume%20Measurement%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=AVC-426M6V0",
   quiz:[
     {q:"1 kilogram = ___ grams.", options:["100","10","1000","10000"], answer:2},
     {q:"1 litre = ___ millilitres.", options:["100","10","10000","1000"], answer:3},
     {q:"Which unit measures how heavy something is?", options:["Kilogram","Litre","Kilometre","Millilitre"], answer:0},
     {q:"Which unit measures the amount of liquid in a bottle?", options:["Centimetre","Kilometre","Millilitre/Litre","Kilogram"], answer:2},
     {q:"A bag weighs 2500 g. How many kilograms is that?", options:["0.25 kg","25 kg","250 kg","2.5 kg"], answer:3}
   ]},
  {subject:"Science", title:"Forces: Gravity and Friction", summary:"Grade 4 Science Energy strand: gravity is the force that pulls objects toward Earth. Friction is the force that resists movement between surfaces in contact.",
   resourceLabel:"YouTube: Forces: Gravity and Friction", resourceUrl:"https://www.youtube.com/results?search_query=Forces%3A%20Gravity%20and%20Friction%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=8wXWraHglVM",
   quiz:[
     {q:"Gravity is a force that ___.", options:["stops all motion","only exists in space","pulls objects toward each other","pushes objects upward"], answer:2},
     {q:"Friction is a force that ___.", options:["resists sliding motion between surfaces","speeds objects up","pulls objects down","pushes objects sideways"], answer:0},
     {q:"Which surface creates MORE friction?", options:["Rough sandpaper","A wet road","A polished marble floor","Ice"], answer:0},
     {q:"Friction produces ___.", options:["heat and slows objects down","more gravity","electrical charge","cold temperatures"], answer:0},
     {q:"Without gravity, objects on Earth would ___.", options:["get heavier","fall faster","stay in one place forever","float away into space"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Environment: Conservation", summary:"Grade 4 Social Studies: conservation means protecting and managing natural resources wisely to prevent their depletion and preserve environments for future generations.",
   resourceLabel:"YouTube: Environment: Conservation", resourceUrl:"https://www.youtube.com/results?search_query=Environment%3A%20Conservation%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=IcyM43z0UE8",
   quiz:[
     {q:"Conservation means ___.", options:["only saving money","using all resources immediately","protecting natural resources wisely","never using resources"], answer:2},
     {q:"Which is an example of conservation?", options:["Planting trees and reducing waste","Wasting paper","Building more factories","Leaving taps running"], answer:0},
     {q:"Canada Day (July 1) celebrates ___.", options:["Canada becoming a nation in 1867","Indigenous peoples' day","Conservation week","The founding of Ontario"], answer:0},
     {q:"Why should we conserve freshwater?", options:["Only 3% of Earth's water is fresh","Freshwater is dirty","Water is unlimited","Only fish need freshwater"], answer:0},
     {q:"Which action MOST helps conserve forests?", options:["Never entering forests","Cutting down all old trees","Using more wood products","Paper recycling and sustainable forestry"], answer:3}
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"Language", title:"Reading: Sequencing", summary:"Grade 4 Reading strand: sequence is the order in which events happen. Signal words: first, then, next, after, finally, before.",
   resourceLabel:"YouTube: Reading: Sequencing", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Sequencing%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4Iz5Gmkz8BQ",
   quiz:[
     {q:"Sequence means ___.", options:["a cause-and-effect relationship","the main idea","the order in which events occur","a comparison"], answer:2},
     {q:"Which signal word shows a sequence?", options:["In contrast","Next","However","Because"], answer:1},
     {q:"Why is sequence important in a how-to text?", options:["Only the first step matters","All steps can be done in any order","It is not","Steps must be in order"], answer:3},
     {q:"Which goes last in a story's sequence?", options:["The beginning","The problem","The introduction","The resolution/ending"], answer:3},
     {q:"'First mix the batter, then bake it' shows ___.", options:["contrast","sequence","cause and effect","comparison"], answer:1}
   ]},
  {subject:"Math", title:"Data: Bar Graphs", summary:"Grade 4 Data strand: a bar graph uses horizontal or vertical bars to compare quantities across categories. Students read, create, and interpret bar graphs.",
   resourceLabel:"YouTube: Data: Bar Graphs", resourceUrl:"https://www.youtube.com/results?search_query=Data%3A%20Bar%20Graphs%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zF_dBk8EPDk",
   quiz:[
     {q:"A bar graph is used to ___.", options:["measure angles","show sequence","compare quantities across categories","calculate perimeter"], answer:2},
     {q:"The vertical axis of a bar graph usually shows ___.", options:["frequency or quantity","colours","categories","dates"], answer:0},
     {q:"If the 'Dogs' bar reaches 12 and 'Cats' bar reaches 8, there are ___ more dogs.", options:["5","4","3","2"], answer:1},
     {q:"What is the title of a graph used for?", options:["Decoration","To tell what data the graph shows","To label the axes","To list all data"], answer:1},
     {q:"A bar graph differs from a pictograph because ___.", options:["only bar graphs have titles","pictographs are always better","bar graphs use bars instead of pictures/symbols","bar graphs are less accurate"], answer:2}
   ]},
  {subject:"Science", title:"Properties of Liquids and Solids", summary:"Grade 4 Science Materials strand: solids have definite shape and volume; liquids have definite volume but take the shape of their container.",
   resourceLabel:"YouTube: Properties of Liquids and Solids", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Liquids%20and%20Solids%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Hd1AdYdEvhw",
   quiz:[
     {q:"A solid has ___.", options:["no definite shape or volume","only colour","definite shape and definite volume","definite volume but no definite shape"], answer:2},
     {q:"A liquid has ___.", options:["definite shape and volume","definite volume, shape of its container","no mass","no volume"], answer:1},
     {q:"Which is a solid at room temperature?", options:["Air","Water","Wood","Mercury"], answer:2},
     {q:"The property of viscosity describes ___.", options:["the colour of a liquid","how thick a liquid is","how hot a liquid is","how heavy a liquid is"], answer:1},
     {q:"Which liquid has higher viscosity (is thicker)?", options:["Honey","Vinegar","Air","Water"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Canadian Culture and Arts", summary:"Grade 4 Social Studies: Canadian culture reflects Indigenous traditions and the contributions of people from many nations, expressed through music, art, literature, and celebrations.",
   resourceLabel:"YouTube: Canadian Culture and Arts", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Culture%20and%20Arts%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Qo7aTFHyhPE",
   quiz:[
     {q:"Canada's culture is ___.", options:["only British and French","uniform and the same everywhere","only Indigenous","shaped by many peoples and cultures"], answer:3},
     {q:"Which is a famous Canadian author?", options:["Charles Dickens","L.M. Montgomery (Anne of Green Gables)","William Shakespeare","Mark Twain"], answer:1},
     {q:"The Group of Seven were known for ___.", options:["painting Canadian landscapes","composing music","writing novels","playing hockey"], answer:0},
     {q:"Indigenous art often features ___.", options:["only landscapes","cultural symbols and stories","only abstract shapes","only portraits"], answer:1},
     {q:"Why is celebrating cultural arts important?", options:["Only for entertainment","Arts preserve culture, identity, and history","Only professional artists need it","It is not important"], answer:1}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"Language", title:"Writing: Narrative Writing", summary:"Grade 4 Writing strand: narrative writing tells a story with a clear beginning (characters/setting), middle (problem/rising action), and end (resolution).",
   resourceLabel:"YouTube: Writing: Narrative Writing", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Narrative%20Writing%20grade%204%20educational",
   quiz:[
     {q:"Narrative writing tells a ___.", options:["fact-based report","story with characters and events","persuasive argument","set of instructions"], answer:1},
     {q:"The beginning of a narrative should introduce ___.", options:["the characters and setting","the conclusion","the climax","the solution"], answer:0},
     {q:"The climax of a story is ___.", options:["the introduction of characters","the most exciting turning point","the beginning","the setting"], answer:1},
     {q:"The resolution of a narrative is ___.", options:["how the story begins","how the problem is solved","the problem","the climax"], answer:1},
     {q:"Which makes a narrative more engaging?", options:["Dialogue and vivid sensory details","Short, boring sentences","No descriptions","Only telling (no showing)"], answer:0}
   ]},
  {subject:"Math", title:"Data: Line Graphs", summary:"Grade 4 Data strand: a line graph shows how data changes over time. Points are connected by a line to show trends: increasing, decreasing, or stable.",
   resourceLabel:"YouTube: Data: Line Graphs", resourceUrl:"https://www.youtube.com/results?search_query=Data%3A%20Line%20Graphs%20grade%204%20educational",
   quiz:[
     {q:"A line graph is best used to show ___.", options:["data that changes over time","angles","fractions","categories compared at one time"], answer:0},
     {q:"The horizontal axis of a line graph usually shows ___.", options:["categories","colours","quantities","time (days, months, years)"], answer:3},
     {q:"An upward-sloping line on a graph shows ___.", options:["data is random","data is staying the same","data is increasing","data is decreasing"], answer:2},
     {q:"Which data set is best shown in a line graph?", options:["Daily temperature over one week","Animal habitats","Favourite sports of 30 students","Number of each type of fruit in a bowl"], answer:0},
     {q:"Points on a line graph are connected to show ___.", options:["separate categories","exact values only","trends and changes over time","the average"], answer:2}
   ]},
  {subject:"Science", title:"Mixtures and Solutions", summary:"Grade 4 Science Materials strand: a mixture is made of two or more substances combined physically. A solution is a mixture where one substance dissolves completely in another.",
   resourceLabel:"YouTube: Mixtures and Solutions", resourceUrl:"https://www.youtube.com/results?search_query=Mixtures%20and%20Solutions%20grade%204%20educational",
   quiz:[
     {q:"A mixture contains ___.", options:["a single compound","two or more substances combined","only one substance","only chemicals"], answer:1},
     {q:"In a solution, the dissolved substance is called the ___.", options:["solute","mixture","solvent","residue"], answer:0},
     {q:"What is a solvent?", options:["A type of magnet","The substance that does the dissolving","A type of acid","The substance that is dissolved"], answer:1},
     {q:"Which is an example of a solution?", options:["Salt dissolved in water","Oil and water (they separate)","Sand and water (sand settles)","Salad (mixed vegetables)"], answer:0},
     {q:"How can you separate a salt-and-water solution?", options:["Using a magnet","Using a filter","Freezing it and removing salt","Evaporating the water"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Citizenship: Rights and Responsibilities", summary:"Grade 4 Social Studies: in a democratic society, citizens have rights (freedoms) and responsibilities (duties). Being an active citizen benefits everyone.",
   resourceLabel:"YouTube: Citizenship: Rights and Responsibilities", resourceUrl:"https://www.youtube.com/results?search_query=Citizenship%3A%20Rights%20and%20Responsibilities%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=FWwEMFSY1r0",
   quiz:[
     {q:"Rights give citizens ___.", options:["no rules","freedoms and protections","unlimited power","only advantages"], answer:1},
     {q:"Responsibilities require citizens to ___.", options:["only benefit themselves","do nothing","obey laws and respect others","ignore rules"], answer:2},
     {q:"Voting is both a right and a ___.", options:["responsibility","privilege only for adults","reward","punishment"], answer:0},
     {q:"Why is community involvement important?", options:["It costs too much","Only politicians should be involved","It makes communities stronger","It is not"], answer:2},
     {q:"Which is an example of civic responsibility?", options:["Ignoring elections","Paying taxes and following laws","Only caring about yourself","Littering"], answer:1}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"Language", title:"Grammar: Conjunctions", summary:"Grade 4 Language strand: conjunctions join words, phrases, or clauses. Coordinating conjunctions: for, and, nor, but, or, yet, so (FANBOYS). Subordinating: because, since, although.",
   resourceLabel:"YouTube: Grammar: Conjunctions", resourceUrl:"https://www.youtube.com/results?search_query=Grammar%3A%20Conjunctions%20grade%204%20educational",
   quiz:[
     {q:"A conjunction joins ___.", options:["words, phrases, or clauses","only nouns","only verbs","only sentences"], answer:0},
     {q:"Which is a coordinating conjunction?", options:["because","but","since","although"], answer:1},
     {q:"Which is a subordinating conjunction?", options:["but","and","because","or"], answer:2},
     {q:"'I wanted to go, ___ it was raining.' Which conjunction fits?", options:["but","and","nor","or"], answer:0},
     {q:"FANBOYS stands for the ___ conjunctions.", options:["correlative","preposition","subordinating","coordinating"], answer:3}
   ]},
  {subject:"Math", title:"Probability: Likely and Unlikely", summary:"Grade 4 Data and Probability strand: probability describes the likelihood of an event: certain, likely, unlikely, or impossible.",
   resourceLabel:"YouTube: Probability: Likely and Unlikely", resourceUrl:"https://www.youtube.com/results?search_query=Probability%3A%20Likely%20and%20Unlikely%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=KzfWUEJjG18",
   quiz:[
     {q:"If an event is 'impossible,' the probability is ___.", options:["close to 1","0","1","close to 0"], answer:1},
     {q:"If an event is 'certain,' the probability is ___.", options:["close to 1","1","close to 0","0"], answer:1},
     {q:"A bag has 4 red and 1 blue marble. Picking red is ___.", options:["likely","unlikely","impossible","certain"], answer:0},
     {q:"Which outcome is 'impossible' when rolling a 6-sided die?", options:["Rolling a 1","Rolling a 7","Rolling a 3","Rolling a 6"], answer:1},
     {q:"Probability can be expressed as a fraction. If 3 of 10 marbles are yellow, P(yellow) = ?", options:["1/3","3/10","7/10","10/3"], answer:1}
   ]},
  {subject:"Science", title:"Physical and Chemical Changes", summary:"Grade 4 Science Materials strand: a physical change alters the form but not the substance (e.g., cutting). A chemical change produces a new substance (e.g., burning).",
   resourceLabel:"YouTube: Physical and Chemical Changes", resourceUrl:"https://www.youtube.com/results?search_query=Physical%20and%20Chemical%20Changes%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=joT50SYQctc",
   quiz:[
     {q:"A physical change ___.", options:["creates a new substance","changes the form but not the substance","is irreversible","involves burning"], answer:2},
     {q:"A chemical change ___.", options:["is always reversible","only changes shape","produces a new substance","is the same as melting"], answer:2},
     {q:"Which is a PHYSICAL change?", options:["Baking a cake","Cutting paper","Rusting iron","Burning wood"], answer:1},
     {q:"Which is a CHEMICAL change?", options:["Tearing paper","Dissolving salt in water","Burning candle wax","Melting ice"], answer:2},
     {q:"Which observation suggests a CHEMICAL change has occurred?", options:["Change in location","Colour change, gas, or heat","Change in size","Change in shape"], answer:1}
   ]},
  {subject:"SocialStudies", title:"First Nations Treaties in Canada", summary:"Grade 4 Social Studies: treaties are agreements between the Crown and First Nations peoples. They were meant to share land but were often not honoured by the government.",
   resourceLabel:"YouTube: First Nations Treaties in Canada", resourceUrl:"https://www.youtube.com/results?search_query=First%20Nations%20Treaties%20in%20Canada%20grade%204%20educational",
   quiz:[
     {q:"A treaty is ___.", options:["a type of building","a style of artwork","a formal agreement between parties","a type of land"], answer:2},
     {q:"Treaties between First Nations and the Crown involved ___.", options:["sharing land and defining rights","only religion","only money","only sharing food"], answer:0},
     {q:"Many treaties were NOT honoured by the government, which led to ___.", options:["loss of land and rights","more treaties being made quickly","stronger First Nations communities","peace and prosperity"], answer:0},
     {q:"Today, treaties are ___.", options:["only museum pieces","still legally binding today","only used in schools","forgotten documents"], answer:1},
     {q:"Learning about treaties helps Canadians ___.", options:["understand history and reconciliation","ignore Indigenous history","focus only on recent history","avoid the topic"], answer:0}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"Language", title:"Grammar: Pronouns and Antecedents", summary:"Grade 4 Language strand: a pronoun replaces a noun (the antecedent). The pronoun must agree with its antecedent in number and gender.",
   resourceLabel:"YouTube: Grammar: Pronouns and Antecedents", resourceUrl:"https://www.youtube.com/results?search_query=Grammar%3A%20Pronouns%20and%20Antecedents%20grade%204%20educational",
   quiz:[
     {q:"A pronoun takes the place of a ___.", options:["noun","adjective","verb","conjunction"], answer:0},
     {q:"The word a pronoun refers back to is called the ___.", options:["object","subject","antecedent","predicate"], answer:2},
     {q:"In 'Maria took her book,' 'her' refers to ___.", options:["the book","Maria","another girl","a third person"], answer:1},
     {q:"Which pronoun agrees with 'students' (plural)?", options:["they","she","it","he"], answer:0},
     {q:"Pronouns must agree with their antecedent in ___ and ___.", options:["place and time","size and colour","number and gender","subject and object"], answer:2}
   ]},
  {subject:"Math", title:"3-Digit × 1-Digit Multiplication", summary:"Grade 4 Number strand: multiply 3-digit numbers by 1-digit numbers using expanded form and the standard algorithm.",
   resourceLabel:"YouTube: 3-Digit × 1-Digit Multiplication", resourceUrl:"https://www.youtube.com/results?search_query=3-Digit%20%C3%97%201-Digit%20Multiplication%20grade%204%20educational",
   quiz:[
     {q:"213 × 3 = ?", options:["639","609","619","649"], answer:0},
     {q:"145 × 4 = ?", options:["580","560","620","590"], answer:0},
     {q:"To solve 234 × 5, you can expand: (200×5) + (30×5) + (4×5) = ?", options:["1200","1070","1170","1140"], answer:2},
     {q:"326 × 3 = ?", options:["968","958","978","998"], answer:2},
     {q:"Which strategy helps check a multiplication answer?", options:["Subtracting","Dividing the answer by the same number","Guessing","Adding"], answer:1}
   ]},
  {subject:"Science", title:"Weather Patterns and Water Cycle", summary:"Grade 4 Science Earth strand: the water cycle involves evaporation, condensation, and precipitation. Weather is caused by movements of air masses.",
   resourceLabel:"YouTube: Weather Patterns and Water Cycle", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20Patterns%20and%20Water%20Cycle%20grade%204%20educational",
   quiz:[
     {q:"What powers the water cycle?", options:["The wind alone","The moon's gravity","Human activity","The sun's energy evaporating water"], answer:3},
     {q:"Evaporation is when water changes from a liquid to a ___.", options:["solid","plasma","gas","crystal"], answer:2},
     {q:"Condensation is when water vapour changes to ___.", options:["ice","liquid water (forming clouds and dew)","rock","salt"], answer:1},
     {q:"Precipitation includes ___.", options:["evaporation and condensation","only rain","rain, snow, sleet, and hail","only snow"], answer:2},
     {q:"Which instrument measures precipitation?", options:["Rain gauge","Anemometer","Thermometer","Barometer"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Colonial Canada", summary:"Grade 4 Social Studies: colonial Canada (1600s–1867) was shaped by French and British settlers, the fur trade, and conflicts with and among Indigenous peoples.",
   resourceLabel:"YouTube: Colonial Canada", resourceUrl:"https://www.youtube.com/results?search_query=Colonial%20Canada%20grade%204%20educational",
   quiz:[
     {q:"New France was the name for ___.", options:["Modern Quebec only","British settlements in Canada","Indigenous territories","French territory in North America"], answer:3},
     {q:"The fur trade was important because ___.", options:["It was only about clothing","It connected two peoples economically","Only Europeans benefited","Only Indigenous peoples benefited"], answer:1},
     {q:"The Acadian people were ___.", options:["American colonists","Indigenous peoples","British settlers in Nova Scotia","French settlers in Atlantic Canada"], answer:3},
     {q:"When did Canada become a country?", options:["1492","1914","1759","1867"], answer:3},
     {q:"The British North America Act (1867) created ___.", options:["New France","The Dominion of Canada (Confederation)","The fur trade","The Indian Act"], answer:1}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"Language", title:"Reading: Text Features in Non-Fiction", summary:"Grade 4 Reading strand: non-fiction text features include headings, subheadings, captions, text boxes, bold words, table of contents, index, and glossary.",
   resourceLabel:"YouTube: Reading: Text Features in Non-Fiction", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Text%20Features%20in%20Non-Fiction%20grade%204%20educational",
   quiz:[
     {q:"A subheading in a text ___.", options:["is unrelated to the text","is the author's name","organizes info by labelling a section","introduces the whole article"], answer:2},
     {q:"A glossary provides ___.", options:["definitions of key words","the author's biography","an index of pages","pictures"], answer:0},
     {q:"An index helps readers ___.", options:["read captions","understand definitions","see the table of contents","find topics by page number"], answer:3},
     {q:"Bold words in a text usually indicate ___.", options:["important vocabulary terms","errors","unrelated information","the author's favourite words"], answer:0},
     {q:"Text boxes in non-fiction ___.", options:["replace the main text","are errors","provide extra related information","are always statistics"], answer:2}
   ]},
  {subject:"Math", title:"Elapsed Time", summary:"Grade 4 Measurement strand: elapsed time is the amount of time that passes between a start time and an end time.",
   resourceLabel:"YouTube: Elapsed Time", resourceUrl:"https://www.youtube.com/results?search_query=Elapsed%20Time%20grade%204%20educational",
   quiz:[
     {q:"A movie starts at 2:15 p.m. and ends at 4:45 p.m. How long is it?", options:["2 hours 45 min","2 hours 30 min","2 hours 15 min","3 hours"], answer:1},
     {q:"School starts at 8:30 a.m. and ends at 3:15 p.m. Total school time = ?", options:["6 h 15 min","7 h 15 min","7 h 45 min","6 h 45 min"], answer:3},
     {q:"3:00 p.m. + 2 hours 40 minutes = ?", options:["5:40 p.m.","6:00 p.m.","5:00 p.m.","4:40 p.m."], answer:0},
     {q:"A task starts at 10:45 a.m. and takes 1 h 30 min. It ends at?", options:["11:15 a.m.","11:45 a.m.","12:15 p.m.","12:45 p.m."], answer:2},
     {q:"How many minutes are in 2 hours 15 minutes?", options:["115","135","125","145"], answer:1}
   ]},
  {subject:"Science", title:"Space: The Solar System", summary:"Grade 4 Science Earth strand: our solar system has the Sun at its centre and 8 planets, plus moons, asteroids, and comets orbiting it.",
   resourceLabel:"YouTube: Space: The Solar System", resourceUrl:"https://www.youtube.com/results?search_query=Space%3A%20The%20Solar%20System%20grade%204%20educational",
   quiz:[
     {q:"How many planets are in our solar system?", options:["9","7","8","10"], answer:2},
     {q:"What is at the centre of our solar system?", options:["The Moon","The Sun","Earth","Jupiter"], answer:1},
     {q:"Which is the largest planet?", options:["Saturn","Earth","Neptune","Jupiter"], answer:3},
     {q:"Planets closer to the Sun are generally ___.", options:["warmer","colder","made of gas","invisible"], answer:0},
     {q:"Which planet is closest to the Sun?", options:["Earth","Venus","Mercury","Mars"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Confederation and Canadian Identity", summary:"Grade 4 Social Studies: Confederation (1867) united four provinces into the Dominion of Canada. Canadian identity includes bilingualism, multiculturalism, and respect for Indigenous peoples.",
   resourceLabel:"YouTube: Confederation and Canadian Identity", resourceUrl:"https://www.youtube.com/results?search_query=Confederation%20and%20Canadian%20Identity%20grade%204%20educational",
   quiz:[
     {q:"Confederation in 1867 united which four provinces?", options:["BC, AB, ON, QC","ON, QC, NB, NS","NL, PE, NB, NS","MB, SK, AB, BC"], answer:1},
     {q:"Canadian identity is shaped by ___.", options:["only British traditions","only geography","only one cultural group","many heritages, old and new"], answer:3},
     {q:"What does 'bilingual' mean in Canada's context?", options:["English and French are both official","Only Quebec speaks French","Everyone speaks English","Speaking three languages"], answer:0},
     {q:"Canada became officially multicultural by law in ___.", options:["1931","2000","1867","1971 (Policy) / 1988 (Act)"], answer:3},
     {q:"Canadian identity includes ___.", options:["only British traditions","only French culture","only hockey and maple syrup","diversity, democracy, and rule of law"], answer:3}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"Language", title:"Writing: Summary Writing", summary:"Grade 4 Writing strand: a summary is a brief restatement of the most important ideas in a text, using your own words. It does not include personal opinions.",
   resourceLabel:"YouTube: Writing: Summary Writing", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Summary%20Writing%20grade%204%20educational",
   videoUrl:"https://www.youtube.com/watch?v=CUbKpjQMM0w",
   quiz:[
     {q:"A summary ___.", options:["is longer than the original","restates the main ideas briefly","includes your personal opinions","retells every detail of a text"], answer:1},
     {q:"When writing a summary, you should ___.", options:["copy the original text word for word","add your own new ideas","include only the main points and key supporting ideas","include all details"], answer:3},
     {q:"A summary should be ___.", options:["shorter than the original","any length","longer than the original text","the same length as the original"], answer:0},
     {q:"Which is NOT appropriate in a summary?", options:["The main idea","Key supporting details","Your personal opinion or new information","The author's conclusion"], answer:2},
     {q:"To summarize means to ___.", options:["state briefly and in your own words","evaluate critically","copy directly","analyze in depth"], answer:0}
   ]},
  {subject:"Math", title:"Equivalent Fractions", summary:"Grade 4 Number strand: equivalent fractions represent the same value even though they have different numerators and denominators. Example: 1/2 = 2/4 = 4/8.",
   resourceLabel:"YouTube: Equivalent Fractions", resourceUrl:"https://www.youtube.com/results?search_query=Equivalent%20Fractions%20grade%204%20educational",
   quiz:[
     {q:"Which fraction is equivalent to 1/2?", options:["2/3","1/3","3/4","2/4"], answer:3},
     {q:"Which fraction is equivalent to 2/3?", options:["4/6","6/8","4/9","3/4"], answer:0},
     {q:"To find an equivalent fraction, multiply or divide the numerator and denominator by the ___.", options:["different numbers","same number","1","0"], answer:1},
     {q:"Is 3/4 equivalent to 6/8?", options:["Cannot tell","Only sometimes","No","Yes"], answer:3},
     {q:"Simplify 6/9 to its lowest terms.", options:["3/9","2/3","3/4","1/2"], answer:1}
   ]},
  {subject:"Science", title:"Space: Moon Phases", summary:"Grade 4 Science Earth strand: the Moon has no light of its own; it reflects sunlight. As it orbits Earth, we see different amounts of its lit side — the phases.",
   resourceLabel:"YouTube: Space: Moon Phases", resourceUrl:"https://www.youtube.com/results?search_query=Space%3A%20Moon%20Phases%20grade%204%20educational",
   quiz:[
     {q:"The Moon produces its own light.", options:["True","Only in summer","Only at night","False"], answer:3},
     {q:"The Moon phases are caused by ___.", options:["The Moon moving in and out of shadow","Earth blocking sunlight (eclipse)","The Moon changing shape","Varying views of its sunlit side"], answer:3},
     {q:"A 'full moon' occurs when ___.", options:["The Moon is between Earth and the Sun","The Moon is in shadow","We see the entire sunlit face of the Moon","The Moon is at its farthest from Earth"], answer:2},
     {q:"A 'new moon' is when ___.", options:["It is a new month","Its lit side faces away from Earth","The Moon is smallest","We see the entire lit face"], answer:1},
     {q:"The Moon completes one full orbit around Earth in about ___.", options:["365 days","28–29 days","14 days","7 days"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Economics: Needs, Wants, Supply, and Demand", summary:"Grade 4 Social Studies: needs are essentials (food, shelter); wants are desires. Supply is how much is available; demand is how much people want.",
   resourceLabel:"YouTube: Economics: Needs, Wants, Supply, and Demand", resourceUrl:"https://www.youtube.com/results?search_query=Economics%3A%20Needs%2C%20Wants%2C%20Supply%2C%20and%20Demand%20grade%204%20educational",
   quiz:[
     {q:"A 'need' is ___.", options:["a luxury item","something you want but cannot have","something essential for survival","something desirable but not essential"], answer:2},
     {q:"A 'want' is ___.", options:["the same as a need","only food and water","essential for survival","something desirable but not necessary"], answer:3},
     {q:"When demand for a product increases and supply stays the same, prices usually ___.", options:["rise","stay the same","disappear","fall"], answer:0},
     {q:"Supply means ___.", options:["how much of a product is available","the desire for a product","the cost of making something","the price charged"], answer:0},
     {q:"Which is a NEED?", options:["Designer clothing","A new video game","Clean drinking water","A vacation"], answer:2}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"Language", title:"Writing: Procedural Texts", summary:"Grade 4 Writing strand: a procedural text (how-to) explains how to do something in step-by-step order. It uses numbered steps, imperative verbs, and clear language.",
   resourceLabel:"YouTube: Writing: Procedural Texts", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Procedural%20Texts%20grade%204%20educational",
   quiz:[
     {q:"The purpose of a procedural text is to ___.", options:["persuade the reader","entertain with a story","explain how to do or make something","compare two ideas"], answer:2},
     {q:"Procedural texts use ___ verbs.", options:["passive","past tense","imperative (command)","subjunctive"], answer:2},
     {q:"What is essential in a procedural text?", options:["Opinions and feelings","Descriptive language only","Characters and a plot","Steps in sequential order"], answer:3},
     {q:"A materials or ingredients list in a procedural text comes ___.", options:["at the end","in the middle","before the steps","after all the steps"], answer:2},
     {q:"Which sentence from a procedural text uses correct style?", options:["I add the flour.","The flour was added.","Add the flour.","She could add the flour."], answer:2}
   ]},
  {subject:"Math", title:"Geometry: 3D Figures", summary:"Grade 4 Geometry strand: 3D figures have length, width, and height. Key figures: cube, rectangular prism, cylinder, cone, sphere, pyramid.",
   resourceLabel:"YouTube: Geometry: 3D Figures", resourceUrl:"https://www.youtube.com/results?search_query=Geometry%3A%203D%20Figures%20grade%204%20educational",
   quiz:[
     {q:"How many faces does a cube have?", options:["6","4","5","8"], answer:0},
     {q:"A rectangular prism has ___ vertices.", options:["8","6","12","4"], answer:0},
     {q:"Which 3D figure has no edges or vertices?", options:["Cube","Sphere","Cylinder","Cone"], answer:1},
     {q:"A cone has how many curved surface(s)?", options:["3","2","1","0"], answer:2},
     {q:"A triangular pyramid (tetrahedron) has ___ faces.", options:["6","5","3","4"], answer:3}
   ]},
  {subject:"Science", title:"Conservation of Energy", summary:"Grade 4 Science Energy strand: energy cannot be created or destroyed; it can only change form. Examples: electrical → light, chemical (food) → kinetic.",
   resourceLabel:"YouTube: Conservation of Energy", resourceUrl:"https://www.youtube.com/results?search_query=Conservation%20of%20Energy%20grade%204%20educational",
   quiz:[
     {q:"The law of conservation of energy states that energy ___.", options:["is always used up","cannot be created or destroyed","can be created from nothing","disappears when used"], answer:1},
     {q:"When you eat food, chemical energy converts to ___.", options:["nuclear energy","light energy","electrical energy","kinetic (movement) and heat energy"], answer:3},
     {q:"A light bulb converts electrical energy into ___.", options:["mechanical energy","sound energy","chemical energy","light and heat energy"], answer:3},
     {q:"Solar panels convert ___ energy to ___ energy.", options:["kinetic, nuclear","light (solar), electrical","chemical, electrical","sound, light"], answer:1},
     {q:"Which is an example of energy transformation?", options:["A windmill turning wind to electricity","Using a non-electric candle","Turning off all lights","Doing nothing"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Heritage Celebrations", summary:"Grade 4 Social Studies: cultural celebrations reflect the heritage and identity of communities. Understanding different celebrations builds respect and inclusion.",
   resourceLabel:"YouTube: Heritage Celebrations", resourceUrl:"https://www.youtube.com/results?search_query=Heritage%20Celebrations%20grade%204%20educational",
   quiz:[
     {q:"A heritage celebration reflects ___.", options:["only modern pop culture","only sports","only government events","a community's traditions and history"], answer:3},
     {q:"Diwali is the Festival of Lights celebrated primarily by ___.", options:["Hindu, Sikh, and Jain communities","Celtic communities","Indigenous communities","Chinese communities"], answer:0},
     {q:"Chinese New Year is celebrated with ___.", options:["Summer solstice","Building snowmen","parades and fireworks","Thanksgiving food"], answer:2},
     {q:"Why is it important to acknowledge multiple cultural celebrations?", options:["Only tourists need to know","It causes confusion","It promotes understanding and inclusion","It is not important"], answer:2},
     {q:"What is Remembrance Day (November 11)?", options:["A cultural celebration","A harvest festival","A day to honour war veterans","Canada's birthday"], answer:2}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"Language", title:"Grammar: Prepositions", summary:"Grade 4 Language strand: prepositions show the relationship between a noun and another word. Common prepositions: in, on, at, by, under, over, between, through.",
   resourceLabel:"YouTube: Grammar: Prepositions", resourceUrl:"https://www.youtube.com/results?search_query=Grammar%3A%20Prepositions%20grade%204%20educational",
   quiz:[
     {q:"A preposition shows the ___ between words.", options:["relationship, like location or time","sound","colour","size"], answer:0},
     {q:"Which is a preposition in: 'The cat sat on the mat'?", options:["cat","mat","The","on"], answer:3},
     {q:"Which sentence uses a preposition?", options:["Dogs run fast.","The book is on the table.","She is happy.","He jumped high."], answer:1},
     {q:"Which is NOT a preposition?", options:["through","between","under","happy"], answer:3},
     {q:"A preposition is usually followed by a ___.", options:["adjective","verb","adverb","noun or pronoun"], answer:3}
   ]},
  {subject:"Math", title:"Division: 2-Digit Divisor Introduction", summary:"Grade 4 Number strand: students divide larger dividends by 1-digit divisors and are introduced to estimation with division.",
   resourceLabel:"YouTube: Division: 2-Digit Divisor Introduction", resourceUrl:"https://www.youtube.com/results?search_query=Division%3A%202-Digit%20Divisor%20Introduction%20grade%204%20educational",
   quiz:[
     {q:"84 ÷ 4 = ?", options:["21","22","20","19"], answer:0},
     {q:"96 ÷ 8 = ?", options:["12","11","10","13"], answer:0},
     {q:"75 ÷ 5 = ?", options:["16","13","15","14"], answer:2},
     {q:"To check your division, you can ___.", options:["subtract the divisor","add the divisor and quotient","multiply the quotient by the divisor","guess again"], answer:2},
     {q:"Estimate: 78 ÷ 4 is approximately?", options:["30","40","20","10"], answer:2}
   ]},
  {subject:"Science", title:"Sustainable Practices", summary:"Grade 4 Science Life Systems/Materials strand: sustainable practices reduce waste and protect the environment. The 3 Rs: Reduce, Reuse, Recycle.",
   resourceLabel:"YouTube: Sustainable Practices", resourceUrl:"https://www.youtube.com/results?search_query=Sustainable%20Practices%20grade%204%20educational",
   quiz:[
     {q:"Sustainable means ___.", options:["never using resources","using as much as possible","meeting today's needs sustainably","spending less money"], answer:2},
     {q:"Which is a sustainable practice?", options:["Printing one page per word","Leaving lights on","Composting organic waste","Buying single-use plastics"], answer:2},
     {q:"'Reduce' means ___.", options:["finding new uses for old items","throwing away more","recycling materials","using less of something"], answer:3},
     {q:"'Reuse' means ___.", options:["throwing items away after one use","finding new uses for old items","melting and reforming materials","burning waste"], answer:1},
     {q:"Composting converts food scraps into ___.", options:["plastic","medicine","electricity","nutrient-rich soil"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Immigration: Building Canada", summary:"Grade 4 Social Studies: immigrants have come to Canada from all over the world, contributing to its economy, culture, and identity. Immigration continues today.",
   resourceLabel:"YouTube: Immigration: Building Canada", resourceUrl:"https://www.youtube.com/results?search_query=Immigration%3A%20Building%20Canada%20grade%204%20educational",
   quiz:[
     {q:"Why have people immigrated to Canada?", options:["Seeking safety, opportunity, or family","Canada is not a destination","Canada forced them","Only recently has anyone come to Canada"], answer:0},
     {q:"What is a refugee?", options:["A student studying abroad","A tourist who stays","Someone fleeing war or persecution","A wealthy immigrant"], answer:2},
     {q:"Immigrants have contributed to Canada by ___.", options:["only speaking one language","only working in farms","causing problems","building communities and businesses"], answer:3},
     {q:"What is multiculturalism?", options:["Only two cultures existing","A policy recognizing and valuing cultural diversity","Ignoring different cultures","Everyone having the same culture"], answer:1},
     {q:"Why is Canada's multicultural heritage considered a strength?", options:["It is a weakness","Diverse ideas make Canada stronger","Only in cities","Only some Canadians benefit"], answer:1}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"Language", title:"Reading Comprehension Strategies Review", summary:"Grade 4 Reading strand: skilled readers use multiple strategies: predicting, visualising, asking questions, making connections, summarising, and synthesising.",
   resourceLabel:"YouTube: Reading Comprehension Strategies Review", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20Comprehension%20Strategies%20Review%20grade%204%20educational",
   quiz:[
     {q:"Visualising while reading means ___.", options:["writing notes","looking at the illustrations only","drawing pictures in a book","creating mental images of the text"], answer:3},
     {q:"Asking questions before and during reading helps ___.", options:["set a purpose and deepen understanding","avoid the text entirely","slow down your reading","only find main ideas"], answer:0},
     {q:"A text-to-world connection is ___.", options:["connecting the text to your personal experience","connecting the text to another book","connecting the text to what you know about the world","connecting to a film"], answer:2},
     {q:"Synthesising information means ___.", options:["only summarising","copying text exactly","combining sources into new understanding","restating information unchanged"], answer:2},
     {q:"Which strategy is best for an unfamiliar word?", options:["Ask someone immediately without trying","Stop reading","Use context clues to find the meaning","Skip it"], answer:2}
   ]},
  {subject:"Math", title:"Review: Number Sense and Operations", summary:"Grade 4 Number strand review: students demonstrate fluency with multiplication, division, fractions, and decimals.",
   resourceLabel:"YouTube: Review: Number Sense and Operations", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Number%20Sense%20and%20Operations%20grade%204%20educational",
   quiz:[
     {q:"345 × 4 = ?", options:["1360","1380","1390","1370"], answer:1},
     {q:"96 ÷ 6 = ?", options:["16","14","17","15"], answer:0},
     {q:"1/2 + 1/2 = ?", options:["2","1","1/2","1/4"], answer:1},
     {q:"0.3 + 0.6 = ?", options:["0.9","0.7","0.8","1.0"], answer:0},
     {q:"Which fraction is between 1/4 and 3/4?", options:["1/8","1/4","1/2","7/8"], answer:2}
   ]},
  {subject:"Science", title:"Year Review: Science Concepts", summary:"Grade 4 Science strand review: habitats, rocks, energy (light, sound, electricity), weather, and space.",
   resourceLabel:"YouTube: Year Review: Science Concepts", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Science%20Concepts%20grade%204%20educational",
   quiz:[
     {q:"A food web shows ___.", options:["the structure of rock layers","how energy flows through food chains","the rock cycle","the water cycle"], answer:1},
     {q:"Igneous rock forms from ___.", options:["sediment layers","compressed sediment","heat and pressure on existing rock","cooled magma/lava"], answer:3},
     {q:"Which is a chemical change?", options:["Melting ice","Cutting paper","Burning wood","Dissolving sugar in water"], answer:2},
     {q:"The Moon reflects ___.", options:["starlight","its own light","earthlight","sunlight"], answer:3},
     {q:"Sound travels fastest through ___.", options:["water","solid materials","air","a vacuum"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Social Studies Year Review", summary:"Grade 4 Social Studies review: ancient civilizations, Canadian history, geography, government, economics, and citizenship.",
   resourceLabel:"YouTube: Social Studies Year Review", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Year%20Review%20grade%204%20educational",
   quiz:[
     {q:"Which ancient civilization developed democracy?", options:["China","Greece","Egypt","Rome"], answer:1},
     {q:"Confederation in 1867 formed which country?", options:["The Dominion of Canada","New France","The British Empire","The United States"], answer:0},
     {q:"Canada has ___ provinces and ___ territories.", options:["9, 4","10, 4","10, 3","8, 4"], answer:2},
     {q:"What is the main purpose of a government?", options:["Entertain citizens","Only fight wars","Organize society and make laws","Only collect taxes"], answer:2},
     {q:"Which is a right of Canadian citizens?", options:["Free speech and equality under the law","Destroying property","Ignoring all rules","Having unlimited money"], answer:0}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"Language", title:"Vocabulary Review and Word Study", summary:"Grade 4 Language strand review: students apply knowledge of synonyms, antonyms, prefixes, suffixes, context clues, and figurative language.",
   resourceLabel:"YouTube: Vocabulary Review and Word Study", resourceUrl:"https://www.youtube.com/results?search_query=Vocabulary%20Review%20and%20Word%20Study%20grade%204%20educational",
   quiz:[
     {q:"The prefix 'un-' in 'unhappy' means ___.", options:["very","not","again","before"], answer:1},
     {q:"The suffix '-less' in 'hopeless' means ___.", options:["before","full of","again","not/without"], answer:3},
     {q:"A simile uses ___ to compare.", options:["only nouns","verb to be","is/was","like or as"], answer:3},
     {q:"A metaphor ___ uses like or as.", options:["sometimes","rarely","always","never"], answer:3},
     {q:"Synonym for 'ancient' = ?", options:["new","young","modern","old/historic"], answer:3}
   ]},
  {subject:"Math", title:"Coordinate Grid", summary:"Grade 4 Geometry strand: students locate and plot points on a coordinate grid using ordered pairs (x, y). The x-axis is horizontal; y-axis is vertical.",
   resourceLabel:"YouTube: Coordinate Grid", resourceUrl:"https://www.youtube.com/results?search_query=Coordinate%20Grid%20grade%204%20educational",
   quiz:[
     {q:"In an ordered pair (3, 5), which number is the x-coordinate?", options:["Neither","Both","5","3"], answer:3},
     {q:"The x-axis is ___.", options:["diagonal","curved","vertical","horizontal"], answer:3},
     {q:"To plot the point (4, 2), you move ___ right and ___ up.", options:["2 right, 4 up","2 up, 4 right","4 up, 2 right","4 right, 2 up"], answer:3},
     {q:"The origin of a coordinate grid is at ___.", options:["(0, 1)","(0, 0)","(1, 0)","(1, 1)"], answer:1},
     {q:"Which point is on the y-axis?", options:["(2, 2)","(5, 1)","(3, 0)","(0, 4)"], answer:3}
   ]},
  {subject:"Science", title:"Review: Ecosystems and Life Systems", summary:"Grade 4 Science review: habitats, communities, adaptations, biodiversity, human impact, and conservation.",
   resourceLabel:"YouTube: Review: Ecosystems and Life Systems", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Ecosystems%20and%20Life%20Systems%20grade%204%20educational",
   quiz:[
     {q:"All the organisms in a shared habitat form a ___.", options:["food chain","ecosystem only","population","community"], answer:3},
     {q:"An adaptation helps an organism ___.", options:["stay sick","survive in its environment","leave its habitat","avoid reproduction"], answer:1},
     {q:"Biodiversity is important because ___.", options:["only scientists care","diverse ecosystems are more resilient","it wastes resources","it is not"], answer:1},
     {q:"Which action BEST protects biodiversity?", options:["Creating wildlife corridors","Draining wetlands","Introducing invasive species","Building highways through forests"], answer:0},
     {q:"The rock cycle shows that rock can transform from ___.", options:["only igneous to metamorphic","only sedimentary to igneous","nothing changes","any rock type to another over time"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Review: Government and Citizenship", summary:"Grade 4 Social Studies review: types of government, rights, responsibilities, Canadian law, and civic participation.",
   resourceLabel:"YouTube: Review: Government and Citizenship", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Government%20and%20Citizenship%20grade%204%20educational",
   quiz:[
     {q:"A democracy is a government where ___.", options:["the military runs everything","leaders are chosen through elections","the monarch holds all power","religious leaders rule"], answer:1},
     {q:"The Canadian Charter of Rights and Freedoms protects ___.", options:["rights of everyone in Canada","only English Canadians","only the rights of the government","only French Canadians"], answer:0},
     {q:"Civic responsibility includes ___.", options:["only paying taxes when asked","never volunteering","voting and following laws","ignoring local issues"], answer:2},
     {q:"Why is an independent judiciary important?", options:["It makes laws more expensive","Only lawyers care","It is not","It keeps laws fair and checks power"], answer:3},
     {q:"Canada's head of government is ___.", options:["The King/Queen","The Chief Justice","The Prime Minister","The Governor General"], answer:2}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"Language", title:"Reading: Author's Purpose", summary:"Grade 4 Reading strand: the author's purpose is the reason for writing — to persuade, inform, or entertain (PIE). Identifying it helps comprehension.",
   resourceLabel:"YouTube: Reading: Author's Purpose", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Author%27s%20Purpose%20grade%204%20educational",
   quiz:[
     {q:"The three common author's purposes are ___.", options:["beginning, middle, end","past, present, future","fact, fiction, opinion","persuade, inform, entertain"], answer:3},
     {q:"A newspaper article about a hurricane has the purpose to ___.", options:["persuade","only describe","entertain","inform"], answer:3},
     {q:"A commercial trying to sell shoes has the purpose to ___.", options:["inform","describe","entertain","persuade"], answer:3},
     {q:"A funny picture book has the purpose to ___.", options:["persuade","instruct","inform","entertain"], answer:3},
     {q:"Identifying author's purpose helps readers ___.", options:["read faster","skip reading strategies","understand why a text was written","find the plot"], answer:2}
   ]},
  {subject:"Math", title:"Review: Measurement", summary:"Grade 4 Measurement review: length, mass, volume, elapsed time, area, and perimeter.",
   resourceLabel:"YouTube: Review: Measurement", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Measurement%20grade%204%20educational",
   quiz:[
     {q:"Area of a rectangle 9 cm × 5 cm = ?", options:["40 cm²","50 cm²","45 cm²","14 cm²"], answer:2},
     {q:"Perimeter of a square with side 8 cm = ?", options:["16 cm","32 cm","64 cm","8 cm"], answer:1},
     {q:"1 kg = ___ g.", options:["1000","10","10000","100"], answer:0},
     {q:"A task from 9:20 a.m. to 11:05 a.m. takes?", options:["2 h 5 min","1 h 45 min","2 h 15 min","1 h 35 min"], answer:1},
     {q:"Convert 4500 mL to litres.", options:["0.45 L","450 L","4.5 L","45 L"], answer:2}
   ]},
  {subject:"Science", title:"Review: Energy Forms and Changes", summary:"Grade 4 Science Energy review: light, sound, electricity, circuits, forces, simple machines.",
   resourceLabel:"YouTube: Review: Energy Forms and Changes", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Energy%20Forms%20and%20Changes%20grade%204%20educational",
   quiz:[
     {q:"Which is an example of electrical energy converting to light?", options:["Burning a candle","A light bulb glowing","A fan spinning","Falling water"], answer:1},
     {q:"Friction creates ___.", options:["cold","static only","more gravity","heat and slows objects"], answer:3},
     {q:"A complete circuit needs a power source, ___, and a load.", options:["insulator","vacuum","conductor/wire","water"], answer:2},
     {q:"Refraction occurs when light passes from one ___ to another.", options:["medium","colour","source","direction"], answer:0},
     {q:"Sound travels as ___ waves.", options:["transverse","compression (longitudinal)","light","electromagnetic"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Review: Ancient Civilizations", summary:"Grade 4 Social Studies review: Egypt, Greece, Rome, and their contributions to modern society.",
   resourceLabel:"YouTube: Review: Ancient Civilizations", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Ancient%20Civilizations%20grade%204%20educational",
   quiz:[
     {q:"Hieroglyphics were used in ___.", options:["China","Egypt","Greece","Rome"], answer:1},
     {q:"Democracy was developed in ___.", options:["Athens, Greece","Egypt","Mesopotamia","Rome"], answer:0},
     {q:"The Roman contribution of ___ influences modern law and government.", options:["hieroglyphics","legal and governmental systems","the Olympic Games","papyrus"], answer:1},
     {q:"Which civilization used the Silk Road for trade?", options:["Ancient Rome","Ancient China and Rome both used it","Ancient Egypt","Ancient Greece"], answer:1},
     {q:"Which ancient civilization was located in present-day Italy?", options:["Mesopotamia","Greece","Egypt","Rome"], answer:3}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"Language", title:"Writing: Editing and Proofreading", summary:"Grade 4 Writing strand: editing focuses on content and organization; proofreading focuses on spelling, grammar, and punctuation. Both improve the final piece.",
   resourceLabel:"YouTube: Writing: Editing and Proofreading", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20Editing%20and%20Proofreading%20grade%204%20educational",
   quiz:[
     {q:"Editing involves ___.", options:["improving content and structure","only punctuation","fixing spelling mistakes","copying neatly"], answer:0},
     {q:"Proofreading involves ___.", options:["only capitals","rewriting the whole piece","checking for spelling, grammar, and punctuation errors","adding new ideas"], answer:3},
     {q:"The acronym COPS (Capitals, Organization, Punctuation, Spelling) is a ___.", options:["paragraph structure","proofreading checklist","story type","writing style"], answer:1},
     {q:"Why is revising and editing important?", options:["Writing is always perfect first time","It is not","Only teachers need to edit","It improves quality for the reader"], answer:3},
     {q:"Which should you do first: edit content or proofread?", options:["Edit content first, then details","Do both at exactly the same time","Proofread first","Do neither"], answer:0}
   ]},
  {subject:"Math", title:"Review: Data and Probability", summary:"Grade 4 Data review: tally charts, bar graphs, line graphs, pictographs, and probability.",
   resourceLabel:"YouTube: Review: Data and Probability", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Data%20and%20Probability%20grade%204%20educational",
   quiz:[
     {q:"Which graph is BEST for showing change over time?", options:["Pictograph","Line graph","Tally chart","Bar graph"], answer:1},
     {q:"Which graph is BEST for comparing categories at one time?", options:["Bar graph","Scatter plot","None","Line graph"], answer:0},
     {q:"P(rolling 6 on a fair die) = ?", options:["1/6","2/6","1/3","1/2"], answer:0},
     {q:"P(picking red from 3 red and 7 blue) = ?", options:["10/3","7/10","3/10","3/7"], answer:2},
     {q:"The mode of a data set is ___.", options:["the most frequent value","the range","the middle value","the average"], answer:0}
   ]},
  {subject:"Science", title:"Review: Materials and Earth", summary:"Grade 4 Science review: rocks, minerals, soil, mixtures, solutions, physical/chemical changes, and the rock cycle.",
   resourceLabel:"YouTube: Review: Materials and Earth", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Materials%20and%20Earth%20grade%204%20educational",
   quiz:[
     {q:"The three rock types are ___.", options:["volcanic, beach, mountain","hard, soft, medium","granite, marble, slate","igneous, sedimentary, metamorphic"], answer:3},
     {q:"A solution differs from a mixture because ___.", options:["the solute dissolves completely","mixtures are permanent","solutions always involve water","they are the same"], answer:0},
     {q:"Which is a physical change?", options:["Baking bread","Tearing paper into smaller pieces","Burning paper","Rusting iron"], answer:1},
     {q:"Soil is made of ___.", options:["only compost","only sand","rock particles, matter, air, and water","only clay"], answer:2},
     {q:"The rock cycle is driven by ___.", options:["only volcanoes","the water cycle","heat, pressure, and weathering","only wind and rain"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Review: Canada's History and Geography", summary:"Grade 4 Social Studies review: Canadian geography, exploration, Indigenous peoples, Confederation, and citizenship.",
   resourceLabel:"YouTube: Review: Canada's History and Geography", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Canada%27s%20History%20and%20Geography%20grade%204%20educational",
   quiz:[
     {q:"Confederation year?", options:["1914","1776","1867","1759"], answer:2},
     {q:"Canada has ___ official languages.", options:["4","1","2","3"], answer:2},
     {q:"The largest province by area is ___.", options:["Ontario","Quebec","Alberta","British Columbia"], answer:1},
     {q:"Treaties between the Crown and First Nations are ___.", options:["only about money","old and irrelevant","still legally binding","fiction"], answer:2},
     {q:"What is the Canadian Charter of Rights and Freedoms?", options:["A trading document","A municipal bylaw","A children's story","A document protecting everyone's rights"], answer:3}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"Language", title:"Grammar Review", summary:"Grade 4 Language strand comprehensive grammar review: parts of speech, sentence types, punctuation, and sentence construction.",
   resourceLabel:"YouTube: Grammar Review", resourceUrl:"https://www.youtube.com/results?search_query=Grammar%20Review%20grade%204%20educational",
   quiz:[
     {q:"Which sentence is a compound sentence?", options:["She is happy.","Running fast.","The dog runs.","I wanted to go, but it was raining."], answer:3},
     {q:"A complex sentence contains ___.", options:["only a dependent clause","two independent clauses","no verbs","an independent and a dependent clause"], answer:3},
     {q:"Which punctuation separates items in a list?", options:["Question mark","Comma","Period","Exclamation mark"], answer:1},
     {q:"What is a clause?", options:["A group of words with a subject and verb","Only a dependent phrase","A word with a prefix","A type of word"], answer:0},
     {q:"An independent clause ___.", options:["has no verb","can stand alone as a complete sentence","cannot stand alone","depends on another clause"], answer:1}
   ]},
  {subject:"Math", title:"Math Review: All Strands", summary:"Grade 4 Mathematics comprehensive review covering number, geometry, measurement, patterning, and data.",
   resourceLabel:"YouTube: Math Review: All Strands", resourceUrl:"https://www.youtube.com/results?search_query=Math%20Review%3A%20All%20Strands%20grade%204%20educational",
   quiz:[
     {q:"7 × 9 = ?", options:["56","54","63","64"], answer:2},
     {q:"Area of 6 cm × 8 cm rectangle = ?", options:["14 cm²","28 cm²","48 cm²","42 cm²"], answer:2},
     {q:"What is the next number? 3, 6, 12, 24, ___", options:["30","48","36","42"], answer:1},
     {q:"Which fraction is greater: 3/4 or 5/8?", options:["Cannot tell","3/4","Equal","5/8"], answer:1},
     {q:"0.45 + 0.35 = ?", options:["0.90","0.80","0.70","0.75"], answer:1}
   ]},
  {subject:"Science", title:"Science Review: All Strands", summary:"Grade 4 Science comprehensive review across life, earth, materials, and energy strands.",
   resourceLabel:"YouTube: Science Review: All Strands", resourceUrl:"https://www.youtube.com/results?search_query=Science%20Review%3A%20All%20Strands%20grade%204%20educational",
   quiz:[
     {q:"What is biodiversity?", options:["A food chain","A weather pattern","A type of rock","The variety of life in an ecosystem"], answer:3},
     {q:"Which rock forms from cooled magma?", options:["Igneous","Limestone","Metamorphic","Sedimentary"], answer:0},
     {q:"A complete circuit requires ___.", options:["only wires","only a battery","power source, conductor, and a load","a magnet"], answer:2},
     {q:"The Moon's phases are caused by ___.", options:["the Moon changing shape","The Sun moving","Varying views of its sunlit side","Earth's shadow"], answer:2},
     {q:"Conservation of energy means energy ___.", options:["cannot be created or destroyed","increases when heated","is created by machines","disappears when used"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Social Studies Review: All Topics", summary:"Grade 4 Social Studies comprehensive review across heritage, identity, government, and geography strands.",
   resourceLabel:"YouTube: Social Studies Review: All Topics", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Review%3A%20All%20Topics%20grade%204%20educational",
   quiz:[
     {q:"Which ancient civilization developed the Olympic Games?", options:["Egypt","Greece","Rome","China"], answer:1},
     {q:"Canada became a country through ___.", options:["a revolution","winning a war","Confederation in 1867","being given independence"], answer:2},
     {q:"Why are treaties important today?", options:["Only in Quebec","Only in the 1800s","They are not","They define legally binding land rights"], answer:3},
     {q:"Sustainable resource use means ___.", options:["using all resources now","never using resources","saving resources for future generations","only using renewable energy"], answer:2},
     {q:"Canada's multicultural heritage is ___.", options:["irrelevant today","a strength that enriches society","only for big cities","a weakness"], answer:1}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"Language", title:"Language Arts: Oral Communication", summary:"Grade 4 Language strand: oral communication includes speaking clearly, listening actively, presenting ideas, and participating respectfully in discussions.",
   resourceLabel:"YouTube: Language Arts: Oral Communication", resourceUrl:"https://www.youtube.com/results?search_query=Language%20Arts%3A%20Oral%20Communication%20grade%204%20educational",
   quiz:[
     {q:"Active listening means ___.", options:["looking away","waiting for your turn to talk only","interrupting to add ideas","paying attention and eye contact"], answer:3},
     {q:"When presenting to a class, you should ___.", options:["speak very quietly","speak clearly, make eye contact, and organize your ideas","go as fast as possible","read directly from notes without looking up"], answer:3},
     {q:"Constructive feedback is ___.", options:["ignoring what someone said","only positive comments","only negative comments","specific, kind, and helpful suggestions"], answer:3},
     {q:"A debate involves ___.", options:["one person speaking alone","sharing feelings only","choosing sides and arguing your case","only asking questions"], answer:2},
     {q:"Why is oral communication important?", options:["It helps in school, work, and life","Only for presentations","Computers do all communication now","Only writing matters"], answer:0}
   ]},
  {subject:"Math", title:"Math: Problem Solving Strategies", summary:"Grade 4 Mathematics: students apply strategies like drawing diagrams, making tables, working backwards, and looking for patterns to solve multi-step problems.",
   resourceLabel:"YouTube: Math: Problem Solving Strategies", resourceUrl:"https://www.youtube.com/results?search_query=Math%3A%20Problem%20Solving%20Strategies%20grade%204%20educational",
   quiz:[
     {q:"Working backwards is a useful strategy when you know ___.", options:["a middle step","nothing about the problem","the starting conditions","the end result and need the start"], answer:3},
     {q:"Making a table helps to ___.", options:["organize data to find a pattern","draw a picture","multiply numbers","avoid solving a problem"], answer:0},
     {q:"A multi-step problem requires ___.", options:["only one operation","two or more steps to solve","reading once and guessing","a calculator always"], answer:1},
     {q:"Drawing a diagram helps to ___.", options:["only geometry problems","skip the calculation","visualize the problem to solve it","decorate your work"], answer:2},
     {q:"Looking for a pattern helps you ___.", options:["only in number sense","predict what comes next","skip the work","guess randomly"], answer:1}
   ]},
  {subject:"Science", title:"Science: Inquiry and STEM Connections", summary:"Grade 4 Science: scientific inquiry involves asking questions, making hypotheses, testing, recording, and forming conclusions. STEM connects science, technology, engineering, and math.",
   resourceLabel:"YouTube: Science: Inquiry and STEM Connections", resourceUrl:"https://www.youtube.com/results?search_query=Science%3A%20Inquiry%20and%20STEM%20Connections%20grade%204%20educational",
   quiz:[
     {q:"A hypothesis is ___.", options:["a proven fact","a conclusion","an educated guess based on knowledge","a question"], answer:2},
     {q:"In an experiment, the variable you change is the ___.", options:["constant","dependent variable","controlled variable","independent variable"], answer:3},
     {q:"The dependent variable is ___.", options:["the materials list","what you change","what you measure (the result)","what you keep the same"], answer:2},
     {q:"A conclusion should ___.", options:["list materials","be written before the experiment","introduce a new idea","state if the hypothesis was supported"], answer:3},
     {q:"STEM stands for ___.", options:["Society, Technology, Economics, Medicine","Science, Technology, Engineering, Mathematics","Science, Tests, Experiments, Methods","Science, Teaching, Energy, Mathematics"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Culminating Task: Community Action Plan", summary:"Grade 4 Social Studies: students apply knowledge of communities, environment, rights, and citizenship to develop a local action plan addressing a community issue.",
   resourceLabel:"YouTube: Culminating Task: Community Action Plan", resourceUrl:"https://www.youtube.com/results?search_query=Culminating%20Task%3A%20Community%20Action%20Plan%20grade%204%20educational",
   quiz:[
     {q:"A community action plan addresses ___.", options:["a local issue with realistic solutions","only school issues","only global issues","only government problems"], answer:0},
     {q:"When presenting a community plan, you should include ___.", options:["only historical information","only pictures","only problems with no solutions","the problem and proposed solutions"], answer:3},
     {q:"Effective community action involves ___.", options:["only money","ignoring different viewpoints","input from community members","only one person deciding"], answer:2},
     {q:"Which is a real example of community action?", options:["Ignoring local pollution","A petition for a new neighbourhood park","Only complaining","Waiting for others to fix issues"], answer:1},
     {q:"Why do citizens need to be active in their community?", options:["It makes communities safer and better","Change is impossible","Only politicians should act","They do not"], answer:0}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"Language", title:"Year Review: Language Arts", summary:"Grade 4 Language Arts comprehensive review covering reading, writing, oral communication, grammar, and media literacy.",
   resourceLabel:"YouTube: Year Review: Language Arts", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Language%20Arts%20grade%204%20educational",
   quiz:[
     {q:"The main idea is ___.", options:["the last sentence","what the whole text is mostly about","a small detail","the title only"], answer:1},
     {q:"A simile uses ___ to compare.", options:["is/was","adjective","metaphor","like or as"], answer:3},
     {q:"An inferring reader ___.", options:["guesses randomly","uses clues to understand unstated ideas","only reads the words on the page","reads very slowly"], answer:1},
     {q:"The purpose of a summary is to ___.", options:["make the text longer","include opinions","briefly restate the main ideas","retell every detail"], answer:2},
     {q:"Editing focuses on ___, while proofreading focuses on ___ .", options:["spelling, content","length, style","grammar, length","content/ideas, then spelling/grammar"], answer:3}
   ]},
  {subject:"Math", title:"Year Review: Mathematics", summary:"Grade 4 Mathematics comprehensive review: all strands.",
   resourceLabel:"YouTube: Year Review: Mathematics", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Mathematics%20grade%204%20educational",
   quiz:[
     {q:"7 × 8 + 4 = ?", options:["56","55","60","52"], answer:2},
     {q:"3/4 is equivalent to ___.", options:["6/10","5/6","6/8","9/16"], answer:2},
     {q:"0.6 + 0.7 = ?", options:["1.0","1.3","1.2","0.13"], answer:1},
     {q:"Area of a 7 cm × 4 cm rectangle = ?", options:["14 cm²","28 cm²","11 cm²","22 cm²"], answer:1},
     {q:"The probability of rolling an even number on a 6-sided die = ?", options:["2/3","1/3","1/2","1/6"], answer:2}
   ]},
  {subject:"Science", title:"Year Review: Science", summary:"Grade 4 Science comprehensive review across all strands.",
   resourceLabel:"YouTube: Year Review: Science", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Science%20grade%204%20educational",
   quiz:[
     {q:"The three rock types are ___.", options:["volcanic, riverbed, mountain","granite, marble, sandstone","igneous, sedimentary, metamorphic","hard, soft, medium"], answer:2},
     {q:"A food chain starts with a ___.", options:["herbivore","decomposer","producer (plant)","carnivore"], answer:2},
     {q:"Refraction is the ___ of light.", options:["speeding up","reflection","bending (change of direction)","absorption"], answer:2},
     {q:"The Moon's phases are caused by ___.", options:["the Moon glowing itself","varying views of the Moon's sunlit side","clouds","seasons"], answer:1},
     {q:"Biodiversity means ___.", options:["all animals being the same","only plants in a habitat","the variety of organisms in an ecosystem","one type of rock"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Year Review: Social Studies", summary:"Grade 4 Social Studies comprehensive review.",
   resourceLabel:"YouTube: Year Review: Social Studies", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Social%20Studies%20grade%204%20educational",
   quiz:[
     {q:"Confederation year = ?", options:["1867","1931","1776","1900"], answer:0},
     {q:"Ancient civilization that developed democracy = ?", options:["China","Greece","Egypt","Rome"], answer:1},
     {q:"Canada has ___ official languages.", options:["2","4","3","1"], answer:0},
     {q:"Rights and responsibilities in a democracy ___.", options:["go together: rights and duties balance","are opposite","only adults have them","are unrelated"], answer:0},
     {q:"Conservation means ___.", options:["only saving money","never using natural resources","wasting resources","using resources wisely for the future"], answer:3}
   ]},
]},
{day:31, label:"Day 31 — Mon", subjects:[
  {subject:"Language", title:"Reading: Fact and Opinion", summary:"Ontario Grade 4 Reading strand: a fact can be proven true or false with evidence, while an opinion expresses a personal belief or judgement that cannot be proven.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Which of these is a fact?", options:["Blue is the nicest colour.","Hockey is the most exciting sport.","Winter is the best season.","Canada has ten provinces."], answer:3},
     {q:"Which of these is an opinion?", options:["A triangle has three sides.","Water boils at 100 degrees Celsius.","Toronto is in Ontario.","Chocolate ice cream is the best flavour."], answer:3},
     {q:"A fact can be described as a statement that ___.", options:["Is always negative","Can be proven true or false","Reflects a personal feeling","Everyone must agree with"], answer:1},
     {q:"Why might two people disagree about an opinion but not a fact?", options:["Opinions can always be proven true","Facts and opinions are exactly the same","Facts change depending on who says them","Opinions are based on personal judgement, while facts can be verified"], answer:3},
     {q:"Which phrase often signals an opinion?", options:["I believe that","According to the data","It was measured that","Research shows"], answer:0}
   ]},
  {subject:"Math", title:"Rounding and Estimating", summary:"Ontario Grade 4 Number strand: rounding numbers to the nearest ten, hundred, or thousand makes estimating sums, differences, and totals faster and easier to check for reasonableness.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"Round 3,482 to the nearest thousand.", options:["4,000","3,000","3,500","3,482"], answer:0},
     {q:"Round 6,251 to the nearest hundred.", options:["6,000","6,300","6,200","6,250"], answer:1},
     {q:"Estimate the sum: 2,890 + 3,150 is approximately ___.", options:["2,800 + 3,100 = 5,900 exactly, no rounding","2,000 + 3,000 = 5,000","10,000","3,000 + 3,000 = 6,000"], answer:3},
     {q:"Why is estimating useful before solving a problem exactly?", options:["It replaces the need to solve the problem","It has no real use in math","It helps you check whether your final answer is reasonable","It always gives the exact answer"], answer:2},
     {q:"Round 749 to the nearest hundred.", options:["750","749","800","700"], answer:2}
   ]},
  {subject:"Science", title:"Species at Risk in Canadian Ecosystems", summary:"Ontario Grade 4 Science Life Systems strand: species at risk are plants or animals in Canada facing possible extinction, often due to habitat loss, pollution, or climate change, and conservation programs work to protect them.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A species at risk is one that is ___.", options:["Facing possible extinction","Found only in aquariums","No longer affected by its environment","Extremely abundant everywhere"], answer:0},
     {q:"Which is a common cause of species becoming at risk?", options:["Too many predators being removed by nature naturally","Nothing affects species survival","Habitat loss","Too much protected land"], answer:2},
     {q:"Which Canadian animal has historically been considered at risk?", options:["Woodland caribou","Raccoon","Common squirrel","House sparrow"], answer:0},
     {q:"Conservation programs for species at risk often involve ___.", options:["Ignoring the issue completely","Removing all environmental laws","Destroying more natural habitat","Protecting habitat and monitoring populations"], answer:3},
     {q:"Why do scientists track species at risk closely?", options:["Only endangered plants are ever tracked","To speed up extinction","To take action before a species disappears entirely","Tracking has no scientific value"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Ancient Mesopotamia", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: Ancient Mesopotamia, located between the Tigris and Euphrates rivers, is considered one of the earliest civilizations, known for early writing, cities, and irrigation systems.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Ancient Mesopotamia developed between which two rivers?", options:["The Amazon and Mississippi","The Ganges and Indus","The Nile and Congo","The Tigris and Euphrates"], answer:3},
     {q:"Mesopotamia is often called one of the earliest ___.", options:["Mountain ranges","Civilizations","Oceans","Deserts"], answer:1},
     {q:"Which early writing system developed in Mesopotamia?", options:["The Latin alphabet","Braille","Hieroglyphics","Cuneiform"], answer:3},
     {q:"Irrigation systems in Mesopotamia were used mainly to ___.", options:["Bring river water to farmland for growing crops","Power early machines","Create early roads","Build pyramids"], answer:0},
     {q:"Why did early civilizations like Mesopotamia often develop near rivers?", options:["Rivers had no practical benefit","Rivers provided water for farming, drinking, and transportation","Rivers were avoided by early people","Rivers made travel impossible"], answer:1}
   ]},
]},
{day:32, label:"Day 32 — Tue", subjects:[
  {subject:"Language", title:"Grammar: Comparative and Superlative Adjectives", summary:"Ontario Grade 4 Writing strand: comparative adjectives (bigger, faster) compare two things, while superlative adjectives (biggest, fastest) compare three or more things, often adding -er or -est.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Which is the comparative form of tall?", options:["Tallest","Tallness","Taller","Tall"], answer:2},
     {q:"Which is the superlative form of fast?", options:["Faster","Fastest","Fast","Fastly"], answer:1},
     {q:"Comparative adjectives are used to compare ___.", options:["One thing only","Nothing at all","Two things","Three or more things"], answer:2},
     {q:"Superlative adjectives are used to compare ___.", options:["Only numbers","Two things only","Three or more things","Only colours"], answer:2},
     {q:"Choose the correct sentence: This is the ___ mountain in the range.", options:["more tall","tall","tallest","taller"], answer:2}
   ]},
  {subject:"Math", title:"Multiplying by 10, 100, and 1,000", summary:"Ontario Grade 4 Number strand: multiplying a whole number by 10, 100, or 1,000 shifts its digits left, adding that many zeros, such as 25 times 100 equals 2,500.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"What is 34 multiplied by 10?", options:["34","34,000","340","3,400"], answer:2},
     {q:"What is 56 multiplied by 100?", options:["5,600","56","560","56,000"], answer:0},
     {q:"What is 7 multiplied by 1,000?", options:["7,000","70","70,000","700"], answer:0},
     {q:"Multiplying by 100 is the same as adding how many zeros?", options:["Two","Three","One","Four"], answer:0},
     {q:"What is 120 multiplied by 10?", options:["12,000","1,200","12","120"], answer:1}
   ]},
  {subject:"Science", title:"Changes of State: Melting, Freezing, and Evaporating", summary:"Ontario Grade 4 Science Matter and Energy strand: matter changes state through processes like melting (solid to liquid), freezing (liquid to solid), and evaporating (liquid to gas), usually caused by adding or removing heat.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Melting occurs when a solid changes into a ___ after gaining heat.", options:["Gas","Liquid","Different solid","Nothing changes"], answer:1},
     {q:"Freezing occurs when a liquid changes into a solid after ___ heat.", options:["Gaining","Creating","Ignoring","Losing"], answer:3},
     {q:"Evaporation occurs when a liquid changes into a ___.", options:["Gas","Different liquid","Solid","Rock"], answer:0},
     {q:"Which is an everyday example of melting?", options:["Water freezing into ice cubes","Steam rising from a lake","Rain falling from clouds","An ice cube turning into water on a warm day"], answer:3},
     {q:"What generally causes a substance to change state?", options:["Adding or removing heat energy","Nothing can cause a change of state","Changing its name","Changing its colour"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Ancient China", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: Ancient China developed along the Yellow and Yangtze rivers, and is known for early inventions such as paper, silk production, and the Great Wall.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Ancient China developed along which rivers?", options:["The Amazon and Mississippi","The Tigris and Euphrates","The Yellow and Yangtze","The Nile and Congo"], answer:2},
     {q:"Which invention is credited to Ancient China?", options:["The printing press in Europe","Modern electricity","The wheel only","Paper"], answer:3},
     {q:"Silk production was an important early industry in ___.", options:["Ancient Rome","Ancient China","Ancient Egypt","Ancient Greece"], answer:1},
     {q:"The Great Wall of China was built mainly to ___.", options:["Store grain","Attract tourists","Help defend against invasions","Provide irrigation"], answer:2},
     {q:"Why do historians study Ancient China's early inventions?", options:["They influenced technology and trade for centuries afterward","Only modern inventions matter to historians","They had no lasting impact","Ancient China invented nothing notable"], answer:0}
   ]},
]},
{day:33, label:"Day 33 — Wed", subjects:[
  {subject:"Language", title:"Writing: Formal and Informal Letters", summary:"Ontario Grade 4 Writing strand: formal letters use polite, professional language for serious purposes (like a business), while informal letters use casual, friendly language for people you know well.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A formal letter is typically used for ___.", options:["Writing to a close friend casually","Professional or serious purposes","Texting a sibling","Writing in a diary"], answer:1},
     {q:"Which greeting fits a formal letter?", options:["Yo,","Whats up,","Hey there!","Dear Sir or Madam,"], answer:3},
     {q:"An informal letter is best suited for ___.", options:["A legal document","A formal complaint to a company","A job application","Writing to a close friend or family member"], answer:3},
     {q:"Which closing best fits a formal letter?", options:["Sincerely,","Later,","See ya later","Bye bye"], answer:0},
     {q:"Why does letter tone change between formal and informal writing?", options:["All letters should sound the same","Formal letters are always shorter","Tone never needs to change","To match the purpose and relationship with the reader"], answer:3}
   ]},
  {subject:"Math", title:"Mixed Numbers and Improper Fractions", summary:"Ontario Grade 4 Number strand: a mixed number combines a whole number and a fraction (like 2 and 1/2), while an improper fraction has a numerator larger than its denominator (like 5/2), and the two can be converted between each other.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"Which is a mixed number?", options:["5/2","1/2","2/5","2 and 1/2"], answer:3},
     {q:"Which is an improper fraction?", options:["3/7","2 and 1/4","1/2","7/3"], answer:3},
     {q:"Convert the mixed number 1 and 3/4 to an improper fraction.", options:["3/4","7/4","4/7","1/4"], answer:1},
     {q:"Convert the improper fraction 9/4 to a mixed number.", options:["2 and 1/2","9/4 cannot convert","2 and 1/4","4 and 1/4"], answer:2},
     {q:"In an improper fraction, the numerator is ___ the denominator.", options:["Unrelated to","Always exactly half of","Equal to or larger than","Always smaller than"], answer:2}
   ]},
  {subject:"Science", title:"Simple Machines: Levers and Inclined Planes", summary:"Ontario Grade 4 Science Structures and Mechanisms strand: a lever uses a pivot point (fulcrum) to lift or move objects with less effort, while an inclined plane is a sloped surface that makes raising objects easier.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A lever uses a ___ to help lift or move objects.", options:["Magnet","Screw","Wheel","Fulcrum (pivot point)"], answer:3},
     {q:"An inclined plane is best described as a ___.", options:["Spinning wheel","Sealed container","Sloped surface","Vertical pole"], answer:2},
     {q:"Which is an everyday example of an inclined plane?", options:["A pulley","A seesaw","A wheel","A ramp"], answer:3},
     {q:"A seesaw is an example of which simple machine?", options:["Screw","Lever","Wedge","Inclined plane"], answer:1},
     {q:"Why do inclined planes make lifting heavy objects easier?", options:["They eliminate gravity","They spread the effort over a longer distance instead of lifting straight up","They make objects lighter permanently","They have no real benefit"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Early Societies: Daily Life and Social Roles", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: early societies such as Egypt, Greece, Rome, Mesopotamia, and China had structured daily lives, with different social roles for rulers, workers, farmers, and families.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"In many early societies, social roles were often organized by ___.", options:["Class or status, such as rulers, workers, and farmers","Age only, with no other factors","No structure at all","Random daily selection"], answer:0},
     {q:"Farmers in early societies were important because they ___.", options:["Only built monuments","Ruled the government","Produced food to support the population","Had no role in daily life"], answer:2},
     {q:"Rulers in early civilizations often held responsibility for ___.", options:["Only farming duties","Nothing important","Leading the society and making major decisions","Cooking for the population"], answer:2},
     {q:"Studying daily life in early societies helps us understand ___.", options:["Nothing useful about history","Daily life was identical everywhere","Only modern life","How people lived, worked, and organized their communities long ago"], answer:3},
     {q:"Which role would likely have existed in most early societies?", options:["Software engineer","Airline pilot","Farmer","Astronaut"], answer:2}
   ]},
]},
{day:34, label:"Day 34 — Thu", subjects:[
  {subject:"Language", title:"Figurative Language: Idioms", summary:"Ontario Grade 4 Reading strand: an idiom is a phrase whose meaning cannot be understood from the literal words alone, such as break the ice or it is raining cats and dogs.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"An idiom is a phrase whose meaning ___.", options:["Is always about weather","Has no meaning at all","Cannot be understood from its literal words alone","Matches its literal words exactly"], answer:2},
     {q:"What does the idiom break the ice mean?", options:["To finish a race","To clean a window","To ease tension and start a conversation","To literally break frozen water"], answer:2},
     {q:"What does it is raining cats and dogs mean?", options:["It is raining very heavily","It is a sunny day","Animals are falling from the sky","Pets are outside playing"], answer:0},
     {q:"Why can idioms be confusing for new readers?", options:["They only exist in one language","Their meaning differs from what the individual words literally say","They never appear in writing","They are always easy to understand literally"], answer:1},
     {q:"Which is an example of an idiom?", options:["Two plus two equals four","The sky is blue.","Spill the beans","The cat is sleeping"], answer:2}
   ]},
  {subject:"Math", title:"Adding and Subtracting Decimals", summary:"Ontario Grade 4 Number strand: adding and subtracting decimals requires lining up the decimal points so digits with the same place value are combined correctly.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"What is 3.25 + 1.50?", options:["4.25","3.75","5.25","4.75"], answer:3},
     {q:"What is 6.80 minus 2.30?", options:["4.10","9.10","4.50","3.50"], answer:2},
     {q:"When adding decimals, it is important to ___.", options:["Always round first","Line up the decimal points","Add only whole numbers","Ignore the decimal point"], answer:1},
     {q:"What is 5.05 + 2.95?", options:["8.10","7.00","7.90","8.00"], answer:3},
     {q:"What is 10.00 minus 4.35?", options:["5.35","6.35","6.65","5.65"], answer:3}
   ]},
  {subject:"Science", title:"Structures: Load and Support", summary:"Ontario Grade 4 Science Structures and Mechanisms strand: a load is the weight a structure must support, and good structural design distributes that load evenly to prevent collapse.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A load on a structure refers to ___.", options:["The structure's age","The weight the structure must support","The colour of the structure","The material's smell"], answer:1},
     {q:"Why is it important for a structure to distribute load evenly?", options:["It makes the structure heavier for no reason","Even distribution has no benefit","It only matters for small structures","To prevent weak points that could cause collapse"], answer:3},
     {q:"Which structural feature helps support heavy loads?", options:["Strong support columns or beams","No support at all","Decorative paint","Thin, unsupported beams"], answer:0},
     {q:"A bridge is designed to safely support the load of ___.", options:["Nothing at all","Vehicles, people, and its own weight","Only light wind","Only itself with nothing on it"], answer:1},
     {q:"What might happen if a structure's support cannot handle its load?", options:["Nothing would happen","The structure could weaken or collapse","The structure would become stronger","The load would disappear"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Early Societies: Beliefs and Traditions", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: early societies such as Egypt, Greece, Rome, Mesopotamia, and China developed belief systems, gods, and traditions that shaped their culture, art, and daily practices.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Many early societies developed belief systems that included ___.", options:["No spiritual practices at all","Gods, traditions, and ceremonies","Only modern religions","Identical beliefs across all civilizations"], answer:1},
     {q:"Beliefs and traditions in early societies often influenced ___.", options:["Only farming techniques","Art, architecture, and daily practices","Only trade routes","Nothing about daily life"], answer:1},
     {q:"Why do historians study the belief systems of early societies?", options:["Only written laws matter to historians","It has no historical value","To better understand their culture, values, and way of life","Beliefs have no connection to culture"], answer:2},
     {q:"Which is an example of how belief systems shaped early societies?", options:["Building temples and monuments for religious purposes","Beliefs only affected modern societies","All societies built the same structures for the same reasons","Beliefs had no effect on architecture"], answer:0},
     {q:"Comparing beliefs across early societies shows that ___.", options:["Only one early society had any beliefs","Different societies expressed traditions in unique but sometimes similar ways","All beliefs were exactly identical worldwide","Beliefs never varied across regions"], answer:1}
   ]},
]},
{day:35, label:"Day 35 — Fri", subjects:[
  {subject:"Language", title:"Reading: Making Predictions", summary:"Ontario Grade 4 Reading strand: making predictions means using clues from the title, pictures, and text so far to thoughtfully guess what might happen next in a story.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Making a prediction while reading means ___.", options:["Using clues from the text to thoughtfully guess what happens next","Skipping to the end of the book","Randomly guessing with no clues","Ignoring the story completely"], answer:0},
     {q:"Which is a good source of clues for making predictions?", options:["The title and pictures","The font style","The price of the book","The publisher's name"], answer:0},
     {q:"Why do good readers make predictions while reading?", options:["It only works for non-fiction texts","Predictions are not useful for reading","It keeps them thinking actively and engaged with the text","It replaces the need to read the rest of the story"], answer:2},
     {q:"If a story's cover shows dark clouds and a worried character, you might predict ___.", options:["The story is a cookbook","Something tense or stormy may happen","A cheerful, sunny beginning","Nothing can be predicted from a cover"], answer:1},
     {q:"After making a prediction, good readers should ___.", options:["Never think about it again","Check whether the story confirms or changes their prediction","Stop reading immediately","Assume they are always correct"], answer:1}
   ]},
  {subject:"Math", title:"Classifying Triangles", summary:"Ontario Grade 4 Geometry strand: triangles can be classified by their sides (equilateral, isosceles, scalene) and by their angles (right, acute, obtuse).",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A triangle with all three sides equal is called ___.", options:["Isosceles","Scalene","Equilateral","Right"], answer:2},
     {q:"A triangle with exactly two equal sides is called ___.", options:["Equilateral","Scalene","Obtuse","Isosceles"], answer:3},
     {q:"A triangle with no equal sides is called ___.", options:["Scalene","Equilateral","Isosceles","Right"], answer:0},
     {q:"A triangle with one 90-degree angle is called a ___ triangle.", options:["Obtuse","Right","Equilateral","Acute"], answer:1},
     {q:"A triangle with all angles less than 90 degrees is called ___.", options:["Right","Scalene","Acute","Obtuse"], answer:2}
   ]},
  {subject:"Science", title:"Space: Constellations and the Night Sky", summary:"Ontario Grade 4 Science Earth and Space Systems strand: constellations are patterns of stars that people have named and used for navigation and storytelling, appearing to shift position across the seasons.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A constellation is a ___.", options:["Type of planet","Type of moon","Single bright star","Pattern of stars that has been named"], answer:3},
     {q:"Constellations have historically been used for ___.", options:["Cooking recipes","Measuring temperature","Navigation and storytelling","Building materials"], answer:2},
     {q:"Which is a well-known constellation visible from Canada?", options:["The Great Lakes","The Big Dipper","The Arctic Circle","The Rocky Mountains"], answer:1},
     {q:"Why do the visible constellations change with the seasons?", options:["The sky is different every night randomly","Stars physically move very quickly","Constellations disappear each season","Earth's position in orbit around the Sun changes our view of the night sky"], answer:3},
     {q:"Constellations are best observed ___.", options:["Only in summer","During the bright daytime","On a clear night away from bright city lights","Only during a full moon"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Comparing Physical Regions of Canada", summary:"Ontario Grade 4 Social Studies People and Environments strand: Canada includes diverse physical regions, such as the Canadian Shield, the Prairies, the Rocky Mountains, and coastal areas, each with distinct landforms and climates.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Which physical region of Canada is known for flat, fertile farmland?", options:["The Prairies","The Arctic","The Rocky Mountains","The Canadian Shield"], answer:0},
     {q:"The Canadian Shield is mainly made up of ___.", options:["Sand dunes","Tropical rainforest","Ancient rock, forests, and lakes","Ocean floor"], answer:2},
     {q:"Which region features tall, rugged mountains in western Canada?", options:["The Arctic tundra","The Rocky Mountains","The St. Lawrence Lowlands","The Prairies"], answer:1},
     {q:"Why do Canada's physical regions have different climates and landscapes?", options:["Climate has no connection to landforms","Canada has only one physical region","All regions of Canada have identical climates","Their location, landforms, and distance from oceans affect their climate"], answer:3},
     {q:"Comparing physical regions helps students understand ___.", options:["How geography shapes where and how people live","That geography has no effect on communities","That climate is the same everywhere in Canada","That Canada is entirely flat"], answer:0}
   ]},
]},
{day:36, label:"Day 36 — Mon", subjects:[
  {subject:"Language", title:"Vocabulary: Homophones", summary:"Ontario Grade 4 Language strand: homophones are words that sound the same but have different spellings and meanings, such as their/there/they are, or to/too/two.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Which set of words are homophones?", options:["Run and walk","Happy and sad","Their, there, they are","Big and small"], answer:2},
     {q:"Choose the correct homophone: ___ going to the park.", options:["They're","Their","There","They are"], answer:0},
     {q:"Choose the correct homophone: I left my book over ___.", options:["there","their","they're","they are"], answer:0},
     {q:"Homophones are words that ___.", options:["Always mean the exact same thing","Sound the same but have different spellings and meanings","Are spelled the same but sound different","Are never used in writing"], answer:1},
     {q:"Which is the correct use: I have ___ apples.", options:["two","too","there","to"], answer:0}
   ]},
  {subject:"Math", title:"Introducing Quadrilaterals", summary:"Ontario Grade 4 Geometry strand: a quadrilateral is any shape with four sides, including squares, rectangles, rhombuses, and trapezoids, each with their own specific properties.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A quadrilateral always has how many sides?", options:["Six","Four","Three","Five"], answer:1},
     {q:"Which shape is a quadrilateral with four equal sides and four right angles?", options:["Square","Trapezoid","Circle","Triangle"], answer:0},
     {q:"A rectangle has ___ pairs of equal opposite sides.", options:["Two","Zero","Four","One"], answer:0},
     {q:"A trapezoid has exactly how many parallel sides?", options:["Zero","Four pairs","Two pairs","One pair"], answer:3},
     {q:"Which of these is NOT a quadrilateral?", options:["Rectangle","Square","Triangle","Rhombus"], answer:2}
   ]},
  {subject:"Science", title:"Weather Instruments and Measurement", summary:"Ontario Grade 4 Science Earth and Space Systems strand: scientists use instruments such as thermometers, rain gauges, and wind vanes to measure and track weather conditions like temperature, precipitation, and wind direction.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A thermometer is used to measure ___.", options:["Air pressure only","Wind direction","Temperature","Rainfall amount"], answer:2},
     {q:"A rain gauge is used to measure ___.", options:["Temperature","The amount of precipitation","Wind speed","Cloud colour"], answer:1},
     {q:"A wind vane is used to determine ___.", options:["Temperature","Wind direction","Humidity","Rainfall totals"], answer:1},
     {q:"Why do meteorologists use weather instruments?", options:["To accurately measure and track weather conditions","Instruments provide no useful weather data","Weather cannot be measured","To guess randomly instead of measuring"], answer:0},
     {q:"Which instrument would help you know if a storm brought a lot of rain?", options:["Compass","Thermometer","Wind vane","Rain gauge"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Indigenous Peoples: Contributions to Canadian Society", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: Indigenous peoples have made significant and lasting contributions to Canadian society, including knowledge of the land, agriculture, medicine, governance, and culture.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Indigenous peoples have contributed knowledge about ___ to Canadian society.", options:["Nothing of lasting value","Foreign countries only","The land, agriculture, and medicine","Only modern technology"], answer:2},
     {q:"Which crop, first cultivated by Indigenous peoples, remains important today?", options:["Corn","Bananas","Coffee","Rice"], answer:0},
     {q:"Indigenous governance systems have influenced ideas about ___.", options:["Cooperation and consensus-based decision making","Foreign political systems only","Nothing related to modern government","Only ancient practices with no modern relevance"], answer:0},
     {q:"Why is it important to recognize Indigenous contributions to Canada?", options:["Indigenous contributions are unimportant","It provides a fuller, more accurate understanding of Canadian history and culture","It has no educational value","Canadian history began only with European settlers"], answer:1},
     {q:"Indigenous art, storytelling, and traditions continue to ___ Canadian culture today.", options:["Replace entirely","Be completely separate from","Have no influence on","Enrich and influence"], answer:3}
   ]},
]},
{day:37, label:"Day 37 — Tue", subjects:[
  {subject:"Language", title:"Writing: Poetry", summary:"Ontario Grade 4 Writing strand: poetry uses rhythm, imagery, and sometimes rhyme to express ideas and feelings in a creative, condensed form, often organized into lines and stanzas.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A stanza in a poem is similar to a ___ in prose writing.", options:["Footnote","Chapter","Book title","Paragraph"], answer:3},
     {q:"Poetry often uses ___ to create vivid mental pictures for the reader.", options:["Imagery","Only numbers","Random letters","Blank pages"], answer:0},
     {q:"Rhyme in poetry means ___.", options:["Words with opposite meanings","Only long words","Words with the same ending sound","Random unrelated words"], answer:2},
     {q:"Which is a common feature of poetry?", options:["Only true, factual statements","Strict business formatting","Rhythm and word choice for effect","No creativity allowed"], answer:2},
     {q:"Why might a poet choose poetry instead of a regular paragraph to express an idea?", options:["To use rhythm, imagery, and condensed language for creative effect","There is no reason to choose poetry","Poetry cannot express any real ideas","Paragraphs are not allowed to express feelings"], answer:0}
   ]},
  {subject:"Math", title:"Factors and Multiples", summary:"Ontario Grade 4 Number strand: a factor is a number that divides evenly into another number, while a multiple is the result of multiplying a number by a whole number.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"Which is a factor of 12?", options:["4","9","5","7"], answer:0},
     {q:"Which is a multiple of 6?", options:["18","25","20","15"], answer:0},
     {q:"A factor of a number ___ evenly into it.", options:["Multiplies infinitely","Has no relationship","Never divides","Divides"], answer:3},
     {q:"List the factors of 10.", options:["2, 4, 5, 10","1, 2, 4, 10","1, 3, 5, 10","1, 2, 5, 10"], answer:3},
     {q:"The first three multiples of 7 are ___.", options:["7, 14, 21","7, 8, 9","1, 7, 14","7, 17, 27"], answer:0}
   ]},
  {subject:"Science", title:"Sound: How Sound Travels Through Materials", summary:"Ontario Grade 4 Science Matter and Energy strand: sound is a vibration that travels through different materials -- solids, liquids, and gases -- typically fastest through solids and slowest through gases like air.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Sound travels as a type of ___.", options:["Solid object","Light wave","Chemical reaction","Vibration"], answer:3},
     {q:"Sound generally travels fastest through ___.", options:["Water","A vacuum with nothing in it","Air","Solids"], answer:3},
     {q:"Sound cannot travel through ___.", options:["Metal","Air","Water","A complete vacuum (empty space)"], answer:3},
     {q:"Why can you sometimes hear sound better with your ear against a solid surface, like a table?", options:["Sound travels efficiently through solid materials","Sound cannot travel through solids","Solids block all sound","It has nothing to do with vibrations"], answer:0},
     {q:"Which best describes how sound moves through air to reach our ears?", options:["As vibrating air particles carrying the sound wave","Only through complete silence","Sound does not move at all","As a beam of light"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Canada's Relationships with Other Countries", summary:"Ontario Grade 4 Social Studies People and Environments strand: Canada maintains relationships with other countries through trade, diplomacy, and international cooperation, which affect its economy and global connections.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Trade with other countries allows Canada to ___.", options:["Stop producing its own goods entirely","Avoid all international contact","Only sell goods, never buy any","Exchange goods and services with the rest of the world"], answer:3},
     {q:"Diplomacy between countries generally involves ___.", options:["Avoiding all communication","Ignoring international issues","Only military action","Communication and cooperation between governments"], answer:3},
     {q:"Which is an example of an item Canada might export to other countries?", options:["Only imported goods","Nothing, Canada exports no goods","Items made exclusively in other countries","Natural resources like lumber or minerals"], answer:3},
     {q:"Why are international relationships important for Canada's economy?", options:["International relationships have no economic effect","They create trade opportunities that support jobs and economic growth","Trade only benefits other countries, never Canada","Canada's economy operates in complete isolation"], answer:1},
     {q:"International cooperation between countries can help address ___.", options:["Only local town issues","Problems within a single country only","Nothing of global importance","Shared challenges, such as environmental or economic issues"], answer:3}
   ]},
]},
{day:38, label:"Day 38 — Wed", subjects:[
  {subject:"Language", title:"Media Literacy: Advertising Techniques", summary:"Ontario Grade 4 Media Literacy strand: advertisers use techniques such as emotional appeals, celebrity endorsements, and repetition to persuade audiences to buy products or believe messages.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"An emotional appeal in advertising tries to ___.", options:["Only use plain black-and-white text","Persuade by triggering feelings like excitement or happiness","Avoid influencing the audience at all","Present only statistics"], answer:1},
     {q:"A celebrity endorsement in an ad means ___.", options:["A famous person promotes the product","Only scientists appear in the ad","The ad contains no persuasive elements","The product has no advertising at all"], answer:0},
     {q:"Repetition in advertising is used to ___.", options:["Confuse viewers on purpose","Help the audience remember the brand or message","Make audiences forget the product","Slow down the ad's pacing for no reason"], answer:1},
     {q:"Why should viewers think critically about advertising techniques?", options:["Critical thinking is unnecessary for ads","Advertising has no techniques worth noticing","To recognize persuasion methods and make informed decisions","All ads present only unbiased facts"], answer:2},
     {q:"Which is an example of an advertising technique?", options:["Using a catchy jingle or slogan","Providing no information about the product","Avoiding any persuasive language","Refusing to show the product"], answer:0}
   ]},
  {subject:"Math", title:"Patterning: Input-Output Tables", summary:"Ontario Grade 4 Algebra strand: an input-output table shows how a rule transforms an input number into an output number, helping students identify and apply numeric rules.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"If the rule is add 5, what is the output when the input is 3?", options:["5","15","3","8"], answer:3},
     {q:"If the rule is multiply by 2, what is the output when the input is 6?", options:["3","12","6","8"], answer:1},
     {q:"In an input-output table, the input is ___.", options:["The name of the rule","The starting number before applying the rule","Never used in the table","Always the final answer"], answer:1},
     {q:"If input 4 gives output 12, and input 5 gives output 15, what is the rule?", options:["Multiply by 3","Subtract 1","Divide by 3","Add 8"], answer:0},
     {q:"Input-output tables are useful because they help you ___.", options:["Replace the need for addition","Guess randomly with no pattern","Avoid using any math rules","Identify and apply a consistent numeric rule"], answer:3}
   ]},
  {subject:"Science", title:"Light: Absorption and Colour", summary:"Ontario Grade 4 Science Matter and Energy strand: objects appear a certain colour based on which wavelengths of light they reflect and which they absorb; a black object absorbs most light, while a white object reflects most light.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A black object appears black because it ___ most light.", options:["Reflects","Ignores","Absorbs","Creates"], answer:2},
     {q:"A white object appears white because it ___ most light.", options:["Blocks completely","Reflects","Destroys","Absorbs"], answer:1},
     {q:"An object appears a certain colour based on which light wavelengths it ___.", options:["Ignores entirely","Reflects","Creates from nothing","Destroys permanently"], answer:1},
     {q:"On a sunny day, why might a black shirt feel hotter than a white shirt?", options:["Colour has no effect on heat absorption","Black absorbs more light energy, which converts to heat","White absorbs more heat than black","Black reflects all light energy away"], answer:1},
     {q:"If an object reflects only green light and absorbs the rest, it will appear ___.", options:["Black","Blue","Green","Red"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Landforms and Bodies of Water in Canada", summary:"Ontario Grade 4 Social Studies People and Environments strand: Canada contains diverse landforms and bodies of water, including mountains, plains, rivers, and lakes, such as the Great Lakes and the St. Lawrence River.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Which are the five connected lakes on the Canada-United States border?", options:["The Arctic Lakes","The Prairie Lakes","The Rocky Lakes","The Great Lakes"], answer:3},
     {q:"The St. Lawrence River is important because it ___.", options:["Is located entirely in another country","Is a small, unused stream","Connects the Great Lakes to the Atlantic Ocean, supporting trade and travel","Has no significance to Canada"], answer:2},
     {q:"Which landform is a large, flat area often used for farming?", options:["Volcano","Canyon","Plain","Mountain range"], answer:2},
     {q:"Studying Canada's landforms and water bodies helps us understand ___.", options:["That all of Canada looks the same","That Canada has no significant water bodies","How geography influences where communities settle and how they live","That geography has no effect on daily life"], answer:2},
     {q:"Which is an example of a landform found in Canada?", options:["A skyscraper","Mountains","A highway","A shopping mall"], answer:1}
   ]},
]},
{day:39, label:"Day 39 — Thu", subjects:[
  {subject:"Language", title:"Grammar: Quotation Marks and Dialogue", summary:"Ontario Grade 4 Writing strand: quotation marks show the exact words a person says in dialogue, with punctuation like commas and periods placed carefully to show who is speaking.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Quotation marks are used to show ___.", options:["The exact words someone says","The title of a chapter","A character's thoughts only","A math equation"], answer:0},
     {q:"Which sentence correctly uses quotation marks?", options:["“Maria said I am ready to go","Maria said I am ready to go.","Maria said, “I am ready to go.”","Maria said, I am ready to go."], answer:2},
     {q:"Dialogue in a story refers to ___.", options:["The book's cover art","The setting description","The table of contents","Conversation between characters"], answer:3},
     {q:"In dialogue, a comma is often placed ___.", options:["Never used in dialogue","Before the closing quotation mark, before the speaker tag","Only at the end of the whole story","Outside the quotation marks always"], answer:1},
     {q:"Why is dialogue useful in storytelling?", options:["It shows characters' personalities and moves the plot forward through their speech","Dialogue has no effect on a story","It is only used in non-fiction","It replaces the need for a plot"], answer:0}
   ]},
  {subject:"Math", title:"Multi-Step Word Problems", summary:"Ontario Grade 4 Number strand: multi-step word problems require identifying and completing more than one operation in the correct order to reach a final answer.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A store had 240 toys, sold 85, then received a shipment of 60 more. How many toys now?", options:["155","215","325","385"], answer:1},
     {q:"Liam saved $45, spent $18, then earned $12 more. How much does Liam have now?", options:["$27","$63","$39","$75"], answer:2},
     {q:"A school has 4 classes of 25 students each, and 10 students are absent today. How many are present?", options:["85","110","100","90"], answer:3},
     {q:"Solving a multi-step problem requires you to ___.", options:["Guess the final number","Use only one operation and ignore the rest","Skip the information given","Complete each necessary step in the correct order"], answer:3},
     {q:"A baker made 150 muffins, sold 3 dozen, then baked 24 more. How many muffins are there now?", options:["150","186","138","126"], answer:2}
   ]},
  {subject:"Science", title:"Electricity: Conductors and Insulators", summary:"Ontario Grade 4 Science Matter and Energy strand: conductors, like most metals, allow electricity to flow through them easily, while insulators, like rubber and plastic, resist the flow of electricity and are used for safety.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A conductor is a material that ___.", options:["Has no effect on electricity","Blocks electricity completely","Allows electricity to flow through it easily","Is always made of wood"], answer:2},
     {q:"An insulator is a material that ___.", options:["Creates electricity from nothing","Allows electricity to flow freely","Resists the flow of electricity","Is always metal"], answer:2},
     {q:"Which material is typically a good conductor?", options:["Rubber","Plastic","Wood","Copper"], answer:3},
     {q:"Why are electrical wires often covered in rubber or plastic?", options:["To insulate them and prevent dangerous electric shocks","Covering wires has no safety purpose","To make wires heavier","To make the wires conduct more electricity"], answer:0},
     {q:"Which of these is typically used as an insulator?", options:["Steel","Aluminum","Copper wire","Rubber"], answer:3}
   ]},
  {subject:"SocialStudies", title:"How Canada's Provinces and Territories Formed", summary:"Ontario Grade 4 Social Studies People and Environments strand: Canada's provinces and territories joined the country at different times in history, starting with Confederation in 1867 and continuing as new provinces and territories were added.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"In what year did Confederation create the original Dominion of Canada?", options:["1867","1900","1776","1812"], answer:0},
     {q:"Canada's provinces and territories joined the country ___.", options:["They have never changed since 1867","At different times throughout history","All at exactly the same time","Before Confederation only"], answer:1},
     {q:"How many provinces and territories make up Canada today?", options:["Ten provinces and three territories","Eight","Five","Twenty"], answer:0},
     {q:"Why is it useful to learn how Canada's provinces and territories formed?", options:["It helps explain Canada's history and how the country grew over time","It has no connection to understanding Canada today","Provinces have always existed exactly as they are now","This history has no educational value"], answer:0},
     {q:"Confederation in 1867 originally united which regions?", options:["Only the territories","British Columbia and Alberta only","Ontario, Quebec, Nova Scotia, and New Brunswick","All ten current provinces at once"], answer:2}
   ]},
]},
{day:40, label:"Day 40 — Fri", subjects:[
  {subject:"Language", title:"Reading: Determining Importance", summary:"Ontario Grade 4 Reading strand: determining importance means identifying which details in a text are essential to understanding it, separating key information from interesting but less important details.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Determining importance while reading means ___.", options:["Ignoring the main idea","Remembering every single detail equally","Identifying which details are most essential to understanding the text","Skipping the text entirely"], answer:2},
     {q:"Which is more likely to be an essential detail in an informational text?", options:["The font used in the book","An unrelated side comment","A key fact directly supporting the main idea","The page number"], answer:2},
     {q:"Why is determining importance a useful reading strategy?", options:["It replaces the need to read carefully","It helps readers focus on and remember the most meaningful information","It means ignoring the main idea","It has no benefit while reading"], answer:1},
     {q:"When summarizing a text, determining importance helps you ___.", options:["Add unrelated new information","Choose only the most essential information to include","Avoid understanding the text","Include every single detail from the text"], answer:1},
     {q:"Which reading skill is closely related to determining importance?", options:["Ignoring punctuation","Identifying the main idea","Skipping the title","Reading only the last page"], answer:1}
   ]},
  {subject:"Math", title:"Coordinate Grids: Plotting Points", summary:"Ontario Grade 4 Geometry strand: a coordinate grid uses a horizontal x-axis and vertical y-axis to locate points using ordered pairs, such as (3, 2), which means 3 units across and 2 units up.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"In the ordered pair (3, 2), which number represents the horizontal position?", options:["Neither","3","2","Both equally"], answer:1},
     {q:"The horizontal axis on a coordinate grid is called the ___.", options:["X-axis","Z-axis","Origin","Y-axis"], answer:0},
     {q:"The point where the x-axis and y-axis meet is called the ___.", options:["Vertex","Endpoint","Origin","Coordinate"], answer:2},
     {q:"To plot the point (4, 1), you would move ___.", options:["Nowhere, since the point does not exist","4 units up, 1 unit across","4 units across, 1 unit up","1 unit across, 4 units down"], answer:2},
     {q:"An ordered pair like (2, 5) is written in the order ___.", options:["(y, x)","Only y-values","Random order","(x, y)"], answer:3}
   ]},
  {subject:"Science", title:"Erosion and Its Effects on Landforms", summary:"Ontario Grade 4 Science Earth and Space Systems strand: erosion is the gradual wearing away and movement of soil and rock by wind, water, or ice, slowly shaping landforms like valleys and canyons over long periods of time.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Erosion is best described as the ___.", options:["Instant disappearance of mountains","Formation of clouds","Sudden creation of new rock","Gradual wearing away and movement of soil and rock"], answer:3},
     {q:"Which of these can cause erosion?", options:["Wind, water, and ice","Only bright sunlight","Nothing natural causes erosion","Only complete stillness"], answer:0},
     {q:"A river slowly carving out a canyon over time is an example of ___.", options:["Erosion","Evaporation","Condensation","Combustion"], answer:0},
     {q:"Erosion typically occurs ___.", options:["Only in outer space","Gradually, often over long periods of time","Only underground","Instantly, within seconds"], answer:1},
     {q:"Why might people plant vegetation along a riverbank?", options:["Plants speed up erosion significantly","Vegetation has no effect on erosion","To make erosion happen faster","Plant roots can help hold soil in place and reduce erosion"], answer:3}
   ]},
  {subject:"SocialStudies", title:"My Role as a Canadian Citizen", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: being a Canadian citizen involves rights, such as voting when old enough, and responsibilities, such as respecting laws, the environment, and the wellbeing of the community.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"A responsibility of Canadian citizens includes ___.", options:["Avoiding all civic participation","Respecting laws and contributing to the community","Breaking rules whenever convenient","Ignoring community needs"], answer:1},
     {q:"Once old enough, Canadian citizens gain the right to ___.", options:["Avoid paying any attention to government","Vote in elections","Ignore all laws","Skip all civic duties"], answer:1},
     {q:"Why might a student get involved in a local community project?", options:["To practice being an active, responsible citizen","Community involvement has no value","It is required to skip school","Only adults can contribute to communities"], answer:0},
     {q:"Respecting the environment is considered part of good citizenship because ___.", options:["Protecting shared resources benefits the whole community","The environment has no connection to citizenship","Only government workers must consider the environment","It has no lasting impact on anyone"], answer:0},
     {q:"Reflecting on your role as a citizen helps you understand ___.", options:["That citizenship applies only to adults","How your actions can positively contribute to your community and country","That individual actions never matter","That being a citizen has no responsibilities"], answer:1}
   ]},
]},
{day:41, label:"Day 41 — Mon", subjects:[
  {subject:"Language", title:"Reading: Point of View", summary:"Ontario Grade 4 Reading strand: point of view is the perspective from which a story is told, either first person (using I or we) or third person (using he, she, or they).",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A story told using I or we is written in ___ point of view.", options:["First person","Third person","Second person","No point of view"], answer:0},
     {q:"A story told using he, she, or they is written in ___ point of view.", options:["No point of view","Third person","First person","Second person"], answer:1},
     {q:"Point of view refers to ___.", options:["The publisher of a book","The font used in a book","The perspective from which a story is told","The book’s page count"], answer:2},
     {q:"Why does point of view matter to a reader?", options:["It shapes what information and feelings the reader has access to","It has no effect on how a story is understood","Point of view never changes a story","It only affects the book’s cover"], answer:0},
     {q:"Which pronoun signals first-person point of view?", options:["I","He","She","They"], answer:0}
   ]},
  {subject:"Math", title:"Division with Remainders", summary:"Ontario Grade 4 Number strand: when a number does not divide evenly, the amount left over is called the remainder, written as R after the quotient, such as 17 divided by 5 equals 3 remainder 2.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"What is 17 divided by 5?", options:["3 remainder 3","4 remainder 0","3 remainder 2","3 remainder 1"], answer:2},
     {q:"A remainder is ___.", options:["The same as the quotient","The amount left over after dividing evenly","Always zero","Only used in multiplication"], answer:1},
     {q:"What is 23 divided by 4?", options:["5 remainder 3","5 remainder 2","4 remainder 3","6 remainder 0"], answer:0},
     {q:"If a division problem has no remainder, the numbers divide ___.", options:["Unevenly","Randomly","Incorrectly","Evenly"], answer:3},
     {q:"What is 29 divided by 6?", options:["5 remainder 5","5 remainder 4","4 remainder 4","4 remainder 5"], answer:3}
   ]},
  {subject:"Science", title:"Life Cycles of Animals", summary:"Ontario Grade 4 Science Life Systems strand: many animals go through distinct life cycle stages, such as egg, larva, pupa, and adult for insects, or birth, growth, and maturity for mammals.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Which is a typical life cycle stage for many insects?", options:["Seed, sprout, flower","Egg and adult only, with nothing between","Egg, larva, pupa, adult","Only adult, with no other stages"], answer:2},
     {q:"A caterpillar is which stage in a butterfly’s life cycle?", options:["Egg","Adult","Pupa","Larva"], answer:3},
     {q:"Mammals typically go through stages including ___.", options:["Egg and pupa only","Birth, growth, and maturity","No identifiable stages","Only an adult stage"], answer:1},
     {q:"Why is studying life cycles useful in science?", options:["Life cycles have no scientific value","It helps explain how living things grow, change, and reproduce over time","Life cycles never change","All animals have identical life cycles"], answer:1},
     {q:"The pupa stage in an insect’s life cycle is when ___.", options:["Nothing happens at all","The insect transforms into its adult form","The insect is first laid as an egg","The insect stops developing permanently"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ancient India", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: Ancient India developed along the Indus River, and is known for early city planning, a written script, and significant early achievements in mathematics.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Ancient India developed along which river?", options:["The Tigris","The Indus River","The Amazon","The Nile"], answer:1},
     {q:"Ancient Indian cities were known for early examples of ___.", options:["Random, unplanned building","No buildings at all","Organized city planning","Only underground homes"], answer:2},
     {q:"Which subject did Ancient India make significant early contributions to?", options:["Modern computer science","Mathematics","Space travel","Aviation"], answer:1},
     {q:"Why do historians consider Ancient India an early major civilization?", options:["It developed no lasting inventions","It developed advanced cities, writing, and knowledge systems early in history","It was identical to every other ancient civilization","It had no notable achievements"], answer:1},
     {q:"Studying Ancient India alongside Egypt, China, and Mesopotamia helps us ___.", options:["Prove that only one civilization ever existed","Ignore historical differences between regions","Avoid learning about world history","Compare how different early civilizations developed"], answer:3}
   ]},
]},
{day:42, label:"Day 42 — Tue", subjects:[
  {subject:"Language", title:"Grammar: Irregular Verbs", summary:"Ontario Grade 4 Writing strand: irregular verbs do not follow the usual pattern of adding -ed for the past tense, such as go becoming went or eat becoming ate.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"What is the past tense of the irregular verb go?", options:["Went","Goed","Gone","Going"], answer:0},
     {q:"What is the past tense of the irregular verb eat?", options:["Eated","Eats","Eating","Ate"], answer:3},
     {q:"An irregular verb is one that ___.", options:["Does not follow the usual -ed pattern for the past tense","Is only used in questions","Has no past tense form","Always adds -ed for the past tense"], answer:0},
     {q:"What is the past tense of the irregular verb see?", options:["Sees","Seeing","Saw","Seed"], answer:2},
     {q:"Which of these is an irregular verb?", options:["Break","Play","Jump","Walk"], answer:0}
   ]},
  {subject:"Math", title:"Subtracting Fractions with the Same Denominator", summary:"Ontario Grade 4 Number strand: to subtract fractions with the same denominator, subtract the numerators and keep the denominator the same, such as 5/8 minus 2/8 equals 3/8.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"What is 5/8 minus 2/8?", options:["2/8","3/8","7/8","3/16"], answer:1},
     {q:"What is 7/10 minus 4/10?", options:["11/10","3/10","3/20","4/10"], answer:1},
     {q:"When subtracting fractions with the same denominator, you ___.", options:["Subtract the numerators and keep the denominator the same","Change the denominator each time","Add the numerators together","Subtract the denominators only"], answer:0},
     {q:"What is 9/12 minus 5/12?", options:["4/12","4/24","5/12","14/12"], answer:0},
     {q:"What is 6/9 minus 6/9?", options:["1","12/9","0/9","6/0"], answer:2}
   ]},
  {subject:"Science", title:"Classifying Materials: Natural and Synthetic", summary:"Ontario Grade 4 Science Matter and Energy strand: natural materials come directly from nature, such as wood or cotton, while synthetic materials are human-made, such as plastic or nylon.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A natural material is one that ___.", options:["Comes directly from nature","Is always metal","Is entirely human-made in a factory","Does not exist in the real world"], answer:0},
     {q:"A synthetic material is one that is ___.", options:["Human-made","Always liquid","Impossible to produce","Found only in forests"], answer:0},
     {q:"Which of these is a natural material?", options:["Nylon","Plastic","Cotton","Polyester"], answer:2},
     {q:"Which of these is a synthetic material?", options:["Plastic","Cotton","Wool","Wood"], answer:0},
     {q:"Why might a designer choose a synthetic material over a natural one?", options:["Synthetic materials can offer specific properties like durability or low cost","Synthetic materials never have any useful properties","There is never a reason to choose synthetic materials","Natural materials cannot be used for anything"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Comparing Early Writing Systems", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: early civilizations developed different writing systems, such as hieroglyphics in Egypt, cuneiform in Mesopotamia, and early script in the Indus Valley, to record information.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Hieroglyphics was the early writing system used in ___.", options:["Ancient Rome","Ancient Greece","Ancient Egypt","Ancient China"], answer:2},
     {q:"Cuneiform was the early writing system used in ___.", options:["Ancient China","Mesopotamia","Ancient India","Ancient Egypt"], answer:1},
     {q:"Early writing systems were mainly developed to ___.", options:["Prevent communication between people","Record and communicate information","Replace spoken language entirely","Decorate buildings only"], answer:1},
     {q:"Why is the development of writing considered a major milestone in early civilizations?", options:["Writing systems were identical across all civilizations","Writing had no effect on early societies","Early societies never needed to record information","It allowed information to be recorded and passed on more reliably"], answer:3},
     {q:"Comparing writing systems across civilizations shows that ___.", options:["Writing systems have no historical significance","Only one civilization ever developed writing","All early writing systems were exactly the same","Different societies solved the need to record information in unique ways"], answer:3}
   ]},
]},
{day:43, label:"Day 43 — Wed", subjects:[
  {subject:"Language", title:"Writing: Book Reviews", summary:"Ontario Grade 4 Writing strand: a book review shares an opinion about a book, supported by reasons and details, and often includes a brief summary along with a recommendation.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A book review typically includes ___.", options:["A list of unrelated books","The author’s home address","An opinion supported by reasons and a brief summary","Only the book’s price"], answer:2},
     {q:"Why should a book review include supporting reasons?", options:["Reasons are not needed in a review","Reviews should never explain opinions","To help the reader understand why the reviewer feels that way","Supporting reasons make a review less convincing"], answer:2},
     {q:"A recommendation in a book review tells the reader ___.", options:["Whether the reviewer thinks others should read the book","The exact page count","Nothing useful","The publisher’s address"], answer:0},
     {q:"Which is an example of a detail that could support a book review?", options:["Copying the entire book word for word","Ignoring the book completely","Describing an exciting scene from the book","Listing unrelated grocery items"], answer:2},
     {q:"A well-written book review helps other readers ___.", options:["Understand only the price of books","Skip reading altogether","Decide whether they might enjoy the book","Avoid all books permanently"], answer:2}
   ]},
  {subject:"Math", title:"Comparing and Ordering Decimals", summary:"Ontario Grade 4 Number strand: to compare decimals, line up the decimal points and compare digits from left to right, starting with the whole number, then tenths, then hundredths.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"Which decimal is greater: 0.45 or 0.5?", options:["0.5","Cannot be compared","They are equal","0.45"], answer:0},
     {q:"Which decimal is smallest: 0.3, 0.25, or 0.35?", options:["0.35","They are all equal","0.25","0.3"], answer:2},
     {q:"To compare decimals, you should first compare the ___.", options:["Whole number part","Hundredths digit","Colour of the numbers","Number of digits after the decimal"], answer:0},
     {q:"Order these from least to greatest: 0.6, 0.06, 0.66.", options:["0.6, 0.06, 0.66","0.06, 0.66, 0.6","0.66, 0.6, 0.06","0.06, 0.6, 0.66"], answer:3},
     {q:"Which decimal is equivalent to 0.5?", options:["0.005","0.55","0.05","0.50"], answer:3}
   ]},
  {subject:"Science", title:"Structures: Types of Bridges", summary:"Ontario Grade 4 Science Structures and Mechanisms strand: different bridge designs, such as beam, arch, and suspension bridges, use different structural principles to support loads and span distances.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A beam bridge is supported mainly by ___.", options:["A curved arch shape","Floating pontoons only","A straight, rigid horizontal structure","Cables hanging from towers"], answer:2},
     {q:"An arch bridge uses a curved shape to help ___.", options:["Distribute weight along the curve","Float on water","Eliminate all structural support","Avoid supporting any load"], answer:0},
     {q:"A suspension bridge is supported mainly by ___.", options:["Underground tunnels","A single wooden beam","Cables hung from tall towers","Solid concrete blocks only"], answer:2},
     {q:"Why might engineers choose different bridge designs for different locations?", options:["Only one bridge design has ever been used","Different designs suit different distances, loads, and terrain","All bridges must use the exact same design everywhere","Bridge design has no connection to location"], answer:1},
     {q:"Which bridge type is well-suited for spanning very long distances, like across a wide river?", options:["None of these can span long distances","A short wooden plank","Beam bridge","Suspension bridge"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Early Societies: Trade and Economy", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: early civilizations such as Egypt, Mesopotamia, China, and India developed trade networks to exchange goods like grain, textiles, and metals with neighbouring regions.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Trade in early societies mainly involved exchanging ___.", options:["Goods such as grain, textiles, and metals","Nothing at all","Only digital information","Only modern currency"], answer:0},
     {q:"Why did early civilizations develop trade networks?", options:["Trade networks did not exist in early history","Early societies were entirely self-sufficient with no needs","To obtain resources and goods not available locally","Trade served no useful purpose"], answer:2},
     {q:"A trade network connects ___.", options:["A single isolated village with no outside contact","Only modern countries","Nothing, since trade never happened historically","Different regions or civilizations exchanging goods"], answer:3},
     {q:"Which might an early civilization export if it had abundant farmland?", options:["Only imported goods","Grain or other crops","Items it does not produce at all","Nothing, since exporting is impossible"], answer:1},
     {q:"Studying early trade helps us understand ___.", options:["That economies have no historical importance","How ancient economies and connections between regions developed","That trade began only in modern times","That ancient civilizations never interacted with each other"], answer:1}
   ]},
]},
{day:44, label:"Day 44 — Thu", subjects:[
  {subject:"Language", title:"Figurative Language: Personification", summary:"Ontario Grade 4 Reading strand: personification gives human qualities or actions to non-human things or ideas, such as saying the wind whispered or the sun smiled down.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Personification is when a writer gives ___.", options:["No meaning to a sentence","Human qualities to non-human things","Colours to sounds","Numbers to letters"], answer:1},
     {q:"Which sentence is an example of personification?", options:["The wind is made of moving air.","The wind whispered through the trees.","The wind comes from changes in air pressure.","The wind speed was 20 kilometres per hour."], answer:1},
     {q:"Why do writers use personification?", options:["Personification has no purpose in writing","To make descriptions more vivid and engaging","To confuse the reader on purpose","To remove all imagery from writing"], answer:1},
     {q:"Which phrase uses personification?", options:["The flowers need water and sunlight.","The flowers danced in the breeze.","The flowers grow in the garden.","The flowers are red and yellow."], answer:1},
     {q:"Personification is a type of ___.", options:["Grammar rule","Punctuation mark","Spelling pattern","Figurative language"], answer:3}
   ]},
  {subject:"Math", title:"Symmetry", summary:"Ontario Grade 4 Geometry strand: a shape has line symmetry if it can be folded along a line so both halves match exactly, and that fold line is called a line of symmetry.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A shape has line symmetry if ___.", options:["It cannot be folded at all","It has no straight edges","It has more than four sides","It can be folded so both halves match exactly"], answer:3},
     {q:"The line along which a symmetrical shape can be folded is called a ___.", options:["Perimeter line","Diagonal","Coordinate","Line of symmetry"], answer:3},
     {q:"How many lines of symmetry does a square have?", options:["One","Two","Four","Zero"], answer:2},
     {q:"Which letter of the alphabet has a vertical line of symmetry?", options:["R","F","G","A"], answer:3},
     {q:"A circle has how many lines of symmetry?", options:["Zero","Four","One","An infinite number"], answer:3}
   ]},
  {subject:"Science", title:"Forces: Magnetism", summary:"Ontario Grade 4 Science Structures and Mechanisms strand: magnetism is a force that attracts certain metals, such as iron, and every magnet has a north pole and a south pole.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Magnetism is a force that attracts ___.", options:["Only liquids","Only wood","Certain metals, such as iron","All materials equally"], answer:2},
     {q:"Every magnet has ___.", options:["A north pole and a south pole","Only a north pole","Three poles","No poles at all"], answer:0},
     {q:"What happens when two magnets’ like poles (north-north or south-south) are brought together?", options:["They attract strongly","They stick together permanently","They repel each other","Nothing happens at all"], answer:2},
     {q:"What happens when two magnets’ opposite poles (north-south) are brought together?", options:["They repel each other","Nothing happens","They cancel out completely","They attract each other"], answer:3},
     {q:"Which material would a magnet most strongly attract?", options:["Iron","Plastic","Wood","Glass"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Early Societies: Art and Architecture", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: early civilizations expressed their culture and beliefs through art and architecture, such as Egyptian pyramids, Greek temples, and Chinese pottery.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Egyptian pyramids were primarily built as ___.", options:["Modern apartments","Tombs for pharaohs","Farming storage only","Shopping centres"], answer:1},
     {q:"Greek temples were often built to honour ___.", options:["Sports teams","Foreign kings only","Modern celebrities","Gods and goddesses"], answer:3},
     {q:"Art and architecture in early societies often reflected their ___.", options:["Beliefs, values, and technology","Random, meaningless choices","Only modern influences","Complete lack of culture"], answer:0},
     {q:"Why do historians study ancient art and architecture?", options:["It offers insight into how early societies lived and what they valued","Only written records matter to historians","Architecture from the past teaches us nothing","Ancient art has no historical value"], answer:0},
     {q:"Which is an example of early architecture still studied today?", options:["A modern shopping mall","A smartphone","The pyramids of Egypt","A highway overpass"], answer:2}
   ]},
]},
{day:45, label:"Day 45 — Fri", subjects:[
  {subject:"Language", title:"Reading: Cause and Effect", summary:"Ontario Grade 4 Reading strand: a cause is why something happens, and an effect is what happens as a result, and identifying these relationships helps readers understand how events connect in a text.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A cause is best described as ___.", options:["The title of a story","What happens as a result of something","A character’s name","The reason why something happens"], answer:3},
     {q:"An effect is best described as ___.", options:["A random unrelated event","The setting of a story","The reason something happens","What happens as a result of a cause"], answer:3},
     {q:"In the sentence It rained, so the game was cancelled, what is the effect?", options:["Neither is an effect","Both are causes","It rained","The game was cancelled"], answer:3},
     {q:"Why is understanding cause and effect useful when reading?", options:["It has no impact on understanding a text","Cause and effect never appears in stories","It helps readers see how events in a text are connected","It replaces the need to read the whole text"], answer:2},
     {q:"Which phrase often signals a cause-and-effect relationship?", options:["Once upon a time","Because of this","In a faraway land","The end"], answer:1}
   ]},
  {subject:"Math", title:"Perimeter and Area of Irregular Shapes", summary:"Ontario Grade 4 Geometry strand: irregular shapes can be broken into smaller regular shapes, like rectangles, to calculate their total perimeter or area by adding the parts together.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"To find the area of an irregular shape, you can ___.", options:["Multiply only the longest side","Ignore parts of the shape","Break it into smaller regular shapes and add their areas","Guess without calculating"], answer:2},
     {q:"An L-shaped figure can be split into how many rectangles to find its area?", options:["It cannot be split","One only","Zero","Two"], answer:3},
     {q:"Perimeter is the measurement of ___.", options:["The shape’s weight","The distance around the outside of a shape","The shape’s volume","The space inside a shape"], answer:1},
     {q:"If two rectangles that make up an irregular shape have areas of 12 and 8 square units, the total area is ___.", options:["96 square units","10 square units","4 square units","20 square units"], answer:3},
     {q:"Why is it useful to break an irregular shape into rectangles?", options:["Rectangles cannot be measured","Rectangles are easier to measure and calculate area for","It is never useful","It makes the shape disappear"], answer:1}
   ]},
  {subject:"Science", title:"Ecosystems: Producers, Consumers, and Decomposers", summary:"Ontario Grade 4 Science Life Systems strand: in an ecosystem, producers (like plants) make their own food, consumers (like animals) eat other organisms, and decomposers (like fungi) break down dead material.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A producer in an ecosystem is an organism that ___.", options:["Makes its own food","Does nothing in the ecosystem","Eats other organisms only","Breaks down dead material"], answer:0},
     {q:"A consumer in an ecosystem is an organism that ___.", options:["Has no role in the ecosystem","Makes its own food using sunlight","Eats other organisms for energy","Breaks down dead material only"], answer:2},
     {q:"A decomposer’s role in an ecosystem is to ___.", options:["Produce oxygen only","Break down dead plants and animals","Make food using sunlight","Hunt other consumers"], answer:1},
     {q:"Which of these is typically classified as a producer?", options:["A mushroom","A wolf","A bird","A plant"], answer:3},
     {q:"Why are decomposers important to an ecosystem?", options:["They prevent all growth in an ecosystem","They recycle nutrients back into the soil for producers to use","They have no effect on the ecosystem","They only consume other consumers"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Canada’s Territories: Yukon, Northwest Territories, and Nunavut", summary:"Ontario Grade 4 Social Studies People and Environments strand: Canada’s three territories -- Yukon, the Northwest Territories, and Nunavut -- make up the northern part of the country and have unique geography, climate, and Indigenous communities.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"How many territories does Canada have?", options:["One","Five","Three","Two"], answer:2},
     {q:"Which of these is one of Canada’s three territories?", options:["Alberta","Quebec","Nunavut","Ontario"], answer:2},
     {q:"Canada’s territories are located mainly in the ___ part of the country.", options:["Eastern coastal","Western coastal only","Northern","Southern"], answer:2},
     {q:"The climate in Canada’s territories is generally ___.", options:["Cold, with long winters","Tropical and warm year-round","Identical to southern Canada","Desert-like with no snow"], answer:0},
     {q:"Why is it important to learn about Canada’s territories?", options:["They have no distinct geography or culture","They have no significance to Canada","They are a significant part of Canada’s geography, culture, and Indigenous communities","They are not actually part of Canada"], answer:2}
   ]},
]},
{day:46, label:"Day 46 — Mon", subjects:[
  {subject:"Language", title:"Vocabulary: Multiple-Meaning Words", summary:"Ontario Grade 4 Language strand: multiple-meaning words are spelled the same but can have different meanings depending on how they are used in a sentence, such as bat, bank, or watch.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"The word bat can mean ___.", options:["Only a flying animal","A flying animal or sports equipment, depending on context","Only a type of tree","Only a colour"], answer:1},
     {q:"In the sentence I watched the clock on my watch, the two uses of watch mean ___.", options:["The exact same thing both times","Both refer to a type of bird","Neither use makes sense","Different things: looked at, and a wristwatch"], answer:3},
     {q:"A multiple-meaning word is one that ___.", options:["Can have different meanings depending on context","Has only one possible meaning","Cannot be used in a sentence","Is always spelled differently for each meaning"], answer:0},
     {q:"The word bank can refer to ___.", options:["Only a type of vehicle","A financial institution or the side of a river, depending on context","Only a financial institution","Only a type of fish"], answer:1},
     {q:"How can a reader figure out which meaning of a word is intended?", options:["By guessing randomly with no strategy","Multiple-meaning words cannot be understood","By ignoring the rest of the sentence","By using context clues from the surrounding sentence"], answer:3}
   ]},
  {subject:"Math", title:"24-Hour Clock (Military Time)", summary:"Ontario Grade 4 Measurement strand: the 24-hour clock counts hours from 00:00 (midnight) to 23:59, avoiding the need for AM and PM, and is commonly used in schedules like transit and travel.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"What time is 14:00 in standard 12-hour time?", options:["12:00 PM","2:00 PM","2:00 AM","4:00 PM"], answer:1},
     {q:"On the 24-hour clock, midnight is written as ___.", options:["1:00","24:00 only","00:00","12:00"], answer:2},
     {q:"What is 6:00 PM written in 24-hour time?", options:["16:00","18:00","20:00","06:00"], answer:1},
     {q:"The 24-hour clock is often used for ___.", options:["Never used anywhere","Casual conversations only","Schedules such as transit and travel","Only cooking recipes"], answer:2},
     {q:"What is 09:00 in 24-hour time equivalent to in standard time?", options:["7:00 AM","9:00 AM","9:00 PM","11:00 AM"], answer:1}
   ]},
  {subject:"Science", title:"Renewable and Non-Renewable Energy Sources", summary:"Ontario Grade 4 Science Matter and Energy strand: renewable energy sources, like solar and wind, can be replenished naturally, while non-renewable sources, like coal and oil, take millions of years to form and can run out.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A renewable energy source is one that ___.", options:["Can be replenished naturally over a short time","Takes millions of years to form","Always causes pollution","Can never be used again once used once"], answer:0},
     {q:"Which is an example of a renewable energy source?", options:["Solar power","Natural gas","Oil","Coal"], answer:0},
     {q:"A non-renewable energy source is one that ___.", options:["Comes only from the sun","Takes an extremely long time to form and can run out","Never runs out","Can be replenished quickly"], answer:1},
     {q:"Which is an example of a non-renewable energy source?", options:["Hydroelectric power","Wind power","Coal","Solar power"], answer:2},
     {q:"Why is there growing interest in using more renewable energy sources?", options:["Renewable sources are always worse for the environment","They can be replenished naturally and often produce less pollution","Non-renewable sources never run out","There is no benefit to renewable energy"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Map Skills: Scale and Symbols", summary:"Ontario Grade 4 Social Studies People and Environments strand: maps use a scale to show real-world distances in a smaller form, and symbols in a legend to represent features like cities, roads, or rivers.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"A map scale helps show ___.", options:["The colour of the land","Nothing useful","The population of a country","Real-world distances in a smaller form"], answer:3},
     {q:"Symbols on a map are explained in a ___.", options:["Legend (or key)","Scale bar only","Title page","Compass rose"], answer:0},
     {q:"If a map scale shows 1 cm equals 10 km, a 3 cm distance on the map represents ___.", options:["3 km","10 km","13 km","30 km"], answer:3},
     {q:"Why do maps use symbols instead of writing out every detail?", options:["Symbols have no purpose on maps","Symbols make maps impossible to understand","Symbols make maps easier to read quickly","Maps are not allowed to use symbols"], answer:2},
     {q:"Which might a map symbol commonly represent?", options:["A city, road, or river","Only the mapmaker’s name","A random unrelated object","Nothing at all"], answer:0}
   ]},
]},
{day:47, label:"Day 47 — Tue", subjects:[
  {subject:"Language", title:"Writing: Dialogue Writing", summary:"Ontario Grade 4 Writing strand: dialogue writing brings characters to life through their spoken words, using quotation marks and a new paragraph each time the speaker changes.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Dialogue in a story refers to ___.", options:["The spoken words of characters","The setting description","The book’s illustrations","The chapter titles"], answer:0},
     {q:"When writing dialogue, a new paragraph is usually started ___.", options:["Only at the very end of the story","Each time the speaker changes","Only when the setting changes","Never, all dialogue stays in one paragraph"], answer:1},
     {q:"Why is dialogue useful in a story?", options:["It reveals character personality and moves the plot forward","Dialogue replaces the need for a plot","Dialogue has no purpose in writing","Dialogue slows down every story unnecessarily"], answer:0},
     {q:"Which punctuation is typically used to show a character’s exact spoken words?", options:["Quotation marks","A semicolon","Parentheses","A colon"], answer:0},
     {q:"Good dialogue should sound ___.", options:["Identical for every character in the story","Completely random and unrelated to the character","Exactly like a textbook","Natural, like how the character would actually speak"], answer:3}
   ]},
  {subject:"Math", title:"Pictographs", summary:"Ontario Grade 4 Data Management strand: a pictograph uses pictures or symbols to represent data, with a key showing how many items each symbol stands for.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A pictograph uses ___ to represent data.", options:["Pictures or symbols","Colours with no meaning","Random shapes with no key","Only numbers written out"], answer:0},
     {q:"The key in a pictograph tells you ___.", options:["How many items each symbol represents","The names of the people who made the graph","Nothing useful","The title of the graph"], answer:0},
     {q:"If a pictograph key shows 1 symbol equals 5 students, and there are 4 symbols for Grade 4, how many Grade 4 students are there?", options:["20","9","5","4"], answer:0},
     {q:"Pictographs are especially useful for ___.", options:["Replacing the need for any data at all","Hiding information from the reader","Making data visually easy to compare at a glance","Making data more difficult to understand"], answer:2},
     {q:"Half of a symbol in a pictograph usually represents ___.", options:["The exact same as a full symbol","Double the full value","Zero","Half of the value the full symbol represents"], answer:3}
   ]},
  {subject:"Science", title:"Simple Machines: Wheel and Axle, and Screw", summary:"Ontario Grade 4 Science Structures and Mechanisms strand: a wheel and axle reduces the effort needed to move objects by rotating together, while a screw is a spiral inclined plane that converts turning motion into straight-line motion.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"A wheel and axle work together by ___.", options:["Never moving at all","Absorbing all force with no motion","Rotating together to reduce the effort needed to move objects","Only working separately, never together"], answer:2},
     {q:"A screw can be thought of as a type of ___ wrapped around a cylinder.", options:["Lever","Inclined plane","Pulley","Wheel"], answer:1},
     {q:"Which everyday object uses a wheel and axle?", options:["A brick","A doorknob","A pane of glass","A flat table"], answer:1},
     {q:"A screw converts ___ motion into straight-line motion.", options:["No motion at all","Sliding","Turning","Bouncing"], answer:2},
     {q:"Why is a wheel and axle considered a simple machine?", options:["It always makes tasks more difficult","It makes moving or lifting objects easier by reducing the effort required","It has no practical use","It only works underwater"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Climate Zones of Canada", summary:"Ontario Grade 4 Social Studies People and Environments strand: Canada spans several climate zones, from the cold Arctic in the north to milder, temperate zones in the south, influencing where people live and how they adapt.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Canada’s northern regions generally have a ___ climate.", options:["Cold, Arctic climate","Desert climate","Consistently warm climate","Tropical"], answer:0},
     {q:"Southern Canada generally has a ___ climate compared to the north.", options:["Identical","Colder","Milder, more temperate","Tropical"], answer:2},
     {q:"Climate zones influence ___.", options:["Where people settle and how they adapt their lifestyles","Only what sports people play","Only the colour of houses","Nothing about how people live"], answer:0},
     {q:"Why might fewer people live in Canada’s far northern climate zones?", options:["The north is actually the warmest region in Canada","Climate has no effect on where people choose to live","The north has no unique climate challenges","The harsh cold climate makes farming and travel more challenging"], answer:3},
     {q:"Studying climate zones helps students understand ___.", options:["That all of Canada has the exact same weather year-round","How geography and weather patterns vary across a large country like Canada","That climate has no connection to geography","That Canada has only one climate zone"], answer:1}
   ]},
]},
{day:48, label:"Day 48 — Wed", subjects:[
  {subject:"Language", title:"Media Literacy: Recognizing Bias in News", summary:"Ontario Grade 4 Media Literacy strand: bias in news occurs when information is presented in a way that favours one side or opinion, and recognizing it helps readers evaluate sources critically.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Bias in news means the information is presented ___.", options:["In a way that favours one side or opinion","Using only statistics","Without any point of view at all","In a completely neutral, balanced way"], answer:0},
     {q:"Why is it important for readers to recognize bias?", options:["Bias has no effect on how information is understood","Recognizing bias is unnecessary","To think critically and evaluate information more carefully","All news is always completely unbiased"], answer:2},
     {q:"Which might be a sign of bias in a news story?", options:["Citing multiple credible sources","Only presenting one side of an issue","Including verified facts and data","Presenting balanced viewpoints from multiple sources"], answer:1},
     {q:"Comparing multiple news sources on the same topic can help readers ___.", options:["Become more confused with no benefit","Avoid learning anything useful","Get a more complete, balanced understanding","Guarantee that one source is entirely correct"], answer:2},
     {q:"A media-literate reader asks questions like ___.", options:["What did I have for breakfast?","What colour is the website?","How long is this article?","Who created this message, and why?"], answer:3}
   ]},
  {subject:"Math", title:"Predicting Outcomes with Probability", summary:"Ontario Grade 4 Data Management strand: probability can be used to predict likely outcomes, such as predicting that rolling a die is more likely to land on a number 1 through 6 than any other value.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"If a bag has 3 red marbles and 1 blue marble, which colour is more likely to be picked?", options:["Red","Neither can be picked","Blue","Equally likely"], answer:0},
     {q:"Rolling a standard six-sided die, what is the chance of rolling a 7?", options:["Unlikely but possible","Likely","Impossible","Certain"], answer:2},
     {q:"Predicting outcomes with probability means ___.", options:["Always being 100 percent certain","Guessing with no reasoning at all","Using known information to estimate what is likely to happen","Ignoring the available data"], answer:2},
     {q:"If a spinner has 4 equal sections numbered 1 to 4, what is the chance of landing on 2?", options:["1 out of 4","2 out of 4","4 out of 4","1 out of 2"], answer:0},
     {q:"An outcome that is certain to happen has a probability of ___.", options:["It cannot be determined","50 percent","0 percent","100 percent"], answer:3}
   ]},
  {subject:"Science", title:"Recycling and Waste Reduction", summary:"Ontario Grade 4 Science Earth and Space Systems strand: recycling and waste reduction help limit the amount of garbage sent to landfills by reusing materials and reducing unnecessary consumption.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Recycling helps reduce the amount of waste sent to ___.", options:["Nowhere, recycling has no effect","Landfills","Space","The ocean only"], answer:1},
     {q:"Which is an example of waste reduction?", options:["Ignoring how much waste is produced","Reusing containers instead of throwing them away","Buying more single-use items","Throwing away recyclable materials"], answer:1},
     {q:"Materials like paper, glass, and some plastics can often be ___.", options:["Never reused in any way","Only thrown away","Destroyed completely with no benefit","Recycled into new products"], answer:3},
     {q:"Why is reducing waste important for the environment?", options:["Landfills have unlimited space","Reducing waste has no benefits","Waste has no impact on the environment","It helps conserve resources and limit pollution from landfills"], answer:3},
     {q:"Which of the three Rs comes first in reducing environmental impact: reduce, reuse, or recycle?", options:["None of them matter","Recycle","Reduce","Reuse"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canadian Identity: Symbols and Traditions", summary:"Ontario Grade 4 Social Studies Heritage and Identity strand: Canadian identity is expressed through symbols and traditions such as the maple leaf, the national anthem, and celebrations that reflect the country’s diverse heritage.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Which is a well-known symbol of Canada?", options:["The palm tree","The pine cone only","The cactus","The maple leaf"], answer:3},
     {q:"National symbols and traditions help express ___.", options:["A country’s shared identity and values","Only one person’s personal opinion","A country’s exact population count","Nothing meaningful about a country"], answer:0},
     {q:"Canada’s national anthem is an example of a ___.", options:["Type of food","Sports event","Type of currency","National tradition and symbol"], answer:3},
     {q:"Why does Canada celebrate diverse cultural traditions?", options:["Cultural diversity has no connection to Canadian identity","Celebrations are not part of Canadian identity","Canada is home to people from many different cultural backgrounds","Canada has only one culture"], answer:2},
     {q:"Learning about Canadian symbols and traditions helps students understand ___.", options:["That traditions are unimportant to a country","That symbols have no meaning","What makes up a shared sense of Canadian identity","That Canada has no shared identity"], answer:2}
   ]},
]},
{day:49, label:"Day 49 — Thu", subjects:[
  {subject:"Language", title:"Grammar: Possessive Nouns and Apostrophes", summary:"Ontario Grade 4 Writing strand: possessive nouns show ownership using an apostrophe, such as adding ’s for singular nouns (the dog’s bone) or just an apostrophe for plural nouns ending in s (the dogs’ bones).",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Which shows correct singular possession?", options:["The dog’s bone","The dogs bone","The dogs’s bone","The dog bone’s"], answer:0},
     {q:"How do you typically form the possessive of a plural noun ending in s?", options:["Add nothing at all","Add ’s","Add just an apostrophe after the s","Remove the s entirely"], answer:2},
     {q:"Which sentence correctly shows plural possession?", options:["The students book’s were on the desk.","The students’ books were on the desk.","The students books were on the desk.","The student’s’ books were on the desk."], answer:1},
     {q:"An apostrophe in a possessive noun shows ___.", options:["A question is being asked","The end of a sentence","Ownership or belonging","That a letter has been removed only"], answer:2},
     {q:"Which is the correct possessive form for a single cat named Max?", options:["Maxes’ toy","Max’s toy","Maxs toy","Max toy’s"], answer:1}
   ]},
  {subject:"Math", title:"Growing and Shrinking Patterns", summary:"Ontario Grade 4 Algebra strand: a growing pattern increases by a consistent rule each step, while a shrinking pattern decreases by a consistent rule each step.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"In the pattern 3, 6, 9, 12, what is the next number?", options:["14","13","15","16"], answer:2},
     {q:"In the pattern 50, 45, 40, 35, what is the next number?", options:["25","32","30","38"], answer:2},
     {q:"A growing pattern is one where the values ___.", options:["Stay exactly the same","Change randomly","Increase by a consistent rule","Decrease by a consistent rule"], answer:2},
     {q:"A shrinking pattern is one where the values ___.", options:["Stay exactly the same","Change randomly with no rule","Increase by a consistent rule","Decrease by a consistent rule"], answer:3},
     {q:"What is the rule for the pattern 2, 4, 8, 16?", options:["Divide by 2 each time","Subtract 2 each time","Add 2 each time","Multiply by 2 each time"], answer:3}
   ]},
  {subject:"Science", title:"Scientific Inquiry: Designing a Fair Test", summary:"Ontario Grade 4 Science Inquiry strand: a fair test changes only one variable at a time while keeping all other conditions the same, so results can be reliably compared and attributed to that one change.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"In a fair test, how many variables should typically be changed at a time?", options:["It does not matter","As many as possible","None at all","Only one"], answer:3},
     {q:"Why is it important to keep other conditions the same in a fair test?", options:["Keeping conditions the same makes the test less accurate","So any difference in results can be attributed to the one variable being tested","Fair tests do not need consistent conditions","It is not important at all"], answer:1},
     {q:"If testing how sunlight affects plant growth, what should stay the same between test plants?", options:["The plant species should be different each time","The amount of sunlight only","Nothing needs to stay the same","Water, soil, and pot size"], answer:3},
     {q:"A variable in an experiment is ___.", options:["Something that never changes","The title of the experiment","A factor that can change and affect the results","The name of the scientist"], answer:2},
     {q:"Why do scientists rely on fair tests?", options:["To draw reliable, accurate conclusions from their results","Fair tests are only used outside of science","Fair testing is unnecessary in science","Fair tests make conclusions less reliable"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Local Government: Municipal Roles", summary:"Ontario Grade 4 Social Studies People and Environments strand: municipal (local) governments are responsible for community services such as roads, parks, garbage collection, and local bylaws, led by a mayor and council.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Which level of government is typically responsible for garbage collection?", options:["Federal government","Municipal (local) government","No government handles this","Only the provincial government"], answer:1},
     {q:"A municipal government is usually led by a ___.", options:["Mayor and council","Premier only","Prime Minister","King or Queen"], answer:0},
     {q:"Which is an example of a municipal responsibility?", options:["Setting national trade policy","Printing national currency","Managing the country’s military","Maintaining local roads and parks"], answer:3},
     {q:"A local bylaw is ___.", options:["A rule with no legal effect","A national law that applies to every country","The same as a federal law","A rule created by the municipal government for the local community"], answer:3},
     {q:"Why is municipal government important to daily life?", options:["It has no connection to daily life","Municipal government does not exist in Canada","It only matters once every four years","It manages many of the services communities rely on every day"], answer:3}
   ]},
]},
{day:50, label:"Day 50 — Fri", subjects:[
  {subject:"Language", title:"Reading: Reflecting and Responding to Texts", summary:"Ontario Grade 4 Reading strand: reflecting on a text means thinking about how it connects to your own experiences, other texts, or the world, and forming a thoughtful personal response.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Reflecting on a text means ___.", options:["Ignoring your own thoughts about the text","Immediately forgetting what you read","Only memorizing the text word for word","Thinking about how the text connects to your experiences or the world"], answer:3},
     {q:"A personal response to a text might include ___.", options:["A list of unrelated topics","Only copying sentences from the text","No opinions or thoughts at all","Your own thoughts, feelings, or connections to the text"], answer:3},
     {q:"Connecting a text to your own experience is an example of a ___ connection.", options:["Meaningless","Random","Text-to-nowhere","Text-to-self"], answer:3},
     {q:"Why is reflecting on a text a valuable reading habit?", options:["It deepens understanding and makes reading more meaningful","Reflection only applies to non-fiction","Reflection has no benefit for readers","It replaces the need to read carefully"], answer:0},
     {q:"Which is an example of a text-to-text connection?", options:["Comparing a story to another book you have read","Only focusing on the cover of the book","Comparing a story to a math worksheet only","Ignoring all other texts"], answer:0}
   ]},
  {subject:"Math", title:"Budgeting Basics", summary:"Ontario Grade 4 Financial Literacy strand: a budget is a plan for how to use money, balancing income (money coming in) with expenses (money going out), and setting aside savings when possible.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A budget is best described as ___.", options:["A list of things you already own","A plan for how to use money","A type of bank account only","A rule that forbids spending money"], answer:1},
     {q:"Income refers to ___.", options:["Money coming in","A type of expense","Money that has been lost","Money going out"], answer:0},
     {q:"An expense refers to ___.", options:["Money going out for something purchased","A type of income","Money saved only","Money coming in"], answer:0},
     {q:"If Malik earns $20 in allowance and spends $12, how much is left to save?", options:["$32","$8","$20","$12"], answer:1},
     {q:"Why is it useful to set aside savings in a budget?", options:["Savings serve no useful purpose","A budget should never include savings","To have money available for future needs or goals","Saving money is the same as spending it"], answer:2}
   ]},
  {subject:"Science", title:"Review: Structures, Forces, and Simple Machines", summary:"Ontario Grade 4 Science Structures and Mechanisms strand review: this lesson revisits structures, forces like magnetism and friction, and simple machines like levers, inclined planes, wheels and axles, and screws, from across the year.",
   resourceLabel:"TVO Learn: Grade 4 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Which is an example of a simple machine studied this year?", options:["A mountain","A river","A lever","A cloud"], answer:2},
     {q:"A structure’s ability to support weight without collapsing depends on its ___.", options:["Smell","Design and how it distributes load","Price","Colour"], answer:1},
     {q:"Magnetism is an example of a ___ studied in this unit.", options:["Writing style","Historical event","Type of rock","Force"], answer:3},
     {q:"Which simple machine converts turning motion into straight-line motion?", options:["Screw","Lever","Wheel and axle","Pulley"], answer:0},
     {q:"Why is it useful to review structures, forces, and simple machines together?", options:["These topics have no connection to each other","Review is never useful in science","Each topic must be learned in complete isolation","They are closely connected ideas that build a fuller understanding of mechanisms"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Culminating Task: Comparing an Early Society to Canada Today", summary:"Ontario Grade 4 Social Studies culminating task: students compare daily life, government, and technology in an early society, such as Ancient Egypt or Mesopotamia, with life in Canada today.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Comparing an early society to Canada today can include looking at ___.", options:["Only the weather","Only the colour of buildings","Nothing meaningful","Daily life, government, and technology"], answer:3},
     {q:"Which is a valid comparison between Ancient Egypt and Canada today?", options:["Canada today has pyramids as its main structures","Both have systems of government, though very different in structure","Ancient Egypt used smartphones","Neither society ever had any form of government"], answer:1},
     {q:"Why is comparing past and present societies a valuable learning task?", options:["This kind of comparison is impossible to make","It helps students understand how societies change and what stays similar over time","Comparing societies has no educational value","Past societies have no connection to life today"], answer:1},
     {q:"A culminating task is typically used to ___.", options:["Bring together and apply learning from throughout a unit or year","Introduce a brand new unit with no prior learning","Test only unrelated content","Replace the need for any learning at all"], answer:0},
     {q:"Which skill is most useful when completing a comparison task like this?", options:["Copying text without analysis","Identifying similarities and differences with supporting evidence","Guessing randomly with no evidence","Ignoring one of the two things being compared"], answer:1}
   ]},
]},
{day:51, label:"Day 51 — Mon", subjects:[
  {subject:"Language", title:"Reading: Making Connections (Text-to-Self, Text-to-Text, Text-to-World)", summary:"Grade 4 Language strand: strong readers make connections between a text and their own life, other texts they have read, and events happening in the wider world.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A text-to-self connection is when a reader links a text to ___.", options:["Their own life and experiences","A completely different book only","A concept unrelated to reading","The number of chapters in the book"], answer:0},
     {q:"A text-to-text connection compares a story to ___.", options:["Only the cover illustration of the book","Another text the reader has read before","Nothing at all, since texts cannot be compared","A concept unrelated to reading comprehension"], answer:1},
     {q:"A text-to-world connection links a story to ___.", options:["Only the page count of the text","Events or issues happening in the wider world","A detail unrelated to the story itself","Nothing, since stories have no connection to the world"], answer:1},
     {q:"Why do readers make connections while reading?", options:["Connections only distract readers from the story","It helps deepen understanding and makes the text more meaningful","Making connections never helps a reader understand a text","This strategy has no connection to reading comprehension"], answer:1},
     {q:"If a story about moving to a new school reminds you of your own first day at school, what kind of connection is this?", options:["A text-to-text connection","A text-to-world connection","A concept unrelated to connections","A text-to-self connection"], answer:3}
   ]},
  {subject:"Math", title:"Multiplying Fractions by Whole Numbers", summary:"Grade 4 Math strand: multiplying a fraction by a whole number means adding that fraction the given number of times, such as 3 times 1/4 equalling 3/4.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"Multiplying a fraction by a whole number is the same as ___.", options:["Dividing the fraction into smaller unrelated parts","A concept unrelated to fractions","Subtracting the whole number from the fraction","Adding that fraction the given number of times"], answer:3},
     {q:"What is 3 × 1/4?", options:["A value unrelated to the multiplication","3/4","1/12","4/3"], answer:1},
     {q:"What is 2 × 2/5?", options:["4/5","2/10","5/2","A value unrelated to the multiplication"], answer:0},
     {q:"When multiplying a fraction by a whole number, which part of the fraction changes?", options:["The numerator, while the denominator stays the same","Neither part changes at all","The denominator, while the numerator stays the same","A part unrelated to fractions"], answer:0},
     {q:"What is 4 × 1/3?", options:["3/4","A value unrelated to the multiplication","4/3","1/12"], answer:2}
   ]},
  {subject:"Science", title:"Ecosystems: Interdependence of Living Things", summary:"Grade 4 Science strand: living things in an ecosystem depend on each other and their environment in a web of interdependent relationships.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Interdependence in an ecosystem means living things ___.", options:["A concept unrelated to ecosystems","Live completely apart from their environment","Rely on each other and their environment to survive","Never interact with each other in any way"], answer:2},
     {q:"Which is an example of interdependence in an ecosystem?", options:["A concept unrelated to living things","A rock resting on the ground with no living connections","Two organisms that never interact in any way","Bees pollinating flowers while flowers provide bees with nectar"], answer:3},
     {q:"What might happen if one species disappeared from an ecosystem?", options:["A concept unrelated to ecosystems","Other species that depended on it could also be affected","Nothing in the ecosystem would ever change","Every other species would automatically disappear too"], answer:1},
     {q:"Why do scientists study interdependence in ecosystems?", options:["Ecosystems have no relationships worth studying","Studying interdependence provides no useful scientific information","This concept has no connection to science","It helps them understand how changes affect the whole community of living things"], answer:3},
     {q:"Which best describes a healthy, balanced ecosystem?", options:["A concept unrelated to ecosystems","One where every species lives in complete isolation","One where living things and their environment support each other","One where no living things ever interact"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Mapping Skills: Latitude and Longitude", summary:"Grade 4 Social Studies strand: latitude and longitude are imaginary lines that form a grid on maps and globes, helping people locate exact places on Earth.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Latitude and longitude lines help people ___.", options:["A concept unrelated to maps","Measure the temperature of a location","Determine the population of a city","Locate exact places on Earth"], answer:3},
     {q:"Lines of latitude run ___.", options:["Diagonally across every map","A direction unrelated to mapping","North to south, connecting the poles","East to west, parallel to the equator"], answer:3},
     {q:"Lines of longitude run ___.", options:["East to west, parallel to the equator","A direction unrelated to mapping","North to south, connecting the poles","Diagonally across every map"], answer:2},
     {q:"Why is a grid of latitude and longitude lines useful on maps?", options:["It only shows the colours of different countries","A concept unrelated to geography","It allows any location on Earth to be described with precise coordinates","It has no practical use for finding locations"], answer:2},
     {q:"The equator is a line of ___.", options:["A term unrelated to mapping","Longitude","Elevation","Latitude"], answer:3}
   ]},
]},
{day:52, label:"Day 52 — Tue", subjects:[
  {subject:"Language", title:"Grammar: Subject-Verb Agreement", summary:"Grade 4 Language strand: subject-verb agreement means matching a singular subject with a singular verb and a plural subject with a plural verb.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Subject-verb agreement means the subject and verb must ___.", options:["A concept unrelated to grammar","Be separated by a comma at all times","Match in number (singular or plural)","Always be written in past tense"], answer:2},
     {q:"Which sentence shows correct subject-verb agreement?", options:["The dogs runs in the park.","The dog run in the park.","The dog runs in the park.","A sentence unrelated to subject-verb agreement"], answer:2},
     {q:"Which sentence shows correct subject-verb agreement?", options:["The child play outside.","The children play outside.","The children plays outside.","A sentence unrelated to subject-verb agreement"], answer:1},
     {q:"A singular subject like “she” should be paired with a verb like ___.", options:["Walk","Walks","A verb form unrelated to agreement","Walking, with no other words needed"], answer:1},
     {q:"Why is subject-verb agreement important in writing?", options:["It has no effect on how a sentence reads","A concept unrelated to clear writing","It only matters in spoken language, never in writing","It makes sentences grammatically correct and easier to understand"], answer:3}
   ]},
  {subject:"Math", title:"Introduction to Prime and Composite Numbers", summary:"Grade 4 Math strand: a prime number has exactly two factors (1 and itself), while a composite number has more than two factors.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A prime number has exactly ___ factors.", options:["Two (1 and itself)","Zero factors","Ten factors","A number of factors unrelated to primes"], answer:0},
     {q:"Which of these is a prime number?", options:["8","7","9","A number unrelated to primes"], answer:1},
     {q:"Which of these is a composite number?", options:["17","13","12","A number unrelated to composites"], answer:2},
     {q:"Why is the number 1 neither prime nor composite?", options:["1 is always considered a prime number","It has only one factor, itself, not two or more","A reason unrelated to factors","It has an unlimited number of factors"], answer:1},
     {q:"Which of these numbers is prime?", options:["A number unrelated to primes","15","10","11"], answer:3}
   ]},
  {subject:"Science", title:"Rock and Mineral Classification: Igneous, Sedimentary, Metamorphic", summary:"Grade 4 Science strand: rocks are classified into three types based on how they form -- igneous (from cooled magma), sedimentary (from compressed layers), and metamorphic (changed by heat and pressure).",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Igneous rock forms when ___.", options:["A process unrelated to rock formation","Existing rock is changed by heat and pressure","Melted magma cools and hardens","Layers of sediment are compressed over time"], answer:2},
     {q:"Sedimentary rock forms when ___.", options:["Existing rock is changed by heat and pressure","Melted magma cools and hardens","A process unrelated to rock formation","Layers of sediment are compressed over time"], answer:3},
     {q:"Metamorphic rock forms when ___.", options:["A process unrelated to rock formation","Existing rock is changed by heat and pressure","Layers of sediment are compressed over time","Melted magma cools and hardens"], answer:1},
     {q:"Which is an example of a way scientists classify rocks?", options:["By how the rock was formed","By where the rock is displayed in a museum","A method unrelated to rock classification","By the colour of the rock alone, with no other criteria"], answer:0},
     {q:"Why do geologists classify rocks into these three types?", options:["A reason unrelated to geology","Rocks are never classified into different types","It helps them understand how each rock formed and what it can reveal about Earth’s history","Classifying rocks provides no useful scientific information"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Comparing Government Systems: Federal, Provincial, and Municipal", summary:"Grade 4 Social Studies strand: Canada has three levels of government -- federal, provincial, and municipal -- each responsible for different services and decisions.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"The federal government is responsible for issues that affect ___.", options:["The whole country","A concept unrelated to government","Only a single city","Only a single street"], answer:0},
     {q:"The provincial government is responsible for issues such as ___.", options:["Decisions made only by other countries","A concept unrelated to government","Education and healthcare within the province","International trade agreements only"], answer:2},
     {q:"The municipal government is responsible for issues such as ___.", options:["National defence and foreign policy","Local roads, garbage collection, and community parks","A concept unrelated to government","International trade agreements"], answer:1},
     {q:"Why does Canada have three levels of government?", options:["A reason unrelated to government structure","Only one level of government is actually needed","Having multiple levels of government serves no useful purpose","Different levels can focus on issues at the national, provincial, and local scale"], answer:3},
     {q:"Which level of government would most likely decide on a new local playground?", options:["A level unrelated to local decisions","Federal","Provincial","Municipal"], answer:3}
   ]},
]},
{day:53, label:"Day 53 — Wed", subjects:[
  {subject:"Language", title:"Vocabulary: Root Words", summary:"Grade 4 Language strand: a root word is the base part of a word that carries its core meaning, and many other words can be built from it by adding prefixes or suffixes.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A root word is ___.", options:["A word with no meaning at all","The base part of a word that carries its core meaning","Always the longest word in a sentence","A concept unrelated to vocabulary"], answer:1},
     {q:"What is the root word in “unhappiness”?", options:["Ness","Un","A word unrelated to the root","Happy"], answer:3},
     {q:"What is the root word in “replayed”?", options:["Re","A word unrelated to the root","Play","Ed"], answer:2},
     {q:"Knowing a root word can help a reader ___.", options:["Never understand the meaning of any word","Figure out the meaning of related, unfamiliar words","A concept unrelated to vocabulary","Only memorize spelling patterns"], answer:1},
     {q:"What is the root word in “disagreement”?", options:["A word unrelated to the root","Agree","Dis","Ment"], answer:1}
   ]},
  {subject:"Math", title:"Measuring and Classifying Angles with a Protractor", summary:"Grade 4 Math strand: a protractor is a tool used to measure the size of an angle in degrees, and angles can be classified as acute, right, obtuse, or straight.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A protractor is used to ___.", options:["Measure the weight of an object","A tool unrelated to angles","Measure the length of a line","Measure the size of an angle in degrees"], answer:3},
     {q:"An angle less than 90 degrees is called ___.", options:["Obtuse","Acute","A term unrelated to angles","Straight"], answer:1},
     {q:"An angle greater than 90 degrees but less than 180 degrees is called ___.", options:["A term unrelated to angles","Right","Obtuse","Acute"], answer:2},
     {q:"An angle that measures exactly 90 degrees is called ___.", options:["An obtuse angle","A term unrelated to angles","A right angle","A straight angle"], answer:2},
     {q:"An angle that measures exactly 180 degrees is called ___.", options:["A term unrelated to angles","A right angle","An acute angle","A straight angle"], answer:3}
   ]},
  {subject:"Science", title:"Waves and Vibrations: How Sound is Produced", summary:"Grade 4 Science strand: sound is produced when an object vibrates, creating waves of energy that travel through air or another medium to our ears.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Sound is produced when an object ___.", options:["Vibrates","A process unrelated to sound","Changes colour","Stays perfectly still"], answer:0},
     {q:"Sound waves travel through ___.", options:["A vacuum with no matter at all","Air and other materials, such as water","A concept unrelated to sound","Only through solid metal"], answer:1},
     {q:"What happens to the vibration of a guitar string when it is plucked?", options:["It stops moving completely","It vibrates back and forth, producing sound waves","A result unrelated to sound production","It changes into a different material"], answer:1},
     {q:"Why can we not hear sound in outer space?", options:["A reason unrelated to how sound travels","Sound only exists on Earth for no scientific reason","There is no air or matter for sound waves to travel through","Sound waves travel faster in space, making them silent"], answer:2},
     {q:"Which best describes a sound wave?", options:["A form of energy that travels through vibrations","A form of light that has no connection to vibration","A concept unrelated to sound","A solid object that can be touched"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Canada’s Industries and Economic Regions", summary:"Grade 4 Social Studies strand: different regions of Canada rely on different industries, such as fishing on the coasts, farming on the Prairies, and manufacturing in central Canada.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"An industry is ___.", options:["A type of government department","A concept unrelated to the economy","Only a building where people live","A type of economic activity that produces goods or services"], answer:3},
     {q:"Which industry is closely associated with the Prairie provinces?", options:["Only tourism","Fishing","An industry unrelated to the Prairies","Farming"], answer:3},
     {q:"Which industry is closely associated with Canada’s coastal regions?", options:["Fishing","Only mining","Farming grain crops","An industry unrelated to coastal regions"], answer:0},
     {q:"Why do different regions of Canada rely on different industries?", options:["Industries are assigned randomly to each region","Every region of Canada has identical industries","Each region’s geography and resources shape which industries can thrive there","A reason unrelated to geography"], answer:2},
     {q:"Which industry is closely associated with central Canada?", options:["Only fishing","Only forestry","Manufacturing","An industry unrelated to central Canada"], answer:2}
   ]},
]},
{day:54, label:"Day 54 — Thu", subjects:[
  {subject:"Language", title:"Writing: Compare and Contrast Paragraphs", summary:"Grade 4 Language strand: a compare and contrast paragraph explains how two subjects are similar and how they are different, often using words like “however” and “similarly.”",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A compare and contrast paragraph explains how two subjects are ___.", options:["Only different, never similar","A concept unrelated to writing","Similar and different","Only similar, never different"], answer:2},
     {q:"Which word signals a comparison (similarity) between two ideas?", options:["However","Although","Similarly","A word unrelated to comparison"], answer:2},
     {q:"Which word signals a contrast (difference) between two ideas?", options:["Likewise","A word unrelated to contrast","However","Similarly"], answer:2},
     {q:"Why might a writer compare and contrast two animals in an essay?", options:["A reason unrelated to writing","To help readers understand how the animals are alike and different","Comparing animals serves no purpose in writing","To make the essay longer with no added meaning"], answer:1},
     {q:"What should a compare and contrast paragraph include?", options:["Details about only one of the two subjects","No details at all, only opinions","Specific details about both similarities and differences","A concept unrelated to this type of writing"], answer:2}
   ]},
  {subject:"Math", title:"Volume of Rectangular Prisms", summary:"Grade 4 Math strand: the volume of a rectangular prism is found by multiplying its length, width, and height, and is measured in cubic units.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"The volume of a rectangular prism is found by multiplying ___.", options:["Only the height of the shape","A formula unrelated to volume","Length × width × height","Only length × width"], answer:2},
     {q:"What is the volume of a rectangular prism with length 4, width 3, and height 2?", options:["14 cubic units","A value unrelated to the calculation","9 cubic units","24 cubic units"], answer:3},
     {q:"Volume is measured in ___.", options:["A unit unrelated to volume","Square units","Cubic units","Linear units"], answer:2},
     {q:"What is the volume of a rectangular prism with length 5, width 2, and height 3?", options:["30 cubic units","20 cubic units","A value unrelated to the calculation","10 cubic units"], answer:0},
     {q:"Why is volume measured in cubic units rather than square units?", options:["Square units are always used for volume instead","A reason unrelated to measurement","Because volume describes a three-dimensional space, not a flat area","Cubic units have no real meaning in math"], answer:2}
   ]},
  {subject:"Science", title:"Simple Circuits: Series vs Parallel", summary:"Grade 4 Science strand: in a series circuit, components are connected in a single loop, while in a parallel circuit, components are connected along multiple paths.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"In a series circuit, components are connected ___.", options:["With no connection between them at all","A concept unrelated to circuits","Along a single loop, one after another","Along multiple separate paths"], answer:2},
     {q:"In a parallel circuit, components are connected ___.", options:["Along multiple separate paths","Along a single loop only","With no connection between them at all","A concept unrelated to circuits"], answer:0},
     {q:"What happens to the other bulbs in a series circuit if one bulb burns out?", options:["A result unrelated to circuits","They all turn off, since the loop is broken","They stay lit with no change at all","They become brighter than before"], answer:1},
     {q:"What happens to the other bulbs in a parallel circuit if one bulb burns out?", options:["The others can stay lit, since each has its own path","The entire house loses power","They all turn off immediately","A result unrelated to circuits"], answer:0},
     {q:"Why might parallel circuits be used for household wiring?", options:["A reason unrelated to circuits","Parallel circuits have no practical advantage","Series circuits are always used in houses instead","So that one broken device does not turn off all the others"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Indigenous Governance and Traditional Knowledge", summary:"Grade 4 Social Studies strand: many Indigenous peoples in Canada have long-standing governance systems and traditional knowledge that guide decision-making and care for the land.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Traditional knowledge refers to ___.", options:["Wisdom and practices passed down through generations within a community","Knowledge that has no connection to any community","Information found only in modern textbooks","A concept unrelated to Indigenous peoples"], answer:0},
     {q:"Indigenous governance systems often emphasize ___.", options:["Community decision-making and care for the land","Ignoring the needs of the land and environment","Decisions made entirely without community input","A concept unrelated to governance"], answer:0},
     {q:"Why is it important to learn about Indigenous governance systems?", options:["It builds a fuller understanding of the diverse ways communities have organized themselves","A reason unrelated to social studies","Only one type of governance system has ever existed","Indigenous governance has no relevance to Canadian history"], answer:0},
     {q:"Traditional knowledge is often passed down through ___.", options:["Sources with no connection to community elders","Storytelling, teachings from elders, and lived experience","Written government documents only","A method unrelated to traditional knowledge"], answer:1},
     {q:"Why might traditional knowledge be valuable for understanding the environment?", options:["It is based on guesses with no real observation involved","Traditional knowledge has no connection to the environment","A reason unrelated to Indigenous knowledge","It reflects generations of careful observation and relationship with the land"], answer:3}
   ]},
]},
{day:55, label:"Day 55 — Fri", subjects:[
  {subject:"Language", title:"Reading: Distinguishing Fact from Opinion", summary:"Grade 4 Language strand: a fact is a statement that can be proven true, while an opinion is a personal belief or judgment that cannot be proven.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A fact is a statement that ___.", options:["Reflects only one person’s feelings","A concept unrelated to reading","Can be proven true","Can never be proven either way"], answer:2},
     {q:"An opinion is a statement that ___.", options:["Reflects a personal belief or judgment","Can always be proven true with evidence","Is the same for every single reader","A concept unrelated to reading"], answer:0},
     {q:"Which of these is a fact?", options:["Chocolate ice cream tastes better than vanilla.","Water freezes at 0 degrees Celsius.","A statement unrelated to facts or opinions","Winter is the best season of the year."], answer:1},
     {q:"Which of these is an opinion?", options:["Dogs have four legs.","A dog is a mammal.","A statement unrelated to facts or opinions","Dogs make the best pets."], answer:3},
     {q:"Why is it important for readers to distinguish fact from opinion?", options:["A concept unrelated to reading comprehension","Facts and opinions are always exactly the same thing","This skill has no use when reading any text","It helps them evaluate information critically and avoid being misled"], answer:3}
   ]},
  {subject:"Math", title:"Temperature and Thermometers (Celsius)", summary:"Grade 4 Math strand: temperature is measured in degrees Celsius in Canada, using a thermometer, with 0°C as the freezing point and 100°C as the boiling point of water.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"In Celsius, water freezes at ___.", options:["32 degrees","100 degrees","A temperature unrelated to freezing","0 degrees"], answer:3},
     {q:"In Celsius, water boils at ___.", options:["100 degrees","32 degrees","A temperature unrelated to boiling","0 degrees"], answer:0},
     {q:"A thermometer is used to measure ___.", options:["A quantity unrelated to thermometers","Weight","Temperature","Length"], answer:2},
     {q:"Which temperature would most likely describe a warm summer day in Ontario?", options:["0 degrees Celsius","A temperature unrelated to a warm day","-15 degrees Celsius","28 degrees Celsius"], answer:3},
     {q:"Which temperature would most likely describe a cold winter day in Ontario?", options:["-10 degrees Celsius","30 degrees Celsius","A temperature unrelated to a cold day","100 degrees Celsius"], answer:0}
   ]},
  {subject:"Science", title:"Forces: Balanced and Unbalanced Forces", summary:"Grade 4 Science strand: balanced forces on an object result in no change in motion, while unbalanced forces cause an object to speed up, slow down, or change direction.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Balanced forces on an object result in ___.", options:["The object always changing direction","The object always speeding up","A concept unrelated to forces","No change in the object’s motion"], answer:3},
     {q:"Unbalanced forces on an object can cause it to ___.", options:["Remain in exactly the same state forever","Speed up, slow down, or change direction","Disappear completely","A concept unrelated to forces"], answer:1},
     {q:"If two people push equally hard on opposite sides of a box and it does not move, the forces are ___.", options:["A term unrelated to forces","Balanced","Unbalanced","Nonexistent"], answer:1},
     {q:"If a soccer ball is kicked and starts rolling, what kind of force acted on it?", options:["An unbalanced force","No force at all","A balanced force","A concept unrelated to forces"], answer:0},
     {q:"Why is it useful to understand balanced and unbalanced forces?", options:["A reason unrelated to forces","It helps explain why objects stay still or change their motion","Forces never affect the motion of objects","This concept has no connection to how objects move"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Settlement Patterns: Why Communities Grow Where They Do", summary:"Grade 4 Social Studies strand: communities often form and grow near resources such as fresh water, fertile land, and transportation routes.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Communities often settle near fresh water because it provides ___.", options:["Drinking water, transportation, and support for farming","A concept unrelated to settlement","Only recreational swimming opportunities","No useful resources at all"], answer:0},
     {q:"Fertile land is valuable to a community because it supports ___.", options:["A concept unrelated to settlement patterns","Nothing related to daily life","Farming and food production","Only mining activities"], answer:2},
     {q:"Why might a community grow near a major transportation route, such as a river or railway?", options:["Transportation routes have no effect on where communities grow","Communities never consider transportation when settling","It makes trade and travel to other places easier","A reason unrelated to settlement patterns"], answer:2},
     {q:"Which of these would most likely attract early settlers to an area?", options:["Access to fresh water and fertile land","The colour of the soil alone","A concept unrelated to settlement","An area with no resources of any kind"], answer:0},
     {q:"Why do geographers study settlement patterns?", options:["Communities are located in completely random places","It helps explain why communities are located where they are","Settlement patterns provide no useful information","A reason unrelated to geography"], answer:1}
   ]},
]},
{day:56, label:"Day 56 — Mon", subjects:[
  {subject:"Language", title:"Figurative Language: Hyperbole", summary:"Grade 4 Language strand: hyperbole is an extreme exaggeration used for effect, such as saying “I have a million things to do.”",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Hyperbole is a figure of speech that uses ___.", options:["Extreme exaggeration for effect","Comparisons using “like” or “as”","A concept unrelated to figurative language","Only literal, exact statements"], answer:0},
     {q:"Which sentence contains a hyperbole?", options:["I had a sandwich for lunch today.","I am so hungry I could eat a horse.","I ate a small snack this afternoon.","A sentence unrelated to hyperbole"], answer:1},
     {q:"Why do writers use hyperbole?", options:["To describe something in a completely literal way","Hyperbole is never used for any purpose in writing","A reason unrelated to figurative language","To emphasize a feeling or idea in a dramatic, memorable way"], answer:3},
     {q:"Which sentence contains a hyperbole?", options:["My backpack has three pockets.","This backpack weighs a million pounds!","This backpack is a bit heavy today.","A sentence unrelated to hyperbole"], answer:1},
     {q:"Is hyperbole meant to be taken literally?", options:["Hyperbole has no real meaning at all","No, it is an exaggeration for effect","A concept unrelated to hyperbole","Yes, hyperbole is always literally true"], answer:1}
   ]},
  {subject:"Math", title:"Ratios and Simple Proportional Reasoning (Intro)", summary:"Grade 4 Math strand: a ratio compares two quantities, such as 2 red marbles for every 3 blue marbles, and can be used to solve simple proportional problems.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A ratio is used to ___.", options:["Compare two quantities","Add two quantities together","Measure the length of an object","A concept unrelated to ratios"], answer:0},
     {q:"If a recipe uses a ratio of 2 cups of flour for every 1 cup of sugar, how much flour is needed for 2 cups of sugar?", options:["2 cups","An amount unrelated to the ratio","1 cup","4 cups"], answer:3},
     {q:"A ratio of 3:1 means that for every 3 of one item, there is/are ___ of the other.", options:["3","A number unrelated to the ratio","1","4"], answer:2},
     {q:"If a class has a ratio of 2 boys for every 3 girls, and there are 6 boys, how many girls are there?", options:["3","9","6","A number unrelated to the ratio"], answer:1},
     {q:"Why are ratios useful in everyday life?", options:["A reason unrelated to ratios","Ratios have no practical use in daily life","They help compare quantities and scale recipes, maps, and mixtures accurately","Ratios can only be used in advanced mathematics"], answer:2}
   ]},
  {subject:"Science", title:"States of Matter and the Particle Model", summary:"Grade 4 Science strand: matter exists in solid, liquid, and gas states, and the particle model explains that particles in a solid are tightly packed, in a liquid can move past each other, and in a gas move freely.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"In a solid, particles are ___.", options:["Spread far apart and moving freely","Not present at all","A description unrelated to particles","Tightly packed and vibrate in place"], answer:3},
     {q:"In a liquid, particles ___.", options:["Are completely fixed in place","A description unrelated to particles","Spread out infinitely in all directions","Can move and slide past one another"], answer:3},
     {q:"In a gas, particles ___.", options:["Are tightly packed together","Remain completely still","A description unrelated to particles","Move freely and spread far apart"], answer:3},
     {q:"The particle model helps explain ___.", options:["Only the colour of different materials","A concept unrelated to matter","Nothing about how matter behaves","Why matter behaves differently as a solid, liquid, or gas"], answer:3},
     {q:"Which state of matter has particles that are the most tightly packed?", options:["Solid","Liquid","Gas","A state unrelated to particle spacing"], answer:0}
   ]},
  {subject:"SocialStudies", title:"The Fur Trade in Canadian History", summary:"Grade 4 Social Studies strand: the fur trade was a major economic activity in early Canadian history, involving Indigenous peoples and European traders exchanging goods such as furs, tools, and cloth.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"The fur trade primarily involved the exchange of ___.", options:["Furs for European tools, cloth, and other goods","A concept unrelated to the fur trade","Only gold and silver coins","Modern manufactured electronics"], answer:0},
     {q:"Which group played a central role in the fur trade as both trappers and traders?", options:["Only settlers who arrived after the fur trade ended","A group unrelated to the fur trade","People with no connection to the fur trade at all","Indigenous peoples"], answer:3},
     {q:"Why was the fur trade economically important in early Canada?", options:["A reason unrelated to the fur trade","It only involved a handful of people with no wider impact","It was a major source of income and connected different regions through trade routes","The fur trade had no economic importance in Canadian history"], answer:2},
     {q:"Which animal’s fur was especially valuable during the fur trade?", options:["Beaver","An animal unrelated to the fur trade","Elephant","Kangaroo"], answer:0},
     {q:"How did the fur trade affect relationships between Indigenous peoples and European traders?", options:["It created important economic and social relationships, though they were not always equal","Indigenous peoples and European traders never interacted","A reason unrelated to the fur trade","It had no effect on relationships between the two groups"], answer:0}
   ]},
]},
{day:57, label:"Day 57 — Tue", subjects:[
  {subject:"Language", title:"Spelling: Compound Words", summary:"Grade 4 Language strand: a compound word is formed by joining two smaller words together, such as “sun” and “flower” combining to make “sunflower.”",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A compound word is formed by ___.", options:["Joining two smaller words together","A concept unrelated to spelling","Adding a prefix only, with no second word","Removing letters from a single word"], answer:0},
     {q:"Which of these is a compound word?", options:["A word unrelated to compound words","Running","Happiness","Basketball"], answer:3},
     {q:"What two smaller words make up “rainbow”?", options:["Rain and bow","Ran and bow","Two words unrelated to “rainbow”","Rain and boat"], answer:0},
     {q:"Which of these is a compound word?", options:["A word unrelated to compound words","Toothbrush","Brushed","Brushing"], answer:1},
     {q:"Why is it useful to recognize compound words when spelling?", options:["A concept unrelated to spelling strategies","Compound words cannot be broken into smaller parts","Recognizing compound words never helps with spelling","It helps break a longer word into two familiar, smaller words"], answer:3}
   ]},
  {subject:"Math", title:"Translations, Reflections, and Rotations", summary:"Grade 4 Math strand: a translation slides a shape, a reflection flips a shape like a mirror image, and a rotation turns a shape around a fixed point.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A translation moves a shape by ___.", options:["A movement unrelated to transformations","Turning it around a fixed point","Flipping it like a mirror image","Sliding it without flipping or turning it"], answer:3},
     {q:"A reflection creates a shape that is ___.", options:["An exact copy with no changes at all","A movement unrelated to transformations","A mirror image of the original shape","Always larger than the original shape"], answer:2},
     {q:"A rotation moves a shape by ___.", options:["Turning it around a fixed point","Flipping it like a mirror image","Sliding it in a straight line","A movement unrelated to transformations"], answer:0},
     {q:"If you slide a triangle three squares to the right without flipping or turning it, this is an example of a ___.", options:["Reflection","A term unrelated to transformations","Translation","Rotation"], answer:2},
     {q:"If you flip a shape over a line so it looks like a mirror image, this is an example of a ___.", options:["Reflection","Translation","Rotation","A term unrelated to transformations"], answer:0}
   ]},
  {subject:"Science", title:"Water Conservation and the Water Cycle in Communities", summary:"Grade 4 Science strand: communities rely on the water cycle for fresh water, and conserving water helps protect this limited resource for future use.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Water conservation means ___.", options:["Removing water from the environment permanently","Using water carefully to avoid wasting it","Using as much water as possible at all times","A concept unrelated to water"], answer:1},
     {q:"Which is an example of water conservation at home?", options:["A concept unrelated to conserving water","Watering the lawn during a rainstorm","Turning off the tap while brushing your teeth","Leaving the tap running for no reason"], answer:2},
     {q:"Why is it important for communities to conserve fresh water?", options:["Fresh water is a limited resource that must be shared and protected","A reason unrelated to water conservation","Fresh water is an unlimited resource with no need for conservation","Communities never need to think about their water use"], answer:0},
     {q:"How does the water cycle provide fresh water to communities?", options:["A reason unrelated to the water cycle","Precipitation refills rivers, lakes, and groundwater that communities depend on","Communities create their own water with no natural cycle involved","The water cycle has no connection to community water supplies"], answer:1},
     {q:"Which of these actions helps conserve water in a community?", options:["A concept unrelated to conservation","Leaving leaks unfixed indefinitely","Fixing leaky pipes and faucets promptly","Wasting water intentionally to test the pipes"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canada’s Relationship with the Commonwealth", summary:"Grade 4 Social Studies strand: Canada is a member of the Commonwealth, a voluntary association of countries, most of which were once part of the British Empire, that cooperate on shared goals.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"The Commonwealth is a voluntary association of countries that ___.", options:["Are required to follow identical laws with no independence","Cooperate on shared goals, such as democracy and development","Have no historical connection to one another","A concept unrelated to international relationships"], answer:1},
     {q:"Many Commonwealth countries share a historical connection to ___.", options:["The former British Empire","No shared history at all","Only ancient civilizations","A country unrelated to the Commonwealth"], answer:0},
     {q:"Is Canada required to follow the laws of other Commonwealth countries?", options:["Yes, Canada must follow every Commonwealth country’s laws","No, Canada remains an independent, self-governing country","A concept unrelated to Canada’s independence","Canada has no independent government of its own"], answer:1},
     {q:"Why might countries choose to remain part of the Commonwealth?", options:["Countries are forced to join with no choice involved","To cooperate on shared goals like trade, education, and development","A reason unrelated to international cooperation","Membership provides no benefits of any kind"], answer:1},
     {q:"Which of these is true about the Commonwealth?", options:["It includes only countries that have never had any historical connection","A statement unrelated to the Commonwealth","It includes many countries that were once part of the British Empire","It has existed for less than one year"], answer:2}
   ]},
]},
{day:58, label:"Day 58 — Wed", subjects:[
  {subject:"Language", title:"Writing: Personal Narratives and Journals", summary:"Grade 4 Language strand: a personal narrative tells a true story from the writer’s own life, often written in first person and organized in the order events happened.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A personal narrative tells a story that is ___.", options:["A concept unrelated to writing","Always completely fictional","True and based on the writer’s own life","Written about someone the writer has never met"], answer:2},
     {q:"A personal narrative is usually written in ___.", options:["First person, using “I”","Second person only, using “you”","A point of view unrelated to personal narratives","Third person only, using “they”"], answer:0},
     {q:"Personal narratives are often organized ___.", options:["In reverse alphabetical order","A concept unrelated to organizing a narrative","In the order the events happened","With no order or structure at all"], answer:2},
     {q:"Why might someone keep a journal?", options:["To write only about topics unrelated to their own life","To record personal thoughts, feelings, and experiences over time","Journals serve no purpose for writers","A reason unrelated to journaling"], answer:1},
     {q:"Which is an example of a topic for a personal narrative?", options:["A memorable trip you took with your family","A fictional story about dragons with no basis in real life","A set of instructions for building a model","A concept unrelated to personal narratives"], answer:0}
   ]},
  {subject:"Math", title:"Circle Graphs (Pie Charts)", summary:"Grade 4 Math strand: a circle graph, or pie chart, shows data as slices of a circle, where each slice represents a proportion of the whole.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"A circle graph shows data as ___.", options:["Slices of a circle representing proportions of a whole","A concept unrelated to circle graphs","A list of numbers with no visual representation","A single straight line"], answer:0},
     {q:"In a circle graph, a larger slice represents ___.", options:["A concept unrelated to circle graphs","A smaller proportion of the total data","No data at all","A greater proportion of the total data"], answer:3},
     {q:"If a circle graph shows that 50% of students prefer summer, what fraction of the circle would represent summer?", options:["A fraction unrelated to the data","The entire circle","Half of the circle","A quarter of the circle"], answer:2},
     {q:"Why might someone use a circle graph instead of a bar graph?", options:["A reason unrelated to graphing data","To show how parts relate to the whole as proportions","Bar graphs and circle graphs always show identical information","Circle graphs cannot display any type of data"], answer:1},
     {q:"All of the slices in a circle graph should add up to ___.", options:["50% of the data","0% of the data","100% of the data","A percentage unrelated to circle graphs"], answer:2}
   ]},
  {subject:"Science", title:"Space: The Sun and Its Role in Our Solar System", summary:"Grade 4 Science strand: the Sun is a star at the centre of our solar system, providing the light and heat energy that supports life on Earth.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"The Sun is best described as a ___.", options:["A concept unrelated to space","Moon that orbits another planet","Star at the centre of our solar system","Planet that orbits the Earth"], answer:2},
     {q:"The Sun provides Earth with ___.", options:["Only darkness","Light and heat energy","No energy of any kind","A concept unrelated to the Sun"], answer:1},
     {q:"Why is the Sun important for life on Earth?", options:["The Sun has no connection to life on Earth","It provides the energy that plants and other living things depend on","Life on Earth exists with no need for any energy source","A reason unrelated to the Sun’s role"], answer:1},
     {q:"All the planets in our solar system orbit ___.", options:["The Sun","A body unrelated to our solar system","Earth","The Moon"], answer:0},
     {q:"Compared to the planets, the Sun is ___.", options:["Exactly the same size as Earth","Much smaller and reflects light from Earth","A description unrelated to the Sun","Far larger and is a source of its own light"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Comparing Urban, Suburban, and Rural Communities", summary:"Grade 4 Social Studies strand: communities can be classified as urban (city), suburban (residential areas near a city), or rural (countryside), each with different features and ways of life.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"An urban community is best described as ___.", options:["An area with very few people and mostly farmland","A densely populated city area","A concept unrelated to communities","A community found only in the far north"], answer:1},
     {q:"A rural community is best described as ___.", options:["A countryside area often used for farming, with a lower population","A densely populated downtown core","An area with no land used for any purpose","A concept unrelated to communities"], answer:0},
     {q:"A suburban community is best described as ___.", options:["A concept unrelated to communities","The very centre of a large city","An area used only for large-scale farming","A residential area located near, but outside, a city’s downtown"], answer:3},
     {q:"Which of these might you expect to find more often in a rural community?", options:["Subway systems","Large farms and open land","A feature unrelated to rural communities","Tall skyscrapers and dense traffic"], answer:1},
     {q:"Why is it useful to compare urban, suburban, and rural communities?", options:["These types of communities have no differences worth studying","It helps show how geography and population shape different ways of life","All communities in Canada are identical","A reason unrelated to social studies"], answer:1}
   ]},
]},
{day:59, label:"Day 59 — Thu", subjects:[
  {subject:"Language", title:"Reading: Using Graphic Organizers", summary:"Grade 4 Language strand: graphic organizers, such as Venn diagrams and story maps, help readers visually organize information and ideas from a text.",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"A graphic organizer helps readers ___.", options:["Visually organize information and ideas from a text","Memorize a text word for word","Avoid reading the text at all","A concept unrelated to reading"], answer:0},
     {q:"A Venn diagram is often used to show ___.", options:["A concept unrelated to graphic organizers","Similarities and differences between two things","The order of events in a single story only","The page numbers of a book"], answer:1},
     {q:"A story map is often used to organize ___.", options:["A concept unrelated to graphic organizers","The price of a book","The characters, setting, problem, and events of a story","Only the title of a book"], answer:2},
     {q:"Why might a reader use a graphic organizer before writing a summary?", options:["Graphic organizers never help with understanding a text","It replaces the need to read the text at all","It helps sort out the most important ideas and details first","A reason unrelated to reading strategies"], answer:2},
     {q:"Which graphic organizer would best help compare two book characters?", options:["A Venn diagram","A number line","A concept unrelated to graphic organizers","A single unrelated list"], answer:0}
   ]},
  {subject:"Math", title:"Mean, Median, and Mode (Intro)", summary:"Grade 4 Math strand: the mean is the average of a set of numbers, the median is the middle value when numbers are ordered, and the mode is the value that appears most often.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"The mean of a set of numbers is found by ___.", options:["Choosing the largest number in the set","Adding all the numbers and dividing by how many there are","A method unrelated to finding the mean","Choosing the smallest number in the set"], answer:1},
     {q:"The median of a set of numbers is ___.", options:["The sum of all the numbers","A value unrelated to the median","The middle value when the numbers are placed in order","Always the first number listed"], answer:2},
     {q:"The mode of a set of numbers is ___.", options:["The value that appears most often","A value unrelated to the mode","The average of all the values","The largest value in the set"], answer:0},
     {q:"What is the median of the set 2, 4, 6, 8, 10?", options:["4","6","A value unrelated to the median","10"], answer:1},
     {q:"What is the mode of the set 3, 5, 5, 7, 9?", options:["9","A value unrelated to the mode","5","3"], answer:2}
   ]},
  {subject:"Science", title:"Energy Transformations in Everyday Devices", summary:"Grade 4 Science strand: many everyday devices transform energy from one form to another, such as a toaster changing electrical energy into heat energy.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Energy transformation means energy ___.", options:["Stays in the exact same form forever","A concept unrelated to energy","Disappears completely with no trace","Changes from one form into another"], answer:3},
     {q:"A toaster transforms electrical energy into ___.", options:["A form of energy unrelated to toasters","Sound energy only","Light energy only","Heat energy"], answer:3},
     {q:"A light bulb transforms electrical energy into ___.", options:["A form of energy unrelated to light bulbs","Light energy (and some heat energy)","Sound energy only","Chemical energy only"], answer:1},
     {q:"A speaker transforms electrical energy into ___.", options:["A form of energy unrelated to speakers","Heat energy only","Sound energy","Light energy only"], answer:2},
     {q:"Why is it useful to understand energy transformations in devices?", options:["It helps explain how everyday technology works and uses energy","Devices never use or change energy in any way","Energy transformations have no connection to how devices work","A reason unrelated to energy"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Cultural Diversity and Multiculturalism in Canada", summary:"Grade 4 Social Studies strand: Canada is home to people from many different cultural backgrounds, and multiculturalism celebrates and protects this diversity as an official policy.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Multiculturalism is a policy that ___.", options:["Requires everyone to share the exact same culture","Ignores the cultural backgrounds of Canadians","A concept unrelated to Canadian society","Celebrates and protects Canada’s cultural diversity"], answer:3},
     {q:"Cultural diversity in a community means ___.", options:["A concept unrelated to communities","No cultural traditions are practiced at all","Everyone in the community shares an identical background","People from many different cultural backgrounds live together"], answer:3},
     {q:"Which is an example of cultural diversity in a Canadian community?", options:["Neighbours celebrating different cultural festivals throughout the year","A concept unrelated to cultural diversity","A town with no cultural traditions of any kind","A community where only one culture is ever represented"], answer:0},
     {q:"Why does Canada value multiculturalism?", options:["Canada requires all citizens to abandon their cultural traditions","Multiculturalism provides no value to Canadian society","It recognizes and respects the contributions of people from many backgrounds","A reason unrelated to Canadian identity"], answer:2},
     {q:"How might multiculturalism be reflected in a Canadian city?", options:["A concept unrelated to multiculturalism","Through a complete absence of cultural variety","Through laws banning cultural celebrations","Through diverse foods, festivals, languages, and traditions"], answer:3}
   ]},
]},
{day:60, label:"Day 60 — Fri", subjects:[
  {subject:"Language", title:"Grammar: Capitalization Rules", summary:"Grade 4 Language strand: capitalization rules include starting every sentence with a capital letter, capitalizing proper nouns, and capitalizing the pronoun “I.”",
   resourceLabel:"TVO Learn: Grade 4 Language", resourceUrl:"https://tvolearn.com/pages/grade-4-language",
   quiz:[
     {q:"Every sentence should begin with ___.", options:["A lowercase letter","A number, with no letters at all","A concept unrelated to capitalization","A capital letter"], answer:3},
     {q:"Proper nouns, such as names of people and places, should be ___.", options:["Capitalized","A concept unrelated to proper nouns","Underlined instead of capitalized","Written entirely in lowercase"], answer:0},
     {q:"The pronoun “I” should always be ___.", options:["Capitalized, no matter where it appears in a sentence","Written in lowercase at the start of a sentence","A concept unrelated to capitalization","Left out of formal writing entirely"], answer:0},
     {q:"Which sentence uses capitalization correctly?", options:["A sentence unrelated to capitalization","My friend and I visited Toronto last summer.","my friend and i visited toronto last summer.","My friend and i visited Toronto last Summer."], answer:1},
     {q:"Why are capitalization rules important in writing?", options:["They help readers understand sentence boundaries and identify proper nouns","A concept unrelated to grammar","Capitalization has no effect on how writing is understood","Capital letters are only used to make writing look nicer"], answer:0}
   ]},
  {subject:"Math", title:"Review: Fractions, Decimals, and Patterns", summary:"Grade 4 Math strand: this review lesson revisits key ideas from Days 51-60, including multiplying fractions, angles, ratios, transformations, and mean/median/mode.",
   resourceLabel:"TVO Learn: Grade 4 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-4-mathematics",
   quiz:[
     {q:"Multiplying a fraction by a whole number is the same as ___.", options:["A concept unrelated to fractions","Subtracting the fraction from the whole number","Adding that fraction the given number of times","Dividing the whole number by the fraction"], answer:2},
     {q:"A protractor is used to measure ___.", options:["Length","Angles","Weight","A quantity unrelated to protractors"], answer:1},
     {q:"A ratio is used to ___.", options:["Measure the volume of a container","Round a number to the nearest ten","A concept unrelated to ratios","Compare two quantities"], answer:3},
     {q:"A translation moves a shape by ___.", options:["Turning it around a fixed point","Flipping it like a mirror image","A movement unrelated to transformations","Sliding it without flipping or turning it"], answer:3},
     {q:"Why is it useful to review fractions, angles, ratios, and data together?", options:["Review never helps strengthen understanding of a subject","These topics have no connection to each other","A reason unrelated to reviewing math","It reinforces how these math concepts connect and build on one another"], answer:3}
   ]},
  {subject:"Science", title:"Review: Forces, Structures, and Systems", summary:"Grade 4 Science strand: this review lesson revisits key ideas from Days 51-60, including ecosystems, rock classification, sound, circuits, balanced forces, states of matter, and energy transformations.",
   resourceLabel:"TVO Learn: Grade 4 Science and Technology", resourceUrl:"https://tvolearn.com/pages/grade-4-science-and-technology",
   quiz:[
     {q:"Interdependence in an ecosystem means living things ___.", options:["Live completely apart from their environment","A concept unrelated to ecosystems","Rely on each other and their environment to survive","Never interact with each other in any way"], answer:2},
     {q:"Balanced forces on an object result in ___.", options:["No change in the object’s motion","The object always changing direction","The object always speeding up","A concept unrelated to forces"], answer:0},
     {q:"In a series circuit, components are connected ___.", options:["A concept unrelated to circuits","Along multiple separate paths","With no connection between them at all","Along a single loop, one after another"], answer:3},
     {q:"Energy transformation means energy ___.", options:["Changes from one form into another","A concept unrelated to energy","Disappears completely with no trace","Stays in the exact same form forever"], answer:0},
     {q:"Why is it useful to review forces, circuits, and energy together?", options:["Each topic must be studied with no connection to the others","These topics have no connection to each other","Review is never useful in science","It reinforces how these interconnected science concepts relate to one another"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Culminating Task: Designing a Model Community", summary:"Grade 4 Social Studies strand: this culminating task asks students to apply Days 51-60 learning about mapping, government, industries, settlement, and diversity to design a model community.",
   resourceLabel:"TVO Learn: Grade 4 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-4-social-studies",
   quiz:[
     {q:"Why might a student consider access to fresh water when designing a model community?", options:["Communities have historically settled near water for drinking, transportation, and farming","A reason unrelated to settlement patterns","Model communities never need to consider natural resources","Fresh water has no connection to where communities are located"], answer:0},
     {q:"Why might a student include all three levels of government when planning a model community?", options:["Levels of government have no connection to community planning","Different levels of government are each responsible for different community needs","A community only ever needs a single level of government","A reason unrelated to Canadian government structure"], answer:1},
     {q:"Why might a student choose to include diverse cultural festivals in a model community?", options:["It reflects the value of cultural diversity and multiculturalism seen in real Canadian communities","A reason unrelated to multiculturalism","Model communities should avoid representing any culture at all","Cultural diversity has no relevance to designing a community"], answer:0},
     {q:"Why might a student include local industries, such as farming or manufacturing, in a model community?", options:["A reason unrelated to economics","Industries reflect how a community’s geography supports its economy","Every community relies on exactly the same industry","Industries have no connection to how a community functions"], answer:1},
     {q:"Why is a culminating task a valuable way to end this set of Social Studies lessons?", options:["Culminating tasks never help reinforce prior learning","A reason unrelated to social studies learning","Applying multiple ideas together provides no educational benefit","It lets students apply many ideas from the unit together in one project"], answer:3}
   ]},
]},
];

export default curriculum;