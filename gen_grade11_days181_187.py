#!/usr/bin/env python3
"""Grade 11, Days 181-187 -- FINAL batch, extends Grade 11 from 180 to 187
days, completing the full 187-day Ontario curriculum target for this grade.
Topics chosen after dumping the entire existing Day 1-180 title list
(data/grade11.json) via
  python3 -c "import json; d=json.load(open('data/grade11.json'));
  [print(s['subject'],'::',s['title']) for day in d for s in day['subjects']]"
and cross-checking every candidate title (and distinctive keyword within it)
against that full dump before use. None of the 24 new topic titles below,
nor any keyword drawn from them (Pastoral, Epic, Comedy of Manners, Toast,
Content Moderation, Definite Integral, Sieve of Eratosthenes, Simpson,
Distance from a Point to a Plane, Catalan, Polar Coordinates, Karyotyping,
Allergies, Seed Dispersal, Edge Effects, Protists, Vitamins, Grahams Law,
Net Ionic, Significant Figures, Boiling Point Elevation, Hand Warmers,
Silica Gel, Fragments and Run-Ons), appears anywhere in Days 1-180.

New topics, Days 181-186 (one new topic per subject per day):
  English: the pastoral tradition; sentence fragments and run-ons; the
    epic as a poetic form; the comedy of manners; the toast as a short
    celebratory speech; content moderation and platform policy.
  Functions: definite integrals and area under a curve (the natural next
    step after Day 178's antiderivatives introduction); the Sieve of
    Eratosthenes; Simpsons paradox; the distance from a point to a plane
    in three dimensions (extending Day 176's line-plane intersection);
    Catalan numbers; polar coordinates and conversion to rectangular form.
  Biology: karyotyping and chromosomal analysis; allergies and
    hypersensitivity; plant seed dispersal strategies; edge effects and
    habitat fragmentation; protists; vitamins and coenzymes in metabolism.
  Chemistry: Grahams law of effusion; net ionic equations and spectator
    ions; significant figures in quantitative chemistry; boiling point
    elevation; the exothermic crystallization chemistry of hand warmers;
    silica gel and desiccants.

Day 187 is the final cross-subject review day of the entire 187-day Grade
11 build, matching the structure of every earlier review day (Days 10, 20,
... 180): one review lesson per subject, each reusing five first-questions
verbatim from the batch, drawn from Days 181, 182, 183, 184, and 185 (the
same "pick five of the batchs regular days" convention used for Day 180,
which drew from five of the nine days in the 171-180 batch). The four Day
187 review titles below were checked against every earlier review-day
title in Days 1-180 and are textually distinct from all of them. Because
this is the capstone review closing out the full K-12 Grade 11 build, the
summaries acknowledge that milestone in their closing line while keeping
the exact mechanical review-day format (title naming the batchs topics,
summary naming the five reviewed lessons, five verbatim first-questions)
used throughout every prior review day.

Subject keys for Grade 11 are "English", "Functions", "Biology",
"Chemistry" (same as all earlier Grade 11 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are avoided entirely (e.g. "Grahams law", "Simpsons paradox",
matching the existing convention seen in "Wilsons theorem", "Eulers
Formula", "Fermats Little Theorem" elsewhere in this file set).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E11 = 'https://tvolearn.com/pages/grade-11-english'
F11 = 'https://tvolearn.com/pages/grade-11-functions'
B11 = 'https://tvolearn.com/pages/grade-11-biology'
C11 = 'https://tvolearn.com/pages/grade-11-chemistry'
RE, RF, RB, RC = (
    'TVO Learn: Grade 11 English',
    'TVO Learn: Grade 11 Functions',
    'TVO Learn: Grade 11 Biology',
    'TVO Learn: Grade 11 Chemistry',
)


def E(t, s, q):
    return sub('English', t, s, RE, E11, q)


def F(t, s, q):
    return sub('Functions', t, s, RF, F11, q)


def B(t, s, q):
    return sub('Biology', t, s, RB, B11, q)


def C(t, s, q):
    return sub('Chemistry', t, s, RC, C11, q)


def _rebalance_answer_positions(days, seed=20260818):
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


g11_181_187 = [
day(181, [
E('Literature: The Pastoral Tradition — Idyllic Nature in Poetry',
  'Grade 11 English strand: pastoral poetry idealizes rural life and the natural landscape, often through the voice of a shepherd or countryside speaker, contrasting the simplicity and harmony of nature with the corruption or stress of urban and courtly life.',
  [('What does pastoral poetry typically idealize?', ['Rural life and the natural landscape', 'The chaos of a crowded courtroom', 'The stress of urban and courtly life', 'A setting with no connection to nature at all'], 0),
   ('Whose voice does pastoral poetry often adopt as its speaker?', ['A shepherd or countryside speaker', 'A judge presiding over a trial', 'A factory worker in a city', 'A speaker with no connection to the countryside'], 0),
   ('What contrast does pastoral poetry frequently draw?', ['The harmony of nature against the corruption of urban or courtly life', 'A contrast between two unrelated cities', 'No contrast of any kind', 'The equal chaos of both country and city life'], 0),
   ('What quality of rural life does pastoral poetry emphasize?', ['Simplicity and harmony', 'Constant conflict and disorder', 'A total absence of any landscape description', 'The complexity of industrial machinery'], 0),
   ('Why might a poet use the pastoral mode to comment indirectly on court or city life?', ['An idealized countryside offers a contrasting backdrop that implicitly critiques urban corruption', 'Pastoral poetry is required to ignore any urban subject entirely', 'The pastoral mode forbids any form of implicit commentary', 'Rural and urban settings are treated as identical in pastoral poetry'], 0)]),
F('Calculus: Definite Integrals and the Area Under a Curve',
  'Grade 11 Functions strand: a definite integral uses upper and lower bounds to calculate the exact accumulated area between a curve and the horizontal axis, building on the idea of an antiderivative to turn the informal notion of area under a curve into a precise, calculable quantity.',
  [('What does a definite integral calculate?', ['The exact accumulated area between a curve and the horizontal axis', 'The slope of a curve at a single point', 'The number of times a curve crosses the vertical axis', 'A quantity with no connection to area at all'], 0),
   ('What two values define the range over which a definite integral is calculated?', ['An upper bound and a lower bound', 'Only a single fixed point', 'The maximum and minimum of an unrelated function', 'A range with no defined limits at all'], 0),
   ('What earlier idea does the definite integral build on?', ['The antiderivative', 'The multiplication table', 'The Pythagorean theorem', 'A concept with no connection to calculus'], 0),
   ('What does the definite integral turn the informal notion of area under a curve into?', ['A precise, calculable quantity', 'An estimate that can never be calculated exactly', 'A quantity with no numerical value at all', 'A concept limited only to straight lines'], 0),
   ('Why is finding an antiderivative a useful first step before evaluating a definite integral?', ['The antiderivative, evaluated at the bounds, gives the accumulated area directly', 'An antiderivative has no connection to evaluating area at all', 'A definite integral can only be evaluated without any antiderivative', 'Antiderivatives always produce a result of zero regardless of the function'], 0)]),
B('Biology: Karyotyping and Chromosomal Analysis Techniques',
  'Grade 11 Biology strand: a karyotype is an organized image of an individuals complete set of chromosomes, arranged by size and banding pattern, that geneticists use to detect structural abnormalities and changes in chromosome number that a standard genetic test might otherwise miss.',
  [('What is a karyotype?', ['An organized image of an individuals complete set of chromosomes', 'A single strand of unpaired DNA', 'A photograph of a whole living cell', 'An image with no connection to chromosomes at all'], 0),
   ('How are chromosomes typically arranged in a karyotype?', ['By size and banding pattern', 'In a random, unordered arrangement', 'By colour only, with no reference to size', 'In alphabetical order by chromosome name'], 0),
   ('What can a karyotype help geneticists detect?', ['Structural abnormalities and changes in chromosome number', 'The exact age of the individual being tested', 'The colour of a persons eyes', 'A quantity with no genetic significance at all'], 0),
   ('Why is a karyotype useful compared to some other genetic tests?', ['It can reveal large-scale chromosomal changes that other tests might miss', 'It reveals no genetic information of any kind', 'It can only be performed on plant cells, never human cells', 'It replaces the need for any chromosomes to be examined'], 0),
   ('What might an unusual number of chromosomes visible in a karyotype indicate?', ['A chromosomal abnormality such as an extra or missing chromosome', 'A completely normal and expected genetic result in every case', 'A condition unrelated to chromosomes entirely', 'That the sample was not actually taken from a living cell'], 0)]),
C('Chemistry: Grahams Law of Effusion and Gas Diffusion Rates',
  'Grade 11 Chemistry strand: Grahams law states that the rate at which a gas effuses through a tiny opening is inversely proportional to the square root of its molar mass, meaning lighter gas molecules escape faster than heavier ones under the same conditions.',
  [('What does Grahams law describe?', ['The rate at which a gas effuses through a tiny opening', 'The exact colour of a gas sample', 'The boiling point of a liquid', 'A quantity with no connection to gases at all'], 0),
   ('According to Grahams law, what is the rate of effusion inversely proportional to?', ['The square root of the gas molar mass', 'The temperature of the surrounding room only', 'The colour of the container holding the gas', 'A quantity with no relationship to molar mass'], 0),
   ('Which gas molecules escape faster under Grahams law, given the same conditions?', ['Lighter gas molecules', 'Heavier gas molecules', 'Molecules of any mass escape at an identical rate', 'Only gas molecules with no mass at all'], 0),
   ('What does effusion refer to in the context of Grahams law?', ['A gas escaping through a tiny opening', 'A liquid boiling at constant pressure', 'A solid melting into a liquid', 'A process with no connection to gas particles'], 0),
   ('Why might helium escape from a small opening faster than carbon dioxide under identical conditions?', ['Helium has a much lower molar mass, so it effuses more quickly', 'Helium and carbon dioxide always effuse at exactly the same rate', 'Helium has a higher molar mass than carbon dioxide', 'Molar mass has no effect on the rate of effusion'], 0)]),
]),
day(182, [
E('Grammar: Sentence Fragments and Run-Ons — Deliberate and Accidental',
  'Grade 11 English strand: a sentence fragment lacks a complete subject-verb combination or a complete thought, while a run-on sentence jams two or more independent clauses together without proper punctuation, and skilled writers distinguish between these as accidental errors to fix and deliberate fragments used for stylistic emphasis.',
  [('What does a sentence fragment lack?', ['A complete subject-verb combination or a complete thought', 'Any punctuation whatsoever', 'A title at the start of the sentence', 'A minimum of ten words'], 0),
   ('What happens in a run-on sentence?', ['Two or more independent clauses are joined without proper punctuation', 'A single independent clause is left entirely unpunctuated', 'A sentence is broken into several very short fragments', 'No clauses of any kind are present in the sentence'], 0),
   ('When might a skilled writer use a sentence fragment on purpose?', ['For stylistic emphasis', 'Only when writing formal academic essays with no exceptions', 'Fragments are never used deliberately under any circumstance', 'Only in legal documents that forbid complete sentences'], 0),
   ('What is one way to correct a run-on sentence?', ['Joining the independent clauses with proper punctuation or a conjunction', 'Removing all punctuation from the sentence entirely', 'Adding more independent clauses without any punctuation', 'Deleting the subject of every clause in the sentence'], 0),
   ('Why is it useful for a writer to recognize the difference between an accidental fragment and a deliberate one?', ['It lets the writer distinguish between an error to fix and a stylistic choice worth keeping', 'There is no meaningful difference between the two in any context', 'Deliberate fragments are always considered grammatical errors', 'Accidental fragments always improve the clarity of a sentence'], 0)]),
F('Number Theory: The Sieve of Eratosthenes and Prime Generation',
  'Grade 11 Functions strand: the Sieve of Eratosthenes generates all prime numbers up to a given limit by listing every integer in that range and systematically crossing out the multiples of each prime starting from two, leaving only the primes uncrossed once the process is complete.',
  [('What does the Sieve of Eratosthenes generate?', ['All prime numbers up to a given limit', 'Only the multiples of ten within a range', 'A single randomly chosen prime number', 'A list with no connection to prime numbers at all'], 0),
   ('What is systematically crossed out during the Sieve of Eratosthenes process?', ['The multiples of each prime, starting from two', 'Every number in the list without exception', 'Only numbers that are already prime', 'Numbers chosen completely at random'], 0),
   ('What remains once the Sieve of Eratosthenes process is complete?', ['Only the uncrossed prime numbers', 'Only the numbers that were crossed out', 'A list containing no numbers at all', 'Every number, since none are ever removed'], 0),
   ('At what number does the Sieve of Eratosthenes typically begin crossing out multiples?', ['Two', 'One thousand', 'Zero', 'A number that varies randomly each time'], 0),
   ('Why is the Sieve of Eratosthenes considered an efficient method for finding primes within a range?', ['It eliminates composite numbers systematically rather than testing each number individually for divisibility', 'It requires testing every possible divisor of every number one at a time', 'It generates only even numbers, ignoring primes entirely', 'It has no systematic method and relies purely on guessing'], 0)]),
B('Biology: Allergies and Hypersensitivity — When Immune Responses Overreact',
  'Grade 11 Biology strand: an allergy is a hypersensitive immune response in which the body treats a normally harmless substance such as pollen or a food protein as a threat, triggering mast cells to release histamine and other chemicals that produce symptoms ranging from mild irritation to a severe, life-threatening reaction.',
  [('What is an allergy?', ['A hypersensitive immune response to a normally harmless substance', 'A response in which the immune system never reacts to anything', 'A condition with no connection to the immune system at all', 'A permanent absence of any immune activity'], 0),
   ('What kind of substance can trigger an allergic reaction?', ['A normally harmless substance such as pollen or a food protein', 'Only substances that are inherently toxic to every person', 'A substance found only inside bacteria', 'A substance with no biological origin at all'], 0),
   ('What cell type releases histamine during an allergic reaction?', ['Mast cells', 'Red blood cells', 'Muscle cells', 'A cell type with no role in immune responses'], 0),
   ('What chemical do mast cells release that produces many allergy symptoms?', ['Histamine', 'Insulin', 'Hemoglobin', 'A chemical unrelated to any immune response'], 0),
   ('What range of severity can allergic reactions have, from mild to extreme?', ['From mild irritation to a severe, life-threatening reaction', 'Every allergic reaction is identical in severity with no variation', 'Allergic reactions are always mild and never dangerous', 'Allergic reactions always require no immune involvement at all'], 0)]),
C('Chemistry: Net Ionic Equations and Spectator Ions',
  'Grade 11 Chemistry strand: a net ionic equation shows only the ions and molecules that actually participate in a chemical change, removing spectator ions that appear unchanged on both sides of the full equation, which highlights the specific reaction actually taking place in an aqueous solution.',
  [('What does a net ionic equation show?', ['Only the ions and molecules that actually participate in a chemical change', 'Every single ion present in the solution, whether or not it reacts', 'A full molecular equation with no ions removed', 'A description with no connection to a chemical reaction'], 0),
   ('What is a spectator ion?', ['An ion that appears unchanged on both sides of the full equation', 'An ion that is completely consumed during the reaction', 'An ion that changes into a different element entirely', 'An ion with no presence in the original solution at all'], 0),
   ('What happens to spectator ions when writing a net ionic equation?', ['They are removed from the equation', 'They are duplicated on both sides of the equation', 'They become the only ions shown in the equation', 'They are converted into solid precipitates automatically'], 0),
   ('What does a net ionic equation highlight about a reaction in aqueous solution?', ['The specific reaction actually taking place', 'A reaction that never actually occurs in solution', 'Only the physical appearance of the solution', 'A process entirely unrelated to the original reactants'], 0),
   ('Why is identifying spectator ions useful when analyzing a reaction in solution?', ['It isolates the actual chemical change from ions that are present but do not react', 'Spectator ions are always the most important part of any reaction', 'Removing spectator ions always eliminates the entire reaction', 'Spectator ions cannot be identified in any aqueous solution'], 0)]),
]),
day(183, [
E('Literature: The Epic — Conventions of a Sweeping Poetic Form',
  'Grade 11 English strand: an epic is a long narrative poem that follows a hero of great cultural significance through a series of trials often spanning vast distances or timescales, traditionally opening with an invocation to a muse and employing an elevated, formal style suited to its grand subject matter.',
  [('What kind of narrative is an epic?', ['A long narrative poem following a hero of great cultural significance', 'A short lyric poem about a single private emotion', 'A brief riddle with no narrative content', 'A poem with no central character of any kind'], 0),
   ('What does an epic hero typically undergo throughout the poem?', ['A series of trials often spanning vast distances or timescales', 'A single uneventful day with no challenges at all', 'No challenges of any kind throughout the narrative', 'A trial that is resolved before the poem even begins'], 0),
   ('What does an epic traditionally open with?', ['An invocation to a muse', 'A detailed weather report', 'A list of unrelated characters with no context', 'A modern news bulletin'], 0),
   ('What kind of style does an epic traditionally employ?', ['An elevated, formal style suited to its grand subject matter', 'A casual, conversational style with no formality', 'A style identical to a text message', 'A style that avoids any elevated language whatsoever'], 0),
   ('Why might an epics vast scope of distance or time suit its subject matter?', ['A grand, sweeping scale reflects the heros larger-than-life cultural significance', 'A vast scope has no connection to a heros significance', 'Epics are always confined to a single room with no scope at all', 'Epic poems must always be shorter than a single stanza'], 0)]),
F('Statistics: Simpsons Paradox and the Danger of Aggregated Data',
  'Grade 11 Functions strand: Simpsons paradox occurs when a trend that appears in several separate groups of data reverses or disappears once those groups are combined into a single aggregated data set, showing why statisticians must examine underlying subgroups rather than relying on combined totals alone.',
  [('What is Simpsons paradox?', ['A trend appearing in separate groups that reverses once the groups are combined', 'A trend that always stays identical whether data is grouped or combined', 'A paradox with no connection to statistics at all', 'A rule stating that combined data is always more accurate than grouped data'], 0),
   ('What can happen to a trend seen in separate groups of data once they are aggregated?', ['It can reverse or disappear entirely', 'It always becomes stronger and more obvious', 'It always remains exactly the same in every case', 'It becomes impossible to observe in the separate groups as well'], 0),
   ('What does Simpsons paradox show about relying only on combined totals?', ['Combined totals alone can hide or misrepresent an underlying trend', 'Combined totals always reveal every trend accurately', 'Aggregated data can never be misleading in any situation', 'Subgroups never need to be examined under any circumstance'], 0),
   ('What should a careful statistician do to avoid being misled by Simpsons paradox?', ['Examine the underlying subgroups rather than relying on combined totals alone', 'Ignore every subgroup and rely only on the combined total', 'Avoid collecting any subgroup data whatsoever', 'Assume that aggregated data is always correct without checking further'], 0),
   ('Why is Simpsons paradox considered a caution for interpreting real-world statistics?', ['It shows that a seemingly clear pattern in combined data can be misleading without deeper analysis', 'It proves that no statistical pattern can ever be trusted at all', 'It guarantees that subgroup data is always irrelevant to any conclusion', 'It shows that aggregated data is always more reliable than subgroup data'], 0)]),
B('Plant Biology: Seed Dispersal Strategies — Wind, Water, and Animal Vectors',
  'Grade 11 Biology strand: plants have evolved a range of seed dispersal strategies, from lightweight winged or feathery seeds carried by wind, to buoyant seeds that float on water, to fruits and burrs that attract or attach to animals, all of which reduce competition with the parent plant and help colonize new habitats.',
  [('What is one strategy plants use to disperse seeds by wind?', ['Lightweight winged or feathery seeds', 'Seeds that are extremely dense and heavy', 'Seeds that dissolve completely before they can travel', 'Seeds with no adaptation for movement of any kind'], 0),
   ('What feature allows some seeds to be dispersed by water?', ['Buoyancy that lets them float', 'A structure that immediately sinks in water', 'A complete lack of any protective coating', 'An inability to survive contact with water at all'], 0),
   ('How do burrs typically achieve dispersal by animals?', ['By attaching to fur or feathers as an animal passes by', 'By being completely ignored by every animal', 'By dissolving instantly on contact with an animal', 'By repelling every animal that comes near them'], 0),
   ('What advantage does seed dispersal provide relative to the parent plant?', ['It reduces competition with the parent plant for resources', 'It guarantees the seed will never germinate at all', 'It increases competition between the seed and the parent plant', 'It has no effect on competition of any kind'], 0),
   ('Why is colonizing new habitats an important outcome of effective seed dispersal?', ['It allows a plant species to spread into new areas and increase its chances of survival', 'New habitats always prevent a seed from germinating', 'Seed dispersal has no connection to colonizing new areas', 'Colonizing new habitats always reduces a species chances of survival'], 0)]),
C('Chemistry: Significant Figures and Precision in Quantitative Chemistry',
  'Grade 11 Chemistry strand: significant figures represent the digits in a measurement that carry meaningful information about its precision, and applying consistent rules for significant figures in calculations ensures that a final answer does not falsely imply more precision than the original measured data actually supports.',
  [('What do significant figures represent in a measurement?', ['The digits that carry meaningful information about its precision', 'Every digit in a number regardless of its meaning', 'Only the first digit of any measured value', 'A quantity with no connection to precision at all'], 0),
   ('Why are consistent rules for significant figures applied during calculations?', ['To ensure a final answer does not falsely imply more precision than the original data supports', 'To make every calculated answer appear as precise as possible regardless of the data', 'Significant figures have no effect on the precision implied by an answer', 'To remove all decimal points from every calculated value'], 0),
   ('What might happen if significant figures are ignored in a chemistry calculation?', ['The final answer could imply a level of precision the original measurements do not support', 'The final answer would always become less precise than the original data', 'Ignoring significant figures always produces a completely correct result', 'The calculation would be entirely unaffected by any precision issue'], 0),
   ('What kind of information do significant figures help communicate about measured data?', ['How precisely a quantity was actually measured', 'The exact chemical identity of a substance', 'The colour of the substance being measured', 'A value with no connection to measurement at all'], 0),
   ('Why is precision in quantitative chemistry important when reporting experimental results?', ['It ensures other scientists can accurately judge the reliability of the reported data', 'Precision has no bearing on how other scientists interpret results', 'Reported results never need to reflect the precision of the original measurement', 'Significant figures are only relevant to qualitative, not quantitative, chemistry'], 0)]),
]),
day(184, [
E('Drama: The Comedy of Manners — Wit and Social Satire on Stage',
  'Grade 11 English strand: a comedy of manners satirizes the behaviour and pretensions of a particular social class, relying on witty, polished dialogue and characters obsessed with reputation and social status to expose the gap between how people present themselves and how they actually behave.',
  [('What does a comedy of manners satirize?', ['The behaviour and pretensions of a particular social class', 'A tragic historical event with no comedic elements', 'A setting with no connection to any social class', 'A purely private, solitary experience with no social dimension'], 0),
   ('What kind of dialogue does a comedy of manners typically rely on?', ['Witty, polished dialogue', 'Dialogue with no wit or polish of any kind', 'Silence, with no spoken dialogue at all', 'Dialogue borrowed entirely from a formal legal document'], 0),
   ('What are characters in a comedy of manners often preoccupied with?', ['Reputation and social status', 'Physical survival in a wilderness setting', 'A complete indifference to how others perceive them', 'Scientific discovery with no social concern at all'], 0),
   ('What gap does a comedy of manners often expose?', ['The gap between how people present themselves and how they actually behave', 'A gap between two unrelated historical periods', 'No gap of any kind, since characters are always sincere', 'The gap between two entirely different literary genres'], 0),
   ('Why is witty dialogue especially important to the comedy of manners genre?', ['It sharpens the satire of social pretension through clever, pointed exchanges', 'Witty dialogue has no connection to satire of any kind', 'A comedy of manners forbids any form of humour', 'Dialogue in this genre must always be entirely serious and formal'], 0)]),
F('Geometry: The Distance from a Point to a Plane in Three Dimensions',
  'Grade 11 Functions strand: the distance from a point to a plane in three dimensions is found by projecting the vector from a known point on the plane to the given point onto the planes normal vector, giving the shortest, perpendicular distance between the point and the plane.',
  [('What is being calculated when finding the distance from a point to a plane?', ['The shortest, perpendicular distance between the point and the plane', 'The longest possible path between the point and the plane', 'A distance measured only along the plane itself', 'A quantity with no connection to distance at all'], 0),
   ('What vector is used to help calculate the distance from a point to a plane?', ['The planes normal vector', 'A vector lying entirely within an unrelated line', 'A vector with no defined direction at all', 'The vector describing an entirely different plane'], 0),
   ('What kind of distance does this method always produce, relative to the plane?', ['A perpendicular distance', 'A distance measured parallel to the plane', 'A distance that varies depending on the angle chosen', 'A distance with no defined geometric meaning'], 0),
   ('What is projected onto the normal vector during this calculation?', ['The vector from a known point on the plane to the given point', 'A vector with no connection to either the point or the plane', 'The equation of an entirely unrelated line', 'The coordinates of the origin only'], 0),
   ('How does this calculation relate to the earlier idea of finding where a line intersects a plane?', ['Both rely on the planes equation and normal vector to describe the planes geometry precisely', 'The two calculations have no mathematical relationship at all', 'Finding a line-plane intersection never involves the planes equation', 'Distance from a point to a plane cannot be calculated using the planes normal vector'], 0)]),
B('Ecology: Edge Effects and Habitat Fragmentation',
  'Grade 11 Biology strand: habitat fragmentation breaks a large, continuous habitat into smaller, isolated patches, increasing the amount of edge relative to interior habitat, and this edge effect exposes interior species to different light, wind, and predation conditions that can reduce biodiversity even when total habitat area seems only modestly reduced.',
  [('What does habitat fragmentation do to a large, continuous habitat?', ['Breaks it into smaller, isolated patches', 'Expands it into an even larger continuous area', 'Leaves it completely unchanged in every way', 'Converts it entirely into open ocean'], 0),
   ('What increases relative to interior habitat as fragmentation occurs?', ['The amount of edge habitat', 'The amount of interior habitat, with no change to edge', 'The total number of unrelated species with no connection to edges', 'The distance between the fragments and the nearest ocean'], 0),
   ('What conditions can differ at a habitats edge compared to its interior?', ['Light, wind, and predation conditions', 'Only the colour of the surrounding rock', 'Conditions identical in every way to the interior', 'A condition with no ecological relevance at all'], 0),
   ('What can the edge effect do to species adapted to interior habitat conditions?', ['Expose them to unfavourable conditions that can reduce biodiversity', 'Immediately improve their survival with no negative effect at all', 'Have no effect on interior species whatsoever', 'Guarantee an increase in their population size'], 0),
   ('Why can habitat fragmentation harm biodiversity even when the total habitat area is only modestly reduced?', ['A larger proportion of the remaining habitat becomes edge habitat, unsuitable for many interior species', 'Fragmentation always increases the amount of usable interior habitat', 'Total habitat area has no connection to species survival', 'Edge habitat is always identical in quality to interior habitat'], 0)]),
C('Chemistry: Boiling Point Elevation and Its Real-World Applications',
  'Grade 11 Chemistry strand: boiling point elevation occurs when dissolving a solute raises the boiling point of a solvent above its pure value, a colligative property that depends on the number of dissolved particles, which explains why adding salt to a pot of water raises the temperature at which it boils.',
  [('What happens to a solvents boiling point when a solute is dissolved in it?', ['The boiling point is raised above its pure value', 'The boiling point is always lowered below its pure value', 'The boiling point remains completely unchanged in every case', 'The solvent stops boiling entirely once a solute is added'], 0),
   ('What category of property is boiling point elevation classified as?', ['A colligative property', 'A property that depends only on solute identity', 'A property unrelated to the number of dissolved particles', 'A purely physical property with no chemical basis'], 0),
   ('What determines the size of the boiling point elevation for a given solvent?', ['The number of dissolved particles', 'The exact colour of the dissolved solute', 'The identity of the solute rather than particle count', 'A factor with no connection to the solute at all'], 0),
   ('What everyday example illustrates boiling point elevation?', ['Adding salt to a pot of water raises the temperature at which it boils', 'Adding salt to water always lowers its boiling point', 'Boiling water always occurs at exactly the same temperature regardless of what is dissolved in it', 'Salt has no measurable effect on the boiling point of water'], 0),
   ('How does boiling point elevation relate to other colligative properties such as freezing point depression?', ['Both depend on the number of dissolved particles in a solution, not their identity', 'Boiling point elevation and freezing point depression have no relationship to each other', 'Freezing point depression depends only on solute identity, unlike boiling point elevation', 'Colligative properties depend on particle identity rather than particle count'], 0)]),
]),
day(185, [
E('Writing: The Toast — A Short Speech of Celebration',
  'Grade 11 English strand: a toast is a brief, warm speech delivered to celebrate a person or occasion, typically opening with a short anecdote or observation, expressing genuine appreciation, and closing with a concise, memorable line that invites the audience to raise a glass together.',
  [('What is a toast?', ['A brief, warm speech delivered to celebrate a person or occasion', 'A lengthy, formal lecture on an academic subject', 'A written letter with no spoken component at all', 'A speech intended to criticize rather than celebrate its subject'], 0),
   ('What does a toast often open with?', ['A short anecdote or observation', 'A detailed legal disclaimer', 'A list of unrelated statistics', 'A lengthy historical timeline'], 0),
   ('What tone does a toast typically aim to express?', ['Genuine appreciation', 'Harsh criticism of the person being celebrated', 'Complete indifference to the occasion', 'A tone with no emotional content at all'], 0),
   ('How does a toast typically close?', ['With a concise, memorable line inviting the audience to raise a glass', 'With an extended argument on an unrelated topic', 'With no closing line of any kind', 'With a detailed critique of the occasion itself'], 0),
   ('Why does a toast benefit from being brief rather than long?', ['Its brevity keeps the celebratory moment focused and memorable for the audience', 'A toast is always more effective the longer it becomes', 'Length has no effect on how a toast is received', 'Toasts are required by convention to last at least ten minutes'], 0)]),
F('Discrete Math: Catalan Numbers and Counting Problems',
  'Grade 11 Functions strand: Catalan numbers form a sequence that counts a surprising range of combinatorial structures, from the number of ways to correctly match parentheses in an expression to the number of distinct ways to triangulate a polygon, making them a recurring pattern across seemingly unrelated counting problems.',
  [('What kind of sequence are Catalan numbers?', ['A sequence that counts a range of combinatorial structures', 'A sequence limited only to even numbers', 'A sequence with no connection to counting problems', 'A sequence that only ever produces the number one'], 0),
   ('Name one combinatorial structure that Catalan numbers can count.', ['The number of ways to correctly match parentheses in an expression', 'The number of days in a calendar year', 'The number of colours visible in a rainbow', 'A structure with no connection to combinatorics at all'], 0),
   ('What geometric counting problem can also be solved using Catalan numbers?', ['The number of distinct ways to triangulate a polygon', 'The exact area of a triangle', 'The circumference of a circle', 'A problem with no connection to polygons at all'], 0),
   ('What makes Catalan numbers notable across different counting problems?', ['They recur as a pattern across seemingly unrelated combinatorial problems', 'They apply to only a single, narrow counting problem', 'They have no mathematical pattern of any kind', 'They only ever apply to problems involving negative numbers'], 0),
   ('Why might a mathematician find it useful to recognize a Catalan number pattern in a new problem?', ['Recognizing the pattern connects the new problem to known counting results and formulas', 'Recognizing a Catalan pattern provides no useful mathematical information', 'Catalan numbers cannot be applied to any newly encountered problem', 'Catalan numbers only ever apply to problems already fully solved'], 0)]),
B('Microbiology: Protists — Diverse Life Strategies Beyond Animals, Plants, and Fungi',
  'Grade 11 Biology strand: protists are a highly diverse group of mostly single-celled eukaryotic organisms that do not fit neatly into the animal, plant, or fungus kingdoms, including photosynthetic algae, animal-like protozoa that actively hunt prey, and fungus-like slime moulds, reflecting a wide range of feeding and reproductive strategies.',
  [('What type of cell do most protists have?', ['A single eukaryotic cell', 'A single prokaryotic cell', 'Multiple cells with no nucleus at all', 'No cells of any kind'], 0),
   ('Why are protists considered difficult to classify?', ['They do not fit neatly into the animal, plant, or fungus kingdoms', 'They fit perfectly and exclusively into the animal kingdom', 'They fit perfectly and exclusively into the plant kingdom', 'They have no classification difficulties at all'], 0),
   ('Name one photosynthetic type of protist.', ['Algae', 'A bacterium with no chloroplasts', 'A vertebrate animal', 'A true fungus'], 0),
   ('What behaviour do animal-like protozoa often display?', ['Actively hunting prey', 'Photosynthesizing using chlorophyll', 'Forming a rigid cell wall identical to plants', 'Remaining completely immobile at all times'], 0),
   ('What does the wide range of protist feeding and reproductive strategies suggest about the group?', ['Protists represent an especially diverse category of life that resists simple classification', 'All protists behave in an identical way with no diversity at all', 'Protists share the exact same feeding strategy as every fungus', 'Protists have no reproductive strategies of any kind'], 0)]),
C('Chemistry: The Chemistry of Hand Warmers — Exothermic Crystallization Reactions',
  'Grade 11 Chemistry strand: a reusable hand warmer contains a supersaturated solution of sodium acetate that releases stored energy as heat when a small metal disc is flexed, triggering rapid crystallization, an exothermic process that can be reversed by boiling the pack to redissolve the crystals for reuse.',
  [('What solution does a reusable hand warmer typically contain?', ['A supersaturated solution of sodium acetate', 'A dilute solution of table salt', 'Pure distilled water with no solute at all', 'A solution containing no dissolved substance whatsoever'], 0),
   ('What triggers the crystallization inside a reusable hand warmer?', ['Flexing a small metal disc', 'Exposing the pack to sunlight', 'Freezing the pack in a refrigerator', 'Adding fresh water to the pack'], 0),
   ('What type of process is the crystallization reaction in a hand warmer?', ['An exothermic process that releases heat', 'An endothermic process that absorbs heat', 'A process that releases no energy at all', 'A purely physical process with no energy change'], 0),
   ('What does supersaturated mean in the context of the hand warmer solution?', ['It holds more dissolved solute than a normal saturated solution would at that temperature', 'It contains no dissolved solute of any kind', 'It is diluted far below its normal saturation point', 'It refers to a solution that has completely evaporated'], 0),
   ('How can a used hand warmer be prepared for reuse?', ['By boiling the pack to redissolve the crystals back into solution', 'By freezing the pack until the crystals disappear', 'A used hand warmer can never be reused under any circumstance', 'By exposing the pack to open flame until it melts completely'], 0)]),
]),
day(186, [
E('Media Literacy: Content Moderation and the Ethics of Platform Policy',
  'Grade 11 English strand: content moderation refers to the policies and processes an online platform uses to review, restrict, or remove user-generated material, raising ongoing ethical tensions between protecting users from harmful content and preserving open expression, especially when moderation decisions are inconsistent or applied without clear explanation.',
  [('What does content moderation refer to?', ['The policies and processes a platform uses to review, restrict, or remove user content', 'A process with no connection to online platforms at all', 'A method used only to promote content, never to restrict it', 'A legal requirement that forbids any review of user content'], 0),
   ('What ethical tension does content moderation often raise?', ['The tension between protecting users from harmful content and preserving open expression', 'A tension with no connection to ethics at all', 'A tension that only concerns advertising revenue', 'A tension between two unrelated technical systems'], 0),
   ('What can make moderation decisions especially controversial?', ['When they are inconsistent or applied without clear explanation', 'When they are applied with perfect consistency and full transparency', 'Moderation decisions are never controversial under any circumstance', 'When a platform removes no content whatsoever'], 0),
   ('What kind of material does content moderation typically review?', ['User-generated material', 'Only material created by the platform itself', 'Material with no connection to any platform user', 'Printed material with no digital component'], 0),
   ('Why might inconsistent content moderation undermine user trust in a platform?', ['Unclear or uneven enforcement makes it hard for users to know what is actually allowed', 'Inconsistent moderation always increases user trust automatically', 'Moderation policy has no effect on how users perceive a platform', 'Clear and consistent moderation is impossible on any platform'], 0)]),
F('Trigonometry: Polar Coordinates and Conversion to Rectangular Form',
  'Grade 11 Functions strand: polar coordinates locate a point using a distance from a fixed origin and an angle from a fixed direction rather than horizontal and vertical distances, and converting between polar and rectangular form uses sine and cosine to translate that distance-and-angle description into the more familiar x and y coordinates.',
  [('What two values locate a point in polar coordinates?', ['A distance from a fixed origin and an angle from a fixed direction', 'Only a horizontal distance, with no angle involved', 'Only a vertical distance, with no angle involved', 'Two unrelated angles with no reference to distance'], 0),
   ('What do polar coordinates use instead of horizontal and vertical distances?', ['A distance and an angle', 'Two unrelated horizontal distances', 'A single unlabelled number with no direction', 'A colour code representing location'], 0),
   ('What trigonometric functions are used to convert polar coordinates into rectangular form?', ['Sine and cosine', 'Only the tangent function, with no other function involved', 'Logarithmic functions exclusively', 'Functions with no connection to trigonometry at all'], 0),
   ('What coordinate system is considered more familiar when converting from polar form?', ['Rectangular, or x and y, coordinates', 'A coordinate system with no defined axes', 'A purely angular system with no distance component', 'A coordinate system limited to a single dimension'], 0),
   ('Why might polar coordinates be more convenient than rectangular coordinates for describing certain curves?', ['Curves with rotational symmetry can often be described more simply using distance and angle', 'Polar coordinates can never describe any curve accurately', 'Rectangular coordinates always describe every curve more simply than polar coordinates', 'Polar coordinates have no practical use in describing curves'], 0)]),
B('Biology: Vitamins and Coenzymes in Metabolic Pathways',
  'Grade 11 Biology strand: many vitamins function as coenzymes or coenzyme precursors, small molecules that bind to enzymes and are essential for the enzymes catalytic activity, so that a deficiency in even one vitamin can disrupt a specific metabolic pathway and produce a defined set of symptoms throughout the body.',
  [('What role do many vitamins play in metabolic pathways?', ['They function as coenzymes or coenzyme precursors', 'They function only as structural components of bone', 'They have no connection to enzyme activity at all', 'They act exclusively as a source of stored energy'], 0),
   ('What does a coenzyme typically bind to in order to function?', ['An enzyme', 'A single unrelated water molecule', 'A structural protein with no catalytic role', 'A cell membrane with no enzymatic activity'], 0),
   ('Why are coenzymes considered essential to many metabolic reactions?', ['They are necessary for the enzymes catalytic activity', 'They actively prevent enzymes from catalyzing any reaction', 'They have no measurable effect on enzyme activity', 'They replace the enzyme entirely during the reaction'], 0),
   ('What can happen if the body is deficient in a specific vitamin that acts as a coenzyme?', ['A specific metabolic pathway can be disrupted, producing a defined set of symptoms', 'Every metabolic pathway in the body improves as a result', 'Vitamin deficiency has no effect on any metabolic pathway', 'The enzyme continues to function with no change whatsoever'], 0),
   ('Why might different vitamin deficiencies produce very different sets of symptoms?', ['Each vitamin-dependent coenzyme supports a distinct metabolic pathway with its own function', 'All vitamins support the exact same single metabolic pathway', 'Vitamin deficiencies never produce any distinguishable symptoms', 'Coenzymes have an identical function regardless of which vitamin they come from'], 0)]),
C('Chemistry: Silica Gel and Desiccants — Adsorption versus Absorption',
  'Grade 11 Chemistry strand: silica gel is a porous desiccant that removes moisture from the air through adsorption, in which water molecules stick to the vast internal surface area of its microscopic pores, a process distinct from absorption, in which a substance is taken up into the bulk volume of another material.',
  [('What is silica gel commonly used for?', ['Removing moisture from the air as a desiccant', 'Adding moisture to dry air', 'Producing a strong chemical odour', 'Conducting electricity in a circuit'], 0),
   ('What process allows silica gel to capture water molecules?', ['Adsorption', 'Sublimation', 'Combustion', 'A process with no connection to moisture at all'], 0),
   ('Where do water molecules attach during adsorption by silica gel?', ['The vast internal surface area of its microscopic pores', 'The exact centre of each individual silica gel bead', 'A location entirely outside the silica gel structure', 'A surface that repels water molecules completely'], 0),
   ('How does adsorption differ from absorption?', ['Adsorption involves molecules sticking to a surface, while absorption takes a substance into the bulk volume of a material', 'Adsorption and absorption describe exactly the same physical process', 'Absorption always occurs only at a materials surface, never within its volume', 'Adsorption always involves a substance dissolving completely into a liquid'], 0),
   ('Why is a large internal surface area important for a desiccant like silica gel?', ['A larger surface area provides more sites for water molecules to adsorb, increasing moisture capacity', 'Surface area has no effect on how much moisture a desiccant can capture', 'A smaller surface area always increases a desiccants moisture capacity', 'Silica gel captures moisture with no relationship to its surface area at all'], 0)]),
]),
day(187, [
E('English Review: Pastoral Poetry, Sentence Fragments, the Epic, the Comedy of Manners, and the Toast',
  'Grade 11 English strand review: students revisit the pastoral tradition, sentence fragments and run-ons, the epic, the comedy of manners, and the toast as a short celebratory speech, closing out the full 187-day Grade 11 English strand.',
  [('What does pastoral poetry typically idealize?', ['Rural life and the natural landscape', 'The chaos of a crowded courtroom', 'The stress of urban and courtly life', 'A setting with no connection to nature at all'], 0),
   ('What does a sentence fragment lack?', ['A complete subject-verb combination or a complete thought', 'Any punctuation whatsoever', 'A title at the start of the sentence', 'A minimum of ten words'], 0),
   ('What kind of narrative is an epic?', ['A long narrative poem following a hero of great cultural significance', 'A short lyric poem about a single private emotion', 'A brief riddle with no narrative content', 'A poem with no central character of any kind'], 0),
   ('What does a comedy of manners satirize?', ['The behaviour and pretensions of a particular social class', 'A tragic historical event with no comedic elements', 'A setting with no connection to any social class', 'A purely private, solitary experience with no social dimension'], 0),
   ('What is a toast?', ['A brief, warm speech delivered to celebrate a person or occasion', 'A lengthy, formal lecture on an academic subject', 'A written letter with no spoken component at all', 'A speech intended to criticize rather than celebrate its subject'], 0)]),
F('Functions Review: Integrals, the Sieve of Eratosthenes, Simpsons Paradox, Plane Geometry, and the Toast to Grade 11 Functions',
  'Grade 11 Functions strand review: students revisit definite integrals, the Sieve of Eratosthenes, Simpsons paradox, the distance from a point to a plane, and Catalan numbers, closing out the full 187-day Grade 11 Functions strand.',
  [('What does a definite integral calculate?', ['The exact accumulated area between a curve and the horizontal axis', 'The slope of a curve at a single point', 'The number of times a curve crosses the vertical axis', 'A quantity with no connection to area at all'], 0),
   ('What does the Sieve of Eratosthenes generate?', ['All prime numbers up to a given limit', 'Only the multiples of ten within a range', 'A single randomly chosen prime number', 'A list with no connection to prime numbers at all'], 0),
   ('What is Simpsons paradox?', ['A trend appearing in separate groups that reverses once the groups are combined', 'A trend that always stays identical whether data is grouped or combined', 'A paradox with no connection to statistics at all', 'A rule stating that combined data is always more accurate than grouped data'], 0),
   ('What is being calculated when finding the distance from a point to a plane?', ['The shortest, perpendicular distance between the point and the plane', 'The longest possible path between the point and the plane', 'A distance measured only along the plane itself', 'A quantity with no connection to distance at all'], 0),
   ('What kind of sequence are Catalan numbers?', ['A sequence that counts a range of combinatorial structures', 'A sequence limited only to even numbers', 'A sequence with no connection to counting problems', 'A sequence that only ever produces the number one'], 0)]),
B('Biology Review: Karyotyping, Allergies, Seed Dispersal, Habitat Fragmentation, and Protists',
  'Grade 11 Biology strand review: students revisit karyotyping, allergies and hypersensitivity, plant seed dispersal, edge effects and habitat fragmentation, and protists, closing out the full 187-day Grade 11 Biology strand.',
  [('What is a karyotype?', ['An organized image of an individuals complete set of chromosomes', 'A single strand of unpaired DNA', 'A photograph of a whole living cell', 'An image with no connection to chromosomes at all'], 0),
   ('What is an allergy?', ['A hypersensitive immune response to a normally harmless substance', 'A response in which the immune system never reacts to anything', 'A condition with no connection to the immune system at all', 'A permanent absence of any immune activity'], 0),
   ('What is one strategy plants use to disperse seeds by wind?', ['Lightweight winged or feathery seeds', 'Seeds that are extremely dense and heavy', 'Seeds that dissolve completely before they can travel', 'Seeds with no adaptation for movement of any kind'], 0),
   ('What does habitat fragmentation do to a large, continuous habitat?', ['Breaks it into smaller, isolated patches', 'Expands it into an even larger continuous area', 'Leaves it completely unchanged in every way', 'Converts it entirely into open ocean'], 0),
   ('What type of cell do most protists have?', ['A single eukaryotic cell', 'A single prokaryotic cell', 'Multiple cells with no nucleus at all', 'No cells of any kind'], 0)]),
C('Chemistry Review: Effusion, Net Ionic Equations, Significant Figures, Boiling Point Elevation, and Hand Warmers',
  'Grade 11 Chemistry strand review: students revisit Grahams law of effusion, net ionic equations, significant figures, boiling point elevation, and the exothermic chemistry of hand warmers, closing out the full 187-day Grade 11 Chemistry strand and this Grade 11 curriculum build.',
  [('What does Grahams law describe?', ['The rate at which a gas effuses through a tiny opening', 'The exact colour of a gas sample', 'The boiling point of a liquid', 'A quantity with no connection to gases at all'], 0),
   ('What does a net ionic equation show?', ['Only the ions and molecules that actually participate in a chemical change', 'Every single ion present in the solution, whether or not it reacts', 'A full molecular equation with no ions removed', 'A description with no connection to a chemical reaction'], 0),
   ('What do significant figures represent in a measurement?', ['The digits that carry meaningful information about its precision', 'Every digit in a number regardless of its meaning', 'Only the first digit of any measured value', 'A quantity with no connection to precision at all'], 0),
   ('What happens to a solvents boiling point when a solute is dissolved in it?', ['The boiling point is raised above its pure value', 'The boiling point is always lowered below its pure value', 'The boiling point remains completely unchanged in every case', 'The solvent stops boiling entirely once a solute is added'], 0),
   ('What solution does a reusable hand warmer typically contain?', ['A supersaturated solution of sodium acetate', 'A dilute solution of table salt', 'Pure distilled water with no solute at all', 'A solution containing no dissolved substance whatsoever'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_181_187)
    append_to(11, g11_181_187)
