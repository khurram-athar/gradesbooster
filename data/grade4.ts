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
   quiz:[
     {q:"A synonym for 'happy' is ___.", options:["joyful","angry","sad","tired"], answer:0},
     {q:"An antonym for 'ancient' is ___.", options:["historic","modern","past","old"], answer:1},
     {q:"Which pair are synonyms?", options:["big/large","fast/slow","night/day","hot/cold"], answer:0},
     {q:"Which pair are antonyms?", options:["quick/fast","bright/dim","small/tiny","glad/happy"], answer:1},
     {q:"Using synonyms in writing helps to ___.", options:["shorten writing","avoid repetition and add variety","change the topic","confuse the reader"], answer:1}
   ]},
  {subject:"Math", title:"2-Digit × 1-Digit Multiplication", summary:"Grade 4 Number strand: multiply 2-digit numbers by 1-digit numbers using the distributive property and place value.",
   resourceLabel:"YouTube: 2-Digit × 1-Digit Multiplication", resourceUrl:"https://www.youtube.com/results?search_query=2-Digit%20%C3%97%201-Digit%20Multiplication%20grade%204%20educational",
   quiz:[
     {q:"23 × 4 = ?", options:["92","72","102","82"], answer:0},
     {q:"45 × 3 = ?", options:["115","135","125","145"], answer:1},
     {q:"67 × 2 = ?", options:["144","134","114","124"], answer:1},
     {q:"To solve 34 × 5, you can think 30×5 + 4×5 = ?", options:["170","160","150","180"], answer:0},
     {q:"Which is correct: 58 × 3 = ?", options:["184","164","154","174"], answer:3}
   ]},
  {subject:"Science", title:"Adaptations", summary:"Grade 4 Science Life Systems: adaptations are physical or behavioural features that help organisms survive in their habitat.",
   resourceLabel:"YouTube: Adaptations", resourceUrl:"https://www.youtube.com/results?search_query=Adaptations%20grade%204%20educational",
   quiz:[
     {q:"An adaptation is ___.", options:["a feature that helps an organism survive","a food chain stage","a type of habitat","a community interaction"], answer:0},
     {q:"A polar bear's white fur is an adaptation that helps it ___.", options:["stay warmer in summer","swim faster","camouflage in snowy environments","attract mates"], answer:2},
     {q:"A cactus stores water in its thick stem as an adaptation to ___.", options:["cold climates","rainy environments","desert environments with little rain","forest life"], answer:2},
     {q:"Which is a behavioural adaptation?", options:["Bird's hollow bones","Birds migrating south in winter","Duck's webbed feet","Fish gills"], answer:1},
     {q:"Camouflage is an adaptation that helps animals ___.", options:["stay hidden from predators or prey","find water","run faster","digest food better"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Ancient Greece", summary:"Grade 4 Social Studies: Ancient Greece developed democracy, philosophy, the Olympics, and architecture that influenced the Western world.",
   resourceLabel:"YouTube: Ancient Greece", resourceUrl:"https://www.youtube.com/results?search_query=Ancient%20Greece%20grade%204%20educational",
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
   quiz:[
     {q:"What does the prefix 'un-' mean?", options:["again","before","after","not"], answer:3},
     {q:"What does 'unhappy' mean?", options:["before happy","happy again","very happy","not happy"], answer:3},
     {q:"What does the suffix '-ful' mean?", options:["full of","without","before","again"], answer:0},
     {q:"Which word means 'without hope'?", options:["hopeless","hopeful","rehope","hopefully"], answer:0},
     {q:"What does 'redo' mean?", options:["not do","do again","do before","do after"], answer:1}
   ]},
  {subject:"Math", title:"Introduction to Long Division", summary:"Grade 4 Number strand: students divide 2-digit dividends by 1-digit divisors, understanding quotient and remainder.",
   resourceLabel:"YouTube: Introduction to Long Division", resourceUrl:"https://www.youtube.com/results?search_query=Introduction%20to%20Long%20Division%20grade%204%20educational",
   quiz:[
     {q:"In division, the number being divided is the ___.", options:["dividend","divisor","quotient","remainder"], answer:0},
     {q:"In division, the number dividing is the ___.", options:["dividend","remainder","divisor","quotient"], answer:2},
     {q:"27 ÷ 4 = 6 remainder ___.", options:["4","2","3","1"], answer:2},
     {q:"37 ÷ 5 = ?", options:["7 r2","7 r3","8 r1","6 r7"], answer:0},
     {q:"A remainder in division is ___.", options:["the divisor","the answer","how many are left over","the quotient"], answer:2}
   ]},
  {subject:"Science", title:"Biodiversity", summary:"Grade 4 Science Life Systems: biodiversity means the variety of living organisms in an ecosystem. Greater biodiversity usually means a healthier ecosystem.",
   resourceLabel:"YouTube: Biodiversity", resourceUrl:"https://www.youtube.com/results?search_query=Biodiversity%20grade%204%20educational",
   quiz:[
     {q:"Biodiversity means ___.", options:["the size of an ecosystem","the number of plants only","the variety of living organisms in an area","only one type of organism"], answer:2},
     {q:"Greater biodiversity usually means ___.", options:["a healthier, more stable ecosystem","only large animals","a less stable ecosystem","fewer species"], answer:0},
     {q:"Which habitat has the greatest biodiversity?", options:["A single-crop farm","An empty field","A parking lot","A tropical rainforest"], answer:3},
     {q:"How does biodiversity benefit humans?", options:["It provides food and medicine","Only animals benefit","Only scientists benefit","It does not"], answer:0},
     {q:"What threatens biodiversity?", options:["More trees","Habitat loss","Clean water","Too much rain"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Ancient Rome", summary:"Grade 4 Social Studies: Ancient Rome built a vast empire, developing law, engineering, and governance that influenced modern Western civilization.",
   resourceLabel:"YouTube: Ancient Rome", resourceUrl:"https://www.youtube.com/results?search_query=Ancient%20Rome%20grade%204%20educational",
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
   quiz:[
     {q:"The main idea is ___.", options:["the last sentence","what the entire text is mostly about","a small detail","the topic sentence only"], answer:1},
     {q:"Supporting details ___.", options:["explain or prove the main idea","are unrelated to the main idea","are always at the beginning","are more important than the main idea"], answer:0},
     {q:"Where is the main idea often found?", options:["In a caption","Only in the middle","First or last sentence","Only at the end"], answer:2},
     {q:"How do you identify the main idea?", options:["Count the paragraphs","Read only the title","Read only the last line","Ask 'What is this MOSTLY about?'"], answer:3},
     {q:"Which is a main idea sentence?", options:["She walked to the store.","The cat was orange.","He ate lunch at noon.","Recycling helps the environment."], answer:3}
   ]},
  {subject:"Math", title:"Fractions: Equal Parts", summary:"Grade 4 Number strand: a fraction represents equal parts of a whole. The numerator shows how many parts are selected; the denominator shows total equal parts.",
   resourceLabel:"YouTube: Fractions: Equal Parts", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%3A%20Equal%20Parts%20grade%204%20educational",
   quiz:[
     {q:"In the fraction 3/4, the denominator is ___.", options:["1","7","4","3"], answer:2},
     {q:"In the fraction 3/4, the numerator is ___.", options:["7","1","4","3"], answer:3},
     {q:"Which fraction represents half?", options:["1/2","1/3","2/3","1/4"], answer:0},
     {q:"A pizza is cut into 8 equal slices. You eat 3. What fraction did you eat?", options:["3/5","3/8","5/8","8/3"], answer:1},
     {q:"The denominator in a fraction tells you ___.", options:["whether the fraction is big","the size of each part","the total number of equal parts","how many parts you have"], answer:2}
   ]},
  {subject:"Science", title:"Human Impact on Ecosystems", summary:"Grade 4 Science Life Systems: human activities such as deforestation, pollution, and urbanization negatively affect ecosystems; conservation actions help protect them.",
   resourceLabel:"YouTube: Human Impact on Ecosystems", resourceUrl:"https://www.youtube.com/results?search_query=Human%20Impact%20on%20Ecosystems%20grade%204%20educational",
   quiz:[
     {q:"Which human activity HARMS ecosystems?", options:["Composting","Dumping waste in rivers","Creating nature reserves","Planting trees"], answer:1},
     {q:"Deforestation means ___.", options:["studying forests","planting forests","protecting forests","cutting down forests"], answer:3},
     {q:"Which action helps PROTECT ecosystems?", options:["Littering","Building factories near rivers","Polluting water","Creating national parks"], answer:3},
     {q:"How does pollution affect wildlife?", options:["Only fish are affected","Only birds are affected","It destroys habitats and harms organisms","It helps wildlife"], answer:2},
     {q:"What can individuals do to reduce environmental impact?", options:["Drive more cars","Cut down more trees","Use more plastic","Reduce, reuse, and recycle"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Indigenous Peoples of North America", summary:"Grade 4 Social Studies: Indigenous peoples of North America include many diverse nations, each with unique cultures, languages, and governance systems.",
   resourceLabel:"YouTube: Indigenous Peoples of North America", resourceUrl:"https://www.youtube.com/results?search_query=Indigenous%20Peoples%20of%20North%20America%20grade%204%20educational",
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
   quiz:[
     {q:"An inference is ___.", options:["the main idea","a conclusion from clues and knowledge","directly stated in the text","a guess with no evidence"], answer:1},
     {q:"What clues help you make an inference?", options:["The book cover only","Only pictures","Random guessing","Text evidence plus what you already know"], answer:3},
     {q:"Maria grabbed her umbrella before leaving. You can infer ___.", options:["She forgot her coat","She likes umbrellas","She is going swimming","It was probably raining"], answer:3},
     {q:"The book's cover shows a spaceship. You can infer the story is about ___.", options:["History","Farming","Cooking","Space/science fiction"], answer:3},
     {q:"After making an inference, a good reader ___.", options:["Reads on to check the inference","Ignores it","Stops reading","Tells others"], answer:0}
   ]},
  {subject:"Math", title:"Comparing Fractions", summary:"Grade 4 Number strand: to compare fractions with the same denominator, compare numerators. To compare different denominators, find equivalent fractions.",
   resourceLabel:"YouTube: Comparing Fractions", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Fractions%20grade%204%20educational",
   quiz:[
     {q:"Which is greater: 3/5 or 1/5?", options:["1/5","Equal","Cannot tell","3/5"], answer:3},
     {q:"Which fraction is closest to 1 (whole)?", options:["0/4","3/4","1/4","2/4"], answer:1},
     {q:"1/2 is ___ 1/4.", options:["equal to","not comparable to","less than","greater than"], answer:3},
     {q:"Order from least to greatest: 3/8, 1/8, 7/8", options:["7/8, 3/8, 1/8","3/8, 1/8, 7/8","1/8, 7/8, 3/8","1/8, 3/8, 7/8"], answer:3},
     {q:"Which is the largest fraction?", options:["1/3","5/6","2/3","1/6"], answer:1}
   ]},
  {subject:"Science", title:"Rocks and Minerals", summary:"Grade 4 Science Earth strand: rocks are made of minerals. The three rock types are igneous, sedimentary, and metamorphic, each formed by different processes.",
   resourceLabel:"YouTube: Rocks and Minerals", resourceUrl:"https://www.youtube.com/results?search_query=Rocks%20and%20Minerals%20grade%204%20educational",
   quiz:[
     {q:"The three types of rocks are igneous, sedimentary, and ___.", options:["metamorphic","fossil","volcanic","crystal"], answer:0},
     {q:"Igneous rock forms from ___.", options:["cooled magma or lava","compressed sediment","plant material","other rocks under pressure"], answer:0},
     {q:"Sedimentary rock forms from ___.", options:["magma","only volcanic activity","layers of sediment compressed over time","magma and pressure"], answer:2},
     {q:"Metamorphic rock forms when ___.", options:["lava cools","sediment is compressed","glaciers melt","rock changed by heat and pressure"], answer:3},
     {q:"Fossils are most often found in ___.", options:["sedimentary rock","granite","metamorphic rock","igneous rock"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Early Canadian History", summary:"Grade 4 Social Studies: Canada's early history includes Indigenous peoples, European exploration, New France, and British colonization.",
   resourceLabel:"YouTube: Early Canadian History", resourceUrl:"https://www.youtube.com/results?search_query=Early%20Canadian%20History%20grade%204%20educational",
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
   quiz:[
     {q:"The topic sentence in a paragraph ___.", options:["ends the paragraph","is unrelated to the other sentences","gives a detail","states the main idea of the paragraph"], answer:3},
     {q:"Supporting sentences in a paragraph ___.", options:["end the paragraph","are optional","support the topic sentence with details","introduce new topics"], answer:2},
     {q:"A concluding sentence ___.", options:["asks a question","introduces the topic","adds a new idea","wraps up the main idea"], answer:3},
     {q:"How many main ideas should one paragraph have?", options:["One","Two or three","None","As many as possible"], answer:0},
     {q:"Which would make a good topic sentence for a paragraph about dogs?", options:["Dogs can run.","My dog is named Rex.","Dogs make excellent pets.","Dogs are brown."], answer:2}
   ]},
  {subject:"Math", title:"Adding Fractions with Same Denominator", summary:"Grade 4 Number strand: to add fractions with the same denominator, add the numerators and keep the denominator the same.",
   resourceLabel:"YouTube: Adding Fractions with Same Denominator", resourceUrl:"https://www.youtube.com/results?search_query=Adding%20Fractions%20with%20Same%20Denominator%20grade%204%20educational",
   quiz:[
     {q:"1/5 + 2/5 = ?", options:["3/10","2/10","1/5","3/5"], answer:3},
     {q:"2/7 + 3/7 = ?", options:["1/7","6/7","5/7","5/14"], answer:2},
     {q:"3/8 + 4/8 = ?", options:["7/16","1/8","7/8","6/8"], answer:2},
     {q:"When adding fractions with the same denominator, the denominator ___.", options:["doubles","stays the same","adds too","becomes 0"], answer:1},
     {q:"1/4 + 2/4 = ?", options:["1/2","3/8","3/4","2/4"], answer:2}
   ]},
  {subject:"Science", title:"Rock Cycle", summary:"Grade 4 Science Earth strand: rocks cycle continuously between igneous, sedimentary, and metamorphic forms through geological processes.",
   resourceLabel:"YouTube: Rock Cycle", resourceUrl:"https://www.youtube.com/results?search_query=Rock%20Cycle%20grade%204%20educational",
   quiz:[
     {q:"What drives the rock cycle?", options:["Heat, pressure, and surface weathering","The moon's gravity","Only volcanic eruptions","Wind and rain only"], answer:0},
     {q:"Weathering and erosion break rocks into ___.", options:["sediment","lava","magma","crystals"], answer:0},
     {q:"Sediment that is compressed and cemented forms ___.", options:["sedimentary rock","metamorphic rock","lava","igneous rock"], answer:0},
     {q:"When magma cools it forms ___.", options:["sediment","igneous rock","sedimentary rock","metamorphic rock"], answer:1},
     {q:"The rock cycle shows that rocks ___.", options:["are always igneous","only come from volcanoes","can transform from one type to another","never change"], answer:2}
   ]},
  {subject:"SocialStudies", title:"European Explorers", summary:"Grade 4 Social Studies: European explorers from the 1400s–1600s sailed to North America, changing the world and affecting Indigenous peoples significantly.",
   resourceLabel:"YouTube: European Explorers", resourceUrl:"https://www.youtube.com/results?search_query=European%20Explorers%20grade%204%20educational",
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
   quiz:[
     {q:"Descriptive writing uses ___.", options:["only facts and numbers","sensory details and vivid language","only dialogue","only action verbs"], answer:1},
     {q:"Which is a more descriptive sentence?", options:["I saw a flower.","The crimson rose smelled sweet.","The flower was nice.","The flower was red."], answer:1},
     {q:"Sensory details include descriptions of ___.", options:["mathematics","sight, sound, smell, touch, and taste","grammar rules only","sentence structure"], answer:1},
     {q:"Vivid adjectives make writing ___.", options:["more boring","harder to read","shorter","more specific and engaging"], answer:3},
     {q:"Which word is more vivid?", options:["ecstatic","okay","happy","fine"], answer:0}
   ]},
  {subject:"Math", title:"Decimals: Tenths", summary:"Grade 4 Number strand: a decimal is another way to write a fraction. Tenths represent parts of a whole divided into 10 equal parts (e.g., 0.3 = 3/10).",
   resourceLabel:"YouTube: Decimals: Tenths", resourceUrl:"https://www.youtube.com/results?search_query=Decimals%3A%20Tenths%20grade%204%20educational",
   quiz:[
     {q:"0.7 means ___.", options:["7 tenths","7 ones","7 hundredths","70 ones"], answer:0},
     {q:"Which decimal equals 3/10?", options:["0.03","30.0","0.3","3.0"], answer:2},
     {q:"What is 6 tenths as a decimal?", options:["0.06","6.0","60.0","0.6"], answer:3},
     {q:"0.1 + 0.4 = ?", options:["0.5","0.04","0.3","5.0"], answer:0},
     {q:"Which is less than 0.5?", options:["0.9","0.3","0.6","0.8"], answer:1}
   ]},
  {subject:"Science", title:"Soil Formation", summary:"Grade 4 Science Earth strand: soil forms over thousands of years by weathering of rock and addition of organic matter. It has layers called horizons.",
   resourceLabel:"YouTube: Soil Formation", resourceUrl:"https://www.youtube.com/results?search_query=Soil%20Formation%20grade%204%20educational",
   quiz:[
     {q:"Soil forms from ___.", options:["weathered rock and organic matter","only sand","water alone","only plants"], answer:0},
     {q:"The top layer of soil is ___.", options:["bedrock","parent material","topsoil (humus-rich)","subsoil"], answer:2},
     {q:"Topsoil is important because ___.", options:["it contains no water","it is the hardest layer","it is rich in nutrients for plants","it is made of solid rock"], answer:2},
     {q:"How long does it take to form good soil?", options:["Hundreds to thousands of years","Only in rainy seasons","A few days","A few years"], answer:0},
     {q:"What does humus in soil come from?", options:["Water","Decayed plants and animals","Rocks only","Sand and gravel"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Government: Democracy and Monarchy", summary:"Grade 4 Social Studies: governments organize society and make laws. A democracy gives citizens a voice; a monarchy is led by a king or queen.",
   resourceLabel:"YouTube: Government: Democracy and Monarchy", resourceUrl:"https://www.youtube.com/results?search_query=Government%3A%20Democracy%20and%20Monarchy%20grade%204%20educational",
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
   quiz:[
     {q:"The purpose of persuasive writing is to ___.", options:["tell a story","describe something","convince the reader to act","explain how to do something"], answer:2},
     {q:"A persuasive text should include ___.", options:["a clear opinion, reasons, and evidence","a fictional story","only opinions with no evidence","only facts with no opinion"], answer:0},
     {q:"Which is a good opinion statement for a persuasive text?", options:["Some students eat lunch.","Dogs exist.","Schools should have longer lunch breaks.","Dogs can run."], answer:2},
     {q:"Counter-arguments in persuasive writing ___.", options:["are unrelated to the topic","should always be avoided","weaken your argument","acknowledge and refute opposing views"], answer:3},
     {q:"A call to action at the end of a persuasive text asks the reader to ___.", options:["do something or change their view","summarize what they read","stop reading","find more information"], answer:0}
   ]},
  {subject:"Math", title:"Decimals: Hundredths", summary:"Grade 4 Number strand: hundredths represent parts of a whole divided into 100 equal parts. 0.23 = 23/100 = 2 tenths + 3 hundredths.",
   resourceLabel:"YouTube: Decimals: Hundredths", resourceUrl:"https://www.youtube.com/results?search_query=Decimals%3A%20Hundredths%20grade%204%20educational",
   quiz:[
     {q:"0.47 means ___.", options:["47 hundredths","4 tenths 7 ones","47 tenths","47 ones"], answer:0},
     {q:"Which decimal equals 15/100?", options:["0.15","1.5","15.0","0.015"], answer:0},
     {q:"What is 8 hundredths as a decimal?", options:["8.0","0.08","80.0","0.8"], answer:1},
     {q:"0.25 + 0.50 = ?", options:["0.55","0.25","0.75","0.70"], answer:2},
     {q:"Which is greater: 0.3 or 0.30?", options:["Cannot compare","Equal — they are the same","0.3","0.30"], answer:1}
   ]},
  {subject:"Science", title:"Properties of Light: Reflection", summary:"Grade 4 Science Energy strand: light travels in straight lines and reflects off surfaces. The angle of incidence equals the angle of reflection.",
   resourceLabel:"YouTube: Properties of Light: Reflection", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Light%3A%20Reflection%20grade%204%20educational",
   quiz:[
     {q:"Light travels in ___.", options:["circles","zigzags","straight lines","curves"], answer:2},
     {q:"Reflection occurs when light ___.", options:["bounces off a surface","bends as it passes through","disappears into an object","is absorbed by a surface"], answer:0},
     {q:"Which surface reflects light best?", options:["A sponge","Dark wood","Black velvet","A mirror"], answer:3},
     {q:"The angle of incidence is ___.", options:["less than the angle of reflection","greater than the angle of reflection","equal to the angle of reflection","always 90 degrees"], answer:2},
     {q:"Why does a mirror show your reflection?", options:["It is transparent","It glows","It absorbs light","It reflects light at the same angle"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Trade and Commerce in History", summary:"Grade 4 Social Studies: trade is the exchange of goods and services. Ancient and early modern civilizations developed trade routes that spread culture and ideas.",
   resourceLabel:"YouTube: Trade and Commerce in History", resourceUrl:"https://www.youtube.com/results?search_query=Trade%20and%20Commerce%20in%20History%20grade%204%20educational",
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
   quiz:[
     {q:"Which spelling is correct?", options:["recieve","receive","receeve","receve"], answer:1},
     {q:"'I before E except after C' means in the word BELIEVE you write ___.", options:["i only","ei","ie","e only"], answer:2},
     {q:"Which is spelled correctly?", options:["freind","frend","friend","frennd"], answer:2},
     {q:"After the letter C, you usually write ___ (not ei).", options:["ie","only e","only i","ei"], answer:3},
     {q:"Which word follows the 'i before e except after c' rule?", options:["weird","believe","their","neither"], answer:1}
   ]},
  {subject:"Math", title:"Money: Making Change", summary:"Grade 4 Number strand: students calculate change by subtracting the price from the amount paid, using coins and bills up to $20.",
   resourceLabel:"YouTube: Money: Making Change", resourceUrl:"https://www.youtube.com/results?search_query=Money%3A%20Making%20Change%20grade%204%20educational",
   quiz:[
     {q:"An item costs $3.75. You pay $5.00. Your change is ___.", options:["$1.25","$1.75","$2.25","$1.00"], answer:0},
     {q:"An item costs $12.49. You pay $15.00. Your change is ___.", options:["$2.61","$2.41","$2.51","$3.51"], answer:2},
     {q:"To calculate change, you ___.", options:["subtract the price from the amount paid","divide the price","add price and amount paid","multiply the price"], answer:0},
     {q:"An item costs $7.89. You pay $10.00. Your change is ___.", options:["$2.21","$3.11","$2.11","$3.21"], answer:2},
     {q:"You have $20. You buy items for $14.37. Change = ?", options:["$5.37","$6.63","$5.63","$6.37"], answer:2}
   ]},
  {subject:"Science", title:"Properties of Light: Refraction", summary:"Grade 4 Science Energy strand: refraction is the bending of light as it passes from one medium to another (e.g., from air to water).",
   resourceLabel:"YouTube: Properties of Light: Refraction", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Light%3A%20Refraction%20grade%204%20educational",
   quiz:[
     {q:"Refraction is the ___ of light.", options:["speeding up","slowing down","bending","absorption"], answer:2},
     {q:"Refraction occurs when light passes from one ___ to another.", options:["source","medium (material)","direction","colour"], answer:1},
     {q:"A straw in a glass of water appears to be bent because of ___.", options:["absorption","refraction","reflection","diffusion"], answer:1},
     {q:"A prism separates white light into its colours because different colours ___ at different angles.", options:["refract","reflect","absorb","emit"], answer:0},
     {q:"A rainbow is an example of ___.", options:["only reflection","only absorption","light bending through water droplets","diffraction only"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Human Rights", summary:"Grade 4 Social Studies: human rights are basic rights all people deserve. The Universal Declaration of Human Rights (UDHR, 1948) protects these rights globally.",
   resourceLabel:"YouTube: Human Rights", resourceUrl:"https://www.youtube.com/results?search_query=Human%20Rights%20grade%204%20educational",
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
   quiz:[
     {q:"An adverb modifies a ___.", options:["preposition only","verb, adjective, or another adverb","noun only","pronoun only"], answer:1},
     {q:"Which word is an adverb in: She spoke softly?", options:["She","spoke","(no adverb)","softly"], answer:3},
     {q:"Adverbs of manner tell ___.", options:["how","when","to what degree","where"], answer:0},
     {q:"Adverbs of time tell ___.", options:["how","where","to what degree","when"], answer:3},
     {q:"Many adverbs end in ___.", options:["–ly","–er","–tion","–ing"], answer:0}
   ]},
  {subject:"Math", title:"Patterns: Numeric and Geometric", summary:"Grade 4 Algebra and Patterning strand: numeric patterns follow a mathematical rule; geometric patterns involve shapes. Students identify rules and extend patterns.",
   resourceLabel:"YouTube: Patterns: Numeric and Geometric", resourceUrl:"https://www.youtube.com/results?search_query=Patterns%3A%20Numeric%20and%20Geometric%20grade%204%20educational",
   quiz:[
     {q:"What is the rule? 3, 6, 9, 12...", options:["add 2","add 3","add 4","multiply by 2"], answer:1},
     {q:"What comes next? 1, 2, 4, 8, 16, ___", options:["24","18","20","32"], answer:3},
     {q:"A geometric pattern uses ___.", options:["only colours","only lines","numbers only","repeating or growing shapes"], answer:3},
     {q:"What is the rule? 100, 90, 80, 70...", options:["subtract 10","subtract 20","subtract 5","add 10"], answer:0},
     {q:"Which is an example of a geometric pattern?", options:["A,B,C,A,B,C","triangle, square, triangle, square","2,4,6,8","red, blue, green, red"], answer:1}
   ]},
  {subject:"Science", title:"Sound: Vibration and Frequency", summary:"Grade 4 Science Energy strand: sounds are made by vibrations. Frequency determines pitch — higher frequency = higher pitch. Amplitude determines volume.",
   resourceLabel:"YouTube: Sound: Vibration and Frequency", resourceUrl:"https://www.youtube.com/results?search_query=Sound%3A%20Vibration%20and%20Frequency%20grade%204%20educational",
   quiz:[
     {q:"Sound is caused by ___.", options:["magnetic fields","light waves","electrical signals","vibrations"], answer:3},
     {q:"Frequency refers to ___.", options:["how loud a sound is","how many vibrations per second","the speed of light","how far sound travels"], answer:1},
     {q:"A high-frequency sound has a ___ pitch.", options:["medium","high","no","low"], answer:1},
     {q:"Amplitude of a sound wave determines its ___.", options:["pitch","volume (loudness)","speed","frequency"], answer:1},
     {q:"In which medium does sound travel fastest?", options:["Air","Vacuum (space)","Solid materials (like steel)","Water"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canadian Geography: Provinces and Territories", summary:"Grade 4 Social Studies: Canada has 10 provinces and 3 territories. Each has a capital city and distinct geographic features.",
   resourceLabel:"YouTube: Canadian Geography: Provinces and Territories", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Geography%3A%20Provinces%20and%20Territories%20grade%204%20educational",
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
   quiz:[
     {q:"Context clues are ___.", options:["words nearby that hint at meaning","only antonyms","only synonyms","definitions found in the glossary"], answer:0},
     {q:"Which type of context clue gives a definition within the text?", options:["Restatement clue: 'X, which means...'","Inference clue","Synonym clue","Antonym clue"], answer:0},
     {q:"Using context clues helps readers ___.", options:["figure out meanings while reading","look up every word in a dictionary","memorize vocabulary lists","skip unknown words"], answer:0},
     {q:"In 'The magnanimous king gave generously to the poor,' magnanimous means ___.", options:["generous and kind","cruel","quiet","stingy"], answer:0},
     {q:"Which strategy helps most with a word you do not know?", options:["Skip to the next chapter","Read the surrounding sentences for clues","Ignore it","Ask someone immediately"], answer:1}
   ]},
  {subject:"Math", title:"Geometry: Angles", summary:"Grade 4 Geometry strand: an angle is formed by two rays with a common endpoint. A right angle = 90°, acute angle < 90°, obtuse angle > 90°.",
   resourceLabel:"YouTube: Geometry: Angles", resourceUrl:"https://www.youtube.com/results?search_query=Geometry%3A%20Angles%20grade%204%20educational",
   quiz:[
     {q:"A right angle measures exactly ___.", options:["180°","45°","60°","90°"], answer:3},
     {q:"An acute angle measures ___.", options:["180°","less than 90°","more than 90°","exactly 90°"], answer:1},
     {q:"An obtuse angle measures ___.", options:["more than 180°","between 90° and 180°","exactly 90°","less than 90°"], answer:1},
     {q:"A straight angle measures ___.", options:["270°","90°","45°","180°"], answer:3},
     {q:"Which tool measures angles?", options:["Scale","Protractor","Ruler","Compass"], answer:1}
   ]},
  {subject:"Science", title:"Pulleys and Gears", summary:"Grade 4 Science Energy strand: pulleys and gears are simple machines that redirect or change force. Gears can speed up or slow down motion and change direction.",
   resourceLabel:"YouTube: Pulleys and Gears", resourceUrl:"https://www.youtube.com/results?search_query=Pulleys%20and%20Gears%20grade%204%20educational",
   quiz:[
     {q:"A pulley is used to ___.", options:["generate electricity","increase temperature","lift or move loads by redirecting force","make objects glow"], answer:2},
     {q:"In a fixed pulley, the force needed to lift a load ___.", options:["halves","doubles","triples","stays the same (only direction changes)"], answer:3},
     {q:"A moveable pulley ___ the force needed.", options:["triples","keeps the same","doubles","reduces by about half"], answer:3},
     {q:"When two gears mesh, they rotate in ___ directions.", options:["opposite","no","the same","random"], answer:0},
     {q:"A larger gear turning a smaller gear makes the smaller gear rotate ___.", options:["faster","slower","at the same speed","backwards only"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Ontario Geography", summary:"Grade 4 Social Studies: Ontario is Canada's most populous province with diverse geography including the Great Lakes, Canadian Shield, and Great Lakes–St. Lawrence Lowlands.",
   resourceLabel:"YouTube: Ontario Geography", resourceUrl:"https://www.youtube.com/results?search_query=Ontario%20Geography%20grade%204%20educational",
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
   quiz:[
     {q:"Comparing means finding how things are ___.", options:["unrelated","different","bigger","the same or similar"], answer:3},
     {q:"Contrasting means finding how things are ___.", options:["different","similar","the same","related"], answer:0},
     {q:"Which signal word shows a contrast?", options:["However","Similarly","Also","Both"], answer:0},
     {q:"A Venn diagram helps ___.", options:["draw maps","add numbers","compare and contrast two or more things","write paragraphs"], answer:2},
     {q:"Which text type often uses comparison and contrast?", options:["A report about two animals","A personal diary","A recipe","A poem"], answer:0}
   ]},
  {subject:"Math", title:"Area and Perimeter", summary:"Grade 4 Measurement strand: perimeter is the distance around a shape; area is the space inside. Area of a rectangle = length × width; perimeter = 2(l + w).",
   resourceLabel:"YouTube: Area and Perimeter", resourceUrl:"https://www.youtube.com/results?search_query=Area%20and%20Perimeter%20grade%204%20educational",
   quiz:[
     {q:"Perimeter is the ___.", options:["space inside a shape","weight of a shape","distance around the outside of a shape","height of a shape"], answer:2},
     {q:"Area is measured in ___.", options:["linear units (cm)","grams","cubic units (cm³)","square units (cm²)"], answer:3},
     {q:"A rectangle is 5 cm long and 3 cm wide. Area = ?", options:["8 cm²","10 cm²","16 cm²","15 cm²"], answer:3},
     {q:"A rectangle is 6 cm long and 4 cm wide. Perimeter = ?", options:["10 cm","20 cm","24 cm","48 cm"], answer:1},
     {q:"Area of a square with side 7 cm = ?", options:["28 cm²","49 cm²","14 cm²","21 cm²"], answer:1}
   ]},
  {subject:"Science", title:"Electricity: Static and Current", summary:"Grade 4 Science Energy strand: static electricity is a build-up of charge; current electricity is a flow of electrons through a conductor.",
   resourceLabel:"YouTube: Electricity: Static and Current", resourceUrl:"https://www.youtube.com/results?search_query=Electricity%3A%20Static%20and%20Current%20grade%204%20educational",
   quiz:[
     {q:"Static electricity is caused by ___.", options:["burning fuel","magnetism","a build-up of electric charge","a flow of electrons in a circuit"], answer:2},
     {q:"Current electricity flows through ___.", options:["a vacuum","conductors in a circuit","insulators","non-metals only"], answer:1},
     {q:"Which is a good conductor of electricity?", options:["Rubber","Wood","Glass","Copper wire"], answer:3},
     {q:"An insulator ___.", options:["creates static electricity","blocks the flow of electricity","allows electricity to flow freely","has no electrical properties"], answer:1},
     {q:"Which is an example of static electricity?", options:["Turning on a light bulb","Charging a phone","A lightning bolt or a rubbed balloon","Using a toaster"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Maps: Physical Features", summary:"Grade 4 Social Studies: physical maps show natural features like mountains, rivers, lakes, and plains. They use colour and symbols to represent terrain.",
   resourceLabel:"YouTube: Maps: Physical Features", resourceUrl:"https://www.youtube.com/results?search_query=Maps%3A%20Physical%20Features%20grade%204%20educational",
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
   quiz:[
     {q:"A simile compares two things using ___.", options:["is/was","and/but","like or as","metaphor words"], answer:2},
     {q:"Which is a simile?", options:["The car is a beast.","Time flies.","She ran like the wind.","The moon smiled."], answer:2},
     {q:"What does 'brave as a lion' mean?", options:["A comparison without meaning","Lions are brave animals","The person is a lion","The person is extremely brave"], answer:3},
     {q:"Similes make writing more ___.", options:["boring","difficult","vivid and relatable","confusing"], answer:2},
     {q:"Which is NOT a simile?", options:["white as snow","cold as ice","The thunder roared","quiet as a mouse"], answer:2}
   ]},
  {subject:"Math", title:"Metric Measurement: Length", summary:"Grade 4 Measurement strand: the metric system uses kilometres (km), metres (m), centimetres (cm), and millimetres (mm). 1 m = 100 cm; 1 km = 1000 m.",
   resourceLabel:"YouTube: Metric Measurement: Length", resourceUrl:"https://www.youtube.com/results?search_query=Metric%20Measurement%3A%20Length%20grade%204%20educational",
   quiz:[
     {q:"1 metre = ___ centimetres.", options:["1","1000","10","100"], answer:3},
     {q:"1 kilometre = ___ metres.", options:["100","10000","10","1000"], answer:3},
     {q:"Which unit would you use to measure the length of a pencil?", options:["Metres","Kilometres","Grams","Centimetres"], answer:3},
     {q:"Which unit would you use to measure the distance between two cities?", options:["Metres","Centimetres","Millimetres","Kilometres"], answer:3},
     {q:"Convert 3 m to cm.", options:["3000 cm","300 cm","3 cm","30 cm"], answer:1}
   ]},
  {subject:"Science", title:"Electric Circuits", summary:"Grade 4 Science Energy strand: a complete circuit allows electricity to flow. It needs a power source, conductors, and a load (device). Circuits can be series or parallel.",
   resourceLabel:"YouTube: Electric Circuits", resourceUrl:"https://www.youtube.com/results?search_query=Electric%20Circuits%20grade%204%20educational",
   quiz:[
     {q:"For electricity to flow, a circuit must be ___.", options:["very long","broken","open","complete (closed)"], answer:3},
     {q:"Which is NOT needed in a basic circuit?", options:["A magnet","Power source (battery)","Load (light bulb)","Wire (conductor)"], answer:0},
     {q:"In a series circuit, components are connected ___.", options:["in a grid","in parallel paths","one after another in one loop","randomly"], answer:2},
     {q:"In a parallel circuit, each branch has ___.", options:["only one component","no power at all","the same current as all others","its own direct path to the power source"], answer:3},
     {q:"If a bulb in a series circuit burns out, the other bulbs ___.", options:["explode","keep working","also go out (circuit is broken)","get brighter"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canada's Natural Resources", summary:"Grade 4 Social Studies: Canada is rich in natural resources including forests, minerals, freshwater, oil, and agricultural land. These support the economy but must be managed sustainably.",
   resourceLabel:"YouTube: Canada's Natural Resources", resourceUrl:"https://www.youtube.com/results?search_query=Canada%27s%20Natural%20Resources%20grade%204%20educational",
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
   quiz:[
     {q:"A metaphor says one thing ___ another.", options:["is like/as","is similar to","is bigger than","IS directly"], answer:3},
     {q:"Which is a metaphor?", options:["He is as strong as an ox.","She ran like a cheetah.","The rain fell like tears.","The world is a stage."], answer:3},
     {q:"What does 'Time is money' mean?", options:["Clocks cost money","Time is free","Time is currency","Time is valuable, don't waste it"], answer:3},
     {q:"A metaphor differs from a simile because it ___.", options:["is only used in poetry","directly states one thing is another","makes no comparison","uses 'like' or 'as'"], answer:1},
     {q:"Which is a metaphor?", options:["Her voice was music to my ears.","quiet as a mouse","brave as a lion","He runs like a gazelle."], answer:0}
   ]},
  {subject:"Math", title:"Mass and Volume Measurement", summary:"Grade 4 Measurement strand: mass is measured in grams (g) and kilograms (kg). Volume is measured in litres (L) and millilitres (mL). 1 kg = 1000 g; 1 L = 1000 mL.",
   resourceLabel:"YouTube: Mass and Volume Measurement", resourceUrl:"https://www.youtube.com/results?search_query=Mass%20and%20Volume%20Measurement%20grade%204%20educational",
   quiz:[
     {q:"1 kilogram = ___ grams.", options:["100","10","1000","10000"], answer:2},
     {q:"1 litre = ___ millilitres.", options:["100","10","10000","1000"], answer:3},
     {q:"Which unit measures how heavy something is?", options:["Kilogram","Litre","Kilometre","Millilitre"], answer:0},
     {q:"Which unit measures the amount of liquid in a bottle?", options:["Centimetre","Kilometre","Millilitre/Litre","Kilogram"], answer:2},
     {q:"A bag weighs 2500 g. How many kilograms is that?", options:["0.25 kg","25 kg","250 kg","2.5 kg"], answer:3}
   ]},
  {subject:"Science", title:"Forces: Gravity and Friction", summary:"Grade 4 Science Energy strand: gravity is the force that pulls objects toward Earth. Friction is the force that resists movement between surfaces in contact.",
   resourceLabel:"YouTube: Forces: Gravity and Friction", resourceUrl:"https://www.youtube.com/results?search_query=Forces%3A%20Gravity%20and%20Friction%20grade%204%20educational",
   quiz:[
     {q:"Gravity is a force that ___.", options:["stops all motion","only exists in space","pulls objects toward each other","pushes objects upward"], answer:2},
     {q:"Friction is a force that ___.", options:["resists sliding motion between surfaces","speeds objects up","pulls objects down","pushes objects sideways"], answer:0},
     {q:"Which surface creates MORE friction?", options:["Rough sandpaper","A wet road","A polished marble floor","Ice"], answer:0},
     {q:"Friction produces ___.", options:["heat and slows objects down","more gravity","electrical charge","cold temperatures"], answer:0},
     {q:"Without gravity, objects on Earth would ___.", options:["get heavier","fall faster","stay in one place forever","float away into space"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Environment: Conservation", summary:"Grade 4 Social Studies: conservation means protecting and managing natural resources wisely to prevent their depletion and preserve environments for future generations.",
   resourceLabel:"YouTube: Environment: Conservation", resourceUrl:"https://www.youtube.com/results?search_query=Environment%3A%20Conservation%20grade%204%20educational",
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
   quiz:[
     {q:"Sequence means ___.", options:["a cause-and-effect relationship","the main idea","the order in which events occur","a comparison"], answer:2},
     {q:"Which signal word shows a sequence?", options:["In contrast","Next","However","Because"], answer:1},
     {q:"Why is sequence important in a how-to text?", options:["Only the first step matters","All steps can be done in any order","It is not","Steps must be in order"], answer:3},
     {q:"Which goes last in a story's sequence?", options:["The beginning","The problem","The introduction","The resolution/ending"], answer:3},
     {q:"'First mix the batter, then bake it' shows ___.", options:["contrast","sequence","cause and effect","comparison"], answer:1}
   ]},
  {subject:"Math", title:"Data: Bar Graphs", summary:"Grade 4 Data strand: a bar graph uses horizontal or vertical bars to compare quantities across categories. Students read, create, and interpret bar graphs.",
   resourceLabel:"YouTube: Data: Bar Graphs", resourceUrl:"https://www.youtube.com/results?search_query=Data%3A%20Bar%20Graphs%20grade%204%20educational",
   quiz:[
     {q:"A bar graph is used to ___.", options:["measure angles","show sequence","compare quantities across categories","calculate perimeter"], answer:2},
     {q:"The vertical axis of a bar graph usually shows ___.", options:["frequency or quantity","colours","categories","dates"], answer:0},
     {q:"If the 'Dogs' bar reaches 12 and 'Cats' bar reaches 8, there are ___ more dogs.", options:["5","4","3","2"], answer:1},
     {q:"What is the title of a graph used for?", options:["Decoration","To tell what data the graph shows","To label the axes","To list all data"], answer:1},
     {q:"A bar graph differs from a pictograph because ___.", options:["only bar graphs have titles","pictographs are always better","bar graphs use bars instead of pictures/symbols","bar graphs are less accurate"], answer:2}
   ]},
  {subject:"Science", title:"Properties of Liquids and Solids", summary:"Grade 4 Science Materials strand: solids have definite shape and volume; liquids have definite volume but take the shape of their container.",
   resourceLabel:"YouTube: Properties of Liquids and Solids", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Liquids%20and%20Solids%20grade%204%20educational",
   quiz:[
     {q:"A solid has ___.", options:["no definite shape or volume","only colour","definite shape and definite volume","definite volume but no definite shape"], answer:2},
     {q:"A liquid has ___.", options:["definite shape and volume","definite volume, shape of its container","no mass","no volume"], answer:1},
     {q:"Which is a solid at room temperature?", options:["Air","Water","Wood","Mercury"], answer:2},
     {q:"The property of viscosity describes ___.", options:["the colour of a liquid","how thick a liquid is","how hot a liquid is","how heavy a liquid is"], answer:1},
     {q:"Which liquid has higher viscosity (is thicker)?", options:["Honey","Vinegar","Air","Water"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Canadian Culture and Arts", summary:"Grade 4 Social Studies: Canadian culture reflects Indigenous traditions and the contributions of people from many nations, expressed through music, art, literature, and celebrations.",
   resourceLabel:"YouTube: Canadian Culture and Arts", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Culture%20and%20Arts%20grade%204%20educational",
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
   quiz:[
     {q:"If an event is 'impossible,' the probability is ___.", options:["close to 1","0","1","close to 0"], answer:1},
     {q:"If an event is 'certain,' the probability is ___.", options:["close to 1","1","close to 0","0"], answer:1},
     {q:"A bag has 4 red and 1 blue marble. Picking red is ___.", options:["likely","unlikely","impossible","certain"], answer:0},
     {q:"Which outcome is 'impossible' when rolling a 6-sided die?", options:["Rolling a 1","Rolling a 7","Rolling a 3","Rolling a 6"], answer:1},
     {q:"Probability can be expressed as a fraction. If 3 of 10 marbles are yellow, P(yellow) = ?", options:["1/3","3/10","7/10","10/3"], answer:1}
   ]},
  {subject:"Science", title:"Physical and Chemical Changes", summary:"Grade 4 Science Materials strand: a physical change alters the form but not the substance (e.g., cutting). A chemical change produces a new substance (e.g., burning).",
   resourceLabel:"YouTube: Physical and Chemical Changes", resourceUrl:"https://www.youtube.com/results?search_query=Physical%20and%20Chemical%20Changes%20grade%204%20educational",
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
];

export default curriculum;