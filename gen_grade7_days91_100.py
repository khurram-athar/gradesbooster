#!/usr/bin/env python3
"""Grade 7, Days 91-100 -- extends Grade 7 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade7.json):
appositives, idioms and their origins, epistolary structure, resumes and
cover letters, infographics and data visualization, correlative
conjunctions, subtext in dialogue, eyewitness news reports, euphemisms and
doublespeak; solving systems by elimination, factoring polynomials using
the GCF, scale factor with area/volume ratios, odds vs probability,
two-way frequency tables, negative exponents, taxes and payroll
deductions, the Pythagorean theorem in three dimensions, misleading
graphs and statistics; series and parallel circuits, meiosis and genetic
diversity, ionic and covalent chemical bonding, osmosis and diffusion,
camouflage and animal defense mechanisms, tidal and geothermal energy,
the life cycle of stars, bacteria vs viruses, the excretory system; the
Klondike Gold Rush, the Sixties Scoop, the Statute of Westminster, the
Komagata Maru incident, Canada's involvement in the Afghanistan War, the
1995 Quebec Referendum, Canada's space program, the Chinese Head Tax and
Exclusion Act, and the Oka Crisis.

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


g7_91_100 = [
day(91, [
L('Grammar: Appositives and Appositive Phrases',
  'Grade 7 Language strand: an appositive is a noun or noun phrase placed beside another noun to rename or add detail about it, such as a golden retriever in My dog, a golden retriever, is friendly.',
  [('What does an appositive do?', ['Renames or adds detail about a nearby noun', 'Turns a noun into a verb', 'A concept unrelated to grammar', 'Ends a sentence with a question mark'], 0),
   ('In the sentence My teacher, Ms. Chen, is very kind, what is the appositive?', ['Ms. Chen', 'My teacher', 'Is very kind', 'A concept unrelated to appositives'], 0),
   ('Is an appositive that is not essential to a sentence’s meaning usually set off by commas?', ['Yes', 'No, appositives are never set off by commas', 'A concept unrelated to appositives', 'Commas are only ever used at the end of a sentence'], 0),
   ('Which sentence correctly uses an appositive?', ['My friend Maria, a talented artist, painted the mural.', 'My friend a talented artist Maria painted the mural.', 'Painted a talented the mural artist Maria friend my.', 'My a talented friend artist painted Maria the mural.'], 0),
   ('Why might a writer use an appositive instead of writing a separate sentence to explain a noun?', ['It can add detail more smoothly without breaking the flow of the sentence', 'Appositives always make writing longer and less clear', 'This concept has no connection to grammar', 'Separate sentences are always clearer than an appositive'], 0)]),
M('Solving Systems of Equations by Elimination',
  'Grade 7 Math strand: the elimination method solves a system of two equations by adding or subtracting the equations to cancel out one variable, making it possible to solve for the other.',
  [('In the elimination method, what is added or subtracted to cancel out a variable?', ['The two equations in the system', 'A single number chosen at random', 'A concept unrelated to systems of equations', 'Only the variables, never the equations'], 0),
   ('If you add x plus y equals 10 and x minus y equals 4, what do you get after the y terms cancel?', ['2x equals 14', '2x equals 6', '2y equals 14', 'x equals 4'], 0),
   ('Before adding or subtracting two equations, might you need to multiply one equation to match coefficients?', ['Yes', 'No, equations can never be multiplied in elimination', 'A concept unrelated to elimination', 'Multiplying equations is never allowed in algebra'], 0),
   ('Why might elimination be a useful method for solving a system of equations?', ['It can remove one variable entirely, leaving a simpler equation to solve', 'Elimination never simplifies a system of equations', 'This concept has no connection to algebra', 'Elimination only works when equations have no variables at all'], 0),
   ('If 2x plus y equals 12 and y equals 2, what is the value of x?', ['5', '2', '12', '10'], 0)]),
Sc('Science: Series and Parallel Circuits',
   'Grade 7 Science strand: in a series circuit, components are connected along a single path so current flows through each one in turn, while in a parallel circuit, components are connected along separate branches.',
   [('In a series circuit, how are components connected?', ['Along a single path', 'Along many separate branches', 'A concept unrelated to circuits', 'They are not connected at all'], 0),
    ('In a parallel circuit, how are components connected?', ['Along separate branches', 'Along a single path only', 'A concept unrelated to circuits', 'They are never connected to a power source'], 0),
    ('If one bulb burns out in a series circuit, do the other bulbs typically stop working too?', ['Yes', 'No, the other bulbs are never affected', 'A concept unrelated to circuits', 'The other bulbs always get brighter instead'], 0),
    ('Why might a parallel circuit be useful in a house, where you want lights to work independently?', ['Each branch can operate even if another branch stops working', 'Parallel circuits always stop working completely if one bulb burns out', 'This concept has no connection to circuits', 'Parallel circuits never allow more than one device to be connected'], 0),
    ('Why is understanding the difference between series and parallel circuits useful for designing electrical systems?', ['It helps engineers choose the right circuit type for how a device should behave', 'The difference between the two circuit types never matters in design', 'This concept has no relevance to science', 'Series and parallel circuits always behave in exactly the same way'], 0)]),
SS('Social Studies: The Klondike Gold Rush',
   'Grade 7 Social Studies strand: the Klondike Gold Rush of the late 1890s drew thousands of prospectors to the Yukon in search of gold, dramatically shaping the region’s population and economy.',
   [('What did the Klondike Gold Rush draw thousands of people to the Yukon in search of?', ['Gold', 'Farmland', 'A concept unrelated to Canadian history', 'Oil'], 0),
    ('Around what decade did the Klondike Gold Rush take place?', ['The 1890s', 'The 1600s', 'A concept unrelated to the Klondike Gold Rush', 'The 2000s'], 0),
    ('Did the Klondike Gold Rush significantly increase the population of the Yukon?', ['Yes', 'No, the population of the Yukon never changed', 'A concept unrelated to the Klondike Gold Rush', 'The Yukon lost all of its population during this time'], 0),
    ('Why might towns like Dawson City have grown rapidly during the Klondike Gold Rush?', ['Prospectors and businesses moved in quickly to support the sudden rush for gold', 'No towns ever grew during the Klondike Gold Rush', 'This concept has no connection to Canadian history', 'Dawson City existed long before any gold was discovered'], 0),
    ('Why might the journey to the Klondike gold fields have been extremely difficult for prospectors?', ['Prospectors often had to travel through harsh, remote terrain with limited supplies', 'The journey to the Klondike was always simple and required no supplies', 'This concept has no relevance to social studies', 'The gold fields were located in an easily accessible city centre'], 0)]),
]),

day(92, [
L('Vocabulary: Idioms and Their Origins',
  'Grade 7 Language strand: an idiom is a phrase whose meaning cannot be understood from the literal meaning of its individual words, such as break the ice, and many idioms have interesting historical origins.',
  [('What is an idiom?', ['A phrase whose meaning cannot be understood from its individual words', 'A word that is spelled exactly as it sounds', 'A concept unrelated to vocabulary', 'A phrase that always means exactly what it literally says'], 0),
   ('What does the idiom break the ice typically mean?', ['To ease tension and start a conversation', 'To literally break a piece of ice', 'A concept unrelated to idioms', 'To end a friendship suddenly'], 0),
   ('Do many idioms have interesting historical origins?', ['Yes', 'No, idioms never have any historical origin', 'A concept unrelated to idioms', 'Idioms are only ever invented within the last year'], 0),
   ('Why might understanding idioms be especially challenging for someone learning a new language?', ['The literal words often do not match the phrase’s actual meaning', 'Idioms always mean exactly what their individual words say', 'This concept has no connection to vocabulary', 'Every language uses the exact same idioms'], 0),
   ('Why might a writer use an idiom instead of a plain, literal description?', ['An idiom can add colour and familiarity to everyday language', 'Idioms always make writing harder to understand for everyone', 'This concept has no connection to vocabulary', 'Idioms are never used in everyday conversation'], 0)]),
M('Factoring Polynomials Using the GCF',
  'Grade 7 Math strand: factoring a polynomial using the greatest common factor means finding the largest expression that divides evenly into every term, then writing the polynomial as that factor times what remains.',
  [('What does factoring a polynomial using the GCF involve finding?', ['The largest expression that divides evenly into every term', 'A random number with no connection to the terms', 'A concept unrelated to factoring', 'The smallest possible number in the polynomial'], 0),
   ('What is the GCF of the terms in 6x plus 9?', ['3', '6', '9', '2'], 0),
   ('After factoring 6x plus 9 using its GCF, what expression do you get?', ['3 times (2x plus 3)', '3 times (2x plus 9)', '6 times (x plus 9)', '9 times (6x plus 1)'], 0),
   ('Why is factoring out the GCF often the first step when simplifying a polynomial expression?', ['It can make the expression simpler and easier to work with in later steps', 'Factoring out the GCF never simplifies an expression', 'This concept has no connection to algebra', 'The GCF should always be factored out last, never first'], 0),
   ('What is the GCF of the terms in 4x squared plus 8x?', ['4x', '4', '8x', 'x'], 0)]),
Sc('Science: Meiosis and Genetic Diversity',
   'Grade 7 Science strand: meiosis is a type of cell division that produces reproductive cells with half the usual number of chromosomes, increasing genetic diversity among offspring.',
   [('What does meiosis produce?', ['Reproductive cells with half the usual number of chromosomes', 'Cells with double the usual number of chromosomes', 'A concept unrelated to biology', 'Cells that are identical in every possible way'], 0),
    ('Does meiosis increase genetic diversity among offspring?', ['Yes', 'No, meiosis has no connection to genetic diversity', 'A concept unrelated to meiosis', 'Meiosis makes every offspring genetically identical'], 0),
    ('Is meiosis a type of cell division?', ['Yes', 'No, meiosis is not connected to cell division', 'A concept unrelated to meiosis', 'Meiosis only happens in plants, never in animals'], 0),
    ('Why might genetic diversity produced by meiosis be important for a species’ survival?', ['Greater variation can help a population adapt to changing conditions over time', 'Genetic diversity has no effect on a species’ ability to survive', 'This concept has no connection to biology', 'Every member of a species should have identical genes to survive'], 0),
    ('Why do reproductive cells need half the usual number of chromosomes before fertilization occurs?', ['So that when two reproductive cells combine, the offspring has the normal full number of chromosomes', 'Reproductive cells never actually combine with each other', 'This concept has no relevance to science', 'Offspring always end up with far too many chromosomes'], 0)]),
SS('Social Studies: The Sixties Scoop',
   'Grade 7 Social Studies strand: the Sixties Scoop refers to a period from the 1960s through the 1980s when many Indigenous children in Canada were removed from their families and placed with non-Indigenous foster or adoptive families.',
   [('What does the term Sixties Scoop refer to?', ['A period when many Indigenous children were removed from their families and placed with non-Indigenous families', 'A sports competition held in the 1960s', 'A concept unrelated to Canadian history', 'A type of government tax program'], 0),
    ('Did the Sixties Scoop mainly affect Indigenous children in Canada?', ['Yes', 'No, it had no connection to Indigenous communities', 'A concept unrelated to the Sixties Scoop', 'It affected only adult members of the government'], 0),
    ('Did the Sixties Scoop continue beyond the 1960s, into later decades?', ['Yes', 'No, it lasted for only a single year', 'A concept unrelated to the Sixties Scoop', 'It ended before the 1960s even began'], 0),
    ('Why is the Sixties Scoop considered a significant and painful part of Canadian history?', ['It separated many Indigenous children from their families, culture, and communities', 'It had no lasting impact on any families or communities', 'This concept has no relevance to social studies', 'Every child involved remained closely connected to their birth family'], 0),
    ('Why might learning about the Sixties Scoop be important for understanding reconciliation efforts in Canada today?', ['It helps explain some of the historical harms that reconciliation efforts aim to address', 'The Sixties Scoop has no connection to reconciliation efforts', 'This concept has no relevance to Canadian history', 'Reconciliation efforts have no connection to Indigenous history at all'], 0)]),
]),

day(93, [
L('Reading: Analyzing Epistolary Structure in Literature',
  'Grade 7 Language strand: an epistolary text tells its story through a series of documents, such as letters, diary entries, or emails, offering readers a personal, first-hand view of events.',
  [('What is an epistolary text?', ['A text that tells its story through documents like letters or diary entries', 'A text with no characters at all', 'A concept unrelated to reading', 'A text written entirely in rhyme'], 0),
   ('Can diary entries be used to tell a story in an epistolary text?', ['Yes', 'No, diary entries can never be used in a story', 'A concept unrelated to epistolary structure', 'Diary entries are only ever used in nonfiction'], 0),
   ('Does an epistolary structure often give readers a personal, first-hand view of events?', ['Yes', 'No, epistolary texts never offer a personal view', 'A concept unrelated to epistolary structure', 'Epistolary texts always describe events from a distant, impersonal view'], 0),
   ('Why might an author choose to tell a story through letters instead of traditional narration?', ['It can create an intimate, personal connection between the reader and the character’s voice', 'Letters never add any personal connection to a story', 'This concept has no connection to literature', 'Traditional narration is always more personal than letters'], 0),
   ('Why might reading multiple characters’ letters in an epistolary novel reveal different perspectives on the same event?', ['Each letter reflects the personal viewpoint and knowledge of the person writing it', 'Every letter in an epistolary novel always describes the exact same perspective', 'This concept has no relevance to reading comprehension', 'Epistolary novels never include more than one character’s writing'], 0)]),
M('Scale Factor and Similar Figures: Area and Volume Ratios',
  'Grade 7 Math strand: when two figures are similar with a given scale factor, their areas are related by the square of the scale factor, and the volumes of similar solids are related by the cube of the scale factor.',
  [('If two similar figures have a scale factor of 2, by what factor are their areas related?', ['4, the square of 2', '2, the same as the scale factor', '8, the cube of 2', '6, double the scale factor'], 0),
   ('If two similar solids have a scale factor of 3, by what factor are their volumes related?', ['27, the cube of 3', '3, the same as the scale factor', '9, the square of 3', '6, double the scale factor'], 0),
   ('Are the areas of similar figures related by the square of the scale factor?', ['Yes', 'No, areas are never related to the scale factor', 'A concept unrelated to similar figures', 'Areas are always identical no matter the scale factor'], 0),
   ('Why might doubling the side lengths of a cube more than double its volume?', ['Volume depends on three dimensions, so scaling affects it by the cube of the scale factor', 'Volume never changes no matter how the side lengths change', 'This concept has no connection to geometry', 'Volume only ever depends on a single dimension'], 0),
   ('If a small similar figure has an area of 5 square cm and the scale factor to a larger figure is 2, what is the larger figure’s area?', ['20 square cm', '10 square cm', '5 square cm', '25 square cm'], 0)]),
Sc('Science: Chemical Bonding: Ionic and Covalent Bonds',
   'Grade 7 Science strand: atoms form chemical bonds by either transferring electrons to form ionic bonds or sharing electrons to form covalent bonds, allowing them to combine into stable compounds.',
   [('What happens during the formation of an ionic bond?', ['Electrons are transferred between atoms', 'Atoms never interact with each other at all', 'A concept unrelated to chemistry', 'Protons are transferred between atoms'], 0),
    ('What happens during the formation of a covalent bond?', ['Electrons are shared between atoms', 'Electrons are always transferred completely', 'A concept unrelated to chemical bonding', 'Neutrons are shared between atoms'], 0),
    ('Do atoms form chemical bonds to become more stable compounds?', ['Yes', 'No, chemical bonds never lead to stability', 'A concept unrelated to chemical bonding', 'Atoms never combine to form compounds'], 0),
    ('Why might table salt, formed from sodium and chlorine, be an example of an ionic bond?', ['Sodium transfers an electron to chlorine, creating oppositely charged ions that attract each other', 'Sodium and chlorine never interact with each other in any way', 'This concept has no connection to chemistry', 'Table salt is formed without any exchange of electrons'], 0),
    ('Why is understanding chemical bonding useful for predicting how substances will behave?', ['The type of bond can affect a substance’s properties, like melting point or conductivity', 'Chemical bonding never affects the properties of a substance', 'This concept has no relevance to science', 'All chemical bonds produce compounds with identical properties'], 0)]),
SS('Social Studies: The Statute of Westminster and Canadian Independence',
   'Grade 7 Social Studies strand: the Statute of Westminster of 1931 granted Canada and other British Dominions greater legislative independence from Britain, marking an important step toward full Canadian sovereignty.',
   [('What did the Statute of Westminster grant to Canada and other British Dominions?', ['Greater legislative independence from Britain', 'Complete control over the British monarchy', 'A concept unrelated to Canadian history', 'A new national flag'], 0),
    ('In what year was the Statute of Westminster passed?', ['1931', '1867', '1982', '1756'], 0),
    ('Did the Statute of Westminster mark an important step toward full Canadian sovereignty?', ['Yes', 'No, it had no connection to Canadian sovereignty', 'A concept unrelated to the Statute of Westminster', 'It reduced Canada’s independence instead of increasing it'], 0),
    ('Why might the Statute of Westminster be considered a significant milestone in Canadian history?', ['It allowed Canada to pass its own laws without needing approval from Britain', 'It had no effect on how Canada could pass its own laws', 'This concept has no relevance to social studies', 'Canada gained no legislative powers of any kind from this statute'], 0),
    ('Why might full legislative independence have taken Canada many decades to fully achieve after 1931?', ['Some aspects of Canada’s constitution still required action by the British Parliament until later reforms', 'Canada achieved complete independence in every respect immediately in 1931', 'This concept has no connection to Canadian history', 'Britain never had any remaining role in Canadian law after 1931'], 0)]),
]),

day(94, [
L('Writing: Writing a Resume and Cover Letter',
  'Grade 7 Language strand: a resume summarizes a person’s skills, education, and experience, while a cover letter introduces the applicant and explains why they are a strong fit for a specific opportunity.',
  [('What does a resume summarize?', ['A person’s skills, education, and experience', 'A person’s favourite movies', 'A concept unrelated to writing', 'A weather forecast for the week'], 0),
   ('What does a cover letter typically explain?', ['Why the applicant is a strong fit for a specific opportunity', 'A recipe for a meal', 'A concept unrelated to writing', 'The plot of a novel'], 0),
   ('Should a resume typically be organized and easy to skim quickly?', ['Yes', 'No, a resume should never be organized', 'A concept unrelated to resumes', 'Resumes are always written as a single unbroken paragraph'], 0),
   ('Why might a cover letter be tailored to a specific job or opportunity rather than written generically?', ['A tailored letter can show the reader exactly how the applicant’s skills match their specific needs', 'Cover letters should never mention a specific job or opportunity', 'This concept has no connection to writing', 'A generic cover letter is always more effective than a tailored one'], 0),
   ('Which of these is most likely a sentence from a cover letter?', ['I am confident my experience organizing school events makes me a strong fit for this role.', 'Add 5 and 9 to get 14.', 'The chemical symbol for oxygen is O.', 'Once upon a time, in a faraway kingdom.'], 0)]),
M('Probability: Odds vs Probability',
  'Grade 7 Math strand: probability compares the number of favourable outcomes to all possible outcomes, while odds compare the number of favourable outcomes to unfavourable outcomes, a related but different ratio.',
  [('What does probability compare?', ['Favourable outcomes to all possible outcomes', 'Favourable outcomes to unfavourable outcomes only', 'A concept unrelated to probability', 'Two completely unrelated numbers'], 0),
   ('What do odds compare?', ['Favourable outcomes to unfavourable outcomes', 'Favourable outcomes to all possible outcomes', 'A concept unrelated to odds', 'The total number of trials only'], 0),
   ('If a bag has 3 red marbles and 7 total marbles, what is the probability of drawing a red marble?', ['3 out of 7', '3 out of 4', '7 out of 3', '4 out of 7'], 0),
   ('Using the same bag of 3 red marbles and 7 total marbles, what are the odds of drawing a red marble, comparing red to non-red?', ['3 to 4', '3 to 7', '7 to 3', '4 to 3'], 0),
   ('Why is it important to know whether a stated ratio represents probability or odds?', ['They are calculated differently and can be easily confused if not clearly understood', 'Probability and odds are always calculated in exactly the same way', 'This concept has no connection to math', 'Odds and probability never appear in real-world situations'], 0)]),
Sc('Science: Osmosis and Diffusion in Cells',
   'Grade 7 Science strand: diffusion is the movement of particles from an area of high concentration to low concentration, while osmosis is the diffusion of water specifically across a cell membrane.',
   [('What is diffusion?', ['The movement of particles from high to low concentration', 'The movement of particles from low to high concentration only', 'A concept unrelated to biology', 'A process where particles never move at all'], 0),
    ('What is osmosis specifically the diffusion of?', ['Water across a cell membrane', 'Solid particles across a wall', 'A concept unrelated to osmosis', 'Electricity across a wire'], 0),
    ('Does diffusion generally continue until particles are evenly spread out?', ['Yes', 'No, diffusion never leads to an even spread of particles', 'A concept unrelated to diffusion', 'Particles always stay clustered in one small area forever'], 0),
    ('Why might a plant cell placed in very salty water lose water through osmosis?', ['Water tends to move toward the area with a higher concentration of dissolved particles, like salt', 'Water never moves in or out of a plant cell', 'This concept has no connection to biology', 'Salty water always causes a cell to gain water instead of losing it'], 0),
    ('Why is understanding osmosis important for understanding how cells stay healthy?', ['Cells rely on a balanced movement of water to maintain their proper shape and function', 'Water movement has no effect on how a cell functions', 'This concept has no relevance to science', 'Cells never need to regulate the water inside or around them'], 0)]),
SS('Social Studies: The Komagata Maru Incident',
   'Grade 7 Social Studies strand: in 1914, the ship Komagata Maru carrying South Asian immigrants was turned away from Vancouver due to discriminatory immigration laws, an event that reflects a difficult period in Canadian immigration history.',
   [('What was the Komagata Maru?', ['A ship carrying South Asian immigrants turned away from Vancouver in 1914', 'A type of Canadian currency', 'A concept unrelated to Canadian history', 'A famous Canadian railway line'], 0),
    ('In what year did the Komagata Maru incident occur?', ['1914', '1867', '1982', '1756'], 0),
    ('Was the Komagata Maru turned away from Canada due to discriminatory immigration laws?', ['Yes', 'No, the ship was welcomed without any restrictions', 'A concept unrelated to the Komagata Maru', 'Immigration laws had no connection to this event'], 0),
    ('Why is the Komagata Maru incident considered an important part of Canadian immigration history?', ['It highlights a period when discriminatory laws limited immigration based on national origin', 'This event had no connection to immigration policy at all', 'This concept has no relevance to social studies', 'The event shows that all immigrants were always welcomed equally at that time'], 0),
    ('Why might learning about events like the Komagata Maru incident be valuable for understanding Canada’s history of immigration policy?', ['It shows how immigration laws have changed and helps explain ongoing efforts toward fairness today', 'Canadian immigration policy has never changed throughout history', 'This concept has no relevance to social studies', 'This event has no connection to any later immigration policies'], 0)]),
]),

day(95, [
L('Media Literacy: Analyzing Infographics and Data Visualization',
  'Grade 7 Language strand: an infographic combines images, charts, and brief text to present information visually, and analyzing one involves evaluating whether its design accurately and clearly represents the data.',
  [('What does an infographic combine to present information?', ['Images, charts, and brief text', 'Only long paragraphs of text', 'A concept unrelated to media literacy', 'Only numbers with no visuals at all'], 0),
   ('Is evaluating whether a chart accurately represents data an important part of analyzing an infographic?', ['Yes', 'No, accuracy never matters when analyzing an infographic', 'A concept unrelated to infographics', 'Infographics are never based on any real data'], 0),
   ('Can a poorly designed chart mislead readers, even if the underlying data is accurate?', ['Yes', 'No, chart design never affects how readers interpret data', 'A concept unrelated to data visualization', 'Every chart design always represents data with perfect clarity'], 0),
   ('Why might a designer choose to use a bar graph instead of a large block of text to present statistics?', ['A visual format can often make complex information easier and quicker to understand', 'Visual formats always make information harder to understand', 'This concept has no connection to media literacy', 'Infographics are never used to communicate statistics'], 0),
   ('Why is it important for readers to think critically about the source of an infographic before trusting its claims?', ['The creator’s purpose or bias could affect how the data is selected or presented', 'The source of an infographic never affects how trustworthy it is', 'This concept has no relevance to media literacy', 'Infographics are always completely free of any bias'], 0)]),
M('Data: Two-Way Frequency Tables',
  'Grade 7 Math strand: a two-way frequency table organizes data about two categorical variables at once, showing how the categories relate to each other in a grid of rows and columns.',
  [('What does a two-way frequency table organize data about?', ['Two categorical variables at once', 'Only a single variable', 'A concept unrelated to data', 'No variables at all'], 0),
   ('Is a two-way frequency table typically organized into rows and columns?', ['Yes', 'No, it is never organized into rows and columns', 'A concept unrelated to frequency tables', 'It only ever has a single row with no columns'], 0),
   ('If a two-way table shows favourite sport by grade level, what two categorical variables does it compare?', ['Favourite sport and grade level', 'Only favourite sport, with no other variable', 'A concept unrelated to two-way tables', 'Only grade level, with no other variable'], 0),
   ('Why might a two-way frequency table be useful for spotting a relationship between two variables?', ['It organizes the data so patterns between the two categories become easier to see', 'Two-way tables never reveal any relationship between variables', 'This concept has no connection to data analysis', 'A two-way table can only ever show a single variable at a time'], 0),
   ('If a two-way table shows that 15 students who play soccer also play basketball, where would that number appear?', ['In the cell where the soccer row and basketball column intersect', 'Outside of the table entirely', 'A concept unrelated to two-way tables', 'Only in the table’s title'], 0)]),
Sc('Science: Camouflage and Animal Defense Mechanisms',
   'Grade 7 Science strand: camouflage is an adaptation that helps an organism blend into its surroundings, one of many defense mechanisms, such as mimicry or warning colouration, that help animals avoid predators.',
   [('What is camouflage?', ['An adaptation that helps an organism blend into its surroundings', 'A loud sound an animal makes to attract predators', 'A concept unrelated to biology', 'A behaviour that makes an animal easier to spot'], 0),
    ('Name one other type of animal defense mechanism besides camouflage, such as mimicry.', ['Mimicry', 'A concept unrelated to defense mechanisms', 'Loud colours meant to attract every predator', 'Standing perfectly still in bright open spaces'], 0),
    ('Can warning colouration help signal to predators that an animal might be dangerous or unpleasant to eat?', ['Yes', 'No, warning colouration never signals anything to predators', 'A concept unrelated to warning colouration', 'Warning colouration always attracts predators instead of warning them'], 0),
    ('Why might a harmless species evolve to look similar to a dangerous species, a strategy called mimicry?', ['Predators may avoid the harmless species if it resembles something dangerous', 'Mimicry never provides any benefit to a harmless species', 'This concept has no connection to biology', 'Predators are never fooled by an animal’s appearance'], 0),
    ('Why is camouflage considered an evolutionary advantage for many prey species?', ['Blending into the environment can make it harder for predators to spot and catch them', 'Camouflage never helps a prey species avoid being caught', 'This concept has no relevance to science', 'Predators can always see camouflaged animals with no difficulty'], 0)]),
SS('Social Studies: Canada’s Involvement in the Afghanistan War',
   'Grade 7 Social Studies strand: Canada took part in the international military and humanitarian mission in Afghanistan following the events of September 11, 2001, marking one of its longest overseas military engagements.',
   [('Following what major event did Canada take part in the international mission in Afghanistan?', ['The events of September 11, 2001', 'The Berlin Airlift', 'A concept unrelated to Canadian history', 'The Suez Crisis'], 0),
    ('Was Canada’s mission in Afghanistan one of its longest overseas military engagements?', ['Yes', 'No, Canada was never involved in Afghanistan', 'A concept unrelated to the Afghanistan War', 'The mission lasted only a single day'], 0),
    ('Did Canada’s involvement in Afghanistan include both military and humanitarian efforts?', ['Yes', 'No, Canada’s role was never connected to humanitarian efforts', 'A concept unrelated to Canada’s Afghanistan mission', 'Canada’s role was purely economic, with no military component'], 0),
    ('Why might Canada’s long engagement in Afghanistan be considered a significant topic in recent Canadian history?', ['It involved major commitments of Canadian troops, resources, and public debate over the mission’s goals', 'This mission had no lasting significance in Canadian history', 'This concept has no relevance to social studies', 'Canada never sent any troops or resources to Afghanistan'], 0),
    ('Why might historians study the effects of Canada’s Afghanistan mission on both Afghanistan and Canada?', ['Understanding a mission’s long-term effects can inform future decisions about international engagement', 'The effects of this mission are considered completely unimportant to study', 'This concept has no relevance to social studies', 'Long military missions never have any lasting effects on either country'], 0)]),
]),

day(96, [
L('Grammar: Correlative Conjunctions',
  'Grade 7 Language strand: correlative conjunctions are pairs of words that work together to connect equal parts of a sentence, such as either/or, neither/nor, and both/and.',
  [('What are correlative conjunctions?', ['Pairs of words that work together to connect equal parts of a sentence', 'A single word used to end a sentence', 'A concept unrelated to grammar', 'A punctuation mark used only in questions'], 0),
   ('Which of these is an example of a correlative conjunction pair?', ['Either/or', 'Quickly/slowly', 'A concept unrelated to correlative conjunctions', 'Run/jump'], 0),
   ('Does the pair neither/nor function as a correlative conjunction?', ['Yes', 'No, neither/nor is never used as a correlative conjunction', 'A concept unrelated to correlative conjunctions', 'Neither/nor can only be used at the start of a paragraph'], 0),
   ('Which sentence correctly uses a correlative conjunction pair?', ['She wants both a sandwich and a salad for lunch.', 'She wants both a sandwich a salad for lunch.', 'She wants a sandwich both and a salad lunch for.', 'Both she a sandwich and salad wants lunch for.'], 0),
   ('Why is it important to keep the two parts of a sentence grammatically parallel when using correlative conjunctions?', ['It keeps the sentence clear and balanced, avoiding confusing or awkward phrasing', 'Parallel structure never matters when using correlative conjunctions', 'This concept has no connection to grammar', 'Correlative conjunctions should always connect unequal or mismatched parts'], 0)]),
M('Negative Exponents and Their Meaning',
  'Grade 7 Math strand: a negative exponent indicates the reciprocal of the base raised to the positive version of that exponent, such as 2 to the power of negative 2 being equal to 1 over 2 squared.',
  [('What does a negative exponent indicate?', ['The reciprocal of the base raised to the positive version of that exponent', 'A number that must always equal zero', 'A concept unrelated to exponents', 'The base multiplied by negative one'], 0),
   ('What is 2 to the power of negative 2 equal to?', ['1 over 4', '1 over 2', '4', '-4'], 0),
   ('What is 5 to the power of negative 1 equal to?', ['1 over 5', '5', '-5', '1 over 25'], 0),
   ('Why might a negative exponent be useful for expressing very small numbers, such as in scientific notation?', ['It allows small values to be written in a compact form based on powers of ten', 'Negative exponents are never used in scientific notation', 'This concept has no connection to math', 'Negative exponents always represent extremely large numbers instead'], 0),
   ('What is 10 to the power of negative 3 equal to?', ['1 over 1000', '1000', '1 over 100', '-1000'], 0)]),
Sc('Science: Tidal and Geothermal Energy',
   'Grade 7 Science strand: tidal energy harnesses the movement of ocean tides to generate electricity, while geothermal energy uses heat from deep within the Earth, both offering renewable alternatives to fossil fuels.',
   [('What does tidal energy harness to generate electricity?', ['The movement of ocean tides', 'The heat from deep within the Earth', 'A concept unrelated to renewable energy', 'The light from the Sun'], 0),
    ('What does geothermal energy use to generate power?', ['Heat from deep within the Earth', 'The movement of ocean tides', 'A concept unrelated to geothermal energy', 'Wind blowing across open land'], 0),
    ('Are both tidal and geothermal energy considered renewable alternatives to fossil fuels?', ['Yes', 'No, neither is considered renewable', 'A concept unrelated to renewable energy', 'Both rely entirely on burning coal'], 0),
    ('Why might a coastal region be well suited to generating tidal energy?', ['Coastal areas experience the regular rise and fall of ocean tides needed to generate power', 'Tides never occur near coastal regions', 'This concept has no connection to renewable energy', 'Tidal energy can only be generated in landlocked regions'], 0),
    ('Why might geothermal energy provide a more constant power supply than solar or wind energy?', ['Heat from within the Earth is available continuously, regardless of weather or time of day', 'Geothermal energy is only available during daylight hours', 'This concept has no relevance to science', 'Geothermal energy depends entirely on wind conditions'], 0)]),
SS('Social Studies: The 1995 Quebec Referendum',
   'Grade 7 Social Studies strand: the 1995 Quebec Referendum asked Quebec voters whether the province should pursue sovereignty from Canada, resulting in a very close vote to remain part of the country.',
   [('What did the 1995 Quebec Referendum ask voters to decide?', ['Whether Quebec should pursue sovereignty from Canada', 'Whether to build a new highway system', 'A concept unrelated to Canadian history', 'Whether to change the national anthem'], 0),
    ('In what year did this referendum take place?', ['1995', '1867', '1931', '1756'], 0),
    ('Was the result of the 1995 Quebec Referendum a very close vote to remain part of Canada?', ['Yes', 'No, the vote was not close at all', 'A concept unrelated to the referendum', 'The vote resulted in Quebec immediately leaving Canada'], 0),
    ('Why might the 1995 Quebec Referendum be considered a significant moment in Canadian history?', ['It highlighted deep questions about national unity and Quebec’s place within Canada', 'The referendum had no impact on discussions about Canadian unity', 'This concept has no relevance to social studies', 'The referendum result was never close or significant in any way'], 0),
    ('Why might the close result of the referendum have led to continued discussions about Quebec’s role in Confederation?', ['A narrow outcome suggested many voters remained divided on the question of sovereignty', 'A close result always ends any further discussion on an issue', 'This concept has no connection to social studies', 'The referendum result was unanimous, with no division among voters'], 0)]),
]),

day(97, [
L('Reading: Analyzing Subtext in Dialogue',
  'Grade 7 Language strand: subtext is the underlying meaning beneath a character’s spoken words, often revealing true feelings or intentions that differ from what is literally being said.',
  [('What is subtext?', ['The underlying meaning beneath a character’s spoken words', 'The exact literal meaning of every word spoken', 'A concept unrelated to reading', 'A footnote added to explain a difficult word'], 0),
   ('Can subtext reveal feelings that differ from what a character literally says?', ['Yes', 'No, subtext never reveals any hidden feelings', 'A concept unrelated to subtext', 'Characters always say exactly what they truly feel'], 0),
   ('If a character says I am fine through gritted teeth while clearly upset, is this an example of subtext?', ['Yes', 'No, this is not an example of subtext', 'A concept unrelated to reading', 'Subtext never appears in dialogue like this'], 0),
   ('Why might an author use subtext instead of having a character state their feelings directly?', ['It can create a more realistic, nuanced portrayal of how people actually communicate', 'Subtext never adds any realism to a story', 'This concept has no connection to literature', 'Characters should always state their feelings directly and plainly'], 0),
   ('Why is paying attention to subtext an important reading skill when analyzing a story’s characters?', ['It can help readers understand a character’s true motivations beyond their literal words', 'Subtext has no connection to understanding a character’s motivations', 'This concept has no relevance to reading comprehension', 'A character’s literal words always reveal their complete truth'], 0)]),
M('Financial Literacy: Taxes and Payroll Deductions',
  'Grade 7 Math strand: payroll deductions are amounts subtracted from an employee’s gross pay, such as income tax, that result in the smaller net pay amount the employee actually receives.',
  [('What are payroll deductions?', ['Amounts subtracted from an employee’s gross pay', 'Extra bonus money added to a paycheque', 'A concept unrelated to financial literacy', 'A type of savings account'], 0),
   ('What do we call the amount of pay an employee actually receives after deductions?', ['Net pay', 'Gross pay', 'A concept unrelated to payroll', 'Overtime pay'], 0),
   ('Is income tax typically one example of a payroll deduction?', ['Yes', 'No, income tax is never deducted from pay', 'A concept unrelated to payroll deductions', 'Income tax is always paid separately with no connection to payroll'], 0),
   ('If an employee’s gross pay is 800 dollars and deductions total 150 dollars, what is their net pay?', ['650 dollars', '800 dollars', '150 dollars', '950 dollars'], 0),
   ('Why is it important to understand the difference between gross pay and net pay when planning a budget?', ['Net pay reflects the actual amount available to spend or save, not the full amount earned', 'Gross pay and net pay are always exactly the same amount', 'This concept has no connection to financial literacy', 'Budgeting never requires knowing the difference between these two amounts'], 0)]),
Sc('Science: The Life Cycle of Stars',
   'Grade 7 Science strand: stars form from clouds of gas and dust, spend most of their life fusing hydrogen into helium, and eventually change dramatically, ending as a white dwarf, neutron star, or black hole depending on their mass.',
   [('What do stars form from?', ['Clouds of gas and dust', 'Solid rock formations', 'A concept unrelated to astronomy', 'Pure liquid water'], 0),
    ('What do stars spend most of their life fusing together?', ['Hydrogen into helium', 'Oxygen into carbon', 'A concept unrelated to stars', 'Iron into gold'], 0),
    ('Can a star’s mass affect what it eventually becomes at the end of its life?', ['Yes', 'No, a star’s mass never affects its final stage', 'A concept unrelated to the life cycle of stars', 'Every star ends its life in exactly the same way'], 0),
    ('Why might a very massive star end its life as a black hole rather than a white dwarf?', ['Extremely massive stars can collapse under their own gravity into an incredibly dense object', 'Massive stars never collapse at the end of their life', 'This concept has no connection to astronomy', 'Every star, regardless of mass, becomes a white dwarf'], 0),
    ('Why do scientists study the life cycle of stars to better understand the universe?', ['It can reveal how elements are formed and how galaxies change over time', 'The life cycle of stars has no connection to understanding the universe', 'This concept has no relevance to science', 'Stars never change or evolve in any way over time'], 0)]),
SS('Social Studies: Canada’s Space Program: Canadarm and Astronauts',
   'Grade 7 Social Studies strand: Canada has contributed to international space exploration through technologies like the Canadarm robotic arm and through Canadian astronauts who have taken part in missions to space.',
   [('What is the Canadarm?', ['A robotic arm technology developed by Canada for space missions', 'A type of Canadian aircraft used only on Earth', 'A concept unrelated to Canadian history', 'A Canadian food brand'], 0),
    ('Have Canadian astronauts taken part in missions to space?', ['Yes', 'No, no Canadian has ever travelled to space', 'A concept unrelated to Canada’s space program', 'Only astronauts from other countries have ever gone to space'], 0),
    ('Has Canada contributed technology to international space exploration efforts?', ['Yes', 'No, Canada has never contributed any space technology', 'A concept unrelated to Canada’s space program', 'Canada has only ever observed space exploration from a distance'], 0),
    ('Why might Canada’s contribution of the Canadarm be considered an important part of its space program?', ['It showcased Canadian engineering and became a recognizable part of international space missions', 'The Canadarm was never actually used on any space mission', 'This concept has no relevance to social studies', 'Canada’s space program has never included any technological contributions'], 0),
    ('Why might international collaboration, such as sharing technology and astronauts, be valuable for space exploration?', ['Combining resources and expertise from multiple countries can achieve more than any single country alone', 'International collaboration never benefits space exploration efforts', 'This concept has no relevance to social studies', 'Every country conducts space missions completely independently with no cooperation'], 0)]),
]),

day(98, [
L('Writing: Writing an Eyewitness News Report',
  'Grade 7 Language strand: an eyewitness news report describes an event from a firsthand perspective, focusing on factual details such as who, what, when, where, and why, while maintaining a clear and objective tone.',
  [('What does an eyewitness news report describe?', ['An event from a firsthand perspective', 'A fictional story with no real events', 'A concept unrelated to writing', 'A recipe for cooking a meal'], 0),
   ('Should an eyewitness news report focus on factual details, like who, what, when, where, and why?', ['Yes', 'No, factual details are never included', 'A concept unrelated to news reports', 'Only opinions should be included, with no facts'], 0),
   ('Should an eyewitness news report typically maintain a clear and objective tone?', ['Yes', 'No, it should always be written with strong personal bias', 'A concept unrelated to news reports', 'Tone never matters in a news report'], 0),
   ('Why might a news reporter avoid including personal opinions in an eyewitness report?', ['Objectivity helps readers trust that the report accurately reflects what actually happened', 'Personal opinions always make a news report more trustworthy', 'This concept has no connection to writing', 'News reports should never include any factual information'], 0),
   ('Which of these sentences sounds most like it belongs in an eyewitness news report?', ['Witnesses said the fire began shortly after 6 p.m. near the corner store.', 'Once upon a time, in a faraway kingdom.', 'Add 12 and 8 to get 20.', 'I believe kindness should guide every decision I make.'], 0)]),
M('The Pythagorean Theorem in Three Dimensions',
  'Grade 7 Math strand: the Pythagorean theorem can be extended into three dimensions to find the diagonal length of a rectangular prism, using the length, width, and height of the shape.',
  [('What can the Pythagorean theorem help find when extended into three dimensions?', ['The diagonal length of a rectangular prism', 'The colour of a rectangular prism', 'A concept unrelated to geometry', 'The weight of a rectangular prism'], 0),
   ('What three measurements of a rectangular prism are used to find its diagonal length?', ['Length, width, and height', 'Only the length', 'A concept unrelated to the Pythagorean theorem', 'Only the height and colour'], 0),
   ('Is finding a diagonal in three dimensions related to the same principle used to find the hypotenuse of a right triangle?', ['Yes', 'No, the two concepts are never related', 'A concept unrelated to the Pythagorean theorem', 'Diagonals in three dimensions have nothing to do with right triangles'], 0),
   ('Why might an engineer need to calculate the diagonal length of a rectangular box?', ['It can help determine whether a long object will fit diagonally inside the box', 'Diagonal length is never useful information for engineers', 'This concept has no connection to geometry', 'Rectangular boxes never have a diagonal length at all'], 0),
   ('If a rectangular prism has a length of 3, width of 4, and height of 12, what is its space diagonal, using length squared plus width squared plus height squared under a square root?', ['13', '19', '144', '25'], 0)]),
Sc('Science: Bacteria vs Viruses',
   'Grade 7 Science strand: bacteria are single-celled living organisms that can reproduce on their own, while viruses are not considered fully alive and can only reproduce by infecting a host cell.',
   [('What are bacteria?', ['Single-celled living organisms that can reproduce on their own', 'Non-living particles that require a host to reproduce', 'A concept unrelated to biology', 'A type of plant found only in forests'], 0),
    ('Can viruses reproduce on their own, without a host cell?', ['No', 'Yes, viruses always reproduce entirely on their own', 'A concept unrelated to viruses', 'Viruses never reproduce under any circumstances'], 0),
    ('Are bacteria generally considered single-celled living organisms?', ['Yes', 'No, bacteria are never considered living organisms', 'A concept unrelated to bacteria', 'Bacteria are always made up of many cells'], 0),
    ('Why might doctors treat a bacterial infection with antibiotics but not a viral infection?', ['Antibiotics target processes specific to living bacterial cells, which viruses do not have', 'Antibiotics are always equally effective against both bacteria and viruses', 'This concept has no connection to biology', 'Bacterial infections and viral infections are always treated in exactly the same way'], 0),
    ('Why is understanding the difference between bacteria and viruses important for public health?', ['It helps determine the most effective treatment and prevention strategies for different infections', 'The difference between bacteria and viruses has no relevance to public health', 'This concept has no relevance to science', 'Bacteria and viruses always require identical treatment methods'], 0)]),
SS('Social Studies: The Chinese Head Tax and Exclusion Act',
   'Grade 7 Social Studies strand: the Canadian government imposed a Chinese Head Tax starting in 1885 and later passed the Chinese Exclusion Act in 1923, discriminatory policies that severely restricted Chinese immigration to Canada.',
   [('What was the Chinese Head Tax?', ['A fee imposed on Chinese immigrants entering Canada', 'A tax placed on all Canadian citizens equally', 'A concept unrelated to Canadian history', 'A tax on imported tea'], 0),
    ('In what year did the Canadian government begin imposing the Chinese Head Tax?', ['1885', '1931', '1995', '1756'], 0),
    ('Did the Chinese Exclusion Act of 1923 severely restrict Chinese immigration to Canada?', ['Yes', 'No, it had no effect on Chinese immigration', 'A concept unrelated to the Chinese Exclusion Act', 'It made Chinese immigration easier than ever before'], 0),
    ('Why are the Chinese Head Tax and Exclusion Act considered discriminatory policies?', ['They specifically targeted and restricted people based on their Chinese origin', 'These policies applied equally to every immigrant group without exception', 'This concept has no relevance to social studies', 'These laws had no connection to immigration policy at all'], 0),
    ('Why might the Canadian government’s later formal apology for these policies be considered significant?', ['It acknowledged the historical harm caused by discriminatory immigration laws', 'An apology for these policies would have no significance at all', 'This concept has no relevance to Canadian history', 'The government has never acknowledged these historical policies'], 0)]),
]),

day(99, [
L('Vocabulary: Euphemisms and Doublespeak',
  'Grade 7 Language strand: a euphemism is a mild or indirect word used in place of a harsher or more blunt one, while doublespeak is language deliberately used to disguise or distort the true meaning of a statement.',
  [('What is a euphemism?', ['A mild or indirect word used in place of a harsher one', 'A word that always makes a statement sound more blunt', 'A concept unrelated to vocabulary', 'A type of punctuation mark'], 0),
   ('What is doublespeak?', ['Language deliberately used to disguise or distort the true meaning of a statement', 'Language that is always perfectly clear and direct', 'A concept unrelated to doublespeak', 'A word repeated exactly twice in a sentence'], 0),
   ('Is passed away considered a euphemism for died?', ['Yes', 'No, passed away is never considered a euphemism', 'A concept unrelated to euphemisms', 'Passed away is a harsher term than died'], 0),
   ('Why might a company use doublespeak when describing layoffs, such as calling them rightsizing?', ['It can soften or obscure the true impact of a difficult decision', 'Doublespeak never changes how a difficult decision is perceived', 'This concept has no connection to vocabulary', 'Rightsizing is always a more blunt term than layoffs'], 0),
   ('Why is it important for readers to recognize euphemisms and doublespeak in persuasive or official language?', ['It helps them understand the real meaning behind softened or misleading language', 'Recognizing these terms never helps with understanding a message', 'This concept has no relevance to vocabulary', 'Euphemisms and doublespeak are never used in real communication'], 0)]),
M('Data: Identifying Misleading Graphs and Statistics',
  'Grade 7 Math strand: a misleading graph can distort how data is perceived, such as by starting a scale at a value other than zero or using inconsistent intervals, making differences look larger or smaller than they really are.',
  [('What can a misleading graph distort?', ['How data is perceived', 'The exact numerical values only, never perception', 'A concept unrelated to data', 'Nothing at all, since graphs are always accurate'], 0),
   ('Can starting a graph’s scale at a value other than zero make a difference appear larger than it really is?', ['Yes', 'No, the starting value of a scale never affects how a graph looks', 'A concept unrelated to misleading graphs', 'Graphs are never affected by where a scale begins'], 0),
   ('Can using inconsistent intervals on a graph’s axis make data misleading?', ['Yes', 'No, interval size never affects how data appears on a graph', 'A concept unrelated to graphs', 'Every graph always uses identical, consistent intervals'], 0),
   ('Why might someone intentionally create a misleading graph when presenting data?', ['To make a certain conclusion appear stronger or more dramatic than the data actually supports', 'Misleading graphs are never created intentionally', 'This concept has no connection to data analysis', 'Misleading graphs always accurately reflect every detail of the data'], 0),
   ('Why is it important to carefully examine the scale and labels on a graph before drawing conclusions from it?', ['A distorted scale or unclear label can lead to an inaccurate understanding of the data', 'The scale and labels on a graph never affect how it should be interpreted', 'This concept has no relevance to math', 'Every graph is guaranteed to be completely accurate and unbiased'], 0)]),
Sc('Science: The Excretory System: Kidneys and Waste Removal',
   'Grade 7 Science strand: the excretory system, including the kidneys, filters waste products and excess water from the blood, producing urine that removes these substances from the body.',
   [('What is the main role of the excretory system?', ['Filtering waste products and excess water from the blood', 'Pumping blood throughout the body', 'A concept unrelated to biology', 'Breaking down food in the stomach'], 0),
    ('What organ is a major part of the excretory system, filtering the blood?', ['The kidneys', 'The lungs', 'A concept unrelated to the excretory system', 'The stomach'], 0),
    ('Does the excretory system produce urine to remove waste from the body?', ['Yes', 'No, urine has no connection to waste removal', 'A concept unrelated to the excretory system', 'The excretory system never removes any waste from the body'], 0),
    ('Why is it important for the kidneys to filter excess water and waste from the blood regularly?', ['Buildup of waste products in the blood could become harmful to the body over time', 'Waste products in the blood are never harmful to the body', 'This concept has no connection to biology', 'The kidneys have no actual role in filtering the blood'], 0),
    ('Why might drinking enough water each day support healthy kidney function?', ['Adequate water helps the kidneys effectively filter waste and produce urine', 'Water intake has no effect on how the kidneys function', 'This concept has no relevance to science', 'The kidneys function identically regardless of how much water a person drinks'], 0)]),
SS('Social Studies: The Oka Crisis and Indigenous Land Rights',
   'Grade 7 Social Studies strand: the Oka Crisis of 1990 was a land dispute between the Mohawk community of Kanesatake and the town of Oka, Quebec, that drew national attention to Indigenous land rights in Canada.',
   [('What was the Oka Crisis?', ['A land dispute between the Mohawk community of Kanesatake and the town of Oka', 'A dispute over a new highway in British Columbia', 'A concept unrelated to Canadian history', 'A trade disagreement between Canada and the United States'], 0),
    ('In what year did the Oka Crisis occur?', ['1990', '1867', '1931', '1756'], 0),
    ('Did the Oka Crisis draw national attention to Indigenous land rights in Canada?', ['Yes', 'No, the crisis had no connection to Indigenous land rights', 'A concept unrelated to the Oka Crisis', 'The crisis was completely ignored by the entire country'], 0),
    ('Why might the Oka Crisis be considered an important moment in the history of Indigenous rights in Canada?', ['It highlighted long-standing land disputes and brought greater public awareness to Indigenous concerns', 'This event had no lasting impact on discussions of Indigenous rights', 'This concept has no relevance to social studies', 'The event had no connection to land or territory of any kind'], 0),
    ('Why might land disputes like the Oka Crisis still be relevant to understanding Indigenous rights today?', ['Many land claims and treaty rights remain important and unresolved issues in Canada', 'Every land dispute in Canadian history has already been completely resolved', 'This concept has no relevance to Canadian history', 'Indigenous land rights are no longer a topic of discussion in Canada'], 0)]),
]),

day(100, [
L('Review: Grammar, Vocabulary, and Media Literacy (Days 91-99)',
  'Grade 7 Language strand review: students revisit appositives, idioms, epistolary structure, resumes and cover letters, infographics, correlative conjunctions, subtext, eyewitness reports, and euphemisms.',
  [('What does an appositive do?', ['Renames or adds detail about a nearby noun', 'Turns a noun into a verb', 'A concept unrelated to grammar', 'Ends a sentence with a question mark'], 0),
   ('What is an idiom?', ['A phrase whose meaning cannot be understood from its individual words', 'A word that is spelled exactly as it sounds', 'A concept unrelated to vocabulary', 'A phrase that always means exactly what it literally says'], 0),
   ('What is an epistolary text?', ['A text that tells its story through documents like letters or diary entries', 'A text with no characters at all', 'A concept unrelated to reading', 'A text written entirely in rhyme'], 0),
   ('What are correlative conjunctions?', ['Pairs of words that work together to connect equal parts of a sentence', 'A single word used to end a sentence', 'A concept unrelated to grammar', 'A punctuation mark used only in questions'], 0),
   ('What is a euphemism?', ['A mild or indirect word used in place of a harsher one', 'A word that always makes a statement sound more blunt', 'A concept unrelated to vocabulary', 'A type of punctuation mark'], 0)]),
M('Review: Algebra, Geometry, and Data (Days 91-99)',
  'Grade 7 Math strand review: students revisit solving systems by elimination, factoring using the GCF, odds vs probability, negative exponents, the Pythagorean theorem in three dimensions, and misleading graphs.',
  [('In the elimination method, what is added or subtracted to cancel out a variable?', ['The two equations in the system', 'A single number chosen at random', 'A concept unrelated to systems of equations', 'Only the variables, never the equations'], 0),
   ('What does factoring a polynomial using the GCF involve finding?', ['The largest expression that divides evenly into every term', 'A random number with no connection to the terms', 'A concept unrelated to factoring', 'The smallest possible number in the polynomial'], 0),
   ('What do odds compare?', ['Favourable outcomes to unfavourable outcomes', 'Favourable outcomes to all possible outcomes', 'A concept unrelated to odds', 'The total number of trials only'], 0),
   ('What does a negative exponent indicate?', ['The reciprocal of the base raised to the positive version of that exponent', 'A number that must always equal zero', 'A concept unrelated to exponents', 'The base multiplied by negative one'], 0),
   ('What can a misleading graph distort?', ['How data is perceived', 'The exact numerical values only, never perception', 'A concept unrelated to data', 'Nothing at all, since graphs are always accurate'], 0)]),
Sc('Review: Physics, Biology, and Space Science (Days 91-99)',
   'Grade 7 Science strand review: students revisit series and parallel circuits, meiosis, chemical bonding, osmosis, camouflage, tidal and geothermal energy, the life cycle of stars, bacteria vs viruses, and the excretory system.',
   [('In a series circuit, how are components connected?', ['Along a single path', 'Along many separate branches', 'A concept unrelated to circuits', 'They are not connected at all'], 0),
    ('What does meiosis produce?', ['Reproductive cells with half the usual number of chromosomes', 'Cells with double the usual number of chromosomes', 'A concept unrelated to biology', 'Cells that are identical in every possible way'], 0),
    ('What happens during the formation of an ionic bond?', ['Electrons are transferred between atoms', 'Atoms never interact with each other at all', 'A concept unrelated to chemistry', 'Protons are transferred between atoms'], 0),
    ('What do stars spend most of their life fusing together?', ['Hydrogen into helium', 'Oxygen into carbon', 'A concept unrelated to stars', 'Iron into gold'], 0),
    ('What are bacteria?', ['Single-celled living organisms that can reproduce on their own', 'Non-living particles that require a host to reproduce', 'A concept unrelated to biology', 'A type of plant found only in forests'], 0)]),
SS('Review: Canadian History and Identity (Days 91-99)',
   'Grade 7 Social Studies strand review: students revisit the Klondike Gold Rush, the Sixties Scoop, the Statute of Westminster, the Komagata Maru incident, the Afghanistan War, the Quebec Referendum, and the Oka Crisis.',
   [('What did the Klondike Gold Rush draw thousands of people to the Yukon in search of?', ['Gold', 'Farmland', 'A concept unrelated to Canadian history', 'Oil'], 0),
    ('What does the term Sixties Scoop refer to?', ['A period when many Indigenous children were removed from their families and placed with non-Indigenous families', 'A sports competition held in the 1960s', 'A concept unrelated to Canadian history', 'A type of government tax program'], 0),
    ('What did the Statute of Westminster grant to Canada and other British Dominions?', ['Greater legislative independence from Britain', 'Complete control over the British monarchy', 'A concept unrelated to Canadian history', 'A new national flag'], 0),
    ('What was the Komagata Maru?', ['A ship carrying South Asian immigrants turned away from Vancouver in 1914', 'A type of Canadian currency', 'A concept unrelated to Canadian history', 'A famous Canadian railway line'], 0),
    ('What was the Oka Crisis?', ['A land dispute between the Mohawk community of Kanesatake and the town of Oka', 'A dispute over a new highway in British Columbia', 'A concept unrelated to Canadian history', 'A trade disagreement between Canada and the United States'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_91_100)
    append_to(7, g7_91_100)
