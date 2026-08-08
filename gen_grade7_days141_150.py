#!/usr/bin/env python3
"""Grade 7, Days 141-150 -- extends Grade 7 from 140 to 150 days. Topics
chosen after reading the full Day 1-140 title list (data/grade7.json) to
avoid any overlap, since Grade 7's earlier 140 days already cover an
unusually exhaustive range of subject matter across all four subjects.
Fresh, non-duplicate topics picked this batch: modal verbs, jargon and
technical vocabulary, frame narratives, writing a feature article,
distinguishing fact from opinion in news, conjunctive adverbs, slang and
changing language, cliffhangers and suspense, writing a blog post;
slope-intercept form, inscribed and circumscribed circles, stocks and
basic investing, standard deviation, calculating density using mass and
volume, rearranging formulas, the golden ratio, fair and unfair games,
comparing subscription and phone plans; extremophiles, CRISPR and gene
editing, exoplanets, endothermic and exothermic reactions, the ozone
layer, acid rain, biomimicry, wildfire ecology, the human microbiome;
the Durham Report and responsible government, the Great Coalition and
the Charlottetown Conference of 1864, Canadas role in the Boer War, the
North-West Rebellion of 1885, Aboriginal veterans and wartime
contributions, the Halibut Treaty of 1923, the Asbestos Strike of 1949,
the Rideau Canal, and the Just Society. Day 150 is a cross-subject review
day drawing quiz content from Days 141-149 of this batch, with review
titles kept textually distinct from every earlier review day (including
Day 140's).

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are dropped entirely, matching the convention established in
gen_grade7_days111_120.py, gen_grade7_days121_130.py, and
gen_grade7_days131_140.py (e.g. "Canadas" not "Canada's").

Usage:
  cd ~/gradesbooster && python3 gen_grade7_days141_150.py
  cd ~/gradesbooster && python3 build_json.py --grade 7
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


g7_141_150 = [
day(141, [
L('Grammar: Modal Verbs and Degrees of Certainty',
  'Grade 7 Language strand: modal verbs such as can, could, may, might, must, and should show degrees of possibility, permission, ability, or obligation, letting a writer express how certain or uncertain a statement is.',
  [('What do modal verbs generally express?', ['Degrees of possibility, permission, ability, or obligation', 'The exact spelling of a word', 'A concept unrelated to grammar', 'The number of syllables in a sentence'], 0),
   ('Which of these words is a modal verb?', ['Must', 'Quickly', 'Blue', 'Running'], 0),
   ('Which modal verb generally suggests the strongest degree of certainty?', ['Must', 'Might', 'Could', 'May'], 0),
   ('Why might a writer choose might instead of must in a sentence?', ['To show that something is only possible rather than certain', 'Might and must always mean exactly the same thing', 'A concept unrelated to modal verbs', 'Might can never be used to express possibility'], 0),
   ('Which sentence correctly uses a modal verb to show obligation?', ['Students must submit their assignments by Friday.', 'Students submit Friday must assignments their by.', 'Friday students by must their submit assignments.', 'Assignments Friday must students their by submit.'], 0)]),
M('Algebra: The Slope-Intercept Form of a Linear Equation',
  'Grade 7 Math strand: the slope-intercept form of a linear equation, y = mx + b, describes a straight line using its slope, m, and its y-intercept, b, the point where the line crosses the y-axis.',
  [('In the equation y = mx + b, what does m represent?', ['The slope of the line', 'The y-intercept of the line', 'A concept unrelated to linear equations', 'The x-intercept of the line'], 0),
   ('In the equation y = mx + b, what does b represent?', ['The y-intercept of the line', 'The slope of the line', 'A concept unrelated to linear equations', 'The steepness of the line only'], 0),
   ('In the equation y = 3x + 5, what is the slope of the line?', ['3', '5', '8', '15'], 0),
   ('In the equation y = 3x + 5, at what point does the line cross the y-axis?', ['(0, 5)', '(5, 0)', '(3, 5)', '(0, 3)'], 0),
   ('Why is slope-intercept form useful for quickly graphing a line?', ['It directly shows both the steepness and the starting point without extra calculation', 'It never provides any useful information about a line', 'A concept unrelated to graphing', 'It can only be used for lines that pass through the origin'], 0)]),
Sc('Extremophiles: Life in Earths Most Extreme Environments',
   'Grade 7 Science strand: extremophiles are organisms that thrive in conditions once thought too harsh for life, such as boiling hydrothermal vents, highly acidic pools, or extreme cold, expanding scientists understanding of where life can exist.',
   [('What is an extremophile?', ['An organism that thrives in extremely harsh environmental conditions', 'An organism that can only survive in mild, comfortable conditions', 'A concept unrelated to biology', 'A type of rock formed under extreme pressure'], 0),
    ('Which environment might host extremophiles?', ['Boiling hydrothermal vents on the ocean floor', 'A climate-controlled greenhouse only', 'A concept unrelated to extremophiles', 'An environment with absolutely no water or chemicals'], 0),
    ('Why do scientists studying the possibility of life on other planets pay close attention to extremophiles?', ['Extremophiles show that life can survive in conditions once thought impossible, widening where life might be found', 'Extremophiles prove that life can never exist anywhere except Earth', 'A concept unrelated to astrobiology', 'Extremophiles have no relevance to the search for life beyond Earth'], 0),
    ('What is one adaptation that might help an extremophile survive extreme heat?', ['Heat-resistant proteins that do not break down at high temperatures', 'A complete absence of any proteins in its cells', 'A concept unrelated to extremophiles', 'An inability to survive above freezing temperatures'], 0),
    ('Why might extremophiles be useful in industrial or medical applications?', ['Their heat- or acid-resistant enzymes can function reliably in harsh industrial processes', 'Extremophile enzymes always stop working outside of a laboratory setting', 'This concept has no connection to science', 'Extremophiles have never been used in any industrial or medical application'], 0)]),
SS('Social Studies: The Durham Report and the Path to Responsible Government',
   'Grade 7 Social Studies strand: after the Rebellions of 1837, Lord Durham was sent to investigate and his 1839 report recommended uniting Upper and Lower Canada and granting responsible government, in which the executive would answer to elected representatives.',
   [('Why was Lord Durham sent to British North America in 1838?', ['To investigate the causes of the Rebellions of 1837 and recommend reforms', 'To negotiate a trade agreement with the United States', 'A concept unrelated to Canadian history', 'To lead a military campaign against a foreign country'], 0),
    ('What did the Durham Report recommend regarding Upper and Lower Canada?', ['Uniting them into a single colony', 'Dividing them into four separate colonies', 'A concept unrelated to the Durham Report', 'Ending all government in both colonies entirely'], 0),
    ('What does responsible government mean?', ['The executive branch must answer to and hold the confidence of elected representatives', 'A government with no elected representatives of any kind', 'A concept unrelated to Canadian history', 'A government controlled entirely by a foreign monarch with no local input'], 0),
    ('In what year was the Durham Report presented?', ['1839', '1867', '1812', '1791'], 0),
    ('Why is the Durham Report considered an important step toward Confederation?', ['It set in motion political changes that pushed the colonies toward greater self-government', 'It had no lasting influence on any later political developments', 'This concept has no relevance to social studies', 'It immediately ended all connection between the colonies and Britain'], 0)]),
]),
day(142, [
L('Vocabulary: Jargon and Technical Vocabulary',
  'Grade 7 Language strand: jargon is specialized vocabulary used within a particular profession or field, such as medicine or computer science, that can be precise for insiders but confusing for readers outside that field.',
  [('What is jargon?', ['Specialized vocabulary used within a particular profession or field', 'A word that has exactly the same meaning in every possible context', 'A concept unrelated to vocabulary', 'A type of punctuation used only in technical writing'], 0),
   ('Why might jargon confuse a general audience?', ['It relies on specialized terms that outsiders to the field may not know', 'Jargon is always identical to everyday, common vocabulary', 'A concept unrelated to jargon', 'General audiences always understand every field of specialized vocabulary'], 0),
   ('Which of these is an example of computer science jargon?', ['Algorithm', 'Blue', 'A concept unrelated to vocabulary', 'Running'], 0),
   ('Why might a writer choose to avoid heavy jargon when writing for a general audience?', ['To make the writing clear and accessible to readers unfamiliar with the field', 'Jargon always makes writing easier for every possible reader to understand', 'This concept has no connection to vocabulary', 'General audiences always prefer highly specialized terminology'], 0),
   ('Why might jargon still be useful within a specific professional community?', ['It allows precise, efficient communication among people who share the same specialized knowledge', 'Jargon never serves any useful purpose, even among experts', 'This concept has no relevance to vocabulary', 'Professional communities always avoid using any specialized terms'], 0)]),
M('Geometry: Inscribed and Circumscribed Circles',
  'Grade 7 Math strand: an inscribed circle fits perfectly inside a polygon, touching each side exactly once, while a circumscribed circle passes through every vertex of a polygon, surrounding it completely.',
  [('What does it mean for a circle to be inscribed in a polygon?', ['The circle fits inside the polygon and touches each side exactly once', 'The circle passes through every vertex of the polygon', 'A concept unrelated to geometry', 'The circle has no connection to the polygon at all'], 0),
   ('What does it mean for a circle to be circumscribed about a polygon?', ['The circle passes through every vertex of the polygon', 'The circle fits entirely inside the polygon with no contact to its sides', 'A concept unrelated to circumscribed circles', 'The circle overlaps only one side of the polygon'], 0),
   ('Which circle passes through every vertex of a triangle?', ['The circumscribed circle', 'The inscribed circle', 'A concept unrelated to triangles', 'Neither circle ever touches a vertex'], 0),
   ('Which circle touches each side of a triangle exactly once?', ['The inscribed circle', 'The circumscribed circle', 'A concept unrelated to inscribed circles', 'Neither circle ever touches a side'], 0),
   ('Why might architects and designers use inscribed and circumscribed circles when planning circular layouts around polygons?', ['They help position a circle so it fits precisely inside or around a polygonal shape', 'Inscribed and circumscribed circles have no practical design applications', 'This concept has no relevance to geometry', 'These circles can only be drawn around shapes with curved sides'], 0)]),
Sc('CRISPR and Modern Gene Editing',
   'Grade 7 Science strand: CRISPR is a gene-editing tool that allows scientists to precisely cut and modify sections of DNA, opening possibilities for treating genetic diseases, improving crops, and advancing biological research.',
   [('What does CRISPR allow scientists to do?', ['Precisely cut and modify specific sections of DNA', 'Observe distant galaxies in high resolution', 'A concept unrelated to science', 'Measure the exact age of a fossil instantly'], 0),
    ('Which of these is a potential application of CRISPR technology?', ['Treating certain genetic diseases', 'Predicting tomorrows weather with certainty', 'A concept unrelated to gene editing', 'Converting sound waves directly into light'], 0),
    ('Why might CRISPR be useful for improving crops?', ['It can be used to edit genes that affect traits like drought resistance or yield', 'It has no possible application in agriculture', 'A concept unrelated to CRISPR', 'It can only be used on animals, never on plants'], 0),
    ('Why do many scientists consider CRISPR a major advance over earlier gene-editing methods?', ['It allows far more precise targeting of specific DNA sequences', 'It is far less precise than every method used before it', 'This concept has no connection to science', 'CRISPR cannot target any specific section of DNA'], 0),
    ('Why does CRISPR raise ethical questions among scientists and the public?', ['Editing genes, especially in humans, raises questions about safety and the limits of altering life', 'Gene editing raises no ethical questions of any kind', 'This concept has no relevance to science', 'CRISPR has never been discussed in relation to ethics'], 0)]),
SS('Social Studies: The Great Coalition and the Charlottetown Conference of 1864',
   'Grade 7 Social Studies strand: in 1864 political rivals in the Province of Canada formed the Great Coalition to pursue federal union, then met with Maritime delegates at the Charlottetown Conference to begin negotiating the terms that would lead to Confederation in 1867.',
   [('What was the Great Coalition of 1864?', ['An alliance of political rivals in the Province of Canada formed to pursue federal union', 'A treaty signed between Canada and France', 'A concept unrelated to Canadian history', 'A military alliance formed to fight a foreign war'], 0),
    ('What was the original purpose of the Charlottetown Conference?', ['Maritime leaders planned to discuss a union of the Maritime colonies', 'To formally end all discussion of any colonial union', 'A concept unrelated to the Charlottetown Conference', 'To negotiate an end to a war with the United States'], 0),
    ('Why did delegates from the Province of Canada attend the Charlottetown Conference?', ['To propose a broader union that would eventually include all the colonies', 'They attended purely by accident with no political purpose', 'A concept unrelated to Confederation', 'To formally reject any possibility of future union'], 0),
    ('In what year did the Charlottetown Conference take place?', ['1864', '1867', '1812', '1885'], 0),
    ('Why is the Charlottetown Conference considered a key early step toward Confederation?', ['It began the formal discussions that eventually led to Confederation in 1867', 'It permanently ended any talk of uniting the colonies', 'This concept has no relevance to social studies', 'It had no connection whatsoever to the events of 1867'], 0)]),
]),
day(143, [
L('Reading: Analyzing Frame Narratives (Stories Within Stories)',
  'Grade 7 Language strand: a frame narrative is a story that contains another story inside it, using an outer story to introduce, connect, or give context to one or more inner stories told by a character.',
  [('What is a frame narrative?', ['A story that contains another story told within it', 'A story that never contains any other story', 'A concept unrelated to reading', 'A story with no characters of any kind'], 0),
   ('What role does the outer story typically play in a frame narrative?', ['It introduces and provides context for the inner story or stories', 'It has no connection to the inner story at all', 'A concept unrelated to frame narratives', 'It always replaces the inner story completely'], 0),
   ('Why might an author use a frame narrative structure?', ['To add context, perspective, or a reason for the inner story being told', 'Frame narratives never add any context to a story', 'This concept has no connection to reading', 'A frame narrative always removes all context from a story'], 0),
   ('Which situation describes a frame narrative?', ['A character in a present-day story begins telling a tale from years earlier', 'A story that features only one single unbroken scene', 'A concept unrelated to frame narratives', 'A poem with no characters or plot at all'], 0),
   ('How does a frame narrative differ from a story with a single, straightforward plot?', ['It layers at least one additional story inside an outer story', 'A frame narrative always has fewer characters than a straightforward story', 'This concept has no relevance to reading', 'Frame narratives and straightforward plots are always identical in structure'], 0)]),
M('Financial Literacy: Understanding Stocks and Basic Investing',
  'Grade 7 Math strand: a stock represents partial ownership in a company, and its price can rise or fall based on factors like company performance and investor demand, making diversification an important strategy for managing risk.',
  [('What does owning a share of stock represent?', ['Partial ownership in a company', 'A guaranteed loan made to a company', 'A concept unrelated to financial literacy', 'A fixed amount of cash with no connection to a company'], 0),
   ('What is one factor that can cause a stocks price to change?', ['Changes in company performance or investor demand', 'Stock prices never change once a company is created', 'A concept unrelated to investing', 'The price of a stock is fixed permanently by law'], 0),
   ('What does diversification mean in the context of investing?', ['Spreading money across different investments to help manage risk', 'Putting all available money into a single stock', 'A concept unrelated to investing', 'Avoiding investing in anything at all'], 0),
   ('If an investor buys a stock at ten dollars and sells it later at fifteen dollars, what is the profit per share?', ['Five dollars', 'Ten dollars', 'Fifteen dollars', 'Twenty-five dollars'], 0),
   ('Why is investing in stocks generally considered riskier than keeping money in a basic savings account?', ['Stock prices can fluctuate and there is no guarantee of a return', 'Stock prices always increase steadily with absolutely no risk involved', 'A concept unrelated to financial literacy', 'Savings accounts are always riskier than owning stock'], 0)]),
Sc('Exoplanets and the Search for Life Beyond Earth',
   'Grade 7 Science strand: an exoplanet is a planet that orbits a star outside our solar system, and scientists study exoplanets located in a stars habitable zone to look for conditions, such as liquid water, that might support life.',
   [('What is an exoplanet?', ['A planet that orbits a star outside our solar system', 'A moon that orbits a planet within our solar system', 'A concept unrelated to astronomy', 'A star located at the center of our solar system'], 0),
    ('What is a habitable zone?', ['The region around a star where conditions might allow liquid water to exist', 'A region where no star can ever form', 'A concept unrelated to exoplanets', 'The exact center of a star, where temperatures are highest'], 0),
    ('Why do scientists consider liquid water important when searching for life on other planets?', ['Liquid water is considered essential for life as we understand it on Earth', 'Liquid water has no connection to how life exists on Earth', 'A concept unrelated to astrobiology', 'Scientists have concluded water always prevents life from forming'], 0),
    ('How do astronomers often detect exoplanets that cannot be seen directly?', ['By observing the slight dimming of a stars light as a planet passes in front of it', 'By listening for radio signals sent directly from the planet', 'A concept unrelated to exoplanet detection', 'Exoplanets can never be detected using any method'], 0),
    ('Why is finding an exoplanet in a habitable zone not proof that life exists there?', ['A habitable zone only indicates conditions that could support life, not confirmed evidence of it', 'A habitable zone always guarantees that life exists on a planet', 'This concept has no relevance to science', 'Habitable zones have no connection to the possibility of life'], 0)]),
SS('Social Studies: Canadas Role in the Boer War',
   'Grade 7 Social Studies strand: Canada sent volunteer troops to support Britain in the Boer War in South Africa beginning in 1899, marking one of the first times Canadian soldiers fought overseas and sparking early debate over Canadas responsibilities within the British Empire.',
   [('Where did the Boer War take place?', ['South Africa', 'Western Europe', 'A concept unrelated to Canadian history', 'Northern Canada'], 0),
    ('Why did Canada send troops to the Boer War?', ['To support Britain as a member of the British Empire', 'To support an entirely unrelated country with no historical ties to Canada', 'A concept unrelated to the Boer War', 'Canada was legally required to send troops with no choice involved'], 0),
    ('In what year did Canada first send troops to the Boer War?', ['1899', '1867', '1914', '1885'], 0),
    ('Why is the Boer War significant in Canadian military history?', ['It marked one of the first times Canadian troops fought overseas', 'It was the only war Canada has ever participated in', 'A concept unrelated to Canadian history', 'Canadian troops refused to take part in the conflict entirely'], 0),
    ('What debate did Canadas involvement in the Boer War spark at home?', ['Disagreement over how much Canada should be obligated to support British military efforts', 'Complete agreement among all Canadians with no debate at all', 'This concept has no relevance to social studies', 'A debate over whether Canada should stop trading with Britain entirely'], 0)]),
]),
day(144, [
L('Writing: Writing a Feature Article',
  'Grade 7 Language strand: a feature article explores a topic in greater depth than a straightforward news story, often including background research, direct quotations, and a narrative angle that engages readers beyond the basic facts.',
  [('How does a feature article generally differ from a straightforward news story?', ['It explores a topic in greater depth, often with a narrative angle', 'It always avoids providing any factual information', 'A concept unrelated to writing', 'It must always be shorter than a basic news story'], 0),
   ('What might a feature article include to support its exploration of a topic?', ['Background research and direct quotations', 'Only a single sentence with no supporting details', 'A concept unrelated to feature articles', 'A list of unrelated statistics with no context'], 0),
   ('Why might a feature article use a narrative angle?', ['To engage readers with a compelling perspective rather than only listing facts', 'A narrative angle always makes an article less engaging', 'This concept has no connection to writing', 'Feature articles are required to avoid any storytelling elements'], 0),
   ('Which topic might work well for a feature article?', ['An in-depth look at a local community garden and the people who run it', 'A single sentence announcing a temperature reading', 'A concept unrelated to feature articles', 'A list of numbers with no explanation of context'], 0),
   ('Why is interviewing sources often an important step in writing a feature article?', ['Direct quotations add credibility and a personal perspective to the article', 'Interviews are never useful when writing an article', 'This concept has no relevance to writing', 'Feature articles are required to avoid quoting any sources'], 0)]),
M('Data Management: Standard Deviation (An Introduction to Spread)',
  'Grade 7 Math strand: standard deviation measures how spread out data values are around the mean, with a small standard deviation showing values clustered close to the mean and a large standard deviation showing values spread far apart.',
  [('What does standard deviation measure?', ['How spread out data values are around the mean', 'The single largest value in a data set', 'A concept unrelated to data management', 'The exact number of values collected in a survey'], 0),
   ('What does a small standard deviation suggest about a data set?', ['The values are clustered close to the mean', 'The values are spread out extremely far from the mean', 'A concept unrelated to standard deviation', 'The data set contains no numerical values at all'], 0),
   ('What does a large standard deviation suggest about a data set?', ['The values are spread out far from the mean', 'The values are always identical to one another', 'A concept unrelated to standard deviation', 'The data set has no mean of any kind'], 0),
   ('Why is standard deviation useful when comparing two data sets with the same mean?', ['It reveals which data set has more variability even when the averages match', 'Standard deviation can never be used to compare two data sets', 'A concept unrelated to data management', 'Standard deviation always produces identical results for every data set'], 0),
   ('Why is standard deviation generally considered a more detailed measure of spread than range alone?', ['It takes every value in the data set into account rather than just the highest and lowest', 'Standard deviation ignores every value except the highest one', 'This concept has no relevance to data management', 'Range always provides more detail about a data sets spread than standard deviation'], 0)]),
Sc('Chemistry: Endothermic and Exothermic Reactions',
   'Grade 7 Science strand: an exothermic reaction releases energy, often as heat, into its surroundings, while an endothermic reaction absorbs energy from its surroundings, often causing the surrounding temperature to drop.',
   [('What happens during an exothermic reaction?', ['Energy is released into the surroundings', 'Energy is absorbed from the surroundings', 'A concept unrelated to chemistry', 'No energy change occurs of any kind'], 0),
    ('What happens during an endothermic reaction?', ['Energy is absorbed from the surroundings', 'Energy is released into the surroundings', 'A concept unrelated to endothermic reactions', 'The reaction always produces a bright flame'], 0),
    ('Which of these is an example of an exothermic reaction?', ['Burning wood in a campfire', 'Melting an ice cube using only body heat', 'A concept unrelated to chemical reactions', 'Dissolving a small amount of salt in cold water'], 0),
    ('Why might the temperature of a container feel colder during an endothermic reaction?', ['The reaction is absorbing heat energy from its surroundings', 'The reaction is releasing large amounts of heat into its surroundings', 'This concept has no connection to science', 'Endothermic reactions never involve any change in temperature'], 0),
    ('Why is it useful for scientists to classify reactions as endothermic or exothermic?', ['It helps predict how a reaction will affect the temperature of its environment', 'This classification has no practical use in science', 'A concept unrelated to chemical reactions', 'Every reaction produces the exact same temperature change'], 0)]),
SS('Social Studies: The North-West Rebellion of 1885',
   'Grade 7 Social Studies strand: the North-West Rebellion of 1885 was an armed resistance led by Louis Riel and Metis and First Nations allies against the Canadian government over land rights and settler encroachment, ending in defeat and Riels execution for treason.',
   [('Who led the North-West Rebellion of 1885?', ['Louis Riel', 'Sir John A. Macdonald', 'Lester B. Pearson', 'Pierre Trudeau'], 0),
    ('What were some of the main concerns behind the North-West Rebellion?', ['Land rights and encroachment by settlers on Metis and First Nations territory', 'A disagreement over which language should be spoken in Parliament', 'A concept unrelated to Canadian history', 'A dispute over control of a coastal fishing route'], 0),
    ('In what year did the North-West Rebellion take place?', ['1885', '1867', '1812', '1837'], 0),
    ('What happened to Louis Riel after the rebellion was defeated?', ['He was tried and executed for treason', 'He was elected prime minister shortly afterward', 'A concept unrelated to the North-West Rebellion', 'He received no consequences of any kind'], 0),
    ('How did the North-West Rebellion differ from the earlier Red River Resistance?', ['It involved armed conflict and ended in military defeat rather than a negotiated settlement', 'It involved no conflict of any kind and ended peacefully', 'This concept has no relevance to social studies', 'The two events took place in exactly the same year'], 0)]),
]),
day(145, [
L('Media Literacy: Distinguishing Fact from Opinion in News',
  'Grade 7 Language strand: a fact can be verified with evidence, while an opinion expresses a personal judgment or belief, and recognizing the difference helps readers evaluate news coverage more critically.',
  [('What is a fact?', ['A statement that can be verified with evidence', 'A statement that expresses a personal judgment or belief', 'A concept unrelated to media literacy', 'A statement that can never be proven true or false'], 0),
   ('What is an opinion?', ['A statement that expresses a personal judgment or belief', 'A statement that can always be verified with hard evidence', 'A concept unrelated to media literacy', 'A statement with no connection to a persons viewpoint'], 0),
   ('Which of these sentences is a fact rather than an opinion?', ['Water boils at 100 degrees Celsius at sea level.', 'That was the best movie ever made.', 'Blue is clearly the most beautiful colour.', 'This restaurant serves the tastiest food in town.'], 0),
   ('Why might a news article blend facts and opinions without clearly labeling them?', ['To try to influence readers while appearing to present straightforward information', 'News articles are legally required to separate every fact from every opinion', 'A concept unrelated to media literacy', 'Blending facts and opinions never has any effect on readers'], 0),
   ('Why is it important for readers to distinguish fact from opinion in news coverage?', ['It helps readers evaluate information critically rather than accepting every claim as verified', 'Distinguishing fact from opinion serves no useful purpose for readers', 'This concept has no relevance to media literacy', 'All news coverage contains only verified facts and never any opinions'], 0)]),
M('Measurement: Calculating Density Using Mass and Volume',
  'Grade 7 Math strand: density is calculated by dividing an objects mass by its volume, giving a measure of how tightly matter is packed into a given space, which is why objects of the same size can have very different weights.',
  [('What formula is used to calculate density?', ['Mass divided by volume', 'Volume divided by mass', 'A concept unrelated to measurement', 'Mass multiplied by volume'], 0),
   ('If an object has a mass of 50 grams and a volume of 10 cubic centimetres, what is its density?', ['5 grams per cubic centimetre', '10 grams per cubic centimetre', '50 grams per cubic centimetre', '500 grams per cubic centimetre'], 0),
   ('Why can two objects of the same size have very different masses?', ['They can have different densities, meaning matter is packed differently within the same volume', 'Two objects of the same size are always exactly the same mass', 'A concept unrelated to density', 'Volume has no connection to mass or density at all'], 0),
   ('What units might density commonly be expressed in?', ['Grams per cubic centimetre', 'Degrees Celsius', 'A concept unrelated to density', 'Seconds per metre'], 0),
   ('Why does an object with a lower density than water generally float?', ['It has less mass packed into the same volume, making it lighter for its size than the water it displaces', 'Objects with a lower density than water always sink immediately', 'This concept has no relevance to measurement', 'Floating has no connection to an objects density'], 0)]),
Sc('The Ozone Layer and Its Protective Role',
   'Grade 7 Science strand: the ozone layer is a region of the upper atmosphere containing a concentrated layer of ozone gas that absorbs most of the suns harmful ultraviolet radiation, protecting living things on Earths surface.',
   [('What does the ozone layer primarily absorb?', ['Most of the suns harmful ultraviolet radiation', 'Most of the visible light reaching Earth', 'A concept unrelated to earth science', 'All of the oxygen in the atmosphere'], 0),
    ('Where is the ozone layer located?', ['In the upper atmosphere', 'Deep underground, below Earths crust', 'A concept unrelated to the ozone layer', 'At the very center of the planet'], 0),
    ('Why is the ozone layer important for living things on Earths surface?', ['It helps protect organisms from excessive ultraviolet radiation exposure', 'It has no measurable effect on living things at all', 'A concept unrelated to science', 'It provides all of the oxygen that living things breathe'], 0),
    ('What human-made chemicals were found to damage the ozone layer?', ['Chlorofluorocarbons, commonly known as CFCs', 'Pure oxygen released from plants', 'A concept unrelated to the ozone layer', 'Water vapour released from oceans'], 0),
    ('Why was international cooperation important in addressing damage to the ozone layer?', ['Reducing ozone-depleting chemicals worldwide required countries to act together', 'A single country acting alone could have solved the problem instantly', 'This concept has no relevance to science', 'International cooperation had no effect on ozone layer damage'], 0)]),
SS('Social Studies: Aboriginal Veterans and Their Wartime Contributions',
   'Grade 7 Social Studies strand: thousands of First Nations, Metis, and Inuit soldiers served in the Canadian military during the First and Second World Wars, making significant contributions despite facing discrimination and, in many cases, unequal treatment after returning home.',
   [('Approximately how many Indigenous soldiers served in the Canadian military during the World Wars?', ['Thousands', 'Fewer than ten', 'A concept unrelated to Canadian history', 'None served in either World War'], 0),
    ('What challenge did many Indigenous veterans face after returning home from war?', ['Unequal treatment and continued discrimination', 'Immediate and complete equality with all other veterans', 'A concept unrelated to Indigenous veterans', 'Guaranteed leadership positions in the federal government'], 0),
    ('Why is the service of Indigenous soldiers in the World Wars considered especially significant?', ['They served in large numbers despite facing discrimination and unequal rights at home', 'They were required by law to serve, unlike every other Canadian', 'A concept unrelated to social studies', 'Indigenous soldiers refused to participate in either World War'], 0),
    ('What is one way Canada has worked to recognize the contributions of Indigenous veterans?', ['Building memorials and holding ceremonies honouring their service', 'Ignoring their contributions completely in official records', 'A concept unrelated to Indigenous veterans', 'Removing all mention of their service from history'], 0),
    ('Why might learning about Indigenous veterans be an important part of understanding Canadian military history?', ['It highlights contributions and sacrifices that were historically overlooked in mainstream accounts', 'Indigenous veterans have no connection to Canadian military history', 'This concept has no relevance to social studies', 'Their service was always fully recognized with no historical oversight'], 0)]),
]),
day(146, [
L('Grammar: Conjunctive Adverbs and Transitional Phrases',
  'Grade 7 Language strand: a conjunctive adverb, such as however, therefore, or moreover, connects two independent clauses and is typically preceded by a semicolon and followed by a comma, showing a logical relationship between ideas.',
  [('What is a conjunctive adverb?', ['A word that connects two independent clauses and shows a logical relationship between them', 'A word that can never connect two clauses', 'A concept unrelated to grammar', 'A word used only at the very start of a story'], 0),
   ('Which of these words is a conjunctive adverb?', ['However', 'Quickly', 'Blue', 'Running'], 0),
   ('What punctuation typically comes before a conjunctive adverb joining two independent clauses?', ['A semicolon', 'A question mark', 'A concept unrelated to punctuation', 'An exclamation mark'], 0),
   ('What punctuation typically follows a conjunctive adverb joining two independent clauses?', ['A comma', 'A semicolon', 'A concept unrelated to conjunctive adverbs', 'A colon'], 0),
   ('Which sentence correctly uses a conjunctive adverb?', ['I studied all week; therefore, I felt ready for the test.', 'I studied all week therefore I felt ready for the test comma.', 'Therefore I studied; all week I felt ready for the test.', 'I studied, therefore; all week I felt ready for the test.'], 0)]),
M('Algebra: Rearranging Formulas and Solving for a Variable',
  'Grade 7 Math strand: rearranging a formula means isolating a different variable using inverse operations, such as rewriting the formula for the area of a rectangle to solve for its width instead of its area.',
  [('What does it mean to rearrange a formula?', ['To isolate a different variable using inverse operations', 'To remove every variable from the formula completely', 'A concept unrelated to algebra', 'To make the formula impossible to solve'], 0),
   ('If A = l times w, how could the formula be rearranged to solve for w?', ['w = A divided by l', 'w = A times l', 'A concept unrelated to rearranging formulas', 'w = A plus l'], 0),
   ('Why might someone need to rearrange a formula rather than use it in its original form?', ['A different variable may need to be calculated depending on the information available', 'Formulas can never be rearranged under any circumstances', 'A concept unrelated to algebra', 'The original form of a formula is always the only usable version'], 0),
   ('Using the formula d = rt, how would you rearrange it to solve for r?', ['r = d divided by t', 'r = d times t', 'A concept unrelated to formulas', 'r = d plus t'], 0),
   ('Why is understanding inverse operations important when rearranging formulas?', ['Reversing each operation correctly is what isolates the desired variable', 'Inverse operations have no role in rearranging formulas', 'This concept has no relevance to algebra', 'Rearranging a formula never requires reversing any operations'], 0)]),
Sc('Acid Rain: Causes and Environmental Effects',
   'Grade 7 Science strand: acid rain forms when pollutants such as sulfur dioxide and nitrogen oxides react with water vapour in the atmosphere, creating precipitation that can harm forests, acidify lakes, and damage buildings and monuments.',
   [('What causes acid rain to form?', ['Pollutants like sulfur dioxide and nitrogen oxides reacting with water vapour in the atmosphere', 'Pure rainwater falling with absolutely no chemical reaction involved', 'A concept unrelated to science', 'A sudden drop in atmospheric temperature alone'], 0),
    ('Which human activity is a major source of the pollutants that cause acid rain?', ['Burning fossil fuels', 'Watering a garden with a hose', 'A concept unrelated to acid rain', 'Recycling paper and cardboard'], 0),
    ('How can acid rain affect lakes and the organisms living in them?', ['It can lower the pH of the water, harming fish and other aquatic life', 'It always raises the pH of lake water to a safer level', 'A concept unrelated to acid rain', 'Acid rain has no effect on lakes or aquatic organisms'], 0),
    ('How can acid rain affect forests?', ['It can damage leaves and reduce nutrients available in the soil', 'It always makes soil more nutrient-rich for every tree', 'A concept unrelated to acid rain', 'Acid rain has no effect on forest ecosystems'], 0),
    ('Why might acid rain damage buildings and monuments made of stone?', ['The acidity can gradually dissolve certain minerals in the stone', 'Acid rain always strengthens the minerals found in stone', 'This concept has no relevance to science', 'Stone buildings are never affected by any form of precipitation'], 0)]),
SS('Social Studies: The Halibut Treaty of 1923 and Canadian Diplomatic Independence',
   'Grade 7 Social Studies strand: the Halibut Treaty of 1923, an agreement between Canada and the United States about Pacific fishing rights, marked the first time Canada negotiated and signed an international treaty independently of Britain, an early step toward full diplomatic autonomy.',
   [('What was the Halibut Treaty of 1923 primarily about?', ['Regulating Pacific halibut fishing rights between Canada and the United States', 'Establishing a new border between Canada and Alaska', 'A concept unrelated to Canadian history', 'Ending a military conflict between Canada and the United States'], 0),
    ('Why is the Halibut Treaty considered a significant milestone in Canadian history?', ['Canada signed it independently, without a British signature, for the first time', 'It was signed entirely by British officials with no Canadian involvement', 'A concept unrelated to the Halibut Treaty', 'It had no lasting significance for Canadian diplomacy'], 0),
    ('Which two countries were involved in the Halibut Treaty of 1923?', ['Canada and the United States', 'Canada and France', 'Canada and Japan', 'Canada and Australia'], 0),
    ('How did the Halibut Treaty relate to Canadas path toward full independence in foreign affairs?', ['It was an early step showing Canada could conduct its own international diplomacy', 'It proved that Canada could never negotiate treaties on its own', 'A concept unrelated to Canadian independence', 'It ended all of Canadas ability to sign future treaties'], 0),
    ('What later document formally confirmed Canadas legislative independence from Britain?', ['The Statute of Westminster', 'The Halibut Treaty of 1923', 'A concept unrelated to Canadian independence', 'The Treaty of Versailles'], 0)]),
]),
day(147, [
L('Vocabulary: Slang and Changing Language Over Time',
  'Grade 7 Language strand: slang is informal vocabulary that develops within a group or generation, often changing quickly and reflecting current culture, which is why it can make older writing or speech feel dated over time.',
  [('What is slang?', ['Informal vocabulary that develops within a group or generation', 'Formal vocabulary used exclusively in academic writing', 'A concept unrelated to vocabulary', 'A word that never changes meaning over time'], 0),
   ('Why does slang often change quickly compared to standard vocabulary?', ['It closely reflects current culture and trends, which shift over time', 'Slang words are legally required to stay the same forever', 'A concept unrelated to slang', 'Standard vocabulary changes far more quickly than slang does'], 0),
   ('Why might slang from decades ago sound unfamiliar or dated today?', ['Language and cultural references naturally shift from one generation to the next', 'Slang from the past always sounds identical to slang used today', 'A concept unrelated to vocabulary', 'Older slang is always identical to formal, standard vocabulary'], 0),
   ('Why might a writer avoid heavy slang in a formal essay?', ['Formal writing generally calls for standard vocabulary that a wide audience will understand', 'Formal essays are required to use as much slang as possible', 'This concept has no connection to vocabulary', 'Slang always makes formal writing clearer for every reader'], 0),
   ('Why might slang still be valuable in casual conversation or informal writing?', ['It can create a sense of familiarity and shared identity among a group', 'Slang has no value in casual conversation of any kind', 'This concept has no relevance to vocabulary', 'Casual conversation always requires strictly formal vocabulary'], 0)]),
M('Geometry: The Golden Ratio in Art and Nature',
  'Grade 7 Math strand: the golden ratio is a special number, approximately 1.618, that appears when a line is divided so the ratio of the whole to the larger part equals the ratio of the larger part to the smaller part, and it appears throughout art, architecture, and natural patterns.',
  [('What is the approximate value of the golden ratio?', ['1.618', '3.14', '2.718', '0.5'], 0),
   ('How is the golden ratio defined in terms of a divided line segment?', ['The ratio of the whole to the larger part equals the ratio of the larger part to the smaller part', 'The whole is always exactly twice as long as the larger part', 'A concept unrelated to the golden ratio', 'The smaller part is always equal to the larger part'], 0),
   ('Where might the golden ratio be observed in nature?', ['In the spiral patterns of some shells and flower seed heads', 'In the exact colour of every leaf on a tree', 'A concept unrelated to geometry', 'In the temperature of ocean water at different depths'], 0),
   ('Why have artists and architects historically used the golden ratio in their work?', ['Many people find proportions based on the golden ratio visually pleasing', 'The golden ratio has never influenced any artistic or architectural work', 'A concept unrelated to art and architecture', 'The golden ratio always makes a design appear unbalanced'], 0),
   ('Why is the golden ratio considered an irrational number?', ['It cannot be written exactly as a simple fraction and its decimal digits never repeat', 'It can always be written as a simple, exact fraction', 'This concept has no relevance to geometry', 'Irrational numbers and the golden ratio have no connection to each other'], 0)]),
Sc('Biomimicry: Engineering Inspired by Nature',
   'Grade 7 Science strand: biomimicry is the practice of designing technology and materials by studying and imitating strategies found in nature, such as modeling an aircraft wing after a birds wing or an adhesive after a geckos foot.',
   [('What is biomimicry?', ['Designing technology by studying and imitating strategies found in nature', 'A process that has no connection to engineering or design', 'A concept unrelated to science', 'A method that avoids studying nature entirely'], 0),
    ('Which of these is an example of biomimicry?', ['Designing an adhesive inspired by the structure of a geckos foot', 'Building a bridge using only randomly selected materials', 'A concept unrelated to biomimicry', 'Designing a building with no reference to nature of any kind'], 0),
    ('Why might engineers look to nature for design solutions?', ['Living organisms have evolved efficient solutions to many physical challenges over millions of years', 'Nature never provides any useful design solutions', 'A concept unrelated to biomimicry', 'Engineers are required by law to avoid studying nature'], 0),
    ('What natural feature inspired the design of some high-speed train fronts?', ['The narrow beak shape of a kingfisher', 'The wide, flat shape of a leaf', 'A concept unrelated to biomimicry', 'The round shape of a pebble'], 0),
    ('Why is biomimicry often considered a sustainable approach to design?', ['It draws on solutions already proven efficient by natural selection rather than starting from scratch', 'Biomimicry always requires more raw materials than traditional design methods', 'This concept has no relevance to science', 'Sustainable design has no connection to studying nature'], 0)]),
SS('Social Studies: The Asbestos Strike of 1949 and the Labour Movement in Quebec',
   'Grade 7 Social Studies strand: the Asbestos Strike of 1949 was a lengthy and often tense labour dispute involving asbestos miners in Quebec demanding better wages and safer working conditions, and it is remembered as a turning point that helped energize the broader Quebec labour movement.',
   [('What industry were the workers involved in the Asbestos Strike of 1949 employed in?', ['Asbestos mining', 'Shipbuilding', 'A concept unrelated to Canadian history', 'Commercial fishing'], 0),
    ('What were striking workers in the Asbestos Strike primarily demanding?', ['Better wages and safer working conditions', 'A complete end to all mining in the province', 'A concept unrelated to the Asbestos Strike', 'The relocation of the mine to another province'], 0),
    ('In what year did the Asbestos Strike take place?', ['1949', '1919', '1867', '1985'], 0),
    ('In which province did the Asbestos Strike of 1949 take place?', ['Quebec', 'Ontario', 'Manitoba', 'Nova Scotia'], 0),
    ('Why is the Asbestos Strike considered an important moment in Quebec labour history?', ['It helped energize and unify the broader labour movement in the province', 'It had no lasting impact on the labour movement in Quebec', 'This concept has no relevance to social studies', 'It permanently ended all labour organizing efforts in the province'], 0)]),
]),
day(148, [
L('Reading: Analyzing Cliffhangers and Suspense Techniques',
  'Grade 7 Language strand: a cliffhanger ends a scene or chapter at a moment of high tension without resolving it, and writers build suspense using techniques like withholding information, foreshadowing danger, and controlling the pace of revealed details.',
  [('What is a cliffhanger?', ['An unresolved moment of high tension left at the end of a scene or chapter', 'A scene that always ties up every loose end completely', 'A concept unrelated to reading', 'A chapter with no conflict or tension of any kind'], 0),
   ('Why might an author end a chapter with a cliffhanger?', ['To encourage readers to keep reading to find out what happens next', 'Cliffhangers always cause readers to stop reading immediately', 'A concept unrelated to cliffhangers', 'Ending on a cliffhanger has no effect on a reader at all'], 0),
   ('Which technique might a writer use to build suspense?', ['Withholding key information from the reader until later', 'Revealing every detail of the plot at the very beginning', 'A concept unrelated to suspense', 'Avoiding any conflict throughout the entire story'], 0),
   ('How does foreshadowing contribute to suspense in a story?', ['It hints at future danger or conflict, creating anticipation in the reader', 'Foreshadowing always removes any sense of anticipation from a story', 'This concept has no connection to reading', 'Foreshadowing can only be used at the very end of a story'], 0),
   ('Which ending best demonstrates a cliffhanger?', ['Just as she reached for the door, the lights went out and a voice whispered her name.', 'She reached the door, opened it, and the story ended peacefully.', 'The chemical symbol for gold is Au.', 'Add 15 and 20 to get 35.'], 0)]),
M('Probability: Analyzing Fair and Unfair Games',
  'Grade 7 Math strand: a game is considered fair when every player has an equal probability of winning based on the rules, while an unfair game gives one player or outcome a greater probability of success than the others.',
  [('What makes a game mathematically fair?', ['Every player has an equal probability of winning', 'One player always has a guaranteed advantage', 'A concept unrelated to probability', 'The rules of the game are kept secret from all players'], 0),
   ('What makes a game mathematically unfair?', ['One player or outcome has a greater probability of winning than the others', 'Every player has exactly the same probability of winning', 'A concept unrelated to fair and unfair games', 'The game has no rules of any kind'], 0),
   ('If a die is rolled and a player wins only by rolling a 6, while another wins on rolling 1 through 5, is this game fair?', ['No, because the probabilities of winning are not equal', 'Yes, because both players have exactly the same chance of winning', 'A concept unrelated to probability', 'It is impossible to determine whether the game is fair'], 0),
   ('How could you test whether a coin used in a game is fair?', ['Flip it many times and check whether heads and tails occur roughly equally', 'Flip the coin exactly once and assume the result applies forever', 'A concept unrelated to fair and unfair games', 'Fairness can never be tested using repeated trials'], 0),
   ('Why is understanding probability important when designing a fair game?', ['It ensures the calculated chances of winning are equal for all players involved', 'Probability has no role in designing a fair or unfair game', 'This concept has no relevance to math', 'Fair games can be designed without any consideration of probability'], 0)]),
Sc('Wildfire Ecology and Forest Regeneration',
   'Grade 7 Science strand: wildfires can destroy vegetation and habitat in the short term, but many forest ecosystems have adapted to periodic fire, with some plant species relying on fire to release seeds or clear space for new growth during forest regeneration.',
   [('What is one short-term effect of a wildfire on a forest ecosystem?', ['Destruction of vegetation and habitat', 'An immediate and permanent increase in biodiversity with no other effects', 'A concept unrelated to science', 'A wildfire always leaves an ecosystem completely unaffected'], 0),
    ('Why have some forest ecosystems adapted to periodic wildfires over time?', ['Fire has historically been a natural and recurring part of many forest ecosystems', 'Wildfires have never occurred naturally in any forest ecosystem', 'A concept unrelated to wildfire ecology', 'Forest ecosystems can never adapt to any environmental disturbance'], 0),
    ('What is one way some plant species have adapted to rely on fire?', ['Certain cones only release their seeds when exposed to the heat of a fire', 'Certain plants immediately die the instant any fire occurs nearby', 'A concept unrelated to wildfire ecology', 'No plant species have ever adapted to rely on fire'], 0),
    ('How can wildfire help clear space for new forest growth?', ['It removes dead material and overcrowded vegetation, allowing sunlight to reach the forest floor', 'It always blocks sunlight from reaching the forest floor permanently', 'This concept has no connection to science', 'Wildfire has no effect on the amount of vegetation in a forest'], 0),
    ('Why might suppressing every wildfire for many decades sometimes lead to larger, more destructive fires later?', ['Unburned dead material can build up over time, creating more fuel for a future fire', 'Suppressing wildfires always eliminates the possibility of any future fire', 'This concept has no relevance to science', 'Dead material never accumulates in a forest ecosystem over time'], 0)]),
SS('Social Studies: The Rideau Canal and Early Canadian Infrastructure',
   'Grade 7 Social Studies strand: the Rideau Canal, built in the 1820s and 1830s under Lieutenant Colonel John By, connected Ottawa to Kingston and was originally constructed as a secure military supply route in case of conflict with the United States.',
   [('What two cities does the Rideau Canal connect?', ['Ottawa and Kingston', 'Toronto and Montreal', 'A concept unrelated to Canadian history', 'Halifax and Quebec City'], 0),
    ('Why was the Rideau Canal originally built?', ['To serve as a secure military supply route in case of conflict with the United States', 'To provide a route exclusively for tourist boat tours', 'A concept unrelated to the Rideau Canal', 'To transport goods exclusively between Canada and Britain'], 0),
    ('Who oversaw the construction of the Rideau Canal?', ['Lieutenant Colonel John By', 'Sir John A. Macdonald', 'Lester B. Pearson', 'Louis Riel'], 0),
    ('During which decades was the Rideau Canal built?', ['The 1820s and 1830s', 'The 1760s and 1770s', 'The 1900s and 1910s', 'The 1950s and 1960s'], 0),
    ('How is the Rideau Canal used today, beyond its original military purpose?', ['As a recreational waterway for boating and, in winter, skating', 'It is no longer used for any purpose at all', 'A concept unrelated to the Rideau Canal', 'Exclusively as a route for commercial cargo ships'], 0)]),
]),
day(149, [
L('Writing: Writing a Blog Post',
  'Grade 7 Language strand: a blog post typically opens with a hook to draw readers in, organizes ideas with headings or short paragraphs for easy scanning, and often closes by inviting readers to comment or share their own thoughts.',
  [('Why might a blog post open with a hook?', ['To draw readers in right away and encourage them to keep reading', 'A hook always discourages readers from continuing', 'A concept unrelated to writing', 'Blog posts are required to begin with a table of contents'], 0),
   ('Why might a blog post use headings or short paragraphs?', ['To make the content easier to scan and read online', 'Headings always make a blog post more difficult to read', 'A concept unrelated to blog posts', 'Short paragraphs are never used in online writing'], 0),
   ('What might a blog post include at the end to engage its audience?', ['An invitation for readers to comment or share their thoughts', 'A demand that readers stop reading immediately', 'A concept unrelated to writing', 'A blog post can never include any kind of conclusion'], 0),
   ('How does a blog post often differ in tone from a formal academic essay?', ['A blog post often uses a more conversational, personal tone', 'A blog post is always required to use extremely formal academic language', 'This concept has no connection to writing', 'Blog posts and academic essays always sound exactly the same'], 0),
   ('Which opening sounds most like the start of a blog post?', ['Ever wondered why some mornings feel impossible to get through? Here is what finally worked for me.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Financial Literacy: Comparing Subscription and Phone Plans',
  'Grade 7 Math strand: comparing subscription or phone plans often involves setting up linear cost equations with a fixed monthly fee plus a per-use charge, then finding the point where two plans cost the same to decide which option is more economical.',
  [('What two components are commonly combined in a phone or subscription plan cost equation?', ['A fixed monthly fee plus a per-use or per-unit charge', 'Two identical fixed fees with no per-use charge at all', 'A concept unrelated to financial literacy', 'A single one-time payment with no monthly component'], 0),
   ('If Plan A costs 20 dollars per month with no extra charges and Plan B costs 10 dollars per month plus 2 dollars per gigabyte used, at how many gigabytes do the two plans cost the same?', ['5 gigabytes', '10 gigabytes', '2 gigabytes', '20 gigabytes'], 0),
   ('Why is it useful to graph two plans on the same axes when comparing costs?', ['The point where the lines intersect shows when the two plans cost the same', 'Graphing two plans together never reveals any useful information', 'A concept unrelated to financial literacy', 'The lines representing two different plans can never intersect'], 0),
   ('If a customer expects to use very little data each month, which type of plan is likely more economical?', ['A plan with a lower fixed fee and a higher per-unit charge', 'A plan with the highest possible fixed fee available', 'A concept unrelated to comparing plans', 'The cost of a plan is never affected by how much data is used'], 0),
   ('Why might a linear equation be a useful model for a subscription plans monthly cost?', ['The cost increases at a constant rate for each additional unit used, matching a linear relationship', 'Subscription costs never increase at a constant, predictable rate', 'This concept has no relevance to math', 'Linear equations can never be used to model any real-world cost'], 0)]),
Sc('The Human Microbiome and Gut Bacteria',
   'Grade 7 Science strand: the human microbiome is the vast community of bacteria and other microorganisms living in and on the body, especially in the digestive system, where many species assist with digestion, produce vitamins, and support the immune system.',
   [('What is the human microbiome?', ['The community of bacteria and other microorganisms living in and on the human body', 'A single organ found only in the digestive system', 'A concept unrelated to biology', 'A type of medication used to treat infections'], 0),
    ('Where in the body is a large portion of the microbiome found?', ['The digestive system', 'The outer surface of the fingernails only', 'A concept unrelated to the human microbiome', 'The human body contains no microorganisms of any kind'], 0),
    ('What is one way gut bacteria can benefit the human body?', ['Assisting with digestion and producing certain vitamins', 'Gut bacteria provide no benefit to the human body whatsoever', 'A concept unrelated to the microbiome', 'Gut bacteria exist only to cause illness'], 0),
    ('How might gut bacteria interact with the immune system?', ['They can help support and regulate immune system function', 'Gut bacteria have no connection to the immune system at all', 'A concept unrelated to biology', 'Gut bacteria always weaken the immune system completely'], 0),
    ('Why might taking antibiotics sometimes disrupt a persons gut microbiome?', ['Antibiotics can kill beneficial bacteria along with harmful ones', 'Antibiotics only ever affect bacteria found outside the human body', 'This concept has no relevance to science', 'Antibiotics have no effect on any bacteria in the digestive system'], 0)]),
SS('Social Studies: The Just Society and Pierre Trudeaus Vision for Canada',
   'Grade 7 Social Studies strand: the Just Society was a political vision promoted by Prime Minister Pierre Trudeau beginning in the late 1960s, emphasizing individual rights, bilingualism, and social equality, and it helped shape policies including the eventual Canadian Charter of Rights and Freedoms.',
   [('Who promoted the vision of the Just Society?', ['Prime Minister Pierre Trudeau', 'Sir John A. Macdonald', 'Lester B. Pearson', 'Stephen Harper'], 0),
    ('What values did the Just Society emphasize?', ['Individual rights, bilingualism, and social equality', 'Strict isolation from all other countries', 'A concept unrelated to the Just Society', 'The elimination of all federal social programs'], 0),
    ('In approximately which decade did Pierre Trudeau introduce the idea of the Just Society?', ['The late 1960s', 'The 1930s', 'The 1900s', 'The 1980s'], 0),
    ('Which major document is often connected to the broader rights-based vision behind the Just Society?', ['The Canadian Charter of Rights and Freedoms', 'The Statute of Westminster', 'A concept unrelated to the Just Society', 'The Halibut Treaty of 1923'], 0),
    ('Why is the Just Society considered an influential political vision in Canadian history?', ['It shaped policy debates around rights and equality for years afterward', 'It had no lasting influence on any later policy debates', 'This concept has no relevance to social studies', 'It was immediately forgotten and never discussed again'], 0)]),
]),
day(150, [
L('Language Review: Modal Verbs, Slang, Frame Narratives, and Blog Writing',
  'Grade 7 Language strand review: students revisit modal verbs, jargon, frame narratives, cliffhangers and suspense, and writing a blog post.',
  [('What do modal verbs generally express?', ['Degrees of possibility, permission, ability, or obligation', 'The exact spelling of a word', 'A concept unrelated to grammar', 'The number of syllables in a sentence'], 0),
   ('What is jargon?', ['Specialized vocabulary used within a particular profession or field', 'A word that has exactly the same meaning in every possible context', 'A concept unrelated to vocabulary', 'A type of punctuation used only in technical writing'], 0),
   ('What is a frame narrative?', ['A story that contains another story told within it', 'A story that never contains any other story', 'A concept unrelated to reading', 'A story with no characters of any kind'], 0),
   ('What is a cliffhanger?', ['An unresolved moment of high tension left at the end of a scene or chapter', 'A scene that always ties up every loose end completely', 'A concept unrelated to reading', 'A chapter with no conflict or tension of any kind'], 0),
   ('Why might a blog post open with a hook?', ['To draw readers in right away and encourage them to keep reading', 'A hook always discourages readers from continuing', 'A concept unrelated to writing', 'Blog posts are required to begin with a table of contents'], 0)]),
M('Math Review: Linear Equations, Circles, Investing, and Data Spread',
  'Grade 7 Math strand review: students revisit slope-intercept form, inscribed and circumscribed circles, basic investing, standard deviation, and calculating density.',
  [('In the equation y = mx + b, what does m represent?', ['The slope of the line', 'The y-intercept of the line', 'A concept unrelated to linear equations', 'The x-intercept of the line'], 0),
   ('What does it mean for a circle to be inscribed in a polygon?', ['The circle fits inside the polygon and touches each side exactly once', 'The circle passes through every vertex of the polygon', 'A concept unrelated to geometry', 'The circle has no connection to the polygon at all'], 0),
   ('What does owning a share of stock represent?', ['Partial ownership in a company', 'A guaranteed loan made to a company', 'A concept unrelated to financial literacy', 'A fixed amount of cash with no connection to a company'], 0),
   ('What does standard deviation measure?', ['How spread out data values are around the mean', 'The single largest value in a data set', 'A concept unrelated to data management', 'The exact number of values collected in a survey'], 0),
   ('What formula is used to calculate density?', ['Mass divided by volume', 'Volume divided by mass', 'A concept unrelated to measurement', 'Mass multiplied by volume'], 0)]),
Sc('Science Review: Extremophiles, Gene Editing, Space, and Environmental Chemistry',
   'Grade 7 Science strand review: students revisit extremophiles, CRISPR gene editing, exoplanets, endothermic and exothermic reactions, and the ozone layer.',
   [('What is an extremophile?', ['An organism that thrives in extremely harsh environmental conditions', 'An organism that can only survive in mild, comfortable conditions', 'A concept unrelated to biology', 'A type of rock formed under extreme pressure'], 0),
    ('What does CRISPR allow scientists to do?', ['Precisely cut and modify specific sections of DNA', 'Observe distant galaxies in high resolution', 'A concept unrelated to science', 'Measure the exact age of a fossil instantly'], 0),
    ('What is an exoplanet?', ['A planet that orbits a star outside our solar system', 'A moon that orbits a planet within our solar system', 'A concept unrelated to astronomy', 'A star located at the center of our solar system'], 0),
    ('What happens during an exothermic reaction?', ['Energy is released into the surroundings', 'Energy is absorbed from the surroundings', 'A concept unrelated to chemistry', 'No energy change occurs of any kind'], 0),
    ('What does the ozone layer primarily absorb?', ['Most of the suns harmful ultraviolet radiation', 'Most of the visible light reaching Earth', 'A concept unrelated to earth science', 'All of the oxygen in the atmosphere'], 0)]),
SS('Social Studies Review: Responsible Government, Confederation Debates, and Diplomacy',
   'Grade 7 Social Studies strand review: students revisit the Durham Report, the Great Coalition and Charlottetown Conference, the Boer War, the North-West Rebellion, and the Halibut Treaty of 1923.',
   [('What did the Durham Report recommend regarding Upper and Lower Canada?', ['Uniting them into a single colony', 'Dividing them into four separate colonies', 'A concept unrelated to the Durham Report', 'Ending all government in both colonies entirely'], 0),
    ('What was the Great Coalition of 1864?', ['An alliance of political rivals in the Province of Canada formed to pursue federal union', 'A treaty signed between Canada and France', 'A concept unrelated to Canadian history', 'A military alliance formed to fight a foreign war'], 0),
    ('Why did Canada send troops to the Boer War?', ['To support Britain as a member of the British Empire', 'To support an entirely unrelated country with no historical ties to Canada', 'A concept unrelated to the Boer War', 'Canada was legally required to send troops with no choice involved'], 0),
    ('Who led the North-West Rebellion of 1885?', ['Louis Riel', 'Sir John A. Macdonald', 'Lester B. Pearson', 'Pierre Trudeau'], 0),
    ('Why is the Halibut Treaty considered a significant milestone in Canadian history?', ['Canada signed it independently, without a British signature, for the first time', 'It was signed entirely by British officials with no Canadian involvement', 'A concept unrelated to the Halibut Treaty', 'It had no lasting significance for Canadian diplomacy'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_141_150)
    append_to(7, g7_141_150)
