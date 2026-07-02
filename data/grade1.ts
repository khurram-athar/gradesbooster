import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"Language", title:"Short Vowel Sounds", summary:"Ontario Grade 1 Reading strand: students blend short vowel sounds in CVC words such as cat, bed, pig, hop, sun.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which word has the short A sound?", options:["Cake","Cat","Cape","Cane"], answer:1},
     {q:"Which word has the short E sound?", options:["Bead","Beat","Bed","Bean"], answer:2},
     {q:"Which word has the short I sound?", options:["Kite","Bike","Fine","Pig"], answer:3},
     {q:"Which word has the short O sound?", options:["Coat","Note","Hop","Hope"], answer:2},
     {q:"Which word has the short U sound?", options:["Cube","Mule","Fun","Tune"], answer:2}
   ]},
  {subject:"Math", title:"Counting to 20", summary:"Ontario Grade 1 Number strand: students count forward and backward by 1s within 20 and represent quantities using objects and numerals.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"What number comes after 15?", options:["14","16","17","13"], answer:1},
     {q:"What number is one less than 10?", options:["9","11","8","12"], answer:0},
     {q:"Count: 17, 18, 19, ___", options:["20","21","22","18"], answer:0},
     {q:"Which number is between 12 and 14?", options:["11","15","13","10"], answer:2},
     {q:"How many fingers on two hands?", options:["8","9","10","11"], answer:2}
   ]},
  {subject:"Science", title:"Living and Non-living Things", summary:"Ontario Grade 1 Life Systems strand: living things grow, reproduce, and respond to their environment; non-living things do not.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Which of these is a living thing?", options:["Rock","Chair","Tree","Table"], answer:2},
     {q:"Which is NOT a living thing?", options:["Bird","Flower","Dog","Brick"], answer:3},
     {q:"Living things need food and ___.", options:["Electricity","Television","Water","Money"], answer:2},
     {q:"Which is a sign that something is alive?", options:["It is heavy","It grows and changes","It is hard","It is coloured"], answer:1},
     {q:"A plant is a living thing because it ___.", options:["Is made of wood","Grows and makes seeds","Is green","Cannot move"], answer:1}
   ]},
  {subject:"SocialStudies", title:"My Family", summary:"Ontario Grade 1 Social Studies Heritage and Identity strand: students describe their family and recognize that families differ in structure and traditions.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"A family is a group of people who ___.", options:["Work at the same job","Live on the same street","Care for each other","All look the same"], answer:2},
     {q:"Which of these is a family member?", options:["Teacher","Parent","Neighbour","Friend"], answer:1},
     {q:"Families can be ___.", options:["Only large","Only small","Many different sizes","Always the same"], answer:2},
     {q:"What do most families do together?", options:["Ignore each other","Share meals and celebrate","Work the same job","Go to the same school"], answer:1},
     {q:"Every family is ___.", options:["Exactly the same","Unique and special","Always big","Always small"], answer:1}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"Language", title:"Long Vowel Sounds", summary:"Ontario Grade 1 Reading strand: long vowels say their name, as in cake, bee, kite, boat, cube. The silent E rule often signals a long vowel.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which word has a long A sound?", options:["Cat","Cab","Cake","Cap"], answer:2},
     {q:"Which word has a long E sound?", options:["Bed","Bed","Bee","Bet"], answer:2},
     {q:"Which word has a long O sound?", options:["Hop","Hot","Hog","Hope"], answer:3},
     {q:"What makes the vowel long in the word KITE?", options:["Two vowels together","Silent E at the end","Consonant blend","Capital letter"], answer:1},
     {q:"Which word has a long U sound?", options:["Cup","Cut","Cub","Cube"], answer:3}
   ]},
  {subject:"Math", title:"Numbers to 50", summary:"Ontario Grade 1 Number strand: students count, read, write, and represent whole numbers to 50, and describe their positions on a number line.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"What number comes after 39?", options:["38","40","41","37"], answer:1},
     {q:"Which is greater: 27 or 32?", options:["27","32","Equal","Cannot tell"], answer:1},
     {q:"What is 10 more than 24?", options:["14","25","34","44"], answer:2},
     {q:"Which number is between 15 and 20?", options:["14","21","17","25"], answer:2},
     {q:"Count by 1s: 45, 46, 47, ___", options:["48","49","44","50"], answer:0}
   ]},
  {subject:"Science", title:"Seasonal Changes: Fall", summary:"Ontario Grade 1 Earth and Space Systems strand: in fall, days shorten, leaves change colour and drop, and animals prepare for winter.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"In fall, leaves on deciduous trees ___.", options:["Stay green","Turn colour and fall off","Grow bigger","Turn white"], answer:1},
     {q:"Fall days are ___ than summer days.", options:["Longer","The same length","Shorter","Hotter"], answer:2},
     {q:"Which month is typically fall in Ontario?", options:["July","October","March","May"], answer:1},
     {q:"What do many animals do to prepare for winter?", options:["Grow wings","Go swimming","Gather food or migrate","Turn red"], answer:2},
     {q:"Fall comes after which season?", options:["Spring","Winter","Summer","Rainy season"], answer:2}
   ]},
  {subject:"SocialStudies", title:"My School Community", summary:"Ontario Grade 1 Social Studies strand: students identify school community members and their roles, and describe how everyone contributes.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Who is usually the leader of a whole school?", options:["A student","The principal","A teacher","A librarian"], answer:1},
     {q:"What is a teacher's main job?", options:["Cook lunch","Help students learn","Fix the building","Drive the bus"], answer:1},
     {q:"How can students help their school community?", options:["Being noisy","Picking up litter and helping others","Staying home","Ignoring rules"], answer:1},
     {q:"What does a librarian do?", options:["Fix computers","Cook lunch","Help students find books","Drive buses"], answer:2},
     {q:"Why do schools have rules?", options:["To be unfair","To keep everyone safe and learning","To punish students","Just because adults say so"], answer:1}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"Language", title:"Consonant Blends: bl, cl, fl, pl", summary:"Ontario Grade 1 Reading strand: consonant blends are two or more consonants together where each sound is heard, such as bl in black and cl in clap.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which word starts with the BL blend?", options:["Clock","Floor","Black","Play"], answer:2},
     {q:"Which word starts with the CL blend?", options:["Blue","Clap","Floor","Plane"], answer:1},
     {q:"Which word starts with the FL blend?", options:["Play","Clock","Blue","Flag"], answer:3},
     {q:"Which word starts with the PL blend?", options:["Black","Floor","Plant","Clock"], answer:2},
     {q:"A consonant blend means ___.", options:["A single letter","Two consonants you hear separately","Only vowels","Silent letters"], answer:1}
   ]},
  {subject:"Math", title:"Addition to 10", summary:"Ontario Grade 1 Number strand: students add two one-digit numbers with sums to 10 using objects, drawings, and number lines.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"3 + 4 = ?", options:["6","7","8","5"], answer:1},
     {q:"5 + 5 = ?", options:["9","10","11","8"], answer:1},
     {q:"2 + 6 = ?", options:["7","8","9","6"], answer:1},
     {q:"1 + 9 = ?", options:["9","10","11","8"], answer:1},
     {q:"4 + 3 = ?", options:["6","7","8","5"], answer:1}
   ]},
  {subject:"Science", title:"Materials: Solid, Liquid, Gas", summary:"Ontario Grade 1 Matter and Materials strand: students identify the three states of matter by exploring everyday examples of solids, liquids, and gases.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Which state of matter has a definite shape?", options:["Liquid","Gas","Solid","Steam"], answer:2},
     {q:"Water is an example of a ___.", options:["Solid","Liquid","Gas","Rock"], answer:1},
     {q:"Which state of matter fills its entire container?", options:["Solid","Liquid","Gas","Ice"], answer:2},
     {q:"Ice is water in a ___ state.", options:["Liquid","Gas","Solid","Hot"], answer:2},
     {q:"Steam is water in a ___ state.", options:["Solid","Liquid","Gas","Cold"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Maps and Directions", summary:"Ontario Grade 1 Social Studies strand B: students use directional language and simple maps to describe locations in familiar places.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"A map is a ___.", options:["Photo from space","Drawing of a real place from above","Painting of nature","Written story"], answer:1},
     {q:"If you face north, south is ___.", options:["Behind you","To your left","To your right","Above you"], answer:0},
     {q:"Which direction does the sun rise?", options:["West","North","East","South"], answer:2},
     {q:"On most maps, north is at the ___.", options:["Bottom","Left","Top","Right"], answer:2},
     {q:"What do we call a map of the whole world?", options:["A globe or world map","A street map","A treasure map","A floor plan"], answer:0}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"Language", title:"Sight Words", summary:"Ontario Grade 1 Reading strand: students recognize high-frequency Dolch sight words automatically, supporting reading fluency. Examples: the, and, a, to, said, is, you, in, was.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which of these is a common sight word?", options:["Elephant","the","xylophone","umbrella"], answer:1},
     {q:"Why do we practise sight words?", options:["They are long words","We see them very often in reading","They are nouns only","They are hard to spell"], answer:1},
     {q:"Which is spelled correctly?", options:["Teh","Thuh","The","Tha"], answer:2},
     {q:"Sight words help us ___.", options:["Spell big words","Read more quickly and fluently","Learn maths","Do science"], answer:1},
     {q:"Which is NOT a typical sight word?", options:["and","the","is","rhinoceros"], answer:3}
   ]},
  {subject:"Math", title:"Subtraction from 10", summary:"Ontario Grade 1 Number strand: students subtract one-digit numbers from numbers up to 10 using objects, drawings, and number lines.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"10 - 3 = ?", options:["6","7","8","5"], answer:1},
     {q:"8 - 4 = ?", options:["3","4","5","6"], answer:1},
     {q:"7 - 2 = ?", options:["4","5","6","3"], answer:1},
     {q:"9 - 5 = ?", options:["3","4","5","6"], answer:1},
     {q:"6 - 6 = ?", options:["0","1","2","3"], answer:0}
   ]},
  {subject:"Science", title:"Needs of Living Things", summary:"Ontario Grade 1 Life Systems strand: all living things need air, water, food, and shelter. Plants also need sunlight to make food through photosynthesis.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Which is NOT a basic need of living things?", options:["Water","Food","Television","Air"], answer:2},
     {q:"Plants use sunlight to make their own ___.", options:["Soil","Food","Water","Shelter"], answer:1},
     {q:"Animals need shelter to ___.", options:["Go to school","Be protected from weather and predators","Play sports","Find water"], answer:1},
     {q:"What do living things need to breathe?", options:["Water","Air","Food","Sunlight"], answer:1},
     {q:"Which is a basic need ALL living things share?", options:["Transportation","Water","Money","Television"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Community Workers", summary:"Ontario Grade 1 Social Studies strand B: students identify community workers and explain how their work benefits everyone in the community.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Who builds houses and buildings?", options:["A teacher","A construction worker","A doctor","A chef"], answer:1},
     {q:"What does a bus driver do?", options:["Teach students","Carry passengers from place to place","Fix roads","Cook food"], answer:1},
     {q:"Where does a chef work?", options:["A school","A hospital","A kitchen or restaurant","A store"], answer:2},
     {q:"Why do communities need workers with many different jobs?", options:["They do not","Different jobs meet different community needs","Only doctors are needed","Only teachers are needed"], answer:1},
     {q:"Who repairs broken water pipes?", options:["A teacher","A pilot","A plumber","A baker"], answer:2}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"Language", title:"Word Families: -at and -an", summary:"Ontario Grade 1 Reading strand: word families share the same rime (ending pattern). The -at family includes cat, bat, hat, sat; the -an family includes can, man, ran, tan.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which word belongs to the -AT family?", options:["Can","Run","Hat","Men"], answer:2},
     {q:"Which word belongs to the -AN family?", options:["Cat","Bat","Hat","Can"], answer:3},
     {q:"How many words are in the -AT family: cat, bat, hat, sat?", options:["2","3","4","5"], answer:2},
     {q:"Which word rhymes with CAN?", options:["Cat","Hat","Ran","Bit"], answer:2},
     {q:"Word families help us ___.", options:["Count numbers","Recognize spelling patterns and read new words","Draw pictures","Do experiments"], answer:1}
   ]},
  {subject:"Math", title:"Place Value: Tens and Ones", summary:"Ontario Grade 1 Number strand: students decompose two-digit numbers into tens and ones using base-ten blocks, understanding that the position of a digit determines its value.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"In the number 23, the digit 2 means ___.", options:["2 ones","20 tens","2 tens","20 ones"], answer:2},
     {q:"How many tens are in 35?", options:["3","5","35","2"], answer:0},
     {q:"How many ones are in 47?", options:["4","7","47","11"], answer:1},
     {q:"What is 3 tens and 4 ones?", options:["43","34","30","4"], answer:1},
     {q:"In the number 16, the 6 means ___.", options:["6 tens","6 ones","16 ones","1 ten"], answer:1}
   ]},
  {subject:"Science", title:"Seasonal Changes: Winter", summary:"Ontario Grade 1 Earth and Space Systems strand: in winter, temperatures drop, many trees are bare, some animals hibernate, and people wear warm clothing.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What season comes after fall?", options:["Spring","Summer","Winter","Rainy season"], answer:2},
     {q:"In winter, many deciduous trees ___.", options:["Grow new leaves","Have bare branches","Grow taller","Turn green"], answer:1},
     {q:"What do bears do in winter?", options:["Fly south","Swim in rivers","Hibernate","Grow bigger"], answer:2},
     {q:"In Ontario, winter weather is usually ___.", options:["Hot and dry","Warm and rainy","Cold with snow and ice","Always sunny"], answer:2},
     {q:"Days in winter are ___ than in summer.", options:["Longer","The same","Shorter","Always sunny"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Rules and Responsibilities", summary:"Ontario Grade 1 Social Studies strand A: students describe their rights and responsibilities at home, at school, and in the community.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Why do schools have rules?", options:["To be unfair","To keep everyone safe and learning","To punish students","Rules are not needed"], answer:1},
     {q:"A responsibility is something you ___.", options:["Are allowed to ignore","Must do for yourself or others","Can always skip","Only adults do"], answer:1},
     {q:"Which is a student responsibility at school?", options:["Talking over the teacher","Completing work and respecting others","Playing all day","Ignoring homework"], answer:1},
     {q:"Rights and responsibilities work together because ___.", options:["They are the same thing","Rights give us freedom; responsibilities ensure we respect others","Only rights matter","Only responsibilities matter"], answer:1},
     {q:"Which is an example of a right?", options:["Working all day","Being treated fairly and kept safe","Having no rules","Ignoring others"], answer:1}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"Language", title:"Writing Complete Sentences", summary:"Ontario Grade 1 Writing strand: a complete sentence has a subject and a verb, begins with a capital letter, and ends with a punctuation mark.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Every sentence must start with a ___.", options:["lowercase letter","Period","Capital letter","Number"], answer:2},
     {q:"Which is a complete sentence?", options:["the dog","Runs fast.","The dog runs fast.","Fast dog."], answer:2},
     {q:"A sentence that asks a question ends with a ___.", options:["Period","Exclamation mark","Question mark","Comma"], answer:2},
     {q:"Which sentence has correct punctuation?", options:["the cat is big","The cat is big.","the cat is big.","The cat is big"], answer:1},
     {q:"A sentence needs a subject (who) and a ___ (action).", options:[], answer:0}
   ]},
  {subject:"Math", title:"Skip Counting by 2s", summary:"Ontario Grade 1 Number strand: students skip count by 2s from 0, landing on even numbers: 0, 2, 4, 6, 8, 10...",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Skip count by 2s: 2, 4, 6, ___", options:["5","7","8","9"], answer:2},
     {q:"Skip count by 2s: 10, 12, 14, ___", options:["15","16","17","13"], answer:1},
     {q:"Which numbers do you land on when skip counting by 2s?", options:["Odd numbers","Even numbers","All numbers","Random numbers"], answer:1},
     {q:"Skip count by 2s from 0: 0, 2, 4, 6, 8, ___", options:["9","10","11","12"], answer:1},
     {q:"Skip counting by 2s helps us count ___ faster.", options:["Odd numbers","By tens","Pairs or groups of 2","By fives"], answer:2}
   ]},
  {subject:"Science", title:"Animals and Their Young", summary:"Ontario Grade 1 Life Systems strand: animals reproduce and care for their young; baby animals resemble their parents and grow to look like them.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"A baby dog is called a ___.", options:["Kitten","Calf","Puppy","Foal"], answer:2},
     {q:"A baby cat is called a ___.", options:["Puppy","Kitten","Cub","Lamb"], answer:1},
     {q:"Baby animals grow up to look like their ___.", options:["Owners","Parents","Teachers","Friends"], answer:1},
     {q:"Why do parent animals care for their young?", options:["For fun","To keep them safe until they can survive","They do not care","Because they are paid"], answer:1},
     {q:"Which baby animal hatches from an egg?", options:["Puppy","Kitten","Duckling","Lamb"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Our Province: Ontario", summary:"Ontario Grade 1 Social Studies strand B: students identify Ontario on a map of Canada, name its capital city, and describe some key features.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What is the capital city of Ontario?", options:["Ottawa","Toronto","Vancouver","Montreal"], answer:1},
     {q:"Ontario is located in ___.", options:["Far west Canada","Far north","East-central Canada","The far east"], answer:2},
     {q:"What large bodies of water border southern Ontario?", options:["The Atlantic Ocean","The Pacific Ocean","The Great Lakes","The Arctic Ocean"], answer:2},
     {q:"Ontario's provincial flower is the ___.", options:["Rose","Trillium","Tulip","Sunflower"], answer:1},
     {q:"Which city is the largest in Ontario?", options:["Ottawa","Hamilton","Toronto","London"], answer:2}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"Language", title:"Question Words: Who, What, Where, When, Why", summary:"Ontario Grade 1 Reading and Writing strands: students identify and use the five W question words to gather information from texts and to formulate questions.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which question word asks about a person?", options:["What","Where","Who","When"], answer:2},
     {q:"Which question word asks about a place?", options:["Who","What","When","Where"], answer:3},
     {q:"Which question word asks about a time?", options:["Who","Where","When","Why"], answer:2},
     {q:"Which question word asks for a reason?", options:["What","Where","Who","Why"], answer:3},
     {q:"What question word asks about an object or event?", options:["Who","What","Where","When"], answer:1}
   ]},
  {subject:"Math", title:"Skip Counting by 5s", summary:"Ontario Grade 1 Number strand: students skip count by 5s from 0, recognising the pattern: 0, 5, 10, 15, 20...",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Skip count by 5s: 5, 10, 15, ___", options:["18","20","19","17"], answer:1},
     {q:"Skip count by 5s: 20, 25, 30, ___", options:["32","35","33","38"], answer:1},
     {q:"How many 5s make 25?", options:["3","4","5","6"], answer:2},
     {q:"Skip counting by 5s is like counting ___.", options:["By ones","By twos","By fives","By tens"], answer:2},
     {q:"5, 10, 15, 20 — what comes next?", options:["21","22","25","30"], answer:2}
   ]},
  {subject:"Science", title:"Parts of a Plant", summary:"Ontario Grade 1 Life Systems strand: students identify and describe the functions of the main parts of a plant: roots, stem, leaves, and flower.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Which part of a plant is usually underground?", options:["Leaves","Flower","Stem","Roots"], answer:3},
     {q:"What do roots do?", options:["Make food from sunlight","Attract bees","Anchor the plant and absorb water","Make flowers"], answer:2},
     {q:"Which part carries water from the roots upward?", options:["Leaf","Flower","Stem","Seed"], answer:2},
     {q:"Leaves make food for the plant using ___.", options:["Rain and soil only","Sunlight, water, and air","Roots and flowers","Heat and wind"], answer:1},
     {q:"What does the flower help the plant make?", options:["More leaves","Seeds","Bigger roots","Stems"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Canadian Symbols", summary:"Ontario Grade 1 Social Studies strand B: students identify major Canadian symbols including the maple leaf, beaver, flag, and national anthem.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What animal is a symbol of Canada?", options:["Eagle","Beaver","Bear","Moose"], answer:1},
     {q:"What is the main symbol on the Canadian flag?", options:["A star","A bear","A maple leaf","A sun"], answer:2},
     {q:"What are the two official colours of the Canadian flag?", options:["Blue and white","Red and white","Green and gold","Red and blue"], answer:1},
     {q:"What is Canada's national anthem?", options:["God Save the King","O Canada","The Maple Leaf Forever","True North"], answer:1},
     {q:"The maple leaf represents ___.", options:["The United States","The beaver","Canada","The queen"], answer:2}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"Language", title:"Punctuation: Period, Question Mark, Exclamation Mark", summary:"Ontario Grade 1 Writing strand: students use end punctuation correctly — period for statements, question mark for questions, and exclamation mark for strong emotion.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which punctuation ends a statement?", options:["?","!",".","..."], answer:2},
     {q:"Which punctuation ends a question?", options:[".",",","?","!"], answer:2},
     {q:"Which punctuation shows excitement or strong feeling?", options:[".",",","?","!"], answer:3},
     {q:"The cat is big ___.", options:["?","!",".","..."], answer:2},
     {q:"Is the cat big ___?", options:[".",",","?","!"], answer:2}
   ]},
  {subject:"Math", title:"Skip Counting by 10s", summary:"Ontario Grade 1 Number strand: students skip count by 10s from 0, recognising the pattern: 0, 10, 20, 30, 40, 50.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Skip count by 10s: 10, 20, 30, ___", options:["35","40","45","50"], answer:1},
     {q:"Skip count by 10s: 50, 60, 70, ___", options:["75","80","85","90"], answer:1},
     {q:"How many 10s make 40?", options:["2","3","4","5"], answer:2},
     {q:"10, 20, 30, 40 — what comes next?", options:["41","42","50","60"], answer:2},
     {q:"Skip counting by 10s is the same as counting ___.", options:["by ones","by fives","groups of 10","groups of 2"], answer:2}
   ]},
  {subject:"Science", title:"Seeds and How Plants Grow", summary:"Ontario Grade 1 Life Systems strand: students investigate how seeds germinate and grow into plants when given water, warmth, air, and light.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What do seeds need to germinate (sprout)?", options:["Ice and darkness","Water, warmth, and air","Only sunlight","Only soil"], answer:1},
     {q:"What is germination?", options:["When a plant dies","When a seed starts to grow into a plant","When leaves fall off","When flowers bloom"], answer:1},
     {q:"Where do seeds come from?", options:["Rocks","Flowers and fruit of plants","The sky","Water"], answer:1},
     {q:"As a seed grows it first produces a ___.", options:["Flower","Fruit","Tiny shoot and root","Large tree"], answer:2},
     {q:"Which is the correct order: seed, ___, plant?", options:["Leaf","Root only","Seedling","Flower"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Indigenous Peoples of Canada", summary:"Ontario Grade 1 Social Studies strand A: students learn that Indigenous peoples were the first peoples of Canada and have rich cultures, languages, and traditions.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Who were the first peoples of Canada?", options:["European settlers","Indigenous peoples","American visitors","Recent immigrants"], answer:1},
     {q:"Indigenous peoples have lived in Canada for ___.", options:["A few years","About 200 years","Thousands of years","50 years"], answer:2},
     {q:"Indigenous peoples have their own ___.", options:["Nothing special","Languages and traditions","European customs only","Modern technology only"], answer:1},
     {q:"We should respect Indigenous cultures because ___.", options:["They are far away","They are part of Canada's history and identity","It does not matter","They are strangers"], answer:1},
     {q:"What do we call the different groups of First Nations peoples?", options:["All the same group","Nations, each with their own culture","European groups","American groups"], answer:1}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"Language", title:"Retelling a Story", summary:"Ontario Grade 1 Reading strand: students retell stories in sequence using the language of beginning, middle, and end, and story elements: characters, setting, problem, solution.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"The beginning of a story tells us ___.", options:["How it ends","Who the characters are and the setting","The solution","A lesson only"], answer:1},
     {q:"The middle of a story contains the ___.", options:["Happy ending","Problem or challenge","Introduction of characters only","Title"], answer:1},
     {q:"The end of a story shows the ___.", options:["New characters","Beginning again","Solution to the problem","First event"], answer:2},
     {q:"Characters are ___.", options:["The place where the story happens","The people or animals in the story","The problem only","The ending"], answer:1},
     {q:"Setting means ___.", options:["The character's name","Where and when the story takes place","The problem","The solution"], answer:1}
   ]},
  {subject:"Math", title:"2D Shapes", summary:"Ontario Grade 1 Geometry strand: students identify and describe properties of 2D shapes: circle, square, rectangle, and triangle.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"How many sides does a triangle have?", options:["2","3","4","5"], answer:1},
     {q:"How many corners does a square have?", options:["3","4","5","6"], answer:1},
     {q:"Which 2D shape has no corners?", options:["Triangle","Square","Circle","Rectangle"], answer:2},
     {q:"How many sides does a rectangle have?", options:["3","4","5","6"], answer:1},
     {q:"Which shape has four equal sides?", options:["Rectangle","Triangle","Circle","Square"], answer:3}
   ]},
  {subject:"Science", title:"Pushes and Pulls", summary:"Ontario Grade 1 Science Physical Education strand: a force is a push or pull that can move, stop, or change the direction of an object.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"A push moves an object ___.", options:["Toward you","Away from you","Up only","Down only"], answer:1},
     {q:"A pull moves an object ___.", options:["Away from you","Toward you","To the side only","Upward"], answer:1},
     {q:"Which is an example of a push?", options:["Opening a drawer","Reeling in a fish","Kicking a ball","Pulling a cart"], answer:2},
     {q:"Forces can change the ___ of a moving object.", options:["Colour","Speed or direction","Smell","Temperature"], answer:1},
     {q:"Which is an example of a pull?", options:["Kicking a ball","Pushing a door open","Opening a drawer","Throwing a ball"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Families Around the World", summary:"Ontario Grade 1 Social Studies strand A: students learn that families around the world share common needs but meet them in different ways through their cultures.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Families around the world all need ___.", options:["The same food","The same clothing","Food, shelter, and love","Electricity"], answer:2},
     {q:"Different families may speak ___.", options:["Only English","Only French","Many different languages","The same language always"], answer:2},
     {q:"Learning about other cultures helps us ___.", options:["Ignore differences","Understand and respect each other","Copy everyone","Stay separate"], answer:1},
     {q:"All families celebrate ___.", options:["The same holidays","Nothing","Important events in their own way","Only Christmas"], answer:2},
     {q:"What do all families around the world have in common?", options:["They look the same","Members care for each other","They live the same way","They all have the same rules"], answer:1}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"Language", title:"Main Idea", summary:"Ontario Grade 1 Reading strand: the main idea is what a text is mostly about. Supporting details give more information about the main idea.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"The main idea of a text is ___.", options:["A small detail","What the text is mostly about","The last sentence","A character's name"], answer:1},
     {q:"Supporting details ___.", options:["Are the most important idea","Explain the main idea with examples","Are not connected to the main idea","Are always at the beginning"], answer:1},
     {q:"A good title for a text about dogs would be ___.", options:["Cats are Great","All About Dogs","My Birthday","The Red Ball"], answer:1},
     {q:"How do you find the main idea?", options:["Read only the last sentence","Ask yourself what the text is mostly about","Count the words","Look at the pictures only"], answer:1},
     {q:"Which sentence is a main idea?", options:["The dog has brown spots.","Dogs make wonderful pets for many reasons.","The dog ran fast.","My dog is named Rex."], answer:1}
   ]},
  {subject:"Math", title:"3D Shapes", summary:"Ontario Grade 1 Geometry strand: students identify and describe 3D figures: sphere, cube, cylinder, and cone, relating them to everyday objects.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Which 3D shape looks like a ball?", options:["Cube","Cylinder","Sphere","Cone"], answer:2},
     {q:"Which 3D shape looks like a box?", options:["Sphere","Cylinder","Cone","Cube"], answer:3},
     {q:"Which 3D shape looks like a soup can?", options:["Sphere","Cylinder","Cube","Cone"], answer:1},
     {q:"A cone has ___ flat face(s).", options:["0","1","2","3"], answer:1},
     {q:"A cube has how many faces?", options:["4","5","6","8"], answer:2}
   ]},
  {subject:"Science", title:"Sound and Hearing", summary:"Ontario Grade 1 Science strand: sounds are made by vibrations. The ear detects sound waves, and sounds can be loud or soft, high-pitched or low-pitched.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Sounds are made by ___.", options:["Light","Vibrations","Heat","Gravity"], answer:1},
     {q:"Which body part do we use to hear?", options:["Eyes","Nose","Ears","Hands"], answer:2},
     {q:"A loud sound has ___ vibrations than a soft sound.", options:["Fewer","Smaller","Larger or stronger","Slower"], answer:2},
     {q:"Which makes a high-pitched sound?", options:["A bass drum","A tuba","A whistle","A cow"], answer:2},
     {q:"Covering your ears reduces sound because ___.", options:["Sound stops completely","Less sound reaches your eardrums","Your hearing improves","Vibrations increase"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Being a Good Citizen", summary:"Ontario Grade 1 Social Studies strand A: students describe what it means to be a responsible and caring member of their school and community.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"A good citizen ___.", options:["Takes others' things","Helps others and follows rules","Is always noisy","Litters"], answer:1},
     {q:"What does it mean to be responsible?", options:["Doing whatever you want","Taking care of your duties","Being unkind","Ignoring others"], answer:1},
     {q:"Why is it important to be kind to others?", options:["It is not important","It makes the community happy and safe","It is only for adults","Only teachers need to be kind"], answer:1},
     {q:"Being a good citizen at school means ___.", options:["Talking during lessons","Sharing, listening, and helping others","Pushing in line","Breaking rules"], answer:1},
     {q:"Good citizens follow rules because ___.", options:["Rules are boring","Rules keep everyone safe and happy","Only some people follow rules","Teachers created them"], answer:1}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"Language", title:"Characters and Setting", summary:"Ontario Grade 1 Reading strand: characters are the people or animals in a story; setting is where and when the story takes place.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Characters are ___.", options:["The place of the story","The people or animals in the story","The ending","The problem"], answer:1},
     {q:"Setting means ___.", options:["What happens in the story","Who is in the story","Where and when the story takes place","The solution"], answer:2},
     {q:"Which question helps identify the setting?", options:["Who is in the story?","What is the problem?","Where and when does the story happen?","How does it end?"], answer:2},
     {q:"A character's traits describe ___.", options:["Where the story happens","What the character is like (brave, funny, etc.)","The problem","The solution"], answer:1},
     {q:"Can a story have more than one character?", options:["No, only one character","Yes, stories can have many characters","Only in long stories","Only in fairy tales"], answer:1}
   ]},
  {subject:"Math", title:"Measuring Length", summary:"Ontario Grade 1 Measurement strand: students measure length using non-standard units (paperclips, cubes) and compare objects using longer, shorter, taller.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Which unit is NOT a standard unit of measurement?", options:["Centimetre","Metre","Paperclip","Kilometre"], answer:2},
     {q:"If a pencil is 8 cubes long and a crayon is 5 cubes long, which is longer?", options:["Crayon","Pencil","Equal","Cannot tell"], answer:1},
     {q:"Taller means ___.", options:["Shorter in height","Greater in height","The same height","Heavier"], answer:1},
     {q:"We measure length to find out ___.", options:["How heavy something is","How long or tall something is","What colour it is","How many there are"], answer:1},
     {q:"Which tool measures length in centimetres?", options:["Scale","Ruler","Thermometer","Clock"], answer:1}
   ]},
  {subject:"Science", title:"Light", summary:"Ontario Grade 1 Science strand: light travels in a straight line, can reflect off surfaces, and allows us to see. The sun is the main natural source of light on Earth.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What is the main natural source of light on Earth?", options:["The moon","A lamp","The sun","Stars"], answer:2},
     {q:"Light travels in a ___.", options:["Curve","Circle","Straight line","Zigzag"], answer:2},
     {q:"Which of these is a source of light?", options:["A rock","A book","A light bulb","A chair"], answer:2},
     {q:"When light hits a mirror it ___.", options:["Disappears","Is absorbed","Bounces back (reflects)","Turns to heat"], answer:2},
     {q:"We need light to ___.", options:["Hear sounds","See objects","Smell things","Taste food"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Rights of Children", summary:"Ontario Grade 1 Social Studies strand A: students identify children's rights as outlined by the United Nations Convention on the Rights of the Child (UNCRC).",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Children have the right to ___.", options:["Do whatever they want","Be safe, cared for, and educated","Ignore school rules","Have no responsibilities"], answer:1},
     {q:"What is the UNCRC?", options:["A type of book","A United Nations document protecting children's rights worldwide","A school subject","A type of toy"], answer:1},
     {q:"Which of these is a child's right?", options:["Working full-time jobs","Education and protection from harm","Having no rules","Ignoring adults"], answer:1},
     {q:"Rights and responsibilities go together because ___.", options:["They are opposite","Our rights give us freedom; responsibilities ensure we respect others' rights","Only rights matter","Only adults have rights"], answer:1},
     {q:"Who is responsible for protecting children's rights?", options:["No one","Children themselves","Governments, communities, and families","Only schools"], answer:2}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"Language", title:"Making Predictions", summary:"Ontario Grade 1 Reading strand: students use text clues, pictures, and prior knowledge to predict what will happen next in a story or text.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Making a prediction means ___.", options:["Guessing what might happen next using clues","Reading the end first","Looking at pictures only","Counting words"], answer:0},
     {q:"What clues help you make a prediction?", options:["Random guessing","Title, pictures, and what you have read so far","Only the last page","The font size"], answer:1},
     {q:"If dark clouds appear in a story, you might predict ___.", options:["It will get hotter","It will rain or storm","The story is ending","A character will laugh"], answer:1},
     {q:"After making a prediction, a good reader ___.", options:["Ignores whether it was right","Reads on to check the prediction","Stops reading","Changes the story"], answer:1},
     {q:"Predictions can be ___.", options:["Always correct","Always wrong","Sometimes right and sometimes wrong, and that is okay","Only for science"], answer:2}
   ]},
  {subject:"Math", title:"Measuring Mass", summary:"Ontario Grade 1 Measurement strand: students compare the mass of objects using non-standard units and a balance scale, using language like heavier and lighter.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Which object is likely heavier: a book or a feather?", options:["Feather","Book","They are equal","Cannot tell"], answer:1},
     {q:"A balance scale tips toward ___.", options:["The lighter object","The heavier object","Neither side","The centre"], answer:1},
     {q:"Mass measures ___.", options:["How long something is","How heavy something is","How tall something is","How hot something is"], answer:1},
     {q:"Which unit is used to measure mass in science?", options:["Centimetres","Litres","Kilograms or grams","Degrees"], answer:2},
     {q:"If one side of a balance is heavier, the other side ___.", options:["Goes down","Goes up","Stays level","Disappears"], answer:1}
   ]},
  {subject:"Science", title:"Magnetism", summary:"Ontario Grade 1 Science strand: magnets attract certain metals (iron, steel, nickel). They have north and south poles; like poles repel, opposite poles attract.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What does a magnet attract?", options:["All metals","Certain metals like iron and steel","Plastic","Wood"], answer:1},
     {q:"A magnet has two ___.", options:["Colours","Sizes","Poles (north and south)","Faces"], answer:2},
     {q:"When two north poles of magnets face each other they ___.", options:["Attract","Repel (push apart)","Stick together","Do nothing"], answer:1},
     {q:"Which of these would a magnet pick up?", options:["A wooden block","A plastic cup","A paper clip","An eraser"], answer:2},
     {q:"Opposite poles of a magnet ___.", options:["Repel each other","Do nothing","Attract each other","Break apart"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Community Helpers", summary:"Ontario Grade 1 Social Studies strand B: students describe the roles of community helpers including firefighters, police, medical workers, and educators.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Who helps put out fires?", options:["A teacher","A firefighter","A doctor","A librarian"], answer:1},
     {q:"Who keeps the neighbourhood safe?", options:["A baker","A police officer","A dentist","A librarian"], answer:1},
     {q:"Who helps us when we are sick?", options:["A firefighter","A police officer","A teacher","A doctor or nurse"], answer:3},
     {q:"What do all community helpers have in common?", options:["They all wear red","They all drive trucks","They help people in the community","They all work at schools"], answer:2},
     {q:"How can you show respect to community helpers?", options:["Ignore them","Thank them and follow their instructions","Argue with them","Avoid them"], answer:1}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"Language", title:"Cause and Effect", summary:"Ontario Grade 1 Reading strand: cause is why something happens; effect is what happens as a result. Signal words include because, so, and as a result.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"The cause is ___.", options:["What happens","Why something happens","When it happens","Who does it"], answer:1},
     {q:"The effect is ___.", options:["Why something happens","What happens as a result","Where it happens","Who does it"], answer:1},
     {q:"Which signal word often introduces a cause?", options:["Then","Finally","Because","Next"], answer:2},
     {q:"It rained, so the grass got wet. What is the effect?", options:["It rained","The rain fell hard","The grass got wet","The sun came out"], answer:2},
     {q:"She studied hard, so she did well on the test. What is the cause?", options:["She did well on the test","She studied hard","The test was easy","The teacher helped"], answer:1}
   ]},
  {subject:"Math", title:"Fractions: Halves", summary:"Ontario Grade 1 Number strand: students divide shapes and sets into two equal parts, using the language of halves and one-half.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"A half means dividing something into ___ equal parts.", options:["1","2","3","4"], answer:1},
     {q:"Which shows a half of a circle?", options:["3/4 of a circle","A whole circle","2 equal semicircles","1 quarter"], answer:2},
     {q:"If you cut a sandwich into halves, how many pieces do you have?", options:["1","2","3","4"], answer:1},
     {q:"One-half is written as ___.", options:["1/3","1/4","1/2","2/1"], answer:2},
     {q:"If you eat one half of a pizza, what fraction is left?", options:["1/3","1/4","1/2","2/3"], answer:2}
   ]},
  {subject:"Science", title:"Weather Patterns", summary:"Ontario Grade 1 Earth and Space Systems strand: students observe and record daily weather conditions including temperature, precipitation, and cloud cover, identifying patterns over time.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Which tool measures air temperature?", options:["Ruler","Thermometer","Scale","Clock"], answer:1},
     {q:"What type of precipitation falls as solid flakes?", options:["Rain","Hail","Sleet","Snow"], answer:3},
     {q:"Cloudy weather means ___.", options:["No clouds in the sky","The sky is covered with clouds","It is raining heavily","The sun is very bright"], answer:1},
     {q:"Weather patterns help us ___.", options:["Pick favourite colours","Plan clothing and activities","Choose what to eat","Watch television"], answer:1},
     {q:"What instrument measures rainfall?", options:["Thermometer","Rain gauge","Barometer","Wind vane"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Land and Water in Canada", summary:"Ontario Grade 1 Social Studies strand B: students identify landforms and bodies of water in Canada including lakes, rivers, mountains, and plains.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Which of these is a body of water?", options:["Mountain","Prairie","Lake Superior","Forest"], answer:2},
     {q:"Which is a landform?", options:["Lake Ontario","Atlantic Ocean","Rocky Mountain","St. Lawrence River"], answer:2},
     {q:"What are the Great Lakes?", options:["Five large lakes in central Canada and the US","Mountains in western Canada","Prairies in central Canada","Glaciers in the north"], answer:0},
     {q:"Canada has ___ coastlines.", options:["One — the east","Three — east, west, and north","Only in the south","No coastline"], answer:1},
     {q:"The Canadian Shield is ___.", options:["A large ocean","A great river","A vast region of ancient rock in central Canada","A mountain range"], answer:2}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"Language", title:"Describing Words: Adjectives", summary:"Ontario Grade 1 Writing strand: adjectives are describing words that tell us more about a noun — they describe colour, size, shape, number, and feeling.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"An adjective is a ___.", options:["Naming word","Action word","Describing word","Connecting word"], answer:2},
     {q:"Which word is an adjective in: The big dog ran?", options:["The","Big","Dog","Ran"], answer:1},
     {q:"Which word is an adjective?", options:["Jump","Happy","Dog","Run"], answer:1},
     {q:"Which sentence has an adjective?", options:["The dog ran.","She ran fast.","The tiny cat sat.","He jumped."], answer:2},
     {q:"Adjectives help us ___.", options:["Name things","Show actions","Describe things more clearly","Connect sentences"], answer:2}
   ]},
  {subject:"Math", title:"Data: Tally Charts", summary:"Ontario Grade 1 Data strand: students collect and organise data using tally marks, where each mark represents one item and a bundle of five is shown with a diagonal line.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"One tally mark represents ___.", options:["5 items","2 items","1 item","10 items"], answer:2},
     {q:"A group of 5 tally marks looks like ___.", options:["IIII","Four vertical lines","Four lines crossed by one diagonal line","IIIII"], answer:2},
     {q:"If you have 7 tally marks, you have ___ items.", options:["5","6","7","8"], answer:2},
     {q:"Why do we use tally marks?", options:["For decoration","To count and record data quickly","To spell words","To draw pictures"], answer:1},
     {q:"IIII I (5 marks) represents how many?", options:["4","5","6","7"], answer:1}
   ]},
  {subject:"Science", title:"The Sun", summary:"Ontario Grade 1 Earth and Space Systems strand: the Sun is a star, the centre of our solar system, and Earth's main source of heat and light. It causes day and night through Earth's rotation.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"The Sun is a ___.", options:["Planet","Moon","Star","Comet"], answer:2},
     {q:"The Sun gives Earth heat and ___.", options:["Rain","Light","Wind","Snow"], answer:1},
     {q:"Day and night are caused by Earth ___.", options:["Moving around the Sun","Rotating (spinning) on its axis","Moving away from the Sun","The Moon blocking the Sun"], answer:1},
     {q:"The Sun rises in the ___ and sets in the ___.", options:["West, east","North, south","East, west","South, north"], answer:2},
     {q:"Why is the Sun important for life on Earth?", options:["It is not important","It provides heat and light needed by plants and animals","Only humans need it","Only plants need it"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Canada's Natural Resources", summary:"Ontario Grade 1 Social Studies strand B: students identify natural resources in Canada such as trees, water, minerals, and farmland and explain why they are important.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"A natural resource is ___.", options:["Something people make in a factory","Something found in nature that people use","A type of money","A building"], answer:1},
     {q:"Which of these is a natural resource?", options:["A plastic bottle","A car","Fresh water","A computer"], answer:2},
     {q:"Why are Canada's forests a natural resource?", options:["They look nice","They provide wood, paper, and habitat for animals","They are cold","They are very tall"], answer:1},
     {q:"Which natural resource do farmers use to grow food?", options:["Rocks","Plastic","Farmland and soil","Metal"], answer:2},
     {q:"Why is it important to protect natural resources?", options:["It is not important","So future generations can also use them","Only adults care about this","Resources never run out"], answer:1}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"Language", title:"Action Words: Verbs", summary:"Ontario Grade 1 Writing strand: verbs are action words that tell what a subject does. Every complete sentence needs a verb.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"A verb is a ___.", options:["Naming word","Describing word","Action word","Connecting word"], answer:2},
     {q:"Which word is a verb: The cat runs fast?", options:["The","Cat","Runs","Fast"], answer:2},
     {q:"Which word is a verb?", options:["Dog","Happy","Jump","Big"], answer:2},
     {q:"Every complete sentence needs a ___.", options:["Noun only","Adjective","Verb","Question mark"], answer:2},
     {q:"Which sentence uses a verb correctly?", options:["The dog happy.","The big dog.","The dog runs.","Dog the runs."], answer:2}
   ]},
  {subject:"Math", title:"Data: Pictographs", summary:"Ontario Grade 1 Data strand: a pictograph uses pictures or symbols to represent data. A key shows what each symbol means.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"In a pictograph, each picture represents ___.", options:["A word","A number or amount shown in the key","A colour","A shape"], answer:1},
     {q:"What is the purpose of a key in a pictograph?", options:["To make it pretty","To explain what each symbol means","To list all students","To show the title"], answer:1},
     {q:"If each star = 2 votes and there are 3 stars, how many votes are there?", options:["3","5","6","2"], answer:2},
     {q:"A pictograph makes data easier to ___.", options:["Hide","Understand and compare","Ignore","Collect"], answer:1},
     {q:"Which type of data is best shown in a pictograph?", options:["Favourite colours of students in a class","The alphabet","How to add numbers","A story"], answer:0}
   ]},
  {subject:"Science", title:"Soil and Earth Materials", summary:"Ontario Grade 1 Earth and Space Systems strand: soil is made of rock particles, organic matter, air, and water. Different soils have different properties.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Soil is made of small pieces of ___ and organic matter.", options:["Plastic","Metal","Rock","Wood"], answer:2},
     {q:"Why is soil important for plants?", options:["It is not","Soil holds the roots and provides nutrients","Soil provides sunlight","Soil provides rain"], answer:1},
     {q:"Which type of soil holds the most water?", options:["Sandy soil","Rocky soil","Clay soil","Gravelly soil"], answer:2},
     {q:"Earthworms help soil by ___.", options:["Destroying roots","Mixing and aerating the soil","Removing water","Making soil harder"], answer:1},
     {q:"What is humus?", options:["A food dip","Decayed organic matter that enriches soil","A type of rock","A type of sand"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Multiculturalism in Canada", summary:"Ontario Grade 1 Social Studies strand A: Canada is a multicultural country where people from many backgrounds live and contribute, enriching Canadian society.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Canada is described as multicultural because ___.", options:["Everyone speaks the same language","People from many different cultures live here","Only Canadian-born people live here","Everyone follows the same traditions"], answer:1},
     {q:"How does multiculturalism make Canada stronger?", options:["It causes problems","It brings different ideas, foods, arts, and perspectives","It does not affect Canada","Only big cities benefit"], answer:1},
     {q:"Which of Canada's two official languages reflects its multicultural roots?", options:["Spanish and English","French and English","French and Italian","English and Chinese"], answer:1},
     {q:"How can we celebrate multiculturalism at school?", options:["Ignore other cultures","Learn about and share different cultural traditions","Speak only one language","Avoid different foods"], answer:1},
     {q:"What does it mean to respect another culture?", options:["Copying everything they do","Ignoring their customs","Valuing their traditions and treating them fairly","Avoiding them"], answer:2}
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"Language", title:"Nouns: People, Places, Things", summary:"Ontario Grade 1 Writing strand: a noun names a person, place, or thing. Proper nouns name specific people, places, or things and begin with a capital letter.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"A noun is a ___.", options:["Describing word","Action word","Naming word","Connecting word"], answer:2},
     {q:"Which word is a noun: The dog runs fast?", options:["The","Dog","Runs","Fast"], answer:1},
     {q:"Which is a proper noun?", options:["dog","city","Canada","house"], answer:2},
     {q:"Proper nouns always start with a ___.", options:["lowercase letter","Period","Capital letter","Number"], answer:2},
     {q:"Which of these is a common noun?", options:["Toronto","Canada","Maria","school"], answer:3}
   ]},
  {subject:"Math", title:"Addition to 20", summary:"Ontario Grade 1 Number strand: students add two numbers with sums up to 20 using strategies such as counting on, making tens, and using doubles.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"7 + 6 = ?", options:["12","13","14","11"], answer:1},
     {q:"9 + 9 = ?", options:["16","17","18","19"], answer:2},
     {q:"5 + 8 = ?", options:["13","12","14","15"], answer:0},
     {q:"11 + 4 = ?", options:["14","15","16","13"], answer:1},
     {q:"6 + 7 = ?", options:["12","13","14","11"], answer:1}
   ]},
  {subject:"Science", title:"Food Chains", summary:"Ontario Grade 1 Life Systems strand: a food chain shows how energy passes from one living thing to another. It starts with a plant (producer), then a herbivore (consumer), then a carnivore.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"In a food chain, plants are called ___.", options:["Consumers","Herbivores","Producers","Carnivores"], answer:2},
     {q:"An animal that eats only plants is called a ___.", options:["Carnivore","Omnivore","Herbivore","Producer"], answer:2},
     {q:"In a food chain, arrows show ___.", options:["Friendship","The direction energy flows","Where animals live","The seasons"], answer:1},
     {q:"Which is a correct simple food chain?", options:["Fox eats grass eats rabbit","Grass is eaten by rabbit, rabbit is eaten by fox","Sun eats grass eats fox","Fox eats sun eats rabbit"], answer:1},
     {q:"A carnivore is an animal that eats ___.", options:["Only plants","Only animals","Both plants and animals","Only grass"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Global Communities", summary:"Ontario Grade 1 Social Studies strand B: students compare communities around the world, identifying similarities and differences in how people meet their basic needs.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Communities around the world are ___.", options:["Exactly the same","All different with nothing in common","Different in some ways and similar in others","Only similar"], answer:2},
     {q:"What basic need do all communities around the world share?", options:["The same language","The same food","Food, shelter, and water","Electricity"], answer:2},
     {q:"How do people in different communities get food?", options:["Everyone grows rice","In many different ways — farming, fishing, buying at stores","Everyone hunts","Everyone buys at supermarkets"], answer:1},
     {q:"What is one way communities around the world are similar?", options:["Same language","Same food","Same sports","People care for each other"], answer:3},
     {q:"Learning about global communities helps us ___.", options:["Ignore other cultures","Understand that we are all connected","Think only our way is right","Avoid other countries"], answer:1}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"Language", title:"Pronouns", summary:"Ontario Grade 1 Writing strand: pronouns take the place of nouns. Examples: I, you, he, she, it, we, they.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"A pronoun takes the place of a ___.", options:["Verb","Adjective","Noun","Adverb"], answer:2},
     {q:"What pronoun replaces 'Maria'?", options:["He","It","She","They"], answer:2},
     {q:"What pronoun replaces 'the boys'?", options:["He","She","It","They"], answer:3},
     {q:"What pronoun replaces 'the dog'?", options:["He","She","It","They"], answer:2},
     {q:"Which sentence uses a pronoun correctly?", options:["Dog runs fast.","Maria she runs fast.","She runs fast.","Running fast."], answer:2}
   ]},
  {subject:"Math", title:"Subtraction from 20", summary:"Ontario Grade 1 Number strand: students subtract single-digit numbers from teens numbers and find differences within 20 using various strategies.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"15 - 7 = ?", options:["7","8","9","6"], answer:1},
     {q:"20 - 9 = ?", options:["10","11","12","9"], answer:1},
     {q:"18 - 6 = ?", options:["11","12","13","10"], answer:1},
     {q:"14 - 8 = ?", options:["5","6","7","4"], answer:1},
     {q:"17 - 9 = ?", options:["7","8","9","6"], answer:1}
   ]},
  {subject:"Science", title:"Animal Habitats", summary:"Ontario Grade 1 Life Systems strand: a habitat is the natural environment where an animal lives, providing food, water, shelter, and space.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"A habitat provides animals with food, water, shelter, and ___.", options:["Toys","Space","Television","Money"], answer:1},
     {q:"Which habitat does a polar bear live in?", options:["Jungle","Desert","Arctic tundra","Rainforest"], answer:2},
     {q:"Which animal lives in a pond habitat?", options:["Camel","Frog","Polar bear","Penguin"], answer:1},
     {q:"A desert habitat is ___.", options:["Cold and wet","Hot and dry with little rainfall","Always covered in snow","Always rainy"], answer:1},
     {q:"What happens to an animal if its habitat is destroyed?", options:["Nothing changes","It may struggle to survive or must find a new habitat","It gets bigger","It becomes stronger"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Helping Others in the Community", summary:"Ontario Grade 1 Social Studies strand A: students explore ways they can contribute to their community through volunteering, kindness, and helping neighbours.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"How can you help your community?", options:["Taking things","Littering","Volunteering and being kind to others","Ignoring others"], answer:2},
     {q:"Why is volunteering important?", options:["It is not","It benefits others and makes the community stronger","Only adults volunteer","It earns money"], answer:1},
     {q:"What is a way kids can help the environment?", options:["Buying more toys","Picking up litter and recycling","Using more electricity","Wasting food"], answer:1},
     {q:"Being kind to a new student at school helps them ___.", options:["Feel uncomfortable","Feel welcome and included","Stay silent","Ignore others"], answer:1},
     {q:"Why do communities need volunteers?", options:["They do not","Volunteers do important work that helps everyone","Volunteering is boring","Only hospitals need volunteers"], answer:1}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"Language", title:"Compound Words", summary:"Ontario Grade 1 Reading strand: a compound word is made of two smaller words joined together to make a new word, such as sunshine, raincoat, and backpack.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"A compound word is ___.", options:["A very long word","Two small words joined to make a new word","A word with a silent letter","A nonsense word"], answer:1},
     {q:"Which is a compound word?", options:["Apple","Beautiful","Sunshine","Elephant"], answer:2},
     {q:"What two words make 'raincoat'?", options:["Rain + coat","Rai + ncoat","R + aincoat","Rainc + oat"], answer:0},
     {q:"What compound word means a bag worn on your back?", options:["Schoolbag","Backpack","Handbag","Purse"], answer:1},
     {q:"Which of these is a compound word?", options:["Running","Quickly","Strangely","Starfish"], answer:3}
   ]},
  {subject:"Math", title:"Ordinal Numbers", summary:"Ontario Grade 1 Number strand: ordinal numbers describe position in a sequence: first (1st), second (2nd), third (3rd), and so on.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"What is the ordinal form of 1?", options:["Onest","First","Oneish","1nd"], answer:1},
     {q:"What is the ordinal form of 3?", options:["Threeth","Thirdly","Third","Threest"], answer:2},
     {q:"If you are 4th in line, how many people are ahead of you?", options:["3","4","5","2"], answer:0},
     {q:"What comes after fifth?", options:["Sixth","Seveth","Fourthly","Fiftth"], answer:0},
     {q:"The ordinal number '2nd' means ___.", options:["Second","Twoth","Twoeth","Secondly"], answer:0}
   ]},
  {subject:"Science", title:"Plants and the Environment", summary:"Ontario Grade 1 Life Systems strand: plants are producers that provide food and oxygen for other living things; they also prevent soil erosion and provide habitats.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Plants produce oxygen through a process called ___.", options:["Digestion","Hibernation","Photosynthesis","Respiration"], answer:2},
     {q:"Why are plants important for animals?", options:["They are not","They provide food and oxygen for animals","They provide electricity","They provide money"], answer:1},
     {q:"What holds soil in place and prevents erosion?", options:["Rocks alone","Plant roots","Rain","Wind"], answer:1},
     {q:"Which of these would NOT survive without plants?", options:["Rocks","Rivers","Most animals","Clouds"], answer:2},
     {q:"How do plants help improve air quality?", options:["They do not","They absorb carbon dioxide and release oxygen","They create pollution","They absorb oxygen"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Celebrations and Traditions", summary:"Ontario Grade 1 Social Studies strand A: students explore different cultural celebrations and traditions, recognising the diversity of practices and their importance to families.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"A tradition is ___.", options:["Something done only once","A special activity a family or culture repeats over time","Always about food","Only for children"], answer:1},
     {q:"Why do families celebrate traditions?", options:["They have to","To mark important events and strengthen bonds","It is boring","To spend money"], answer:1},
     {q:"Which is an example of a tradition?", options:["Brushing your teeth","An annual family holiday gathering","Going to sleep","Watching TV"], answer:1},
     {q:"How are celebrations different around the world?", options:["They are all the same","They vary in customs, foods, and meanings","Only the date changes","Only adults celebrate"], answer:1},
     {q:"Learning about others' celebrations helps us ___.", options:["Ignore differences","Understand and appreciate cultural diversity","Copy everything","Stay separate"], answer:1}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"Language", title:"Synonyms", summary:"Ontario Grade 1 Writing strand: synonyms are words that have the same or similar meanings. Using synonyms makes writing more interesting.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"A synonym is a word that means the ___.", options:["Opposite","Same or similar thing","Nothing at all","Bigger thing"], answer:1},
     {q:"Which is a synonym for big?", options:["Small","Large","Tiny","Little"], answer:1},
     {q:"Which is a synonym for happy?", options:["Sad","Angry","Joyful","Tired"], answer:2},
     {q:"Which is a synonym for fast?", options:["Slow","Quick","Quiet","Soft"], answer:1},
     {q:"Using synonyms in writing makes it ___.", options:["More confusing","More boring","More interesting and varied","Shorter"], answer:2}
   ]},
  {subject:"Math", title:"Money: Coins", summary:"Ontario Grade 1 Number strand: students identify Canadian coins (penny, nickel, dime, quarter) and their values, and count small collections of coins.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"How much is a nickel worth?", options:["1 cent","5 cents","10 cents","25 cents"], answer:1},
     {q:"How much is a dime worth?", options:["1 cent","5 cents","10 cents","25 cents"], answer:2},
     {q:"How much is a quarter worth?", options:["1 cent","5 cents","10 cents","25 cents"], answer:3},
     {q:"Which coin is worth the most?", options:["Penny","Nickel","Dime","Quarter"], answer:3},
     {q:"How many nickels make a dime?", options:["1","2","3","4"], answer:1}
   ]},
  {subject:"Science", title:"Energy and Movement", summary:"Ontario Grade 1 Science Physical Education strand: energy can cause objects to move. Stored energy (potential) and moving energy (kinetic) are two basic forms.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What is energy?", options:["The ability to do work or cause change","A type of rock","A kind of animal","A colour"], answer:0},
     {q:"A ball sitting on a hill has ___ energy.", options:["No","Kinetic (moving)","Potential (stored)","Electrical"], answer:2},
     {q:"A ball rolling down a hill has ___ energy.", options:["No","Kinetic (moving)","Potential (stored)","Chemical"], answer:1},
     {q:"Which of these uses electrical energy?", options:["A rock","A wooden block","A light bulb","A leaf"], answer:2},
     {q:"What energy does the Sun give to Earth?", options:["Mechanical","Heat and light (solar energy)","Chemical","Nuclear"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Traditions from Around the World", summary:"Ontario Grade 1 Social Studies strand A: students explore cultural traditions from different countries, building respect and appreciation for diversity.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Why do countries have their own traditions?", options:["They have to","Traditions reflect the culture, history, and values of a people","Everyone chose the same ones","Rules forced them to"], answer:1},
     {q:"Which festival involves lanterns and is celebrated in China?", options:["Diwali","Hanukkah","Chinese Lantern Festival","Carnival"], answer:2},
     {q:"Diwali is celebrated by people of which background?", options:["Chinese","Hindu (and others in South Asia)","Japanese","European"], answer:1},
     {q:"Why is it important to learn about traditions from around the world?", options:["It is not important","It promotes respect and understanding","It is confusing","Only tourists need to know"], answer:1},
     {q:"Which of these is a Canadian tradition?", options:["Cinco de Mayo","Diwali as celebrated in Canada","Canada Day fireworks","Chinese New Year only"], answer:1}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"Language", title:"Antonyms", summary:"Ontario Grade 1 Writing strand: antonyms are words that have opposite meanings, such as hot/cold, happy/sad, and big/small.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"An antonym is a word that means the ___ of another word.", options:["Same","Opposite","Similar","Bigger"], answer:1},
     {q:"What is the antonym of BIG?", options:["Large","Huge","Small","Giant"], answer:2},
     {q:"What is the antonym of HOT?", options:["Warm","Cold","Cool","Frozen"], answer:1},
     {q:"What is the antonym of DAY?", options:["Morning","Afternoon","Evening","Night"], answer:3},
     {q:"Using antonyms helps us ___.", options:["Make writing longer","Compare and contrast ideas","Confuse readers","Remove nouns"], answer:1}
   ]},
  {subject:"Math", title:"Time: Reading Clocks", summary:"Ontario Grade 1 Measurement strand: students tell time to the hour and half hour on both analogue and digital clocks.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"On a clock, the short hand points to the ___.", options:["Minutes","Seconds","Hour","Day"], answer:2},
     {q:"What time is shown when both hands point to 12?", options:["6:00","12:00","3:00","9:00"], answer:1},
     {q:"If the hour hand points to 3 and the minute hand to 12, the time is ___.", options:["12:03","12:30","3:00","3:30"], answer:2},
     {q:"Half past 4 means ___.", options:["4:00","4:05","4:30","4:15"], answer:2},
     {q:"How many hours are in one day?", options:["12","24","48","60"], answer:1}
   ]},
  {subject:"Science", title:"Simple Machines", summary:"Ontario Grade 1 Science strand: simple machines make work easier. Examples include lever, wheel and axle, pulley, inclined plane, wedge, and screw.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"A simple machine makes work ___.", options:["Harder","Slower","Easier","More confusing"], answer:1},
     {q:"A ramp is an example of an ___.", options:["Lever","Pulley","Inclined plane","Wheel and axle"], answer:2},
     {q:"A wheel and axle reduces ___.", options:["Speed","The force needed to move things","Height","Distance"], answer:1},
     {q:"Which simple machine is a seesaw an example of?", options:["Pulley","Inclined plane","Wedge","Lever"], answer:3},
     {q:"How many types of simple machines are there?", options:["3","4","5","6"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Canada Day and National Holidays", summary:"Ontario Grade 1 Social Studies strand B: students learn about Canada Day and other national holidays, understanding what they celebrate and why they are important.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Canada Day is celebrated on ___.", options:["July 4","July 1","October 1","November 11"], answer:1},
     {q:"What does Canada Day celebrate?", options:["Christmas","Canada's birthday as a nation","Thanksgiving","Halloween"], answer:1},
     {q:"Remembrance Day honours ___.", options:["The founding of Canada","Veterans who served in wars","Canadian athletes","Canadian scientists"], answer:1},
     {q:"What is the date of Remembrance Day?", options:["October 31","December 25","November 11","July 1"], answer:2},
     {q:"Victoria Day in Canada honours ___.", options:["Canada Day celebrations","The Queen's birthday and the monarchy","Halloween","Summer solstice"], answer:1}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"Language", title:"Prefixes: un- and re-", summary:"Ontario Grade 1 Reading strand: a prefix is added to the beginning of a word to change its meaning. Un- means not; re- means again.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"What does the prefix UN- mean?", options:["Again","Before","Not","After"], answer:2},
     {q:"What does UNKIND mean?", options:["Very kind","Not kind","Kind again","Extremely kind"], answer:1},
     {q:"What does the prefix RE- mean?", options:["Not","Before","After","Again"], answer:3},
     {q:"What does REREAD mean?", options:["Not read","Read before","Read again","Read after"], answer:2},
     {q:"Which word has a prefix?", options:["Running","Jumped","Unhappy","Cats"], answer:2}
   ]},
  {subject:"Math", title:"Number Patterns", summary:"Ontario Grade 1 Algebra and Patterning strand: students identify, describe, and extend number patterns involving addition or subtraction.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"What comes next? 2, 4, 6, 8, ___", options:["9","10","12","11"], answer:1},
     {q:"What is the rule? 10, 20, 30, 40...", options:["Add 5","Add 10","Add 2","Add 15"], answer:1},
     {q:"What comes next? 1, 3, 5, 7, ___", options:["8","9","10","6"], answer:1},
     {q:"What is the rule? 20, 18, 16, 14...", options:["Add 2","Subtract 3","Subtract 2","Add 1"], answer:2},
     {q:"What comes next? 5, 10, 15, 20, ___", options:["21","22","25","30"], answer:2}
   ]},
  {subject:"Science", title:"Rocks and Their Properties", summary:"Ontario Grade 1 Earth and Space Systems strand: rocks can be described by colour, texture, hardness, and size. Different rocks have different properties and uses.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Rocks can be described by ___.", options:["Their feelings","Their colour, texture, and hardness","Their names only","Their families"], answer:1},
     {q:"Which rock is used to make jewellery?", options:["Limestone","Granite","Diamond (a mineral)","Sandstone"], answer:2},
     {q:"What does the hardness of a rock tell us?", options:["Its colour","How easily it can be scratched","Its weight","Its age"], answer:1},
     {q:"Where can you find rocks?", options:["Only underground","Only in rivers","Everywhere — on land, in water, underground","Only in mountains"], answer:2},
     {q:"Which of these is made from a natural rock or mineral?", options:["Plastic cup","Salt (a mineral)","Glass window (made from sand, a mineral)","Both b and c"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Maps of Canada", summary:"Ontario Grade 1 Social Studies strand B: students read simple maps of Canada, identifying provinces, territories, capital cities, and geographic regions.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"How many provinces does Canada have?", options:["8","9","10","12"], answer:2},
     {q:"How many territories does Canada have?", options:["1","2","3","4"], answer:2},
     {q:"What is the capital city of Canada?", options:["Toronto","Montreal","Ottawa","Vancouver"], answer:2},
     {q:"Which province is on the far east coast of Canada?", options:["British Columbia","Ontario","Alberta","Newfoundland and Labrador"], answer:3},
     {q:"Which territory is in the far north of Canada?", options:["Ontario","Nunavut","Quebec","Alberta"], answer:1}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"Language", title:"Suffixes: -er and -ing", summary:"Ontario Grade 1 Reading strand: a suffix is added to the end of a word to change its meaning. -Er means one who does; -ing indicates an ongoing action.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"What does the suffix -ER mean when added to a verb?", options:["The action itself","One who does the action","Doing the action now","Having done the action"], answer:1},
     {q:"What does TEACHER mean?", options:["To teach","One who teaches","Is teaching","Taught"], answer:1},
     {q:"What does RUNNING mean?", options:["Ran once","About to run","Currently doing the action of running","One who runs"], answer:2},
     {q:"Which word has a suffix?", options:["Running","Of","The","And"], answer:0},
     {q:"Adding -ING to a verb creates a ___.", options:["Noun","Adjective","Present participle (ongoing action)","Prefix"], answer:2}
   ]},
  {subject:"Math", title:"Addition Strategies", summary:"Ontario Grade 1 Number strand: students use mental math strategies such as doubles, near doubles, make ten, and counting on to add efficiently.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Counting on means starting at the bigger number and ___.", options:["Subtracting","Adding backwards","Counting forward the smaller number","Counting from 1"], answer:2},
     {q:"6 + 6 = 12 is an example of a ___.", options:["Near double","Double","Make ten","Counting on"], answer:1},
     {q:"7 + 6: think 7 + 7 = 14, then subtract 1 = 13. This is a ___.", options:["Double","Near double strategy","Make ten","Counting on"], answer:1},
     {q:"Make 10: 8 + 5 = 8 + 2 + 3 = 10 + 3 = ___", options:["12","13","14","11"], answer:1},
     {q:"Which strategy works best for 9 + 4?", options:["Count from 1","Doubles","Make ten: 9+1+3=13","Subtraction"], answer:2}
   ]},
  {subject:"Science", title:"Water on Earth", summary:"Ontario Grade 1 Earth and Space Systems strand: water covers most of Earth's surface. It exists in three states and cycles through the environment.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What percentage of Earth's surface is covered by water?", options:["About 30 percent","About 50 percent","About 70 percent","About 90 percent"], answer:2},
     {q:"Water in three states: ___.", options:["Solid, liquid, gas","Hot, warm, cold","Fast, slow, still","Deep, shallow, wide"], answer:0},
     {q:"What is the water cycle?", options:["How water is made in factories","The continuous movement of water through evaporation, condensation, and precipitation","How we filter drinking water","How rain is collected in rivers"], answer:1},
     {q:"Which state is water in when it forms clouds?", options:["Solid","Liquid","Gas (water vapour)","Plasma"], answer:2},
     {q:"Why is clean water important?", options:["It is not","All living things need clean water to survive","Only fish need clean water","Only humans need water"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Provinces of Canada", summary:"Ontario Grade 1 Social Studies strand B: students identify the ten provinces of Canada and some facts about each, locating them on a map.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Which province is on the west coast of Canada?", options:["Ontario","Quebec","British Columbia","Manitoba"], answer:2},
     {q:"Which province is Canada's largest by area?", options:["Ontario","Quebec","Alberta","British Columbia"], answer:1},
     {q:"The Maritime provinces include New Brunswick, Nova Scotia, and ___.", options:["Ontario","Prince Edward Island","Quebec","Newfoundland"], answer:1},
     {q:"Which province is known for the Prairies (flat grasslands)?", options:["British Columbia","Ontario","Saskatchewan","Quebec"], answer:2},
     {q:"What is the capital city of Quebec?", options:["Montreal","Quebec City","Ottawa","Toronto"], answer:1}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"Language", title:"Poetry", summary:"Ontario Grade 1 Reading and Writing strands: students read and write simple poems, identifying rhyme, rhythm, and descriptive language, and appreciating how poets choose words carefully.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Poetry often uses ___.", options:["Only long sentences","Rhyme, rhythm, and descriptive language","Only facts","Lots of numbers"], answer:1},
     {q:"Which lines rhyme?", options:["The cat sat on the mat / The dog ran to school","Roses are red / Violets are blue","Today is Monday / I ate my lunch","She ran fast / He jumped high"], answer:1},
     {q:"Rhythm in a poem means ___.", options:["The poem is long","A regular beat or pattern in the words","The poem rhymes","The poem is happy"], answer:1},
     {q:"A poem is different from a story because ___.", options:["It has no words","It often uses line breaks and focuses on feelings and images","It is always longer","It has no characters"], answer:1},
     {q:"Which is an example of descriptive language in a poem?", options:["She went to the store","The shimmering silver moon glowed softly","It was night","He walked home"], answer:1}
   ]},
  {subject:"Math", title:"Subtraction Strategies", summary:"Ontario Grade 1 Number strand: students use strategies such as counting back, fact families, and think-addition to subtract efficiently.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Counting back: 12 - 3 means start at 12 and count back ___.", options:["12 steps","1 step","3 steps","2 steps"], answer:2},
     {q:"Think-addition: 13 - 5 = ? Think 5 + ___ = 13", options:["7","8","9","6"], answer:1},
     {q:"A fact family uses the same three numbers. 7+5=12, 5+7=12, 12-5=___, 12-7=5.", options:["5","7","4","6"], answer:1},
     {q:"Which is a subtraction strategy?", options:["Counting on from 1","Making a ten","Counting back from the bigger number","Skip counting by 5"], answer:2},
     {q:"14 - 6 = ?", options:["7","8","9","6"], answer:1}
   ]},
  {subject:"Science", title:"Stars and Space", summary:"Ontario Grade 1 Earth and Space Systems strand: the Sun is the closest star to Earth. Stars are large balls of hot gas. The Moon orbits Earth.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"The Sun is a ___.", options:["Planet","Moon","Large ball of hot gas called a star","Comet"], answer:2},
     {q:"Which planet do we live on?", options:["Mars","Venus","Earth","Jupiter"], answer:2},
     {q:"The Moon ___.", options:["Makes its own light","Orbits (circles) the Earth","Is a star","Is bigger than Earth"], answer:1},
     {q:"Stars are visible mainly at ___.", options:["Noon","Dawn","Night","Dusk only"], answer:2},
     {q:"How does the Moon appear to change shape?", options:["It actually changes shape","We see different amounts of its lit side as it orbits Earth","Clouds cover it","It grows and shrinks"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Caring for the Environment", summary:"Ontario Grade 1 Social Studies strand B: students identify ways to protect the environment including reducing waste, recycling, and conserving water and energy.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What does REDUCE mean in reduce, reuse, recycle?", options:["Throw away more","Use less of something","Make something bigger","Buy more"], answer:1},
     {q:"Which is an example of recycling?", options:["Throwing a bottle in the garbage","Turning a used newspaper into new paper","Buying new items","Wasting water"], answer:1},
     {q:"Why should we turn off lights when leaving a room?", options:["Lights do not matter","To save electrical energy","Lights are too bright","To make the room dark"], answer:1},
     {q:"What is one way to conserve water?", options:["Leave the tap running","Take very long showers","Turn off the tap while brushing teeth","Water your lawn every hour"], answer:2},
     {q:"Caring for the environment benefits ___.", options:["Only humans","Only animals","Both humans and all living things now and in the future","Nobody"], answer:2}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"Language", title:"Non-Fiction Text Features", summary:"Ontario Grade 1 Reading strand: non-fiction texts contain features like headings, photographs, captions, table of contents, and indexes that help readers find and understand information.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"What is a heading in a non-fiction text?", options:["A type of hat","A bold title that tells what a section is about","A picture at the top","The author's name"], answer:1},
     {q:"What is a caption?", options:["A title","Words that explain a photograph or illustration","A type of heading","The conclusion"], answer:1},
     {q:"What does a table of contents show?", options:["The author's biography","Chapter/section titles and page numbers","Definitions of words","Only pictures"], answer:1},
     {q:"How is a non-fiction text different from fiction?", options:["It has pictures","Non-fiction contains facts about real topics; fiction is made up","It is shorter","It has more chapters"], answer:1},
     {q:"Which of these is a non-fiction book?", options:["The Three Little Pigs","Charlotte's Web","Encyclopaedia of Animals","Harry Potter"], answer:2}
   ]},
  {subject:"Math", title:"Review: Number Sense to 50", summary:"Ontario Grade 1 Number strand review: students count, compare, order, and represent numbers to 50, and demonstrate understanding of place value and operations.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"What is 3 tens and 7 ones?", options:["30","37","73","13"], answer:1},
     {q:"Which is greatest: 24, 42, or 34?", options:["24","34","42","44"], answer:2},
     {q:"15 + 7 = ?", options:["20","22","21","23"], answer:1},
     {q:"20 - 8 = ?", options:["11","12","13","14"], answer:1},
     {q:"Skip count by 5s: 25, 30, ___", options:["33","35","40","32"], answer:1}
   ]},
  {subject:"Science", title:"Seasons Review", summary:"Ontario Grade 1 Earth and Space Systems strand review: students review the four seasons, their characteristics, and how plants, animals, and people respond to seasonal changes.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What are the four seasons in order starting with spring?", options:["Spring, Summer, Fall, Winter","Summer, Fall, Winter, Spring","Winter, Spring, Summer, Fall","Fall, Winter, Spring, Summer"], answer:0},
     {q:"In which season do most plants grow flowers?", options:["Winter","Fall","Spring and Summer","No season"], answer:2},
     {q:"Which season has the longest days in Ontario?", options:["Winter","Fall","Summer","Spring"], answer:2},
     {q:"What do deciduous trees do in fall?", options:["Grow new leaves","Lose their leaves","Stay the same","Grow taller only"], answer:1},
     {q:"In Ontario, which season has the coldest temperatures?", options:["Fall","Spring","Summer","Winter"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Rights Review", summary:"Ontario Grade 1 Social Studies strand A review: students review children's rights, responsibilities, and what it means to be a responsible citizen in the school and community.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What are the three main rights of all children?", options:["Work, play, travel","Education, safety, and being cared for","Money, toys, vacations","Adults choose their rights"], answer:1},
     {q:"What is a responsibility?", options:["Something we are paid for","Something we are expected to do for ourselves and others","Something only adults have","Something we can always skip"], answer:1},
     {q:"Name one way to be a responsible student.", options:["Talking in class","Helping others and doing your work","Ignoring instructions","Being noisy"], answer:1},
     {q:"Responsible citizens ___.", options:["Only follow rules they like","Follow rules, help others, and care for their community","Do whatever they want","Never follow rules"], answer:1},
     {q:"Why do rights and responsibilities go together?", options:["They do not","Having rights means taking responsibility to respect others' rights too","Only adults need to think about this","Rights are more important"], answer:1}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"Language", title:"Creative Writing", summary:"Ontario Grade 1 Writing strand: students write short creative stories with a beginning, middle, and end, using descriptive language, interesting characters, and a simple plot.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Creative writing lets you ___.", options:["Write only facts","Create imaginary stories and characters","Write only your name","Copy other stories"], answer:1},
     {q:"A good creative story has a ___.", options:["Beginning only","Beginning, middle, and end","Middle only","Only a problem"], answer:1},
     {q:"What makes a story more interesting?", options:["Very short sentences only","Descriptive language and interesting characters","Just names and places","Numbers and lists"], answer:1},
     {q:"The problem in a story is ___.", options:["The beginning","The ending","The challenge the character must solve","The setting"], answer:2},
     {q:"A story's solution is ___.", options:["The problem","How the character solves the problem","The setting","The beginning"], answer:1}
   ]},
  {subject:"Math", title:"Review: Patterns and Shapes", summary:"Ontario Grade 1 Geometry and Patterning review: students identify and extend patterns, and describe properties of 2D and 3D shapes.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Which 2D shape has three sides?", options:["Square","Rectangle","Circle","Triangle"], answer:3},
     {q:"What comes next? Triangle, Square, Triangle, Square, ___", options:["Circle","Triangle","Rectangle","Square"], answer:1},
     {q:"A cube has how many faces?", options:["4","5","6","8"], answer:2},
     {q:"Which is a 3D shape?", options:["Circle","Square","Sphere","Triangle"], answer:2},
     {q:"What is the pattern rule? 5, 10, 15, 20...", options:["Add 2","Add 5","Add 10","Add 3"], answer:1}
   ]},
  {subject:"Science", title:"Life Cycles Review", summary:"Ontario Grade 1 Life Systems strand review: students review life cycles of different animals including butterfly, frog, and chicken, identifying the stages.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What are the four stages of a butterfly's life cycle?", options:["Egg, larva, pupa, adult","Baby, child, teen, adult","Seed, sprout, plant, flower","Egg, chick, chicken, adult"], answer:0},
     {q:"What is a tadpole?", options:["A baby butterfly","A baby frog","A type of fish","A baby bird"], answer:1},
     {q:"In the life cycle of a chicken: egg, chick, ___.", options:["Larva","Pupa","Adult chicken","Caterpillar"], answer:2},
     {q:"All life cycles ___.", options:["Begin with an adult","End with a seed","Are continuous processes","Are the same for all animals"], answer:2},
     {q:"What is metamorphosis?", options:["A type of habitat","A kind of rock","A process of dramatic change in form during a life cycle","A season change"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Community Review", summary:"Ontario Grade 1 Social Studies review: students review the concept of community, types of communities, community workers, and the importance of caring for the environment.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What is a community?", options:["A building","A group of people living and working together in a place","A type of map","A natural resource"], answer:1},
     {q:"Name two types of communities.", options:["Urban and rural","Big and small","Old and new","Rich and poor"], answer:0},
     {q:"Which community worker helps people get from place to place?", options:["A teacher","A bus driver or train conductor","A doctor","A librarian"], answer:1},
     {q:"Why should communities care for the environment?", options:["Only some communities do","To keep the natural world healthy for everyone now and in the future","It is not necessary","Only scientists care about this"], answer:1},
     {q:"What makes a community strong?", options:["Only money","Cooperation, diversity, and people helping each other","Lots of buildings","Only having the same culture"], answer:1}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"Language", title:"Story Structure Review", summary:"Ontario Grade 1 Reading and Writing strands review: students apply understanding of story structure (characters, setting, problem, solution) to read and write stories.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"What are the five main story elements?", options:["Title, pages, words, pictures, cover","Characters, setting, problem, events, solution","Beginning, ending, middle, pictures, words","Nouns, verbs, adjectives, adverbs, pronouns"], answer:1},
     {q:"The setting tells us ___.", options:["The characters' feelings","Where and when the story takes place","The main problem","The lesson"], answer:1},
     {q:"The problem in a story creates ___.", options:["The happy ending","The setting","Conflict and suspense","The characters"], answer:1},
     {q:"Identifying story elements helps readers ___.", options:["Read faster","Understand and remember stories better","Skip pages","Count words"], answer:1},
     {q:"Which element is most important in a story?", options:["Setting","Characters","All elements work together","Pictures"], answer:2}
   ]},
  {subject:"Math", title:"Review: Addition and Subtraction", summary:"Ontario Grade 1 Number strand review: students apply addition and subtraction strategies to solve problems within 20.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"14 + 5 = ?", options:["18","19","20","21"], answer:1},
     {q:"17 - 8 = ?", options:["8","9","10","7"], answer:1},
     {q:"A farmer has 12 chickens. 4 run away. How many are left?", options:["7","8","9","10"], answer:1},
     {q:"Sam has 6 apples and gets 7 more. How many total?", options:["12","13","14","15"], answer:1},
     {q:"20 - 11 = ?", options:["8","9","10","11"], answer:1}
   ]},
  {subject:"Science", title:"Animal Review", summary:"Ontario Grade 1 Life Systems strand review: students review key concepts about animals including needs, habitats, young, and adaptations.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What do all animals need to survive?", options:["Television","Food, water, air, and shelter","Only food","Money"], answer:1},
     {q:"An adaptation is ___.", options:["A type of habitat","A special feature that helps an animal survive","A kind of food","A life cycle stage"], answer:1},
     {q:"Which animal is adapted to cold Arctic environments?", options:["Camel","Polar bear","Frog","Butterfly"], answer:1},
     {q:"What is a food chain?", options:["A chain you can eat","A sequence showing who eats whom in an ecosystem","A type of animal","A habitat"], answer:1},
     {q:"Baby animals grow to look like their ___.", options:["Owners","Teachers","Parents","Friends"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Heritage Review", summary:"Ontario Grade 1 Social Studies strand A review: students review concepts of heritage, identity, family, traditions, and cultural celebrations.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Heritage includes ___.", options:["Only buildings","The traditions, stories, values, and culture passed through generations","Only money","Only food"], answer:1},
     {q:"How does learning about our heritage help us?", options:["It does not","It helps us understand who we are and where we come from","It is boring","Only adults need to learn heritage"], answer:1},
     {q:"Which of these is part of a family's heritage?", options:["A new toy","A traditional recipe passed down through generations","A new house","A recent movie"], answer:1},
     {q:"How do families pass on their heritage?", options:["By forgetting old traditions","Through stories, traditions, celebrations, and language","By never celebrating","By moving away"], answer:1},
     {q:"Why is Canada's multicultural heritage an asset?", options:["It causes confusion","It brings diverse perspectives and richness to Canadian society","It creates problems","Only in big cities"], answer:1}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"Language", title:"Reading Fluency", summary:"Ontario Grade 1 Reading strand: reading fluency means reading smoothly, at an appropriate pace, with expression. Practice with familiar texts builds fluency.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Reading fluency means ___.", options:["Reading as fast as possible","Reading smoothly, accurately, and with expression","Reading silently only","Reading only short books"], answer:1},
     {q:"Which practice builds reading fluency?", options:["Reading a new book every day only","Re-reading familiar texts and reading aloud","Only reading in your head","Only reading alone"], answer:1},
     {q:"Expression in reading means ___.", options:["Reading in a monotone voice","Changing your voice to match the mood and punctuation","Only whispering","Only shouting"], answer:1},
     {q:"A fluent reader ___.", options:["Reads every word slowly","Pauses at commas and periods","Sounds out every letter individually","Never re-reads"], answer:1},
     {q:"Why is reading fluency important?", options:["It is not","Fluent reading allows you to focus on understanding the meaning","Only speed matters","Only accuracy matters"], answer:1}
   ]},
  {subject:"Math", title:"Review: Measurement", summary:"Ontario Grade 1 Measurement strand review: students apply understanding of length, mass, capacity, and time to solve problems.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"Which tool measures length?", options:["Scale","Ruler","Thermometer","Clock"], answer:1},
     {q:"Which measures how heavy something is?", options:["Ruler","Thermometer","Scale","Clock"], answer:2},
     {q:"Half past 7 means ___.", options:["7:05","7:15","7:30","7:50"], answer:2},
     {q:"If a pencil is 10 cubes long and a pen is 14 cubes long, which is shorter?", options:["Pen","Pencil","Equal","Cannot tell"], answer:1},
     {q:"What unit do we use to measure length in metric system?", options:["Pounds","Kilograms","Centimetres","Degrees"], answer:2}
   ]},
  {subject:"Science", title:"Plant Review", summary:"Ontario Grade 1 Life Systems and Earth strand review: students review plant parts, plant needs, life cycles, and the importance of plants to the environment.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Which part of a plant makes food?", options:["Root","Stem","Leaf (through photosynthesis)","Seed"], answer:2},
     {q:"What are the four things plants need to grow?", options:["Books, pencils, chairs, desks","Sunlight, water, air, and nutrients from soil","Money, toys, television, games","Electricity, heat, noise, colour"], answer:1},
     {q:"What does a plant seed need to germinate?", options:["Darkness only","Water, warmth, and air","Only sunlight","Only soil"], answer:1},
     {q:"A fruit contains ___.", options:["Only juice","Seeds that can grow into new plants","Roots","Stems"], answer:1},
     {q:"Why are plants important to the environment?", options:["They are not","They produce oxygen, provide food, and support habitats","Only for decoration","Only for food"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Culture Review", summary:"Ontario Grade 1 Social Studies strand A review: students review key vocabulary and concepts related to culture, including traditions, celebrations, language, and respect for diversity.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Culture includes ___.", options:["Only clothing","Language, traditions, art, food, and values of a group of people","Only food","Only music"], answer:1},
     {q:"How do we show respect for different cultures?", options:["Ignoring them","Making fun of them","Learning about them and treating everyone fairly","Copying everything"], answer:2},
     {q:"Why is cultural diversity an asset in Canada?", options:["It causes problems","It enriches society with different perspectives and ideas","Only if everyone speaks the same language","Only in big cities"], answer:1},
     {q:"Which is the best way to learn about another culture?", options:["Assume you know everything","Ask respectful questions and listen to learn","Read one book and decide","Watch one movie"], answer:1},
     {q:"Multiculturalism in Canada means ___.", options:["Only one culture is valued","All cultures are respected and valued","French and English only","Immigrants must forget their culture"], answer:1}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"Language", title:"Spelling Patterns: -ight, -ake, -ine", summary:"Ontario Grade 1 Reading strand: spelling patterns help students decode and spell new words. Word families like night, sight, light; cake, lake, make; mine, fine, pine share patterns.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which word belongs to the -IGHT family?", options:["Lake","Mine","Night","Cake"], answer:2},
     {q:"Which word belongs to the -AKE family?", options:["Night","Light","Right","Cake"], answer:3},
     {q:"Which word belongs to the -INE family?", options:["Sight","Fine","Night","Lake"], answer:1},
     {q:"Which spelling pattern do BRIGHT and TIGHT share?", options:["ake","ine","ight","ake"], answer:2},
     {q:"Learning spelling patterns helps us ___.", options:["Only spell one word","Read and spell many words in the same family","Draw letters only","Sound out every letter always"], answer:1}
   ]},
  {subject:"Math", title:"Review: Data and Probability", summary:"Ontario Grade 1 Data strand review: students collect, organise, and interpret data using tally charts and pictographs, and explore basic probability.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"A tally chart uses ___ to count data.", options:["Pictures","Numbers only","Tally marks","Coins"], answer:2},
     {q:"A pictograph uses ___ to show data.", options:["Only numbers","Pictures or symbols","Only tally marks","Letters"], answer:1},
     {q:"If 5 students chose apples and 3 chose oranges, which is more popular?", options:["Oranges","Apples","Equal","Cannot tell"], answer:1},
     {q:"Probability means ___.", options:["Collecting data","The chance of an event happening","Drawing graphs","Counting by 5s"], answer:1},
     {q:"If a bag has 3 red and 1 blue marble, reaching in without looking gives you a better chance of pulling out a ___.", options:["Blue","Red","Green","Cannot tell"], answer:1}
   ]},
  {subject:"Science", title:"Earth and Weather Review", summary:"Ontario Grade 1 Earth and Space Systems review: students review weather patterns, the water cycle, rocks, soil, and the Sun's role in Earth's systems.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What causes day and night?", options:["Earth moving around the Sun","Earth rotating on its axis","The Moon blocking the Sun","Clouds covering the sky"], answer:1},
     {q:"The water cycle involves ___.", options:["Evaporation, condensation, and precipitation","Only rain falling","Only rivers flowing","Only clouds forming"], answer:0},
     {q:"What is a thermometer used for?", options:["Measuring length","Measuring mass","Measuring temperature","Measuring time"], answer:2},
     {q:"Soil is made of ___.", options:["Only sand","Rock particles, organic matter, air, and water","Only clay","Only rocks"], answer:1},
     {q:"The Sun provides Earth with ___.", options:["Only light","Only heat","Heat and light energy essential for life","Water"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Citizenship and Community", summary:"Ontario Grade 1 Social Studies review: students review civic concepts including rights, responsibilities, community participation, and environmental stewardship.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What does it mean to be a good citizen?", options:["Following only favourite rules","Ignoring community issues","Being responsible, respectful, and contributing to your community","Doing whatever you want"], answer:2},
     {q:"Why is voting important in a democracy?", options:["It is not","Citizens choose their leaders and have a voice in decisions","Only important people vote","Votes do not count"], answer:1},
     {q:"How can children participate in their community?", options:["Only adults participate","Through volunteering, recycling, and helping neighbours","By staying home","By watching others"], answer:1},
     {q:"What is one way to care for the community environment?", options:["Littering","Wasting water","Reducing, reusing, and recycling","Using more electricity"], answer:2},
     {q:"A democratic community values ___.", options:["Silence","Only one person's opinion","Fairness, equality, and participation of all members","Money above all"], answer:2}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"Language", title:"Reading Skills Review", summary:"Ontario Grade 1 Reading strand review: students review key reading strategies including predicting, retelling, identifying main idea, making connections, and using text features.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"Which reading strategy helps you guess what happens next?", options:["Retelling","Connecting","Predicting","Summarising"], answer:2},
     {q:"Retelling a story means ___.", options:["Reading it again","Telling the main events in your own words in order","Drawing pictures","Changing the ending"], answer:1},
     {q:"The main idea is ___.", options:["A small detail","What the text is mostly about","The first sentence always","The title"], answer:1},
     {q:"A text-to-self connection means ___.", options:["The text connects to another book","Comparing two texts","Relating the text to your own personal experience","Connecting to world events"], answer:2},
     {q:"Non-fiction text features include ___.", options:["Plot and characters","Headings, captions, and index","Only pictures","Stories and poems"], answer:1}
   ]},
  {subject:"Math", title:"Review: Number Sense", summary:"Ontario Grade 1 Number strand review: students review counting, place value, addition, subtraction, fractions, and money.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"4 tens + 7 ones = ?", options:["40","47","74","17"], answer:1},
     {q:"18 + 5 = ?", options:["22","23","24","21"], answer:1},
     {q:"20 - 13 = ?", options:["6","7","8","9"], answer:1},
     {q:"One-half is written as ___.", options:["1/3","1/4","1/2","2/3"], answer:2},
     {q:"A dime is worth ___ cents.", options:["5","10","25","50"], answer:1}
   ]},
  {subject:"Science", title:"Life Science Review", summary:"Ontario Grade 1 Life Systems strand review: students review living vs non-living, needs of living things, plants, animals, food chains, and habitats.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"What are the four needs of all living things?", options:["Sun, moon, stars, planets","Air, water, food, and shelter","Books, toys, music, games","Electricity, light, heat, money"], answer:1},
     {q:"Name two parts of a plant.", options:["Wheel and pedal","Root and leaf","Lens and frame","Door and window"], answer:1},
     {q:"A food chain starts with a ___.", options:["Carnivore","Herbivore","Producer (plant)","Decomposer"], answer:2},
     {q:"A habitat provides an animal with ___.", options:["Toys and entertainment","Food, water, shelter, and space","Electricity and heat","School and education"], answer:1},
     {q:"Which best describes metamorphosis?", options:["A type of habitat","A food chain","A dramatic change in form during a life cycle","A kind of rock"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Review: Communities and Canada", summary:"Ontario Grade 1 Social Studies review: students demonstrate understanding of communities, Canadian geography, symbols, and civic values.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"Which Canadian symbol has a maple leaf?", options:["The flag","The coat of arms","The dollar bill","All three"], answer:3},
     {q:"What is the capital city of Canada?", options:["Toronto","Ottawa","Montreal","Vancouver"], answer:1},
     {q:"How many provinces does Canada have?", options:["8","9","10","12"], answer:2},
     {q:"Which of the following is an example of multiculturalism?", options:["Everyone speaks the same language","Many different cultures contributing to society","One culture being better","Avoiding other cultures"], answer:1},
     {q:"What should every citizen do to keep their community clean?", options:["Litter occasionally","Leave lights on always","Reduce waste and recycle","Waste water"], answer:2}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"Language", title:"Year Review: Language Arts", summary:"Ontario Grade 1 Language strand comprehensive review: students demonstrate reading, writing, and oral communication skills developed throughout the year.",
   resourceLabel:"TVO Learn: Grade 1 Language", resourceUrl:"https://tvolearn.com/pages/grade-1-language",
   quiz:[
     {q:"A noun names a ___.", options:["Action","Person, place, or thing","Describing word","Connecting word"], answer:1},
     {q:"A verb shows ___.", options:["A name","An action or state of being","A description","A connection"], answer:1},
     {q:"An adjective describes a ___.", options:["Verb","Noun","Adverb","Pronoun"], answer:1},
     {q:"Which is a complete sentence?", options:["The dog.","Runs fast.","The dog runs.","Big dog fast."], answer:2},
     {q:"Why is reading every day important?", options:["It is not","It builds vocabulary, comprehension, and imagination","Only for school","Only for homework"], answer:1}
   ]},
  {subject:"Math", title:"Year Review: Mathematics", summary:"Ontario Grade 1 Mathematics comprehensive review covering number sense, geometry, measurement, patterning, and data.",
   resourceLabel:"TVO Learn: Grade 1 Mathematics", resourceUrl:"https://tvolearn.com/pages/grade-1-mathematics",
   quiz:[
     {q:"3 tens + 5 ones = ?", options:["53","30","35","45"], answer:2},
     {q:"9 + 8 = ?", options:["16","17","18","15"], answer:1},
     {q:"20 - 7 = ?", options:["12","13","14","11"], answer:1},
     {q:"A square has ___ equal sides.", options:["2","3","4","5"], answer:2},
     {q:"Skip count by 2s: 16, 18, 20, ___", options:["21","22","24","23"], answer:1}
   ]},
  {subject:"Science", title:"Year Review: Science", summary:"Ontario Grade 1 Science comprehensive review covering life systems, earth and space, matter, and physical science.",
   resourceLabel:"TVO Learn: Grade 1 Science & Technology", resourceUrl:"https://tvolearn.com/pages/grade-1-science-and-technology",
   quiz:[
     {q:"Living things need ___.", options:["Electricity and television","Air, water, food, and shelter","Money and toys","Books and pencils"], answer:1},
     {q:"Earth has ___ seasons.", options:["2","3","4","5"], answer:2},
     {q:"A push and pull are examples of ___.", options:["Weather","Forces","Patterns","States of matter"], answer:1},
     {q:"The Sun is a ___.", options:["Planet","Moon","Star","Comet"], answer:2},
     {q:"Plants make their food using sunlight through ___.", options:["Digestion","Hibernation","Photosynthesis","Respiration"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Year Review: Social Studies", summary:"Ontario Grade 1 Social Studies comprehensive review covering family, community, Canada, and civic values.",
   resourceLabel:"TVO Learn: Grade 1 Social Studies", resourceUrl:"https://tvolearn.com/pages/grade-1-social-studies",
   quiz:[
     {q:"What is the capital of Canada?", options:["Toronto","Montreal","Ottawa","Vancouver"], answer:2},
     {q:"Community workers ___.", options:["Create problems","Provide services that help people","Only work for money","Are not important"], answer:1},
     {q:"What does it mean to be a good citizen?", options:["Following only favourite rules","Being responsible and contributing positively to the community","Ignoring rules","Doing whatever you want"], answer:1},
     {q:"Canada's two official languages are ___.", options:["Spanish and English","French and English","Italian and French","English and Chinese"], answer:1},
     {q:"Why is respecting all cultures important in Canada?", options:["It is not","Canada is built on diversity and everyone deserves respect","Only some cultures matter","Only in big cities"], answer:1}
   ]},
]},
];

export default curriculum;