#!/usr/bin/env python3
"""Grade 7, Days 121-130 -- extends Grade 7 from 120 to 130 days. Topics
chosen after grepping the existing Day 1-120 title list (data/grade7.json)
in full to avoid any overlap, since Grade 7's earlier 120 days already
cover an unusually exhaustive range of subject matter: subject-verb
agreement with collective nouns, eponyms, dramatic irony in plays,
writing a book review, evaluating deepfakes, coordinating/subordinating
conjunctions, oxymorons, in medias res and nonlinear timelines, writing a
historical diary entry; conditional probability, probability with vs
without replacement, converting imperial and metric units, range and
interquartile range, frequency polygons, volume by water displacement,
surface-area-to-volume ratio, depreciation, the midpoint formula; the
chemistry of solutions and solubility, glaciers, blood composition and
blood types, how vaccines work, moon phases and tidal cycles, solar
panels and photovoltaic technology, decomposers and nutrient recycling,
physical/chemical weathering of rock, 3D printing and additive
manufacturing; the United Empire Loyalists, the Rebellions of 1837, the
Meech Lake and Charlottetown Accords, the Group of Seven, the Bank of
Canada and monetary policy, the 1972 Summit Series, Canada and the
founding of NATO, time zones and the International Date Line, and urban
heat islands.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are dropped entirely, matching
the convention established in gen_grade7_days111_120.py (e.g. "Canadas"
not "Canada's").
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


def _rebalance_answer_positions(days, seed=20260730):
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


g7_121_130 = [
day(121, [
L('Grammar: Subject-Verb Agreement with Collective Nouns',
  'Grade 7 Language strand: a collective noun names a group treated as a single unit, such as team, class, or family, and it typically takes a singular verb unless the individual members are clearly acting separately.',
  [('What is a collective noun?', ['A noun that names a group treated as a single unit', 'A noun that always describes a single person', 'A verb describing group action', 'A punctuation mark used to join clauses'], 0),
   ('Which of these words is a collective noun?', ['Committee', 'Quickly', 'Blue', 'Running'], 0),
   ('Does a collective noun usually take a singular verb when the group acts as one unit?', ['Yes, because the group is treated as a single entity', 'No, collective nouns always take a plural verb', 'Collective nouns never take any verb at all', 'This concept has no connection to grammar'], 0),
   ('In the sentence The committee is reviewing the proposal, why is the singular verb is used?', ['Because the committee is acting together as one unit', 'Because committee is always a plural word', 'Because is is the only verb allowed in English', 'This concept has no connection to subject-verb agreement'], 0),
   ('Which sentence correctly matches a collective noun with its verb?', ['The class is going on a field trip.', 'The class is going on a field trips.', 'The class going trip a field is.', 'A class field trip is on the going.'], 0)]),
M('Probability: Conditional Probability (Intro)',
  'Grade 7 Math strand: conditional probability is the probability that an event happens given that another event has already occurred, and it often differs from the probability of that event occurring on its own.',
  [('What does conditional probability measure?', ['The probability of an event given that another event has already occurred', 'The probability of an event that can never happen', 'A concept unrelated to probability', 'The probability of two events that are always identical'], 0),
   ('If a bag has 3 red and 2 blue marbles and one red marble is removed without replacement, how does the probability of drawing another red marble change?', ['It decreases, since one red marble and one total marble were removed', 'It stays exactly the same as before', 'It increases to 100 percent automatically', 'A concept unrelated to probability'], 0),
   ('Conditional probability is often described using what phrase?', ['The probability of A given B', 'The probability of A multiplied by B with no condition', 'A concept unrelated to conditional probability', 'The probability of A occurring before B is defined'], 0),
   ('Why might knowing that a card drawn is a face card change the probability that it is also a king?', ['Knowing one condition narrows down the possible outcomes being considered', 'Conditions never affect a probability calculation', 'This concept has no connection to math', 'A face card can never also be a king'], 0),
   ('In a class of 20 students where 12 play soccer and 5 of those also play basketball, what is the probability a student plays basketball given that they play soccer?', ['5 out of 12', '5 out of 20', '12 out of 20', '12 out of 5'], 0)]),
Sc('Solutions, Solubility, and Concentration',
   'Grade 7 Science strand: a solution forms when one substance dissolves evenly into another, solubility describes how much of a substance can dissolve in a given amount of solvent, and concentration describes how much solute is present in a solution.',
   [('What is a solution?', ['A mixture formed when one substance dissolves evenly into another', 'A substance that never mixes with any other substance', 'A concept unrelated to science', 'A solid that cannot be broken down further'], 0),
    ('What does solubility describe?', ['How much of a substance can dissolve in a given amount of solvent', 'The colour of a substance only', 'A concept unrelated to solubility', 'The temperature at which a substance freezes'], 0),
    ('What does concentration describe in a solution?', ['How much solute is present in a solution', 'The exact colour of the solvent', 'A concept unrelated to solutions', 'The container size holding the solution'], 0),
    ('Why might sugar dissolve faster in hot water than in cold water?', ['Higher temperatures generally increase how quickly a solute dissolves', 'Temperature never affects how quickly a solute dissolves', 'This concept has no connection to science', 'Cold water always dissolves sugar faster than hot water'], 0),
    ('What happens when a solution reaches its maximum solubility and can dissolve no more solute?', ['It becomes saturated', 'It becomes completely solid', 'A concept unrelated to solubility', 'It stops being considered a solution at all'], 0)]),
SS('Social Studies: United Empire Loyalists and Their Impact on Canada',
   'Grade 7 Social Studies strand: United Empire Loyalists were colonists who remained loyal to Britain during the American Revolution and resettled in what is now Canada, shaping the early population and development of regions like Ontario and the Maritimes.',
   [('Who were the United Empire Loyalists?', ['Colonists who remained loyal to Britain during the American Revolution', 'Colonists who fought for American independence', 'A concept unrelated to Canadian history', 'A group of French explorers who settled Quebec'], 0),
    ('Where did many United Empire Loyalists resettle after the American Revolution?', ['Regions that are now Ontario and the Maritimes', 'Regions that are now part of Mexico', 'A concept unrelated to Loyalist settlement', 'Regions that are now part of South America'], 0),
    ('Why did United Empire Loyalists leave the newly independent United States?', ['They wished to remain under British rule rather than live in the new republic', 'They were forced out by British soldiers with no connection to loyalty', 'A concept unrelated to Canadian history', 'They were seeking a warmer climate for farming'], 0),
    ('How did the arrival of United Empire Loyalists affect the population of British North America?', ['It significantly increased the population and led to new colonial boundaries', 'It had no effect on the population at all', 'This concept has no connection to Canadian history', 'It caused the population of British North America to shrink dramatically'], 0),
    ('Why do historians consider the Loyalist migration an important event in Canadian history?', ['It helped shape the early English-speaking population and political development of Canada', 'It has no lasting significance for Canadian history', 'This concept has no relevance to social studies', 'It only affected a single small village with no wider impact'], 0)]),
]),
day(122, [
L('Vocabulary: Eponyms — Words Named After People',
  'Grade 7 Language strand: an eponym is a word created from the name of a real or fictional person, such as sandwich from the Earl of Sandwich or volt from the scientist Alessandro Volta.',
  [('What is an eponym?', ['A word created from the name of a real or fictional person', 'A word that has no origin at all', 'A concept unrelated to vocabulary', 'A word borrowed directly from a sound'], 0),
   ('Which of these words is an eponym?', ['Sandwich', 'Table', 'Quickly', 'Blue'], 0),
   ('The unit volt is named after which scientist?', ['Alessandro Volta', 'Isaac Newton', 'Marie Curie', 'Albert Einstein'], 0),
   ('Why might a product or invention eventually become an eponym in everyday language?', ['A brand or inventor becomes so closely tied to an item that its name becomes the common word for it', 'Eponyms are never connected to real people or brands', 'This concept has no connection to vocabulary', 'Every word in English started as an eponym'], 0),
   ('Which is an example of an eponym drawn from mythology or literature?', ['A herculean effort, named after the mythological hero Hercules', 'A quick walk in the park', 'A simple math equation', 'A plain white wall'], 0)]),
M('Probability: With Replacement vs Without Replacement',
  'Grade 7 Math strand: in a with replacement scenario an item is returned before the next draw so probabilities stay the same, while in a without replacement scenario the item stays out, changing the probabilities for later draws.',
  [('What happens in a with replacement scenario after an item is drawn?', ['The item is returned before the next draw', 'The item is destroyed and cannot be replaced', 'A concept unrelated to probability', 'The item is doubled before the next draw'], 0),
   ('How do probabilities change across draws in a without replacement scenario?', ['They change because the total number of items decreases', 'They always stay exactly the same', 'A concept unrelated to probability', 'They become impossible to calculate at all'], 0),
   ('If a bag has 4 marbles and one is drawn without replacement, how many marbles remain for the next draw?', ['3', '4', '5', '0'], 0),
   ('Why might a without replacement scenario give a different probability for a second event than a with replacement scenario?', ['Removing an item changes both the total count and possibly the count of a specific outcome', 'Removing an item never changes any probability', 'This concept has no connection to math', 'With replacement and without replacement always give identical results'], 0),
   ('Drawing a card, recording it, and then putting it back in the deck before drawing again is an example of which scenario?', ['With replacement', 'Without replacement', 'A concept unrelated to probability', 'Neither type of draw applies here'], 0)]),
Sc('Glaciers and Their Role in Shaping Landscapes',
   'Grade 7 Science strand: glaciers are massive, slow-moving bodies of ice that shape the land beneath and around them by eroding rock, carving valleys, and depositing sediment as they advance and retreat over long periods of time.',
   [('What is a glacier?', ['A massive, slow-moving body of ice', 'A fast-flowing river of warm water', 'A concept unrelated to earth science', 'A type of underground cave system'], 0),
    ('How can glaciers shape the landscape beneath them?', ['By eroding rock and carving valleys as they move', 'By having no effect on the land at all', 'A concept unrelated to glaciers', 'By instantly melting without leaving any trace'], 0),
    ('What happens to sediment carried by a glacier when the glacier retreats?', ['It is often deposited, forming new landforms', 'It disappears completely with no trace left behind', 'A concept unrelated to glaciers', 'It turns instantly into solid rock'], 0),
    ('Why do many valleys shaped by glaciers have a distinctive U shape rather than a V shape?', ['Glacial ice erodes broadly along the sides and bottom of a valley as it moves', 'Glaciers never change the shape of a valley', 'This concept has no connection to earth science', 'Only rivers, never glaciers, can shape a valley'], 0),
    ('Why are scientists interested in studying how glaciers are changing today?', ['Changes in glacier size can indicate broader shifts in global climate', 'Glaciers never change in size over time', 'This concept has no relevance to science', 'Glaciers have no connection to climate at all'], 0)]),
SS('Social Studies: The Rebellions of 1837 in Upper and Lower Canada',
   'Grade 7 Social Studies strand: in 1837, reformers in Upper and Lower Canada rebelled against colonial governments they saw as unfair and unrepresentative, and although the rebellions were defeated, they contributed to later reforms in Canadian self-government.',
   [('What happened during the Rebellions of 1837?', ['Reformers in Upper and Lower Canada rebelled against colonial governments', 'A trade agreement was signed between Canada and Britain', 'A concept unrelated to Canadian history', 'A new national holiday was created'], 0),
    ('Why did reformers rebel in 1837?', ['They viewed the colonial governments as unfair and unrepresentative', 'They wanted to strengthen ties with Britain even further', 'A concept unrelated to the rebellions', 'They were protesting a change to the school calendar'], 0),
    ('Were the Rebellions of 1837 ultimately defeated?', ['Yes', 'No, the rebels immediately won full independence', 'A concept unrelated to the rebellions', 'The rebellions never actually took place'], 0),
    ('How did the Rebellions of 1837 influence later Canadian history?', ['They contributed to reforms that eventually expanded self-government in the colonies', 'They had no lasting effect on Canadian government at all', 'This concept has no relevance to social studies', 'They caused Britain to abandon all of its North American colonies immediately'], 0),
    ('Which report, commissioned after the rebellions, recommended greater self-government for the colonies?', ['The Durham Report', 'The Persons Case ruling', 'The Balfour Declaration', 'The Quebec Act'], 0)]),
]),
day(123, [
L('Reading: Analyzing Dramatic Irony in Plays',
  'Grade 7 Language strand: dramatic irony occurs when the audience knows something important that a character on stage does not, creating tension or humour as the audience watches the character act without that knowledge.',
  [('What is dramatic irony?', ['When the audience knows something a character does not', 'When a character explains every detail directly to the audience', 'A concept unrelated to reading', 'When two characters share identical knowledge at all times'], 0),
   ('What effect can dramatic irony create for an audience?', ['Tension or humour as the audience watches events unfold', 'Complete confusion with no emotional effect', 'A concept unrelated to dramatic irony', 'Boredom, since the audience already knows everything'], 0),
   ('In which situation is dramatic irony present?', ['The audience knows a character is walking into a trap, but the character does not', 'A character explains the plot directly to another character who already knows it', 'Two characters discover the same secret at the exact same moment', 'The audience and every character know exactly the same information'], 0),
   ('Why might a playwright use dramatic irony to build suspense?', ['Watching a character act without key knowledge can make the audience anxious about what will happen', 'Dramatic irony always removes suspense from a scene', 'This concept has no connection to literature', 'Dramatic irony requires the audience to know nothing about the plot'], 0),
   ('How does dramatic irony differ from a simple plot twist?', ['Dramatic irony relies on the audience knowing more than a character, not on a sudden surprise reveal', 'Dramatic irony and a plot twist always mean exactly the same thing', 'This concept has no relevance to reading comprehension', 'A plot twist requires the audience to know less than every character'], 0)]),
M('Measurement: Converting Between Imperial and Metric Units',
  'Grade 7 Math strand: the imperial system uses units like inches, feet, and pounds while the metric system uses units like centimetres, metres, and kilograms, and converting between the two systems requires using an approximate conversion factor.',
  [('Which system uses units like inches, feet, and pounds?', ['The imperial system', 'The metric system', 'A concept unrelated to measurement', 'Neither system uses these units'], 0),
   ('Approximately how many centimetres are in one inch?', ['2.54 centimetres', '10 centimetres', '1 centimetre', '100 centimetres'], 0),
   ('Why is a conversion factor needed when converting between imperial and metric units?', ['The two systems are based on different units, so a fixed ratio connects them', 'Imperial and metric units are always exactly the same size', 'A concept unrelated to measurement', 'Conversion factors are never used in measurement'], 0),
   ('If a board is 5 feet long, roughly how many metres is that, given about 3.28 feet in a metre?', ['About 1.5 metres', 'About 15 metres', 'About 0.5 metres', 'About 50 metres'], 0),
   ('Why might understanding both imperial and metric units be useful in everyday life?', ['Different countries and industries commonly use different systems of measurement', 'Only one measurement system exists worldwide', 'This concept has no connection to math', 'Imperial and metric units can never be compared to each other'], 0)]),
Sc('Blood Composition and Blood Types',
   'Grade 7 Science strand: blood is made up of plasma, red blood cells, white blood cells, and platelets, and a persons blood type is determined by specific markers on the surface of their red blood cells.',
   [('What are the main components of blood?', ['Plasma, red blood cells, white blood cells, and platelets', 'Only water and salt', 'A concept unrelated to biology', 'Only bone and muscle tissue'], 0),
    ('What is the main role of red blood cells?', ['Carrying oxygen throughout the body', 'Fighting off infection only', 'A concept unrelated to blood', 'Producing sound waves'], 0),
    ('What determines a persons blood type?', ['Specific markers on the surface of red blood cells', 'The colour of a persons skin', 'A concept unrelated to blood type', 'The persons height and weight'], 0),
    ('Why is it important for doctors to know a patients blood type before a transfusion?', ['Mismatched blood types can cause a dangerous immune reaction', 'Blood type never matters during a transfusion', 'This concept has no connection to biology', 'Every blood type is always compatible with every other type'], 0),
    ('What is the role of platelets in the blood?', ['Helping blood clot to stop bleeding', 'Carrying oxygen to the lungs', 'A concept unrelated to blood composition', 'Producing new bone cells'], 0)]),
SS('Social Studies: The Meech Lake and Charlottetown Accords',
   'Grade 7 Social Studies strand: the Meech Lake and Charlottetown Accords were attempts in the late 1980s and early 1990s to amend the Canadian constitution and address Quebecs demands for recognition, but both ultimately failed to gain the required approval.',
   [('What were the Meech Lake and Charlottetown Accords attempting to do?', ['Amend the Canadian constitution and address Quebecs demands for recognition', 'Establish a new trade agreement with the United States', 'A concept unrelated to Canadian history', 'Create a new national anthem for Canada'], 0),
    ('Did both accords ultimately gain the approval needed to take effect?', ['No, both accords ultimately failed', 'Yes, both accords were fully approved and enacted', 'A concept unrelated to the accords', 'Only the Charlottetown Accord failed, while Meech Lake succeeded'], 0),
    ('Roughly when did these constitutional negotiations take place?', ['The late 1980s and early 1990s', 'The early 1800s', 'The 1950s', 'The 2010s'], 0),
    ('Why were these accords significant even though they failed?', ['They revealed deep divisions over how to accommodate Quebec within Confederation', 'They had no impact on Canadian political discussions at all', 'This concept has no relevance to social studies', 'They were approved without any public debate or discussion'], 0),
    ('What method was used to attempt to ratify the Charlottetown Accord?', ['A national referendum', 'A unanimous vote in the Senate only', 'An international treaty signing', 'A decision made solely by the Prime Minister'], 0)]),
]),
day(124, [
L('Writing: Writing a Book Review',
  'Grade 7 Language strand: a book review summarizes a text without giving away every detail, evaluates its strengths and weaknesses, and offers the writers opinion supported by specific examples from the book.',
  [('What should a book review generally include, along with a summary?', ['An evaluation of strengths and weaknesses supported by examples', 'Only the books total page count', 'A concept unrelated to writing', 'A complete retelling of every plot detail'], 0),
   ('Why might a book review avoid giving away every plot detail?', ['To avoid spoiling the story for readers who have not read it yet', 'Spoilers are always required in a book review', 'This concept has no connection to writing', 'A book review should never mention the plot at all'], 0),
   ('What should support the opinions expressed in a book review?', ['Specific examples from the book', 'Only the reviewers personal mood that day', 'A concept unrelated to book reviews', 'Random guesses with no connection to the text'], 0),
   ('Why might a reviewer discuss a books pacing or character development?', ['These elements affect how effectively the story is told', 'Pacing and character development are never relevant to a review', 'This concept has no connection to writing', 'A book review can only discuss the cover design'], 0),
   ('Which sentence sounds most like part of a book review?', ['The novels vivid descriptions pulled me into the setting, though the ending felt rushed.', 'Once upon a time, in a faraway kingdom.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.'], 0)]),
M('Data Management: Range and Interquartile Range (IQR)',
  'Grade 7 Math strand: the range of a data set is the difference between its highest and lowest values, while the interquartile range measures the spread of the middle half of the data and is less affected by extreme values.',
  [('How is the range of a data set calculated?', ['Subtracting the lowest value from the highest value', 'Adding every value together', 'A concept unrelated to data management', 'Multiplying the highest and lowest values'], 0),
   ('What does the interquartile range measure?', ['The spread of the middle half of the data', 'The single most common value in the data', 'A concept unrelated to interquartile range', 'The total number of values in a data set'], 0),
   ('Why is the interquartile range often more useful than the range when a data set has extreme outliers?', ['The interquartile range is less affected by unusually high or low values', 'The interquartile range is always identical to the range', 'A concept unrelated to data management', 'Outliers always make the interquartile range meaningless'], 0),
   ('If a data set has a lowest value of 5 and a highest value of 45, what is the range?', ['40', '50', '5', '45'], 0),
   ('The interquartile range is generally found using which two values?', ['The first quartile and the third quartile', 'Only the mean and the mode', 'A concept unrelated to quartiles', 'Only the very first and very last data points listed'], 0)]),
Sc('How Vaccines Train the Immune System',
   'Grade 7 Science strand: a vaccine introduces a weakened, inactivated, or partial form of a pathogen so the immune system can learn to recognize it and build a faster, stronger defense if the real pathogen is encountered later.',
   [('What does a vaccine typically introduce into the body?', ['A weakened, inactivated, or partial form of a pathogen', 'A fully active, dangerous version of a disease with no changes', 'A concept unrelated to science', 'A random substance with no connection to disease'], 0),
    ('Why does a vaccine help the immune system respond faster to a real infection later?', ['The immune system has already learned to recognize the pathogen from the vaccine', 'Vaccines have no effect on how the immune system responds', 'A concept unrelated to vaccines', 'The immune system forgets the vaccine immediately'], 0),
    ('What cells does the immune system use to remember a pathogen after vaccination?', ['Memory cells', 'Only red blood cells', 'A concept unrelated to the immune system', 'Only skin cells'], 0),
    ('Why might a vaccinated persons body respond more quickly to a pathogen than an unvaccinated persons body?', ['The vaccinated persons immune system has already been trained to recognize that specific pathogen', 'Vaccination always makes the immune system weaker overall', 'This concept has no connection to biology', 'Only unvaccinated people have functioning immune systems'], 0),
    ('Why are vaccines considered an important public health tool?', ['They can reduce the spread and severity of infectious diseases within a population', 'Vaccines have no effect on how diseases spread through a population', 'This concept has no relevance to science', 'Vaccines only work for a single person and never affect anyone else'], 0)]),
SS('Social Studies: The Group of Seven and Canadian National Identity',
   'Grade 7 Social Studies strand: the Group of Seven was a collective of Canadian landscape painters active in the early 20th century whose bold depictions of the Canadian wilderness helped shape a distinct sense of national identity and pride.',
   [('What was the Group of Seven?', ['A collective of Canadian landscape painters active in the early 20th century', 'A group of Canadian prime ministers', 'A concept unrelated to Canadian history', 'A sports team representing Canada internationally'], 0),
    ('What did the Group of Seven primarily paint?', ['The Canadian wilderness and landscape', 'Portraits of European royalty', 'A concept unrelated to the Group of Seven', 'Scenes exclusively from cities outside Canada'], 0),
    ('How did the Group of Seven influence Canadian culture?', ['Their art helped shape a distinct sense of Canadian national identity', 'Their work had no influence on Canadian culture at all', 'A concept unrelated to Canadian identity', 'They discouraged any interest in Canadian landscapes'], 0),
    ('Why might depicting the rugged Canadian wilderness have resonated with audiences in the early 20th century?', ['It offered a distinctly Canadian artistic style separate from European traditions', 'Canadian audiences had no interest in art depicting their own country', 'This concept has no relevance to social studies', 'The Group of Seven copied European landscapes exactly'], 0),
    ('Why do museums and schools still study the Group of Seven today?', ['Their work remains an important part of Canadian art history and cultural identity', 'Their paintings were destroyed and no longer exist', 'This concept has no relevance to Canadian history', 'The Group of Seven has been entirely forgotten by historians'], 0)]),
]),
day(125, [
L('Media Literacy: Evaluating Deepfakes and Digital Manipulation',
  'Grade 7 Language strand: a deepfake uses artificial intelligence to create convincing but fake images, audio, or video of real people, making it essential for viewers to critically evaluate digital media before trusting or sharing it.',
  [('What is a deepfake?', ['AI-generated media that convincingly but falsely depicts a real person', 'A completely unedited video with no digital changes', 'A concept unrelated to media literacy', 'A type of printed newspaper article'], 0),
   ('What technology is typically used to create a deepfake?', ['Artificial intelligence', 'A simple pencil and paper sketch', 'A concept unrelated to deepfakes', 'An unedited photograph with no software involved'], 0),
   ('Why is it important to critically evaluate digital media before sharing it?', ['Manipulated content can spread false information convincingly', 'All digital media is always completely accurate', 'A concept unrelated to media literacy', 'Sharing unverified content never causes any harm'], 0),
   ('Which of these might be a warning sign that a video could be a deepfake?', ['Unnatural facial movements or mismatched audio and lip movement', 'Perfectly natural, verified footage from a trusted news source', 'A concept unrelated to digital manipulation', 'A video with a clearly labeled and credited source'], 0),
   ('Why might deepfakes pose a challenge for journalism and public trust?', ['They can make it harder to distinguish real events from fabricated ones', 'Deepfakes always clearly announce themselves as fake', 'This concept has no relevance to media literacy', 'Deepfakes have no impact on how people perceive news'], 0)]),
M('Data Management: Constructing Frequency Polygons',
  'Grade 7 Math strand: a frequency polygon displays grouped data as a series of connected line segments plotted at the midpoint of each interval, offering an alternative to a histogram for showing the shape of a distribution.',
  [('What does a frequency polygon use to display data?', ['A series of connected line segments plotted at interval midpoints', 'Solid bars with no connecting lines', 'A concept unrelated to data management', 'Randomly placed dots with no clear pattern'], 0),
   ('What point of each interval is typically used to plot a frequency polygon?', ['The midpoint', 'The lowest value only', 'A concept unrelated to frequency polygons', 'The highest value only'], 0),
   ('How does a frequency polygon differ from a histogram?', ['It uses connected points instead of bars to show the same kind of grouped data', 'A frequency polygon and a histogram are always exactly identical', 'A concept unrelated to data displays', 'A frequency polygon can only display a single data value'], 0),
   ('Why might a frequency polygon be useful for comparing two data sets on the same graph?', ['Overlapping line shapes can be easier to compare than overlapping bars', 'Frequency polygons can never be used to compare two data sets', 'This concept has no connection to math', 'Only one frequency polygon can ever exist on a single graph'], 0),
   ('What does the overall shape of a frequency polygon help reveal about a data set?', ['The general distribution and trend of the data', 'The exact colour used in the original data collection', 'A concept unrelated to frequency polygons', 'The names of the people who collected the data'], 0)]),
Sc('Moon Phases and Tidal Cycles',
   'Grade 7 Science strand: the moon appears to change shape in the sky as it orbits Earth in a predictable cycle of phases, and its gravitational pull, along with the suns, causes the rise and fall of ocean tides.',
   [('Why does the moon appear to change shape in the sky over about a month?', ['It moves through a predictable cycle of phases as it orbits Earth', 'The moon physically changes shape every night', 'A concept unrelated to astronomy', 'The moon disappears completely every single day'], 0),
    ('What mainly causes ocean tides on Earth?', ['The gravitational pull of the moon and the sun', 'Wind blowing across the ocean surface only', 'A concept unrelated to tides', 'Ocean currents with no connection to gravity'], 0),
    ('What is a full moon?', ['The phase when the entire visible side of the moon appears illuminated', 'The phase when the moon is completely invisible', 'A concept unrelated to moon phases', 'A phase that never actually occurs'], 0),
    ('Why do the highest tides, called spring tides, occur during a full or new moon?', ['The gravitational pull of the sun and moon align, increasing their combined effect', 'The sun and moon have no combined effect on tides', 'This concept has no connection to science', 'Spring tides only occur during the spring season'], 0),
    ('Why is understanding the predictable cycle of moon phases and tides useful for coastal communities?', ['It helps with activities like fishing, navigation, and planning around changing water levels', 'Moon phases and tides have no practical use for coastal communities', 'This concept has no relevance to science', 'Tides never actually change throughout a lunar cycle'], 0)]),
SS('Social Studies: The Bank of Canada and Monetary Policy',
   'Grade 7 Social Studies strand: the Bank of Canada is the countrys central bank, responsible for setting monetary policy, controlling the money supply, and working to keep inflation low and stable to support the overall economy.',
   [('What is the Bank of Canada?', ['The countrys central bank', 'A private bank that competes with other Canadian banks for customers', 'A concept unrelated to Canadian government', 'A department that manages national parks'], 0),
    ('What is one main responsibility of the Bank of Canada?', ['Setting monetary policy and controlling the money supply', 'Building highways across the country', 'A concept unrelated to the Bank of Canada', 'Managing Canadas foreign embassies'], 0),
    ('What economic goal does the Bank of Canada aim to support by keeping inflation low and stable?', ['A healthy, stable overall economy', 'Rapid, unlimited price increases every year', 'A concept unrelated to monetary policy', 'The complete elimination of all Canadian currency'], 0),
    ('Why might the Bank of Canada adjust interest rates as a tool of monetary policy?', ['Changing interest rates can influence borrowing, spending, and overall economic activity', 'Interest rates have no connection to the economy at all', 'This concept has no relevance to social studies', 'The Bank of Canada has no ability to influence interest rates'], 0),
    ('Why is it important for a country to have a central bank like the Bank of Canada?', ['It helps manage the money supply and maintain economic stability', 'A central bank has no meaningful role in a countrys economy', 'This concept has no relevance to Canadian history', 'Central banks only exist to print currency with no other function'], 0)]),
]),
day(126, [
L('Grammar: Coordinating and Subordinating Conjunctions',
  'Grade 7 Language strand: a coordinating conjunction, such as and or but, joins two equal ideas, while a subordinating conjunction, such as although or because, joins a dependent clause to an independent clause.',
  [('What does a coordinating conjunction do?', ['Joins two equal ideas', 'Joins a dependent clause only', 'A concept unrelated to grammar', 'Ends a sentence with no connection to grammar'], 0),
   ('Which of these is a coordinating conjunction?', ['And', 'Although', 'Because', 'Since'], 0),
   ('What does a subordinating conjunction do?', ['Joins a dependent clause to an independent clause', 'Joins two completely unrelated sentences with no connection', 'A concept unrelated to subordinating conjunctions', 'Replaces a noun in a sentence'], 0),
   ('In the sentence Although it was raining, we went outside, what type of conjunction is although?', ['A subordinating conjunction', 'A coordinating conjunction', 'A concept unrelated to conjunctions', 'A type of pronoun'], 0),
   ('Why is it useful to know the difference between coordinating and subordinating conjunctions?', ['It helps writers correctly join clauses and vary sentence structure', 'The difference between these conjunctions never matters in writing', 'This concept has no connection to grammar', 'Only subordinating conjunctions exist in English'], 0)]),
M('Geometry: Volume of Irregular Solids by Water Displacement',
  'Grade 7 Math strand: the volume of an irregular solid that cannot be measured with a simple formula can be found using water displacement, where the amount of water an object pushes aside equals its volume.',
  [('What method can be used to find the volume of an irregular solid?', ['Water displacement', 'Multiplying its length, width, and height only', 'A concept unrelated to geometry', 'Weighing the object on a scale only'], 0),
   ('In water displacement, what does the amount of water pushed aside represent?', ['The volume of the object', 'The mass of the object', 'A concept unrelated to water displacement', 'The temperature of the object'], 0),
   ('If an object raises the water level in a container from 200 mL to 250 mL, what is the volume of the object?', ['50 mL', '200 mL', '250 mL', '450 mL'], 0),
   ('Why is water displacement useful for measuring the volume of an oddly shaped rock?', ['A simple geometric formula cannot easily be applied to its irregular shape', 'Every irregular object already has an obvious volume formula', 'This concept has no connection to math', 'Water displacement can only be used on perfectly cube-shaped objects'], 0),
   ('What must be true about the irregular solid for the water displacement method to work correctly?', ['It must not dissolve or absorb the water it is placed in', 'It must always float on top of the water', 'A concept unrelated to measuring volume', 'It must be exactly the same size as the container'], 0)]),
Sc('Renewable Energy: Solar Panels and Photovoltaic Technology',
   'Grade 7 Science strand: solar panels use photovoltaic cells to convert sunlight directly into electricity, offering a renewable energy source that produces no direct emissions while generating power.',
   [('What do photovoltaic cells in a solar panel convert into electricity?', ['Sunlight', 'Wind', 'A concept unrelated to renewable energy', 'Heat from underground'], 0),
    ('Why is solar power considered a renewable energy source?', ['Sunlight is naturally replenished and does not run out', 'Sunlight is a limited resource that will soon disappear', 'A concept unrelated to solar power', 'Solar panels require burning fossil fuels to operate'], 0),
    ('What is one advantage of solar power over fossil fuels?', ['It produces no direct emissions while generating electricity', 'It never depends on weather or sunlight conditions', 'A concept unrelated to solar energy', 'It requires no technology to harness at all'], 0),
    ('What might reduce how much electricity a solar panel produces on a given day?', ['Cloud cover or reduced sunlight reaching the panel', 'The colour of nearby buildings only', 'A concept unrelated to solar panels', 'The time of year, with no other factor involved'], 0),
    ('Solar panels are often grouped together on rooftops or in large fields called what?', ['Solar farms', 'Wind farms', 'A concept unrelated to solar energy', 'Power plants only'], 0)]),
SS('Social Studies: The 1972 Summit Series and Cold War Sports Diplomacy',
   'Grade 7 Social Studies strand: the 1972 Summit Series was a hockey competition between Canada and the Soviet Union that became a symbol of Cold War rivalry, with Canadas dramatic victory sparking a surge of national pride.',
   [('What was the 1972 Summit Series?', ['A hockey competition between Canada and the Soviet Union', 'A trade agreement between Canada and the United States', 'A concept unrelated to Canadian history', 'A summit meeting between world political leaders'], 0),
    ('Why did the 1972 Summit Series become a symbol of Cold War rivalry?', ['It pitted two nations from opposing sides of the Cold War against each other in sport', 'It had no connection to international politics at all', 'A concept unrelated to the Summit Series', 'It was played entirely within a single country with no international element'], 0),
    ('How did Canadians generally react to their teams victory in the series?', ['With a surge of national pride', 'With complete indifference to the result', 'A concept unrelated to the Summit Series', 'With disappointment, since Canada actually lost'], 0),
    ('Why might a sports competition like the Summit Series carry political significance beyond the game itself?', ['It can symbolize broader ideological and national rivalries between competing systems', 'Sports competitions never carry any meaning beyond the game itself', 'This concept has no relevance to social studies', 'The Cold War had no connection to any cultural or sporting events'], 0),
    ('Why is the 1972 Summit Series still remembered as a significant moment in Canadian history?', ['It is seen as a defining moment of national identity and Cold War tension', 'It has been completely forgotten by most Canadians today', 'This concept has no relevance to Canadian history', 'It had no lasting cultural impact on Canada'], 0)]),
]),
day(127, [
L('Vocabulary: Oxymorons and Contradictory Phrases',
  'Grade 7 Language strand: an oxymoron combines two contradictory terms for effect, such as deafening silence or bittersweet, often highlighting a complex or ironic idea in just a few words.',
  [('What is an oxymoron?', ['A phrase that combines two contradictory terms', 'A word that means the exact same thing twice', 'A concept unrelated to vocabulary', 'A phrase with only one possible meaning'], 0),
   ('Which of these phrases is an example of an oxymoron?', ['Deafening silence', 'Bright sunshine', 'Cold winter', 'Fast runner'], 0),
   ('Why might a writer use an oxymoron in a piece of writing?', ['To highlight a complex or ironic idea in just a few words', 'Oxymorons never add any meaning to writing', 'A concept unrelated to oxymorons', 'Oxymorons are always grammatically incorrect and should be avoided'], 0),
   ('What makes bittersweet an oxymoron?', ['It combines the contradictory ideas of bitterness and sweetness', 'It describes only one simple, uncomplicated feeling', 'A concept unrelated to oxymorons', 'It has no connection to taste or emotion at all'], 0),
   ('Why might the phrase original copy be considered an oxymoron?', ['Original suggests something new, while copy suggests something duplicated', 'The two words always mean exactly the same thing', 'This concept has no relevance to vocabulary', 'A copy is always considered more original than the source'], 0)]),
M('Geometry: Surface-Area-to-Volume Ratio and Its Real-World Effects',
  'Grade 7 Math strand: the surface-area-to-volume ratio compares an objects outer surface area to its interior volume, and this ratio decreases as an object gets larger, which affects things like heat loss and cooling rates.',
  [('What does the surface-area-to-volume ratio compare?', ['An objects outer surface area to its interior volume', 'An objects height to its width only', 'A concept unrelated to geometry', 'An objects mass to its colour'], 0),
   ('What generally happens to the surface-area-to-volume ratio as an object gets larger?', ['It decreases', 'It always stays exactly the same', 'A concept unrelated to this ratio', 'It increases without any limit'], 0),
   ('Why might a smaller object cool down faster than a larger object of the same shape?', ['A smaller object has a relatively larger surface area compared to its volume, allowing faster heat loss', 'Smaller objects always have a lower surface-area-to-volume ratio than larger ones', 'A concept unrelated to geometry', 'Object size has no effect on how quickly heat is lost'], 0),
   ('A cube with side length 2 has a smaller surface-area-to-volume ratio than a cube with side length ___.', ['1', '3', '4', '5'], 0),
   ('Why might engineers consider surface-area-to-volume ratio when designing cooling systems for machinery?', ['A higher ratio can help a design lose heat more efficiently', 'Surface-area-to-volume ratio has no connection to how objects lose heat', 'This concept has no relevance to math', 'Cooling systems never depend on the shape or size of an object'], 0)]),
Sc('Decomposers and Nutrient Recycling in Ecosystems',
   'Grade 7 Science strand: decomposers, such as fungi and bacteria, break down dead organisms and waste material, releasing nutrients back into the soil and allowing them to be reused by other living things in an ecosystem.',
   [('What is the main role of decomposers in an ecosystem?', ['Breaking down dead organisms and waste to release nutrients', 'Producing their own food using sunlight only', 'A concept unrelated to ecosystems', 'Hunting and consuming only living prey'], 0),
    ('Which of these organisms are common decomposers?', ['Fungi and bacteria', 'Only large predators', 'A concept unrelated to decomposers', 'Only plants that photosynthesize'], 0),
    ('What happens to nutrients released by decomposers?', ['They return to the soil and can be reused by other living things', 'They disappear from the ecosystem permanently', 'A concept unrelated to nutrient cycling', 'They only benefit the decomposers themselves'], 0),
    ('Why would an ecosystem struggle to function without decomposers?', ['Dead material and waste would build up instead of being recycled into usable nutrients', 'Ecosystems function exactly the same with or without decomposers', 'This concept has no connection to biology', 'Only producers, never decomposers, matter in an ecosystem'], 0),
    ('How are decomposers connected to nutrient cycles, such as the carbon and nitrogen cycles?', ['They help break down organic material, returning key elements to the environment for reuse', 'Decomposers have no role in any nutrient cycle', 'This concept has no relevance to science', 'Nutrient cycles function without any input from living organisms'], 0)]),
SS('Social Studies: Canada and the Founding of NATO',
   'Grade 7 Social Studies strand: Canada was a founding member of the North Atlantic Treaty Organization in 1949, a military alliance created to provide collective defense among member countries during the early Cold War period.',
   [('What is NATO?', ['A military alliance created to provide collective defense among member countries', 'A trade agreement focused only on agricultural goods', 'A concept unrelated to Canadian history', 'An organization focused solely on environmental protection'], 0),
    ('Was Canada a founding member of NATO?', ['Yes', 'No, Canada joined NATO decades after it was founded', 'A concept unrelated to NATO', 'Canada has never been a member of NATO'], 0),
    ('In what year was NATO founded?', ['1949', '1867', '1999', '1918'], 0),
    ('Why was NATO created during the early Cold War period?', ['Member countries wanted collective protection against potential threats from the Soviet Union', 'NATO was created with no connection to Cold War tensions', 'A concept unrelated to NATO', 'NATO was created purely to promote international trade'], 0),
    ('What does collective defense mean within an alliance like NATO?', ['An attack on one member is treated as an attack on all members', 'Each member must handle every conflict entirely alone', 'A concept unrelated to collective defense', 'Only the strongest member is responsible for defending the alliance'], 0)]),
]),
day(128, [
L('Reading: Analyzing In Medias Res and Nonlinear Timelines',
  'Grade 7 Language strand: in medias res means beginning a story in the middle of the action rather than at the very start, and a nonlinear timeline presents events out of chronological order, requiring readers to piece the story together.',
  [('What does in medias res mean?', ['Beginning a story in the middle of the action', 'Ending a story before any action occurs', 'A concept unrelated to reading', 'Telling a story in strict chronological order only'], 0),
   ('What is a nonlinear timeline in storytelling?', ['A structure where events are presented out of chronological order', 'A structure where every event happens in perfect time order', 'A concept unrelated to nonlinear timelines', 'A timeline that only ever moves forward one second at a time'], 0),
   ('Why might an author choose to begin a story in medias res?', ['To immediately capture the readers interest with action or tension', 'Beginning in the middle of the action always confuses readers with no benefit', 'A concept unrelated to reading strategies', 'Every story is required to begin in medias res'], 0),
   ('What skill do readers often need when following a nonlinear timeline?', ['Piecing together the order of events as the story unfolds', 'Ignoring the order of events completely', 'A concept unrelated to reading comprehension', 'Reading only the first page of the story'], 0),
   ('Which is an example of a nonlinear structure?', ['A story that begins with the ending, then flashes back to explain how it happened', 'A story told in exact chronological order from beginning to end with no flashbacks', 'A recipe with numbered steps', 'A list of dictionary definitions'], 0)]),
M('Financial Literacy: Understanding Depreciation and Asset Value Over Time',
  'Grade 7 Math strand: depreciation is the gradual decrease in the value of an asset, such as a car or electronic device, over time due to age, wear, and changing market conditions.',
  [('What is depreciation?', ['The gradual decrease in the value of an asset over time', 'The gradual increase in the value of an asset over time', 'A concept unrelated to financial literacy', 'A fixed value that never changes for any asset'], 0),
   ('Which of these items is most likely to depreciate in value over time?', ['A used car', 'A rare, well-preserved painting', 'A concept unrelated to depreciation', 'Land in a rapidly growing city, which often appreciates instead'], 0),
   ('What might cause an electronic device to lose value over time?', ['Age, wear, and the release of newer models', 'Devices always keep the exact same value forever', 'A concept unrelated to depreciation', 'Depreciation only applies to houses, never electronics'], 0),
   ('If a car worth 20,000 dollars depreciates by 10 percent in its first year, what is its approximate value after that year?', ['18,000 dollars', '22,000 dollars', '20,000 dollars', '2,000 dollars'], 0),
   ('Why might understanding depreciation be useful when deciding whether to buy a new or used vehicle?', ['It helps estimate how much value the vehicle may lose over time', 'Depreciation has no connection to buying decisions', 'This concept has no relevance to financial literacy', 'Every vehicle depreciates at exactly the same fixed rate'], 0)]),
Sc('Physical and Chemical Weathering of Rocks',
   'Grade 7 Science strand: physical weathering breaks rock into smaller pieces without changing its chemical makeup, such as through freezing and thawing, while chemical weathering alters the minerals in rock through reactions like oxidation or dissolution.',
   [('What does physical weathering do to rock?', ['Breaks it into smaller pieces without changing its chemical makeup', 'Completely dissolves the rock into liquid', 'A concept unrelated to earth science', 'Turns the rock into a different type of mineral entirely'], 0),
    ('What is one process that causes physical weathering?', ['Freezing and thawing of water in cracks', 'Photosynthesis in nearby plants only', 'A concept unrelated to physical weathering', 'Sound waves traveling through the air'], 0),
    ('What happens during chemical weathering?', ['The minerals in rock are altered through chemical reactions', 'The rock is broken apart with no chemical change at all', 'A concept unrelated to chemical weathering', 'Rock instantly transforms into a living organism'], 0),
    ('Why might iron-rich rocks develop a reddish, rusty appearance over time?', ['Oxidation, a type of chemical weathering, reacts with the iron in the rock', 'Rocks never undergo any type of chemical change', 'This concept has no connection to earth science', 'Only physical weathering can ever change a rocks appearance'], 0),
    ('Why might freezing and thawing be especially effective at breaking apart rock in a crack?', ['Water expands as it freezes, widening the crack over repeated cycles', 'Water always shrinks as it freezes, closing cracks completely', 'This concept has no relevance to science', 'Freezing and thawing have no effect on the size of a crack'], 0)]),
SS('Social Studies: Time Zones and the International Date Line',
   'Grade 7 Social Studies strand: time zones divide the world into regions that generally share the same standard time based on longitude, and the International Date Line marks where, by convention, the calendar date changes by a full day.',
   [('What do time zones divide the world into?', ['Regions that generally share the same standard time', 'Regions that always share identical weather patterns', 'A concept unrelated to geography', 'Regions based only on population size'], 0),
    ('What is the International Date Line used for?', ['Marking where the calendar date changes by a full day', 'Marking the boundary between countries only', 'A concept unrelated to time zones', 'Measuring temperature differences across the globe'], 0),
    ('What geographic measurement are time zones generally based on?', ['Longitude', 'Latitude only, with no connection to longitude', 'A concept unrelated to time zones', 'Altitude above sea level'], 0),
    ('Why do countries or regions sometimes adjust their official time zone boundaries away from a strict longitude line?', ['To keep areas with close economic or political ties on the same time for convenience', 'Time zone boundaries can never be adjusted for any reason', 'This concept has no connection to geography', 'Longitude has no relationship to time zones at all'], 0),
    ('Why might understanding time zones be important for international communication and travel?', ['It helps people coordinate schedules and avoid confusion across different regions', 'Time zones have no effect on communication or travel planning', 'This concept has no relevance to social studies', 'Every location in the world shares the exact same time'], 0)]),
]),
day(129, [
L('Writing: Writing a Diary Entry from a Historical Perspective',
  'Grade 7 Language strand: a historical diary entry imagines the voice and perspective of a person living through a past event, using accurate details and a personal tone to help readers connect emotionally with history.',
  [('What does a historical diary entry imagine?', ['The voice and perspective of a person living through a past event', 'A completely fictional world with no connection to history', 'A concept unrelated to writing', 'A formal news report with no personal perspective'], 0),
   ('Why is accurate historical detail important in this type of writing?', ['It helps the diary entry feel authentic to the time period being described', 'Accuracy is never important in creative writing', 'A concept unrelated to historical diary entries', 'Historical details should always be avoided completely'], 0),
   ('What tone does a diary entry typically use?', ['A personal, reflective tone', 'A strictly formal, businesslike tone with no emotion', 'A concept unrelated to tone in writing', 'An entirely objective tone with no perspective at all'], 0),
   ('Why might writing a diary entry from a historical perspective help readers understand a past event more deeply?', ['It connects readers emotionally by showing history through an individual persons experience', 'Diary entries never help readers understand historical events', 'This concept has no connection to writing', 'Historical events are always better understood only through statistics'], 0),
   ('Which opening sounds most like a historical diary entry?', ['Today, the ship finally docked after weeks at sea, and I can hardly believe what I have seen.', 'The chemical symbol for gold is Au.', 'Add 15 and 20 to get 35.', 'Please find attached the quarterly financial report.'], 0)]),
M('Geometry: The Midpoint of a Line Segment on the Cartesian Plane',
  'Grade 7 Math strand: the midpoint of a line segment is the point exactly halfway between its two endpoints, and it can be found on the Cartesian plane by averaging the x-coordinates and averaging the y-coordinates of the endpoints.',
  [('What is the midpoint of a line segment?', ['The point exactly halfway between its two endpoints', 'The point at one of the two endpoints', 'A concept unrelated to geometry', 'The longest possible point along the segment'], 0),
   ('How is the midpoint of a segment found on the Cartesian plane?', ['By averaging the x-coordinates and averaging the y-coordinates of the endpoints', 'By adding the x-coordinates together with no division', 'A concept unrelated to midpoints', 'By multiplying the two endpoints together'], 0),
   ('What is the midpoint of a segment with endpoints at (2, 4) and (6, 8)?', ['(4, 6)', '(8, 12)', '(2, 4)', '(6, 8)'], 0),
   ('Why might finding a midpoint be useful when working with maps or coordinate-based problems?', ['It can help locate a central point between two known locations', 'Midpoints have no practical use on the Cartesian plane', 'A concept unrelated to geometry', 'A midpoint can only be found using a physical ruler, never coordinates'], 0),
   ('If one endpoint of a segment is (0, 0) and the midpoint is (3, 5), what is the other endpoint?', ['(6, 10)', '(3, 5)', '(1.5, 2.5)', '(0, 0)'], 0)]),
Sc('3D Printing and Additive Manufacturing',
   'Grade 7 Science strand: 3D printing, also called additive manufacturing, builds objects layer by layer from a digital design, allowing complex shapes to be created that would be difficult or impossible to make using traditional manufacturing methods.',
   [('What is another name for 3D printing?', ['Additive manufacturing', 'Subtractive manufacturing', 'A concept unrelated to technology', 'Traditional casting'], 0),
    ('How does a 3D printer typically build an object?', ['Layer by layer from a digital design', 'By carving material away from a solid block', 'A concept unrelated to 3D printing', 'By melting an entire object into a single mold instantly'], 0),
    ('What is one advantage of 3D printing over some traditional manufacturing methods?', ['It can create complex shapes that would be difficult to make otherwise', 'It can only ever create simple cube shapes', 'A concept unrelated to 3D printing', 'It always requires more raw material than traditional methods'], 0),
    ('Why might engineers use 3D printing to create a prototype before mass-producing a product?', ['It allows a design to be tested and adjusted quickly and at lower cost', 'Prototypes can never be created using 3D printing', 'This concept has no connection to technology', 'Mass production always happens before any prototype is made'], 0),
    ('Which of these fields has benefited from advances in 3D printing technology?', ['Medicine, through custom prosthetics and models', 'Only the food service industry, with no other applications', 'A concept unrelated to 3D printing', 'Fields that have no use for manufactured objects'], 0)]),
SS('Social Studies: Urban Heat Islands and City Climate Patterns',
   'Grade 7 Social Studies strand: an urban heat island forms when cities, with their concentration of pavement and buildings, absorb and retain more heat than surrounding rural areas, creating noticeably warmer local temperatures.',
   [('What is an urban heat island?', ['An area where a city is noticeably warmer than surrounding rural areas', 'A rural area that is always colder than any nearby city', 'A concept unrelated to geography', 'An island located entirely within a citys harbour'], 0),
    ('Why do cities often become warmer than surrounding rural areas?', ['Pavement and buildings absorb and retain more heat than natural landscapes', 'Cities always contain more trees and green space than rural areas', 'A concept unrelated to urban heat islands', 'Cities receive less sunlight than rural areas'], 0),
    ('Which surface would likely contribute most to an urban heat island effect?', ['Dark asphalt pavement', 'A large grassy field', 'A concept unrelated to heat retention', 'A forest with dense tree cover'], 0),
    ('Why might city planners add green spaces or reflective roofing to reduce the urban heat island effect?', ['These features can help lower how much heat a city absorbs and retains', 'Green spaces and reflective roofing always increase citywide temperatures', 'This concept has no connection to social studies', 'Urban heat islands cannot be reduced by any planning decisions'], 0),
    ('Why is understanding urban heat islands important for city planning and public health?', ['Higher urban temperatures can affect energy use, comfort, and heat-related health risks', 'Urban temperature has no connection to public health or energy use', 'This concept has no relevance to social studies', 'Cities are always exactly the same temperature as nearby rural areas'], 0)]),
]),
day(130, [
L('Language Review: Grammar, Vocabulary, Reading, and Writing',
  'Grade 7 Language strand review: students revisit subject-verb agreement with collective nouns, eponyms, dramatic irony, evaluating deepfakes, oxymorons, and writing a historical diary entry.',
  [('What is a collective noun?', ['A noun that names a group treated as a single unit', 'A noun that always describes a single person', 'A verb describing group action', 'A punctuation mark used to join clauses'], 0),
   ('What is an eponym?', ['A word created from the name of a real or fictional person', 'A word that has no origin at all', 'A concept unrelated to vocabulary', 'A word borrowed directly from a sound'], 0),
   ('What is dramatic irony?', ['When the audience knows something a character does not', 'When a character explains every detail directly to the audience', 'A concept unrelated to reading', 'When two characters share identical knowledge at all times'], 0),
   ('What is a deepfake?', ['AI-generated media that convincingly but falsely depicts a real person', 'A completely unedited video with no digital changes', 'A concept unrelated to media literacy', 'A type of printed newspaper article'], 0),
   ('What is an oxymoron?', ['A phrase that combines two contradictory terms', 'A word that means the exact same thing twice', 'A concept unrelated to vocabulary', 'A phrase with only one possible meaning'], 0)]),
M('Math Review: Probability, Measurement, Data, and Geometry',
  'Grade 7 Math strand review: students revisit conditional probability, converting imperial and metric units, range and interquartile range, volume by water displacement, and the midpoint formula.',
  [('What does conditional probability measure?', ['The probability of an event given that another event has already occurred', 'The probability of an event that can never happen', 'A concept unrelated to probability', 'The probability of two events that are always identical'], 0),
   ('Which system uses units like inches, feet, and pounds?', ['The imperial system', 'The metric system', 'A concept unrelated to measurement', 'Neither system uses these units'], 0),
   ('How is the range of a data set calculated?', ['Subtracting the lowest value from the highest value', 'Adding every value together', 'A concept unrelated to data management', 'Multiplying the highest and lowest values'], 0),
   ('What method can be used to find the volume of an irregular solid?', ['Water displacement', 'Multiplying its length, width, and height only', 'A concept unrelated to geometry', 'Weighing the object on a scale only'], 0),
   ('How is the midpoint of a segment found on the Cartesian plane?', ['By averaging the x-coordinates and averaging the y-coordinates of the endpoints', 'By adding the x-coordinates together with no division', 'A concept unrelated to midpoints', 'By multiplying the two endpoints together'], 0)]),
Sc('Science Review: Chemistry, Earth Science, Biology, and Technology',
   'Grade 7 Science strand review: students revisit solutions and solubility, glaciers, blood composition, how vaccines work, and 3D printing and additive manufacturing.',
   [('What is a solution?', ['A mixture formed when one substance dissolves evenly into another', 'A substance that never mixes with any other substance', 'A concept unrelated to science', 'A solid that cannot be broken down further'], 0),
    ('What is a glacier?', ['A massive, slow-moving body of ice', 'A fast-flowing river of warm water', 'A concept unrelated to earth science', 'A type of underground cave system'], 0),
    ('What are the main components of blood?', ['Plasma, red blood cells, white blood cells, and platelets', 'Only water and salt', 'A concept unrelated to biology', 'Only bone and muscle tissue'], 0),
    ('What does a vaccine typically introduce into the body?', ['A weakened, inactivated, or partial form of a pathogen', 'A fully active, dangerous version of a disease with no changes', 'A concept unrelated to science', 'A random substance with no connection to disease'], 0),
    ('What is another name for 3D printing?', ['Additive manufacturing', 'Subtractive manufacturing', 'A concept unrelated to technology', 'Traditional casting'], 0)]),
SS('Social Studies Review: Nation-Building and Global Institutions',
   'Grade 7 Social Studies strand review: students revisit the United Empire Loyalists, the Rebellions of 1837, the Meech Lake and Charlottetown Accords, the Group of Seven, the Bank of Canada, and the founding of NATO.',
   [('Who were the United Empire Loyalists?', ['Colonists who remained loyal to Britain during the American Revolution', 'Colonists who fought for American independence', 'A concept unrelated to Canadian history', 'A group of French explorers who settled Quebec'], 0),
    ('What happened during the Rebellions of 1837?', ['Reformers in Upper and Lower Canada rebelled against colonial governments', 'A trade agreement was signed between Canada and Britain', 'A concept unrelated to Canadian history', 'A new national holiday was created'], 0),
    ('What were the Meech Lake and Charlottetown Accords attempting to do?', ['Amend the Canadian constitution and address Quebecs demands for recognition', 'Establish a new trade agreement with the United States', 'A concept unrelated to Canadian history', 'Create a new national anthem for Canada'], 0),
    ('What was the Group of Seven?', ['A collective of Canadian landscape painters active in the early 20th century', 'A group of Canadian prime ministers', 'A concept unrelated to Canadian history', 'A sports team representing Canada internationally'], 0),
    ('What is NATO?', ['A military alliance created to provide collective defense among member countries', 'A trade agreement focused only on agricultural goods', 'A concept unrelated to Canadian history', 'An organization focused solely on environmental protection'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_121_130)
    append_to(7, g7_121_130)
