#!/usr/bin/env python3
"""Grade 10, Days 171-180 -- extends Grade 10 from 170 to 180 days. Topics
chosen after dumping and grepping the full existing Day 1-170 (subject,
title) list from data/grade10.json to avoid any overlap: reported speech
and indirect quotation, analyzing the epilogue and denouement, the travel
narrative and sense of place, analyzing sports broadcasting and commentary,
the detective and mystery genre, nonverbal communication and body
language, analyzing editing techniques and montage, sentence combining and
coordination strategies, and the product review and consumer persuasion;
the Sieve of Eratosthenes, the Mean Value Theorem, solving rational
inequalities, Eulerian and Hamiltonian paths, the F-distribution and
analysis of variance, spherical geometry and great circles, the rational
root theorem, antiderivatives and the indefinite integral, and the law of
large numbers; the physics of rainbows and light dispersion, the chemistry
of photography and light-sensitive compounds, sand dunes and aeolian
landforms, the human liver and detoxification, lenses and image
formation, the chemistry of soap and saponification, deltas and river
systems, fish migration and life cycles (the salmon run), and the
chemistry of fermentation and brewing; the 1957 federal election and the
end of Liberal dominance, the Canadian Bill of Rights of 1960, the
extension of the federal vote to Indigenous peoples in 1960, the
Diefenbaker government and the nuclear weapons controversy, the 1963
federal election and the return of the Liberals under Pearson, the Royal
Commission on Bilingualism and Biculturalism, the Great Flag Debate and
the adoption of the Maple Leaf in 1964, the Company of Young Canadians and
youth activism in the 1960s, and Expo 67 and the Centennial celebrations
-- continuing directly from the postwar and early Cold War history
sequence that closed Days 161-170 into the Diefenbaker-Pearson era of
Canadian history.

None of the thirty-six new subject titles above, nor the four Day 180
review titles, duplicate any (subject, title) pair found in Days 1-170 --
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
matching the Days 111-170 convention.
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


g10_171_180 = [
day(171, [
E('Grammar: Reported Speech and Indirect Quotation',
  'Grade 10 English strand: reported speech, also called indirect quotation, restates what someone said without using their exact words or quotation marks, typically shifting verb tense and pronouns to fit the perspective of the person reporting the statement.',
  [('What does reported speech do?', ['Restates what someone said without using their exact words or quotation marks', 'Repeats a statement word for word inside quotation marks', 'Removes all verbs from a sentence', 'Converts a sentence into a question with no other change'], 0),
   ('What commonly shifts when a direct quotation is converted into reported speech?', ['Verb tense and pronouns', 'The alphabet used to write the sentence', 'The language of the entire document', 'The font used to print the text'], 0),
   ('Which sentence is an example of reported speech?', ['She said that she was tired.', 'She said, I am tired.', 'Is she tired.', 'Tired, she said, I am.'], 0),
   ('Why might a writer use reported speech instead of a direct quotation?', ['To summarize what was said more smoothly within a larger narrative', 'Because reported speech always requires quotation marks', 'Because reported speech cannot include any pronouns', 'Because direct quotations are grammatically incorrect'], 0),
   ('What punctuation mark is typically absent from reported speech but present in a direct quotation?', ['Quotation marks', 'A period at the end of the sentence', 'A capital letter at the start of the sentence', 'A space between words'], 0)]),
M('Number Theory: The Sieve of Eratosthenes',
  'Grade 10 Math strand: the Sieve of Eratosthenes is an ancient algorithm for finding all prime numbers up to a given limit by systematically marking the multiples of each prime as composite, leaving only the primes unmarked once the process is complete.',
  [('What does the Sieve of Eratosthenes find?', ['All prime numbers up to a given limit', 'The exact square root of a number', 'The sum of an arithmetic series', 'The area of a triangle'], 0),
   ('How does the sieve identify composite numbers?', ['By systematically marking the multiples of each prime', 'By dividing every number by zero', 'By listing only even numbers', 'By randomly selecting numbers to remove'], 0),
   ('What remains unmarked once the Sieve of Eratosthenes process is complete?', ['The prime numbers', 'Only the composite numbers', 'Only the even numbers', 'No numbers at all'], 0),
   ('Roughly how old is the method attributed to Eratosthenes?', ['It dates back to ancient Greek mathematics', 'It was invented in the twentieth century', 'It was invented within the last decade', 'It has no known origin at all'], 0),
   ('Why is the Sieve of Eratosthenes considered an efficient method for small to moderate limits?', ['It eliminates many composite numbers at once through systematic marking rather than testing each number individually', 'It requires checking every possible divisor of every number one at a time', 'It only works for a single specific number', 'It cannot be performed without a computer'], 0)]),
Sc('Physics: The Physics of Rainbows and Light Dispersion',
   'Grade 10 Science strand: a rainbow forms when sunlight enters raindrops and is refracted, internally reflected, and dispersed into its component colours, with each colour bending at a slightly different angle due to its distinct wavelength.',
   [('What natural event causes light to disperse into a rainbow?', ['Sunlight entering raindrops and being refracted and internally reflected', 'Sunlight passing through a completely opaque object', 'Moonlight reflecting off a still lake with no droplets present', 'Sunlight being absorbed entirely by the atmosphere'], 0),
    ('Why do different colours appear at different positions in a rainbow?', ['Each colour bends at a slightly different angle due to its distinct wavelength', 'Each colour has an identical wavelength and bends the same amount', 'Colour has no effect on how light refracts', 'Raindrops only allow one colour of light to pass through at a time'], 0),
    ('What optical process occurs inside a raindrop to produce a rainbow?', ['Refraction, internal reflection, and dispersion of light', 'Complete absorption of all light with no colour produced', 'A chemical reaction between water and air', 'The raindrop generating its own light source'], 0),
    ('Which colour is typically found on the outer edge of a primary rainbow?', ['Red', 'Violet', 'Green', 'Indigo'], 0),
    ('Why must an observer face away from the sun to see a rainbow?', ['Sunlight must be refracted and reflected back toward the observer by raindrops located opposite the sun', 'Rainbows only form when an observer faces directly toward the sun', 'Rainbows form independently of the position of the sun', 'Facing the sun blocks all light from entering the eye'], 0)]),
H('The 1957 Federal Election and the End of Liberal Dominance',
  'Grade 10 History strand: the 1957 federal election ended twenty-two years of unbroken Liberal government when John Diefenbakers Progressive Conservatives won a minority government, a surprise result that reflected voter fatigue with long Liberal rule and controversies such as the Pipeline Debate.',
  [('What did the 1957 federal election end?', ['Twenty-two years of unbroken Liberal government', 'The existence of the Canadian House of Commons', 'The Canadian monarchy', 'All federal elections in Canada'], 0),
   ('Which party won the 1957 federal election?', ['The Progressive Conservatives, led by John Diefenbaker', 'The Liberals, led by Louis St. Laurent', 'The Co-operative Commonwealth Federation', 'The Social Credit Party'], 0),
   ('What type of government did the Progressive Conservatives form after the 1957 election?', ['A minority government', 'A government with every seat in the House of Commons', 'A coalition with a foreign government', 'No government was formed at all'], 0),
   ('What earlier controversy contributed to voter dissatisfaction with the Liberal government?', ['The 1956 Pipeline Debate', 'The Confederation debates of the 1860s', 'The Statute of Westminster', 'The Halifax Explosion'], 0),
   ('Why was the 1957 election result considered a surprise by many observers?', ['The Liberals had governed for over two decades and were widely expected to win again', 'No party had ever won an election in Canadian history before 1957', 'The Progressive Conservatives had never existed before 1957', 'Voting had been suspended for the previous twenty years'], 0)]),
]),
day(172, [
E('Reading: Analyzing the Epilogue and Denouement',
  'Grade 10 English strand: the denouement is the section of a narrative that resolves remaining plot threads after the climax, while an epilogue is a short concluding section, sometimes set after a time jump, that shows readers what became of the characters once the main story has ended.',
  [('What does the denouement of a narrative do?', ['Resolves remaining plot threads after the climax', 'Introduces the main conflict for the first time', 'Occurs before any characters are introduced', 'Replaces the need for a climax entirely'], 0),
   ('What is an epilogue?', ['A short concluding section that shows what became of the characters after the main story ends', 'The opening paragraph of a narrative', 'A list of characters printed before the story begins', 'A summary printed on the back cover of a book'], 0),
   ('What often distinguishes an epilogue from the rest of a narrative?', ['It is sometimes set after a time jump beyond the main events of the story', 'It always occurs at the exact midpoint of the story', 'It cannot mention any character from the main story', 'It always introduces a brand new unrelated plot'], 0),
   ('Why might an author include a denouement after the climax?', ['To give readers closure by tying up loose plot threads', 'To introduce the main conflict for the first time', 'To prevent the story from ever reaching a climax', 'To remove all sense of resolution from the narrative'], 0),
   ('How can analyzing a denouement or epilogue deepen a readers understanding of a text?', ['It reveals how the author chooses to resolve conflict and shape a final impression', 'It has no effect on how a reader interprets the story', 'It only repeats information already given in the introduction', 'It removes the need to read the rest of the narrative'], 0)]),
M('Calculus: The Mean Value Theorem',
  'Grade 10 Math strand: the Mean Value Theorem states that for a smooth, continuous function over a closed interval, there exists at least one point where the instantaneous rate of change equals the average rate of change across the entire interval.',
  [('What does the Mean Value Theorem guarantee for a smooth, continuous function over an interval?', ['At least one point where the instantaneous rate of change equals the average rate of change', 'That the function must be equal to zero somewhere in the interval', 'That the function has no derivative anywhere', 'That the interval must contain only whole numbers'], 0),
   ('What condition must a function generally satisfy for the Mean Value Theorem to apply?', ['It must be continuous and differentiable over the interval', 'It must be undefined at every point in the interval', 'It must have no defined interval at all', 'It must be a straight horizontal line only'], 0),
   ('What does the average rate of change over an interval represent graphically?', ['The slope of the secant line connecting the endpoints of the interval', 'The slope of a line tangent to the y-axis', 'The area under the curve across the interval', 'The exact value of the function at its midpoint'], 0),
   ('What does the instantaneous rate of change at a specific point represent graphically?', ['The slope of the tangent line at that point', 'The total area beneath the entire curve', 'The y-intercept of the function', 'The domain of the function'], 0),
   ('Why is the Mean Value Theorem useful in calculus?', ['It connects a functions overall behaviour on an interval to its behaviour at a specific point', 'It proves that every function has exactly one root', 'It eliminates the need to ever compute a derivative', 'It only applies to functions with no real-world meaning'], 0)]),
Sc('Chemistry: The Chemistry of Photography and Light-Sensitive Compounds',
   'Grade 10 Science strand: traditional film photography relies on light-sensitive silver halide compounds that undergo a chemical change when exposed to light, forming a latent image that is then made visible and permanent through a sequence of chemical development and fixing steps.',
   [('What type of compound makes traditional photographic film light-sensitive?', ['Silver halide compounds', 'Table salt', 'Pure carbon', 'Distilled water'], 0),
    ('What happens to a light-sensitive compound when it is exposed to light during photography?', ['It undergoes a chemical change that forms a latent image', 'It instantly evaporates with no chemical change', 'It becomes completely transparent with no image formed', 'It changes into an entirely different element'], 0),
    ('What is a latent image?', ['An invisible image formed on film that has not yet been chemically developed', 'A fully visible printed photograph with no further processing needed', 'A digital file stored on a memory card', 'An image that can never be developed under any condition'], 0),
    ('What chemical process makes a latent image visible and permanent?', ['Development and fixing', 'Freezing and melting', 'Boiling and evaporation', 'Filtration and distillation'], 0),
    ('Why must photographic film traditionally be handled in a darkroom before development?', ['Exposure to additional light would alter or destroy the latent image', 'Darkrooms have no effect on light-sensitive compounds', 'Film is only light-sensitive after development is complete', 'Light exposure has no chemical effect on silver halide compounds'], 0)]),
H('The Canadian Bill of Rights of 1960',
  'Grade 10 History strand: the Canadian Bill of Rights, introduced by Prime Minister John Diefenbaker in 1960, was the first federal statute to set out fundamental rights and freedoms for Canadians, though as an ordinary act of Parliament it carried less legal force than the Charter of Rights and Freedoms that followed decades later.',
  [('Who introduced the Canadian Bill of Rights?', ['Prime Minister John Diefenbaker', 'Prime Minister Louis St. Laurent', 'Prime Minister Lester Pearson', 'Prime Minister Mackenzie King'], 0),
   ('In what year was the Canadian Bill of Rights introduced?', ['1960', '1940', '1867', '1982'], 0),
   ('What was significant about the Canadian Bill of Rights at the federal level?', ['It was the first federal statute to set out fundamental rights and freedoms for Canadians', 'It was the first Canadian law of any kind ever passed', 'It ended all federal elections in Canada', 'It abolished the Canadian Senate'], 0),
   ('Why did the Canadian Bill of Rights carry less legal force than a constitutional document?', ['It was an ordinary act of Parliament rather than an entrenched constitutional provision', 'It applied only to citizens outside of Canada', 'It could never be cited in any court case', 'It was written entirely in a language with no legal standing'], 0),
   ('What later Canadian document expanded on the idea of protecting fundamental rights with stronger legal force?', ['The Charter of Rights and Freedoms', 'The Statute of Westminster', 'The British North America Act of 1867', 'The Quebec Act'], 0)]),
]),
day(173, [
E('Writing: The Travel Narrative and Sense of Place',
  'Grade 10 English strand: a travel narrative recounts a journey to an unfamiliar location, using vivid sensory detail to create a strong sense of place and often reflecting on how the experience of travel changed the writers perspective or understanding of the world.',
  [('What does a travel narrative typically recount?', ['A journey to an unfamiliar location', 'A single event that occurs entirely at home', 'A purely fictional world with no real setting', 'A scientific report with no narrative elements'], 0),
   ('What technique helps a travel narrative create a strong sense of place?', ['Vivid sensory detail', 'A complete absence of any description', 'A list of unrelated statistics', 'A formal legal argument'], 0),
   ('What might a travel narrative reflect on beyond simply describing a location?', ['How the experience of travel changed the writers perspective or understanding', 'The exact price of every meal purchased during the trip', 'A weather report with no personal reflection', 'A set of directions with no descriptive language'], 0),
   ('Why might sensory detail such as sound and smell be especially important in a travel narrative?', ['It helps immerse the reader in an unfamiliar setting they have not personally experienced', 'It has no effect on how a reader imagines a setting', 'Sensory detail is never included in travel writing', 'It replaces the need for any narrative structure at all'], 0),
   ('What distinguishes a travel narrative from a simple itinerary?', ['A travel narrative includes reflection and descriptive storytelling, not just a list of locations and times', 'A travel narrative never mentions any specific location', 'An itinerary always includes personal reflection', 'There is no meaningful difference between the two forms'], 0)]),
M('Algebra: Solving Rational Inequalities',
  'Grade 10 Math strand: solving a rational inequality involves finding the values of the variable that make a fraction containing that variable positive, negative, zero, or undefined, typically by identifying critical values and testing the sign of the expression across the intervals they create.',
  [('What does solving a rational inequality involve finding?', ['The values of the variable that satisfy a given inequality involving a fraction', 'The exact single value that makes the fraction equal to one', 'The name of the variable used in the expression', 'The colour used to graph the inequality'], 0),
   ('What are critical values in the context of a rational inequality?', ['Values where the numerator or denominator equals zero', 'Values that make every rational inequality false', 'Any value chosen at random with no mathematical basis', 'Values that cannot be graphed on a number line'], 0),
   ('Why must values that make the denominator of a rational inequality equal to zero be excluded?', ['Division by zero is undefined', 'Those values always satisfy the inequality', 'Excluding values has no mathematical purpose', 'Zero denominators always produce a true inequality'], 0),
   ('What is a common method for testing the sign of a rational expression across an interval?', ['Substituting a test value from each interval into the expression', 'Assuming every interval has the same sign with no testing', 'Ignoring the denominator entirely', 'Only testing the endpoints of the entire number line'], 0),
   ('How is the solution to a rational inequality typically expressed?', ['As a set of intervals on a number line', 'As a single fixed number with no range', 'As a single word with no numerical value', 'As an equation set equal to zero only'], 0)]),
Sc('Earth Science: Sand Dunes and Aeolian Landforms',
   'Grade 10 Science strand: sand dunes are aeolian landforms shaped by wind erosion and deposition, forming when wind transports and accumulates loose sand grains around an obstacle or over time, with dune shape influenced by wind direction, sand supply, and vegetation cover.',
   [('What are sand dunes an example of?', ['Aeolian landforms shaped by wind', 'Landforms shaped entirely by ocean currents', 'Landforms formed only by volcanic eruptions', 'Landforms created by glacial ice alone'], 0),
    ('What process causes sand to accumulate into a dune?', ['Wind transporting and depositing loose sand grains', 'Sand grains chemically bonding together instantly', 'A sudden drop in air temperature', 'Sand grains being magnetically attracted to one another'], 0),
    ('What factor can influence the shape of a sand dune?', ['Wind direction, sand supply, and vegetation cover', 'The exact colour of the surrounding rock', 'The phase of the moon on a given night', 'The number of animals living nearby'], 0),
    ('What term describes processes shaped primarily by wind?', ['Aeolian', 'Fluvial', 'Glacial', 'Volcanic'], 0),
    ('Why can vegetation help stabilize a sand dune?', ['Plant roots can anchor sand grains and reduce further wind erosion', 'Vegetation always increases the rate of wind erosion', 'Plants prevent wind from blowing across a dune entirely', 'Vegetation has no physical effect on loose sand'], 0)]),
H('Indigenous Peoples and the Extension of the Federal Vote in 1960',
  'Grade 10 History strand: in 1960, the Diefenbaker government extended the federal vote to First Nations peoples living on reserves without requiring them to give up their status or treaty rights, ending a long-standing restriction and marking a step toward greater political inclusion, though many barriers to full equality remained.',
  [('What change did the federal government make in 1960 regarding First Nations peoples?', ['It extended the federal vote to First Nations peoples living on reserves', 'It removed the right to vote from all Canadian citizens', 'It created an entirely new federal electoral system', 'It ended all federal elections in Canada'], 0),
   ('What did First Nations voters not have to give up in order to vote after 1960?', ['Their status or treaty rights', 'Their citizenship in Canada', 'Their right to live in Canada', 'Their right to own property'], 0),
   ('Which government extended the federal vote to First Nations peoples in 1960?', ['The Diefenbaker government', 'The Laurier government', 'The Mackenzie King government', 'The Trudeau government'], 0),
   ('What long-standing restriction did the 1960 change end?', ['A restriction that had prevented many First Nations peoples from voting in federal elections', 'A restriction on international travel for all Canadians', 'A restriction on owning a business in Canada', 'A restriction on attending public school'], 0),
   ('What remained true even after the 1960 change was made?', ['Many barriers to full equality for Indigenous peoples remained', 'All inequality faced by Indigenous peoples in Canada ended immediately', 'No further historical change affecting Indigenous rights ever occurred', 'Indigenous peoples gained full political equality with no further issues'], 0)]),
]),
day(174, [
E('Media Literacy: Analyzing Sports Broadcasting and Commentary',
  'Grade 10 English strand: sports broadcasting combines live play-by-play description with colour commentary that adds context, opinion, and analysis, shaping how an audience interprets a game through word choice, tone, and the narratives commentators choose to emphasize.',
  [('What does play-by-play description provide during a sports broadcast?', ['A live account of the action as it happens', 'A written summary published only after the event ends', 'A silent broadcast with no spoken description', 'A prerecorded segment unrelated to the live game'], 0),
   ('What does colour commentary typically add to a sports broadcast?', ['Context, opinion, and analysis', 'A completely silent broadcast', 'An unrelated news segment about world events', 'A recipe segment with no connection to sports'], 0),
   ('How can commentators shape audience interpretation of a game?', ['Through word choice, tone, and the narratives they choose to emphasize', 'Commentary has no influence on how an audience understands a game', 'By remaining completely silent throughout the broadcast', 'By reading directly from an unrelated script with no analysis'], 0),
   ('Why might media literacy be useful when watching a sports broadcast?', ['It helps viewers recognize bias or a particular narrative within the commentary', 'It guarantees that all commentary is entirely free of opinion', 'It removes the need to think critically about broadcast content', 'It proves that sports broadcasts contain no spoken language'], 0),
   ('Which of the following is an example of colour commentary rather than play-by-play?', ['An analysis of why a team changed strategy at halftime', 'A direct description of a ball crossing the goal line', 'A statement of the current score with no further comment', 'The time remaining on the game clock'], 0)]),
M('Discrete Math: Eulerian and Hamiltonian Paths',
  'Grade 10 Math strand: an Eulerian path visits every edge of a graph exactly once, while a Hamiltonian path visits every vertex of a graph exactly once, two related but distinct concepts used to model routing problems such as delivery routes and circuit design.',
  [('What must an Eulerian path visit exactly once?', ['Every edge of a graph', 'Every colour used to draw a graph', 'Every possible graph that could ever exist', 'The exact midpoint of a graph'], 0),
   ('What must a Hamiltonian path visit exactly once?', ['Every vertex of a graph', 'Every edge of a graph', 'No vertices or edges at all', 'Only the starting vertex of a graph'], 0),
   ('How do Eulerian and Hamiltonian paths differ from one another?', ['An Eulerian path focuses on edges, while a Hamiltonian path focuses on vertices', 'They are identical concepts with different names', 'An Eulerian path can never be drawn on any graph', 'A Hamiltonian path must always repeat every edge twice'], 0),
   ('Which real-world problem could be modelled using a Hamiltonian path?', ['Planning a delivery route that visits every location exactly once', 'Measuring the exact temperature of a room', 'Calculating the derivative of a polynomial function', 'Finding the area under a curve'], 0),
   ('Why are Eulerian and Hamiltonian paths useful in fields such as logistics and circuit design?', ['They provide mathematical models for efficiently visiting locations or connections without unnecessary repetition', 'They have no practical application outside of pure mathematics', 'They only apply to graphs with a single vertex', 'They eliminate the need for any planning in routing problems'], 0)]),
Sc('Biology: The Human Liver and Detoxification',
   'Grade 10 Science strand: the liver is a vital organ that filters blood from the digestive tract, breaking down toxins, metabolizing nutrients, and producing bile to aid digestion, making it central to maintaining chemical balance within the body.',
   [('What is one of the main functions of the liver?', ['Filtering blood and breaking down toxins', 'Pumping blood throughout the entire body', 'Producing sound for the vocal cords', 'Regulating body temperature directly through the skin'], 0),
    ('What substance does the liver produce to aid digestion?', ['Bile', 'Insulin', 'Saliva', 'Mucus'], 0),
    ('From where does the liver receive blood rich in absorbed nutrients?', ['The digestive tract', 'The lungs exclusively', 'The skin exclusively', 'The bones exclusively'], 0),
    ('What role does the liver play in metabolizing nutrients?', ['It processes nutrients absorbed from digestion so they can be used or stored by the body', 'It destroys all nutrients before they can be used', 'It has no involvement in nutrient processing at all', 'It only processes nutrients that enter through the skin'], 0),
    ('Why is the liver considered central to maintaining chemical balance in the body?', ['It filters toxins and regulates many substances circulating in the blood', 'It has no connection to any chemical process in the body', 'It only affects the colour of a persons hair', 'It exclusively controls eye colour'], 0)]),
H('The Diefenbaker Government and the Nuclear Weapons Controversy',
  'Grade 10 History strand: the Diefenbaker government faced a bitter controversy in the early 1960s over whether Canada should accept nuclear warheads for the Bomarc missiles and other weapons systems already stationed on Canadian soil, a dispute that divided the cabinet and contributed to the governments defeat in 1963.',
  [('What controversy did the Diefenbaker government face in the early 1960s?', ['Whether Canada should accept nuclear warheads for weapons systems already on Canadian soil', 'Whether Canada should join the United Nations', 'Whether Canada should adopt a new currency', 'Whether Canada should abolish the Senate'], 0),
   ('Which missile system was at the centre of the nuclear weapons controversy?', ['The Bomarc missile', 'The Avro Arrow', 'The V-2 rocket', 'The Sputnik satellite'], 0),
   ('How did the nuclear weapons controversy affect the Diefenbaker cabinet?', ['It divided the cabinet over whether to accept the warheads', 'It had no effect on the cabinet at all', 'It caused the cabinet to unanimously support the warheads immediately', 'It led to the permanent cancellation of the cabinet'], 0),
   ('What political outcome did the controversy contribute to?', ['The defeat of the Diefenbaker government in 1963', 'An immediate landslide re-election for Diefenbaker', 'The permanent end of federal elections in Canada', 'A formal merger of Canada with another country'], 0),
   ('What broader Cold War tension formed the backdrop of this controversy?', ['Debates over nuclear weapons and defence alliances between Western nations', 'A dispute over Arctic fishing rights', 'A trade agreement with a South American country', 'A disagreement over provincial highway funding'], 0)]),
]),
day(175, [
E('Literature: The Detective and Mystery Genre',
  'Grade 10 English strand: the detective and mystery genre centres on solving a crime or puzzle through the careful gathering of clues and logical deduction, typically following an investigator who must interpret evidence more skillfully than the reader to reach the correct solution.',
  [('What does the detective and mystery genre typically centre on?', ['Solving a crime or puzzle through the gathering of clues and logical deduction', 'A story with no conflict or problem to solve', 'A purely descriptive account of a setting with no plot', 'A collection of unrelated poems with no narrative'], 0),
   ('What skill does a detective typically use to reach a solution?', ['Logical deduction based on interpreting evidence', 'Random guessing with no basis in evidence', 'Ignoring all clues presented in the story', 'Refusing to investigate any aspect of the crime'], 0),
   ('What is a defining feature of many detective narratives?', ['The investigator interprets evidence more skillfully than the reader', 'The crime is solved before the story begins', 'No evidence is ever presented to the reader', 'The identity of the culprit is revealed in the first sentence'], 0),
   ('Why do readers often enjoy the mystery genre?', ['It invites them to piece together clues alongside the investigator', 'It removes any sense of curiosity from the reading experience', 'It provides no puzzle or problem to engage with', 'It never reveals a solution of any kind'], 0),
   ('Which of the following is a common element found in detective fiction?', ['A red herring intended to mislead the investigator and reader', 'A recipe with no connection to any crime', 'A weather report with no narrative purpose', 'A bibliography with no story elements'], 0)]),
M('Statistics: The F-Distribution and Analysis of Variance (ANOVA)',
  'Grade 10 Math strand: analysis of variance, or ANOVA, uses the F-distribution to test whether the means of three or more groups differ significantly, comparing the variation between group means to the variation within each group to determine whether the differences are likely due to chance.',
  [('What does analysis of variance, or ANOVA, test?', ['Whether the means of three or more groups differ significantly', 'Whether a single number is prime', 'The exact slope of a straight line', 'The area under a single point on a graph'], 0),
   ('What distribution does ANOVA rely on to determine significance?', ['The F-distribution', 'The binomial distribution', 'The Poisson distribution', 'The geometric distribution'], 0),
   ('What two types of variation does ANOVA compare?', ['Variation between group means and variation within each group', 'The colour of each group and its exact size', 'The alphabetical order of group names', 'The physical location where each group was measured'], 0),
   ('Why is ANOVA useful when comparing more than two groups at once?', ['It tests all group means simultaneously rather than requiring many separate pairwise tests', 'It can only be used to compare exactly two groups', 'It eliminates the need for any data collection', 'It guarantees that all group means are always identical'], 0),
   ('What might a large F-value in an ANOVA test suggest?', ['That the differences between group means are unlikely to be due to chance alone', 'That no data was collected for the study', 'That every group mean is exactly equal', 'That the study contains no groups at all'], 0)]),
Sc('Physics: Lenses and Image Formation',
   'Grade 10 Science strand: a lens is a transparent optical device that refracts light to form an image, with a converging lens bending light rays toward a focal point and a diverging lens spreading light rays apart, producing images that vary in size, orientation, and position depending on the lens type and object distance.',
   [('What does a lens do to light passing through it?', ['Refracts the light to form an image', 'Absorbs all light with no image produced', 'Reflects all light back toward its source', 'Converts light into sound waves'], 0),
    ('What does a converging lens do to light rays?', ['Bends them toward a focal point', 'Spreads them apart in every direction', 'Blocks them from passing through entirely', 'Has no effect on light rays at all'], 0),
    ('What does a diverging lens do to light rays?', ['Spreads them apart', 'Bends them toward a single focal point', 'Absorbs them completely', 'Converts them into a different colour'], 0),
    ('What factors can affect the size, orientation, and position of an image formed by a lens?', ['The type of lens and the distance of the object from the lens', 'The colour of the lens frame', 'The brand name of the lens', 'The time of day the lens is used'], 0),
    ('Which everyday device relies on lenses to form an image?', ['A camera', 'A thermometer', 'A battery', 'A speaker'], 0)]),
H('The 1963 Federal Election and the Return of the Liberals Under Pearson',
  'Grade 10 History strand: the 1963 federal election returned the Liberal Party to power under Lester Pearson, forming a minority government after the Diefenbaker Progressive Conservatives were weakened by internal divisions and the fallout from the nuclear weapons controversy.',
  [('Which party returned to power in the 1963 federal election?', ['The Liberal Party, under Lester Pearson', 'The Progressive Conservatives, under John Diefenbaker', 'The Co-operative Commonwealth Federation', 'The Reform Party'], 0),
   ('What type of government did Pearson form after the 1963 election?', ['A minority government', 'A government with every seat in the House of Commons', 'A government formed entirely of independent members', 'No government was formed at all'], 0),
   ('What weakened the Progressive Conservatives heading into the 1963 election?', ['Internal divisions and fallout from the nuclear weapons controversy', 'A complete absence of any political party in Canada', 'A sudden and total collapse of the federal government structure', 'An agreement to cancel all future elections'], 0),
   ('Who led the Liberal Party to victory in the 1963 election?', ['Lester Pearson', 'Louis St. Laurent', 'Pierre Trudeau', 'John Diefenbaker'], 0),
   ('What broader period of Canadian politics did the 1963 election help usher in?', ['The Pearson era of minority Liberal governments', 'A period with no elected government of any kind', 'The permanent dominance of a single political party with no opposition', 'The end of the Canadian parliamentary system'], 0)]),
]),
day(176, [
E('Oral Communication: Nonverbal Communication and Body Language',
  'Grade 10 English strand: nonverbal communication includes body language such as posture, gestures, facial expression, and eye contact, all of which can reinforce, contradict, or add nuance to the words a speaker uses during a presentation or conversation.',
  [('What does nonverbal communication include?', ['Body language such as posture, gestures, facial expression, and eye contact', 'Only the exact words spoken during a conversation', 'A written transcript with no spoken element', 'A single printed document with no live speaker'], 0),
   ('How can body language relate to spoken words during a presentation?', ['It can reinforce, contradict, or add nuance to what is being said', 'It always contradicts spoken words with no exception', 'It has no relationship to spoken words whatsoever', 'It completely replaces the need for any spoken words'], 0),
   ('Why might a speaker maintain eye contact during a conversation?', ['To convey confidence and engagement with the listener', 'To avoid communicating with the listener entirely', 'Because eye contact has no effect on communication', 'To signal that the conversation has ended'], 0),
   ('What might crossed arms and a lack of eye contact suggest about a speaker during a conversation?', ['Discomfort or disengagement, depending on the context', 'Complete enthusiasm and total engagement in every case', 'Nothing at all, since body language carries no meaning', 'That the speaker is about to give a formal toast'], 0),
   ('Why is awareness of nonverbal communication useful in oral communication skills?', ['It helps a speaker align their body language with their intended message', 'It removes the need to ever consider an audience', 'It guarantees that spoken words alone will always be understood correctly', 'It has no connection to effective communication of any kind'], 0)]),
M('Geometry: Spherical Geometry and Great Circles',
  'Grade 10 Math strand: spherical geometry studies shapes and angles on the surface of a sphere rather than a flat plane, where the shortest path between two points is an arc of a great circle, a concept used in real-world applications such as long-distance air and sea navigation.',
  [('What surface does spherical geometry study?', ['The surface of a sphere', 'A completely flat plane only', 'A single straight line', 'A three-dimensional cube'], 0),
   ('What represents the shortest path between two points on a sphere?', ['An arc of a great circle', 'A straight line drawn through the centre of the sphere', 'A perfectly horizontal line at the equator only', 'A path that ignores the curvature of the sphere'], 0),
   ('What is a great circle?', ['A circle on a sphere whose plane passes through the spheres centre', 'A circle drawn on a completely flat sheet of paper', 'A circle with no defined radius', 'A shape that is not actually circular at all'], 0),
   ('In which real-world field is spherical geometry commonly applied?', ['Long-distance air and sea navigation', 'Balancing a chemical equation', 'Simplifying a rational expression', 'Filing a legal document'], 0),
   ('How do the angles of a triangle drawn on a sphere differ from those of a triangle on a flat plane?', ['The angles of a spherical triangle can sum to more than 180 degrees', 'The angles of a spherical triangle always sum to exactly 90 degrees', 'Spherical triangles cannot have angles at all', 'The angles always sum to exactly 180 degrees, identical to a flat triangle'], 0)]),
Sc('Chemistry: The Chemistry of Soap and Saponification',
   'Grade 10 Science strand: soap is produced through saponification, a chemical reaction in which a fat or oil reacts with a strong base to form soap molecules and glycerol, with each soap molecule having a water-attracting head and a grease-attracting tail that allows it to lift oils away from a surface.',
   [('What chemical process produces soap?', ['Saponification', 'Electrolysis', 'Distillation', 'Combustion'], 0),
    ('What two substances react during saponification?', ['A fat or oil and a strong base', 'Water and table salt', 'Two different metals', 'Oxygen and hydrogen gas'], 0),
    ('What byproduct is formed alongside soap during saponification?', ['Glycerol', 'Carbon dioxide gas', 'Pure oxygen', 'Table sugar'], 0),
    ('What structural feature allows a soap molecule to lift grease away from a surface?', ['A water-attracting head and a grease-attracting tail', 'A single uniform charge across the entire molecule', 'An identical structure to a water molecule', 'A complete absence of any chemical bonds'], 0),
    ('Why is soaps dual structure useful for cleaning?', ['It allows soap to bind to both grease and water, letting grease be rinsed away', 'It prevents soap from ever coming into contact with water', 'It causes soap to repel all substances equally', 'It has no effect on removing dirt or grease from a surface'], 0)]),
H('The Royal Commission on Bilingualism and Biculturalism',
  'Grade 10 History strand: the Royal Commission on Bilingualism and Biculturalism was established in 1963 by the Pearson government to examine the state of bilingualism in Canada and recommend measures to better reflect the countrys English and French linguistic duality, laying groundwork for the Official Languages Act.',
  [('When was the Royal Commission on Bilingualism and Biculturalism established?', ['1963', '1867', '1931', '1982'], 0),
   ('Which government established the Royal Commission on Bilingualism and Biculturalism?', ['The Pearson government', 'The Diefenbaker government', 'The Mackenzie King government', 'The Trudeau government'], 0),
   ('What was the Royal Commission asked to examine?', ['The state of bilingualism in Canada', 'The state of Canadian agriculture', 'The design of a new Canadian flag', 'The condition of Canadian railways'], 0),
   ('What later federal legislation did the Royal Commissions work help lay the groundwork for?', ['The Official Languages Act', 'The Old Age Pensions Act', 'The Canadian Bill of Rights', 'The National Housing Act'], 0),
   ('What broader aspect of Canadian identity did the Royal Commission focus on reflecting?', ['The countrys English and French linguistic duality', 'A single unified provincial identity with no federal role', 'An exclusively agricultural national economy', 'A purely military national identity'], 0)]),
]),
day(177, [
E('Film Study: Analyzing Editing Techniques and Montage',
  'Grade 10 English strand: film editing shapes how a story is told by determining the order, pacing, and juxtaposition of shots, and montage is a specific editing technique that assembles a rapid sequence of images to condense time, build emotion, or suggest a relationship between ideas.',
  [('What does film editing shape?', ['How a story is told through the order, pacing, and juxtaposition of shots', 'Only the volume of the films soundtrack', 'The exact colour of the actors costumes', 'The physical location where a film is screened'], 0),
   ('What is montage?', ['An editing technique that assembles a rapid sequence of images', 'A single unedited continuous shot with no cuts', 'A technique used only in silent films with no sound', 'A method of removing all sound from a film entirely'], 0),
   ('What can montage help a filmmaker accomplish?', ['Condense time, build emotion, or suggest a relationship between ideas', 'Remove any sense of narrative from a film', 'Eliminate the need for any images in a scene', 'Prevent the audience from experiencing any emotion'], 0),
   ('How does the pacing of edited shots affect a viewers experience?', ['Faster cuts can create tension or excitement, while slower cuts can create calm or reflection', 'Pacing has no effect on how a viewer experiences a film', 'Every film uses identical pacing regardless of its content', 'Pacing only affects the films runtime and nothing else'], 0),
   ('Why might a filmmaker juxtapose two contrasting shots next to each other?', ['To suggest a meaningful relationship or contrast between the two images', 'To ensure the two shots have no connection to one another', 'Because juxtaposition is never used in film editing', 'To remove all meaning from the sequence of shots'], 0)]),
M('Algebra: The Rational Root Theorem',
  'Grade 10 Math strand: the Rational Root Theorem provides a method for identifying possible rational roots of a polynomial equation with integer coefficients by comparing the factors of the constant term to the factors of the leading coefficient, narrowing down candidates before testing them directly.',
  [('What does the Rational Root Theorem help identify?', ['Possible rational roots of a polynomial equation with integer coefficients', 'The exact derivative of a polynomial function', 'The area under a polynomial curve', 'The number of dimensions in a graph'], 0),
   ('What two values does the Rational Root Theorem compare?', ['The factors of the constant term and the factors of the leading coefficient', 'The exact colour and size of the graph', 'The number of variables and the number of constants', 'The degree of the polynomial and its y-intercept only'], 0),
   ('What must be true about the coefficients of a polynomial for the Rational Root Theorem to apply directly?', ['They must be integers', 'They must all be equal to zero', 'They must all be irrational numbers', 'They must be expressed only as percentages'], 0),
   ('Why is the Rational Root Theorem useful before testing candidate roots directly?', ['It narrows down a large set of possible roots to a smaller, manageable list', 'It guarantees every real number is automatically a root', 'It eliminates the need to ever solve a polynomial equation', 'It proves that no polynomial can have any rational roots'], 0),
   ('After identifying possible rational roots, what is typically done next?', ['Each candidate is tested, often using substitution or synthetic division, to confirm whether it is an actual root', 'The candidates are immediately discarded without any testing', 'The polynomial is redefined to remove all of its terms', 'The equation is declared unsolvable with no further steps'], 0)]),
Sc('Earth Science: Deltas and River Systems',
   'Grade 10 Science strand: a river delta forms where a river slows and deposits sediment as it enters a larger body of water such as a lake or ocean, building a fan-shaped or branching landform over time and creating fertile, biologically productive habitats at the rivers mouth.',
   [('Where does a river delta typically form?', ['Where a river enters a larger body of water and deposits sediment', 'At the exact source of a river high in the mountains', 'In the middle of a desert with no water present', 'Only at the bottom of a deep ocean trench'], 0),
    ('Why does a river deposit sediment as it approaches a larger body of water?', ['The river slows down, reducing its ability to carry sediment', 'The river suddenly speeds up and carries no sediment at all', 'The water instantly freezes at the rivers mouth', 'Sediment is created only at the source of the river'], 0),
    ('What shape do many river deltas form over time?', ['A fan-shaped or branching landform', 'A perfectly circular landform with no variation', 'A single straight line with no branching', 'A shape identical to a mountain peak'], 0),
    ('Why are deltas often biologically productive habitats?', ['The fertile sediment and nutrient-rich water support a wide range of plant and animal life', 'Deltas contain no nutrients of any kind', 'Deltas are always too dry to support any living organisms', 'Delta sediment actively repels all forms of life'], 0),
    ('Which factor can affect how quickly a delta forms and grows?', ['The amount of sediment carried by the river', 'The exact number of animals living nearby', 'The colour of the surrounding rock', 'The name given to the river by local residents'], 0)]),
H('The Great Flag Debate and the Adoption of the Maple Leaf in 1964',
  'Grade 10 History strand: the Great Flag Debate was a lengthy and often contentious parliamentary dispute in 1964 over adopting a new, distinctly Canadian national flag to replace the Red Ensign, resolved when the maple leaf design proposed by Lester Pearson was adopted, with the new flag raised for the first time in February 1965.',
  [('What was the Great Flag Debate about?', ['Adopting a new, distinctly Canadian national flag', 'Adopting a new national currency', 'Choosing a new national anthem', 'Selecting a new national capital city'], 0),
   ('What flag did the new Canadian flag replace?', ['The Red Ensign', 'The Union Jack of the United Kingdom', 'The flag of the United States', 'The flag of France'], 0),
   ('In what year did the Great Flag Debate take place in Parliament?', ['1964', '1867', '1949', '1982'], 0),
   ('Who proposed the maple leaf design ultimately adopted as the new flag?', ['Prime Minister Lester Pearson', 'Prime Minister John Diefenbaker', 'Prime Minister Louis St. Laurent', 'Prime Minister Pierre Trudeau'], 0),
   ('When was the new Canadian flag first raised?', ['February 1965', 'July 1867', 'January 1947', 'September 1939'], 0)]),
]),
day(178, [
E('Grammar: Sentence Combining and Coordination Strategies',
  'Grade 10 English strand: sentence combining joins two or more short, related sentences into a single, more sophisticated sentence using coordination strategies such as coordinating conjunctions, semicolons, or subordinating structures, improving flow and reducing choppy, repetitive writing.',
  [('What does sentence combining do?', ['Joins two or more short, related sentences into a single, more sophisticated sentence', 'Removes all punctuation from a paragraph', 'Splits one long sentence into many unrelated sentences', 'Deletes the subject of every sentence in a paragraph'], 0),
   ('What is one strategy used in sentence combining?', ['Using a coordinating conjunction to join related ideas', 'Removing every verb from a sentence', 'Writing every sentence in a completely different language', 'Ending every sentence with a question mark regardless of content'], 0),
   ('What problem in writing can sentence combining help reduce?', ['Choppy, repetitive writing made up of many short sentences', 'A complete absence of any punctuation', 'Overly long paragraphs with no sentences at all', 'A total lack of subjects and verbs'], 0),
   ('Which example demonstrates effective sentence combining?', ['The rain stopped, and the sun came out.', 'The rain stopped. The sun came out.', 'Rain the stopped sun the out came.', 'Stopped rain sun came out.'], 0),
   ('Why might a writer use varied sentence combining strategies throughout a piece of writing?', ['To create more natural flow and avoid a repetitive, monotonous rhythm', 'To make every sentence identical in length and structure', 'To eliminate all coordinating conjunctions from the text', 'Because sentence combining always makes writing less clear'], 0)]),
M('Calculus: Antiderivatives and the Indefinite Integral',
  'Grade 10 Math strand: an antiderivative of a function is a new function whose derivative equals the original function, and the indefinite integral represents the entire family of antiderivatives of a function, differing from one another only by a constant of integration.',
  [('What is an antiderivative of a function?', ['A new function whose derivative equals the original function', 'A function with no relationship to the original function', 'The exact same function written in a different colour', 'A function that has no derivative at all'], 0),
   ('What does the indefinite integral of a function represent?', ['The entire family of antiderivatives of that function', 'A single specific numerical value only', 'The area under a curve between two fixed points only', 'A function with no connection to derivatives'], 0),
   ('What distinguishes different antiderivatives of the same function from one another?', ['A constant of integration', 'The variable used in the original function', 'The degree of the original polynomial', 'The colour used to graph the function'], 0),
   ('Why is a constant of integration included when writing an indefinite integral?', ['Because the derivative of any constant is zero, so many antiderivatives are possible', 'Because every antiderivative must equal exactly zero', 'Because integration always produces a negative number', 'Because indefinite integrals cannot include any constant'], 0),
   ('How is antidifferentiation related to differentiation?', ['It is the reverse process of differentiation', 'It is completely unrelated to differentiation', 'It always produces the same result as differentiation', 'It can only be applied to constant functions'], 0)]),
Sc('Biology: Fish Migration and Life Cycles: The Salmon Run',
   'Grade 10 Science strand: many salmon species hatch in freshwater streams, migrate to the ocean to mature, and then return to the same freshwater stream where they hatched to spawn, a demanding life cycle known as the salmon run that plays a vital ecological role in many Canadian watersheds.',
   [('Where do many salmon species hatch?', ['In freshwater streams', 'In the deep open ocean', 'In freshwater lakes located in deserts', 'On dry land with no water present'], 0),
    ('Where do salmon typically migrate to mature after hatching?', ['The ocean', 'A landlocked desert with no water', 'A mountain summit with no water source', 'An underground cave system'], 0),
    ('What do adult salmon typically do when they are ready to spawn?', ['Return to the same freshwater stream where they hatched', 'Remain permanently in the ocean with no further migration', 'Migrate to a completely unrelated species habitat', 'Stop reproducing entirely once they reach adulthood'], 0),
    ('What term describes this demanding migratory life cycle of salmon?', ['The salmon run', 'The predator cycle', 'The photosynthetic cycle', 'The hibernation cycle'], 0),
    ('Why is the salmon run considered ecologically important in many Canadian watersheds?', ['It transports nutrients between ocean and freshwater ecosystems and supports many other species', 'It has no effect on any other species in the ecosystem', 'It removes all nutrients permanently from the watershed', 'It only affects a single unrelated species with no broader impact'], 0)]),
H('The Company of Young Canadians and Youth Activism in the 1960s',
  'Grade 10 History strand: the Company of Young Canadians was a federally funded volunteer organization created in 1966 to engage young Canadians in community development and social change projects, reflecting a broader wave of youth activism and social movements that characterized Canada and much of the world during the 1960s.',
  [('What was the Company of Young Canadians?', ['A federally funded volunteer organization created to engage young Canadians in community development', 'A branch of the Canadian military created for youth recruits', 'A private corporation focused entirely on manufacturing', 'A federal department overseeing international trade'], 0),
   ('In what year was the Company of Young Canadians created?', ['1966', '1919', '1939', '1982'], 0),
   ('What type of projects did the Company of Young Canadians focus on?', ['Community development and social change projects', 'Military training exercises only', 'International banking regulations', 'Railway construction projects only'], 0),
   ('What broader trend did the Company of Young Canadians reflect during the 1960s?', ['A wave of youth activism and social movements', 'A complete absence of youth involvement in public life', 'A decline in community organizations across Canada', 'A nationwide ban on volunteer work'], 0),
   ('How did youth activism in 1960s Canada relate to trends elsewhere in the world?', ['It reflected a broader wave of youth activism occurring in many countries during the decade', 'It occurred in complete isolation from any global trend', 'It was the only example of youth activism in world history', 'It had no connection whatsoever to international events'], 0)]),
]),
day(179, [
E('Writing: The Product Review and Consumer Persuasion',
  'Grade 10 English strand: a product review evaluates the features, quality, and value of a product for potential consumers, combining descriptive detail with persuasive language to help readers decide whether the product is worth purchasing.',
  [('What does a product review evaluate?', ['The features, quality, and value of a product for potential consumers', 'A completely fictional story with no real product involved', 'A historical event with no connection to any product', 'A scientific theory unrelated to consumer goods'], 0),
   ('What two elements does a product review typically combine?', ['Descriptive detail and persuasive language', 'A recipe and a musical score', 'A legal contract and a weather report', 'A map and a set of driving directions'], 0),
   ('What is the purpose of persuasive language within a product review?', ['To help readers decide whether the product is worth purchasing', 'To confuse the reader about the products features', 'To remove any opinion from the review entirely', 'To ensure the review contains no descriptive detail'], 0),
   ('Which of the following would likely appear in a well-written product review?', ['A specific comparison of the products strengths and weaknesses', 'A description of an unrelated historical event', 'A list of random numbers with no context', 'A summary of a different, unrelated product category'], 0),
   ('Why might a reader consult a product review before making a purchase?', ['To gain insight into the products quality and value from someone who has used it', 'Because product reviews are legally required reading before any purchase', 'Because product reviews never contain any useful information', 'To avoid learning anything about the product at all'], 0)]),
M('Probability: The Law of Large Numbers',
  'Grade 10 Math strand: the law of large numbers states that as the number of trials in a random experiment increases, the experimental probability of an outcome tends to converge toward its theoretical probability, explaining why large samples tend to produce more reliable estimates than small ones.',
  [('What does the law of large numbers describe?', ['How experimental probability converges toward theoretical probability as trials increase', 'A method for calculating the exact area of a triangle', 'A rule stating that every event has an equal chance of occurring', 'A law that applies only to numbers greater than one million'], 0),
   ('What happens to experimental probability as the number of trials in an experiment increases?', ['It tends to converge toward the theoretical probability', 'It always becomes completely random with no pattern', 'It moves further away from the theoretical probability with every trial', 'It becomes impossible to calculate at all'], 0),
   ('Why do large samples tend to produce more reliable estimates than small samples?', ['Random fluctuations tend to average out over a greater number of trials', 'Small samples always produce more accurate results than large samples', 'Sample size has no effect on the reliability of an estimate', 'Large samples always eliminate the need for any probability calculation'], 0),
   ('Which scenario illustrates the law of large numbers?', ['Flipping a coin many times and observing the proportion of heads approach one half', 'Flipping a coin exactly one time and recording the result', 'Rolling a die without recording any outcome at all', 'Calculating the area of a circle with a given radius'], 0),
   ('Why is the law of large numbers relevant to fields such as insurance and gambling?', ['It helps explain why outcomes become more predictable in aggregate over many repeated trials', 'It guarantees an individual outcome with complete certainty every time', 'It has no relevance to any real-world application', 'It only applies to a single trial and no more'], 0)]),
Sc('Chemistry: The Chemistry of Fermentation and Brewing',
   'Grade 10 Science strand: fermentation is a chemical process in which microorganisms such as yeast convert sugars into other compounds, such as alcohol and carbon dioxide, in the absence of oxygen, a reaction that underlies brewing, baking, and other food production processes.',
   [('What is fermentation?', ['A chemical process in which microorganisms convert sugars into other compounds', 'A process that only occurs at extremely high temperatures with no microorganisms involved', 'A physical process with no chemical change of any kind', 'A process that requires large amounts of oxygen to occur'], 0),
    ('Which organism commonly drives the fermentation process in brewing?', ['Yeast', 'A species of large mammal', 'A type of coral', 'A species of bird'], 0),
    ('What two compounds are commonly produced when yeast ferments sugar?', ['Alcohol and carbon dioxide', 'Table salt and pure water', 'Oxygen gas and nitrogen gas', 'Iron and copper'], 0),
    ('Under what condition does fermentation typically occur?', ['In the absence of oxygen', 'Only in the presence of large amounts of oxygen', 'Only at freezing temperatures', 'Only inside a sealed metal container with no biological activity'], 0),
    ('Which food production process relies on fermentation besides brewing?', ['Baking bread, which relies on carbon dioxide produced by yeast', 'Boiling water with no other ingredients', 'Freezing vegetables with no chemical change', 'Cutting fruit into smaller pieces'], 0)]),
H('Expo 67 and the Centennial Celebrations of Canadian Confederation',
  'Grade 10 History strand: Expo 67 was a world exposition held in Montreal in 1967 as the centrepiece of Canadas centennial celebrations marking one hundred years since Confederation, drawing tens of millions of visitors and becoming a widely remembered symbol of Canadian confidence and international engagement during the era.',
  [('What was Expo 67?', ['A world exposition held in Montreal in 1967', 'A federal election held across Canada', 'A treaty signed between Canada and France', 'A new branch of the Canadian military'], 0),
   ('What milestone did Expo 67 help celebrate?', ['One hundred years since Canadian Confederation', 'The end of the Second World War', 'The founding of the United Nations', 'The signing of the Statute of Westminster'], 0),
   ('In which Canadian city was Expo 67 held?', ['Montreal', 'Toronto', 'Vancouver', 'Ottawa'], 0),
   ('Approximately how many visitors did Expo 67 draw?', ['Tens of millions', 'Fewer than one hundred', 'Exactly one thousand', 'No visitors attended at all'], 0),
   ('What does Expo 67 often symbolize in accounts of Canadian history?', ['Canadian confidence and international engagement during the centennial era', 'A period of complete international isolation for Canada', 'The end of all international exhibitions in Canada', 'A time when Canada had no relations with other countries'], 0)]),
]),
day(180, [
E('English Review: Grammar, Reading, Writing, and Oral Communication (Days 171-179)',
  'Grade 10 English strand review: students revisit reported speech, the epilogue and denouement, the travel narrative, sports broadcasting commentary, the detective and mystery genre, nonverbal communication, film editing and montage, sentence combining, and the product review.',
  [('What does reported speech do?', ['Restates what someone said without using their exact words or quotation marks', 'Repeats a statement word for word inside quotation marks', 'Removes all verbs from a sentence', 'Converts a sentence into a question with no other change'], 0),
   ('What does the denouement of a narrative do?', ['Resolves remaining plot threads after the climax', 'Introduces the main conflict for the first time', 'Occurs before any characters are introduced', 'Replaces the need for a climax entirely'], 0),
   ('What does a travel narrative typically recount?', ['A journey to an unfamiliar location', 'A single event that occurs entirely at home', 'A purely fictional world with no real setting', 'A scientific report with no narrative elements'], 0),
   ('What does the detective and mystery genre typically centre on?', ['Solving a crime or puzzle through the gathering of clues and logical deduction', 'A story with no conflict or problem to solve', 'A purely descriptive account of a setting with no plot', 'A collection of unrelated poems with no narrative'], 0),
   ('What is montage?', ['An editing technique that assembles a rapid sequence of images', 'A single unedited continuous shot with no cuts', 'A technique used only in silent films with no sound', 'A method of removing all sound from a film entirely'], 0)]),
M('Math Review: Number Theory, Calculus, Algebra, and Statistics (Days 171-179)',
  'Grade 10 Math strand review: students revisit the Sieve of Eratosthenes, the Mean Value Theorem, rational inequalities, Eulerian and Hamiltonian paths, the F-distribution and ANOVA, spherical geometry, the Rational Root Theorem, antiderivatives, and the law of large numbers.',
  [('What does the Sieve of Eratosthenes find?', ['All prime numbers up to a given limit', 'The exact square root of a number', 'The sum of an arithmetic series', 'The area of a triangle'], 0),
   ('What does the Mean Value Theorem guarantee for a smooth, continuous function over an interval?', ['At least one point where the instantaneous rate of change equals the average rate of change', 'That the function must be equal to zero somewhere in the interval', 'That the function has no derivative anywhere', 'That the interval must contain only whole numbers'], 0),
   ('What must an Eulerian path visit exactly once?', ['Every edge of a graph', 'Every colour used to draw a graph', 'Every possible graph that could ever exist', 'The exact midpoint of a graph'], 0),
   ('What does analysis of variance, or ANOVA, test?', ['Whether the means of three or more groups differ significantly', 'Whether a single number is prime', 'The exact slope of a straight line', 'The area under a single point on a graph'], 0),
   ('What is an antiderivative of a function?', ['A new function whose derivative equals the original function', 'A function with no relationship to the original function', 'The exact same function written in a different colour', 'A function that has no derivative at all'], 0)]),
Sc('Science Review: Physics, Chemistry, Earth Science, and Biology (Days 171-179)',
   'Grade 10 Science strand review: students revisit light dispersion in rainbows, the chemistry of photography, sand dunes, the human liver, lenses and image formation, soap and saponification, deltas and river systems, the salmon run, and the chemistry of fermentation.',
   [('What natural event causes light to disperse into a rainbow?', ['Sunlight entering raindrops and being refracted and internally reflected', 'Sunlight passing through a completely opaque object', 'Moonlight reflecting off a still lake with no droplets present', 'Sunlight being absorbed entirely by the atmosphere'], 0),
    ('What type of compound makes traditional photographic film light-sensitive?', ['Silver halide compounds', 'Table salt', 'Pure carbon', 'Distilled water'], 0),
    ('What is one of the main functions of the liver?', ['Filtering blood and breaking down toxins', 'Pumping blood throughout the entire body', 'Producing sound for the vocal cords', 'Regulating body temperature directly through the skin'], 0),
    ('What chemical process produces soap?', ['Saponification', 'Electrolysis', 'Distillation', 'Combustion'], 0),
    ('What term describes the demanding migratory life cycle of salmon?', ['The salmon run', 'The predator cycle', 'The photosynthetic cycle', 'The hibernation cycle'], 0)]),
H('History Review: The Diefenbaker-Pearson Era in Canada (Days 171-179)',
  'Grade 10 History strand review: students revisit the 1957 federal election, the Canadian Bill of Rights of 1960, the extension of the federal vote to Indigenous peoples, the nuclear weapons controversy, the 1963 election, the Royal Commission on Bilingualism and Biculturalism, the flag debate, youth activism, and Expo 67.',
  [('Which party won the 1957 federal election?', ['The Progressive Conservatives, led by John Diefenbaker', 'The Liberals, led by Louis St. Laurent', 'The Co-operative Commonwealth Federation', 'The Social Credit Party'], 0),
   ('In what year was the Canadian Bill of Rights introduced?', ['1960', '1940', '1867', '1982'], 0),
   ('What did the federal government do in 1960 regarding First Nations peoples?', ['It extended the federal vote to First Nations peoples living on reserves', 'It removed the right to vote from all Canadian citizens', 'It created an entirely new federal electoral system', 'It ended all federal elections in Canada'], 0),
   ('What was the Great Flag Debate about?', ['Adopting a new, distinctly Canadian national flag', 'Adopting a new national currency', 'Choosing a new national anthem', 'Selecting a new national capital city'], 0),
   ('What milestone did Expo 67 help celebrate?', ['One hundred years since Canadian Confederation', 'The end of the Second World War', 'The founding of the United Nations', 'The signing of the Statute of Westminster'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_171_180)
    append_to(10, g10_171_180)
