#!/usr/bin/env python3
"""Grade 8 — days 1-15."""
import sys
sys.path.insert(0,'/sessions/wonderful-keen-tesla/mnt/gradesbooster')
from gen_curriculum import sub,day,write_new

U='https://tvolearn.com/pages/grade-8'
R='TVO Learn: Grade 8'

def L(t,s,q): return sub('Language',t,s,R,U,q)
def M(t,s,q): return sub('Math',t,s,R,U,q)
def Sc(t,s,q): return sub('Science',t,s,R,U,q)
def H(t,s,q): return sub('History',t,s,R,U,q)

g8=[
day(1,[
L('Reading Strategies: Inference and Evidence','Readers make inferences by combining text evidence with background knowledge. Students practise identifying implicit meaning and citing specific textual evidence.',[
  ('An inference is ___.',['a direct quote from the text','a summary of the whole text','a conclusion drawn by combining text clues with background knowledge','a definition of a word'],2),
  ('Textual evidence is ___.',['your personal opinion about the text','specific words, phrases, or details from the text that support a claim or inference','a paraphrase of the main idea','the author\'s biography'],1),
  ('When an author implies something without stating it directly, readers must ___.',['skip that part','ask the teacher','make an inference using context clues and prior knowledge','only read literal statements'],2),
  ('Which question requires an inference to answer?',['What year was the novel published?','How many characters are in the story?','Why does the character seem afraid even though she smiles?','What is the title of the book?'],2),
  ('To support an inference, you should ___.',['guess and move on','cite the specific passage from the text that led you to that conclusion','rely only on personal experience','summarise the entire chapter'],1)]),
M('Number Sense: Powers and Scientific Notation','Students work with powers (base and exponent), evaluate expressions, and write large/small numbers in scientific notation.',[
  ('In 5³, the base is ___ and the exponent is ___.',['3 and 5','5 and 3','5 and 5','3 and 3'],1),
  ('Evaluate 2⁴.',['8','16','24','32'],1),
  ('Scientific notation writes numbers as ___.',['fractions','a number between 1 and 10 multiplied by a power of 10','a number times 100','decimals only'],1),
  ('Write 34 000 in scientific notation.',['3.4 × 10³','34 × 10³','3.4 × 10⁴','0.34 × 10⁵'],2),
  ('Which correctly converts 6.02 × 10³ to standard form?',['60.2','602','6020','60200'],2)]),
Sc('Cells: Structure and Function','Students examine the cell as the basic unit of life. They compare plant and animal cells and identify organelles and their functions.',[
  ('The cell theory states ___.',['only animals have cells','cells are the basic unit of life, all living things are made of cells, and all cells come from pre-existing cells','only plants have cells','cells are not alive'],1),
  ('Which organelle is the "control centre" of the cell?',['Mitochondria','Cell wall','Nucleus','Vacuole'],2),
  ('Mitochondria are responsible for ___.',['storing water','producing proteins','photosynthesis only','producing energy (ATP) through cellular respiration'],3),
  ('Which structure is found in plant cells but NOT in animal cells?',['Nucleus','Cell membrane','Mitochondria','Cell wall and chloroplasts'],3),
  ('The cell membrane ___.',['is only in plant cells','controls what enters and exits the cell','produces energy','stores genetic information'],1)]),
H('New France: Colonisation and Society','Students explore the establishment of New France, the role of the fur trade, relations with Indigenous peoples, and French colonial society.',[
  ('New France was established primarily because of ___.',['gold mining','the fur trade, which was enormously profitable and drove French interest in North America','farming','religious persecution'],1),
  ('The seigneurial system in New France was ___.',['a democratic land system','a system of land grants where seigneurs received land and censitaires (tenant farmers) farmed it in exchange for rent and duties','a system of slave labour','an Indigenous land management system'],1),
  ('The Catholic Church in New France played ___.',['no role','a minor economic role only','a central role in education, social services, and cultural life — it was the most powerful institution','a purely political role'],2),
  ('Relations between French colonists and Indigenous peoples were shaped by ___.',['complete cooperation always','competition and conflict only','a complex mix of trade alliances (especially with the Huron-Wendat), military alliances, cultural exchange, and devastating disease and displacement','total indifference on both sides'],2),
  ('Samuel de Champlain\'s significance to New France includes ___.',['he only explored, never settled','founding Quebec City (1608), mapping New France, forging Indigenous alliances, and governing the colony','defeating the British in battle','discovering the St. Lawrence River'],1)])]),
day(2,[
L('Writing: Thesis Development','Students craft strong thesis statements for analytical and argumentative essays. A thesis must be specific, debatable, and guide the essay\'s argument.',[
  ('A thesis statement should be ___.',['a fact everyone agrees with','a question','a broad topic sentence','a specific, debatable claim that tells readers what the essay will argue and why'],3),
  ('Which is the strongest thesis statement?',['World War II was a major event.','There were many causes of World War II.','The Treaty of Versailles was a significant cause of World War II.','The Nazi\'s policy of aggressive expansion, enabled by Allied appeasement, was the primary cause of World War II.'],3),
  ('A thesis statement appears ___.',['only in the conclusion','throughout every paragraph','at the end of the introduction paragraph, guiding the reader into the body of the essay','at the beginning of each body paragraph'],2),
  ('A debatable thesis means ___.',['it is obviously true','it cannot be argued against','it is obviously false','a reasonable person could disagree with or argue against it'],3),
  ('A thesis statement should NOT be ___.',['specific','arguable','a statement of pure, undisputed fact with no room for argument','analytical'],2)]),
M('Proportional Reasoning: Rates and Ratios','Students solve problems involving unit rates, proportions, and percent change. They distinguish proportional from non-proportional relationships.',[
  ('A unit rate expresses a ratio as ___.',['a fraction only','a rate with a denominator of 1','any ratio','a percentage'],1),
  ('If 5 kg of apples cost $8.75, the unit price is ___.',['$1.50/kg','$1.65/kg','$1.75/kg','$43.75/kg'],2),
  ('A proportion states that ___.',['two sums are equal','two products are equal','two differences are equal','two ratios are equal'],3),
  ('Solve the proportion: 3/4 = x/20',['x = 12','x = 15','x = 16','x = 5'],1),
  ('Percent change = ___.',['(new − old) / new × 100','(old − new) / new × 100','(new − old) / old × 100','new / old × 100'],2)]),
Sc('Cells: Cell Division and Specialisation','Students explore mitosis (cell division for growth and repair), meiosis (for reproduction), and how cells specialise into tissues, organs, and systems.',[
  ('Mitosis results in ___.',['two genetically identical daughter cells','four genetically different cells','one cell dividing into eight','cells with half the DNA'],0),
  ('Meiosis results in ___.',['two identical cells','four genetically unique cells with half the chromosomes (gametes for sexual reproduction)','one large cell','identical twins'],1),
  ('Cell specialisation means ___.',['all cells look the same','cells change into random types','cells develop specific structures and functions suited to a particular role in the organism','only occurs in plants'],2),
  ('The correct order of organisation from smallest to largest is ___.',['organ → tissue → cell → organ system','cell → tissue → organ → organ system → organism','tissue → cell → organ → organism','organism → organ → tissue → cell'],1),
  ('Why can\'t most specialised cells undergo unlimited division?',['They can always divide','They lose their specialised function; highly specialised cells sacrifice replication ability for their specific role','They are too small','They have no nucleus'],1)]),
H('The British Conquest and After','Students examine the Seven Years\' War in North America (1756–1763), the Battle of the Plains of Abraham, and the subsequent British governance of Quebec.',[
  ('The Battle of the Plains of Abraham (1759) was significant because ___.',['France won and kept New France','It had no lasting impact','The British defeat of France led to Britain gaining control of New France','The battle was a draw'],2),
  ('The Treaty of Paris (1763) ___.',['gave New France back to France','made New France independent','formally transferred New France to British control, ending French colonial rule','created Canada as a country'],2),
  ('The Royal Proclamation of 1763 ___.',['ignored Indigenous peoples','gave Quebec to France','established British governance in Quebec and recognised Indigenous peoples\' land rights west of the Appalachians','abolished the fur trade'],2),
  ('The Quebec Act of 1774 ___.',['made English the only language','abolished Catholicism in Quebec','restored French civil law, protected the Catholic Church, and expanded Quebec\'s territory — angering American colonists','granted Quebec independence'],2),
  ('For French Canadians after the conquest, the most pressing concern was ___.',['economic development only','preserving their language, religion, civil law, and cultural identity under British rule','joining the American colonies','establishing a new French empire'],2)])]),
day(3,[
L('Literary Analysis: Themes in Fiction','Students identify and analyse the major themes in fiction. They support thematic interpretations with specific textual evidence and consider how different readers may interpret the same theme.',[
  ('A theme in literature is ___.',['the setting of the story','the main character\'s name','a central message or insight about human experience that the text conveys','a summary of the plot'],2),
  ('How does a writer convey theme?',['By stating it in a title note','By telling readers directly in a summary','Through characters\' actions, conflicts, dialogue, symbols, and the consequences of choices','Only through the narrator'],2),
  ('Which is a theme (not a topic)?',['Friendship','War','Love','Unchecked ambition leads to self-destruction'],3),
  ('A text can have ___.',['only one theme','exactly two themes','no themes','multiple themes that may even seem to contradict each other'],3),
  ('To support a thematic interpretation, you should ___.',['only state your opinion','cite specific passages and explain how those details develop the theme','summarise the entire plot','only use quotes from the author\'s interviews'],1)]),
M('Linear Equations: Solving Multi-Step','Students solve multi-step linear equations with variables on one or both sides. They check solutions by substitution.',[
  ('Solve: 2x + 5 = 17',['x = 11','x = 6','x = 5','x = 4'],1),
  ('Solve: 3x − 4 = 2x + 7',['x = 3','x = 11','x = 7','x = −11'],1),
  ('To solve an equation with variables on both sides, first ___.',['multiply both sides by zero','add the variables together','collect variable terms on one side and constant terms on the other','ignore one side'],2),
  ('Check: Is x = 4 a solution to 5x − 3 = 17?',['No, because 5(4) − 3 = 17 ✓','Yes, because 5(4) − 3 = 17 ✓','No, because 17 ≠ 20','Yes, but the equation is wrong'],1),
  ('Solve: 4(x + 3) = 28',['x = 7','x = 4','x = 31/4','x = 10'],1)]),
Sc('Reproduction: Sexual and Asexual','Students compare sexual and asexual reproduction in plants and animals. They understand the advantages of each strategy in different contexts.',[
  ('Asexual reproduction involves ___.',['two parents','gametes','fertilisation','one parent producing genetically identical offspring'],3),
  ('Sexual reproduction involves ___.',['one parent only','no genetic variation','the joining of two gametes to produce offspring with genetic variation','cloning'],2),
  ('An advantage of asexual reproduction is ___.',['genetic diversity','slower reproduction','rapid reproduction without a mate, useful in stable environments','resistance to disease'],2),
  ('An advantage of sexual reproduction is ___.',['only one parent needed','faster reproduction','no energy cost','genetic variation, which increases a population\'s ability to adapt to changing environments'],3),
  ('Budding, as in yeast and hydra, is a form of ___.',['sexual reproduction','fertilisation','meiosis','asexual reproduction'],3)]),
H('Loyalists and the American Revolution','Students examine why the American Revolution occurred, who the Loyalists were, and how their migration to Canada shaped British North America.',[
  ('Loyalists were ___.',['colonists who supported American independence','Indigenous peoples who allied with France','colonists who remained loyal to the British Crown during and after the American Revolution','British soldiers stationed in America'],2),
  ('The main grievances of American colonists that led to revolution included ___.',['too much freedom','excellent representation in Parliament','taxation without representation and restrictions on westward expansion','being forced to speak French'],2),
  ('Why did many Loyalists migrate to what is now Canada after 1783?',['They were forced out of Canada','They preferred the climate','They faced persecution in the United States and sought refuge in British territories','They received no land grants'],2),
  ('The arrival of Loyalists in British North America led to ___.',['the creation of New France','the founding of Upper Canada (Ontario) and New Brunswick as separate colonies','the end of British rule','the departure of all French settlers'],1),
  ('The Constitutional Act of 1791 divided Quebec into ___.',['Upper and Lower Canada, with separate elected assemblies','three provinces','one united colony','independent states'],0)])]),
day(4,[
L('Grammar: Sentence Variety and Syntax','Students use a variety of sentence structures (simple, compound, complex, compound-complex) to improve writing fluency and impact. They avoid common errors like comma splices and run-ons.',[
  ('A compound-complex sentence has ___.',['one independent clause only','two independent clauses and at least one dependent clause','only dependent clauses','one of each type of clause'],1),
  ('A comma splice is ___.',['a correctly punctuated compound sentence','a sentence with a subordinating conjunction','an error where two independent clauses are joined with only a comma, no conjunction','a sentence with too many commas'],2),
  ('Which is a run-on sentence?',['She ran quickly.','Although it was late, he stayed.','She ran quickly, and he followed.','The storm arrived we had no warning.'],3),
  ('Sentence variety improves writing because ___.',['longer sentences are always better','shorter sentences are always better','varied sentence structures create rhythm, emphasise key points, and keep readers engaged','only grammar matters'],2),
  ('Which correctly joins two independent clauses?',['She studied hard, she passed the exam.','She studied hard she passed the exam.','She studied hard; therefore, she passed the exam.','She studied hard and she passed the exam no comma needed'],2)]),
M('Geometry: Pythagorean Theorem','Students understand and apply the Pythagorean Theorem (a² + b² = c²) to find missing side lengths in right triangles and solve real-world problems.',[
  ('The Pythagorean Theorem states that in a right triangle ___.',['a + b = c','a² − b² = c²','a² + b² = c² where c is the hypotenuse','a × b = c²'],2),
  ('The hypotenuse is ___.',['the shortest side','any side','the side opposite the right angle (always the longest side)','the vertical side'],2),
  ('A right triangle has legs of 3 cm and 4 cm. The hypotenuse = ?',['5 cm','7 cm','6 cm','25 cm'],0),
  ('A ladder 10 m long leans against a wall. The base is 6 m from the wall. How high does it reach?',['8 m','7 m','4 m','16 m'],0),
  ('Can the Pythagorean Theorem be used on ANY triangle?',['Yes, always','No, only on right triangles','Only on equilateral triangles','Only on isosceles triangles'],1)]),
Sc('Fluids: Properties and Pressure','Students explore the properties of fluids (liquids and gases), viscosity, density, buoyancy, and how pressure works in fluids.',[
  ('Viscosity is ___.',['the mass of a fluid','the colour of a fluid','a fluid\'s resistance to flow — high viscosity means slow flow (honey); low viscosity means fast flow (water)','the boiling point of a fluid'],2),
  ('Density of a fluid is ___.',['its volume only','its mass only','mass per unit volume (D = m/V)','its temperature'],2),
  ('An object floats when ___.',['it is very large','it is made of metal','its density is less than the density of the fluid it is placed in','its density is greater than the fluid'],2),
  ('Pressure in a fluid increases with ___.',['decreasing depth','increasing depth (due to the increasing weight of fluid above)','the colour of the fluid','only temperature'],1),
  ('Pascal\'s principle states that ___.',['pressure decreases in fluids','pressure is applied only to the bottom of a fluid','pressure applied to an enclosed fluid is transmitted equally in all directions','fluids do not transmit pressure'],2)]),
H('The War of 1812','Students examine the causes, key battles, and consequences of the War of 1812 for Canada, the United States, Britain, and Indigenous peoples.',[
  ('A main cause of the War of 1812 was ___.',['Canada invading the United States','a trade dispute between France and Britain only','British impressment of American sailors and trade interference, plus American desire for westward expansion','a Canadian declaration of war'],2),
  ('Tecumseh was significant during the War of 1812 because ___.',['he led American forces','he founded Upper Canada','he was a Shawnee leader who allied with Britain to resist American expansion, contributing crucially to early British-Canadian victories','he negotiated the peace treaty'],2),
  ('The burning of York (now Toronto) in 1813 ___.',['ended the war','was a British victory','was an American victory that destroyed the capital of Upper Canada','had no military significance'],2),
  ('The Treaty of Ghent (1814) ended the war ___.',['with clear American victory','with clear British victory','largely restoring pre-war boundaries — neither side gained or lost significant territory','with Canadian independence'],2),
  ('The War of 1812 contributed to Canadian identity by ___.',['proving Canada wanted to join the United States','having no lasting impact','creating a sense of shared defence and pride among colonists who had helped repel American invasion','leading to Confederation immediately'],2)])]),
day(5,[
L('Media Literacy: Bias and Perspective','Students identify bias in media sources. They understand how word choice, framing, omission, and visual selection can shape audience perception.',[
  ('Media bias refers to ___.',['only deliberate lying','any factual error in reporting','any slant, framing, or selection of information in media that favours one perspective over another','only political bias'],2),
  ('A news article\'s headline can show bias by ___.',['reporting facts accurately','using emotionally charged words that frame the story favourably or unfavourably before the reader even reads the content','including photos','citing sources'],1),
  ('Omission bias in media occurs when ___.',['everything relevant is included','only negative news is published','important information that would change the reader\'s interpretation is left out','only images are used'],2),
  ('To read media critically, you should ___.',['trust all major outlets','trust no sources','consider the source\'s ownership, funding, stated purpose, and whether multiple credible sources report the same information','only read social media'],2),
  ('Which action best demonstrates media literacy?',['Reading only one trusted news source','Avoiding all news','Comparing coverage of the same event across multiple sources with different perspectives','Only watching videos'],2)]),
M('Analytic Geometry: Slope and y-intercept','Students calculate slope from two points, write equations in slope-intercept form (y = mx + b), and graph linear equations.',[
  ('Slope (m) is calculated as ___.',['rise × run','run / rise','rise / run (change in y over change in x)','y / x'],2),
  ('The y-intercept (b) is ___.',['the slope of the line','where the line crosses the x-axis','where the line crosses the y-axis','the x-coordinate only'],2),
  ('In y = 3x − 2, the slope is ___ and the y-intercept is ___.',['−2 and 3','3 and −2','3 and 2','2 and 3'],1),
  ('The slope of a line through (1,2) and (3,8) is ___.',['2','3','4','6'],1),
  ('A line with slope 0 is ___.',['vertical','diagonal','undefined','horizontal'],3)]),
Sc('Fluids: Hydraulics and Pneumatics','Students explore how hydraulic and pneumatic systems use fluid pressure to transmit force and do work. They examine real-world applications.',[
  ('Hydraulic systems use ___.',['gases only','solid materials','liquids (usually oil) to transmit pressure and force','electricity only'],2),
  ('Pneumatic systems use ___.',['liquids','solids','compressed gases (usually air) to transmit force','only steam'],2),
  ('A hydraulic lift works because ___.',['the fluid is heated','Pascal\'s principle: pressure applied to an enclosed liquid is transmitted equally in all directions, multiplying force over a larger area','the piston is magnetic','gravity pulls the fluid'],1),
  ('Which is a real-world application of hydraulics?',['Bicycle tyres','Hot-air balloons','Car brakes and construction equipment','Speakers'],2),
  ('An advantage of pneumatic systems over hydraulic systems is ___.',['more force per unit','liquids are lighter','compressed air is readily available, leaks are less messy, and systems are lighter','they are always cheaper'],2)]),
H('Responsible Government and Reform','Students examine the Rebellions of 1837, the Durham Report, and the achievement of Responsible Government in 1848.',[
  ('The Rebellions of 1837 in Upper and Lower Canada were caused by ___.',['foreign invasion','American aggression','frustration with undemocratic governance — the elected assemblies had little power while appointed councils dominated','economic success'],2),
  ('William Lyon Mackenzie (Upper Canada) and Louis-Joseph Papineau (Lower Canada) were ___.',['British governors','leaders of the 1837 reform movements who demanded responsible government','military generals who defeated the British','Loyalist founders'],1),
  ('The Durham Report (1839) recommended ___.',['independence for Canada','keeping the existing system','uniting Upper and Lower Canada and eventually granting responsible government','separating the colonies further'],2),
  ('Responsible government means ___.',['the governor has total power','only appointed officials govern','the executive (cabinet) is responsible to (must maintain the confidence of) the elected legislative assembly, not to the Crown','elected officials can be overruled by Britain at any time'],2),
  ('Responsible government was achieved in the Province of Canada in ___.',['1791','1837','1867','1848, when the governor accepted that the elected majority must govern'],3)])]),
day(6,[
L('Reading: Non-Fiction Structures','Students identify and analyse different non-fiction text structures: cause/effect, compare/contrast, problem/solution, chronological order, and description.',[
  ('Which text structure is used in a passage that explains how deforestation leads to soil erosion?',['Compare/contrast','Problem/solution','Chronological order','Cause and effect'],3),
  ('Signal words for compare/contrast text structure include ___.',['first, then, next','because, as a result, therefore','similarly, on the other hand, however, in contrast','for example, such as, specifically'],2),
  ('A problem/solution structure ___.',['lists events in order','describes two things side by side','compares two texts','identifies an issue and proposes one or more ways to address it'],3),
  ('Chronological order text structure ___.',['always discusses causes','presents events or steps in time sequence','compares two ideas','explains why something happened'],1),
  ('Recognising text structure helps readers ___.',['only identify vocabulary','only find the main idea','understand how information is organised, predict content, and comprehend relationships between ideas more efficiently','count paragraphs'],2)]),
M('Geometry: Circle Measurements','Students calculate circumference (C = πd or 2πr) and area (A = πr²) of circles and apply these formulas in real-world contexts.',[
  ('The circumference formula is ___.',['C = πr²','C = 2πr or πd','C = 2r','C = r²π'],1),
  ('The area formula for a circle is ___.',['A = πd','A = 2πr','A = πr²','A = πd²'],2),
  ('A circle has radius 5 cm. Circumference = ? (use π ≈ 3.14)',['15.70 cm','78.5 cm','31.4 cm','62.8 cm'],2),
  ('A circle has diameter 10 m. Area = ? (use π ≈ 3.14)',['31.4 m²','78.5 m²','314 m²','15.7 m²'],1),
  ('If the radius doubles, the area ___.',['doubles','stays the same','quadruples (increases by a factor of 4)','triples'],2)]),
Sc('Cells: Genetics Introduction','Students are introduced to heredity — how traits pass from parents to offspring through genes and chromosomes. They explore dominant/recessive alleles and Punnett squares.',[
  ('Genes are ___.',['proteins in the blood','sections of DNA on chromosomes that carry instructions for specific traits','only in plant cells','made of amino acids'],1),
  ('An allele is ___.',['a type of chromosome','one version of a gene (e.g., the allele for brown eyes vs. blue eyes)','a type of cell','a protein'],1),
  ('A dominant allele ___.',['is always expressed in the phenotype even if only one copy is present','only shows when two copies are present','is always harmful','is rarer than recessive alleles'],0),
  ('A recessive allele ___.',['always shows in the phenotype','disappears after one generation','is expressed in the phenotype only when two copies (homozygous recessive) are present','is always beneficial'],2),
  ('A Punnett square is used to ___.',['draw cell diagrams','predict the probability of offspring inheriting specific traits from parents','only show dominant traits','map chromosomes'],1)]),
H('Confederation: Causes and Process','Students explore the political, economic, and military pressures that led to Confederation in 1867 and the roles of the Fathers of Confederation.',[
  ('The main pressures that drove Confederation in the 1860s included ___.',['only economic reasons','only military threats','political deadlock in the Province of Canada, fear of American expansionism, railway financing, and British pressure to reduce defence costs','religious conflict only'],2),
  ('The Charlottetown Conference (1864) was significant because ___.',['it created the Senate','it ended the American Civil War','it was the first major meeting at which Canadian and Maritime politicians discussed Confederation','it adopted the Constitution'],2),
  ('The British North America Act (1867) created ___.',['a republic','a fully independent nation immediately','the Dominion of Canada, a federal state with Ontario, Quebec, Nova Scotia, and New Brunswick as founding provinces','a colony of France'],2),
  ('Who was the first Prime Minister of Canada?',['George-Étienne Cartier','D\'Arcy McGee','Thomas D\'Arcy McGee','Sir John A. Macdonald'],3),
  ('Federal division of powers means ___.',['only the federal government has power','only provinces have power','some powers belong to the federal government, some to provinces, and some are shared','Confederation was temporary'],2)])]),
day(7,[
L('Writing: Analytical Paragraph (PEEL)','Students write well-structured analytical paragraphs using the PEEL structure: Point, Evidence, Explanation, Link.',[
  ('In the PEEL structure, "Point" means ___.',['a quotation from the text','the topic sentence that states the paragraph\'s main argument','the concluding sentence only','the connection to next paragraph'],1),
  ('"Evidence" in PEEL means ___.',['your personal opinion','a transition sentence','specific textual evidence (quote, paraphrase, data) that supports the point','a link back to the thesis'],2),
  ('"Explanation" in PEEL means ___.',['another piece of evidence','the topic sentence repeated','the analysis that explains HOW the evidence supports the point','the conclusion'],2),
  ('"Link" in PEEL means ___.',['the opening sentence','the evidence sentence','a sentence that connects the paragraph back to the thesis or forward to the next idea','another analysis'],2),
  ('Strong analytical writing requires ___.',['more personal pronouns','plot summary instead of analysis','as many quotes as possible','close analysis of textual evidence that connects to a broader argument, not just retelling what happens'],3)]),
M('Data Management: Probability','Students calculate theoretical and experimental probability, including compound events. They use tree diagrams and sample spaces.',[
  ('The probability of an event ranges from ___.',['0 to 100','−1 to 1','0 to 1','1 to 10'],2),
  ('A sample space lists ___.',['only the most likely outcomes','only two outcomes','all possible outcomes of an experiment','only favourable outcomes'],2),
  ('A tree diagram helps find probabilities by ___.',['drawing only one branch','visually showing all possible outcomes of sequential events through branching','eliminating impossible events','replacing calculations'],1),
  ('The probability of flipping heads twice in a row is ___.',['1/2','1/4','1/3','2/4'],1),
  ('If P(A) = 0.3, what is P(not A)?',['0.3','0.6','0.7','0.03'],2)]),
Sc('Systems in Action: Mechanical Systems','Students explore mechanical systems including gears, pulleys, levers, and how these are combined in machines to change force, speed, and direction.',[
  ('A gear train transmits ___.',['electrical signals','fluid pressure','rotational motion and force between shafts, allowing speed and torque to be changed','only up-down motion'],2),
  ('When a small gear drives a large gear, the large gear ___.',['turns faster','turns at the same speed','turns slower but with more torque (force)','stops completely'],2),
  ('Mechanical advantage is ___.',['the number of gears in a system','the ratio of output force to input force — it tells you how much a machine multiplies force','the speed of the machine','the size of the machine'],1),
  ('A fixed pulley changes ___.',['the magnitude of force','the mechanical advantage only','the direction of force (you pull down to lift up) but not the magnitude','both force and direction equally'],2),
  ('Which system has a mechanical advantage of 2?',['A lever where effort arm = load arm','A single fixed pulley','A system where you apply 50 N to lift 100 N','A gear where input and output gears are equal'],2)]),
H('Building a Nation: 1867–1900','Students examine how Canada expanded after Confederation: Manitoba (1870), BC (1871), CPR, North-West Resistance, and the numbered treaties.',[
  ('The numbered treaties (1871–1921) were ___.',['gifts of land to settlers','agreements between the Canadian government and First Nations peoples that defined land rights, reserves, and annual payments','proclamations of Indigenous independence','private land sales'],1),
  ('The Canadian Pacific Railway (completed 1885) was important because ___.',['it connected the East Coast to Europe','it was primarily a luxury project','it fulfilled the promise to BC, physically united Canada, and allowed prairie settlement and resource extraction','it replaced all other transportation'],2),
  ('The North-West Resistance of 1885 was led by ___.',['John A. Macdonald','George-Étienne Cartier','Gabriel Dumont and Louis Riel, defending Métis land rights in what is now Saskatchewan','Tecumseh'],2),
  ('Louis Riel is a controversial historical figure because ___.',['he was never important','history is unambiguous about him','he was executed for treason by the Canadian government, but is also seen as a defender of Métis rights and a Father of Manitoba','he was a British loyalist'],2),
  ('Manitoba joined Confederation in 1870 as a result of ___.',['a Canadian military conquest','a federal election','the Red River Resistance, in which Riel negotiated Manitoba\'s entry as a province with protections for Métis land and language','a British proclamation'],2)])]),
day(8,[
L('Oral Communication: Formal Presentation Skills','Students plan and deliver a formal presentation. They apply skills in organisation, eye contact, voice projection, pacing, and responding to questions.',[
  ('Effective formal presentations include ___.',['reading word-for-word from notes','memorising every word rigidly','a clear introduction, organised body with transitions, conclusion, confident eye contact, and varied tone','only visual aids'],2),
  ('Why should you avoid reading directly from slides or notes?',['You should always read from notes','It is fine for all audiences','Reading prevents natural delivery — it limits eye contact, lowers engagement, and makes the presentation feel scripted and impersonal','Only for long presentations'],2),
  ('Pacing in a presentation means ___.',['how many slides you use','the number of facts you include','controlling the speed of delivery — speaking slowly enough to be understood but briskly enough to hold attention','only the conclusion'],2),
  ('When responding to an audience question, you should ___.',['ignore it','pretend you didn\'t hear','restate the question to ensure everyone heard it, then answer clearly and honestly — admitting if you don\'t know','argue with the questioner'],2),
  ('Body language during a presentation includes ___.',['only words','only volume','posture, eye contact, gestures, and movement — all of which affect how confident and credible you appear to the audience','only facial expressions'],2)]),
M('Integers and Rational Numbers','Students extend operations to all integers and rational numbers. They add, subtract, multiply, and divide positive and negative fractions and decimals.',[
  ('(−3) × (−5) = ___.',['−15','8','15','−8'],2),
  ('(−12) ÷ 4 = ___.',['−3','3','−8','48'],0),
  ('(−2/3) + (1/2) = ___.',['−1/6','1/6','−1/2','3/5'],0),
  ('The product of a positive and a negative number is always ___.',['positive','zero','negative','undefined'],2),
  ('(−4.5) − (−2.0) = ___.',['−6.5','−2.5','2.5','6.5'],1)]),
Sc('Optics: Light, Colour, and Vision','Students extend their understanding of light, exploring how the eye perceives colour, how additive and subtractive colour mixing works, and modern applications of optics.',[
  ('Additive colour mixing (light) combines ___.',['pigments','inks','coloured lights — red + green + blue (RGB) combine to make white light','only primary colours of paint'],2),
  ('Subtractive colour mixing (pigments) works because ___.',['light is added','pigments emit light','pigments absorb certain wavelengths and reflect others; mixing pigments absorbs more wavelengths, producing darker colours','colours multiply'],2),
  ('The human retina has two types of photoreceptors ___.',['only rods','only cones','rods (sensitive to low light/motion) and cones (sensitive to colour and fine detail)','rods and lenses'],2),
  ('Colour blindness occurs when ___.',['the cornea is damaged','rods are missing','one or more types of cone cells are absent or malfunctioning, making certain colours indistinguishable','the pupil cannot dilate'],2),
  ('Fibre optics transmit information using ___.',['radio waves','electrical signals through copper','pulses of light through thin glass or plastic fibres, enabling high-speed internet and medical imaging (endoscopes)','magnetic fields'],2)]),
H('Immigration and Social Change 1867–1914','Students examine waves of immigration to Canada, the experiences of newcomers, discriminatory policies, and cultural changes in the late 19th and early 20th century.',[
  ('The Canadian government encouraged immigration in the late 1800s primarily to ___.',['limit population growth','compete with Mexico','settle the Prairies, build the CPR, and develop the agricultural and resource economy','reduce cultural diversity'],2),
  ('The Chinese Head Tax (1885–1923) was ___.',['a welcoming program','a tax levied specifically on Chinese immigrants to deter their entry after the CPR was built using Chinese labour','a tax on all immigrants','a land grant program'],1),
  ('The Komagata Maru incident (1914) demonstrated ___.',['Canada\'s open immigration policy','Canada\'s commitment to diversity','Canada\'s racially discriminatory immigration policies, which excluded most non-European immigrants','Canada\'s military strength'],2),
  ('Clifford Sifton\'s immigration policy in the 1890s–1900s targeted ___.',['immigrants from Asia','immigrants from the Caribbean','primarily farmers from Eastern Europe (Ukrainians, Poles) and the United States to settle the Prairies','skilled urban workers from Britain only'],2),
  ('Early immigrant experiences often included ___.',['immediate full acceptance','automatic citizenship and land grants','discrimination, language barriers, harsh pioneer conditions, and pressure to assimilate while trying to maintain cultural identity','only positive experiences'],2)])]),
day(9,[
L('Shakespeare: Introduction to the Plays','Students are introduced to Shakespearean language, dramatic conventions, historical context, and the structure of Shakespearean tragedy and comedy.',[
  ('Shakespeare wrote during ___.',['the Medieval period','the Romantic era','the Elizabethan/Jacobean era (late 16th–early 17th century)','the Victorian era'],2),
  ('Iambic pentameter is ___.',['a type of drama','a poetic metre of 10 syllables per line (5 pairs of unstressed-stressed syllables: da-DUM da-DUM da-DUM da-DUM da-DUM) used extensively by Shakespeare','a type of comedy','a stage direction'],1),
  ('A Shakespearean tragedy typically ends with ___.',['marriage and festivity','a misunderstanding that is resolved','the deaths of main characters as a consequence of a fatal flaw','a happy reunion'],2),
  ('A soliloquy is ___.',['a conversation between two characters','a stage direction','a character\'s speech delivered alone on stage, revealing inner thoughts to the audience but not to other characters','a chorus singing'],2),
  ('Why is understanding Shakespeare\'s context important?',['It is not relevant','To memorise famous quotes','The social, political, and theatrical conventions of Elizabethan England shape the meanings and subtleties of his plays','Only for English literature degrees'],2)]),
M('Analytic Geometry: Systems of Equations','Students solve systems of two linear equations graphically and algebraically (substitution method).',[
  ('A system of two linear equations has a unique solution when ___.',['the lines are parallel','the equations are identical','the two lines intersect at exactly one point','the lines have the same slope'],2),
  ('A system with parallel lines (same slope, different y-intercepts) has ___.',['one solution','infinite solutions','no solution','two solutions'],2),
  ('To solve a system by substitution: solve one equation for one variable, then ___.',['solve the same equation again','substitute that expression into the other equation and solve for the remaining variable','add the equations','multiply the equations'],1),
  ('Solve: y = 2x + 1 and y = −x + 7',['x = 2, y = 5','x = 3, y = 7','x = 2, y = 7','x = 1, y = 3'],0),
  ('Graphically, the solution to a system of equations is ___.',['the y-intercepts','the slopes','the intersection point of the two lines','anywhere on both lines'],2)]),
Sc('Cells: Biotechnology and Ethics','Students explore how biotechnology (genetic engineering, CRISPR, cloning, GMOs) applies cell biology, and consider ethical questions raised by these technologies.',[
  ('Genetic engineering involves ___.',['only cross-breeding animals','selective plant breeding only','deliberately modifying an organism\'s DNA to change its characteristics, add new traits, or correct genetic errors','removing organs'],2),
  ('CRISPR-Cas9 is ___.',['a computer program','a type of microscope','a gene-editing tool that acts like molecular scissors, precisely cutting and editing DNA sequences','a drug treatment'],2),
  ('A GMO (genetically modified organism) is ___.',['only a cloned animal','any organism bred through natural selection','an organism whose genome has been altered through genetic engineering to express a desired trait','only a plant'],2),
  ('One benefit of GM crops is ___.',['they are always more expensive','they never affect ecosystems','they can be engineered for higher yields, pest resistance, drought tolerance, or enhanced nutrition','they eliminate all farming'],2),
  ('An ethical concern about biotechnology is ___.',['there are no concerns','it only helps science','questions about designer babies, unintended ecological consequences, corporate control of food supply, and the limits of scientific intervention in nature','it makes food taste worse'],2)]),
H('World War I: Canada\'s Experience','Students examine Canada\'s military contributions, the home front, the conscription crisis, and how WWI changed Canada\'s international standing.',[
  ('Canada\'s most celebrated military achievement of WWI was ___.',['the invasion of Germany','the Battle of the Atlantic','the Battle of Vimy Ridge (1917), where all four Canadian divisions fought together for the first time','the air campaign over England'],2),
  ('The conscription crisis of 1917 divided Canada primarily along ___.',['class lines','religious lines','rural/urban lines','English-French (linguistic) lines, with most French Canadians opposing conscription'],3),
  ('Women\'s contribution on the home front during WWI led to ___.',['no changes','stricter restrictions','women being granted the right to vote federally in 1918 (with exclusions for some women)','women being banned from public life'],2),
  ('Trench warfare was characterised by ___.',['fast movement and cavalry charges','no casualties','a rapid victory for the Allies','static defensive lines, extremely high casualties, mud, disease, and the use of artillery and poison gas'],3),
  ('The end of WWI left Canada with ___.',['no international recognition','the same colonial status as before','greater international status and autonomy, having signed the Treaty of Versailles separately, reflecting growing independence from Britain','a weakened military'],2)])]),
day(10,[
L('Independent Reading: Novel Study Launch','Students select a novel for in-depth study. They track character, plot, setting, theme, and author\'s craft through journals and analytical response tasks.',[
  ('A reading response journal is most useful when ___.',['you only write summaries of events','you write personal reactions without referring to the text','you combine close observations from the text with your own analysis, questions, and connections','you copy memorable quotations only'],2),
  ('Analysing author\'s craft means ___.',['summarising what happens','listing characters','examining the techniques and choices the author makes (structure, diction, point of view, symbolism) and their effect on the reader','only identifying grammar errors'],2),
  ('Point of view affects a novel because ___.',['it only changes the narrator\'s name','it has no effect','the narrator\'s perspective shapes what information readers access, which characters they trust, and how they interpret events','it only matters in non-fiction'],2),
  ('A motif in literature is ___.',['the protagonist\'s goal','a recurring element (image, symbol, idea) that develops and deepens the work\'s themes','the chapter structure only','the physical description of the setting'],1),
  ('Setting in a novel contributes to ___.',['only the physical geography','only the time period','mood, theme, character development, and conflict — the setting is an active element, not just a backdrop','only the plot'],2)]),
M('Measurement: Surface Area and Volume of 3D Solids','Students calculate surface area and volume of prisms, cylinders, cones, and spheres using formulas.',[
  ('The volume of a cylinder is ___.',['V = πr²','V = 2πrh','V = πr²h','V = 4/3 πr³'],2),
  ('The surface area of a rectangular prism is ___.',['2lw + 2lh + 2wh','l × w × h','2(l + w + h)','lw + lh + wh'],0),
  ('A cylinder has radius 3 cm and height 10 cm. Volume = ? (π ≈ 3.14)',['94.2 cm³','282.6 cm³','188.4 cm³','94.2 cm²'],1),
  ('Volume of a cone = ___.',['πr²h','1/3 πr²h','4/3 πr³','2πr²h'],1),
  ('The surface area of a sphere is ___.',['πr²','2πr²','4/3 πr³','4πr²'],3)]),
Sc('Systems in Action: Fluid Systems','Students connect fluid properties to engineered systems, examining hydraulic and pneumatic applications, and designing simple fluid systems.',[
  ('In a hydraulic system, the working fluid is ___.',['usually a compressible gas','always water','usually an incompressible liquid (hydraulic oil) that transmits force efficiently without compressing','only air'],2),
  ('Why are liquids used in hydraulic systems rather than gases?',['Liquids are cheaper','Gases are too colourful','Liquids are nearly incompressible, so force is transmitted directly and efficiently without energy loss to compression','Liquids are lighter'],2),
  ('A hydraulic jack multiplies force because ___.',['the piston is magnetic','pressure is transmitted equally in all directions, and a small force on a small piston creates high pressure that acts on a much larger piston','friction helps','it uses electricity'],1),
  ('Pneumatic systems (e.g., air brakes on buses) have the advantage of ___.',['being completely noiseless','requiring no energy','using compressed air, which is readily available, clean, and safe (air leaks are not harmful like oil leaks)','producing more force than hydraulics always'],2),
  ('A disadvantage of pneumatic systems is ___.',['they use liquid','they are too heavy','compressed air is slightly compressible, making them less precise than hydraulic systems for exact positioning','they cannot be used in vehicles'],2)]),
H('The Great Depression and Canada','Students examine the causes and impact of the Great Depression (1929–1939) on Canadians, and the political and social responses it generated.',[
  ('The Great Depression began with ___.',['a Canadian bank failure','the start of WWI','the stock market crash of October 1929 in the United States, which spread globally','a drought only in Canada'],2),
  ('In Canada, the Prairies suffered most severely because ___.',['they had the most industry','they were unaffected','drought and falling wheat prices combined to destroy the agricultural economy, creating the "Dirty Thirties"','they had no government'],2),
  ('R.B. Bennett\'s government response to the Depression initially focused on ___.',['social programs and welfare','massive public investment','raising tariffs to protect Canadian industry, which worsened trade and the Depression','nationalising the banks'],2),
  ('The "On to Ottawa Trek" (1935) was ___.',['a tourism campaign','a military march','a protest march by unemployed Canadians from western relief camps to Ottawa to demand government action, ending in the Regina Riot','a political convention'],2),
  ('The Social Credit and CCF parties grew during the Depression because ___.',['traditional parties solved all problems','Canadians were satisfied with the government response','widespread suffering and failure of traditional parties to provide relief led voters to support new political movements offering alternatives','both parties had existed for decades'],2)])]),
day(11,[
L('Writing: The Research Essay — Sources and Integration','Students find, evaluate, and ethically integrate source material into a research essay. They practise paraphrasing, quoting, and citing sources.',[
  ('Plagiarism is ___.',['only copying entire essays','using a dictionary','presenting someone else\'s ideas, words, or work as your own without proper acknowledgement','summarising your own ideas'],2),
  ('Paraphrasing means ___.',['copying text word for word','changing only a few words from the original','restating an author\'s idea completely in your own words and sentence structure, while citing the source','using quotation marks around copied text'],2),
  ('A direct quotation should be used when ___.',['you want to avoid summarising','the original wording is especially powerful, precise, or authoritative — and you always include a citation','you can\'t understand the source','you want to make your essay longer'],1),
  ('Signal phrases (e.g., "According to Smith..." or "Historians argue...") are used to ___.',['hide sources','replace citations','introduce sources smoothly and attribute ideas to their authors within your text','only begin essays'],2),
  ('A Works Cited or bibliography page ___.',['is optional','lists only books','lists all sources consulted and cited, following a consistent citation format (MLA, APA, Chicago), allowing readers to verify your research','is only for academic journals'],2)]),
M('Patterning: Arithmetic and Geometric Sequences','Students identify, extend, and create arithmetic sequences (constant difference) and geometric sequences (constant ratio). They write general terms.',[
  ('An arithmetic sequence has ___.',['a constant ratio between terms','random differences','a constant difference (common difference) between consecutive terms','no pattern'],0),
  ('A geometric sequence has ___.',['a constant difference','no pattern','a constant ratio (common ratio) between consecutive terms','only positive numbers'],2),
  ('The arithmetic sequence 5, 8, 11, 14... has a common difference of ___.',['5','8','3','11'],2),
  ('The geometric sequence 2, 6, 18, 54... has a common ratio of ___.',['2','3','6','4'],1),
  ('The nth term of an arithmetic sequence starting at a with common difference d is ___.',['a + d','a × n','a + (n−1)d','nd + a'],2)]),
Sc('Cells: The Immune System','Students explore how the body defends itself — physical barriers, innate immunity, and adaptive immunity (B cells, T cells, antibodies, vaccines).',[
  ('The first line of defence against pathogens includes ___.',['antibodies','T cells','skin and mucous membranes, which physically block most pathogens','blood cells'],2),
  ('The innate immune response is ___.',['slow and targeted','specific to each pathogen','fast and non-specific — it responds the same way to many different types of invaders','inactive until vaccines are given'],2),
  ('B cells of the adaptive immune system produce ___.',['red blood cells','antibodies that bind to specific antigens on pathogens, marking them for destruction','only hormones','physical barriers'],1),
  ('Vaccines work by ___.',['killing all bacteria','curing active infection','introducing a harmless form of an antigen to train the adaptive immune system to respond quickly if the real pathogen is encountered','replacing antibodies'],2),
  ('Memory cells formed after an infection or vaccination ___.',['disappear quickly','serve no purpose after the initial infection','remain in the body long-term and enable a much faster immune response upon future exposure to the same pathogen','attack all foreign cells'],2)]),
H('WWII: Canada\'s Role','Students examine Canada\'s military contributions to WWII — the Battle of Britain, Dieppe, Sicily, D-Day — and the impact on the home front.',[
  ('Canada\'s contribution to the Battle of Britain (1940) included ___.',['only ground troops','sending a naval fleet only','Royal Canadian Air Force pilots who flew alongside the RAF to defend Britain against German air attack','an invasion of Germany'],2),
  ('The Dieppe Raid (1942) was ___.',['a major Allied victory','irrelevant to Canada','a disastrous Allied amphibious assault on the French coast in which the majority of troops were Canadian, resulting in massive casualties but providing lessons for D-Day','a secret spy mission'],2),
  ('On D-Day (June 6, 1944), Canadian forces landed at ___.',['Gold Beach','Utah Beach','Sword Beach','Juno Beach, one of five Allied landing zones in the Normandy invasion'],3),
  ('On the home front, Japanese Canadians during WWII were ___.',['treated equally','celebrated for contributions','protected by the government','forcibly relocated to internment camps and had their property confiscated — a serious historical injustice'],3),
  ('By the end of WWII, Canada\'s military contribution had ___.',['diminished Canada\'s international standing','had no lasting effect','firmly established Canada as an independent middle power with significant international influence','resulted in colonial dependence'],2)])]),
day(12,[
L('Novel Study: Character and Conflict','Students analyse how conflict shapes character development. They distinguish types of conflict and trace how characters respond and change.',[
  ('The five main types of literary conflict are ___.',['only person vs. person','only internal','person vs. person, person vs. self, person vs. society, person vs. nature, person vs. technology/fate','only two types exist'],2),
  ('An internal conflict (person vs. self) involves ___.',['a character fighting another character','a character battling a storm','a character\'s struggle with their own emotions, moral dilemmas, or competing desires','a character vs. society'],2),
  ('How does conflict drive a narrative?',['It slows the story down','It is optional','It creates tension, forces characters to make choices, and drives the plot forward through rising action toward the climax','Only in action stories'],2),
  ('A character foil is ___.',['a character who never changes','the antagonist always','a character whose contrasting traits highlight qualities of the protagonist','the narrator'],2),
  ('Analysing how a character responds to conflict reveals ___.',['nothing about the character','only physical traits','the character\'s values, strengths, weaknesses, and inner nature — conflict is the crucible that reveals who characters truly are','only plot information'],2)]),
M('Financial Literacy: Simple and Compound Interest','Students calculate simple interest (I = Prt) and compound interest, and understand the difference in long-term growth.',[
  ('Simple interest is calculated using ___.',['I = Prt² ','I = P(1+r)^t','I = Prt (Principal × rate × time)','I = P + r + t'],2),
  ('Compound interest differs from simple interest because ___.',['it is always lower','it is always higher','interest is earned on both the original principal and accumulated interest, causing exponential growth','it uses a different formula for the same result'],2),
  ('You invest $1000 at 5% simple interest for 3 years. Interest earned = ?',['$50','$150','$500','$1150'],1),
  ('The "power of compound interest" refers to ___.',['interest rates decreasing over time','debt disappearing faster','the exponential growth of an investment because interest earns interest, producing much larger returns over time','simple addition of interest'],2),
  ('Why should you start saving early?',['Starting time doesn\'t matter','Later is better','Compound interest means a longer time horizon produces dramatically larger returns — even small amounts saved early grow significantly','Only the amount matters'],2)]),
Sc('Fluids: Environmental Applications','Students connect fluid properties to environmental contexts — ocean currents, atmospheric pressure, water treatment, and the effects of pollution on fluid systems.',[
  ('Ocean currents are driven by ___.',['only wind','only temperature','differences in temperature and salinity (density) in seawater, along with wind and Earth\'s rotation (Coriolis effect)','tidal forces only'],2),
  ('Atmospheric pressure decreases with altitude because ___.',['the air gets warmer','there is more air above you','there is less air (and therefore less weight of air) above you as you go higher','the Earth\'s gravity decreases sharply'],2),
  ('Water treatment plants use ___.',['only chemicals','only filters','physical filtration, chemical treatment (chlorination), and sometimes UV disinfection to remove pathogens and contaminants','boiling only'],2),
  ('Oil spills are particularly harmful to marine ecosystems because ___.',['oil is naturally present in oceans','oil is easily cleaned up','oil floats on water, reducing oxygen exchange, coating marine animals, and persisting in the food chain','they only affect fish'],2),
  ('Microplastics in water systems are concerning because ___.',['they dissolve quickly','they are only aesthetic','they are tiny plastic particles that persist for centuries, accumulate in organisms through the food chain, and carry toxic chemicals','they only affect humans'],2)]),
H('The Cold War and Canada','Students examine the Cold War, Canada\'s role in NATO, the Korean War, the Cuban Missile Crisis, and peacekeeping.',[
  ('The Cold War was a conflict between ___.',['Canada and the United States','France and Germany','the United States and its allies (NATO) and the Soviet Union and its allies (Warsaw Pact) — primarily an ideological struggle between capitalism and communism','China and Japan'],2),
  ('Canada\'s key role in the Cold War included ___.',['neutral isolation','supporting the Soviet Union','membership in NATO, hosting NORAD, contributing to Korean War (1950–53), and participating in peacekeeping missions','invading Eastern Europe'],2),
  ('The Cuban Missile Crisis (1962) involved ___.',['Canada and Britain','France and Germany','the US and USSR in a 13-day nuclear standoff after the USSR placed missiles in Cuba — the closest the Cold War came to nuclear war','China and the US'],2),
  ('UN peacekeeping was pioneered by ___.',['John A. Macdonald','Lester B. Pearson, whose proposal to end the Suez Crisis (1956) earned him the Nobel Peace Prize and established Canada\'s identity as a peacekeeper','Pierre Trudeau','Tommy Douglas'],1),
  ('Canada\'s participation in NORAD (1958) involved ___.',['economic cooperation only','cultural exchange','joint Canada-US air defence of North America against the threat of Soviet nuclear attack','a military conflict with the US'],2)])]),
day(13,[
L('Writing: Persuasive Letter','Students write a formal persuasive letter to a public official or organisation. They apply knowledge of audience, purpose, formal register, and persuasive techniques.',[
  ('A formal letter differs from an informal one in ___.',['using slang and contractions','relying on emotional appeals only','using formal register, proper salutation and closing, professional tone, and precise language appropriate for the addressee','only the length'],2),
  ('The purpose of a persuasive letter is ___.',['to entertain the reader','to describe a scene','to change the reader\'s mind or prompt a specific action, using reasoned argument and evidence','to summarise events'],2),
  ('When writing to a public official, you should ___.',['use slang','write as briefly as possible regardless of content','address them by their proper title, state your position clearly, provide evidence, and suggest a specific action they can take','avoid stating your position'],2),
  ('Which persuasive technique involves showing the reader that the letter-writer\'s position is backed by credible evidence?',['Pathos','Bandwagon','Ethos (establishing credibility and authority)','Ad hominem'],2),
  ('A strong closing paragraph in a persuasive letter ___.',['introduces new arguments','apologises for bothering the reader','restates the request or recommended action clearly and thanks the reader for their time','only says goodbye'],2)]),
M('Geometry: Angle Relationships','Students apply angle relationships — supplementary, complementary, vertically opposite, and angles in parallel lines cut by a transversal — to find unknown angles.',[
  ('Supplementary angles sum to ___.',['90°','45°','360°','180°'],3),
  ('Complementary angles sum to ___.',['180°','90°','360°','270°'],1),
  ('Vertically opposite angles are ___.',['supplementary','complementary','equal to each other','always 90°'],2),
  ('When a transversal crosses two parallel lines, alternate interior angles are ___.',['supplementary','unrelated','equal','complementary'],2),
  ('Co-interior (same-side interior) angles formed by a transversal cutting parallel lines are ___.',['equal','supplementary (sum to 180°)','complementary','vertically opposite'],1)]),
Sc('Light and Optics: Mirrors and Lenses in Technology','Students explore how mirrors and lenses are used in technology — cameras, telescopes, microscopes, corrective lenses, and medical equipment.',[
  ('A refracting telescope uses ___.',['mirrors to form images','radio waves','two convex lenses — an objective lens to gather and focus light and an eyepiece lens to magnify the image','only one lens'],2),
  ('A reflecting telescope uses ___.',['only lenses','a concave mirror to gather and focus light, and an eyepiece lens to magnify','only flat mirrors','prisms only'],1),
  ('A compound microscope magnifies by ___.',['one powerful lens','a mirror and a single lens','two lens systems: the objective lens produces a magnified image and the eyepiece lens magnifies it further','electricity alone'],2),
  ('Corrective lenses for myopia (short-sightedness) are ___.',['convex','flat','concave lenses that diverge light so it focuses correctly on the retina instead of in front of it','only for reading'],2),
  ('MRI (magnetic resonance imaging) differs from X-rays in that ___.',['MRI uses X-radiation','MRI only scans bones','MRI uses magnetic fields and radio waves to image soft tissues without ionising radiation; X-rays use radiation and are best for dense tissues like bone','MRI is a newer word for X-ray'],2)]),
H('Social Movements in Canada: Rights and Equality','Students examine the women\'s suffrage movement, Indigenous rights movements, and the Canadian civil rights movement in the 20th century.',[
  ('Canadian women won the federal right to vote in ___.',['1867','1900','1929','1918 (with exceptions; all women by 1940)'],3),
  ('The "Persons Case" (1929) was significant because ___.',['it granted women the vote','it was irrelevant to women\'s history','the Judicial Committee of the Privy Council ruled that women were "persons" under Canadian law and could be appointed to the Senate','it created the Charter of Rights'],2),
  ('The Indian Act (1876) affected Indigenous peoples by ___.',['granting them full rights','having no lasting impact','imposing strict government control over Indigenous life, banning cultural practices, creating the reserve system, and undermining Indigenous self-governance','being repealed in 1900'],2),
  ('The residential school system in Canada was designed to ___.',['celebrate Indigenous cultures','improve Indigenous education','forcibly assimilate Indigenous children by removing them from their families, banning their languages, and replacing their culture with Euro-Canadian values — causing multigenerational trauma','improve literacy in rural Canada'],2),
  ('The Canadian Human Rights Act (1977) ___.',['had no effect','only applied to immigrants','prohibited discrimination in federal jurisdiction on grounds including race, sex, religion, and disability','replaced the Charter of Rights'],2)])]),
day(14,[
L('Media Creation: Podcast Script','Students plan and write a script for a short informational podcast episode. They learn to write for the ear — using conversational language, clear structure, and engaging hooks.',[
  ('Writing for a podcast differs from writing an essay because ___.',['podcasts have no structure','essays are always shorter','podcast scripts use conversational language, shorter sentences, and audio-specific elements (music, sound effects) since they will be heard, not read','essays are always better'],2),
  ('An effective podcast hook ___.',['begins with a long history lesson','starts with "Welcome to our podcast"','opens with a compelling question, surprising fact, or brief story to immediately grab the listener\'s attention','lists all topics to be covered'],2),
  ('Transitions in a podcast script ___.',['are unimportant','only appear at the beginning','guide listeners through the episode, signalling topic shifts and maintaining flow since listeners can\'t see headings','should be avoided'],2),
  ('Why is clarity especially important in audio media?',['It is not more important','Visual aids compensate','Listeners cannot re-read — they must understand each point as it is spoken, so language must be clear, concise, and well-organised','Only for news podcasts'],2),
  ('A call to action at the end of a podcast episode ___.',['is always inappropriate','ends the podcast abruptly','invites listeners to do something (subscribe, visit a website, reflect on a question, share the episode) — it extends engagement beyond the episode itself','should be very long'],2)]),
M('Probability: Compound Events and Simulations','Students calculate probabilities of independent and dependent compound events and use simulations to explore experimental probability.',[
  ('Independent events are events where ___.',['the first event changes the probability of the second','they happen at the same time','the outcome of one does NOT affect the probability of the other','they must both occur'],2),
  ('P(A and B) for independent events = ___.',['P(A) + P(B)','P(A) − P(B)','P(A) × P(B)','P(A) / P(B)'],2),
  ('Dependent events are events where ___.',['the first event has no effect on the second','they are impossible','the outcome of the first event DOES affect the probability of the second event','they always have equal probability'],2),
  ('A bag has 3 red and 2 blue marbles. You draw one without replacing it. P(red then blue) = ?',['3/5 × 2/5 = 6/25','3/5 × 2/4 = 6/20 = 3/10','2/5 × 3/4 = 6/20','1/2'],1),
  ('A simulation in probability ___.',['always gives exact theoretical results','replaces all probability calculations','uses a model (random number table, spinner, computer) to experimentally estimate probabilities for complex situations','only works with coins'],2)]),
Sc('Review: Science Connections Grade 8','Students connect the four Grade 8 science strands (cells, fluids, mechanical systems, optics) and see their real-world and technological applications.',[
  ('Which science strand best explains how vaccines work?',['Fluids','Mechanical systems','Optics','Cells and the immune system'],3),
  ('Hydraulic brakes in a car apply principles from which strand?',['Cells','Optics','Mechanical systems','Fluids'],3),
  ('The compound microscope is an application of ___.',['fluid mechanics','genetics','cellular respiration','optics (mirrors and lenses)'],3),
  ('Genetic engineering uses knowledge from which strand?',['Fluids','Optics and light','Cells and genetics','Mechanical systems'],2),
  ('Understanding buoyancy helps engineers design ___.',['optical instruments','gene therapies','submarines and ships (fluids and density)','lever systems'],2)]),
H('Canada in the Modern World: 1950s–1980s','Students examine key events: Quiet Revolution, Official Languages Act, Charter of Rights, Constitution Act 1982, and Canada\'s evolving identity.',[
  ('The Quiet Revolution in Quebec (1960s) was ___.',['a military coup','a religious revival','a period of rapid social, political, and cultural change in which Quebec modernised its institutions and French Canadians asserted a distinct identity','a reconciliation with Indigenous peoples'],2),
  ('The Official Languages Act (1969) ___.',['made only English official','made only French official','declared English and French to be Canada\'s two official languages at the federal level','removed all language rights'],2),
  ('The repatriation of the Constitution in 1982 was significant because ___.',['it changed Canada\'s capital','Canada had to get Britain\'s permission to amend its constitution before this — repatriation gave Canada full constitutional independence','it created the provinces','it ended Confederation'],1),
  ('The Canadian Charter of Rights and Freedoms (1982) ___.',['only applies to criminals','has no effect on laws','guarantees fundamental rights and freedoms to all Canadians and allows courts to strike down laws that violate these rights','is not part of the Constitution'],2),
  ('The FLQ Crisis (1970) involved ___.',['a peaceful independence movement','an economic crisis','a Quebec separatist terrorist group that kidnapped and murdered government officials, leading Trudeau to invoke the War Measures Act — a controversial use of emergency powers','a conflict with the United States'],2)])]),
day(15,[
L('Reading: Shakespearean Drama','Students read excerpts from a Shakespeare play (e.g., Macbeth or Romeo and Juliet). They interpret Elizabethan language, identify dramatic conventions, and analyse key scenes.',[
  ('In Shakespearean tragedy, the protagonist\'s downfall is typically caused by ___.',['bad luck alone','supernatural forces only','a fatal flaw (hamartia) — a character weakness that leads to poor decisions and ultimately destruction','external enemies only'],2),
  ('An aside in theatre is ___.',['a stage direction','a character\'s words spoken to another character','a brief remark spoken by a character to the audience, unheard by other characters on stage','a scene description'],2),
  ('The witches in Macbeth serve to ___.',['add comedy','resolve the conflict','introduce supernatural elements that tempt Macbeth, raise questions about fate vs. free will, and foreshadow his downfall','explain the historical setting'],2),
  ('Dramatic irony occurs when ___.',['the audience knows less than the characters','two characters disagree','the audience knows something important that one or more characters do not, creating tension','the plot is confusing'],2),
  ('Analysing a key scene in Shakespeare involves ___.',['only memorising lines','only identifying rhymes','examining language, imagery, power dynamics, themes, and how the scene advances plot or develops character','only summarising what happens'],2)]),
M('Algebra: Polynomials Introduction','Students identify monomials, binomials, and trinomials. They add and subtract polynomials by collecting like terms.',[
  ('A polynomial is ___.',['only a one-term expression','only a two-term expression','an expression of one or more terms consisting of variables and coefficients','a type of equation only'],2),
  ('A binomial has ___.',['one term','two terms','three terms','four terms'],1),
  ('Like terms are ___.',['any terms in an expression','terms with identical variable parts (same variable(s) raised to the same power)','only constant terms','only terms with coefficients'],1),
  ('Simplify: (3x² + 2x − 1) + (x² − 4x + 5)',['4x² − 2x + 4','4x² + 6x + 4','2x² − 2x + 6','4x⁴ − 2x + 4'],0),
  ('Simplify: (5x − 3) − (2x + 1)',['3x − 4','3x − 2','7x − 4','3x + 2'],0)]),
Sc('Cells: Review and Synthesis','Students synthesise their learning about cells, reproduction, genetics, and body systems, connecting ideas across the strand.',[
  ('Which correctly shows the flow of genetic information?',['Protein → RNA → DNA','RNA → DNA → Protein','DNA → RNA → Protein (transcription then translation)','Protein → DNA → RNA'],2),
  ('How does mitosis differ from meiosis?',['They are identical','Mitosis produces 4 cells; meiosis produces 2','Mitosis produces 2 identical daughter cells for growth/repair; meiosis produces 4 genetically unique gametes for reproduction','Meiosis produces identical cells'],2),
  ('Which body system most directly interacts with the immune system?',['Digestive','Muscular','Circulatory (blood carries immune cells throughout the body)','Skeletal'],2),
  ('The discovery of DNA\'s double helix structure by Watson and Crick (1953) was important because ___.',['it discovered cells','it proved evolution','it revealed how genetic information is encoded, copied, and passed on — enabling molecular biology and biotechnology','it had no practical impact'],2),
  ('Biotechnology raises ethical questions because ___.',['it has no practical applications','science should never be questioned','the power to modify genomes, clone organisms, and engineer life raises profound questions about safety, equity, identity, and the limits of human intervention in nature','ethics are irrelevant to science'],2)]),
H('Contemporary Canada: Issues and Identity','Students examine contemporary Canadian issues: Indigenous reconciliation, environmental policy, Quebec and Canadian identity, and Canada\'s role in global affairs.',[
  ('The Truth and Reconciliation Commission (TRC) of Canada ___.',['denied the residential school system occurred','was a trial of Indigenous leaders','documented the history and lasting harms of residential schools and issued 94 Calls to Action to begin reconciliation between Canada and Indigenous peoples','ended all Indigenous land claims'],2),
  ('The United Nations Declaration on the Rights of Indigenous Peoples (UNDRIP), adopted by Canada in 2016 and legislated in 2021, ___.',['has no legal significance','was rejected by Canada','affirms Indigenous peoples\' rights to self-determination, culture, and free, prior, and informed consent on decisions affecting their lands','only applies outside Canada'],2),
  ('Canada\'s multiculturalism policy (enshrined in the Multiculturalism Act, 1988) states ___.',['only two cultures are recognised','all cultures must assimilate','that cultural diversity is a fundamental Canadian value and the government will support the preservation and sharing of all cultural heritages','multicultural policies ended in 2000'],2),
  ('Quebec\'s distinct society debate concerns ___.',['only language policy','only economics','whether Quebec should be recognised constitutionally as a distinct society within Canada, given its unique French language, civil law, and culture','whether Quebec should join France'],2),
  ('Canada\'s reputation as a "middle power" in global affairs refers to ___.',['being a small, unimportant country','being a military superpower','being a country of significant but not dominant power that contributes to international stability through diplomacy, multilateralism, and peacekeeping','having the world\'s largest military'],2)])])
]

write_new(8, g8)
print('Grade 8 days 1-15 written.')
