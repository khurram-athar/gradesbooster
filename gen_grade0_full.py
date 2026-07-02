#!/usr/bin/env python3
"""Full Grade 0 (Kindergarten) — all 30 days."""
import sys
sys.path.insert(0,'/sessions/wonderful-keen-tesla/mnt/gradesbooster')
from gen_curriculum import sub,day,write_new

U='https://tvolearn.com/pages/kindergarten'
R='TVO Learn: Kindergarten'

def L(t,s,q): return sub('Language',t,s,R,U,q)
def M(t,s,q): return sub('Math',t,s,R,U,q)
def Sc(t,s,q): return sub('Science',t,s,R,U,q)
def SS(t,s,q): return sub('SocialStudies',t,s,R,U,q)

g0=[
day(1,[
L('Letter A','Explore uppercase and lowercase A. Students identify the letter, practise its short /a/ sound, and find words beginning with A such as apple, ant, and astronaut.',[
  ('Which word starts with A?',['Ball','Cat','Apple','Dog'],2),
  ('What sound does short A make?',['Ah as in apple','Oh as in open','Ee as in see','Oo as in boot'],0),
  ('How many sides does uppercase A have?',['1','2','3','4'],2),
  ('Which A word is a fruit?',['Ant','Apple','Arrow','Axe'],1),
  ('Find the A: cat, apple, dog, sun',['cat','apple','dog','sun'],1)]),
M('Counting 1 to 5','Students count objects up to 5, match numerals to quantities, and begin to understand one-to-one correspondence.',[
  ('How many fingers on one hand?',['3','4','5','6'],2),
  ('What number comes after 3?',['2','4','5','1'],1),
  ('Which numeral means three?',['1','2','3','4'],2),
  ('Count the dots: ● ● ● ● How many?',['3','4','5','2'],1),
  ('What number comes before 5?',['3','4','6','2'],1)]),
Sc('Living and Non-Living Things','Students learn to distinguish living things (grow, breathe, need food/water) from non-living things (do not grow on their own, do not breathe).',[
  ('A living thing ___.',['cannot move ever','never changes','grows and needs food, water, and air','is made of metal'],2),
  ('Which is a living thing?',['Rock','Tree','Chair','Book'],1),
  ('Which is non-living?',['Dog','Flower','Table','Cat'],2),
  ('A non-living thing ___.',['breathes','grows on its own','does not grow, breathe, or reproduce on its own','needs food and water'],2),
  ('A bird is living because it ___.',['is colourful','makes noise','breathes, eats, and grows','can fly only'],2)]),
SS('My Family','Students explore different family structures — large, small, single-parent, grandparent families — and appreciate that all families are special.',[
  ('A family is a group of ___.',['strangers','people who care for and support each other','only parents and children','only people who look alike'],1),
  ('Which is an example of a family member?',['Teacher','Neighbour','Grandparent','Doctor'],2),
  ('Families can be ___.',['only large','only small','different sizes and structures','only two people'],2),
  ('How do families show they care?',['By ignoring each other','By helping, listening, and spending time together','By fighting only','By living apart'],1),
  ('Why is your family special?',['It is not','Every family is unique and special in its own way','Only big families are special','Only famous families are special'],1)])]),
day(2,[
L('Letter B','Explore uppercase and lowercase B. Students identify the letter, practise its /b/ sound, and name B words such as ball, bear, and butterfly.',[
  ('Which word starts with B?',['Dog','Cat','Ball','Frog'],2),
  ('What sound does B make?',['Puh','Buh','Duh','Kuh'],1),
  ('Which B word is an animal?',['Bat — yes it is a B animal','Car','Sun','Tree'],0),
  ('Find the B: cat, ball, apple, sun',['cat','ball','apple','sun'],1),
  ('How many bumps does lowercase b have?',['0','1','2','3'],1)]),
M('Counting 6 to 10','Students count objects from 6 to 10, match numerals to quantities, and practise counting on from 5.',[
  ('What number comes after 7?',['6','8','9','10'],1),
  ('Count: ●●●●●●●● How many dots?',['6','7','8','9'],2),
  ('Which numeral means eight?',['6','7','8','9'],2),
  ('What number comes before 10?',['7','8','9','11'],2),
  ('Count by 1s: 6, 7, ___',['5','8','9','10'],1)]),
Sc('Plants Around Us','Students explore plants in their environment. All plants have basic needs: sunlight, water, and soil. Plant parts include roots, stem, leaves, and sometimes flowers.',[
  ('All plants need ___ to grow.',['Snow and ice','Sunlight, water, and soil','Only water','Only sunlight'],1),
  ('Which part of a plant soaks up water from the soil?',['Leaves','Flowers','Stem','Roots'],3),
  ('Leaves help a plant by ___.',['holding it up only','storing seeds','making food using sunlight','protecting the roots'],2),
  ('Where do most plants grow?',['In the air','In soil','In water only','In rocks only'],1),
  ('Which is a plant?',['Cat','Rock','Daisy','Cloud'],2)]),
SS('My Home and Community','Students explore different types of homes (house, apartment, townhouse) and the idea that home is within a neighbourhood and community.',[
  ('A home is a place where ___.',['only adults live','people live and feel safe and cared for','only families with pets live','only babies live'],1),
  ('Which is a type of home?',['School','Hospital','Apartment building','Library'],2),
  ('A community is ___.',['one family only','a place where people live and work together','only a school','only a park'],1),
  ('What makes a home special?',['Its size','The colour of the walls','The people and love inside it','Only if it has a yard'],2),
  ('Which building is in most communities?',['A spaceship','A submarine','A school or fire station','A castle'],2)])]),
day(3,[
L('Letter C','Explore uppercase and lowercase C. Students identify the letter, practise its hard /k/ sound (cat, car), and find C words.',[
  ('Which word starts with C?',['Dog','Cat','Ball','Egg'],1),
  ('What sound does C make in "cat"?',['Sss','Shh','Kuh','Chh'],2),
  ('Which C word is an animal?',['Car','Cow','Clock','Cloud'],1),
  ('Find all C words: cat, dog, cow, cup',['cat only','dog only','cat, cow, and cup','cow only'],2),
  ('Lowercase c looks like ___.',['a straight line','a circle with a gap on the right','a rectangle','two bumps'],1)]),
M('2D Shapes: Circle and Square','Students identify, name, sort, and describe circles and squares. Circles have no corners; squares have 4 equal sides and 4 corners.',[
  ('A circle has ___ corners.',['1','2','3','0'],3),
  ('A square has ___ equal sides.',['2','3','4','5'],2),
  ('Which shape is perfectly round?',['Square','Triangle','Circle','Rectangle'],2),
  ('How many sides does a square have?',['2','3','4','6'],2),
  ('Which shape has no straight sides?',['Square','Triangle','Rectangle','Circle'],3)]),
Sc('Seasons: Autumn','Students explore the characteristics of autumn in Ontario — shorter days, falling leaves, cooler temperatures, and animals preparing for winter.',[
  ('What season comes after summer?',['Winter','Autumn/Fall','Spring','Rainy season'],1),
  ('In autumn, many trees ___.',['grow new leaves','bloom with flowers','lose their leaves','stay exactly the same'],2),
  ('Autumn is usually ___ than summer.',['hotter','cooler','the same temperature','colder than winter'],1),
  ('Animals prepare for winter in autumn by ___.',['playing more','storing food or preparing to migrate or hibernate','swimming more','staying exactly the same'],1),
  ('What do you wear in autumn?',['Swimsuit and sandals','Light jacket or sweater','Heavy winter coat','Nothing different'],1)]),
SS('Helping at Home','Students explore household responsibilities and how children can contribute by tidying, setting the table, and caring for pets.',[
  ('Helping at home means ___.',['only watching TV','doing chores and tasks that help the family','only doing homework','only playing games'],1),
  ('Which is an example of helping at home?',['Leaving toys everywhere','Putting toys away neatly','Eating all the snacks','Ignoring chores'],1),
  ('Why is it important to help at home?',['It is not','It teaches responsibility and helps the family work together','Only parents should do chores','Only if you are asked'],1),
  ('Which chore could a kindergartener do?',['Fix the roof','Pay the bills','Put shoes away neatly','Cook dinner alone'],2),
  ('When you help at home, your family feels ___.',['annoyed','proud and grateful','angry','nothing'],1)])]),
day(4,[
L('Letter D','Explore uppercase and lowercase D. Students identify the letter, practise its /d/ sound, and name D words such as dog, duck, and drum.',[
  ('Which word starts with D?',['Cat','Ball','Dog','Frog'],2),
  ('What sound does D make?',['Tuh','Buh','Duh','Puh'],2),
  ('Which D word is an animal?',['Door','Drum','Duck','Den'],2),
  ('Lowercase d looks like ___.',['only a straight line','a circle with a tall line on the right','two bumps','a curved line only'],1),
  ('Find the D words: door, cat, duck, ball',['cat and ball','door and duck','duck only','ball only'],1)]),
M('Number Order 1-10','Students arrange numbers 1-10 in order, identify missing numbers, and understand more/fewer using a number line.',[
  ('What number is missing? 1, 2, ___, 4, 5',['3','6','7','0'],0),
  ('Which number is greater: 7 or 4?',['4','7','Equal','Cannot tell'],1),
  ('Put in order: 5, 3, 1, 4, 2',['1, 2, 3, 4, 5','5, 4, 3, 2, 1','3, 1, 2, 4, 5','1, 3, 2, 5, 4'],0),
  ('What comes between 6 and 8?',['5','7','9','6'],1),
  ('Which has MORE: a group of 2 or a group of 9?',['2','9','Equal','Cannot tell'],1)]),
Sc('Water Around Us','Students explore water in their environment. Water is a liquid that flows, takes the shape of its container, and is essential for all life.',[
  ('Water is a ___.',['solid','gas','liquid','powder'],2),
  ('Living things need water to ___.',['only look nice','survive and stay healthy','only taste good','only wash'],1),
  ('Where can we find water in nature?',['Only in taps','Only in bottles','Rivers, lakes, rain, and oceans','Only in stores'],2),
  ('What shape does water take?',['Always a ball','Always flat','The shape of its container','Always a cube'],2),
  ('Why is clean water important?',['Only for swimming','For drinking, cooking, and keeping animals and plants alive','Only for cleaning','It is not important'],1)]),
SS('Community Helpers: Police and Firefighters','Students learn how police officers keep communities safe and how firefighters protect people and property. Both are important community helpers.',[
  ('What do police officers do?',['Teach in schools','Keep communities safe and uphold laws','Fix buildings','Deliver mail'],1),
  ('What do firefighters do?',['Only drive trucks','Protect people from fires and respond to emergencies','Teach children to read','Only put out campfires'],1),
  ('What number do you call in an emergency in Canada?',['411','511','911','211'],2),
  ('Firefighters wear special gear to ___.',['look important','protect themselves from heat, smoke, and flames','run faster','only look scary'],1),
  ('Why are community helpers important?',['They are not','They provide services that keep everyone safe and healthy','Only adults need them','Only in emergencies'],1)])]),
day(5,[
L('Vowels: A, E, I, O, U','Students learn to identify the five vowels and their short sounds. Vowels are special letters: a (apple), e (egg), i (igloo), o (octopus), u (umbrella).',[
  ('How many vowels are in the alphabet?',['3','4','5','6'],2),
  ('Which letter is a vowel?',['B','C','E','F'],2),
  ('Which word has the short A sound?',['Bike','Cat','Pete','Cute'],1),
  ('Which word has the short E sound?',['Cake','Mine','Egg','Boot'],2),
  ('The vowels are ___.',['B, C, D, F, G','A, E, I, O, U','Only A and E','Only I and O'],1)]),
M('Addition to 5','Students use objects, fingers, and drawings to add two groups and find totals up to 5.',[
  ('2 + 3 = ?',['4','5','6','3'],1),
  ('1 + 4 = ?',['4','5','6','3'],1),
  ('You have 2 apples and 2 oranges. How many fruit in all?',['2','3','4','5'],2),
  ('0 + 5 = ?',['0','4','5','10'],2),
  ('What does + mean?',['Take away','Put together to find the total','Multiply','Divide'],1)]),
Sc('The Sun and Moon','Students explore the Sun as Earth\'s main light and heat source. The Moon reflects sunlight and can be seen at night. They observe day and night.',[
  ('The Sun gives us ___ and ___.',['ice and darkness','light and heat','rain and snow','cold and wind'],1),
  ('The Sun is a ___.',['planet','moon','very large star','comet'],2),
  ('The Moon ___ its own light.',['makes plenty of','produces strongly','does not produce — it reflects sunlight','creates daily'],2),
  ('We usually see the Sun during the ___.',['night','day','only at sunrise','only in winter'],1),
  ('Why should you never look directly at the Sun?',['It is invisible','It moves too fast','Its intense light can damage your eyes','It is too far away to matter'],2)]),
SS('My School Community','Students explore the school as a community. They identify key helpers: principal, teacher, custodian, librarian, and secretary.',[
  ('Who is the leader of a school?',['The student','The custodian','The principal','The librarian'],2),
  ('What is a teacher\'s main role?',['Fix the building','Cook food','Help students learn','Answer phones'],2),
  ('What does a school custodian do?',['Teach reading','Keep the school clean and safe','Run the office','Drive the bus'],1),
  ('A school is a community because ___.',['it has one teacher','people work and learn together there','it is a building','only children are there'],1),
  ('Which person helps students find books?',['Principal','Custodian','Secretary','Librarian'],3)])]),
day(6,[
L('Letter E','Explore uppercase and lowercase E. Students practise the short /e/ sound (egg, elephant) and identify E words.',[
  ('Which word starts with E?',['Dog','Apple','Egg','Cat'],2),
  ('What is the short E sound?',['Ay as in day','Ee as in see','Eh as in egg','Oh as in go'],2),
  ('Which E word is an animal?',['Egg','Eagle','Empty','Each'],1),
  ('Find the E: cat, egg, tree, and elephant',['cat','egg','tree','elephant (both egg and elephant)'],3),
  ('E is a ___.',['consonant','number','vowel','colour'],2)]),
M('Patterns: ABAB','Students identify, copy, extend, and create simple repeating AB patterns using colours, shapes, sounds, and actions.',[
  ('What comes next? Red, Blue, Red, Blue, ___',['Red','Green','Yellow','Blue'],0),
  ('What is the pattern? Circle, Square, Circle, Square',['AAAA','ABAB','AABB','ABBA'],1),
  ('What comes next? clap, stomp, clap, stomp, ___',['stomp','clap','jump','sit'],1),
  ('A repeating pattern always ___.',['stops after 4 items','changes randomly','follows the same rule over and over','has only 2 colours'],2),
  ('Create an ABAB pattern: Star, Heart, Star, Heart, ___',['Circle','Heart','Star','Triangle'],2)]),
Sc('Pets and Their Needs','Students explore common pets (dog, cat, fish, bird) and their needs: food, water, shelter, exercise, and love.',[
  ('What do all pets need to stay healthy?',['Only toys','Food, water, shelter, and care','Only a bed','Only food'],1),
  ('Why do dogs need daily exercise?',['They do not','Exercise keeps them healthy and happy','Only puppies need exercise','Only for big dogs'],1),
  ('A fish needs ___ to breathe.',['air like humans','soil','water with dissolved oxygen (and often a filter)','only food'],2),
  ('Who is responsible for a pet\'s care?',['Only the veterinarian','Only adults','The owner/family who chose to have the pet','No one'],2),
  ('Why is it important to care well for pets?',['It is not','Animals feel pain and need care just as people do; owners are responsible','Only if you want to','Only for expensive pets'],1)]),
SS('Rules and Responsibility','Students explore why communities have rules: to keep people safe and ensure fairness. They discuss school rules and why following them matters.',[
  ('Rules help ___.',['create chaos','keep people safe and ensure fairness','only help teachers','only help adults'],1),
  ('Which is a school rule?',['Run in the halls','Push others in line','Listen when someone is speaking','Never ask questions'],2),
  ('What happens if no one follows rules?',['Everything stays the same','Communities become unsafe and unfair','Only teachers care','Rules fix themselves'],1),
  ('A responsibility is ___.',['something others do for you','a job or duty that you are expected to do','only for adults','never fun'],1),
  ('Which is an example of responsibility at school?',['Littering','Arriving on time with your bag packed','Ignoring a classmate\'s help','Only doing your favourite subjects'],1)])]),
day(7,[
L('Letter F','Explore uppercase and lowercase F. Students practise the /f/ sound and name F words such as fish, frog, and flower.',[
  ('Which word starts with F?',['Dog','Cat','Fish','Egg'],2),
  ('What sound does F make?',['Vvv','Buh','Fff','Puh'],2),
  ('Which F word is an animal?',['Flower','Farm','Frog','Float'],2),
  ('Find all F words: fish, cat, frog, flower',['cat only','fish only','fish, frog, and flower','frog only'],2),
  ('Lowercase f looks like ___.',['a straight line','a hook at the top with a crossbar','two bumps','a circle'],1)]),
M('Counting to 20','Students count forward from any number to 20, identify missing numbers, and begin to recognise teen numbers as ten and some more.',[
  ('What comes after 13?',['12','14','15','16'],1),
  ('Count: 15, 16, 17, ___',['18','19','20','14'],0),
  ('Which number is between 10 and 12?',['9','11','13','8'],1),
  ('How many tens are in the number 15?',['0','1','2','5'],1),
  ('Count on from 17: 17, 18, 19, ___',['16','20','21','22'],1)]),
Sc('Wild Animals','Students explore wild animals in Ontario and beyond. Wild animals live in natural habitats, find their own food, and are not tamed.',[
  ('A wild animal is one that ___.',['lives in a cage','is someone\'s pet','lives in a natural habitat and finds its own food','is always dangerous'],2),
  ('Which is a wild animal?',['Dog','Cat','Moose','Goldfish'],2),
  ('Where would you find a beaver in the wild?',['In a city apartment','In a desert','Near lakes and rivers in forests','In a shopping mall'],2),
  ('Wild animals should ___.',['be taken home as pets','always be fed by humans','be observed from a safe distance and left in their habitat','be hunted for food always'],2),
  ('What do wild animals eat?',['Food from grocery stores','Only vegetables','What they find in their natural habitat (prey, plants, insects)','Only what humans give them'],2)]),
SS('Being a Good Friend','Students explore qualities of friendship: kindness, sharing, taking turns, listening, and including others. Good friends treat each other with respect.',[
  ('A good friend ___.',['takes your things without asking','is kind and includes others','only plays with you if you have toys','ignores you when busy'],1),
  ('Sharing means ___.',['keeping everything for yourself','letting others use or enjoy what you have','only sharing food','only sharing with best friends'],1),
  ('Taking turns means ___.',['always going first','each person gets a chance','only one person goes','skipping others'],1),
  ('Why is it important to include everyone?',['It is not','Everyone deserves to feel welcome and belonging','Only some people need friends','Only if you like them'],1),
  ('Which is an act of friendship?',['Laughing at a mistake','Pushing in line','Cheering a friend on when they try something hard','Ignoring a friend who is sad'],2)])]),
day(8,[
L('Letter G','Explore uppercase and lowercase G. Students practise the hard /g/ sound (goat, grape) and find G words.',[
  ('Which word starts with G?',['Dog','Apple','Goat','Fish'],2),
  ('What sound does G make in "goat"?',['Juh','Kuh','Guh','Shh'],2),
  ('Which G word is a fruit?',['Goat','Grape','Grass','Grain'],1),
  ('Find the G: dog, goat, green, frog',['dog','goat','green','goat and green'],3),
  ('G is a ___.',['vowel','consonant','number','colour'],1)]),
M('Non-Standard Measurement: Length','Students measure the length of objects using non-standard units (paper clips, blocks, hands) and use the words longer, shorter, and same.',[
  ('Measuring tells you ___.',['the colour of something','how long, tall, or heavy something is','what something smells like','where something is'],1),
  ('Non-standard units for measuring include ___.',['metres and centimetres','paper clips, hand spans, or blocks','kilograms','thermometers'],1),
  ('A book is 8 paper clips long. A pencil is 5. The book is ___.',['shorter','the same length as the pencil','longer','impossible to compare'],2),
  ('To compare lengths fairly, you must ___.',['guess','use a computer','start measuring from the same point','always use a ruler'],2),
  ('If a desk is 3 shoe lengths long, shoe length is a ___.',['standard unit','non-standard unit','weight unit','temperature unit'],1)]),
Sc('Parts of a Plant','Students name and describe the function of plant parts: roots (absorb water), stem (transport water and support), leaves (make food), flower (reproduction), seed (new plant).',[
  ('Roots help a plant by ___.',['making food using sunlight','producing flowers','absorbing water and nutrients from the soil','protecting seeds'],2),
  ('The stem of a plant ___.',['only makes flowers','only holds seeds','supports the plant and carries water from roots to leaves','absorbs sunlight directly'],2),
  ('Leaves are the main part of a plant that ___.',['hold up the plant','make food using sunlight and air','absorb water from soil','produce seeds only'],1),
  ('A flower helps a plant by ___.',['absorbing water','making food','supporting the stem','producing seeds that grow into new plants'],3),
  ('A seed will grow into ___.',['a flower only','a root only','a new plant','only a stem'],2)]),
SS('Canadian Symbols','Students learn symbols that represent Canada: the maple leaf flag, beaver, and Parliament Buildings. These symbols create a shared Canadian identity.',[
  ('What appears on the Canadian flag?',['A beaver','An eagle','A maple leaf','A moose'],2),
  ('Canada\'s national animal is the ___.',['moose','beaver','bear','wolf'],1),
  ('The maple leaf is a symbol of ___.',['the United States','England','Canada','France'],2),
  ('Where does the Canadian government meet?',['The CN Tower','Parliament Hill in Ottawa','Niagara Falls','The Rocky Mountains'],1),
  ('Why do countries have symbols?',['Only for money','To identify the nation and give its people a shared sense of pride and belonging','Only for flags','Only for tourists'],1)])]),
day(9,[
L('Letter H','Explore uppercase and lowercase H. Students practise the /h/ sound and name H words such as house, horse, and hat.',[
  ('Which word starts with H?',['Dog','Apple','House','Frog'],2),
  ('What sound does H make?',['Kuh','Huh (a breathy sound)','Puh','Shh'],1),
  ('Which H word do you wear on your head?',['House','Horse','Hat','Hand'],2),
  ('Find the H: hat, dog, horse, cat',['dog and cat','hat and horse','horse only','hat only'],1),
  ('H is a ___.',['vowel','consonant','number','colour'],1)]),
M('Subtraction from 5','Students subtract within 5 using objects, pictures, and fingers. They understand subtraction as taking away.',[
  ('5 - 2 = ?',['2','3','4','5'],1),
  ('4 - 4 = ?',['0','1','4','8'],0),
  ('What does the - sign mean?',['Add','Multiply','Take away','Measure'],2),
  ('3 - 1 = ?',['1','2','3','4'],1),
  ('You have 5 grapes and eat 3. How many are left?',['1','2','3','4'],1)]),
Sc('Winter Season','Students explore characteristics of winter in Ontario: cold temperatures, ice and snow, shorter days, and how animals and plants respond.',[
  ('What is winter like in Ontario?',['Very hot and sunny','Cold with snow and ice','Always rainy','Never changes'],1),
  ('In winter, deciduous trees (like maples) ___.',['grow new leaves','bloom with flowers','lose their leaves (they fell in autumn)','stay green'],2),
  ('Some animals hibernate in winter. Hibernation means ___.',['flying south','growing thicker fur','sleeping deeply to save energy through winter','staying exactly the same'],2),
  ('Days are ___ in winter than in summer.',['longer','the same length','shorter','exactly 12 hours'],2),
  ('What do humans wear in winter to stay warm?',['Swimsuits','T-shirts and shorts','Heavy coats, mittens, and boots','No special clothing'],2)]),
SS('Our Environment: Caring for Nature','Students learn that the environment includes air, water, land, plants, and animals. Everyone can help protect it by reducing waste and not littering.',[
  ('The environment includes ___.',['only animals','only plants','the air, water, land, plants, and all living things around us','only what we can see in cities'],2),
  ('Littering means ___.',['recycling properly','dropping waste on the ground instead of in a bin','composting','picking up litter'],2),
  ('How can you help the environment?',['Leave taps running','Litter in parks','Turn off lights and put waste in the bin','Use extra plastic bags'],2),
  ('Why is clean air important?',['Only for birds','All living things need clean air to breathe and stay healthy','Only in cities','Only in summer'],1),
  ('Recycling helps the environment because ___.',['it makes more rubbish','it reduces waste and reuses materials','it is only for adults','only paper can be recycled'],1)])]),
day(10,[
L('Short Vowel Sounds','Students review and practise identifying short vowel sounds: a (cat), e (hen), i (pig), o (dog), u (bug) in spoken words.',[
  ('Which word has the short A sound?',['Bike','Name','Cat','Cute'],2),
  ('Which word has the short I sound?',['Cake','Pig','Pete','Tube'],1),
  ('Which word has the short O sound?',['Bean','Rain','Dog','Blue'],2),
  ('Which word has the short U sound?',['Rain','Cake','Bee','Bug'],3),
  ('All short vowel sounds come from ___.',['consonants','the vowels A, E, I, O, U','only A and E','numbers'],1)]),
M('3D Shapes: Sphere, Cube, Cylinder','Students identify and describe 3D shapes they encounter daily. A sphere (ball), cube (dice), and cylinder (can) are explored.',[
  ('A sphere looks like ___.',['a box','a flat circle','a ball','a cone'],2),
  ('A cube has ___ flat faces.',['4','5','6','8'],2),
  ('Which 3D shape is a can of soup?',['Sphere','Cube','Cylinder','Cone'],2),
  ('Which 3D shape can roll in any direction?',['Cube','Cylinder','Cone','Sphere'],3),
  ('How many corners (vertices) does a cube have?',['4','6','8','12'],2)]),
Sc('Weather','Students explore types of weather (sunny, cloudy, rainy, snowy, windy) and learn that weather affects what we wear and do each day.',[
  ('Weather is ___.',['the same every day','the condition of the air outside at a particular time','only about temperature','only rain or sunshine'],1),
  ('Which tool measures temperature outside?',['A ruler','A scale','A thermometer','A compass'],2),
  ('On a rainy day, you would wear ___.',['sandals and shorts','a swimsuit','a raincoat and boots','a heavy winter coat'],2),
  ('Why does weather change from day to day?',['It does not change','Movements of air, moisture, and temperature differences cause weather changes','Only in spring','Only the Sun affects weather'],1),
  ('Which weather word means "no clouds and bright sunshine"?',['Foggy','Cloudy','Snowy','Sunny'],3)]),
SS('Family Traditions','Students learn that families celebrate traditions: special events, foods, stories, and practices that are passed down and shared. All traditions are valued.',[
  ('A family tradition is ___.',['something only old people do','a special practice, story, or celebration that a family shares and passes down','only a holiday','only about food'],1),
  ('An example of a family tradition could be ___.',['ignoring family members','a special meal made every year for a holiday','arguing about rules','never celebrating anything'],1),
  ('Why are traditions important?',['They are not','They connect families to their history and heritage and create special memories','Only for wealthy families','Only for certain cultures'],1),
  ('Can different families have different traditions?',['No','Only if they are the same culture','Yes — each family\'s traditions are unique and special','Only in other countries'],2),
  ('Sharing family traditions with classmates ___.',['causes problems','shows respect and helps others learn about different cultures','is embarrassing','only confuses others'],1)])]),
day(11,[
L('Letter I','Explore uppercase and lowercase I. Students practise the short /i/ sound (igloo, insect) and the long /i/ sound (ice, island).',[
  ('Which word has the short I sound?',['Ice','Bike','Igloo','Fire'],2),
  ('Which word starts with I and is a cold home?',['Island','Iron','Igloo','Ivy'],2),
  ('I is a ___.',['consonant','number','vowel','colour'],2),
  ('Find the I: ant, igloo, elephant, octopus',['ant','igloo','elephant','octopus'],1),
  ('Which I word is a small creature?',['Island','Iron','Insect','Ice'],2)]),
M('Addition to 10','Students add two groups with totals up to 10. They use number lines, counters, and drawings.',[
  ('4 + 6 = ?',['8','9','10','11'],2),
  ('7 + 3 = ?',['8','9','10','11'],2),
  ('You have 5 stickers and get 4 more. How many total?',['8','9','10','11'],1),
  ('3 + 3 = ?',['5','6','7','8'],1),
  ('8 + 2 = ?',['9','10','11','12'],1)]),
Sc('Farm Animals','Students learn about common farm animals (cow, pig, chicken, sheep, horse) and how farms provide food and other products for communities.',[
  ('Which animal lives on a farm and gives us milk?',['Dog','Cow','Cat','Fish'],1),
  ('Which farm animal gives us wool for clothing?',['Pig','Cow','Horse','Sheep'],3),
  ('Eggs come from ___.',['cows','pigs','chickens','sheep'],2),
  ('Why are farms important?',['They are not','Farms produce food that feeds communities and countries','Only animals live there','Only for rural people'],1),
  ('Which of these is a farm animal?',['Tiger','Elephant','Horse','Polar bear'],2)]),
SS('Kinds of Families','Students learn that families can look different — some have two parents, some one parent, some grandparents as caregivers, blended families — and all are equally valid.',[
  ('All families are ___.',['the same','small','different and equally special and valid','only large'],2),
  ('Which is an example of a family type?',['A country','A school','A single-parent family','A city'],2),
  ('A blended family is one where ___.',['no children are present','only grandparents live together','two families join together (step-parents, step-siblings)','only one parent lives in the house'],2),
  ('What makes every family special?',['Only its size','Only its money','The love and care the members share','Only how big the house is'],2),
  ('Why is it important to respect different kinds of families?',['It is not','All families deserve respect; diversity in families is natural and normal','Only traditional families are valid','Only if they are like yours'],1)])]),
day(12,[
L('Letter J','Explore uppercase and lowercase J. Students practise the /j/ sound and name J words such as jump, jungle, and jar.',[
  ('Which word starts with J?',['Dog','Cat','Jump','Kite'],2),
  ('What sound does J make?',['Yuh','Juh (as in jump)','Shh','Kuh'],1),
  ('Which J word means to leap into the air?',['Jar','Jam','Jump','Just'],2),
  ('Find the J: jellyfish, cat, jar, apple',['cat and apple','jellyfish and jar','jar only','jellyfish only'],1),
  ('J is a ___.',['vowel','consonant','number','colour'],1)]),
M('Ordinal Numbers: 1st to 5th','Students use ordinal numbers (first, second, third, fourth, fifth) to describe position in a line or sequence.',[
  ('First means ___.',['last in line','in the middle','number one in position','second'],2),
  ('If you win a race, you are in ___ place.',['last','second','third','first'],3),
  ('Third means ___.',['2nd in order','3rd in order','4th in order','5th in order'],1),
  ('In a line of 5: cat, dog, bird, fish, rabbit — which is SECOND?',['cat','dog','bird','fish'],1),
  ('The word "second" describes ___.',['a unit of time only','a place in an ordered sequence','only sports rankings','only book chapters'],1)]),
Sc('Materials: Natural and Human-Made','Students sort materials into natural (wood, cotton, water, wool) and human-made/manufactured (plastic, glass, metal, nylon). Both types have different properties and uses.',[
  ('A natural material is one that ___.',['is made in a factory','comes from nature (plants, animals, or the earth)','is always plastic','is never used for clothing'],1),
  ('Which is a natural material?',['Plastic','Nylon','Glass','Wood'],3),
  ('Which is a human-made (manufactured) material?',['Cotton','Wool','Plastic','Wood'],2),
  ('Why do humans make new materials?',['Only for decoration','To create materials with specific properties that may not exist in nature','Natural materials are bad','Only for factories'],1),
  ('Wool comes from ___.',['trees','sheep','factories','plastic plants'],1)]),
SS('Our Town/City','Students explore the features of their local community: streets, buildings, parks, services, and how the town/city helps people meet their needs.',[
  ('What is a community?',['Only one house','Only a school','A group of people living and working together in an area','Only a shopping centre'],2),
  ('Which feature do most towns have?',['A volcano','An ocean beach','Roads, schools, and emergency services','Only one store'],2),
  ('A park is an important community space because ___.',['it is only for dogs','it gives people a place to relax, play, and connect with nature','only athletes use it','it replaces schools'],1),
  ('Which service helps when there is a fire?',['School','Library','Fire station','Grocery store'],1),
  ('Why do people live in communities?',['To be isolated','Communities allow people to share resources, services, and support each other','Only for shopping','Only for work'],1)])]),
day(13,[
L('Letter K','Explore uppercase and lowercase K. Students practise the /k/ sound (same as hard C) and name K words such as kite, king, and kangaroo.',[
  ('Which word starts with K?',['Cat','Kite','Ball','Door'],1),
  ('K makes the same sound as ___.',['hard C (kuh)','soft C (sss)','G','H'],0),
  ('Which K word is a large jumping animal?',['King','Kite','Kangaroo','Kind'],2),
  ('Find the K: kite, cat, king, dog',['cat and dog','kite and king','king only','kite only'],1),
  ('K is a ___.',['vowel','consonant','number','colour'],1)]),
M('ABC Patterns','Students identify, extend, and create ABC patterns (three repeating units) using colours, shapes, and objects.',[
  ('In an ABC pattern, what comes after A, B, C?',['D','C','A (the pattern repeats)','B'],2),
  ('What comes next? Red, Blue, Green, Red, Blue, ___',['Red','Yellow','Green','Blue'],2),
  ('Identify: triangle, circle, square, triangle, circle, ___',['triangle','circle','square','rectangle'],2),
  ('An ABC pattern repeats every ___ items.',['2','3','4','5'],1),
  ('Create: Cat, Dog, Bird, Cat, Dog, ___',['Cat','Dog','Fish','Bird'],3)]),
Sc('Sound and Light','Students explore that sound travels as vibrations and light travels in straight lines. They investigate different sources of both.',[
  ('Sound is produced by ___.',['light waves','vibrations','magnetic fields','heat only'],1),
  ('You can make sound by ___.',['only pressing a button','banging, plucking, blowing, or vibrating objects','looking at things','only singing'],1),
  ('Light travels in ___.',['curves','zigzags','straight lines','circles'],2),
  ('Which is a natural source of light?',['A torch','A lamp','The Sun','A television'],2),
  ('Why do we need light?',['Only for reading','To see, grow plants, and feel warmth — light is essential for life on Earth','Only at night','Only in winter'],1)]),
SS('Rights and Responsibilities','Students learn that rights (things they are entitled to: safety, education, play) come with responsibilities (duties: respect, cooperation, looking after things).',[
  ('A right is something you ___.',['must give up','are entitled to have or do','can take from others','never deserve'],1),
  ('A responsibility is something you ___.',['are expected to do or look after','can ignore','only do when adults watch','never have as a child'],0),
  ('Which is a right of children in Canada?',['Working long hours','Education, safety, and play','No protection under law','Only food'],1),
  ('Which is a responsibility at school?',['Littering in the hallway','Arriving late every day','Treating classmates with respect','Ignoring classroom rules'],2),
  ('Rights and responsibilities ___.',['are unrelated','go together — having rights means respecting others\' rights too','only adults have','only governments have'],1)])]),
day(14,[
L('Letter L','Explore uppercase and lowercase L. Students practise the /l/ sound and name L words such as leaf, lion, and lemon.',[
  ('Which word starts with L?',['Dog','Apple','Leaf','Mango'],2),
  ('What sound does L make?',['Ruh','Lll (as in leaf)','Buh','Puh'],1),
  ('Which L word is an animal?',['Leaf','Lemon','Lion','Light'],2),
  ('Find all L words: leaf, dog, lemon, lion',['dog only','leaf, lemon, and lion','lion only','lemon only'],1),
  ('Lowercase l looks like ___.',['a bump','a tall straight line','a curve','two bumps'],1)]),
M('Number Words 1 to 10','Students match numerals to number words: one, two, three, four, five, six, seven, eight, nine, ten.',[
  ('Which number word means 5?',['Three','Four','Five','Six'],2),
  ('The number 8 is spelled ___.',['Eight','Eight — that\'s correct','Ate','Ayt'],0),
  ('Which number word means 10?',['Nine','Ten','Seven','Eight'],1),
  ('Match: 3 = ?',['One','Two','Three','Four'],2),
  ('How do you spell 7?',['Sevan','Sevun','Seven','Siven'],2)]),
Sc('Spring Season','Students explore characteristics of spring in Ontario: warming temperatures, returning birds, blossoming plants, and rain showers.',[
  ('What season comes after winter?',['Autumn','Spring','Summer','Rainy season'],1),
  ('In spring, plants ___.',['die off','go dormant','start growing again — new leaves and flowers appear','have no change'],2),
  ('Many birds ___ in spring after being away in warmer places.',['hibernate','return (migrate back north)','disappear','stay underground'],1),
  ('Spring weather in Ontario is often ___.',['hot and dry like summer','cold and snowy like winter','warming, with rain showers','always perfect'],2),
  ('What is one sign that spring has arrived?',['Snow on the ground','Leaves falling from trees','Flowers blooming and birds singing','Very cold temperatures'],2)]),
SS('Special People in My Life','Students identify and appreciate special people in their lives: family members, friends, teachers, and community helpers who contribute to their wellbeing.',[
  ('A special person in your life is someone who ___.',['ignores you','does not care about you','cares about you, helps you, and makes you feel valued','only gives you gifts'],2),
  ('How can you show appreciation to someone special?',['Ignore them','Take their things','Say thank you and show kindness','Never talk to them'],2),
  ('Which person at school helps you feel safe and learn every day?',['A stranger','Your teacher','Someone on TV','No one'],1),
  ('Why is it important to appreciate the people who help you?',['It is not','It shows respect and encourages positive relationships','Only for birthdays','Only if they give you things'],1),
  ('A community helper who is special to the community is ___.',['anyone who contributes positively to others\' wellbeing','only a policeman','only a teacher','only a family member'],0)])]),
day(15,[
L('Letter M','Explore uppercase and lowercase M. Students practise the /m/ sound and name M words such as moon, monkey, and mango.',[
  ('Which word starts with M?',['Dog','Apple','Moon','Kite'],2),
  ('What sound does M make?',['Mmm (lips together)','Nnn','Buh','Puh'],0),
  ('Which M word is an animal?',['Moon','Mango','Monkey','Mud'],2),
  ('Find all M words: moon, sun, mango, monkey',['sun only','moon, mango, monkey','mango only','monkey only'],1),
  ('Lowercase m has ___.',['one bump','two bumps','three bumps','no bumps'],1)]),
M('Counting by 2s to 20','Students skip-count by 2s (2, 4, 6, 8...) to 20, recognising the pattern of even numbers.',[
  ('Count by 2s: 2, 4, 6, ___',['7','8','9','10'],1),
  ('Count by 2s: 10, 12, 14, ___',['15','16','17','18'],1),
  ('Counting by 2s gives you ___ numbers.',['odd','even','random','prime'],1),
  ('What comes next? 16, 18, ___',['17','20','19','21'],1),
  ('Which list is counting by 2s?',['1,2,3,4,5','2,4,6,8,10','1,3,5,7,9','2,3,5,7,11'],1)]),
Sc('Seasons Review','Students review the four seasons in Ontario, reinforcing what changes during each — temperatures, clothing, plants, animals, and activities.',[
  ('Which season comes after summer?',['Winter','Spring','Fall/Autumn','Rainy season'],2),
  ('In spring, many animals ___.',['hibernate','have babies and become active again','migrate south','go dormant'],1),
  ('What type of clothing do you wear in summer?',['Heavy coat and boots','Light clothes and shorts','Thick sweaters','Ski gear'],1),
  ('In fall, many farmers ___.',['plant crops','harvest their crops','begin planting seeds','do nothing'],1),
  ('Which season is it when you can make a snowman?',['Spring','Summer','Fall','Winter'],3)]),
SS('Community Helpers: Doctors and Teachers','Students explore how doctors keep us healthy and how teachers help us learn. They appreciate that community helpers work to improve the lives of everyone.',[
  ('What does a doctor do?',['Build houses','Help people stay healthy and treat illness','Teach reading and writing','Drive a fire truck'],1),
  ('Why is a teacher an important community helper?',['They fix cars','They help children learn and grow','They deliver mail','They cook food'],1),
  ('Where do you go to see a doctor?',['A library','A fire station','A clinic or hospital','A school'],2),
  ('Community helpers work to make our community ___.',['worse','better and safer for everyone','confusing','smaller'],1),
  ('Who would you visit for a check-up to make sure you are healthy?',['Teacher','Doctor','Firefighter','Librarian'],1)])]),
day(16,[
L('Letter P','Explore uppercase and lowercase P. Students identify the letter, practise its sound, and name words beginning with P such as penguin, pizza, and purple.',[
  ('What sound does the letter P make?',['Buh','Puh','Duh','Guh'],1),
  ('Which word starts with P?',['Dog','Cat','Pig','Run'],2),
  ('How do you write a lowercase p?',['Like a b facing right','A stick with a circle at the bottom left','A tall stick','Two circles'],1),
  ('Which of these starts with P?',['Apple','Banana','Pear','Mango'],2),
  ('Find the P word: sun, moon, ___, stars',['Sky','Planet','Cloud','Rain'],1)]),
M('Numbers 1-20: Recognition','Students read and write numerals 1 to 20, connecting each numeral to its quantity.',[
  ('What number comes after 15?',['14','16','17','18'],1),
  ('Which numeral means fifteen?',['51','5','15','150'],2),
  ('Count: 17, 18, 19, ___',['20','21','22','10'],0),
  ('Which group has 20 items?',['A group of ten','A group of fifteen','A group of twenty','A group of five'],2),
  ('Write the number: nineteen',['91','9','19','190'],2)]),
Sc('Push and Pull: Forces','Students explore how pushing and pulling are forces that move objects. They observe that heavier objects need more force.',[
  ('A push moves an object ___ you.',['toward','away from','beside','under'],1),
  ('A pull moves an object ___ you.',['away from','beside','toward','under'],2),
  ('Which is an example of a push?',['Pulling a wagon','Opening a drawer toward you','Kicking a ball','Picking up a book'],2),
  ('Which is an example of a pull?',['Pushing a door open','Throwing a ball','Opening a drawer toward you','Kicking a soccer ball'],2),
  ('A heavy object needs ___ force to move than a light one.',['less','the same','more','no'],2)]),
SS('Our School Community','Students explore the school as a community. They identify helpers such as the principal, caretaker, librarian, and office staff.',[
  ('Who is the leader of a school?',['Teacher','Principal','Librarian','Caretaker'],1),
  ('What does a librarian do?',['Fix the building','Help with books and reading','Cook food','Drive the bus'],1),
  ('A caretaker helps keep the school ___.',['noisy','clean and safe','messy','closed'],1),
  ('Why is the school a community?',['People fight there','People live there','People work and learn together','No one helps each other'],2),
  ('Who answers the phone and helps visitors in a school?',['The teacher','The caretaker','The office staff','The librarian'],2)])]),
day(17,[
L('Letter Q','Explore uppercase and lowercase Q. Students identify the letter, practise its sound, and recognise that Q is almost always followed by U in English words.',[
  ('What sound does Q make?',['Kw','Sh','Th','Zh'],0),
  ('Q is almost always followed by ___.',['A','E','U','O'],2),
  ('Which word starts with Q?',['King','Queen','Quick','Both B and C'],3),
  ('A word that means silent and peaceful starts with Q. It is ___.',['Quick','Quiet','Quite','Quiz'],1),
  ('Which Q word describes something fast?',['Quiet','Queen','Quick','Quarter'],2)]),
M('Sorting by Size and Colour','Students sort collections by size (big/small) and colour. They explain their sorting rule.',[
  ('When you sort by size, you group objects that are ___.',['the same colour','the same size','the same shape','the same weight'],1),
  ('Which sorting rule is used if all red things are together?',['Shape','Size','Colour','Weight'],2),
  ('You can sort the same set of objects in ___ ways.',['only one','only two','many different','no'],2),
  ('What is the sorting rule if you put triangles together?',['Colour','Size','Shape','Number'],2),
  ('You have 3 big blocks and 5 small blocks. How many blocks in all?',['3','5','7','8'],3)]),
Sc('Sinking and Floating','Students predict and test whether objects sink or float in water, discovering that shape and material affect floating.',[
  ('An object that stays on top of water ___.',['sinks','floats','dissolves','disappears'],1),
  ('An object that goes to the bottom of water ___.',['floats','dissolves','sinks','melts'],2),
  ('A wooden stick will most likely ___.',['sink','float','dissolve','explode'],1),
  ('A heavy metal coin will most likely ___.',['float','dissolve','fly','sink'],3),
  ('What can change whether something floats?',['Only its colour','Its shape and the material it is made of','Only its colour and smell','Nothing'],1)]),
SS('Needs and Wants','Students learn to distinguish between needs (things necessary to survive) and wants (things we desire but do not need).',[
  ('A need is something you ___ to survive.',['want','must have','choose','enjoy'],1),
  ('A want is something you ___ to survive.',['must have','do not need','cannot live without','must buy'],1),
  ('Which is a NEED?',['A toy car','A video game','Clean water','A bicycle'],2),
  ('Which is a WANT?',['Food','Shelter','A new book bag','Clothing'],2),
  ('Why is it important to know the difference between needs and wants?',['It is not important','It helps you make good choices with money and resources','Only adults need to know','Wants are always wrong'],1)])]),
day(18,[
L('Letter R','Explore uppercase and lowercase R. Students identify the letter, practise its /r/ sound, and name words beginning with R such as rabbit, rain, and rainbow.',[
  ('Which word starts with R?',['Ball','Cake','Rain','Dog'],2),
  ('What sound does R make?',['Luh','Ruh','Wuh','Nuh'],1),
  ('Which animal starts with R?',['Cat','Bear','Dog','Rabbit'],3),
  ('Find the R word: The ___ is falling from the sky.',['Sun','Moon','Rain','Wind'],2),
  ('Which colour starts with R?',['Blue','Green','Red','Purple'],2)]),
M('Patterns: ABAB and AABB','Students identify, copy, extend, and create repeating patterns using objects, sounds, and actions.',[
  ('In an ABAB pattern, what comes after A?',['A','C','B','D'],2),
  ('What comes next? Red, Blue, Red, Blue, ___',['Red','Green','Yellow','Purple'],0),
  ('What is the pattern rule for: circle, circle, square, circle, circle, square?',['ABAB','AABB','ABBA','AAAB'],1),
  ('What comes next? 1, 2, 1, 2, ___',['3','1','2','4'],1),
  ('Creating a pattern means you ___.',['mix things randomly','make a random pile','repeat a rule over and over','count to 10'],2)]),
Sc('Living Things: Animals','Students explore characteristics of animals. All animals move, eat, grow, and produce offspring. They are sorted by habitat and diet.',[
  ('All animals ___.',['make their own food from sunlight','can fly','eat other organisms to get energy','live in water'],2),
  ('An animal that eats only plants is a ___.',['carnivore','herbivore','omnivore','decomposer'],1),
  ('An animal that eats only meat is a ___.',['herbivore','omnivore','carnivore','producer'],2),
  ('A bear that eats both plants and fish is an ___.',['herbivore','carnivore','omnivore','insectivore'],2),
  ('Which is a characteristic all animals share?',['They all fly','They all swim','They all breathe','They all have fur'],2)]),
SS('Our Neighbourhood','Students explore their neighbourhood as a community with homes, parks, stores, schools, and community services close together.',[
  ('A neighbourhood is a ___.',['country','planet','city','small area where people live close together'],3),
  ('Which place would you find in a neighbourhood?',['A mountain range','A desert','A park or playground','An ocean'],2),
  ('What makes a neighbourhood a community?',['The buildings','People sharing the same area and looking out for each other','Only the stores','Only the houses'],1),
  ('A map of a neighbourhood shows ___.',['only countries','where places like homes, schools, and parks are located','only oceans','only mountains'],1),
  ('Why are parks important in a neighbourhood?',['They are not','They give people a place to play, relax, and connect with nature','Only children use them','Only for sports'],1)])]),
day(19,[
L('Letter S','Explore uppercase and lowercase S. Students identify the letter, practise its /s/ sound, and name S words such as sun, snake, and star.',[
  ('Which word starts with S?',['Hat','Bat','Sun','Run'],2),
  ('What sound does S make?',['Shh','Sss','Zzz','Tss'],1),
  ('Find the S word: The ___ shines in the sky.',['Moon','Cloud','Rain','Sun'],3),
  ('Which animal starts with S?',['Dog','Cat','Bird','Snake'],3),
  ('How many S words: sun, moon, star, sky, cloud?',['1','2','3','4'],2)]),
M('Addition to 10','Students add two groups of objects to find the total. They use pictures, counters, and number lines to explore addition.',[
  ('3 + 4 = ?',['5','6','7','8'],2),
  ('How many in all: 2 apples + 5 apples?',['3','6','7','8'],2),
  ('5 + 5 = ?',['9','10','11','8'],1),
  ('What does the + sign mean?',['Take away','Put together / add','Compare','Divide'],1),
  ('1 + 9 = ?',['8','10','11','9'],1)]),
Sc('The Sun and Sky','Students explore the Sun as Earth\'s main source of light and heat. They observe that the sky changes from day to night.',[
  ('The Sun gives Earth ___ and ___.',['cold and dark','light and heat','rain and wind','snow and ice'],1),
  ('The Sun is a ___.',['planet','moon','star','comet'],2),
  ('During the day, the Sun is ___ in the sky.',['invisible','visible (we can see it when skies are clear)','underground','on the horizon only'],1),
  ('At night, the Sun ___.',['is still in the sky in the same place','has moved to the other side of Earth (appears to set)','disappears forever','gets smaller'],1),
  ('Why should you never look directly at the Sun?',['It is dark','It is too cold','Its light can damage your eyes','It is invisible'],2)]),
SS('Canadian Symbols','Students learn about symbols that represent Canada: the maple leaf, beaver, Canadian flag, Parliament Buildings, and the national anthem.',[
  ('What is Canada\'s national symbol on the flag?',['Rose','Beaver','Maple leaf','Moose'],2),
  ('The beaver is a Canadian symbol of ___.',['danger','hard work and industry','beauty','sport'],1),
  ('Canada\'s national anthem is called ___.',['God Save the King','O Canada','Amazing Grace','The Star-Spangled Banner'],1),
  ('Where does Canada\'s federal government meet?',['The CN Tower','Parliament Hill','Niagara Falls','The Rockies'],1),
  ('The colours of the Canadian flag are ___.',['Blue and white','Red, white, and blue','Red and white','Green and gold'],2)])]),
day(20,[
L('Letter T','Explore uppercase and lowercase T. Students identify the letter, practise its /t/ sound, and name T words such as tiger, table, and turtle.',[
  ('Which word starts with T?',['Dog','Cat','Fish','Tiger'],3),
  ('What sound does T make?',['Duh','Tuh','Buh','Kuh'],1),
  ('Find the T word: I sit at a ___ to eat.',['Chair','Desk','Table','Bench'],2),
  ('Which colour starts with T?',['Blue','Teal','Red','Green'],1),
  ('How many T words: tree, flower, turtle, table, apple?',['1','2','3','4'],2)]),
M('Subtraction from 10','Students subtract within 10 using objects, pictures, and number lines. They understand subtraction as taking away.',[
  ('10 - 3 = ?',['6','7','8','9'],1),
  ('8 - 5 = ?',['2','3','4','5'],1),
  ('What does the - sign mean?',['Add','Take away','Put together','Share'],1),
  ('7 - 7 = ?',['7','1','0','14'],2),
  ('6 - 2 = ?',['2','3','4','5'],2)]),
Sc('Air and Wind','Students explore air as a real substance that takes up space, and that moving air is called wind. Wind can be gentle or strong.',[
  ('Moving air is called ___.',['Rain','Wind','Snow','Clouds'],1),
  ('Air takes up ___.',['no space','space (even if we cannot see it)','only a little space','only hot space'],1),
  ('A gentle breeze and a storm are both caused by ___.',['rain','moving air (wind)','the sun heating the ground evenly','no movement'],1),
  ('Which tool measures wind speed?',['Thermometer','Ruler','Anemometer','Scale'],2),
  ('What can wind do?',['Nothing','Move leaves, fly kites, and power windmills','Only feel cold','Only dry laundry'],1)]),
SS('Feelings and Emotions','Students explore a range of emotions and learn healthy ways to express feelings and manage emotions in social situations.',[
  ('A feeling that makes you smile and feel happy inside is ___.',['anger','sadness','joy','fear'],2),
  ('When you feel angry, a healthy response is to ___.',['hit someone','yell loudly','take deep breaths and talk about it','ignore it forever'],2),
  ('Why is it important to talk about your feelings?',['It is not','It helps others understand you and helps you feel better','Only adults talk about feelings','Feelings should always be hidden'],1),
  ('If a friend is sad, you could ___.',['ignore them','laugh at them','ask if they are okay and listen','run away'],2),
  ('Being kind to someone who is upset is called ___.',['arguing','empathy','ignoring','competing'],1)])]),
day(21,[
L('Letter U','Explore uppercase and lowercase U. Students identify the letter, practise its short /u/ sound (umbrella) and long /u/ sound (uniform), and find U words.',[
  ('Which word starts with U?',['Apple','Egg','Umbrella','Ice'],2),
  ('The short U sound is heard in ___.',['Unite','Umbrella','Use','Cube'],1),
  ('Which U word means something you wear?',['Undo','Under','Uniform','Upper'],2),
  ('U is a ___.',['consonant','vowel','number','colour'],1),
  ('Find the U: apple, umbrella, orange, egg',['apple','umbrella','orange','egg'],1)]),
M('Graphs: Bar Graphs','Students create and read simple picture and bar graphs. They answer questions about the data shown.',[
  ('A bar graph uses ___ to show information.',['colours only','bars (rectangles) of different heights','circles','only numbers'],1),
  ('The tallest bar in a bar graph shows the ___ amount.',['smallest','same','largest','unknown'],2),
  ('What question does a graph help answer?',['How does something smell?','How many of each thing are there?','What colour is something?','How heavy is something?'],1),
  ('If 5 kids chose pizza and 3 chose pasta, which bar is taller?',['Pasta','They are equal','Pizza','Cannot tell'],2),
  ('The title of a graph tells you ___.',['how many bars there are','what the graph is about','the exact numbers','the colours used'],1)]),
Sc('Day and Night','Students explore why we have day and night — Earth rotates on its axis, causing each side to face toward or away from the Sun.',[
  ('Day and night are caused by ___.',['the Moon moving','clouds covering the Sun','Earth rotating (spinning) on its axis','the Sun moving around Earth'],2),
  ('When your part of Earth faces the Sun, it is ___.',['night','raining','day','cold'],2),
  ('One full rotation of Earth takes about ___.',['1 hour','24 hours (1 day)','1 month','1 year'],1),
  ('At night, the Sun ___.',['is visible in the sky','is shining on the other side of Earth','disappears','gets cold'],1),
  ('The Moon is best seen at ___.',['noon','daytime','nighttime','sunrise only'],2)]),
SS('Friends and Kindness','Students explore what makes a good friend and practise acts of kindness. They discuss how kind actions make communities happier.',[
  ('A good friend ___.',['always agrees','is kind, listens, and includes others','ignores your feelings','only plays with you if you have toys'],1),
  ('Kindness means ___.',['always winning','saying and doing things that make others feel valued','only sharing food','ignoring others'],1),
  ('If a classmate has no one to play with, you could ___.',['ignore them','laugh at them','invite them to join your game','tell them to find others'],2),
  ('Why is kindness important in a community?',['It is not','It makes everyone feel welcome and valued','Only kind people deserve it','Only some people need kindness'],1),
  ('Which is an act of kindness?',['Taking someone\'s pencil','Pushing in line','Holding the door open for someone','Laughing at a mistake'],2)])]),
day(22,[
L('Letter V','Explore uppercase and lowercase V. Students identify the letter, practise its /v/ sound, and name V words such as van, vest, and vegetables.',[
  ('Which word starts with V?',['Ball','Van','Cat','Door'],1),
  ('What sound does V make?',['Fuh','Vvv','Buh','Wuh'],1),
  ('Find the V word: carrots and ___ are good for you.',['Candy','Chips','Vegetables','Cookies'],2),
  ('Which V word is a type of clothing?',['Van','Vine','Vest','Vase'],2),
  ('How many V words: van, vase, apple, vine, umbrella?',['2','3','4','5'],1)]),
M('2D Shapes Review','Students review circles, squares, triangles, and rectangles. They identify, describe, and sort shapes by their properties.',[
  ('A circle has ___ corners.',['0','1','2','4'],0),
  ('A square has ___ equal sides.',['2','3','4','5'],2),
  ('A triangle has ___ sides.',['2','3','4','5'],1),
  ('Which shape has 4 sides but they are not all equal?',['Square','Circle','Triangle','Rectangle'],3),
  ('A shape with no straight sides and no corners is a ___.',['triangle','square','rectangle','circle'],3)]),
Sc('Plants Need Water and Light','Students investigate what happens to plants without water or light, reinforcing that plants need both to grow.',[
  ('Plants need ___ and ___ to grow.',['ice and darkness','water and sunlight','mud and shade','sand and wind'],1),
  ('What would most likely happen to a plant with no water?',['It grows faster','It stays the same','It wilts and eventually dies','It glows'],2),
  ('Leaves face toward light because ___.',['they are afraid of the dark','plants use sunlight to make food (photosynthesis)','leaves like warmth only','roots need light'],1),
  ('Which part of a plant absorbs water from the soil?',['Leaves','Flowers','Stem','Roots'],3),
  ('Plants make their food using ___.',['soil alone','only water','sunlight, water, and carbon dioxide','only air'],2)]),
SS('Helping at Home','Students explore how family members share responsibilities at home: cooking, cleaning, caring for younger siblings, and yard work.',[
  ('Responsibilities at home are ___.',['only for adults','tasks that all family members share to keep the home running well','only chores for children','optional extras'],1),
  ('Which is an example of helping at home?',['Leaving your toys everywhere','Cleaning up after yourself','Watching TV all day','Eating all the snacks'],1),
  ('Why is it important to share home responsibilities?',['It is not','It teaches children to be responsible and helps the family work as a team','Only adults should work','Only if parents ask'],1),
  ('A chore is ___.',['a type of game','a job you do at home to help the family','a school subject','a type of food'],1),
  ('Which chore could a kindergartener do?',['Pay the bills','Drive to the store','Fix the roof','Put toys away and help set the table'],3)])]),
day(23,[
L('Letter W','Explore uppercase and lowercase W. Students identify the letter, practise its /w/ sound, and name W words such as water, whale, and winter.',[
  ('Which word starts with W?',['Rain','Snow','Water','Ice'],2),
  ('What sound does W make?',['Vvv','Wuh','Buh','Muh'],1),
  ('Find the W: spring, summer, ___, fall',['Autumn','Winter','Rainy','Cold'],1),
  ('Which W word is a large ocean animal?',['Wolf','Worm','Whale','Wasp'],2),
  ('How many W words: well, wall, ball, walk, tall?',['1','2','3','4'],2)]),
M('Measurement: Length','Students use non-standard units (paper clips, blocks) to measure and compare the length of objects. They use terms: longer, shorter, same.',[
  ('Measurement tells you ___.',['the colour of something','how long, tall, or heavy something is','how hot something is','what something smells like'],1),
  ('If you measure a pencil with paper clips, you are using a ___.',['standard unit','non-standard unit','ruler','metre stick'],1),
  ('Which statement about length is correct?',['Longer means shorter','Longer means it takes up more space from end to end','All things are the same length','Shorter means bigger'],1),
  ('To compare two lengths, you should ___.',['guess','line them up at the same starting point','use a scale','smell them'],1),
  ('A book is 8 paper clips long. A pencil is 5 paper clips long. The book is ___.',['shorter','the same length','longer','impossible to compare'],2)]),
Sc('Animals in Winter','Students learn how animals survive winter: some hibernate, some migrate south, and some stay active by adapting their behaviour.',[
  ('Hibernation means ___.',['flying south for winter','sleeping deeply through winter to save energy','growing a thicker coat','building a nest'],1),
  ('Which animal is known for hibernating in winter?',['Goose','Butterfly','Bear','Robin'],2),
  ('Migration means ___.',['sleeping through winter','growing thicker fur','travelling to a warmer place for winter','staying and being active'],2),
  ('Which bird migrates south in autumn?',['Owl','Chickadee','Canada Goose','Crow'],2),
  ('Some animals grow thicker fur in winter to ___.',['look better','keep warm','find food faster','swim better'],1)]),
SS('Weather and Our Lives','Students explore how weather affects daily decisions: what to wear, what activities to do, and how communities prepare for extreme weather.',[
  ('Weather affects what we ___.',['eat for breakfast','wear and what activities we do','dream about','read'],1),
  ('On a rainy day you would wear ___.',['a swimsuit','a t-shirt and shorts','a raincoat and boots','nothing different'],2),
  ('Extreme weather like a blizzard can ___.',['have no impact','cause school closures and road dangers','only affect farms','only affect the sky'],1),
  ('A weather forecast helps people ___.',['predict the future','plan and prepare for upcoming weather','control the weather','make it rain'],1),
  ('Which job involves predicting the weather?',['Baker','Meteorologist','Plumber','Librarian'],1)])]),
day(24,[
L('Letter X','Explore uppercase and lowercase X. Students identify the letter, practise its /ks/ sound, and note that X rarely starts words in English.',[
  ('What sound does X usually make?',['Zuh','Ks (as in fox)','Sh','Tuh'],1),
  ('X is found at the ___ of most English words.',['beginning','middle or end','never','only at the start'],1),
  ('Which word has an X?',['Dog','Cat','Fox','Bird'],2),
  ('An X on a map often marks ___.',['water','mountains','a special or buried location','a road'],2),
  ('Which word ends in X?',['Ball','Box','Bat','Bag'],1)]),
M('Measurement: Capacity','Students compare the capacity (how much a container holds) using non-standard units. They use terms: more, less, same.',[
  ('Capacity means ___.',['how heavy something is','how much a container can hold','how long something is','how hot something is'],1),
  ('A bucket holds ___ water than a cup.',['less','the same','more','no'],2),
  ('If you fill a small jar and a big jar with water, the big jar holds ___.',['less','the same','more','nothing'],2),
  ('To compare capacity you could ___.',['weigh the containers','count the containers','fill each with water and compare','smell them'],2),
  ('Which holds the most: a teaspoon, a cup, or a pot?',['Teaspoon','Cup','Pot','They are all equal'],2)]),
Sc('Properties of Water','Students explore water as a liquid that takes the shape of its container, that it freezes into solid ice and evaporates into invisible vapour.',[
  ('Water is a ___.',['solid','gas','liquid at room temperature','powder'],2),
  ('When water freezes it becomes ___.',['gas','vapour','liquid','solid ice'],3),
  ('When water evaporates it becomes ___.',['solid','heavier','invisible water vapour (gas)','coloured'],2),
  ('Water takes the shape of ___.',['its original form only','its container','a ball always','a flat sheet always'],1),
  ('Which temperature turns liquid water into ice?',['Above 0°C','At 0°C (or below)','At 100°C','At 50°C'],1)]),
SS('My Country: Canada','Students explore Canada as their country: its size, capital city, official languages, and symbols that make it unique.',[
  ('Canada is located in ___.',['South America','Europe','Africa','North America'],3),
  ('Canada\'s capital city is ___.',['Toronto','Montreal','Ottawa','Vancouver'],2),
  ('Canada has ___ official languages.',['1','2','3','4'],1),
  ('What are Canada\'s official languages?',['Spanish and English','French and English','Italian and French','English and Chinese'],1),
  ('Canada is the ___ largest country in the world by area.',['1st','2nd','3rd','5th'],1)])]),
day(25,[
L('Letter Y','Explore uppercase and lowercase Y. Students identify the letter, practise its /y/ sound, and name Y words such as yak, yarn, and yes.',[
  ('Which word starts with Y?',['Zoo','Fox','Yak','Ant'],2),
  ('What sound does Y make at the start of a word?',['Wuh','Yuh','Juh','Iuh'],1),
  ('Find the Y: The answer is ___, not no.',['Maybe','Yes','No','Perhaps'],1),
  ('Which Y word is something you knit with?',['Yam','Year','Yarn','Yard'],2),
  ('How many Y words: yes, year, no, yesterday, red?',['1','2','3','4'],1)]),
M('Numbers to 20: Addition and Subtraction','Students add and subtract within 20 using number lines, counters, and mental strategies.',[
  ('12 + 5 = ?',['16','17','18','15'],1),
  ('18 - 4 = ?',['12','13','14','15'],2),
  ('What is 10 + 7?',['16','17','18','15'],1),
  ('20 - 9 = ?',['10','11','12','13'],1),
  ('A number line helps you ___.',['measure weight','add and subtract by counting forward and backward','find shapes','measure temperature'],1)]),
Sc('Insects','Students explore characteristics of insects: 6 legs, 3 body parts (head, thorax, abdomen), and often wings. Common Ontario insects are identified.',[
  ('All insects have ___ legs.',['4','6','8','10'],1),
  ('The three body parts of an insect are head, thorax, and ___.',['wing','tail','abdomen','shell'],2),
  ('Which is an insect?',['Spider','Worm','Butterfly','Centipede'],2),
  ('A spider is NOT an insect because it has ___ legs.',['6','8','4','10'],1),
  ('Which Ontario insect is known for its orange and black wings?',['Bumblebee','Monarch butterfly','Firefly','Dragonfly'],1)]),
SS('Exploring Our Differences and Similarities','Students celebrate diversity by exploring how people are alike and different in appearance, language, food, and traditions.',[
  ('People from different cultures may have different ___.',['Only food','Only language','Languages, foods, celebrations, and traditions','Only names'],2),
  ('Celebrating our differences helps us ___.',['fight more','feel confused','learn from and respect each other','stay separate'],2),
  ('Which is a way people are similar across all cultures?',['They all eat the same food','They all look the same','They all have families, feelings, and a need to belong','They all speak English'],2),
  ('Diversity in a classroom means ___.',['everyone is the same','everyone has the exact same background','students come from different backgrounds and experiences','only one culture is represented'],2),
  ('Why is it important to learn about other cultures?',['It is not','It builds empathy and understanding','Only for geography class','Only for adults'],1)])]),
day(26,[
L('Letter Z','Explore uppercase and lowercase Z. Students identify the letter, practise its /z/ sound, and name Z words such as zebra, zero, and zip.',[
  ('Which word starts with Z?',['Animal','Bee','Zebra','Dog'],2),
  ('What sound does Z make?',['Sss','Zzz','Tuh','Shh'],1),
  ('Find the Z: The number that means nothing is ___.',['One','Ten','Zero','Two'],2),
  ('Which Z word is a striped animal?',['Zap','Zip','Zebra','Zone'],2),
  ('Z is the ___ letter of the English alphabet.',['1st','13th','25th','26th'],3)]),
M('Sorting 3D Shapes','Students identify and sort 3D shapes: sphere, cube, cylinder, and cone. They describe them using faces, edges, and vertices.',[
  ('A sphere looks like ___.',['a box','a ball','a can','a cone'],1),
  ('A cube has ___ flat faces.',['4','5','6','8'],2),
  ('A cylinder has ___ flat circular faces.',['0','1','2','3'],2),
  ('Which 3D shape comes to a point at the top?',['Sphere','Cube','Cylinder','Cone'],3),
  ('Which 3D shape can roll?',['Cube','Cone and sphere','Only sphere','Rectangle'],1)]),
Sc('Taking Care of Our Environment','Students learn about littering and waste, and simple actions to protect the environment: picking up litter, reducing waste, and recycling.',[
  ('Litter means ___.',['recycled material','waste thrown on the ground instead of in a bin','a type of animal home','a bed for kittens only'],1),
  ('Recycling means ___.',['throwing everything away','using objects again or making them into new things','burning waste','ignoring waste'],1),
  ('Which action helps the environment?',['Leaving garbage in a park','Picking up litter','Wasting water','Leaving lights on all night'],1),
  ('The three Rs are Reduce, Reuse, and ___.',['Recycle','Refuse','Rotate','Reach'],0),
  ('Why is it important to look after the environment?',['It is not','We share the planet with all living things and must keep it healthy','Only scientists care','Only for adults'],1)]),
SS('All About Me: Reflection','Students reflect on their learning through the year, identifying what they have learned, how they have grown, and what they are proud of.',[
  ('Reflecting on your learning means ___.',['ignoring what happened','thinking about what you learned and how you grew','copying someone else','only thinking about bad things'],1),
  ('I am most proud when ___.',['I give up','I try my best and do not give up','I do nothing','I copy others'],1),
  ('Something new I learned this year is ___.',['Nothing','How to read new words, count higher, and learn about the world','Only my name','Only colours'],1),
  ('A goal for next year could be ___.',['To do nothing new','To try something harder and keep learning','To never make mistakes','To stop reading'],1),
  ('Learning is ___.',['only at school','only from books','something that happens everywhere and every day','only from teachers'],2)])]),
day(27,[
L('Reading: Simple Sentences','Students read and understand simple sentences. They identify the naming part (who or what) and the action part (what they do).',[
  ('A sentence has a naming part and an ___ part.',['eating','describing','action','colouring'],2),
  ('In "The cat runs fast," the naming part is ___.',['runs','fast','The cat','fast and runs'],2),
  ('In "The dog jumps high," the action part is ___.',['The dog','jumps high','high','The'],1),
  ('A complete sentence needs ___.',['only a noun','only a verb','a naming part (noun) and an action part (verb)','only adjectives'],2),
  ('Which is a complete sentence?',['The big red.','Runs fast.','The bird sings.','Jumping high quickly.'],2)]),
M('Counting Back: Subtraction','Students use counting back as a strategy for subtraction within 20.',[
  ('To subtract 3 from 9, count back 3 from 9. Answer = ?',['5','6','7','8'],1),
  ('10 - 4: count back 4 from 10. Answer = ?',['5','6','7','8'],1),
  ('15 - 3 = ?',['10','11','12','13'],2),
  ('Counting back means you count in which direction?',['Forward (up)','Backward (down)','Sideways','Randomly'],1),
  ('Which strategy helps with subtraction?',['Adding more','Counting back from the starting number','Multiplication','Dividing'],1)]),
Sc('Materials Around Us','Students explore everyday materials (wood, plastic, metal, fabric, glass) and their properties such as hard, soft, bendy, and transparent.',[
  ('Wood is usually described as ___.',['soft and bendy','transparent','hard and solid','liquid'],2),
  ('Which material lets light through (is transparent)?',['Wood','Metal','Glass','Fabric'],2),
  ('Fabric is usually ___.',['hard and rigid','soft and flexible','transparent','liquid'],1),
  ('Which material is a good conductor of electricity?',['Wood','Glass','Metal','Rubber'],2),
  ('We choose materials based on their ___.',['colour only','size only','properties (what they are like and what they can do)','weight only'],2)]),
SS('Special Days and Celebrations','Students explore special days celebrated in their community and around the world, recognising that different cultures celebrate in unique ways.',[
  ('A celebration is ___.',['a type of food','a special occasion that people mark with activities','a type of building','a school subject'],1),
  ('Which is a Canadian celebration?',['Diwali (Hindu/Sikh)','Canada Day (July 1)','Eid al-Fitr (Islamic)','Chinese New Year'],1),
  ('Why do different cultures celebrate differently?',['They do not','Each culture has unique traditions, histories, and values that shape its celebrations','Only one way is correct','All celebrations are the same'],1),
  ('Learning about others\' celebrations helps us ___.',['feel confused','respect and appreciate different cultures','ignore diversity','stay only with our own culture'],1),
  ('What is Diwali known as?',['Festival of Colour','Festival of Lights','Festival of Music','Festival of Food'],1)])]),
day(28,[
L('Writing: My Favourite Thing','Students practise simple sentence writing about a personal favourite topic, using a capital letter, words, and a period.',[
  ('A sentence starts with a ___ letter.',['lowercase','capital (uppercase)','random','number'],1),
  ('A sentence ends with a ___.',['comma','capital letter','period, question mark, or exclamation mark','slash'],2),
  ('Which is written correctly?',['my dog is fluffy.','My dog is fluffy.','my Dog is fluffy.','My dog is Fluffy'],1),
  ('When writing about your favourite thing, a good first sentence ___.',['says nothing','tells what your favourite thing is and why you like it','lists random words','asks a question with no answer'],1),
  ('A picture can help your reader ___.',['add more letters','understand your writing better','change your topic','erase your work'],1)]),
M('Number Stories','Students create and solve simple addition and subtraction number stories using pictures and equations.',[
  ('A number story is ___.',['a book about numbers','a maths problem described in words','only about counting','a fairy tale'],1),
  ('There are 3 birds on a branch. 2 more land. How many now?',['3','4','5','6'],2),
  ('I had 7 cookies. I ate 3. How many are left?',['3','4','5','6'],1),
  ('Which equation matches: 4 ducks plus 2 ducks?',['4 - 2 = 2','4 + 2 = 6','4 x 2 = 8','6 - 2 = 4'],1),
  ('A number story always includes ___.',['a character, a problem, and a number answer','only an equation','only a picture','only letters'],0)]),
Sc('Living and Non-Living Review','Students review the differences between living things (grow, breathe, reproduce, respond) and non-living things (do not do these things).',[
  ('Living things can ___.',['fly always','grow, breathe, and reproduce','glow in the dark','never change'],1),
  ('A rock is non-living because it ___.',['breathes','grows','reproduces','does not grow, breathe, or reproduce'],3),
  ('Which is a living thing?',['A chair','A cloud','A tree','A book'],2),
  ('A non-living thing ___.',['grows on its own','needs food and water to survive','does not grow, breathe, or reproduce on its own','has feelings'],2),
  ('Which is the best example of a non-living thing?',['Fish','Flower','Water','Mushroom'],2)]),
SS('Caring for the Earth','Students review environmental responsibility: conserving water, reducing waste, protecting animals and plants, and making choices that help the planet.',[
  ('Conserving water means ___.',['using as much water as possible','wasting water daily','using water carefully and not wasting it','only drinking water'],2),
  ('Which action helps protect the Earth?',['Leaving taps running','Throwing litter in parks','Turning off lights when leaving a room','Buying more plastic bags'],2),
  ('Protecting habitats helps ___.',['only humans','the animals and plants that live there','nobody','only farmers'],1),
  ('Why should we reduce waste?',['Waste is good','Less waste means less pollution and a healthier planet','Only adults need to reduce waste','Waste helps plants grow'],1),
  ('One thing a child can do to help the Earth is ___.',['Drive a car','Use less plastic and recycle where possible','Move to another planet','Wait for adults to fix everything'],1)])]),
day(29,[
L('Rhyming Words','Students identify and generate rhyming words. Rhyming words have the same ending sound (e.g., cat/hat, dog/log, play/day).',[
  ('Rhyming words have the same ___.',['beginning sound','middle sound','ending sound','number of letters'],2),
  ('Which word rhymes with CAT?',['Dog','Hat','Cup','Sun'],1),
  ('Which word rhymes with SUN?',['Moon','Star','Fun','Sky'],2),
  ('Which pair of words rhymes?',['Dog/Cat','Ball/Bat','Play/Day','Sun/Moon'],2),
  ('If CAKE rhymes with LAKE, which also rhymes?',['Like','Bike','Make','Milk'],2)]),
M('Counting to 100 by 2s and 5s','Students count forward by 2s and 5s to 100, building number sense and a foundation for multiplication.',[
  ('Count by 2s: 2, 4, 6, ___, 10',['7','8','9','11'],1),
  ('Count by 5s: 5, 10, 15, ___',['16','18','20','25'],2),
  ('Count by 2s: 14, 16, ___',['17','18','19','20'],1),
  ('Count by 5s: 25, 30, ___',['33','35','40','45'],1),
  ('Counting by 2s gives you only ___ numbers.',['odd','even','random','prime'],1)]),
Sc('Science Review: All Strands','Students review life science (plants, animals), earth science (seasons, weather), and physical science (forces, materials).',[
  ('Plants make food using ___, water, and carbon dioxide.',['Soil','Sunlight','Fertilizer','Rain'],1),
  ('Animals need food, water, shelter, and ___ to survive.',['Toys','Air','Television','Money'],1),
  ('The four seasons in Ontario are ___.',['Hot, cold, wet, dry','Spring, summer, fall, winter','North, south, east, west','Day, night, dawn, dusk'],1),
  ('A push and a pull are both types of ___.',['weather','patterns','forces','materials'],2),
  ('Which is a property of metal?',['Soft and bendy','Transparent','Usually hard and conducts electricity','Light as a feather'],2)]),
SS('Social Studies Review','Students review communities, Canadian geography, symbols, seasons, and citizenship topics covered through the year.',[
  ('What is the capital city of Canada?',['Toronto','Vancouver','Ottawa','Montreal'],2),
  ('A community is ___.',['a type of animal','a group of people living and working together in an area','only a city','only a village'],1),
  ('Which is a Canadian symbol?',['Eiffel Tower','Bald Eagle','Maple leaf','Statue of Liberty'],2),
  ('Being a good citizen means ___.',['only following rules you like','following laws, helping others, and respecting the community','never helping anyone','only thinking about yourself'],1),
  ('Canada has ___ official languages.',['1','2','3','4'],1)])]),
day(30,[
L('Alphabet Review and Simple Reading','Students review all 26 letters, their sounds, and demonstrate early reading of simple CVC (consonant-vowel-consonant) words.',[
  ('How many letters are in the English alphabet?',['24','25','26','27'],2),
  ('Which is a vowel?',['B','C','D','E'],3),
  ('A CVC word has ___ letters.',['2','3','4','5'],1),
  ('Which is a CVC word?',['Street','Cat','Play','Bring'],1),
  ('Reading means ___.',['colouring pictures','turning letters into words and understanding their meaning','only looking at books','only writing'],1)]),
M('Year Review: Math','Students review all Kindergarten math concepts: counting, shapes, patterns, measurement, and addition/subtraction.',[
  ('Count: How many in 3 + 4?',['5','6','7','8'],2),
  ('What shape has 4 equal sides?',['Triangle','Circle','Rectangle','Square'],3),
  ('What comes next? 2, 4, 6, ___',['7','8','9','10'],1),
  ('8 - 3 = ?',['4','5','6','7'],1),
  ('Which is longer: a desk or a pencil?',['Pencil','Desk','They are the same','Cannot tell'],1)]),
Sc('Year Review: Science','Students review all Kindergarten science: living and non-living, plants, animals, seasons, weather, forces, and materials.',[
  ('A plant is a ___ thing.',['non-living','living','neither','both'],1),
  ('Animals need food, water, shelter, and air. These are called ___.',['Wants','Needs','Options','Extras'],1),
  ('Which season is it when leaves fall off trees?',['Spring','Summer','Fall/Autumn','Winter'],2),
  ('A push and pull are types of ___.',['weather','forces','patterns','materials'],1),
  ('Which material is transparent (see-through)?',['Wood','Metal','Glass','Rubber'],2)]),
SS('Year Review: Social Studies and Citizenship','Students review community helpers, Canadian symbols, rights and responsibilities, celebrations, and caring for the Earth.',[
  ('Who helps keep you healthy by giving check-ups?',['Teacher','Doctor','Librarian','Caretaker'],1),
  ('What symbol appears on the Canadian flag?',['Eagle','Maple leaf','Beaver','Moose'],1),
  ('A right is something you ___.',['must give to others','are allowed to do or have','can take from others','never earn'],1),
  ('Why is recycling important?',['It is not','It reduces waste and protects the environment','Only for adults','Only for scientists'],1),
  ('A good citizen ___.',['ignores community rules','respects others, follows rules, and helps the community','only cares about themselves','never votes'],1)])]),
]

write_new(0, g0)
print('Grade 0 (30 days) done.')
