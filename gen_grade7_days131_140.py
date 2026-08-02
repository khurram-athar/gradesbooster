#!/usr/bin/env python3
"""Grade 7, Days 131-140 -- extends Grade 7 from 130 to 140 days. Topics
chosen after reading the full Day 1-130 title list (data/grade7.json) to
avoid any overlap, since Grade 7's earlier 130 days already cover an
unusually exhaustive range of subject matter across all four subjects.
Fresh, non-duplicate topics picked this batch: relative clauses, malapropisms,
literary archetypes, writing a movie review, evaluating influencer marketing,
reported (indirect) speech, acronyms and initialisms, anti-heroes and morally
complex characters, writing a podcast script; mean absolute deviation, angle
relationships in parallel lines cut by a transversal, mortgages and
amortization, cumulative frequency and ogives, tessellations and symmetry,
converting units of area and volume, geometric probability with area models,
consecutive integer word problems, indirect measurement with similar
triangles; comets/asteroids/meteors, permafrost and the cryosphere, light and
colour (absorption/reflection), biodegradable materials and waste
management, nanotechnology, circadian rhythms, the Doppler effect, hydrogen
fuel cells, fermentation; the Fenian Raids, the National Policy of 1879, the
1982 patriation of the constitution, the 1964 flag debate, Canadas
peacekeeping mission in Cyprus, the National Energy Program and western
alienation, the 1988 free trade election, the history of O Canada and
national symbols, and the history of the CBC.

Subject keys for Grade 7 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 7 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option text;
apostrophes are dropped entirely, matching the convention established in
gen_grade7_days111_120.py and gen_grade7_days121_130.py (e.g. "Canadas" not
"Canada's").

Usage:
  cd ~/gradesbooster && python3 gen_grade7_days131_140.py
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


g7_131_140 = [
day(131, [
L('Grammar: Relative Clauses and Relative Pronouns',
  'Grade 7 Language strand: a relative clause adds extra information about a noun and begins with a relative pronoun such as who, whom, whose, which, or that, connecting the extra detail directly to the noun it describes.',
  [('What is a relative clause?', ['A clause that adds extra information about a noun using a relative pronoun', 'A clause that always stands alone as its own sentence', 'A concept unrelated to grammar', 'A clause that never connects to any noun'], 0),
   ('Which word is commonly used as a relative pronoun?', ['Which', 'Quickly', 'Blue', 'Running'], 0),
   ('In the sentence The book which I borrowed was excellent, what does the relative clause describe?', ['The book', 'The act of borrowing only', 'A concept unrelated to relative clauses', 'The reader of the book'], 0),
   ('Why would a writer use who instead of which in a relative clause?', ['Who generally refers to people while which generally refers to things', 'Who and which always mean exactly the same thing', 'This concept has no connection to grammar', 'Which can only ever refer to people'], 0),
   ('Which sentence correctly uses a relative clause?', ['The teacher who helped me was very patient.', 'The teacher who helped me was patient very.', 'Patient the teacher who helped me was.', 'Helped the teacher who was me patient.'], 0)]),
M('Data Management: Mean Absolute Deviation (MAD)',
  'Grade 7 Math strand: mean absolute deviation, or MAD, measures the average distance between each data value and the mean of the data set, giving a sense of how spread out the values are.',
  [('What does mean absolute deviation (MAD) measure?', ['The average distance between each data value and the mean', 'The single highest value in a data set', 'A concept unrelated to data management', 'The total number of values in a data set'], 0),
   ('What is the first step in finding the MAD of a data set?', ['Calculating the mean of the data set', 'Multiplying every value by itself', 'A concept unrelated to MAD', 'Removing the lowest and highest values entirely'], 0),
   ('Why are absolute values used when calculating MAD?', ['So that positive and negative differences do not cancel each other out', 'Absolute value has no purpose in this calculation', 'A concept unrelated to data management', 'Absolute values always make every difference equal to zero'], 0),
   ('If a data set has a mean of 10 and one value is 14, what is the absolute deviation of that value from the mean?', ['4', '10', '14', '24'], 0),
   ('Why might MAD be useful for comparing how consistent two data sets are?', ['A smaller MAD suggests the data values are generally closer to the mean', 'MAD can never be used to compare two different data sets', 'This concept has no connection to math', 'A larger MAD always means the data set has fewer values'], 0)]),
Sc('Comets, Asteroids, and Meteors',
   'Grade 7 Science strand: comets are icy bodies that develop glowing tails as they near the sun, asteroids are rocky or metallic bodies found mostly in the asteroid belt between Mars and Jupiter, and meteors are streaks of light produced when space debris burns up in Earths atmosphere.',
   [('What is a comet mostly made of?', ['Ice, dust, and rocky material', 'Pure liquid water only', 'A concept unrelated to astronomy', 'Solid metal with no ice at all'], 0),
    ('Where are most asteroids in our solar system found?', ['The asteroid belt between Mars and Jupiter', 'Deep inside the suns core', 'A concept unrelated to asteroids', 'Orbiting far outside the solar system entirely'], 0),
    ('What is a meteor?', ['A streak of light produced when space debris burns up in the atmosphere', 'A fully formed planet within our solar system', 'A concept unrelated to astronomy', 'A type of cloud found only on Earth'], 0),
    ('Why does a comet develop a glowing tail as it approaches the sun?', ['Heat from the sun causes ice on the comet to turn into gas and dust that stream away from it', 'Comets always have an identical tail regardless of distance from the sun', 'This concept has no connection to science', 'A comets tail forms only when it is farthest from the sun'], 0),
    ('What is the difference between a meteor and a meteorite?', ['A meteorite is a piece of space debris that survives and reaches the ground', 'A meteor and a meteorite are always exactly the same thing', 'This concept has no relevance to astronomy', 'A meteorite can only be found floating in space, never on the ground'], 0)]),
SS('Social Studies: The Fenian Raids and the Push Toward Confederation',
   'Grade 7 Social Studies strand: the Fenian Raids were a series of armed incursions into British North America by an Irish-American group in the 1860s, and the resulting sense of vulnerability helped strengthen support for Confederation among the colonies.',
   [('What were the Fenian Raids?', ['A series of armed incursions into British North America by an Irish-American group', 'A peaceful trade negotiation between Canada and Ireland', 'A concept unrelated to Canadian history', 'A series of scientific expeditions across the Arctic'], 0),
    ('Why did the Fenians target British North America in the 1860s?', ['They hoped pressuring Britain in North America would help the cause of Irish independence', 'They wanted to establish a new trade route to Asia', 'A concept unrelated to the Fenian Raids', 'They were hired directly by the Canadian government'], 0),
    ('How did the Fenian Raids affect support for Confederation among the colonies?', ['They increased a sense of vulnerability that strengthened support for a unified defense', 'They had no effect whatsoever on support for Confederation', 'A concept unrelated to Canadian history', 'They caused every colony to reject the idea of Confederation completely'], 0),
    ('In which decade did the Fenian Raids mainly take place?', ['The 1860s', 'The 1700s', 'The 1900s', 'The 1950s'], 0),
    ('Why do historians consider the Fenian Raids significant to Confederation in 1867?', ['They highlighted the colonies need for stronger, unified defense against outside threats', 'They have no connection to the events leading up to Confederation', 'This concept has no relevance to social studies', 'They led to the colonies being permanently annexed by another country'], 0)]),
]),
day(132, [
L('Vocabulary: Malapropisms and Word Confusion',
  'Grade 7 Language strand: a malapropism happens when a speaker or character mistakenly swaps a word for a similar-sounding word, often creating an unintentionally funny effect, as when a character says dance a flamingo instead of dance a flamenco.',
  [('What is a malapropism?', ['The mistaken use of a word in place of a similar-sounding word', 'A word that has exactly one correct meaning', 'A concept unrelated to vocabulary', 'A word that never appears in dialogue'], 0),
   ('Which sentence contains an example of a malapropism?', ['She wanted to dance a flamingo at the party.', 'She wanted to dance a flamenco at the party.', 'She wanted to sing a song at the party.', 'She wanted to read a book at the party.'], 0),
   ('Why might an author give a character a habit of using malapropisms?', ['To add humour and reveal something about the characters personality', 'Malapropisms are always meant to be taken completely seriously', 'A concept unrelated to characterization', 'Malapropisms never appear in fiction'], 0),
   ('The term malapropism comes from a character in which type of work?', ['A stage play', 'A scientific textbook', 'A concept unrelated to vocabulary', 'A weather report'], 0),
   ('Why is context important for recognizing a malapropism?', ['Context reveals that a similar-sounding but incorrect word was used by mistake', 'Context never helps identify a mistaken word choice', 'This concept has no connection to vocabulary', 'A malapropism can only be identified by its spelling, never its meaning'], 0)]),
M('Geometry: Angle Relationships in Parallel Lines and Transversals',
  'Grade 7 Math strand: when a transversal crosses two parallel lines, it creates pairs of angles with predictable relationships, including equal corresponding angles, equal alternate interior angles, and supplementary co-interior angles.',
  [('What is a transversal?', ['A line that crosses two or more other lines', 'A line that never intersects any other line', 'A concept unrelated to geometry', 'A line segment with no defined length'], 0),
   ('What is true about corresponding angles when a transversal crosses two parallel lines?', ['They are equal in measure', 'They always add up to 90 degrees', 'A concept unrelated to parallel lines', 'They are always equal to zero degrees'], 0),
   ('What is true about alternate interior angles formed by a transversal crossing two parallel lines?', ['They are equal in measure', 'They always add up to 360 degrees', 'A concept unrelated to transversals', 'They are never related to each other in any way'], 0),
   ('What do co-interior (same-side interior) angles add up to when formed by a transversal crossing two parallel lines?', ['180 degrees', '90 degrees', '360 degrees', '45 degrees'], 0),
   ('If one angle formed by a transversal crossing parallel lines measures 70 degrees, what is the measure of its corresponding angle?', ['70 degrees', '110 degrees', '180 degrees', '35 degrees'], 0)]),
Sc('Permafrost and the Cryosphere',
   'Grade 7 Science strand: the cryosphere includes all the frozen water on Earth, such as glaciers, sea ice, and snow, while permafrost is ground that has remained frozen for two or more consecutive years, mostly found in Arctic and high-altitude regions.',
   [('What is permafrost?', ['Ground that has remained frozen for two or more consecutive years', 'Ground that has never once frozen in recorded history', 'A concept unrelated to earth science', 'A type of rock found only underwater'], 0),
    ('What does the term cryosphere refer to?', ['All the frozen water found on Earth, including ice, snow, and permafrost', 'Only the liquid water found in oceans', 'A concept unrelated to the cryosphere', 'The layer of gases surrounding Earth'], 0),
    ('Why is thawing permafrost a concern for scientists studying climate change?', ['Thawing permafrost can release trapped greenhouse gases into the atmosphere', 'Thawing permafrost has no effect on the atmosphere at all', 'A concept unrelated to earth science', 'Permafrost releases oxygen only, with no other gases involved'], 0),
    ('Where is permafrost most commonly found?', ['Arctic and high-altitude mountain regions', 'Tropical rainforests near the equator', 'A concept unrelated to permafrost', 'Ocean floors far from any coastline'], 0),
    ('Why might thawing permafrost cause problems for roads and buildings constructed on top of it?', ['The ground becomes unstable and can shift or sink as the ice within it melts', 'Thawing permafrost always makes the ground more solid and stable', 'This concept has no relevance to earth science', 'Buildings are never affected by changes in the ground beneath them'], 0)]),
SS('Social Studies: The National Policy of 1879',
   'Grade 7 Social Studies strand: the National Policy, introduced by Prime Minister John A. Macdonald in 1879, combined protective tariffs on foreign goods, construction of a transcontinental railway, and immigration to the west into a single strategy for economic development.',
   [('What was the National Policy of 1879?', ['An economic strategy combining tariffs, a transcontinental railway, and western immigration', 'A treaty ending a war between Canada and another country', 'A concept unrelated to Canadian history', 'A policy focused only on education reform'], 0),
    ('Why did the National Policy include protective tariffs on foreign goods?', ['To protect Canadian manufacturers from foreign competition', 'To eliminate all trade between Canada and other countries', 'A concept unrelated to the National Policy', 'Tariffs were included with no economic purpose at all'], 0),
    ('What role did the railway play in the National Policy?', ['It aimed to connect the country and encourage settlement of the west', 'It had no connection to settlement or economic development', 'A concept unrelated to the National Policy', 'It was intended to discourage any travel between regions'], 0),
    ('Why did the National Policy encourage immigration to western Canada?', ['To populate the west and support agricultural and economic growth', 'To reduce the overall population of Canada', 'A concept unrelated to Canadian history', 'Immigration was actively discouraged under the National Policy'], 0),
    ('Who was the prime minister most closely associated with introducing the National Policy?', ['Sir John A. Macdonald', 'Sir Wilfrid Laurier', 'Lester B. Pearson', 'Pierre Trudeau'], 0)]),
]),
day(133, [
L('Reading: Analyzing Literary Archetypes',
  'Grade 7 Language strand: a literary archetype is a recurring character type, symbol, or pattern, such as the hero or the wise mentor, that appears across many stories and cultures because it reflects a familiar human experience.',
  [('What is a literary archetype?', ['A recurring character type or pattern found across many stories', 'A character that appears in only one story ever written', 'A concept unrelated to reading', 'A type of punctuation used in dialogue'], 0),
   ('Which of these is a well-known literary archetype?', ['The wise mentor who guides the hero', 'A character with no name or role in the story', 'A concept unrelated to archetypes', 'A list of chapter titles'], 0),
   ('Why do archetypes appear across many different cultures and time periods?', ['They reflect familiar human experiences and roles that many cultures recognize', 'Archetypes are always invented by a single author with no wider connection', 'This concept has no connection to literature', 'Archetypes only appear in stories written in the last ten years'], 0),
   ('How does an archetype differ from a highly unique, one-of-a-kind character?', ['An archetype follows a recognizable pattern seen in other stories, while a unique character does not', 'An archetype and a unique character are always exactly identical', 'This concept has no relevance to reading', 'Archetypes can only exist in nonfiction writing'], 0),
   ('Which situation best reflects the hero archetype?', ['A character who leaves home, faces challenges, and grows through the journey', 'A character who never leaves home or faces any challenge', 'A concept unrelated to literary archetypes', 'A character who exists only in a list of ingredients'], 0)]),
M('Financial Literacy: Mortgages and Amortization (Intro)',
  'Grade 7 Math strand: a mortgage is a long-term loan used to purchase property, and amortization describes the schedule of regular payments that gradually pay down both the interest owed and the original amount borrowed.',
  [('What is a mortgage?', ['A long-term loan used to purchase property', 'A one-time payment made in full with no borrowing involved', 'A concept unrelated to financial literacy', 'A type of savings account with no connection to borrowing'], 0),
   ('What does amortization describe in relation to a mortgage?', ['The schedule of regular payments that gradually pay down the loan', 'A single payment that pays off the entire mortgage instantly', 'A concept unrelated to mortgages', 'The exact size of the home being purchased'], 0),
   ('How might a longer amortization period generally affect the total interest paid on a mortgage?', ['A longer period generally increases the total interest paid over time', 'A longer period always decreases the total interest paid to zero', 'A concept unrelated to amortization', 'The length of the amortization period never affects total interest'], 0),
   ('Why does a larger down payment generally reduce the size of a mortgage needed?', ['A larger down payment covers more of the purchase price upfront, leaving less to borrow', 'A larger down payment always increases the amount that must be borrowed', 'This concept has no connection to financial literacy', 'Down payments have no relationship to the size of a mortgage'], 0),
   ('How does a higher interest rate generally affect a mortgages monthly payment?', ['It generally increases the monthly payment amount', 'It always decreases the monthly payment amount to zero', 'A concept unrelated to mortgages', 'Interest rates never affect monthly mortgage payments'], 0)]),
Sc('Light and Colour: Absorption and Reflection',
   'Grade 7 Science strand: an object appears a particular colour because it reflects that wavelength of light while absorbing most other wavelengths, and darker colours generally absorb more light energy, which is often converted into heat.',
   [('Why does an object appear a particular colour, such as red?', ['It reflects that wavelength of light while absorbing most other wavelengths', 'It creates that colour of light entirely on its own with no outside light needed', 'A concept unrelated to science', 'Colour has no connection to light at all'], 0),
    ('Why do black surfaces generally feel warmer in sunlight than white surfaces?', ['Black surfaces absorb more light energy, which converts into heat', 'Black surfaces reflect all light and absorb none of it', 'A concept unrelated to light and colour', 'Colour has no effect on how much heat a surface absorbs'], 0),
    ('Why do white or light-coloured surfaces generally reflect more light?', ['They reflect most wavelengths of visible light rather than absorbing them', 'White surfaces absorb every wavelength of light completely', 'A concept unrelated to science', 'Light-coloured surfaces produce their own light source'], 0),
    ('What generally happens to light energy that is absorbed by an object rather than reflected?', ['It is often converted into heat energy', 'It disappears completely with no effect on the object', 'A concept unrelated to light and colour', 'It is converted directly into sound energy'], 0),
    ('Why does a red apple appear red under white light?', ['It reflects mostly red wavelengths of light while absorbing the other colours', 'It absorbs every wavelength of light equally', 'This concept has no connection to science', 'It produces red light itself with no outside light source needed'], 0)]),
SS('Social Studies: The Patriation of the Canadian Constitution in 1982',
   'Grade 7 Social Studies strand: patriation in 1982 brought full authority over the Canadian constitution under Canadian control for the first time, ending the need for British approval of constitutional changes, and was accompanied by the introduction of the Canadian Charter of Rights and Freedoms.',
   [('What does patriation of the constitution mean?', ['Bringing full authority over the constitution under Canadian control', 'Sending the constitution to another country for approval', 'A concept unrelated to Canadian history', 'Removing the constitution from use entirely'], 0),
    ('Who was the prime minister during the 1982 patriation of the constitution?', ['Pierre Trudeau', 'Sir John A. Macdonald', 'Lester B. Pearson', 'Stephen Harper'], 0),
    ('What important document was introduced alongside patriation in 1982?', ['The Canadian Charter of Rights and Freedoms', 'The Statute of Westminster', 'A concept unrelated to patriation', 'The Treaty of Versailles'], 0),
    ('Which province did not formally sign on to the 1982 constitutional agreement?', ['Quebec', 'Ontario', 'British Columbia', 'Nova Scotia'], 0),
    ('Why is the 1982 patriation considered a significant milestone in Canadian history?', ['Canada gained full authority to amend its own constitution without requiring British approval', 'It had no meaningful effect on how Canadas constitution could be changed', 'This concept has no relevance to social studies', 'It marked the moment Canada lost all connection to its previous constitution'], 0)]),
]),
day(134, [
L('Writing: Writing a Movie Review',
  'Grade 7 Language strand: a movie review briefly summarizes the plot without spoiling key surprises, evaluates elements like acting, direction, and visuals, and supports the writers opinion with specific scenes or examples from the film.',
  [('What should a movie review generally include, along with a brief summary?', ['An evaluation of elements like acting, direction, and visuals', 'Only the exact runtime of the movie', 'A concept unrelated to writing', 'A complete transcript of every line of dialogue'], 0),
   ('Why might a movie review avoid revealing a films biggest plot twist?', ['To avoid spoiling the experience for viewers who have not seen it yet', 'Spoilers are always required in a movie review', 'This concept has no connection to writing', 'A movie review should never mention the plot at all'], 0),
   ('What should support the opinions expressed in a movie review?', ['Specific scenes or examples from the film', 'Only the reviewers mood on the day of writing', 'A concept unrelated to movie reviews', 'Random guesses with no connection to the film'], 0),
   ('Why might a reviewer discuss a films direction or visual style?', ['These elements affect how effectively the story is told on screen', 'Direction and visuals are never relevant to a movie review', 'This concept has no connection to writing', 'A movie review can only discuss the poster design'], 0),
   ('Which sentence sounds most like part of a movie review?', ['The lead actors performance brought real emotion to an otherwise predictable plot.', 'Once upon a time, in a faraway kingdom.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.'], 0)]),
M('Data Management: Cumulative Frequency and Ogives',
  'Grade 7 Math strand: a cumulative frequency table keeps a running total of frequencies as data values increase, and an ogive is a line graph of that running total, often used to estimate the median of a data set.',
  [('What does a cumulative frequency table show?', ['A running total of frequencies as data values increase', 'Only the single most frequent value in a data set', 'A concept unrelated to data management', 'The exact colour used to display each data value'], 0),
   ('What is an ogive?', ['A line graph showing cumulative frequency', 'A type of bar graph with no connection to frequency', 'A concept unrelated to data displays', 'A graph that can only display a single data point'], 0),
   ('How is each new value added to a cumulative frequency table?', ['By adding it to the running total of all previous frequencies', 'By replacing the previous total completely', 'A concept unrelated to cumulative frequency', 'By subtracting it from the running total'], 0),
   ('What can the shape of an ogive help estimate about a data set?', ['The approximate median of the data', 'The exact colour of the original survey used to collect data', 'A concept unrelated to ogives', 'The name of the person who collected the data'], 0),
   ('If a cumulative frequency table shows 5, 12, 20, and 30 for four increasing intervals, how many data values fall within the third interval alone?', ['8', '20', '12', '30'], 0)]),
Sc('Biodegradable Materials and Waste Management',
   'Grade 7 Science strand: biodegradable materials, such as food scraps and paper, break down naturally through the action of living organisms, while non-biodegradable materials, such as many plastics, persist in the environment for a very long time and pose challenges for waste management.',
   [('What does biodegradable mean?', ['Able to be broken down naturally by living organisms', 'Unable to ever break down under any circumstances', 'A concept unrelated to science', 'Made entirely of metal or glass'], 0),
    ('Which of these materials is generally considered non-biodegradable?', ['Many types of plastic', 'A banana peel', 'A concept unrelated to biodegradability', 'A sheet of paper'], 0),
    ('Why can non-biodegradable materials be especially problematic in landfills?', ['They can remain in the environment for a very long time without breaking down', 'They always break down completely within a single day', 'A concept unrelated to waste management', 'Landfills have no connection to biodegradability at all'], 0),
    ('How can recycling help reduce problems associated with non-biodegradable waste?', ['It can reduce the amount of new non-biodegradable material sent to landfills', 'Recycling always increases the total amount of waste produced', 'This concept has no connection to science', 'Recycling has no effect on how materials are managed'], 0),
    ('Which of these is an example of a biodegradable material?', ['Food scraps', 'A plastic bottle', 'A concept unrelated to biodegradability', 'A styrofoam container'], 0)]),
SS('Social Studies: The Great Canadian Flag Debate of 1964',
   'Grade 7 Social Studies strand: the flag debate of 1964, championed by Prime Minister Lester B. Pearson, led to the adoption of the red and white Maple Leaf flag in 1965, replacing the Red Ensign and sparking heated disagreement over Canadas ties to British symbols.',
   [('What was the Great Canadian Flag Debate of 1964 about?', ['Choosing a new national flag design to replace the existing one', 'Deciding whether Canada should adopt a new national anthem', 'A concept unrelated to Canadian history', 'Choosing the location of a new national capital'], 0),
    ('Which prime minister championed the introduction of a new Canadian flag?', ['Lester B. Pearson', 'Sir John A. Macdonald', 'Pierre Trudeau', 'Stephen Harper'], 0),
    ('What flag design was ultimately chosen as a result of the debate?', ['The red and white Maple Leaf flag', 'A flag featuring only the Union Jack', 'A concept unrelated to the flag debate', 'A flag with no connection to Canada at all'], 0),
    ('In what year was the new Canadian flag officially adopted?', ['1965', '1867', '1982', '1939'], 0),
    ('Why was the flag debate considered controversial at the time?', ['Some Canadians wanted to preserve stronger visual ties to British symbols like the Red Ensign', 'The debate had no connection to Canadian identity or history', 'This concept has no relevance to social studies', 'Every Canadian agreed completely on the new design from the start'], 0)]),
]),
day(135, [
L('Media Literacy: Evaluating Influencer Marketing',
  'Grade 7 Language strand: influencer marketing happens when a social media personality promotes a product, often for payment, and viewers benefit from recognizing sponsored content and thinking critically about whether a recommendation is genuine.',
  [('What is influencer marketing?', ['When a social media personality promotes a product, often for payment', 'A completely unpaid recommendation with no business relationship', 'A concept unrelated to media literacy', 'A type of printed magazine advertisement only'], 0),
   ('Why are influencers often required to disclose when content is sponsored?', ['So viewers know a payment or partnership may have influenced the recommendation', 'Disclosure is never required for sponsored content', 'A concept unrelated to influencer marketing', 'Sponsored content is always identical to genuine, unpaid opinions'], 0),
   ('Why is it important to think critically about an influencers product recommendation?', ['The recommendation may be influenced by payment rather than the influencers honest opinion', 'Every influencer recommendation is always completely unbiased', 'A concept unrelated to media literacy', 'Critical thinking is never useful when viewing social media content'], 0),
   ('Which of these might indicate a social media post is sponsored content?', ['A label such as ad or sponsored included in the post', 'A post with absolutely no connection to any product', 'A concept unrelated to influencer marketing', 'A post that never mentions a brand or product at all'], 0),
   ('Why does influencer marketing matter to consumers making purchasing decisions?', ['Recognizing sponsored content helps consumers make more informed choices', 'Sponsored content has no effect on what consumers decide to buy', 'This concept has no relevance to media literacy', 'Consumers can never be influenced by social media content'], 0)]),
M('Geometry: Tessellations and Symmetry',
  'Grade 7 Math strand: a tessellation is a repeating pattern of shapes that covers a flat surface with no gaps or overlaps, and shapes like equilateral triangles, squares, and regular hexagons can tessellate because their angles divide evenly around a point.',
  [('What is a tessellation?', ['A repeating pattern of shapes that covers a surface with no gaps or overlaps', 'A single shape that never repeats in any pattern', 'A concept unrelated to geometry', 'A pattern that always leaves large gaps between shapes'], 0),
   ('Which of these regular shapes can tessellate on its own?', ['A square', 'A regular pentagon', 'A concept unrelated to tessellations', 'A regular heptagon'], 0),
   ('Why can a regular hexagon tessellate without leaving any gaps?', ['Its interior angles divide evenly into 360 degrees around each point', 'Its interior angles always add up to more than 360 degrees', 'A concept unrelated to tessellations', 'Hexagons can never fit together without leaving gaps'], 0),
   ('What role does symmetry often play in a tessellating pattern?', ['It helps the repeating shapes align consistently across the surface', 'Symmetry always prevents shapes from tessellating', 'A concept unrelated to geometry', 'Tessellations can never contain any symmetry at all'], 0),
   ('Which natural structure is often cited as an example of a tessellating pattern?', ['A honeycomb made of hexagonal cells', 'A single round pebble', 'A concept unrelated to tessellations', 'A cloud with no repeating shape'], 0)]),
Sc('Nanotechnology: Engineering at the Atomic Scale',
   'Grade 7 Science strand: nanotechnology involves designing and manipulating materials at an extremely small scale, measured in nanometres, enabling applications such as targeted drug delivery in medicine and stronger, lighter materials in engineering.',
   [('What is nanotechnology?', ['The design and manipulation of materials at an extremely small, nanometre scale', 'The study of objects that are visible only from space', 'A concept unrelated to science', 'A technology that only works on objects larger than a house'], 0),
    ('Roughly how small is a nanometre?', ['About one billionth of a metre', 'About one metre exactly', 'A concept unrelated to nanotechnology', 'About one thousand kilometres'], 0),
    ('Why might materials behave differently at the nanoscale compared to their normal, everyday size?', ['Extremely small particles can have different physical and chemical properties than larger amounts of the same material', 'Materials always behave in exactly the same way no matter their size', 'A concept unrelated to nanotechnology', 'Nanoscale materials never have any special properties'], 0),
    ('How is nanotechnology sometimes used in medicine?', ['To help deliver medication directly and precisely to targeted cells', 'To completely replace the need for any medical treatment', 'This concept has no connection to science', 'Nanotechnology has no applications in medicine at all'], 0),
    ('Why might engineers use nanotechnology to develop new materials?', ['It can help create materials that are stronger or lighter than traditional materials', 'Nanotechnology can only make materials heavier and weaker', 'This concept has no relevance to science', 'New materials can never be developed using nanotechnology'], 0)]),
SS('Social Studies: Canadas Peacekeeping Mission in Cyprus',
   'Grade 7 Social Studies strand: Canada contributed troops to a United Nations peacekeeping force in Cyprus beginning in 1964 to help maintain a ceasefire between Greek and Turkish Cypriot communities, becoming one of Canadas longest peacekeeping commitments.',
   [('What was the purpose of the United Nations peacekeeping force sent to Cyprus?', ['To help maintain a ceasefire between Greek and Turkish Cypriot communities', 'To conquer new territory on behalf of the United Nations', 'A concept unrelated to Canadian history', 'To build new highways across the island'], 0),
    ('Why was a peacekeeping force needed in Cyprus in the 1960s?', ['Tension and conflict existed between the islands two main ethnic communities', 'Cyprus had no history of any internal tension at all', 'A concept unrelated to peacekeeping', 'The mission was sent for reasons unrelated to any conflict'], 0),
    ('Roughly how long did Canadian troops contribute to the peacekeeping mission in Cyprus?', ['Several decades', 'Only a single afternoon', 'A concept unrelated to Cyprus', 'Canada never sent any troops to Cyprus'], 0),
    ('What is the general goal of a peacekeeping mission like the one in Cyprus?', ['To maintain a ceasefire and help prevent renewed violence', 'To take direct military control of the region permanently', 'A concept unrelated to peacekeeping', 'To end all communication between the two communities involved'], 0),
    ('Why did missions like the one in Cyprus contribute to Canadas international reputation?', ['They reinforced Canadas identity as a committed contributor to international peacekeeping efforts', 'Peacekeeping missions have no connection to how other countries view Canada', 'This concept has no relevance to social studies', 'Canada has never participated in any peacekeeping mission'], 0)]),
]),
day(136, [
L('Grammar: Reported (Indirect) Speech',
  'Grade 7 Language strand: reported speech restates what someone said without using their exact words in quotation marks, often shifting the verb tense and changing pronouns to fit the perspective of the person reporting it.',
  [('What is reported speech?', ['Restating what someone said without using their exact quoted words', 'A word-for-word quotation placed in quotation marks', 'A concept unrelated to grammar', 'A sentence with no connection to speech at all'], 0),
   ('If someone says I am tired, how might this be rewritten in reported speech?', ['She said she was tired.', 'She said I am tired.', 'A concept unrelated to reported speech', 'She said tired I am.'], 0),
   ('Why does the verb tense often shift when converting direct speech into reported speech?', ['Reported speech usually moves the tense back to reflect that the statement happened earlier', 'Verb tense never changes when converting to reported speech', 'A concept unrelated to grammar', 'Reported speech always uses the future tense regardless of the original statement'], 0),
   ('Why might pronouns change when converting direct speech into reported speech?', ['The pronouns need to match the perspective of the person reporting the statement', 'Pronouns are never affected by converting speech into reported form', 'This concept has no connection to grammar', 'Reported speech always removes every pronoun completely'], 0),
   ('Which sentence is written correctly in reported speech?', ['He said that he would call later.', 'He said that I will call later.', 'He said, He would call later.', 'He said that will call later he.'], 0)]),
M('Measurement: Converting Units of Area and Volume',
  'Grade 7 Math strand: converting between units of area requires squaring the linear conversion factor, while converting between units of volume requires cubing it, since area and volume involve two and three dimensions respectively.',
  [('Why must a linear conversion factor be squared when converting between units of area?', ['Because area involves two dimensions, so the conversion factor applies twice', 'Area conversions never require any adjustment to the linear factor', 'A concept unrelated to measurement', 'Squaring a conversion factor only applies to units of volume'], 0),
   ('How many square centimetres are in 1 square metre, given 100 centimetres in 1 metre?', ['10,000', '100', '1,000', '1,000,000'], 0),
   ('Why must a linear conversion factor be cubed when converting between units of volume?', ['Because volume involves three dimensions, so the conversion factor applies three times', 'Volume conversions never require any adjustment to the linear factor', 'A concept unrelated to measurement', 'Cubing a conversion factor only applies to units of area'], 0),
   ('How many cubic centimetres are in 1 cubic metre, given 100 centimetres in 1 metre?', ['1,000,000', '10,000', '100', '1,000'], 0),
   ('Why can the simple linear conversion factor not be used directly when converting square or cubic units?', ['Applying it without squaring or cubing would ignore the extra dimensions involved', 'Linear, square, and cubic units always convert using the exact same factor', 'This concept has no connection to measurement', 'Square and cubic units never need any conversion at all'], 0)]),
Sc('Circadian Rhythms and the Sleep-Wake Cycle',
   'Grade 7 Science strand: a circadian rhythm is an internal biological clock that repeats roughly every 24 hours, regulating the sleep-wake cycle and other body functions largely in response to patterns of light and darkness.',
   [('What is a circadian rhythm?', ['An internal biological clock that repeats roughly every 24 hours', 'A rhythm that only occurs once per year', 'A concept unrelated to biology', 'A pattern found only in plants, never in animals'], 0),
    ('What is one major factor that helps regulate the circadian rhythm?', ['Exposure to light and darkness', 'The colour of a persons clothing', 'A concept unrelated to circadian rhythms', 'The number of books a person owns'], 0),
    ('Why is a consistent sleep-wake cycle generally considered important for the body?', ['It supports healthy brain function, mood, and overall physical health', 'Sleep has no measurable effect on the brain or body', 'A concept unrelated to biology', 'The body functions identically whether or not a person sleeps'], 0),
    ('What might disrupt a persons circadian rhythm?', ['Exposure to bright screen light late at night', 'A completely dark, quiet room used only for sleeping', 'A concept unrelated to circadian rhythms', 'Waking up at the exact same time every single day'], 0),
    ('Why might travelling across many time zones cause jet lag?', ['It temporarily disrupts the bodys internal clock, which has not yet adjusted to the new light pattern', 'Jet lag has no connection to the circadian rhythm at all', 'This concept has no relevance to science', 'The circadian rhythm instantly resets the moment a plane lands'], 0)]),
SS('Social Studies: The National Energy Program and Western Alienation',
   'Grade 7 Social Studies strand: the National Energy Program, introduced by the federal government in 1980, aimed to increase Canadian control over the oil industry and stabilize energy prices, but it angered many in western provinces like Alberta and deepened feelings of western alienation.',
   [('What was the National Energy Program?', ['A federal policy from 1980 aimed at increasing Canadian control over oil and stabilizing prices', 'A program focused entirely on building new schools', 'A concept unrelated to Canadian history', 'An agreement to import all of Canadas oil from other countries'], 0),
    ('Why did the federal government introduce the National Energy Program?', ['To increase Canadian ownership of the energy industry and manage energy prices', 'To eliminate the energy industry from the Canadian economy entirely', 'A concept unrelated to the National Energy Program', 'To transfer full control of oil resources to another country'], 0),
    ('How did many people in western provinces, especially Alberta, react to the National Energy Program?', ['With anger, feeling the policy unfairly targeted their regions oil industry', 'With enthusiastic support and no objections at all', 'A concept unrelated to western Canada', 'They were completely unaffected by the policy'], 0),
    ('What does the term western alienation generally describe?', ['A feeling among people in western Canada that the federal government overlooks or mistreats their interests', 'A feeling of strong satisfaction with federal government policies', 'A concept unrelated to Canadian politics', 'A term with no connection to any Canadian region'], 0),
    ('Why is the National Energy Program still discussed in relation to regional tensions in Canada?', ['It is often cited as a key example of conflict between federal policy and western provincial interests', 'It has been completely forgotten and has no lasting significance', 'This concept has no relevance to social studies', 'It only affected a single small town with no wider impact'], 0)]),
]),
day(137, [
L('Vocabulary: Acronyms and Initialisms',
  'Grade 7 Language strand: an acronym is an abbreviation formed from the first letters of a phrase and pronounced as a single word, such as NASA, while an initialism is pronounced letter by letter, such as FBI.',
  [('What is an acronym?', ['An abbreviation formed from initial letters and pronounced as a single word', 'A word with no connection to any longer phrase', 'A concept unrelated to vocabulary', 'A phrase that is always written out in full with no shortening'], 0),
   ('Which of these is an example of an acronym pronounced as a word?', ['NASA', 'FBI', 'CD', 'ATM'], 0),
   ('How does an initialism differ from an acronym?', ['An initialism is pronounced letter by letter rather than as a single word', 'An initialism and an acronym are always pronounced in exactly the same way', 'A concept unrelated to vocabulary', 'An initialism can never be formed from a phrase'], 0),
   ('Why might people use acronyms and initialisms in everyday language?', ['They shorten long phrases into something quicker and easier to say', 'Acronyms and initialisms always make communication more confusing with no benefit', 'This concept has no connection to vocabulary', 'Every English word is technically an acronym'], 0),
   ('Which of these is best described as an initialism rather than an acronym?', ['FBI, pronounced letter by letter', 'NASA, pronounced as a single word', 'A concept unrelated to abbreviations', 'A word that has no letters at all'], 0)]),
M('Probability: Geometric Probability with Area Models',
  'Grade 7 Math strand: geometric probability compares the area of a favourable region to the area of the entire possible region, useful for situations like a dart landing inside a target or a spinner stopping in a certain zone.',
  [('What does geometric probability compare?', ['The area of a favourable region to the area of the entire possible region', 'The number of dice rolled in an experiment', 'A concept unrelated to probability', 'The exact colour of a spinner with no connection to area'], 0),
   ('If a target has a total area of 100 square centimetres and a bullseye area of 20 square centimetres, what is the probability of landing in the bullseye?', ['20 out of 100', '100 out of 20', '80 out of 100', '20 out of 80'], 0),
   ('How does geometric probability differ from counting individual equally likely outcomes?', ['It compares continuous regions of area instead of counting separate discrete outcomes', 'Geometric probability and counting outcomes are always calculated in exactly the same way', 'A concept unrelated to probability', 'Geometric probability can never be applied to a spinner or dartboard'], 0),
   ('On a spinner divided into unequal regions, why might a larger region have a higher probability of being landed on?', ['A larger area typically represents a greater share of the total possible outcomes', 'Every region on a spinner always has an identical probability regardless of size', 'This concept has no connection to probability', 'Smaller regions always have a higher probability than larger ones'], 0),
   ('Why are area models especially useful for probability situations involving continuous space, like a dartboard?', ['They allow probability to be calculated using regions rather than only countable, separate outcomes', 'Area models can only be used when outcomes are countable and separate', 'This concept has no relevance to math', 'Continuous space situations can never be modeled using area'], 0)]),
Sc('The Doppler Effect and Changing Sound',
   'Grade 7 Science strand: the Doppler effect is the change in pitch heard when a sound source moves relative to a listener, with pitch rising as the source approaches and falling as it moves away, caused by sound waves being compressed or stretched.',
   [('What is the Doppler effect?', ['A change in pitch caused by relative motion between a sound source and a listener', 'A change in the colour of an object as it moves', 'A concept unrelated to science', 'A sound that never changes no matter how it moves'], 0),
    ('What happens to the pitch of a siren as an ambulance approaches, then passes by?', ['The pitch sounds higher while approaching and lower after it passes', 'The pitch always stays exactly the same the entire time', 'A concept unrelated to the Doppler effect', 'The pitch becomes silent the moment the ambulance passes'], 0),
    ('What causes sound waves to seem compressed as a source moves toward a listener?', ['The source is catching up slightly to its own previously emitted sound waves', 'Sound waves always spread out further as a source approaches', 'A concept unrelated to sound', 'Compression only happens when a sound source is standing still'], 0),
    ('Why does pitch sound lower as a sound source moves away from a listener?', ['The sound waves are stretched out, lowering their frequency as heard by the listener', 'The sound waves are compressed further as the source moves away', 'This concept has no connection to science', 'Pitch never changes based on the motion of a sound source'], 0),
    ('Which field uses the Doppler effect to help detect the speed and direction of moving objects?', ['Weather radar', 'Basic arithmetic', 'A concept unrelated to the Doppler effect', 'Handwriting analysis'], 0)]),
SS('Social Studies: The 1988 Free Trade Election',
   'Grade 7 Social Studies strand: the 1988 federal election centered on whether Canada should sign a free trade agreement with the United States, with supporters citing economic growth and opponents warning of lost sovereignty and jobs, and the governing party that supported the deal won.',
   [('What major issue was at the center of the 1988 federal election?', ['Whether Canada should sign a free trade agreement with the United States', 'Whether Canada should adopt a new national flag', 'A concept unrelated to Canadian history', 'Whether Canada should end all international trade completely'], 0),
    ('What was one argument made in favour of the proposed free trade agreement?', ['It could increase trade and support economic growth', 'It would guarantee the end of all international trade', 'A concept unrelated to the 1988 election', 'It would have no effect on the economy whatsoever'], 0),
    ('What was one argument made against the proposed free trade agreement?', ['Concerns about losing economic sovereignty and jobs', 'Concerns that trade with the United States would completely stop', 'A concept unrelated to the 1988 election', 'Concerns that the agreement would raise no economic questions at all'], 0),
    ('What was the outcome of the 1988 federal election regarding free trade?', ['The governing party that supported the agreement won and the deal proceeded', 'The election resulted in trade with the United States being banned', 'A concept unrelated to the 1988 election', 'No government was formed as a result of the election'], 0),
    ('What larger trade agreement did the Canada-US Free Trade Agreement later help lead to?', ['The North American Free Trade Agreement (NAFTA)', 'A trade agreement exclusively with countries in Asia', 'A concept unrelated to Canadian trade history', 'An agreement ending all trade with the United States'], 0)]),
]),
day(138, [
L('Reading: Analyzing Anti-Heroes and Morally Complex Characters',
  'Grade 7 Language strand: an anti-hero is a main character who lacks some traditional heroic qualities, such as pure honesty or selflessness, yet still drives the story forward and often reveals a more complicated view of right and wrong.',
  [('What is an anti-hero?', ['A main character who lacks some traditional heroic qualities', 'A character who is always purely good with no flaws', 'A concept unrelated to reading', 'A minor character with no role in the plot'], 0),
   ('Which trait might an anti-hero commonly display?', ['Moral flaws or questionable choices despite being the main character', 'Complete honesty and selflessness at all times', 'A concept unrelated to anti-heroes', 'A total absence of personality or motivation'], 0),
   ('Why might an author choose to write an anti-hero instead of a traditional hero?', ['To create a more realistic or complex view of right and wrong', 'Anti-heroes always make a story less interesting to readers', 'This concept has no connection to literature', 'Every story is required to feature an anti-hero'], 0),
   ('How does an anti-hero generally differ from a villain?', ['An anti-hero is still the main character driving the story, despite flaws, while a villain typically opposes the protagonist', 'An anti-hero and a villain are always exactly the same role in a story', 'This concept has no relevance to reading', 'A villain always narrates the story from the anti-heros point of view'], 0),
   ('Which description best fits an anti-hero?', ['A morally flawed character who still takes center stage in the story', 'A character who is perfectly virtuous in every situation', 'A concept unrelated to literary characters', 'A character who never appears in the story at all'], 0)]),
M('Algebra: Solving Word Problems with Consecutive Integers',
  'Grade 7 Math strand: consecutive integers are whole numbers that follow each other in order, such as 5, 6, and 7, and word problems about them can be solved by representing the unknown integers algebraically as n, n+1, n+2, and so on.',
  [('What are consecutive integers?', ['Whole numbers that follow each other in order, such as 5, 6, and 7', 'Numbers that are always separated by a gap of at least ten', 'A concept unrelated to algebra', 'Numbers that must all be equal to each other'], 0),
   ('How might three consecutive integers be represented algebraically?', ['n, n+1, and n+2', 'n, 2n, and 3n', 'A concept unrelated to consecutive integers', 'n, n, and n'], 0),
   ('If three consecutive integers add up to 60, which equation represents this situation?', ['n + (n+1) + (n+2) = 60', 'n + n + n = 60 with no adjustment', 'A concept unrelated to algebra', '3n + 2 = 60 with no other terms'], 0),
   ('Using n + (n+1) + (n+2) = 60, what is the value of n?', ['19', '20', '21', '18'], 0),
   ('Why is representing consecutive integers algebraically helpful when solving these word problems?', ['It turns a wordy description into a solvable equation with a single unknown', 'Algebra can never be used to represent consecutive integers', 'This concept has no connection to math', 'Consecutive integer problems can only be solved by guessing randomly'], 0)]),
Sc('Renewable Energy: Hydrogen Fuel Cells',
   'Grade 7 Science strand: a hydrogen fuel cell generates electricity through a chemical reaction between hydrogen and oxygen, producing water as its main byproduct, making it a clean energy option though challenges remain around storing and producing hydrogen.',
   [('What does a hydrogen fuel cell use to generate electricity?', ['A chemical reaction between hydrogen and oxygen', 'Burning coal in a large furnace', 'A concept unrelated to renewable energy', 'Sunlight captured by a solar panel'], 0),
    ('What is the main byproduct produced by a hydrogen fuel cell?', ['Water', 'Thick black smoke', 'A concept unrelated to hydrogen fuel cells', 'Large amounts of solid ash'], 0),
    ('Why are hydrogen fuel cells often considered a clean energy option?', ['They produce water rather than carbon emissions at the point of use', 'They release large amounts of carbon dioxide directly into the air', 'A concept unrelated to renewable energy', 'They require burning fossil fuels to operate at all'], 0),
    ('What is one challenge associated with using hydrogen fuel cells widely?', ['Storing and producing hydrogen can be difficult and energy-intensive', 'Hydrogen is the easiest possible fuel to store and never requires any energy to produce', 'This concept has no connection to science', 'Hydrogen fuel cells have no challenges at all'], 0),
    ('Which of these is a real-world application of hydrogen fuel cell technology?', ['Powering certain vehicles and buses', 'Powering a device with no moving parts or electrical needs', 'A concept unrelated to hydrogen fuel cells', 'Replacing all forms of transportation immediately worldwide'], 0)]),
SS('Social Studies: The History of O Canada and National Symbols',
   'Grade 7 Social Studies strand: O Canada was composed in 1880 and became Canadas official national anthem in 1980, joining other national symbols like the Maple Leaf flag as a shared marker of Canadian identity.',
   [('In approximately what year was the music for O Canada composed?', ['1880', '1867', '1965', '1982'], 0),
    ('In what year did O Canada officially become Canadas national anthem?', ['1980', '1867', '1920', '1945'], 0),
    ('Who composed the original music for O Canada?', ['Calixa Lavallee', 'Sir John A. Macdonald', 'Lester B. Pearson', 'Pierre Trudeau'], 0),
    ('Why are national symbols like an anthem considered important to a country?', ['They can help foster a shared sense of identity and belonging among citizens', 'National symbols have no effect on how citizens view their country', 'A concept unrelated to social studies', 'Anthems are chosen randomly with no connection to national identity'], 0),
    ('Besides the national anthem, which of these is also considered a well-known Canadian national symbol?', ['The maple leaf', 'A symbol used exclusively by one province', 'A concept unrelated to national symbols', 'A symbol with no connection to Canadian identity'], 0)]),
]),
day(139, [
L('Writing: Writing a Podcast Script',
  'Grade 7 Language strand: a podcast script plans out an audio show with a strong opening hook, clearly organized segments, natural transitions, and a conversational tone suited to being heard rather than read.',
  [('What should a podcast script generally include?', ['A strong opening hook, organized segments, and clear transitions', 'Only a single unbroken paragraph with no structure', 'A concept unrelated to writing', 'A list of unrelated topics with no connections between them'], 0),
   ('Why does a podcast script often use a conversational tone?', ['Because listeners are hearing the words rather than reading them, so natural speech feels more engaging', 'A conversational tone is never appropriate for an audio format', 'A concept unrelated to podcast scripts', 'Podcasts are always written in a strictly formal, academic style'], 0),
   ('Why might a podcast script include notes for sound cues or music transitions?', ['To help guide pacing and signal shifts between segments for the listener', 'Sound cues are never included in a podcast script', 'This concept has no connection to writing', 'Music transitions always confuse listeners with no benefit'], 0),
   ('Why is a strong opening hook important in a podcast script?', ['It helps capture listener interest right away, before they decide whether to keep listening', 'The opening of a podcast never affects whether listeners keep listening', 'This concept has no relevance to writing', 'A podcast script should always begin with the credits'], 0),
   ('Which excerpt sounds most like the opening of a podcast script?', ['Welcome back to the show. Today we are diving into a mystery that stumped scientists for decades.', 'Add 15 and 20 to get 35.', 'The chemical symbol for gold is Au.', 'Please find attached the quarterly financial report.'], 0)]),
M('Geometry: Indirect Measurement Using Similar Triangles',
  'Grade 7 Math strand: indirect measurement uses similar triangles, such as the triangles formed by an object and its shadow, to calculate a height or distance that would be difficult to measure directly, by setting up a proportion between corresponding sides.',
  [('What is indirect measurement?', ['A method of finding a measurement, like height, without measuring it directly', 'A method that always requires physically climbing to the top of an object', 'A concept unrelated to geometry', 'A method that can only be used on objects smaller than one metre'], 0),
   ('Why are similar triangles useful for indirect measurement problems involving shadows?', ['The triangles formed by an object and its shadow are proportional to a second object and its shadow', 'Similar triangles have no connection to shadows or height', 'A concept unrelated to geometry', 'Shadows never form triangles of any kind'], 0),
   ('If a 2 metre tall post casts a 3 metre shadow at the same time a tree casts a 9 metre shadow, how tall is the tree?', ['6 metres', '9 metres', '3 metres', '13.5 metres'], 0),
   ('What must be true about the two triangles used in an indirect measurement problem for the method to work?', ['They must be similar, with proportional corresponding sides', 'They must be exactly the same size with no proportional relationship needed', 'A concept unrelated to indirect measurement', 'They must have no shared angles at all'], 0),
   ('Why might indirect measurement be useful for finding the height of a very tall building?', ['It avoids the need to physically climb or directly measure an object that is difficult to reach', 'Indirect measurement can only be used on objects at ground level', 'This concept has no relevance to geometry', 'Tall buildings can always be measured directly with a small ruler'], 0)]),
Sc('The Process of Fermentation',
   'Grade 7 Science strand: fermentation is a process in which microorganisms like yeast and bacteria break down sugars without using oxygen, producing byproducts such as carbon dioxide or lactic acid that are used in foods like bread and yogurt.',
   [('What is fermentation?', ['A process in which microorganisms break down sugars without using oxygen', 'A process that always requires large amounts of oxygen', 'A concept unrelated to science', 'A process that only occurs inside rocks'], 0),
    ('Which microorganism is commonly responsible for making bread dough rise?', ['Yeast', 'A type of large mammal', 'A concept unrelated to fermentation', 'A species of tree'], 0),
    ('What gas is produced by yeast during the fermentation of bread dough?', ['Carbon dioxide', 'Oxygen only', 'A concept unrelated to fermentation', 'Helium'], 0),
    ('Why has fermentation historically been important for preserving food?', ['It can slow the growth of harmful microorganisms and extend how long food stays edible', 'Fermentation always causes food to spoil more quickly', 'This concept has no connection to science', 'Fermentation has never been used in food preparation'], 0),
    ('What role do bacteria play in the fermentation process used to make yogurt?', ['They produce lactic acid, which thickens and flavours the milk', 'They have no effect on the milk at all', 'A concept unrelated to fermentation', 'They convert the milk directly into a solid metal'], 0)]),
SS('Social Studies: The History of the CBC and Public Broadcasting',
   'Grade 7 Social Studies strand: the Canadian Broadcasting Corporation, founded in 1936, is a publicly funded broadcaster created to provide Canadian news and cultural programming in both English and French, helping to counter the influence of foreign broadcast signals.',
   [('What is the CBC?', ['A publicly funded Canadian broadcaster', 'A privately owned foreign broadcasting company', 'A concept unrelated to Canadian history', 'A company that only produces printed newspapers'], 0),
    ('Why was a public broadcaster created in Canada in the 1930s?', ['To provide Canadian content and help counter the influence of foreign broadcast signals', 'To completely eliminate radio broadcasting in Canada', 'A concept unrelated to the CBC', 'To broadcast programming exclusively from other countries'], 0),
    ('How is the CBC primarily funded?', ['Through public funding from the government', 'Entirely through a single private investor', 'A concept unrelated to public broadcasting', 'The CBC receives no funding of any kind'], 0),
    ('What is one goal of public broadcasting in Canada?', ['Providing news and cultural programming in both English and French', 'Broadcasting only in a single language with no other option', 'A concept unrelated to the CBC', 'Avoiding any coverage of Canadian news or culture'], 0),
    ('In approximately what year was the CBC founded?', ['1936', '1867', '1982', '1965'], 0)]),
]),
day(140, [
L('Language Review: Grammar, Vocabulary, Reading, Media Literacy, and Writing',
  'Grade 7 Language strand review: students revisit relative clauses, malapropisms, literary archetypes, evaluating influencer marketing, and writing a podcast script.',
  [('What is a relative clause?', ['A clause that adds extra information about a noun using a relative pronoun', 'A clause that always stands alone as its own sentence', 'A concept unrelated to grammar', 'A clause that never connects to any noun'], 0),
   ('What is a malapropism?', ['The mistaken use of a word in place of a similar-sounding word', 'A word that has exactly one correct meaning', 'A concept unrelated to vocabulary', 'A word that never appears in dialogue'], 0),
   ('What is a literary archetype?', ['A recurring character type or pattern found across many stories', 'A character that appears in only one story ever written', 'A concept unrelated to reading', 'A type of punctuation used in dialogue'], 0),
   ('What is influencer marketing?', ['When a social media personality promotes a product, often for payment', 'A completely unpaid recommendation with no business relationship', 'A concept unrelated to media literacy', 'A type of printed magazine advertisement only'], 0),
   ('What should a podcast script generally include?', ['A strong opening hook, organized segments, and clear transitions', 'Only a single unbroken paragraph with no structure', 'A concept unrelated to writing', 'A list of unrelated topics with no connections between them'], 0)]),
M('Math Review: Data, Geometry, Financial Literacy, Probability, and Algebra',
  'Grade 7 Math strand review: students revisit mean absolute deviation, angle relationships in parallel lines, mortgages and amortization, geometric probability, and consecutive integer word problems.',
  [('What does mean absolute deviation (MAD) measure?', ['The average distance between each data value and the mean', 'The single highest value in a data set', 'A concept unrelated to data management', 'The total number of values in a data set'], 0),
   ('What is a transversal?', ['A line that crosses two or more other lines', 'A line that never intersects any other line', 'A concept unrelated to geometry', 'A line segment with no defined length'], 0),
   ('What is a mortgage?', ['A long-term loan used to purchase property', 'A one-time payment made in full with no borrowing involved', 'A concept unrelated to financial literacy', 'A type of savings account with no connection to borrowing'], 0),
   ('What does geometric probability compare?', ['The area of a favourable region to the area of the entire possible region', 'The number of dice rolled in an experiment', 'A concept unrelated to probability', 'The exact colour of a spinner with no connection to area'], 0),
   ('What are consecutive integers?', ['Whole numbers that follow each other in order, such as 5, 6, and 7', 'Numbers that are always separated by a gap of at least ten', 'A concept unrelated to algebra', 'Numbers that must all be equal to each other'], 0)]),
Sc('Science Review: Astronomy, Earth Science, Physics, Technology, and Biology',
   'Grade 7 Science strand review: students revisit comets and asteroids, permafrost and the cryosphere, light and colour, nanotechnology, and circadian rhythms.',
   [('What is a comet mostly made of?', ['Ice, dust, and rocky material', 'Pure liquid water only', 'A concept unrelated to astronomy', 'Solid metal with no ice at all'], 0),
    ('What is permafrost?', ['Ground that has remained frozen for two or more consecutive years', 'Ground that has never once frozen in recorded history', 'A concept unrelated to earth science', 'A type of rock found only underwater'], 0),
    ('Why does an object appear a particular colour, such as red?', ['It reflects that wavelength of light while absorbing most other wavelengths', 'It creates that colour of light entirely on its own with no outside light needed', 'A concept unrelated to science', 'Colour has no connection to light at all'], 0),
    ('What is nanotechnology?', ['The design and manipulation of materials at an extremely small, nanometre scale', 'The study of objects that are visible only from space', 'A concept unrelated to science', 'A technology that only works on objects larger than a house'], 0),
    ('What is a circadian rhythm?', ['An internal biological clock that repeats roughly every 24 hours', 'A rhythm that only occurs once per year', 'A concept unrelated to biology', 'A pattern found only in plants, never in animals'], 0)]),
SS('Social Studies Review: Confederation, Constitution, and Canadian Identity',
   'Grade 7 Social Studies strand review: students revisit the Fenian Raids, the National Policy of 1879, the patriation of the constitution, the flag debate of 1964, and the history of the CBC.',
   [('What were the Fenian Raids?', ['A series of armed incursions into British North America by an Irish-American group', 'A peaceful trade negotiation between Canada and Ireland', 'A concept unrelated to Canadian history', 'A series of scientific expeditions across the Arctic'], 0),
    ('What was the National Policy of 1879?', ['An economic strategy combining tariffs, a transcontinental railway, and western immigration', 'A treaty ending a war between Canada and another country', 'A concept unrelated to Canadian history', 'A policy focused only on education reform'], 0),
    ('What does patriation of the constitution mean?', ['Bringing full authority over the constitution under Canadian control', 'Sending the constitution to another country for approval', 'A concept unrelated to Canadian history', 'Removing the constitution from use entirely'], 0),
    ('What was the Great Canadian Flag Debate of 1964 about?', ['Choosing a new national flag design to replace the existing one', 'Deciding whether Canada should adopt a new national anthem', 'A concept unrelated to Canadian history', 'Choosing the location of a new national capital'], 0),
    ('What is the CBC?', ['A publicly funded Canadian broadcaster', 'A privately owned foreign broadcasting company', 'A concept unrelated to Canadian history', 'A company that only produces printed newspapers'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g7_131_140)
    append_to(7, g7_131_140)
