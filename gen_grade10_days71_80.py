#!/usr/bin/env python3
"""Phase 3 extension: Grade 10, Days 71-80 (fifth Grade 10 batch). Topics
chosen to avoid any overlap with the existing Day 1-70 set (see
data/grade10.ts): the unreliable narrator, motif and recurring imagery,
sentence fragments and run-ons, diction and tone, the cover letter and
resume, frame narratives, constructive feedback, dialogue as
characterization, and modifiers in English; the discriminant, direct and
partial variation, compound interest, angle of elevation and depression,
the three-dimensional Pythagorean theorem, laws of exponents, the dot
product, polynomial zeros/factors/end behaviour, and dilations in Math;
periodic trends, the circulatory and respiratory systems, static
electricity, renewable and non-renewable energy resources, empirical and
molecular formulas, biodiversity and conservation, simple machines, soil
formation, and xylem/phloem in Science; and Canada in the First World
War, the Conscription Crisis, the Chanak Affair and Statute of
Westminster, the 1918-1920 Spanish Flu pandemic, the Bomarc missile
crisis, the Massey Commission, and three Civics lessons (how a bill
becomes a law, the electoral system, levels of government) in History.

Subject keys for Grade 10 are "English", "Math", "Science", and
"History" (confirmed via data/grade10.ts), same as
gen_grade10_days61_70.py. History content is kept within Canadian
history/civics scope and, consistent with the existing Day 1-70 set,
within the 1914-to-present era (the civics lessons are contemporary and
not tied to a historical period).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option
text; apostrophes and quotation marks use the curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

E10 = 'https://tvolearn.com/pages/grade-10-english'
M10 = 'https://tvolearn.com/pages/grade-10-mathematics'
S10 = 'https://tvolearn.com/pages/grade-10-science'
H10 = 'https://tvolearn.com/pages/grade-10-history'
RE, RM, RS, RH = (
    'TVO Learn: Grade 10 English',
    'TVO Learn: Grade 10 Mathematics',
    'TVO Learn: Grade 10 Science',
    'TVO Learn: Grade 10 History',
)


def E(t, s, q):
    return sub('English', t, s, RE, E10, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M10, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S10, q)


def H(t, s, q):
    return sub('History', t, s, RH, H10, q)


g10_71_80 = [
day(71, [
E('Reading: The Unreliable Narrator',
  'Grade 10 English strand: an unreliable narrator is a narrator whose credibility is compromised, whether by bias, limited knowledge, or deliberate deception, requiring readers to critically evaluate the accuracy of the account being presented.',
  [('An unreliable narrator is best described as a narrator whose ___.', ['Credibility or accuracy is compromised in some way', 'Account is always completely accurate and objective', 'A concept unrelated to narrative point of view', 'Only appears in non-fiction texts, never in fiction'], 0),
   ('Which of these might cause a narrator to be unreliable?', ['A personal bias, limited knowledge, or a deliberate intent to deceive', 'Having complete and perfect knowledge of every event', 'A trait unrelated to narrative reliability', 'Narrating a story in the third person exclusively'], 0),
   ('Why must readers pay close attention to inconsistencies when a narrator may be unreliable?', ['Inconsistencies can reveal gaps between what a narrator claims and what actually occurred in the story', 'Inconsistencies never provide any useful information to a reader', 'A reason unrelated to evaluating a narrator’s credibility', 'Unreliable narrators always state events with perfect accuracy'], 0),
   ('Why might an author choose to use an unreliable narrator rather than an objective one?', ['It can create suspense or complexity by forcing readers to question what is really happening', 'Unreliable narrators always make a story less interesting', 'A reason unrelated to narrative technique', 'Objective narrators are never a valid choice for a story'], 0),
   ('Why is recognizing an unreliable narrator considered an important critical reading skill?', ['It helps readers interpret a text more carefully rather than accepting every claim at face value', 'This skill has no connection to critical reading', 'Readers should always accept a narrator’s account without question', 'This concept only applies to nonfiction writing'], 0)]),
M('Quadratic Relations: The Discriminant and Nature of Roots',
  'Grade 10 Quadratics strand (extension): the discriminant, b² - 4ac, determines the number and type of roots a quadratic equation has, indicating whether the roots are real and distinct, real and equal, or non-real.',
  [('The discriminant of a quadratic equation is calculated using the expression ___.', ['b² - 4ac', 'b² + 4ac', 'An expression unrelated to the discriminant', '-b divided by 2a'], 0),
   ('If the discriminant of a quadratic equation is positive, the equation has ___.', ['Two real, distinct roots', 'No real roots', 'A result unrelated to the discriminant', 'Exactly one repeated real root'], 0),
   ('If the discriminant of a quadratic equation equals zero, the equation has ___.', ['Exactly one repeated real root', 'Two distinct real roots', 'A result unrelated to the discriminant', 'No real roots at all'], 0),
   ('Why does a negative discriminant indicate that a quadratic equation has no real roots?', ['A negative value under the square root in the quadratic formula produces non-real, complex results', 'A negative discriminant always indicates two real, distinct roots', 'A reason unrelated to the discriminant', 'The discriminant’s sign has no connection to the type of roots a quadratic has'], 0),
   ('Why is the discriminant a useful tool before fully solving a quadratic equation?', ['It allows a student to quickly determine the number and type of roots without applying the entire quadratic formula', 'The discriminant provides no useful information about a quadratic equation', 'A reason unrelated to solving quadratic equations', 'Calculating the discriminant always takes longer than fully solving the equation'], 0)]),
Sc('Chemistry: Periodic Trends',
   'Grade 10 Chemistry strand (extension): periodic trends describe predictable patterns in properties such as atomic radius, ionization energy, and electronegativity as one moves across a period or down a group of the periodic table.',
   [('Periodic trends describe predictable patterns in properties as one moves across a ___ of the periodic table.', ['Period or down a group', 'Random arrangement with no predictable pattern', 'A concept unrelated to the periodic table', 'Colour scheme only, with no connection to chemical properties'], 0),
    ('As you move from left to right across a period, atomic radius generally ___.', ['Decreases', 'Increases', 'A trend unrelated to atomic radius', 'Stays exactly the same'], 0),
    ('As you move down a group of the periodic table, atomic radius generally ___.', ['Increases', 'Decreases', 'A trend unrelated to atomic radius', 'Stays exactly the same'], 0),
    ('Why does ionization energy generally increase as you move from left to right across a period?', ['Increasing nuclear charge pulls the outermost electrons more tightly, making them harder to remove', 'Ionization energy always decreases across a period, with no connection to nuclear charge', 'A reason unrelated to periodic trends', 'Nuclear charge has no effect on how tightly electrons are held'], 0),
    ('Why are periodic trends useful for predicting how an element will behave in a chemical reaction?', ['They provide insight into an atom’s tendency to gain, lose, or share electrons based on its position on the periodic table', 'Periodic trends provide no useful information about chemical behaviour', 'A reason unrelated to periodic trends', 'An element’s position on the periodic table never affects how it reacts'], 0)]),
H('Canada and the First World War: Vimy Ridge and the Birth of National Identity',
  'Grade 10 History strand: Canada entered the First World War in 1914 as part of the British Empire, and the 1917 victory at Vimy Ridge, where Canadian troops fought together as a unified force for the first time, became a defining symbol of emerging Canadian national identity.',
  [('Canada entered the First World War in which year?', ['1914', '1917', '1929', '1939'], 0),
   ('At the Battle of Vimy Ridge, Canadian troops fought together as a unified force for the ___.', ['First time', 'Only time in Canadian military history', 'A detail unrelated to Vimy Ridge', 'Last time before Confederation'], 0),
   ('Canada’s participation in the First World War was initially tied to its status as part of ___.', ['The British Empire', 'An independent nation with no ties to Britain', 'A relationship unrelated to Canada’s WWI involvement', 'The United States’ military alliance'], 0),
   ('Why is the Battle of Vimy Ridge often described as a defining moment in Canadian national identity?', ['Canadian troops’ success fighting as a unified national force helped foster a growing sense of pride and distinct identity', 'This battle had no connection to Canadian national identity', 'Vimy Ridge has no lasting significance in Canadian history', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians often connect Canada’s First World War experience to its later push for greater independence from Britain?', ['The war’s sacrifices and achievements strengthened Canada’s confidence in asserting its own voice on the world stage', 'Canada’s First World War experience had no connection to its later independence', 'Canadian independence was never connected to any historical events', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(72, [
E('Reading: Motif and Recurring Imagery',
  'Grade 10 English strand: a motif is a recurring element, image, or idea that appears throughout a text, reinforcing a story’s themes and adding layers of meaning through repetition.',
  [('A motif is best described as a recurring ___.', ['Element, image, or idea that appears throughout a text', 'Character who appears only once in a story', 'A concept unrelated to literary analysis', 'Setting that changes completely with every scene'], 0),
   ('Why might an author repeat a specific image throughout a novel?', ['Repetition can reinforce a theme or draw attention to its significance', 'Repeating an image always weakens a story’s structure', 'A reason unrelated to literary technique', 'Authors never intentionally repeat images or ideas'], 0),
   ('Which is an example of how a motif might function in a text?', ['A recurring symbol, such as light and darkness, that reinforces a central theme', 'A single unrelated detail mentioned only once', 'A technique unrelated to motif', 'An element that never connects to any broader theme'], 0),
   ('Why might tracking a motif across an entire novel deepen a reader’s understanding of theme?', ['Seeing how a motif evolves or shifts can reveal how a theme develops over the course of the story', 'Motifs never change or develop throughout a text', 'A reason unrelated to thematic analysis', 'Tracking a motif provides no additional insight into a text'], 0),
   ('Why is motif considered distinct from a one-time literary device, like a single metaphor?', ['A motif recurs multiple times across a text, building cumulative meaning, rather than appearing only once', 'A motif and a single metaphor are always identical in function', 'This distinction has no connection to literary analysis', 'Motifs only ever appear a single time in a text'], 0)]),
M('Algebra: Direct and Partial Variation',
  'Grade 10 Algebra strand (extension): direct variation describes a relationship where one quantity is a constant multiple of another, expressed as y = kx, while partial variation includes an additional constant term, expressed as y = kx + b.',
  [('Direct variation describes a relationship expressed in the form ___.', ['y = kx', 'y = kx + b', 'An expression unrelated to direct variation', 'y = k divided by x'], 0),
   ('Partial variation differs from direct variation because it includes ___.', ['An additional constant term', 'No constant of variation at all', 'A difference unrelated to variation relationships', 'A variable exponent on x'], 0),
   ('In a direct variation relationship, when x = 0, the value of y must be ___.', ['0', 'Equal to the constant of variation, k', 'A value unrelated to direct variation', 'Undefined in every case'], 0),
   ('Why does the graph of a partial variation relationship not pass through the origin, unlike a direct variation relationship?', ['The added constant term shifts the line vertically away from the point (0, 0)', 'Partial variation relationships always pass through the origin, just like direct variation', 'A reason unrelated to variation relationships', 'The constant of variation, k, has no effect on where a line is positioned'], 0),
   ('Why are direct and partial variation useful for modelling real-world relationships, such as the cost of a service with a flat fee plus a per-unit rate?', ['They provide a simple linear model that reflects either a purely proportional relationship or one with a fixed starting value', 'Direct and partial variation have no real-world modelling applications', 'A reason unrelated to variation relationships', 'Costs involving a flat fee and a per-unit rate can never be modelled using these relationships'], 0)]),
Sc('Biology: The Circulatory and Respiratory Systems',
   'Grade 10 Biology strand: the circulatory system transports oxygen, nutrients, and waste throughout the body using the heart and blood vessels, working closely with the respiratory system, which exchanges oxygen and carbon dioxide between the body and the environment.',
   [('The circulatory system primarily transports oxygen, nutrients, and waste using the heart and ___.', ['Blood vessels', 'Lungs exclusively, with no connection to blood vessels', 'A structure unrelated to circulation', 'Digestive organs only, with no connection to blood'], 0),
    ('The respiratory system primarily exchanges which two gases between the body and the environment?', ['Oxygen and carbon dioxide', 'Nitrogen and hydrogen', 'A pair of gases unrelated to respiration', 'Oxygen and helium'], 0),
    ('Which structure in the circulatory system pumps blood throughout the body?', ['The heart', 'The lungs', 'A structure unrelated to circulation', 'The diaphragm'], 0),
    ('Why do the circulatory and respiratory systems work closely together?', ['The circulatory system carries the oxygen absorbed by the respiratory system to cells throughout the body, and returns carbon dioxide for exhalation', 'These two systems function completely independently with no connection to each other', 'A reason unrelated to human body systems', 'The respiratory system has no role in delivering oxygen to the body’s cells'], 0),
    ('Why is understanding the circulatory and respiratory systems important for studying conditions like cardiovascular disease?', ['Many health conditions arise from disruptions to how these systems transport oxygen and maintain blood flow', 'These body systems have no connection to any medical conditions', 'A reason unrelated to human health', 'Cardiovascular disease has no connection to the circulatory system'], 0)]),
H('The Conscription Crisis of 1917',
  'Grade 10 History strand: the 1917 Conscription Crisis erupted when the federal government introduced mandatory military service to address wartime troop shortages, a decision that deeply divided English and French Canada and strained national unity.',
  [('The Conscription Crisis took place in which year?', ['1917', '1929', '1945', '1962'], 0),
   ('Conscription refers to a policy of ___.', ['Mandatory military service', 'Voluntary military enlistment only', 'A policy unrelated to military service', 'Mandatory civilian labour with no connection to the military'], 0),
   ('The federal government introduced conscription in 1917 primarily to address ___.', ['Wartime troop shortages', 'A shortage of factory workers', 'A reason entirely unrelated to the war', 'A shortage of agricultural labourers'], 0),
   ('Why did the Conscription Crisis deeply divide English and French Canada?', ['Many French Canadians felt less connected to a war fought primarily for British imperial interests, while many English Canadians strongly supported the war effort', 'English and French Canadians held identical views on conscription', 'This crisis had no connection to any divisions within Canada', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians consider the Conscription Crisis an important moment in Canadian political history?', ['It revealed and deepened long-standing tensions between English and French Canada that would continue to shape national politics', 'The Conscription Crisis had no lasting effect on Canadian politics', 'English and French Canada have never experienced any political tension', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(73, [
E('Grammar: Sentence Fragments and Run-On Sentences',
  'Grade 10 English strand: a sentence fragment is an incomplete sentence missing a subject, verb, or complete thought, while a run-on sentence improperly joins two or more independent clauses without correct punctuation or conjunctions.',
  [('A sentence fragment is best described as a group of words that ___.', ['Is missing a subject, verb, or complete thought', 'Always contains two complete independent clauses', 'A concept unrelated to sentence structure', 'Is always too long to be considered a single sentence'], 0),
   ('A run-on sentence occurs when ___.', ['Two or more independent clauses are joined without correct punctuation or conjunctions', 'A sentence contains only a single word', 'A concept unrelated to grammar', 'A sentence is missing its subject entirely'], 0),
   ('Which of these is an example of a sentence fragment?', ['Running through the park every morning.', 'She ran through the park every morning.', 'A sentence unrelated to fragments or run-ons', 'After she finished, she ran through the park.'], 0),
   ('Why might a writer use a semicolon to correct a run-on sentence?', ['A semicolon can properly join two closely related independent clauses without a coordinating conjunction', 'A semicolon can never be used to join two clauses', 'A reason unrelated to correcting run-on sentences', 'Semicolons always create a sentence fragment instead of fixing one'], 0),
   ('Why is it important to avoid both fragments and run-ons in formal academic writing?', ['Both errors can confuse a reader and obscure the intended meaning of a sentence', 'These errors never affect how clearly a sentence communicates meaning', 'A reason unrelated to writing conventions', 'Formal writing has no expectations around sentence structure'], 0)]),
M('Financial Literacy: Compound Interest and Amortization',
  'Grade 10 Financial Literacy strand (extension): compound interest is calculated on both the initial principal and the accumulated interest from previous periods, and an amortization schedule breaks down how each loan payment is divided between interest and principal over time.',
  [('Compound interest is calculated based on ___.', ['Both the initial principal and the accumulated interest from previous periods', 'Only the initial principal, with no connection to accumulated interest', 'A concept unrelated to interest calculations', 'A fixed amount that never changes over time'], 0),
   ('An amortization schedule shows how each loan payment is divided between ___.', ['Interest and principal', 'Only interest, with no connection to principal', 'A concept unrelated to loan repayment', 'Taxes and fees exclusively'], 0),
   ('Compared to simple interest, compound interest generally causes an investment to grow ___.', ['Faster over time', 'Slower over time', 'A comparison unrelated to interest calculations', 'At exactly the same rate as simple interest'], 0),
   ('Why does the portion of an amortized loan payment applied to interest typically decrease over the life of the loan?', ['As the principal balance shrinks with each payment, the interest charged on that smaller balance also decreases', 'The portion applied to interest always increases over the life of the loan', 'A reason unrelated to amortization', 'The amount applied to interest never changes throughout a loan’s term'], 0),
   ('Why is understanding compound interest important when comparing long-term savings or investment options?', ['Small differences in interest rate or compounding frequency can lead to significantly different amounts over a long period of time', 'Compound interest has no meaningful effect on long-term savings or investments', 'A reason unrelated to financial literacy', 'All savings and investment options grow at an identical rate regardless of compounding'], 0)]),
Sc('Physics: Static Electricity and Electric Charge',
   'Grade 10 Physics strand: static electricity results from an imbalance of electric charge on an object’s surface, typically caused by the transfer of electrons through friction, and objects with like charges repel while objects with opposite charges attract.',
   [('Static electricity results from an imbalance of ___ on an object’s surface.', ['Electric charge', 'Temperature', 'A concept unrelated to static electricity', 'Mass'], 0),
    ('Static electricity is typically caused by the transfer of ___ through friction.', ['Electrons', 'Protons', 'A particle unrelated to static electricity', 'Neutrons'], 0),
    ('Objects with like electric charges will ___ each other.', ['Repel', 'Attract', 'A result unrelated to electric charge', 'Have no effect on'], 0),
    ('Why does rubbing two different materials together often generate static electricity?', ['The friction can transfer electrons from one material to the other, creating a charge imbalance', 'Friction never causes any transfer of electric charge between materials', 'A reason unrelated to static electricity', 'Rubbing two materials together always removes all electric charge from both objects'], 0),
    ('Why is understanding static electricity important for practical safety concerns, such as around flammable materials?', ['A static discharge can create a spark capable of igniting flammable vapours or materials', 'Static electricity has no connection to any safety concerns', 'A reason unrelated to physics', 'Static discharges are never capable of producing a spark'], 0)]),
H('Growing Canadian Autonomy: The Chanak Affair and the Statute of Westminster',
  'Grade 10 History strand: Canada’s refusal to automatically support Britain during the 1922 Chanak Affair and the 1931 Statute of Westminster, which granted Canada full legal independence in domestic and foreign affairs, marked key steps in Canada’s growing autonomy from Britain.',
  [('The Chanak Affair took place in which year?', ['1922', '1914', '1931', '1945'], 0),
   ('The Statute of Westminster was passed in which year?', ['1931', '1922', '1914', '1945'], 0),
   ('The Statute of Westminster granted Canada ___.', ['Full legal independence in domestic and foreign affairs', 'Complete separation from the British monarchy entirely', 'A result unrelated to Canadian autonomy', 'Increased military obligations to Britain'], 0),
   ('Why is Canada’s response to the Chanak Affair considered an early sign of growing Canadian autonomy?', ['Canada declined to automatically commit troops to support Britain, showing a new willingness to make independent foreign policy decisions', 'Canada immediately and fully supported Britain’s request with no hesitation', 'The Chanak Affair had no connection to Canadian autonomy', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians view the Statute of Westminster as a major turning point in Canada’s relationship with Britain?', ['It formally recognized Canada’s legal authority to govern itself independently, rather than remaining subordinate to British parliamentary decisions', 'The Statute of Westminster had no effect on Canada’s relationship with Britain', 'This legislation increased Britain’s control over Canadian affairs', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(74, [
E('Writing: Analyzing Diction and Tone',
  'Grade 10 English strand: diction refers to an author’s specific word choices, while tone is the author’s attitude toward a subject conveyed through that diction, style, and other stylistic choices.',
  [('Diction refers to an author’s ___.', ['Specific word choices', 'Choice of setting exclusively, with no connection to word choice', 'A concept unrelated to writing style', 'Handwriting or font style alone'], 0),
   ('Tone is best described as ___.', ['The author’s attitude toward a subject, conveyed through word choice and style', 'The physical setting of a narrative, with no connection to attitude', 'A concept unrelated to diction', 'A synonym for a story’s plot events'], 0),
   ('Which is an example of how diction can shape tone?', ['Choosing harsh, blunt words rather than gentle, soft ones to create a critical tone', 'Word choice never has any effect on a text’s tone', 'A technique unrelated to diction and tone', 'Diction only affects a text’s length, not its tone'], 0),
   ('Why might two authors describe the same event using very different diction?', ['Each author’s specific word choices reflect their own distinct attitude or perspective toward the event', 'Diction is always identical across every author who writes about the same event', 'A reason unrelated to diction and tone', 'Word choice has no connection to an author’s perspective'], 0),
   ('Why is analyzing diction and tone considered a valuable close-reading skill?', ['It allows readers to uncover an author’s underlying attitude or perspective beyond the literal meaning of the words', 'This skill has no connection to understanding a text more deeply', 'Diction and tone are never worth analyzing closely', 'Only plot events, not word choice, ever reveal an author’s attitude'], 0)]),
M('Geometry: Angle of Elevation and Depression',
  'Grade 10 Trigonometry strand: the angle of elevation is the angle measured upward from a horizontal line of sight to an object above, while the angle of depression is the angle measured downward from a horizontal line of sight to an object below.',
  [('The angle of elevation is measured ___ from a horizontal line of sight.', ['Upward, to an object above', 'Downward, to an object below', 'A concept unrelated to angles of elevation', 'Sideways, with no vertical component'], 0),
   ('The angle of depression is measured ___ from a horizontal line of sight.', ['Downward, to an object below', 'Upward, to an object above', 'A concept unrelated to angles of depression', 'Only along the ground, with no connection to height'], 0),
   ('If a person on top of a cliff looks down at a boat, the angle formed between their horizontal line of sight and the boat is called the ___.', ['Angle of depression', 'Angle of elevation', 'An angle unrelated to this scenario', 'A right angle by definition, with no need for measurement'], 0),
   ('Why are the angle of elevation and the angle of depression between two points always equal to one another?', ['They are alternate interior angles formed by a transversal crossing two parallel horizontal lines of sight', 'These two angles are never related to each other in any way', 'A reason unrelated to angles of elevation and depression', 'The angle of depression is always exactly double the angle of elevation'], 0),
   ('Why are angle of elevation and depression problems useful for solving real-world measurement tasks, such as finding the height of a building?', ['They allow trigonometric ratios to be applied to indirectly calculate distances or heights that cannot be measured directly', 'These angles have no real-world measurement applications', 'A reason unrelated to trigonometry', 'Heights of buildings can never be calculated using angles of elevation or depression'], 0)]),
Sc('Earth Science: Renewable and Non-Renewable Energy Resources',
   'Grade 10 Earth Science strand: renewable energy resources, such as solar and wind, can be replenished naturally within a short time frame, while non-renewable energy resources, such as coal and oil, take millions of years to form and are being depleted faster than they can be replaced.',
   [('Renewable energy resources are best described as resources that ___.', ['Can be replenished naturally within a short time frame', 'Take millions of years to form', 'A concept unrelated to energy resources', 'Can never be replenished under any circumstances'], 0),
    ('Which of these is an example of a non-renewable energy resource?', ['Coal', 'Solar energy', 'Wind energy', 'An energy source unrelated to this classification'], 0),
    ('Non-renewable energy resources are generally being used ___ than they can naturally be replaced.', ['Faster', 'Slower', 'A comparison unrelated to energy resources', 'At exactly the same rate'], 0),
    ('Why are fossil fuels classified as non-renewable energy resources?', ['They take millions of years to form from ancient organic matter, far longer than the rate at which they are consumed', 'Fossil fuels can be replenished within a single human lifetime', 'A reason unrelated to energy classification', 'This classification has no connection to how quickly a resource forms'], 0),
    ('Why is the shift toward renewable energy resources considered important for long-term sustainability?', ['Renewable resources can be replenished naturally, reducing the risk of depleting a limited, non-renewable supply', 'Renewable energy resources have no connection to long-term sustainability', 'A reason unrelated to Earth Science', 'Non-renewable energy resources will never become depleted'], 0)]),
H('The 1918-1920 Spanish Flu Pandemic in Canada',
  'Grade 10 History strand: the Spanish Flu pandemic swept through Canada from 1918 to 1920, killing tens of thousands of people, overwhelming healthcare systems already strained by the First World War, and prompting new public health measures.',
  [('The Spanish Flu pandemic affected Canada primarily during which years?', ['1918 to 1920', '1929 to 1931', '1939 to 1941', '1945 to 1947'], 0),
   ('The Spanish Flu pandemic arrived in Canada around the same time as ___.', ['The end of the First World War', 'The Great Depression', 'An event entirely unrelated to the pandemic’s timing', 'The Second World War'], 0),
   ('The Spanish Flu pandemic in Canada is estimated to have caused ___.', ['Tens of thousands of deaths', 'No deaths at all', 'A death toll unrelated to public health history', 'Fewer than one hundred deaths nationwide'], 0),
   ('Why did the Spanish Flu pandemic place such severe strain on Canadian healthcare systems at the time?', ['Healthcare resources and personnel were already stretched thin by the ongoing demands of the First World War', 'Canadian healthcare systems faced no additional strain during this period', 'This pandemic had no connection to the state of healthcare in Canada', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians and public health officials continue to study the 1918-1920 pandemic today?', ['It offers important lessons about public health responses, healthcare capacity, and the spread of infectious disease', 'The Spanish Flu pandemic has no lasting relevance to public health today', 'This event has been entirely forgotten with no historical record', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(75, [
E('Writing: The Cover Letter and Resume',
  'Grade 10 English strand: a cover letter introduces a candidate and explains their interest in a specific opportunity, while a resume summarizes a candidate’s skills, education, and experience in a clear, organized format.',
  [('A cover letter is primarily used to ___.', ['Introduce a candidate and explain their interest in a specific opportunity', 'Provide a complete, detailed list of every job a candidate has ever held', 'A concept unrelated to professional writing', 'Replace the need for a resume entirely'], 0),
   ('A resume is best described as a document that ___.', ['Summarizes a candidate’s skills, education, and experience in a clear, organized format', 'Tells a detailed personal story with no organization', 'A concept unrelated to professional writing', 'Is always written in the same format as a cover letter'], 0),
   ('Why should a cover letter be tailored to a specific job rather than written generically?', ['A tailored letter can directly connect a candidate’s relevant skills to the specific opportunity being sought', 'Cover letters should never mention a specific job or opportunity', 'A reason unrelated to professional writing', 'A generic cover letter is always more effective than a tailored one'], 0),
   ('Why is clear, concise formatting especially important in a resume?', ['It allows a reader to quickly scan and identify a candidate’s most relevant qualifications', 'Formatting has no effect on how a resume is read or understood', 'A reason unrelated to professional writing', 'Resumes are always read in extremely close detail, word for word'], 0),
   ('Why are cover letter and resume writing considered valuable skills to develop in Grade 10?', ['They prepare students for real-world tasks like applying for jobs, volunteer positions, or programs', 'These skills have no real-world application for students', 'A reason unrelated to professional or practical writing', 'Only adults with careers ever need to write a cover letter or resume'], 0)]),
M('Geometry: The Pythagorean Theorem in Three Dimensions',
  'Grade 10 Geometry strand (extension): the Pythagorean theorem can be extended into three dimensions to find the diagonal length of a rectangular prism by applying the relationship twice, first to a base rectangle and then to the resulting right triangle.',
  [('In three dimensions, the Pythagorean theorem can be used to find the ___ of a rectangular prism.', ['Diagonal length', 'Surface area', 'A measurement unrelated to the Pythagorean theorem', 'Volume'], 0),
   ('To find the diagonal of a rectangular prism, the Pythagorean theorem is generally applied ___.', ['Twice, first to a base rectangle and then to the resulting right triangle', 'Only once, with no additional steps required', 'A method unrelated to this calculation', 'Zero times, since this shape has no diagonal'], 0),
   ('For a rectangular prism with length l, width w, and height h, the length of the space diagonal, d, satisfies ___.', ['d² = l² + w² + h²', 'd = l + w + h', 'A relationship unrelated to this calculation', 'd² = l² - w² - h²'], 0),
   ('Why must the diagonal of the base rectangle be calculated as an intermediate step when finding a rectangular prism’s space diagonal?', ['That base diagonal becomes one leg of the right triangle used to calculate the full three-dimensional diagonal', 'The base diagonal has no connection to the three-dimensional diagonal', 'A reason unrelated to this calculation', 'This intermediate step is unnecessary and can always be skipped'], 0),
   ('Why is extending the Pythagorean theorem into three dimensions useful in fields like construction or design?', ['It allows the direct distance between opposite corners of a three-dimensional object to be calculated without physical measurement', 'This extension has no real-world application in construction or design', 'A reason unrelated to three-dimensional geometry', 'The Pythagorean theorem can never be applied to three-dimensional shapes'], 0)]),
Sc('Chemistry: Empirical and Molecular Formulas',
   'Grade 10 Chemistry strand (extension): an empirical formula shows the simplest whole-number ratio of atoms in a compound, while a molecular formula shows the actual number of atoms of each element present in a single molecule.',
   [('An empirical formula shows the ___ of atoms in a compound.', ['Simplest whole-number ratio', 'Exact total number, regardless of ratio', 'A concept unrelated to chemical formulas', 'Mass in grams'], 0),
    ('A molecular formula shows ___.', ['The actual number of atoms of each element in a single molecule', 'Only the ratio of atoms, with no connection to actual quantity', 'A concept unrelated to chemical formulas', 'The charge of the overall compound only'], 0),
    ('If a compound has the molecular formula C6H12O6, what would its empirical formula be?', ['CH2O', 'C6H12O6', 'A formula unrelated to this compound', 'C3H6O3'], 0),
    ('Why can two different compounds share the same empirical formula but have different molecular formulas?', ['Their molecular formulas can be different whole-number multiples of the same simplest ratio', 'Two compounds can never share the same empirical formula', 'A reason unrelated to chemical formulas', 'Empirical and molecular formulas are always identical for every compound'], 0),
    ('Why is determining a compound’s empirical formula a useful step in identifying an unknown substance?', ['It provides the simplest ratio of elements present, which can then be used alongside molar mass data to determine the full molecular formula', 'Empirical formulas provide no useful information for identifying a compound', 'A reason unrelated to chemical analysis', 'An unknown substance can never be identified using its empirical formula'], 0)]),
H('The Bomarc Missile Crisis and Canada-US Cold War Tensions',
  'Grade 10 History strand: the early 1960s Bomarc missile controversy, over whether Canada should accept nuclear warheads for American-designed missiles on Canadian soil, exposed deep divisions within Canadian politics and ultimately contributed to the fall of the Diefenbaker government.',
  [('The Bomarc missile controversy took place primarily during which decade?', ['The 1960s', 'The 1920s', 'The 1940s', 'The 1980s'], 0),
   ('The Bomarc missile controversy centred on whether Canada should accept ___.', ['Nuclear warheads for American-designed missiles on Canadian soil', 'A trade agreement entirely unrelated to defense', 'A controversy unrelated to Cold War defense policy', 'New immigration quotas from the United States'], 0),
   ('The Bomarc missile controversy contributed to the fall of which prime minister’s government?', ['John Diefenbaker', 'Lester Pearson', 'A leader unrelated to this controversy', 'Pierre Trudeau'], 0),
   ('Why did the Bomarc missile controversy expose deep divisions within Canadian politics?', ['It raised difficult questions about Canadian sovereignty, nuclear weapons, and the country’s military relationship with the United States', 'This controversy had no connection to any political divisions', 'All Canadian politicians agreed completely on this issue', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians study the Bomarc missile crisis as part of Canada’s broader Cold War history?', ['It illustrates the pressures Canada faced in balancing its own sovereignty with its defense commitments to the United States during the Cold War', 'The Bomarc crisis has no connection to Canada’s Cold War history', 'Canada’s defense policy was never influenced by Cold War tensions', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(76, [
E('Literature: Frame Narratives and Nested Stories',
  'Grade 10 English strand: a frame narrative is a story structure in which one story is told within another, using an outer narrative to introduce, contextualize, or provide a lens for one or more inner stories.',
  [('A frame narrative is best described as a structure in which ___.', ['One story is told within another', 'Only a single storyline exists with no embedded stories', 'A concept unrelated to narrative structure', 'Every character narrates the exact same events identically'], 0),
   ('In a frame narrative, the outer story typically functions to ___.', ['Introduce, contextualize, or provide a lens for the inner story or stories', 'Have no relationship to the inner story at all', 'A function unrelated to frame narratives', 'Replace the need for an inner story entirely'], 0),
   ('Which is an example of how a frame narrative might be used?', ['A character recounting a past experience as a story within the main narrative', 'A story told entirely without any narrator', 'A technique unrelated to frame narratives', 'A single event described only once with no embedded structure'], 0),
   ('Why might an author use a frame narrative to explore a theme from multiple angles?', ['The relationship between the outer and inner stories can add layered perspectives or meaning to a shared theme', 'Frame narratives never provide any additional perspective on a theme', 'A reason unrelated to narrative structure', 'A frame narrative always simplifies a theme rather than layering it'], 0),
   ('Why can a frame narrative create suspense or curiosity about how the outer and inner stories connect?', ['Readers may wonder how the framing story relates to or is resolved by the story nested within it', 'Frame narratives never create any sense of suspense or curiosity', 'A reason unrelated to narrative technique', 'The outer and inner stories are always completely unrelated with no connection at all'], 0)]),
M('Algebra: Laws of Exponents and Rational Exponents',
  'Grade 10 Algebra strand (extension): the laws of exponents govern how expressions with powers are multiplied, divided, and simplified, and a rational exponent expresses a root, such as x^(1/2) representing the square root of x.',
  [('According to the product law of exponents, x^a multiplied by x^b equals ___.', ['x^(a+b)', 'x^(a times b)', 'An expression unrelated to the laws of exponents', 'x^(a-b)'], 0),
   ('A rational exponent such as x^(1/2) represents ___.', ['The square root of x', 'X multiplied by one-half', 'A concept unrelated to rational exponents', 'X raised to a negative power'], 0),
   ('According to the quotient law of exponents, x^a divided by x^b equals ___.', ['x^(a-b)', 'x^(a+b)', 'An expression unrelated to the laws of exponents', 'x^(a divided by b)'], 0),
   ('Why does raising a power to another power require multiplying the exponents, as in (x^a)^b = x^(ab)?', ['Raising a power to another power means repeating the multiplication of x^a a total of b times, which adds the exponent a to itself b times', 'Raising a power to another power always requires adding the exponents instead of multiplying them', 'A reason unrelated to the laws of exponents', 'This law only applies when a and b are both equal to one'], 0),
   ('Why are rational exponents useful for representing roots within algebraic expressions?', ['They allow roots to be manipulated using the same laws of exponents as whole-number powers', 'Rational exponents have no connection to roots or radicals', 'A reason unrelated to simplifying algebraic expressions', 'Roots can never be expressed using exponents of any kind'], 0)]),
Sc('Biology: Biodiversity and Conservation Strategies',
   'Grade 10 Biology strand: biodiversity refers to the variety of living organisms within an ecosystem, and conservation strategies, such as protected areas and species reintroduction programs, aim to maintain or restore that variety in the face of habitat loss and other threats.',
   [('Biodiversity refers to the ___ within an ecosystem.', ['Variety of living organisms', 'Total mass of a single dominant species', 'A concept unrelated to ecosystems', 'Amount of available sunlight only'], 0),
    ('Which of these is an example of a conservation strategy?', ['Establishing a protected area to preserve a habitat', 'Removing all protections from a natural habitat', 'A strategy unrelated to conservation', 'Deliberately introducing an invasive species to an ecosystem'], 0),
    ('Habitat loss is generally considered a ___ to biodiversity.', ['Threat', 'Benefit', 'A factor unrelated to biodiversity', 'A factor with no measurable effect on biodiversity'], 0),
    ('Why is high biodiversity generally considered beneficial to the overall stability of an ecosystem?', ['A greater variety of species can make an ecosystem more resilient to disturbances or environmental change', 'High biodiversity always makes an ecosystem less stable', 'A reason unrelated to ecosystem stability', 'Biodiversity has no connection to how an ecosystem responds to change'], 0),
    ('Why might a species reintroduction program be used as a conservation strategy?', ['It can help restore a species that has been lost from an ecosystem, supporting the ecosystem’s overall balance and function', 'Reintroduction programs have no effect on an ecosystem’s balance', 'A reason unrelated to conservation biology', 'Species that are lost from an ecosystem can never be reintroduced'], 0)]),
H('The Massey Commission and the Shaping of Canadian Culture',
  'Grade 10 History strand: the 1949-1951 Massey Commission investigated the state of arts, letters, and sciences in Canada, leading to recommendations that shaped the creation of institutions such as the Canada Council for the Arts to support Canadian cultural identity.',
  [('The Massey Commission conducted its investigation primarily during which years?', ['1949 to 1951', '1914 to 1916', '1929 to 1931', '1969 to 1971'], 0),
   ('The Massey Commission investigated the state of ___ in Canada.', ['Arts, letters, and sciences', 'Only military spending, with no connection to culture', 'A subject entirely unrelated to Canadian culture', 'Provincial boundaries and geography'], 0),
   ('Recommendations from the Massey Commission helped lead to the creation of ___.', ['The Canada Council for the Arts', 'An organization entirely unrelated to Canadian culture', 'The Canadian Armed Forces', 'A federal department focused only on agriculture'], 0),
   ('Why was the Massey Commission concerned about the influence of American media and culture on Canada?', ['Commissioners worried that a lack of support for Canadian arts and culture could weaken a distinct Canadian identity', 'The Massey Commission had no concerns about American cultural influence', 'This concern has no connection to Canadian cultural policy', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians consider the Massey Commission significant in the development of Canadian cultural policy?', ['It laid the groundwork for ongoing federal support of Canadian arts and culture that continues to shape national identity today', 'The Massey Commission had no lasting influence on Canadian cultural policy', 'Canadian cultural policy has never been shaped by federal government action', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(77, [
E('Oral Communication: Giving and Receiving Constructive Feedback',
  'Grade 10 English strand: constructive feedback offers specific, actionable observations intended to help a writer or speaker improve, balancing honest critique with respect and encouragement.',
  [('Constructive feedback is best described as feedback that is ___.', ['Specific, actionable, and intended to help someone improve', 'Vague and focused only on general praise with no detail', 'A concept unrelated to communication', 'Intended only to criticize without any purpose of improvement'], 0),
   ('Why is specificity important when giving feedback on a piece of writing?', ['Specific feedback helps the writer understand exactly what to revise and how to improve it', 'Vague feedback is always more helpful than specific feedback', 'A reason unrelated to giving effective feedback', 'Specificity has no effect on how useful feedback is'], 0),
   ('Which is an example of constructive feedback on a piece of writing?', ['Your introduction could more clearly state your main argument.', 'This is bad.', 'A comment unrelated to giving feedback', 'I have no comments at all.'], 0),
   ('Why might a peer feedback session use a structured format, such as identifying one strength and one area for improvement?', ['A structured format ensures feedback is balanced, focused, and useful for revision', 'Structured formats always make feedback less useful', 'A reason unrelated to peer feedback', 'Feedback sessions are more effective with no structure at all'], 0),
   ('Why is learning to receive feedback gracefully considered an important part of the writing process?', ['Being open to feedback allows a writer to revise and strengthen their work more effectively', 'Receiving feedback has no connection to improving a piece of writing', 'A reason unrelated to the writing process', 'Writers should always ignore any feedback they receive'], 0)]),
M('Vectors: The Dot Product and Applications',
  'Grade 10 Vectors strand (extension): the dot product combines two vectors to produce a single scalar value, calculated by multiplying corresponding components and summing the results, and can be used to determine the angle between two vectors.',
  [('The dot product of two vectors produces a ___.', ['Single scalar value', 'A new vector, with no connection to a scalar', 'A concept unrelated to vectors', 'A matrix, with no connection to scalars'], 0),
   ('The dot product of two vectors is calculated by ___.', ['Multiplying corresponding components and summing the results', 'Subtracting corresponding components from one another', 'A method unrelated to the dot product', 'Multiplying only the magnitudes of the two vectors, ignoring direction'], 0),
   ('If the dot product of two non-zero vectors equals zero, the vectors are ___.', ['Perpendicular to each other', 'Parallel to each other', 'A relationship unrelated to the dot product', 'Identical in both magnitude and direction'], 0),
   ('Why can the dot product be used to determine the angle between two vectors?', ['The dot product formula directly relates the vectors’ magnitudes and the cosine of the angle between them', 'The dot product has no connection to the angle between two vectors', 'A reason unrelated to vector operations', 'The angle between two vectors can never be calculated using any vector operation'], 0),
   ('Why is the dot product useful in real-world applications, such as calculating the work done by a force?', ['It captures how much one vector, like a force, acts in the direction of another, like displacement', 'The dot product has no real-world applications', 'A reason unrelated to vector operations', 'Work done by a force never involves any relationship between two vectors'], 0)]),
Sc('Physics: Simple Machines and Mechanical Advantage',
   'Grade 10 Physics strand: a simple machine, such as a lever or pulley, changes the direction or magnitude of an applied force, and mechanical advantage measures how much a machine multiplies an input force.',
   [('A simple machine changes the direction or magnitude of ___.', ['An applied force', 'The mass of an object, with no connection to force', 'A concept unrelated to simple machines', 'The colour of an object'], 0),
    ('Mechanical advantage measures how much a machine ___.', ['Multiplies an input force', 'Reduces the total energy in a system', 'A concept unrelated to mechanical advantage', 'Changes the temperature of an object'], 0),
    ('Which of these is an example of a simple machine?', ['A lever', 'A smartphone', 'A device unrelated to simple machines', 'A television'], 0),
    ('Why does using a lever allow a person to lift a heavier load with less applied force?', ['The lever multiplies the applied force by trading off distance, requiring the effort to move a greater distance than the load', 'A lever always requires the exact same amount of force as lifting the load directly', 'A reason unrelated to simple machines', 'Levers have no effect on the amount of force needed to lift a load'], 0),
    ('Why are simple machines considered fundamental to understanding more complex mechanical systems?', ['Complex machines are often built from combinations of simple machines working together', 'Simple machines have no connection to more complex mechanical systems', 'A reason unrelated to physics', 'Complex mechanical systems never rely on any simple machine principles'], 0)]),
H('Civics: How a Bill Becomes a Law in Canada',
  'Grade 10 Civics strand: a bill must pass through multiple stages in both the House of Commons and the Senate, including readings, committee review, and votes, before receiving royal assent and becoming law.',
  [('A bill must pass through multiple stages in which two bodies before becoming law?', ['The House of Commons and the Senate', 'Only the Supreme Court, with no connection to Parliament', 'A pair of bodies unrelated to the legislative process', 'Only a provincial legislature, with no federal involvement'], 0),
   ('Before becoming law, a bill must receive ___.', ['Royal assent', 'Approval from every province individually', 'A step unrelated to the legislative process', 'A public referendum vote'], 0),
   ('Committee review of a bill typically involves ___.', ['Detailed examination and possible amendments to the bill', 'An automatic, unquestioned approval with no examination', 'A step unrelated to the legislative process', 'The complete cancellation of the bill in every case'], 0),
   ('Why does a bill typically go through multiple readings in the House of Commons before becoming law?', ['Multiple readings allow for debate, scrutiny, and revision before a final decision is made', 'Multiple readings serve no purpose in the legislative process', 'A reason unrelated to how laws are made', 'A bill only ever requires a single reading with no further discussion'], 0),
   ('Why is understanding the legislative process considered an important part of Canadian civics education?', ['It helps citizens understand how laws affecting their lives are debated, revised, and ultimately passed', 'This knowledge has no relevance to being an informed citizen', 'The legislative process has no connection to laws that affect citizens', 'This topic has no relevance to understanding Canadian government'], 0)])]),

day(78, [
E('Reading: Analyzing Dialogue as Characterization',
  'Grade 10 English strand: dialogue reveals character through word choice, tone, and speech patterns, allowing readers to infer a character’s personality, background, and relationships without direct narrator description.',
  [('Dialogue can reveal character through a speaker’s ___.', ['Word choice, tone, and speech patterns', 'Physical appearance exclusively, with no connection to speech', 'A concept unrelated to characterization', 'Setting alone, with no connection to how a character speaks'], 0),
   ('Why might an author give two characters noticeably different speech patterns?', ['Distinct speech patterns can help distinguish their personalities, backgrounds, or social status', 'Speech patterns never provide any information about a character', 'A reason unrelated to characterization through dialogue', 'Every character in a story must speak in an identical way'], 0),
   ('Which is an example of how dialogue might reveal a character’s emotional state?', ['A character speaking in short, clipped sentences when they are angry or anxious', 'A character’s dialogue never changes based on their emotional state', 'A technique unrelated to characterization', 'Dialogue can only reveal a character’s physical location'], 0),
   ('Why is dialogue often considered a more subtle form of characterization than direct narrator description?', ['It allows readers to infer a character’s traits themselves, rather than being told directly by the narrator', 'Dialogue is always more direct and obvious than narrator description', 'A reason unrelated to characterization', 'Readers can never infer anything about a character from dialogue'], 0),
   ('Why might a character’s relationship with another character be revealed through their dialogue?', ['The way characters address or respond to one another can reflect the closeness, tension, or power dynamic between them', 'Dialogue never reveals anything about the relationship between two characters', 'A reason unrelated to characterization', 'Relationships between characters can only be shown through narration, never dialogue'], 0)]),
M('Polynomial Functions: Zeros, Factors, and End Behaviour',
  'Grade 10 Functions strand (extension): the zeros of a polynomial function are the x-values where the function equals zero, directly corresponding to its factors, and a polynomial’s degree and leading coefficient determine its end behaviour.',
  [('The zeros of a polynomial function are the x-values where the function’s output equals ___.', ['0', '1', 'A value unrelated to finding zeros', 'The function’s leading coefficient'], 0),
   ('If (x - 3) is a factor of a polynomial function, then the function must have a zero at ___.', ['x = 3', 'x = -3', 'A value unrelated to this factor', 'x = 0'], 0),
   ('The end behaviour of a polynomial function is primarily determined by its ___.', ['Degree and leading coefficient', 'Constant term only, with no connection to degree', 'A concept unrelated to polynomial functions', 'Y-intercept only, with no connection to degree'], 0),
   ('Why does an even-degree polynomial function with a positive leading coefficient rise on both ends of its graph?', ['As x approaches positive or negative infinity, an even power always produces a large positive result, multiplied by the positive coefficient', 'Even-degree polynomials always fall on both ends of the graph regardless of their leading coefficient', 'A reason unrelated to end behaviour', 'The leading coefficient has no effect on a polynomial’s end behaviour'], 0),
   ('Why is identifying the zeros and factors of a polynomial function useful for sketching its graph?', ['The zeros indicate where the graph crosses or touches the x-axis, helping outline the overall shape of the curve', 'Zeros and factors provide no useful information for graphing a polynomial function', 'A reason unrelated to polynomial functions', 'A polynomial’s graph can never be sketched using its zeros or factors'], 0)]),
Sc('Earth Science: Soil Formation and Land Use',
   'Grade 10 Earth Science strand: soil forms gradually through the weathering of rock and the accumulation of organic matter, and land use decisions, such as farming practices or urban development, can significantly affect soil health and erosion rates.',
   [('Soil forms gradually through the weathering of rock and the accumulation of ___.', ['Organic matter', 'Liquid water only, with no connection to organic matter', 'A concept unrelated to soil formation', 'Metal ore exclusively'], 0),
    ('Which of these is an example of a land use decision that could affect soil health?', ['Farming practices', 'The distance to the nearest ocean', 'A factor unrelated to land use', 'The average daily temperature of the sun'], 0),
    ('Soil formation is generally considered a ___ process.', ['Slow, gradual', 'Instantaneous', 'A process unrelated to soil formation', 'Process that reverses itself every day'], 0),
    ('Why can certain farming practices, such as leaving fields bare after harvest, increase the rate of soil erosion?', ['Without plant roots or cover to hold it in place, exposed soil is more easily carried away by wind or water', 'Bare soil is always more resistant to erosion than soil covered by plants', 'A reason unrelated to soil erosion', 'Farming practices have no connection to how quickly soil erodes'], 0),
    ('Why is understanding soil formation and land use important for sustainable agriculture?', ['Since soil forms so slowly, protecting it from excessive erosion or degradation is essential for long-term food production', 'Soil formation has no connection to agricultural sustainability', 'A reason unrelated to Earth Science', 'Soil erosion has no effect on a region’s ability to grow food over time'], 0)]),
H('Civics: The Canadian Electoral System',
  'Grade 10 Civics strand: Canada uses a first-past-the-post electoral system, in which the candidate who receives the most votes in a riding wins that seat, and the party that wins the most seats typically forms government.',
  [('Canada’s federal electoral system is generally described as ___.', ['First-past-the-post', 'Pure proportional representation', 'A system unrelated to Canadian elections', 'A system requiring a majority of 50 percent or more to win a riding'], 0),
   ('In a first-past-the-post system, the winning candidate in a riding is the one who receives ___.', ['The most votes, even without an outright majority', 'Exactly fifty percent of the vote', 'A result unrelated to this electoral system', 'The fewest votes among all candidates'], 0),
   ('The political party that wins the most seats in a federal election typically ___.', ['Forms government', 'Is automatically dissolved', 'A result unrelated to Canadian elections', 'Loses all further involvement in government'], 0),
   ('Why can a party sometimes form a majority government without winning a majority of the total popular vote nationwide?', ['Under first-past-the-post, seats are won riding by riding, so a party can win many ridings without needing an overall majority of votes', 'This outcome is impossible under Canada’s electoral system', 'A reason unrelated to Canada’s electoral system', 'A majority government always requires more than fifty percent of the national popular vote'], 0),
   ('Why is understanding the electoral system considered important for informed civic participation?', ['It helps citizens understand how their votes translate into political representation and government formation', 'The electoral system has no connection to civic participation', 'Understanding elections has no relevance to being an informed citizen', 'This topic has no relevance to understanding Canadian government'], 0)])]),

day(79, [
E('Grammar: Modifiers and Sentence Clarity',
  'Grade 10 English strand: a modifier describes, clarifies, or adds detail to another word in a sentence, and a misplaced or dangling modifier can create confusing or unintentionally humorous sentence meanings.',
  [('A modifier is best described as a word or phrase that ___.', ['Describes, clarifies, or adds detail to another word in a sentence', 'Always replaces the subject of a sentence entirely', 'A concept unrelated to sentence structure', 'Has no grammatical function within a sentence'], 0),
   ('A misplaced modifier occurs when ___.', ['A modifier is positioned so that it appears to describe the wrong word in a sentence', 'A sentence contains no modifiers at all', 'A concept unrelated to grammar', 'A modifier is placed directly next to the word it describes'], 0),
   ('Which of these sentences contains a misplaced modifier?', ['Running down the street, the bus was missed by Sam.', 'Sam missed the bus while running down the street.', 'A sentence unrelated to misplaced modifiers', 'While running down the street, Sam missed the bus.'], 0),
   ('Why can a dangling modifier create confusion for a reader?', ['It leaves unclear or implies an incorrect subject for the action being described', 'Dangling modifiers always make a sentence perfectly clear', 'A reason unrelated to sentence clarity', 'Dangling modifiers only ever occur in spoken language, never in writing'], 0),
   ('Why is revising for misplaced and dangling modifiers an important step in the editing process?', ['Correcting them ensures a sentence clearly communicates its intended meaning to the reader', 'This type of revision has no effect on a sentence’s clarity', 'A reason unrelated to the editing process', 'Misplaced modifiers never cause any confusion for a reader'], 0)]),
M('Geometry: Dilations and Scale Factor',
  'Grade 10 Geometry strand: a dilation is a transformation that resizes a figure proportionally from a fixed centre point, using a scale factor to determine whether the resulting image is enlarged or reduced.',
  [('A dilation is a transformation that ___.', ['Resizes a figure proportionally from a fixed centre point', 'Moves a figure without changing its size', 'A concept unrelated to geometric transformations', 'Reflects a figure across a line, with no change in size'], 0),
   ('If a dilation has a scale factor greater than 1, the resulting image is ___.', ['Enlarged', 'Reduced', 'A result unrelated to scale factor', 'Identical in size to the original figure'], 0),
   ('If a dilation has a scale factor between 0 and 1, the resulting image is ___.', ['Reduced', 'Enlarged', 'A result unrelated to scale factor', 'Reflected across the centre point'], 0),
   ('Why do the angles of a figure remain unchanged after a dilation, even though its side lengths change?', ['A dilation resizes a figure proportionally, preserving its overall shape and therefore its angle measures', 'Angles always change proportionally along with the side lengths during a dilation', 'A reason unrelated to dilations', 'Dilations never preserve any properties of the original figure'], 0),
   ('Why are dilations and scale factor useful concepts in real-world contexts, such as creating a scale model or a map?', ['They allow a real object to be proportionally resized while maintaining its accurate overall shape', 'Dilations and scale factor have no real-world modelling applications', 'A reason unrelated to geometric transformations', 'Scale models and maps never involve any proportional resizing of a real object'], 0)]),
Sc('Biology: Plant Structures and Transport Systems',
   'Grade 10 Biology strand: vascular plants use specialized tissues called xylem and phloem to transport water, minerals, and the products of photosynthesis throughout the plant.',
   [('Xylem tissue in a plant is primarily responsible for transporting ___.', ['Water and minerals', 'Only the products of photosynthesis, with no connection to water', 'A concept unrelated to plant transport systems', 'Oxygen exclusively, with no connection to water or minerals'], 0),
    ('Phloem tissue in a plant is primarily responsible for transporting ___.', ['The products of photosynthesis, such as sugars', 'Only water, with no connection to sugars', 'A concept unrelated to plant transport systems', 'Carbon dioxide exclusively'], 0),
    ('In most plants, water generally moves through the xylem in which direction?', ['Upward, from the roots toward the leaves', 'Downward, from the leaves toward the roots', 'A direction unrelated to xylem transport', 'Sideways only, with no vertical movement'], 0),
    ('Why is it useful for a plant to have two separate transport tissues, xylem and phloem, rather than just one?', ['Each tissue is specialized to move different substances, such as water versus sugars, often in different directions at once', 'Xylem and phloem always transport the exact same substances in the exact same direction', 'A reason unrelated to plant biology', 'Plants have no need to transport any substances internally'], 0),
    ('Why are xylem and phloem considered essential to the survival of tall vascular plants, like trees?', ['They allow water, nutrients, and sugars to be efficiently transported over long distances between the roots and the leaves', 'Xylem and phloem have no connection to how tall a plant can grow', 'A reason unrelated to plant biology', 'Tall plants have no need to transport water or nutrients internally'], 0)]),
H('Civics: Levels of Government — Federal, Provincial, and Municipal',
  'Grade 10 Civics strand: Canada’s system of government is divided into federal, provincial, and municipal levels, each responsible for distinct areas such as national defense, education and healthcare, and local services like garbage collection and zoning.',
  [('Canada’s system of government is divided into which three levels?', ['Federal, provincial, and municipal', 'Executive, legislative, and judicial only, with no connection to jurisdiction', 'A set of levels unrelated to Canadian government', 'National, international, and local only'], 0),
   ('Which level of government is typically responsible for national defense?', ['Federal', 'Provincial', 'A level unrelated to this responsibility', 'Municipal'], 0),
   ('Which level of government is typically responsible for local services like garbage collection and zoning?', ['Municipal', 'Federal', 'A level unrelated to this responsibility', 'An international governing body'], 0),
   ('Why are education and healthcare typically managed primarily at the provincial level in Canada?', ['Canada’s constitution assigns these areas of responsibility to provincial governments rather than the federal government', 'Education and healthcare are always managed exclusively at the federal level', 'A reason unrelated to how Canadian government responsibilities are divided', 'The provincial level of government has no defined responsibilities'], 0),
   ('Why is understanding the division of responsibilities across levels of government important for Canadian citizens?', ['It helps citizens know which level of government to contact or hold accountable for a specific issue', 'This division of responsibilities has no relevance to Canadian citizens', 'All levels of government are responsible for identical issues', 'This topic has no relevance to understanding Canadian civics'], 0)])]),

day(80, [
E('Review: Narrative Technique, Style, and Professional Writing',
  'Grade 10 English strand: this review lesson revisits the unreliable narrator, motif and recurring imagery, sentence fragments and run-ons, diction and tone, the cover letter and resume, frame narratives, constructive feedback, dialogue as characterization, and modifiers covered across Days 71-79.',
  [('An unreliable narrator is best described as a narrator whose ___.', ['Credibility or accuracy is compromised in some way', 'Account is always completely accurate and objective', 'A concept unrelated to narrative point of view', 'Only appears in non-fiction texts, never in fiction'], 0),
   ('A motif is best described as a recurring ___.', ['Element, image, or idea that appears throughout a text', 'Character who appears only once in a story', 'A concept unrelated to literary analysis', 'Setting that changes completely with every scene'], 0),
   ('A resume is best described as a document that ___.', ['Summarizes a candidate’s skills, education, and experience in a clear, organized format', 'Tells a detailed personal story with no organization', 'A concept unrelated to professional writing', 'Is always written in the same format as a cover letter'], 0),
   ('Dialogue can reveal character through a speaker’s ___.', ['Word choice, tone, and speech patterns', 'Physical appearance exclusively, with no connection to speech', 'A concept unrelated to characterization', 'Setting alone, with no connection to how a character speaks'], 0),
   ('Why is it useful to review these varied narrative and professional writing skills together?', ['It reinforces how narrative technique, style, and clear communication all shape effective writing', 'These topics have no connection to each other', 'Review is never useful in English studies', 'Each topic must be studied with no connection to the others'], 0)]),
M('Review: Discriminants, Variation, Finance, and Vectors',
  'Grade 10 Math strand review: this lesson revisits the discriminant, direct and partial variation, compound interest, angle of elevation and depression, the three-dimensional Pythagorean theorem, laws of exponents, the dot product, polynomial zeros and factors, and dilations covered across Days 71-79.',
  [('The discriminant of a quadratic equation is calculated using the expression ___.', ['b² - 4ac', 'b² + 4ac', 'An expression unrelated to the discriminant', '-b divided by 2a'], 0),
   ('Direct variation describes a relationship expressed in the form ___.', ['y = kx', 'y = kx + b', 'An expression unrelated to direct variation', 'y = k divided by x'], 0),
   ('Compound interest is calculated based on ___.', ['Both the initial principal and the accumulated interest from previous periods', 'Only the initial principal, with no connection to accumulated interest', 'A concept unrelated to interest calculations', 'A fixed amount that never changes over time'], 0),
   ('If the dot product of two non-zero vectors equals zero, the vectors are ___.', ['Perpendicular to each other', 'Parallel to each other', 'A relationship unrelated to the dot product', 'Identical in both magnitude and direction'], 0),
   ('Why is it valuable to review these connected mathematical concepts together?', ['It reinforces how these skills build on and relate to one another', 'These concepts have no connection to each other', 'Review is never useful in math', 'Each concept must be understood with no connection to the others'], 0)]),
Sc('Review: Periodic Trends, Body Systems, Energy, and Earth Resources',
   'Grade 10 Science strand review: this lesson revisits periodic trends, the circulatory and respiratory systems, static electricity, renewable and non-renewable energy resources, empirical and molecular formulas, biodiversity and conservation, simple machines, soil formation, and xylem and phloem covered across Days 71-79.',
   [('As you move from left to right across a period, atomic radius generally ___.', ['Decreases', 'Increases', 'A trend unrelated to atomic radius', 'Stays exactly the same'], 0),
    ('The circulatory system primarily transports oxygen, nutrients, and waste using the heart and ___.', ['Blood vessels', 'Lungs exclusively, with no connection to blood vessels', 'A structure unrelated to circulation', 'Digestive organs only, with no connection to blood'], 0),
    ('Renewable energy resources are best described as resources that ___.', ['Can be replenished naturally within a short time frame', 'Take millions of years to form', 'A concept unrelated to energy resources', 'Can never be replenished under any circumstances'], 0),
    ('Mechanical advantage measures how much a machine ___.', ['Multiplies an input force', 'Reduces the total energy in a system', 'A concept unrelated to mechanical advantage', 'Changes the temperature of an object'], 0),
    ('Why is it valuable to review these connected science concepts together?', ['It reinforces how these scientific ideas relate to and build on one another', 'These concepts have no connection to each other', 'Review is never useful at the end of a unit', 'Each concept must be understood with no connection to the others'], 0)]),
H('Review: The World Wars, Autonomy, and Canadian Civics',
  'Grade 10 History strand review: this lesson revisits Canada and the First World War, the Conscription Crisis, the Chanak Affair and Statute of Westminster, the Spanish Flu pandemic, the Bomarc missile crisis, the Massey Commission, and how bills, elections, and levels of government function, covered across Days 71-79.',
  [('Canada entered the First World War in which year?', ['1914', '1917', '1929', '1939'], 0),
   ('The Conscription Crisis took place in which year?', ['1917', '1929', '1945', '1962'], 0),
   ('The Statute of Westminster was passed in which year?', ['1931', '1922', '1914', '1945'], 0),
   ('Canada’s federal electoral system is generally described as ___.', ['First-past-the-post', 'Pure proportional representation', 'A system unrelated to Canadian elections', 'A system requiring a majority of 50 percent or more to win a riding'], 0),
   ('Why is it valuable to review these connected developments in Canadian history and civics together?', ['It reinforces how policy, autonomy, and civic structures have interacted throughout Canadian history', 'These events have no meaningful connections to each other', 'Review is never useful in history', 'Each event must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260908):
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
    _rebalance_answer_positions(g10_71_80)
    append_to(10, g10_71_80)
