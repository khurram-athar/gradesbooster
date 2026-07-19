#!/usr/bin/env python3
"""Grade 7, Days 81-90 -- extends Grade 7 from 80 to 90 days. Topics chosen
to avoid any overlap with the existing Day 1-80 set (see data/grade7.json):
motifs, personal manifestos, nominalization, neologisms, logical
fallacies, letters of recommendation, algorithmic content curation,
absolute phrases, frame narratives; solving systems by substitution,
scientific notation operations, probability simulations, perpendicular
bisectors, correlation vs causation, multiplying binomials, credit
scores, composite solids with curved surfaces, divisibility and primes;
ecosystem succession, sound in musical instruments, green architecture,
combustion chemistry, bioluminescence, antibiotic resistance, lift and
drag, genetic variation, space weather; the Berlin Airlift, the Suez
Crisis and Canadian peacekeeping origins, Canadian health care history,
global water rights, e-commerce, the auto industry, daylight saving
time, space law, and credit unions.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L7 = 'https://tvolearn.com/pages/grade-7-language'
M7 = 'https://tvolearn.com/pages/grade-7-mathematics'
S7 = 'https://tvolearn.com/pages/grade-7-science-and-technology'
SS7 = 'https://tvolearn.com/pages/grade-7-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 7 Language',
    'TVO Learn: Grade 7 Mathematics',
    'TVO Learn: Grade 7 Science and Technology',
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


def _rebalance_answer_positions(days, seed=20260926):
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


g7_81_90 = [
day(81, [
L('Reading: Analyzing Motifs in Literature',
  'Grade 7 Language strand: a motif is a recurring element, such as an image, phrase, or idea, that appears throughout a text and reinforces its central themes.',
  [('What do we call a recurring element, like an image or idea, that reinforces a text’s themes?', ['A motif', 'A concept unrelated to reading', 'A footnote', 'A citation'], 0),
   ('Does a motif appear once in a text, or repeatedly throughout it?', ['Repeatedly throughout it', 'Only once, at the very beginning', 'A concept unrelated to motifs', 'Only in the final chapter'], 0),
   ('Can a recurring image, like birds appearing throughout a novel, function as a motif?', ['Yes', 'No, images can never function as a motif', 'A concept unrelated to reading', 'Motifs can only ever be single words'], 0),
   ('Why might an author repeat a specific image or phrase throughout a story?', ['To reinforce a central theme or idea across the narrative', 'Repetition never adds any meaning to a story', 'This concept has no connection to literature', 'Authors never intentionally repeat any elements'], 0),
   ('Why is identifying a motif a useful skill when analyzing a novel’s deeper meaning?', ['It can reveal patterns that connect to the story’s central themes', 'Motifs never connect to a story’s themes', 'This concept has no relevance to reading comprehension', 'A motif only ever appears in poetry, never in novels'], 0)]),
M('Solving Systems of Equations by Substitution',
  'Grade 7 Math strand: the substitution method solves a system of two equations by solving one equation for a variable, then substituting that expression into the other equation.',
  [('In the substitution method, what do you do first with one of the equations?', ['Solve it for a single variable', 'Graph both equations immediately', 'A concept unrelated to systems of equations', 'Multiply both equations together'], 0),
   ('After solving one equation for a variable, what do you do with that expression?', ['Substitute it into the other equation', 'Ignore it completely', 'A concept unrelated to substitution', 'Divide it by zero'], 0),
   ('If y equals x plus 2, and you substitute this into another equation, what are you solving for?', ['The value of x', 'The value of y only, ignoring x', 'A concept unrelated to substitution', 'Nothing at all'], 0),
   ('Why might substitution be a useful method for solving a system of equations?', ['It can turn two equations with two variables into one equation with a single variable', 'Substitution never simplifies a system of equations', 'This concept has no connection to algebra', 'Substitution only works when equations have no variables at all'], 0),
   ('If x plus y equals 10 and y equals 4, what is the value of x after substitution?', ['6', '4', '10', '14'], 0)]),
Sc('Science: Ecosystem Succession: How Ecosystems Change Over Time',
   'Grade 7 Science strand: ecosystem succession is the gradual process by which an ecosystem changes over time, such as a bare patch of land slowly developing into a forest through different stages.',
   [('What is ecosystem succession?', ['The gradual process by which an ecosystem changes over time', 'A process where ecosystems never change at all', 'A concept unrelated to ecology', 'A single, instant event with no stages'], 0),
    ('Can a bare patch of land eventually develop into a forest through succession?', ['Yes', 'No, bare land can never develop into anything else', 'A concept unrelated to succession', 'Succession only happens in the ocean'], 0),
    ('Does ecosystem succession happen through different stages over time?', ['Yes', 'No, succession happens all at once with no stages', 'A concept unrelated to succession', 'Succession has no connection to time at all'], 0),
    ('Why might small plants, like grasses, often appear before large trees during succession?', ['Small plants can often survive in poor soil conditions and help prepare the way for larger plants', 'Large trees always appear before any other plants', 'This concept has no connection to ecosystem succession', 'Small plants never grow before larger ones'], 0),
    ('Why is understanding ecosystem succession useful for restoring a damaged habitat?', ['It helps scientists predict how an ecosystem might naturally recover over time', 'Succession has no connection to habitat restoration', 'This concept has no relevance to science', 'Damaged habitats never go through any stages of recovery'], 0)]),
SS('Social Studies: The Berlin Airlift and Cold War Tensions',
   'Grade 7 Social Studies strand: the Berlin Airlift was a major Cold War event in which Western countries flew supplies into West Berlin after the Soviet Union blocked land routes into the city.',
   [('What was the Berlin Airlift?', ['An operation flying supplies into West Berlin after a Soviet blockade', 'A modern airline company', 'A concept unrelated to history', 'A type of sporting event'], 0),
    ('Which country blocked land routes into West Berlin, leading to the airlift?', ['The Soviet Union', 'Canada', 'A concept unrelated to the Berlin Airlift', 'France'], 0),
    ('Did Western countries respond to the blockade by flying supplies into West Berlin?', ['Yes', 'No, they did nothing in response to the blockade', 'A concept unrelated to the Berlin Airlift', 'They only responded by sending supplies over land'], 0),
    ('Why might the Berlin Airlift be seen as an important moment in Cold War history?', ['It showed how far countries would go to support allies without direct military conflict', 'The Berlin Airlift had no connection to the Cold War', 'This concept has no relevance to social studies', 'The airlift caused immediate war between the two sides'], 0),
    ('Why might delivering supplies by air, rather than by land, have been a significant challenge?', ['Airlifts require careful planning and resources to move large amounts of supplies quickly and safely', 'Delivering supplies by air was never any more difficult than by land', 'This concept has no connection to the Berlin Airlift', 'Airplanes were never involved in the Berlin Airlift at all'], 0)]),
]),

day(82, [
L('Writing: Writing a Personal Manifesto',
  'Grade 7 Language strand: a personal manifesto is a piece of writing that expresses an individual’s core beliefs, values, and goals, often written with a confident and declarative tone.',
  [('What kind of writing expresses an individual’s core beliefs and values?', ['A personal manifesto', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Is a personal manifesto often written with a confident, declarative tone?', ['Yes', 'No, it is always written in a hesitant, uncertain tone', 'A concept unrelated to writing', 'Tone never matters in a personal manifesto'], 0),
   ('Might a personal manifesto include a person’s goals for the future?', ['Yes', 'No, manifestos never include any future goals', 'A concept unrelated to personal manifestos', 'Goals are only found in business documents, never manifestos'], 0),
   ('Why might someone write a personal manifesto?', ['To clarify and express what they believe in and value most', 'Personal manifestos serve no real purpose', 'This concept has no connection to writing', 'Manifestos are only ever written by famous historical figures'], 0),
   ('Which of these sentences sounds most like it belongs in a personal manifesto?', ['I believe kindness should guide every decision I make.', 'The chemical symbol for iron is Fe.', 'Add 6 and 3 to get 9.', 'The capital of France is Paris.'], 0)]),
M('Scientific Notation: Operations',
  'Grade 7 Math strand: students learn to multiply and divide numbers written in scientific notation, keeping track of the exponent of 10 while multiplying or dividing the decimal parts.',
  [('When multiplying two numbers in scientific notation, what happens to the exponents of 10?', ['They are added together', 'They are subtracted', 'A concept unrelated to scientific notation', 'They are multiplied together'], 0),
   ('When dividing two numbers in scientific notation, what happens to the exponents of 10?', ['They are subtracted', 'They are added together', 'A concept unrelated to scientific notation', 'They are divided'], 0),
   ('What is the result of multiplying (2 times 10 to the 3rd) by (3 times 10 to the 2nd)?', ['6 times 10 to the 5th', '6 times 10 to the 6th', '5 times 10 to the 5th', '6 times 10 to the 1st'], 0),
   ('Why is scientific notation useful when multiplying very large or very small numbers?', ['It simplifies the process by separating the exponent work from the decimal work', 'Scientific notation never simplifies any calculations', 'This concept has no connection to math', 'Scientific notation only works with small, simple numbers'], 0),
   ('What is the result of dividing (8 times 10 to the 5th) by (2 times 10 to the 2nd)?', ['4 times 10 to the 3rd', '4 times 10 to the 7th', '6 times 10 to the 3rd', '4 times 10 to the 2nd'], 0)]),
Sc('Science: The Physics of Sound in Musical Instruments',
   'Grade 7 Science strand: musical instruments produce sound through vibrations, with the length, tension, or thickness of a vibrating string or column of air determining the pitch of the sound.',
   [('How do musical instruments produce sound?', ['Through vibrations', 'Through complete silence', 'A concept unrelated to sound', 'Without any physical movement at all'], 0),
    ('Name one factor that can determine the pitch of a vibrating string, such as its length.', ['Its length', 'A concept unrelated to sound', 'Its colour', 'Its smell'], 0),
    ('Does a shorter, tighter string typically produce a higher or lower pitch?', ['A higher pitch', 'A lower pitch', 'A concept unrelated to sound', 'No pitch at all'], 0),
    ('Why might a guitar player press down on different parts of a string to change the note?', ['Shortening the vibrating length of the string changes its pitch', 'Pressing on a string never changes the pitch of a note', 'This concept has no connection to sound physics', 'Only the guitar’s colour affects its pitch'], 0),
    ('Why do wind instruments, like flutes, use columns of air rather than strings to produce sound?', ['The vibrating air column inside the instrument creates the sound, and its length affects pitch', 'Wind instruments never actually produce any sound', 'This concept has no connection to physics', 'Wind instruments rely on strings just like guitars'], 0)]),
SS('Social Studies: The Suez Crisis and Canadian Peacekeeping Origins',
   'Grade 7 Social Studies strand: the Suez Crisis of 1956 was an international conflict that led Canadian diplomat Lester B. Pearson to propose the first large-scale United Nations peacekeeping force.',
   [('In what year did the Suez Crisis occur?', ['1956', '1867', '1945', '2001'], 0),
    ('Which Canadian diplomat proposed the first large-scale UN peacekeeping force during the Suez Crisis?', ['Lester B. Pearson', 'A concept unrelated to Canadian history', 'A fictional diplomat', 'A diplomat from a different country'], 0),
    ('Did the Suez Crisis lead to the creation of a UN peacekeeping force?', ['Yes', 'No, peacekeeping has no connection to the Suez Crisis', 'A concept unrelated to the Suez Crisis', 'The crisis had no resolution of any kind'], 0),
    ('Why might Canada’s role in resolving the Suez Crisis be considered historically significant?', ['It marked the beginning of Canada’s long tradition of international peacekeeping', 'Canada played no role at all in resolving the Suez Crisis', 'This concept has no relevance to Canadian history', 'Peacekeeping began in a completely different country'], 0),
    ('Why might peacekeeping forces be useful for resolving international conflicts?', ['They can help maintain stability and prevent further conflict between opposing sides', 'Peacekeeping forces never actually help resolve any conflict', 'This concept has no connection to international relations', 'Peacekeeping forces only ever make conflicts worse'], 0)]),
]),

day(83, [
L('Grammar: Nominalization and Sentence Complexity',
  'Grade 7 Language strand: nominalization turns a verb or adjective into a noun, such as changing decide into decision, often used in formal writing to create more complex, abstract sentences.',
  [('What does nominalization do to a verb or adjective?', ['Turns it into a noun', 'Turns it into a question', 'A concept unrelated to grammar', 'Removes it from the sentence'], 0),
   ('Which word is the nominalized form of the verb decide?', ['Decision', 'Deciding', 'Decisive', 'Decided'], 0),
   ('Is nominalization often used in formal or informal writing?', ['Formal writing', 'Informal writing only', 'A concept unrelated to nominalization', 'Neither formal nor informal writing'], 0),
   ('Which sentence uses nominalization?', ['The committee’s decision surprised everyone.', 'The committee decided quickly.', 'They will decide tomorrow.', 'Deciding is hard sometimes.'], 0),
   ('Why might a writer use nominalization in an academic essay?', ['It can create a more formal, abstract, and complex tone', 'Nominalization always makes writing simpler and less formal', 'This concept has no connection to writing style', 'Academic essays never use nominalized words'], 0)]),
M('Probability: Simulations and Random Sampling',
  'Grade 7 Math strand: a simulation models a real-world situation using repeated random trials, such as flipping a coin many times, to estimate the probability of an event.',
  [('What does a simulation use to model a real-world situation?', ['Repeated random trials', 'A single guess with no trials', 'A concept unrelated to probability', 'Only historical data with no trials at all'], 0),
   ('Can flipping a coin many times be an example of a simulation?', ['Yes', 'No, coin flips can never be used in a simulation', 'A concept unrelated to simulations', 'Simulations never involve any random trials'], 0),
   ('Why might running more trials in a simulation give a more accurate estimate of probability?', ['More trials can better reflect the true likelihood of an event over time', 'Running more trials never improves the accuracy of an estimate', 'This concept has no connection to probability', 'Fewer trials always give a more accurate estimate'], 0),
   ('What is random sampling used for in a simulation?', ['Selecting outcomes without bias to represent real possibilities', 'Choosing only the outcomes you want to see', 'A concept unrelated to sampling', 'Ignoring all randomness completely'], 0),
   ('Why might scientists use a simulation instead of testing something in real life?', ['A simulation can model a situation quickly, safely, or when real-life testing is impractical', 'Simulations never provide any useful information', 'This concept has no connection to probability', 'Real-life testing is always easier than running a simulation'], 0)]),
Sc('Science: Green Architecture and Sustainable Building',
   'Grade 7 Science strand: green architecture designs buildings to reduce environmental impact, using strategies such as solar panels, efficient insulation, and materials that reduce energy use.',
   [('What does green architecture aim to reduce?', ['Environmental impact', 'The size of a building only', 'A concept unrelated to architecture', 'The number of windows in a building'], 0),
    ('Name one strategy used in green architecture, such as solar panels.', ['Solar panels', 'A concept unrelated to green architecture', 'Wasting as much energy as possible', 'Ignoring insulation completely'], 0),
    ('Can efficient insulation help reduce a building’s energy use?', ['Yes', 'No, insulation has no connection to energy use', 'A concept unrelated to green architecture', 'Insulation always increases energy use'], 0),
    ('Why might a building with solar panels use less energy from traditional power sources?', ['Solar panels can generate their own electricity from sunlight', 'Solar panels never generate any usable electricity', 'This concept has no connection to green architecture', 'Solar panels only work at night'], 0),
    ('Why is green architecture becoming more common in new construction projects?', ['It can help reduce environmental impact and lower long-term energy costs', 'Green architecture has no real benefit to builders or the environment', 'This concept has no relevance to science', 'Green architecture always costs more with no benefits at all'], 0)]),
SS('Social Studies: The History of Canadian Health Care',
   'Grade 7 Social Studies strand: Canada’s public health care system, often called Medicare, developed over the mid-1900s to provide medical coverage for all Canadians, regardless of their ability to pay.',
   [('What is Canada’s public health care system often called?', ['Medicare', 'A concept unrelated to Canadian history', 'A private insurance company', 'A hospital chain'], 0),
    ('Does Medicare provide medical coverage for all Canadians, regardless of ability to pay?', ['Yes', 'No, only wealthy citizens are covered', 'A concept unrelated to health care', 'Medicare has no connection to medical coverage'], 0),
    ('Around what time period did Canada’s public health care system develop?', ['The mid-1900s', 'The 1600s', 'A concept unrelated to Canadian history', 'The 2020s'], 0),
    ('Why might a public health care system be considered important for a country’s citizens?', ['It can provide access to medical care regardless of a person’s income', 'Public health care has no benefit to citizens', 'This concept has no relevance to social studies', 'Health care access never depends on a person’s income in any country'], 0),
    ('Why might the development of Medicare be considered a significant milestone in Canadian history?', ['It reflects a major shift toward ensuring health care access for all Canadians', 'Medicare had no significant impact on Canadian society', 'This concept has no connection to Canadian history', 'Health care in Canada has never changed over time'], 0)]),
]),

day(84, [
L('Vocabulary: Neologisms and Newly Coined Words',
  'Grade 7 Language strand: a neologism is a newly coined word or phrase, often created to describe new technology, culture, or ideas, such as selfie or blog.',
  [('What do we call a newly coined word or phrase?', ['A neologism', 'A concept unrelated to vocabulary', 'A synonym', 'A homophone'], 0),
   ('Which of these is an example of a neologism created to describe new technology?', ['Blog', 'Apple', 'Book', 'Tree'], 0),
   ('Are neologisms often created to describe new technology, culture, or ideas?', ['Yes', 'No, neologisms are never connected to new ideas', 'A concept unrelated to neologisms', 'Neologisms only describe ancient concepts'], 0),
   ('Why might a neologism like selfie become widely used in everyday language?', ['It fills a need to describe a new behaviour or object that did not previously have a common name', 'Neologisms are never actually adopted into everyday language', 'This concept has no connection to vocabulary', 'New words are never created to describe modern technology'], 0),
   ('Why do dictionaries sometimes add neologisms after they become widely used?', ['Dictionaries aim to reflect how language is actually used by people', 'Dictionaries never add any new words at all', 'This concept has no connection to vocabulary', 'Neologisms are removed from language once they are created'], 0)]),
M('Geometry: Constructing Perpendicular Bisectors',
  'Grade 7 Math strand: a perpendicular bisector is a line that crosses a segment at its midpoint, forming right angles, and can be constructed using a compass and straightedge.',
  [('What does a perpendicular bisector cross a segment at?', ['Its midpoint', 'One of its endpoints', 'A concept unrelated to geometry', 'A random point outside the segment'], 0),
   ('Does a perpendicular bisector form right angles with the segment it crosses?', ['Yes', 'No, it never forms right angles', 'A concept unrelated to perpendicular bisectors', 'It always forms a straight line with no angle at all'], 0),
   ('What tools can be used to construct a perpendicular bisector?', ['A compass and straightedge', 'Only a ruler with no compass', 'A concept unrelated to construction', 'A protractor alone, with no other tool'], 0),
   ('Why might a perpendicular bisector be useful for finding the exact centre of a circle?', ['Perpendicular bisectors of chords in a circle intersect at the circle’s centre', 'Perpendicular bisectors have no connection to circles', 'This concept has no connection to geometry', 'The centre of a circle can never be found using construction'], 0),
   ('If a segment is 10 cm long, where would its perpendicular bisector cross it?', ['At the 5 cm mark', 'At the very start of the segment', 'At the very end of the segment', 'At the 10 cm mark'], 0)]),
Sc('Science: The Chemistry of Combustion',
   'Grade 7 Science strand: combustion is a chemical reaction where a fuel reacts with oxygen, releasing energy as heat and light, such as when wood burns in a campfire.',
   [('What is combustion?', ['A chemical reaction where fuel reacts with oxygen, releasing energy', 'A process that only involves ice melting', 'A concept unrelated to chemistry', 'A reaction that never releases any energy'], 0),
    ('What two things react together during combustion?', ['Fuel and oxygen', 'Only water', 'A concept unrelated to combustion', 'Only ice and snow'], 0),
    ('Does combustion release energy as heat and light?', ['Yes', 'No, combustion never releases any energy', 'A concept unrelated to combustion', 'Combustion only absorbs energy, never releases it'], 0),
    ('Why does a campfire need a steady supply of oxygen to keep burning?', ['Combustion requires oxygen to react with the fuel and sustain the reaction', 'Fires never actually need any oxygen to keep burning', 'This concept has no connection to combustion', 'Oxygen prevents combustion from happening at all'], 0),
    ('Why is understanding combustion important for fire safety?', ['Knowing what fuels a fire can help people prevent or safely extinguish it', 'Combustion has no connection to fire safety', 'This concept has no relevance to science', 'Fires can never actually be prevented or put out'], 0)]),
SS('Social Studies: Water Rights and Access Around the World',
   'Grade 7 Social Studies strand: access to clean, safe drinking water varies greatly around the world, with some regions facing water scarcity while others have widespread water infrastructure.',
   [('Does access to clean drinking water vary around the world?', ['Yes', 'No, every region has exactly the same access to water', 'A concept unrelated to global issues', 'Water access has no connection to different regions'], 0),
    ('What do we call a situation where a region does not have enough available water?', ['Water scarcity', 'Water abundance', 'A concept unrelated to water access', 'A trade agreement'], 0),
    ('Can widespread water infrastructure help provide reliable access to clean water?', ['Yes', 'No, infrastructure never affects water access', 'A concept unrelated to water rights', 'Infrastructure only affects electricity, never water'], 0),
    ('Why might a region with limited rainfall face greater challenges with water access?', ['Less rainfall can mean less available fresh water for drinking, farming, and other uses', 'Rainfall has no connection to a region’s water access', 'This concept has no relevance to social studies', 'Every region receives the exact same amount of rainfall'], 0),
    ('Why might international organizations work to improve water access in regions facing scarcity?', ['Reliable access to clean water is essential for health, agriculture, and daily life', 'Water access has no connection to health or daily life', 'This concept has no relevance to global issues', 'International organizations never focus on water access at all'], 0)]),
]),

day(85, [
L('Reading: Evaluating Logical Fallacies in Arguments',
  'Grade 7 Language strand: a logical fallacy is a flaw in reasoning that weakens an argument, such as a hasty generalization, which draws a broad conclusion from very limited evidence.',
  [('What do we call a flaw in reasoning that weakens an argument?', ['A logical fallacy', 'A concept unrelated to reading', 'A citation', 'A footnote'], 0),
   ('What is a hasty generalization?', ['Drawing a broad conclusion from very limited evidence', 'Drawing a careful conclusion from extensive evidence', 'A concept unrelated to logical fallacies', 'A conclusion that always uses complete and thorough evidence'], 0),
   ('Can identifying logical fallacies help readers evaluate the strength of an argument?', ['Yes', 'No, logical fallacies never affect how strong an argument is', 'A concept unrelated to reading', 'Fallacies always make an argument stronger'], 0),
   ('Which of these is an example of a hasty generalization?', ['I met two rude people from that city, so everyone there must be rude.', 'I researched many sources before forming my opinion.', 'The study included a large, diverse sample of participants.', 'The data was collected over several years from multiple regions.'], 0),
   ('Why is it important for readers to recognize logical fallacies in persuasive writing?', ['It helps them evaluate whether an argument is actually well-supported', 'Recognizing fallacies never helps with evaluating an argument', 'This concept has no connection to reading comprehension', 'Every argument in persuasive writing is always completely valid'], 0)]),
M('Data: Correlation vs Causation',
  'Grade 7 Math strand: correlation describes a relationship between two variables, while causation means one variable directly causes a change in another, a stronger claim that requires more evidence.',
  [('What does correlation describe?', ['A relationship between two variables', 'A concept unrelated to data', 'The exact cause of an event', 'A single, unrelated fact'], 0),
   ('What does causation mean?', ['One variable directly causes a change in another', 'Two variables have absolutely no connection at all', 'A concept unrelated to data analysis', 'Correlation and causation always mean the exact same thing'], 0),
   ('Does correlation alone prove that one variable causes another?', ['No', 'Yes, correlation always proves causation', 'A concept unrelated to data', 'Correlation and causation are identical concepts'], 0),
   ('If ice cream sales and drowning incidents both increase in the summer, does that mean ice cream causes drowning?', ['No, both are likely related to a third factor, like warmer weather', 'Yes, ice cream directly causes drowning', 'A concept unrelated to correlation and causation', 'This proves a direct cause-and-effect relationship'], 0),
   ('Why is it important to understand the difference between correlation and causation when interpreting data?', ['Mistaking correlation for causation could lead to incorrect conclusions', 'The two concepts are always interchangeable with no difference', 'This concept has no connection to data analysis', 'Correlation and causation never need to be distinguished'], 0)]),
Sc('Science: Bioluminescence and Deep-Sea Life',
   'Grade 7 Science strand: bioluminescence, the ability to produce light through a chemical reaction, is common among deep-sea organisms, helping them survive in an environment with little to no sunlight.',
   [('What is bioluminescence?', ['The ability to produce light through a chemical reaction', 'A process where organisms absorb sunlight only', 'A concept unrelated to biology', 'A process that only happens on land'], 0),
    ('Is bioluminescence common among deep-sea organisms?', ['Yes', 'No, bioluminescence is never found in the deep sea', 'A concept unrelated to deep-sea life', 'Bioluminescence only occurs in shallow, sunny waters'], 0),
    ('Does the deep sea receive little to no sunlight?', ['Yes', 'No, the deep sea receives the same sunlight as the surface', 'A concept unrelated to ocean zones', 'The deep sea is always brightly lit by the sun'], 0),
    ('Why might a deep-sea organism use bioluminescence to attract prey?', ['A glowing light could lure curious prey close enough to catch in the dark', 'Bioluminescence never helps attract any prey', 'This concept has no connection to biology', 'Deep-sea organisms never need to attract prey'], 0),
    ('Why do scientists find studying bioluminescent deep-sea organisms valuable?', ['Understanding how they produce light could lead to new scientific or medical discoveries', 'Bioluminescent organisms have no scientific value at all', 'This concept has no relevance to science', 'Everything about bioluminescence has already been fully discovered'], 0)]),
SS('Social Studies: The Rise of E-Commerce and Its Economic Impact',
   'Grade 7 Social Studies strand: e-commerce, the buying and selling of goods online, has rapidly grown in recent decades, changing how businesses operate and how consumers shop.',
   [('What is e-commerce?', ['The buying and selling of goods online', 'A type of in-person farmers market only', 'A concept unrelated to the economy', 'A government program with no connection to shopping'], 0),
    ('Has e-commerce grown rapidly in recent decades?', ['Yes', 'No, e-commerce has stayed exactly the same size for centuries', 'A concept unrelated to e-commerce', 'E-commerce has actually decreased over time'], 0),
    ('Has e-commerce changed how consumers shop?', ['Yes', 'No, e-commerce has had no effect on shopping habits', 'A concept unrelated to e-commerce', 'Consumers only ever shop in physical stores today'], 0),
    ('Why might a small local business choose to sell products online through e-commerce?', ['It can reach a much larger group of potential customers beyond their local area', 'Selling online never helps a business reach more customers', 'This concept has no connection to e-commerce', 'Small businesses are never allowed to sell products online'], 0),
    ('Why might the growth of e-commerce create challenges for traditional brick-and-mortar stores?', ['Some customers may prefer the convenience of shopping online instead of visiting in person', 'E-commerce has no effect on how customers choose to shop', 'This concept has no relevance to social studies', 'Traditional stores are never affected by online competition'], 0)]),
]),

day(86, [
L('Writing: Writing a Letter of Recommendation',
  'Grade 7 Language strand: a letter of recommendation describes a person’s strengths and qualifications, often written to support their application for a job, program, or opportunity.',
  [('What kind of letter describes a person’s strengths to support an application?', ['A letter of recommendation', 'A concept unrelated to writing', 'A grocery list', 'A weather report'], 0),
   ('Might a letter of recommendation be written to support someone’s job application?', ['Yes', 'No, letters of recommendation are never used for job applications', 'A concept unrelated to writing', 'Job applications never require any supporting letters'], 0),
   ('Should a letter of recommendation include specific examples of a person’s strengths?', ['Yes', 'No, specific examples are never included', 'A concept unrelated to writing', 'Only vague, general statements should be included'], 0),
   ('Why might a specific example strengthen a letter of recommendation more than a general statement?', ['A specific example provides concrete evidence of a person’s abilities', 'Specific examples never add any value to a recommendation', 'This concept has no connection to writing', 'General statements are always more convincing than specific examples'], 0),
   ('Which of these is most likely a sentence from a letter of recommendation?', ['I have seen her consistently lead group projects with confidence and care.', 'Add 7 and 8 to get 15.', 'The chemical symbol for sodium is Na.', 'Once upon a time, in a faraway kingdom.'], 0)]),
M('Multiplying a Binomial by a Binomial',
  'Grade 7 Math strand: students learn to multiply two binomials, such as (x plus 2) times (x plus 3), by multiplying each term in the first binomial by each term in the second.',
  [('What is (x plus 2) times (x plus 3) equal to?', ['x squared plus 5x plus 6', 'x squared plus 6x plus 5', 'x squared plus 2x plus 3', '2x plus 6'], 0),
   ('When multiplying two binomials, how many multiplications are needed in total?', ['Four', 'Two', 'A concept unrelated to multiplying binomials', 'One'], 0),
   ('What is (x plus 1) times (x plus 4) equal to?', ['x squared plus 5x plus 4', 'x squared plus 4x plus 1', 'x squared plus 1x plus 4', '2x plus 5'], 0),
   ('Why is it important to combine like terms after multiplying two binomials?', ['It simplifies the expression into its most compact and clear form', 'Combining like terms never simplifies an expression', 'This concept has no connection to algebra', 'Like terms should always be kept separate and never combined'], 0),
   ('What is (x minus 2) times (x plus 5) equal to?', ['x squared plus 3x minus 10', 'x squared plus 10x minus 3', 'x squared minus 3x plus 10', 'x squared plus 7x minus 10'], 0)]),
Sc('Science: Antibiotic Resistance: A Modern Challenge',
   'Grade 7 Science strand: antibiotic resistance occurs when bacteria evolve to survive medicines designed to kill them, making some infections harder to treat and posing a growing public health challenge.',
   [('What is antibiotic resistance?', ['When bacteria evolve to survive medicines designed to kill them', 'A process where bacteria are instantly destroyed by every medicine', 'A concept unrelated to biology', 'A type of vaccine'], 0),
    ('Can antibiotic resistance make some infections harder to treat?', ['Yes', 'No, antibiotic resistance never affects how infections are treated', 'A concept unrelated to antibiotic resistance', 'Resistant bacteria are always easier to treat'], 0),
    ('Is antibiotic resistance considered a growing public health challenge?', ['Yes', 'No, it has never been considered a challenge at all', 'A concept unrelated to public health', 'Antibiotic resistance was solved long ago with no remaining concern'], 0),
    ('Why might overusing antibiotics contribute to antibiotic resistance?', ['Frequent use gives bacteria more opportunities to evolve and survive the medicine', 'Overusing antibiotics has no connection to resistance', 'This concept has no connection to biology', 'Using antibiotics less often always increases resistance instead'], 0),
    ('Why is it important for people to finish a full course of prescribed antibiotics?', ['Stopping early might allow surviving, potentially resistant bacteria to multiply', 'Finishing a course of antibiotics has no effect on resistance', 'This concept has no relevance to science', 'Antibiotics work exactly the same whether or not the full course is finished'], 0)]),
SS('Social Studies: Canada’s Auto Industry and Manufacturing History',
   'Grade 7 Social Studies strand: Canada’s auto industry, centred largely in Ontario, has played a major role in the country’s manufacturing economy since the early 1900s.',
   [('In which province has Canada’s auto industry largely been centred?', ['Ontario', 'A concept unrelated to Canada', 'British Columbia', 'Nova Scotia'], 0),
    ('Has Canada’s auto industry played a major role in the country’s economy?', ['Yes', 'No, the auto industry has no connection to Canada’s economy', 'A concept unrelated to Canadian industry', 'The auto industry has never existed in Canada'], 0),
    ('Around what time period did Canada’s auto industry begin to grow significantly?', ['The early 1900s', 'The 1600s', 'A concept unrelated to Canadian history', 'The 2020s'], 0),
    ('Why might a strong auto manufacturing industry benefit a region’s economy?', ['It can create many jobs and support related industries, like parts suppliers', 'Manufacturing industries never create any jobs', 'This concept has no connection to social studies', 'A strong auto industry always harms the local economy'], 0),
    ('Why might changes in global manufacturing trends affect Canada’s auto industry today?', ['Shifts in technology, trade, and competition can change where and how vehicles are produced', 'Global manufacturing trends never affect any single country’s industry', 'This concept has no relevance to social studies', 'Canada’s auto industry has never changed since it began'], 0)]),
]),

day(87, [
L('Media Literacy: Analyzing Algorithmic Content Curation',
  'Grade 7 Language strand: many apps and websites use algorithms to decide what content to show users, often based on their past activity, which can shape what information and opinions someone sees.',
  [('What do many apps and websites use to decide what content to show users?', ['Algorithms', 'A concept unrelated to media literacy', 'Random guessing with no pattern', 'A single employee choosing manually for every user'], 0),
   ('Is content shown to users often based on their past activity?', ['Yes', 'No, past activity never affects what content is shown', 'A concept unrelated to algorithms', 'Content shown to users is always completely random'], 0),
   ('Can algorithms shape what information and opinions someone is exposed to?', ['Yes', 'No, algorithms have no effect on what a person sees', 'A concept unrelated to media literacy', 'Every user sees the exact same content regardless of any algorithm'], 0),
   ('Why might two people searching the same topic online see very different results?', ['Algorithms may personalize results based on each person’s past online activity', 'Search results are always identical for every single user', 'This concept has no connection to algorithmic curation', 'Algorithms never take into account any personal activity'], 0),
   ('Why is it important for people to be aware of how algorithms curate the content they see?', ['It can help them understand that their online experience may be shaped by personalized filtering', 'Awareness of algorithms never changes how someone understands their online experience', 'This concept has no relevance to media literacy', 'Algorithms have no influence on what people believe or see online'], 0)]),
M('Financial Literacy: Understanding Credit Scores',
  'Grade 7 Math strand: a credit score is a number that reflects how reliably a person has repaid borrowed money in the past, affecting their ability to get loans or lower interest rates in the future.',
  [('What does a credit score reflect?', ['How reliably a person has repaid borrowed money in the past', 'A person’s exact age', 'A concept unrelated to finance', 'A person’s favourite hobbies'], 0),
   ('Can a credit score affect a person’s ability to get a loan?', ['Yes', 'No, credit scores have no connection to loans', 'A concept unrelated to credit scores', 'Loans are never affected by a person’s financial history'], 0),
   ('Might a higher credit score help someone qualify for a lower interest rate?', ['Yes', 'No, interest rates are never affected by credit scores', 'A concept unrelated to credit scores', 'A higher credit score always leads to a higher interest rate'], 0),
   ('Why might paying bills on time help build a strong credit score?', ['Consistent, reliable repayment history is a key factor in calculating a credit score', 'Paying bills on time never affects a credit score', 'This concept has no connection to financial literacy', 'Credit scores are calculated completely at random'], 0),
   ('Why is understanding credit scores useful knowledge for planning future major purchases, like a car?', ['A good credit score can make it easier and cheaper to borrow money when needed', 'Credit scores have no connection to major purchases', 'This concept has no relevance to financial literacy', 'Major purchases never require any borrowed money'], 0)]),
Sc('Science: The Physics of Flight: Lift and Drag',
   'Grade 7 Science strand: an airplane stays in the air due to four forces: lift, which pushes it upward, and drag, which slows it down, working together with thrust and gravity.',
   [('What force pushes an airplane upward, keeping it in the air?', ['Lift', 'Drag', 'A concept unrelated to flight', 'Gravity only'], 0),
    ('What force slows an airplane down as it moves through the air?', ['Drag', 'Lift', 'A concept unrelated to flight', 'Thrust only'], 0),
    ('Besides lift and drag, name one other force involved in flight, such as thrust or gravity.', ['Thrust', 'A concept unrelated to flight', 'Sound', 'Light'], 0),
    ('Why is the shape of an airplane’s wing important for generating lift?', ['The wing’s curved shape helps create differences in air pressure that produce lift', 'Wing shape has no connection to how lift is generated', 'This concept has no connection to physics', 'Airplanes generate lift with no need for any specific wing shape'], 0),
    ('Why must an airplane’s thrust be strong enough to overcome drag during flight?', ['Thrust needs to push the plane forward against the resistance created by drag', 'Thrust and drag have no connection to each other', 'This concept has no relevance to science', 'Drag always helps an airplane move faster, never slower'], 0)]),
SS('Social Studies: The History of Daylight Saving Time',
   'Grade 7 Social Studies strand: daylight saving time is the practice of moving clocks forward in spring and back in fall, originally intended to make better use of daylight hours and save energy.',
   [('What is daylight saving time?', ['The practice of moving clocks forward in spring and back in fall', 'A rule requiring everyone to wake up at the same time', 'A concept unrelated to timekeeping', 'A type of holiday celebrated worldwide'], 0),
    ('When are clocks typically moved forward for daylight saving time?', ['In spring', 'In fall', 'A concept unrelated to daylight saving time', 'Only in winter'], 0),
    ('Was daylight saving time originally intended to help save energy?', ['Yes', 'No, it was never connected to energy savings', 'A concept unrelated to daylight saving time', 'It was created only for entertainment purposes'], 0),
    ('Why might some regions choose not to observe daylight saving time?', ['They may feel the time change does not provide enough benefit for their location or climate', 'Every region in the world is required to observe daylight saving time', 'This concept has no connection to daylight saving time', 'Daylight saving time has no effect on daily schedules at all'], 0),
    ('Why might daylight saving time be a topic of ongoing debate in some countries?', ['People have different opinions about whether the practice still provides meaningful benefits today', 'Daylight saving time has never been debated by anyone', 'This concept has no relevance to social studies', 'Every country in the world has always agreed on this issue'], 0)]),
]),

day(88, [
L('Grammar: Absolute Phrases',
  'Grade 7 Language strand: an absolute phrase modifies an entire sentence rather than a single word, often combining a noun with a participle, such as in Her arms crossed, she waited by the door.',
  [('What does an absolute phrase modify?', ['An entire sentence', 'Only a single word', 'A concept unrelated to grammar', 'Nothing at all'], 0),
   ('An absolute phrase often combines a noun with what other type of word?', ['A participle', 'A preposition only', 'A concept unrelated to absolute phrases', 'A conjunction only'], 0),
   ('In the sentence Her arms crossed, she waited by the door, what is the absolute phrase?', ['Her arms crossed', 'She waited by the door', 'By the door', 'Waited'], 0),
   ('Which sentence correctly uses an absolute phrase?', ['His eyes closed, he listened carefully to the music.', 'His eyes he closed listened carefully the music to.', 'Closed his eyes he to the music listened.', 'He listened his eyes closed carefully to the music closed.'], 0),
   ('Why might a writer use an absolute phrase to add detail to a sentence?', ['It can add vivid, descriptive detail without creating a separate sentence', 'Absolute phrases never add any detail to a sentence', 'This concept has no connection to grammar', 'Absolute phrases always make a sentence less descriptive'], 0)]),
M('Geometry: Volume of Composite Solids with Curved Surfaces',
  'Grade 7 Math strand: students find the volume of composite solids that combine shapes with curved surfaces, such as a cylinder topped with a cone, by finding the volume of each part and adding them together.',
  [('To find the volume of a composite solid made of a cylinder and a cone, what should you do?', ['Find the volume of each part and add them together', 'Only calculate the volume of the cylinder', 'A concept unrelated to composite solids', 'Only calculate the volume of the cone'], 0),
   ('If a cylinder’s volume is 40 cubic cm and a cone on top has a volume of 10 cubic cm, what is the total volume?', ['50 cubic cm', '40 cubic cm', '10 cubic cm', '30 cubic cm'], 0),
   ('Why is it useful to break a composite solid into simpler shapes before finding its volume?', ['It makes the calculation more manageable by using known volume formulas for each simple shape', 'Breaking a solid into simpler shapes never helps calculate its volume', 'This concept has no connection to geometry', 'Composite solids can never be broken into simpler shapes'], 0),
   ('If a composite solid is made of two cylinders with volumes of 25 and 15 cubic cm, what is the total volume?', ['40 cubic cm', '25 cubic cm', '15 cubic cm', '10 cubic cm'], 0),
   ('Why might understanding composite solid volume be useful for designing a real object, like a water tank?', ['Many real objects are made of combined shapes, so this skill helps calculate their total capacity', 'Composite solid volume never applies to any real-world object', 'This concept has no connection to geometry', 'Water tanks are always made of a single, simple shape'], 0)]),
Sc('Science: Genetic Variation and Biodiversity',
   'Grade 7 Science strand: genetic variation refers to the differences in genes among individuals of a species, contributing to biodiversity and helping populations adapt to changing environments.',
   [('What does genetic variation refer to?', ['Differences in genes among individuals of a species', 'A single, identical gene shared by every individual', 'A concept unrelated to biology', 'A process where genes never change at all'], 0),
    ('Does genetic variation contribute to biodiversity?', ['Yes', 'No, genetic variation has no connection to biodiversity', 'A concept unrelated to genetics', 'Biodiversity is only affected by habitat, never genetics'], 0),
    ('Can genetic variation help a population adapt to a changing environment?', ['Yes', 'No, genetic variation never helps with adaptation', 'A concept unrelated to genetic variation', 'Populations never need to adapt to any environment'], 0),
    ('Why might a population with high genetic variation be more likely to survive a sudden environmental change, like a new disease?', ['Some individuals may already have traits that help them resist the new challenge', 'Genetic variation has no connection to surviving environmental changes', 'This concept has no connection to biology', 'Every individual in a population always has identical genes'], 0),
    ('Why is protecting genetic variation important for conservation efforts?', ['It helps ensure species have the best chance of adapting to future environmental changes', 'Genetic variation has no relevance to conservation efforts', 'This concept has no relevance to science', 'Species never actually need genetic variation to survive'], 0)]),
SS('Social Studies: Space Law and International Treaties on Space',
   'Grade 7 Social Studies strand: space law includes international treaties, such as the Outer Space Treaty of 1967, that establish rules for how countries can explore and use outer space peacefully.',
   [('What is space law?', ['International treaties that establish rules for exploring and using outer space', 'A rule about airplane travel on Earth', 'A concept unrelated to space exploration', 'A private company’s internal policy'], 0),
    ('What is the name of a major international treaty on space, established in 1967?', ['The Outer Space Treaty', 'A concept unrelated to space law', 'The Berlin Treaty', 'The Suez Agreement'], 0),
    ('Does space law aim to ensure countries use outer space peacefully?', ['Yes', 'No, space law encourages conflict in space', 'A concept unrelated to space law', 'Space law has no connection to how countries use space'], 0),
    ('Why might countries agree to international treaties about space exploration?', ['Shared rules can help prevent conflict and encourage peaceful cooperation in space', 'Countries never need any agreements about space exploration', 'This concept has no connection to social studies', 'Space exploration has no connection to international relations'], 0),
    ('Why might space law become an increasingly important topic as more countries and companies explore space?', ['More activity in space increases the need for clear rules to avoid conflicts or unsafe practices', 'Space law will never need to be updated or discussed further', 'This concept has no relevance to social studies', 'Only one single country is ever involved in exploring space'], 0)]),
]),

day(89, [
L('Reading: Analyzing Frame Narratives',
  'Grade 7 Language strand: a frame narrative is a story structure where one story is told within another, such as a character telling a story to another character, adding layers of meaning to the text.',
  [('What is a frame narrative?', ['A story structure where one story is told within another', 'A story with only one single character', 'A concept unrelated to reading', 'A story told with no dialogue at all'], 0),
   ('Can a frame narrative add layers of meaning to a text?', ['Yes', 'No, frame narratives never add any meaning', 'A concept unrelated to frame narratives', 'Frame narratives always simplify a story completely'], 0),
   ('If a character tells a story to another character within a novel, is that an example of a frame narrative?', ['Yes', 'No, this is not an example of a frame narrative', 'A concept unrelated to reading', 'This can never happen within a novel'], 0),
   ('Why might an author use a frame narrative instead of telling a single, straightforward story?', ['It can add complexity and multiple perspectives to how the story is understood', 'Frame narratives never add any complexity to a story', 'This concept has no connection to literature', 'A frame narrative always makes a story less interesting'], 0),
   ('Why might readers need to pay close attention to the different layers within a frame narrative?', ['Understanding who is telling each part of the story can affect how the events are interpreted', 'The layers of a frame narrative never affect how a story is interpreted', 'This concept has no relevance to reading comprehension', 'Frame narratives never actually contain more than one layer'], 0)]),
M('Number Theory: Divisibility and Prime Numbers Deeper Dive',
  'Grade 7 Math strand: students deepen their understanding of divisibility rules and prime numbers, exploring how prime factorization can be used to simplify fractions and find common factors.',
  [('What is a prime number?', ['A number greater than 1 with exactly two factors, 1 and itself', 'A number that can be divided evenly by any number', 'A concept unrelated to number theory', 'A number with no factors at all'], 0),
   ('What is the prime factorization of 12?', ['2 times 2 times 3', '2 times 6', '3 times 4', '1 times 12'], 0),
   ('Why is prime factorization useful for simplifying a fraction?', ['It helps identify common factors that can be cancelled out between the numerator and denominator', 'Prime factorization never helps with simplifying a fraction', 'This concept has no connection to fractions', 'Fractions can never be simplified using prime factorization'], 0),
   ('Is the number 7 a prime number?', ['Yes', 'No, 7 has more than two factors', 'A concept unrelated to prime numbers', '7 is neither prime nor composite'], 0),
   ('Why might understanding divisibility rules help you quickly check if a number is prime?', ['Divisibility rules can quickly rule out certain factors without long division', 'Divisibility rules never help with checking prime numbers', 'This concept has no connection to number theory', 'Every number is automatically prime unless proven otherwise'], 0)]),
Sc('Science: Space Weather and Solar Flares',
   'Grade 7 Science strand: space weather refers to conditions in space, such as solar flares, bursts of energy from the Sun that can affect satellites, power grids, and communication systems on Earth.',
   [('What does space weather refer to?', ['Conditions in space, such as solar flares', 'Only weather patterns found on Earth', 'A concept unrelated to space', 'Conditions found only on the Moon'], 0),
    ('What is a solar flare?', ['A burst of energy from the Sun', 'A type of cloud found on Earth', 'A concept unrelated to space weather', 'A burst of energy from the Moon'], 0),
    ('Can solar flares affect satellites and power grids on Earth?', ['Yes', 'No, solar flares never affect anything on Earth', 'A concept unrelated to solar flares', 'Solar flares only affect objects on the Moon'], 0),
    ('Why might scientists closely monitor solar flares?', ['Strong solar flares could disrupt communication systems or damage satellites', 'Solar flares have no effect on any technology on Earth', 'This concept has no connection to space weather', 'Monitoring solar flares serves no useful purpose'], 0),
    ('Why is understanding space weather becoming more important as society relies more on satellite technology?', ['More reliance on satellites means more potential impact if space weather disrupts them', 'Satellite technology has no connection to space weather', 'This concept has no relevance to science', 'Space weather has no effect on modern technology'], 0)]),
SS('Social Studies: The Role of Credit Unions and Cooperatives',
   'Grade 7 Social Studies strand: a credit union is a cooperative financial institution owned by its members, often offering banking services with a focus on community benefit rather than maximizing profit.',
   [('What is a credit union?', ['A cooperative financial institution owned by its members', 'A private company owned by a single wealthy investor', 'A concept unrelated to finance', 'A government tax office'], 0),
    ('Is a credit union owned by its members?', ['Yes', 'No, a credit union is owned by a single distant shareholder', 'A concept unrelated to credit unions', 'Credit unions have no owners at all'], 0),
    ('Does a credit union often focus on community benefit rather than maximizing profit?', ['Yes', 'No, credit unions only focus on maximizing profit', 'A concept unrelated to credit unions', 'Community benefit has no connection to credit unions'], 0),
    ('Why might someone choose to bank with a credit union instead of a large traditional bank?', ['They may prefer an institution that is owned by its members and focused on community benefit', 'Credit unions never offer any banking services at all', 'This concept has no connection to social studies', 'There is never any difference between a credit union and a bank'], 0),
    ('Why might cooperative financial institutions like credit unions be considered beneficial for local communities?', ['Profits are often reinvested into member services or the local community rather than outside shareholders', 'Credit unions never provide any benefit to communities', 'This concept has no relevance to social studies', 'Cooperative institutions always operate exactly like large corporations'], 0)]),
]),

day(90, [
L('Review: Motifs, Grammar, and Media Literacy (Days 81-89)',
  'Grade 7 Language strand review: students revisit motifs, personal manifestos, nominalization, neologisms, logical fallacies, letters of recommendation, algorithmic content curation, absolute phrases, and frame narratives.',
  [('What do we call a recurring element, like an image or idea, that reinforces a text’s themes?', ['A motif', 'A concept unrelated to reading', 'A footnote', 'A citation'], 0),
   ('What does nominalization do to a verb or adjective?', ['Turns it into a noun', 'Turns it into a question', 'A concept unrelated to grammar', 'Removes it from the sentence'], 0),
   ('What do we call a newly coined word or phrase?', ['A neologism', 'A concept unrelated to vocabulary', 'A synonym', 'A homophone'], 0),
   ('What do we call a flaw in reasoning that weakens an argument?', ['A logical fallacy', 'A concept unrelated to reading', 'A citation', 'A footnote'], 0),
   ('What is a frame narrative?', ['A story structure where one story is told within another', 'A story with only one single character', 'A concept unrelated to reading', 'A story told with no dialogue at all'], 0)]),
M('Review: Algebra, Geometry, and Data (Days 81-89)',
  'Grade 7 Math strand review: students revisit solving systems by substitution, scientific notation operations, perpendicular bisectors, correlation vs causation, multiplying binomials, credit scores, composite solid volume, and prime factorization.',
  [('In the substitution method, what do you do first with one of the equations?', ['Solve it for a single variable', 'Graph both equations immediately', 'A concept unrelated to systems of equations', 'Multiply both equations together'], 0),
   ('What does a perpendicular bisector cross a segment at?', ['Its midpoint', 'One of its endpoints', 'A concept unrelated to geometry', 'A random point outside the segment'], 0),
   ('What does causation mean?', ['One variable directly causes a change in another', 'Two variables have absolutely no connection at all', 'A concept unrelated to data analysis', 'Correlation and causation always mean the exact same thing'], 0),
   ('What is (x plus 2) times (x plus 3) equal to?', ['x squared plus 5x plus 6', 'x squared plus 6x plus 5', 'x squared plus 2x plus 3', '2x plus 6'], 0),
   ('What is a prime number?', ['A number greater than 1 with exactly two factors, 1 and itself', 'A number that can be divided evenly by any number', 'A concept unrelated to number theory', 'A number with no factors at all'], 0)]),
Sc('Review: Ecology, Chemistry, and Physical Science (Days 81-89)',
   'Grade 7 Science strand review: students revisit ecosystem succession, sound in instruments, green architecture, combustion, bioluminescence, antibiotic resistance, lift and drag, genetic variation, and space weather.',
   [('What is ecosystem succession?', ['The gradual process by which an ecosystem changes over time', 'A process where ecosystems never change at all', 'A concept unrelated to ecology', 'A single, instant event with no stages'], 0),
    ('What is combustion?', ['A chemical reaction where fuel reacts with oxygen, releasing energy', 'A process that only involves ice melting', 'A concept unrelated to chemistry', 'A reaction that never releases any energy'], 0),
    ('What is antibiotic resistance?', ['When bacteria evolve to survive medicines designed to kill them', 'A process where bacteria are instantly destroyed by every medicine', 'A concept unrelated to biology', 'A type of vaccine'], 0),
    ('What force pushes an airplane upward, keeping it in the air?', ['Lift', 'Drag', 'A concept unrelated to flight', 'Gravity only'], 0),
    ('What is a solar flare?', ['A burst of energy from the Sun', 'A type of cloud found on Earth', 'A concept unrelated to space weather', 'A burst of energy from the Moon'], 0)]),
SS('Review: Global History and Economics (Days 81-89)',
   'Grade 7 Social Studies strand review: students revisit the Berlin Airlift, the Suez Crisis, Canadian health care history, global water rights, e-commerce, the auto industry, daylight saving time, space law, and credit unions.',
   [('What was the Berlin Airlift?', ['An operation flying supplies into West Berlin after a Soviet blockade', 'A modern airline company', 'A concept unrelated to history', 'A type of sporting event'], 0),
    ('Which Canadian diplomat proposed the first large-scale UN peacekeeping force during the Suez Crisis?', ['Lester B. Pearson', 'A concept unrelated to Canadian history', 'A fictional diplomat', 'A diplomat from a different country'], 0),
    ('What is Canada’s public health care system often called?', ['Medicare', 'A concept unrelated to Canadian history', 'A private insurance company', 'A hospital chain'], 0),
    ('What is e-commerce?', ['The buying and selling of goods online', 'A type of in-person farmers market only', 'A concept unrelated to the economy', 'A government program with no connection to shopping'], 0),
    ('What is a credit union?', ['A cooperative financial institution owned by its members', 'A private company owned by a single wealthy investor', 'A concept unrelated to finance', 'A government tax office'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_81_90)
    append_to(7, g7_81_90)
