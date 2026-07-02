#!/usr/bin/env python3
"""Grade 6 — days 16-30 (appended to existing days 1-15)."""
import sys
sys.path.insert(0,'/sessions/wonderful-keen-tesla/mnt/gradesbooster')
from gen_curriculum import sub,day,append_to

U='https://tvolearn.com/pages/grade-6'
R='TVO Learn: Grade 6'

def L(t,s,q): return sub('Language',t,s,R,U,q)
def M(t,s,q): return sub('Math',t,s,R,U,q)
def Sc(t,s,q): return sub('Science',t,s,R,U,q)
def SS(t,s,q): return sub('SocialStudies',t,s,R,U,q)

g6_extra=[
day(16,[
L('Literary Devices: Foreshadowing and Flashback','Students identify and analyse foreshadowing (hints at future events) and flashback (interruption to show past events) in narratives.',[
  ('Foreshadowing in a story means ___.',['looking back at a past event','a hint or clue given early in the story about events that will happen later','a character\'s thoughts only','dialogue between characters'],1),
  ('A flashback is ___.',['a prediction of future events','a scene that interrupts the present narrative to reveal something from the past','a type of simile','a character description'],1),
  ('Which sentence uses foreshadowing?',['She remembered the summer she was seven.','He had no idea the locked door would change everything.','The dog barked twice.','The weather was warm.'],1),
  ('Flashbacks are used by authors to ___.',['confuse the reader','provide background information and deepen understanding of characters or events','speed up the plot','only describe settings'],1),
  ('Which literary device interrupts the current timeline to show past events?',['Foreshadowing','Metaphor','Flashback','Onomatopoeia'],2)]),
M('Ratios','Students understand ratios as comparisons of two quantities. They write ratios in three forms (a:b, a to b, a/b) and find equivalent ratios.',[
  ('A ratio compares ___.',['a fraction and a decimal','only percentages','two quantities or amounts','only whole numbers'],2),
  ('The ratio of 3 red to 5 blue balls can be written as ___.',['3/5 only','3:5, 3 to 5, or 3/5 — all three forms are equivalent','only 3 to 5','5:3 only'],1),
  ('Which ratio is equivalent to 2:3?',['4:5','4:6','3:2','6:9'],1),
  ('A recipe needs 2 cups of flour for every 3 cups of water. For 6 cups of flour, you need ___.',['6 cups','7 cups','8 cups','9 cups'],3),
  ('Ratios can be used to ___.',['only add numbers','compare, scale, and solve proportion problems in real contexts','only subtract','only multiply'],1)]),
Sc('Space: The Solar System','Students explore the eight planets, dwarf planets, moons, asteroids, and comets. They compare planet characteristics and orbital patterns.',[
  ('The correct order of planets from the Sun is ___.',['Venus, Mercury, Earth, Mars...','Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune','Earth, Venus, Mars, Jupiter...','Mars, Venus, Mercury, Earth...'],1),
  ('Which planet is the largest in our solar system?',['Saturn','Uranus','Jupiter','Neptune'],2),
  ('A moon is ___.',['a star','a natural satellite that orbits a planet','a small sun','an asteroid'],1),
  ('What distinguishes a planet from a dwarf planet?',['Size only','Planets orbit the Sun and have cleared their orbital neighbourhood of debris; dwarf planets have not','Composition only','Colour only'],1),
  ('Which of these is NOT a planet in our solar system?',['Uranus','Pluto (dwarf planet)','Neptune','Saturn'],1)]),
SS('Ancient Civilisations: Rome','Students explore the rise and fall of the Roman Empire, its government structure, engineering achievements, and lasting influence on the Western world.',[
  ('The Roman Republic was governed by ___.',['a single king with unlimited power','a Senate and elected magistrates representing different classes of citizens','only military generals','only priests'],1),
  ('Julius Caesar was ___.',['the first Roman Emperor','a Roman general and statesman who was assassinated in 44 BCE, leading to the end of the Republic','a Greek philosopher','a Carthaginian general'],1),
  ('Roman engineering achievements include ___.',['the pyramids','the Great Wall','aqueducts, roads, concrete construction, and the Colosseum','Stonehenge'],2),
  ('The Roman Empire fell in ___.',['100 CE','476 CE (Western Roman Empire)','1066 CE','250 BCE'],1),
  ('Latin, the language of Rome, influenced ___.',['only Italian','no modern languages','many modern languages including French, Spanish, Italian, Portuguese, and Romanian','only scientific vocabulary'],2)])]),
day(17,[
L('Writing: Argumentative Essay','Students write a multi-paragraph argumentative essay with a clear claim, organized supporting points with evidence, counterargument acknowledgement, and a conclusion.',[
  ('The claim in an argumentative essay is ___.',['a question about the topic','the writer\'s main position or argument that the essay will defend','a list of facts only','the conclusion alone'],1),
  ('Why is it important to address the counterargument in an essay?',['It is not important','Acknowledging and refuting opposing views strengthens your argument and shows you\'ve considered multiple perspectives','Only for long essays','Only for debate class'],1),
  ('Evidence in an argumentative essay should be ___.',['only personal opinion','facts, statistics, examples, or expert opinions that support the claim','unrelated to the topic','only from the internet'],1),
  ('A transition between paragraphs helps ___.',['shorten the essay','create flow and show the logical relationship between ideas','only add more words','only for introductions'],1),
  ('The conclusion of an argumentative essay should ___.',['introduce new evidence','simply list facts again','restate the claim, summarise key points, and leave the reader with a final thought','apologise for the opinion'],2)]),
M('Percentages','Students understand percentages as rates per 100. They convert between fractions, decimals, and percentages, and solve percent problems.',[
  ('A percentage is a ratio out of ___.',['10','50','100','1000'],2),
  ('50% as a decimal is ___.',['5.0','0.05','0.5','500'],2),
  ('3/4 expressed as a percentage is ___.',['34%','43%','75%','25%'],2),
  ('What is 20% of 80?',['4','8','12','16'],3),
  ('A shirt costs $40 and is 25% off. How much do you save?',['$8','$10','$12','$15'],1)]),
Sc('Biodiversity and Classification','Students explore the classification of living things (Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species) and the importance of biodiversity.',[
  ('Taxonomy is the science of ___.',['measuring animals','naming, describing, and classifying living things into groups','only studying bacteria','counting species'],1),
  ('The eight levels of biological classification from broadest to most specific are ___.',['Species first to Domain last','Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species','Kingdom to Species only','Only Kingdom, Phylum, Species'],1),
  ('Two organisms belong to the same genus. They must also share the same ___.',['family, order, class, phylum, kingdom, and domain — all broader categories','species always','only kingdom','only phylum'],0),
  ('Biodiversity refers to ___.',['the total number of people on Earth','the variety of life forms in an ecosystem or on Earth — genes, species, and ecosystems','only tropical animals','only plant species'],1),
  ('Why is biodiversity important?',['It is not','Diverse ecosystems are more resilient, provide more resources, and support healthier environments for all life including humans','Only for scientists','Only for forests'],1)]),
SS('Ancient Civilisations: Greece','Students study ancient Greek city-states (Athens and Sparta), the origins of democracy, Greek philosophy, and the legacy of Greek culture.',[
  ('The two main rival city-states in ancient Greece were ___.',['Rome and Athens','Athens and Sparta','Corinth and Thebes','Olympia and Delphi'],1),
  ('Ancient Athens is credited with developing ___.',['monarchy for all cities','the earliest form of direct democracy in which citizens voted on laws and leaders','only military power','the Roman senate'],1),
  ('Socrates, Plato, and Aristotle were ___.',['Greek generals','Greek philosophers who explored ethics, knowledge, politics, and the nature of reality','Greek architects','Roman emperors'],1),
  ('The Olympic Games originated in ancient Greece to ___.',['train soldiers only','honour the gods, particularly Zeus, and foster athletic competition among city-states','trade goods between cities','elect leaders'],1),
  ('Greek culture influenced the modern world through ___.',['only Greek food','democracy, philosophy, theatre, architecture (columns), the Olympics, and scientific thought','only language','only art styles'],1)])]),
day(18,[
L('Media Literacy: Advertising Techniques','Students analyse advertising strategies including emotional appeal, bandwagon, celebrity endorsement, and fear appeal. They evaluate the purpose and impact of media messages.',[
  ('Media literacy involves ___.',['only watching more television','the ability to access, analyse, evaluate, and create media in a variety of forms','only reading newspapers','only creating videos'],1),
  ('The "bandwagon" advertising technique says ___.',['only experts use this product','this product is dangerous','everyone is using this — join in or miss out','a celebrity likes this'],2),
  ('Emotional appeal in advertising works by ___.',['listing technical facts','triggering emotions (happiness, fear, nostalgia, belonging) to influence purchasing decisions','giving accurate statistics only','showing product ingredients'],1),
  ('Why is it important to analyse advertising critically?',['It is not','Understanding persuasion techniques helps you make informed choices rather than being manipulated','Only for marketing students','Only for adults'],1),
  ('A disclaimer in small print at the bottom of an ad is there to ___.',['decorate the ad','make it look longer','provide legally required disclosures that qualify or limit the main claim','show the logo'],2)]),
M('Integers: Introduction','Students extend their number sense to negative numbers. They place integers on a number line, compare them, and understand real-world contexts (temperature, elevation, debt).',[
  ('An integer is ___.',['only a positive whole number','a whole number that can be positive, negative, or zero','a fraction','a decimal'],1),
  ('Which number is greatest?',['−5','−10','0','3'],3),
  ('What is the opposite of −7?',['−7','7','0','1/7'],1),
  ('The temperature is −3°C. It drops 4 more degrees. New temperature = ?',['−7°C','−1°C','1°C','7°C'],0),
  ('On a number line, numbers to the left of 0 are ___.',['positive','neutral','greater','negative'],3)]),
Sc('Electricity and Circuits','Students explore electrical circuits, including series and parallel circuits, conductors, insulators, voltage, current, and resistance.',[
  ('In a series circuit, if one bulb burns out ___.',['all other bulbs stay on','only the next bulb goes out','all bulbs go out (single path for current)','nothing changes'],2),
  ('In a parallel circuit, if one bulb burns out ___.',['all bulbs go out','all other bulbs stay on (each branch has its own path)','only the bulb before it goes out','the battery dies'],1),
  ('Voltage is ___.',['the flow of electrons','the resistance to current','the electrical potential difference (energy per charge) that drives current through a circuit','a unit of resistance'],2),
  ('Which material is a good electrical conductor?',['Rubber','Plastic','Glass','Copper'],3),
  ('Resistance in a circuit ___.',['increases current flow','has no effect','opposes the flow of electric current, converting electrical energy to heat','makes voltage higher'],2)]),
SS('Ancient Civilisations: China','Students study the Han Dynasty, the Silk Road, major inventions (paper, compass, printing, gunpowder), and China\'s influence on world history.',[
  ('The Silk Road was ___.',['a road made of silk','a type of Chinese fabric','a vast network of trade routes connecting China to Central Asia, the Middle East, and Europe','a river route only'],2),
  ('Which of these was NOT invented in ancient China?',['Paper','Gunpowder','The printing press (woodblock printing)','The telephone'],3),
  ('The Great Wall of China was built primarily to ___.',['impress foreign visitors','attract tourists','divide China into provinces','protect China\'s northern border from nomadic invasions'],3),
  ('The Han Dynasty is often compared to Rome because ___.',['they were allies','both empires were roughly contemporary, large, powerful, and had significant lasting cultural influence','they shared the same language','they were geographically connected'],1),
  ('Confucianism emphasises ___.',['military conquest above all','individual freedom only','social harmony, respect for elders and rulers, education, and ethical conduct','isolation from other societies'],2)])]),
day(19,[
L('Reading: Synthesising Information from Multiple Sources','Students gather information from two or more sources and synthesise it into a unified understanding, noting similarities, differences, and gaps.',[
  ('Synthesising information means ___.',['summarising one source','copying from multiple sources','combining and connecting ideas from multiple sources to form a new, deeper understanding','only comparing sources'],2),
  ('When synthesising, you should look for ___.',['only agreements between sources','similarities, differences, unique insights, and gaps in the information','only facts that agree','only contradictions'],1),
  ('Why is it useful to consult multiple sources on a topic?',['It is not','Different sources offer different perspectives, ensuring a more complete and accurate picture','Only if sources agree','Only for long essays'],1),
  ('What should you do when two sources contradict each other?',['Ignore one','Choose the longer source','Investigate further — consider the credibility, date, and bias of each source','Always prefer the most popular'],2),
  ('When writing a synthesis paragraph, you should ___.',['simply list what each source says separately','blend ideas from multiple sources into your own analytical statement','only quote directly','never use your own words'],1)]),
M('Order of Operations (BEDMAS)','Students apply the correct order of operations: Brackets, Exponents, Division/Multiplication (left to right), Addition/Subtraction (left to right).',[
  ('BEDMAS stands for ___.',['Brackets, Exponents, Division, Multiplication, Addition, Subtraction','Base, Equation, Data, Method, Answer, Step','Brackets, Equation, Division, Math, Addition, Subtraction','None of these'],0),
  ('What is 3 + 4 × 2?',['14','11','10','8'],1),
  ('What is (3 + 4) × 2?',['14','11','10','8'],0),
  ('What is 20 ÷ 4 + 3 × 2?',['11','14','5','13'],0),
  ('Which operation is performed FIRST in 8 − 2² + 1?',['Subtraction','Addition','The exponent (2² = 4)','Division'],2)]),
Sc('Flight and Aerodynamics','Students explore the four forces of flight (lift, weight, thrust, drag) and Bernoulli\'s principle. They investigate how wing shape generates lift.',[
  ('The four forces acting on an aircraft in flight are ___.',['push, pull, spin, and float','lift, weight, thrust, and drag','gravity, wind, speed, and size','hot air, cold air, wind, speed'],1),
  ('Lift is a force that acts ___.',['downward','backward','forward','upward, opposing gravity'],3),
  ('Drag is ___.',['the forward force of the engine','the upward aerodynamic force','the air resistance force that opposes motion through air','weight acting down'],2),
  ('Bernoulli\'s principle explains lift because ___.',['wings are heavy','air moving faster over the curved top of the wing creates lower pressure above, generating upward lift','engines push up','wings catch wind'],1),
  ('Which wing shape generates more lift?',['Flat, symmetrical','Curved on top and flatter on the bottom (aerofoil/airfoil shape)','Pointed at both ends','Thick rectangular shape'],1)]),
SS('Medieval Europe','Students explore the feudal system, the role of the Church, the Crusades, the Black Death, and the transition from the Middle Ages to the Renaissance.',[
  ('The feudal system in Medieval Europe was ___.',['a democratic government','a hierarchical structure: monarch → nobles → knights → serfs/peasants who exchanged land and service for protection','a merchant economy','an early republic'],1),
  ('The Black Death (bubonic plague) in the 14th century ___.',['had no major effects','killed roughly one-third of Europe\'s population, disrupting the feudal system and accelerating social change','only affected Asia','only lasted one year'],1),
  ('The Catholic Church in Medieval Europe ___.',['had no political influence','was a purely spiritual institution','held enormous political and social power, influencing monarchs, laws, and daily life','was opposed by all monarchs'],2),
  ('The Crusades were ___.',['peaceful trade missions','military campaigns primarily aimed at capturing Jerusalem and the Holy Land from Muslim rule','only fought in Europe','fought between European kingdoms only'],1),
  ('The Renaissance began in ___.',['Britain','Russia','Spain','Italy in the 14th–15th century, marking a renewed interest in classical learning, art, and science'],3)])]),
day(20,[
L('Grammar: Complex Sentences and Clauses','Students identify and write complex sentences using independent and dependent clauses. They use subordinating conjunctions (because, although, when, if, while, unless).',[
  ('An independent clause can ___.',['not stand on its own','stand alone as a complete sentence','never be part of a complex sentence','only be one word'],1),
  ('A dependent clause ___.',['can stand alone','is always a complete thought','cannot stand alone — it depends on an independent clause to make sense','is never combined with other clauses'],2),
  ('A complex sentence contains ___.',['two independent clauses','only one clause','an independent clause and at least one dependent clause joined by a subordinating conjunction','only dependent clauses'],2),
  ('Which word is a subordinating conjunction?',['And','But','Although','Or'],2),
  ('Which is a complex sentence?',['The dog barked and the cat ran.','She sings.','Although it was raining, the game continued.','Run quickly.'],2)]),
M('Algebra: Variables and Expressions','Students write and evaluate algebraic expressions. They use variables to represent unknown quantities and substitute values to find results.',[
  ('A variable in algebra is ___.',['always the letter x','a letter or symbol that represents an unknown or changing quantity','always equal to 0','only used in equations'],1),
  ('Evaluate 3n + 5 when n = 4.',['17','22','12','16'],0),
  ('Which expression means "5 more than twice a number n"?',['5n + 2','2n + 5','5 + 2 + n','2 + 5n'],1),
  ('Simplify: 4x + 3x',['7x²','12x','7x','43x'],2),
  ('In the expression 6y − 2, the coefficient of y is ___.',['2','6','−2','y'],1)]),
Sc('Climate and Climate Change','Students examine the difference between weather and climate, greenhouse gases, global warming, and human impacts on Earth\'s climate system.',[
  ('Climate is ___.',['today\'s temperature','the average weather patterns over a long time period (decades) in a region','only temperature and precipitation','only summer and winter temperatures'],1),
  ('The greenhouse effect is ___.',['always harmful','the natural process by which greenhouse gases trap heat, warming Earth enough to support life','only caused by humans','a type of pollution only'],1),
  ('Which gas is the most significant human-caused contributor to climate change?',['Oxygen','Nitrogen','Carbon dioxide (CO₂) from burning fossil fuels','Argon'],2),
  ('Global warming refers to ___.',['only the summer getting warmer','the long-term increase in Earth\'s average temperature due to enhanced greenhouse gas emissions','only melting ice caps','only ocean temperature changes'],1),
  ('Which action reduces an individual\'s carbon footprint?',['Flying more often','Driving alone always','Using public transit, eating less meat, and using renewable energy','Buying more products'],2)]),
SS('The Renaissance','Students explore the Renaissance as a period of renewed interest in classical learning, humanism, art, science, and exploration (14th–17th century).',[
  ('Renaissance means ___.',['revolution','new beginning','rebirth — referring to the revival of classical Greek and Roman ideas in Europe','darkness'],2),
  ('Humanism during the Renaissance emphasised ___.',['only religious devotion','the potential, dignity, and achievements of human beings and earthly life','only military conquest','only farming improvements'],1),
  ('Leonardo da Vinci exemplified the Renaissance ideal because ___.',['he was only a painter','he was a master of painting, sculpture, engineering, anatomy, and science — a "Renaissance man"','he invented firearms','he was a military general'],1),
  ('The printing press, invented by Gutenberg around 1440, changed society by ___.',['making books more expensive','allowing rapid, cheap reproduction of books, spreading ideas, literacy, and the Reformation','reducing communication','only helping artists'],1),
  ('Which period of exploration coincided with the Renaissance?',['Ancient times','The Dark Ages','The Age of Exploration — European navigators explored the Americas, Africa, and Asia','The Industrial Revolution'],2)])]),
day(21,[
L('Poetry: Form, Tone, and Theme','Students analyse the form (structure, rhyme scheme, stanza patterns), tone (author\'s attitude), and theme (central message) of a variety of poems.',[
  ('A poem\'s tone is ___.',['the subject of the poem','the central message or lesson','the author\'s attitude toward the subject, conveyed through word choice and structure','the poem\'s rhyme scheme'],2),
  ('A poem\'s theme is ___.',['the number of stanzas','the rhyming pattern','the central message or insight about life that the poem conveys','only a stated lesson in the last line'],2),
  ('A sonnet is a 14-line poem with ___.',['no rhyme','a specific rhyme scheme (Shakespearean: ABAB CDCD EFEF GG; Petrarchan: ABBA ABBA CDE CDE)','only 10 syllables total','free verse structure'],1),
  ('Free verse poetry ___.',['always rhymes','has no regular rhyme or metre — it focuses on imagery and natural speech rhythms','is only one stanza','must have exactly 10 lines'],1),
  ('Analysing a poem\'s tone helps you understand ___.',['how many words it has','the poet\'s feelings toward the subject and the emotional effect on the reader','only the rhyme scheme','only the punctuation'],1)]),
M('Equations: Solving One-Step','Students solve one-step equations involving addition, subtraction, multiplication, and division. They use inverse operations to isolate the variable.',[
  ('To solve x + 7 = 15, you ___.',['add 7 to both sides','multiply both sides by 7','subtract 7 from both sides','divide both sides by 7'],2),
  ('Solve: x − 4 = 9',['x = 5','x = 13','x = 36','x = 4'],1),
  ('Solve: 3x = 24',['x = 72','x = 21','x = 8','x = 27'],2),
  ('Solve: x/5 = 6',['x = 1.2','x = 30','x = 11','x = 0.83'],1),
  ('The idea of "inverse operations" means ___.',['doing the same thing to both sides','using opposite operations to undo and isolate the variable','only adding or subtracting','multiplying only'],1)]),
Sc('Optics: Light and Mirrors','Students explore how light behaves with mirrors. They learn the law of reflection (angle of incidence = angle of reflection) and how concave/convex mirrors form images.',[
  ('The law of reflection states that ___.',['light is absorbed by mirrors','the angle of incidence always equals the angle of reflection','mirrors bend light','light speeds up after reflecting'],1),
  ('The angle of incidence is measured from ___.',['the surface of the mirror','the normal (a line perpendicular to the mirror surface at the point of reflection)','the edge of the mirror','the light source'],1),
  ('A concave mirror ___.',['always makes objects appear smaller','spreads light outward','curves inward, converging reflected light rays (used in telescopes and satellite dishes)','has no focal point'],2),
  ('A convex mirror ___.',['always forms real images','converges light to a focal point','curves outward, diverging light rays, giving a wide field of view (used in car wing mirrors)','magnifies objects'],2),
  ('A flat (plane) mirror produces an image that is ___.',['magnified and inverted','reduced and upright','the same size as the object, upright, and laterally reversed (mirror image)','always blurry'],2)]),
SS('The Age of Exploration','Students study 15th–17th century European exploration, key explorers (Columbus, Cabot, Champlain), the impact on Indigenous peoples, and the Columbian Exchange.',[
  ('The main motivations for European exploration were ___.',['only curiosity','Gold, God, and Glory — the pursuit of trade wealth, spreading Christianity, and national prestige','only scientific discovery','only escaping disease'],1),
  ('Christopher Columbus\'s 1492 voyage ___.',['reached Asia as planned','discovered Australia','established contact between Europe and the Americas, beginning sustained transatlantic interaction','proved the Earth was flat'],1),
  ('The Columbian Exchange refers to ___.',['a stock market in Colombia','the transfer of plants, animals, diseases, and ideas between the Americas, Africa, and Europe after 1492','only the transfer of gold','a trade agreement'],1),
  ('How did European exploration affect Indigenous peoples of the Americas?',['It benefited them greatly','It had no effect','It brought devastating disease, displacement, and cultural destruction, causing massive population decline','Only positively through trade'],2),
  ('Samuel de Champlain is significant in Canadian history because ___.',['he was the first European to reach North America','he founded New France and Quebec City, and mapped much of what is now eastern Canada','he discovered British Columbia','he was a British explorer'],1)])]),
day(22,[
L('Research Project: Planning and Sourcing','Students plan a research project by developing a research question, identifying key subtopics, evaluating sources for credibility, and organising notes.',[
  ('A good research question is ___.',['one with a simple yes/no answer','so broad it can never be answered','focused, specific, open-ended, and answerable through research','already answered in one book'],2),
  ('A primary source is ___.',['always more reliable than a secondary source','a first-hand account or original document (diary, photograph, interview, speech, artefact)','a textbook summary','only an internet source'],1),
  ('A secondary source is ___.',['always less valuable','an interpretation or analysis of primary sources created after the event','only a website','a first-hand account'],1),
  ('To evaluate a source\'s credibility, you check ___.',['only the length','only the title','the author\'s credentials, the publisher, the date, the evidence cited, and potential bias','only the illustrations'],2),
  ('Why should you organise your notes by subtopic?',['It is not necessary','It makes copying easier','It creates a logical structure for your research, making writing much easier','Only for long projects'],2)]),
M('Geometry: Transformations','Students perform and describe translations (slides), reflections (flips), and rotations (turns) of 2D shapes on a coordinate plane.',[
  ('A translation (slide) moves a shape ___.',['by flipping it over a line','by rotating it around a point','by sliding it in a direction without turning or flipping it','by resizing it'],2),
  ('A reflection (flip) produces ___.',['the same orientation as the original','a mirror image of the shape across a line of reflection','a smaller version of the shape','a rotated version'],1),
  ('A rotation turns a shape ___.',['around a fixed point (centre of rotation) by a given angle and direction','along a straight line','by flipping it over an axis','by stretching it'],0),
  ('After a translation right 4 units, a point at (2,3) moves to ___.',['(6,3)','(2,7)','(−2,3)','(2,−1)'],0),
  ('Which transformation preserves the size and shape of the original figure?',['Dilation (enlargement)','Translation only','All three: translation, reflection, and rotation preserve size and shape','None of them'],2)]),
Sc('Biodiversity: Food Webs and Human Impact','Students analyse multi-level food webs, identify keystone species, and examine how human activities alter ecosystems and biodiversity.',[
  ('A keystone species is ___.',['always the largest animal in an ecosystem','any common animal','a species that has a disproportionately large effect on its ecosystem relative to its abundance','only an endangered species'],2),
  ('If a top predator is removed from an ecosystem, the most likely effect is ___.',['no change','only the prey population changes','a population explosion of prey, which overgrazes vegetation, collapsing the ecosystem (trophic cascade)','only the plants change'],2),
  ('Habitat fragmentation means ___.',['making habitats larger','connecting isolated patches','breaking up large, continuous habitats into smaller isolated patches, reducing biodiversity','only cutting down trees'],2),
  ('An invasive species ___.',['helps native species recover','has no effect in new environments','is native to the ecosystem','is a non-native species that spreads rapidly and harms native species and ecosystems'],3),
  ('Which human activity has the greatest impact on global biodiversity loss?',['Recycling','Habitat destruction (primarily for agriculture and urban expansion)','Fishing for food','Walking in parks'],1)]),
SS('The British Empire and Colonialism','Students examine how Britain built a global empire through trade, military power, and colonisation, and explore the complex consequences for colonised peoples.',[
  ('At its height, the British Empire was ___.',['only in North America','only in Africa','the largest empire in history, spanning roughly one-quarter of the world\'s land area','only in Asia'],2),
  ('Colonialism involved ___.',['only trading with other nations','a foreign power taking control of another territory, settling it, exploiting its resources, and governing its people','only building roads abroad','only sending aid'],1),
  ('The transatlantic slave trade was ___.',['a trade in luxury goods','a voluntary migration','the forced transportation and enslavement of millions of Africans by European colonial powers for labour in the Americas','only practiced in Africa'],2),
  ('The impact of British colonialism on Canada includes ___.',['only positive effects','only negative effects','the settlement of Upper and Lower Canada, displacement of Indigenous peoples, fur trade, and eventual Confederation','no lasting effects'],2),
  ('Why is understanding colonialism important today?',['It is not','Understanding colonialism helps explain ongoing inequalities, land disputes, and the need for reconciliation with Indigenous peoples','Only for history teachers','Only in countries that were colonies'],1)])]),
day(23,[
L('Oral Literacy: Debate and Discussion','Students participate in structured debates and discussions. They learn to present arguments clearly, listen actively, ask probing questions, and respond respectfully to opposing views.',[
  ('In a formal debate, the proposition side ___.',['asks questions only','agrees with the resolution and argues in favour of it','opposes the resolution','only listens'],1),
  ('Listening actively during a debate means ___.',['planning your rebuttal only','truly attending to what others say, identifying their key points and evidence, so you can respond thoughtfully','waiting for your turn to speak only','ignoring opposing points'],1),
  ('A rebuttal is ___.',['a new argument unrelated to what was said','a repetition of your opening statement','a direct response that challenges, refutes, or provides a counter-example to an opponent\'s argument','only an insult'],2),
  ('Why is respectful discussion important even when you strongly disagree?',['It is not','Respectful discourse models democratic values and allows ideas to be examined on their merits, not personalities','Only for school','Only for adults'],1),
  ('Citing evidence during a debate ___.',['is optional','weakens your argument','makes your argument more persuasive and credible','only helps the opposition'],2)]),
M('Data: Mean, Median, Mode, Range','Students calculate and interpret mean, median, mode, and range for data sets and understand which measure is most appropriate in different contexts.',[
  ('The mean is ___.',['the middle value','the most frequent value','the sum of all values divided by the number of values','the difference between the highest and lowest values'],2),
  ('For the data set 3, 7, 7, 10, 13, the mode is ___.',['3','7','10','8'],1),
  ('For the data set 2, 5, 8, 11, 14, the median is ___.',['5','8','10','11'],1),
  ('The range of 4, 9, 3, 15, 7 is ___.',['12','9','7','15'],0),
  ('When data has an extreme outlier, which measure of centre is most misleading?',['Median','Mode','Range','Mean'],3)]),
Sc('Optics: Lenses and the Eye','Students explore how convex and concave lenses refract light to form images, and how the eye uses a convex lens (the cornea and lens) to focus images on the retina.',[
  ('A convex lens ___.',['diverges light rays outward','has no effect on light','converges (brings together) light rays to a focal point on the other side','absorbs light only'],2),
  ('A concave lens ___.',['converges light rays','diverges (spreads out) light rays, making objects appear smaller','has no effect','only reflects light'],1),
  ('The human eye focuses light using ___.',['only the retina','only the iris','the cornea and a flexible crystalline lens that focuses light onto the retina','the pupil only'],2),
  ('Myopia (short-sightedness) means ___.',['seeing both near and far clearly','difficulty seeing distant objects clearly because light focuses in front of the retina','difficulty seeing nearby objects','a perfect lens'],1),
  ('A concave lens corrects myopia because it ___.',['converges light before it enters the eye','absorbs extra light','diverges light slightly so it reaches the retina rather than focusing in front of it','thickens the lens of the eye'],2)]),
SS('Trade and Economic Systems','Students explore mercantilism, the triangular trade, the Industrial Revolution\'s economic impact, and how trade systems shaped world history.',[
  ('Mercantilism was the belief that ___.',['trade benefits all countries equally','a country\'s wealth is limited and colonies exist to supply raw materials to and buy goods from the mother country','free trade is best','industrial production should be shared'],1),
  ('The Triangular Trade involved ___.',['three equal partners trading peacefully','the exchange of enslaved Africans for American raw materials and European manufactured goods in a cycle of exploitation','only food and clothing','only European countries'],1),
  ('The Industrial Revolution (18th–19th century) changed economies by ___.',['reducing production','replacing hand production with machine manufacturing, creating factories, and moving from rural to urban economies','eliminating trade','only affecting Britain'],1),
  ('Supply and demand explains that when supply of a good decreases and demand stays constant, the price ___.',['stays the same','decreases','increases','becomes impossible to calculate'],2),
  ('A tariff is ___.',['a type of income tax','a tax on imported goods that raises their price to protect domestic industries','a trade agreement','only for luxury goods'],1)])]),
day(24,[
L('Writing: Memoir','Students write a personal memoir — a piece of narrative non-fiction drawn from their own life experiences. They use vivid detail, reflection, and a clear focus.',[
  ('A memoir is ___.',['a fictional story about a historical figure','a biography written by someone else','a piece of narrative non-fiction told from the author\'s perspective, reflecting on personal experience','a report on current events'],2),
  ('What distinguishes a memoir from an autobiography?',['They are identical','A memoir covers one\'s entire life; an autobiography focuses on one event','A memoir focuses on a particular theme or period in the author\'s life, while an autobiography covers the whole life story','An autobiography is fiction'],1),
  ('Effective memoirs include ___.',['only basic facts of what happened','vivid sensory details, emotional reflection, and a meaningful theme or insight about life','only dialogue','only descriptions of places'],1),
  ('In memoir writing, reflection means ___.',['summarising what happened','simply retelling events in order','stepping back to analyse what the experience meant and what you learned from it','adding fictional elements'],2),
  ('The voice in a memoir should be ___.',['completely neutral and without personality','identical to a newspaper report','the authentic, personal voice of the author — their thoughts, feelings, and perspective shine through','always formal'],2)]),
M('Geometry: Area of Triangles and Parallelograms','Students apply the formulas for area of triangles (A = ½bh) and parallelograms (A = bh), and understand how these relate to rectangles.',[
  ('The area formula for a parallelogram is ___.',['A = l × w','A = b × h','A = ½ × b × h','A = π × r²'],1),
  ('The area formula for a triangle is ___.',['A = b × h','A = 2 × b × h','A = ½ × b × h','A = b + h'],2),
  ('A triangle has base 8 cm and height 5 cm. Area = ?',['13 cm²','20 cm²','40 cm²','16 cm²'],1),
  ('A parallelogram has base 10 m and height 4 m. Area = ?',['14 m²','28 m²','40 m²','20 m²'],2),
  ('Why does the triangle formula have ½?',['Only tradition','A triangle is half of a rectangle/parallelogram with the same base and height','Triangles are smaller than rectangles','No real reason'],1)]),
Sc('Simple and Complex Machines','Students revisit simple machines (lever, inclined plane, wheel-and-axle, pulley, wedge, screw) and examine how they combine in compound machines.',[
  ('A screw is essentially ___.',['a type of lever','a wheel-and-axle','an inclined plane wrapped in a spiral around a cylinder','a type of pulley'],2),
  ('A wedge is ___.',['two inclined planes joined at their thick ends to split, hold, or tighten materials','a type of wheel','a screw without threads','a fixed pulley'],0),
  ('A compound machine is ___.',['always electronic','always very large','one that combines two or more simple machines to accomplish a task','only found in factories'],2),
  ('Which example best illustrates a compound machine?',['A screw alone','A lever alone','A wheel alone','A bicycle, which combines wheel-and-axle, gears, levers, and a pulley-like chain system'],3),
  ('Simple machines make work easier by ___.',['increasing the amount of work done','reducing the total energy needed','changing the direction and/or size of the input force required to do work','only reducing speed'],2)]),
SS('Causes of World War I','Students explore the long- and short-term causes of WWI: militarism, alliances, imperialism, nationalism (MAIN), and the assassination of Archduke Franz Ferdinand.',[
  ('The acronym MAIN summarises the long-term causes of WWI. It stands for ___.',['Military, Alliances, Imperialism, Nationalism','Motivation, Army, Industry, Nations','Manufacturing, Alliances, International, Nationalism','Military, Aggression, Independence, Neutrality'],0),
  ('The immediate trigger for WWI was ___.',['Germany invading France','Britain declaring war on Germany','the assassination of Archduke Franz Ferdinand of Austria-Hungary in Sarajevo (June 28, 1914)','the sinking of the Lusitania'],2),
  ('The system of military alliances in 1914 meant that ___.',['war was impossible','a conflict between two countries could rapidly drag in many others through treaty obligations','only the strongest nations were involved','only economic disputes arose'],1),
  ('Nationalism as a cause of WWI refers to ___.',['a desire for international cooperation','extreme pride in and loyalty to one\'s nation, and the desire of ethnic groups to have their own independent states','only economic competition','religious differences'],1),
  ('Militarism as a cause of WWI refers to ___.',['only fighting wars','the glorification and rapid build-up of military forces and weapons by major European powers in the decades before 1914','only spending money on armies','naval competition only'],1)])]),
day(25,[
L('Novel Study: Character Development','Students track and analyse how the protagonist and key supporting characters change over the course of a novel, identifying motivations, conflicts, and growth.',[
  ('Character development (or "character arc") refers to ___.',['the list of characters in a novel','the physical description of characters','the way a character changes, grows, or learns through the events of the story','the number of times a character appears'],2),
  ('A character\'s motivation is ___.',['how they look','where they live','what drives their actions and decisions — their goals, fears, desires','their name only'],2),
  ('An internal conflict is ___.',['a fight between two characters','a battle between the character and nature','a struggle within a character — their own emotions, values, and choices','a conflict with society'],2),
  ('An external conflict is ___.',['a character\'s internal doubt','a struggle between a character and an outside force (person, society, nature, technology)','only a physical fight','only the villain'],1),
  ('Tracking character development through a novel means ___.',['memorising all character names','noting how characters speak, think, act, and change in response to events and conflicts throughout the story','only analysing the hero','only counting interactions'],1)]),
M('Data: Graphing and Interpreting','Students create and interpret various graphs (bar, line, circle/pie) and draw conclusions from data, considering bias and sample size.',[
  ('A line graph is most useful for showing ___.',['comparisons between categories at one point in time','how data changes over time (trends)','parts of a whole','individual values only'],1),
  ('A circle (pie) graph is most useful for showing ___.',['data trends over time','comparisons of categories','how parts relate to a whole (percentages/proportions)','exact values'],2),
  ('A sample size that is too small can ___.',['make a graph look better','provide misleading results that may not represent the population accurately','have no effect on conclusions','make calculations easier'],1),
  ('Bias in data collection means ___.',['the data is always accurate','a systematic error or slant that makes results unrepresentative of the actual population','only a small error','only intentional cheating'],1),
  ('If a graph\'s y-axis doesn\'t start at 0, it can ___.',['make data more accurate','have no effect','exaggerate differences between values, making them look larger than they are','always be trusted'],2)]),
Sc('Earth\'s Systems: Rock Cycle and Plate Tectonics','Students explore the rock cycle (igneous, sedimentary, metamorphic), plate tectonics, and how Earth\'s internal processes shape the surface.',[
  ('The rock cycle describes ___.',['only how rocks fall down hills','the continuous process by which rocks transform between igneous, sedimentary, and metamorphic forms','how rocks grow','only weathering and erosion'],1),
  ('Plate tectonics theory explains that ___.',['continents are fixed forever','Earth\'s lithosphere is divided into plates that move slowly over the mantle, causing earthquakes, volcanoes, and mountain building','only volcanoes','only earthquakes'],1),
  ('When two tectonic plates collide, they can form ___.',['ocean trenches only','rift valleys only','nothing','mountain ranges (fold mountains) or one plate subducts under the other, creating trenches'],3),
  ('Which boundary type creates rift valleys and new ocean floor?',['Convergent (collision) boundary','Transform (sliding) boundary','Divergent (spreading) boundary','Subduction zone'],2),
  ('Earthquakes occur because ___.',['plates are stationary','only volcanoes cause them','tectonic plates suddenly slip past each other, releasing stored energy as seismic waves','rain erodes the surface'],2)]),
SS('Canada in World War I','Students study Canada\'s contributions to WWI (Vimy Ridge, Passchendaele), the impact on the home front, conscription crisis, and how the war shaped Canadian identity.',[
  ('Canada\'s most celebrated WWI military achievement is ___.',['the invasion of Germany','the Battle of Vimy Ridge (April 1917) where Canadian forces captured a German stronghold that others had failed to take','the liberation of Paris','the naval blockade of Germany'],1),
  ('The conscription crisis of 1917 caused ___.',['no controversy','a deep division in Canada, particularly between English Canadians (generally supporting conscription) and French Canadians (largely opposing it)','French and English Canadians to unite completely','only economic problems'],1),
  ('How did WWI change the role of women in Canada?',['It had no effect','Women were prohibited from wartime work','Women took on industrial and agricultural jobs during the war, and many provinces granted women the right to vote between 1916 and 1919','Only nursing was affected'],2),
  ('The Battle of Passchendaele (1917) is remembered as ___.',['a quick Canadian victory','a significant Canadian air battle','one of the bloodiest battles of WWI, fought in the mud of Belgium with enormous casualties for little strategic gain','a naval victory'],2),
  ('How did WWI contribute to Canada\'s sense of national identity?',['It had no effect','Canada\'s military contributions earned international respect and led to greater autonomy from Britain, fostering pride in being distinctly Canadian','Only through hockey','Only through economic growth'],1)])]),
day(26,[
L('Writing: Research Essay — Drafting','Students draft a multi-paragraph research essay: introduction with thesis, body paragraphs with topic sentences and evidence, and a conclusion that synthesises findings.',[
  ('A thesis statement in a research essay ___.',['asks a question','summarises the entire essay in a single sentence','is the writer\'s central argument or claim that the essay will prove','is only in the conclusion'],2),
  ('Each body paragraph in a research essay should begin with ___.',['a quotation','a topic sentence that states the paragraph\'s main point','a new thesis','a conclusion'],1),
  ('In-text citations or references are used to ___.',['make the essay longer','give credit to sources and allow readers to verify information','only in long essays','avoid using evidence'],1),
  ('The conclusion of a research essay should ___.',['introduce new evidence','repeat the introduction word for word','synthesise the key findings, restate the thesis, and explain the broader significance','be only one sentence'],2),
  ('Why is it important to paraphrase rather than copy sources?',['It is not','To avoid plagiarism and to demonstrate your own understanding of the material','Only for professional writers','Only in exams'],1)]),
M('Volume: Rectangular Prisms','Students calculate the volume of rectangular prisms (V = l × w × h) and solve real-world problems involving volume.',[
  ('Volume measures ___.',['the area of a flat surface','the perimeter of a shape','the amount of three-dimensional space enclosed by a solid','the weight of an object'],2),
  ('The formula for the volume of a rectangular prism is ___.',['V = l + w + h','V = l × w','V = l × w × h','V = 2(lw + lh + wh)'],2),
  ('A box is 5 cm long, 4 cm wide, and 3 cm high. Its volume = ?',['12 cm³','20 cm³','47 cm³','60 cm³'],3),
  ('Volume is measured in ___.',['cm²','cm','cm³ (cubic units)','grams'],2),
  ('A fish tank is 80 cm × 30 cm × 40 cm. Its volume in litres (1 L = 1000 cm³) is ___.',['96 L','960 L','9600 L','2.4 L'],0)]),
Sc('Human Body Systems','Students explore body systems and how they interrelate: digestive, circulatory, respiratory, nervous, and musculoskeletal systems.',[
  ('The digestive system breaks food into ___.',['bones','only protein','nutrients small enough to be absorbed into the bloodstream','only sugars'],2),
  ('The main function of the circulatory system is ___.',['controlling movement','digesting food','breathing','transporting oxygen, nutrients, hormones, and waste products through the blood'],3),
  ('Gas exchange (O₂ in, CO₂ out) occurs in the ___.',['liver','kidneys','alveoli of the lungs','stomach'],2),
  ('The nervous system consists of ___.',['only the brain','only the spinal cord','the brain, spinal cord, and network of nerves that carry signals between the body and brain','only sensory nerves'],2),
  ('Body systems work together. Which describes their interaction?',['They work independently and never interact','The digestive system passes nutrients to the circulatory system, which delivers them throughout the body — this shows how systems depend on each other','Only the nervous system affects others','They work in pairs only'],1)]),
SS('World War I: Impact and Consequences','Students examine the human cost of WWI, the Treaty of Versailles, and the seeds of future conflict.',[
  ('WWI resulted in approximately ___.',['10 000 deaths','50 million deaths','17 million deaths (including military and civilian)','1 million deaths'],2),
  ('The Treaty of Versailles (1919) punished Germany by ___.',['rewarding Germany with new territory','making Germany pay reparations, accept blame (War Guilt Clause), lose territory, and limit its military','offering Germany generous aid','only restricting trade'],1),
  ('Why do many historians argue the Treaty of Versailles contributed to World War II?',['It was too generous','The harsh terms created economic collapse and humiliation in Germany, fuelling resentment that extremist parties like the Nazis exploited','It had no long-term effects','Because of geography only'],1),
  ('The League of Nations, created after WWI, was intended to ___.',['enforce German reparations only','prevent future wars through collective security and diplomacy','divide up German colonies','only help European nations'],1),
  ('The United States did NOT join the League of Nations because ___.',['it wasn\'t invited','the US Senate rejected the treaty, preferring isolationism and fearing entanglement in European affairs','it had no interest in peace','it was still fighting WWI'],1)])]),
day(27,[
L('Reading: Independent Novel Study','Students read a self-selected novel and demonstrate comprehension through journal responses, tracking plot structure, character development, and thematic connections.',[
  ('A reading journal helps you ___.',['avoid rereading','only count pages','track your thoughts, questions, and responses to the text as you read, deepening your engagement','only write summaries'],2),
  ('The climax of a novel is ___.',['the very beginning','the falling action','the point of highest tension where the central conflict reaches its peak','the resolution'],2),
  ('Falling action in plot structure refers to ___.',['events before the conflict','events building to the climax','events that follow the climax as loose ends are tied up and tension decreases','the very end'],2),
  ('Connecting a novel\'s themes to the real world means ___.',['only describing the plot','describing all the characters','relating the story\'s central messages to your own life, society, or other texts','only comparing it to movies'],2),
  ('A literary discussion of a novel goes beyond plot summary by ___.',['listing all events','only naming characters','analysing the author\'s choices and exploring the deeper meanings and themes of the text','only describing the cover'],2)]),
M('Patterning and Algebra: Graphing Relationships','Students represent and analyse linear relationships using tables of values, graphs (on a coordinate plane), and equations.',[
  ('A linear relationship produces points that ___.',['curve unpredictably','form a straight line when graphed','always go through the origin only','scatter randomly'],1),
  ('A table of values shows ___.',['only one pair of values','corresponding input and output values for a relationship','only addition facts','only random numbers'],1),
  ('If y = 2x + 1, what is y when x = 4?',['7','8','9','10'],2),
  ('On a graph, the y-intercept is ___.',['where the line crosses the x-axis','where the line crosses the y-axis','the steepness of the line','the length of the line'],1),
  ('The slope of a line represents ___.',['the y-intercept value','the x-axis value','the rate of change — how much y changes for every 1-unit increase in x','only the direction of the line'],2)]),
Sc('Ecosystems and Environmental Stewardship','Students examine ecosystem services, the impact of pollution, and what students and communities can do to protect natural environments.',[
  ('Ecosystem services are ___.',['products sold in nature stores','the benefits humans receive from ecosystems (clean air, clean water, food, climate regulation, pollination, etc.)','only recreational benefits','only services provided by animals'],1),
  ('The main cause of freshwater pollution in Ontario is ___.',['natural processes only','industrial and agricultural runoff, sewage discharge, and urban stormwater contamination','only littering','only oil spills'],1),
  ('Bioaccumulation means ___.',['plants growing bigger','the process by which pollutants accumulate in an organism and concentrate at higher levels of the food chain','soil getting nutrients','water evaporating'],1),
  ('Which action helps protect local ecosystems?',['Draining wetlands for development','Removing invasive species and restoring native vegetation','Using more pesticides','Paving over green spaces'],1),
  ('Environmental stewardship is ___.',['ignoring environmental problems','the responsible care and management of the environment, accepting that humans have a duty to protect natural resources','only for scientists','only about recycling'],1)]),
SS('Canada Between the Wars (1919–1939)','Students examine Canada\'s political maturation (Statute of Westminster 1931), economic boom and crash (1929), and rise of Social Credit and Co-operative Commonwealth Federation.',[
  ('The Statute of Westminster (1931) ___.',['made Canada fully independent from Britain overnight','gave Canada full control over its foreign policy and laws, effectively recognising Canadian sovereignty within the Commonwealth','dissolved the British Empire','gave Quebec independence'],1),
  ('The Great Depression (1929–1939) in Canada caused ___.',['economic prosperity','only minor disruptions','massive unemployment, poverty, drought (the Dust Bowl in the Prairies), and political unrest','only stock market issues'],2),
  ('The "Dirty Thirties" in the Prairie provinces were worsened by ___.',['too much rainfall','industrial pollution','severe drought and poor farming practices that caused massive topsoil erosion and crop failure','foreign invasion'],2),
  ('The CCF (Co-operative Commonwealth Federation), founded in 1932, advocated for ___.',['continued free-market capitalism without regulation','eliminating all taxation','democratic socialism: public ownership of key industries and social programs to help workers and the unemployed','monarchy only'],1),
  ('Canada\'s response to WWI veterans, including benefits and pensions, was ___.',['generous from the start','completely ignored','inadequate, leading to protests like the Regina Riot (1935) during the "On to Ottawa Trek"','only handled by charities'],2)])]),
day(28,[
L('Writing: Editing and Proofreading','Students refine their writing through systematic editing (content, organisation, style) and proofreading (grammar, spelling, punctuation), using editing marks and checklists.',[
  ('Editing focuses on ___.',['only spelling errors','only punctuation','improving content, organisation, clarity, and style — the big-picture issues','only finding typos'],2),
  ('Proofreading focuses on ___.',['content and ideas','paragraph structure','fixing spelling, grammar, punctuation, and formatting errors — the surface-level details','changing the thesis'],2),
  ('Reading your writing aloud helps you ___.',['write faster','avoid all errors immediately','catch awkward phrasing, missing words, and sentences that don\'t flow well','only find spelling errors'],2),
  ('Peer editing means ___.',['writing for someone else','a classmate critically reviewing your work and offering constructive feedback','copying a classmate\'s work','only correcting grammar'],1),
  ('Which comes first: editing or proofreading?',['Proofreading','They are done simultaneously','Editing (big-picture revisions to content and structure) should come before proofreading (surface-level corrections)','Neither is needed'],2)]),
M('Fractions, Decimals, and Percents: Connecting','Students convert fluently between fractions, decimals, and percentages, and apply these conversions to real-world problems.',[
  ('Convert 3/5 to a decimal.',['0.3','0.6','0.35','0.53'],1),
  ('Convert 0.45 to a percentage.',['4.5%','0.45%','45%','450%'],2),
  ('Convert 35% to a fraction in lowest terms.',['35/100','7/20','35/10','7/100'],1),
  ('Arrange in order from least to greatest: 0.6, 3/5, 58%, 0.65.',['0.65, 0.6, 3/5, 58%','3/5 = 0.6 = 60% < 0.65 and 58% < 60% so: 58%, 0.6 = 3/5, 0.65','0.6, 58%, 3/5, 0.65','3/5, 0.6, 0.65, 58%'],1),
  ('A student scored 18/24 on a test. What percentage is this?',['18%','24%','75%','80%'],2)]),
Sc('Light: Colour and the Electromagnetic Spectrum','Students explore how white light splits into the visible spectrum, how objects absorb/reflect/transmit light to produce colour, and the broader electromagnetic spectrum.',[
  ('White light is ___.',['a single colour','only yellow and white','a mixture of all visible colours of the spectrum','not actually light'],2),
  ('A red object appears red because ___.',['it produces red light','it absorbs all colours and reflects red wavelengths to our eyes','it is transparent to red only','it contains red pigment only'],1),
  ('The primary colours of light are ___.',['red, yellow, blue','red, green, blue (RGB)','cyan, magenta, yellow','black, white, grey'],1),
  ('The electromagnetic spectrum includes ___.',['only visible light','radio waves, microwaves, infrared, visible light, UV, X-rays, and gamma rays','only harmful waves','only waves humans can hear'],1),
  ('Which part of the electromagnetic spectrum is used in medical X-rays?',['Radio waves','Infrared','Visible light','X-rays'],3)]),
SS('World War II: Causes and Canada\'s Role','Students examine the rise of fascism, appeasement, and Canada\'s significant contributions to WWII on land, sea, and air.',[
  ('The main ideological forces driving WWII were ___.',['communism vs. democracy only','fascism/Nazism in Germany and Italy, militarism in Japan, vs. the Allied democracies','only economic disputes','only nationalism'],1),
  ('Appeasement in the 1930s meant ___.',['fighting back aggressively','the British and French policy of granting concessions to Hitler to avoid war — famously at Munich in 1938','only economic sanctions','helping Germany rebuild'],1),
  ('Canada declared war on Germany ___.',['the same day as Britain','a week before Britain','one week after Britain (September 10, 1939), demonstrating growing Canadian autonomy','two months after Britain'],2),
  ('The Battle of the Atlantic was crucial because ___.',['it won the war in one battle','Allied naval forces, including many Canadians, protected vital supply convoys crossing the Atlantic — without which Britain could not survive','it only affected submarines','it had no strategic value'],1),
  ('D-Day (June 6, 1944) was significant because ___.',['Canada did not participate','it was a minor skirmish','Canadian forces at Juno Beach were one of five Allied forces landing on Normandy — it began the liberation of Western Europe','it ended the war immediately'],2)])]),
day(29,[
L('Media: Creating a Documentary Script','Students plan and write a short documentary script, incorporating research, narration, interview questions, and visual descriptions.',[
  ('A documentary is a type of ___.',['fiction film','animation','non-fiction film or media that presents facts about real-world events, people, or topics','only a school project'],2),
  ('A script for a documentary includes ___.',['only visuals','only music','narration, dialogue, visual directions, and interview questions — all working together to tell a true story','only facts and statistics'],2),
  ('Why do documentaries often include interviews?',['Only for entertainment','To meet a time requirement','First-hand accounts and expert opinions make the story more credible, human, and engaging','Interviews replace all narration'],2),
  ('A "hook" at the start of a documentary ___.',['puts audiences to sleep','introduces all facts immediately','is a compelling opening (striking visual, intriguing question, shocking fact) that grabs the audience\'s attention','is only a song'],2),
  ('When writing documentary narration, the tone should be ___.',['always humorous','always angry','matched to the subject — serious for serious topics, accessible and clear, and based on verified facts','identical for all documentaries'],2)]),
M('Probability: Theoretical and Experimental','Students distinguish theoretical probability (what should happen) from experimental probability (what does happen). They run probability experiments and compare results.',[
  ('Theoretical probability is based on ___.',['only past experiments','what actually happens in a trial','what mathematically should happen under ideal conditions (favourable outcomes / total outcomes)','only computer simulations'],2),
  ('Experimental probability is based on ___.',['mathematical calculation only','actual results from repeated trials of an experiment','only one trial','only paper calculations'],1),
  ('If you flip a coin 100 times and get 53 heads, the experimental probability of heads is ___.',['1/2','53/100','47/100','100/53'],1),
  ('As the number of trials increases, experimental probability ___.',['gets further from theoretical','has no relationship to theoretical','tends to get closer to the theoretical probability (law of large numbers)','becomes exactly 1'],2),
  ('The theoretical probability of rolling a 4 on a standard die is ___.',['1/4','4/6','1/6','4/1'],2)]),
Sc('Review: Science Connections','Students connect the science strands studied in Grade 6 — biodiversity, flight, electricity, optics, and Earth systems — and see how they relate to real-world issues and careers.',[
  ('Which science strand explains why an eagle can be seen as a keystone species?',['Electricity','Optics','Flight','Biodiversity and ecosystems'],3),
  ('Engineers who design aircraft apply principles from which science topic?',['Rock cycle','Biodiversity','Electricity','Flight and aerodynamics'],3),
  ('Electrical engineers study circuits to develop ___.',['new species','flight paths','new rock types','efficient power systems, renewable energy, and electronic devices'],3),
  ('Understanding optics helps in developing ___.',['food webs','aircraft','tectonic maps','telescopes, cameras, glasses, fibre optics, and medical imaging'],3),
  ('Knowledge of plate tectonics helps ___.',['design aircraft','classify species','build better circuits','predict earthquakes and volcanic eruptions, and understand mineral deposits'],3)]),
SS('Canada After WWII: Social and Political Change','Students explore Canada\'s post-WWII social changes: the baby boom, immigration, multiculturalism, the welfare state (Medicare, CPP), and the growth of suburbs.',[
  ('The "baby boom" after WWII referred to ___.',['a decline in birth rates','a large spike in birth rates as returning soldiers started families (approx. 1946–1964)','an immigration wave','a government housing program'],1),
  ('Multiculturalism became official Canadian policy in ___.',['1867','1919','1971 under Prime Minister Pierre Trudeau, recognising and celebrating cultural diversity','1999'],2),
  ('Medicare (universal health care) in Canada ___.',['was established in 1867','has always existed','began in Saskatchewan in 1962 under Tommy Douglas and was adopted federally in 1966','was never established'],2),
  ('Post-WWII immigration to Canada was significant because ___.',['it had no effect','immigrants came from fewer countries','large numbers of displaced Europeans and later people from around the world reshaped Canada\'s population, economy, and culture','only European refugees came'],2),
  ('The Canada Pension Plan (CPP), established in 1965, was designed to ___.',['fund military spending','provide retirement income security to Canadian workers','only help the wealthy','only benefit Quebec'],1)])]),
day(30,[
L('Year-End Celebration: Reflecting on Learning','Students reflect on their literacy growth through the year, share writing accomplishments, and set goals for Grade 7 language arts.',[
  ('Reflecting on your learning means ___.',['forgetting what you studied','thinking critically about how your skills have grown, what you found challenging, and what you\'re proud of','copying your best work','only reviewing test scores'],1),
  ('Setting a literacy goal for Grade 7 means ___.',['giving up on improving','identifying a specific reading, writing, or communication skill you want to develop and making a plan','only choosing what books to read','only for students who failed'],1),
  ('A portfolio of your best writing shows ___.',['only your weakest work','only test scores','your growth as a writer over the year — varied pieces that demonstrate different skills and your development','only long essays'],2),
  ('Sharing a piece of writing with an audience shows ___.',['it is finished forever','bravery and communication skills, and helps writers understand how others respond to their work','only for perfect pieces','only for publication'],1),
  ('The most important writing habit you can build is ___.',['only writing when required','writing only for teachers','writing regularly, reading widely, and viewing revision as an essential part of the process','only grammar'],2)]),
M('Grade 6 Math Year Review','Students consolidate key Grade 6 math concepts: ratios, percentages, integers, algebra, geometry, measurement, and data.',[
  ('Simplify the ratio 15:25.',['15:25','3:5','5:3','1:5'],1),
  ('What is 30% of 150?',['45','30','50','40'],0),
  ('Solve: 4x − 3 = 13',['x = 4','x = 2.5','x = 5','x = 10'],0),
  ('A rectangular prism is 6 cm × 5 cm × 4 cm. Volume = ?',['15 cm³','60 cm³','120 cm³','300 cm³'],2),
  ('What is the mean of 8, 12, 15, 9, 11?',['11','55','10','12'],0)]),
Sc('Grade 6 Science Year Review','Students review all Grade 6 science strands: biodiversity, flight, electricity, optics, and Earth systems.',[
  ('Domain, Kingdom, Phylum, Class, Order, Family, Genus, Species — this is the ___.',['water cycle','rock cycle','electromagnetic spectrum','biological classification hierarchy (taxonomy)'],3),
  ('The four forces of flight are ___.',['push, pull, up, down','lift, weight, thrust, drag','air, gravity, speed, angle','force, mass, acceleration, velocity'],1),
  ('In a series circuit with 3 bulbs, if one bulb fails ___.',['only that bulb goes out','all bulbs remain on','all bulbs go out because current has only one path','only the next bulb fails'],2),
  ('A convex lens ___.',['diverges light rays','has no effect on light','converges light rays to a focal point','absorbs all light'],2),
  ('Plate tectonics explains ___.',['why it rains','how electricity works','why light bends','why continents move and why earthquakes and volcanoes occur at plate boundaries'],3)]),
SS('Grade 6 Social Studies Year Review','Students review ancient civilisations, exploration, WWI and WWII, and Canada\'s development into a modern nation.',[
  ('Which ancient civilisation first developed democracy?',['Rome','Egypt','Greece (specifically Athens)','China'],2),
  ('The Columbian Exchange describes ___.',['a stock market','the transfer of goods, species, diseases, and ideas between the Old and New Worlds after 1492','a peace treaty','only gold and silver trade'],1),
  ('The MAIN causes of WWI stand for ___.',['Military, Alliances, Imperialism, Nationalism','Money, Army, Industry, Nations','Manufacturing, Alliances, Independence, Neutrality','Military, Aggression, Imperialism, Nationalism'],0),
  ('Canada declared war on Germany in WWII ___.',['the same day as Britain','before Britain','a week after Britain, showing Canadian independence','never'],2),
  ('Multiculturalism became official Canadian government policy in ___.',['1867','1919','1971','1982'],2)])])
]

append_to(6, g6_extra)
print('Grade 6 days 16-30 appended.')
