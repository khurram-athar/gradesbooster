#!/usr/bin/env python3
"""Phase 3: Grade 8, Days 41-50 (second Grade 8 batch, continuing the
10-day pattern). Topics chosen to avoid any overlap with the existing Day
1-40 set (see data/grade8.json after the Days 31-40 batch): tragic
heroes, systems by elimination, factoring trinomials, astrophysics,
CRISPR and gene editing, and further 20th-century Canadian history (the
Halifax Explosion, the Persons Case, the Avro Arrow, the White Paper of
1969, the Meech Lake and Charlottetown Accords, same-sex marriage
legalization, and recent reconciliation developments).

Grade 8's fourth subject key remains "History" (not "SocialStudies"),
consistent with the Days 31-40 batch and the pre-existing data/grade8.ts.

As with the earlier batches: videoUrl is intentionally left unset for
every subject -- fetch_video_ids.py fills these in automatically on its
next daily run. No embedded ASCII double-quote characters are used
anywhere in question/summary/option text; apostrophes use the curly
Unicode form (’) so they never collide with the single-quoted Python
string literals used here.
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-social-studies'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science & Technology',
    'TVO Learn: Grade 8 History',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L8, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M8, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S8, q)


def H(t, s, q):
    return sub('History', t, s, RH, H8, q)


g8_41_50 = [
day(41, [
L('Reading: Analyzing Tragic Heroes in Literature',
  'Grade 8 Reading strand: a tragic hero is a character with admirable qualities and a significant flaw, called a tragic flaw, that ultimately contributes to their downfall.',
  [('A tragic hero typically has ___.', ['Admirable qualities and a significant flaw', 'No notable qualities of any kind', 'A flaw with no effect on the story', 'Only negative traits with no strengths'], 0),
   ('A tragic flaw is best described as ___.', ['A significant weakness that contributes to the hero’s downfall', 'A strength that guarantees the hero’s success', 'A trait unrelated to the story’s outcome', 'A flaw that never affects the plot'], 0),
   ('Why might a tragic hero’s downfall create a powerful emotional impact for readers?', ['Readers may sympathize with a character who has both strengths and flaws', 'Downfalls have no emotional effect on readers', 'Tragic heroes never earn any sympathy from readers', 'A character with no flaws creates a more powerful impact'], 0),
   ('Which is an example of a possible tragic flaw?', ['Excessive pride leading to poor decisions', 'A character with no decisions to make', 'A strength that always leads to success', 'A trait unrelated to the character’s choices'], 0),
   ('Why is the tragic hero considered an important literary archetype?', ['It explores the complex relationship between human strengths and weaknesses', 'This archetype has no significance in literature', 'Tragic heroes never appear in significant works of literature', 'This concept has no connection to character development'], 0)]),
M('Solving Systems of Equations by Elimination',
  'Grade 8 Algebra strand: the elimination method solves a system of equations by adding or subtracting the equations to eliminate one variable, making it possible to solve for the other.',
  [('The elimination method involves ___.', ['Adding or subtracting equations to eliminate one variable', 'Only graphing both equations with no algebraic steps', 'Ignoring one of the two equations entirely', 'Substituting one equation directly into the other'], 0),
   ('Solve the system using elimination: x + y = 10 and x minus y = 2.', ['x = 6, y = 4', 'x = 4, y = 6', 'x = 8, y = 2', 'x = 5, y = 5'], 0),
   ('Why might elimination be a useful method when the coefficients of one variable are already opposites?', ['Adding the equations directly cancels out that variable', 'Elimination never works when coefficients are opposites', 'This situation requires substitution instead', 'Elimination can only be used with equations that have no variables'], 0),
   ('Solve the system using elimination: 2x + y = 11 and x minus y = 1.', ['x = 4, y = 3', 'x = 3, y = 4', 'x = 5, y = 1', 'x = 2, y = 7'], 0),
   ('After eliminating one variable and solving for the other, the next step is typically to ___.', ['Substitute that value back into one of the original equations', 'Stop, since only one variable ever needs to be found', 'Ignore the second variable completely', 'Start the entire process over with new equations'], 0)]),
Sc('Astrophysics: The Life Cycle of Stars',
   'Grade 8 Science Earth and Space Systems strand: stars go through a life cycle that includes formation from clouds of gas and dust, a stable main sequence phase, and an eventual dramatic ending, such as a supernova or collapse into a white dwarf.',
   [('Stars form from clouds of ___.', ['Gas and dust', 'Solid rock only', 'Pure water', 'Metal with no other elements'], 0),
    ('During the main sequence phase, a star ___.', ['Remains relatively stable, fusing hydrogen into helium', 'Immediately collapses with no stable phase', 'Stops producing any energy', 'Has no connection to nuclear fusion'], 0),
    ('A supernova is best described as ___.', ['A massive, dramatic explosion marking the end of certain stars’ life cycles', 'The very beginning of a star’s formation', 'A type of planet', 'An event unrelated to stars'], 0),
    ('A white dwarf is one possible remnant left behind after ___.', ['A star like our Sun exhausts its nuclear fuel', 'A star is first forming', 'A planet collides with an asteroid', 'A galaxy is first created'], 0),
    ('Why do astronomers study the life cycle of stars?', ['It helps explain the origins and eventual fates of stars, including our own Sun', 'Stars have no identifiable life cycle', 'This research has no scientific value', 'Studying star life cycles has no connection to astronomy'], 0)]),
H('The Halifax Explosion',
  'Grade 8 History strand: the Halifax Explosion of 1917, caused by a collision between two ships in Halifax Harbour, was one of the largest accidental explosions in history and had a devastating impact on the city.',
  [('The Halifax Explosion occurred in which year?', ['1867', '1917', '1945', '1970'], 1),
   ('The Halifax Explosion was caused by ___.', ['A collision between two ships in Halifax Harbour', 'A natural disaster unrelated to human activity', 'An event unrelated to Canadian history', 'A planned military attack'], 0),
   ('The Halifax Explosion is considered one of ___.', ['The largest accidental explosions in history', 'The smallest, least significant events in Canadian history', 'A minor event with no lasting impact', 'An event with no connection to Halifax'], 0),
   ('Why is the Halifax Explosion significant to Canadian history?', ['It caused devastating loss of life and property, prompting major relief and recovery efforts', 'It had no lasting impact on Halifax or Canada', 'This event never actually occurred', 'It has no connection to Canadian history'], 0),
   ('Why do historians study events like the Halifax Explosion?', ['They highlight both tragedy and the resilience and cooperation shown in recovery efforts', 'These events have no historical significance', 'Studying such events serves no educational purpose', 'This event has no connection to understanding Canadian history'], 0)])]),

day(42, [
L('Writing: The Persuasive Speech for a Formal Debate',
  'Grade 8 Writing strand: a persuasive speech for a formal debate presents a clear position on a topic, supported by structured arguments and evidence, while anticipating and addressing the opposing side.',
  [('A persuasive speech for a formal debate should present ___.', ['A clear position supported by structured arguments and evidence', 'No clear position at all', 'Only the speaker’s personal preferences with no evidence', 'A summary with no argument'], 0),
   ('Why is it important to anticipate the opposing side’s arguments in a debate speech?', ['It allows the speaker to prepare effective responses and strengthen their position', 'Anticipating opposing arguments always weakens a debate speech', 'Debate speeches should never consider the opposing side', 'This preparation has no strategic value'], 0),
   ('Which is an example of a structured argument in a debate speech?', ['A clear claim supported by specific evidence and reasoning', 'A vague statement with no supporting evidence', 'An argument unrelated to the debate topic', 'A statement with no clear position'], 0),
   ('Why might a debate speech use confident, clear delivery in addition to strong content?', ['Delivery can affect how persuasive and credible the argument seems to an audience', 'Delivery has no effect on how a speech is received', 'Content is the only factor that matters in a debate', 'Confidence has no connection to persuasion'], 0),
   ('A strong conclusion in a debate speech should ___.', ['Reinforce the speaker’s position and its key supporting points', 'Introduce a brand new, unrelated topic', 'Contain no connection to the rest of the speech', 'Undermine the speaker’s own argument'], 0)]),
M('Solving for Missing Sides and Angles Using Trigonometry',
  'Grade 8 Geometry strand (pre-high-school extension): applying the trigonometric ratios sine, cosine, and tangent allows you to solve for unknown side lengths or angles in a right triangle when other measurements are known.',
  [('If you know an angle and the hypotenuse of a right triangle, which ratio could help you find the opposite side?', ['Sine', 'A ratio unrelated to trigonometry', 'Only the Pythagorean theorem, with no trigonometry involved', 'None of the trigonometric ratios apply here'], 0),
   ('If you know the adjacent and opposite sides of a right triangle, which ratio could help you find the angle?', ['Tangent', 'A method unrelated to trigonometry', 'Only the circumference formula', 'The volume formula'], 0),
   ('To find a missing angle using a known ratio of sides, you would typically use ___.', ['The inverse trigonometric function (such as inverse tangent)', 'Only addition, with no trigonometry involved', 'A method with no connection to trigonometric ratios', 'The Pythagorean theorem exclusively'], 0),
   ('If the opposite side is 5 and the hypotenuse is 10 in a right triangle, what is the sine of the angle?', ['0.5', '2', '5', '10'], 0),
   ('Why are trigonometric ratios useful for solving real-world problems, such as finding the height of a building using an angle of elevation?', ['They relate angles to side length ratios, allowing indirect calculation of unknown measurements', 'Trigonometric ratios have no real-world applications', 'These ratios only apply to shapes with no angles', 'This method requires physically measuring every side directly'], 0)]),
Sc('Materials Science: Polymers and Composites',
   'Grade 8 Science Matter and Energy strand: polymers are large molecules made of repeating units, while composites combine two or more different materials to create a substance with enhanced properties.',
   [('A polymer is best described as ___.', ['A large molecule made of repeating units', 'A single, simple atom', 'A material with no molecular structure', 'A type of pure element only'], 0),
    ('A composite material is formed by ___.', ['Combining two or more different materials', 'Using only a single, unmixed material', 'Removing all materials from a substance', 'A process unrelated to material combination'], 0),
    ('Which is an example of a polymer?', ['Plastic', 'Pure gold', 'Pure oxygen gas', 'A single water molecule'], 0),
    ('Why might engineers use composite materials instead of a single material?', ['Composites can combine the beneficial properties of multiple materials', 'Composites always have worse properties than single materials', 'Combining materials has no effect on their properties', 'Composite materials are never used in real engineering'], 0),
    ('Which is an example of a composite material used in construction or manufacturing?', ['Reinforced concrete, combining concrete and steel', 'Pure water with no other materials', 'A single element with no combination involved', 'Air with no other substances mixed in'], 0)]),
H('The Persons Case and Legal Rights for Women',
  'Grade 8 History strand: the Persons Case of 1929 was a landmark legal decision that established that women in Canada were legally considered persons eligible to be appointed to the Senate, expanding women’s legal rights.',
  [('The Persons Case was decided in which year?', ['1867', '1918', '1929', '1982'], 2),
   ('The Persons Case established that women in Canada were legally considered ___.', ['Persons eligible to be appointed to the Senate', 'Ineligible for any legal rights', 'Excluded from all legal recognition', 'A group with no connection to Canadian law'], 0),
   ('The Persons Case is considered a landmark decision because it ___.', ['Expanded legal rights for women in Canada', 'Reduced legal rights for women', 'Had no effect on Canadian law', 'Was unrelated to women’s legal status'], 0),
   ('The group of women who advocated for this legal change are often referred to as ___.', ['The Famous Five', 'A group unrelated to Canadian history', 'A modern advocacy organization', 'A group with no historical significance'], 0),
   ('Why is the Persons Case still studied as part of Canadian history today?', ['It represents a significant milestone in the advancement of women’s legal rights', 'It has no lasting significance in Canadian history', 'This case never actually took place', 'It has no connection to legal rights in Canada'], 0)])]),

day(43, [
L('Grammar: Parallelism and Sentence Balance',
  'Grade 8 Writing strand: parallelism means using a consistent grammatical structure for related ideas in a sentence, which creates balance, rhythm, and clarity in writing.',
  [('Parallelism in writing means ___.', ['Using a consistent grammatical structure for related ideas', 'Using different grammatical structures for every related idea', 'Avoiding lists entirely in writing', 'Using only single-word sentences'], 0),
   ('Which sentence demonstrates correct parallelism?', ['She enjoys hiking, swimming, and biking.', 'She enjoys hiking, swimming, and to bike.', 'She enjoys to hike, swimming, and biking.', 'She enjoys hiking, to swim, and biking.'], 0),
   ('Why is parallel structure valuable in writing?', ['It creates clarity, balance, and rhythm in sentences', 'It makes sentences more confusing to read', 'Parallel structure has no effect on writing quality', 'It should always be avoided in formal writing'], 0),
   ('Which sentence lacks parallel structure?', ['He likes reading, writing, and painting.', 'He likes to read, writing, and painting.', 'Reading, writing, and painting are his interests.', 'He enjoys reading, writing, and painting daily.'], 1),
   ('Parallelism is especially useful when writing ___.', ['A list of related items or actions', 'A single isolated word', 'Random unrelated ideas with no structure', 'A sentence containing no verbs'], 0)]),
M('Factoring Trinomials',
  'Grade 8 Algebra strand (pre-high-school extension): factoring a trinomial, such as x squared plus 5x plus 6, involves finding two binomials that multiply together to produce the original expression.',
  [('Factor: x squared plus 5x plus 6.', ['(x + 2)(x + 3)', '(x + 1)(x + 6)', '(x + 5)(x + 1)', '(x + 6)(x + 6)'], 0),
   ('Factor: x squared plus 7x plus 12.', ['(x + 3)(x + 4)', '(x + 2)(x + 6)', '(x + 1)(x + 12)', '(x + 7)(x + 5)'], 0),
   ('When factoring a trinomial like x squared plus bx plus c, you look for two numbers that ___.', ['Multiply to give c and add to give b', 'Multiply to give b and add to give c', 'Are always equal to each other', 'Have no relationship to b or c'], 0),
   ('Factor: x squared plus 9x plus 20.', ['(x + 4)(x + 5)', '(x + 2)(x + 10)', '(x + 1)(x + 20)', '(x + 9)(x + 11)'], 0),
   ('Why is factoring trinomials a useful algebraic skill?', ['It can help solve quadratic equations and simplify expressions', 'Factoring has no practical use in algebra', 'Trinomials can never be factored', 'This skill only applies to linear equations'], 0)]),
Sc('Environmental Science: Ocean Acidification',
   'Grade 8 Science Earth and Space Systems strand: ocean acidification occurs when the ocean absorbs excess carbon dioxide from the atmosphere, lowering its pH and posing risks to marine life, especially shell-forming organisms.',
   [('Ocean acidification occurs when the ocean absorbs excess ___.', ['Carbon dioxide from the atmosphere', 'Oxygen only', 'Nitrogen only', 'Helium'], 0),
    ('Ocean acidification results in a ___ ocean pH.', ['Lower', 'Higher', 'Completely unchanged', 'Unrelated to carbon dioxide levels'], 0),
    ('Which type of marine organism is especially at risk from ocean acidification?', ['Shell-forming organisms, like coral and shellfish', 'Organisms with no connection to ocean chemistry', 'Only organisms living entirely on land', 'Organisms unaffected by any pH changes'], 0),
    ('Why might rising carbon dioxide emissions contribute to ocean acidification?', ['Increased atmospheric carbon dioxide leads to more being absorbed by ocean water', 'Carbon dioxide emissions have no connection to ocean chemistry', 'The ocean never absorbs any atmospheric gases', 'Ocean pH is entirely unrelated to atmospheric conditions'], 0),
    ('Why is ocean acidification considered an important environmental issue?', ['It can significantly disrupt marine ecosystems and the organisms that depend on them', 'Ocean acidification has no effect on marine life', 'This issue has no connection to environmental science', 'Marine ecosystems are unaffected by changes in ocean chemistry'], 0)]),
H('Canada’s Response to the Holocaust',
  'Grade 8 History strand: Canada’s immigration policies during the Holocaust era were notably restrictive toward Jewish refugees, a historical decision that is now widely studied and critically examined.',
  [('During the Holocaust era, Canada’s immigration policies toward Jewish refugees were generally ___.', ['Restrictive', 'Fully open with no restrictions', 'Unrelated to immigration policy', 'Identical to policies from a completely different era'], 0),
   ('Canada’s restrictive immigration policies during this period are now ___.', ['Widely studied and critically examined', 'Considered to have no historical significance', 'Viewed as having no lasting impact on historical understanding', 'Entirely forgotten with no historical record'], 0),
   ('Why do historians study Canada’s response to the Holocaust?', ['To understand and reflect on historical decisions and their consequences', 'This response has no relevance to Canadian history', 'Canada had no immigration policy during this era', 'This topic has no connection to historical study'], 0),
   ('Why might reflecting on past immigration policies be valuable for understanding present-day decisions?', ['It can offer insight into the impact of policy choices on vulnerable populations', 'Past policies have no connection to present-day decision-making', 'Historical reflection serves no useful purpose', 'Immigration policy has never changed throughout history'], 0),
   ('Why is Canada’s response to the Holocaust considered an important part of history education?', ['It encourages critical reflection on the consequences of restrictive policies', 'This topic has no educational value', 'It has no connection to understanding history', 'Canada’s role during this period should not be studied'], 0)])]),

day(44, [
L('Vocabulary: Jargon and Technical Language Across Fields',
  'Grade 8 Language strand: jargon refers to specialized vocabulary used within a specific field or profession, and understanding it is important for reading texts related to that field accurately.',
  [('Jargon refers to ___.', ['Specialized vocabulary used within a specific field', 'Vocabulary used only in casual conversation', 'Words with no specific meaning', 'Vocabulary that never appears in professional writing'], 0),
   ('Why might jargon be difficult for someone outside a particular field to understand?', ['It often has specific meanings understood mainly by people within that field', 'Jargon is always easy for everyone to understand immediately', 'Jargon never appears in professional or technical writing', 'Specialized vocabulary has no connection to a particular field'], 0),
   ('Which is an example of medical jargon?', ['Diagnosis', 'Happy', 'Quickly', 'Nice'], 0),
   ('Why might a writer explain jargon when writing for a general audience?', ['To help readers unfamiliar with the field understand the content', 'Jargon should never be explained under any circumstances', 'General audiences always understand specialized vocabulary automatically', 'Explaining jargon makes writing less clear'], 0),
   ('Understanding jargon across different fields can help readers ___.', ['Better comprehend texts related to specific subjects or professions', 'Avoid reading any technical texts', 'Ignore the meaning of specialized vocabulary', 'Understand only casual, everyday conversation'], 0)]),
M('Correlation vs. Causation in Data',
  'Grade 8 Data Management strand: correlation describes a relationship between two variables, while causation means one variable directly causes a change in another -- correlation alone does not prove causation.',
  [('Correlation between two variables means ___.', ['They tend to change together in some observable pattern', 'One variable definitely causes the other to change', 'The variables have no relationship at all', 'The variables are always identical'], 0),
   ('Causation means ___.', ['One variable directly causes a change in another', 'Two variables happen to change together with no direct link', 'Variables can never influence each other', 'A relationship that has no real-world significance'], 0),
   ('Why is it important to remember that correlation does not necessarily imply causation?', ['Two variables might be related without one actually causing the other', 'Correlation and causation always mean exactly the same thing', 'Causation can be assumed whenever a correlation exists', 'This distinction has no relevance to interpreting data'], 0),
   ('Which is an example of correlation without necessarily indicating causation?', ['Ice cream sales and swimming pool visits both increasing in summer', 'A plant growing because it was watered', 'A car stopping because the brakes were applied', 'A light turning on because a switch was flipped'], 0),
   ('Why should researchers be cautious about claiming causation based only on correlated data?', ['Other factors might explain the relationship, requiring further investigation', 'Correlation always proves causation with no further investigation needed', 'Causation is irrelevant to interpreting any data', 'Researchers should never analyze relationships between variables'], 0)]),
Sc('Biotechnology: CRISPR and Gene Editing',
   'Grade 8 Science Life Systems strand: CRISPR is a gene-editing technology that allows scientists to make precise changes to DNA, with significant potential applications and ethical considerations in medicine and agriculture.',
   [('CRISPR is a technology used to ___.', ['Make precise changes to DNA', 'Measure the size of a cell', 'Predict weather patterns', 'Study the movement of tectonic plates'], 0),
    ('CRISPR has potential applications in fields such as ___.', ['Medicine and agriculture', 'Fields with no connection to biology', 'Only entertainment technology', 'A single, unrelated area of study'], 0),
    ('Why does gene editing technology like CRISPR raise ethical considerations?', ['It has the potential to significantly alter living organisms, raising questions about appropriate use', 'Gene editing has no ethical implications at all', 'CRISPR has no connection to living organisms', 'Ethical considerations are irrelevant to scientific research'], 0),
    ('Which is a potential application of CRISPR in agriculture?', ['Developing crops with improved resistance to disease', 'A use unrelated to farming or crops', 'An application with no connection to agriculture', 'A technology that cannot be applied to plants'], 0),
    ('Why is CRISPR considered a significant advancement in biotechnology?', ['It allows for much more precise and efficient gene editing than earlier methods', 'It has no advantages over earlier gene-editing methods', 'Gene editing technology has no scientific significance', 'CRISPR cannot be used to edit genes at all'], 0)]),
H('The Avro Arrow and Canadian Sovereignty',
  'Grade 8 History strand: the Avro Arrow was an advanced Canadian-designed fighter jet whose cancellation in 1959 sparked ongoing debate about Canadian technological independence and sovereignty.',
  [('The Avro Arrow was a Canadian-designed ___.', ['Fighter jet', 'Passenger train', 'Naval ship', 'Space shuttle'], 0),
   ('The Avro Arrow project was cancelled in which year?', ['1931', '1945', '1959', '1982'], 2),
   ('The cancellation of the Avro Arrow sparked debate about ___.', ['Canadian technological independence and sovereignty', 'A topic unrelated to Canadian history', 'An issue with no lasting significance', 'A decision with no public reaction'], 0),
   ('Why is the Avro Arrow still discussed in Canadian history today?', ['It raises ongoing questions about Canada’s role in advanced technology and defence', 'It has no connection to Canadian technological history', 'The Avro Arrow project never actually existed', 'This topic has no relevance to Canadian sovereignty'], 0),
   ('Why might the cancellation of a major technological project like the Avro Arrow be historically significant?', ['It can reflect broader decisions about a country’s economic and technological priorities', 'Cancelled projects have no historical significance', 'This event has no connection to Canadian identity', 'Technological projects never involve important policy decisions'], 0)])]),

day(45, [
L('Reading: Analyzing Historical Fiction',
  'Grade 8 Reading strand: historical fiction blends real historical settings and events with fictional characters and plots, and analyzing it involves distinguishing between factual and imagined elements.',
  [('Historical fiction combines ___.', ['Real historical settings or events with fictional characters and plots', 'Only completely factual accounts with no fictional elements', 'Only fictional worlds with no historical basis at all', 'Elements unrelated to any real time period'], 0),
   ('When analyzing historical fiction, readers should consider ___.', ['Which elements are historically accurate and which are fictional', 'Only the fictional elements, ignoring history entirely', 'Only the historical facts, with no attention to the story', 'Nothing related to accuracy or fiction'], 0),
   ('Why might an author choose historical fiction to explore a real historical period?', ['It allows readers to engage emotionally with history through relatable characters and stories', 'Historical fiction always distorts historical understanding', 'This genre has no educational value', 'Fiction removes any connection to real history'], 0),
   ('Which is an example of a historically accurate element that might appear in historical fiction?', ['A real historical event or setting used as the story’s backdrop', 'A completely fictional planet with no historical basis', 'An event that never occurred in any time period', 'A setting unrelated to any real historical era'], 0),
   ('Why is it important for readers to recognize the fictional elements within historical fiction?', ['To avoid mistaking invented details for verified historical facts', 'Fictional elements are never present in historical fiction', 'All details in historical fiction are always completely accurate', 'This distinction has no importance for readers'], 0)]),
M('Introduction to Modular Arithmetic',
  'Grade 8 Number strand (pre-high-school extension): modular arithmetic involves working with remainders after division, often used in real-world contexts like telling time on a 12-hour clock.',
  [('Modular arithmetic focuses on ___.', ['The remainder after division', 'Only whole numbers with no remainders', 'A concept unrelated to division', 'Ignoring division entirely'], 0),
   ('On a 12-hour clock, 15 o’clock would correspond to which hour, using modular arithmetic?', ['3 o’clock', '15 o’clock exactly, with no adjustment', '12 o’clock', '5 o’clock'], 0),
   ('What is 17 mod 5 (the remainder when 17 is divided by 5)?', ['2', '3', '5', '12'], 0),
   ('Why is modular arithmetic useful for understanding clocks and calendars?', ['These systems repeat in cycles, similar to how remainders repeat in modular arithmetic', 'Clocks and calendars have no connection to remainders', 'Modular arithmetic has no real-world applications', 'Time never involves any repeating patterns'], 0),
   ('What is 22 mod 7 (the remainder when 22 is divided by 7)?', ['1', '3', '7', '22'], 0)]),
Sc('Forensic Science: Applying Scientific Methods to Investigation',
   'Grade 8 Science Inquiry strand: forensic science applies scientific methods and evidence analysis, such as fingerprinting or chemical testing, to investigate crimes and support legal processes.',
   [('Forensic science applies scientific methods to ___.', ['Investigate crimes and support legal processes', 'A field entirely unrelated to investigation', 'Only artistic creation, with no connection to science', 'Predicting weather patterns'], 0),
    ('Which is an example of evidence forensic scientists might analyze?', ['Fingerprints', 'A completely unrelated object with no connection to an investigation', 'Nothing at all, since forensic science analyzes no physical evidence', 'Only witness opinions, with no physical evidence'], 0),
    ('Why is following a careful, systematic scientific method important in forensic investigations?', ['It helps ensure evidence is reliable and conclusions are well-supported', 'A systematic method has no importance in forensic science', 'Forensic evidence never needs careful analysis', 'Scientific methods have no connection to legal investigations'], 0),
    ('Chemical testing in forensic science might be used to ___.', ['Identify unknown substances found at a scene', 'Have no connection to identifying substances', 'Replace the need for any physical evidence', 'Determine weather conditions only'], 0),
    ('Why is forensic science considered an interdisciplinary field?', ['It combines knowledge from biology, chemistry, and other sciences with investigative processes', 'It relies on a single area of science with no other connections', 'Forensic science has no connection to other scientific fields', 'This field only involves legal knowledge, with no science involved'], 0)]),
H('The White Paper of 1969 and Indigenous Resistance',
  'Grade 8 History strand: the White Paper of 1969 was a federal government policy proposal that would have eliminated the Indian Act and Indigenous legal status, but was withdrawn after strong resistance from First Nations communities.',
  [('The White Paper was proposed in which year?', ['1931', '1969', '1982', '2000'], 1),
   ('The White Paper of 1969 proposed to ___.', ['Eliminate the Indian Act and Indigenous legal status', 'Strengthen Indigenous rights significantly', 'Have no effect on existing policy', 'Expand Indigenous self-government immediately'], 0),
   ('The White Paper was ultimately withdrawn due to ___.', ['Strong resistance from First Nations communities', 'Widespread support from all communities involved', 'No opposition of any kind', 'A decision unrelated to Indigenous concerns'], 0),
   ('Why is the White Paper of 1969 considered an important moment in Indigenous political history?', ['It sparked significant organized Indigenous political activism in response', 'It had no effect on Indigenous political organizing', 'This proposal was never actually made', 'It has no connection to Indigenous rights movements'], 0),
   ('Why do historians study the resistance to the White Paper?', ['It illustrates the strength and impact of Indigenous political advocacy', 'This resistance has no historical significance', 'Indigenous communities had no response to this proposal', 'This event has no connection to Canadian history'], 0)])]),

day(46, [
L('Writing: The Multi-Genre Project',
  'Grade 8 Writing strand: a multi-genre project explores a single topic through multiple forms of writing, such as poetry, a letter, and a news article, allowing for varied perspectives and creative expression.',
  [('A multi-genre project explores a single topic through ___.', ['Multiple forms of writing', 'Only a single form of writing', 'No structured writing at all', 'A topic with no connection between the pieces'], 0),
   ('Which is an example of combining genres in a multi-genre project about a historical event?', ['Writing a poem, a letter, and a news article about the same event', 'Writing only one essay with no variation in form', 'Ignoring the historical event entirely', 'Copying text from a single unrelated source'], 0),
   ('Why might a multi-genre project offer a richer understanding of a topic than a single essay?', ['Different genres can highlight different perspectives and emotional dimensions of the topic', 'Multiple genres always make a topic more confusing', 'A single essay always provides a more complete understanding', 'Genre variety has no effect on how a topic is understood'], 0),
   ('A multi-genre project requires writers to consider ___.', ['How each genre’s conventions shape the presentation of the topic', 'Nothing related to differences between genres', 'Only one single writing style throughout', 'A topic with no coherent connections between pieces'], 0),
   ('Why might a multi-genre project be considered a creative writing challenge?', ['It requires adapting tone, structure, and style across multiple different forms of writing', 'It only requires writing in a single form with no variation', 'Multi-genre projects require no creative thinking', 'This type of project has no connection to different writing conventions'], 0)]),
M('Introduction to the Quadratic Formula',
  'Grade 8 Algebra strand (pre-high-school extension): the quadratic formula, x equals negative b plus or minus the square root of b squared minus 4ac all over 2a, can be used to solve any quadratic equation in the form ax squared plus bx plus c equals zero.',
  [('The quadratic formula is used to solve equations in the form ___.', ['ax squared plus bx plus c equals zero', 'ax plus b equals zero', 'a plus b equals c', 'a divided by b equals c'], 0),
   ('In the quadratic formula, which symbol represents the coefficient of the x squared term?', ['a', 'b', 'c', 'x'], 0),
   ('The quadratic formula includes a square root of ___.', ['b squared minus 4ac', 'a squared plus b squared', 'c squared minus a', 'b plus c'], 0),
   ('Why is the quadratic formula considered a powerful tool in algebra?', ['It can solve any quadratic equation, even ones that are difficult to factor', 'It can only be used with equations that are already factored', 'The quadratic formula has no practical use in algebra', 'It only works for linear equations, not quadratics'], 0),
   ('For the equation x squared plus 3x plus 2 equals zero, what are the values of a, b, and c?', ['a = 1, b = 3, c = 2', 'a = 3, b = 2, c = 1', 'a = 2, b = 1, c = 3', 'a = 1, b = 2, c = 3'], 0)]),
Sc('Meteorology: Predicting Severe Weather',
   'Grade 8 Science Earth and Space Systems strand: meteorologists use data from radar, satellites, and weather models to predict severe weather events, such as tornadoes and hurricanes, helping communities prepare in advance.',
   [('Meteorologists use tools such as ___ to help predict severe weather.', ['Radar and satellites', 'Only guesswork with no data', 'A single unrelated tool with no connection to weather', 'Tools that provide no useful information'], 0),
    ('Predicting severe weather events, like hurricanes, helps communities ___.', ['Prepare in advance to reduce risk', 'Have no ability to prepare for danger', 'Ignore all warnings about severe weather', 'Avoid using any weather-related data'], 0),
    ('A weather model is used to ___.', ['Simulate and forecast future weather conditions', 'Have no connection to forecasting', 'Replace the need for any weather data', 'Predict only past weather events'], 0),
    ('Why is early warning important when severe weather, like a tornado, is predicted?', ['It can give people time to take safety precautions', 'Early warnings have no benefit for community safety', 'Severe weather events cannot be predicted in advance', 'Preparation has no connection to severe weather warnings'], 0),
    ('Why is meteorology considered a valuable scientific field?', ['It helps communities understand and prepare for potentially dangerous weather conditions', 'Meteorology has no real-world benefits', 'Weather prediction has no scientific basis', 'This field has no connection to public safety'], 0)]),
H('The Meech Lake and Charlottetown Accords',
  'Grade 8 History strand: the Meech Lake Accord and Charlottetown Accord were failed attempts in the late 1980s and early 1990s to amend Canada’s constitution and address Quebec’s status within Confederation.',
  [('The Meech Lake Accord and Charlottetown Accord were attempts to ___.', ['Amend Canada’s constitution', 'Eliminate Canada’s constitution entirely', 'Create an entirely new country', 'Address issues unrelated to Canadian government'], 0),
   ('These accords were significantly focused on addressing ___.', ['Quebec’s status within Confederation', 'A topic with no connection to Canadian federalism', 'Issues unrelated to Canadian unity', 'A matter unrelated to constitutional change'], 0),
   ('Both the Meech Lake Accord and Charlottetown Accord ultimately ___.', ['Failed to be ratified', 'Were immediately successful with no challenges', 'Had no connection to Canadian politics', 'Were never actually proposed'], 0),
   ('Why are these accords significant to the study of Canadian federalism?', ['They reflect ongoing challenges in balancing regional and national interests within Canada', 'They have no connection to Canadian federalism', 'These accords never actually existed', 'This topic has no relevance to understanding Canadian government'], 0),
   ('Why might failed constitutional negotiations still be historically significant?', ['They reveal important tensions and priorities within a country’s political system', 'Failed negotiations have no historical value', 'Only successful agreements are ever studied in history', 'This topic has no connection to understanding Canadian unity'], 0)])]),

day(47, [
L('Media Literacy: Analyzing Political Cartoons',
  'Grade 8 Media Literacy strand: political cartoons use symbolism, exaggeration, and humour to comment on political or social issues, requiring readers to interpret visual and textual clues to understand the message.',
  [('Political cartoons often use ___ to comment on issues.', ['Symbolism, exaggeration, and humour', 'Only plain, literal illustrations with no deeper meaning', 'No visual elements at all', 'Text with no visual component'], 0),
   ('Why might a political cartoonist use exaggeration in their work?', ['To emphasize a point or draw attention to a particular issue', 'Exaggeration always removes meaning from a cartoon', 'Political cartoons never use exaggeration', 'This technique has no persuasive purpose'], 0),
   ('Interpreting a political cartoon often requires readers to ___.', ['Analyze both the visual symbols and any accompanying text', 'Ignore all visual elements completely', 'Focus only on the cartoon’s colours', 'Avoid considering the cartoon’s intended message'], 0),
   ('Symbolism in a political cartoon might involve using ___.', ['A specific image to represent a larger idea or group', 'Only random, meaningless images', 'No connection between images and ideas', 'Images unrelated to any political or social issue'], 0),
   ('Why are political cartoons considered a valuable historical and media literacy resource?', ['They offer insight into public opinion and commentary on issues from a specific time period', 'Political cartoons provide no historical insight', 'These cartoons have no connection to public opinion', 'This type of media has no educational value'], 0)]),
M('Precision and Significant Figures in Measurement',
  'Grade 8 Measurement strand: significant figures indicate the precision of a measurement, and understanding them helps ensure calculations reflect an appropriate and honest level of accuracy.',
  [('Significant figures indicate ___.', ['The precision of a measurement', 'The exact colour of a measured object', 'A number with no connection to measurement', 'Only whole numbers with no decimals'], 0),
   ('In the measurement 3.20 cm, how many significant figures are there?', ['One', 'Two', 'Three', 'Four'], 2),
   ('Why is it important to consider significant figures when reporting a measurement?', ['It reflects the actual precision of the measuring tool or method used', 'Significant figures have no connection to measurement accuracy', 'Reporting extra digits always makes a measurement more accurate', 'Precision has no relevance to scientific measurement'], 0),
   ('If a measurement is recorded with too many digits beyond the precision of the tool used, it may ___.', ['Falsely suggest a level of accuracy that was not actually achieved', 'Always be considered more accurate than necessary', 'Have no effect on how the measurement is interpreted', 'Improve the actual precision of the measurement'], 0),
   ('Why might scientists pay close attention to significant figures in their calculations?', ['To ensure their results honestly reflect the precision of their original data', 'Significant figures have no role in scientific calculations', 'Precision is never a consideration in scientific work', 'This concept only applies to non-scientific measurements'], 0)]),
Sc('Artificial Intelligence and Machine Learning: An Introduction',
   'Grade 8 Science and Technology strand: artificial intelligence refers to computer systems designed to perform tasks that typically require human intelligence, and machine learning is a method that allows these systems to improve through exposure to data.',
   [('Artificial intelligence refers to ___.', ['Computer systems designed to perform tasks requiring human-like intelligence', 'A system with no connection to computing', 'A concept unrelated to technology', 'Only physical robots, with no software involved'], 0),
    ('Machine learning allows computer systems to ___.', ['Improve their performance through exposure to data', 'Remain completely unchanged regardless of new information', 'Function with no connection to data at all', 'Replace the need for any programming'], 0),
    ('Which is an example of a real-world application of artificial intelligence?', ['A virtual assistant that responds to voice commands', 'A tool with no connection to computing technology', 'An object unrelated to any form of intelligence', 'A device that cannot process any information'], 0),
    ('Why might machine learning models require large amounts of data?', ['More data can help the model identify patterns and improve accuracy', 'Data has no connection to how machine learning models function', 'Machine learning models never require any data', 'Large amounts of data always make a model less accurate'], 0),
    ('Why is understanding artificial intelligence increasingly important today?', ['AI technology is being used across many industries and everyday applications', 'Artificial intelligence has no real-world relevance', 'AI is used exclusively in fictional stories', 'This technology has no connection to modern life'], 0)]),
H('Canada’s Role in the Suez Crisis and UN Peacekeeping Origins',
  'Grade 8 History strand: Canadian diplomat Lester B. Pearson played a key role in resolving the 1956 Suez Crisis by proposing the first large-scale United Nations peacekeeping force, later earning him the Nobel Peace Prize.',
  [('The Suez Crisis took place in which year?', ['1919', '1945', '1956', '1982'], 2),
   ('Lester B. Pearson proposed the creation of ___.', ['The first large-scale United Nations peacekeeping force', 'A new Canadian political party', 'A trade agreement unrelated to peacekeeping', 'A domestic Canadian policy with no international connection'], 0),
   ('For his role in resolving the Suez Crisis, Lester B. Pearson later received the ___.', ['Nobel Peace Prize', 'No recognition of any kind', 'An award unrelated to international diplomacy', 'A prize for scientific achievement'], 0),
   ('Why is Canada’s role in the Suez Crisis significant to the history of peacekeeping?', ['It marked an early and influential example of international peacekeeping efforts', 'It had no connection to the development of peacekeeping', 'Canada played no role in resolving this crisis', 'This event has no historical significance'], 0),
   ('Why might this event be seen as an important part of Canada’s international reputation?', ['It reflects Canada’s early and significant contribution to global diplomacy and peacekeeping', 'This event has no connection to Canada’s international reputation', 'Canada’s involvement in this crisis was never recognized', 'This event has no relevance to Canadian history'], 0)])]),

day(48, [
L('Grammar: Nominalization and Concise Writing',
  'Grade 8 Writing strand: nominalization turns verbs or adjectives into nouns (decide becomes decision), which can sometimes make writing wordier, so concise writing often favours strong, direct verbs instead.',
  [('Nominalization refers to ___.', ['Turning a verb or adjective into a noun', 'Turning a noun into a verb', 'Removing all nouns from a sentence', 'A rule unrelated to word forms'], 0),
   ('Which is an example of a nominalized form of the verb decide?', ['Decision', 'Decide', 'Deciding quickly', 'Undecided'], 0),
   ('Why might overusing nominalizations make writing less concise?', ['It can replace strong, direct verbs with wordier noun phrases', 'Nominalization always makes writing shorter and clearer', 'Nominalized words have no effect on sentence length', 'Concise writing always requires more nominalizations'], 0),
   ('Which sentence demonstrates more concise, direct writing?', ['She decided quickly.', 'She made a decision quickly.', 'A decision was made by her quickly.', 'The making of a decision occurred quickly by her.'], 0),
   ('Why might a writer choose to revise nominalized sentences into more direct ones?', ['Direct sentences with strong verbs are often clearer and more engaging', 'Nominalized sentences are always clearer than direct ones', 'Revising sentences has no effect on writing quality', 'Concise writing has no connection to verb choice'], 0)]),
M('Introduction to Conditional Probability',
  'Grade 8 Data Management strand (pre-high-school extension): conditional probability is the probability of an event occurring given that another event has already occurred, which can change the likelihood compared to the event happening independently.',
  [('Conditional probability refers to ___.', ['The probability of an event occurring given that another event has already occurred', 'The probability of two completely unrelated events', 'A probability that never changes based on other events', 'A concept unrelated to probability'], 0),
   ('If drawing a card from a deck without replacement, why might the probability of the second draw depend on the first?', ['The first draw changes the number and composition of remaining cards', 'The two draws are always completely unrelated to each other', 'Conditional probability never applies to drawing cards', 'The probability always stays exactly the same regardless of prior events'], 0),
   ('If a bag has 3 red and 2 blue marbles, and a red marble is removed, what is the probability the next marble drawn is red?', ['2 out of 4', '3 out of 5', '2 out of 5', '3 out of 4'], 0),
   ('Why is conditional probability useful in real-world situations, such as drawing cards or medical testing?', ['It accounts for how earlier events can affect the likelihood of later outcomes', 'Conditional probability has no real-world applications', 'Earlier events never affect the probability of later outcomes', 'This concept only applies to theoretical, unrealistic situations'], 0),
   ('Two events are considered independent if ___.', ['The occurrence of one does not affect the probability of the other', 'They always affect each other significantly', 'They can never both occur', 'They are always identical events'], 0)]),
Sc('Sustainable Agriculture and Food Technology',
   'Grade 8 Science and Technology strand: sustainable agriculture practices, along with food technologies like vertical farming and precision agriculture, aim to increase food production efficiency while minimizing environmental impact.',
   [('Sustainable agriculture aims to ___.', ['Increase food production efficiency while minimizing environmental impact', 'Maximize environmental harm with no consideration of efficiency', 'Ignore food production entirely', 'Have no connection to environmental impact'], 0),
    ('Vertical farming involves growing crops ___.', ['In stacked layers, often indoors, to maximize limited space', 'Only in traditional, expansive outdoor fields', 'Without using any technology', 'In a method with no connection to space efficiency'], 0),
    ('Precision agriculture uses technology to ___.', ['Optimize resources like water and fertilizer based on specific field data', 'Ignore all data related to farming', 'Use resources with no consideration of efficiency', 'Replace the need for any farming technology'], 0),
    ('Why might sustainable agriculture practices be increasingly important as global population grows?', ['They can help meet increasing food demands while protecting environmental resources', 'Sustainable practices have no connection to meeting food demands', 'Population growth has no effect on agricultural practices', 'Environmental impact is unrelated to food production methods'], 0),
    ('Why is food technology considered an important area of scientific innovation?', ['It can help address challenges related to food security and environmental sustainability', 'Food technology has no real-world significance', 'This area of innovation has no connection to agriculture', 'Food production has no relationship to technological advancement'], 0)]),
H('The Employment Equity Act and Workplace Rights',
  'Grade 8 History strand: the Employment Equity Act, passed in 1986, aimed to address workplace discrimination and promote equal opportunity for underrepresented groups, including women, Indigenous peoples, and people with disabilities.',
  [('The Employment Equity Act was passed in which year?', ['1919', '1945', '1986', '2000'], 2),
   ('The Employment Equity Act aimed to address ___.', ['Workplace discrimination and promote equal opportunity', 'No issues related to employment', 'A topic unrelated to Canadian workplaces', 'The elimination of all workplace regulations'], 0),
   ('Which groups were specifically identified as underrepresented under this legislation?', ['Women, Indigenous peoples, and people with disabilities', 'No specific groups were identified', 'Only groups unrelated to workplace equity', 'Groups with no historical connection to discrimination'], 0),
   ('Why is the Employment Equity Act considered significant in Canadian labour history?', ['It represented a formal effort to promote fairness and equal opportunity in the workplace', 'It had no effect on workplace practices', 'This legislation was never actually passed', 'It has no connection to workplace rights in Canada'], 0),
   ('Why might legislation like the Employment Equity Act continue to be studied and discussed today?', ['It reflects ongoing efforts to address workplace equity and inclusion', 'This legislation has no relevance to modern discussions of workplace rights', 'Workplace discrimination has never been a historical concern', 'This topic has no connection to Canadian history'], 0)])]),

day(49, [
L('Writing: The Personal Manifesto',
  'Grade 8 Writing strand: a personal manifesto expresses a writer’s core beliefs and values, often written with a strong, declarative voice to clearly communicate what the writer stands for.',
  [('A personal manifesto is meant to express a writer’s ___.', ['Core beliefs and values', 'A completely unrelated topic', 'Someone else’s beliefs and values', 'A summary of unrelated facts'], 0),
   ('A manifesto is often written with a ___ voice.', ['Strong, declarative', 'Extremely vague and uncertain', 'Completely neutral with no personal viewpoint', 'A voice with no connection to the writer'], 0),
   ('Why might a writer use bold, direct statements in a personal manifesto?', ['To clearly and confidently communicate what they believe and stand for', 'Bold statements have no place in a manifesto', 'A manifesto should always avoid expressing clear beliefs', 'Direct statements always weaken this type of writing'], 0),
   ('Which is an example of a statement that might appear in a personal manifesto?', ['I believe kindness should guide every decision I make.', 'The weather today is mild.', 'This is a random, unrelated fact.', 'A manifesto contains no personal statements.'], 0),
   ('Why might writing a personal manifesto help a writer reflect on their own identity?', ['It requires clearly articulating their values and what matters most to them', 'This type of writing has no connection to self-reflection', 'A manifesto never requires any personal reflection', 'Personal identity has no connection to this type of writing'], 0)]),
M('Introduction to Complex Fractions and Rational Expressions',
  'Grade 8 Number strand (pre-high-school extension): a complex fraction contains a fraction within its numerator, denominator, or both, and simplifying it often involves rewriting it as a division problem.',
  [('A complex fraction is one that contains ___.', ['A fraction within its numerator, denominator, or both', 'Only whole numbers with no fractions at all', 'No numerical values of any kind', 'A single digit with no fraction involved'], 0),
   ('Simplifying a complex fraction often involves rewriting it as a ___ problem.', ['Division', 'Addition only', 'A problem unrelated to fractions', 'Subtraction only'], 0),
   ('Simplify: (1/2) divided by (1/4).', ['2', '1/8', '4', '1/2'], 0),
   ('A rational expression is best described as ___.', ['A fraction where the numerator and denominator are polynomials', 'A number with no connection to fractions', 'Always a whole number with no variables', 'An expression that can never include variables'], 0),
   ('Why might complex fractions appear in more advanced algebraic problems?', ['They often result from combining multiple fractional expressions within a single problem', 'Complex fractions never appear in algebra', 'They have no connection to rational expressions', 'These fractions only appear in basic arithmetic, never algebra'], 0)]),
Sc('The Physics of Sound and Acoustics',
   'Grade 8 Science Matter and Energy strand: acoustics is the study of how sound behaves in different environments, including how it reflects, absorbs, and travels, which is important for designing spaces like concert halls.',
   [('Acoustics is the study of ___.', ['How sound behaves in different environments', 'How light travels through space', 'The structure of rocks', 'The movement of tectonic plates'], 0),
    ('Sound waves can ___ when they encounter different surfaces.', ['Reflect or be absorbed', 'Always disappear completely', 'Never interact with surfaces at all', 'Turn into light waves'], 0),
    ('Why might a concert hall be designed with specific materials and shapes?', ['To control how sound reflects and travels for optimal listening quality', 'Acoustic design has no effect on sound quality', 'Concert halls are never designed with sound in mind', 'The materials used have no connection to acoustics'], 0),
    ('Soft materials, like curtains or carpet, tend to ___ sound more than hard surfaces.', ['Absorb', 'Reflect', 'Amplify', 'Have no effect on'], 0),
    ('Why is understanding acoustics valuable in fields like architecture and audio engineering?', ['It helps design spaces and technologies that control sound quality effectively', 'Acoustics has no real-world applications', 'Sound behavior has no connection to building or space design', 'This field has no relevance to engineering or design'], 0)]),
H('Same-Sex Marriage Legalization in Canada',
  'Grade 8 History strand: Canada legalized same-sex marriage nationwide in 2005, becoming one of the first countries in the world to do so, following a series of court decisions and public advocacy.',
  [('Canada legalized same-sex marriage nationwide in which year?', ['1982', '2000', '2005', '2015'], 2),
   ('Canada was among ___ countries in the world to legalize same-sex marriage nationwide.', ['The first', 'The last', 'A country with no connection to this issue', 'One with no historical significance regarding this topic'], 0),
   ('The legalization of same-sex marriage in Canada followed ___.', ['A series of court decisions and public advocacy', 'No legal or public activity of any kind', 'A process unrelated to legal or social change', 'Immediate, uncontested legislative action with no prior advocacy'], 0),
   ('Why is the legalization of same-sex marriage considered a significant milestone in Canadian history?', ['It reflected an expansion of legal rights and recognition for same-sex couples', 'It had no effect on legal rights in Canada', 'This event never actually took place', 'It has no connection to Canadian social history'], 0),
   ('Why might studying this history be relevant to understanding social change in Canada?', ['It illustrates how legal and social advocacy can lead to expanded rights over time', 'This topic has no connection to understanding social change', 'Social change in Canada has never involved legal advocacy', 'This event has no relevance to Canadian history'], 0)])]),

day(50, [
L('Reading: Evaluating an Author’s Use of Structure',
  'Grade 8 Reading strand: an author’s structural choices, such as chronological order, flashback, or parallel storylines, shape how a story unfolds and affect the reader’s understanding and engagement.',
  [('An author’s structural choices can include using ___.', ['Chronological order, flashback, or parallel storylines', 'Only random, unrelated events with no structure', 'No identifiable structure of any kind', 'A structure unrelated to how a story unfolds'], 0),
   ('Why might an author use parallel storylines in a text?', ['To show connections or contrasts between different characters or events', 'Parallel storylines always confuse readers with no purpose', 'This structure has no effect on a story’s meaning', 'Parallel storylines are never used in literature'], 0),
   ('Chronological structure presents events ___.', ['In the order they occur in time', 'In a completely random order', 'With no connection to time at all', 'Only in reverse order, from end to beginning'], 0),
   ('Why is evaluating an author’s structural choices considered an important reading skill?', ['Structure significantly shapes how readers understand and experience a story', 'Structural choices have no effect on how a story is understood', 'This skill has no connection to reading comprehension', 'All stories use identical structures regardless of the author’s choices'], 0),
   ('Which is an example of how structure might affect a reader’s understanding of a mystery story?', ['Withholding key information until later in the story to build suspense', 'Presenting all information immediately with no structural choices', 'Structure has no effect on how mystery stories are understood', 'Mystery stories never use any particular structural techniques'], 0)]),
M('Review: Systems, Trigonometric Applications, and Advanced Algebra',
  'Grade 8 Number and Algebra strands review: this lesson revisits solving systems by elimination, applying trigonometric ratios, factoring trinomials, the quadratic formula, and conditional probability from recent lessons.',
  [('Solve the system using elimination: x + y = 12 and x minus y = 4.', ['x = 8, y = 4', 'x = 4, y = 8', 'x = 6, y = 6', 'x = 12, y = 4'], 0),
   ('Factor: x squared plus 6x plus 8.', ['(x + 2)(x + 4)', '(x + 1)(x + 8)', '(x + 3)(x + 5)', '(x + 6)(x + 2)'], 0),
   ('The quadratic formula is used to solve equations in the form ___.', ['ax squared plus bx plus c equals zero', 'ax plus b equals zero', 'a plus b equals c', 'a divided by b equals c'], 0),
   ('Conditional probability refers to ___.', ['The probability of an event occurring given that another event has already occurred', 'The probability of two completely unrelated events', 'A probability that never changes based on other events', 'A concept unrelated to probability'], 0),
   ('Why is it useful to review systems, trigonometry, and advanced algebra together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
Sc('Review: Biotechnology, Environmental Science, and Emerging Technology',
   'Grade 8 Science review: this lesson revisits CRISPR and gene editing, ocean acidification, forensic science, artificial intelligence, and sustainable agriculture covered across recent lessons.',
   [('CRISPR is a technology used to ___.', ['Make precise changes to DNA', 'Measure the size of a cell', 'Predict weather patterns', 'Study the movement of tectonic plates'], 0),
    ('Ocean acidification occurs when the ocean absorbs excess ___.', ['Carbon dioxide from the atmosphere', 'Oxygen only', 'Nitrogen only', 'Helium'], 0),
    ('Forensic science applies scientific methods to ___.', ['Investigate crimes and support legal processes', 'A field entirely unrelated to investigation', 'Only artistic creation, with no connection to science', 'Predicting weather patterns'], 0),
    ('Machine learning allows computer systems to ___.', ['Improve their performance through exposure to data', 'Remain completely unchanged regardless of new information', 'Function with no connection to data at all', 'Replace the need for any programming'], 0),
    ('Why is it valuable to review biotechnology, environmental science, and emerging technology together?', ['It helps connect and reinforce related science concepts learned across recent lessons', 'These topics are entirely unrelated to each other', 'Review provides no benefit in science', 'Each topic must always be studied in isolation'], 0)]),
H('Review: Rights, Reconciliation, and Modern Canadian History',
  'Grade 8 History review: this lesson revisits the Persons Case, the White Paper of 1969, the Meech Lake and Charlottetown Accords, the Employment Equity Act, and same-sex marriage legalization covered across recent lessons.',
  [('The Persons Case established that women in Canada were legally considered ___.', ['Persons eligible to be appointed to the Senate', 'Ineligible for any legal rights', 'Excluded from all legal recognition', 'A group with no connection to Canadian law'], 0),
   ('The White Paper of 1969 proposed to ___.', ['Eliminate the Indian Act and Indigenous legal status', 'Strengthen Indigenous rights significantly', 'Have no effect on existing policy', 'Expand Indigenous self-government immediately'], 0),
   ('The Meech Lake Accord and Charlottetown Accord were attempts to ___.', ['Amend Canada’s constitution', 'Eliminate Canada’s constitution entirely', 'Create an entirely new country', 'Address issues unrelated to Canadian government'], 0),
   ('Canada legalized same-sex marriage nationwide in which year?', ['1982', '2000', '2005', '2015'], 2),
   ('Why is it useful to review rights, reconciliation, and modern Canadian history topics together?', ['It helps reinforce how these historical developments connect to shape rights in Canada today', 'These topics have no meaningful connections', 'Review is never useful in history', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260720):
    """Same technique used for the earlier Phase 3 batches -- reassigns
    each question's correct-answer slot via a shuffled round-robin (even
    across 0-3) and shuffles the wrong options into the remaining slots.
    Question and option TEXT is never changed. Mutates `days` in place."""
    import random
    rng = random.Random(seed)
    all_quizzes = [quiz for _, subs in days for *_, quiz in subs]
    n = sum(len(quiz) for quiz in all_quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in all_quizzes:
        for i, (q, opts, ans) in enumerate(quiz):
            correct_text = opts[ans]
            wrong_texts = [o for j, o in enumerate(opts) if j != ans]
            rng.shuffle(wrong_texts)
            target = targets[idx]
            idx += 1
            new_opts = [None, None, None, None]
            new_opts[target] = correct_text
            wi = 0
            for slot in range(4):
                if new_opts[slot] is None:
                    new_opts[slot] = wrong_texts[wi]
                    wi += 1
            quiz[i] = (q, new_opts, target)


if __name__ == '__main__':
    _rebalance_answer_positions(g8_41_50)
    append_to(8, g8_41_50)
