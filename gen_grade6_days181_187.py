#!/usr/bin/env python3
"""Grade 6, Days 181-187 -- extends Grade 6 from 180 to 187 days, completing
the full 187-day Ontario Grade 6 curriculum target. This is the FINAL batch
for this grade. Modeled exactly on gen_grade6_days171_180.py: same L/M/Sc/SS
helpers over gen_curriculum's sub()/day()/append_to(), same TVO Learn
placeholder resourceLabel/resourceUrl convention (videoUrl intentionally
left unset, filled in later by the daily curriculum-video-backfill
scheduled task). This batch is only 7 days (181-187), not the usual 10,
since 180 + 7 = 187 is the full-year target: 6 new content days
(181-186, one new topic per subject per day) plus Day 187 as a final
cross-subject capstone review day.

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-180
topics (see data/grade6.json, checked via a full subject/title dump before
writing this file), which already densely cover nearly the entire grade 6
curriculum -- and a great deal of enrichment beyond it -- across all four
subjects. New topics for Days 181-186: the subjunctive mood, understanding
motifs in literature, writing a speech of introduction, malapropisms and
word confusion, analyzing infographics, and non-verbal communication for
Language; introduction to modular arithmetic (clock math), solving systems
of two linear equations by graphing, calculating percentiles, conditional
probability, exterior angles of polygons, and multiplying/dividing numbers
in scientific notation for Math; crystal formation and crystallization,
Earths magnetic field and how a compass works, the Maillard reaction (the
chemistry of browning food), sonar technology, the ozone layer, and
additive versus subtractive colour mixing for Science; and Nellie McClung
and the fight for womens suffrage in Canada, equalization payments between
provinces, the White Paper of 1969, the CBC as Canadas public broadcaster,
Canadas mission in Afghanistan, and the Indian Act for Social Studies --
none of those exact ideas appear in Days 1-180. Day 187 is the final
cross-subject review day of the entire 187-day build, matching the
end-of-batch review pattern used in every prior batch for this grade; its
four review titles (Language Review: The Final Chapter -- Grammar,
Vocabulary, and Communication Skills / Math Review: The Final Chapter --
Number Systems, Geometry, and Probability / Science Review: The Final
Chapter -- Chemistry, Earth Science, and Technology / Social Studies
Review: The Final Chapter -- Government, Rights, and Canadian History) are
worded distinctly from every earlier review days titles, while their
summaries acknowledge this is the capstone review closing out the full
187-day Grade 6 program. No embedded ASCII apostrophe or double-quote
characters are used anywhere in title/summary/question/option text --
apostrophes are dropped entirely (e.g. "Canadas" not "Canada's", "Earths"
not "Earth's"), matching the rest of Grade 6.

Usage: python3 gen_grade6_days181_187.py
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science and Technology',
    'TVO Learn: Grade 6 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L6, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M6, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S6, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS6, q)


def _rebalance_answer_positions(days, seed=20260818187):
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


g6_181_187 = [
day(181, [
L('Grammar: The Subjunctive Mood and Its Uses',
  'Grade 6 Language strand: the subjunctive mood expresses a wish, suggestion, or a condition that is not currently true, often appearing in clauses such as if I were you or the teacher suggested that he arrive early.',
  [('What does the subjunctive mood typically express?', ['A wish, suggestion, or a condition that is not currently true', 'A simple statement of fact', 'A command given to a group', 'A question about the past'], 0),
   ('Which sentence uses the subjunctive mood correctly?', ['If I were taller, I would join the team.', 'If I was taller, I would join the team.', 'If I am taller, I would join the team.', 'If I will be taller, I would join the team.'], 0),
   ('Which word in the sentence The coach suggested that she practice every day signals the subjunctive mood?', ['Practice, the base form used instead of practices', 'Coach', 'Suggested', 'Every day'], 0),
   ('Why does English use were instead of was in subjunctive statements like If I were you?', ['The special verb form signals that the statement describes a hypothetical or unreal situation', 'Was is grammatically incorrect in every sentence', 'Were is only used when talking about more than one person', 'The subjunctive mood has no connection to hypothetical situations'], 0),
   ('Why might a writer choose subjunctive phrasing such as I wish I were rather than a simple statement?', ['It clearly signals that the wish describes something not currently true, adding precision to the sentences meaning', 'Subjunctive phrasing always makes a sentence factually true', 'The subjunctive mood cannot be used to express wishes', 'Simple statements always convey hypothetical ideas more clearly than the subjunctive'], 0)]),
M('Number Sense: Introduction to Modular Arithmetic (Clock Math)',
  'Grade 6 Math strand: modular arithmetic finds the remainder after dividing one number by another, often called clock math because a 12-hour clock cycles back to 1 after reaching 12, similar to counting modulo 12.',
  [('What does modular arithmetic calculate?', ['The remainder after dividing one number by another', 'The sum of two numbers', 'The square root of a number', 'The average of a list of numbers'], 0),
   ('What is 14 mod 5?', ['4', '2', '9', '5'], 0),
   ('On a 12-hour clock, what time is 3 hours after 11:00?', ['2:00', '14:00', '3:00', '1:00'], 0),
   ('Why is a 12-hour clock a useful real-world example of modular arithmetic?', ['Clock times cycle back to 1 after reaching 12, matching how modular arithmetic wraps numbers around after reaching a fixed value', 'Clocks never repeat any numbers throughout the day', 'A 12-hour clock counts upward forever without ever resetting', 'Modular arithmetic has no connection to how time is measured'], 0),
   ('Why might modular arithmetic be useful in fields such as computer science, beyond telling time?', ['It provides a systematic way to work with numbers that cycle or repeat in a fixed pattern, useful for tasks such as scheduling or encoding data', 'Modular arithmetic can only be used to calculate exact, non-repeating totals', 'Computers never need to work with repeating or cyclical patterns', 'Modular arithmetic removes the need for any other type of calculation'], 0)]),
Sc('Science: Crystal Formation and Crystallization',
   'Grade 6 Science strand: crystallization occurs when a dissolved substance separates from a solution and its particles arrange themselves into a repeating geometric pattern, forming a solid crystal, a process that can be sped up by cooling or evaporating a solution.',
   [('What is crystallization?', ['A process in which a dissolved substance separates from a solution and forms a solid with a repeating geometric pattern', 'A process that only occurs inside living cells', 'The complete disappearance of a dissolved substance', 'A process that turns a solid directly into a gas'], 0),
    ('What can speed up the crystallization process in a solution?', ['Cooling or evaporating the solution', 'Adding more solvent to the solution', 'Keeping the solution at a constant warm temperature indefinitely', 'Removing all dissolved substance from the solution'], 0),
    ('What repeating structure do the particles in a crystal typically form?', ['A repeating geometric pattern', 'A completely random, unrepeated arrangement', 'A liquid structure with no fixed shape', 'A gaseous cloud with no particles'], 0),
    ('Why do crystals often form specific geometric shapes, such as cubes or hexagons?', ['The particles arrange themselves in a repeating pattern determined by how they bond together at a molecular level', 'Crystal shapes are chosen randomly with no connection to particle arrangement', 'All crystals form the exact same shape regardless of their particles', 'Crystals never have any predictable shape at all'], 0),
    ('Why might scientists grow crystals slowly in a laboratory rather than quickly?', ['Slower crystallization generally allows larger, more well formed crystals to develop, since the particles have more time to arrange into an orderly pattern', 'Growing crystals slowly always produces smaller, weaker crystals', 'The speed of crystallization has no effect on the size of the resulting crystals', 'Crystals can only form correctly when cooled instantly'], 0)]),
SS('Social Studies: Nellie McClung and the Fight for Womens Suffrage in Canada',
   'Grade 6 Social Studies strand: Nellie McClung was a Canadian author and activist who campaigned for womens right to vote, helping Manitoba become the first province to grant women suffrage in 1916.',
   [('What cause did Nellie McClung campaign for?', ['Womens right to vote', 'Lower taxes for farmers', 'The construction of new railways', 'Free international trade agreements'], 0),
    ('Which province became the first in Canada to grant women the right to vote, largely due to activists like McClung?', ['Manitoba', 'Ontario', 'British Columbia', 'Quebec'], 0),
    ('In what year did Manitoba grant women the right to vote?', ['1916', '1867', '1929', '1949'], 0),
    ('Why might activists like Nellie McClung have used writing and public speaking to advance their cause?', ['Public writing and speaking could reach and persuade a wide audience, building support for changing unfair laws', 'Writing and speaking had no effect on public opinion at the time', 'Activists were legally required to remain silent about their views', 'Only government officials were permitted to discuss voting laws'], 0),
    ('Why is the history of the womens suffrage movement in Canada still studied today?', ['It highlights how organized advocacy can lead to meaningful legal change and expanded rights over time', 'The movement had no lasting impact on Canadian law', 'Voting rights in Canada have never changed since Confederation', 'Studying past advocacy movements has no relevance to understanding rights today'], 0)]),
]),
day(182, [
L('Reading: Understanding Motifs in Literature',
  'Grade 6 Language strand: a motif is a recurring image, symbol, or idea that appears repeatedly throughout a literary work, helping to reinforce its central themes.',
  [('What is a motif?', ['A recurring image, symbol, or idea that appears repeatedly throughout a literary work', 'A single event that happens only once in a story', 'A type of punctuation used in dialogue', 'The title of a book'], 0),
   ('What is one purpose of a motif in a story?', ['It helps reinforce the storys central themes', 'It replaces the need for a plot', 'It only appears one single time in a story', 'It has no connection to a storys meaning'], 0),
   ('Which of these could serve as a motif if it appeared repeatedly throughout a novel?', ['A particular colour, object, or phrase', 'A page number', 'The books total word count', 'The font used in printing'], 0),
   ('Why might an author repeat a specific image, such as a caged bird, throughout a story?', ['Repetition can draw attention to an idea, such as a feeling of being trapped, and connect it to a larger theme', 'Repeating an image always confuses readers with no benefit', 'Authors never repeat images or ideas within a single story', 'A repeated image can never be connected to a storys theme'], 0),
   ('Why is recognizing motifs useful for a reader analyzing a novels deeper meaning?', ['Noticing patterns that repeat can reveal ideas the author wants to emphasize beyond the surface events of the plot', 'Motifs never reveal anything about an authors intended themes', 'Recognizing patterns in a text always distracts from its meaning', 'A novels deeper meaning can only be found in its title'], 0)]),
M('Algebra: Solving Systems of Two Linear Equations by Graphing',
  'Grade 6 Math strand: a system of two linear equations can be solved by graphing both lines on the same coordinate plane and identifying the point where they intersect, which represents the solution that satisfies both equations.',
  [('What does the point of intersection of two graphed lines represent in a system of equations?', ['The solution that satisfies both equations', 'The steepest point on either line', 'The starting point of the first line only', 'A point that satisfies neither equation'], 0),
   ('How many solutions does a system of two linear equations typically have if the lines intersect at exactly one point?', ['One solution', 'No solution', 'Infinite solutions', 'Two solutions'], 0),
   ('What does it mean if two lines in a system never intersect?', ['The system has no solution', 'The system has exactly one solution', 'The system has infinite solutions', 'The lines are the same line'], 0),
   ('Why does graphing provide a visual way to solve a system of two linear equations?', ['The intersection point can be seen directly on the graph, showing the values that make both equations true at the same time', 'Graphing never shows where two equations share a common solution', 'A graph can only display a single equation at once', 'Intersection points on a graph have no connection to solving equations'], 0),
   ('Why might graphing be less precise than other methods for solving a system of equations with a solution that includes fractions?', ['Reading exact fractional coordinates from a hand-drawn graph can be difficult, making the graphical method better suited for estimating or checking a solution', 'Graphing always gives a more precise answer than any other method', 'Fractional solutions can never be estimated using a graph', 'Graphing and algebraic methods always produce identical levels of precision'], 0)]),
Sc('Science: Earths Magnetic Field and How a Compass Works',
   'Grade 6 Science strand: Earth behaves like a giant magnet with a magnetic field that stretches from pole to pole, and a compass needle aligns itself with this field to point toward magnetic north.',
   [('What does Earth behave like, according to scientists studying magnetism?', ['A giant magnet with a magnetic field', 'A completely non-magnetic sphere', 'A magnet only at its exact center', 'An object with no magnetic properties at all'], 0),
    ('What does a compass needle align itself with?', ['Earths magnetic field', 'The nearest large body of water', 'The position of the sun only', 'The direction of the wind'], 0),
    ('Toward what does a compass needle typically point?', ['Magnetic north', 'The equator', 'The nearest mountain', 'The center of Earth'], 0),
    ('Why has a compass been such a useful navigation tool throughout history?', ['It provides a reliable way to determine direction using Earths magnetic field, even when other landmarks are not visible', 'A compass only works when landmarks are already clearly visible', 'Compasses have never been useful for navigation', 'Earths magnetic field has no connection to how a compass functions'], 0),
    ('Why might a compass give an inaccurate reading if held too close to a strong magnet or large piece of metal?', ['A nearby magnetic source can interfere with the compass needles alignment to Earths much weaker magnetic field', 'Nearby metal objects always make a compass more accurate', 'Compass needles are never affected by nearby magnetic materials', 'Earths magnetic field becomes stronger near metal objects'], 0)]),
SS('Social Studies: Equalization Payments Between Canadian Provinces',
   'Grade 6 Social Studies strand: equalization payments are funds transferred by the federal government to less wealthy provinces so that all provinces can provide reasonably similar levels of public services at reasonably similar levels of taxation.',
   [('What are equalization payments?', ['Funds transferred by the federal government to less wealthy provinces', 'Taxes collected exclusively from foreign visitors', 'Loans that provinces must repay to private banks', 'Fees charged to municipalities for road repairs'], 0),
    ('What is the main goal of the equalization payment system?', ['To help all provinces provide reasonably similar levels of public services', 'To eliminate all provincial governments', 'To fund only one province permanently', 'To replace provincial taxes entirely'], 0),
    ('Which level of government provides equalization payments to provinces?', ['The federal government', 'Municipal governments', 'Foreign governments', 'Private companies'], 0),
    ('Why might a country like Canada choose to redistribute funds between provinces of differing wealth?', ['Redistribution can help ensure that residents across the country have access to comparable services such as healthcare and education, regardless of where they live', 'Redistributing funds always reduces the quality of services in every province', 'Provinces are never permitted to have differing levels of wealth', 'Equalization payments have no connection to public services'], 0),
    ('Why can equalization payments sometimes be a source of political debate between provinces?', ['Provinces receiving fewer payments may feel their contributions outweigh what they receive back, while others may depend on the funding to maintain public services', 'All provinces always agree completely on how equalization payments should work', 'Equalization payments are never discussed in Canadian politics', 'Every province receives the exact same amount regardless of wealth'], 0)]),
]),
day(183, [
L('Writing: Writing a Speech of Introduction',
  'Grade 6 Language strand: a speech of introduction presents a guest speaker to an audience by briefly highlighting their background and achievements, building excitement and credibility before they begin speaking.',
  [('What does a speech of introduction typically present?', ['A guest speaker to an audience', 'An unrelated news story', 'A detailed weather forecast', 'A list of upcoming school events'], 0),
   ('What does a speech of introduction usually highlight about the speaker?', ['Their background and achievements', 'An unrelated news story', 'A detailed weather forecast', 'The introducers own opinions on unrelated topics'], 0),
   ('What is one goal of a speech of introduction?', ['Building excitement and credibility before the speaker begins', 'Making the audience forget about the guest speaker', 'Replacing the guest speakers entire presentation', 'Discouraging the audience from listening further'], 0),
   ('Why should a speech of introduction remain relatively brief?', ['A concise introduction keeps the audiences focus on the guest speaker rather than the person introducing them', 'A brief introduction always fails to properly welcome a guest speaker', 'Longer introductions are always more effective than shorter ones', 'Length has no effect on how an audience responds to an introduction'], 0),
   ('Why might including a specific accomplishment or credential in an introduction help the audience?', ['Specific details can establish why the speaker is worth listening to, building trust and interest before they even begin', 'Specific details always make an introduction less credible', 'Credentials have no effect on how an audience perceives a speaker', 'General statements always build more trust than specific details'], 0)]),
M('Data Management: Calculating Percentiles in a Data Set',
  'Grade 6 Math strand: a percentile indicates the percentage of values in a data set that fall below a particular value, helping compare an individual score to the rest of a group.',
  [('What does a percentile indicate about a value in a data set?', ['The percentage of values in the data set that fall below it', 'The exact average of the entire data set', 'The largest value found anywhere in the data set', 'The total number of values in the data set'], 0),
   ('If a students test score is at the 80th percentile, what does that mean?', ['About 80 percent of scores in the data set are below that students score', 'The student answered exactly 80 percent of questions correctly', '80 students took the test', 'The student scored in the bottom 20 percent'], 0),
   ('What percentile represents the median of a data set?', ['The 50th percentile', 'The 100th percentile', 'The 0th percentile', 'The 25th percentile'], 0),
   ('Why are percentiles useful for comparing an individual result to a larger group?', ['They show relative standing within the group rather than just a raw score, making comparisons easier to interpret', 'Percentiles always hide how an individual compares to a group', 'Raw scores always provide more useful comparisons than percentiles', 'Percentiles cannot be used to compare individual results at all'], 0),
   ('Why might two data sets with different total numbers of values still be compared fairly using percentiles?', ['Percentiles are based on relative position within each data set, so they allow meaningful comparisons regardless of how many values each set contains', 'Percentiles can only be calculated when two data sets have the exact same number of values', 'Data sets of different sizes can never be compared in any way', 'Percentiles always require identical sample sizes to be meaningful'], 0)]),
Sc('Science: The Maillard Reaction — The Chemistry of Browning Food',
   'Grade 6 Science strand: the Maillard reaction is a chemical reaction between amino acids and sugars that occurs when food is heated, producing the browned colour and rich flavour found in foods such as toasted bread and seared meat.',
   [('What two substances react with each other during the Maillard reaction?', ['Amino acids and sugars', 'Water and salt', 'Oxygen and carbon dioxide', 'Oil and vinegar'], 0),
    ('What condition is needed for the Maillard reaction to occur in food?', ['The food must be heated', 'The food must be frozen', 'The food must be soaked in water', 'The food must be left in complete darkness'], 0),
    ('What visible change does the Maillard reaction typically produce in food?', ['A browned colour', 'A bright blue colour', 'No visible change at all', 'A transparent appearance'], 0),
    ('Why does toasted bread taste and look different from untoasted bread?', ['Heating triggers the Maillard reaction, producing new flavour compounds and a browned colour that are not present in the unheated bread', 'Toasting bread removes all of its flavour compounds', 'The Maillard reaction only occurs in liquids, never in bread', 'Heat has no effect on the flavour or colour of bread'], 0),
    ('Why might a cook sear meat at a high temperature before finishing it in a lower-temperature oven?', ['The high heat triggers the Maillard reaction on the surface, developing a browned crust and rich flavour that a lower temperature alone would not produce', 'Searing meat always removes its flavour entirely', 'The Maillard reaction only happens at very low temperatures', 'High heat prevents any chemical reactions from occurring in food'], 0)]),
SS('Social Studies: The White Paper of 1969 and First Nations Opposition',
   'Grade 6 Social Studies strand: the 1969 White Paper was a federal government policy proposal that would have eliminated the Indian Act and existing treaty rights, but it was withdrawn after strong opposition from First Nations leaders and communities across Canada.',
   [('What government document is known as the White Paper of 1969?', ['A federal policy proposal that would have eliminated the Indian Act and existing treaty rights', 'A treaty signed between Canada and another country', 'A provincial budget report', 'A report on Canadian trade with Europe'], 0),
    ('How did First Nations leaders and communities respond to the White Paper?', ['They strongly opposed it', 'They immediately approved it with no concerns', 'They had no reaction to the proposal at all', 'They were not informed of the proposal'], 0),
    ('What happened to the White Paper after facing this opposition?', ['It was withdrawn', 'It was immediately passed into law', 'It was expanded to apply to more countries', 'It became a permanent part of the constitution unchanged'], 0),
    ('Why might First Nations leaders have opposed a policy that removed the Indian Act and treaty rights, even though the Indian Act itself contained many discriminatory provisions?', ['Treaty rights and existing legal recognition were seen as important protections, and removing them without proper consultation could have eliminated hard-won rights rather than improving them', 'First Nations leaders had no concerns about losing treaty rights', 'The Indian Act contained no provisions related to land or governance', 'Removing legal recognition was expected to immediately improve conditions for First Nations peoples'], 0),
    ('Why is the response to the White Paper considered an important moment in the history of Indigenous political organizing in Canada?', ['It demonstrated the impact of unified political action and helped shape future government consultation with Indigenous peoples', 'The response had no lasting effect on government policy', 'Indigenous political organizing began for the first time after this event', 'The White Paper was never discussed or opposed by any First Nations leaders'], 0)]),
]),
day(184, [
L('Vocabulary: Malapropisms and Word Confusion',
  'Grade 6 Language strand: a malapropism occurs when a speaker mistakenly uses a word that sounds similar to the intended word but has a very different, often humorous, meaning.',
  [('What is a malapropism?', ['The mistaken use of a word that sounds similar to the intended word but has a different meaning', 'A word with exactly one correct pronunciation', 'A formal word used only in legal documents', 'A word that has no other similar-sounding words'], 0),
   ('What effect does a malapropism often have on a sentence?', ['It creates an unintended and often humorous meaning', 'It always makes the sentence perfectly accurate', 'It removes all meaning from a sentence', 'It is always used intentionally for formal writing'], 0),
   ('Which of these phrases contains a malapropism?', ['For all intensive purposes, we should leave now.', 'For all intents and purposes, we should leave now.', 'We should leave now, for good reason.', 'We should leave immediately without hesitation.'], 0),
   ('Why do malapropisms often occur between words that sound alike?', ['Similar-sounding words can be easily confused in memory or in quick speech, leading a speaker to substitute the wrong one', 'Malapropisms only occur between words with completely different sounds', 'Speakers never confuse words that sound similar to each other', 'Malapropisms are always planned in advance before speaking'], 0),
   ('Why might authors sometimes use malapropisms intentionally when writing dialogue for a character?', ['Intentional malapropisms can add humour and reveal something about a characters personality or level of confidence', 'Malapropisms never reveal anything about a characters personality', 'Authors are never permitted to use incorrect word choices in dialogue', 'Intentional malapropisms always make dialogue less realistic'], 0)]),
M('Probability: Conditional Probability and Real-World Applications',
  'Grade 6 Math strand: conditional probability is the likelihood of an event occurring given that another event has already happened, and it is often used to make more accurate predictions when extra information is available.',
  [('What does conditional probability measure?', ['The likelihood of an event occurring given that another event has already happened', 'The total number of outcomes in a sample space', 'The average of all possible outcomes', 'The likelihood of an event that has no connection to any other event'], 0),
   ('If it is known that a card drawn from a deck is a face card, how does this information affect the probability of it being a king?', ['It changes the probability, since only face cards are now being considered', 'It has no effect on the probability at all', 'It always makes the probability equal to zero', 'It always makes the probability equal to one'], 0),
   ('What is one everyday example where conditional probability could be used?', ['Estimating the chance of rain given that it is already cloudy', 'Counting the total number of days in a year', 'Measuring the length of a table', 'Calculating the area of a rectangle'], 0),
   ('Why does having extra information often change a probability calculation?', ['Extra information can narrow down the possible outcomes being considered, making the estimate more specific and accurate', 'Extra information always makes a probability calculation less accurate', 'Additional information never changes the outcomes being considered', 'Probability calculations always ignore any new information provided'], 0),
   ('Why might conditional probability be useful in fields such as medicine, such as interpreting the result of a medical test?', ['It helps estimate the likelihood of a condition being present given a specific test result, providing more meaningful information than considering the test result alone', 'Medical test results have no connection to probability of any kind', 'Conditional probability cannot be applied to any real-world situation', 'Test results always provide complete certainty with no need for probability'], 0)]),
Sc('Science: Sonar Technology and Mapping the Ocean Floor',
   'Grade 6 Science strand: sonar uses sound waves to detect objects and measure distances underwater, sending out a pulse of sound and calculating distance based on how long the echo takes to return.',
   [('What does sonar use to detect objects underwater?', ['Sound waves', 'Radio signals only', 'Visible light only', 'Magnetic fields'], 0),
    ('How does sonar calculate the distance to an object?', ['By measuring how long it takes for an echo to return after a sound pulse is sent out', 'By measuring the water temperature only', 'By counting the number of waves on the surface', 'By measuring the colour of the water'], 0),
    ('What is one major use of sonar technology?', ['Mapping the ocean floor', 'Measuring air temperature', 'Predicting earthquakes on land', 'Growing crops more efficiently'], 0),
    ('Why is sonar especially useful for exploring the deep ocean, where light cannot easily reach?', ['Sound waves can travel effectively through water even in complete darkness, unlike light, which is quickly absorbed or scattered at depth', 'Sound waves cannot travel through water at all', 'Light travels farther through water than sound does', 'Sonar only works in shallow water near the surface'], 0),
    ('Why might a longer time delay between sending a sonar pulse and receiving its echo indicate a greater distance to an object?', ['Sound travels at a fairly consistent speed through water, so a longer delay means the sound had to travel farther before reflecting back', 'A longer delay always means the object is closer to the sonar source', 'The speed of sound through water constantly changes with no consistent pattern', 'Sonar echoes have no connection to the distance of an object'], 0)]),
SS('Social Studies: The CBC — Canadas Public Broadcaster',
   'Grade 6 Social Studies strand: the Canadian Broadcasting Corporation, or CBC, is a federally funded public broadcaster that provides radio and television programming across the country, including news, entertainment, and content in both English and French.',
   [('What does the acronym CBC stand for?', ['The Canadian Broadcasting Corporation', 'The Canadian Business Council', 'The Central Broadcast Committee', 'The Canadian Bilingual Congress'], 0),
    ('How is the CBC primarily funded?', ['Through federal government funding', 'Entirely through private foreign investors', 'Through provincial lottery revenue only', 'It receives no funding of any kind'], 0),
    ('In which two languages does the CBC provide programming?', ['English and French', 'Spanish and Portuguese', 'Only English', 'Only French'], 0),
    ('Why might a country choose to fund a public broadcaster like the CBC rather than relying only on privately owned media companies?', ['A publicly funded broadcaster can provide programming that serves the public interest, including news and content that might not always be profitable for private companies', 'Public broadcasters are never able to provide news programming', 'Private companies always provide the exact same content as public broadcasters', 'Funding a public broadcaster has no connection to serving public interest'], 0),
    ('Why is it important for the CBC to provide programming in both English and French?', ['Canada has two official languages, and offering content in both helps serve and represent both English-speaking and French-speaking communities across the country', 'Canada has only one official language, so a second language is unnecessary', 'Providing content in two languages has no benefit to Canadian communities', 'The CBC broadcasts only in languages other than English or French'], 0)]),
]),
day(185, [
L('Media Literacy: Analyzing Infographics',
  'Grade 6 Language strand: an infographic combines images, charts, and brief text to present information visually, and analyzing one critically involves checking the accuracy of its data and considering how its design might influence a viewers interpretation.',
  [('What does an infographic combine to present information?', ['Images, charts, and brief text', 'Only a single unlabelled photograph', 'Only handwritten notes with no images', 'A list of unrelated numbers with no visuals'], 0),
   ('What is one important step when critically analyzing an infographic?', ['Checking the accuracy of its data', 'Ignoring all of the images it contains', 'Assuming every infographic is entirely accurate', 'Only reading the title and nothing else'], 0),
   ('What might the design of an infographic influence?', ['A viewers interpretation of the information', 'The actual accuracy of the underlying data', 'The length of the original research study', 'The number of people who created it'], 0),
   ('Why might a poorly designed infographic mislead a viewer even if the underlying data is accurate?', ['Choices such as exaggerated chart scales or misleading images can distort how the information is perceived, even without changing the actual numbers', 'Poor design always makes the underlying data itself inaccurate', 'Infographic design has no effect on how a viewer interprets information', 'A well-designed infographic can never be misleading in any way'], 0),
   ('Why is it useful to check the original source of the data used in an infographic?', ['Verifying the source helps confirm that the information is reliable and has not been taken out of context or altered', 'The original source of data has no connection to its reliability', 'Infographics never include data that comes from an outside source', 'Checking a source always makes an infographic less trustworthy'], 0)]),
M('Geometry: Exterior Angles of Polygons',
  'Grade 6 Math strand: an exterior angle of a polygon is formed by extending one side of the polygon, and the sum of the exterior angles of any convex polygon, one at each vertex, always equals 360 degrees.',
  [('How is an exterior angle of a polygon formed?', ['By extending one side of the polygon', 'By drawing a line through the center of the polygon', 'By connecting two opposite vertices', 'By measuring the area of the polygon'], 0),
   ('What is the sum of the exterior angles of any convex polygon, taking one at each vertex?', ['360 degrees', '180 degrees', '90 degrees', '720 degrees'], 0),
   ('What is the measure of each exterior angle of a regular hexagon?', ['60 degrees', '45 degrees', '90 degrees', '120 degrees'], 0),
   ('Why does the sum of the exterior angles remain 360 degrees regardless of how many sides a convex polygon has?', ['Walking around the entire shape and returning to the starting point and direction always requires turning through a full 360-degree rotation', 'The number of sides always changes the total turning angle needed', 'Exterior angles of a polygon never add up to a consistent total', 'A polygon with more sides always has a larger total of exterior angles'], 0),
   ('Why is knowing that exterior angles sum to 360 degrees useful for finding the exterior angle of a regular polygon with many sides?', ['It allows the measure of each equal exterior angle to be found quickly by dividing 360 degrees by the number of sides', 'The number of sides has no connection to the size of each exterior angle', 'Exterior angles of a regular polygon can never be calculated using this total', 'Dividing 360 degrees by the number of sides only works for irregular polygons'], 0)]),
Sc('Science: The Ozone Layer and Its Protective Role',
   'Grade 6 Science strand: the ozone layer is a region high in Earths atmosphere that absorbs most of the suns harmful ultraviolet radiation, protecting living things on the surface below.',
   [('What does the ozone layer absorb?', ['Most of the suns harmful ultraviolet radiation', 'Most of Earths visible sunlight', 'All forms of precipitation', 'Sound waves travelling through the atmosphere'], 0),
    ('Where is the ozone layer located?', ['High in Earths atmosphere', 'Deep underground', 'At the bottom of the ocean', 'Inside Earths core'], 0),
    ('What does the ozone layer protect living things from?', ['Harmful ultraviolet radiation from the sun', 'Ordinary visible sunlight of any kind', 'All forms of precipitation', 'Changes in wind speed'], 0),
    ('Why was the thinning of the ozone layer, once caused by certain chemicals, considered a serious environmental concern?', ['A thinner ozone layer allows more harmful ultraviolet radiation to reach Earths surface, increasing risks to living things', 'A thinner ozone layer has no effect on the amount of radiation reaching Earth', 'Ultraviolet radiation is completely harmless to all living things', 'The ozone layer has no connection to protecting life on Earth'], 0),
    ('Why is international cooperation, such as agreements to reduce ozone-depleting chemicals, important for protecting the ozone layer?', ['Because the atmosphere circulates globally, chemicals released in one country can affect the ozone layer worldwide, so coordinated action is more effective than isolated efforts', 'Chemicals released in one country never affect the atmosphere anywhere else', 'The ozone layer can be fully protected by a single country acting alone', 'International agreements have no effect on atmospheric chemical levels'], 0)]),
SS('Social Studies: Canadas Mission in Afghanistan',
   'Grade 6 Social Studies strand: Canada took part in a multinational military and reconstruction mission in Afghanistan beginning in 2001, contributing troops and aid as part of an international effort following the September 11 attacks.',
   [('In what year did Canadas mission in Afghanistan begin?', ['2001', '1945', '1989', '2010'], 0),
    ('What kind of mission did Canada take part in Afghanistan?', ['A multinational military and reconstruction mission', 'A purely academic research exchange', 'A trade negotiation mission only', 'A mission with no international partners'], 0),
    ('What global event was closely connected to the start of the mission in Afghanistan?', ['The September 11 attacks', 'The signing of the Treaty of Versailles', 'The fall of the Berlin Wall', 'The Cuban Missile Crisis'], 0),
    ('Why might Canada have chosen to contribute troops and aid to a multinational mission rather than acting alone?', ['Working with international partners can share the responsibilities and resources needed for a large and complex mission', 'Acting alone is always easier than working with international partners', 'Canada is never permitted to participate in missions with other countries', 'Multinational missions never involve sharing responsibilities or resources'], 0),
    ('Why does Canadas involvement in Afghanistan continue to be studied and discussed today?', ['It raises important questions about the goals, costs, and lasting effects of Canadas international military commitments', 'The mission had no lasting effects worth studying', 'Canadas involvement in Afghanistan is no longer discussed by historians', 'International military commitments never raise questions worth studying'], 0)]),
]),
day(186, [
L('Oral Communication: Non-Verbal Communication and Body Language',
  'Grade 6 Language strand: non-verbal communication includes body language, facial expressions, gestures, and posture, which can convey meaning and emotion alongside or even instead of spoken words.',
  [('What is non-verbal communication?', ['Communication that includes body language, facial expressions, gestures, and posture', 'Communication that uses only written text', 'Communication that occurs only over the telephone', 'Communication that uses only numbers'], 0),
   ('What can non-verbal communication convey alongside spoken words?', ['Meaning and emotion', 'Only mathematical data', 'Only written text', 'Nothing beyond the spoken words themselves'], 0),
   ('Which of these is an example of non-verbal communication?', ['Crossing your arms while speaking', 'Writing an email', 'Reading a book silently', 'Typing a text message'], 0),
   ('Why might a listener pay attention to a speakers body language in addition to their words?', ['Body language can reveal additional information about a speakers true feelings or confidence, sometimes clarifying or even contradicting the spoken message', 'Body language never provides any additional information to a listener', 'Spoken words always contain all of the information a listener needs', 'A speakers body language has no connection to their true feelings'], 0),
   ('Why is it important for a public speaker to be aware of their own non-verbal communication during a presentation?', ['Their gestures, posture, and expressions can strengthen or undermine the intended message, so being aware of them helps ensure the presentation is received as intended', 'Non-verbal communication has no effect on how a presentation is received', 'A speakers posture and gestures are never noticed by an audience', 'Being aware of body language always weakens a presentation'], 0)]),
M('Number Sense: Multiplying and Dividing Numbers in Scientific Notation',
  'Grade 6 Math strand: numbers in scientific notation are multiplied or divided by first multiplying or dividing the decimal parts and then adding or subtracting the exponents on the powers of ten.',
  [('When multiplying two numbers in scientific notation, what happens to the exponents on the powers of ten?', ['They are added together', 'They are subtracted', 'They are multiplied together', 'They stay exactly the same'], 0),
   ('What is 2 times 10 to the power of 3, multiplied by 3 times 10 to the power of 2, in scientific notation?', ['6 x 10 to the power of 5', '6 x 10 to the power of 6', '5 x 10 to the power of 5', '6 x 10 to the power of 1'], 0),
   ('When dividing two numbers in scientific notation, what happens to the exponents on the powers of ten?', ['They are subtracted', 'They are added together', 'They are multiplied together', 'They stay exactly the same'], 0),
   ('Why does multiplying numbers in scientific notation involve adding the exponents rather than multiplying them?', ['Multiplying powers of ten with the same base combines the total number of factors of ten, which corresponds to adding their exponents', 'Adding exponents always produces an incorrect result when multiplying', 'Exponents on powers of ten are never affected by multiplication', 'Multiplying numbers in scientific notation always requires subtracting the exponents instead'], 0),
   ('Why is scientific notation especially useful when multiplying or dividing very large or very small numbers?', ['It keeps the calculation manageable by separating the decimal part from the power of ten, avoiding long strings of zeros', 'Scientific notation always makes calculations more difficult to manage', 'Very large or very small numbers can never be expressed in scientific notation', 'Scientific notation removes the need to track any exponents at all'], 0)]),
Sc('Science: Colour Mixing — Additive versus Subtractive Colour',
   'Grade 6 Science strand: additive colour mixing combines coloured light, such as red, green, and blue, to create new colours including white, while subtractive colour mixing combines pigments, which absorb light and produce new colours by removing wavelengths.',
   [('What does additive colour mixing combine?', ['Coloured light', 'Solid pigments only', 'Sound waves of different frequencies', 'Magnetic fields of different strengths'], 0),
    ('What three colours of light are commonly combined in additive colour mixing?', ['Red, green, and blue', 'Red, yellow, and blue', 'Black, white, and gray', 'Orange, purple, and green'], 0),
    ('What does subtractive colour mixing combine?', ['Pigments, which absorb light', 'Sound waves of different frequencies', 'Magnetic fields of different strengths', 'Gases of different densities'], 0),
    ('Why does combining all three primary colours of light in additive mixing produce white light?', ['Combining red, green, and blue light at full intensity includes the full range of visible light wavelengths, which the eye perceives as white', 'Combining coloured light always produces black instead of white', 'Light mixing has no connection to how colour is perceived', 'Only a single colour of light can ever be produced through mixing'], 0),
    ('Why do mixing paints, which use subtractive colour mixing, produce darker colours as more colours are combined, unlike mixing light?', ['Each added pigment absorbs more wavelengths of light, so less light is reflected back, making the resulting colour appear darker', 'Adding more paint colours always makes the mixture appear brighter', 'Pigments reflect every wavelength of light regardless of how many are combined', 'Subtractive and additive colour mixing always produce identical results'], 0)]),
SS('Social Studies: The Indian Act — History and Impact',
   'Grade 6 Social Studies strand: the Indian Act, first passed in 1876, is federal legislation that has governed many aspects of registered First Nations peoples lives, including status, land, and governance, and it remains a significant and controversial part of Canadian law.',
   [('In what year was the Indian Act first passed?', ['1876', '1867', '1931', '1949'], 0),
    ('What does the Indian Act govern for registered First Nations peoples?', ['Aspects of their lives including status, land, and governance', 'Only matters related to international trade', 'Only the design of the national flag', 'Only matters related to space exploration'], 0),
    ('What type of legislation is the Indian Act?', ['Federal legislation', 'A provincial bylaw only', 'An international treaty between two countries', 'A municipal parking regulation'], 0),
    ('Why is the Indian Act often described as controversial?', ['It has historically imposed significant control over First Nations peoples lives without their full consent, including policies that caused lasting harm', 'The Indian Act has never had any effect on First Nations peoples lives', 'The legislation was created entirely by First Nations leaders themselves', 'The Indian Act contains no provisions related to governance or land'], 0),
    ('Why do many advocates today call for reform or replacement of the Indian Act?', ['They argue that greater self-governance and control over their own affairs would better respect First Nations rights and better reflect modern relationships between First Nations and the Canadian government', 'Advocates believe the Indian Act requires no changes of any kind', 'Self-governance has no connection to respecting First Nations rights', 'The Indian Act has already been fully replaced with new legislation'], 0)]),
]),
day(187, [
L('Language Review: The Final Chapter — Grammar, Vocabulary, and Communication Skills',
  'Grade 6 Language strand review: as the capstone lesson completing the full 187-day Grade 6 curriculum, students revisit the subjunctive mood, motifs in literature, writing a speech of introduction, malapropisms, and analyzing infographics.',
  [('What does the subjunctive mood typically express?', ['A wish, suggestion, or a condition that is not currently true', 'A simple statement of fact', 'A command given to a group', 'A question about the past'], 0),
   ('What is a motif?', ['A recurring image, symbol, or idea that appears repeatedly throughout a literary work', 'A single event that happens only once in a story', 'A type of punctuation used in dialogue', 'The title of a book'], 0),
   ('What does a speech of introduction typically present?', ['A guest speaker to an audience', 'An unrelated news story', 'A detailed weather forecast', 'A list of upcoming school events'], 0),
   ('What is a malapropism?', ['The mistaken use of a word that sounds similar to the intended word but has a different meaning', 'A word with exactly one correct pronunciation', 'A formal word used only in legal documents', 'A word that has no other similar-sounding words'], 0),
   ('What does an infographic combine to present information?', ['Images, charts, and brief text', 'Only a single unlabelled photograph', 'Only handwritten notes with no images', 'A list of unrelated numbers with no visuals'], 0)]),
M('Math Review: The Final Chapter — Number Systems, Geometry, and Probability',
  'Grade 6 Math strand review: as the capstone lesson completing the full 187-day Grade 6 curriculum, students revisit modular arithmetic, solving systems of equations by graphing, percentiles, conditional probability, and exterior angles of polygons.',
  [('What does modular arithmetic calculate?', ['The remainder after dividing one number by another', 'The sum of two numbers', 'The square root of a number', 'The average of a list of numbers'], 0),
   ('What does the point of intersection of two graphed lines represent in a system of equations?', ['The solution that satisfies both equations', 'The steepest point on either line', 'The starting point of the first line only', 'A point that satisfies neither equation'], 0),
   ('What does a percentile indicate about a value in a data set?', ['The percentage of values in the data set that fall below it', 'The exact average of the entire data set', 'The largest value found anywhere in the data set', 'The total number of values in the data set'], 0),
   ('What does conditional probability measure?', ['The likelihood of an event occurring given that another event has already happened', 'The total number of outcomes in a sample space', 'The average of all possible outcomes', 'The likelihood of an event that has no connection to any other event'], 0),
   ('How is an exterior angle of a polygon formed?', ['By extending one side of the polygon', 'By drawing a line through the center of the polygon', 'By connecting two opposite vertices', 'By measuring the area of the polygon'], 0)]),
Sc('Science Review: The Final Chapter — Chemistry, Earth Science, and Technology',
   'Grade 6 Science strand review: as the capstone lesson completing the full 187-day Grade 6 curriculum, students revisit crystallization, Earths magnetic field, the Maillard reaction, sonar technology, and the ozone layer.',
   [('What is crystallization?', ['A process in which a dissolved substance separates from a solution and forms a solid with a repeating geometric pattern', 'A process that only occurs inside living cells', 'The complete disappearance of a dissolved substance', 'A process that turns a solid directly into a gas'], 0),
    ('What does Earth behave like, according to scientists studying magnetism?', ['A giant magnet with a magnetic field', 'A completely non-magnetic sphere', 'A magnet only at its exact center', 'An object with no magnetic properties at all'], 0),
    ('What two substances react with each other during the Maillard reaction?', ['Amino acids and sugars', 'Water and salt', 'Oxygen and carbon dioxide', 'Oil and vinegar'], 0),
    ('What does sonar use to detect objects underwater?', ['Sound waves', 'Radio signals only', 'Visible light only', 'Magnetic fields'], 0),
    ('What does the ozone layer absorb?', ['Most of the suns harmful ultraviolet radiation', 'Most of Earths visible sunlight', 'All forms of precipitation', 'Sound waves travelling through the atmosphere'], 0)]),
SS('Social Studies Review: The Final Chapter — Government, Rights, and Canadian History',
   'Grade 6 Social Studies strand review: as the capstone lesson completing the full 187-day Grade 6 curriculum, students revisit Nellie McClung and womens suffrage, equalization payments, the White Paper of 1969, the CBC, and Canadas mission in Afghanistan.',
   [('What cause did Nellie McClung campaign for?', ['Womens right to vote', 'Lower taxes for farmers', 'The construction of new railways', 'Free international trade agreements'], 0),
    ('What are equalization payments?', ['Funds transferred by the federal government to less wealthy provinces', 'Taxes collected exclusively from foreign visitors', 'Loans that provinces must repay to private banks', 'Fees charged to municipalities for road repairs'], 0),
    ('What government document is known as the White Paper of 1969?', ['A federal policy proposal that would have eliminated the Indian Act and existing treaty rights', 'A treaty signed between Canada and another country', 'A provincial budget report', 'A report on Canadian trade with Europe'], 0),
    ('What does the acronym CBC stand for?', ['The Canadian Broadcasting Corporation', 'The Canadian Business Council', 'The Central Broadcast Committee', 'The Canadian Bilingual Congress'], 0),
    ('In what year did Canadas mission in Afghanistan begin?', ['2001', '1945', '1989', '2010'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_181_187)
    append_to(6, g6_181_187)
