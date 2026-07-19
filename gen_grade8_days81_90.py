#!/usr/bin/env python3
"""Grade 8, Days 81-90 -- extends Grade 8 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade8.json):
anti-heroes, rhetorical analysis essays, correlative conjunctions,
portmanteau words, stream-of-consciousness narration, op-ed rebuttals,
deepfakes, passive voice in scientific writing, bildungsroman; law of
sines and cosines, matrices, normal distribution, completing the square,
vectors, amortization and mortgages, z-scores, spherical geometry,
systems of three variables; epigenetics, superconductors, coral reef
marine biology, quantum physics basics, immunology, bioplastics, black
holes, epidemiology, battery chemistry; the Chinese Immigration Act
repeal, the Just Society, the fall of the Berlin Wall from a Canadian
perspective, Vimy Ridge remembrance, the founding of the CBC, the 1995
Quebec referendum, Canada's role in Afghanistan, the Nisga'a Treaty, and
the Truth and Reconciliation Commission's 94 Calls to Action.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-history'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science and Technology',
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


def _rebalance_answer_positions(days, seed=20260927):
    import random
    rng = random.Random(seed)
    quizzes = [sub_entry[5] for _, subs in days for sub_entry in subs]
    n = sum(len(q) for q in quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in quizzes:
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
    return days


g8_81_90 = [
day(81, [
L('Reading: Analyzing Anti-Heroes in Literature',
  'Grade 8 Language strand: an anti-hero is a main character who lacks traditional heroic qualities, such as courage or moral virtue, yet still drives the story forward in a compelling way.',
  [('What is an anti-hero?', ['A main character who lacks traditional heroic qualities', 'A villain with no role in the main plot', 'A concept unrelated to reading', 'A minor character with no importance'], 0),
   ('Does an anti-hero still play a central role in driving the story forward?', ['Yes', 'No, anti-heroes never play any central role', 'A concept unrelated to anti-heroes', 'Anti-heroes only ever appear in the background'], 0),
   ('Which of these traits might an anti-hero lack compared to a traditional hero?', ['Moral virtue', 'The ability to speak', 'A concept unrelated to anti-heroes', 'A physical body'], 0),
   ('Why might an author choose to write an anti-hero instead of a traditional hero?', ['It can create a more complex, realistic character that challenges readers’ expectations', 'Anti-heroes never add any complexity to a story', 'This concept has no connection to literature', 'Traditional heroes are always more interesting than anti-heroes'], 0),
   ('Why might readers still feel sympathy for an anti-hero despite their flaws?', ['Authors often show relatable struggles or reasons behind the anti-hero’s flawed choices', 'Readers never feel any sympathy for a flawed character', 'This concept has no relevance to reading comprehension', 'Anti-heroes are always portrayed with absolutely no depth'], 0)]),
M('Introduction to the Law of Sines and Cosines',
  'Grade 8 Math strand: the law of sines and the law of cosines are formulas used to find missing sides or angles in any triangle, not just right triangles.',
  [('What can the law of sines and cosines help you find in a triangle?', ['Missing sides or angles', 'Only the triangle’s colour', 'A concept unrelated to trigonometry', 'Only the triangle’s perimeter'], 0),
   ('Do the law of sines and cosines apply only to right triangles, or to any triangle?', ['Any triangle', 'Only right triangles', 'A concept unrelated to these laws', 'Only equilateral triangles'], 0),
   ('Why are the law of sines and cosines useful beyond the Pythagorean theorem?', ['They can be applied to triangles that are not right triangles', 'They can only ever be used on right triangles, just like the Pythagorean theorem', 'This concept has no connection to trigonometry', 'These laws never apply to any triangle at all'], 0),
   ('If you know two angles and one side of a triangle, which law could help find another side?', ['The law of sines', 'A concept unrelated to trigonometry', 'Only the Pythagorean theorem, which requires a right angle', 'No law can ever help in this situation'], 0),
   ('Why might a surveyor use the law of cosines when measuring land that forms a non-right triangle?', ['It allows them to calculate an unknown side or angle without needing a right angle', 'The law of cosines never applies to real-world measurement problems', 'This concept has no relevance to math', 'Surveyors never need to measure any triangular shapes'], 0)]),
Sc('Science: Epigenetics: How Environment Affects Gene Expression',
   'Grade 8 Science strand: epigenetics studies how environmental factors, such as diet or stress, can influence whether certain genes are turned on or off, without changing the underlying DNA sequence.',
   [('What does epigenetics study?', ['How environmental factors influence whether genes are turned on or off', 'How genes are physically removed from an organism', 'A concept unrelated to biology', 'How DNA sequences are permanently rewritten'], 0),
    ('Name one environmental factor that might influence gene expression, such as diet.', ['Diet', 'A concept unrelated to epigenetics', 'A favourite colour', 'A random guess with no scientific basis'], 0),
    ('Does epigenetics involve changing the underlying DNA sequence itself?', ['No', 'Yes, it always changes the DNA sequence', 'A concept unrelated to epigenetics', 'Epigenetics has no connection to genes at all'], 0),
    ('Why might scientists be interested in how stress affects gene expression?', ['Understanding these effects could reveal connections between environment and health outcomes', 'Stress has no connection to gene expression', 'This concept has no relevance to science', 'Gene expression is never affected by any outside factor'], 0),
    ('Why is epigenetics considered a relatively new and evolving area of scientific study?', ['Scientists are still working to understand the full range of factors that can influence gene expression', 'Epigenetics has already been completely understood with nothing left to discover', 'This concept has no relevance to science', 'Gene expression was fully explained centuries ago'], 0)]),
H('The Chinese Immigration Act Repeal and Reconciliation',
  'Grade 8 History strand: after decades of restrictive immigration laws targeting Chinese immigrants, Canada repealed the Chinese Immigration Act in 1947, a step toward addressing past discrimination.',
  [('In what year was the Chinese Immigration Act repealed?', ['1947', '1867', '1988', '2001'], 0),
   ('Did the Chinese Immigration Act restrict Chinese immigration to Canada?', ['Yes', 'No, it encouraged unlimited Chinese immigration', 'A concept unrelated to Canadian history', 'It had no connection to immigration at all'], 0),
   ('Was the repeal of this act a step toward addressing past discrimination?', ['Yes', 'No, the repeal had no connection to discrimination', 'A concept unrelated to Canadian history', 'The act was never actually repealed'], 0),
   ('Why is the repeal of the Chinese Immigration Act considered an important moment in Canadian history?', ['It marked a significant shift away from a discriminatory immigration policy', 'The repeal had no real significance in Canadian history', 'This concept has no connection to history', 'Immigration policy in Canada has never changed over time'], 0),
   ('Why is it valuable for students to learn about historical policies like the Chinese Immigration Act?', ['It helps build understanding of how discrimination has shaped Canadian history and policy', 'Historical immigration policies have no relevance to understanding Canada today', 'This concept has no relevance to History', 'Past discrimination never has any connection to modern Canadian society'], 0)]),
]),

day(82, [
L('Writing: The Rhetorical Analysis Essay',
  'Grade 8 Language strand: a rhetorical analysis essay examines how a writer or speaker uses persuasive techniques, such as ethos, pathos, and logos, to influence an audience.',
  [('What does a rhetorical analysis essay examine?', ['How a writer or speaker uses persuasive techniques', 'Only the length of a text', 'A concept unrelated to writing', 'Only the punctuation used in a text'], 0),
   ('Name one persuasive technique a rhetorical analysis might examine, such as ethos or pathos.', ['Ethos', 'A concept unrelated to rhetorical analysis', 'A grocery list', 'A math formula'], 0),
   ('Does ethos refer to an appeal based on credibility and trustworthiness?', ['Yes', 'No, ethos refers only to emotion', 'A concept unrelated to rhetorical analysis', 'Ethos has no connection to persuasion'], 0),
   ('Does pathos refer to an appeal based on emotion?', ['Yes', 'No, pathos refers only to logic', 'A concept unrelated to rhetorical analysis', 'Pathos has no connection to persuasion'], 0),
   ('Why might a rhetorical analysis essay be useful for understanding a political speech?', ['It can reveal the specific techniques used to persuade or influence listeners', 'Rhetorical analysis never reveals anything useful about a speech', 'This concept has no connection to writing', 'Political speeches never use any persuasive techniques'], 0)]),
M('Matrices: An Introduction',
  'Grade 8 Math strand: a matrix is a rectangular arrangement of numbers organized into rows and columns, used to represent and solve certain types of mathematical problems.',
  [('What is a matrix?', ['A rectangular arrangement of numbers in rows and columns', 'A single number with no structure', 'A concept unrelated to math', 'A type of geometric shape only'], 0),
   ('What are the two directions a matrix is organized by?', ['Rows and columns', 'Only rows, with no columns', 'A concept unrelated to matrices', 'Only diagonals'], 0),
   ('In a matrix with 2 rows and 3 columns, how many total numbers does it contain?', ['6', '5', '2', '3'], 0),
   ('Why might a matrix be useful for organizing data, like scores from multiple games and players?', ['It provides a clear, organized way to display data across two categories at once', 'Matrices never help organize any kind of data', 'This concept has no connection to math', 'Rows and columns never actually represent meaningful data'], 0),
   ('What is the size of a matrix with 3 rows and 2 columns often written as?', ['3 by 2', '2 by 3', 'A concept unrelated to matrices', '5 by 5'], 0)]),
Sc('Science: The Physics of Superconductors',
   'Grade 8 Science strand: a superconductor is a material that can conduct electricity with zero resistance when cooled to extremely low temperatures, allowing electric current to flow without losing energy.',
   [('What is a superconductor?', ['A material that conducts electricity with zero resistance at low temperatures', 'A material that always blocks electricity completely', 'A concept unrelated to physics', 'A material that only works at very high temperatures'], 0),
    ('Does a superconductor need to be cooled to extremely low temperatures to work?', ['Yes', 'No, superconductors work best at room temperature only', 'A concept unrelated to superconductors', 'Temperature has no connection to superconductivity'], 0),
    ('Does electric current flow through a superconductor without losing energy?', ['Yes', 'No, superconductors always lose a large amount of energy', 'A concept unrelated to superconductors', 'Superconductors never actually conduct any electricity'], 0),
    ('Why might superconductors be useful for technologies like maglev trains?', ['They can create powerful magnetic fields efficiently, without energy loss from resistance', 'Superconductors have no connection to magnetic technology', 'This concept has no relevance to science', 'Maglev trains never use any superconducting technology'], 0),
    ('Why is the requirement for extremely low temperatures a current challenge for using superconductors widely?', ['Cooling materials to such low temperatures can be expensive and difficult to maintain', 'Cooling has no connection to how superconductors are used', 'This concept has no relevance to physics', 'Superconductors work at any temperature with no special cooling needed'], 0)]),
H('The Just Society and Pierre Trudeau’s Legacy',
  'Grade 8 History strand: Prime Minister Pierre Trudeau promoted the idea of a Just Society in the late 1960s, aiming to expand human rights, bilingualism, and social equality across Canada.',
  [('Which prime minister promoted the idea of a Just Society?', ['Pierre Trudeau', 'A concept unrelated to Canadian history', 'A fictional political figure', 'A prime minister from a different country'], 0),
   ('Around what decade did Pierre Trudeau promote the Just Society?', ['The late 1960s', 'The 1800s', 'A concept unrelated to Canadian history', 'The 2020s'], 0),
   ('Did the Just Society aim to expand human rights and social equality?', ['Yes', 'No, it aimed to reduce human rights protections', 'A concept unrelated to the Just Society', 'It had no connection to social equality at all'], 0),
   ('Why might the Just Society be considered an influential vision in Canadian political history?', ['It shaped policies related to rights, bilingualism, and equality that influenced later governments', 'The Just Society had no lasting influence on Canadian policy', 'This concept has no connection to Canadian history', 'This vision was never discussed by any government'], 0),
   ('Why is it valuable for students to study political visions like the Just Society?', ['It helps show how political ideas can shape a country’s laws and values over time', 'Political visions never have any effect on a country’s policies', 'This concept has no relevance to History', 'The Just Society has no connection to Canadian identity'], 0)]),
]),

day(83, [
L('Grammar: Correlative Conjunctions and Parallelism',
  'Grade 8 Language strand: correlative conjunctions, such as either/or and not only/but also, must be paired with parallel grammatical structures to sound clear and balanced.',
  [('Name one pair of correlative conjunctions, such as either/or.', ['Either/or', 'A concept unrelated to grammar', 'Cat/dog', 'Run/jump'], 0),
   ('What must correlative conjunctions be paired with to sound clear and balanced?', ['Parallel grammatical structures', 'Random, mismatched structures', 'A concept unrelated to correlative conjunctions', 'No structure at all'], 0),
   ('Which sentence correctly uses parallel structure with correlative conjunctions?', ['She not only sings but also dances.', 'She not only sings but also to dance.', 'Not only she sings but also dancing.', 'She sings not only but also dances she.'], 0),
   ('Why might a sentence using either/or sound awkward if it lacks parallel structure?', ['Mismatched structures can make a sentence confusing or grammatically incorrect', 'Parallel structure never affects how clear a sentence sounds', 'This concept has no connection to grammar', 'Correlative conjunctions never require any specific structure'], 0),
   ('Which sentence uses correlative conjunctions with correct parallel structure?', ['Neither the teacher nor the students were ready.', 'Neither the teacher nor were the students ready.', 'Neither ready nor the teacher the students were.', 'Ready neither the teacher nor students were.'], 0)]),
M('Introduction to Normal Distribution',
  'Grade 8 Math strand: a normal distribution is a symmetric, bell-shaped pattern of data where most values cluster near the mean, with fewer values appearing farther from the average.',
  [('What shape does a normal distribution typically form?', ['A symmetric, bell shape', 'A completely flat line', 'A concept unrelated to statistics', 'A perfectly straight diagonal line'], 0),
   ('In a normal distribution, do most values cluster near the mean or far from it?', ['Near the mean', 'Far from the mean', 'A concept unrelated to normal distribution', 'Values never cluster anywhere in particular'], 0),
   ('Why might test scores from a large group of students often form a roughly normal distribution?', ['Most students tend to perform near an average level, with fewer scoring extremely high or low', 'Test scores never form any kind of predictable pattern', 'This concept has no connection to statistics', 'A normal distribution never applies to real-world data like test scores'], 0),
   ('In a bell-shaped normal distribution, where is the peak of the curve typically located?', ['At the mean', 'At the very lowest value', 'A concept unrelated to normal distribution', 'At the very highest value only'], 0),
   ('Why is understanding normal distribution useful for interpreting large data sets?', ['It helps identify what values are typical versus unusually high or low', 'Normal distribution never helps with interpreting any data', 'This concept has no relevance to statistics', 'All data sets always form the exact same shape regardless of pattern'], 0)]),
Sc('Science: Marine Biology: Coral Reef Ecosystems',
   'Grade 8 Science strand: coral reefs are diverse marine ecosystems built by colonies of tiny coral organisms, supporting a huge variety of fish and other sea life, but are highly sensitive to changes in ocean temperature.',
   [('What builds a coral reef?', ['Colonies of tiny coral organisms', 'Large rocks that fall from cliffs', 'A concept unrelated to marine biology', 'Sand carried by ocean currents'], 0),
    ('Do coral reefs support a huge variety of fish and other sea life?', ['Yes', 'No, coral reefs support no living things at all', 'A concept unrelated to coral reefs', 'Only one single species can live near a coral reef'], 0),
    ('Are coral reefs highly sensitive to changes in ocean temperature?', ['Yes', 'No, coral reefs are unaffected by any ocean temperature change', 'A concept unrelated to coral reefs', 'Ocean temperature has no connection to marine ecosystems'], 0),
    ('Why might rising ocean temperatures cause coral bleaching, harming reef ecosystems?', ['Warmer water can stress coral, causing them to expel the algae that give them colour and nutrients', 'Ocean temperature has no connection to coral health', 'This concept has no connection to marine biology', 'Coral reefs are never affected by changes in their environment'], 0),
    ('Why are coral reefs sometimes called the rainforests of the sea?', ['Like rainforests, they support an extremely high level of biodiversity in a relatively small area', 'Coral reefs have no connection to biodiversity at all', 'This concept has no relevance to science', 'Rainforests and coral reefs share no similarities whatsoever'], 0)]),
H('The Fall of the Berlin Wall: A Canadian Perspective',
  'Grade 8 History strand: the fall of the Berlin Wall in 1989 marked the symbolic end of the Cold War, an event that Canada, as a NATO member, watched closely given its own Cold War alliances and policies.',
  [('In what year did the Berlin Wall fall?', ['1989', '1945', '1867', '2001'], 0),
   ('Did the fall of the Berlin Wall mark the symbolic end of the Cold War?', ['Yes', 'No, it had no connection to the Cold War', 'A concept unrelated to the Berlin Wall', 'The Cold War ended long before the wall fell'], 0),
   ('Was Canada a member of NATO during the Cold War?', ['Yes', 'No, Canada had no connection to NATO', 'A concept unrelated to Canadian history', 'NATO did not exist during the Cold War'], 0),
   ('Why might Canada, as a NATO member, have closely followed the events surrounding the fall of the Berlin Wall?', ['Canada’s alliances and policies were closely tied to the broader Cold War tensions between East and West', 'Canada had no interest in or connection to Cold War events', 'This concept has no connection to Canadian history', 'NATO membership had no effect on how Canada viewed world events'], 0),
   ('Why is the fall of the Berlin Wall considered a major turning point in 20th-century world history?', ['It represented the collapse of a major political and physical divide between two opposing global powers', 'The fall of the Berlin Wall had no lasting significance on world history', 'This concept has no relevance to History', 'The wall’s fall had no connection to the wider Cold War'], 0)]),
]),

day(84, [
L('Vocabulary: Portmanteau Words and Blends',
  'Grade 8 Language strand: a portmanteau word combines the sounds and meanings of two existing words to create a new one, such as combining internet and etiquette to form netiquette.',
  [('What does a portmanteau word combine to create a new word?', ['The sounds and meanings of two existing words', 'Only the sounds of one single word', 'A concept unrelated to vocabulary', 'Two completely unrelated random sounds'], 0),
   ('Which word is a portmanteau made from internet and etiquette?', ['Netiquette', 'Internet', 'Etiquette', 'Network'], 0),
   ('Which word is a portmanteau made from motor and hotel?', ['Motel', 'Motorcycle', 'Hotelier', 'Automobile'], 0),
   ('Why might a portmanteau word be created to describe a new concept or technology?', ['It efficiently combines two familiar ideas into one convenient word', 'Portmanteau words never actually describe anything meaningful', 'This concept has no connection to vocabulary', 'New concepts never need any new words to describe them'], 0),
   ('Why might portmanteau words become widely adopted into everyday language over time?', ['They can capture a useful or popular idea in a memorable, catchy way', 'Portmanteau words are never actually adopted into common usage', 'This concept has no relevance to vocabulary', 'New words are always immediately rejected by most speakers'], 0)]),
M('Algebra: Completing the Square',
  'Grade 8 Math strand: completing the square is a method for rewriting a quadratic expression into a perfect square trinomial plus a constant, useful for solving quadratic equations.',
  [('What does completing the square help rewrite a quadratic expression into?', ['A perfect square trinomial plus a constant', 'A completely different type of equation', 'A concept unrelated to algebra', 'A simple linear expression'], 0),
   ('Is completing the square a method useful for solving quadratic equations?', ['Yes', 'No, it has no connection to quadratic equations', 'A concept unrelated to algebra', 'It only works for linear equations'], 0),
   ('In the expression x squared plus 6x, what number would you add to complete the square?', ['9', '6', '3', '36'], 0),
   ('Why might completing the square be useful for finding the vertex of a parabola?', ['Rewriting the equation in vertex form directly reveals the coordinates of the vertex', 'Completing the square never helps identify a parabola’s vertex', 'This concept has no connection to algebra', 'Parabolas never actually have a vertex to find'], 0),
   ('In the expression x squared plus 10x, what number would you add to complete the square?', ['25', '10', '5', '100'], 0)]),
Sc('Science: Introduction to Quantum Physics',
   'Grade 8 Science strand: quantum physics studies the behaviour of extremely small particles, such as electrons, which can behave differently than larger objects described by everyday physics.',
   [('What does quantum physics study?', ['The behaviour of extremely small particles', 'The behaviour of extremely large objects only', 'A concept unrelated to science', 'Only objects that are visible to the naked eye'], 0),
    ('Name one example of a particle studied in quantum physics, such as an electron.', ['An electron', 'A concept unrelated to quantum physics', 'A planet', 'A mountain'], 0),
    ('Can extremely small particles behave differently than larger, everyday objects?', ['Yes', 'No, small particles always behave exactly like large objects', 'A concept unrelated to quantum physics', 'Particles never behave in any predictable pattern'], 0),
    ('Why do scientists need special theories, like quantum physics, to describe particles like electrons?', ['The rules that govern everyday large objects do not fully apply at such a tiny scale', 'Everyday physics fully explains the behaviour of every particle', 'This concept has no connection to quantum physics', 'Electrons behave in exactly the same way as basketballs or cars'], 0),
    ('Why is quantum physics considered important for modern technology, like computer chips?', ['Understanding particle behaviour at this scale has enabled advances in electronics and computing', 'Quantum physics has no connection to modern technology', 'This concept has no relevance to science', 'Computer chips are built with no reliance on quantum physics concepts'], 0)]),
H('Vimy Ridge and Canadian War Remembrance',
  'Grade 8 History strand: the Battle of Vimy Ridge in 1917, where Canadian troops fought together as a unified force, is remembered as a significant moment in the development of Canadian identity.',
  [('In what year did the Battle of Vimy Ridge take place?', ['1917', '1867', '1945', '1812'], 0),
   ('Did Canadian troops fight together as a unified force at Vimy Ridge?', ['Yes', 'No, Canadian troops did not participate in this battle', 'A concept unrelated to Canadian history', 'Only troops from other countries fought at Vimy Ridge'], 0),
   ('Is the Battle of Vimy Ridge remembered as significant to the development of Canadian identity?', ['Yes', 'No, it has no connection to Canadian identity', 'A concept unrelated to Vimy Ridge', 'This battle has been completely forgotten in Canadian history'], 0),
   ('Why might the Battle of Vimy Ridge be seen as a turning point in how Canada saw itself as a nation?', ['The victory demonstrated Canadian troops’ capability and unity as a distinct fighting force', 'The battle had no effect on how Canadians viewed their country', 'This concept has no connection to Canadian history', 'Canadian troops were not recognized for any achievement at Vimy Ridge'], 0),
   ('Why do Canadians continue to commemorate the Battle of Vimy Ridge today?', ['It honours the sacrifices made and reflects an important part of Canadian identity and history', 'This event has no ongoing significance to Canadians today', 'This concept has no relevance to History', 'Vimy Ridge is remembered only in a different country, not Canada'], 0)]),
]),

day(85, [
L('Reading: Analyzing Stream-of-Consciousness Narration',
  'Grade 8 Language strand: stream-of-consciousness narration presents a character’s continuous flow of thoughts and feelings as they occur, often without traditional sentence structure or clear organization.',
  [('What does stream-of-consciousness narration present?', ['A character’s continuous flow of thoughts and feelings', 'Only a strict, formal summary of events', 'A concept unrelated to reading', 'A list of characters with no thoughts included'], 0),
   ('Does stream-of-consciousness narration often follow traditional sentence structure?', ['No', 'Yes, it always follows strict traditional structure', 'A concept unrelated to narration', 'This style never includes any thoughts at all'], 0),
   ('Why might an author use stream-of-consciousness narration to portray a character’s inner experience?', ['It can create an intimate, realistic sense of how thoughts naturally occur', 'This style never reveals anything about a character’s inner experience', 'This concept has no connection to literature', 'Stream-of-consciousness narration always feels distant and impersonal'], 0),
   ('Why might stream-of-consciousness writing be more challenging for readers to follow?', ['Its lack of traditional structure can make the flow of ideas harder to track', 'This style is always easier to read than traditional narration', 'This concept has no connection to reading comprehension', 'Stream-of-consciousness writing never actually presents any complex ideas'], 0),
   ('Which of these best describes stream-of-consciousness narration?', ['A character’s thoughts flowing freely, jumping between ideas as they occur', 'A perfectly organized list of events in chronological order', 'A formal essay with a clear thesis and structured paragraphs', 'A dictionary definition of a single word'], 0)]),
M('Introduction to Vectors',
  'Grade 8 Math strand: a vector is a quantity that has both magnitude, or size, and direction, such as a force applied at a specific angle, often represented visually as an arrow.',
  [('What two things does a vector have?', ['Magnitude and direction', 'Only a colour', 'A concept unrelated to math', 'Only a single number with no direction'], 0),
   ('How is a vector often represented visually?', ['As an arrow', 'As a single dot only', 'A concept unrelated to vectors', 'As a random squiggle with no meaning'], 0),
   ('Does the length of a vector’s arrow typically represent its magnitude?', ['Yes', 'No, length has no connection to magnitude', 'A concept unrelated to vectors', 'The colour of the arrow always shows magnitude instead'], 0),
   ('Why might a vector be a more useful way to describe a force than just a single number?', ['A vector captures both how strong the force is and which direction it is applied', 'A single number always fully describes a force with no need for direction', 'This concept has no connection to vectors', 'Vectors never actually describe any real-world quantity'], 0),
   ('Which of these is an example of a vector quantity, since it includes both size and direction?', ['Wind blowing at 20 kilometres per hour toward the north', 'The temperature of a room', 'The number of students in a class', 'The price of an item at a store'], 0)]),
Sc('Science: The Science of Vaccines and Immunology',
   'Grade 8 Science strand: immunology studies how the immune system protects the body, and vaccines work by training this system to recognize specific pathogens before a real infection occurs.',
   [('What does immunology study?', ['How the immune system protects the body', 'How plants create their own food', 'A concept unrelated to biology', 'How rocks are formed over time'], 0),
    ('What do vaccines train the immune system to do?', ['Recognize specific pathogens', 'Ignore all pathogens completely', 'A concept unrelated to vaccines', 'Become permanently weaker'], 0),
    ('Do vaccines typically work before a real infection occurs?', ['Yes', 'No, vaccines only work after a person is already sick', 'A concept unrelated to vaccines', 'Vaccines have no connection to timing at all'], 0),
    ('Why might a vaccine include a small, harmless piece of a pathogen rather than the full, dangerous version?', ['It allows the immune system to learn and respond safely, without causing the actual illness', 'Vaccines always include the full, dangerous version of a pathogen', 'This concept has no connection to immunology', 'A harmless piece of a pathogen provides no useful immune response'], 0),
    ('Why is community-wide vaccination sometimes described as helping protect vulnerable individuals through herd immunity?', ['When enough people are immune, it becomes harder for a disease to spread, protecting those who cannot be vaccinated', 'Vaccinating a community never has any effect on how a disease spreads', 'This concept has no relevance to science', 'Herd immunity has no connection to vaccination at all'], 0)]),
H('The Founding of the CBC and Canadian Broadcasting',
  'Grade 8 History strand: the Canadian Broadcasting Corporation, founded in 1936, was created to provide national radio and later television programming that reflected Canadian stories and identity.',
  [('In what year was the Canadian Broadcasting Corporation founded?', ['1936', '1867', '1989', '1945'], 0),
   ('What does CBC stand for?', ['Canadian Broadcasting Corporation', 'Canadian Business Council', 'A concept unrelated to Canadian history', 'Central Broadcasting Committee'], 0),
   ('Was the CBC created to provide national radio and television programming?', ['Yes', 'No, it was created only to sell products', 'A concept unrelated to the CBC', 'The CBC has never provided any programming'], 0),
   ('Why might a national broadcaster like the CBC be considered important for Canadian identity?', ['It helps share stories and perspectives that reflect Canadian culture and experiences', 'A national broadcaster has no connection to a country’s identity', 'This concept has no connection to Canadian history', 'The CBC has never broadcast anything related to Canada'], 0),
   ('Why might a country choose to fund a public broadcaster instead of relying only on private companies?', ['A public broadcaster can prioritize national content and public interest over profit alone', 'Public broadcasters never provide any benefit over private companies', 'This concept has no relevance to History', 'Private companies always better represent a country’s identity'], 0)]),
]),

day(86, [
L('Writing: The Op-Ed Rebuttal',
  'Grade 8 Language strand: an op-ed rebuttal responds directly to another published opinion piece, presenting a counterargument supported by evidence and reasoning.',
  [('What does an op-ed rebuttal respond to?', ['Another published opinion piece', 'A math textbook', 'A concept unrelated to writing', 'A recipe for baking bread'], 0),
   ('Does an op-ed rebuttal present a counterargument supported by evidence?', ['Yes', 'No, it never includes any evidence', 'A concept unrelated to writing', 'A rebuttal only ever repeats the original argument'], 0),
   ('Why might a writer choose to write a rebuttal instead of ignoring an opposing opinion piece?', ['It allows them to directly challenge and respond to specific points made by the other writer', 'Rebuttals never actually engage with the original argument', 'This concept has no connection to writing', 'Ignoring an opposing viewpoint is always the better strategy'], 0),
   ('Which of these would most likely appear in an op-ed rebuttal?', ['While the original article claims X, the evidence actually suggests Y.', 'Once upon a time, there was a princess.', 'Add 9 and 3 to get 12.', 'The chemical symbol for helium is He.'], 0),
   ('Why is it important for an op-ed rebuttal to directly address the original argument’s points?', ['It makes the response more focused, credible, and persuasive to readers', 'Rebuttals are always more effective when they ignore the original argument completely', 'This concept has no connection to writing', 'Readers never care whether a rebuttal actually responds to the original piece'], 0)]),
M('Introduction to Amortization and Mortgages',
  'Grade 8 Math strand: amortization describes how a loan, such as a mortgage, is gradually paid off over time through regular payments that cover both interest and part of the original amount borrowed.',
  [('What does amortization describe?', ['How a loan is gradually paid off over time', 'A type of savings account with no payments', 'A concept unrelated to finance', 'A one-time payment with no ongoing schedule'], 0),
   ('Do regular loan payments typically cover both interest and part of the original amount borrowed?', ['Yes', 'No, payments only ever cover interest', 'A concept unrelated to amortization', 'Payments never actually reduce the original loan amount'], 0),
   ('What is a mortgage?', ['A loan used to purchase property, like a house', 'A type of car repair', 'A concept unrelated to finance', 'A savings account for retirement only'], 0),
   ('Why might early payments on a mortgage go mostly toward interest rather than the loan’s principal?', ['Interest is often calculated based on the remaining balance, which is highest at the start of the loan', 'Interest and principal are always paid in exactly equal amounts every month', 'This concept has no connection to amortization', 'Early payments never include any interest at all'], 0),
   ('Why is understanding amortization useful when considering a major purchase, like a home?', ['It helps someone understand the total cost and time it will take to pay off a loan', 'Amortization never affects how someone plans a major purchase', 'This concept has no relevance to financial literacy', 'Loans never need to be paid back over time'], 0)]),
Sc('Science: Renewable Materials: Bioplastics',
   'Grade 8 Science strand: bioplastics are materials made from renewable sources, such as corn starch or sugarcane, offering an alternative to traditional plastics made from petroleum.',
   [('What are bioplastics made from?', ['Renewable sources, such as corn starch or sugarcane', 'Only petroleum, just like traditional plastic', 'A concept unrelated to materials science', 'Only metal and glass'], 0),
    ('Are bioplastics considered an alternative to traditional plastics made from petroleum?', ['Yes', 'No, bioplastics have no connection to traditional plastics', 'A concept unrelated to bioplastics', 'Bioplastics are exactly the same as petroleum-based plastics'], 0),
    ('Name one renewable source that can be used to make bioplastics, such as corn starch.', ['Corn starch', 'A concept unrelated to bioplastics', 'Crude oil', 'Coal'], 0),
    ('Why might bioplastics be considered a more environmentally friendly option than some traditional plastics?', ['They can be made from renewable resources and may break down more easily in some cases', 'Bioplastics have no environmental benefit compared to traditional plastics', 'This concept has no connection to materials science', 'Traditional plastics are always more sustainable than bioplastics'], 0),
    ('Why might researchers continue working to improve bioplastic technology?', ['Some bioplastics still face challenges, like cost or how well they break down in different environments', 'Bioplastic technology has already been perfected with no room for improvement', 'This concept has no relevance to science', 'Bioplastics never have any limitations to address'], 0)]),
H('The 1995 Quebec Referendum',
  'Grade 8 History strand: the 1995 Quebec referendum asked Quebec voters whether the province should become sovereign, resulting in a very close vote to remain part of Canada.',
  [('In what year did the Quebec referendum on sovereignty take place?', ['1995', '1867', '1982', '1970'], 0),
   ('What question did the 1995 Quebec referendum ask voters?', ['Whether Quebec should become sovereign', 'Whether Canada should adopt a new flag', 'A concept unrelated to Canadian history', 'Whether Canada should join a new trade agreement'], 0),
   ('Was the result of the 1995 referendum a close vote?', ['Yes', 'No, it was an overwhelming landslide vote', 'A concept unrelated to the referendum', 'There was no vote at all'], 0),
   ('Why might the closeness of the 1995 referendum result be considered historically significant?', ['It highlighted deep and closely divided opinions about Quebec’s place within Canada', 'The result had no significance at all in Canadian history', 'This concept has no connection to Canadian history', 'The vote was never close and had an obvious outcome'], 0),
   ('Why is the 1995 Quebec referendum an important topic for understanding Canadian federalism?', ['It reflects ongoing questions about national unity and provincial identity within Canada', 'This event has no connection to Canadian federalism', 'This concept has no relevance to History', 'Quebec has never had any unique relationship with the rest of Canada'], 0)]),
]),

day(87, [
L('Media Literacy: Analyzing Deepfakes and Digital Manipulation',
  'Grade 8 Language strand: a deepfake is a digitally altered video or image, often created using artificial intelligence, that can make it appear someone said or did something they never actually did.',
  [('What is a deepfake?', ['A digitally altered video or image', 'A completely unedited, original recording', 'A concept unrelated to media literacy', 'A traditional printed newspaper article'], 0),
   ('Is artificial intelligence often used to create deepfakes?', ['Yes', 'No, deepfakes are never created using any technology', 'A concept unrelated to deepfakes', 'Deepfakes are always created without any digital tools'], 0),
   ('Can a deepfake make it appear someone said or did something they never actually did?', ['Yes', 'No, deepfakes never alter what appears to happen in a video', 'A concept unrelated to deepfakes', 'Deepfakes only ever show completely accurate events'], 0),
   ('Why might deepfakes pose a challenge for evaluating the reliability of online video content?', ['They can convincingly fabricate events, making it harder to know what is real', 'Deepfakes are always obviously fake and easy to identify', 'This concept has no connection to media literacy', 'Deepfakes have no effect on how believable a video seems'], 0),
   ('Why is it important for people to critically evaluate videos before believing or sharing them?', ['Digitally manipulated content, like deepfakes, can spread false information convincingly', 'Every video seen online is always completely authentic', 'This concept has no relevance to media literacy', 'Sharing unverified content never has any negative consequences'], 0)]),
M('Statistics: Z-Scores and Standardization',
  'Grade 8 Math strand: a z-score describes how many standard deviations a data point is from the mean, allowing different data sets to be compared on a standardized scale.',
  [('What does a z-score describe?', ['How many standard deviations a data point is from the mean', 'The exact value of a data point with no comparison', 'A concept unrelated to statistics', 'The total number of data points in a set'], 0),
   ('Can z-scores be used to compare data points from different data sets?', ['Yes', 'No, z-scores can never be used to compare different data sets', 'A concept unrelated to z-scores', 'Z-scores only apply to a single, specific data set with no comparison possible'], 0),
   ('If a data point has a z-score of 0, what does that tell you?', ['It is exactly at the mean', 'It is far above the mean', 'A concept unrelated to z-scores', 'It is far below the mean'], 0),
   ('If a data point has a positive z-score, is it above or below the mean?', ['Above the mean', 'Below the mean', 'A concept unrelated to z-scores', 'Exactly at the mean'], 0),
   ('Why might a z-score be useful for comparing a student’s test score to two different tests with different scoring scales?', ['It standardizes both scores so they can be fairly compared on the same scale', 'Z-scores never help with comparing different tests', 'This concept has no connection to statistics', 'Test scores can never be meaningfully compared to each other'], 0)]),
Sc('Science: The Physics of Black Holes',
   'Grade 8 Science strand: a black hole is a region in space with gravity so strong that nothing, not even light, can escape it, formed when a massive star collapses at the end of its life.',
   [('What is a black hole?', ['A region in space with gravity so strong nothing can escape it', 'A bright star that never changes', 'A concept unrelated to astronomy', 'An empty area of space with no gravity at all'], 0),
    ('Can light escape from a black hole?', ['No', 'Yes, light easily escapes a black hole', 'A concept unrelated to black holes', 'Only some types of light can escape'], 0),
    ('How does a black hole typically form?', ['When a massive star collapses at the end of its life', 'When a star is first formed from gas and dust', 'A concept unrelated to black holes', 'When a planet cools down over time'], 0),
    ('Why can’t scientists directly see a black hole, even with powerful telescopes?', ['A black hole itself emits no light, since even light cannot escape its gravity', 'Black holes are actually very easy to see directly with the naked eye', 'This concept has no connection to how black holes work', 'Black holes emit extremely bright light that can always be seen'], 0),
    ('Why do scientists study the effects of black holes on nearby stars and matter?', ['Observing these effects can provide indirect evidence about black holes since they cannot be seen directly', 'Nearby stars are never affected in any way by a black hole', 'This concept has no relevance to science', 'Black holes have no measurable effect on their surroundings'], 0)]),
H('Canada’s Role in Afghanistan',
  'Grade 8 History strand: Canada participated in the international military and humanitarian mission in Afghanistan beginning in 2001, contributing troops, aid, and reconstruction support over more than a decade.',
  [('Around what year did Canada begin its involvement in Afghanistan?', ['2001', '1867', '1945', '1970'], 0),
   ('Did Canada contribute troops to the mission in Afghanistan?', ['Yes', 'No, Canada had no military involvement in Afghanistan', 'A concept unrelated to Canadian history', 'Only humanitarian aid was ever provided, with no troops at all'], 0),
   ('Did Canada’s involvement in Afghanistan include reconstruction support?', ['Yes', 'No, reconstruction was never part of Canada’s role', 'A concept unrelated to Canada’s role in Afghanistan', 'Reconstruction support was provided by a completely different country only'], 0),
   ('Why might Canada’s mission in Afghanistan be considered a significant chapter in its modern military history?', ['It was one of Canada’s largest and longest military commitments in recent history', 'This mission had no impact on Canada’s military history', 'This concept has no connection to Canadian history', 'Canada has never participated in any international military missions'], 0),
   ('Why might learning about Canada’s international missions, like the one in Afghanistan, help students understand Canada’s global role?', ['It shows how Canada engages with international conflicts and humanitarian efforts abroad', 'Canada has no role in any international affairs', 'This concept has no relevance to History', 'International missions have no connection to a country’s global identity'], 0)]),
]),

day(88, [
L('Grammar: The Passive Voice in Scientific Writing',
  'Grade 8 Language strand: scientific writing often uses the passive voice, such as the solution was heated, to emphasize the process or results rather than who performed the action.',
  [('Does scientific writing often use the passive voice?', ['Yes', 'No, scientific writing never uses the passive voice', 'A concept unrelated to grammar', 'Only fiction writing uses the passive voice'], 0),
   ('In the passive voice sentence the solution was heated, what is emphasized?', ['The process or result', 'Who performed the action', 'A concept unrelated to passive voice', 'Neither the process nor who performed it'], 0),
   ('Which sentence is written in the passive voice?', ['The data was collected over three weeks.', 'We collected the data over three weeks.', 'I collected the data quickly.', 'They are collecting data now.'], 0),
   ('Why might a scientist choose the passive voice when describing an experiment’s procedure?', ['It keeps the focus on the scientific process rather than on the individual researcher', 'The passive voice always makes scientific writing less clear', 'This concept has no connection to grammar', 'Scientific writing should never focus on a process or result'], 0),
   ('Why might overusing the passive voice in writing sometimes make sentences feel less direct?', ['It can obscure who or what is responsible for an action', 'The passive voice always makes writing more direct and clear', 'This concept has no connection to writing style', 'The passive voice never has any effect on how direct a sentence feels'], 0)]),
M('Introduction to Spherical Geometry',
  'Grade 8 Math strand: spherical geometry studies shapes and distances on the surface of a sphere, where the shortest path between two points is a curved arc rather than a straight line.',
  [('What surface does spherical geometry study shapes and distances on?', ['A sphere', 'A flat plane only', 'A concept unrelated to geometry', 'A cube'], 0),
   ('On a sphere, is the shortest path between two points a straight line or a curved arc?', ['A curved arc', 'A straight line, just like on a flat plane', 'A concept unrelated to spherical geometry', 'There is no shortest path on a sphere'], 0),
   ('Why might the rules of spherical geometry differ from the geometry learned on a flat plane?', ['A curved surface changes how distances and angles behave compared to a flat surface', 'Spherical geometry and flat-plane geometry always follow the exact same rules', 'This concept has no connection to geometry', 'Spheres have no connection to geometry at all'], 0),
   ('Why is spherical geometry useful for navigation, such as planning airplane flight paths?', ['Earth is roughly spherical, so the shortest real-world routes follow curved paths', 'Flight paths are always planned using flat-plane geometry only', 'This concept has no connection to navigation', 'The shape of the Earth has no effect on how flights are planned'], 0),
   ('On a globe, would the shortest route between two distant cities usually look like a straight line on a flat map?', ['No, it usually appears as a curved line on a flat map', 'Yes, it always appears as a perfectly straight line', 'A concept unrelated to spherical geometry', 'There is never a shortest route between two cities'], 0)]),
Sc('Science: Epidemiology: Tracking the Spread of Disease',
   'Grade 8 Science strand: epidemiology is the study of how diseases spread through populations, helping scientists identify patterns, causes, and effective ways to control outbreaks.',
   [('What does epidemiology study?', ['How diseases spread through populations', 'How rocks form over millions of years', 'A concept unrelated to science', 'How plants convert sunlight into food'], 0),
    ('Can epidemiology help scientists identify patterns in how a disease spreads?', ['Yes', 'No, epidemiology has no connection to identifying patterns', 'A concept unrelated to epidemiology', 'Diseases never spread in any identifiable pattern'], 0),
    ('Does epidemiology help find effective ways to control disease outbreaks?', ['Yes', 'No, epidemiology has no connection to controlling outbreaks', 'A concept unrelated to epidemiology', 'Outbreaks can never be controlled in any way'], 0),
    ('Why might epidemiologists track how quickly a disease spreads from person to person?', ['This information helps predict future spread and guide public health responses', 'Tracking disease spread never provides any useful information', 'This concept has no connection to epidemiology', 'Diseases always spread at the exact same rate in every situation'], 0),
    ('Why is epidemiology considered an important field during a public health emergency?', ['It provides critical data to help guide decisions that protect public health', 'Epidemiology has no relevance during a public health emergency', 'This concept has no relevance to science', 'Public health emergencies never require any scientific data'], 0)]),
H('The Nisga’a Treaty and Modern Land Claims',
  'Grade 8 History strand: the Nisga’a Treaty, finalized in 2000, was a landmark modern land claims agreement that recognized Nisga’a self-government and land rights in British Columbia.',
  [('In what year was the Nisga’a Treaty finalized?', ['2000', '1867', '1945', '1970'], 0),
   ('Which Canadian province is associated with the Nisga’a Treaty?', ['British Columbia', 'Ontario', 'A concept unrelated to Canadian history', 'Nova Scotia'], 0),
   ('Did the Nisga’a Treaty recognize self-government and land rights?', ['Yes', 'No, it had no connection to self-government or land rights', 'A concept unrelated to the Nisga’a Treaty', 'The treaty removed all existing land rights'], 0),
   ('Why is the Nisga’a Treaty considered a landmark modern land claims agreement?', ['It was one of the first modern treaties to formally recognize Indigenous self-government in Canada', 'The treaty had no historical significance at all', 'This concept has no connection to Canadian history', 'Land claims agreements had never been discussed before this treaty'], 0),
   ('Why is it valuable for students to learn about modern treaties like the Nisga’a Treaty?', ['It helps show how Indigenous rights and governance continue to evolve through modern agreements', 'Modern treaties have no connection to understanding Indigenous history', 'This concept has no relevance to History', 'This treaty has no ongoing relevance in Canada today'], 0)]),
]),

day(89, [
L('Reading: Analyzing Bildungsroman: Coming-of-Age Stories',
  'Grade 8 Language strand: a bildungsroman is a story that follows a character’s psychological and moral growth from youth to adulthood, often centred on key formative experiences.',
  [('What is a bildungsroman?', ['A story following a character’s growth from youth to adulthood', 'A story with no central character at all', 'A concept unrelated to reading', 'A collection of unrelated short poems'], 0),
   ('Does a bildungsroman often focus on a character’s psychological and moral growth?', ['Yes', 'No, it never focuses on any character growth', 'A concept unrelated to bildungsroman', 'This type of story only focuses on physical setting, never growth'], 0),
   ('Might a bildungsroman include key formative experiences that shape the main character?', ['Yes', 'No, formative experiences are never included', 'A concept unrelated to bildungsroman', 'These stories never include any meaningful events'], 0),
   ('Why might readers relate to a bildungsroman even if the story is set in a different time or place?', ['The themes of growth, identity, and self-discovery can feel universal across different experiences', 'Readers can never relate to a story about a character’s growth', 'This concept has no connection to reading comprehension', 'Coming-of-age themes are never relatable to any reader'], 0),
   ('Which of these best describes the focus of a bildungsroman?', ['A young character’s journey toward maturity and self-understanding', 'A detailed description of a fictional city’s architecture', 'A step-by-step recipe for baking bread', 'A scientific report on a chemical reaction'], 0)]),
M('Solving Systems of Three Variables',
  'Grade 8 Math strand: a system of three variables involves three equations with three unknowns, solved by combining equations to eliminate variables one at a time until each unknown is found.',
  [('How many equations are typically needed to solve a system with three variables?', ['Three', 'One', 'Two', 'Five'], 0),
   ('What is a common strategy for solving a system of three variables?', ['Combining equations to eliminate variables one at a time', 'Guessing the answer with no calculation at all', 'A concept unrelated to systems of equations', 'Ignoring two of the three equations completely'], 0),
   ('If you eliminate one variable from two equations in a system of three, how many variables remain in that new equation?', ['Two', 'Three', 'One', 'Zero'], 0),
   ('Why might solving a system of three variables take more steps than solving a system of two variables?', ['There are more unknowns and equations to work through before finding each value', 'Systems of three variables never actually require any extra steps', 'This concept has no connection to algebra', 'Three-variable systems are always simpler to solve than two-variable systems'], 0),
   ('Why might a system of three variables be useful for solving a real-world problem involving three unknown quantities?', ['It allows all three unknowns to be determined at once using the given relationships', 'Real-world problems never involve more than one unknown quantity', 'This concept has no connection to math', 'Three-variable systems can never be applied to any real situation'], 0)]),
Sc('Science: The Chemistry of Batteries and Energy Storage',
   'Grade 8 Science strand: batteries store chemical energy and convert it into electrical energy through a chemical reaction between two different materials, called electrodes, separated by an electrolyte.',
   [('What type of energy do batteries store?', ['Chemical energy', 'Only light energy', 'A concept unrelated to batteries', 'Only sound energy'], 0),
    ('What are the two different materials in a battery, where the chemical reaction occurs, called?', ['Electrodes', 'A concept unrelated to batteries', 'Circuits', 'Insulators'], 0),
    ('What separates the two electrodes in a battery?', ['An electrolyte', 'A concept unrelated to batteries', 'A simple wire only', 'Nothing at all'], 0),
    ('Why might a rechargeable battery be able to reverse its chemical reaction?', ['Applying an external electrical current can reverse the chemical process, restoring the battery’s charge', 'Rechargeable batteries never actually reverse any chemical reaction', 'This concept has no connection to battery chemistry', 'All batteries work in exactly the same non-reversible way'], 0),
    ('Why is understanding battery chemistry important for developing better electric vehicles?', ['Improved battery technology could allow vehicles to store more energy and travel farther', 'Battery chemistry has no connection to electric vehicle technology', 'This concept has no relevance to science', 'Electric vehicles never actually rely on any battery technology'], 0)]),
H('The Truth and Reconciliation Commission’s 94 Calls to Action',
  'Grade 8 History strand: the Truth and Reconciliation Commission released 94 Calls to Action in 2015, recommending steps for governments, institutions, and Canadians to address the legacy of residential schools.',
  [('In what year did the Truth and Reconciliation Commission release its Calls to Action?', ['2015', '1867', '1945', '1970'], 0),
   ('How many Calls to Action did the Truth and Reconciliation Commission release?', ['94', '10', '50', '150'], 0),
   ('Do the Calls to Action address the legacy of residential schools?', ['Yes', 'No, they have no connection to residential schools', 'A concept unrelated to the Truth and Reconciliation Commission', 'They only address unrelated economic policies'], 0),
   ('Why might the Calls to Action involve recommendations for governments, institutions, and individual Canadians?', ['Addressing a legacy of harm requires action and change at multiple levels of society', 'The Calls to Action are only relevant to a single government department', 'This concept has no connection to Canadian history', 'Reconciliation efforts never require any action from institutions or individuals'], 0),
   ('Why is understanding the 94 Calls to Action important for students learning about reconciliation in Canada?', ['It provides concrete steps that reflect ongoing efforts to address historical harms and build a better future', 'The Calls to Action have no relevance to reconciliation efforts today', 'This concept has no relevance to History', 'Reconciliation in Canada has already been fully completed with nothing left to do'], 0)]),
]),

day(90, [
L('Review: Literary Analysis and Grammar (Days 81-89)',
  'Grade 8 Language strand review: students revisit anti-heroes, rhetorical analysis, correlative conjunctions, portmanteau words, stream-of-consciousness narration, op-ed rebuttals, deepfakes, passive voice, and bildungsroman.',
  [('What is an anti-hero?', ['A main character who lacks traditional heroic qualities', 'A villain with no role in the main plot', 'A concept unrelated to reading', 'A minor character with no importance'], 0),
   ('What does a rhetorical analysis essay examine?', ['How a writer or speaker uses persuasive techniques', 'Only the length of a text', 'A concept unrelated to writing', 'Only the punctuation used in a text'], 0),
   ('What does stream-of-consciousness narration present?', ['A character’s continuous flow of thoughts and feelings', 'Only a strict, formal summary of events', 'A concept unrelated to reading', 'A list of characters with no thoughts included'], 0),
   ('What is a deepfake?', ['A digitally altered video or image', 'A completely unedited, original recording', 'A concept unrelated to media literacy', 'A traditional printed newspaper article'], 0),
   ('What is a bildungsroman?', ['A story following a character’s growth from youth to adulthood', 'A story with no central character at all', 'A concept unrelated to reading', 'A collection of unrelated short poems'], 0)]),
M('Review: Advanced Algebra, Geometry, and Statistics (Days 81-89)',
  'Grade 8 Math strand review: students revisit the law of sines and cosines, matrices, normal distribution, completing the square, vectors, amortization, z-scores, spherical geometry, and systems of three variables.',
  [('What can the law of sines and cosines help you find in a triangle?', ['Missing sides or angles', 'Only the triangle’s colour', 'A concept unrelated to trigonometry', 'Only the triangle’s perimeter'], 0),
   ('What is a matrix?', ['A rectangular arrangement of numbers in rows and columns', 'A single number with no structure', 'A concept unrelated to math', 'A type of geometric shape only'], 0),
   ('What two things does a vector have?', ['Magnitude and direction', 'Only a colour', 'A concept unrelated to math', 'Only a single number with no direction'], 0),
   ('What does a z-score describe?', ['How many standard deviations a data point is from the mean', 'The exact value of a data point with no comparison', 'A concept unrelated to statistics', 'The total number of data points in a set'], 0),
   ('How many equations are typically needed to solve a system with three variables?', ['Three', 'One', 'Two', 'Five'], 0)]),
Sc('Review: Physics, Biology, and Chemistry (Days 81-89)',
   'Grade 8 Science strand review: students revisit epigenetics, superconductors, coral reefs, quantum physics, immunology, bioplastics, black holes, epidemiology, and battery chemistry.',
   [('What does epigenetics study?', ['How environmental factors influence whether genes are turned on or off', 'How genes are physically removed from an organism', 'A concept unrelated to biology', 'How DNA sequences are permanently rewritten'], 0),
    ('What builds a coral reef?', ['Colonies of tiny coral organisms', 'Large rocks that fall from cliffs', 'A concept unrelated to marine biology', 'Sand carried by ocean currents'], 0),
    ('What does quantum physics study?', ['The behaviour of extremely small particles', 'The behaviour of extremely large objects only', 'A concept unrelated to science', 'Only objects that are visible to the naked eye'], 0),
    ('What is a black hole?', ['A region in space with gravity so strong nothing can escape it', 'A bright star that never changes', 'A concept unrelated to astronomy', 'An empty area of space with no gravity at all'], 0),
    ('What does epidemiology study?', ['How diseases spread through populations', 'How rocks form over millions of years', 'A concept unrelated to science', 'How plants convert sunlight into food'], 0)]),
H('Review: Modern Canadian History and Reconciliation (Days 81-89)',
  'Grade 8 History strand review: students revisit the Chinese Immigration Act repeal, the Just Society, the fall of the Berlin Wall, Vimy Ridge, the CBC, the 1995 Quebec referendum, Afghanistan, the Nisga’a Treaty, and the 94 Calls to Action.',
  [('In what year was the Chinese Immigration Act repealed?', ['1947', '1867', '1988', '2001'], 0),
   ('Which prime minister promoted the idea of a Just Society?', ['Pierre Trudeau', 'A concept unrelated to Canadian history', 'A fictional political figure', 'A prime minister from a different country'], 0),
   ('In what year did the Battle of Vimy Ridge take place?', ['1917', '1867', '1945', '1812'], 0),
   ('In what year did the Quebec referendum on sovereignty take place?', ['1995', '1867', '1982', '1970'], 0),
   ('How many Calls to Action did the Truth and Reconciliation Commission release?', ['94', '10', '50', '150'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_81_90)
    append_to(8, g8_81_90)
