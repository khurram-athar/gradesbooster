#!/usr/bin/env python3
"""Grade 10, Days 141-150 -- extends Grade 10 from 140 to 150 days. Topics
chosen after grepping the existing Day 1-140 title list (data/grade10.json)
extensively to avoid any overlap: product placement in film and television,
cleft sentences, allusion in literature, the business memo and professional
email, the Kunstlerroman (artist novel), native advertising and sponsored
content, subject-verb agreement in complex sentences, synecdoche and
metonymy, and the vignette as a narrative form; optimization using
derivatives, Wilsons Theorem, the chi-squared goodness-of-fit test,
LHopitals Rule, fractals and self-similarity, recurrence relations, areas
between curves, the Chinese Remainder Theorem, and the geometric
distribution; coevolution and mutualism, enzymes and biological catalysis,
nuclear fission and fusion, earthquakes and seismology, stem cells and
cellular differentiation, nanotechnology, special relativity and time
dilation, ocean acidification, and the human brain and neuroplasticity;
the On-to-Ottawa Trek, the Padlock Law of Quebec, the National Housing Act
of 1938, the Munich Agreement, the founding of Trans-Canada Air Lines, the
founding of the National Film Board, the founding of the Canadian Wheat
Board, the Ogdensburg Agreement, and the National Resources Mobilization
Act, continuing the institution-building and pre-war Canadian history
sequence begun in Days 131-140.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used anywhere
in title/question/summary/option text -- apostrophes are dropped entirely,
matching the Days 111-140 convention.
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


def _rebalance_answer_positions(days, seed=20260807):
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


g10_141_150 = [
day(141, [
E('Media Literacy: Analyzing Product Placement in Film and Television',
  'Grade 10 English strand: product placement is the practice of featuring a branded product or service within a film, television show, or other media content in exchange for payment or promotional consideration, blurring the line between entertainment and advertising.',
  [('What is product placement?', ['A branded product or service featured within media content in exchange for payment or promotion', 'A method of editing film footage after production', 'A legal requirement for all television broadcasts', 'A type of movie theatre seating arrangement'], 0),
   ('What line does product placement blur?', ['The line between entertainment and advertising', 'The line between fiction and historical fact', 'The line between print and digital media', 'The line between comedy and tragedy'], 0),
   ('Why might a viewer fail to notice product placement?', ['Because it is woven into the story or setting rather than presented as a separate advertisement', 'Because product placement is always announced loudly before it appears', 'Because product placement never appears in visual media', 'Because television programs are required to pause before showing a brand'], 0),
   ('Which of the following is an example of product placement?', ['A character in a film prominently using a specific named brand of laptop', 'A standalone thirty-second commercial break between scenes', 'A newspaper article reviewing a new product', 'A billboard advertisement seen while driving to a theatre'], 0),
   ('Why is media literacy useful for recognizing product placement?', ['It helps viewers distinguish between organic story content and paid promotional material', 'It removes the need to ever watch a film critically', 'It guarantees that all media content is free of any advertising', 'It has no connection to how audiences interpret visual media'], 0)]),
M('Calculus: Optimization Problems Using Derivatives',
  'Grade 10 Math strand: optimization problems use derivatives to find the maximum or minimum value of a quantity, typically by setting the derivative of a function equal to zero to locate critical points and then testing which point yields the greatest or least value.',
  [('What do optimization problems in calculus typically find?', ['The maximum or minimum value of a quantity', 'The exact colour of a graphed function', 'The total number of variables in an equation', 'The name of the mathematician who first studied the function'], 0),
   ('What is the first step commonly used to locate a critical point?', ['Setting the derivative of the function equal to zero', 'Multiplying the function by a random constant', 'Graphing the function without calculating anything', 'Ignoring the function entirely and guessing an answer'], 0),
   ('What is a critical point in an optimization problem?', ['A point where the derivative is zero or undefined', 'A point where the function is always negative', 'A point that never appears on a graph', 'A point defined only by its y-intercept'], 0),
   ('Why must a critical point be tested after it is found?', ['To determine whether it represents a maximum, a minimum, or neither', 'Because critical points are always automatically the maximum', 'Because testing a critical point is never necessary', 'To convert the critical point into a whole number'], 0),
   ('Which real-world scenario is a classic example of an optimization problem?', ['Finding the dimensions that minimize the material used to build a box of fixed volume', 'Counting the total number of boxes in a warehouse', 'Measuring the exact colour of a box', 'Determining the manufacturer of a randomly selected box'], 0)]),
Sc('Biology: Coevolution and Mutualistic Relationships',
   'Grade 10 Science strand: coevolution occurs when two or more species reciprocally influence each others evolution over time, often producing mutualistic relationships in which both species benefit, such as flowering plants and their pollinators.',
   [('What is coevolution?', ['A process in which two or more species reciprocally influence each others evolution over time', 'A process in which a single species evolves with no influence from any other organism', 'A process that only occurs in extinct species', 'A sudden, one-time genetic mutation with no evolutionary effect'], 0),
    ('What is a mutualistic relationship?', ['A relationship in which both interacting species benefit', 'A relationship in which one species is harmed and the other is unaffected', 'A relationship that only occurs between members of the same species', 'A relationship in which both species are harmed equally'], 0),
    ('Which pairing is a classic example of coevolved mutualism?', ['Flowering plants and their pollinators', 'A shark and a school of unrelated fish with no interaction', 'Two unrelated species that never interact', 'A rock and the moss growing nearby with no exchange of benefit'], 0),
    ('Why might a flower and its pollinator evolve matching physical traits?', ['Because traits that improve the exchange of nectar for pollination benefit both species over generations', 'Because flowers and pollinators never influence one anothers traits', 'Because pollinators always harm the flowers they visit', 'Because matching traits occur randomly with no evolutionary benefit'], 0),
    ('How does coevolution differ from a relationship where only one species benefits?', ['In coevolved mutualism both species gain an advantage, while in relationships like parasitism only one species benefits', 'Coevolution always harms both species involved', 'Coevolution never involves more than one species', 'There is no meaningful difference between mutualism and parasitism'], 0)]),
H('The On-to-Ottawa Trek of 1935',
  'Grade 10 History strand: the On-to-Ottawa Trek was a 1935 protest march in which unemployed men from federal relief camps travelled by rail from British Columbia toward Ottawa to demand better wages and conditions, ending when the trek was stopped by police in Regina, resulting in the Regina Riot.',
  [('What was the On-to-Ottawa Trek?', ['A 1935 protest march by unemployed men from federal relief camps travelling toward Ottawa', 'A ceremonial parade celebrating Canadian Confederation', 'A railway construction project connecting British Columbia to Ontario', 'A diplomatic mission sent to negotiate with the United States'], 0),
   ('What were the trekkers protesting?', ['Poor wages and conditions in federal relief camps', 'A new federal tax on farm equipment', 'The construction of a new national railway', 'A proposed reduction in provincial voting rights'], 0),
   ('How did the trekkers initially travel toward Ottawa?', ['By riding freight trains', 'By flying in chartered aircraft', 'By walking the entire distance on foot with no vehicles', 'By sailing along the Pacific coast'], 0),
   ('Where was the trek ultimately stopped?', ['In Regina, Saskatchewan', 'In Ottawa, Ontario, after arriving successfully', 'In Vancouver, British Columbia, before it began', 'In Halifax, Nova Scotia'], 0),
   ('What violent event resulted when the trek was stopped?', ['The Regina Riot', 'The Halifax Explosion', 'The Winnipeg General Strike', 'The Oka Crisis'], 0)]),
]),
day(142, [
E('Grammar: Cleft Sentences for Emphasis',
  'Grade 10 English strand: a cleft sentence divides a single idea into two clauses, typically using a phrase such as It was... that or What... is to shift emphasis onto a particular piece of information within a sentence.',
  [('What does a cleft sentence do?', ['It divides a single idea into two clauses to shift emphasis onto a particular piece of information', 'It combines two unrelated ideas into a single run-on sentence', 'It removes all punctuation from a sentence', 'It converts a sentence into a question automatically'], 0),
   ('Which sentence opener commonly signals a cleft sentence?', ['It was... that', 'Once upon a time', 'In conclusion', 'On the other hand'], 0),
   ('Which sentence is an example of a cleft sentence?', ['It was the coach who called the final play.', 'The coach called the final play.', 'The coach, who arrived late, called the final play.', 'Calling the final play, the coach smiled.'], 0),
   ('Why might a writer choose a cleft sentence over a plain statement?', ['To draw the readers attention to a specific detail within the sentence', 'To remove all meaning from the sentence', 'To avoid using a subject or verb entirely', 'To make the sentence impossible to understand'], 0),
   ('What type of clause commonly follows the emphasized element in a cleft sentence?', ['A relative clause beginning with that or who', 'A completely unrelated independent sentence', 'A single isolated noun with no clause at all', 'A question with no connection to the emphasized element'], 0)]),
M('Number Theory: Wilsons Theorem',
  'Grade 10 Math strand: Wilsons Theorem states that a whole number p greater than 1 is prime if and only if (p minus 1) factorial plus 1 is divisible by p, offering a distinctive test for primality rooted in factorials and modular arithmetic.',
  [('What does Wilsons Theorem provide a test for?', ['Whether a number is prime', 'Whether a number is even', 'Whether a fraction is in lowest terms', 'Whether a shape is a regular polygon'], 0),
   ('What quantity does Wilsons Theorem involve, in addition to the number p?', ['The factorial of p minus 1', 'The square root of p', 'The sine of p degrees', 'The logarithm of p'], 0),
   ('According to Wilsons Theorem, if p is prime, what must be true about (p minus 1) factorial plus 1?', ['It is divisible by p', 'It is always equal to zero', 'It is always a negative number', 'It is never a whole number'], 0),
   ('What area of mathematics connects most directly to Wilsons Theorem?', ['Modular arithmetic and number theory', 'Coordinate geometry', 'Trigonometric identities', 'Statistical sampling methods'], 0),
   ('Why is Wilsons Theorem considered mostly a theoretical rather than practical primality test?', ['Calculating a large factorial becomes computationally expensive very quickly', 'It only works for the number zero', 'Factorials are never used in mathematics', 'Prime numbers do not exist above one hundred'], 0)]),
Sc('Chemistry: Enzymes and Biological Catalysis',
   'Grade 10 Science strand: enzymes are specialized proteins that act as biological catalysts, speeding up chemical reactions in living organisms by lowering the activation energy required, without being consumed in the reaction themselves.',
   [('What are enzymes?', ['Specialized proteins that act as biological catalysts', 'Simple sugars used only for energy storage', 'Inorganic minerals found only in rock formations', 'Waste products removed entirely from living cells'], 0),
    ('How do enzymes speed up chemical reactions?', ['By lowering the activation energy required for the reaction', 'By increasing the activation energy required for the reaction', 'By permanently stopping the reaction from occurring', 'By converting the reactants into an entirely different element'], 0),
    ('What happens to an enzyme after it catalyzes a reaction?', ['It is not consumed and can be used again', 'It is destroyed completely and cannot be reused', 'It transforms permanently into the reaction product', 'It stops functioning as a protein entirely'], 0),
    ('What term describes the specific molecule an enzyme acts upon?', ['The substrate', 'The catalyst', 'The solvent', 'The precipitate'], 0),
    ('Why can extreme heat cause an enzyme to stop functioning?', ['High temperatures can denature the enzyme, changing its shape so it no longer fits its substrate', 'Heat always makes enzymes work more efficiently with no limit', 'Enzymes are entirely unaffected by any temperature change', 'Heat converts every enzyme into a substrate automatically'], 0)]),
H('The Padlock Law of Quebec, 1937',
  'Grade 10 History strand: the Padlock Law, passed by the Quebec government in 1937, allowed authorities to shut and padlock any premises used to propagate communism or bolshevism without a trial, a measure later challenged as an infringement on civil liberties.',
  [('In what year was the Padlock Law passed?', ['1937', '1867', '1905', '1949'], 0),
   ('Which government passed the Padlock Law?', ['The government of Quebec', 'The government of Ontario', 'The federal government of Canada', 'The government of British Columbia'], 0),
   ('What could authorities do under the Padlock Law?', ['Shut and padlock any premises used to propagate communism or bolshevism without a trial', 'Grant additional voting rights to every citizen', 'Fund new provincial highways across Quebec', 'Establish a new provincial bank'], 0),
   ('What broader concern did the Padlock Law later raise?', ['Concerns about civil liberties and freedom of expression', 'Concerns about the price of wheat', 'Concerns about railway safety standards', 'Concerns about international trade tariffs'], 0),
   ('What legal concept did critics argue the Padlock Law violated by allowing action without a trial?', ['Due process', 'Universal suffrage', 'Free trade', 'Responsible government'], 0)]),
]),
day(143, [
E('Reading: Analyzing Allusion in Literature',
  'Grade 10 English strand: an allusion is a brief, indirect reference to a person, place, event, or work from history, mythology, religion, or another text, allowing a writer to add layered meaning by connecting a new work to a shared body of prior knowledge.',
  [('What is an allusion?', ['A brief, indirect reference to a person, place, event, or work outside the text', 'A detailed, fully explained retelling of another entire story', 'A grammatical error found within a sentence', 'A punctuation mark used to end a question'], 0),
   ('What kinds of sources might an allusion draw from?', ['History, mythology, religion, or another literary work', 'Only mathematical formulas', 'Only weather reports', 'Only grammar textbooks'], 0),
   ('Why might a writer use allusion?', ['To add layered meaning by connecting the text to a shared body of prior knowledge', 'To ensure that no reader can understand the text at all', 'To remove any connection between the text and outside knowledge', 'To avoid using any figurative language whatsoever'], 0),
   ('What is required of a reader to fully understand an allusion?', ['Familiarity with the outside reference being made', 'No prior knowledge of any kind', 'A complete misunderstanding of the text', 'Fluency in a foreign language unrelated to the reference'], 0),
   ('Which of the following is an example of an allusion?', ['Describing a difficult task as a Herculean effort', 'Describing a room as painted blue', 'Listing the ingredients of a recipe', 'Stating the exact time of day in a scene'], 0)]),
M('Statistics: The Chi-Squared Goodness-of-Fit Test',
  'Grade 10 Math strand: the chi-squared goodness-of-fit test compares observed categorical data to the frequencies that would be expected under a specific hypothesis, producing a statistic that indicates whether the observed data significantly differs from what was expected.',
  [('What does a chi-squared goodness-of-fit test compare?', ['Observed categorical data to the frequencies expected under a specific hypothesis', 'The slope of two unrelated lines', 'The derivative of a function at a single point', 'The volume of two different solids'], 0),
   ('What type of data is the chi-squared goodness-of-fit test designed to analyze?', ['Categorical data', 'Only irrational numbers', 'Only data with negative values', 'Only data with exactly two data points'], 0),
   ('What does a large chi-squared statistic generally suggest?', ['The observed data significantly differs from what was expected', 'The observed data matches the expected data perfectly in every case', 'The sample size was too large to be valid', 'No hypothesis was ever tested'], 0),
   ('What must be defined before running a chi-squared goodness-of-fit test?', ['The expected frequencies under a stated hypothesis', 'The exact colour of the data visualization', 'The derivative of the data set', 'The physical location where data was collected'], 0),
   ('In which field is the chi-squared goodness-of-fit test commonly applied?', ['Analyzing survey or experimental data across categories', 'Designing architectural blueprints', 'Composing musical scales', 'Translating a text between languages'], 0)]),
Sc('Physics: Nuclear Fission and Nuclear Fusion',
   'Grade 10 Science strand: nuclear fission splits a heavy atomic nucleus into smaller nuclei, releasing energy, while nuclear fusion combines two light nuclei into a heavier one, also releasing energy, with fission used in current nuclear power plants and fusion powering stars such as the sun.',
   [('What happens during nuclear fission?', ['A heavy atomic nucleus splits into smaller nuclei, releasing energy', 'Two light nuclei combine into a heavier nucleus, releasing energy', 'An atom gains an electron with no change in energy', 'A molecule breaks down into individual atoms with no energy released'], 0),
    ('What happens during nuclear fusion?', ['Two light nuclei combine into a heavier nucleus, releasing energy', 'A heavy nucleus splits into smaller nuclei, releasing energy', 'An atom loses a proton with no other effect', 'A compound dissolves completely in water'], 0),
    ('Which process powers current nuclear power plants?', ['Nuclear fission', 'Nuclear fusion', 'Simple combustion of fossil fuels', 'Wind-driven turbines only'], 0),
    ('Which process powers stars such as the sun?', ['Nuclear fusion', 'Nuclear fission', 'Chemical combustion of gas', 'Radioactive decay alone with no fusion involved'], 0),
    ('Why is nuclear fusion considered an attractive future energy source?', ['It has the potential to release large amounts of energy with fewer long-lived radioactive byproducts than fission', 'It produces no energy at all', 'It is identical to burning fossil fuels', 'It requires no scientific research to implement'], 0)]),
H('The National Housing Act of 1938',
  'Grade 10 History strand: the National Housing Act of 1938 expanded federal involvement in housing by offering government-backed loans to encourage home construction and repair during the Great Depression, laying groundwork for later federal housing policy in Canada.',
  [('In what year was the National Housing Act passed?', ['1938', '1867', '1905', '1949'], 0),
   ('What did the National Housing Act offer to encourage home construction?', ['Government-backed loans', 'Free land grants to every citizen', 'A new national currency', 'Mandatory military service for builders'], 0),
   ('During what economic period was the National Housing Act introduced?', ['The Great Depression', 'The dot-com boom of the 1990s', 'The years immediately following Confederation', 'The height of the Klondike Gold Rush'], 0),
   ('What broader policy area did the National Housing Act help establish?', ['Federal involvement in housing policy', 'Federal control over provincial elections', 'A national postal service', 'A national system of criminal courts'], 0),
   ('Why might a government offer backed loans for housing during a depression?', ['To stimulate construction activity and employment during an economic downturn', 'To discourage any new construction during hard times', 'To eliminate the need for any future housing', 'To transfer all housing responsibility to foreign governments'], 0)]),
]),
day(144, [
E('Writing: The Business Memo and Professional Email',
  'Grade 10 English strand: a business memo or professional email is a concise workplace document that communicates information, requests, or decisions to colleagues using a clear subject line, direct opening statement, and organized body, avoiding unnecessary detail.',
  [('What is the purpose of a business memo or professional email?', ['To communicate information, requests, or decisions to colleagues concisely', 'To provide a lengthy personal narrative unrelated to work', 'To replace all verbal communication in a workplace permanently', 'To entertain readers with an extended work of fiction'], 0),
   ('What should a professional email typically include at the top?', ['A clear subject line', 'A handwritten signature only', 'An unrelated image with no context', 'A blank space with no information'], 0),
   ('How should the opening of a business memo generally be structured?', ['With a direct statement of the main point or request', 'With a long personal anecdote unrelated to the topic', 'With no information about the purpose of the memo', 'With a detailed weather report'], 0),
   ('Why do business memos favour concise, organized writing?', ['Because workplace readers often need to find key information quickly', 'Because concise writing has no value in a professional setting', 'Because memos are never read by anyone', 'Because organization makes information harder to find'], 0),
   ('Which of the following is appropriate content for a professional email?', ['A clearly stated request with any necessary supporting details', 'An unrelated joke with no connection to work', 'A vague message with no clear purpose', 'A message written entirely in informal slang'], 0)]),
M('Calculus: LHopitals Rule for Evaluating Limits',
  'Grade 10 Math strand: LHopitals Rule provides a method for evaluating limits that produce an indeterminate form such as zero over zero, by taking the derivative of the numerator and denominator separately and then re-evaluating the resulting limit.',
  [('What type of limit is LHopitals Rule designed to evaluate?', ['A limit that produces an indeterminate form such as zero over zero', 'A limit that is already a whole number with no calculation needed', 'A limit that only involves constant functions', 'A limit that cannot be expressed as a fraction of any kind'], 0),
   ('What is the general procedure used in LHopitals Rule?', ['Taking the derivative of the numerator and denominator separately, then re-evaluating the limit', 'Multiplying the numerator and denominator by zero', 'Ignoring the denominator entirely', 'Replacing the entire limit with an arbitrary constant'], 0),
   ('What must be true about a limit before LHopitals Rule can be applied?', ['It must result in an indeterminate form', 'It must already have a defined finite value', 'It must involve only whole numbers', 'It must be evaluated at exactly zero'], 0),
   ('Why might LHopitals Rule need to be applied more than once to a single limit?', ['The resulting limit after one application may still be an indeterminate form', 'LHopitals Rule can never be applied more than once under any circumstance', 'Applying it twice always produces an incorrect answer', 'The rule only works when applied exactly three times'], 0),
   ('LHopitals Rule builds most directly on which earlier calculus concept?', ['Derivatives', 'Basic arithmetic with no calculus involved', 'The Pythagorean Theorem', 'The quadratic formula'], 0)]),
Sc('Earth Science: Earthquakes and Seismology',
   'Grade 10 Science strand: seismology is the scientific study of earthquakes, which occur when built-up stress along a fault is suddenly released, sending seismic waves through the Earth that scientists measure using instruments called seismographs.',
   [('What is seismology the study of?', ['Earthquakes and the seismic waves they produce', 'The formation of clouds and weather patterns', 'The chemical composition of ocean water', 'The life cycle of stars'], 0),
    ('What causes an earthquake to occur?', ['Built-up stress along a fault is suddenly released', 'A sudden drop in atmospheric temperature', 'The gradual erosion of a river bank', 'A change in the phase of the moon'], 0),
    ('What instrument do scientists use to measure seismic waves?', ['A seismograph', 'A barometer', 'A thermometer', 'A spectrometer'], 0),
    ('What travels through the Earth during an earthquake?', ['Seismic waves', 'Sound waves through the atmosphere only', 'Light waves through solid rock', 'Radio waves generated by the fault line'], 0),
    ('Why do earthquakes tend to occur more frequently along fault lines?', ['Stress accumulates most readily where tectonic plates meet and grind against each other', 'Fault lines have no connection to tectonic activity', 'Earthquakes occur with equal frequency everywhere on Earth', 'Fault lines only exist in areas with no tectonic plates'], 0)]),
H('The Munich Agreement and Canadas Response, 1938',
  'Grade 10 History strand: the Munich Agreement of 1938 allowed Nazi Germany to annex the Sudetenland region of Czechoslovakia in exchange for a promise to seek no further territorial expansion, a policy of appeasement that Prime Minister Mackenzie King publicly supported at the time.',
  [('In what year was the Munich Agreement signed?', ['1938', '1867', '1919', '1949'], 0),
   ('What territory did the Munich Agreement allow Nazi Germany to annex?', ['The Sudetenland region of Czechoslovakia', 'The entire nation of Poland', 'A province of Canada', 'A territory belonging to the United States'], 0),
   ('What policy did the Munich Agreement represent?', ['Appeasement', 'Outright military confrontation', 'Complete economic isolation', 'Unconditional surrender'], 0),
   ('What promise did Germany make as part of the Munich Agreement?', ['To seek no further territorial expansion', 'To immediately disarm its entire military', 'To join the League of Nations', 'To grant independence to all of its territories'], 0),
   ('How did Prime Minister Mackenzie King respond to the Munich Agreement at the time?', ['He publicly supported it', 'He immediately declared war in response', 'He resigned from office in protest', 'He refused to comment on international affairs'], 0)]),
]),
day(145, [
E('Literature: The Artist Novel and the Kunstlerroman',
  'Grade 10 English strand: a Kunstlerroman, or artist novel, is a type of coming-of-age narrative that follows the development of an artist, writer, or musician from youth into creative maturity, closely related to the broader bildungsroman tradition.',
  [('What is a Kunstlerroman?', ['A coming-of-age narrative that follows the development of an artist from youth into creative maturity', 'A formal legal document used in court proceedings', 'A type of scientific research paper', 'A short poem with a strict rhyme scheme'], 0),
   ('What broader narrative tradition is the Kunstlerroman closely related to?', ['The bildungsroman', 'The epistolary novel', 'The detective procedural', 'The captivity narrative'], 0),
   ('What type of protagonist does a Kunstlerroman typically follow?', ['An artist, writer, or musician', 'A retired judge with no creative pursuits', 'A historical military general', 'An anonymous crowd with no individual characters'], 0),
   ('What does a Kunstlerroman typically trace across its plot?', ['The growth of the protagonists creative identity and craft', 'The construction of a large public building', 'The history of a nations legal system', 'The migration patterns of a species of bird'], 0),
   ('Why might an author choose the Kunstlerroman form?', ['To explore how artistic vision and personal identity develop together over time', 'To avoid describing any character development at all', 'To focus exclusively on unrelated historical events', 'To eliminate any reference to art or creativity'], 0)]),
M('Geometry: Fractals and Self-Similarity',
  'Grade 10 Math strand: a fractal is a geometric figure that displays self-similarity, meaning smaller portions of the figure resemble the whole shape at different scales, a property found in mathematical constructions as well as natural forms like coastlines and snowflakes.',
  [('What key property defines a fractal?', ['Self-similarity, where smaller portions resemble the whole shape at different scales', 'A shape with exactly three straight sides', 'A shape that only exists in three dimensions', 'A number with no decimal component'], 0),
   ('What does self-similarity mean in the context of fractals?', ['Smaller sections of a shape look similar to the entire shape', 'Every fractal is identical to every other fractal', 'A shape has no repeating pattern at any scale', 'A shape becomes a perfect circle when zoomed in'], 0),
   ('Which of the following is a natural example often associated with fractal-like patterns?', ['A coastline', 'A perfectly smooth sphere', 'A single straight line segment', 'A flat, featureless plane'], 0),
   ('How does zooming into a fractal typically appear?', ['Similar patterns continue to appear at smaller and smaller scales', 'The shape becomes completely blank with no detail', 'The shape transforms into an entirely unrelated image', 'The shape disappears entirely after one level of zoom'], 0),
   ('Why are fractals of interest beyond pure mathematics?', ['They help describe complex natural patterns that simple Euclidean shapes cannot easily capture', 'They have no application outside of abstract theory', 'They can only describe perfectly regular polygons', 'They were disproven and are no longer studied'], 0)]),
Sc('Biology: Stem Cells and Cellular Differentiation',
   'Grade 10 Science strand: stem cells are unspecialized cells capable of dividing and developing into many different specialized cell types through a process called cellular differentiation, making them essential to growth, tissue repair, and ongoing medical research.',
   [('What is a defining feature of a stem cell?', ['It is unspecialized and can develop into many different specialized cell types', 'It is always fully specialized with a single fixed function', 'It cannot divide under any circumstance', 'It exists only outside of living organisms'], 0),
    ('What is cellular differentiation?', ['The process by which an unspecialized cell develops into a specialized cell type', 'The process by which a cell loses its nucleus permanently', 'The process by which two unrelated organisms merge into one', 'The process by which a cell converts directly into a mineral'], 0),
    ('Why are stem cells important for tissue repair?', ['They can develop into the specialized cells needed to replace damaged tissue', 'They actively destroy healthy tissue in the body', 'They have no role in any biological process', 'They can only exist in plants, not animals'], 0),
    ('Which of the following describes a specialized cell that stem cells might differentiate into?', ['A muscle cell or a nerve cell', 'A grain of sand', 'A drop of water with no cellular structure', 'A mineral crystal'], 0),
    ('Why are stem cells a significant focus of modern medical research?', ['Their ability to become many cell types offers potential treatments for injury and disease', 'They have no potential medical application of any kind', 'They are identical to bacteria in every respect', 'They cannot be studied using any modern technology'], 0)]),
H('The Founding of Trans-Canada Air Lines in 1937',
  'Grade 10 History strand: Trans-Canada Air Lines was founded in 1937 as a federal Crown corporation to establish reliable, government-backed commercial air travel across the country, later becoming Air Canada and shaping the development of Canadian aviation infrastructure.',
  [('In what year was Trans-Canada Air Lines founded?', ['1937', '1867', '1905', '1949'], 0),
   ('What type of organization was Trans-Canada Air Lines when it was founded?', ['A federal Crown corporation', 'A privately owned foreign company', 'A provincial ministry with no national reach', 'A volunteer-run charitable organization'], 0),
   ('What was the main purpose of founding Trans-Canada Air Lines?', ['To establish reliable, government-backed commercial air travel across the country', 'To eliminate all forms of air travel in Canada', 'To build a network of national highways', 'To create a national postal delivery service'], 0),
   ('What airline did Trans-Canada Air Lines eventually become?', ['Air Canada', 'The Canadian Pacific Railway', 'The Royal Canadian Air Force', 'The National Film Board'], 0),
   ('Why might the federal government have chosen to back commercial aviation directly in the 1930s?', ['To ensure the development of national air travel infrastructure across a vast country', 'Because private companies had already fully developed air travel with no gaps', 'Because aviation had no importance to a country the size of Canada', 'To discourage any future development of air travel'], 0)]),
]),
day(146, [
E('Media Literacy: Analyzing Native Advertising and Sponsored Content',
  'Grade 10 English strand: native advertising is paid promotional content designed to match the look, tone, and format of the surrounding editorial material in which it appears, often labelled as sponsored content, making it important for readers to distinguish it from independent journalism.',
  [('What is native advertising?', ['Paid promotional content designed to match the look, tone, and format of the surrounding editorial material', 'A completely unpaid opinion piece written by an ordinary reader', 'A government regulation banning all forms of advertising', 'A style of advertising used only in radio broadcasts'], 0),
   ('What label is native advertising often given to indicate it is paid content?', ['Sponsored content', 'Breaking news', 'Editorial opinion', 'Letters to the editor'], 0),
   ('Why can native advertising be difficult for readers to identify?', ['It is designed to closely resemble the independent articles around it', 'It is always printed in a completely different font and colour', 'It is legally required to appear only on the final page', 'It never appears alongside any other content'], 0),
   ('Why is it important for readers to distinguish native advertising from journalism?', ['Because sponsored content is created to promote a product or brand rather than provide independent reporting', 'Because native advertising is always more accurate than journalism', 'Because journalism and advertising are legally identical', 'Because readers are never affected by promotional content'], 0),
   ('Which detail would most likely indicate an article is native advertising?', ['A small label reading sponsored or paid partner content', 'A byline listing a staff reporters name only', 'A dateline showing when the article was published', 'A photo credit listing the photographers name'], 0)]),
M('Discrete Math: Recurrence Relations',
  'Grade 10 Math strand: a recurrence relation defines each term of a sequence using one or more of the terms that came before it, along with initial starting values, providing a powerful way to model patterns that build step by step, such as the Fibonacci sequence.',
  [('What does a recurrence relation define?', ['Each term of a sequence using one or more of the terms that came before it', 'A single isolated number with no connection to a sequence', 'The area of a two-dimensional shape', 'The angle between two intersecting lines'], 0),
   ('What must be provided along with a recurrence relation to fully determine a sequence?', ['Initial starting values', 'The final term of the sequence only', 'A completely unrelated equation', 'The colour used to graph the sequence'], 0),
   ('Which classic sequence is commonly defined using a recurrence relation?', ['The Fibonacci sequence', 'A sequence of random, unrelated numbers', 'A sequence containing only the number zero', 'A sequence with no defined terms at all'], 0),
   ('Why are recurrence relations useful for modelling real situations?', ['Many real processes build directly on their own previous outcomes over time', 'Real processes never depend on any previous outcome', 'Recurrence relations only apply to abstract, unrealistic scenarios', 'Recurrence relations cannot model any repeating process'], 0),
   ('How does a recurrence relation differ from a closed-form formula for a sequence?', ['A recurrence relation depends on prior terms, while a closed-form formula computes a term directly from its position', 'The two approaches are mathematically identical in every way', 'A closed-form formula always requires knowing every previous term', 'A recurrence relation never involves any prior term'], 0)]),
Sc('Chemistry: Nanotechnology and Nanomaterials',
   'Grade 10 Science strand: nanotechnology involves designing and manipulating materials at the scale of individual atoms and molecules, typically less than 100 nanometres in size, producing nanomaterials with unique properties that differ significantly from the same substance at a larger scale.',
   [('At what approximate scale does nanotechnology operate?', ['Less than 100 nanometres, close to the scale of atoms and molecules', 'Larger than one kilometre', 'Exactly the size of a typical human cell', 'Only at the scale of entire planets'], 0),
    ('What is a nanomaterial?', ['A material engineered or structured at the nanoscale', 'A material that exists only in outer space', 'A material with no measurable size at all', 'A material found exclusively in living organisms'], 0),
    ('Why can a nanomaterial behave differently from the same substance at a larger scale?', ['Its properties can change significantly once its structure reaches the nanoscale', 'Nanomaterials are chemically identical to all other forms of the substance in every way', 'Size has no effect on the properties of any material', 'Nanomaterials are always heavier than their larger-scale counterparts'], 0),
    ('Which field commonly applies nanotechnology?', ['Medicine, electronics, and materials science', 'Only ancient historical research', 'Only competitive sports', 'Only culinary arts with no scientific basis'], 0),
    ('Why does surface area become especially important at the nanoscale?', ['A much larger proportion of a nanomaterials atoms are located at its surface, increasing reactivity', 'Surface area has no effect on any material at any scale', 'Nanomaterials have no surface area at all', 'Reactivity always decreases as surface area increases'], 0)]),
H('The Founding of the National Film Board of Canada in 1939',
  'Grade 10 History strand: the National Film Board of Canada was established in 1939 to produce and distribute films that would interpret Canada to Canadians and the world, playing a major role in wartime propaganda and later in the countrys documentary filmmaking tradition.',
  [('In what year was the National Film Board of Canada established?', ['1939', '1867', '1905', '1949'], 0),
   ('What was the National Film Board originally created to do?', ['Produce and distribute films that would interpret Canada to Canadians and the world', 'Regulate the price of imported films from other countries', 'Build movie theatres in every Canadian city', 'Train professional actors for the stage'], 0),
   ('What role did the National Film Board play during the Second World War?', ['It produced wartime propaganda films', 'It refused to produce any films related to the war', 'It focused exclusively on foreign films with no Canadian content', 'It was shut down for the duration of the war'], 0),
   ('What filmmaking tradition did the National Film Board become closely associated with over time?', ['Documentary filmmaking', 'Big-budget science fiction films', 'Silent-era filmmaking exclusively', 'Animated musical films only'], 0),
   ('Who was appointed to help establish and lead the early National Film Board?', ['John Grierson', 'Robert Borden', 'Mackenzie King', 'Lester Pearson'], 0)]),
]),
day(147, [
E('Grammar: Subject-Verb Agreement in Complex Sentences',
  'Grade 10 English strand: subject-verb agreement requires a verb to match its subject in number, a rule that becomes more challenging in complex sentences containing intervening phrases, collective nouns, or compound subjects joined by conjunctions.',
  [('What does subject-verb agreement require?', ['A verb to match its subject in number', 'A verb to always be in the past tense', 'A subject to always be a proper noun', 'A sentence to contain no verbs at all'], 0),
   ('Why can subject-verb agreement become more difficult in complex sentences?', ['Intervening phrases can separate the subject from its verb, creating confusion about which word the verb should match', 'Complex sentences never contain a subject or a verb', 'Subject-verb agreement only applies to one-word sentences', 'Intervening phrases always make agreement automatically correct'], 0),
   ('Which sentence demonstrates correct subject-verb agreement with an intervening phrase?', ['The list of items on the shelf was long.', 'The list of items on the shelf were long.', 'The list of items on the shelf being long.', 'The list of item on the shelf was long.'], 0),
   ('How should a verb typically agree with a compound subject joined by and?', ['The verb should usually be plural, matching the combined subject', 'The verb should always be singular regardless of the subject', 'The verb should be omitted entirely', 'The verb should match only the first noun in the subject'], 0),
   ('How does a collective noun such as team typically affect subject-verb agreement?', ['It is usually treated as singular when the group acts as one unit', 'It always requires a plural verb with no exception', 'It cannot be used as a subject at all', 'It has no effect on verb choice whatsoever'], 0)]),
M('Calculus: Areas Between Curves',
  'Grade 10 Math strand: finding the area between two curves involves subtracting the value of the lower function from the value of the upper function over a given interval and evaluating the resulting definite integral, extending the basic idea of area under a single curve.',
  [('What quantity does finding the area between two curves generally require subtracting?', ['The lower function value from the upper function value over an interval', 'The x-intercept from the y-intercept', 'The slope of one curve from the slope of another', 'The domain of a function from its range'], 0),
   ('What mathematical tool is used to evaluate the area between two curves once the functions are set up?', ['A definite integral', 'A single multiplication of two constants', 'A basic proportion with no calculus involved', 'The Pythagorean Theorem'], 0),
   ('What earlier concept does finding the area between curves extend?', ['Finding the area under a single curve', 'Solving a linear equation in one variable', 'Finding the perimeter of a rectangle', 'Graphing a single point on a coordinate plane'], 0),
   ('Why is it important to identify which function is on top over a given interval?', ['Because the area calculation depends on subtracting the lower curve from the upper curve', 'Because the top function is always irrelevant to the calculation', 'Because only the bottom function needs to be considered', 'Because area between curves never depends on the order of the functions'], 0),
   ('What must be identified first before setting up the integral for the area between two curves?', ['The points where the two curves intersect, defining the interval of integration', 'The colour used to shade the region on a graph', 'The name of the mathematician who discovered integration', 'The total number of curves that exist in mathematics'], 0)]),
Sc('Physics: Special Relativity and Time Dilation',
   'Grade 10 Science strand: special relativity, developed by Albert Einstein, describes how measurements of time and space change for observers moving at different constant speeds, predicting time dilation, in which a clock moving relative to an observer appears to run slower than a stationary one.',
   [('Who developed the theory of special relativity?', ['Albert Einstein', 'Isaac Newton', 'Galileo Galilei', 'Marie Curie'], 0),
    ('What does special relativity describe?', ['How measurements of time and space change for observers moving at different constant speeds', 'How chemical reactions occur at high temperatures', 'How plants convert sunlight into energy', 'How rocks form over geological time'], 0),
    ('What is time dilation?', ['The effect in which a moving clock appears to run slower relative to a stationary observer', 'The effect in which time always speeds up for every observer equally', 'A phenomenon that only applies to objects at rest', 'A measurement error with no real physical basis'], 0),
    ('Under what condition does time dilation become noticeable?', ['When an object moves at speeds approaching the speed of light', 'When an object is standing completely still', 'When an object is heated to room temperature', 'When an object is submerged in water'], 0),
    ('What does special relativity assume remains constant for all observers?', ['The speed of light in a vacuum', 'The mass of every object regardless of speed', 'The temperature of every object in the universe', 'The colour of light regardless of its source'], 0)]),
H('The Founding of the Canadian Wheat Board in 1935',
  'Grade 10 History strand: the Canadian Wheat Board was established in 1935 as a federal marketing agency to stabilize wheat prices and provide farmers with a more predictable and orderly system for selling grain during a period of severe agricultural hardship.',
  [('In what year was the Canadian Wheat Board established?', ['1935', '1867', '1905', '1949'], 0),
   ('What type of organization was the Canadian Wheat Board?', ['A federal marketing agency', 'A private international corporation', 'A provincial court system', 'A national police force'], 0),
   ('What commodity did the Canadian Wheat Board primarily regulate?', ['Wheat', 'Coal', 'Timber', 'Automobiles'], 0),
   ('What problem was the Canadian Wheat Board designed to address for farmers?', ['Unstable and unpredictable wheat prices', 'A shortage of farmland across the country', 'A lack of any railway access to prairie farms', 'An oversupply of manufactured goods'], 0),
   ('During what period of hardship was the Canadian Wheat Board created?', ['The Great Depression', 'The First World War', 'The Second World War', 'The Klondike Gold Rush'], 0)]),
]),
day(148, [
E('Reading: Analyzing Synecdoche and Metonymy',
  'Grade 10 English strand: synecdoche is a figure of speech in which a part represents a whole or a whole represents a part, while metonymy uses a closely associated term to stand in for something else, both allowing writers to create compact, vivid substitutions.',
  [('What does synecdoche involve?', ['A part representing a whole, or a whole representing a part', 'A direct comparison using like or as', 'A word that imitates a natural sound', 'A statement that contradicts itself for effect'], 0),
   ('What does metonymy involve?', ['A closely associated term standing in for something else', 'The repetition of the same consonant sound', 'A reversal of normal word order for emphasis', 'An exaggerated statement not meant to be taken literally'], 0),
   ('Which phrase is an example of synecdoche?', ['Referring to a car as a set of wheels', 'Describing rain as falling cats and dogs', 'Comparing a persons smile to sunshine', 'Describing silence as deafening'], 0),
   ('Which phrase is an example of metonymy?', ['Referring to the news media as the press', 'Comparing a heart to a drum', 'Describing a whisper as a roar', 'Giving a river human emotions'], 0),
   ('Why might a writer use synecdoche or metonymy?', ['To create a compact, vivid substitution that adds interest to the language', 'To remove all figurative meaning from a sentence', 'To make a sentence grammatically incorrect on purpose', 'To avoid referring to any object or idea at all'], 0)]),
M('Number Theory: The Chinese Remainder Theorem',
  'Grade 10 Math strand: the Chinese Remainder Theorem provides a method for solving a system of simultaneous congruences with pairwise coprime moduli, guaranteeing a unique solution modulo the product of those moduli.',
  [('What kind of problem does the Chinese Remainder Theorem help solve?', ['A system of simultaneous congruences', 'A single linear equation with one variable', 'The area of a triangle', 'The probability of a coin flip'], 0),
   ('What condition must the moduli in the system satisfy for the theorem to apply directly?', ['The moduli must be pairwise coprime', 'The moduli must all be equal to one another', 'The moduli must all be negative numbers', 'The moduli must be irrational numbers'], 0),
   ('What does the Chinese Remainder Theorem guarantee about the solution?', ['A unique solution modulo the product of the moduli', 'An infinite number of unrelated solutions', 'That no solution can ever exist', 'A solution only when all moduli equal zero'], 0),
   ('What earlier number theory concept does the Chinese Remainder Theorem rely on?', ['Modular arithmetic', 'The Pythagorean Theorem', 'The quadratic formula', 'Basic long division with no remainders'], 0),
   ('In which modern field is the Chinese Remainder Theorem often applied?', ['Cryptography and computer science', 'Ancient astronomy with no modern use', 'Ceramic arts and pottery design', 'Competitive swimming techniques'], 0)]),
Sc('Earth Science: Ocean Acidification and Its Effects',
   'Grade 10 Science strand: ocean acidification occurs as seawater absorbs increasing amounts of carbon dioxide from the atmosphere, lowering the oceans pH and reducing the availability of carbonate ions that many marine organisms need to build shells and skeletons.',
   [('What causes ocean acidification?', ['Seawater absorbing increasing amounts of carbon dioxide from the atmosphere', 'A sudden decrease in ocean salinity worldwide', 'The complete freezing of all ocean water', 'A reduction in the number of ocean currents'], 0),
    ('What happens to the oceans pH as acidification occurs?', ['It decreases, becoming more acidic', 'It increases, becoming more basic', 'It remains completely unchanged in every case', 'It becomes undefined and unmeasurable'], 0),
    ('What resource becomes less available to marine organisms as the ocean acidifies?', ['Carbonate ions needed to build shells and skeletons', 'Oxygen dissolved in the atmosphere', 'Freshwater entering from rivers', 'Sunlight reaching the ocean surface'], 0),
    ('Which type of marine organism is most directly threatened by reduced carbonate availability?', ['Shellfish and coral', 'Fully land-based mammals', 'Desert reptiles', 'Freshwater-only amphibians'], 0),
    ('What atmospheric change is most directly linked to rising ocean acidification?', ['Increasing atmospheric carbon dioxide levels', 'Decreasing atmospheric oxygen levels', 'Increasing atmospheric nitrogen levels', 'Decreasing atmospheric pressure worldwide'], 0)]),
H('The Ogdensburg Agreement of 1940',
  'Grade 10 History strand: the Ogdensburg Agreement of 1940 was a defence pact between Canada and the United States, negotiated by Prime Minister Mackenzie King and President Franklin Roosevelt, that created the Permanent Joint Board on Defence to coordinate the two countries military cooperation.',
  [('In what year was the Ogdensburg Agreement signed?', ['1940', '1867', '1919', '1949'], 0),
   ('Which two countries were party to the Ogdensburg Agreement?', ['Canada and the United States', 'Canada and the United Kingdom', 'Canada and France', 'The United States and Mexico'], 0),
   ('Which two leaders negotiated the Ogdensburg Agreement?', ['Prime Minister Mackenzie King and President Franklin Roosevelt', 'Prime Minister Robert Borden and President Woodrow Wilson', 'Prime Minister Lester Pearson and President John F. Kennedy', 'Prime Minister Wilfrid Laurier and President Theodore Roosevelt'], 0),
   ('What body did the Ogdensburg Agreement create?', ['The Permanent Joint Board on Defence', 'The Royal Canadian Mounted Police', 'The Bank of Canada', 'The National Film Board'], 0),
   ('What was the main purpose of the Permanent Joint Board on Defence?', ['To coordinate military cooperation between Canada and the United States', 'To regulate international trade tariffs', 'To oversee immigration policy exclusively', 'To manage national parks along the border'], 0)]),
]),
day(149, [
E('Writing: The Vignette as a Narrative Form',
  'Grade 10 English strand: a vignette is a brief, richly descriptive scene or narrative moment that captures a single impression, character, or emotion without necessarily following a complete traditional plot structure.',
  [('What is a vignette?', ['A brief, richly descriptive scene or narrative moment that captures a single impression', 'A lengthy legal contract used in publishing', 'A formal citation format used in research papers', 'A type of grammatical error found in essays'], 0),
   ('Does a vignette typically follow a complete traditional plot structure?', ['No, it often captures a moment without a full conventional plot', 'Yes, it always includes a complete beginning, middle, and end', 'Yes, it is defined by having multiple detailed subplots', 'No, a vignette never contains any descriptive detail'], 0),
   ('What might a vignette focus on capturing?', ['A single impression, character, or emotion', 'An exhaustive list of unrelated facts', 'A complete legal argument', 'A step-by-step scientific procedure'], 0),
   ('Why might a writer choose to write a vignette rather than a full short story?', ['To focus intensely on one moment or feeling without the demands of a complete plot', 'Because vignettes are required to be longer than any short story', 'Because a vignette cannot include any descriptive language', 'Because vignettes must always resolve every conflict fully'], 0),
   ('Which of the following best describes a collection of linked vignettes?', ['A series of brief, connected scenes that together build a larger impression or narrative', 'A single unbroken chapter with no scene breaks', 'A formal essay structured around a single thesis', 'A dictionary of unrelated definitions'], 0)]),
M('Probability: The Geometric Distribution',
  'Grade 10 Math strand: the geometric distribution models the number of independent trials needed to achieve the first success in a repeated experiment, where each trial has the same constant probability of success.',
  [('What does the geometric distribution model?', ['The number of independent trials needed to achieve the first success', 'The exact area under a curved graph', 'The volume of a three-dimensional solid', 'The angle between two intersecting planes'], 0),
   ('What must remain constant across each trial for the geometric distribution to apply?', ['The probability of success on each trial', 'The colour of the object being tested', 'The number of trials remaining', 'The physical location of the experiment'], 0),
   ('What condition must the trials satisfy for the geometric distribution to apply?', ['The trials must be independent of one another', 'The trials must all produce the exact same outcome', 'The trials must depend entirely on the previous result', 'The trials must occur only once in total'], 0),
   ('Which scenario could be modeled using a geometric distribution?', ['The number of times a basketball player shoots before making their first free throw', 'The exact height of a single building', 'The colour of a randomly selected object', 'The temperature of a room at a single moment'], 0),
   ('How does the geometric distribution differ from the binomial distribution?', ['The geometric distribution counts trials until the first success, while the binomial distribution counts successes in a fixed number of trials', 'The two distributions are mathematically identical in every way', 'The geometric distribution only applies to exactly two possible outcomes', 'The binomial distribution cannot be used to model any real event'], 0)]),
Sc('Biology: The Human Brain and Neuroplasticity',
   'Grade 10 Science strand: neuroplasticity is the brains ability to reorganize itself by forming new neural connections throughout life, allowing the brain to adapt to new experiences, learning, injury, and changes in the environment.',
   [('What is neuroplasticity?', ['The brains ability to reorganize itself by forming new neural connections throughout life', 'The complete inability of the brain to change after birth', 'A permanent, unchangeable structure of the nervous system', 'A condition found only in the muscular system'], 0),
    ('What can trigger the brain to form new neural connections?', ['New experiences, learning, or recovery from injury', 'A total absence of any external stimulus', 'The complete removal of the nervous system', 'Only events that occur before birth'], 0),
    ('Why is neuroplasticity important for recovery after a brain injury?', ['It allows the brain to reorganize and sometimes compensate for damaged areas', 'It guarantees that no recovery is ever possible after injury', 'It has no connection to how the brain responds to injury', 'It only occurs in organs other than the brain'], 0),
    ('At what point in life does neuroplasticity occur?', ['Throughout life, though it is often most pronounced in childhood', 'Only during a single day after birth', 'Only after the age of eighty', 'Neuroplasticity does not occur at any point in life'], 0),
    ('Why is understanding neuroplasticity valuable for education and therapy?', ['It suggests that targeted practice and experience can help reshape neural connections over time', 'It proves that learning has no effect on the brain', 'It shows that the brain is entirely fixed from birth', 'It has no practical application in either field'], 0)]),
H('The National Resources Mobilization Act of 1940',
  'Grade 10 History strand: the National Resources Mobilization Act of 1940 authorized the Canadian federal government to conscript men for home defence during the Second World War, a limited form of conscription that stopped short of requiring overseas combat service and foreshadowed the later conscription crisis of 1944.',
  [('In what year was the National Resources Mobilization Act passed?', ['1940', '1867', '1919', '1949'], 0),
   ('What did the National Resources Mobilization Act authorize the federal government to do?', ['Conscript men for home defence during the Second World War', 'Nationalize every private business in Canada', 'Establish a new national currency', 'Create a national system of public healthcare'], 0),
   ('What type of military service did the Act stop short of requiring?', ['Overseas combat service', 'Service within Canadian borders', 'Naval training exercises', 'Basic physical fitness testing'], 0),
   ('What later event did the limited conscription under this Act foreshadow?', ['The conscription crisis of 1944', 'The Halifax Explosion', 'The October Crisis', 'The Winnipeg General Strike'], 0),
   ('During which global conflict was the National Resources Mobilization Act passed?', ['The Second World War', 'The First World War', 'The Korean War', 'The Boer War'], 0)]),
]),
day(150, [
E('English Review: Media, Grammar, and Literary Devices (Days 141-149)',
  'Grade 10 English strand review: students revisit product placement, cleft sentences, allusion, the business memo and professional email, the Kunstlerroman, native advertising, subject-verb agreement in complex sentences, synecdoche and metonymy, and the vignette.',
  [('What is product placement?', ['A branded product or service featured within media content in exchange for payment or promotion', 'A method of editing film footage after production', 'A legal requirement for all television broadcasts', 'A type of movie theatre seating arrangement'], 0),
   ('What does a cleft sentence do?', ['It divides a single idea into two clauses to shift emphasis onto a particular piece of information', 'It combines two unrelated ideas into a single run-on sentence', 'It removes all punctuation from a sentence', 'It converts a sentence into a question automatically'], 0),
   ('What is an allusion?', ['A brief, indirect reference to a person, place, event, or work outside the text', 'A detailed, fully explained retelling of another entire story', 'A grammatical error found within a sentence', 'A punctuation mark used to end a question'], 0),
   ('What is a Kunstlerroman?', ['A coming-of-age narrative that follows the development of an artist from youth into creative maturity', 'A formal legal document used in court proceedings', 'A type of scientific research paper', 'A short poem with a strict rhyme scheme'], 0),
   ('What does synecdoche involve?', ['A part representing a whole, or a whole representing a part', 'A direct comparison using like or as', 'A word that imitates a natural sound', 'A statement that contradicts itself for effect'], 0)]),
M('Math Review: Calculus, Number Theory, and Probability (Days 141-149)',
  'Grade 10 Math strand review: students revisit optimization using derivatives, Wilsons Theorem, the chi-squared goodness-of-fit test, LHopitals Rule, fractals and self-similarity, recurrence relations, areas between curves, the Chinese Remainder Theorem, and the geometric distribution.',
  [('What do optimization problems in calculus typically find?', ['The maximum or minimum value of a quantity', 'The exact colour of a graphed function', 'The total number of variables in an equation', 'The name of the mathematician who first studied the function'], 0),
   ('What does Wilsons Theorem provide a test for?', ['Whether a number is prime', 'Whether a number is even', 'Whether a fraction is in lowest terms', 'Whether a shape is a regular polygon'], 0),
   ('What type of limit is LHopitals Rule designed to evaluate?', ['A limit that produces an indeterminate form such as zero over zero', 'A limit that is already a whole number with no calculation needed', 'A limit that only involves constant functions', 'A limit that cannot be expressed as a fraction of any kind'], 0),
   ('What does a recurrence relation define?', ['Each term of a sequence using one or more of the terms that came before it', 'A single isolated number with no connection to a sequence', 'The area of a two-dimensional shape', 'The angle between two intersecting lines'], 0),
   ('What does the geometric distribution model?', ['The number of independent trials needed to achieve the first success', 'The exact area under a curved graph', 'The volume of a three-dimensional solid', 'The angle between two intersecting planes'], 0)]),
Sc('Science Review: Biology, Chemistry, Physics, and Earth Science (Days 141-149)',
   'Grade 10 Science strand review: students revisit coevolution and mutualism, enzymes and biological catalysis, nuclear fission and fusion, earthquakes and seismology, stem cells and cellular differentiation, nanotechnology, special relativity and time dilation, ocean acidification, and the human brain.',
   [('What is coevolution?', ['A process in which two or more species reciprocally influence each others evolution over time', 'A process in which a single species evolves with no influence from any other organism', 'A process that only occurs in extinct species', 'A sudden, one-time genetic mutation with no evolutionary effect'], 0),
    ('What are enzymes?', ['Specialized proteins that act as biological catalysts', 'Simple sugars used only for energy storage', 'Inorganic minerals found only in rock formations', 'Waste products removed entirely from living cells'], 0),
    ('What happens during nuclear fission?', ['A heavy atomic nucleus splits into smaller nuclei, releasing energy', 'Two light nuclei combine into a heavier nucleus, releasing energy', 'An atom gains an electron with no change in energy', 'A molecule breaks down into individual atoms with no energy released'], 0),
    ('What is cellular differentiation?', ['The process by which an unspecialized cell develops into a specialized cell type', 'The process by which a cell loses its nucleus permanently', 'The process by which two unrelated organisms merge into one', 'The process by which a cell converts directly into a mineral'], 0),
    ('What is time dilation?', ['The effect in which a moving clock appears to run slower relative to a stationary observer', 'The effect in which time always speeds up for every observer equally', 'A phenomenon that only applies to objects at rest', 'A measurement error with no real physical basis'], 0)]),
H('History Review: Canada on the Eve of the Second World War (Days 141-149)',
  'Grade 10 History strand review: students revisit the On-to-Ottawa Trek, the Padlock Law, the National Housing Act, the Munich Agreement, the founding of Trans-Canada Air Lines, the National Film Board, the Canadian Wheat Board, the Ogdensburg Agreement, and the National Resources Mobilization Act.',
  [('What was the On-to-Ottawa Trek?', ['A 1935 protest march by unemployed men from federal relief camps travelling toward Ottawa', 'A ceremonial parade celebrating Canadian Confederation', 'A railway construction project connecting British Columbia to Ontario', 'A diplomatic mission sent to negotiate with the United States'], 0),
   ('What could authorities do under the Padlock Law?', ['Shut and padlock any premises used to propagate communism or bolshevism without a trial', 'Grant additional voting rights to every citizen', 'Fund new provincial highways across Quebec', 'Establish a new provincial bank'], 0),
   ('What territory did the Munich Agreement allow Nazi Germany to annex?', ['The Sudetenland region of Czechoslovakia', 'The entire nation of Poland', 'A province of Canada', 'A territory belonging to the United States'], 0),
   ('What body did the Ogdensburg Agreement create?', ['The Permanent Joint Board on Defence', 'The Royal Canadian Mounted Police', 'The Bank of Canada', 'The National Film Board'], 0),
   ('What did the National Resources Mobilization Act authorize the federal government to do?', ['Conscript men for home defence during the Second World War', 'Nationalize every private business in Canada', 'Establish a new national currency', 'Create a national system of public healthcare'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_141_150)
    append_to(10, g10_141_150)
