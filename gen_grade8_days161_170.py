#!/usr/bin/env python3
"""Grade 8, Days 161-170 -- extends Grade 8 from 160 to 170 days. Topics
chosen after dumping the existing Day 1-160 title list (data/grade8.json)
in full to avoid any overlap: direct and indirect speech, compound words
and their formation, diction and word choice in literature, the cause
and effect essay, evaluating online reviews and influencer marketing,
the imperative mood, anagrams and wordplay, personification and
anthropomorphism, and the personal response to literature; the Law of
Large Numbers, twin primes and the distribution of primes, projective
geometry, the Rational Root Theorem, the Monty Hall Problem, the Mean
Value Theorem, Goldbachs Conjecture, expected value, and outliers and
their effect on data; chromatography, the Doppler effect, weathering and
the formation of caves, fermentation, the Big Bang Theory, how
touchscreens work, the chemistry of photography and film development,
center of mass and balance, and bioaccumulation and biomagnification;
the creation of the Canada Pension Plan, Tommy Douglas and the
introduction of medicare in Saskatchewan, the North American Free Trade
Agreement of 1994, the 1972 Canada-Soviet Summit Series, the Berger
Inquiry and the Mackenzie Valley Pipeline, the Marshall Decision and
Indigenous fishing rights, Africville and the displacement of a Black
Nova Scotian community, the creation of Via Rail, and Canadas Centennial
Year and Expo 67. None of these topics duplicate any Day 1-160 subject
or title. Day 170 is a cross-subject review day drawing on Days
161-169; each review title includes the Days 161-169 range so it is
textually distinct from every earlier review days title.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used
anywhere in title/question/summary/option text; apostrophes are dropped
entirely, matching the convention used in gen_grade8_days151_160.py.
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


g8_161_170 = [
day(161, [
L('Grammar: Direct and Indirect Speech',
  'Grade 8 Language strand: direct speech quotes a speakers exact words within quotation marks, while indirect speech, or reported speech, restates what someone said without quotation marks, often shifting pronouns and verb tense.',
  [('What does direct speech do?', ['Quotes a speakers exact words within quotation marks', 'Removes all punctuation from a sentence', 'Always uses the future tense', 'Combines two unrelated sentences'], 0),
   ('What does indirect speech do?', ['Restates what someone said without using quotation marks', 'Quotes a speaker word for word inside quotation marks', 'Removes the speaker from the sentence entirely', 'Uses only questions to report speech'], 0),
   ('Which sentence is an example of indirect speech?', ['She said that she was tired.', 'She said, I am tired.', 'Tired, she said, I am.', 'I am tired, she asked.'], 0),
   ('What often shifts when direct speech is converted to indirect speech?', ['Pronouns and verb tense', 'The alphabet used to write the sentence', 'The subject of the sentence into a verb', 'Nothing ever changes in the conversion'], 0),
   ('Why is understanding the difference between direct and indirect speech useful in writing?', ['It helps a writer report dialogue and statements accurately in narrative and nonfiction writing', 'It has no effect on how dialogue is written', 'Indirect speech is never used in any type of writing', 'Direct speech and indirect speech always mean exactly the same thing'], 0)]),
M('Statistics: An Introduction to the Law of Large Numbers',
  'Grade 8 Math strand: the Law of Large Numbers states that as a random experiment, such as a coin flip, is repeated more and more times, the average of the results tends to get closer to the expected theoretical probability.',
  [('What does the Law of Large Numbers describe?', ['How the average of repeated random trials tends toward the expected probability', 'A rule for rounding decimals to the nearest whole number', 'A method for factoring polynomials', 'How to calculate the area of a triangle'], 0),
   ('What happens as a random experiment is repeated more and more times?', ['The observed average result gets closer to the theoretical expected value', 'The observed average result becomes more random and unpredictable', 'The theoretical expected value keeps changing with every trial', 'Nothing happens no matter how many times the experiment repeats'], 0),
   ('Which is an example the Law of Large Numbers could describe?', ['Flipping a coin thousands of times and seeing the proportion of heads approach one half', 'Flipping a coin exactly one time', 'Measuring the length of a single pencil', 'Counting the number of days in a single week'], 0),
   ('Does the Law of Large Numbers guarantee an exact outcome on any single trial?', ['No, it describes a long-run average, not a single result', 'Yes, it guarantees the exact result of every single trial', 'It only applies to trials that never repeat', 'It guarantees that every trial produces an identical outcome'], 0),
   ('Why is the Law of Large Numbers important in fields such as insurance and gambling?', ['It allows long-run averages to be predicted reliably even though individual outcomes are uncertain', 'It has no practical use in either insurance or gambling', 'It guarantees that a gambler will always win in the long run', 'It proves that probability calculations are never useful'], 0)]),
Sc('Chemistry: Chromatography and Separating Mixtures',
   'Grade 8 Science strand: chromatography separates the components of a mixture, such as ink, based on how differently each component travels through a material like paper, allowing scientists to identify individual substances within a mixture.',
   [('What does chromatography do?', ['Separates the components of a mixture based on how they travel through a material', 'Combines several pure substances into a single mixture', 'Measures the temperature of a chemical reaction', 'Changes a mixture into a single element'], 0),
    ('Which everyday substance is commonly used to demonstrate chromatography in a classroom?', ['Ink', 'Salt', 'Sand', 'Iron filings'], 0),
    ('Why do different components of a mixture separate during chromatography?', ['They travel at different rates through the material used', 'They all travel at exactly the same rate', 'They react chemically with each other during the process', 'They evaporate completely and leave nothing behind'], 0),
    ('What can chromatography help scientists do?', ['Identify individual substances within a mixture', 'Create brand new elements', 'Destroy a mixture completely', 'Measure the exact mass of a single atom'], 0),
    ('Why is chromatography considered a useful technique in forensic science?', ['It can help identify unknown substances found at a scene by comparing how they separate', 'It has no practical applications outside a classroom', 'It can only be used to identify pure elements, never mixtures', 'It always destroys the evidence being analyzed'], 0)]),
H('The Creation of the Canada Pension Plan in 1965',
  'Grade 8 History strand: established in 1965, the Canada Pension Plan created a contributory, government-administered pension program funded by workers and employers, providing retirement, disability, and survivor benefits to eligible Canadians.',
  [('In what year was the Canada Pension Plan established?', ['1965', '1867', '1927', '1949'], 0),
   ('How is the Canada Pension Plan funded?', ['Through contributions from workers and employers', 'Through a one-time payment from the federal government only', 'Through donations from foreign governments', 'Through a tax on imported goods only'], 0),
   ('What type of pension program is the Canada Pension Plan?', ['A contributory, government-administered pension program', 'A private program run entirely by individual banks', 'A program available only to government employees', 'A program that requires no financial contribution at all'], 0),
   ('Besides retirement, what other kinds of benefits does the Canada Pension Plan provide?', ['Disability and survivor benefits', 'Free university tuition for all Canadians', 'Unlimited travel benefits', 'Free housing for every contributor'], 0),
   ('Why was the creation of the Canada Pension Plan considered an important step in Canadian social policy?', ['It gave working Canadians a structured way to build retirement income across their careers', 'It eliminated all other forms of retirement savings in Canada', 'It had no lasting effect on Canadian social policy', 'It only applied to a small number of provinces'], 0)]),
]),
day(162, [
L('Vocabulary: Compound Words and Their Formation',
  'Grade 8 Language strand: a compound word forms when two or more smaller words combine to create a new word with its own meaning, and compounds can be written as one word, as two separate words, or joined by a hyphen.',
  [('What is a compound word?', ['A word formed by combining two or more smaller words', 'A word borrowed directly from another language with no change', 'A word with no defined meaning at all', 'A single letter used to represent a whole word'], 0),
   ('Which is an example of a closed compound word, written as one word?', ['Sunflower', 'Ice cream', 'Well known', 'Post office'], 0),
   ('Which is an example of an open compound word, written as two separate words?', ['Ice cream', 'Sunflower', 'Football', 'Toothbrush'], 0),
   ('Which is an example of a hyphenated compound word?', ['Well-known', 'Sunflower', 'Ice cream', 'Football'], 0),
   ('Why might the meaning of a compound word differ from the meanings of its individual parts?', ['The combined word can take on a new, specific meaning distinct from either part alone', 'A compound word always means the exact same thing as each smaller word', 'Compound words never have any meaning at all', 'The individual parts of a compound word are always identical in meaning'], 0)]),
M('Number Theory: Twin Primes and the Distribution of Prime Numbers',
  'Grade 8 Math strand: twin primes are pairs of prime numbers that differ by exactly two, such as 11 and 13, and mathematicians continue to study how prime numbers are distributed among the whole numbers.',
  [('What are twin primes?', ['Pairs of prime numbers that differ by exactly two', 'Pairs of prime numbers that are always identical', 'Any two even numbers next to each other', 'Pairs of numbers that add up to exactly ten'], 0),
   ('Which of these is a pair of twin primes?', ['17 and 19', '14 and 16', '15 and 17', '20 and 22'], 0),
   ('What do mathematicians study when examining the distribution of primes?', ['How prime numbers are spaced out among the whole numbers', 'How to convert primes into decimals', 'The colour associated with each prime number', 'How to remove all primes from a number line'], 0),
   ('Is the number of twin prime pairs known to be finite or infinite?', ['It is unknown, since the Twin Prime Conjecture remains unproven', 'It is proven to be exactly one hundred', 'It is proven to be finite with no exceptions', 'It is proven to be infinite with a formal proof'], 0),
   ('Why do prime numbers become less frequent as numbers get larger?', ['Larger numbers have more possible factors, making primes rarer', 'Larger numbers always have fewer possible factors', 'Prime numbers stop existing after a certain point', 'Prime numbers become more common as numbers increase'], 0)]),
Sc('Physics: An Introduction to the Doppler Effect',
   'Grade 8 Science strand: the Doppler effect describes the change in pitch of a sound as its source moves toward or away from a listener, caused by sound waves being compressed or stretched by the motion of the source.',
   [('What does the Doppler effect describe?', ['The change in pitch of a sound as its source moves toward or away from a listener', 'The change in colour of a light source at rest', 'The loss of all sound as an object moves', 'The change in the mass of a moving object'], 0),
    ('What happens to sound waves as a source moves toward a listener?', ['The waves become compressed, raising the pitch', 'The waves become stretched, lowering the pitch', 'The waves disappear completely', 'The waves remain exactly the same'], 0),
    ('What happens to sound waves as a source moves away from a listener?', ['The waves become stretched, lowering the pitch', 'The waves become compressed, raising the pitch', 'The waves travel backward in time', 'The waves instantly stop moving'], 0),
    ('Which everyday example demonstrates the Doppler effect?', ['The changing pitch of a siren as an ambulance passes by', 'The colour of a stationary traffic light', 'The smell of fresh bread in a bakery', 'The taste of a sour lemon'], 0),
    ('Why is the Doppler effect useful in fields such as weather forecasting?', ['It allows radar to measure the motion of precipitation within a storm', 'It has no practical use in weather forecasting', 'It can only measure the temperature of the air', 'It prevents radar from detecting any kind of motion'], 0)]),
H('Tommy Douglas and the Introduction of Medicare in Saskatchewan',
  'Grade 8 History strand: as premier of Saskatchewan, Tommy Douglas introduced a provincial universal hospital and medical insurance program in 1962, a model that later expanded nationally and earned him recognition as a founder of Canadian medicare.',
  [('What position did Tommy Douglas hold when he introduced medicare in Saskatchewan?', ['Premier of Saskatchewan', 'Prime Minister of Canada', 'Mayor of Regina', 'Leader of the federal opposition'], 0),
   ('In what year did Saskatchewan introduce its medical insurance program under Tommy Douglas?', ['1962', '1867', '1921', '1949'], 0),
   ('What kind of program did Tommy Douglas introduce in Saskatchewan?', ['A universal hospital and medical insurance program', 'A program that only covered dental care', 'A program available only to government workers', 'A program that eliminated all hospitals in the province'], 0),
   ('What happened to the Saskatchewan medicare model in the years that followed?', ['It later expanded to become a model adopted across Canada', 'It was cancelled within a single year and never used again', 'It remained available only in Saskatchewan with no wider influence', 'It was replaced immediately by a private insurance system'], 0),
   ('Why is Tommy Douglas often remembered as a founder of Canadian medicare?', ['His provincial program became the basis for Canadas national healthcare system', 'He opposed all forms of public healthcare throughout his career', 'His program had no influence on healthcare outside Saskatchewan', 'He is remembered for reasons unrelated to healthcare policy'], 0)]),
]),
day(163, [
L('Reading: Analyzing Diction and Word Choice in Literature',
  'Grade 8 Language strand: diction refers to an authors deliberate choice of words, and analyzing diction, including whether words are formal or informal, concrete or abstract, helps readers understand tone, mood, and characterization.',
  [('What does diction refer to?', ['An authors deliberate choice of words', 'The physical layout of a page', 'The number of chapters in a book', 'The font used to print a text'], 0),
   ('What can analyzing an authors diction help a reader understand?', ['Tone, mood, and characterization', 'The exact number of pages in a book', 'The publication date of a text', 'The price of a book'], 0),
   ('Which is an example of formal diction?', ['Utilize instead of use', 'Gonna instead of going to', 'Yeah instead of yes', 'Kinda instead of kind of'], 0),
   ('Why might an author use concrete, sensory diction rather than abstract language?', ['To create a vivid, specific image for readers', 'To make a passage as vague as possible', 'To remove all imagery from a text', 'To confuse the reader intentionally'], 0),
   ('Why is diction considered a powerful literary tool?', ['Small differences in word choice can significantly change how a reader interprets a text', 'Word choice has no effect on how a text is interpreted', 'Diction only matters in poetry, never in prose', 'Every word in a language carries the exact same tone'], 0)]),
M('Geometry: An Introduction to Projective Geometry',
  'Grade 8 Math strand: projective geometry studies properties of shapes that stay the same under projection, such as how parallel lines appear to meet at a vanishing point in perspective drawing, differing from the parallel-line rules of Euclidean geometry.',
  [('What does projective geometry study?', ['Properties of shapes that stay the same under projection', 'Only the exact area of a circle', 'The weight of a three-dimensional solid', 'The colour of a geometric figure'], 0),
   ('In perspective drawing, where do parallel lines appear to meet?', ['At a vanishing point', 'At the center of the page only', 'They never appear to meet under any circumstance', 'At every point along the line'], 0),
   ('How does projective geometry differ from Euclidean geometry regarding parallel lines?', ['In projective geometry, parallel lines can appear to meet, unlike in Euclidean geometry', 'Projective geometry has no concept of parallel lines at all', 'Euclidean geometry allows parallel lines to meet, unlike projective geometry', 'The two systems treat parallel lines in exactly the same way'], 0),
   ('Which real-world application relies on ideas from projective geometry?', ['Artists use it to create realistic perspective drawings', 'Chefs use it to measure ingredients', 'Musicians use it to tune instruments', 'Athletes use it to time a race'], 0),
   ('Why is projective geometry useful beyond art and drawing?', ['It provides tools used in computer graphics and camera image processing', 'It has no practical applications outside of art', 'It can only be used to draw perfect circles', 'It prevents any image from ever being rendered digitally'], 0)]),
Sc('Earth Science: Weathering and the Formation of Caves',
   'Grade 8 Science strand: weathering breaks down rock over time through physical and chemical processes, and when slightly acidic water slowly dissolves soluble rock such as limestone, it can carve out extensive underground cave systems.',
   [('What does weathering do to rock over time?', ['Breaks it down through physical and chemical processes', 'Instantly turns rock into water', 'Has no effect on rock of any kind', 'Makes rock permanently indestructible'], 0),
    ('What type of rock is commonly dissolved to form limestone caves?', ['Limestone', 'Granite', 'Obsidian', 'Basalt'], 0),
    ('What property of water helps it dissolve limestone over time?', ['Slight acidity', 'Extremely high salt content', 'Its solid, frozen state', 'Its complete lack of any minerals'], 0),
    ('Which is an example of physical weathering?', ['Ice repeatedly freezing and expanding within cracks in rock', 'A chemical reaction that changes a rocks composition', 'A rock being formed deep underground', 'A rock cooling slowly from molten lava'], 0),
    ('Why do cave systems typically take an extremely long time to form?', ['Chemical weathering by water dissolves rock only very gradually', 'Caves form instantly the moment water touches rock', 'Weathering has no connection to how caves are formed', 'Limestone dissolves faster than any other type of rock'], 0)]),
H('The North American Free Trade Agreement of 1994',
  'Grade 8 History strand: the North American Free Trade Agreement, which took effect in 1994, reduced trade barriers between Canada, the United States, and Mexico, building on the earlier Canada-United States Free Trade Agreement to expand continental trade.',
  [('In what year did the North American Free Trade Agreement take effect?', ['1994', '1867', '1988', '1949'], 0),
   ('Which three countries were part of the North American Free Trade Agreement?', ['Canada, the United States, and Mexico', 'Canada, Britain, and France', 'Canada, Mexico, and Brazil', 'The United States, Mexico, and Cuba'], 0),
   ('What did the North American Free Trade Agreement aim to reduce between its member countries?', ['Trade barriers', 'The size of each countrys population', 'The number of provinces in Canada', 'The number of official languages spoken'], 0),
   ('Which earlier agreement did the North American Free Trade Agreement build upon?', ['The Canada-United States Free Trade Agreement', 'The Statute of Westminster', 'The British North America Act', 'The Treaty of Versailles'], 0),
   ('Why was the addition of Mexico to this trade agreement significant for Canada?', ['It expanded Canadian trade opportunities across the entire North American continent', 'It ended all trade between Canada and the United States', 'It had no effect on Canadian trade of any kind', 'It reduced Canadas trade opportunities significantly'], 0)]),
]),
day(164, [
L('Writing: The Cause and Effect Essay',
  'Grade 8 Language strand: a cause and effect essay explains why an event or situation occurred and examines the consequences that followed, organized either by explaining multiple causes of one effect or multiple effects of one cause.',
  [('What does a cause and effect essay explain?', ['Why an event occurred and the consequences that followed', 'A random list of unrelated facts', 'Only the setting of a story', 'A single characters physical appearance'], 0),
   ('Which organizational pattern might a cause and effect essay use?', ['Multiple causes leading to one effect, or one cause leading to multiple effects', 'A list of characters with no explanation', 'An essay with no organizational structure at all', 'A single sentence with no supporting detail'], 0),
   ('What transitional words often signal cause and effect relationships?', ['Words such as because, therefore, and as a result', 'Words such as meanwhile and elsewhere only', 'Words that never appear in this type of essay', 'Only numbers and dates'], 0),
   ('Why is evidence important when explaining causes in this type of essay?', ['It supports the claim that one event genuinely led to another rather than merely following it', 'Evidence is never needed in a cause and effect essay', 'Evidence only matters in a persuasive essay, never in this type', 'Causes never need to be supported by any evidence'], 0),
   ('Why is a cause and effect essay a useful way to analyze historical or scientific events?', ['It helps readers understand the reasoning behind why something happened and what resulted from it', 'It has no use in analyzing historical or scientific events', 'It only describes events without explaining any reasoning', 'It focuses exclusively on describing a setting'], 0)]),
M('Algebra: An Introduction to the Rational Root Theorem',
  'Grade 8 Math strand: the Rational Root Theorem provides a method for listing possible rational roots of a polynomial equation by comparing the factors of its constant term with the factors of its leading coefficient.',
  [('What does the Rational Root Theorem help find?', ['A list of possible rational roots of a polynomial equation', 'The exact area of a triangle', 'A rule for rounding decimals', 'The colour of a graphed function'], 0),
   ('What two parts of a polynomial does the Rational Root Theorem compare?', ['The factors of the constant term and the factors of the leading coefficient', 'The number of terms and the number of variables', 'The degree of the polynomial and its graph colour', 'The exponents and the number of pages in a textbook'], 0),
   ('Does the Rational Root Theorem guarantee that every listed possibility is an actual root?', ['No, it only narrows down candidates that must then be tested', 'Yes, every listed possibility is always an actual root', 'It guarantees the polynomial has no roots at all', 'It only applies to polynomials with exactly one term'], 0),
   ('Why is the Rational Root Theorem a useful starting point for factoring a polynomial?', ['It reduces the number of values that need to be tested as possible roots', 'It eliminates the need to ever factor a polynomial', 'It always finds every root instantly with no testing required', 'It only works for polynomials with no constant term'], 0),
   ('Why might a polynomial have no rational roots at all?', ['Its roots may be irrational or complex numbers instead', 'Every polynomial always has at least one rational root', 'Polynomials with no constant term cannot exist', 'Rational roots are required for a polynomial to be valid'], 0)]),
Sc('Biology: The Process of Fermentation',
   'Grade 8 Science strand: fermentation is a process by which microorganisms such as yeast or bacteria break down sugars without oxygen, producing byproducts such as alcohol or carbon dioxide, and it is used to make foods such as bread, yogurt, and cheese.',
   [('What is fermentation?', ['A process by which microorganisms break down sugars without oxygen', 'A process that requires large amounts of oxygen', 'A process that only occurs in plants', 'A process that destroys all sugar molecules instantly'], 0),
    ('Which organism commonly carries out fermentation in bread making?', ['Yeast', 'Algae', 'Moss', 'Coral'], 0),
    ('What gas produced during fermentation causes bread dough to rise?', ['Carbon dioxide', 'Oxygen', 'Nitrogen', 'Hydrogen'], 0),
    ('Which of these foods is commonly produced using fermentation?', ['Yogurt', 'Raw carrots', 'Fresh lettuce', 'Plain rice'], 0),
    ('Why is fermentation considered an anaerobic process?', ['It occurs in the absence of oxygen', 'It requires a constant, large supply of oxygen', 'It only occurs at extremely high temperatures', 'It cannot occur in any living organism'], 0)]),
H('The 1972 Canada-Soviet Summit Series and Cold War Culture',
  'Grade 8 History strand: the 1972 Summit Series pitted Canadian and Soviet professional hockey players against each other for the first time, becoming a symbol of Cold War rivalry and a defining moment in Canadian national identity.',
  [('In what year did the Canada-Soviet Summit Series take place?', ['1972', '1867', '1949', '1988'], 0),
   ('What sport was featured in the Summit Series?', ['Hockey', 'Basketball', 'Soccer', 'Baseball'], 0),
   ('Which two countries competed against each other in the Summit Series?', ['Canada and the Soviet Union', 'Canada and the United States', 'Canada and Sweden', 'Canada and Britain'], 0),
   ('Why did the Summit Series become a symbol of Cold War rivalry?', ['It represented a direct competition between a Western and a Soviet nation during a tense global era', 'It had no connection to international politics of any kind', 'It was played entirely for charity with no competitive element', 'It took place decades before the Cold War began'], 0),
   ('Why is the Summit Series still remembered as an important moment in Canadian history?', ['It became a defining and unifying moment in Canadian national identity and pride', 'It had no lasting impact on how Canadians viewed themselves', 'It was quickly forgotten within a few weeks of ending', 'It only mattered to hockey players, not to the wider public'], 0)]),
]),
day(165, [
L('Media Literacy: Evaluating Online Reviews and Influencer Marketing',
  'Grade 8 Language strand: online reviews and influencer endorsements can shape consumer opinions, but paid partnerships, fake reviews, and undisclosed sponsorships make it important for media consumers to evaluate the credibility of online recommendations.',
  [('What can shape consumer opinions online?', ['Online reviews and influencer endorsements', 'Only the price listed on a product', 'Only the colour of a products packaging', 'Only the length of a product description'], 0),
   ('What is one reason online reviews might not be fully trustworthy?', ['Some reviews may be fake or written by paid reviewers', 'All online reviews are always written by the manufacturer', 'Reviews can never be written by real customers', 'Every review website independently verifies each review'], 0),
   ('What should an influencer disclose when promoting a product they were paid to endorse?', ['That the content is a paid partnership or sponsorship', 'Their personal home address', 'The exact cost of producing the video', 'Nothing needs to be disclosed under any circumstance'], 0),
   ('Why should media consumers evaluate online recommendations critically?', ['Undisclosed sponsorships can create a biased or misleading impression of a product', 'Every online recommendation is always completely unbiased', 'Critical evaluation of online content serves no useful purpose', 'Online recommendations never influence purchasing decisions'], 0),
   ('Which is a sign that an online review might not be genuine?', ['Overly generic praise with no specific details about the product', 'A review that mentions specific strengths and weaknesses', 'A review written by a verified purchaser', 'A review that includes a photo of the product in use'], 0)]),
M('Probability: An Introduction to the Monty Hall Problem',
  'Grade 8 Math strand: the Monty Hall Problem is a probability puzzle based on a game show scenario in which switching a chosen door after one losing door is revealed actually increases the probability of winning, a result that often surprises people at first.',
  [('What is the Monty Hall Problem based on?', ['A game show scenario involving choosing between doors', 'A card game played with a standard deck', 'A dice game played by two players', 'A puzzle involving coin flips only'], 0),
   ('In the Monty Hall Problem, what happens after a contestant picks a door?', ['The host reveals a losing door among the remaining choices', 'The game ends immediately with no further action', 'All the doors are opened at the same time', 'The contestant is given a completely new set of doors'], 0),
   ('According to the Monty Hall Problem, what strategy increases the probability of winning?', ['Switching to the other unopened door', 'Always keeping the original door chosen', 'Choosing a door at random every single time', 'Refusing to choose any door at all'], 0),
   ('Why does the Monty Hall result often surprise people at first?', ['It seems like switching should not matter, but a careful probability calculation shows it does', 'The math behind it has never been verified by anyone', 'Switching doors is mathematically proven to make no difference', 'The problem has no clear mathematical answer at all'], 0),
   ('Why is the Monty Hall Problem a popular example in the study of probability?', ['It shows how intuition can mislead us about conditional probability', 'It proves that probability calculations are always intuitive', 'It has no connection to the study of probability', 'It shows that switching a choice never changes any outcome'], 0)]),
Sc('Space Science: The Big Bang Theory and the Origin of the Universe',
   'Grade 8 Science strand: the Big Bang Theory proposes that the universe began as an extremely hot, dense point approximately 13.8 billion years ago and has been expanding and cooling ever since, a model supported by evidence such as the cosmic microwave background.',
   [('What does the Big Bang Theory propose about the origin of the universe?', ['It began as an extremely hot, dense point that has been expanding ever since', 'It has always existed in its current form with no beginning', 'It began as a single planet that later became the whole universe', 'It formed instantly in its final shape with no expansion at all'], 0),
    ('Approximately how long ago does the Big Bang Theory suggest the universe began?', ['About 13.8 billion years ago', 'About 100 years ago', 'About 6,000 years ago', 'About 1 million years ago'], 0),
    ('What has the universe been doing since the Big Bang, according to the theory?', ['Expanding and cooling', 'Shrinking and heating up', 'Remaining exactly the same size', 'Reversing back toward its starting point'], 0),
    ('What evidence supports the Big Bang Theory?', ['The cosmic microwave background radiation', 'The presence of oceans on Earth', 'The existence of the Moon', 'The colour of the daytime sky'], 0),
    ('Why do scientists consider the expansion of the universe strong evidence for the Big Bang?', ['Distant galaxies are observed moving away from each other, consistent with an expanding universe', 'Galaxies have never been observed moving in any direction', 'The universe has been proven to be shrinking, not expanding', 'Galaxy motion has no connection to theories about the universes origin'], 0)]),
H('The Berger Inquiry and the Mackenzie Valley Pipeline',
  'Grade 8 History strand: led by Justice Thomas Berger in the mid-1970s, the Berger Inquiry examined the proposed Mackenzie Valley Pipeline and recommended a delay in construction to address the environmental and Indigenous land claim concerns it raised.',
  [('Who led the inquiry into the proposed Mackenzie Valley Pipeline?', ['Justice Thomas Berger', 'Prime Minister Pierre Trudeau', 'Premier Tommy Douglas', 'Justice Thomas Rowell'], 0),
   ('In what decade did the Berger Inquiry take place?', ['The 1970s', 'The 1920s', 'The 1950s', 'The 1990s'], 0),
   ('What project did the Berger Inquiry examine?', ['The proposed Mackenzie Valley Pipeline', 'The construction of the Trans-Canada Highway', 'The building of the Canadian Pacific Railway', 'The creation of the St. Lawrence Seaway'], 0),
   ('What did the Berger Inquiry ultimately recommend?', ['A delay in pipeline construction to address environmental and land claim concerns', 'Immediate construction with no further review', 'Cancelling all future pipeline projects in Canada permanently', 'Transferring the project entirely to a foreign company'], 0),
   ('Why is the Berger Inquiry considered an important moment for Indigenous rights in Canada?', ['It gave Indigenous communities in the region a formal opportunity to raise concerns about development on their land', 'It excluded Indigenous communities from any discussion of the project', 'It had no connection to Indigenous rights or land use', 'It resulted in the immediate approval of the pipeline with no consultation'], 0)]),
]),
day(166, [
L('Grammar: The Imperative Mood and Command Sentences',
  'Grade 8 Language strand: the imperative mood is used to give commands, make requests, or offer instructions, typically omitting the subject you, which is understood rather than stated.',
  [('What is the imperative mood used for?', ['Giving commands, making requests, or offering instructions', 'Describing a series of past events only', 'Asking a question about the future', 'Expressing uncertainty about a fact'], 0),
   ('Which sentence is written in the imperative mood?', ['Close the door.', 'She closed the door.', 'Did she close the door?', 'The door was closed by her.'], 0),
   ('What subject is typically omitted in an imperative sentence?', ['You, since it is understood rather than stated', 'I, since it is always stated directly', 'They, since it never appears in any sentence', 'It, since imperative sentences never have a subject of any kind'], 0),
   ('In which type of writing might the imperative mood commonly appear?', ['A recipe or a set of instructions', 'A private diary entry describing feelings', 'A poem with no clear audience', 'A weather report describing yesterdays temperature'], 0),
   ('Why is the imperative mood considered direct compared to other moods?', ['It addresses the reader or listener directly without extra explanation', 'It always requires a long, detailed explanation before the command', 'It can never address a reader or listener directly', 'It is used only to describe events that already happened'], 0)]),
M('Number Theory: An Introduction to Goldbachs Conjecture',
  'Grade 8 Math strand: Goldbachs Conjecture proposes that every even whole number greater than two can be written as the sum of two prime numbers, a statement that has been tested extensively but never formally proven.',
  [('What does Goldbachs Conjecture propose?', ['Every even whole number greater than two can be written as the sum of two primes', 'Every odd whole number can be written as the sum of two primes', 'No even number can ever be written as the sum of two primes', 'Every whole number is itself a prime number'], 0),
   ('Which pair of primes could represent the number 10 under Goldbachs Conjecture?', ['3 and 7', '4 and 6', '1 and 9', '2 and 9'], 0),
   ('Has Goldbachs Conjecture ever been formally proven?', ['No, it remains unproven despite extensive testing', 'Yes, it was proven centuries ago with a complete formal proof', 'Yes, it was disproven and shown to be false', 'It was proven true only for the number ten'], 0),
   ('Why is Goldbachs Conjecture still considered a conjecture rather than a theorem?', ['A conjecture requires a general proof, and only a proof, not examples alone, can confirm it for all cases', 'Conjectures and theorems always mean exactly the same thing', 'It has already been formally proven and renamed a theorem', 'Testing a single example is enough to make something a theorem'], 0),
   ('Why do mathematicians continue to find Goldbachs Conjecture interesting?', ['It is simple to state, yet has resisted proof for centuries', 'It was proven within a single day of being proposed', 'It has no real mathematical significance at all', 'It only applies to numbers smaller than ten'], 0)]),
Sc('Technology: How Touchscreens Work',
   'Grade 8 Science strand: most modern touchscreens use a grid of electrical sensors beneath the glass that detect the change in an electrical field caused by the conductive touch of a human finger, allowing the device to calculate the exact location of a touch.',
   [('What do most modern touchscreens use to detect a touch?', ['A grid of electrical sensors beneath the glass', 'A tiny camera hidden inside the screen', 'A magnet attached to the back of the device', 'A speaker that listens for sound waves'], 0),
    ('Why can a human finger activate a touchscreen?', ['The body is conductive and changes the screens electrical field when it touches the glass', 'The body produces a magnetic field strong enough to move the screen', 'The body emits light that the screen can detect', 'The body is completely non-conductive, which activates the screen'], 0),
    ('What does a touchscreen calculate when it detects a change in its electrical field?', ['The exact location of the touch', 'The temperature of the room', 'The weight of the device', 'The brightness of the surrounding light'], 0),
    ('Why might a touchscreen fail to respond to a touch from a gloved hand?', ['Most gloves are not conductive, so they do not change the screens electrical field', 'Gloves always make a touchscreen more responsive', 'Touchscreens cannot detect any object heavier than a finger', 'Gloves permanently damage the screens electrical sensors'], 0),
    ('Why are capacitive touchscreens widely used in smartphones and tablets?', ['They allow precise, responsive detection of a fingers location without moving parts', 'They require far more electricity than any other type of screen', 'They can only detect touches from a stylus, never a finger', 'They have no practical advantage over older screen designs'], 0)]),
H('The Marshall Decision and Indigenous Fishing Rights',
  'Grade 8 History strand: in 1999, the Supreme Court of Canada ruling in the Marshall case affirmed treaty rights allowing Mikmaq and Maliseet peoples to fish and hunt for a moderate livelihood, reshaping the management of fisheries in Atlantic Canada.',
  [('In what year did the Supreme Court of Canada issue the Marshall decision?', ['1999', '1867', '1949', '1970'], 0),
   ('Which court issued the Marshall decision?', ['The Supreme Court of Canada', 'The Supreme Court of the United States', 'The International Court of Justice', 'A provincial small claims court'], 0),
   ('What treaty right did the Marshall decision affirm?', ['The right of Mikmaq and Maliseet peoples to fish and hunt for a moderate livelihood', 'The right of a single private company to control all fisheries', 'The right of the federal government to ban all fishing permanently', 'The right of foreign nations to fish freely in Canadian waters'], 0),
   ('What region of Canada was most directly affected by the Marshall decision?', ['Atlantic Canada', 'Northern Ontario', 'The Prairie provinces', 'British Columbia'], 0),
   ('Why is the Marshall decision considered a significant moment in Indigenous rights history?', ['It confirmed that historic treaty rights continue to have legal force in the present day', 'It eliminated all treaty rights previously held by Indigenous peoples', 'It had no effect on how fisheries were managed', 'It applied only to non-Indigenous fishers'], 0)]),
]),
day(167, [
L('Vocabulary: Anagrams and Wordplay',
  'Grade 8 Language strand: an anagram rearranges the letters of a word or phrase to form a new word or phrase, and exploring anagrams and other forms of wordplay helps students develop flexible thinking about spelling and vocabulary.',
  [('What does an anagram do?', ['Rearranges the letters of a word or phrase to form a new word or phrase', 'Translates a word into another language', 'Removes all vowels from a word', 'Combines two unrelated words into a sentence'], 0),
   ('Which of these is an anagram of the word LISTEN?', ['SILENT', 'LESSON', 'SILVER', 'LISTED'], 0),
   ('What skill does solving anagrams help develop?', ['Flexible thinking about spelling and letter patterns', 'Skill at solving long division problems', 'The ability to memorize historical dates', 'The ability to identify musical notes'], 0),
   ('Why must an anagram use the exact same letters as the original word?', ['Because an anagram is a rearrangement, not a substitution, of letters', 'Anagrams are allowed to add extra letters freely', 'Anagrams only need to share a single letter with the original word', 'Anagrams have no connection to the letters in the original word'], 0),
   ('Why might writers use wordplay such as anagrams in puzzles or riddles?', ['To create an engaging challenge that rewards close attention to language', 'To make a puzzle impossible for anyone to solve', 'Wordplay is never used in puzzles or riddles', 'To remove all meaning from the words being used'], 0)]),
M('Probability: An Introduction to Expected Value',
  'Grade 8 Math strand: expected value calculates the long-run average outcome of a probability experiment by multiplying each possible outcome by its probability and summing the results, providing a way to compare the fairness of games or decisions.',
  [('What does expected value calculate?', ['The long-run average outcome of a probability experiment', 'The single most likely outcome of one trial', 'The largest possible outcome in a set of data', 'The exact outcome of the very next trial'], 0),
   ('How is expected value calculated?', ['By multiplying each outcome by its probability and summing the results', 'By adding together every possible outcome with no other calculation', 'By choosing the outcome that occurs most often in a small sample', 'By dividing the largest outcome by the smallest outcome'], 0),
   ('What can expected value help compare?', ['The fairness of different games or decisions', 'The exact colour of two different objects', 'The alphabetical order of a list of outcomes', 'The physical size of two unrelated shapes'], 0),
   ('If a game has a negative expected value, what does that suggest about playing it repeatedly?', ['A player would tend to lose money on average over many plays', 'A player is guaranteed to win every single time', 'The game has no relationship to money at all', 'A player would break even on every single play'], 0),
   ('Why is expected value considered a long-run measure rather than a prediction of any single outcome?', ['A single trial can differ greatly from the average, which only emerges over many repetitions', 'Expected value always predicts the exact result of the very next trial', 'Expected value has no connection to repeated trials of an experiment', 'A single trial always matches the expected value exactly'], 0)]),
Sc('Chemistry: The Chemistry of Photography and Film Development',
   'Grade 8 Science strand: traditional film photography relies on a chemical reaction in which light-sensitive silver compounds on film darken when exposed to light, and a developing solution then converts the exposed compounds into a visible image.',
   [('What makes traditional photographic film sensitive to light?', ['Light-sensitive silver compounds on the film', 'A layer of plain water on the film', 'A magnetic coating on the film', 'A layer of sugar crystals on the film'], 0),
    ('What happens to the silver compounds on film when they are exposed to light?', ['They begin a chemical change that will darken when developed', 'They instantly evaporate and disappear from the film', 'They turn completely transparent with no change at all', 'They freeze solid regardless of the temperature'], 0),
    ('What does a developing solution do to exposed film?', ['Converts the exposed silver compounds into a visible image', 'Erases the image completely from the film', 'Adds colour to a film that has no chemical exposure', 'Prevents any chemical reaction from ever occurring'], 0),
    ('Why must traditional film be handled in darkness before it is developed?', ['Any additional light exposure would alter the chemical reaction and ruin the image', 'Darkness has no effect on undeveloped film', 'Light exposure always improves the quality of the final image', 'Film only reacts to light after it has already been developed'], 0),
    ('Why is film photography considered a chemical process rather than a purely digital one?', ['The image forms through a genuine chemical reaction on the film rather than through electronic sensors', 'Film cameras use exactly the same technology as digital cameras', 'No chemical reaction of any kind occurs during film photography', 'Digital cameras also rely on light-sensitive silver compounds'], 0)]),
H('Africville and the Displacement of a Black Nova Scotian Community',
  'Grade 8 History strand: Africville was a Black community in Halifax, Nova Scotia, whose residents were relocated and whose homes were demolished by the city between the 1960s and early 1970s, an event now recognized as a significant injustice in Canadian history.',
  [('In what city was the community of Africville located?', ['Halifax, Nova Scotia', 'Toronto, Ontario', 'Winnipeg, Manitoba', 'Montreal, Quebec'], 0),
   ('What happened to the residents of Africville between the 1960s and early 1970s?', ['They were relocated and their homes were demolished by the city', 'They were granted expanded property rights over the land', 'The community was left completely undisturbed', 'The city built new schools and hospitals for the community'], 0),
   ('What kind of community was Africville?', ['A Black community', 'A community made up entirely of recent immigrants', 'A community built exclusively for government workers', 'A community with no permanent residents'], 0),
   ('How is the demolition of Africville generally viewed today?', ['As a significant injustice in Canadian history', 'As an example of successful, fair urban planning', 'As an event with no lasting historical significance', 'As a decision that was celebrated by the community at the time'], 0),
   ('Why is the story of Africville an important part of Black Canadian history?', ['It highlights the impact of discriminatory decisions on an established Black community', 'It has no connection to the history of Black Canadians', 'It shows a community that always received fair and equal treatment', 'It describes events that took place outside of Canada'], 0)]),
]),
day(168, [
L('Reading: Analyzing Personification and Anthropomorphism',
  'Grade 8 Language strand: personification gives human qualities to a nonhuman object or idea in a brief, figurative way, while anthropomorphism more fully portrays a nonhuman character, such as an animal, as having human behaviour throughout a story.',
  [('What does personification do?', ['Gives human qualities to a nonhuman object or idea', 'Removes all descriptive language from a sentence', 'Compares two unlike things using like or as', 'Repeats the same consonant sound across nearby words'], 0),
   ('Which sentence is an example of personification?', ['The wind whispered through the trees.', 'The wind was as loud as a train.', 'The wind blew at twenty kilometres per hour.', 'The wind is a type of weather.'], 0),
   ('How does anthropomorphism differ from personification?', ['Anthropomorphism more fully portrays a nonhuman character with human behaviour throughout a story', 'Anthropomorphism only occurs in a single brief phrase', 'Personification and anthropomorphism mean exactly the same thing', 'Anthropomorphism never involves any human qualities at all'], 0),
   ('Which is an example of anthropomorphism?', ['A talking animal character who behaves like a human throughout a novel', 'A single sentence describing the weather', 'A factual description of an animals diet', 'A list of scientific facts about a species'], 0),
   ('Why might an author use personification in a poem?', ['To create a vivid, imaginative image or evoke an emotional response', 'To remove all imagery from the poem', 'To make the poem as literal and factual as possible', 'Personification is never used in poetry'], 0)]),
M('Statistics: An Introduction to the Mean Value Theorem',
  'Grade 8 Math strand: the Mean Value Theorem states that for a smooth, continuous curve between two points, there is at least one point where the instantaneous rate of change equals the average rate of change over the whole interval.',
  [('What does the Mean Value Theorem guarantee for a smooth, continuous curve between two points?', ['At least one point where the instantaneous rate of change equals the average rate of change', 'That the curve must be a perfectly straight line', 'That no rate of change can ever be calculated', 'That the curve has no defined endpoints'], 0),
   ('What does the average rate of change over an interval represent on a graph?', ['The slope of the line connecting the two endpoints', 'The highest point on the entire graph', 'The exact width of the interval only', 'The colour used to draw the curve'], 0),
   ('What does the instantaneous rate of change at a point represent?', ['The slope of the tangent line at that exact point', 'The total area beneath the entire curve', 'The distance between two unrelated points', 'The average of every point on the graph'], 0),
   ('Why must a curve be smooth and continuous for the Mean Value Theorem to apply?', ['Breaks or sharp corners in the curve could prevent a matching tangent slope from existing', 'Smoothness has no effect on whether the theorem applies', 'The theorem only applies to curves with sharp corners', 'Continuous curves can never have a defined slope'], 0),
   ('Why is the Mean Value Theorem considered an important result in calculus?', ['It connects the idea of average change to instantaneous change in a precise way', 'It has no practical use within the study of calculus', 'It proves that average and instantaneous rates are always unrelated', 'It only applies to numbers smaller than ten'], 0)]),
Sc('Physics: Center of Mass and Balance',
   'Grade 8 Science strand: the center of mass is the point where an objects mass is evenly balanced in every direction, and an object remains stable as long as a vertical line from its center of mass falls within its base of support.',
   [('What is the center of mass of an object?', ['The point where its mass is evenly balanced in every direction', 'The heaviest single part of an object', 'The exact geometric center of an objects surface only', 'A point that only exists in perfectly round objects'], 0),
    ('What determines whether an object remains stable and does not tip over?', ['Whether a vertical line from its center of mass falls within its base of support', 'The colour of the object', 'The temperature of the surrounding air', 'The exact material the object is made from'], 0),
    ('Why do objects with a wide base tend to be more stable?', ['A wider base makes it more likely the center of mass stays above the base of support', 'A wide base always raises an objects center of mass', 'A wide base has no effect on an objects stability', 'A wide base makes an object heavier than a narrow one'], 0),
    ('What happens to an objects stability if its center of mass is raised too high?', ['The object becomes more likely to tip over', 'The object becomes impossible to move', 'The object automatically becomes more stable', 'The objects mass decreases significantly'], 0),
    ('Why do tightrope walkers often carry a long balancing pole?', ['It helps lower and adjust their overall center of mass for better balance', 'It has no effect on their balance at all', 'It increases their height to see farther ahead', 'It is used only to measure the length of the rope'], 0)]),
H('The Creation of Via Rail and the Decline of Passenger Rail',
  'Grade 8 History strand: created in 1977 as a Crown corporation, Via Rail took over most intercity passenger rail service in Canada from private railways, a response to decades of declining ridership as cars and airplanes became more popular.',
  [('In what year was Via Rail created?', ['1977', '1867', '1949', '1921'], 0),
   ('What kind of organization is Via Rail?', ['A Crown corporation', 'A privately owned foreign company', 'A branch of a provincial ministry', 'A charitable, not-for-profit organization'], 0),
   ('What service did Via Rail take over from private railway companies?', ['Most intercity passenger rail service in Canada', 'All freight shipping across Canada', 'Airport security services', 'Municipal bus routes within cities'], 0),
   ('What contributed to the decline of passenger rail ridership before Via Rail was created?', ['The growing popularity of cars and airplanes for travel', 'A sudden ban on all forms of public transportation', 'A dramatic increase in the price of gasoline only', 'The complete disappearance of Canadian roads and highways'], 0),
   ('Why did the federal government decide to create a dedicated passenger rail corporation?', ['To preserve passenger train service that private railways were finding less profitable to operate', 'To eliminate passenger rail service entirely across Canada', 'To transfer all Canadian railways to foreign ownership', 'To replace all trains in Canada with airplanes'], 0)]),
]),
day(169, [
L('Writing: The Personal Response to Literature',
  'Grade 8 Language strand: a personal response to literature expresses a readers individual reaction to a text, connecting specific details from the text to the readers own thoughts, feelings, or experiences.',
  [('What does a personal response to literature express?', ['A readers individual reaction to a text', 'A publishers marketing summary of a book', 'A complete summary with no personal opinion', 'A list of every character mentioned in a text'], 0),
   ('What should a strong personal response connect to the readers own thoughts or experiences?', ['Specific details from the text', 'Unrelated details from a different book entirely', 'No details from the text at all', 'Only the books title and author'], 0),
   ('Why is it important to support a personal response with evidence from the text?', ['Evidence shows the response is grounded in the text rather than a vague general opinion', 'Evidence is never required in a personal response', 'A personal response should avoid mentioning the text entirely', 'Evidence only matters in a formal literary analysis, never here'], 0),
   ('How does a personal response differ from a formal literary analysis?', ['A personal response focuses on the readers reaction rather than an objective, structured argument', 'The two forms of writing are always identical', 'A formal literary analysis never uses evidence from the text', 'A personal response must always be written in the third person only'], 0),
   ('Why might teachers ask students to write a personal response to a novel?', ['To encourage reflective thinking and a genuine connection between the reader and the text', 'To test a students ability to memorize page numbers', 'Personal responses serve no educational purpose', 'To discourage students from forming their own opinions'], 0)]),
M('Statistics: An Introduction to Outliers and Their Effect on Data',
  'Grade 8 Math strand: an outlier is a data value that differs significantly from the rest of a data set, and because outliers can strongly influence measures such as the mean, statisticians examine them carefully before deciding whether to include or exclude them from an analysis.',
  [('What is an outlier?', ['A data value that differs significantly from the rest of a data set', 'The most common value in a data set', 'The exact middle value of a data set', 'A value that appears more than once in a data set'], 0),
   ('Which measure of central tendency is most affected by an outlier?', ['The mean', 'The mode only', 'The total number of data points', 'The range of the smallest values only'], 0),
   ('Why might a statistician investigate an outlier before removing it from a data set?', ['The value could be a data entry error or a genuine, meaningful result', 'Outliers should always be removed without any investigation', 'Outliers never affect the results of a statistical analysis', 'Every outlier is always caused by the exact same kind of error'], 0),
   ('How does the median typically respond to an outlier compared to the mean?', ['The median usually changes far less than the mean does', 'The median always changes more dramatically than the mean', 'The median and the mean always change by the exact same amount', 'The median cannot be calculated if an outlier is present'], 0),
   ('Why is it important to report whether outliers were removed from a data set?', ['Removing outliers can significantly change the conclusions drawn from the data', 'Removing outliers never has any effect on the conclusions drawn', 'Outliers are not relevant to any statistical report', 'Data sets are not permitted to contain outliers'], 0)]),
Sc('Biology: Bioaccumulation and Biomagnification in Food Chains',
   'Grade 8 Science strand: bioaccumulation occurs when an organism absorbs a toxin faster than it can eliminate it, and biomagnification describes how the concentration of that toxin increases at each higher level of a food chain, posing the greatest risk to top predators.',
   [('What is bioaccumulation?', ['When an organism absorbs a toxin faster than it can eliminate it', 'When an organism eliminates toxins faster than it absorbs them', 'When a toxin has no effect on any living organism', 'When an organism produces a toxin for the first time'], 0),
    ('What does biomagnification describe?', ['How the concentration of a toxin increases at each higher level of a food chain', 'How a toxin instantly disappears at each level of a food chain', 'How a food chain becomes larger with each new organism added', 'How predators avoid consuming any toxins at all'], 0),
    ('Which organisms in a food chain are typically at greatest risk from biomagnification?', ['Top predators', 'Producers such as plants', 'Organisms that are never eaten by anything', 'Decomposers only'], 0),
    ('Why does a toxin become more concentrated as it moves up a food chain?', ['Each predator consumes many organisms that have already accumulated the toxin', 'Toxins are destroyed completely at every level of a food chain', 'Predators are immune to all toxins found in their prey', 'Toxin concentration always decreases at higher levels of a food chain'], 0),
    ('Why are bioaccumulation and biomagnification important concepts in environmental science?', ['They help explain how pollution can seriously harm animals far from its original source', 'They have no connection to environmental pollution', 'They only apply to organisms living in a laboratory setting', 'They prove that pollution never affects living organisms'], 0)]),
H('Canadas Centennial Year and Expo 67',
  'Grade 8 History strand: 1967 marked the one-hundredth anniversary of Confederation, celebrated across the country and highlighted by Expo 67, a world exposition held in Montreal that drew millions of visitors and became a symbol of Canadian confidence and modernity.',
  [('What milestone did Canada celebrate in 1967?', ['The one-hundredth anniversary of Confederation', 'The fiftieth anniversary of Confederation', 'The end of the Second World War', 'The signing of the Treaty of Versailles'], 0),
   ('What major event was held in Montreal as part of the centennial celebrations?', ['Expo 67, a world exposition', 'The Winter Olympics', 'The Summit Series hockey tournament', 'The signing of the North American Free Trade Agreement'], 0),
   ('What did Expo 67 attract to Montreal?', ['Millions of visitors from around the world', 'Only a small number of local residents', 'No visitors at all due to construction delays', 'Only government officials from Canada'], 0),
   ('What did Expo 67 come to symbolize for many Canadians?', ['Canadian confidence and modernity', 'A period of economic decline', 'The end of Canadian independence', 'A rejection of international cooperation'], 0),
   ('Why is 1967 considered a significant year in Canadian history beyond the centennial celebrations itself?', ['It reflected growing national pride and Canadas emerging identity on the world stage', 'It marked the only year Canada ever hosted an international event', 'It had no lasting significance for Canadian identity', 'It marked the end of Canadas relationship with the Commonwealth'], 0)]),
]),
day(170, [
L('Language Review: Grammar, Vocabulary, and Descriptive Writing (Days 161-169)',
  'Grade 8 Language strand review: students revisit direct and indirect speech, compound words, diction and word choice, the cause and effect essay, and evaluating online reviews and influencer marketing.',
  [('What does direct speech do?', ['Quotes a speakers exact words within quotation marks', 'Removes all punctuation from a sentence', 'Always uses the future tense', 'Combines two unrelated sentences'], 0),
   ('What is a compound word?', ['A word formed by combining two or more smaller words', 'A word borrowed directly from another language with no change', 'A word with no defined meaning at all', 'A single letter used to represent a whole word'], 0),
   ('What does diction refer to?', ['An authors deliberate choice of words', 'The physical layout of a page', 'The number of chapters in a book', 'The font used to print a text'], 0),
   ('What does a cause and effect essay explain?', ['Why an event occurred and the consequences that followed', 'A random list of unrelated facts', 'Only the setting of a story', 'A single characters physical appearance'], 0),
   ('What can shape consumer opinions online?', ['Online reviews and influencer endorsements', 'Only the price listed on a product', 'Only the colour of a products packaging', 'Only the length of a product description'], 0)]),
M('Math Review: Statistics, Number Theory, and Probability (Days 161-169)',
  'Grade 8 Math strand review: students revisit the Law of Large Numbers, twin primes, projective geometry, the Rational Root Theorem, and the Monty Hall Problem.',
  [('What does the Law of Large Numbers describe?', ['How the average of repeated random trials tends toward the expected probability', 'A rule for rounding decimals to the nearest whole number', 'A method for factoring polynomials', 'How to calculate the area of a triangle'], 0),
   ('What are twin primes?', ['Pairs of prime numbers that differ by exactly two', 'Pairs of prime numbers that are always identical', 'Any two even numbers next to each other', 'Pairs of numbers that add up to exactly ten'], 0),
   ('What does projective geometry study?', ['Properties of shapes that stay the same under projection', 'Only the exact area of a circle', 'The weight of a three-dimensional solid', 'The colour of a geometric figure'], 0),
   ('What does the Rational Root Theorem help find?', ['A list of possible rational roots of a polynomial equation', 'The exact area of a triangle', 'A rule for rounding decimals', 'The colour of a graphed function'], 0),
   ('What is the Monty Hall Problem based on?', ['A game show scenario involving choosing between doors', 'A card game played with a standard deck', 'A dice game played by two players', 'A puzzle involving coin flips only'], 0)]),
Sc('Science Review: Chemistry, Physics, and Earth Science (Days 161-169)',
   'Grade 8 Science strand review: students revisit chromatography, the Doppler effect, weathering and the formation of caves, fermentation, and the Big Bang Theory.',
   [('What does chromatography do?', ['Separates the components of a mixture based on how they travel through a material', 'Combines several pure substances into a single mixture', 'Measures the temperature of a chemical reaction', 'Changes a mixture into a single element'], 0),
    ('What does the Doppler effect describe?', ['The change in pitch of a sound as its source moves toward or away from a listener', 'The change in colour of a light source at rest', 'The loss of all sound as an object moves', 'The change in the mass of a moving object'], 0),
    ('What does weathering do to rock over time?', ['Breaks it down through physical and chemical processes', 'Instantly turns rock into water', 'Has no effect on rock of any kind', 'Makes rock permanently indestructible'], 0),
    ('What is fermentation?', ['A process by which microorganisms break down sugars without oxygen', 'A process that requires large amounts of oxygen', 'A process that only occurs in plants', 'A process that destroys all sugar molecules instantly'], 0),
    ('What does the Big Bang Theory propose about the origin of the universe?', ['It began as an extremely hot, dense point that has been expanding ever since', 'It has always existed in its current form with no beginning', 'It began as a single planet that later became the whole universe', 'It formed instantly in its final shape with no expansion at all'], 0)]),
H('History Review: Social Programs and Modern Canadian Milestones (Days 161-169)',
  'Grade 8 History strand review: students revisit the Canada Pension Plan, Tommy Douglas and medicare in Saskatchewan, the North American Free Trade Agreement, the 1972 Canada-Soviet Summit Series, and the Berger Inquiry.',
  [('In what year was the Canada Pension Plan established?', ['1965', '1867', '1927', '1949'], 0),
   ('What position did Tommy Douglas hold when he introduced medicare in Saskatchewan?', ['Premier of Saskatchewan', 'Prime Minister of Canada', 'Mayor of Regina', 'Leader of the federal opposition'], 0),
   ('In what year did the North American Free Trade Agreement take effect?', ['1994', '1867', '1988', '1949'], 0),
   ('In what year did the Canada-Soviet Summit Series take place?', ['1972', '1867', '1949', '1988'], 0),
   ('Who led the inquiry into the proposed Mackenzie Valley Pipeline?', ['Justice Thomas Berger', 'Prime Minister Pierre Trudeau', 'Premier Tommy Douglas', 'Justice Thomas Rowell'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_161_170)
    append_to(8, g8_161_170)
