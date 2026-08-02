#!/usr/bin/env python3
"""Grade 9, Days 131-140 -- extends Grade 9 from 130 to 140 days. Topics
chosen after dumping and reading the full Day 1-130 title list (data/grade9.json)
to avoid any overlap, which by this point is exhaustive across all four
subjects: hyphens and compound modifiers, semantic change, stream of
consciousness narration, writing a research proposal, algorithmic
recommendation systems, who vs whom, the character sketch, false cognates,
and the doppelganger motif; solving radical equations, the Euclidean
algorithm and greatest common divisor, vector projections, Bayes Theorem,
z-scores, inflation and the time value of money, sigma notation, continuity
of functions, and polar coordinates; chemical equilibrium and Le Chateliers
Principle, torque and rotational equilibrium, stem cells and cellular
differentiation, ice cores and paleoclimatology, comets/asteroids/near-Earth
objects, the lymphatic system, colligative properties of solutions,
projectile motion, and karst topography; the geography of Antarctica and
the Antarctic Treaty System, global biodiversity hotspots, enclaves and
special administrative regions, planned capital cities, global air travel
networks, the diamond and gemstone trade, land reclamation, permafrost and
thawing tundra, and global financial centres.

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 9 batches); SocialStudies
content is Geography-focused, matching the existing convention.

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided entirely (e.g.
"Chateliers" not "Chatelier's", "countrys" not "country's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-english'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science'
SS9 = 'https://tvolearn.com/pages/grade-9-geography'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 English',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science',
    'TVO Learn: Grade 9 Geography',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


def _rebalance_answer_positions(days, seed=20260801):
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


g9_131_140 = [
day(131, [
L('Grammar: Hyphens and Compound Modifiers',
  'Grade 9 Language strand: a hyphen can join two or more words into a single compound modifier that describes a noun, such as well known becoming well-known, and correct hyphenation helps a reader group the right words together and avoid ambiguity.',
  [('What is a compound modifier?', ['Two or more words joined together to describe a noun as a single unit', 'A single unmodified noun with no description', 'A punctuation mark used only in dialogue', 'A sentence with no verb at all'], 0),
   ('Why are compound modifiers often hyphenated when placed before a noun?', ['The hyphen shows the words function together as one descriptive unit', 'Hyphens have no grammatical purpose whatsoever', 'Hyphens always change the meaning of a word entirely', 'Hyphenation is required only in formal poetry'], 0),
   ('Which sentence correctly hyphenates a compound modifier before a noun?', ['The five-year plan outlined every stage of the project.', 'The five year plan outlined every, stage of the project.', 'The five-year-plan-outlined every stage of the project.', 'The five year-plan outlined-every stage of the project.'], 0),
   ('Compound modifiers formed with an adverb ending in -ly, such as highly regarded, are usually treated how?', ['Left unhyphenated, since -ly already signals the words work together', 'Always hyphenated with no exceptions at all', 'Never allowed to appear before a noun', 'Separated by a comma instead of a hyphen'], 0),
   ('Why might leaving out a needed hyphen create ambiguity in a sentence?', ['A reader may misread which words are meant to be grouped together as one description', 'Ambiguity can never result from missing punctuation', 'Hyphens have no effect on how a sentence is read', 'Removing a hyphen always makes a sentence clearer'], 0)]),
M('Algebra: Solving Radical Equations',
  'Grade 9 Math strand: a radical equation contains a variable inside a radical, and solving one typically involves isolating the radical, then raising both sides of the equation to a matching power to remove it, followed by checking for extraneous solutions.',
  [('What defines a radical equation?', ['An equation in which a variable appears inside a radical, such as a square root', 'An equation with no variables of any kind', 'An equation that only involves whole number coefficients', 'An equation that cannot be graphed'], 0),
   ('What is a common first step in solving a radical equation?', ['Isolating the radical on one side of the equation', 'Immediately squaring every term with no isolation first', 'Deleting the radical without performing any operation', 'Multiplying both sides by zero'], 0),
   ('After isolating a square root, what operation removes it from the equation?', ['Squaring both sides of the equation', 'Taking the square root of both sides again', 'Adding one to both sides', 'Dividing both sides by the variable'], 0),
   ('Why must solutions to a radical equation always be checked in the original equation?', ['Squaring both sides can introduce extraneous solutions that do not actually satisfy the original equation', 'Checking solutions is never necessary once an equation is solved', 'Radical equations always have exactly one guaranteed solution', 'Squaring both sides never changes the set of valid solutions'], 0),
   ('If solving x = sqrt(x+2) produces a candidate solution of x=-1, why would this be rejected?', ['Substituting -1 back into the original equation does not produce a true statement', 'Negative numbers can never appear anywhere in a radical equation', 'The equation has no valid solutions under any circumstances', 'The candidate solution must always be accepted without checking'], 0)]),
Sc('Chemistry: Chemical Equilibrium and Le Chateliers Principle',
   'Grade 9 Science strand: chemical equilibrium occurs when the forward and reverse rates of a reversible reaction become equal, and Le Chateliers Principle predicts how a system at equilibrium shifts in response to a change in concentration, temperature, or pressure.',
   [('What defines chemical equilibrium in a reversible reaction?', ['A state where the forward and reverse reaction rates become equal', 'A state where all reactants are completely used up', 'A state where no reaction has ever occurred', 'A state where only the forward reaction takes place'], 0),
    ('What does Le Chateliers Principle predict?', ['How a system at equilibrium shifts in response to a change in conditions', 'The exact colour of every chemical reaction', 'That equilibrium can never be disturbed by any change', 'The total mass of the reactants only'], 0),
    ('According to Le Chateliers Principle, what happens if the concentration of a reactant is increased?', ['The equilibrium shifts to produce more product, using up some of the added reactant', 'The reaction stops permanently with no further change', 'The equilibrium always shifts to produce less product', 'Concentration changes have no effect on equilibrium at all'], 0),
    ('Which factor, besides concentration, can shift a chemical equilibrium according to Le Chateliers Principle?', ['A change in temperature or pressure', 'The colour of the reaction container', 'The time of day the reaction occurs', 'The name given to the chemical compound'], 0),
    ('Why is understanding chemical equilibrium important in industrial chemistry?', ['It helps chemists adjust conditions to maximize the yield of a desired product', 'Equilibrium has no relevance to industrial processes', 'Industrial chemistry never involves reversible reactions', 'Equilibrium always guarantees the lowest possible yield'], 0)]),
SS('Social Studies: The Geography of Antarctica and the Antarctic Treaty System',
   'Grade 9 Social Studies (Geography) strand: Antarctica is governed under the Antarctic Treaty System, an international agreement that sets the continent aside for peaceful scientific research and limits military activity and resource extraction, making it a unique case in global geography.',
   [('What is the Antarctic Treaty System?', ['An international agreement governing Antarctica for peaceful, scientific purposes', 'A single countrys law that governs all of Antarctica', 'A trade agreement unrelated to any scientific activity', 'An agreement that has never been signed by any nation'], 0),
    ('What does the Antarctic Treaty generally restrict on the continent?', ['Military activity and resource extraction', 'All forms of scientific research', 'International cooperation of any kind', 'Weather monitoring and climate study'], 0),
    ('Why is Antarctica often described as a unique case in global political geography?', ['No single country holds full sovereignty over the entire continent', 'It is owned entirely by one government with no international involvement', 'It has no connection to international law or agreements', 'It is the only continent with a permanent large population'], 0),
    ('What type of activity does the Antarctic Treaty System actively encourage on the continent?', ['International scientific research and cooperation', 'Large-scale mining and drilling operations', 'Permanent military bases for multiple nations', 'Unrestricted commercial fishing with no oversight'], 0),
    ('Why might Antarcticas governance model be considered unusual compared to most territories on Earth?', ['It is managed collectively by multiple nations under a shared treaty rather than by a single government', 'It is governed identically to every other continent on Earth', 'It has no rules or agreements governing activity there at all', 'It was permanently colonized by a single nation long ago'], 0)]),
]),
day(132, [
L('Vocabulary: Semantic Change and Words That Shifted Meaning Over Time',
  'Grade 9 Language strand: semantic change describes how a words meaning can shift, narrow, widen, or reverse over generations, so that a term once used one way, such as nice originally meaning foolish, can come to mean something quite different today.',
  [('What is semantic change?', ['The process by which a words meaning shifts over time', 'A rule that prevents any word from ever changing meaning', 'A punctuation mark used to separate clauses', 'A type of formal citation format'], 0),
   ('What does it mean if a words meaning narrows over time?', ['The word comes to refer to a smaller, more specific set of things than it once did', 'The word comes to mean absolutely everything with no limits', 'The word disappears from the language completely', 'The word becomes a proper noun with a capital letter'], 0),
   ('Which is an example of semantic change?', ['A word that once meant foolish coming to mean pleasant or agreeable', 'A word that has remained completely unchanged since its creation', 'A word invented yesterday with no prior history', 'A word used exclusively in advanced mathematics'], 0),
   ('Why is it useful for readers to understand semantic change?', ['It helps explain why older texts sometimes use familiar words in unfamiliar ways', 'It has no bearing on understanding texts from earlier time periods', 'Semantic change only applies to numbers, never words', 'Understanding word history never helps with reading comprehension'], 0),
   ('Semantic change is closely related to which other area of language study?', ['Etymology, the study of word origins', 'Punctuation rules exclusively', 'Sentence diagramming exclusively', 'Verb conjugation exclusively'], 0)]),
M('Number Theory: The Euclidean Algorithm and Greatest Common Divisor',
  'Grade 9 Math strand: the Euclidean algorithm finds the greatest common divisor of two integers by repeatedly dividing and taking remainders until a remainder of zero is reached, offering a faster method than listing every factor.',
  [('What does the Euclidean algorithm calculate?', ['The greatest common divisor of two integers', 'The least common multiple of every integer', 'The exact prime factorization of a single number', 'The sum of two unrelated fractions'], 0),
   ('How does the Euclidean algorithm proceed?', ['By repeatedly dividing and taking remainders until a remainder of zero is reached', 'By listing every possible factor of both numbers first', 'By guessing an answer with no calculation involved', 'By multiplying the two numbers together repeatedly'], 0),
   ('What is the greatest common divisor of two numbers when the Euclidean algorithm stops?', ['The last nonzero remainder produced during the process', 'Always the larger of the two original numbers', 'Always the number one, regardless of the inputs', 'The sum of both original numbers'], 0),
   ('Why might the Euclidean algorithm be preferred over listing all factors of large numbers?', ['It finds the greatest common divisor more quickly, especially for large integers', 'It always produces an incorrect answer for large numbers', 'Listing factors is always faster for every possible number', 'The Euclidean algorithm cannot be used on large numbers at all'], 0),
   ('What is the greatest common divisor of 24 and 36, found using the Euclidean algorithm?', ['12', '6', '18', '4'], 0)]),
Sc('Physics: Torque and Rotational Equilibrium',
   'Grade 9 Science strand: torque measures the turning effect of a force applied at a distance from a pivot point, and an object is in rotational equilibrium when the total torque acting on it is balanced, resulting in no change to its rotational motion.',
   [('What does torque measure?', ['The turning effect of a force applied at a distance from a pivot point', 'The total mass of an object with no reference to force', 'The temperature of a rotating object', 'The colour of an object in motion'], 0),
    ('What two factors determine the amount of torque produced by a force?', ['The size of the force and its distance from the pivot point', 'Only the colour of the object experiencing the force', 'Only the temperature of the surrounding environment', 'Only the time of day the force is applied'], 0),
    ('What does it mean for an object to be in rotational equilibrium?', ['The total torque acting on it is balanced, so its rotational motion does not change', 'The object is spinning faster and faster with no limit', 'No forces of any kind are acting on the object', 'The object has stopped existing entirely'], 0),
    ('Applying a force farther from a pivot point generally has what effect on torque?', ['It increases the torque produced by that force', 'It always eliminates torque completely', 'It has no effect on torque whatsoever', 'It always decreases torque to zero'], 0),
    ('A seesaw balanced perfectly level with two riders is an example of what physics concept?', ['Rotational equilibrium', 'Terminal velocity', 'Simple harmonic motion', 'Radioactive decay'], 0)]),
SS('Social Studies: The Geography of Global Biodiversity Hotspots',
   'Grade 9 Social Studies (Geography) strand: a biodiversity hotspot is a region with an exceptionally high number of unique species that is also facing significant habitat loss, making these areas a priority for global conservation efforts.',
   [('What defines a biodiversity hotspot?', ['A region with an exceptionally high number of unique species that is also facing significant habitat loss', 'Any region with no living species present at all', 'A region where habitat loss has never occurred', 'A region with only one single species living in it'], 0),
    ('Why do biodiversity hotspots receive special attention from conservation organizations?', ['They contain a large share of the worlds unique species that are at high risk of disappearing', 'These regions have no unique species of any kind', 'Conservation organizations avoid these regions entirely', 'These regions face no environmental threats whatsoever'], 0),
    ('What threat commonly endangers species within a biodiversity hotspot?', ['Habitat loss from human development or land use change', 'An overabundance of protected land with no development', 'A complete absence of any human activity nearby', 'Species in hotspots are never at risk of any kind'], 0),
    ('Why might a region with fewer total species still be considered less of a conservation priority than a hotspot?', ['It may lack the combination of high uniqueness and high risk that defines a true hotspot', 'Every region on Earth is considered an equal conservation priority', 'Species count has no bearing on conservation priorities', 'Hotspots are chosen entirely at random with no criteria'], 0),
    ('Studying the geography of biodiversity hotspots helps researchers make decisions about what?', ['Where to focus limited conservation resources most effectively', 'How to eliminate biodiversity from a region entirely', 'Where to build the largest possible cities', 'How to ignore environmental risk factors completely'], 0)]),
]),
day(133, [
L('Reading: Analyzing Stream of Consciousness Narration',
  'Grade 9 Language strand: stream of consciousness is a narrative technique that presents a characters continuous flow of thoughts, feelings, and impressions in real time, often with looser sentence structure, to immerse the reader directly in the characters mind.',
  [('What does stream of consciousness narration attempt to capture?', ['A characters continuous flow of thoughts and impressions as they occur', 'Only a characters physical actions with no inner thought at all', 'A strict, chronological summary of an entire plot', 'A list of unrelated facts with no connection to any character'], 0),
   ('What stylistic feature often characterizes stream of consciousness writing?', ['Looser, less structured sentences that mimic the movement of thought', 'Strict, formally outlined paragraphs with no variation', 'Only dialogue, with no narration of any kind', 'Numbered lists replacing all prose'], 0),
   ('Why might an author choose stream of consciousness over a more traditional narrative style?', ['To immerse readers directly in a characters inner experience', 'To make the story as impersonal and distant as possible', 'To remove any sense of character from the narrative', 'To avoid ever describing a characters thoughts'], 0),
   ('Stream of consciousness narration is most closely associated with representing which aspect of a character?', ['Their internal, psychological experience', 'Their physical appearance only', 'Their family history exclusively', 'Their financial situation only'], 0),
   ('Why can stream of consciousness passages sometimes feel challenging to read?', ['The thoughts may jump between ideas without the usual transitions of conventional narration', 'These passages are always written with extremely simple vocabulary', 'They never include any emotional content whatsoever', 'They are always the shortest passages in a text'], 0)]),
M('Geometry: Vector Projections and Scalar Components',
  'Grade 9 Math strand: the projection of one vector onto another describes how much of the first vector points in the direction of the second, and it can be calculated using the dot product together with the magnitude of the vector being projected onto.',
  [('What does the projection of one vector onto another describe?', ['How much of the first vector points in the direction of the second', 'The total length of both vectors added together', 'The colour associated with each vector', 'The number of dimensions a vector exists in'], 0),
   ('What mathematical tool is used to calculate a vector projection?', ['The dot product, together with the magnitude of the vector being projected onto', 'Only the sum of the two vectors', 'Only the difference of the two vectors magnitudes', 'A random number generator'], 0),
   ('If two vectors are perpendicular, what is the projection of one onto the other?', ['Zero, since perpendicular vectors have no component in each others direction', 'Equal to the length of the longer vector', 'Always a negative number', 'Undefined and impossible to calculate'], 0),
   ('The scalar component of a projection represents what kind of quantity?', ['A magnitude with a sign, indicating size and direction along the target vector', 'A colour value with no numerical meaning', 'A count of how many vectors exist in a diagram', 'A fixed constant that never changes between problems'], 0),
   ('Vector projections are useful in physics for calculating what kind of quantity?', ['The component of a force acting in a specific direction', 'The temperature of an object in motion', 'The exact colour of a moving object', 'The name of the object being measured'], 0)]),
Sc('Biology: Stem Cells and Cellular Differentiation',
   'Grade 9 Science strand: stem cells are unspecialized cells capable of developing into many different cell types through a process called differentiation, giving them significant potential in medical research and regenerative therapies.',
   [('What is a defining feature of a stem cell?', ['It is an unspecialized cell capable of developing into many different cell types', 'It is a fully specialized cell that can never change', 'It is a cell found only in plants, never animals', 'It is a cell that cannot divide under any circumstances'], 0),
    ('What is the process called by which a stem cell becomes a specialized cell type?', ['Differentiation', 'Photosynthesis', 'Combustion', 'Sedimentation'], 0),
    ('Why do stem cells hold significant potential in medical research?', ['They may be used to replace or repair damaged tissue in regenerative therapies', 'They have no practical application in medicine whatsoever', 'They can only be studied but never used for any treatment', 'They are identical in every way to fully differentiated cells'], 0),
    ('Once a cell has fully differentiated into a specific type, such as a muscle cell, what has generally happened to its ability to become other cell types?', ['It has largely lost the flexibility of an unspecialized stem cell', 'It has gained the ability to become any cell type at will', 'Nothing changes at all in the cells capabilities', 'It becomes more flexible than it was as a stem cell'], 0),
    ('Stem cell research connects most directly to which broader biological concept discussed earlier in the course?', ['Gene expression and how cells use their genetic information differently', 'The rock cycle and rock formation', 'Ocean currents and climate patterns', 'Map projections and cartography'], 0)]),
SS('Social Studies: The Geography of Enclaves, Exclaves, and Special Administrative Regions',
   'Grade 9 Social Studies (Geography) strand: an enclave is a territory entirely surrounded by another countrys land, an exclave is a piece of a country separated from its main territory, and special administrative regions operate under distinct laws within a larger nation, creating unusual political geography.',
   [('What is an enclave?', ['A territory entirely surrounded by the land of another country', 'A territory located in the middle of an ocean with no land nearby', 'A region with no borders of any kind', 'A term with no connection to political geography'], 0),
    ('What is an exclave?', ['A piece of a countrys territory that is separated from its main territory', 'A territory that has never been claimed by any nation', 'A region located at the exact centre of a countrys mainland', 'A synonym for an ocean current'], 0),
    ('What defines a special administrative region?', ['An area that operates under distinct laws or a different level of autonomy within a larger nation', 'A region with absolutely no laws or government of any kind', 'A territory that is identical in every way to the rest of its country', 'A term used only to describe uninhabited land'], 0),
    ('Why might enclaves and exclaves create unique geographic or political challenges?', ['Access, governance, and border crossing can be more complicated than for connected territory', 'These territories never experience any political or logistical challenges', 'Enclaves and exclaves are always larger than the countries that surround them', 'They have no connection to international law of any kind'], 0),
    ('Why do geographers study unusual political territories such as enclaves and special administrative regions?', ['To understand how historical events and agreements can shape unusual borders and governance', 'These territories are considered irrelevant to the study of geography', 'All borders around the world are shaped in an identical, simple way', 'Political geography never examines unusual or complex borders'], 0)]),
]),
day(134, [
L('Writing: Writing a Research Proposal',
  'Grade 9 Language strand: a research proposal outlines a planned investigation before the work begins, stating a clear research question, explaining its significance, and describing the methods a writer intends to use to find an answer.',
  [('What is the purpose of a research proposal?', ['To outline a planned investigation before the research work begins', 'To summarize research that was completed many years earlier', 'To replace the need for any research question', 'To criticize research conducted by other people'], 0),
   ('What should a strong research proposal clearly state?', ['A specific, focused research question', 'An unrelated list of personal hobbies', 'The final answer before any research occurs', 'A summary of an entirely unrelated topic'], 0),
   ('Why do research proposals typically explain the significance of a topic?', ['To show readers why the investigation is worth pursuing', 'Significance is never a relevant consideration in research', 'To make the proposal as confusing as possible', 'To avoid stating any purpose for the research'], 0),
   ('What part of a research proposal describes how the investigation will be carried out?', ['The methods section', 'The title page alone', 'The dedication page', 'The index at the very end'], 0),
   ('Why might a student write a research proposal before starting a larger project?', ['To plan the scope and direction of the project and get feedback early', 'Research proposals serve no planning purpose whatsoever', 'To guarantee an identical result to every other students project', 'Proposals are only ever written after a project is finished'], 0)]),
M('Data Management: Bayes Theorem and Updating Probabilities',
  'Grade 9 Math strand: Bayes Theorem provides a method for updating the probability of an event as new evidence becomes available, building directly on the idea of conditional probability introduced earlier in the course.',
  [('What does Bayes Theorem allow you to do?', ['Update the probability of an event based on new evidence', 'Calculate the area of any triangle', 'Determine the exact value of an unrelated variable', 'Eliminate the need for probability altogether'], 0),
   ('Bayes Theorem builds most directly on which earlier probability concept?', ['Conditional probability', 'The Pythagorean Theorem', 'Synthetic division', 'The dot product of vectors'], 0),
   ('In Bayes Theorem, what happens to an initial probability estimate once new evidence is considered?', ['It is revised to produce an updated, more informed probability', 'It is always discarded and replaced with zero', 'It remains completely unchanged regardless of new evidence', 'It is converted into an unrelated geometric shape'], 0),
   ('Why is Bayes Theorem useful in fields such as medical testing?', ['It helps estimate the true likelihood of a condition after accounting for a test result', 'It has no application to medicine or testing of any kind', 'It guarantees a test result is always accurate with no uncertainty', 'It eliminates the need for any medical testing altogether'], 0),
   ('What is required before Bayes Theorem can be applied to a problem?', ['Some known or estimated probabilities relating the event and the evidence', 'A guarantee that the event in question is impossible', 'A completed geometric proof with no probability involved', 'A list of unrelated historical dates'], 0)]),
Sc('Earth Science: Ice Cores and Paleoclimatology',
   'Grade 9 Science strand: paleoclimatology is the study of past climates, and scientists drill ice cores from glaciers and polar ice sheets to analyze trapped air bubbles and chemical layers that reveal temperature and atmospheric conditions from thousands of years ago.',
   [('What does paleoclimatology study?', ['The climates of the past', 'Only the weather forecast for tomorrow', 'The structure of modern cities', 'The chemical composition of ocean plastics'], 0),
    ('What do scientists extract from glaciers and polar ice sheets to study past climate?', ['Ice cores', 'Fossilized leaves only', 'Volcanic ash exclusively', 'Ocean sediment exclusively'], 0),
    ('What can trapped air bubbles inside an ice core reveal about the past?', ['The composition of the atmosphere at the time the ice formed', 'Nothing useful about the atmosphere at any point in history', 'The exact population of a nearby city', 'The colour of the sky on a single specific day'], 0),
    ('Why do ice cores often show a layered structure?', ['Each layer typically corresponds to a different year of snowfall and ice accumulation', 'The layers are added artificially by scientists after drilling', 'Ice cores never show any layered structure at all', 'Layers form only once every thousand years with no yearly pattern'], 0),
    ('Why is paleoclimatology useful for understanding modern climate change?', ['It provides a long-term record that helps scientists compare current changes to natural patterns of the past', 'It has no relevance to studying modern climate change', 'Past climate data cannot be compared to modern data in any way', 'Ice cores only reveal information about future climate, never the past'], 0)]),
SS('Social Studies: The Geography of Planned Capital Cities',
   'Grade 9 Social Studies (Geography) strand: some nations have built entirely new, planned capital cities, often to shift political power to a more central location, ease congestion in an existing large city, or symbolize a fresh start, revealing how geography and politics intersect in urban planning.',
   [('What is a planned capital city?', ['A capital built intentionally from the ground up, rather than growing organically over time', 'A capital city with absolutely no government buildings', 'Any city that has existed for over a thousand years', 'A city that has never had any residents'], 0),
    ('Why might a country choose to build an entirely new capital city?', ['To shift political power to a more central location or relieve congestion in an existing large city', 'Countries never have any reason to build a new capital', 'To eliminate the need for a government entirely', 'To reduce the total population of the country to zero'], 0),
    ('What can a newly built capital city symbolize for a nation?', ['A fresh start or a new direction for the country', 'A permanent rejection of all future development', 'The complete elimination of national identity', 'A citys refusal to have any government functions'], 0),
    ('How does a planned capital city typically differ in design from a city that grew organically over centuries?', ['It is often designed with a deliberate layout from the very beginning', 'It always has a completely random, unplanned street pattern', 'It is built with no consideration of function or design at all', 'It cannot include any government buildings by definition'], 0),
    ('Why do geographers find planned capital cities an interesting case study?', ['They show how political decisions can directly shape the physical geography and layout of a settlement', 'Planned capital cities have no connection to political decisions', 'Geographers consider urban planning irrelevant to their field', 'Every capital city in the world was planned in an identical way'], 0)]),
]),
day(135, [
L('Media Literacy: Analyzing Algorithmic Recommendation Systems',
  'Grade 9 Language strand: algorithmic recommendation systems use data about a users past behaviour to suggest new content, and understanding how these systems work helps a media-literate reader recognize why certain videos, posts, or products keep appearing in their feed.',
  [('What do algorithmic recommendation systems use to suggest content?', ['Data about a users past behaviour and preferences', 'A completely random selection process with no data involved', 'A printed list updated once per year', 'The users physical location only, with no other information'], 0),
   ('Why might a recommendation system keep suggesting similar types of content?', ['It is designed to show users more of what has kept their attention before', 'It intentionally avoids showing users anything related to their interests', 'Recommendation systems change their suggestions with no pattern at all', 'The system has no access to any user data whatsoever'], 0),
   ('What is one potential consequence of relying heavily on algorithmic recommendations?', ['A viewer may see a narrower range of perspectives over time', 'Viewers always see a perfectly balanced range of every possible viewpoint', 'Algorithms have no effect on what content a person is shown', 'Recommendations are always chosen entirely at random'], 0),
   ('Why is it useful for a media-literate person to understand how recommendation systems work?', ['It helps them recognize why their feed looks the way it does and seek out other viewpoints', 'Understanding these systems has no practical benefit at all', 'Recommendation systems cannot be understood by anyone', 'This knowledge only applies to people who design software'], 0),
   ('Which of these is an example of an algorithmic recommendation system at work?', ['A streaming service suggesting shows based on titles a user has previously watched', 'A printed newspaper delivered on a fixed daily schedule', 'A single static poster displayed in a store window', 'A book chosen randomly from a shelf with no data involved'], 0)]),
M('Statistics: Z-Scores and Standardizing Data',
  'Grade 9 Math strand: a z-score expresses how many standard deviations a data point lies above or below the mean of a data set, allowing values from different distributions to be compared on a common scale.',
  [('What does a z-score measure?', ['How many standard deviations a data point lies above or below the mean', 'The total number of data points in a set', 'The exact colour associated with a data point', 'The name of the variable being studied'], 0),
   ('A z-score of zero indicates what about a data point?', ['The data point is exactly equal to the mean', 'The data point is the largest value in the entire data set', 'The data point does not exist in the data set', 'The data point is always negative'], 0),
   ('Why are z-scores useful when comparing values from two different data sets?', ['They place values on a common, standardized scale for fair comparison', 'They make it impossible to ever compare two data sets', 'Z-scores can only be calculated for a single data set at a time with no comparison allowed', 'They eliminate the need to ever calculate a mean'], 0),
   ('What does a negative z-score indicate about a data point?', ['The data point lies below the mean of the data set', 'The data point lies above the mean of the data set', 'The data point is equal to the standard deviation', 'The data set contains no valid values at all'], 0),
   ('Calculating a z-score requires which two values from a data set?', ['The mean and the standard deviation', 'Only the largest and smallest values', 'Only the total number of data points', 'Only the median value'], 0)]),
Sc('Astronomy: Comets, Asteroids, and Near-Earth Objects',
   'Grade 9 Science strand: comets are icy bodies that develop glowing tails as they near the Sun, asteroids are rocky remnants mostly found in the asteroid belt, and near-Earth objects are tracked closely because their orbits occasionally bring them close to our planet.',
   [('What is a comet primarily made of?', ['Ice, dust, and rocky material', 'Pure liquid water with nothing else', 'Solid gold and other precious metals', 'Only gases, with no solid material at all'], 0),
    ('What causes a comets glowing tail to form?', ['Heat from the Sun causes ice on the comet to vaporize and release gas and dust', 'The tail is a permanent, unchanging feature unrelated to the Sun', 'Comets generate their own tail using internal engines', 'The tail forms only when a comet is far from any star'], 0),
    ('Where are most asteroids in our solar system located?', ['In the asteroid belt between Mars and Jupiter', 'Inside the core of the Sun', 'Beyond the orbit of every planet, with no defined region', 'Only within Earths own atmosphere'], 0),
    ('What defines a near-Earth object?', ['A comet or asteroid whose orbit brings it relatively close to Earths orbit', 'Any object located inside Earths own atmosphere permanently', 'A planet located within our solar system', 'A star located outside the Milky Way galaxy'], 0),
    ('Why do astronomers closely track near-Earth objects?', ['To monitor the small possibility that one could someday collide with Earth', 'Near-Earth objects pose no scientific interest of any kind', 'Tracking these objects has no connection to planetary safety', 'These objects are tracked only for entertainment purposes'], 0)]),
SS('Social Studies: The Geography of Global Air Travel and Flight Networks',
   'Grade 9 Social Studies (Geography) strand: global air travel connects distant regions through networks of hub airports and flight routes, shaping patterns of trade, tourism, and migration while raising questions about accessibility and environmental impact.',
   [('What role do hub airports play in global flight networks?', ['They serve as central connecting points linking many different flight routes together', 'They exist only to store aircraft with no passenger flights at all', 'Hub airports have no connection to other airports whatsoever', 'They are located exclusively in rural, unpopulated areas'], 0),
    ('How does global air travel influence patterns of trade and tourism?', ['It allows people and goods to move quickly between distant regions, encouraging trade and travel', 'Air travel has no effect on trade or tourism of any kind', 'Global air travel always reduces the total amount of trade worldwide', 'Air travel only connects cities within a single country'], 0),
    ('What environmental concern is commonly associated with the growth of global air travel?', ['Increased greenhouse gas emissions from aircraft', 'A guaranteed reduction in all forms of pollution', 'Air travel has no measurable environmental impact at all', 'A permanent decrease in global energy consumption'], 0),
    ('Why might some regions have far fewer flight connections than major global hubs?', ['Lower demand, geographic isolation, or limited infrastructure can result in fewer routes', 'Every region on Earth has an identical number of flight connections', 'Flight connections are assigned entirely at random with no pattern', 'Regions with fewer flights always have larger populations than hubs'], 0),
    ('Why do geographers study the structure of global flight networks?', ['To understand how accessibility and connectivity vary across different regions of the world', 'Flight networks have no relevance to the study of geography', 'Every region of the world is equally connected by air travel', 'Geographers only study networks that involve land transportation'], 0)]),
]),
day(136, [
L('Grammar: Who vs Whom and Pronoun Case',
  'Grade 9 Language strand: who functions as a subject pronoun while whom functions as an object pronoun, and choosing correctly between them depends on whether the pronoun is performing the action or receiving it within its own clause.',
  [('When should who be used in a sentence?', ['When the pronoun is the subject performing the action', 'When the pronoun is always the very last word in a sentence', 'When the pronoun refers only to inanimate objects', 'When no verb appears anywhere in the sentence'], 0),
   ('When should whom be used in a sentence?', ['When the pronoun is the object receiving the action', 'When the pronoun is always the subject of a sentence', 'When the sentence contains no clauses at all', 'When referring exclusively to a place rather than a person'], 0),
   ('In the sentence blank called you last night, which pronoun correctly fills the blank?', ['Who', 'Whom', 'Whose', 'Which'], 0),
   ('One way to test whether who or whom is correct is to replace it with what pair of pronouns?', ['He or she for who, him or her for whom', 'Only numbers, with no pronouns involved', 'Only proper nouns naming a specific person', 'Only punctuation marks with no words at all'], 0),
   ('Why do many English speakers today often use who even in situations that traditionally call for whom?', ['Whom has become less common in casual speech even though formal writing still distinguishes the two', 'Whom was never used correctly at any point in the history of English', 'Formal writing has completely eliminated the word who', 'The two words have always been considered identical in meaning'], 0)]),
M('Financial Literacy: Inflation and the Time Value of Money',
  'Grade 9 Math strand: inflation gradually reduces the purchasing power of money over time, and the time value of money reflects the principle that a given amount of money today is generally worth more than the same amount received in the future.',
  [('What does inflation gradually reduce?', ['The purchasing power of money over time', 'The total number of banks in a country', 'The physical size of paper currency', 'The number of digits in a bank account'], 0),
   ('What does the time value of money principle state?', ['Money available today is generally worth more than the same amount received in the future', 'Money always loses all of its value the moment it is earned', 'Future money is always worth more than present money in every case', 'Time has no connection to the value of money whatsoever'], 0),
   ('Why is money received today generally considered more valuable than the same amount in the future?', ['It can be invested or saved to grow in value before that future date arrives', 'Money received today can never be saved or invested at all', 'Future money always arrives with no possible delay or risk', 'There is no mathematical relationship between time and money'], 0),
   ('If inflation rises faster than the interest earned on savings, what happens to the real value of those savings?', ['The real purchasing power of the savings can decline over time', 'The real purchasing power always increases no matter what', 'Inflation has no effect on the value of savings at all', 'Savings automatically double in value regardless of inflation'], 0),
   ('Understanding inflation and the time value of money is especially useful when planning for what kind of financial decision?', ['Long-term savings and investment decisions', 'Deciding what colour to paint a room', 'Choosing a favourite school subject', 'Selecting a route to walk to school'], 0)]),
Sc('Biology: The Lymphatic System and Immune Defense',
   'Grade 9 Science strand: the lymphatic system is a network of vessels and nodes that drains excess fluid from body tissues and plays a central role in immune defense by filtering pathogens and supporting the activity of white blood cells.',
   [('What is a primary function of the lymphatic system?', ['Draining excess fluid from body tissues', 'Pumping blood directly to and from the heart', 'Digesting food before it enters the stomach', 'Producing sound waves for hearing'], 0),
    ('How does the lymphatic system support immune defense?', ['It filters pathogens and supports the activity of white blood cells', 'It has no connection to the immune system at all', 'It actively works against the bodys own white blood cells', 'It prevents white blood cells from ever functioning'], 0),
    ('What are lymph nodes?', ['Small structures along the lymphatic system that filter lymph fluid and trap pathogens', 'Large muscles located only in the legs', 'Bones found exclusively in the skull', 'A type of blood vessel found only in the heart'], 0),
    ('Why might lymph nodes near an infection become swollen?', ['They are actively filtering pathogens and increasing immune cell activity in response', 'Swelling always indicates the lymphatic system has completely failed', 'Lymph nodes never respond to any kind of infection', 'Swelling only occurs when no infection is present'], 0),
    ('The lymphatic system works closely alongside which other body system to fight infection?', ['The circulatory system', 'The skeletal system', 'The digestive system', 'The reproductive system'], 0)]),
SS('Social Studies: The Geography of the Global Diamond and Gemstone Trade',
   'Grade 9 Social Studies (Geography) strand: the global diamond and gemstone trade connects mining regions, often in Africa and parts of Asia, to cutting, polishing, and retail centres worldwide, and international efforts such as certification schemes attempt to prevent the trade of gems linked to conflict.',
   [('In which regions are many of the worlds diamonds and gemstones mined?', ['Parts of Africa and Asia', 'Only within Western Europe', 'Only within North America', 'Only within Antarctica'], 0),
    ('What happens to many rough diamonds after they are mined?', ['They are transported to specialized centres for cutting and polishing before reaching retail markets', 'They are immediately sold to consumers with no further processing', 'They are permanently discarded after being mined', 'They are converted directly into a different mineral'], 0),
    ('What is the purpose of international certification schemes in the diamond trade?', ['To help prevent the trade of diamonds linked to violent conflict', 'To increase the trade of diamonds linked to conflict', 'To eliminate the diamond trade entirely worldwide', 'To ensure every diamond is mined in the same single country'], 0),
    ('Why can the geography of the diamond trade raise ethical concerns?', ['Mining and trade in some regions has historically been connected to conflict and labour exploitation', 'The diamond trade has never raised any ethical concerns anywhere', 'Diamonds are mined using processes with no human involvement at all', 'Every diamond mining region has identical labour and safety conditions'], 0),
    ('Why do geographers study global commodity chains like the diamond and gemstone trade?', ['To understand how a resource moves from its source to consumers around the world, and who benefits along the way', 'Commodity chains have no geographic dimension worth studying', 'Diamonds are the only resource ever studied in economic geography', 'This topic is considered purely a matter of chemistry, not geography'], 0)]),
]),
day(137, [
L('Writing: The Character Sketch',
  'Grade 9 Language strand: a character sketch is a brief piece of descriptive writing that captures a characters personality, appearance, and mannerisms, often used by writers as a planning tool before drafting a longer story.',
  [('What is a character sketch?', ['A brief piece of descriptive writing that captures a characters personality, appearance, and mannerisms', 'A complete novel with multiple fully developed plots', 'A formal citation of academic sources', 'A mathematical diagram used to solve equations'], 0),
   ('Why might a writer create a character sketch before drafting a longer story?', ['It helps the writer plan and clarify who a character is before writing extended scenes', 'Character sketches serve no planning purpose for writers', 'A character sketch always replaces the need for a full story', 'Writers are required to write a character sketch after finishing a story, never before'], 0),
   ('Which detail would most likely appear in a character sketch?', ['A description of the characters habitual gestures or speech patterns', 'A full outline of an entirely unrelated plot', 'A bibliography of unrelated academic sources', 'A list of unrelated statistical data'], 0),
   ('A well-written character sketch typically focuses on making a character feel what?', ['Distinct and believable to the reader', 'As vague and forgettable as possible', 'Identical to every other character in the story', 'Completely irrelevant to the plot'], 0),
   ('How does a character sketch differ from a full short story?', ['It focuses narrowly on describing a character rather than developing a complete plot', 'It always includes a complete, resolved plot with multiple conflicts', 'It is always longer than a full short story', 'It cannot include any descriptive details of any kind'], 0)]),
M('Sequences and Series: Sigma Notation and Summation',
  'Grade 9 Math strand: sigma notation provides a compact way to write the sum of a sequence of terms, using the Greek letter sigma along with an index that specifies the starting and ending values being added.',
  [('What does sigma notation provide a compact way to represent?', ['The sum of a sequence of terms', 'The product of two unrelated fractions', 'The area of a random polygon', 'The colour of a graphed function'], 0),
   ('What symbol is used in sigma notation to represent a sum?', ['The Greek letter sigma', 'The Greek letter pi', 'A plus sign repeated many times with no other symbol', 'A question mark'], 0),
   ('In sigma notation, what do the numbers above and below the sigma symbol indicate?', ['The starting and ending values of the index being summed', 'The exact final answer of the summation', 'The colour of each term in the sequence', 'The number of variables used in an unrelated equation'], 0),
   ('What does the expression below the sigma symbol typically represent?', ['The variable and starting value of the summation index', 'The final answer to the entire summation', 'An unrelated geometric shape', 'A constant that has no connection to the sum'], 0),
   ('Why is sigma notation especially useful for long sequences and series?', ['It allows a lengthy sum to be written concisely instead of listing every term', 'It makes long sums impossible to calculate', 'It requires every term to be written out individually with no shortcuts', 'It removes the need for any numbers in a summation'], 0)]),
Sc('Chemistry: Colligative Properties of Solutions',
   'Grade 9 Science strand: colligative properties, such as freezing point depression and boiling point elevation, depend on the number of dissolved particles in a solution rather than the identity of the solute, which explains why salt lowers the freezing point of icy roads.',
   [('What do colligative properties of a solution primarily depend on?', ['The number of dissolved particles in the solution', 'The exact colour of the dissolved solute', 'The country where the solution was mixed', 'The time of year the solution was prepared'], 0),
    ('What is freezing point depression?', ['The lowering of a solutions freezing point caused by dissolved particles', 'The raising of a solutions freezing point caused by dissolved particles', 'A process that has no connection to dissolved particles', 'A permanent increase in a solutions total volume'], 0),
    ('What is boiling point elevation?', ['The raising of a solutions boiling point caused by dissolved particles', 'The lowering of a solutions boiling point caused by dissolved particles', 'A process that only occurs in pure water with no solute', 'A change that has no connection to dissolved particles'], 0),
    ('Why is salt commonly spread on icy roads in winter?', ['It lowers the freezing point of the water on the road, helping melt ice at colder temperatures', 'Salt raises the freezing point of water, making ice form faster', 'Salt has no effect on the freezing point of water at all', 'Salt is used only to change the colour of the ice'], 0),
    ('If two solutions contain the same number of dissolved particles but different solutes, how do their colligative properties compare?', ['They are expected to be similar, since colligative properties depend on particle number rather than solute identity', 'They will always be completely different from one another', 'Colligative properties cannot be compared between different solutes', 'The solution with a more colourful solute will always have different properties'], 0)]),
SS('Social Studies: The Geography of Land Reclamation: Building New Land from the Sea',
   'Grade 9 Social Studies (Geography) strand: land reclamation is the process of creating new usable land by draining or filling in areas of water, a technique long used in low-lying countries such as the Netherlands and increasingly seen in coastal cities seeking to expand available space.',
   [('What is land reclamation?', ['The process of creating new usable land by draining or filling in areas of water', 'The process of returning developed land back into open ocean', 'A method used only to build new mountains', 'A term with no connection to coastlines or water'], 0),
    ('Which country has a long historical tradition of land reclamation using polders?', ['The Netherlands', 'Switzerland', 'Mongolia', 'Nepal'], 0),
    ('Why might a coastal city pursue land reclamation projects?', ['To expand available land for housing, infrastructure, or economic development', 'To permanently reduce the total amount of usable land in the city', 'Coastal cities never have a reason to expand available land', 'To eliminate the need for any coastline whatsoever'], 0),
    ('What is one geographic risk associated with land reclaimed from the sea?', ['Reclaimed land can be more vulnerable to flooding or rising sea levels than natural high ground', 'Reclaimed land is always completely immune to flooding', 'Reclamation eliminates all risk of coastal erosion permanently', 'Reclaimed land is always located far from any coastline'], 0),
    ('Why do geographers study land reclamation projects around the world?', ['To understand how human engineering reshapes coastlines and creates new challenges for planning and resilience', 'Land reclamation has no connection to the field of geography', 'Reclaimed land is identical in every way to naturally formed land', 'This topic is considered purely a matter of architecture, not geography'], 0)]),
]),
day(138, [
L('Vocabulary: False Cognates and False Friends',
  'Grade 9 Language strand: a false cognate, or false friend, is a word in one language that looks or sounds similar to a word in another language but has a different meaning, and recognizing these pairs helps language learners avoid common translation mistakes.',
  [('What is a false cognate?', ['A word that looks or sounds similar to a word in another language but has a different meaning', 'A word that is spelled identically in every language on Earth', 'A word invented entirely by a single author', 'A word with no meaning in any language'], 0),
   ('Why are false cognates sometimes called false friends?', ['They appear helpful and familiar but can mislead a language learner', 'They are always genuinely helpful with no risk of confusion', 'The term has no connection to language learning at all', 'False friends refers only to characters in a novel'], 0),
   ('What kind of mistake can false cognates cause?', ['Translation errors, since the learner assumes an incorrect meaning based on similarity', 'They can never cause any kind of mistake', 'They only cause errors in mathematics, not language', 'They eliminate the possibility of any translation error'], 0),
   ('Why is it useful for language learners to study common false cognates?', ['It helps them avoid predictable translation mistakes between related languages', 'Studying false cognates has no benefit for language learners', 'False cognates only exist in languages with no shared history', 'This knowledge is useful only for native speakers, never learners'], 0),
   ('A true cognate, unlike a false cognate, is a word that shares what with a word in another language?', ['Both a similar form and a similar meaning', 'A similar form but always an opposite meaning', 'No similarity of any kind', 'The exact same pronunciation but a different alphabet only'], 0)]),
M('Calculus Preview: Continuity of Functions',
  'Grade 9 Math strand: a function is continuous at a point if its graph has no break, jump, or hole there, meaning the limit of the function as it approaches that point equals the actual value of the function at that point.',
  [('What does it mean for a function to be continuous at a point?', ['Its graph has no break, jump, or hole at that point', 'The function is undefined at every single point', 'The function only exists for negative numbers', 'The graph must always be a straight line'], 0),
   ('For a function to be continuous at a point, its limit at that point must equal what?', ['The actual value of the function at that point', 'Zero, regardless of the function', 'The largest value the function ever reaches', 'A value chosen at random with no connection to the function'], 0),
   ('Which of these would indicate a function is not continuous at a specific point?', ['A hole or gap in the graph at that point', 'A smooth curve with no interruptions', 'A straight line with no breaks', 'A function defined everywhere with matching limits'], 0),
   ('Why is the concept of continuity closely related to the concept of a limit?', ['Continuity requires that a functions limit at a point actually match the functions value there', 'Continuity and limits are entirely unrelated mathematical ideas', 'Limits can only be calculated for continuous functions, never any other kind', 'Continuity has no mathematical definition at all'], 0),
   ('A function that is continuous over an entire interval can generally be drawn how?', ['Without lifting a pen from the paper across that interval', 'Only by using a ruler with no curves allowed', 'Only if the function is a straight line', 'It is impossible to draw a continuous function at all'], 0)]),
Sc('Physics: Projectile Motion',
   'Grade 9 Science strand: projectile motion describes the curved path of an object launched into the air and influenced only by gravity, combining constant horizontal velocity with a steadily changing vertical velocity to produce a parabolic trajectory.',
   [('What forces act on an object undergoing ideal projectile motion, once launched?', ['Only gravity, assuming air resistance is ignored', 'Only friction, with no gravity involved', 'No forces act on the object at all', 'Only a constant forward-pushing engine force'], 0),
    ('What shape does the path of a projectile typically trace?', ['A parabola', 'A perfect circle', 'A straight vertical line', 'A straight horizontal line'], 0),
    ('What happens to the horizontal velocity of a projectile during its flight, ignoring air resistance?', ['It remains constant throughout the flight', 'It steadily increases until the object lands', 'It steadily decreases to zero before landing', 'It reverses direction midway through the flight'], 0),
    ('What happens to the vertical velocity of a projectile as it rises and then falls?', ['It steadily changes due to the constant pull of gravity', 'It remains exactly constant throughout the entire flight', 'It is always equal to zero throughout the flight', 'It increases and decreases at completely random intervals'], 0),
    ('A ball thrown horizontally off a cliff is an example of what kind of motion?', ['Projectile motion', 'Simple harmonic motion', 'Uniform circular motion', 'Terminal velocity motion'], 0)]),
SS('Social Studies: The Geography of Permafrost and Thawing Tundra',
   'Grade 9 Social Studies (Geography) strand: permafrost is ground that remains frozen for at least two consecutive years, and its thawing in tundra regions due to rising temperatures threatens infrastructure, releases stored greenhouse gases, and reshapes northern landscapes and communities.',
   [('What is permafrost?', ['Ground that remains frozen for at least two consecutive years', 'Ground that has never once been frozen', 'A type of ocean current found near the equator', 'A landform found only in tropical rainforests'], 0),
    ('What is causing permafrost in many tundra regions to thaw?', ['Rising temperatures linked to a warming climate', 'A sudden, unexplained increase in snowfall', 'A permanent decrease in global temperatures', 'Permafrost never thaws under any circumstances'], 0),
    ('What infrastructure risk can thawing permafrost create?', ['Ground instability that can damage roads, pipelines, and buildings built on top of it', 'Thawing permafrost always strengthens the ground beneath infrastructure', 'Infrastructure is never affected by changes in ground temperature', 'Thawing permafrost has no connection to construction or infrastructure'], 0),
    ('What greenhouse gases can be released when permafrost thaws?', ['Carbon dioxide and methane, previously trapped in the frozen ground', 'Only oxygen, with no other gases released', 'No gases of any kind are released when permafrost thaws', 'Only helium, previously trapped in the frozen ground'], 0),
    ('Why is thawing permafrost a concern for communities living in northern regions?', ['It can undermine the stability of the land their homes and infrastructure rely on', 'Thawing permafrost has no effect on nearby communities', 'Communities in northern regions are never affected by ground conditions', 'Thawing permafrost always improves the stability of local infrastructure'], 0)]),
]),
day(139, [
L('Reading: Analyzing the Doppelganger Motif in Literature',
  'Grade 9 Language strand: a doppelganger is a characters double or look-alike, often used as a literary motif to explore hidden identity, inner conflict, or a characters darker impulses within a story.',
  [('What is a doppelganger in literature?', ['A characters double or look-alike, often symbolizing a hidden side of that character', 'A minor character who appears only once with no significance', 'A type of formal citation used in essays', 'A punctuation mark used in dialogue'], 0),
   ('What theme does the doppelganger motif often explore?', ['Hidden identity or inner conflict within a character', 'The exact geographic setting of a story', 'A characters favourite hobbies with no deeper meaning', 'The history of a completely unrelated nation'], 0),
   ('Why might an author introduce a doppelganger for a main character?', ['To externalize a struggle happening within the characters own mind', 'To eliminate the need for any character development', 'To confuse readers with no narrative purpose at all', 'To remove the main character from the story entirely'], 0),
   ('A doppelganger is best described as a type of what literary device?', ['A recurring motif used to develop character and theme', 'A rhyme scheme used only in poetry', 'A formal citation format', 'A grammatical rule about sentence structure'], 0),
   ('How might a reader interpret the appearance of a doppelganger in a story?', ['As a signal that the story is exploring duality or conflicting aspects of identity', 'As a sign that the story has no thematic content at all', 'As proof that the story takes place in outer space', 'As an indication that the story has ended'], 0)]),
M('Geometry: An Introduction to Polar Coordinates',
  'Grade 9 Math strand: polar coordinates locate a point using a distance from a fixed origin and an angle from a fixed direction, offering an alternative to the x and y values used in the standard coordinate plane.',
  [('What two values are used to locate a point in polar coordinates?', ['A distance from the origin and an angle from a fixed direction', 'Only a single x-value with no other information', 'Only a colour and a shape', 'Only the slope of an unrelated line'], 0),
   ('What is the fixed point called from which distance is measured in the polar coordinate system?', ['The origin, or pole', 'The vertex of a triangle', 'The discriminant', 'The asymptote'], 0),
   ('How do polar coordinates differ from standard x-y coordinates?', ['They describe a points location using distance and angle rather than horizontal and vertical position', 'They can only be used to describe points located at the origin', 'They cannot be used to graph any kind of curve', 'They are identical to x-y coordinates in every way'], 0),
   ('Which type of curve is often easier to describe using polar coordinates than standard coordinates?', ['A spiral or circular curve centred on the origin', 'A straight vertical line only', 'A single isolated point with no curve at all', 'A curve that does not exist on any graph'], 0),
   ('In polar coordinates, what does increasing the angle value typically represent?', ['Rotating further around the origin from the fixed reference direction', 'Moving directly away from the origin with no rotation', 'Decreasing the distance from the origin to zero', 'Changing the colour of the graphed curve'], 0)]),
Sc('Earth Science: Karst Topography and Cave Formation',
   'Grade 9 Science strand: karst topography forms when slightly acidic water gradually dissolves soluble rock such as limestone, creating sinkholes, underground caves, and dramatic surface features over long periods of time.',
   [('What type of rock is most commonly associated with karst topography?', ['Soluble rock such as limestone', 'Rock that is completely resistant to any form of dissolving', 'Only volcanic rock formed from lava', 'Only rock found on the ocean floor'], 0),
    ('What process gradually creates karst features like caves and sinkholes?', ['Slightly acidic water dissolving soluble rock over long periods of time', 'A sudden, single explosive event with no gradual process', 'Wind erosion acting alone with no water involved', 'Freezing temperatures with no connection to water chemistry'], 0),
    ('What is a sinkhole?', ['A depression or hole formed when underground rock dissolves and the ground above collapses', 'A raised mountain peak formed by tectonic activity', 'A type of river delta found near an ocean', 'A structure built intentionally by engineers to store water'], 0),
    ('Why does water capable of dissolving limestone tend to be slightly acidic?', ['It often absorbs carbon dioxide from the air or soil, forming a weak acid', 'Limestone can only be dissolved by pure water with no acidity at all', 'Acidity has no connection to a waters ability to dissolve rock', 'The water becomes acidic only after passing through solid granite'], 0),
    ('Why might karst regions be more prone to groundwater contamination?', ['Water can move quickly through cracks and caves with little natural filtering by soil', 'Karst regions have no underground water of any kind', 'Groundwater in karst regions is always completely immune to contamination', 'Water moves more slowly through karst regions than anywhere else'], 0)]),
SS('Social Studies: The Geography of Global Financial Centres and Banking Hubs',
   'Grade 9 Social Studies (Geography) strand: global financial centres, such as major cities with concentrated banking, stock exchange, and insurance activity, serve as hubs that connect national economies to international capital flows and shape patterns of global economic influence.',
   [('What characterizes a global financial centre?', ['A concentration of banking, stock exchange, and insurance activity in one location', 'A city with no economic activity of any kind', 'A rural area with no access to any financial services', 'A region that has banned all forms of international trade'], 0),
    ('What role do global financial centres play in the world economy?', ['They connect national economies to international flows of capital and investment', 'They isolate national economies from any international connection', 'Financial centres have no measurable role in the global economy', 'They exist only to serve the local population with no international role'], 0),
    ('Why do certain cities emerge as major global financial centres rather than others?', ['Factors like infrastructure, regulation, time zone, and history can attract concentrated financial activity', 'Financial centres are chosen entirely at random with no contributing factors', 'Every city in the world has an identical chance of becoming a financial centre', 'Financial centres form only in cities with no history of trade'], 0),
    ('How can the location of a global financial centre influence a countrys economic importance?', ['It can help attract international investment and business activity to that region', 'The location of a financial centre has no effect on a countrys economy', 'Financial centres always reduce a countrys economic influence', 'A financial centres location is entirely disconnected from investment activity'], 0),
    ('Why do geographers study the distribution of global financial centres around the world?', ['To understand patterns of economic power and connection between different regions of the world', 'Financial centres have no connection to the study of geography', 'Every region of the world has identical levels of economic influence', 'This topic is considered purely a matter of accounting, not geography'], 0)]),
]),
day(140, [
L('Language Review: Modifiers, Semantics, Narration, and Pronoun Case',
  'Grade 9 Language strand review: students revisit hyphens and compound modifiers, semantic change, stream of consciousness narration, who vs whom, and the doppelganger motif from Days 131-139.',
  [('What is a compound modifier?', ['Two or more words joined together to describe a noun as a single unit', 'A single unmodified noun with no description', 'A punctuation mark used only in dialogue', 'A sentence with no verb at all'], 0),
   ('What is semantic change?', ['The process by which a words meaning shifts over time', 'A rule that prevents any word from ever changing meaning', 'A punctuation mark used to separate clauses', 'A type of formal citation format'], 0),
   ('What does stream of consciousness narration attempt to capture?', ['A characters continuous flow of thoughts and impressions as they occur', 'Only a characters physical actions with no inner thought at all', 'A strict, chronological summary of an entire plot', 'A list of unrelated facts with no connection to any character'], 0),
   ('When should whom be used in a sentence?', ['When the pronoun is the object receiving the action', 'When the pronoun is always the subject of a sentence', 'When the sentence contains no clauses at all', 'When referring exclusively to a place rather than a person'], 0),
   ('What is a doppelganger in literature?', ['A characters double or look-alike, often symbolizing a hidden side of that character', 'A minor character who appears only once with no significance', 'A type of formal citation used in essays', 'A punctuation mark used in dialogue'], 0)]),
M('Math Review: Algebra, Number Theory, Statistics, and Calculus Preview',
  'Grade 9 Math strand review: students revisit radical equations, the Euclidean algorithm, Bayes Theorem, z-scores, and continuity of functions from Days 131-139.',
  [('What defines a radical equation?', ['An equation in which a variable appears inside a radical, such as a square root', 'An equation with no variables of any kind', 'An equation that only involves whole number coefficients', 'An equation that cannot be graphed'], 0),
   ('What does the Euclidean algorithm calculate?', ['The greatest common divisor of two integers', 'The least common multiple of every integer', 'The exact prime factorization of a single number', 'The sum of two unrelated fractions'], 0),
   ('What does Bayes Theorem allow you to do?', ['Update the probability of an event based on new evidence', 'Calculate the area of any triangle', 'Determine the exact value of an unrelated variable', 'Eliminate the need for probability altogether'], 0),
   ('What does a z-score measure?', ['How many standard deviations a data point lies above or below the mean', 'The total number of data points in a set', 'The exact colour associated with a data point', 'The name of the variable being studied'], 0),
   ('What does it mean for a function to be continuous at a point?', ['Its graph has no break, jump, or hole at that point', 'The function is undefined at every single point', 'The function only exists for negative numbers', 'The graph must always be a straight line'], 0)]),
Sc('Science Review: Chemistry, Physics, Biology, and Earth Systems',
   'Grade 9 Science strand review: students revisit chemical equilibrium, torque and rotational equilibrium, stem cells and differentiation, comets and near-Earth objects, and projectile motion from Days 131-139.',
   [('What defines chemical equilibrium in a reversible reaction?', ['A state where the forward and reverse reaction rates become equal', 'A state where all reactants are completely used up', 'A state where no reaction has ever occurred', 'A state where only the forward reaction takes place'], 0),
    ('What does torque measure?', ['The turning effect of a force applied at a distance from a pivot point', 'The total mass of an object with no reference to force', 'The temperature of a rotating object', 'The colour of an object in motion'], 0),
    ('What is a defining feature of a stem cell?', ['It is an unspecialized cell capable of developing into many different cell types', 'It is a fully specialized cell that can never change', 'It is a cell found only in plants, never animals', 'It is a cell that cannot divide under any circumstances'], 0),
    ('What defines a near-Earth object?', ['A comet or asteroid whose orbit brings it relatively close to Earths orbit', 'Any object located inside Earths own atmosphere permanently', 'A planet located within our solar system', 'A star located outside the Milky Way galaxy'], 0),
    ('What shape does the path of a projectile typically trace?', ['A parabola', 'A perfect circle', 'A straight vertical line', 'A straight horizontal line'], 0)]),
SS('Social Studies Review: Global Geography and Regional Case Studies',
   'Grade 9 Social Studies (Geography) strand review: students revisit Antarctica and the Antarctic Treaty, global biodiversity hotspots, enclaves and special administrative regions, the diamond and gemstone trade, and permafrost from Days 131-139.',
   [('What is the Antarctic Treaty System?', ['An international agreement governing Antarctica for peaceful, scientific purposes', 'A single countrys law that governs all of Antarctica', 'A trade agreement unrelated to any scientific activity', 'An agreement that has never been signed by any nation'], 0),
    ('What defines a biodiversity hotspot?', ['A region with an exceptionally high number of unique species that is also facing significant habitat loss', 'Any region with no living species present at all', 'A region where habitat loss has never occurred', 'A region with only one single species living in it'], 0),
    ('What is an enclave?', ['A territory entirely surrounded by the land of another country', 'A territory located in the middle of an ocean with no land nearby', 'A region with no borders of any kind', 'A term with no connection to political geography'], 0),
    ('What is the purpose of international certification schemes in the diamond trade?', ['To help prevent the trade of diamonds linked to violent conflict', 'To increase the trade of diamonds linked to conflict', 'To eliminate the diamond trade entirely worldwide', 'To ensure every diamond is mined in the same single country'], 0),
    ('What is permafrost?', ['Ground that remains frozen for at least two consecutive years', 'Ground that has never once been frozen', 'A type of ocean current found near the equator', 'A landform found only in tropical rainforests'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_131_140)
    append_to(9, g9_131_140)
