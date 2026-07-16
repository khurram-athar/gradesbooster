import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"Language", title:"Short Vowel Sounds", summary:"Ontario Grade 1 Reading strand: students blend short vowel sounds in CVC words such as cat, bed, pig, hop, sun.",
   resourceLabel:"YouTube: Short Vowel Sounds", resourceUrl:"https://www.youtube.com/results?search_query=Short%20Vowel%20Sounds%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=RUSCz41aDug",
   quiz:[
     {q:"Which word has the short A sound?", options:["Cane","Cape","Cake","Cat"], answer:3},
     {q:"Which word has the short E sound?", options:["Bead","Beat","Bed","Bean"], answer:2},
     {q:"Which word has the short I sound?", options:["Pig","Fine","Kite","Bike"], answer:0},
     {q:"Which word has the short O sound?", options:["Hope","Hop","Coat","Note"], answer:1},
     {q:"Which word has the short U sound?", options:["Cube","Mule","Fun","Tune"], answer:2}
   ],
   worksheet:[
     {prompt:"Fill in the short vowel: c_t (a pet that meows)", answers:["a"]},
     {prompt:"Fill in the short vowel: p_g (a farm animal)", answers:["i"]},
     {prompt:"Fill in the short vowel: s_n (it shines in the sky)", answers:["u"]}
   ]},
  {subject:"Math", title:"Counting to 20", summary:"Ontario Grade 1 Number strand: students count forward and backward by 1s within 20 and represent quantities using objects and numerals.",
   resourceLabel:"YouTube: Counting to 20", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20to%2020%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=D0Ajq682yrA",
   quiz:[
     {q:"What number comes after 15?", options:["13","16","17","14"], answer:1},
     {q:"What number is one less than 10?", options:["12","8","11","9"], answer:3},
     {q:"Count: 17, 18, 19, ___", options:["22","20","18","21"], answer:1},
     {q:"Which number is between 12 and 14?", options:["13","15","11","10"], answer:0},
     {q:"How many fingers on two hands?", options:["8","11","9","10"], answer:3}
   ],
   worksheet:[
     {prompt:"What number comes right after 15?", answers:["16","sixteen"]},
     {prompt:"What number is one less than 10?", answers:["9","nine"]},
     {prompt:"Count on: 17, 18, 19, ___", answers:["20","twenty"]}
   ]},
  {subject:"Science", title:"Living and Non-living Things", summary:"Ontario Grade 1 Life Systems strand: living things grow, reproduce, and respond to their environment; non-living things do not.",
   resourceLabel:"YouTube: Living and Non-living Things", resourceUrl:"https://www.youtube.com/results?search_query=Living%20and%20Non-living%20Things%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=yW5VbMEDRJk",
   quiz:[
     {q:"Which of these is a living thing?", options:["Tree","Rock","Table","Chair"], answer:0},
     {q:"Which is NOT a living thing?", options:["Brick","Flower","Dog","Bird"], answer:0},
     {q:"Living things need food and ___.", options:["Television","Electricity","Water","Money"], answer:2},
     {q:"Which is a sign that something is alive?", options:["It is heavy","It is coloured","It is hard","It grows and changes"], answer:3},
     {q:"A plant is a living thing because it ___.", options:["Is green","Is made of wood","Grows and makes seeds","Cannot move"], answer:2}
   ],
   worksheet:[
     {prompt:"A tree is a ___ thing.", answers:["living"]},
     {prompt:"A chair is a ___ thing.", answers:["non-living","nonliving","non living"]},
     {prompt:"Living things grow and ___.", answers:["change","changes"]}
   ]},
  {subject:"SocialStudies", title:"My Family", summary:"Ontario Grade 1 Social Studies Heritage and Identity strand: students describe their family and recognize that families differ in structure and traditions.",
   resourceLabel:"YouTube: My Family", resourceUrl:"https://www.youtube.com/results?search_query=My%20Family%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=FHaObkHEkHQ",
   quiz:[
     {q:"A family is a group of people who ___.", options:["Work at the same job","Live on the same street","Care for each other","All look the same"], answer:2},
     {q:"Which of these is a family member?", options:["Teacher","Neighbour","Parent","Friend"], answer:2},
     {q:"Families can be ___.", options:["Only large","Many different sizes","Always the same","Only small"], answer:1},
     {q:"What do most families do together?", options:["Share meals and celebrate","Go to the same school","Work the same job","Ignore each other"], answer:0},
     {q:"Every family is ___.", options:["Unique and special","Always big","Always small","Exactly the same"], answer:0}
   ],
   worksheet:[
     {prompt:"A family is a group of people who ___ for each other.", answers:["care"]},
     {prompt:"Families can be many different ___.", answers:["sizes"]},
     {prompt:"What do most families do together? Share ___.", answers:["meals","meal"]}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"Language", title:"Long Vowel Sounds", summary:"Ontario Grade 1 Reading strand: long vowels say their name, as in cake, bee, kite, boat, cube. The silent E rule often signals a long vowel.",
   resourceLabel:"YouTube: Long Vowel Sounds", resourceUrl:"https://www.youtube.com/results?search_query=Long%20Vowel%20Sounds%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=xTKPXa9y9TM",
   quiz:[
     {q:"Which word has a long A sound?", options:["Cap","Cat","Cab","Cake"], answer:3},
     {q:"Which word has a long E sound?", options:["Bet","Bed","Bee","Best"], answer:2},
     {q:"Which word has a long O sound?", options:["Hop","Hope","Hog","Hot"], answer:1},
     {q:"What makes the vowel long in the word KITE?", options:["Silent E at the end","Capital letter","Two vowels together","Consonant blend"], answer:0},
     {q:"Which word has a long U sound?", options:["Cup","Cube","Cut","Cub"], answer:1}
   ]},
  {subject:"Math", title:"Numbers to 50", summary:"Ontario Grade 1 Number strand: students count, read, write, and represent whole numbers to 50, and describe their positions on a number line.",
   resourceLabel:"YouTube: Numbers to 50", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%20to%2050%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mKSNQuQrsm0",
   quiz:[
     {q:"What number comes after 39?", options:["38","41","40","37"], answer:2},
     {q:"Which is greater: 27 or 32?", options:["Equal","27","Cannot tell","32"], answer:3},
     {q:"What is 10 more than 24?", options:["34","25","44","14"], answer:0},
     {q:"Which number is between 15 and 20?", options:["17","14","21","25"], answer:0},
     {q:"Count by 1s: 45, 46, 47, ___", options:["50","48","44","49"], answer:1}
   ]},
  {subject:"Science", title:"Seasonal Changes: Fall", summary:"Ontario Grade 1 Earth and Space Systems strand: in fall, days shorten, leaves change colour and drop, and animals prepare for winter.",
   resourceLabel:"YouTube: Seasonal Changes: Fall", resourceUrl:"https://www.youtube.com/results?search_query=Seasonal%20Changes%3A%20Fall%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=AuHH6U4pufs",
   quiz:[
     {q:"In fall, leaves on deciduous trees ___.", options:["Stay green","Turn colour and fall off","Grow bigger","Turn white"], answer:1},
     {q:"Fall days are ___ than summer days.", options:["Hotter","Longer","The same length","Shorter"], answer:3},
     {q:"Which month is typically fall in Ontario?", options:["October","July","March","May"], answer:0},
     {q:"What do many animals do to prepare for winter?", options:["Turn red","Go swimming","Gather food or migrate","Grow wings"], answer:2},
     {q:"Fall comes after which season?", options:["Summer","Spring","Rainy season","Winter"], answer:0}
   ]},
  {subject:"SocialStudies", title:"My School Community", summary:"Ontario Grade 1 Social Studies strand: students identify school community members and their roles, and describe how everyone contributes.",
   resourceLabel:"YouTube: My School Community", resourceUrl:"https://www.youtube.com/results?search_query=My%20School%20Community%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zeM5ewySceQ",
   quiz:[
     {q:"Who is usually the leader of a whole school?", options:["A student","A librarian","The principal","A teacher"], answer:2},
     {q:"What is a teacher's main job?", options:["Fix the building","Cook lunch","Help students learn","Drive the bus"], answer:2},
     {q:"How can students help their school community?", options:["Being noisy","Ignoring rules","Picking up litter and helping others","Staying home"], answer:2},
     {q:"What does a librarian do?", options:["Cook lunch","Drive buses","Fix computers","Help students find books"], answer:3},
     {q:"Why do schools have rules?", options:["To punish students","To keep everyone safe and learning","Just because adults say so","To be unfair"], answer:1}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"Language", title:"Consonant Blends: bl, cl, fl, pl", summary:"Ontario Grade 1 Reading strand: consonant blends are two or more consonants together where each sound is heard, such as bl in black and cl in clap.",
   resourceLabel:"YouTube: Consonant Blends: bl, cl, fl, pl", resourceUrl:"https://www.youtube.com/results?search_query=Consonant%20Blends%3A%20bl%2C%20cl%2C%20fl%2C%20pl%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=QZ1Uu2MRXTY",
   quiz:[
     {q:"Which word starts with the BL blend?", options:["Floor","Play","Clock","Black"], answer:3},
     {q:"Which word starts with the CL blend?", options:["Floor","Plane","Blue","Clap"], answer:3},
     {q:"Which word starts with the FL blend?", options:["Clock","Flag","Blue","Play"], answer:1},
     {q:"Which word starts with the PL blend?", options:["Black","Clock","Floor","Plant"], answer:3},
     {q:"A consonant blend means ___.", options:["A single letter","Two consonants you hear separately","Silent letters","Only vowels"], answer:1}
   ]},
  {subject:"Math", title:"Addition to 10", summary:"Ontario Grade 1 Number strand: students add two one-digit numbers with sums to 10 using objects, drawings, and number lines.",
   resourceLabel:"YouTube: Addition to 10", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20to%2010%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=tVHOBVAFjUw",
   quiz:[
     {q:"3 + 4 = ?", options:["5","7","8","6"], answer:1},
     {q:"5 + 5 = ?", options:["8","9","11","10"], answer:3},
     {q:"2 + 6 = ?", options:["8","6","7","9"], answer:0},
     {q:"1 + 9 = ?", options:["8","11","9","10"], answer:3},
     {q:"4 + 3 = ?", options:["5","7","6","8"], answer:1}
   ]},
  {subject:"Science", title:"Materials: Solid, Liquid, Gas", summary:"Ontario Grade 1 Matter and Materials strand: students identify the three states of matter by exploring everyday examples of solids, liquids, and gases.",
   resourceLabel:"YouTube: Materials: Solid, Liquid, Gas", resourceUrl:"https://www.youtube.com/results?search_query=Materials%3A%20Solid%2C%20Liquid%2C%20Gas%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=MrTxRn9MNWM",
   quiz:[
     {q:"Which state of matter has a definite shape?", options:["Steam","Gas","Solid","Liquid"], answer:2},
     {q:"Water is an example of a ___.", options:["Gas","Solid","Rock","Liquid"], answer:3},
     {q:"Which state of matter fills its entire container?", options:["Liquid","Ice","Solid","Gas"], answer:3},
     {q:"Ice is water in a ___ state.", options:["Gas","Liquid","Hot","Solid"], answer:3},
     {q:"Steam is water in a ___ state.", options:["Solid","Cold","Liquid","Gas"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Maps and Directions", summary:"Ontario Grade 1 Social Studies strand B: students use directional language and simple maps to describe locations in familiar places.",
   resourceLabel:"YouTube: Maps and Directions", resourceUrl:"https://www.youtube.com/results?search_query=Maps%20and%20Directions%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mtsx8V3mE8o",
   quiz:[
     {q:"A map is a ___.", options:["Written story","Painting of nature","Drawing of a real place from above","Photo from space"], answer:2},
     {q:"If you face north, south is ___.", options:["To your right","Behind you","To your left","Above you"], answer:1},
     {q:"Which direction does the sun rise?", options:["West","East","South","North"], answer:1},
     {q:"On most maps, north is at the ___.", options:["Left","Top","Bottom","Right"], answer:1},
     {q:"What do we call a map of the whole world?", options:["A floor plan","A treasure map","A globe or world map","A street map"], answer:2}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"Language", title:"Sight Words", summary:"Ontario Grade 1 Reading strand: students recognize high-frequency Dolch sight words automatically, supporting reading fluency. Examples: the, and, a, to, said, is, you, in, was.",
   resourceLabel:"YouTube: Sight Words", resourceUrl:"https://www.youtube.com/results?search_query=Sight%20Words%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=U8t9Jg1r6G0",
   quiz:[
     {q:"Which of these is a common sight word?", options:["the","Elephant","umbrella","xylophone"], answer:0},
     {q:"Why do we practise sight words?", options:["They are hard to spell","We see them very often in reading","They are long words","They are nouns only"], answer:1},
     {q:"Which is spelled correctly?", options:["The","Tha","Thuh","Teh"], answer:0},
     {q:"Sight words help us ___.", options:["Read more quickly and fluently","Spell big words","Learn maths","Do science"], answer:0},
     {q:"Which is NOT a typical sight word?", options:["and","rhinoceros","is","the"], answer:1}
   ]},
  {subject:"Math", title:"Subtraction from 10", summary:"Ontario Grade 1 Number strand: students subtract one-digit numbers from numbers up to 10 using objects, drawings, and number lines.",
   resourceLabel:"YouTube: Subtraction from 10", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20from%2010%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=__JnyeG92Tg",
   quiz:[
     {q:"10 - 3 = ?", options:["7","6","5","8"], answer:0},
     {q:"8 - 4 = ?", options:["5","4","3","6"], answer:1},
     {q:"7 - 2 = ?", options:["6","5","3","4"], answer:1},
     {q:"9 - 5 = ?", options:["4","6","3","5"], answer:0},
     {q:"6 - 6 = ?", options:["1","2","3","0"], answer:3}
   ]},
  {subject:"Science", title:"Needs of Living Things", summary:"Ontario Grade 1 Life Systems strand: all living things need air, water, food, and shelter. Plants also need sunlight to make food through photosynthesis.",
   resourceLabel:"YouTube: Needs of Living Things", resourceUrl:"https://www.youtube.com/results?search_query=Needs%20of%20Living%20Things%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4p5e2l-zd5U",
   quiz:[
     {q:"Which is NOT a basic need of living things?", options:["Water","Television","Air","Food"], answer:1},
     {q:"Plants use sunlight to make their own ___.", options:["Food","Shelter","Soil","Water"], answer:0},
     {q:"Animals need shelter to ___.", options:["Be protected from weather and predators","Go to school","Find water","Play sports"], answer:0},
     {q:"What do living things need to breathe?", options:["Food","Air","Water","Sunlight"], answer:1},
     {q:"Which is a basic need ALL living things share?", options:["Money","Water","Transportation","Television"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Community Workers", summary:"Ontario Grade 1 Social Studies strand B: students identify community workers and explain how their work benefits everyone in the community.",
   resourceLabel:"YouTube: Community Workers", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Workers%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=wlBC2ljoGAk",
   quiz:[
     {q:"Who builds houses and buildings?", options:["A doctor","A chef","A teacher","A construction worker"], answer:3},
     {q:"What does a bus driver do?", options:["Carry passengers from place to place","Fix roads","Teach students","Cook food"], answer:0},
     {q:"Where does a chef work?", options:["A kitchen or restaurant","A hospital","A store","A school"], answer:0},
     {q:"Why do communities need workers with many different jobs?", options:["Only teachers are needed","Only doctors are needed","They do not","Each job meets a different need"], answer:3},
     {q:"Who repairs broken water pipes?", options:["A baker","A teacher","A plumber","A pilot"], answer:2}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"Language", title:"Word Families: -at and -an", summary:"Ontario Grade 1 Reading strand: word families share the same rime (ending pattern). The -at family includes cat, bat, hat, sat; the -an family includes can, man, ran, tan.",
   resourceLabel:"YouTube: Word Families: -at and -an", resourceUrl:"https://www.youtube.com/results?search_query=Word%20Families%3A%20-at%20and%20-an%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=uVeEAFy1z68",
   quiz:[
     {q:"Which word belongs to the -AT family?", options:["Run","Hat","Men","Can"], answer:1},
     {q:"Which word belongs to the -AN family?", options:["Can","Bat","Cat","Hat"], answer:0},
     {q:"How many words are in the -AT family: cat, bat, hat, sat?", options:["4","5","2","3"], answer:0},
     {q:"Which word rhymes with CAN?", options:["Cat","Bit","Ran","Hat"], answer:2},
     {q:"Word families help us ___.", options:["Do experiments","Count numbers","Spot spelling patterns","Draw pictures"], answer:2}
   ]},
  {subject:"Math", title:"Place Value: Tens and Ones", summary:"Ontario Grade 1 Number strand: students decompose two-digit numbers into tens and ones using base-ten blocks, understanding that the position of a digit determines its value.",
   resourceLabel:"YouTube: Place Value: Tens and Ones", resourceUrl:"https://www.youtube.com/results?search_query=Place%20Value%3A%20Tens%20and%20Ones%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=1F3AycEDksY",
   quiz:[
     {q:"In the number 23, the digit 2 means ___.", options:["20 tens","20 ones","2 ones","2 tens"], answer:3},
     {q:"How many tens are in 35?", options:["5","2","35","3"], answer:3},
     {q:"How many ones are in 47?", options:["11","4","47","7"], answer:3},
     {q:"What is 3 tens and 4 ones?", options:["34","30","4","43"], answer:0},
     {q:"In the number 16, the 6 means ___.", options:["6 tens","16 ones","6 ones","1 ten"], answer:2}
   ]},
  {subject:"Science", title:"Seasonal Changes: Winter", summary:"Ontario Grade 1 Earth and Space Systems strand: in winter, temperatures drop, many trees are bare, some animals hibernate, and people wear warm clothing.",
   resourceLabel:"YouTube: Seasonal Changes: Winter", resourceUrl:"https://www.youtube.com/results?search_query=Seasonal%20Changes%3A%20Winter%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=UQjT5uKp2hg",
   quiz:[
     {q:"What season comes after fall?", options:["Spring","Winter","Summer","Rainy season"], answer:1},
     {q:"In winter, many deciduous trees ___.", options:["Grow taller","Turn green","Grow new leaves","Have bare branches"], answer:3},
     {q:"What do bears do in winter?", options:["Fly south","Hibernate","Swim in rivers","Grow bigger"], answer:1},
     {q:"In Ontario, winter weather is usually ___.", options:["Always sunny","Cold with snow and ice","Warm and rainy","Hot and dry"], answer:1},
     {q:"Days in winter are ___ than in summer.", options:["The same","Always sunny","Longer","Shorter"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Rules and Responsibilities", summary:"Ontario Grade 1 Social Studies strand A: students describe their rights and responsibilities at home, at school, and in the community.",
   resourceLabel:"YouTube: Rules and Responsibilities", resourceUrl:"https://www.youtube.com/results?search_query=Rules%20and%20Responsibilities%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=5dtuZkposkk",
   quiz:[
     {q:"Why do schools have rules?", options:["Rules are not needed","To be unfair","To keep everyone safe and learning","To punish students"], answer:2},
     {q:"A responsibility is something you ___.", options:["Only adults do","Can always skip","Are allowed to ignore","Must do for yourself or others"], answer:3},
     {q:"Which is a student responsibility at school?", options:["Completing work and respecting others","Playing all day","Ignoring homework","Talking over the teacher"], answer:0},
     {q:"Rights and responsibilities work together because ___.", options:["Only responsibilities matter","Rights need responsibilities to work","Only rights matter","They are the same thing"], answer:1},
     {q:"Which is an example of a right?", options:["Being treated fairly and kept safe","Having no rules","Working all day","Ignoring others"], answer:0}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"Language", title:"Writing Complete Sentences", summary:"Ontario Grade 1 Writing strand: a complete sentence has a subject and a verb, begins with a capital letter, and ends with a punctuation mark.",
   resourceLabel:"YouTube: Writing Complete Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Writing%20Complete%20Sentences%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=DuubQG3gFb8",
   quiz:[
     {q:"Every sentence must start with a ___.", options:["Number","Capital letter","lowercase letter","Period"], answer:1},
     {q:"Which is a complete sentence?", options:["Fast dog.","The dog runs fast.","Runs fast.","the dog"], answer:1},
     {q:"A sentence that asks a question ends with a ___.", options:["Question mark","Period","Comma","Exclamation mark"], answer:0},
     {q:"Which sentence has correct punctuation?", options:["The cat is big.","the cat is big","the cat is big.","The cat is big"], answer:0},
     {q:"A sentence needs a subject (who) and a ___ (action).", options:["Verb","Noun","Adjective","Punctuation mark"], answer:0}
   ]},
  {subject:"Math", title:"Skip Counting by 2s", summary:"Ontario Grade 1 Number strand: students skip count by 2s from 0, landing on even numbers: 0, 2, 4, 6, 8, 10...",
   resourceLabel:"YouTube: Skip Counting by 2s", resourceUrl:"https://www.youtube.com/results?search_query=Skip%20Counting%20by%202s%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=GvTcpfSnOMQ",
   quiz:[
     {q:"Skip count by 2s: 2, 4, 6, ___", options:["9","8","5","7"], answer:1},
     {q:"Skip count by 2s: 10, 12, 14, ___", options:["17","16","15","13"], answer:1},
     {q:"Which numbers do you land on when skip counting by 2s?", options:["Even numbers","Random numbers","All numbers","Odd numbers"], answer:0},
     {q:"Skip count by 2s from 0: 0, 2, 4, 6, 8, ___", options:["12","9","11","10"], answer:3},
     {q:"Skip counting by 2s helps us count ___ faster.", options:["Odd numbers","Pairs or groups of 2","By tens","By fives"], answer:1}
   ]},
  {subject:"Science", title:"Animals and Their Young", summary:"Ontario Grade 1 Life Systems strand: animals reproduce and care for their young; baby animals resemble their parents and grow to look like them.",
   resourceLabel:"YouTube: Animals and Their Young", resourceUrl:"https://www.youtube.com/results?search_query=Animals%20and%20Their%20Young%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=s37MDCK2bpM",
   quiz:[
     {q:"A baby dog is called a ___.", options:["Kitten","Calf","Puppy","Foal"], answer:2},
     {q:"A baby cat is called a ___.", options:["Puppy","Kitten","Lamb","Cub"], answer:1},
     {q:"Baby animals grow up to look like their ___.", options:["Owners","Friends","Teachers","Parents"], answer:3},
     {q:"Why do parent animals care for their young?", options:["For fun","Because they are paid","To keep them safe until they can survive","They do not care"], answer:2},
     {q:"Which baby animal hatches from an egg?", options:["Duckling","Kitten","Lamb","Puppy"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Our Province: Ontario", summary:"Ontario Grade 1 Social Studies strand B: students identify Ontario on a map of Canada, name its capital city, and describe some key features.",
   resourceLabel:"YouTube: Our Province: Ontario", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Province%3A%20Ontario%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=M4r5Zf0yf9s",
   quiz:[
     {q:"What is the capital city of Ontario?", options:["Toronto","Montreal","Vancouver","Ottawa"], answer:0},
     {q:"Ontario is located in ___.", options:["Far west Canada","East-central Canada","The far east","Far north"], answer:1},
     {q:"What large bodies of water border southern Ontario?", options:["The Arctic Ocean","The Pacific Ocean","The Great Lakes","The Atlantic Ocean"], answer:2},
     {q:"Ontario's provincial flower is the ___.", options:["Trillium","Rose","Sunflower","Tulip"], answer:0},
     {q:"Which city is the largest in Ontario?", options:["Toronto","Hamilton","Ottawa","London"], answer:0}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"Language", title:"Question Words: Who, What, Where, When, Why", summary:"Ontario Grade 1 Reading and Writing strands: students identify and use the five W question words to gather information from texts and to formulate questions.",
   resourceLabel:"YouTube: Question Words: Who, What, Where, When, Why", resourceUrl:"https://www.youtube.com/results?search_query=Question%20Words%3A%20Who%2C%20What%2C%20Where%2C%20When%2C%20Why%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PUyOzCZ9XJE",
   quiz:[
     {q:"Which question word asks about a person?", options:["Who","What","When","Where"], answer:0},
     {q:"Which question word asks about a place?", options:["When","Who","Where","What"], answer:2},
     {q:"Which question word asks about a time?", options:["Why","Where","When","Who"], answer:2},
     {q:"Which question word asks for a reason?", options:["Why","Where","Who","What"], answer:0},
     {q:"What question word asks about an object or event?", options:["When","Who","What","Where"], answer:2}
   ]},
  {subject:"Math", title:"Skip Counting by 5s", summary:"Ontario Grade 1 Number strand: students skip count by 5s from 0, recognising the pattern: 0, 5, 10, 15, 20...",
   resourceLabel:"YouTube: Skip Counting by 5s", resourceUrl:"https://www.youtube.com/results?search_query=Skip%20Counting%20by%205s%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=RNr2pjm2x9k",
   quiz:[
     {q:"Skip count by 5s: 5, 10, 15, ___", options:["18","19","17","20"], answer:3},
     {q:"Skip count by 5s: 20, 25, 30, ___", options:["35","32","33","38"], answer:0},
     {q:"How many 5s make 25?", options:["5","4","3","6"], answer:0},
     {q:"Skip counting by 5s is like counting ___.", options:["By tens","By fives","By twos","By ones"], answer:1},
     {q:"5, 10, 15, 20 — what comes next?", options:["30","22","25","21"], answer:2}
   ]},
  {subject:"Science", title:"Parts of a Plant", summary:"Ontario Grade 1 Life Systems strand: students identify and describe the functions of the main parts of a plant: roots, stem, leaves, and flower.",
   resourceLabel:"YouTube: Parts of a Plant", resourceUrl:"https://www.youtube.com/results?search_query=Parts%20of%20a%20Plant%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=yTzSIXUU_ds",
   quiz:[
     {q:"Which part of a plant is usually underground?", options:["Stem","Leaves","Roots","Flower"], answer:2},
     {q:"What do roots do?", options:["Anchor the plant and absorb water","Make food from sunlight","Attract bees","Make flowers"], answer:0},
     {q:"Which part carries water from the roots upward?", options:["Leaf","Stem","Flower","Seed"], answer:1},
     {q:"Leaves make food for the plant using ___.", options:["Heat and wind","Rain and soil only","Sunlight, water, and air","Roots and flowers"], answer:2},
     {q:"What does the flower help the plant make?", options:["Stems","Seeds","More leaves","Bigger roots"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Canadian Symbols", summary:"Ontario Grade 1 Social Studies strand B: students identify major Canadian symbols including the maple leaf, beaver, flag, and national anthem.",
   resourceLabel:"YouTube: Canadian Symbols", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Symbols%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=38BGXJ572Y8",
   quiz:[
     {q:"What animal is a symbol of Canada?", options:["Eagle","Beaver","Bear","Moose"], answer:1},
     {q:"What is the main symbol on the Canadian flag?", options:["A maple leaf","A bear","A sun","A star"], answer:0},
     {q:"What are the two official colours of the Canadian flag?", options:["Green and gold","Red and blue","Blue and white","Red and white"], answer:3},
     {q:"What is Canada's national anthem?", options:["The Maple Leaf Forever","O Canada","God Save the King","True North"], answer:1},
     {q:"The maple leaf represents ___.", options:["The United States","The beaver","Canada","The queen"], answer:2}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"Language", title:"Punctuation: Period, Question Mark, Exclamation Mark", summary:"Ontario Grade 1 Writing strand: students use end punctuation correctly — period for statements, question mark for questions, and exclamation mark for strong emotion.",
   resourceLabel:"YouTube: Punctuation: Period, Question Mark, Exclamation Mark", resourceUrl:"https://www.youtube.com/results?search_query=Punctuation%3A%20Period%2C%20Question%20Mark%2C%20Exclamation%20Mark%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=LdCOswMeXFQ",
   quiz:[
     {q:"Which punctuation ends a statement?", options:[".","!","?","..."], answer:0},
     {q:"Which punctuation ends a question?", options:[".","?",",","!"], answer:1},
     {q:"Which punctuation shows excitement or strong feeling?", options:[".",",","!","?"], answer:2},
     {q:"The cat is big ___.", options:[".","...","?","!"], answer:0},
     {q:"Is the cat big ___?", options:[",","?","!","."], answer:1}
   ]},
  {subject:"Math", title:"Skip Counting by 10s", summary:"Ontario Grade 1 Number strand: students skip count by 10s from 0, recognising the pattern: 0, 10, 20, 30, 40, 50.",
   resourceLabel:"YouTube: Skip Counting by 10s", resourceUrl:"https://www.youtube.com/results?search_query=Skip%20Counting%20by%2010s%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ftati8iGQcs",
   quiz:[
     {q:"Skip count by 10s: 10, 20, 30, ___", options:["50","40","45","35"], answer:1},
     {q:"Skip count by 10s: 50, 60, 70, ___", options:["85","90","75","80"], answer:3},
     {q:"How many 10s make 40?", options:["4","5","2","3"], answer:0},
     {q:"10, 20, 30, 40 — what comes next?", options:["60","50","41","42"], answer:1},
     {q:"Skip counting by 10s is the same as counting ___.", options:["groups of 2","by fives","by ones","groups of 10"], answer:3}
   ]},
  {subject:"Science", title:"Seeds and How Plants Grow", summary:"Ontario Grade 1 Life Systems strand: students investigate how seeds germinate and grow into plants when given water, warmth, air, and light.",
   resourceLabel:"YouTube: Seeds and How Plants Grow", resourceUrl:"https://www.youtube.com/results?search_query=Seeds%20and%20How%20Plants%20Grow%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ro8Z9qIlWjM",
   quiz:[
     {q:"What do seeds need to germinate (sprout)?", options:["Only sunlight","Ice and darkness","Only soil","Water, warmth, and air"], answer:3},
     {q:"What is germination?", options:["When flowers bloom","When a seed starts to grow into a plant","When a plant dies","When leaves fall off"], answer:1},
     {q:"Where do seeds come from?", options:["The sky","Water","Flowers and fruit of plants","Rocks"], answer:2},
     {q:"As a seed grows it first produces a ___.", options:["Tiny shoot and root","Flower","Large tree","Fruit"], answer:0},
     {q:"Which is the correct order: seed, ___, plant?", options:["Flower","Leaf","Seedling","Root only"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Indigenous Peoples of Canada", summary:"Ontario Grade 1 Social Studies strand A: students learn that Indigenous peoples were the first peoples of Canada and have rich cultures, languages, and traditions.",
   resourceLabel:"YouTube: Indigenous Peoples of Canada", resourceUrl:"https://www.youtube.com/results?search_query=Indigenous%20Peoples%20of%20Canada%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=CISeEFTsgDA",
   quiz:[
     {q:"Who were the first peoples of Canada?", options:["American visitors","Recent immigrants","European settlers","Indigenous peoples"], answer:3},
     {q:"Indigenous peoples have lived in Canada for ___.", options:["Thousands of years","About 200 years","A few years","50 years"], answer:0},
     {q:"Indigenous peoples have their own ___.", options:["Languages and traditions","Nothing special","European customs only","Modern technology only"], answer:0},
     {q:"We should respect Indigenous cultures because ___.", options:["They are strangers","They shape Canada's history","It does not matter","They are far away"], answer:1},
     {q:"What do we call the different groups of First Nations peoples?", options:["Nations, each with their own culture","American groups","European groups","All the same group"], answer:0}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"Language", title:"Retelling a Story", summary:"Ontario Grade 1 Reading strand: students retell stories in sequence using the language of beginning, middle, and end, and story elements: characters, setting, problem, solution.",
   resourceLabel:"YouTube: Retelling a Story", resourceUrl:"https://www.youtube.com/results?search_query=Retelling%20a%20Story%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=JNemQATWt2E",
   quiz:[
     {q:"The beginning of a story tells us ___.", options:["A lesson only","The solution","Who the characters are and the setting","How it ends"], answer:2},
     {q:"The middle of a story contains the ___.", options:["Problem or challenge","Title","Introduction of characters only","Happy ending"], answer:0},
     {q:"The end of a story shows the ___.", options:["New characters","First event","Beginning again","Solution to the problem"], answer:3},
     {q:"Characters are ___.", options:["The ending","The people or animals in the story","The problem only","The place where the story happens"], answer:1},
     {q:"Setting means ___.", options:["The solution","The character's name","The problem","Where and when the story takes place"], answer:3}
   ]},
  {subject:"Math", title:"2D Shapes", summary:"Ontario Grade 1 Geometry strand: students identify and describe properties of 2D shapes: circle, square, rectangle, and triangle.",
   resourceLabel:"YouTube: 2D Shapes", resourceUrl:"https://www.youtube.com/results?search_query=2D%20Shapes%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ux_kLd7qAcY",
   quiz:[
     {q:"How many sides does a triangle have?", options:["4","3","2","5"], answer:1},
     {q:"How many corners does a square have?", options:["4","3","6","5"], answer:0},
     {q:"Which 2D shape has no corners?", options:["Circle","Rectangle","Triangle","Square"], answer:0},
     {q:"How many sides does a rectangle have?", options:["6","3","4","5"], answer:2},
     {q:"Which shape has four equal sides?", options:["Triangle","Circle","Square","Rectangle"], answer:2}
   ]},
  {subject:"Science", title:"Pushes and Pulls", summary:"Ontario Grade 1 Science Physical Education strand: a force is a push or pull that can move, stop, or change the direction of an object.",
   resourceLabel:"YouTube: Pushes and Pulls", resourceUrl:"https://www.youtube.com/results?search_query=Pushes%20and%20Pulls%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zI-vmLrBQzU",
   quiz:[
     {q:"A push moves an object ___.", options:["Toward you","Up only","Away from you","Down only"], answer:2},
     {q:"A pull moves an object ___.", options:["To the side only","Toward you","Upward","Away from you"], answer:1},
     {q:"Which is an example of a push?", options:["Reeling in a fish","Pulling a cart","Kicking a ball","Opening a drawer"], answer:2},
     {q:"Forces can change the ___ of a moving object.", options:["Colour","Smell","Speed or direction","Temperature"], answer:2},
     {q:"Which is an example of a pull?", options:["Throwing a ball","Pushing a door open","Kicking a ball","Opening a drawer"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Families Around the World", summary:"Ontario Grade 1 Social Studies strand A: students learn that families around the world share common needs but meet them in different ways through their cultures.",
   resourceLabel:"YouTube: Families Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Families%20Around%20the%20World%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ItVdo8DMLOA",
   quiz:[
     {q:"Families around the world all need ___.", options:["Food, shelter, and love","The same food","The same clothing","Electricity"], answer:0},
     {q:"Different families may speak ___.", options:["Only English","Only French","The same language always","Many different languages"], answer:3},
     {q:"Learning about other cultures helps us ___.", options:["Copy everyone","Understand and respect each other","Stay separate","Ignore differences"], answer:1},
     {q:"All families celebrate ___.", options:["Important events in their own way","Nothing","Only Christmas","The same holidays"], answer:0},
     {q:"What do all families around the world have in common?", options:["They all have the same rules","They live the same way","They look the same","Members care for each other"], answer:3}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"Language", title:"Main Idea", summary:"Ontario Grade 1 Reading strand: the main idea is what a text is mostly about. Supporting details give more information about the main idea.",
   resourceLabel:"YouTube: Main Idea", resourceUrl:"https://www.youtube.com/results?search_query=Main%20Idea%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=xJGQIYU_xhs",
   quiz:[
     {q:"The main idea of a text is ___.", options:["A small detail","A character's name","What the text is mostly about","The last sentence"], answer:2},
     {q:"Supporting details ___.", options:["Are the most important idea","Are not connected to the main idea","Are always at the beginning","Explain the main idea with examples"], answer:3},
     {q:"A good title for a text about dogs would be ___.", options:["My Birthday","The Red Ball","Cats are Great","All About Dogs"], answer:3},
     {q:"How do you find the main idea?", options:["Count the words","Read only the last sentence","Ask what the text is mostly about","Look at the pictures only"], answer:2},
     {q:"Which sentence is a main idea?", options:["Dogs make wonderful pets.","The dog ran fast.","The dog has brown spots.","My dog is named Rex."], answer:0}
   ]},
  {subject:"Math", title:"3D Shapes", summary:"Ontario Grade 1 Geometry strand: students identify and describe 3D figures: sphere, cube, cylinder, and cone, relating them to everyday objects.",
   resourceLabel:"YouTube: 3D Shapes", resourceUrl:"https://www.youtube.com/results?search_query=3D%20Shapes%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=REjfX9cDavw",
   quiz:[
     {q:"Which 3D shape looks like a ball?", options:["Cylinder","Cube","Cone","Sphere"], answer:3},
     {q:"Which 3D shape looks like a box?", options:["Cube","Cone","Sphere","Cylinder"], answer:0},
     {q:"Which 3D shape looks like a soup can?", options:["Cone","Cylinder","Sphere","Cube"], answer:1},
     {q:"A cone has ___ flat face(s).", options:["1","2","0","3"], answer:0},
     {q:"A cube has how many faces?", options:["5","8","6","4"], answer:2}
   ]},
  {subject:"Science", title:"Sound and Hearing", summary:"Ontario Grade 1 Science strand: sounds are made by vibrations. The ear detects sound waves, and sounds can be loud or soft, high-pitched or low-pitched.",
   resourceLabel:"YouTube: Sound and Hearing", resourceUrl:"https://www.youtube.com/results?search_query=Sound%20and%20Hearing%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pcWiWjxhKE8",
   quiz:[
     {q:"Sounds are made by ___.", options:["Light","Vibrations","Heat","Gravity"], answer:1},
     {q:"Which body part do we use to hear?", options:["Hands","Nose","Ears","Eyes"], answer:2},
     {q:"A loud sound has ___ vibrations than a soft sound.", options:["Smaller","Fewer","Slower","Larger or stronger"], answer:3},
     {q:"Which makes a high-pitched sound?", options:["A cow","A whistle","A tuba","A bass drum"], answer:1},
     {q:"Covering your ears reduces sound because ___.", options:["Vibrations increase","Sound stops completely","Your hearing improves","Less sound reaches your eardrums"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Being a Good Citizen", summary:"Ontario Grade 1 Social Studies strand A: students describe what it means to be a responsible and caring member of their school and community.",
   resourceLabel:"YouTube: Being a Good Citizen", resourceUrl:"https://www.youtube.com/results?search_query=Being%20a%20Good%20Citizen%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=jqweYnRRs1Q",
   quiz:[
     {q:"A good citizen ___.", options:["Helps others and follows rules","Litters","Is always noisy","Takes others' things"], answer:0},
     {q:"What does it mean to be responsible?", options:["Being unkind","Taking care of your duties","Ignoring others","Doing whatever you want"], answer:1},
     {q:"Why is it important to be kind to others?", options:["It is only for adults","It is not important","Only teachers need to be kind","It makes the community happy and safe"], answer:3},
     {q:"Being a good citizen at school means ___.", options:["Pushing in line","Talking during lessons","Sharing, listening, and helping others","Breaking rules"], answer:2},
     {q:"Good citizens follow rules because ___.", options:["Only some people follow rules","Teachers created them","Rules are boring","Rules keep everyone safe and happy"], answer:3}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"Language", title:"Characters and Setting", summary:"Ontario Grade 1 Reading strand: characters are the people or animals in a story; setting is where and when the story takes place.",
   resourceLabel:"YouTube: Characters and Setting", resourceUrl:"https://www.youtube.com/results?search_query=Characters%20and%20Setting%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=alQDawFP3sA",
   quiz:[
     {q:"Characters are ___.", options:["The place of the story","The people or animals in the story","The ending","The problem"], answer:1},
     {q:"Setting means ___.", options:["What happens in the story","Where and when the story takes place","Who is in the story","The solution"], answer:1},
     {q:"Which question helps identify the setting?", options:["What is the problem?","How does it end?","Who is in the story?","Where and when does the story happen?"], answer:3},
     {q:"A character's traits describe ___.", options:["What the character is like","Where the story happens","The problem","The solution"], answer:0},
     {q:"Can a story have more than one character?", options:["No, only one character","Only in long stories","Yes, stories can have many characters","Only in fairy tales"], answer:2}
   ]},
  {subject:"Math", title:"Measuring Length", summary:"Ontario Grade 1 Measurement strand: students measure length using non-standard units (paperclips, cubes) and compare objects using longer, shorter, taller.",
   resourceLabel:"YouTube: Measuring Length", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Length%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2wUsdsae0ro",
   quiz:[
     {q:"Which unit is NOT a standard unit of measurement?", options:["Centimetre","Paperclip","Kilometre","Metre"], answer:1},
     {q:"If a pencil is 8 cubes long and a crayon is 5 cubes long, which is longer?", options:["Cannot tell","Pencil","Crayon","Equal"], answer:1},
     {q:"Taller means ___.", options:["Heavier","Shorter in height","Greater in height","The same height"], answer:2},
     {q:"We measure length to find out ___.", options:["How many there are","How long or tall something is","What colour it is","How heavy something is"], answer:1},
     {q:"Which tool measures length in centimetres?", options:["Clock","Ruler","Thermometer","Scale"], answer:1}
   ]},
  {subject:"Science", title:"Light", summary:"Ontario Grade 1 Science strand: light travels in a straight line, can reflect off surfaces, and allows us to see. The sun is the main natural source of light on Earth.",
   resourceLabel:"YouTube: Light", resourceUrl:"https://www.youtube.com/results?search_query=Light%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=kkwgPwBKyl4",
   quiz:[
     {q:"What is the main natural source of light on Earth?", options:["Stars","The sun","A lamp","The moon"], answer:1},
     {q:"Light travels in a ___.", options:["Circle","Zigzag","Straight line","Curve"], answer:2},
     {q:"Which of these is a source of light?", options:["A light bulb","A book","A chair","A rock"], answer:0},
     {q:"When light hits a mirror it ___.", options:["Is absorbed","Turns to heat","Disappears","Bounces back (reflects)"], answer:3},
     {q:"We need light to ___.", options:["Hear sounds","See objects","Smell things","Taste food"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Rights of Children", summary:"Ontario Grade 1 Social Studies strand A: students identify children's rights as outlined by the United Nations Convention on the Rights of the Child (UNCRC).",
   resourceLabel:"YouTube: Rights of Children", resourceUrl:"https://www.youtube.com/results?search_query=Rights%20of%20Children%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=TyP09S0UEzA",
   quiz:[
     {q:"Children have the right to ___.", options:["Ignore school rules","Do whatever they want","Be safe, cared for, and educated","Have no responsibilities"], answer:2},
     {q:"What is the UNCRC?", options:["A school subject","A type of book","A UN document on children's rights","A type of toy"], answer:2},
     {q:"Which of these is a child's right?", options:["Working full-time jobs","Ignoring adults","Having no rules","Education and protection from harm"], answer:3},
     {q:"Rights and responsibilities go together because ___.", options:["They are opposite","Only rights matter","Rights need responsibilities too","Only adults have rights"], answer:2},
     {q:"Who is responsible for protecting children's rights?", options:["No one","Children themselves","Only schools","Governments, communities, and families"], answer:3}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"Language", title:"Making Predictions", summary:"Ontario Grade 1 Reading strand: students use text clues, pictures, and prior knowledge to predict what will happen next in a story or text.",
   resourceLabel:"YouTube: Making Predictions", resourceUrl:"https://www.youtube.com/results?search_query=Making%20Predictions%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PCtWPYF3y2U",
   quiz:[
     {q:"Making a prediction means ___.", options:["Guessing what happens next","Counting words","Reading the end first","Looking at pictures only"], answer:0},
     {q:"What clues help you make a prediction?", options:["The font size","Random guessing","Only the last page","Title, pictures, and what you've read"], answer:3},
     {q:"If dark clouds appear in a story, you might predict ___.", options:["The story is ending","It will get hotter","It will rain or storm","A character will laugh"], answer:2},
     {q:"After making a prediction, a good reader ___.", options:["Changes the story","Stops reading","Ignores whether it was right","Reads on to check the prediction"], answer:3},
     {q:"Predictions can be ___.", options:["Always wrong","Sometimes right, sometimes wrong","Only for science","Always correct"], answer:1}
   ]},
  {subject:"Math", title:"Measuring Mass", summary:"Ontario Grade 1 Measurement strand: students compare the mass of objects using non-standard units and a balance scale, using language like heavier and lighter.",
   resourceLabel:"YouTube: Measuring Mass", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Mass%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ybEU-6U7s8k",
   quiz:[
     {q:"Which object is likely heavier: a book or a feather?", options:["Feather","Book","They are equal","Cannot tell"], answer:1},
     {q:"A balance scale tips toward ___.", options:["The heavier object","Neither side","The centre","The lighter object"], answer:0},
     {q:"Mass measures ___.", options:["How hot something is","How heavy something is","How tall something is","How long something is"], answer:1},
     {q:"Which unit is used to measure mass in science?", options:["Litres","Centimetres","Kilograms or grams","Degrees"], answer:2},
     {q:"If one side of a balance is heavier, the other side ___.", options:["Goes up","Stays level","Goes down","Disappears"], answer:0}
   ]},
  {subject:"Science", title:"Magnetism", summary:"Ontario Grade 1 Science strand: magnets attract certain metals (iron, steel, nickel). They have north and south poles; like poles repel, opposite poles attract.",
   resourceLabel:"YouTube: Magnetism", resourceUrl:"https://www.youtube.com/results?search_query=Magnetism%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=HpI0VKjOdVc",
   quiz:[
     {q:"What does a magnet attract?", options:["Plastic","Wood","Certain metals like iron and steel","All metals"], answer:2},
     {q:"A magnet has two ___.", options:["Colours","Sizes","Faces","Poles (north and south)"], answer:3},
     {q:"When two north poles of magnets face each other they ___.", options:["Do nothing","Attract","Repel (push apart)","Stick together"], answer:2},
     {q:"Which of these would a magnet pick up?", options:["A paper clip","A wooden block","An eraser","A plastic cup"], answer:0},
     {q:"Opposite poles of a magnet ___.", options:["Do nothing","Break apart","Repel each other","Attract each other"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Community Helpers", summary:"Ontario Grade 1 Social Studies strand B: students describe the roles of community helpers including firefighters, police, medical workers, and educators.",
   resourceLabel:"YouTube: Community Helpers", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Helpers%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=wlBC2ljoGAk",
   quiz:[
     {q:"Who helps put out fires?", options:["A doctor","A teacher","A firefighter","A librarian"], answer:2},
     {q:"Who keeps the neighbourhood safe?", options:["A baker","A librarian","A police officer","A dentist"], answer:2},
     {q:"Who helps us when we are sick?", options:["A doctor or nurse","A police officer","A firefighter","A teacher"], answer:0},
     {q:"What do all community helpers have in common?", options:["They all drive trucks","They all wear red","They all work at schools","They help people in the community"], answer:3},
     {q:"How can you show respect to community helpers?", options:["Ignore them","Avoid them","Thank them and follow their instructions","Argue with them"], answer:2}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"Language", title:"Cause and Effect", summary:"Ontario Grade 1 Reading strand: cause is why something happens; effect is what happens as a result. Signal words include because, so, and as a result.",
   resourceLabel:"YouTube: Cause and Effect", resourceUrl:"https://www.youtube.com/results?search_query=Cause%20and%20Effect%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ZUyEerOK1gw",
   quiz:[
     {q:"The cause is ___.", options:["Who does it","When it happens","What happens","Why something happens"], answer:3},
     {q:"The effect is ___.", options:["Where it happens","What happens as a result","Who does it","Why something happens"], answer:1},
     {q:"Which signal word often introduces a cause?", options:["Finally","Because","Then","Next"], answer:1},
     {q:"It rained, so the grass got wet. What is the effect?", options:["The grass got wet","The sun came out","The rain fell hard","It rained"], answer:0},
     {q:"She studied hard, so she did well on the test. What is the cause?", options:["She studied hard","The test was easy","She did well on the test","The teacher helped"], answer:0}
   ]},
  {subject:"Math", title:"Fractions: Halves", summary:"Ontario Grade 1 Number strand: students divide shapes and sets into two equal parts, using the language of halves and one-half.",
   resourceLabel:"YouTube: Fractions: Halves", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%3A%20Halves%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=362JVVvgYPE",
   quiz:[
     {q:"A half means dividing something into ___ equal parts.", options:["1","3","2","4"], answer:2},
     {q:"Which shows a half of a circle?", options:["2 equal semicircles","A whole circle","1 quarter","3/4 of a circle"], answer:0},
     {q:"If you cut a sandwich into halves, how many pieces do you have?", options:["2","3","1","4"], answer:0},
     {q:"One-half is written as ___.", options:["1/4","1/3","2/1","1/2"], answer:3},
     {q:"If you eat one half of a pizza, what fraction is left?", options:["1/3","2/3","1/4","1/2"], answer:3}
   ]},
  {subject:"Science", title:"Weather Patterns", summary:"Ontario Grade 1 Earth and Space Systems strand: students observe and record daily weather conditions including temperature, precipitation, and cloud cover, identifying patterns over time.",
   resourceLabel:"YouTube: Weather Patterns", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20Patterns%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=oPq42NB2aTA",
   quiz:[
     {q:"Which tool measures air temperature?", options:["Scale","Ruler","Thermometer","Clock"], answer:2},
     {q:"What type of precipitation falls as solid flakes?", options:["Hail","Rain","Snow","Sleet"], answer:2},
     {q:"Cloudy weather means ___.", options:["It is raining heavily","No clouds in the sky","The sky is covered with clouds","The sun is very bright"], answer:2},
     {q:"Weather patterns help us ___.", options:["Plan clothing and activities","Pick favourite colours","Watch television","Choose what to eat"], answer:0},
     {q:"What instrument measures rainfall?", options:["Wind vane","Barometer","Rain gauge","Thermometer"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Land and Water in Canada", summary:"Ontario Grade 1 Social Studies strand B: students identify landforms and bodies of water in Canada including lakes, rivers, mountains, and plains.",
   resourceLabel:"YouTube: Land and Water in Canada", resourceUrl:"https://www.youtube.com/results?search_query=Land%20and%20Water%20in%20Canada%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Qo7aTFHyhPE",
   quiz:[
     {q:"Which of these is a body of water?", options:["Prairie","Forest","Lake Superior","Mountain"], answer:2},
     {q:"Which is a landform?", options:["Atlantic Ocean","Lake Ontario","Rocky Mountain","St. Lawrence River"], answer:2},
     {q:"What are the Great Lakes?", options:["Mountains in western Canada","Glaciers in the north","Five large lakes in Canada and the US","Prairies in central Canada"], answer:2},
     {q:"Canada has ___ coastlines.", options:["Only in the south","Three — east, west, and north","One — the east","No coastline"], answer:1},
     {q:"The Canadian Shield is ___.", options:["A vast region of ancient rock","A great river","A mountain range","A large ocean"], answer:0}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"Language", title:"Describing Words: Adjectives", summary:"Ontario Grade 1 Writing strand: adjectives are describing words that tell us more about a noun — they describe colour, size, shape, number, and feeling.",
   resourceLabel:"YouTube: Describing Words: Adjectives", resourceUrl:"https://www.youtube.com/results?search_query=Describing%20Words%3A%20Adjectives%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=-NqnQJjDmB0",
   quiz:[
     {q:"An adjective is a ___.", options:["Connecting word","Naming word","Action word","Describing word"], answer:3},
     {q:"Which word is an adjective in: The big dog ran?", options:["Ran","The","Dog","Big"], answer:3},
     {q:"Which word is an adjective?", options:["Happy","Run","Dog","Jump"], answer:0},
     {q:"Which sentence has an adjective?", options:["The dog ran.","The tiny cat sat.","She ran fast.","He jumped."], answer:1},
     {q:"Adjectives help us ___.", options:["Name things","Show actions","Connect sentences","Describe things more clearly"], answer:3}
   ]},
  {subject:"Math", title:"Data: Tally Charts", summary:"Ontario Grade 1 Data strand: students collect and organise data using tally marks, where each mark represents one item and a bundle of five is shown with a diagonal line.",
   resourceLabel:"YouTube: Data: Tally Charts", resourceUrl:"https://www.youtube.com/results?search_query=Data%3A%20Tally%20Charts%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zF_dBk8EPDk",
   quiz:[
     {q:"One tally mark represents ___.", options:["10 items","1 item","2 items","5 items"], answer:1},
     {q:"A group of 5 tally marks looks like ___.", options:["IIIII","IIII","Four vertical lines","Four lines crossed by one diagonal line"], answer:3},
     {q:"If you have 7 tally marks, you have ___ items.", options:["6","5","8","7"], answer:3},
     {q:"Why do we use tally marks?", options:["To spell words","For decoration","To draw pictures","To count and record data quickly"], answer:3},
     {q:"IIII I (5 marks) represents how many?", options:["6","7","5","4"], answer:2}
   ]},
  {subject:"Science", title:"The Sun", summary:"Ontario Grade 1 Earth and Space Systems strand: the Sun is a star, the centre of our solar system, and Earth's main source of heat and light. It causes day and night through Earth's rotation.",
   resourceLabel:"YouTube: The Sun", resourceUrl:"https://www.youtube.com/results?search_query=The%20Sun%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=sePqPIXMsAc",
   quiz:[
     {q:"The Sun is a ___.", options:["Comet","Planet","Star","Moon"], answer:2},
     {q:"The Sun gives Earth heat and ___.", options:["Snow","Wind","Light","Rain"], answer:2},
     {q:"Day and night are caused by Earth ___.", options:["Moving around the Sun","Moving away from the Sun","The Moon blocking the Sun","Rotating (spinning) on its axis"], answer:3},
     {q:"The Sun rises in the ___ and sets in the ___.", options:["North, south","East, west","West, east","South, north"], answer:1},
     {q:"Why is the Sun important for life on Earth?", options:["It is not important","Only plants need it","It provides heat and light for life","Only humans need it"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canada's Natural Resources", summary:"Ontario Grade 1 Social Studies strand B: students identify natural resources in Canada such as trees, water, minerals, and farmland and explain why they are important.",
   resourceLabel:"YouTube: Canada's Natural Resources", resourceUrl:"https://www.youtube.com/results?search_query=Canada%27s%20Natural%20Resources%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ajk-pvm5vfQ",
   quiz:[
     {q:"A natural resource is ___.", options:["Something from nature that people use","A building","Something people make in a factory","A type of money"], answer:0},
     {q:"Which of these is a natural resource?", options:["Fresh water","A car","A computer","A plastic bottle"], answer:0},
     {q:"Why are Canada's forests a natural resource?", options:["They are very tall","They look nice","They are cold","They provide wood and habitat"], answer:3},
     {q:"Which natural resource do farmers use to grow food?", options:["Rocks","Metal","Plastic","Farmland and soil"], answer:3},
     {q:"Why is it important to protect natural resources?", options:["Only adults care about this","So future generations can also use them","It is not important","Resources never run out"], answer:1}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"Language", title:"Action Words: Verbs", summary:"Ontario Grade 1 Writing strand: verbs are action words that tell what a subject does. Every complete sentence needs a verb.",
   resourceLabel:"YouTube: Action Words: Verbs", resourceUrl:"https://www.youtube.com/results?search_query=Action%20Words%3A%20Verbs%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ZYPjmjff0Zo",
   quiz:[
     {q:"A verb is a ___.", options:["Naming word","Connecting word","Action word","Describing word"], answer:2},
     {q:"Which word is a verb: The cat runs fast?", options:["Runs","Cat","Fast","The"], answer:0},
     {q:"Which word is a verb?", options:["Big","Jump","Dog","Happy"], answer:1},
     {q:"Every complete sentence needs a ___.", options:["Noun only","Verb","Question mark","Adjective"], answer:1},
     {q:"Which sentence uses a verb correctly?", options:["The big dog.","The dog happy.","The dog runs.","Dog the runs."], answer:2}
   ]},
  {subject:"Math", title:"Data: Pictographs", summary:"Ontario Grade 1 Data strand: a pictograph uses pictures or symbols to represent data. A key shows what each symbol means.",
   resourceLabel:"YouTube: Data: Pictographs", resourceUrl:"https://www.youtube.com/results?search_query=Data%3A%20Pictographs%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zF_dBk8EPDk",
   quiz:[
     {q:"In a pictograph, each picture represents ___.", options:["A colour","A number or amount shown in the key","A word","A shape"], answer:1},
     {q:"What is the purpose of a key in a pictograph?", options:["To make it pretty","To list all students","To explain what each symbol means","To show the title"], answer:2},
     {q:"If each star = 2 votes and there are 3 stars, how many votes are there?", options:["5","2","6","3"], answer:2},
     {q:"A pictograph makes data easier to ___.", options:["Collect","Hide","Understand and compare","Ignore"], answer:2},
     {q:"Which type of data is best shown in a pictograph?", options:["The alphabet","A story","How to add numbers","Favourite colours of students in a class"], answer:3}
   ]},
  {subject:"Science", title:"Soil and Earth Materials", summary:"Ontario Grade 1 Earth and Space Systems strand: soil is made of rock particles, organic matter, air, and water. Different soils have different properties.",
   resourceLabel:"YouTube: Soil and Earth Materials", resourceUrl:"https://www.youtube.com/results?search_query=Soil%20and%20Earth%20Materials%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=6e53-Z2gZzY",
   quiz:[
     {q:"Soil is made of small pieces of ___ and organic matter.", options:["Wood","Plastic","Rock","Metal"], answer:2},
     {q:"Why is soil important for plants?", options:["Soil holds roots and gives nutrients","Soil provides sunlight","Soil provides rain","It is not"], answer:0},
     {q:"Which type of soil holds the most water?", options:["Clay soil","Sandy soil","Rocky soil","Gravelly soil"], answer:0},
     {q:"Earthworms help soil by ___.", options:["Mixing and aerating the soil","Removing water","Destroying roots","Making soil harder"], answer:0},
     {q:"What is humus?", options:["A type of rock","A type of sand","A food dip","Decayed matter that enriches soil"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Multiculturalism in Canada", summary:"Ontario Grade 1 Social Studies strand A: Canada is a multicultural country where people from many backgrounds live and contribute, enriching Canadian society.",
   resourceLabel:"YouTube: Multiculturalism in Canada", resourceUrl:"https://www.youtube.com/results?search_query=Multiculturalism%20in%20Canada%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=rKgoVDV6UiE",
   quiz:[
     {q:"Canada is described as multicultural because ___.", options:["People from many different cultures live here","Everyone speaks the same language","Everyone follows the same traditions","Only Canadian-born people live here"], answer:0},
     {q:"How does multiculturalism make Canada stronger?", options:["It causes problems","It brings different ideas and foods","Only big cities benefit","It does not affect Canada"], answer:1},
     {q:"Which of Canada's two official languages reflects its multicultural roots?", options:["French and Italian","French and English","Spanish and English","English and Chinese"], answer:1},
     {q:"How can we celebrate multiculturalism at school?", options:["Avoid different foods","Speak only one language","Learn about and share traditions","Ignore other cultures"], answer:2},
     {q:"What does it mean to respect another culture?", options:["Avoiding them","Copying everything they do","Valuing and respecting their traditions","Ignoring their customs"], answer:2}
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"Language", title:"Nouns: People, Places, Things", summary:"Ontario Grade 1 Writing strand: a noun names a person, place, or thing. Proper nouns name specific people, places, or things and begin with a capital letter.",
   resourceLabel:"YouTube: Nouns: People, Places, Things", resourceUrl:"https://www.youtube.com/results?search_query=Nouns%3A%20People%2C%20Places%2C%20Things%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=3K5vg_QsKCc",
   quiz:[
     {q:"A noun is a ___.", options:["Naming word","Connecting word","Action word","Describing word"], answer:0},
     {q:"Which word is a noun: The dog runs fast?", options:["The","Dog","Fast","Runs"], answer:1},
     {q:"Which is a proper noun?", options:["dog","city","Canada","house"], answer:2},
     {q:"Proper nouns always start with a ___.", options:["Number","lowercase letter","Capital letter","Period"], answer:2},
     {q:"Which of these is a common noun?", options:["school","Maria","Toronto","Canada"], answer:0}
   ]},
  {subject:"Math", title:"Addition to 20", summary:"Ontario Grade 1 Number strand: students add two numbers with sums up to 20 using strategies such as counting on, making tens, and using doubles.",
   resourceLabel:"YouTube: Addition to 20", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20to%2020%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=VScM8Z8Jls0",
   quiz:[
     {q:"7 + 6 = ?", options:["14","12","13","11"], answer:2},
     {q:"9 + 9 = ?", options:["18","17","19","16"], answer:0},
     {q:"5 + 8 = ?", options:["14","13","15","12"], answer:1},
     {q:"11 + 4 = ?", options:["13","15","16","14"], answer:1},
     {q:"6 + 7 = ?", options:["12","11","13","14"], answer:2}
   ]},
  {subject:"Science", title:"Food Chains", summary:"Ontario Grade 1 Life Systems strand: a food chain shows how energy passes from one living thing to another. It starts with a plant (producer), then a herbivore (consumer), then a carnivore.",
   resourceLabel:"YouTube: Food Chains", resourceUrl:"https://www.youtube.com/results?search_query=Food%20Chains%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=0DL4AUBe3WA",
   quiz:[
     {q:"In a food chain, plants are called ___.", options:["Consumers","Carnivores","Herbivores","Producers"], answer:3},
     {q:"An animal that eats only plants is called a ___.", options:["Producer","Herbivore","Carnivore","Omnivore"], answer:1},
     {q:"In a food chain, arrows show ___.", options:["Friendship","Where animals live","The seasons","The direction energy flows"], answer:3},
     {q:"Which is a correct simple food chain?", options:["Sun eats grass eats fox","Fox eats grass eats rabbit","Fox eats sun eats rabbit","Grass, then rabbit, then fox"], answer:3},
     {q:"A carnivore is an animal that eats ___.", options:["Only plants","Both plants and animals","Only animals","Only grass"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Global Communities", summary:"Ontario Grade 1 Social Studies strand B: students compare communities around the world, identifying similarities and differences in how people meet their basic needs.",
   resourceLabel:"YouTube: Global Communities", resourceUrl:"https://www.youtube.com/results?search_query=Global%20Communities%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=-84U1EsZCbY",
   quiz:[
     {q:"Communities around the world are ___.", options:["Only similar","All different with nothing in common","Exactly the same","Different in some, similar in others"], answer:3},
     {q:"What basic need do all communities around the world share?", options:["Food, shelter, and water","Electricity","The same language","The same food"], answer:0},
     {q:"How do people in different communities get food?", options:["Everyone buys at supermarkets","Everyone hunts","Everyone grows rice","In many different ways"], answer:3},
     {q:"What is one way communities around the world are similar?", options:["People care for each other","Same sports","Same language","Same food"], answer:0},
     {q:"Learning about global communities helps us ___.", options:["Avoid other countries","Ignore other cultures","Think only our way is right","Understand that we are all connected"], answer:3}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"Language", title:"Pronouns", summary:"Ontario Grade 1 Writing strand: pronouns take the place of nouns. Examples: I, you, he, she, it, we, they.",
   resourceLabel:"YouTube: Pronouns", resourceUrl:"https://www.youtube.com/results?search_query=Pronouns%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=OP9-kOCSqY8",
   quiz:[
     {q:"A pronoun takes the place of a ___.", options:["Noun","Adverb","Adjective","Verb"], answer:0},
     {q:"What pronoun replaces 'Maria'?", options:["It","They","He","She"], answer:3},
     {q:"What pronoun replaces 'the boys'?", options:["It","She","He","They"], answer:3},
     {q:"What pronoun replaces 'the dog'?", options:["She","It","He","They"], answer:1},
     {q:"Which sentence uses a pronoun correctly?", options:["She runs fast.","Running fast.","Maria she runs fast.","Dog runs fast."], answer:0}
   ]},
  {subject:"Math", title:"Subtraction from 20", summary:"Ontario Grade 1 Number strand: students subtract single-digit numbers from teens numbers and find differences within 20 using various strategies.",
   resourceLabel:"YouTube: Subtraction from 20", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20from%2020%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=gbb2W-rrYik",
   quiz:[
     {q:"15 - 7 = ?", options:["9","6","7","8"], answer:3},
     {q:"20 - 9 = ?", options:["11","10","12","9"], answer:0},
     {q:"18 - 6 = ?", options:["13","11","10","12"], answer:3},
     {q:"14 - 8 = ?", options:["4","6","5","7"], answer:1},
     {q:"17 - 9 = ?", options:["7","6","9","8"], answer:3}
   ]},
  {subject:"Science", title:"Animal Habitats", summary:"Ontario Grade 1 Life Systems strand: a habitat is the natural environment where an animal lives, providing food, water, shelter, and space.",
   resourceLabel:"YouTube: Animal Habitats", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Habitats%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Xj1ASC-TlsI",
   quiz:[
     {q:"A habitat provides animals with food, water, shelter, and ___.", options:["Television","Toys","Space","Money"], answer:2},
     {q:"Which habitat does a polar bear live in?", options:["Desert","Jungle","Arctic tundra","Rainforest"], answer:2},
     {q:"Which animal lives in a pond habitat?", options:["Polar bear","Camel","Frog","Penguin"], answer:2},
     {q:"A desert habitat is ___.", options:["Always covered in snow","Hot and dry with little rainfall","Always rainy","Cold and wet"], answer:1},
     {q:"What happens to an animal if its habitat is destroyed?", options:["Nothing changes","It becomes stronger","It gets bigger","It may struggle or need a new habitat"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Helping Others in the Community", summary:"Ontario Grade 1 Social Studies strand A: students explore ways they can contribute to their community through volunteering, kindness, and helping neighbours.",
   resourceLabel:"YouTube: Helping Others in the Community", resourceUrl:"https://www.youtube.com/results?search_query=Helping%20Others%20in%20the%20Community%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=9Wzqrp4iMrg",
   quiz:[
     {q:"How can you help your community?", options:["Taking things","Volunteering and being kind to others","Ignoring others","Littering"], answer:1},
     {q:"Why is volunteering important?", options:["It is not","Only adults volunteer","It helps others and the community","It earns money"], answer:2},
     {q:"What is a way kids can help the environment?", options:["Wasting food","Buying more toys","Using more electricity","Picking up litter and recycling"], answer:3},
     {q:"Being kind to a new student at school helps them ___.", options:["Stay silent","Feel welcome and included","Ignore others","Feel uncomfortable"], answer:1},
     {q:"Why do communities need volunteers?", options:["Volunteers help everyone","Volunteering is boring","Only hospitals need volunteers","They do not"], answer:0}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"Language", title:"Compound Words", summary:"Ontario Grade 1 Reading strand: a compound word is made of two smaller words joined together to make a new word, such as sunshine, raincoat, and backpack.",
   resourceLabel:"YouTube: Compound Words", resourceUrl:"https://www.youtube.com/results?search_query=Compound%20Words%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=82G-ZWzUHhU",
   quiz:[
     {q:"A compound word is ___.", options:["Two small words joined together","A very long word","A word with a silent letter","A nonsense word"], answer:0},
     {q:"Which is a compound word?", options:["Sunshine","Beautiful","Elephant","Apple"], answer:0},
     {q:"What two words make 'raincoat'?", options:["Rainc + oat","R + aincoat","Rain + coat","Rai + ncoat"], answer:2},
     {q:"What compound word means a bag worn on your back?", options:["Schoolbag","Handbag","Backpack","Purse"], answer:2},
     {q:"Which of these is a compound word?", options:["Quickly","Strangely","Running","Starfish"], answer:3}
   ]},
  {subject:"Math", title:"Ordinal Numbers", summary:"Ontario Grade 1 Number strand: ordinal numbers describe position in a sequence: first (1st), second (2nd), third (3rd), and so on.",
   resourceLabel:"YouTube: Ordinal Numbers", resourceUrl:"https://www.youtube.com/results?search_query=Ordinal%20Numbers%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=BaO1E21SpkI",
   quiz:[
     {q:"What is the ordinal form of 1?", options:["First","Onest","Oneish","1nd"], answer:0},
     {q:"What is the ordinal form of 3?", options:["Thirdly","Threest","Third","Threeth"], answer:2},
     {q:"If you are 4th in line, how many people are ahead of you?", options:["3","4","2","5"], answer:0},
     {q:"What comes after fifth?", options:["Seveth","Fiftth","Fourthly","Sixth"], answer:3},
     {q:"The ordinal number '2nd' means ___.", options:["Secondly","Second","Twoth","Twoeth"], answer:1}
   ]},
  {subject:"Science", title:"Plants and the Environment", summary:"Ontario Grade 1 Life Systems strand: plants are producers that provide food and oxygen for other living things; they also prevent soil erosion and provide habitats.",
   resourceLabel:"YouTube: Plants and the Environment", resourceUrl:"https://www.youtube.com/results?search_query=Plants%20and%20the%20Environment%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=yTzSIXUU_ds",
   quiz:[
     {q:"Plants produce oxygen through a process called ___.", options:["Hibernation","Digestion","Respiration","Photosynthesis"], answer:3},
     {q:"Why are plants important for animals?", options:["They provide money","They provide food and oxygen for animals","They are not","They provide electricity"], answer:1},
     {q:"What holds soil in place and prevents erosion?", options:["Rain","Plant roots","Wind","Rocks alone"], answer:1},
     {q:"Which of these would NOT survive without plants?", options:["Clouds","Rivers","Rocks","Most animals"], answer:3},
     {q:"How do plants help improve air quality?", options:["They absorb oxygen","They absorb CO2, release oxygen","They do not","They create pollution"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Celebrations and Traditions", summary:"Ontario Grade 1 Social Studies strand A: students explore different cultural celebrations and traditions, recognising the diversity of practices and their importance to families.",
   resourceLabel:"YouTube: Celebrations and Traditions", resourceUrl:"https://www.youtube.com/results?search_query=Celebrations%20and%20Traditions%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=BYA4k3eB7OQ",
   quiz:[
     {q:"A tradition is ___.", options:["An activity repeated over time","Only for children","Something done only once","Always about food"], answer:0},
     {q:"Why do families celebrate traditions?", options:["To mark events and strengthen bonds","It is boring","To spend money","They have to"], answer:0},
     {q:"Which is an example of a tradition?", options:["Watching TV","Going to sleep","Brushing your teeth","An annual family holiday gathering"], answer:3},
     {q:"How are celebrations different around the world?", options:["They are all the same","Only the date changes","Only adults celebrate","They vary in customs and meanings"], answer:3},
     {q:"Learning about others' celebrations helps us ___.", options:["Understand cultural diversity","Copy everything","Stay separate","Ignore differences"], answer:0}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"Language", title:"Synonyms", summary:"Ontario Grade 1 Writing strand: synonyms are words that have the same or similar meanings. Using synonyms makes writing more interesting.",
   resourceLabel:"YouTube: Synonyms", resourceUrl:"https://www.youtube.com/results?search_query=Synonyms%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=N394RCO1F6k",
   quiz:[
     {q:"A synonym is a word that means the ___.", options:["Nothing at all","Same or similar thing","Bigger thing","Opposite"], answer:1},
     {q:"Which is a synonym for big?", options:["Tiny","Little","Small","Large"], answer:3},
     {q:"Which is a synonym for happy?", options:["Sad","Joyful","Angry","Tired"], answer:1},
     {q:"Which is a synonym for fast?", options:["Quick","Soft","Slow","Quiet"], answer:0},
     {q:"Using synonyms in writing makes it ___.", options:["Shorter","More interesting and varied","More boring","More confusing"], answer:1}
   ]},
  {subject:"Math", title:"Money: Coins", summary:"Ontario Grade 1 Number strand: students identify Canadian coins (penny, nickel, dime, quarter) and their values, and count small collections of coins.",
   resourceLabel:"YouTube: Money: Coins", resourceUrl:"https://www.youtube.com/results?search_query=Money%3A%20Coins%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pnXJGNo08v0",
   quiz:[
     {q:"How much is a nickel worth?", options:["1 cent","10 cents","25 cents","5 cents"], answer:3},
     {q:"How much is a dime worth?", options:["5 cents","1 cent","25 cents","10 cents"], answer:3},
     {q:"How much is a quarter worth?", options:["1 cent","25 cents","10 cents","5 cents"], answer:1},
     {q:"Which coin is worth the most?", options:["Quarter","Nickel","Penny","Dime"], answer:0},
     {q:"How many nickels make a dime?", options:["2","4","1","3"], answer:0}
   ]},
  {subject:"Science", title:"Energy and Movement", summary:"Ontario Grade 1 Science Physical Education strand: energy can cause objects to move. Stored energy (potential) and moving energy (kinetic) are two basic forms.",
   resourceLabel:"YouTube: Energy and Movement", resourceUrl:"https://www.youtube.com/results?search_query=Energy%20and%20Movement%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Q0LBegPWzrg",
   quiz:[
     {q:"What is energy?", options:["The ability to do work or cause change","A type of rock","A kind of animal","A colour"], answer:0},
     {q:"A ball sitting on a hill has ___ energy.", options:["No","Electrical","Potential (stored)","Kinetic (moving)"], answer:2},
     {q:"A ball rolling down a hill has ___ energy.", options:["Kinetic (moving)","Potential (stored)","No","Chemical"], answer:0},
     {q:"Which of these uses electrical energy?", options:["A light bulb","A wooden block","A leaf","A rock"], answer:0},
     {q:"What energy does the Sun give to Earth?", options:["Heat and light (solar energy)","Mechanical","Chemical","Nuclear"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Traditions from Around the World", summary:"Ontario Grade 1 Social Studies strand A: students explore cultural traditions from different countries, building respect and appreciation for diversity.",
   resourceLabel:"YouTube: Traditions from Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Traditions%20from%20Around%20the%20World%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=RwSYrsjTiW4",
   quiz:[
     {q:"Why do countries have their own traditions?", options:["Everyone chose the same ones","Rules forced them to","They have to","They reflect a culture's history"], answer:3},
     {q:"Which festival involves lanterns and is celebrated in China?", options:["Diwali","Hanukkah","Chinese Lantern Festival","Carnival"], answer:2},
     {q:"Diwali is celebrated by people of which background?", options:["European","Hindu (and others in South Asia)","Japanese","Chinese"], answer:1},
     {q:"Why is it important to learn about traditions from around the world?", options:["Only tourists need to know","It is not important","It is confusing","It promotes respect and understanding"], answer:3},
     {q:"Which of these is a Canadian tradition?", options:["Chinese New Year only","Canada Day fireworks","Cinco de Mayo","Diwali as celebrated in Canada"], answer:3}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"Language", title:"Antonyms", summary:"Ontario Grade 1 Writing strand: antonyms are words that have opposite meanings, such as hot/cold, happy/sad, and big/small.",
   resourceLabel:"YouTube: Antonyms", resourceUrl:"https://www.youtube.com/results?search_query=Antonyms%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Kq78ZHokUGw",
   quiz:[
     {q:"An antonym is a word that means the ___ of another word.", options:["Similar","Bigger","Same","Opposite"], answer:3},
     {q:"What is the antonym of BIG?", options:["Large","Small","Huge","Giant"], answer:1},
     {q:"What is the antonym of HOT?", options:["Warm","Frozen","Cold","Cool"], answer:2},
     {q:"What is the antonym of DAY?", options:["Afternoon","Morning","Night","Evening"], answer:2},
     {q:"Using antonyms helps us ___.", options:["Compare and contrast ideas","Make writing longer","Remove nouns","Confuse readers"], answer:0}
   ]},
  {subject:"Math", title:"Time: Reading Clocks", summary:"Ontario Grade 1 Measurement strand: students tell time to the hour and half hour on both analogue and digital clocks.",
   resourceLabel:"YouTube: Time: Reading Clocks", resourceUrl:"https://www.youtube.com/results?search_query=Time%3A%20Reading%20Clocks%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Bvq5YqyRoKU",
   quiz:[
     {q:"On a clock, the short hand points to the ___.", options:["Minutes","Seconds","Day","Hour"], answer:3},
     {q:"What time is shown when both hands point to 12?", options:["6:00","12:00","9:00","3:00"], answer:1},
     {q:"If the hour hand points to 3 and the minute hand to 12, the time is ___.", options:["12:03","3:30","3:00","12:30"], answer:2},
     {q:"Half past 4 means ___.", options:["4:05","4:00","4:15","4:30"], answer:3},
     {q:"How many hours are in one day?", options:["12","60","24","48"], answer:2}
   ]},
  {subject:"Science", title:"Simple Machines", summary:"Ontario Grade 1 Science strand: simple machines make work easier. Examples include lever, wheel and axle, pulley, inclined plane, wedge, and screw.",
   resourceLabel:"YouTube: Simple Machines", resourceUrl:"https://www.youtube.com/results?search_query=Simple%20Machines%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=LSfNYpCprw4",
   quiz:[
     {q:"A simple machine makes work ___.", options:["Harder","More confusing","Easier","Slower"], answer:3},
     {q:"A ramp is an example of an ___.", options:["Wheel and axle","Inclined plane","Pulley","Lever"], answer:1},
     {q:"A wheel and axle reduces ___.", options:["Speed","Height","Distance","The force needed to move things"], answer:3},
     {q:"Which simple machine is a seesaw an example of?", options:["Pulley","Wedge","Inclined plane","Lever"], answer:3},
     {q:"How many types of simple machines are there?", options:["3","4","5","6"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Canada Day and National Holidays", summary:"Ontario Grade 1 Social Studies strand B: students learn about Canada Day and other national holidays, understanding what they celebrate and why they are important.",
   resourceLabel:"YouTube: Canada Day and National Holidays", resourceUrl:"https://www.youtube.com/results?search_query=Canada%20Day%20and%20National%20Holidays%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Qo7aTFHyhPE",
   quiz:[
     {q:"Canada Day is celebrated on ___.", options:["July 1","November 11","July 4","October 1"], answer:0},
     {q:"What does Canada Day celebrate?", options:["Canada's birthday as a nation","Christmas","Thanksgiving","Halloween"], answer:0},
     {q:"Remembrance Day honours ___.", options:["Veterans who served in wars","Canadian scientists","Canadian athletes","The founding of Canada"], answer:0},
     {q:"What is the date of Remembrance Day?", options:["July 1","October 31","November 11","December 25"], answer:2},
     {q:"Victoria Day in Canada honours ___.", options:["Halloween","Summer solstice","Canada Day celebrations","The Queen's birthday and the monarchy"], answer:3}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"Language", title:"Prefixes: un- and re-", summary:"Ontario Grade 1 Reading strand: a prefix is added to the beginning of a word to change its meaning. Un- means not; re- means again.",
   resourceLabel:"YouTube: Prefixes: un- and re-", resourceUrl:"https://www.youtube.com/results?search_query=Prefixes%3A%20un-%20and%20re-%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=jX5VVlU2hVQ",
   quiz:[
     {q:"What does the prefix UN- mean?", options:["Not","Before","After","Again"], answer:0},
     {q:"What does UNKIND mean?", options:["Extremely kind","Not kind","Very kind","Kind again"], answer:1},
     {q:"What does the prefix RE- mean?", options:["After","Again","Not","Before"], answer:1},
     {q:"What does REREAD mean?", options:["Read again","Read before","Read after","Not read"], answer:0},
     {q:"Which word has a prefix?", options:["Unhappy","Jumped","Cats","Running"], answer:0}
   ]},
  {subject:"Math", title:"Number Patterns", summary:"Ontario Grade 1 Algebra and Patterning strand: students identify, describe, and extend number patterns involving addition or subtraction.",
   resourceLabel:"YouTube: Number Patterns", resourceUrl:"https://www.youtube.com/results?search_query=Number%20Patterns%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Tu4NRKtHxuM",
   quiz:[
     {q:"What comes next? 2, 4, 6, 8, ___", options:["9","10","11","12"], answer:1},
     {q:"What is the rule? 10, 20, 30, 40...", options:["Add 15","Add 5","Add 2","Add 10"], answer:3},
     {q:"What comes next? 1, 3, 5, 7, ___", options:["10","9","8","6"], answer:1},
     {q:"What is the rule? 20, 18, 16, 14...", options:["Add 2","Add 1","Subtract 3","Subtract 2"], answer:3},
     {q:"What comes next? 5, 10, 15, 20, ___", options:["30","22","21","25"], answer:3}
   ]},
  {subject:"Science", title:"Rocks and Their Properties", summary:"Ontario Grade 1 Earth and Space Systems strand: rocks can be described by colour, texture, hardness, and size. Different rocks have different properties and uses.",
   resourceLabel:"YouTube: Rocks and Their Properties", resourceUrl:"https://www.youtube.com/results?search_query=Rocks%20and%20Their%20Properties%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ty2Za-O9h6w",
   quiz:[
     {q:"Rocks can be described by ___.", options:["Their names only","Their feelings","Their families","Their colour, texture, and hardness"], answer:3},
     {q:"Which rock is used to make jewellery?", options:["Granite","Limestone","Sandstone","Diamond (a mineral)"], answer:3},
     {q:"What does the hardness of a rock tell us?", options:["Its colour","Its age","How easily it can be scratched","Its weight"], answer:2},
     {q:"Where can you find rocks?", options:["Only in rivers","On land, in water, underground","Only in mountains","Only underground"], answer:1},
     {q:"Which of these is made from a natural rock or mineral?", options:["Salt (a mineral)","Both b and c","Glass window (made from sand, a mineral)","Plastic cup"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Maps of Canada", summary:"Ontario Grade 1 Social Studies strand B: students read simple maps of Canada, identifying provinces, territories, capital cities, and geographic regions.",
   resourceLabel:"YouTube: Maps of Canada", resourceUrl:"https://www.youtube.com/results?search_query=Maps%20of%20Canada%20grade%201%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Q_VFQUZ9oo4",
   quiz:[
     {q:"How many provinces does Canada have?", options:["10","8","12","9"], answer:0},
     {q:"How many territories does Canada have?", options:["2","3","1","4"], answer:1},
     {q:"What is the capital city of Canada?", options:["Ottawa","Vancouver","Toronto","Montreal"], answer:0},
     {q:"Which province is on the far east coast of Canada?", options:["Alberta","Newfoundland and Labrador","Ontario","British Columbia"], answer:1},
     {q:"Which territory is in the far north of Canada?", options:["Quebec","Alberta","Nunavut","Ontario"], answer:2}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"Language", title:"Suffixes: -er and -ing", summary:"Ontario Grade 1 Reading strand: a suffix is added to the end of a word to change its meaning. -Er means one who does; -ing indicates an ongoing action.",
   resourceLabel:"YouTube: Suffixes: -er and -ing", resourceUrl:"https://www.youtube.com/results?search_query=Suffixes%3A%20-er%20and%20-ing%20grade%201%20educational",
   quiz:[
     {q:"What does the suffix -ER mean when added to a verb?", options:["One who does the action","The action itself","Having done the action","Doing the action now"], answer:0},
     {q:"What does TEACHER mean?", options:["Is teaching","To teach","One who teaches","Taught"], answer:2},
     {q:"What does RUNNING mean?", options:["One who runs","About to run","Ran once","Currently doing the action of running"], answer:3},
     {q:"Which word has a suffix?", options:["Of","The","Running","And"], answer:2},
     {q:"Adding -ING to a verb creates a ___.", options:["Noun","Present participle (ongoing action)","Adjective","Prefix"], answer:1}
   ]},
  {subject:"Math", title:"Addition Strategies", summary:"Ontario Grade 1 Number strand: students use mental math strategies such as doubles, near doubles, make ten, and counting on to add efficiently.",
   resourceLabel:"YouTube: Addition Strategies", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20Strategies%20grade%201%20educational",
   quiz:[
     {q:"Counting on means starting at the bigger number and ___.", options:["Counting from 1","Adding backwards","Counting forward the smaller number","Subtracting"], answer:2},
     {q:"6 + 6 = 12 is an example of a ___.", options:["Make ten","Counting on","Near double","Double"], answer:3},
     {q:"7 + 6: think 7 + 7 = 14, then subtract 1 = 13. This is a ___.", options:["Double","Near double strategy","Counting on","Make ten"], answer:1},
     {q:"Make 10: 8 + 5 = 8 + 2 + 3 = 10 + 3 = ___", options:["12","14","13","11"], answer:2},
     {q:"Which strategy works best for 9 + 4?", options:["Count from 1","Doubles","Subtraction","Make ten: 9+1+3=13"], answer:3}
   ]},
  {subject:"Science", title:"Water on Earth", summary:"Ontario Grade 1 Earth and Space Systems strand: water covers most of Earth's surface. It exists in three states and cycles through the environment.",
   resourceLabel:"YouTube: Water on Earth", resourceUrl:"https://www.youtube.com/results?search_query=Water%20on%20Earth%20grade%201%20educational",
   quiz:[
     {q:"What percentage of Earth's surface is covered by water?", options:["About 50 percent","About 90 percent","About 30 percent","About 70 percent"], answer:3},
     {q:"Water in three states: ___.", options:["Deep, shallow, wide","Hot, warm, cold","Solid, liquid, gas","Fast, slow, still"], answer:2},
     {q:"What is the water cycle?", options:["The cycle of evaporation and rain","How water is made in factories","How rain is collected in rivers","How we filter drinking water"], answer:0},
     {q:"Which state is water in when it forms clouds?", options:["Solid","Gas (water vapour)","Plasma","Liquid"], answer:1},
     {q:"Why is clean water important?", options:["It is not","All living things need clean water","Only fish need clean water","Only humans need water"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Provinces of Canada", summary:"Ontario Grade 1 Social Studies strand B: students identify the ten provinces of Canada and some facts about each, locating them on a map.",
   resourceLabel:"YouTube: Provinces of Canada", resourceUrl:"https://www.youtube.com/results?search_query=Provinces%20of%20Canada%20grade%201%20educational",
   quiz:[
     {q:"Which province is on the west coast of Canada?", options:["Manitoba","Ontario","Quebec","British Columbia"], answer:3},
     {q:"Which province is Canada's largest by area?", options:["British Columbia","Alberta","Quebec","Ontario"], answer:2},
     {q:"The Maritime provinces include New Brunswick, Nova Scotia, and ___.", options:["Ontario","Newfoundland","Quebec","Prince Edward Island"], answer:3},
     {q:"Which province is known for the Prairies (flat grasslands)?", options:["Quebec","British Columbia","Ontario","Saskatchewan"], answer:3},
     {q:"What is the capital city of Quebec?", options:["Ottawa","Toronto","Quebec City","Montreal"], answer:2}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"Language", title:"Poetry", summary:"Ontario Grade 1 Reading and Writing strands: students read and write simple poems, identifying rhyme, rhythm, and descriptive language, and appreciating how poets choose words carefully.",
   resourceLabel:"YouTube: Poetry", resourceUrl:"https://www.youtube.com/results?search_query=Poetry%20grade%201%20educational",
   quiz:[
     {q:"Poetry often uses ___.", options:["Only facts","Rhyme, rhythm, and descriptive language","Only long sentences","Lots of numbers"], answer:1},
     {q:"Which lines rhyme?", options:["The cat sat on the mat / The dog ran to school","She ran fast / He jumped high","Today is Monday / I ate my lunch","Roses are red / Violets are blue"], answer:3},
     {q:"Rhythm in a poem means ___.", options:["A regular beat or pattern in the words","The poem rhymes","The poem is long","The poem is happy"], answer:0},
     {q:"A poem is different from a story because ___.", options:["It is always longer","It has no characters","It uses line breaks and feelings","It has no words"], answer:2},
     {q:"Which is an example of descriptive language in a poem?", options:["He walked home","She went to the store","The shimmering silver moon glowed softly","It was night"], answer:2}
   ]},
  {subject:"Math", title:"Subtraction Strategies", summary:"Ontario Grade 1 Number strand: students use strategies such as counting back, fact families, and think-addition to subtract efficiently.",
   resourceLabel:"YouTube: Subtraction Strategies", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20Strategies%20grade%201%20educational",
   quiz:[
     {q:"Counting back: 12 - 3 means start at 12 and count back ___.", options:["1 step","12 steps","2 steps","3 steps"], answer:3},
     {q:"Think-addition: 13 - 5 = ? Think 5 + ___ = 13", options:["6","7","9","8"], answer:3},
     {q:"A fact family uses the same three numbers. 7+5=12, 5+7=12, 12-5=___, 12-7=5.", options:["6","5","4","7"], answer:3},
     {q:"Which is a subtraction strategy?", options:["Counting on from 1","Making a ten","Counting back from the bigger number","Skip counting by 5"], answer:2},
     {q:"14 - 6 = ?", options:["9","6","7","8"], answer:3}
   ]},
  {subject:"Science", title:"Stars and Space", summary:"Ontario Grade 1 Earth and Space Systems strand: the Sun is the closest star to Earth. Stars are large balls of hot gas. The Moon orbits Earth.",
   resourceLabel:"YouTube: Stars and Space", resourceUrl:"https://www.youtube.com/results?search_query=Stars%20and%20Space%20grade%201%20educational",
   quiz:[
     {q:"The Sun is a ___.", options:["Moon","Planet","Comet","Large ball of hot gas called a star"], answer:3},
     {q:"Which planet do we live on?", options:["Earth","Jupiter","Mars","Venus"], answer:0},
     {q:"The Moon ___.", options:["Is a star","Orbits (circles) the Earth","Makes its own light","Is bigger than Earth"], answer:1},
     {q:"Stars are visible mainly at ___.", options:["Night","Dusk only","Dawn","Noon"], answer:0},
     {q:"How does the Moon appear to change shape?", options:["It actually changes shape","It grows and shrinks","We see varying amounts of its lit side","Clouds cover it"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Caring for the Environment", summary:"Ontario Grade 1 Social Studies strand B: students identify ways to protect the environment including reducing waste, recycling, and conserving water and energy.",
   resourceLabel:"YouTube: Caring for the Environment", resourceUrl:"https://www.youtube.com/results?search_query=Caring%20for%20the%20Environment%20grade%201%20educational",
   quiz:[
     {q:"What does REDUCE mean in reduce, reuse, recycle?", options:["Use less of something","Throw away more","Make something bigger","Buy more"], answer:0},
     {q:"Which is an example of recycling?", options:["Wasting water","Buying new items","Turning a used newspaper into new paper","Throwing a bottle in the garbage"], answer:2},
     {q:"Why should we turn off lights when leaving a room?", options:["To save electrical energy","To make the room dark","Lights do not matter","Lights are too bright"], answer:0},
     {q:"What is one way to conserve water?", options:["Leave the tap running","Water your lawn every hour","Turn off the tap while brushing teeth","Take very long showers"], answer:2},
     {q:"Caring for the environment benefits ___.", options:["All living things, now and later","Only humans","Nobody","Only animals"], answer:0}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"Language", title:"Non-Fiction Text Features", summary:"Ontario Grade 1 Reading strand: non-fiction texts contain features like headings, photographs, captions, table of contents, and indexes that help readers find and understand information.",
   resourceLabel:"YouTube: Non-Fiction Text Features", resourceUrl:"https://www.youtube.com/results?search_query=Non-Fiction%20Text%20Features%20grade%201%20educational",
   quiz:[
     {q:"What is a heading in a non-fiction text?", options:["A picture at the top","A bold title for a section","A type of hat","The author's name"], answer:1},
     {q:"What is a caption?", options:["A title","Words explaining a photo","A type of heading","The conclusion"], answer:1},
     {q:"What does a table of contents show?", options:["Only pictures","The author's biography","Definitions of words","Chapter/section titles and page numbers"], answer:3},
     {q:"How is a non-fiction text different from fiction?", options:["It has pictures","It has more chapters","Non-fiction is real; fiction is not","It is shorter"], answer:2},
     {q:"Which of these is a non-fiction book?", options:["Harry Potter","The Three Little Pigs","Charlotte's Web","Encyclopaedia of Animals"], answer:3}
   ]},
  {subject:"Math", title:"Review: Number Sense to 50", summary:"Ontario Grade 1 Number strand review: students count, compare, order, and represent numbers to 50, and demonstrate understanding of place value and operations.",
   resourceLabel:"YouTube: Review: Number Sense to 50", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Number%20Sense%20to%2050%20grade%201%20educational",
   quiz:[
     {q:"What is 3 tens and 7 ones?", options:["30","13","37","73"], answer:2},
     {q:"Which is greatest: 24, 42, or 34?", options:["34","24","44","42"], answer:3},
     {q:"15 + 7 = ?", options:["21","23","22","20"], answer:2},
     {q:"20 - 8 = ?", options:["13","12","11","14"], answer:1},
     {q:"Skip count by 5s: 25, 30, ___", options:["40","32","35","33"], answer:2}
   ]},
  {subject:"Science", title:"Seasons Review", summary:"Ontario Grade 1 Earth and Space Systems strand review: students review the four seasons, their characteristics, and how plants, animals, and people respond to seasonal changes.",
   resourceLabel:"YouTube: Seasons Review", resourceUrl:"https://www.youtube.com/results?search_query=Seasons%20Review%20grade%201%20educational",
   quiz:[
     {q:"What are the four seasons in order starting with spring?", options:["Spring, Summer, Fall, Winter","Fall, Winter, Spring, Summer","Summer, Fall, Winter, Spring","Winter, Spring, Summer, Fall"], answer:0},
     {q:"In which season do most plants grow flowers?", options:["No season","Fall","Spring and Summer","Winter"], answer:2},
     {q:"Which season has the longest days in Ontario?", options:["Winter","Fall","Spring","Summer"], answer:3},
     {q:"What do deciduous trees do in fall?", options:["Stay the same","Lose their leaves","Grow new leaves","Grow taller only"], answer:1},
     {q:"In Ontario, which season has the coldest temperatures?", options:["Spring","Summer","Fall","Winter"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Rights Review", summary:"Ontario Grade 1 Social Studies strand A review: students review children's rights, responsibilities, and what it means to be a responsible citizen in the school and community.",
   resourceLabel:"YouTube: Rights Review", resourceUrl:"https://www.youtube.com/results?search_query=Rights%20Review%20grade%201%20educational",
   quiz:[
     {q:"What are the three main rights of all children?", options:["Education, safety, and being cared for","Work, play, travel","Adults choose their rights","Money, toys, vacations"], answer:0},
     {q:"What is a responsibility?", options:["Something we are paid for","Something we can always skip","Something we're expected to do","Something only adults have"], answer:2},
     {q:"Name one way to be a responsible student.", options:["Talking in class","Being noisy","Helping others and doing your work","Ignoring instructions"], answer:2},
     {q:"Responsible citizens ___.", options:["Do whatever they want","Follow rules and help others","Only follow rules they like","Never follow rules"], answer:1},
     {q:"Why do rights and responsibilities go together?", options:["Only adults need to think about this","They do not","Rights are more important","Rights mean responsibility to others"], answer:3}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"Language", title:"Creative Writing", summary:"Ontario Grade 1 Writing strand: students write short creative stories with a beginning, middle, and end, using descriptive language, interesting characters, and a simple plot.",
   resourceLabel:"YouTube: Creative Writing", resourceUrl:"https://www.youtube.com/results?search_query=Creative%20Writing%20grade%201%20educational",
   quiz:[
     {q:"Creative writing lets you ___.", options:["Copy other stories","Write only your name","Write only facts","Create imaginary stories and characters"], answer:3},
     {q:"A good creative story has a ___.", options:["Middle only","Only a problem","Beginning only","Beginning, middle, and end"], answer:3},
     {q:"What makes a story more interesting?", options:["Descriptive language and characters","Very short sentences only","Numbers and lists","Just names and places"], answer:0},
     {q:"The problem in a story is ___.", options:["The ending","The setting","The beginning","The challenge the character must solve"], answer:3},
     {q:"A story's solution is ___.", options:["The setting","The problem","How the character solves the problem","The beginning"], answer:2}
   ]},
  {subject:"Math", title:"Review: Patterns and Shapes", summary:"Ontario Grade 1 Geometry and Patterning review: students identify and extend patterns, and describe properties of 2D and 3D shapes.",
   resourceLabel:"YouTube: Review: Patterns and Shapes", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Patterns%20and%20Shapes%20grade%201%20educational",
   quiz:[
     {q:"Which 2D shape has three sides?", options:["Rectangle","Square","Triangle","Circle"], answer:2},
     {q:"What comes next? Triangle, Square, Triangle, Square, ___", options:["Triangle","Rectangle","Square","Circle"], answer:0},
     {q:"A cube has how many faces?", options:["8","5","4","6"], answer:3},
     {q:"Which is a 3D shape?", options:["Sphere","Square","Triangle","Circle"], answer:0},
     {q:"What is the pattern rule? 5, 10, 15, 20...", options:["Add 5","Add 2","Add 3","Add 10"], answer:0}
   ]},
  {subject:"Science", title:"Life Cycles Review", summary:"Ontario Grade 1 Life Systems strand review: students review life cycles of different animals including butterfly, frog, and chicken, identifying the stages.",
   resourceLabel:"YouTube: Life Cycles Review", resourceUrl:"https://www.youtube.com/results?search_query=Life%20Cycles%20Review%20grade%201%20educational",
   quiz:[
     {q:"What are the four stages of a butterfly's life cycle?", options:["Baby, child, teen, adult","Egg, larva, pupa, adult","Seed, sprout, plant, flower","Egg, chick, chicken, adult"], answer:1},
     {q:"What is a tadpole?", options:["A baby bird","A baby frog","A type of fish","A baby butterfly"], answer:1},
     {q:"In the life cycle of a chicken: egg, chick, ___.", options:["Adult chicken","Larva","Pupa","Caterpillar"], answer:0},
     {q:"All life cycles ___.", options:["Are the same for all animals","Begin with an adult","Are continuous processes","End with a seed"], answer:2},
     {q:"What is metamorphosis?", options:["A kind of rock","A dramatic change in form during life","A season change","A type of habitat"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Community Review", summary:"Ontario Grade 1 Social Studies review: students review the concept of community, types of communities, community workers, and the importance of caring for the environment.",
   resourceLabel:"YouTube: Community Review", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Review%20grade%201%20educational",
   quiz:[
     {q:"What is a community?", options:["A type of map","A group living and working together","A natural resource","A building"], answer:1},
     {q:"Name two types of communities.", options:["Old and new","Urban and rural","Rich and poor","Big and small"], answer:1},
     {q:"Which community worker helps people get from place to place?", options:["A librarian","A teacher","A bus driver or train conductor","A doctor"], answer:2},
     {q:"Why should communities care for the environment?", options:["To keep nature healthy now and later","Only some communities do","It is not necessary","Only scientists care about this"], answer:0},
     {q:"What makes a community strong?", options:["Cooperation and helping each other","Only having the same culture","Only money","Lots of buildings"], answer:0}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"Language", title:"Story Structure Review", summary:"Ontario Grade 1 Reading and Writing strands review: students apply understanding of story structure (characters, setting, problem, solution) to read and write stories.",
   resourceLabel:"YouTube: Story Structure Review", resourceUrl:"https://www.youtube.com/results?search_query=Story%20Structure%20Review%20grade%201%20educational",
   quiz:[
     {q:"What are the five main story elements?", options:["Nouns, verbs, adjectives, adverbs, pronouns","Beginning, ending, middle, pictures, words","Characters, setting, problem, events, solution","Title, pages, words, pictures, cover"], answer:2},
     {q:"The setting tells us ___.", options:["The characters' feelings","Where and when the story takes place","The main problem","The lesson"], answer:1},
     {q:"The problem in a story creates ___.", options:["The characters","The happy ending","The setting","Conflict and suspense"], answer:2},
     {q:"Identifying story elements helps readers ___.", options:["Read faster","Count words","Understand and remember stories better","Skip pages"], answer:2},
     {q:"Which element is most important in a story?", options:["Pictures","Characters","Setting","All elements work together"], answer:3}
   ]},
  {subject:"Math", title:"Review: Addition and Subtraction", summary:"Ontario Grade 1 Number strand review: students apply addition and subtraction strategies to solve problems within 20.",
   resourceLabel:"YouTube: Review: Addition and Subtraction", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Addition%20and%20Subtraction%20grade%201%20educational",
   quiz:[
     {q:"14 + 5 = ?", options:["21","19","20","18"], answer:1},
     {q:"17 - 8 = ?", options:["10","9","7","8"], answer:1},
     {q:"A farmer has 12 chickens. 4 run away. How many are left?", options:["7","8","10","9"], answer:1},
     {q:"Sam has 6 apples and gets 7 more. How many total?", options:["12","15","13","14"], answer:2},
     {q:"20 - 11 = ?", options:["8","9","10","11"], answer:1}
   ]},
  {subject:"Science", title:"Animal Review", summary:"Ontario Grade 1 Life Systems strand review: students review key concepts about animals including needs, habitats, young, and adaptations.",
   resourceLabel:"YouTube: Animal Review", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Review%20grade%201%20educational",
   quiz:[
     {q:"What do all animals need to survive?", options:["Money","Only food","Food, water, air, and shelter","Television"], answer:2},
     {q:"An adaptation is ___.", options:["A feature that helps an animal survive","A life cycle stage","A kind of food","A type of habitat"], answer:0},
     {q:"Which animal is adapted to cold Arctic environments?", options:["Frog","Polar bear","Butterfly","Camel"], answer:1},
     {q:"What is a food chain?", options:["A habitat","A type of animal","Who eats whom in an ecosystem","A chain you can eat"], answer:2},
     {q:"Baby animals grow to look like their ___.", options:["Owners","Friends","Parents","Teachers"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Heritage Review", summary:"Ontario Grade 1 Social Studies strand A review: students review concepts of heritage, identity, family, traditions, and cultural celebrations.",
   resourceLabel:"YouTube: Heritage Review", resourceUrl:"https://www.youtube.com/results?search_query=Heritage%20Review%20grade%201%20educational",
   quiz:[
     {q:"Heritage includes ___.", options:["Only money","Traditions and culture passed down","Only food","Only buildings"], answer:1},
     {q:"How does learning about our heritage help us?", options:["It helps us understand who we are","It is boring","Only adults need to learn heritage","It does not"], answer:0},
     {q:"Which of these is part of a family's heritage?", options:["A new house","A recent movie","A family recipe passed down","A new toy"], answer:2},
     {q:"How do families pass on their heritage?", options:["By forgetting old traditions","Through stories and traditions","By never celebrating","By moving away"], answer:1},
     {q:"Why is Canada's multicultural heritage an asset?", options:["It brings diverse richness to Canada","It causes confusion","Only in big cities","It creates problems"], answer:0}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"Language", title:"Reading Fluency", summary:"Ontario Grade 1 Reading strand: reading fluency means reading smoothly, at an appropriate pace, with expression. Practice with familiar texts builds fluency.",
   resourceLabel:"YouTube: Reading Fluency", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20Fluency%20grade%201%20educational",
   quiz:[
     {q:"Reading fluency means ___.", options:["Reading only short books","Reading smoothly and with expression","Reading as fast as possible","Reading silently only"], answer:1},
     {q:"Which practice builds reading fluency?", options:["Only reading alone","Reading a new book every day only","Re-reading familiar texts and reading aloud","Only reading in your head"], answer:2},
     {q:"Expression in reading means ___.", options:["Changing your voice to match the mood","Only whispering","Reading in a monotone voice","Only shouting"], answer:0},
     {q:"A fluent reader ___.", options:["Reads every word slowly","Never re-reads","Pauses at commas and periods","Sounds out every letter individually"], answer:2},
     {q:"Why is reading fluency important?", options:["It lets you focus on meaning","It is not","Only speed matters","Only accuracy matters"], answer:0}
   ]},
  {subject:"Math", title:"Review: Measurement", summary:"Ontario Grade 1 Measurement strand review: students apply understanding of length, mass, capacity, and time to solve problems.",
   resourceLabel:"YouTube: Review: Measurement", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Measurement%20grade%201%20educational",
   quiz:[
     {q:"Which tool measures length?", options:["Clock","Thermometer","Ruler","Scale"], answer:2},
     {q:"Which measures how heavy something is?", options:["Ruler","Scale","Thermometer","Clock"], answer:1},
     {q:"Half past 7 means ___.", options:["7:15","7:05","7:30","7:50"], answer:2},
     {q:"If a pencil is 10 cubes long and a pen is 14 cubes long, which is shorter?", options:["Equal","Cannot tell","Pencil","Pen"], answer:2},
     {q:"What unit do we use to measure length in metric system?", options:["Centimetres","Pounds","Kilograms","Degrees"], answer:0}
   ]},
  {subject:"Science", title:"Plant Review", summary:"Ontario Grade 1 Life Systems and Earth strand review: students review plant parts, plant needs, life cycles, and the importance of plants to the environment.",
   resourceLabel:"YouTube: Plant Review", resourceUrl:"https://www.youtube.com/results?search_query=Plant%20Review%20grade%201%20educational",
   quiz:[
     {q:"Which part of a plant makes food?", options:["Root","Seed","Stem","Leaf (through photosynthesis)"], answer:3},
     {q:"What are the four things plants need to grow?", options:["Money, toys, television, games","Electricity, heat, noise, colour","Sunlight, water, air, and nutrients from soil","Books, pencils, chairs, desks"], answer:2},
     {q:"What does a plant seed need to germinate?", options:["Water, warmth, and air","Darkness only","Only soil","Only sunlight"], answer:0},
     {q:"A fruit contains ___.", options:["Roots","Only juice","Seeds that can grow into new plants","Stems"], answer:2},
     {q:"Why are plants important to the environment?", options:["Only for decoration","Only for food","They are not","They produce oxygen and provide food"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Culture Review", summary:"Ontario Grade 1 Social Studies strand A review: students review key vocabulary and concepts related to culture, including traditions, celebrations, language, and respect for diversity.",
   resourceLabel:"YouTube: Culture Review", resourceUrl:"https://www.youtube.com/results?search_query=Culture%20Review%20grade%201%20educational",
   quiz:[
     {q:"Culture includes ___.", options:["Language, traditions, and values","Only clothing","Only food","Only music"], answer:0},
     {q:"How do we show respect for different cultures?", options:["Ignoring them","Copying everything","Learning about them and being fair","Making fun of them"], answer:2},
     {q:"Why is cultural diversity an asset in Canada?", options:["It causes problems","It enriches society with new ideas","Only if everyone speaks the same language","Only in big cities"], answer:1},
     {q:"Which is the best way to learn about another culture?", options:["Ask questions and listen to learn","Watch one movie","Assume you know everything","Read one book and decide"], answer:0},
     {q:"Multiculturalism in Canada means ___.", options:["All cultures are respected and valued","French and English only","Only one culture is valued","Immigrants must forget their culture"], answer:0}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"Language", title:"Spelling Patterns: -ight, -ake, -ine", summary:"Ontario Grade 1 Reading strand: spelling patterns help students decode and spell new words. Word families like night, sight, light; cake, lake, make; mine, fine, pine share patterns.",
   resourceLabel:"YouTube: Spelling Patterns: -ight, -ake, -ine", resourceUrl:"https://www.youtube.com/results?search_query=Spelling%20Patterns%3A%20-ight%2C%20-ake%2C%20-ine%20grade%201%20educational",
   quiz:[
     {q:"Which word belongs to the -IGHT family?", options:["Cake","Lake","Mine","Night"], answer:3},
     {q:"Which word belongs to the -AKE family?", options:["Night","Right","Light","Cake"], answer:3},
     {q:"Which word belongs to the -INE family?", options:["Night","Lake","Sight","Fine"], answer:3},
     {q:"Which spelling pattern do BRIGHT and TIGHT share?", options:["ine","ake","ight","ite"], answer:2},
     {q:"Learning spelling patterns helps us ___.", options:["Draw letters only","Sound out every letter always","Read and spell related words","Only spell one word"], answer:2}
   ]},
  {subject:"Math", title:"Review: Data and Probability", summary:"Ontario Grade 1 Data strand review: students collect, organise, and interpret data using tally charts and pictographs, and explore basic probability.",
   resourceLabel:"YouTube: Review: Data and Probability", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Data%20and%20Probability%20grade%201%20educational",
   quiz:[
     {q:"A tally chart uses ___ to count data.", options:["Tally marks","Coins","Pictures","Numbers only"], answer:0},
     {q:"A pictograph uses ___ to show data.", options:["Only numbers","Pictures or symbols","Letters","Only tally marks"], answer:1},
     {q:"If 5 students chose apples and 3 chose oranges, which is more popular?", options:["Equal","Apples","Cannot tell","Oranges"], answer:1},
     {q:"Probability means ___.", options:["Drawing graphs","Counting by 5s","The chance of an event happening","Collecting data"], answer:2},
     {q:"If a bag has 3 red and 1 blue marble, reaching in without looking gives you a better chance of pulling out a ___.", options:["Green","Red","Cannot tell","Blue"], answer:1}
   ]},
  {subject:"Science", title:"Earth and Weather Review", summary:"Ontario Grade 1 Earth and Space Systems review: students review weather patterns, the water cycle, rocks, soil, and the Sun's role in Earth's systems.",
   resourceLabel:"YouTube: Earth and Weather Review", resourceUrl:"https://www.youtube.com/results?search_query=Earth%20and%20Weather%20Review%20grade%201%20educational",
   quiz:[
     {q:"What causes day and night?", options:["The Moon blocking the Sun","Clouds covering the sky","Earth moving around the Sun","Earth rotating on its axis"], answer:3},
     {q:"The water cycle involves ___.", options:["Only clouds forming","Only rain falling","Evaporation, condensation, precipitation","Only rivers flowing"], answer:2},
     {q:"What is a thermometer used for?", options:["Measuring time","Measuring length","Measuring mass","Measuring temperature"], answer:3},
     {q:"Soil is made of ___.", options:["Only sand","Only rocks","Only clay","Rock, organic matter, air, and water"], answer:3},
     {q:"The Sun provides Earth with ___.", options:["Only light","Water","Heat and light energy essential for life","Only heat"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Citizenship and Community", summary:"Ontario Grade 1 Social Studies review: students review civic concepts including rights, responsibilities, community participation, and environmental stewardship.",
   resourceLabel:"YouTube: Citizenship and Community", resourceUrl:"https://www.youtube.com/results?search_query=Citizenship%20and%20Community%20grade%201%20educational",
   quiz:[
     {q:"What does it mean to be a good citizen?", options:["Doing whatever you want","Following only favourite rules","Ignoring community issues","Being responsible and helping others"], answer:3},
     {q:"Why is voting important in a democracy?", options:["Only important people vote","Citizens choose leaders and have a say","Votes do not count","It is not"], answer:1},
     {q:"How can children participate in their community?", options:["Only adults participate","By volunteering and helping neighbours","By watching others","By staying home"], answer:1},
     {q:"What is one way to care for the community environment?", options:["Using more electricity","Reducing, reusing, and recycling","Littering","Wasting water"], answer:1},
     {q:"A democratic community values ___.", options:["Money above all","Silence","Only one person's opinion","Fairness, equality, and participation"], answer:3}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"Language", title:"Reading Skills Review", summary:"Ontario Grade 1 Reading strand review: students review key reading strategies including predicting, retelling, identifying main idea, making connections, and using text features.",
   resourceLabel:"YouTube: Reading Skills Review", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20Skills%20Review%20grade%201%20educational",
   quiz:[
     {q:"Which reading strategy helps you guess what happens next?", options:["Connecting","Predicting","Retelling","Summarising"], answer:1},
     {q:"Retelling a story means ___.", options:["Telling events in your own words","Changing the ending","Drawing pictures","Reading it again"], answer:0},
     {q:"The main idea is ___.", options:["A small detail","What the text is mostly about","The first sentence always","The title"], answer:1},
     {q:"A text-to-self connection means ___.", options:["Comparing two texts","Relating it to your own experience","Connecting to world events","The text connects to another book"], answer:1},
     {q:"Non-fiction text features include ___.", options:["Headings, captions, and index","Plot and characters","Only pictures","Stories and poems"], answer:0}
   ]},
  {subject:"Math", title:"Review: Number Sense", summary:"Ontario Grade 1 Number strand review: students review counting, place value, addition, subtraction, fractions, and money.",
   resourceLabel:"YouTube: Review: Number Sense", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Number%20Sense%20grade%201%20educational",
   quiz:[
     {q:"4 tens + 7 ones = ?", options:["17","47","40","74"], answer:1},
     {q:"18 + 5 = ?", options:["21","22","23","24"], answer:2},
     {q:"20 - 13 = ?", options:["7","9","6","8"], answer:0},
     {q:"One-half is written as ___.", options:["1/3","1/2","1/4","2/3"], answer:1},
     {q:"A dime is worth ___ cents.", options:["5","50","25","10"], answer:3}
   ]},
  {subject:"Science", title:"Life Science Review", summary:"Ontario Grade 1 Life Systems strand review: students review living vs non-living, needs of living things, plants, animals, food chains, and habitats.",
   resourceLabel:"YouTube: Life Science Review", resourceUrl:"https://www.youtube.com/results?search_query=Life%20Science%20Review%20grade%201%20educational",
   quiz:[
     {q:"What are the four needs of all living things?", options:["Books, toys, music, games","Air, water, food, and shelter","Sun, moon, stars, planets","Electricity, light, heat, money"], answer:1},
     {q:"Name two parts of a plant.", options:["Wheel and pedal","Root and leaf","Door and window","Lens and frame"], answer:1},
     {q:"A food chain starts with a ___.", options:["Producer (plant)","Herbivore","Decomposer","Carnivore"], answer:0},
     {q:"A habitat provides an animal with ___.", options:["Electricity and heat","Food, water, shelter, and space","Toys and entertainment","School and education"], answer:1},
     {q:"Which best describes metamorphosis?", options:["A big body change during a life cycle","A kind of rock","A food chain","A type of habitat"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Review: Communities and Canada", summary:"Ontario Grade 1 Social Studies review: students demonstrate understanding of communities, Canadian geography, symbols, and civic values.",
   resourceLabel:"YouTube: Review: Communities and Canada", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Communities%20and%20Canada%20grade%201%20educational",
   quiz:[
     {q:"Which Canadian symbol has a maple leaf?", options:["The flag","The dollar bill","The coat of arms","All three"], answer:3},
     {q:"What is the capital city of Canada?", options:["Montreal","Vancouver","Ottawa","Toronto"], answer:2},
     {q:"How many provinces does Canada have?", options:["10","9","12","8"], answer:0},
     {q:"Which of the following is an example of multiculturalism?", options:["Many different cultures contributing to society","Everyone speaks the same language","Avoiding other cultures","One culture being better"], answer:0},
     {q:"What should every citizen do to keep their community clean?", options:["Litter occasionally","Leave lights on always","Waste water","Reduce waste and recycle"], answer:3}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"Language", title:"Year Review: Language Arts", summary:"Ontario Grade 1 Language strand comprehensive review: students demonstrate reading, writing, and oral communication skills developed throughout the year.",
   resourceLabel:"YouTube: Year Review: Language Arts", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Language%20Arts%20grade%201%20educational",
   quiz:[
     {q:"A noun names a ___.", options:["Connecting word","Action","Person, place, or thing","Describing word"], answer:2},
     {q:"A verb shows ___.", options:["A connection","A name","A description","An action or state of being"], answer:3},
     {q:"An adjective describes a ___.", options:["Noun","Adverb","Verb","Pronoun"], answer:0},
     {q:"Which is a complete sentence?", options:["Big dog fast.","The dog.","The dog runs.","Runs fast."], answer:2},
     {q:"Why is reading every day important?", options:["It builds vocabulary and imagination","It is not","Only for homework","Only for school"], answer:0}
   ]},
  {subject:"Math", title:"Year Review: Mathematics", summary:"Ontario Grade 1 Mathematics comprehensive review covering number sense, geometry, measurement, patterning, and data.",
   resourceLabel:"YouTube: Year Review: Mathematics", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Mathematics%20grade%201%20educational",
   quiz:[
     {q:"3 tens + 5 ones = ?", options:["35","30","53","45"], answer:0},
     {q:"9 + 8 = ?", options:["15","18","16","17"], answer:3},
     {q:"20 - 7 = ?", options:["14","12","11","13"], answer:3},
     {q:"A square has ___ equal sides.", options:["2","5","3","4"], answer:3},
     {q:"Skip count by 2s: 16, 18, 20, ___", options:["21","22","23","24"], answer:1}
   ]},
  {subject:"Science", title:"Year Review: Science", summary:"Ontario Grade 1 Science comprehensive review covering life systems, earth and space, matter, and physical science.",
   resourceLabel:"YouTube: Year Review: Science", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Science%20grade%201%20educational",
   quiz:[
     {q:"Living things need ___.", options:["Money and toys","Books and pencils","Air, water, food, and shelter","Electricity and television"], answer:2},
     {q:"Earth has ___ seasons.", options:["2","4","5","3"], answer:1},
     {q:"A push and pull are examples of ___.", options:["Patterns","Weather","States of matter","Forces"], answer:3},
     {q:"The Sun is a ___.", options:["Star","Planet","Comet","Moon"], answer:0},
     {q:"Plants make their food using sunlight through ___.", options:["Photosynthesis","Hibernation","Respiration","Digestion"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Year Review: Social Studies", summary:"Ontario Grade 1 Social Studies comprehensive review covering family, community, Canada, and civic values.",
   resourceLabel:"YouTube: Year Review: Social Studies", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Social%20Studies%20grade%201%20educational",
   quiz:[
     {q:"What is the capital of Canada?", options:["Vancouver","Toronto","Ottawa","Montreal"], answer:2},
     {q:"Community workers ___.", options:["Provide services that help people","Are not important","Only work for money","Create problems"], answer:0},
     {q:"What does it mean to be a good citizen?", options:["Following only favourite rules","Being responsible and helping others","Doing whatever you want","Ignoring rules"], answer:1},
     {q:"Canada's two official languages are ___.", options:["Spanish and English","Italian and French","French and English","English and Chinese"], answer:2},
     {q:"Why is respecting all cultures important in Canada?", options:["Canada values diversity and respect","Only in big cities","Only some cultures matter","It is not"], answer:0}
   ]},
]},
{day:31, label:"Day 31 — Mon", subjects:[
  {subject:"Language", title:"Consonant Digraphs: sh, ch, th, wh", summary:"Students learn that two consonants can combine to make one new sound called a digraph, such as sh in ship, ch in chip, th in thin, and wh in whale.",
   resourceLabel:"YouTube: Consonant Digraphs: sh, ch, th, wh", resourceUrl:"https://www.youtube.com/results?search_query=Consonant%20Digraphs%3A%20sh%2C%20ch%2C%20th%2C%20wh%20grade%201%20educational",
   quiz:[
     {q:"Which word begins with the digraph sh?", options:["Cat","Dog","Ship","Run"], answer:2},
     {q:"Which word begins with the digraph ch?", options:["Hat","Chip","Sun","Pig"], answer:1},
     {q:"Which word begins with the digraph th?", options:["Top","Sit","Thin","Man"], answer:2},
     {q:"A digraph is two consonant letters that make ___.", options:["One new sound together","A vowel sound","Two separate sounds","No sound at all"], answer:0},
     {q:"Which word begins with the digraph wh?", options:["Whale","Cat","Bed","Sun"], answer:0}
   ],
   worksheet:[
     {prompt:"What two letters make the sh sound at the start of the word ship?", answers:["sh"]},
     {prompt:"What two letters make the ch sound at the start of the word chip?", answers:["ch"]},
     {prompt:"Say the word whale. What two letters make the wh sound at the start?", answers:["wh"]}
   ]},
  {subject:"Math", title:"Counting to 100", summary:"Students practise counting aloud from 1 to 100 by ones, and recognize written numerals up to 100, extending counting skills learned earlier in the year.",
   resourceLabel:"YouTube: Counting to 100", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20to%20100%20grade%201%20educational",
   quiz:[
     {q:"What number comes right after 69?", options:["68","69","70","71"], answer:2},
     {q:"What number comes right after 99?", options:["98","99","101","100"], answer:3},
     {q:"Which number is greater, 76 or 67?", options:["They are equal","76","Cannot tell","67"], answer:1},
     {q:"What number comes right before 80?", options:["78","80","81","79"], answer:3},
     {q:"Counting from 1 to 100 means we say each number ___.", options:["Twice each","In order, one at a time","Backward only","In random order"], answer:1}
   ],
   worksheet:[
     {prompt:"What number comes right after 59?", answers:["60","sixty"]},
     {prompt:"What number comes right after 89?", answers:["90","ninety"]},
     {prompt:"What number comes right before 100?", answers:["99","ninety-nine","ninety nine"]}
   ]},
  {subject:"Science", title:"Seasonal Changes: Spring", summary:"Students learn that spring is a season when the weather warms up, snow melts, plants begin to grow, and many animals become active again after winter.",
   resourceLabel:"YouTube: Seasonal Changes: Spring", resourceUrl:"https://www.youtube.com/results?search_query=Seasonal%20Changes%3A%20Spring%20grade%201%20educational",
   quiz:[
     {q:"What usually happens to the weather in spring?", options:["It gets colder","It stays exactly the same","It disappears","It gets warmer"], answer:3},
     {q:"What happens to snow as spring arrives?", options:["It turns to sand","It grows bigger","It turns purple","It melts"], answer:3},
     {q:"Which of these often happens to plants in spring?", options:["They freeze completely","They begin to grow","They disappear forever","They turn to stone"], answer:1},
     {q:"Which season comes right before spring?", options:["Spring again","Winter","Summer","Fall"], answer:1},
     {q:"Why do many animals become more active in spring?", options:["The warmer weather brings more food and better conditions","Animals never move in spring","Spring has no effect on animals","Animals sleep more in spring"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one thing that happens to snow in spring.", answers:["it melts","melts","melting"]},
     {prompt:"Name one thing that begins to grow in spring, like a flower or plant.", answers:["flowers","plants","flower","plant"]},
     {prompt:"Does the weather usually get warmer or colder in spring?", answers:["warmer"]}
   ]},
  {subject:"SocialStudies", title:"Our Neighbourhood: Places We Visit", summary:"Students learn about familiar places in their neighbourhood, such as a park, library, or store, and discuss how each place helps the community.",
   resourceLabel:"YouTube: Our Neighbourhood: Places We Visit", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Neighbourhood%3A%20Places%20We%20Visit%20grade%201%20educational",
   quiz:[
     {q:"Which of these is a place you might find in a neighbourhood?", options:["The ocean floor","Outer space","A volcano","A park"], answer:3},
     {q:"What can you do at a library?", options:["Borrow books","Deliver mail","Fight fires","Buy groceries"], answer:0},
     {q:"Why are neighbourhood places like parks and libraries helpful?", options:["They cost nothing and do nothing","People never use them","They are not helpful","They give people places to play, learn, and gather"], answer:3},
     {q:"A neighbourhood is a part of a larger ___.", options:["Ocean","Desert","Galaxy","Community"], answer:3},
     {q:"Which of these might you visit to buy food in your neighbourhood?", options:["A mountain","A cloud","A grocery store","A fire truck"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one place you might visit in your neighbourhood, like a park or library.", answers:["park","library","store"]},
     {prompt:"What can you borrow at a library?", answers:["books","a book"]},
     {prompt:"Do neighbourhoods have many different places that help people?", answers:["yes"]}
   ]},
]},
{day:32, label:"Day 32 — Tue", subjects:[
  {subject:"Language", title:"Word Families: -it and -in", summary:"Students explore the -it and -in word families, learning that changing the first letter of sit or pin can create new rhyming words such as bit, hit, win, and fin.",
   resourceLabel:"YouTube: Word Families: -it and -in", resourceUrl:"https://www.youtube.com/results?search_query=Word%20Families%3A%20-it%20and%20-in%20grade%201%20educational",
   quiz:[
     {q:"Which word belongs to the -it word family?", options:["Sit","Dog","Sun","Cat"], answer:0},
     {q:"Which word belongs to the -in word family?", options:["Top","Bed","Win","Man"], answer:2},
     {q:"Which word rhymes with pin?", options:["Sun","Dog","Cat","Fin"], answer:3},
     {q:"A word family is a group of words that share the same ___.", options:["Meaning","Author","Colour","Ending sound"], answer:3},
     {q:"Which word does not belong to the -it family?", options:["Sit","Hit","Bit","Dog"], answer:3}
   ],
   worksheet:[
     {prompt:"Change the first letter of sit to make a new word that rhymes.", answers:["bit","hit","fit","kit"]},
     {prompt:"Change the first letter of pin to make a new word that rhymes.", answers:["win","fin","din","tin"]},
     {prompt:"Do sit and hit belong to the same word family?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Numbers to 100: Tens and Ones", summary:"Students learn to break apart two-digit numbers into tens and ones, such as recognizing that 47 is made of 4 tens and 7 ones.",
   resourceLabel:"YouTube: Numbers to 100: Tens and Ones", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%20to%20100%3A%20Tens%20and%20Ones%20grade%201%20educational",
   quiz:[
     {q:"How many tens are in the number 52?", options:["2","50","5","7"], answer:2},
     {q:"How many ones are in the number 38?", options:["38","30","3","8"], answer:3},
     {q:"Which number has 7 tens and 2 ones?", options:["79","27","70","72"], answer:3},
     {q:"What number is made of 9 tens and 0 ones?", options:["19","90","9","99"], answer:1},
     {q:"Breaking a number into tens and ones helps us understand its ___.", options:["Sound","Smell","Value","Colour"], answer:2}
   ],
   worksheet:[
     {prompt:"How many tens are in the number 47?", answers:["4","four"]},
     {prompt:"How many ones are in the number 47?", answers:["7","seven"]},
     {prompt:"Write the number that has 6 tens and 3 ones.", answers:["63"]}
   ]},
  {subject:"Science", title:"Seasonal Changes: Summer", summary:"Students learn that summer is the warmest season of the year, with long sunny days, and that many plants and animals are very active during this time.",
   resourceLabel:"YouTube: Seasonal Changes: Summer", resourceUrl:"https://www.youtube.com/results?search_query=Seasonal%20Changes%3A%20Summer%20grade%201%20educational",
   quiz:[
     {q:"Which season is usually the warmest of the year?", options:["Spring","Winter","Fall","Summer"], answer:3},
     {q:"In summer, are the days usually longer or shorter?", options:["Shorter","Longer","There is no daylight","Exactly the same"], answer:1},
     {q:"Which season comes right after summer?", options:["Summer again","Spring","Winter","Fall"], answer:3},
     {q:"Why are plants often very healthy and green in summer?", options:["Summer is the coldest season","They get plenty of sunlight and warmth","Plants stop growing in summer","Summer has no sunlight"], answer:1},
     {q:"Which of these is a common summer activity?", options:["Swimming outdoors","Sledding downhill","Building a snowman","Raking fallen leaves"], answer:0}
   ],
   worksheet:[
     {prompt:"Is summer usually the warmest or the coldest season?", answers:["warmest"]},
     {prompt:"Are the days in summer usually long or short?", answers:["long"]},
     {prompt:"Name one activity people often do in summer, like swimming.", answers:["swimming","swim","play outside","picnic"]}
   ]},
  {subject:"SocialStudies", title:"Jobs People Do: Goods and Services", summary:"Students learn that some jobs make or sell goods, like toys or bread, while other jobs provide services, like teaching or fixing things, and both kinds of jobs help a community.",
   resourceLabel:"YouTube: Jobs People Do: Goods and Services", resourceUrl:"https://www.youtube.com/results?search_query=Jobs%20People%20Do%3A%20Goods%20and%20Services%20grade%201%20educational",
   quiz:[
     {q:"What word describes an item that is made or sold, like a toy?", options:["A season","A good","A rule","A service"], answer:1},
     {q:"What word describes a helpful job like teaching or fixing something?", options:["A good","A holiday","A service","A season"], answer:2},
     {q:"Which of these jobs mainly provides a service?", options:["Farmer","Teacher","Baker","Toy maker"], answer:1},
     {q:"Which of these jobs mainly makes a good?", options:["Doctor","Teacher","Baker","Dentist"], answer:2},
     {q:"Why does a community need both goods and services?", options:["Goods and services are not needed","Communities need only goods","People need things to buy and helpful jobs done","Communities need only services"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one job that makes or sells a good, like a baker.", answers:["baker","toy maker","farmer"]},
     {prompt:"Name one job that provides a service, like a teacher.", answers:["teacher","doctor","dentist"]},
     {prompt:"Do both goods and services help people in a community?", answers:["yes"]}
   ]},
]},
{day:33, label:"Day 33 — Wed", subjects:[
  {subject:"Language", title:"Word Families: -ug and -ub", summary:"Students explore the -ug and -ub word families, learning that changing the first letter of bug or cub can create new rhyming words such as hug, rug, tub, and cub.",
   resourceLabel:"YouTube: Word Families: -ug and -ub", resourceUrl:"https://www.youtube.com/results?search_query=Word%20Families%3A%20-ug%20and%20-ub%20grade%201%20educational",
   quiz:[
     {q:"Which word belongs to the -ug word family?", options:["Cat","Sun","Bug","Dog"], answer:2},
     {q:"Which word belongs to the -ub word family?", options:["Bed","Man","Cub","Top"], answer:2},
     {q:"Which word rhymes with rug?", options:["Dog","Sun","Cat","Hug"], answer:3},
     {q:"Which word does not belong to the -ub family?", options:["Cub","Rub","Tub","Cat"], answer:3},
     {q:"Word families help us read new words by noticing ___.", options:["Similar endings","Pictures only","Colours","Page numbers"], answer:0}
   ],
   worksheet:[
     {prompt:"Change the first letter of bug to make a new word that rhymes.", answers:["hug","rug","mug","jug","tug"]},
     {prompt:"Change the first letter of cub to make a new word that rhymes.", answers:["tub","rub","sub","hub"]},
     {prompt:"Do bug and hug belong to the same word family?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Comparing Numbers: Greater Than and Less Than", summary:"Students learn to compare two numbers up to 100 and use the words greater than, less than, and equal to describe which number is bigger or smaller.",
   resourceLabel:"YouTube: Comparing Numbers: Greater Than and Less Than", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Numbers%3A%20Greater%20Than%20and%20Less%20Than%20grade%201%20educational",
   quiz:[
     {q:"Which number is greater, 62 or 26?", options:["They are equal","26","62","Cannot tell"], answer:2},
     {q:"Which number is less, 81 or 18?", options:["They are equal","18","Cannot tell","81"], answer:1},
     {q:"What word describes two numbers that have the same value?", options:["Greater","Odd","Equal","Less"], answer:2},
     {q:"Which word means a number is bigger than another?", options:["Less than","Equal to","Greater than","Odd"], answer:2},
     {q:"Which of these is true?", options:["15 is greater than 25","50 is greater than 40","30 is less than 20","10 is equal to 20"], answer:1}
   ],
   worksheet:[
     {prompt:"Which number is greater, 45 or 54?", answers:["54"]},
     {prompt:"Which number is less, 68 or 39?", answers:["39"]},
     {prompt:"Are 20 and 20 equal or different?", answers:["equal","the same"]}
   ]},
  {subject:"Science", title:"Insects and Their Body Parts", summary:"Students learn that insects, such as ants and butterflies, have three main body parts and six legs, and explore how insects are different from other animals.",
   resourceLabel:"YouTube: Insects and Their Body Parts", resourceUrl:"https://www.youtube.com/results?search_query=Insects%20and%20Their%20Body%20Parts%20grade%201%20educational",
   quiz:[
     {q:"How many legs does an insect have?", options:["10","4","8","6"], answer:3},
     {q:"How many main body parts does an insect have?", options:["5","3","2","4"], answer:1},
     {q:"Which of these is an insect?", options:["Dog","Fish","Butterfly","Bird"], answer:2},
     {q:"Which of these is not an insect?", options:["Bee","Spider","Ladybug","Ant"], answer:1},
     {q:"What covers the outside of many insect bodies?", options:["A hard outer shell","Scales like a fish","Fur","Feathers"], answer:0}
   ],
   worksheet:[
     {prompt:"How many legs does an insect have?", answers:["6","six"]},
     {prompt:"Name one insect, like an ant or butterfly.", answers:["ant","butterfly","bee","ladybug"]},
     {prompt:"How many main body parts does an insect have?", answers:["3","three"]}
   ]},
  {subject:"SocialStudies", title:"Needs and Wants: What We Really Need", summary:"Students learn to tell the difference between needs, things we must have to live such as food and shelter, and wants, things that are nice to have but not necessary such as toys.",
   resourceLabel:"YouTube: Needs and Wants: What We Really Need", resourceUrl:"https://www.youtube.com/results?search_query=Needs%20and%20Wants%3A%20What%20We%20Really%20Need%20grade%201%20educational",
   quiz:[
     {q:"Which of these is a need?", options:["Water","A video game","Candy","A toy"], answer:0},
     {q:"Which of these is a want?", options:["Shelter","Water","Food","A new toy"], answer:3},
     {q:"What is the difference between a need and a want?", options:["Needs are necessary to live, wants are not","There is no difference","Wants are more important","Needs are only for adults"], answer:0},
     {q:"Which of these is something every person needs to survive?", options:["A birthday gift","Shelter","A game console","A bicycle"], answer:1},
     {q:"Why is it helpful to understand needs and wants?", options:["It does not matter","Wants are always more important than needs","It helps us make good choices about what is most important","Needs and wants are the same thing"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one thing that is a need, like food or water.", answers:["food","water","shelter","clothing"]},
     {prompt:"Name one thing that is a want, like a toy.", answers:["toy","candy","video game"]},
     {prompt:"Do people need food to live?", answers:["yes"]}
   ]},
]},
{day:34, label:"Day 34 — Thu", subjects:[
  {subject:"Language", title:"Beginning Blends: sp, sm, sn, sw", summary:"Students learn that two consonants can blend together at the start of a word, such as sp in spin, sm in smile, sn in snail, and sw in swim.",
   resourceLabel:"YouTube: Beginning Blends: sp, sm, sn, sw", resourceUrl:"https://www.youtube.com/results?search_query=Beginning%20Blends%3A%20sp%2C%20sm%2C%20sn%2C%20sw%20grade%201%20educational",
   quiz:[
     {q:"Which word begins with the blend sp?", options:["Dog","Run","Cat","Spin"], answer:3},
     {q:"Which word begins with the blend sm?", options:["Hat","Pig","Smile","Sun"], answer:2},
     {q:"Which word begins with the blend sn?", options:["Sit","Snail","Top","Man"], answer:1},
     {q:"Which word begins with the blend sw?", options:["Sun","Swim","Bed","Cat"], answer:1},
     {q:"A beginning blend is when two consonant letters ___.", options:["Blend their sounds together at the start of a word","Turn into vowels","Are never used","Are silent"], answer:0}
   ],
   worksheet:[
     {prompt:"What two letters blend together at the start of the word spin?", answers:["sp"]},
     {prompt:"What two letters blend together at the start of the word smile?", answers:["sm"]},
     {prompt:"Say the word swim. What two letters blend at the start?", answers:["sw"]}
   ]},
  {subject:"Math", title:"Fractions: Quarters", summary:"Students learn that dividing a whole into four equal parts creates quarters, and that one of the four parts is called one-quarter or one-fourth.",
   resourceLabel:"YouTube: Fractions: Quarters", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%3A%20Quarters%20grade%201%20educational",
   quiz:[
     {q:"If a shape is cut into 4 equal parts, each part is called ___.", options:["One-quarter","One whole","One-half","One-third"], answer:0},
     {q:"How many quarters make one whole?", options:["4","2","5","3"], answer:0},
     {q:"Which is smaller, one-quarter or one-half?", options:["One-half","One-quarter","They are equal","Cannot tell"], answer:1},
     {q:"A whole cut into four equal parts shows ___.", options:["Quarters","Wholes","Thirds","Halves"], answer:0},
     {q:"If you eat one-quarter of a sandwich, how many quarters are left?", options:["2","4","3","1"], answer:2}
   ],
   worksheet:[
     {prompt:"If a pizza is cut into 4 equal parts, what is each part called?", answers:["a quarter","quarter","one-quarter","one fourth","a fourth"]},
     {prompt:"How many quarters make one whole?", answers:["4","four"]},
     {prompt:"Is one-quarter bigger or smaller than one-half?", answers:["smaller"]}
   ]},
  {subject:"Science", title:"Nocturnal Animals: Creatures of the Night", summary:"Students learn that nocturnal animals, such as owls and bats, are awake and active mostly at night and sleep during the day.",
   resourceLabel:"YouTube: Nocturnal Animals: Creatures of the Night", resourceUrl:"https://www.youtube.com/results?search_query=Nocturnal%20Animals%3A%20Creatures%20of%20the%20Night%20grade%201%20educational",
   quiz:[
     {q:"What does the word nocturnal mean?", options:["Always asleep","Awake mostly at night","Awake mostly during the day","Never awake"], answer:1},
     {q:"Which of these animals is known for being nocturnal?", options:["Squirrel","Owl","Chicken","Robin"], answer:1},
     {q:"What do most nocturnal animals do during the day?", options:["Go swimming","Sleep or rest","Play loudly","Fly to school"], answer:1},
     {q:"Why might large eyes help a nocturnal animal like an owl?", options:["Large eyes help in bright sunlight only","Nocturnal animals cannot see at all","They help the animal see well in the dark","Large eyes are not helpful at night"], answer:2},
     {q:"Which of these is also a nocturnal animal?", options:["Duck","Bat","Rooster","Robin"], answer:1}
   ],
   worksheet:[
     {prompt:"What word describes animals that are awake mostly at night?", answers:["nocturnal"]},
     {prompt:"Name one nocturnal animal, like an owl or bat.", answers:["owl","bat","raccoon"]},
     {prompt:"Do nocturnal animals usually sleep during the day?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Transportation Then and Now", summary:"Students compare how people travelled long ago, such as by horse and wagon, to how people travel today, such as by car, bus, and airplane.",
   resourceLabel:"YouTube: Transportation Then and Now", resourceUrl:"https://www.youtube.com/results?search_query=Transportation%20Then%20and%20Now%20grade%201%20educational",
   quiz:[
     {q:"How did many people travel long ago before cars were invented?", options:["By airplane","By rocket","By horse and wagon","By submarine"], answer:2},
     {q:"Which of these is a common way people travel today?", options:["Car","Ox cart only","Sailboat only","Horse and wagon only"], answer:0},
     {q:"How has transportation changed over time?", options:["It has not changed at all","It has become slower","People no longer travel","It has become faster and easier"], answer:3},
     {q:"Which of these did NOT exist long ago the way it does today?", options:["Airplanes","Walking","Rivers","The sun"], answer:0},
     {q:"Why is it useful to learn about transportation then and now?", options:["It helps us understand how travel has changed and improved","It is not useful","Old and new transportation are identical","Transportation never changes"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one way people travelled long ago, like by horse.", answers:["horse","wagon","horse and wagon"]},
     {prompt:"Name one way people travel today, like by car.", answers:["car","bus","airplane","train"]},
     {prompt:"Is travel today usually faster than travel long ago?", answers:["yes"]}
   ]},
]},
{day:35, label:"Day 35 — Fri", subjects:[
  {subject:"Language", title:"Rhyming Words", summary:"Students practise identifying rhyming words, pairs of words that end with the same sound, such as cat and hat or sun and fun.",
   resourceLabel:"YouTube: Rhyming Words", resourceUrl:"https://www.youtube.com/results?search_query=Rhyming%20Words%20grade%201%20educational",
   quiz:[
     {q:"Which word rhymes with cat?", options:["Sun","Pig","Hat","Dog"], answer:2},
     {q:"Which word rhymes with sun?", options:["Cat","Bed","Dog","Fun"], answer:3},
     {q:"Two words rhyme when they ___.", options:["Have the same meaning","Are the same length","Start with the same letter","End with the same sound"], answer:3},
     {q:"Which word rhymes with hop?", options:["Pig","Sun","Top","Cat"], answer:2},
     {q:"Which pair of words does NOT rhyme?", options:["Sun and fun","Dog and log","Cat and dog","Cat and hat"], answer:2}
   ],
   worksheet:[
     {prompt:"Name a word that rhymes with cat.", answers:["hat","bat","mat","sat","rat","fat"]},
     {prompt:"Name a word that rhymes with sun.", answers:["fun","run","bun","one"]},
     {prompt:"Do hat and cat rhyme?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Measuring Capacity: More and Less", summary:"Students compare the capacity of different containers, learning which container holds more or less using non-standard units, such as pouring water between cups.",
   resourceLabel:"YouTube: Measuring Capacity: More and Less", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Capacity%3A%20More%20and%20Less%20grade%201%20educational",
   quiz:[
     {q:"Which container usually holds more water, a bucket or a teacup?", options:["Teacup","Cannot tell","Bucket","They hold the same"], answer:2},
     {q:"What word describes how much liquid a container can hold?", options:["Weight","Capacity","Length","Colour"], answer:1},
     {q:"If you pour water from a full cup into a bigger empty bowl, what happens?", options:["The bowl overflows immediately","The water disappears","The water fits with room to spare","Nothing happens"], answer:2},
     {q:"Which of these containers likely holds the least amount of water?", options:["A swimming pool","A bucket","A teaspoon","A bathtub"], answer:2},
     {q:"Comparing capacity helps us understand ___.", options:["How much a container can hold","How heavy an object is","What colour something is","How long an object is"], answer:0}
   ],
   worksheet:[
     {prompt:"If a big jug and a small cup are filled with water, which one holds more?", answers:["the jug","jug","big jug"]},
     {prompt:"What word describes how much a container can hold?", answers:["capacity"]},
     {prompt:"Which usually holds less water, a bathtub or a teacup?", answers:["teacup","the teacup"]}
   ]},
  {subject:"Science", title:"The Moon and Its Phases", summary:"Students learn that the Moon appears to change shape in the sky over about a month, moving through phases such as a full moon and a crescent moon.",
   resourceLabel:"YouTube: The Moon and Its Phases", resourceUrl:"https://www.youtube.com/results?search_query=The%20Moon%20and%20Its%20Phases%20grade%201%20educational",
   quiz:[
     {q:"What do we call it when the Moon looks like a complete circle in the sky?", options:["New moon","Crescent moon","Half moon","Full moon"], answer:3},
     {q:"What do we call the thin curved shape of the Moon?", options:["Star","Full moon","Square moon","Crescent moon"], answer:3},
     {q:"About how long does it take the Moon to go through all of its phases?", options:["One year","About a month","One day","Ten years"], answer:1},
     {q:"Why does the Moon appear to change shape in the sky?", options:["The Moon disappears and grows back","Clouds change the Moon shape","The Moon actually changes size","Different amounts of sunlit Moon are visible from Earth over time"], answer:3},
     {q:"The changing shapes of the Moon are called Moon ___.", options:["Phases","Rings","Colours","Seasons"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call it when the whole round Moon is visible in the sky?", answers:["full moon"]},
     {prompt:"What do we call the thin curved shape of the Moon?", answers:["crescent moon","crescent"]},
     {prompt:"Does the Moon appear to change shape over time?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"My Body Belongs to Me: Personal Safety", summary:"Students learn simple personal safety rules, such as it is okay to say no to unwanted touches and to tell a trusted adult if something makes them feel unsafe.",
   resourceLabel:"YouTube: My Body Belongs to Me: Personal Safety", resourceUrl:"https://www.youtube.com/results?search_query=My%20Body%20Belongs%20to%20Me%3A%20Personal%20Safety%20grade%201%20educational",
   quiz:[
     {q:"What should you do if someone makes you feel unsafe?", options:["Ignore the feeling","Run away and hide alone","Stay quiet forever","Tell a trusted adult"], answer:3},
     {q:"Is it okay to say no to a touch that makes you feel uncomfortable?", options:["Yes, it is okay","No, never","Only if an adult says so","Only at school"], answer:0},
     {q:"Which of these is a trusted adult you might talk to about a safety concern?", options:["Nobody","A parent or teacher","A cartoon character","A stranger online"], answer:1},
     {q:"Why is it important to talk about feelings of being unsafe?", options:["Only adults have feelings","Feelings are never important","It is better to stay silent","Trusted adults can help keep you safe"], answer:3},
     {q:"Whose body is it, and who gets to decide about unwanted touches?", options:["No one decides","Only an adult decides","My body belongs to me","Only a teacher decides"], answer:2}
   ],
   worksheet:[
     {prompt:"What should you do if something makes you feel unsafe?", answers:["tell a trusted adult","tell an adult"]},
     {prompt:"Is it okay to say no if someone tries to touch you in a way you do not like?", answers:["yes"]},
     {prompt:"Name one trusted adult you could talk to, like a parent or teacher.", answers:["parent","teacher","mom","dad"]}
   ]},
]},
{day:36, label:"Day 36 — Mon", subjects:[
  {subject:"Language", title:"Sequencing Events: First, Next, Last", summary:"Students learn to put events from a story in order using the words first, next, and last, helping them understand and retell what happened.",
   resourceLabel:"YouTube: Sequencing Events: First, Next, Last", resourceUrl:"https://www.youtube.com/results?search_query=Sequencing%20Events%3A%20First%2C%20Next%2C%20Last%20grade%201%20educational",
   quiz:[
     {q:"Which word describes the event that happens at the beginning of a story?", options:["Middle only","First","Never","Last"], answer:1},
     {q:"Which word describes the event that happens at the end of a story?", options:["First","Last","Before","Next"], answer:1},
     {q:"Which sentence uses sequencing words correctly?", options:["None of these show order","Last we start the day","First we ate lunch then we woke up","First we woke up, next we ate breakfast, last we went to school"], answer:3},
     {q:"Why is putting events in order important when retelling a story?", options:["Stories have no order","It helps the story make sense","Only the ending matters","Order does not matter"], answer:1},
     {q:"Which word would you use to describe an event that happens in the middle?", options:["Next","Before","First","Last"], answer:0}
   ],
   worksheet:[
     {prompt:"What word tells us an event that happens at the very beginning?", answers:["first"]},
     {prompt:"What word tells us an event that happens at the very end?", answers:["last"]},
     {prompt:"Put these words in order to describe a sequence: first, next, ___.", answers:["last"]}
   ]},
  {subject:"Math", title:"Symmetry: Matching Halves", summary:"Students explore symmetry by folding shapes and pictures in half to see if both sides match exactly, learning that a symmetrical shape has two matching halves.",
   resourceLabel:"YouTube: Symmetry: Matching Halves", resourceUrl:"https://www.youtube.com/results?search_query=Symmetry%3A%20Matching%20Halves%20grade%201%20educational",
   quiz:[
     {q:"What does it mean for a shape to be symmetrical?", options:["The shape is coloured red","The shape has no sides","The shape is always a circle","Both halves match exactly"], answer:3},
     {q:"Which of these shapes is symmetrical?", options:["An uneven splash","A heart","A random blob","A scribble"], answer:1},
     {q:"If you fold a symmetrical picture exactly in half, what happens?", options:["The sides look completely different","Nothing can be compared","The picture disappears","Both sides match"], answer:3},
     {q:"A line that divides a shape into two matching halves is called a line of ___.", options:["Colour","Weight","Length","Symmetry"], answer:3},
     {q:"Which of these letters is symmetrical when folded top to bottom?", options:["J","F","G","B"], answer:3}
   ],
   worksheet:[
     {prompt:"What word describes a shape whose two halves match exactly?", answers:["symmetrical","symmetry"]},
     {prompt:"Name one shape that is symmetrical, like a circle or square.", answers:["circle","square","heart"]},
     {prompt:"If you fold a symmetrical shape in half, do both sides match?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Recycling and Reducing Waste", summary:"Students learn simple ways to care for the environment by reducing waste, reusing items, and recycling materials such as paper, plastic, and cans.",
   resourceLabel:"YouTube: Recycling and Reducing Waste", resourceUrl:"https://www.youtube.com/results?search_query=Recycling%20and%20Reducing%20Waste%20grade%201%20educational",
   quiz:[
     {q:"Which of these materials can often be recycled?", options:["Paper","Sunlight","Rainbows","Air"], answer:0},
     {q:"What does it mean to reuse an item?", options:["Ignoring it","Burying it in the yard","Throwing it away right away","Using it again instead of throwing it away"], answer:3},
     {q:"Why is recycling helpful for the environment?", options:["It has no effect","It creates more garbage","It reduces waste and saves resources","It harms the environment"], answer:2},
     {q:"Which of these actions helps reduce waste?", options:["Littering outside","Using a reusable water bottle","Throwing away recyclable cans","Wasting paper"], answer:1},
     {q:"The three words often used together to describe caring for the environment are reduce, reuse, and ___.", options:["Replace","Recycle","Remove","Repeat"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one material that can be recycled, like paper or plastic.", answers:["paper","plastic","cans","glass"]},
     {prompt:"What word describes using something again instead of throwing it away?", answers:["reuse","reusing"]},
     {prompt:"Is it good for the environment to recycle instead of throwing everything away?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Communication Then and Now", summary:"Students compare how people communicated long ago, such as sending letters, to how people communicate today, such as using phones and computers.",
   resourceLabel:"YouTube: Communication Then and Now", resourceUrl:"https://www.youtube.com/results?search_query=Communication%20Then%20and%20Now%20grade%201%20educational",
   quiz:[
     {q:"How did many people send messages long ago before phones were common?", options:["By writing letters","By text message","By email","By video call"], answer:0},
     {q:"Which of these is a common way people communicate today?", options:["Only smoke signals","Only carrier pigeons","Only letters carried by horse","Telephone"], answer:3},
     {q:"How has communication changed over time?", options:["People no longer communicate","It has become slower","It has not changed at all","It has become faster and easier"], answer:3},
     {q:"Which of these did people use to communicate long before phones existed?", options:["Written letters","Text messages","The internet","Video calls"], answer:0},
     {q:"Why is it useful to compare communication then and now?", options:["Old and new communication are identical","It helps us understand how technology has changed our lives","Communication never changes","It is not useful"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one way people communicated long ago, like writing a letter.", answers:["letter","writing letters","sending letters"]},
     {prompt:"Name one way people communicate today, like using a phone.", answers:["phone","telephone","computer","email"]},
     {prompt:"Is communication today usually faster than communication long ago?", answers:["yes"]}
   ]},
]},
{day:37, label:"Day 37 — Tue", subjects:[
  {subject:"Language", title:"Fiction and Non-Fiction: Comparing Texts", summary:"Students learn to compare fiction texts, which tell made-up stories, with non-fiction texts, which give true facts and information.",
   resourceLabel:"YouTube: Fiction and Non-Fiction: Comparing Texts", resourceUrl:"https://www.youtube.com/results?search_query=Fiction%20and%20Non-Fiction%3A%20Comparing%20Texts%20grade%201%20educational",
   quiz:[
     {q:"What kind of story does a fiction book tell?", options:["A true story","A made-up story","No story at all","Only facts"], answer:1},
     {q:"What kind of information does a non-fiction book give?", options:["Only pictures","Made-up stories","True facts and information","Nothing at all"], answer:2},
     {q:"Which of these is an example of a fiction book?", options:["A book about talking animals having an adventure","A book about the solar system","A book about real ocean animals","A book about the water cycle"], answer:0},
     {q:"Which of these is an example of a non-fiction book?", options:["A book of true facts about dinosaurs","A story about a talking teddy bear","A story about a dragon","A tale about a magic castle"], answer:0},
     {q:"Why is it useful to know if a book is fiction or non-fiction?", options:["All books are the same","Fiction and non-fiction are identical","It does not matter","It helps us know if a book is telling a true story or made-up story"], answer:3}
   ],
   worksheet:[
     {prompt:"Does a fiction book tell a true story or a made-up story?", answers:["made-up story","made up story","made-up"]},
     {prompt:"Does a non-fiction book give true facts or made-up stories?", answers:["true facts","facts"]},
     {prompt:"Name one example of a non-fiction topic, like animals or weather.", answers:["animals","weather","space"]}
   ]},
  {subject:"Math", title:"Sorting and Classifying Objects", summary:"Students practise sorting a group of objects into categories based on shared attributes, such as colour, size, or shape, and explain the rule used to sort them.",
   resourceLabel:"YouTube: Sorting and Classifying Objects", resourceUrl:"https://www.youtube.com/results?search_query=Sorting%20and%20Classifying%20Objects%20grade%201%20educational",
   quiz:[
     {q:"Which of these is a way you could sort a group of objects?", options:["Randomly with no rule","By colour","Objects cannot be sorted","By nothing"], answer:1},
     {q:"If you sort shapes by number of sides, where would a triangle and a different triangle go?", options:["In the same group","No group at all","Shapes cannot be sorted this way","In different groups"], answer:0},
     {q:"Why do we sort objects into groups?", options:["Sorting is never useful","It makes objects disappear","It helps us see patterns and organize information","It has no purpose"], answer:2},
     {q:"Which of these objects would NOT belong in a group of red objects?", options:["A blue car","A red block","A red ball","A red apple"], answer:0},
     {q:"A sorting rule tells us ___.", options:["The weather","Nothing useful","How objects are grouped together","The colour of the sky"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one way you could sort a group of buttons, like by colour or size.", answers:["colour","size","shape"]},
     {prompt:"If you sort toys by colour, what group would a red ball and a red block go in?", answers:["red","red group"]},
     {prompt:"Can objects be sorted in more than one way?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Taking Care of Our Teeth", summary:"Students learn simple habits for keeping teeth healthy, such as brushing twice a day, flossing, eating healthy foods, and visiting the dentist.",
   resourceLabel:"YouTube: Taking Care of Our Teeth", resourceUrl:"https://www.youtube.com/results?search_query=Taking%20Care%20of%20Our%20Teeth%20grade%201%20educational",
   quiz:[
     {q:"How many times a day should you usually brush your teeth?", options:["Twice","Only on weekends","Never","Once"], answer:0},
     {q:"Who is a helper that checks and cares for our teeth?", options:["A dentist","A baker","A firefighter","A postal worker"], answer:0},
     {q:"Which of these habits helps keep our teeth healthy?", options:["Ignoring toothaches","Brushing and flossing","Never brushing","Eating candy all day"], answer:1},
     {q:"Why is it important to take care of our teeth?", options:["Teeth care is not important","Teeth do not need care","Healthy teeth help us eat and stay healthy","Only adults have teeth"], answer:2},
     {q:"Which of these foods is better for healthy teeth?", options:["An apple","A sugary soda","A sugary candy","A lollipop"], answer:0}
   ],
   worksheet:[
     {prompt:"How many times a day should you usually brush your teeth?", answers:["2","two","twice"]},
     {prompt:"Who helps check that your teeth are healthy?", answers:["dentist"]},
     {prompt:"Name one healthy food that is good for your teeth, like an apple.", answers:["apple","vegetables","cheese"]}
   ]},
  {subject:"SocialStudies", title:"Cooperation and Teamwork in a Group", summary:"Students learn what it means to cooperate with others in a group, such as sharing materials, taking turns, and listening to different ideas to reach a shared goal.",
   resourceLabel:"YouTube: Cooperation and Teamwork in a Group", resourceUrl:"https://www.youtube.com/results?search_query=Cooperation%20and%20Teamwork%20in%20a%20Group%20grade%201%20educational",
   quiz:[
     {q:"What does it mean to cooperate with a group?", options:["Refusing to share","Doing everything alone","Working together toward a shared goal","Ignoring everyone else"], answer:2},
     {q:"Which of these shows good cooperation in a group?", options:["Yelling over others","Sharing materials and taking turns","Refusing to listen","Grabbing everything for yourself"], answer:1},
     {q:"Why is cooperation important when working in a group?", options:["It slows everything down","Groups work better without cooperation","Cooperation is not helpful","It helps the group reach its goal more smoothly"], answer:3},
     {q:"What should you do if a group member has a different idea than you?", options:["Listen and discuss the idea","Yell at them","Leave the group","Ignore them completely"], answer:0},
     {q:"A group that cooperates well can often ___.", options:["Make tasks harder","Finish tasks more successfully","Avoid working together","Never finish anything"], answer:1}
   ],
   worksheet:[
     {prompt:"What word describes people working together toward a shared goal?", answers:["cooperation","teamwork"]},
     {prompt:"Name one way to cooperate in a group, like sharing or taking turns.", answers:["sharing","taking turns","listening"]},
     {prompt:"Should group members listen to each other ideas?", answers:["yes"]}
   ]},
]},
{day:38, label:"Day 38 — Wed", subjects:[
  {subject:"Language", title:"Asking and Answering Questions About a Text", summary:"Students practise asking and answering simple questions about a story or text they have read or heard, to check their understanding of what happened.",
   resourceLabel:"YouTube: Asking and Answering Questions About a Text", resourceUrl:"https://www.youtube.com/results?search_query=Asking%20and%20Answering%20Questions%20About%20a%20Text%20grade%201%20educational",
   quiz:[
     {q:"Why do readers ask questions about a text?", options:["Questions are never helpful","To skip reading","To help them understand what they read","To confuse themselves"], answer:2},
     {q:"Which of these is a good question to ask after reading a story?", options:["What happened in the story?","What is your favourite colour?","What is the weather today?","None of these"], answer:0},
     {q:"Answering questions about a text helps us ___.", options:["Skip the ending","Ignore the story","Understand and remember what we read","Forget the story"], answer:2},
     {q:"Which question word would you use to ask about a character in a story?", options:["Nothing","Who","Colour","Never"], answer:1},
     {q:"If you cannot answer a question about a story, what might help?", options:["Reading the story again","Ignoring the question","Giving up completely","Changing the story"], answer:0}
   ],
   worksheet:[
     {prompt:"What is one question you could ask about a story you just read?", answers:["who is in the story","what happened","where did it happen"]},
     {prompt:"Why do we ask questions about a text?", answers:["to understand it","to check understanding"]},
     {prompt:"Can asking questions help you understand a story better?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Money: Making Small Amounts", summary:"Students practise combining coins, such as nickels, dimes, and pennies, to make small amounts of money, such as making 15 cents using a dime and a nickel.",
   resourceLabel:"YouTube: Money: Making Small Amounts", resourceUrl:"https://www.youtube.com/results?search_query=Money%3A%20Making%20Small%20Amounts%20grade%201%20educational",
   quiz:[
     {q:"Which coin is worth 10 cents?", options:["Dime","Penny","Quarter","Nickel"], answer:0},
     {q:"Which coin is worth 5 cents?", options:["Penny","Quarter","Dime","Nickel"], answer:3},
     {q:"Which combination of coins makes 15 cents?", options:["Two pennies","A dime and a nickel","A quarter","One nickel"], answer:1},
     {q:"How many nickels make 10 cents?", options:["3","1","2","4"], answer:2},
     {q:"If you have a dime and two pennies, how much money do you have?", options:["12 cents","13 cents","11 cents","10 cents"], answer:0}
   ],
   worksheet:[
     {prompt:"Which two coins could you use to make 15 cents?", answers:["dime and nickel","a dime and a nickel"]},
     {prompt:"How many pennies make 5 cents?", answers:["5","five"]},
     {prompt:"What coin is worth 10 cents?", answers:["dime"]}
   ]},
  {subject:"Science", title:"The Five Senses", summary:"Students review the five senses, sight, hearing, smell, taste, and touch, and the body part used for each, such as eyes for sight and ears for hearing.",
   resourceLabel:"YouTube: The Five Senses", resourceUrl:"https://www.youtube.com/results?search_query=The%20Five%20Senses%20grade%201%20educational",
   quiz:[
     {q:"Which body part do we use to smell?", options:["Nose","Tongue","Eyes","Ears"], answer:0},
     {q:"Which body part do we use to taste?", options:["Nose","Tongue","Ears","Skin"], answer:1},
     {q:"Which sense do we use to hear sounds?", options:["Taste","Sight","Smell","Hearing"], answer:3},
     {q:"Which body part helps us feel if something is soft or rough?", options:["Ears","Tongue","Nose","Skin"], answer:3},
     {q:"How many senses do people have?", options:["3","4","5","6"], answer:2}
   ],
   worksheet:[
     {prompt:"What body part do we use to smell?", answers:["nose"]},
     {prompt:"What body part do we use to taste?", answers:["tongue"]},
     {prompt:"Name one sense that uses our skin to feel things.", answers:["touch"]}
   ]},
  {subject:"SocialStudies", title:"Our Capital City: Ottawa", summary:"Students learn that Ottawa is the capital city of Canada, where important government buildings, such as the Parliament Buildings, are located.",
   resourceLabel:"YouTube: Our Capital City: Ottawa", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Capital%20City%3A%20Ottawa%20grade%201%20educational",
   quiz:[
     {q:"What is the capital city of Canada?", options:["Toronto","Ottawa","Montreal","Vancouver"], answer:1},
     {q:"What important buildings are located in Ottawa?", options:["A ski resort","A fishing dock","The Parliament Buildings","A large farm"], answer:2},
     {q:"Why is Ottawa an important city in Canada?", options:["It has no government buildings","It is the smallest town in Canada","It is where important government decisions are made","It is not important"], answer:2},
     {q:"In which province is Ottawa located?", options:["Alberta","Ontario","Quebec","Manitoba"], answer:1},
     {q:"What is usually located in a capital city?", options:["A large desert","A small pond","The government of a country","Nothing important"], answer:2}
   ],
   worksheet:[
     {prompt:"What is the capital city of Canada?", answers:["ottawa"]},
     {prompt:"What are the important government buildings in Ottawa called?", answers:["parliament buildings","parliament"]},
     {prompt:"Is Ottawa an important city for the government of Canada?", answers:["yes"]}
   ]},
]},
{day:39, label:"Day 39 — Thu", subjects:[
  {subject:"Language", title:"Letter Writing: A Note to a Friend", summary:"Students learn the basic parts of a friendly letter, including a greeting, a short message, and a closing, and practise writing a simple note to a friend.",
   resourceLabel:"YouTube: Letter Writing: A Note to a Friend", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20Writing%3A%20A%20Note%20to%20a%20Friend%20grade%201%20educational",
   quiz:[
     {q:"What word often begins a friendly letter?", options:["Chapter One","Dear","The End","Once"], answer:1},
     {q:"What is the greeting of a letter used for?", options:["To draw a picture","To end the letter","To greet the person you are writing to","To add a date only"], answer:2},
     {q:"Which of these could be a closing for a friendly letter?", options:["From","Once upon a time","Chapter Two","The middle"], answer:0},
     {q:"Why might you write a letter to a friend?", options:["To confuse your friend","To share news or say something kind","Letters are never useful","To avoid talking"], answer:1},
     {q:"A friendly letter usually has a greeting, a message, and a ___.", options:["Table of contents","Index","Closing","Glossary"], answer:2}
   ],
   worksheet:[
     {prompt:"What word often starts a friendly letter, like Dear?", answers:["dear"]},
     {prompt:"What is one thing you might write in the closing of a letter, like Love or From?", answers:["love","from","your friend"]},
     {prompt:"Does a friendly letter usually have a greeting at the start?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Time: Half Past the Hour", summary:"Students learn to read an analog clock showing half past the hour, recognizing that the long hand points to the 6 and the short hand is halfway between two numbers.",
   resourceLabel:"YouTube: Time: Half Past the Hour", resourceUrl:"https://www.youtube.com/results?search_query=Time%3A%20Half%20Past%20the%20Hour%20grade%201%20educational",
   quiz:[
     {q:"At half past the hour, where does the long hand point?", options:["The 6","The 12","The 3","The 9"], answer:0},
     {q:"At half past 4, where is the short hand pointing?", options:["Exactly at the 4","Exactly at the 5","Between the 4 and 5","Exactly at the 12"], answer:2},
     {q:"Half past the hour means how many minutes have passed since the hour started?", options:["60 minutes","15 minutes","30 minutes","45 minutes"], answer:2},
     {q:"If the long hand points to the 6 and the short hand is between the 7 and 8, what time is it?", options:["Half past 7","Half past 8","Half past 6","Half past 12"], answer:0},
     {q:"Reading a clock to the half hour helps us know ___.", options:["What day it is","What colour it is","What time it is","What season it is"], answer:2}
   ],
   worksheet:[
     {prompt:"When the long hand points to the 6, what part of the hour is it?", answers:["half past","half past the hour"]},
     {prompt:"At half past 3, is the short hand pointing exactly at the 3 or between the 3 and 4?", answers:["between the 3 and 4","between 3 and 4"]},
     {prompt:"What number does the long hand point to at half past any hour?", answers:["6","the 6"]}
   ]},
  {subject:"Science", title:"Changing Materials: Heating and Cooling", summary:"Students learn that heating and cooling can change materials, such as ice melting into water when warmed or water freezing into ice when cooled.",
   resourceLabel:"YouTube: Changing Materials: Heating and Cooling", resourceUrl:"https://www.youtube.com/results?search_query=Changing%20Materials%3A%20Heating%20and%20Cooling%20grade%201%20educational",
   quiz:[
     {q:"What happens to ice when it is heated?", options:["It turns to stone","It disappears completely","It gets colder","It melts into water"], answer:3},
     {q:"What happens to water when it is cooled to a very low temperature?", options:["It boils","It freezes into ice","Nothing happens","It turns to gas"], answer:1},
     {q:"Heating and cooling can change a material from one ___ to another.", options:["Name","Owner","Colour","State"], answer:3},
     {q:"Which of these is an example of heating changing a material?", options:["A rock staying the same","Butter melting in the sun","A book being read","A shoe being tied"], answer:1},
     {q:"Why is it useful to know how heating and cooling change materials?", options:["Materials never change","Heat and cold do nothing","It helps us understand how the world around us works","It is not useful"], answer:2}
   ],
   worksheet:[
     {prompt:"What happens to ice when it is heated?", answers:["it melts","melts"]},
     {prompt:"What happens to water when it is cooled a lot?", answers:["it freezes","freezes"]},
     {prompt:"Name one material that changes when you heat it, like ice or chocolate.", answers:["ice","chocolate","butter"]}
   ]},
  {subject:"SocialStudies", title:"Landmarks and Special Places in Canada", summary:"Students learn about well-known Canadian landmarks, such as Niagara Falls and the Rocky Mountains, and discuss why these special places are important.",
   resourceLabel:"YouTube: Landmarks and Special Places in Canada", resourceUrl:"https://www.youtube.com/results?search_query=Landmarks%20and%20Special%20Places%20in%20Canada%20grade%201%20educational",
   quiz:[
     {q:"What is Niagara Falls?", options:["A famous waterfall","A city hall","A desert","A small pond"], answer:0},
     {q:"Which of these is a famous Canadian mountain range?", options:["The Amazon River","The Rocky Mountains","The Great Wall","The Sahara Desert"], answer:1},
     {q:"Why are landmarks like Niagara Falls important to Canada?", options:["No one visits them","They are found in every country","They are not important","They are special natural places many people visit"], answer:3},
     {q:"Which of these is a tall tower landmark found in Toronto?", options:["The CN Tower","The Great Wall","The Rocky Mountains","The Eiffel Tower"], answer:0},
     {q:"What is a landmark?", options:["A type of food","A well-known and special place","A kind of weather","A school subject"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one famous Canadian landmark, like Niagara Falls.", answers:["niagara falls","the rocky mountains","cn tower"]},
     {prompt:"Are the Rocky Mountains located in Canada?", answers:["yes"]},
     {prompt:"What is Niagara Falls an example of, a waterfall or a desert?", answers:["waterfall"]}
   ]},
]},
{day:40, label:"Day 40 — Fri", subjects:[
  {subject:"Language", title:"Language Review: Sounds, Words, and Stories", summary:"Students review recent Language skills: digraphs, word families, blends, rhyming, sequencing, and comparing fiction and non-fiction texts.",
   resourceLabel:"YouTube: Language Review: Sounds, Words, and Stories", resourceUrl:"https://www.youtube.com/results?search_query=Language%20Review%3A%20Sounds%2C%20Words%2C%20and%20Stories%20grade%201%20educational",
   quiz:[
     {q:"Which word begins with the digraph sh?", options:["Cat","Run","Dog","Ship"], answer:3},
     {q:"Which word rhymes with cat?", options:["Hat","Pig","Dog","Sun"], answer:0},
     {q:"Which word belongs to the -it word family?", options:["Sun","Dog","Sit","Cat"], answer:2},
     {q:"What kind of story does a fiction book tell?", options:["A true story","Only facts","No story at all","A made-up story"], answer:3},
     {q:"Which word begins with the blend sp?", options:["Spin","Cat","Dog","Run"], answer:0}
   ],
   worksheet:[
     {prompt:"What two letters make the sh sound at the start of the word ship?", answers:["sh"]},
     {prompt:"Name a word that rhymes with cat.", answers:["hat","bat","mat","sat","rat","fat"]},
     {prompt:"Does a fiction book tell a true story or a made-up story?", answers:["made-up story","made up story","made-up"]}
   ]},
  {subject:"Math", title:"Math Review: Numbers, Shapes, and Time", summary:"Students review recent Math skills: counting to 100, place value, comparing numbers, fractions, capacity, symmetry, sorting, money, and telling time to the half hour.",
   resourceLabel:"YouTube: Math Review: Numbers, Shapes, and Time", resourceUrl:"https://www.youtube.com/results?search_query=Math%20Review%3A%20Numbers%2C%20Shapes%2C%20and%20Time%20grade%201%20educational",
   quiz:[
     {q:"What number comes right after 99?", options:["101","99","98","100"], answer:3},
     {q:"Which number is greater, 62 or 26?", options:["They are equal","26","62","Cannot tell"], answer:2},
     {q:"If a shape is cut into 4 equal parts, each part is called ___.", options:["One-quarter","One-third","One-half","One whole"], answer:0},
     {q:"Which coin is worth 10 cents?", options:["Dime","Penny","Quarter","Nickel"], answer:0},
     {q:"At half past the hour, where does the long hand point?", options:["The 3","The 9","The 12","The 6"], answer:3}
   ],
   worksheet:[
     {prompt:"What number comes right after 89?", answers:["90","ninety"]},
     {prompt:"How many tens are in the number 47?", answers:["4","four"]},
     {prompt:"How many quarters make one whole?", answers:["4","four"]}
   ]},
  {subject:"Science", title:"Science Review: Seasons, Senses, and Earth", summary:"Students review recent Science topics: seasonal changes, insects, nocturnal animals, the Moon, recycling, dental health, the five senses, and changing materials.",
   resourceLabel:"YouTube: Science Review: Seasons, Senses, and Earth", resourceUrl:"https://www.youtube.com/results?search_query=Science%20Review%3A%20Seasons%2C%20Senses%2C%20and%20Earth%20grade%201%20educational",
   quiz:[
     {q:"Which season is usually the warmest of the year?", options:["Spring","Fall","Winter","Summer"], answer:3},
     {q:"How many legs does an insect have?", options:["4","8","10","6"], answer:3},
     {q:"Which of these animals is known for being nocturnal?", options:["Owl","Chicken","Squirrel","Robin"], answer:0},
     {q:"Which body part do we use to smell?", options:["Ears","Tongue","Eyes","Nose"], answer:3},
     {q:"What happens to water when it is cooled to a very low temperature?", options:["It freezes into ice","It turns to gas","It boils","Nothing happens"], answer:0}
   ],
   worksheet:[
     {prompt:"Is summer usually the warmest or the coldest season?", answers:["warmest"]},
     {prompt:"How many legs does an insect have?", answers:["6","six"]},
     {prompt:"What happens to ice when it is heated?", answers:["it melts","melts"]}
   ]},
  {subject:"SocialStudies", title:"Social Studies Review: Community, Canada, and Cooperation", summary:"Students review recent Social Studies topics: neighbourhoods, jobs, needs and wants, transportation, personal safety, communication, cooperation, and Canadian landmarks.",
   resourceLabel:"YouTube: Social Studies Review: Community, Canada, and Cooperation", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Review%3A%20Community%2C%20Canada%2C%20and%20Cooperation%20grade%201%20educational",
   quiz:[
     {q:"Which of these is a place you might find in a neighbourhood?", options:["Outer space","A park","A volcano","The ocean floor"], answer:1},
     {q:"Which of these is a need?", options:["Water","Candy","A video game","A toy"], answer:0},
     {q:"What should you do if someone makes you feel unsafe?", options:["Run away and hide alone","Ignore the feeling","Tell a trusted adult","Stay quiet forever"], answer:2},
     {q:"What is the capital city of Canada?", options:["Vancouver","Ottawa","Montreal","Toronto"], answer:1},
     {q:"What does it mean to cooperate with a group?", options:["Working together toward a shared goal","Ignoring everyone else","Refusing to share","Doing everything alone"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one place you might visit in your neighbourhood, like a park or library.", answers:["park","library","store"]},
     {prompt:"What is the capital city of Canada?", answers:["ottawa"]},
     {prompt:"What should you do if someone makes you feel unsafe?", answers:["tell a trusted adult","tell an adult"]}
   ]},
]},
];

export default curriculum;