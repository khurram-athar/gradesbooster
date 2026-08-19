#!/usr/bin/env python3
"""Grade 10, Days 181-187 -- extends Grade 10 from 180 to 187 days. This is
the FINAL batch for Grade 10: 180 + 7 = 187, completing the full-year
187-day Ontario curriculum target for this grade. Structured as six new
content days (181-186, one new topic per subject per day) plus Day 187 as
a final cross-subject review day.

New topics introduced in this batch, chosen after dumping and grepping the
full existing Day 1-180 (subject, title) list from data/grade10.json (via
`python3 -c "import json; d=json.load(open('data/grade10.json'));
[print(s['subject'],'::',s['title']) for day in d for s in day['subjects']]"`)
and targeted keyword searches to avoid overlap:

English -- analyzing flashback and nonlinear timelines, the letter to the
editor, split infinitives and usage debates, analyzing documentary film
techniques, the panel discussion and moderation, and the mock-epic and
satirical verse.

Math -- Goldbachs Conjecture, linear approximation and differentials, loci
and locus problems, solving systems using matrices and Gaussian
elimination, the Traveling Salesman Problem, and z-scores and standardized
values.

Science -- terminal velocity and air resistance (physics), food
preservation and the chemistry of spoilage (chemistry), tides and the
physics of ocean tides (earth science), decomposers and nutrient cycling
(biology), friction and traction in everyday motion (physics), and the
chemistry of rust prevention and metal coatings (chemistry).

History -- Trudeaumania and the 1968 federal election, the Just Society
and Trudeaus early political vision, Canadas adoption of the metric
system in the 1970s, the Immigration Act of 1976 and the points system,
the patriation of the Constitution in 1982, and the Progressive
Conservative landslide of 1984 under Brian Mulroney -- continuing directly
from Expo 67 (1967), which closed Days 171-180, into the Trudeau and
Mulroney eras of Canadian federal politics.

None of the twenty-four new subject titles above, nor the four Day 187
review titles, duplicate any (subject, title) pair found in Days 1-180 --
confirmed by dumping the full existing title list and running targeted
substring/keyword checks (including near-match checks, not just exact
matches) before writing this script. The known pre-existing duplicate
History title "The October Crisis and the War Measures Act" (occurring
twice in Days 1-160) predates this batch and is left untouched; no third
occurrence is added, and no new duplicate is introduced anywhere in this
batch.

Day 187 is the final cross-subject review day of the entire 187-day
Grade 10 curriculum build. Its four review titles ("English Review: The
Final Review -- ...", "Math Review: The Final Review -- ...", "Science
Review: The Final Review -- ...", "History Review: The Final Review --
...") are textually distinct from every earlier review day title in the
file, and each summary explicitly notes that it is the concluding review
of the full Grade 10 course, since this is the capstone day of the whole
K-12 curriculum build for this grade -- while still following the exact
mechanical review-day format (subject-strand summary plus a five-question
quiz drawing on the days it reviews) used in every prior review batch.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
apostrophe or double-quote characters are used anywhere in
title/question/summary/option text -- apostrophes are dropped entirely,
matching the Days 111-180 convention (e.g. "Trudeaus", "Canadas",
"Goldbachs", "governments").
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


g10_181_187 = [
day(181, [
E('Reading: Analyzing Flashback and Nonlinear Timelines',
  'Grade 10 English strand: a flashback interrupts the chronological order of a narrative to show an earlier event, and writers use flashbacks and other nonlinear timelines to reveal backstory, build suspense, or highlight a connection between past and present without following strict chronological order.',
  [('What does a flashback do within a narrative?', ['Interrupts the chronological order to show an earlier event', 'Predicts an event that has not yet happened', 'Repeats the current scene word for word', 'Removes all characters from the story'], 0),
   ('What is one reason a writer might use a flashback?', ['To reveal backstory or build suspense', 'To make the timeline impossible to follow', 'To remove the need for a plot', 'To end the story before it begins'], 0),
   ('What term describes a narrative structure that does not follow strict chronological order?', ['A nonlinear timeline', 'A completely linear timeline', 'A single unbroken timeline with no gaps', 'A timeline with only future events'], 0),
   ('What might a flashback highlight about the relationship between past and present events?', ['A meaningful connection between them', 'That the two time periods are entirely unrelated', 'That the present has no bearing on the story', 'That the past can never influence a character'], 0),
   ('Why might a nonlinear timeline challenge a reader more than a strictly chronological one?', ['The reader must piece together the order of events rather than following them in sequence', 'Nonlinear timelines always confuse readers with no purpose', 'A nonlinear timeline removes every character from the plot', 'Nonlinear timelines cannot include any flashback'], 0)]),
M('Number Theory: Goldbachs Conjecture',
  'Grade 10 Math strand: Goldbachs Conjecture proposes that every even integer greater than two can be written as the sum of two prime numbers, a statement that has been verified for an enormous range of numbers through computation yet still has no formal mathematical proof.',
  [('What does Goldbachs Conjecture propose?', ['That every even integer greater than two can be written as the sum of two prime numbers', 'That every odd integer is automatically prime', 'That no even number can ever be divided evenly', 'That prime numbers do not exist beyond one hundred'], 0),
   ('What has happened to Goldbachs Conjecture despite extensive testing?', ['It has been verified for an enormous range of numbers but never formally proven', 'It has been formally proven for all numbers', 'It has been completely disproven', 'It has never been tested for any number'], 0),
   ('Which pair of primes could demonstrate Goldbachs Conjecture for the number 10?', ['5 and 5, or 3 and 7', '4 and 6', '1 and 9', '10 and 0'], 0),
   ('Why is Goldbachs Conjecture still considered a conjecture rather than a theorem?', ['No general mathematical proof covering all even numbers has yet been found', 'It has already been proven false', 'It applies only to negative numbers', 'It was proven true in the eighteenth century'], 0),
   ('What type of number does Goldbachs Conjecture say every even integer greater than two can be expressed as the sum of?', ['Two prime numbers', 'Two even numbers only', 'Two negative numbers', 'Two irrational numbers'], 0)]),
Sc('Physics: Terminal Velocity and Air Resistance',
   'Grade 10 Science strand: terminal velocity is the constant maximum speed a falling object reaches once the upward force of air resistance grows large enough to balance the downward force of gravity, after which the object stops accelerating and falls at a steady rate.',
   [('What is terminal velocity?', ['The constant maximum speed a falling object reaches when air resistance balances gravity', 'The speed of an object the instant it is released', 'The speed of an object with no air resistance acting on it', 'The speed at which an object accelerates forever without limit'], 0),
    ('What happens to an objects acceleration once it reaches terminal velocity?', ['The acceleration becomes zero and the object falls at a constant speed', 'The acceleration increases without limit', 'The object begins to move upward', 'The object instantly stops moving entirely'], 0),
    ('What two forces balance each other at terminal velocity?', ['Gravity and air resistance', 'Friction and magnetism', 'Buoyancy and tension', 'Electric force and gravity'], 0),
    ('How does the surface area of a falling object affect its terminal velocity?', ['A larger surface area generally increases air resistance and lowers terminal velocity', 'Surface area has no effect on air resistance whatsoever', 'A larger surface area always increases terminal velocity', 'Terminal velocity depends only on colour, not surface area'], 0),
    ('Why does a skydiver reach a slower terminal velocity when their parachute opens?', ['The parachute greatly increases air resistance acting against gravity', 'The parachute removes gravity entirely', 'The parachute increases the skydivers mass', 'The parachute eliminates all air resistance'], 0)]),
H('Trudeaumania and the 1968 Federal Election',
  'Grade 10 History strand: Trudeaumania describes the wave of enthusiasm surrounding Pierre Trudeau during the 1968 federal election, which the Liberals won decisively behind his charisma, media appeal, and vision of a Just Society, ushering in a new era of Canadian federal politics.',
  [('What does the term Trudeaumania describe?', ['The wave of public enthusiasm surrounding Pierre Trudeau during the 1968 election', 'A federal law passed in 1968', 'A treaty signed between Canada and France', 'A new Canadian currency introduced in 1968'], 0),
   ('Which party won the 1968 federal election?', ['The Liberal Party, led by Pierre Trudeau', 'The Progressive Conservatives, led by John Diefenbaker', 'The Co-operative Commonwealth Federation', 'The Social Credit Party'], 0),
   ('What personal qualities were often credited with fueling Trudeaumania?', ['Charisma and strong media appeal', 'A total avoidance of public appearances', 'A complete lack of any political vision', 'An exclusively written campaign with no public events'], 0),
   ('What vision did Trudeau associate with his political platform around this period?', ['The Just Society', 'The National Policy', 'The White Paper', 'The Meech Lake Accord'], 0),
   ('What broader shift did the 1968 election help usher in for Canadian federal politics?', ['A new era shaped by Trudeaus leadership and political style', 'The permanent end of the Liberal Party', 'A return to nineteenth-century political parties', 'The abolition of federal elections'], 0)]),
]),
day(182, [
E('Writing: The Letter to the Editor',
  'Grade 10 English strand: a letter to the editor is a piece of persuasive writing submitted to a newspaper or publication in response to a current issue or a previously published article, using a clear argument, supporting evidence, and a respectful but urgent tone to influence public opinion.',
  [('What is a letter to the editor?', ['A piece of persuasive writing submitted to a newspaper or publication in response to a current issue', 'A private letter never intended for publication', 'A recipe published in a cooking magazine', 'A weather report with no argument'], 0),
   ('What tone does an effective letter to the editor typically use?', ['A respectful but urgent tone', 'A tone with no clear opinion at all', 'An entirely comedic tone with no argument', 'A tone that avoids addressing the issue'], 0),
   ('What might a letter to the editor respond to?', ['A current issue or a previously published article', 'A private conversation with no public relevance', 'A math equation with no connection to current events', 'A recipe with no argument'], 0),
   ('What helps make a letter to the editor persuasive?', ['A clear argument supported by evidence', 'A complete absence of any opinion', 'Random unrelated facts with no connection to the issue', 'Ignoring the topic entirely'], 0),
   ('Why might a reader write a letter to the editor rather than simply discussing an issue privately?', ['To influence public opinion by reaching a wider audience through publication', 'Because private discussion always reaches more people', 'Because letters to the editor are never read by anyone', 'To avoid taking any position on the issue'], 0)]),
M('Calculus: Linear Approximation and Differentials',
  'Grade 10 Math strand: linear approximation uses the tangent line at a known point on a function to estimate the value of the function at a nearby point, with the differential representing the small change in the linear approximation that corresponds to a small change in the input.',
  [('What does linear approximation use to estimate a functions value near a known point?', ['The tangent line at that known point', 'A completely unrelated function', 'The area under the entire curve', 'A random guess with no mathematical basis'], 0),
   ('What does the differential represent in linear approximation?', ['The small change in the linear approximation corresponding to a small change in input', 'The exact value of the function at every point', 'The total area under the curve', 'The maximum value a function can ever reach'], 0),
   ('Why is linear approximation generally most accurate close to the known point?', ['The tangent line closely matches the curve only near the point of tangency', 'Tangent lines are always identical to the curve everywhere', 'Linear approximation is equally accurate at any distance from the point', 'Linear approximation ignores the shape of the curve entirely'], 0),
   ('What information is needed to construct a linear approximation of a function at a point?', ['The function value and its derivative at that point', 'Only the y-intercept of the graph', 'The area under the curve across its entire domain', 'The second derivative at every point on the curve'], 0),
   ('In what type of real-world situation might linear approximation be useful?', ['Estimating a small change in output resulting from a small change in input', 'Calculating the exact value of a function infinitely far from a known point', 'Finding the colour of a graphed function', 'Measuring a quantity with no relationship to calculus'], 0)]),
Sc('Chemistry: Food Preservation and the Chemistry of Spoilage',
   'Grade 10 Science strand: food spoilage occurs when microorganisms and chemical reactions such as oxidation break down the compounds in food, and preservation methods including refrigeration, drying, canning, and the addition of salt or acid work by slowing microbial growth or altering the chemical conditions food needs to spoil.',
   [('What commonly causes food spoilage?', ['Microorganisms and chemical reactions such as oxidation', 'A complete absence of any chemical activity', 'Food becoming instantly sterile with no further change', 'The total removal of all bacteria with no other cause'], 0),
    ('How does refrigeration help preserve food?', ['It slows the growth rate of microorganisms that cause spoilage', 'It instantly destroys all chemical reactions in food', 'It increases the rate of microbial growth', 'It has no effect on microorganisms at all'], 0),
    ('How can adding salt help preserve food?', ['It draws water out of microbial cells, slowing their growth', 'It always speeds up spoilage', 'It has no chemical effect on food', 'It removes all nutrients from the food'], 0),
    ('What role can acid play in food preservation, such as in pickling?', ['It creates conditions that many spoilage microorganisms cannot easily survive in', 'It has no effect on the growth of microorganisms', 'It always accelerates spoilage', 'It removes the need for any other preservation method'], 0),
    ('Why does drying food help prevent spoilage?', ['Removing moisture limits the water microorganisms need to grow', 'Drying always increases the moisture content of food', 'Microorganisms grow faster in dry conditions than in moist ones', 'Drying has no effect on microbial growth'], 0)]),
H('The Just Society: Trudeaus Political Vision',
  'Grade 10 History strand: the Just Society was the guiding political vision Pierre Trudeau promoted throughout his early years as prime minister, emphasizing individual rights, bilingualism, and greater social and economic equality as central goals for federal policy in Canada.',
  [('What was the Just Society?', ['The guiding political vision Pierre Trudeau promoted as prime minister', 'A treaty signed between Canada and Britain', 'A federal department created in 1968', 'A new Canadian province'], 0),
   ('Which values did the Just Society emphasize?', ['Individual rights, bilingualism, and greater social and economic equality', 'Complete isolation from international affairs', 'The abolition of all federal programs', 'A return to nineteenth-century policies'], 0),
   ('Who is most closely associated with promoting the idea of the Just Society?', ['Pierre Trudeau', 'John Diefenbaker', 'Lester Pearson', 'Louis St. Laurent'], 0),
   ('During which period did the Just Society serve as a guiding political vision?', ['Trudeaus early years as prime minister, beginning in the late 1960s', 'The 1867 Confederation debates', 'The Second World War', 'The 1867-1900 period of Canadian settlement'], 0),
   ('How did the Just Society relate to federal policy goals of the period?', ['It set out central goals for federal policy such as expanding rights and equality', 'It called for the complete elimination of federal government', 'It focused exclusively on foreign trade agreements', 'It had no connection to any federal policy'], 0)]),
]),
day(183, [
E('Grammar: Split Infinitives and Usage Debates',
  'Grade 10 English strand: a split infinitive occurs when a word, usually an adverb, is placed between the word to and the verb that follows it, as in to boldly go, a construction once widely considered incorrect but now generally accepted in modern usage when it improves clarity or emphasis.',
  [('What is a split infinitive?', ['A construction where a word is placed between to and the verb that follows it', 'A sentence with no verb at all', 'A sentence that begins with a question word', 'A verb with two different subjects'], 0),
   ('Which of the following is an example of a split infinitive?', ['To boldly go', 'To go boldly forward', 'Boldly to go now', 'Going to boldly'], 0),
   ('How was the split infinitive traditionally viewed by many grammar guides?', ['As an incorrect or awkward construction to be avoided', 'As the only correct way to form an infinitive', 'As a construction found only in poetry', 'As a rule with no historical basis whatsoever'], 0),
   ('How is the split infinitive generally viewed in modern usage?', ['As generally acceptable, especially when it improves clarity or emphasis', 'As always grammatically incorrect with no exception', 'As a construction that no longer exists in English', 'As acceptable only in legal documents'], 0),
   ('Why might a writer choose to split an infinitive deliberately?', ['To place emphasis on the adverb or to avoid an awkward sentence structure', 'To make a sentence impossible to understand', 'Because split infinitives always weaken a sentence', 'Because English grammar requires every infinitive to be split'], 0)]),
M('Geometry: Loci and Locus Problems',
  'Grade 10 Math strand: a locus is the set of all points that satisfy a given geometric condition, such as a fixed distance from a point or an equal distance from two points, and locus problems ask students to describe or sketch the shape formed by all such points.',
  [('What is a locus in geometry?', ['The set of all points that satisfy a given geometric condition', 'A single fixed point with no other points nearby', 'A line with an undefined length', 'A shape with no defined boundary at all'], 0),
   ('What shape is formed by the locus of points a fixed distance from a single given point?', ['A circle', 'A straight line', 'A square', 'A single point'], 0),
   ('What shape is formed by the locus of points equidistant from two fixed points?', ['The perpendicular bisector of the segment joining the two points', 'A circle centred on one of the two points', 'A single point exactly halfway between them with no other points included', 'A triangle connecting the two points'], 0),
   ('What does a locus problem typically ask a student to do?', ['Describe or sketch the shape formed by all points satisfying a given condition', 'Calculate the exact area of an unrelated triangle', 'Solve an equation with no geometric meaning', 'List every integer between two numbers'], 0),
   ('Which real-world application might rely on locus reasoning?', ['Determining the safe zone equidistant from two transmission towers', 'Calculating the derivative of a polynomial function', 'Balancing a chemical equation', 'Converting a decimal to a percentage'], 0)]),
Sc('Earth Science: Tides and the Physics of Ocean Tides',
   'Grade 10 Science strand: ocean tides are the periodic rise and fall of sea level caused primarily by the gravitational pull of the moon and, to a lesser extent, the sun, producing predictable high and low tide cycles that vary with the relative positions of the Earth, moon, and sun.',
   [('What primarily causes ocean tides?', ['The gravitational pull of the moon and, to a lesser extent, the sun', 'Wind blowing across the surface of the ocean', 'Volcanic activity beneath the ocean floor', 'Changes in ocean water temperature alone'], 0),
    ('What pattern do ocean tides generally follow?', ['A predictable periodic rise and fall of sea level', 'A completely random and unpredictable pattern', 'A single rise with no corresponding fall', 'A pattern that never repeats'], 0),
    ('What produces especially strong tides known as spring tides?', ['An alignment of the sun, Earth, and moon that combines their gravitational effects', 'The arrival of the spring season each year', 'A sudden drop in ocean temperature', 'The complete absence of any gravitational pull'], 0),
    ('What term describes the weaker tides that occur when the sun and moon are at right angles relative to Earth?', ['Neap tides', 'Spring tides', 'King tides', 'Storm tides'], 0),
    ('Why is the moons gravitational pull more influential on tides than the suns, despite the suns much greater mass?', ['The moon is far closer to Earth, which increases its tidal influence', 'The sun has no gravitational pull at all', 'The moon is more massive than the sun', 'Distance has no effect on gravitational influence'], 0)]),
H('Canadas Adoption of the Metric System in the 1970s',
  'Grade 10 History strand: in the 1970s the federal government began converting Canada from imperial to metric measurement in weather reporting, road signs, and consumer goods, a gradual process intended to align Canadian trade and daily life with the metric standard used by most of the world.',
  [('What change did the federal government begin implementing in the 1970s?', ['Converting Canada from imperial to metric measurement', 'Replacing the Canadian dollar with a new currency', 'Abolishing all provincial governments', 'Ending federal elections'], 0),
   ('In which areas of daily life was the metric conversion first introduced?', ['Weather reporting, road signs, and consumer goods', 'Only in scientific laboratories with no public application', 'Only in federal court proceedings', 'Only in international treaties'], 0),
   ('Why did the federal government pursue metric conversion?', ['To align Canadian trade and daily life with the metric standard used by most of the world', 'To make measurement more difficult for Canadians', 'To copy a system used only by one other country', 'To eliminate the need for any measurement system'], 0),
   ('How would the transition to the metric system in Canada best be described?', ['A gradual process introduced over time', 'An instantaneous change completed in a single day', 'A process that was never actually implemented', 'A change reversed within one year'], 0),
   ('What measurement system did Canada primarily use before the metric conversion?', ['The imperial system', 'The metric system', 'A system unique to Canada with no international counterpart', 'No standardized measurement system at all'], 0)]),
]),
day(184, [
E('Media Literacy: Analyzing Documentary Film Techniques',
  'Grade 10 English strand: documentary filmmakers use techniques such as archival footage, expert interviews, voice-over narration, and selective editing to present factual subject matter persuasively, meaning viewers must think critically about whose perspective a documentary emphasizes and what it leaves out.',
  [('Which technique might a documentary filmmaker use to present factual subject matter?', ['Archival footage, expert interviews, and voice-over narration', 'A completely fictional plot with no factual basis', 'A script written entirely in verse', 'An animated sequence with no connection to reality'], 0),
   ('Why might a viewer need to think critically when watching a documentary?', ['Documentaries can emphasize a particular perspective and leave out other information', 'Documentaries always present every possible perspective equally', 'Documentaries never involve any editing choices', 'Documentary filmmakers cannot select which footage to include'], 0),
   ('What is the purpose of voice-over narration in many documentaries?', ['To guide viewers through the subject matter and provide context', 'To remove all information from the film', 'To replace every visual image with silence', 'To prevent the audience from understanding the topic'], 0),
   ('How can selective editing shape a viewers understanding of a documentary subject?', ['By determining which footage and interviews are included or left out', 'Editing has no effect on how a documentary is understood', 'Selective editing always presents a fully neutral account', 'Editing only affects the length of a film, not its meaning'], 0),
   ('Why might expert interviews be included in a documentary?', ['To lend credibility and provide informed perspective on the subject', 'To confuse viewers with unrelated information', 'To remove any factual basis from the film', 'Because documentaries are required to include no spoken interviews'], 0)]),
M('Algebra: Solving Systems Using Matrices and Gaussian Elimination',
  'Grade 10 Math strand: a system of linear equations can be represented as a matrix, and Gaussian elimination is a systematic method of using row operations to transform that matrix into a simpler form from which the solution to the system can be read directly.',
  [('How can a system of linear equations be represented for use with Gaussian elimination?', ['As a matrix', 'As a single unrelated number', 'As a circle graph', 'As a single word problem with no numerical structure'], 0),
   ('What is Gaussian elimination?', ['A systematic method of using row operations to simplify a matrix and solve a system', 'A method for finding the area of a triangle', 'A method for graphing a single point', 'A method with no connection to systems of equations'], 0),
   ('What is the goal of applying row operations during Gaussian elimination?', ['To transform the matrix into a simpler form from which the solution can be read', 'To make the matrix impossible to solve', 'To remove all numbers from the matrix', 'To convert the matrix into a single unrelated equation'], 0),
   ('Which of the following is an example of a row operation used in Gaussian elimination?', ['Adding a multiple of one row to another row', 'Deleting every row from the matrix', 'Replacing all numbers in the matrix with zero', 'Converting the matrix into a word problem'], 0),
   ('Why is Gaussian elimination useful for systems with more than two variables?', ['It provides an organized, systematic approach that scales to larger systems', 'It only works for systems with exactly one variable', 'It cannot be applied to any system with more than one equation', 'It eliminates the need to ever solve for a variable'], 0)]),
Sc('Biology: Decomposers and Nutrient Cycling in Ecosystems',
   'Grade 10 Science strand: decomposers such as fungi and bacteria break down dead organisms and waste material into simpler substances, releasing nutrients back into the soil and water so they can be reused by other living things, making decomposers essential to nutrient cycling within an ecosystem.',
   [('What role do decomposers play in an ecosystem?', ['They break down dead organisms and waste into simpler substances', 'They produce all of the oxygen in an ecosystem', 'They consume only living plants and animals', 'They prevent any nutrients from returning to the soil'], 0),
    ('Which organisms are common examples of decomposers?', ['Fungi and bacteria', 'Only large mammals', 'Only birds of prey', 'Only photosynthetic plants'], 0),
    ('What happens to nutrients once decomposers break down dead material?', ['They are released back into the soil and water for reuse', 'They are permanently destroyed and lost from the ecosystem', 'They are converted directly into oxygen gas', 'They remain locked inside the decomposer forever'], 0),
    ('Why are decomposers considered essential to nutrient cycling?', ['They allow nutrients from dead organisms to be reused by other living things', 'They remove all nutrients from an ecosystem permanently', 'They have no effect on the availability of nutrients', 'They only cycle nutrients within their own bodies'], 0),
    ('What might happen to an ecosystem if decomposers were removed entirely?', ['Dead material would accumulate and nutrients would not be efficiently recycled', 'Nothing would change in the ecosystem', 'All nutrients would instantly double in quantity', 'Every organism in the ecosystem would immediately become a decomposer'], 0)]),
H('The Immigration Act of 1976 and the Points System',
  'Grade 10 History strand: the Immigration Act of 1976 established a legal framework that formalized the points system for evaluating prospective immigrants based on factors such as education, skills, and language ability, shaping Canadian immigration policy on the basis of qualifications rather than national origin.',
  [('What did the Immigration Act of 1976 establish?', ['A legal framework that formalized the points system for evaluating prospective immigrants', 'A ban on all immigration to Canada', 'A treaty ending immigration between Canada and Britain', 'A new provincial border'], 0),
   ('What factors did the points system use to evaluate prospective immigrants?', ['Education, skills, and language ability', 'Only the applicants country of birth', 'Only the applicants religion', 'Only the applicants age'], 0),
   ('How did the points system change the basis for Canadian immigration policy?', ['It shifted evaluation toward qualifications rather than national origin', 'It based every decision solely on national origin', 'It removed all criteria for evaluating immigrants', 'It ended immigration to Canada entirely'], 0),
   ('In what year was the Immigration Act that formalized the points system passed?', ['1976', '1867', '1919', '1947'], 0),
   ('Why is the points system considered a significant shift in Canadian immigration history?', ['It moved policy away from discriminatory national origin criteria toward measurable qualifications', 'It had no meaningful effect on immigration policy', 'It restricted immigration to a single country of origin', 'It eliminated any consideration of an applicants skills'], 0)]),
]),
day(185, [
E('Oral Communication: The Panel Discussion and Moderation',
  'Grade 10 English strand: a panel discussion brings together multiple speakers with different perspectives on a topic under the guidance of a moderator, who introduces the subject, manages turn-taking, keeps the conversation focused, and ensures that each panelist has a fair opportunity to contribute.',
  [('What is a panel discussion?', ['A format that brings together multiple speakers with different perspectives on a topic', 'A speech delivered by a single speaker with no audience', 'A silent presentation with no spoken words', 'A written report with no discussion element'], 0),
   ('What role does a moderator play in a panel discussion?', ['Introducing the topic, managing turn-taking, and keeping the conversation focused', 'Speaking for the entire discussion with no other participants', 'Preventing any panelist from speaking', 'Ending the discussion before it begins'], 0),
   ('Why might a panel discussion include speakers with different perspectives?', ['To give the audience a fuller understanding of multiple viewpoints on a topic', 'To ensure every speaker agrees completely with no disagreement', 'To remove any discussion of the topic entirely', 'Because panels are required to have identical opinions'], 0),
   ('What does it mean for a moderator to ensure fair turn-taking?', ['Giving each panelist a reasonable opportunity to contribute to the discussion', 'Allowing only one panelist to speak for the entire event', 'Preventing the audience from hearing any panelist', 'Ending the panel immediately after it starts'], 0),
   ('Why might a moderator need to keep a panel discussion focused?', ['To prevent the conversation from straying too far from the intended topic', 'Because focus has no value in oral communication', 'To ensure the panelists never address the topic at all', 'Because moderators are not responsible for guiding discussion'], 0)]),
M('Discrete Math: The Traveling Salesman Problem',
  'Grade 10 Math strand: the Traveling Salesman Problem asks for the shortest possible route that visits a given set of locations exactly once and returns to the starting point, a deceptively simple question that becomes extremely difficult to solve exactly as the number of locations grows.',
  [('What does the Traveling Salesman Problem ask for?', ['The shortest possible route that visits a set of locations exactly once and returns to the start', 'The tallest building among a set of locations', 'The average distance between two random points', 'A route that avoids visiting any location at all'], 0),
   ('What happens to the difficulty of solving the Traveling Salesman Problem exactly as the number of locations increases?', ['It becomes extremely difficult to solve exactly', 'It becomes easier to solve with each additional location', 'It has no effect on the difficulty of the problem', 'It becomes impossible to define as a problem'], 0),
   ('What real-world scenario could the Traveling Salesman Problem help model?', ['Planning an efficient delivery route across multiple locations', 'Measuring the temperature of a single location', 'Balancing a chemical equation', 'Finding the area of a triangle'], 0),
   ('Why is the Traveling Salesman Problem considered deceptively simple?', ['Its description is easy to state, yet finding an exact optimal solution is computationally demanding', 'It has no real mathematical content at all', 'It can always be solved instantly regardless of the number of locations', 'It is unrelated to any concept in graph theory'], 0),
   ('What field of mathematics is the Traveling Salesman Problem most closely associated with?', ['Discrete mathematics and graph theory', 'Trigonometry', 'Basic arithmetic', 'Plane geometry involving circles only'], 0)]),
Sc('Physics: Friction and Traction in Everyday Motion',
   'Grade 10 Science strand: friction is a force that resists the relative motion between two surfaces in contact, and traction is the specific application of friction that allows tires, shoes, and other surfaces to grip and prevent slipping, with factors such as surface texture and applied force affecting how much friction is generated.',
   [('What does friction do between two surfaces in contact?', ['Resists their relative motion', 'Increases their relative motion without limit', 'Has no effect on their relative motion', 'Eliminates all contact between the surfaces'], 0),
    ('What is traction?', ['The application of friction that allows surfaces to grip and prevent slipping', 'A force that has no relationship to friction', 'A measurement of temperature between two surfaces', 'A term used only in describing ocean currents'], 0),
    ('Which factor can affect how much friction is generated between two surfaces?', ['Surface texture and the amount of applied force', 'The colour of the two surfaces', 'The exact time of day the surfaces touch', 'The distance from the nearest ocean'], 0),
    ('Why do winter tires often provide better traction on icy roads than standard tires?', ['Their tread and rubber composition are designed to grip better in cold, slippery conditions', 'They eliminate all friction between the tire and the road', 'They have no rubber content at all', 'They are designed to reduce contact with the road surface'], 0),
    ('What might happen if there were no friction between a shoe and the ground while walking?', ['The foot would slip rather than grip the surface', 'Walking would become easier with no resistance at all', 'Friction has no relevance to walking', 'The shoe would instantly stop touching the ground'], 0)]),
H('The Patriation of the Constitution in 1982',
  'Grade 10 History strand: the patriation of the Constitution in 1982 transferred final legal authority over the Canadian Constitution from the British Parliament to Canada, giving the country full control over its own amending formula and simultaneously introducing the Canadian Charter of Rights and Freedoms.',
  [('What did the patriation of the Constitution in 1982 accomplish?', ['It transferred final legal authority over the Canadian Constitution from Britain to Canada', 'It transferred authority over the Canadian Constitution to the United States', 'It ended the existence of the Canadian Constitution entirely', 'It gave Britain greater control over Canadian law'], 0),
   ('What new document was introduced alongside the patriation of the Constitution in 1982?', ['The Canadian Charter of Rights and Freedoms', 'The Canadian Bill of Rights', 'The Official Languages Act', 'The Statute of Westminster'], 0),
   ('What had the British Parliament previously held with respect to the Canadian Constitution?', ['Final legal authority to amend it', 'No connection to the Canadian Constitution whatsoever', 'Authority over Canadian provincial elections only', 'Authority limited strictly to Canadian trade policy'], 0),
   ('What did patriation give Canada full control over?', ['Its own constitutional amending formula', 'Control over the government of the United Kingdom', 'Control over the constitutions of other countries', 'Control over international shipping law'], 0),
   ('In what year did the patriation of the Constitution take place?', ['1982', '1867', '1931', '1949'], 0)]),
]),
day(186, [
E('Literature: The Mock-Epic and Satirical Verse',
  'Grade 10 English strand: a mock-epic applies the grand style, conventions, and elevated language of classical epic poetry to a trivial or ordinary subject, creating satirical humour through the exaggerated mismatch between form and content.',
  [('What does a mock-epic apply to a trivial or ordinary subject?', ['The grand style and conventions of classical epic poetry', 'A completely plain, unadorned style with no formal elements', 'A strictly factual, journalistic style', 'A style with no connection to poetry at all'], 0),
   ('How does a mock-epic typically create humour?', ['Through the exaggerated mismatch between elevated form and a trivial subject', 'By using no exaggeration of any kind', 'By avoiding any reference to epic conventions', 'By presenting the subject with complete seriousness and no irony'], 0),
   ('What kind of language does a mock-epic typically borrow from classical epic poetry?', ['Elevated, grand language', 'Extremely simple, childlike language', 'Language limited to legal terminology', 'Language with no rhetorical elements'], 0),
   ('What is the general purpose of satirical verse such as a mock-epic?', ['To criticize or poke fun at a subject through exaggeration and irony', 'To provide a completely neutral, unbiased account of a subject', 'To eliminate all humour from the text', 'To remove any critical perspective from the writing'], 0),
   ('Why might exaggerated formality make a trivial subject seem humorous in a mock-epic?', ['The contrast between serious tone and minor subject matter creates comic irony', 'Formality always makes a subject seem more important with no comic effect', 'Trivial subjects cannot be paired with formal language', 'Mock-epics never use any form of irony'], 0)]),
M('Statistics: Z-Scores and Standardized Values',
  'Grade 10 Math strand: a z-score expresses how many standard deviations a particular data value lies above or below the mean of a data set, allowing values from different distributions to be compared on a common standardized scale.',
  [('What does a z-score express?', ['How many standard deviations a data value lies above or below the mean', 'The exact value of the mean itself', 'The total number of data points in a set', 'The largest value found in a data set'], 0),
   ('What is one benefit of converting data values to z-scores?', ['Values from different distributions can be compared on a common standardized scale', 'Z-scores make it impossible to compare any two data sets', 'Z-scores eliminate the need for a mean or standard deviation', 'Z-scores only apply to a single specific data set with no broader use'], 0),
   ('What does a z-score of zero indicate about a data value?', ['The value is exactly equal to the mean of the data set', 'The value is far above the mean', 'The value is far below the mean', 'The value cannot be calculated'], 0),
   ('What does a negative z-score indicate about a data value?', ['The value lies below the mean of the data set', 'The value lies above the mean of the data set', 'The value is exactly equal to the standard deviation', 'The data set contains no negative numbers'], 0),
   ('What two measures are needed to calculate a z-score for a given data value?', ['The mean and standard deviation of the data set', 'Only the largest and smallest values in the data set', 'Only the median of the data set', 'The number of data points and nothing else'], 0)]),
Sc('Chemistry: The Chemistry of Rust Prevention and Metal Coatings',
   'Grade 10 Science strand: rust forms when iron reacts with oxygen and moisture in an electrochemical process, and preventing rust often involves applying a protective coating such as paint, zinc galvanization, or oil to block the metal surface from contact with the oxygen and water that drive the reaction.',
   [('What causes iron to rust?', ['A reaction between iron, oxygen, and moisture', 'A reaction between iron and pure nitrogen gas only', 'Exposure to extremely cold, dry air with no moisture present', 'A reaction that requires no oxygen whatsoever'], 0),
    ('What type of chemical process is rusting?', ['An electrochemical process', 'A purely mechanical process with no chemical change', 'A process that occurs only inside a sealed vacuum', 'A nuclear reaction'], 0),
    ('What is one common method used to prevent rust on metal surfaces?', ['Applying a protective coating such as paint or zinc galvanization', 'Increasing the metals direct exposure to oxygen and water', 'Removing all carbon from the metal', 'Exposing the metal to additional moisture'], 0),
    ('What does a protective coating do to help prevent rust?', ['Blocks the metal surface from contact with oxygen and water', 'Increases the rate at which oxygen reaches the metal surface', 'Has no effect on the reaction between iron and oxygen', 'Removes iron from the metal entirely'], 0),
    ('What metal is commonly used to galvanize iron or steel as a rust-prevention method?', ['Zinc', 'Gold', 'Helium', 'Neon'], 0)]),
H('Brian Mulroney and the Progressive Conservative Landslide of 1984',
  'Grade 10 History strand: the 1984 federal election produced a landslide victory for the Progressive Conservatives under Brian Mulroney, ending an extended period of Liberal dominance in federal politics and setting the stage for major policy shifts including free trade negotiations with the United States.',
  [('What was the outcome of the 1984 federal election?', ['A landslide victory for the Progressive Conservatives under Brian Mulroney', 'A narrow Liberal minority government', 'A tie between all major parties', 'The cancellation of the federal election'], 0),
   ('Who led the Progressive Conservatives to victory in the 1984 election?', ['Brian Mulroney', 'Pierre Trudeau', 'John Diefenbaker', 'Lester Pearson'], 0),
   ('What period of federal politics did the 1984 election result help bring to an end?', ['An extended period of Liberal dominance in federal politics', 'An extended period with no federal government of any kind', 'A period with no political parties in Canada', 'A period of Progressive Conservative dominance'], 0),
   ('What major policy shift did the Mulroney government help set in motion after 1984?', ['Free trade negotiations with the United States', 'The permanent end of all trade with other countries', 'The abolition of the Canadian dollar', 'The cancellation of all federal elections'], 0),
   ('How large was the Progressive Conservative victory in the 1984 federal election?', ['It was a landslide, winning by a wide margin', 'It was decided by a single vote', 'It resulted in no government being formed', 'It was the closest election in Canadian history'], 0)]),
]),
day(187, [
E('English Review: The Final Review -- Reading, Writing, Grammar, and Media Literacy (Days 181-186)',
  'Grade 10 English strand review, and the concluding review of the full Grade 10 English course: students revisit flashback and nonlinear timelines, the letter to the editor, split infinitives, documentary film techniques, the panel discussion, and the mock-epic, completing the 187-day Grade 10 English curriculum.',
  [('What does a flashback do within a narrative?', ['Interrupts the chronological order to show an earlier event', 'Predicts an event that has not yet happened', 'Repeats the current scene word for word', 'Removes all characters from the story'], 0),
   ('What is a letter to the editor?', ['A piece of persuasive writing submitted to a newspaper or publication in response to a current issue', 'A private letter never intended for publication', 'A recipe published in a cooking magazine', 'A weather report with no argument'], 0),
   ('What is a split infinitive?', ['A construction where a word is placed between to and the verb that follows it', 'A sentence with no verb at all', 'A sentence that begins with a question word', 'A verb with two different subjects'], 0),
   ('Which technique might a documentary filmmaker use to present factual subject matter?', ['Archival footage, expert interviews, and voice-over narration', 'A completely fictional plot with no factual basis', 'A script written entirely in verse', 'An animated sequence with no connection to reality'], 0),
   ('What is a panel discussion?', ['A format that brings together multiple speakers with different perspectives on a topic', 'A speech delivered by a single speaker with no audience', 'A silent presentation with no spoken words', 'A written report with no discussion element'], 0)]),
M('Math Review: The Final Review -- Number Theory, Calculus, Geometry, and Statistics (Days 181-186)',
  'Grade 10 Math strand review, and the concluding review of the full Grade 10 Math course: students revisit Goldbachs Conjecture, linear approximation, loci, Gaussian elimination, the Traveling Salesman Problem, and z-scores, completing the 187-day Grade 10 Math curriculum.',
  [('What does Goldbachs Conjecture propose?', ['That every even integer greater than two can be written as the sum of two prime numbers', 'That every odd integer is automatically prime', 'That no even number can ever be divided evenly', 'That prime numbers do not exist beyond one hundred'], 0),
   ('What does linear approximation use to estimate a functions value near a known point?', ['The tangent line at that known point', 'A completely unrelated function', 'The area under the entire curve', 'A random guess with no mathematical basis'], 0),
   ('What is a locus in geometry?', ['The set of all points that satisfy a given geometric condition', 'A single fixed point with no other points nearby', 'A line with an undefined length', 'A shape with no defined boundary at all'], 0),
   ('How can a system of linear equations be represented for use with Gaussian elimination?', ['As a matrix', 'As a single unrelated number', 'As a circle graph', 'As a single word problem with no numerical structure'], 0),
   ('What does the Traveling Salesman Problem ask for?', ['The shortest possible route that visits a set of locations exactly once and returns to the start', 'The tallest building among a set of locations', 'The average distance between two random points', 'A route that avoids visiting any location at all'], 0)]),
Sc('Science Review: The Final Review -- Physics, Chemistry, Earth Science, and Biology (Days 181-186)',
   'Grade 10 Science strand review, and the concluding review of the full Grade 10 Science course: students revisit terminal velocity, food spoilage and preservation, ocean tides, decomposers and nutrient cycling, friction and traction, and rust prevention, completing the 187-day Grade 10 Science curriculum.',
   [('What is terminal velocity?', ['The constant maximum speed a falling object reaches when air resistance balances gravity', 'The speed of an object the instant it is released', 'The speed of an object with no air resistance acting on it', 'The speed at which an object accelerates forever without limit'], 0),
    ('What commonly causes food spoilage?', ['Microorganisms and chemical reactions such as oxidation', 'A complete absence of any chemical activity', 'Food becoming instantly sterile with no further change', 'The total removal of all bacteria with no other cause'], 0),
    ('What primarily causes ocean tides?', ['The gravitational pull of the moon and, to a lesser extent, the sun', 'Wind blowing across the surface of the ocean', 'Volcanic activity beneath the ocean floor', 'Changes in ocean water temperature alone'], 0),
    ('What role do decomposers play in an ecosystem?', ['They break down dead organisms and waste into simpler substances', 'They produce all of the oxygen in an ecosystem', 'They consume only living plants and animals', 'They prevent any nutrients from returning to the soil'], 0),
    ('What does friction do between two surfaces in contact?', ['Resists their relative motion', 'Increases their relative motion without limit', 'Has no effect on their relative motion', 'Eliminates all contact between the surfaces'], 0)]),
H('History Review: The Final Review -- Canada in the Trudeau and Mulroney Years (Days 181-186)',
  'Grade 10 History strand review, and the concluding review of the full Grade 10 History course: students revisit Trudeaumania and the 1968 election, the Just Society, the metric conversion of the 1970s, the Immigration Act of 1976, the patriation of the Constitution in 1982, and the Mulroney landslide of 1984, completing the 187-day Grade 10 History curriculum.',
  [('What does the term Trudeaumania describe?', ['The wave of public enthusiasm surrounding Pierre Trudeau during the 1968 election', 'A federal law passed in 1968', 'A treaty signed between Canada and France', 'A new Canadian currency introduced in 1968'], 0),
   ('What was the Just Society?', ['The guiding political vision Pierre Trudeau promoted as prime minister', 'A treaty signed between Canada and Britain', 'A federal department created in 1968', 'A new Canadian province'], 0),
   ('What change did the federal government begin implementing in the 1970s?', ['Converting Canada from imperial to metric measurement', 'Replacing the Canadian dollar with a new currency', 'Abolishing all provincial governments', 'Ending federal elections'], 0),
   ('What did the Immigration Act of 1976 establish?', ['A legal framework that formalized the points system for evaluating prospective immigrants', 'A ban on all immigration to Canada', 'A treaty ending immigration between Canada and Britain', 'A new provincial border'], 0),
   ('What did the patriation of the Constitution in 1982 accomplish?', ['It transferred final legal authority over the Canadian Constitution from Britain to Canada', 'It transferred authority over the Canadian Constitution to the United States', 'It ended the existence of the Canadian Constitution entirely', 'It gave Britain greater control over Canadian law'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_181_187)
    append_to(10, g10_181_187)
