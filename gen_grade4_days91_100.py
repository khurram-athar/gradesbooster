#!/usr/bin/env python3
"""Grade 4, Days 91-100 -- extends Grade 4 from 90 to 100 days. Topics chosen
to avoid any overlap with the existing Day 1-90 set (see data/grade4.json):
verb tenses, foreshadowing, shades of meaning, sentence fragments and
run-on sentences, biography writing, assonance and consonance, modal
verbs, flashback, interview writing; subtracting mixed numbers, expanded
form, adding/subtracting money amounts, choosing an appropriate graph,
probability terms (certain/impossible/equally likely), ordering fractions
with different denominators, sales tax, perimeter of regular polygons
using formulas, divisibility rules; shell/frame/solid structures,
separating mixtures, potential and kinetic energy, types of
precipitation, everyday uses of rocks and minerals, the wedge, the
Moon's effect on tides, streamlining and drag in water, keystone
species; the Inca civilization, Canada's Constitution and Charter of
Rights and Freedoms, federal elections and voting, the Group of Seven,
the Governor General, public services and community institutions,
non-governmental organizations (NGOs), Canada's agricultural regions,
and the St. Lawrence Seaway.

Subject keys for Grade 4 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 4 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260923):
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


g4_91_100 = [
day(91, [
L('Grammar: Verb Tenses — Past, Present, and Future',
  'Grade 4 Language strand: verb tense tells when an action happens — past tense describes something that already happened, present tense describes something happening now, and future tense describes something that will happen.',
  [('Which verb tense describes an action that already happened?', ['Past tense', 'Present tense', 'Future tense', 'A concept unrelated to grammar'], 0),
   ('Which sentence uses the future tense?', ['She will walk to school tomorrow.', 'She walks to school every day.', 'She walked to school yesterday.', 'A concept unrelated to grammar'], 0),
   ('Which sentence uses the present tense?', ['He plays soccer every Saturday.', 'He played soccer last Saturday.', 'He will play soccer next Saturday.', 'A concept unrelated to grammar'], 0),
   ('Why is it important to use consistent verb tense throughout a piece of writing?', ['It helps the reader clearly understand when events are happening', 'Verb tense never affects how clear a sentence is', 'This concept has no connection to writing', 'Mixing tenses always makes writing easier to understand'], 0),
   ('Which sentence correctly uses the past tense of the verb jump?', ['Yesterday, the frog jumped into the pond.', 'Yesterday, the frog jumps into the pond.', 'Yesterday, the frog will jump into the pond.', 'A concept unrelated to grammar'], 0)]),
M('Fractions: Subtracting Mixed Numbers',
  'Grade 4 Math strand: students learn to subtract one mixed number from another, such as finding 3 and 3 fourths minus 1 and 1 fourth, by subtracting the whole numbers and the fractions separately.',
  [('What is 3 and 3 fourths minus 1 and 1 fourth?', ['2 and 2 fourths', '2 and 4 fourths', '1 and 2 fourths', '3 and 2 fourths'], 0),
   ('What is 5 and 2 fifths minus 2 and 1 fifth?', ['3 and 1 fifth', '3 and 3 fifths', '2 and 1 fifth', '4 and 1 fifth'], 0),
   ('What is 4 and 5 sixths minus 2 and 2 sixths?', ['2 and 3 sixths', '2 and 5 sixths', '3 and 3 sixths', '1 and 3 sixths'], 0),
   ('When subtracting mixed numbers, what should you subtract first?', ['The whole numbers and the fractions can each be subtracted separately', 'Only the whole numbers, ignoring the fractions completely', 'Only the fractions, ignoring the whole numbers completely', 'Neither part should ever be subtracted'], 0),
   ('What is 6 and 3 fourths minus 4 and 1 fourth?', ['2 and 2 fourths', '2 and 4 fourths', '3 and 2 fourths', '2 and 1 fourth'], 0)]),
Sc('Science: Structures: Shell, Frame, and Solid Structures',
   'Grade 4 Science strand: structures can be built as shell structures with a strong outer covering and hollow inside, frame structures made of connected beams or rods, or solid structures that are filled all the way through.',
   [('What do we call a structure with a strong outer covering and a hollow inside?', ['A shell structure', 'A frame structure', 'A solid structure', 'A concept unrelated to structures'], 0),
    ('What do we call a structure made of connected beams or rods?', ['A frame structure', 'A shell structure', 'A solid structure', 'A concept unrelated to structures'], 0),
    ('Is a solid structure, such as a dam, filled all the way through?', ['Yes', 'No, solid structures are always hollow', 'A concept unrelated to structures', 'Solid structures have no material inside them at all'], 0),
    ('Why might an egg be considered an example of a shell structure?', ['Its strong outer covering protects the hollow space inside', 'An egg has no connection to structures', 'This concept has no relevance to science', 'An egg is completely solid all the way through'], 0),
    ('Why might engineers choose a frame structure, like a bicycle frame, instead of a solid structure?', ['A frame can be strong while using less material and being lighter', 'Frame structures are always heavier than solid structures', 'This concept has no connection to structures', 'Frame structures are never used for anything real'], 0)]),
SS('Social Studies: Ancient Inca Civilization',
   'Grade 4 Social Studies strand: the Inca civilization built a large empire along the Andes Mountains in South America, known for its capital city Cusco, extensive road system, and the mountaintop city of Machu Picchu.',
   [('Where did the Inca civilization build its empire?', ['Along the Andes Mountains in South America', 'In what is now Mexico', 'A concept unrelated to ancient civilizations', 'In what is now Canada'], 0),
    ('What was the name of the Inca capital city?', ['Cusco', 'Tenochtitlan', 'Athens', 'A concept unrelated to the Inca'], 0),
    ('What famous mountaintop city did the Inca build?', ['Machu Picchu', 'Rome', 'A concept unrelated to the Inca', 'Ottawa'], 0),
    ('Why might the Inca’s extensive road system have been important to their empire?', ['It likely helped connect distant regions for trade, travel, and communication', 'Roads have no connection to ancient empires', 'The Inca never built any roads at all', 'This concept has no relevance to social studies'], 0),
    ('Why do historians consider the Inca’s ability to build in the mountains impressive?', ['They constructed lasting stone structures on difficult, high-altitude terrain', 'Building in mountains has no connection to history', 'The Inca never built anything in the mountains', 'This concept has no relevance to social studies'], 0)]),
]),

day(92, [
L('Reading: Understanding Foreshadowing',
  'Grade 4 Language strand: foreshadowing is when an author gives a hint or clue early in a story about something that will happen later, building suspense for the reader.',
  [('What do we call a hint an author gives early in a story about something that will happen later?', ['Foreshadowing', 'A concept unrelated to reading', 'A synonym', 'A metaphor'], 0),
   ('Does foreshadowing usually appear near the beginning or end of a story?', ['Near the beginning', 'Near the end', 'A concept unrelated to foreshadowing', 'Foreshadowing never appears anywhere in a story'], 0),
   ('What feeling can foreshadowing help build in a reader?', ['Suspense', 'Boredom', 'A concept unrelated to reading', 'Confusion with no purpose'], 0),
   ('Why might an author use foreshadowing instead of simply stating what will happen?', ['It keeps readers curious and engaged as they wait to see what happens', 'Foreshadowing never affects how a reader feels', 'This concept has no connection to storytelling', 'Authors should never give any hints about future events'], 0),
   ('If a story shows dark storm clouds gathering just before a character sets sail, what might this foreshadow?', ['Trouble or danger ahead on the journey', 'A concept unrelated to the story', 'A completely happy, uneventful trip', 'Nothing at all connected to the plot'], 0)]),
M('Number Sense: Representing Numbers in Expanded Form',
  'Grade 4 Math strand: students learn to write a number in expanded form by showing the value of each digit, such as writing 3,482 as 3,000 plus 400 plus 80 plus 2.',
  [('What is 3,482 written in expanded form?', ['3,000 + 400 + 80 + 2', '3,000 + 40 + 8 + 2', '300 + 400 + 80 + 2', '3,000 + 480 + 2'], 0),
   ('What is 5,791 written in expanded form?', ['5,000 + 700 + 90 + 1', '5,000 + 70 + 9 + 1', '500 + 700 + 90 + 1', '5,000 + 791'], 0),
   ('What number is represented by 2,000 + 300 + 40 + 5?', ['2,345', '2,354', '2,435', '23,45'], 0),
   ('Why is expanded form useful for understanding a number like 4,672?', ['It shows the value that each digit represents based on its place', 'Expanded form never shows any useful information', 'This concept has no connection to place value', 'Expanded form always hides the value of a number'], 0),
   ('What number is represented by 6,000 + 200 + 10 + 9?', ['6,219', '6,291', '6,129', '6,912'], 0)]),
Sc('Science: Matter: Methods for Separating Mixtures',
   'Grade 4 Science strand: mixtures can be separated using methods such as filtering, which uses a strainer to catch solid pieces, or evaporation, which lets a liquid dry up and leaves behind the solid that was dissolved in it.',
   [('What method uses a strainer to catch solid pieces out of a mixture?', ['Filtering', 'Evaporation', 'A concept unrelated to mixtures', 'Freezing'], 0),
    ('What method lets a liquid dry up to leave behind a dissolved solid?', ['Evaporation', 'Filtering', 'A concept unrelated to mixtures', 'Melting'], 0),
    ('Could you use filtering to separate sand from water?', ['Yes', 'No, filtering never separates sand from water', 'A concept unrelated to mixtures', 'Filtering only works on gases'], 0),
    ('Why might evaporation be a good method for separating salt from salt water?', ['The water dries up and leaves the solid salt behind', 'Evaporation has no connection to separating mixtures', 'This concept has no relevance to science', 'Evaporation always removes the salt instead of the water'], 0),
    ('Why is it useful to know different ways to separate mixtures?', ['It helps us recover or clean useful materials from a combined mixture', 'Separating mixtures never has any real use', 'This concept has no connection to matter', 'Mixtures can never actually be separated'], 0)]),
SS('Social Studies: Canada’s Constitution and the Charter of Rights and Freedoms',
   'Grade 4 Social Studies strand: Canada’s Constitution is the country’s highest set of laws, and it includes the Canadian Charter of Rights and Freedoms, which protects basic rights such as freedom of speech and equality for all Canadians.',
   [('What do we call the country’s highest set of laws?', ['The Constitution', 'A concept unrelated to government', 'A local bylaw', 'A school handbook'], 0),
    ('What part of the Constitution protects basic rights like freedom of speech?', ['The Canadian Charter of Rights and Freedoms', 'A concept unrelated to Canadian law', 'A provincial sports league rule', 'A single city’s parking bylaw'], 0),
    ('Does the Charter protect equality for all Canadians?', ['Yes', 'No, the Charter protects no one', 'A concept unrelated to rights', 'Only some Canadians have any rights at all'], 0),
    ('Why might it be important for a country to have a constitution?', ['It sets out the basic rules and rights that guide how the country is governed', 'A constitution never affects how a country is governed', 'This concept has no connection to government', 'Countries never need any basic laws at all'], 0),
    ('Why might freedom of speech, protected by the Charter, be important in a democracy?', ['It allows citizens to share their opinions and ideas openly', 'Freedom of speech has no connection to democracy', 'This concept has no relevance to social studies', 'Citizens are never allowed to share opinions in a democracy'], 0)]),
]),

day(93, [
L('Vocabulary: Shades of Meaning',
  'Grade 4 Language strand: many words have similar meanings but different shades of meaning, such as happy, glad, and thrilled, which all describe positive feelings but with different levels of intensity.',
  [('What do we call words with similar meanings but different levels of intensity, like happy, glad, and thrilled?', ['Shades of meaning', 'A concept unrelated to vocabulary', 'Homophones', 'Prefixes'], 0),
   ('Which word suggests the strongest level of happiness?', ['Thrilled', 'Glad', 'Content', 'A concept unrelated to shades of meaning'], 0),
   ('Which word suggests a milder feeling of being upset than furious?', ['Annoyed', 'Furious', 'Enraged', 'A concept unrelated to shades of meaning'], 0),
   ('Why might a writer choose the word enormous instead of big?', ['Enormous conveys a stronger, more precise shade of meaning', 'Enormous and big always mean exactly opposite things', 'This concept has no connection to vocabulary', 'Word choice never changes how a sentence feels'], 0),
   ('Which word shows the mildest shade of meaning for cold?', ['Cool', 'Freezing', 'Frigid', 'A concept unrelated to shades of meaning'], 0)]),
M('Financial Literacy: Adding and Subtracting Money Amounts',
  'Grade 4 Math strand: students learn to add and subtract amounts of money with dollars and cents, such as finding the total cost of two items or the change owed after a purchase.',
  [('What is 4 dollars 25 cents plus 2 dollars 50 cents?', ['6 dollars 75 cents', '6 dollars 25 cents', '7 dollars 25 cents', '6 dollars 50 cents'], 0),
   ('What is 10 dollars minus 3 dollars 40 cents?', ['6 dollars 60 cents', '7 dollars 60 cents', '6 dollars 40 cents', '7 dollars 40 cents'], 0),
   ('If a book costs 8 dollars 15 cents and a pen costs 1 dollar 20 cents, what is the total cost?', ['9 dollars 35 cents', '9 dollars 15 cents', '8 dollars 35 cents', '10 dollars 35 cents'], 0),
   ('Why is it important to line up dollars and cents correctly when adding money amounts?', ['It keeps the place value correct so the total is accurate', 'Lining up money amounts never matters', 'This concept has no connection to adding money', 'Dollars and cents can be mixed up with no effect on the answer'], 0),
   ('If you pay 20 dollars for an item that costs 14 dollars 75 cents, how much change should you receive?', ['5 dollars 25 cents', '6 dollars 25 cents', '5 dollars 75 cents', '4 dollars 25 cents'], 0)]),
Sc('Science: Energy: Potential and Kinetic Energy',
   'Grade 4 Science strand: potential energy is stored energy an object has because of its position, such as a ball held up high, while kinetic energy is the energy of motion, such as that same ball falling or rolling.',
   [('What do we call stored energy an object has because of its position?', ['Potential energy', 'Kinetic energy', 'A concept unrelated to energy', 'Sound energy'], 0),
    ('What do we call the energy of motion?', ['Kinetic energy', 'Potential energy', 'A concept unrelated to energy', 'Light energy'], 0),
    ('Does a ball held up high have potential energy?', ['Yes', 'No, a held ball never has any energy', 'A concept unrelated to energy', 'Only moving objects can have any energy at all'], 0),
    ('Why does a ball rolling down a hill have kinetic energy?', ['It is in motion, and motion is what kinetic energy describes', 'Kinetic energy has no connection to motion', 'This concept has no relevance to science', 'A rolling ball never actually has any energy'], 0),
    ('Why might a roller coaster at the top of a hill have a lot of potential energy?', ['Its high position stores energy that can convert to motion as it descends', 'Height has no connection to potential energy', 'This concept has no relevance to science', 'A roller coaster never has any stored energy'], 0)]),
SS('Social Studies: How Canadians Vote: Federal Elections',
   'Grade 4 Social Studies strand: in a federal election, Canadian citizens who are eighteen or older can vote for a candidate to represent their riding in the House of Commons, helping decide who leads the country.',
   [('How old must a Canadian citizen typically be to vote in a federal election?', ['Eighteen or older', 'Any age at all', 'A concept unrelated to elections', 'Only sixteen or older'], 0),
    ('What do voters choose in a federal election?', ['A candidate to represent their riding', 'A concept unrelated to elections', 'A new school principal', 'A local sports team captain'], 0),
    ('Where do elected federal representatives sit to make decisions for the country?', ['The House of Commons', 'A local town hall only', 'A concept unrelated to government', 'A private company office'], 0),
    ('Why is voting an important responsibility for eligible citizens in a democracy?', ['It gives citizens a voice in choosing who leads and represents them', 'Voting never actually affects who leads a country', 'This concept has no connection to democracy', 'Citizens have no role in choosing their government'], 0),
    ('Why might elections be held regularly instead of only once?', ['Regular elections let citizens choose new leaders and hold them accountable', 'Elections never need to happen more than once', 'This concept has no relevance to social studies', 'Leaders are never accountable to citizens in a democracy'], 0)]),
]),

day(94, [
L('Grammar: Sentence Fragments and Run-on Sentences',
  'Grade 4 Language strand: a sentence fragment is an incomplete sentence missing a subject or verb, while a run-on sentence incorrectly joins two or more complete sentences together without proper punctuation.',
  [('What do we call an incomplete sentence that is missing a subject or verb?', ['A sentence fragment', 'A run-on sentence', 'A concept unrelated to grammar', 'A complete sentence'], 0),
   ('What do we call two or more complete sentences incorrectly joined without proper punctuation?', ['A run-on sentence', 'A sentence fragment', 'A concept unrelated to grammar', 'A compound word'], 0),
   ('Which of these is a sentence fragment?', ['Running to the store.', 'She ran to the store.', 'She ran to the store, and then she came home.', 'A concept unrelated to grammar'], 0),
   ('Why is it important to fix run-on sentences in your writing?', ['It helps readers understand where one idea ends and another begins', 'Run-on sentences never cause any confusion for readers', 'This concept has no connection to writing clearly', 'Readers always understand run-on sentences perfectly'], 0),
   ('Which sentence correctly fixes this run-on: I like pizza I like pasta too?', ['I like pizza, and I like pasta too.', 'I like pizza I like pasta too', 'I like, pizza I like pasta too.', 'A concept unrelated to grammar'], 0)]),
M('Data Management: Choosing an Appropriate Graph',
  'Grade 4 Math strand: students learn that different graphs suit different data, such as bar graphs for comparing categories, line graphs for showing change over time, and circle graphs for showing parts of a whole.',
  [('Which type of graph is best for comparing amounts in different categories?', ['A bar graph', 'A line graph', 'A circle graph', 'A concept unrelated to data'], 0),
   ('Which type of graph is best for showing how something changes over time?', ['A line graph', 'A bar graph', 'A pictograph', 'A concept unrelated to data'], 0),
   ('Which type of graph is best for showing parts of a whole, like percentages of a budget?', ['A circle graph', 'A line graph', 'A bar graph', 'A concept unrelated to data'], 0),
   ('Why might a scientist use a line graph to track a plant’s height over several weeks?', ['A line graph clearly shows how a value changes over time', 'Line graphs never show any change over time', 'This concept has no connection to data management', 'A line graph only works for comparing separate categories'], 0),
   ('Why is it important to choose the right type of graph for your data?', ['The right graph makes the data easier to understand and compare', 'Choosing a graph type never affects how clear data is', 'This concept has no relevance to math', 'All graphs always show exactly the same information'], 0)]),
Sc('Science: Weather: Types of Precipitation',
   'Grade 4 Science strand: precipitation is water that falls from clouds to the ground in different forms, including rain, snow, sleet, and hail, depending on the temperature of the air it falls through.',
   [('What do we call water that falls from clouds to the ground?', ['Precipitation', 'Evaporation', 'A concept unrelated to weather', 'Condensation'], 0),
    ('Name one form of precipitation, such as snow.', ['Snow', 'A concept unrelated to precipitation', 'Sunshine', 'Wind'], 0),
    ('Is hail a form of precipitation made of small balls of ice?', ['Yes', 'No, hail is never made of ice', 'A concept unrelated to precipitation', 'Hail only falls as a liquid'], 0),
    ('Why might rain turn into snow as it falls?', ['The air it falls through can be cold enough to freeze the water', 'Temperature has no connection to the type of precipitation', 'This concept has no relevance to science', 'Rain always stays exactly the same no matter the temperature'], 0),
    ('Why is sleet sometimes tricky to predict compared to rain or snow?', ['It forms when precipitation partly melts and then refreezes as it falls', 'Sleet has no connection to temperature changes in the air', 'This concept has no relevance to weather', 'Sleet always falls in exactly the same way as snow'], 0)]),
SS('Social Studies: The Group of Seven: Canadian Landscape Painters',
   'Grade 4 Social Studies strand: the Group of Seven was a collection of Canadian artists in the early twentieth century known for painting Canada’s rugged wilderness landscapes, helping shape a distinct Canadian artistic identity.',
   [('What was the Group of Seven known for painting?', ['Canada’s rugged wilderness landscapes', 'Ancient Roman ruins', 'A concept unrelated to Canadian art', 'City skylines in Europe'], 0),
    ('When did the Group of Seven create most of their well-known work?', ['The early twentieth century', 'The eighteenth century', 'A concept unrelated to Canadian history', 'The twenty-first century'], 0),
    ('Did the Group of Seven help shape a distinct Canadian artistic identity?', ['Yes', 'No, they had no effect on Canadian art', 'A concept unrelated to art', 'They only painted portraits of world leaders'], 0),
    ('Why might the Group of Seven have chosen to paint Canada’s wilderness instead of European scenes?', ['They wanted to capture and celebrate Canada’s own unique landscapes', 'They had no interest in Canada’s landscapes at all', 'This concept has no connection to Canadian art', 'European scenes and Canadian wilderness look exactly the same'], 0),
    ('Why do many Canadians still recognize the Group of Seven’s paintings today?', ['Their artwork remains an important and celebrated part of Canadian culture', 'Their paintings have been completely forgotten by everyone', 'This concept has no relevance to social studies', 'Canadian art has no connection to Canadian identity'], 0)]),
]),

day(95, [
L('Writing: Writing a Biography',
  'Grade 4 Language strand: a biography is a true account of a real person’s life written by someone else, often including important events, achievements, and challenges the person experienced.',
  [('What do we call a true account of a real person’s life written by someone else?', ['A biography', 'A concept unrelated to writing', 'A recipe', 'A weather report'], 0),
   ('Should a biography include important events and achievements from the person’s life?', ['Yes', 'No, biographies never include real events', 'A concept unrelated to writing', 'Only fictional events belong in a biography'], 0),
   ('Is a biography written by the person about their own life, or by someone else?', ['By someone else', 'By the person about their own life', 'A concept unrelated to writing', 'Biographies are never written by anyone'], 0),
   ('Why might a biography include the challenges a person faced, not just their achievements?', ['It gives a fuller, more honest picture of the person’s life', 'Challenges have no connection to understanding a person’s life', 'This concept has no connection to writing a biography', 'A biography should only ever describe perfect events'], 0),
   ('Which of these would most likely appear in a biography of a famous scientist?', ['A description of the discoveries and struggles that shaped their career', 'A made-up story about a dragon', 'A list of unrelated math equations', 'A recipe for baking bread'], 0)]),
M('Probability: Certain, Impossible, and Equally Likely Events',
  'Grade 4 Math strand: an event is certain if it will definitely happen, impossible if it can never happen, and equally likely if it has the same chance of happening as another outcome, such as flipping heads or tails on a fair coin.',
  [('What do we call an event that will definitely happen?', ['Certain', 'Impossible', 'A concept unrelated to probability', 'Unlikely'], 0),
   ('What do we call an event that can never happen?', ['Impossible', 'Certain', 'A concept unrelated to probability', 'Likely'], 0),
   ('Is flipping heads or tails on a fair coin an example of equally likely outcomes?', ['Yes', 'No, one outcome is always more likely than the other', 'A concept unrelated to probability', 'A coin can never land on either side'], 0),
   ('Why is rolling a 7 on a standard 6-sided die considered impossible?', ['A standard die only has the numbers 1 through 6, so 7 can never appear', 'Rolling a 7 happens very often on a 6-sided die', 'This concept has no connection to probability', 'Every number is equally likely to appear, including 7'], 0),
   ('Why is it certain that the Sun will rise tomorrow?', ['It happens every single day without exception, based on the Earth’s rotation', 'This event has never actually happened before', 'This concept has no relevance to probability', 'The Sun rising is only a possible, not certain, event'], 0)]),
Sc('Science: Rocks and Minerals: Everyday Uses',
   'Grade 4 Science strand: rocks and minerals are used in many everyday products and structures, such as limestone in buildings, graphite in pencils, and quartz in glass and electronics.',
   [('Name one everyday product made using a mineral, such as pencils made with graphite.', ['Pencils made with graphite', 'A concept unrelated to rocks and minerals', 'Bread made with flour', 'Clothing made only from cotton'], 0),
    ('What type of rock is often used in building construction, such as limestone?', ['Limestone', 'A concept unrelated to rocks and minerals', 'Only wood', 'Only plastic'], 0),
    ('Is quartz a mineral used in making glass?', ['Yes', 'No, quartz has no connection to glass', 'A concept unrelated to minerals', 'Glass is never made using minerals'], 0),
    ('Why might it be important to study where useful rocks and minerals come from?', ['It helps us understand how to responsibly find and use these natural resources', 'Rocks and minerals have no connection to everyday products', 'This concept has no relevance to science', 'Useful rocks and minerals never actually run out'], 0),
    ('Why might electronics companies be interested in minerals like quartz?', ['Certain minerals have properties useful for building electronic components', 'Minerals are never used in making electronics', 'This concept has no relevance to science', 'Electronics are made entirely without any natural materials'], 0)]),
SS('Social Studies: The Role of the Governor General in Canada',
   'Grade 4 Social Studies strand: the Governor General is the representative of the Crown in Canada, performing ceremonial duties such as opening Parliament and formally approving new laws.',
   [('Who does the Governor General represent in Canada?', ['The Crown', 'A single province only', 'A concept unrelated to government', 'A foreign country’s president'], 0),
    ('Name one ceremonial duty of the Governor General, such as opening Parliament.', ['Opening Parliament', 'A concept unrelated to government', 'Coaching a sports team', 'Running a local business'], 0),
    ('Does the Governor General formally approve new laws passed by Parliament?', ['Yes', 'No, the Governor General has no role in approving laws', 'A concept unrelated to government', 'Only mayors approve laws in Canada'], 0),
    ('Why might the role of the Governor General be considered mostly ceremonial today?', ['Elected leaders, not the Governor General, make most day-to-day political decisions', 'The Governor General personally makes every government decision alone', 'This concept has no connection to Canadian government', 'Canada has no connection to the Crown at all'], 0),
    ('Why might it be useful for students to learn about the Governor General’s role?', ['It helps explain how Canada’s system of government is structured', 'The Governor General has no relevance to understanding government', 'This concept has no relevance to social studies', 'Canada’s government has no formal structure at all'], 0)]),
]),

day(96, [
L('Figurative Language: Assonance and Consonance',
  'Grade 4 Language strand: assonance is the repetition of vowel sounds within nearby words, such as the ee sound in fleet feet, while consonance is the repetition of consonant sounds, such as the t sound in pitter patter.',
  [('What do we call the repetition of vowel sounds within nearby words?', ['Assonance', 'Consonance', 'A concept unrelated to figurative language', 'Alliteration'], 0),
   ('What do we call the repetition of consonant sounds within nearby words?', ['Consonance', 'Assonance', 'A concept unrelated to figurative language', 'A metaphor'], 0),
   ('Which phrase is an example of assonance?', ['Fleet feet', 'Big blue balloon', 'Silent slippers', 'A concept unrelated to figurative language'], 0),
   ('Why might a poet use assonance or consonance in their writing?', ['These sound patterns can make a poem more musical and memorable', 'Assonance and consonance never affect how a poem sounds', 'This concept has no connection to figurative language', 'Sound patterns are never used in poetry'], 0),
   ('Which phrase is an example of consonance, repeating a consonant sound?', ['Pitter patter', 'Loud thunder', 'Bright sunshine', 'A concept unrelated to figurative language'], 0)]),
M('Fractions: Ordering Fractions with Different Denominators',
  'Grade 4 Math strand: students learn to order fractions with different denominators from least to greatest by finding a common denominator or comparing them to a benchmark like one half.',
  [('To order fractions with different denominators, what can you find to help compare them?', ['A common denominator', 'A common numerator only', 'A concept unrelated to fractions', 'The largest possible denominator only'], 0),
   ('Which fraction is greater, 1 half or 1 third?', ['1 half', '1 third', 'They are equal', 'Cannot be compared'], 0),
   ('Which list correctly orders these fractions from least to greatest: 1 fourth, 1 half, 3 fourths?', ['1 fourth, 1 half, 3 fourths', '3 fourths, 1 half, 1 fourth', '1 half, 1 fourth, 3 fourths', '3 fourths, 1 fourth, 1 half'], 0),
   ('Why is one half often used as a helpful benchmark when comparing fractions?', ['It gives an easy reference point to decide if a fraction is bigger or smaller', 'One half can never be used to compare fractions', 'This concept has no connection to ordering fractions', 'Benchmarks never help with comparing numbers'], 0),
   ('Which fraction is closest to one whole: 1 fourth, 1 half, or 3 fourths?', ['3 fourths', '1 fourth', '1 half', 'They are all exactly equal to one whole'], 0)]),
Sc('Science: Simple Machines: The Wedge',
   'Grade 4 Science strand: a wedge is a simple machine with a thick end that tapers to a thin edge, used to push things apart or cut through materials, such as an axe blade or a doorstop.',
   [('What shape does a wedge have, with a thick end tapering to what?', ['A thin edge', 'A perfectly flat surface', 'A concept unrelated to simple machines', 'A perfect circle'], 0),
    ('Name one example of a wedge, such as an axe blade.', ['An axe blade', 'A concept unrelated to simple machines', 'A flat table top', 'A round wheel'], 0),
    ('Can a wedge be used to push things apart or cut through materials?', ['Yes', 'No, a wedge is never used for cutting or splitting', 'A concept unrelated to wedges', 'A wedge can only be used to hold a door open forever'], 0),
    ('Why might a doorstop shaped like a wedge work well to hold a door in place?', ['Its tapered shape can wedge tightly against the floor and door', 'A wedge shape has no connection to holding objects in place', 'This concept has no relevance to science', 'A doorstop shaped like a wedge can never actually work'], 0),
    ('Why is a wedge considered a simple machine, similar to a lever or pulley?', ['It changes the amount or direction of force needed to do work', 'A wedge never changes how much force is needed', 'This concept has no connection to simple machines', 'Simple machines never make any task easier'], 0)]),
SS('Social Studies: Public Services and Community Institutions',
   'Grade 4 Social Studies strand: public services such as libraries, hospitals, and fire departments are funded by government and community resources to meet the needs of everyone in a community.',
   [('Name one public service that meets a community’s needs, such as a library.', ['A library', 'A concept unrelated to community services', 'A private amusement park', 'A single person’s home'], 0),
    ('Are public services like hospitals typically funded by government and community resources?', ['Yes', 'No, public services are never funded by the community', 'A concept unrelated to public services', 'Public services are always fully paid for by one single family'], 0),
    ('What public service responds quickly to fires and emergencies?', ['The fire department', 'A concept unrelated to public services', 'A private bakery', 'A local toy store'], 0),
    ('Why might a community choose to fund a public library instead of leaving it to private businesses?', ['It ensures that books and resources are accessible to everyone, regardless of income', 'Public libraries have no benefit to a community', 'This concept has no connection to public services', 'Only wealthy people are ever allowed to use a library'], 0),
    ('Why are public services like hospitals and fire departments important to a community?', ['They provide essential care and safety that benefit all community members', 'Public services have no real impact on a community', 'This concept has no relevance to social studies', 'Communities never actually need this kind of support'], 0)]),
]),

day(97, [
L('Grammar: Modal Verbs',
  'Grade 4 Language strand: modal verbs, such as can, could, should, and must, are helping verbs that express ability, possibility, permission, or necessity.',
  [('What do we call helping verbs such as can, could, should, and must?', ['Modal verbs', 'A concept unrelated to grammar', 'Nouns', 'Adjectives'], 0),
   ('Which modal verb expresses ability, as in I can swim?', ['Can', 'Must', 'A concept unrelated to grammar', 'Was'], 0),
   ('Which modal verb expresses necessity, as in You must wear a helmet?', ['Must', 'Could', 'A concept unrelated to grammar', 'Ran'], 0),
   ('Why might a writer use should instead of must in a sentence giving advice?', ['Should suggests a recommendation, while must suggests a requirement', 'Should and must always mean exactly the same thing', 'This concept has no connection to grammar', 'Modal verbs never change the meaning of a sentence'], 0),
   ('Which sentence correctly uses a modal verb to ask for permission?', ['May I borrow your pencil?', 'Pencil your borrow may I?', 'I pencil borrow may.', 'A concept unrelated to grammar'], 0)]),
M('Financial Literacy: Understanding Sales Tax (GST/HST)',
  'Grade 4 Math strand: sales tax is an extra percentage added to the price of many goods and services, such as the HST in Ontario, which increases the total amount a customer pays at checkout.',
  [('What do we call the extra percentage added to the price of many goods and services?', ['Sales tax', 'A discount', 'A concept unrelated to money', 'A refund'], 0),
   ('What is the name of the sales tax charged in Ontario?', ['HST', 'GDP', 'A concept unrelated to finance', 'ATM'], 0),
   ('Does sales tax increase or decrease the total amount a customer pays?', ['Increase', 'Decrease', 'A concept unrelated to sales tax', 'Sales tax has no effect on the total'], 0),
   ('Why might the price shown on a store shelf be different from the amount you actually pay at checkout?', ['Sales tax is often added to the shelf price at checkout', 'Store prices never change at checkout', 'This concept has no connection to sales tax', 'Sales tax always lowers the amount you pay'], 0),
   ('If an item costs 10 dollars and 1 dollar 30 cents in sales tax is added, what is the total cost?', ['11 dollars 30 cents', '10 dollars 30 cents', '11 dollars', '9 dollars 70 cents'], 0)]),
Sc('Science: Space: The Moon’s Effect on Earth — Tides',
   'Grade 4 Science strand: the Moon’s gravity pulls on Earth’s oceans, causing tides, the regular rising and falling of sea levels along coastlines.',
   [('What causes tides, the regular rising and falling of sea levels?', ['The Moon’s gravity pulling on Earth’s oceans', 'The Sun’s heat warming the oceans', 'A concept unrelated to tides', 'Wind blowing across the ocean surface only'], 0),
    ('Do tides cause sea levels along coastlines to rise and fall?', ['Yes', 'No, sea levels never change', 'A concept unrelated to tides', 'Tides only affect rivers, never oceans'], 0),
    ('What force from the Moon is mainly responsible for tides?', ['Gravity', 'Sunlight', 'A concept unrelated to tides', 'Wind'], 0),
    ('Why might coastal communities need to know the tide schedule?', ['Tides can affect boating, fishing, and beach safety', 'Tides have no connection to coastal communities', 'This concept has no relevance to science', 'Tide schedules never change and do not need tracking'], 0),
    ('Why does the Moon, despite being far away, have a noticeable effect on Earth’s oceans?', ['Its gravitational pull is strong enough to move huge amounts of ocean water', 'The Moon has no gravitational pull at all', 'This concept has no relevance to science', 'Distance always makes gravity completely disappear'], 0)]),
SS('Social Studies: The Role of Non-Governmental Organizations (NGOs)',
   'Grade 4 Social Studies strand: a non-governmental organization, or NGO, is a group that is not run by the government and works to help people or protect the environment, such as providing disaster relief or supporting education.',
   [('What does NGO stand for?', ['Non-governmental organization', 'National government office', 'A concept unrelated to organizations', 'New government operation'], 0),
    ('Is an NGO run by the government?', ['No', 'Yes, NGOs are always run by the government', 'A concept unrelated to NGOs', 'NGOs are the same thing as a national government'], 0),
    ('Name one type of work an NGO might do, such as disaster relief.', ['Disaster relief', 'A concept unrelated to NGOs', 'Selling video games', 'Running a private restaurant'], 0),
    ('Why might people choose to support an NGO that helps with education in other countries?', ['It can help provide resources and opportunities where they are needed most', 'NGOs never actually help anyone', 'This concept has no connection to global issues', 'Education has no connection to community wellbeing'], 0),
    ('Why might NGOs work alongside governments instead of replacing them?', ['NGOs can offer additional support and expertise that complements government efforts', 'NGOs and governments never work together', 'This concept has no relevance to social studies', 'NGOs always try to replace a country’s government'], 0)]),
]),

day(98, [
L('Reading: Understanding Flashback in Narratives',
  'Grade 4 Language strand: a flashback is when a story pauses its current events to show something that happened earlier, helping readers understand a character’s past or the reasons behind their actions.',
  [('What do we call it when a story pauses to show something that happened earlier?', ['A flashback', 'A concept unrelated to reading', 'A foreshadow', 'A summary'], 0),
   ('Can a flashback help readers understand a character’s past?', ['Yes', 'No, flashbacks never explain anything about a character', 'A concept unrelated to reading', 'Flashbacks only describe future events'], 0),
   ('Does a flashback show events from before or after the current point in the story?', ['Before', 'After', 'A concept unrelated to reading', 'Flashbacks show no events at all'], 0),
   ('Why might an author use a flashback to explain why a character is afraid of dogs?', ['It can reveal a past experience that caused the character’s fear', 'Flashbacks never explain a character’s feelings', 'This concept has no connection to storytelling', 'A character’s fear can never be explained by past events'], 0),
   ('Which of these is most likely a signal that a flashback is beginning in a story?', ['The narrator suddenly describes an event from years earlier', 'A character orders food at a restaurant', 'A concept unrelated to the story', 'The story ends with no further explanation'], 0)]),
M('Geometry: Perimeter of Regular Polygons Using Formulas',
  'Grade 4 Math strand: students learn to find the perimeter of a regular polygon, where all sides are equal, by multiplying the length of one side by the number of sides.',
  [('How do you find the perimeter of a regular polygon?', ['Multiply the length of one side by the number of sides', 'Add the length of only two sides', 'A concept unrelated to geometry', 'Divide the length of one side by the number of sides'], 0),
   ('What is the perimeter of a regular pentagon with sides of 6 cm?', ['30 cm', '25 cm', '36 cm', '24 cm'], 0),
   ('What is the perimeter of a square with sides of 8 cm?', ['32 cm', '16 cm', '24 cm', '40 cm'], 0),
   ('Why does multiplying work as a shortcut for finding the perimeter of a regular polygon?', ['All the sides are equal, so adding them repeatedly is the same as multiplying', 'Multiplication never works for finding perimeter', 'This concept has no connection to geometry', 'Regular polygons never have equal sides'], 0),
   ('What is the perimeter of a regular hexagon with sides of 5 cm?', ['30 cm', '25 cm', '35 cm', '20 cm'], 0)]),
Sc('Science: Forces: Streamlining and Reducing Drag in Water',
   'Grade 4 Science strand: streamlining is shaping an object to move smoothly through water with less resistance, called drag, which is why boats and fish often have narrow, smooth, pointed shapes.',
   [('What do we call the force that resists an object’s motion through water?', ['Drag', 'Gravity', 'A concept unrelated to forces', 'Magnetism'], 0),
    ('What do we call shaping an object to move smoothly through water with less resistance?', ['Streamlining', 'Erosion', 'A concept unrelated to forces', 'Evaporation'], 0),
    ('Do fish often have narrow, smooth, pointed shapes to help them move through water?', ['Yes', 'No, fish shapes have no connection to moving through water', 'A concept unrelated to streamlining', 'Fish are always shaped like perfect cubes'], 0),
    ('Why might boat designers shape a hull to be narrow and smooth?', ['A streamlined shape reduces drag, helping the boat move faster and more efficiently', 'Boat shape has no connection to how fast it can travel', 'This concept has no relevance to science', 'A wide, blocky shape always moves fastest through water'], 0),
    ('Why might a wide, flat object experience more drag moving through water than a narrow, pointed one?', ['It pushes against more water at once, increasing resistance', 'Shape never affects how much resistance an object experiences', 'This concept has no relevance to forces', 'Flat objects always move through water with no resistance at all'], 0)]),
SS('Social Studies: Canada’s Agricultural Regions and Food Production',
   'Grade 4 Social Studies strand: Canada has distinct agricultural regions, such as the Prairies for grain farming and the Niagara region for fruit growing, which produce much of the country’s food.',
   [('Which Canadian region is known for grain farming, such as wheat?', ['The Prairies', 'The Arctic tundra', 'A concept unrelated to agriculture', 'The deep ocean'], 0),
    ('Which Ontario region is known for growing fruit, such as grapes and peaches?', ['The Niagara region', 'A concept unrelated to agriculture', 'The far north', 'A city’s downtown core'], 0),
    ('Do different regions of Canada grow different types of food based on their climate and land?', ['Yes', 'No, every region of Canada grows exactly the same food', 'A concept unrelated to agriculture', 'Climate never affects what can be grown'], 0),
    ('Why might farmers in the Prairies focus on growing grain crops like wheat?', ['The flat land and climate of the Prairies are well suited to grain farming', 'The Prairies have no connection to farming', 'This concept has no relevance to social studies', 'Grain crops can only be grown in mountains'], 0),
    ('Why is it important for Canada to have multiple agricultural regions producing different foods?', ['It helps provide a variety of food and supports the country’s food supply', 'Having multiple agricultural regions has no benefit to Canada', 'This concept has no relevance to social studies', 'Canada does not need to grow its own food'], 0)]),
]),

day(99, [
L('Writing: Writing an Interview',
  'Grade 4 Language strand: writing an interview involves preparing clear questions in advance and recording a person’s answers accurately, often used in non-fiction writing like newspaper articles.',
  [('What should a writer prepare in advance before conducting an interview?', ['Clear questions', 'A fictional story', 'A concept unrelated to writing', 'A drawing with no connection to the topic'], 0),
   ('What is the goal of recording a person’s answers during an interview?', ['To record their answers accurately', 'To make up new answers instead', 'A concept unrelated to writing', 'To ignore what the person actually says'], 0),
   ('Is an interview often used in non-fiction writing, like newspaper articles?', ['Yes', 'No, interviews are never used in non-fiction writing', 'A concept unrelated to writing', 'Interviews are only used in fictional stories'], 0),
   ('Why might a reporter ask open-ended questions during an interview instead of only yes-or-no questions?', ['Open-ended questions can lead to more detailed and useful answers', 'Open-ended questions never provide any useful information', 'This concept has no connection to interviewing', 'Yes-or-no questions always provide the most detail'], 0),
   ('Which of these would most likely be a good interview question for a local firefighter?', ['What made you want to become a firefighter?', 'What is the chemical symbol for water?', 'Add 3 and 4 to get 7.', 'A triangle has three sides.'], 0)]),
M('Number Sense: Divisibility Rules (2, 5, and 10)',
  'Grade 4 Math strand: divisibility rules help determine if a number can be divided evenly by another number, such as a number being divisible by 2 if it ends in an even digit, by 5 if it ends in 0 or 5, and by 10 if it ends in 0.',
  [('A number is divisible by 2 if it ends in what kind of digit?', ['An even digit', 'An odd digit', 'A concept unrelated to divisibility', 'Any digit except zero'], 0),
   ('A number is divisible by 5 if it ends in which digits?', ['0 or 5', '2 or 4', '1 or 3', '6 or 8'], 0),
   ('A number is divisible by 10 if it ends in which digit?', ['0', '5', '1', '2'], 0),
   ('Why are divisibility rules useful when working with larger numbers?', ['They let you quickly check if a number divides evenly without doing full division', 'Divisibility rules never help with checking numbers', 'This concept has no connection to number sense', 'Divisibility rules only work for very small numbers'], 0),
   ('Is the number 340 divisible by both 2 and 5?', ['Yes', 'No, 340 is divisible by neither 2 nor 5', 'A concept unrelated to divisibility', '340 is divisible by 5 only, never by 2'], 0)]),
Sc('Science: Ecosystems: Keystone Species',
   'Grade 4 Science strand: a keystone species is a species that has a very large effect on its ecosystem compared to its numbers, such as a sea otter controlling sea urchin populations to protect kelp forests.',
   [('What do we call a species that has a very large effect on its ecosystem compared to its numbers?', ['A keystone species', 'An invasive species', 'A concept unrelated to ecosystems', 'A domesticated species'], 0),
    ('Name one example of a keystone species, such as the sea otter.', ['The sea otter', 'A concept unrelated to keystone species', 'A house cat', 'A farm chicken'], 0),
    ('Can removing a keystone species cause major changes throughout an ecosystem?', ['Yes', 'No, removing any species never affects an ecosystem', 'A concept unrelated to ecosystems', 'Keystone species have no real impact on their ecosystem'], 0),
    ('Why might sea otters be important for protecting kelp forests?', ['They control sea urchin populations that would otherwise overeat the kelp', 'Sea otters have no connection to kelp forests', 'This concept has no relevance to science', 'Kelp forests grow better without any otters present'], 0),
    ('Why do scientists pay special attention to keystone species when protecting an ecosystem?', ['Losing a keystone species can cause much bigger changes than losing other species', 'All species have exactly the same impact on an ecosystem', 'This concept has no relevance to science', 'Keystone species are never actually important to an ecosystem'], 0)]),
SS('Social Studies: The St. Lawrence Seaway and Its Importance to Trade',
   'Grade 4 Social Studies strand: the St. Lawrence Seaway is a system of canals and locks that allows large ships to travel between the Atlantic Ocean and the Great Lakes, supporting trade across central Canada.',
   [('What is the St. Lawrence Seaway a system of?', ['Canals and locks', 'Mountains and valleys', 'A concept unrelated to geography', 'Deserts and dunes'], 0),
    ('What does the St. Lawrence Seaway allow large ships to travel between?', ['The Atlantic Ocean and the Great Lakes', 'The Pacific Ocean and the Arctic Ocean', 'A concept unrelated to trade', 'Two cities within the same province'], 0),
    ('Does the St. Lawrence Seaway support trade across central Canada?', ['Yes', 'No, the Seaway has no connection to trade', 'A concept unrelated to the Seaway', 'The Seaway only supports trade in one small town'], 0),
    ('Why are locks an important part of the St. Lawrence Seaway?', ['They raise and lower ships to different water levels along the route', 'Locks have no function within the Seaway', 'This concept has no relevance to social studies', 'Locks are only used to stop ships from moving at all'], 0),
    ('Why might the St. Lawrence Seaway be considered important to Canada’s economy?', ['It allows goods to be shipped efficiently between inland regions and international markets', 'The Seaway has no connection to Canada’s economy', 'This concept has no relevance to social studies', 'Goods can never be transported using the Seaway'], 0)]),
]),

day(100, [
L('Review: Vocabulary, Grammar, and Reading Skills (Days 91-99)',
  'Grade 4 Language strand review: students revisit verb tenses, foreshadowing, shades of meaning, sentence fragments and run-ons, biography writing, assonance and consonance, modal verbs, flashback, and interview writing.',
  [('Which verb tense describes an action that already happened?', ['Past tense', 'Present tense', 'Future tense', 'A concept unrelated to grammar'], 0),
   ('What do we call words with similar meanings but different levels of intensity, like happy, glad, and thrilled?', ['Shades of meaning', 'A concept unrelated to vocabulary', 'Homophones', 'Prefixes'], 0),
   ('What do we call a true account of a real person’s life written by someone else?', ['A biography', 'A concept unrelated to writing', 'A recipe', 'A weather report'], 0),
   ('What do we call helping verbs such as can, could, should, and must?', ['Modal verbs', 'A concept unrelated to grammar', 'Nouns', 'Adjectives'], 0),
   ('What should a writer prepare in advance before conducting an interview?', ['Clear questions', 'A fictional story', 'A concept unrelated to writing', 'A drawing with no connection to the topic'], 0)]),
M('Review: Fractions, Number Sense, and Data (Days 91-99)',
  'Grade 4 Math strand review: students revisit subtracting mixed numbers, expanded form, adding and subtracting money, choosing appropriate graphs, probability terms, ordering fractions, sales tax, perimeter of regular polygons, and divisibility rules.',
  [('What is 3 and 3 fourths minus 1 and 1 fourth?', ['2 and 2 fourths', '2 and 4 fourths', '1 and 2 fourths', '3 and 2 fourths'], 0),
   ('What is 4 dollars 25 cents plus 2 dollars 50 cents?', ['6 dollars 75 cents', '6 dollars 25 cents', '7 dollars 25 cents', '6 dollars 50 cents'], 0),
   ('What do we call an event that will definitely happen?', ['Certain', 'Impossible', 'A concept unrelated to probability', 'Unlikely'], 0),
   ('What do we call the extra percentage added to the price of many goods and services?', ['Sales tax', 'A discount', 'A concept unrelated to money', 'A refund'], 0),
   ('A number is divisible by 2 if it ends in what kind of digit?', ['An even digit', 'An odd digit', 'A concept unrelated to divisibility', 'Any digit except zero'], 0)]),
Sc('Review: Structures, Matter, Energy, and Earth and Space Systems (Days 91-99)',
   'Grade 4 Science strand review: students revisit shell/frame/solid structures, separating mixtures, potential and kinetic energy, precipitation, rocks and minerals, the wedge, tides, drag in water, and keystone species.',
   [('What do we call a structure with a strong outer covering and a hollow inside?', ['A shell structure', 'A frame structure', 'A solid structure', 'A concept unrelated to structures'], 0),
    ('What do we call stored energy an object has because of its position?', ['Potential energy', 'Kinetic energy', 'A concept unrelated to energy', 'Sound energy'], 0),
    ('Name one everyday product made using a mineral, such as pencils made with graphite.', ['Pencils made with graphite', 'A concept unrelated to rocks and minerals', 'Bread made with flour', 'Clothing made only from cotton'], 0),
    ('What causes tides, the regular rising and falling of sea levels?', ['The Moon’s gravity pulling on Earth’s oceans', 'The Sun’s heat warming the oceans', 'A concept unrelated to tides', 'Wind blowing across the ocean surface only'], 0),
    ('What do we call a species that has a very large effect on its ecosystem compared to its numbers?', ['A keystone species', 'An invasive species', 'A concept unrelated to ecosystems', 'A domesticated species'], 0)]),
SS('Review: Ancient Societies, Government, and Canadian Geography (Days 91-99)',
   'Grade 4 Social Studies strand review: students revisit the Inca civilization, the Constitution and Charter, federal elections, the Group of Seven, the Governor General, public services, NGOs, agricultural regions, and the St. Lawrence Seaway.',
   [('Where did the Inca civilization build its empire?', ['Along the Andes Mountains in South America', 'In what is now Mexico', 'A concept unrelated to ancient civilizations', 'In what is now Canada'], 0),
    ('How old must a Canadian citizen typically be to vote in a federal election?', ['Eighteen or older', 'Any age at all', 'A concept unrelated to elections', 'Only sixteen or older'], 0),
    ('Who does the Governor General represent in Canada?', ['The Crown', 'A single province only', 'A concept unrelated to government', 'A foreign country’s president'], 0),
    ('What does NGO stand for?', ['Non-governmental organization', 'National government office', 'A concept unrelated to organizations', 'New government operation'], 0),
    ('What is the St. Lawrence Seaway a system of?', ['Canals and locks', 'Mountains and valleys', 'A concept unrelated to geography', 'Deserts and dunes'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g4_91_100)
    append_to(4, g4_91_100)
