#!/usr/bin/env python3
"""Grade 6, Days 131-140 -- extends Grade 6 from 130 to 140 days. Modeled
exactly on gen_grade6_days121_130.py: same L/M/Sc/SS helpers over
gen_curriculum's sub()/day()/append_to(), same TVO Learn placeholder
resourceLabel/resourceUrl convention (videoUrl intentionally left unset,
filled in later by the daily curriculum-video-backfill scheduled task).

Topics chosen to avoid any overlap with the existing Grade 6 Days 1-130
topics (see data/grade6.json), which already densely cover nearly the
entire grade 6 curriculum across all four subjects. New topics: relative
pronouns and relative clauses, writing free verse poetry, eponyms, writing
a public service announcement script, correlative conjunctions, analyzing
editorial cartoons, group discussion and collaborative talk norms, the
show-dont-tell writing technique, and cliches for Language; surface area
of pyramids, multiplying and dividing mixed numbers, evaluating algebraic
expressions by substitution, vertices/edges/faces and Eulers formula,
odds in favour and against, payroll deductions and net income, comparing
numbers in scientific notation, constructing perpendicular and angle
bisectors, and converting units of area for Math; the Sun as a star,
generators, the nitrogen cycle, hurricanes and tornadoes, Earths layers,
inclined planes and wedges, separating mixtures, bioindicators, and 3D
printing for Science; and the Chinese Head Tax, the Quebec referendums,
the discovery of insulin, the Canadian Bill of Rights of 1960, the
Official Languages Act, the Battle of Vimy Ridge, the printing press, the
Great Wall of China, and the Supreme Court of Canada for Social Studies --
none of those exact ideas appear in Days 1-130. Day 140 is a review day
across all four subjects, matching the end-of-batch pattern used in every
prior 10-day batch. No embedded ASCII apostrophe or double-quote
characters are used anywhere in title/summary/question/option text --
apostrophes are dropped entirely (e.g. "Canadas" not "Canada's"),
matching the rest of Grade 6.

Usage: python3 gen_grade6_days131_140.py
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


def _rebalance_answer_positions(days, seed=20260801):
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


g6_131_140 = [
day(131, [
L('Grammar: Relative Pronouns and Relative Clauses',
  'Grade 6 Language strand: a relative clause begins with a relative pronoun such as who, whom, whose, which, or that, and adds extra information about a noun in the main sentence.',
  [('What does a relative clause do?', ['Adds extra information about a noun in the main sentence', 'Always begins a brand new sentence', 'Replaces the subject of a sentence entirely', 'Removes the need for any punctuation'], 0),
   ('Which word is commonly used as a relative pronoun?', ['Which', 'Quickly', 'Under', 'And'], 0),
   ('Which sentence contains a relative clause?', ['The book that I borrowed was excellent.', 'I borrowed a book yesterday.', 'The library was very quiet.', 'I enjoy reading many books.'], 0),
   ('Which relative pronoun is typically used to show possession?', ['Whose', 'Who', 'That', 'Which'], 0),
   ('Why might a writer use a relative clause instead of writing two separate short sentences?', ['It combines related ideas smoothly into one clear sentence', 'It always makes writing more confusing', 'Relative clauses are never grammatically correct', 'It removes all detail from a sentence'], 0)]),
M('Geometry: Surface Area of Pyramids',
  'Grade 6 Math strand: the surface area of a pyramid is the sum of the area of its base and the areas of its triangular faces, found by adding together all the flat surfaces that cover the shape.',
  [('What is surface area?', ['The total area of all the flat surfaces that cover a three-dimensional shape', 'The distance around the base of a shape only', 'The space enclosed inside a three-dimensional shape', 'A measurement used only for two-dimensional shapes'], 0),
   ('What two parts make up the surface area of a pyramid?', ['The base and the triangular faces', 'Only the base, with no other faces', 'Only the apex of the pyramid', 'The volume and the height'], 0),
   ('How many triangular faces does a square-based pyramid have?', ['Four', 'Three', 'Five', 'Six'], 0),
   ('Why might you calculate the area of each face separately before finding the total surface area?', ['Each face may have a different shape or size that must be measured individually', 'All faces of a pyramid are always identical rectangles', 'Surface area never requires measuring individual faces', 'Pyramids do not have separate faces to measure'], 0),
   ('What type of unit is surface area always measured in?', ['Square units', 'Linear units', 'Cubic units', 'No units are needed'], 0)]),
Sc('The Sun — Our Closest Star and Source of Energy',
   'Grade 6 Science strand: the Sun is a massive ball of hot, glowing gas at the centre of our solar system, and its energy drives Earths weather, climate, and nearly all life through the process of photosynthesis.',
   [('What is the Sun?', ['A massive ball of hot, glowing gas at the centre of our solar system', 'A large rocky planet with no light of its own', 'A frozen moon orbiting Earth', 'An artificial satellite launched by humans'], 0),
    ('What process do plants use to convert the Suns energy into food?', ['Photosynthesis', 'Respiration', 'Evaporation', 'Condensation'], 0),
    ('What does the Suns energy help drive on Earth?', ['Weather and climate patterns', 'The rotation of the Moon only', 'Ocean tides with no other effect', 'Earthquakes and volcanic eruptions'], 0),
    ('Why is the Sun classified as a star rather than a planet?', ['It produces its own light and heat through nuclear fusion', 'It reflects light from other stars', 'It orbits around Earth', 'It has no connection to light or heat production'], 0),
    ('Why is the Sun considered essential to nearly all life on Earth?', ['Nearly all food chains ultimately depend on energy that begins with the Sun', 'Living things do not require any source of energy', 'The Sun has no connection to food chains on Earth', 'Only ocean life depends on energy from the Sun'], 0)]),
SS('Social Studies: The Chinese Head Tax — A Chapter in Canadian Immigration History',
   'Grade 6 Social Studies strand: the Chinese Head Tax was a fee imposed on Chinese immigrants entering Canada beginning in 1885, a discriminatory policy later followed by an outright exclusion act, both now formally recognized as historical injustices.',
   [('What was the Chinese Head Tax?', ['A fee imposed on Chinese immigrants entering Canada', 'A tax paid by all Canadian citizens equally', 'A reward given to new immigrants', 'A type of import tax on goods from China'], 0),
    ('In what year did the Chinese Head Tax begin?', ['1885', '1867', '1929', '1945'], 0),
    ('What law later replaced the head tax with an outright ban on Chinese immigration?', ['The Chinese Exclusion Act', 'The Official Languages Act', 'The Immigration Points Act', 'The Persons Case'], 0),
    ('Why is the Chinese Head Tax now viewed as a historical injustice?', ['It unfairly targeted a specific group of immigrants based on their origin', 'It applied equally and fairly to every immigrant group', 'It had no lasting impact on Chinese Canadian communities', 'It was never actually enforced by the government'], 0),
    ('Why might a government issue a formal apology for a past policy like the head tax?', ['To acknowledge historical wrongs and support reconciliation with affected communities', 'Apologies have no role in addressing historical injustices', 'Formal apologies are only given for recent events', 'Governments never revisit past immigration policies'], 0)]),
]),
day(132, [
L('Poetry: Writing Free Verse Poetry',
  'Grade 6 Language strand: free verse poetry does not follow a fixed rhyme scheme or meter, allowing poets to focus on natural rhythm, vivid imagery, and line breaks that emphasize meaning.',
  [('What is free verse poetry?', ['Poetry that does not follow a fixed rhyme scheme or meter', 'Poetry that must always rhyme in a strict pattern', 'A five-line poem with a set rhythm', 'Poetry written only about nature'], 0),
   ('What might a free verse poet emphasize instead of rhyme?', ['Rhythm, imagery, and meaningful line breaks', 'Random letters with no structure', 'A strict syllable count in every line', 'Only punctuation at the end of lines'], 0),
   ('Which of these is true about free verse poetry?', ['Its lines can be irregular in length', 'Every line must be exactly the same length', 'It must always follow an AABB rhyme scheme', 'It cannot use imagery of any kind'], 0),
   ('Why might a poet choose free verse over a strict form like a limerick?', ['It gives more freedom to shape the poems structure around its meaning', 'Free verse has far stricter rules than a limerick', 'Free verse cannot express any emotion', 'A limerick allows more creative freedom than free verse'], 0),
   ('Where a poet chooses to break a line in free verse can affect what?', ['The poems rhythm and emphasis', 'Nothing about how the poem is read', 'Only the poems title', 'The poems required rhyme scheme'], 0)]),
M('Number Sense: Multiplying and Dividing Mixed Numbers',
  'Grade 6 Math strand: multiplying and dividing mixed numbers requires first converting each mixed number into an improper fraction, then multiplying or dividing as with any fraction.',
  [('What must be done before multiplying two mixed numbers?', ['Convert each mixed number into an improper fraction', 'Round each mixed number to the nearest whole number', 'Add the whole number parts together first', 'Ignore the fractional parts entirely'], 0),
   ('What is 1 1/2 written as an improper fraction?', ['3/2', '1/2', '2/1', '3/1'], 0),
   ('When dividing fractions, what operation replaces the division?', ['Multiplying by the reciprocal of the second fraction', 'Adding the two fractions together', 'Subtracting the numerators only', 'Multiplying only the denominators'], 0),
   ('What is 1 1/2 multiplied by 2?', ['3', '2', '4', '1'], 0),
   ('Why is converting to an improper fraction helpful when multiplying mixed numbers?', ['It makes the multiplication process consistent and easier to complete accurately', 'It removes the need to multiply at all', 'Improper fractions cannot be multiplied together', 'It changes the value of the original number'], 0)]),
Sc('Generators — How Motion Creates Electricity',
   'Grade 6 Science strand: a generator converts mechanical motion into electrical energy by rotating a coil of wire within a magnetic field, a process used in many power plants to supply electricity.',
   [('What does a generator convert into electrical energy?', ['Mechanical motion', 'Sunlight only', 'Chemical energy stored in a battery', 'Sound waves'], 0),
    ('What happens when a coil of wire rotates within a magnetic field?', ['An electric current is produced', 'The magnetic field disappears completely', 'The wire coil stops moving', 'Heat is produced with no electricity'], 0),
    ('Which of these commonly uses a generator to produce electricity?', ['A power plant', 'A flashlight battery', 'A solar panel', 'A wooden ramp'], 0),
    ('What might provide the motion needed to turn a generator in a hydroelectric dam?', ['Flowing water', 'Sunlight', 'Wind stored in a container', 'Chemical reactions in soil'], 0),
    ('Why are generators important for supplying electricity to homes and cities?', ['They convert other forms of energy into the electrical energy that powers devices', 'They store electricity but never produce it', 'Generators have no connection to how electricity is supplied', 'Homes and cities do not rely on generators for electricity'], 0)]),
SS('Social Studies: The Quebec Referendums and Canadian National Unity',
   'Grade 6 Social Studies strand: Quebec held referendums in 1980 and 1995 asking voters whether the province should pursue sovereignty, and in both cases voters chose to remain part of Canada, shaping ongoing conversations about national unity.',
   [('What question did the Quebec referendums ask voters?', ['Whether the province should pursue sovereignty', 'Whether Canada should change its national anthem', 'Whether a new province should be created', 'Whether Quebec should build a new highway'], 0),
    ('In what years were the Quebec referendums held?', ['1980 and 1995', '1867 and 1929', '1945 and 1970', '1917 and 1960'], 0),
    ('What was the outcome of both Quebec referendums?', ['Voters chose to remain part of Canada', 'Voters chose to become fully independent', 'The referendums were cancelled before any voting', 'The results were never announced'], 0),
    ('Why are the Quebec referendums considered significant in Canadian history?', ['They reflect ongoing questions about identity, language, and national unity', 'They had no effect on how Canadians think about national unity', 'They only concerned issues unrelated to Quebec', 'They were held without any public attention'], 0),
    ('Why might a province hold a referendum on a major constitutional question like sovereignty?', ['To let citizens directly decide on an issue that affects their political future', 'Referendums are never used for major political questions', 'Only the federal government can decide such questions', 'Referendums remove the need for any public input'], 0)]),
]),
day(133, [
L('Vocabulary: Eponyms — Words Named After People',
  'Grade 6 Language strand: an eponym is a word that comes from the name of a real or fictional person, such as sandwich from the Earl of Sandwich, showing how names can become everyday vocabulary.',
  [('What is an eponym?', ['A word that comes from the name of a person', 'A word formed by combining two shorter words', 'A word borrowed directly from another language', 'A word with the exact opposite meaning of another word'], 0),
   ('Which word is an eponym named after the Earl of Sandwich?', ['Sandwich', 'Brunch', 'Smog', 'Motel'], 0),
   ('Eponyms often develop when what happens?', ['A person becomes closely associated with an invention or idea', 'A word is translated directly from another language', 'Two unrelated words are combined at random', 'A word is shortened for convenience'], 0),
   ('Why might learning about eponyms help build vocabulary?', ['It reveals interesting word history that helps in remembering meaning', 'Eponyms have no connection to word meaning', 'Eponyms are never used in everyday English', 'Learning eponyms replaces the need to learn any other words'], 0),
   ('Which describes how an eponym differs from a portmanteau?', ['An eponym comes from a persons name, while a portmanteau blends two words', 'An eponym and a portmanteau are exactly the same thing', 'A portmanteau always comes from a persons name', 'An eponym is always a blend of two shorter words'], 0)]),
M('Algebra: Evaluating Algebraic Expressions by Substitution',
  'Grade 6 Math strand: evaluating an algebraic expression by substitution means replacing each variable with a given number and then following the order of operations to find the value.',
  [('What does it mean to evaluate an algebraic expression by substitution?', ['Replacing each variable with a given number and calculating the value', 'Rewriting an expression with no numbers at all', 'Removing all variables from an expression', 'Guessing the value of an expression without calculating'], 0),
   ('What is the value of 3x + 2 when x = 4?', ['14', '12', '9', '20'], 0),
   ('What is the value of 2y - 5 when y = 6?', ['7', '6', '12', '1'], 0),
   ('Which step should be followed after substituting numbers into an expression?', ['Follow the order of operations to simplify', 'Immediately ignore any exponents present', 'Add the variable back into the expression', 'Skip all multiplication and division steps'], 0),
   ('Why is substitution a useful algebra skill?', ['It allows an expression to be evaluated for specific real-world values', 'It removes the need to ever use variables', 'Substitution only works with whole numbers', 'It has no real-world application'], 0)]),
Sc('The Nitrogen Cycle and Its Role in Ecosystems',
   'Grade 6 Science strand: the nitrogen cycle describes how nitrogen moves between the atmosphere, soil, and living things, with certain bacteria converting nitrogen gas into forms that plants can use to grow.',
   [('What does the nitrogen cycle describe?', ['How nitrogen moves between the atmosphere, soil, and living things', 'How water evaporates and condenses in the atmosphere', 'How rocks are broken down over time', 'How carbon moves through fossil fuels only'], 0),
    ('What role do certain bacteria play in the nitrogen cycle?', ['Converting nitrogen gas into forms plants can absorb and use', 'Removing all nitrogen permanently from an ecosystem', 'Producing oxygen for the atmosphere', 'Breaking down rocks into soil'], 0),
    ('Where is most of the nitrogen on Earth found?', ['In the atmosphere as a gas', 'Deep underground in solid rock', 'Only inside living plants', 'Only in ocean water'], 0),
    ('Why do plants need nitrogen?', ['To grow and produce proteins', 'To absorb sunlight more effectively', 'Plants have no need for nitrogen at all', 'To produce oxygen exclusively'], 0),
    ('Why is the nitrogen cycle important to nearly all life on Earth?', ['Nitrogen is a necessary building block for proteins in living organisms', 'Nitrogen has no role in supporting living organisms', 'Only bacteria require nitrogen to survive', 'The nitrogen cycle only affects the atmosphere'], 0)]),
SS('Social Studies: Banting and Best — The Discovery of Insulin in Canada',
   'Grade 6 Social Studies strand: Frederick Banting and Charles Best discovered insulin in 1921 at a Canadian university, a breakthrough that transformed diabetes from a fatal condition into a manageable one and remains one of Canadas most significant medical achievements.',
   [('What did Banting and Best discover in 1921?', ['Insulin', 'Penicillin', 'The vaccine for polio', 'X-ray imaging'], 0),
    ('Where did Banting and Best make their discovery?', ['At a Canadian university', 'On a Canadian naval ship', 'At an American hospital', 'In a European laboratory'], 0),
    ('How did the discovery of insulin change the treatment of diabetes?', ['It transformed diabetes from a fatal condition into a manageable one', 'It had no effect on how diabetes was treated', 'It made diabetes impossible to diagnose', 'It eliminated the need for any medical treatment at all'], 0),
    ('Why is the discovery of insulin considered one of Canadas most significant achievements?', ['It has saved countless lives worldwide and represents major Canadian scientific innovation', 'It only affected a small number of people in one city', 'It has no lasting impact on medicine today', 'It was discovered outside of Canada'], 0),
    ('Why might international recognition, such as a Nobel Prize, be given for a discovery like insulin?', ['It represents a breakthrough with a major positive impact on human health', 'International awards are never given for medical discoveries', 'The discovery had no benefit to human health', 'Nobel Prizes are only given for literature and peace'], 0)]),
]),
day(134, [
L('Writing: Writing a Public Service Announcement (PSA) Script',
  'Grade 6 Language strand: a public service announcement, or PSA, is a short script written to inform or persuade an audience about an important issue, using clear language and a strong call to action.',
  [('What is the purpose of a PSA?', ['To inform or persuade an audience about an important issue', 'To advertise a product for profit', 'To tell a long fictional story', 'To report the days sports scores'], 0),
   ('What should a strong PSA include near the end?', ['A clear call to action', 'A list of unrelated facts', 'An unrelated joke', 'A summary of a movie plot'], 0),
   ('Why do PSAs usually use short, clear sentences?', ['So the message is easy to understand quickly', 'Short sentences make a message harder to understand', 'PSAs are always read silently, never aloud', 'Clarity is not important in a PSA'], 0),
   ('Which topic would be most appropriate for a PSA?', ['Encouraging recycling in the community', 'A made-up adventure story', 'A private conversation between friends', 'A detailed movie review'], 0),
   ('Why might a PSA use a memorable slogan?', ['It helps the audience remember and act on the message', 'Slogans always confuse the intended audience', 'PSAs are not meant to be remembered', 'A slogan removes the need for any other content'], 0)]),
M('Geometry: Vertices, Edges, and Faces of 3D Shapes (Eulers Formula)',
  'Grade 6 Math strand: every three-dimensional shape has vertices, edges, and faces, and for many solids these three counts are related by Eulers formula, which states that vertices plus faces equals edges plus two.',
  [('What is a vertex on a 3D shape?', ['A corner point where edges meet', 'A flat surface of the shape', 'A line segment connecting two faces', 'The centre point inside a shape'], 0),
   ('What is an edge on a 3D shape?', ['A line segment where two faces meet', 'A single point on a shape', 'The flat surface of a shape', 'The space enclosed by a shape'], 0),
   ('How many faces does a cube have?', ['Six', 'Four', 'Eight', 'Twelve'], 0),
   ('According to Eulers formula, what does vertices plus faces equal?', ['Edges plus two', 'Edges minus two', 'Edges times two', 'Edges divided by two'], 0),
   ('How many vertices does a rectangular prism have?', ['Eight', 'Six', 'Ten', 'Four'], 0)]),
Sc('Hurricanes and Tornadoes — Extreme Weather Events',
   'Grade 6 Science strand: hurricanes are large rotating storms that form over warm ocean water, while tornadoes are fast, narrow rotating columns of air that form over land, and both can cause significant destruction.',
   [('Where do hurricanes typically form?', ['Over warm ocean water', 'Over frozen tundra', 'Deep underground', 'Only over large cities'], 0),
    ('Where do tornadoes typically form?', ['Over land', 'Only over open ocean', 'Inside caves', 'Only at the North Pole'], 0),
    ('What is a key difference between hurricanes and tornadoes?', ['Hurricanes are much larger storms, while tornadoes are narrower and more localized', 'Tornadoes are always larger than hurricanes', 'Hurricanes and tornadoes are exactly the same size', 'Hurricanes only occur in winter and tornadoes only in summer'], 0),
    ('What is one danger commonly associated with hurricanes?', ['Storm surge and flooding', 'A sudden drop in air temperature only', 'Complete lack of wind', 'An increase in air pressure with no other effects'], 0),
    ('Why do meteorologists track these extreme weather events closely?', ['To warn communities and reduce the risk to lives and property', 'These events have no effect on communities', 'Extreme weather events cannot be tracked or predicted', 'Tracking storms has no practical purpose'], 0)]),
SS('Social Studies: The Canadian Bill of Rights of 1960',
   'Grade 6 Social Studies strand: the Canadian Bill of Rights, passed in 1960, was an early federal law protecting rights such as equality and freedom of speech, later expanded upon by the more powerful Canadian Charter of Rights and Freedoms in 1982.',
   [('In what year was the Canadian Bill of Rights passed?', ['1960', '1867', '1929', '1982'], 0),
    ('What did the Canadian Bill of Rights aim to protect?', ['Rights such as equality and freedom of speech', 'Only the rights of government officials', 'Property boundaries between provinces', 'Trade agreements with other countries'], 0),
    ('What later document expanded upon the protections in the Bill of Rights?', ['The Canadian Charter of Rights and Freedoms', 'The Official Languages Act', 'The Immigration Points System', 'The Confederation agreement'], 0),
    ('Why is the Bill of Rights considered less powerful than the later Charter?', ['It was a federal law rather than part of the constitution, giving it a more limited legal reach', 'It protected far more rights than the Charter ever did', 'The Bill of Rights is still the primary rights document today', 'The two documents are legally identical'], 0),
    ('Why might a country create foundational rights legislation like the Bill of Rights?', ['To formally establish and protect the basic rights of its citizens', 'Rights legislation has no real effect on citizens', 'To limit the rights that citizens are allowed to have', 'Such legislation is never necessary in a democracy'], 0)]),
]),
day(135, [
L('Grammar: Correlative Conjunctions',
  'Grade 6 Language strand: correlative conjunctions are pairs of words, such as either or, neither nor, and not only but also, that work together to connect balanced parts of a sentence.',
  [('What are correlative conjunctions?', ['Pairs of words that work together to connect balanced parts of a sentence', 'Single words that never appear in pairs', 'Words used only at the very end of a sentence', 'Punctuation marks used to separate clauses'], 0),
   ('Which of these is a correlative conjunction pair?', ['Either, or', 'Quickly, slowly', 'Under, over', 'Happy, sad'], 0),
   ('Which sentence uses correlative conjunctions correctly?', ['Neither the cat nor the dog was hungry.', 'Neither the cat or the dog was hungry.', 'Either the cat and the dog was hungry.', 'Neither the cat but the dog was hungry.'], 0),
   ('Which pair correctly completes this sentence: ___ the rain ___ the wind stopped the game?', ['Neither, nor', 'Either, and', 'Not only, or', 'Both, so'], 0),
   ('Why must the parts joined by correlative conjunctions usually match in grammatical form?', ['It keeps the sentence balanced and clear', 'Matching grammatical form is never necessary', 'Correlative conjunctions ignore sentence structure entirely', 'Mismatched grammar always makes a sentence correct'], 0)]),
M('Probability: Odds in Favour and Odds Against',
  'Grade 6 Math strand: odds in favour compare the number of favourable outcomes to unfavourable outcomes, while odds against compare unfavourable outcomes to favourable ones, offering another way to express likelihood besides probability.',
  [('What do odds in favour compare?', ['Favourable outcomes to unfavourable outcomes', 'Only the total number of possible outcomes', 'Unfavourable outcomes to the total outcomes', 'Nothing related to outcomes at all'], 0),
   ('What do odds against compare?', ['Unfavourable outcomes to favourable outcomes', 'Favourable outcomes to the total number of outcomes', 'Only the number of favourable outcomes', 'The total outcomes to zero'], 0),
   ('If a bag has 3 red marbles and 5 blue marbles, what are the odds in favour of drawing red?', ['3 to 5', '5 to 3', '3 to 8', '8 to 3'], 0),
   ('How is expressing odds different from expressing probability?', ['Odds compare outcomes to each other rather than to the total', 'Odds and probability are calculated in exactly the same way', 'Odds can only be used for coin flips', 'Probability never involves comparing outcomes'], 0),
   ('Why might odds be a useful way to describe likelihood in games?', ['They directly compare the chances of winning to the chances of losing', 'Odds have no connection to games or likelihood', 'Odds can only be calculated after a game ends', 'Odds always give the exact same information as a percent'], 0)]),
Sc('Earths Layers — Crust, Mantle, and Core',
   'Grade 6 Science strand: the Earth is made up of layers, including the thin outer crust, the mostly solid mantle, and the core, which consists of a molten outer layer and a solid inner layer.',
   [('What is the outermost layer of the Earth called?', ['The crust', 'The mantle', 'The outer core', 'The inner core'], 0),
    ('What layer lies beneath the crust and makes up most of Earths volume?', ['The mantle', 'The crust', 'The outer core', 'The atmosphere'], 0),
    ('What are the two parts of Earths core?', ['A molten outer core and a solid inner core', 'A gas outer core and a liquid inner core', 'Two identical solid layers', 'A frozen outer core and a molten inner core'], 0),
    ('Why is the inner core solid despite extremely high temperatures?', ['Immense pressure keeps it solid even at very high temperatures', 'The inner core is actually the coolest layer of the Earth', 'Solid rock cannot melt under any conditions', 'The inner core has no connection to temperature or pressure'], 0),
    ('Why is understanding Earths layered structure useful for explaining events like earthquakes?', ['Movement and pressure between these layers can cause the ground to shift and shake', 'Earths layers have no connection to earthquakes', 'Earthquakes only occur in the atmosphere', 'The layers of the Earth never interact with each other'], 0)]),
SS('Social Studies: The Official Languages Act and Bilingualism in Canada',
   'Grade 6 Social Studies strand: the Official Languages Act of 1969 established English and French as Canadas two official languages, requiring federal services to be available in both languages across the country.',
   [('What did the Official Languages Act establish?', ['English and French as Canadas two official languages', 'A single official language for all of Canada', 'A ban on speaking any language other than English', 'A requirement to learn a third language in schools'], 0),
    ('In what year was the Official Languages Act passed?', ['1969', '1867', '1929', '1982'], 0),
    ('What does the Official Languages Act require of federal services?', ['That they be available in both English and French', 'That they only be offered in English', 'That they be offered only in French', 'That they be available in ten different languages'], 0),
    ('Why might Canada have chosen to recognize two official languages?', ['To reflect the countrys history and the presence of both English and French speaking communities', 'Canada has never had any French speaking communities', 'Recognizing two languages has no connection to Canadian history', 'The choice was made without any historical reasoning'], 0),
    ('Why is bilingualism significant to Canadian identity?', ['It reflects the shared history of English and French speaking communities in shaping the country', 'Bilingualism has no connection to Canadian identity', 'Only one language has ever shaped Canadian history', 'Canadian identity is unrelated to language'], 0)]),
]),
day(136, [
L('Media Literacy: Analyzing Editorial Cartoons',
  'Grade 6 Language strand: editorial cartoons use humor, symbolism, and exaggeration to express an opinion about a current issue, requiring readers to interpret visual clues alongside any captions.',
  [('What is the purpose of an editorial cartoon?', ['To express an opinion about a current issue', 'To provide a purely factual weather report', 'To advertise a product for sale', 'To tell a lengthy fictional story'], 0),
   ('What techniques do editorial cartoonists commonly use?', ['Humor, symbolism, and exaggeration', 'Only realistic, detailed drawings with no symbolism', 'Long paragraphs of text with no images', 'Complex mathematical diagrams'], 0),
   ('Why might a reader need background knowledge to understand an editorial cartoon?', ['The symbols and references often relate to current events', 'Editorial cartoons never relate to real events', 'Background knowledge is never useful when reading a cartoon', 'Editorial cartoons only use random, meaningless images'], 0),
   ('What role does exaggeration play in an editorial cartoon?', ['It emphasizes a point or opinion in a memorable way', 'It always makes a cartoons message unclear', 'Exaggeration removes any opinion from the cartoon', 'It has no effect on how a viewer understands the cartoon'], 0),
   ('Why are editorial cartoons considered a form of persuasive media?', ['They are designed to influence how readers think about an issue', 'They only present neutral, unbiased information', 'Editorial cartoons never contain any opinion', 'They are created only for entertainment with no message'], 0)]),
M('Financial Literacy: Understanding Payroll Deductions and Net Income',
  'Grade 6 Math strand: net income is the amount of money left after payroll deductions, such as taxes and other contributions, are subtracted from gross income, the total amount earned before deductions.',
  [('What is gross income?', ['The total amount earned before any deductions', 'The amount left after taxes are subtracted', 'Money earned only from investments', 'The total cost of monthly expenses'], 0),
   ('What is net income?', ['The amount left after deductions are subtracted from gross income', 'The total amount earned before any deductions', 'The amount spent on entertainment each month', 'A fixed amount that never changes'], 0),
   ('Which of these is an example of a payroll deduction?', ['Income tax', 'A grocery bill', 'A birthday gift', 'A restaurant meal'], 0),
   ('If gross income is 800 dollars and deductions total 150 dollars, what is the net income?', ['650 dollars', '950 dollars', '800 dollars', '150 dollars'], 0),
   ('Why is it important to understand the difference between gross and net income when budgeting?', ['Net income reflects the actual amount available to spend or save', 'Gross income is always the amount available to spend', 'Deductions never affect how much money a person can spend', 'Budgeting does not require knowing either amount'], 0)]),
Sc('Inclined Planes and Wedges — Simple Machines That Reduce Effort',
   'Grade 6 Science strand: an inclined plane is a flat, sloped surface that reduces the force needed to raise an object, while a wedge is essentially two inclined planes joined together, often used to split or cut materials.',
   [('What is an inclined plane?', ['A flat, sloped surface that reduces the force needed to raise an object', 'A wheel connected to a rope or cable', 'A lever with a fixed pivot point', 'A machine made only of gears'], 0),
    ('What is a wedge?', ['Two inclined planes joined together, often used to split or cut', 'A wheel that spins freely on an axle', 'A rope threaded through a pulley', 'A flat surface with no slope at all'], 0),
    ('Which everyday object is an example of an inclined plane?', ['A ramp', 'A pair of scissors', 'A doorknob', 'A seesaw'], 0),
    ('Which everyday object is an example of a wedge?', ['An axe blade', 'A flagpole', 'A wheelbarrow wheel', 'A rolling pin'], 0),
    ('Why does using a ramp make it easier to move a heavy object upward compared to lifting it straight up?', ['It spreads the work over a longer distance, reducing the force needed at any moment', 'A ramp always requires more force than lifting straight up', 'Ramps have no effect on the force needed to move an object', 'Using a ramp removes the need for any force at all'], 0)]),
SS('Social Studies: The Battle of Vimy Ridge and Canadian Identity',
   'Grade 6 Social Studies strand: the Battle of Vimy Ridge in 1917 saw Canadian troops fighting together as a unified force for the first time in World War I, a victory often described as a defining moment in the development of Canadian national identity.',
   [('In what year did the Battle of Vimy Ridge take place?', ['1917', '1867', '1929', '1945'], 0),
    ('What made the Battle of Vimy Ridge significant for Canadian troops?', ['It was the first time all four Canadian divisions fought together as a unified force', 'It was fought entirely by soldiers from another country', 'It took place with no Canadian involvement at all', 'It was a minor skirmish with no lasting significance'], 0),
    ('During what larger conflict did the Battle of Vimy Ridge occur?', ['World War I', 'World War II', 'The War of 1812', 'The Cold War'], 0),
    ('Why is Vimy Ridge often described as a defining moment for Canadian identity?', ['The victory helped build a sense of national pride and unity distinct from Britain', 'The battle had no effect on how Canadians viewed their country', 'Vimy Ridge is remembered only outside of Canada', 'The battle weakened Canadian unity and pride'], 0),
    ('Why do memorials, such as the one at Vimy Ridge, remain important today?', ['They honour those who served and preserve the memory of significant historical events', 'Memorials have no role in remembering historical events', 'Vimy Ridge has been forgotten by most Canadians today', 'Memorials are built only for events with no historical value'], 0)]),
]),
day(137, [
L('Oral Communication: Group Discussion and Collaborative Talk Norms',
  'Grade 6 Language strand: effective group discussions rely on shared norms such as listening actively, taking turns, staying on topic, and building respectfully on others ideas.',
  [('What is a shared norm that supports effective group discussion?', ['Listening actively and taking turns', 'Interrupting whenever you have a new idea', 'Speaking only about unrelated topics', 'Ignoring what other speakers say'], 0),
   ('Why is staying on topic important during a group discussion?', ['It keeps the conversation focused and useful for everyone', 'Staying on topic makes a discussion less useful', 'Discussions are more effective when they constantly change subject', 'Topics never matter in a group discussion'], 0),
   ('What does it mean to build on someone elses idea?', ['Adding to or extending what another speaker said', 'Completely ignoring what another speaker said', 'Repeating your own idea without listening to others', 'Ending the discussion immediately after someone speaks'], 0),
   ('Why might a group agree on discussion norms before starting?', ['It helps ensure the conversation stays respectful and productive', 'Agreeing on norms always slows down a discussion unnecessarily', 'Group norms have no effect on how a discussion goes', 'Norms are only useful for written work, not discussions'], 0),
   ('Which behavior would NOT support a productive group discussion?', ['Interrupting other speakers frequently', 'Listening carefully to other viewpoints', 'Taking turns to share ideas', 'Building respectfully on what others say'], 0)]),
M('Number Sense: Comparing and Ordering Numbers in Scientific Notation',
  'Grade 6 Math strand: numbers written in scientific notation can be compared by first comparing their powers of ten, and if those are equal, comparing the leading decimal factors.',
  [('When comparing two numbers in scientific notation, what should be compared first?', ['The powers of ten', 'The decimal point only', 'The number of digits in the answer', 'The colour used to write the number'], 0),
   ('Which number is greater: 3.2 x 10^5 or 4.1 x 10^4?', ['3.2 x 10^5', '4.1 x 10^4', 'They are equal', 'It cannot be determined'], 0),
   ('If two numbers in scientific notation have the same power of ten, what determines which is greater?', ['The leading decimal factor', 'The colour used to display the number', 'The number of zeros in the original number', 'Nothing can be determined in this case'], 0),
   ('Why is scientific notation useful for comparing very large numbers?', ['It allows numbers to be compared quickly using their exponents', 'It makes numbers impossible to compare', 'Scientific notation removes the ability to compare numbers', 'It only works for comparing small numbers'], 0),
   ('Which number is smaller: 5.6 x 10^3 or 5.9 x 10^3?', ['5.6 x 10^3', '5.9 x 10^3', 'They are equal', 'It cannot be determined'], 0)]),
Sc('Separating Mixtures — Filtration, Evaporation, and Distillation',
   'Grade 6 Science strand: mixtures can be separated using physical methods such as filtration, which removes solids from liquids, evaporation, which leaves dissolved solids behind as a liquid turns to gas, and distillation, which separates liquids by boiling point.',
   [('What does filtration separate?', ['Solids from liquids', 'Two gases from each other', 'Two liquids with the same boiling point', 'Colours from a mixture'], 0),
    ('What happens during evaporation to separate a mixture?', ['The liquid turns into gas, leaving dissolved solids behind', 'The solid turns directly into a liquid', 'Nothing changes state during evaporation', 'The mixture becomes more concentrated as a solid'], 0),
    ('What property does distillation use to separate liquids?', ['Differences in boiling point', 'Differences in colour only', 'Differences in weight only', 'Differences in smell only'], 0),
    ('Which method would best separate sand from water?', ['Filtration', 'Distillation', 'Magnetism', 'Freezing'], 0),
    ('Why are these separation methods considered physical rather than chemical processes?', ['They do not change the chemical makeup of the substances involved', 'They always create entirely new substances', 'Physical processes always involve chemical reactions', 'These methods permanently destroy the original substances'], 0)]),
SS('Social Studies: The Printing Press and the Spread of Ideas in Europe',
   'Grade 6 Social Studies strand: the printing press, developed in the 1400s, allowed books and documents to be produced quickly and affordably, dramatically increasing literacy and speeding the spread of new ideas across Europe.',
   [('What did the printing press allow people to do?', ['Produce books and documents quickly and affordably', 'Travel between countries more quickly', 'Communicate instantly across long distances', 'Build large stone monuments'], 0),
    ('In roughly what century was the printing press developed?', ['The 1400s', 'The 1800s', 'The 900s', 'The 1700s'], 0),
    ('What effect did the printing press have on literacy across Europe?', ['It helped increase literacy by making books more widely available', 'It had no effect on how many people could read', 'It made books more expensive and harder to obtain', 'It reduced the number of books being produced'], 0),
    ('Why did the printing press speed up the spread of new ideas?', ['Information could be copied and distributed far faster than by hand', 'Ideas could no longer be written down at all', 'The printing press slowed down communication significantly', 'It made it impossible to share information widely'], 0),
    ('Why might the printing press be considered one of the most important inventions in history?', ['It transformed how knowledge and ideas were shared across society', 'It had no lasting impact on how societies developed', 'The printing press was quickly forgotten after its invention', 'It only affected a small, isolated region for a short time'], 0)]),
]),
day(138, [
L('Writing: Show, Dont Tell — Bringing Scenes to Life',
  'Grade 6 Language strand: show, dont tell is a writing technique in which a writer uses sensory detail and action to let readers experience a scene, rather than simply stating a characters emotion.',
  [('What does show, dont tell mean in writing?', ['Using sensory detail and action to let readers experience a scene', 'Simply stating a characters emotion directly', 'Avoiding any description of a character at all', 'Writing only in the form of a list'], 0),
   ('Which sentence best demonstrates showing rather than telling?', ['Her hands trembled as she gripped the letter.', 'She was nervous.', 'She felt a bit worried.', 'She was in a nervous mood.'], 0),
   ('Why might showing be more engaging for a reader than simply telling?', ['It lets a reader draw conclusions and feel more involved in the scene', 'Showing always makes writing more confusing to follow', 'Telling is always more descriptive than showing', 'Readers prefer writing with no sensory detail at all'], 0),
   ('Which technique commonly supports show, dont tell?', ['Vivid sensory description and specific action', 'Listing facts with no description', 'Avoiding any mention of setting or action', 'Using only abstract, general statements'], 0),
   ('When might a writer choose to tell rather than show?', ['When moving quickly through a less important moment', 'Telling should always replace showing in every sentence', 'A writer should never use telling in any situation', 'Only the ending of a story can ever use telling'], 0)]),
M('Geometry: Constructing Perpendicular and Angle Bisectors',
  'Grade 6 Math strand: a perpendicular bisector divides a line segment into two equal parts at a right angle, while an angle bisector divides an angle into two equal smaller angles, both often constructed using a compass and straightedge.',
  [('What does a perpendicular bisector do to a line segment?', ['Divides it into two equal parts at a right angle', 'Divides it into three unequal parts', 'Extends the segment to twice its length', 'Rotates the segment ninety degrees without dividing it'], 0),
   ('What does an angle bisector do to an angle?', ['Divides it into two equal smaller angles', 'Doubles the size of the original angle', 'Turns the angle into a straight line', 'Removes the vertex of the angle entirely'], 0),
   ('What tools are traditionally used to construct these bisectors?', ['A compass and straightedge', 'A calculator and protractor only', 'A ruler and coloured pencils', 'A computer program exclusively'], 0),
   ('If a 60 degree angle is bisected, what is the measure of each resulting angle?', ['30 degrees', '60 degrees', '120 degrees', '15 degrees'], 0),
   ('Why might a perpendicular bisector be useful for finding the midpoint of a segment?', ['It crosses the segment exactly at its midpoint', 'It never intersects the original segment', 'A perpendicular bisector always avoids the midpoint', 'It only applies to angles, not line segments'], 0)]),
Sc('Bioindicators — Using Species to Measure Environmental Health',
   'Grade 6 Science strand: a bioindicator is a species whose presence, absence, or condition reflects the health of an ecosystem, since some organisms are especially sensitive to changes in pollution or habitat quality.',
   [('What is a bioindicator?', ['A species whose presence, absence, or condition reflects ecosystem health', 'A species that has no connection to environmental conditions', 'A tool used only to measure air temperature', 'A machine used to filter polluted water'], 0),
    ('Why are some organisms useful as bioindicators?', ['They are especially sensitive to changes in pollution or habitat quality', 'They are completely unaffected by any environmental change', 'They only live in areas with no pollution at all', 'They cannot be studied by scientists'], 0),
    ('Which organism is commonly used as a bioindicator of water quality?', ['Certain aquatic insects such as mayflies', 'Large ocean-going whales only', 'Domesticated farm animals', 'Birds that never come near water'], 0),
    ('What might a sudden decline in a bioindicator species suggest about an ecosystem?', ['The ecosystem may be experiencing pollution or habitat degradation', 'The ecosystem is definitely becoming healthier', 'Bioindicator declines have no meaning for ecosystem health', 'The species decline is unrelated to environmental conditions'], 0),
    ('Why might scientists monitor bioindicators instead of measuring every environmental factor directly?', ['Bioindicators can reveal overall ecosystem health more efficiently than testing every factor separately', 'Monitoring bioindicators provides no useful information', 'Every environmental factor is equally easy to measure directly', 'Bioindicators are never used in real scientific research'], 0)]),
SS('Social Studies: The Great Wall of China — Construction and Purpose',
   'Grade 6 Social Studies strand: the Great Wall of China is a massive series of fortifications built over centuries to protect Chinese states and empires from invasions and raids, stretching thousands of kilometres across northern China.',
   [('What was the main purpose of the Great Wall of China?', ['To protect Chinese states and empires from invasions and raids', 'To serve only as a decorative monument', 'To mark the boundary of a single small village', 'To provide a route for trading ships'], 0),
    ('How was the Great Wall of China built?', ['Over centuries, connecting and extending earlier fortifications', 'In a single year by one small group of workers', 'By a single ruler working alone', 'It was built entirely underground'], 0),
    ('Roughly how long does the Great Wall of China stretch?', ['Thousands of kilometres', 'Only a few kilometres', 'Less than one kilometre', 'Around one hundred metres'], 0),
    ('Why did different Chinese dynasties continue building and repairing the wall?', ['To maintain a strong defense against invasions over time', 'The wall required no maintenance once built', 'Later dynasties had no interest in defense', 'The wall was rebuilt only for decorative purposes'], 0),
    ('Why is the Great Wall of China considered an extraordinary feat of engineering?', ['It was constructed across difficult terrain over an immense distance using the technology of its time', 'It was built entirely on flat, easy terrain', 'Modern machinery was used throughout its construction', 'The wall required no planning or coordinated effort'], 0)]),
]),
day(139, [
L('Reading: Understanding Cliches and Overused Language',
  'Grade 6 Language strand: a cliche is an expression that has been used so often it has lost much of its original impact, so writers often replace cliches with fresh, original language.',
  [('What is a cliche?', ['An expression that has been used so often it has lost its original impact', 'A brand new expression that no one has ever used before', 'A grammar rule about punctuation', 'A word borrowed from another language'], 0),
   ('Which of these phrases is a common cliche?', ['As busy as a bee', 'The unusual purple bicycle rolled slowly', 'A quiet stream flowed behind the barn', 'The scientist recorded three new measurements'], 0),
   ('Why might a writer avoid using too many cliches?', ['Overused phrases can make writing feel unoriginal', 'Cliches always make writing feel fresh and new', 'Cliches are required in every piece of writing', 'Avoiding cliches makes writing harder to understand'], 0),
   ('What might a writer do instead of using a cliche?', ['Create a fresh, original description', 'Repeat the same cliche multiple times', 'Remove all descriptive language entirely', 'Use only technical vocabulary'], 0),
   ('Why do cliches often start out as effective, vivid expressions?', ['They were once striking or clever before becoming overused', 'Cliches have never been considered effective at any point', 'They are created specifically to sound dull', 'Cliches are always invented by accident with no meaning'], 0)]),
M('Measurement: Converting Between Units of Area',
  'Grade 6 Math strand: converting between units of area, such as square centimetres and square metres, requires squaring the linear conversion factor since area involves two dimensions.',
  [('Why must the linear conversion factor be squared when converting units of area?', ['Because area involves two dimensions, length and width', 'Because area only involves a single dimension', 'Squaring is never required when converting area units', 'Linear and area units always use the same conversion factor'], 0),
   ('How many square centimetres are in one square metre?', ['10,000', '100', '1,000', '100,000'], 0),
   ('If 1 metre equals 100 centimetres, what does 1 square metre equal in square centimetres?', ['100 x 100, or 10,000', '100 + 100, or 200', '100 divided by 2, or 50', '100, with no change'], 0),
   ('Which unit would be most appropriate for measuring the area of a classroom floor?', ['Square metres', 'Square kilometres', 'Cubic centimetres', 'Millimetres'], 0),
   ('Why is it incorrect to simply use the linear conversion factor when converting area units?', ['Area is two-dimensional, so the conversion factor must be applied twice', 'Area and length always use identical conversion factors', 'Area units never need to be converted', 'Linear conversion factors apply only to volume, not area'], 0)]),
Sc('3D Printing and Modern Manufacturing Technology',
   'Grade 6 Science strand: 3D printing is a technology that builds three-dimensional objects layer by layer from a digital design, allowing for rapid prototyping and customized manufacturing in fields from medicine to engineering.',
   [('How does a 3D printer create an object?', ['By building it layer by layer from a digital design', 'By carving an object out of a solid block', 'By melting an existing object into a new shape', 'By photographing an object from multiple angles'], 0),
    ('What is one advantage of 3D printing for designers and engineers?', ['It allows for rapid prototyping of new designs', 'It always takes longer than traditional manufacturing methods', '3D printing cannot be used to test new designs', 'It removes the need for any digital design'], 0),
    ('In which field can 3D printing be used to create custom medical devices?', ['Medicine', 'Ancient history', 'Creative writing', 'Music composition'], 0),
    ('What must exist before a 3D printer can create a physical object?', ['A digital design file', 'A finished physical prototype', 'A handwritten letter', 'A separate 3D printed copy'], 0),
    ('Why is 3D printing considered useful for creating customized products?', ['Each object can be designed and printed individually to fit specific needs', '3D printing can only create identical mass-produced objects', 'Customization is impossible with 3D printing technology', 'Digital designs cannot be modified once created'], 0)]),
SS('Social Studies: The Supreme Court of Canada and Judicial Review',
   'Grade 6 Social Studies strand: the Supreme Court of Canada is the countrys highest court, with the power of judicial review to determine whether laws are constitutional, making it a key institution in Canadas system of government.',
   [('What is the Supreme Court of Canada?', ['The countrys highest court', 'A committee that writes new laws', 'A branch of the Royal Canadian Mounted Police', 'An advisory group with no legal authority'], 0),
    ('What power allows the Supreme Court to determine whether laws are constitutional?', ['Judicial review', 'Royal assent', 'Executive privilege', 'Parliamentary sovereignty'], 0),
    ('Why is judicial review an important power for the Supreme Court to hold?', ['It ensures that laws align with the principles of the constitution', 'It allows the Court to write brand new laws directly', 'Judicial review has no real effect on Canadian law', 'It removes the need for any constitution at all'], 0),
    ('How does the Supreme Court fit into Canadas system of government?', ['It acts as the final authority on legal disputes and constitutional questions', 'It has no connection to the rest of the government', 'It is responsible for enforcing traffic laws only', 'It only handles disputes between provinces and no other cases'], 0),
    ('Why might citizens value having an independent court system like the Supreme Court?', ['It helps protect rights and ensures laws are applied fairly, separate from political influence', 'An independent court system has no benefit to citizens', 'Courts function better when controlled directly by elected officials', 'Judicial independence removes all fairness from the legal system'], 0)]),
]),
day(140, [
L('Language Review: Grammar, Poetry, and Media Literacy',
  'Grade 6 Language strand review: students revisit relative clauses, free verse poetry, eponyms, PSA scripts, correlative conjunctions, editorial cartoons, and the show-dont-tell writing technique.',
  [('What does a relative clause do?', ['Adds extra information about a noun in the main sentence', 'Always begins a brand new sentence', 'Replaces the subject of a sentence entirely', 'Removes the need for any punctuation'], 0),
   ('What is free verse poetry?', ['Poetry that does not follow a fixed rhyme scheme or meter', 'Poetry that must always rhyme in a strict pattern', 'A five-line poem with a set rhythm', 'Poetry written only about nature'], 0),
   ('What is an eponym?', ['A word that comes from the name of a person', 'A word formed by combining two shorter words', 'A word borrowed directly from another language', 'A word with the exact opposite meaning of another word'], 0),
   ('What are correlative conjunctions?', ['Pairs of words that work together to connect balanced parts of a sentence', 'Single words that never appear in pairs', 'Words used only at the very end of a sentence', 'Punctuation marks used to separate clauses'], 0),
   ('What does show, dont tell mean in writing?', ['Using sensory detail and action to let readers experience a scene', 'Simply stating a characters emotion directly', 'Avoiding any description of a character at all', 'Writing only in the form of a list'], 0)]),
M('Math Review: Geometry, Number Sense, and Probability',
  'Grade 6 Math strand review: students revisit surface area of pyramids, multiplying and dividing mixed numbers, evaluating expressions by substitution, Eulers formula, and odds in favour and against.',
  [('What is surface area?', ['The total area of all the flat surfaces that cover a three-dimensional shape', 'The distance around the base of a shape only', 'The space enclosed inside a three-dimensional shape', 'A measurement used only for two-dimensional shapes'], 0),
   ('What must be done before multiplying two mixed numbers?', ['Convert each mixed number into an improper fraction', 'Round each mixed number to the nearest whole number', 'Add the whole number parts together first', 'Ignore the fractional parts entirely'], 0),
   ('What does it mean to evaluate an algebraic expression by substitution?', ['Replacing each variable with a given number and calculating the value', 'Rewriting an expression with no numbers at all', 'Removing all variables from an expression', 'Guessing the value of an expression without calculating'], 0),
   ('According to Eulers formula, what does vertices plus faces equal?', ['Edges plus two', 'Edges minus two', 'Edges times two', 'Edges divided by two'], 0),
   ('What do odds in favour compare?', ['Favourable outcomes to unfavourable outcomes', 'Only the total number of possible outcomes', 'Unfavourable outcomes to the total outcomes', 'Nothing related to outcomes at all'], 0)]),
Sc('Science Review: Energy, Earth Systems, and Technology',
   'Grade 6 Science strand review: students revisit the Sun as a star, generators, the nitrogen cycle, Earths layers, and simple machines such as inclined planes and wedges.',
   [('What is the Sun?', ['A massive ball of hot, glowing gas at the centre of our solar system', 'A large rocky planet with no light of its own', 'A frozen moon orbiting Earth', 'An artificial satellite launched by humans'], 0),
    ('What does a generator convert into electrical energy?', ['Mechanical motion', 'Sunlight only', 'Chemical energy stored in a battery', 'Sound waves'], 0),
    ('What does the nitrogen cycle describe?', ['How nitrogen moves between the atmosphere, soil, and living things', 'How water evaporates and condenses in the atmosphere', 'How rocks are broken down over time', 'How carbon moves through fossil fuels only'], 0),
    ('What is the outermost layer of the Earth called?', ['The crust', 'The mantle', 'The outer core', 'The inner core'], 0),
    ('What is an inclined plane?', ['A flat, sloped surface that reduces the force needed to raise an object', 'A wheel connected to a rope or cable', 'A lever with a fixed pivot point', 'A machine made only of gears'], 0)]),
SS('Social Studies Review: Canadian History and World Innovations',
   'Grade 6 Social Studies strand review: students revisit the Chinese Head Tax, the Quebec referendums, the discovery of insulin, the Battle of Vimy Ridge, and the printing press.',
   [('What was the Chinese Head Tax?', ['A fee imposed on Chinese immigrants entering Canada', 'A tax paid by all Canadian citizens equally', 'A reward given to new immigrants', 'A type of import tax on goods from China'], 0),
    ('What question did the Quebec referendums ask voters?', ['Whether the province should pursue sovereignty', 'Whether Canada should change its national anthem', 'Whether a new province should be created', 'Whether Quebec should build a new highway'], 0),
    ('What did Banting and Best discover in 1921?', ['Insulin', 'Penicillin', 'The vaccine for polio', 'X-ray imaging'], 0),
    ('What made the Battle of Vimy Ridge significant for Canadian troops?', ['It was the first time all four Canadian divisions fought together as a unified force', 'It was fought entirely by soldiers from another country', 'It took place with no Canadian involvement at all', 'It was a minor skirmish with no lasting significance'], 0),
    ('What did the printing press allow people to do?', ['Produce books and documents quickly and affordably', 'Travel between countries more quickly', 'Communicate instantly across long distances', 'Build large stone monuments'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_131_140)
    append_to(6, g6_131_140)
