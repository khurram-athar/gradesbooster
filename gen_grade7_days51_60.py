#!/usr/bin/env python3
"""Phase 3 extension: Grade 7, Days 51-60 (first batch past the Day 50
milestone, pushing toward the full 157-day year). Topics chosen to
avoid any overlap with the existing Day 1-50 set (see
data/grade7.json): close reading, polynomials, Newton's Laws, and the
League of Nations through the Arab Spring.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science & Technology',
    'TVO Learn: Grade 7 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L7, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M7, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S7, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS7, q)


g7_51_60 = [
day(51, [
L('Reading: Close Reading Strategies for Complex Texts',
  'Grade 7 Language strand: close reading involves carefully rereading a text, annotating key details, and analyzing specific word choices to build a deeper understanding of challenging material.',
  [('Close reading involves ___.', ['Carefully rereading a text and analyzing specific details', 'Reading a text only once, as quickly as possible', 'A concept unrelated to reading', 'Skipping difficult sections of a text entirely'], 0),
   ('Why might a reader annotate a text while close reading?', ['To track important details, questions, and reactions as they read', 'Annotating never helps a reader understand a text', 'A reason unrelated to close reading', 'Annotations always distract from understanding a text'], 0),
   ('Why is close reading especially useful for complex or challenging texts?', ['It helps break down difficult ideas into smaller, more manageable parts', 'Complex texts never benefit from careful, repeated reading', 'A reason unrelated to close reading', 'Close reading only works for simple, easy texts'], 0),
   ('Which is an example of a close reading strategy?', ['Rereading a confusing paragraph and noting unfamiliar vocabulary', 'Reading only the title of a text and nothing else', 'A concept unrelated to close reading', 'Ignoring any words that are difficult to understand'], 0),
   ('Why might a reader reread a text multiple times during close reading?', ['Each rereading can reveal new details or deepen understanding', 'Rereading a text is never useful for understanding it', 'A reason unrelated to close reading', 'A single reading always reveals everything about a text'], 0)]),
M('Solving and Graphing Inequalities on a Number Line',
  'Grade 7 Math strand: solving an inequality finds the range of values that make it true, and graphing it on a number line uses an open or closed circle and an arrow to show that range.',
  [('Solving an inequality finds ___.', ['A range of values that make the statement true', 'A single exact value that makes the statement true', 'A concept unrelated to inequalities', 'No values at all that satisfy the statement'], 0),
   ('On a number line, an open circle at a point means ___.', ['That value is not included in the solution', 'That value is included in the solution', 'A concept unrelated to graphing inequalities', 'The graph has no solution at all'], 0),
   ('On a number line, a closed (filled-in) circle at a point means ___.', ['That value is included in the solution', 'That value is not included in the solution', 'A concept unrelated to graphing inequalities', 'The inequality has no solution'], 0),
   ('If x ≥ 4, which type of circle would be used at 4 on the number line?', ['A closed (filled-in) circle', 'An open circle', 'A circle unrelated to this inequality', 'No circle would be used at all'], 0),
   ('Solve for x: 2x < 10.', ['x < 5', 'x < 12', 'A solution unrelated to the inequality', 'x < 20'], 0)]),
Sc('Newton’s Laws of Motion (Intro)',
   'Grade 7 Science strand: Newton’s three laws of motion describe how objects behave when forces act on them, including inertia, the relationship between force and acceleration, and action-reaction pairs.',
   [('Newton’s first law of motion describes ___.', ['Inertia -- an object’s tendency to resist changes in motion', 'The relationship between force and colour', 'A concept unrelated to Newton’s laws', 'The speed of light in a vacuum'], 0),
    ('Newton’s second law of motion relates ___.', ['Force, mass, and acceleration', 'Only the temperature of an object', 'A concept unrelated to Newton’s laws', 'The volume and density of an object'], 0),
    ('Newton’s third law of motion states that ___.', ['For every action, there is an equal and opposite reaction', 'Objects in motion always eventually speed up on their own', 'A concept unrelated to Newton’s laws', 'Forces never have any reaction at all'], 0),
    ('Which is an example of Newton’s third law in action?', ['A swimmer pushing water backward to move forward', 'A ball sitting still on a table with no forces acting on it', 'A concept unrelated to Newton’s laws', 'An object that never interacts with any other object'], 0),
    ('Why are Newton’s laws considered fundamental to understanding motion?', ['They explain how and why objects move or stay still under different forces', 'These laws have no connection to how objects move', 'A reason unrelated to physics', 'Newton’s laws only apply to objects in outer space'], 0)]),
SS('The League of Nations and Its Legacy',
   'Grade 7 Social Studies strand: the League of Nations was an international organization formed after World War I to promote peace and cooperation between countries, though it ultimately struggled to prevent future conflict.',
   [('The League of Nations was formed after ___.', ['World War I', 'World War II', 'A conflict unrelated to the League of Nations', 'The Cold War'], 0),
    ('The main goal of the League of Nations was to ___.', ['Promote peace and cooperation between countries', 'Encourage new wars between member countries', 'A concept unrelated to the League of Nations', 'End all international trade'], 0),
    ('Which of these contributed to the League of Nations’ struggles?', ['It lacked the power to enforce its decisions on member countries', 'Every country in the world immediately joined and fully supported it', 'A reason unrelated to the League of Nations', 'It had no connection to preventing conflict'], 0),
    ('Why is the League of Nations often discussed alongside the later United Nations?', ['The League’s shortcomings influenced the design of the UN as its successor organization', 'The League of Nations and the United Nations have no historical connection', 'A reason unrelated to international organizations', 'The United Nations was formed long before the League of Nations'], 0),
    ('Why do historians study the League of Nations today?', ['It offers important lessons about the challenges of international cooperation', 'The League of Nations has no relevance to understanding global history', 'A reason unrelated to social studies learning', 'It successfully prevented all future global conflicts'], 0)])]),
day(52, [
L('Grammar: Parallel Structure in Complex Sentences',
  'Grade 7 Language strand: parallel structure in complex sentences means keeping grammatically similar elements consistent, even across clauses joined by conjunctions like “although” or “because.”',
  [('Parallel structure means keeping grammatically similar elements ___.', ['Consistent throughout a sentence', 'Different from one another throughout a sentence', 'A concept unrelated to grammar', 'Randomly varied with no consistent pattern'], 0),
   ('Which sentence uses correct parallel structure?', ['She enjoys hiking, biking, and swimming.', 'She enjoys hiking, to bike, and swimming.', 'A sentence unrelated to parallel structure', 'She enjoys hiking, biking, and to swim.'], 0),
   ('Which sentence uses correct parallel structure in a complex sentence?', ['Although he was tired, he finished his homework and cleaned his room.', 'Although he was tired, he finished his homework and was cleaning his room.', 'A sentence unrelated to parallel structure', 'Although being tired, he finished his homework and cleaned his room.'], 0),
   ('Why is parallel structure especially important in complex sentences with multiple clauses?', ['It keeps the sentence clear and grammatically consistent despite its added complexity', 'Complex sentences never need to follow consistent grammatical patterns', 'A reason unrelated to grammar', 'Parallel structure only matters in short, simple sentences'], 0),
   ('Which phrase breaks parallel structure?', ['“running, jumping, and to climb”', '“running, jumping, and climbing”', 'A phrase unrelated to parallel structure', '“to run, to jump, and to climb”'], 0)]),
M('Polynomials: Introduction to Terms and Like Terms',
  'Grade 7 Math strand: a polynomial is an expression made up of terms combined with addition or subtraction, and like terms have the same variable raised to the same power and can be combined.',
  [('A polynomial is an expression made up of ___.', ['Terms combined using addition or subtraction', 'Only a single number with no variables', 'A concept unrelated to polynomials', 'Terms that can never be combined in any way'], 0),
   ('Like terms have ___.', ['The same variable raised to the same power', 'Completely different variables from one another', 'A concept unrelated to like terms', 'No connection to variables at all'], 0),
   ('Which of these are like terms?', ['3x and 7x', '3x and 7y', 'Terms unrelated to this concept', '3x and 7x²'], 0),
   ('Simplify: 4x + 3x.', ['7x', '12x', 'A value unrelated to the calculation', '7x²'], 0),
   ('Why can 5y and 5y² not be combined as like terms?', ['They have the same variable but different exponents', 'They have completely different variables', 'A reason unrelated to like terms', 'Terms can never be combined under any circumstances'], 0)]),
Sc('The Water Cycle and Its Connection to Climate',
   'Grade 7 Science strand: the water cycle describes how water moves through evaporation, condensation, and precipitation, and it plays a key role in shaping regional and global climate patterns.',
   [('The water cycle includes the processes of ___.', ['Evaporation, condensation, and precipitation', 'Only freezing, with no other processes involved', 'A concept unrelated to the water cycle', 'A single process that never repeats'], 0),
    ('Evaporation occurs when ___.', ['Water changes from a liquid into a gas', 'Water changes from a gas into a liquid', 'A process unrelated to evaporation', 'Water changes directly into a solid'], 0),
    ('Condensation occurs when ___.', ['Water vapour changes into liquid water droplets', 'Liquid water changes into water vapour', 'A process unrelated to condensation', 'Water changes directly into ice'], 0),
    ('How does the water cycle influence regional climate?', ['It affects patterns of rainfall, humidity, and temperature in different regions', 'The water cycle has no connection to climate at all', 'A reason unrelated to the water cycle', 'Climate is determined with no involvement from water at all'], 0),
    ('Why might scientists study changes in the water cycle when studying climate change?', ['Shifts in evaporation and precipitation patterns can signal broader climate changes', 'The water cycle has no connection to climate change', 'A reason unrelated to environmental science', 'The water cycle never changes over time'], 0)]),
SS('Canada’s Immigration Policy: Historical Changes',
   'Grade 7 Social Studies strand: Canada’s immigration policy has changed significantly over time, shifting from restrictive and discriminatory practices to a points-based system aimed at welcoming diverse newcomers.',
   [('Canada’s early immigration policies were often ___.', ['Restrictive and discriminatory toward certain groups', 'Completely open to every immigrant with no restrictions at all', 'A concept unrelated to Canada’s immigration history', 'Focused only on welcoming immigrants from every country equally'], 0),
    ('Canada’s modern immigration system often uses ___.', ['A points-based system considering factors like skills and education', 'A system that considers no criteria at all', 'A concept unrelated to immigration policy', 'A system that only accepts immigrants from a single country'], 0),
    ('Why might a country change its immigration policies over time?', ['Economic needs, social values, and global events can all influence policy changes', 'Immigration policies never change once they are established', 'A reason unrelated to immigration policy', 'Policy changes have no connection to a country’s needs or values'], 0),
    ('Why is it important to study the history of Canada’s immigration policy?', ['It helps explain how Canada’s population and society have developed and changed', 'This history has no connection to understanding Canada today', 'A reason unrelated to social studies learning', 'Immigration policy has remained exactly the same throughout Canadian history'], 0),
    ('Which of these reflects a shift toward more inclusive immigration policy?', ['Removing restrictions based on a person’s country of origin', 'Adding new restrictions based on a person’s country of origin', 'A concept unrelated to immigration policy', 'Closing Canada’s borders to all immigration entirely'], 0)])]),
day(53, [
L('Writing: Writing a Compare and Contrast Essay',
  'Grade 7 Language strand: a compare and contrast essay examines the similarities and differences between two subjects, often organized point-by-point or subject-by-subject.',
  [('A compare and contrast essay examines ___.', ['The similarities and differences between two subjects', 'Only the differences, never any similarities', 'A concept unrelated to writing', 'A single subject with no comparison at all'], 0),
   ('In a point-by-point structure, a writer organizes the essay by ___.', ['Discussing one point of comparison at a time for both subjects', 'Discussing all of one subject, then all of the other subject', 'A concept unrelated to essay structure', 'Randomly mixing ideas with no clear organization'], 0),
   ('In a subject-by-subject structure, a writer organizes the essay by ___.', ['Discussing all of one subject, then all of the other subject', 'Discussing one point of comparison at a time for both subjects', 'A concept unrelated to essay structure', 'Avoiding any clear structure altogether'], 0),
   ('Which transition word might signal a similarity in a compare and contrast essay?', ['Similarly', 'However', 'A word unrelated to signaling similarity', 'Although'], 0),
   ('Why might a writer choose to compare and contrast two subjects in an essay?', ['To help readers understand each subject more clearly through comparison', 'Comparing subjects never adds any value to an essay', 'A reason unrelated to writing', 'To avoid discussing either subject in any detail'], 0)]),
M('The Pythagorean Theorem: Applications',
  'Grade 7 Math strand: the Pythagorean theorem (a² + b² = c²) can be applied to real-world problems, such as finding the shortest distance across a rectangular field or checking whether a corner is a right angle.',
  [('The Pythagorean theorem states that ___.', ['a² + b² = c², where c is the hypotenuse of a right triangle', 'a + b = c for any triangle', 'A formula unrelated to the Pythagorean theorem', 'a² - b² = c² for any triangle'], 0),
   ('If a right triangle has legs of 3 and 4, what is the length of the hypotenuse?', ['5', '7', 'A value unrelated to the calculation', '12'], 0),
   ('If a right triangle has legs of 6 and 8, what is the length of the hypotenuse?', ['10', '14', 'A value unrelated to the calculation', '48'], 0),
   ('Which of these is a real-world application of the Pythagorean theorem?', ['Finding the shortest diagonal distance across a rectangular field', 'Measuring the temperature of a room', 'A concept unrelated to the Pythagorean theorem', 'Finding the average of a set of numbers'], 0),
   ('The Pythagorean theorem can only be applied to a triangle that is ___.', ['A right triangle', 'An equilateral triangle', 'A type of triangle unrelated to this theorem', 'Any triangle with no specific requirements'], 0)]),
Sc('Sound Waves: Pitch, Volume, and Frequency',
   'Grade 7 Science strand: sound travels as waves, and its pitch is determined by frequency (how many vibrations per second) while its volume is determined by amplitude (the size of the vibration).',
   [('Pitch is determined by ___.', ['Frequency, or how many vibrations occur per second', 'The colour of the sound wave', 'A concept unrelated to pitch', 'The distance the sound has travelled'], 0),
    ('Volume is determined by ___.', ['Amplitude, or the size of the vibration', 'Frequency, or how many vibrations occur per second', 'A concept unrelated to volume', 'The temperature of the surrounding air'], 0),
    ('A higher frequency sound wave produces a ___ pitch.', ['Higher', 'Lower', 'A pitch unrelated to frequency', 'Silent'], 0),
    ('A larger amplitude sound wave produces a ___ volume.', ['Louder', 'Quieter', 'A volume unrelated to amplitude', 'Silent'], 0),
    ('Why might a small object, like a whistle, tend to produce a higher pitch than a large object, like a tuba?', ['Smaller objects generally vibrate at higher frequencies than larger objects', 'Object size has no connection to the pitch it produces', 'A reason unrelated to sound waves', 'Larger objects always produce higher pitches than smaller ones'], 0)]),
SS('The Marshall Plan and European Reconstruction',
   'Grade 7 Social Studies strand: the Marshall Plan was a large-scale American aid program launched after World War II to help rebuild the economies of war-torn European countries.',
   [('The Marshall Plan was launched to help ___.', ['Rebuild the economies of war-torn European countries after World War II', 'Start a new conflict in Europe', 'A concept unrelated to the Marshall Plan', 'End all trade between European nations'], 0),
    ('The Marshall Plan primarily provided European countries with ___.', ['Economic aid', 'Military weapons only, with no economic support', 'A type of support unrelated to the Marshall Plan', 'No support of any kind'], 0),
    ('Why might economic aid have been especially important for Europe after World War II?', ['Many countries faced widespread destruction and needed support to rebuild', 'European countries faced no economic challenges after the war', 'A reason unrelated to post-war reconstruction', 'Economic aid had no effect on rebuilding efforts'], 0),
    ('Which country launched the Marshall Plan?', ['The United States', 'A country unrelated to the Marshall Plan', 'Canada', 'A country that no longer exists today'], 0),
    ('Why is the Marshall Plan still studied as an example of international cooperation?', ['It shows how aid can help rebuild economies and stability after a major conflict', 'The Marshall Plan had no lasting effect on Europe’s recovery', 'A reason unrelated to its historical significance', 'It focused only on military strategy, with no economic component'], 0)])]),
day(54, [
L('Vocabulary: Analogies and Word Relationships',
  'Grade 7 Language strand: an analogy compares two pairs of words that share a similar relationship, such as synonym, antonym, cause-and-effect, or part-to-whole relationships.',
  [('An analogy compares two pairs of words that share a ___.', ['Similar relationship', 'Completely unrelated meaning', 'A concept unrelated to analogies', 'Identical spelling pattern'], 0),
   ('Complete the analogy: Petal is to flower as page is to ___.', ['Book', 'Pencil', 'A word unrelated to the analogy', 'Sky'], 0),
   ('What relationship does the analogy “spark is to fire as seed is to plant” show?', ['Cause and effect', 'Synonyms', 'A relationship unrelated to analogies', 'Antonyms'], 0),
   ('Complete the analogy: Enormous is to huge as tiny is to ___.', ['Small', 'Gigantic', 'A word unrelated to the analogy', 'Loud'], 0),
   ('Why are analogies a useful vocabulary tool?', ['They help build understanding of relationships between words and concepts', 'Analogies never help with understanding vocabulary', 'A concept unrelated to vocabulary building', 'Analogies only apply to numbers, not words'], 0)]),
M('Volume and Surface Area of Spheres (Intro)',
  'Grade 7 Math strand: the volume of a sphere is found using the formula (4/3)πr³, and its surface area is found using the formula 4πr², where r is the radius.',
  [('The formula for the volume of a sphere is ___.', ['(4/3)πr³', 'πr²', 'A formula unrelated to the volume of a sphere', '2πr'], 0),
   ('The formula for the surface area of a sphere is ___.', ['4πr²', '(4/3)πr³', 'A formula unrelated to the surface area of a sphere', 'πr²'], 0),
   ('In the sphere formulas, what does “r” represent?', ['The radius of the sphere', 'The diameter of the sphere', 'A value unrelated to spheres', 'The circumference of the sphere'], 0),
   ('If a sphere has a radius of 3, what is its approximate volume using π ≈ 3.14?', ['About 113.04 cubic units', 'About 28.26 cubic units', 'A value unrelated to the calculation', 'About 9 cubic units'], 0),
   ('Why might understanding the volume of a sphere be useful in real life?', ['It helps calculate the capacity of round objects, like balls or tanks', 'Sphere volume calculations have no real-world use', 'A reason unrelated to spheres', 'Spheres never have a measurable volume'], 0)]),
Sc('Structures: Load, Stress, and Material Strength',
   'Grade 7 Science strand: a structure must withstand different types of load and stress, and engineers select materials based on their strength, flexibility, and ability to resist these forces.',
   [('Load refers to ___.', ['The weight or force a structure must support', 'The colour of a structure’s materials', 'A concept unrelated to structures', 'The height of a structure alone'], 0),
    ('Stress in a structure refers to ___.', ['The internal force experienced by a material under load', 'The external appearance of a structure', 'A concept unrelated to structures', 'A structure with no forces acting on it at all'], 0),
    ('Why might an engineer choose a flexible material for a structure in an earthquake-prone area?', ['Flexible materials can absorb and withstand shifting forces without breaking', 'Flexibility has no connection to how a structure performs in an earthquake', 'A reason unrelated to materials engineering', 'Rigid materials are always safer in earthquake-prone areas'], 0),
    ('Which of these is an example of a structure experiencing load?', ['A bridge supporting the weight of passing vehicles', 'A structure with nothing resting on or pushing against it', 'A concept unrelated to load', 'A material with no connection to forces at all'], 0),
    ('Why do engineers test the strength of materials before building a structure?', ['To ensure the materials can safely support the expected loads and stresses', 'Testing materials provides no useful information for construction', 'A reason unrelated to engineering', 'Materials never need to be tested before use'], 0)]),
SS('Decolonization in Africa: An Overview',
   'Grade 7 Social Studies strand: decolonization in Africa refers to the process, largely occurring in the mid-20th century, by which African nations gained independence from European colonial powers.',
   [('Decolonization in Africa refers to the process by which ___.', ['African nations gained independence from European colonial powers', 'European powers expanded their control over African nations', 'A concept unrelated to decolonization', 'African nations became colonies for the first time'], 0),
    ('Decolonization in Africa largely occurred during ___.', ['The mid-20th century', 'The 1500s', 'A time period unrelated to decolonization in Africa', 'Ancient times, thousands of years ago'], 0),
    ('Which of these was a common challenge many newly independent African nations faced?', ['Building new governments and economies after colonial rule', 'Having no challenges at all after gaining independence', 'A reason unrelated to decolonization', 'Remaining under colonial control indefinitely'], 0),
    ('Why is the history of decolonization in Africa significant to study?', ['It helps explain the political and economic landscape of many African nations today', 'This history has no connection to understanding the world today', 'A reason unrelated to social studies learning', 'Decolonization in Africa never actually took place'], 0),
    ('Which of these best describes the goal of independence movements in Africa?', ['Achieving self-governance and freedom from colonial rule', 'Strengthening colonial control over African nations', 'A concept unrelated to independence movements', 'Preventing any future political change in the region'], 0)])]),
day(55, [
L('Reading: Analyzing Flashback and Foreshadowing Together',
  'Grade 7 Language strand: flashback interrupts a story to show a past event, while foreshadowing hints at a future event, and authors often use both techniques together to build a richer narrative.',
  [('A flashback interrupts a story to show ___.', ['A past event', 'A future event', 'A concept unrelated to narrative techniques', 'An event happening in the present moment only'], 0),
   ('Foreshadowing hints at ___.', ['A future event in the story', 'A past event in the story', 'A concept unrelated to narrative techniques', 'An event that has no connection to the plot'], 0),
   ('Why might an author use both flashback and foreshadowing in the same story?', ['To build a richer narrative that connects past, present, and future events', 'These two techniques can never be used together', 'A reason unrelated to narrative structure', 'To confuse the reader with no clear purpose'], 0),
   ('Which is an example of a flashback?', ['A character suddenly remembering an event from years earlier', 'A character noticing dark clouds before a coming storm', 'A concept unrelated to flashback', 'A character describing their current surroundings'], 0),
   ('How might recognizing flashback and foreshadowing improve a reader’s understanding of a story?', ['It helps reveal how the past, present, and future connect within the narrative', 'These techniques never affect how a reader understands a story', 'A reason unrelated to reading comprehension', 'Recognizing these techniques makes a story harder to understand'], 0)]),
M('Ratio and Rate Problems with Multiple Steps',
  'Grade 7 Math strand: multi-step ratio and rate problems require combining several calculations, such as finding a unit rate and then using it to solve for a larger or smaller quantity.',
  [('A multi-step ratio problem often requires ___.', ['Combining several calculations to reach a final answer', 'Only a single calculation with no additional steps', 'A concept unrelated to ratio problems', 'Ignoring the given ratio entirely'], 0),
   ('If a car travels 150 km in 3 hours, what is its unit rate in km per hour?', ['50 km/h', '450 km/h', 'A rate unrelated to the calculation', '3 km/h'], 0),
   ('If a recipe uses a ratio of 2 cups of flour for every 3 cups of sugar, how many cups of flour are needed for 9 cups of sugar?', ['6 cups', '9 cups', 'An amount unrelated to the ratio', '13.5 cups'], 0),
   ('If 5 workers can build a fence in 10 hours, how many hours would it take 10 workers, assuming the same rate per worker?', ['5 hours', '20 hours', 'A value unrelated to the calculation', '10 hours'], 0),
   ('Why are multi-step ratio problems useful to practice?', ['They build skills for solving more complex, real-world proportional situations', 'Multi-step ratio problems have no practical use', 'A reason unrelated to ratio problems', 'They only apply to problems with a single possible step'], 0)]),
Sc('The Digestive System in Depth',
   'Grade 7 Science strand: the digestive system breaks down food into nutrients the body can absorb and use, involving organs such as the stomach, small intestine, and large intestine.',
   [('The main function of the digestive system is to ___.', ['Break down food into nutrients the body can absorb and use', 'Pump blood throughout the body', 'A function unrelated to the digestive system', 'Filter air before it reaches the lungs'], 0),
    ('Which organ is primarily responsible for breaking down food using acid and enzymes?', ['The stomach', 'The heart', 'An organ unrelated to digestion', 'The lungs'], 0),
    ('The small intestine plays a key role in ___.', ['Absorbing nutrients into the bloodstream', 'Pumping blood to the rest of the body', 'A role unrelated to the small intestine', 'Filtering air for the lungs'], 0),
    ('The large intestine mainly functions to ___.', ['Absorb water and form waste for elimination', 'Break food down using stomach acid', 'A function unrelated to the large intestine', 'Pump oxygen throughout the body'], 0),
    ('Why is the digestive system considered essential for overall health?', ['It provides the body with the nutrients and energy needed to function', 'The digestive system has no connection to the body’s overall health', 'A reason unrelated to biology', 'The body can function normally with no digestive system at all'], 0)]),
SS('The Non-Aligned Movement During the Cold War',
   'Grade 7 Social Studies strand: the Non-Aligned Movement was a group of countries during the Cold War that chose not to formally align with either the United States or the Soviet Union.',
   [('The Non-Aligned Movement was made up of countries that chose not to ___.', ['Formally align with either the United States or the Soviet Union', 'Participate in any international organizations at all', 'A concept unrelated to the Non-Aligned Movement', 'Communicate with any other countries during the Cold War'], 0),
    ('Why might a country have chosen to join the Non-Aligned Movement?', ['To maintain independence from the two major Cold War powers', 'To become fully controlled by one of the two major powers', 'A reason unrelated to the Non-Aligned Movement', 'Joining provided no benefit to member countries at all'], 0),
    ('The Cold War was primarily a period of tension between ___.', ['The United States and the Soviet Union', 'Canada and the United States', 'Two countries unrelated to the Cold War', 'Every country in the world equally'], 0),
    ('Why is the Non-Aligned Movement an important part of Cold War history?', ['It shows that many countries sought an independent path rather than choosing a side', 'It shows that every country in the world was forced to pick a side', 'A reason unrelated to Cold War history', 'The Non-Aligned Movement had no real impact on world history'], 0),
    ('Which of these best describes the overall goal of the Non-Aligned Movement?', ['Pursuing an independent path in international relations', 'Strengthening one side of the Cold War over the other', 'A concept unrelated to the Non-Aligned Movement', 'Ending all international cooperation between countries'], 0)])]),
day(56, [
L('Media Literacy: Evaluating Online Sources for Credibility',
  'Grade 7 Language strand: evaluating an online source for credibility involves checking its author, publication date, purpose, and whether its claims are supported by reliable evidence.',
  [('Evaluating an online source for credibility involves checking its ___.', ['Author, publication date, purpose, and supporting evidence', 'Font style and background colour only', 'A concept unrelated to media literacy', 'Number of images used on the page'], 0),
   ('Why is it important to check who authored an online source?', ['It helps determine whether the author has relevant expertise or potential bias', 'The author of a source never affects its credibility', 'A reason unrelated to evaluating sources', 'Every author is equally credible regardless of their background'], 0),
   ('Why might checking the publication date of a source matter?', ['It helps determine whether the information is current and still accurate', 'The publication date never affects how reliable a source is', 'A reason unrelated to evaluating sources', 'Older sources are always more reliable than newer ones'], 0),
   ('Which is a warning sign that an online source may not be credible?', ['It makes claims with no supporting evidence or citations', 'It clearly cites its sources and evidence', 'A concept unrelated to evaluating sources', 'It is written by an expert in the field'], 0),
   ('Why is evaluating source credibility an important skill today?', ['It helps readers avoid being misled by inaccurate or biased information online', 'This skill has no use when reading information online', 'A reason unrelated to media literacy', 'All online information can be trusted without question'], 0)]),
M('Probability: Complementary Events',
  'Grade 7 Math strand: complementary events are two outcomes where exactly one must occur, and their probabilities always add up to 1 (or 100%).',
  [('Complementary events are two outcomes where ___.', ['Exactly one of the two must occur', 'Both outcomes must occur at the same time', 'A concept unrelated to complementary events', 'Neither outcome can ever occur'], 0),
   ('The probabilities of two complementary events always add up to ___.', ['1 (or 100%)', '0', 'A value unrelated to complementary events', '2 (or 200%)'], 0),
   ('If the probability of rain tomorrow is 30%, what is the probability it will not rain?', ['70%', '30%', 'A value unrelated to the calculation', '100%'], 0),
   ('If the probability of drawing a red marble from a bag is 2/5, what is the probability of not drawing a red marble?', ['3/5', '2/5', 'A value unrelated to the calculation', '1/5'], 0),
   ('Why are complementary events useful in probability?', ['They allow one probability to be calculated easily if the other is already known', 'Complementary events have no practical use in probability', 'A reason unrelated to complementary events', 'They can only be used when there are more than two possible outcomes'], 0)]),
Sc('Fossil Formation and the Geologic Time Scale',
   'Grade 7 Science strand: fossils form when the remains or traces of living things are preserved in rock over long periods of time, and the geologic time scale organizes Earth’s history into different eras and periods.',
   [('Fossils typically form when ___.', ['The remains or traces of living things are preserved in rock over time', 'A living thing is preserved instantly with no time required', 'A concept unrelated to fossil formation', 'Rocks form with no connection to living things at all'], 0),
    ('The geologic time scale organizes Earth’s history into ___.', ['Different eras and periods', 'A single unbroken block of time', 'A concept unrelated to the geologic time scale', 'Only the years since human history began'], 0),
    ('Why are fossils useful to scientists studying Earth’s history?', ['They provide evidence about past life forms and environmental conditions', 'Fossils provide no useful scientific information', 'A reason unrelated to fossils', 'Fossils only reveal information about modern living things'], 0),
    ('Which of these is required for a fossil to form?', ['Conditions that allow remains to be preserved rather than decompose completely', 'A living thing that has never existed', 'A concept unrelated to fossil formation', 'The complete absence of any rock or sediment'], 0),
    ('Why might scientists use the geologic time scale when studying fossils?', ['It helps place fossils within a specific era, giving context to when a species existed', 'The geologic time scale has no connection to studying fossils', 'A reason unrelated to Earth science', 'Fossils can never be placed within a specific time period'], 0)]),
SS('Canada’s National Parks and Environmental Policy',
   'Grade 7 Social Studies strand: Canada’s national parks protect significant natural areas, and environmental policy shapes how the country balances conservation with development and resource use.',
   [('Canada’s national parks are primarily established to ___.', ['Protect significant natural areas and biodiversity', 'Encourage unrestricted development in natural areas', 'A concept unrelated to national parks', 'Remove all public access to natural areas'], 0),
    ('Environmental policy generally aims to balance ___.', ['Conservation with development and resource use', 'Development alone, with no consideration for the environment', 'A concept unrelated to environmental policy', 'Conservation alone, with no consideration for the economy'], 0),
    ('Why might governments create environmental policies related to national parks?', ['To help protect natural areas for future generations while managing human impact', 'Environmental policies have no connection to protecting natural areas', 'A reason unrelated to environmental policy', 'National parks require no policies or protections at all'], 0),
    ('Which of these might be a challenge in balancing conservation and development?', ['Weighing the economic benefits of development against environmental protection', 'There are never any challenges involved in this balance', 'A concept unrelated to environmental policy', 'Conservation and development always align perfectly with no tension'], 0),
    ('Why is it valuable for students to learn about environmental policy?', ['It helps them understand how societies make decisions about protecting natural resources', 'Environmental policy has no connection to understanding society', 'A reason unrelated to social studies learning', 'Environmental policy is decided with no input from society at all'], 0)])]),
day(57, [
L('Writing: Writing a Process Analysis Essay (How Something Works)',
  'Grade 7 Language strand: a process analysis essay explains how something works or how to complete a task, breaking the process down into clear, logically ordered steps.',
  [('A process analysis essay explains ___.', ['How something works or how to complete a task', 'A completely unrelated personal opinion', 'A concept unrelated to writing', 'A fictional story with no factual basis'], 0),
   ('A process analysis essay should break its topic down into ___.', ['Clear, logically ordered steps', 'A single confusing paragraph with no structure', 'A concept unrelated to process analysis essays', 'Random, unordered pieces of information'], 0),
   ('Which of these would be an appropriate topic for a process analysis essay?', ['How a bill becomes a law', 'A personal memory from childhood', 'A concept unrelated to process analysis essays', 'A persuasive argument about a controversial topic'], 0),
   ('Why might a writer use transition words like “first,” “next,” and “finally” in a process analysis essay?', ['They help guide the reader clearly through each step of the process', 'These words are never useful in this type of essay', 'A reason unrelated to process analysis essays', 'They are only used in fictional stories'], 0),
   ('Why is it important for a process analysis essay to be written in a logical order?', ['Steps presented out of order can confuse the reader and make the process hard to follow', 'The order of steps never affects how clearly a process is understood', 'A reason unrelated to writing', 'A process analysis essay does not need any clear order at all'], 0)]),
M('Standard Form vs. Expanded Form of Numbers',
  'Grade 7 Math strand: standard form writes a number using digits, such as 4,502, while expanded form breaks it down by place value, such as 4,000 + 500 + 2.',
  [('Standard form writes a number using ___.', ['Digits, in its usual numerical form', 'Only words, with no digits at all', 'A concept unrelated to standard form', 'Roman numerals only'], 0),
   ('Expanded form breaks a number down by ___.', ['Place value', 'Its total value with no breakdown at all', 'A concept unrelated to expanded form', 'Alphabetical order'], 0),
   ('What is 3,406 written in expanded form?', ['3,000 + 400 + 6', '3,000 + 40 + 6', 'A value unrelated to the conversion', '300 + 40 + 6'], 0),
   ('What is 2,000 + 300 + 70 + 5 written in standard form?', ['2,375', '2,357', 'A value unrelated to the conversion', '23,075'], 0),
   ('Why might expanded form be useful when teaching place value?', ['It clearly shows the value each digit represents based on its position', 'Expanded form has no connection to understanding place value', 'A reason unrelated to expanded form', 'Expanded form is only used with very small numbers'], 0)]),
Sc('Symbiosis: Mutualism, Commensalism, and Parasitism',
   'Grade 7 Science strand: symbiosis describes close relationships between different species, including mutualism (both benefit), commensalism (one benefits, the other is unaffected), and parasitism (one benefits at the other’s expense).',
   [('In a mutualistic relationship, ___.', ['Both species benefit', 'Only one species benefits, while the other is harmed', 'A concept unrelated to mutualism', 'Neither species benefits at all'], 0),
    ('In a commensal relationship, ___.', ['One species benefits while the other is unaffected', 'Both species are harmed equally', 'A concept unrelated to commensalism', 'Both species benefit equally'], 0),
    ('In a parasitic relationship, ___.', ['One species benefits at the expense of the other', 'Both species benefit equally', 'A concept unrelated to parasitism', 'Neither species is affected in any way'], 0),
    ('Which is an example of a mutualistic relationship?', ['Bees pollinating flowers while feeding on their nectar', 'A tick feeding on a dog’s blood, harming the dog', 'A concept unrelated to mutualism', 'Two species that never interact with one another'], 0),
    ('Why do scientists study symbiotic relationships in ecosystems?', ['They help explain how different species depend on and affect one another', 'Symbiotic relationships provide no useful information about ecosystems', 'A reason unrelated to biology', 'Species in an ecosystem never interact with each other'], 0)]),
SS('The Arab Spring and Its Global Impact',
   'Grade 7 Social Studies strand: the Arab Spring was a wave of pro-democracy protests and uprisings that spread across several Middle Eastern and North African countries beginning in 2010 and 2011.',
   [('The Arab Spring was a wave of ___.', ['Pro-democracy protests and uprisings', 'Celebrations with no political purpose', 'A concept unrelated to the Arab Spring', 'International trade agreements'], 0),
    ('The Arab Spring began spreading across the Middle East and North Africa around ___.', ['2010 and 2011', 'The 1800s', 'A time period unrelated to the Arab Spring', 'Ancient times, thousands of years ago'], 0),
    ('Which of these was a common demand of protesters during the Arab Spring?', ['Greater political freedom and an end to authoritarian rule', 'A return to stricter authoritarian governments', 'A demand unrelated to the Arab Spring', 'The complete removal of all elections'], 0),
    ('Why did the Arab Spring have such a widespread impact across the region?', ['Similar political and economic frustrations existed in multiple countries at the same time', 'The events in one country had no effect on any other country', 'A reason unrelated to the Arab Spring', 'The protests were limited to a single city with no broader impact'], 0),
    ('Why do historians and social studies students continue to study the Arab Spring?', ['It offers insight into how citizen movements can influence political change', 'The Arab Spring had no lasting effect on the region', 'A reason unrelated to its historical significance', 'The events of the Arab Spring have been completely forgotten'], 0)])]),
day(58, [
L('Grammar: Using Semicolons, Colons, and Dashes',
  'Grade 7 Language strand: semicolons join related independent clauses, colons introduce lists or explanations, and dashes can be used to add emphasis or set off extra information.',
  [('A semicolon can be used to ___.', ['Join two closely related independent clauses', 'Replace every comma in a sentence', 'A concept unrelated to punctuation', 'End a sentence in place of a period'], 0),
   ('A colon is often used to ___.', ['Introduce a list or explanation', 'Replace a question mark', 'A concept unrelated to punctuation', 'Separate every word in a sentence'], 0),
   ('A dash can be used to ___.', ['Add emphasis or set off extra information', 'Replace all punctuation in a sentence', 'A concept unrelated to punctuation', 'Indicate the end of a paragraph'], 0),
   ('Which sentence correctly uses a colon?', ['She packed three things: a map, water, and snacks.', 'She packed three things, a map, water, and snacks.', 'A sentence unrelated to colon use', 'She packed three things; a map, water, and snacks.'], 0),
   ('Why might a writer choose a dash instead of a comma to set off extra information?', ['A dash can create a stronger emphasis or a more dramatic pause', 'Dashes are never used to set off extra information', 'A reason unrelated to punctuation', 'Dashes always weaken the emphasis of a sentence'], 0)]),
M('Box-and-Whisker Plots (Intro)',
  'Grade 7 Math strand: a box-and-whisker plot displays a data set’s minimum, first quartile, median, third quartile, and maximum, helping to visualize its spread and central tendency.',
  [('A box-and-whisker plot displays a data set’s ___.', ['Minimum, quartiles, median, and maximum', 'Only the maximum value in the data set', 'A concept unrelated to box-and-whisker plots', 'Only the average of the data set'], 0),
   ('The line inside the box of a box-and-whisker plot typically represents the ___.', ['Median', 'Maximum', 'A value unrelated to box-and-whisker plots', 'Range'], 0),
   ('The “whiskers” of a box-and-whisker plot extend to show the ___.', ['Minimum and maximum values in the data set', 'Only the median value', 'A concept unrelated to box-and-whisker plots', 'Only the values within the box itself'], 0),
   ('Why might a box-and-whisker plot be useful for comparing two data sets?', ['It visually shows the spread and central tendency of each set side by side', 'Box-and-whisker plots cannot be used to compare data sets', 'A reason unrelated to box-and-whisker plots', 'They only display a single number with no visual comparison'], 0),
   ('What does the “box” portion of a box-and-whisker plot represent?', ['The middle 50% of the data, between the first and third quartiles', 'The entire range of the data set', 'A concept unrelated to box-and-whisker plots', 'Only the single highest value in the data set'], 0)]),
Sc('Nuclear Energy: Fission and Power Generation',
   'Grade 7 Science strand: nuclear energy is produced through fission, a process where atomic nuclei split apart and release large amounts of energy, which can be used to generate electricity.',
   [('Nuclear fission occurs when ___.', ['An atomic nucleus splits apart, releasing energy', 'Two atomic nuclei combine into one', 'A process unrelated to nuclear fission', 'An atom disappears with no reaction at all'], 0),
    ('Nuclear power plants use fission to ___.', ['Generate heat that is used to produce electricity', 'Directly power vehicles with no electricity involved', 'A process unrelated to nuclear power', 'Cool down surrounding areas with no energy production'], 0),
    ('Which of these is a potential benefit of nuclear energy?', ['It can generate large amounts of electricity without directly burning fossil fuels', 'It produces no usable energy at all', 'A concept unrelated to nuclear energy', 'It requires no safety considerations of any kind'], 0),
    ('Which of these is a potential concern associated with nuclear energy?', ['Safely managing radioactive waste', 'Nuclear energy has no potential concerns of any kind', 'A concept unrelated to nuclear energy', 'It cannot generate any electricity at all'], 0),
    ('Why might countries consider nuclear energy as part of their energy strategy?', ['It can provide a significant, relatively low-carbon source of electricity', 'Nuclear energy provides no benefits to a country’s energy strategy', 'A reason unrelated to nuclear energy', 'It has no connection to generating electricity'], 0)]),
SS('Urban Sprawl and City Planning Challenges',
   'Grade 7 Social Studies strand: urban sprawl refers to the rapid, spread-out expansion of a city into surrounding areas, creating challenges for transportation, infrastructure, and city planning.',
   [('Urban sprawl refers to ___.', ['The rapid, spread-out expansion of a city into surrounding areas', 'A city that never grows or changes over time', 'A concept unrelated to urban sprawl', 'A city shrinking in population and size'], 0),
    ('Which of these is a common challenge associated with urban sprawl?', ['Increased dependence on cars and longer commute times', 'A significant reduction in the need for transportation', 'A concept unrelated to urban sprawl', 'A city with no transportation challenges at all'], 0),
    ('Why might urban sprawl create challenges for city infrastructure?', ['Spread-out development can be more costly and difficult to service with roads, water, and utilities', 'Infrastructure needs are never affected by how a city is developed', 'A reason unrelated to urban sprawl', 'Spread-out cities always require less infrastructure than compact ones'], 0),
    ('Which of these is a strategy city planners might use to address urban sprawl?', ['Encouraging more compact, mixed-use development', 'Encouraging development to spread out as much as possible', 'A concept unrelated to city planning', 'Avoiding any planning or strategy at all'], 0),
    ('Why is urban sprawl an important topic in city planning?', ['It affects transportation, the environment, and quality of life in a growing city', 'Urban sprawl has no effect on how a city functions', 'A reason unrelated to city planning', 'Urban sprawl is not a real or relevant issue for city planners'], 0)])]),
day(59, [
L('Reading: Analyzing Nonfiction Text Structures',
  'Grade 7 Language strand: nonfiction texts are often organized using structures like cause-and-effect, problem-and-solution, or sequence, and recognizing these structures helps readers follow the author’s ideas.',
  [('Nonfiction texts are often organized using structures such as ___.', ['Cause-and-effect, problem-and-solution, or sequence', 'Only rhyme and rhythm', 'A concept unrelated to nonfiction text structures', 'A single unchanging structure used in every text'], 0),
   ('A cause-and-effect structure explains ___.', ['How one event leads to another', 'The steps needed to solve a problem', 'A structure unrelated to cause-and-effect', 'Events with no connection to one another'], 0),
   ('A problem-and-solution structure presents ___.', ['A problem, followed by one or more possible solutions', 'Only a problem, with no solution ever discussed', 'A structure unrelated to problem-and-solution', 'A solution with no explanation of the original problem'], 0),
   ('A sequence structure organizes information ___.', ['In a specific order, such as chronological order', 'With no order or organization at all', 'A structure unrelated to sequence', 'In a completely random order every time'], 0),
   ('Why is it useful for readers to recognize a text’s structure?', ['It helps them anticipate how information will be organized and better follow the author’s ideas', 'Recognizing text structure never helps with understanding a text', 'A reason unrelated to reading comprehension', 'All nonfiction texts use exactly the same structure'], 0)]),
M('Adding and Subtracting Polynomials',
  'Grade 7 Math strand: adding or subtracting polynomials involves combining like terms while keeping unlike terms separate.',
  [('To add polynomials, you ___.', ['Combine like terms', 'Multiply every term together', 'A method unrelated to adding polynomials', 'Combine unlike terms only'], 0),
   ('Simplify: (3x + 5) + (2x + 1).', ['5x + 6', '5x + 5', 'A value unrelated to the calculation', '6x + 6'], 0),
   ('Simplify: (7x + 4) - (2x + 1).', ['5x + 3', '5x + 5', 'A value unrelated to the calculation', '9x + 3'], 0),
   ('When subtracting polynomials, what must be done to the terms in the second polynomial?', ['Their signs must be changed before combining like terms', 'Their signs are never changed during subtraction', 'A step unrelated to subtracting polynomials', 'They must be multiplied by 2 before combining'], 0),
   ('Why must like terms be combined carefully when adding or subtracting polynomials?', ['Only terms with the same variable and exponent can be combined accurately', 'Any two terms can always be combined regardless of their variable or exponent', 'A reason unrelated to polynomials', 'Polynomials never require any careful combination of terms'], 0)]),
Sc('The Skeletal and Muscular Systems in Depth',
   'Grade 7 Science strand: the skeletal system provides structure, protection, and support for the body, while the muscular system works with it through contraction and relaxation to produce movement.',
   [('The skeletal system provides the body with ___.', ['Structure, protection, and support', 'The ability to digest food', 'A function unrelated to the skeletal system', 'The ability to pump blood'], 0),
    ('Muscles produce movement through the process of ___.', ['Contraction and relaxation', 'Digestion and absorption', 'A process unrelated to muscles', 'Filtration and excretion'], 0),
    ('Which is an example of the skeletal and muscular systems working together?', ['Bending your arm at the elbow using both bone and muscle', 'Digesting a meal using only the stomach', 'A concept unrelated to these systems', 'Breathing using only the lungs, with no involvement from bones or muscles'], 0),
    ('Why might bones be described as providing a framework for the body?', ['They give the body its overall shape and structure, supporting other systems', 'Bones have no connection to the body’s overall shape', 'A reason unrelated to the skeletal system', 'The body has no structure or framework at all'], 0),
    ('Why do the skeletal and muscular systems need to work closely together?', ['Muscles need bones to pull against in order to create controlled movement', 'These two systems function completely independently of one another', 'A reason unrelated to body systems', 'Movement occurs with no involvement from bones or muscles'], 0)]),
SS('Global Food Security and Agriculture',
   'Grade 7 Social Studies strand: food security means having reliable access to enough safe, nutritious food, and global agriculture faces challenges such as climate change, population growth, and unequal distribution of resources.',
   [('Food security refers to ___.', ['Having reliable access to enough safe, nutritious food', 'Having access to an unlimited supply of any type of food', 'A concept unrelated to food security', 'A concern that only applies to a single country'], 0),
    ('Which of these is a challenge facing global agriculture today?', ['Climate change affecting crop yields and growing conditions', 'An unlimited and endlessly reliable food supply everywhere', 'A concept unrelated to agricultural challenges', 'A complete absence of any global food challenges'], 0),
    ('Why might population growth create challenges for food security?', ['A growing population requires more food production and resources to meet demand', 'Population growth has no connection to food security', 'A reason unrelated to food security', 'A larger population automatically guarantees enough food for everyone'], 0),
    ('Which of these could help improve food security in a region?', ['Investing in sustainable farming techniques and infrastructure', 'Ignoring agricultural challenges entirely', 'A concept unrelated to food security', 'Reducing food production without any other changes'], 0),
    ('Why is global food security an important topic in social studies?', ['It connects to economics, geography, and the well-being of people around the world', 'Food security has no connection to social studies topics', 'A reason unrelated to this unit', 'Food security is a concern only in fictional scenarios'], 0)])]),
day(60, [
L('Writing: Writing a Eulogy or Tribute Speech',
  'Grade 7 Language strand: a eulogy or tribute speech honours a person by sharing meaningful memories, qualities, and the impact they had on others, often organized around specific stories or themes.',
  [('A eulogy or tribute speech is written to ___.', ['Honour a person by sharing meaningful memories and qualities', 'Criticize a person’s actions and character', 'A concept unrelated to this type of writing', 'Provide only a list of dates and facts with no personal reflection'], 0),
   ('Which of these might a tribute speech include?', ['A specific story that reflects the person’s character', 'A list of unrelated statistics with no connection to the person', 'A concept unrelated to tribute speeches', 'Criticism of the person being honoured'], 0),
   ('Why might a speaker organize a tribute speech around specific themes, such as kindness or determination?', ['It helps highlight meaningful qualities in a clear, memorable way', 'Themes are never used to organize this type of speech', 'A reason unrelated to tribute speeches', 'Themes make a speech harder for an audience to follow'], 0),
   ('Why is tone especially important in a eulogy or tribute speech?', ['A respectful, sincere tone helps honour the person appropriately', 'Tone has no effect on how a tribute speech is received', 'A reason unrelated to this type of writing', 'A humorous, disrespectful tone is always most appropriate'], 0),
   ('Which of these is a purpose of a tribute speech?', ['To celebrate and remember the impact a person had on others', 'To provide a purely factual, emotionless account of events', 'A concept unrelated to tribute speeches', 'To focus only on negative memories of a person'], 0)]),
M('Review: Polynomials, Pythagorean Applications, and Data Displays',
  'Grade 7 Math strand: this review lesson revisits key ideas from Days 51-60, including polynomials, the Pythagorean theorem, spheres, and box-and-whisker plots.',
  [('A polynomial is an expression made up of ___.', ['Terms combined using addition or subtraction', 'Only a single number with no variables', 'A concept unrelated to polynomials', 'Terms that can never be combined in any way'], 0),
   ('The Pythagorean theorem states that ___.', ['a² + b² = c², where c is the hypotenuse of a right triangle', 'a + b = c for any triangle', 'A formula unrelated to the Pythagorean theorem', 'a² - b² = c² for any triangle'], 0),
   ('The formula for the volume of a sphere is ___.', ['(4/3)πr³', 'πr²', 'A formula unrelated to the volume of a sphere', '2πr'], 0),
   ('The line inside the box of a box-and-whisker plot typically represents the ___.', ['Median', 'Maximum', 'A value unrelated to box-and-whisker plots', 'Range'], 0),
   ('Why is it useful to review polynomials, geometry, and data displays together?', ['It reinforces how these math concepts connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Motion, Sound, Structures, and Systems',
   'Grade 7 Science strand: this review lesson revisits key ideas from Days 51-60, including Newton’s laws, sound waves, structures, symbiosis, and the skeletal and muscular systems.',
   [('Newton’s first law of motion describes ___.', ['Inertia -- an object’s tendency to resist changes in motion', 'The relationship between force and colour', 'A concept unrelated to Newton’s laws', 'The speed of light in a vacuum'], 0),
    ('Pitch is determined by ___.', ['Frequency, or how many vibrations occur per second', 'The colour of the sound wave', 'A concept unrelated to pitch', 'The distance the sound has travelled'], 0),
    ('In a mutualistic relationship, ___.', ['Both species benefit', 'Only one species benefits, while the other is harmed', 'A concept unrelated to mutualism', 'Neither species benefits at all'], 0),
    ('Muscles produce movement through the process of ___.', ['Contraction and relaxation', 'Digestion and absorption', 'A process unrelated to muscles', 'Filtration and excretion'], 0),
    ('Why is it useful to review motion, sound, structures, and body systems together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: International Relations and Canadian Policy',
   'Grade 7 Social Studies strand: this review lesson revisits key ideas from Days 51-60, including the League of Nations, Canadian immigration policy, decolonization, the Non-Aligned Movement, and the Arab Spring.',
   [('The League of Nations was formed after ___.', ['World War I', 'World War II', 'A conflict unrelated to the League of Nations', 'The Cold War'], 0),
    ('Canada’s modern immigration system often uses ___.', ['A points-based system considering factors like skills and education', 'A system that considers no criteria at all', 'A concept unrelated to immigration policy', 'A system that only accepts immigrants from a single country'], 0),
    ('Decolonization in Africa refers to the process by which ___.', ['African nations gained independence from European colonial powers', 'European powers expanded their control over African nations', 'A concept unrelated to decolonization', 'African nations became colonies for the first time'], 0),
    ('The Arab Spring was a wave of ___.', ['Pro-democracy protests and uprisings', 'Celebrations with no political purpose', 'A concept unrelated to the Arab Spring', 'International trade agreements'], 0),
    ('Why is it useful to review international relations and policy topics together?', ['It reinforces how these interconnected historical and political events shaped the modern world', 'These topics have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history and policy'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260802):
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
    _rebalance_answer_positions(g7_51_60)
    append_to(7, g7_51_60)
