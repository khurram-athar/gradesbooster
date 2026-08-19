#!/usr/bin/env python3
"""Grade 5, Days 181-187 -- the FINAL batch for Grade 5, extending it from
180 to 187 days and completing the full 187-day Ontario curriculum target
for this grade. Modeled exactly on gen_grade5_days171_180.py (itself
modeled on the preceding batches all the way back to
gen_grade5_days141_150.py): same L/M/Sc/SS helpers over gen_curriculum's
sub()/day()/append_to(), same TVO Learn placeholder resourceLabel/
resourceUrl convention (videoUrl intentionally left unset, filled in later
by the daily curriculum-video-backfill scheduled task), and the same
_rebalance_answer_positions() post-processing step.

This batch is only 7 days, not the usual 10, because 180 + 7 = 187 (the
full-year target). It is structured as 6 new content days (Days 181-186,
one new topic per subject per day) plus Day 187, a final cross-subject
review day that also serves as the capstone review for the entire 187-day
K-12 curriculum build for this grade.

Every existing (subject, title) pair across Grade 5 Days 1-180 was dumped
from data/grade5.json (720 entries, all unique) and checked against every
topic below before it was chosen. New topics: writing a limerick,
neologisms (newly invented words), recognizing deepfakes and manipulated
media, understanding anthropomorphism in stories, and using parentheses
for extra information for Language; triangular numbers, classifying
prisms by their bases, constructing frequency polygons, understanding
insurance basics, and multiplying by 11 using mental math tricks for
Math; diffusion, blood types and the science of blood donation, vaccines
and how they help the immune system, nuclear fusion and how the Sun
produces energy, and the process of fossilization for Science; and the
Canadian Bill of Rights of 1960, responsible government and how Canada
gained self-rule, Canadas role in the Cold War, the Royal Canadian Mint,
and understanding GST, PST, and HST in Canada for Social Studies -- none
of those exact ideas appear in Days 1-180. Day 187 is the final
cross-subject review day, matching the end-of-batch pattern used in every
prior batch (drawing one representative quiz question per subject from
each of the first five days of the batch, Days 181-185, exactly as Day
180 drew from Days 171-175). Because this is the very last day of the
entire K-12 curriculum build for this grade, the Day 187 review titles
and summaries acknowledge this is a capstone/end-of-program review, while
still following the exact mechanical review-day format used in every
prior batch. The four Day 187 review titles were checked against every
earlier review-day title in Days 1-180 and are textually distinct from
all of them.

No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are dropped entirely, matching
the rest of Grade 5 Days 1-180 (e.g. "Canadas" not "Canada's", "countrys"
not "country's").
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L5 = 'https://tvolearn.com/pages/grade-5-language'
M5 = 'https://tvolearn.com/pages/grade-5-mathematics'
S5 = 'https://tvolearn.com/pages/grade-5-science-and-technology'
SS5 = 'https://tvolearn.com/pages/grade-5-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 5 Language',
    'TVO Learn: Grade 5 Mathematics',
    'TVO Learn: Grade 5 Science and Technology',
    'TVO Learn: Grade 5 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L5, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M5, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S5, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS5, q)


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


g5_181_187 = [
day(181, [
L('Poetry: Writing a Limerick',
  'Grade 5 Language strand: a limerick is a humorous five-line poem with an AABBA rhyme scheme, where lines one, two, and five are longer and rhyme together, and lines three and four are shorter and rhyme together.',
  [('How many lines does a limerick have?', ['5', '3', '4', '7'], 0),
   ('What rhyme scheme does a limerick traditionally follow?', ['AABBA', 'ABAB', 'AAAA', 'ABCB'], 0),
   ('What tone does a limerick usually have?', ['Humorous or silly', 'Extremely serious', 'Formal and solemn', 'This concept has no connection to poetry'], 0),
   ('Which lines in a limerick are typically shorter than the others?', ['Lines three and four', 'Lines one and two', 'Lines two and five', 'All five lines are always the same length'], 0),
   ('Why might a poet choose the limerick form to tell a silly, exaggerated story?', ['Its bouncy rhythm and rhyme scheme suit a playful, comic tone', 'Limericks are always written about serious historical events', 'This concept has no relevance to poetry', 'A limerick can never include any humour at all'], 0)]),
M('Number Sense: Triangular Numbers',
  'Grade 5 Math strand: a triangular number is a number that can be arranged into an equilateral triangle of dots, formed by adding consecutive whole numbers starting from 1, such as 1, 3, 6, 10, and 15.',
  [('What is a triangular number?', ['A number that can be arranged into an equilateral triangle of dots', 'A number that is always divisible by 3', 'A number with exactly three digits', 'A number that can never be added to another number'], 0),
   ('What are the first four triangular numbers?', ['1, 3, 6, 10', '1, 2, 3, 4', '2, 4, 6, 8', '1, 4, 9, 16'], 0),
   ('How is the triangular number 10 formed by adding consecutive whole numbers?', ['1 plus 2 plus 3 plus 4 equals 10', '10 is formed only by multiplying 2 and 5', '10 has no connection to consecutive whole numbers', 'This concept has no relevance to number sense'], 0),
   ('What is the next triangular number after 15?', ['21', '18', '20', '16'], 0),
   ('Why might arranging dots into a triangle shape help someone understand how triangular numbers grow?', ['The visual pattern shows how each new row adds one more dot than the last', 'Arranging dots never shows any pattern in triangular numbers', 'This concept has no connection to math', 'Triangular numbers always decrease as more dots are added'], 0)]),
Sc('Diffusion — How Substances Spread and Mix',
   'Grade 5 Science strand: diffusion is the movement of particles from an area of higher concentration to an area of lower concentration, such as when a drop of food colouring gradually spreads through a glass of water.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The freezing of a liquid into a solid', 'The bending of light through a lens', 'This concept has no connection to science'], 0),
    ('What happens when a drop of food colouring is placed in a glass of water?', ['It gradually spreads through the water by diffusion', 'It immediately disappears with no visible change', 'It always sinks straight to the bottom and stays there', 'This concept has no relevance to diffusion'], 0),
    ('Why does diffusion usually happen faster in a gas than in a liquid?', ['Gas particles move more freely and quickly than particles in a liquid', 'Gas particles never move at all', 'This concept has no connection to science', 'Liquids always diffuse faster than gases'], 0),
    ('Why might you eventually smell perfume from across a room even if you are far from the source?', ['Perfume particles diffuse through the air from an area of higher to lower concentration', 'Smells never travel through the air by diffusion', 'This concept has no relevance to science', 'Perfume particles can only be smelled right next to the bottle'], 0),
    ('Why does diffusion eventually stop once particles are evenly spread throughout a space?', ['There is no longer a difference in concentration to drive further movement', 'Diffusion never stops once it begins', 'This concept has no connection to science', 'Particles always continue moving toward a single concentrated point'], 0)]),
SS('The Canadian Bill of Rights of 1960',
   'Grade 5 Social Studies strand: the Canadian Bill of Rights, passed in 1960, was an early federal law protecting basic rights and freedoms, later expanded upon by the Charter of Rights and Freedoms in 1982.',
   [('What was the Canadian Bill of Rights?', ['An early federal law protecting basic rights and freedoms', 'A law that created the Supreme Court of Canada', 'A treaty between Canada and another country', 'This concept has no connection to Canadian history'], 0),
    ('In what year was the Canadian Bill of Rights passed?', ['1960', '1867', '1982', '1945'], 0),
    ('What later document expanded upon the protections in the Canadian Bill of Rights?', ['The Charter of Rights and Freedoms', 'The Statute of Westminster', 'The Indian Act', 'This concept has no relevance to Canadian government'], 0),
    ('Why is the Canadian Bill of Rights considered an important step in Canadian history?', ['It was one of the first federal laws to formally protect basic rights and freedoms', 'It had no effect on rights or freedoms in Canada', 'This concept has no connection to social studies', 'It removed all rights that Canadians previously had'], 0),
    ('Why might the Charter of Rights and Freedoms be considered stronger than the earlier Canadian Bill of Rights?', ['The Charter is entrenched in the Constitution, giving it greater legal authority', 'The Charter has no connection to the Canadian Bill of Rights', 'This concept has no relevance to social studies', 'The Canadian Bill of Rights was always more powerful than the Charter'], 0)]),
]),
day(182, [
L('Vocabulary: Neologisms — Newly Invented Words',
  'Grade 5 Language strand: a neologism is a newly coined word or phrase that enters a language, often created to describe new technology, culture, or ideas, such as selfie or blog.',
  [('What is a neologism?', ['A newly coined word or phrase that enters a language', 'A word borrowed directly from an ancient language', 'A word that has completely disappeared from use', 'This concept has no connection to vocabulary'], 0),
   ('Which of these is an example of a neologism?', ['Selfie', 'House', 'Tree', 'Water'], 0),
   ('What often inspires the creation of a neologism?', ['New technology, culture, or ideas', 'Only ancient historical events', 'This concept has no relevance to vocabulary', 'Neologisms are never inspired by anything new'], 0),
   ('Why might a neologism like blog have entered common use?', ['It described a new kind of online activity that needed a name', 'It has existed in the language for thousands of years', 'This concept has no connection to vocabulary', 'New words are never created for new inventions'], 0),
   ('Why does a language often gain new neologisms over time?', ['Language evolves to describe new inventions, trends, and ideas as they appear', 'A language never changes or adds new words', 'This concept has no relevance to vocabulary', 'Neologisms always replace every existing word in a language'], 0)]),
M('Geometry: Classifying Prisms by Their Bases',
  'Grade 5 Math strand: a prism is named according to the shape of its base, such as a triangular prism having triangular bases or a hexagonal prism having hexagonal bases, with rectangular faces connecting the two matching bases.',
  [('How is a prism named?', ['According to the shape of its base', 'According to its total number of faces only', 'According to its colour', 'This concept has no connection to geometry'], 0),
   ('What shape are the bases of a triangular prism?', ['Triangles', 'Squares', 'Hexagons', 'Circles'], 0),
   ('What connects the two matching bases of a prism?', ['Rectangular faces', 'Triangular faces only', 'Curved surfaces', 'This concept has no relevance to prisms'], 0),
   ('How many triangular faces does a hexagonal prism have?', ['0, since its side faces are rectangles', '6', '2', '4'], 0),
   ('Why might identifying the shape of a prisms base be the fastest way to classify it?', ['The base shape determines the prisms name and much of its structure', 'The base shape has no connection to how a prism is classified', 'This concept has no relevance to geometry', 'Every prism has exactly the same base shape'], 0)]),
Sc('Blood Types and the Science of Blood Donation',
   'Grade 5 Science strand: human blood is grouped into different types, such as A, B, AB, and O, and understanding blood types helps ensure that a blood donation is safely matched to a recipient.',
   [('What are the main human blood types?', ['A, B, AB, and O', 'Red, blue, green, and yellow', 'Fast, slow, thick, and thin', 'This concept has no connection to science'], 0),
    ('Why does blood type matter during a blood donation?', ['It helps ensure the donated blood is safely matched to the recipient', 'Blood type has no effect on how a donation is used', 'This concept has no relevance to science', 'Every blood type can always be mixed with any other blood type with no risk'], 0),
    ('What could happen if a person receives a blood transfusion with an incompatible blood type?', ['Their immune system could react in a dangerous way', 'Nothing would happen at all', 'This concept has no connection to blood donation', 'The blood types would immediately become identical'], 0),
    ('Why might hospitals keep a supply of several different blood types on hand?', ['Different patients need blood types that match their own for a safe transfusion', 'Hospitals never need more than one blood type', 'This concept has no relevance to science', 'All patients can always safely receive any blood type'], 0),
    ('Why is blood donation considered an important way people can help their community?', ['Donated blood can be used to treat patients who need transfusions for surgery, illness, or injury', 'Blood donation has no connection to helping others', 'This concept has no relevance to science', 'Donated blood is never actually used by hospitals'], 0)]),
SS('Responsible Government — How Canada Gained Self-Rule',
   'Grade 5 Social Studies strand: responsible government means that the elected representatives, rather than an appointed governor, hold the real power to make decisions, a principle Canada gradually achieved during the 1800s.',
   [('What does responsible government mean?', ['Elected representatives, rather than an appointed governor, hold the real power to make decisions', 'A government with no elected representatives at all', 'A government controlled entirely by a foreign monarch', 'This concept has no connection to Canadian history'], 0),
    ('Roughly when did Canada gradually achieve responsible government?', ['During the 1800s', 'During the 1600s', 'During the 1960s', 'This concept has no relevance to Canadian history'], 0),
    ('Before responsible government, who held much of the real decision-making power in the colonies?', ['An appointed governor', 'The elected assembly alone', 'Ordinary citizens through public votes', 'This concept has no connection to social studies'], 0),
    ('Why might colonists have pushed for responsible government?', ['They wanted elected representatives, who were accountable to voters, to hold real decision-making power', 'They wanted an appointed governor to have even more power', 'This concept has no relevance to Canadian history', 'They had no interest in how their colony was governed'], 0),
    ('Why is responsible government considered an important step toward modern Canadian democracy?', ['It shifted real political power to representatives accountable to the people', 'It removed all elected representatives from government', 'This concept has no relevance to social studies', 'It had no effect on how Canada is governed today'], 0)]),
]),
day(183, [
L('Media Literacy: Recognizing Deepfakes and Manipulated Media',
  'Grade 5 Language strand: a deepfake is a digitally altered video or image made to look real using technology, and recognizing manipulated media helps readers and viewers think critically about what they see online.',
  [('What is a deepfake?', ['A digitally altered video or image made to look real using technology', 'A traditional printed newspaper article', 'A handwritten letter from a real person', 'This concept has no connection to media literacy'], 0),
   ('Why is it important to think critically about media that might be a deepfake?', ['Manipulated media can look convincing but may not show something that actually happened', 'Deepfakes are always obviously fake and easy to spot', 'This concept has no relevance to media literacy', 'Every video seen online is guaranteed to be real'], 0),
   ('What might be one clue that a video could be manipulated?', ['Unnatural movements or mismatched audio and video', 'A video is always considered real if it has sound', 'This concept has no connection to media literacy', 'Manipulated videos never contain any people at all'], 0),
   ('Why might checking a claim against other trusted sources help someone evaluate a suspicious video?', ['Comparing information across reliable sources can reveal whether a video is accurate', 'Checking other sources never provides any useful information', 'This concept has no relevance to media literacy', 'A single video is always more reliable than multiple trusted sources'], 0),
   ('Why is media literacy especially important as technology for creating manipulated media improves?', ['More realistic manipulated media makes careful, critical thinking increasingly necessary', 'Improved technology has no effect on how believable manipulated media appears', 'This concept has no relevance to media literacy', 'Manipulated media has become impossible to create with modern technology'], 0)]),
M('Data Management: Constructing Frequency Polygons',
  'Grade 5 Math strand: a frequency polygon is a line graph formed by plotting the midpoint of each interval in a set of grouped data and connecting the points, giving a visual picture of how the data is distributed.',
  [('What is a frequency polygon?', ['A line graph formed by plotting the midpoint of each interval in grouped data and connecting the points', 'A bar graph showing individual data values', 'A circle graph showing percentages', 'This concept has no connection to data management'], 0),
   ('What point from each interval is plotted when constructing a frequency polygon?', ['The midpoint of the interval', 'The smallest value in the interval only', 'The largest value in the interval only', 'This concept has no relevance to frequency polygons'], 0),
   ('What do the plotted points on a frequency polygon get connected with?', ['Straight lines', 'Curved dotted lines only', 'They are never connected', 'This concept has no connection to data management'], 0),
   ('Why might a frequency polygon be useful for comparing two different sets of grouped data?', ['Two frequency polygons can be drawn on the same graph to compare their shapes directly', 'Frequency polygons can never be compared to each other', 'This concept has no relevance to data management', 'Only one frequency polygon can ever exist on a single graph'], 0),
   ('Why might a frequency polygon give a clearer picture of a datas overall shape than a table of numbers alone?', ['The visual line shows trends and patterns that can be harder to see in a table', 'A frequency polygon never shows any useful information about data', 'This concept has no connection to math', 'A table of numbers always shows patterns more clearly than any graph'], 0)]),
Sc('Vaccines and How They Help the Immune System',
   'Grade 5 Science strand: a vaccine trains the immune system to recognize and fight a specific germ by introducing a safe, weakened, or inactive version of it, helping the body build protection before a real infection occurs.',
   [('What does a vaccine train the body to do?', ['Recognize and fight a specific germ', 'Grow taller more quickly', 'Digest food more efficiently', 'This concept has no connection to science'], 0),
    ('What does a vaccine typically introduce into the body?', ['A safe, weakened, or inactive version of a germ', 'A large dose of the full, active illness', 'A completely unrelated substance with no connection to any germ', 'This concept has no relevance to vaccines'], 0),
    ('When does a vaccine help build protection compared to a real infection?', ['Before a real infection occurs', 'Only after a person has already become seriously ill', 'Vaccines never build any protection', 'This concept has no connection to the immune system'], 0),
    ('Why might a vaccinated persons immune system respond more quickly to a real infection later on?', ['The immune system already learned to recognize that germ from the vaccine', 'Vaccines have no effect on how the immune system responds to germs', 'This concept has no relevance to science', 'A vaccinated persons immune system forgets the germ immediately'], 0),
    ('Why are vaccines considered an important tool in public health?', ['They can help prevent the spread of serious diseases within a community', 'Vaccines have no connection to preventing the spread of disease', 'This concept has no relevance to science', 'Vaccines always make diseases spread more quickly'], 0)]),
SS('Canadas Role in the Cold War',
   'Grade 5 Social Studies strand: during the Cold War, a long period of tension between the United States and the Soviet Union after the Second World War, Canada joined alliances such as NATO and contributed to efforts like NORAD to help defend North America.',
   [('What was the Cold War?', ['A long period of tension between the United States and the Soviet Union after the Second World War', 'A war fought entirely with weather and climate technology', 'A short battle fought only in Canada', 'This concept has no connection to social studies'], 0),
    ('Which alliance did Canada join partly in response to Cold War tensions?', ['NATO', 'The Commonwealth of Nations only', 'The World Trade Organization', 'This concept has no relevance to the Cold War'], 0),
    ('What was NORAD, which Canada contributed to during this period?', ['A joint effort with the United States to help defend North American airspace', 'A Canadian sports league', 'A Canadian trade agreement with Europe', 'This concept has no connection to Canadian history'], 0),
    ('Why might Canada have joined alliances like NATO during the Cold War?', ['To cooperate with other countries for collective defence and security', 'Canada had no interest in international defence during this period', 'This concept has no relevance to social studies', 'Alliances like NATO had no connection to the Cold War'], 0),
    ('Why is understanding the Cold War useful for learning about twentieth-century Canadian foreign policy?', ['It shows how global tensions shaped Canadas alliances and defence decisions', 'The Cold War had no effect on Canadian foreign policy', 'This concept has no relevance to social studies', 'Canada was never involved in any international alliances during this period'], 0)]),
]),
day(184, [
L('Reading: Understanding Anthropomorphism in Stories',
  'Grade 5 Language strand: anthropomorphism is when an author gives human qualities, such as speech or emotions, to animals or objects in a story, a technique often used in fables and fantasy writing.',
  [('What is anthropomorphism?', ['Giving human qualities to animals or objects in a story', 'Describing only real historical events', 'Writing a story with no characters at all', 'This concept has no connection to reading'], 0),
   ('Which human qualities might an author give to an animal character through anthropomorphism?', ['Speech or emotions', 'The ability to photosynthesize', 'A complete absence of any personality', 'This concept has no relevance to reading'], 0),
   ('In which type of story is anthropomorphism often used?', ['Fables and fantasy writing', 'Strictly factual news reports only', 'This concept has no connection to reading', 'Anthropomorphism is never used in any type of story'], 0),
   ('Why might an author use anthropomorphism to teach a lesson in a fable?', ['Giving animals human behaviour can make a moral lesson more engaging and relatable', 'Anthropomorphism never helps convey a lesson in a story', 'This concept has no relevance to reading', 'Fables never include any animal characters'], 0),
   ('Why might readers of all ages find anthropomorphic characters, like a talking fox, appealing?', ['Human-like animal characters can feel familiar while still being imaginative and fun', 'Talking animal characters are always confusing and unappealing to readers', 'This concept has no relevance to reading', 'Anthropomorphism removes all imagination from a story'], 0)]),
M('Financial Literacy: Understanding Insurance Basics',
  'Grade 5 Math strand: insurance is a way of managing financial risk, where a person pays a regular amount called a premium so that the insurance company helps cover the cost if an unexpected loss or accident occurs.',
  [('What is insurance?', ['A way of managing financial risk by paying a regular premium for coverage against unexpected loss', 'A type of tax collected by the government', 'A free service with no cost involved', 'This concept has no connection to financial literacy'], 0),
   ('What is the regular payment for insurance called?', ['A premium', 'A dividend', 'A deduction', 'A discount'], 0),
   ('What might an insurance company help cover if an unexpected accident occurs?', ['Some or all of the resulting cost', 'None of the cost under any circumstance', 'Only costs related to groceries', 'This concept has no relevance to insurance'], 0),
   ('Why might a family choose to pay for home insurance even if they never experience an accident?', ['It helps protect them financially from the risk of a costly, unexpected event', 'Insurance always costs more than any possible loss it could cover', 'This concept has no relevance to financial literacy', 'Home insurance has no connection to managing financial risk'], 0),
   ('Why is understanding insurance considered a useful financial literacy skill?', ['It helps people understand how to plan for and manage unexpected financial risks', 'Insurance has no connection to financial planning', 'This concept has no relevance to math', 'Unexpected costs never need to be planned for in any way'], 0)]),
Sc('Nuclear Fusion — How the Sun Produces Energy',
   'Grade 5 Science strand: nuclear fusion occurs when two atomic nuclei combine under extreme heat and pressure to form a heavier nucleus, releasing enormous amounts of energy, which is the process that powers the Sun.',
   [('What happens during nuclear fusion?', ['Two atomic nuclei combine under extreme heat and pressure to form a heavier nucleus', 'A single nucleus splits apart into two smaller pieces', 'Two liquids are physically mixed together', 'This concept has no connection to science'], 0),
    ('What does nuclear fusion release as it combines nuclei?', ['Enormous amounts of energy', 'A small amount of water', 'Cold air only', 'This concept has no relevance to nuclear fusion'], 0),
    ('What process powers the Sun?', ['Nuclear fusion', 'Burning of fossil fuels', 'Reflection of light from nearby stars', 'This concept has no connection to the Sun'], 0),
    ('Why is extreme heat and pressure needed for nuclear fusion to occur?', ['These conditions force atomic nuclei close enough together to combine', 'Heat and pressure have no effect on whether fusion occurs', 'This concept has no relevance to science', 'Nuclear fusion always happens at very low temperatures'], 0),
    ('Why might scientists be interested in developing nuclear fusion as a future energy source on Earth?', ['It could potentially provide a large amount of energy with very low emissions', 'Nuclear fusion has no connection to producing energy', 'This concept has no relevance to science', 'Fusion energy has already completely replaced every other energy source on Earth'], 0)]),
SS('The Royal Canadian Mint and How Coins Are Made',
   'Grade 5 Social Studies strand: the Royal Canadian Mint is the Crown corporation responsible for producing Canadas circulating coins, using metal blanks that are stamped with official designs before being distributed for use.',
   [('What is the Royal Canadian Mint responsible for?', ['Producing Canadas circulating coins', 'Printing Canadas paper currency', 'Setting interest rates for Canadian banks', 'This concept has no connection to social studies'], 0),
    ('What type of organization is the Royal Canadian Mint?', ['A Crown corporation', 'A private international bank', 'A branch of a foreign government', 'This concept has no relevance to Canadian currency'], 0),
    ('What are metal blanks stamped with during the coin-making process?', ['Official designs', 'Random unrelated patterns', 'Nothing at all', 'This concept has no connection to the Royal Canadian Mint'], 0),
    ('Why might the design stamped on a Canadian coin be considered important?', ['It can represent national symbols, history, or important events', 'Coin designs have no meaning or purpose at all', 'This concept has no relevance to social studies', 'Every Canadian coin has always used the exact same single design forever'], 0),
    ('Why does Canada rely on a dedicated Crown corporation to produce its coins?', ['A dedicated organization can ensure coins are produced consistently, securely, and to an official standard', 'Coin production has no connection to how a countrys currency works', 'This concept has no relevance to social studies', 'Coins in Canada are never produced by any official organization'], 0)]),
]),
day(185, [
L('Grammar: Using Parentheses for Extra Information',
  'Grade 5 Language strand: parentheses are punctuation marks used to add extra information, an explanation, or a side comment to a sentence without changing its main meaning.',
  [('What are parentheses used for in a sentence?', ['Adding extra information, an explanation, or a side comment', 'Ending every sentence in a paragraph', 'Replacing a subject in a sentence', 'This concept has no connection to grammar'], 0),
   ('What happens to the main meaning of a sentence when parentheses are used correctly?', ['It stays the same, since the parentheses add extra, non-essential information', 'It always changes completely', 'This concept has no relevance to grammar', 'The sentence loses its subject entirely'], 0),
   ('Which of these sentences correctly uses parentheses?', ['My dog Max (who is three years old) loves to run.', 'My dog Max who is (three) years old loves to run.', 'My dog (Max who is three years old loves to run.', 'My dog Max who is three years old loves to run (.)'], 0),
   ('Why might a writer choose parentheses instead of starting a brand-new sentence for extra information?', ['Parentheses let the writer add a brief detail without interrupting the flow of the main sentence', 'Parentheses always make a sentence more confusing than starting a new one', 'This concept has no connection to grammar', 'Extra information can never be added to an existing sentence'], 0),
   ('Why might a reader be able to skip the text inside parentheses and still understand the main sentence?', ['Information in parentheses is usually additional detail rather than essential meaning', 'Text inside parentheses is always the most important part of a sentence', 'This concept has no relevance to grammar', 'A sentence can never be understood if any part of it is skipped'], 0)]),
M('Number Sense: Multiplying by 11 — Mental Math Tricks',
  'Grade 5 Math strand: multiplying a two-digit number by 11 can often be done mentally by adding the two digits together and placing the sum between them, a shortcut that builds flexible number sense.',
  [('What mental math shortcut can help with multiplying a two-digit number by 11?', ['Adding the two digits together and placing the sum between them', 'Always doubling the number twice', 'Subtracting the digits from each other', 'This concept has no connection to number sense'], 0),
   ('Using the shortcut, what is 23 multiplied by 11?', ['253', '233', '243', '223'], 0),
   ('Using the shortcut, what is 42 multiplied by 11?', ['462', '442', '452', '424'], 0),
   ('Why might this shortcut for multiplying by 11 need an extra adjustment when the two digits add up to 10 or more?', ['The sum would not fit in a single digit, so an extra ten needs to be carried over', 'The shortcut always works exactly the same way with no exceptions', 'This concept has no relevance to number sense', 'Multiplying by 11 never produces a sum greater than 9'], 0),
   ('Why can practising mental math shortcuts like this one be useful in everyday life?', ['It can help with quick calculations without needing a calculator', 'Mental math shortcuts never provide any real benefit', 'This concept has no relevance to math', 'Calculators are always required for any multiplication problem'], 0)]),
Sc('The Process of Fossilization — How Fossils Form',
   'Grade 5 Science strand: fossilization is the slow process by which the remains or traces of an organism are preserved in rock over thousands or millions of years, usually after being quickly buried by sediment.',
   [('What is fossilization?', ['The slow process by which the remains or traces of an organism are preserved in rock', 'The instant transformation of a living animal into a rock', 'A process that only happens to plants, never animals', 'This concept has no connection to science'], 0),
    ('What often needs to happen quickly for an organism to begin fossilizing?', ['It needs to be buried by sediment', 'It needs to be left completely exposed to the open air', 'It needs to be placed directly in water with no burial at all', 'This concept has no relevance to fossilization'], 0),
    ('About how long can the fossilization process take?', ['Thousands or millions of years', 'A single day', 'A few minutes', 'This concept has no connection to fossilization'], 0),
    ('Why might scientists study fossils to learn about Earths history?', ['Fossils can reveal information about organisms and environments from long ago', 'Fossils never provide any information about the past', 'This concept has no relevance to science', 'Fossils are always exactly the same age as the rock surrounding them'], 0),
    ('Why are fossils considered rare, even though many organisms have lived on Earth?', ['Very specific conditions, like quick burial, are usually needed for fossilization to occur', 'Every organism that has ever lived automatically becomes a fossil', 'This concept has no relevance to science', 'Fossilization happens to every living thing within a few hours of death'], 0)]),
SS('Understanding GST, PST, and HST in Canada',
   'Grade 5 Social Studies strand: Canadians pay different sales taxes depending on their province, including the federal Goods and Services Tax, provincial sales taxes, and the Harmonized Sales Tax, which combines federal and provincial tax into one rate.',
   [('What does GST stand for?', ['Goods and Services Tax', 'General Spending Tax', 'Government Savings Trust', 'This concept has no connection to social studies'], 0),
    ('What does the Harmonized Sales Tax, or HST, do?', ['Combines the federal and provincial tax into one rate', 'Removes all sales tax entirely', 'Applies only to international purchases', 'This concept has no relevance to sales tax'], 0),
    ('What is a provincial sales tax, sometimes called PST, collected by?', ['A provincial government', 'A foreign government only', 'A private company with no government connection', 'This concept has no connection to Canadian taxes'], 0),
    ('Why might sales tax amounts differ depending on which province a purchase is made in?', ['Provinces can set their own provincial tax rates, which combine differently with federal tax', 'Sales tax is always exactly the same amount in every province', 'This concept has no relevance to social studies', 'Provinces have no role in setting any taxes at all'], 0),
    ('Why is understanding sales tax useful when planning a purchase?', ['It helps a person estimate the total cost, including tax, before buying something', 'Sales tax never affects the total cost of a purchase', 'This concept has no relevance to social studies', 'Tax is never added to the price of an item in Canada'], 0)]),
]),
day(186, [
L('Writing: Writing a Radio Play Script',
  'Grade 5 Language strand: a radio play script is written to be performed using only sound, so writers rely on dialogue, sound effects, and narration to help listeners picture the setting and action without any visuals.',
  [('What is a radio play script written to be performed using?', ['Only sound', 'Only silent visuals with no sound', 'A combination of sound and video with no dialogue', 'This concept has no connection to writing'], 0),
   ('What might a radio play script use to help listeners picture a thunderstorm?', ['Sound effects, such as thunder and rain', 'A detailed painted backdrop', 'This concept has no relevance to writing', 'Radio plays never include any sound effects'], 0),
   ('Why is dialogue especially important in a radio play script?', ['Listeners rely on spoken words, since they cannot see the characters', 'Dialogue is never included in a radio play script', 'This concept has no connection to writing', 'Listeners can already see the characters, so dialogue is unnecessary'], 0),
   ('Why might a narrator be used in a radio play to describe a setting?', ['A narrator can describe details that listeners would otherwise only get from seeing them', 'A narrator is never included in a radio play', 'This concept has no relevance to writing', 'Settings never need to be described in a radio play'], 0),
   ('Why does writing a radio play script require different skills than writing a script for a television show?', ['A radio script must convey every visual detail through sound and words alone', 'Radio scripts and television scripts always rely on identical techniques', 'This concept has no relevance to writing', 'Television scripts never include any dialogue at all'], 0)]),
M('Geometry: Sum of Exterior Angles of a Polygon',
  'Grade 5 Math strand: the exterior angles of any convex polygon, one at each vertex, always add up to 360 degrees, regardless of how many sides the polygon has.',
  [('What do the exterior angles of any convex polygon always add up to?', ['360 degrees', '180 degrees', '90 degrees', '540 degrees'], 0),
   ('Does the sum of exterior angles change depending on the number of sides a polygon has?', ['No, it always stays at 360 degrees', 'Yes, it always increases with more sides', 'Yes, it always decreases with more sides', 'This concept has no relevance to geometry'], 0),
   ('What is the measure of each exterior angle of a regular polygon with 4 equal sides?', ['90 degrees', '180 degrees', '45 degrees', '360 degrees'], 0),
   ('Why might knowing that exterior angles always sum to 360 degrees be useful when finding the measure of one angle in a regular polygon?', ['Dividing 360 by the number of sides gives the measure of each equal exterior angle', 'This total has no connection to finding individual exterior angles', 'This concept has no relevance to geometry', 'Exterior angles are never useful when studying regular polygons'], 0),
   ('Why is the constant sum of exterior angles considered a useful geometric pattern?', ['It applies to every convex polygon, no matter how many sides it has', 'It only applies to a single specific polygon and no others', 'This concept has no relevance to math', 'The sum of exterior angles is never the same for any two polygons'], 0)]),
Sc('The Physics of Rainbows — How Light Disperses into Colour',
   'Grade 5 Science strand: a rainbow forms when sunlight enters raindrops and is refracted, reflected, and dispersed into its different wavelengths, spreading white light into the familiar band of colours.',
   [('What happens to sunlight as it enters a raindrop to form a rainbow?', ['It is refracted, reflected, and dispersed into its different wavelengths', 'It is completely absorbed with no light escaping', 'It instantly turns into a solid', 'This concept has no connection to science'], 0),
    ('What does dispersing white light into different wavelengths produce?', ['A band of separate colours', 'A single, unchanged colour', 'Complete darkness', 'This concept has no relevance to rainbows'], 0),
    ('Why is a rainbow more likely to appear after rain when the Sun comes out?', ['Raindrops in the air can refract and disperse the sunlight', 'Rain always blocks every bit of sunlight completely', 'This concept has no connection to science', 'Rainbows only ever appear at night'], 0),
    ('Why does a rainbow always appear as a curved band rather than a straight line?', ['Light bends at a specific angle within each raindrop, creating a curved pattern of colour', 'Rainbows are always perfectly straight lines', 'This concept has no relevance to science', 'Raindrops never bend light in any particular pattern'], 0),
    ('Why might understanding refraction, from earlier lessons on lenses, help explain how a rainbow forms?', ['The same bending of light that happens in a lens also happens as light passes through a raindrop', 'Refraction has no connection to how a rainbow forms', 'This concept has no relevance to science', 'Rainbows form through a process completely unrelated to light bending'], 0)]),
SS('Canada as a Founding Member of the United Nations',
   'Grade 5 Social Studies strand: Canada was one of the original member countries when the United Nations was formed in 1945, and it has continued to support the organizations goals of international peace, cooperation, and human rights.',
   [('When was Canada one of the original member countries of the United Nations?', ['1945', '1867', '1982', '1960'], 0),
    ('What is one goal of the United Nations that Canada has continued to support?', ['International peace, cooperation, and human rights', 'Ending all international trade between countries', 'Removing every countrys individual government', 'This concept has no connection to social studies'], 0),
    ('What kind of organization is the United Nations?', ['An international organization made up of member countries', 'A single countrys national government', 'A private company that sells goods internationally', 'This concept has no relevance to the United Nations'], 0),
    ('Why might a country choose to become a founding member of an organization like the United Nations?', ['To help shape international cooperation on shared global challenges from the very beginning', 'Founding membership has no effect on international cooperation', 'This concept has no relevance to social studies', 'Countries never choose to join international organizations'], 0),
    ('Why might Canadas long membership in the United Nations be considered part of its global identity?', ['It reflects a long-standing commitment to international cooperation and human rights', 'Membership in the United Nations has no connection to a countrys global identity', 'This concept has no relevance to social studies', 'Canada has never been involved with the United Nations in any way'], 0)]),
]),
day(187, [
L('Language Review: Capstone — Poetry, Vocabulary, Media Literacy, and Reading',
  'Grade 5 Language strand review, and the capstone lesson of the full 187-day program: students revisit writing a limerick, neologisms, recognizing deepfakes and manipulated media, anthropomorphism, and using parentheses.',
  [('How many lines does a limerick have?', ['5', '3', '4', '7'], 0),
   ('What is a neologism?', ['A newly coined word or phrase that enters a language', 'A word borrowed directly from an ancient language', 'A word that has completely disappeared from use', 'This concept has no connection to vocabulary'], 0),
   ('What is a deepfake?', ['A digitally altered video or image made to look real using technology', 'A traditional printed newspaper article', 'A handwritten letter from a real person', 'This concept has no connection to media literacy'], 0),
   ('What is anthropomorphism?', ['Giving human qualities to animals or objects in a story', 'Describing only real historical events', 'Writing a story with no characters at all', 'This concept has no connection to reading'], 0),
   ('What are parentheses used for in a sentence?', ['Adding extra information, an explanation, or a side comment', 'Ending every sentence in a paragraph', 'Replacing a subject in a sentence', 'This concept has no connection to grammar'], 0)]),
M('Math Review: Capstone — Number Sense, Geometry, Data Management, and Financial Literacy',
  'Grade 5 Math strand review, and the capstone lesson of the full 187-day program: students revisit triangular numbers, classifying prisms by their bases, constructing frequency polygons, understanding insurance basics, and multiplying by 11.',
  [('What is a triangular number?', ['A number that can be arranged into an equilateral triangle of dots', 'A number that is always divisible by 3', 'A number with exactly three digits', 'A number that can never be added to another number'], 0),
   ('How is a prism named?', ['According to the shape of its base', 'According to its total number of faces only', 'According to its colour', 'This concept has no connection to geometry'], 0),
   ('What is a frequency polygon?', ['A line graph formed by plotting the midpoint of each interval in grouped data and connecting the points', 'A bar graph showing individual data values', 'A circle graph showing percentages', 'This concept has no connection to data management'], 0),
   ('What is insurance?', ['A way of managing financial risk by paying a regular premium for coverage against unexpected loss', 'A type of tax collected by the government', 'A free service with no cost involved', 'This concept has no connection to financial literacy'], 0),
   ('What mental math shortcut can help with multiplying a two-digit number by 11?', ['Adding the two digits together and placing the sum between them', 'Always doubling the number twice', 'Subtracting the digits from each other', 'This concept has no connection to number sense'], 0)]),
Sc('Science Review: Capstone — Diffusion, Human Biology, and Earth Science',
   'Grade 5 Science strand review, and the capstone lesson of the full 187-day program: students revisit diffusion, blood types and blood donation, vaccines, nuclear fusion, and the process of fossilization.',
   [('What is diffusion?', ['The movement of particles from an area of higher concentration to lower concentration', 'The freezing of a liquid into a solid', 'The bending of light through a lens', 'This concept has no connection to science'], 0),
    ('What are the main human blood types?', ['A, B, AB, and O', 'Red, blue, green, and yellow', 'Fast, slow, thick, and thin', 'This concept has no connection to science'], 0),
    ('What does a vaccine train the body to do?', ['Recognize and fight a specific germ', 'Grow taller more quickly', 'Digest food more efficiently', 'This concept has no connection to science'], 0),
    ('What happens during nuclear fusion?', ['Two atomic nuclei combine under extreme heat and pressure to form a heavier nucleus', 'A single nucleus splits apart into two smaller pieces', 'Two liquids are physically mixed together', 'This concept has no connection to science'], 0),
    ('What is fossilization?', ['The slow process by which the remains or traces of an organism are preserved in rock', 'The instant transformation of a living animal into a rock', 'A process that only happens to plants, never animals', 'This concept has no connection to science'], 0)]),
SS('SocialStudies Review: Capstone — Rights, Government History, and Global Citizenship',
   'Grade 5 Social Studies strand review, and the capstone lesson of the full 187-day program: students revisit the Canadian Bill of Rights of 1960, responsible government, Canadas role in the Cold War, the Royal Canadian Mint, and GST, PST, and HST.',
   [('What was the Canadian Bill of Rights?', ['An early federal law protecting basic rights and freedoms', 'A law that created the Supreme Court of Canada', 'A treaty between Canada and another country', 'This concept has no connection to Canadian history'], 0),
    ('What does responsible government mean?', ['Elected representatives, rather than an appointed governor, hold the real power to make decisions', 'A government with no elected representatives at all', 'A government controlled entirely by a foreign monarch', 'This concept has no connection to Canadian history'], 0),
    ('What was the Cold War?', ['A long period of tension between the United States and the Soviet Union after the Second World War', 'A war fought entirely with weather and climate technology', 'A short battle fought only in Canada', 'This concept has no connection to social studies'], 0),
    ('What is the Royal Canadian Mint responsible for?', ['Producing Canadas circulating coins', 'Printing Canadas paper currency', 'Setting interest rates for Canadian banks', 'This concept has no connection to social studies'], 0),
    ('What does GST stand for?', ['Goods and Services Tax', 'General Spending Tax', 'Government Savings Trust', 'This concept has no connection to social studies'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g5_181_187)
    append_to(5, g5_181_187)
