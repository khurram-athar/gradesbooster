import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"Language", title:"Short Vowel Sounds", summary:"Practice blending short vowel sounds (a, e, i, o, u) in simple words like cat, bed, pig, hop, sun — a Grade 1 foundation skill Grade 2 builds on.",
   resourceLabel:"YouTube: Short Vowel Sounds", resourceUrl:"https://www.youtube.com/results?search_query=Short%20Vowel%20Sounds%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=-EbzKgs6Aiw",
   quiz:[
     {q:"Which word has the short 'a' sound?", options:["car","cake","cat","cane"], answer:2},
     {q:"Which word has the short 'i' sound?", options:["pig","pie","pine","pi"], answer:0},
     {q:"Which word rhymes with 'hop'?", options:["hat","hope","hip","top"], answer:3},
     {q:"What sound does the 'u' make in 'sun'?", options:["long u","long o","short u","silent"], answer:2},
     {q:"Which word has a short 'e' sound?", options:["bed","bee","be","bead"], answer:0},
   ],
   worksheet:[
     {prompt:"Which vowel is missing? c_t (an animal that meows)", answers:["a"]},
     {prompt:"Which vowel is missing? p_g (a farm animal)", answers:["i"]},
     {prompt:"Write a word that rhymes with 'hop'.", answers:["top","mop","pop","stop","shop","drop","chop","flop","cop"]}
   ]},
  {subject:"Math", title:"Numbers to 50", summary:"Ontario Number strand: count, read, and represent whole numbers to 50, and compare quantities.",
   resourceLabel:"YouTube: Numbers to 50", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%20to%2050%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=9XZypM2Z3Ro",
   quiz:[
     {q:"Which number comes right after 39?", options:["38","41","40","30"], answer:2},
     {q:"Which number is greater, 27 or 32?", options:["Cannot tell","27","They are equal","32"], answer:3},
     {q:"What number is 10 more than 24?", options:["44","14","34","25"], answer:2},
     {q:"Which of these is between 15 and 20?", options:["21","14","25","17"], answer:3},
     {q:"Count by 1s: 45, 46, 47, __?", options:["50","49","44","48"], answer:3},
   ],
   worksheet:[
     {prompt:"What number comes right after 39?", answers:["40","forty"]},
     {prompt:"Which is greater: 27 or 32? Write the greater number.", answers:["32","thirty-two","thirty two"]},
     {prompt:"What number is 10 more than 24?", answers:["34","thirty-four","thirty four"]}
   ]},
  {subject:"Science", title:"Living vs. Nonliving Things", summary:"Ontario Life Systems strand: living things grow, need food/water/air, and respond to their environment; nonliving things do not.",
   resourceLabel:"YouTube: Living vs. Nonliving Things", resourceUrl:"https://www.youtube.com/results?search_query=Living%20vs.%20Nonliving%20Things%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=QmQvdUaH7hE",
   quiz:[
     {q:"Which of these is a living thing?", options:["Cloud","Tree","Rock","Chair"], answer:1},
     {q:"Which of these is NOT living?", options:["Dog","Bird","Bicycle","Flower"], answer:2},
     {q:"All living things need...", options:["Wheels","Electricity","Paint","Food and water"], answer:3},
     {q:"Living things can...", options:["Stay exactly the same forever","Grow and change","Never need food","Be made of metal only"], answer:1},
     {q:"Which is a sign something is alive?", options:["It is blue","It is hard","It breathes","It is heavy"], answer:2},
   ],
   worksheet:[
     {prompt:"A bird is a ___ thing.", answers:["living"]},
     {prompt:"A bicycle is a ___ thing.", answers:["nonliving","non-living","non living"]},
     {prompt:"All living things need food and ___.", answers:["water"]}
   ]},
  {subject:"SocialStudies", title:"My Family and Community", summary:"Ontario Heritage & Identity strand: families and communities have traditions, celebrations, and roles that make up our personal and community identity.",
   resourceLabel:"YouTube: My Family and Community", resourceUrl:"https://www.youtube.com/results?search_query=My%20Family%20and%20Community%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"A community is a place where people...", options:["Only work","Never meet","Live alone","Live and help each other"], answer:3},
     {q:"Which of these is part of a community?", options:["An ocean far away","A different planet","School","The moon"], answer:2},
     {q:"A family tradition is something a family...", options:["Is not allowed to do","Does once and forgets","Does together every year","Buys at a store"], answer:2},
     {q:"A neighbor is someone who...", options:["Lives far away","Lives in another country","You never see","Lives near you"], answer:3},
     {q:"Communities can be found in...", options:["Cities, towns, and farms","Only cities","Only the country","Nowhere"], answer:0},
   ],
   worksheet:[
     {prompt:"A ___ is a place where people live and help each other.", answers:["community"]},
     {prompt:"A neighbor is someone who lives ___ you.", answers:["near","close to","nearby"]},
     {prompt:"A family tradition is something a family does together every ___.", answers:["year"]}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"Language", title:"Long Vowel Sounds", summary:"Long vowels often say their own name, like in cake, bee, kite, boat, and cube.",
   resourceLabel:"YouTube: Long Vowel Sounds", resourceUrl:"https://www.youtube.com/results?search_query=Long%20Vowel%20Sounds%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4TjcT7Gto3U",
   quiz:[
     {q:"Which word has a long 'a' sound?", options:["cat","cab","cake","cap"], answer:2},
     {q:"Which word has a long 'e' sound?", options:["bee","bed","bet","beg"], answer:0},
     {q:"Which word has a long 'o' sound?", options:["bog","boat","bob","box"], answer:1},
     {q:"What makes the 'i' long in 'kite'?", options:["A capital letter","Two consonants","The silent 'e'","Nothing"], answer:2},
     {q:"Which word has a long 'u' sound?", options:["cuff","cut","cube","cup"], answer:2},
   ]},
  {subject:"Math", title:"Addition Within 20", summary:"Ontario Number/Algebra strands: add two numbers with a total to 20 using counting on, doubles, and number lines.",
   resourceLabel:"YouTube: Addition Within 20", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20Within%2020%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ZgzpTx-s9Zo",
   quiz:[
     {q:"7 + 6 = ?", options:["14","13","11","12"], answer:1},
     {q:"9 + 9 = ?", options:["17","19","18","16"], answer:2},
     {q:"5 + 8 = ?", options:["12","13","15","14"], answer:1},
     {q:"11 + 4 = ?", options:["14","13","16","15"], answer:3},
     {q:"6 + 7 = ?", options:["13","11","14","12"], answer:0},
   ]},
  {subject:"Science", title:"Growth and Changes in Animals", summary:"Ontario Life Systems strand for Grade 2: animals grow and change through life cycles and need certain things to survive.",
   resourceLabel:"YouTube: Growth and Changes in Animals", resourceUrl:"https://www.youtube.com/results?search_query=Growth%20and%20Changes%20in%20Animals%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=LHcQWk1dHzk",
   quiz:[
     {q:"What is a life cycle?", options:["The stages of an animal's growth","A type of bicycle","A season","A kind of food"], answer:0},
     {q:"A caterpillar changes into a...", options:["Frog","Fish","Bird","Butterfly or moth"], answer:3},
     {q:"Baby animals usually need...", options:["Nothing at all","A school","Care, food, and protection from a parent","Only sunlight"], answer:2},
     {q:"Which is the correct order for a frog's life cycle?", options:["Egg, tadpole, frog","Egg, frog, tadpole","Frog, tadpole, egg","Tadpole, frog, egg"], answer:0},
     {q:"As most animals grow, they...", options:["Disappear","Get smaller","Stay exactly the same","Change in size and sometimes shape"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Traditions and Celebrations", summary:"Different families and communities in Canada celebrate different traditions, and learning about them builds understanding and respect.",
   resourceLabel:"YouTube: Traditions and Celebrations", resourceUrl:"https://www.youtube.com/results?search_query=Traditions%20and%20Celebrations%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pD8dTo4NxHM",
   quiz:[
     {q:"Why do families have traditions?", options:["To celebrate what matters to them","No real reason","To follow rules only","Because they must"], answer:0},
     {q:"Learning about other families' traditions helps us...", options:["Ignore differences","Copy everyone exactly","Forget our own traditions","Understand and respect each other"], answer:3},
     {q:"A celebration is often a time when families...", options:["Avoid each other","Stay silent","Come together to mark something special","Work extra hours"], answer:2},
     {q:"Which is an example of a tradition?", options:["Watching TV once","Brushing teeth","A yearly family celebration or holiday","Walking to school"], answer:2},
     {q:"In Canada, families come from...", options:["No particular background","Only one country","Only one culture","Many different cultures and backgrounds"], answer:3},
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"Language", title:"Nouns: People, Places, Things", summary:"A noun names a person, place, animal, or thing, like teacher, park, dog, or book.",
   resourceLabel:"YouTube: Nouns: People, Places, Things", resourceUrl:"https://www.youtube.com/results?search_query=Nouns%3A%20People%2C%20Places%2C%20Things%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=3K5vg_QsKCc",
   quiz:[
     {q:"Which word is a noun?", options:["Dog","Quickly","Run","Happy"], answer:0},
     {q:"Which word names a place?", options:["Sing","Jump","Blue","School"], answer:3},
     {q:"Which word names a person?", options:["Hop","Green","Fast","Teacher"], answer:3},
     {q:"In 'The cat sat on the mat,' which word is a noun?", options:["Sat","Cat","On","The"], answer:1},
     {q:"Which is a thing (object) noun?", options:["Slowly","Run","Book","Quiet"], answer:2},
   ]},
  {subject:"Math", title:"Subtraction Within 20", summary:"Practice taking away numbers within 20, using counting back and known facts.",
   resourceLabel:"YouTube: Subtraction Within 20", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20Within%2020%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ds226Vh7epg",
   quiz:[
     {q:"15 - 7 = ?", options:["7","6","9","8"], answer:3},
     {q:"18 - 9 = ?", options:["9","10","11","8"], answer:0},
     {q:"12 - 5 = ?", options:["6","8","7","5"], answer:2},
     {q:"20 - 13 = ?", options:["7","9","8","6"], answer:0},
     {q:"16 - 8 = ?", options:["9","8","6","7"], answer:1},
   ]},
  {subject:"Science", title:"Properties of Liquids and Solids", summary:"Ontario Matter & Energy strand for Grade 2: solids hold their shape; liquids take the shape of their container and can be poured.",
   resourceLabel:"YouTube: Properties of Liquids and Solids", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Liquids%20and%20Solids%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=qYzjg5nRMOg",
   quiz:[
     {q:"Which of these is a solid?", options:["Rock","Water","Juice","Milk"], answer:0},
     {q:"A liquid will...", options:["Take the shape of its container","Never move","Keep one shape always","Disappear instantly"], answer:0},
     {q:"Which of these is a liquid?", options:["Ice cube","Orange juice","Wooden block","Book"], answer:1},
     {q:"What happens when a solid like ice melts?", options:["Nothing happens","It becomes a liquid","It becomes a gas instantly","It becomes heavier only"], answer:1},
     {q:"You can pour a...", options:["Both equally well","Liquid","Solid","Neither"], answer:1},
   ]},
  {subject:"SocialStudies", title:"Communities Around the World", summary:"Ontario People & Environment strand: communities around the world look different based on climate, land, and culture, but all communities help meet people's needs.",
   resourceLabel:"YouTube: Communities Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Communities%20Around%20the%20World%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=A96dvMFqxk4",
   quiz:[
     {q:"Why do communities around the world look different?", options:["Random chance only","No reason","Different climates, land, and cultures","They are all the same"], answer:2},
     {q:"A community near the ocean might rely on...", options:["Fishing","Desert farming only","Nothing special","Snowplowing year round"], answer:0},
     {q:"What do all communities need, no matter where they are?", options:["The same weather","Identical buildings","Nothing in common","Shelter, food, and water"], answer:3},
     {q:"Comparing communities helps us understand...", options:["Nothing useful","How places are alike and different","Only our own community","That everyone is exactly alike"], answer:1},
     {q:"A community in a cold climate might need...", options:["Only swimsuits","Nothing different","Warm clothing and heated homes","No shelter"], answer:2},
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"Language", title:"Action Verbs", summary:"A verb shows action — what someone or something does, like run, jump, eat, or read.",
   resourceLabel:"YouTube: Action Verbs", resourceUrl:"https://www.youtube.com/results?search_query=Action%20Verbs%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=iwfUZAYyqR0",
   quiz:[
     {q:"Which word is a verb (action word)?", options:["Table","Blue","Jump","Happy"], answer:2},
     {q:"In 'The dog runs fast,' which word is the verb?", options:["Runs","Dog","The","Fast"], answer:0},
     {q:"Which sentence has an action verb?", options:["She is tall.","The sky is blue.","I am happy.","He kicks the ball."], answer:3},
     {q:"Which word shows someone reading?", options:["Library","Reads","Book","Quiet"], answer:1},
     {q:"Which is NOT a verb?", options:["Run","Sleep","Chair","Eat"], answer:2},
   ]},
  {subject:"Math", title:"Place Value: Tens and Ones", summary:"Two-digit numbers are made of tens and ones, like 34 = 3 tens + 4 ones — a key Ontario Number strand idea.",
   resourceLabel:"YouTube: Place Value: Tens and Ones", resourceUrl:"https://www.youtube.com/results?search_query=Place%20Value%3A%20Tens%20and%20Ones%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=_dHu5TFxPtk",
   quiz:[
     {q:"In the number 47, how many tens are there?", options:["47","0","7","4"], answer:3},
     {q:"In the number 62, how many ones are there?", options:["8","60","6","2"], answer:3},
     {q:"3 tens and 5 ones equals...", options:["305","35","8","53"], answer:1},
     {q:"Which number has 5 tens and 0 ones?", options:["5","500","50","15"], answer:2},
     {q:"What is 2 tens + 9 ones?", options:["20","29","92","11"], answer:1},
   ]},
  {subject:"Science", title:"Structures and Mechanisms: Movement", summary:"Ontario Structures & Mechanisms strand for Grade 2: simple mechanisms like wheels, levers, and gears help things move.",
   resourceLabel:"YouTube: Structures and Mechanisms: Movement", resourceUrl:"https://www.youtube.com/results?search_query=Structures%20and%20Mechanisms%3A%20Movement%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=1R6MxJpEjfs",
   quiz:[
     {q:"What helps a wagon move easily?", options:["Wheels","Nothing","Glue","A flat bottom with no wheels"], answer:0},
     {q:"A lever can help you...", options:["Sing a song","Make food","Paint a picture","Lift a heavy object with less effort"], answer:3},
     {q:"Which everyday object uses wheels to move?", options:["A spoon","A pillow","A bicycle","A book"], answer:2},
     {q:"A see-saw is an example of a...", options:["Liquid","Habitat","Lever","Wheel"], answer:2},
     {q:"Gears work together to...", options:["Move connected parts","Stay still forever","Make sounds only","Melt"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Maps and Globes", summary:"A map is a flat drawing of a place, and a globe is a round model of the whole Earth.",
   resourceLabel:"YouTube: Maps and Globes", resourceUrl:"https://www.youtube.com/results?search_query=Maps%20and%20Globes%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=KS6R6xSV9Vc",
   quiz:[
     {q:"A globe is shaped like a...", options:["Triangle","Square","Line","Sphere (ball)"], answer:3},
     {q:"A map shows...", options:["Nothing real","Places from above","Smells","Sounds"], answer:1},
     {q:"What is a map key (legend) for?", options:["Telling the weather","Explaining symbols on the map","Locking the map","Decoration only"], answer:1},
     {q:"Which shows the whole Earth at once best?", options:["A street sign","A clock","A globe","A photo of one house"], answer:2},
     {q:"Maps can help you...", options:["Brush your teeth","Cook dinner","Sing a song","Find your way to a place"], answer:3},
   ]},
]},
{day:5, label:"Day 5 — Fri (Review)", reviewNote:"Review day: mixed questions from Days 1–4 to check what's sticking before moving on.", subjects:[
  {subject:"Language", title:"Review: Vowel Sounds, Nouns & Verbs", summary:"Mixed review of short/long vowels, nouns, and action verbs.",
   resourceLabel:"YouTube: Review: Vowel Sounds, Nouns & Verbs", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Vowel%20Sounds%2C%20Nouns%20%26%20Verbs%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=_II6ySgUtWc",
   quiz:[
     {q:"Which word has a long vowel sound?", options:["cake","cap","cat","cab"], answer:0},
     {q:"Which word is a noun?", options:["Quickly","Park","Run","Happy"], answer:1},
     {q:"Which word is a verb?", options:["Jump","Soft","Blue","Table"], answer:0},
     {q:"Which word has a short vowel sound?", options:["pine","pi","pig","pie"], answer:2},
     {q:"In 'The girl reads a book,' which word is the verb?", options:["The","Book","Girl","Reads"], answer:3},
   ]},
  {subject:"Math", title:"Review: Numbers, Addition & Subtraction", summary:"Mixed review of counting to 50, addition and subtraction within 20, and place value.",
   resourceLabel:"YouTube: Review: Numbers, Addition & Subtraction", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Numbers%2C%20Addition%20%26%20Subtraction%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=7J1OkxuyLD0",
   quiz:[
     {q:"8 + 7 = ?", options:["14","13","15","16"], answer:2},
     {q:"17 - 9 = ?", options:["6","9","7","8"], answer:3},
     {q:"Which number is greater, 41 or 38?", options:["41","Equal","38","Can't tell"], answer:0},
     {q:"In 56, how many tens are there?", options:["6","56","5","0"], answer:2},
     {q:"What is 10 more than 33?", options:["43","34","44","23"], answer:0},
   ]},
  {subject:"Science", title:"Review: Living Things, Matter & Movement", summary:"Mixed review of living/nonliving things, animal life cycles, solids/liquids, and simple machines.",
   resourceLabel:"YouTube: Review: Living Things, Matter & Movement", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Living%20Things%2C%20Matter%20%26%20Movement%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=kBL9-RFhnbM",
   quiz:[
     {q:"Which is a living thing?", options:["Cloud","Bird","Rock","Chair"], answer:1},
     {q:"A tadpole grows into a...", options:["Frog","Butterfly","Bird","Fish"], answer:0},
     {q:"Which is a solid?", options:["Milk","Rock","Juice","Water"], answer:1},
     {q:"What helps a wagon move easily?", options:["Wheels","A flat base","Paint","Glue"], answer:0},
     {q:"A liquid takes the shape of...", options:["A square always","A ball always","Nothing","Its container"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Review: Community, Traditions & Maps", summary:"Mixed review of community, family traditions, world communities, and maps/globes.",
   resourceLabel:"YouTube: Review: Community, Traditions & Maps", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Community%2C%20Traditions%20%26%20Maps%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"A community is a group of people who...", options:["Only work","Live and help each other","Never meet","Live alone"], answer:1},
     {q:"A family tradition is something done...", options:["Never","Together regularly to celebrate","By strangers only","Once and forgotten"], answer:1},
     {q:"A globe shows...", options:["One street","The whole Earth","Nothing real","A single house"], answer:1},
     {q:"Communities near oceans often rely on...", options:["Fishing","Desert farming","Nothing special","Snowplowing"], answer:0},
     {q:"A map key (legend) explains...", options:["The weather","Nothing","Symbols on the map","A story"], answer:2},
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"Language", title:"Describing Words (Adjectives)", summary:"An adjective describes a noun, telling more about its size, colour, shape, or feeling.",
   resourceLabel:"YouTube: Describing Words (Adjectives)", resourceUrl:"https://www.youtube.com/results?search_query=Describing%20Words%20%28Adjectives%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=5ZkMbLkGims",
   quiz:[
     {q:"Which word describes a noun (an adjective)?", options:["Quickly","Run","Jump","Big"], answer:3},
     {q:"In 'The red ball bounced,' which word describes the ball?", options:["Bounced","The","Ball","Red"], answer:3},
     {q:"Which is an adjective for size?", options:["Tiny","Sing","Walk","Eat"], answer:0},
     {q:"Which sentence uses an adjective?", options:["The soft blanket is warm.","They eat.","He jumps.","She runs."], answer:0},
     {q:"Which word could describe a feeling?", options:["Table","Happy","Run","Door"], answer:1},
   ]},
  {subject:"Math", title:"Skip Counting by 2s, 5s, and 10s", summary:"Ontario Algebra strand: skip counting helps see number patterns and prepares for multiplication.",
   resourceLabel:"YouTube: Skip Counting by 2s, 5s, and 10s", resourceUrl:"https://www.youtube.com/results?search_query=Skip%20Counting%20by%202s%2C%205s%2C%20and%2010s%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=DS3W9WLIxlQ",
   quiz:[
     {q:"Count by 2s: 2, 4, 6, __?", options:["7","9","10","8"], answer:3},
     {q:"Count by 5s: 5, 10, 15, __?", options:["25","20","18","16"], answer:1},
     {q:"Count by 10s: 10, 20, 30, __?", options:["35","45","50","40"], answer:3},
     {q:"Which set of numbers is skip counting by 5s?", options:["2,4,6,8","5,10,15,20","1,2,3,4","10,20,40,80"], answer:1},
     {q:"What comes next: 6, 8, 10, __?", options:["14","13","11","12"], answer:3},
   ]},
  {subject:"Science", title:"Air and Water in the Environment", summary:"Ontario Earth & Space Systems strand for Grade 2: air and water are essential resources found all around us and need to be kept clean.",
   resourceLabel:"YouTube: Air and Water in the Environment", resourceUrl:"https://www.youtube.com/results?search_query=Air%20and%20Water%20in%20the%20Environment%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=h7rhOM2dXtE",
   quiz:[
     {q:"Why is clean water important?", options:["Living things need it to survive","It is not important","Only for swimming","No reason"], answer:0},
     {q:"Which of these can pollute the air?", options:["Smoke from factories or cars","Fresh wind","Clouds","Rain"], answer:0},
     {q:"What is one way to help keep water clean?", options:["Ignoring spills","Not littering near water","Dumping garbage in rivers","Wasting water"], answer:1},
     {q:"We can't see air, but we know it's there because...", options:["We can feel wind","It is solid","It has a colour","It never moves"], answer:0},
     {q:"Which is a way to conserve (save) water?", options:["Turning off the tap when not using it","Ignoring leaks","Leaving the tap running","Wasting water on purpose"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Rules and Responsibilities", summary:"Rules and laws keep people safe and help communities run smoothly and fairly.",
   resourceLabel:"YouTube: Rules and Responsibilities", resourceUrl:"https://www.youtube.com/results?search_query=Rules%20and%20Responsibilities%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=5dtuZkposkk",
   quiz:[
     {q:"Why do we have rules?", options:["To make things confusing","To keep people safe and fair","No reason","To stop fun"], answer:1},
     {q:"A rule at school might be...", options:["Ignore the teacher","Run in the halls","Raise your hand to speak","Yell during class"], answer:2},
     {q:"A law is a rule made by...", options:["A pet","The government","Nobody","One kid"], answer:1},
     {q:"A responsibility is something you...", options:["Can ignore","Should take care of or do","Never have to do","Only an adult can have"], answer:1},
     {q:"Traffic lights help...", options:["Keep cars and people safe","Decorate the street","Make noise","Confuse drivers"], answer:0},
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"Language", title:"Finding the Main Idea", summary:"The main idea is what a story or text is mostly about.",
   resourceLabel:"YouTube: Finding the Main Idea", resourceUrl:"https://www.youtube.com/results?search_query=Finding%20the%20Main%20Idea%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=xJGQIYU_xhs",
   quiz:[
     {q:"The main idea of a story is...", options:["The title only","What the story is mostly about","A small detail","The last word"], answer:1},
     {q:"If a story is about a dog learning tricks, the main idea is about...", options:["A house","A dog learning tricks","The weather","A car"], answer:1},
     {q:"Details in a story...", options:["Are always wrong","Support and explain the main idea","Replace the main idea","Have nothing to do with the main idea"], answer:1},
     {q:"A good title usually hints at...", options:["The author's age","The main idea","A random word","Nothing"], answer:1},
     {q:"To find the main idea, you should...", options:["Think about what most of it is about","Skip reading","Guess randomly","Read only the last sentence"], answer:0},
   ]},
  {subject:"Math", title:"Comparing and Ordering Numbers", summary:"Use greater than, less than, and equal to in order to compare numbers up to 100.",
   resourceLabel:"YouTube: Comparing and Ordering Numbers", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20and%20Ordering%20Numbers%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=I_USfjnTLSY",
   quiz:[
     {q:"Which symbol means 'greater than'?", options:["<",">","+","="], answer:1},
     {q:"Which is true: 45 ___ 54", options:["45 > 54","45 < 54","45 = 54","Cannot compare"], answer:1},
     {q:"Put these in order from smallest to largest: 12, 8, 19", options:["8, 12, 19","8, 19, 12","19, 12, 8","12, 8, 19"], answer:0},
     {q:"Which number is the largest: 67, 76, 61?", options:["67","76","They are equal","61"], answer:1},
     {q:"23 ___ 23 — which symbol fits?", options:[">","=","<","+"], answer:1},
   ]},
  {subject:"Science", title:"Pushes and Pulls", summary:"Forces like pushes and pulls make objects start moving, stop moving, speed up, slow down, or change direction.",
   resourceLabel:"YouTube: Pushes and Pulls", resourceUrl:"https://www.youtube.com/results?search_query=Pushes%20and%20Pulls%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zI-vmLrBQzU",
   quiz:[
     {q:"Opening a door is an example of a...", options:["Liquid","Push or pull","Habitat","Tradition"], answer:1},
     {q:"A push can make an object...", options:["Move away from you","Grow","Disappear","Become a liquid"], answer:0},
     {q:"A pull can make an object...", options:["Change colour","Disappear","Become heavier","Move toward you"], answer:3},
     {q:"Which is an example of a pull?", options:["Kicking a ball","Dropping a book","Throwing a ball","Pulling a wagon"], answer:3},
     {q:"Forces can make a moving object...", options:["Speed up or slow down","Become a solid","Disappear","Never change"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Jobs and Community Helpers", summary:"People in a community have different jobs that help everyone — like firefighters, teachers, and doctors.",
   resourceLabel:"YouTube: Jobs and Community Helpers", resourceUrl:"https://www.youtube.com/results?search_query=Jobs%20and%20Community%20Helpers%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=wlBC2ljoGAk",
   quiz:[
     {q:"Who helps put out fires?", options:["Pilots","Firefighters","Teachers","Bakers"], answer:1},
     {q:"Who helps you learn at school?", options:["Teachers","Farmers","Doctors","Firefighters"], answer:0},
     {q:"A farmer's job helps provide...", options:["Fire safety","Mail only","Education only","Food"], answer:3},
     {q:"Why are community helpers important?", options:["They provide services everyone needs","No reason","They are not important","They only help themselves"], answer:0},
     {q:"Which job helps deliver mail and packages?", options:["Mail carrier","Dentist","Chef","Pilot"], answer:0},
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"Language", title:"Sequencing Events", summary:"Sequencing means putting events in the order they happened — first, next, then, last.",
   resourceLabel:"YouTube: Sequencing Events", resourceUrl:"https://www.youtube.com/results?search_query=Sequencing%20Events%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4AMptAmS_xM",
   quiz:[
     {q:"Which word usually signals the FIRST event?", options:["Then","First","Finally","Last"], answer:1},
     {q:"Which word usually signals the LAST event?", options:["Then","Next","Finally","First"], answer:2},
     {q:"Why is sequencing important when reading a story?", options:["It replaces the main idea","It changes the ending","It is not important","It shows the order of events"], answer:3},
     {q:"In a recipe, sequencing tells you...", options:["The price of food","Nothing useful","What order to do steps in","The color of the food"], answer:2},
     {q:"Which set is in correct time order?", options:["Lunch, dinner, breakfast","Breakfast, lunch, dinner","Dinner, breakfast, lunch","Lunch, breakfast, dinner"], answer:1},
   ]},
  {subject:"Math", title:"Telling Time to the Hour and Half Hour", summary:"Ontario Spatial Sense / Measurement: read clocks to tell time to the hour and half hour.",
   resourceLabel:"YouTube: Telling Time to the Hour and Half Hour", resourceUrl:"https://www.youtube.com/results?search_query=Telling%20Time%20to%20the%20Hour%20and%20Half%20Hour%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=MaVgBjVh4b8",
   quiz:[
     {q:"When the minute hand points to 12 and hour hand points to 3, the time is...", options:["12:00","3:00","6:00","9:00"], answer:1},
     {q:"When the minute hand points to 6, how many minutes past the hour is it?", options:["45","30","60","15"], answer:1},
     {q:"How many minutes are in one hour?", options:["100","45","60","30"], answer:2},
     {q:"What time is 'half past 4'?", options:["4:15","4:45","4:30","4:00"], answer:2},
     {q:"The short hand on a clock shows the...", options:["Seconds","Minutes","Day","Hours"], answer:3},
   ]},
  {subject:"Science", title:"Changes in Matter: Melting and Freezing", summary:"Matter can change state — solids can melt into liquids, and liquids can freeze into solids.",
   resourceLabel:"YouTube: Changes in Matter: Melting and Freezing", resourceUrl:"https://www.youtube.com/results?search_query=Changes%20in%20Matter%3A%20Melting%20and%20Freezing%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ZnizM4qb06I",
   quiz:[
     {q:"What happens to ice when it gets warm?", options:["Nothing happens","It melts into water","It disappears completely","It becomes a gas instantly"], answer:1},
     {q:"What happens to water when it gets very cold?", options:["It freezes into ice","It disappears","Nothing happens","It becomes a gas"], answer:0},
     {q:"Melting changes a...", options:["Gas into a solid","Solid into a liquid","Liquid into nothing","Liquid into a solid"], answer:1},
     {q:"Freezing changes a...", options:["Solid into a gas","Liquid into a solid","Gas into a liquid","Solid into a liquid"], answer:1},
     {q:"Which is an example of melting?", options:["A rock staying a rock","An ice cream cone melting in the sun","A cloud forming","Water turning to ice in a freezer"], answer:1},
   ]},
  {subject:"SocialStudies", title:"Finding Directions on a Map", summary:"Maps use symbols, a compass rose, and directions (N, S, E, W) to help people find their way.",
   resourceLabel:"YouTube: Finding Directions on a Map", resourceUrl:"https://www.youtube.com/results?search_query=Finding%20Directions%20on%20a%20Map%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mtsx8V3mE8o",
   quiz:[
     {q:"A compass rose on a map shows...", options:["Directions like North, South, East, West","The population","The weather","Nothing useful"], answer:0},
     {q:"Which direction is opposite of North?", options:["East","Up","South","West"], answer:2},
     {q:"Map symbols are explained in the...", options:["Border","Title","Compass rose","Legend (key)"], answer:3},
     {q:"If you are facing North and turn around, you now face...", options:["West","East","North","South"], answer:3},
     {q:"Why are symbols used on maps?", options:["To show real things simply","To take up space","To confuse readers","No reason"], answer:0},
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"Language", title:"Rhyming Words and Syllables", summary:"Rhyming words end with the same sound, and syllables are the beats in a word.",
   resourceLabel:"YouTube: Rhyming Words and Syllables", resourceUrl:"https://www.youtube.com/results?search_query=Rhyming%20Words%20and%20Syllables%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=9S7DY2lgJlU",
   quiz:[
     {q:"Which word rhymes with 'cat'?", options:["Hat","Dog","Sun","Cup"], answer:0},
     {q:"How many syllables are in the word 'elephant'?", options:["3","4","1","2"], answer:0},
     {q:"Which word rhymes with 'jump'?", options:["Jam","Cat","Stump","Sit"], answer:2},
     {q:"How many syllables are in 'dog'?", options:["2","1","4","3"], answer:1},
     {q:"Which pair of words rhymes?", options:["Cake / Cup","Cake / Lake","Cake / Dog","Cake / Run"], answer:1},
   ]},
  {subject:"Math", title:"2D Shapes and 3D Shapes", summary:"Ontario Spatial Sense strand: identify and describe 2D shapes (flat) and 3D shapes (solid).",
   resourceLabel:"YouTube: 2D Shapes and 3D Shapes", resourceUrl:"https://www.youtube.com/results?search_query=2D%20Shapes%20and%203D%20Shapes%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ux_kLd7qAcY",
   quiz:[
     {q:"How many sides does a triangle have?", options:["2","4","3","5"], answer:2},
     {q:"Which of these is a 3D shape?", options:["Circle","Square","Cube","Triangle"], answer:2},
     {q:"How many sides does a rectangle have?", options:["3","4","6","2"], answer:1},
     {q:"A sphere looks like a...", options:["Cone","Triangle","Ball","Box"], answer:2},
     {q:"Which shape has no corners?", options:["Rectangle","Circle","Triangle","Square"], answer:1},
   ]},
  {subject:"Science", title:"Weather and Seasons", summary:"Weather changes day to day, and the four seasons (spring, summer, fall, winter) bring different patterns of weather.",
   resourceLabel:"YouTube: Weather and Seasons", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20and%20Seasons%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4HeeCYVqf3U",
   quiz:[
     {q:"How many seasons are there in a year?", options:["5","4","2","3"], answer:1},
     {q:"Which season usually comes after winter?", options:["Summer","Winter again","Spring","Fall"], answer:2},
     {q:"What might you wear in a cold winter?", options:["Shorts only","Nothing extra","Warm coat and mittens","Swimsuit"], answer:2},
     {q:"Weather can include...", options:["Nothing changeable","Rain, snow, wind, and sunshine","Only sunshine","Only rain"], answer:1},
     {q:"In fall, what often happens to leaves on many trees?", options:["Nothing changes","They turn blue","They grow bigger only","They turn colours and fall off"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Comparing Communities", summary:"Communities can be urban (city), suburban, or rural (countryside), each with different features and ways of life.",
   resourceLabel:"YouTube: Comparing Communities", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Communities%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"A city is an example of a...", options:["Urban community","A planet","Rural community","Neither"], answer:0},
     {q:"A rural community is usually...", options:["Very crowded with tall buildings","On the moon","In the countryside with farms","Underwater"], answer:2},
     {q:"Which is more likely found in a city?", options:["No people at all","Tall buildings and many people","No buildings","Large open farm fields only"], answer:1},
     {q:"Why might people choose to live in a rural area?", options:["No reason","To be near tall skyscrapers only","For open space and farming","Because cities don't exist"], answer:2},
     {q:"Urban, suburban, and rural are all types of...", options:["Weather","Communities","Maps","Animals"], answer:1},
   ]},
]},
{day:10, label:"Day 10 — Fri (Review)", reviewNote:"Final review day: a mix of everything from the two weeks, getting ready for September.", subjects:[
  {subject:"Language", title:"Final Review: Language Skills", summary:"Mixed review of vowels, nouns, verbs, adjectives, main idea, sequencing, and rhyming.",
   resourceLabel:"YouTube: Final Review: Language Skills", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Language%20Skills%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=o73GnZotE_Y",
   quiz:[
     {q:"Which word is an adjective?", options:["Jump","Big","Run","Quickly"], answer:1},
     {q:"What is the main idea of a story?", options:["The title only","A small detail","What it's mostly about","The last word"], answer:2},
     {q:"Which word signals the first event in a sequence?", options:["Finally","Then","First","Last"], answer:2},
     {q:"Which word rhymes with 'hat'?", options:["Dog","Cat","Sun","Cup"], answer:1},
     {q:"In 'The big dog barked loudly,' which word is the verb?", options:["Barked","Big","Dog","Loudly"], answer:0},
   ]},
  {subject:"Math", title:"Final Review: Math Skills", summary:"Mixed review of addition, subtraction, place value, skip counting, comparing numbers, time, and shapes.",
   resourceLabel:"YouTube: Final Review: Math Skills", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Math%20Skills%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=joHaCejRnmo",
   quiz:[
     {q:"9 + 8 = ?", options:["18","16","15","17"], answer:3},
     {q:"14 - 6 = ?", options:["6","7","9","8"], answer:3},
     {q:"Count by 10s: 40, 50, __?", options:["55","70","65","60"], answer:3},
     {q:"Which is greater: 58 or 85?", options:["58","Can't tell","85","Equal"], answer:2},
     {q:"How many sides does a triangle have?", options:["3","2","5","4"], answer:0},
   ]},
  {subject:"Science", title:"Final Review: Science Skills", summary:"Mixed review of living things, life cycles, matter, forces, weather, and air/water.",
   resourceLabel:"YouTube: Final Review: Science Skills", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Science%20Skills%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4VapPTbbGkA",
   quiz:[
     {q:"Which is a living thing?", options:["Tree","Rock","Chair","Cloud"], answer:0},
     {q:"A push or pull is an example of a...", options:["Liquid","Season","Force","Tradition"], answer:2},
     {q:"What happens when ice melts?", options:["It becomes heavier","It becomes a gas instantly","It becomes water","Nothing"], answer:2},
     {q:"How many seasons are in a year?", options:["2","4","3","5"], answer:1},
     {q:"Why is clean water important?", options:["Living things need it","It isn't important","No reason","Only for swimming"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Final Review: Social Studies Skills", summary:"Mixed review of community, traditions, maps, rules, jobs, and types of communities.",
   resourceLabel:"YouTube: Final Review: Social Studies Skills", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Social%20Studies%20Skills%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4Ub0dIC4ezw",
   quiz:[
     {q:"A community is a group of people who...", options:["Live and help each other","Only work","Never meet","Live alone"], answer:0},
     {q:"What does a map legend explain?", options:["Nothing","A story","Symbols on the map","The weather"], answer:2},
     {q:"Who helps put out fires in a community?", options:["Pilots","Teachers","Farmers","Firefighters"], answer:3},
     {q:"A rural community is usually...", options:["On the moon","A big crowded city","Underwater","The countryside with farms"], answer:3},
     {q:"Why do communities have rules?", options:["No reason","To keep people safe and fair","To confuse people","To stop fun"], answer:1},
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"Language", title:"Compound Words", summary:"A compound word is two smaller words joined together to make a new word, like sun + flower = sunflower or rain + bow = rainbow.",
   resourceLabel:"YouTube: Compound Words", resourceUrl:"https://www.youtube.com/results?search_query=Compound%20Words%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=82G-ZWzUHhU",
   quiz:[
     {q:"Which word is a compound word?", options:["Sunflower","Running","Beautiful","Quickly"], answer:0},
     {q:"What two words make up 'cupcake'?", options:["Cup + cup","Cu + pcake","Cup + cake","Cupc + ake"], answer:2},
     {q:"Which two words join to make 'raincoat'?", options:["Ran + coat","Rain + cat","Rain + coat","Rain + oat"], answer:2},
     {q:"Which is a compound word?", options:["Bedroom","Quickly","Happily","Sleeping"], answer:0},
     {q:"What compound word do 'tooth' and 'brush' make?", options:["Toobrush","Toothbrush","Brushooth","Teethbrush"], answer:1},
   ]},
  {subject:"Math", title:"Addition Within 100 (No Regrouping)", summary:"We can add two-digit numbers by adding the tens together and the ones together, like 32 + 15 = 47.",
   resourceLabel:"YouTube: Addition Within 100 (No Regrouping)", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20Within%20100%20%28No%20Regrouping%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=c4xw9DqOKH4",
   quiz:[
     {q:"23 + 14 = ?", options:["36","38","37","27"], answer:2},
     {q:"41 + 25 = ?", options:["64","65","56","66"], answer:3},
     {q:"30 + 47 = ?", options:["17","77","78","76"], answer:1},
     {q:"52 + 16 = ?", options:["67","69","68","58"], answer:2},
     {q:"61 + 28 = ?", options:["88","79","89","90"], answer:2},
   ]},
  {subject:"Science", title:"What Plants Need to Grow", summary:"Plants need four things to grow: sunlight, water, soil (nutrients), and air. Without any of these, a plant cannot stay healthy.",
   resourceLabel:"YouTube: What Plants Need to Grow", resourceUrl:"https://www.youtube.com/results?search_query=What%20Plants%20Need%20to%20Grow%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=u46A0WKp2nk",
   quiz:[
     {q:"Which of these do plants need to grow?", options:["Wind only","Darkness only","Rocks to eat","Sunlight"], answer:3},
     {q:"What do plants take in through their roots?", options:["Nothing","Sunlight","Air only","Water and nutrients from soil"], answer:3},
     {q:"A plant kept in the dark will most likely...", options:["Get bigger leaves","Stop growing and become unhealthy","Grow extra fast","Bloom more flowers"], answer:1},
     {q:"What do leaves use sunlight to do?", options:["Make the plant walk","Make food for the plant","Keep the plant warm only","Nothing"], answer:1},
     {q:"Which of these is NOT something a plant needs?", options:["A television","Sunlight","Water","Soil"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Symbols of Canada", summary:"Canada has special symbols that represent who we are as a country — like the maple leaf, the Canadian flag, and our national anthem 'O Canada'.",
   resourceLabel:"YouTube: Symbols of Canada", resourceUrl:"https://www.youtube.com/results?search_query=Symbols%20of%20Canada%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=38BGXJ572Y8",
   quiz:[
     {q:"What leaf is a symbol of Canada?", options:["Fern leaf","Oak leaf","Pine needle","Maple leaf"], answer:3},
     {q:"What are the two colours on the Canadian flag?", options:["Blue and white","Green and white","Red and blue","Red and white"], answer:3},
     {q:"What is the name of Canada's national anthem?", options:["O Canada","Star-Spangled Banner","The Maple Leaf Forever","God Save the King"], answer:0},
     {q:"A national symbol is something that...", options:["Belongs to one person","Has no meaning","Is a secret","Represents the whole country"], answer:3},
     {q:"The beaver is also a symbol of Canada because it represents...", options:["Hard work","Laziness","Speed","Flying"], answer:0},
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"Language", title:"Contractions", summary:"A contraction is two words joined together with an apostrophe (') to replace missing letters, like do + not = don't, or I + am = I'm.",
   resourceLabel:"YouTube: Contractions", resourceUrl:"https://www.youtube.com/results?search_query=Contractions%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=gubPH3WEurg",
   quiz:[
     {q:"What is the contraction for 'do not'?", options:["do'nt","don't","dont","dn't"], answer:1},
     {q:"What two words make up 'I'm'?", options:["I + mine","I + am","I + me","I + my"], answer:1},
     {q:"What does the apostrophe (') in a contraction represent?", options:["A period","Extra words","Missing letters","A comma"], answer:2},
     {q:"What is the contraction for 'can not'?", options:["cant","cann't","can't","ca'nt"], answer:2},
     {q:"Which is the correct contraction for 'they are'?", options:["theyre","theyare","they're","ther're"], answer:2},
   ]},
  {subject:"Math", title:"Subtraction Within 100 (No Regrouping)", summary:"We can subtract two-digit numbers by taking away the tens and the ones separately, like 57 - 23 = 34.",
   resourceLabel:"YouTube: Subtraction Within 100 (No Regrouping)", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20Within%20100%20%28No%20Regrouping%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ds226Vh7epg",
   quiz:[
     {q:"57 - 23 = ?", options:["35","24","33","34"], answer:3},
     {q:"86 - 42 = ?", options:["54","45","43","44"], answer:3},
     {q:"79 - 35 = ?", options:["43","34","45","44"], answer:3},
     {q:"95 - 61 = ?", options:["44","33","34","35"], answer:2},
     {q:"68 - 14 = ?", options:["54","53","64","55"], answer:0},
   ]},
  {subject:"Science", title:"Animal Habitats", summary:"An animal's habitat is the place where it lives and finds food, water, and shelter. Different animals live in different habitats like forests, oceans, and the arctic.",
   resourceLabel:"YouTube: Animal Habitats", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Habitats%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Xj1ASC-TlsI",
   quiz:[
     {q:"A polar bear's habitat is the...", options:["Ocean only","Arctic (cold, snowy)","Desert","Tropical rainforest"], answer:1},
     {q:"Fish live in a __ habitat.", options:["Arctic only","Desert","Forest","Water/ocean"], answer:3},
     {q:"What does an animal get from its habitat?", options:["Nothing","Food, water, and shelter","Only water","Only food"], answer:1},
     {q:"A squirrel lives in a __ habitat.", options:["Ocean","Desert","Arctic","Forest"], answer:3},
     {q:"If a habitat is destroyed, the animals that live there may...", options:["Get more food","Grow bigger","Not be affected at all","Struggle to survive or have to move"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Indigenous Peoples and First Nations of Canada", summary:"Canada is home to many Indigenous peoples — the First Nations, Métis, and Inuit — who have lived on this land for thousands of years and have rich cultures and traditions.",
   resourceLabel:"YouTube: Indigenous Peoples and First Nations of Canada", resourceUrl:"https://www.youtube.com/results?search_query=Indigenous%20Peoples%20and%20First%20Nations%20of%20Canada%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Qo7aTFHyhPE",
   quiz:[
     {q:"Who were the first people to live in Canada?", options:["British settlers","French settlers","American explorers","Indigenous peoples"], answer:3},
     {q:"The word 'Indigenous' means...", options:["New to a place","From another country","Living in cities only","Originally from a place"], answer:3},
     {q:"Why is it important to learn about Indigenous cultures?", options:["To copy them exactly","It is not important","Because they are all the same","To respect Canada's history"], answer:3},
     {q:"The Inuit people traditionally lived in which part of Canada?", options:["The arctic north","The southern farmlands","The tropical rainforest","The Pacific islands"], answer:0},
     {q:"Traditional Indigenous knowledge often includes...", options:["Caring for land and storytelling","Modern factory work","Nothing about nature","How to use computers"], answer:0},
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"Language", title:"Synonyms", summary:"Synonyms are words that mean the same or nearly the same thing, like happy and glad, or big and large.",
   resourceLabel:"YouTube: Synonyms", resourceUrl:"https://www.youtube.com/results?search_query=Synonyms%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=hFFW9zKJ5os",
   quiz:[
     {q:"Which word is a synonym for 'happy'?", options:["Tired","Angry","Sad","Glad"], answer:3},
     {q:"Which word means the same as 'big'?", options:["Large","Tiny","Little","Small"], answer:0},
     {q:"Which word is a synonym for 'fast'?", options:["Slow","Calm","Quick","Quiet"], answer:2},
     {q:"Choose the synonym for 'start'?", options:["Finish","Stop","End","Begin"], answer:3},
     {q:"Which word has the same meaning as 'scared'?", options:["Calm","Afraid","Brave","Happy"], answer:1},
   ]},
  {subject:"Math", title:"Counting Coins", summary:"Canadian coins have different values: a penny = 1¢, a nickel = 5¢, a dime = 10¢, and a quarter = 25¢. We can add them together to find the total.",
   resourceLabel:"YouTube: Counting Coins", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20Coins%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=MbtmucV-U2c",
   quiz:[
     {q:"How much is one quarter worth?", options:["25¢","10¢","5¢","1¢"], answer:0},
     {q:"How much is one dime worth?", options:["25¢","10¢","5¢","1¢"], answer:1},
     {q:"What is the total value of 2 nickels?", options:["15¢","5¢","2¢","10¢"], answer:3},
     {q:"Which coins make exactly 15¢?", options:["One quarter","Two dimes","One dime and one nickel","Three pennies"], answer:2},
     {q:"How many pennies equal one nickel?", options:["10","1","5","2"], answer:2},
   ]},
  {subject:"Science", title:"The Five Senses", summary:"We learn about the world using our five senses: sight (eyes), hearing (ears), smell (nose), taste (tongue), and touch (skin).",
   resourceLabel:"YouTube: The Five Senses", resourceUrl:"https://www.youtube.com/results?search_query=The%20Five%20Senses%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=q1xNuU7gaAQ",
   quiz:[
     {q:"Which sense do you use to see a rainbow?", options:["Hearing","Touch","Sight","Smell"], answer:2},
     {q:"Which body part do you use for the sense of hearing?", options:["Tongue","Eyes","Nose","Ears"], answer:3},
     {q:"Which sense helps you know if food tastes sweet?", options:["Sight","Taste","Touch","Smell"], answer:1},
     {q:"How many senses do humans have?", options:["4","5","6","3"], answer:1},
     {q:"Which sense would tell you that something is rough or smooth?", options:["Taste","Sight","Touch","Hearing"], answer:2},
   ]},
  {subject:"SocialStudies", title:"How Communities Change Over Time", summary:"Communities change over time — buildings get built or torn down, technology changes, and people's ways of life are different from long ago.",
   resourceLabel:"YouTube: How Communities Change Over Time", resourceUrl:"https://www.youtube.com/results?search_query=How%20Communities%20Change%20Over%20Time%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=FnF5I3_q0H4",
   quiz:[
     {q:"Long ago, how did most people travel?", options:["By car","By airplane","By subway","By horse, walking, or boat"], answer:3},
     {q:"How have communities changed over time?", options:["Buildings and technology have changed","They haven't changed at all","Only the weather changed","Communities disappear and reappear"], answer:0},
     {q:"An old photograph of a town helps us understand...", options:["What it looks like now","Nothing useful","The future","What it looked like in the past"], answer:3},
     {q:"Which of these is a modern invention that changed communities?", options:["Electricity and the internet","Horse and carriage","A wooden plow","Oil lamps"], answer:0},
     {q:"Why is it helpful to learn about how communities changed?", options:["It helps us see how things improved","It is not helpful","To copy the past exactly","No reason"], answer:0},
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"Language", title:"Antonyms", summary:"Antonyms are words that mean the opposite, like hot and cold, or up and down.",
   resourceLabel:"YouTube: Antonyms", resourceUrl:"https://www.youtube.com/results?search_query=Antonyms%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=wKEKEVHpwkk",
   quiz:[
     {q:"What is the antonym (opposite) of 'hot'?", options:["Frozen","Cool","Warm","Cold"], answer:3},
     {q:"Which word is the opposite of 'up'?", options:["Over","Down","Above","High"], answer:1},
     {q:"What is the antonym of 'happy'?", options:["Sad","Cheerful","Joyful","Glad"], answer:0},
     {q:"Which word is the opposite of 'fast'?", options:["Speedy","Quick","Slow","Swift"], answer:2},
     {q:"What is the antonym of 'start'?", options:["Open","Launch","Begin","Finish"], answer:3},
   ]},
  {subject:"Math", title:"Measuring Length with Non-Standard Units", summary:"We can measure how long things are using non-standard units like paper clips, cubes, or hand spans — then count how many units fit.",
   resourceLabel:"YouTube: Measuring Length with Non-Standard Units", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Length%20with%20Non-Standard%20Units%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2wUsdsae0ro",
   quiz:[
     {q:"If a pencil is 8 paper clips long, and a book is 12 paper clips long, which is longer?", options:["Pencil","Book","Cannot tell","They are the same"], answer:1},
     {q:"Why do we need to use the SAME unit when comparing lengths?", options:["To make it harder","Because units are the same always","So measurements are fair and accurate","No reason"], answer:2},
     {q:"A non-standard unit for measuring could be...", options:["A centimeter ruler","A paper clip","A scale","A thermometer"], answer:1},
     {q:"If a table is 20 cubes long and a shelf is 15 cubes long, how many more cubes long is the table?", options:["4","5","35","6"], answer:1},
     {q:"When measuring length, you should line up your units...", options:["In a circle","With gaps between them","End to end in a straight line","Randomly"], answer:2},
   ]},
  {subject:"Science", title:"Ramps and Inclined Planes", summary:"A ramp (inclined plane) is a simple machine that makes it easier to move things up or down. The less steep the ramp, the easier it is to push something up.",
   resourceLabel:"YouTube: Ramps and Inclined Planes", resourceUrl:"https://www.youtube.com/results?search_query=Ramps%20and%20Inclined%20Planes%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=3COvm0TtxWg",
   quiz:[
     {q:"A ramp is also called an...", options:["Lever","Pulley","Inclined plane","Wheel"], answer:2},
     {q:"What does a ramp help you do?", options:["Move things up or down more easily","Add colour","Create sound","Make things disappear"], answer:3},
     {q:"A wheelchair ramp helps people...", options:["Add decoration","Make noise","Go faster","Move up steps without climbing"], answer:3},
     {q:"If you make a ramp less steep (lower angle), it becomes...", options:["Impossible to use","The same difficulty","Harder to push something up","Easier to push something up"], answer:3},
     {q:"Which of these is an example of using a ramp?", options:["Pushing a box down a slide","Hitting a ball with a bat","Pouring water","Pulling a rope"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Needs vs. Wants", summary:"Needs are things we must have to survive, like food, water, clothing, and shelter. Wants are things we would like to have but do not need to survive, like toys or candy.",
   resourceLabel:"YouTube: Needs vs. Wants", resourceUrl:"https://www.youtube.com/results?search_query=Needs%20vs.%20Wants%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=aRcXutXvfmM",
   quiz:[
     {q:"Which of these is a NEED?", options:["Food","Candy","Toys","Video games"], answer:0},
     {q:"Which of these is a WANT?", options:["Shelter","Water","Clothing","New sneakers"], answer:3},
     {q:"Why is clean water a need?", options:["Because our bodies need it to survive","Because it tastes sweet","Because it is fun","Because everyone wants it"], answer:0},
     {q:"Which is the best description of a 'want'?", options:["Something you must have to live","Something free","Something every person owns","Something nice but not essential"], answer:3},
     {q:"A home to live in is an example of a...", options:["Toy","Want","Need","Luxury"], answer:2},
   ]},
]},
{day:15, label:"Day 15 — Fri (Review)", reviewNote:"Week 3 review — mixed questions from Days 11–14", subjects:[
  {subject:"Language", title:"Review: Compound Words, Contractions, Synonyms & Antonyms", summary:"Mixed review of compound words, contractions, synonyms, and antonyms.",
   resourceLabel:"YouTube: Review: Compound Words, Contractions, Synonyms & Antonyms", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Compound%20Words%2C%20Contractions%2C%20Synonyms%20%26%20Antonyms%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PDI2xlOBcM4",
   quiz:[
     {q:"Which word is a compound word?", options:["Beautiful","Running","Bedroom","Slowly"], answer:2},
     {q:"What is the contraction for 'I am'?", options:["I'am","Im","Iam","I'm"], answer:3},
     {q:"Which word is a synonym for 'big'?", options:["Little","Tiny","Large","Small"], answer:2},
     {q:"What is the antonym of 'hot'?", options:["Boiling","Cold","Warm","Steamy"], answer:1},
     {q:"What does the apostrophe in 'don't' represent?", options:["Nothing","Extra letters","A period","Missing letters"], answer:3},
   ]},
  {subject:"Math", title:"Review: Addition, Subtraction, Coins & Measuring", summary:"Mixed review of two-digit addition, two-digit subtraction, counting coins, and measuring with non-standard units.",
   resourceLabel:"YouTube: Review: Addition, Subtraction, Coins & Measuring", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Addition%2C%20Subtraction%2C%20Coins%20%26%20Measuring%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=BxrzwF6oV6s",
   quiz:[
     {q:"34 + 23 = ?", options:["58","57","56","67"], answer:1},
     {q:"76 - 42 = ?", options:["44","34","33","35"], answer:1},
     {q:"How much is one quarter worth?", options:["10¢","5¢","50¢","25¢"], answer:3},
     {q:"Which coin is worth 10¢?", options:["Nickel","Penny","Dime","Quarter"], answer:2},
     {q:"When measuring with non-standard units, you should line units...", options:["With big gaps","In a circle","End to end in a straight line","Randomly"], answer:2},
   ]},
  {subject:"Science", title:"Review: Plants, Habitats, Senses & Ramps", summary:"Mixed review of what plants need, animal habitats, the five senses, and inclined planes.",
   resourceLabel:"YouTube: Review: Plants, Habitats, Senses & Ramps", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Plants%2C%20Habitats%2C%20Senses%20%26%20Ramps%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=kBL9-RFhnbM",
   quiz:[
     {q:"What do plants need to grow?", options:["Sunlight, water, soil, and air","Nothing special","Only water","Darkness, salt, and stones"], answer:0},
     {q:"A polar bear lives in which habitat?", options:["Ocean only","Rainforest","Arctic","Desert"], answer:2},
     {q:"Which sense do you use your ears for?", options:["Touch","Sight","Hearing","Taste"], answer:2},
     {q:"A ramp is also called an...", options:["Inclined plane","Pulley","Lever","Gear"], answer:0},
     {q:"How many senses do humans have?", options:["4","3","5","6"], answer:2},
   ]},
  {subject:"SocialStudies", title:"Review: Canada Symbols, Indigenous Peoples, Change & Needs", summary:"Mixed review of Canadian symbols, Indigenous peoples, how communities change, and needs vs. wants.",
   resourceLabel:"YouTube: Review: Canada Symbols, Indigenous Peoples, Change & Needs", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Canada%20Symbols%2C%20Indigenous%20Peoples%2C%20Change%20%26%20Needs%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=glSIDAyyPJA",
   quiz:[
     {q:"What leaf is on the Canadian flag?", options:["Pine needle","Maple leaf","Fern","Oak leaf"], answer:1},
     {q:"Who were the first people to live in Canada?", options:["American explorers","Indigenous peoples","British settlers","French settlers"], answer:1},
     {q:"Which of these is a NEED?", options:["Toys","Video games","Shelter","Candy"], answer:2},
     {q:"How have communities changed over time?", options:["They stay exactly the same","No change at all","Only population changes","Technology and buildings change"], answer:3},
     {q:"What is Canada's national anthem called?", options:["Maple Leaf Forever","God Save the King","True North","O Canada"], answer:3},
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"Language", title:"Story Elements: Character, Setting, Plot", summary:"Every story has three main elements: characters (who is in the story), setting (where and when it happens), and plot (what happens — beginning, middle, end).",
   resourceLabel:"YouTube: Story Elements: Character, Setting, Plot", resourceUrl:"https://www.youtube.com/results?search_query=Story%20Elements%3A%20Character%2C%20Setting%2C%20Plot%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=1M0pFLXegG0",
   quiz:[
     {q:"The 'setting' of a story is...", options:["The lesson learned","What happens at the end","Who is in the story","Where and when the story happens"], answer:3},
     {q:"The 'characters' in a story are...", options:["The places in the story","The people or animals in the story","The time of day","The main problem"], answer:1},
     {q:"The 'plot' of a story is...", options:["The setting","What happens in the story","The title","The characters"], answer:1},
     {q:"In 'The Three Bears,' Goldilocks is a...", options:["Title","Plot","Character","Setting"], answer:2},
     {q:"A forest in winter is an example of a story's...", options:["Character","Setting","Plot","Lesson"], answer:1},
   ]},
  {subject:"Math", title:"Growing and Shrinking Patterns", summary:"In a growing pattern, something gets bigger each time (like 1, 3, 5, 7). In a shrinking pattern, something gets smaller each time (like 20, 17, 14, 11).",
   resourceLabel:"YouTube: Growing and Shrinking Patterns", resourceUrl:"https://www.youtube.com/results?search_query=Growing%20and%20Shrinking%20Patterns%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=JcNCfb0c8nc",
   quiz:[
     {q:"What comes next in this growing pattern: 2, 5, 8, 11, __?", options:["12","14","13","15"], answer:1},
     {q:"What kind of pattern is 20, 17, 14, 11?", options:["Repeating only","Random","Shrinking","Growing"], answer:2},
     {q:"What comes next in 30, 25, 20, 15, __?", options:["5","10","12","14"], answer:1},
     {q:"In the pattern 3, 6, 9, 12, the rule is...", options:["Add 2","Add 3","Add 4","Subtract 3"], answer:1},
     {q:"Which pattern is a GROWING pattern?", options:["9, 6, 3, 0","10, 8, 6, 4","2, 4, 6, 8","5, 4, 3, 2"], answer:2},
   ]},
  {subject:"Science", title:"Properties of Materials", summary:"Materials have properties that describe what they are like — hard or soft, rough or smooth, flexible or stiff, shiny or dull. These properties help us decide how to use them.",
   resourceLabel:"YouTube: Properties of Materials", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Materials%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=veUUii1U8-o",
   quiz:[
     {q:"Which word describes a surface you might feel on sandpaper?", options:["Smooth","Wet","Rough","Soft"], answer:2},
     {q:"A material that can bend without breaking is called...", options:["Flexible","Stiff","Heavy","Hard"], answer:0},
     {q:"Which material is best for making a drinking cup — something that is...?", options:["Flexible and stretchy","Waterproof and holds its shape","Rough and sharp","Melts in cold water"], answer:1},
     {q:"A property of a material is something you can...", options:["Only guess","Smell only","Observe or measure, like colour","Never describe"], answer:2},
     {q:"Which is a property of a metal spoon?", options:["Light and see-through","Rough and bendy","Soft and fluffy","Hard and shiny"], answer:3},
   ]},
  {subject:"SocialStudies", title:"How Money and Trading Work", summary:"Long ago, people traded goods they had for goods they needed (called bartering). Today, we use money — coins and bills — to buy and sell things in a fair way.",
   resourceLabel:"YouTube: How Money and Trading Work", resourceUrl:"https://www.youtube.com/results?search_query=How%20Money%20and%20Trading%20Work%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Z7hwaeaDk-I",
   quiz:[
     {q:"What is 'bartering'?", options:["Trading items without money","Saving money in a bank","Spending all your money","Buying things with coins"], answer:0},
     {q:"Why do we use money?", options:["Just for fun","As a fair way to buy and sell things","Because it is heavy","To fill piggy banks only"], answer:1},
     {q:"If you earn money, you have...", options:["Lost it","Borrowed it","Money earned from work or selling","Spent it already"], answer:2},
     {q:"Which of these is a Canadian coin?", options:["The Peso","The Euro","The Pound","The Dollar coin (Loonie)"], answer:3},
     {q:"Saving money means...", options:["Throwing it away","Giving it all away","Spending it all right away","Keeping some money to use later"], answer:3},
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"Language", title:"Plural Nouns (-s and -es)", summary:"A plural noun means more than one. Most nouns add -s (cats, books), but nouns ending in -s, -sh, -ch, or -x add -es (buses, boxes, lunches).",
   resourceLabel:"YouTube: Plural Nouns (-s and -es)", resourceUrl:"https://www.youtube.com/results?search_query=Plural%20Nouns%20%28-s%20and%20-es%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lD1OaD4FBqM",
   quiz:[
     {q:"What is the plural of 'cat'?", options:["Caties","Cates","Cats","Catses"], answer:2},
     {q:"What is the plural of 'box'?", options:["Box","Boxs","Boxies","Boxes"], answer:3},
     {q:"Which ending do you usually add to make a noun plural?", options:["-s or -es","-ed","-ing","-ly"], answer:0},
     {q:"What is the plural of 'bus'?", options:["Buses","Buss","Busies","Bus"], answer:0},
     {q:"What is the plural of 'lunch'?", options:["Lunches","Lunchies","Lunch","Lunchs"], answer:0},
   ]},
  {subject:"Math", title:"Fractions: Halves and Quarters", summary:"A fraction shows equal parts of a whole. When something is cut into 2 equal parts, each part is one half (1/2). When cut into 4 equal parts, each part is one quarter (1/4).",
   resourceLabel:"YouTube: Fractions: Halves and Quarters", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%3A%20Halves%20and%20Quarters%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=362JVVvgYPE",
   quiz:[
     {q:"If a pizza is cut into 2 equal pieces, each piece is...", options:["One whole","One third","One half","One quarter"], answer:2},
     {q:"If a square is cut into 4 equal parts, each part is...", options:["One whole","One quarter","One half","One third"], answer:1},
     {q:"What does the bottom number in a fraction tell you?", options:["The size of the shape","Nothing","How many parts are shaded","How many equal parts in the whole"], answer:3},
     {q:"Which fraction is bigger: 1/2 or 1/4?", options:["They are the same","Cannot compare","1/4","1/2"], answer:3},
     {q:"If you eat 1 out of 4 equal slices of an apple, you ate...", options:["1/4","1/1","1/3","1/2"], answer:0},
   ]},
  {subject:"Science", title:"Day, Night, and Shadows", summary:"The Earth rotates (spins), causing day and night. Shadows are made when something blocks light. Shadows change in length and direction through the day.",
   resourceLabel:"YouTube: Day, Night, and Shadows", resourceUrl:"https://www.youtube.com/results?search_query=Day%2C%20Night%2C%20and%20Shadows%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=3ydqMIvAWz4",
   quiz:[
     {q:"What causes day and night on Earth?", options:["The moon moving around Earth","The Earth rotating (spinning)","Clouds covering the sun","The sun moving around Earth"], answer:1},
     {q:"A shadow is formed when an object...", options:["Reflects light","Blocks light","Creates light","Absorbs all light perfectly"], answer:1},
     {q:"When is your shadow the shortest?", options:["Late afternoon","Early morning","Around noon (midday)","At night"], answer:2},
     {q:"Why does your shadow move during the day?", options:["The sun's position changes in the sky","The ground moves","You keep moving","Shadows are alive"], answer:0},
     {q:"At night, we cannot see our shadows because...", options:["There is little or no sunlight","Shadows disappear forever at night","We are too small","The Earth stops spinning"], answer:0},
   ]},
  {subject:"SocialStudies", title:"The Seven Continents and Five Oceans", summary:"Earth has seven continents (large land areas): Africa, Antarctica, Asia, Australia, Europe, North America, and South America. The five oceans are: Pacific, Atlantic, Indian, Southern, and Arctic.",
   resourceLabel:"YouTube: The Seven Continents and Five Oceans", resourceUrl:"https://www.youtube.com/results?search_query=The%20Seven%20Continents%20and%20Five%20Oceans%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=K6DSMZ8b3LE",
   quiz:[
     {q:"How many continents are there on Earth?", options:["8","5","6","7"], answer:3},
     {q:"Which continent do we live on in Canada?", options:["Asia","North America","Europe","South America"], answer:1},
     {q:"How many oceans are there on Earth?", options:["7","6","4","5"], answer:3},
     {q:"Which is the largest ocean?", options:["Pacific","Arctic","Atlantic","Indian"], answer:0},
     {q:"Which of these is a continent?", options:["Africa","Canada","France","Pacific Ocean"], answer:0},
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"Language", title:"Possessive Nouns", summary:"A possessive noun shows ownership. We add an apostrophe + s ('s) to a noun to show it belongs to someone, like 'the dog's bone' means the bone belongs to the dog.",
   resourceLabel:"YouTube: Possessive Nouns", resourceUrl:"https://www.youtube.com/results?search_query=Possessive%20Nouns%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=h7_aNX-wj9A",
   quiz:[
     {q:"Which sentence uses a possessive noun correctly?", options:["Dogs bone","The dogs bone","The dog's bone","The dogs' bone's"], answer:2},
     {q:"'Sara's hat' means...", options:["The hat belongs to Sara","A hat named Sara","Many hats","Sara is a hat"], answer:0},
     {q:"How do you show that a book belongs to Tom?", options:["Tom's book","Tom book","Book Tom","Toms book"], answer:0},
     {q:"What punctuation mark is used in a possessive noun?", options:["Apostrophe (')","Comma","Question mark","Period"], answer:0},
     {q:"Which is the possessive form of 'the cat'?", options:["The cat's","Cat's the","The's cat","The cats"], answer:0},
   ]},
  {subject:"Math", title:"Reading Pictographs and Bar Graphs", summary:"A pictograph uses pictures to show data, and a bar graph uses bars. Both have a title and labels to help us read the information.",
   resourceLabel:"YouTube: Reading Pictographs and Bar Graphs", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20Pictographs%20and%20Bar%20Graphs%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zF_dBk8EPDk",
   quiz:[
     {q:"What is a pictograph?", options:["A map of a picture","A type of calculator","A written story","A graph that uses pictures to show data"], answer:3},
     {q:"In a bar graph, a taller bar means...", options:["More of something","Less of something","Nothing special","The same as shorter bars"], answer:0},
     {q:"What does the title of a graph tell you?", options:["A story","The exact numbers","Nothing","What the graph is about"], answer:3},
     {q:"In a pictograph, each picture of a star represents 2 votes. If there are 4 stars, how many votes are there?", options:["8","4","6","2"], answer:0},
     {q:"Why do we use graphs?", options:["To organise and compare data easily","To draw pictures only","To write stories","To decorate pages"], answer:0},
   ]},
  {subject:"Science", title:"Light and Sound as Forms of Energy", summary:"Light and sound are both forms of energy. Light travels in straight lines and helps us see. Sound is made by vibrations and travels through air to reach our ears.",
   resourceLabel:"YouTube: Light and Sound as Forms of Energy", resourceUrl:"https://www.youtube.com/results?search_query=Light%20and%20Sound%20as%20Forms%20of%20Energy%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=cDaWohR_DVo",
   quiz:[
     {q:"What makes a sound?", options:["Light bouncing","Vibrations shaking back and forth","Hot air only","Only electricity"], answer:1},
     {q:"Light travels in...", options:["Curved lines only","Random directions only","Circles","Straight lines"], answer:3},
     {q:"Which of these produces light?", options:["A sound","A shadow","The sun and a light bulb","A rock"], answer:2},
     {q:"Why can we hear sound?", options:["Vibrations travel to our ears","Sound is visible","Our eyes pick it up","We create sound in our brains"], answer:0},
     {q:"Which is an example of a source of light?", options:["Silence","A shadow","A rock","A candle flame"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Caring for the Environment", summary:"We can help protect our environment by reducing waste, reusing things, recycling, and not polluting our air, water, or land. Everyone can help keep our planet healthy.",
   resourceLabel:"YouTube: Caring for the Environment", resourceUrl:"https://www.youtube.com/results?search_query=Caring%20for%20the%20Environment%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=X2YgM1Zw4_E",
   quiz:[
     {q:"What does 'recycling' mean?", options:["Buying more things","Burning old items","Throwing things in the garbage","Turning old materials into new products"], answer:3},
     {q:"Which action helps protect the environment?", options:["Littering","Turning off lights when not in use","Throwing garbage in rivers","Leaving taps running"], answer:1},
     {q:"The three R's that help the environment are...", options:["Reduce, Reuse, Recycle","Rain, Rocks, Rivers","Read, Run, Rest","Repeat, Replace, Rebuild"], answer:0},
     {q:"Why is it important to care for the environment?", options:["No real reason","It is not important","All living things depend on it","Only scientists care about it"], answer:2},
     {q:"Which of these would HARM the environment?", options:["Planting trees","Pouring chemicals into a lake","Picking up litter","Composting food scraps"], answer:1},
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"Language", title:"Question Words", summary:"Question words help us ask questions: Who (asks about a person), What (asks about a thing), Where (asks about a place), When (asks about a time), Why (asks about a reason), and How (asks about the way something is done).",
   resourceLabel:"YouTube: Question Words", resourceUrl:"https://www.youtube.com/results?search_query=Question%20Words%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=xFt17oZYvHs",
   quiz:[
     {q:"Which question word asks about a PERSON?", options:["Where","When","What","Who"], answer:3},
     {q:"Which question word asks about a PLACE?", options:["How","When","Why","Where"], answer:3},
     {q:"Fill in the blank: '__ did you eat for lunch?' (asking about a thing)", options:["What","When","Where","Who"], answer:0},
     {q:"Which question word asks about a REASON?", options:["When","Where","Why","How"], answer:2},
     {q:"'__ did the party start?' is asking about...", options:["A person","A place","A time","A reason"], answer:2},
   ]},
  {subject:"Math", title:"Equal Groups as Early Multiplication", summary:"When we put things into equal groups, we can count them faster. For example, 3 groups of 4 = 12. This is the beginning of multiplication!",
   resourceLabel:"YouTube: Equal Groups as Early Multiplication", resourceUrl:"https://www.youtube.com/results?search_query=Equal%20Groups%20as%20Early%20Multiplication%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=gzFbUZ8VjEg",
   quiz:[
     {q:"How many are in 2 groups of 5?", options:["12","8","10","7"], answer:2},
     {q:"How many are in 3 groups of 3?", options:["3","12","6","9"], answer:3},
     {q:"If there are 4 bags with 2 apples each, how many apples are there?", options:["2","10","8","6"], answer:2},
     {q:"Which picture shows 3 equal groups of 4?", options:["12 objects in 3 groups of 4","4 objects in 3 unequal groups","12 objects all together in 1 group","3 objects in 4 groups"], answer:0},
     {q:"2 groups of 6 equals...", options:["10","12","14","8"], answer:1},
   ]},
  {subject:"Science", title:"Parts of the Human Body", summary:"Our body has many parts that work together: head, shoulders, arms, hands, chest, stomach, legs, knees, and feet. Each part has an important job.",
   resourceLabel:"YouTube: Parts of the Human Body", resourceUrl:"https://www.youtube.com/results?search_query=Parts%20of%20the%20Human%20Body%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=B3Fv2X8EKfE",
   quiz:[
     {q:"Which body part helps you walk and run?", options:["Arms","Ears","Nose","Legs and feet"], answer:3},
     {q:"What does your heart do?", options:["Helps you move your arms","Helps you see","Helps you smell","Pumps blood through your body"], answer:3},
     {q:"Which body part helps you breathe?", options:["Brain","Lungs","Stomach","Elbows"], answer:1},
     {q:"What is the job of your brain?", options:["Control your body and thinking","Pump blood","Help you walk only","Digest food"], answer:0},
     {q:"Which body part connects your hand to your shoulder?", options:["Elbow and arm","Knee","Ankle","Hip"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Good Citizenship", summary:"A good citizen is someone who helps their community, follows rules, respects others, and takes care of shared spaces. Being a helpful community member makes life better for everyone.",
   resourceLabel:"YouTube: Good Citizenship", resourceUrl:"https://www.youtube.com/results?search_query=Good%20Citizenship%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=QYa_DmgBUAk",
   quiz:[
     {q:"What is a good citizen?", options:["Someone who breaks rules","Someone who never talks to neighbours","Someone who helps their community and follows rules","Someone who only thinks about themselves"], answer:2},
     {q:"Which is an example of good citizenship?", options:["Bullying classmates","Littering in the park","Helping pick up litter in the park","Ignoring others who need help"], answer:2},
     {q:"Why is voting (when you are old enough) important?", options:["Voting changes nothing","It lets people have a say in decisions","It is not important","Only leaders should vote"], answer:1},
     {q:"Which of these shows respect for others?", options:["Interrupting people constantly","Ignoring community rules","Taking other people's belongings","Listening when others are speaking"], answer:3},
     {q:"Being a good neighbour includes...", options:["Keeping shared spaces clean and being kind","Taking things without asking","Ignoring your neighbours","Making lots of noise at night"], answer:0},
   ]},
]},
{day:20, label:"Day 20 — Fri (Review)", reviewNote:"Week 4 review — mixed questions from Days 16–19", subjects:[
  {subject:"Language", title:"Review: Story Elements, Plurals, Possessives & Question Words", summary:"Mixed review of story elements, plural nouns, possessive nouns, and question words.",
   resourceLabel:"YouTube: Review: Story Elements, Plurals, Possessives & Question Words", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Story%20Elements%2C%20Plurals%2C%20Possessives%20%26%20Question%20Words%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=h7_aNX-wj9A",
   quiz:[
     {q:"The 'setting' of a story is...", options:["Who is in it","What happens","Where and when it takes place","The lesson"], answer:2},
     {q:"What is the plural of 'box'?", options:["Boxes","Boxies","Boxxes","Boxs"], answer:0},
     {q:"Which is the correct possessive form?", options:["The dog's bone","Dogs bone","Dog bone","The dogs bone"], answer:0},
     {q:"Which question word asks about a place?", options:["Where","When","Who","What"], answer:0},
     {q:"Characters in a story are...", options:["The people or animals in it","The title","The setting","What happens"], answer:0},
   ]},
  {subject:"Math", title:"Review: Patterns, Fractions, Graphs & Equal Groups", summary:"Mixed review of growing/shrinking patterns, fractions, reading graphs, and equal groups.",
   resourceLabel:"YouTube: Review: Patterns, Fractions, Graphs & Equal Groups", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Patterns%2C%20Fractions%2C%20Graphs%20%26%20Equal%20Groups%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=gzFbUZ8VjEg",
   quiz:[
     {q:"What comes next: 4, 8, 12, 16, __?", options:["19","20","22","18"], answer:1},
     {q:"A pizza cut into 4 equal parts — each part is...", options:["One whole","One third","One quarter","One half"], answer:2},
     {q:"In a bar graph, a taller bar means...", options:["Less","Same","Nothing","More"], answer:3},
     {q:"How many in 3 groups of 5?", options:["12","8","15","10"], answer:2},
     {q:"The pattern 15, 12, 9, 6 is a __ pattern.", options:["Shrinking","Random","Growing","Repeating"], answer:0},
   ]},
  {subject:"Science", title:"Review: Materials, Shadows, Light & Body", summary:"Mixed review of properties of materials, day/night/shadows, light and sound, and the human body.",
   resourceLabel:"YouTube: Review: Materials, Shadows, Light & Body", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Materials%2C%20Shadows%2C%20Light%20%26%20Body%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lOIGOT88Aqc",
   quiz:[
     {q:"Which word describes the feel of sandpaper?", options:["Rough","Smooth","Wet","Soft"], answer:0},
     {q:"What causes day and night?", options:["The sun moving around Earth","The Earth rotating","The moon moving","Clouds"], answer:1},
     {q:"Sound is made by...", options:["Electricity only","Light bouncing","Hot air","Vibrations"], answer:3},
     {q:"Which body part pumps blood?", options:["Lungs","Heart","Brain","Stomach"], answer:1},
     {q:"When is your shadow the shortest?", options:["Noon","Night","Morning","Evening"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Review: Money, Continents, Environment & Citizenship", summary:"Mixed review of money and trading, continents and oceans, caring for the environment, and good citizenship.",
   resourceLabel:"YouTube: Review: Money, Continents, Environment & Citizenship", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Money%2C%20Continents%2C%20Environment%20%26%20Citizenship%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=FVQhFIF2-tI",
   quiz:[
     {q:"What is bartering?", options:["Saving coins","Trading goods without money","Buying things with money","Spending all money"], answer:1},
     {q:"How many continents are there?", options:["8","7","6","5"], answer:1},
     {q:"Which of the 3 R's helps the environment?", options:["Read, Run, Rest","Reduce, Reuse, Recycle","Repeat, Replace, Rebuild","Rain, Rivers, Rocks"], answer:1},
     {q:"Which action shows good citizenship?", options:["Ignoring neighbours","Helping pick up litter","Littering","Breaking rules"], answer:1},
     {q:"Which continent is Canada on?", options:["South America","Asia","North America","Europe"], answer:2},
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"Language", title:"Alphabetical Order", summary:"Alphabetical order means putting words in the order of the letters in the alphabet (a, b, c… z). When words start with the same letter, look at the second letter.",
   resourceLabel:"YouTube: Alphabetical Order", resourceUrl:"https://www.youtube.com/results?search_query=Alphabetical%20Order%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=z9tqxFdmx5k",
   quiz:[
     {q:"Which word would come FIRST in alphabetical order?", options:["Cat","Dog","Ball","Ant"], answer:3},
     {q:"Put these in alphabetical order: sun, moon, star. Which comes first?", options:["Sun","All the same","Moon","Star"], answer:2},
     {q:"Which word comes LAST in alphabetical order: pig, owl, rabbit, horse?", options:["Rabbit","Owl","Horse","Pig"], answer:0},
     {q:"If two words start with the same letter, we look at the __ letter.", options:["Last","Second","Third","First"], answer:1},
     {q:"Which word comes first alphabetically: apple or ant?", options:["Apple","Cannot tell","Both the same","Ant"], answer:3},
   ]},
  {subject:"Math", title:"Position Words", summary:"Position words describe where things are — over, under, above, below, beside, left, right, in front, and behind.",
   resourceLabel:"YouTube: Position Words", resourceUrl:"https://www.youtube.com/results?search_query=Position%20Words%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=HnlJzWhsNnw",
   quiz:[
     {q:"If a ball is on TOP of a box, the ball is __ the box.", options:["Under","Over/above","Beside","Behind"], answer:1},
     {q:"Which word means the OPPOSITE of 'left'?", options:["Back","Down","Right","Up"], answer:2},
     {q:"The dog is __ the chair (the dog is in front of and sitting next to the chair).", options:["Beside","Over","Behind","Under"], answer:0},
     {q:"What position word means the cat is directly below the table?", options:["Under","Over","Beside","In front of"], answer:0},
     {q:"Your right hand is on which side?", options:["The same side as your heart","The opposite side from your heart","Above you","Behind you"], answer:1},
   ]},
  {subject:"Science", title:"Living vs. Non-Living Things (Deeper Look)", summary:"Living things need food, water, air, and space to grow. They also respond to their environment and reproduce (have offspring). Non-living things do not do these things.",
   resourceLabel:"YouTube: Living vs. Non-Living Things (Deeper Look)", resourceUrl:"https://www.youtube.com/results?search_query=Living%20vs.%20Non-Living%20Things%20%28Deeper%20Look%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=QmQvdUaH7hE",
   quiz:[
     {q:"Which is a characteristic of ALL living things?", options:["They always live in water","They can fly","They need food, water, and air","They are always green"], answer:2},
     {q:"Which of these is a non-living thing?", options:["A mushroom","A cloud","A flower","A worm"], answer:1},
     {q:"'Reproduce' means...", options:["To breathe air","To move quickly","To eat food","To make copies of yourself"], answer:3},
     {q:"A rock is non-living because it does NOT...", options:["Have a surface","Stay in one place","Grow, eat, breathe, or reproduce","Have colour"], answer:2},
     {q:"Which of these is a living thing?", options:["A cloud","Water","Air","A butterfly"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Transportation Long Ago vs. Today", summary:"Transportation has changed a lot over time. Long ago, people walked, rode horses, or travelled by boat. Today, we have cars, trains, airplanes, and buses.",
   resourceLabel:"YouTube: Transportation Long Ago vs. Today", resourceUrl:"https://www.youtube.com/results?search_query=Transportation%20Long%20Ago%20vs.%20Today%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=7WME-lWSbDw",
   quiz:[
     {q:"Long ago, before cars existed, how did most people travel on land?", options:["By subway","By horse, foot, or horse-drawn carriage","By airplane","By rocket ship"], answer:1},
     {q:"Which of these is a MODERN form of transportation?", options:["Walking","Sailboat from long ago","Airplane","Horse and buggy"], answer:2},
     {q:"How has transportation changed our world?", options:["It has not changed anything","It changed nothing about trade","It lets travel go faster and farther","It made travel slower"], answer:2},
     {q:"Which form of transportation was used to cross oceans long ago?", options:["Sailing ship","Train","Airplane","Car"], answer:0},
     {q:"Today, which form of transportation is the FASTEST for travelling very long distances?", options:["Train","Airplane","Horse","Car"], answer:1},
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"Language", title:"Punctuation in Context", summary:"Sentences end with different punctuation marks: a period (.) ends a statement, a question mark (?) ends a question, and an exclamation mark (!) ends an exciting or surprising sentence.",
   resourceLabel:"YouTube: Punctuation in Context", resourceUrl:"https://www.youtube.com/results?search_query=Punctuation%20in%20Context%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=LdCOswMeXFQ",
   quiz:[
     {q:"Which punctuation mark ends a question?", options:["Question mark (?)","Exclamation mark (!)","Comma (,)","Period (.)"], answer:0},
     {q:"'The cat sat on the mat' should end with a...", options:["Exclamation mark","Comma","Period","Question mark"], answer:2},
     {q:"'Watch out!' should end with an...", options:["Period","Exclamation mark","Question mark","Comma"], answer:1},
     {q:"Which sentence needs a question mark?", options:["The sky is blue","Watch out","Where are you going","I love pizza"], answer:2},
     {q:"A period is used at the end of a...", options:["Title only","Exclamation","Question","Statement"], answer:3},
   ]},
  {subject:"Math", title:"Estimation Then Counting to Check", summary:"Estimation means making a good guess about a number without counting exactly. After estimating, you count to check how close your guess was.",
   resourceLabel:"YouTube: Estimation Then Counting to Check", resourceUrl:"https://www.youtube.com/results?search_query=Estimation%20Then%20Counting%20to%20Check%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=xnUkIsdvfGY",
   quiz:[
     {q:"What is an estimate?", options:["A good guess about a number","A type of graph","The wrong answer always","An exact answer"], answer:0},
     {q:"If you see about 30 marbles in a jar, a good estimate would be...", options:["1,000","1","500","30"], answer:3},
     {q:"Why do we check our estimate by counting?", options:["Estimates are always right","Just for fun","To see how close our guess was","Counting is not useful"], answer:2},
     {q:"If you estimate 20 and count 22, your estimate was...", options:["Exactly right","Very close","Impossible","Very far off"], answer:1},
     {q:"Which is the best strategy for estimating?", options:["Always guess 1","Always guess 100","Never guess","Use what you know to guess reasonably"], answer:3},
   ]},
  {subject:"Science", title:"Using Tools: Thermometers and Magnifying Glasses", summary:"Scientists use special tools to observe and measure. A thermometer measures temperature (how hot or cold something is). A magnifying glass makes small things look bigger so we can study them.",
   resourceLabel:"YouTube: Using Tools: Thermometers and Magnifying Glasses", resourceUrl:"https://www.youtube.com/results?search_query=Using%20Tools%3A%20Thermometers%20and%20Magnifying%20Glasses%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=AmrFkCwd1Lc",
   quiz:[
     {q:"What does a thermometer measure?", options:["Time","Temperature","Length","Weight"], answer:1},
     {q:"What does a magnifying glass do?", options:["Measures temperature","Makes objects look bigger","Measures length","Weighs objects"], answer:1},
     {q:"On a thermometer, a higher number means the temperature is...", options:["Colder","Impossible to tell","The same","Warmer"], answer:3},
     {q:"Why do scientists use tools?", options:["Tools are never useful","To make more accurate measurements","To draw pictures only","Just for decoration"], answer:1},
     {q:"You would use a magnifying glass to...", options:["Look closely at a tiny insect","Check the temperature outside","Measure a pencil's length","Weigh a rock"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Celebrations and Traditions Around the World", summary:"Families and communities around the world celebrate many different holidays and traditions, like Diwali, Hanukkah, Eid, Christmas, Lunar New Year, and Kwanzaa. Each celebration has its own meaning and customs.",
   resourceLabel:"YouTube: Celebrations and Traditions Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Celebrations%20and%20Traditions%20Around%20the%20World%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=RwSYrsjTiW4",
   quiz:[
     {q:"Diwali is often called the...", options:["Festival of Harvest","Festival of Water","Festival of Lights","Festival of Snow"], answer:2},
     {q:"Lunar New Year is celebrated by many people from...", options:["No specific culture","African cultures","Asian cultures like Chinese","European cultures only"], answer:2},
     {q:"Why do communities around the world have different celebrations?", options:["Cultures have different histories","No real reason","Only one culture celebrates anything","All celebrations are the same"], answer:0},
     {q:"Learning about other cultures' celebrations helps us...", options:["Respect people different from us","Copy them exactly","Stop celebrating everything","Ignore our own traditions"], answer:0},
     {q:"Which of these is an example of a religious holiday?", options:["A regular Thursday","A school day","A birthday","Eid, Hanukkah, or Christmas"], answer:3},
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"Language", title:"Types of Sentences", summary:"There are three types of sentences: a statement tells something (ends with a period), a question asks something (ends with a question mark), and an exclamation shows strong feeling (ends with an exclamation mark).",
   resourceLabel:"YouTube: Types of Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Types%20of%20Sentences%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=g9_DQOwETMo",
   quiz:[
     {q:"Which sentence is a STATEMENT?", options:["Watch out!","Are you ready?","The sun is bright.","Where are you going?"], answer:2},
     {q:"Which sentence is a QUESTION?", options:["The sky is blue.","Go away!","I like cats.","What is your name?"], answer:3},
     {q:"Which sentence is an EXCLAMATION?", options:["We won the game!","What time is it?","The cat sat.","She reads books."], answer:0},
     {q:"A statement always ends with a...", options:["Period","Comma","Exclamation mark","Question mark"], answer:0},
     {q:"'How many apples are there?' is what type of sentence?", options:["Statement","Question","Exclamation","Command"], answer:1},
   ]},
  {subject:"Math", title:"Doubles Facts", summary:"Doubles facts are when you add a number to itself: 1+1=2, 2+2=4, 3+3=6, 4+4=8, 5+5=10, 6+6=12. Knowing doubles makes adding much faster!",
   resourceLabel:"YouTube: Doubles Facts", resourceUrl:"https://www.youtube.com/results?search_query=Doubles%20Facts%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=qaqLjzMyyHI",
   quiz:[
     {q:"What is 4 + 4?", options:["8","6","7","9"], answer:0},
     {q:"What is 6 + 6?", options:["13","10","12","11"], answer:2},
     {q:"What is 5 + 5?", options:["9","10","11","12"], answer:1},
     {q:"What is 3 + 3?", options:["5","6","8","7"], answer:1},
     {q:"Doubles facts are when you add...", options:["A number plus 1","Two different numbers","A number plus 10","A number to itself"], answer:3},
   ]},
  {subject:"Science", title:"Animal Habitats (Deeper Look)", summary:"Animals are specially suited for their habitats — their body features help them survive. A polar bear has thick fur for the cold arctic. A fish has gills for breathing underwater.",
   resourceLabel:"YouTube: Animal Habitats (Deeper Look)", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Habitats%20%28Deeper%20Look%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Mad8J-iu2J0",
   quiz:[
     {q:"Why does a polar bear have thick white fur?", options:["To swim faster","To stay warm and blend in with snow","Just for looks","Because all bears have white fur"], answer:1},
     {q:"A fish breathes underwater using...", options:["Lungs","Gills","Its skin only","Fins"], answer:1},
     {q:"A camel is suited to live in the desert because it...", options:["Loves cold weather","Has thick white fur","Has gills","Can store water and fat in its humps"], answer:3},
     {q:"What does 'adapted' mean when we talk about animals?", options:["The animal moves to a new country","The animal changes its diet only","Nothing special","Features that help it survive"], answer:3},
     {q:"A duck's webbed feet help it...", options:["Fly higher","Run fast on land","Climb trees","Swim in water"], answer:3},
   ]},
  {subject:"SocialStudies", title:"Alphabetical Review: Canadian Communities", summary:"Canada has many communities from coast to coast — from big cities like Toronto, Vancouver, and Montreal to smaller towns and rural areas. Each place has unique features that make it special.",
   resourceLabel:"YouTube: Alphabetical Review: Canadian Communities", resourceUrl:"https://www.youtube.com/results?search_query=Alphabetical%20Review%3A%20Canadian%20Communities%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Qo7aTFHyhPE",
   quiz:[
     {q:"Which city is the capital of Canada?", options:["Ottawa","Vancouver","Montreal","Toronto"], answer:0},
     {q:"Canada stretches from coast to coast — from which ocean to which ocean?", options:["Pacific to Atlantic","Only one ocean","Arctic to Indian","Atlantic to Pacific"], answer:0},
     {q:"Which of these is a large Canadian city?", options:["Paris","London, England","Toronto","New York"], answer:2},
     {q:"What makes communities across Canada unique?", options:["Different geography and cultures","They all have the same weather","Nothing makes them different","They are all exactly alike"], answer:0},
     {q:"Quebec is a province where many people speak...", options:["Spanish","French","Mandarin","Italian"], answer:1},
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"Language", title:"Predicting What Happens Next", summary:"Good readers make predictions — they use clues in the story and what they already know to guess what might happen next.",
   resourceLabel:"YouTube: Predicting What Happens Next", resourceUrl:"https://www.youtube.com/results?search_query=Predicting%20What%20Happens%20Next%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pu0RahGZ-38",
   quiz:[
     {q:"What is a prediction when reading?", options:["A guess about what happens next","Reading backwards","Copying the story","Remembering what happened"], answer:0},
     {q:"What do good readers use to make a prediction?", options:["Nothing","The last word in the book","Clues and their own knowledge","Random guesses only"], answer:2},
     {q:"In a story, the sky gets dark and thundery. A good prediction is...", options:["It will become sunny and warm","It will probably rain or storm","The characters will go swimming","Nothing will happen"], answer:1},
     {q:"If a prediction turns out to be wrong, you should...", options:["Change it based on new info","Skip ahead","Decide the book is wrong","Stop reading"], answer:0},
     {q:"Why is making predictions helpful when reading?", options:["It replaces reading","It is only for teachers","It keeps readers thinking and engaged","It is not helpful"], answer:2},
   ]},
  {subject:"Math", title:"Comparing Capacity and Mass Informally", summary:"Capacity is how much something can hold. Mass is how heavy something is. We can compare by asking: which holds more? Which is heavier?",
   resourceLabel:"YouTube: Comparing Capacity and Mass Informally", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Capacity%20and%20Mass%20Informally%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pbX2c_nTWl0",
   quiz:[
     {q:"Which holds MORE: a bathtub or a teacup?", options:["Cannot compare","Both the same","Bathtub","Teacup"], answer:2},
     {q:"Which is HEAVIER: a schoolbag full of books or an empty bag?", options:["Full schoolbag with books","Both the same","Empty bag","Cannot compare"], answer:0},
     {q:"'Capacity' means...", options:["How much something can hold","How long something is","How heavy something is","How fast something moves"], answer:0},
     {q:"If a large pot holds more soup than a small bowl, the pot has a...", options:["Smaller capacity","Larger capacity","Same capacity","Less mass"], answer:1},
     {q:"Which is a good tool to compare mass (weight)?", options:["Ruler","Thermometer","Measuring cup","Balance scale"], answer:3},
   ]},
  {subject:"Science", title:"The Five Senses in Science Observations", summary:"Scientists use all five senses to make observations — they look, listen, smell, feel, and sometimes taste (safely!) to learn about the world around them.",
   resourceLabel:"YouTube: The Five Senses in Science Observations", resourceUrl:"https://www.youtube.com/results?search_query=The%20Five%20Senses%20in%20Science%20Observations%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=q1xNuU7gaAQ",
   quiz:[
     {q:"What is a scientific observation?", options:["Drawing a picture only","Guessing randomly","Reading a textbook only","Using senses to notice details"], answer:3},
     {q:"Which senses can a scientist use to observe a lemon?", options:["Only smell","Sight, smell, touch, and taste","Only sight","Hearing only"], answer:1},
     {q:"Which sense would you use to tell if a rock is smooth or bumpy?", options:["Taste","Touch","Sight","Hearing"], answer:1},
     {q:"Why do scientists use more than one sense when observing?", options:["Senses are not used in science","More senses give more accurate info","One sense is always enough","No reason"], answer:1},
     {q:"Observing means...", options:["Noticing details using your senses","Measuring only with tools","Reading about something","Guessing about something"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Transportation and Its Impact on Communities", summary:"Transportation connects communities — roads, trains, and airports allow people and goods to move between towns, cities, and countries. This helps communities grow and trade.",
   resourceLabel:"YouTube: Transportation and Its Impact on Communities", resourceUrl:"https://www.youtube.com/results?search_query=Transportation%20and%20Its%20Impact%20on%20Communities%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=3ww-9ZkVkMw",
   quiz:[
     {q:"How does transportation help communities?", options:["It does not help","It only helps cities","It only brings problems","It connects people and moves goods"], answer:3},
     {q:"Which form of transportation connects cities very quickly over long distances?", options:["Airplane","Bicycle","Walking","Horse"], answer:0},
     {q:"Roads and highways are important for communities because they...", options:["Let cars move people and goods","Only carry water","Look pretty","Have no useful purpose"], answer:0},
     {q:"Before highways and cars, how did settlers in Canada move heavy goods?", options:["By airplane","By rivers, canoes, and wagons","By bicycle","By train only"], answer:1},
     {q:"A port (harbour) in a community is important for...", options:["Making electricity","Growing crops","Building houses","Receiving and sending goods by ship"], answer:3},
   ]},
]},
{day:25, label:"Day 25 — Fri (Review)", reviewNote:"Week 5 review — mixed questions from Days 21–24", subjects:[
  {subject:"Language", title:"Review: Alphabetical Order, Punctuation, Sentence Types & Predictions", summary:"Mixed review of alphabetical order, punctuation marks, types of sentences, and making predictions.",
   resourceLabel:"YouTube: Review: Alphabetical Order, Punctuation, Sentence Types & Predictions", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Alphabetical%20Order%2C%20Punctuation%2C%20Sentence%20Types%20%26%20Predictions%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=o3zwyUbBi6w",
   quiz:[
     {q:"Which word comes first in alphabetical order: dog, ant, cat?", options:["All the same","Dog","Ant","Cat"], answer:2},
     {q:"A question ends with a...", options:["Period","Exclamation mark","Question mark","Comma"], answer:2},
     {q:"Which is a STATEMENT sentence?", options:["Watch out!","The bird is singing.","Where are you?","Come here!"], answer:1},
     {q:"What do good readers use to make a prediction?", options:["Nothing","Clues in the story","The last page only","Random guesses"], answer:1},
     {q:"'We won!' is what type of sentence?", options:["Question","Command","Statement","Exclamation"], answer:3},
   ]},
  {subject:"Math", title:"Review: Position Words, Doubles, Estimation & Capacity", summary:"Mixed review of position words, doubles facts, estimating, and comparing capacity and mass.",
   resourceLabel:"YouTube: Review: Position Words, Doubles, Estimation & Capacity", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Position%20Words%2C%20Doubles%2C%20Estimation%20%26%20Capacity%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=joHaCejRnmo",
   quiz:[
     {q:"Which word describes where something is below another object?", options:["In front","Over","Under","Beside"], answer:2},
     {q:"What is 5 + 5?", options:["8","11","9","10"], answer:3},
     {q:"What is a good estimate for a jar with about 20 jelly beans?", options:["100","1,000","2","20"], answer:3},
     {q:"Which holds more: a swimming pool or a glass of water?", options:["Swimming pool","Both the same","Cannot compare","Glass of water"], answer:0},
     {q:"What is 3 + 3?", options:["7","8","6","5"], answer:2},
   ]},
  {subject:"Science", title:"Review: Living Things, Animal Adaptations, Tools & Senses", summary:"Mixed review of living vs. non-living, animal adaptations, science tools, and using senses to observe.",
   resourceLabel:"YouTube: Review: Living Things, Animal Adaptations, Tools & Senses", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Living%20Things%2C%20Animal%20Adaptations%2C%20Tools%20%26%20Senses%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=m2MibjJgyjs",
   quiz:[
     {q:"Which is a characteristic of all living things?", options:["They can fly","They need food, water, and air","They are always green","They live in water only"], answer:1},
     {q:"Why does a polar bear have thick white fur?", options:["Because all bears do","To swim faster","To stay warm and blend in with snow","For looks"], answer:2},
     {q:"What does a thermometer measure?", options:["Temperature","Weight","Length","Time"], answer:0},
     {q:"A fish has gills to help it...", options:["Breathe underwater","Climb trees","Walk on land","Fly in the air"], answer:0},
     {q:"What is a scientific observation?", options:["Using your senses to notice details","Drawing only","A random guess","Reading a book only"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Review: Transportation, Celebrations, Canadian Communities & Environment", summary:"Mixed review of transportation history, world celebrations, Canadian communities, and caring for the environment.",
   resourceLabel:"YouTube: Review: Transportation, Celebrations, Canadian Communities & Environment", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Transportation%2C%20Celebrations%2C%20Canadian%20Communities%20%26%20Environment%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=NR7z9FbUf5k",
   quiz:[
     {q:"Long ago, how did most people travel on land?", options:["By car","By subway","By horse or foot","By airplane"], answer:2},
     {q:"Diwali is called the Festival of...", options:["Snow","Water","Lights","Harvest"], answer:2},
     {q:"What is the capital city of Canada?", options:["Vancouver","Toronto","Montreal","Ottawa"], answer:3},
     {q:"Which of the 3 R's helps protect the environment?", options:["Recycle, Reduce, Reuse","Repeat, Replace, Rebuild","Rain, Rivers, Rocks","Read, Run, Rest"], answer:0},
     {q:"Airports are important for communities because they...", options:["Allow fast travel to distant places","Look nice","Grow food","Only carry water"], answer:0},
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"Language", title:"Retelling a Story in Your Own Words", summary:"Retelling a story means explaining what happened in your own words — including the main characters, the setting, the problem, and the solution.",
   resourceLabel:"YouTube: Retelling a Story in Your Own Words", resourceUrl:"https://www.youtube.com/results?search_query=Retelling%20a%20Story%20in%20Your%20Own%20Words%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=JNemQATWt2E",
   quiz:[
     {q:"When retelling a story, you should include...", options:["Only the title","Random details","The characters and what happened","Only the last event"], answer:2},
     {q:"What does 'in your own words' mean?", options:["Rewrite every single word differently","Not speak at all","Say it in your own words, not copied","Copy the book exactly"], answer:2},
     {q:"What is the 'problem' in a story?", options:["The title","The challenge in the story","The setting","The character's name"], answer:1},
     {q:"What is the 'solution' in a story?", options:["The first sentence","The main character's name","The setting","How the problem gets solved"], answer:3},
     {q:"When retelling, which order should you follow?", options:["Middle, end, beginning","End, beginning, middle","Randomly","Beginning, middle, end"], answer:3},
   ]},
  {subject:"Math", title:"Addition Within 100 (Review and Challenge)", summary:"Practice adding two-digit numbers. Remember to add the ones first, then the tens. Some questions will challenge your thinking!",
   resourceLabel:"YouTube: Addition Within 100 (Review and Challenge)", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20Within%20100%20%28Review%20and%20Challenge%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=YdF_A1O006Q",
   quiz:[
     {q:"45 + 32 = ?", options:["67","76","77","78"], answer:2},
     {q:"63 + 15 = ?", options:["77","79","88","78"], answer:3},
     {q:"21 + 48 = ?", options:["70","59","69","68"], answer:2},
     {q:"50 + 37 = ?", options:["88","97","86","87"], answer:3},
     {q:"33 + 44 = ?", options:["78","77","76","87"], answer:1},
   ]},
  {subject:"Science", title:"What Plants Need: Deeper Exploration", summary:"Plants make their own food using sunlight, water, and air (carbon dioxide) — this process is called photosynthesis. Roots absorb water and nutrients; leaves capture sunlight.",
   resourceLabel:"YouTube: What Plants Need: Deeper Exploration", resourceUrl:"https://www.youtube.com/results?search_query=What%20Plants%20Need%3A%20Deeper%20Exploration%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=u46A0WKp2nk",
   quiz:[
     {q:"What is photosynthesis?", options:["How plants eat insects","How plants use sunlight to make food","How plants move around","How plants sleep at night"], answer:1},
     {q:"Which part of the plant absorbs water from the soil?", options:["Stem only","Leaves","Flowers","Roots"], answer:3},
     {q:"Which part of the plant captures sunlight?", options:["Roots","Leaves","Seeds","Flowers"], answer:1},
     {q:"What gas do plants take in from the air during photosynthesis?", options:["Carbon dioxide","Oxygen","Steam","Nitrogen"], answer:0},
     {q:"What do plants release into the air that helps people breathe?", options:["Oxygen","Water vapour only","Nitrogen","Carbon dioxide"], answer:0},
   ]},
  {subject:"SocialStudies", title:"People and the Environment: Making a Difference", summary:"People can both harm and help the environment. Pollution harms nature, but acts like planting trees, picking up litter, and saving energy help protect it for future generations.",
   resourceLabel:"YouTube: People and the Environment: Making a Difference", resourceUrl:"https://www.youtube.com/results?search_query=People%20and%20the%20Environment%3A%20Making%20a%20Difference%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=belXC_IoW4o",
   quiz:[
     {q:"Which human action HARMS the environment?", options:["Picking up litter","Planting trees","Dumping garbage in a river","Using reusable bags"], answer:2},
     {q:"Which action helps protect the environment for future generations?", options:["Wasting electricity","Burning waste in the open air","Littering","Planting trees and gardens"], answer:3},
     {q:"What does 'pollution' mean?", options:["Making the environment dirty with waste","Planting more trees","Conserving water","Cleaning up the environment"], answer:0},
     {q:"How can students help the environment at school?", options:["Wasting paper","Turning off lights and recycling","Leaving taps running","Dropping litter"], answer:1},
     {q:"Why is it important to protect the environment for future generations?", options:["So future kids have clean air and water","The environment never changes","It is not important","Only adults need to worry about it"], answer:0},
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"Language", title:"Using Describing Words in Writing", summary:"Describing words (adjectives and adverbs) make writing more interesting and detailed. Instead of 'The cat ran,' you could write 'The small, fluffy cat ran quickly.'",
   resourceLabel:"YouTube: Using Describing Words in Writing", resourceUrl:"https://www.youtube.com/results?search_query=Using%20Describing%20Words%20in%20Writing%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=MofJXWoGOdY",
   quiz:[
     {q:"Which sentence uses the BEST describing words?", options:["The cat ran.","Something happened.","A thing moved.","The small fluffy cat ran quickly."], answer:3},
     {q:"Which word is an adjective (describes a noun)?", options:["Fluffy","Jumped","Run","Quickly"], answer:0},
     {q:"Adding describing words to your writing makes it...", options:["More interesting and detailed","Harder to understand","More boring","Shorter"], answer:0},
     {q:"Which word describes HOW the girl sang (an adverb)?", options:["Happy","Loudly","Song","Beautiful"], answer:1},
     {q:"Choose the best describing word for the blank: 'The __ puppy played in the snow.'", options:["Tiny playful","Table","Run","Quickly"], answer:0},
   ]},
  {subject:"Math", title:"Subtraction Within 100 (Review and Challenge)", summary:"Practice subtracting two-digit numbers. Remember to subtract the ones first, then the tens.",
   resourceLabel:"YouTube: Subtraction Within 100 (Review and Challenge)", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20Within%20100%20%28Review%20and%20Challenge%29%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ds226Vh7epg",
   quiz:[
     {q:"87 - 34 = ?", options:["53","52","54","63"], answer:0},
     {q:"69 - 25 = ?", options:["43","44","45","54"], answer:1},
     {q:"98 - 56 = ?", options:["42","43","41","52"], answer:0},
     {q:"75 - 43 = ?", options:["33","31","42","32"], answer:3},
     {q:"56 - 31 = ?", options:["26","24","25","35"], answer:2},
   ]},
  {subject:"Science", title:"Weather and How We Measure It", summary:"Scientists called meteorologists study weather. They use thermometers to measure temperature, rain gauges to measure rainfall, and wind vanes to find wind direction.",
   resourceLabel:"YouTube: Weather and How We Measure It", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20and%20How%20We%20Measure%20It%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=fPneyo-KiZo",
   quiz:[
     {q:"What is a meteorologist?", options:["A geologist","An astronaut","A doctor","A scientist who studies weather"], answer:3},
     {q:"What tool measures how much rain has fallen?", options:["Rain gauge","Magnifying glass","Thermometer","Wind vane"], answer:0},
     {q:"What does a wind vane tell you?", options:["The direction the wind is blowing","How heavy the clouds are","How hot it is","How much it rained"], answer:0},
     {q:"If the thermometer shows a very high number, the weather is...", options:["Cool","Very cold","Rainy","Very warm or hot"], answer:3},
     {q:"Why is it useful to measure and record weather?", options:["Weather never changes","It is not useful","It helps predict weather safely","Only scientists need to know"], answer:2},
   ]},
  {subject:"SocialStudies", title:"Canada's Regions and Geography", summary:"Canada is a huge country with many different regions — the mountains of British Columbia, the prairies of Alberta and Saskatchewan, the Great Lakes area, and the Atlantic coast all have different landscapes and ways of life.",
   resourceLabel:"YouTube: Canada's Regions and Geography", resourceUrl:"https://www.youtube.com/results?search_query=Canada%27s%20Regions%20and%20Geography%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Q_VFQUZ9oo4",
   quiz:[
     {q:"Which province is known for the Rocky Mountains?", options:["Ontario","Prince Edward Island","British Columbia","Nova Scotia"], answer:2},
     {q:"The prairies in Canada are known for...", options:["Tropical beaches","Tall mountains","Deep oceans","Flat farmland and wheat fields"], answer:3},
     {q:"The Great Lakes are located near which Canadian province?", options:["Ontario","Nova Scotia","Alberta","British Columbia"], answer:0},
     {q:"Why do different regions of Canada have different ways of life?", options:["Only the weather is different","All regions are the same","Geography and climate shape daily life","No reason"], answer:2},
     {q:"Canada is the __ largest country in the world by area.", options:["Third","Fourth","Second","First"], answer:2},
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"Language", title:"Reading for Details", summary:"When we read for details, we look for specific information — who, what, where, when, and how. Details support the main idea and help us understand the story better.",
   resourceLabel:"YouTube: Reading for Details", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20for%20Details%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=OHuJWfpsRrM",
   quiz:[
     {q:"What are 'details' in a text?", options:["The title only","The main idea only","Facts that support the main idea","Random words"], answer:2},
     {q:"If a story says 'Maya walked her golden dog to the sunny park,' what detail tells us WHAT the dog looks like?", options:["Walked","Maya","Park","Golden"], answer:3},
     {q:"Reading for details helps you...", options:["Only read faster","Find facts and understand it better","Skip important information","Ignore the main idea"], answer:1},
     {q:"Which question word helps you find WHERE details in a story?", options:["Why","What","Where","Who"], answer:2},
     {q:"Details in a story can tell you...", options:["Who, what, where, when, and how","Only the ending","Nothing important","Only the lesson"], answer:0},
   ]},
  {subject:"Math", title:"Counting Coins and Making Change", summary:"We can add different coins together to make a total. We can also figure out how much change we receive when we pay for something.",
   resourceLabel:"YouTube: Counting Coins and Making Change", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20Coins%20and%20Making%20Change%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=MbtmucV-U2c",
   quiz:[
     {q:"What is the total value of 1 quarter, 1 dime, and 1 nickel?", options:["40¢","45¢","35¢","30¢"], answer:0},
     {q:"If something costs 20¢ and you pay with a quarter (25¢), how much change do you get?", options:["5¢","10¢","15¢","4¢"], answer:0},
     {q:"Which combination makes exactly 30¢?", options:["2 dimes + 2 nickels","1 quarter + 1 penny","1 quarter + 1 nickel","3 dimes"], answer:3},
     {q:"What is the total of 2 quarters?", options:["55¢","45¢","50¢","40¢"], answer:2},
     {q:"If you have 1 dime and 3 nickels, how much money do you have?", options:["30¢","35¢","20¢","25¢"], answer:3},
   ]},
  {subject:"Science", title:"Simple Machines Around Us", summary:"Simple machines make work easier. We have learned about levers, ramps (inclined planes), and wheels. Other simple machines include pulleys and wedges. They help us lift, move, or cut things.",
   resourceLabel:"YouTube: Simple Machines Around Us", resourceUrl:"https://www.youtube.com/results?search_query=Simple%20Machines%20Around%20Us%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=LSfNYpCprw4",
   quiz:[
     {q:"Which simple machine is a ramp also known as?", options:["Inclined plane","Wedge","Lever","Pulley"], answer:0},
     {q:"A door stopper that holds a door open is an example of a...", options:["Wedge","Lever","Pulley","Wheel"], answer:0},
     {q:"Which simple machine helps lift a flag up a flagpole?", options:["Wedge","Lever","Pulley","Inclined plane"], answer:2},
     {q:"A see-saw is an example of a...", options:["Wheel","Pulley","Ramp","Lever"], answer:3},
     {q:"Simple machines help us by...", options:["Adding more steps to tasks","Making work easier by reducing force","Making work harder","Making things slower always"], answer:1},
   ]},
  {subject:"SocialStudies", title:"Why Rules and Laws are Important", summary:"Communities use rules and laws to make sure everyone is treated fairly and can stay safe. Laws are made by governments, and everyone in a community must follow them.",
   resourceLabel:"YouTube: Why Rules and Laws are Important", resourceUrl:"https://www.youtube.com/results?search_query=Why%20Rules%20and%20Laws%20are%20Important%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=5dtuZkposkk",
   quiz:[
     {q:"Who creates laws for a community or country?", options:["Children only","Nobody","The government","One person alone"], answer:2},
     {q:"Why are traffic laws like traffic lights important?", options:["They are optional","They just look nice","They keep drivers and walkers safe","They are only for trucks"], answer:2},
     {q:"What happens when people do not follow the laws?", options:["Nothing at all","The community gets better","Everyone gets a prize","Others may get hurt or face trouble"], answer:3},
     {q:"Rules in a school help to...", options:["Make school boring","Help only some students","Stop learning","Keep students safe and learning fairly"], answer:3},
     {q:"Which of these is an example of a law that helps communities?", options:["A rule that everyone must wear yellow","A law against owning pets","A rule that only adults can speak","A speed limit to keep roads safe"], answer:3},
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"Language", title:"Simple Poetry and Rhythm", summary:"Poems often use rhythm (a beat) and rhyming words to make them fun to read aloud. Each line in a poem has a pattern of sounds. Poetry helps us play with language!",
   resourceLabel:"YouTube: Simple Poetry and Rhythm", resourceUrl:"https://www.youtube.com/results?search_query=Simple%20Poetry%20and%20Rhythm%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=4rOnRJlevmI",
   quiz:[
     {q:"What is rhythm in a poem?", options:["Rhyming words at the end","The number of words","The title of the poem","The beat or pattern of sounds aloud"], answer:3},
     {q:"Which pair of words RHYMES?", options:["Sing / blue","Tree / table","Cat / dog","Moon / spoon"], answer:3},
     {q:"Reading a poem ALOUD helps you notice...", options:["Only the title","Nothing special","Only the meaning","The rhythm and rhyming patterns"], answer:3},
     {q:"In a poem, lines that rhyme usually have the same...", options:["Beginning sound","Number of letters","Ending sound","Middle vowel"], answer:2},
     {q:"What makes a poem different from a regular sentence?", options:["Poems have no words","Poems are always very long","Poems often use rhythm and rhyme","Poems never have punctuation"], answer:2},
   ]},
  {subject:"Math", title:"Numbers to 200: Counting and Comparing", summary:"We can count, read, and write numbers past 100 — all the way to 200. A number like 134 has 1 hundred, 3 tens, and 4 ones.",
   resourceLabel:"YouTube: Numbers to 200: Counting and Comparing", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%20to%20200%3A%20Counting%20and%20Comparing%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Vvu-_yXnh14",
   quiz:[
     {q:"What number comes right after 109?", options:["110","120","100","108"], answer:0},
     {q:"Which number is greater: 145 or 154?", options:["154","Cannot tell","They are equal","145"], answer:0},
     {q:"In the number 136, how many tens are there?", options:["1","13","3","6"], answer:2},
     {q:"Which number is between 120 and 130?", options:["115","135","119","125"], answer:3},
     {q:"Count by 10s: 150, 160, 170, __?", options:["190","175","180","178"], answer:2},
   ]},
  {subject:"Science", title:"Earth and Space: The Sun, Moon, and Stars", summary:"The sun is a star that gives Earth light and warmth. The moon orbits Earth and reflects sunlight. Stars are very far away and look small in the night sky because of the distance.",
   resourceLabel:"YouTube: Earth and Space: The Sun, Moon, and Stars", resourceUrl:"https://www.youtube.com/results?search_query=Earth%20and%20Space%3A%20The%20Sun%2C%20Moon%2C%20and%20Stars%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pZkFWD1oRh8",
   quiz:[
     {q:"What is the sun?", options:["A moon","A very large cloud","A planet","A star that gives Earth light and heat"], answer:3},
     {q:"Why does the moon seem to glow at night?", options:["It is on fire","It reflects light from the sun","It is very close to Earth","It makes its own light"], answer:1},
     {q:"Why do stars look so small in the night sky?", options:["Because they are very far away from Earth","Because they only come out at night","Because they are tiny","Because they are behind clouds"], answer:0},
     {q:"The moon travels (orbits) around...", options:["Mars","The sun","Earth","Another moon"], answer:2},
     {q:"What would happen to life on Earth without the sun?", options:["We would see better","No plant growth; cold and dark","Animals would be happier","Nothing would change"], answer:1},
   ]},
  {subject:"SocialStudies", title:"Our Rights and the Rights of Children", summary:"Every child has rights — things they are entitled to, like the right to safety, education, a family, and to be treated with respect. The United Nations Convention on the Rights of the Child protects these rights.",
   resourceLabel:"YouTube: Our Rights and the Rights of Children", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Rights%20and%20the%20Rights%20of%20Children%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=puarPOoJUy8",
   quiz:[
     {q:"What is a 'right'?", options:["A school subject","Something everyone is entitled to","Something you must give away","A type of direction"], answer:1},
     {q:"Which of these is a right that every child should have?", options:["The right to never follow rules","The right to have the most toys","The right to stay up all night","The right to education and to be safe"], answer:3},
     {q:"The United Nations Convention on the Rights of the Child is...", options:["A children's book","It protects children's rights","A school rule","A type of game"], answer:1},
     {q:"If everyone has rights, then everyone also has a responsibility to...", options:["Ignore others' rights","Only care about their own rights","Break rules","Respect the rights of others"], answer:3},
     {q:"Which of these is an example of a child's right being respected?", options:["A child being treated unfairly","A child not being allowed to go to school","A child being kept safe and cared for","A child having no access to a doctor"], answer:2},
   ]},
]},
{day:30, label:"Day 30 — Fri (Final Review)", reviewNote:"Day 30 Final Review — mixed questions from Days 26–29", subjects:[
  {subject:"Language", title:"Final Review: Retelling, Describing Words, Details & Poetry", summary:"Mixed review of retelling stories, using describing words, reading for details, and simple poetry.",
   resourceLabel:"YouTube: Final Review: Retelling, Describing Words, Details & Poetry", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Retelling%2C%20Describing%20Words%2C%20Details%20%26%20Poetry%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=w33-m8-geuM",
   quiz:[
     {q:"When retelling a story, what should you include?", options:["Characters, setting, and solution","Only the title","Random details","Only the last event"], answer:0},
     {q:"Which word is a describing word (adjective)?", options:["Jump","Fluffy","Run","Quickly"], answer:1},
     {q:"Reading for details means looking for...", options:["Only the main idea","The title only","Facts like who, what, where, when","Nothing specific"], answer:2},
     {q:"What is rhythm in a poem?", options:["The beat or pattern of sounds","The number of words","Rhyming only","The title"], answer:0},
     {q:"Which pair of words rhymes?", options:["Jump / book","Tree / run","Moon / spoon","Dog / cat"], answer:2},
   ]},
  {subject:"Math", title:"Final Review: Coins, Subtraction, Numbers to 200 & Capacity", summary:"Mixed review of counting coins, two-digit subtraction, numbers to 200, and comparing capacity and mass.",
   resourceLabel:"YouTube: Final Review: Coins, Subtraction, Numbers to 200 & Capacity", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Coins%2C%20Subtraction%2C%20Numbers%20to%20200%20%26%20Capacity%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=MbtmucV-U2c",
   quiz:[
     {q:"What is the total of 1 quarter and 1 dime?", options:["40¢","35¢","30¢","25¢"], answer:1},
     {q:"87 - 54 = ?", options:["34","43","33","32"], answer:2},
     {q:"Which number is greater: 142 or 124?", options:["They are equal","124","Cannot tell","142"], answer:3},
     {q:"Which holds MORE: a large bucket or a small cup?", options:["Small cup","Large bucket","Both the same","Cannot compare"], answer:1},
     {q:"What number comes right after 199?", options:["210","201","200","198"], answer:2},
   ]},
  {subject:"Science", title:"Final Review: Plants, Simple Machines, Weather Tools & Space", summary:"Mixed review of plant needs and photosynthesis, simple machines, measuring weather, and the sun, moon, and stars.",
   resourceLabel:"YouTube: Final Review: Plants, Simple Machines, Weather Tools & Space", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Plants%2C%20Simple%20Machines%2C%20Weather%20Tools%20%26%20Space%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=YqtPrEb3yOY",
   quiz:[
     {q:"What do plants use to make their own food?", options:["Darkness and salt","Sunlight, water, and carbon dioxide","Soil only","Nothing — they eat insects"], answer:1},
     {q:"A pulley helps lift...", options:["Light brighter","Temperature","Sound louder","A flag up a flagpole"], answer:3},
     {q:"What tool measures how much rain has fallen?", options:["Thermometer","Wind vane","Rain gauge","Magnifying glass"], answer:2},
     {q:"Why does the moon seem to glow?", options:["It is on fire","It makes its own light","It is a star","It reflects sunlight"], answer:3},
     {q:"Which part of a plant absorbs water from the soil?", options:["Roots","Leaves","Stem","Flowers"], answer:0},
   ]},
  {subject:"SocialStudies", title:"Final Review: Environment, Geography, Laws & Children's Rights", summary:"Mixed review of protecting the environment, Canada's regions, rules and laws, and children's rights.",
   resourceLabel:"YouTube: Final Review: Environment, Geography, Laws & Children's Rights", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Environment%2C%20Geography%2C%20Laws%20%26%20Children%27s%20Rights%20grade%202%20educational",
   videoUrl:"https://www.youtube.com/watch?v=TyP09S0UEzA",
   quiz:[
     {q:"Which action protects the environment?", options:["Wasting electricity","Planting trees and recycling","Littering","Pouring chemicals into lakes"], answer:1},
     {q:"Which province is known for the Rocky Mountains?", options:["Quebec","Ontario","Nova Scotia","British Columbia"], answer:3},
     {q:"Why are laws important in a community?", options:["They stop fun","They are not important","They keep people safe and treat fairly","Only adults benefit from laws"], answer:2},
     {q:"Which is a right that every child should have?", options:["The right to stay up all night","The right to own the most toys","The right to never follow rules","The right to education and safety"], answer:3},
     {q:"Canada is the __ largest country in the world by area.", options:["First","Second","Tenth","Third"], answer:1},
   ]},
]},
{day:31, label:"Day 31 — Mon", subjects:[
  {subject:"Language", title:"Consonant Blends: bl, cl, fl, gl", summary:"Students learn beginning consonant blends where two consonants join and both sounds are heard, such as bl in black, cl in clap, fl in flag, and gl in glow.",
   resourceLabel:"YouTube: Consonant Blends: bl, cl, fl, gl", resourceUrl:"https://www.youtube.com/results?search_query=Consonant%20Blends%3A%20bl%2C%20cl%2C%20fl%2C%20gl%20grade%202%20educational",
   quiz:[
     {q:"Which word begins with the bl blend?", options:["Black","Cat","Dog","Sun"], answer:0},
     {q:"Which word begins with the cl blend?", options:["Cat","Bed","Sun","Clap"], answer:3},
     {q:"Which word begins with the fl blend?", options:["Sun","Cat","Dog","Flag"], answer:3},
     {q:"Which word begins with the gl blend?", options:["Cat","Glow","Dog","Sun"], answer:1},
     {q:"A consonant blend is two consonants that ___.", options:["Always make one new sound like a digraph","Are always silent","Blend together with both sounds heard","Never appear together"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one word that begins with the bl blend, like black or blue.", answers:["black","blue","blow","blob"]},
     {prompt:"What two letters begin the word clap?", answers:["cl"]},
     {prompt:"Name one word that begins with the gl blend, like glow or glue.", answers:["glow","glue","glass"]}
   ]},
  {subject:"Math", title:"Addition Within 100 (With Regrouping)", summary:"Students add two-digit numbers within 100 that require regrouping a ten when the ones digits add to 10 or more.",
   resourceLabel:"YouTube: Addition Within 100 (With Regrouping)", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20Within%20100%20%28With%20Regrouping%29%20grade%202%20educational",
   quiz:[
     {q:"What is 27 + 15?", options:["43","41","32","42"], answer:3},
     {q:"What is 38 + 26?", options:["54","65","63","64"], answer:3},
     {q:"What is 46 + 19?", options:["64","55","66","65"], answer:3},
     {q:"When the ones digits add to 10 or more, we ___.", options:["Regroup a ten into the tens column","Ignore the extra","Stop the problem","Subtract instead"], answer:0},
     {q:"What is 55 + 27?", options:["82","81","72","83"], answer:0}
   ],
   worksheet:[
     {prompt:"What is 27 + 15?", answers:["42","forty-two","forty two"]},
     {prompt:"When adding 38 + 26, do the ones digits add up to 10 or more?", answers:["yes"]},
     {prompt:"What is 46 + 19?", answers:["65","sixty-five","sixty five"]}
   ]},
  {subject:"Science", title:"Nocturnal Animals: Creatures of the Night", summary:"Students learn that nocturnal animals, such as owls and bats, are awake and active at night and sleep during the day, often having special senses like keen hearing or eyesight to help them in the dark.",
   resourceLabel:"YouTube: Nocturnal Animals: Creatures of the Night", resourceUrl:"https://www.youtube.com/results?search_query=Nocturnal%20Animals%3A%20Creatures%20of%20the%20Night%20grade%202%20educational",
   quiz:[
     {q:"What do we call an animal that is active mainly at night?", options:["A hibernating animal","A migrating animal","A nocturnal animal","A diurnal animal"], answer:2},
     {q:"Which of these animals is known for being nocturnal?", options:["An owl","A butterfly","A robin","A squirrel"], answer:0},
     {q:"Nocturnal animals usually sleep during ___.", options:["Every other hour","The night","The day","Only in winter"], answer:2},
     {q:"Why might keen hearing help a nocturnal animal?", options:["It helps them find food and avoid danger in the dark","It helps them change colour","It helps them build nests only","It helps them fly to warmer places"], answer:0},
     {q:"Which sense often helps owls hunt at night?", options:["Taste only","Smell only","Hearing and sight","Touch only"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call an animal that is awake mostly at night?", answers:["a nocturnal animal","nocturnal"]},
     {prompt:"Name one nocturnal animal, like an owl or a bat.", answers:["an owl","owl","a bat","bat"]},
     {prompt:"Do nocturnal animals usually sleep during the day?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Farms and Where Our Food Comes From", summary:"Students learn that much of our food is grown or raised on farms, where farmers grow crops like wheat and vegetables and raise animals like cows and chickens, before the food travels to stores.",
   resourceLabel:"YouTube: Farms and Where Our Food Comes From", resourceUrl:"https://www.youtube.com/results?search_query=Farms%20and%20Where%20Our%20Food%20Comes%20From%20grade%202%20educational",
   quiz:[
     {q:"Where does much of our food come from before it reaches a store?", options:["A library","A farm","A school","A hospital"], answer:1},
     {q:"Which of these is a crop a farmer might grow?", options:["A television","Wheat","A shoe","A car"], answer:1},
     {q:"Which of these animals might a farmer raise for food?", options:["A cow","A tiger","A lion","A whale"], answer:0},
     {q:"After food is grown or raised on a farm, it usually ___.", options:["Stays on the farm forever","Is never eaten","Travels to stores for people to buy","Disappears completely"], answer:2},
     {q:"Why are farms important to communities?", options:["They print newspapers","They teach students","They build houses","They grow and raise much of the food we eat"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one place where much of our food is grown or raised.", answers:["a farm","farm"]},
     {prompt:"Name one crop a farmer might grow, like wheat or corn.", answers:["wheat","corn","vegetables"]},
     {prompt:"Does food usually travel from a farm to a store before we buy it?", answers:["yes"]}
   ]},
]},
{day:32, label:"Day 32 — Tue", subjects:[
  {subject:"Language", title:"Consonant Digraphs: sh, ch, th, wh", summary:"Students learn that a consonant digraph is two consonants that combine to make one new sound, such as sh in ship, ch in chip, th in thin, and wh in whale.",
   resourceLabel:"YouTube: Consonant Digraphs: sh, ch, th, wh", resourceUrl:"https://www.youtube.com/results?search_query=Consonant%20Digraphs%3A%20sh%2C%20ch%2C%20th%2C%20wh%20grade%202%20educational",
   quiz:[
     {q:"Which word begins with the sh digraph?", options:["Sun","Cat","Ship","Dog"], answer:2},
     {q:"Which word begins with the ch digraph?", options:["Dog","Cat","Sun","Chip"], answer:3},
     {q:"Which word begins with the th digraph?", options:["Dog","Sun","Cat","Thin"], answer:3},
     {q:"Which word begins with the wh digraph?", options:["Cat","Sun","Whale","Dog"], answer:2},
     {q:"A consonant digraph is two consonants that ___.", options:["Are always silent","Always keep both sounds separate","Combine to make one new sound","Never appear together"], answer:2}
   ],
   worksheet:[
     {prompt:"What two letters make the beginning sound in the word ship?", answers:["sh"]},
     {prompt:"Name one word that begins with the ch digraph, like chip or chair.", answers:["chip","chair","chin"]},
     {prompt:"What two letters make the beginning sound in the word whale?", answers:["wh"]}
   ]},
  {subject:"Math", title:"Subtraction Within 100 (With Regrouping)", summary:"Students subtract two-digit numbers within 100 that require regrouping a ten when the ones digit of the first number is smaller than the ones digit being subtracted.",
   resourceLabel:"YouTube: Subtraction Within 100 (With Regrouping)", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20Within%20100%20%28With%20Regrouping%29%20grade%202%20educational",
   quiz:[
     {q:"What is 52 - 27?", options:["24","35","25","26"], answer:2},
     {q:"What is 43 - 18?", options:["35","24","26","25"], answer:3},
     {q:"What is 71 - 36?", options:["35","34","36","45"], answer:0},
     {q:"We regroup (borrow) a ten when ___.", options:["The numbers are both even","The ones digit we are subtracting from is too small","We are adding not subtracting","The tens digits are equal"], answer:1},
     {q:"What is 80 - 45?", options:["45","36","34","35"], answer:3}
   ],
   worksheet:[
     {prompt:"What is 52 - 27?", answers:["25","twenty-five","twenty five"]},
     {prompt:"When subtracting 43 - 18, is the ones digit 3 smaller than 8?", answers:["yes"]},
     {prompt:"What is 71 - 36?", answers:["35","thirty-five","thirty five"]}
   ]},
  {subject:"Science", title:"Insects and Their Body Parts", summary:"Students learn that insects are small animals with six legs and three main body parts, head, thorax, and abdomen, and that many insects also have wings and antennae.",
   resourceLabel:"YouTube: Insects and Their Body Parts", resourceUrl:"https://www.youtube.com/results?search_query=Insects%20and%20Their%20Body%20Parts%20grade%202%20educational",
   quiz:[
     {q:"How many legs does an insect have?", options:["Four","Six","Ten","Eight"], answer:1},
     {q:"What are the three main body parts of an insect?", options:["Head, thorax, and abdomen","Legs, eyes, and fur","Shell, fin, and gills","Head, tail, and wings"], answer:0},
     {q:"Which body part do many insects use to sense their surroundings?", options:["Fins","Fur","Antennae","Gills"], answer:2},
     {q:"Which of these is an example of an insect?", options:["A worm","A spider","A ladybug","A snail"], answer:2},
     {q:"How is a spider different from an insect?", options:["A spider has six legs, not eight","A spider has wings","A spider has eight legs, not six","An insect has eight legs"], answer:2}
   ],
   worksheet:[
     {prompt:"How many legs does an insect have?", answers:["6","six"]},
     {prompt:"Name the three main body parts of an insect: head, thorax, and ___.", answers:["abdomen"]},
     {prompt:"Name one body part many insects use to sense their surroundings, like antennae.", answers:["antennae","wings"]}
   ]},
  {subject:"SocialStudies", title:"Community Types: City, Suburb, and Countryside", summary:"Students compare different types of communities, such as a busy city with tall buildings, a quieter suburb with houses close together, and the countryside with farms and open land.",
   resourceLabel:"YouTube: Community Types: City, Suburb, and Countryside", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Types%3A%20City%2C%20Suburb%2C%20and%20Countryside%20grade%202%20educational",
   quiz:[
     {q:"Which type of community usually has tall buildings and many people?", options:["The countryside","A forest","An ocean","A city"], answer:3},
     {q:"Which type of community usually has farms and open land?", options:["A subway","The countryside","A skyscraper","A city"], answer:1},
     {q:"A suburb is usually ___.", options:["Found only underwater","The same as a farm","Busier than any city","Between a city and the countryside in size and busyness"], answer:3},
     {q:"Which of these might you find in a city but not usually in the countryside?", options:["Large farms","Quiet forests only","Wide open fields","Many tall buildings close together"], answer:3},
     {q:"Why do different communities look different from each other?", options:["They are built to fit the land and the needs of the people there","Communities never change","Only cities have people","All communities look exactly the same"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one type of community with tall buildings and many people, like a city.", answers:["a city","city"]},
     {prompt:"Name one type of community with farms and open land, like the countryside.", answers:["the countryside","countryside","rural area"]},
     {prompt:"Are suburbs usually busier than the countryside but quieter than a city?", answers:["yes"]}
   ]},
]},
{day:33, label:"Day 33 — Wed", subjects:[
  {subject:"Language", title:"Common and Proper Nouns", summary:"Students learn that a common noun names a general person, place, or thing, like city or dog, while a proper noun names a specific one and begins with a capital letter, like Toronto or Rex.",
   resourceLabel:"YouTube: Common and Proper Nouns", resourceUrl:"https://www.youtube.com/results?search_query=Common%20and%20Proper%20Nouns%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a common noun?", options:["Dog","Monday","Toronto","Canada"], answer:0},
     {q:"Which of these is a proper noun?", options:["dog","Toronto","city","boy"], answer:1},
     {q:"A proper noun always begins with a ___.", options:["Number","Capital letter","Question mark","Lowercase letter"], answer:1},
     {q:"Which sentence uses a proper noun correctly?", options:["My friend lives in Toronto.","My Friend lives in toronto.","My friend lives in toronto.","my friend lives in Toronto."], answer:0},
     {q:"Which of these is a common noun, not a proper noun?", options:["Canada","City","Monday","Toronto"], answer:1}
   ],
   worksheet:[
     {prompt:"Is the word dog a common noun or a proper noun?", answers:["common noun","common"]},
     {prompt:"Is the word Toronto a common noun or a proper noun?", answers:["proper noun","proper"]},
     {prompt:"Should a proper noun begin with a capital letter?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Telling Time to Five-Minute Intervals", summary:"Students learn to read an analog clock to the nearest five minutes, counting by 5s around the clock face starting from the 12.",
   resourceLabel:"YouTube: Telling Time to Five-Minute Intervals", resourceUrl:"https://www.youtube.com/results?search_query=Telling%20Time%20to%20Five-Minute%20Intervals%20grade%202%20educational",
   quiz:[
     {q:"If the minute hand points to the 3, what time is it past the hour?", options:["15 minutes","5 minutes","20 minutes","30 minutes"], answer:0},
     {q:"If the minute hand points to the 6, what time is it past the hour?", options:["45 minutes","30 minutes","15 minutes","6 minutes"], answer:1},
     {q:"If the minute hand points to the 9, what time is it past the hour?", options:["15 minutes","30 minutes","9 minutes","45 minutes"], answer:3},
     {q:"When reading a clock, each number represents ___ minutes.", options:["5","15","10","1"], answer:0},
     {q:"If the hour hand is between 2 and 3, and the minute hand points to the 6, what time is it?", options:["2:15","6:02","2:30","3:30"], answer:2}
   ],
   worksheet:[
     {prompt:"If the minute hand points to the 3, how many minutes past the hour is it?", answers:["15"]},
     {prompt:"If the minute hand points to the 6, how many minutes past the hour is it?", answers:["30"]},
     {prompt:"Counting by 5s around a clock face, what number comes after 20?", answers:["25"]}
   ]},
  {subject:"Science", title:"Recycling and Reducing Waste", summary:"Students learn that recycling turns used materials like paper, plastic, and glass into new products, and that reducing and reusing waste helps protect the environment.",
   resourceLabel:"YouTube: Recycling and Reducing Waste", resourceUrl:"https://www.youtube.com/results?search_query=Recycling%20and%20Reducing%20Waste%20grade%202%20educational",
   quiz:[
     {q:"What is recycling?", options:["Burying all waste","Burning all garbage","Turning used materials into new products","Throwing everything away"], answer:2},
     {q:"Which of these materials can often be recycled?", options:["Water","Food scraps only","Air","Paper"], answer:3},
     {q:"Which action helps reduce waste?", options:["Reusing a shopping bag","Buying more than you need","Wasting paper","Throwing away items that still work"], answer:0},
     {q:"Why is recycling helpful for the environment?", options:["It creates more garbage","It has no effect","It uses up more resources","It saves materials and reduces garbage"], answer:3},
     {q:"Which of these bins would glass bottles most likely go into?", options:["A recycling bin","A garden","A closet","A pond"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one material that can be recycled, like paper or plastic.", answers:["paper","plastic","glass"]},
     {prompt:"What do we call turning used materials into new products?", answers:["recycling"]},
     {prompt:"Name one way to reduce waste, like reusing a bag.", answers:["reusing a bag","reusing","using less"]}
   ]},
  {subject:"SocialStudies", title:"Provinces and Territories of Canada", summary:"Students learn that Canada is divided into ten provinces and three territories, each with its own capital city, and that Ontario is the province where they live.",
   resourceLabel:"YouTube: Provinces and Territories of Canada", resourceUrl:"https://www.youtube.com/results?search_query=Provinces%20and%20Territories%20of%20Canada%20grade%202%20educational",
   quiz:[
     {q:"What do we call the large regions Canada is divided into, such as Ontario and Quebec?", options:["Oceans","Provinces","Countries","Continents"], answer:1},
     {q:"How many provinces does Canada have?", options:["3","5","13","10"], answer:3},
     {q:"Besides provinces, Canada also has three ___.", options:["Continents","Capitals","Oceans","Territories"], answer:3},
     {q:"Which of these is a province in Canada?", options:["London","Texas","France","Ontario"], answer:3},
     {q:"Each province and territory in Canada has its own ___.", options:["Continent","Ocean","Capital city","Language spoken by everyone"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the large regions Canada is divided into, like Ontario?", answers:["provinces"]},
     {prompt:"How many provinces does Canada have?", answers:["10","ten"]},
     {prompt:"Name the province where Ontario students live.", answers:["Ontario"]}
   ]},
]},
{day:34, label:"Day 34 — Thu", subjects:[
  {subject:"Language", title:"Pronouns: He, She, It, They", summary:"Students learn that a pronoun is a word that can take the place of a noun, such as using he for a boy, she for a girl, it for a thing, and they for more than one person or thing.",
   resourceLabel:"YouTube: Pronouns: He, She, It, They", resourceUrl:"https://www.youtube.com/results?search_query=Pronouns%3A%20He%2C%20She%2C%20It%2C%20They%20grade%202%20educational",
   quiz:[
     {q:"Which pronoun could replace the noun Sam if Sam is a boy?", options:["They","She","He","It"], answer:2},
     {q:"Which pronoun could replace the noun Maria if Maria is a girl?", options:["It","He","They","She"], answer:3},
     {q:"Which pronoun could replace the words the two cats?", options:["She","It","He","They"], answer:3},
     {q:"Which pronoun could replace the word ball?", options:["They","It","She","He"], answer:1},
     {q:"A pronoun is a word that ___.", options:["Takes the place of a noun","Describes a noun","Joins two sentences","Shows an action"], answer:0}
   ],
   worksheet:[
     {prompt:"Which pronoun could replace the word boy?", answers:["he"]},
     {prompt:"Which pronoun could replace the word girl?", answers:["she"]},
     {prompt:"Which pronoun could replace the words the dogs?", answers:["they"]}
   ]},
  {subject:"Math", title:"Measuring Length with Centimetres and Metres", summary:"Students learn to measure the length of objects using standard units, choosing centimetres for shorter objects like a pencil and metres for longer distances like a hallway.",
   resourceLabel:"YouTube: Measuring Length with Centimetres and Metres", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Length%20with%20Centimetres%20and%20Metres%20grade%202%20educational",
   quiz:[
     {q:"Which unit would you use to measure the length of a pencil?", options:["Kilograms","Centimetres","Litres","Metres"], answer:1},
     {q:"Which unit would you use to measure the length of a hallway?", options:["Millilitres","Metres","Degrees","Centimetres"], answer:1},
     {q:"Which is longer, 1 metre or 1 centimetre?", options:["1 centimetre","They are equal","1 metre","Cannot tell"], answer:2},
     {q:"About how many centimetres long is a small paperclip?", options:["About 3 metres","About 3 centimetres","About 300 centimetres","About 30 metres"], answer:1},
     {q:"Choosing the right unit helps us measure length ___.", options:["Incorrectly","Loudly","Accurately","Randomly"], answer:2}
   ],
   worksheet:[
     {prompt:"Would you use centimetres or metres to measure a pencil?", answers:["centimetres"]},
     {prompt:"Would you use centimetres or metres to measure the length of a hallway?", answers:["metres"]},
     {prompt:"Which is longer, 1 metre or 1 centimetre?", answers:["1 metre","metre"]}
   ]},
  {subject:"Science", title:"States of Matter: Gases", summary:"Students learn that a gas is a state of matter that has no definite shape or volume and spreads out to fill its container, such as the air we breathe.",
   resourceLabel:"YouTube: States of Matter: Gases", resourceUrl:"https://www.youtube.com/results?search_query=States%20of%20Matter%3A%20Gases%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of a gas?", options:["Air","Juice","A rock","Ice"], answer:0},
     {q:"Does a gas have a definite shape of its own?", options:["Only when frozen","Yes, it always keeps one shape","Only sometimes","No, it takes the shape of its container"], answer:3},
     {q:"What happens to a gas inside a balloon?", options:["It stays in one corner","It spreads out to fill the whole balloon","It turns into a solid","It disappears completely"], answer:1},
     {q:"Which of the three states of matter usually cannot be seen?", options:["Liquid","Solid","Gas","None of them"], answer:2},
     {q:"Water can become a gas called water vapour when it ___.", options:["Turns into a rock","Evaporates and turns into a gas","Freezes solid","Becomes colder"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one example of a gas, like air.", answers:["air"]},
     {prompt:"Does a gas have a definite shape?", answers:["no"]},
     {prompt:"What state of matter fills up all the space in its container?", answers:["a gas","gas"]}
   ]},
  {subject:"SocialStudies", title:"Municipal Government: Mayors and Councils", summary:"Students learn that a municipal government, led by a mayor and council, makes decisions for a city or town, such as caring for parks, roads, and local services.",
   resourceLabel:"YouTube: Municipal Government: Mayors and Councils", resourceUrl:"https://www.youtube.com/results?search_query=Municipal%20Government%3A%20Mayors%20and%20Councils%20grade%202%20educational",
   quiz:[
     {q:"Who usually leads a city or town government?", options:["A principal","A mayor","A king","A farmer"], answer:1},
     {q:"Which of these is something a municipal government might take care of?", options:["Local roads and parks","Outer space","Ocean currents","The weather"], answer:0},
     {q:"How do people in a community usually choose their mayor?", options:["By voting in an election","By age only","By flipping a coin","It is never chosen"], answer:0},
     {q:"A group of elected people who help run a city along with the mayor is called the ___.", options:["School board","Sports team","City council","Farmers market"], answer:2},
     {q:"Why is local government important to a community?", options:["It makes decisions that affect daily life, like roads and parks","It never makes decisions","It only affects other countries","It has no effect on daily life"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the leader of a city or town government?", answers:["a mayor","mayor"]},
     {prompt:"Name one thing a municipal government might take care of, like roads or parks.", answers:["roads","parks","local services"]},
     {prompt:"Do people in a community vote to choose their mayor and council?", answers:["yes"]}
   ]},
]},
{day:35, label:"Day 35 — Fri", subjects:[
  {subject:"Language", title:"Review: Blends, Digraphs, Nouns and Pronouns", summary:"Students review recent Language skills: consonant blends, consonant digraphs, common and proper nouns, and pronouns.",
   resourceLabel:"YouTube: Review: Blends, Digraphs, Nouns and Pronouns", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Blends%2C%20Digraphs%2C%20Nouns%20and%20Pronouns%20grade%202%20educational",
   quiz:[
     {q:"Which word begins with the bl blend?", options:["Black","Dog","Cat","Sun"], answer:0},
     {q:"Which word begins with the sh digraph?", options:["Dog","Cat","Ship","Sun"], answer:2},
     {q:"Which of these is a proper noun?", options:["city","boy","dog","Toronto"], answer:3},
     {q:"Which pronoun could replace the words the two cats?", options:["She","It","They","He"], answer:2},
     {q:"A consonant digraph is two consonants that ___.", options:["Never appear together","Are always silent","Always keep both sounds separate","Combine to make one new sound"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one word that begins with the bl blend, like black or blue.", answers:["black","blue","blow"]},
     {prompt:"What two letters make the beginning sound in the word ship?", answers:["sh"]},
     {prompt:"Which pronoun could replace the word boy?", answers:["he"]}
   ]},
  {subject:"Math", title:"Review: Regrouping, Time and Measuring", summary:"Students review recent Math skills: addition and subtraction within 100 with regrouping, telling time to five-minute intervals, and measuring length with centimetres and metres.",
   resourceLabel:"YouTube: Review: Regrouping, Time and Measuring", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Regrouping%2C%20Time%20and%20Measuring%20grade%202%20educational",
   quiz:[
     {q:"What is 27 + 15?", options:["32","41","43","42"], answer:3},
     {q:"What is 52 - 27?", options:["26","25","35","24"], answer:1},
     {q:"If the minute hand points to the 3, what time is it past the hour?", options:["20 minutes","15 minutes","5 minutes","30 minutes"], answer:1},
     {q:"Which unit would you use to measure the length of a hallway?", options:["Degrees","Centimetres","Millilitres","Metres"], answer:3},
     {q:"What is 46 + 19?", options:["64","55","65","66"], answer:2}
   ],
   worksheet:[
     {prompt:"What is 27 + 15?", answers:["42","forty-two","forty two"]},
     {prompt:"If the minute hand points to the 6, how many minutes past the hour is it?", answers:["30"]},
     {prompt:"Would you use centimetres or metres to measure a pencil?", answers:["centimetres"]}
   ]},
  {subject:"Science", title:"Review: Nocturnal Animals, Insects, Recycling and Gases", summary:"Students review recent Science topics: nocturnal animals, insects and their body parts, recycling and reducing waste, and the gas state of matter.",
   resourceLabel:"YouTube: Review: Nocturnal Animals, Insects, Recycling and Gases", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Nocturnal%20Animals%2C%20Insects%2C%20Recycling%20and%20Gases%20grade%202%20educational",
   quiz:[
     {q:"Which of these animals is known for being nocturnal?", options:["A squirrel","An owl","A robin","A butterfly"], answer:1},
     {q:"What are the three main body parts of an insect?", options:["Legs, eyes, and fur","Head, thorax, and abdomen","Head, tail, and wings","Shell, fin, and gills"], answer:1},
     {q:"Which of these materials can often be recycled?", options:["Air","Paper","Food scraps only","Water"], answer:1},
     {q:"Which of these is an example of a gas?", options:["A rock","Ice","Juice","Air"], answer:3},
     {q:"Why are nocturnal animals often good at hearing or seeing in the dark?", options:["It helps them fly to warmer places","It helps them find food and avoid danger at night","It helps them build nests only","It helps them change colour"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one nocturnal animal, like an owl or a bat.", answers:["an owl","owl","a bat","bat"]},
     {prompt:"How many legs does an insect have?", answers:["6","six"]},
     {prompt:"Name one material that can be recycled, like paper or plastic.", answers:["paper","plastic","glass"]}
   ]},
  {subject:"SocialStudies", title:"Review: Food Sources, Community Types, Provinces and Local Government", summary:"Students review recent Social Studies topics: where food comes from, types of communities, the provinces and territories of Canada, and municipal government.",
   resourceLabel:"YouTube: Review: Food Sources, Community Types, Provinces and Local Government", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Food%20Sources%2C%20Community%20Types%2C%20Provinces%20and%20Local%20Government%20grade%202%20educational",
   quiz:[
     {q:"Where does much of our food come from before it reaches a store?", options:["A farm","A school","A hospital","A library"], answer:0},
     {q:"Which type of community usually has farms and open land?", options:["The countryside","A subway","A skyscraper","A city"], answer:0},
     {q:"How many provinces does Canada have?", options:["10","13","3","5"], answer:0},
     {q:"Who usually leads a city or town government?", options:["A mayor","A farmer","A king","A principal"], answer:0},
     {q:"Why are farms important to communities?", options:["They build houses","They print newspapers","They teach students","They grow and raise much of the food we eat"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one place where much of our food is grown or raised.", answers:["a farm","farm"]},
     {prompt:"Name one type of community with tall buildings and many people, like a city.", answers:["a city","city"]},
     {prompt:"How many provinces does Canada have?", answers:["10","ten"]}
   ]},
]},
{day:36, label:"Day 36 — Mon", subjects:[
  {subject:"Language", title:"Prefixes: un- and re-", summary:"Students learn that the prefixes un- and re- can be added to the beginning of a word to change its meaning, with un- often meaning not, and re- often meaning again.",
   resourceLabel:"YouTube: Prefixes: un- and re-", resourceUrl:"https://www.youtube.com/results?search_query=Prefixes%3A%20un-%20and%20re-%20grade%202%20educational",
   quiz:[
     {q:"What does the prefix un- usually mean?", options:["Again","Always","Before","Not"], answer:3},
     {q:"What does the prefix re- usually mean?", options:["Before","Never","Not","Again"], answer:3},
     {q:"Which word means to do something again by using the prefix re-?", options:["Redo","Predo","Undo","Disdo"], answer:0},
     {q:"Which word means not happy by using the prefix un-?", options:["Unhappy","Prehappy","Rehappy","Dishappy"], answer:0},
     {q:"A prefix is added to the ___ of a word to change its meaning.", options:["Middle","Beginning","End","Nowhere"], answer:1}
   ],
   worksheet:[
     {prompt:"What does the prefix un- usually mean, as in unhappy?", answers:["not"]},
     {prompt:"What does the prefix re- usually mean, as in redo?", answers:["again"]},
     {prompt:"Name one word that begins with the prefix un-, like unhappy or unsafe.", answers:["unhappy","unsafe","unfair"]}
   ]},
  {subject:"Math", title:"Fractions: Thirds and Eighths", summary:"Students explore fractions with thirds and eighths, understanding that a whole can be split into 3 or 8 equal parts, each called one third or one eighth.",
   resourceLabel:"YouTube: Fractions: Thirds and Eighths", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%3A%20Thirds%20and%20Eighths%20grade%202%20educational",
   quiz:[
     {q:"If a whole is split into 3 equal parts, each part is called ___.", options:["One eighth","One half","One quarter","One third"], answer:3},
     {q:"If a whole is split into 8 equal parts, each part is called ___.", options:["One half","One third","One whole","One eighth"], answer:3},
     {q:"Which is bigger, one third or one eighth of the same pizza?", options:["They are equal","One eighth","One third","Cannot tell"], answer:2},
     {q:"Three friends sharing a pizza equally would each get ___ of the pizza.", options:["One half","One eighth","One third","The whole pizza"], answer:2},
     {q:"Splitting a whole into more equal parts makes each part ___.", options:["Disappear","Smaller","Bigger","Stay the same size"], answer:1}
   ],
   worksheet:[
     {prompt:"If a pizza is cut into 3 equal parts, what is each part called?", answers:["one third","a third"]},
     {prompt:"If a chocolate bar is cut into 8 equal parts, what is each part called?", answers:["one eighth","an eighth"]},
     {prompt:"Which is bigger, one third or one eighth of the same whole?", answers:["one third","a third"]}
   ]},
  {subject:"Science", title:"Magnets: Push and Pull Without Touching", summary:"Students learn that a magnet can push or pull certain metal objects without touching them, and that magnets have two ends called poles that can attract or repel each other.",
   resourceLabel:"YouTube: Magnets: Push and Pull Without Touching", resourceUrl:"https://www.youtube.com/results?search_query=Magnets%3A%20Push%20and%20Pull%20Without%20Touching%20grade%202%20educational",
   quiz:[
     {q:"What can a magnet do to certain metal objects without touching them?", options:["Make them disappear","Change their colour","Melt them","Push or pull them"], answer:3},
     {q:"Which of these materials would a magnet most likely attract?", options:["An iron nail","A plastic cup","A wooden block","A paper towel"], answer:0},
     {q:"What do we call the two ends of a magnet?", options:["Tips","Wheels","Poles","Corners"], answer:2},
     {q:"What happens when two magnets with the same pole are brought close together?", options:["They melt","They always stick together","They disappear","They push each other away"], answer:3},
     {q:"What happens when two magnets with opposite poles are brought close together?", options:["They always push apart","They melt","They disappear","They attract and pull together"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the force a magnet uses to attract or push away objects?", answers:["magnetism","magnetic force"]},
     {prompt:"Name one material that a magnet can attract, like iron or steel.", answers:["iron","steel"]},
     {prompt:"Do magnets have two ends called poles?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Immigration: New Families Joining Canada", summary:"Students learn that immigration is when people move from one country to make a new home in another country, and that many families have come to Canada from around the world, adding to its cultures and traditions.",
   resourceLabel:"YouTube: Immigration: New Families Joining Canada", resourceUrl:"https://www.youtube.com/results?search_query=Immigration%3A%20New%20Families%20Joining%20Canada%20grade%202%20educational",
   quiz:[
     {q:"What is immigration?", options:["When animals migrate with the seasons","When people travel on vacation","When people move from one country to live in another","When a family moves within the same city"], answer:2},
     {q:"What do we call a person who has moved to a new country to live?", options:["An immigrant","A citizen only","A tourist","A visitor only"], answer:0},
     {q:"Why might a family choose to immigrate to Canada?", options:["To find new opportunities, safety, or to be with family","Only for a short vacation","To avoid all other countries","Canada has no reasons to immigrate to"], answer:0},
     {q:"How do immigrant families often help Canadian communities?", options:["They do not help communities","By changing nothing about the community","By sharing their cultures, languages, and traditions","By keeping to themselves only"], answer:2},
     {q:"Canada is often described as a country made up of ___.", options:["Only one culture","People from many different cultures and backgrounds","Only people born in Canada","No immigrants at all"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call it when people move from one country to live in another?", answers:["immigration"]},
     {prompt:"What do we call a person who moves to a new country to live?", answers:["an immigrant","immigrant"]},
     {prompt:"Do families who immigrate to Canada bring their own traditions and cultures?", answers:["yes"]}
   ]},
]},
{day:37, label:"Day 37 — Tue", subjects:[
  {subject:"Language", title:"Suffixes: -ful and -less", summary:"Students learn that the suffixes -ful and -less can be added to the end of a word, with -ful often meaning full of, and -less often meaning without.",
   resourceLabel:"YouTube: Suffixes: -ful and -less", resourceUrl:"https://www.youtube.com/results?search_query=Suffixes%3A%20-ful%20and%20-less%20grade%202%20educational",
   quiz:[
     {q:"What does the suffix -ful usually mean?", options:["Before","Full of","Again","Without"], answer:1},
     {q:"What does the suffix -less usually mean?", options:["Without","Full of","Never before","Always"], answer:0},
     {q:"Which word means without help by using the suffix -less?", options:["Helpless","Helpful","Prehelp","Rehelp"], answer:0},
     {q:"Which word means full of joy by using the suffix -ful?", options:["Joyful","Prejoy","Rejoy","Joyless"], answer:0},
     {q:"A suffix is added to the ___ of a word to change its meaning.", options:["Beginning","End","Nowhere","Middle"], answer:1}
   ],
   worksheet:[
     {prompt:"What does the suffix -ful usually mean, as in joyful?", answers:["full of"]},
     {prompt:"What does the suffix -less usually mean, as in helpless?", answers:["without"]},
     {prompt:"Name one word that ends in -ful, like joyful or careful.", answers:["joyful","careful","colourful"]}
   ]},
  {subject:"Math", title:"Odd and Even Numbers", summary:"Students learn to identify odd and even numbers, understanding that even numbers can be split into two equal groups and odd numbers cannot.",
   resourceLabel:"YouTube: Odd and Even Numbers", resourceUrl:"https://www.youtube.com/results?search_query=Odd%20and%20Even%20Numbers%20grade%202%20educational",
   quiz:[
     {q:"Is the number 8 odd or even?", options:["Even","Both","Neither","Odd"], answer:0},
     {q:"Is the number 7 odd or even?", options:["Odd","Neither","Even","Both"], answer:0},
     {q:"Which of these numbers is even?", options:["11","13","10","15"], answer:2},
     {q:"Which of these numbers is odd?", options:["6","9","8","4"], answer:1},
     {q:"An even number can always be split into ___.", options:["Three equal groups","Odd groups only","No equal groups","Two equal groups"], answer:3}
   ],
   worksheet:[
     {prompt:"Is the number 8 odd or even?", answers:["even"]},
     {prompt:"Is the number 7 odd or even?", answers:["odd"]},
     {prompt:"Can an even number always be split into two equal groups?", answers:["yes"]}
   ]},
  {subject:"Science", title:"The Water Cycle", summary:"Students learn about the water cycle, the process where water evaporates into the air, forms clouds through condensation, and falls back to the earth as precipitation like rain or snow.",
   resourceLabel:"YouTube: The Water Cycle", resourceUrl:"https://www.youtube.com/results?search_query=The%20Water%20Cycle%20grade%202%20educational",
   quiz:[
     {q:"What do we call water turning into vapour and rising into the air?", options:["Freezing","Condensation","Evaporation","Precipitation"], answer:2},
     {q:"What do we call water vapour forming into clouds?", options:["Evaporation","Condensation","Melting","Precipitation"], answer:1},
     {q:"What do we call rain or snow falling from clouds to the ground?", options:["Freezing","Precipitation","Evaporation","Condensation"], answer:1},
     {q:"Where does most of the water that evaporates come from?", options:["Only underground caves","Only clouds","Oceans, lakes, and rivers","Only swimming pools"], answer:2},
     {q:"The water cycle describes how water ___.", options:["Only exists in oceans","Moves between the earth, air, and clouds again and again","Never moves at all","Disappears forever after it rains"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call water turning into vapour and rising into the air?", answers:["evaporation"]},
     {prompt:"What do we call rain or snow falling from clouds?", answers:["precipitation"]},
     {prompt:"Name one form precipitation can take, like rain or snow.", answers:["rain","snow"]}
   ]},
  {subject:"SocialStudies", title:"My Body Belongs to Me: Personal Safety", summary:"Students learn that their body belongs to them, that they can say no to touches that make them uncomfortable, and that they should tell a trusted adult if something makes them feel unsafe.",
   resourceLabel:"YouTube: My Body Belongs to Me: Personal Safety", resourceUrl:"https://www.youtube.com/results?search_query=My%20Body%20Belongs%20to%20Me%3A%20Personal%20Safety%20grade%202%20educational",
   quiz:[
     {q:"Whose body belongs to a child?", options:["Only their parents decide everything about it","Their own body belongs to them","No one, it belongs to strangers","Only their teacher"], answer:1},
     {q:"What can a child do if a touch makes them feel uncomfortable or unsafe?", options:["Ignore the feeling completely","Do whatever they are told","Say no and tell a trusted adult","Stay quiet and never tell anyone"], answer:2},
     {q:"Who could be a trusted adult a child talks to about feeling unsafe?", options:["A stranger","A parent or teacher","Only another child","No one at all"], answer:1},
     {q:"Why is it important for children to know their body belongs to them?", options:["It helps them stay safe and speak up if something feels wrong","Children should never speak up","It only matters for adults","It has no importance"], answer:0},
     {q:"If something makes a child feel unsafe, a helpful first step is to ___.", options:["Ignore it and hope it stops","Blame themselves","Tell a trusted adult right away","Keep it a secret forever"], answer:2}
   ],
   worksheet:[
     {prompt:"Whose body belongs to you?", answers:["my body","mine","yours"]},
     {prompt:"What should you do if a touch makes you feel unsafe or uncomfortable?", answers:["say no","tell a trusted adult"]},
     {prompt:"Name one person who could be a trusted adult, like a parent or teacher.", answers:["a parent","parent","a teacher","teacher"]}
   ]},
]},
{day:38, label:"Day 38 — Wed", subjects:[
  {subject:"Language", title:"Comparing with -er and -est", summary:"Students learn that the suffixes -er and -est can be added to describing words to compare things, with -er comparing two things, as in taller, and -est comparing three or more, as in tallest.",
   resourceLabel:"YouTube: Comparing with -er and -est", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20with%20-er%20and%20-est%20grade%202%20educational",
   quiz:[
     {q:"Which suffix compares exactly two things?", options:["-less","-ful","-est","-er"], answer:3},
     {q:"Which suffix compares three or more things?", options:["-er","-ful","-est","-less"], answer:2},
     {q:"Which word correctly compares two runners?", options:["Fast","Fasting","Fastest","Faster"], answer:3},
     {q:"Which word correctly compares the tallest person in a whole class?", options:["Tallest","Tall","Talling","Taller"], answer:0},
     {q:"If Sam is tall, Mia is taller, and Leo is the ___, Leo is the tallest of all three.", options:["Tallness","Taller","Tallest","Tall"], answer:2}
   ],
   worksheet:[
     {prompt:"If comparing two children heights, which word would you use, taller or tallest?", answers:["taller"]},
     {prompt:"If comparing the heights of a whole class, which word would you use, taller or tallest?", answers:["tallest"]},
     {prompt:"Add -er to the word fast to compare two runners.", answers:["faster"]}
   ]},
  {subject:"Math", title:"Repeating Patterns with Shapes and Numbers", summary:"Students identify and extend repeating patterns made from shapes, colours, or numbers, recognizing the core unit that repeats over and over.",
   resourceLabel:"YouTube: Repeating Patterns with Shapes and Numbers", resourceUrl:"https://www.youtube.com/results?search_query=Repeating%20Patterns%20with%20Shapes%20and%20Numbers%20grade%202%20educational",
   quiz:[
     {q:"In the pattern circle, square, circle, square, ___, what comes next?", options:["Star","Triangle","Square","Circle"], answer:3},
     {q:"In the pattern 3, 6, 3, 6, 3, ___, what comes next?", options:["12","9","6","3"], answer:2},
     {q:"In the pattern red, blue, blue, red, blue, blue, ___, what comes next?", options:["Blue","Yellow","Green","Red"], answer:3},
     {q:"What do we call the smallest part of a pattern that repeats over and over?", options:["The end","The core","The total","The middle"], answer:1},
     {q:"A repeating pattern is one where the core ___.", options:["Only appears once","Repeats again and again","Gets bigger each time","Never repeats"], answer:1}
   ],
   worksheet:[
     {prompt:"In the pattern circle, square, circle, square, what shape comes next?", answers:["circle"]},
     {prompt:"In the pattern 2, 4, 2, 4, 2, what number comes next?", answers:["4","four"]},
     {prompt:"What do we call the smallest part of a pattern that repeats?", answers:["the core","core"]}
   ]},
  {subject:"Science", title:"Rocks and Soil: What the Earth is Made Of", summary:"Students learn that rocks come in many shapes, sizes, and colours, and that soil is made up of tiny broken bits of rock mixed with decayed plants and animals, which helps plants grow.",
   resourceLabel:"YouTube: Rocks and Soil: What the Earth is Made Of", resourceUrl:"https://www.youtube.com/results?search_query=Rocks%20and%20Soil%3A%20What%20the%20Earth%20is%20Made%20Of%20grade%202%20educational",
   quiz:[
     {q:"What is soil made up of?", options:["Only glass","Tiny broken bits of rock mixed with decayed plants and animals","Only water","Only metal"], answer:1},
     {q:"Which of these is true about rocks?", options:["They are always tiny","They are all exactly the same","They are all soft","They come in many shapes, sizes, and colours"], answer:3},
     {q:"Why is soil important for plants?", options:["It only harms plants","It provides nutrients and support for roots to grow","It has no use for plants","It stops plants from growing"], answer:1},
     {q:"Over a very long time, rocks can slowly break down into ___.", options:["Tiny pieces that become part of soil","Water","Gas","Metal"], answer:0},
     {q:"Which of these is an example of a rock?", options:["Air","Water","Granite","Wood"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one thing soil is made of, like broken rock or decayed plants.", answers:["broken rock","decayed plants","tiny rock pieces"]},
     {prompt:"Do rocks come in different shapes, sizes, and colours?", answers:["yes"]},
     {prompt:"Does soil help plants grow?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Saving and Spending Money Wisely", summary:"Students learn the difference between saving money for later and spending money now, and that making thoughtful choices about money helps people reach their goals.",
   resourceLabel:"YouTube: Saving and Spending Money Wisely", resourceUrl:"https://www.youtube.com/results?search_query=Saving%20and%20Spending%20Money%20Wisely%20grade%202%20educational",
   quiz:[
     {q:"What does it mean to save money?", options:["Giving all your money away","Putting money aside instead of spending it right away","Losing your money","Spending all your money right away"], answer:1},
     {q:"What does it mean to spend money?", options:["Using money to buy something","Putting money away for later","Hiding money","Throwing money away"], answer:0},
     {q:"Why might someone choose to save money instead of spending it right away?", options:["To lose track of it","Money should never be saved","To buy something bigger or more important later","Saving money is never useful"], answer:2},
     {q:"Which of these is an example of making a wise choice about money?", options:["Thinking before spending and saving some for later","Losing money on purpose","Never thinking about money at all","Spending every coin the moment you get it"], answer:0},
     {q:"Making thoughtful choices about money can help someone ___.", options:["Waste all their money","Reach a savings goal","Never buy anything they want","Avoid ever having money"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call putting money aside instead of spending it right away?", answers:["saving"]},
     {prompt:"What do we call using money to buy something now?", answers:["spending"]},
     {prompt:"Can saving money help you buy something bigger later?", answers:["yes"]}
   ]},
]},
{day:39, label:"Day 39 — Thu", subjects:[
  {subject:"Language", title:"Writing a Simple Paragraph", summary:"Students learn that a simple paragraph has a topic sentence that introduces the main idea, a few detail sentences that add information, and stays focused on one idea.",
   resourceLabel:"YouTube: Writing a Simple Paragraph", resourceUrl:"https://www.youtube.com/results?search_query=Writing%20a%20Simple%20Paragraph%20grade%202%20educational",
   quiz:[
     {q:"What is a topic sentence?", options:["The last sentence in a story","A sentence with no meaning","The sentence that introduces the main idea of a paragraph","A question only"], answer:2},
     {q:"What do detail sentences in a paragraph do?", options:["Change the topic completely","Add more information about the main idea","Ask random questions","End the paragraph immediately"], answer:1},
     {q:"A good paragraph usually stays focused on ___.", options:["Only questions","No idea at all","Many unrelated ideas","One main idea"], answer:3},
     {q:"Which of these would make the best topic sentence for a paragraph about dogs?", options:["Dogs make wonderful pets for many families.","I like pizza for lunch.","Cars can be fast or slow.","The sky is blue today."], answer:0},
     {q:"Why is it important to stay on topic when writing a paragraph?", options:["It confuses the reader on purpose","Paragraphs do not need a topic","Readers prefer unrelated ideas","It helps the reader understand the main idea clearly"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the sentence that introduces the main idea of a paragraph?", answers:["the topic sentence","topic sentence"]},
     {prompt:"Should the sentences in a paragraph stay focused on one idea?", answers:["yes"]},
     {prompt:"Name one thing a detail sentence does in a paragraph, like adding information.", answers:["adds information","gives more details"]}
   ]},
  {subject:"Math", title:"Symmetry in Shapes", summary:"Students learn that a shape has symmetry if it can be folded along a line so that both halves match exactly, and that this line is called a line of symmetry.",
   resourceLabel:"YouTube: Symmetry in Shapes", resourceUrl:"https://www.youtube.com/results?search_query=Symmetry%20in%20Shapes%20grade%202%20educational",
   quiz:[
     {q:"A shape has symmetry if it can be folded so that ___.", options:["Both halves match exactly","One half disappears","Both halves are different sizes","It cannot be folded at all"], answer:0},
     {q:"What do we call the line where a symmetrical shape can be folded so both halves match?", options:["A border line","A line of symmetry","A number line","A curved line"], answer:1},
     {q:"Which of these shapes has a line of symmetry?", options:["An uneven shape","A square","A scribble","A random blob"], answer:1},
     {q:"How many lines of symmetry does a circle have?", options:["Exactly two","Exactly one","Many","None"], answer:2},
     {q:"Which of these letters has a line of symmetry?", options:["A","G","R","F"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call a shape that can be folded so both halves match exactly?", answers:["a symmetrical shape","symmetrical"]},
     {prompt:"What do we call the line where a symmetrical shape can be folded so both halves match?", answers:["a line of symmetry","line of symmetry"]},
     {prompt:"Does a circle have a line of symmetry?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Healthy Eating and the Food Groups", summary:"Students learn that eating a balance of different food groups, such as fruits, vegetables, grains, and proteins, helps their bodies grow strong and stay healthy.",
   resourceLabel:"YouTube: Healthy Eating and the Food Groups", resourceUrl:"https://www.youtube.com/results?search_query=Healthy%20Eating%20and%20the%20Food%20Groups%20grade%202%20educational",
   quiz:[
     {q:"Why is it important to eat a balance of different food groups?", options:["It only matters for adults","It makes food taste worse","It has no effect on health","It helps the body grow strong and stay healthy"], answer:3},
     {q:"Which of these is an example of a fruit or vegetable?", options:["An apple","A cookie","A candy bar","A soda"], answer:0},
     {q:"Which food group gives the body energy from foods like bread and rice?", options:["Only fats","Only sugar","Grains","Only sweets"], answer:2},
     {q:"Which of these is a healthy snack choice?", options:["A bag of candy","A can of soda","Carrot sticks","A bag of chips"], answer:2},
     {q:"Eating too much of only one food group and ignoring the others can ___.", options:["Always make you healthier","Make you grow taller instantly","Make it harder for the body to stay balanced and healthy","Have no effect at all"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one food group, like fruits or vegetables.", answers:["fruits","vegetables","grains","proteins"]},
     {prompt:"Does eating a balance of different food groups help your body stay healthy?", answers:["yes"]},
     {prompt:"Name one fruit or vegetable you could eat for a healthy snack.", answers:["an apple","apple","carrot","banana"]}
   ]},
  {subject:"SocialStudies", title:"Landmarks and Famous Places in Canada", summary:"Students learn about well-known Canadian landmarks, such as the CN Tower, Niagara Falls, and the Parliament Buildings, and why these places are important to the country.",
   resourceLabel:"YouTube: Landmarks and Famous Places in Canada", resourceUrl:"https://www.youtube.com/results?search_query=Landmarks%20and%20Famous%20Places%20in%20Canada%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a famous Canadian landmark?", options:["The Pyramids","The Great Wall","The CN Tower","The Eiffel Tower"], answer:2},
     {q:"In which city would you find the CN Tower?", options:["Montreal","Ottawa","Vancouver","Toronto"], answer:3},
     {q:"Which famous Canadian landmark is a large and powerful waterfall?", options:["Parliament Hill","The CN Tower","Niagara Falls","The Rocky Mountains"], answer:2},
     {q:"Where do Canadas government leaders meet, at a famous landmark in Ottawa?", options:["The Parliament Buildings","A shopping mall","Niagara Falls","The CN Tower"], answer:0},
     {q:"Why are landmarks important to a country?", options:["They are never visited","They are only found in other countries","They have no importance at all","They represent history, culture, or natural beauty"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one famous Canadian landmark, like the CN Tower or Niagara Falls.", answers:["the CN Tower","CN Tower","Niagara Falls"]},
     {prompt:"In which city is the CN Tower located?", answers:["Toronto"]},
     {prompt:"Name one reason people visit famous landmarks, like to learn about history.", answers:["to learn about history","to see something special","to visit"]}
   ]},
]},
{day:40, label:"Day 40 — Fri", subjects:[
  {subject:"Language", title:"Final Review: Prefixes, Suffixes, Comparing Words and Paragraphs", summary:"Students review recent Language skills: prefixes un- and re-, suffixes -ful and -less, comparing with -er and -est, and writing a simple paragraph.",
   resourceLabel:"YouTube: Final Review: Prefixes, Suffixes, Comparing Words and Paragraphs", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Prefixes%2C%20Suffixes%2C%20Comparing%20Words%20and%20Paragraphs%20grade%202%20educational",
   quiz:[
     {q:"What does the prefix un- usually mean?", options:["Before","Not","Always","Again"], answer:1},
     {q:"Which word means full of joy by using the suffix -ful?", options:["Joyless","Rejoy","Joyful","Prejoy"], answer:2},
     {q:"Which suffix compares three or more things?", options:["-est","-er","-less","-ful"], answer:0},
     {q:"What is a topic sentence?", options:["The sentence that introduces the main idea of a paragraph","A question only","The last sentence in a story","A sentence with no meaning"], answer:0},
     {q:"Which word means without help by using the suffix -less?", options:["Prehelp","Helpful","Helpless","Rehelp"], answer:2}
   ],
   worksheet:[
     {prompt:"What does the prefix re- usually mean, as in redo?", answers:["again"]},
     {prompt:"What does the suffix -less usually mean, as in helpless?", answers:["without"]},
     {prompt:"What do we call the sentence that introduces the main idea of a paragraph?", answers:["the topic sentence","topic sentence"]}
   ]},
  {subject:"Math", title:"Final Review: Fractions, Odd/Even, Patterns and Symmetry", summary:"Students review recent Math skills: thirds and eighths, odd and even numbers, repeating patterns, and symmetry in shapes.",
   resourceLabel:"YouTube: Final Review: Fractions, Odd/Even, Patterns and Symmetry", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Fractions%2C%20Odd/Even%2C%20Patterns%20and%20Symmetry%20grade%202%20educational",
   quiz:[
     {q:"If a whole is split into 8 equal parts, each part is called ___.", options:["One whole","One eighth","One half","One third"], answer:1},
     {q:"Which of these numbers is odd?", options:["8","4","6","9"], answer:3},
     {q:"In the pattern circle, square, circle, square, ___, what comes next?", options:["Star","Triangle","Circle","Square"], answer:2},
     {q:"A shape has symmetry if it can be folded so that ___.", options:["Both halves are different sizes","Both halves match exactly","One half disappears","It cannot be folded at all"], answer:1},
     {q:"Splitting a whole into more equal parts makes each part ___.", options:["Disappear","Bigger","Smaller","Stay the same size"], answer:2}
   ],
   worksheet:[
     {prompt:"If a whole is split into 3 equal parts, what is each part called?", answers:["one third","a third"]},
     {prompt:"Is the number 8 odd or even?", answers:["even"]},
     {prompt:"What do we call the line where a symmetrical shape can be folded so both halves match?", answers:["a line of symmetry","line of symmetry"]}
   ]},
  {subject:"Science", title:"Final Review: Magnets, Water Cycle, Rocks/Soil and Healthy Eating", summary:"Students review recent Science topics: magnets, the water cycle, rocks and soil, and healthy eating and food groups.",
   resourceLabel:"YouTube: Final Review: Magnets, Water Cycle, Rocks/Soil and Healthy Eating", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Magnets%2C%20Water%20Cycle%2C%20Rocks/Soil%20and%20Healthy%20Eating%20grade%202%20educational",
   quiz:[
     {q:"Which of these materials would a magnet most likely attract?", options:["A paper towel","A wooden block","A plastic cup","An iron nail"], answer:3},
     {q:"What do we call rain or snow falling from clouds to the ground?", options:["Precipitation","Condensation","Evaporation","Freezing"], answer:0},
     {q:"What is soil made up of?", options:["Tiny broken bits of rock mixed with decayed plants and animals","Only water","Only metal","Only glass"], answer:0},
     {q:"Why is it important to eat a balance of different food groups?", options:["It has no effect on health","It only matters for adults","It makes food taste worse","It helps the body grow strong and stay healthy"], answer:3},
     {q:"What happens when two magnets with opposite poles are brought close together?", options:["They melt","They disappear","They always push apart","They attract and pull together"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the force a magnet uses to attract or push away objects?", answers:["magnetism","magnetic force"]},
     {prompt:"What do we call water turning into vapour and rising into the air?", answers:["evaporation"]},
     {prompt:"What is soil made up of?", answers:["broken rock and decayed plants","tiny broken bits of rock and decayed matter"]}
   ]},
  {subject:"SocialStudies", title:"Final Review: Immigration, Personal Safety, Money and Landmarks", summary:"Students review recent Social Studies topics: immigration, personal safety, saving and spending money wisely, and Canadian landmarks.",
   resourceLabel:"YouTube: Final Review: Immigration, Personal Safety, Money and Landmarks", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Immigration%2C%20Personal%20Safety%2C%20Money%20and%20Landmarks%20grade%202%20educational",
   quiz:[
     {q:"What is immigration?", options:["When people travel on vacation","When people move from one country to live in another","When animals migrate with the seasons","When a family moves within the same city"], answer:1},
     {q:"Who could be a trusted adult a child talks to about feeling unsafe?", options:["Only another child","A stranger","A parent or teacher","No one at all"], answer:2},
     {q:"What does it mean to save money?", options:["Losing your money","Putting money aside instead of spending it right away","Spending all your money right away","Giving all your money away"], answer:1},
     {q:"In which city would you find the CN Tower?", options:["Toronto","Ottawa","Vancouver","Montreal"], answer:0},
     {q:"Why might a family choose to immigrate to Canada?", options:["Only for a short vacation","To find new opportunities, safety, or to be with family","To avoid all other countries","Canada has no reasons to immigrate to"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call it when people move from one country to live in another?", answers:["immigration"]},
     {prompt:"What should you do if a touch makes you feel unsafe or uncomfortable?", answers:["say no","tell a trusted adult"]},
     {prompt:"What do we call putting money aside instead of spending it right away?", answers:["saving"]}
   ]},
]},
{day:41, label:"Day 41 — Mon", subjects:[
  {subject:"Language", title:"Silent Letters: kn, wr, mb, gh", summary:"Students learn that some words contain silent letters, letters that are written but not pronounced, such as the k in knee, the w in write, the b in comb, and the gh in night.",
   resourceLabel:"YouTube: Silent Letters: kn, wr, mb, gh", resourceUrl:"https://www.youtube.com/results?search_query=Silent%20Letters%3A%20kn%2C%20wr%2C%20mb%2C%20gh%20grade%202%20educational",
   quiz:[
     {q:"Which letter is silent in the word knee?", options:["K","N","E","All letters are pronounced"], answer:0},
     {q:"Which letter is silent in the word write?", options:["I","W","R","T"], answer:1},
     {q:"Which letter is silent in the word comb?", options:["O","M","C","B"], answer:3},
     {q:"In the word night, which two letters together are silent?", options:["IG","NI","HT","GH"], answer:3},
     {q:"A silent letter is a letter that is ___.", options:["Written but not pronounced","Always capitalized","Never written","Always pronounced loudly"], answer:0}
   ],
   worksheet:[
     {prompt:"What letter is silent at the beginning of the word knee?", answers:["k"]},
     {prompt:"What letter is silent at the beginning of the word write?", answers:["w"]},
     {prompt:"Name one word with a silent letter, like comb or night.", answers:["comb","night","knee","write"]}
   ]},
  {subject:"Math", title:"Numbers to 1000: Counting and Comparing", summary:"Students count, read, and compare numbers up to 1000, using place value to understand hundreds, tens, and ones.",
   resourceLabel:"YouTube: Numbers to 1000: Counting and Comparing", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%20to%201000%3A%20Counting%20and%20Comparing%20grade%202%20educational",
   quiz:[
     {q:"What number comes right after 499?", options:["501","500","450","499"], answer:1},
     {q:"Which number is greater, 620 or 602?", options:["They are equal","620","602","Cannot tell"], answer:1},
     {q:"How many hundreds are in the number 700?", options:["17","70","7","700"], answer:2},
     {q:"Which of these numbers is between 400 and 500?", options:["501","399","600","450"], answer:3},
     {q:"In the number 384, what digit is in the hundreds place?", options:["0","3","8","4"], answer:1}
   ],
   worksheet:[
     {prompt:"What number comes right after 499?", answers:["500","five hundred"]},
     {prompt:"Which is greater, 350 or 305?", answers:["350"]},
     {prompt:"How many hundreds are in the number 400?", answers:["4","four"]}
   ]},
  {subject:"Science", title:"Life Cycle of a Plant: Seed to Flower", summary:"Students learn the life cycle of a plant, from a seed that sprouts into a seedling, grows into a mature plant, and produces flowers that make new seeds.",
   resourceLabel:"YouTube: Life Cycle of a Plant: Seed to Flower", resourceUrl:"https://www.youtube.com/results?search_query=Life%20Cycle%20of%20a%20Plant%3A%20Seed%20to%20Flower%20grade%202%20educational",
   quiz:[
     {q:"What is the very first stage of a plant life cycle?", options:["A flower","A root","A seed","A leaf"], answer:2},
     {q:"What do we call a young plant that has just sprouted from a seed?", options:["A sapling","A seedling","A bud","A stem"], answer:1},
     {q:"What does a mature plant produce that can grow into a new plant?", options:["Seeds","Water","Soil","Rocks"], answer:0},
     {q:"Put these stages in order.", options:["Seed, seedling, mature plant, flower","Flower, seed, seedling, mature plant","Seedling, flower, seed, mature plant","Mature plant, flower, seed, seedling"], answer:0},
     {q:"A plant life cycle describes how a plant ___.", options:["Grows and changes from a seed to a new seed-producing plant","Turns into an animal","Never changes at all","Only lives for one day"], answer:0}
   ],
   worksheet:[
     {prompt:"What is the very first stage in a plant life cycle?", answers:["a seed","seed"]},
     {prompt:"What do we call a young plant that has just sprouted?", answers:["a seedling","seedling"]},
     {prompt:"What does a flower produce that can grow into a new plant?", answers:["seeds","new seeds"]}
   ]},
  {subject:"SocialStudies", title:"Explorers and Early Settlers in Canada", summary:"Students learn about explorers and early settlers who traveled to Canada long ago, discovering the land, meeting Indigenous peoples, and building the first small communities.",
   resourceLabel:"YouTube: Explorers and Early Settlers in Canada", resourceUrl:"https://www.youtube.com/results?search_query=Explorers%20and%20Early%20Settlers%20in%20Canada%20grade%202%20educational",
   quiz:[
     {q:"What do we call a person who travels to discover new lands?", options:["An explorer","A farmer","A tourist","A mayor"], answer:0},
     {q:"What do we call people who build the first communities in a new place?", options:["Settlers","Mayors","Tourists","Astronauts"], answer:0},
     {q:"When explorers arrived in Canada long ago, who was already living on the land?", options:["No one at all","Indigenous peoples","Only animals","Only settlers from Europe"], answer:1},
     {q:"Why did early explorers travel to new lands like Canada?", options:["To discover new places and resources","To avoid meeting new people","To build only underground homes","To stay home instead"], answer:0},
     {q:"Early settlers often built their first communities near ___.", options:["The top of tall mountains only","Rivers and lakes for water and travel","Places with no resources","The middle of the desert"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call a person who travels to discover new lands?", answers:["an explorer","explorer"]},
     {prompt:"What do we call the first people to build a community in a new place?", answers:["settlers","early settlers"]},
     {prompt:"Did explorers meet Indigenous peoples already living on the land?", answers:["yes"]}
   ]},
]},
{day:42, label:"Day 42 — Tue", subjects:[
  {subject:"Language", title:"Homophones: Words That Sound the Same", summary:"Students learn that homophones are words that sound the same but have different spellings and meanings, such as to, too, and two, or their and there.",
   resourceLabel:"YouTube: Homophones: Words That Sound the Same", resourceUrl:"https://www.youtube.com/results?search_query=Homophones%3A%20Words%20That%20Sound%20the%20Same%20grade%202%20educational",
   quiz:[
     {q:"What do we call words that sound the same but have different spellings and meanings?", options:["Homophones","Antonyms","Compound words","Synonyms"], answer:0},
     {q:"Which word means also or as well?", options:["Too","Ten","Two","To"], answer:0},
     {q:"Which word means the number 2?", options:["Too","Twelve","Two","To"], answer:2},
     {q:"Which word means toward or in the direction of?", options:["Ten","Two","Too","To"], answer:3},
     {q:"Their and there are examples of ___.", options:["Prefixes","Homophones","Contractions","Compound words"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one homophone pair, like to and too.", answers:["to and too","their and there","two and to"]},
     {prompt:"Which word means the number after one, to, too, or two?", answers:["two"]},
     {prompt:"Which word means also, to, too, or two?", answers:["too"]}
   ]},
  {subject:"Math", title:"Fact Families: Addition and Subtraction", summary:"Students learn that a fact family is a group of related addition and subtraction facts made from the same three numbers, such as 4 + 5 = 9, 5 + 4 = 9, 9 - 4 = 5, and 9 - 5 = 4.",
   resourceLabel:"YouTube: Fact Families: Addition and Subtraction", resourceUrl:"https://www.youtube.com/results?search_query=Fact%20Families%3A%20Addition%20and%20Subtraction%20grade%202%20educational",
   quiz:[
     {q:"What do we call a group of related addition and subtraction facts made from the same three numbers?", options:["A fact family","A number line","A pattern","A fraction"], answer:0},
     {q:"If 4 + 5 = 9, which of these also belongs in the same fact family?", options:["5 - 9 = 4","9 - 5 = 4","4 - 5 = 9","9 + 5 = 14"], answer:1},
     {q:"Which three numbers make up the fact family that includes 3 + 6 = 9?", options:["3, 6, and 9","3, 9, and 12","6, 9, and 15","3, 6, and 18"], answer:0},
     {q:"If 8 + 2 = 10, what is 10 - 8?", options:["2","10","8","18"], answer:0},
     {q:"Knowing a fact family helps you ___.", options:["Multiply numbers","Only solve addition problems","Forget subtraction","Solve both addition and subtraction problems more quickly"], answer:3}
   ],
   worksheet:[
     {prompt:"If 4 + 5 = 9, what subtraction fact also belongs in this fact family?", answers:["9 - 5 = 4","9 - 4 = 5"]},
     {prompt:"Name the three numbers in the fact family for 3 + 6 = 9.", answers:["3, 6, and 9","3 6 9"]},
     {prompt:"If 7 + 2 = 9, what is 9 - 2?", answers:["7"]}
   ]},
  {subject:"Science", title:"Floating and Sinking", summary:"Students explore why some objects float on water while others sink, learning that this depends on an objects weight, shape, and the material it is made of.",
   resourceLabel:"YouTube: Floating and Sinking", resourceUrl:"https://www.youtube.com/results?search_query=Floating%20and%20Sinking%20grade%202%20educational",
   quiz:[
     {q:"What do we call it when an object stays on top of the water?", options:["Sinking","Melting","Floating","Freezing"], answer:2},
     {q:"What do we call it when an object goes down under the water?", options:["Sinking","Floating","Boiling","Evaporating"], answer:0},
     {q:"Which of these objects would most likely float in water?", options:["A large rock","A brick","A metal spoon","A wooden block"], answer:3},
     {q:"Which of these objects would most likely sink in water?", options:["A heavy rock","A leaf","A rubber duck","An empty plastic bottle"], answer:0},
     {q:"Whether an object floats or sinks depends on its ___.", options:["Name only","Colour only","Smell only","Weight, shape, and material"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call it when an object stays on top of the water?", answers:["floating","float"]},
     {prompt:"What do we call it when an object goes down under the water?", answers:["sinking","sink"]},
     {prompt:"Name one object that usually floats in water, like a leaf or a piece of wood.", answers:["a leaf","leaf","a piece of wood","wood"]}
   ]},
  {subject:"SocialStudies", title:"Volunteering: Helping Our Community", summary:"Students learn that volunteering means giving time and effort to help others without expecting payment, such as helping clean a park or collecting food for those in need.",
   resourceLabel:"YouTube: Volunteering: Helping Our Community", resourceUrl:"https://www.youtube.com/results?search_query=Volunteering%3A%20Helping%20Our%20Community%20grade%202%20educational",
   quiz:[
     {q:"What do we call giving your time to help others without being paid?", options:["Shopping","Voting","Working for money","Volunteering"], answer:3},
     {q:"Which of these is an example of volunteering?", options:["Buying a new toy","Sleeping in late","Watching television","Helping clean up a local park"], answer:3},
     {q:"Why might someone choose to volunteer in their community?", options:["To stay away from other people","To avoid helping anyone","To help others and make the community better","To earn a large paycheck"], answer:2},
     {q:"Which of these groups might collect food to help families in need?", options:["A food bank","A car dealership","A toy store","A movie theatre"], answer:0},
     {q:"Volunteering can help a community by ___.", options:["Taking resources away from people","Having no effect at all","Bringing people together to solve problems and help others","Making the community worse"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call giving your time to help others without expecting payment?", answers:["volunteering"]},
     {prompt:"Name one way someone could volunteer, like cleaning a park.", answers:["cleaning a park","collecting food","helping others"]},
     {prompt:"Does volunteering help make a community better?", answers:["yes"]}
   ]},
]},
{day:43, label:"Day 43 — Wed", subjects:[
  {subject:"Language", title:"Adverbs: How, When, and Where", summary:"Students learn that an adverb is a word that describes a verb, telling how, when, or where an action happens, such as quickly, today, or outside.",
   resourceLabel:"YouTube: Adverbs: How, When, and Where", resourceUrl:"https://www.youtube.com/results?search_query=Adverbs%3A%20How%2C%20When%2C%20and%20Where%20grade%202%20educational",
   quiz:[
     {q:"An adverb is a word that describes a ___.", options:["Article","Noun","Verb","Pronoun"], answer:2},
     {q:"Which word tells how someone runs in the sentence, She runs quickly?", options:["Runs","She","Quickly","The"], answer:2},
     {q:"Which word is an adverb that tells when, as in We will go today?", options:["We","Today","Will","Go"], answer:1},
     {q:"Which word is an adverb that tells where, as in The cat sat outside?", options:["The","Outside","Cat","Sat"], answer:1},
     {q:"Which of these words is an adverb?", options:["Happy","Dog","Carefully","Jump"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one adverb that tells how something happens, like quickly or slowly.", answers:["quickly","slowly","carefully"]},
     {prompt:"Name one adverb that tells when something happens, like today or soon.", answers:["today","soon","yesterday"]},
     {prompt:"Name one adverb that tells where something happens, like outside or here.", answers:["outside","here","there"]}
   ]},
  {subject:"Math", title:"Telling Time: Elapsed Time and the Calendar", summary:"Students learn to figure out how much time has passed between two events, called elapsed time, and to read a calendar to find days, weeks, and months.",
   resourceLabel:"YouTube: Telling Time: Elapsed Time and the Calendar", resourceUrl:"https://www.youtube.com/results?search_query=Telling%20Time%3A%20Elapsed%20Time%20and%20the%20Calendar%20grade%202%20educational",
   quiz:[
     {q:"How many days are in one week?", options:["10","5","30","7"], answer:3},
     {q:"If a game starts at 2:00 and ends at 3:00, how much time has passed?", options:["30 minutes","15 minutes","1 hour","2 hours"], answer:2},
     {q:"How many months are in one year?", options:["12","10","365","52"], answer:0},
     {q:"What tool would you use to find out what day of the week a date falls on?", options:["A calendar","A thermometer","A scale","A ruler"], answer:0},
     {q:"Elapsed time tells us ___.", options:["The temperature outside","The day of the week only","How much time has passed between two events","The weight of an object"], answer:2}
   ],
   worksheet:[
     {prompt:"How many days are in one week?", answers:["7","seven"]},
     {prompt:"If a movie starts at 3:00 and ends at 4:00, how much time has passed?", answers:["1 hour","one hour"]},
     {prompt:"How many months are in one year?", answers:["12","twelve"]}
   ]},
  {subject:"Science", title:"Forces: Gravity Pulls Things Down", summary:"Students learn that gravity is a force that pulls objects toward the earth, which is why things fall down instead of floating away when dropped.",
   resourceLabel:"YouTube: Forces: Gravity Pulls Things Down", resourceUrl:"https://www.youtube.com/results?search_query=Forces%3A%20Gravity%20Pulls%20Things%20Down%20grade%202%20educational",
   quiz:[
     {q:"What do we call the force that pulls objects toward the earth?", options:["Gravity","Wind","Friction","Magnetism"], answer:0},
     {q:"If you drop a ball, which way does gravity pull it?", options:["Sideways only","Down toward the ground","Nowhere at all","Up into the sky"], answer:1},
     {q:"Why does a dropped pencil fall to the floor instead of floating in the air?", options:["Gravity pulls it toward the earth","Magnetism pulls it down","Wind pushes it down","It has no weight"], answer:0},
     {q:"Which of these is an example of gravity at work?", options:["Water evaporating","An apple falling from a tree","Wind blowing leaves","A magnet pulling a paperclip"], answer:1},
     {q:"Without gravity, objects on earth would ___.", options:["Float away instead of staying on the ground","Melt instantly","Become heavier","Turn into gas"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the force that pulls objects toward the earth?", answers:["gravity"]},
     {prompt:"If you drop a ball, which direction does gravity pull it?", answers:["down","downward"]},
     {prompt:"Does gravity pull objects toward the earth or away from it?", answers:["toward the earth","toward"]}
   ]},
  {subject:"SocialStudies", title:"Weather and Climate Across Canada", summary:"Students learn that weather and climate can be very different across Canada, with some regions having cold snowy winters, others having milder weather, and coastlines with rain.",
   resourceLabel:"YouTube: Weather and Climate Across Canada", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20and%20Climate%20Across%20Canada%20grade%202%20educational",
   quiz:[
     {q:"What do we call the usual weather pattern of a region over a long time?", options:["A map","A season","A landmark","Climate"], answer:3},
     {q:"Which season in many parts of Canada is known for cold temperatures and snow?", options:["Only autumn","Winter","Only spring","Summer"], answer:1},
     {q:"Why might the climate be different in different parts of Canada?", options:["Climate never changes anywhere","Only cities have climate","All of Canada always has the exact same weather","Location, such as being near mountains, coasts, or the north, affects climate"], answer:3},
     {q:"Which part of Canada might experience a lot of rain because it is near the ocean?", options:["A coastal region","The top of a dry plain","The middle of a desert","An underground cave"], answer:0},
     {q:"Understanding climate helps people ___.", options:["Change the seasons","Ignore the weather completely","Stop the weather from happening","Prepare for the kind of weather common in their region"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one type of weather common in many parts of Canada during winter.", answers:["snow","cold weather","snowy weather"]},
     {prompt:"Do different regions of Canada have different climates?", answers:["yes"]},
     {prompt:"Name one part of Canada known for rainy weather, like the coast.", answers:["the coast","coast","coastal areas"]}
   ]},
]},
{day:44, label:"Day 44 — Thu", subjects:[
  {subject:"Language", title:"Cause and Effect in Stories", summary:"Students learn to identify cause and effect in stories, understanding that a cause is why something happens and an effect is what happens as a result.",
   resourceLabel:"YouTube: Cause and Effect in Stories", resourceUrl:"https://www.youtube.com/results?search_query=Cause%20and%20Effect%20in%20Stories%20grade%202%20educational",
   quiz:[
     {q:"What do we call the reason something happens in a story?", options:["An effect","A character","A setting","A cause"], answer:3},
     {q:"What do we call the result of an event in a story?", options:["A title","A cause","A rhyme","An effect"], answer:3},
     {q:"If a boy forgot his umbrella and got wet in the rain, what is the cause?", options:["He stayed dry","It stopped raining","He got wet","He forgot his umbrella"], answer:3},
     {q:"If a boy forgot his umbrella and got wet in the rain, what is the effect?", options:["He forgot his umbrella","He owns an umbrella","It was sunny","He got wet"], answer:3},
     {q:"Understanding cause and effect helps readers ___.", options:["Ignore the story completely","Skip the ending","Change the characters names","Understand why events happen in a story"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the reason something happens in a story?", answers:["a cause","cause"]},
     {prompt:"What do we call the result of what happens in a story?", answers:["an effect","effect"]},
     {prompt:"If it rained and the ground got wet, name the effect.", answers:["the ground got wet","ground got wet"]}
   ]},
  {subject:"Math", title:"Tally Charts and Simple Data Collection", summary:"Students learn to collect data by counting and recording it using tally marks, then use a tally chart to see totals for each category.",
   resourceLabel:"YouTube: Tally Charts and Simple Data Collection", resourceUrl:"https://www.youtube.com/results?search_query=Tally%20Charts%20and%20Simple%20Data%20Collection%20grade%202%20educational",
   quiz:[
     {q:"What do we call marks used to keep count while collecting data?", options:["Tally marks","Number lines","Fractions","Graphs"], answer:0},
     {q:"How many tally marks are grouped together before starting a new group?", options:["4","10","5","3"], answer:2},
     {q:"If a tally chart shows one full group of five plus three more marks, what is the total?", options:["5","8","10","3"], answer:1},
     {q:"Why do we collect data using a tally chart?", options:["To draw pictures only","To tell time","To measure length","To count and organize information clearly"], answer:3},
     {q:"After collecting data in a tally chart, the totals can be shown in a ___.", options:["Clock","Bar graph or pictograph","Calendar","Thermometer"], answer:1}
   ],
   worksheet:[
     {prompt:"How many tally marks make up one group in a tally chart?", answers:["5","five"]},
     {prompt:"What do we call marks used to keep count while collecting data?", answers:["tally marks"]},
     {prompt:"If a tally chart shows one full group of 5 plus 2 more marks, how many is that in total?", answers:["7","seven"]}
   ]},
  {subject:"Science", title:"Food Chains: Who Eats What", summary:"Students learn that a food chain shows how energy passes from one living thing to another, starting with a plant, moving to an animal that eats the plant, and then to an animal that eats that animal.",
   resourceLabel:"YouTube: Food Chains: Who Eats What", resourceUrl:"https://www.youtube.com/results?search_query=Food%20Chains%3A%20Who%20Eats%20What%20grade%202%20educational",
   quiz:[
     {q:"What do we call a chain that shows how energy passes from one living thing to another through eating?", options:["A food chain","A habitat","A water cycle","A life cycle"], answer:0},
     {q:"What is usually the first link in a food chain?", options:["A fish","A lion","A bird","A plant"], answer:3},
     {q:"In a food chain with grass, a rabbit, and a fox, what does the rabbit eat?", options:["Grass","Rocks","The fox","Water"], answer:0},
     {q:"In a food chain with grass, a rabbit, and a fox, what eats the rabbit?", options:["Nothing eats the rabbit","The sun","The fox","The grass"], answer:2},
     {q:"Food chains show how ___.", options:["Water evaporates into the air","Energy moves from plants to animals that eat them","Seasons change throughout the year","Rocks turn into soil"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call a chain that shows who eats what in nature?", answers:["a food chain","food chain"]},
     {prompt:"What is usually the first link in a food chain, like a plant?", answers:["a plant","plant"]},
     {prompt:"Name an animal that eats plants, like a rabbit or a deer.", answers:["a rabbit","rabbit","a deer","deer"]}
   ]},
  {subject:"SocialStudies", title:"Public Safety Services: Police, Fire, and Ambulance", summary:"Students learn about public safety services in a community, such as police officers who keep people safe, firefighters who put out fires, and paramedics who help people who are hurt or sick.",
   resourceLabel:"YouTube: Public Safety Services: Police, Fire, and Ambulance", resourceUrl:"https://www.youtube.com/results?search_query=Public%20Safety%20Services%3A%20Police%2C%20Fire%2C%20and%20Ambulance%20grade%202%20educational",
   quiz:[
     {q:"Which public safety service is trained to put out fires?", options:["Farmers","Mail carriers","Firefighters","Teachers"], answer:2},
     {q:"Which public safety service helps keep a community safe from crime?", options:["Police officers","Bakers","Artists","Librarians"], answer:0},
     {q:"Which public safety service helps people who are hurt or sick get to a hospital quickly?", options:["A librarian","Paramedics in an ambulance","A shopkeeper","A mail carrier"], answer:1},
     {q:"What number do many communities use to call for help in an emergency?", options:["911","411","511","111"], answer:0},
     {q:"Public safety services are important because they ___.", options:["Are never needed","Help keep people in a community safe and healthy","Have no purpose in a community","Only help during holidays"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one public safety service that helps put out fires.", answers:["firefighters","fire department"]},
     {prompt:"Name one public safety service that helps keep people safe from crime.", answers:["police","police officers"]},
     {prompt:"Name one public safety service that helps people who are hurt or sick.", answers:["ambulance","paramedics"]}
   ]},
]},
{day:45, label:"Day 45 — Fri", subjects:[
  {subject:"Language", title:"Review: Silent Letters, Homophones, Adverbs and Cause and Effect", summary:"Students review recent Language skills: silent letters, homophones, adverbs, and cause and effect in stories.",
   resourceLabel:"YouTube: Review: Silent Letters, Homophones, Adverbs and Cause and Effect", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Silent%20Letters%2C%20Homophones%2C%20Adverbs%20and%20Cause%20and%20Effect%20grade%202%20educational",
   quiz:[
     {q:"Which letter is silent in the word write?", options:["T","I","W","R"], answer:2},
     {q:"Which word means also or as well?", options:["Two","Too","Ten","To"], answer:1},
     {q:"Which word is an adverb that tells where, as in The cat sat outside?", options:["Outside","Cat","The","Sat"], answer:0},
     {q:"What do we call the result of an event in a story?", options:["A cause","A title","An effect","A rhyme"], answer:2},
     {q:"Their and there are examples of ___.", options:["Compound words","Homophones","Prefixes","Contractions"], answer:1}
   ],
   worksheet:[
     {prompt:"What letter is silent at the beginning of the word knee?", answers:["k"]},
     {prompt:"Name one homophone pair, like to and too.", answers:["to and too","their and there","two and to"]},
     {prompt:"Name one adverb that tells how something happens, like quickly or slowly.", answers:["quickly","slowly","carefully"]}
   ]},
  {subject:"Math", title:"Review: Numbers to 1000, Fact Families, Elapsed Time and Data", summary:"Students review recent Math skills: numbers to 1000, fact families, elapsed time and the calendar, and tally charts.",
   resourceLabel:"YouTube: Review: Numbers to 1000, Fact Families, Elapsed Time and Data", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Numbers%20to%201000%2C%20Fact%20Families%2C%20Elapsed%20Time%20and%20Data%20grade%202%20educational",
   quiz:[
     {q:"Which number is greater, 620 or 602?", options:["620","602","They are equal","Cannot tell"], answer:0},
     {q:"If 8 + 2 = 10, what is 10 - 8?", options:["18","8","10","2"], answer:3},
     {q:"How many months are in one year?", options:["10","12","52","365"], answer:1},
     {q:"Why do we collect data using a tally chart?", options:["To tell time","To draw pictures only","To count and organize information clearly","To measure length"], answer:2},
     {q:"In the number 384, what digit is in the hundreds place?", options:["8","3","0","4"], answer:1}
   ],
   worksheet:[
     {prompt:"What number comes right after 499?", answers:["500","five hundred"]},
     {prompt:"If 4 + 5 = 9, what subtraction fact also belongs in this fact family?", answers:["9 - 5 = 4","9 - 4 = 5"]},
     {prompt:"How many days are in one week?", answers:["7","seven"]}
   ]},
  {subject:"Science", title:"Review: Plant Life Cycle, Floating and Sinking, Gravity and Food Chains", summary:"Students review recent Science topics: the life cycle of a plant, floating and sinking, gravity, and food chains.",
   resourceLabel:"YouTube: Review: Plant Life Cycle, Floating and Sinking, Gravity and Food Chains", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Plant%20Life%20Cycle%2C%20Floating%20and%20Sinking%2C%20Gravity%20and%20Food%20Chains%20grade%202%20educational",
   quiz:[
     {q:"What does a mature plant produce that can grow into a new plant?", options:["Water","Rocks","Seeds","Soil"], answer:2},
     {q:"Which of these objects would most likely sink in water?", options:["A leaf","A rubber duck","An empty plastic bottle","A heavy rock"], answer:3},
     {q:"Why does a dropped pencil fall to the floor instead of floating in the air?", options:["It has no weight","Gravity pulls it toward the earth","Wind pushes it down","Magnetism pulls it down"], answer:1},
     {q:"In a food chain with grass, a rabbit, and a fox, what eats the rabbit?", options:["The sun","The fox","Nothing eats the rabbit","The grass"], answer:1},
     {q:"What do we call a chain that shows how energy passes from one living thing to another through eating?", options:["A life cycle","A water cycle","A habitat","A food chain"], answer:3}
   ],
   worksheet:[
     {prompt:"What is the very first stage in a plant life cycle?", answers:["a seed","seed"]},
     {prompt:"What do we call it when an object stays on top of the water?", answers:["floating","float"]},
     {prompt:"What do we call the force that pulls objects toward the earth?", answers:["gravity"]}
   ]},
  {subject:"SocialStudies", title:"Review: Explorers, Volunteering, Weather and Public Safety", summary:"Students review recent Social Studies topics: explorers and early settlers, volunteering, weather and climate across Canada, and public safety services.",
   resourceLabel:"YouTube: Review: Explorers, Volunteering, Weather and Public Safety", resourceUrl:"https://www.youtube.com/results?search_query=Review%3A%20Explorers%2C%20Volunteering%2C%20Weather%20and%20Public%20Safety%20grade%202%20educational",
   quiz:[
     {q:"Why did early explorers travel to new lands like Canada?", options:["To build only underground homes","To discover new places and resources","To avoid meeting new people","To stay home instead"], answer:1},
     {q:"Which of these is an example of volunteering?", options:["Buying a new toy","Sleeping in late","Helping clean up a local park","Watching television"], answer:2},
     {q:"Which season in many parts of Canada is known for cold temperatures and snow?", options:["Only spring","Summer","Winter","Only autumn"], answer:2},
     {q:"What number do many communities use to call for help in an emergency?", options:["511","411","111","911"], answer:3},
     {q:"Why might the climate be different in different parts of Canada?", options:["Climate never changes anywhere","Only cities have climate","Location, such as being near mountains, coasts, or the north, affects climate","All of Canada always has the exact same weather"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a person who travels to discover new lands?", answers:["an explorer","explorer"]},
     {prompt:"What do we call giving your time to help others without expecting payment?", answers:["volunteering"]},
     {prompt:"Name one public safety service that helps put out fires.", answers:["firefighters","fire department"]}
   ]},
]},
{day:46, label:"Day 46 — Mon", subjects:[
  {subject:"Language", title:"Combining Sentences with And, But, and Because", summary:"Students learn to combine two short sentences into one longer sentence using the joining words and, but, and because.",
   resourceLabel:"YouTube: Combining Sentences with And, But, and Because", resourceUrl:"https://www.youtube.com/results?search_query=Combining%20Sentences%20with%20And%2C%20But%2C%20and%20Because%20grade%202%20educational",
   quiz:[
     {q:"Which joining word combines two similar ideas?", options:["Because","Or","And","But"], answer:2},
     {q:"Which joining word shows a contrast or difference between two ideas?", options:["Because","And","So","But"], answer:3},
     {q:"Which joining word gives a reason for something?", options:["Or","But","Because","And"], answer:2},
     {q:"Which sentence correctly combines two ideas with and?", options:["I like dogs but I like cats.","I like dogs, cats.","I like dogs and I like cats.","I like dogs because cats."], answer:2},
     {q:"Combining short sentences into one longer sentence can make writing ___.", options:["Shorter than one word","Impossible to read","Smoother and more interesting","Always incorrect"], answer:2}
   ],
   worksheet:[
     {prompt:"Which joining word would you use to combine two similar ideas, like I like apples and I like pears?", answers:["and"]},
     {prompt:"Which joining word shows a difference between two ideas, like It was cold but I was warm?", answers:["but"]},
     {prompt:"Which joining word explains a reason, like I wore a coat because it was cold?", answers:["because"]}
   ]},
  {subject:"Math", title:"Rounding to the Nearest Ten", summary:"Students learn to round two-digit numbers to the nearest ten, checking the ones digit to decide whether to round up or down.",
   resourceLabel:"YouTube: Rounding to the Nearest Ten", resourceUrl:"https://www.youtube.com/results?search_query=Rounding%20to%20the%20Nearest%20Ten%20grade%202%20educational",
   quiz:[
     {q:"What is 23 rounded to the nearest ten?", options:["10","23","20","30"], answer:2},
     {q:"What is 47 rounded to the nearest ten?", options:["40","45","50","47"], answer:2},
     {q:"When rounding, if the ones digit is 5 or more, we round ___.", options:["Nowhere","Up to the next ten","Down to the previous ten","To zero"], answer:1},
     {q:"What is 62 rounded to the nearest ten?", options:["62","50","60","70"], answer:2},
     {q:"Rounding numbers helps us ___.", options:["Avoid using numbers","Get the exact answer every time","Make numbers bigger only","Estimate quickly using simpler numbers"], answer:3}
   ],
   worksheet:[
     {prompt:"What is 23 rounded to the nearest ten?", answers:["20","twenty"]},
     {prompt:"What is 47 rounded to the nearest ten?", answers:["50","fifty"]},
     {prompt:"If the ones digit is 5 or more, do we round up?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Animal Migration and Hibernation", summary:"Students learn that some animals migrate, traveling long distances to find food or warmer weather, while other animals hibernate, going into a deep sleep through the cold winter months.",
   resourceLabel:"YouTube: Animal Migration and Hibernation", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Migration%20and%20Hibernation%20grade%202%20educational",
   quiz:[
     {q:"What do we call it when animals travel long distances to find food or warmer weather?", options:["Pollination","Migration","Hibernation","Evaporation"], answer:1},
     {q:"What do we call it when an animal goes into a deep sleep through the cold winter months?", options:["Metamorphosis","Camouflage","Migration","Hibernation"], answer:3},
     {q:"Which of these animals is known for migrating long distances?", options:["A snail","A goose","A worm","A rock"], answer:1},
     {q:"Which of these animals is known for hibernating in winter?", options:["A fish","A butterfly","A bear","A goose"], answer:2},
     {q:"Why might an animal migrate to a warmer place?", options:["To change colour","To find food and better living conditions","To avoid all other animals","To grow new feathers only"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call it when animals travel long distances to find food or warmer weather?", answers:["migration","migrate"]},
     {prompt:"What do we call it when an animal goes into a deep sleep through winter?", answers:["hibernation","hibernate"]},
     {prompt:"Name one animal that hibernates, like a bear.", answers:["a bear","bear"]}
   ]},
  {subject:"SocialStudies", title:"Cultural Diversity: Celebrating Our Differences", summary:"Students learn that communities in Canada are made up of people from many different cultures and backgrounds, and that learning about different traditions, languages, and foods helps everyone understand and respect each other.",
   resourceLabel:"YouTube: Cultural Diversity: Celebrating Our Differences", resourceUrl:"https://www.youtube.com/results?search_query=Cultural%20Diversity%3A%20Celebrating%20Our%20Differences%20grade%202%20educational",
   quiz:[
     {q:"What word describes a community made up of people from many different cultures and backgrounds?", options:["Empty","Diverse","Identical","Silent"], answer:1},
     {q:"Which of these might be different between two cultures?", options:["Food, language, and traditions","The number of days in a week","Gravity","The colour of the sky"], answer:0},
     {q:"Why is it helpful to learn about different cultures in your community?", options:["It helps people understand and respect each other","It has no benefit at all","It causes communities to fall apart","It makes people forget their own culture"], answer:0},
     {q:"Which of these is a respectful way to learn about a friends culture?", options:["Refusing to learn anything new","Asking questions and listening with respect","Making fun of their traditions","Ignoring them completely"], answer:1},
     {q:"Celebrating cultural diversity means ___.", options:["Valuing and respecting many different backgrounds and traditions","Ignoring all traditions","Only valuing one culture","Avoiding people who are different"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes a community made up of people from many different cultures?", answers:["diverse","diversity"]},
     {prompt:"Name one thing that can be different between cultures, like food or language.", answers:["food","language","traditions","clothing"]},
     {prompt:"Does learning about other cultures help people understand each other?", answers:["yes"]}
   ]},
]},
{day:47, label:"Day 47 — Tue", subjects:[
  {subject:"Language", title:"Reading Comprehension: Fact vs Opinion", summary:"Students learn the difference between a fact, a statement that can be proven true, and an opinion, a statement that shows what someone thinks or feels.",
   resourceLabel:"YouTube: Reading Comprehension: Fact vs Opinion", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20Comprehension%3A%20Fact%20vs%20Opinion%20grade%202%20educational",
   quiz:[
     {q:"What do we call a statement that can be proven true?", options:["An opinion","A question","A rhyme","A fact"], answer:3},
     {q:"What do we call a statement that shows what someone thinks or feels?", options:["An opinion","A setting","A title","A fact"], answer:0},
     {q:"Which of these sentences is a fact?", options:["Cats are better than dogs.","Summer is the best season.","A week has seven days.","Pizza is the tastiest food."], answer:2},
     {q:"Which of these sentences is an opinion?", options:["There are twelve months in a year.","Fish live in water.","Chocolate ice cream tastes the best.","A triangle has three sides."], answer:2},
     {q:"Facts can be checked and proven, while opinions ___.", options:["Are always false","Show what a person thinks or feels","Can never be spoken aloud","Are always the same as facts"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call a statement that can be proven true?", answers:["a fact","fact"]},
     {prompt:"What do we call a statement that shows what someone thinks or feels?", answers:["an opinion","opinion"]},
     {prompt:"Is the statement dogs are the best pets a fact or an opinion?", answers:["an opinion","opinion"]}
   ]},
  {subject:"Math", title:"Area: Covering a Shape with Squares", summary:"Students learn that area is the amount of space a flat shape covers, measured by counting how many equal squares fit inside the shape.",
   resourceLabel:"YouTube: Area: Covering a Shape with Squares", resourceUrl:"https://www.youtube.com/results?search_query=Area%3A%20Covering%20a%20Shape%20with%20Squares%20grade%202%20educational",
   quiz:[
     {q:"What do we call the amount of space a flat shape covers?", options:["Weight","Perimeter","Length","Area"], answer:3},
     {q:"If a rectangle is covered exactly by 8 equal squares, what is its area?", options:["8 square units","4 square units","2 square units","8 metres"], answer:0},
     {q:"To measure area, we count how many equal ___ fit inside a shape.", options:["Squares","Circles","Dots","Lines"], answer:0},
     {q:"Which shape would likely have a larger area, one covered by 4 squares or one covered by 10 squares?", options:["The one covered by 10 squares","They are always equal","Cannot be measured","The one covered by 4 squares"], answer:0},
     {q:"Area is measured in units such as ___.", options:["Kilograms","Litres","Degrees","Square units"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the amount of space a flat shape covers?", answers:["area"]},
     {prompt:"If a rectangle is covered by 6 equal squares with no gaps, what is its area?", answers:["6 squares","6"]},
     {prompt:"Do all the squares used to measure area need to be the same size?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Pollination: How Bees Help Plants Grow", summary:"Students learn that pollination happens when bees and other insects carry pollen from one flower to another, helping plants make seeds and grow new plants.",
   resourceLabel:"YouTube: Pollination: How Bees Help Plants Grow", resourceUrl:"https://www.youtube.com/results?search_query=Pollination%3A%20How%20Bees%20Help%20Plants%20Grow%20grade%202%20educational",
   quiz:[
     {q:"What do we call it when insects carry pollen from one flower to another?", options:["Evaporation","Migration","Hibernation","Pollination"], answer:3},
     {q:"Which of these insects is well known for helping pollinate flowers?", options:["A worm","A bee","An ant","A spider"], answer:1},
     {q:"What is the powder inside a flower called that bees carry from flower to flower?", options:["Soil","Bark","Sap","Pollen"], answer:3},
     {q:"Why is pollination important for plants?", options:["It helps plants stay small forever","It stops plants from growing","It helps plants make seeds and grow new plants","It has no effect on plants"], answer:2},
     {q:"Bees are attracted to flowers partly because flowers provide ___.", options:["Rocks for the bees to eat","Nectar for the bees to collect","Nothing at all","Water for the bees to drink only"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one insect that helps pollinate flowers, like a bee or a butterfly.", answers:["a bee","bee","a butterfly","butterfly"]},
     {prompt:"What is the yellow powder inside a flower called that insects carry from flower to flower?", answers:["pollen"]},
     {prompt:"Does pollination help plants make seeds?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"The Role of Schools and Libraries in a Community", summary:"Students learn that schools help children learn and grow, while libraries offer books and resources for people of all ages to read, learn, and explore new ideas.",
   resourceLabel:"YouTube: The Role of Schools and Libraries in a Community", resourceUrl:"https://www.youtube.com/results?search_query=The%20Role%20of%20Schools%20and%20Libraries%20in%20a%20Community%20grade%202%20educational",
   quiz:[
     {q:"What is the main purpose of a school in a community?", options:["To fix cars","To grow crops","To help children learn and grow","To sell food"], answer:2},
     {q:"What can people typically borrow for free at a library?", options:["Cars","Houses","Food only","Books"], answer:3},
     {q:"Who can usually use the resources at a public library?", options:["Only children","Only teachers","People of all ages","Only adults"], answer:2},
     {q:"Which of these activities might happen at a school?", options:["Doctors performing surgery","Students learning to read and do math","Farmers growing crops","Firefighters putting out fires"], answer:1},
     {q:"Schools and libraries both help communities by ___.", options:["Building roads","Selling clothing","Supporting learning and sharing knowledge","Growing vegetables"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a place where children go to learn?", answers:["a school","school"]},
     {prompt:"What do we call a place where people can borrow books for free?", answers:["a library","library"]},
     {prompt:"Are libraries useful for people of all ages?", answers:["yes"]}
   ]},
]},
{day:48, label:"Day 48 — Wed", subjects:[
  {subject:"Language", title:"Using a Dictionary and Glossary", summary:"Students learn how to use a dictionary or glossary to find the meaning of a word, using guide words and alphabetical order to locate entries quickly.",
   resourceLabel:"YouTube: Using a Dictionary and Glossary", resourceUrl:"https://www.youtube.com/results?search_query=Using%20a%20Dictionary%20and%20Glossary%20grade%202%20educational",
   quiz:[
     {q:"What can you use to find the meaning of an unfamiliar word?", options:["A map","A recipe","A calendar","A dictionary"], answer:3},
     {q:"What do we call a list of important words and their meanings at the back of a book?", options:["A glossary","A table of contents","An index card","A title page"], answer:0},
     {q:"How are words usually organized in a dictionary?", options:["Randomly","In alphabetical order","By length","By colour"], answer:1},
     {q:"What are the two words at the top of a dictionary page called, showing the first and last entries?", options:["Title words","Cover words","Guide words","Page numbers"], answer:2},
     {q:"Using a dictionary helps readers ___.", options:["Solve math problems","Find the meaning and spelling of words","Draw pictures","Tell time"], answer:1}
   ],
   worksheet:[
     {prompt:"What book can you use to find the meaning of a word?", answers:["a dictionary","dictionary"]},
     {prompt:"What do we call a list of words and meanings found at the back of a book?", answers:["a glossary","glossary"]},
     {prompt:"Are the words in a dictionary listed in alphabetical order?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Perimeter: Measuring Around a Shape", summary:"Students learn that perimeter is the total distance around the outside edge of a shape, found by adding the lengths of all its sides.",
   resourceLabel:"YouTube: Perimeter: Measuring Around a Shape", resourceUrl:"https://www.youtube.com/results?search_query=Perimeter%3A%20Measuring%20Around%20a%20Shape%20grade%202%20educational",
   quiz:[
     {q:"What do we call the total distance around the outside edge of a shape?", options:["Mass","Area","Perimeter","Volume"], answer:2},
     {q:"If a square has sides of 4 centimetres each, what is its perimeter?", options:["16 centimetres","8 centimetres","4 centimetres","12 centimetres"], answer:0},
     {q:"To find the perimeter of a shape, we ___.", options:["Measure only one side","Multiply its width by its height","Count the squares inside it","Add the lengths of all its sides"], answer:3},
     {q:"What is the perimeter of a rectangle with sides of 3, 5, 3, and 5 centimetres?", options:["15 centimetres","8 centimetres","20 centimetres","16 centimetres"], answer:3},
     {q:"Perimeter is different from area because perimeter measures ___.", options:["The exact same thing as area","Only weight","Only the width of a shape","The distance around a shape, not the space inside it"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the distance around the outside edge of a shape?", answers:["perimeter"]},
     {prompt:"If a square has sides of 4 centimetres each, what is its perimeter?", answers:["16 centimetres","16"]},
     {prompt:"To find perimeter, do we add the lengths of all the sides?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Simple Circuits and Electricity", summary:"Students learn that a simple electric circuit is a complete loop that lets electricity flow from a battery through wires to power something like a light bulb.",
   resourceLabel:"YouTube: Simple Circuits and Electricity", resourceUrl:"https://www.youtube.com/results?search_query=Simple%20Circuits%20and%20Electricity%20grade%202%20educational",
   quiz:[
     {q:"What do we call a complete loop that lets electricity flow through it?", options:["A pattern","A magnet","A circuit","A pulley"], answer:2},
     {q:"Which of these provides the energy in a simple circuit?", options:["A cotton ball","A leaf","A battery","A wooden block"], answer:2},
     {q:"What happens to a light bulb in a circuit if the loop is broken?", options:["The light turns off","The light gets brighter","The light changes colour","Nothing changes"], answer:0},
     {q:"Which of these materials would work well as a wire in a circuit because it lets electricity flow through it?", options:["Paper","Rubber","Wood","Metal"], answer:3},
     {q:"A simple circuit usually includes a battery, wires, and ___.", options:["A cup of water","Something that uses electricity, like a light bulb","A stack of books","A pile of sand"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call a complete loop that lets electricity flow?", answers:["a circuit","circuit"]},
     {prompt:"Name one part of a simple circuit, like a battery or a wire.", answers:["a battery","battery","a wire","wire","a bulb","bulb"]},
     {prompt:"Does a circuit need to be a complete loop for electricity to flow?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Wildlife and Where Animals Live", summary:"Students learn about wildlife found across Canada, such as moose in forests, polar bears in the Arctic, and beavers near rivers and lakes, and how each animal is suited to where it lives.",
   resourceLabel:"YouTube: Canadian Wildlife and Where Animals Live", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Wildlife%20and%20Where%20Animals%20Live%20grade%202%20educational",
   quiz:[
     {q:"Which large animal is commonly found in Canadian forests?", options:["A moose","A camel","A penguin","A kangaroo"], answer:0},
     {q:"Which animal is well known for living in the cold Arctic region of Canada?", options:["A lion","A monkey","A polar bear","A parrot"], answer:2},
     {q:"Which animal is often found building dams near rivers and lakes in Canada?", options:["A beaver","A giraffe","An elephant","A camel"], answer:0},
     {q:"Why is a polar bear well suited to living in the Arctic?", options:["It only eats plants","It has thin fur to stay cool","It cannot swim in cold water","It has thick fur and fat to stay warm in the cold"], answer:3},
     {q:"Learning about Canadian wildlife helps us understand ___.", options:["How to read a clock","How to build houses","How to bake bread","How animals are suited to the places they live"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one animal found in Canadian forests, like a moose or a deer.", answers:["a moose","moose","a deer","deer"]},
     {prompt:"Name one animal that lives in the cold Arctic region of Canada.", answers:["a polar bear","polar bear"]},
     {prompt:"Name one animal often found living near rivers and lakes in Canada.", answers:["a beaver","beaver"]}
   ]},
]},
{day:49, label:"Day 49 — Thu", subjects:[
  {subject:"Language", title:"Writing Simple Instructions: How-To Writing", summary:"Students learn to write simple step-by-step instructions, called how-to writing, using order words like first, next, and last to explain how to do something.",
   resourceLabel:"YouTube: Writing Simple Instructions: How-To Writing", resourceUrl:"https://www.youtube.com/results?search_query=Writing%20Simple%20Instructions%3A%20How-To%20Writing%20grade%202%20educational",
   quiz:[
     {q:"What do we call writing that explains the steps to do something?", options:["A song","How-to writing","A poem","A letter"], answer:1},
     {q:"Which of these is an order word used in how-to writing?", options:["Blue","Quickly","Happy","First"], answer:3},
     {q:"Why is it important to write the steps of instructions in order?", options:["To make the writing longer","So the reader can follow them correctly","Order does not matter","So the reader gets confused"], answer:1},
     {q:"Which sentence would most likely begin a set of how-to instructions?", options:["The end.","First, gather all your materials.","Once upon a time.","Yesterday I went to the park."], answer:1},
     {q:"How-to writing is most useful for ___.", options:["Telling a make-believe story","Listing opinions about a topic","Describing a characters feelings","Explaining how to complete a task step by step"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call writing that explains the steps to do something?", answers:["how-to writing","instructions"]},
     {prompt:"Name one order word used in how-to writing, like first or next.", answers:["first","next","last","then"]},
     {prompt:"Should the steps in how-to writing be written in the correct order?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Ordinal Numbers: First, Second, Third", summary:"Students learn to use ordinal numbers, such as first, second, and third, to describe the position or order of objects and events in a sequence.",
   resourceLabel:"YouTube: Ordinal Numbers: First, Second, Third", resourceUrl:"https://www.youtube.com/results?search_query=Ordinal%20Numbers%3A%20First%2C%20Second%2C%20Third%20grade%202%20educational",
   quiz:[
     {q:"Which ordinal number describes the object at the very start of a line?", options:["Second","Fourth","First","Third"], answer:2},
     {q:"Which ordinal number comes right after first?", options:["Fourth","Fifth","Third","Second"], answer:3},
     {q:"If a student is the third person in line, which two students came before them?", options:["The fourth and fifth students","Only the first student","No one came before them","The first and second students"], answer:3},
     {q:"Ordinal numbers are used to describe ___.", options:["The exact amount of something","The weight of an object","The position or order of something in a sequence","The temperature outside"], answer:2},
     {q:"Which of these is an ordinal number?", options:["Five","Fifty","Fives","Fifth"], answer:3}
   ],
   worksheet:[
     {prompt:"Which ordinal number describes the very first object in a line?", answers:["first"]},
     {prompt:"Which ordinal number describes the object right after the first one?", answers:["second"]},
     {prompt:"If a runner finishes the race in third place, what ordinal number describes their position?", answers:["third"]}
   ]},
  {subject:"Science", title:"Classifying Animals: Mammals, Birds, Fish, and More", summary:"Students learn to classify animals into groups such as mammals, birds, fish, reptiles, and amphibians, based on shared features like fur, feathers, scales, or how they breathe.",
   resourceLabel:"YouTube: Classifying Animals: Mammals, Birds, Fish, and More", resourceUrl:"https://www.youtube.com/results?search_query=Classifying%20Animals%3A%20Mammals%2C%20Birds%2C%20Fish%2C%20and%20More%20grade%202%20educational",
   quiz:[
     {q:"Which animal group is covered in fur and feeds its babies milk?", options:["Reptiles","Birds","Fish","Mammals"], answer:3},
     {q:"Which animal group is covered in feathers and can usually fly?", options:["Fish","Birds","Mammals","Amphibians"], answer:1},
     {q:"Which animal group lives mostly in water and breathes using gills?", options:["Fish","Mammals","Insects","Birds"], answer:0},
     {q:"Which of these is an example of a reptile?", options:["A frog","A robin","A snake","A dog"], answer:2},
     {q:"Scientists classify animals into groups based on ___.", options:["Shared features like fur, feathers, or scales","Their favourite colour","Their name only","Where they were born only"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one group that animals with fur and that feed their babies milk belong to.", answers:["mammals","mammal"]},
     {prompt:"Name one feature that helps classify a bird, like feathers or wings.", answers:["feathers","wings"]},
     {prompt:"Name one group of animals that live mostly in water and breathe with gills.", answers:["fish"]}
   ]},
  {subject:"SocialStudies", title:"Communication Long Ago and Today", summary:"Students compare how people communicated long ago, using letters and messengers, with how people communicate today, using telephones, computers, and the internet.",
   resourceLabel:"YouTube: Communication Long Ago and Today", resourceUrl:"https://www.youtube.com/results?search_query=Communication%20Long%20Ago%20and%20Today%20grade%202%20educational",
   quiz:[
     {q:"Which of these was a common way people communicated with each other long ago?", options:["Using the internet","Writing a letter","Sending a text message","Video calling"], answer:1},
     {q:"Which of these tools helps people communicate quickly over long distances today?", options:["A carrier pigeon only","A telephone","A messenger on foot only","A quill pen only"], answer:1},
     {q:"How has communication changed from long ago to today?", options:["It has completely stopped","It has become much faster with new technology","It has stayed exactly the same","It has become much slower"], answer:1},
     {q:"Long ago, how might an important message have been delivered to a faraway town?", options:["By a video call","By email","By a messenger traveling on foot or horseback","By a text message"], answer:2},
     {q:"Fast communication today, like the internet, allows people to ___.", options:["Wait many weeks to send a simple message","Never talk to people far away","Share information and messages almost instantly","Only communicate in person"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one way people communicated long ago, like writing a letter.", answers:["a letter","letter","writing a letter"]},
     {prompt:"Name one way people communicate quickly today, like a telephone or computer.", answers:["a telephone","telephone","a computer","computer","the internet"]},
     {prompt:"Is communicating with someone far away usually faster today than it was long ago?", answers:["yes"]}
   ]},
]},
{day:50, label:"Day 50 — Fri", subjects:[
  {subject:"Language", title:"Final Review: Sentence Combining, Fact and Opinion, Dictionaries and How-To Writing", summary:"Students review recent Language skills: combining sentences with joining words, fact versus opinion, using a dictionary and glossary, and how-to writing.",
   resourceLabel:"YouTube: Final Review: Sentence Combining, Fact and Opinion, Dictionaries and How-To Writing", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Sentence%20Combining%2C%20Fact%20and%20Opinion%2C%20Dictionaries%20and%20How-To%20Writing%20grade%202%20educational",
   quiz:[
     {q:"Which joining word shows a contrast or difference between two ideas?", options:["Because","But","Or","And"], answer:1},
     {q:"Which of these sentences is a fact?", options:["Pizza is the tastiest food.","Summer is the best season.","A week has seven days.","Cats are better than dogs."], answer:2},
     {q:"What do we call a list of important words and their meanings at the back of a book?", options:["An index card","A table of contents","A title page","A glossary"], answer:3},
     {q:"Which of these is an order word used in how-to writing?", options:["First","Blue","Happy","Quickly"], answer:0},
     {q:"Combining short sentences into one longer sentence can make writing ___.", options:["Smoother and more interesting","Shorter than one word","Always incorrect","Impossible to read"], answer:0}
   ],
   worksheet:[
     {prompt:"Which joining word gives a reason for something?", answers:["because"]},
     {prompt:"Is the statement dogs are the best pets a fact or an opinion?", answers:["an opinion","opinion"]},
     {prompt:"Name one order word used in how-to writing, like first or next.", answers:["first","next","last","then"]}
   ]},
  {subject:"Math", title:"Final Review: Rounding, Area, Perimeter and Ordinal Numbers", summary:"Students review recent Math skills: rounding to the nearest ten, area, perimeter, and ordinal numbers.",
   resourceLabel:"YouTube: Final Review: Rounding, Area, Perimeter and Ordinal Numbers", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Rounding%2C%20Area%2C%20Perimeter%20and%20Ordinal%20Numbers%20grade%202%20educational",
   quiz:[
     {q:"What is 47 rounded to the nearest ten?", options:["47","50","40","45"], answer:1},
     {q:"To measure area, we count how many equal ___ fit inside a shape.", options:["Squares","Circles","Lines","Dots"], answer:0},
     {q:"To find the perimeter of a shape, we ___.", options:["Add the lengths of all its sides","Multiply its width by its height","Measure only one side","Count the squares inside it"], answer:0},
     {q:"If a student is the third person in line, which two students came before them?", options:["The first and second students","Only the first student","No one came before them","The fourth and fifth students"], answer:0},
     {q:"What is the perimeter of a rectangle with sides of 3, 5, 3, and 5 centimetres?", options:["8 centimetres","15 centimetres","20 centimetres","16 centimetres"], answer:3}
   ],
   worksheet:[
     {prompt:"What is 23 rounded to the nearest ten?", answers:["20","twenty"]},
     {prompt:"What do we call the amount of space a flat shape covers?", answers:["area"]},
     {prompt:"Which ordinal number comes right after first?", answers:["second"]}
   ]},
  {subject:"Science", title:"Final Review: Migration, Pollination, Circuits and Animal Classification", summary:"Students review recent Science topics: animal migration and hibernation, pollination, simple circuits and electricity, and classifying animals.",
   resourceLabel:"YouTube: Final Review: Migration, Pollination, Circuits and Animal Classification", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Migration%2C%20Pollination%2C%20Circuits%20and%20Animal%20Classification%20grade%202%20educational",
   quiz:[
     {q:"Which of these animals is known for hibernating in winter?", options:["A fish","A butterfly","A bear","A goose"], answer:2},
     {q:"Why is pollination important for plants?", options:["It helps plants make seeds and grow new plants","It stops plants from growing","It has no effect on plants","It helps plants stay small forever"], answer:0},
     {q:"What happens to a light bulb in a circuit if the loop is broken?", options:["The light changes colour","Nothing changes","The light turns off","The light gets brighter"], answer:2},
     {q:"Which animal group is covered in fur and feeds its babies milk?", options:["Fish","Reptiles","Mammals","Birds"], answer:2},
     {q:"Which of these is an example of a reptile?", options:["A dog","A snake","A robin","A frog"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call it when animals travel long distances to find food or warmer weather?", answers:["migration","migrate"]},
     {prompt:"What is the powder inside a flower called that bees carry from flower to flower?", answers:["pollen"]},
     {prompt:"What do we call a complete loop that lets electricity flow?", answers:["a circuit","circuit"]}
   ]},
  {subject:"SocialStudies", title:"Final Review: Diversity, Schools and Libraries, Wildlife and Communication", summary:"Students review recent Social Studies topics: cultural diversity, the role of schools and libraries, Canadian wildlife, and communication long ago and today.",
   resourceLabel:"YouTube: Final Review: Diversity, Schools and Libraries, Wildlife and Communication", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Diversity%2C%20Schools%20and%20Libraries%2C%20Wildlife%20and%20Communication%20grade%202%20educational",
   quiz:[
     {q:"Why is it helpful to learn about different cultures in your community?", options:["It has no benefit at all","It makes people forget their own culture","It causes communities to fall apart","It helps people understand and respect each other"], answer:3},
     {q:"Who can usually use the resources at a public library?", options:["People of all ages","Only children","Only adults","Only teachers"], answer:0},
     {q:"Which animal is often found building dams near rivers and lakes in Canada?", options:["A camel","A giraffe","An elephant","A beaver"], answer:3},
     {q:"How has communication changed from long ago to today?", options:["It has become much slower","It has become much faster with new technology","It has completely stopped","It has stayed exactly the same"], answer:1},
     {q:"Celebrating cultural diversity means ___.", options:["Avoiding people who are different","Ignoring all traditions","Valuing and respecting many different backgrounds and traditions","Only valuing one culture"], answer:2}
   ],
   worksheet:[
     {prompt:"What word describes a community made up of people from many different cultures?", answers:["diverse","diversity"]},
     {prompt:"What do we call a place where people can borrow books for free?", answers:["a library","library"]},
     {prompt:"Name one animal that lives in the cold Arctic region of Canada.", answers:["a polar bear","polar bear"]}
   ]},
]},
{day:51, label:"Day 51 — Mon", subjects:[
  {subject:"Language", title:"Regular Past Tense Verbs: Adding -ed", summary:"Students learn that many verbs show something already happened by adding the ending -ed, such as jump becoming jumped, walk becoming walked, and play becoming played.",
   resourceLabel:"YouTube: Regular Past Tense Verbs: Adding -ed", resourceUrl:"https://www.youtube.com/results?search_query=Regular%20Past%20Tense%20Verbs%3A%20Adding%20-ed%20grade%202%20educational",
   quiz:[
     {q:"What ending do we usually add to a verb to show something already happened?", options:["-est","-er","-ed","-ing"], answer:2},
     {q:"What is the past tense of the verb jump?", options:["Jumps","Jumpy","Jumping","Jumped"], answer:3},
     {q:"What is the past tense of the verb walk?", options:["Walker","Walking","Walks","Walked"], answer:3},
     {q:"Which sentence uses the correct past tense of play?", options:["Yesterday I plays outside.","Yesterday I played outside.","Yesterday I play outside.","Yesterday I playing outside."], answer:1},
     {q:"Adding -ed to a verb tells the reader that an action ___.", options:["Will happen soon","Is happening right now","Already happened","Never happened"], answer:2}
   ],
   worksheet:[
     {prompt:"What ending do we usually add to a verb to show it already happened?", answers:["-ed","ed"]},
     {prompt:"What is the past tense of the verb jump?", answers:["jumped"]},
     {prompt:"What is the past tense of the verb walk?", answers:["walked"]}
   ]},
  {subject:"Math", title:"Skip Counting by 3s and 4s", summary:"Students practice skip counting by 3s and by 4s, extending patterns such as 3, 6, 9, 12 and 4, 8, 12, 16 to build number sense.",
   resourceLabel:"YouTube: Skip Counting by 3s and 4s", resourceUrl:"https://www.youtube.com/results?search_query=Skip%20Counting%20by%203s%20and%204s%20grade%202%20educational",
   quiz:[
     {q:"Skip count by 3s: 3, 6, 9, ___", options:["15","10","11","12"], answer:3},
     {q:"Skip count by 4s: 4, 8, 12, ___", options:["14","15","16","20"], answer:2},
     {q:"Which set of numbers shows skip counting by 3s?", options:["5, 10, 15, 20","4, 8, 12, 16","3, 6, 9, 12","2, 4, 6, 8"], answer:2},
     {q:"Which set of numbers shows skip counting by 4s?", options:["5, 10, 15, 20","3, 6, 9, 12","4, 8, 12, 16","2, 4, 6, 8"], answer:2},
     {q:"Skip counting by 3s and 4s helps us ___.", options:["Count in equal groups more quickly","Read a clock","Tell time","Measure length"], answer:0}
   ],
   worksheet:[
     {prompt:"Skip count by 3s: 3, 6, 9, ___", answers:["12","twelve"]},
     {prompt:"Skip count by 4s: 4, 8, 12, ___", answers:["16","sixteen"]},
     {prompt:"What number comes next when skip counting by 3s: 9, 12, 15, ___?", answers:["18","eighteen"]}
   ]},
  {subject:"Science", title:"Animal Camouflage: Hiding in Plain Sight", summary:"Students learn that camouflage happens when the color or pattern of an animal helps it blend into its surroundings, making it harder for predators or prey to see it.",
   resourceLabel:"YouTube: Animal Camouflage: Hiding in Plain Sight", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Camouflage%3A%20Hiding%20in%20Plain%20Sight%20grade%202%20educational",
   quiz:[
     {q:"What word describes an animal blending into its surroundings using color or pattern?", options:["Pollination","Migration","Hibernation","Camouflage"], answer:3},
     {q:"Why might an animal use camouflage?", options:["To fly faster","To hide from predators or sneak up on prey","To change the weather","To make more noise"], answer:1},
     {q:"Which animal is well known for using camouflage to blend into leaves?", options:["A stick insect","A peacock","A flamingo","A penguin"], answer:0},
     {q:"The white fur of a polar bear helps it camouflage in ___.", options:["A sandy desert","A rocky cave","A green forest","Snow and ice"], answer:3},
     {q:"Camouflage helps animals survive by ___.", options:["Making them harder to see in their habitat","Making them louder","Making them run faster","Making them brighter colors always"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes an animal blending into its surroundings using color or pattern?", answers:["camouflage"]},
     {prompt:"Name one reason an animal might use camouflage, like hiding from a predator.", answers:["hiding from a predator","to hide from predators","to hide from prey"]},
     {prompt:"Name one animal that uses camouflage, like a frog or a stick insect.", answers:["a frog","frog","a stick insect","stick insect","a chameleon","chameleon"]}
   ]},
  {subject:"SocialStudies", title:"Notable Canadians and Their Achievements", summary:"Students learn about notable Canadians from the past and present who made important contributions in fields such as science, sports, and the arts.",
   resourceLabel:"YouTube: Notable Canadians and Their Achievements", resourceUrl:"https://www.youtube.com/results?search_query=Notable%20Canadians%20and%20Their%20Achievements%20grade%202%20educational",
   quiz:[
     {q:"What word describes a person who is well known for an important contribution?", options:["Invisible","Ordinary","Silent","Notable"], answer:3},
     {q:"Which of these is a field where a notable Canadian might make a contribution?", options:["Only traveling","Only sleeping","Only eating","Science, sports, or the arts"], answer:3},
     {q:"Why is it valuable to learn about notable Canadians?", options:["It helps us understand important achievements and history","It teaches nothing about Canada","It has no value at all","It only teaches math"], answer:0},
     {q:"A notable Canadian scientist might be remembered for ___.", options:["An important discovery or invention","Losing a game","Staying home all day","Forgetting their homework"], answer:0},
     {q:"Learning about people who made a difference can inspire us to ___.", options:["Avoid learning new things","Ignore our community","Stop trying new things","Work hard and contribute to our community"], answer:3}
   ],
   worksheet:[
     {prompt:"What word describes a person who is well known for an important contribution?", answers:["notable","famous"]},
     {prompt:"Name one field where a notable Canadian might make a contribution, like science or sports.", answers:["science","sports","the arts","music"]},
     {prompt:"Why do we learn about notable Canadians in social studies?", answers:["to learn about their achievements","to learn about important contributions","to learn about their achievements and history"]}
   ]},
]},
{day:52, label:"Day 52 — Tue", subjects:[
  {subject:"Language", title:"Capitalization Rules: Names, Places, and Titles", summary:"Students learn that capital letters are used at the beginning of names of people, places, and titles, such as Sarah, Toronto, and the title of a book.",
   resourceLabel:"YouTube: Capitalization Rules: Names, Places, and Titles", resourceUrl:"https://www.youtube.com/results?search_query=Capitalization%20Rules%3A%20Names%2C%20Places%2C%20and%20Titles%20grade%202%20educational",
   quiz:[
     {q:"What kind of letter starts the name of a person, like Sarah?", options:["A lowercase letter","A capital letter","A number","A silent letter"], answer:1},
     {q:"Which of these words should start with a capital letter?", options:["dog","the","and","Toronto"], answer:3},
     {q:"Which sentence uses capitalization correctly?", options:["my friend sam lives in ottawa.","My friend Sam lives in Ottawa.","My Friend sam Lives in ottawa.","my friend Sam lives in Ottawa."], answer:1},
     {q:"The first word in the title of a book should begin with a ___.", options:["Question mark","Capital letter","Number","Lowercase letter"], answer:1},
     {q:"Capitalization rules help readers know that a word is ___.", options:["A special name for a person, place, or title","Always plural","Always a verb","Always short"], answer:0}
   ],
   worksheet:[
     {prompt:"What kind of letter starts the name of a person?", answers:["a capital letter","capital letter"]},
     {prompt:"Should the name of a city, like Toronto, start with a capital letter?", answers:["yes"]},
     {prompt:"Name one type of word that always starts with a capital letter, like a name or a place.", answers:["a name","name","a place","place","a title","title"]}
   ]},
  {subject:"Math", title:"Introduction to Division: Sharing Equally into Groups", summary:"Students learn that division means sharing a group of objects equally into smaller groups, such as sharing 12 apples equally among 3 friends so each friend gets 4.",
   resourceLabel:"YouTube: Introduction to Division: Sharing Equally into Groups", resourceUrl:"https://www.youtube.com/results?search_query=Introduction%20to%20Division%3A%20Sharing%20Equally%20into%20Groups%20grade%202%20educational",
   quiz:[
     {q:"What do we call splitting a group of objects equally into smaller groups?", options:["Multiplication","Rounding","Addition","Division"], answer:3},
     {q:"If you share 12 apples equally among 3 friends, how many apples does each friend get?", options:["4","3","6","12"], answer:0},
     {q:"If you share 10 stickers equally between 2 friends, how many stickers does each friend get?", options:["5","10","2","4"], answer:0},
     {q:"If you share 8 cookies equally among 4 friends, how many cookies does each friend get?", options:["4","1","8","2"], answer:3},
     {q:"Sharing a group of objects equally means each group gets ___.", options:["The same amount","Only one object total","A different amount each time","Nothing at all"], answer:0}
   ],
   worksheet:[
     {prompt:"If you share 12 apples equally among 3 friends, how many apples does each friend get?", answers:["4","four"]},
     {prompt:"What do we call splitting a group of objects equally into smaller groups?", answers:["division","sharing equally"]},
     {prompt:"If you share 10 stickers equally between 2 friends, how many stickers does each friend get?", answers:["5","five"]}
   ]},
  {subject:"Science", title:"Life Cycle of a Butterfly: Metamorphosis", summary:"Students learn the life cycle of a butterfly, called metamorphosis, which includes the stages of egg, caterpillar, chrysalis, and adult butterfly.",
   resourceLabel:"YouTube: Life Cycle of a Butterfly: Metamorphosis", resourceUrl:"https://www.youtube.com/results?search_query=Life%20Cycle%20of%20a%20Butterfly%3A%20Metamorphosis%20grade%202%20educational",
   quiz:[
     {q:"What is the first stage of a butterfly life cycle?", options:["Egg","Adult butterfly","Caterpillar","Chrysalis"], answer:0},
     {q:"What do we call a young butterfly that hatches from an egg and eats leaves?", options:["A chick","A caterpillar","A cub","A tadpole"], answer:1},
     {q:"What do we call the stage where a caterpillar forms a hard case and changes shape?", options:["Burrow","Chrysalis","Nest","Web"], answer:1},
     {q:"Put the butterfly life cycle stages in the correct order.", options:["Adult butterfly, egg, chrysalis, caterpillar","Caterpillar, adult butterfly, egg, chrysalis","Chrysalis, egg, caterpillar, adult butterfly","Egg, caterpillar, chrysalis, adult butterfly"], answer:3},
     {q:"The complete change in body shape that a butterfly goes through is called ___.", options:["Hibernation","Pollination","Metamorphosis","Migration"], answer:2}
   ],
   worksheet:[
     {prompt:"What is the first stage of a butterfly life cycle?", answers:["egg","an egg"]},
     {prompt:"What do we call a young butterfly that hatches from an egg and eats leaves?", answers:["a caterpillar","caterpillar"]},
     {prompt:"What do we call the changing process a caterpillar goes through inside a chrysalis?", answers:["metamorphosis"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Inventions That Changed the World", summary:"Students learn about inventions created in Canada that changed the way people live, work, and play, such as basketball and insulin.",
   resourceLabel:"YouTube: Canadian Inventions That Changed the World", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Inventions%20That%20Changed%20the%20World%20grade%202%20educational",
   quiz:[
     {q:"What word describes something new that a person creates for the first time?", options:["An invention","A festival","A tradition","A landmark"], answer:0},
     {q:"Which sport was invented by a Canadian named James Naismith?", options:["Soccer","Basketball","Baseball","Tennis"], answer:1},
     {q:"Why are inventions important to a community?", options:["They always cause problems","They can solve problems and make life easier","They stop people from working","They have no effect on daily life"], answer:1},
     {q:"Insulin, an important medicine, was discovered by scientists working in which country?", options:["Brazil","Australia","Egypt","Canada"], answer:3},
     {q:"Learning about inventions helps us understand ___.", options:["How to play music","How to grow plants","How new ideas can improve daily life","How to bake bread"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one invention or discovery created in Canada, like basketball or insulin.", answers:["basketball","insulin"]},
     {prompt:"What word describes something new that a person creates for the first time?", answers:["an invention","invention"]},
     {prompt:"Why are inventions important to a community?", answers:["they solve problems","they make life easier","they help people"]}
   ]},
]},
{day:53, label:"Day 53 — Wed", subjects:[
  {subject:"Language", title:"Multiple-Meaning Words", summary:"Students learn that some words have more than one meaning depending on how they are used in a sentence, such as bat, an animal or something used to hit a ball, and bark, the sound a dog makes or the covering of a tree.",
   resourceLabel:"YouTube: Multiple-Meaning Words", resourceUrl:"https://www.youtube.com/results?search_query=Multiple-Meaning%20Words%20grade%202%20educational",
   quiz:[
     {q:"What do we call a word that has more than one meaning?", options:["A multiple-meaning word","A synonym","An antonym","A silent letter"], answer:0},
     {q:"In the sentence, the dog began to bark, what does bark mean?", options:["A type of boat","The covering of a tree","A baseball bat","The sound a dog makes"], answer:3},
     {q:"In the sentence, the bark of the tree was rough, what does bark mean?", options:["The covering of a tree","A flying animal","A type of ball","The sound a dog makes"], answer:0},
     {q:"Which word can mean both an animal and a piece of sports equipment?", options:["Dog","Chair","Tree","Bat"], answer:3},
     {q:"To figure out which meaning of a word is being used, readers should ___.", options:["Guess without reading","Look at the other words in the sentence","Ignore the sentence completely","Only look at the first letter"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one word that can mean two different things, like bat or bark.", answers:["bat","bark","ring","bank"]},
     {prompt:"In the sentence, the dog began to bark, what does bark mean?", answers:["the sound a dog makes","dog sound","sound"]},
     {prompt:"In the sentence, we saw a bat flying at night, what does bat mean?", answers:["an animal","animal","flying animal"]}
   ]},
  {subject:"Math", title:"Probability: Likely, Unlikely, Certain, and Impossible", summary:"Students learn to describe the chance of an event happening using the words certain, likely, unlikely, and impossible.",
   resourceLabel:"YouTube: Probability: Likely, Unlikely, Certain, and Impossible", resourceUrl:"https://www.youtube.com/results?search_query=Probability%3A%20Likely%2C%20Unlikely%2C%20Certain%2C%20and%20Impossible%20grade%202%20educational",
   quiz:[
     {q:"What word describes an event that will definitely happen?", options:["Certain","Unlikely","Impossible","Random"], answer:0},
     {q:"What word describes an event that can never happen?", options:["Probable","Impossible","Likely","Certain"], answer:1},
     {q:"Is it certain or unlikely that the sun will rise tomorrow?", options:["Impossible","Unlikely","Certain","Random"], answer:2},
     {q:"Is it likely or unlikely that it will snow in Ontario in July?", options:["Impossible","Certain","Likely","Unlikely"], answer:3},
     {q:"If a bag has only red marbles, picking a blue marble is ___.", options:["Likely","Certain","Unlikely but possible","Impossible"], answer:3}
   ],
   worksheet:[
     {prompt:"What word describes an event that will definitely happen?", answers:["certain"]},
     {prompt:"What word describes an event that will definitely not happen?", answers:["impossible"]},
     {prompt:"Is it likely or unlikely that it will snow in July in Ontario?", answers:["unlikely"]}
   ]},
  {subject:"Science", title:"Bones and Muscles: How Our Body Moves", summary:"Students learn that bones form a skeleton that supports and protects the body, while muscles work with bones to help the body move.",
   resourceLabel:"YouTube: Bones and Muscles: How Our Body Moves", resourceUrl:"https://www.youtube.com/results?search_query=Bones%20and%20Muscles%3A%20How%20Our%20Body%20Moves%20grade%202%20educational",
   quiz:[
     {q:"What do we call the frame of bones that supports our body?", options:["A skeleton","A muscle","An organ","A joint"], answer:0},
     {q:"What body part works together with bones to help us move?", options:["Skin","Nails","Muscles","Hair"], answer:2},
     {q:"Which of these is a job that bones do for the body?", options:["Digesting food","Seeing light","Protecting organs like the heart and brain","Pumping blood"], answer:2},
     {q:"Where would you find the bones that protect your brain?", options:["The hand","The skull","The leg","The arm"], answer:1},
     {q:"Muscles help the body move by ___.", options:["Turning into skin","Pulling on bones to create movement","Making bones disappear","Stopping the heart"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call the frame of bones inside our body?", answers:["a skeleton","skeleton"]},
     {prompt:"What body part works with bones to help us move?", answers:["muscles","muscle"]},
     {prompt:"Name one job that bones do for our body, like protecting organs.", answers:["protecting organs","support the body","protect the body"]}
   ]},
  {subject:"SocialStudies", title:"How We Get Our Water: From Source to Tap", summary:"Students learn how water travels from lakes and rivers, through a treatment plant that makes it clean, and finally through pipes to homes and schools.",
   resourceLabel:"YouTube: How We Get Our Water: From Source to Tap", resourceUrl:"https://www.youtube.com/results?search_query=How%20We%20Get%20Our%20Water%3A%20From%20Source%20to%20Tap%20grade%202%20educational",
   quiz:[
     {q:"Where might the water that reaches our homes first come from?", options:["A grocery store","A cloud only","A lake or river","A library"], answer:2},
     {q:"What do we call a place that cleans water so it is safe to drink?", options:["A fire station","A school","A water treatment plant","A farm"], answer:2},
     {q:"How does clean water usually travel from a treatment plant to our homes?", options:["Through underground pipes","By airplane","By boat only","By truck only"], answer:0},
     {q:"Why is it important to clean water before people drink it?", options:["To make it taste like juice","To remove dirt and germs so it is safe","To make it colder","To make it a different color"], answer:1},
     {q:"Communities build water systems so that people can ___.", options:["Never use water at all","Avoid drinking water completely","Only use rainwater","Have safe, clean water for drinking and washing"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one place water might come from before it reaches our homes, like a lake or river.", answers:["a lake","lake","a river","river"]},
     {prompt:"What do we call a place that cleans water before it reaches our homes?", answers:["a treatment plant","treatment plant","water treatment plant"]},
     {prompt:"How does clean water travel from a treatment plant to our homes?", answers:["through pipes","pipes"]}
   ]},
]},
{day:54, label:"Day 54 — Thu", subjects:[
  {subject:"Language", title:"Using Context Clues to Find Word Meaning", summary:"Students learn to use context clues, the words and sentences around an unfamiliar word, to figure out what that word probably means.",
   resourceLabel:"YouTube: Using Context Clues to Find Word Meaning", resourceUrl:"https://www.youtube.com/results?search_query=Using%20Context%20Clues%20to%20Find%20Word%20Meaning%20grade%202%20educational",
   quiz:[
     {q:"What do we call the words and sentences around an unfamiliar word that help us understand its meaning?", options:["Context clues","Silent letters","Compound words","Rhyming words"], answer:0},
     {q:"If a sentence says, the enormous elephant was huge and heavy, what does enormous most likely mean?", options:["Very small","Very quiet","Very fast","Very big"], answer:3},
     {q:"Why should readers use context clues when they find an unfamiliar word?", options:["To change the word into a picture","To figure out its meaning without a dictionary","To stop reading the book","To skip the word completely"], answer:1},
     {q:"If a sentence says, the frigid winter air made her shiver, what does frigid most likely mean?", options:["Very bright","Very loud","Very cold","Very hot"], answer:2},
     {q:"Context clues can be found ___.", options:["Only in the title of the book","In the words and sentences near the unfamiliar word","Only in pictures","Only in the dictionary"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call the words around an unfamiliar word that help us guess its meaning?", answers:["context clues"]},
     {prompt:"If a sentence says, the enormous elephant was huge and heavy, what might enormous mean?", answers:["very big","huge","big"]},
     {prompt:"Why are context clues useful when reading?", answers:["they help us understand new words","help figure out word meaning"]}
   ]},
  {subject:"Math", title:"Using a Number Line to Add and Subtract", summary:"Students learn to use a number line as a tool to add by jumping forward and to subtract by jumping backward.",
   resourceLabel:"YouTube: Using a Number Line to Add and Subtract", resourceUrl:"https://www.youtube.com/results?search_query=Using%20a%20Number%20Line%20to%20Add%20and%20Subtract%20grade%202%20educational",
   quiz:[
     {q:"On a number line, which direction do you jump to add numbers?", options:["Backward","Forward","You do not move","Sideways"], answer:1},
     {q:"On a number line, which direction do you jump to subtract numbers?", options:["Backward","Forward","Upward","Downward"], answer:0},
     {q:"Starting at 5 on a number line and jumping forward 3, where do you land?", options:["2","6","8","9"], answer:2},
     {q:"Starting at 10 on a number line and jumping backward 4, where do you land?", options:["4","8","14","6"], answer:3},
     {q:"A number line is a useful tool because it helps us ___.", options:["Only measure weight","Only count coins","See addition and subtraction as jumps forward or backward","Only tell time"], answer:2}
   ],
   worksheet:[
     {prompt:"On a number line, which direction do you jump to add?", answers:["forward","to the right"]},
     {prompt:"On a number line, which direction do you jump to subtract?", answers:["backward","to the left"]},
     {prompt:"Starting at 5 on a number line and jumping forward 3, where do you land?", answers:["8","eight"]}
   ]},
  {subject:"Science", title:"The Phases of the Moon", summary:"Students learn that the moon appears to change shape in the sky over about a month, moving through phases such as new moon, crescent, half moon, and full moon.",
   resourceLabel:"YouTube: The Phases of the Moon", resourceUrl:"https://www.youtube.com/results?search_query=The%20Phases%20of%20the%20Moon%20grade%202%20educational",
   quiz:[
     {q:"What do we call the changing shapes of the moon that we see in the sky?", options:["Seasons","Phases of the moon","Constellations","Eclipses"], answer:1},
     {q:"Which phase of the moon looks like a complete bright circle?", options:["New moon","Crescent moon","Full moon","Half moon"], answer:2},
     {q:"During a new moon, how much of the moon can we usually see?", options:["Very little or none","The whole moon","Exactly half","Three quarters"], answer:0},
     {q:"About how long does it take the moon to go through all of its phases?", options:["About a week","About a year","About a day","About a month"], answer:3},
     {q:"The moon appears to change shape because ___.", options:["We see different amounts of its sunlit side as it orbits earth","The moon changes size","The moon turns a different color","The moon disappears and reappears"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the changing shapes of the moon we see in the sky?", answers:["phases of the moon","moon phases"]},
     {prompt:"Name one phase of the moon, like full moon or new moon.", answers:["full moon","new moon","crescent","half moon"]},
     {prompt:"About how long does it take the moon to go through all its phases?", answers:["about a month","one month","a month"]}
   ]},
  {subject:"SocialStudies", title:"Types of Homes Around the World", summary:"Students learn that people around the world live in many different types of homes, such as apartments, houses, igloos, and huts, often built to suit the climate and resources of their region.",
   resourceLabel:"YouTube: Types of Homes Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Types%20of%20Homes%20Around%20the%20World%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a type of home people might live in?", options:["An apartment","A mountain","A cloud","A river"], answer:0},
     {q:"Why might homes look different in different parts of the world?", options:["Different climates and available resources","All homes are exactly the same everywhere","Weather does not affect homes","Homes never change"], answer:0},
     {q:"Which type of home was traditionally built to suit a very cold, snowy climate?", options:["A houseboat","A beach hut","A treehouse","An igloo"], answer:3},
     {q:"In a crowded city, many people might choose to live in a ___.", options:["A large farm","An apartment building","A floating village","A desert tent"], answer:1},
     {q:"Learning about homes around the world helps us understand ___.", options:["How to build roads","How people adapt to their environment","How to grow crops","How to read a map only"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one type of home people might live in, like an apartment or a house.", answers:["an apartment","apartment","a house","house","an igloo","igloo"]},
     {prompt:"Why might homes look different in different parts of the world?", answers:["different climates","different resources","climate and resources"]},
     {prompt:"Name a type of home built to suit a cold, snowy climate.", answers:["an igloo","igloo"]}
   ]},
]},
{day:55, label:"Day 55 — Fri", subjects:[
  {subject:"Language", title:"Onomatopoeia: Sound Words in Stories", summary:"Students learn that onomatopoeia words imitate the sound they describe, such as buzz, crash, splash, and pop, adding excitement to writing.",
   resourceLabel:"YouTube: Onomatopoeia: Sound Words in Stories", resourceUrl:"https://www.youtube.com/results?search_query=Onomatopoeia%3A%20Sound%20Words%20in%20Stories%20grade%202%20educational",
   quiz:[
     {q:"What do we call a word that imitates the sound it describes?", options:["An antonym","Onomatopoeia","A synonym","A compound word"], answer:1},
     {q:"Which of these words is an example of onomatopoeia?", options:["Buzz","Quickly","Elephant","Happy"], answer:0},
     {q:"Which onomatopoeia word describes the sound of something falling into water?", options:["Pop","Crash","Buzz","Splash"], answer:3},
     {q:"Which onomatopoeia word describes the sound of two objects colliding loudly?", options:["Hum","Splash","Whisper","Crash"], answer:3},
     {q:"Writers use onomatopoeia to ___.", options:["Remove all sounds from a story","Confuse the reader","Make writing longer only","Help readers imagine the sounds in a story"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call a word that imitates the sound it describes, like buzz or splash?", answers:["onomatopoeia"]},
     {prompt:"Name one onomatopoeia word that describes the sound a bee makes.", answers:["buzz"]},
     {prompt:"Name one onomatopoeia word that describes the sound something makes when it falls into water.", answers:["splash"]}
   ]},
  {subject:"Math", title:"Measuring Mass with Grams and Kilograms", summary:"Students learn that mass, or how heavy an object is, can be measured using grams for lighter objects and kilograms for heavier objects.",
   resourceLabel:"YouTube: Measuring Mass with Grams and Kilograms", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Mass%20with%20Grams%20and%20Kilograms%20grade%202%20educational",
   quiz:[
     {q:"What unit would you most likely use to measure the mass of a paperclip?", options:["Litres","Centimetres","Grams","Kilograms"], answer:2},
     {q:"What unit would you most likely use to measure the mass of a large dog?", options:["Kilograms","Metres","Millilitres","Grams"], answer:0},
     {q:"Which is heavier, 1 kilogram or 1 gram?", options:["They are equal","1 gram","Cannot tell","1 kilogram"], answer:3},
     {q:"What tool would you use to measure the mass of an object?", options:["A thermometer","A scale","A ruler","A clock"], answer:1},
     {q:"Mass tells us ___.", options:["How hot an object is","How much liquid an object holds","How long an object is","How heavy an object is"], answer:3}
   ],
   worksheet:[
     {prompt:"What unit would you use to measure the mass of a light object, like a pencil?", answers:["grams","gram"]},
     {prompt:"What unit would you use to measure the mass of a heavy object, like a dog?", answers:["kilograms","kilogram"]},
     {prompt:"Which is heavier, 1 kilogram or 1 gram?", answers:["1 kilogram","kilogram"]}
   ]},
  {subject:"Science", title:"How Wind and Water Change the Land: Erosion", summary:"Students learn that erosion happens when wind and water slowly wear away rock and soil, changing the shape of the land over time.",
   resourceLabel:"YouTube: How Wind and Water Change the Land: Erosion", resourceUrl:"https://www.youtube.com/results?search_query=How%20Wind%20and%20Water%20Change%20the%20Land%3A%20Erosion%20grade%202%20educational",
   quiz:[
     {q:"What do we call it when wind and water slowly wear away rock and soil?", options:["Hibernation","Erosion","Migration","Pollination"], answer:1},
     {q:"Which of these can cause erosion?", options:["Sunlight only","Silence","Wind and water","Colours"], answer:2},
     {q:"Erosion usually happens ___.", options:["In one single second","Only in cities","Only during the night","Slowly, over a long period of time"], answer:3},
     {q:"Which of these landforms could be shaped by water erosion over time?", options:["A library","A parking lot","A river canyon","A classroom"], answer:2},
     {q:"Planting trees and grass can help reduce erosion because roots ___.", options:["Attract more wind","Hold soil in place","Stop rain completely","Make rocks heavier"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call it when wind and water slowly wear away rock and soil?", answers:["erosion"]},
     {prompt:"Name one force of nature that can cause erosion, like wind or water.", answers:["wind","water"]},
     {prompt:"Does erosion happen quickly or slowly, over a long time?", answers:["slowly","over a long time"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Sports and Pastimes", summary:"Students learn about sports and pastimes enjoyed across Canada, such as hockey, lacrosse, skating, and camping, and how they reflect Canadian culture and geography.",
   resourceLabel:"YouTube: Canadian Sports and Pastimes", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Sports%20and%20Pastimes%20grade%202%20educational",
   quiz:[
     {q:"Which sport is widely played and watched across Canada, especially in winter?", options:["Sumo wrestling","Bullfighting","Hockey","Surfing"], answer:2},
     {q:"Which sport, often called the national summer sport of Canada, uses a small rubber ball and a net on a long stick?", options:["Lacrosse","Cricket","Basketball","Golf"], answer:0},
     {q:"Why might winter sports like hockey and skating be popular in many parts of Canada?", options:["Because it never snows in Canada","Because Canada has no winter season","Because winters are cold with lots of snow and ice","Because ice never forms in Canada"], answer:2},
     {q:"Which of these is an outdoor pastime many Canadians enjoy in the summer?", options:["Camping","Ice fishing","Tobogganing","Building snow forts"], answer:0},
     {q:"Sports and pastimes in a country can reflect its ___.", options:["Only its currency","Only its government","Culture, climate, and geography","Only its population size"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one sport that is popular in Canada, like hockey or lacrosse.", answers:["hockey","lacrosse"]},
     {prompt:"Which Canadian sport is often played on ice?", answers:["hockey"]},
     {prompt:"Name one outdoor pastime enjoyed in Canada, like camping or skating.", answers:["camping","skating"]}
   ]},
]},
{day:56, label:"Day 56 — Mon", subjects:[
  {subject:"Language", title:"Text Features: Titles, Headings, and Captions", summary:"Students learn that text features such as titles, headings, and captions help readers find information and understand what a section of text is about.",
   resourceLabel:"YouTube: Text Features: Titles, Headings, and Captions", resourceUrl:"https://www.youtube.com/results?search_query=Text%20Features%3A%20Titles%2C%20Headings%2C%20and%20Captions%20grade%202%20educational",
   quiz:[
     {q:"What do we call the words at the top of a book that tell what it is about?", options:["A title","A glossary","A footnote","A caption"], answer:0},
     {q:"What do we call a short label under a picture that explains what it shows?", options:["A title","A heading","A caption","A table of contents"], answer:2},
     {q:"What do we call a word or phrase that introduces a new section in a text?", options:["A footnote","An index","A caption","A heading"], answer:3},
     {q:"Why are text features like titles and headings helpful to readers?", options:["They remove all pictures","They make books heavier","They make reading impossible","They help readers find information quickly"], answer:3},
     {q:"Which of these is an example of a text feature?", options:["A heading","A verb","A syllable","A vowel"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the words at the top of a book or chapter that tell what it is about?", answers:["a title","title"]},
     {prompt:"What do we call a short label under a picture that explains what it shows?", answers:["a caption","caption"]},
     {prompt:"What do we call a word or phrase that introduces a new section of text?", answers:["a heading","heading"]}
   ]},
  {subject:"Math", title:"Measuring Capacity with Litres and Millilitres", summary:"Students learn that capacity, or how much liquid a container can hold, can be measured using millilitres for small amounts and litres for larger amounts.",
   resourceLabel:"YouTube: Measuring Capacity with Litres and Millilitres", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Capacity%20with%20Litres%20and%20Millilitres%20grade%202%20educational",
   quiz:[
     {q:"What unit would you most likely use to measure a small spoonful of liquid?", options:["Metres","Millilitres","Kilograms","Litres"], answer:1},
     {q:"What unit would you most likely use to measure the water in a bathtub?", options:["Millilitres","Litres","Grams","Centimetres"], answer:1},
     {q:"Which holds more liquid, 1 litre or 1 millilitre?", options:["1 millilitre","They are equal","Cannot tell","1 litre"], answer:3},
     {q:"What do we call the amount of liquid a container can hold?", options:["Mass","Area","Capacity","Perimeter"], answer:2},
     {q:"A large water bottle would most likely be measured in ___.", options:["Metres","Litres","Kilograms","Degrees"], answer:1}
   ],
   worksheet:[
     {prompt:"What unit would you use to measure a small amount of liquid, like in a spoon?", answers:["millilitres","millilitre"]},
     {prompt:"What unit would you use to measure a large amount of liquid, like in a bathtub?", answers:["litres","litre"]},
     {prompt:"Which holds more liquid, 1 litre or 1 millilitre?", answers:["1 litre","litre"]}
   ]},
  {subject:"Science", title:"Static Electricity: Why Balloons Stick to Walls", summary:"Students learn that static electricity happens when tiny charges build up on an object, such as a balloon rubbed on hair, causing it to stick to a wall or attract small bits of paper.",
   resourceLabel:"YouTube: Static Electricity: Why Balloons Stick to Walls", resourceUrl:"https://www.youtube.com/results?search_query=Static%20Electricity%3A%20Why%20Balloons%20Stick%20to%20Walls%20grade%202%20educational",
   quiz:[
     {q:"What kind of electricity builds up when you rub a balloon on your hair?", options:["Solar electricity","Circuit electricity","Wind electricity","Static electricity"], answer:3},
     {q:"After rubbing a balloon on your hair, what might the balloon do?", options:["Stick to a wall","Freeze","Turn into a solid","Melt"], answer:0},
     {q:"What can happen when you rub a balloon on hair and then hold it near small bits of paper?", options:["Nothing happens at all","The paper turns into water","The paper disappears","The paper is attracted to the balloon"], answer:3},
     {q:"Static electricity is different from the electricity in a simple circuit because static electricity ___.", options:["Never happens outdoors","Builds up charges that are not flowing in a loop","Always needs a battery","Only comes from the sun"], answer:1},
     {q:"Rubbing certain materials together can cause tiny charges to ___.", options:["Turn into heat only","Disappear completely","Build up on their surfaces","Turn into light only"], answer:2}
   ],
   worksheet:[
     {prompt:"What kind of electricity builds up when you rub a balloon on your hair?", answers:["static electricity","static"]},
     {prompt:"What can a balloon with static electricity stick to, like a wall?", answers:["a wall","wall"]},
     {prompt:"Name one small object that a balloon with static electricity might attract, like bits of paper.", answers:["bits of paper","paper","small pieces of paper"]}
   ]},
  {subject:"SocialStudies", title:"Why People Settle Near Water and Resources", summary:"Students learn that communities often grow near lakes, rivers, and other resources because water and resources provide food, transportation, and materials people need.",
   resourceLabel:"YouTube: Why People Settle Near Water and Resources", resourceUrl:"https://www.youtube.com/results?search_query=Why%20People%20Settle%20Near%20Water%20and%20Resources%20grade%202%20educational",
   quiz:[
     {q:"Why do many communities grow near lakes and rivers?", options:["Water and resources are easier to access there","Water is never useful to communities","Rivers make land colder","Lakes make travel impossible"], answer:0},
     {q:"Which of these is a reason people might settle near water?", options:["Water stops all travel","Water makes land disappear","Water removes all resources","Water for drinking, farming, and transportation"], answer:3},
     {q:"Which of these resources might attract people to build a community nearby?", options:["Empty air only","Fertile farmland and fresh water","A place with no water","A place with no resources"], answer:1},
     {q:"Rivers can help communities by providing a route for ___.", options:["Only swimming","Transportation and trade","Only fishing tournaments","Only boating races"], answer:1},
     {q:"Studying why communities settle in certain places helps us understand ___.", options:["How to build a car","How to play music","How to bake bread","How geography and resources shape where people live"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one resource that might make people want to build a community nearby, like water.", answers:["water","fresh water","fertile land","trees"]},
     {prompt:"Why might people build communities near rivers or lakes?", answers:["for water","for transportation","for water and transportation"]},
     {prompt:"Name one thing water provides for a community, like transportation or drinking water.", answers:["transportation","drinking water","water for farming"]}
   ]},
]},
{day:57, label:"Day 57 — Tue", subjects:[
  {subject:"Language", title:"Purpose for Writing: Inform, Entertain, or Persuade", summary:"Students learn that writers have a purpose for writing, such as to inform readers with facts, to entertain readers with a fun story, or to persuade readers to agree with an idea.",
   resourceLabel:"YouTube: Purpose for Writing: Inform, Entertain, or Persuade", resourceUrl:"https://www.youtube.com/results?search_query=Purpose%20for%20Writing%3A%20Inform%2C%20Entertain%2C%20or%20Persuade%20grade%202%20educational",
   quiz:[
     {q:"What is the purpose of writing that gives readers facts and information?", options:["To entertain","To inform","To rhyme","To persuade"], answer:1},
     {q:"What is the purpose of writing a funny story or an adventure tale?", options:["To entertain","To persuade","To measure","To inform"], answer:0},
     {q:"What is the purpose of writing that tries to convince readers to agree with an idea?", options:["To persuade","To inform","To entertain","To describe only colours"], answer:0},
     {q:"A weather report that shares facts about the weather tomorrow is meant to ___.", options:["Entertain","Persuade","Inform","Confuse"], answer:2},
     {q:"A poster that says, recycle to help our planet, is trying to ___.", options:["Only entertain readers","Confuse the reader","Persuade readers to take action","Only inform readers with numbers"], answer:2}
   ],
   worksheet:[
     {prompt:"What is the purpose of writing when the goal is to give readers facts?", answers:["to inform","inform"]},
     {prompt:"What is the purpose of writing when the goal is to make readers laugh or enjoy a story?", answers:["to entertain","entertain"]},
     {prompt:"What is the purpose of writing when the goal is to convince readers to agree with an idea?", answers:["to persuade","persuade"]}
   ]},
  {subject:"Math", title:"Comparing Money Amounts and Making Combinations", summary:"Students learn to compare different amounts of money to see which is greater, and to find different combinations of coins that add up to the same amount.",
   resourceLabel:"YouTube: Comparing Money Amounts and Making Combinations", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Money%20Amounts%20and%20Making%20Combinations%20grade%202%20educational",
   quiz:[
     {q:"Which is worth more, 3 quarters or 2 dimes?", options:["Cannot tell","They are equal","2 dimes","3 quarters"], answer:3},
     {q:"Which combination of coins adds up to 15 cents?", options:["A dime and a nickel","One nickel","Two quarters","Three dimes"], answer:0},
     {q:"How many cents is 1 quarter worth?", options:["10 cents","1 cent","25 cents","5 cents"], answer:2},
     {q:"Which amount of money is greater, 45 cents or 4 dimes?", options:["They are equal","45 cents","Cannot tell","4 dimes"], answer:1},
     {q:"Comparing money amounts helps us know ___.", options:["How to measure length","How to weigh objects","How to tell time","Which amount is worth more or less"], answer:3}
   ],
   worksheet:[
     {prompt:"Which is worth more, 3 quarters or 2 dimes?", answers:["3 quarters","three quarters"]},
     {prompt:"Name two coins that could add up to 15 cents.", answers:["a dime and a nickel","dime and nickel"]},
     {prompt:"If you have 1 quarter, how many cents do you have?", answers:["25","25 cents"]}
   ]},
  {subject:"Science", title:"Protecting Endangered Animals", summary:"Students learn that an endangered animal is one that is at risk of disappearing forever, and that people can help protect these animals by preserving habitats and reducing pollution.",
   resourceLabel:"YouTube: Protecting Endangered Animals", resourceUrl:"https://www.youtube.com/results?search_query=Protecting%20Endangered%20Animals%20grade%202%20educational",
   quiz:[
     {q:"What word describes an animal that is at risk of disappearing forever?", options:["Domestic","Migratory","Nocturnal","Endangered"], answer:3},
     {q:"Which of these can help protect endangered animals?", options:["Cutting down more forests","Ignoring the problem","Increasing pollution","Preserving their habitats"], answer:3},
     {q:"Which of these is an example of an endangered animal?", options:["A pet goldfish","A giant panda","A farm cow","A house cat"], answer:1},
     {q:"Why might an animal become endangered?", options:["Eating too much food","Losing its habitat or being hunted too much","Having too many babies","Living too long"], answer:1},
     {q:"Protecting endangered animals is important because ___.", options:["It makes habitats disappear faster","It has no effect on nature","It only helps people, not animals","It helps keep nature balanced and healthy for the future"], answer:3}
   ],
   worksheet:[
     {prompt:"What word describes an animal that is at risk of disappearing forever?", answers:["endangered"]},
     {prompt:"Name one way people can help protect endangered animals, like preserving habitats.", answers:["preserving habitats","protecting habitats","reducing pollution"]},
     {prompt:"Name one endangered animal, like a panda or a sea turtle.", answers:["a panda","panda","a sea turtle","sea turtle"]}
   ]},
  {subject:"SocialStudies", title:"History of Money: From Trading to Coins", summary:"Students learn that before coins and bills existed, people traded goods directly, called bartering, and over time societies developed coins and paper money to make trading easier.",
   resourceLabel:"YouTube: History of Money: From Trading to Coins", resourceUrl:"https://www.youtube.com/results?search_query=History%20of%20Money%3A%20From%20Trading%20to%20Coins%20grade%202%20educational",
   quiz:[
     {q:"What do we call it when people trade goods directly without using money?", options:["Borrowing","Bartering","Saving","Investing"], answer:1},
     {q:"Before coins and paper money existed, how did people usually get the things they needed?", options:["By using the internet","By using credit cards","By trading goods directly with each other","By using cheques"], answer:2},
     {q:"Why did societies eventually begin using coins instead of only trading goods?", options:["Coins made trading easier and fairer","Coins made trading impossible","Coins were heavier than goods","Coins removed the need for goods"], answer:0},
     {q:"What were some of the first types of money often made from?", options:["Plastic cards","Wood only","Metal, shaped into coins","Paper only"], answer:2},
     {q:"Learning about the history of money helps us understand ___.", options:["How to read a map","How to grow crops","How to build houses","How trading and money have changed over time"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call it when people trade goods directly without using money?", answers:["bartering","trading goods"]},
     {prompt:"What did people use before coins and paper money existed?", answers:["bartering","trading goods","trading"]},
     {prompt:"Why did societies eventually start using coins instead of only bartering?", answers:["to make trading easier","easier trading"]}
   ]},
]},
{day:58, label:"Day 58 — Wed", subjects:[
  {subject:"Language", title:"Story Theme: The Lesson Behind a Story", summary:"Students learn that a theme is the main lesson or message of a story, often about kindness, honesty, or working hard, that readers can apply to their own lives.",
   resourceLabel:"YouTube: Story Theme: The Lesson Behind a Story", resourceUrl:"https://www.youtube.com/results?search_query=Story%20Theme%3A%20The%20Lesson%20Behind%20a%20Story%20grade%202%20educational",
   quiz:[
     {q:"What do we call the main lesson or message of a story?", options:["Theme","Setting","Character","Caption"], answer:0},
     {q:"Which of these is a common theme found in stories?", options:["The book title only","The exact page number","The font used","Kindness matters"], answer:3},
     {q:"How is theme different from plot?", options:["Theme and plot are the same thing","Plot is the lesson, theme is the setting","Theme is only a picture","Theme is the lesson, plot is the sequence of events"], answer:3},
     {q:"In a story where a slow turtle wins a race by trying hard, a likely theme is ___.", options:["Fast animals always win","Racing is dangerous","Hard work and patience can lead to success","Turtles cannot move"], answer:2},
     {q:"Finding the theme of a story helps readers ___.", options:["Skip the ending","Avoid thinking about the story","Understand a lesson they can apply to their own lives","Forget the story quickly"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the main lesson or message of a story?", answers:["theme","the theme"]},
     {prompt:"Name one common story theme, like kindness or honesty.", answers:["kindness","honesty","hard work","friendship"]},
     {prompt:"How is a theme different from the plot of a story?", answers:["theme is the lesson","theme is the message, plot is what happens"]}
   ]},
  {subject:"Math", title:"Sorting 3D Objects by Attributes", summary:"Students learn to sort three-dimensional objects, such as cubes, spheres, cones, and cylinders, by attributes like the number of faces, edges, and whether they can roll.",
   resourceLabel:"YouTube: Sorting 3D Objects by Attributes", resourceUrl:"https://www.youtube.com/results?search_query=Sorting%203D%20Objects%20by%20Attributes%20grade%202%20educational",
   quiz:[
     {q:"Which 3D shape looks like a ball and can roll in any direction?", options:["Sphere","Cylinder","Cube","Cone"], answer:0},
     {q:"Which 3D shape has six flat square faces?", options:["Sphere","Cone","Cube","Cylinder"], answer:2},
     {q:"Which 3D shape has one flat circular face and one pointed tip?", options:["Cone","Cube","Cylinder","Sphere"], answer:0},
     {q:"Which 3D shape has two flat circular faces and one curved surface, like a can?", options:["Cone","Cube","Cylinder","Sphere"], answer:2},
     {q:"When sorting 3D shapes, we can group them by ___.", options:["The number of faces, edges, and whether they roll","Their name only","Their colour only","Their smell"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one three-dimensional shape, like a cube or a sphere.", answers:["a cube","cube","a sphere","sphere","a cone","cone","a cylinder","cylinder"]},
     {prompt:"Which 3D shape looks like a ball and can roll in any direction?", answers:["a sphere","sphere"]},
     {prompt:"Which 3D shape has six flat square faces?", answers:["a cube","cube"]}
   ]},
  {subject:"Science", title:"Taking Care of Your Teeth", summary:"Students learn healthy habits for taking care of their teeth, such as brushing twice a day, flossing, and visiting the dentist for checkups.",
   resourceLabel:"YouTube: Taking Care of Your Teeth", resourceUrl:"https://www.youtube.com/results?search_query=Taking%20Care%20of%20Your%20Teeth%20grade%202%20educational",
   quiz:[
     {q:"How many times a day should you usually brush your teeth?", options:["Once a week","Twice","Never","Ten times"], answer:1},
     {q:"What tool is used to clean between your teeth?", options:["A hammer","A ruler","Floss","A thermometer"], answer:2},
     {q:"Who should you visit for regular teeth checkups?", options:["A dentist","A farmer","A firefighter","A librarian"], answer:0},
     {q:"Which of these foods can help keep teeth healthy?", options:["Sugary candy","Sugary soda","Fruits and vegetables","Sticky sweets"], answer:2},
     {q:"Taking care of your teeth is important because it helps ___.", options:["Prevent cavities and keep teeth healthy","Stop you from smiling","Make teeth fall out faster","Make food taste worse"], answer:0}
   ],
   worksheet:[
     {prompt:"How many times a day should you usually brush your teeth?", answers:["twice","two times","2"]},
     {prompt:"Name one tool used to clean between your teeth, like floss.", answers:["floss"]},
     {prompt:"Who should you visit for regular teeth checkups?", answers:["a dentist","dentist"]}
   ]},
  {subject:"SocialStudies", title:"Community Recreation: Parks, Rinks, and Playgrounds", summary:"Students learn that communities build recreation spaces, such as parks, skating rinks, and playgrounds, so people can exercise, play, and spend time together.",
   resourceLabel:"YouTube: Community Recreation: Parks, Rinks, and Playgrounds", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Recreation%3A%20Parks%2C%20Rinks%2C%20and%20Playgrounds%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of a community recreation space?", options:["A park","A bank","A hospital","A factory"], answer:0},
     {q:"Why do communities build recreation spaces like parks and playgrounds?", options:["To store extra food","To park cars only","So people can exercise, play, and spend time together","So no one can go outside"], answer:2},
     {q:"Which recreation space would most likely have ice for skating in winter?", options:["A skating rink","A library","A grocery store","A bakery"], answer:0},
     {q:"Which of these activities might happen at a community playground?", options:["Firefighters putting out fires","Children playing on swings and slides","Farmers growing crops","Doctors performing surgery"], answer:1},
     {q:"Community recreation spaces help people by ___.", options:["Removing all green spaces","Giving them places to be active and connect with others","Keeping everyone indoors","Making communities more crowded with buildings only"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one recreation space found in many communities, like a park or a playground.", answers:["a park","park","a playground","playground","a rink","rink"]},
     {prompt:"Why do communities build recreation spaces like parks and playgrounds?", answers:["so people can play and exercise","for exercise and fun","so people can spend time together"]},
     {prompt:"Name one activity people might do at a community park.", answers:["playing","exercising","picnicking","walking"]}
   ]},
]},
{day:59, label:"Day 59 — Thu", subjects:[
  {subject:"Language", title:"Writing a Friendly Letter", summary:"Students learn the parts of a friendly letter, including the greeting, body, closing, and signature, used to write a personal message to someone.",
   resourceLabel:"YouTube: Writing a Friendly Letter", resourceUrl:"https://www.youtube.com/results?search_query=Writing%20a%20Friendly%20Letter%20grade%202%20educational",
   quiz:[
     {q:"What part of a friendly letter greets the person you are writing to?", options:["The greeting","The closing","The signature only","The body"], answer:0},
     {q:"What part of a friendly letter contains the main message?", options:["The date only","The body","The closing","The greeting"], answer:1},
     {q:"Which of these is an example of a greeting in a friendly letter?", options:["Once upon a time.","Your friend,","Dear Sam,","The end."], answer:2},
     {q:"Which of these is an example of a closing in a friendly letter?", options:["The Title","Chapter One","Your friend,","Dear Sam,"], answer:2},
     {q:"A friendly letter is most often written to ___.", options:["Share a personal message with someone you know","List math problems","Explain science facts only","Give a weather report"], answer:0}
   ],
   worksheet:[
     {prompt:"What part of a friendly letter greets the person you are writing to, like Dear Sam?", answers:["the greeting","greeting"]},
     {prompt:"What part of a friendly letter contains the main message?", answers:["the body","body"]},
     {prompt:"What part of a friendly letter comes at the end, like Your friend, before your name?", answers:["the closing","closing"]}
   ]},
  {subject:"Math", title:"Finding the Mode in a Data Set", summary:"Students learn that the mode of a data set is the number or item that appears most often, helping to summarize information collected in a survey or chart.",
   resourceLabel:"YouTube: Finding the Mode in a Data Set", resourceUrl:"https://www.youtube.com/results?search_query=Finding%20the%20Mode%20in%20a%20Data%20Set%20grade%202%20educational",
   quiz:[
     {q:"What do we call the number or item that appears most often in a data set?", options:["Mode","Fraction","Area","Perimeter"], answer:0},
     {q:"In the data set 2, 3, 3, 5, 3, what number appears most often?", options:["4","2","5","3"], answer:3},
     {q:"If most classmates in a survey picked red as their favourite colour, what is the mode?", options:["Yellow","Green","Red","Blue"], answer:2},
     {q:"In the data set 7, 7, 8, 9, 9, 9, what is the mode?", options:["7","9","There is no mode","8"], answer:1},
     {q:"Finding the mode of a data set helps us know ___.", options:["How long something is","What time it is","Which item or number appears most often","How much something weighs"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the number or item that appears most often in a data set?", answers:["mode","the mode"]},
     {prompt:"In the data set 2, 3, 3, 5, 3, what number appears most often?", answers:["3","three"]},
     {prompt:"If most classmates picked red as their favourite colour, what is the mode of that survey?", answers:["red"]}
   ]},
  {subject:"Science", title:"Where Energy Comes From: Sun, Wind, and Water", summary:"Students learn that energy can come from natural sources such as the sun, wind, and moving water, which can be used to create electricity and power homes.",
   resourceLabel:"YouTube: Where Energy Comes From: Sun, Wind, and Water", resourceUrl:"https://www.youtube.com/results?search_query=Where%20Energy%20Comes%20From%3A%20Sun%2C%20Wind%2C%20and%20Water%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a natural source of energy?", options:["A rubber ball","A cardboard box","The sun","A plastic bag"], answer:2},
     {q:"What do we call panels that capture energy from sunlight?", options:["Water wheels","Batteries only","Wind turbines","Solar panels"], answer:3},
     {q:"Which machine uses wind to create energy?", options:["A solar panel","A wind turbine","A battery","A dam"], answer:1},
     {q:"Moving water, like a river through a dam, can be used to create ___.", options:["Wind","Soil","Sunlight","Electricity"], answer:3},
     {q:"Using natural sources like sun, wind, and water for energy is helpful because they ___.", options:["Disappear after one use","Can be used again and again without running out","Cannot power anything","Always cause pollution"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one natural source of energy, like the sun or wind.", answers:["the sun","sun","wind","water"]},
     {prompt:"What do we call panels that capture energy from the sun?", answers:["solar panels"]},
     {prompt:"Name one machine that uses wind to create energy, like a wind turbine.", answers:["a wind turbine","wind turbine"]}
   ]},
  {subject:"SocialStudies", title:"Museums and Historical Sites: Learning About the Past", summary:"Students learn that museums and historical sites help people learn about the past by displaying old objects, artifacts, and stories from earlier times.",
   resourceLabel:"YouTube: Museums and Historical Sites: Learning About the Past", resourceUrl:"https://www.youtube.com/results?search_query=Museums%20and%20Historical%20Sites%3A%20Learning%20About%20the%20Past%20grade%202%20educational",
   quiz:[
     {q:"What do we call a place that displays old objects and artifacts for people to learn from?", options:["A museum","A bank","A farm","A factory"], answer:0},
     {q:"What do we call an old object that helps us learn about people from the past?", options:["A recipe","A map only","A calendar","An artifact"], answer:3},
     {q:"Why might a class visit a historical site on a field trip?", options:["To buy groceries","To learn about important events from the past","To play sports","To watch a movie"], answer:1},
     {q:"Which of these might you find displayed inside a museum?", options:["Old tools and artifacts","Restaurant menus","Fresh vegetables","New cars for sale"], answer:0},
     {q:"Museums and historical sites help communities by ___.", options:["Hiding artifacts from everyone","Preserving and sharing stories from the past","Selling old objects only","Erasing history completely"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call a place that displays old objects and artifacts for people to learn from?", answers:["a museum","museum"]},
     {prompt:"What do we call an old object that helps us learn about the past, like an old tool?", answers:["an artifact","artifact"]},
     {prompt:"Name one reason people visit museums, like to learn about history.", answers:["to learn about history","to learn about the past"]}
   ]},
]},
{day:60, label:"Day 60 — Fri", subjects:[
  {subject:"Language", title:"Final Review: Language Skills (Days 51-59)", summary:"Students review Language skills from Days 51 to 59: past tense verbs, capitalization, multiple-meaning words, context clues, onomatopoeia, text features, purpose for writing, story theme, and friendly letters.",
   resourceLabel:"YouTube: Final Review: Language Skills (Days 51-59)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Language%20Skills%20%28Days%2051-59%29%20grade%202%20educational",
   quiz:[
     {q:"What ending do we usually add to a verb to show something already happened?", options:["-ing","-er","-ed","-est"], answer:2},
     {q:"What kind of letter starts the name of a person, like Sarah?", options:["A number","A capital letter","A silent letter","A lowercase letter"], answer:1},
     {q:"What do we call the words and sentences around an unfamiliar word that help us understand its meaning?", options:["Compound words","Context clues","Silent letters","Rhyming words"], answer:1},
     {q:"What is the purpose of writing that gives readers facts and information?", options:["To entertain","To persuade","To inform","To rhyme"], answer:2},
     {q:"What part of a friendly letter contains the main message?", options:["The greeting","The body","The closing","The date only"], answer:1}
   ],
   worksheet:[
     {prompt:"What is the past tense of the verb jump?", answers:["jumped"]},
     {prompt:"What do we call a word that has more than one meaning?", answers:["a multiple-meaning word","multiple-meaning word"]},
     {prompt:"What do we call the main lesson or message of a story?", answers:["theme","the theme"]}
   ]},
  {subject:"Math", title:"Final Review: Math Skills (Days 51-59)", summary:"Students review Math skills from Days 51 to 59: skip counting by 3s and 4s, division, probability, number lines, measuring mass and capacity, comparing money, sorting 3D objects, and finding the mode.",
   resourceLabel:"YouTube: Final Review: Math Skills (Days 51-59)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Math%20Skills%20%28Days%2051-59%29%20grade%202%20educational",
   quiz:[
     {q:"Skip count by 4s: 4, 8, 12, ___", options:["14","16","15","20"], answer:1},
     {q:"If you share 12 apples equally among 3 friends, how many apples does each friend get?", options:["6","4","3","12"], answer:1},
     {q:"Is it likely or unlikely that it will snow in Ontario in July?", options:["Certain","Impossible","Likely","Unlikely"], answer:3},
     {q:"What unit would you most likely use to measure the water in a bathtub?", options:["Centimetres","Litres","Millilitres","Grams"], answer:1},
     {q:"Which 3D shape has six flat square faces?", options:["Cube","Sphere","Cylinder","Cone"], answer:0}
   ],
   worksheet:[
     {prompt:"Skip count by 3s: 3, 6, 9, ___", answers:["12","twelve"]},
     {prompt:"What do we call splitting a group of objects equally into smaller groups?", answers:["division","sharing equally"]},
     {prompt:"What do we call the number or item that appears most often in a data set?", answers:["mode","the mode"]}
   ]},
  {subject:"Science", title:"Final Review: Science Skills (Days 51-59)", summary:"Students review Science topics from Days 51 to 59: animal camouflage, butterfly metamorphosis, bones and muscles, moon phases, erosion, static electricity, endangered animals, dental care, and energy sources.",
   resourceLabel:"YouTube: Final Review: Science Skills (Days 51-59)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Science%20Skills%20%28Days%2051-59%29%20grade%202%20educational",
   quiz:[
     {q:"Why might an animal use camouflage?", options:["To hide from predators or sneak up on prey","To make more noise","To fly faster","To change the weather"], answer:0},
     {q:"What do we call the stage where a caterpillar forms a hard case and changes shape?", options:["Nest","Web","Burrow","Chrysalis"], answer:3},
     {q:"What do we call it when wind and water slowly wear away rock and soil?", options:["Pollination","Migration","Erosion","Hibernation"], answer:2},
     {q:"What kind of electricity builds up when you rub a balloon on your hair?", options:["Static electricity","Circuit electricity","Wind electricity","Solar electricity"], answer:0},
     {q:"Which of these is a natural source of energy?", options:["A cardboard box","A rubber ball","The sun","A plastic bag"], answer:2}
   ],
   worksheet:[
     {prompt:"What word describes an animal blending into its surroundings using color or pattern?", answers:["camouflage"]},
     {prompt:"What do we call the changing shapes of the moon that we see in the sky?", answers:["phases of the moon","moon phases"]},
     {prompt:"What word describes an animal that is at risk of disappearing forever?", answers:["endangered"]}
   ]},
  {subject:"SocialStudies", title:"Final Review: Social Studies Skills (Days 51-59)", summary:"Students review Social Studies topics from Days 51 to 59: notable Canadians, Canadian inventions, water systems, homes around the world, Canadian sports, settlement patterns, the history of money, community recreation, and museums.",
   resourceLabel:"YouTube: Final Review: Social Studies Skills (Days 51-59)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Social%20Studies%20Skills%20%28Days%2051-59%29%20grade%202%20educational",
   quiz:[
     {q:"Which sport was invented by a Canadian named James Naismith?", options:["Soccer","Baseball","Tennis","Basketball"], answer:3},
     {q:"How does clean water usually travel from a treatment plant to our homes?", options:["By truck only","By boat only","Through underground pipes","By airplane"], answer:2},
     {q:"Which sport is widely played and watched across Canada, especially in winter?", options:["Surfing","Bullfighting","Hockey","Sumo wrestling"], answer:2},
     {q:"Why did societies eventually begin using coins instead of only trading goods?", options:["Coins removed the need for goods","Coins were heavier than goods","Coins made trading easier and fairer","Coins made trading impossible"], answer:2},
     {q:"Why might a class visit a historical site on a field trip?", options:["To watch a movie","To play sports","To learn about important events from the past","To buy groceries"], answer:2}
   ],
   worksheet:[
     {prompt:"What word describes a person who is well known for an important contribution?", answers:["notable","famous"]},
     {prompt:"What do we call a place that cleans water before it reaches our homes?", answers:["a treatment plant","treatment plant","water treatment plant"]},
     {prompt:"What do we call a place that displays old objects and artifacts for people to learn from?", answers:["a museum","museum"]}
   ]},
]},
{day:61, label:"Day 61 — Mon", subjects:[
  {subject:"Language", title:"Irregular Past Tense Verbs", summary:"Students learn that some verbs do not add -ed to show the past tense but change into a new word instead, such as go becoming went, run becoming ran, and see becoming saw.",
   resourceLabel:"YouTube: Irregular Past Tense Verbs", resourceUrl:"https://www.youtube.com/results?search_query=Irregular%20Past%20Tense%20Verbs%20grade%202%20educational",
   quiz:[
     {q:"What is the past tense of the verb go?", options:["Goed","Went","Going","Goes"], answer:1},
     {q:"What is the past tense of the verb run?", options:["Runned","Runs","Ran","Running"], answer:2},
     {q:"What is the past tense of the verb see?", options:["Saw","Sees","Seeing","Seed"], answer:0},
     {q:"Which sentence uses the correct irregular past tense of eat?", options:["Yesterday I eated breakfast.","Yesterday I eating breakfast.","Yesterday I eat breakfast.","Yesterday I ate breakfast."], answer:3},
     {q:"Irregular past tense verbs are different from regular past tense verbs because they ___.", options:["Always add -ing at the end","Change into a whole new word instead of adding -ed","Always add -ed at the end","Never change at all"], answer:1}
   ],
   worksheet:[
     {prompt:"What is the past tense of the verb go?", answers:["went"]},
     {prompt:"What is the past tense of the verb run?", answers:["ran"]},
     {prompt:"What is the past tense of the verb see?", answers:["saw"]}
   ]},
  {subject:"Math", title:"Understanding Hundreds: Place Value to 1000", summary:"Students learn that three-digit numbers are made up of hundreds, tens, and ones, and practice breaking numbers like 342 into 3 hundreds, 4 tens, and 2 ones.",
   resourceLabel:"YouTube: Understanding Hundreds: Place Value to 1000", resourceUrl:"https://www.youtube.com/results?search_query=Understanding%20Hundreds%3A%20Place%20Value%20to%201000%20grade%202%20educational",
   quiz:[
     {q:"How many hundreds are in the number 342?", options:["2","4","7","3"], answer:3},
     {q:"How many tens are in the number 156?", options:["7","1","6","5"], answer:3},
     {q:"What is the value of the 7 in the number 273?", options:["700","270","70","7"], answer:2},
     {q:"Which number has 5 hundreds, 2 tens, and 8 ones?", options:["285","852","258","528"], answer:3},
     {q:"Place value helps us understand ___.", options:["The shape of a number","The colour of a number","The sound of a number","What each digit in a number is worth"], answer:3}
   ],
   worksheet:[
     {prompt:"How many hundreds are in the number 342?", answers:["3","three"]},
     {prompt:"How many tens are in the number 342?", answers:["4","four"]},
     {prompt:"How many ones are in the number 342?", answers:["2","two"]}
   ]},
  {subject:"Science", title:"Life Cycle of a Frog: From Tadpole to Frog", summary:"Students learn the life cycle of a frog, which begins as an egg in water, hatches into a swimming tadpole, grows legs, and changes into an adult frog that can live on land and in water.",
   resourceLabel:"YouTube: Life Cycle of a Frog: From Tadpole to Frog", resourceUrl:"https://www.youtube.com/results?search_query=Life%20Cycle%20of%20a%20Frog%3A%20From%20Tadpole%20to%20Frog%20grade%202%20educational",
   quiz:[
     {q:"What is the first stage of a frog life cycle?", options:["Froglet","Adult frog","Tadpole","Egg"], answer:3},
     {q:"What do we call a young frog that swims using a tail before it grows legs?", options:["A chick","A caterpillar","A cub","A tadpole"], answer:3},
     {q:"Where does a frog usually lay its eggs?", options:["In a nest in a tree","On a rock in the desert","In water","Underground"], answer:2},
     {q:"Put the frog life cycle stages in the correct order.", options:["Froglet, egg, tadpole, adult frog","Adult frog, egg, froglet, tadpole","Tadpole, adult frog, egg, froglet","Egg, tadpole, froglet, adult frog"], answer:3},
     {q:"As a tadpole grows into a frog, it ___.", options:["Turns into a fish permanently","Grows legs and loses its tail","Grows a shell and stops moving","Grows wings and flies away"], answer:1}
   ],
   worksheet:[
     {prompt:"What is the first stage of a frog life cycle?", answers:["egg","an egg"]},
     {prompt:"What do we call a young frog that swims and breathes with gills before it grows legs?", answers:["a tadpole","tadpole"]},
     {prompt:"Where does a frog lay its eggs?", answers:["in water","water"]}
   ]},
  {subject:"SocialStudies", title:"Local Businesses: Meeting Our Community Needs", summary:"Students learn that local businesses, such as bakeries, grocery stores, and repair shops, provide goods and services that help meet the needs of people living in a community.",
   resourceLabel:"YouTube: Local Businesses: Meeting Our Community Needs", resourceUrl:"https://www.youtube.com/results?search_query=Local%20Businesses%3A%20Meeting%20Our%20Community%20Needs%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of a local business?", options:["A bakery","A cloud","A mountain","A river"], answer:0},
     {q:"What do local businesses provide to the people in a community?", options:["Only entertainment","Only maps","Goods and services people need","Only weather reports"], answer:2},
     {q:"Why might a family visit a local grocery store?", options:["To mail a letter","To play a sport","To watch a movie","To buy food and other items they need"], answer:3},
     {q:"A shoe repair shop is an example of a business that provides a ___.", options:["Service","Type of food","Type of weather","Type of animal"], answer:0},
     {q:"Local businesses help a community by ___.", options:["Making it harder to find food","Removing all jobs from a community","Providing jobs and things people need nearby","Taking away community services"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one local business found in many communities, like a bakery or a grocery store.", answers:["a bakery","bakery","a grocery store","grocery store"]},
     {prompt:"What do we call the goods and services a business provides to help people?", answers:["goods and services","things people need"]},
     {prompt:"Why are local businesses important to a community?", answers:["they provide goods and services","they help meet needs","they help people get what they need"]}
   ]},
]},
{day:62, label:"Day 62 — Tue", subjects:[
  {subject:"Language", title:"Sentence Fragments vs Complete Sentences", summary:"Students learn that a complete sentence has a subject and a verb and expresses a full thought, while a sentence fragment is missing a part and does not express a complete thought.",
   resourceLabel:"YouTube: Sentence Fragments vs Complete Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Sentence%20Fragments%20vs%20Complete%20Sentences%20grade%202%20educational",
   quiz:[
     {q:"What two parts does a complete sentence need?", options:["A subject and a verb","Only a noun","Only a question mark","Only a capital letter"], answer:0},
     {q:"Which of these is a complete sentence?", options:["Fast dog the.","Ran fast dog","The dog ran fast.","Running fast."], answer:2},
     {q:"Which of these is a sentence fragment?", options:["Under the table.","She smiled.","Birds fly.","The cat slept."], answer:0},
     {q:"A sentence fragment is missing ___.", options:["A part needed to express a complete thought","A title","A capital letter only","A period only"], answer:0},
     {q:"Why is it important to write in complete sentences?", options:["So readers can understand a full thought clearly","So sentences look longer","So readers get confused","So writing has no meaning"], answer:0}
   ],
   worksheet:[
     {prompt:"What two parts does a complete sentence need, like a subject and a verb?", answers:["a subject and a verb","subject and verb"]},
     {prompt:"Is the group of words running fast a complete sentence or a fragment?", answers:["a fragment","fragment"]},
     {prompt:"Is the sentence the dog ran fast a complete sentence or a fragment?", answers:["a complete sentence","complete sentence"]}
   ]},
  {subject:"Math", title:"Adding Three One-Digit Numbers", summary:"Students learn strategies for adding three one-digit numbers together, such as looking for a ten first or adding two numbers before adding the third.",
   resourceLabel:"YouTube: Adding Three One-Digit Numbers", resourceUrl:"https://www.youtube.com/results?search_query=Adding%20Three%20One-Digit%20Numbers%20grade%202%20educational",
   quiz:[
     {q:"What is 2 + 3 + 4?", options:["7","8","9","10"], answer:2},
     {q:"What is 5 + 5 + 1?", options:["10","11","12","9"], answer:1},
     {q:"What is 6 + 2 + 2?", options:["8","10","11","9"], answer:1},
     {q:"When adding three numbers, a helpful strategy is to ___.", options:["Look for two numbers that make a ten first","Only add the first two numbers","Ignore the third number","Always add in a random order"], answer:0},
     {q:"What is 4 + 4 + 4?", options:["8","12","10","14"], answer:1}
   ],
   worksheet:[
     {prompt:"What is 2 + 3 + 4?", answers:["9","nine"]},
     {prompt:"What is 5 + 5 + 1?", answers:["11","eleven"]},
     {prompt:"What is 3 + 3 + 3?", answers:["9","nine"]}
   ]},
  {subject:"Science", title:"Fossils: Clues from the Past", summary:"Students learn that fossils are the preserved remains or traces of ancient plants and animals found in rock, giving scientists clues about life on earth long ago.",
   resourceLabel:"YouTube: Fossils: Clues from the Past", resourceUrl:"https://www.youtube.com/results?search_query=Fossils%3A%20Clues%20from%20the%20Past%20grade%202%20educational",
   quiz:[
     {q:"What word describes the preserved remains or traces of ancient living things?", options:["A shadow","A crystal","A fossil","A magnet"], answer:2},
     {q:"Where are fossils most often found?", options:["In layers of rock","Floating in the air","In a rainbow","Inside a cloud"], answer:0},
     {q:"What can scientists learn by studying fossils?", options:["How to bake bread","Clues about plants and animals from long ago","How to tell time","How to build a house"], answer:1},
     {q:"Which of these could become a fossil over a very long time?", options:["A dinosaur bone buried in mud","A cloud","A snowflake","A soap bubble"], answer:0},
     {q:"Studying fossils helps scientists understand ___.", options:["How to count money","How to grow a garden","What the weather will be tomorrow","What life on earth was like millions of years ago"], answer:3}
   ],
   worksheet:[
     {prompt:"What word describes the preserved remains or traces of ancient living things found in rock?", answers:["fossil","fossils"]},
     {prompt:"Name one place fossils are often found, like in rock.", answers:["in rock","rock","in the ground"]},
     {prompt:"What can scientists learn from studying fossils?", answers:["clues about life long ago","about ancient plants and animals","about the past"]}
   ]},
  {subject:"SocialStudies", title:"Schools Long Ago and Today", summary:"Students compare what schools were like long ago, such as one-room schoolhouses with fewer supplies, to schools today, which often have computers, libraries, and many more resources.",
   resourceLabel:"YouTube: Schools Long Ago and Today", resourceUrl:"https://www.youtube.com/results?search_query=Schools%20Long%20Ago%20and%20Today%20grade%202%20educational",
   quiz:[
     {q:"What did many schools look like long ago, especially in small communities?", options:["A school with no students","An underwater classroom","A large building with computers in every room","A one-room schoolhouse with all grades together"], answer:3},
     {q:"Which of these is something many schools have today that schools long ago usually did not?", options:["Chalkboards","Desks","Pencils","Computers"], answer:3},
     {q:"How did students long ago often travel to school compared to some students today?", options:["They often walked long distances","They always took a rocket","They always took an airplane","They never went to school"], answer:0},
     {q:"Comparing schools long ago and today helps us understand ___.", options:["How to grow food","How to play a sport","How to build a computer","How education has changed over time"], answer:3},
     {q:"Which of these might have been used for writing in schools long ago instead of paper and pencil?", options:["A laptop computer","A smartphone","A tablet","A small chalkboard called a slate"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one thing schools have today that schools long ago often did not have, like computers.", answers:["computers","a computer"]},
     {prompt:"What did many schools look like long ago, with all grades in one place?", answers:["a one-room schoolhouse","one-room schoolhouse","one room"]},
     {prompt:"Name one way schools have changed over time.", answers:["more technology","more resources","computers","bigger buildings"]}
   ]},
]},
{day:63, label:"Day 63 — Wed", subjects:[
  {subject:"Language", title:"Using Quotation Marks in Dialogue", summary:"Students learn that quotation marks are punctuation marks placed before and after the exact spoken words of a character in a story, helping readers know exactly what was said aloud.",
   resourceLabel:"YouTube: Using Quotation Marks in Dialogue", resourceUrl:"https://www.youtube.com/results?search_query=Using%20Quotation%20Marks%20in%20Dialogue%20grade%202%20educational",
   quiz:[
     {q:"What do we call the punctuation marks placed before and after the exact words a character speaks?", options:["Quotation marks","A period","A question mark","A comma"], answer:0},
     {q:"What do we call the words that characters speak aloud in a story?", options:["A summary","A heading","Dialogue","A caption"], answer:2},
     {q:"Why do writers use quotation marks around spoken words?", options:["To hide what a character said","To show readers exactly what a character said","To end the story","To make the story shorter"], answer:1},
     {q:"Quotation marks are placed ___ the exact words a character speaks.", options:["Before and after","In the middle of","Only before","Only after"], answer:0},
     {q:"Which part of a story would most likely use quotation marks?", options:["The title of the book","The table of contents","A conversation between two characters","The page number"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the punctuation marks placed before and after the exact words a character speaks?", answers:["quotation marks"]},
     {prompt:"What do we call the words that characters speak aloud in a story?", answers:["dialogue"]},
     {prompt:"Why do writers use quotation marks in a story?", answers:["to show exactly what a character said","to show spoken words","so readers know what was said"]}
   ]},
  {subject:"Math", title:"Missing Number Addition and Subtraction Sentences", summary:"Students solve equations with a missing number, such as 5 plus a missing number equals 9, by using their knowledge of addition and subtraction facts.",
   resourceLabel:"YouTube: Missing Number Addition and Subtraction Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Missing%20Number%20Addition%20and%20Subtraction%20Sentences%20grade%202%20educational",
   quiz:[
     {q:"What number makes this true: 5 + ___ = 9?", options:["5","9","4","14"], answer:2},
     {q:"What number makes this true: ___ minus 3 equals 6?", options:["6","9","3","12"], answer:1},
     {q:"What number makes this true: 10 minus ___ equals 4?", options:["6","10","14","4"], answer:0},
     {q:"What number makes this true: 7 + ___ = 12?", options:["4","6","5","7"], answer:2},
     {q:"To find a missing number in an equation, it helps to ___.", options:["Guess without checking","Think about the opposite operation or count on","Change all the numbers","Ignore the equal sign"], answer:1}
   ],
   worksheet:[
     {prompt:"What number makes this true: 5 + ___ = 9?", answers:["4","four"]},
     {prompt:"What number makes this true: ___ - 3 = 6?", answers:["9","nine"]},
     {prompt:"What number makes this true: 10 - ___ = 4?", answers:["6","six"]}
   ]},
  {subject:"Science", title:"Wheels and Axles: Making Work Easier", summary:"Students learn that a wheel and axle is a simple machine made of a wheel attached to a rod called an axle, which turns together to help move objects with less effort.",
   resourceLabel:"YouTube: Wheels and Axles: Making Work Easier", resourceUrl:"https://www.youtube.com/results?search_query=Wheels%20and%20Axles%3A%20Making%20Work%20Easier%20grade%202%20educational",
   quiz:[
     {q:"What do we call the rod that a wheel turns around?", options:["A ramp","An axle","A lever","A pulley"], answer:1},
     {q:"Which of these objects uses wheels and axles?", options:["A doorstop","A seesaw","A magnet","A bicycle"], answer:3},
     {q:"A wheel and axle is a type of ___.", options:["Simple machine","Living thing","Food group","Weather pattern"], answer:0},
     {q:"Using a wheel and axle to move a heavy object makes the task ___.", options:["Easier","Impossible","Slower and harder","Dangerous"], answer:0},
     {q:"Which part of a wagon turns together as one unit?", options:["The box only","The paint on the wagon","The wheel and axle","The handle only"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the rod that a wheel turns around?", answers:["an axle","axle"]},
     {prompt:"Name one object that uses wheels and axles, like a bicycle or a wagon.", answers:["a bicycle","bicycle","a wagon","wagon","a car","car"]},
     {prompt:"Does a wheel and axle make moving objects easier or harder?", answers:["easier"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Currency: The Loonie, Toonie, and Bills", summary:"Students learn about Canadian money, including the one dollar coin called the loonie, the two dollar coin called the toonie, and paper bills used to pay for goods and services.",
   resourceLabel:"YouTube: Canadian Currency: The Loonie, Toonie, and Bills", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Currency%3A%20The%20Loonie%2C%20Toonie%2C%20and%20Bills%20grade%202%20educational",
   quiz:[
     {q:"What is the name of the Canadian one dollar coin?", options:["The toonie","The nickel","The dime","The loonie"], answer:3},
     {q:"What is the name of the Canadian two dollar coin?", options:["The penny","The quarter","The loonie","The toonie"], answer:3},
     {q:"Why do people in Canada use money like coins and bills?", options:["To measure temperature","To decorate their homes","To feed animals","To pay for goods and services"], answer:3},
     {q:"Which of these is Canadian paper money called?", options:["A leaf","A rock","A bill","A ticket"], answer:2},
     {q:"The picture on the Canadian one dollar coin shows a ___.", options:["Moose","Bear","Loon, a type of bird","Beaver"], answer:2}
   ],
   worksheet:[
     {prompt:"What is the name of the Canadian one dollar coin?", answers:["loonie","the loonie"]},
     {prompt:"What is the name of the Canadian two dollar coin?", answers:["toonie","the toonie"]},
     {prompt:"Name one way Canadian money is used, like paying for goods and services.", answers:["to pay for goods","to buy things","paying for goods and services"]}
   ]},
]},
{day:64, label:"Day 64 — Thu", subjects:[
  {subject:"Language", title:"Point of View: Whose Story Is It", summary:"Students learn that point of view tells readers who is telling the story, such as first person, when a character uses words like I and me, or third person, when a narrator uses words like he, she, and they.",
   resourceLabel:"YouTube: Point of View: Whose Story Is It", resourceUrl:"https://www.youtube.com/results?search_query=Point%20of%20View%3A%20Whose%20Story%20Is%20It%20grade%202%20educational",
   quiz:[
     {q:"What do we call the perspective from which a story is told?", options:["A theme","Point of view","A heading","A caption"], answer:1},
     {q:"If a character tells the story using the word I, what point of view is being used?", options:["First person","No point of view","Second person","Third person"], answer:0},
     {q:"If a narrator tells the story using words like he and she, what point of view is being used?", options:["First person","No point of view","Third person","Second person"], answer:2},
     {q:"Which sentence is told from a first person point of view?", options:["He walked to the park with his dog.","I walked to the park with my dog.","They walked to the park with their dog.","She walked to the park with her dog."], answer:1},
     {q:"Knowing the point of view of a story helps readers understand ___.", options:["The title of the book","Whose thoughts and feelings are being shared","The font used in the book","The page number of the story"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call the perspective from which a story is told?", answers:["point of view"]},
     {prompt:"If a character tells the story using the word I, what point of view is that?", answers:["first person"]},
     {prompt:"If a narrator tells the story using words like he and she, what point of view is that?", answers:["third person"]}
   ]},
  {subject:"Math", title:"Arrays: Rows and Columns", summary:"Students learn that an array is a way of arranging objects into equal rows and columns, which helps show multiplication as repeated groups.",
   resourceLabel:"YouTube: Arrays: Rows and Columns", resourceUrl:"https://www.youtube.com/results?search_query=Arrays%3A%20Rows%20and%20Columns%20grade%202%20educational",
   quiz:[
     {q:"What do we call objects arranged into equal rows and columns?", options:["A pattern","A fraction","A graph","An array"], answer:3},
     {q:"If an array has 3 rows with 4 objects in each row, how many objects are there in total?", options:["12","9","7","10"], answer:0},
     {q:"If an array has 2 rows with 5 objects in each row, how many objects are there in total?", options:["5","12","10","7"], answer:2},
     {q:"In an array, each row must have ___.", options:["A different number of objects","The same number of objects as every other row","Only one object","No objects at all"], answer:1},
     {q:"Arrays help us understand multiplication because they show ___.", options:["Only time","Only subtraction","Only measurement","Equal groups arranged in rows and columns"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call objects arranged into equal rows and columns?", answers:["an array","array"]},
     {prompt:"If an array has 3 rows with 4 objects in each row, how many objects are there in total?", answers:["12","twelve"]},
     {prompt:"Do all rows in an array have the same number of objects?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Decomposers: Breaking Down Dead Plants and Animals", summary:"Students learn that decomposers, such as worms, mushrooms, and some bacteria, break down dead plants and animals, returning nutrients to the soil.",
   resourceLabel:"YouTube: Decomposers: Breaking Down Dead Plants and Animals", resourceUrl:"https://www.youtube.com/results?search_query=Decomposers%3A%20Breaking%20Down%20Dead%20Plants%20and%20Animals%20grade%202%20educational",
   quiz:[
     {q:"What do we call living things that break down dead plants and animals?", options:["Predators","Decomposers","Producers","Pollinators"], answer:1},
     {q:"Which of these is an example of a decomposer?", options:["A cloud","A rock","A rose","A worm"], answer:3},
     {q:"What do decomposers return to the soil after breaking down dead material?", options:["Plastic","Sand","Nutrients","Water only"], answer:2},
     {q:"Why are decomposers important to nature?", options:["They recycle nutrients so new plants can grow","They make soil disappear","They stop all plants from growing","They create pollution"], answer:0},
     {q:"Which of these is a job that mushrooms can do in nature?", options:["Fly through the air","Swim in the ocean","Help break down dead material","Make electricity"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call living things that break down dead plants and animals?", answers:["decomposers","decomposer"]},
     {prompt:"Name one example of a decomposer, like a worm or a mushroom.", answers:["a worm","worm","a mushroom","mushroom"]},
     {prompt:"What do decomposers return to the soil after breaking down dead material?", answers:["nutrients"]}
   ]},
  {subject:"SocialStudies", title:"Canadian National Parks: Protecting Wild Spaces", summary:"Students learn that Canada has national parks, protected areas of land set aside to preserve nature, wildlife, and beautiful landscapes for everyone to enjoy.",
   resourceLabel:"YouTube: Canadian National Parks: Protecting Wild Spaces", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20National%20Parks%3A%20Protecting%20Wild%20Spaces%20grade%202%20educational",
   quiz:[
     {q:"What do we call an area of land protected to preserve nature and wildlife?", options:["A parking lot","A national park","A factory","A shopping mall"], answer:1},
     {q:"Why are national parks important to Canada?", options:["They remove all trees","They stop animals from living freely","They are used only for building houses","They protect nature, wildlife, and beautiful landscapes"], answer:3},
     {q:"Which activity might a family enjoy in a national park?", options:["Watching a movie indoors","Shopping for clothes","Hiking and camping","Visiting a bank"], answer:2},
     {q:"National parks help protect animals by ___.", options:["Taking away their water","Preserving their natural habitats","Filling their homes with buildings","Removing their food sources"], answer:1},
     {q:"Which of these is something visitors are usually asked to do in a national park?", options:["Pick all the flowers","Leave garbage behind","Respect nature and leave no trace","Feed wild animals junk food"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call an area of land protected to preserve nature and wildlife?", answers:["a national park","national park"]},
     {prompt:"Name one reason national parks are important, like protecting wildlife.", answers:["to protect wildlife","protecting nature","protecting wildlife and nature"]},
     {prompt:"Name one activity people might do in a national park, like hiking.", answers:["hiking","camping","exploring nature"]}
   ]},
]},
{day:65, label:"Day 65 — Fri", subjects:[
  {subject:"Language", title:"Opinion Writing: Stating and Supporting an Opinion", summary:"Students learn to write an opinion by clearly stating what they think and giving at least one reason that supports their opinion.",
   resourceLabel:"YouTube: Opinion Writing: Stating and Supporting an Opinion", resourceUrl:"https://www.youtube.com/results?search_query=Opinion%20Writing%3A%20Stating%20and%20Supporting%20an%20Opinion%20grade%202%20educational",
   quiz:[
     {q:"What do we call a sentence that shares what a person thinks or feels?", options:["An opinion","A heading","A fact","A caption"], answer:0},
     {q:"What should a writer give after stating an opinion?", options:["A random fact","Nothing at all","A reason that supports it","A different opinion"], answer:2},
     {q:"Which sentence is an opinion?", options:["Puppies have four legs.","A puppy is a young dog.","Puppies are born with their eyes closed.","I think puppies are the best pets."], answer:3},
     {q:"Which word often signals that a sentence is an opinion?", options:["Is","Was","Think","Has"], answer:2},
     {q:"Good opinion writing includes ___.", options:["A clear opinion and a reason to support it","Only facts and numbers","A list of unrelated ideas","No opinion at all"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call a sentence that shares what a person thinks or feels?", answers:["an opinion","opinion"]},
     {prompt:"What should you give after stating your opinion to support it?", answers:["a reason","reason","reasons"]},
     {prompt:"Name one word that often signals an opinion, like think or believe.", answers:["think","believe","i think","i believe"]}
   ]},
  {subject:"Math", title:"Reading a Thermometer: Measuring Temperature", summary:"Students learn to read a thermometer to measure temperature in degrees Celsius and understand that higher numbers mean warmer temperatures.",
   resourceLabel:"YouTube: Reading a Thermometer: Measuring Temperature", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20a%20Thermometer%3A%20Measuring%20Temperature%20grade%202%20educational",
   quiz:[
     {q:"What tool do we use to measure temperature?", options:["A ruler","A clock","A scale","A thermometer"], answer:3},
     {q:"What unit is commonly used to measure temperature in Canada?", options:["Kilograms","Degrees Celsius","Metres","Litres"], answer:1},
     {q:"Does a higher number on a thermometer mean the temperature is warmer or colder?", options:["Colder","Impossible to tell","The same","Warmer"], answer:3},
     {q:"Which temperature would most likely be recorded on a hot summer day?", options:["Minus 20 degrees Celsius","30 degrees Celsius","5 degrees Celsius","0 degrees Celsius"], answer:1},
     {q:"A thermometer helps us know ___.", options:["How heavy something is","How long something is","How loud something is","How hot or cold something is"], answer:3}
   ],
   worksheet:[
     {prompt:"What tool do we use to measure temperature?", answers:["a thermometer","thermometer"]},
     {prompt:"What unit do we use to measure temperature in Canada?", answers:["degrees celsius","celsius"]},
     {prompt:"Does a higher number on a thermometer mean warmer or colder?", answers:["warmer"]}
   ]},
  {subject:"Science", title:"Plant Adaptations: Surviving in Different Places", summary:"Students learn that plants have special features, called adaptations, that help them survive in different environments, such as thick stems that store water in a desert or wide leaves that capture sunlight in a rainforest.",
   resourceLabel:"YouTube: Plant Adaptations: Surviving in Different Places", resourceUrl:"https://www.youtube.com/results?search_query=Plant%20Adaptations%3A%20Surviving%20in%20Different%20Places%20grade%202%20educational",
   quiz:[
     {q:"What word describes a special feature that helps a plant survive in its environment?", options:["An adaptation","A fossil","A habitat","A migration"], answer:0},
     {q:"Which adaptation helps a cactus survive in a dry desert?", options:["A stem that never stores water","Roots that need constant flooding","A thick stem that stores water","Wide leaves that need lots of rain"], answer:2},
     {q:"Why might a rainforest plant have very wide leaves?", options:["To avoid all sunlight","To capture as much sunlight as possible","To stay hidden underground","To store extra water like a cactus"], answer:1},
     {q:"Which of these is an example of a plant adaptation?", options:["A plant that never needs sunlight","Sharp spines that protect a cactus from animals","A plant that grows only in space","A plant that never needs water"], answer:1},
     {q:"Plant adaptations help a plant ___.", options:["Survive better in its specific environment","Move around like an animal","Stop needing sunlight completely","Change into a different species instantly"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes a special feature that helps a plant survive in its environment?", answers:["an adaptation","adaptation"]},
     {prompt:"Name one plant adaptation that helps a cactus survive in a dry desert.", answers:["storing water","thick stem","spines","storing water in its stem"]},
     {prompt:"Why do plants in a rainforest often have wide leaves?", answers:["to capture sunlight","to collect more sunlight","to catch sunlight"]}
   ]},
  {subject:"SocialStudies", title:"Time Zones: Why Time Differs Across Canada", summary:"Students learn that Canada is so wide that it is divided into different time zones, meaning the time of day can be different in places like British Columbia and Newfoundland at the same moment.",
   resourceLabel:"YouTube: Time Zones: Why Time Differs Across Canada", resourceUrl:"https://www.youtube.com/results?search_query=Time%20Zones%3A%20Why%20Time%20Differs%20Across%20Canada%20grade%202%20educational",
   quiz:[
     {q:"What do we call the different regions of time across a wide country like Canada?", options:["Provinces","Continents","Territories","Time zones"], answer:3},
     {q:"Why does Canada have more than one time zone?", options:["Because every province chooses a random time","Because Canada has only one season","Because Canada has no clocks","Because the country is very wide from coast to coast"], answer:3},
     {q:"If it is noon in one time zone, could it be a different time in another Canadian time zone at the same moment?", options:["No, time zones do not exist","No, it is always the same time everywhere","Yes, but only during winter","Yes, it could be earlier or later"], answer:3},
     {q:"Why is it helpful to know about time zones when calling family in another province?", options:["So you can skip a day of the week","So you can change the weather","So you know what time it actually is for them","So you can change the date on a calendar"], answer:2},
     {q:"Time zones exist because ___.", options:["The sun never moves","Clocks are different colours in each province","Different parts of the world see sunrise and sunset at different times","All places on earth have the exact same time"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the different regions of time across a wide country like Canada?", answers:["time zones","time zone"]},
     {prompt:"Why does Canada have more than one time zone?", answers:["because it is so wide","because the country is very wide","because it stretches across a large distance"]},
     {prompt:"Can it be a different time of day in two provinces at the same moment?", answers:["yes"]}
   ]},
]},
{day:66, label:"Day 66 — Mon", subjects:[
  {subject:"Language", title:"Idioms and Expressions", summary:"Students learn that an idiom is a group of words with a meaning different from the literal meaning of the individual words, such as it is raining cats and dogs meaning it is raining very hard.",
   resourceLabel:"YouTube: Idioms and Expressions", resourceUrl:"https://www.youtube.com/results?search_query=Idioms%20and%20Expressions%20grade%202%20educational",
   quiz:[
     {q:"What do we call a group of words whose meaning is different from what the words literally say?", options:["A heading","A fact","An idiom","A caption"], answer:2},
     {q:"What does the idiom it is raining cats and dogs mean?", options:["It is very sunny","It is very cold","It is raining very hard","Animals are falling from the sky"], answer:2},
     {q:"What does the idiom break a leg mean when said to a performer before a show?", options:["Be careful not to fall","Stay home today","Good luck","Stop performing"], answer:2},
     {q:"What does it mean if someone says an idea costs an arm and a leg?", options:["It requires body parts","It is impossible to buy","It is very expensive","It is very cheap"], answer:2},
     {q:"Understanding idioms helps readers because ___.", options:["Idioms have no meaning at all","Idioms always mean exactly what they say","The literal words do not always explain the real meaning","Idioms are only used in math"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a group of words whose meaning is different from what the words literally say?", answers:["an idiom","idiom"]},
     {prompt:"What does the idiom it is raining cats and dogs mean?", answers:["it is raining very hard","raining hard","heavy rain"]},
     {prompt:"What does the idiom break a leg mean when said to a performer?", answers:["good luck","wishing someone good luck"]}
   ]},
  {subject:"Math", title:"Near Doubles: Doubles Plus One and Doubles Minus One", summary:"Students learn to use known doubles facts, like 5 plus 5 equals 10, to quickly solve near doubles, such as 5 plus 6, by thinking of it as double 5 plus one more.",
   resourceLabel:"YouTube: Near Doubles: Doubles Plus One and Doubles Minus One", resourceUrl:"https://www.youtube.com/results?search_query=Near%20Doubles%3A%20Doubles%20Plus%20One%20and%20Doubles%20Minus%20One%20grade%202%20educational",
   quiz:[
     {q:"What is 5 + 5?", options:["10","11","8","9"], answer:0},
     {q:"Using the fact that 5 + 5 = 10, what is 5 + 6?", options:["10","11","9","12"], answer:1},
     {q:"Using the fact that 4 + 4 = 8, what is 4 + 5?", options:["10","9","8","7"], answer:1},
     {q:"Using the fact that 6 + 6 = 12, what is 6 + 7?", options:["12","13","14","11"], answer:1},
     {q:"Near doubles are a helpful strategy because they let us ___.", options:["Use a known double fact to solve a close addition problem quickly","Only work with even numbers","Always subtract instead of add","Ignore addition facts completely"], answer:0}
   ],
   worksheet:[
     {prompt:"What is 5 + 5?", answers:["10","ten"]},
     {prompt:"Using the fact that 5 + 5 = 10, what is 5 + 6?", answers:["11","eleven"]},
     {prompt:"Using the fact that 4 + 4 = 8, what is 4 + 5?", answers:["9","nine"]}
   ]},
  {subject:"Science", title:"Planets in Our Solar System", summary:"Students learn that the solar system includes the sun and the planets that orbit it, such as Mercury, Venus, Earth, and Mars, each with its own size and distance from the sun.",
   resourceLabel:"YouTube: Planets in Our Solar System", resourceUrl:"https://www.youtube.com/results?search_query=Planets%20in%20Our%20Solar%20System%20grade%202%20educational",
   quiz:[
     {q:"What do we call the group of planets that orbit the sun?", options:["The water cycle","The rock cycle","The solar system","The food chain"], answer:2},
     {q:"Which planet do people live on?", options:["Venus","Mars","Earth","Jupiter"], answer:2},
     {q:"Which of these is a planet in our solar system?", options:["Mars","A star","A comet","The moon"], answer:0},
     {q:"What do all the planets in our solar system orbit?", options:["The moon","The sun","A comet","Earth"], answer:1},
     {q:"Which planet is often called the red planet?", options:["Earth","Venus","Mars","Mercury"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the group of planets that orbit the sun?", answers:["the solar system","solar system"]},
     {prompt:"Which planet do people live on?", answers:["earth"]},
     {prompt:"Name one planet in our solar system besides earth, like Mars or Venus.", answers:["mars","venus","mercury","jupiter","saturn","uranus","neptune"]}
   ]},
  {subject:"SocialStudies", title:"Food From Around the World: Exploring Cultures Through Food", summary:"Students learn that families from different cultures often enjoy special foods and recipes that have been passed down for generations, helping to share and celebrate their culture.",
   resourceLabel:"YouTube: Food From Around the World: Exploring Cultures Through Food", resourceUrl:"https://www.youtube.com/results?search_query=Food%20From%20Around%20the%20World%3A%20Exploring%20Cultures%20Through%20Food%20grade%202%20educational",
   quiz:[
     {q:"Why might a family cook a special recipe that has been passed down for generations?", options:["To copy a recipe from a stranger","To avoid eating anything at all","To celebrate and share their culture","To follow a rule with no meaning"], answer:2},
     {q:"What can trying foods from different cultures teach us?", options:["Only about one culture","Only about cooking tools","About the traditions and history of different cultures","Nothing about other cultures"], answer:2},
     {q:"Which of these is an example of a food tradition?", options:["A family recipe passed down through generations","A brand new food invented yesterday","A food nobody has ever eaten","A food with no ingredients"], answer:0},
     {q:"Learning about food from around the world helps students understand ___.", options:["That all cultures eat the same food","That different cultures have unique and special traditions","That food has no connection to culture","That recipes never change"], answer:1},
     {q:"Sharing food from different cultures at a school event can help classmates ___.", options:["Ignore other cultures","Learn about and appreciate different cultures","Avoid trying new things","Stop celebrating traditions"], answer:1}
   ],
   worksheet:[
     {prompt:"Name one reason families might cook a special recipe passed down in their family.", answers:["to celebrate their culture","to share their culture","tradition"]},
     {prompt:"What do we call food traditions passed down from one generation to the next?", answers:["a tradition","tradition","family tradition"]},
     {prompt:"Why is it fun to try foods from different cultures?", answers:["to learn about other cultures","to experience different cultures","to learn about the world"]}
   ]},
]},
{day:67, label:"Day 67 — Tue", subjects:[
  {subject:"Language", title:"Alliteration: Repeating Beginning Sounds", summary:"Students learn that alliteration happens when two or more words close together begin with the same sound, such as silly snakes slither slowly, adding rhythm to writing.",
   resourceLabel:"YouTube: Alliteration: Repeating Beginning Sounds", resourceUrl:"https://www.youtube.com/results?search_query=Alliteration%3A%20Repeating%20Beginning%20Sounds%20grade%202%20educational",
   quiz:[
     {q:"What do we call it when two or more words close together begin with the same sound?", options:["Rhyme","Synonym","Alliteration","Onomatopoeia"], answer:2},
     {q:"Which phrase is an example of alliteration?", options:["The dog ran fast","I like pizza","She is happy","Silly snakes slither slowly"], answer:3},
     {q:"In the phrase silly snakes slither slowly, which sound repeats at the beginning of each word?", options:["The t sound","The s sound","The a sound","The l sound"], answer:1},
     {q:"Which pair of words shows alliteration?", options:["Big blue balloon","Big blue kite","Big red balloon","Small blue balloon"], answer:0},
     {q:"Writers use alliteration to ___.", options:["Make writing shorter","Add rhythm and a fun sound to their writing","Make writing harder to read","Remove all sounds from writing"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call it when two or more words close together begin with the same sound?", answers:["alliteration"]},
     {prompt:"Which two words show alliteration: happy hippo or happy elephant?", answers:["happy hippo"]},
     {prompt:"In the phrase silly snakes slither slowly, which sound repeats at the beginning of each word?", answers:["s","the s sound","silly s sound"]}
   ]},
  {subject:"Math", title:"Input and Output Number Patterns", summary:"Students learn to find a rule that changes an input number into an output number, such as add 2, and use that rule to complete a number pattern.",
   resourceLabel:"YouTube: Input and Output Number Patterns", resourceUrl:"https://www.youtube.com/results?search_query=Input%20and%20Output%20Number%20Patterns%20grade%202%20educational",
   quiz:[
     {q:"If the rule is add 2 and the input is 3, what is the output?", options:["5","6","3","4"], answer:0},
     {q:"If the rule is add 3 and the input is 4, what is the output?", options:["5","8","7","6"], answer:2},
     {q:"If an input of 5 gives an output of 8, what is the rule?", options:["Subtract 3","Add 2","Add 5","Add 3"], answer:3},
     {q:"If the rule is subtract 2 and the input is 9, what is the output?", options:["5","9","11","7"], answer:3},
     {q:"An input and output number pattern always follows ___.", options:["A different rule each time","Only subtraction","No rule at all","The same rule for every number in the pattern"], answer:3}
   ],
   worksheet:[
     {prompt:"If the rule is add 2 and the input is 3, what is the output?", answers:["5","five"]},
     {prompt:"If the rule is add 3 and the input is 4, what is the output?", answers:["7","seven"]},
     {prompt:"If an input of 5 gives an output of 8, what is the rule?", answers:["add 3","plus 3"]}
   ]},
  {subject:"Science", title:"How We Breathe: The Lungs and Respiratory System", summary:"Students learn that the lungs are organs inside the chest that help the body breathe in oxygen from the air and breathe out carbon dioxide.",
   resourceLabel:"YouTube: How We Breathe: The Lungs and Respiratory System", resourceUrl:"https://www.youtube.com/results?search_query=How%20We%20Breathe%3A%20The%20Lungs%20and%20Respiratory%20System%20grade%202%20educational",
   quiz:[
     {q:"What organs help us breathe air in and out?", options:["The stomach","The bones","The skin","The lungs"], answer:3},
     {q:"What gas does our body need that we breathe in from the air?", options:["Oxygen","Nitrogen only","Carbon dioxide","Smoke"], answer:0},
     {q:"What gas do we breathe out of our lungs?", options:["Water only","Oxygen","Helium","Carbon dioxide"], answer:3},
     {q:"Where are the lungs located in the body?", options:["Inside the foot","Inside the leg","Inside the chest","Inside the arm"], answer:2},
     {q:"Why is breathing important for our body?", options:["It has no purpose","It brings oxygen that our body needs to work","It only makes noise","It stops our heart from beating"], answer:1}
   ],
   worksheet:[
     {prompt:"What organs help us breathe air in and out?", answers:["lungs","the lungs"]},
     {prompt:"What gas do we breathe in that our body needs?", answers:["oxygen"]},
     {prompt:"What gas do we breathe out?", answers:["carbon dioxide"]}
   ]},
  {subject:"SocialStudies", title:"Postal Codes and Addresses: Finding Your Way", summary:"Students learn that an address, including a postal code, helps identify exactly where a person lives so that mail and packages can be delivered to the right place.",
   resourceLabel:"YouTube: Postal Codes and Addresses: Finding Your Way", resourceUrl:"https://www.youtube.com/results?search_query=Postal%20Codes%20and%20Addresses%3A%20Finding%20Your%20Way%20grade%202%20educational",
   quiz:[
     {q:"What do we call the group of letters and numbers that helps identify a specific area for mail delivery?", options:["A postal code","A birthday","A time zone","A phone number"], answer:0},
     {q:"Which of these is part of a home address?", options:["A shoe size","A favourite colour","A street name and house number","A birthday"], answer:2},
     {q:"Why is an address important?", options:["It tells you what to eat","It helps mail and packages reach the right place","It tells you the weather","It tells you what time it is"], answer:1},
     {q:"Who might use your address to deliver a package?", options:["A mail carrier","A teacher","A dentist","A chef"], answer:0},
     {q:"A complete address usually includes ___.", options:["Only a first name","Only a phone number","Only a favourite colour","A house number, street name, city, and postal code"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the group of letters and numbers that helps identify a specific area for mail delivery?", answers:["a postal code","postal code"]},
     {prompt:"Name one part of an address, like a street name or a house number.", answers:["a street name","street name","a house number","house number"]},
     {prompt:"Why is an address important for mail delivery?", answers:["so mail goes to the right place","so packages are delivered correctly","to find the right location"]}
   ]},
]},
{day:68, label:"Day 68 — Wed", subjects:[
  {subject:"Language", title:"Reading Fluency and Expression", summary:"Students learn that reading fluently means reading smoothly and at a good pace, while reading with expression means using your voice to show feelings and match punctuation, like excitement for an exclamation mark.",
   resourceLabel:"YouTube: Reading Fluency and Expression", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20Fluency%20and%20Expression%20grade%202%20educational",
   quiz:[
     {q:"What do we call reading smoothly and at a good pace?", options:["A caption","Fluency","A theme","A summary"], answer:1},
     {q:"What should your voice show when reading a sentence that ends with an exclamation mark?", options:["Silence","Confusion only","No feeling at all","Excitement or strong feeling"], answer:3},
     {q:"Reading with expression means ___.", options:["Using your voice to show feelings while reading","Reading as fast as possible with no pauses","Skipping all punctuation","Reading in a whisper the whole time"], answer:0},
     {q:"Why is reading fluency important?", options:["It removes all meaning from a story","It slows readers down on purpose","It helps readers understand and enjoy a story more easily","It makes reading impossible"], answer:2},
     {q:"If a sentence ends with a question mark, how should your voice sound at the end?", options:["It should stop suddenly with no sound","It should get very loud","It should stay completely flat","It should rise, like you are asking something"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call reading smoothly and at a good pace?", answers:["fluency","reading fluency","fluent reading"]},
     {prompt:"What should your voice show when you read a sentence that ends with an exclamation mark?", answers:["excitement","strong feeling","emotion"]},
     {prompt:"Why is reading with expression helpful to listeners?", answers:["it helps the story come alive","it makes the story more interesting","it helps listeners understand feelings"]}
   ]},
  {subject:"Math", title:"Line Plots: Organizing Data Points", summary:"Students learn to organize data on a line plot, a simple graph that uses marks above a number line to show how many times each value occurs.",
   resourceLabel:"YouTube: Line Plots: Organizing Data Points", resourceUrl:"https://www.youtube.com/results?search_query=Line%20Plots%3A%20Organizing%20Data%20Points%20grade%202%20educational",
   quiz:[
     {q:"What do we call a graph that uses marks above a number line to show data?", options:["A pictograph","A tally chart","A line plot","A bar graph"], answer:2},
     {q:"On a line plot, what does each mark usually represent?", options:["One piece of data","The total of all data","The average of all data","Nothing at all"], answer:0},
     {q:"If a line plot shows 3 marks above the number 5, how many times did the value 5 occur in the data?", options:["5","8","3","2"], answer:2},
     {q:"A line plot is a useful tool because it helps us ___.", options:["Measure length","See how often each value occurs in a set of data","Tell time","Measure temperature"], answer:1},
     {q:"If the number 4 has more marks above it than any other number on a line plot, what does that tell us?", options:["The value 4 is the smallest number","The value 4 was never counted","The value 4 occurs least often","The value 4 occurs most often in the data"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call a graph that uses marks above a number line to show data?", answers:["a line plot","line plot"]},
     {prompt:"On a line plot, what does each mark usually represent?", answers:["one item","one piece of data","one data point"]},
     {prompt:"If a line plot shows 3 marks above the number 5, how many times did the value 5 occur?", answers:["3","three"]}
   ]},
  {subject:"Science", title:"Clouds and the Weather They Bring", summary:"Students learn to identify different types of clouds, such as fluffy cumulus clouds, thin wispy cirrus clouds, and gray stratus clouds, and connect them to the weather they often bring.",
   resourceLabel:"YouTube: Clouds and the Weather They Bring", resourceUrl:"https://www.youtube.com/results?search_query=Clouds%20and%20the%20Weather%20They%20Bring%20grade%202%20educational",
   quiz:[
     {q:"What do we call fluffy, cotton-like clouds often seen on a sunny day?", options:["Stratus clouds","Storm clouds only","Cumulus clouds","Cirrus clouds"], answer:2},
     {q:"What do we call thin, wispy clouds found high in the sky?", options:["Rain clouds only","Cirrus clouds","Stratus clouds","Cumulus clouds"], answer:1},
     {q:"What do we call gray clouds that often cover the whole sky and can bring rain?", options:["Cirrus clouds","Cumulus clouds","Clear clouds","Stratus clouds"], answer:3},
     {q:"Which type of cloud is most closely connected to a chance of rain covering the whole sky?", options:["Cirrus clouds","Stratus clouds","No clouds at all","Cumulus clouds"], answer:1},
     {q:"Observing clouds can help us ___.", options:["Predict what kind of weather might be coming","Tell exact time","Change the weather instantly","Measure how heavy an object is"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call fluffy, cotton-like clouds often seen on a sunny day?", answers:["cumulus clouds","cumulus"]},
     {prompt:"What do we call thin, wispy clouds high in the sky?", answers:["cirrus clouds","cirrus"]},
     {prompt:"What do we call gray clouds that often cover the whole sky and can bring rain?", answers:["stratus clouds","stratus"]}
   ]},
  {subject:"SocialStudies", title:"Preparing for Severe Weather: Staying Safe", summary:"Students learn simple steps for staying safe during severe weather, such as a thunderstorm or blizzard, including listening to an adult, staying indoors, and having an emergency kit ready.",
   resourceLabel:"YouTube: Preparing for Severe Weather: Staying Safe", resourceUrl:"https://www.youtube.com/results?search_query=Preparing%20for%20Severe%20Weather%3A%20Staying%20Safe%20grade%202%20educational",
   quiz:[
     {q:"What should you do during a thunderstorm to stay safe?", options:["Ignore the storm completely","Stay indoors away from windows","Go swimming outside","Stand under a tall tree outside"], answer:1},
     {q:"Who should children listen to for guidance during severe weather?", options:["A pet","A stranger","A trusted adult","No one"], answer:2},
     {q:"Which of these might be found in a family emergency kit?", options:["A television remote","A flashlight and batteries","A bicycle","A video game"], answer:1},
     {q:"Why is it helpful for a family to have an emergency plan for severe weather?", options:["So the storm becomes stronger","So everyone knows what to do and stays safe","So no one prepares at all","So the weather changes instantly"], answer:1},
     {q:"During a blizzard, which of these is a safe choice?", options:["Staying inside a warm home","Walking far from home alone","Ignoring warnings from adults","Staying outside for a long time"], answer:0}
   ],
   worksheet:[
     {prompt:"What should you do during a thunderstorm to stay safe?", answers:["stay indoors","go inside","stay inside"]},
     {prompt:"Who should you listen to during severe weather to stay safe?", answers:["an adult","a trusted adult","adults"]},
     {prompt:"Name one item that might be in a family emergency kit, like a flashlight.", answers:["a flashlight","flashlight","water","batteries"]}
   ]},
]},
{day:69, label:"Day 69 — Thu", subjects:[
  {subject:"Language", title:"Root Words and Word Families", summary:"Students learn that a root word is the base part of a word that carries its main meaning, and that other words can be built from it, such as play, playful, and player, all coming from the root word play.",
   resourceLabel:"YouTube: Root Words and Word Families", resourceUrl:"https://www.youtube.com/results?search_query=Root%20Words%20and%20Word%20Families%20grade%202%20educational",
   quiz:[
     {q:"What do we call the base part of a word that carries its main meaning?", options:["A caption","A root word","A synonym","An antonym"], answer:1},
     {q:"What is the root word in the word playful?", options:["Fully","Ful","Full","Play"], answer:3},
     {q:"Which of these words comes from the root word teach?", options:["Farmer","Painter","Doctor","Teacher"], answer:3},
     {q:"Which group of words are all part of the same word family built from the root word jump?", options:["Read, reader, reading, reread","Jump, jumped, jumping, jumper","Run, ran, running, runner","Play, player, playful, played"], answer:1},
     {q:"Understanding root words helps readers ___.", options:["Figure out the meaning of related unfamiliar words","Only read short words","Avoid learning new words","Forget how to read"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the base part of a word that carries its main meaning?", answers:["a root word","root word"]},
     {prompt:"What is the root word in the word playful?", answers:["play"]},
     {prompt:"Name one word that can be built from the root word teach, like teacher.", answers:["teacher","teaching","teaches"]}
   ]},
  {subject:"Math", title:"Multiplication Facts: 2s, 5s, and 10s", summary:"Students learn and practice basic multiplication facts for the 2 times table, 5 times table, and 10 times table, such as 2 times 3 equals 6.",
   resourceLabel:"YouTube: Multiplication Facts: 2s, 5s, and 10s", resourceUrl:"https://www.youtube.com/results?search_query=Multiplication%20Facts%3A%202s%2C%205s%2C%20and%2010s%20grade%202%20educational",
   quiz:[
     {q:"What is 2 times 3?", options:["6","5","8","7"], answer:0},
     {q:"What is 5 times 4?", options:["15","10","20","25"], answer:2},
     {q:"What is 10 times 2?", options:["12","10","20","22"], answer:2},
     {q:"What is 5 times 5?", options:["20","25","30","15"], answer:1},
     {q:"Multiplication facts for the 10 times table always end in what digit?", options:["0","5","2","1"], answer:0}
   ],
   worksheet:[
     {prompt:"What is 2 times 3?", answers:["6","six"]},
     {prompt:"What is 5 times 4?", answers:["20","twenty"]},
     {prompt:"What is 10 times 2?", answers:["20","twenty"]}
   ]},
  {subject:"Science", title:"Animal Diets: Herbivores, Carnivores, and Omnivores", summary:"Students learn that animals can be grouped by what they eat, such as herbivores that eat only plants, carnivores that eat only meat, and omnivores that eat both plants and meat.",
   resourceLabel:"YouTube: Animal Diets: Herbivores, Carnivores, and Omnivores", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Diets%3A%20Herbivores%2C%20Carnivores%2C%20and%20Omnivores%20grade%202%20educational",
   quiz:[
     {q:"What do we call an animal that eats only plants?", options:["A herbivore","A decomposer","A carnivore","An omnivore"], answer:0},
     {q:"What do we call an animal that eats only meat?", options:["A producer","A carnivore","An omnivore","A herbivore"], answer:1},
     {q:"What do we call an animal that eats both plants and meat?", options:["An omnivore","A herbivore","A carnivore","A decomposer"], answer:0},
     {q:"Which of these animals is a herbivore that eats mostly grass and leaves?", options:["A wolf","A deer","A lion","A shark"], answer:1},
     {q:"Bears are often considered omnivores because they eat ___.", options:["Only rocks and soil","Both plants like berries and meat like fish","Only sunlight","Only water"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call an animal that eats only plants?", answers:["a herbivore","herbivore"]},
     {prompt:"What do we call an animal that eats only meat?", answers:["a carnivore","carnivore"]},
     {prompt:"What do we call an animal that eats both plants and meat?", answers:["an omnivore","omnivore"]}
   ]},
  {subject:"SocialStudies", title:"Life in Northern Canada: Weather and Ways of Living", summary:"Students learn that Northern Canada has a cold climate with long winters, and that communities there have adapted their ways of living, travel, and clothing to the environment.",
   resourceLabel:"YouTube: Life in Northern Canada: Weather and Ways of Living", resourceUrl:"https://www.youtube.com/results?search_query=Life%20in%20Northern%20Canada%3A%20Weather%20and%20Ways%20of%20Living%20grade%202%20educational",
   quiz:[
     {q:"What kind of climate does Northern Canada generally have?", options:["A cold climate with long winters","A hot climate with no winter","A rainy climate with no snow","A desert climate with no water"], answer:0},
     {q:"Which of these is a way people in Northern Canada might adapt to a cold climate?", options:["Avoiding all winter clothing","Ignoring the cold weather","Wearing sandals year round","Wearing warm layered clothing"], answer:3},
     {q:"Why might communities in Northern Canada use different methods of travel than a big city?", options:["Because cars are not allowed anywhere in Canada","Because of snow, ice, and remote locations","Because they have no need to travel","Because there are no roads anywhere in Canada"], answer:1},
     {q:"Which of these might be true about daylight in parts of Northern Canada during winter?", options:["There is always more daylight than in summer","There can be very few hours of daylight","There is no daylight ever, all year","There is always exactly 12 hours of daylight"], answer:1},
     {q:"Learning about life in Northern Canada helps us understand ___.", options:["That no one lives in Northern Canada","That all parts of Canada have the same weather","That climate has no effect on daily life","How people adapt their lives to a unique climate"], answer:3}
   ],
   worksheet:[
     {prompt:"What kind of climate does Northern Canada have, with long cold winters?", answers:["a cold climate","cold climate"]},
     {prompt:"Name one way people in Northern Canada might adapt to the cold climate, like wearing warm clothing.", answers:["wearing warm clothing","warm clothing","special travel methods"]},
     {prompt:"Why might traveling in Northern Canada look different than traveling in a city?", answers:["because of snow and ice","because of the cold climate","different terrain"]}
   ]},
]},
{day:70, label:"Day 70 — Fri", subjects:[
  {subject:"Language", title:"Final Review: Language Skills (Days 61-69)", summary:"Students review Language skills from Days 61 to 69: irregular past tense verbs, sentence fragments, quotation marks, point of view, opinion writing, idioms, alliteration, reading fluency, and root words.",
   resourceLabel:"YouTube: Final Review: Language Skills (Days 61-69)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Language%20Skills%20%28Days%2061-69%29%20grade%202%20educational",
   quiz:[
     {q:"What is the past tense of the verb go?", options:["Goed","Going","Goes","Went"], answer:3},
     {q:"What two parts does a complete sentence need?", options:["Only a question mark","Only a capital letter","A subject and a verb","Only a noun"], answer:2},
     {q:"What do we call the punctuation marks placed before and after the exact words a character speaks?", options:["Quotation marks","A comma","A period","A question mark"], answer:0},
     {q:"What do we call the perspective from which a story is told?", options:["A theme","Point of view","A caption","A heading"], answer:1},
     {q:"What do we call a group of words whose meaning is different from what the words literally say?", options:["A fact","A caption","A heading","An idiom"], answer:3}
   ],
   worksheet:[
     {prompt:"What is the past tense of the verb go?", answers:["went"]},
     {prompt:"What do we call a group of words whose meaning is different from what the words literally say?", answers:["an idiom","idiom"]},
     {prompt:"What do we call the base part of a word that carries its main meaning?", answers:["a root word","root word"]}
   ]},
  {subject:"Math", title:"Final Review: Math Skills (Days 61-69)", summary:"Students review Math skills from Days 61 to 69: place value to 1000, adding three numbers, missing number equations, arrays, thermometers, near doubles, number patterns, line plots, and multiplication facts.",
   resourceLabel:"YouTube: Final Review: Math Skills (Days 61-69)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Math%20Skills%20%28Days%2061-69%29%20grade%202%20educational",
   quiz:[
     {q:"How many hundreds are in the number 342?", options:["7","3","2","4"], answer:1},
     {q:"What is 2 + 3 + 4?", options:["10","9","8","7"], answer:1},
     {q:"What number makes this true: 5 + ___ = 9?", options:["5","14","4","9"], answer:2},
     {q:"If an array has 3 rows with 4 objects in each row, how many objects are there in total?", options:["12","7","9","10"], answer:0},
     {q:"What is 2 times 3?", options:["6","8","5","7"], answer:0}
   ],
   worksheet:[
     {prompt:"How many hundreds are in the number 342?", answers:["3","three"]},
     {prompt:"What is 2 + 3 + 4?", answers:["9","nine"]},
     {prompt:"What is 2 times 3?", answers:["6","six"]}
   ]},
  {subject:"Science", title:"Final Review: Science Skills (Days 61-69)", summary:"Students review Science topics from Days 61 to 69: frog life cycles, fossils, wheels and axles, decomposers, plant adaptations, planets, breathing and lungs, clouds and weather, and animal diets.",
   resourceLabel:"YouTube: Final Review: Science Skills (Days 61-69)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Science%20Skills%20%28Days%2061-69%29%20grade%202%20educational",
   quiz:[
     {q:"What is the first stage of a frog life cycle?", options:["Tadpole","Adult frog","Egg","Froglet"], answer:2},
     {q:"What word describes the preserved remains or traces of ancient living things?", options:["A magnet","A crystal","A shadow","A fossil"], answer:3},
     {q:"What do we call living things that break down dead plants and animals?", options:["Decomposers","Producers","Pollinators","Predators"], answer:0},
     {q:"Which planet do people live on?", options:["Earth","Mars","Venus","Jupiter"], answer:0},
     {q:"What do we call an animal that eats only meat?", options:["A carnivore","A herbivore","An omnivore","A producer"], answer:0}
   ],
   worksheet:[
     {prompt:"What is the first stage of a frog life cycle?", answers:["egg","an egg"]},
     {prompt:"What word describes the preserved remains or traces of ancient living things found in rock?", answers:["fossil","fossils"]},
     {prompt:"What do we call an animal that eats only plants?", answers:["a herbivore","herbivore"]}
   ]},
  {subject:"SocialStudies", title:"Final Review: Social Studies Skills (Days 61-69)", summary:"Students review Social Studies topics from Days 61 to 69: local businesses, schools long ago and today, Canadian currency, national parks, time zones, food from around the world, addresses, severe weather safety, and life in Northern Canada.",
   resourceLabel:"YouTube: Final Review: Social Studies Skills (Days 61-69)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Social%20Studies%20Skills%20%28Days%2061-69%29%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of a local business?", options:["A bakery","A mountain","A cloud","A river"], answer:0},
     {q:"What is the name of the Canadian one dollar coin?", options:["The toonie","The dime","The nickel","The loonie"], answer:3},
     {q:"What do we call an area of land protected to preserve nature and wildlife?", options:["A factory","A shopping mall","A parking lot","A national park"], answer:3},
     {q:"What do we call the different regions of time across a wide country like Canada?", options:["Time zones","Provinces","Continents","Territories"], answer:0},
     {q:"What should you do during a thunderstorm to stay safe?", options:["Stand under a tall tree outside","Go swimming outside","Ignore the storm completely","Stay indoors away from windows"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the goods and services a business provides to help people?", answers:["goods and services","things people need"]},
     {prompt:"What is the name of the Canadian one dollar coin?", answers:["loonie","the loonie"]},
     {prompt:"What do we call an area of land protected to preserve nature and wildlife?", answers:["a national park","national park"]}
   ]},
]},
{day:71, label:"Day 71 — Mon", subjects:[
  {subject:"Language", title:"Similes: Comparing with Like and As", summary:"Students learn that a simile is a figure of speech that compares two different things using the words like or as, helping readers picture an idea more clearly, such as as brave as a lion.",
   resourceLabel:"YouTube: Similes: Comparing with Like and As", resourceUrl:"https://www.youtube.com/results?search_query=Similes%3A%20Comparing%20with%20Like%20and%20As%20grade%202%20educational",
   quiz:[
     {q:"What do we call a phrase that compares two things using like or as?", options:["An antonym","A simile","A synonym","A caption"], answer:1},
     {q:"Which sentence contains a simile?", options:["The kitten was as fluffy as a cloud.","The kitten is small.","The kitten sat down.","The kitten was fluffy."], answer:0},
     {q:"Finish the simile: as busy as a ___.", options:["Rock","Cloud","Bee","Chair"], answer:2},
     {q:"Which word is most often used along with like to form a simile?", options:["The","As","But","And"], answer:1},
     {q:"Writers use similes to ___.", options:["Help readers picture an idea by comparing it to something familiar","Make sentences shorter","Remove all description from writing","Confuse the reader on purpose"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call a phrase that compares two things using like or as?", answers:["a simile","simile"]},
     {prompt:"Finish the simile: as quiet as a ___.", answers:["mouse","a mouse"]},
     {prompt:"Which two words are most often used to signal a simile?", answers:["like and as","like, as"]}
   ]},
  {subject:"Math", title:"Three-Digit Addition with Regrouping", summary:"Students learn to add two three-digit numbers that require regrouping, carrying a group of ten ones into the tens place or a group of ten tens into the hundreds place.",
   resourceLabel:"YouTube: Three-Digit Addition with Regrouping", resourceUrl:"https://www.youtube.com/results?search_query=Three-Digit%20Addition%20with%20Regrouping%20grade%202%20educational",
   quiz:[
     {q:"What is 236 + 148?", options:["384","374","284","394"], answer:0},
     {q:"What is 275 + 126?", options:["301","391","411","401"], answer:3},
     {q:"What is 359 + 172?", options:["431","531","521","541"], answer:1},
     {q:"When adding two three-digit numbers, we regroup when a column adds up to ___.", options:["Ten or more","Always, no matter what","Exactly one","Zero"], answer:0},
     {q:"What is 418 + 265?", options:["583","693","673","683"], answer:3}
   ],
   worksheet:[
     {prompt:"What is 236 + 148?", answers:["384"]},
     {prompt:"What is 275 + 126?", answers:["401"]},
     {prompt:"When do we regroup while adding, when a column adds to ten or more, or when it adds to less than ten?", answers:["ten or more","when a column adds to ten or more"]}
   ]},
  {subject:"Science", title:"Parts of a Plant: Roots, Stem, Leaves, and Flower", summary:"Students learn to identify the main parts of a plant, including the roots that absorb water, the stem that supports the plant, the leaves that capture sunlight, and the flower that helps make seeds.",
   resourceLabel:"YouTube: Parts of a Plant: Roots, Stem, Leaves, and Flower", resourceUrl:"https://www.youtube.com/results?search_query=Parts%20of%20a%20Plant%3A%20Roots%2C%20Stem%2C%20Leaves%2C%20and%20Flower%20grade%202%20educational",
   quiz:[
     {q:"Which part of a plant absorbs water from the soil?", options:["The stem","The flower","The leaves","The roots"], answer:3},
     {q:"Which part of a plant supports it and carries water upward?", options:["The stem","The roots","The petals","The seeds"], answer:0},
     {q:"Which part of a plant captures sunlight to help make food?", options:["The roots","The seeds","The leaves","The stem"], answer:2},
     {q:"Which part of a plant helps it make seeds?", options:["The soil","The flower","The stem","The roots"], answer:1},
     {q:"Roots grow ___.", options:["Underground to anchor the plant and absorb water","Only in water, never in soil","In the sky to catch sunlight","Only on the flower"], answer:0}
   ],
   worksheet:[
     {prompt:"Which part of a plant absorbs water from the soil?", answers:["the roots","roots"]},
     {prompt:"Which part of a plant supports it and carries water upward?", answers:["the stem","stem"]},
     {prompt:"Which part of a plant captures sunlight to make food?", answers:["the leaves","leaves"]}
   ]},
  {subject:"SocialStudies", title:"Where Our Clothes and Toys Come From", summary:"Students learn that many of the clothes and toys we use are made in factories, sometimes in other countries, using materials that started as raw resources like cotton or plastic.",
   resourceLabel:"YouTube: Where Our Clothes and Toys Come From", resourceUrl:"https://www.youtube.com/results?search_query=Where%20Our%20Clothes%20and%20Toys%20Come%20From%20grade%202%20educational",
   quiz:[
     {q:"Where are many clothes and toys made before they reach a store?", options:["A farm only","A forest","A factory","A lake"], answer:2},
     {q:"Which of these is a raw material that clothing can be made from?", options:["Glass","Water only","Cotton","Metal only"], answer:2},
     {q:"Are all the clothes and toys people use always made in the same country they live in?", options:["Clothes are never made anywhere","Yes, always","No, many are made in other countries and shipped","Toys are never shipped anywhere"], answer:2},
     {q:"Why might a toy be made in one country and sold in another?", options:["Toys can only be sold in the country where they are made","Companies often make products where it is efficient, then ship them to stores worldwide","Toys are only made by hand at home","Shipping does not exist"], answer:1},
     {q:"Learning where products come from helps us understand ___.", options:["That factories do not exist","How different countries and communities are connected","That every product magically appears in stores","That all toys grow on trees"], answer:1}
   ],
   worksheet:[
     {prompt:"Where are many clothes and toys made before they reach a store?", answers:["a factory","factory","factories"]},
     {prompt:"Name one raw material that clothing can be made from, like cotton.", answers:["cotton","wool"]},
     {prompt:"Are all the clothes and toys we use always made in the same country we live in?", answers:["no"]}
   ]},
]},
{day:72, label:"Day 72 — Tue", subjects:[
  {subject:"Language", title:"Prepositions: Words That Show Where", summary:"Students learn that a preposition is a word that shows the location or position of one thing in relation to another, such as in, on, under, and beside.",
   resourceLabel:"YouTube: Prepositions: Words That Show Where", resourceUrl:"https://www.youtube.com/results?search_query=Prepositions%3A%20Words%20That%20Show%20Where%20grade%202%20educational",
   quiz:[
     {q:"What do we call a word that shows the position of one thing compared to another?", options:["A pronoun","A preposition","A verb","An adjective"], answer:1},
     {q:"Which sentence uses a preposition correctly to show location?", options:["The cat is under the table.","The cat under.","Table the cat is.","The cat is table."], answer:0},
     {q:"Which word is a preposition in the sentence: the book is on the shelf?", options:["Book","On","The","Shelf"], answer:1},
     {q:"Which of these is an example of a preposition?", options:["Quickly","Jumped","Beside","Happy"], answer:2},
     {q:"Prepositions help readers understand ___.", options:["When a story ends","How a character feels","Where something is located","Who wrote the story"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a word that shows the position of one thing compared to another, like under or beside?", answers:["a preposition","preposition"]},
     {prompt:"Which preposition tells that the ball is inside the box?", answers:["in","in the box"]},
     {prompt:"Name one preposition that tells where something is, such as under or beside.", answers:["under","beside","on","in","above","below"]}
   ]},
  {subject:"Math", title:"Three-Digit Subtraction with Regrouping", summary:"Students learn to subtract three-digit numbers that require regrouping, borrowing a group of ten from the tens place or hundreds place when a digit is too small to subtract from.",
   resourceLabel:"YouTube: Three-Digit Subtraction with Regrouping", resourceUrl:"https://www.youtube.com/results?search_query=Three-Digit%20Subtraction%20with%20Regrouping%20grade%202%20educational",
   quiz:[
     {q:"What is 342 - 158?", options:["284","184","194","174"], answer:1},
     {q:"What is 500 - 267?", options:["233","243","333","223"], answer:0},
     {q:"What is 623 - 348?", options:["375","265","285","275"], answer:3},
     {q:"When the top digit in a column is smaller than the bottom digit, what do we do to subtract?", options:["Ignore that column","Regroup from the next place value","Skip the whole problem","Add instead of subtract"], answer:1},
     {q:"What is 415 - 289?", options:["226","116","126","136"], answer:2}
   ],
   worksheet:[
     {prompt:"What is 342 - 158?", answers:["184"]},
     {prompt:"What is 500 - 267?", answers:["233"]},
     {prompt:"When subtracting, if the top digit is smaller than the bottom digit in a column, what do we do?", answers:["regroup","borrow from the next column","regroup from the next place value"]}
   ]},
  {subject:"Science", title:"Levers: Lifting with Less Effort", summary:"Students learn that a lever is a simple machine made of a bar that rests on a fixed point called a fulcrum, which helps lift or move heavy objects with less effort.",
   resourceLabel:"YouTube: Levers: Lifting with Less Effort", resourceUrl:"https://www.youtube.com/results?search_query=Levers%3A%20Lifting%20with%20Less%20Effort%20grade%202%20educational",
   quiz:[
     {q:"What do we call the fixed point that a lever rests on?", options:["An axle","A wedge","A fulcrum","A pulley"], answer:2},
     {q:"Which of these tools is an example of a lever?", options:["A thermometer","A magnet","A funnel","A seesaw"], answer:3},
     {q:"A lever is a type of ___.", options:["Food group","Living thing","Simple machine","Weather pattern"], answer:2},
     {q:"Using a lever to lift a heavy rock makes the task ___.", options:["Dangerous only","Slower and harder","Impossible","Easier"], answer:3},
     {q:"Which part of a lever stays still while the bar moves up and down?", options:["The fulcrum","The handle","The load","The tip"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the fixed point that a lever rests on?", answers:["a fulcrum","fulcrum"]},
     {prompt:"Name one tool that works as a lever, like a seesaw or a shovel.", answers:["a seesaw","seesaw","a shovel","shovel"]},
     {prompt:"Does a lever make lifting a heavy object easier or harder?", answers:["easier"]}
   ]},
  {subject:"SocialStudies", title:"Advertising: How Companies Try to Sell Us Things", summary:"Students learn that advertisements are messages created by companies to convince people to buy a product, often using bright colours, catchy words, or famous characters to grab attention.",
   resourceLabel:"YouTube: Advertising: How Companies Try to Sell Us Things", resourceUrl:"https://www.youtube.com/results?search_query=Advertising%3A%20How%20Companies%20Try%20to%20Sell%20Us%20Things%20grade%202%20educational",
   quiz:[
     {q:"What do we call a message created by a company to convince people to buy a product?", options:["A biography","An advertisement","A weather report","A map"], answer:1},
     {q:"Which of these is a technique advertisements often use to grab attention?", options:["Bright colours and catchy words","Silence and no sound at all","Blank pages with no pictures","Tiny grey text no one can read"], answer:0},
     {q:"Why is it helpful to think carefully before buying something seen in an advertisement?", options:["Because advertisements are always true","To avoid ever buying anything at all","To decide if it is something you really need or want","Because advertisements never try to persuade anyone"], answer:2},
     {q:"Where might a child see an advertisement?", options:["On television, a website, or a billboard","Nowhere at all","Only in outer space","Only inside a locked box"], answer:0},
     {q:"Advertisements often try to ___.", options:["Teach a math lesson","Give a weather forecast","Explain a science experiment","Persuade people that they need or want a product"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call a message created by a company to convince people to buy a product?", answers:["an advertisement","advertisement","an ad"]},
     {prompt:"Name one technique advertisements use to grab attention, like bright colours.", answers:["bright colours","catchy words","famous characters"]},
     {prompt:"Why is it a good idea to think carefully before buying something you saw in an advertisement?", answers:["to make sure you really need it","to decide if it is a good choice","to avoid spending money on things you do not need"]}
   ]},
]},
{day:73, label:"Day 73 — Wed", subjects:[
  {subject:"Language", title:"Interjections: Showing Strong Feelings", summary:"Students learn that an interjection is a short word or phrase that expresses strong feeling, such as wow, oh no, or hooray, and is often followed by an exclamation mark.",
   resourceLabel:"YouTube: Interjections: Showing Strong Feelings", resourceUrl:"https://www.youtube.com/results?search_query=Interjections%3A%20Showing%20Strong%20Feelings%20grade%202%20educational",
   quiz:[
     {q:"What do we call a short word or phrase that expresses strong feeling?", options:["A pronoun","An interjection","A preposition","A synonym"], answer:1},
     {q:"Which of these is an example of an interjection?", options:["Under","Hooray","Quietly","Table"], answer:1},
     {q:"What punctuation mark most often follows an interjection?", options:["A question mark","An exclamation mark","A comma","A period"], answer:1},
     {q:"Which sentence begins with an interjection?", options:["Wow, that is a huge dinosaur!","A huge dinosaur is here.","That is a huge dinosaur.","Is that a huge dinosaur?"], answer:0},
     {q:"Interjections are used in writing to ___.", options:["Connect two sentences together","Name a person or place","Show strong feelings like surprise or excitement","Show the location of an object"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a short word that expresses strong feeling, like wow?", answers:["an interjection","interjection"]},
     {prompt:"What punctuation mark often follows an interjection?", answers:["an exclamation mark","exclamation mark","exclamation point"]},
     {prompt:"Give one example of an interjection that shows excitement.", answers:["wow","hooray","yay","oh no","ouch"]}
   ]},
  {subject:"Math", title:"Multiplication Facts: 3s and 4s", summary:"Students learn and practice basic multiplication facts for the 3 times table and 4 times table, such as 3 times 4 equals 12.",
   resourceLabel:"YouTube: Multiplication Facts: 3s and 4s", resourceUrl:"https://www.youtube.com/results?search_query=Multiplication%20Facts%3A%203s%20and%204s%20grade%202%20educational",
   quiz:[
     {q:"What is 3 times 4?", options:["14","10","12","16"], answer:2},
     {q:"What is 4 times 5?", options:["20","16","24","18"], answer:0},
     {q:"What is 3 times 6?", options:["15","21","18","12"], answer:2},
     {q:"What is 4 times 4?", options:["20","16","14","12"], answer:1},
     {q:"What is 3 times 7?", options:["20","21","18","24"], answer:1}
   ],
   worksheet:[
     {prompt:"What is 3 times 4?", answers:["12"]},
     {prompt:"What is 4 times 5?", answers:["20"]},
     {prompt:"What is 3 times 6?", answers:["18"]}
   ]},
  {subject:"Science", title:"The Heart: Pumping Blood Through Our Body", summary:"Students learn that the heart is a muscle that pumps blood through the body, delivering oxygen and nutrients to every part, and that exercise helps keep the heart strong.",
   resourceLabel:"YouTube: The Heart: Pumping Blood Through Our Body", resourceUrl:"https://www.youtube.com/results?search_query=The%20Heart%3A%20Pumping%20Blood%20Through%20Our%20Body%20grade%202%20educational",
   quiz:[
     {q:"What organ pumps blood through the body?", options:["The brain","The heart","The lungs","The stomach"], answer:1},
     {q:"What does blood deliver to every part of the body?", options:["Only sound","Only water","Only air","Oxygen and nutrients"], answer:3},
     {q:"Which of these activities helps keep the heart strong?", options:["Regular exercise","Skipping meals","Sitting still all day","Avoiding all movement"], answer:0},
     {q:"The heart is made mostly of ___.", options:["Bone","Skin","Muscle","Hair"], answer:2},
     {q:"Why is the heart an important organ?", options:["It pumps blood that carries oxygen through the body","It helps us hear","It helps us smell","It helps us see"], answer:0}
   ],
   worksheet:[
     {prompt:"What organ pumps blood through the body?", answers:["the heart","heart"]},
     {prompt:"What does blood deliver to every part of the body?", answers:["oxygen and nutrients","oxygen","nutrients"]},
     {prompt:"Name one activity that helps keep the heart strong, like exercise.", answers:["exercise","running","playing sports","being active"]}
   ]},
  {subject:"SocialStudies", title:"Levels of Government: Town, Province, and Country", summary:"Students learn that Canada has three levels of government, municipal government that looks after a town or city, provincial government that looks after a province, and federal government that looks after the whole country.",
   resourceLabel:"YouTube: Levels of Government: Town, Province, and Country", resourceUrl:"https://www.youtube.com/results?search_query=Levels%20of%20Government%3A%20Town%2C%20Province%2C%20and%20Country%20grade%202%20educational",
   quiz:[
     {q:"What do we call the level of government that looks after a town or city?", options:["Federal government","Provincial government","No government","Municipal government"], answer:3},
     {q:"What do we call the level of government that looks after the whole country?", options:["Municipal government","Federal government","Town council only","Provincial government"], answer:1},
     {q:"Which level of government looks after an entire province, like Ontario?", options:["School government","Municipal government","Provincial government","Federal government"], answer:2},
     {q:"Which of these is usually a responsibility of a municipal government?", options:["The entire national defence","Choosing the countrywide currency","Local roads and garbage collection","Setting the whole country border"], answer:2},
     {q:"Canada has how many main levels of government?", options:["Ten","One","Five","Three"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the level of government that looks after a town or city?", answers:["municipal government","municipal"]},
     {prompt:"What do we call the level of government that looks after the whole country?", answers:["federal government","federal"]},
     {prompt:"Name one thing a provincial government might be responsible for, like schools or highways.", answers:["schools","highways","hospitals"]}
   ]},
]},
{day:74, label:"Day 74 — Thu", subjects:[
  {subject:"Language", title:"Persuasive Writing: Convincing Your Reader", summary:"Students learn that persuasive writing tries to convince a reader to agree with an idea or take an action by giving strong reasons and using words like should or must.",
   resourceLabel:"YouTube: Persuasive Writing: Convincing Your Reader", resourceUrl:"https://www.youtube.com/results?search_query=Persuasive%20Writing%3A%20Convincing%20Your%20Reader%20grade%202%20educational",
   quiz:[
     {q:"What is the main goal of persuasive writing?", options:["To tell what time it is","To list random facts","To describe a setting only","To convince the reader to agree with an idea"], answer:3},
     {q:"Which sentence is an example of persuasive writing?", options:["Recycling bins are blue.","Paper comes from trees.","You should recycle to help protect the earth.","The earth is a planet."], answer:2},
     {q:"Which word is commonly used in persuasive writing to urge the reader to act?", options:["Has","Should","Was","The"], answer:1},
     {q:"A strong piece of persuasive writing includes ___.", options:["No opinion at all","Clear reasons that support the opinion of the writer","Only questions and no reasons","Random unrelated facts"], answer:1},
     {q:"Why might a student write a persuasive letter to their school?", options:["To list the alphabet","To convince the school to make a positive change","To retell a story","To describe the weather"], answer:1}
   ],
   worksheet:[
     {prompt:"What is the goal of persuasive writing?", answers:["to convince the reader","convince the reader","to persuade the reader"]},
     {prompt:"Name one word often used in persuasive writing, like should or must.", answers:["should","must"]},
     {prompt:"What should a persuasive writer give to support an idea?", answers:["strong reasons","reasons","a reason"]}
   ]},
  {subject:"Math", title:"Fractions of a Group: Sharing a Set of Objects", summary:"Students learn to find a fraction of a group of objects, such as finding one half of a group of 8 apples by splitting the group into two equal parts.",
   resourceLabel:"YouTube: Fractions of a Group: Sharing a Set of Objects", resourceUrl:"https://www.youtube.com/results?search_query=Fractions%20of%20a%20Group%3A%20Sharing%20a%20Set%20of%20Objects%20grade%202%20educational",
   quiz:[
     {q:"What is one half of a group of 8 apples?", options:["6","8","4","2"], answer:2},
     {q:"What is one quarter of a group of 12 stickers?", options:["2","6","4","3"], answer:3},
     {q:"If a group of 6 balloons is split into two equal parts, how many balloons are in each part?", options:["6","3","4","2"], answer:1},
     {q:"What is one third of a group of 9 marbles?", options:["2","9","4","3"], answer:3},
     {q:"To find a fraction of a group, we ___.", options:["Multiply the group by ten","Add one to the group","Ignore the group size","Split the group into equal parts"], answer:3}
   ],
   worksheet:[
     {prompt:"What is one half of a group of 8 apples?", answers:["4"]},
     {prompt:"What is one quarter of a group of 12 stickers?", answers:["3"]},
     {prompt:"If a group of 6 balloons is split into two equal parts, how many balloons are in each part?", answers:["3"]}
   ]},
  {subject:"Science", title:"How Our Body Digests Food", summary:"Students learn that digestion is the process the body uses to break down food into nutrients, starting in the mouth and continuing through the stomach and intestines.",
   resourceLabel:"YouTube: How Our Body Digests Food", resourceUrl:"https://www.youtube.com/results?search_query=How%20Our%20Body%20Digests%20Food%20grade%202%20educational",
   quiz:[
     {q:"What do we call the process the body uses to break down food?", options:["Circulation","Reflection","Respiration","Digestion"], answer:3},
     {q:"Where does digestion of food begin?", options:["The mouth","The lungs","The intestines","The stomach"], answer:0},
     {q:"Which organ helps break down food after it leaves the mouth?", options:["The heart","The stomach","The lungs","The brain"], answer:1},
     {q:"Why does our body need to digest food?", options:["To change food into water","To break it down into nutrients the body can use","To make food disappear completely","To stop the body from growing"], answer:1},
     {q:"After food leaves the stomach, where does it travel next?", options:["The brain","The heart","The intestines","The lungs"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the process the body uses to break down food?", answers:["digestion"]},
     {prompt:"Where does digestion begin?", answers:["the mouth","mouth"]},
     {prompt:"Name one organ that helps digest food, like the stomach.", answers:["the stomach","stomach","the intestines","intestines"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Holidays: Canada Day and Remembrance Day", summary:"Students learn about two important Canadian holidays: Canada Day on July 1st, which celebrates the birthday of Canada, and Remembrance Day on November 11th, when Canadians honour those who served in the armed forces.",
   resourceLabel:"YouTube: Canadian Holidays: Canada Day and Remembrance Day", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Holidays%3A%20Canada%20Day%20and%20Remembrance%20Day%20grade%202%20educational",
   quiz:[
     {q:"On what date is Canada Day celebrated?", options:["January 1st","December 25th","July 1st","November 11th"], answer:2},
     {q:"On what date is Remembrance Day observed?", options:["October 31st","September 1st","November 11th","July 1st"], answer:2},
     {q:"What does Canada Day celebrate?", options:["The start of school","A famous hockey game","The end of winter","The birthday of Canada"], answer:3},
     {q:"What symbol do many Canadians wear in November to honour those who served?", options:["A poppy","A maple leaf pin","A snowflake","A flag pin"], answer:0},
     {q:"Why do communities across Canada hold ceremonies on Remembrance Day?", options:["To welcome the new school year","To celebrate a hockey championship","To celebrate a harvest festival","To honour and remember those who served the country"], answer:3}
   ],
   worksheet:[
     {prompt:"On what date is Canada Day celebrated?", answers:["july 1","july 1st"]},
     {prompt:"On what date is Remembrance Day observed?", answers:["november 11","november 11th"]},
     {prompt:"What symbol do Canadians often wear in November to honour those who served?", answers:["a poppy","poppy"]}
   ]},
]},
{day:75, label:"Day 75 — Fri", subjects:[
  {subject:"Language", title:"Nonfiction Text Features: Diagrams and Labels", summary:"Students learn that nonfiction books often include diagrams and labels, which are pictures with words pointing to specific parts, to help readers understand information more clearly.",
   resourceLabel:"YouTube: Nonfiction Text Features: Diagrams and Labels", resourceUrl:"https://www.youtube.com/results?search_query=Nonfiction%20Text%20Features%3A%20Diagrams%20and%20Labels%20grade%202%20educational",
   quiz:[
     {q:"What do we call a picture with labels pointing to specific parts?", options:["A glossary","A diagram","A caption","A heading"], answer:1},
     {q:"What do we call the words that point to and name parts of a diagram?", options:["Titles","Chapters","Rhymes","Labels"], answer:3},
     {q:"Why do nonfiction books often include diagrams?", options:["To confuse the reader","To help readers understand information more clearly","To make the book longer","To replace all the words in a book"], answer:1},
     {q:"Which of these would most likely include a labelled diagram?", options:["A fairy tale about a dragon","A birthday card","A nonfiction book about the parts of a plant","A poem about the moon"], answer:2},
     {q:"A label on a diagram usually points to ___.", options:["The title of the book","The page number","A specific part being named","A random unrelated word"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a picture with labels pointing to specific parts?", answers:["a diagram","diagram"]},
     {prompt:"What do we call the words that point to and name parts of a diagram?", answers:["labels","a label"]},
     {prompt:"Why do nonfiction books use diagrams and labels?", answers:["to help readers understand information","to explain information clearly","to show information visually"]}
   ]},
  {subject:"Math", title:"Comparing Fractions: Which Is Greater", summary:"Students learn to compare simple fractions with the same denominator, such as comparing three quarters and one quarter, to decide which fraction represents a greater amount.",
   resourceLabel:"YouTube: Comparing Fractions: Which Is Greater", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Fractions%3A%20Which%20Is%20Greater%20grade%202%20educational",
   quiz:[
     {q:"Which is greater, one half or one quarter?", options:["One half","Cannot tell","One quarter","They are equal"], answer:0},
     {q:"Which is greater, three quarters or one quarter?", options:["They are equal","Three quarters","One quarter","Cannot tell"], answer:1},
     {q:"When two fractions have the same denominator, which fraction is greater?", options:["The one written first","They are always equal","The one with the smaller numerator","The one with the larger numerator"], answer:3},
     {q:"Which is greater, two thirds or one third?", options:["They are equal","One third","Cannot tell","Two thirds"], answer:3},
     {q:"A fraction with a larger numerator and the same denominator represents ___.", options:["No amount at all","The same amount","A greater amount","A smaller amount"], answer:2}
   ],
   worksheet:[
     {prompt:"Which is greater, one half or one quarter?", answers:["one half"]},
     {prompt:"Which is greater, three quarters or one quarter?", answers:["three quarters"]},
     {prompt:"When two fractions have the same denominator, how do we know which is greater?", answers:["the one with the bigger numerator is greater","compare the numerators","the larger top number is greater"]}
   ]},
  {subject:"Science", title:"Types of Precipitation: Rain, Snow, Sleet, and Hail", summary:"Students learn that precipitation is water that falls from clouds in different forms, including rain, snow, sleet, and hail, depending on the temperature of the air.",
   resourceLabel:"YouTube: Types of Precipitation: Rain, Snow, Sleet, and Hail", resourceUrl:"https://www.youtube.com/results?search_query=Types%20of%20Precipitation%3A%20Rain%2C%20Snow%2C%20Sleet%2C%20and%20Hail%20grade%202%20educational",
   quiz:[
     {q:"What word describes water that falls from clouds in different forms?", options:["Condensation","Evaporation","Pollination","Precipitation"], answer:3},
     {q:"Which of these is a form of precipitation?", options:["A rainbow","Sunshine","Snow","Wind"], answer:2},
     {q:"What usually causes precipitation to fall as snow instead of rain?", options:["Hot temperatures","Strong sunshine","No clouds at all","Cold temperatures"], answer:3},
     {q:"Which type of precipitation falls as small balls of ice, often during a thunderstorm?", options:["Hail","Rain","Fog","Snow"], answer:0},
     {q:"Precipitation is an important part of ___.", options:["The water cycle","The solar system","The rock cycle","The food chain"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes water that falls from clouds, such as rain or snow?", answers:["precipitation"]},
     {prompt:"Name one form of precipitation that falls in cold winter weather.", answers:["snow","hail","sleet"]},
     {prompt:"What usually causes water to fall as snow instead of rain?", answers:["cold air","cold temperatures","freezing temperatures"]}
   ]},
  {subject:"SocialStudies", title:"Family Heritage: Learning Where We Come From", summary:"Students learn that heritage means the traditions, language, and history passed down through a family, and that people can learn about their heritage by talking to relatives or looking at old photographs.",
   resourceLabel:"YouTube: Family Heritage: Learning Where We Come From", resourceUrl:"https://www.youtube.com/results?search_query=Family%20Heritage%3A%20Learning%20Where%20We%20Come%20From%20grade%202%20educational",
   quiz:[
     {q:"What word describes the traditions, language, and history passed down through a family?", options:["Heritage","Government","Currency","Geography"], answer:0},
     {q:"Which of these is a good way to learn about family heritage?", options:["Ignoring all family members","Talking with relatives about family stories","Only reading science books","Watching random cartoons"], answer:1},
     {q:"Which of these could be part of a family heritage?", options:["A rule made up on the spot","A special recipe passed down for generations","A stranger encountered yesterday","A brand new invention with no history"], answer:1},
     {q:"Why might someone look at old family photographs?", options:["To learn about outer space","To learn how to cook","To learn a new sport","To learn about family history and heritage"], answer:3},
     {q:"Learning about family heritage helps a person understand ___.", options:["Where their family traditions and history come from","How to measure length","How to tell time","How to build a house"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes the traditions, language, and history passed down through a family?", answers:["heritage"]},
     {prompt:"Name one way a person could learn about their family heritage, like talking to relatives.", answers:["talking to relatives","asking relatives","looking at old photographs"]},
     {prompt:"Name one thing that might be part of a family heritage, like a language or a recipe.", answers:["a language","language","a recipe","recipe","a tradition","tradition"]}
   ]},
]},
{day:76, label:"Day 76 — Mon", subjects:[
  {subject:"Language", title:"Making Connections: Text to Self", summary:"Students learn to make text-to-self connections by relating events or feelings in a story to their own life experiences, which helps deepen understanding of what they read.",
   resourceLabel:"YouTube: Making Connections: Text to Self", resourceUrl:"https://www.youtube.com/results?search_query=Making%20Connections%3A%20Text%20to%20Self%20grade%202%20educational",
   quiz:[
     {q:"What do we call connecting a story to something in your own life?", options:["A caption","A rhyme","A summary","A text-to-self connection"], answer:3},
     {q:"Why might a reader make a text-to-self connection while reading?", options:["It removes all the pictures","It changes the ending of the story","It helps them understand the story more deeply","It makes the book disappear"], answer:2},
     {q:"Which is an example of a text-to-self connection?", options:["This book was written by a famous author.","This book has ten chapters.","This book has a red cover.","This story reminds me of the time I lost my favourite toy."], answer:3},
     {q:"Making connections while reading can help a reader ___.", options:["Read more slowly with no purpose","Skip the whole book","Understand and remember a story better","Forget the story completely"], answer:2},
     {q:"A text-to-self connection links a story to ___.", options:["Something the reader has experienced in their own life","The title of another book","A math equation","A map of the world"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call connecting a story to something in your own life?", answers:["a text-to-self connection","text-to-self connection"]},
     {prompt:"Why do readers make text-to-self connections?", answers:["to understand the story better","to deepen understanding","it helps understanding"]},
     {prompt:"Name one thing a reader might connect a story to, like a memory or a feeling.", answers:["a memory","a feeling","an experience"]}
   ]},
  {subject:"Math", title:"Faces, Edges, and Vertices of 3D Shapes", summary:"Students learn to identify and count the flat faces, straight edges, and pointed vertices of three-dimensional shapes, such as cubes and pyramids.",
   resourceLabel:"YouTube: Faces, Edges, and Vertices of 3D Shapes", resourceUrl:"https://www.youtube.com/results?search_query=Faces%2C%20Edges%2C%20and%20Vertices%20of%203D%20Shapes%20grade%202%20educational",
   quiz:[
     {q:"How many faces does a cube have?", options:["12","6","8","4"], answer:1},
     {q:"What do we call the corner point where edges of a 3D shape meet?", options:["A base","A face","An edge","A vertex"], answer:3},
     {q:"How many edges does a cube have?", options:["6","12","10","8"], answer:1},
     {q:"What do we call a flat surface on a 3D shape?", options:["A face","An edge","A line","A vertex"], answer:0},
     {q:"How many vertices does a cube have?", options:["6","12","8","4"], answer:2}
   ],
   worksheet:[
     {prompt:"How many faces does a cube have?", answers:["6"]},
     {prompt:"What do we call the corner point where edges of a 3D shape meet?", answers:["a vertex","vertex","corner"]},
     {prompt:"How many edges does a cube have?", answers:["12"]}
   ]},
  {subject:"Science", title:"Stars and Constellations", summary:"Students learn that stars are giant balls of hot gas that give off their own light, and that a constellation is a group of stars that forms a pattern in the night sky.",
   resourceLabel:"YouTube: Stars and Constellations", resourceUrl:"https://www.youtube.com/results?search_query=Stars%20and%20Constellations%20grade%202%20educational",
   quiz:[
     {q:"What do we call a giant ball of hot gas that gives off its own light in space?", options:["A star","A moon","A planet","A comet"], answer:0},
     {q:"What do we call a group of stars that forms a pattern in the night sky?", options:["A constellation","An orbit","A galaxy","An eclipse"], answer:0},
     {q:"Which of these is an example of a constellation?", options:["Earth","The moon","The sun","The Big Dipper"], answer:3},
     {q:"Stars appear to twinkle in the night sky because ___.", options:["Their light travels through moving air in our atmosphere","They are actually moving very slowly across the sky","They are very close to Earth","They turn on and off"], answer:0},
     {q:"When is it easiest to see stars in the sky?", options:["During a thunderstorm","At noon on a sunny day","At night, away from bright city lights","Only in the summer"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a giant ball of hot gas that gives off its own light in space?", answers:["a star","star"]},
     {prompt:"What do we call a group of stars that forms a pattern in the sky?", answers:["a constellation","constellation"]},
     {prompt:"Name one famous constellation, like the Big Dipper.", answers:["the big dipper","big dipper","orion"]}
   ]},
  {subject:"SocialStudies", title:"Famous Landmarks Around the World", summary:"Students learn about famous landmarks from other countries, such as the Eiffel Tower in France and the Great Wall in China, and how landmarks help people recognize and remember a place.",
   resourceLabel:"YouTube: Famous Landmarks Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Famous%20Landmarks%20Around%20the%20World%20grade%202%20educational",
   quiz:[
     {q:"In which country would you find the Eiffel Tower?", options:["Canada","France","Egypt","China"], answer:1},
     {q:"In which country would you find the Great Wall?", options:["Egypt","China","Canada","France"], answer:1},
     {q:"What do we call a well-known structure or place that helps people recognize a location?", options:["A government","A province","A landmark","A currency"], answer:2},
     {q:"Why are famous landmarks important to a country?", options:["They have no meaning at all","They stop tourists from visiting","They help represent the culture and history of a place","They are only used for parking"], answer:2},
     {q:"Which of these is an example of a famous landmark?", options:["A random empty field","An ordinary street sign","The Great Wall","A plain brick wall"], answer:2}
   ],
   worksheet:[
     {prompt:"In which country would you find the Eiffel Tower?", answers:["france"]},
     {prompt:"In which country would you find the Great Wall?", answers:["china"]},
     {prompt:"What do we call a well-known structure or place that helps people recognize a location?", answers:["a landmark","landmark"]}
   ]},
]},
{day:77, label:"Day 77 — Tue", subjects:[
  {subject:"Language", title:"Summarizing a Story in a Few Sentences", summary:"Students learn to summarize a story by telling the most important events in just a few sentences, leaving out small details that are not essential to the main plot.",
   resourceLabel:"YouTube: Summarizing a Story in a Few Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Summarizing%20a%20Story%20in%20a%20Few%20Sentences%20grade%202%20educational",
   quiz:[
     {q:"What does it mean to summarize a story?", options:["To tell the most important events in a few sentences","To draw a picture instead of writing","To read the story out loud","To copy the whole story word for word"], answer:0},
     {q:"A good summary should include ___.", options:["Only the most important events","Every single detail from the story","No events at all","Only the title of the story"], answer:0},
     {q:"Which of these is closest to a summary of a story about a lost dog?", options:["A dog gets lost, a family searches, and they find the dog.","Dogs are mammals with four legs.","The author lives in Ontario.","The cover of the book is blue."], answer:0},
     {q:"Why might a student summarize a chapter before starting a new one?", options:["To make the chapter longer","To change the ending","To remember what happened so far","To forget the story completely"], answer:2},
     {q:"A summary is usually ___ than the original story.", options:["Exactly the same length","Written only in pictures","Much shorter","Much longer"], answer:2}
   ],
   worksheet:[
     {prompt:"What does it mean to summarize a story?", answers:["to tell the most important events in a few sentences","to tell the main events briefly","retelling the main events shortly"]},
     {prompt:"Should a summary include every small detail or just the most important events?", answers:["the most important events","just the most important events"]},
     {prompt:"Why is summarizing a story a useful skill?", answers:["it helps readers remember the main events","it helps understanding","to check understanding of the story"]}
   ]},
  {subject:"Math", title:"Quarter Past and Quarter To: Telling Time in Detail", summary:"Students learn to read clocks that show quarter past the hour, when the minute hand points to the 3, and quarter to the hour, when the minute hand points to the 9.",
   resourceLabel:"YouTube: Quarter Past and Quarter To: Telling Time in Detail", resourceUrl:"https://www.youtube.com/results?search_query=Quarter%20Past%20and%20Quarter%20To%3A%20Telling%20Time%20in%20Detail%20grade%202%20educational",
   quiz:[
     {q:"When the minute hand points to the 3, what time is it, quarter past or quarter to the hour?", options:["Quarter past","Half past","Quarter to","On the hour"], answer:0},
     {q:"When the minute hand points to the 9, what time is it?", options:["On the hour","Half past the hour","Quarter past the hour","Quarter to the next hour"], answer:3},
     {q:"How many minutes are in a quarter of an hour?", options:["30","15","10","45"], answer:1},
     {q:"If it is quarter past 4, where does the minute hand point?", options:["The 12","The 6","The 9","The 3"], answer:3},
     {q:"If it is quarter to 5, how many minutes remain until the hour of 5?", options:["15","45","30","10"], answer:0}
   ],
   worksheet:[
     {prompt:"When the minute hand points to the 3, what do we call that time, quarter past or quarter to?", answers:["quarter past"]},
     {prompt:"When the minute hand points to the 9, what do we call that time?", answers:["quarter to"]},
     {prompt:"How many minutes are in a quarter of an hour?", answers:["15"]}
   ]},
  {subject:"Science", title:"Animal Life Spans: How Long Animals Live", summary:"Students learn that different animals have different life spans, the length of time they typically live, such as a mouse living only a few years while a tortoise can live over one hundred years.",
   resourceLabel:"YouTube: Animal Life Spans: How Long Animals Live", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Life%20Spans%3A%20How%20Long%20Animals%20Live%20grade%202%20educational",
   quiz:[
     {q:"What word describes the length of time an animal typically lives?", options:["Camouflage","Migration","Habitat","Life span"], answer:3},
     {q:"Which of these animals is known for having a very long life span?", options:["A mayfly","A housefly","A tortoise","A mouse"], answer:2},
     {q:"Does a small mouse usually have a longer or shorter life span than a large tortoise?", options:["Longer","Exactly the same","Shorter","Mice do not have a life span"], answer:2},
     {q:"Which of these could affect how long an animal lives?", options:["The colour of the sky","The season only","The day of the week","Its size, habitat, and species"], answer:3},
     {q:"Learning about animal life spans helps scientists understand ___.", options:["How long different animals typically live","How to tell time","How to build a house","How to bake bread"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes the length of time an animal typically lives?", answers:["life span","a life span"]},
     {prompt:"Name one animal that has a very long life span, like a tortoise.", answers:["a tortoise","tortoise","an elephant","elephant"]},
     {prompt:"Does a mouse usually have a longer or shorter life span than a tortoise?", answers:["shorter"]}
   ]},
  {subject:"SocialStudies", title:"Reading a Map Legend: Symbols and Keys", summary:"Students learn that a map legend, also called a key, explains what the symbols and colours on a map represent, such as a blue line for a river or a green square for a park.",
   resourceLabel:"YouTube: Reading a Map Legend: Symbols and Keys", resourceUrl:"https://www.youtube.com/results?search_query=Reading%20a%20Map%20Legend%3A%20Symbols%20and%20Keys%20grade%202%20educational",
   quiz:[
     {q:"What do we call the part of a map that explains what symbols and colours represent?", options:["A border","A scale","A legend","A compass"], answer:2},
     {q:"What might a blue line on a map most likely represent?", options:["A road","A desert","A mountain","A river or body of water"], answer:3},
     {q:"Why is a map legend useful to someone reading a map?", options:["It changes the size of the map","It explains what the symbols and colours mean","It tells you the time of day","It removes all symbols from the map"], answer:1},
     {q:"If a map legend shows a green square means a park, what does a green square on the map represent?", options:["A park","A school","A river","A hospital"], answer:0},
     {q:"A map legend is also sometimes called a ___.", options:["Key","Border","Compass rose","Scale bar"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the part of a map that explains what symbols and colours represent?", answers:["a legend","legend","a key","key"]},
     {prompt:"What might a blue line on a map represent?", answers:["a river","river","water"]},
     {prompt:"Why is a map legend useful?", answers:["it explains what the symbols mean","it helps readers understand the map","to understand map symbols"]}
   ]},
]},
{day:78, label:"Day 78 — Wed", subjects:[
  {subject:"Language", title:"Editing Your Writing: Checking for Mistakes", summary:"Students learn that editing means rereading their writing to check for and fix mistakes in spelling, punctuation, and capital letters before sharing a finished piece.",
   resourceLabel:"YouTube: Editing Your Writing: Checking for Mistakes", resourceUrl:"https://www.youtube.com/results?search_query=Editing%20Your%20Writing%3A%20Checking%20for%20Mistakes%20grade%202%20educational",
   quiz:[
     {q:"What do we call rereading writing to check for and fix mistakes?", options:["Editing","Skipping","Illustrating","Publishing"], answer:0},
     {q:"Which of these is something a writer checks for while editing?", options:["Spelling and punctuation","The size of the desk","The colour of the paper","The time of day"], answer:0},
     {q:"When should editing usually happen during the writing process?", options:["After a first draft is written, before sharing the final piece","Never, editing is not needed","Before any writing begins","Only after the piece is published"], answer:0},
     {q:"Which sentence needs editing because of a capitalization mistake?", options:["my dog likes to run in the park.","She has a small dog.","The dog ran fast.","My dog likes to run in the park."], answer:0},
     {q:"Editing helps a writer ___.", options:["Ignore spelling completely","Add random mistakes on purpose","Erase the whole piece of writing","Make their writing clearer and more correct"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call rereading writing to check for and fix mistakes?", answers:["editing","edit"]},
     {prompt:"Name one thing a writer checks for while editing, like spelling or punctuation.", answers:["spelling","punctuation","capital letters"]},
     {prompt:"Why is editing an important step in writing?", answers:["to fix mistakes","to make writing clearer","it helps writing become clearer"]}
   ]},
  {subject:"Math", title:"Estimating Sums and Differences", summary:"Students learn to estimate a sum or difference by rounding numbers before adding or subtracting, which gives a quick, reasonable answer without exact calculation.",
   resourceLabel:"YouTube: Estimating Sums and Differences", resourceUrl:"https://www.youtube.com/results?search_query=Estimating%20Sums%20and%20Differences%20grade%202%20educational",
   quiz:[
     {q:"What do we do to numbers before estimating a sum?", options:["Divide them in half","Multiply them by ten","Round them to a nearby ten","Ignore them completely"], answer:2},
     {q:"Estimate the sum of 42 and 39 by rounding each to the nearest ten first.", options:["60","70","80","90"], answer:2},
     {q:"Estimate the difference of 81 and 19 by rounding each to the nearest ten first.", options:["60","40","70","50"], answer:0},
     {q:"Why might someone estimate before solving an exact math problem?", options:["To quickly check if the exact answer seems reasonable","To make the problem harder","To avoid all math forever","To get a random answer"], answer:0},
     {q:"An estimate is ___.", options:["Never useful in math","Always the exact answer","Always wrong","A close, reasonable answer found by rounding"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we do to numbers before estimating a sum?", answers:["round them","round the numbers"]},
     {prompt:"Estimate the sum of 42 and 39 by rounding each to the nearest ten first.", answers:["80"]},
     {prompt:"Why is estimating a useful skill?", answers:["it gives a quick reasonable answer","to check if an exact answer makes sense","it helps check work quickly"]}
   ]},
  {subject:"Science", title:"Renewable and Nonrenewable Energy Sources", summary:"Students learn that renewable energy sources, like sunlight and wind, can be used again and again without running out, while nonrenewable energy sources, like coal and oil, take millions of years to form and can run out.",
   resourceLabel:"YouTube: Renewable and Nonrenewable Energy Sources", resourceUrl:"https://www.youtube.com/results?search_query=Renewable%20and%20Nonrenewable%20Energy%20Sources%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a renewable energy source?", options:["Coal","Sunlight","Natural gas","Oil"], answer:1},
     {q:"Which of these is a nonrenewable energy source?", options:["Water","Wind","Coal","Sunlight"], answer:2},
     {q:"What does it mean for an energy source to be renewable?", options:["It takes millions of years to form","It runs out after one use","It cannot be used at all","It can be used again and again without running out"], answer:3},
     {q:"Why do many scientists encourage using more renewable energy?", options:["Because it is always more expensive","Because it never produces any energy","Because it is illegal to use nonrenewable energy","Because it will not run out like nonrenewable sources can"], answer:3},
     {q:"Wind turbines and solar panels are used to capture ___.", options:["Renewable energy from wind and sunlight","Energy from ocean salt only","Nonrenewable energy from coal","Energy from underground oil"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one renewable energy source, like the sun or wind.", answers:["the sun","sun","wind","water"]},
     {prompt:"Name one nonrenewable energy source, like coal or oil.", answers:["coal","oil"]},
     {prompt:"Which type of energy source can run out, renewable or nonrenewable?", answers:["nonrenewable"]}
   ]},
  {subject:"SocialStudies", title:"Fair Play: Following Rules When We Play", summary:"Students learn that fair play means following the rules of a game, taking turns, and treating others with respect, whether a team wins or loses.",
   resourceLabel:"YouTube: Fair Play: Following Rules When We Play", resourceUrl:"https://www.youtube.com/results?search_query=Fair%20Play%3A%20Following%20Rules%20When%20We%20Play%20grade%202%20educational",
   quiz:[
     {q:"What do we call following the rules of a game and treating others with respect?", options:["Fair play","Arguing","Cheating","Ignoring the rules"], answer:0},
     {q:"Which of these is an example of fair play?", options:["Cheating to win","Yelling at teammates","Breaking the rules on purpose","Taking turns and following the rules"], answer:3},
     {q:"How should players treat each other after a game, whether they win or lose?", options:["With respect and good sportsmanship","By ignoring the other team","By breaking the rules","With anger"], answer:0},
     {q:"Why is fair play important in games and sports?", options:["It lets one team cheat","It helps everyone enjoy the game and be treated fairly","It makes the game longer","It stops anyone from playing"], answer:1},
     {q:"Which of these shows good sportsmanship after losing a game?", options:["Blaming a teammate unfairly","Breaking the game equipment","Yelling and refusing to shake hands","Congratulating the other team"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call following the rules of a game and treating others with respect?", answers:["fair play"]},
     {prompt:"Name one example of fair play, like taking turns.", answers:["taking turns","following the rules","sharing"]},
     {prompt:"How should players treat each other whether their team wins or loses?", answers:["with respect","fairly","kindly"]}
   ]},
]},
{day:79, label:"Day 79 — Thu", subjects:[
  {subject:"Language", title:"Word Choice: How Writers Choose Strong Words", summary:"Students learn that writers choose strong, specific words on purpose, such as replacing happy with thrilled, to create a clearer picture and stronger feeling for the reader.",
   resourceLabel:"YouTube: Word Choice: How Writers Choose Strong Words", resourceUrl:"https://www.youtube.com/results?search_query=Word%20Choice%3A%20How%20Writers%20Choose%20Strong%20Words%20grade%202%20educational",
   quiz:[
     {q:"What do we call the specific words a writer chooses on purpose to create an effect?", options:["A title","Punctuation","Word choice","A caption"], answer:2},
     {q:"Which word is a stronger, more specific choice than the word happy?", options:["Fine","Thrilled","Nice","Good"], answer:1},
     {q:"Why might a writer replace the word big with enormous?", options:["To remove all meaning","To make the word shorter","To make the sentence confusing","To create a stronger, clearer picture for the reader"], answer:3},
     {q:"Which sentence uses the strongest word choice?", options:["The dinosaur moved.","The big dinosaur walked.","A dinosaur was there.","The enormous dinosaur stomped through the forest."], answer:3},
     {q:"Strong word choice helps writing become ___.", options:["Harder to understand","Completely silent","More vivid and interesting for the reader","Shorter than a single word"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the specific words a writer chooses on purpose?", answers:["word choice"]},
     {prompt:"Which is a stronger word choice than happy: glad or thrilled?", answers:["thrilled"]},
     {prompt:"Why do writers choose strong, specific words?", answers:["to create a clearer picture","to make writing more interesting","to give the reader a stronger feeling"]}
   ]},
  {subject:"Math", title:"Venn Diagrams: Sorting Objects by Attributes", summary:"Students learn to use a Venn diagram, two overlapping circles, to sort objects by shared and different attributes, placing items that share both attributes in the overlapping middle section.",
   resourceLabel:"YouTube: Venn Diagrams: Sorting Objects by Attributes", resourceUrl:"https://www.youtube.com/results?search_query=Venn%20Diagrams%3A%20Sorting%20Objects%20by%20Attributes%20grade%202%20educational",
   quiz:[
     {q:"What do we call a diagram with two overlapping circles used to sort objects?", options:["A Venn diagram","A bar graph","A line plot","A tally chart"], answer:0},
     {q:"Where do we place an object that shares both attributes in a Venn diagram?", options:["Only in the left circle","In the overlapping middle section","Only in the right circle","Outside both circles"], answer:1},
     {q:"Which of these could be an attribute used to sort shapes in a Venn diagram?", options:["The weather today","The time of day","Number of sides","A favourite song"], answer:2},
     {q:"If a shape is red and has four sides, and the circles show red shapes and four-sided shapes, where does it go?", options:["Only in the red circle","Only in the four-sided circle","In the overlapping middle section","Outside both circles"], answer:2},
     {q:"A Venn diagram helps us understand ___.", options:["How to add two numbers","How to measure temperature","How to tell time","How groups of objects are similar and different"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call a diagram with two overlapping circles used to sort objects?", answers:["a venn diagram","venn diagram"]},
     {prompt:"Where do we place an object that fits into both circles of a Venn diagram?", answers:["in the overlapping middle section","the middle","in the middle"]},
     {prompt:"Name one attribute we might use to sort shapes in a Venn diagram, like colour or number of sides.", answers:["colour","number of sides","shape","size"]}
   ]},
  {subject:"Science", title:"Scientific Method: Asking Questions and Testing Ideas", summary:"Students learn that scientists use the scientific method, a set of steps that includes asking a question, making a prediction, testing the idea, and recording what happens, to learn about the world.",
   resourceLabel:"YouTube: Scientific Method: Asking Questions and Testing Ideas", resourceUrl:"https://www.youtube.com/results?search_query=Scientific%20Method%3A%20Asking%20Questions%20and%20Testing%20Ideas%20grade%202%20educational",
   quiz:[
     {q:"What is usually the first step of the scientific method?", options:["Building a robot","Recording results","Skipping the test","Asking a question"], answer:3},
     {q:"What do we call the guess a scientist makes about what will happen before testing an idea?", options:["A constellation","A habitat","A fossil","A prediction"], answer:3},
     {q:"Why do scientists test their ideas?", options:["To skip recording results","To see if their prediction was correct","To avoid learning anything new","To make the question disappear"], answer:1},
     {q:"Why is it important for scientists to record what happens during a test?", options:["So no one else can see the results","So they can remember and learn from the results","So they can forget the test happened","So the test becomes a secret"], answer:1},
     {q:"Using the scientific method helps scientists ___.", options:["Ignore what they observe","Guess randomly with no testing","Avoid asking any questions","Learn about the world in a careful, organized way"], answer:3}
   ],
   worksheet:[
     {prompt:"What is the first step of the scientific method, before testing an idea?", answers:["asking a question","ask a question"]},
     {prompt:"What do we call the guess a scientist makes about what will happen before testing an idea?", answers:["a prediction","prediction"]},
     {prompt:"Why do scientists record what happens during a test?", answers:["to remember the results","to see what happened","to learn from the results"]}
   ]},
  {subject:"SocialStudies", title:"How People Told Time Before Clocks and Watches", summary:"Students learn that before mechanical clocks and watches were common, people told time using tools like sundials, which used the position of the sun shadow, and hourglasses filled with falling sand.",
   resourceLabel:"YouTube: How People Told Time Before Clocks and Watches", resourceUrl:"https://www.youtube.com/results?search_query=How%20People%20Told%20Time%20Before%20Clocks%20and%20Watches%20grade%202%20educational",
   quiz:[
     {q:"What tool used the position of a shadow from the sun to tell time?", options:["A thermometer","A sundial","A compass","A calendar"], answer:1},
     {q:"What tool used falling sand to measure time?", options:["A globe","An hourglass","A map","A sundial"], answer:1},
     {q:"Why did a sundial stop working well at night?", options:["Clocks needed batteries","The moon was too bright","Sand ran out","There was no sunlight to make a shadow"], answer:3},
     {q:"Before alarm clocks, what natural event often helped people know it was time to wake up?", options:["The sunrise","A thunderstorm","A rainbow","A full moon"], answer:0},
     {q:"Learning about tools like sundials and hourglasses helps us understand ___.", options:["How to travel by airplane","How to build a computer","How to grow food","How people measured time long ago before modern clocks"], answer:3}
   ],
   worksheet:[
     {prompt:"What tool used the position of a shadow from the sun to tell time?", answers:["a sundial","sundial"]},
     {prompt:"What tool used falling sand to measure time?", answers:["an hourglass","hourglass"]},
     {prompt:"Name one way people long ago knew it was time to wake up without an alarm clock, like the sunrise.", answers:["the sunrise","sunrise","a rooster crowing","rooster crowing"]}
   ]},
]},
{day:80, label:"Day 80 — Fri", subjects:[
  {subject:"Language", title:"Final Review: Language Skills (Days 71-79)", summary:"Students review Language skills from Days 71 to 79: similes, prepositions, interjections, persuasive writing, nonfiction text features, making connections, summarizing, editing, and word choice.",
   resourceLabel:"YouTube: Final Review: Language Skills (Days 71-79)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Language%20Skills%20%28Days%2071-79%29%20grade%202%20educational",
   quiz:[
     {q:"What do we call a phrase that compares two things using like or as?", options:["A caption","A synonym","A simile","An antonym"], answer:2},
     {q:"What do we call a word that shows the position of one thing compared to another?", options:["A verb","A pronoun","A preposition","An adjective"], answer:2},
     {q:"What do we call a short word or phrase that expresses strong feeling?", options:["A synonym","An interjection","A pronoun","A preposition"], answer:1},
     {q:"What is the main goal of persuasive writing?", options:["To tell what time it is","To convince the reader to agree with an idea","To list random facts","To describe a setting only"], answer:1},
     {q:"What do we call rereading writing to check for and fix mistakes?", options:["Illustrating","Skipping","Editing","Publishing"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a phrase that compares two things using like or as?", answers:["a simile","simile"]},
     {prompt:"What do we call a word that shows the position of one thing compared to another, like under or beside?", answers:["a preposition","preposition"]},
     {prompt:"What do we call rereading writing to check for and fix mistakes?", answers:["editing","edit"]}
   ]},
  {subject:"Math", title:"Final Review: Math Skills (Days 71-79)", summary:"Students review Math skills from Days 71 to 79: three-digit addition and subtraction with regrouping, multiplication facts for 3s and 4s, fractions of a group, comparing fractions, 3D shape attributes, quarter past and quarter to, estimating sums and differences, and Venn diagrams.",
   resourceLabel:"YouTube: Final Review: Math Skills (Days 71-79)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Math%20Skills%20%28Days%2071-79%29%20grade%202%20educational",
   quiz:[
     {q:"What is 236 + 148?", options:["374","394","384","284"], answer:2},
     {q:"What is 342 - 158?", options:["184","284","174","194"], answer:0},
     {q:"What is 3 times 4?", options:["10","16","12","14"], answer:2},
     {q:"Which is greater, one half or one quarter?", options:["They are equal","One half","One quarter","Cannot tell"], answer:1},
     {q:"How many faces does a cube have?", options:["12","6","8","4"], answer:1}
   ],
   worksheet:[
     {prompt:"What is 236 + 148?", answers:["384"]},
     {prompt:"What is 3 times 4?", answers:["12"]},
     {prompt:"How many faces does a cube have?", answers:["6"]}
   ]},
  {subject:"Science", title:"Final Review: Science Skills (Days 71-79)", summary:"Students review Science topics from Days 71 to 79: parts of a plant, levers, the heart, digestion, precipitation, stars and constellations, animal life spans, renewable and nonrenewable energy, and the scientific method.",
   resourceLabel:"YouTube: Final Review: Science Skills (Days 71-79)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Science%20Skills%20%28Days%2071-79%29%20grade%202%20educational",
   quiz:[
     {q:"Which part of a plant absorbs water from the soil?", options:["The leaves","The roots","The flower","The stem"], answer:1},
     {q:"What do we call the fixed point that a lever rests on?", options:["A pulley","A fulcrum","An axle","A wedge"], answer:1},
     {q:"What organ pumps blood through the body?", options:["The lungs","The heart","The brain","The stomach"], answer:1},
     {q:"What word describes water that falls from clouds in different forms?", options:["Condensation","Evaporation","Pollination","Precipitation"], answer:3},
     {q:"What do we call a group of stars that forms a pattern in the night sky?", options:["A constellation","An eclipse","A galaxy","An orbit"], answer:0}
   ],
   worksheet:[
     {prompt:"Which part of a plant absorbs water from the soil?", answers:["the roots","roots"]},
     {prompt:"What organ pumps blood through the body?", answers:["the heart","heart"]},
     {prompt:"What word describes water that falls from clouds in different forms?", answers:["precipitation"]}
   ]},
  {subject:"SocialStudies", title:"Final Review: Social Studies Skills (Days 71-79)", summary:"Students review Social Studies topics from Days 71 to 79: where products come from, advertising, levels of government, Canadian holidays, family heritage, world landmarks, map legends, fair play, and how people told time long ago.",
   resourceLabel:"YouTube: Final Review: Social Studies Skills (Days 71-79)", resourceUrl:"https://www.youtube.com/results?search_query=Final%20Review%3A%20Social%20Studies%20Skills%20%28Days%2071-79%29%20grade%202%20educational",
   quiz:[
     {q:"Where are many clothes and toys made before they reach a store?", options:["A lake","A forest","A farm only","A factory"], answer:3},
     {q:"What do we call a message created by a company to convince people to buy a product?", options:["A weather report","A biography","A map","An advertisement"], answer:3},
     {q:"What do we call the level of government that looks after a town or city?", options:["Municipal government","No government","Provincial government","Federal government"], answer:0},
     {q:"On what date is Canada Day celebrated?", options:["December 25th","January 1st","November 11th","July 1st"], answer:3},
     {q:"What do we call the part of a map that explains what symbols and colours represent?", options:["A legend","A scale","A border","A compass"], answer:0}
   ],
   worksheet:[
     {prompt:"Where are many clothes and toys made before they reach a store?", answers:["a factory","factory","factories"]},
     {prompt:"What do we call the level of government that looks after a town or city?", answers:["municipal government","municipal"]},
     {prompt:"On what date is Canada Day celebrated?", answers:["july 1","july 1st"]}
   ]},
]},
{day:81, label:"Day 81 — Mon", subjects:[
  {subject:"Language", title:"Compound Sentences: Joining Ideas with Or and So", summary:"Students learn that two related sentences can be joined into one compound sentence using the joining words or or so, such as combining You can walk and You can bike into You can walk or you can bike.",
   resourceLabel:"YouTube: Compound Sentences: Joining Ideas with Or and So", resourceUrl:"https://www.youtube.com/results?search_query=Compound%20Sentences%3A%20Joining%20Ideas%20with%20Or%20and%20So%20grade%202%20educational",
   quiz:[
     {q:"Which word can join two sentences to show a choice?", options:["A","Or","The","An"], answer:1},
     {q:"Which word can join two sentences to show a result?", options:["So","Or","A","The"], answer:0},
     {q:"Which sentence correctly joins two ideas with so?", options:["It was cold wore I a coat so.","It was cold, so I wore a coat.","It was cold I wore a coat so.","So cold it was, I wore a coat."], answer:1},
     {q:"Why might a writer combine two short sentences into one compound sentence?", options:["It can make writing flow more smoothly","This concept has no connection to writing","Short sentences should never be combined","Combining sentences always makes writing confusing"], answer:0},
     {q:"Which sentence correctly joins two ideas with or?", options:["Or juice milk have can you.","Juice milk or you can have you can have.","You can have juice or you can have milk.","You can have juice you can have milk or."], answer:2}
   ],
   worksheet:[
     {prompt:"Name a joining word that can combine two sentences, like or or so.", answers:["or","so"]},
     {prompt:"Join these ideas with so: It was raining. We stayed inside.", answers:["It was raining, so we stayed inside.","It was raining so we stayed inside"]},
     {prompt:"Does joining two related sentences with or or so make one longer sentence?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Multiplication Facts: 6s and 7s", summary:"Students practise and memorize multiplication facts for the 6 and 7 times tables, building on earlier work with the 2s, 3s, 4s, 5s, and 10s times tables.",
   resourceLabel:"YouTube: Multiplication Facts: 6s and 7s", resourceUrl:"https://www.youtube.com/results?search_query=Multiplication%20Facts%3A%206s%20and%207s%20grade%202%20educational",
   quiz:[
     {q:"What is 6 times 4?", options:["24","28","20","18"], answer:0},
     {q:"What is 7 times 3?", options:["24","21","14","18"], answer:1},
     {q:"What is 6 times 5?", options:["35","30","25","20"], answer:1},
     {q:"What is 7 times 5?", options:["35","25","40","30"], answer:0},
     {q:"What is 6 times 7?", options:["35","42","48","36"], answer:1}
   ],
   worksheet:[
     {prompt:"What is 6 times 3?", answers:["18","eighteen"]},
     {prompt:"What is 7 times 2?", answers:["14","fourteen"]},
     {prompt:"What is 6 times 6?", answers:["36","thirty-six"]}
   ]},
  {subject:"Science", title:"Our Skeleton and Joints: How We Bend and Move", summary:"Students learn that our skeleton is made of bones that support our body, and that joints, such as our elbows and knees, are the places where two bones meet and allow us to bend and move.",
   resourceLabel:"YouTube: Our Skeleton and Joints: How We Bend and Move", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Skeleton%20and%20Joints%3A%20How%20We%20Bend%20and%20Move%20grade%202%20educational",
   quiz:[
     {q:"What do we call the places where two bones meet?", options:["Veins","Muscles","Joints","Nerves"], answer:2},
     {q:"Which of these is an example of a joint in the body?", options:["The hair","The knee","The skin","The tongue"], answer:1},
     {q:"Why are joints important for how our body moves?", options:["Joints only exist to hold blood","Bones can bend anywhere without joints","They allow our bones to bend at certain points","Joints have no connection to movement"], answer:2},
     {q:"What is our skeleton made of?", options:["Only blood","Bones","Only muscle","Only skin"], answer:1},
     {q:"Our skeleton is best described as the structure that ___ our body.", options:["Feeds","Supports","Colours","Waters"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call the places where two bones meet and allow us to bend?", answers:["joints"]},
     {prompt:"Name one joint in your body, like your elbow or knee.", answers:["elbow","knee"]},
     {prompt:"Does our skeleton help support our whole body?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"How Laws Are Made and Enforced", summary:"Students learn that laws are made by elected governments to keep people safe and treated fairly, and that police and courts help make sure laws are followed and enforced.",
   resourceLabel:"YouTube: How Laws Are Made and Enforced", resourceUrl:"https://www.youtube.com/results?search_query=How%20Laws%20Are%20Made%20and%20Enforced%20grade%202%20educational",
   quiz:[
     {q:"Who is responsible for making laws?", options:["Only children","Elected governments","No one at all","A single random citizen"], answer:1},
     {q:"Which of these helps enforce laws in a community?", options:["Police officers","Bakers","Artists","Farmers"], answer:0},
     {q:"Why are laws important for a community?", options:["Laws have no real purpose","Laws only benefit one single person","They help keep people safe and treated fairly","Communities function better without any laws"], answer:2},
     {q:"What might happen if a community had no laws at all?", options:["Nothing would change at all","People could be treated unfairly or unsafely","Laws have no connection to safety","Communities always run better without laws"], answer:1},
     {q:"Courts help make sure that laws are ___.", options:["Followed fairly","Ignored completely","Written by only one person","Never enforced"], answer:0}
   ],
   worksheet:[
     {prompt:"Who helps make laws for a country or province?", answers:["government","elected government"]},
     {prompt:"Name one group that helps make sure laws are followed, like police or courts.", answers:["police","courts"]},
     {prompt:"Do laws help keep people safe and treated fairly?", answers:["yes"]}
   ]},
]},
{day:82, label:"Day 82 — Tue", subjects:[
  {subject:"Language", title:"Figurative Language: Metaphors", summary:"Students learn that a metaphor describes one thing by saying it is another thing, without using like or as, such as saying the classroom was a zoo to describe a noisy room.",
   resourceLabel:"YouTube: Figurative Language: Metaphors", resourceUrl:"https://www.youtube.com/results?search_query=Figurative%20Language%3A%20Metaphors%20grade%202%20educational",
   quiz:[
     {q:"What is a metaphor?", options:["A sentence with no comparison at all","A comparison that always uses like or as","A type of punctuation mark","A comparison that says one thing is another thing"], answer:3},
     {q:"Which of these sentences is a metaphor?", options:["The playground was a beehive of activity.","The playground was empty today.","The playground was as busy as a beehive.","The playground had many students."], answer:0},
     {q:"What does the metaphor time is money suggest?", options:["Time can be spent like real coins","Time has no value at all","Money and time have no connection","Time is valuable, like money"], answer:3},
     {q:"How is a metaphor different from a simile?", options:["A simile never makes any comparison","A metaphor and a simile are exactly the same thing","A metaphor does not use like or as, while a simile does","A metaphor always uses like or as"], answer:2},
     {q:"Why might an author use a metaphor in their writing?", options:["Metaphors are never used by authors","Metaphors make writing less interesting","Metaphors have no purpose in writing","To create a vivid picture in the readers mind"], answer:3}
   ],
   worksheet:[
     {prompt:"Does a metaphor use the words like or as?", answers:["no"]},
     {prompt:"What does the metaphor the classroom was a zoo suggest about the classroom?", answers:["it was noisy or chaotic","noisy"]},
     {prompt:"Is the sentence Her smile was as bright as the sun a metaphor or a simile?", answers:["simile"]}
   ]},
  {subject:"Math", title:"Division Facts: Related to Multiplication", summary:"Students learn that division facts are closely related to multiplication facts, such as knowing that if 6 times 4 equals 24, then 24 divided by 6 equals 4.",
   resourceLabel:"YouTube: Division Facts: Related to Multiplication", resourceUrl:"https://www.youtube.com/results?search_query=Division%20Facts%3A%20Related%20to%20Multiplication%20grade%202%20educational",
   quiz:[
     {q:"If 4 times 5 equals 20, what does 20 divided by 4 equal?", options:["5","20","10","4"], answer:0},
     {q:"If 3 times 6 equals 18, what does 18 divided by 3 equal?", options:["18","9","3","6"], answer:3},
     {q:"If 8 times 2 equals 16, what does 16 divided by 8 equal?", options:["8","4","2","16"], answer:2},
     {q:"Knowing multiplication facts can help us solve ___ facts.", options:["Only fraction","Subtraction","Division","Addition"], answer:2},
     {q:"If 9 times 3 equals 27, what does 27 divided by 9 equal?", options:["27","3","9","6"], answer:1}
   ],
   worksheet:[
     {prompt:"If 6 times 4 equals 24, what does 24 divided by 6 equal?", answers:["4","four"]},
     {prompt:"If 5 times 3 equals 15, what does 15 divided by 5 equal?", answers:["3","three"]},
     {prompt:"If 7 times 2 equals 14, what does 14 divided by 7 equal?", answers:["2","two"]}
   ]},
  {subject:"Science", title:"Deserts: Life in a Dry Habitat", summary:"Students learn that a desert is a very dry habitat that gets little rain, and that plants and animals living there, such as cacti and camels, have special features to survive with little water.",
   resourceLabel:"YouTube: Deserts: Life in a Dry Habitat", resourceUrl:"https://www.youtube.com/results?search_query=Deserts%3A%20Life%20in%20a%20Dry%20Habitat%20grade%202%20educational",
   quiz:[
     {q:"What kind of habitat is a desert?", options:["A very dry habitat with little rain","A cold, icy habitat","A very wet habitat with lots of rain","An underwater habitat"], answer:0},
     {q:"Which plant is well known for surviving in the desert?", options:["Seaweed","Fern","Water lily","Cactus"], answer:3},
     {q:"Which animal is well known for surviving in the desert?", options:["Penguin","Polar bear","Camel","Whale"], answer:2},
     {q:"Why can cacti survive with very little water?", options:["This concept has no connection to desert survival","Cacti absorb water only from the air","Cacti never need any water at all","They can store water inside their thick stems"], answer:3},
     {q:"A desert is best described as a habitat that is ___.", options:["Underwater","Frozen year-round","Dry with little rainfall","Wet with lots of rainfall"], answer:2}
   ],
   worksheet:[
     {prompt:"Is a desert habitat usually very dry or very wet?", answers:["very dry","dry"]},
     {prompt:"Name one plant that can survive in a desert, like a cactus.", answers:["cactus"]},
     {prompt:"Name one animal that can survive in a desert, like a camel.", answers:["camel"]}
   ]},
  {subject:"SocialStudies", title:"Trade Between Countries: Imports and Exports", summary:"Students learn that countries trade goods with each other, sending exports to other countries and receiving imports from other countries, so people can access products not made locally.",
   resourceLabel:"YouTube: Trade Between Countries: Imports and Exports", resourceUrl:"https://www.youtube.com/results?search_query=Trade%20Between%20Countries%3A%20Imports%20and%20Exports%20grade%202%20educational",
   quiz:[
     {q:"What are exports?", options:["Money a country never uses","Goods a country never sells","Goods a country only keeps for itself","Goods a country sends to another country"], answer:3},
     {q:"What are imports?", options:["Money with no real value","Goods a country only sends away","Goods a country receives from another country","Goods that are never traded"], answer:2},
     {q:"Why do countries trade goods with each other?", options:["To access products that may not be made locally","Countries never need goods from elsewhere","This concept has no connection to daily life","Trade has no benefit to any country"], answer:0},
     {q:"If Canada sends maple syrup to another country, is that an import or an export for Canada?", options:["Neither","Both at the same time","An export","An import"], answer:2},
     {q:"Trading goods between countries is an example of ___.", options:["Ignoring other countries needs","Something that never actually happens","Working together to share resources","Countries refusing to work together"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call goods a country sends to another country?", answers:["exports"]},
     {prompt:"What do we call goods a country receives from another country?", answers:["imports"]},
     {prompt:"Does trade help countries access products not made locally?", answers:["yes"]}
   ]},
]},
{day:83, label:"Day 83 — Wed", subjects:[
  {subject:"Language", title:"Analogies: Comparing Word Relationships", summary:"Students learn that an analogy compares two pairs of words that share a similar relationship, such as hot is to cold as up is to down, both showing opposite pairs.",
   resourceLabel:"YouTube: Analogies: Comparing Word Relationships", resourceUrl:"https://www.youtube.com/results?search_query=Analogies%3A%20Comparing%20Word%20Relationships%20grade%202%20educational",
   quiz:[
     {q:"What is an analogy?", options:["A single word with two meanings","A word with no meaning at all","A comparison of two pairs of words that share a relationship","A punctuation mark"], answer:2},
     {q:"Complete the analogy: bird is to nest as bee is to ___.", options:["Burrow","Web","Hive","Den"], answer:2},
     {q:"Complete the analogy: finger is to hand as toe is to ___.", options:["Arm","Foot","Ear","Head"], answer:1},
     {q:"What relationship do the words puppy and dog share in an analogy about baby animals and adult animals?", options:["A puppy and dog are the same age","A puppy is unrelated to a dog","A puppy is bigger than a dog","A puppy is a baby dog"], answer:3},
     {q:"Solving analogies helps students understand ___.", options:["Only how to spell words correctly","Only how to count numbers","Nothing useful about language","How words and ideas relate to each other"], answer:3}
   ],
   worksheet:[
     {prompt:"In the analogy hot is to cold as up is to ___, what word completes the pattern?", answers:["down"]},
     {prompt:"What kind of relationship do hot/cold and up/down share?", answers:["opposites","they are opposites"]},
     {prompt:"Is an analogy a way of comparing word relationships?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Fact Family Triangles: Multiplication and Division", summary:"Students learn to use a fact family triangle, showing three related numbers, to see how one multiplication fact and its related division facts connect, such as 3, 4, and 12.",
   resourceLabel:"YouTube: Fact Family Triangles: Multiplication and Division", resourceUrl:"https://www.youtube.com/results?search_query=Fact%20Family%20Triangles%3A%20Multiplication%20and%20Division%20grade%202%20educational",
   quiz:[
     {q:"In the fact family with 5, 6, and 30, what is 5 times 6?", options:["11","25","36","30"], answer:3},
     {q:"In the fact family with 5, 6, and 30, what is 30 divided by 5?", options:["5","30","6","25"], answer:2},
     {q:"In the fact family with 7, 8, and 56, what is 56 divided by 8?", options:["56","7","48","8"], answer:1},
     {q:"A fact family triangle shows how many related number facts?", options:["Four","Ten","Two","One"], answer:0},
     {q:"A fact family triangle uses three numbers to show connected ___ and ___ facts.", options:["Addition and subtraction","Time and money","Multiplication and division","Fraction and decimal"], answer:2}
   ],
   worksheet:[
     {prompt:"In the fact family with 3, 4, and 12, what is 3 times 4?", answers:["12","twelve"]},
     {prompt:"In the fact family with 3, 4, and 12, what is 12 divided by 4?", answers:["3","three"]},
     {prompt:"In the fact family with 3, 4, and 12, what is 12 divided by 3?", answers:["4","four"]}
   ]},
  {subject:"Science", title:"Rainforests: A Warm, Wet Habitat", summary:"Students learn that a rainforest is a warm, wet habitat that gets a huge amount of rain each year, supporting a great variety of plants and animals such as monkeys, parrots, and frogs.",
   resourceLabel:"YouTube: Rainforests: A Warm, Wet Habitat", resourceUrl:"https://www.youtube.com/results?search_query=Rainforests%3A%20A%20Warm%2C%20Wet%20Habitat%20grade%202%20educational",
   quiz:[
     {q:"What kind of habitat is a rainforest?", options:["A dry, sandy habitat","An underwater habitat only","A cold, icy habitat","A warm, wet habitat with lots of rain"], answer:3},
     {q:"Which animal is well known for living in the rainforest?", options:["Polar bear","Monkey","Camel","Penguin"], answer:1},
     {q:"Why do rainforests support so many different plants and animals?", options:["Rainforests have no food or shelter at all","Very few living things can survive there","The warm, wet climate provides lots of food and shelter","Rainforests are always frozen solid"], answer:2},
     {q:"Which of these is a feature of a rainforest?", options:["Deep ocean water covering the land","Ice covering the ground year-round","Sand dunes with almost no rain","Tall trees and lots of rainfall"], answer:3},
     {q:"A rainforest is best described as a habitat with a huge amount of ___.", options:["Sand","Snow","Ice","Rainfall"], answer:3}
   ],
   worksheet:[
     {prompt:"Is a rainforest habitat usually warm and wet or cold and dry?", answers:["warm and wet","warm, wet"]},
     {prompt:"Name one animal that lives in the rainforest, like a monkey or parrot.", answers:["monkey","parrot","frog"]},
     {prompt:"Do rainforests support a great variety of plants and animals?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Confederation: How Canada Became a Country", summary:"Students learn that Canadian Confederation was the joining together of separate colonies in 1867 to form the country of Canada, with its own government to make decisions.",
   resourceLabel:"YouTube: Canadian Confederation: How Canada Became a Country", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Confederation%3A%20How%20Canada%20Became%20a%20Country%20grade%202%20educational",
   quiz:[
     {q:"What was Canadian Confederation?", options:["A war between two countries","A type of sporting event","A single citys founding","Separate colonies joining together to form the country of Canada"], answer:3},
     {q:"In what year did Canadian Confederation take place?", options:["1900","1812","1867","1776"], answer:2},
     {q:"What happened to Canadas government after Confederation?", options:["Canada lost its ability to make any decisions","Canada gained its own government to make decisions","No government existed after Confederation","Another country took over completely"], answer:1},
     {q:"Why is Confederation an important event in Canadian history?", options:["It happened in a different country entirely","It only affected one small town","It has no connection to Canadian history","It marks when Canada became its own country"], answer:3},
     {q:"Confederation is best described as colonies joining to form ___.", options:["Two separate countries","No country at all","One country","A single small city"], answer:2}
   ],
   worksheet:[
     {prompt:"In what year did Canadian Confederation happen?", answers:["1867"]},
     {prompt:"What word describes separate colonies joining together to form one country?", answers:["confederation"]},
     {prompt:"Did Canada gain its own government to make decisions after Confederation?", answers:["yes"]}
   ]},
]},
{day:84, label:"Day 84 — Thu", subjects:[
  {subject:"Language", title:"Proofreading Symbols: Marking Up Writing", summary:"Students learn simple proofreading symbols, such as a caret to add a missing word or a line through a word to remove it, used to mark corrections in a piece of writing.",
   resourceLabel:"YouTube: Proofreading Symbols: Marking Up Writing", resourceUrl:"https://www.youtube.com/results?search_query=Proofreading%20Symbols%3A%20Marking%20Up%20Writing%20grade%202%20educational",
   quiz:[
     {q:"What is a proofreading symbol used for?", options:["Colouring in a word","Marking corrections in a piece of writing","Erasing an entire page","Drawing a picture on a page"], answer:1},
     {q:"What does a caret symbol usually show in proofreading?", options:["A sentence should be deleted entirely","A missing word should be added there","A word should be made bigger","A word should be coloured"], answer:1},
     {q:"What does drawing a line through a word usually mean?", options:["The word should be repeated twice","The word should be removed","The word is spelled correctly","The word should be kept exactly as is"], answer:1},
     {q:"Why are proofreading symbols useful when editing writing?", options:["They are only used for drawing pictures","They have no real purpose in writing","They make writing harder to understand","They help writers quickly mark exact corrections"], answer:3},
     {q:"Using proofreading symbols is part of the writing step called ___.", options:["Ignoring mistakes","Publishing only","Drawing","Editing"], answer:3}
   ],
   worksheet:[
     {prompt:"What symbol is often used to show a missing word should be added?", answers:["caret"]},
     {prompt:"What can a line through a word show a writer should do?", answers:["remove it","delete it"]},
     {prompt:"Do proofreading symbols help writers mark corrections in their writing?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Measuring Angles: Right, Acute, and Obtuse", summary:"Students learn to identify three kinds of angles: a right angle, which looks like the corner of a square, an acute angle, which is smaller than a right angle, and an obtuse angle, which is larger.",
   resourceLabel:"YouTube: Measuring Angles: Right, Acute, and Obtuse", resourceUrl:"https://www.youtube.com/results?search_query=Measuring%20Angles%3A%20Right%2C%20Acute%2C%20and%20Obtuse%20grade%202%20educational",
   quiz:[
     {q:"What is a right angle?", options:["An angle that looks like the corner of a square","An angle only found in circles","An angle that is always curved","An angle with no size at all"], answer:0},
     {q:"Which of these describes an acute angle?", options:["The same as a straight line","Smaller than a right angle","Exactly equal to a right angle","Larger than a right angle"], answer:1},
     {q:"Which of these describes an obtuse angle?", options:["Larger than a right angle","Exactly equal to a right angle","The same as no angle at all","Smaller than a right angle"], answer:0},
     {q:"Which of these shapes has four right angles?", options:["A triangle with all different angles","A circle","A square","A curved line"], answer:2},
     {q:"Learning to identify angles helps us describe ___.", options:["The smell of shapes","The corners of shapes","The weight of shapes","The colour of shapes"], answer:1}
   ],
   worksheet:[
     {prompt:"What kind of angle looks like the corner of a square?", answers:["right angle"]},
     {prompt:"Is an acute angle smaller or larger than a right angle?", answers:["smaller"]},
     {prompt:"Is an obtuse angle smaller or larger than a right angle?", answers:["larger"]}
   ]},
  {subject:"Science", title:"Ocean Zones: Sunlight, Twilight, and Midnight", summary:"Students learn that the ocean has different zones based on depth and light, with the sunlit zone near the top, the twilight zone getting dim light, and the dark midnight zone far below.",
   resourceLabel:"YouTube: Ocean Zones: Sunlight, Twilight, and Midnight", resourceUrl:"https://www.youtube.com/results?search_query=Ocean%20Zones%3A%20Sunlight%2C%20Twilight%2C%20and%20Midnight%20grade%202%20educational",
   quiz:[
     {q:"What is the sunlit zone of the ocean?", options:["The deepest, darkest zone","The top zone that gets the most sunlight","A zone with no water at all","A zone found only on land"], answer:1},
     {q:"What is the twilight zone of the ocean?", options:["A middle zone that gets only dim light","A zone found only near the shore","The top zone with bright sunlight","The very deepest, completely dark zone"], answer:0},
     {q:"What is the midnight zone of the ocean?", options:["A zone that never has any water","The top zone with the brightest sunlight","A zone found only near the surface","The deepest zone, which is completely dark"], answer:3},
     {q:"Why does light decrease as you go deeper into the ocean?", options:["Water makes light brighter the deeper you go","The ocean has no connection to sunlight at all","Sunlight cannot travel very far through deep water","Sunlight always reaches every part of the ocean equally"], answer:2},
     {q:"The three ocean zones are organized based on their depth and ___.", options:["Amount of light","Water temperature only","Amount of sand","Number of fish"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the top ocean zone that gets the most sunlight?", answers:["sunlit zone"]},
     {prompt:"Does the twilight zone get bright sunlight or dim light?", answers:["dim light","dim"]},
     {prompt:"Is the midnight zone bright or completely dark?", answers:["completely dark","dark"]}
   ]},
  {subject:"SocialStudies", title:"Non-Profit Organizations: Helping Communities in Need", summary:"Students learn that a non-profit organization is a group that works to help people or causes, such as a food bank or animal shelter, using donations instead of trying to earn a profit.",
   resourceLabel:"YouTube: Non-Profit Organizations: Helping Communities in Need", resourceUrl:"https://www.youtube.com/results?search_query=Non-Profit%20Organizations%3A%20Helping%20Communities%20in%20Need%20grade%202%20educational",
   quiz:[
     {q:"What is a non-profit organization?", options:["A type of school subject","A store that only tries to earn money","A government building","A group that uses donations to help people or causes"], answer:3},
     {q:"Which of these is an example of a non-profit organization?", options:["A grocery store","A food bank","A car dealership","A toy factory"], answer:1},
     {q:"How does a non-profit organization usually get the resources it needs?", options:["By taking money from the government only","Non-profits never need any resources","Through donations from people in the community","By selling products for the highest possible price"], answer:2},
     {q:"Why might a community value having a non-profit organization like a food bank?", options:["Non-profits have no connection to community needs","Food banks never actually help anyone","This concept has no relevance to social studies","It helps people in the community who need food"], answer:3},
     {q:"Non-profit organizations are focused on helping others rather than ___.", options:["Earning a profit for themselves","Working together with volunteers","Serving their community","Collecting donations"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call a group that helps people or causes using donations?", answers:["non-profit organization","non-profit"]},
     {prompt:"Name one example of a non-profit organization, like a food bank.", answers:["food bank","animal shelter"]},
     {prompt:"Does a non-profit organization try to earn money for itself, or help others?", answers:["help others"]}
   ]},
]},
{day:85, label:"Day 85 — Fri", subjects:[
  {subject:"Language", title:"Story Conflict: The Problem in a Story", summary:"Students learn that most stories have a conflict, a problem the main character must face and try to solve, which often drives the events of the story forward.",
   resourceLabel:"YouTube: Story Conflict: The Problem in a Story", resourceUrl:"https://www.youtube.com/results?search_query=Story%20Conflict%3A%20The%20Problem%20in%20a%20Story%20grade%202%20educational",
   quiz:[
     {q:"What is a story conflict?", options:["The colour of the book cover","The problem a main character must face and try to solve","The name of the illustrator","The title of the book"], answer:1},
     {q:"Which of these is an example of a story conflict?", options:["A character eats breakfast with no problems","A character is lost and must find their way home","A character reads a book quietly","A character has a calm, uneventful day"], answer:1},
     {q:"Why is conflict an important part of most stories?", options:["Conflict has no connection to how a story unfolds","Conflict only appears in the very last page","It often drives the events of the story forward","Stories are always better with no conflict at all"], answer:2},
     {q:"At the end of a story, what usually happens to the conflict?", options:["It has no ending at all","It disappears with no explanation at all","It always stays exactly the same","It is often solved or resolved"], answer:3},
     {q:"Recognizing a storys conflict helps readers understand ___.", options:["Only the number of pages","Nothing about the story","Only the books price","What problem the character is trying to solve"], answer:3}
   ],
   worksheet:[
     {prompt:"What word describes the problem a main character must face in a story?", answers:["conflict"]},
     {prompt:"Does a storys conflict often drive the events of the story forward?", answers:["yes"]},
     {prompt:"If a character is lost in a forest and must find their way home, is that a story conflict?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Data: Choosing the Best Graph to Show Information", summary:"Students learn to think about which type of graph, such as a bar graph, pictograph, or line plot, best shows a certain kind of information clearly.",
   resourceLabel:"YouTube: Data: Choosing the Best Graph to Show Information", resourceUrl:"https://www.youtube.com/results?search_query=Data%3A%20Choosing%20the%20Best%20Graph%20to%20Show%20Information%20grade%202%20educational",
   quiz:[
     {q:"Which graph type uses pictures to show data?", options:["A number line","A pictograph","A line plot","A bar graph"], answer:1},
     {q:"Which graph type uses bars to compare different amounts?", options:["A pictograph","A bar graph","A calendar","A Venn diagram"], answer:1},
     {q:"Why might someone choose a bar graph over a pictograph?", options:["A bar graph can more precisely show exact amounts","Bar graphs are never useful for showing data","The type of graph never actually matters","Pictographs always show more precise data"], answer:0},
     {q:"If you wanted to show how many students chose each favourite colour, which graph could help?", options:["A bar graph","A blank page","A calendar","A single number"], answer:0},
     {q:"Choosing the best graph for data helps information become ___.", options:["Impossible to read","Completely hidden","Clearer and easier to understand","More confusing"], answer:2}
   ],
   worksheet:[
     {prompt:"Which type of graph uses pictures to represent data?", answers:["pictograph"]},
     {prompt:"Which type of graph uses bars to compare amounts?", answers:["bar graph"]},
     {prompt:"Should the type of graph chosen depend on the kind of information being shown?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Compound Machines: Combining Simple Machines", summary:"Students learn that a compound machine is made by combining two or more simple machines, such as a wheelbarrow, which uses a wheel and axle together with a lever.",
   resourceLabel:"YouTube: Compound Machines: Combining Simple Machines", resourceUrl:"https://www.youtube.com/results?search_query=Compound%20Machines%3A%20Combining%20Simple%20Machines%20grade%202%20educational",
   quiz:[
     {q:"What is a compound machine?", options:["A machine that never actually works","A type of animal","A machine with only one single part","A machine made by combining two or more simple machines"], answer:3},
     {q:"Which of these is an example of a compound machine?", options:["A single nail","A wheelbarrow","A single wheel with nothing else","A plain rock"], answer:1},
     {q:"Which simple machines combine to make a wheelbarrow work?", options:["Only a single pulley","A wheel and axle with a lever","Only a single screw","A magnet and a spring"], answer:1},
     {q:"Why might combining simple machines create a more useful tool?", options:["Combining them can make certain tasks even easier to do","This concept has no connection to tools","Simple machines can never be combined","Combining machines always makes tasks harder"], answer:0},
     {q:"A pair of scissors is a compound machine made of two combined ___.", options:["Wheels","Screws","Levers","Pulleys"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call a machine made by combining two or more simple machines?", answers:["compound machine"]},
     {prompt:"Name one example of a compound machine, like a wheelbarrow.", answers:["wheelbarrow"]},
     {prompt:"Does a wheelbarrow combine a wheel and axle with a lever?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Natural Resources: What Canada Provides", summary:"Students learn that Canada has many natural resources, such as forests, fresh water, and minerals, which provide materials that people use and that support many jobs.",
   resourceLabel:"YouTube: Natural Resources: What Canada Provides", resourceUrl:"https://www.youtube.com/results?search_query=Natural%20Resources%3A%20What%20Canada%20Provides%20grade%202%20educational",
   quiz:[
     {q:"What are natural resources?", options:["Only objects made in a factory","Only items found in a store","Materials from nature that people use","Materials that do not exist in nature"], answer:2},
     {q:"Which of these is an example of a Canadian natural resource?", options:["Video games","Paved roads","Forests","Plastic toys"], answer:2},
     {q:"How do natural resources support jobs in Canada?", options:["Natural resources have no connection to any jobs","Many people work in industries that use these resources","No jobs exist because of natural resources","Natural resources only exist in other countries"], answer:1},
     {q:"Why is it important to use natural resources carefully?", options:["Careful use of resources has no benefit","Natural resources can never run out","So they remain available for the future","This concept has no relevance to Canada"], answer:2},
     {q:"Natural resources like forests and fresh water come directly from ___.", options:["Nature","Factories only","Imagination only","Stores only"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes materials from nature that people use, like forests or water?", answers:["natural resources"]},
     {prompt:"Name one natural resource found in Canada, like forests or fresh water.", answers:["forests","fresh water","minerals"]},
     {prompt:"Do natural resources support many jobs in Canada?", answers:["yes"]}
   ]},
]},
{day:86, label:"Day 86 — Mon", subjects:[
  {subject:"Language", title:"Word Endings: Adding -tion and -ness", summary:"Students learn that adding -tion to some words can turn an action into a noun, like adding to inform to make information, and adding -ness can turn an adjective into a noun, like kind into kindness.",
   resourceLabel:"YouTube: Word Endings: Adding -tion and -ness", resourceUrl:"https://www.youtube.com/results?search_query=Word%20Endings%3A%20Adding%20-tion%20and%20-ness%20grade%202%20educational",
   quiz:[
     {q:"What does adding -ness to a word like kind create?", options:["No real word at all","Kindly, a different adjective","Kindness, a noun","Kinding, a verb"], answer:2},
     {q:"What does adding -tion to a word like inform create?", options:["Informed, a different verb form only","Information, a noun","No real word at all","Informly, an adverb"], answer:1},
     {q:"Which word means the state of being happy?", options:["Happiness","Happier","Happied","Happily"], answer:0},
     {q:"Add -tion to the word educate. What new word do you make?", options:["Education","Educative","Educated","Educately"], answer:0},
     {q:"Adding endings like -tion and -ness often changes a word into a ___.", options:["Verb","Number","Noun","Question"], answer:2}
   ],
   worksheet:[
     {prompt:"Add -ness to the word kind. What new word do you make?", answers:["kindness"]},
     {prompt:"Add -tion to the word inform. What new word do you make?", answers:["information"]},
     {prompt:"Does adding -ness to an adjective usually turn it into a noun?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Money: Different Combinations for the Same Total", summary:"Students practise finding different combinations of coins and bills that add up to the same total amount of money, such as making 50 cents using different sets of coins.",
   resourceLabel:"YouTube: Money: Different Combinations for the Same Total", resourceUrl:"https://www.youtube.com/results?search_query=Money%3A%20Different%20Combinations%20for%20the%20Same%20Total%20grade%202%20educational",
   quiz:[
     {q:"Which combination of coins could make exactly 25 cents?", options:["Two dimes","One penny","One nickel","One quarter"], answer:3},
     {q:"Which combination of coins could make exactly 15 cents?", options:["One dime and one nickel","One nickel only","One quarter","Two pennies"], answer:0},
     {q:"If you have 3 dimes, how many cents do you have in total?", options:["30","3","10","13"], answer:0},
     {q:"Why might it be useful to know different ways to make the same total?", options:["There is never more than one way to make a total","This concept has no connection to money","Coins can only ever be combined in one way","It helps when paying with the coins you actually have"], answer:3},
     {q:"Finding different coin combinations for the same total is an example of ___.", options:["Ignoring numbers completely","Flexible thinking with numbers","ForgETting how coins work","Avoiding math altogether"], answer:1}
   ],
   worksheet:[
     {prompt:"Name two different ways to make 10 cents using coins, like two nickels or ten pennies.", answers:["two nickels","ten pennies"]},
     {prompt:"If a nickel is 5 cents, how many nickels make 25 cents?", answers:["5","five"]},
     {prompt:"Can two different combinations of coins add up to the exact same total?", answers:["yes"]}
   ]},
  {subject:"Science", title:"The Rock Cycle: Igneous, Sedimentary, and Metamorphic", summary:"Students learn that rocks can slowly change from one type to another over a very long time, forming igneous rock from cooled melted rock, sedimentary rock from layers of sediment, and metamorphic rock from heat and pressure.",
   resourceLabel:"YouTube: The Rock Cycle: Igneous, Sedimentary, and Metamorphic", resourceUrl:"https://www.youtube.com/results?search_query=The%20Rock%20Cycle%3A%20Igneous%2C%20Sedimentary%2C%20and%20Metamorphic%20grade%202%20educational",
   quiz:[
     {q:"What is igneous rock?", options:["Rock formed only from sand blowing in wind","Rock that never actually forms","Rock formed only underwater","Rock formed from cooled melted rock"], answer:3},
     {q:"What is sedimentary rock?", options:["Rock formed only from ice","Rock that has no connection to layers","Rock formed from layers of sediment","Rock formed only from lava"], answer:2},
     {q:"What is metamorphic rock?", options:["Rock found only in the ocean","Rock that never changes at all","Rock changed by heat and pressure","Rock formed only from wind"], answer:2},
     {q:"Why is this process called a rock cycle?", options:["Rocks never change from one type to another","The rock cycle has no connection to time","Only one type of rock has ever existed","Rocks can slowly change from one type into another over time"], answer:3},
     {q:"The rock cycle shows that rocks are always ___.", options:["Slowly changing over long periods of time","Exactly the same forever","Unrelated to one another","Disappearing completely with no trace"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one of the three main types of rock, like igneous, sedimentary, or metamorphic.", answers:["igneous","sedimentary","metamorphic"]},
     {prompt:"Does igneous rock form from cooled melted rock?", answers:["yes"]},
     {prompt:"Does sedimentary rock form from layers of sediment?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Our Postal System: From Sender to Receiver", summary:"Students learn the steps a letter or package takes through the postal system, from being dropped off, sorted at a postal facility, and delivered by a carrier to its receiver.",
   resourceLabel:"YouTube: Our Postal System: From Sender to Receiver", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Postal%20System%3A%20From%20Sender%20to%20Receiver%20grade%202%20educational",
   quiz:[
     {q:"What is the postal system?", options:["A system that only sells groceries","A system that fights fires","A system with no real purpose","The system that collects, sorts, and delivers mail"], answer:3},
     {q:"Which of these is a step in how mail travels?", options:["Being planted in a garden","Being sold at a store","Being cooked in an oven","Being sorted at a postal facility"], answer:3},
     {q:"Who helps deliver mail to its final receiver?", options:["A farmer","A dentist","A postal carrier","A firefighter"], answer:2},
     {q:"Why is the postal system important for a community?", options:["It has no connection to communication","Mail never actually needs to be delivered","It helps people send and receive letters and packages","This concept has no relevance to communities"], answer:2},
     {q:"The postal system connects a sender to a ___.", options:["Receiver","A completely different country only","Random stranger","Nobody at all"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the system that collects, sorts, and delivers mail?", answers:["postal system"]},
     {prompt:"Name one step a letter takes, like being sorted or delivered.", answers:["sorted","delivered"]},
     {prompt:"Does a postal carrier help deliver mail to its receiver?", answers:["yes"]}
   ]},
]},
{day:87, label:"Day 87 — Tue", subjects:[
  {subject:"Language", title:"Formal and Informal Language: How We Talk in Different Places", summary:"Students learn that formal language, used in places like a classroom presentation, is more polite and careful, while informal language, used with friends, is more relaxed and casual.",
   resourceLabel:"YouTube: Formal and Informal Language: How We Talk in Different Places", resourceUrl:"https://www.youtube.com/results?search_query=Formal%20and%20Informal%20Language%3A%20How%20We%20Talk%20in%20Different%20Places%20grade%202%20educational",
   quiz:[
     {q:"What is formal language?", options:["Language only used with close friends","Polite and careful language used in serious situations","Language with no rules at all","A type of punctuation mark"], answer:1},
     {q:"What is informal language?", options:["Language only used in a courtroom","Relaxed, casual language used with friends","A kind of math equation","Language that is always written, never spoken"], answer:1},
     {q:"Which situation calls for formal language?", options:["Giving a presentation to the whole class","Joking around with a close friend","Playing a game with a sibling","Chatting with a best friend at recess"], answer:0},
     {q:"Which situation calls for informal language?", options:["Presenting a report to the class","Speaking at a formal event","Writing a serious letter to a mayor","Talking with a close friend at recess"], answer:3},
     {q:"Choosing formal or informal language depends on ___.", options:["Only the time of day","Nothing at all","The situation and who you are talking to","Only the weather outside"], answer:2}
   ],
   worksheet:[
     {prompt:"Would you use formal or informal language during a classroom presentation?", answers:["formal"]},
     {prompt:"Would you use formal or informal language chatting with a close friend?", answers:["informal"]},
     {prompt:"Is formal language usually more polite and careful than informal language?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Time: Converting Hours to Minutes", summary:"Students learn that one hour is equal to 60 minutes, and practise converting between hours and minutes, such as figuring out that 2 hours equals 120 minutes.",
   resourceLabel:"YouTube: Time: Converting Hours to Minutes", resourceUrl:"https://www.youtube.com/results?search_query=Time%3A%20Converting%20Hours%20to%20Minutes%20grade%202%20educational",
   quiz:[
     {q:"How many minutes are in 1 hour?", options:["60","30","100","12"], answer:0},
     {q:"How many minutes are in 3 hours?", options:["180","150","190","160"], answer:0},
     {q:"How many minutes are in half an hour?", options:["15","45","30","60"], answer:2},
     {q:"If an activity lasts 90 minutes, how many hours and minutes is that?", options:["1 hour and 30 minutes","90 hours","2 hours","1 hour and 90 minutes"], answer:0},
     {q:"Converting hours to minutes means multiplying the number of hours by ___.", options:["100","60","24","30"], answer:1}
   ],
   worksheet:[
     {prompt:"How many minutes are in 1 hour?", answers:["60","sixty"]},
     {prompt:"How many minutes are in 2 hours?", answers:["120","one hundred twenty"]},
     {prompt:"How many minutes are in half an hour?", answers:["30","thirty"]}
   ]},
  {subject:"Science", title:"Our Immune System: Fighting Off Germs", summary:"Students learn that our immune system is a team of body parts and cells that work together to fight off germs, helping us recover when we get sick.",
   resourceLabel:"YouTube: Our Immune System: Fighting Off Germs", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Immune%20System%3A%20Fighting%20Off%20Germs%20grade%202%20educational",
   quiz:[
     {q:"What is our immune system?", options:["A part of our skeleton only","A single bone in our body","A type of food we eat","A team of body parts and cells that fight off germs"], answer:3},
     {q:"What does our immune system help us do?", options:["Taste our food better","Grow taller every day","Fight off germs and recover when we get sick","See colours more clearly"], answer:2},
     {q:"Which of these helps support a healthy immune system?", options:["Never washing our hands at all","Ignoring germs completely","Washing our hands and eating healthy food","Avoiding all healthy food"], answer:2},
     {q:"Why is it helpful to rest when we are sick?", options:["Rest makes germs multiply faster","Resting helps our immune system fight off germs","Resting has no connection to getting better","Our immune system never needs any help"], answer:1},
     {q:"Our immune system is best described as our bodys ___.", options:["Defense against germs","Least important system","Only decoration","System for tasting food"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the team of body parts and cells that fight off germs?", answers:["immune system"]},
     {prompt:"Does our immune system help us recover when we get sick?", answers:["yes"]},
     {prompt:"Can washing our hands help stop germs from making us sick?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"City Planning: Designing Where We Live", summary:"Students learn that city planning involves deciding where to build homes, roads, parks, and schools, so that a community is organized and works well for the people who live there.",
   resourceLabel:"YouTube: City Planning: Designing Where We Live", resourceUrl:"https://www.youtube.com/results?search_query=City%20Planning%3A%20Designing%20Where%20We%20Live%20grade%202%20educational",
   quiz:[
     {q:"What is city planning?", options:["A type of sport played outdoors","A rule about how to bake bread","A story written by an author","Deciding where to build homes, roads, parks, and schools"], answer:3},
     {q:"Which of these might a city planner help decide?", options:["Where a new park should be built","What clothes a person should wear","What a family should eat for dinner","What book a student should read"], answer:0},
     {q:"Why is city planning important for a community?", options:["It helps organize a community so it works well for its people","Communities work better with absolutely no planning","City planning has no benefit to a community","This concept has no connection to daily life"], answer:0},
     {q:"If a city planner wants to reduce traffic near a school, what might they plan?", options:["A safer road design near the school","A brand new ocean nearby","A taller building far away","Nothing at all needs to be planned"], answer:0},
     {q:"City planning helps make sure a community has enough ___.", options:["Only roads and nothing else","Only homes and nothing else","No buildings of any kind","Homes, roads, parks, and schools"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call deciding where to build homes, roads, and parks in a community?", answers:["city planning"]},
     {prompt:"Name one thing city planners might decide the location of, like a park or school.", answers:["park","school","road"]},
     {prompt:"Does city planning help a community work well for the people who live there?", answers:["yes"]}
   ]},
]},
{day:88, label:"Day 88 — Wed", subjects:[
  {subject:"Language", title:"Skimming and Scanning: Reading Strategies for Finding Information", summary:"Students learn two reading strategies: skimming, which means quickly looking over a text to get its general idea, and scanning, which means quickly searching for a specific piece of information.",
   resourceLabel:"YouTube: Skimming and Scanning: Reading Strategies for Finding Information", resourceUrl:"https://www.youtube.com/results?search_query=Skimming%20and%20Scanning%3A%20Reading%20Strategies%20for%20Finding%20Information%20grade%202%20educational",
   quiz:[
     {q:"What is skimming?", options:["Reading every single word very slowly","Quickly looking over a text to get its general idea","Memorizing an entire book word for word","Ignoring a text completely"], answer:1},
     {q:"What is scanning?", options:["Reading a book from cover to cover slowly","Colouring in the pictures of a book","Quickly searching for a specific piece of information","Writing a brand new story"], answer:2},
     {q:"Which strategy would help you quickly find a phone number in a long list?", options:["Skimming","Scanning","Memorizing the entire list","Ignoring the list completely"], answer:1},
     {q:"Which strategy would help you get a general idea of what an article is about before reading it fully?", options:["Scanning","Skimming","Reading only the very last word","Skipping the article entirely"], answer:1},
     {q:"Skimming and scanning are useful reading strategies because they help readers ___.", options:["Make reading take much longer","Forget the topic of a text","Avoid reading altogether","Find information quickly and efficiently"], answer:3}
   ],
   worksheet:[
     {prompt:"What reading strategy means quickly looking over a text to get its general idea?", answers:["skimming"]},
     {prompt:"What reading strategy means quickly searching for one specific piece of information?", answers:["scanning"]},
     {prompt:"Would scanning help you quickly find a specific date in a long article?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Patterns: Finding the Rule", summary:"Students learn to look at a number pattern, such as 3, 6, 9, 12, and figure out the rule that explains how each number connects to the next, such as add 3 each time.",
   resourceLabel:"YouTube: Patterns: Finding the Rule", resourceUrl:"https://www.youtube.com/results?search_query=Patterns%3A%20Finding%20the%20Rule%20grade%202%20educational",
   quiz:[
     {q:"What is the rule for the pattern 2, 4, 6, 8?", options:["Add 2 each time","Add 4 each time","Subtract 2 each time","Multiply by 2 each time"], answer:0},
     {q:"What is the rule for the pattern 10, 20, 30, 40?", options:["Multiply by 10 each time","Add 10 each time","Add 5 each time","Subtract 10 each time"], answer:1},
     {q:"Using the rule add 4, what comes after 16 in the pattern 4, 8, 12, 16?", options:["18","24","22","20"], answer:3},
     {q:"Finding the rule of a pattern helps us ___.", options:["Ignore the numbers entirely","Forget the whole pattern","Make the pattern completely random","Predict what number comes next"], answer:3},
     {q:"What is the rule for the pattern 20, 17, 14, 11?", options:["Add 7 each time","Subtract 7 each time","Add 3 each time","Subtract 3 each time"], answer:3}
   ],
   worksheet:[
     {prompt:"In the pattern 3, 6, 9, 12, what is the rule?", answers:["add 3","add 3 each time"]},
     {prompt:"In the pattern 5, 10, 15, 20, what is the rule?", answers:["add 5","add 5 each time"]},
     {prompt:"Using the rule add 3, what comes after 12 in the pattern 3, 6, 9, 12?", answers:["15","fifteen"]}
   ]},
  {subject:"Science", title:"Chemical and Physical Changes: How Matter Can Change", summary:"Students learn that a physical change, like tearing paper, changes how something looks without making a new substance, while a chemical change, like burning wood, creates a new substance entirely.",
   resourceLabel:"YouTube: Chemical and Physical Changes: How Matter Can Change", resourceUrl:"https://www.youtube.com/results?search_query=Chemical%20and%20Physical%20Changes%3A%20How%20Matter%20Can%20Change%20grade%202%20educational",
   quiz:[
     {q:"What is a physical change?", options:["A change only found in outer space","A change that never actually happens","A change that always creates a brand new substance","A change in how something looks, without creating a new substance"], answer:3},
     {q:"What is a chemical change?", options:["A change that never creates anything new","A change that only happens to liquids","A change that only affects the colour of an object","A change that creates a brand new substance"], answer:3},
     {q:"Which of these is an example of a physical change?", options:["Burning a piece of paper","Baking a cake","Tearing a piece of paper","Rusting metal"], answer:2},
     {q:"Which of these is an example of a chemical change?", options:["Burning wood","Cutting a piece of string","Bending a paperclip","Folding paper"], answer:0},
     {q:"Chemical changes are different from physical changes because they ___.", options:["Only change the size of an object","Only happen once a year","Create an entirely new substance","Never actually change anything"], answer:2}
   ],
   worksheet:[
     {prompt:"Does tearing a piece of paper create a new substance, or just change its shape?", answers:["just change its shape","change its shape"]},
     {prompt:"Does burning wood create a new substance?", answers:["yes"]},
     {prompt:"What kind of change creates a brand new substance?", answers:["chemical change"]}
   ]},
  {subject:"SocialStudies", title:"Global Citizenship: Being a Responsible World Citizen", summary:"Students learn that a global citizen thinks beyond their own community and considers how their actions, such as recycling or being kind to others, can affect people around the world.",
   resourceLabel:"YouTube: Global Citizenship: Being a Responsible World Citizen", resourceUrl:"https://www.youtube.com/results?search_query=Global%20Citizenship%3A%20Being%20a%20Responsible%20World%20Citizen%20grade%202%20educational",
   quiz:[
     {q:"What is a global citizen?", options:["A person with no connection to other people","Someone who only thinks about their own street","Someone who considers how their actions affect people around the world","Someone who ignores every other country"], answer:2},
     {q:"Which of these is an action a responsible global citizen might take?", options:["Ignoring people in other countries completely","Recycling to help protect the environment","Refusing to help anyone at all","Wasting resources on purpose"], answer:1},
     {q:"Why might recycling in your own community help the whole world?", options:["Recycling only ever affects one single street","This concept has no relevance to global citizenship","Recycling has no connection to the environment","Protecting the environment can benefit people everywhere"], answer:3},
     {q:"How can being kind to newcomers show global citizenship?", options:["It shows care for people no matter where they come from","Global citizens should never be kind to newcomers","This concept only applies within one single country","Kindness has no connection to global citizenship"], answer:0},
     {q:"Being a global citizen means caring about people ___.", options:["Only in your own house","Around the world, not just in your own community","Nowhere at all","Only in your own school"], answer:1}
   ],
   worksheet:[
     {prompt:"What word describes someone who thinks about how their actions affect the whole world?", answers:["global citizen"]},
     {prompt:"Name one action a global citizen might take, like recycling.", answers:["recycling","being kind to others"]},
     {prompt:"Can our actions in our own community affect people in other parts of the world?", answers:["yes"]}
   ]},
]},
{day:89, label:"Day 89 — Thu", subjects:[
  {subject:"Language", title:"Writing a Book Review: Sharing Your Opinion of a Book", summary:"Students learn to write a simple book review, sharing their opinion about a book they read, along with reasons for their opinion, such as liking the characters or the exciting plot.",
   resourceLabel:"YouTube: Writing a Book Review: Sharing Your Opinion of a Book", resourceUrl:"https://www.youtube.com/results?search_query=Writing%20a%20Book%20Review%3A%20Sharing%20Your%20Opinion%20of%20a%20Book%20grade%202%20educational",
   quiz:[
     {q:"What is a book review?", options:["A list of every word in a book","A summary with no opinions at all","Writing that shares your opinion about a book, with reasons","A drawing of the book cover only"], answer:2},
     {q:"Why should a book review include reasons for your opinion?", options:["It helps explain why you feel that way about the book","Reasons are never needed in a review","This concept has no connection to writing","A review should never include any opinions"], answer:0},
     {q:"Which of these is an example of a reason in a book review?", options:["The book has one hundred pages","The book was published last year","I liked how brave the main character was","The book has a blue cover"], answer:2},
     {q:"A book review is different from a summary because a review also includes ___.", options:["Only the exact same words from the book","Only the title of the book","Nothing extra at all","Your opinion and reasons"], answer:3},
     {q:"Writing a book review can help other readers decide whether to ___.", options:["Read the book themselves","Avoid reading altogether","Never read any book again","Ignore the book completely"], answer:0}
   ],
   worksheet:[
     {prompt:"What kind of writing shares your opinion about a book you read?", answers:["book review"]},
     {prompt:"Should a book review include reasons that support your opinion?", answers:["yes"]},
     {prompt:"Name one reason you might like a book, like exciting characters or an exciting plot.", answers:["exciting characters","exciting plot","interesting characters"]}
   ]},
  {subject:"Math", title:"Estimating Products: Rounding Before Multiplying", summary:"Students learn to estimate the product of a multiplication problem by rounding one or both numbers to a friendly number first, making the multiplication easier to do quickly.",
   resourceLabel:"YouTube: Estimating Products: Rounding Before Multiplying", resourceUrl:"https://www.youtube.com/results?search_query=Estimating%20Products%3A%20Rounding%20Before%20Multiplying%20grade%202%20educational",
   quiz:[
     {q:"To estimate 4 times 11, what friendly number could 11 be rounded to?", options:["10","15","11","20"], answer:0},
     {q:"Using 4 times 10 as an estimate, what is a reasonable estimate for 4 times 11?", options:["40","44","400","4"], answer:0},
     {q:"What is a reasonable estimate for 5 times 21?", options:["About 10","About 1000","About 100","About 5"], answer:2},
     {q:"Why might someone estimate a product before finding the exact answer?", options:["Estimating has no connection to multiplication","An estimate is always exactly the same as the real answer","Estimating a product is never useful","An estimate can help check whether the exact answer is reasonable"], answer:3},
     {q:"Estimating products is a useful skill because it can help us ___.", options:["Replace the need for exact answers completely","Solve problems more quickly and check our work","Avoid learning multiplication facts","Make multiplication impossible to understand"], answer:1}
   ],
   worksheet:[
     {prompt:"To estimate 6 times 9, what friendly number could 9 be rounded to?", answers:["10"]},
     {prompt:"Using 6 times 10 as an estimate, what is a reasonable estimate for 6 times 9?", answers:["60","sixty"]},
     {prompt:"Is an estimate an exact answer or an approximate answer?", answers:["approximate answer","approximate"]}
   ]},
  {subject:"Science", title:"Biomes of the World: Comparing Different Habitats", summary:"Students learn that a biome is a large natural area with its own climate, plants, and animals, and that comparing biomes, like deserts, rainforests, and grasslands, shows how living things adapt to different conditions.",
   resourceLabel:"YouTube: Biomes of the World: Comparing Different Habitats", resourceUrl:"https://www.youtube.com/results?search_query=Biomes%20of%20the%20World%3A%20Comparing%20Different%20Habitats%20grade%202%20educational",
   quiz:[
     {q:"What is a biome?", options:["A kind of rock formation only","A type of ocean wave","A large natural area with its own climate, plants, and animals","A single tree found in a forest"], answer:2},
     {q:"Which of these is an example of a biome?", options:["A grocery store","A rainforest","A single classroom","A birthday party"], answer:1},
     {q:"Why do animals in a desert biome look different from animals in an Arctic biome?", options:["Each biome has different conditions that animals must adapt to","Animals never adapt to their biome at all","All biomes have the exact same conditions","This concept has no connection to biomes"], answer:0},
     {q:"Comparing different biomes helps scientists understand ___.", options:["How living things adapt to different environments","Only how one single biome works","Nothing useful about the natural world","Only the weather in one single place"], answer:0},
     {q:"A biomes climate, plants, and animals are all closely ___.", options:["Impossible to compare","Completely unrelated","Connected to each other","Chosen at random"], answer:2}
   ],
   worksheet:[
     {prompt:"What word describes a large natural area with its own climate, plants, and animals?", answers:["biome"]},
     {prompt:"Name one example of a biome, like a desert or rainforest.", answers:["desert","rainforest","grassland"]},
     {prompt:"Do living things adapt differently depending on the biome they live in?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Comparing Rural, Urban, and Suburban Jobs", summary:"Students learn that the kinds of jobs people do can differ between rural areas, such as farming, urban areas, such as office work, and suburban areas, which often blend both kinds of jobs.",
   resourceLabel:"YouTube: Comparing Rural, Urban, and Suburban Jobs", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Rural%2C%20Urban%2C%20and%20Suburban%20Jobs%20grade%202%20educational",
   quiz:[
     {q:"Which job is most common in a rural area?", options:["Farming","Skyscraper construction","Office work in a skyscraper","Subway operator"], answer:0},
     {q:"Which job is more common in a busy urban area?", options:["Farming large fields","Herding livestock","Office work","Fishing on a small lake"], answer:2},
     {q:"Why might job types differ between rural and urban areas?", options:["Each area has different land, resources, and population needs","This concept has no connection to communities","Rural and urban areas never have any differences","Job types are always exactly the same everywhere"], answer:0},
     {q:"What might make suburban jobs unique compared to rural or urban jobs?", options:["Suburban areas never have any jobs at all","Suburban jobs are always identical to rural jobs","Suburban jobs have no connection to communities","They often blend features of both rural and urban work"], answer:3},
     {q:"Comparing jobs across rural, urban, and suburban areas helps us understand ___.", options:["That location has no effect on community life","That jobs never change based on location","How communities and their needs can differ","That every community is exactly the same"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one job common in a rural area, like farming.", answers:["farming"]},
     {prompt:"Name one job common in an urban area, like office work.", answers:["office work"]},
     {prompt:"Do suburban areas often blend jobs from both rural and urban areas?", answers:["yes"]}
   ]},
]},
{day:90, label:"Day 90 — Fri", subjects:[
  {subject:"Language", title:"Language Review: Sentences, Figurative Language, and Reading Strategies", summary:"Students review recent Language skills: compound sentences, metaphors, analogies, proofreading symbols, story conflict, word endings, formal and informal language, skimming and scanning, and book reviews.",
   resourceLabel:"YouTube: Language Review: Sentences, Figurative Language, and Reading Strategies", resourceUrl:"https://www.youtube.com/results?search_query=Language%20Review%3A%20Sentences%2C%20Figurative%20Language%2C%20and%20Reading%20Strategies%20grade%202%20educational",
   quiz:[
     {q:"Which word can join two sentences to show a result?", options:["So","Or","The","A"], answer:0},
     {q:"Which of these sentences is a metaphor?", options:["The playground had many students.","The playground was empty today.","The playground was as busy as a beehive.","The playground was a beehive of activity."], answer:3},
     {q:"What does a caret symbol usually show in proofreading?", options:["A word should be coloured","A missing word should be added there","A word should be made bigger","A sentence should be deleted entirely"], answer:1},
     {q:"Which situation calls for formal language?", options:["Chatting with a best friend at recess","Joking around with a close friend","Playing a game with a sibling","Giving a presentation to the whole class"], answer:3},
     {q:"What is skimming?", options:["Reading every single word very slowly","Quickly looking over a text to get its general idea","Ignoring a text completely","Memorizing an entire book word for word"], answer:1}
   ],
   worksheet:[
     {prompt:"Which word can join two sentences to show a choice?", answers:["or"]},
     {prompt:"What is a metaphor?", answers:["a comparison that says one thing is another thing","a comparison"]},
     {prompt:"What is a story conflict?", answers:["the problem a main character must face and try to solve","a problem"]}
   ]},
  {subject:"Math", title:"Math Review: Multiplication, Division, and Measurement", summary:"Students review recent Math skills: multiplication facts for 6s and 7s, division facts, fact family triangles, measuring angles, choosing graphs, coin combinations, converting time, patterns, and estimating products.",
   resourceLabel:"YouTube: Math Review: Multiplication, Division, and Measurement", resourceUrl:"https://www.youtube.com/results?search_query=Math%20Review%3A%20Multiplication%2C%20Division%2C%20and%20Measurement%20grade%202%20educational",
   quiz:[
     {q:"What is 7 times 3?", options:["24","14","18","21"], answer:3},
     {q:"In the fact family with 5, 6, and 30, what is 30 divided by 5?", options:["30","25","6","5"], answer:2},
     {q:"Which of these describes an acute angle?", options:["Exactly equal to a right angle","Larger than a right angle","The same as a straight line","Smaller than a right angle"], answer:3},
     {q:"What is the rule for the pattern 2, 4, 6, 8?", options:["Add 2 each time","Add 4 each time","Multiply by 2 each time","Subtract 2 each time"], answer:0},
     {q:"What is a reasonable estimate for 5 times 21?", options:["About 100","About 5","About 10","About 1000"], answer:0}
   ],
   worksheet:[
     {prompt:"What is 6 times 3?", answers:["18","eighteen"]},
     {prompt:"If 6 times 4 equals 24, what does 24 divided by 6 equal?", answers:["4","four"]},
     {prompt:"How many minutes are in 1 hour?", answers:["60","sixty"]}
   ]},
  {subject:"Science", title:"Science Review: Bodies, Habitats, and Matter", summary:"Students review recent Science topics: our skeleton and joints, deserts, rainforests, ocean zones, compound machines, the rock cycle, our immune system, chemical and physical changes, and biomes.",
   resourceLabel:"YouTube: Science Review: Bodies, Habitats, and Matter", resourceUrl:"https://www.youtube.com/results?search_query=Science%20Review%3A%20Bodies%2C%20Habitats%2C%20and%20Matter%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of a joint in the body?", options:["The skin","The knee","The tongue","The hair"], answer:1},
     {q:"Which animal is well known for living in the rainforest?", options:["Penguin","Monkey","Polar bear","Camel"], answer:1},
     {q:"What is sedimentary rock?", options:["Rock that has no connection to layers","Rock formed from layers of sediment","Rock formed only from ice","Rock formed only from lava"], answer:1},
     {q:"Which of these is an example of a chemical change?", options:["Burning wood","Folding paper","Cutting a piece of string","Bending a paperclip"], answer:0},
     {q:"What is a biome?", options:["A kind of rock formation only","A single tree found in a forest","A type of ocean wave","A large natural area with its own climate, plants, and animals"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call the places where two bones meet?", answers:["joints"]},
     {prompt:"What kind of habitat is a desert?", answers:["a very dry habitat with little rain","a dry habitat"]},
     {prompt:"What is our immune system?", answers:["a team of body parts and cells that fight off germs","fights off germs"]}
   ]},
  {subject:"SocialStudies", title:"Social Studies Review: Laws, Trade, and Community Planning", summary:"Students review recent Social Studies topics: how laws are made, trade between countries, Canadian Confederation, non-profit organizations, natural resources, our postal system, city planning, global citizenship, and comparing jobs.",
   resourceLabel:"YouTube: Social Studies Review: Laws, Trade, and Community Planning", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Review%3A%20Laws%2C%20Trade%2C%20and%20Community%20Planning%20grade%202%20educational",
   quiz:[
     {q:"What are exports?", options:["Goods a country never sells","Money a country never uses","Goods a country only keeps for itself","Goods a country sends to another country"], answer:3},
     {q:"Which of these is an example of a Canadian natural resource?", options:["Paved roads","Plastic toys","Video games","Forests"], answer:3},
     {q:"What is city planning?", options:["Deciding where to build homes, roads, parks, and schools","A rule about how to bake bread","A story written by an author","A type of sport played outdoors"], answer:0},
     {q:"What is a global citizen?", options:["Someone who only thinks about their own street","Someone who considers how their actions affect people around the world","A person with no connection to other people","Someone who ignores every other country"], answer:1},
     {q:"Which job is most common in a rural area?", options:["Office work in a skyscraper","Farming","Skyscraper construction","Subway operator"], answer:1}
   ],
   worksheet:[
     {prompt:"Who is responsible for making laws?", answers:["elected governments","governments"]},
     {prompt:"What was Canadian Confederation?", answers:["separate colonies joining together to form the country of Canada","colonies joining together"]},
     {prompt:"What is a non-profit organization?", answers:["a group that uses donations to help people or causes","a group that helps people"]}
   ]},
]},
{day:91, label:"Day 91 — Mon", subjects:[
  {subject:"Language", title:"Personification: Giving Human Traits to Objects", summary:"Ontario Grade 2 Language strand: students learn that personification gives human qualities to an animal, object, or idea, such as saying the wind whispered or the sun smiled, to make writing more vivid.",
   resourceLabel:"YouTube: Personification: Giving Human Traits to Objects", resourceUrl:"https://www.youtube.com/results?search_query=Personification%3A%20Giving%20Human%20Traits%20to%20Objects%20grade%202%20educational",
   quiz:[
     {q:"What is personification?", options:["A type of punctuation mark","Giving human qualities to an object, animal, or idea","A word that names a person only","A sentence with no meaning at all"], answer:1},
     {q:"Which sentence is an example of personification?", options:["The stars winked at us from the sky.","The stars are far away in the sky.","The sky has many stars in it.","The sky was dark and clear."], answer:0},
     {q:"In the sentence the old car groaned as it started, what is being given a human quality?", options:["The key","The car","The driver","The road"], answer:1},
     {q:"Why might a writer use personification in a story?", options:["To make objects and animals feel more alive and interesting","Personification is only used in math","Personification has no purpose in writing","Personification makes writing harder to understand"], answer:0},
     {q:"Which of these gives a human trait to the wind?", options:["The wind can be strong or gentle.","The wind is a type of weather.","The wind howled angrily through the trees.","The wind blows from the west today."], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call it when a writer gives human qualities to an object, like saying the wind whispered?", answers:["personification"]},
     {prompt:"In the sentence the leaves danced in the breeze, what human action is given to the leaves?", answers:["dancing","danced"]},
     {prompt:"Does personification make writing more vivid and interesting?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Multiplication Facts: 8s and 9s", summary:"Ontario Grade 2 Number strand: students practise and memorize multiplication facts for the 8 and 9 times tables, building on earlier work with the 2s, 3s, 4s, 5s, 6s, 7s, and 10s times tables.",
   resourceLabel:"YouTube: Multiplication Facts: 8s and 9s", resourceUrl:"https://www.youtube.com/results?search_query=Multiplication%20Facts%3A%208s%20and%209s%20grade%202%20educational",
   quiz:[
     {q:"What is 8 times 4?", options:["32","36","28","24"], answer:0},
     {q:"What is 9 times 3?", options:["30","27","18","24"], answer:1},
     {q:"What is 8 times 6?", options:["54","48","42","40"], answer:1},
     {q:"What is 9 times 5?", options:["45","36","50","40"], answer:0},
     {q:"What is 9 times 9?", options:["99","81","90","72"], answer:1}
   ],
   worksheet:[
     {prompt:"What is 8 times 3?", answers:["24","twenty-four"]},
     {prompt:"What is 9 times 2?", answers:["18","eighteen"]},
     {prompt:"What is 8 times 5?", answers:["40","forty"]}
   ]},
  {subject:"Science", title:"Vertebrates and Invertebrates: Animals With and Without Backbones", summary:"Ontario Grade 2 Life Systems strand: students learn that animals with a backbone are called vertebrates, such as fish and birds, while animals without a backbone, such as insects and worms, are called invertebrates.",
   resourceLabel:"YouTube: Vertebrates and Invertebrates: Animals With and Without Backbones", resourceUrl:"https://www.youtube.com/results?search_query=Vertebrates%20and%20Invertebrates%3A%20Animals%20With%20and%20Without%20Backbones%20grade%202%20educational",
   quiz:[
     {q:"What is a vertebrate?", options:["An animal that lives only in water","An animal that has no bones at all","An animal that has a backbone","A plant with a stem"], answer:2},
     {q:"What is an invertebrate?", options:["An animal that always has fur","An animal that does not have a backbone","An animal that can fly","A type of rock"], answer:1},
     {q:"Which of these is a vertebrate?", options:["A snail","A spider","A fish","A worm"], answer:2},
     {q:"Which of these is an invertebrate?", options:["A fish","An insect","A dog","A bird"], answer:1},
     {q:"Vertebrates and invertebrates are grouped based on whether they have a ___.", options:["Colour","Backbone","Home","Tail"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call an animal that has a backbone?", answers:["vertebrate"]},
     {prompt:"What do we call an animal that does not have a backbone?", answers:["invertebrate"]},
     {prompt:"Is a worm a vertebrate or an invertebrate?", answers:["invertebrate"]}
   ]},
  {subject:"SocialStudies", title:"Provincial and Territorial Symbols: Flowers, Birds, and Flags", summary:"Ontario Grade 2 Social Studies strand: students learn that each Canadian province and territory has its own symbols, such as an official flower, bird, and flag, that represent its identity.",
   resourceLabel:"YouTube: Provincial and Territorial Symbols: Flowers, Birds, and Flags", resourceUrl:"https://www.youtube.com/results?search_query=Provincial%20and%20Territorial%20Symbols%3A%20Flowers%2C%20Birds%2C%20and%20Flags%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of a provincial symbol?", options:["A single citys nickname","An official provincial flower","A national anthem only","A type of homework"], answer:1},
     {q:"Why might a province choose an official bird or flower?", options:["To represent something special about that province","Provinces are not allowed to have symbols","Every province must use the exact same symbols","Symbols have no connection to a province"], answer:0},
     {q:"What is the official flower of Ontario?", options:["The rose","The tulip","The trillium","The sunflower"], answer:2},
     {q:"Provincial flags are usually flown alongside the ___.", options:["Flag of another country","Canadian flag","No other flag at all","Flag of a different city only"], answer:1},
     {q:"Learning about provincial symbols helps us understand ___.", options:["What makes each province unique","That every province is identical","That only Ontario has symbols","That symbols are not important"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one kind of symbol a province might have, like a flower or a flag.", answers:["flower","flag","bird"]},
     {prompt:"Does each Canadian province and territory have its own set of symbols?", answers:["yes"]},
     {prompt:"What is the official flower of Ontario?", answers:["trillium"]}
   ]},
]},
{day:92, label:"Day 92 — Tue", subjects:[
  {subject:"Language", title:"Irregular Plural Nouns: Special Cases Like Mice and Geese", summary:"Ontario Grade 2 Language strand: students learn that some plural nouns do not simply add -s or -es, but change in a special way, such as mouse becoming mice, goose becoming geese, and child becoming children.",
   resourceLabel:"YouTube: Irregular Plural Nouns: Special Cases Like Mice and Geese", resourceUrl:"https://www.youtube.com/results?search_query=Irregular%20Plural%20Nouns%3A%20Special%20Cases%20Like%20Mice%20and%20Geese%20grade%202%20educational",
   quiz:[
     {q:"What is the plural of mouse?", options:["Mousees","Mouses","Mices","Mice"], answer:3},
     {q:"What is the plural of tooth?", options:["Teeth","Toothes","Tooths","Teeths"], answer:0},
     {q:"What is the plural of foot?", options:["Foots","Feets","Footes","Feet"], answer:3},
     {q:"What is the plural of child?", options:["Childrens","Childs","Children","Childes"], answer:2},
     {q:"Words like mice and geese are called irregular plurals because they ___.", options:["Are not real words","Always add -s at the end","Never change at all","Do not simply add -s or -es"], answer:3}
   ],
   worksheet:[
     {prompt:"What is the plural form of the word mouse?", answers:["mice"]},
     {prompt:"What is the plural form of the word child?", answers:["children"]},
     {prompt:"What is the plural form of the word goose?", answers:["geese"]}
   ]},
  {subject:"Math", title:"Division with Remainders: When Sharing Does Not Come Out Even", summary:"Ontario Grade 2 Number strand: students learn that when a group of objects cannot be shared equally, there may be some left over, called a remainder, such as sharing 10 stickers among 3 friends leaving 1 remainder.",
   resourceLabel:"YouTube: Division with Remainders: When Sharing Does Not Come Out Even", resourceUrl:"https://www.youtube.com/results?search_query=Division%20with%20Remainders%3A%20When%20Sharing%20Does%20Not%20Come%20Out%20Even%20grade%202%20educational",
   quiz:[
     {q:"If 9 cookies are shared equally among 4 people, how many cookies are left over?", options:["1","3","0","2"], answer:0},
     {q:"If 13 marbles are shared equally among 3 people, how many marbles are left over?", options:["3","0","2","1"], answer:3},
     {q:"What do we call the amount left over after sharing equally?", options:["A product","A factor","A remainder","A sum"], answer:2},
     {q:"If 8 crayons are shared equally among 2 people, is there a remainder?", options:["Yes, there are 3 left over","Yes, there are 2 left over","No, they share evenly","Yes, there is 1 left over"], answer:2},
     {q:"If 11 grapes are shared equally among 5 people, how many grapes are left over?", options:["0","1","2","3"], answer:1}
   ],
   worksheet:[
     {prompt:"If 10 stickers are shared equally among 3 friends, how many are left over as a remainder?", answers:["1","one"]},
     {prompt:"What do we call the amount left over when a group cannot be shared equally?", answers:["remainder"]},
     {prompt:"If 7 apples are shared equally among 2 people, how many apples are left over?", answers:["1","one"]}
   ]},
  {subject:"Science", title:"The Nervous System: How Our Brain Sends Messages", summary:"Ontario Grade 2 Life Systems strand: students learn that our nervous system, made up of the brain, spinal cord, and nerves, sends messages through our body so we can think, feel, and move.",
   resourceLabel:"YouTube: The Nervous System: How Our Brain Sends Messages", resourceUrl:"https://www.youtube.com/results?search_query=The%20Nervous%20System%3A%20How%20Our%20Brain%20Sends%20Messages%20grade%202%20educational",
   quiz:[
     {q:"What is the main job of the nervous system?", options:["To send messages through the body","To digest our food","To pump blood through the body","To help us breathe only"], answer:0},
     {q:"Which organ is the control centre of the nervous system?", options:["The lungs","The skin","The stomach","The brain"], answer:3},
     {q:"What connects the brain to the rest of the body to send messages?", options:["Blood only","Muscles only","Nerves","Bones only"], answer:2},
     {q:"If you touch something hot, what helps you feel pain and pull your hand away quickly?", options:["Your circulatory system only","Your skeletal system only","Your digestive system","Your nervous system"], answer:3},
     {q:"The spinal cord is best described as a pathway that ___.", options:["Filters air we breathe","Breaks down food for energy","Carries messages between the brain and body","Pumps blood to the heart"], answer:2}
   ],
   worksheet:[
     {prompt:"What organ is the control centre of our nervous system?", answers:["brain"]},
     {prompt:"Name one part of the nervous system besides the brain, like the spinal cord or nerves.", answers:["spinal cord","nerves"]},
     {prompt:"Does our nervous system help us feel, think, and move?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Levels of Leadership: Prime Minister, Premier, and Mayor", summary:"Ontario Grade 2 Social Studies strand: students learn that Canada has leaders at different levels of government, including the Prime Minister for the country, a Premier for each province, and a mayor for a city or town.",
   resourceLabel:"YouTube: Levels of Leadership: Prime Minister, Premier, and Mayor", resourceUrl:"https://www.youtube.com/results?search_query=Levels%20of%20Leadership%3A%20Prime%20Minister%2C%20Premier%2C%20and%20Mayor%20grade%202%20educational",
   quiz:[
     {q:"Who leads the entire country of Canada?", options:["The premier","The principal","The mayor","The prime minister"], answer:3},
     {q:"Who leads a province, such as Ontario?", options:["The mayor","The prime minister","The premier","The governor"], answer:2},
     {q:"Who leads a city or town?", options:["The mayor","The prime minister","The principal","The premier"], answer:0},
     {q:"Why does Canada have leaders at different levels?", options:["Leaders at different levels never work together","This concept has no connection to Canada","Different levels of government handle different responsibilities","Only one leader is needed for everything"], answer:2},
     {q:"Which leader is responsible for decisions about a single city, like fixing local roads?", options:["The premier","A senator","The mayor","The prime minister"], answer:2}
   ],
   worksheet:[
     {prompt:"Who is the leader of the whole country of Canada?", answers:["prime minister"]},
     {prompt:"Who is the leader of a province, like Ontario?", answers:["premier"]},
     {prompt:"Who is the leader of a city or town?", answers:["mayor"]}
   ]},
]},
{day:93, label:"Day 93 — Wed", subjects:[
  {subject:"Language", title:"Making Inferences: Reading Between the Lines", summary:"Ontario Grade 2 Reading strand: students learn to make an inference by using clues from the text along with what they already know to figure out something the author does not state directly.",
   resourceLabel:"YouTube: Making Inferences: Reading Between the Lines", resourceUrl:"https://www.youtube.com/results?search_query=Making%20Inferences%3A%20Reading%20Between%20the%20Lines%20grade%202%20educational",
   quiz:[
     {q:"What is an inference?", options:["A sentence copied exactly from the text","A word written in bold letters","A conclusion made using text clues and what you already know","The title of a book"], answer:2},
     {q:"If a character is smiling and jumping up and down, what might you infer about how they feel?", options:["They feel nothing at all","They feel sick","They feel happy or excited","They feel angry"], answer:2},
     {q:"Which clue would help you infer that it is raining outside?", options:["Characters are wearing sunglasses","Characters are carrying umbrellas and wearing raincoats","Characters are building a snowman","Characters are swimming in a pool"], answer:1},
     {q:"Why is making inferences an important reading skill?", options:["Making inferences means ignoring the text completely","It has no connection to understanding a story","Inferences are always stated directly by the author","It helps readers understand ideas the author does not state directly"], answer:3},
     {q:"Making an inference is different from a fact because an inference is ___.", options:["Always written in the text exactly as shown","Never based on any clues at all","The same thing as a fact","A conclusion based on clues, not something directly stated"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call figuring out something the author does not state directly, using clues?", answers:["inference","making an inference"]},
     {prompt:"If a character is shivering and wearing a coat, what might you infer about the weather?", answers:["it is cold","cold"]},
     {prompt:"Do readers use clues from the text and what they already know to make an inference?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Naming Fraction Parts: Numerator and Denominator", summary:"Ontario Grade 2 Number strand: students learn the vocabulary for the parts of a fraction, where the denominator shows how many equal parts a whole is divided into, and the numerator shows how many of those parts are being counted.",
   resourceLabel:"YouTube: Naming Fraction Parts: Numerator and Denominator", resourceUrl:"https://www.youtube.com/results?search_query=Naming%20Fraction%20Parts%3A%20Numerator%20and%20Denominator%20grade%202%20educational",
   quiz:[
     {q:"In the fraction 2 over 5, what is the numerator?", options:["5","7","3","2"], answer:3},
     {q:"In the fraction 2 over 5, what is the denominator?", options:["2","7","5","3"], answer:2},
     {q:"What does the denominator of a fraction tell us?", options:["The exact colour of the shape","How many equal parts the whole is divided into","The total number of shapes","How many parts are shaded or counted"], answer:1},
     {q:"What does the numerator of a fraction tell us?", options:["How many of the equal parts are being counted","The name of the shape","The size of the whole shape","How many parts the whole is divided into"], answer:0},
     {q:"In the fraction 1 over 2, what does the number 2 represent?", options:["Only 2 parts are shaded","The shape is 2 centimetres long","The whole is divided into 2 equal parts","The shape has 2 corners"], answer:2}
   ],
   worksheet:[
     {prompt:"In the fraction 3 over 4, what number is the numerator?", answers:["3","three"]},
     {prompt:"In the fraction 3 over 4, what number is the denominator?", answers:["4","four"]},
     {prompt:"Does the denominator show how many equal parts a whole is divided into?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Layers of the Earth: Crust, Mantle, and Core", summary:"Ontario Grade 2 Earth and Space Systems strand: students learn that the Earth is made of layers, including the outer crust we live on, the hot mantle beneath it, and the core at the very centre.",
   resourceLabel:"YouTube: Layers of the Earth: Crust, Mantle, and Core", resourceUrl:"https://www.youtube.com/results?search_query=Layers%20of%20the%20Earth%3A%20Crust%2C%20Mantle%2C%20and%20Core%20grade%202%20educational",
   quiz:[
     {q:"What is the outermost layer of the Earth called?", options:["The core","The atmosphere","The mantle","The crust"], answer:3},
     {q:"What is the layer at the very centre of the Earth called?", options:["The crust","The core","The mantle","The surface"], answer:1},
     {q:"Which layer of the Earth is located between the crust and the core?", options:["The atmosphere","The soil","The mantle","The ocean"], answer:2},
     {q:"Which layer of the Earth do people, animals, and plants live on?", options:["The ocean floor only","The mantle","The core","The crust"], answer:3},
     {q:"The layers of the Earth are best described as being arranged from the ___ to the very centre.", options:["Sky downward","Centre outward only","Ocean upward","Outside surface inward"], answer:3}
   ],
   worksheet:[
     {prompt:"What is the outer layer of the Earth called, the one we live on?", answers:["crust"]},
     {prompt:"What is the very centre layer of the Earth called?", answers:["core"]},
     {prompt:"Is the mantle located between the crust and the core?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Voting and Elections: How We Choose Our Leaders", summary:"Ontario Grade 2 Social Studies strand: students learn that in an election, people vote to choose their leaders, such as a mayor or prime minister, and that the person with the most votes usually wins.",
   resourceLabel:"YouTube: Voting and Elections: How We Choose Our Leaders", resourceUrl:"https://www.youtube.com/results?search_query=Voting%20and%20Elections%3A%20How%20We%20Choose%20Our%20Leaders%20grade%202%20educational",
   quiz:[
     {q:"What is an election?", options:["A type of holiday celebration","A kind of school assignment","A game played at recess","An event where people vote to choose their leaders"], answer:3},
     {q:"What does it mean to vote?", options:["To build something out of blocks","To draw a picture of a leader","To mark your choice for a leader or decision","To ignore an important decision"], answer:2},
     {q:"In most elections, who usually wins?", options:["The tallest person","The person with the most votes","The person who votes last","The person who does not run at all"], answer:1},
     {q:"Why is voting an important part of choosing leaders?", options:["Elections never actually happen","Only one single person is allowed to decide","Voting has no effect on who becomes a leader","It lets many people have a say in who leads them"], answer:3},
     {q:"Elections allow citizens to ___.", options:["Avoid all responsibility for their community","Ignore their communitys leadership","Help choose who represents them","Prevent leaders from ever changing"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call the event where people choose their leaders by voting?", answers:["election"]},
     {prompt:"What do we call marking a choice for a leader during an election?", answers:["voting","a vote"]},
     {prompt:"Does the leader with the most votes usually win an election?", answers:["yes"]}
   ]},
]},
{day:94, label:"Day 94 — Thu", subjects:[
  {subject:"Language", title:"Using a Table of Contents and Index", summary:"Ontario Grade 2 Reading strand: students learn that a table of contents at the front of a book lists chapters and page numbers, while an index at the back lists topics in alphabetical order to help readers find information quickly.",
   resourceLabel:"YouTube: Using a Table of Contents and Index", resourceUrl:"https://www.youtube.com/results?search_query=Using%20a%20Table%20of%20Contents%20and%20Index%20grade%202%20educational",
   quiz:[
     {q:"What is a table of contents?", options:["A drawing on the cover of a book","A list of chapters and page numbers at the front of a book","A summary of the whole book","A list of every word in a book"], answer:1},
     {q:"What is an index?", options:["A picture of the main character","An alphabetical list of topics and their page numbers at the back of a book","A list of chapters at the front of a book","The name of the author"], answer:1},
     {q:"If you wanted to quickly find which chapter starts on page 20, which part of the book would help?", options:["The back cover","The table of contents","The title page","The index"], answer:1},
     {q:"If you wanted to find every page that mentions volcanoes, which part of the book would help most?", options:["The dedication page","The front cover","The table of contents","The index"], answer:3},
     {q:"Both a table of contents and an index help readers ___.", options:["Draw new pictures for the book","Ignore the book completely","Memorize the entire book","Find information in a book quickly"], answer:3}
   ],
   worksheet:[
     {prompt:"Where in a book would you usually find a table of contents, the front or the back?", answers:["front"]},
     {prompt:"Where in a book would you usually find an index, the front or the back?", answers:["back"]},
     {prompt:"Is an index organized in alphabetical order?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Rounding to the Nearest Hundred", summary:"Ontario Grade 2 Number strand: students learn to round three-digit numbers to the nearest hundred by looking at the tens digit, building on earlier work rounding to the nearest ten.",
   resourceLabel:"YouTube: Rounding to the Nearest Hundred", resourceUrl:"https://www.youtube.com/results?search_query=Rounding%20to%20the%20Nearest%20Hundred%20grade%202%20educational",
   quiz:[
     {q:"What is 180 rounded to the nearest hundred?", options:["200","190","100","180"], answer:0},
     {q:"What is 620 rounded to the nearest hundred?", options:["500","600","650","700"], answer:1},
     {q:"What is 750 rounded to the nearest hundred?", options:["800","750","600","700"], answer:0},
     {q:"To round a number to the nearest hundred, which digit do we look at?", options:["The thousands digit","The ones digit","The tens digit","The first letter"], answer:2},
     {q:"What is 910 rounded to the nearest hundred?", options:["910","900","800","1000"], answer:1}
   ],
   worksheet:[
     {prompt:"What is 340 rounded to the nearest hundred?", answers:["300","three hundred"]},
     {prompt:"What is 470 rounded to the nearest hundred?", answers:["500","five hundred"]},
     {prompt:"What is 250 rounded to the nearest hundred?", answers:["300","three hundred"]}
   ]},
  {subject:"Science", title:"Volcanoes: When Earth Crust Erupts", summary:"Ontario Grade 2 Earth and Space Systems strand: students learn that a volcano is an opening in the Earth crust where hot melted rock, called magma, can erupt onto the surface as lava.",
   resourceLabel:"YouTube: Volcanoes: When Earth Crust Erupts", resourceUrl:"https://www.youtube.com/results?search_query=Volcanoes%3A%20When%20Earth%20Crust%20Erupts%20grade%202%20educational",
   quiz:[
     {q:"What is a volcano?", options:["A type of large lake","An opening in the Earth crust where melted rock can erupt","A kind of ocean current","A very tall, cold mountain only"], answer:1},
     {q:"What is magma?", options:["Hot melted rock found underground","A kind of soil","Cold hard rock found on the surface","A type of cloud"], answer:0},
     {q:"What do we call magma once it erupts onto the surface?", options:["Sediment","Ash only","Mist","Lava"], answer:3},
     {q:"Why might a volcanic eruption be dangerous?", options:["Eruptions have no effect on the surrounding area","Lava is always cool to the touch","Hot lava and ash can spread over a wide area","Volcanoes never actually erupt"], answer:2},
     {q:"A volcano is best described as a place where the Earth crust can ___.", options:["Release hot melted rock","Disappear entirely","Freeze completely solid","Turn into water"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call an opening in the Earth crust where hot melted rock can erupt?", answers:["volcano"]},
     {prompt:"What do we call hot melted rock while it is still underground?", answers:["magma"]},
     {prompt:"What do we call hot melted rock once it erupts onto the surface?", answers:["lava"]}
   ]},
  {subject:"SocialStudies", title:"The Fur Trade: An Early Canadian Industry", summary:"Ontario Grade 2 Social Studies strand: students learn that the fur trade was an early industry in Canadian history, where Indigenous peoples and European traders exchanged furs, such as beaver pelts, for goods.",
   resourceLabel:"YouTube: The Fur Trade: An Early Canadian Industry", resourceUrl:"https://www.youtube.com/results?search_query=The%20Fur%20Trade%3A%20An%20Early%20Canadian%20Industry%20grade%202%20educational",
   quiz:[
     {q:"What was the fur trade?", options:["A kind of school subject","A modern clothing store","A type of Canadian sport","An early industry where furs were exchanged for goods"], answer:3},
     {q:"Which animal fur was especially important during the fur trade?", options:["The elephant","The beaver","The kangaroo","The lion"], answer:1},
     {q:"Who took part in the fur trade in early Canada?", options:["No one actually took part","Only modern-day shoppers","Indigenous peoples and European traders","Only people living in cities today"], answer:2},
     {q:"Why was the fur trade important to early Canadian history?", options:["It only happened in a different country","It has no connection to Canadian history","It never actually involved any trading","It shaped trade relationships and early settlements"], answer:3},
     {q:"The fur trade is an example of people exchanging goods, which we call ___.", options:["Trading","Building","Farming","Voting"], answer:0}
   ],
   worksheet:[
     {prompt:"What animal fur was especially valuable during the fur trade?", answers:["beaver"]},
     {prompt:"Did Indigenous peoples and European traders exchange goods during the fur trade?", answers:["yes"]},
     {prompt:"What word describes trading goods like furs for other items?", answers:["trade","trading"]}
   ]},
]},
{day:95, label:"Day 95 — Fri", subjects:[
  {subject:"Language", title:"Prefixes: dis- and mis-", summary:"Ontario Grade 2 Language strand: students learn that adding the prefix dis- or mis- to a word can change its meaning to the opposite or to something done incorrectly, such as agree becoming disagree and spell becoming misspell.",
   resourceLabel:"YouTube: Prefixes: dis- and mis-", resourceUrl:"https://www.youtube.com/results?search_query=Prefixes%3A%20dis-%20and%20mis-%20grade%202%20educational",
   quiz:[
     {q:"What does adding dis- to the word agree create?", options:["Agreement, a completely unrelated noun","Disagree, meaning the opposite of agree","A word with no real meaning","Agreeing, a different verb form"], answer:1},
     {q:"What does adding mis- to the word spell create?", options:["Spelling, a different verb form","Misspell, meaning to spell incorrectly","Spellful, an unrelated word","A word with no real meaning"], answer:1},
     {q:"Which word means the opposite of obey?", options:["Reobey","Obeyness","Disobey","Obeyful"], answer:2},
     {q:"Which word means to understand something incorrectly?", options:["Understandful","Disunderstand","Reunderstand","Misunderstand"], answer:3},
     {q:"Adding dis- or mis- to a word usually changes its meaning to show ___.", options:["A brighter colour","A faster speed","A larger size","The opposite or an incorrect action"], answer:3}
   ],
   worksheet:[
     {prompt:"Add dis- to the word agree. What new word do you make?", answers:["disagree"]},
     {prompt:"Add mis- to the word spell. What new word do you make?", answers:["misspell"]},
     {prompt:"Does adding dis- to a word often make it mean the opposite?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Equivalent Fractions: Different Names for the Same Amount", summary:"Ontario Grade 2 Number strand: students learn that two fractions can be equivalent, meaning they name the same amount, such as one half being the same amount as two quarters.",
   resourceLabel:"YouTube: Equivalent Fractions: Different Names for the Same Amount", resourceUrl:"https://www.youtube.com/results?search_query=Equivalent%20Fractions%3A%20Different%20Names%20for%20the%20Same%20Amount%20grade%202%20educational",
   quiz:[
     {q:"Which fraction is equivalent to one half?", options:["One third","Two quarters","Three quarters","One quarter"], answer:1},
     {q:"What does it mean for two fractions to be equivalent?", options:["They always look exactly the same on paper","They name the same amount","One fraction must be larger","They can never be compared"], answer:1},
     {q:"If a pizza is cut into 4 equal slices and you eat 2, what fraction is equivalent to what you ate?", options:["One half","One quarter","One third","Three quarters"], answer:0},
     {q:"Two fractions can look different but still be ___.", options:["Equivalent, naming the same amount","Impossible to compare","Always the exact same numbers","Always unrelated to each other"], answer:0},
     {q:"Which of these shows an equivalent fraction pair?", options:["One third and one half","One quarter and three quarters","One half and two quarters","One half and one quarter"], answer:2}
   ],
   worksheet:[
     {prompt:"Is one half the same amount as two quarters?", answers:["yes"]},
     {prompt:"What word describes two fractions that name the same amount?", answers:["equivalent"]},
     {prompt:"Is two quarters equivalent to one half?", answers:["yes"]}
   ]},
  {subject:"Science", title:"Animal Body Coverings: Fur, Feathers, Scales, and Skin", summary:"Ontario Grade 2 Life Systems strand: students learn that animals have different body coverings, such as fur, feathers, scales, or smooth skin, which help protect them and suit the environment they live in.",
   resourceLabel:"YouTube: Animal Body Coverings: Fur, Feathers, Scales, and Skin", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Body%20Coverings%3A%20Fur%2C%20Feathers%2C%20Scales%2C%20and%20Skin%20grade%202%20educational",
   quiz:[
     {q:"Which animal body covering do birds usually have?", options:["Scales","Shells","Fur","Feathers"], answer:3},
     {q:"Which animal body covering do fish usually have?", options:["Fur","Scales","Wool","Feathers"], answer:1},
     {q:"Which animal body covering do mammals like bears usually have?", options:["Feathers","Fur","Scales","Shells"], answer:1},
     {q:"Why do animals have different body coverings?", options:["To help protect them and suit their environment","Body coverings only affect how an animal looks","All animals have the exact same body covering","Body coverings have no real purpose"], answer:0},
     {q:"A frog usually has what kind of body covering?", options:["Thick fur","Hard scales like a fish","Smooth, moist skin","Feathers"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one type of body covering an animal might have, like fur or feathers.", answers:["fur","feathers","scales","skin"]},
     {prompt:"Do birds usually have feathers as their body covering?", answers:["yes"]},
     {prompt:"Do fish usually have scales as their body covering?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Treaties: Agreements Between Indigenous Peoples and Newcomers", summary:"Ontario Grade 2 Social Studies strand: students learn that a treaty is a formal agreement, often about sharing land and resources, that was made between Indigenous peoples and newcomers to Canada.",
   resourceLabel:"YouTube: Treaties: Agreements Between Indigenous Peoples and Newcomers", resourceUrl:"https://www.youtube.com/results?search_query=Treaties%3A%20Agreements%20Between%20Indigenous%20Peoples%20and%20Newcomers%20grade%202%20educational",
   quiz:[
     {q:"What is a treaty?", options:["A type of Canadian sport","A kind of school subject","A formal agreement, often about sharing land and resources","A holiday celebrated in December"], answer:2},
     {q:"Who were treaties in Canadian history often made between?", options:["Only people from a different country entirely","No one, they never actually happened","Indigenous peoples and newcomers","Only people living in one single city"], answer:2},
     {q:"What might a treaty be an agreement about?", options:["What food to eat for breakfast","Sharing land and resources","Which sports team wins a game","What clothes to wear each day"], answer:1},
     {q:"Why are treaties an important part of Canadian history?", options:["They have no connection to Canadian history","They only affected people outside of Canada","They shaped relationships between Indigenous peoples and newcomers","They were never actually followed by anyone"], answer:2},
     {q:"Learning about treaties helps students understand ___.", options:["Important agreements in Canadian history","Nothing relevant about Canada","Only how to read a map","Only modern-day sports rules"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes a formal agreement about sharing land and resources?", answers:["treaty"]},
     {prompt:"Were treaties made between Indigenous peoples and newcomers to Canada?", answers:["yes"]},
     {prompt:"Do treaties often involve agreements about land?", answers:["yes"]}
   ]},
]},
{day:96, label:"Day 96 — Mon", subjects:[
  {subject:"Language", title:"Suffixes: Adding -ly to Turn Adjectives into Adverbs", summary:"Ontario Grade 2 Language strand: students learn that adding the suffix -ly to many adjectives creates an adverb, describing how an action is done, such as quiet becoming quietly and slow becoming slowly.",
   resourceLabel:"YouTube: Suffixes: Adding -ly to Turn Adjectives into Adverbs", resourceUrl:"https://www.youtube.com/results?search_query=Suffixes%3A%20Adding%20-ly%20to%20Turn%20Adjectives%20into%20Adverbs%20grade%202%20educational",
   quiz:[
     {q:"What does adding -ly to the word slow create?", options:["Sloth, an unrelated word","Slower, a comparing word","Slowly, an adverb describing how something is done","Slowness, a different noun"], answer:2},
     {q:"Which word is an adverb formed by adding -ly?", options:["Quieter","Quietly","Quietness","Quiet"], answer:1},
     {q:"In the sentence she ran quickly, what does the word quickly describe?", options:["How she ran","Where she is going","Who she is","What she is wearing"], answer:0},
     {q:"Add -ly to the word careful. What new word do you make?", options:["Carefully","Carefuler","Carefulness","Careless"], answer:0},
     {q:"Adding -ly to an adjective usually creates a word that describes ___.", options:["A person or place","A colour only","How an action happens","A number of objects"], answer:2}
   ],
   worksheet:[
     {prompt:"Add -ly to the word quiet. What new word do you make?", answers:["quietly"]},
     {prompt:"Add -ly to the word slow. What new word do you make?", answers:["slowly"]},
     {prompt:"Does an adverb ending in -ly usually describe how an action is done?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Multi-Step Word Problems: Addition and Subtraction Together", summary:"Ontario Grade 2 Number strand: students learn to solve word problems that require more than one step, such as adding two amounts together and then subtracting a third amount, to find a final answer.",
   resourceLabel:"YouTube: Multi-Step Word Problems: Addition and Subtraction Together", resourceUrl:"https://www.youtube.com/results?search_query=Multi-Step%20Word%20Problems%3A%20Addition%20and%20Subtraction%20Together%20grade%202%20educational",
   quiz:[
     {q:"A boy has 6 marbles, finds 5 more, then loses 4. How many marbles does he have now?", options:["6","11","8","7"], answer:3},
     {q:"A class has 12 pencils, gets 8 more, then gives away 6. How many pencils are left?", options:["14","6","12","20"], answer:0},
     {q:"A farmer has 20 eggs, sells 9, then collects 5 more. How many eggs does the farmer have now?", options:["16","25","15","11"], answer:0},
     {q:"What is the first step when solving a multi-step word problem?", options:["Skipping the problem entirely","Only reading the last sentence","Guessing the answer with no plan","Figuring out what the problem is asking and what steps are needed"], answer:3},
     {q:"A store has 15 toys, sells 7, then receives 10 more. How many toys does the store have now?", options:["15","18","25","8"], answer:1}
   ],
   worksheet:[
     {prompt:"If you have 5 apples, get 4 more, then give away 3, how many apples do you have left?", answers:["6","six"]},
     {prompt:"What does a multi-step word problem require you to do?", answers:["more than one step","more than one operation"]},
     {prompt:"If you start with 10 stickers, get 5 more, then use 2, how many stickers are left?", answers:["13","thirteen"]}
   ]},
  {subject:"Science", title:"Symbiosis: When Living Things Help Each Other", summary:"Ontario Grade 2 Life Systems strand: students learn that symbiosis is a close relationship between two different living things, such as bees and flowers, where one or both living things benefit.",
   resourceLabel:"YouTube: Symbiosis: When Living Things Help Each Other", resourceUrl:"https://www.youtube.com/results?search_query=Symbiosis%3A%20When%20Living%20Things%20Help%20Each%20Other%20grade%202%20educational",
   quiz:[
     {q:"What is symbiosis?", options:["A type of rock formation","A single living thing with no relationships","A kind of weather pattern","A close relationship between two different living things"], answer:3},
     {q:"Which of these is an example of symbiosis?", options:["A cloud floating in the sky","A river flowing downhill","Bees collecting nectar and pollinating flowers","A rock sitting in a field"], answer:2},
     {q:"How do flowers benefit when bees visit them?", options:["Flowers have no connection to bees","Flowers are harmed every time a bee visits","Bees help spread pollen so flowers can make seeds","Bees never actually visit flowers"], answer:2},
     {q:"How do bees benefit from visiting flowers?", options:["Bees are harmed by visiting flowers","Bees gain nothing at all from flowers","Bees only visit flowers for shelter","Bees collect nectar from flowers for food"], answer:3},
     {q:"Symbiosis shows that living things in nature are often ___.", options:["Connected and can help each other","Completely unrelated to each other","Never able to interact at all","Always in danger from each other"], answer:0}
   ],
   worksheet:[
     {prompt:"What word describes a close relationship between two different living things?", answers:["symbiosis"]},
     {prompt:"Name one pair of living things that help each other, like bees and flowers.", answers:["bees and flowers"]},
     {prompt:"Can symbiosis benefit one or both living things involved?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"The United Nations: Countries Working Together", summary:"Ontario Grade 2 Social Studies strand: students learn that the United Nations is a group made up of many countries, including Canada, that work together to solve world problems and keep peace.",
   resourceLabel:"YouTube: The United Nations: Countries Working Together", resourceUrl:"https://www.youtube.com/results?search_query=The%20United%20Nations%3A%20Countries%20Working%20Together%20grade%202%20educational",
   quiz:[
     {q:"What is the United Nations?", options:["A single countrys government only","A kind of school club","A type of sports league","A group of many countries that work together to solve world problems"], answer:3},
     {q:"Is Canada a member of the United Nations?", options:["Only some Canadian cities are members","Canada left the United Nations long ago","No, Canada has never joined","Yes, Canada is a member"], answer:3},
     {q:"What is one goal of the United Nations?", options:["To end all forms of cooperation","To stop countries from ever meeting","To help keep peace around the world","To make every country identical"], answer:2},
     {q:"Why might countries choose to work together through an organization like the United Nations?", options:["Countries never benefit from working together","This concept has no connection to global citizenship","Working together can help solve problems that affect many countries","Only one single country can solve world problems alone"], answer:2},
     {q:"The United Nations is best described as an organization that helps countries ___.", options:["Cooperate on shared world problems","Avoid working together at all costs","Compete against each other constantly","Ignore problems in other countries"], answer:0}
   ],
   worksheet:[
     {prompt:"What do we call the group made up of many countries working together?", answers:["United Nations"]},
     {prompt:"Is Canada a member of the United Nations?", answers:["yes"]},
     {prompt:"Does the United Nations try to help keep peace around the world?", answers:["yes"]}
   ]},
]},
{day:97, label:"Day 97 — Tue", subjects:[
  {subject:"Language", title:"Sentence Variety: Combining Short and Long Sentences", summary:"Ontario Grade 2 Writing strand: students learn that mixing short and long sentences in a piece of writing creates sentence variety, which can make writing more interesting to read.",
   resourceLabel:"YouTube: Sentence Variety: Combining Short and Long Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Sentence%20Variety%3A%20Combining%20Short%20and%20Long%20Sentences%20grade%202%20educational",
   quiz:[
     {q:"What is sentence variety?", options:["Using only short sentences","Mixing short and long sentences in writing","Using only long sentences","Never using any punctuation"], answer:1},
     {q:"Why might a writer use sentence variety?", options:["Sentence variety makes writing harder to read","To make writing more interesting to read","Writers should always use the exact same sentence length","Sentence variety has no purpose in writing"], answer:1},
     {q:"Which set of sentences shows good sentence variety?", options:["The dog ran. Excited and full of energy, it bounded across the yard chasing the ball.","Dog. Dog ran. Dog jumped. Dog barked.","The dog ran fast fast fast fast fast.","The dog ran. The dog jumped. The dog barked. The dog played."], answer:0},
     {q:"What might happen if a writer only uses short, choppy sentences?", options:["The writing always sounds more interesting","Short sentences are always better than long ones","This has no effect on how writing sounds","The writing might sound repetitive or robotic"], answer:3},
     {q:"Using a mix of sentence lengths can help writing sound more ___.", options:["Repetitive and boring","Confusing and unclear","Natural and engaging","Impossible to read"], answer:2}
   ],
   worksheet:[
     {prompt:"What do we call mixing short and long sentences in writing?", answers:["sentence variety"]},
     {prompt:"Can using only short sentences over and over make writing sound choppy?", answers:["yes"]},
     {prompt:"Does sentence variety help make writing more interesting to read?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Conducting a Survey and Graphing the Results", summary:"Ontario Grade 2 Data strand: students learn to collect data by asking classmates a survey question, then organize and display the results using a graph, such as a bar graph or pictograph.",
   resourceLabel:"YouTube: Conducting a Survey and Graphing the Results", resourceUrl:"https://www.youtube.com/results?search_query=Conducting%20a%20Survey%20and%20Graphing%20the%20Results%20grade%202%20educational",
   quiz:[
     {q:"What is a survey?", options:["A question asked to collect information from people","A kind of math equation","A type of graph only","A drawing of a shape"], answer:0},
     {q:"After conducting a survey about favourite fruits, what is a good next step?", options:["Organize the results and display them on a graph","Ask the exact same question forever","Ignore what people said","Throw away all the answers"], answer:0},
     {q:"Which of these could be a good survey question for a class?", options:["What is 5 plus 5?","What colour is the sky today?","What is your favourite season?","What is the capital of France?"], answer:2},
     {q:"Why is it useful to graph the results of a survey?", options:["A graph makes the results easier to see and compare","Surveys should never be graphed","Graphs make survey results harder to understand","Graphing has no connection to data"], answer:0},
     {q:"Collecting survey data and graphing it is part of the ___ strand in math.", options:["Patterning","Data","Geometry","Measurement"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call asking people a question to collect information?", answers:["a survey"]},
     {prompt:"After collecting survey data, what can be used to display the results?", answers:["a graph","a bar graph","a pictograph"]},
     {prompt:"Does a survey help us collect information from a group of people?", answers:["yes"]}
   ]},
  {subject:"Science", title:"How Animals Communicate: Sounds, Signals, and Body Language", summary:"Ontario Grade 2 Life Systems strand: students learn that animals communicate with each other using sounds, body language, and signals, such as a dog wagging its tail or a bird singing a song.",
   resourceLabel:"YouTube: How Animals Communicate: Sounds, Signals, and Body Language", resourceUrl:"https://www.youtube.com/results?search_query=How%20Animals%20Communicate%3A%20Sounds%2C%20Signals%2C%20and%20Body%20Language%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a way animals communicate?", options:["Using a telephone","Reading a book","Writing a letter","Making sounds"], answer:3},
     {q:"What might a dog wagging its tail be communicating?", options:["That it cannot see anything","That it is asleep","That it feels happy or excited","That it is a different animal"], answer:2},
     {q:"Why might a bird sing a song?", options:["Birds never make any sounds","Only humans can communicate with sound","To communicate with other birds","Singing has no purpose for birds"], answer:2},
     {q:"Which of these is an example of animal body language?", options:["A cat with closed eyes","A cat arching its back when scared","A cat sleeping quietly","A cat eating its food"], answer:1},
     {q:"Animal communication helps animals ___.", options:["Warn others, find mates, or protect their group","Ignore danger completely","Never interact with other animals","Avoid all other animals forever"], answer:0}
   ],
   worksheet:[
     {prompt:"Name one way an animal might communicate, like making a sound or using body language.", answers:["sound","body language"]},
     {prompt:"Can a wagging tail be a way a dog communicates?", answers:["yes"]},
     {prompt:"Do animals use sounds to communicate with each other?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Agriculture Regions: What Grows Where", summary:"Ontario Grade 2 Social Studies strand: students learn that different regions of Canada grow different crops and raise different animals based on their climate and land, such as wheat on the Prairies and fruit in Ontario.",
   resourceLabel:"YouTube: Canadian Agriculture Regions: What Grows Where", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Agriculture%20Regions%3A%20What%20Grows%20Where%20grade%202%20educational",
   quiz:[
     {q:"Which crop is commonly grown on the Canadian Prairies?", options:["Pineapples","Bananas","Coconuts","Wheat"], answer:3},
     {q:"Why does the Prairie region grow so much wheat?", options:["Its flat land and climate are well suited to growing grain crops","Wheat cannot grow anywhere in Canada","The Prairies have no farmland at all","The Prairies are covered entirely in ice year-round"], answer:0},
     {q:"What helps farmers decide what crops to grow in a region?", options:["The climate and type of land in that region","The name of the province only","The colour of the sky","Farmers never consider climate or land"], answer:0},
     {q:"Which of these is grown in parts of Ontario?", options:["Fruit, such as apples and peaches","Only bananas","Only rice","Only coconuts"], answer:0},
     {q:"Comparing farming across Canadian regions helps us understand ___.", options:["That farming does not exist in Canada","That every region grows the exact same crops","That climate has no effect on farming","How climate and land affect what people grow"], answer:3}
   ],
   worksheet:[
     {prompt:"Name one crop grown in a Canadian region, like wheat on the Prairies.", answers:["wheat"]},
     {prompt:"Does the type of crop grown in a region depend on its climate and land?", answers:["yes"]},
     {prompt:"Name one fruit or crop commonly grown in Ontario.", answers:["fruit","corn","apples"]}
   ]},
]},
{day:98, label:"Day 98 — Wed", subjects:[
  {subject:"Language", title:"Personal Narrative Writing: Telling a True Story About Yourself", summary:"Ontario Grade 2 Writing strand: students learn to write a personal narrative, a true story about something that happened to them, told in order with a beginning, middle, and end, and including their own feelings.",
   resourceLabel:"YouTube: Personal Narrative Writing: Telling a True Story About Yourself", resourceUrl:"https://www.youtube.com/results?search_query=Personal%20Narrative%20Writing%3A%20Telling%20a%20True%20Story%20About%20Yourself%20grade%202%20educational",
   quiz:[
     {q:"What is a personal narrative?", options:["A made-up story about dragons","A true story about something that happened to the writer","A drawing with no words","A list of math facts"], answer:1},
     {q:"Which of these would be a good topic for a personal narrative?", options:["The life cycle of a butterfly","The capital city of Ontario","A time you visited your grandparents","How to multiply two numbers"], answer:2},
     {q:"Why might a writer include their own feelings in a personal narrative?", options:["Feelings should never be included in writing","It helps readers understand the experience more fully","Personal narratives cannot include any feelings","This concept has no connection to narrative writing"], answer:1},
     {q:"A personal narrative is different from a book review because a narrative ___.", options:["Only reviews someone elses book","Tells a true story about the writer","Is always about a made-up character","Never includes any events"], answer:1},
     {q:"A well organized personal narrative usually has a ___.", options:["Only a title page","No clear order at all","Only a middle","Beginning, middle, and end"], answer:3}
   ],
   worksheet:[
     {prompt:"What kind of writing tells a true story about something that happened to you?", answers:["personal narrative"]},
     {prompt:"Should a personal narrative be told in order, with a beginning, middle, and end?", answers:["yes"]},
     {prompt:"Can a personal narrative include how you felt during the event?", answers:["yes"]}
   ]},
  {subject:"Math", title:"Problem Solving: Choosing the Right Operation", summary:"Ontario Grade 2 Number strand: students learn to read a word problem carefully and decide whether to add, subtract, multiply, or divide based on the clues and the question being asked.",
   resourceLabel:"YouTube: Problem Solving: Choosing the Right Operation", resourceUrl:"https://www.youtube.com/results?search_query=Problem%20Solving%3A%20Choosing%20the%20Right%20Operation%20grade%202%20educational",
   quiz:[
     {q:"If a problem asks how many items are left after some are given away, which operation should you use?", options:["Subtraction","Addition","Multiplication","Division"], answer:0},
     {q:"If a problem asks for the total after combining two groups, which operation should you use?", options:["Comparison","Addition","Subtraction","Division"], answer:1},
     {q:"If a problem asks how many items are in 4 equal groups of 5, which operation should you use?", options:["Subtraction","Addition of only one number","Division","Multiplication"], answer:3},
     {q:"If a problem asks how many equal groups can be made when sharing 20 items among 4 friends, which operation should you use?", options:["Addition","Multiplication","Subtraction","Division"], answer:3},
     {q:"Why is it important to read a word problem carefully before solving it?", options:["Reading carefully has no effect on solving problems","Every problem always uses the same operation","The words in a problem never matter","It helps you choose the correct operation to use"], answer:3}
   ],
   worksheet:[
     {prompt:"If a word problem asks how many are left, which operation might you use?", answers:["subtraction","subtract"]},
     {prompt:"If a word problem asks for a total when joining groups together, which operation might you use?", answers:["addition","add"]},
     {prompt:"If a word problem asks how many equal groups can be made from a total, which operation might you use?", answers:["division","divide"]}
   ]},
  {subject:"Science", title:"Extreme Weather: Storms and Severe Conditions", summary:"Ontario Grade 2 Earth and Space Systems strand: students learn about extreme weather events, such as thunderstorms, blizzards, and high winds, and how people can stay safe when severe weather happens.",
   resourceLabel:"YouTube: Extreme Weather: Storms and Severe Conditions", resourceUrl:"https://www.youtube.com/results?search_query=Extreme%20Weather%3A%20Storms%20and%20Severe%20Conditions%20grade%202%20educational",
   quiz:[
     {q:"Which of these is an example of extreme weather?", options:["A light cloud","A gentle breeze","A calm, sunny day","A thunderstorm"], answer:3},
     {q:"What is a blizzard?", options:["A warm, sunny day","A calm winter morning","A light rain shower","A severe snowstorm with strong winds"], answer:3},
     {q:"Why is it important to know about extreme weather?", options:["Extreme weather never actually happens","Extreme weather is never dangerous","So people can prepare and stay safe","Knowing about weather has no benefit"], answer:2},
     {q:"Which of these is a safe action during a thunderstorm?", options:["Staying indoors away from windows","Swimming in an open lake","Flying a kite outside","Standing under a tall tree outside"], answer:0},
     {q:"Extreme weather events can include storms with ___.", options:["Only gentle breezes","No weather at all","Strong winds, heavy snow, or thunder and lightning","Only clear blue skies"], answer:2}
   ],
   worksheet:[
     {prompt:"Name one type of extreme weather, like a thunderstorm or blizzard.", answers:["thunderstorm","blizzard"]},
     {prompt:"Can extreme weather include very strong winds?", answers:["yes"]},
     {prompt:"Is it important to stay safe during severe weather?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Canada and Its Neighbour: Sharing a Border with the United States", summary:"Ontario Grade 2 Social Studies strand: students learn that Canada shares a long border with the United States, its neighbouring country to the south, and that people, goods, and ideas often cross between the two countries.",
   resourceLabel:"YouTube: Canada and Its Neighbour: Sharing a Border with the United States", resourceUrl:"https://www.youtube.com/results?search_query=Canada%20and%20Its%20Neighbour%3A%20Sharing%20a%20Border%20with%20the%20United%20States%20grade%202%20educational",
   quiz:[
     {q:"Which country shares a long border with Canada to the south?", options:["Brazil","Mexico","The United States","France"], answer:2},
     {q:"What might cross the border between Canada and the United States?", options:["Only animals cross the border","People, goods, and ideas","Only mail crosses the border","Nothing ever crosses the border"], answer:1},
     {q:"Why might Canada and the United States work together on some issues?", options:["The two countries have no connection at all","Neighbouring countries never work together","They are located on opposite sides of the world","They are close neighbours who share a long border"], answer:3},
     {q:"Sharing a border with another country can lead to shared ___.", options:["Trade and travel between the two countries","Two countries becoming exactly identical","No interaction of any kind","A complete lack of any connection"], answer:0},
     {q:"Canada is located ___ of the United States.", options:["East","North","West","South"], answer:1}
   ],
   worksheet:[
     {prompt:"What country is located just south of Canada, sharing a long border?", answers:["United States"]},
     {prompt:"Do people and goods sometimes cross the border between Canada and the United States?", answers:["yes"]},
     {prompt:"Is the United States a neighbouring country of Canada?", answers:["yes"]}
   ]},
]},
{day:99, label:"Day 99 — Thu", subjects:[
  {subject:"Language", title:"Comparing Fiction and Nonfiction Texts", summary:"Ontario Grade 2 Reading strand: students learn to compare fiction texts, which tell made-up stories, with nonfiction texts, which give true facts and information about real topics.",
   resourceLabel:"YouTube: Comparing Fiction and Nonfiction Texts", resourceUrl:"https://www.youtube.com/results?search_query=Comparing%20Fiction%20and%20Nonfiction%20Texts%20grade%202%20educational",
   quiz:[
     {q:"What is fiction?", options:["A list of numbers","A text that gives only true facts","A made-up story that is not literally true","A drawing with no text"], answer:2},
     {q:"What is nonfiction?", options:["A text that gives true facts and information","A made-up story about talking animals","A story that is always false","A poem with no real meaning"], answer:0},
     {q:"Which of these is most likely a nonfiction book?", options:["A book about a talking dragon","A book about a magic castle","A book about how volcanoes form","A book about a wizard school"], answer:2},
     {q:"Which of these is most likely a fiction book?", options:["A book explaining the water cycle","A book about famous Canadian inventors","A book about how plants grow","A story about a superhero with magic powers"], answer:3},
     {q:"Comparing fiction and nonfiction helps readers understand ___.", options:["The difference between made-up stories and true information","That only fiction books exist","That every book is exactly the same","That fiction and nonfiction have no differences"], answer:0}
   ],
   worksheet:[
     {prompt:"Does a fiction text tell a made-up story or give true facts?", answers:["made-up story","a made-up story"]},
     {prompt:"Does a nonfiction text give true facts about a real topic?", answers:["yes"]},
     {prompt:"Is a book about dragons flying likely to be fiction or nonfiction?", answers:["fiction"]}
   ]},
  {subject:"Math", title:"Problem Solving: Choosing the Right Operation (Applied Practice)", summary:"Ontario Grade 2 Number strand: students apply their understanding of addition, subtraction, multiplication, and division to solve a variety of real-life word problems by first identifying what operation is needed.",
   resourceLabel:"YouTube: Problem Solving: Choosing the Right Operation (Applied Practice)", resourceUrl:"https://www.youtube.com/results?search_query=Problem%20Solving%3A%20Choosing%20the%20Right%20Operation%20%28Applied%20Practice%29%20grade%202%20educational",
   quiz:[
     {q:"If 3 friends each have 4 stickers, how many stickers do they have altogether?", options:["12","9","7","15"], answer:0},
     {q:"If a baker makes 24 muffins and sells 15, how many muffins are left?", options:["9","39","15","24"], answer:0},
     {q:"If 18 crayons are shared equally among 3 children, how many crayons does each child get?", options:["15","21","6","3"], answer:2},
     {q:"A problem states a class collected 45 cans on Monday and 30 more on Tuesday. What operation finds the total?", options:["Multiplication","Division","Subtraction","Addition"], answer:3},
     {q:"Applying the correct operation to a real-life problem helps us find the ___.", options:["Longest possible answer","Accurate and reasonable answer","Answer with no connection to the problem","Least accurate answer possible"], answer:1}
   ],
   worksheet:[
     {prompt:"If a problem asks how many stickers 3 friends have altogether if each has 4, which operation would you use?", answers:["multiplication","multiply"]},
     {prompt:"If a problem asks how many are left after some are used, which operation would you use?", answers:["subtraction","subtract"]},
     {prompt:"Why is it helpful to identify the operation before solving a word problem?", answers:["it helps you solve it correctly","to solve correctly"]}
   ]},
  {subject:"Science", title:"Ecosystems: How Living and Non-Living Things Work Together", summary:"Ontario Grade 2 Life Systems strand: students learn that an ecosystem is made up of living things, such as plants and animals, and non-living things, such as water, air, and soil, all interacting together in one place.",
   resourceLabel:"YouTube: Ecosystems: How Living and Non-Living Things Work Together", resourceUrl:"https://www.youtube.com/results?search_query=Ecosystems%3A%20How%20Living%20and%20Non-Living%20Things%20Work%20Together%20grade%202%20educational",
   quiz:[
     {q:"What is an ecosystem?", options:["A single plant growing alone","Only the rocks and water in a place","Living and non-living things interacting together in one place","Only the living things in a forest"], answer:2},
     {q:"Which of these is a non-living part of an ecosystem?", options:["A bird","Soil","A tree","A fish"], answer:1},
     {q:"Which of these is a living part of an ecosystem?", options:["A plant","Water","Sunlight","Air"], answer:0},
     {q:"Why do living things in an ecosystem depend on non-living things?", options:["They need things like water, air, and sunlight to survive","Non-living things have no effect on living things","Living things need nothing from their surroundings","This concept has no connection to ecosystems"], answer:0},
     {q:"An ecosystem is best described as a place where living and non-living things ___.", options:["Have no connection whatsoever","Never interact with each other at all","Interact and depend on each other","Exist completely separately"], answer:2}
   ],
   worksheet:[
     {prompt:"What word describes living and non-living things interacting together in one place?", answers:["ecosystem"]},
     {prompt:"Name one non-living part of an ecosystem, like water or soil.", answers:["water","air","soil"]},
     {prompt:"Do living things in an ecosystem depend on non-living things like water and air?", answers:["yes"]}
   ]},
  {subject:"SocialStudies", title:"Canadian Peacekeeping: Helping Keep the Peace Around the World", summary:"Ontario Grade 2 Social Studies strand: students learn that Canada has a history of sending peacekeepers to help calm conflicts and support peace in other parts of the world.",
   resourceLabel:"YouTube: Canadian Peacekeeping: Helping Keep the Peace Around the World", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Peacekeeping%3A%20Helping%20Keep%20the%20Peace%20Around%20the%20World%20grade%202%20educational",
   quiz:[
     {q:"What is a peacekeeper?", options:["A person sent to help calm conflict and support peace","A type of weather forecaster","A person who starts conflicts","A person who ignores world events"], answer:0},
     {q:"Has Canada historically taken part in peacekeeping missions?", options:["No, Canada has never taken part","Peacekeeping has never existed","Yes, Canada has a history of peacekeeping","Only other countries take part in peacekeeping"], answer:2},
     {q:"Why might a country send peacekeepers to another region?", options:["To help support peace during a conflict","To ignore problems happening elsewhere","Peacekeepers have no real purpose","To make a conflict worse"], answer:0},
     {q:"Peacekeeping is connected to which broader idea learned in social studies?", options:["Countries always working alone","Ignoring problems in other countries","Avoiding all international cooperation","Countries working together, like through the United Nations"], answer:3},
     {q:"Canadian peacekeepers are best described as people who help ___.", options:["Stay only within Canadian borders","Avoid helping anyone at all","Support peace in other parts of the world","Create new conflicts around the world"], answer:2}
   ],
   worksheet:[
     {prompt:"What word describes people sent to help calm conflict and support peace?", answers:["peacekeepers"]},
     {prompt:"Has Canada sent peacekeepers to help in other parts of the world?", answers:["yes"]},
     {prompt:"Does peacekeeping aim to support peace during a conflict?", answers:["yes"]}
   ]},
]},
{day:100, label:"Day 100 — Fri", subjects:[
  {subject:"Language", title:"Language Review: Figurative Language, Word Parts, and Text Types", summary:"Students review recent Language skills: personification, irregular plural nouns, making inferences, using a table of contents and index, prefixes dis- and mis-, suffixes -ly, sentence variety, personal narrative writing, and comparing fiction and nonfiction.",
   resourceLabel:"YouTube: Language Review: Figurative Language, Word Parts, and Text Types", resourceUrl:"https://www.youtube.com/results?search_query=Language%20Review%3A%20Figurative%20Language%2C%20Word%20Parts%2C%20and%20Text%20Types%20grade%202%20educational",
   quiz:[
     {q:"Which sentence is an example of personification?", options:["The stars winked at us from the sky.","The stars are far away in the sky.","The sky was dark and clear.","The sky has many stars in it."], answer:0},
     {q:"What is the plural of tooth?", options:["Teeths","Toothes","Tooths","Teeth"], answer:3},
     {q:"Which word means the opposite of obey?", options:["Obeyful","Disobey","Reobey","Obeyness"], answer:1},
     {q:"What is a personal narrative?", options:["A made-up story about dragons","A drawing with no words","A list of math facts","A true story about something that happened to the writer"], answer:3},
     {q:"Which of these is most likely a nonfiction book?", options:["A book about a talking dragon","A book about how volcanoes form","A book about a magic castle","A book about a wizard school"], answer:1}
   ],
   worksheet:[
     {prompt:"What do we call giving human qualities to an object, like saying the wind whispered?", answers:["personification"]},
     {prompt:"What is the plural form of the word mouse?", answers:["mice"]},
     {prompt:"What is an inference?", answers:["a conclusion made using text clues and what you already know","a conclusion using clues"]}
   ]},
  {subject:"Math", title:"Math Review: Multiplication, Fractions, and Problem Solving", summary:"Students review recent Math skills: multiplication facts for 8s and 9s, division with remainders, naming fraction parts, rounding to the nearest hundred, equivalent fractions, multi-step word problems, surveys and graphing, and choosing the right operation.",
   resourceLabel:"YouTube: Math Review: Multiplication, Fractions, and Problem Solving", resourceUrl:"https://www.youtube.com/results?search_query=Math%20Review%3A%20Multiplication%2C%20Fractions%2C%20and%20Problem%20Solving%20grade%202%20educational",
   quiz:[
     {q:"What is 9 times 3?", options:["30","18","24","27"], answer:3},
     {q:"What is 620 rounded to the nearest hundred?", options:["650","500","600","700"], answer:2},
     {q:"Which fraction is equivalent to one half?", options:["Three quarters","One quarter","One third","Two quarters"], answer:3},
     {q:"A boy has 6 marbles, finds 5 more, then loses 4. How many marbles does he have now?", options:["7","6","11","8"], answer:0},
     {q:"If a problem asks for the total after combining two groups, which operation should you use?", options:["Addition","Comparison","Subtraction","Division"], answer:0}
   ],
   worksheet:[
     {prompt:"What is 8 times 4?", answers:["32","thirty-two"]},
     {prompt:"What do we call the amount left over when a group cannot be shared equally?", answers:["remainder"]},
     {prompt:"In the fraction 3 over 4, what number is the numerator?", answers:["3","three"]}
   ]},
  {subject:"Science", title:"Science Review: Animals, Earth, and Ecosystems", summary:"Students review recent Science topics: vertebrates and invertebrates, the nervous system, layers of the Earth, volcanoes, animal body coverings, symbiosis, how animals communicate, extreme weather, and ecosystems.",
   resourceLabel:"YouTube: Science Review: Animals, Earth, and Ecosystems", resourceUrl:"https://www.youtube.com/results?search_query=Science%20Review%3A%20Animals%2C%20Earth%2C%20and%20Ecosystems%20grade%202%20educational",
   quiz:[
     {q:"Which of these is a vertebrate?", options:["A spider","A fish","A snail","A worm"], answer:1},
     {q:"What is a volcano?", options:["A kind of ocean current","An opening in the Earth crust where melted rock can erupt","A type of large lake","A very tall, cold mountain only"], answer:1},
     {q:"Which animal body covering do birds usually have?", options:["Shells","Feathers","Scales","Fur"], answer:1},
     {q:"Which of these is an example of extreme weather?", options:["A thunderstorm","A calm, sunny day","A gentle breeze","A light cloud"], answer:0},
     {q:"What is an ecosystem?", options:["A single plant growing alone","Only the living things in a forest","Only the rocks and water in a place","Living and non-living things interacting together in one place"], answer:3}
   ],
   worksheet:[
     {prompt:"What do we call an animal that has a backbone?", answers:["vertebrate"]},
     {prompt:"What is the outer layer of the Earth called, the one we live on?", answers:["crust"]},
     {prompt:"What word describes a close relationship between two different living things?", answers:["symbiosis"]}
   ]},
  {subject:"SocialStudies", title:"Social Studies Review: Government, History, and Geography", summary:"Students review recent Social Studies topics: provincial and territorial symbols, levels of leadership, voting and elections, the fur trade, treaties, the United Nations, Canadian agriculture regions, Canada and the United States, and peacekeeping.",
   resourceLabel:"YouTube: Social Studies Review: Government, History, and Geography", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Review%3A%20Government%2C%20History%2C%20and%20Geography%20grade%202%20educational",
   quiz:[
     {q:"Who leads a province, such as Ontario?", options:["The governor","The mayor","The prime minister","The premier"], answer:3},
     {q:"Which animal fur was especially important during the fur trade?", options:["The kangaroo","The elephant","The lion","The beaver"], answer:3},
     {q:"What is the United Nations?", options:["A group of many countries that work together to solve world problems","A single countrys government only","A kind of school club","A type of sports league"], answer:0},
     {q:"Which crop is commonly grown on the Canadian Prairies?", options:["Bananas","Wheat","Coconuts","Pineapples"], answer:1},
     {q:"Which country shares a long border with Canada to the south?", options:["Mexico","The United States","Brazil","France"], answer:1}
   ],
   worksheet:[
     {prompt:"Who leads the entire country of Canada?", answers:["prime minister"]},
     {prompt:"What is an election?", answers:["an event where people vote to choose their leaders","people vote to choose leaders"]},
     {prompt:"What is a treaty?", answers:["a formal agreement, often about sharing land and resources","a formal agreement"]}
   ]},
]},
{day:101, label:"Day 101 — Mon", subjects:[
  {subject:"Language", title:"Subjects and Predicates: The Two Parts of a Sentence", summary:"Ontario Grade 2 Language strand: students learn that every complete sentence has two main parts, a subject that names who or what the sentence is about, and a predicate that tells what the subject does or is.",
   resourceLabel:"YouTube: Subjects and Predicates: The Two Parts of a Sentence", resourceUrl:"https://www.youtube.com/results?search_query=Subjects%20and%20Predicates%3A%20The%20Two%20Parts%20of%20a%20Sentence%20grade%202%20educational",
   quiz:[
     {q:"What is the subject of a sentence?", options:["A punctuation mark at the end","The part that names who or what the sentence is about","The part that tells what the subject does","A describing word only"], answer:1},
     {q:"What is the predicate of a sentence?", options:["The part that tells what the subject does or is","The part that names who the sentence is about","A question mark","The first word of the sentence"], answer:0},
     {q:"In the sentence The dog ran fast, what is the subject?", options:["ran","The dog","ran fast","fast"], answer:1},
     {q:"In the sentence The dog ran fast, what is the predicate?", options:["ran fast","fast only","dog","The dog"], answer:0},
     {q:"Why does a sentence need both a subject and a predicate?", options:["To use more punctuation","To be a longer sentence","To be a complete thought","To sound louder"], answer:2}
   ]},
  {subject:"Math", title:"Multiplication Facts: 0s, 1s, and 10s", summary:"Ontario Grade 2 Number strand: students practise and memorize multiplication facts for the 0, 1, and 10 times tables, learning that any number multiplied by 0 equals 0, any number multiplied by 1 stays the same, and multiplying by 10 adds a zero.",
   resourceLabel:"YouTube: Multiplication Facts: 0s, 1s, and 10s", resourceUrl:"https://www.youtube.com/results?search_query=Multiplication%20Facts%3A%200s%2C%201s%2C%20and%2010s%20grade%202%20educational",
   quiz:[
     {q:"What is 5 times 0?", options:["0","10","5","50"], answer:0},
     {q:"What is 7 times 1?", options:["8","7","17","0"], answer:1},
     {q:"What is 6 times 10?", options:["6","60","16","610"], answer:1},
     {q:"What is 9 times 0?", options:["0","19","90","9"], answer:0},
     {q:"What happens when you multiply any number by 1?", options:["The number becomes 10","The number stays the same","The number doubles","The number becomes 0"], answer:1}
   ]},
  {subject:"Science", title:"Weathering: How Rocks Slowly Break Down", summary:"Ontario Grade 2 Earth and Space Systems strand: students learn that weathering is the slow breaking down of rocks by wind, water, ice, and changes in temperature over a long period of time.",
   resourceLabel:"YouTube: Weathering: How Rocks Slowly Break Down", resourceUrl:"https://www.youtube.com/results?search_query=Weathering%3A%20How%20Rocks%20Slowly%20Break%20Down%20grade%202%20educational",
   quiz:[
     {q:"What is weathering?", options:["A type of severe storm","The movement of soil from one place to another","The slow breaking down of rocks by wind, water, and ice","The melting of snow in spring"], answer:2},
     {q:"Which of these can cause weathering?", options:["A calm, sunny day","Wind and water","A quiet forest","A clear night sky"], answer:1},
     {q:"Does weathering happen quickly or slowly?", options:["Only underwater","Only during an earthquake","Slowly, over a long time","Instantly, in one second"], answer:2},
     {q:"How can freezing and thawing water crack a rock?", options:["Rocks never contain any cracks","Water seeps into cracks, freezes, expands, and breaks the rock apart","Freezing has no effect on rocks","Water always makes rocks stronger"], answer:1},
     {q:"Weathering is best described as a process that ___.", options:["Turns rocks into water","Breaks rocks into smaller pieces over time","Has no effect on the Earth crust","Builds new mountains instantly"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Terry Fox: A Canadian Hero and His Marathon of Hope", summary:"Ontario Grade 2 Social Studies Heritage and Identity strand: students learn about Terry Fox, a young Canadian who ran across much of Canada to raise money for cancer research in a journey called the Marathon of Hope.",
   resourceLabel:"YouTube: Terry Fox: A Canadian Hero and His Marathon of Hope", resourceUrl:"https://www.youtube.com/results?search_query=Terry%20Fox%3A%20A%20Canadian%20Hero%20and%20His%20Marathon%20of%20Hope%20grade%202%20educational",
   quiz:[
     {q:"What did Terry Fox call his run across Canada?", options:["The Freedom Run","The Marathon of Hope","The Great Canadian Walk","The Race for Canada"], answer:1},
     {q:"Why did Terry Fox run across Canada?", options:["To raise money for cancer research","To win a race","To become famous","To visit every province for fun"], answer:0},
     {q:"What challenge did Terry Fox face during his run?", options:["He could not swim","He had never travelled before","He ran with one leg after losing the other to cancer","He ran only around his own house"], answer:2},
     {q:"Communities across Canada still honour Terry Fox by ___.", options:["Ignoring his story completely","Holding an annual run to raise money for cancer research","Forgetting his journey each year","Only remembering him in one city"], answer:1},
     {q:"Why is Terry Fox considered a Canadian hero?", options:["He showed courage and inspired others to help a cause bigger than himself","He was the fastest runner in the world","He only ran for his own benefit","He never faced any challenges"], answer:0}
   ]},
]},
{day:102, label:"Day 102 — Tue", subjects:[
  {subject:"Language", title:"Articles: Using A, An, and The Correctly", summary:"Ontario Grade 2 Language strand: students learn that the articles a and an come before a noun to mean any one example, using a before a consonant sound and an before a vowel sound, while the comes before a noun to mean one specific thing.",
   resourceLabel:"YouTube: Articles: Using A, An, and The Correctly", resourceUrl:"https://www.youtube.com/results?search_query=Articles%3A%20Using%20A%2C%20An%2C%20and%20The%20Correctly%20grade%202%20educational",
   quiz:[
     {q:"Which article is used before a word that starts with a vowel sound, like apple?", options:["the","a","no article needed","an"], answer:3},
     {q:"Which article is used before a word that starts with a consonant sound, like dog?", options:["a","no article needed","an","the"], answer:0},
     {q:"Which sentence uses the correct article?", options:["She ate a apple.","She ate the apple an.","She ate apple a.","She ate an apple."], answer:3},
     {q:"Which sentence uses the correct article?", options:["He read the a book.","He read an book.","He read a book.","He read book a."], answer:2},
     {q:"When do we use the word the before a noun?", options:["Only at the start of a sentence","When we mean any example at all","Only before vowel sounds","When we mean one specific thing"], answer:3}
   ]},
  {subject:"Math", title:"Composing and Decomposing 2D Shapes", summary:"Ontario Grade 2 Geometry strand: students learn to compose new shapes by combining smaller two-dimensional shapes, and decompose a larger shape into smaller shapes, such as building a square from two triangles.",
   resourceLabel:"YouTube: Composing and Decomposing 2D Shapes", resourceUrl:"https://www.youtube.com/results?search_query=Composing%20and%20Decomposing%202D%20Shapes%20grade%202%20educational",
   quiz:[
     {q:"What does it mean to compose a shape?", options:["To combine smaller shapes to make a new shape","To erase a shape completely","To colour a shape a single colour","To draw a shape with no sides"], answer:0},
     {q:"What does it mean to decompose a shape?", options:["To make a shape disappear","To measure the perimeter of a shape","To combine shapes into a bigger one","To break a larger shape into smaller shapes"], answer:3},
     {q:"Two triangles put together can compose which shape?", options:["A circle","A straight line only","A square or rectangle","A single point"], answer:2},
     {q:"If you cut a rectangle in half diagonally, what shapes do you get?", options:["Two hexagons","Two squares only","Two triangles","Two circles"], answer:2},
     {q:"Composing and decomposing shapes helps students understand ___.", options:["That only one shape exists","How shapes relate to and can form other shapes","That shapes never change","That shapes cannot be combined"], answer:1}
   ]},
  {subject:"Science", title:"Animal Movement: Fins, Wings, and Legs", summary:"Ontario Grade 2 Life Systems strand: students learn that animals have different body structures, such as fins, wings, and legs, that help them move in the specific environment where they live.",
   resourceLabel:"YouTube: Animal Movement: Fins, Wings, and Legs", resourceUrl:"https://www.youtube.com/results?search_query=Animal%20Movement%3A%20Fins%2C%20Wings%2C%20and%20Legs%20grade%202%20educational",
   quiz:[
     {q:"What body part helps a fish move through water?", options:["Fins","Legs","Wings","Feathers"], answer:0},
     {q:"What body part helps a bird fly through the air?", options:["Gills","Roots","Fins","Wings"], answer:3},
     {q:"What body part helps most mammals walk and run on land?", options:["Scales","Fins","Legs","Wings"], answer:2},
     {q:"Why do different animals have different movement structures?", options:["Only birds are able to move at all","Movement structures have no real purpose","All animals move in the exact same way","To help them move well in the place they live"], answer:3},
     {q:"A frog has strong back legs mainly to help it ___.", options:["Stay still forever","Swim using fins only","Jump long distances","Fly through the air"], answer:2}
   ]},
  {subject:"SocialStudies", title:"What Is a Democracy? Citizens Have a Voice in Decisions", summary:"Ontario Grade 2 Social Studies strand: students learn that in a democracy, citizens have a say in decisions and choose their leaders through voting, and that Canada is a democratic country.",
   resourceLabel:"YouTube: What Is a Democracy? Citizens Have a Voice in Decisions", resourceUrl:"https://www.youtube.com/results?search_query=What%20Is%20a%20Democracy%3F%20Citizens%20Have%20a%20Voice%20in%20Decisions%20grade%202%20educational",
   quiz:[
     {q:"What is a democracy?", options:["A place where only one person makes every decision","A system where citizens cannot vote","A system with no leaders at all","A system where citizens have a voice and vote for their leaders"], answer:3},
     {q:"Is Canada a democratic country?", options:["Only some Canadian cities are democracies","No, Canada has never been a democracy","Yes, Canada is a democracy","Canada stopped being a democracy long ago"], answer:2},
     {q:"How do citizens in a democracy have a say in decisions?", options:["By voting in elections","By letting only one family decide","By ignoring all elections","By never taking part in anything"], answer:0},
     {q:"Why is voting an important part of a democracy?", options:["Only leaders are allowed to vote","Voting is not connected to democracy","It lets citizens choose who represents them","Voting has no effect on decisions"], answer:2},
     {q:"In a democracy, decisions are usually made by ___.", options:["Ignoring what citizens want","A small group with no elections","Listening to the voice of many citizens","One single unelected ruler"], answer:2}
   ]},
]},
{day:103, label:"Day 103 — Wed", subjects:[
  {subject:"Language", title:"Verb Tenses: Talking About Past, Present, and Future", summary:"Ontario Grade 2 Language strand: students learn that verbs change form to show when an action happens, using past tense for something already done, present tense for something happening now, and future tense for something that will happen.",
   resourceLabel:"YouTube: Verb Tenses: Talking About Past, Present, and Future", resourceUrl:"https://www.youtube.com/results?search_query=Verb%20Tenses%3A%20Talking%20About%20Past%2C%20Present%2C%20and%20Future%20grade%202%20educational",
   quiz:[
     {q:"Which sentence is in the past tense?", options:["She will walk to school.","She walks to school.","She walked to school.","She is walking to school."], answer:2},
     {q:"Which sentence is in the present tense?", options:["He had played soccer.","He played soccer yesterday.","He plays soccer every day.","He will play soccer tomorrow."], answer:2},
     {q:"Which sentence is in the future tense?", options:["They visited the zoo yesterday.","They will visit the zoo tomorrow.","They visit the zoo often.","They were visiting the zoo."], answer:1},
     {q:"Which word signals that a sentence is talking about the future?", options:["already","yesterday","now","will"], answer:3},
     {q:"Changing a verb tense helps a reader understand ___.", options:["What colour something is","How many people are in a story","Where a story takes place","When an action happens"], answer:3}
   ]},
  {subject:"Math", title:"Number Patterns on a Hundred Chart", summary:"Ontario Grade 2 Patterning strand: students explore a hundred chart to find and describe number patterns, such as columns increasing by 10 going down and rows increasing by 1 going across.",
   resourceLabel:"YouTube: Number Patterns on a Hundred Chart", resourceUrl:"https://www.youtube.com/results?search_query=Number%20Patterns%20on%20a%20Hundred%20Chart%20grade%202%20educational",
   quiz:[
     {q:"On a hundred chart, what happens to a number as you move down one row?", options:["It increases by 1","It decreases by 10","It stays the same","It increases by 10"], answer:3},
     {q:"On a hundred chart, what happens to a number as you move one space to the right?", options:["It increases by 10","It decreases by 1","It increases by 1","It stays the same"], answer:2},
     {q:"On a hundred chart, if you are on 24 and move down one row, what number do you land on?", options:["23","34","14","25"], answer:1},
     {q:"On a hundred chart, if you are on 47 and move one space to the right, what number do you land on?", options:["48","37","46","57"], answer:0},
     {q:"A hundred chart helps students see number patterns because ___.", options:["Numbers are placed in random order","It only shows even numbers","Numbers are arranged in a clear, organized grid","It only shows odd numbers"], answer:2}
   ]},
  {subject:"Science", title:"Food Webs: Connecting Many Food Chains", summary:"Ontario Grade 2 Life Systems strand: students learn that a food web shows how many food chains connect together, because most animals eat more than one kind of food and are eaten by more than one predator.",
   resourceLabel:"YouTube: Food Webs: Connecting Many Food Chains", resourceUrl:"https://www.youtube.com/results?search_query=Food%20Webs%3A%20Connecting%20Many%20Food%20Chains%20grade%202%20educational",
   quiz:[
     {q:"What is a food web?", options:["A spider web found in a garden","A chart of animal habitats only","A single line showing one animal eating one plant","Many connected food chains showing how animals eat different things"], answer:3},
     {q:"Why do scientists use a food web instead of just one food chain?", options:["Every animal eats the exact same food","Most animals eat more than one kind of food","Food chains never connect to each other","A food web only shows plants"], answer:1},
     {q:"In a food web, an animal that eats both plants and other animals is called a ___.", options:["Producer only","Non-living thing","Omnivore","Decomposer only"], answer:2},
     {q:"What might happen to a food web if one type of animal disappeared?", options:["Food webs cannot be affected by changes","Every other animal would disappear instantly","Nothing would change at all","It could affect the other animals connected to it"], answer:3},
     {q:"A food web is best described as a way to show ___.", options:["A single unrelated fact about one animal","That animals never depend on other living things","That plants have no role in an ecosystem","How living things in an ecosystem depend on each other for food"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Provincial and Territorial Capital Cities", summary:"Ontario Grade 2 Social Studies strand: students learn that each Canadian province and territory has its own capital city, such as Toronto for Ontario and Ottawa as the capital of the whole country.",
   resourceLabel:"YouTube: Provincial and Territorial Capital Cities", resourceUrl:"https://www.youtube.com/results?search_query=Provincial%20and%20Territorial%20Capital%20Cities%20grade%202%20educational",
   quiz:[
     {q:"What is the capital city of Ontario?", options:["Ottawa","Montreal","Vancouver","Toronto"], answer:3},
     {q:"What is the capital city of Canada?", options:["Calgary","Winnipeg","Ottawa","Toronto"], answer:2},
     {q:"What do we call the main city where the government of a province or country is based?", options:["A border town","A capital city","A suburb","A rural area"], answer:1},
     {q:"Why does each province and territory have its own capital city?", options:["Capitals are chosen at random every year","Every province shares the exact same capital","Capital cities have no real purpose","It is where the provincial or territorial government meets and works"], answer:3},
     {q:"Is Ottawa located in the province of Ontario?", options:["No, Ottawa is located in Quebec","Ottawa is not located in any province","Yes, Ottawa is located in Ontario","Ottawa is a separate country"], answer:2}
   ]},
]},
{day:104, label:"Day 104 — Thu", subjects:[
  {subject:"Language", title:"Using Illustrations to Understand a Story", summary:"Ontario Grade 2 Reading strand: students learn to use illustrations and pictures alongside the words in a text to build and confirm their understanding of characters, setting, and events.",
   resourceLabel:"YouTube: Using Illustrations to Understand a Story", resourceUrl:"https://www.youtube.com/results?search_query=Using%20Illustrations%20to%20Understand%20a%20Story%20grade%202%20educational",
   quiz:[
     {q:"Why might a reader look at the illustrations in a book?", options:["To ignore the words completely","To help understand the story better","Pictures have no connection to the story","Illustrations never help understanding"], answer:1},
     {q:"If the words in a story do not explain what a character looks like, where might a reader find clues?", options:["The title page only","The illustrations","The back cover only","The table of contents"], answer:1},
     {q:"Illustrations can help a reader understand ___.", options:["Only the price of the book","The setting, characters, and mood of a story","Nothing about the story at all","Only the title of the book"], answer:1},
     {q:"If a picture shows dark clouds and rain, what might that tell a reader about the setting?", options:["The picture has no meaning","The story takes place indoors only","The weather is sunny and warm","The weather is stormy"], answer:3},
     {q:"Using illustrations along with the text is a strategy that helps readers ___.", options:["Avoid understanding the story","Skip reading the words entirely","Ignore important story details","Understand and enjoy a story more fully"], answer:3}
   ]},
  {subject:"Math", title:"Estimating Length Before Measuring", summary:"Ontario Grade 2 Measurement strand: students learn to make a reasonable estimate of an object length before measuring it with a ruler or measuring tape, then compare the estimate to the actual measurement.",
   resourceLabel:"YouTube: Estimating Length Before Measuring", resourceUrl:"https://www.youtube.com/results?search_query=Estimating%20Length%20Before%20Measuring%20grade%202%20educational",
   quiz:[
     {q:"What does it mean to estimate a length?", options:["To make a reasonable guess before measuring","To draw a picture of an object","To measure something perfectly the first time","To ignore the size of an object"], answer:0},
     {q:"Why is it useful to estimate before measuring?", options:["Estimating has no purpose in math","It helps you check if your measurement makes sense","Estimating replaces the need to measure","Estimating always gives the exact answer"], answer:1},
     {q:"Which tool would you use to check an estimate of length?", options:["A ruler or measuring tape","A thermometer","A scale for mass","A clock"], answer:0},
     {q:"If you estimate a pencil is about 15 centimetres long, what should you do next?", options:["Assume your estimate is always exact","Never measure it at all","Measure it with a ruler to check your estimate","Throw away the pencil"], answer:2},
     {q:"A good estimate of length should be ___.", options:["Always much too small","Reasonably close to the actual measurement","Always much too large","Always exactly correct"], answer:1}
   ]},
  {subject:"Science", title:"Tundra Habitats: Life in the Cold", summary:"Ontario Grade 2 Life Systems strand: students learn that the tundra is a cold habitat with very few trees, where specially adapted plants and animals, such as arctic foxes and caribou, survive harsh winters.",
   resourceLabel:"YouTube: Tundra Habitats: Life in the Cold", resourceUrl:"https://www.youtube.com/results?search_query=Tundra%20Habitats%3A%20Life%20in%20the%20Cold%20grade%202%20educational",
   quiz:[
     {q:"What is a tundra?", options:["A hot, wet rainforest","A cold habitat with very few trees","A deep ocean habitat","A warm desert habitat"], answer:1},
     {q:"Which animal is adapted to live in the tundra?", options:["Arctic fox","Parrot","Elephant","Monkey"], answer:0},
     {q:"Why do few trees grow in the tundra?", options:["Trees are not affected by climate","The tundra is always too hot for trees","Tundra soil has too much sunlight","The ground is frozen and the climate is very cold"], answer:3},
     {q:"How might a thick white coat help an animal survive in the tundra?", options:["It helps the animal swim faster","It has no useful purpose","It keeps the animal warm and helps it blend into the snow","It makes the animal colder"], answer:2},
     {q:"The tundra is best described as a habitat where living things must adapt to ___.", options:["Very cold temperatures and short growing seasons","Constant heavy rainfall","Extremely hot and humid weather","Deep ocean water pressure"], answer:0}
   ]},
  {subject:"SocialStudies", title:"First Nations, Inuit, and Metis: Three Distinct Indigenous Peoples", summary:"Ontario Grade 2 Social Studies Heritage and Identity strand: students learn that Indigenous peoples in Canada include three distinct groups, First Nations, Inuit, and Metis, each with its own history, languages, and traditions.",
   resourceLabel:"YouTube: First Nations, Inuit, and Metis: Three Distinct Indigenous Peoples", resourceUrl:"https://www.youtube.com/results?search_query=First%20Nations%2C%20Inuit%2C%20and%20Metis%3A%20Three%20Distinct%20Indigenous%20Peoples%20grade%202%20educational",
   quiz:[
     {q:"What are the three distinct groups of Indigenous peoples in Canada?", options:["Provinces, cities, and towns","Settlers, explorers, and traders","Farmers, teachers, and mayors","First Nations, Inuit, and Metis"], answer:3},
     {q:"Do First Nations, Inuit, and Metis peoples each have their own history and traditions?", options:["No, all three groups are exactly the same","Yes, each group has its own history and traditions","Only Inuit have traditions","Only First Nations have traditions"], answer:1},
     {q:"Which Indigenous group has traditionally lived in the Arctic regions of Canada?", options:["None of these groups","Only Metis","Inuit","Only First Nations"], answer:2},
     {q:"Why is it important to learn that Indigenous peoples are not all the same group?", options:["Learning about differences is not useful","All Indigenous peoples are identical","Only one Indigenous group exists in Canada","Each group has its own distinct culture and identity"], answer:3},
     {q:"The word Metis describes people who have ___.", options:["Mixed Indigenous and European ancestry and their own distinct culture","Only recently arrived in Canada","No connection to Indigenous history at all","Only European ancestry"], answer:0}
   ]},
]},
{day:105, label:"Day 105 — Fri", subjects:[
  {subject:"Language", title:"Compare and Contrast: How Two Things Are Alike and Different", summary:"Ontario Grade 2 Reading strand: students learn to compare and contrast two texts, characters, or ideas by describing how they are alike and how they are different.",
   resourceLabel:"YouTube: Compare and Contrast: How Two Things Are Alike and Different", resourceUrl:"https://www.youtube.com/results?search_query=Compare%20and%20Contrast%3A%20How%20Two%20Things%20Are%20Alike%20and%20Different%20grade%202%20educational",
   quiz:[
     {q:"What does it mean to compare two things?", options:["To draw a picture of them","To describe how they are alike","To ignore both things","To describe how they are different only"], answer:1},
     {q:"What does it mean to contrast two things?", options:["To describe how they are exactly the same","To describe how they are different","To measure their size","To combine them into one thing"], answer:1},
     {q:"Which of these is an example of comparing two story characters?", options:["One character is a girl and one is a boy","One book has pictures and one does not","Both characters are brave and kind","One story is short and one is long"], answer:2},
     {q:"Which of these is an example of contrasting two story characters?", options:["Both characters have a pet dog","Both characters live in the same town","Both characters like to read","One character is shy while the other is outgoing"], answer:3},
     {q:"Comparing and contrasting helps readers ___.", options:["Avoid thinking about a story","Read only one book at a time","Ignore important details in a text","Understand how ideas or characters relate to each other"], answer:3}
   ]},
  {subject:"Math", title:"Interpreting Bar Graphs with a Scale of More Than One", summary:"Ontario Grade 2 Data strand: students learn to read a bar graph where each square or unit on the scale represents more than one item, such as a scale where each square stands for two or five objects.",
   resourceLabel:"YouTube: Interpreting Bar Graphs with a Scale of More Than One", resourceUrl:"https://www.youtube.com/results?search_query=Interpreting%20Bar%20Graphs%20with%20a%20Scale%20of%20More%20Than%20One%20grade%202%20educational",
   quiz:[
     {q:"On a bar graph where each square represents 2 items, how many items does a bar of 3 squares show?", options:["5","6","2","3"], answer:1},
     {q:"On a bar graph where each square represents 5 items, how many items does a bar of 4 squares show?", options:["9","20","25","15"], answer:1},
     {q:"Why might a bar graph use a scale where each square represents more than one item?", options:["To fit larger amounts of data on the graph clearly","To make the graph impossible to read","To make the data smaller than it really is","Scales never represent more than one item"], answer:0},
     {q:"If a bar graph scale shows each square equals 10, and a bar has 5 squares, what total does the bar represent?", options:["50","5","10","15"], answer:0},
     {q:"Before reading the bars on a graph, what should you check first?", options:["The title of the classroom","The time of day","The scale, to see what each square represents","The colour of the bars only"], answer:2}
   ]},
  {subject:"Science", title:"The Skin: Protecting Our Bodies", summary:"Ontario Grade 2 Life Systems strand: students learn that the skin is the outer covering of our body that protects us from germs and injury, helps control body temperature, and lets us feel touch.",
   resourceLabel:"YouTube: The Skin: Protecting Our Bodies", resourceUrl:"https://www.youtube.com/results?search_query=The%20Skin%3A%20Protecting%20Our%20Bodies%20grade%202%20educational",
   quiz:[
     {q:"What is one important job of the skin?", options:["Breaking down food for energy","Sending messages to the brain only","Pumping blood through the body","Protecting the body from germs and injury"], answer:3},
     {q:"How does the skin help us sense the world around us?", options:["It lets us see colours","It lets us feel touch, such as heat, cold, and pressure","It lets us taste flavours","It lets us hear sounds"], answer:1},
     {q:"How does the skin help control body temperature?", options:["By making us hungry","By sweating to cool us down when we are hot","By helping us digest food","By helping us breathe air"], answer:1},
     {q:"Why is it important to keep a cut on the skin clean?", options:["To help prevent germs from entering the body","Germs cannot enter through skin","Cleaning a cut has no purpose","Cuts on skin are never a concern"], answer:0},
     {q:"The skin is best described as the body organ that ___.", options:["Pumps blood to every organ","Only controls how we move","Covers and protects the body","Digests the food we eat"], answer:2}
   ]},
  {subject:"SocialStudies", title:"National Emblems of Canada: The Coat of Arms and Other Symbols", summary:"Ontario Grade 2 Social Studies strand: students learn that Canada has official national emblems, including the Coat of Arms, that represent the history and identity of the country beyond the more familiar flag and anthem.",
   resourceLabel:"YouTube: National Emblems of Canada: The Coat of Arms and Other Symbols", resourceUrl:"https://www.youtube.com/results?search_query=National%20Emblems%20of%20Canada%3A%20The%20Coat%20of%20Arms%20and%20Other%20Symbols%20grade%202%20educational",
   quiz:[
     {q:"What is the Coat of Arms of Canada?", options:["A type of Canadian clothing","A famous Canadian mountain","An official emblem that represents the history and identity of Canada","A Canadian sports team logo"], answer:2},
     {q:"Which of these is an example of a Canadian national emblem?", options:["A single citys local logo","A private company logo","The Coat of Arms","A students favourite toy"], answer:2},
     {q:"Why do countries have official emblems like a Coat of Arms?", options:["Emblems have no real meaning","To represent the history and values of the country","Only provinces are allowed emblems","Countries are not allowed emblems"], answer:1},
     {q:"National emblems are different from a national flag because they ___.", options:["Are always exactly the same as a flag","Have no connection to a country at all","Can include more detailed symbols and images","Cannot be used by a country"], answer:2},
     {q:"Learning about national emblems helps students understand ___.", options:["Symbols that represent Canadian history and identity","That Canada has no symbols at all","That only flags represent countries","That symbols are unimportant"], answer:0}
   ]},
]},
{day:106, label:"Day 106 — Mon", subjects:[
  {subject:"Language", title:"Following Multi-Step Written Directions", summary:"Ontario Grade 2 Reading and Writing strands: students learn to read and follow written directions that have more than one step, completing each step in the correct order to finish a task successfully.",
   resourceLabel:"YouTube: Following Multi-Step Written Directions", resourceUrl:"https://www.youtube.com/results?search_query=Following%20Multi-Step%20Written%20Directions%20grade%202%20educational",
   quiz:[
     {q:"What is a multi-step direction?", options:["A direction that never needs to be followed","A direction with only one step","A direction with more than one step to follow","A direction with no steps at all"], answer:2},
     {q:"Why is it important to follow the steps of a direction in order?", options:["Steps should always be skipped","Completing steps out of order can lead to mistakes","Directions do not need to be read carefully","Order never matters when following directions"], answer:1},
     {q:"If a direction says first colour the circle, then cut it out, what should you do first?", options:["Colour the circle","Skip both steps","Do both steps at the same time","Cut it out"], answer:0},
     {q:"What is a good strategy before starting a multi-step task?", options:["Read all the directions carefully before beginning","Start immediately without reading anything","Ignore the directions completely","Only read the very last step"], answer:0},
     {q:"Following multi-step directions carefully helps you ___.", options:["Finish a task incorrectly","Avoid understanding the task","Complete a task correctly and in the right order","Skip important steps"], answer:2}
   ]},
  {subject:"Math", title:"Ordering Numbers to 1000", summary:"Ontario Grade 2 Number strand: students learn to order a set of three-digit numbers from least to greatest or greatest to least by comparing the hundreds, tens, and ones digits.",
   resourceLabel:"YouTube: Ordering Numbers to 1000", resourceUrl:"https://www.youtube.com/results?search_query=Ordering%20Numbers%20to%201000%20grade%202%20educational",
   quiz:[
     {q:"Which set of numbers is ordered from least to greatest?", options:["489, 356, 214","214, 489, 356","356, 214, 489","214, 356, 489"], answer:3},
     {q:"Which number is the greatest: 342, 423, or 234?", options:["423","They are all equal","342","234"], answer:0},
     {q:"Which number is the least: 567, 675, or 756?", options:["567","They are all equal","675","756"], answer:0},
     {q:"When ordering three-digit numbers, which digit should you compare first?", options:["The ones digit","The last letter","The tens digit","The hundreds digit"], answer:3},
     {q:"Which set of numbers is ordered from greatest to least?", options:["415, 623, 812","812, 623, 415","623, 415, 812","812, 415, 623"], answer:1}
   ]},
  {subject:"Science", title:"Camouflage vs Mimicry: Two Ways Animals Stay Safe", summary:"Ontario Grade 2 Life Systems strand: students learn that camouflage lets an animal blend into its surroundings to hide, while mimicry lets a harmless animal look like a dangerous one to scare away predators.",
   resourceLabel:"YouTube: Camouflage vs Mimicry: Two Ways Animals Stay Safe", resourceUrl:"https://www.youtube.com/results?search_query=Camouflage%20vs%20Mimicry%3A%20Two%20Ways%20Animals%20Stay%20Safe%20grade%202%20educational",
   quiz:[
     {q:"What is camouflage?", options:["When an animal looks like a different, dangerous animal","When an animal grows larger","When an animal changes its habitat","When an animal blends into its surroundings to hide"], answer:3},
     {q:"What is mimicry?", options:["When an animal grows a new colour every day","When an animal hides underground forever","When a harmless animal looks like a dangerous one to stay safe","When an animal blends perfectly into a rock"], answer:2},
     {q:"A stick insect that looks like a twig is an example of ___.", options:["Hibernation","Mimicry","Camouflage","Migration"], answer:2},
     {q:"A harmless fly that looks like a stinging wasp is an example of ___.", options:["Camouflage","Migration","Hibernation","Mimicry"], answer:3},
     {q:"Both camouflage and mimicry help animals ___.", options:["Avoid being caught by predators","Fly faster through the air","Find water more easily","Grow bigger more quickly"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Languages of the World: How People Communicate Differently", summary:"Ontario Grade 2 Social Studies People and Environments strand: students learn that people around the world speak many different languages, and that Canada itself has two official languages, English and French.",
   resourceLabel:"YouTube: Languages of the World: How People Communicate Differently", resourceUrl:"https://www.youtube.com/results?search_query=Languages%20of%20the%20World%3A%20How%20People%20Communicate%20Differently%20grade%202%20educational",
   quiz:[
     {q:"What are the two official languages of Canada?", options:["English and Spanish","English and Mandarin","French and German","English and French"], answer:3},
     {q:"Why do different countries around the world often speak different languages?", options:["Language has no connection to culture","Countries are not allowed different languages","Every country in the world speaks the exact same language","Language is often connected to a country history and culture"], answer:3},
     {q:"What is one way people can communicate even if they do not speak the same language?", options:["By speaking louder in their own language","By refusing to interact","Using gestures, pictures, or a translator","It is impossible to communicate at all"], answer:2},
     {q:"Learning about different languages around the world helps students understand ___.", options:["That only one language exists","That language does not matter","That people communicate in many different ways","That every language sounds the same"], answer:2},
     {q:"In Canada, French is especially widely spoken in which province?", options:["Quebec","Newfoundland and Labrador","British Columbia","Alberta"], answer:0}
   ]},
]},
{day:107, label:"Day 107 — Tue", subjects:[
  {subject:"Language", title:"Story Mood: How a Story Makes Us Feel", summary:"Ontario Grade 2 Reading strand: students learn that mood is the feeling a story creates for the reader, such as happy, scary, or calm, built through word choice, setting, and events.",
   resourceLabel:"YouTube: Story Mood: How a Story Makes Us Feel", resourceUrl:"https://www.youtube.com/results?search_query=Story%20Mood%3A%20How%20a%20Story%20Makes%20Us%20Feel%20grade%202%20educational",
   quiz:[
     {q:"What is the mood of a story?", options:["The title of the story","The feeling a story creates for the reader","The number of characters in a story","The length of the story"], answer:1},
     {q:"Which words might create a scary mood in a story?", options:["Sunny, cheerful, and bright","Dark, creaking, and shadowy","Colourful, happy, and playful","Warm, friendly, and calm"], answer:1},
     {q:"Which words might create a happy mood in a story?", options:["Bright, cheerful, and sunny","Frightening, eerie, and strange","Silent, empty, and grey","Dark, gloomy, and cold"], answer:0},
     {q:"How can a writer create mood in a story?", options:["By using no words at all","By avoiding all descriptions","Mood cannot be created by a writer","By choosing specific words and details"], answer:3},
     {q:"Understanding the mood of a story helps readers ___.", options:["Skip reading the story entirely","Ignore the events of the story","Connect more deeply with how the story feels","Avoid understanding the characters"], answer:2}
   ]},
  {subject:"Math", title:"Locating Numbers on a Number Line to 1000", summary:"Ontario Grade 2 Number strand: students learn to locate and compare three-digit numbers on a number line, understanding that numbers further to the right are greater in value.",
   resourceLabel:"YouTube: Locating Numbers on a Number Line to 1000", resourceUrl:"https://www.youtube.com/results?search_query=Locating%20Numbers%20on%20a%20Number%20Line%20to%201000%20grade%202%20educational",
   quiz:[
     {q:"On a number line, numbers further to the right are ___.", options:["Greater in value","Always negative","Smaller in value","Always equal"], answer:0},
     {q:"On a number line from 0 to 1000, which number would be closer to 1000: 850 or 350?", options:["850","Neither number fits on the line","They are equally close","350"], answer:0},
     {q:"If you locate 400 and 600 on a number line, which number is further to the right?", options:["Both are in the same spot","Neither can be placed","600","400"], answer:2},
     {q:"A number line can help you find a number that is ___.", options:["Between two other numbers","Always the smallest number","Impossible to compare","Always the largest number"], answer:0},
     {q:"Where would the number 500 be located on a number line from 0 to 1000?", options:["Off the number line completely","Exactly in the middle","At the very end","At the very start"], answer:1}
   ]},
  {subject:"Science", title:"Life Cycle of an Insect: From Egg to Adult", summary:"Ontario Grade 2 Life Systems strand: students learn that many insects go through a life cycle with several stages, such as egg, larva, pupa, and adult, changing form as they grow.",
   resourceLabel:"YouTube: Life Cycle of an Insect: From Egg to Adult", resourceUrl:"https://www.youtube.com/results?search_query=Life%20Cycle%20of%20an%20Insect%3A%20From%20Egg%20to%20Adult%20grade%202%20educational",
   quiz:[
     {q:"What is usually the first stage in an insect life cycle?", options:["Larva","Adult","Pupa","Egg"], answer:3},
     {q:"What is the larva stage of an insect life cycle?", options:["The stage where the insect lays eggs","The final adult stage","A young, worm-like stage that hatches from an egg","A stage that never actually happens"], answer:2},
     {q:"During the pupa stage, what is happening inside the insect?", options:["It is laying new eggs","It is migrating to a new country","Its body is changing into its adult form","It is hunting for food actively"], answer:2},
     {q:"Which of these correctly orders the stages of many insect life cycles?", options:["Larva, adult, egg, pupa","Egg, larva, pupa, adult","Adult, egg, larva, pupa","Pupa, adult, egg, larva"], answer:1},
     {q:"Why is learning about insect life cycles useful?", options:["It helps us understand how insects grow and change over time","All insects look the same their entire life","Insects never actually change form","Life cycles have no connection to insects"], answer:0}
   ]},
  {subject:"SocialStudies", title:"The Underground Railroad: A Journey to Freedom", summary:"Ontario Grade 2 Social Studies Heritage and Identity strand: students learn that the Underground Railroad was a secret network of routes and safe houses that helped freedom seekers travel to Canada to escape slavery.",
   resourceLabel:"YouTube: The Underground Railroad: A Journey to Freedom", resourceUrl:"https://www.youtube.com/results?search_query=The%20Underground%20Railroad%3A%20A%20Journey%20to%20Freedom%20grade%202%20educational",
   quiz:[
     {q:"What was the Underground Railroad?", options:["A modern subway system","An actual railroad built underground","A type of Canadian sports league","A secret network of routes and safe houses to help freedom seekers reach Canada"], answer:3},
     {q:"Why did freedom seekers travel along the Underground Railroad?", options:["To escape slavery and reach freedom in Canada","To attend a school in another country","To visit family for a short trip","To go on a vacation"], answer:0},
     {q:"Did the Underground Railroad involve an actual train running underground?", options:["No, it was a network of secret routes and safe houses","It was a type of airplane route","Yes, it was a real underground train","It was a type of Canadian highway"], answer:0},
     {q:"Why might people helping freedom seekers along the route need to keep it secret?", options:["To protect the freedom seekers from being caught","Secrecy was not important at all","Everyone already knew every detail","It was not dangerous for anyone involved"], answer:0},
     {q:"The Underground Railroad is an important part of history because it shows ___.", options:["That helping others was not valued","That freedom was never an important idea","That Canada played no role in this history","People helping others reach freedom and safety"], answer:3}
   ]},
]},
{day:108, label:"Day 108 — Wed", subjects:[
  {subject:"Language", title:"Using Transition Words: First, Next, Then, Finally", summary:"Ontario Grade 2 Writing strand: students learn to use transition words such as first, next, then, and finally to show the order of events clearly when writing instructions or telling a story.",
   resourceLabel:"YouTube: Using Transition Words: First, Next, Then, Finally", resourceUrl:"https://www.youtube.com/results?search_query=Using%20Transition%20Words%3A%20First%2C%20Next%2C%20Then%2C%20Finally%20grade%202%20educational",
   quiz:[
     {q:"What is a transition word?", options:["A word that names a person","A word that shows the order of events","A word used only in math","A word that describes a colour"], answer:1},
     {q:"Which transition word would you use to show what happens at the very beginning?", options:["Finally","Then","First","Before that"], answer:2},
     {q:"Which transition word would you use to show what happens at the very end?", options:["First","Finally","Next","Before"], answer:1},
     {q:"Why are transition words helpful in writing instructions?", options:["They make instructions harder to follow","They help the reader follow the correct order of steps","They only belong in math problems","They are never used in writing"], answer:1},
     {q:"Which sentence correctly uses a transition word?", options:["Sugar flour first mix together the.","The first together mix flour sugar.","Mix flour sugar first the together.","First, mix the flour and sugar together."], answer:3}
   ]},
  {subject:"Math", title:"Mental Math Strategies: Doubling and Halving", summary:"Ontario Grade 2 Number strand: students learn mental math strategies for doubling a number, such as thinking of 7 plus 7, and for halving a number, such as sharing 14 into two equal groups.",
   resourceLabel:"YouTube: Mental Math Strategies: Doubling and Halving", resourceUrl:"https://www.youtube.com/results?search_query=Mental%20Math%20Strategies%3A%20Doubling%20and%20Halving%20grade%202%20educational",
   quiz:[
     {q:"What does it mean to double a number?", options:["To add the number to itself","To cut the number in half","To multiply the number by 0","To subtract 1 from the number"], answer:0},
     {q:"What is double 6?", options:["6","12","8","10"], answer:1},
     {q:"What does it mean to halve a number?", options:["To add the number to itself","To round the number up","To multiply the number by 10","To split the number into two equal parts"], answer:3},
     {q:"What is half of 16?", options:["12","6","10","8"], answer:3},
     {q:"Doubling and halving are useful mental math strategies because they help you ___.", options:["Avoid using numbers at all","Only work with written calculations","Never solve a problem correctly","Solve problems quickly in your head"], answer:3}
   ]},
  {subject:"Science", title:"Exoskeletons and Endoskeletons: Two Kinds of Body Support", summary:"Ontario Grade 2 Life Systems strand: students learn that some animals, like insects, have a hard outer covering called an exoskeleton for support, while other animals, like humans, have an internal skeleton called an endoskeleton.",
   resourceLabel:"YouTube: Exoskeletons and Endoskeletons: Two Kinds of Body Support", resourceUrl:"https://www.youtube.com/results?search_query=Exoskeletons%20and%20Endoskeletons%3A%20Two%20Kinds%20of%20Body%20Support%20grade%202%20educational",
   quiz:[
     {q:"What is an exoskeleton?", options:["A soft, flexible skin only","A type of plant root","A skeleton found inside the body","A hard outer covering that supports and protects an animal body"], answer:3},
     {q:"What is an endoskeleton?", options:["A hard covering found outside the body","A body covering made of feathers","A type of leaf","A skeleton found inside the body"], answer:3},
     {q:"Which of these animals has an exoskeleton?", options:["A dog","A bird","An insect","A human"], answer:2},
     {q:"Which of these animals has an endoskeleton?", options:["A human","A crab","A spider","An insect"], answer:0},
     {q:"Both exoskeletons and endoskeletons help an animal by ___.", options:["Helping the animal breathe underwater only","Preventing the animal from moving at all","Providing support and protection for the body","Making the animal invisible"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Map Scale: Understanding How Maps Show Real Distances", summary:"Ontario Grade 2 Social Studies strand: students learn that a map scale shows how a distance on a map compares to the real distance in the world, helping map readers estimate how far apart places actually are.",
   resourceLabel:"YouTube: Map Scale: Understanding How Maps Show Real Distances", resourceUrl:"https://www.youtube.com/results?search_query=Map%20Scale%3A%20Understanding%20How%20Maps%20Show%20Real%20Distances%20grade%202%20educational",
   quiz:[
     {q:"What is a map scale?", options:["A picture of a compass","A drawing of a mountain","A tool that shows how map distance compares to real distance","A list of city names"], answer:2},
     {q:"Why do maps include a scale?", options:["To make the map more colourful","To help readers estimate real distances between places","To replace the map legend","Scales have no purpose on a map"], answer:1},
     {q:"If a map scale shows that 1 centimetre equals 10 kilometres, what does 3 centimetres on the map represent?", options:["10 kilometres","13 kilometres","3 kilometres","30 kilometres"], answer:3},
     {q:"Which map tool helps you understand what symbols mean, working alongside the scale?", options:["The map legend","The title only","The border only","The compass rose only"], answer:0},
     {q:"Understanding map scale helps students ___.", options:["Make maps less useful","Estimate how far apart real places are","Avoid using maps altogether","Ignore distances between places"], answer:1}
   ]},
]},
{day:109, label:"Day 109 — Thu", subjects:[
  {subject:"Language", title:"Writing a Descriptive Paragraph Using the Five Senses", summary:"Ontario Grade 2 Writing strand: students learn to write a descriptive paragraph that uses details from the five senses, sight, sound, smell, taste, and touch, to help readers picture what is being described.",
   resourceLabel:"YouTube: Writing a Descriptive Paragraph Using the Five Senses", resourceUrl:"https://www.youtube.com/results?search_query=Writing%20a%20Descriptive%20Paragraph%20Using%20the%20Five%20Senses%20grade%202%20educational",
   quiz:[
     {q:"What is a descriptive paragraph?", options:["A list of math facts","A paragraph with no details at all","A paragraph that uses details to help readers picture something","A paragraph that only asks questions"], answer:2},
     {q:"Which sense would help you describe how fresh bread smells?", options:["Smell","Sight","Taste","Hearing"], answer:0},
     {q:"Which sentence uses a sense detail about sound?", options:["The leaves were bright orange.","The leaves felt dry and crisp.","The leaves crunched loudly under our feet.","The leaves tasted bitter."], answer:2},
     {q:"Why do writers use sensory details in descriptive writing?", options:["Sensory details make writing less interesting","Descriptive writing should avoid all details","Sensory details have no purpose in writing","To help readers imagine the experience more vividly"], answer:3},
     {q:"Which of these uses the sense of touch in a description?", options:["The blanket felt soft and warm.","The blanket made a rustling sound.","The blanket was bright red.","The blanket smelled like flowers."], answer:0}
   ]},
  {subject:"Math", title:"Congruent Shapes: Same Size and Same Shape", summary:"Ontario Grade 2 Geometry strand: students learn that two shapes are congruent when they are exactly the same size and the same shape, even if they are turned or flipped in a different direction.",
   resourceLabel:"YouTube: Congruent Shapes: Same Size and Same Shape", resourceUrl:"https://www.youtube.com/results?search_query=Congruent%20Shapes%3A%20Same%20Size%20and%20Same%20Shape%20grade%202%20educational",
   quiz:[
     {q:"What does it mean for two shapes to be congruent?", options:["They are exactly the same size and shape","They have different sizes but the same shape","They are the same colour only","They have the same size but different shapes"], answer:0},
     {q:"If you flip a congruent shape over, is it still congruent to the original?", options:["Yes, flipping does not change its size or shape","No, flipping always changes the shape","Flipping always makes it larger","Flipping always makes it smaller"], answer:0},
     {q:"Which pair of shapes would be congruent?", options:["A large square and a small square","A triangle and a circle","Two triangles that are the exact same size and shape","A rectangle and a square"], answer:2},
     {q:"Turning a shape to face a different direction ___ its congruence to the original.", options:["Always erases","Always doubles","Always changes","Does not change"], answer:3},
     {q:"Identifying congruent shapes helps students understand ___.", options:["That congruent shapes must be different colours","That shapes can be equal in size and shape even when turned","That size never matters when comparing shapes","That all shapes are always congruent"], answer:1}
   ]},
  {subject:"Science", title:"Seed Dispersal: How Plants Spread Their Seeds", summary:"Ontario Grade 2 Life Systems strand: students learn that plants disperse, or spread, their seeds in different ways, such as wind carrying light seeds, water carrying floating seeds, and animals carrying seeds in fur or after eating fruit.",
   resourceLabel:"YouTube: Seed Dispersal: How Plants Spread Their Seeds", resourceUrl:"https://www.youtube.com/results?search_query=Seed%20Dispersal%3A%20How%20Plants%20Spread%20Their%20Seeds%20grade%202%20educational",
   quiz:[
     {q:"What does it mean for a plant to disperse its seeds?", options:["To turn its seeds into flowers","To stop making seeds completely","To spread its seeds to new places","To keep all its seeds in one spot forever"], answer:2},
     {q:"How might wind help disperse seeds?", options:["By burying seeds underground","By carrying light seeds through the air to new places","Wind never affects seeds at all","By turning seeds into water"], answer:1},
     {q:"How might an animal help disperse the seeds of a plant?", options:["By carrying seeds in its fur or eating fruit and dropping seeds elsewhere","By destroying every seed it touches","Animals never interact with seeds","By keeping seeds in one exact spot"], answer:0},
     {q:"Why is seed dispersal important for a plant?", options:["It helps new plants grow in new places without overcrowding the parent plant","It stops new plants from ever growing","Seed dispersal has no benefit to a plant","It only helps animals, not plants"], answer:0},
     {q:"Which of these is a way that water can disperse seeds?", options:["Water only affects fully grown plants","Water never carries seeds anywhere","Carrying floating seeds downstream to a new location","Water always destroys every seed"], answer:2}
   ]},
  {subject:"SocialStudies", title:"How Communities Help Each Other After a Disaster", summary:"Ontario Grade 2 Social Studies strand: students learn that when a disaster such as a flood or storm affects a community, neighbours, volunteers, and organizations often work together to help people recover and rebuild.",
   resourceLabel:"YouTube: How Communities Help Each Other After a Disaster", resourceUrl:"https://www.youtube.com/results?search_query=How%20Communities%20Help%20Each%20Other%20After%20a%20Disaster%20grade%202%20educational",
   quiz:[
     {q:"What is one way communities help each other after a disaster?", options:["Neighbours and volunteers work together to help people recover","No one is ever able to help after a disaster","Communities always ignore people in need","Disasters never affect communities"], answer:0},
     {q:"Which of these is an example of a natural disaster?", options:["A quiet sunny afternoon","A regular school day","A flood","A calm lake"], answer:2},
     {q:"Why might volunteers collect food and supplies after a disaster?", options:["To help people who lost their homes or belongings","Only governments are allowed to help","Supplies are not needed after a disaster","Volunteers never collect supplies"], answer:0},
     {q:"What is one way people can prepare before a disaster happens?", options:["Ignoring the possibility of a disaster","Refusing to plan for emergencies","Avoiding all safety information","Making an emergency plan and kit"], answer:3},
     {q:"Communities that help each other after a disaster show the importance of ___.", options:["Avoiding community involvement","Ignoring people who need assistance","Cooperation and caring for one another","Working alone with no help from others"], answer:2}
   ]},
]},
{day:110, label:"Day 110 — Fri", subjects:[
  {subject:"Language", title:"Language Review: Sentences, Grammar, and Story Comprehension", summary:"Students review recent Language skills: subjects and predicates, articles a/an/the, verb tenses, using illustrations to understand a story, comparing and contrasting texts, following multi-step directions, story mood, transition words, and writing descriptive paragraphs using the five senses.",
   resourceLabel:"YouTube: Language Review: Sentences, Grammar, and Story Comprehension", resourceUrl:"https://www.youtube.com/results?search_query=Language%20Review%3A%20Sentences%2C%20Grammar%2C%20and%20Story%20Comprehension%20grade%202%20educational",
   quiz:[
     {q:"What is the subject of a sentence?", options:["The part that names who or what the sentence is about","The part that tells what the subject does","A punctuation mark at the end","A describing word only"], answer:0},
     {q:"Which sentence uses the correct article?", options:["She ate the apple an.","She ate apple a.","She ate a apple.","She ate an apple."], answer:3},
     {q:"Which sentence is in the future tense?", options:["They visit the zoo often.","They will visit the zoo tomorrow.","They visited the zoo yesterday.","They were visiting the zoo."], answer:1},
     {q:"What does it mean to contrast two things?", options:["To describe how they are exactly the same","To measure their size","To combine them into one thing","To describe how they are different"], answer:3},
     {q:"Why do writers use sensory details in descriptive writing?", options:["Sensory details make writing less interesting","To help readers imagine the experience more vividly","Descriptive writing should avoid all details","Sensory details have no purpose in writing"], answer:1}
   ]},
  {subject:"Math", title:"Math Review: Multiplication, Geometry, and Number Sense", summary:"Students review recent Math skills: multiplication facts for 0s, 1s, and 10s, composing and decomposing 2D shapes, number patterns on a hundred chart, estimating length, interpreting bar graphs with a scale, ordering numbers to 1000, locating numbers on a number line, doubling and halving, and congruent shapes.",
   resourceLabel:"YouTube: Math Review: Multiplication, Geometry, and Number Sense", resourceUrl:"https://www.youtube.com/results?search_query=Math%20Review%3A%20Multiplication%2C%20Geometry%2C%20and%20Number%20Sense%20grade%202%20educational",
   quiz:[
     {q:"What is 6 times 10?", options:["6","610","16","60"], answer:3},
     {q:"On a hundred chart, what happens to a number as you move down one row?", options:["It decreases by 10","It stays the same","It increases by 10","It increases by 1"], answer:2},
     {q:"Which number is the greatest: 342, 423, or 234?", options:["234","342","They are all equal","423"], answer:3},
     {q:"What is half of 16?", options:["8","6","12","10"], answer:0},
     {q:"What does it mean for two shapes to be congruent?", options:["They are exactly the same size and shape","They have the same size but different shapes","They are the same colour only","They have different sizes but the same shape"], answer:0}
   ]},
  {subject:"Science", title:"Science Review: Earth, Animals, and Plants", summary:"Students review recent Science topics: weathering, animal movement, food webs, tundra habitats, the skin, camouflage and mimicry, insect life cycles, exoskeletons and endoskeletons, and seed dispersal.",
   resourceLabel:"YouTube: Science Review: Earth, Animals, and Plants", resourceUrl:"https://www.youtube.com/results?search_query=Science%20Review%3A%20Earth%2C%20Animals%2C%20and%20Plants%20grade%202%20educational",
   quiz:[
     {q:"What is weathering?", options:["A type of severe storm","The slow breaking down of rocks by wind, water, and ice","The melting of snow in spring","The movement of soil from one place to another"], answer:1},
     {q:"What is a food web?", options:["A chart of animal habitats only","Many connected food chains showing how animals eat different things","A single line showing one animal eating one plant","A spider web found in a garden"], answer:1},
     {q:"What is one important job of the skin?", options:["Sending messages to the brain only","Protecting the body from germs and injury","Breaking down food for energy","Pumping blood through the body"], answer:1},
     {q:"What is mimicry?", options:["When a harmless animal looks like a dangerous one to stay safe","When an animal blends perfectly into a rock","When an animal grows a new colour every day","When an animal hides underground forever"], answer:0},
     {q:"What is an exoskeleton?", options:["A soft, flexible skin only","A skeleton found inside the body","A type of plant root","A hard outer covering that supports and protects an animal body"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Social Studies Review: Canadian Heritage, Government, and Geography", summary:"Students review recent Social Studies topics: Terry Fox, democracy, provincial and territorial capital cities, First Nations, Inuit, and Metis peoples, national emblems, languages of the world, the Underground Railroad, map scale, and communities helping after a disaster.",
   resourceLabel:"YouTube: Social Studies Review: Canadian Heritage, Government, and Geography", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Review%3A%20Canadian%20Heritage%2C%20Government%2C%20and%20Geography%20grade%202%20educational",
   quiz:[
     {q:"What did Terry Fox call his run across Canada?", options:["The Freedom Run","The Great Canadian Walk","The Race for Canada","The Marathon of Hope"], answer:3},
     {q:"What is a democracy?", options:["A system where citizens cannot vote","A system with no leaders at all","A place where only one person makes every decision","A system where citizens have a voice and vote for their leaders"], answer:3},
     {q:"What are the three distinct groups of Indigenous peoples in Canada?", options:["First Nations, Inuit, and Metis","Settlers, explorers, and traders","Provinces, cities, and towns","Farmers, teachers, and mayors"], answer:0},
     {q:"What was the Underground Railroad?", options:["An actual railroad built underground","A secret network of routes and safe houses to help freedom seekers reach Canada","A type of Canadian sports league","A modern subway system"], answer:1},
     {q:"What is one way communities help each other after a disaster?", options:["Communities always ignore people in need","Neighbours and volunteers work together to help people recover","No one is ever able to help after a disaster","Disasters never affect communities"], answer:1}
   ]},
]},
];

export default curriculum;