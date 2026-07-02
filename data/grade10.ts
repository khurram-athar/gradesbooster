import type { DayContent } from '@/types';

const curriculum: DayContent[] = [
{day:1, label:"Day 1 — Mon", subjects:[
  {subject:"English", title:"Literary Analysis: Elements of Fiction", summary:"Students analyse the key elements of fiction — plot, character, setting, conflict, theme, point of view, and style — in preparation for novel and short story study.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Which element of fiction asks "how is the story told and in whose voice?"", options:["Plot","Setting","Theme","Point of view and narrative style"], answer:3},
     {q:"The climax of a narrative is ___.", options:["the opening situation","the falling action","the point of highest tension where the central conflict reaches its peak","the resolution where conflict is resolved"], answer:2},
     {q:"A flat character is ___.", options:["always the protagonist","a character who changes dramatically","a character with only one or two traits who does not develop over the course of the story","more realistic than a round character"], answer:2},
     {q:"Setting contributes to a story by ___.", options:["only providing physical location","being unimportant to theme","establishing mood, creating symbolic meaning, reflecting character psychology, and shaping the conflicts characters face","only indicating time period"], answer:2},
     {q:"Style in fiction refers to ___.", options:["only the plot structure","the author's characteristic way of using language — sentence structure, diction, imagery, rhythm, and tone","only genre","the length of the work"], answer:1}
   ]},
  {subject:"Math", title:"Linear Systems: Two Variables", summary:"Students review and extend solving systems of linear equations (two variables) graphically, by substitution, and by elimination. They interpret solutions in context.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A system of two linear equations with one unique solution means ___.", options:["the lines are parallel","the equations are identical","the lines intersect at exactly one point","there are infinite solutions"], answer:2},
     {q:"Solve by elimination: 3x + y = 11 and x − y = 1", options:["x = 3, y = 2","x = 2, y = 5","x = 4, y = −1","x = 3, y = −2"], answer:0},
     {q:"Solve by substitution: y = 2x − 3 and 4x − y = 9", options:["x = 3, y = 3","x = 2, y = 1","x = 4, y = 5","x = 3, y = 1"], answer:0},
     {q:"A system with no solution has lines that are ___.", options:["perpendicular","identical","intersecting","parallel — same slope, different y-intercepts"], answer:3},
     {q:"In context, the solution (3, 150) to a cost system where x = hours and y = dollars means ___.", options:["the minimum cost is 3","the maximum hours are 150","at 3 hours, the cost is $150 — the two pricing options cost the same","3 hours costs $0"], answer:2}
   ]},
  {subject:"Science", title:"Chemistry: Atomic Theory and the Periodic Table", summary:"Students examine the development of atomic theory (Dalton, Thomson, Rutherford, Bohr) and how the periodic table organises elements by atomic structure.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Rutherford's gold foil experiment showed ___.", options:["atoms are solid spheres","electrons orbit in shells","atoms have a small, dense, positively charged nucleus with mostly empty space around it","atoms contain no neutrons"], answer:2},
     {q:"The Bohr model of the atom shows electrons ___.", options:["randomly distributed throughout","in the nucleus","orbiting the nucleus in specific energy levels (shells)","only on one side of the nucleus"], answer:2},
     {q:"In the periodic table, elements in the same group (column) ___.", options:["have the same atomic mass","are in the same period","share similar chemical properties because they have the same number of valence electrons","have the same number of neutrons"], answer:2},
     {q:"Atomic number equals ___.", options:["the number of neutrons","the number of protons (which equals the number of electrons in a neutral atom)","the mass number","protons plus neutrons"], answer:1},
     {q:"Mass number equals ___.", options:["atomic number only","number of electrons","number of protons","protons + neutrons"], answer:3}
   ]},
  {subject:"History", title:"Canada and World War II: Causes and Outbreak", summary:"Students examine the causes of WWII — rise of fascism, appeasement, Nazi aggression — and Canada's declaration of war and early contributions.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The policy of appeasement pursued by Britain and France in the 1930s meant ___.", options:["confronting Hitler's aggression immediately","imposing economic sanctions only","making concessions to Hitler (notably at Munich, 1938) to avoid war — ultimately failing when Germany invaded Poland","supporting Germany's expansion"], answer:2},
     {q:"Canada declared war on Germany in September 1939 ___.", options:["the same day as Britain, demonstrating full dependence","before Britain, showing independence","a week after Britain, demonstrating growing autonomy as a sovereign nation","only after Japan attacked Pearl Harbor"], answer:2},
     {q:"The Holocaust refers to ___.", options:["a German military strategy","civilian war casualties in general","the systematic Nazi genocide of six million Jews and millions of others (Roma, LGBTQ+, disabled people, Soviet POWs)","the firebombing of German cities"], answer:2},
     {q:"The Battle of the Atlantic was crucial for Canada because ___.", options:["it was fought in the Pacific","it only involved the British Navy","the Royal Canadian Navy played a central role protecting supply convoys that kept Britain alive and enabled the Allied war effort","it ended the war quickly"], answer:2},
     {q:"Canada's decision to declare war separately from Britain in 1939 was significant because ___.", options:["it made no difference","Canada was forced to declare war","it was a major assertion of Canadian sovereignty — contrasting with WWI when Canada was automatically at war when Britain declared it","Canada opposed the war initially"], answer:2}
   ]},
]},
{day:2, label:"Day 2 — Tue", subjects:[
  {subject:"English", title:"Writing: The Literary Essay", summary:"Students write analytical literary essays with a clear thesis, developed body paragraphs using textual evidence, and effective conclusions. They apply the writing process.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A literary essay thesis should ___.", options:["summarise the plot","ask a question about the text","state an arguable, specific interpretation of the text that the essay will prove through close analysis","describe the author's biography"], answer:2},
     {q:"Body paragraphs in a literary essay should follow ___.", options:["no particular structure","the PEEL or similar structure: Point, Evidence (quotation), Explanation/Analysis, Link","only description of events","the plot chronologically"], answer:1},
     {q:"Embedding a quotation means ___.", options:["dropping in a quote with no context","using only long block quotations","integrating the quoted words smoothly into your own sentence so the result is grammatically coherent","avoiding quotations entirely"], answer:2},
     {q:"Literary present tense means ___.", options:["discussing the author's life in present tense","using future tense for predictions","writing about the events of a literary text in present tense (e.g., "Hamlet hesitates because...")","only for poetry"], answer:2},
     {q:"A counterargument paragraph in a literary essay ___.", options:["proves your thesis is wrong","is always required","acknowledges a competing interpretation and then refutes it, making your argument more sophisticated","only appears in persuasive essays"], answer:2}
   ]},
  {subject:"Math", title:"Quadratic Equations: Factoring and the Quadratic Formula", summary:"Students solve quadratic equations by factoring and applying the quadratic formula. They connect solutions to graphs of parabolas.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The quadratic formula is ___.", options:["x = −b/2a","x = (−b ± √(b²−4ac)) / 2a","x = b² − 4ac","x = a(x−h)² + k"], answer:1},
     {q:"The discriminant b² − 4ac tells you ___.", options:["the vertex of the parabola","the y-intercept","the nature of solutions: positive = 2 real roots, zero = 1 repeated root, negative = no real roots","the axis of symmetry"], answer:2},
     {q:"Factor and solve: x² − 7x + 12 = 0", options:["x = 3 and x = 4","x = −3 and x = −4","x = 3 and x = −4","x = −3 and x = 4"], answer:0},
     {q:"Solve using the quadratic formula: 2x² + 3x − 2 = 0", options:["x = 1/2 and x = −2","x = 2 and x = −1/2","x = 1 and x = −2","x = 1/2 and x = 2"], answer:0},
     {q:"The solutions of a quadratic equation correspond to ___.", options:["the y-intercepts of the parabola","the vertex of the parabola","the x-intercepts (zeros/roots) of the corresponding parabola","the axis of symmetry"], answer:2}
   ]},
  {subject:"Science", title:"Chemistry: Chemical Bonding", summary:"Students explore ionic bonding (transfer of electrons between metals and non-metals) and covalent bonding (sharing of electrons between non-metals).",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Ionic bonds form when ___.", options:["two non-metals share electrons","a metal transfers electrons to a non-metal, forming positive and negative ions that attract each other","two metals combine","atoms share electrons equally"], answer:1},
     {q:"Covalent bonds form when ___.", options:["metals and non-metals combine","two non-metals share one or more pairs of electrons to achieve stable electron configurations","electrons are transferred","ionic compounds dissolve"], answer:1},
     {q:"NaCl (table salt) is an example of ___.", options:["a covalent compound","a metallic bond","an ionic compound (Na⁺ and Cl⁻ attracted by electrostatic force)","a noble gas compound"], answer:2},
     {q:"H₂O is an example of ___.", options:["an ionic compound","a metallic compound","a covalent compound (oxygen and hydrogen share electrons)","a noble gas compound"], answer:2},
     {q:"Valence electrons are important in bonding because ___.", options:["they are in the nucleus","only metals have them","they are the outermost electrons that atoms share or transfer during chemical bonding","they are irrelevant to chemical reactions"], answer:2}
   ]},
  {subject:"History", title:"Canada's War Effort: Military Contributions", summary:"Students examine Canada's major military contributions in WWII — Battle of Britain, Dieppe, Sicily, Italy, and D-Day.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The British Commonwealth Air Training Plan (BCATP) located in Canada was significant because ___.", options:["it trained only British pilots","Canada refused to participate","it trained nearly 140,000 air crew from Allied nations in Canada, making Canada crucial to Allied air power","it was a failure"], answer:2},
     {q:"The Dieppe Raid (August 1942) was significant because ___.", options:["it was a major Allied victory","Canada was not involved","despite being a costly failure with enormous Canadian casualties, it provided crucial lessons that improved the planning of D-Day","it ended the war in Europe"], answer:2},
     {q:"Canadian forces participated in the Italian Campaign (1943-45), which was important because ___.", options:["it had no strategic value","the Pacific front was more important","liberating Italy helped weaken Axis power in southern Europe and tied up significant German forces, contributing to the overall Allied strategy","Canada was only involved in Northwest Europe"], answer:2},
     {q:"On D-Day (June 6, 1944), Canadians landed at ___.", options:["Omaha Beach","Utah Beach","Gold Beach","Juno Beach, one of five Allied landing zones, where they achieved the greatest advance of any Allied force on that day"], answer:3},
     {q:"The Liberation of the Netherlands (1944-45) is remembered because ___.", options:["it had little strategic importance","only British forces were involved","Canadian forces played the primary role, and the Dutch people have maintained a deep gratitude and friendship with Canada ever since","it was the last battle of WWI"], answer:2}
   ]},
]},
{day:3, label:"Day 3 — Wed", subjects:[
  {subject:"English", title:"Shakespeare: Studying a Play", summary:"Students read and analyse a Shakespearean play in depth, examining dramatic conventions, language, themes, and historical context. (e.g., Romeo and Juliet, Macbeth, A Midsummer Night's Dream)",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Tragic heroes in Shakespeare typically possess ___.", options:["no admirable qualities","only virtues with no flaws","a fundamental flaw (hamartia) that, combined with fate and circumstance, leads to their destruction despite their admirable qualities","complete knowledge of their fate"], answer:2},
     {q:"Shakespeare's language uses iambic pentameter, which ___.", options:["is a type of rhyme scheme","has 12 syllables per line","has 10 syllables per line alternating unstressed and stressed (da-DUM), creating a natural speech rhythm","is always rhymed"], answer:2},
     {q:"Dramatic irony in a Shakespeare play occurs when ___.", options:["two characters argue","the audience knows something a character does not, creating tension or dark humour (e.g., the audience knows Romeo and Juliet will die)","the plot has a twist ending","a character delivers a soliloquy"], answer:1},
     {q:"The theatrical conventions of the Globe Theatre included ___.", options:["women playing female roles","elaborate special effects","all male cast (boys playing women), minimal scenery, and audiences standing in the yard or seated in galleries — the language did the work of setting and atmosphere","private performances only for royalty"], answer:2},
     {q:"Analysing Shakespeare's language involves ___.", options:["only translating into modern English","ignoring the poetry","examining metaphor, imagery, verse vs. prose, wordplay, and how specific language choices reveal character and develop theme","memorising speeches"], answer:2}
   ]},
  {subject:"Math", title:"Quadratics: Graphing Parabolas", summary:"Students graph parabolas using vertex form y = a(x−h)² + k, identify key features (vertex, axis of symmetry, direction of opening, x- and y-intercepts), and use transformations.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"In y = a(x − h)² + k, the vertex is ___.", options:["(h, k)","(k, h)","(−h, k)","(a, k)"], answer:0},
     {q:"If a > 0, the parabola opens ___.", options:["downward","horizontally","upward","sideways"], answer:2},
     {q:"The axis of symmetry of a parabola in vertex form y = a(x − h)² + k is ___.", options:["y = k","x = 0","x = h","y = h"], answer:2},
     {q:"The graph of y = −2(x − 3)² + 5 has vertex ___ and opens ___.", options:["(3, 5) and upward","(−3, 5) and downward","(3, 5) and downward","(−3, −5) and upward"], answer:2},
     {q:"Converting from standard form (ax² + bx + c) to vertex form requires ___.", options:["factoring only","the quadratic formula","completing the square","graphing first"], answer:2}
   ]},
  {subject:"Science", title:"Chemistry: Chemical Reactions", summary:"Students classify chemical reactions (synthesis, decomposition, single displacement, double displacement, combustion) and balance equations.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A balanced chemical equation has ___.", options:["more products than reactants","the same number of atoms of each element on both sides of the equation","different total masses on each side","fewer products than reactants"], answer:1},
     {q:"In a synthesis reaction ___.", options:["one compound breaks into two products","two or more reactants combine to form one product","one element replaces another in a compound","two ionic compounds exchange ions"], answer:1},
     {q:"Combustion reactions always involve ___.", options:["water and carbon dioxide only","a compound decomposing","a substance reacting with oxygen to produce heat and light, usually producing CO₂ and H₂O","two ionic compounds reacting"], answer:2},
     {q:"The Law of Conservation of Mass states ___.", options:["mass is created in exothermic reactions","mass is lost in combustion","the total mass of reactants equals the total mass of products in a chemical reaction","only applies to physical changes"], answer:2},
     {q:"Balance: H₂ + O₂ → H₂O. The balanced equation is ___.", options:["H₂ + O₂ → H₂O","2H₂ + O₂ → 2H₂O","H₂ + 2O₂ → H₂O","H₂ + O₂ → 2H₂O"], answer:1}
   ]},
  {subject:"History", title:"Canada's Home Front in WWII", summary:"Students examine how WWII transformed Canadian society — women's roles, war economy, rationing, and injustices such as Japanese-Canadian internment.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The internment of Japanese Canadians during WWII involved ___.", options:["voluntary relocation for safety","about 100 people","the forced removal of approximately 22,000 Japanese Canadians from BC, confiscation of their property, and internment in camps — a serious violation of civil rights","immediate restoration of rights after the war"], answer:2},
     {q:"Women's roles changed during WWII because ___.", options:["women were prohibited from wartime work","nothing changed significantly","with men overseas, women entered the industrial workforce in large numbers, taking on roles previously closed to them","only nursing was available"], answer:2},
     {q:"War industries in Canada during WWII ___.", options:["had no impact on the economy","led to economic depression","transformed Canada's economy, producing ships, aircraft, and munitions that made Canada a significant industrial power","employed only men"], answer:2},
     {q:"Rationing during WWII in Canada ___.", options:["was not necessary in Canada","only applied to luxury goods","restricted civilian consumption of resources (food, fuel, rubber, metals) to ensure sufficient supplies for the military","was entirely voluntary"], answer:2},
     {q:"The Quebec government's resistance to conscription during WWII ___.", options:["showed Quebec supported full participation","had no significant effect","reflected deep French-Canadian opposition to fighting in what many Québécois saw as a British war, reviving the tensions of the 1917 conscription crisis","was supported by the federal Liberal government fully"], answer:2}
   ]},
]},
{day:4, label:"Day 4 — Thu", subjects:[
  {subject:"English", title:"Media Studies: Advertising and Persuasion", summary:"Students critically analyse advertising texts across media, examining techniques of persuasion, target audiences, construction of identity, and representation.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Semiotics in media analysis is the study of ___.", options:["statistics about media use","only visual art","signs and symbols and how they create meaning — how images, words, sounds, and colours communicate culturally specific messages","only written language"], answer:2},
     {q:"A target audience is ___.", options:["all people everywhere","only children","the specific group of people an advertiser intends to reach, defined by demographics, interests, and values","only people who buy the product"], answer:2},
     {q:"How advertising constructs identity means ___.", options:["advertising reflects only real identities","products have no connection to identity","advertisers create associations between products and desirable identities, lifestyles, or values — buying the product is implicitly coded as "becoming" that identity","only clothing ads do this"], answer:2},
     {q:"Representation in media refers to ___.", options:["technical production quality","only who is shown in ads","how media texts portray different groups of people — which groups are shown, how, in what roles, and which groups are absent or stereotyped","only gender representation"], answer:2},
     {q:"Decoding media means ___.", options:["fixing broken signals","only describing what you see","actively analysing the constructed meanings, assumptions, and ideological messages embedded in media texts — asking who made it, for what purpose, and whose interests it serves","only for professional critics"], answer:2}
   ]},
  {subject:"Math", title:"Quadratics: Standard Form and Applications", summary:"Students work with quadratic functions in standard form (y = ax² + bx + c), find the vertex using x = −b/2a, and model real-world situations.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"In the standard form y = ax² + bx + c, the axis of symmetry is ___.", options:["x = c","x = a/b","x = −b/2a","x = b/2a"], answer:2},
     {q:"A ball is thrown and its height (in metres) is h = −5t² + 20t + 2. The t-value at max height = ?", options:["2 s (from t = −20/(2×−5) = 2)","4 s","10 s","1 s"], answer:0},
     {q:"The y-intercept of y = 3x² − 5x + 7 is ___.", options:["3","−5","7","0"], answer:2},
     {q:"Revenue R = x(100 − 2x) where x = price increase. Maximum revenue is at x = ___.", options:["100","50","25","0"], answer:2},
     {q:"The parabola y = −x² + 4x − 3 opens ___ and its vertex is at ___.", options:["upward, (2, 1)","downward, (2, 1)","downward, (−2, 1)","upward, (−2, −1)"], answer:1}
   ]},
  {subject:"Science", title:"Biology: Cell Biology Review and DNA", summary:"Students review cell structure and extend understanding to DNA structure, the genetic code, and the processes of transcription and translation.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"DNA is a double helix composed of ___.", options:["amino acids and lipids","nucleotides — each with a sugar (deoxyribose), phosphate group, and one of four nitrogenous bases (A, T, G, C)","proteins only","lipids and carbohydrates"], answer:1},
     {q:"Complementary base pairing in DNA means ___.", options:["any base can pair with any other","Adenine pairs with Thymine (A-T) and Guanine pairs with Cytosine (G-C)","bases pair randomly","only A-T pairs exist"], answer:1},
     {q:"Transcription is the process of ___.", options:["copying DNA to make a DNA copy","using mRNA to make a protein","synthesising mRNA from a DNA template in the nucleus","cell division"], answer:2},
     {q:"Translation is the process of ___.", options:["copying DNA","making mRNA","synthesising a protein by reading the mRNA sequence using ribosomes and tRNA","DNA replication"], answer:2},
     {q:"A mutation is ___.", options:["always harmful","a change in the DNA sequence, which may be neutral, beneficial, or harmful, and can be caused by errors in replication or environmental factors (mutagens)","always beneficial","only in cancer cells"], answer:1}
   ]},
  {subject:"History", title:"The Cold War: Origins and Canada's Role", summary:"Students examine the ideological conflict between the USA and USSR, Canada's participation in NATO and NORAD, and the Korean War.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Cold War was primarily ___.", options:["a hot shooting war between the US and USSR","an economic partnership","a military conflict in Asia only","a political, economic, and ideological struggle between the capitalist West (led by the US) and the communist East (led by the USSR), 1945–1991"], answer:3},
     {q:"The NATO alliance, which Canada joined in 1949, committed members to ___.", options:["economic cooperation only","trade agreements","collective defence: an attack on one member is considered an attack on all","a shared currency"], answer:2},
     {q:"NORAD (1958) involved Canada and the United States in ___.", options:["joint economic management","a trade agreement","joint air defence of North America against the threat of Soviet nuclear bomber attack","a shared space program"], answer:2},
     {q:"Canada's participation in the Korean War (1950-53) saw ___.", options:["Canada officially neutral","no Canadian casualties","over 26,000 Canadians serving as part of the UN force, with Canada fulfilling its collective security commitments","Canada leading the UN forces"], answer:2},
     {q:"The Avro Arrow (CF-105) controversy in 1959 involved ___.", options:["Canada building nuclear weapons","a successful fighter jet program","the Canadian government cancelling what was arguably the world's most advanced jet interceptor, raising questions about Canadian industrial sovereignty and dependence on the US","a dispute with the Soviet Union"], answer:2}
   ]},
]},
{day:5, label:"Day 5 — Fri", subjects:[
  {subject:"English", title:"Independent Reading: Novel Selection and Response", summary:"Students select a Canadian novel or a world novel in English translation and write analytical reading journal entries tracking theme, character, and author's craft.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"When selecting a novel for independent study, you should consider ___.", options:["only page count","only genre","whether the novel offers complexity — rich characters, thematic depth, and stylistic choices worth analysing","only how popular it is"], answer:2},
     {q:"A reading response that analyses theme goes beyond plot by ___.", options:["listing chapter summaries","counting characters","examining how specific events, characters, and images work together to develop the author's central insight about human experience","only describing the ending"], answer:2},
     {q:"Tracking character arc means ___.", options:["listing every action a character takes","noting physical descriptions only","examining how a character's beliefs, values, and behaviour change in response to the conflicts and events of the narrative","only tracking the protagonist"], answer:2},
     {q:"Reading a Canadian novel specifically can develop ___.", options:["only grammar skills","awareness of Canadian geography","understanding of Canadian history, social issues, and diverse voices — including Indigenous, immigrant, and regional perspectives often absent from US and British canons","only French-language knowledge"], answer:2},
     {q:"An analytical journal entry differs from a summary by ___.", options:["being longer","having no plot references","asking "why" and "how" rather than only "what" — examining the author's choices and their effects rather than retelling events","using more quotations"], answer:2}
   ]},
  {subject:"Math", title:"Quadratics: Revenue, Profit, and Projectile Problems", summary:"Students apply quadratic models to real-world situations: projectile motion, revenue and profit maximisation, area optimisation.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A projectile is launched with height h = −4.9t² + 30t + 1.5. Maximum height occurs at t = ?", options:["approximately 3.06 s (using t = −b/2a = −30/(2×−4.9))","5 s","0 s","1.5 s"], answer:0},
     {q:"Revenue = price × quantity sold. If quantity decreases as price increases according to q = 200 − 2p, then Revenue = ?", options:["200p","p(200 − 2p) = 200p − 2p² — a downward parabola","2p − 200","200 − 2p"], answer:1},
     {q:"For R = −2p² + 200p, maximum revenue is at p = ___.", options:["200","100","50","25"], answer:2},
     {q:"A rectangular garden has perimeter 40 m. The area as a function of width w is ___.", options:["A = w²","A = w(40 − w)","A = w(20 − w)","A = 20w"], answer:2},
     {q:"The maximum area of the garden from the previous question is ___.", options:["400 m²","200 m²","100 m²","25 m²"], answer:2}
   ]},
  {subject:"Science", title:"Biology: Genetics and Heredity", summary:"Students apply Mendelian genetics — dominant/recessive, codominance, incomplete dominance, multiple alleles — to dihybrid crosses and inheritance patterns.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"In a dihybrid cross between two AaBb parents, the expected phenotype ratio of offspring is ___.", options:["1:2:1","1:1","3:1","9:3:3:1"], answer:3},
     {q:"Codominance means ___.", options:["one allele is dominant over another","the heterozygote shows a blend of both traits","both alleles are fully expressed simultaneously in the phenotype (e.g., AB blood type showing both A and B antigens)","one allele disappears"], answer:2},
     {q:"Incomplete dominance means ___.", options:["one allele masks the other","the heterozygote shows a phenotype intermediate between the two homozygous phenotypes (e.g., red + white = pink)","both alleles show separately","neither allele expresses"], answer:1},
     {q:"Sex-linked traits are carried on ___.", options:["autosomes only","both X and Y chromosomes equally","the sex chromosomes (usually X), making them more commonly expressed in males (XY) who have only one X","mitochondrial DNA only"], answer:2},
     {q:"Genetic disorders such as cystic fibrosis are ___.", options:["always dominant","caused by environmental factors only","autosomal recessive — two copies of the recessive allele are needed for the disorder to manifest","always sex-linked"], answer:2}
   ]},
  {subject:"History", title:"The Quiet Revolution and Canadian Identity", summary:"Students examine Quebec's Quiet Revolution, bilingualism, the October Crisis, and the evolution of Canadian identity in the 1960s-70s.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Quiet Revolution in Quebec (1960-66 and beyond) involved ___.", options:["a violent uprising","no significant change to Quebec society","rapid secularisation, nationalisation of industries, modernisation of education and social services, and a strong assertion of Québécois identity under Premier Jean Lesage","Quebec separating from Canada"], answer:2},
     {q:"The Official Languages Act (1969) ___.", options:["made only French official at the federal level","made only English official","declared English and French both official languages of Canada at the federal level, requiring government services in both languages","ended all language disputes"], answer:2},
     {q:"The October Crisis (1970) involved ___.", options:["an economic crisis","a Quebec election","FLQ (Front de libération du Québec) terrorists kidnapping British diplomat James Cross and Quebec Cabinet minister Pierre Laporte — Trudeau invoked the War Measures Act","a peaceful protest"], answer:2},
     {q:"Pierre Trudeau's vision of Canada emphasised ___.", options:["two nations (French and English) with equal power","Quebec as a special society","a bilingual, multicultural Canada where individual rights are paramount and Quebec does not have special status above other provinces","Canadian independence from all alliances"], answer:2},
     {q:"The repatriation of the Constitution in 1982 was controversial in Quebec because ___.", options:["Quebec wanted it repatriated","Quebec approved the final document","Quebec Premier Lévesque felt that Quebec was left out of the final negotiations and never signed the Constitution Act, creating an ongoing constitutional wound","it granted Quebec special status"], answer:2}
   ]},
]},
{day:6, label:"Day 6 — Mon", subjects:[
  {subject:"English", title:"Grammar and Style: Sophisticated Sentence Construction", summary:"Students apply advanced grammar — parallel structure, varied syntax, subordination and coordination, active vs. passive voice — to improve the quality of their analytical writing.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Active voice means ___.", options:["the verb is in present tense","the subject performs the action (e.g., "The author develops tension")","the subject receives the action","only simple sentences"], answer:1},
     {q:"Passive voice is appropriate when ___.", options:["always","never","the actor is unknown or less important than the action, or in formal scientific writing (e.g., "The sample was heated")","only in news writing"], answer:2},
     {q:"Subordination in sentences means ___.", options:["using only short sentences","making all clauses equal","connecting a less important idea (dependent clause) to a main clause using a subordinating conjunction, showing the logical relationship between ideas","avoiding all conjunctions"], answer:2},
     {q:"Varied sentence length in academic writing ___.", options:["is only for creative writing","is irrelevant to quality","creates rhythm, emphasises key points, and prevents monotony — a long analytical sentence followed by a short, punchy one can be highly effective","should be avoided in formal essays"], answer:2},
     {q:"Wordiness in academic writing should be ___.", options:["encouraged for formal tone","eliminated — each word should earn its place; unnecessary padding weakens analytical writing","only avoided in creative writing","only a concern in short essays"], answer:2}
   ]},
  {subject:"Math", title:"Analytic Geometry: Distance, Midpoint, and Slopes", summary:"Students apply the distance formula, midpoint formula, and slope relationships to classify and verify geometric shapes.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The midpoint formula for points (x₁,y₁) and (x₂,y₂) is ___.", options:["((x₁+x₂)/2, (y₁+y₂)/2)","(x₂−x₁, y₂−y₁)","((x₁×x₂)/2, (y₁×y₂)/2)","(x₁−x₂, y₁−y₂)"], answer:0},
     {q:"Two lines are perpendicular if their slopes satisfy ___.", options:["m₁ = m₂","m₁ + m₂ = 0","m₁ × m₂ = −1","m₁ − m₂ = 1"], answer:2},
     {q:"The distance between (1,2) and (4,6) is ___.", options:["5","7","3","4"], answer:0},
     {q:"To verify a quadrilateral is a parallelogram, you would show ___.", options:["all angles are 90°","all sides are equal","both pairs of opposite sides have equal lengths and equal slopes (i.e., are parallel)","the diagonals are equal in length"], answer:2},
     {q:"The median of a triangle from vertex A to the midpoint M of the opposite side is ___.", options:["the altitude from A","the line from A to M (midpoint of BC)","the perpendicular bisector","the angle bisector from A"], answer:1}
   ]},
  {subject:"Science", title:"Biology: Evolution and Natural Selection", summary:"Students examine Darwin's theory of evolution by natural selection, evidence for evolution, and mechanisms of evolutionary change.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Natural selection operates on ___.", options:["individual organisms's acquired traits","genetic mutations only","heritable variation — individuals with traits better suited to their environment survive and reproduce more, passing those traits to offspring","all members of a species equally"], answer:2},
     {q:"Evidence for evolution includes ___.", options:["only fossil records","only DNA comparisons","the fossil record, comparative anatomy (homologous structures), biogeography, comparative embryology, and DNA/protein similarities","only direct observation of new species forming"], answer:2},
     {q:"Homologous structures are ___.", options:["structures that look identical and have the same function","structures with no genetic relationship","structures in different species that are anatomically similar due to common ancestry, even if they now serve different functions (e.g., human arm and whale flipper)","only found in invertebrates"], answer:2},
     {q:"Genetic drift refers to ___.", options:["evolution driven by natural selection","gene flow between populations","random changes in allele frequencies in a population, especially significant in small populations where chance events can dramatically alter gene frequencies","directional selection"], answer:2},
     {q:"Speciation occurs when ___.", options:["two populations exchange genes freely","populations become more similar","a population splits, the two parts become reproductively isolated, and they diverge genetically until they can no longer interbreed — forming two distinct species","only in isolated island ecosystems"], answer:2}
   ]},
  {subject:"History", title:"Canada and the United States: A Complex Relationship", summary:"Students examine the economic, military, cultural, and political dimensions of the Canada-US relationship.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada and the US share the world's largest ___.", options:["economic agreement","military alliance","land border — approximately 8,891 km — and maintain one of the world's most integrated economic relationships","cultural exchange program"], answer:2},
     {q:"NAFTA (1994), replaced by CUSMA (2020), is significant because ___.", options:["it had no economic impact","it only affects agriculture","about 70-75% of Canadian exports go to the United States — free trade has deeply integrated the two economies","it was rejected by Canada initially"], answer:2},
     {q:"American cultural dominance concerns some Canadians because ___.", options:["American and Canadian culture are identical","Canadians prefer American culture","the overwhelming presence of American media, entertainment, and consumer products can crowd out Canadian voices, leading to policies like Canadian content (CanCon) requirements","American culture only affects youth"], answer:2},
     {q:"The National Policy (1879) and CanCon regulations (CRTC) are both examples of ___.", options:["Canadian indifference to American influence","Canada copying American policy","government measures to protect Canadian economic and cultural interests from American dominance","provincial policies only"], answer:2},
     {q:"Canada-US tensions have arisen over ___.", options:["no significant issues","only trade disputes","issues including acid rain (1980s), softwood lumber, border management, Arctic sovereignty, and policy differences on issues like gun control, health care, and multilateralism","only environmental issues"], answer:2}
   ]},
]},
{day:7, label:"Day 7 — Tue", subjects:[
  {subject:"English", title:"Oral Communication: Seminar and Discussion", summary:"Students participate in and lead Socratic seminars on literary and media texts. They apply skills in active listening, analytical speaking, text-based evidence, and respectful dialogue.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A Socratic seminar is ___.", options:["a teacher-led lecture","a competitive debate","a student-led discussion in which participants explore ideas from a shared text through open-ended questions, building on each other's interpretations","a formal presentation with slides"], answer:2},
     {q:"An open-ended question in a seminar ___.", options:["has one correct answer","can be answered yes or no","requires reading only one passage","opens rich discussion by asking "why," "how," or "what does this mean" — inviting multiple interpretations rather than a single correct answer"], answer:3},
     {q:"Effective seminar participation includes ___.", options:["speaking as often as possible","only agreeing with others","interrupting to correct errors","building on others' ideas, asking follow-up questions, referring to the text, and changing your view when presented with compelling evidence"], answer:3},
     {q:"Evaluating the quality of an argument in a seminar means ___.", options:["judging how confident the speaker sounds","only agreeing with friends","checking whether the claim is supported by specific, relevant textual evidence and whether the reasoning is logical","only evaluating grammar"], answer:2},
     {q:"The purpose of a Socratic seminar is ___.", options:["to determine who is right","to assign grades for speaking","to reach a single agreed conclusion","to deepen everyone's understanding through collaborative inquiry — the process of thinking together is the goal"], answer:3}
   ]},
  {subject:"Math", title:"Trigonometry: Primary Trig Ratios (SOH-CAH-TOA)", summary:"Students apply sine, cosine, and tangent ratios in right triangles to find unknown sides and angles. They solve problems in context.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"SOH-CAH-TOA means ___.", options:["a method for factoring quadratics","a type of geometric proof","the definitions of the three primary trig ratios: Sin = Opposite/Hypotenuse, Cos = Adjacent/Hypotenuse, Tan = Opposite/Adjacent","only used in advanced calculus"], answer:2},
     {q:"In a right triangle with angle θ, opposite side 5, and hypotenuse 13, sin θ = ___.", options:["13/5","5/13","12/13","5/12"], answer:1},
     {q:"To find an unknown angle using trig, you use ___.", options:["the Pythagorean theorem","a ratio and then the inverse trig function (sin⁻¹, cos⁻¹, or tan⁻¹)","only sin ratios","only the cosine rule"], answer:1},
     {q:"A ladder 8 m long leans against a wall at 60° to the ground. Height on wall = ?", options:["4 m","6.93 m (8 × sin 60°)","4.62 m","8 × tan 60°"], answer:1},
     {q:"The angle of elevation of the top of a building is 35° from 50 m away. Height = ?", options:["50 × tan 35° ≈ 35.0 m","50 × sin 35° ≈ 28.7 m","50 / tan 35°","50 × cos 35°"], answer:0}
   ]},
  {subject:"Science", title:"Physics: Kinematics — Motion in One Dimension", summary:"Students analyse motion using displacement, velocity, acceleration, and time. They apply kinematics equations and interpret distance-time and velocity-time graphs.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Displacement differs from distance because ___.", options:["they are identical","displacement is always larger","displacement is a vector quantity describing change in position (with direction), while distance is the total path length travelled (scalar)","distance is a vector quantity"], answer:2},
     {q:"Average velocity = ___.", options:["total distance / total time","displacement / time","speed only","final velocity only"], answer:1},
     {q:"On a velocity-time graph, acceleration is represented by ___.", options:["the area under the graph","the slope of the graph","the y-intercept","the x-intercept"], answer:1},
     {q:"On a distance-time graph, a horizontal line means ___.", options:["constant velocity","increasing speed","the object is stationary (no change in distance with time)","decreasing speed"], answer:2},
     {q:"A car accelerates from 0 to 30 m/s in 10 s. Acceleration = ?", options:["3 m/s²","30 m/s²","300 m/s²","0.3 m/s²"], answer:0}
   ]},
  {subject:"History", title:"The Charter of Rights and Freedoms", summary:"Students examine the Canadian Charter of Rights and Freedoms (1982), key rights it protects, important court cases, and its limitations.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Charter of Rights and Freedoms is part of ___.", options:["the Criminal Code","the Constitution Act, 1982 — making it the supreme law of Canada that overrides any inconsistent legislation","the Civil Code of Quebec only","the BNA Act of 1867"], answer:1},
     {q:"Section 33 of the Charter, the "notwithstanding clause," allows ___.", options:["courts to override government decisions","individuals to exempt themselves from laws","Parliament or a provincial legislature to pass laws that override certain Charter rights for up to five years","the courts to strike down the Constitution"], answer:2},
     {q:"Section 15 (Equality Rights) protects against discrimination based on ___.", options:["only race and gender","only citizenship","race, national or ethnic origin, colour, religion, sex, age, and mental or physical disability (and more as interpreted by courts)","only grounds explicitly listed, no more"], answer:2},
     {q:"The Supreme Court of Canada has the power to ___.", options:["only advise on laws","strike down laws that violate the Charter, forcing legislatures to amend or repeal them","only interpret laws literally","override the Constitution"], answer:1},
     {q:"A key limitation of Charter rights is ___.", options:["they apply only to federal government","they have no limitations","that Section 1 allows rights to be limited by law where the limit is reasonable and can be justified in a free and democratic society","they only protect citizens, not permanent residents"], answer:2}
   ]},
]},
{day:8, label:"Day 8 — Wed", subjects:[
  {subject:"English", title:"Writing: The Comparative Essay", summary:"Students write a comparative literary essay analysing similarities and differences between two texts (novels, plays, poems, films) in terms of theme, technique, or character.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A comparative essay thesis must ___.", options:["only list the texts being compared","only identify similarities","describe only differences","establish a meaningful analytical point about both texts — arguing what the comparison reveals about theme, technique, or human experience"], answer:3},
     {q:"Two common structures for comparative essays are ___.", options:["block only","point-by-point only","block (all of text A, then all of text B) and point-by-point (compare both texts on each criterion in sequence), each with advantages","random alternation"], answer:2},
     {q:"The "so what?" of a comparative essay means ___.", options:["explaining what the texts are about","listing plot differences","telling the reader why the comparison matters — what larger insight about literature, society, or human nature does comparing these two texts reveal","describing the authors"], answer:2},
     {q:"Effective transitions in a comparative essay include ___.", options:["only "also" and "and"","words like "however," "in contrast," "similarly," "while," and "both authors..." to signal whether you are comparing or contrasting","only "but" and "or"","no transitions needed"], answer:1},
     {q:"When writing a paragraph in a comparative essay, you should ___.", options:["write a full paragraph about text A, then a full paragraph about text B each time","only analyse one text thoroughly","avoid linking the two texts in the same paragraph","aim to discuss both texts within most analytical paragraphs, building a layered comparison"], answer:3}
   ]},
  {subject:"Math", title:"Trigonometry: Angles in Standard Position", summary:"Students extend trig to angles in standard position (0°–360°), the CAST rule, and the unit circle. They find exact trig values for special angles.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"An angle in standard position has its vertex at the origin and its initial arm ___.", options:["along the negative x-axis","along the positive y-axis","along the positive x-axis","along the negative y-axis"], answer:2},
     {q:"The CAST rule tells you which trig functions are positive in each quadrant: ___.", options:["All positive in Q1 only","Sin positive in Q1 and Q2; Cos positive in Q1 and Q4; Tan positive in Q1 and Q3","All functions negative in Q2","Only Cos is ever positive"], answer:1},
     {q:"The reference angle is ___.", options:["the angle in standard position","always 45°","the acute angle between the terminal arm and the nearest x-axis","the complement of the angle"], answer:2},
     {q:"sin 150° = ___.", options:["−1/2","√3/2","1/2","−√3/2"], answer:2},
     {q:"cos 270° = ___.", options:["0","1","−1","undefined"], answer:0}
   ]},
  {subject:"Science", title:"Physics: Forces and Newton's Laws", summary:"Students apply Newton's three laws of motion to analyse forces and predict the behaviour of objects. They work with free body diagrams.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Newton's First Law (Inertia) states ___.", options:["force equals mass times acceleration","for every action there is an equal and opposite reaction","an object at rest stays at rest and an object in motion stays in motion with constant velocity unless acted upon by a net external force","heavier objects fall faster"], answer:2},
     {q:"Newton's Second Law states ___.", options:["objects always move in circles","F = ma: net force equals mass times acceleration","for every action there is a reaction","inertia keeps objects at rest"], answer:1},
     {q:"Newton's Third Law states ___.", options:["only applies to collisions","objects slow down due to gravity","F = ma","for every force (action), there is an equal and opposite force (reaction) exerted on the first object by the second"], answer:3},
     {q:"A free body diagram shows ___.", options:["the path an object takes","the internal structure of an object","all external forces acting on an object as arrows, used to analyse net force","only gravitational force"], answer:2},
     {q:"If a 10 kg object experiences a net force of 30 N, its acceleration is ___.", options:["300 m/s²","0.33 m/s²","3 m/s²","30 m/s²"], answer:2}
   ]},
  {subject:"History", title:"Multiculturalism and Immigration in Canada", summary:"Students examine the evolution of Canadian immigration policy from exclusion to multiculturalism, and the ongoing debates about Canadian identity.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's pre-WWII immigration policy was ___.", options:["open and welcoming to all","consistently multicultural","explicitly racially discriminatory, favouring white British and Northern European immigrants and using mechanisms like the Chinese Head Tax, Continuous Journey Regulation, and order-in-council to exclude others","neutral and based only on economics"], answer:2},
     {q:"The Immigration Act of 1967 introduced a ___.", options:["racial preference system","points-based system that evaluated applicants on education, skills, and language ability, effectively removing explicit racial discrimination","quota system by country of origin","policy of accepting only refugees"], answer:1},
     {q:"The Canadian Multiculturalism Act (1988) ___.", options:["was only a symbolic gesture","declared Canada officially bilingual","enshrined multiculturalism in law, committing the government to preserve and enhance the multicultural heritage of Canadians while ensuring all Canadians enjoy equal opportunity","reversed immigration policy"], answer:2},
     {q:"Current debates about Canadian immigration include ___.", options:["no debates — it is completely settled","only economic concerns","questions about integration vs. cultural retention, housing pressures from population growth, refugee processing times, and recognition of foreign credentials","only refugee policy"], answer:2},
     {q:"Canada accepts immigrants through several streams including ___.", options:["only refugees","only economic immigrants","economic immigration (skilled workers, investors), family reunification, and humanitarian/refugee streams — each reflecting different priorities","only family reunification"], answer:2}
   ]},
]},
{day:9, label:"Day 9 — Thu", subjects:[
  {subject:"English", title:"Novel Study: Examining a Contemporary Canadian Novel", summary:"Students deeply read a contemporary Canadian novel, examining how the text engages with specifically Canadian themes — landscape, identity, colonial history, immigration, or social justice.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canadian literature often reflects ___.", options:["only rural themes","identical concerns to American and British literature","specifically Canadian preoccupations: the vastness of the landscape, settler-colonial history, multicultural identity, and the ongoing question of what it means to be Canadian","only Quebec themes"], answer:2},
     {q:"Postcolonial literary criticism examines ___.", options:["only novels set in the past","how literature reinforces colonial power","how literary texts engage with the history and legacy of colonialism — examining power dynamics, representation of Indigenous peoples, and resistance and reclamation","only British literature"], answer:1},
     {q:"Narrative voice in a novel set in Canada might use dialect, Indigenous languages, or multicultural expressions to ___.", options:["alienate readers","make the novel less marketable","confuse the language","authentically represent Canadian voices and resist the dominance of standard white, anglophone literary conventions"], answer:3},
     {q:"Setting in a Canadian novel often functions as more than location — it can ___.", options:["always be ignored","only indicate time period","represent the social and political tensions of Canada itself — from frozen tundra representing isolation to urban diversity representing the complexity of modern Canadian identity","only establish mood"], answer:2},
     {q:"Reading a Canadian novel critically includes asking ___.", options:["only what happens","only who the main character is","whose perspective dominates, whose voices are absent, what assumptions about Canada are embedded in the narrative, and how the text challenges or reinforces those assumptions","only what the theme is"], answer:2}
   ]},
  {subject:"Math", title:"Trigonometry: The Sine Law", summary:"Students apply the Sine Law (a/sinA = b/sinB = c/sinC) to find unknown sides and angles in non-right triangles.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Sine Law applies to ___.", options:["only right triangles","only equilateral triangles","any triangle where you know two angles and a side (AAS or ASA) or two sides and an angle opposite one of them (SSA)","only when all three sides are known"], answer:2},
     {q:"The Sine Law states ___.", options:["a² = b² + c² − 2bc cosA","a/sinA = b/sinB = c/sinC","sinA + sinB + sinC = 1","a × sinA = b × sinB"], answer:1},
     {q:"In a triangle, angle A = 35°, angle B = 80°, a = 10 cm. Find b.", options:["b = 10 × sin80° / sin35° ≈ 17.2 cm","b = 10 × sin35° / sin80°","b = sin80° / sin35°","b = 10 / sin80°"], answer:0},
     {q:"The ambiguous case (SSA) in the Sine Law can result in ___.", options:["always one triangle","always no triangle","zero, one, or two possible triangles depending on the relative lengths of the given sides","always two triangles"], answer:2},
     {q:"To use the Sine Law, the angle must be ___.", options:["90° always","opposite to a known side (so that angle-side pair appears in the same ratio)","adjacent to both known sides","the largest angle"], answer:1}
   ]},
  {subject:"Science", title:"Physics: Work, Energy, and Power", summary:"Students apply the concepts of work (W = Fd cosθ), kinetic and potential energy, conservation of energy, and power (P = W/t).",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Work is done on an object when ___.", options:["a force is applied","an object is at rest but a force is applied","a force causes displacement in the direction of the force (W = Fd cosθ)","any force is present"], answer:2},
     {q:"Kinetic energy is ___.", options:["energy stored in position","energy due to motion: KE = ½mv²","energy from chemical bonds","energy from heat"], answer:1},
     {q:"Gravitational potential energy is ___.", options:["energy due to motion","energy from temperature","energy from chemical bonds","energy stored in an object due to its height: PE = mgh"], answer:3},
     {q:"The Law of Conservation of Energy states ___.", options:["energy is created in nuclear reactions","energy is destroyed in friction","energy can be created from nothing","energy cannot be created or destroyed — only transformed from one form to another"], answer:3},
     {q:"Power is ___.", options:["force times distance","the total energy used","the rate at which work is done: P = W/t (measured in watts, W)","energy per unit mass"], answer:2}
   ]},
  {subject:"History", title:"Indigenous Rights and Land Claims in Canada", summary:"Students examine the historical and legal context of Indigenous land claims, treaty rights, and the Supreme Court's evolving jurisprudence.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Royal Proclamation of 1763 is significant to Indigenous rights because ___.", options:["it removed all Indigenous land rights","it had no lasting legal significance","it explicitly recognised Indigenous peoples' right to their lands and required the Crown to negotiate treaties before settlement — its principles remain relevant in Canadian law","it only applied to Quebec"], answer:2},
     {q:"Section 35 of the Constitution Act (1982) ___.", options:["removed treaty rights","was a minor symbolic clause","recognises and affirms existing Aboriginal and treaty rights, providing constitutional protection that has enabled significant court victories for First Nations","only protects Métis rights"], answer:2},
     {q:"The Calder case (1973) was significant because ___.", options:["Canada won completely","no court considered Indigenous land rights","the Supreme Court of Canada was split but acknowledged for the first time that Aboriginal title may exist in Canadian law — a turning point in legal recognition","only BC was affected"], answer:2},
     {q:"Comprehensive land claims are ___.", options:["already fully settled","criminal cases","claims by First Nations that were never covered by treaties, seeking negotiated agreements on land ownership, resource rights, and governance","minor boundary disputes"], answer:2},
     {q:"Free, prior, and informed consent (FPIC), enshrined in UNDRIP, means ___.", options:["governments can consult without obtaining agreement","companies do not need to consult Indigenous peoples","only applies outside Canada","Indigenous peoples must be consulted and must give meaningful consent — not just be notified — before projects affecting their lands and rights proceed"], answer:3}
   ]},
]},
{day:10, label:"Day 10 — Fri", subjects:[
  {subject:"English", title:"Film Study: Cinematic Techniques", summary:"Students study film as a literary medium. They analyse how directors use camera work, editing, sound, mise-en-scène, and narrative structure to create meaning.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Mise-en-scène refers to ___.", options:["only camera movement","only dialogue","the editing choices in a film","everything visible in the frame: set design, lighting, costumes, actor placement and movement — the visual environment of a scene"], answer:3},
     {q:"A close-up shot in film is used to ___.", options:["show the entire scene","establish location","emphasise a character's facial expression, revealing emotion or psychological state","only show objects"], answer:2},
     {q:"Non-diegetic sound in film is ___.", options:["sound that characters in the film can hear","only dialogue","background noise from the setting","sound outside the film's world that only the audience hears — such as a musical score"], answer:3},
     {q:"Parallel editing (cross-cutting) is a film technique that ___.", options:["slows narrative pace","only shows one storyline","cuts between two or more scenes happening simultaneously, building tension and showing thematic connections between actions","removes sound from scenes"], answer:2},
     {q:"Analysing film as a text means ___.", options:["only describing the plot","listing all the actors","watching it for entertainment only","examining the choices the director makes and the effects they create — film is a constructed text like a novel, with meaning made through deliberate artistic decisions"], answer:3}
   ]},
  {subject:"Math", title:"Trigonometry: The Cosine Law", summary:"Students apply the Cosine Law (a² = b² + c² − 2bc cosA) to find unknown sides and angles in triangles where the Sine Law cannot be applied directly.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Cosine Law is used when ___.", options:["two angles and a side are known","only right triangles","you have two sides and the included angle (SAS) or all three sides and need an angle (SSS)","any triangle problem"], answer:2},
     {q:"The Cosine Law states: a² = ___.", options:["b × c × cosA","b² + c² − 2bc cosA","b + c − 2bc cosA","sinA × sinB × sinC"], answer:1},
     {q:"In a triangle with b = 7, c = 9, and A = 50°, find a.", options:["a² = 49 + 81 − 2(7)(9)cos50° ≈ a ≈ 7.0","a = 7 + 9 = 16","a = 50","a = sin50°"], answer:0},
     {q:"The Cosine Law rearranged to find angle A gives ___.", options:["cosA = (b² + c² + a²) / 2bc","cosA = (b² + c² − a²) / 2bc","cosA = a/sinA","cosA = 2bc − b² − c²"], answer:1},
     {q:"When would you choose the Cosine Law over the Sine Law?", options:["Always","When you have AAS or ASA","When you know SAS or SSS — cases where the Sine Law cannot be applied directly","Never"], answer:2}
   ]},
  {subject:"Science", title:"Physics: Waves and Sound", summary:"Students examine the properties of waves (transverse, longitudinal, amplitude, wavelength, frequency, speed) and sound as a longitudinal wave.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A transverse wave has ___.", options:["particles moving parallel to wave direction","no amplitude","no frequency","particles oscillating perpendicular to the direction of wave travel (e.g., water waves, light)"], answer:3},
     {q:"A longitudinal wave has particles moving ___.", options:["perpendicular to wave direction","in circles","parallel to the direction of wave travel (e.g., sound waves)","only vertically"], answer:2},
     {q:"The speed of a wave equals ___.", options:["amplitude × frequency","wavelength / frequency","wavelength × frequency (v = fλ)","frequency only"], answer:2},
     {q:"Sound travels fastest in ___.", options:["a vacuum","air","water","solids, where particles are closely packed and can transmit vibrations rapidly"], answer:3},
     {q:"The Doppler effect is ___.", options:["a change in wave amplitude","a standing wave pattern","the apparent change in frequency of a wave due to relative motion between the source and observer — sound from an approaching ambulance has higher pitch than one moving away","only applies to light"], answer:2}
   ]},
  {subject:"History", title:"Canada's Environmental History", summary:"Students examine key moments in Canadian environmental history, from the creation of national parks to current climate policy debates.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Banff National Park (established 1885) and subsequent parks were initially created primarily to ___.", options:["protect Indigenous territory","serve purely ecological goals","attract tourists and protect scenic landscapes, though the conservation mission grew over time — a complex history that included displacing Indigenous peoples from park lands","protect endangered species"], answer:2},
     {q:"The Kyoto Protocol (1997) committed Canada to ___.", options:["no specific emissions targets","only monitoring emissions","reducing greenhouse gas emissions below 1990 levels — though Canada later withdrew in 2011 without meeting its targets","only renewable energy"], answer:2},
     {q:"The "social licence to operate" concept in resource development means ___.", options:["government approval is sufficient","legal permits override all concerns","companies need more than legal permits — they need the genuine acceptance of communities (including Indigenous communities) affected by their projects","only applies in BC"], answer:2},
     {q:"The debate over the Trans Mountain Pipeline expansion reflects tensions between ___.", options:["only economic concerns","only environmental concerns","only Indigenous rights","multiple competing interests: Indigenous rights and title, environmental protection, economic development, and national energy strategy"], answer:3},
     {q:"Canada's Net Zero by 2050 target means ___.", options:["Canada will stop all industrial activity","zero emissions from all sources by 2050","reducing emissions to zero immediately","achieving a balance between greenhouse gas emissions produced and removed, through a combination of emission reductions and carbon sequestration"], answer:3}
   ]},
]},
{day:11, label:"Day 11 — Mon", subjects:[
  {subject:"English", title:"Writing: The Reflective Essay", summary:"Students write a personal reflective essay on a significant literary or cultural experience. They combine analytical rigour with genuine personal voice and insight.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A reflective essay differs from a personal narrative because ___.", options:["reflective essays are shorter","narratives are more accurate","a reflective essay doesn't just describe an experience but critically examines what it meant and what the writer learned from it — the reflection is the point","only narratives use personal voice"], answer:2},
     {q:"Effective reflective writing moves between ___.", options:["only description","only analysis","only emotion","the specific (concrete events, quotations, images) and the general (broader insights, connections to larger ideas or universal experiences)"], answer:3},
     {q:"Voice in reflective writing ___.", options:["should be completely impersonal","is unimportant","should sound like an academic essay only","is central — the essay should sound like a thinking, feeling human being, not a generic template"], answer:3},
     {q:"A strong reflective essay ending ___.", options:["simply stops describing","restates the opening paragraph","summarises only what happened","leaves the reader with a new understanding that emerged from the reflection — a genuine insight, not just a summary"], answer:3},
     {q:"The best reflective essays are ___.", options:["always positive","free of any analysis","written about trivial events only","honest, specific, and intellectually curious — they take a risk by exploring genuine complexity rather than offering safe, expected conclusions"], answer:3}
   ]},
  {subject:"Math", title:"Financial Literacy: Earning, Saving, and Investing", summary:"Students examine income types, taxes, budgeting, compound interest, and basic investing principles relevant to their near future.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's progressive income tax system means ___.", options:["everyone pays the same rate","lower incomes pay more","higher income earners pay a higher marginal tax rate on income above each bracket threshold","taxes are optional"], answer:2},
     {q:"A TFSA (Tax-Free Savings Account) ___.", options:["has no contribution limit","removes all income tax on your salary","allows Canadians to contribute up to an annual limit and earn investment income tax-free inside the account","is only for retirement"], answer:2},
     {q:"An RRSP (Registered Retirement Savings Plan) ___.", options:["is taxed on contribution","earns no interest","allows contributions to be deducted from taxable income now, with growth tax-sheltered until withdrawal in retirement when you may be in a lower tax bracket","is only for people over 65"], answer:2},
     {q:"Diversification in investing means ___.", options:["only investing in one stock","always investing in gold","putting all money in savings accounts","spreading investments across different asset types and sectors to reduce risk — losses in one area are offset by gains in another"], answer:3},
     {q:"The Rule of 72 estimates ___.", options:["how long to pay off debt at any rate","how many years to accumulate $1000","your retirement age","how many years it takes to double an investment: 72 ÷ annual interest rate ≈ years to double"], answer:3}
   ]},
  {subject:"Science", title:"Physics: Light — Reflection, Refraction, Optics", summary:"Students study the behaviour of light: law of reflection, refraction (Snell's Law), total internal reflection, and optical instruments.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Snell's Law (n₁sinθ₁ = n₂sinθ₂) describes ___.", options:["the reflection of light","the absorption of light","how light bends when passing from one medium to another — the angle of refraction depends on the ratio of the refractive indices","only applies to lenses"], answer:2},
     {q:"Total internal reflection occurs when ___.", options:["light enters a denser medium","light hits a mirror","light travels from a denser to a less dense medium at an angle greater than the critical angle — it reflects completely rather than refracting","light hits a coloured surface"], answer:2},
     {q:"Fibre optic cables transmit data using ___.", options:["electrical signals","radio waves","magnetic pulses","total internal reflection — light pulses bounce along the glass fibre without escaping, enabling high-speed data transmission"], answer:3},
     {q:"A converging (convex) lens ___.", options:["diverges all light","has no focal point","only works in telescopes","bends parallel rays of light toward a focal point, forming real images of distant objects"], answer:3},
     {q:"The index of refraction (n) of a medium is ___.", options:["the speed of light in that medium","the wavelength of light in that medium","c/v — the ratio of the speed of light in a vacuum to the speed of light in the medium (always ≥ 1)","the colour of light in that medium"], answer:2}
   ]},
  {subject:"History", title:"Charter Rights: Case Studies", summary:"Students examine landmark Supreme Court of Canada cases under the Charter, analysing the legal reasoning and social implications.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"R v Oakes (1986) established ___.", options:["that the Charter has no limits","the Oakes Test — a two-part framework for determining whether a law that limits a Charter right can be justified under Section 1","that all laws are constitutional","that Section 33 is never valid"], answer:1},
     {q:"Singh v Minister of Employment and Immigration (1985) established ___.", options:["only citizens have Charter rights","refugee claimants have no rights in Canada","that Convention refugees have Charter rights, including the right to an oral hearing before being denied protection — a landmark case for refugee rights in Canada","only landed immigrants have Charter rights"], answer:2},
     {q:"M v H (1999) was significant for ___.", options:["corporate rights","freedom of speech","extending spousal support rights to same-sex partners, a major step toward equal rights for LGBTQ+ Canadians","religious rights"], answer:2},
     {q:"Eldridge v British Columbia (1997) established ___.", options:["corporations have equality rights","that language rights only apply to official languages","that the government must provide sign language interpreters to Deaf patients in hospitals, as failing to do so violates Section 15 equality rights","that only federal laws must respect the Charter"], answer:2},
     {q:"A common pattern in Charter litigation is ___.", options:["Charter cases always go against the government","the government always wins","courts balance individual rights against collective interests, with Section 1 allowing rights to be limited when demonstrably justified — no right is absolute in a constitutional democracy","only wealthy individuals use the Charter"], answer:2}
   ]},
]},
{day:12, label:"Day 12 — Tue", subjects:[
  {subject:"English", title:"Literature: Poetry — Voice, Identity, and Social Justice", summary:"Students read and analyse contemporary poetry by Canadian poets, particularly from Indigenous, Black Canadian, and immigrant voices, examining how poetry enacts identity and challenges injustice.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Contemporary Canadian poetry by marginalised voices ___.", options:["is identical to traditional British poetry","has no political dimension","often challenges dominant narratives, reclaims cultural identity, uses code-switching between languages, and speaks truth about lived experiences of colonialism, racism, and displacement","is only about nature"], answer:2},
     {q:"Code-switching in poetry refers to ___.", options:["only a technical error","a poetic device unrelated to identity","switching between computer codes in a poem","alternating between two or more languages or registers within a single poem, often reflecting the speaker's multiple cultural identities"], answer:3},
     {q:"Slam poetry and spoken word ___.", options:["are not literary forms","are only for entertainment","have no connection to written poetry","are forms of oral poetry that emphasise performance, rhythm, voice, and political engagement — often more accessible and diverse in voices than published print poetry"], answer:3},
     {q:"When reading poetry by marginalised poets, it is important to ___.", options:["apply only standard literary analysis tools","ignore context","assume all such poetry is political","bring understanding of the historical and social context of the poet's experience, recognising that form, language, and voice are often themselves acts of resistance"], answer:3},
     {q:"The intersection of identity and poetry means ___.", options:["poets should not write about their identity","only confessional poetry has value","all poetry is political","a poet's race, gender, sexuality, class, and cultural background shape what they write about, how they write, and what literary conventions they accept, reject, or subvert"], answer:3}
   ]},
  {subject:"Math", title:"Review: Quadratics, Trigonometry, and Analytic Geometry", summary:"Students consolidate Grade 10 math topics.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Solve by the quadratic formula: x² − 4x − 5 = 0", options:["x = 5 and x = −1","x = −5 and x = 1","x = 4 and x = −5","x = 4 and x = 1"], answer:0},
     {q:"In a triangle with A = 40°, B = 75°, a = 12, find b using the Sine Law.", options:["b = 12 sin75° / sin40° ≈ 18.0","b = 12 sin40° / sin75°","b = sin75° / sin40°","b = 12 / sin75°"], answer:0},
     {q:"Two lines are perpendicular. One has slope 2/3. The other's slope is ___.", options:["2/3","−3/2","3/2","−2/3"], answer:1},
     {q:"A parabola y = a(x − 3)² − 4 opens upward. Which value of a is correct?", options:["a = −1","a = −0.5","a = 2","a = 0"], answer:2},
     {q:"The distance between (−1, 2) and (3, −1) is ___.", options:["5","7","√7","3"], answer:0}
   ]},
  {subject:"Science", title:"Physics: Electromagnetism Basics", summary:"Students explore electric fields, electric potential, magnetic fields, and how they interact — culminating in understanding electromagnetic induction.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Electric field lines show ___.", options:["the path a positive test charge would take if released in the field","the direction of electron flow only","the location of neutral particles","magnetic force only"], answer:0},
     {q:"A magnetic field is created by ___.", options:["stationary electric charges","temperature differences","light waves","moving electric charges (current-carrying conductors) and permanent magnets"], answer:3},
     {q:"Electromagnetic induction (Faraday's law) means ___.", options:["magnetic fields attract iron","magnets produce light","a changing magnetic field through a conductor induces an electric current — the principle behind generators and transformers","current only flows in one direction"], answer:2},
     {q:"An electric motor converts ___.", options:["mechanical energy to electrical energy","chemical energy to heat","electrical energy to mechanical energy, using the force on a current-carrying conductor in a magnetic field","light to electrical energy"], answer:2},
     {q:"An electric generator converts ___.", options:["electrical energy to heat","electrical energy to mechanical energy","light to electricity","mechanical energy (e.g., from a turbine) to electrical energy through electromagnetic induction"], answer:3}
   ]},
  {subject:"History", title:"Contemporary Canadian Issues: Technology and Society", summary:"Students examine how digital technology and social media have transformed Canadian society, politics, and economy.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The digital economy has changed Canadian employment by ___.", options:["having no significant effect","only reducing jobs","creating entirely new sectors (tech companies, the gig economy, platform work) while automating or displacing some traditional jobs — raising questions about the future of work and worker protections","only benefiting urban workers"], answer:2},
     {q:"Social media platforms in Canada raise concerns about ___.", options:["only privacy issues","only political advertising","no significant concerns","privacy, disinformation, mental health impacts (especially on youth), algorithmic content curation, and foreign interference in democratic processes"], answer:3},
     {q:"Canada's Bill C-18 (Online News Act, 2023) was an attempt to ___.", options:["censor online news","ban social media","require digital platforms (Google, Meta) to pay Canadian news publishers for using their content — a major policy attempt to support journalism in the digital age","regulate only CBC content"], answer:2},
     {q:"Artificial intelligence is affecting Canadian society by ___.", options:["having no economic effect","only helping in medicine","eliminating all creative jobs","transforming healthcare (diagnosis), financial services (fraud detection), transportation (autonomous vehicles), and raising fundamental questions about labour, privacy, and democratic oversight"], answer:3},
     {q:"A key Canadian concern about digital technology is ___.", options:["Canada is a world leader with no concerns","only copyright issues","technological dependence — Canada consumes vast amounts of US-developed technology and platforms, raising questions about sovereignty, data privacy, and the economic costs of foreign tech dominance","only gaming addiction"], answer:2}
   ]},
]},
{day:13, label:"Day 13 — Wed", subjects:[
  {subject:"English", title:"Writing: The Research Essay — Advanced Skills", summary:"Students research and write a multi-source academic essay on a literary, historical, or social topic, applying MLA or APA citation, synthesis, and academic argument.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"An annotated bibliography includes ___.", options:["only titles and authors","only the URL","a full citation plus a brief critical summary of each source — evaluating its relevance, credibility, and contribution to your research","only books, not websites"], answer:2},
     {q:"Synthesising multiple sources means ___.", options:["only summarising each source separately","summarising sources in alphabetical order","weaving ideas from multiple sources together to build a complex argument — connecting, comparing, and contrasting perspectives rather than simply reporting them one by one","only using the most recent sources"], answer:2},
     {q:"In MLA format, in-text citations for a quotation include ___.", options:["only the author's first name","the full title of the source","the author's last name and page number in parentheses: (Smith 42)","a footnote number only"], answer:2},
     {q:"A research essay conclusion at the senior level should ___.", options:["only repeat the introduction","introduce entirely new evidence","show the significance of your findings, acknowledge complexity or limitations, and suggest questions for further inquiry","just restate your thesis"], answer:2},
     {q:"Academic writing avoids ___.", options:["first-person entirely always","logical argument","evidence","vague generalisations, unsupported claims, colloquialisms, and hedging that avoids taking a clear position"], answer:3}
   ]},
  {subject:"Math", title:"Geometry: Circle and Line Relationships", summary:"Students explore the geometry of circles — tangent lines, chords, secants — and prove circle theorems using congruence and angle relationships.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A tangent to a circle ___.", options:["passes through the centre","intersects the circle at two points","is perpendicular to the radius at the point of tangency","is parallel to any chord"], answer:2},
     {q:"An inscribed angle in a circle is ___.", options:["a central angle","an angle between two tangents","an angle formed by two chords that meet at a point on the circle, and equals half the central angle that subtends the same arc","an angle outside the circle"], answer:2},
     {q:"A central angle ___.", options:["is less than its inscribed angle","is half the inscribed angle subtending the same arc","is unrelated to the arc","equals the inscribed angle subtending the same arc"], answer:1},
     {q:"Two tangents drawn from an external point to a circle ___.", options:["have different lengths","may or may not be equal","are equal in length","are perpendicular to each other"], answer:2},
     {q:"The angle in a semicircle (inscribed angle subtending a diameter) is always ___.", options:["45°","60°","180°","90°"], answer:3}
   ]},
  {subject:"Science", title:"Physics and Chemistry: Nuclear Science", summary:"Students explore nuclear structure, radioactive decay (alpha, beta, gamma), half-life, nuclear fission and fusion, and their applications and risks.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Radioactive decay occurs when ___.", options:["any atom is heated","only man-made isotopes break down","an unstable nucleus releases energy/particles to reach a more stable configuration, changing its atomic number or mass number","electrons are removed from atoms"], answer:2},
     {q:"Alpha radiation is ___.", options:["a high-energy photon","a fast electron","a helium nucleus (2 protons + 2 neutrons) — most massive and least penetrating (stopped by paper or skin)","a neutron"], answer:2},
     {q:"Beta radiation is ___.", options:["a helium nucleus","a high-energy photon","a fast-moving electron emitted from the nucleus when a neutron converts to a proton — more penetrating than alpha, stopped by thin metal","a cluster of protons"], answer:2},
     {q:"Half-life is ___.", options:["the time for a radioactive sample to decay to 50% of its initial amount of radioactive material","the time for complete decay","the lifespan of a nuclear reactor","the time for gamma radiation to stop"], answer:0},
     {q:"Nuclear fission differs from fusion in that ___.", options:["fission joins nuclei; fusion splits them","only fusion produces energy","fission splits heavy nuclei (releasing energy), while fusion joins light nuclei (also releasing energy but requiring enormous temperatures and pressure — the process powering the sun)","both are identical processes"], answer:2}
   ]},
  {subject:"History", title:"Global Citizenship and Human Rights", summary:"Students examine international human rights frameworks (UDHR, ICC), Canada's role, and the responsibilities of individuals and states in a globalised world.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Universal Declaration of Human Rights (1948) ___.", options:["only applies to UN member states","was drafted without Canadian involvement","is legally binding on all nations","was proclaimed by the UN General Assembly as a foundational statement of universal human rights — though it is not legally binding on its own, it has inspired binding human rights treaties"], answer:2},
     {q:"The International Criminal Court (ICC) ___.", options:["is the same as the International Court of Justice","has no jurisdiction over heads of state","was established in 2002 to try individuals for genocide, war crimes, and crimes against humanity where national courts are unable or unwilling to do so","only tries non-state actors"], answer:2},
     {q:"Canada's commitment to international human rights has been complicated by ___.", options:["Canada having a perfect human rights record","no domestic rights violations","the gap between Canada's stated commitments internationally and the ongoing human rights issues at home — particularly the rights of Indigenous peoples, systemic racism, and poverty","only foreign policy issues"], answer:2},
     {q:"R2P (Responsibility to Protect) is a principle that ___.", options:["gives any country the right to invade another","has no support from Canada","denies sovereignty in all cases","states that when a government fails to protect its people from atrocities or commits atrocities itself, the international community has a responsibility to intervene — Canada was a key architect of this doctrine"], answer:3},
     {q:"Being a global citizen means ___.", options:["ignoring local issues","only caring about problems in other countries","taking no responsibility for global issues","recognising that you are connected to and affected by what happens elsewhere in the world, and that you have responsibilities to promote justice, equality, and sustainability globally"], answer:3}
   ]},
]},
{day:14, label:"Day 14 — Thu", subjects:[
  {subject:"English", title:"Oral and Media: Podcasting and Digital Storytelling", summary:"Students plan and create a short digital story or podcast episode, applying media production principles, research, and narrative skills.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A podcast script differs from a written essay because ___.", options:["it requires no research","it uses casual language only","it never uses evidence","it is designed to be heard — it uses conversational language, shorter sentences, audio cues, and engaging pacing, while still requiring solid research and clear structure"], answer:3},
     {q:"Digital storytelling combines ___.", options:["only text","only images","only audio","narrative, images, video, music, and/or sound effects to tell a story or explain a topic in a multi-modal format accessible to modern audiences"], answer:3},
     {q:"Copyright considerations in podcasting and digital media mean ___.", options:["all music and images are freely usable","only images need attribution","copyright doesn't apply to educational projects","you must use licensed or original music and images, give proper attribution, and understand Creative Commons licensing"], answer:3},
     {q:"The most important quality in a podcast is ___.", options:["the most expensive microphone","the longest run time","the most sound effects","clear, well-organised content delivered with an engaging voice that creates a genuine connection with the listener"], answer:3},
     {q:"Audience awareness in digital storytelling means ___.", options:["ignoring who will see your work","only making content for your teacher","making content as long as possible","constantly making decisions about content, tone, language, and format based on who you are trying to reach and what you want them to take away"], answer:3}
   ]},
  {subject:"Math", title:"Linear and Quadratic Systems", summary:"Students find the intersection of a linear equation and a quadratic (parabola), solving graphically and algebraically.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"To find where y = x + 3 meets y = x², you set them equal and solve ___.", options:["y = y","x + 3 = x², then x² − x − 3 = 0","x = x²","y = 0"], answer:1},
     {q:"The number of intersections of a line and a parabola can be ___.", options:["only 1","only 2","always 0","0, 1, or 2, depending on the discriminant of the resulting quadratic equation"], answer:3},
     {q:"Solve: y = 3 and y = x² − 1", options:["x = ±1","x = ±2","x = 0 only","x = 3"], answer:1},
     {q:"If the discriminant of the system's resulting equation is negative, the line and parabola ___.", options:["intersect at two points","are parallel","intersect at one point","do not intersect"], answer:3},
     {q:"Graphically, the solution(s) to a linear-quadratic system are ___.", options:["the x-intercepts of the parabola","the y-intercepts of both graphs","the point(s) where the line and parabola cross","the vertex of the parabola"], answer:2}
   ]},
  {subject:"Science", title:"Science Review: Connecting Chemistry, Biology, Physics", summary:"Students connect the three Grade 10 science strands and their real-world applications.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Biochemistry connects chemistry and biology through ___.", options:["only DNA","only enzymes","the study of chemical reactions in living things — photosynthesis (chemistry of carbon fixation), cellular respiration (oxidation of glucose), and protein synthesis (chemistry of the genetic code)","only cell division"], answer:2},
     {q:"Biophysics connects biology and physics through ___.", options:["only anatomy","only genetics","the application of physical principles to biological systems — fluid dynamics in blood flow, optics in vision, electricity in nerve impulses, and mechanics in muscle and bone","only ecology"], answer:2},
     {q:"Medical imaging (MRI, X-ray, ultrasound) applies ___.", options:["only biology","only chemistry","physics (electromagnetic radiation, magnetic fields, sound waves) to visualise internal biological structures — a synthesis of physics and biology","only genetics"], answer:2},
     {q:"Climate change is a phenomenon that requires ___.", options:["only chemistry to understand","only biology to understand","only physics to understand","understanding from all three strands: chemistry (greenhouse gas reactions), biology (ecosystem impacts), and physics (heat transfer, atmospheric science)"], answer:3},
     {q:"The synthesis of penicillin from a biological source (Penicillium mold) into a pharmaceutical involves ___.", options:["only biology","only physics","a combination of biology (identifying the natural compound), chemistry (purifying and synthesising it), and physics (understanding its mechanism of action)","only chemistry"], answer:2}
   ]},
  {subject:"History", title:"Year-End Review: Canadian History and Civics", summary:"Students synthesise learning across Grade 10 history, connecting historical developments to contemporary Canadian issues.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Which concept best connects Canada's experience in WWI and WWII to Canada's contemporary foreign policy?", options:["Isolationism","Military dominance","Colonial dependence","Canada as a "middle power" — committed to multilateralism, collective security, and peacekeeping rather than unilateral military action"], answer:3},
     {q:"The connection between the Quiet Revolution, the Official Languages Act, and the Quebec referendums is ___.", options:["no meaningful connection","the growth of English dominance","the ongoing tension between Quebec's desire for self-determination and the federal vision of a bilingual, multicultural Canada","only economic issues"], answer:2},
     {q:"Indigenous land claims, the Charter's Section 35, and the TRC Calls to Action are all part of ___.", options:["completed historical events","only legal debates","only provincial issues","Canada's ongoing — and still incomplete — process of addressing the colonial legacy and working toward reconciliation with Indigenous peoples"], answer:3},
     {q:"Canada's immigration and multiculturalism policies, while imperfect, reflect ___.", options:["a desire for cultural homogeneity","complete equality for all groups","no particular values","a stated commitment to diversity and inclusion that must be evaluated against lived realities of discrimination and inequality that many communities still face"], answer:3},
     {q:"The most important lesson from Grade 10 Canadian history and civics is ___.", options:["Canada is perfect","history has no relevance to today","all problems are already solved","democracy, rights, and justice are ongoing projects — the Canada of today was made by choices, and the Canada of the future will be made by the choices of people like you"], answer:3}
   ]},
]},
{day:15, label:"Day 15 — Fri", subjects:[
  {subject:"English", title:"Writing: Exam Preparation — Timed Literary Response", summary:"Students practise timed literary analysis, applying strategies for close reading under time pressure, efficient evidence selection, and focused analytical argumentation.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"For a timed literary essay (45-60 min), the best planning approach is ___.", options:["writing without planning","planning for 20+ minutes before writing","spending 5-7 minutes forming a clear thesis, selecting 2-3 pieces of evidence, and making a quick outline, then writing efficiently","only writing a conclusion first"], answer:1},
     {q:"Under time pressure, you should prioritise ___.", options:["perfect spelling throughout","covering every detail in the text","a clear argument with well-selected evidence over quantity of points — depth beats breadth in a time-limited analytical response","the longest quotations possible"], answer:2},
     {q:"If you get stuck mid-essay during an exam, you should ___.", options:["start over","leave the essay blank","stare at the page indefinitely","quickly reread the question, decide on your most important analytical point for the next paragraph, and continue writing even if it's less polished than ideal"], answer:3},
     {q:"The most common weakness in timed literary essays is ___.", options:["too much analysis","using quotations","excessive personal opinion","plot summary replacing analysis — strong exam essays spend most of their words analysing and interpreting, not describing what happens"], answer:3},
     {q:"After writing a timed essay, use any remaining time to ___.", options:["rewrite the entire introduction","add random quotations","add as many new points as possible","check that your thesis is clear, your evidence is relevant, and your analysis actually explains the connection between evidence and argument"], answer:3}
   ]},
  {subject:"Math", title:"Review: Grade 10 Math Comprehensive", summary:"Students review all major Grade 10 mathematics topics.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Solve the system: 2x + 3y = 12 and x − y = 1", options:["x = 3, y = 2","x = 2, y = 3","x = 4, y = 3","x = 5, y = 1"], answer:0},
     {q:"Factor: x² − 9", options:["(x − 3)²","(x + 9)(x − 1)","(x − 3)(x + 3)","(x + 9)(x − 9)"], answer:2},
     {q:"A triangle has sides a = 8, b = 6, and included angle C = 45°. Find c.", options:["c² = 64 + 36 − 2(8)(6)cos45° ≈ c ≈ 5.68","c = 14","c = 10","c = 45"], answer:0},
     {q:"The vertex of y = 2x² + 8x + 5 is at x = ___.", options:["x = −2 (from x = −8/(2×2))","x = 2","x = 5","x = 4"], answer:0},
     {q:"Two tangents from external point P to a circle each have length 10 cm. The angle between them is 60°. This is a ___ problem.", options:["trigonometry and circle geometry","pure algebra","systems of equations","only requiring the Pythagorean theorem"], answer:0}
   ]},
  {subject:"Science", title:"Science: Sustainability and Future Technologies", summary:"Students examine sustainable technologies — renewable energy, green chemistry, biotechnology — and their role in addressing 21st century challenges.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Green chemistry principles aim to ___.", options:["increase chemical production","maximise energy consumption","design chemical products and processes that reduce or eliminate hazardous substances — making chemistry more environmentally sustainable from the start","only apply to pharmaceuticals"], answer:2},
     {q:"Solar cells (photovoltaics) convert ___.", options:["heat to electricity","chemical energy to electricity","nuclear energy to electricity","light (photons) directly to electrical energy using semiconductor materials"], answer:3},
     {q:"Bioremediation is ___.", options:["removing beneficial organisms","only relevant in Canada","a technology using living organisms (bacteria, fungi, plants) to break down or neutralise pollutants in contaminated environments","a type of genetic engineering"], answer:2},
     {q:"Carbon capture and storage (CCS) ___.", options:["removes CO₂ from the atmosphere permanently always","is only theoretical","has no application to industry","captures CO₂ emissions at point sources (e.g., power plants) and stores them underground — controversial because it may allow fossil fuel use to continue while reducing emissions"], answer:2},
     {q:"The sustainable development concept of "meeting the needs of the present without compromising the ability of future generations to meet their own needs" was defined in ___.", options:["the Paris Agreement","the Kyoto Protocol","only recently","the 1987 Brundtland Report — and remains the foundational definition of sustainability"], answer:3}
   ]},
  {subject:"History", title:"Citizenship: Civic Participation and Democratic Engagement", summary:"Students examine forms of civic engagement, the responsibilities of citizenship, and how they can participate meaningfully in Canadian democracy now.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Voting is ___.", options:["the only form of civic engagement","the most effective form of advocacy","not important for young people","a fundamental right and responsibility in democracy — but just one of many forms of civic participation"], answer:3},
     {q:"Active citizenship includes ___.", options:["only voting","only serving in government","boycotting elections","staying informed, engaging with community issues, contacting elected representatives, participating in public consultations, joining community organisations, and advocating for change"], answer:3},
     {q:"Civil disobedience is ___.", options:["always illegal and never justified","always effective","never used in Canada","the deliberate, nonviolent breaking of a law as a form of protest against injustice — with a long history in Canadian and global activism"], answer:3},
     {q:"Media literacy is a civic skill because ___.", options:["it is not relevant to democracy","it is only for media professionals","only governments need it","citizens who can critically evaluate media — identifying bias, misinformation, and propaganda — make better informed democratic decisions"], answer:3},
     {q:"Young people's civic engagement matters because ___.", options:["youth have no political power","only adults can make change","voting is the only mechanism for change","young Canadians' voices, especially on climate, Indigenous reconciliation, and inequality, are essential to the democracy's future — and the decision to engage or disengage has real consequences"], answer:3}
   ]},
]},
];
{day:16, label:"Day 16 — Mon", subjects:[
  {subject:"English", title:"Reading: Short Fiction and the Short Story Form", summary:"Students analyse the distinctive features of the short story — economy of language, compressed plot, a single dominant effect — through close reading of examples.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The "single effect" principle (Poe) in short fiction means ___.", options:["stories must have only one character","stories should produce one dominant emotional or intellectual effect in the reader, to which every element contributes","stories must end happily","only one literary device is used"], answer:1},
     {q:"Economy in short fiction means ___.", options:["stories must be under 1000 words","every word must count — short stories cannot afford excess, so each detail, word, and image must do multiple jobs simultaneously","using only simple vocabulary","avoiding all description"], answer:1},
     {q:"The epiphany in short fiction (James Joyce's concept) is ___.", options:["the climax of the action","a religious vision","a character's sudden, profound moment of insight or recognition that changes their understanding","the opening image"], answer:2},
     {q:"Ambiguity in a short story ___.", options:["is always a flaw","means the story is poorly written","occurs when the story resists a single definitive interpretation, deliberately leaving room for multiple readings","only confuses readers"], answer:2},
     {q:"Analysing setting in a short story involves ___.", options:["only noting the location","ignoring setting for plot","examining how place and time create mood, reflect character psychology, and create symbolic meaning that extends beyond the physical","only noting the weather"], answer:2}
   ]},
  {subject:"Math", title:"Quadratics: Completing the Square", summary:"Students convert quadratic equations from standard to vertex form by completing the square, then use vertex form for graphing and solving.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Completing the square transforms ax² + bx + c into ___.", options:["factored form","slope-intercept form","vertex form a(x − h)² + k, revealing the vertex directly","scientific notation"], answer:2},
     {q:"To complete the square for x² + 6x, you add and subtract ___.", options:["9 (half of 6, squared: (6/2)² = 9)","6","3","36"], answer:0},
     {q:"x² + 8x + 3 in vertex form is ___.", options:["(x + 4)² − 13","(x + 4)² + 3","(x + 8)² − 13","(x − 4)² − 13"], answer:0},
     {q:"Solve x² − 4x − 5 = 0 by completing the square.", options:["x = 5 or x = −1 (vertex form: (x−2)² = 9, x−2 = ±3)","x = 4 or x = −5","x = 2 or x = −3","x = 5 or x = 1"], answer:0},
     {q:"Why is vertex form useful?", options:["It is never useful","Only for graphing horizontal lines","It directly reveals the vertex (h, k) and direction of opening, making graphing and optimisation problems much easier","It eliminates all other methods"], answer:2}
   ]},
  {subject:"Science", title:"Chemistry: Acids, Bases, and pH", summary:"Students examine Arrhenius acid/base definitions, the pH scale, neutralisation reactions, and indicators.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"An Arrhenius acid ___.", options:["accepts a proton","produces hydroxide ions in solution","produces hydrogen ions (H⁺) when dissolved in water","is always corrosive"], answer:2},
     {q:"An Arrhenius base ___.", options:["donates a proton","produces hydrogen ions","produces hydroxide ions (OH⁻) when dissolved in water","is always a liquid"], answer:2},
     {q:"A pH of 7 indicates ___.", options:["a strong acid","a strong base","a neutral solution (equal H⁺ and OH⁻)","a weak base"], answer:2},
     {q:"A neutralisation reaction between an acid and a base produces ___.", options:["only water","only a salt","water and a salt","only CO₂"], answer:2},
     {q:"Universal indicator or pH paper measures ___.", options:["temperature","concentration of the solution","the approximate pH of a solution by changing colour","only strong acids and bases"], answer:2}
   ]},
  {subject:"History", title:"Post-War Canada: Social Change 1945-1970", summary:"Students examine the baby boom, suburbanisation, the welfare state, women's liberation, and shifting Canadian values in the post-WWII decades.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's post-WWII welfare state included ___.", options:["only pensions","no new social programs","the creation of unemployment insurance (1940), family allowances (1944), hospital insurance (1957), Medicare (1966), and the Canada Pension Plan (1965)","only healthcare"], answer:2},
     {q:"The women's liberation movement in Canada in the 1960s-70s fought for ___.", options:["only voting rights (already won)","no significant changes","equal pay, reproductive rights, equal access to education and careers, and an end to legal and social discrimination","only workplace safety"], answer:2},
     {q:"The Royal Commission on the Status of Women (1970) ___.", options:["found no inequalities","was irrelevant","documented systemic gender inequality in Canada and made 167 recommendations that shaped decades of policy reform","only addressed employment issues"], answer:2},
     {q:"Post-WWII suburbanisation was driven by ___.", options:["a preference for dense urban living","a decline in car ownership","government housing policy, veterans' benefits, affordable mortgages, and the growth of car culture — creating the suburban lifestyle that defines much of Canada today","only immigration"], answer:2},
     {q:"Pierre Trudeau's "Just Society" vision (1968 onward) emphasised ___.", options:["regional favouritism","collective rights over individual rights","only economic growth","individual rights, bilingualism, multiculturalism, and the Charter — a vision of Canada as a rights-based, diverse nation rather than a British-French bicultural compact"], answer:3}
   ]},
]},
{day:17, label:"Day 17 — Tue", subjects:[
  {subject:"English", title:"Writing: Voice and Style in Creative Non-Fiction", summary:"Students examine and practise creative non-fiction (personal essay, literary journalism) — writing that uses narrative and literary techniques to engage with real events and ideas.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Creative non-fiction differs from journalism because ___.", options:["it invents facts","it ignores truth","it is shorter","while factually accurate, it uses literary techniques — scene-setting, character, metaphor, dialogue, and personal voice — to make real events and ideas as compelling as fiction"], answer:3},
     {q:"The personal essay is ___.", options:["a formal academic essay in first person","only for personal stories with no ideas","always about childhood memories","a literary form that uses personal experience as a lens to explore larger intellectual, social, or philosophical questions"], answer:3},
     {q:"Voice in creative non-fiction must be ___.", options:["formal and distant","identical to academic writing","generic and impersonal","distinctive and authentic — the writer's personality, perspective, and sensibility must be audible on every page"], answer:3},
     {q:"Literary journalism (narrative non-fiction) researches ___.", options:["only one source","without interviewing people","facts, people, and events thoroughly, then presents them through narrative techniques — creating scenes, developing characters, and building a story arc from real material","only online sources"], answer:3},
     {q:"The ethical obligation in creative non-fiction is ___.", options:["to entertain at all costs","to be as emotional as possible","to avoid research","to represent facts, people, and events truthfully — even when using literary techniques, you cannot invent or fabricate"], answer:3}
   ]},
  {subject:"Math", title:"Analytic Geometry: Circles and Equations", summary:"Students write and analyse equations of circles in the form (x−h)² + (y−k)² = r², identify centre and radius, and find intersections with lines.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The equation (x − 3)² + (y + 2)² = 25 represents a circle with centre ___ and radius ___.", options:["(3, −2) and 5","(−3, 2) and 5","(3, 2) and 25","(−3, −2) and 5"], answer:0},
     {q:"A circle centred at the origin with radius 7 has equation ___.", options:["x + y = 7","x² + y² = 49","x² + y² = 7","(x+7)² + (y+7)² = 0"], answer:1},
     {q:"To find whether a point lies inside, on, or outside a circle, you ___.", options:["use the slope formula","compare the distance from the point to the centre with the radius","always substitute into the linear equation","use the midpoint formula"], answer:1},
     {q:"A diameter of a circle has endpoints (2, 1) and (8, 5). The centre is at ___.", options:["(5, 3) — midpoint of the diameter","(6, 4)","(10, 6)","(3, 2)"], answer:0},
     {q:"The radius of a circle with centre (1, 2) passing through (4, 6) is ___.", options:["5 (distance from (1,2) to (4,6) = √9+16 = 5)","7","√7","3"], answer:0}
   ]},
  {subject:"Science", title:"Biology: Ecosystems and Human Impact", summary:"Students examine ecosystem dynamics, human impacts on biodiversity, and conservation approaches including stewardship and sustainable development.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A trophic cascade occurs when ___.", options:["the sun provides less energy","rainfall increases","a change in one trophic level (typically through predator loss or addition) causes large changes in population sizes at other levels","only in marine ecosystems"], answer:2},
     {q:"Eutrophication of lakes is caused by ___.", options:["acid rain only","oil spills","excess nutrients (often nitrogen and phosphorus from agricultural runoff) causing algal blooms, oxygen depletion, and ecosystem collapse","only industrial pollution"], answer:2},
     {q:"The concept of "ecological footprint" measures ___.", options:["how far you walk each day","only your carbon emissions","the land and water area required to sustain an individual's or population's consumption and absorb its waste","only food consumption"], answer:2},
     {q:"Ecological restoration involves ___.", options:["only building new habitats","leaving ecosystems alone completely","actively rehabilitating degraded, damaged, or destroyed ecosystems by reintroducing species, removing invasives, and improving habitat quality","only replanting trees"], answer:2},
     {q:"An ecosystem service is ___.", options:["a government program","only about food production","a service provided only by coral reefs","a benefit that humans receive from functioning ecosystems: clean water, air purification, pollination, climate regulation, flood control"], answer:3}
   ]},
  {subject:"History", title:"Canada and International Relations: 1970-2000", summary:"Students examine Canada's foreign policy — peacekeeping, the G7, NAFTA, and humanitarian commitments — in the late 20th century.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's peacekeeping role, established by Lester Pearson's Suez Crisis proposal (1956), meant ___.", options:["Canada sending troops to fight in all wars","Canada staying neutral in all conflicts","Canada contributing military personnel to UN peacekeeping operations to separate warring parties and maintain ceasefires — earning an international reputation for peace","Canada avoiding all international commitments"], answer:2},
     {q:"NAFTA (North American Free Trade Agreement, 1994) ___.", options:["only applied to Mexico and the US","was rejected by Canada","eliminated most tariffs on goods traded between Canada, the US, and Mexico, deeply integrating the three economies","had no impact on Canadian employment"], answer:2},
     {q:"Canada's military involvement in Kosovo (1999) and other humanitarian interventions reflected ___.", options:["isolationism","neutrality in all conflicts","the R2P (Responsibility to Protect) principle — that the international community has a duty to intervene when governments commit atrocities against their own people","only NATO obligations"], answer:2},
     {q:"The Chrétien government's decision NOT to join the US-led invasion of Iraq (2003) reflected ___.", options:["complete indifference to international affairs","anti-American sentiment","Canada's commitment to multilateralism — requiring UN Security Council authorisation before military action, even when this meant disagreeing with its closest ally","a lack of military capacity"], answer:2},
     {q:"Canada's G7 membership reflects ___.", options:["Canada being the world's largest economy","Canada having nuclear weapons","Canada's status as one of the world's major industrialised democratic nations, with influence in global economic and security discussions","Canada being an American state"], answer:2}
   ]},
]},
{day:18, label:"Day 18 — Wed", subjects:[
  {subject:"English", title:"Media Literacy: News Literacy and Misinformation", summary:"Students develop skills for critically evaluating news sources, identifying misinformation, and understanding how false information spreads.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Misinformation differs from disinformation in that ___.", options:["they are identical","misinformation is always worse","misinformation is false information spread without intent to deceive, while disinformation is deliberately false or misleading information spread to deceive","disinformation is accidental"], answer:2},
     {q:"A "deepfake" is ___.", options:["a credible news source","a type of documentary","a satire article","AI-generated video or audio that realistically depicts someone saying or doing something they never did — a growing tool for disinformation"], answer:3},
     {q:"The SIFT method for evaluating sources stands for ___.", options:["Search, Investigate, Find, Trust","Stop, Investigate the source, Find better coverage, Trace claims — a practical framework for quickly assessing online information credibility","Source, Integrity, Fact, Truth","Standard, Internet, Facts, Testing"], answer:1},
     {q:"Filter bubbles in social media refer to ___.", options:["blocking spam","only seeing news","algorithms that show you content matching your existing preferences and beliefs, creating an information environment that reinforces your worldview and filters out contradicting perspectives","parental controls"], answer:2},
     {q:"Lateral reading for fact-checking means ___.", options:["reading a page very carefully from top to bottom","relying on the website's "about" page","never reading news online","opening multiple new tabs to look for what other credible sources say about this source or claim, rather than judging the source only from the source itself"], answer:3}
   ]},
  {subject:"Math", title:"Functions: Introduction to Polynomial Functions", summary:"Students are introduced to polynomial functions — degree, end behaviour, zeros, and graphical features — as a bridge from Grade 10 quadratics to Grade 11 functions.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A polynomial function of degree n has ___.", options:["only n terms","exactly n roots always","a graph that crosses the x-axis n times always","at most n real zeros (x-intercepts), and its end behaviour is determined by the leading term"], answer:3},
     {q:"The end behaviour of a polynomial is determined by ___.", options:["all terms equally","the constant term","the leading term (the term with the highest degree and its coefficient)","the number of terms"], answer:2},
     {q:"A cubic function (degree 3) with positive leading coefficient has end behaviour: ___.", options:["rises left, falls right","falls both directions","rises both directions","falls left, rises right"], answer:3},
     {q:"The zeros of a polynomial function are ___.", options:["the y-intercepts","the slope values","the x-values where f(x) = 0 — the x-intercepts of the graph","the coefficient values"], answer:2},
     {q:"A polynomial function y = (x − 2)(x + 1)(x − 4) has x-intercepts at ___.", options:["x = 2, 1, 4","x = −2, 1, −4","x = 2, −1, 4","x = 0, 2, −1, 4"], answer:2}
   ]},
  {subject:"Science", title:"Physics: Nuclear Energy and Radiation Safety", summary:"Students examine nuclear fission reactors, CANDU reactor technology, radioactive waste management, and radiation safety.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The CANDU (CANada Deuterium Uranium) reactor is notable because ___.", options:["it uses enriched uranium","it was built in the US","it produces no radiation","it uses natural (unenriched) uranium as fuel and heavy water (D₂O) as a moderator — a uniquely Canadian nuclear technology"], answer:3},
     {q:"A nuclear reactor moderator ___.", options:["splits uranium atoms","provides the reaction's fuel","transfers heat to a generator","slows neutrons to the speed needed to sustain a fission chain reaction — in CANDU, heavy water is the moderator"], answer:3},
     {q:"Radioactive waste management is challenging because ___.", options:["nuclear waste is harmless","it decays in days","only liquid waste is produced","high-level radioactive waste remains dangerous for thousands of years, requiring secure long-term storage in geological repositories"], answer:3},
     {q:"Radiation protection uses the ALARA principle, which means ___.", options:["always leave all radiation alone","radioactive materials need no protection","As Low As Reasonably Achievable — minimise exposure through time, distance, and shielding","all radiation is immediately fatal"], answer:0},
     {q:"A significant advantage of nuclear power over fossil fuels is ___.", options:["no waste produced","no safety concerns","it produces no air pollution and very low greenhouse gas emissions during operation, providing large amounts of reliable baseload electricity","it uses renewable fuel"], answer:2}
   ]},
  {subject:"History", title:"Social Movements: Civil Rights and Equality in Canada", summary:"Students examine the civil rights struggles of Black Canadians, the women's movement, LGBTQ+ rights, and disability rights in the 20th-21st century.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The Viola Desmond case (1946) is significant because ___.", options:["it involved a legal dispute about property","it was about voting rights","she successfully argued her case","a Black Nova Scotian woman was arrested for refusing to leave a whites-only section of a movie theatre — her case became a landmark in the civil rights history of Black Canadians"], answer:3},
     {q:"The Nova Scotia Human Rights Act (1963) and the Canadian Human Rights Act (1977) were ___.", options:["purely symbolic","unenforceable","legislation that prohibited discrimination in public life on grounds of race, religion, sex, and other grounds, providing legal tools to fight discrimination","only about employment"], answer:2},
     {q:"LGBTQ+ rights milestones in Canada include ___.", options:["no significant legal changes","only the decriminalisation of homosexuality","only marriage equality","decriminalisation of homosexuality (1969), addition of sexual orientation to the Charter (1995 SCC ruling), and equal marriage rights nationally (2005)"], answer:3},
     {q:"The disability rights movement in Canada achieved ___.", options:["no legal recognition","only charitable support","recognition in the Charter (Section 15), the Accessibility for Ontarians with Disabilities Act (2005), and the Accessible Canada Act (2019)","only building code changes"], answer:2},
     {q:"A common pattern across all these civil rights movements is ___.", options:["change was granted voluntarily by governments","each movement operated in isolation","courts did all the work","marginalised groups had to organise, advocate, and sometimes challenge law in courts over decades before rights were recognised and enforced"], answer:2}
   ]},
]},
{day:19, label:"Day 19 — Thu", subjects:[
  {subject:"English", title:"Shakespeare: A Midsummer Night's Dream or Julius Caesar", summary:"Students study a second Shakespeare play, analysing dramatic structure, language, and themes with greater independence and sophistication than in Grade 9.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"In Shakespeare's comedies, the central disruption is ___.", options:["a tragic death","a political crisis","a major war","a social or romantic disorder that is resolved by the play's end — usually through marriage or reconciliation"], answer:3},
     {q:"In Julius Caesar, Brutus's fatal flaw is arguably ___.", options:["cowardice","greed","ambition","an idealism that blinds him to political realities and allows him to be manipulated by Cassius"], answer:3},
     {q:"Antony's funeral speech ("Friends, Romans, countrymen") is dramatically effective because ___.", options:["he directly insults the conspirators","he praises Brutus and the conspirators throughout but subtly turns the crowd against them through irony — a masterclass in rhetoric","he reveals the assassination plot","he appeals only to reason"], answer:1},
     {q:"The theme of appearance vs. reality in Shakespeare is explored through ___.", options:["characters who are always honest","only supernatural elements","disguise, self-deception, political manipulation, and the gap between public persona and private reality — characters are often not what they seem","only the comedies"], answer:2},
     {q:"Studying Shakespeare with greater independence means ___.", options:["only reading sparknotes","the teacher explains everything","making your own interpretive choices — selecting which scenes to focus on, forming your own thematic arguments, and supporting them with textual evidence","avoiding personal interpretation"], answer:2}
   ]},
  {subject:"Math", title:"Review: Functions, Geometry, and Systems", summary:"Students consolidate Grade 10 mathematics — quadratics, trigonometry, analytic geometry, linear systems, and an introduction to polynomial functions.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The parabola y = −3(x + 2)² + 7 has vertex ___ and opens ___.", options:["(2, 7) downward","(−2, 7) downward","(−2, 7) upward","(2, −7) upward"], answer:1},
     {q:"Find the angle in a triangle where cos A = (9 + 25 − 16)/(2 × 3 × 5) = 18/30.", options:["A ≈ 53°","A = 90°","A ≈ 37°","A = 60°"], answer:0},
     {q:"The circle (x + 1)² + (y − 3)² = 16 has centre ___ and radius ___.", options:["(1, −3) and 4","(−1, 3) and 16","(−1, 3) and 4","(1, 3) and 4"], answer:2},
     {q:"Solve: 3x² − x − 2 = 0", options:["x = 1 and x = −2/3","x = −1 and x = 2/3","x = 1 and x = 2/3","x = −1 and x = −2/3"], answer:0},
     {q:"A polynomial y = x(x − 3)(x + 2) has zeros at ___.", options:["x = 0, 3, −2","x = 0, −3, 2","x = 1, 3, −2","x = 3 and x = −2 only"], answer:0}
   ]},
  {subject:"Science", title:"Science: Energy Systems and Sustainability", summary:"Students examine Ontario's energy mix, the transition to renewable energy, and the science behind solar, wind, hydro, and nuclear power.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Ontario's electricity mix includes ___.", options:["mostly coal","only nuclear","mostly imported US electricity","a combination of nuclear (~60%), hydro (~24%), wind and solar (~9%), and gas — making it one of the lowest-carbon grids in the world"], answer:3},
     {q:"Solar photovoltaic (PV) cells convert ___.", options:["heat directly to electricity","chemical energy to electricity","wind energy to electricity","light (photons) to electricity via the photovoltaic effect in semiconductor materials"], answer:3},
     {q:"Wind turbines convert ___.", options:["solar energy to wind","chemical energy to electricity","the kinetic energy of moving air to rotational mechanical energy, which drives a generator to produce electricity","water pressure to electricity"], answer:2},
     {q:"Hydroelectric power generates electricity by ___.", options:["burning water","using solar panels on water","harnessing the gravitational potential energy of falling water to spin turbines connected to generators","splitting water molecules"], answer:2},
     {q:"A major challenge of renewable energy transition is ___.", options:["renewables produce too much electricity","nuclear is already renewable","fossil fuels will run out soon","intermittency — solar produces no electricity at night, and wind is variable — requiring energy storage solutions like batteries or pumped hydro"], answer:3}
   ]},
  {subject:"History", title:"Canada's Constitution and Federalism", summary:"Students examine the Canadian Constitution — the division of powers, federalism, constitutional amendments, and ongoing debates about the constitutional order.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The division of powers in the Constitution Act (1867) allocates ___.", options:["all power to provinces","all power to the federal government","certain powers exclusively to the federal government (e.g., defence, criminal law), others to provinces (e.g., education, health care), and some to both (concurrent)","powers only based on tradition"], answer:2},
     {q:"Section 91 lists federal powers, which include ___.", options:["education and hospitals","property and civil rights","criminal law, banking, currency, navigation, and trade — matters of national concern","only defence and foreign affairs"], answer:2},
     {q:"Section 92 lists provincial powers, which include ___.", options:["criminal law and banking","defence and foreign policy","property and civil rights, hospitals, education, and natural resources within the province","taxation of all kinds"], answer:2},
     {q:"Intergovernmental transfers (e.g., Equalization) redistribute ___.", options:["tax dollars from provinces to the federal government","money between private businesses","money from wealthier provinces (through federal taxation) to provinces with lower fiscal capacity, enabling comparable public services across Canada","only to Quebec"], answer:2},
     {q:"A constitutional amendment in Canada typically requires ___.", options:["only a federal majority vote","only a referendum","a provincial legislature vote alone","the consent of Parliament and at least 7 of 10 provinces representing 50% of the population — the "7/50 formula""], answer:3}
   ]},
]},
{day:20, label:"Day 20 — Fri", subjects:[
  {subject:"English", title:"Independent Novel Study: Final Essay", summary:"Students write a full independent analytical essay on their novel, demonstrating the full range of Grade 10 literary analysis skills.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The most important quality of a Grade 10 analytical essay is ___.", options:["length","number of quotations","correct spelling","a clear, arguable thesis supported by well-chosen evidence and analytical reasoning that connects evidence to argument"], answer:3},
     {q:"Literary analysis differs from plot summary in that ___.", options:["plot summary is more valuable","they are identical","literary analysis requires less detail","literary analysis asks "how" and "why" — examining the author's choices and their effects — while plot summary only describes "what happens""], answer:3},
     {q:"An effective concluding paragraph ___.", options:["just repeats the introduction","leaves the reader with nothing new","adds an entirely new argument","synthesises the essay's argument, extends the thesis to a larger significance, and leaves the reader with a new insight or question"], answer:3},
     {q:"Revision of an essay differs from proofreading in that ___.", options:["they are the same thing","only spelling matters","revision is for surface errors only","revision addresses big-picture issues (argument, structure, evidence, analysis) while proofreading addresses surface errors (grammar, spelling, punctuation)"], answer:3},
     {q:"Receiving and using feedback means ___.", options:["accepting all suggestions uncritically","rejecting all external input","writing without revision","reading feedback carefully, asking what specific concerns underlie the comments, and making deliberate choices about what to change and why"], answer:3}
   ]},
  {subject:"Math", title:"Introduction to Functions: Domain, Range, Notation", summary:"Students are introduced to functions formally — function notation f(x), domain, range, mapping diagrams, and identifying functions vs. relations.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A function is a relation in which ___.", options:["every y-value maps to one x-value","every x-value maps to exactly one y-value","all x and y values are positive","every ordered pair is (x, x)"], answer:1},
     {q:"The domain of a function is ___.", options:["the set of all output values","the graph of the function","the set of all possible input values (x-values)","the rule of the function"], answer:2},
     {q:"The range of a function is ___.", options:["the set of all input values","the equation of the function","the set of all possible output values (y-values)","the domain reflected"], answer:2},
     {q:"f(x) = 3x − 2. Find f(4).", options:["10","14","12","6"], answer:0},
     {q:"The vertical line test determines ___.", options:["the domain","the range","the y-intercept","whether a graph represents a function — if any vertical line intersects the graph more than once, it is not a function"], answer:3}
   ]},
  {subject:"Science", title:"Chemistry: Organic Chemistry Introduction", summary:"Students are introduced to organic compounds — hydrocarbons (alkanes, alkenes, alkynes), functional groups, and their importance in medicine, materials, and environment.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Organic chemistry is the study of ___.", options:["all chemical reactions","only natural substances","only laboratory-made substances","compounds containing carbon — the chemistry of life and of most fuels, medicines, plastics, and synthetic materials"], answer:3},
     {q:"Hydrocarbons are compounds containing only ___.", options:["carbon and oxygen","carbon and nitrogen","carbon and hydrogen","carbon only"], answer:2},
     {q:"Alkanes are hydrocarbons with ___.", options:["at least one double bond","at least one triple bond","only single carbon-carbon bonds — the simplest hydrocarbon family, e.g., methane, ethane, propane","aromatic rings"], answer:2},
     {q:"Alkenes contain ___.", options:["only single bonds","at least one triple C-C bond","at least one double carbon-carbon bond (C=C), making them more reactive than alkanes","only aromatic rings"], answer:2},
     {q:"Functional groups in organic chemistry are ___.", options:["always carbon only","specific atoms or groups of atoms that determine the characteristic chemical reactions of a molecule (e.g., –OH = alcohol, –COOH = carboxylic acid)","only found in natural compounds","only in plastics"], answer:1}
   ]},
  {subject:"History", title:"The Environment and Politics: Canada's Climate Debate", summary:"Students examine the political dimensions of climate change in Canada — carbon pricing, oil sands, Indigenous rights, and intergenerational justice.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's carbon pricing system (federal carbon tax/backstop) ___.", options:["gives money to oil companies","increases government profit directly","has faced no political opposition","puts a price on carbon emissions to incentivise reduction, with proceeds returned to Canadians as rebates — controversial politically, especially in fossil fuel-dependent provinces"], answer:3},
     {q:"Alberta's oil sands are significant because ___.", options:["they are small and economically minor","they represent a conflict between environmental and economic interests — a massive economic resource and employer that also produces some of the world's most GHG-intensive oil, intersecting with Indigenous rights issues","they are already shut down","they are internationally praised universally"], answer:1},
     {q:"Intergenerational justice in the climate debate means ___.", options:["only current generations matter","older generations should pay all costs","current decisions about emissions and fossil fuel development will disproportionately affect future generations who had no vote in those decisions","young people have no role in the debate"], answer:2},
     {q:"Indigenous peoples are disproportionately affected by climate change because ___.", options:["they live in cities mostly","they are too small a population to be significantly affected","many Indigenous communities live in northern and coastal regions most vulnerable to climate impacts (permafrost thaw, sea level rise, disruption of traditional hunting/fishing/gathering)","they have caused the most emissions"], answer:2},
     {q:"Climate litigation — suing governments for inadequate climate action — is ___.", options:["not happening in Canada","always unsuccessful","only a European tactic","an emerging legal strategy in Canada and globally, with youth-led cases challenging governments' insufficient climate policies under constitutional rights frameworks"], answer:3}
   ]},
]},
{day:21, label:"Day 21 — Mon", subjects:[
  {subject:"English", title:"Media Creation: Short Film or Podcast Episode", summary:"Students plan, script, and produce a short media piece (podcast episode or video essay) on a literary or social topic, applying media literacy and production skills.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A video essay differs from a documentary in that ___.", options:["it uses no research","it is always shorter","it is fictional","it is usually narrated by a single voice presenting a personal analytical argument, often directly to camera — blending documentary and persuasive essay forms"], answer:3},
     {q:"Pre-production in media making includes ___.", options:["only editing","only recording","only publishing","all the planning work before recording begins: research, scripting, storyboarding, location scouting, and equipment preparation"], answer:3},
     {q:"A strong script for a media piece ___.", options:["is identical to a written essay","is read word for word with no improvisation","is optional","serves as a guide, with natural speech rhythms, clear structure, and room for the speaker's personality to come through"], answer:3},
     {q:"Ethical considerations in creating media about real people or communities include ___.", options:["no ethics apply in student media","only copyright issues matter","informed consent, accurate representation, avoiding harm, and being especially careful with vulnerable communities whose stories you do not share","only privacy in social media"], answer:2},
     {q:"Publishing a media piece to a real audience (school website, YouTube) means ___.", options:["no additional responsibility","only technical quality matters","all facts must be perfect","it is a public act with real consequences — accuracy, fairness, and quality matter far more than when the audience is only your teacher"], answer:3}
   ]},
  {subject:"Math", title:"Quadratics and Functions: Consolidation", summary:"Students review and consolidate Grade 10 quadratic and function concepts, preparing for Grade 11 Functions.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Convert y = x² − 6x + 11 to vertex form.", options:["y = (x − 3)² + 2","y = (x + 3)² − 11","y = (x − 6)² + 2","y = (x − 3)² − 9 + 11 = (x−3)²+2"], answer:0},
     {q:"A function has domain {x ∈ ℝ | x ≠ −2}. What type of function likely has this restriction?", options:["A linear function","A polynomial function","A rational function with denominator (x + 2)","A quadratic function"], answer:2},
     {q:"f(x) = x² − 4 and g(x) = 2x + 1. Find f(g(2)).", options:["f(5) = 21","f(2) + g(2) = 5","g(f(2)) = 1","f(5) = 25"], answer:0},
     {q:"The zeros of f(x) = x² − x − 6 are ___.", options:["x = 2 and x = −3","x = −2 and x = 3","x = 3 and x = 2","x = 6 and x = −1"], answer:1},
     {q:"A quadratic with vertex (2, −3) and passing through (0, 1) has a = ___.", options:["a = 1","a = −1","a = 4","a = 0"], answer:0}
   ]},
  {subject:"Science", title:"Science: Human Health and Biotechnology", summary:"Students examine how scientific knowledge is applied in medicine — vaccines, antibiotics, gene therapy, and CRISPR — and the ethical questions raised.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"mRNA vaccines (like those developed for COVID-19) work by ___.", options:["injecting a weakened virus","injecting DNA into the nucleus","using a live pathogen","delivering messenger RNA instructions that cause your cells to produce a viral protein, training your immune system to recognise and fight the real pathogen"], answer:3},
     {q:"Antibiotic resistance is a growing problem because ___.", options:["antibiotics are now weaker","bacteria have evolved to survive antibiotic treatment, often due to overuse or misuse of antibiotics — a major public health threat requiring careful prescribing and new antibiotic development","viruses have become resistant","resistance only affects hospitals"], answer:1},
     {q:"CRISPR-Cas9 genome editing allows ___.", options:["only reading DNA","only destroying cells","precise cutting and editing of DNA sequences at targeted locations, enabling potential treatments for genetic diseases and raising ethical questions about germline editing and enhancement","only adding genes"], answer:2},
     {q:"Personalised medicine uses ___.", options:["the same treatment for all patients","only natural remedies","no data from patients","genetic and other biological data to tailor medical treatments to individual patients, improving effectiveness and reducing side effects"], answer:3},
     {q:"The ethical principle of informed consent in medicine means ___.", options:["doctors decide what is best","patients must accept recommended treatment","patients have the right to receive complete, understandable information about a proposed treatment or research study before deciding whether to participate","only applies in research"], answer:2}
   ]},
  {subject:"History", title:"Canada Today: Contemporary Challenges", summary:"Students examine contemporary challenges facing Canada: reconciliation, climate, housing, inequality, and democratic participation.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's housing crisis affects young Canadians because ___.", options:["housing is affordable everywhere","only major cities have issues","the crisis is limited to coastal cities","rapidly rising home prices and rents in most Canadian cities have made homeownership essentially unattainable for most people your age, raising fundamental questions about intergenerational equity"], answer:3},
     {q:"Income inequality in Canada has ___.", options:["decreased dramatically","remained perfectly stable","has no effect on social outcomes","grown significantly since the 1980s, with the top income earners capturing an increasing share of income growth while wages for middle and lower income Canadians have stagnated in real terms"], answer:3},
     {q:"Truth and Reconciliation in Canada is ___.", options:["complete","only about acknowledging the past","not relevant to young Canadians","an ongoing process of healing, redress, and structural change — including implementation of the 94 Calls to Action, land rights resolution, and building genuine nation-to-nation relationships"], answer:3},
     {q:"Declining voter turnout (especially among youth) is concerning because ___.", options:["democracy works fine without participation","politicians will decide what young people need","youth issues are always addressed regardless","when young people disengage from formal politics, their interests are underrepresented in policy decisions that will affect their lives for decades"], answer:3},
     {q:"A genuinely engaged Grade 10 citizen can ___.", options:["only vote in 3-6 years","do nothing meaningful until they're older","change nothing at the local level","stay informed, discuss issues critically, join youth advocacy groups, contact elected officials, participate in public consultations, and model the democratic citizenship Canada needs"], answer:3}
   ]},
]},
{day:22, label:"Day 22 — Tue", subjects:[
  {subject:"English", title:"Writing: Final Culminating Task", summary:"Students complete a major writing task — analytical essay, creative work, or multimodal project — that demonstrates the full range of Grade 10 English skills.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A culminating writing task should demonstrate ___.", options:["only your vocabulary knowledge","only your grammar skills","a wide range of skills learned over the year: analytical thinking, thesis development, evidence use, stylistic control, and sophisticated engagement with ideas","only your length capabilities"], answer:2},
     {q:"Self-editing a major piece means ___.", options:["fixing only spelling errors","asking a friend to rewrite it","reading aloud to catch awkward phrasing","systematically reviewing for argument clarity, evidence quality, analytical depth, cohesion, and then surface errors — in that order"], answer:3},
     {q:"A strong culminating essay demonstrates intellectual maturity by ___.", options:["avoiding complex sentences","using only safe, obvious arguments","acknowledging complexity — engaging with nuance, counterarguments, and the limitations of your own interpretation, rather than oversimplifying","only using approved ideas"], answer:2},
     {q:"Publishing or presenting a culminating piece to a real audience ___.", options:["only stresses students","is irrelevant to the work's quality","makes writing more meaningful and develops genuine communication skills by creating authentic purpose and accountability beyond the classroom","should be avoided"], answer:2},
     {q:"Reflecting on a year of writing development means ___.", options:["only comparing grades","ignoring what you've learned","recognising that writing is a thinking skill — as your writing has improved, so has your ability to form, develop, and communicate complex ideas","only noting what still needs work"], answer:2}
   ]},
  {subject:"Math", title:"Exam Preparation: Grade 10 Mathematics Review", summary:"Students review all major Grade 10 math concepts for assessment readiness.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Solve: x² + 2x − 15 = 0", options:["x = 3 and x = −5","x = −3 and x = 5","x = 5 and x = −5","x = 3 and x = 5"], answer:0},
     {q:"In triangle ABC, a = 10, b = 7, B = 30°. Use the Sine Law to find sin A.", options:["sin A = 10 sin30° / 7 = 5/7 ≈ 0.714","sin A = 7/10","sin A = sin30°","sin A = 1"], answer:0},
     {q:"The midpoint of (−4, 6) and (2, −2) is ___.", options:["(−1, 2)","(−2, 4)","(−3, 4)","(1, −2)"], answer:0},
     {q:"A parabola has zeros at x = −1 and x = 5 and passes through (0, −5). Find a.", options:["a = 1","a = −1","a = 5","a = −5"], answer:0},
     {q:"If f(x) = 2x² − 3, find f(−2).", options:["f(−2) = 2(4) − 3 = 5","f(−2) = −11","f(−2) = 4 − 3 = 1","f(−2) = −4 − 3 = −7"], answer:0}
   ]},
  {subject:"Science", title:"Science: Review and Synthesis", summary:"Students synthesise all three Grade 10 science strands — chemistry, biology, and physics — and their interconnections.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Chemical bonding concepts explain ___.", options:["only why acids are sour","physical, biological, and chemical properties of all substances: why water is liquid at room temperature, why DNA has a double helix, why metals conduct electricity","only laboratory reactions","only ionic compounds"], answer:1},
     {q:"Evolution (biology) connects to chemistry through ___.", options:["no connection exists","only fossil records","mutation being a chemical process — changes in DNA base sequences caused by chemical damage, replication errors, or mutagens lead to the genetic variation on which natural selection acts","only protein structure"], answer:2},
     {q:"Newton's laws and kinematics explain ___.", options:["only car crashes","only sports","both mechanical motion at the human scale and, with quantum modifications, the behaviour of electrons in atoms — physics underlies both chemistry and biology","only space travel"], answer:2},
     {q:"Climate change is a Grade 10 Science topic because ___.", options:["it only involves biology","it only involves physics","it only involves chemistry","it requires all three strands: the chemistry of greenhouse gases, the biology of ecosystem impacts, and the physics of heat transfer and atmospheric energy balance"], answer:3},
     {q:"The most important lesson from Grade 10 Science is ___.", options:["memorising all the formulas","science is a collection of fixed facts","only chemistry is important","science is a way of thinking — a method for using evidence, model-building, and testing to understand the world, which applies across disciplines and to the decisions of everyday life"], answer:3}
   ]},
  {subject:"History", title:"Grade 10 History: Looking Back and Forward", summary:"Students synthesise Grade 10 history and connect it to their emerging understanding of citizenship and their role in the future of Canada.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The thread connecting Canada's WWII experience, the Charter, and reconciliation is ___.", options:["only conflict","only politics","the ongoing expansion of who is recognised as a full, rights-bearing member of the Canadian community — from enfranchising women and fighting fascism to protecting minority rights and acknowledging Indigenous sovereignty","only economic growth"], answer:2},
     {q:"Canada's relationship with the United States, seen across the 20th century, is best described as ___.", options:["complete Canadian independence","identical interests always","complete American dominance","deep economic and cultural integration combined with persistent efforts to maintain a distinct Canadian identity — a relationship of both partnership and ongoing negotiation of sovereignty"], answer:3},
     {q:"The evolution of immigration policy from exclusion to multiculturalism shows ___.", options:["Canada was always multicultural","policy never matters","change only happens through demographics","policy reflects the values and power dynamics of its time — and can change dramatically when social movements, court decisions, and political will align"], answer:2},
     {q:"Climate change is a historical issue because ___.", options:["it only started recently","it has nothing to do with history","it only matters to scientists","its causes are rooted in historical decisions about industrialisation and fossil fuels, and its solutions require understanding the history of international cooperation, Indigenous knowledge, and political economy"], answer:3},
     {q:"As a Grade 10 student completing this course, your most important takeaway is ___.", options:["dates and facts about WWII","how to memorise the Constitution","only Quebec history matters","that history is not about the past — it is about understanding how we got here and taking responsibility for where we go next"], answer:3}
   ]},
]},
{day:23, label:"Day 23 — Wed", subjects:[
  {subject:"English", title:"Reading and Writing: Synthesis Task", summary:"Students read two or three related texts on a contemporary issue and write a synthesis essay that integrates ideas across sources with an original argument.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Synthesising sources means ___.", options:["summarising each source separately","using only one source at a time","copying from all sources equally","building a unified, original argument that draws on multiple sources — connecting, comparing, and using them to support your own analytical position"], answer:3},
     {q:"A synthesis essay differs from a research essay in that ___.", options:["it uses no sources","it is always shorter","it requires original research","it focuses on connecting and integrating a given set of sources rather than independently researching a topic, though both require original analytical argument"], answer:3},
     {q:"When sources disagree, a synthesis essay should ___.", options:["only use the sources that agree with your thesis","ignore the disagreement","present only one side","acknowledge and explore the tension between sources, using it to develop a more nuanced argument that accounts for the complexity"], answer:3},
     {q:"Original voice in synthesis means ___.", options:["copying the authors' styles","avoiding analysis","using the authors' words only","your thesis and argument are your own — sources provide evidence, but you are the author of the argument"], answer:3},
     {q:"The most common weakness in synthesis writing is ___.", options:["too much original argument","over-reliance on quotations","too many sources","the "laundry list" structure — listing what each source says without building a coherent, unified analytical argument that advances your own thesis"], answer:3}
   ]},
  {subject:"Math", title:"Trigonometry Extension: Sine and Cosine Graphs", summary:"Students explore the graphs of y = sinx and y = cosx, identifying amplitude, period, phase shift, and vertical shift for transformations.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The period of y = sinx is ___.", options:["180°","90°","360° (or 2π radians) — the function completes one full cycle every 360°","720°"], answer:2},
     {q:"The amplitude of y = 3sin(x) is ___.", options:["3 — the maximum displacement from the midline","9","1/3","1"], answer:0},
     {q:"In y = sin(2x), the period is ___.", options:["720°","360°","90°","180° — multiplying x by 2 halves the period"], answer:3},
     {q:"A phase shift of 30° in y = cos(x − 30°) means ___.", options:["the graph shifts up 30°","the graph shifts left 30°","the graph compresses horizontally","the graph shifts right 30°"], answer:3},
     {q:"The vertical shift in y = sinx + 2 is ___.", options:["the period changes to 2","the amplitude is 2","the graph shifts up 2 units","the frequency doubles"], answer:2}
   ]},
  {subject:"Science", title:"Physics: Modern Physics Concepts", summary:"Students are introduced to key modern physics concepts: quantum theory, the photoelectric effect, the wave-particle duality of light, and relativistic effects.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The photoelectric effect showed that ___.", options:["light is purely a wave","electrons have no mass","light behaves as particles (photons) — each photon carries energy proportional to its frequency, and can eject electrons from metal surfaces if its energy exceeds a threshold","electricity can produce light"], answer:2},
     {q:"Wave-particle duality means ___.", options:["waves and particles are unrelated","only light has this duality","quantum objects like electrons and photons exhibit both wave-like and particle-like properties depending on how they are observed or measured","all objects behave this way at human scale"], answer:2},
     {q:"Einstein's E = mc² means ___.", options:["energy is always conserved","mass and energy are different and unrelated","matter and energy are equivalent — mass can be converted to energy (as in nuclear reactions) and energy to mass","only applies in nuclear physics"], answer:2},
     {q:"Quantum mechanics is necessary because ___.", options:["classical physics explains everything","atoms follow the same rules as baseballs","there are no laws at atomic scale","classical physics fails to describe the behaviour of particles at atomic and subatomic scales — quantum mechanics provides the correct framework"], answer:3},
     {q:"The uncertainty principle (Heisenberg) states ___.", options:["scientists are not precise enough","measurement is always perfect","position and momentum can always both be determined precisely","you cannot precisely know both the position and momentum of a particle simultaneously — a fundamental limit of nature, not of measurement technology"], answer:3}
   ]},
  {subject:"History", title:"Historical Thinking: Applying Concepts", summary:"Students apply the six historical thinking concepts to a contemporary Canadian issue, demonstrating the relevance of historical reasoning to present-day problems.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Applying historical significance to a contemporary issue means asking ___.", options:["is this event recent?","is this in the news?","how many people are affected?","why does this matter? Who is affected, and what long-term consequences might it have — the same criteria we use to assess historical events"], answer:3},
     {q:"Using cause and consequence thinking about climate policy means ___.", options:["only looking at economic causes","assuming one cause","only considering future consequences","tracing the multiple causes of current emissions, the complex consequences of different policy choices, and the interconnected systems that make climate change both a cause and consequence of other issues"], answer:3},
     {q:"Continuity and change thinking reveals that some aspects of inequality in Canada ___.", options:["have completely disappeared","are entirely new","are unrelated to history","have persisted over generations (systemic racism, Indigenous dispossession) while others have changed significantly — understanding both helps identify what still needs to change"], answer:2},
     {q:"Historical perspective taking applied to contemporary debates means ___.", options:["only studying the past","avoiding taking any position","caring only about your own perspective","understanding that different people hold different values and see the same issue through different historical experiences — this builds empathy and better problem-solving"], answer:3},
     {q:"The ethical dimension of historical thinking applied today means ___.", options:["judging only historical actors","avoiding all moral judgment","not caring about outcomes","recognising that we have responsibilities arising from historical injustices, and that our own choices about how to respond to these injustices are themselves historical and ethical decisions"], answer:3}
   ]},
]},
{day:24, label:"Day 24 — Thu", subjects:[
  {subject:"English", title:"Literature: A Non-Western Perspective", summary:"Students read and analyse a novel or collection of short stories from a non-Western tradition (translated or originally in English), examining cultural context and literary universality.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Why study literature from non-Western traditions?", options:["Only Western literature has universal themes","Non-Western literature is too difficult","World literature uses only different settings","World literature expands our understanding of universal human experiences while also challenging Western assumptions about how stories work, what values matter, and whose experiences are central"], answer:3},
     {q:"When reading literature in translation, it is important to acknowledge ___.", options:["translations are always perfect","the original text is irrelevant","no meaning is lost in translation","that translation always involves interpretation — choices made by the translator shape the text, and some nuances of the original language and culture may be altered or lost"], answer:3},
     {q:"Cultural context helps readers understand ___.", options:["only surface details","nothing important","only historical facts","references, values, and narrative conventions that may be unfamiliar — without context, important meanings may be missed or misread from a Western perspective"], answer:2},
     {q:"Universal themes in world literature include ___.", options:["only themes from each culture","no shared human experiences across cultures","unique themes in each tradition","love, loss, justice, identity, family, power, and what it means to be human — themes that transcend culture even as they are expressed through culturally specific stories"], answer:3},
     {q:"Avoiding cultural projection means ___.", options:["learning nothing from other cultures","reading non-Western literature as confirmation of Western views","interpreting cultural differences as deficiencies from a Western norm","reading literature from other traditions on its own terms, with curiosity about difference rather than measuring it against Western literary standards"], answer:3}
   ]},
  {subject:"Math", title:"Exam Readiness: Problem Solving and Communication", summary:"Students practise explaining their mathematical reasoning clearly in writing — an essential skill for senior math assessments.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Mathematical communication means ___.", options:["only showing numerical steps","avoiding words in solutions","always using symbols only","clearly explaining your reasoning in words alongside mathematical work — describing what you did and why, so a reader can follow your thinking"], answer:3},
     {q:"When solving a word problem, the first step is ___.", options:["doing the calculation immediately","drawing a picture","defining variables and restating what is given and what is being asked — this prevents errors and demonstrates clear thinking","checking the answer first"], answer:2},
     {q:"Checking reasonableness of an answer means ___.", options:["only checking arithmetic","recalculating the same way","always getting a decimal","asking whether your answer makes sense in the context of the problem — a negative time, a probability above 1, or an impossibly large distance signal an error"], answer:0},
     {q:"Partial credit on exams usually requires ___.", options:["a correct final answer only","showing only the setup","all correct or nothing","showing all work, even if the final answer is wrong — examiners award marks for correct method and reasoning"], answer:3},
     {q:"The most effective exam preparation for math is ___.", options:["reading the textbook","memorising formulas only","re-reading your notes","practising problems under time pressure, then reviewing errors carefully to understand what went wrong — not just redoing problems you already know"], answer:3}
   ]},
  {subject:"Science", title:"Science: Career Connections", summary:"Students explore STEM careers and how Grade 10 science knowledge connects to post-secondary pathways and the workforce.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Environmental science careers connect to ___.", options:["only biology from Grade 10","only physics","a combination of biology (ecosystems), chemistry (pollution analysis), and physics (atmospheric science) from Grade 10, plus mathematics, geography, and policy","only laboratory work"], answer:2},
     {q:"Biomedical engineering connects to ___.", options:["only physics","only chemistry","biology (cell and human biology) and physics (mechanics, fluids, imaging) and chemistry (biomaterials)","only medicine"], answer:2},
     {q:"Data science, a rapidly growing field, requires ___.", options:["only computer science","only mathematics","no science background","strong mathematical foundations (statistics, algebra) combined with domain knowledge in whatever field the data is from — including science fields"], answer:3},
     {q:"Clean energy technology careers require knowledge of ___.", options:["only electrical engineering","only economics","physics (electricity, thermodynamics), chemistry (batteries, fuel cells), and materials science — all rooted in Grade 10 science concepts","only environmental science"], answer:2},
     {q:"The most transferable skill from Grade 10 science to any career is ___.", options:["memorising formulas","lab technique","only knowing specific content","evidence-based reasoning — the ability to define a problem, gather data, analyse it critically, and draw justified conclusions"], answer:3}
   ]},
  {subject:"History", title:"Reflection: My Canada", summary:"Students write a personal reflection on what Canada means to them, connecting historical learning to personal identity and future citizenship commitments.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A thoughtful reflection on Canadian identity should ___.", options:["only celebrate Canada","only criticise Canada","remain neutral on all issues","acknowledge both Canada's genuine achievements and its significant failures, and consider what kind of Canada you want to help build"], answer:3},
     {q:"Canada's history of Indigenous dispossession, Japanese-Canadian internment, and racial exclusion in immigration policy teaches ___.", options:["that Canada has always been perfect","that these were unavoidable","that only some Canadians are responsible for the past","that good intentions and democratic structures are not sufficient protection against injustice — active vigilance and institutional accountability are always needed"], answer:3},
     {q:"The most important thing young Canadians can do for democracy is ___.", options:["only vote when old enough","leave politics to older generations","remain politically uninformed","stay engaged, informed, and civically active throughout their lives — democracy atrophies without participation"], answer:3},
     {q:"Canada's commitment to diversity and human rights is ___.", options:["perfectly achieved","irrelevant to daily life","a fixed achievement that needs no further work","an ongoing aspiration that requires constant attention, especially as new communities arrive and old inequalities persist"], answer:3},
     {q:"My Canada is ___.", options:["already perfect","not my responsibility to improve","only for people born here","a work in progress — and you are part of its continuing story, with both the right and the responsibility to participate in shaping what it becomes"], answer:3}
   ]},
]},
{day:25, label:"Day 25 — Fri", subjects:[
  {subject:"English", title:"Language Conventions: Grammar for Academic Writing", summary:"Students master advanced grammar for academic writing: subordination, parallelism, active vs. passive voice, avoiding wordiness, and punctuation (semicolons, colons, dashes).",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A semicolon can join ___.", options:["a dependent and independent clause","any two phrases","two independent clauses that are closely related in meaning — stronger than a comma, weaker than a period","a list of only two items"], answer:2},
     {q:"A colon is used to ___.", options:["end a sentence","separate subjects from verbs","introduce a list, explanation, or quotation that follows a complete independent clause","before every quotation"], answer:2},
     {q:"An em dash (—) is used to ___.", options:["indicate a range of numbers","replace all commas","only in informal writing","add emphasis or set off supplementary information — it creates a stronger pause than commas and more informality than parentheses"], answer:3},
     {q:"Eliminating wordiness means ___.", options:["removing all adjectives","using simpler vocabulary","making essays shorter overall","removing unnecessary words without losing meaning: "due to the fact that" → "because""], answer:3},
     {q:"Parallelism errors in lists mean ___.", options:["the list has too many items","items are alphabetical","mixing grammatical forms: "She likes swimming, to run, and hikes" — all items must be in the same form: "swimming, running, and hiking"","the list is too long"], answer:2}
   ]},
  {subject:"Math", title:"Functions and Graphs: Transformations", summary:"Students apply transformations (stretch, compress, reflect, shift) to parent functions, building intuition for Grade 11 Functions.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The transformation y = f(x) + 3 shifts the graph ___.", options:["right 3 units","down 3 units","left 3 units","up 3 units"], answer:3},
     {q:"The transformation y = f(x − 2) shifts the graph ___.", options:["up 2 units","left 2 units","right 2 units — replacing x with (x − c) shifts the graph RIGHT by c","down 2 units"], answer:2},
     {q:"The transformation y = −f(x) ___.", options:["shifts the graph down","shifts the graph right","compresses the graph horizontally","reflects the graph over the x-axis (negates all y-values)"], answer:3},
     {q:"The transformation y = f(2x) ___.", options:["stretches horizontally by 2","shifts right by 2","reflects over the y-axis","compresses horizontally by a factor of 2 (each x-value is halved to get the same output)"], answer:3},
     {q:"The transformation y = 2f(x) ___.", options:["compresses vertically","stretches the graph horizontally","shifts up 2","stretches vertically by a factor of 2 (all y-values are doubled)"], answer:3}
   ]},
  {subject:"Science", title:"Biology: Human Reproduction and Development", summary:"Students examine human reproduction, the menstrual cycle, fertilisation, prenatal development, and related health topics.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Fertilisation occurs when ___.", options:["the ovum is released from the ovary","implantation occurs in the uterus","the embryo develops all its organs","a sperm cell penetrates the ovum, combining their 23 chromosomes each to form a 46-chromosome zygote"], answer:3},
     {q:"The placenta's function is ___.", options:["to produce eggs","to contract during birth","to produce testosterone","to exchange nutrients, oxygen, and waste between the mother's blood and the developing foetus without allowing blood to mix"], answer:3},
     {q:"Critical periods in prenatal development are important because ___.", options:["no time is more sensitive than another","the foetus cannot be harmed before birth","some developmental stages are irreversible","during specific windows, organ systems are developing and are especially vulnerable to damage from teratogens (alcohol, drugs, infections)"], answer:2},
     {q:"Hormones that regulate the menstrual cycle include ___.", options:["only oestrogen","only progesterone","adrenaline and cortisol","oestrogen, progesterone, FSH (follicle stimulating hormone), and LH (luteinising hormone) — working in a coordinated monthly feedback cycle"], answer:3},
     {q:"Reproductive health education is important because ___.", options:["it encourages sexual activity","it is only for biology class","it is unrelated to well-being","informed young people can make healthier decisions, understand their bodies, and recognise and respond to reproductive health issues effectively"], answer:3}
   ]},
  {subject:"History", title:"Media and History: How History is Represented", summary:"Students examine how films, television, novels, and social media represent historical events, and how to critically evaluate historical representation in popular media.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Historical films and television often ___.", options:["perfectly represent historical events","have no influence on public understanding of history","are always based entirely on primary sources","prioritise dramatic narrative over historical accuracy — compressing timelines, inventing dialogue, and simplifying complex events for entertainment purposes"], answer:3},
     {q:"The danger of Hollywood historical films is ___.", options:["they are too long","only that they use old footage","they are always good for education","they can shape public understanding of historical events more powerfully than academic history, potentially spreading inaccuracies, anachronisms, or ideological distortions at large scale"], answer:3},
     {q:"How should a historically literate person watch a historical film?", options:["Never watch historical films","Believe everything in the film","Only watch documentaries","Engage critically — enjoy the narrative while staying alert to what has been changed, simplified, or omitted, and consulting historical sources for the fuller picture"], answer:3},
     {q:"Social media's effect on historical memory includes ___.", options:["no significant effect","only preserving accurate history","replacing all other forms of historical knowledge","spreading both valuable grassroots history (family stories, community memory) and serious distortions (memes decontextualising events, conspiracy theories), making media literacy essential"], answer:3},
     {q:"The inclusion of diverse perspectives in historical representation in film and media ___.", options:["is always present","is not important","makes historical narratives less accurate","corrects the long dominance of perspectives from powerful groups and brings the experiences of women, Indigenous peoples, and marginalised communities into mainstream historical consciousness"], answer:3}
   ]},
]},
{day:26, label:"Day 26 — Mon", subjects:[
  {subject:"English", title:"Year-End Celebration: Reading and Writing Portfolio", summary:"Students curate and present a portfolio of their best reading and writing work from Grade 10, reflecting on their development.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A portfolio of best work shows ___.", options:["only your first piece","only your longest piece","only error-free work","a curated selection demonstrating the range and depth of your skills — showing growth, versatility, and your strongest analytical and creative moments"], answer:3},
     {q:"Selecting pieces for a portfolio involves ___.", options:["taking the highest-graded pieces only","random selection","choosing based on teacher preference","deliberate reflection: which pieces best demonstrate your analytical thinking, voice, and growth as a reader and writer"], answer:3},
     {q:"Writing a portfolio reflection means ___.", options:["listing your grades","only noting what you liked","summarising each piece","examining how your skills have developed, what you have learned about reading and writing, and what you want to improve in Grade 11"], answer:3},
     {q:"Sharing portfolio work with a peer or audience ___.", options:["only reveals weaknesses","is only for teachers to do","is inappropriate at high school level","makes writing purposeful and develops the communication skills of presenting your thinking to others — a skill for life beyond school"], answer:3},
     {q:"The most valuable thing in a writing portfolio is ___.", options:["the piece with the best grade","the longest essay","the piece with the most quotations","the piece that shows who you are as a thinker — your voice, your ideas, and your genuine engagement with literature and language"], answer:3}
   ]},
  {subject:"Math", title:"Looking Ahead: Grade 11 Mathematics Pathways", summary:"Students learn about the three Grade 11 math pathways — Functions (MCR3U), Functions and Applications (MCF3M), and Foundations for College (MBF3C) — and make informed choices.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"MCR3U (Grade 11 Functions) is the pathway for students planning ___.", options:["a direct path to the workforce","college-level programs not requiring advanced math","post-secondary programs requiring calculus or advanced math: university STEM, business, economics, or health science programs","all Grade 12 courses equally"], answer:2},
     {q:"Functions in Grade 11 extend Grade 10 quadratics to ___.", options:["linear equations only","polynomial, rational, exponential, and trigonometric functions — a significantly more abstract and rigorous treatment","geometry only","financial math only"], answer:1},
     {q:"Choosing a math pathway wisely requires ___.", options:["only considering current grade","following friends' choices","ignoring post-secondary plans","researching the prerequisites for programs you're interested in and honestly assessing your mathematical skills — changing pathways later is difficult"], answer:3},
     {q:"The most important preparation for Grade 11 Functions is ___.", options:["memorising all quadratic formulas","only practising graphing","avoiding all math over summer","solid understanding of Grade 10 quadratics, functions, and analytic geometry — the Grade 11 course assumes mastery of these topics from the start"], answer:3},
     {q:"Mathematics beyond high school is used in ___.", options:["only pure math careers","only engineering","only science","nearly every professional field: architecture, nursing, social science (statistics), finance, data analysis, education, and increasingly in arts and humanities through digital tools"], answer:3}
   ]},
  {subject:"Science", title:"Science: Looking Forward to Grade 11", summary:"Students preview Grade 11 science pathways — Biology, Chemistry, Physics — and understand how Grade 10 learning connects.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Grade 11 Biology extends Grade 10 knowledge of ___.", options:["only evolution","only cells","atomic theory","cellular processes, genetics, evolution, and ecosystems into greater depth — including animal and plant physiology, population ecology, and evolution through natural selection"], answer:3},
     {q:"Grade 11 Chemistry builds directly on ___.", options:["only physics concepts","only biology","no Grade 10 content","atomic theory, chemical bonding, and reaction types from Grade 10 — extending to stoichiometry (quantitative reactions), solution chemistry, and gas laws"], answer:2},
     {q:"Grade 11 Physics extends ___.", options:["only waves","only nuclear science","only optics from Grade 10","kinematics, forces, work and energy from Grade 10 into more complex motion (projectile, circular) and introduces electricity, waves, and modern physics in greater depth"], answer:3},
     {q:"All three Grade 11 sciences require ___.", options:["no mathematics","only memorisation","only writing skills","stronger mathematical skills than Grade 10 — especially algebra, significant figures, and graphing — as quantitative problem-solving becomes more central"], answer:3},
     {q:"Choosing Grade 11 sciences based on future interests means ___.", options:["taking all sciences always","taking no sciences","only choosing based on the teacher","considering whether you want to continue toward health sciences (biology + chemistry), engineering (physics + chemistry), environmental science (all three), or other pathways"], answer:3}
   ]},
  {subject:"History", title:"History Final Reflection: What Did We Learn?", summary:"Students write a final synthesis on the most significant lessons from Grade 10 History for their identity and future as Canadian citizens.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The most significant lesson from WWII for democratic citizens is ___.", options:["democracies always win wars","only military power matters","history has no lessons","even democratic societies can engage in serious injustices (internment, racism) — democratic structures do not automatically prevent human rights violations; active vigilance and rights protection are essential"], answer:3},
     {q:"The Charter of Rights and Freedoms matters to Grade 10 students because ___.", options:["it only applies to adults","only lawyers need to know it","it is already fully implemented","it protects your rights right now, and understanding it empowers you to recognise when your rights or others' rights are violated and to seek remedy"], answer:3},
     {q:"Reconciliation is a Grade 10 student's concern because ___.", options:["only the government can act on reconciliation","it was resolved by the TRC report","it is only a political issue","how your generation responds to the legacy of colonialism will determine whether the Calls to Action are implemented, and that response starts with education and empathy"], answer:3},
     {q:"The most important citizenship skill developed in Grade 10 History is ___.", options:["memorising dates","knowing all prime ministers","only understanding WWII","critical historical thinking — the ability to analyse competing claims, evaluate evidence, consider multiple perspectives, and form reasoned judgements about complex questions"], answer:3},
     {q:"Canada's history teaches that ___.", options:["Canada has always been just","change is impossible","history is irrelevant","the Canada we have was made by choices — and the better Canada we want requires your generation to make better choices, informed by honest understanding of both the achievements and the failures of our past"], answer:3}
   ]},
]},
{day:27, label:"Day 27 — Tue", subjects:[
  {subject:"English", title:"Media: Social Media and Identity", summary:"Students analyse how social media platforms construct and perform identity, and examine the mental health, social, and political implications.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Social media platforms are ___.", options:["neutral tools that reflect real life","always harmful","only entertainment","designed environments shaped by algorithmic choices, monetisation incentives, and design psychology — they actively shape how users present themselves and what they consume"], answer:3},
     {q:"The "performance of self" on social media means ___.", options:["social media shows the real you always","only celebrities perform identity online","everyone acts completely natural online","users actively curate and construct a version of themselves for an audience — social media identity is a performance, not a transparent window into the self"], answer:3},
     {q:"Algorithmic amplification can harm democratic discourse by ___.", options:["making politics too boring","spreading only factual content","limiting political discussion","creating filter bubbles, amplifying outrage and extreme content (since it drives engagement), and enabling the rapid spread of misinformation"], answer:3},
     {q:"Social media's mental health impacts on adolescents may include ___.", options:["no scientific evidence of any impact","only positive effects on wellbeing","stronger social connections for everyone","increased anxiety and depression linked to social comparison, cyberbullying, disrupted sleep, and the pursuit of validation through likes — though research shows complex, varied effects"], answer:3},
     {q:"Being a responsible social media user means ___.", options:["avoiding all social media","only using private accounts","sharing everything immediately without thinking","thinking critically about what you consume, being aware of how platforms manipulate you, respecting others' dignity online, and not sharing unverified information"], answer:3}
   ]},
  {subject:"Math", title:"Personal Finance: Practical Mathematics", summary:"Students apply math to real personal finance scenarios — tax filing, credit, mortgages, insurance — relevant to their near future.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A credit score measures ___.", options:["your income","how much money you have","your tax bracket","your creditworthiness — based on payment history, amount owed, length of credit history, and types of credit — used by lenders to decide whether to lend and at what rate"], answer:3},
     {q:"Compound interest on debt (like a credit card at 20% APR) is ___.", options:["beneficial to the borrower","easy to pay off","irrelevant if you make minimum payments","extremely expensive over time — minimum payments barely cover interest, so debt can grow exponentially if not paid down aggressively"], answer:3},
     {q:"A mortgage is ___.", options:["rent you pay to a landlord","a type of savings account","a government housing subsidy","a loan secured against property — usually for 25 years, where missing payments can result in losing your home"], answer:3},
     {q:"Filing an income tax return in Canada ___.", options:["is optional","only applies to people with high income","is required annually for all Canadians who earn income — and even those with low income should file to receive benefits and credits they are entitled to","can be done without any documentation"], answer:2},
     {q:"OSAP (Ontario Student Assistance Program) provides ___.", options:["employment","guaranteed employment after graduation","unlimited funding for any student","needs-based grants and loans to eligible post-secondary students to help cover tuition and living costs"], answer:3}
   ]},
  {subject:"Science", title:"Science: Environmental Decision Making", summary:"Students apply scientific knowledge to make and justify environmental decisions, practising evidence-based reasoning and ethical analysis.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A life cycle assessment (LCA) ___.", options:["only considers manufacturing cost","only measures CO₂","evaluates only the end-of-life disposal","examines the environmental impact of a product or service across its entire life: raw materials, manufacturing, transportation, use, and disposal — giving a complete picture of its environmental cost"], answer:3},
     {q:"Greenwashing refers to ___.", options:["genuine environmental improvement","government environmental regulation","reducing a company's carbon footprint","companies making misleading claims about their products' environmental benefits to attract eco-conscious consumers without making substantive changes"], answer:3},
     {q:"When evaluating an environmental policy proposal, you should consider ___.", options:["only economic costs","only environmental benefits","only public opinion","scientific effectiveness, economic costs and benefits, social equity (who bears costs and who benefits), technological feasibility, and political realities"], answer:3},
     {q:"The precautionary principle in environmental decisions means ___.", options:["wait for 100% certainty before acting","regulation is always wrong","industry self-regulation is sufficient","when scientific evidence suggests potential serious harm, take protective action even if full certainty has not yet been established"], answer:3},
     {q:"Effective environmental citizenship includes ___.", options:["only personal recycling","only political activism","ignoring environmental issues","a combination of personal choices (reducing consumption), political engagement (voting for climate action), and community action (supporting local environmental initiatives)"], answer:3}
   ]},
  {subject:"History", title:"Year-End Exam Preparation: Canadian History and Civics", summary:"Students review key concepts and practise historical thinking skills for assessment.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The most testable skill in Canadian history is ___.", options:["memorising dates and names","only knowing WWII","only understanding the Constitution","historical thinking — using concepts of significance, causation, continuity and change, perspective, evidence, and ethical judgement to analyse and interpret historical events and issues"], answer:3},
     {q:"When answering a source-analysis question in history, you should ___.", options:["copy the source text","describe what you see only","ignore the source's context","identify the source's origin (author, audience, purpose, date), analyse its content, evaluate its reliability and limitations, and connect it to your historical knowledge"], answer:3},
     {q:"A short analytical response in history should ___.", options:["list all the facts you know","avoid taking a position","be as long as possible","begin with a clear claim, support it with specific evidence, and explain the connection between evidence and claim — even a paragraph must have an argument"], answer:3},
     {q:"The connection between Canada's WWII home front and contemporary Canadian identity is ___.", options:["no connection","only about economics","only about military history","that the decisions made then — about women's roles, immigration, civil liberties, and social programs — directly shaped the Canada we live in today"], answer:3},
     {q:"In an exam essay on Canadian history, the most important first step is ___.", options:["writing as fast as possible","copying the question","writing your conclusion first","reading the question carefully and forming a clear, specific argument before writing — a minute of planning saves five minutes of aimless writing"], answer:3}
   ]},
]},
{day:28, label:"Day 28 — Wed", subjects:[
  {subject:"English", title:"Writing: Reflecting on Grade 10 English", summary:"Students write a final metacognitive reflection on their development as readers, writers, and thinkers in Grade 10.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Metacognitive reflection means ___.", options:["listing all the books read","summarising essay grades","only writing what you enjoyed","thinking carefully about your own learning process — how you have grown, what strategies work for you, and what skills you still want to develop"], answer:3},
     {q:"The most important growth in Grade 10 English is ___.", options:["vocabulary size","writing speed","perfect grammar","the development of analytical thinking — the ability to form, support, and communicate complex interpretive arguments about texts and ideas"], answer:3},
     {q:"Setting meaningful literacy goals for Grade 11 means ___.", options:["hoping things will be easier","picking goals your teacher suggested","avoiding challenging texts","identifying specific, realistic improvements in areas where you still struggle, and committing to the strategies that will get you there"], answer:3},
     {q:"Reading widely outside school hours ___.", options:["is less important than school reading","is only for pleasure and has no academic value","replaces school reading","builds background knowledge, vocabulary, and the habit of sustained attention that makes all academic reading easier and more rewarding"], answer:3},
     {q:"The most powerful thing writing can do is ___.", options:["earn good grades","fill required pages","meet word counts","make meaning — writing develops thought, communicates ideas, and connects human experiences across time and culture"], answer:3}
   ]},
  {subject:"Math", title:"Mathematics: Year-End Summary and Growth Reflection", summary:"Students reflect on their mathematical growth in Grade 10 and the role of mathematical thinking in their lives.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The key mathematical concept connecting all Grade 10 topics is ___.", options:["only algebra","only geometry","functions — the relationship between two quantities, expressed through equations, graphs, and tables, underlies quadratics, trig, analytic geometry, and data management","only trigonometry"], answer:2},
     {q:"Mathematical persistence means ___.", options:["getting every answer right immediately","only doing easy problems","giving up when confused","continuing to work on a challenging problem, trying different approaches, and learning from errors — the most important mathematical disposition"], answer:3},
     {q:"The connection between mathematics and other subjects in Grade 10 is ___.", options:["no connection exists","only through physics","only through economics","profound: history uses data analysis, science requires measurement and modelling, English benefits from logical argument, and economics uses functions and statistics"], answer:3},
     {q:"The biggest misconception about mathematics is ___.", options:["that it takes practice","that it requires thought","that it involves patterns","that some people are just "not math people" — mathematical skill is developed through practice and persistence, not a fixed innate ability"], answer:3},
     {q:"Grade 10 mathematics has prepared you for ___.", options:["nothing useful in life","only Grade 11 exams","only STEM careers","a wide range of future study and careers, but most importantly for logical, quantitative thinking — a fundamental skill for navigating a complex world full of data, models, and numerical claims"], answer:3}
   ]},
  {subject:"Science", title:"Science: Science and Society — A Final Reflection", summary:"Students reflect on the role of science in society and their responsibilities as scientifically literate citizens.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Scientific literacy means ___.", options:["knowing all scientific facts","only being good at labs","being a scientist","being able to read, understand, and critically evaluate scientific claims — distinguishing evidence-based science from pseudoscience, and understanding the nature and limits of scientific knowledge"], answer:3},
     {q:"The relationship between science and policy is ___.", options:["science automatically determines policy","scientists should make all decisions","science has no role in policy","complex — science provides evidence and analysis, but policy decisions also involve values, economics, and politics: science informs but does not determine policy"], answer:3},
     {q:"Anti-science sentiment (vaccine hesitancy, climate denial) is best addressed by ___.", options:["dismissing people who hold these views","only more data","making science optional","understanding its roots (distrust of institutions, misinformation, community identity) and engaging respectfully with evidence and transparent communication rather than dismissal"], answer:3},
     {q:"The most important scientific habit for a Grade 10 graduate to carry into adult life is ___.", options:["remembering the periodic table","knowing all physics formulas","being able to identify DNA bases","asking "what is the evidence?" — evaluating claims critically, distinguishing correlation from causation, and updating beliefs when evidence warrants"], answer:3},
     {q:"Science's greatest achievement is ___.", options:["only medicine","only technology","only the internet","the method itself — a self-correcting system of knowledge-building based on evidence, peer review, and revision, which has transformed human understanding and wellbeing despite being a very recent human invention"], answer:3}
   ]},
  {subject:"History", title:"Canada's Story: A Continuing Narrative", summary:"Students write a final historical essay on the most significant development in Canadian history and its relevance to their lives as future citizens.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's most significant unresolved historical challenge is ___.", options:["the 1867 Confederation debt","WWI conscription crisis","the implementation of Responsible Government","the relationship between the Canadian state and Indigenous peoples — a relationship marked by colonisation, dispossession, and injustice that requires ongoing reconciliation, not just acknowledgement"], answer:3},
     {q:"The Charter of Rights and Freedoms (1982) is significant because ___.", options:["it was Canada's first constitution","it only affects criminal law","it was only a ceremonial change","it transformed Canada into a rights-based constitutional democracy where courts can strike down laws that violate fundamental rights — a genuine revolution in the relationship between citizens and the state"], answer:3},
     {q:"Canada's identity as a "middle power" committed to multilateralism is ___.", options:["outdated in the 21st century","a permanent achievement","only relevant in foreign policy","a strategic choice that reflects both Canada's values and its interests — small enough to need international cooperation, influential enough to shape it"], answer:3},
     {q:"The most important historical lesson for Grade 10 students is ___.", options:["study hard for tests","grades matter most","history is boring","history is not about the past — it is the ongoing story of how human beings make choices about power, justice, and belonging, and your generation will be the authors of its next chapters"], answer:3},
     {q:"Completing Grade 10 History means ___.", options:["you now know everything about Canada","history class is finished","you can stop thinking about current events","you have developed the historical thinking skills to be a more engaged, critical, and responsible citizen — skills that matter every day, not just in exams"], answer:3}
   ]},
]},
{day:29, label:"Day 29 — Thu", subjects:[
  {subject:"English", title:"Exam Skills: The Unseen Poem", summary:"Students practise analysing an unseen poem under exam conditions — applying close reading, identifying form and content, and writing a focused analytical response.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Approaching an unseen poem for the first time, you should ___.", options:["write immediately","read only the first stanza","guess the theme from the title","read the entire poem at least twice: once for overall meaning and feeling, then again for specific craft choices to analyse"], answer:3},
     {q:"In an unseen poem analysis, you should prioritise ___.", options:["identifying the rhyme scheme before anything else","memorising all literary terms","proving you know many techniques","analysing HOW specific craft choices create meaning and effect — the technique is never the point; its effect is"], answer:3},
     {q:"If you are unsure of an image's meaning in an unseen poem, you should ___.", options:["skip it","say "I don't know"","look it up (in an exam, this isn't possible)","make a thoughtful, supported interpretation based on context — there is rarely only one correct reading, and a well-reasoned interpretation earns marks even if it differs from others"], answer:3},
     {q:"Time management for an unseen poem response (20 minutes) should be ___.", options:["all time writing","no planning","10 minutes reading/annotating, 2 minutes planning your thesis, 8 minutes writing — having a clear argument before writing saves time","15 minutes reading, 5 minutes writing"], answer:0},
     {q:"A strong response to an unseen poem ___.", options:["identifies every literary term","summarises the poem","avoids quoting the poem","makes an argument about how the poem creates meaning, supports it with specific quotation and analysis, and returns to the central argument in a conclusion"], answer:3}
   ]},
  {subject:"Math", title:"Exam Skills: Mathematical Problem Solving Strategies", summary:"Students practise multi-step problem solving strategies for exam conditions.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"When a math problem seems impossible, the best strategy is ___.", options:["leave it blank immediately","only try one approach","panic","write what you know: draw a diagram, define variables, write related formulas — starting the solution often reveals the path forward"], answer:3},
     {q:"Working backwards in a problem means ___.", options:["guessing the answer","only for simple problems","never used in real math","starting from what you want to find and determining what you would need to know — useful for complex problems where the path forward is unclear"], answer:3},
     {q:"Checking your answer in a word problem means ___.", options:["recalculating the same way","only for calculator problems","only checking arithmetic","substituting your answer back into the original problem context to verify it makes sense — does the answer answer the question asked? Is it a reasonable value?"], answer:3},
     {q:"Making an estimate before solving is useful because ___.", options:["it replaces the calculation","it is only for multiple choice","it takes too much time","it gives you a benchmark — if your calculation gives a very different answer from your estimate, that signals an error to find"], answer:3},
     {q:"The most important strategy for a difficult exam problem is ___.", options:["copying from a neighbour","skipping and never returning","showing partial work earns no marks","attempting every part and showing all work — partial marks for method are available even when the final answer is wrong"], answer:3}
   ]},
  {subject:"Science", title:"Science: Exam Preparation and Review", summary:"Students review key concepts from all three Grade 10 science strands for assessment readiness.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The difference between ionic and covalent bonding is ___.", options:["no difference","only in crystal structure","only in state at room temperature","ionic bonding involves electron transfer between a metal and non-metal forming ions; covalent bonding involves electron sharing between non-metals"], answer:3},
     {q:"Natural selection requires ___.", options:["directed change by an organism","a single generation to produce new species","no genetic variation","heritable variation within a population, differential reproductive success (some variants reproduce more), and inheritance of advantageous traits"], answer:3},
     {q:"Newton's Second Law (F = ma) means ___.", options:["only mass affects force","only acceleration matters","force and acceleration are unrelated","a net force on an object causes acceleration proportional to the force and inversely proportional to mass — doubling the force doubles the acceleration; doubling the mass halves it"], answer:3},
     {q:"pH 3 compared to pH 5 is ___.", options:["twice as acidic","no difference in acidity","ten times less acidic","one hundred times more acidic — because pH is a logarithmic scale, each unit represents a 10-fold change in H⁺ concentration"], answer:3},
     {q:"The conservation of energy means ___.", options:["energy is destroyed in friction","energy can be created in nuclear reactions","machines can exceed 100% efficiency","the total energy in a closed system remains constant — energy transforms between forms (kinetic to potential, chemical to thermal) but is neither created nor destroyed"], answer:3}
   ]},
  {subject:"History", title:"History Exam: Practise Essay", summary:"Students practise a 45-minute historical essay, applying all historical thinking skills to a significant Canadian history question.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"A strong history essay begins with ___.", options:["a question restated verbatim","a general statement about history","a list of facts","a clear, specific thesis that states your argument — not just the topic, but your interpretive claim about it"], answer:3},
     {q:"Historical evidence in an essay should ___.", options:["only come from memory","be as general as possible","include only dates","be specific: named people, events, dates, and details that directly support your analytical argument"], answer:3},
     {q:"Acknowledging historical complexity in an essay means ___.", options:["avoiding a clear argument","only presenting two sides","making no judgements","recognising that causes are multiple, perspectives differ, and outcomes are contested — and integrating this complexity into your argument rather than oversimplifying"], answer:3},
     {q:"The conclusion of a history essay should ___.", options:["introduce new evidence","restate only the facts","only repeat your thesis word for word","synthesise your argument, confirm your thesis has been proven, and extend to a broader significance — why does this matter beyond the specific question?"], answer:3},
     {q:"After writing a history essay under time pressure, you should ___.", options:["never reread your work","immediately submit without review","only check spelling","reread quickly for argument clarity, logical flow, and whether you actually answered the question asked — these are the most common exam errors"], answer:3}
   ]},
]},
{day:30, label:"Day 30 — Fri", subjects:[
  {subject:"English", title:"Year-End: English as a Lifelong Practice", summary:"A final celebration of reading, writing, and thinking. Students share work, set goals, and understand English as a practice they will carry into all areas of their lives.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Reading great literature develops ___.", options:["only vocabulary","only knowledge of plots","only grammar skills","empathy, critical thinking, historical and cultural awareness, and the capacity for sustained engagement with complex ideas — skills that transfer to every area of life"], answer:3},
     {q:"Writing is a thinking tool because ___.", options:["writing is only for communication","you think first, then write","writing and thinking are separate activities","the act of writing forces you to clarify, organise, and develop your thinking — ideas that seem clear in your head often reveal their gaps and complexities when you write them down"], answer:3},
     {q:"The texts you have studied in Grade 10 English ___.", options:["are now irrelevant to your life","only matter for literary study","have no connection to the real world","have expanded your understanding of human experience, your awareness of power and language, and your ability to engage critically with the world"], answer:3},
     {q:"Continuing to read widely beyond school ___.", options:["is optional and has no value","only applies to people in literature programs","replaces formal education","is one of the most powerful investments you can make in your intellectual and empathetic development — the lifelong reader is better equipped for almost everything"], answer:3},
     {q:"The most important thing you've learned in Grade 10 English is ___.", options:["how to avoid comma splices","the plot of every text","only Shakespeare's language","that language and story are not decorations on top of human experience — they are the medium through which we understand, make sense of, and share that experience"], answer:3}
   ]},
  {subject:"Math", title:"Grade 10 Math: Final Celebration and Reflection", summary:"A final review and reflection on mathematical growth, connecting the year's learning to lifelong mathematical thinking.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The most useful mathematical idea from Grade 10 for daily life is ___.", options:["the quadratic formula specifically","factoring polynomials","the Cosine Law","the concept of function — understanding relationships between variables — which underlies everything from budgeting to understanding health statistics to evaluating environmental claims"], answer:3},
     {q:"Mathematical confidence is built by ___.", options:["only solving easy problems","avoiding all challenging problems","only memorising formulas","working through difficulty, making mistakes, learning from them, and developing the persistence to try new approaches — not by only doing what already feels comfortable"], answer:3},
     {q:"Grade 10 math connects to citizenship through ___.", options:["no connection","only through science","only through engineering","the ability to understand and evaluate statistical claims in media, evaluate financial products, understand probability (in health and risk decisions), and interpret graphical data — mathematical literacy is civic literacy"], answer:3},
     {q:"The mathematical skill most undervalued by students is ___.", options:["computation speed","formula memorisation","the ability to perform operations","the ability to communicate mathematical reasoning clearly — being able to explain why a solution works is more valuable and harder than just finding the answer"], answer:3},
     {q:"Finishing Grade 10 Math means ___.", options:["you've learned all the math you'll ever need","math is finished for most of you","only engineers need to remember this","you've built a foundation — functions, geometry, data, and algebraic reasoning — that will serve you in whatever you do next, from everyday decisions to advanced study"], answer:3}
   ]},
  {subject:"Science", title:"Grade 10 Science: Final Synthesis", summary:"A final celebration of scientific learning and a look ahead to senior science and life as a scientifically literate citizen.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"The three Grade 10 science strands connect through ___.", options:["having nothing in common","only sharing lab equipment","only being about Canada","the fundamental idea that the world operates through consistent, discoverable principles — whether in the chemical behaviour of atoms, the evolution of life, or the motion of objects"], answer:3},
     {q:"Science is not a set of facts to memorise but ___.", options:["a way to pass tests","a collection of correct answers","only relevant for scientists","a method for building knowledge through observation, hypothesis, experimentation, and revision — the facts are important, but the method is more powerful"], answer:3},
     {q:"Being scientifically literate in the age of misinformation means ___.", options:["trusting all claims from scientists","trusting no online information","ignoring science in daily decisions","being able to evaluate claims critically: checking sources, looking for evidence, understanding the difference between correlation and causation, and recognising the provisional nature of scientific knowledge"], answer:3},
     {q:"The environmental challenges facing your generation ___.", options:["are already solved","only require technology","are someone else's problem","will require scientific knowledge to understand, technical innovation to address, political will to implement, and social change to sustain — and science literacy is the foundation of all of it"], answer:3},
     {q:"The greatest scientific frontier for your generation is ___.", options:["already fully mapped out","only space exploration","only artificial intelligence","genuinely unknown — questions about consciousness, quantum computing, the origins of life, dark matter, and the full potential of biotechnology remain open, and some of you may contribute to answering them"], answer:3}
   ]},
  {subject:"History", title:"Canada's Future: Your Role as a Citizen", summary:"A final reflection on Canadian history, citizenship, and the responsibilities of the Grade 10 generation.",
   resourceLabel:"TVO Learn: Grade 10", resourceUrl:"https://tvolearn.com/pages/grade-10",
   quiz:[
     {q:"Canada's most important strength as you enter adulthood is ___.", options:["its military power","only its natural resources","only its geography","its commitment — imperfect but genuine and ongoing — to democratic governance, human rights, diversity, and international cooperation: values worth defending and improving"], answer:3},
     {q:"The generation entering high school now will determine ___.", options:["nothing important about Canada's future","only their personal futures","only economic outcomes","whether reconciliation moves from aspiration to reality, whether Canada meets its climate commitments, and whether democracy remains a genuine tool for all Canadians or only for the privileged"], answer:3},
     {q:"Studying Canadian history has prepared you to ___.", options:["feel proud of everything Canada has done","feel ashamed of everything","ignore current events","engage more thoughtfully with current issues — recognising historical patterns, understanding how we got here, and taking seriously your role in shaping what comes next"], answer:3},
     {q:"The most important civic skill for your generation is ___.", options:["only voting","only protesting","only consuming news","critical thinking combined with civic engagement: being able to evaluate claims, understand systems, recognise injustice, and act purposefully — not just react — in the democratic spaces available to you"], answer:3},
     {q:"Canada's story is ___.", options:["finished","already told in full","only about the past","still being written — and you are not just a reader of this story, but one of its authors"], answer:3}
   ]},
]},
];

export default curriculum;