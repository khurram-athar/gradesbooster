#!/usr/bin/env python3
"""Grade 4, Days 181-187 -- FINAL BATCH extending Grade 4 from 180 to 187
days, completing the full 187-day Ontario curriculum target for this
grade. Modeled exactly on gen_grade4_days171_180.py: same L/M/Sc/SS
helpers over gen_curriculum's sub()/day()/append_to(), same TVO Learn
placeholder resourceLabel/resourceUrl convention (videoUrl intentionally
left unset, filled in later by the daily curriculum-video-backfill
scheduled task). This batch is only 7 days (not the usual 10) because
180 + 7 = 187, so it is structured as 6 new content days (181-186, one
new topic per subject per day) plus Day 187 as a final cross-subject
review day.

Topics chosen to avoid any overlap with the existing Grade 4 Days 1-180
topics (verified against data/grade4.json, which already densely covers
nearly the entire grade 4 curriculum, including the immediately prior
Days 171-180 batch). New topics: double negatives, malapropisms and word
mix-ups, writing a podcast script, building suspense in a story, and em
dashes and ellipses in writing for Language; multiplying a 4-digit number
by a 1-digit number, complementary and supplementary angles,
complementary events, understanding currency exchange rates, and
dividing a 3-digit number by a 2-digit divisor for Math; the excretory
system, Earths revolution and the four seasons, grassland and prairie
ecosystems, tornadoes, and gemstones for Science; and the Kingdom of
Axum, Canadas Prairie provinces, the Bank of Canada, Elections Canada,
and Canadas Coat of Arms and national motto for Social Studies -- none of
those exact ideas appear in Days 1-180 (note: Days 1-180 already cover
Earths rotation and the day/night cycle, desert survival strategies for
animals, and Canadian biomes including forests, wetlands, and tundra, so
this batch narrows to previously-untouched angles: Earths revolution and
the seasons specifically, distinct from Earths rotation and the
day/night cycle; desert plant adaptations specifically, distinct from
general desert animal survival strategies; and grassland/prairie
ecosystems specifically, a biome not covered in the earlier Canadian
biomes lesson). Day 186 also adds one further Language, Math, Science,
and Social Studies topic each (writing a postcard from a historical time
period, an introduction to imperial units of measurement, desert plant
adaptations, and the role of the Speaker of the House of Commons) to
complete the six regular days.

Day 187 is the final cross-subject review day of the entire 187-day
Grade 4 curriculum, matching the end-of-batch pattern used in every
prior batch (one representative question drawn from each of the first
five lessons of the batch, per subject, exactly as Day 180 did for Days
171-175). The four Day 187 review titles (Language Review: Grammar,
Vocabulary, and New Writing Forms / Math Review: Multiplication, Angles,
and Probability / Science Review: The Human Body, Seasons, and Natural
Forces / Social Studies Review: Ancient Civilizations, Geography, and
Government) were checked against every earlier review-day title in Days
1-180, including Day 140, Day 150, Day 160, Day 170, Day 180, and every
"Review: ... (Days X-Y)" day, and are textually distinct from all of
them. Since this is the capstone review closing out the full 187-day
Grade 4 program, each review lessons summary text explicitly notes it is
the final lesson of the 187-day curriculum, while the review titles and
quiz-question format otherwise follow the exact mechanical pattern used
in every prior batch (one verbatim question reused from each of the
first five lessons of the batch). No embedded ASCII double-quote or
apostrophe characters are used anywhere in title/summary/question/option
text, matching the convention used in gen_grade4_days171_180.py
(apostrophes dropped entirely, e.g. "Canadas" not "Canada's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L4 = 'https://tvolearn.com/pages/grade-4-language'
M4 = 'https://tvolearn.com/pages/grade-4-mathematics'
S4 = 'https://tvolearn.com/pages/grade-4-science-and-technology'
SS4 = 'https://tvolearn.com/pages/grade-4-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 4 Language',
    'TVO Learn: Grade 4 Mathematics',
    'TVO Learn: Grade 4 Science and Technology',
    'TVO Learn: Grade 4 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L4, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M4, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S4, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS4, q)


def _rebalance_answer_positions(days, seed=20260901):
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


g4_181_187 = [
day(181, [
L('Grammar: Double Negatives',
  'Grade 4 Language strand: a double negative occurs when two negative words are used in the same clause, which can cancel each other out or create confusing, non-standard grammar, so standard English uses only one negative word per clause.',
  [('What is a double negative?', ['Using two negative words in the same clause', 'Using two positive words in the same clause', 'A sentence with no verb', 'A question with two parts'], 0),
   ('Which sentence contains a double negative?', ['I do not have no pencils.', 'I do not have any pencils.', 'I have some pencils.', 'I have a pencil.'], 0),
   ('How many negative words should a single clause in standard English contain?', ['Just one', 'Exactly two', 'At least three', 'Zero, negatives are never allowed'], 0),
   ('Which sentence correctly avoids a double negative?', ['She does not want anything.', 'She does not want nothing.', 'She does not never want it.', 'She has not no interest.'], 0),
   ('Why do writers avoid double negatives in formal writing?', ['Double negatives can confuse the meaning of a sentence', 'Double negatives always make writing clearer', 'Formal writing requires at least two negatives per sentence', 'Double negatives are required by grammar rules'], 0)]),
M('Number Sense: Multiplying a 4-Digit Number by a 1-Digit Number',
  'Grade 4 Math strand: multiplying a 4-digit number by a 1-digit number involves multiplying each place value in turn, from ones through thousands, regrouping as needed and adding the partial results.',
  [('What is a good first step when multiplying a 4-digit number by a 1-digit number?', ['Multiply the ones digit first, then regroup as needed', 'Multiply the thousands digit first', 'Add the two numbers together', 'Divide the 4-digit number by the 1-digit number'], 0),
   ('What is 2,134 multiplied by 3?', ['6,402', '6,302', '6,502', '6,412'], 0),
   ('What is 4,021 multiplied by 2?', ['8,042', '8,142', '8,032', '8,242'], 0),
   ('When multiplying and a place value product is 10 or more, what should you do?', ['Regroup the extra value into the next place value', 'Ignore the extra value completely', 'Start the entire multiplication over', 'Write only the ones digit and stop'], 0),
   ('Why is it useful to multiply large numbers digit by digit?', ['It breaks a large multiplication into smaller, manageable steps', 'It always produces an incorrect product', 'It removes the need to know multiplication facts', 'It only works with numbers under 100'], 0)]),
Sc('Science: The Excretory System — How the Body Removes Waste',
   'Grade 4 Science strand: the excretory system, including the kidneys, bladder, and skin, removes waste products and excess water from the body to keep it healthy and balanced.',
   [('What is the main job of the excretory system?', ['Removing waste products and excess water from the body', 'Pumping blood through the body', 'Breaking down food for energy', 'Sending messages to the brain'], 0),
    ('Which organ filters waste out of the blood to form urine?', ['The kidneys', 'The heart', 'The lungs', 'The stomach'], 0),
    ('Where is urine stored before it leaves the body?', ['The bladder', 'The lungs', 'The brain', 'The stomach'], 0),
    ('Besides the kidneys and bladder, what other organ helps remove waste through sweat?', ['The skin', 'The heart', 'The eyes', 'The teeth'], 0),
    ('Why is the excretory system important for staying healthy?', ['It removes waste that could harm the body if it built up', 'It has no effect on the bodys health', 'It only functions once in a lifetime', 'It stops the body from ever needing water'], 0)]),
SS('Social Studies: The Kingdom of Axum — Ancient Trade Power of Africa',
   'Grade 4 Social Studies strand: the Kingdom of Axum was a powerful ancient trading civilization in what is now Ethiopia and Eritrea, known for its wealth from trade routes connecting Africa, Arabia, and the Mediterranean world.',
   [('Where was the ancient Kingdom of Axum located?', ['In what is now Ethiopia and Eritrea', 'In what is now France', 'In what is now Japan', 'In what is now Mexico'], 0),
    ('What made the Kingdom of Axum wealthy and powerful?', ['Its trade routes connecting Africa, Arabia, and the Mediterranean', 'Its large fishing fleet in the Pacific Ocean', 'Its control over the Arctic Ocean', 'Its isolation from all other civilizations'], 0),
    ('What goods might have been traded along Axums routes?', ['Items such as ivory, gold, and spices', 'Only modern electronics', 'Only plastic goods', 'Only automobiles'], 0),
    ('Why are trade routes important to understanding an ancient civilizations power?', ['They show how a civilization built wealth and connections with others', 'Trade routes have no connection to a civilizations power', 'Ancient civilizations never engaged in trade', 'Trade routes only existed in modern times'], 0),
    ('Why do historians study ancient trading powers like Axum?', ['To understand how early civilizations connected and influenced each other', 'Ancient trading powers have no historical importance', 'Axum has no connection to African history', 'Trade has never shaped history'], 0)]),
]),
day(182, [
L('Vocabulary: Malapropisms and Word Mix-Ups',
  'Grade 4 Language strand: a malapropism is the mistaken use of a word in place of a similar-sounding word, often creating a humorous or nonsensical sentence.',
  [('What is a malapropism?', ['The mistaken use of a word in place of a similar-sounding word', 'A word that has two opposite meanings', 'A word borrowed from another language', 'A word that rhymes with another word'], 0),
   ('Which sentence contains a malapropism?', ['We need to escape this dangerous situation, said the pacific leader.', 'We need to escape this dangerous situation, said the peaceful leader.', 'We need to leave now.', 'We must go quickly.'], 0),
   ('Why do malapropisms often create humor?', ['The mixed-up word creates an unexpected or silly meaning', 'Malapropisms always make perfect sense', 'Malapropisms are never noticed by readers', 'They always use the exact correct word'], 0),
   ('What might cause a person to use a malapropism?', ['Confusing two words that sound alike but have different meanings', 'Using a thesaurus correctly', 'Speaking in complete silence', 'Reading a dictionary definition aloud correctly'], 0),
   ('Why is it helpful to recognize malapropisms while reading or editing?', ['It helps identify and correct word-choice errors that change meaning', 'Malapropisms never affect the meaning of a sentence', 'Recognizing them has no value for writers', 'Malapropisms are always used on purpose by careful writers'], 0)]),
M('Geometry: Complementary and Supplementary Angles',
  'Grade 4 Math strand: complementary angles are two angles that add up to 90 degrees, while supplementary angles are two angles that add up to 180 degrees.',
  [('What do complementary angles add up to?', ['90 degrees', '180 degrees', '360 degrees', '45 degrees'], 0),
   ('What do supplementary angles add up to?', ['180 degrees', '90 degrees', '360 degrees', '270 degrees'], 0),
   ('If one angle measures 30 degrees, what does its complementary angle measure?', ['60 degrees', '150 degrees', '90 degrees', '70 degrees'], 0),
   ('If one angle measures 110 degrees, what does its supplementary angle measure?', ['70 degrees', '80 degrees', '110 degrees', '250 degrees'], 0),
   ('Why is it useful to know about complementary and supplementary angles?', ['It helps find missing angle measures when two angles form a right angle or straight line', 'These angle types are never found in real shapes', 'Complementary and supplementary angles always measure the same amount', 'Angles never add up to a fixed total'], 0)]),
Sc('Science: Earths Revolution and the Four Seasons',
   'Grade 4 Science strand: Earths revolution around the sun, combined with the tilt of its axis, causes the changing seasons as different parts of Earth receive more or less direct sunlight throughout the year.',
   [('What is Earths revolution?', ['Earths yearlong orbit around the sun', 'Earths daily spin on its axis', 'The moons orbit around Earth', 'The suns orbit around Earth'], 0),
    ('About how long does it take Earth to complete one revolution around the sun?', ['About one year', 'About one day', 'About one week', 'About one hour'], 0),
    ('What causes the changing seasons on Earth?', ['The tilt of Earths axis combined with its revolution around the sun', 'The moon changing shape each night', 'Earth speeding up and slowing down randomly', 'The sun moving closer and farther from Earth each day'], 0),
    ('During summer in the Northern Hemisphere, how is that part of Earth tilted?', ['Toward the sun, receiving more direct sunlight', 'Away from the sun, receiving less sunlight', 'Directly sideways to the sun', 'Earth is never tilted at all'], 0),
    ('Why is understanding Earths revolution important for understanding the seasons?', ['It explains why different times of year receive different amounts of sunlight', 'Revolution has no connection to the seasons', 'The seasons are caused only by ocean currents', 'Earths tilt never changes the amount of sunlight received'], 0)]),
SS('Social Studies: Canadas Prairie Provinces — Agriculture and Geography',
   'Grade 4 Social Studies strand: the Prairie provinces of Alberta, Saskatchewan, and Manitoba feature flat, fertile grassland well suited to growing crops such as wheat and canola, making the region a major centre of Canadian agriculture.',
   [('Which three provinces are commonly known as the Prairie provinces?', ['Alberta, Saskatchewan, and Manitoba', 'Ontario, Quebec, and Nova Scotia', 'British Columbia, Yukon, and Nunavut', 'New Brunswick, Newfoundland, and Labrador'], 0),
    ('What type of landscape is common across much of the Prairies?', ['Flat, fertile grassland', 'Tall mountain ranges', 'Dense tropical rainforest', 'Icy glaciers'], 0),
    ('Which crops are commonly grown in the Prairie provinces?', ['Wheat and canola', 'Coffee and cocoa', 'Bananas and pineapples', 'Rice grown in flooded paddies'], 0),
    ('Why is the Prairie region considered important to Canadas economy?', ['It produces a large share of Canadas agricultural output', 'It has no connection to Canadas economy', 'It produces no food at all', 'It is the least populated part of Canada with no industry'], 0),
    ('Why is fertile soil important to the Prairie provinces?', ['It allows large-scale farming of crops that feed Canada and other countries', 'Fertile soil has no effect on farming', 'The Prairies have no soil at all', 'Fertile soil prevents any crops from growing'], 0)]),
]),
day(183, [
L('Writing: Writing a Podcast Script',
  'Grade 4 Language strand: a podcast script is written to be spoken aloud, organized into a clear introduction, main segments, and a conclusion, often including natural-sounding language and cues for pacing.',
  [('What is a podcast script written for?', ['To be spoken aloud for listeners', 'To be read silently by one person', 'To be used only as a math worksheet', 'To replace all forms of written communication'], 0),
   ('What might a podcast script include at the very beginning?', ['A clear introduction to the topic or episode', 'The conclusion of the episode', 'A blank page', 'Only a single number'], 0),
   ('Why might a podcast script use natural-sounding language?', ['It helps the spoken delivery sound conversational to listeners', 'Podcast scripts are never meant to be read aloud', 'Formal, robotic language always sounds best when spoken', 'Natural language confuses listeners on purpose'], 0),
   ('What might a writer include in a script to help control pacing while speaking?', ['Cues such as pauses or emphasis notes', 'Random unrelated numbers', 'A list of unrelated topics', 'Complete silence with no words at all'], 0),
   ('Why is organizing a podcast script into segments helpful?', ['It helps guide listeners clearly through different parts of the episode', 'Segments have no effect on how listeners follow along', 'A podcast script should never be organized', 'Organization only matters in written essays, not audio'], 0)]),
M('Probability: Complementary Events',
  'Grade 4 Math strand: complementary events are two outcomes where exactly one must happen, and their probabilities always add up to 1, so the probability of an event not happening equals 1 minus the probability of it happening.',
  [('What are complementary events?', ['Two outcomes where exactly one of them must happen', 'Two outcomes that can never happen', 'Two outcomes that always happen together', 'Two outcomes with the exact same probability'], 0),
   ('What do the probabilities of complementary events always add up to?', ['1', '0', '2', '100'], 0),
   ('If the probability of rain tomorrow is 1/4, what is the probability it will not rain?', ['3/4', '1/4', '1/2', '4/4'], 0),
   ('If the probability of drawing a red marble is 0.3, what is the probability of not drawing a red marble?', ['0.7', '0.3', '1.3', '0.03'], 0),
   ('Why is understanding complementary events useful in probability?', ['It allows the probability of an event not happening to be calculated easily', 'Complementary events can never be calculated', 'It only applies to events that are impossible', 'Complementary events always have equal probabilities of exactly 0.5'], 0)]),
Sc('Science: Grassland and Prairie Ecosystems',
   'Grade 4 Science strand: grassland and prairie ecosystems are dominated by grasses rather than trees, supporting animals such as bison and burrowing rodents that are adapted to open, windy environments with periodic wildfires.',
   [('What plant life dominates a grassland or prairie ecosystem?', ['Grasses, rather than trees', 'Dense rainforest trees', 'Coral and seaweed', 'Cactus and desert shrubs only'], 0),
    ('Which animal is commonly associated with North American prairies?', ['The bison', 'The polar bear', 'The dolphin', 'The penguin'], 0),
    ('Why might burrowing animals be well adapted to prairie ecosystems?', ['Burrows offer shelter in an open landscape with few trees', 'Burrows are only useful in forests', 'Prairie animals never need shelter', 'Burrowing has no survival advantage on a prairie'], 0),
    ('What natural event periodically affects many grassland ecosystems?', ['Wildfires', 'Constant snowfall', 'Ocean flooding', 'Volcanic eruptions'], 0),
    ('Why are grassland ecosystems important to study?', ['They support unique wildlife and are important for agriculture', 'Grasslands support no forms of life', 'Grasslands have no connection to farming', 'Grassland ecosystems are identical to rainforests'], 0)]),
SS('Social Studies: The Bank of Canada — Canadas Central Bank',
   'Grade 4 Social Studies strand: the Bank of Canada is the countrys central bank, responsible for issuing Canadian currency and working to keep prices stable by managing the countrys money supply.',
   [('What is the Bank of Canada?', ['Canadas central bank', 'A local bank branch in one city', 'A private company that sells cars', 'A museum about Canadian history'], 0),
    ('What is one key responsibility of the Bank of Canada?', ['Issuing Canadian currency', 'Building highways', 'Running national parks', 'Regulating television broadcasting'], 0),
    ('What does the Bank of Canada aim to keep stable?', ['Prices, by managing the countrys money supply', 'The weather across the country', 'The number of provinces in Canada', 'The length of the school year'], 0),
    ('How is the Bank of Canada different from a regular retail bank a person might use daily?', ['It manages the national economy rather than serving individual customers directly', 'It has no role in Canadas economy', 'It is owned by a single private citizen', 'It only operates outside of Canada'], 0),
    ('Why is a central bank important to a countrys economy?', ['It helps manage currency and stabilize prices for the whole country', 'Central banks have no effect on an economy', 'A country cannot have any currency without a branch in every town', 'It only affects one small business'], 0)]),
]),
day(184, [
L('Reading: Building Suspense in a Story',
  'Grade 4 Language strand: authors build suspense by withholding information, using pacing, and creating tension about what will happen next, keeping readers eager to continue.',
  [('What does it mean for an author to build suspense?', ['Creating tension and curiosity about what will happen next', 'Revealing the ending at the very start of the story', 'Removing all conflict from the story', 'Ending the story before any events occur'], 0),
   ('What is one technique authors use to build suspense?', ['Withholding key information from the reader', 'Explaining every detail immediately', 'Avoiding any conflict in the plot', 'Skipping the climax of the story'], 0),
   ('How can pacing affect suspense in a story?', ['Slowing down key moments can increase tension for readers', 'Pacing has no effect on how suspenseful a story feels', 'Suspense only depends on the length of a book', 'Fast pacing always removes all suspense'], 0),
   ('Why might an author end a chapter at a tense moment?', ['To make readers want to keep reading to find out what happens', 'To immediately reveal the solution to the conflict', 'To end the story permanently', 'To remove all interest from the plot'], 0),
   ('Why is suspense an effective tool in storytelling?', ['It keeps readers emotionally engaged and eager to continue', 'Suspense makes readers stop reading immediately', 'Suspense has no effect on how a story is experienced', 'Suspense is only used in nonfiction writing'], 0)]),
M('Financial Literacy: Understanding Currency Exchange Rates',
  'Grade 4 Math strand: a currency exchange rate shows how much one countrys money is worth compared to another countrys money, and it is used to convert an amount from one currency into another.',
  [('What does a currency exchange rate show?', ['How much one countrys money is worth compared to another countrys money', 'The total population of a country', 'The distance between two countries', 'The temperature in a country'], 0),
   ('What is a currency exchange rate used for?', ['Converting an amount of money from one currency into another', 'Measuring the size of a country', 'Calculating the time zone of a country', 'Determining a countrys official language'], 0),
   ('If 1 Canadian dollar equals 0.75 US dollars, how many US dollars would 10 Canadian dollars convert to?', ['7.50 US dollars', '10.75 US dollars', '0.75 US dollars', '75 US dollars'], 0),
   ('Why might exchange rates change over time?', ['Economic factors can cause the relative value of currencies to shift', 'Exchange rates are always fixed and never change', 'Currency values have no connection to economics', 'Exchange rates only apply to one single day in history'], 0),
   ('Why is understanding exchange rates useful when travelling to another country?', ['It helps travellers know how much their money is worth in the local currency', 'Exchange rates have no effect on travel', 'Money never needs to be converted between countries', 'Every country uses the exact same currency'], 0)]),
Sc('Science: Tornadoes — How They Form and Safety',
   'Grade 4 Science strand: a tornado is a rapidly rotating column of air that forms during severe thunderstorms when warm and cold air masses collide, and knowing safety steps like sheltering in a basement or interior room can help keep people safe.',
   [('What is a tornado?', ['A rapidly rotating column of air extending from a thunderstorm to the ground', 'A slow-moving cloud with no wind', 'A type of ocean wave', 'A calm, sunny weather pattern'], 0),
    ('What kind of storm can produce a tornado?', ['A severe thunderstorm', 'A light drizzle', 'A clear, cloudless sky', 'A gentle breeze'], 0),
    ('What often happens when warm and cold air masses collide?', ['Conditions can become unstable enough to form severe storms, including tornadoes', 'The weather always stays exactly the same', 'All clouds instantly disappear', 'Temperatures instantly become equal everywhere'], 0),
    ('What is a recommended safety step during a tornado warning?', ['Sheltering in a basement or interior room away from windows', 'Standing outside to watch the tornado', 'Opening all the windows in the house', 'Driving directly toward the tornado'], 0),
    ('Why is it important to understand tornado safety?', ['Knowing safety steps can help protect people during a dangerous storm', 'Tornado safety has no effect on protecting people', 'Tornadoes never pose any danger', 'Safety steps only apply to other types of weather'], 0)]),
SS('Social Studies: Elections Canada — Running Canadas Federal Elections',
   'Grade 4 Social Studies strand: Elections Canada is the independent federal agency responsible for organizing and overseeing national elections, ensuring that voting is fair, accessible, and accurately counted.',
   [('What is Elections Canada?', ['The independent federal agency responsible for organizing national elections', 'A private company that sells voting machines', 'A group that only counts votes in one city', 'A television network that reports election results'], 0),
    ('What is one responsibility of Elections Canada?', ['Ensuring that federal voting is fair and accurately counted', 'Building new highways', 'Setting provincial tax rates', 'Managing national parks'], 0),
    ('Why is it important for Elections Canada to be independent?', ['So elections are run fairly without political interference', 'So only one political party can ever win', 'So elections never actually take place', 'So votes are never counted at all'], 0),
    ('What might Elections Canada do to help make voting accessible?', ['Provide multiple ways to vote, such as by mail or in person', 'Prevent citizens from voting entirely', 'Only allow voting in one single city', 'Require voters to pay a fee to vote'], 0),
    ('Why is a fair and accurate election process important in a democracy?', ['It ensures that the results reflect the true will of the voters', 'Fair elections have no importance in a democracy', 'Accuracy in vote counting is never necessary', 'Democracy does not require any elections at all'], 0)]),
]),
day(185, [
L('Grammar: Em Dashes and Ellipses in Writing',
  'Grade 4 Language strand: an em dash can be used to set off extra information or create a dramatic pause, while an ellipsis, made of three dots, shows that words have been left out or that a thought trails off.',
  [('What can an em dash be used for in a sentence?', ['Setting off extra information or creating a dramatic pause', 'Ending every sentence in a paragraph', 'Replacing all commas in a piece of writing', 'Starting the first word of every sentence'], 0),
   ('How many dots make up an ellipsis?', ['Three', 'One', 'Five', 'Two'], 0),
   ('What can an ellipsis show in a sentence?', ['That words have been left out or a thought trails off', 'That a sentence is a question', 'That a word is misspelled', 'That a sentence must be read loudly'], 0),
   ('Which sentence correctly uses an em dash to add extra information?', ['The trip — though long and tiring — was worth it in the end.', 'The trip, though, long, and, tiring was worth it, in the end.', 'The trip though long and tiring was worth it in the end', 'The trip; though long and tiring; was worth it in the end.'], 0),
   ('Why might a writer choose an em dash instead of a comma?', ['To create a stronger pause or emphasize the extra information', 'Em dashes and commas always mean the exact same thing', 'Em dashes are never used in writing', 'Commas can never set off extra information'], 0)]),
M('Number Sense: Dividing a 3-Digit Number by a 2-Digit Divisor',
  'Grade 4 Math strand: dividing a 3-digit number by a 2-digit divisor involves estimating how many times the divisor fits into the leading digits, then dividing, multiplying, subtracting, and bringing down the next digit.',
  [('What is a helpful strategy when starting to divide a 3-digit number by a 2-digit divisor?', ['Estimate how many times the divisor fits into the leading digits', 'Immediately guess the final answer with no estimation', 'Add the divisor to the 3-digit number', 'Multiply the two numbers together'], 0),
   ('What is 288 divided by 12?', ['24', '22', '26', '20'], 0),
   ('What is 455 divided by 13?', ['35', '33', '37', '31'], 0),
   ('After dividing and multiplying at each step, what should you do next?', ['Subtract, then bring down the next digit if there is one', 'Multiply again by the same divisor', 'Skip the remaining digits entirely', 'Add the divisor to the quotient'], 0),
   ('Why might dividing by a 2-digit divisor be more challenging than dividing by a 1-digit divisor?', ['It often requires estimating multiples of a larger number', 'It never requires any estimation at all', '2-digit divisors always divide evenly', 'Dividing by a 2-digit number is never used in math'], 0)]),
Sc('Science: Gemstones — How Precious Minerals Form',
   'Grade 4 Science strand: gemstones are minerals that form underground under intense heat and pressure over long periods of time, and their hardness, colour, and clarity determine how they are valued and used in jewellery.',
   [('What is a gemstone?', ['A mineral valued for qualities such as its hardness, colour, and clarity', 'A type of soft plant tissue', 'A tool used only for farming', 'A liquid found in oceans'], 0),
    ('Under what conditions do many gemstones form underground?', ['Intense heat and pressure over long periods of time', 'Freezing temperatures with no pressure at all', 'Instantly, within a few seconds', 'Only inside living plants'], 0),
    ('Which quality might affect how a gemstone is valued?', ['Its hardness, colour, and clarity', 'Its weight in kilograms only', 'Its exact age in days', 'The season it was found in'], 0),
    ('What are gemstones commonly used for?', ['Jewellery and decorative items', 'Cooking ingredients', 'Building roads', 'Producing electricity directly'], 0),
    ('Why do gemstones often take a long time to form?', ['Mineral crystals need extended time under heat and pressure to grow', 'Gemstones form instantly with no natural process', 'Gemstones are manufactured only in factories', 'Time has no effect on how minerals form'], 0)]),
SS('Social Studies: Canadas Coat of Arms and National Motto',
   'Grade 4 Social Studies strand: the Coat of Arms of Canada is an official symbol featuring a lion, a unicorn, and other heraldic images, paired with the national motto A Mari Usque Ad Mare, meaning from sea to sea.',
   [('What is the Coat of Arms of Canada?', ['An official symbol representing Canada, featuring heraldic images', 'A type of Canadian currency', 'A national holiday', 'A style of Canadian clothing'], 0),
    ('What does Canadas national motto, A Mari Usque Ad Mare, mean?', ['From sea to sea', 'Strength and honour', 'Peace and prosperity', 'One nation, many peoples'], 0),
    ('Which animals appear as heraldic images on Canadas Coat of Arms?', ['A lion and a unicorn', 'A polar bear and a beaver', 'A moose and an eagle', 'A wolf and a hawk'], 0),
    ('Why might a country have an official Coat of Arms?', ['To serve as a formal symbol representing the nations identity and history', 'A Coat of Arms has no meaning or purpose', 'It is only used for decoration with no symbolic value', 'Every country is required to have an identical design'], 0),
    ('Why is Canadas national motto meaningful to the countrys geography?', ['It reflects Canadas vast stretch between the Atlantic and Pacific oceans', 'The motto has no connection to Canadas geography', 'Canada does not border any oceans', 'The motto refers only to a single small lake'], 0)]),
]),
day(186, [
L('Writing: Writing a Postcard from a Historical Time Period',
  'Grade 4 Language strand: writing a postcard from a historical time period combines factual details about the past with a personal, first-person voice, describing what a writer might have seen, heard, or felt if living then.',
  [('What does writing a postcard from a historical time period combine?', ['Factual historical details with a personal, first-person voice', 'Only scientific formulas with no narrative voice', 'A list of unrelated numbers', 'Only present-day events with no history at all'], 0),
   ('What point of view is often used when writing a historical postcard?', ['First-person, as if the writer lived during that time', 'Third-person only, describing someone else entirely', 'No point of view at all', 'Only a formal business tone'], 0),
   ('What might a historical postcard describe?', ['What the writer might have seen, heard, or felt during that time', 'Only modern technology that did not exist then', 'A completely unrelated fictional planet', 'Only mathematical equations'], 0),
   ('Why is researching a time period important before writing a postcard from it?', ['It helps ensure the details feel accurate and believable', 'Research has no effect on historical writing', 'Postcards never need any factual information', 'Historical accuracy is never important in writing'], 0),
   ('Why might writing a postcard from history help a reader understand the past?', ['It presents historical events through a personal, relatable perspective', 'Postcards have no connection to understanding history', 'Personal perspectives always distort historical facts', 'Historical writing must always avoid a personal viewpoint'], 0)]),
M('Measurement: Introduction to Imperial Units (Inches, Feet, and Yards)',
  'Grade 4 Math strand: imperial units, including inches, feet, and yards, are a system of measurement historically used in Canada and still commonly seen today, alongside the metric system, especially for measuring length.',
  [('Which of these is an imperial unit of length?', ['Inches', 'Kilometres', 'Litres', 'Grams'], 0),
   ('How many inches are in one foot?', ['12', '10', '3', '100'], 0),
   ('How many feet are in one yard?', ['3', '12', '1', '10'], 0),
   ('Which measurement system, alongside imperial units, is commonly used in Canada today?', ['The metric system', 'The Roman numeral system', 'The binary number system', 'The Celsius-only weight system'], 0),
   ('Why is it useful to recognize imperial units even though Canada mainly uses the metric system?', ['Imperial units still appear in some everyday contexts and older measurements', 'Imperial units are never used or seen anywhere in Canada', 'Imperial units and metric units are always exactly identical', 'Recognizing imperial units has no practical use at all'], 0)]),
Sc('Science: Desert Plant Adaptations — Cacti and Succulents',
   'Grade 4 Science strand: desert plants such as cacti and succulents have adaptations like thick, water-storing tissue and small or spiny leaves that help them survive in hot, dry environments with little rainfall.',
   [('What is one adaptation common to many desert plants like cacti?', ['Thick, water-storing tissue', 'Large, thin leaves that lose water quickly', 'Roots that only grow in constantly flooded soil', 'A need for extremely cold temperatures'], 0),
    ('Why might a cactus have spines instead of large leaves?', ['Spines reduce water loss and can help protect the plant', 'Spines increase water loss significantly', 'Spines have no function for the plant', 'Spines are only used for producing flowers'], 0),
    ('What is a succulent?', ['A plant that stores water in its thick leaves or stems', 'A plant that only grows underwater', 'A plant that cannot survive any sunlight', 'A type of tree found only in rainforests'], 0),
    ('Why do desert plants need special adaptations to survive?', ['Desert environments are hot and dry with little rainfall', 'Deserts receive constant heavy rainfall', 'Desert plants face no environmental challenges', 'Deserts are always cold with abundant water'], 0),
    ('Why is studying desert plant adaptations valuable to scientists?', ['It helps explain how living things survive in extreme environments', 'Desert plants have no adaptations worth studying', 'Adaptations only occur in animals, never in plants', 'Studying plants has no scientific value'], 0)]),
SS('Social Studies: The Role of the Speaker of the House of Commons',
   'Grade 4 Social Studies strand: the Speaker of the House of Commons is a Member of Parliament chosen to preside over debates, maintain order, and ensure that parliamentary rules are followed during sittings.',
   [('What is the Speaker of the House of Commons?', ['A Member of Parliament chosen to preside over debates', 'The leader of a foreign country', 'A judge on the Supreme Court', 'A newspaper reporter covering Parliament'], 0),
    ('What is one key responsibility of the Speaker?', ['Maintaining order during debates in the House of Commons', 'Setting municipal parking bylaws', 'Managing a citys public library', 'Running a national park'], 0),
    ('How is the Speaker of the House of Commons chosen?', ['Elected by fellow Members of Parliament', 'Appointed by a foreign government', 'Selected randomly from the public', 'Chosen by a single vote in one town'], 0),
    ('Why is it important for the Speaker to remain impartial during debates?', ['To ensure fairness for all Members of Parliament regardless of party', 'Impartiality has no role in running debates', 'The Speaker should always favour one political party', 'Fairness is never required in Parliament'], 0),
    ('Why is the role of the Speaker important to how Parliament functions?', ['It helps ensure debates are conducted in an orderly, fair manner', 'The Speaker has no effect on how Parliament runs', 'Parliament could function identically with no Speaker at all', 'The Speakers role is purely ceremonial with no real duties'], 0)]),
]),
day(187, [
L('Language Review: Grammar, Vocabulary, and New Writing Forms',
  'Grade 4 Language strand review: as the final lesson of the 187-day Grade 4 curriculum, students revisit double negatives, malapropisms, writing a podcast script, building suspense in a story, and em dashes and ellipses.',
  [('What is a double negative?', ['Using two negative words in the same clause', 'Using two positive words in the same clause', 'A sentence with no verb', 'A question with two parts'], 0),
   ('What is a malapropism?', ['The mistaken use of a word in place of a similar-sounding word', 'A word that has two opposite meanings', 'A word borrowed from another language', 'A word that rhymes with another word'], 0),
   ('What is a podcast script written for?', ['To be spoken aloud for listeners', 'To be read silently by one person', 'To be used only as a math worksheet', 'To replace all forms of written communication'], 0),
   ('What does it mean for an author to build suspense?', ['Creating tension and curiosity about what will happen next', 'Revealing the ending at the very start of the story', 'Removing all conflict from the story', 'Ending the story before any events occur'], 0),
   ('What can an em dash be used for in a sentence?', ['Setting off extra information or creating a dramatic pause', 'Ending every sentence in a paragraph', 'Replacing all commas in a piece of writing', 'Starting the first word of every sentence'], 0)]),
M('Math Review: Multiplication, Angles, and Probability',
  'Grade 4 Math strand review: as the final lesson of the 187-day Grade 4 curriculum, students revisit multiplying a 4-digit number by a 1-digit number, complementary and supplementary angles, complementary events, currency exchange rates, and dividing a 3-digit number by a 2-digit divisor.',
  [('What is a good first step when multiplying a 4-digit number by a 1-digit number?', ['Multiply the ones digit first, then regroup as needed', 'Multiply the thousands digit first', 'Add the two numbers together', 'Divide the 4-digit number by the 1-digit number'], 0),
   ('What do complementary angles add up to?', ['90 degrees', '180 degrees', '360 degrees', '45 degrees'], 0),
   ('What are complementary events?', ['Two outcomes where exactly one of them must happen', 'Two outcomes that can never happen', 'Two outcomes that always happen together', 'Two outcomes with the exact same probability'], 0),
   ('What does a currency exchange rate show?', ['How much one countrys money is worth compared to another countrys money', 'The total population of a country', 'The distance between two countries', 'The temperature in a country'], 0),
   ('What is a helpful strategy when starting to divide a 3-digit number by a 2-digit divisor?', ['Estimate how many times the divisor fits into the leading digits', 'Immediately guess the final answer with no estimation', 'Add the divisor to the 3-digit number', 'Multiply the two numbers together'], 0)]),
Sc('Science Review: The Human Body, Seasons, and Natural Forces',
   'Grade 4 Science strand review: as the final lesson of the 187-day Grade 4 curriculum, students revisit the excretory system, Earths revolution and the seasons, grassland and prairie ecosystems, tornadoes, and gemstones.',
   [('What is the main job of the excretory system?', ['Removing waste products and excess water from the body', 'Pumping blood through the body', 'Breaking down food for energy', 'Sending messages to the brain'], 0),
    ('What is Earths revolution?', ['Earths yearlong orbit around the sun', 'Earths daily spin on its axis', 'The moons orbit around Earth', 'The suns orbit around Earth'], 0),
    ('What plant life dominates a grassland or prairie ecosystem?', ['Grasses, rather than trees', 'Dense rainforest trees', 'Coral and seaweed', 'Cactus and desert shrubs only'], 0),
    ('What is a tornado?', ['A rapidly rotating column of air extending from a thunderstorm to the ground', 'A slow-moving cloud with no wind', 'A type of ocean wave', 'A calm, sunny weather pattern'], 0),
    ('What is a gemstone?', ['A mineral valued for qualities such as its hardness, colour, and clarity', 'A type of soft plant tissue', 'A tool used only for farming', 'A liquid found in oceans'], 0)]),
SS('Social Studies Review: Ancient Civilizations, Geography, and Government',
   'Grade 4 Social Studies strand review: as the final lesson of the 187-day Grade 4 curriculum, students revisit the Kingdom of Axum, Canadas Prairie provinces, the Bank of Canada, Elections Canada, and Canadas Coat of Arms.',
   [('Where was the ancient Kingdom of Axum located?', ['In what is now Ethiopia and Eritrea', 'In what is now France', 'In what is now Japan', 'In what is now Mexico'], 0),
    ('Which three provinces are commonly known as the Prairie provinces?', ['Alberta, Saskatchewan, and Manitoba', 'Ontario, Quebec, and Nova Scotia', 'British Columbia, Yukon, and Nunavut', 'New Brunswick, Newfoundland, and Labrador'], 0),
    ('What is the Bank of Canada?', ['Canadas central bank', 'A local bank branch in one city', 'A private company that sells cars', 'A museum about Canadian history'], 0),
    ('What is Elections Canada?', ['The independent federal agency responsible for organizing national elections', 'A private company that sells voting machines', 'A group that only counts votes in one city', 'A television network that reports election results'], 0),
    ('What is the Coat of Arms of Canada?', ['An official symbol representing Canada, featuring heraldic images', 'A type of Canadian currency', 'A national holiday', 'A style of Canadian clothing'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_181_187)
    append_to(4, g4_181_187)
