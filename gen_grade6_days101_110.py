#!/usr/bin/env python3
"""Grade 6, Days 101-110 -- extends Grade 6 from 100 to 110 days. Topics
chosen to avoid any overlap with the existing Day 1-100 set (see
data/grade6.json): direct and indirect (reported) speech, main idea and
supporting details, writing a book review, homophones and commonly
confused word pairs, analyzing memes and internet culture, possessive
nouns and apostrophe use, interviewing techniques, sequencing and
chronological order, writing a diary or journal entry; prime and composite
numbers, rounding decimals, the angle sum of a triangle, area of a
trapezoid, histograms, currency exchange rates, scaling recipe ratios,
speed/distance/time rate problems, complementary probability events; the
lymphatic system, tides, levers and their three classes, coral reefs,
cloud types, tsunamis, bird migration, the greenhouse effect, composting;
the Achaemenid Empire of ancient Persia, land acknowledgements, urban and
rural communities in Canada, the Group of Seven, the October Crisis and
the War Measures Act, Japanese Canadian internment in World War II, the
World Health Organization, Arctic sovereignty, and the Trans-Canada
Highway. Day 110 follows the established every-tenth-day review pattern
(see Day 100), reviewing Days 101-109.

Subject keys for Grade 6 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 6 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
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


def _rebalance_answer_positions(days, seed=20260925):
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


g6_101_110 = [
day(101, [
L('Grammar: Direct and Indirect (Reported) Speech',
  'Grade 6 Language strand: direct speech reports a speaker’s exact words, usually set off by quotation marks, while indirect (reported) speech restates what was said without quotation marks and typically shifts the pronouns and verb tense.',
  [('What does direct speech do?', ['Reports a speaker’s exact words, usually in quotation marks', 'A concept unrelated to grammar', 'Removes all punctuation from a sentence', 'Changes a sentence into a question'], 0),
   ('What does indirect (reported) speech do?', ['Restates what was said without quotation marks', 'Always keeps the exact same words as direct speech', 'A concept unrelated to grammar', 'Removes the subject from a sentence'], 0),
   ('Sam said, I am tired right now is an example of which type of speech?', ['Direct speech', 'Indirect speech', 'A concept unrelated to grammar', 'Neither direct nor indirect speech'], 0),
   ('Which sentence correctly rewrites Sam said, I am tired right now as indirect speech?', ['Sam said that he was tired.', 'Sam said, I am tired right now.', 'Tired right now, said Sam.', 'Sam is saying tired now.'], 0),
   ('Why might a writer choose indirect speech instead of direct speech when summarizing a long conversation?', ['It allows the writer to condense what was said without quoting every exact word', 'Indirect speech always uses more words than direct speech', 'This concept has no connection to grammar', 'Indirect speech requires quotation marks around every sentence'], 0)]),
M('Number Sense: Prime and Composite Numbers',
  'Grade 6 Math strand: a prime number has exactly two factors, 1 and itself, while a composite number has more than two factors; the number 1 is neither prime nor composite.',
  [('What is a prime number?', ['A number with exactly two factors, 1 and itself', 'A number with more than two factors', 'A concept unrelated to number sense', 'A number that is always even'], 0),
   ('What is a composite number?', ['A number with more than two factors', 'A number with exactly two factors', 'A concept unrelated to number sense', 'A number that is always odd'], 0),
   ('Is the number 7 prime or composite?', ['Prime', 'Composite', 'A concept unrelated to number sense', 'Neither prime nor composite'], 0),
   ('Is the number 12 prime or composite?', ['Composite', 'Prime', 'A concept unrelated to number sense', 'Neither prime nor composite'], 0),
   ('Why is the number 2 the only even prime number?', ['Every other even number can be divided evenly by 2, giving it more than two factors', 'Even numbers can never have any factors at all', 'This concept has no connection to number sense', 'All even numbers are prime numbers'], 0)]),
Sc('Science: The Lymphatic System: Fighting Infection and Maintaining Fluid Balance',
   'Grade 6 Science strand: the lymphatic system is a network of vessels and nodes that collects excess fluid from body tissues, filters out harmful substances, and helps the immune system fight infection.',
   [('What does the lymphatic system collect from body tissues?', ['Excess fluid', 'Only bone cells', 'A concept unrelated to the human body', 'Only hair follicles'], 0),
    ('What do lymph nodes help do to harmful substances passing through them?', ['Filter them out', 'Multiply them', 'A concept unrelated to the lymphatic system', 'Turn them into bone'], 0),
    ('Does the lymphatic system help the immune system fight infection?', ['Yes', 'No, the lymphatic system has no role in fighting infection', 'A concept unrelated to the lymphatic system', 'Only the skeletal system fights infection'], 0),
    ('Why might lymph nodes swell when a person has an infection?', ['They are working harder to filter out and fight the germs causing the infection', 'Swelling in lymph nodes never has any connection to infection', 'This concept has no connection to biology', 'Lymph nodes only swell when a person is perfectly healthy'], 0),
    ('Why is it useful for the body to have a system that returns excess fluid from tissues back into the bloodstream?', ['Without it, fluid could build up in tissues and cause swelling and other problems', 'Excess fluid in tissues never causes any problems for the body', 'This concept has no relevance to science', 'The body never has any excess fluid in its tissues'], 0)]),
SS('Social Studies: Ancient Persia: The Achaemenid Empire',
   'Grade 6 Social Studies strand: the Achaemenid Empire of ancient Persia was one of the largest empires in the ancient world, known for its extensive road system, tolerance of local customs, and administrative organization into provinces called satrapies.',
   [('What was the Achaemenid Empire?', ['One of the largest empires in the ancient world, centred in ancient Persia', 'A small city-state with no influence beyond its borders', 'A concept unrelated to ancient history', 'A modern country in North America'], 0),
    ('What were the provinces of the Achaemenid Empire called?', ['Satrapies', 'A concept unrelated to Persian history', 'Boroughs', 'Territories only found in Egypt'], 0),
    ('Was the Achaemenid Empire known for building an extensive road system?', ['Yes', 'No, the empire never built any roads', 'A concept unrelated to ancient Persia', 'Roads were only built much later by other empires'], 0),
    ('Why might tolerating the customs and religions of conquered peoples have helped the Achaemenid Empire stay stable?', ['Allowing local traditions to continue could reduce resistance and rebellion across a large empire', 'Tolerating other customs always made the empire weaker', 'This concept has no connection to ancient history', 'The empire never conquered any other peoples'], 0),
    ('Why might a well-organized road system have been important for governing such a large empire?', ['It allowed messages, soldiers, and goods to move quickly across vast distances', 'Roads never had any effect on how easily an empire could be governed', 'This concept has no relevance to social studies', 'The empire had no need to communicate across its territory'], 0)]),
]),

day(102, [
L('Reading: Identifying Main Idea and Supporting Details',
  'Grade 6 Language strand: the main idea is the central point a text is making, while supporting details are the facts, examples, and explanations that develop and prove that main idea.',
  [('What is the main idea of a text?', ['The central point the text is making', 'A minor detail mentioned only once', 'A concept unrelated to reading', 'The title of the text only'], 0),
   ('What are supporting details?', ['Facts, examples, and explanations that develop the main idea', 'Ideas that contradict the main idea', 'A concept unrelated to reading', 'Random information with no purpose'], 0),
   ('Where is the main idea of a paragraph often found?', ['In the topic sentence, often at the beginning', 'Only in the very last word of the paragraph', 'A concept unrelated to reading', 'Never written anywhere in the paragraph'], 0),
   ('If a paragraph is about the benefits of recycling, which sentence would most likely be a supporting detail?', ['Recycling one aluminum can saves enough energy to run a television for hours.', 'The weather today is sunny.', 'My favourite colour is blue.', 'The store closes at nine.'], 0),
   ('Why is it useful for readers to distinguish between the main idea and supporting details?', ['It helps readers understand what a text is really about instead of getting lost in minor facts', 'Supporting details are always more important than the main idea', 'This concept has no connection to reading comprehension', 'Every sentence in a text is always equally important'], 0)]),
M('Rounding Decimals to a Given Place Value',
  'Grade 6 Math strand: rounding a decimal to a given place value means finding the closest value at that place, using the digit to the right to decide whether to round up or keep the digit the same.',
  [('When rounding, if the digit to the right is 5 or greater, what do you do to the digit being rounded?', ['Round it up by one', 'Round it down by one', 'A concept unrelated to rounding', 'Leave it exactly the same'], 0),
   ('When rounding, if the digit to the right is less than 5, what do you do to the digit being rounded?', ['Leave it the same', 'Round it up by one', 'A concept unrelated to rounding', 'Remove it entirely'], 0),
   ('What is 4.67 rounded to the nearest tenth?', ['4.7', '4.6', '4.0', '5.0'], 0),
   ('What is 12.34 rounded to the nearest whole number?', ['12', '13', '12.3', '12.4'], 0),
   ('Why might a store round prices to the nearest cent instead of using many decimal places?', ['It keeps prices simple and easy for customers to understand and pay', 'Rounding prices never makes them easier to understand', 'This concept has no connection to math', 'Stores never need to display prices with any decimal places'], 0)]),
Sc('Science: Tides: How the Moon and Sun Affect Earth’s Oceans',
   'Grade 6 Science strand: tides are the regular rise and fall of ocean water levels, caused mainly by the gravitational pull of the Moon, with the Sun also playing a smaller role.',
   [('What are tides?', ['The regular rise and fall of ocean water levels', 'A type of ocean current unrelated to gravity', 'A concept unrelated to Earth science', 'A permanent rise in sea level'], 0),
    ('What is the main cause of tides on Earth?', ['The gravitational pull of the Moon', 'The colour of the ocean water', 'A concept unrelated to tides', 'The temperature of the air above the ocean'], 0),
    ('Does the Sun also have an effect on Earth’s tides?', ['Yes, though a smaller effect than the Moon', 'No, the Sun has no effect on tides at all', 'A concept unrelated to tides', 'Only the Sun affects tides, not the Moon'], 0),
    ('Why do most coastal areas experience two high tides and two low tides each day?', ['Earth’s rotation moves different areas through the bulges of water pulled by the Moon’s gravity', 'Tides never follow any kind of regular daily pattern', 'This concept has no connection to Earth science', 'The ocean’s water level never changes throughout the day'], 0),
    ('Why might especially high tides occur when the Sun, Moon, and Earth are aligned?', ['The combined gravitational pull of the Sun and Moon creates a stronger effect on the ocean', 'The Sun and Moon’s gravity always cancel each other out completely', 'This concept has no relevance to science', 'Alignment of the Sun and Moon has no connection to tides'], 0)]),
SS('Social Studies: Land Acknowledgements: Purpose and Practice',
   'Grade 6 Social Studies strand: a land acknowledgement is a statement recognizing the traditional Indigenous territory on which an event or activity takes place, intended to honour Indigenous peoples’ historic and ongoing connection to the land.',
   [('What is a land acknowledgement?', ['A statement recognizing the traditional Indigenous territory of a place', 'A legal document transferring land ownership', 'A concept unrelated to Canadian history', 'A map showing provincial borders'], 0),
    ('What is one purpose of a land acknowledgement?', ['To honour Indigenous peoples’ historic and ongoing connection to the land', 'To erase the history of Indigenous peoples', 'A concept unrelated to land acknowledgements', 'To determine new provincial boundaries'], 0),
    ('Are land acknowledgements often given at the start of public events and school gatherings?', ['Yes', 'No, they are never given at any type of event', 'A concept unrelated to land acknowledgements', 'They are only used in courtrooms'], 0),
    ('Why might learning the name of the traditional territory a school is on be an important step for students?', ['It builds awareness and respect for the Indigenous history connected to that specific place', 'Learning about traditional territory has no connection to Indigenous history', 'This concept has no connection to social studies', 'Every school in Canada is built on the exact same territory'], 0),
    ('Why do some people say a land acknowledgement should be paired with meaningful action, not just words?', ['Genuine respect and reconciliation involve ongoing effort, not only a spoken statement', 'A spoken acknowledgement always accomplishes everything on its own', 'This concept has no relevance to social studies', 'Land acknowledgements have no connection to reconciliation'], 0)]),
]),

day(103, [
L('Writing: Writing a Book Review',
  'Grade 6 Language strand: a book review summarizes a text without revealing major plot twists, evaluates its strengths and weaknesses, and gives the reviewer’s opinion supported by specific examples from the book.',
  [('What does a book review typically include?', ['A summary, an evaluation, and the reviewer’s supported opinion', 'Only a list of characters’ names', 'A concept unrelated to writing', 'A word-for-word copy of the book’s first chapter'], 0),
   ('Should a book review reveal major plot twists or the ending?', ['No, it should generally avoid spoiling major twists or the ending', 'Yes, a review must always reveal the entire ending', 'A concept unrelated to book reviews', 'Book reviews never contain any information about the plot'], 0),
   ('Why should a book review include specific examples from the text?', ['Examples help support and prove the reviewer’s opinions', 'Examples are never necessary in a book review', 'A concept unrelated to writing', 'A review should never mention anything from the actual book'], 0),
   ('Which sentence sounds most like it belongs in a book review?', ['The pacing in the middle chapters felt slow, but the ending made up for it.', 'The bus arrives at eight in the morning.', 'Water boils at 100 degrees Celsius.', 'The store is having a sale this weekend.'], 0),
   ('Why might a reviewer’s personal opinion still be considered valuable even though other readers might disagree?', ['A well-supported opinion can still give useful insight, even if not everyone shares the same view', 'Opinions in a review are never useful to other readers', 'This concept has no connection to writing', 'A book review must always match every other reader’s opinion exactly'], 0)]),
M('Geometry: The Angle Sum of a Triangle',
  'Grade 6 Math strand: the three interior angles of any triangle always add up to 180 degrees, a fact that can be used to find a missing angle when the other two are known.',
  [('What do the three interior angles of any triangle always add up to?', ['180 degrees', '360 degrees', '90 degrees', '270 degrees'], 0),
   ('If a triangle has angles of 60 degrees and 70 degrees, what is the measure of the third angle?', ['50 degrees', '60 degrees', '70 degrees', '40 degrees'], 0),
   ('If a triangle has one angle measuring 90 degrees, what do the other two angles add up to?', ['90 degrees', '180 degrees', '270 degrees', '45 degrees'], 0),
   ('Can a triangle have two angles that each measure 100 degrees?', ['No, because the angles would add up to more than 180 degrees', 'Yes, this is a completely normal triangle', 'A concept unrelated to geometry', 'Triangles never have a limit on their angle measures'], 0),
   ('Why is knowing that a triangle’s angles always sum to 180 degrees useful for solving geometry problems?', ['It allows you to calculate a missing angle when the other two angles are known', 'This rule never helps solve any kind of geometry problem', 'This concept has no connection to math', 'The angles of a triangle can add up to any number at all'], 0)]),
Sc('Science: Levers: The Three Classes and Their Mechanical Advantage',
   'Grade 6 Science strand: a lever is a simple machine made of a rigid bar that pivots on a fixed point called a fulcrum, and levers are classified into three classes based on the relative positions of the fulcrum, the effort, and the load.',
   [('What is a lever?', ['A simple machine made of a rigid bar that pivots on a fulcrum', 'A machine that only spins in circles', 'A concept unrelated to simple machines', 'A tool used only for cutting'], 0),
    ('What is the fixed point that a lever pivots on called?', ['The fulcrum', 'The load', 'A concept unrelated to levers', 'The effort'], 0),
    ('How many classes of levers are there, based on the positions of the fulcrum, effort, and load?', ['Three', 'Two', 'A concept unrelated to levers', 'Five'], 0),
    ('In a first-class lever, such as a see-saw, where is the fulcrum located?', ['Between the effort and the load', 'At one end, with the effort in the middle', 'A concept unrelated to levers', 'There is no fulcrum in a first-class lever'], 0),
    ('Why might using a lever make it easier to lift a heavy object?', ['A lever can multiply the force applied, allowing a smaller effort to move a larger load', 'Levers never make lifting a heavy object any easier', 'This concept has no relevance to science', 'A lever always requires more force than lifting an object directly'], 0)]),
SS('Social Studies: Urban and Rural Communities in Canada',
   'Grade 6 Social Studies strand: urban communities are densely populated areas such as cities with many services close together, while rural communities are less densely populated areas often centred around farming or resource industries, and each type of community faces different opportunities and challenges.',
   [('What is an urban community?', ['A densely populated area, such as a city', 'A sparsely populated farming area', 'A concept unrelated to Canadian geography', 'A community with no people at all'], 0),
    ('What is a rural community?', ['A less densely populated area, often centred around farming or resource industries', 'A densely populated downtown city core', 'A concept unrelated to communities', 'A community found only underwater'], 0),
    ('Are services like hospitals and public transit typically closer together in urban areas?', ['Yes', 'No, services are always farther apart in cities', 'A concept unrelated to urban communities', 'Cities never have any public services'], 0),
    ('Why might people living in a rural community need to travel farther to access certain services, like a large hospital?', ['Rural areas have lower population density, so specialized services are often located farther apart', 'Rural communities always have more services than cities', 'This concept has no connection to social studies', 'Services are distributed identically in every community type'], 0),
    ('Why might understanding the differences between urban and rural communities help with planning things like infrastructure and services?', ['Different communities have different needs, so planning should reflect those differences', 'Every community in Canada has identical needs regardless of location', 'This concept has no relevance to social studies', 'Infrastructure planning never considers where people live'], 0)]),
]),

day(104, [
L('Vocabulary: Homophones and Commonly Confused Word Pairs',
  'Grade 6 Language strand: homophones are words that sound the same but have different spellings and meanings, such as their, there, and they’re, and recognizing them helps writers choose the correct word for their meaning.',
  [('What are homophones?', ['Words that sound the same but have different spellings and meanings', 'Words that are spelled the same but sound different', 'A concept unrelated to vocabulary', 'Words that mean the exact same thing'], 0),
   ('Which group of words are homophones of each other?', ['Their, there, they’re', 'Happy, sad, angry', 'Run, jump, walk', 'Blue, green, red'], 0),
   ('Which sentence uses the correct homophone? The books belong ___ the students.', ['to', 'too', 'two', 'A concept unrelated to homophones'], 0),
   ('Which sentence uses the correct homophone? ___ going to the store later today.', ['They’re', 'Their', 'There', 'A concept unrelated to homophones'], 0),
   ('Why is it important for writers to choose the correct homophone when writing?', ['Using the wrong homophone can confuse readers or change the meaning of a sentence', 'Homophones never affect how a reader understands a sentence', 'This concept has no connection to vocabulary', 'All homophones can be used interchangeably with no difference in meaning'], 0)]),
M('Geometry: Area of a Trapezoid',
  'Grade 6 Math strand: the area of a trapezoid is found using the formula one half times the sum of the two parallel sides, called bases, multiplied by the height between them.',
  [('What shape has exactly one pair of parallel sides, called bases?', ['A trapezoid', 'A square', 'A concept unrelated to geometry', 'A circle'], 0),
   ('What is the formula for the area of a trapezoid?', ['One half times the sum of the two bases, times the height', 'Length times width', 'Side times side', 'Base times height only, with no other terms'], 0),
   ('If a trapezoid has bases of 6 and 10 and a height of 4, what is its area?', ['32', '40', '60', '16'], 0),
   ('In the trapezoid area formula, what does the height measure?', ['The perpendicular distance between the two parallel bases', 'The length of the longer base only', 'A concept unrelated to trapezoids', 'The total perimeter of the shape'], 0),
   ('Why does the trapezoid area formula add the two bases together before multiplying?', ['Averaging the two parallel side lengths accounts for the shape’s sloped, non-parallel sides', 'Adding the bases together never has any effect on finding the area', 'This concept has no connection to math', 'A trapezoid’s area only depends on its height, not its bases'], 0)]),
Sc('Science: Coral Reefs: Biodiversity Hotspots Under Threat',
   'Grade 6 Science strand: coral reefs are built by tiny animals called coral polyps and support an enormous diversity of marine life, but they are threatened by rising ocean temperatures, pollution, and ocean acidification.',
   [('What builds a coral reef?', ['Tiny animals called coral polyps', 'Large fish swimming in groups', 'A concept unrelated to marine biology', 'Plants growing on the ocean floor'], 0),
    ('Why are coral reefs described as biodiversity hotspots?', ['They support an enormous diversity of marine life', 'They contain almost no living organisms', 'A concept unrelated to coral reefs', 'Biodiversity has no connection to coral reefs'], 0),
    ('Name one threat facing coral reefs today, such as rising ocean temperatures.', ['Rising ocean temperatures', 'A concept unrelated to coral reefs', 'Coral reefs face no threats at all', 'Too much cold water only'], 0),
    ('What is coral bleaching, which can occur when ocean water becomes too warm?', ['When stressed coral expels the colourful algae living inside it, turning white', 'When coral grows extra colourful algae', 'A concept unrelated to coral reefs', 'When coral polyps multiply rapidly in warm water'], 0),
    ('Why might protecting coral reefs be important for both ocean life and coastal communities?', ['Reefs provide habitat for countless species and can also protect shorelines from strong waves', 'Coral reefs have no connection to any other living things or communities', 'This concept has no relevance to science', 'Coral reefs provide no benefit to anything outside the reef itself'], 0)]),
SS('Social Studies: The Group of Seven and Canadian Artistic Identity',
   'Grade 6 Social Studies strand: the Group of Seven was a collective of Canadian landscape painters in the early twentieth century whose bold depictions of the Canadian wilderness helped shape a distinct sense of Canadian artistic identity.',
   [('What was the Group of Seven?', ['A collective of Canadian landscape painters', 'A group of Canadian hockey players', 'A concept unrelated to Canadian history', 'A political party in early Canada'], 0),
    ('What did the Group of Seven mainly paint?', ['The Canadian wilderness and landscapes', 'Portraits of European royalty', 'A concept unrelated to the Group of Seven', 'City skylines outside of Canada'], 0),
    ('Did the Group of Seven’s work help shape a distinct Canadian artistic identity?', ['Yes', 'No, their work had no connection to Canadian identity', 'A concept unrelated to Canadian art', 'They only painted subjects from outside Canada'], 0),
    ('Why might the Group of Seven have chosen to paint the rugged Canadian landscape instead of following European artistic traditions?', ['They wanted to create art that reflected Canada’s own unique natural environment and identity', 'They were required by law to paint only landscapes', 'This concept has no connection to social studies', 'European artistic traditions had no influence on any Canadian painters'], 0),
    ('Why is studying artists like the Group of Seven considered part of understanding Canadian heritage and identity?', ['Art can reflect and shape how a country understands and represents itself', 'Art has no connection to a country’s heritage or identity', 'This concept has no relevance to social studies', 'The Group of Seven’s paintings had no lasting influence on Canadian culture'], 0)]),
]),

day(105, [
L('Media Literacy: Analyzing Memes and Internet Culture',
  'Grade 6 Language strand: a meme is an image, video, or piece of text, often humorous, that spreads rapidly online and is frequently remixed, and analyzing memes critically helps readers consider their intended message, audience, and possible bias.',
  [('What is a meme?', ['An image, video, or piece of text that spreads rapidly online, often humorous', 'A formal news article written by a journalist', 'A concept unrelated to media literacy', 'A type of textbook used in schools'], 0),
   ('Are memes often remixed or changed as they spread online?', ['Yes', 'No, memes are never changed once they are created', 'A concept unrelated to memes', 'Memes can only ever be viewed once and then disappear'], 0),
   ('Why might it be important to think critically about a meme’s intended message?', ['Memes can shape opinions quickly, even if the information in them is not accurate', 'Memes never contain any kind of message or opinion', 'A concept unrelated to media literacy', 'Every meme is always completely accurate and unbiased'], 0),
   ('Why might a meme spread faster than a lengthy news article?', ['Memes are often short, visual, and easy to quickly share and understand', 'Memes always take longer to read than full news articles', 'This concept has no connection to media literacy', 'News articles are never shared online'], 0),
   ('Why should readers consider the original source of a meme before believing its message?', ['A meme’s creator may have a particular bias or agenda that shapes the message', 'The source of a meme never affects how trustworthy it is', 'This concept has no relevance to media literacy', 'Memes are always created by official news organizations'], 0)]),
M('Data Management: Constructing and Interpreting Histograms',
  'Grade 6 Math strand: a histogram is a type of bar graph that displays the frequency of numerical data grouped into equal intervals, with bars touching to show that the data is continuous.',
  [('What does a histogram display?', ['The frequency of numerical data grouped into equal intervals', 'Only the names of categories with no numerical data', 'A concept unrelated to data management', 'The exact location of each data point on a map'], 0),
   ('In a histogram, do the bars typically touch each other?', ['Yes, to show the data is continuous', 'No, there is always a gap between every bar', 'A concept unrelated to histograms', 'Bars in a histogram are never used at all'], 0),
   ('What must the intervals, or groups, in a histogram be?', ['Equal in size', 'Random and unequal in size', 'A concept unrelated to histograms', 'Always exactly one unit wide'], 0),
   ('If a histogram shows the tallest bar for the interval 10 to 19 years old, what does this suggest?', ['More data values fall within that age range than any other', 'No data values fall within that age range', 'A concept unrelated to histograms', 'Every age range has the exact same number of data values'], 0),
   ('Why might a histogram be more useful than a simple list of numbers for understanding a large data set?', ['It visually shows the distribution and patterns in the data at a glance', 'Histograms never help show any patterns in data', 'This concept has no connection to data management', 'A list of numbers always shows patterns more clearly than any graph'], 0)]),
Sc('Science: Cloud Types and Reading the Sky for Weather Clues',
   'Grade 6 Science strand: clouds form when water vapour condenses in the atmosphere, and different cloud types, such as puffy cumulus clouds, wispy cirrus clouds, and flat stratus clouds, can give clues about upcoming weather.',
   [('What causes clouds to form?', ['Water vapour condensing in the atmosphere', 'Rocks breaking down on the ground', 'A concept unrelated to weather', 'The ocean freezing completely'], 0),
    ('What are puffy, cotton-like clouds usually called?', ['Cumulus clouds', 'Cirrus clouds', 'A concept unrelated to cloud types', 'Stratus clouds'], 0),
    ('What are thin, wispy, high-altitude clouds usually called?', ['Cirrus clouds', 'Cumulus clouds', 'A concept unrelated to cloud types', 'Stratus clouds'], 0),
    ('What are flat, grey clouds that often cover the whole sky usually called?', ['Stratus clouds', 'Cumulus clouds', 'A concept unrelated to cloud types', 'Cirrus clouds'], 0),
    ('Why might tall, dark cumulonimbus clouds signal that a thunderstorm is approaching?', ['These clouds form from strong upward air currents that also produce heavy rain and lightning', 'These clouds are always a sign of clear, sunny weather', 'This concept has no connection to science', 'Cloud shape never gives any clue about upcoming weather'], 0)]),
SS('Social Studies: The October Crisis and the War Measures Act',
   'Grade 6 Social Studies strand: the October Crisis of 1970 was a period of political turmoil in Quebec involving kidnappings by a militant group, leading the federal government to invoke the War Measures Act, which temporarily suspended certain civil liberties.',
   [('In what decade did the October Crisis take place?', ['The 1970s', 'The 1920s', 'A concept unrelated to Canadian history', 'The 1990s'], 0),
    ('What Canadian province was at the centre of the October Crisis?', ['Quebec', 'British Columbia', 'A concept unrelated to the October Crisis', 'Nova Scotia'], 0),
    ('What federal law did the government invoke during the October Crisis?', ['The War Measures Act', 'The Multiculturalism Act', 'A concept unrelated to the October Crisis', 'The Constitution Act'], 0),
    ('Why was the government’s use of the War Measures Act controversial?', ['It temporarily suspended certain civil liberties, such as the right to be free from arrest without charge', 'The Act had no real effect on anyone’s rights', 'This concept has no connection to Canadian history', 'The Act was never actually used during the crisis'], 0),
    ('Why do historians still debate the government’s response to the October Crisis today?', ['People weigh differently the need for public safety against the importance of protecting civil liberties', 'No one has ever discussed the government’s response to the crisis', 'This concept has no relevance to social studies', 'The events of the October Crisis had no lasting impact on Canada'], 0)]),
]),

day(106, [
L('Grammar: Possessive Nouns and Apostrophe Use',
  'Grade 6 Language strand: a possessive noun shows ownership, formed by adding an apostrophe and s to a singular noun (the dog’s bone) or just an apostrophe to a plural noun ending in s (the dogs’ bones).',
  [('What does a possessive noun show?', ['Ownership', 'A question', 'A concept unrelated to grammar', 'A negative statement'], 0),
   ('How do you usually make a singular noun possessive?', ['Add an apostrophe and s', 'Add only an s', 'A concept unrelated to grammar', 'Add an apostrophe only, with no s'], 0),
   ('How do you usually make a plural noun that already ends in s possessive?', ['Add only an apostrophe', 'Add an apostrophe and another s', 'A concept unrelated to grammar', 'Remove the s entirely'], 0),
   ('Which sentence correctly uses a possessive noun?', ['The dog’s bone is buried in the yard.', 'The dogs bone is buried in the yard.', 'The dog bones is buried in the yard.', 'The dog’ bone is buried in the yard.'], 0),
   ('Why might mixing up its and it’s be a common grammar mistake for writers?', ['It’s is a contraction of it is, while its shows possession, and the words sound identical', 'These two words are never confused by writers', 'This concept has no connection to grammar', 'Its and it’s always mean exactly the same thing'], 0)]),
M('Financial Literacy: Understanding Currency Exchange Rates',
  'Grade 6 Math strand: a currency exchange rate tells you how much one country’s currency is worth in terms of another, and multiplying an amount by the exchange rate lets you convert between currencies.',
  [('What does a currency exchange rate tell you?', ['How much one country’s currency is worth in terms of another', 'The total population of a country', 'A concept unrelated to financial literacy', 'The exact price of every item in a store'], 0),
   ('If the exchange rate is 1 Canadian dollar equals 0.75 US dollars, how many US dollars would 10 Canadian dollars be worth?', ['7.50 US dollars', '10.75 US dollars', '13.30 US dollars', '0.75 US dollars'], 0),
   ('To convert an amount of money to another currency, what do you typically do with the exchange rate?', ['Multiply the amount by the exchange rate', 'Always subtract the exchange rate', 'A concept unrelated to currency exchange', 'Ignore the exchange rate completely'], 0),
   ('Do exchange rates between currencies stay exactly the same forever?', ['No, they can change daily based on economic factors', 'Yes, exchange rates never change once they are set', 'A concept unrelated to exchange rates', 'Exchange rates are only updated once every ten years'], 0),
   ('Why might a Canadian family planning a trip abroad want to check the current exchange rate before they go?', ['It helps them understand how much their money will actually be worth in the country they are visiting', 'Exchange rates never affect how much a traveller can buy abroad', 'This concept has no connection to financial literacy', 'Every country in the world uses the exact same currency'], 0)]),
Sc('Science: Tsunamis: Causes and Effects',
   'Grade 6 Science strand: a tsunami is a series of powerful ocean waves usually triggered by an underwater earthquake, volcanic eruption, or landslide, capable of causing severe flooding and damage when it reaches shore.',
   [('What is a tsunami?', ['A series of powerful ocean waves', 'A type of desert sandstorm', 'A concept unrelated to Earth science', 'A slow-moving glacier'], 0),
    ('What commonly triggers a tsunami?', ['An underwater earthquake', 'A sudden drop in air temperature', 'A concept unrelated to tsunamis', 'A change in the colour of the ocean'], 0),
    ('Can a volcanic eruption also trigger a tsunami?', ['Yes', 'No, only earthquakes can ever trigger a tsunami', 'A concept unrelated to tsunamis', 'Volcanoes have no connection to the ocean'], 0),
    ('Why can a tsunami cause severe flooding when it reaches shore?', ['The wave can carry an enormous amount of water onto the land very quickly', 'Tsunami waves are always smaller than normal ocean waves', 'This concept has no connection to Earth science', 'Tsunamis never actually reach the shore'], 0),
    ('Why do coastal communities in earthquake-prone regions often have tsunami warning systems?', ['Early warning can give people time to move to higher ground before a tsunami arrives', 'Warning systems never provide any useful information about tsunamis', 'This concept has no relevance to science', 'Tsunamis always happen with no warning signs beforehand'], 0)]),
SS('Social Studies: Japanese Canadian Internment During World War II',
   'Grade 6 Social Studies strand: during World War II, the Canadian government forcibly relocated and interned thousands of Japanese Canadians, seizing their property, in a policy now recognized as a serious violation of their rights.',
   [('During which conflict were Japanese Canadians forcibly interned by the Canadian government?', ['World War II', 'World War I', 'A concept unrelated to Canadian history', 'The Cold War'], 0),
    ('What happened to the property of many interned Japanese Canadians?', ['It was seized by the government', 'It was carefully protected and returned immediately', 'A concept unrelated to internment', 'It was left completely untouched'], 0),
    ('Is the internment of Japanese Canadians now recognized as a violation of their rights?', ['Yes', 'No, it is considered to have been entirely justified', 'A concept unrelated to Japanese Canadian history', 'This event never actually happened'], 0),
    ('Why might the Canadian government’s wartime fears have led to unjust treatment of Japanese Canadians?', ['Fear and prejudice during wartime led to policies that violated the rights of an entire community based on ancestry', 'The government’s actions had no connection to fear or prejudice', 'This concept has no connection to Canadian history', 'Japanese Canadians were treated exactly the same as all other Canadians during the war'], 0),
    ('Why is it important for students to learn about historical injustices like Japanese Canadian internment?', ['Understanding past injustices can help prevent similar mistakes and support reconciliation efforts', 'Learning about past injustices serves no purpose today', 'This concept has no relevance to social studies', 'This event has no connection to how Canada addresses rights today'], 0)]),
]),

day(107, [
L('Oral Communication: Effective Interviewing Techniques',
  'Grade 6 Language strand: effective interviewing involves preparing open-ended questions in advance, listening actively to responses, and asking thoughtful follow-up questions to gather detailed information from the person being interviewed.',
  [('What type of questions should be prepared in advance for an effective interview?', ['Open-ended questions', 'Questions that can only be answered with yes or no', 'A concept unrelated to oral communication', 'No questions should ever be prepared in advance'], 0),
   ('Why is active listening important during an interview?', ['It helps the interviewer respond thoughtfully and ask good follow-up questions', 'Active listening never affects the quality of an interview', 'A concept unrelated to interviewing', 'Interviewers should never listen to the person’s answers'], 0),
   ('What is a follow-up question?', ['A question that digs deeper into a previous answer', 'The very first question asked in an interview', 'A concept unrelated to interviewing', 'A question that has nothing to do with the topic'], 0),
   ('Which of these is most likely an open-ended interview question?', ['What was the most challenging part of training for the competition?', 'Did you compete?', 'Are you tired?', 'Is it Tuesday?'], 0),
   ('Why might preparing questions in advance still leave room for spontaneous follow-up questions during an interview?', ['Unexpected or interesting answers may lead to new questions that were not planned beforehand', 'An interview should never include any questions beyond the ones prepared in advance', 'This concept has no connection to oral communication', 'Follow-up questions are never useful during an interview'], 0)]),
M('Ratios in Recipes: Scaling Quantities Up and Down',
  'Grade 6 Math strand: scaling a recipe means multiplying every ingredient amount by the same ratio to increase or decrease the number of servings while keeping the proportions the same.',
  [('What does it mean to scale a recipe?', ['To multiply every ingredient amount by the same ratio to change the number of servings', 'To change only one ingredient while keeping the others the same', 'A concept unrelated to ratios', 'To remove all measurements from the recipe'], 0),
   ('If a recipe for 4 servings needs 2 cups of flour, how much flour is needed to make 8 servings?', ['4 cups', '2 cups', '6 cups', '8 cups'], 0),
   ('If a recipe for 6 servings needs 3 eggs, how many eggs are needed for 2 servings?', ['1 egg', '2 eggs', '3 eggs', '6 eggs'], 0),
   ('Why must every ingredient be scaled by the same ratio when adjusting a recipe’s serving size?', ['Changing the ratio between ingredients would alter the taste and texture of the final dish', 'Ingredients never need to be scaled by the same amount', 'This concept has no connection to math', 'A recipe’s proportions never affect how it turns out'], 0),
   ('Why is understanding ratios useful when doubling or halving a recipe for a family gathering?', ['It ensures the dish keeps the same flavour and texture no matter how many servings are made', 'Ratios have no real-world application in cooking', 'This concept has no relevance to math', 'A recipe always tastes the same no matter how the ingredients are adjusted'], 0)]),
Sc('Science: Bird Migration: Navigation and Survival',
   'Grade 6 Science strand: many bird species migrate long distances each year to find better food sources and nesting conditions, using cues such as the position of the sun and stars, Earth’s magnetic field, and landmarks to navigate.',
   [('Why do many bird species migrate?', ['To find better food sources and nesting conditions', 'To avoid ever having to build a nest', 'A concept unrelated to bird behaviour', 'Migration serves no purpose for birds'], 0),
    ('Name one cue that migrating birds may use to navigate, such as the position of the sun.', ['The position of the sun', 'A concept unrelated to bird migration', 'The colour of the ocean', 'The taste of the water'], 0),
    ('Can migrating birds use Earth’s magnetic field to help them navigate?', ['Yes', 'No, birds have no way of sensing Earth’s magnetic field', 'A concept unrelated to bird migration', 'Only fish can sense Earth’s magnetic field'], 0),
    ('Why might birds that migrate in large flocks have a survival advantage over birds that migrate alone?', ['Travelling in a flock can help birds conserve energy and better watch for predators', 'Flying in a flock never provides any benefit to migrating birds', 'This concept has no connection to biology', 'Birds that migrate alone always survive better than those in flocks'], 0),
    ('Why might climate change and habitat loss pose a serious threat to migratory bird species?', ['These changes can disrupt the food sources and stopover habitats birds depend on during their journey', 'Migratory birds are never affected by changes to their environment', 'This concept has no relevance to science', 'Bird migration routes never depend on environmental conditions'], 0)]),
SS('Social Studies: The World Health Organization and Global Health',
   'Grade 6 Social Studies strand: the World Health Organization is an agency of the United Nations that works to coordinate international responses to health emergencies, promote disease prevention, and improve health outcomes worldwide.',
   [('What is the World Health Organization an agency of?', ['The United Nations', 'A single country’s government', 'A concept unrelated to global health', 'A private for-profit company'], 0),
    ('What is one goal of the World Health Organization?', ['Coordinating international responses to health emergencies', 'Preventing all countries from communicating about health issues', 'A concept unrelated to global health', 'Increasing the spread of disease worldwide'], 0),
    ('Does the World Health Organization work with countries around the world on disease prevention?', ['Yes', 'No, it only works within a single country', 'A concept unrelated to the World Health Organization', 'The organization has no connection to disease prevention'], 0),
    ('Why might it be important for countries to cooperate through an organization like the World Health Organization during a global health emergency?', ['Diseases can spread across borders, so a coordinated international response can be more effective', 'Diseases never spread beyond the borders of a single country', 'This concept has no connection to social studies', 'Countries never benefit from cooperating on health issues'], 0),
    ('Why might the World Health Organization also focus on long-term goals, like improving access to clean water and vaccines?', ['Preventing illness before it starts can improve health outcomes more effectively than only treating emergencies', 'Preventing illness has no connection to improving global health', 'This concept has no relevance to social studies', 'Access to clean water and vaccines has no effect on public health'], 0)]),
]),

day(108, [
L('Reading: Sequencing Events and Chronological Order',
  'Grade 6 Language strand: sequencing means identifying the order in which events happen in a text, and chronological order arranges events from earliest to latest using clues like dates, time words, and transitions.',
  [('What does sequencing mean in reading?', ['Identifying the order in which events happen', 'Identifying the setting of a story', 'A concept unrelated to reading', 'Identifying the main character of a story'], 0),
   ('What does chronological order arrange events by?', ['From earliest to latest', 'From least to most important', 'A concept unrelated to sequencing', 'In a completely random order'], 0),
   ('Which of these is a time word or transition that signals sequence, such as first, next, or finally?', ['Next', 'A concept unrelated to sequencing', 'Blue', 'Happy'], 0),
   ('Why might a recipe or set of instructions typically be written in chronological order?', ['Following the steps in the correct order is necessary for the task to work correctly', 'The order of steps in instructions never matters', 'This concept has no connection to reading comprehension', 'Instructions are usually written with no particular order at all'], 0),
   ('Why might an author choose to tell a story out of chronological order, using flashbacks, instead of a straightforward sequence?', ['It can build suspense or reveal important background information at a strategic moment', 'Telling a story out of order never has any effect on the reader', 'This concept has no relevance to reading comprehension', 'All stories must always be told in strict chronological order'], 0)]),
M('Rate Problems: Speed, Distance, and Time',
  'Grade 6 Math strand: speed is a rate that compares distance travelled to the time it takes, calculated using the formula speed equals distance divided by time, which can be rearranged to solve for distance or time.',
  [('What is speed?', ['A rate that compares distance travelled to time', 'The total distance travelled with no reference to time', 'A concept unrelated to rates', 'The total time spent travelling with no reference to distance'], 0),
   ('What is the formula for speed?', ['Speed equals distance divided by time', 'Speed equals time divided by distance', 'Speed equals distance times time', 'A concept unrelated to rate problems'], 0),
   ('If a car travels 150 kilometres in 3 hours, what is its speed?', ['50 kilometres per hour', '450 kilometres per hour', '3 kilometres per hour', '147 kilometres per hour'], 0),
   ('If a cyclist travels at 20 kilometres per hour for 2 hours, how far do they travel?', ['40 kilometres', '20 kilometres', '10 kilometres', '22 kilometres'], 0),
   ('Why is understanding rates like speed useful for planning a road trip?', ['It helps estimate how long a journey will take based on the distance and expected speed', 'Speed has no connection to how long a trip will take', 'This concept has no connection to math', 'Distance and time are never related to each other in any way'], 0)]),
Sc('Science: The Greenhouse Effect and Global Warming',
   'Grade 6 Science strand: the greenhouse effect occurs when gases in the atmosphere, such as carbon dioxide, trap heat from the sun near Earth’s surface, and human activities that increase these gases are contributing to global warming.',
   [('What does the greenhouse effect do?', ['Traps heat from the sun near Earth’s surface', 'Cools Earth’s surface rapidly', 'A concept unrelated to Earth science', 'Removes all heat from the atmosphere'], 0),
    ('Name one gas that contributes to the greenhouse effect, such as carbon dioxide.', ['Carbon dioxide', 'A concept unrelated to the greenhouse effect', 'Pure oxygen only', 'Only water in its solid form'], 0),
    ('Are human activities, such as burning fossil fuels, increasing the amount of greenhouse gases in the atmosphere?', ['Yes', 'No, human activities have no effect on greenhouse gases', 'A concept unrelated to global warming', 'Greenhouse gases can never increase in the atmosphere'], 0),
    ('Why is the greenhouse effect itself considered a naturally necessary process for life on Earth?', ['Without any greenhouse effect, Earth would be far too cold to support most life', 'The greenhouse effect has never had any role in keeping Earth warm', 'This concept has no connection to science', 'Earth would be exactly the same temperature with no atmosphere at all'], 0),
    ('Why are scientists concerned about the enhanced greenhouse effect caused by human activity?', ['Extra greenhouse gases trap additional heat, contributing to rising global temperatures and climate change', 'Extra greenhouse gases have no effect on global temperatures', 'This concept has no relevance to science', 'Global temperatures never change no matter the amount of greenhouse gases'], 0)]),
SS('Social Studies: Arctic Sovereignty and a Changing North',
   'Grade 6 Social Studies strand: Arctic sovereignty refers to a country’s recognized authority over its northern territories and waters, an issue of growing importance for Canada as melting sea ice opens new shipping routes and raises questions about resource access.',
   [('What does Arctic sovereignty refer to?', ['A country’s recognized authority over its northern territories and waters', 'A treaty about ocean fishing only', 'A concept unrelated to Canadian geography', 'A type of Arctic wildlife'], 0),
    ('Why has Arctic sovereignty become a more prominent issue in recent years?', ['Melting sea ice is opening new shipping routes and access to resources', 'The Arctic has become colder and completely inaccessible', 'A concept unrelated to Arctic sovereignty', 'Interest in the Arctic has completely disappeared'], 0),
    ('Does Canada claim sovereignty over parts of the Arctic?', ['Yes', 'No, Canada has no territory in the Arctic', 'A concept unrelated to Canadian geography', 'Canada has given up all claims to northern territory'], 0),
    ('Why might new Arctic shipping routes created by melting sea ice raise questions between different countries?', ['Multiple countries may have different views on who controls or can use these newly accessible waters', 'New shipping routes have no connection to questions of ownership or control', 'This concept has no connection to social studies', 'Only one country has ever shown any interest in the Arctic'], 0),
    ('Why might Indigenous communities in the North have an important perspective on decisions about Arctic sovereignty and development?', ['They have long-standing knowledge of and connections to the land that can inform sustainable decision-making', 'Indigenous communities have no connection to the Arctic region', 'This concept has no relevance to social studies', 'Decisions about the Arctic never affect the people who live there'], 0)]),
]),

day(109, [
L('Writing: Writing a Diary or Journal Entry',
  'Grade 6 Language strand: a diary or journal entry is a personal, first-person reflection on events and feelings, often dated, that allows a writer to explore their thoughts in an informal, honest voice.',
  [('What point of view is typically used in a diary or journal entry?', ['First person', 'Third person', 'A concept unrelated to writing', 'Second person'], 0),
   ('What do diary and journal entries usually include at the top?', ['A date', 'A bibliography', 'A concept unrelated to journal writing', 'A table of contents'], 0),
   ('Is the tone of a diary entry usually formal or informal?', ['Informal', 'Always extremely formal', 'A concept unrelated to diary writing', 'Diary entries never have any particular tone'], 0),
   ('Which sentence sounds most like it belongs in a diary entry?', ['Dear diary, today was such a strange and exciting day, I can barely believe it happened.', 'The report outlines quarterly sales figures for the company.', 'This textbook chapter covers the water cycle.', 'The recipe requires two cups of sugar.'], 0),
   ('Why might writing in a diary help someone process their thoughts and feelings about an event?', ['Putting thoughts into words can help a person reflect on and better understand their own experiences', 'Writing about an event never helps a person understand their feelings', 'This concept has no connection to writing', 'Diaries are only ever used to record facts with no personal reflection'], 0)]),
M('Probability: Complementary Events',
  'Grade 6 Math strand: two events are complementary if together they cover all possible outcomes and cannot both happen at the same time, so their probabilities always add up to 1, or 100 percent.',
  [('What does it mean for two events to be complementary?', ['Together they cover all possible outcomes and cannot both happen at once', 'They can both happen at exactly the same time', 'A concept unrelated to probability', 'They never have any connection to each other'], 0),
   ('What do the probabilities of two complementary events always add up to?', ['1, or 100 percent', '0', '2', 'A concept unrelated to complementary events'], 0),
   ('If the probability of rain tomorrow is 30 percent, what is the probability that it will not rain?', ['70 percent', '30 percent', '100 percent', '0 percent'], 0),
   ('Are rolling an even number and rolling an odd number on a standard die complementary events?', ['Yes', 'No, these events are unrelated', 'A concept unrelated to probability', 'These events can happen at the same time'], 0),
   ('Why is the concept of complementary events useful when calculating probability?', ['If you know the probability of one event, you can quickly find the probability of it not happening', 'Complementary events never help with calculating probability', 'This concept has no connection to math', 'The probabilities of complementary events are never related to each other'], 0)]),
Sc('Science: Composting: Turning Waste into Soil Nutrients',
   'Grade 6 Science strand: composting is the natural process by which decomposers such as bacteria, fungi, and worms break down organic waste like food scraps and yard trimmings into nutrient-rich soil.',
   [('What is composting?', ['The natural process of breaking down organic waste into nutrient-rich soil', 'A process that destroys all organic material with no result', 'A concept unrelated to science', 'A method of freezing food waste indefinitely'], 0),
    ('Name one type of decomposer involved in composting, such as bacteria or worms.', ['Bacteria', 'A concept unrelated to composting', 'Only metal objects', 'Only plastic materials'], 0),
    ('Name one type of material that can typically be composted, such as food scraps.', ['Food scraps', 'A concept unrelated to composting', 'Glass bottles', 'Metal cans'], 0),
    ('Why might adding compost to garden soil help plants grow better?', ['Compost adds nutrients that enrich the soil and support healthy plant growth', 'Compost removes all nutrients from soil', 'This concept has no connection to biology', 'Compost has no effect on how well plants grow'], 0),
    ('Why is composting considered a beneficial alternative to sending food waste to a landfill?', ['It recycles nutrients back into the soil instead of letting waste take up space and produce landfill gases', 'Composting always produces more waste than sending it to a landfill', 'This concept has no relevance to science', 'Food waste in a landfill provides the exact same benefit as composting'], 0)]),
SS('Social Studies: The Trans-Canada Highway and National Infrastructure',
   'Grade 6 Social Studies strand: the Trans-Canada Highway is a highway system stretching across all ten provinces, completed in the 1960s, that improved transportation, trade, and connections between communities across the country.',
   [('What is the Trans-Canada Highway?', ['A highway system stretching across all ten provinces', 'A single highway found only in Ontario', 'A concept unrelated to Canadian geography', 'A railway built in the nineteenth century'], 0),
    ('In approximately what decade was the Trans-Canada Highway completed?', ['The 1960s', 'The 1800s', 'A concept unrelated to Canadian history', 'The 2010s'], 0),
    ('Did the completion of the Trans-Canada Highway improve transportation and trade across the country?', ['Yes', 'No, it had no effect on transportation or trade', 'A concept unrelated to the Trans-Canada Highway', 'It only connected two cities in one province'], 0),
    ('Why might a national highway system be considered important infrastructure for a large country like Canada?', ['It helps connect distant communities and supports the movement of people and goods across the country', 'A national highway system has no benefit for a large country', 'This concept has no connection to social studies', 'Canada’s provinces have no need to be connected to one another'], 0),
    ('Why might building infrastructure like the Trans-Canada Highway have been a significant engineering challenge?', ['It had to cross a vast and varied landscape, including mountains, forests, and rugged terrain', 'Canada’s landscape is completely flat and uniform from coast to coast', 'This concept has no relevance to social studies', 'Highways never need to account for the geography they cross'], 0)]),
]),

day(110, [
L('Review: Grammar, Reading, and Media Literacy (Days 101-109)',
  'Grade 6 Language strand review: students revisit direct and indirect speech, main idea and supporting details, book reviews, homophones, meme analysis, possessive nouns, interviewing techniques, sequencing, and diary writing.',
  [('What does direct speech do?', ['Reports a speaker’s exact words, usually in quotation marks', 'A concept unrelated to grammar', 'Removes all punctuation from a sentence', 'Changes a sentence into a question'], 0),
   ('What is the main idea of a text?', ['The central point the text is making', 'A minor detail mentioned only once', 'A concept unrelated to reading', 'The title of the text only'], 0),
   ('What are homophones?', ['Words that sound the same but have different spellings and meanings', 'Words that are spelled the same but sound different', 'A concept unrelated to vocabulary', 'Words that mean the exact same thing'], 0),
   ('What does a possessive noun show?', ['Ownership', 'A question', 'A concept unrelated to grammar', 'A negative statement'], 0),
   ('What does sequencing mean in reading?', ['Identifying the order in which events happen', 'Identifying the setting of a story', 'A concept unrelated to reading', 'Identifying the main character of a story'], 0)]),
M('Review: Number Sense, Geometry, Data, and Probability (Days 101-109)',
  'Grade 6 Math strand review: students revisit prime and composite numbers, rounding decimals, the angle sum of a triangle, area of a trapezoid, histograms, currency exchange rates, recipe ratios, rate problems, and complementary events.',
  [('What is a prime number?', ['A number with exactly two factors, 1 and itself', 'A number with more than two factors', 'A concept unrelated to number sense', 'A number that is always even'], 0),
   ('What do the three interior angles of any triangle always add up to?', ['180 degrees', '360 degrees', '90 degrees', '270 degrees'], 0),
   ('What is the formula for the area of a trapezoid?', ['One half times the sum of the two bases, times the height', 'Length times width', 'Side times side', 'Base times height only, with no other terms'], 0),
   ('What is the formula for speed?', ['Speed equals distance divided by time', 'Speed equals time divided by distance', 'Speed equals distance times time', 'A concept unrelated to rate problems'], 0),
   ('What do the probabilities of two complementary events always add up to?', ['1, or 100 percent', '0', '2', 'A concept unrelated to complementary events'], 0)]),
Sc('Review: Human Body, Earth Science, and Ecology (Days 101-109)',
   'Grade 6 Science strand review: students revisit the lymphatic system, tides, levers, coral reefs, cloud types, tsunamis, bird migration, the greenhouse effect, and composting.',
   [('What does the lymphatic system collect from body tissues?', ['Excess fluid', 'Only bone cells', 'A concept unrelated to the human body', 'Only hair follicles'], 0),
    ('What is the main cause of tides on Earth?', ['The gravitational pull of the Moon', 'The colour of the ocean water', 'A concept unrelated to tides', 'The temperature of the air above the ocean'], 0),
    ('What is a lever?', ['A simple machine made of a rigid bar that pivots on a fulcrum', 'A machine that only spins in circles', 'A concept unrelated to simple machines', 'A tool used only for cutting'], 0),
    ('What is a tsunami?', ['A series of powerful ocean waves', 'A type of desert sandstorm', 'A concept unrelated to Earth science', 'A slow-moving glacier'], 0),
    ('What does the greenhouse effect do?', ['Traps heat from the sun near Earth’s surface', 'Cools Earth’s surface rapidly', 'A concept unrelated to Earth science', 'Removes all heat from the atmosphere'], 0)]),
SS('Review: World History, Canadian Identity, and Global Issues (Days 101-109)',
   'Grade 6 Social Studies strand review: students revisit ancient Persia, land acknowledgements, urban and rural communities, the Group of Seven, the October Crisis, Japanese Canadian internment, the World Health Organization, Arctic sovereignty, and the Trans-Canada Highway.',
   [('What was the Achaemenid Empire?', ['One of the largest empires in the ancient world, centred in ancient Persia', 'A small city-state with no influence beyond its borders', 'A concept unrelated to ancient history', 'A modern country in North America'], 0),
    ('What is a land acknowledgement?', ['A statement recognizing the traditional Indigenous territory of a place', 'A legal document transferring land ownership', 'A concept unrelated to Canadian history', 'A map showing provincial borders'], 0),
    ('What federal law did the government invoke during the October Crisis?', ['The War Measures Act', 'The Multiculturalism Act', 'A concept unrelated to the October Crisis', 'The Constitution Act'], 0),
    ('What is the World Health Organization an agency of?', ['The United Nations', 'A single country’s government', 'A concept unrelated to global health', 'A private for-profit company'], 0),
    ('What is the Trans-Canada Highway?', ['A highway system stretching across all ten provinces', 'A single highway found only in Ontario', 'A concept unrelated to Canadian geography', 'A railway built in the nineteenth century'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g6_101_110)
    append_to(6, g6_101_110)
