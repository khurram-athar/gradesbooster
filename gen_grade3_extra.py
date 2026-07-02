#!/usr/bin/env python3
import sys
sys.path.insert(0,'/sessions/wonderful-keen-tesla/mnt/gradesbooster')
from gen_curriculum import sub,day,append_to

L3='https://tvolearn.com/pages/grade-3-language'
M3='https://tvolearn.com/pages/grade-3-mathematics'
S3='https://tvolearn.com/pages/grade-3-science-and-technology'
SS3='https://tvolearn.com/pages/grade-3-social-studies'
RL,RM,RS,RSS='TVO Learn: Grade 3 Language','TVO Learn: Grade 3 Mathematics','TVO Learn: Grade 3 Science & Technology','TVO Learn: Grade 3 Social Studies'

def L(t,s,q): return sub('Language',t,s,RL,L3,q)
def M(t,s,q): return sub('Math',t,s,RM,M3,q)
def Sc(t,s,q): return sub('Science',t,s,RS,S3,q)
def SS(t,s,q): return sub('SocialStudies',t,s,RSS,SS3,q)

g3=[
day(16,[
L('Grammar: Verb Tenses','Grade 3 Language strand: verbs change form to show past (walked), present (walks), and future (will walk) tense. Recognising tense helps readers understand when events happen.',[
  ('A verb in PAST tense shows something that ___.',['is happening now','will happen','already happened','might happen'],2),
  ('Which is a PRESENT tense verb?',['walked','will walk','runs','ran'],2),
  ('Which is a PAST tense verb?',['jump','jumped','will jump','jumping'],1),
  ('The FUTURE tense uses the word ___.',['was','is','will','had'],2),
  ('Change to past tense: "She plays outside."',['She will play outside.','She played outside.','She is playing outside.','She plays outside.'],1)]),
M('Multiplication: Groups Of','Grade 3 Number strand: multiplication means adding equal groups. 3 × 4 means 3 groups of 4. Students use arrays and repeated addition to understand multiplication.',[
  ('3 × 4 means ___.',['3 + 4','3 groups of 4','4 groups of 3 only','3 - 4'],1),
  ('What is 2 × 5?',['7','8','10','12'],2),
  ('An array with 3 rows and 4 columns shows ___ × ___ = ___.',['3 × 4 = 12','4 × 3 = 7','2 × 6 = 12','3 + 4 = 7'],0),
  ('6 × 1 = ?',['0','1','6','7'],2),
  ('Which repeated addition equals 4 × 3?',['4+4+4','3+3+3+3','4+3','4×4×4'],1)]),
Sc('Forces: Magnets','Grade 3 Science Physical strand: magnets attract iron and steel objects and repel other magnets at the same pole. Students explore attraction, repulsion, and magnetic fields.',[
  ('Magnets attract objects made of ___.',['plastic and glass','iron and steel','wood and paper','rubber and fabric'],1),
  ('When two magnets face North-to-North they ___.',['attract','repel (push away)','stick permanently','do nothing'],1),
  ('Opposite poles of two magnets ___.',['repel','attract','cancel out','do nothing'],1),
  ('Which item is attracted to a magnet?',['A wooden stick','A glass bottle','A steel paper clip','A rubber eraser'],2),
  ('A magnetic field is ___.',['only visible in space','the area around a magnet where magnetic force acts','the magnet itself','a type of electricity'],1)]),
SS('Urban and Rural Communities','Grade 3 Social Studies: communities can be urban (cities, many people, many services) or rural (countryside, fewer people, farming). Each has unique features.',[
  ('An urban community is usually ___.',['a small farm area','a large city with many people and services','a forest with no people','a single street'],1),
  ('A rural community is usually ___.',['a busy city','a suburb only','a town or countryside area with fewer people, often with farming','a coastal city'],2),
  ('Which is more likely found in a rural community?',['Skyscrapers','Subway systems','Large farms and open land','Airports'],2),
  ('Which is more likely found in an urban community?',['Very few people','Large farms','Public transit and tall buildings','Dirt roads'],2),
  ('Both urban and rural communities ___.',['have no schools','have hospitals only','have people with needs, goods, and services','are the same size'],2)])]),
day(17,[
L('Reading: Summarising','Grade 3 Reading strand: a summary briefly states the most important ideas in a text. It is shorter than the original and uses your own words, not opinions.',[
  ('A summary is ___.',['a copy of the whole text','a long detailed retelling','a brief restatement of main ideas in your own words','your personal opinion'],2),
  ('A good summary does NOT include ___.',['the main idea','key events','your personal opinion','important details'],2),
  ('Why is summarising useful?',['It makes reading longer','It helps you understand and remember the key points','It replaces reading','It is only for book reports'],1),
  ('Which is the best summary of a story about a lost dog found by a child?',['I liked this story.','A child found a lost dog and returned it to its owner.','There was a dog. It was brown. It was lost. A child was walking. The child saw the dog. The dog was happy.','Dogs are wonderful pets.'],1),
  ('When summarising, you should ___.',['include every detail','copy exactly','focus on main ideas and leave out minor details','add new information'],2)]),
M('Multiplication: Facts to 5×5','Grade 3 Number strand: students recall multiplication facts to 5×5 fluently. Strategies include skip counting, arrays, and recognising patterns.',[
  ('4 × 5 = ?',['15','18','20','25'],2),
  ('3 × 3 = ?',['6','9','12','15'],1),
  ('5 × 5 = ?',['20','25','30','35'],1),
  ('2 × 4 = ?',['6','8','10','12'],1),
  ('Which multiplication fact equals 12?',['2 × 5','3 × 4','4 × 4','5 × 3'],1)]),
Sc('Forces: Gravity','Grade 3 Science Physical strand: gravity is the force that pulls objects toward Earth. Objects fall because of gravity; heavier objects need more force to lift.',[
  ('Gravity is a force that pulls objects ___.',['upward','sideways','toward the centre of Earth (downward)','in circles'],2),
  ('What would happen to a ball if there were no gravity?',['It would fall faster','It would stay in place or float away','It would get heavier','It would explode'],1),
  ('Gravity acts on ___.',['only heavy objects','only light objects','all objects with mass','only metal objects'],2),
  ('If you drop a ball from a height, gravity makes it ___.',['stay in place','fly up','fall toward the ground','move sideways'],2),
  ('Gravity on Earth is ___ gravity on the Moon.',['weaker than','equal to','stronger than','the same as'],2)]),
SS('Urban Services vs Rural Services','Grade 3 Social Studies: urban communities have dense public services (transit, hospitals, many stores); rural communities rely more on personal vehicles and may travel further for services.',[
  ('Which service is MORE commonly found in urban areas?',['Individual wells','Subway/bus transit systems','Dirt roads','Large wheat farms'],1),
  ('In a rural area, people often travel ___ for services like hospitals.',['shorter distances','the same distance','longer distances','no distance (they are always nearby)'],2),
  ('Which is a service found in BOTH urban and rural communities?',['Subway trains','Skyscrapers','Schools and emergency services','Major international airports'],2),
  ('A major advantage of urban living is ___.',['more open space','less noise','more access to services and transit','lower cost of living always'],1),
  ('A major advantage of rural living is ___.',['more services','more public transit','more open space, nature, and often lower cost of living','more cultural events always'],2)])]),
day(18,[
L('Writing: Personal Narrative','Grade 3 Writing strand: a personal narrative tells a true story from the writer\'s own life. It uses first person (I, me, my), includes feelings, and follows a sequence of events.',[
  ('A personal narrative is written from the ___ person point of view.',['second','third','first (I, me, my)','fourth'],2),
  ('A personal narrative tells ___.',['a made-up story','a true story from the writer\'s own experience','a report about science','another person\'s biography'],1),
  ('Which sentence belongs in a personal narrative?',['The character felt happy.','She walked to school.','I felt so excited when I opened my birthday gift!','Studies show that exercise is healthy.'],2),
  ('Personal narratives include ___.',['only dialogue','the writer\'s feelings and personal reactions','only facts without feelings','step-by-step instructions'],1),
  ('A good personal narrative has a clear ___, middle, and end.',['question','beginning','number','argument'],1)]),
M('Division: Sharing Equally','Grade 3 Number strand: division means sharing a total into equal groups. 12 ÷ 3 = 4 means 12 shared equally among 3 gives 4 each.',[
  ('12 ÷ 3 = ?',['3','4','5','6'],1),
  ('Division means ___.',['adding groups','taking away one','sharing into equal groups','multiplying'],2),
  ('If 10 apples are shared equally among 5 children, each child gets ___.',['1','2','3','5'],1),
  ('15 ÷ 5 = ?',['2','3','4','5'],1),
  ('If 4 × 3 = 12, then 12 ÷ 4 = ?',['2','3','4','5'],1)]),
Sc('Simple Machines: Levers','Grade 3 Science Physical strand: a lever is a simple machine with a rigid bar and a fulcrum (pivot point) that makes lifting easier. Examples: seesaw, bottle opener.',[
  ('A lever has a rigid bar and a ___ (pivot point).',['wheel','pulley','fulcrum','gear'],2),
  ('Moving the fulcrum closer to the load makes it ___ to lift.',['harder','impossible','easier','the same'],2),
  ('Which is an example of a lever?',['A wheel on an axle','A ramp','A seesaw','A pulley system'],2),
  ('Levers help by ___.',['making objects heavier','reducing the force needed to move a load','making work impossible','only moving objects sideways'],1),
  ('Which everyday object uses a lever?',['A water slide','A bottle opener or scissors','A spinning wheel','A car wheel'],1)]),
SS('Economic Interdependence','Grade 3 Social Studies: communities depend on each other for goods and services. Trade links rural (food, raw materials) and urban (manufactured goods, services) communities.',[
  ('Economic interdependence means ___.',['communities can survive completely alone','communities depend on each other for goods and services','only cities need trade','only farms need trade'],1),
  ('A rural community might trade ___ with an urban community.',['factory goods','food and raw materials','banking services','concerts and museums'],1),
  ('An urban community might provide a rural community with ___.',['wheat and dairy','manufactured goods, hospitals, and financial services','forests and rivers','only tourism'],1),
  ('Why can no community be completely self-sufficient today?',['They can — communities need nothing from outside','It would take too much specialised labour and resources','Only small communities need others','Only urban communities need trade'],1),
  ('Trade between communities benefits ___.',['only sellers','only buyers','both communities involved','only the government'],2)])]),
day(19,[
L('Vocabulary: Synonyms and Antonyms','Grade 3 Language strand: synonyms are words with similar meanings; antonyms have opposite meanings. Rich vocabulary improves writing and reading comprehension.',[
  ('A synonym for "happy" is ___.',['sad','angry','joyful','tired'],2),
  ('An antonym for "brave" is ___.',['courageous','fearless','bold','cowardly'],3),
  ('Which pair are synonyms?',['hot/cold','fast/quick','big/small','day/night'],1),
  ('Which pair are antonyms?',['large/big','fast/quick','loud/quiet','happy/joyful'],2),
  ('Using synonyms in writing helps you ___.',['confuse the reader','avoid repeating the same words and vary your language','shorten your writing','change your topic'],1)]),
M('Fractions: Halves, Thirds, Quarters','Grade 3 Number strand: fractions represent equal parts of a whole. One half = 1/2, one third = 1/3, one quarter = 1/4. The denominator shows equal parts.',[
  ('1/2 means ___.',['one of three equal parts','one of two equal parts','two of one equal part','half of the denominator'],1),
  ('A pizza divided into 4 equal slices — one slice = ___.',['1/3','1/4','1/2','2/4'],1),
  ('Which fraction is the largest?',['1/4','1/3','1/2','1/8'],2),
  ('If a shape is divided into 3 equal parts and 1 part is shaded, the fraction is ___.',['1/2','1/4','1/3','3/1'],2),
  ('The bottom number of a fraction tells you ___.',['how many parts are selected','the total number of equal parts','the size of each part','the name of the fraction'],1)]),
Sc('Simple Machines: Inclined Planes and Wedges','Grade 3 Science Physical strand: an inclined plane (ramp) reduces force needed to raise a load. A wedge is two inclined planes joined — used for splitting or holding.',[
  ('An inclined plane is also called a ___.',['lever','pulley','ramp','gear'],2),
  ('An inclined plane makes work easier by ___.',['increasing the load','reducing the force needed to raise something by spreading it over a longer distance','making objects heavier','reversing direction of force only'],1),
  ('A wedge is formed by ___.',['one inclined plane','two inclined planes joined together','a lever and a fulcrum','a pulley and rope'],1),
  ('Which is an example of a wedge?',['A ramp','An axe blade or door stopper','A seesaw','A pulley'],1),
  ('Which is an example of an inclined plane?',['A bottle opener','A pair of scissors','A loading ramp','A wheel'],2)]),
SS('Indigenous Communities in Canada','Grade 3 Social Studies: Indigenous peoples have lived in Canada for thousands of years. Their communities have distinct cultures, languages, and relationships with the land.',[
  ('Indigenous peoples of Canada ___.',['arrived recently','have lived in Canada for thousands of years','are all the same','have only one language'],1),
  ('Indigenous communities in Canada ___.',['are all the same culture','have diverse languages, traditions, and relationships with their land','have no distinct culture','are found only in one province'],1),
  ('Traditional Indigenous knowledge often focuses on ___.',['ignoring nature','a deep understanding of and respect for the land and all living things','only one topic','only farming'],1),
  ('Why is learning about Indigenous cultures important?',['It is not important','They are a vital part of Canada\'s history and identity that enriches all Canadians','Only in Ontario','Only for adults'],1),
  ('Reconciliation in Canada refers to ___.',['ignoring the past','building respectful relationships and repairing harm done to Indigenous peoples','only money','only a political debate'],1)])]),
day(20,[
L('Reading: Non-Fiction Text Features','Grade 3 Reading strand: non-fiction texts include features that help readers navigate and understand: headings, captions, diagrams, glossary, index, table of contents.',[
  ('A table of contents helps readers ___.',['define difficult words','understand captions','find the page numbers of sections','make a prediction'],2),
  ('A caption in a non-fiction text ___.',['explains what an illustration or photograph shows','introduces the whole book','is the author\'s name','asks a question'],0),
  ('A glossary provides ___.',['page numbers','an index','definitions of key terms used in the book','a summary of the whole book'],2),
  ('A diagram in non-fiction usually includes ___.',['only colours','labels that identify parts of what is shown','a plot outline','opinions only'],1),
  ('Why do non-fiction texts include these features?',['To make the book longer','To help readers find, understand, and navigate information more easily','Only for decoration','Only for younger readers'],1)]),
M('Measurement: Perimeter','Grade 3 Measurement strand: perimeter is the distance around the outside of a shape. Add all side lengths to find the perimeter.',[
  ('Perimeter is the distance ___.',['inside a shape','around the outside of a shape','between two points','above a shape'],1),
  ('A rectangle is 5 cm long and 3 cm wide. Perimeter = ?',['8 cm','15 cm','16 cm','10 cm'],2),
  ('A square has sides of 4 cm each. Perimeter = ?',['4 cm','8 cm','12 cm','16 cm'],3),
  ('To find perimeter, you ___.',['multiply length × width','add all the side lengths','divide the area','count the corners'],1),
  ('Perimeter is measured in ___ units.',['square','cubic','linear (cm, m)','weight'],2)]),
Sc('Soil and Erosion','Grade 3 Science Earth strand: soil is made of rock particles, organic matter, air, and water. Erosion is the wearing away of soil by wind and water.',[
  ('Soil is made of ___.',['only sand','only clay','rock particles, organic matter, air, and water','plastic and glass'],2),
  ('Erosion is ___.',['growing plants','the wearing away of soil by wind, water, or ice','adding nutrients to soil','a type of rock'],1),
  ('Which action INCREASES erosion?',['Planting trees','Covering soil with vegetation','Leaving soil bare and uncovered','Building raised garden beds'],2),
  ('How do plant roots help prevent erosion?',['They do not','They hold soil in place','They increase water runoff','They dry out the soil'],1),
  ('Topsoil is important for farming because ___.',['it is the hardest layer','it is where bedrock forms','it is richest in nutrients for growing plants','it contains the most rocks'],2)]),
SS('Mapping: Cardinal Directions','Grade 3 Social Studies: cardinal directions (North, South, East, West) and intermediate directions (NE, NW, SE, SW) help us navigate maps and describe locations.',[
  ('The four cardinal directions are ___.',['Up, Down, Left, Right','N, S, E, W','NE, NW, SE, SW','High, Low, Far, Near'],1),
  ('On a standard map, North is usually at the ___.',['bottom','left side','right side','top'],3),
  ('East is opposite to ___.',['North','South','West','Up'],2),
  ('A compass rose on a map shows ___.',['temperature','the direction of north and other directions','the distance scale','population'],1),
  ('NW stands for ___.',['North-West','Northern Way','Near West','No Wind'],0)])]),
day(21,[
L('Writing: Descriptive Writing','Grade 3 Writing strand: descriptive writing uses sensory details (sight, sound, smell, touch, taste) and precise language to create a vivid picture for the reader.',[
  ('Descriptive writing creates a clear picture using ___.',['only facts','only numbers','sensory details and vivid language','only dialogue'],2),
  ('Sensory details describe what you can ___.',['count','see, hear, smell, feel, and taste','only see','only touch'],1),
  ('Which is more descriptive?',['The flower was nice.','The velvet-soft purple flower smelled like honey.','I saw a flower.','The flower was there.'],1),
  ('Vivid adjectives make writing ___.',['harder to understand','more specific and engaging','shorter','less interesting'],1),
  ('Which word is more precise than "said"?',['Told','Spoke','Whispered','Talked'],2)]),
M('Time: Reading Clocks','Grade 3 Measurement strand: students tell time to the nearest 5 minutes on analogue clocks and understand a.m./p.m., hours, and minutes.',[
  ('How many minutes are in one hour?',['30','45','60','100'],2),
  ('On an analogue clock, the short hand points to the ___.',['minutes','seconds','hours','days'],2),
  ('3:45 means ___.',['quarter past 3','45 hours past 3','15 minutes to 4','quarter to 3'],2),
  ('a.m. refers to time ___.',['in the afternoon','at night after midnight','from midnight to noon','from noon to midnight'],2),
  ('How many minutes does the minute hand travel in a quarter turn (from 12 to 3)?',['5','10','15','20'],2)]),
Sc('Rocks and Their Properties','Grade 3 Science Earth strand: rocks are identified by properties such as colour, lustre, texture, hardness, and whether they have crystals or fossils.',[
  ('Which property describes how shiny a rock looks?',['Texture','Hardness','Lustre','Colour'],2),
  ('The Mohs scale measures a rock\'s ___.',['colour','lustre','hardness','size'],2),
  ('A rock that has visible grains or crystals is described as having a ___ texture.',['smooth','coarse/grainy','glassy','slippery'],1),
  ('Fossils are most often found in which rock type?',['Igneous','Metamorphic','Sedimentary','Granite'],2),
  ('Which rock property helps geologists identify minerals?',['Only weight','Colour, lustre, hardness, and cleavage combined','Only shape','Only where it was found'],1)]),
SS('Mapping: Scale and Distance','Grade 3 Social Studies: a map scale shows the relationship between distance on the map and actual distance. Students use a scale to estimate real distances.',[
  ('A map scale shows ___.',['how beautiful a map is','the relationship between a distance on the map and the actual distance it represents','the direction of North','the population of a place'],1),
  ('If 1 cm on a map = 10 km in reality, how far is a 3 cm line?',['3 km','10 km','30 km','300 km'],2),
  ('Why do maps need a scale?',['For decoration','So readers can estimate real distances from the map','To show colours','To name cities'],1),
  ('A large-scale map shows ___ area with ___ detail.',['a large, less','a small, more','only cities, more','only countries, less'],1),
  ('What does the scale bar on a map tell you?',['The map\'s title','How long the map is','The distance represented by a specific length on the map','The year the map was made'],2)])]),
day(22,[
L('Grammar: Adjectives','Grade 3 Language strand: adjectives describe nouns. They tell what kind, how many, which one, or what colour. Comparatives add -er; superlatives add -est.',[
  ('An adjective describes a ___.',['verb','adverb','noun','conjunction'],2),
  ('Which is an adjective in: The tiny blue bird sang?',['bird','sang','tiny and blue','The'],2),
  ('To compare two things, you use a ___ adjective.',['regular','superlative','comparative (-er)','adverb'],2),
  ('Which is the superlative form of "tall"?',['Taller','Tallest','Most tall','More tall'],1),
  ('Which sentence uses an adjective correctly?',['She runs quickly.','The loud, excited crowd cheered.','He jumps high.','They went there.'],1)]),
M('Data: Collecting and Organising','Grade 3 Data strand: students collect data by surveying, use tally charts to organise it, and display it in pictographs or bar graphs.',[
  ('A tally chart uses marks to ___.',['draw a graph','count and record data quickly','add numbers','measure length'],1),
  ('In a tally, four vertical lines crossed by one diagonal line = ___.',['4','5','6','7'],1),
  ('A pictograph uses ___ to represent data.',['bars','lines','pictures or symbols','only numbers'],2),
  ('A survey is a way to ___.',['measure distance','collect data by asking people questions','draw graphs','calculate perimeter'],1),
  ('After collecting data, the next step is to ___.',['throw it away','organise it in a table or chart','multiply it','ignore patterns'],1)]),
Sc('The Water Cycle','Grade 3 Science Earth strand: the water cycle involves evaporation (liquid to vapour), condensation (vapour to cloud), and precipitation (rain/snow). It repeats continuously.',[
  ('Evaporation is when water changes from liquid to ___.',['solid ice','water vapour (gas)','snow','mud'],1),
  ('Condensation forms ___.',['rain directly','clouds when water vapour cools and becomes liquid droplets','ice on the ground','more evaporation'],1),
  ('Precipitation is ___.',['evaporation happening fast','condensation in clouds','water falling from clouds as rain, snow, sleet, or hail','water heating up'],2),
  ('What powers the water cycle?',['The Moon','The wind alone','The Sun\'s energy','Human activity'],2),
  ('After precipitation, water returns to the cycle by ___.',['staying on the ground forever','freezing permanently','evaporating again or flowing to oceans and lakes','disappearing'],2)]),
SS('Canadian Provinces and Territories','Grade 3 Social Studies: Canada has 10 provinces and 3 territories. Each has a capital city. Students learn their locations and key features.',[
  ('Canada has ___ provinces.',['8','9','10','11'],2),
  ('Canada has ___ territories.',['1','2','3','4'],2),
  ('Which province is the most populated?',['British Columbia','Alberta','Quebec','Ontario'],3),
  ('What is the capital city of Ontario?',['Ottawa','Toronto','Hamilton','London'],1),
  ('Which territory is the largest by area?',['Yukon','Northwest Territories','Nunavut','British Columbia'],2)])]),
day(23,[
L('Reading: Cause and Effect','Grade 3 Reading strand: cause is why something happened; effect is what happened. Signal words include because, so, therefore, as a result, and since.',[
  ('A cause is ___.',['what happened','why something happened','when something happened','where something happened'],1),
  ('An effect is ___.',['why something happened','who made it happen','what happened as a result','where something happened'],2),
  ('Which word signals a cause?',['So','Then','Because','After'],2),
  ('Which word signals an effect?',['Since','Because','As a result','If'],2),
  ('"It rained, so the game was cancelled." The CAUSE is ___.',['The game was cancelled','It rained','The players stayed home','The field was wet'],1)]),
M('Multiplication Facts to 9×9','Grade 3 Number strand: students extend multiplication fluency to 9×9 using patterns, skip counting, and doubling strategies.',[
  ('6 × 7 = ?',['40','42','44','48'],1),
  ('8 × 4 = ?',['28','30','32','36'],2),
  ('9 × 6 = ?',['48','52','54','56'],2),
  ('7 × 7 = ?',['42','47','49','56'],2),
  ('8 × 9 = ?',['63','70','72','81'],2)]),
Sc('Air and Its Properties','Grade 3 Science Physical strand: air is a mixture of gases that takes up space, has mass, exerts pressure, and can be compressed. Wind is moving air.',[
  ('Air takes up ___.',['no space','space (even though we cannot see it)','only a little space in hot weather','space only at high altitude'],1),
  ('Air has ___.',['no mass','mass (it can be weighed)','negative mass','only heat'],1),
  ('Compressed air means ___.',['air that is heated','air that is cooled','air that is squeezed into a smaller space','air that is released'],2),
  ('Air pressure is ___.',['only found underwater','the force exerted by air on surfaces','not real','only exists at sea level'],1),
  ('Wind is ___.',['a type of cloud','heated water rising','moving air caused by differences in air pressure','solid air'],2)]),
SS('Goods and Services in the Community','Grade 3 Social Studies: goods are physical products (food, clothing); services are actions that help people (teaching, firefighting). Communities need both.',[
  ('A good is ___.',['something someone does to help you','a physical product you can touch and use','a type of community helper','a type of tax'],1),
  ('A service is ___.',['a physical product','something someone does to help others (e.g., teaching, doctoring)','only in cities','only paid work'],1),
  ('Which is a good?',['Teaching a class','Cutting hair','A loaf of bread','Driving a bus'],2),
  ('Which is a service?',['A book','A chair','A table','A haircut at a salon'],3),
  ('Communities need both goods and services because ___.',['goods are better than services','services are more important','people need physical products AND help from others to live well','only one is necessary'],2)])]),
day(24,[
L('Reading Strategies Review','Grade 3 Reading strand: skilled readers use strategies — predicting, visualising, making connections, questioning, inferring, determining importance, and synthesising.',[
  ('Predicting means ___.',['reading slowly','making a guess about what will happen using clues','looking only at pictures','reading the last page first'],1),
  ('Making a text-to-self connection means ___.',['connecting the text to a movie','connecting the text to something in your own life','connecting two books together','connecting to a news story'],1),
  ('Determining importance means ___.',['reading everything equally carefully','identifying the key ideas and distinguishing them from supporting details','reading only the first sentence','re-reading the whole text'],1),
  ('Synthesising information means ___.',['copying','combining information from multiple sources to form a new understanding','only summarising','restating without thinking'],1),
  ('Good readers constantly ___ as they read.',['count words','monitor understanding and use fix-up strategies when confused','read without thinking','skip difficult parts'],1)]),
M('Area: Counting Square Units','Grade 3 Measurement strand: area is the amount of space inside a shape, measured in square units. Students find area by counting squares on a grid.',[
  ('Area is the amount of space ___.',['around a shape','inside a shape','above a shape','between two shapes'],1),
  ('Area is measured in ___.',['cm (linear)','cm² (square units)','cm³ (cubic)','kg'],1),
  ('A rectangle 4 cm × 3 cm has an area of ___.',['7 cm²','12 cm²','14 cm²','24 cm²'],1),
  ('To find the area of a rectangle, you ___.',['add length + width','multiply length × width','subtract width from length','divide length by width'],1),
  ('A square with sides of 5 cm has an area of ___.',['10 cm²','20 cm²','25 cm²','50 cm²'],2)]),
Sc('Living Things: Adaptation Review','Grade 3 Science Life strand: adaptations are features that help organisms survive in their habitat. Physical adaptations (camouflage, thick fur) and behavioural adaptations (migration, hibernation).',[
  ('A physical adaptation is ___.',['a learned behaviour','a body feature that helps survival','a choice an animal makes','a type of habitat'],1),
  ('Camouflage is an adaptation that helps animals ___.',['find food faster','attract mates only','blend into their surroundings to hide from predators or prey','grow larger'],2),
  ('Migration as a behavioural adaptation means ___.',['sleeping all winter','changing colour in winter','moving seasonally to a better climate or food source','building a nest'],2),
  ('Thick fur in winter is an adaptation for ___.',['swimming faster','camouflage','staying warm in cold environments','finding food underground'],2),
  ('Which is a behavioural adaptation?',['A polar bear\'s white fur','Webbed feet on a duck','Birds flying south for winter','A giraffe\'s long neck'],2)]),
SS('Government: Rules and Laws','Grade 3 Social Studies: communities need rules and laws to keep everyone safe and to treat people fairly. Rules apply in school; laws apply to the whole country.',[
  ('Rules in school help ___.',['make school messy','make school unsafe','keep everyone safe and learning','only help teachers'],2),
  ('Laws apply to ___.',['only children','only adults','everyone in the community/country','only the government'],2),
  ('Which is an example of a school rule?',['Pay taxes','Vote in elections','Raise your hand before speaking','Drive on the right side of the road'],2),
  ('Which is an example of a law?',['Always walk quietly in the hall','Wear your school uniform','Stop at a red traffic light','Pack your bag each day'],2),
  ('Why do communities need both rules and laws?',['They do not','They protect people, ensure fairness, and allow communities to function safely','Only schools need rules','Only governments need laws'],1)])]),
day(25,[
L('Grammar Review: Sentences','Grade 3 Language strand: a simple sentence has one independent clause. A compound sentence joins two independent clauses with a conjunction (and, but, or). A complex sentence has a dependent clause.',[
  ('A simple sentence has ___.',['two independent clauses','one subject and one predicate (one main idea)','no verb','no subject'],1),
  ('A compound sentence joins two independent clauses with ___.',['a period','a semicolon only','a coordinating conjunction (and, but, or)','brackets'],2),
  ('Which is a compound sentence?',['She ran fast.','The dog barked.','I wanted to go, but it was raining.','Because she was tired.'],2),
  ('A dependent clause ___.',['can stand alone as a sentence','depends on an independent clause to make sense','has no verb','is always a question'],1),
  ('Which is a complex sentence?',['He ate breakfast.','He and she played.','Because she was tired, she went to bed early.','Run fast!'],2)]),
M('Number Patterns','Grade 3 Patterning strand: students identify the rule in number patterns, extend them, and create their own. Patterns can increase, decrease, or alternate.',[
  ('What is the rule? 5, 10, 15, 20...',['add 4','add 5','add 6','multiply by 2'],1),
  ('What comes next? 3, 6, 12, 24, ___',['30','36','48','42'],2),
  ('What is the rule? 100, 90, 80, 70...',['subtract 5','subtract 10','add 10','subtract 20'],1),
  ('What comes next? 2, 5, 8, 11, ___',['12','13','14','15'],2),
  ('A decreasing pattern means the numbers ___.',['go up','alternate','go down','stay the same'],2)]),
Sc('Weather Observation Tools','Grade 3 Science Earth strand: scientists measure weather using thermometers (temperature), rain gauges (precipitation), wind vanes (wind direction), and anemometers (wind speed).',[
  ('A thermometer measures ___.',['wind speed','wind direction','temperature','precipitation'],2),
  ('A rain gauge measures ___.',['wind speed','how much rain has fallen','temperature','air pressure'],1),
  ('A wind vane shows ___.',['how fast the wind blows','how cold the wind is','the direction the wind is coming from','the amount of rain'],2),
  ('An anemometer measures ___.',['temperature','precipitation','wind direction','wind speed'],3),
  ('Why is measuring weather important?',['It is not','It helps us predict weather, stay safe, and plan our lives','Only scientists care','It is just for interest'],1)]),
SS('Review: Communities and People','Grade 3 Social Studies review: urban/rural communities, Indigenous peoples, Canadian provinces, mapping, goods/services, government, and citizenship.',[
  ('An urban community usually has more ___ than a rural community.',['farmland','open space','people and services','forests'],2),
  ('Indigenous peoples have lived in Canada for ___.',['100 years','500 years','thousands of years','only recently'],2),
  ('Canada has 10 provinces and ___ territories.',['1','2','3','4'],2),
  ('A good is a physical product; a service is ___.',['also a product','an action that helps people','only for money','only from the government'],1),
  ('Laws exist to ___.',['punish only','help communities function safely and fairly','create confusion','only protect adults'],1)])]),
day(26,[
L('Media Literacy: Advertisements','Grade 3 Language/Media strand: advertisements are created to persuade people to buy or do something. Students identify persuasive techniques: slogans, endorsements, images, and exaggerations.',[
  ('An advertisement is created to ___.',['inform only','entertain only','persuade people to buy or do something','report the news'],2),
  ('A slogan is ___.',['a type of image','a catchy phrase that sticks in your mind','a long paragraph','the price tag'],1),
  ('Celebrity endorsement means ___.',['a celebrity designs the product','a famous person says they use or like the product to influence buyers','the product is made in Hollywood','an advertisement with no pictures'],1),
  ('Why should you think critically about advertisements?',['You should not','Ads may exaggerate or mislead; you should make informed choices','All ads are perfectly true','Only children need to question ads'],1),
  ('What is the PURPOSE of most advertisements?',['To educate','To report facts','To entertain only','To persuade you to buy something or change your behaviour'],3)]),
M('Fractions on a Number Line','Grade 3 Number strand: fractions can be placed on a number line between 0 and 1. 1/2 is halfway, 1/4 is one quarter of the way, and 3/4 is three quarters.',[
  ('Where does 1/2 sit on a number line between 0 and 1?',['Near 0','Exactly in the middle','Near 1','Exactly at 1'],1),
  ('Which fraction is closer to 1?',['1/4','1/3','1/2','3/4'],3),
  ('Where is 1/4 on a number line between 0 and 1?',['Halfway','One quarter of the way from 0 to 1','Three quarters of the way','At 0'],1),
  ('Order from least to greatest: 3/4, 1/4, 1/2',['3/4, 1/2, 1/4','1/4, 3/4, 1/2','1/4, 1/2, 3/4','1/2, 1/4, 3/4'],2),
  ('1/3 is ___ than 1/2.',['greater','equal','less','not comparable'],2)]),
Sc('Habitats: Forest and Wetland','Grade 3 Science Life strand: forests provide food, shelter, and water for many organisms. Wetlands (swamps, marshes, bogs) are highly biodiverse and filter water.',[
  ('A forest habitat provides organisms with ___.',['only shade','food, shelter, water, and space','only wood','no water'],1),
  ('Wetlands are important because they ___.',['are wastelands','filter water, reduce flooding, and support enormous biodiversity','are only homes for fish','are useless swamps'],1),
  ('Which animal is commonly found in an Ontario forest?',['Polar bear','Camel','Moose or white-tailed deer','Penguin'],2),
  ('A marsh is a type of ___.',['desert','wetland with grasses and shallow water','forest','mountain habitat'],1),
  ('Why are wetlands threatened?',['They are growing rapidly','Draining for farming and urban development reduces their area','Nobody wants to build near wetlands','Wetlands are always protected'],1)]),
SS('Canada\'s Place in the World','Grade 3 Social Studies: Canada is a large, diverse country that participates in global trade, peacekeeping, and cooperation through organisations like the United Nations.',[
  ('Canada is located in ___.',['South America','Africa','Europe','North America (the northern half)'],3),
  ('Canada participates in the United Nations to ___.',['control other countries','cooperate with other nations on peace, rights, and development','only trade goods','avoid international contact'],1),
  ('Canada has traded goods with other countries because ___.',['it has everything it needs','it lacks some resources and has excess of others — trade benefits all','only for money','only with the USA'],1),
  ('Canadian peacekeepers ___.',['fight wars for profit','help keep peace in conflict zones around the world','only work in Canada','have no role internationally'],1),
  ('Why is it important for children to learn about Canada\'s global role?',['It is not','Understanding Canada\'s place in the world helps us be informed and responsible global citizens','Only for geography class','Only for adults'],1)])]),
day(27,[
L('Writing Process: Editing','Grade 3 Writing strand: editing improves the content and clarity of writing. Students check for main idea, supporting details, logical flow, and removing off-topic sentences.',[
  ('Editing focuses on ___.',['spelling and punctuation','the content, structure, and clarity of writing','only vocabulary','only sentence length'],1),
  ('Proofreading focuses on ___.',['content and ideas','spelling, grammar, punctuation, and capitalization','only vocabulary','removing sentences'],2),
  ('When editing, you should check that ___.',['you have the most words','every sentence is very long','the main idea is clear and supported by relevant details','there are no commas at all'],2),
  ('An off-topic sentence in a paragraph should be ___.',['kept for length','moved to the beginning','removed or replaced','underlined'],2),
  ('Which editing question is most useful?',['Did I use fancy words?','Is my writing as long as possible?','Does each paragraph focus on one main idea with supporting details?','Did I use a lot of adjectives?'],2)]),
M('Review: Multiplication and Division','Grade 3 Number strand review: multiplication as equal groups, division as equal sharing, fact families, and solving word problems.',[
  ('5 × 6 = ?',['24','28','30','35'],2),
  ('24 ÷ 4 = ?',['4','5','6','7'],2),
  ('The fact family for 3, 4, 12 includes ___.',['3+4=7 and 12-3=9','3×4=12 and 12÷3=4','3+4=12 and 12÷3=6','3×4=7 and 4×3=12'],1),
  ('A bag has 35 candies split equally into 7 bags. Each bag has ___.',['4','5','6','7'],1),
  ('Which word problem uses multiplication?',['12 less than 20','5 groups of 8 chairs — how many chairs in all?','25 minus 10','30 shared by 6'],1)]),
Sc('Light: Shadows and Reflection','Grade 3 Science Physical strand: light travels in straight lines; opaque objects block light creating shadows. Smooth shiny surfaces reflect light.',[
  ('A shadow forms when ___.',['light bends around an object','an opaque object blocks light','a transparent object lets light through','light speeds up'],1),
  ('Light travels in ___.',['curves','circles','straight lines','spirals'],2),
  ('An opaque object ___.',['lets all light through','lets some light through','blocks all light','produces its own light'],2),
  ('A shadow is ___ when the light source is far away.',['taller','wider','smaller','the same size as the object'],2),
  ('Reflection of light occurs on ___.',['rough dark surfaces only','only mirrors','smooth shiny surfaces such as mirrors and calm water','all surfaces equally'],2)]),
SS('Review: Social Studies Grade 3','Grade 3 Social Studies comprehensive review of all topics: communities, mapping, history, economics, government, and Canada\'s global role.',[
  ('Which describes an urban community?',['Many farms and open land','Many people, services, and tall buildings','One store and few services','Forests and rivers only'],1),
  ('A map scale helps you ___.',['find North','calculate real distances from the map','read the map title','name provinces'],1),
  ('Indigenous peoples have lived in Canada for ___.',['500 years','100 years','thousands of years','only since Confederation'],2),
  ('A service is ___.',['a physical product','something done to help others','always free','only from the government'],1),
  ('Laws exist to ___.',['confuse people','protect citizens and allow communities to function fairly and safely','help only the wealthy','punish everyone'],1)])]),
day(28,[
L('Oral Communication: Speaking and Listening','Grade 3 Language strand: effective oral communication involves speaking clearly and confidently, listening actively, and responding respectfully in discussions.',[
  ('Active listening means ___.',['only waiting for your turn to talk','paying full attention, making eye contact, and responding appropriately','nodding without paying attention','interrupting with ideas'],1),
  ('When presenting to a class, you should ___.',['speak very quietly','look only at your paper','speak clearly, make eye contact, and stay on topic','use only one word at a time'],1),
  ('Asking a relevant question during a discussion shows ___.',['you were not listening','active engagement and interest in the topic','you are bored','you disagree with everything'],1),
  ('When someone is speaking, you should ___.',['interrupt when you have a good idea','look around the room','listen without interrupting and wait for your turn','finish their sentences'],2),
  ('Eye contact when presenting helps ___.',['confuse your audience','show confidence and connect with your audience','make the audience look away','replace your notes'],1)]),
M('3-Digit Addition','Grade 3 Number strand: students add 3-digit numbers with regrouping. Example: 347 + 285 = 632. They use place value strategies.',[
  ('347 + 215 = ?',['552','562','572','542'],1),
  ('When the ones column adds to more than 9, you ___.',['stop adding','add the tens column first','regroup (carry) the extra ten to the tens column','write only the ones digit and ignore the rest'],2),
  ('456 + 234 = ?',['680','690','700','670'],1),
  ('What is 500 + 300 + 80 + 20 + 7 + 3?',['900','910','910','910'],1),
  ('293 + 148 = ?',['431','441','441','451'],1)]),
Sc('Sound: Pitch and Volume','Grade 3 Science Physical strand: sounds have pitch (high/low, determined by frequency) and volume (loud/soft, determined by amplitude). Students explore how these properties are created.',[
  ('Pitch refers to how ___ a sound is.',['loud or soft','high or low','fast or slow','long or short'],1),
  ('A high-pitched sound has a ___ frequency.',['low','high','zero','random'],1),
  ('Volume (loudness) is determined by ___.',['frequency','the size of vibrations (amplitude)','how fast the sound travels','colour of the source'],1),
  ('Plucking a guitar string tighter produces a ___ pitch.',['lower','the same','higher','softer'],2),
  ('How can you make a drum sound louder?',['Hit it more gently','Hit it harder (increase amplitude/force)','Make the drum smaller','Use a smaller drum stick'],1)]),
SS('Heritage Celebrations','Grade 3 Social Studies: heritage celebrations reflect the unique traditions of communities. Students explore how different cultures mark special occasions and what these celebrations mean.',[
  ('A heritage celebration reflects ___.',['only modern entertainment','a community\'s cultural traditions, history, and values','only government events','only sport'],1),
  ('Why is it important to acknowledge different cultural celebrations?',['It is not important','It promotes respect, understanding, and inclusion in a diverse society','Only in large cities','Only for tourists'],1),
  ('Diwali is the Festival of ___.',['Sound','Light','Colour','Spring'],1),
  ('Canada Day (July 1) celebrates ___.',['The founding of Ontario','Canada becoming a country in 1867','The discovery of Canada','The Queen\'s birthday'],1),
  ('Celebrating diverse heritage events in school helps ___.',['create conflict','build a sense of belonging and respect for all students\'  backgrounds','replace learning','confuse students'],1)])]),
day(29,[
L('Language Review: Reading and Writing','Grade 3 Language strand comprehensive review of reading strategies, writing forms, grammar, and vocabulary studied throughout the year.',[
  ('The main idea of a text is ___.',['a small supporting detail','what the text is mostly about','the last sentence','only the title'],1),
  ('An inference is ___.',['directly stated','a conclusion drawn from text evidence plus prior knowledge','a question','a main idea'],1),
  ('Cause answers the question ___ ; effect answers ___.',['What? Where?','Why? What happened?','When? Where?','Who? How?'],1),
  ('A synonym for "enormous" is ___.',['tiny','large/huge','normal','slow'],1),
  ('Descriptive writing creates ___.',['instructions','an argument','a vivid picture using sensory details','a summary'],2)]),
M('Review: Measurement and Data','Grade 3 Measurement and Data review: perimeter, area, time, and data collection/display.',[
  ('Perimeter of a 6 × 4 rectangle = ?',['10 cm','20 cm','24 cm','48 cm'],1),
  ('Area of a 5 × 5 square = ?',['10 cm²','20 cm²','25 cm²','50 cm²'],2),
  ('A movie starts at 2:15 p.m. and ends at 4:00 p.m. Duration = ?',['1 h 30 min','1 h 45 min','2 h 15 min','2 h 30 min'],1),
  ('The mode is the ___ value in a data set.',['middle','highest','most frequent','average'],2),
  ('A bar graph is best for comparing ___.',['change over time','categories at one point in time','fractions','angles'],1)]),
Sc('Science Review: All Strands','Grade 3 Science review covering forces, simple machines, soil/rocks/water cycle, weather, habitats, and light/sound.',[
  ('Gravity pulls objects ___.',['upward','sideways','downward toward Earth','in circles'],2),
  ('A lever makes work easier using a bar and a ___.',['wheel','pulley','fulcrum','gear'],2),
  ('The water cycle includes evaporation, condensation, and ___.',['erosion','gravity','precipitation','reflection'],2),
  ('Sedimentary rock is most likely to contain ___.',['crystals only','fossils','magma','only metamorphic minerals'],1),
  ('Sound is produced by ___.',['light waves','vibrations','magnetic fields','electrical signals'],1)]),
SS('Culminating: My Community Action','Grade 3 Social Studies culminating task: students apply knowledge of communities, citizenship, and global connections to identify a community issue and propose a responsible action plan.',[
  ('A community action plan identifies ___.',['only problems','a local issue and proposes realistic solutions','only global problems','only things adults can do'],1),
  ('Effective community action involves ___.',['only one person deciding alone','collaboration and input from diverse community members','ignoring different views','only government action'],1),
  ('Which step comes FIRST in a community action plan?',['Evaluate results','Take action','Identify the problem or issue','Celebrate success'],2),
  ('Why should young people care about their community?',['They should not','Active citizens at any age can make a difference and build stronger communities','Only adults can help','It is only for school projects'],1),
  ('A good community action is ___.',['unrealistic and expensive','realistic, kind, inclusive, and sustainable','done by only one person','something that only helps one group'],1)])]),
day(30,[
L('Year Review: Language Arts','Grade 3 Language Arts comprehensive review across reading, writing, oral communication, grammar, media, and vocabulary.',[
  ('The main idea is ___.',['a detail','the title only','what the whole text is mostly about','the last sentence'],2),
  ('A personal narrative is written in ___ person.',['second','third','first','fourth'],2),
  ('An adjective describes a ___.',['verb','noun','adverb','conjunction'],1),
  ('A compound sentence uses a ___ to join two independent clauses.',['period','conjunction (and, but, or)','comma only','semicolon only'],1),
  ('Synonyms are words with ___ meanings; antonyms have ___ meanings.',['opposite, similar','similar, opposite','same, same','no, different'],1)]),
M('Year Review: Mathematics','Grade 3 Mathematics review covering number, measurement, geometry, patterning, and data.',[
  ('7 × 8 = ?',['54','56','58','64'],1),
  ('45 ÷ 9 = ?',['4','5','6','7'],1),
  ('Area of a 7 × 3 rectangle = ?',['10 cm²','21 cm²','20 cm²','14 cm²'],1),
  ('What is 1/2 + 1/2?',['1/4','1/2','1','2/2'],2),
  ('What is the rule? 4, 8, 16, 32...',['add 4','multiply by 2','add 12','multiply by 3'],1)]),
Sc('Year Review: Science','Grade 3 Science comprehensive review across all strands.',[
  ('Gravity is a force that pulls objects ___.',['upward','sideways','downward toward Earth','randomly'],2),
  ('The water cycle is powered by ___.',['the Moon','wind alone','the Sun\'s energy','human activity'],2),
  ('Which rock type contains fossils?',['Igneous','Metamorphic','Sedimentary','Granite'],2),
  ('A shadow is formed when ___ blocks light.',['glass','a transparent object','an opaque object','a mirror'],2),
  ('Sound is caused by ___.',['light','vibrations','gravity','magnets'],1)]),
SS('Year Review: Social Studies','Grade 3 Social Studies comprehensive review.',[
  ('Urban communities usually have ___ rural communities.',['fewer services than','the same services as','more services and people than','less technology than'],2),
  ('Canada has 10 provinces and ___ territories.',['2','3','4','5'],1),
  ('Indigenous peoples have lived in Canada for ___.',['500 years','thousands of years','200 years','100 years'],1),
  ('A service is ___.',['a physical product','an action that helps others','always free','made only in factories'],1),
  ('Laws exist to ___.',['punish everyone','only protect the rich','keep communities safe and fair for everyone','create confusion'],2)]),
]),
]

append_to(3, g3)
print('Grade 3 done.')
