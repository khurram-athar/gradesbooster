#!/usr/bin/env python3
"""Grade 10, Days 161-170 -- extends Grade 10 from 160 to 170 days. Topics
chosen after grepping the existing Day 1-160 title list (data/grade10.json)
extensively to avoid any overlap: analyzing livestreaming and influencer
culture, nominal clauses and noun clauses, understatement and litotes, the
retrospective review, the quest narrative and the object of the quest,
analyzing comment sections and online discourse, semicolons and colons for
sentence control, anaphora and rhetorical repetition, and the personal essay
and the anecdote; curve sketching using the first and second derivative
tests, the twin prime conjecture, Type I and Type II errors in hypothesis
testing, tessellations and symmetry groups, the scalar triple product and
volume, trees and spanning trees in graph theory, the hypergeometric
distribution, simplifying complex rational expressions, and Newtons Method
for approximating roots; the chemistry of fireworks and flame tests, black
holes and gravitational collapse, permafrost and the changing Arctic,
hibernation, torpor, and metabolic adaptation, the chemistry of sunscreen
and ultraviolet protection, the physics of musical instruments and sound
production, hurricanes and tropical cyclone formation, bioaccumulation and
biomagnification in food chains, and household chemistry -- cleaning
products and chemical safety; the baby boom and postwar economic growth,
the Veterans Charter, the Canadian Citizenship Act of 1947, the Gouzenko
Affair, the founding of NATO in 1949, Louis St. Laurent and the politics of
Uncle Louis, the Old Age Security Act of 1951, the 1956 Pipeline Debate,
and the founding of the Canada Council for the Arts in 1957, continuing
directly from the Second World War history sequence that closed Days
151-160 into the early postwar and Cold War era of Canadian history.

None of the thirty-six new subject titles above, nor the four Day 170
review titles, duplicate any (subject, title) pair found in Days 1-160 --
confirmed by dumping and grepping the full existing title list before
writing this script. The known pre-existing duplicate History title "The
October Crisis and the War Measures Act" (occurring twice in Days 1-160)
predates this batch and is left untouched; no third occurrence is added.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used anywhere
in title/question/summary/option text -- apostrophes are dropped entirely,
matching the Days 111-160 convention.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


def _rebalance_answer_positions(days, seed=20260813):
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


g10_161_170 = [
day(161, [
E('Media Literacy: Analyzing Livestreaming and Influencer Culture',
  'Grade 10 English strand: livestreaming and influencer culture involve content creators broadcasting in real time or building a personal brand across social platforms, often blurring the line between authentic personal expression and commercial promotion aimed at a following audience.',
  [('What is a defining feature of livestreaming?', ['Broadcasting content to an audience in real time', 'Publishing a printed newspaper once a week', 'Recording a film with no audience of any kind', 'Mailing a letter to a single recipient'], 0),
   ('What does influencer culture typically involve?', ['A content creator building a personal brand and audience across social platforms', 'A government agency regulating all social media content', 'A library cataloguing printed books by subject', 'A factory manufacturing television sets'], 0),
   ('Why can influencer content blur the line between authenticity and promotion?', ['Creators often promote products or brands while presenting content as personal or unscripted', 'Influencers are legally required to avoid any promotional content', 'Influencer content never includes any personal opinion', 'Livestreams cannot include any commercial material by definition'], 0),
   ('What term describes a creators audience of regular followers?', ['A following', 'A jury', 'A congress', 'A committee'], 0),
   ('Why is media literacy useful when viewing livestreamed or influencer content?', ['It helps viewers recognize when personal content is also serving a promotional or commercial purpose', 'It guarantees that all influencer content is completely free of promotion', 'It removes any need to think critically about online content', 'It proves that livestreams are always entirely unscripted'], 0)]),
M('Calculus: Curve Sketching Using the First and Second Derivative Tests',
  'Grade 10 Math strand: curve sketching uses the first derivative to locate increasing and decreasing intervals and turning points, and the second derivative to determine concavity and inflection points, combining both tests to produce an accurate graph of a function without plotting every point.',
  [('What does the first derivative test help locate on a graph?', ['Increasing and decreasing intervals and turning points', 'The exact colour used to draw the graph', 'The total number of variables in the function', 'The name of the mathematician who defined the function'], 0),
   ('What does the second derivative test help determine?', ['Concavity and inflection points', 'The domain of a completely unrelated function', 'The exact y-intercept only', 'The number of times a graph must be redrawn'], 0),
   ('Why might a mathematician sketch a curve using derivative tests rather than plotting many points?', ['It produces an accurate graph efficiently by identifying key features directly', 'Plotting points is always mathematically impossible', 'Derivative tests remove the need for a graph to have any shape', 'It guarantees the graph will contain no curves of any kind'], 0),
   ('What indicates a local maximum when using the first derivative test?', ['The derivative changes from positive to negative at that point', 'The derivative remains zero across the entire domain', 'The function is undefined at every point nearby', 'The derivative changes from negative to more negative'], 0),
   ('What combined information do the first and second derivative tests provide together?', ['A complete picture of a functions shape, including turning points and concavity', 'The exact numeric value of every point on the graph', 'A list of unrelated historical dates', 'The colour scheme used in a textbook diagram'], 0)]),
Sc('Chemistry: The Chemistry of Fireworks and Flame Tests',
   'Grade 10 Science strand: a flame test identifies certain metal ions by observing the distinct colour their compounds produce when heated in a flame, a principle also used in fireworks, where specific metal salts are chosen to create vivid colours through the same excited-electron process.',
   [('What does a flame test identify?', ['Certain metal ions, based on the colour their compounds produce when heated', 'The exact temperature of a flame in degrees', 'The density of a solid object', 'The pH of a neutral solution'], 0),
    ('What causes the colour produced during a flame test?', ['Electrons absorbing energy and releasing it as light when they return to a lower energy level', 'A permanent chemical change that destroys the metal entirely', 'The reflection of surrounding room light off the flame', 'A change in the mass of the metal sample'], 0),
    ('How are flame test principles applied in fireworks?', ['Specific metal salts are chosen to produce particular colours when they burn', 'Fireworks never use any metal compounds at all', 'Fireworks rely only on the colour of the night sky', 'Colour in fireworks is added after the explosion using paint'], 0),
    ('Which metal is commonly associated with a bright red flame colour in fireworks?', ['Strontium', 'Helium', 'Argon', 'Neon'], 0),
    ('Why can flame tests be a useful first step in identifying an unknown compound?', ['A distinctive flame colour narrows down which metal ions might be present', 'Flame tests reveal the exact molecular formula with no other tests needed', 'Flame tests work equally well on any substance regardless of composition', 'Flame tests eliminate the need for any further chemical analysis'], 0)]),
H('The Baby Boom and Postwar Economic Growth in Canada',
  'Grade 10 History strand: the baby boom was a sharp rise in birth rates across Canada following the Second World War, accompanying rapid postwar economic growth, suburban expansion, and increased consumer spending that reshaped Canadian society through the late 1940s and 1950s.',
  [('What was the baby boom?', ['A sharp rise in birth rates across Canada following the Second World War', 'A sudden decline in the Canadian population after 1945', 'A federal law limiting family size', 'A period when no children were born in Canada'], 0),
   ('What economic trend accompanied the baby boom in Canada?', ['Rapid postwar economic growth', 'A prolonged nationwide economic depression', 'The complete collapse of the Canadian dollar', 'A total halt in all industrial production'], 0),
   ('What form of housing development expanded rapidly during this period?', ['Suburban housing', 'Underground housing built entirely below ground', 'Housing built exclusively in remote wilderness areas', 'Housing construction was banned across Canada'], 0),
   ('What consumer trend increased alongside the baby boom?', ['Consumer spending on homes, appliances, and automobiles', 'A nationwide boycott of all consumer goods', 'A strict rationing system that lasted through the 1950s', 'A total ban on the sale of automobiles'], 0),
   ('During which decades did the Canadian baby boom mainly occur?', ['The late 1940s and 1950s', 'The 1920s and 1930s', 'The 1960s and 1970s only', 'The 1980s and 1990s only'], 0)]),
]),
day(162, [
E('Grammar: Nominal Clauses and Noun Clauses',
  'Grade 10 English strand: a nominal clause, also called a noun clause, functions within a sentence the way a single noun would, serving as a subject, object, or complement, and is often introduced by words such as that, what, whoever, or whether.',
  [('What role does a nominal clause play in a sentence?', ['The same role a single noun would play, such as subject or object', 'The same role a preposition would play', 'The same role a comma would play', 'No grammatical role of any kind'], 0),
   ('Which word commonly introduces a nominal clause?', ['That', 'And', 'But', 'Or'], 0),
   ('Which sentence contains a nominal clause?', ['What she said surprised everyone.', 'She said something surprising.', 'Everyone was surprised.', 'The surprising statement was hers.'], 0),
   ('What is another common name for a nominal clause?', ['A noun clause', 'An adjective phrase', 'A prepositional phrase', 'An interjection'], 0),
   ('Why might a writer use a nominal clause instead of a simple noun?', ['To express a more complex idea that a single word cannot capture', 'To remove all meaning from a sentence', 'Because nominal clauses are never allowed in formal writing', 'To avoid ever using a subject in a sentence'], 0)]),
M('Number Theory: The Twin Prime Conjecture',
  'Grade 10 Math strand: the twin prime conjecture proposes that there are infinitely many pairs of prime numbers that differ by exactly two, such as 11 and 13, a statement that remains unproven despite being tested extensively for very large numbers.',
  [('What does the twin prime conjecture propose?', ['That there are infinitely many pairs of primes differing by exactly two', 'That every prime number is even', 'That no two prime numbers can ever differ by two', 'That prime numbers stop existing after a certain value'], 0),
   ('Which pair of numbers is an example of twin primes?', ['11 and 13', '10 and 12', '9 and 11', '14 and 16'], 0),
   ('Has the twin prime conjecture been proven?', ['No, it remains unproven despite extensive testing', 'Yes, it was proven in the eighteenth century', 'Yes, it was disproven with a single counterexample', 'It was proven true only for numbers less than ten'], 0),
   ('What branch of mathematics does the twin prime conjecture belong to?', ['Number theory', 'Trigonometry', 'Coordinate geometry', 'Statistics'], 0),
   ('Why do mathematicians continue to study the twin prime conjecture despite its difficulty?', ['Progress on the problem can reveal deeper patterns about how prime numbers are distributed', 'The conjecture has no connection to any other area of mathematics', 'Solving it would have no effect on number theory at all', 'It was already fully solved decades ago with no remaining questions'], 0)]),
Sc('Physics: Black Holes and Gravitational Collapse',
   'Grade 10 Science strand: a black hole forms when a massive star collapses under its own gravity after exhausting its nuclear fuel, creating a region of space with gravity so strong that nothing, not even light, can escape once it passes the event horizon.',
   [('How does a black hole typically form?', ['A massive star collapses under its own gravity after exhausting its nuclear fuel', 'A star suddenly gains a large amount of new mass from nowhere', 'A planet cools down completely and stops orbiting', 'Two asteroids collide at low speed'], 0),
    ('What is unable to escape a black hole once it crosses the event horizon?', ['Light', 'Sound travelling through a vacuum', 'Radio waves broadcast from Earth', 'Heat generated on a distant planet'], 0),
    ('What term describes the boundary around a black hole beyond which nothing can escape?', ['The event horizon', 'The photosphere', 'The magnetosphere', 'The troposphere'], 0),
    ('Why can a black hole not be observed directly with visible light?', ['No light escapes from within the event horizon', 'Black holes reflect all light perfectly', 'Black holes produce no gravity at all', 'Black holes are always located inside the atmosphere of a planet'], 0),
    ('What must a star typically have in order to eventually collapse into a black hole?', ['Enough mass to overcome the forces that normally support a stars structure', 'No mass at all', 'A perfectly circular orbit around another star', 'A temperature below absolute zero'], 0)]),
H('The Veterans Charter and Reintegration After the Second World War',
  'Grade 10 History strand: the Veterans Charter was a package of federal programs introduced after the Second World War to help returning Canadian soldiers reintegrate into civilian life through education grants, job placement support, and assistance purchasing homes or farms.',
  [('What was the Veterans Charter?', ['A package of federal programs to help returning soldiers reintegrate into civilian life', 'A treaty ending the Second World War in Europe', 'A new branch of the Canadian military', 'A federal tax imposed on returning veterans'], 0),
   ('Which of the following was included in the Veterans Charter?', ['Education grants for returning soldiers', 'A ban on veterans seeking employment', 'A requirement that veterans remain in the military for life', 'A prohibition on veterans owning property'], 0),
   ('What type of support did the Veterans Charter provide related to housing?', ['Assistance purchasing homes or farms', 'A requirement that veterans live in military barracks permanently', 'A ban on veterans owning any land', 'Free international travel with no housing support'], 0),
   ('Why did the federal government introduce the Veterans Charter after the war?', ['To help a large number of returning soldiers transition successfully into civilian life', 'To prevent veterans from ever working again', 'To keep soldiers enlisted in the military indefinitely', 'Because no soldiers were returning to Canada after the war'], 0),
   ('What broader postwar goal did the Veterans Charter support?', ['A stable and prosperous transition to a peacetime economy', 'A continuation of wartime rationing indefinitely', 'The permanent closure of Canadian universities', 'A return to a purely agricultural economy with no industry'], 0)]),
]),
day(163, [
E('Reading: Analyzing Understatement and Litotes',
  'Grade 10 English strand: understatement deliberately presents something as less significant than it actually is, often for ironic or humorous effect, and litotes is a specific form of understatement that uses a negative construction to affirm a positive, such as saying not bad to mean very good.',
  [('What does understatement do?', ['Deliberately presents something as less significant than it actually is', 'Exaggerates an idea far beyond its actual size', 'Repeats the same word at the start of several clauses', 'Compares two unlike things using like or as'], 0),
   ('What is litotes?', ['A form of understatement that uses a negative construction to affirm a positive', 'A form of exaggeration used to inflate an idea', 'A device that gives human traits to an animal', 'A word that imitates the sound it describes'], 0),
   ('Which phrase is an example of litotes?', ['Saying the exam was not the easiest to describe a very difficult exam', 'Saying the exam was the hardest thing in the entire universe', 'Saying the exam felt like climbing a mountain of fire', 'Saying the exam was as easy as breathing'], 0),
   ('Why might a writer use understatement?', ['To create an ironic or humorous effect', 'To make an idea seem far larger than it actually is', 'To remove all meaning from a sentence', 'To confuse the reader with unrelated information'], 0),
   ('How does understatement differ from hyperbole?', ['Understatement minimizes something, while hyperbole exaggerates it', 'The two devices are identical in every way', 'Understatement always uses negative words, and hyperbole never does', 'Hyperbole minimizes something, while understatement exaggerates it'], 0)]),
M('Statistics: Type I and Type II Errors in Hypothesis Testing',
  'Grade 10 Math strand: in hypothesis testing, a Type I error occurs when a true null hypothesis is incorrectly rejected, while a Type II error occurs when a false null hypothesis is incorrectly accepted, and understanding both helps researchers weigh the risks of drawing an incorrect conclusion.',
  [('What is a Type I error?', ['Incorrectly rejecting a null hypothesis that is actually true', 'Correctly rejecting a null hypothesis that is actually false', 'Incorrectly accepting a null hypothesis that is actually false', 'Correctly accepting a null hypothesis that is actually true'], 0),
   ('What is a Type II error?', ['Incorrectly failing to reject a null hypothesis that is actually false', 'Incorrectly rejecting a null hypothesis that is actually true', 'Correctly identifying every result in a data set', 'A calculation error unrelated to hypothesis testing'], 0),
   ('Why is it useful for researchers to understand both types of error?', ['It helps them weigh the risks of drawing an incorrect conclusion from a test', 'It guarantees that no error can ever occur in a study', 'It removes the need to ever collect any data', 'It proves that hypothesis testing is never useful'], 0),
   ('Which term describes rejecting a true null hypothesis?', ['A Type I error', 'A Type II error', 'A sampling frame', 'A confidence interval'], 0),
   ('In hypothesis testing, what does the null hypothesis typically represent?', ['A default claim of no effect or no difference', 'A claim that is always assumed to be false from the start', 'A random guess with no statistical meaning', 'The final conclusion of every study'], 0)]),
Sc('Earth Science: Permafrost and the Changing Arctic',
   'Grade 10 Science strand: permafrost is ground that remains frozen for at least two consecutive years, common across much of the Canadian Arctic, and its thawing due to a warming climate can destabilize infrastructure, release stored greenhouse gases, and alter northern ecosystems.',
   [('What is permafrost?', ['Ground that remains frozen for at least two consecutive years', 'Ice that forms only on the surface of the ocean', 'A type of rock found only near volcanoes', 'Snow that falls once and never melts anywhere'], 0),
    ('Where is permafrost commonly found in Canada?', ['Across much of the Canadian Arctic', 'Only in southern Ontario', 'Only along the Pacific coastline', 'Only in the Great Lakes region'], 0),
    ('What can happen to infrastructure built on permafrost that begins to thaw?', ['It can become destabilized as the ground shifts', 'It automatically becomes stronger and more stable', 'It is completely unaffected by any ground movement', 'It converts entirely into a different building material'], 0),
    ('What greenhouse gas concern is associated with thawing permafrost?', ['Thawing permafrost can release stored greenhouse gases such as methane', 'Thawing permafrost removes all greenhouse gases from the atmosphere', 'Thawing permafrost has no connection to atmospheric gases', 'Thawing permafrost only releases oxygen into the atmosphere'], 0),
    ('What is driving the widespread thawing of permafrost in recent decades?', ['A warming climate', 'A sudden decrease in global temperatures', 'A reduction in the amount of ice at the poles', 'A decline in ocean salinity worldwide'], 0)]),
H('The Canadian Citizenship Act of 1947',
  'Grade 10 History strand: the Canadian Citizenship Act of 1947 created a distinct legal status of Canadian citizen for the first time, separate from British subject status, and took effect on January 1, 1947, with Prime Minister Mackenzie King becoming the first person to be granted Canadian citizenship.',
  [('What did the Canadian Citizenship Act of 1947 create for the first time?', ['A distinct legal status of Canadian citizen, separate from British subject status', 'A new Canadian currency', 'A new Canadian flag', 'A new provincial border'], 0),
   ('On what date did the Canadian Citizenship Act take effect?', ['January 1, 1947', 'July 1, 1867', 'September 1, 1939', 'May 8, 1945'], 0),
   ('Who became the first person granted Canadian citizenship under the new Act?', ['Prime Minister Mackenzie King', 'Prime Minister Robert Borden', 'Prime Minister Wilfrid Laurier', 'Prime Minister Lester Pearson'], 0),
   ('Before 1947, what legal status did people born in Canada generally hold?', ['British subject status', 'American citizen status', 'French citizen status', 'No legal status of any kind'], 0),
   ('Why is the Canadian Citizenship Act of 1947 considered a significant milestone?', ['It formally established a distinct Canadian national identity in law', 'It ended all immigration to Canada permanently', 'It abolished the Canadian Parliament', 'It merged Canada with another country'], 0)]),
]),
day(164, [
E('Writing: The Retrospective Review (Book, Film, or Album)',
  'Grade 10 English strand: a retrospective review looks back on a book, film, or album some time after its original release, evaluating how well it has aged, what lasting influence it has had, and how it might be understood differently by a present-day audience.',
  [('What does a retrospective review typically do?', ['Looks back on a work some time after its original release to evaluate it anew', 'Reviews a work before it has ever been released to the public', 'Summarizes a work without offering any evaluation', 'Focuses only on the price of the original release'], 0),
   ('What might a retrospective review consider that a review at the time of release could not?', ['How well the work has aged and what lasting influence it has had', 'The exact date the work was first released', 'The name of the original publisher only', 'The original cover price of the work'], 0),
   ('Why might a present-day audience interpret an older work differently than its original audience did?', ['Cultural context and expectations change over time', 'Older works never contain any meaning at all', 'Audiences never change their perspective over time', 'Only the original audience is capable of understanding a work'], 0),
   ('Which of the following could be the subject of a retrospective review?', ['A film released twenty years ago', 'A weather forecast for tomorrow', 'A live sports score being updated in real time', 'A recipe with no connection to any creative work'], 0),
   ('What skill does writing a retrospective review help a student practise?', ['Evaluating a work critically using both historical and present-day context', 'Memorizing a work word for word with no analysis', 'Avoiding any personal judgment about a work', 'Summarizing a work with no reference to its context'], 0)]),
M('Geometry: Tessellations and Symmetry Groups',
  'Grade 10 Math strand: a tessellation is a pattern of shapes that covers a plane with no gaps or overlaps, and the symmetry group of a tessellation describes the full set of rotations, reflections, and translations that map the pattern onto itself.',
  [('What is a tessellation?', ['A pattern of shapes that covers a plane with no gaps or overlaps', 'A single isolated point on a coordinate plane', 'A three-dimensional solid with no flat faces', 'A graph with no defined shape at all'], 0),
   ('What does the symmetry group of a tessellation describe?', ['The full set of rotations, reflections, and translations that map the pattern onto itself', 'The exact colour used to shade the pattern', 'The total number of shapes used in a single tessellation', 'The name of the artist who created the pattern'], 0),
   ('Which regular polygon can tessellate a plane on its own?', ['A square', 'A regular pentagon', 'A regular heptagon', 'A regular nonagon'], 0),
   ('What type of transformation slides a shape without rotating or flipping it?', ['A translation', 'A reflection', 'A dilation', 'A rotation'], 0),
   ('Why are tessellations studied in both mathematics and art?', ['They combine geometric structure with visually repeating patterns', 'They have no connection to visual design of any kind', 'They can only be created using irrational numbers', 'They cannot be found in any real architectural design'], 0)]),
Sc('Biology: Hibernation, Torpor, and Metabolic Adaptation',
   'Grade 10 Science strand: hibernation is a prolonged state of reduced metabolic activity that some animals enter to survive periods of cold and food scarcity, while torpor describes a shorter-term, less extreme drop in body temperature and metabolism used by other animals to conserve energy.',
   [('What is hibernation?', ['A prolonged state of reduced metabolic activity used to survive cold and food scarcity', 'A permanent state that an animal never leaves once it begins', 'A behaviour found only in plants, never in animals', 'A sudden increase in metabolic rate during summer'], 0),
    ('How does torpor differ from hibernation?', ['Torpor is a shorter-term, less extreme drop in metabolism and body temperature', 'Torpor always lasts longer than hibernation', 'Torpor involves a permanent increase in body temperature', 'Torpor and hibernation are identical in every respect'], 0),
    ('Why might an animal enter hibernation or torpor?', ['To conserve energy during periods when food is scarce', 'To increase its body temperature as high as possible', 'To attract more predators to its location', 'To permanently stop all bodily functions'], 0),
    ('What body process slows significantly during hibernation?', ['Metabolic rate', 'The rate of tooth growth', 'The rate of fur colour change', 'The rate of eye colour change'], 0),
    ('Which environmental condition commonly triggers hibernation in many mammals?', ['Cold temperatures and reduced food availability in winter', 'Warm temperatures and abundant food in summer', 'A sudden increase in daylight hours', 'A rise in ocean water levels'], 0)]),
H('The Gouzenko Affair and Early Cold War Espionage in Canada',
  'Grade 10 History strand: the Gouzenko Affair began in 1945 when Soviet embassy clerk Igor Gouzenko defected in Ottawa with documents revealing a Soviet spy network operating in Canada, an event widely seen as an early spark of the Cold War and a wake-up call about espionage among wartime allies.',
  [('Who was Igor Gouzenko?', ['A Soviet embassy clerk who defected in Ottawa in 1945', 'A Canadian prime minister during the Second World War', 'A German general who surrendered in 1945', 'A British diplomat stationed in Washington'], 0),
   ('What did Gouzenko reveal when he defected?', ['Documents exposing a Soviet spy network operating in Canada', 'A plan to invade Canada by sea', 'A treaty ending the Second World War', 'A new design for a Canadian warship'], 0),
   ('In what city did the Gouzenko Affair take place?', ['Ottawa', 'Halifax', 'Vancouver', 'Winnipeg'], 0),
   ('What broader historical period is the Gouzenko Affair often seen as an early spark of?', ['The Cold War', 'The First World War', 'The Great Depression', 'The Confederation era'], 0),
   ('Why was the Gouzenko Affair significant for Canada-Soviet relations among wartime allies?', ['It exposed espionage that undermined trust between former wartime allies', 'It strengthened trust between Canada and the Soviet Union permanently', 'It had no effect on international relations of any kind', 'It led to an immediate military alliance between Canada and the Soviet Union'], 0)]),
]),
day(165, [
E('Literature: The Quest Narrative and the Object of the Quest',
  'Grade 10 English strand: a quest narrative follows a protagonist on a journey to obtain a specific object, place, or goal, encountering obstacles and allies along the way, with the pursuit of that object often serving as a vehicle for the protagonists inner growth or transformation.',
  [('What does a quest narrative typically follow?', ['A protagonist on a journey to obtain a specific object, place, or goal', 'A static character who never leaves a single room', 'A list of unrelated historical facts with no protagonist', 'A scientific report with no narrative elements'], 0),
   ('What might a protagonist encounter during a quest narrative?', ['Obstacles and allies along the journey', 'No characters or challenges of any kind', 'A story with no setting described at all', 'A narrative that never leaves the opening scene'], 0),
   ('What deeper purpose can the pursuit of the quest object serve in the story?', ['A vehicle for the protagonists inner growth or transformation', 'A device that prevents any character development', 'A way to avoid ever resolving the plot', 'A method for eliminating conflict from the story entirely'], 0),
   ('Which of the following is an example of a quest object in a quest narrative?', ['A legendary artifact the protagonist must retrieve', 'A grocery list with no connection to the plot', 'A weather report unrelated to the story', 'A footnote citing an unrelated source'], 0),
   ('Why is the structure of a quest narrative useful for exploring character development?', ['The challenges faced along the journey reveal and change who the protagonist is', 'Quest narratives never include any character development', 'The protagonist remains completely unchanged by the journey in every case', 'Quest narratives are defined by having no protagonist at all'], 0)]),
M('Vectors: The Scalar Triple Product and Volume',
  'Grade 10 Math strand: the scalar triple product combines the dot product and cross product of three vectors to produce a single number equal to the volume of the parallelepiped formed by those vectors, providing a way to test whether three vectors lie in the same plane.',
  [('What does the scalar triple product of three vectors produce?', ['A single number equal to the volume of the parallelepiped formed by the vectors', 'A new vector perpendicular to all three original vectors', 'A matrix with no numerical value', 'A single point with no coordinates'], 0),
   ('Which two vector operations are combined to compute the scalar triple product?', ['The dot product and the cross product', 'Addition and subtraction only', 'Multiplication by a scalar only', 'Division of two vectors'], 0),
   ('What does a scalar triple product equal to zero indicate about three vectors?', ['The vectors are coplanar, lying in the same plane', 'The vectors form a perfect cube with maximum volume', 'The vectors cannot be graphed in three dimensions', 'The vectors are always perpendicular to one another'], 0),
   ('What geometric shape is associated with the scalar triple product?', ['A parallelepiped', 'A perfect sphere', 'A regular pentagon', 'A single straight line'], 0),
   ('Why is the scalar triple product useful in three-dimensional geometry?', ['It provides a way to calculate volume and test whether vectors are coplanar', 'It can only be used to measure angles in two dimensions', 'It eliminates the need to ever use a cross product', 'It has no connection to volume or coplanarity of any kind'], 0)]),
Sc('Chemistry: The Chemistry of Sunscreen and Ultraviolet Protection',
   'Grade 10 Science strand: sunscreen protects skin from ultraviolet radiation using chemical compounds that absorb UV light or physical mineral particles that reflect and scatter it, reducing the risk of sunburn and long-term skin damage caused by prolonged sun exposure.',
   [('What does sunscreen protect the skin from?', ['Ultraviolet radiation', 'Visible light of any colour', 'Cold temperatures only', 'Airborne pollen only'], 0),
    ('How do chemical sunscreen compounds typically work?', ['They absorb ultraviolet light before it can damage the skin', 'They permanently change the colour of the skin', 'They block all forms of light entirely', 'They have no interaction with light of any kind'], 0),
    ('How do physical mineral sunscreen ingredients typically work?', ['They reflect and scatter ultraviolet light away from the skin', 'They dissolve completely into the skin with no protective effect', 'They absorb only visible light and ignore ultraviolet light', 'They increase the skins sensitivity to sunlight'], 0),
    ('What long-term risk can prolonged unprotected sun exposure increase?', ['The risk of skin damage and skin cancer', 'The risk of developing colour blindness', 'The risk of losing a sense of taste', 'The risk of developing hearing loss'], 0),
    ('Why might a sunscreen be labelled with a specific protection factor number?', ['To indicate how effectively it filters ultraviolet radiation', 'To indicate the exact price of the product', 'To indicate the weight of the bottle', 'To indicate an unrelated nutritional value'], 0)]),
H('The Founding of NATO and Canadas Cold War Commitment, 1949',
  'Grade 10 History strand: Canada was a founding member of the North Atlantic Treaty Organization in 1949, a military alliance formed among Western nations to provide collective defence against the perceived threat of Soviet expansion during the early Cold War.',
  [('What was NATO formed to provide among its member nations?', ['Collective defence against a shared threat', 'A shared currency for all member nations', 'A single unified national anthem', 'A ban on all international trade'], 0),
   ('In what year was NATO founded?', ['1949', '1919', '1939', '1957'], 0),
   ('What role did Canada play in the founding of NATO?', ['Canada was a founding member', 'Canada refused to join NATO at any point', 'Canada joined NATO only after the year 2000', 'Canada was excluded from NATO membership entirely'], 0),
   ('What perceived threat motivated the formation of NATO?', ['Soviet expansion during the early Cold War', 'An invasion by a South American nation', 'A trade dispute with Australia', 'A famine affecting Western Europe'], 0),
   ('What broader global tension was NATO formed in response to?', ['The onset of the Cold War between Western nations and the Soviet Union', 'The conclusion of the First World War', 'A dispute over Arctic fishing rights', 'The founding of the League of Nations'], 0)]),
]),
day(166, [
E('Media Literacy: Analyzing Comment Sections and Online Discourse',
  'Grade 10 English strand: comment sections and online discourse allow readers to respond publicly to digital content, creating a space for discussion that can range from informative debate to hostility, and requiring critical judgment to separate credible contributions from misinformation or harassment.',
  [('What do comment sections allow readers to do?', ['Respond publicly to digital content', 'Print a physical copy of an article', 'Delete an article from the internet entirely', 'Prevent any other reader from seeing an article'], 0),
   ('What range of tone can online discourse in comment sections display?', ['It can range from informative debate to hostility', 'It is always perfectly calm with no disagreement', 'It never includes any opinion of any kind', 'It is limited entirely to a single approved response'], 0),
   ('Why does reading a comment section require critical judgment?', ['To separate credible contributions from misinformation or harassment', 'Because every comment posted online is always accurate', 'Because comment sections never contain any opinions', 'Because critical judgment is never necessary online'], 0),
   ('Which of the following might appear in an online comment section?', ['A thoughtful reply that adds relevant context to an article', 'A printed newspaper clipping mailed to the editor', 'A handwritten letter delivered by post', 'A radio broadcast transcript from decades ago'], 0),
   ('Why might a reader be cautious about accepting claims made in an online comment as fact?', ['Anonymous commenters may not provide verified or accurate information', 'All online comments are professionally fact-checked before posting', 'Comment sections are legally required to contain only true statements', 'Every commenter online is a credentialed expert'], 0)]),
M('Discrete Math: Trees and Spanning Trees in Graph Theory',
  'Grade 10 Math strand: in graph theory, a tree is a connected graph with no cycles, and a spanning tree of a larger graph is a subgraph that includes every vertex while using the minimum number of edges needed to keep the graph connected.',
  [('What defines a tree in graph theory?', ['A connected graph with no cycles', 'A graph with no vertices at all', 'A graph that must contain at least one cycle', 'A graph with an infinite number of edges'], 0),
   ('What is a spanning tree of a graph?', ['A subgraph that includes every vertex while using the minimum number of edges to stay connected', 'A graph with no connection to the original vertices', 'A tree that contains no vertices whatsoever', 'A graph that removes every vertex from the original'], 0),
   ('Why does a spanning tree contain no cycles?', ['Removing a cycle keeps all vertices connected while using fewer edges', 'Cycles are required in every spanning tree', 'A spanning tree must contain more edges than the original graph', 'Spanning trees are defined only by their vertices, never their edges'], 0),
   ('Which real-world problem can be modelled using spanning trees?', ['Designing a network that connects every location with the least amount of cable', 'Measuring the exact temperature of a room', 'Calculating the area of a circle', 'Finding the derivative of a polynomial function'], 0),
   ('How does a spanning tree relate to the original graph it comes from?', ['It uses a subset of the original graphs edges to connect all the same vertices', 'It contains entirely new vertices unrelated to the original graph', 'It always contains more edges than the original graph', 'It has no relationship to the original graph at all'], 0)]),
Sc('Physics: The Physics of Musical Instruments and Sound Production',
   'Grade 10 Science strand: musical instruments produce sound through vibrating strings, air columns, or membranes, with pitch determined by the frequency of vibration and factors such as length, tension, and material shaping the specific sound each instrument produces.',
   [('How do musical instruments generally produce sound?', ['Through vibrating strings, air columns, or membranes', 'By absorbing all surrounding light', 'By remaining completely motionless at all times', 'By changing colour in response to temperature'], 0),
    ('What determines the pitch of a musical sound?', ['The frequency of vibration', 'The colour of the instrument', 'The weight of the musician playing it', 'The time of day the instrument is played'], 0),
    ('Which factor can affect the pitch produced by a vibrating string?', ['The length and tension of the string', 'The colour of the string', 'The brand name printed on the instrument', 'The temperature of the room only'], 0),
    ('How does a wind instrument such as a flute typically produce sound?', ['By vibrating a column of air within the instrument', 'By vibrating a metal string stretched across its body', 'By striking a stretched membrane with a mallet', 'By absorbing sound waves with no vibration involved'], 0),
    ('Why do different instruments playing the same note still sound different from one another?', ['Each instrument produces a distinct combination of overtones alongside the fundamental frequency', 'All instruments produce identical sound waves with no variation', 'Only the volume of the note changes between instruments', 'Pitch has no connection to how an instrument sounds'], 0)]),
H('Louis St. Laurent and the Politics of Uncle Louis',
  'Grade 10 History strand: Louis St. Laurent served as prime minister of Canada from 1948 to 1957, presiding over a period of postwar prosperity and expanding federal programs, and earned the affectionate nickname Uncle Louis for his approachable public image during the era of early television politics.',
  [('From what years did Louis St. Laurent serve as prime minister of Canada?', ['1948 to 1957', '1867 to 1873', '1935 to 1948', '1957 to 1963'], 0),
   ('What nickname was Louis St. Laurent given?', ['Uncle Louis', 'The Little Prince', 'The Iron Duke', 'The Great Reformer'], 0),
   ('What kind of period did St. Laurents government preside over?', ['A period of postwar prosperity and expanding federal programs', 'A period of severe economic depression', 'A period with no federal government in operation', 'A period of open military conflict within Canada'], 0),
   ('Why did St. Laurent earn his approachable nickname?', ['His public image connected well with voters during the era of early television politics', 'He refused to ever appear in public', 'He was never seen by the Canadian public', 'He avoided all forms of media entirely'], 0),
   ('What broader economic condition characterized much of the St. Laurent era?', ['Postwar economic prosperity', 'A prolonged nationwide famine', 'A complete halt in international trade', 'A currency collapse across North America'], 0)]),
]),
day(167, [
E('Grammar: Semicolons, Colons, and Sentence Control',
  'Grade 10 English strand: a semicolon joins two closely related independent clauses without a coordinating conjunction, while a colon introduces a list, explanation, or elaboration that follows a complete independent clause, and both punctuation marks give a writer precise control over sentence structure.',
  [('What can a semicolon join?', ['Two closely related independent clauses without a coordinating conjunction', 'A single word and a period with no clause involved', 'Two unrelated paragraphs from different documents', 'A title and a page number only'], 0),
   ('What does a colon typically introduce?', ['A list, explanation, or elaboration following a complete independent clause', 'A brand new unrelated paragraph with no connection to the sentence', 'A question with no relationship to the preceding sentence', 'A single unrelated letter of the alphabet'], 0),
   ('Which sentence correctly uses a semicolon?', ['The rain stopped; the sun came out.', 'The rain stopped; and the sun came out.', 'The rain; stopped the sun came out.', 'The rain stopped the; sun came out.'], 0),
   ('What must generally precede a colon for it to be used correctly?', ['A complete independent clause', 'A single comma with no other words', 'An unrelated exclamation point', 'A blank line with no text at all'], 0),
   ('Why might a writer choose a semicolon instead of a period between two related sentences?', ['To show a closer relationship between the two ideas than a period would suggest', 'To make the two ideas seem completely unrelated', 'Because a semicolon always ends a sentence permanently', 'Because a semicolon removes all meaning from a sentence'], 0)]),
M('Probability: The Hypergeometric Distribution',
  'Grade 10 Math strand: the hypergeometric distribution models the probability of a specific number of successes when sampling without replacement from a finite population containing a known number of successes and failures, distinguishing it from the binomial distribution, which assumes sampling with replacement.',
  [('What does the hypergeometric distribution model?', ['The probability of a specific number of successes when sampling without replacement', 'The probability of an event that never occurs', 'The area under a normal curve only', 'The slope of a line between two points'], 0),
   ('How does the hypergeometric distribution differ from the binomial distribution?', ['It assumes sampling without replacement from a finite population, rather than with replacement', 'It assumes an infinite population with no fixed size', 'It cannot be used to calculate any probability', 'It is mathematically identical to the binomial distribution in every case'], 0),
   ('What must be known about the population to apply the hypergeometric distribution?', ['The number of successes and failures in the finite population', 'The exact colour of every item in the population', 'The geographic location where the population was measured', 'The name of the researcher conducting the study'], 0),
   ('Which scenario could be modelled with a hypergeometric distribution?', ['Drawing a hand of cards from a deck without putting any cards back', 'Flipping a fair coin an infinite number of times', 'Measuring the exact height of a single building', 'Calculating the derivative of a polynomial function'], 0),
   ('Why does sampling without replacement change the probability calculation compared to sampling with replacement?', ['Each draw changes the composition of the remaining population, affecting later probabilities', 'Sampling without replacement has no effect on probability at all', 'Sampling without replacement always produces identical results to sampling with replacement', 'Sampling without replacement removes the need for any calculation'], 0)]),
Sc('Earth Science: Hurricanes and Tropical Cyclone Formation',
   'Grade 10 Science strand: a hurricane is a powerful tropical cyclone that forms over warm ocean water when converging winds and rising warm, moist air organize into a rotating storm system, drawing energy from ocean heat and releasing it through intense wind and rainfall.',
   [('Over what type of environment do hurricanes typically form?', ['Warm ocean water', 'Frozen tundra', 'A dry desert with no moisture', 'A mountain range far from any ocean'], 0),
    ('What powers a hurricanes intensity?', ['Energy drawn from warm ocean water', 'Energy drawn from cold mountain air', 'Energy drawn from underground caves', 'Energy drawn from a nearby volcano'], 0),
    ('What atmospheric motion characterizes a hurricane?', ['A rotating storm system of converging winds', 'A completely still mass of air with no wind', 'A single straight-line wind with no rotation', 'A stationary cloud with no movement at all'], 0),
    ('What term describes hurricanes and similar storms occurring in different regions of the world?', ['Tropical cyclones', 'Cold fronts', 'Blizzards', 'Sandstorms'], 0),
    ('Why do hurricanes typically weaken after making landfall?', ['They lose their primary energy source once they move away from warm ocean water', 'They gain additional energy once they reach land', 'Land always increases the wind speed of a hurricane', 'Hurricanes are unaffected by whether they are over land or ocean'], 0)]),
H('The Old Age Security Act of 1951',
  'Grade 10 History strand: the Old Age Security Act of 1951 established a universal federal pension paid to Canadians aged seventy and older regardless of income, replacing the earlier means-tested Old Age Pensions Act of 1927 and expanding the reach of Canadas social safety net.',
  [('What did the Old Age Security Act of 1951 establish?', ['A universal federal pension paid to Canadians aged seventy and older', 'A new national holiday for seniors', 'A ban on retirement before the age of seventy', 'A provincial tax exclusive to Quebec'], 0),
   ('What earlier program did the Old Age Security Act replace?', ['The means-tested Old Age Pensions Act of 1927', 'The National Housing Act of 1938', 'The National Resources Mobilization Act of 1940', 'The Canadian Citizenship Act of 1947'], 0),
   ('What made the new pension under the 1951 Act different from the earlier program?', ['It was paid universally regardless of income, rather than being means-tested', 'It was only available to citizens under the age of twenty', 'It required recipients to have no prior employment history', 'It eliminated all federal pensions entirely'], 0),
   ('At what age were Canadians originally eligible for the pension under the 1951 Act?', ['Seventy', 'Fifty', 'Eighty-five', 'Thirty'], 0),
   ('What broader trend did the Old Age Security Act reflect in postwar Canada?', ['The expansion of Canadas social safety net', 'The elimination of all federal social programs', 'A shift away from any form of government pension', 'A reduction in the voting age across Canada'], 0)]),
]),
day(168, [
E('Reading: Analyzing Anaphora and Rhetorical Repetition',
  'Grade 10 English strand: anaphora is a rhetorical device in which a word or phrase is deliberately repeated at the beginning of successive clauses or sentences, building rhythm and emphasis to reinforce an idea or stir emotion in a speech or piece of writing.',
  [('What is anaphora?', ['The deliberate repetition of a word or phrase at the beginning of successive clauses or sentences', 'A comparison between two unlike things using like or as', 'A brief indirect reference to another text or event', 'A statement that contradicts itself for effect'], 0),
   ('What effect does anaphora often create?', ['Rhythm and emphasis that reinforce an idea', 'Complete confusion with no discernible pattern', 'A total absence of any emotional impact', 'A random and unstructured list of unrelated words'], 0),
   ('In which type of writing or speech is anaphora commonly used?', ['Persuasive speeches', 'A grocery list with no rhetorical purpose', 'A table of contents', 'A set of assembly instructions'], 0),
   ('Which example demonstrates anaphora?', ['We will fight on the beaches, we will fight on the landing grounds, we will fight in the fields.', 'The beaches, landing grounds, and fields were all quiet that day.', 'A single fight took place on the beach.', 'The fields were empty and silent.'], 0),
   ('Why might a speaker use anaphora when delivering a speech?', ['To build momentum and stir emotion through deliberate repetition', 'To ensure the speech contains no repeated words at all', 'To make the speech as short as possible with no elaboration', 'To avoid connecting with the audience emotionally'], 0)]),
M('Algebra: Simplifying Complex Rational Expressions',
  'Grade 10 Math strand: a complex rational expression contains a fraction within its numerator, denominator, or both, and simplifying it typically involves finding a common denominator for the smaller fractions and then rewriting the entire expression as a single simplified fraction.',
  [('What defines a complex rational expression?', ['It contains a fraction within its numerator, denominator, or both', 'It contains no fractions of any kind', 'It is always equal to zero', 'It cannot contain any variables'], 0),
   ('What is a common first step when simplifying a complex rational expression?', ['Finding a common denominator for the smaller fractions within it', 'Immediately setting the entire expression equal to zero', 'Removing all variables from the expression', 'Multiplying the expression by an unrelated constant'], 0),
   ('What is the goal of simplifying a complex rational expression?', ['To rewrite it as a single simplified fraction', 'To convert it into a whole number with no fraction at all', 'To remove all numerical values from the expression', 'To make the expression undefined for every value'], 0),
   ('Why must any values that make a denominator equal to zero be excluded from the domain?', ['Division by zero is undefined', 'Those values always make the expression equal to one', 'Zero denominators are required for a valid expression', 'Excluding values has no mathematical purpose'], 0),
   ('Which skill from earlier algebra is essential when simplifying complex rational expressions?', ['Finding a common denominator and combining fractions', 'Graphing a single point with no equation', 'Measuring an angle with a protractor', 'Converting a fraction into a percentage only'], 0)]),
Sc('Biology: Bioaccumulation and Biomagnification in Food Chains',
   'Grade 10 Science strand: bioaccumulation is the gradual buildup of a substance such as a pesticide or heavy metal within an individual organism over time, and biomagnification is the increasing concentration of that substance at each successive level of a food chain as predators consume many contaminated prey.',
   [('What is bioaccumulation?', ['The gradual buildup of a substance within an individual organism over time', 'The instant disappearance of a substance from an ecosystem', 'A process that only occurs in nonliving matter', 'A sudden decrease in an organisms body mass'], 0),
    ('What is biomagnification?', ['The increasing concentration of a substance at each successive level of a food chain', 'A decrease in the concentration of a substance as it moves up a food chain', 'A process that only affects the very bottom of a food chain', 'A process unrelated to food chains of any kind'], 0),
    ('Why does biomagnification cause top predators to carry especially high concentrations of a contaminant?', ['They consume many contaminated prey, each carrying accumulated amounts of the substance', 'Top predators are immune to all forms of contamination', 'Top predators never consume any prey containing contaminants', 'Contaminants disappear entirely before reaching a top predator'], 0),
    ('Which of the following could undergo bioaccumulation in an organism?', ['A persistent pesticide absorbed from the environment', 'A sound wave passing through the air', 'A beam of visible light', 'A change in air pressure'], 0),
    ('Why are bioaccumulation and biomagnification important concerns for environmental science?', ['They show how pollutants can become increasingly dangerous as they move up a food chain', 'They prove that pollutants always disappear naturally with no risk', 'They have no connection to the health of any ecosystem', 'They only apply to organisms that never consume any food'], 0)]),
H('The 1956 Pipeline Debate in the Canadian Parliament',
  'Grade 10 History strand: the 1956 Pipeline Debate was a heated and prolonged dispute in the Canadian House of Commons over the Liberal governments plan to fund a natural gas pipeline, during which the government used closure to limit debate, contributing to public backlash and the Liberals defeat in the 1957 election.',
  [('What was the central issue of the 1956 Pipeline Debate?', ['Funding a natural gas pipeline project', 'The location of a new national capital', 'A dispute over fishing rights in the Atlantic', 'The design of a new Canadian flag'], 0),
   ('In which body of Parliament did the Pipeline Debate take place?', ['The House of Commons', 'The Senate exclusively', 'A provincial legislature', 'A municipal city council'], 0),
   ('What procedural tool did the government use to limit debate on the pipeline issue?', ['Closure', 'A royal proclamation', 'A national referendum', 'An emergency wartime measure'], 0),
   ('What was one political consequence of the controversy surrounding the Pipeline Debate?', ['Public backlash that contributed to the governments defeat in the following election', 'An immediate increase in public support for the governing party', 'The permanent cancellation of all future elections', 'A formal alliance between all opposition parties'], 0),
   ('In what year did the governing party lose the election following the Pipeline Debate?', ['1957', '1949', '1963', '1968'], 0)]),
]),
day(169, [
E('Writing: The Personal Essay and the Anecdote',
  'Grade 10 English strand: a personal essay explores a writers own experience or perspective on a topic, often built around a central anecdote, a brief and vivid story drawn from real life that grounds a larger reflection or insight in specific, concrete detail.',
  [('What does a personal essay typically explore?', ['A writers own experience or perspective on a topic', 'A purely fictional world with no connection to the writer', 'A set of unrelated statistics with no narrative', 'A formal legal argument with no personal voice'], 0),
   ('What is an anecdote?', ['A brief and vivid story drawn from real life', 'A lengthy legal contract', 'A table of unrelated numerical data', 'A list of bibliographic citations'], 0),
   ('What role does an anecdote often play within a personal essay?', ['It grounds a larger reflection or insight in specific, concrete detail', 'It removes all detail from the essay entirely', 'It replaces the need for any reflection or insight', 'It has no connection to the essays larger meaning'], 0),
   ('Why might a personal essay begin with an anecdote?', ['To draw the reader in with a concrete, relatable moment before moving to reflection', 'To confuse the reader before providing any context', 'To avoid ever connecting with the reader', 'To ensure the essay contains no specific details'], 0),
   ('What distinguishes a personal essay from a purely factual report?', ['A personal essay incorporates the writers own voice, experience, and reflection', 'A personal essay never includes any true information', 'A factual report always includes the authors personal opinion', 'There is no meaningful difference between the two forms'], 0)]),
M('Calculus: Newtons Method for Approximating Roots',
  'Grade 10 Math strand: Newtons Method is an iterative technique for approximating the roots of a function by repeatedly using the tangent line at a current estimate to produce a closer estimate, converging toward a solution when the initial guess is reasonably close to the actual root.',
  [('What does Newtons Method approximate?', ['The roots of a function', 'The exact area under a curve', 'The volume of a three-dimensional solid', 'The angle between two intersecting lines'], 0),
   ('What geometric feature does Newtons Method use at each step?', ['The tangent line at the current estimate', 'A circle drawn around the current estimate', 'A horizontal line through the origin', 'A vertical line through the y-intercept'], 0),
   ('What term describes the process of repeating a calculation to get closer to an answer?', ['Iteration', 'Differentiation', 'Integration', 'Factorization'], 0),
   ('What condition generally helps Newtons Method converge successfully?', ['Starting with an initial guess reasonably close to the actual root', 'Starting with a guess that is infinitely far from the root', 'Avoiding the use of any derivative at all', 'Using a function with no roots whatsoever'], 0),
   ('What earlier calculus concept is required to apply Newtons Method?', ['The derivative of the function', 'The exact integral of an unrelated function', 'A completed table of logarithms', 'A protractor for measuring angles'], 0)]),
Sc('Chemistry: Household Chemistry -- Cleaning Products and Chemical Safety',
   'Grade 10 Science strand: household cleaning products rely on chemical properties such as acidity, alkalinity, and surfactant action to remove dirt and grease, and understanding these properties helps explain why certain products should never be mixed, since some combinations can produce hazardous gases.',
   [('What chemical property helps many cleaning products remove grease and dirt?', ['Surfactant action', 'Radioactivity', 'Magnetism', 'Electrical conductivity'], 0),
    ('Which of the following describes an alkaline household cleaning product?', ['A product with a high pH used to cut through grease', 'A product with a pH of exactly seven and no cleaning ability', 'A product made entirely of pure water with no additives', 'A product that only functions at freezing temperatures'], 0),
    ('Why should certain household cleaning products never be mixed together?', ['Some combinations can produce hazardous gases', 'Mixing cleaning products always improves their effectiveness with no risk', 'Household cleaning products contain no chemical properties at all', 'Mixing products always results in a completely inert substance'], 0),
    ('Which common combination of household chemicals is known to be dangerous if mixed?', ['Bleach and ammonia', 'Water and salt', 'Vinegar and sugar', 'Baking soda and flour'], 0),
    ('Why is understanding basic chemistry useful for using household cleaning products safely?', ['It helps people recognize which products are unsafe to combine and how to use them properly', 'It has no practical application to everyday life', 'It guarantees that all cleaning products are completely safe under any condition', 'It removes the need to ever read a product label'], 0)]),
H('The Founding of the Canada Council for the Arts, 1957',
  'Grade 10 History strand: the Canada Council for the Arts was established in 1957 to provide federal funding and support for artists, writers, and cultural organizations, implementing a key recommendation of the earlier Massey Commission and marking a major expansion of government support for Canadian culture.',
  [('In what year was the Canada Council for the Arts established?', ['1957', '1939', '1949', '1967'], 0),
   ('What was the Canada Council for the Arts created to provide?', ['Federal funding and support for artists, writers, and cultural organizations', 'Federal funding exclusively for military research', 'A new national police force', 'A federal agency regulating agriculture'], 0),
   ('Which earlier commission had recommended the creation of a body like the Canada Council?', ['The Massey Commission', 'The Rowell-Sirois Commission', 'The Durham Report', 'The Manitoba Schools Question inquiry'], 0),
   ('What broader shift did the founding of the Canada Council represent?', ['A major expansion of government support for Canadian culture', 'A complete elimination of federal involvement in culture', 'A shift of all cultural funding to private corporations only', 'A ban on federal funding for the arts'], 0),
   ('Why might a national government choose to fund artists and cultural organizations directly?', ['To support the development and preservation of a distinct national culture', 'To eliminate all forms of artistic expression', 'Because artists never require any form of financial support', 'To transfer control of all culture to foreign governments'], 0)]),
]),
day(170, [
E('English Review: Grammar, Reading, Writing, and Media Literacy (Days 161-169)',
  'Grade 10 English strand review: students revisit livestreaming and influencer culture, nominal clauses, understatement and litotes, the retrospective review, the quest narrative, comment sections and online discourse, semicolons and colons, anaphora, and the personal essay.',
  [('What does influencer culture typically involve?', ['A content creator building a personal brand and audience across social platforms', 'A government agency regulating all social media content', 'A library cataloguing printed books by subject', 'A factory manufacturing television sets'], 0),
   ('What role does a nominal clause play in a sentence?', ['The same role a single noun would play, such as subject or object', 'The same role a preposition would play', 'The same role a comma would play', 'No grammatical role of any kind'], 0),
   ('What is litotes?', ['A form of understatement that uses a negative construction to affirm a positive', 'A form of exaggeration used to inflate an idea', 'A device that gives human traits to an animal', 'A word that imitates the sound it describes'], 0),
   ('What does a retrospective review typically do?', ['Looks back on a work some time after its original release to evaluate it anew', 'Reviews a work before it has ever been released to the public', 'Summarizes a work without offering any evaluation', 'Focuses only on the price of the original release'], 0),
   ('What is anaphora?', ['The deliberate repetition of a word or phrase at the beginning of successive clauses or sentences', 'A comparison between two unlike things using like or as', 'A brief indirect reference to another text or event', 'A statement that contradicts itself for effect'], 0)]),
M('Math Review: Calculus, Number Theory, Statistics, and Geometry (Days 161-169)',
  'Grade 10 Math strand review: students revisit curve sketching with derivative tests, the twin prime conjecture, Type I and Type II errors, tessellations, the scalar triple product, spanning trees, the hypergeometric distribution, simplifying complex rational expressions, and Newtons Method.',
  [('What does the first derivative test help locate on a graph?', ['Increasing and decreasing intervals and turning points', 'The exact colour used to draw the graph', 'The total number of variables in the function', 'The name of the mathematician who defined the function'], 0),
   ('What does the twin prime conjecture propose?', ['That there are infinitely many pairs of primes differing by exactly two', 'That every prime number is even', 'That no two prime numbers can ever differ by two', 'That prime numbers stop existing after a certain value'], 0),
   ('What is a Type I error?', ['Incorrectly rejecting a null hypothesis that is actually true', 'Correctly rejecting a null hypothesis that is actually false', 'Incorrectly accepting a null hypothesis that is actually false', 'Correctly accepting a null hypothesis that is actually true'], 0),
   ('What does the scalar triple product of three vectors produce?', ['A single number equal to the volume of the parallelepiped formed by the vectors', 'A new vector perpendicular to all three original vectors', 'A matrix with no numerical value', 'A single point with no coordinates'], 0),
   ('What does Newtons Method approximate?', ['The roots of a function', 'The exact area under a curve', 'The volume of a three-dimensional solid', 'The angle between two intersecting lines'], 0)]),
Sc('Science Review: Chemistry, Physics, Earth Science, and Biology (Days 161-169)',
   'Grade 10 Science strand review: students revisit flame tests and fireworks chemistry, black holes, permafrost, hibernation and torpor, sunscreen and ultraviolet protection, the physics of musical instruments, hurricanes, bioaccumulation and biomagnification, and household cleaning chemistry.',
   [('What does a flame test identify?', ['Certain metal ions, based on the colour their compounds produce when heated', 'The exact temperature of a flame in degrees', 'The density of a solid object', 'The pH of a neutral solution'], 0),
    ('How does a black hole typically form?', ['A massive star collapses under its own gravity after exhausting its nuclear fuel', 'A star suddenly gains a large amount of new mass from nowhere', 'A planet cools down completely and stops orbiting', 'Two asteroids collide at low speed'], 0),
    ('What is permafrost?', ['Ground that remains frozen for at least two consecutive years', 'Ice that forms only on the surface of the ocean', 'A type of rock found only near volcanoes', 'Snow that falls once and never melts anywhere'], 0),
    ('What is biomagnification?', ['The increasing concentration of a substance at each successive level of a food chain', 'A decrease in the concentration of a substance as it moves up a food chain', 'A process that only affects the very bottom of a food chain', 'A process unrelated to food chains of any kind'], 0),
    ('Over what type of environment do hurricanes typically form?', ['Warm ocean water', 'Frozen tundra', 'A dry desert with no moisture', 'A mountain range far from any ocean'], 0)]),
H('History Review: Postwar Canada and the Early Cold War (Days 161-169)',
  'Grade 10 History strand review: students revisit the baby boom, the Veterans Charter, the Canadian Citizenship Act of 1947, the Gouzenko Affair, the founding of NATO, Louis St. Laurent, the Old Age Security Act of 1951, the 1956 Pipeline Debate, and the founding of the Canada Council for the Arts.',
  [('What was the baby boom?', ['A sharp rise in birth rates across Canada following the Second World War', 'A sudden decline in the Canadian population after 1945', 'A federal law limiting family size', 'A period when no children were born in Canada'], 0),
   ('What did the Canadian Citizenship Act of 1947 create for the first time?', ['A distinct legal status of Canadian citizen, separate from British subject status', 'A new Canadian currency', 'A new Canadian flag', 'A new provincial border'], 0),
   ('What did Gouzenko reveal when he defected?', ['Documents exposing a Soviet spy network operating in Canada', 'A plan to invade Canada by sea', 'A treaty ending the Second World War', 'A new design for a Canadian warship'], 0),
   ('What did the Old Age Security Act of 1951 establish?', ['A universal federal pension paid to Canadians aged seventy and older', 'A new national holiday for seniors', 'A ban on retirement before the age of seventy', 'A provincial tax exclusive to Quebec'], 0),
   ('What was the central issue of the 1956 Pipeline Debate?', ['Funding a natural gas pipeline project', 'The location of a new national capital', 'A dispute over fishing rights in the Atlantic', 'The design of a new Canadian flag'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_161_170)
    append_to(10, g10_161_170)
