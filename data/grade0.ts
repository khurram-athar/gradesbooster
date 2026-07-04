import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"Language", title:"Letter A", summary:"Explore uppercase and lowercase A. Students identify the letter, practise its short /a/ sound, and find words beginning with A such as apple, ant, and astronaut.",
   resourceLabel:"YouTube: Letter A", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20A%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=gsb999VSvh8",
   quiz:[
     {q:"Which word starts with A?", options:["Dog","Apple","Cat","Ball"], answer:1},
     {q:"What sound does short A make?", options:["Ah as in apple","Oo as in boot","Ee as in see","Oh as in open"], answer:0},
     {q:"How many sides does uppercase A have?", options:["1","2","3","4"], answer:2},
     {q:"Which A word is a fruit?", options:["Apple","Ant","Axe","Arrow"], answer:0},
     {q:"Find the A: cat, apple, dog, sun", options:["sun","dog","apple","cat"], answer:2}
   ]},
  {subject:"Math", title:"Counting 1 to 5", summary:"Students count objects up to 5, match numerals to quantities, and begin to understand one-to-one correspondence.",
   resourceLabel:"YouTube: Counting 1 to 5", resourceUrl:"https://www.youtube.com/results?search_query=Counting%201%20to%205%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mKSNQuQrsm0",
   quiz:[
     {q:"How many fingers on one hand?", options:["3","5","4","6"], answer:1},
     {q:"What number comes after 3?", options:["5","4","2","1"], answer:1},
     {q:"Which numeral means three?", options:["3","4","1","2"], answer:0},
     {q:"Count the dots: ● ● ● ● How many?", options:["3","4","2","5"], answer:1},
     {q:"What number comes before 5?", options:["4","2","6","3"], answer:0}
   ]},
  {subject:"Science", title:"Living and Non-Living Things", summary:"Students learn to distinguish living things (grow, breathe, need food/water) from non-living things (do not grow on their own, do not breathe).",
   resourceLabel:"YouTube: Living and Non-Living Things", resourceUrl:"https://www.youtube.com/results?search_query=Living%20and%20Non-Living%20Things%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Gy60BqCnTG4",
   quiz:[
     {q:"A living thing ___.", options:["never changes","is made of metal","grows and needs food, water, and air","cannot move ever"], answer:2},
     {q:"Which is a living thing?", options:["Chair","Book","Tree","Rock"], answer:2},
     {q:"Which is non-living?", options:["Dog","Table","Cat","Flower"], answer:1},
     {q:"A non-living thing ___.", options:["does not grow, breathe, or reproduce on its own","needs food and water","breathes","grows on its own"], answer:0},
     {q:"A bird is living because it ___.", options:["can fly only","breathes, eats, and grows","makes noise","is colourful"], answer:1}
   ]},
  {subject:"SocialStudies", title:"My Family", summary:"Students explore different family structures — large, small, single-parent, grandparent families — and appreciate that all families are special.",
   resourceLabel:"YouTube: My Family", resourceUrl:"https://www.youtube.com/results?search_query=My%20Family%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=FHaObkHEkHQ",
   quiz:[
     {q:"A family is a group of ___.", options:["only people who look alike","people who care for and support each other","only parents and children","strangers"], answer:1},
     {q:"Which is an example of a family member?", options:["Grandparent","Teacher","Neighbour","Doctor"], answer:0},
     {q:"Families can be ___.", options:["different sizes and structures","only small","only two people","only large"], answer:0},
     {q:"How do families show they care?", options:["By ignoring each other","By living apart","By helping, listening, and spending time together","By fighting only"], answer:2},
     {q:"Why is your family special?", options:["Every family is unique and special in its own way","It is not","Only big families are special","Only famous families are special"], answer:0}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"Language", title:"Letter B", summary:"Explore uppercase and lowercase B. Students identify the letter, practise its /b/ sound, and name B words such as ball, bear, and butterfly.",
   resourceLabel:"YouTube: Letter B", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20B%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=f1bcER1Zzak",
   quiz:[
     {q:"Which word starts with B?", options:["Dog","Frog","Cat","Ball"], answer:3},
     {q:"What sound does B make?", options:["Buh","Kuh","Duh","Puh"], answer:0},
     {q:"Which B word is an animal?", options:["Sun","Tree","Car","Bat"], answer:3},
     {q:"Find the B: cat, ball, apple, sun", options:["apple","ball","sun","cat"], answer:1},
     {q:"How many bumps does lowercase b have?", options:["0","2","1","3"], answer:2}
   ]},
  {subject:"Math", title:"Counting 6 to 10", summary:"Students count objects from 6 to 10, match numerals to quantities, and practise counting on from 5.",
   resourceLabel:"YouTube: Counting 6 to 10", resourceUrl:"https://www.youtube.com/results?search_query=Counting%206%20to%2010%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mKSNQuQrsm0",
   quiz:[
     {q:"What number comes after 7?", options:["6","9","10","8"], answer:3},
     {q:"Count: ●●●●●●●● How many dots?", options:["8","9","6","7"], answer:0},
     {q:"Which numeral means eight?", options:["7","8","9","6"], answer:1},
     {q:"What number comes before 10?", options:["11","9","7","8"], answer:1},
     {q:"Count by 1s: 6, 7, ___", options:["9","8","10","5"], answer:1}
   ]},
  {subject:"Science", title:"Plants Around Us", summary:"Students explore plants in their environment. All plants have basic needs: sunlight, water, and soil. Plant parts include roots, stem, leaves, and sometimes flowers.",
   resourceLabel:"YouTube: Plants Around Us", resourceUrl:"https://www.youtube.com/results?search_query=Plants%20Around%20Us%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=BwYjVLMucX0",
   quiz:[
     {q:"All plants need ___ to grow.", options:["Snow and ice","Only water","Sunlight, water, and soil","Only sunlight"], answer:2},
     {q:"Which part of a plant soaks up water from the soil?", options:["Roots","Flowers","Stem","Leaves"], answer:0},
     {q:"Leaves help a plant by ___.", options:["making food using sunlight","storing seeds","protecting the roots","holding it up only"], answer:0},
     {q:"Where do most plants grow?", options:["In the air","In soil","In water only","In rocks only"], answer:1},
     {q:"Which is a plant?", options:["Cloud","Daisy","Rock","Cat"], answer:1}
   ]},
  {subject:"SocialStudies", title:"My Home and Community", summary:"Students explore different types of homes (house, apartment, townhouse) and the idea that home is within a neighbourhood and community.",
   resourceLabel:"YouTube: My Home and Community", resourceUrl:"https://www.youtube.com/results?search_query=My%20Home%20and%20Community%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=wP_IbZSxhEs",
   quiz:[
     {q:"A home is a place where ___.", options:["only babies live","people live and feel safe and cared for","only adults live","only families with pets live"], answer:1},
     {q:"Which is a type of home?", options:["Apartment building","School","Library","Hospital"], answer:0},
     {q:"A community is ___.", options:["only a park","only a school","a place where people live and work together","one family only"], answer:2},
     {q:"What makes a home special?", options:["Only if it has a yard","The people and love inside it","Its size","The colour of the walls"], answer:1},
     {q:"Which building is in most communities?", options:["A submarine","A school or fire station","A spaceship","A castle"], answer:1}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"Language", title:"Letter C", summary:"Explore uppercase and lowercase C. Students identify the letter, practise its hard /k/ sound (cat, car), and find C words.",
   resourceLabel:"YouTube: Letter C", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20C%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=1dhzPuT6jm0",
   quiz:[
     {q:"Which word starts with C?", options:["Cat","Egg","Dog","Ball"], answer:0},
     {q:"What sound does C make in 'cat'?", options:["Shh","Chh","Sss","Kuh"], answer:3},
     {q:"Which C word is an animal?", options:["Cow","Car","Cloud","Clock"], answer:0},
     {q:"Find all C words: cat, dog, cow, cup", options:["cat only","cow only","cat, cow, and cup","dog only"], answer:2},
     {q:"Lowercase c looks like ___.", options:["a straight line","a rectangle","two bumps","a circle with a gap on the right"], answer:3}
   ]},
  {subject:"Math", title:"2D Shapes: Circle and Square", summary:"Students identify, name, sort, and describe circles and squares. Circles have no corners; squares have 4 equal sides and 4 corners.",
   resourceLabel:"YouTube: 2D Shapes: Circle and Square", resourceUrl:"https://www.youtube.com/results?search_query=2D%20Shapes%3A%20Circle%20and%20Square%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ux_kLd7qAcY",
   quiz:[
     {q:"A circle has ___ corners.", options:["1","2","0","3"], answer:2},
     {q:"A square has ___ equal sides.", options:["3","5","2","4"], answer:3},
     {q:"Which shape is perfectly round?", options:["Circle","Square","Triangle","Rectangle"], answer:0},
     {q:"How many sides does a square have?", options:["2","4","3","6"], answer:1},
     {q:"Which shape has no straight sides?", options:["Square","Rectangle","Circle","Triangle"], answer:2}
   ]},
  {subject:"Science", title:"Seasons: Autumn", summary:"Students explore the characteristics of autumn in Ontario — shorter days, falling leaves, cooler temperatures, and animals preparing for winter.",
   resourceLabel:"YouTube: Seasons: Autumn", resourceUrl:"https://www.youtube.com/results?search_query=Seasons%3A%20Autumn%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=D6yQ8-M8rmU",
   quiz:[
     {q:"What season comes after summer?", options:["Rainy season","Autumn/Fall","Winter","Spring"], answer:1},
     {q:"In autumn, many trees ___.", options:["grow new leaves","lose their leaves","bloom with flowers","stay exactly the same"], answer:1},
     {q:"Autumn is usually ___ than summer.", options:["hotter","colder than winter","cooler","the same temperature"], answer:2},
     {q:"Animals prepare for winter in autumn by ___.", options:["storing food or preparing to migrate or hibernate","staying exactly the same","swimming more","playing more"], answer:0},
     {q:"What do you wear in autumn?", options:["Light jacket or sweater","Swimsuit and sandals","Nothing different","Heavy winter coat"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Helping at Home", summary:"Students explore household responsibilities and how children can contribute by tidying, setting the table, and caring for pets.",
   resourceLabel:"YouTube: Helping at Home", resourceUrl:"https://www.youtube.com/results?search_query=Helping%20at%20Home%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"Helping at home means ___.", options:["only playing games","only doing homework","doing chores and tasks that help the family","only watching TV"], answer:2},
     {q:"Which is an example of helping at home?", options:["Ignoring chores","Leaving toys everywhere","Putting toys away neatly","Eating all the snacks"], answer:2},
     {q:"Why is it important to help at home?", options:["Only parents should do chores","Only if you are asked","It teaches responsibility and helps the family work together","It is not"], answer:2},
     {q:"Which chore could a kindergartener do?", options:["Cook dinner alone","Fix the roof","Pay the bills","Put shoes away neatly"], answer:3},
     {q:"When you help at home, your family feels ___.", options:["angry","annoyed","nothing","proud and grateful"], answer:3}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"Language", title:"Letter D", summary:"Explore uppercase and lowercase D. Students identify the letter, practise its /d/ sound, and name D words such as dog, duck, and drum.",
   resourceLabel:"YouTube: Letter D", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20D%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=nb8DqaQmNWg",
   quiz:[
     {q:"Which word starts with D?", options:["Cat","Ball","Frog","Dog"], answer:3},
     {q:"What sound does D make?", options:["Duh","Puh","Tuh","Buh"], answer:0},
     {q:"Which D word is an animal?", options:["Door","Duck","Den","Drum"], answer:1},
     {q:"Lowercase d looks like ___.", options:["a circle with a tall line on the right","a curved line only","only a straight line","two bumps"], answer:0},
     {q:"Find the D words: door, cat, duck, ball", options:["duck only","door and duck","ball only","cat and ball"], answer:1}
   ]},
  {subject:"Math", title:"Number Order 1-10", summary:"Students arrange numbers 1-10 in order, identify missing numbers, and understand more/fewer using a number line.",
   resourceLabel:"YouTube: Number Order 1-10", resourceUrl:"https://www.youtube.com/results?search_query=Number%20Order%201-10%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mKSNQuQrsm0",
   quiz:[
     {q:"What number is missing? 1, 2, ___, 4, 5", options:["0","3","7","6"], answer:1},
     {q:"Which number is greater: 7 or 4?", options:["Cannot tell","Equal","4","7"], answer:3},
     {q:"Put in order: 5, 3, 1, 4, 2", options:["3, 1, 2, 4, 5","1, 2, 3, 4, 5","1, 3, 2, 5, 4","5, 4, 3, 2, 1"], answer:1},
     {q:"What comes between 6 and 8?", options:["5","6","9","7"], answer:3},
     {q:"Which has MORE: a group of 2 or a group of 9?", options:["2","Cannot tell","Equal","9"], answer:3}
   ]},
  {subject:"Science", title:"Water Around Us", summary:"Students explore water in their environment. Water is a liquid that flows, takes the shape of its container, and is essential for all life.",
   resourceLabel:"YouTube: Water Around Us", resourceUrl:"https://www.youtube.com/results?search_query=Water%20Around%20Us%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=c-3KCzxEgek",
   quiz:[
     {q:"Water is a ___.", options:["solid","gas","powder","liquid"], answer:3},
     {q:"Living things need water to ___.", options:["survive and stay healthy","only wash","only taste good","only look nice"], answer:0},
     {q:"Where can we find water in nature?", options:["Only in taps","Rivers, lakes, rain, and oceans","Only in bottles","Only in stores"], answer:1},
     {q:"What shape does water take?", options:["Always a ball","Always a cube","The shape of its container","Always flat"], answer:2},
     {q:"Why is clean water important?", options:["Only for swimming","It is not important","For drinking, cooking, and keeping animals and plants alive","Only for cleaning"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Community Helpers: Police and Firefighters", summary:"Students learn how police officers keep communities safe and how firefighters protect people and property. Both are important community helpers.",
   resourceLabel:"YouTube: Community Helpers: Police and Firefighters", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Helpers%3A%20Police%20and%20Firefighters%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=H2mjK20_3xM",
   quiz:[
     {q:"What do police officers do?", options:["Keep communities safe and uphold laws","Deliver mail","Fix buildings","Teach in schools"], answer:0},
     {q:"What do firefighters do?", options:["Teach children to read","Only drive trucks","Protect people from fires and respond to emergencies","Only put out campfires"], answer:2},
     {q:"What number do you call in an emergency in Canada?", options:["911","411","511","211"], answer:0},
     {q:"Firefighters wear special gear to ___.", options:["protect themselves from heat, smoke, and flames","look important","only look scary","run faster"], answer:0},
     {q:"Why are community helpers important?", options:["Only in emergencies","Only adults need them","They are not","They provide services that keep everyone safe and healthy"], answer:3}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"Language", title:"Vowels: A, E, I, O, U", summary:"Students learn to identify the five vowels and their short sounds. Vowels are special letters: a (apple), e (egg), i (igloo), o (octopus), u (umbrella).",
   resourceLabel:"YouTube: Vowels: A, E, I, O, U", resourceUrl:"https://www.youtube.com/results?search_query=Vowels%3A%20A%2C%20E%2C%20I%2C%20O%2C%20U%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=kzVEpZEzhFo",
   quiz:[
     {q:"How many vowels are in the alphabet?", options:["5","6","3","4"], answer:0},
     {q:"Which letter is a vowel?", options:["B","E","F","C"], answer:1},
     {q:"Which word has the short A sound?", options:["Cute","Bike","Pete","Cat"], answer:3},
     {q:"Which word has the short E sound?", options:["Mine","Egg","Cake","Boot"], answer:1},
     {q:"The vowels are ___.", options:["A, E, I, O, U","Only I and O","Only A and E","B, C, D, F, G"], answer:0}
   ]},
  {subject:"Math", title:"Addition to 5", summary:"Students use objects, fingers, and drawings to add two groups and find totals up to 5.",
   resourceLabel:"YouTube: Addition to 5", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20to%205%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mjlsSYLLOSE",
   quiz:[
     {q:"2 + 3 = ?", options:["6","3","5","4"], answer:2},
     {q:"1 + 4 = ?", options:["6","5","4","3"], answer:1},
     {q:"You have 2 apples and 2 oranges. How many fruit in all?", options:["4","2","5","3"], answer:0},
     {q:"0 + 5 = ?", options:["0","4","10","5"], answer:3},
     {q:"What does + mean?", options:["Put together to find the total","Take away","Divide","Multiply"], answer:0}
   ]},
  {subject:"Science", title:"The Sun and Moon", summary:"Students explore the Sun as Earth's main light and heat source. The Moon reflects sunlight and can be seen at night. They observe day and night.",
   resourceLabel:"YouTube: The Sun and Moon", resourceUrl:"https://www.youtube.com/results?search_query=The%20Sun%20and%20Moon%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=sePqPIXMsAc",
   quiz:[
     {q:"The Sun gives us ___ and ___.", options:["light and heat","rain and snow","ice and darkness","cold and wind"], answer:0},
     {q:"The Sun is a ___.", options:["very large star","moon","planet","comet"], answer:0},
     {q:"The Moon ___ its own light.", options:["produces strongly","does not produce — it reflects sunlight","makes plenty of","creates daily"], answer:1},
     {q:"We usually see the Sun during the ___.", options:["only at sunrise","day","only in winter","night"], answer:1},
     {q:"Why should you never look directly at the Sun?", options:["It moves too fast","It is invisible","It is too far away to matter","Its intense light can damage your eyes"], answer:3}
   ]},
  {subject:"SocialStudies", title:"My School Community", summary:"Students explore the school as a community. They identify key helpers: principal, teacher, custodian, librarian, and secretary.",
   resourceLabel:"YouTube: My School Community", resourceUrl:"https://www.youtube.com/results?search_query=My%20School%20Community%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"Who is the leader of a school?", options:["The librarian","The principal","The custodian","The student"], answer:1},
     {q:"What is a teacher's main role?", options:["Help students learn","Fix the building","Answer phones","Cook food"], answer:0},
     {q:"What does a school custodian do?", options:["Drive the bus","Teach reading","Keep the school clean and safe","Run the office"], answer:2},
     {q:"A school is a community because ___.", options:["it has one teacher","only children are there","people work and learn together there","it is a building"], answer:2},
     {q:"Which person helps students find books?", options:["Librarian","Custodian","Secretary","Principal"], answer:0}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"Language", title:"Letter E", summary:"Explore uppercase and lowercase E. Students practise the short /e/ sound (egg, elephant) and identify E words.",
   resourceLabel:"YouTube: Letter E", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20E%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=beaUUPPUT2Y",
   quiz:[
     {q:"Which word starts with E?", options:["Egg","Cat","Apple","Dog"], answer:0},
     {q:"What is the short E sound?", options:["Oh as in go","Ee as in see","Eh as in egg","Ay as in day"], answer:2},
     {q:"Which E word is an animal?", options:["Each","Eagle","Egg","Empty"], answer:1},
     {q:"Which words start with E: cat, egg, tree, elephant?", options:["elephant only","egg only","egg and elephant","cat and tree"], answer:2},
     {q:"E is a ___.", options:["colour","vowel","consonant","number"], answer:1}
   ]},
  {subject:"Math", title:"Patterns: ABAB", summary:"Students identify, copy, extend, and create simple repeating AB patterns using colours, shapes, sounds, and actions.",
   resourceLabel:"YouTube: Patterns: ABAB", resourceUrl:"https://www.youtube.com/results?search_query=Patterns%3A%20ABAB%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Js45cR_7wFE",
   quiz:[
     {q:"What comes next? Red, Blue, Red, Blue, ___", options:["Yellow","Red","Green","Blue"], answer:1},
     {q:"What is the pattern? Circle, Square, Circle, Square", options:["AAAA","ABAB","AABB","ABBA"], answer:1},
     {q:"What comes next? clap, stomp, clap, stomp, ___", options:["jump","sit","stomp","clap"], answer:3},
     {q:"A repeating pattern always ___.", options:["changes randomly","follows the same rule over and over","stops after 4 items","has only 2 colours"], answer:1},
     {q:"Create an ABAB pattern: Star, Heart, Star, Heart, ___", options:["Circle","Star","Heart","Triangle"], answer:1}
   ]},
  {subject:"Science", title:"Pets and Their Needs", summary:"Students explore common pets (dog, cat, fish, bird) and their needs: food, water, shelter, exercise, and love.",
   resourceLabel:"YouTube: Pets and Their Needs", resourceUrl:"https://www.youtube.com/results?search_query=Pets%20and%20Their%20Needs%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=m2MibjJgyjs",
   quiz:[
     {q:"What do all pets need to stay healthy?", options:["Only food","Only a bed","Food, water, shelter, and care","Only toys"], answer:2},
     {q:"Why do dogs need daily exercise?", options:["They do not","Only puppies need exercise","Only for big dogs","Exercise keeps them healthy and happy"], answer:3},
     {q:"A fish needs ___ to breathe.", options:["soil","only food","water with dissolved oxygen (and often a filter)","air like humans"], answer:2},
     {q:"Who is responsible for a pet's care?", options:["The owner/family who chose to have the pet","Only adults","Only the veterinarian","No one"], answer:0},
     {q:"Why is it important to care well for pets?", options:["Only if you want to","It is not","Only for expensive pets","Animals feel pain and need care just as people do; owners are responsible"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Rules and Responsibility", summary:"Students explore why communities have rules: to keep people safe and ensure fairness. They discuss school rules and why following them matters.",
   resourceLabel:"YouTube: Rules and Responsibility", resourceUrl:"https://www.youtube.com/results?search_query=Rules%20and%20Responsibility%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=5dtuZkposkk",
   quiz:[
     {q:"Rules help ___.", options:["keep people safe and ensure fairness","only help adults","only help teachers","create chaos"], answer:0},
     {q:"Which is a school rule?", options:["Run in the halls","Never ask questions","Listen when someone is speaking","Push others in line"], answer:2},
     {q:"What happens if no one follows rules?", options:["Rules fix themselves","Communities become unsafe and unfair","Everything stays the same","Only teachers care"], answer:1},
     {q:"A responsibility is ___.", options:["something others do for you","never fun","a job or duty that you are expected to do","only for adults"], answer:2},
     {q:"Which is an example of responsibility at school?", options:["Only doing your favourite subjects","Littering","Arriving on time with your bag packed","Ignoring a classmate's help"], answer:2}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"Language", title:"Letter F", summary:"Explore uppercase and lowercase F. Students practise the /f/ sound and name F words such as fish, frog, and flower.",
   resourceLabel:"YouTube: Letter F", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20F%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=-kZUq9u7SUk",
   quiz:[
     {q:"Which word starts with F?", options:["Fish","Dog","Cat","Egg"], answer:0},
     {q:"What sound does F make?", options:["Buh","Puh","Vvv","Fff"], answer:3},
     {q:"Which F word is an animal?", options:["Frog","Farm","Float","Flower"], answer:0},
     {q:"Find all F words: fish, cat, frog, flower", options:["fish only","fish, frog, and flower","frog only","cat only"], answer:1},
     {q:"Lowercase f looks like ___.", options:["a straight line","a circle","a hook at the top with a crossbar","two bumps"], answer:2}
   ]},
  {subject:"Math", title:"Counting to 20", summary:"Students count forward from any number to 20, identify missing numbers, and begin to recognise teen numbers as ten and some more.",
   resourceLabel:"YouTube: Counting to 20", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20to%2020%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=D0Ajq682yrA",
   quiz:[
     {q:"What comes after 13?", options:["16","15","14","12"], answer:2},
     {q:"Count: 15, 16, 17, ___", options:["20","19","18","14"], answer:2},
     {q:"Which number is between 10 and 12?", options:["11","8","9","13"], answer:0},
     {q:"How many tens are in the number 15?", options:["5","1","0","2"], answer:1},
     {q:"Count on from 17: 17, 18, 19, ___", options:["16","22","21","20"], answer:3}
   ]},
  {subject:"Science", title:"Wild Animals", summary:"Students explore wild animals in Ontario and beyond. Wild animals live in natural habitats, find their own food, and are not tamed.",
   resourceLabel:"YouTube: Wild Animals", resourceUrl:"https://www.youtube.com/results?search_query=Wild%20Animals%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=CA6Mofzh7jo",
   quiz:[
     {q:"A wild animal is one that ___.", options:["is always dangerous","lives in a natural habitat and finds its own food","is someone's pet","lives in a cage"], answer:1},
     {q:"Which is a wild animal?", options:["Cat","Goldfish","Moose","Dog"], answer:2},
     {q:"Where would you find a beaver in the wild?", options:["In a city apartment","In a desert","In a shopping mall","Near lakes and rivers in forests"], answer:3},
     {q:"Wild animals should ___.", options:["be hunted for food always","be observed from a safe distance and left in their habitat","be taken home as pets","always be fed by humans"], answer:1},
     {q:"What do wild animals eat?", options:["What they find in their natural habitat (prey, plants, insects)","Food from grocery stores","Only vegetables","Only what humans give them"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Being a Good Friend", summary:"Students explore qualities of friendship: kindness, sharing, taking turns, listening, and including others. Good friends treat each other with respect.",
   resourceLabel:"YouTube: Being a Good Friend", resourceUrl:"https://www.youtube.com/results?search_query=Being%20a%20Good%20Friend%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lWgi6fHYlF8",
   quiz:[
     {q:"A good friend ___.", options:["is kind and includes others","ignores you when busy","takes your things without asking","only plays with you if you have toys"], answer:0},
     {q:"Sharing means ___.", options:["only sharing with best friends","only sharing food","keeping everything for yourself","letting others use or enjoy what you have"], answer:3},
     {q:"Taking turns means ___.", options:["only one person goes","always going first","skipping others","each person gets a chance"], answer:3},
     {q:"Why is it important to include everyone?", options:["It is not","Everyone deserves to feel welcome and belonging","Only some people need friends","Only if you like them"], answer:1},
     {q:"Which is an act of friendship?", options:["Pushing in line","Ignoring a friend who is sad","Laughing at a mistake","Cheering a friend on when they try something hard"], answer:3}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"Language", title:"Letter G", summary:"Explore uppercase and lowercase G. Students practise the hard /g/ sound (goat, grape) and find G words.",
   resourceLabel:"YouTube: Letter G", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20G%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=0KXtxIiQ7gk",
   quiz:[
     {q:"Which word starts with G?", options:["Goat","Dog","Fish","Apple"], answer:0},
     {q:"What sound does G make in 'goat'?", options:["Kuh","Guh","Juh","Shh"], answer:1},
     {q:"Which G word is a fruit?", options:["Grass","Goat","Grape","Grain"], answer:2},
     {q:"Find the G: dog, goat, green, frog", options:["goat","green","goat and green","dog"], answer:2},
     {q:"G is a ___.", options:["vowel","number","colour","consonant"], answer:3}
   ]},
  {subject:"Math", title:"Non-Standard Measurement: Length", summary:"Students measure the length of objects using non-standard units (paper clips, blocks, hands) and use the words longer, shorter, and same.",
   resourceLabel:"YouTube: Non-Standard Measurement: Length", resourceUrl:"https://www.youtube.com/results?search_query=Non-Standard%20Measurement%3A%20Length%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2wUsdsae0ro",
   quiz:[
     {q:"Measuring tells you ___.", options:["where something is","the colour of something","how long, tall, or heavy something is","what something smells like"], answer:2},
     {q:"Non-standard units for measuring include ___.", options:["thermometers","paper clips, hand spans, or blocks","metres and centimetres","kilograms"], answer:1},
     {q:"A book is 8 paper clips long. A pencil is 5. The book is ___.", options:["shorter","longer","the same length as the pencil","impossible to compare"], answer:1},
     {q:"To compare lengths fairly, you must ___.", options:["guess","always use a ruler","use a computer","start measuring from the same point"], answer:3},
     {q:"If a desk is 3 shoe lengths long, shoe length is a ___.", options:["weight unit","temperature unit","standard unit","non-standard unit"], answer:3}
   ]},
  {subject:"Science", title:"Parts of a Plant", summary:"Students name and describe the function of plant parts: roots (absorb water), stem (transport water and support), leaves (make food), flower (reproduction), seed (new plant).",
   resourceLabel:"YouTube: Parts of a Plant", resourceUrl:"https://www.youtube.com/results?search_query=Parts%20of%20a%20Plant%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=A-xScqCN0GA",
   quiz:[
     {q:"Roots help a plant by ___.", options:["protecting seeds","absorbing water and nutrients from the soil","making food using sunlight","producing flowers"], answer:1},
     {q:"The stem of a plant ___.", options:["only holds seeds","supports the plant and carries water from roots to leaves","absorbs sunlight directly","only makes flowers"], answer:1},
     {q:"Leaves are the main part of a plant that ___.", options:["absorb water from soil","make food using sunlight and air","hold up the plant","produce seeds only"], answer:1},
     {q:"A flower helps a plant by ___.", options:["supporting the stem","producing seeds that grow into new plants","making food","absorbing water"], answer:1},
     {q:"A seed will grow into ___.", options:["only a stem","a root only","a new plant","a flower only"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Canadian Symbols", summary:"Students learn symbols that represent Canada: the maple leaf flag, beaver, and Parliament Buildings. These symbols create a shared Canadian identity.",
   resourceLabel:"YouTube: Canadian Symbols", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Symbols%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=38BGXJ572Y8",
   quiz:[
     {q:"What appears on the Canadian flag?", options:["A maple leaf","A moose","An eagle","A beaver"], answer:0},
     {q:"Canada's national animal is the ___.", options:["beaver","moose","bear","wolf"], answer:0},
     {q:"The maple leaf is a symbol of ___.", options:["England","Canada","France","the United States"], answer:1},
     {q:"Where does the Canadian government meet?", options:["The CN Tower","Niagara Falls","The Rocky Mountains","Parliament Hill in Ottawa"], answer:3},
     {q:"Why do countries have symbols?", options:["Only for flags","To identify the nation and give its people a shared sense of pride and belonging","Only for money","Only for tourists"], answer:1}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"Language", title:"Letter H", summary:"Explore uppercase and lowercase H. Students practise the /h/ sound and name H words such as house, horse, and hat.",
   resourceLabel:"YouTube: Letter H", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20H%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PUI5-AphjMg",
   quiz:[
     {q:"Which word starts with H?", options:["Dog","Apple","House","Frog"], answer:2},
     {q:"What sound does H make?", options:["Kuh","Shh","Puh","Huh (a breathy sound)"], answer:3},
     {q:"Which H word do you wear on your head?", options:["Horse","Hand","Hat","House"], answer:2},
     {q:"Find the H: hat, dog, horse, cat", options:["dog and cat","hat only","hat and horse","horse only"], answer:2},
     {q:"H is a ___.", options:["number","consonant","vowel","colour"], answer:1}
   ]},
  {subject:"Math", title:"Subtraction from 5", summary:"Students subtract within 5 using objects, pictures, and fingers. They understand subtraction as taking away.",
   resourceLabel:"YouTube: Subtraction from 5", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20from%205%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=rqiu_xcvSk4",
   quiz:[
     {q:"5 - 2 = ?", options:["2","3","4","5"], answer:1},
     {q:"4 - 4 = ?", options:["8","1","0","4"], answer:2},
     {q:"What does the - sign mean?", options:["Take away","Measure","Add","Multiply"], answer:0},
     {q:"3 - 1 = ?", options:["3","4","2","1"], answer:2},
     {q:"You have 5 grapes and eat 3. How many are left?", options:["2","4","1","3"], answer:0}
   ]},
  {subject:"Science", title:"Winter Season", summary:"Students explore characteristics of winter in Ontario: cold temperatures, ice and snow, shorter days, and how animals and plants respond.",
   resourceLabel:"YouTube: Winter Season", resourceUrl:"https://www.youtube.com/results?search_query=Winter%20Season%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=e19bGkyRJLg",
   quiz:[
     {q:"What is winter like in Ontario?", options:["Always rainy","Very hot and sunny","Never changes","Cold with snow and ice"], answer:3},
     {q:"In winter, deciduous trees (like maples) ___.", options:["stay green","grow new leaves","lose their leaves (they fell in autumn)","bloom with flowers"], answer:2},
     {q:"Some animals hibernate in winter. Hibernation means ___.", options:["flying south","growing thicker fur","sleeping deeply to save energy through winter","staying exactly the same"], answer:2},
     {q:"Days are ___ in winter than in summer.", options:["longer","the same length","exactly 12 hours","shorter"], answer:3},
     {q:"What do humans wear in winter to stay warm?", options:["Heavy coats, mittens, and boots","No special clothing","T-shirts and shorts","Swimsuits"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Our Environment: Caring for Nature", summary:"Students learn that the environment includes air, water, land, plants, and animals. Everyone can help protect it by reducing waste and not littering.",
   resourceLabel:"YouTube: Our Environment: Caring for Nature", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Environment%3A%20Caring%20for%20Nature%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=UWdx1Fgn75o",
   quiz:[
     {q:"The environment includes ___.", options:["only animals","only plants","only what we can see in cities","the air, water, land, plants, and all living things around us"], answer:3},
     {q:"Littering means ___.", options:["picking up litter","recycling properly","composting","dropping waste on the ground instead of in a bin"], answer:2},
     {q:"How can you help the environment?", options:["Leave taps running","Use extra plastic bags","Litter in parks","Turn off lights and put waste in the bin"], answer:3},
     {q:"Why is clean air important?", options:["Only in cities","Only for birds","Only in summer","All living things need clean air to breathe and stay healthy"], answer:3},
     {q:"Recycling helps the environment because ___.", options:["it reduces waste and reuses materials","it makes more rubbish","it is only for adults","only paper can be recycled"], answer:0}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"Language", title:"Short Vowel Sounds", summary:"Students review and practise identifying short vowel sounds: a (cat), e (hen), i (pig), o (dog), u (bug) in spoken words.",
   resourceLabel:"YouTube: Short Vowel Sounds", resourceUrl:"https://www.youtube.com/results?search_query=Short%20Vowel%20Sounds%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=RUSCz41aDug",
   quiz:[
     {q:"Which word has the short A sound?", options:["Bike","Cat","Cute","Name"], answer:1},
     {q:"Which word has the short I sound?", options:["Pig","Cake","Tube","Pete"], answer:0},
     {q:"Which word has the short O sound?", options:["Blue","Bean","Dog","Rain"], answer:2},
     {q:"Which word has the short U sound?", options:["Cake","Rain","Bee","Bug"], answer:3},
     {q:"All short vowel sounds come from ___.", options:["the vowels A, E, I, O, U","only A and E","consonants","numbers"], answer:0}
   ]},
  {subject:"Math", title:"3D Shapes: Sphere, Cube, Cylinder", summary:"Students identify and describe 3D shapes they encounter daily. A sphere (ball), cube (dice), and cylinder (can) are explored.",
   resourceLabel:"YouTube: 3D Shapes: Sphere, Cube, Cylinder", resourceUrl:"https://www.youtube.com/results?search_query=3D%20Shapes%3A%20Sphere%2C%20Cube%2C%20Cylinder%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=guNdJ5MtX1A",
   quiz:[
     {q:"A sphere looks like ___.", options:["a box","a cone","a ball","a flat circle"], answer:2},
     {q:"A cube has ___ flat faces.", options:["6","8","4","5"], answer:0},
     {q:"Which 3D shape is a can of soup?", options:["Cone","Sphere","Cylinder","Cube"], answer:2},
     {q:"Which 3D shape can roll in any direction?", options:["Sphere","Cube","Cylinder","Cone"], answer:0},
     {q:"How many corners (vertices) does a cube have?", options:["4","12","6","8"], answer:3}
   ]},
  {subject:"Science", title:"Weather", summary:"Students explore types of weather (sunny, cloudy, rainy, snowy, windy) and learn that weather affects what we wear and do each day.",
   resourceLabel:"YouTube: Weather", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=yPqRqjM8MOQ",
   quiz:[
     {q:"Weather is ___.", options:["the same every day","only about temperature","the condition of the air outside at a particular time","only rain or sunshine"], answer:2},
     {q:"Which tool measures temperature outside?", options:["A compass","A thermometer","A ruler","A scale"], answer:1},
     {q:"On a rainy day, you would wear ___.", options:["a swimsuit","a raincoat and boots","sandals and shorts","a heavy winter coat"], answer:1},
     {q:"Why does weather change from day to day?", options:["Only the Sun affects weather","Movements of air, moisture, and temperature differences cause weather changes","Only in spring","It does not change"], answer:1},
     {q:"Which weather word means 'no clouds and bright sunshine'?", options:["Snowy","Sunny","Cloudy","Foggy"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Family Traditions", summary:"Students learn that families celebrate traditions: special events, foods, stories, and practices that are passed down and shared. All traditions are valued.",
   resourceLabel:"YouTube: Family Traditions", resourceUrl:"https://www.youtube.com/results?search_query=Family%20Traditions%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=pD8dTo4NxHM",
   quiz:[
     {q:"A family tradition is ___.", options:["only a holiday","a special practice, story, or celebration that a family shares and passes down","only about food","something only old people do"], answer:1},
     {q:"An example of a family tradition could be ___.", options:["a special meal made every year for a holiday","arguing about rules","never celebrating anything","ignoring family members"], answer:0},
     {q:"Why are traditions important?", options:["Only for certain cultures","They connect families to their history and heritage and create special memories","Only for wealthy families","They are not"], answer:1},
     {q:"Can different families have different traditions?", options:["Yes — each family's traditions are unique and special","Only if they are the same culture","Only in other countries","No"], answer:0},
     {q:"Sharing family traditions with classmates ___.", options:["only confuses others","is embarrassing","shows respect and helps others learn about different cultures","causes problems"], answer:2}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"Language", title:"Letter I", summary:"Explore uppercase and lowercase I. Students practise the short /i/ sound (igloo, insect) and the long /i/ sound (ice, island).",
   resourceLabel:"YouTube: Letter I", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20I%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=b_gJVJvOA3Q",
   quiz:[
     {q:"Which word has the short I sound?", options:["Igloo","Ice","Fire","Bike"], answer:0},
     {q:"Which word starts with I and is a cold home?", options:["Iron","Ivy","Island","Igloo"], answer:3},
     {q:"I is a ___.", options:["consonant","number","vowel","colour"], answer:2},
     {q:"Find the I: ant, igloo, elephant, octopus", options:["elephant","ant","octopus","igloo"], answer:3},
     {q:"Which I word is a small creature?", options:["Island","Insect","Ice","Iron"], answer:1}
   ]},
  {subject:"Math", title:"Addition to 10", summary:"Students add two groups with totals up to 10. They use number lines, counters, and drawings.",
   resourceLabel:"YouTube: Addition to 10", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20to%2010%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mjlsSYLLOSE",
   quiz:[
     {q:"4 + 6 = ?", options:["8","11","10","9"], answer:2},
     {q:"7 + 3 = ?", options:["8","9","11","10"], answer:3},
     {q:"You have 5 stickers and get 4 more. How many total?", options:["8","9","10","11"], answer:1},
     {q:"3 + 3 = ?", options:["5","6","8","7"], answer:1},
     {q:"8 + 2 = ?", options:["10","11","9","12"], answer:0}
   ]},
  {subject:"Science", title:"Farm Animals", summary:"Students learn about common farm animals (cow, pig, chicken, sheep, horse) and how farms provide food and other products for communities.",
   resourceLabel:"YouTube: Farm Animals", resourceUrl:"https://www.youtube.com/results?search_query=Farm%20Animals%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zFtMamMUAVw",
   quiz:[
     {q:"Which animal lives on a farm and gives us milk?", options:["Cow","Cat","Fish","Dog"], answer:0},
     {q:"Which farm animal gives us wool for clothing?", options:["Pig","Sheep","Cow","Horse"], answer:1},
     {q:"Eggs come from ___.", options:["sheep","pigs","cows","chickens"], answer:3},
     {q:"Why are farms important?", options:["They are not","Only animals live there","Only for rural people","Farms produce food that feeds communities and countries"], answer:3},
     {q:"Which of these is a farm animal?", options:["Tiger","Polar bear","Horse","Elephant"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Kinds of Families", summary:"Students learn that families can look different — some have two parents, some one parent, some grandparents as caregivers, blended families — and all are equally valid.",
   resourceLabel:"YouTube: Kinds of Families", resourceUrl:"https://www.youtube.com/results?search_query=Kinds%20of%20Families%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=hpCyiyNqzlE",
   quiz:[
     {q:"All families are ___.", options:["the same","small","different and equally special and valid","only large"], answer:2},
     {q:"Which is an example of a family type?", options:["A school","A single-parent family","A country","A city"], answer:1},
     {q:"A blended family is one where ___.", options:["only one parent lives in the house","only grandparents live together","two families join together (step-parents, step-siblings)","no children are present"], answer:2},
     {q:"What makes every family special?", options:["Only how big the house is","The love and care the members share","Only its size","Only its money"], answer:1},
     {q:"Why is it important to respect different kinds of families?", options:["All families deserve respect; diversity in families is natural and normal","Only if they are like yours","Only traditional families are valid","It is not"], answer:0}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"Language", title:"Letter J", summary:"Explore uppercase and lowercase J. Students practise the /j/ sound and name J words such as jump, jungle, and jar.",
   resourceLabel:"YouTube: Letter J", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20J%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=6KXX6fCKWes",
   quiz:[
     {q:"Which word starts with J?", options:["Cat","Kite","Jump","Dog"], answer:2},
     {q:"What sound does J make?", options:["Kuh","Juh (as in jump)","Shh","Yuh"], answer:1},
     {q:"Which J word means to leap into the air?", options:["Jump","Just","Jar","Jam"], answer:0},
     {q:"Find the J: jellyfish, cat, jar, apple", options:["jellyfish only","cat and apple","jar only","jellyfish and jar"], answer:3},
     {q:"J is a ___.", options:["number","vowel","consonant","colour"], answer:2}
   ]},
  {subject:"Math", title:"Ordinal Numbers: 1st to 5th", summary:"Students use ordinal numbers (first, second, third, fourth, fifth) to describe position in a line or sequence.",
   resourceLabel:"YouTube: Ordinal Numbers: 1st to 5th", resourceUrl:"https://www.youtube.com/results?search_query=Ordinal%20Numbers%3A%201st%20to%205th%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=BdVlwetlzOM",
   quiz:[
     {q:"First means ___.", options:["number one in position","second","last in line","in the middle"], answer:0},
     {q:"If you win a race, you are in ___ place.", options:["last","first","third","second"], answer:1},
     {q:"Third means ___.", options:["4th in order","5th in order","2nd in order","3rd in order"], answer:3},
     {q:"In a line of 5: cat, dog, bird, fish, rabbit — which is SECOND?", options:["dog","cat","bird","fish"], answer:0},
     {q:"The word 'second' describes ___.", options:["only sports rankings","only book chapters","a place in an ordered sequence","a unit of time only"], answer:2}
   ]},
  {subject:"Science", title:"Materials: Natural and Human-Made", summary:"Students sort materials into natural (wood, cotton, water, wool) and human-made/manufactured (plastic, glass, metal, nylon). Both types have different properties and uses.",
   resourceLabel:"YouTube: Materials: Natural and Human-Made", resourceUrl:"https://www.youtube.com/results?search_query=Materials%3A%20Natural%20and%20Human-Made%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PDqcFqdarzk",
   quiz:[
     {q:"A natural material is one that ___.", options:["is always plastic","comes from nature (plants, animals, or the earth)","is made in a factory","is never used for clothing"], answer:1},
     {q:"Which is a natural material?", options:["Nylon","Glass","Plastic","Wood"], answer:3},
     {q:"Which is a human-made (manufactured) material?", options:["Wood","Cotton","Plastic","Wool"], answer:2},
     {q:"Why do humans make new materials?", options:["Only for factories","Only for decoration","Natural materials are bad","To create materials with specific properties that may not exist in nature"], answer:3},
     {q:"Wool comes from ___.", options:["factories","trees","sheep","plastic plants"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Our Town/City", summary:"Students explore the features of their local community: streets, buildings, parks, services, and how the town/city helps people meet their needs.",
   resourceLabel:"YouTube: Our Town/City", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Town%2FCity%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=JAlPmtJm6eA",
   quiz:[
     {q:"What is a community?", options:["Only a shopping centre","Only a school","Only one house","A group of people living and working together in an area"], answer:3},
     {q:"Which feature do most towns have?", options:["Only one store","A volcano","An ocean beach","Roads, schools, and emergency services"], answer:3},
     {q:"A park is an important community space because ___.", options:["it gives people a place to relax, play, and connect with nature","it replaces schools","only athletes use it","it is only for dogs"], answer:0},
     {q:"Which service helps when there is a fire?", options:["Library","School","Grocery store","Fire station"], answer:0},
     {q:"Why do people live in communities?", options:["Only for shopping","To be isolated","Only for work","Communities allow people to share resources, services, and support each other"], answer:3}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"Language", title:"Letter K", summary:"Explore uppercase and lowercase K. Students practise the /k/ sound (same as hard C) and name K words such as kite, king, and kangaroo.",
   resourceLabel:"YouTube: Letter K", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20K%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=TxH4HwSdu9c",
   quiz:[
     {q:"Which word starts with K?", options:["Cat","Ball","Door","Kite"], answer:3},
     {q:"K makes the same sound as ___.", options:["G","H","soft C (sss)","hard C (kuh)"], answer:3},
     {q:"Which K word is a large jumping animal?", options:["Kangaroo","Kite","King","Kind"], answer:0},
     {q:"Find the K: kite, cat, king, dog", options:["kite only","kite and king","cat and dog","king only"], answer:1},
     {q:"K is a ___.", options:["vowel","number","consonant","colour"], answer:2}
   ]},
  {subject:"Math", title:"ABC Patterns", summary:"Students identify, extend, and create ABC patterns (three repeating units) using colours, shapes, and objects.",
   resourceLabel:"YouTube: ABC Patterns", resourceUrl:"https://www.youtube.com/results?search_query=ABC%20Patterns%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zegJZ5WsqUo",
   quiz:[
     {q:"In an ABC pattern, what comes after A, B, C?", options:["A (the pattern repeats)","C","B","D"], answer:0},
     {q:"What comes next? Red, Blue, Green, Red, Blue, ___", options:["Yellow","Green","Red","Blue"], answer:1},
     {q:"Identify: triangle, circle, square, triangle, circle, ___", options:["square","triangle","rectangle","circle"], answer:0},
     {q:"An ABC pattern repeats every ___ items.", options:["2","5","3","4"], answer:2},
     {q:"Create: Cat, Dog, Bird, Cat, Dog, ___", options:["Fish","Bird","Dog","Cat"], answer:1}
   ]},
  {subject:"Science", title:"Sound and Light", summary:"Students explore that sound travels as vibrations and light travels in straight lines. They investigate different sources of both.",
   resourceLabel:"YouTube: Sound and Light", resourceUrl:"https://www.youtube.com/results?search_query=Sound%20and%20Light%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ssB_EgEOuRM",
   quiz:[
     {q:"Sound is produced by ___.", options:["magnetic fields","light waves","heat only","vibrations"], answer:3},
     {q:"You can make sound by ___.", options:["looking at things","only pressing a button","only singing","banging, plucking, blowing, or vibrating objects"], answer:3},
     {q:"Light travels in ___.", options:["circles","curves","zigzags","straight lines"], answer:3},
     {q:"Which is a natural source of light?", options:["A television","A torch","A lamp","The Sun"], answer:3},
     {q:"Why do we need light?", options:["To see, grow plants, and feel warmth","Only for reading","Only at night","Only in winter"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Rights and Responsibilities", summary:"Students learn that rights (things they are entitled to: safety, education, play) come with responsibilities (duties: respect, cooperation, looking after things).",
   resourceLabel:"YouTube: Rights and Responsibilities", resourceUrl:"https://www.youtube.com/results?search_query=Rights%20and%20Responsibilities%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=TafvHxXFzUM",
   quiz:[
     {q:"A right is something you ___.", options:["are entitled to have or do","must give up","can take from others","never deserve"], answer:0},
     {q:"A responsibility is something you ___.", options:["can ignore","never have as a child","are expected to do or look after","only do when adults watch"], answer:2},
     {q:"Which is a right of children in Canada?", options:["No protection under law","Education, safety, and play","Working long hours","Only food"], answer:1},
     {q:"Which is a responsibility at school?", options:["Arriving late every day","Treating classmates with respect","Littering in the hallway","Ignoring classroom rules"], answer:1},
     {q:"Rights and responsibilities ___.", options:["only governments have","go together — having rights means respecting others' rights too","only adults have","are unrelated"], answer:1}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"Language", title:"Letter L", summary:"Explore uppercase and lowercase L. Students practise the /l/ sound and name L words such as leaf, lion, and lemon.",
   resourceLabel:"YouTube: Letter L", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20L%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=aw8_argqbmA",
   quiz:[
     {q:"Which word starts with L?", options:["Leaf","Apple","Dog","Mango"], answer:0},
     {q:"What sound does L make?", options:["Ruh","Puh","Buh","Lll (as in leaf)"], answer:3},
     {q:"Which L word is an animal?", options:["Leaf","Lion","Light","Lemon"], answer:1},
     {q:"Find all L words: leaf, dog, lemon, lion", options:["lemon only","lion only","dog only","leaf, lemon, and lion"], answer:3},
     {q:"Lowercase l looks like ___.", options:["a bump","a tall straight line","two bumps","a curve"], answer:1}
   ]},
  {subject:"Math", title:"Number Words 1 to 10", summary:"Students match numerals to number words: one, two, three, four, five, six, seven, eight, nine, ten.",
   resourceLabel:"YouTube: Number Words 1 to 10", resourceUrl:"https://www.youtube.com/results?search_query=Number%20Words%201%20to%2010%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=WfEyynAaLRY",
   quiz:[
     {q:"Which number word means 5?", options:["Six","Three","Four","Five"], answer:3},
     {q:"The number 8 is spelled ___.", options:["Eigth","Eight","Ate","Ayt"], answer:1},
     {q:"Which number word means 10?", options:["Ten","Seven","Eight","Nine"], answer:0},
     {q:"Match: 3 = ?", options:["Four","One","Three","Two"], answer:2},
     {q:"How do you spell 7?", options:["Sevan","Siven","Sevun","Seven"], answer:3}
   ]},
  {subject:"Science", title:"Spring Season", summary:"Students explore characteristics of spring in Ontario: warming temperatures, returning birds, blossoming plants, and rain showers.",
   resourceLabel:"YouTube: Spring Season", resourceUrl:"https://www.youtube.com/results?search_query=Spring%20Season%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=1hPCeJKhl-4",
   quiz:[
     {q:"What season comes after winter?", options:["Autumn","Summer","Rainy season","Spring"], answer:3},
     {q:"In spring, plants ___.", options:["start growing again","die off","go dormant","have no change"], answer:0},
     {q:"Many birds ___ in spring after being away in warmer places.", options:["hibernate","disappear","return (migrate back north)","stay underground"], answer:2},
     {q:"Spring weather in Ontario is often ___.", options:["warming, with rain showers","hot and dry like summer","always perfect","cold and snowy like winter"], answer:0},
     {q:"What is one sign that spring has arrived?", options:["Very cold temperatures","Snow on the ground","Leaves falling from trees","Flowers blooming and birds singing"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Special People in My Life", summary:"Students identify and appreciate special people in their lives: family members, friends, teachers, and community helpers who contribute to their wellbeing.",
   resourceLabel:"YouTube: Special People in My Life", resourceUrl:"https://www.youtube.com/results?search_query=Special%20People%20in%20My%20Life%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=jt2q1cHsH6E",
   quiz:[
     {q:"A special person in your life is someone who ___.", options:["ignores you","only gives you gifts","cares about you, helps you, and makes you feel valued","does not care about you"], answer:2},
     {q:"How can you show appreciation to someone special?", options:["Say thank you and show kindness","Never talk to them","Take their things","Ignore them"], answer:0},
     {q:"Which person at school helps you feel safe and learn every day?", options:["No one","Someone on TV","A stranger","Your teacher"], answer:3},
     {q:"Why is it important to appreciate the people who help you?", options:["It shows respect and encourages positive relationships","Only for birthdays","Only if they give you things","It is not"], answer:0},
     {q:"A community helper who is special to the community is ___.", options:["only a family member","only a teacher","only a policeman","anyone who contributes positively to others' wellbeing"], answer:3}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"Language", title:"Letter M", summary:"Explore uppercase and lowercase M. Students practise the /m/ sound and name M words such as moon, monkey, and mango.",
   resourceLabel:"YouTube: Letter M", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20M%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=dxrS93gOdck",
   quiz:[
     {q:"Which word starts with M?", options:["Dog","Moon","Apple","Kite"], answer:1},
     {q:"What sound does M make?", options:["Buh","Mmm (lips together)","Nnn","Puh"], answer:1},
     {q:"Which M word is an animal?", options:["Mud","Moon","Monkey","Mango"], answer:2},
     {q:"Find all M words: moon, sun, mango, monkey", options:["mango only","monkey only","moon, mango, monkey","sun only"], answer:2},
     {q:"Lowercase m has ___.", options:["one bump","three bumps","two bumps","no bumps"], answer:2}
   ]},
  {subject:"Math", title:"Counting by 2s to 20", summary:"Students skip-count by 2s (2, 4, 6, 8...) to 20, recognising the pattern of even numbers.",
   resourceLabel:"YouTube: Counting by 2s to 20", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20by%202s%20to%2020%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=GvTcpfSnOMQ",
   quiz:[
     {q:"Count by 2s: 2, 4, 6, ___", options:["10","9","7","8"], answer:3},
     {q:"Count by 2s: 10, 12, 14, ___", options:["18","16","17","15"], answer:1},
     {q:"Counting by 2s gives you ___ numbers.", options:["even","odd","random","prime"], answer:0},
     {q:"What comes next? 16, 18, ___", options:["21","20","17","19"], answer:1},
     {q:"Which list is counting by 2s?", options:["2,3,5,7,11","1,3,5,7,9","1,2,3,4,5","2,4,6,8,10"], answer:3}
   ]},
  {subject:"Science", title:"Seasons Review", summary:"Students review the four seasons in Ontario, reinforcing what changes during each — temperatures, clothing, plants, animals, and activities.",
   resourceLabel:"YouTube: Seasons Review", resourceUrl:"https://www.youtube.com/results?search_query=Seasons%20Review%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=PBM8N0jktso",
   quiz:[
     {q:"Which season comes after summer?", options:["Fall/Autumn","Spring","Rainy season","Winter"], answer:0},
     {q:"In spring, many animals ___.", options:["hibernate","migrate south","have babies and become active again","go dormant"], answer:2},
     {q:"What type of clothing do you wear in summer?", options:["Ski gear","Light clothes and shorts","Heavy coat and boots","Thick sweaters"], answer:1},
     {q:"In fall, many farmers ___.", options:["do nothing","harvest their crops","begin planting seeds","plant crops"], answer:1},
     {q:"Which season is it when you can make a snowman?", options:["Spring","Fall","Winter","Summer"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Community Helpers: Doctors and Teachers", summary:"Students explore how doctors keep us healthy and how teachers help us learn. They appreciate that community helpers work to improve the lives of everyone.",
   resourceLabel:"YouTube: Community Helpers: Doctors and Teachers", resourceUrl:"https://www.youtube.com/results?search_query=Community%20Helpers%3A%20Doctors%20and%20Teachers%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=bwx2Z69S0YA",
   quiz:[
     {q:"What does a doctor do?", options:["Drive a fire truck","Build houses","Help people stay healthy and treat illness","Teach reading and writing"], answer:2},
     {q:"Why is a teacher an important community helper?", options:["They fix cars","They deliver mail","They cook food","They help children learn and grow"], answer:3},
     {q:"Where do you go to see a doctor?", options:["A fire station","A library","A school","A clinic or hospital"], answer:3},
     {q:"Community helpers work to make our community ___.", options:["better and safer for everyone","worse","smaller","confusing"], answer:0},
     {q:"Who would you visit for a check-up to make sure you are healthy?", options:["Librarian","Teacher","Firefighter","Doctor"], answer:3}
   ]},
]},
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"Language", title:"Letter P", summary:"Explore uppercase and lowercase P. Students identify the letter, practise its sound, and name words beginning with P such as penguin, pizza, and purple.",
   resourceLabel:"YouTube: Letter P", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20P%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=-v1fg2Hp63s",
   quiz:[
     {q:"What sound does the letter P make?", options:["Puh","Guh","Buh","Duh"], answer:0},
     {q:"Which word starts with P?", options:["Pig","Run","Cat","Dog"], answer:0},
     {q:"How do you write a lowercase p?", options:["A tall stick","Like a b facing right","Two circles","A stick with a circle at the bottom left"], answer:3},
     {q:"Which of these starts with P?", options:["Banana","Apple","Mango","Pear"], answer:3},
     {q:"Find the P word: sun, moon, ___, stars", options:["Cloud","Rain","Planet","Sky"], answer:2}
   ]},
  {subject:"Math", title:"Numbers 1-20: Recognition", summary:"Students read and write numerals 1 to 20, connecting each numeral to its quantity.",
   resourceLabel:"YouTube: Numbers 1-20: Recognition", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%201-20%3A%20Recognition%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=rMDqnSmfG2w",
   quiz:[
     {q:"What number comes after 15?", options:["17","14","16","18"], answer:2},
     {q:"Which numeral means fifteen?", options:["15","51","5","150"], answer:0},
     {q:"Count: 17, 18, 19, ___", options:["20","21","22","10"], answer:0},
     {q:"Which group has 20 items?", options:["A group of twenty","A group of fifteen","A group of five","A group of ten"], answer:0},
     {q:"Write the number: nineteen", options:["9","19","190","91"], answer:1}
   ]},
  {subject:"Science", title:"Push and Pull: Forces", summary:"Students explore how pushing and pulling are forces that move objects. They observe that heavier objects need more force.",
   resourceLabel:"YouTube: Push and Pull: Forces", resourceUrl:"https://www.youtube.com/results?search_query=Push%20and%20Pull%3A%20Forces%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=GXedKUqEGJE",
   quiz:[
     {q:"A push moves an object ___ you.", options:["away from","beside","under","toward"], answer:0},
     {q:"A pull moves an object ___ you.", options:["beside","under","away from","toward"], answer:3},
     {q:"Which is an example of a push?", options:["Picking up a book","Opening a drawer toward you","Kicking a ball","Pulling a wagon"], answer:2},
     {q:"Which is an example of a pull?", options:["Pushing a door open","Opening a drawer toward you","Kicking a soccer ball","Throwing a ball"], answer:1},
     {q:"A heavy object needs ___ force to move than a light one.", options:["the same","less","more","no"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Our School Community", summary:"Students explore the school as a community. They identify helpers such as the principal, caretaker, librarian, and office staff.",
   resourceLabel:"YouTube: Our School Community", resourceUrl:"https://www.youtube.com/results?search_query=Our%20School%20Community%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"Who is the leader of a school?", options:["Teacher","Principal","Caretaker","Librarian"], answer:1},
     {q:"What does a librarian do?", options:["Help with books and reading","Cook food","Fix the building","Drive the bus"], answer:0},
     {q:"A caretaker helps keep the school ___.", options:["clean and safe","closed","messy","noisy"], answer:0},
     {q:"Why is the school a community?", options:["People fight there","People work and learn together","No one helps each other","People live there"], answer:1},
     {q:"Who answers the phone and helps visitors in a school?", options:["The office staff","The librarian","The teacher","The caretaker"], answer:0}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"Language", title:"Letter Q", summary:"Explore uppercase and lowercase Q. Students identify the letter, practise its sound, and recognise that Q is almost always followed by U in English words.",
   resourceLabel:"YouTube: Letter Q", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20Q%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=L987a64I2cY",
   quiz:[
     {q:"What sound does Q make?", options:["Sh","Kw","Zh","Th"], answer:1},
     {q:"Q is almost always followed by ___.", options:["E","U","A","O"], answer:1},
     {q:"Which word starts with Q?", options:["Quick","Both B and C","Queen","King"], answer:1},
     {q:"A word that means silent and peaceful starts with Q. It is ___.", options:["Quiet","Quick","Quite","Quiz"], answer:0},
     {q:"Which Q word describes something fast?", options:["Quick","Quiet","Queen","Quarter"], answer:0}
   ]},
  {subject:"Math", title:"Sorting by Size and Colour", summary:"Students sort collections by size (big/small) and colour. They explain their sorting rule.",
   resourceLabel:"YouTube: Sorting by Size and Colour", resourceUrl:"https://www.youtube.com/results?search_query=Sorting%20by%20Size%20and%20Colour%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=8kcbajwxEfE",
   quiz:[
     {q:"When you sort by size, you group objects that are ___.", options:["the same colour","the same shape","the same weight","the same size"], answer:3},
     {q:"Which sorting rule is used if all red things are together?", options:["Colour","Shape","Weight","Size"], answer:0},
     {q:"You can sort the same set of objects in ___ ways.", options:["only one","many different","only two","no"], answer:1},
     {q:"What is the sorting rule if you put triangles together?", options:["Size","Number","Shape","Colour"], answer:2},
     {q:"You have 3 big blocks and 5 small blocks. How many blocks in all?", options:["5","3","8","7"], answer:2}
   ]},
  {subject:"Science", title:"Sinking and Floating", summary:"Students predict and test whether objects sink or float in water, discovering that shape and material affect floating.",
   resourceLabel:"YouTube: Sinking and Floating", resourceUrl:"https://www.youtube.com/results?search_query=Sinking%20and%20Floating%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=vo_uzrSzY9k",
   quiz:[
     {q:"An object that stays on top of water ___.", options:["floats","disappears","sinks","dissolves"], answer:0},
     {q:"An object that goes to the bottom of water ___.", options:["floats","melts","dissolves","sinks"], answer:3},
     {q:"A wooden stick will most likely ___.", options:["explode","sink","dissolve","float"], answer:3},
     {q:"A heavy metal coin will most likely ___.", options:["sink","float","dissolve","fly"], answer:0},
     {q:"What can change whether something floats?", options:["Its shape and the material it is made of","Nothing","Only its colour","Only its colour and smell"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Needs and Wants", summary:"Students learn to distinguish between needs (things necessary to survive) and wants (things we desire but do not need).",
   resourceLabel:"YouTube: Needs and Wants", resourceUrl:"https://www.youtube.com/results?search_query=Needs%20and%20Wants%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=aRcXutXvfmM",
   quiz:[
     {q:"A need is something you ___ to survive.", options:["must have","choose","want","enjoy"], answer:0},
     {q:"A want is something you ___ to survive.", options:["must have","cannot live without","must buy","do not need"], answer:3},
     {q:"Which is a NEED?", options:["A video game","Clean water","A bicycle","A toy car"], answer:1},
     {q:"Which is a WANT?", options:["Food","Clothing","Shelter","A new book bag"], answer:3},
     {q:"Why is it important to know the difference between needs and wants?", options:["Only adults need to know","Wants are always wrong","It is not important","It helps you make good choices with money and resources"], answer:3}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"Language", title:"Letter R", summary:"Explore uppercase and lowercase R. Students identify the letter, practise its /r/ sound, and name words beginning with R such as rabbit, rain, and rainbow.",
   resourceLabel:"YouTube: Letter R", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20R%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=aC_0vQRQe-s",
   quiz:[
     {q:"Which word starts with R?", options:["Cake","Rain","Dog","Ball"], answer:1},
     {q:"What sound does R make?", options:["Nuh","Ruh","Luh","Wuh"], answer:1},
     {q:"Which animal starts with R?", options:["Dog","Cat","Rabbit","Bear"], answer:2},
     {q:"Find the R word: The ___ is falling from the sky.", options:["Moon","Sun","Wind","Rain"], answer:3},
     {q:"Which colour starts with R?", options:["Blue","Purple","Green","Red"], answer:3}
   ]},
  {subject:"Math", title:"Patterns: ABAB and AABB", summary:"Students identify, copy, extend, and create repeating patterns using objects, sounds, and actions.",
   resourceLabel:"YouTube: Patterns: ABAB and AABB", resourceUrl:"https://www.youtube.com/results?search_query=Patterns%3A%20ABAB%20and%20AABB%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Js45cR_7wFE",
   quiz:[
     {q:"In an ABAB pattern, what comes after A?", options:["A","C","B","D"], answer:2},
     {q:"What comes next? Red, Blue, Red, Blue, ___", options:["Yellow","Green","Purple","Red"], answer:3},
     {q:"What is the pattern rule for: circle, circle, square, circle, circle, square?", options:["ABAB","AAAB","ABBA","AABB"], answer:3},
     {q:"What comes next? 1, 2, 1, 2, ___", options:["4","3","1","2"], answer:2},
     {q:"Creating a pattern means you ___.", options:["count to 10","repeat a rule over and over","make a random pile","mix things randomly"], answer:1}
   ]},
  {subject:"Science", title:"Living Things: Animals", summary:"Students explore characteristics of animals. All animals move, eat, grow, and produce offspring. They are sorted by habitat and diet.",
   resourceLabel:"YouTube: Living Things: Animals", resourceUrl:"https://www.youtube.com/results?search_query=Living%20Things%3A%20Animals%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Gy60BqCnTG4",
   quiz:[
     {q:"All animals ___.", options:["can fly","make their own food from sunlight","eat other organisms to get energy","live in water"], answer:2},
     {q:"An animal that eats only plants is a ___.", options:["herbivore","omnivore","carnivore","decomposer"], answer:0},
     {q:"An animal that eats only meat is a ___.", options:["omnivore","herbivore","producer","carnivore"], answer:3},
     {q:"A bear that eats both plants and fish is an ___.", options:["herbivore","insectivore","carnivore","omnivore"], answer:3},
     {q:"Which is a characteristic all animals share?", options:["They all have fur","They all breathe","They all swim","They all fly"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Our Neighbourhood", summary:"Students explore their neighbourhood as a community with homes, parks, stores, schools, and community services close together.",
   resourceLabel:"YouTube: Our Neighbourhood", resourceUrl:"https://www.youtube.com/results?search_query=Our%20Neighbourhood%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=iwxkwPA8c68",
   quiz:[
     {q:"A neighbourhood is a ___.", options:["planet","small area where people live close together","country","city"], answer:1},
     {q:"Which place would you find in a neighbourhood?", options:["An ocean","A desert","A mountain range","A park or playground"], answer:3},
     {q:"What makes a neighbourhood a community?", options:["People sharing the same area and looking out for each other","Only the houses","The buildings","Only the stores"], answer:0},
     {q:"A map of a neighbourhood shows ___.", options:["only oceans","only mountains","where places like homes, schools, and parks are located","only countries"], answer:2},
     {q:"Why are parks important in a neighbourhood?", options:["They are not","Only children use them","They give people a place to play, relax, and connect with nature","Only for sports"], answer:2}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"Language", title:"Letter S", summary:"Explore uppercase and lowercase S. Students identify the letter, practise its /s/ sound, and name S words such as sun, snake, and star.",
   resourceLabel:"YouTube: Letter S", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20S%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=uSVzk2pqWB4",
   quiz:[
     {q:"Which word starts with S?", options:["Run","Sun","Hat","Bat"], answer:1},
     {q:"What sound does S make?", options:["Sss","Tss","Zzz","Shh"], answer:0},
     {q:"Find the S word: The ___ shines in the sky.", options:["Rain","Cloud","Sun","Moon"], answer:2},
     {q:"Which animal starts with S?", options:["Bird","Snake","Cat","Dog"], answer:1},
     {q:"How many S words: sun, moon, star, sky, cloud?", options:["3","2","1","4"], answer:0}
   ]},
  {subject:"Math", title:"Addition to 10", summary:"Students add two groups of objects to find the total. They use pictures, counters, and number lines to explore addition.",
   resourceLabel:"YouTube: Addition to 10", resourceUrl:"https://www.youtube.com/results?search_query=Addition%20to%2010%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=mjlsSYLLOSE",
   quiz:[
     {q:"3 + 4 = ?", options:["6","8","7","5"], answer:2},
     {q:"How many in all: 2 apples + 5 apples?", options:["8","6","7","3"], answer:2},
     {q:"5 + 5 = ?", options:["11","9","10","8"], answer:2},
     {q:"What does the + sign mean?", options:["Divide","Take away","Compare","Put together / add"], answer:3},
     {q:"1 + 9 = ?", options:["11","10","9","8"], answer:1}
   ]},
  {subject:"Science", title:"The Sun and Sky", summary:"Students explore the Sun as Earth's main source of light and heat. They observe that the sky changes from day to night.",
   resourceLabel:"YouTube: The Sun and Sky", resourceUrl:"https://www.youtube.com/results?search_query=The%20Sun%20and%20Sky%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=sePqPIXMsAc",
   quiz:[
     {q:"The Sun gives Earth ___ and ___.", options:["cold and dark","rain and wind","light and heat","snow and ice"], answer:2},
     {q:"The Sun is a ___.", options:["moon","planet","star","comet"], answer:2},
     {q:"During the day, the Sun is ___ in the sky.", options:["visible (we can see it when skies are clear)","invisible","underground","on the horizon only"], answer:0},
     {q:"At night, the Sun ___.", options:["gets smaller","is still in the sky in the same place","disappears forever","has moved to the other side of Earth (appears to set)"], answer:3},
     {q:"Why should you never look directly at the Sun?", options:["Its light can damage your eyes","It is invisible","It is too cold","It is dark"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Canadian Symbols", summary:"Students learn about symbols that represent Canada: the maple leaf, beaver, Canadian flag, Parliament Buildings, and the national anthem.",
   resourceLabel:"YouTube: Canadian Symbols", resourceUrl:"https://www.youtube.com/results?search_query=Canadian%20Symbols%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=38BGXJ572Y8",
   quiz:[
     {q:"What is Canada's national symbol on the flag?", options:["Moose","Rose","Maple leaf","Beaver"], answer:2},
     {q:"The beaver is a Canadian symbol of ___.", options:["sport","beauty","hard work and industry","danger"], answer:2},
     {q:"Canada's national anthem is called ___.", options:["Amazing Grace","The Star-Spangled Banner","O Canada","God Save the King"], answer:2},
     {q:"Where does Canada's federal government meet?", options:["The CN Tower","Parliament Hill","Niagara Falls","The Rockies"], answer:1},
     {q:"The colours of the Canadian flag are ___.", options:["Red, white, and blue","Blue and white","Red and white","Green and gold"], answer:2}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"Language", title:"Letter T", summary:"Explore uppercase and lowercase T. Students identify the letter, practise its /t/ sound, and name T words such as tiger, table, and turtle.",
   resourceLabel:"YouTube: Letter T", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20T%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=HHEqOLZ0hr4",
   quiz:[
     {q:"Which word starts with T?", options:["Fish","Cat","Dog","Tiger"], answer:3},
     {q:"What sound does T make?", options:["Tuh","Duh","Kuh","Buh"], answer:0},
     {q:"Find the T word: I sit at a ___ to eat.", options:["Chair","Bench","Table","Desk"], answer:2},
     {q:"Which colour starts with T?", options:["Red","Green","Teal","Blue"], answer:2},
     {q:"How many T words: tree, flower, turtle, table, apple?", options:["1","4","3","2"], answer:2}
   ]},
  {subject:"Math", title:"Subtraction from 10", summary:"Students subtract within 10 using objects, pictures, and number lines. They understand subtraction as taking away.",
   resourceLabel:"YouTube: Subtraction from 10", resourceUrl:"https://www.youtube.com/results?search_query=Subtraction%20from%2010%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=ba7KtARU0UI",
   quiz:[
     {q:"10 - 3 = ?", options:["7","8","9","6"], answer:0},
     {q:"8 - 5 = ?", options:["5","4","2","3"], answer:3},
     {q:"What does the - sign mean?", options:["Take away","Share","Add","Put together"], answer:0},
     {q:"7 - 7 = ?", options:["0","7","1","14"], answer:0},
     {q:"6 - 2 = ?", options:["5","4","3","2"], answer:1}
   ]},
  {subject:"Science", title:"Air and Wind", summary:"Students explore air as a real substance that takes up space, and that moving air is called wind. Wind can be gentle or strong.",
   resourceLabel:"YouTube: Air and Wind", resourceUrl:"https://www.youtube.com/results?search_query=Air%20and%20Wind%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=A02GNVy115E",
   quiz:[
     {q:"Moving air is called ___.", options:["Snow","Wind","Clouds","Rain"], answer:1},
     {q:"Air takes up ___.", options:["only hot space","no space","space (even if we cannot see it)","only a little space"], answer:2},
     {q:"A gentle breeze and a storm are both caused by ___.", options:["the sun heating the ground evenly","no movement","moving air (wind)","rain"], answer:2},
     {q:"Which tool measures wind speed?", options:["Scale","Thermometer","Ruler","Anemometer"], answer:3},
     {q:"What can wind do?", options:["Nothing","Only feel cold","Move leaves, fly kites, and power windmills","Only dry laundry"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Feelings and Emotions", summary:"Students explore a range of emotions and learn healthy ways to express feelings and manage emotions in social situations.",
   resourceLabel:"YouTube: Feelings and Emotions", resourceUrl:"https://www.youtube.com/results?search_query=Feelings%20and%20Emotions%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=jetoWelJJJk",
   quiz:[
     {q:"A feeling that makes you smile and feel happy inside is ___.", options:["joy","fear","anger","sadness"], answer:0},
     {q:"When you feel angry, a healthy response is to ___.", options:["take deep breaths and talk about it","hit someone","yell loudly","ignore it forever"], answer:0},
     {q:"Why is it important to talk about your feelings?", options:["Feelings should always be hidden","It helps others understand you and helps you feel better","Only adults talk about feelings","It is not"], answer:1},
     {q:"If a friend is sad, you could ___.", options:["ignore them","run away","ask if they are okay and listen","laugh at them"], answer:2},
     {q:"Being kind to someone who is upset is called ___.", options:["competing","ignoring","arguing","empathy"], answer:3}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"Language", title:"Letter U", summary:"Explore uppercase and lowercase U. Students identify the letter, practise its short /u/ sound (umbrella) and long /u/ sound (uniform), and find U words.",
   resourceLabel:"YouTube: Letter U", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20U%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=IF59Xs60uRM",
   quiz:[
     {q:"Which word starts with U?", options:["Apple","Egg","Ice","Umbrella"], answer:3},
     {q:"The short U sound is heard in ___.", options:["Cube","Unite","Use","Umbrella"], answer:3},
     {q:"Which U word means something you wear?", options:["Upper","Undo","Under","Uniform"], answer:3},
     {q:"U is a ___.", options:["consonant","vowel","colour","number"], answer:1},
     {q:"Find the U: apple, umbrella, orange, egg", options:["orange","egg","umbrella","apple"], answer:2}
   ]},
  {subject:"Math", title:"Graphs: Bar Graphs", summary:"Students create and read simple picture and bar graphs. They answer questions about the data shown.",
   resourceLabel:"YouTube: Graphs: Bar Graphs", resourceUrl:"https://www.youtube.com/results?search_query=Graphs%3A%20Bar%20Graphs%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=zF_dBk8EPDk",
   quiz:[
     {q:"A bar graph uses ___ to show information.", options:["colours only","only numbers","bars (rectangles) of different heights","circles"], answer:2},
     {q:"The tallest bar in a bar graph shows the ___ amount.", options:["smallest","same","unknown","largest"], answer:3},
     {q:"What question does a graph help answer?", options:["How heavy is something?","What colour is something?","How does something smell?","How many of each thing are there?"], answer:3},
     {q:"If 5 kids chose pizza and 3 chose pasta, which bar is taller?", options:["They are equal","Cannot tell","Pizza","Pasta"], answer:2},
     {q:"The title of a graph tells you ___.", options:["what the graph is about","the colours used","how many bars there are","the exact numbers"], answer:0}
   ]},
  {subject:"Science", title:"Day and Night", summary:"Students explore why we have day and night — Earth rotates on its axis, causing each side to face toward or away from the Sun.",
   resourceLabel:"YouTube: Day and Night", resourceUrl:"https://www.youtube.com/results?search_query=Day%20and%20Night%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Wr-CRKsTYGs",
   quiz:[
     {q:"Day and night are caused by ___.", options:["clouds covering the Sun","the Sun moving around Earth","Earth rotating (spinning) on its axis","the Moon moving"], answer:2},
     {q:"When your part of Earth faces the Sun, it is ___.", options:["night","day","cold","raining"], answer:1},
     {q:"One full rotation of Earth takes about ___.", options:["1 year","24 hours (1 day)","1 month","1 hour"], answer:1},
     {q:"At night, the Sun ___.", options:["is shining on the other side of Earth","disappears","is visible in the sky","gets cold"], answer:0},
     {q:"The Moon is best seen at ___.", options:["sunrise only","nighttime","daytime","noon"], answer:1}
   ]},
  {subject:"SocialStudies", title:"Friends and Kindness", summary:"Students explore what makes a good friend and practise acts of kindness. They discuss how kind actions make communities happier.",
   resourceLabel:"YouTube: Friends and Kindness", resourceUrl:"https://www.youtube.com/results?search_query=Friends%20and%20Kindness%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=BNNcpAcF0GM",
   quiz:[
     {q:"A good friend ___.", options:["ignores your feelings","is kind, listens, and includes others","always agrees","only plays with you if you have toys"], answer:1},
     {q:"Kindness means ___.", options:["ignoring others","only sharing food","saying and doing things that make others feel valued","always winning"], answer:2},
     {q:"If a classmate has no one to play with, you could ___.", options:["laugh at them","invite them to join your game","tell them to find others","ignore them"], answer:1},
     {q:"Why is kindness important in a community?", options:["It makes everyone feel welcome and valued","It is not","Only kind people deserve it","Only some people need kindness"], answer:0},
     {q:"Which is an act of kindness?", options:["Laughing at a mistake","Pushing in line","Holding the door open for someone","Taking someone's pencil"], answer:2}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"Language", title:"Letter V", summary:"Explore uppercase and lowercase V. Students identify the letter, practise its /v/ sound, and name V words such as van, vest, and vegetables.",
   resourceLabel:"YouTube: Letter V", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20V%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=yZjEtwr8Q4o",
   quiz:[
     {q:"Which word starts with V?", options:["Van","Door","Cat","Ball"], answer:0},
     {q:"What sound does V make?", options:["Buh","Wuh","Vvv","Fuh"], answer:2},
     {q:"Find the V word: carrots and ___ are good for you.", options:["Candy","Chips","Vegetables","Cookies"], answer:2},
     {q:"Which V word is a type of clothing?", options:["Van","Vine","Vest","Vase"], answer:2},
     {q:"How many V words: van, vase, apple, vine, umbrella?", options:["4","3","2","5"], answer:1}
   ]},
  {subject:"Math", title:"2D Shapes Review", summary:"Students review circles, squares, triangles, and rectangles. They identify, describe, and sort shapes by their properties.",
   resourceLabel:"YouTube: 2D Shapes Review", resourceUrl:"https://www.youtube.com/results?search_query=2D%20Shapes%20Review%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=Ux_kLd7qAcY",
   quiz:[
     {q:"A circle has ___ corners.", options:["4","2","0","1"], answer:2},
     {q:"A square has ___ equal sides.", options:["3","5","2","4"], answer:3},
     {q:"A triangle has ___ sides.", options:["3","2","5","4"], answer:0},
     {q:"Which shape has 4 sides but they are not all equal?", options:["Circle","Square","Rectangle","Triangle"], answer:2},
     {q:"A shape with no straight sides and no corners is a ___.", options:["triangle","rectangle","square","circle"], answer:3}
   ]},
  {subject:"Science", title:"Plants Need Water and Light", summary:"Students investigate what happens to plants without water or light, reinforcing that plants need both to grow.",
   resourceLabel:"YouTube: Plants Need Water and Light", resourceUrl:"https://www.youtube.com/results?search_query=Plants%20Need%20Water%20and%20Light%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=u46A0WKp2nk",
   quiz:[
     {q:"Plants need ___ and ___ to grow.", options:["sand and wind","ice and darkness","water and sunlight","mud and shade"], answer:2},
     {q:"What would most likely happen to a plant with no water?", options:["It stays the same","It wilts and eventually dies","It glows","It grows faster"], answer:1},
     {q:"Leaves face toward light because ___.", options:["they are afraid of the dark","roots need light","plants use sunlight to make food (photosynthesis)","leaves like warmth only"], answer:2},
     {q:"Which part of a plant absorbs water from the soil?", options:["Leaves","Roots","Flowers","Stem"], answer:1},
     {q:"Plants make their food using ___.", options:["only air","only water","sunlight, water, and carbon dioxide","soil alone"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Helping at Home", summary:"Students explore how family members share responsibilities at home: cooking, cleaning, caring for younger siblings, and yard work.",
   resourceLabel:"YouTube: Helping at Home", resourceUrl:"https://www.youtube.com/results?search_query=Helping%20at%20Home%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=lGC0zxgRNJQ",
   quiz:[
     {q:"Responsibilities at home are ___.", options:["optional extras","only chores for children","only for adults","tasks that all family members share to keep the home running well"], answer:3},
     {q:"Which is an example of helping at home?", options:["Cleaning up after yourself","Watching TV all day","Eating all the snacks","Leaving your toys everywhere"], answer:0},
     {q:"Why is it important to share home responsibilities?", options:["It teaches children to be responsible and helps the family work as a team","Only if parents ask","Only adults should work","It is not"], answer:0},
     {q:"A chore is ___.", options:["a job you do at home to help the family","a type of game","a type of food","a school subject"], answer:0},
     {q:"Which chore could a kindergartener do?", options:["Fix the roof","Pay the bills","Put toys away and help set the table","Drive to the store"], answer:2}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"Language", title:"Letter W", summary:"Explore uppercase and lowercase W. Students identify the letter, practise its /w/ sound, and name W words such as water, whale, and winter.",
   resourceLabel:"YouTube: Letter W", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20W%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=jxBDGPvZPi0",
   quiz:[
     {q:"Which word starts with W?", options:["Water","Rain","Snow","Ice"], answer:0},
     {q:"What sound does W make?", options:["Buh","Vvv","Muh","Wuh"], answer:3},
     {q:"Find the W: spring, summer, ___, fall", options:["Autumn","Winter","Rainy","Cold"], answer:1},
     {q:"Which W word is a large ocean animal?", options:["Wasp","Whale","Worm","Wolf"], answer:1},
     {q:"How many W words: well, wall, ball, walk, tall?", options:["3","4","2","1"], answer:0}
   ]},
  {subject:"Math", title:"Measurement: Length", summary:"Students use non-standard units (paper clips, blocks) to measure and compare the length of objects. They use terms: longer, shorter, same.",
   resourceLabel:"YouTube: Measurement: Length", resourceUrl:"https://www.youtube.com/results?search_query=Measurement%3A%20Length%20kindergarten%20educational",
   videoUrl:"https://www.youtube.com/watch?v=2wUsdsae0ro",
   quiz:[
     {q:"Measurement tells you ___.", options:["how hot something is","the colour of something","what something smells like","how long, tall, or heavy something is"], answer:3},
     {q:"If you measure a pencil with paper clips, you are using a ___.", options:["non-standard unit","ruler","standard unit","metre stick"], answer:0},
     {q:"Which statement about length is correct?", options:["Shorter means bigger","All things are the same length","Longer means shorter","Longer means it takes up more space from end to end"], answer:3},
     {q:"To compare two lengths, you should ___.", options:["smell them","guess","use a scale","line them up at the same starting point"], answer:3},
     {q:"A book is 8 paper clips long. A pencil is 5 paper clips long. The book is ___.", options:["longer","shorter","impossible to compare","the same length"], answer:0}
   ]},
  {subject:"Science", title:"Animals in Winter", summary:"Students learn how animals survive winter: some hibernate, some migrate south, and some stay active by adapting their behaviour.",
   resourceLabel:"YouTube: Animals in Winter", resourceUrl:"https://www.youtube.com/results?search_query=Animals%20in%20Winter%20kindergarten%20educational",
   quiz:[
     {q:"Hibernation means ___.", options:["building a nest","growing a thicker coat","flying south for winter","sleeping deeply through winter to save energy"], answer:3},
     {q:"Which animal is known for hibernating in winter?", options:["Butterfly","Robin","Bear","Goose"], answer:2},
     {q:"Migration means ___.", options:["growing thicker fur","travelling to a warmer place for winter","sleeping through winter","staying and being active"], answer:1},
     {q:"Which bird migrates south in autumn?", options:["Canada Goose","Owl","Crow","Chickadee"], answer:0},
     {q:"Some animals grow thicker fur in winter to ___.", options:["swim better","find food faster","keep warm","look better"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Weather and Our Lives", summary:"Students explore how weather affects daily decisions: what to wear, what activities to do, and how communities prepare for extreme weather.",
   resourceLabel:"YouTube: Weather and Our Lives", resourceUrl:"https://www.youtube.com/results?search_query=Weather%20and%20Our%20Lives%20kindergarten%20educational",
   quiz:[
     {q:"Weather affects what we ___.", options:["read","eat for breakfast","wear and what activities we do","dream about"], answer:2},
     {q:"On a rainy day you would wear ___.", options:["a t-shirt and shorts","a raincoat and boots","nothing different","a swimsuit"], answer:1},
     {q:"Extreme weather like a blizzard can ___.", options:["cause school closures and road dangers","only affect farms","have no impact","only affect the sky"], answer:0},
     {q:"A weather forecast helps people ___.", options:["make it rain","plan and prepare for upcoming weather","control the weather","predict the future"], answer:1},
     {q:"Which job involves predicting the weather?", options:["Librarian","Plumber","Meteorologist","Baker"], answer:2}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"Language", title:"Letter X", summary:"Explore uppercase and lowercase X. Students identify the letter, practise its /ks/ sound, and note that X rarely starts words in English.",
   resourceLabel:"YouTube: Letter X", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20X%20kindergarten%20educational",
   quiz:[
     {q:"What sound does X usually make?", options:["Zuh","Tuh","Ks (as in fox)","Sh"], answer:2},
     {q:"X is found at the ___ of most English words.", options:["never","beginning","only at the start","middle or end"], answer:3},
     {q:"Which word has an X?", options:["Dog","Bird","Cat","Fox"], answer:3},
     {q:"An X on a map often marks ___.", options:["water","a road","mountains","a special or buried location"], answer:3},
     {q:"Which word ends in X?", options:["Bat","Ball","Box","Bag"], answer:2}
   ]},
  {subject:"Math", title:"Measurement: Capacity", summary:"Students compare the capacity (how much a container holds) using non-standard units. They use terms: more, less, same.",
   resourceLabel:"YouTube: Measurement: Capacity", resourceUrl:"https://www.youtube.com/results?search_query=Measurement%3A%20Capacity%20kindergarten%20educational",
   quiz:[
     {q:"Capacity means ___.", options:["how long something is","how hot something is","how heavy something is","how much a container can hold"], answer:3},
     {q:"A bucket holds ___ water than a cup.", options:["the same","less","more","no"], answer:2},
     {q:"If you fill a small jar and a big jar with water, the big jar holds ___.", options:["the same","less","nothing","more"], answer:3},
     {q:"To compare capacity you could ___.", options:["count the containers","smell them","fill each with water and compare","weigh the containers"], answer:2},
     {q:"Which holds the most: a teaspoon, a cup, or a pot?", options:["They are all equal","Pot","Teaspoon","Cup"], answer:1}
   ]},
  {subject:"Science", title:"Properties of Water", summary:"Students explore water as a liquid that takes the shape of its container, that it freezes into solid ice and evaporates into invisible vapour.",
   resourceLabel:"YouTube: Properties of Water", resourceUrl:"https://www.youtube.com/results?search_query=Properties%20of%20Water%20kindergarten%20educational",
   quiz:[
     {q:"Water is a ___.", options:["solid","powder","liquid at room temperature","gas"], answer:2},
     {q:"When water freezes it becomes ___.", options:["solid ice","liquid","gas","vapour"], answer:0},
     {q:"When water evaporates it becomes ___.", options:["heavier","coloured","solid","invisible water vapour (gas)"], answer:3},
     {q:"Water takes the shape of ___.", options:["its original form only","its container","a flat sheet always","a ball always"], answer:1},
     {q:"Which temperature turns liquid water into ice?", options:["At 100°C","At 50°C","At 0°C (or below)","Above 0°C"], answer:2}
   ]},
  {subject:"SocialStudies", title:"My Country: Canada", summary:"Students explore Canada as their country: its size, capital city, official languages, and symbols that make it unique.",
   resourceLabel:"YouTube: My Country: Canada", resourceUrl:"https://www.youtube.com/results?search_query=My%20Country%3A%20Canada%20kindergarten%20educational",
   quiz:[
     {q:"Canada is located in ___.", options:["Africa","Europe","South America","North America"], answer:3},
     {q:"Canada's capital city is ___.", options:["Vancouver","Ottawa","Montreal","Toronto"], answer:1},
     {q:"Canada has ___ official languages.", options:["1","4","3","2"], answer:3},
     {q:"What are Canada's official languages?", options:["English and Chinese","Spanish and English","Italian and French","French and English"], answer:3},
     {q:"Canada is the ___ largest country in the world by area.", options:["3rd","1st","2nd","5th"], answer:2}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"Language", title:"Letter Y", summary:"Explore uppercase and lowercase Y. Students identify the letter, practise its /y/ sound, and name Y words such as yak, yarn, and yes.",
   resourceLabel:"YouTube: Letter Y", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20Y%20kindergarten%20educational",
   quiz:[
     {q:"Which word starts with Y?", options:["Zoo","Yak","Ant","Fox"], answer:1},
     {q:"What sound does Y make at the start of a word?", options:["Wuh","Juh","Iuh","Yuh"], answer:3},
     {q:"Find the Y: The answer is ___, not no.", options:["No","Yes","Maybe","Perhaps"], answer:1},
     {q:"Which Y word is something you knit with?", options:["Year","Yarn","Yam","Yard"], answer:1},
     {q:"How many Y words: yes, year, no, yesterday, red?", options:["2","1","3","4"], answer:0}
   ]},
  {subject:"Math", title:"Numbers to 20: Addition and Subtraction", summary:"Students add and subtract within 20 using number lines, counters, and mental strategies.",
   resourceLabel:"YouTube: Numbers to 20: Addition and Subtraction", resourceUrl:"https://www.youtube.com/results?search_query=Numbers%20to%2020%3A%20Addition%20and%20Subtraction%20kindergarten%20educational",
   quiz:[
     {q:"12 + 5 = ?", options:["18","16","17","15"], answer:2},
     {q:"18 - 4 = ?", options:["12","15","14","13"], answer:2},
     {q:"What is 10 + 7?", options:["17","15","16","18"], answer:0},
     {q:"20 - 9 = ?", options:["10","12","13","11"], answer:3},
     {q:"A number line helps you ___.", options:["add and subtract by counting forward and backward","measure temperature","find shapes","measure weight"], answer:0}
   ]},
  {subject:"Science", title:"Insects", summary:"Students explore characteristics of insects: 6 legs, 3 body parts (head, thorax, abdomen), and often wings. Common Ontario insects are identified.",
   resourceLabel:"YouTube: Insects", resourceUrl:"https://www.youtube.com/results?search_query=Insects%20kindergarten%20educational",
   quiz:[
     {q:"All insects have ___ legs.", options:["10","8","4","6"], answer:3},
     {q:"The three body parts of an insect are head, thorax, and ___.", options:["abdomen","tail","shell","wing"], answer:0},
     {q:"Which is an insect?", options:["Worm","Spider","Butterfly","Centipede"], answer:2},
     {q:"A spider is NOT an insect because it has ___ legs.", options:["6","10","4","8"], answer:3},
     {q:"Which Ontario insect is known for its orange and black wings?", options:["Monarch butterfly","Dragonfly","Bumblebee","Firefly"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Exploring Our Differences and Similarities", summary:"Students celebrate diversity by exploring how people are alike and different in appearance, language, food, and traditions.",
   resourceLabel:"YouTube: Exploring Our Differences and Similarities", resourceUrl:"https://www.youtube.com/results?search_query=Exploring%20Our%20Differences%20and%20Similarities%20kindergarten%20educational",
   quiz:[
     {q:"People from different cultures may have different ___.", options:["Only names","Only language","Languages, foods, celebrations, and traditions","Only food"], answer:2},
     {q:"Celebrating our differences helps us ___.", options:["learn from and respect each other","feel confused","stay separate","fight more"], answer:0},
     {q:"Which is a way people are similar across all cultures?", options:["They all speak English","They all eat the same food","They all have families, feelings, and a need to belong","They all look the same"], answer:2},
     {q:"Diversity in a classroom means ___.", options:["students come from different backgrounds and experiences","only one culture is represented","everyone is the same","everyone has the exact same background"], answer:0},
     {q:"Why is it important to learn about other cultures?", options:["It builds empathy and understanding","Only for adults","Only for geography class","It is not"], answer:0}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"Language", title:"Letter Z", summary:"Explore uppercase and lowercase Z. Students identify the letter, practise its /z/ sound, and name Z words such as zebra, zero, and zip.",
   resourceLabel:"YouTube: Letter Z", resourceUrl:"https://www.youtube.com/results?search_query=Letter%20Z%20kindergarten%20educational",
   quiz:[
     {q:"Which word starts with Z?", options:["Dog","Animal","Bee","Zebra"], answer:3},
     {q:"What sound does Z make?", options:["Tuh","Shh","Zzz","Sss"], answer:2},
     {q:"Find the Z: The number that means nothing is ___.", options:["One","Zero","Two","Ten"], answer:1},
     {q:"Which Z word is a striped animal?", options:["Zap","Zone","Zip","Zebra"], answer:3},
     {q:"Z is the ___ letter of the English alphabet.", options:["26th","13th","25th","1st"], answer:0}
   ]},
  {subject:"Math", title:"Sorting 3D Shapes", summary:"Students identify and sort 3D shapes: sphere, cube, cylinder, and cone. They describe them using faces, edges, and vertices.",
   resourceLabel:"YouTube: Sorting 3D Shapes", resourceUrl:"https://www.youtube.com/results?search_query=Sorting%203D%20Shapes%20kindergarten%20educational",
   quiz:[
     {q:"A sphere looks like ___.", options:["a can","a cone","a box","a ball"], answer:3},
     {q:"A cube has ___ flat faces.", options:["4","8","5","6"], answer:3},
     {q:"A cylinder has ___ flat circular faces.", options:["0","2","1","3"], answer:1},
     {q:"Which 3D shape comes to a point at the top?", options:["Cone","Cylinder","Sphere","Cube"], answer:0},
     {q:"Which 3D shape can roll?", options:["Cone and sphere","Only sphere","Rectangle","Cube"], answer:0}
   ]},
  {subject:"Science", title:"Taking Care of Our Environment", summary:"Students learn about littering and waste, and simple actions to protect the environment: picking up litter, reducing waste, and recycling.",
   resourceLabel:"YouTube: Taking Care of Our Environment", resourceUrl:"https://www.youtube.com/results?search_query=Taking%20Care%20of%20Our%20Environment%20kindergarten%20educational",
   quiz:[
     {q:"Litter means ___.", options:["a bed for kittens only","recycled material","waste thrown on the ground instead of in a bin","a type of animal home"], answer:2},
     {q:"Recycling means ___.", options:["ignoring waste","using objects again or making them into new things","throwing everything away","burning waste"], answer:1},
     {q:"Which action helps the environment?", options:["Leaving garbage in a park","Wasting water","Picking up litter","Leaving lights on all night"], answer:2},
     {q:"The three Rs are Reduce, Reuse, and ___.", options:["Rotate","Refuse","Reach","Recycle"], answer:3},
     {q:"Why is it important to look after the environment?", options:["We share the planet with all living things and must keep it healthy","Only for adults","Only scientists care","It is not"], answer:0}
   ]},
  {subject:"SocialStudies", title:"All About Me: Reflection", summary:"Students reflect on their learning through the year, identifying what they have learned, how they have grown, and what they are proud of.",
   resourceLabel:"YouTube: All About Me: Reflection", resourceUrl:"https://www.youtube.com/results?search_query=All%20About%20Me%3A%20Reflection%20kindergarten%20educational",
   quiz:[
     {q:"Reflecting on your learning means ___.", options:["copying someone else","ignoring what happened","only thinking about bad things","thinking about what you learned and how you grew"], answer:3},
     {q:"I am most proud when ___.", options:["I try my best and do not give up","I do nothing","I copy others","I give up"], answer:0},
     {q:"Something new I learned this year is ___.", options:["Only my name","Only colours","Nothing","How to read new words, count higher, and learn about the world"], answer:3},
     {q:"A goal for next year could be ___.", options:["To do nothing new","To never make mistakes","To try something harder and keep learning","To stop reading"], answer:2},
     {q:"Learning is ___.", options:["only from teachers","only at school","only from books","something that happens everywhere and every day"], answer:3}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"Language", title:"Reading: Simple Sentences", summary:"Students read and understand simple sentences. They identify the naming part (who or what) and the action part (what they do).",
   resourceLabel:"YouTube: Reading: Simple Sentences", resourceUrl:"https://www.youtube.com/results?search_query=Reading%3A%20Simple%20Sentences%20kindergarten%20educational",
   quiz:[
     {q:"A sentence has a naming part and an ___ part.", options:["action","describing","eating","colouring"], answer:0},
     {q:"In 'The cat runs fast,' the naming part is ___.", options:["fast and runs","runs","The cat","fast"], answer:2},
     {q:"In 'The dog jumps high,' the action part is ___.", options:["The dog","jumps high","The","high"], answer:1},
     {q:"A complete sentence needs ___.", options:["only adjectives","a naming part (noun) and an action part (verb)","only a verb","only a noun"], answer:1},
     {q:"Which is a complete sentence?", options:["Jumping high quickly.","The bird sings.","Runs fast.","The big red."], answer:1}
   ]},
  {subject:"Math", title:"Counting Back: Subtraction", summary:"Students use counting back as a strategy for subtraction within 20.",
   resourceLabel:"YouTube: Counting Back: Subtraction", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20Back%3A%20Subtraction%20kindergarten%20educational",
   quiz:[
     {q:"To subtract 3 from 9, count back 3 from 9. Answer = ?", options:["5","7","8","6"], answer:3},
     {q:"10 - 4: count back 4 from 10. Answer = ?", options:["8","7","6","5"], answer:2},
     {q:"15 - 3 = ?", options:["13","11","10","12"], answer:3},
     {q:"Counting back means you count in which direction?", options:["Sideways","Forward (up)","Randomly","Backward (down)"], answer:3},
     {q:"Which strategy helps with subtraction?", options:["Multiplication","Dividing","Counting back from the starting number","Adding more"], answer:2}
   ]},
  {subject:"Science", title:"Materials Around Us", summary:"Students explore everyday materials (wood, plastic, metal, fabric, glass) and their properties such as hard, soft, bendy, and transparent.",
   resourceLabel:"YouTube: Materials Around Us", resourceUrl:"https://www.youtube.com/results?search_query=Materials%20Around%20Us%20kindergarten%20educational",
   quiz:[
     {q:"Wood is usually described as ___.", options:["transparent","hard and solid","liquid","soft and bendy"], answer:1},
     {q:"Which material lets light through (is transparent)?", options:["Fabric","Wood","Metal","Glass"], answer:3},
     {q:"Fabric is usually ___.", options:["liquid","soft and flexible","hard and rigid","transparent"], answer:1},
     {q:"Which material is a good conductor of electricity?", options:["Wood","Glass","Rubber","Metal"], answer:3},
     {q:"We choose materials based on their ___.", options:["properties (what they are like and what they can do)","weight only","colour only","size only"], answer:0}
   ]},
  {subject:"SocialStudies", title:"Special Days and Celebrations", summary:"Students explore special days celebrated in their community and around the world, recognising that different cultures celebrate in unique ways.",
   resourceLabel:"YouTube: Special Days and Celebrations", resourceUrl:"https://www.youtube.com/results?search_query=Special%20Days%20and%20Celebrations%20kindergarten%20educational",
   quiz:[
     {q:"A celebration is ___.", options:["a special occasion that people mark with activities","a type of building","a type of food","a school subject"], answer:0},
     {q:"Which is a Canadian celebration?", options:["Canada Day (July 1)","Chinese New Year","Eid al-Fitr (Islamic)","Diwali (Hindu/Sikh)"], answer:0},
     {q:"Why do different cultures celebrate differently?", options:["All celebrations are the same","Only one way is correct","Each culture has unique traditions, histories, and values that shape its celebrations","They do not"], answer:2},
     {q:"Learning about others' celebrations helps us ___.", options:["ignore diversity","stay only with our own culture","feel confused","respect and appreciate different cultures"], answer:3},
     {q:"What is Diwali known as?", options:["Festival of Lights","Festival of Music","Festival of Food","Festival of Colour"], answer:0}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"Language", title:"Writing: My Favourite Thing", summary:"Students practise simple sentence writing about a personal favourite topic, using a capital letter, words, and a period.",
   resourceLabel:"YouTube: Writing: My Favourite Thing", resourceUrl:"https://www.youtube.com/results?search_query=Writing%3A%20My%20Favourite%20Thing%20kindergarten%20educational",
   quiz:[
     {q:"A sentence starts with a ___ letter.", options:["capital (uppercase)","lowercase","number","random"], answer:0},
     {q:"A sentence ends with a ___.", options:["slash","comma","period, question mark, or exclamation mark","capital letter"], answer:2},
     {q:"Which is written correctly?", options:["my Dog is fluffy.","my dog is fluffy.","My dog is Fluffy","My dog is fluffy."], answer:3},
     {q:"When writing about your favourite thing, a good first sentence ___.", options:["tells what your favourite thing is and why you like it","lists random words","says nothing","asks a question with no answer"], answer:0},
     {q:"A picture can help your reader ___.", options:["understand your writing better","add more letters","erase your work","change your topic"], answer:0}
   ]},
  {subject:"Math", title:"Number Stories", summary:"Students create and solve simple addition and subtraction number stories using pictures and equations.",
   resourceLabel:"YouTube: Number Stories", resourceUrl:"https://www.youtube.com/results?search_query=Number%20Stories%20kindergarten%20educational",
   quiz:[
     {q:"A number story is ___.", options:["a book about numbers","a fairy tale","a maths problem described in words","only about counting"], answer:2},
     {q:"There are 3 birds on a branch. 2 more land. How many now?", options:["3","5","4","6"], answer:1},
     {q:"I had 7 cookies. I ate 3. How many are left?", options:["4","5","3","6"], answer:0},
     {q:"Which equation matches: 4 ducks plus 2 ducks?", options:["4 x 2 = 8","6 - 2 = 4","4 + 2 = 6","4 - 2 = 2"], answer:2},
     {q:"A number story always includes ___.", options:["only letters","a character, a problem, and a number answer","only a picture","only an equation"], answer:1}
   ]},
  {subject:"Science", title:"Living and Non-Living Review", summary:"Students review the differences between living things (grow, breathe, reproduce, respond) and non-living things (do not do these things).",
   resourceLabel:"YouTube: Living and Non-Living Review", resourceUrl:"https://www.youtube.com/results?search_query=Living%20and%20Non-Living%20Review%20kindergarten%20educational",
   quiz:[
     {q:"Living things can ___.", options:["never change","grow, breathe, and reproduce","glow in the dark","fly always"], answer:1},
     {q:"A rock is non-living because it ___.", options:["grows","does not grow, breathe, or reproduce","reproduces","breathes"], answer:1},
     {q:"Which is a living thing?", options:["A book","A chair","A cloud","A tree"], answer:3},
     {q:"A non-living thing ___.", options:["has feelings","grows on its own","needs food and water to survive","does not grow, breathe, or reproduce on its own"], answer:3},
     {q:"Which is the best example of a non-living thing?", options:["Mushroom","Fish","Water","Flower"], answer:2}
   ]},
  {subject:"SocialStudies", title:"Caring for the Earth", summary:"Students review environmental responsibility: conserving water, reducing waste, protecting animals and plants, and making choices that help the planet.",
   resourceLabel:"YouTube: Caring for the Earth", resourceUrl:"https://www.youtube.com/results?search_query=Caring%20for%20the%20Earth%20kindergarten%20educational",
   quiz:[
     {q:"Conserving water means ___.", options:["using as much water as possible","only drinking water","wasting water daily","using water carefully and not wasting it"], answer:3},
     {q:"Which action helps protect the Earth?", options:["Leaving taps running","Throwing litter in parks","Turning off lights when leaving a room","Buying more plastic bags"], answer:2},
     {q:"Protecting habitats helps ___.", options:["only humans","the animals and plants that live there","only farmers","nobody"], answer:1},
     {q:"Why should we reduce waste?", options:["Only adults need to reduce waste","Waste is good","Waste helps plants grow","Less waste means less pollution and a healthier planet"], answer:3},
     {q:"One thing a child can do to help the Earth is ___.", options:["Move to another planet","Drive a car","Use less plastic and recycle where possible","Wait for adults to fix everything"], answer:2}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"Language", title:"Rhyming Words", summary:"Students identify and generate rhyming words. Rhyming words have the same ending sound (e.g., cat/hat, dog/log, play/day).",
   resourceLabel:"YouTube: Rhyming Words", resourceUrl:"https://www.youtube.com/results?search_query=Rhyming%20Words%20kindergarten%20educational",
   quiz:[
     {q:"Rhyming words have the same ___.", options:["beginning sound","middle sound","ending sound","number of letters"], answer:2},
     {q:"Which word rhymes with CAT?", options:["Hat","Dog","Sun","Cup"], answer:0},
     {q:"Which word rhymes with SUN?", options:["Star","Fun","Moon","Sky"], answer:1},
     {q:"Which pair of words rhymes?", options:["Ball/Bat","Play/Day","Sun/Moon","Dog/Cat"], answer:1},
     {q:"If CAKE rhymes with LAKE, which also rhymes?", options:["Like","Milk","Bike","Make"], answer:3}
   ]},
  {subject:"Math", title:"Counting to 100 by 2s and 5s", summary:"Students count forward by 2s and 5s to 100, building number sense and a foundation for multiplication.",
   resourceLabel:"YouTube: Counting to 100 by 2s and 5s", resourceUrl:"https://www.youtube.com/results?search_query=Counting%20to%20100%20by%202s%20and%205s%20kindergarten%20educational",
   quiz:[
     {q:"Count by 2s: 2, 4, 6, ___, 10", options:["8","9","11","7"], answer:0},
     {q:"Count by 5s: 5, 10, 15, ___", options:["20","25","18","16"], answer:0},
     {q:"Count by 2s: 14, 16, ___", options:["17","19","18","20"], answer:2},
     {q:"Count by 5s: 25, 30, ___", options:["45","40","33","35"], answer:3},
     {q:"Counting by 2s gives you only ___ numbers.", options:["even","prime","odd","random"], answer:0}
   ]},
  {subject:"Science", title:"Science Review: All Strands", summary:"Students review life science (plants, animals), earth science (seasons, weather), and physical science (forces, materials).",
   resourceLabel:"YouTube: Science Review: All Strands", resourceUrl:"https://www.youtube.com/results?search_query=Science%20Review%3A%20All%20Strands%20kindergarten%20educational",
   quiz:[
     {q:"Plants make food using ___, water, and carbon dioxide.", options:["Soil","Sunlight","Fertilizer","Rain"], answer:1},
     {q:"Animals need food, water, shelter, and ___ to survive.", options:["Money","Television","Toys","Air"], answer:3},
     {q:"The four seasons in Ontario are ___.", options:["North, south, east, west","Hot, cold, wet, dry","Spring, summer, fall, winter","Day, night, dawn, dusk"], answer:2},
     {q:"A push and a pull are both types of ___.", options:["forces","weather","patterns","materials"], answer:0},
     {q:"Which is a property of metal?", options:["Transparent","Soft and bendy","Light as a feather","Usually hard and conducts electricity"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Social Studies Review", summary:"Students review communities, Canadian geography, symbols, seasons, and citizenship topics covered through the year.",
   resourceLabel:"YouTube: Social Studies Review", resourceUrl:"https://www.youtube.com/results?search_query=Social%20Studies%20Review%20kindergarten%20educational",
   quiz:[
     {q:"What is the capital city of Canada?", options:["Vancouver","Ottawa","Montreal","Toronto"], answer:1},
     {q:"A community is ___.", options:["only a village","a group of people living and working together in an area","only a city","a type of animal"], answer:1},
     {q:"Which is a Canadian symbol?", options:["Maple leaf","Bald Eagle","Eiffel Tower","Statue of Liberty"], answer:0},
     {q:"Being a good citizen means ___.", options:["never helping anyone","only following rules you like","following laws, helping others, and respecting the community","only thinking about yourself"], answer:2},
     {q:"Canada has ___ official languages.", options:["3","1","4","2"], answer:3}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"Language", title:"Alphabet Review and Simple Reading", summary:"Students review all 26 letters, their sounds, and demonstrate early reading of simple CVC (consonant-vowel-consonant) words.",
   resourceLabel:"YouTube: Alphabet Review and Simple Reading", resourceUrl:"https://www.youtube.com/results?search_query=Alphabet%20Review%20and%20Simple%20Reading%20kindergarten%20educational",
   quiz:[
     {q:"How many letters are in the English alphabet?", options:["24","26","25","27"], answer:1},
     {q:"Which is a vowel?", options:["B","C","D","E"], answer:3},
     {q:"A CVC word has ___ letters.", options:["4","3","5","2"], answer:1},
     {q:"Which is a CVC word?", options:["Bring","Cat","Street","Play"], answer:1},
     {q:"Reading means ___.", options:["colouring pictures","only looking at books","only writing","turning letters into words and understanding their meaning"], answer:3}
   ]},
  {subject:"Math", title:"Year Review: Math", summary:"Students review all Kindergarten math concepts: counting, shapes, patterns, measurement, and addition/subtraction.",
   resourceLabel:"YouTube: Year Review: Math", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Math%20kindergarten%20educational",
   quiz:[
     {q:"Count: How many in 3 + 4?", options:["6","5","8","7"], answer:3},
     {q:"What shape has 4 equal sides?", options:["Square","Triangle","Circle","Rectangle"], answer:0},
     {q:"What comes next? 2, 4, 6, ___", options:["8","9","10","7"], answer:0},
     {q:"8 - 3 = ?", options:["7","6","5","4"], answer:2},
     {q:"Which is longer: a desk or a pencil?", options:["Cannot tell","Pencil","They are the same","Desk"], answer:3}
   ]},
  {subject:"Science", title:"Year Review: Science", summary:"Students review all Kindergarten science: living and non-living, plants, animals, seasons, weather, forces, and materials.",
   resourceLabel:"YouTube: Year Review: Science", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Science%20kindergarten%20educational",
   quiz:[
     {q:"A plant is a ___ thing.", options:["both","living","non-living","neither"], answer:1},
     {q:"Animals need food, water, shelter, and air. These are called ___.", options:["Extras","Options","Wants","Needs"], answer:3},
     {q:"Which season is it when leaves fall off trees?", options:["Spring","Winter","Summer","Fall/Autumn"], answer:3},
     {q:"A push and pull are types of ___.", options:["materials","forces","patterns","weather"], answer:1},
     {q:"Which material is transparent (see-through)?", options:["Metal","Wood","Rubber","Glass"], answer:3}
   ]},
  {subject:"SocialStudies", title:"Year Review: Social Studies and Citizenship", summary:"Students review community helpers, Canadian symbols, rights and responsibilities, celebrations, and caring for the Earth.",
   resourceLabel:"YouTube: Year Review: Social Studies and Citizenship", resourceUrl:"https://www.youtube.com/results?search_query=Year%20Review%3A%20Social%20Studies%20and%20Citizenship%20kindergarten%20educational",
   quiz:[
     {q:"Who helps keep you healthy by giving check-ups?", options:["Doctor","Caretaker","Teacher","Librarian"], answer:0},
     {q:"What symbol appears on the Canadian flag?", options:["Beaver","Maple leaf","Moose","Eagle"], answer:1},
     {q:"A right is something you ___.", options:["never earn","can take from others","must give to others","are allowed to do or have"], answer:3},
     {q:"Why is recycling important?", options:["Only for adults","It reduces waste and protects the environment","It is not","Only for scientists"], answer:1},
     {q:"A good citizen ___.", options:["ignores community rules","never votes","only cares about themselves","respects others, follows rules, and helps the community"], answer:3}
   ]},
]},
];

export default curriculum;