#!/usr/bin/env python3
"""Grade 2, Days 161-170 -- fourteenth batch, extending Grade 2 past Day 160
toward the full ~187-day school year. Uses the sub()/day()/append_to()
helpers imported directly from gen_curriculum.py (no worksheet field --
Grade 2's sub() signature is exactly (subject_key, title, summary,
resourceLabel, resourceUrl, quiz), confirmed by reading gen_curriculum.py
directly and by reading gen_grade2_days151_160.py, the immediately prior
batch for this grade, which confirms the same in its own docstring after
checking; there is no worksheet argument anywhere in Grade 2's current
generator scripts, and no append_worksheet_days() function is used by
Grade 2 past roughly Day 100 -- that helper only appears in the Grade 0
and Grade 1 scripts and in Grade 2's much older Days 31-100 scripts):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by the video-backfill task)

Topics chosen to avoid overlap with existing Grade 2 Days 1-160 (dumped
and checked against data/grade2.json before writing, which already
densely covers nearly the full grade 2 ELA, math, science, and social
studies curriculum):

Language: riddles, haiku, shape (concrete) poems, possessive pronouns,
news reports, word sorts, tongue twisters, comparing different versions
of the same story, and environmental print -- none of which appear in
the existing Days 1-160 Language coverage (which already includes
similes, metaphors, personification, hyperbole, alliteration, assonance
and consonance, onomatopoeia, idioms, adages and proverbs, analogies,
acrostic poems, list poems, free verse poetry, and possessive nouns,
among dozens of other topics).

Math: recognizing equal parts of a whole, unit fractions, creating a
pictograph with a key, reading a calendar (days/weeks/months), comparing
how long activities take, ordinal numbers from eleventh to twentieth,
geometric slides/flips/turns, Canadian coin values by name, and writing
numbers in word form. (Multiplication and division facts, most fraction
topics, most graph types, most time-telling topics, and ordinal numbers
one through tenth are already exhaustively covered across Days 1-160, so
new angles distinct from that existing coverage were chosen instead.)

Science: earthworms, octopuses, turtles, dinosaurs and fossils, mountain
habitats, cave habitats, glaciers, earthquakes, and ants -- none of which
appear in the very dense existing Days 1-160 science coverage (which
already includes sharks, penguins, bats, spiders, whales and dolphins,
deserts, rainforests, tundra, wetlands, grasslands and prairies, ocean
zones, coral reefs, the rock cycle, volcanoes, erosion, weathering, and
ice ages, among dozens of other animals, habitats, and earth science
topics).

Social Studies: the Supreme Court of Canada, Canada's national motto, the
poppy as a symbol of remembrance, lacrosse as Canada's national summer
sport, the Great Lakes, Canadian Thanksgiving, public transit, farmers
markets, and the CN Tower -- distinct from the existing Governor General,
Senate, Order of Canada, hockey, Niagara Falls, Canadian currency,
Canadian holidays (Canada Day and Remembrance Day generally), and famous
landmarks lessons already in Days 1-160.

Day 170 is a review day across all four subjects, matching the
end-of-batch pattern used in every prior 10-day batch (Day 140, Day 150,
Day 160, etc). Its four review titles are textually distinct from every
earlier review title in Days 1-160. No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz
text -- contractions and possessives are avoided entirely (or rewritten
without the apostrophe, e.g. "Canadas" not "Canada's") to keep the
generated .ts string literals valid.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to


def mk(subject_key, title, summary, quiz):
    rl = f'YouTube: {title}'
    ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{title} grade 2 educational')
    return sub(subject_key, title, summary, rl, ru, quiz)


def L(t, s, q):
    return mk('Language', t, s, q)


def M(t, s, q):
    return mk('Math', t, s, q)


def Sc(t, s, q):
    return mk('Science', t, s, q)


def SS(t, s, q):
    return mk('SocialStudies', t, s, q)


def _rebalance_answer_positions(days, seed=20260813):
    import random
    rng = random.Random(seed)
    all_quizzes = [quiz for _, subs in days for *_, quiz in subs]
    n = sum(len(quiz) for quiz in all_quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in all_quizzes:
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


g2_161_170 = [
day(161, [
L('Riddles: Writing Playful Questions and Answers',
  'Grade 2 Language strand: a riddle is a playful question with a clue-filled answer, often using wordplay or hidden meanings to make the reader think and smile.',
  [('What is a riddle?', ['A playful question with a clue-filled answer', 'A true news report', 'A math equation', 'A silent letter'], 0),
   ('Riddles often use ___ to make the reader think and guess.', ['Clues and wordplay', 'Loud noises only', 'Long lists of facts', 'Blank pages'], 0),
   ('Why might a writer include a riddle in a story?', ['To entertain and challenge the reader', 'To end the story with no reason', 'To remove all humour from the text', 'To confuse the reader with no clues at all'], 0),
   ('A good riddle usually has a clear ___ at the end.', ['Answer', 'Ending in silence', 'New character', 'No purpose'], 0),
   ('Which of these is written like a riddle?', ['What has keys but cannot open a door', 'The sky is blue', 'I ran to school today', 'Water is a liquid'], 0)]),
M('Fractions: Recognizing Equal Parts of a Whole',
  'Grade 2 Math strand: for a shape to show a true fraction, it must be divided into parts that are all the same size, called equal parts.',
  [('For a fraction to be shown correctly, a shape must be divided into ___.', ['Equal parts', 'Random sized pieces', 'Only two pieces', 'Different sized pieces'], 0),
   ('If a circle is cut into four parts, but they are different sizes, does it correctly show fourths?', ['No', 'Yes', 'Sometimes', 'Only on weekends'], 0),
   ('Which of these correctly shows halves?', ['A rectangle split into two equal parts', 'A rectangle split into two very different sized parts', 'A rectangle with no lines', 'A rectangle split into five parts'], 0),
   ('Why do fractions require equal parts?', ['So each part represents the same amount of the whole', 'Equal parts are never needed', 'Fractions ignore size completely', 'Only whole numbers need equal parts'], 0),
   ('A shape split into three equal parts shows ___.', ['Thirds', 'Halves', 'Fourths', 'Fifths'], 0)]),
Sc('Earthworms: Helpers Beneath the Soil',
   'Grade 2 Science strand: earthworms live underground and help the soil by tunnelling through it, letting in air and water, and breaking down dead plant material.',
   [('Where do earthworms usually live?', ['Underground in soil', 'In the ocean', 'In trees', 'In the sky'], 0),
    ('How do earthworms help soil?', ['By tunnelling and letting in air and water', 'By removing all air from soil', 'By making soil harder', 'By covering soil with ice'], 0),
    ('What do earthworms often eat?', ['Dead plant material in the soil', 'Only rocks', 'Only metal', 'Nothing at all'], 0),
    ('Why are earthworms sometimes called helpers of the garden?', ['They improve soil health for plants to grow', 'They destroy every plant', 'They have no effect on gardens', 'They only live in water'], 0),
    ('Earthworms are an example of an animal that lives ___.', ['Mostly underground', 'Mostly in the clouds', 'Mostly on ice', 'Mostly underwater in the ocean'], 0)]),
SS('The Supreme Court of Canada: The Highest Court in the Land',
   'Grade 2 Social Studies strand: the Supreme Court of Canada is the highest court in the country, making final decisions on the most important legal cases.',
   [('What is the Supreme Court of Canada?', ['The highest court in the country', 'A local library', 'A type of school', 'A city council'], 0),
    ('What does the Supreme Court do?', ['Makes final decisions on the most important legal cases', 'Delivers mail', 'Teaches students', 'Builds roads'], 0),
    ('Why is the Supreme Court considered the highest court?', ['Its decisions are final and cannot be appealed to a higher court', 'It is the smallest court', 'It has no real power', 'It only handles minor disagreements'], 0),
    ('Which of these might the Supreme Court decide on?', ['Important legal questions affecting the whole country', 'What food to serve at lunch', 'Which movie to watch', 'What time recess starts'], 0),
    ('The word supreme in Supreme Court means ___.', ['Highest or greatest', 'Smallest', 'Newest', 'Quietest'], 0)]),
]),
day(162, [
L('Haiku: Poems Built From Counting Syllables',
  'Grade 2 Language strand: a haiku is a short poem, often about nature, made of three lines with a pattern of five, seven, and five syllables.',
  [('How many lines does a haiku usually have?', ['3', '5', '10', '1'], 0),
   ('What is the usual syllable pattern of a haiku?', ['Five, seven, five', 'Four, four, four', 'Ten, ten, ten', 'Two, two, two'], 0),
   ('What topic do haiku poems often describe?', ['Nature', 'Math facts', 'Grocery lists', 'Traffic signs'], 0),
   ('A syllable is ___.', ['A beat or chunk of sound in a word', 'A punctuation mark', 'A whole sentence', 'A silent letter only'], 0),
   ('Why might counting syllables be tricky when writing a haiku?', ['Some words have more beats than they first seem', 'Words never have syllables', 'Haiku have no rules at all', 'Syllables are always exactly one per word'], 0)]),
M('Fractions: Unit Fractions and Their Names',
  'Grade 2 Math strand: a unit fraction has a numerator of one, like 1/2, 1/3, or 1/4, and represents a single equal part of a whole.',
  [('What is a unit fraction?', ['A fraction with a numerator of one', 'A fraction with a denominator of one', 'A whole number', 'A fraction with no parts'], 0),
   ('Which of these is a unit fraction?', ['1/4', '2/4', '3/4', '4/4'], 0),
   ('In the fraction 1/5, what does the 1 represent?', ['One equal part out of the whole', 'Five equal parts', 'The whole itself', 'Nothing at all'], 0),
   ('Which of these is NOT a unit fraction?', ['3/5', '1/2', '1/3', '1/6'], 0),
   ('A unit fraction always has a numerator of ___.', ['One', 'Two', 'Zero', 'Ten'], 0)]),
Sc('Octopuses: Clever Creatures of the Sea',
   'Grade 2 Science strand: octopuses are intelligent ocean animals with eight arms, soft bodies, and the ability to change colour to blend into their surroundings.',
   [('How many arms does an octopus have?', ['Eight', 'Four', 'Six', 'Two'], 0),
    ('What can an octopus do to blend into its surroundings?', ['Change colour', 'Grow wings', 'Breathe fire', 'Fly'], 0),
    ('Where do octopuses live?', ['In the ocean', 'In deserts', 'In trees', 'In the sky'], 0),
    ('What kind of body does an octopus have?', ['Soft, without a bony skeleton', 'Hard and covered in scales', 'Covered in fur', 'Made only of bone'], 0),
    ('Octopuses are often described as one of the most ___ ocean animals.', ['Intelligent', 'Least active', 'Loudest', 'Largest'], 0)]),
SS('From Sea to Sea: Canadas National Motto',
   'Grade 2 Social Studies strand: Canadas national motto, A Mari Usque Ad Mare, means from sea to sea and reflects the countrys vast size stretching between oceans.',
   [('What does Canadas national motto mean in English?', ['From sea to sea', 'From coast to mountain', 'From north to south only', 'From city to city'], 0),
    ('What does the motto reflect about Canada?', ['The countrys vast size stretching between oceans', 'That Canada has no coastline', 'That Canada is a very small country', 'That Canada has only one ocean'], 0),
    ('A national motto is ___.', ['A short phrase that represents a countrys identity', 'A type of currency', 'A national holiday', 'A kind of map'], 0),
    ('How many oceans touch Canadas coastlines?', ['Three', 'One', 'Zero', 'Ten'], 0),
    ('Why might a country choose a motto about its geography?', ['To capture something important about its identity', 'Mottoes never relate to geography', 'Countries never have mottoes', 'To confuse citizens'], 0)]),
]),
day(163, [
L('Shape Poems: Writing Poetry in a Picture',
  'Grade 2 Language strand: a shape poem, also called a concrete poem, arranges its words so the poem itself forms the outline of its topic, like a poem about a tree shaped like a tree.',
  [('What makes a shape poem special?', ['The words are arranged to form the outline of the topic', 'It has no words at all', 'It must rhyme perfectly', 'It has exactly one line'], 0),
   ('A shape poem about a snake might be arranged in a ___ pattern.', ['Curvy, winding', 'Perfectly square', 'Random scattered dots', 'A single straight column of numbers'], 0),
   ('A shape poem is also known as a ___ poem.', ['Concrete', 'Silent', 'Numeric', 'Blank'], 0),
   ('Why might a poet choose to write a shape poem?', ['To connect the look of the poem to its meaning', 'To hide the topic completely', 'To remove all imagery', 'To avoid choosing a topic'], 0),
   ('Which topic could work well for a shape poem?', ['A poem about a balloon shaped like a circle', 'A poem about nothing', 'A poem with no topic', 'A poem about silence only'], 0)]),
M('Data: Creating a Pictograph With a Key',
  'Grade 2 Math strand: a pictograph uses pictures to represent data, and a key tells the reader how many items each picture stands for, such as one picture equalling two votes.',
  [('What does a key on a pictograph tell the reader?', ['How many items each picture represents', 'The title of the graph only', 'The colour of the picture', 'Nothing important'], 0),
   ('If the key shows one picture equals two votes, how many votes do three pictures represent?', ['6', '3', '2', '9'], 0),
   ('Why is a key important when creating a pictograph?', ['It helps readers correctly interpret the data', 'It has no real purpose', 'It only decorates the graph', 'It replaces the need for pictures'], 0),
   ('Which of these could be a picture used in a pictograph about favourite fruits?', ['A small apple symbol', 'A random letter', 'A blank square', 'A punctuation mark'], 0),
   ('A pictograph is especially useful for showing data in a way that is ___.', ['Visual and easy to compare', 'Impossible to understand', 'Written only in words', 'Always inaccurate'], 0)]),
Sc('Turtles: Reptiles With Shells',
   'Grade 2 Science strand: turtles are reptiles with a hard shell that protects their soft body, and many species can pull their head and legs inside the shell for safety.',
   [('What protects a turtles soft body?', ['A hard shell', 'Feathers', 'Fur', 'Scales alone with no shell'], 0),
    ('What can many turtles do when they feel threatened?', ['Pull their head and legs into their shell', 'Fly away', 'Change colour', 'Grow larger instantly'], 0),
    ('What type of animal is a turtle classified as?', ['A reptile', 'A mammal', 'A bird', 'An insect'], 0),
    ('Which of these describes most turtles?', ['Cold-blooded animals with a protective shell', 'Warm-blooded animals with fur', 'Animals with wings', 'Animals with no legs at all'], 0),
    ('Why is a turtles shell an important adaptation?', ['It provides protection from predators', 'It has no purpose', 'It prevents the turtle from moving at all', 'It makes the turtle heavier for no reason'], 0)]),
SS('The Poppy: A Symbol of Remembrance',
   'Grade 2 Social Studies strand: the poppy is a red flower worn as a symbol of remembrance to honour those who served and died in wars, especially around Remembrance Day.',
   [('What does the poppy symbolize?', ['Remembrance of those who served and died in wars', 'A type of currency', 'A community sport', 'A kind of weather'], 0),
    ('What colour is the poppy most associated with remembrance?', ['Red', 'Blue', 'Yellow', 'Purple'], 0),
    ('Around which day do people often wear a poppy?', ['Remembrance Day', 'Canada Day', 'Thanksgiving', 'Victoria Day'], 0),
    ('Why do people choose to wear a poppy?', ['To honour and remember those who served', 'To celebrate a sports victory', 'To mark a birthday', 'To show the weather forecast'], 0),
    ('The poppy is an example of a ___.', ['Symbol', 'Type of money', 'Kind of vehicle', 'Musical instrument'], 0)]),
]),
day(164, [
L('Possessive Pronouns: Mine, Yours, His, and Hers',
  'Grade 2 Language strand: a possessive pronoun shows who something belongs to without using an apostrophe, such as mine, yours, his, hers, its, ours, and theirs.',
  [('What does a possessive pronoun show?', ['Who something belongs to', 'A question', 'An action', 'A feeling only'], 0),
   ('Which word is a possessive pronoun?', ['Mine', 'Run', 'Blue', 'Quickly'], 0),
   ('In the sentence This book is hers, which word is the possessive pronoun?', ['Hers', 'Book', 'Is', 'This'], 0),
   ('Do possessive pronouns use an apostrophe?', ['No, they do not', 'Yes, always', 'Only on Fridays', 'Only for names'], 0),
   ('Which sentence uses a possessive pronoun correctly?', ['The red bike is mine', 'The red bike is I', 'The red bike is she', 'The red bike is they'], 0)]),
M('Calendars: Days, Weeks, and Months of the Year',
  'Grade 2 Math strand: a calendar organizes time into days, weeks, and months, helping us track dates, plan events, and understand how much time has passed.',
  [('How many days are in one week?', ['7', '5', '10', '30'], 0),
   ('How many months are in one year?', ['12', '7', '52', '4'], 0),
   ('A calendar helps us keep track of ___.', ['Dates and events', 'Only the weather', 'Only the temperature', 'Nothing important'], 0),
   ('If today is Monday, what day comes next?', ['Tuesday', 'Sunday', 'Friday', 'Wednesday'], 0),
   ('About how many weeks are in one year?', ['52', '12', '7', '365'], 0)]),
Sc('Dinosaurs: Learning From Fossils',
   'Grade 2 Science strand: dinosaurs were animals that lived millions of years ago, and scientists learn about them today mainly by studying fossils, the preserved remains or traces left in rock.',
   [('How do scientists learn about dinosaurs today?', ['By studying fossils', 'By watching them in person', 'By reading old newspapers', 'By guessing with no evidence'], 0),
    ('What is a fossil?', ['A preserved remain or trace of an ancient living thing', 'A living dinosaur', 'A type of rock with no history', 'A modern animal bone'], 0),
    ('When did dinosaurs live?', ['Millions of years ago', 'Last year', 'One hundred years ago', 'Next year'], 0),
    ('Why are fossils important to scientists?', ['They provide clues about ancient life', 'They have no scientific value', 'They only show modern animals', 'They are always fake'], 0),
    ('Which of these might a fossil preserve?', ['The shape of a dinosaur bone', 'A live dinosaur sound recording', 'A photograph', 'A video'], 0)]),
SS('Lacrosse: Canadas National Summer Sport',
   'Grade 2 Social Studies strand: lacrosse is recognized as Canadas official national summer sport, a fast game played with a small ball and a long stick with a net at the end.',
   [('What is lacrosse recognized as in Canada?', ['The national summer sport', 'The national winter sport', 'A type of food', 'A type of currency'], 0),
    ('What equipment is used to play lacrosse?', ['A stick with a net at the end', 'A racket and a shuttlecock', 'A bat and a glove', 'A puck and skates'], 0),
    ('Is lacrosse usually played in summer or winter?', ['Summer', 'Winter', 'Neither season', 'Only underwater'], 0),
    ('Which of these describes lacrosse?', ['A fast game played with a small ball', 'A slow game played with no ball', 'A game played only on ice', 'A board game'], 0),
    ('Which sport is often called Canadas national winter sport, alongside lacrosse as the summer one?', ['Hockey', 'Soccer', 'Basketball', 'Tennis'], 0)]),
]),
day(165, [
L('News Reports: Writing Just the Facts',
  'Grade 2 Language strand: a news report shares real events by answering who, what, where, when, and why, using clear facts instead of opinions.',
  [('What is the main purpose of a news report?', ['To share real events using facts', 'To tell a made-up fairy tale', 'To give only opinions', 'To write a poem'], 0),
   ('Which questions does a good news report usually answer?', ['Who, what, where, when, and why', 'Only where', 'Only why', 'None of these'], 0),
   ('A news report should be based on ___.', ['Facts', 'Made-up events only', 'Opinions only', 'Guesses with no evidence'], 0),
   ('Which of these sounds most like a line from a news report?', ['Firefighters arrived at the school at nine in the morning', 'Once upon a time in a faraway land', 'I think pizza is the best food', 'Roses are red'], 0),
   ('Why is it important for a news report to stick to facts?', ['So readers can trust the information', 'Facts are never useful', 'Opinions are always better', 'News reports should confuse readers'], 0)]),
M('Time: Comparing How Long Activities Take',
  'Grade 2 Math strand: some activities take more time than others, and students can compare durations to decide which activity takes longer or shorter to complete.',
  [('Which activity most likely takes longer?', ['A full school day', 'Brushing your teeth', 'Tying your shoe', 'Blinking your eyes'], 0),
   ('Which activity most likely takes a shorter amount of time?', ['Clapping your hands once', 'Watching a movie', 'Sleeping overnight', 'A full school day'], 0),
   ('Why might it be useful to compare how long activities take?', ['It helps with planning and understanding time', 'It has no real use', 'It removes the need for clocks', 'It makes time disappear'], 0),
   ('Which is the better estimate for how long it takes to eat breakfast?', ['A few minutes', 'A few seconds', 'A few days', 'A few months'], 0),
   ('Comparing durations means deciding which activity takes ___ time.', ['More or less', 'Only more', 'Only the same', 'No'], 0)]),
Sc('Mountain Habitats: Life at High Elevations',
   'Grade 2 Science strand: mountain habitats are found at high elevations where the air is thinner and colder, and the plants and animals that live there have special adaptations to survive.',
   [('What is the air like at high elevations on a mountain?', ['Thinner and colder', 'Thicker and hotter', 'Exactly the same as at sea level', 'Full of water'], 0),
    ('Why do mountain animals need special adaptations?', ['To survive the cold and thin air', 'Mountains have no unique conditions', 'All habitats are identical', 'Adaptations are never needed'], 0),
    ('Which of these might be found on a mountain habitat?', ['Thick fur to stay warm', 'Fins for swimming only', 'Gills for breathing underwater', 'No adaptations at all'], 0),
    ('As elevation increases on a mountain, temperature usually ___.', ['Decreases', 'Increases', 'Stays exactly the same', 'Disappears'], 0),
    ('A mountain habitat is an example of a habitat shaped mainly by ___.', ['Elevation and climate', 'Ocean currents', 'Underground caves', 'City streets'], 0)]),
SS('The Great Lakes: Canadas Freshwater Giants',
   'Grade 2 Social Studies strand: the Great Lakes are a group of five enormous freshwater lakes along the border between Canada and the United States, holding a huge share of the worlds fresh water.',
   [('How many Great Lakes are there?', ['Five', 'Three', 'Seven', 'Two'], 0),
    ('What kind of water do the Great Lakes hold?', ['Fresh water', 'Salt water', 'No water', 'Frozen water only'], 0),
    ('Where are the Great Lakes located?', ['Along the border between Canada and the United States', 'In northern Europe', 'In the middle of the ocean', 'In the desert'], 0),
    ('Why are the Great Lakes considered important?', ['They hold a huge share of the worlds fresh water', 'They have no fresh water at all', 'They are located in the desert', 'They are very small ponds'], 0),
    ('The Great Lakes are an example of ___.', ['A geographic feature', 'A type of government', 'A national holiday', 'A kind of currency'], 0)]),
]),
day(166, [
L('Word Sorts: Grouping Words by Spelling Pattern',
  'Grade 2 Language strand: a word sort is an activity where students group words that share a spelling pattern, sound, or meaning to notice patterns in language.',
  [('What is a word sort?', ['Grouping words that share a pattern', 'A type of punctuation', 'A silent letter', 'A math activity'], 0),
   ('Which of these could be a spelling pattern used in a word sort?', ['Words ending in -at', 'A single random letter', 'A whole paragraph', 'A picture with no words'], 0),
   ('Why do students practise word sorts?', ['To notice patterns and improve spelling', 'To remove all patterns from words', 'To make reading harder', 'To avoid learning new words'], 0),
   ('If sorting by vowel sound, which words might belong together?', ['Cake, rain, and day', 'Cake, dog, and cup', 'Rain, dog, and fish', 'Day, cup, and pen'], 0),
   ('A word sort can help readers become better at ___.', ['Recognizing spelling patterns', 'Forgetting letters', 'Avoiding books', 'Ignoring sounds'], 0)]),
M('Ordinal Numbers: From Eleventh to Twentieth',
  'Grade 2 Math strand: ordinal numbers describe position or order, and beyond tenth they continue as eleventh, twelfth, thirteenth, all the way to twentieth.',
  [('What comes after tenth?', ['Eleventh', 'Twelfth', 'Ninth', 'Twentieth'], 0),
   ('What is the ordinal form of the number 15?', ['Fifteenth', 'Fiveteenth', 'Fifteen', 'Fiftieth'], 0),
   ('What is the ordinal form of the number 20?', ['Twentieth', 'Twenty', 'Twoth', 'Twentyth'], 0),
   ('Ordinal numbers describe ___.', ['Position or order', 'Only amounts', 'Only colours', 'Only shapes'], 0),
   ('If a runner finishes right after the twelfth place runner, what place do they finish in?', ['Thirteenth', 'Eleventh', 'Twelfth', 'Fourteenth'], 0)]),
Sc('Caves: Dark Underground Habitats',
   'Grade 2 Science strand: caves are dark underground spaces where little or no sunlight reaches, and the animals that live there, like bats, are often adapted to darkness.',
   [('What is a cave?', ['A dark underground space', 'A type of cloud', 'A kind of ocean', 'A tall mountain peak'], 0),
    ('How much sunlight usually reaches deep inside a cave?', ['Little or none', 'A great deal', 'The same as outside', 'More than outside'], 0),
    ('Which animal is commonly adapted to living in caves?', ['Bats', 'Polar bears', 'Camels', 'Penguins'], 0),
    ('Why might animals in caves rely less on eyesight?', ['Because there is very little light to see by', 'Because caves are extremely bright', 'Because eyesight is never useful', 'Because caves have no walls'], 0),
    ('A cave is best described as a ___ habitat.', ['Dark, underground', 'Bright, underwater', 'Hot, sandy', 'Icy, open'], 0)]),
SS('Canadian Thanksgiving: A Harvest Celebration',
   'Grade 2 Social Studies strand: Canadian Thanksgiving is a holiday celebrated in October where families gather to give thanks and share a meal celebrating the harvest.',
   [('What does Canadian Thanksgiving celebrate?', ['The harvest and giving thanks', 'A hockey championship', 'A type of weather', 'A new school year'], 0),
    ('In which month is Canadian Thanksgiving celebrated?', ['October', 'December', 'July', 'March'], 0),
    ('What do families often do together on Thanksgiving?', ['Gather and share a meal', 'Avoid seeing each other', 'Go to school', 'Work all day with no breaks'], 0),
    ('The word harvest refers to ___.', ['Gathering crops that have grown', 'A type of building', 'A kind of vehicle', 'A musical instrument'], 0),
    ('Why might people give thanks at a harvest celebration?', ['To appreciate the food and resources they have', 'Giving thanks has no purpose', 'Harvest celebrations never involve thanks', 'Only farmers may give thanks'], 0)]),
]),
day(167, [
L('Tongue Twisters: Playing With Repeated Sounds',
  'Grade 2 Language strand: a tongue twister is a phrase that repeats similar sounds again and again, making it fun and tricky to say quickly and clearly.',
  [('What is a tongue twister?', ['A phrase that repeats similar sounds and is tricky to say', 'A type of punctuation', 'A silent letter', 'A math equation'], 0),
   ('Why are tongue twisters tricky to say quickly?', ['They repeat very similar sounds close together', 'They have no sounds at all', 'They are written backwards', 'They contain no words'], 0),
   ('Which of these is an example of a tongue twister?', ['She sells seashells by the seashore', 'The sky is blue today', 'I like apples', 'We went to the park'], 0),
   ('Tongue twisters are closely related to which sound device?', ['Alliteration', 'A silent vowel', 'A capital letter', 'A question mark'], 0),
   ('Why might people enjoy practising tongue twisters?', ['They are a fun challenge for speaking clearly', 'They make speaking impossible forever', 'They have no purpose at all', 'They remove all sounds from words'], 0)]),
M('Geometry: Slides, Flips, and Turns',
  'Grade 2 Math strand: a slide moves a shape without turning it, a flip creates a mirror image of a shape, and a turn rotates a shape around a point.',
  [('What happens to a shape during a slide?', ['It moves without turning', 'It becomes a mirror image', 'It rotates around a point', 'It disappears'], 0),
   ('What happens to a shape during a flip?', ['It becomes a mirror image', 'It only moves sideways', 'It grows larger', 'It shrinks smaller'], 0),
   ('What happens to a shape during a turn?', ['It rotates around a point', 'It becomes a mirror image', 'It changes colour', 'It disappears completely'], 0),
   ('Which of these describes a slide?', ['Moving a shape straight across without rotating it', 'Flipping a shape upside down', 'Spinning a shape in a circle', 'Erasing a shape'], 0),
   ('Slides, flips, and turns are all examples of ___.', ['Ways to move a shape', 'Types of numbers', 'Units of measurement', 'Kinds of graphs'], 0)]),
Sc('Glaciers: Slow-Moving Rivers of Ice',
   'Grade 2 Science strand: a glacier is a huge, slow-moving mass of ice that forms over many years from packed snow, and glaciers can carve valleys as they move.',
   [('What is a glacier?', ['A huge, slow-moving mass of ice', 'A type of cloud', 'A fast-flowing river of water', 'A warm ocean current'], 0),
    ('How does a glacier form?', ['From packed snow building up over many years', 'From melted rock', 'From ocean waves', 'From volcanic ash'], 0),
    ('What can a moving glacier do to the land beneath it?', ['Carve out valleys', 'Turn the land into sand instantly', 'Create no change at all', 'Make the land warmer'], 0),
    ('Do glaciers move quickly or slowly?', ['Very slowly', 'Very quickly, like a race car', 'Instantly', 'They never move'], 0),
    ('Glaciers are made mostly of ___.', ['Packed ice and snow', 'Liquid water only', 'Sand', 'Rock'], 0)]),
SS('Public Transit: Getting Around Our Communities',
   'Grade 2 Social Studies strand: public transit includes buses, subways, and trains that carry many people at once, helping communities move around without everyone needing a car.',
   [('What is public transit?', ['Buses, subways, and trains that carry many people', 'A type of private car', 'A kind of bicycle only', 'A walking path'], 0),
    ('Why is public transit helpful for communities?', ['It helps people move around without needing a car', 'It has no benefit at all', 'It only helps one person at a time', 'It replaces the need for roads'], 0),
    ('Which of these is an example of public transit?', ['A city bus', 'A single family car', 'A private airplane', 'A personal bicycle'], 0),
    ('How many people can public transit typically carry at once?', ['Many people', 'Only one person', 'No people at all', 'Only two people'], 0),
    ('Using public transit instead of individual cars can help reduce ___.', ['Traffic and pollution', 'The number of roads needed instantly', 'The size of a city', 'The number of communities'], 0)]),
]),
day(168, [
L('Comparing Different Versions of the Same Story',
  'Grade 2 Language strand: many well-known stories, like fairy tales, have different versions told by different authors or cultures, and comparing them shows how details, characters, or endings can change.',
  [('What can be different between two versions of the same story?', ['Details, characters, or the ending', 'Nothing, versions are always identical', 'The story stops existing', 'Only the page numbers'], 0),
   ('Why might different cultures tell their own version of a familiar story?', ['To reflect their own traditions and ideas', 'Stories can never change', 'Only one version is ever allowed', 'Cultures never share stories'], 0),
   ('When comparing two story versions, what might a reader look for?', ['Similarities and differences in plot or characters', 'Only the cover colour', 'Only the number of pages', 'Only the price of the book'], 0),
   ('Comparing story versions helps readers understand ___.', ['How the same idea can be told in different ways', 'That only one story can ever exist', 'That stories never have characters', 'That comparing is not useful'], 0),
   ('Which is an example of comparing story versions?', ['Noticing how two tellings of the same fairy tale have different endings', 'Reading a single book once', 'Ignoring every story detail', 'Refusing to read more than one book'], 0)]),
M('Money: Canadian Coin Values — Nickel, Dime, Quarter, Loonie, and Toonie',
  'Grade 2 Math strand: Canadian coins have different names and values, including the nickel worth five cents, the dime worth ten cents, the quarter worth twenty-five cents, the loonie worth one dollar, and the toonie worth two dollars.',
  [('How much is a nickel worth?', ['Five cents', 'Ten cents', 'Twenty-five cents', 'One dollar'], 0),
   ('How much is a dime worth?', ['Ten cents', 'Five cents', 'One dollar', 'Two dollars'], 0),
   ('How much is a quarter worth?', ['Twenty-five cents', 'Ten cents', 'One dollar', 'Fifty cents'], 0),
   ('What is the value of a loonie?', ['One dollar', 'Two dollars', 'Ten cents', 'Twenty-five cents'], 0),
   ('What is the value of a toonie?', ['Two dollars', 'One dollar', 'Twenty-five cents', 'Five cents'], 0)]),
Sc('Earthquakes: When the Earth Shakes',
   'Grade 2 Science strand: an earthquake happens when the ground suddenly shakes because of movement deep within the Earths crust, sometimes caused by shifting rock along a fault.',
   [('What is an earthquake?', ['A sudden shaking of the ground', 'A type of storm', 'A kind of ocean wave', 'A change in air temperature'], 0),
    ('What can cause an earthquake?', ['Movement of rock along a fault deep in the Earth', 'Wind blowing over the ocean', 'Rain falling on a mountain', 'Trees growing tall'], 0),
    ('Where does the movement that causes an earthquake usually happen?', ['Deep within the Earths crust', 'High in the sky', 'In the ocean waves', 'On the surface of the moon'], 0),
    ('Why do scientists study earthquakes?', ['To understand them and help keep people safe', 'Earthquakes are not worth studying', 'To make earthquakes happen more often', 'To stop the Earth from having a crust'], 0),
    ('An earthquake is best described as ___.', ['A sudden shaking of the ground', 'A gentle breeze', 'A slow-moving cloud', 'A calm, still day'], 0)]),
SS('Farmers Markets: Buying Food Grown Close to Home',
   'Grade 2 Social Studies strand: a farmers market is a place where local farmers sell fruits, vegetables, and other food directly to shoppers, often close to where the food was grown.',
   [('What is a farmers market?', ['A place where local farmers sell food directly to shoppers', 'A type of grocery store chain', 'A school event', 'A kind of factory'], 0),
    ('What might you buy at a farmers market?', ['Fruits and vegetables', 'Only clothing', 'Only furniture', 'Only electronics'], 0),
    ('Why might people choose to shop at a farmers market?', ['To buy food grown close to home', 'Farmers markets never sell food', 'It is always more expensive than any option', 'Farmers markets only sell toys'], 0),
    ('Who typically sells food at a farmers market?', ['Local farmers', 'Only large international companies', 'Only online stores', 'Only restaurants'], 0),
    ('Buying food from a farmers market can support ___.', ['Local farmers and the community', 'No one at all', 'Only large corporations', 'Farmers in other countries only'], 0)]),
]),
day(169, [
L('Environmental Print: Reading Signs and Logos Around Us',
  'Grade 2 Language strand: environmental print is the words and symbols we see in everyday life, like stop signs, store logos, and food labels, that we often recognize without sounding out every letter.',
  [('What is environmental print?', ['Words and symbols seen in everyday life', 'A type of punctuation', 'A silent letter', 'A kind of math problem'], 0),
   ('Which of these is an example of environmental print?', ['A stop sign', 'A blank page', 'A silent room', 'An empty box'], 0),
   ('Why can young readers often recognize environmental print quickly?', ['They see it often and remember its shape and colour', 'It is always written in tiny letters', 'It never repeats', 'It has no meaning'], 0),
   ('Environmental print can be found ___.', ['All around our daily surroundings', 'Only inside books', 'Only in outer space', 'Nowhere at all'], 0),
   ('Reading environmental print is a useful first step toward ___.', ['Becoming a confident reader', 'Forgetting the alphabet', 'Avoiding all print', 'Ignoring signs'], 0)]),
M('Number Sense: Writing Numbers in Word Form',
  'Grade 2 Math strand: numbers can be written using digits, like 342, or in word form, like three hundred forty-two, spelling out the value in words.',
  [('What is 342 written in word form?', ['Three hundred forty-two', 'Three forty two hundred', 'Three hundred and forty', 'Thirty-four two'], 0),
   ('What is 25 written in word form?', ['Twenty-five', 'Two hundred five', 'Twenty and five ones', 'Fifty-two'], 0),
   ('What is one hundred six written using digits?', ['106', '116', '160', '16'], 0),
   ('Writing numbers in word form means writing them ___.', ['Spelled out using words', 'Using only digits', 'Using only pictures', 'Using only symbols'], 0),
   ('What is 90 written in word form?', ['Ninety', 'Nine', 'Nineteen', 'Nine hundred'], 0)]),
Sc('Ants: Insect Colonies at Work',
   'Grade 2 Science strand: ants are insects that live and work together in large groups called colonies, sharing jobs like gathering food, building tunnels, and caring for young ants.',
   [('What is a group of ants living together called?', ['A colony', 'A herd', 'A flock', 'A pod'], 0),
    ('What kind of animal is an ant?', ['An insect', 'A mammal', 'A bird', 'A reptile'], 0),
    ('Which job might ants share in their colony?', ['Gathering food', 'Flying to another planet', 'Breathing underwater', 'Swimming in the ocean'], 0),
    ('Why do ants work together in a colony?', ['To share jobs and support the whole group', 'Ants never work together', 'To avoid finding food', 'To live completely alone'], 0),
    ('Ants build underground ___ as part of their colony.', ['Tunnels', 'Nests made of ice', 'Coral reefs', 'Bird nests'], 0)]),
SS('The CN Tower: A Famous Canadian Landmark',
   'Grade 2 Social Studies strand: the CN Tower is a very tall tower in Toronto, once the tallest freestanding structure in the world, known for its observation decks and views of the city.',
   [('In which city is the CN Tower located?', ['Toronto', 'Vancouver', 'Montreal', 'Ottawa'], 0),
    ('What was the CN Tower once known as?', ['The tallest freestanding structure in the world', 'The smallest tower in Canada', 'A type of bridge', 'A kind of park'], 0),
    ('What can visitors do at the CN Tower?', ['View the city from its observation decks', 'Go swimming in a pool at the top', 'Ski down the tower', 'Fish for salmon'], 0),
    ('The CN Tower is an example of a Canadian ___.', ['Landmark', 'River', 'Prairie', 'Ocean'], 0),
    ('Why might a tower like the CN Tower attract visitors?', ['Its height offers impressive views of the city', 'It is invisible from the ground', 'It has no notable features', 'It cannot be seen or visited'], 0)]),
]),
day(170, [
L('Language Review: Poetry Forms, Grammar, and New Writing Genres',
  'Grade 2 Language strand review: students revisit riddles, haiku, shape poems, possessive pronouns, news reports, word sorts, tongue twisters, comparing story versions, and environmental print.',
  [('What is a riddle?', ['A playful question with a clue-filled answer', 'A true news report', 'A math equation', 'A silent letter'], 0),
   ('How many lines does a haiku usually have?', ['3', '5', '10', '1'], 0),
   ('What makes a shape poem special?', ['The words are arranged to form the outline of the topic', 'It has no words at all', 'It must rhyme perfectly', 'It has exactly one line'], 0),
   ('What does a possessive pronoun show?', ['Who something belongs to', 'A question', 'An action', 'A feeling only'], 0),
   ('What is the main purpose of a news report?', ['To share real events using facts', 'To tell a made-up fairy tale', 'To give only opinions', 'To write a poem'], 0)]),
M('Math Review: Fractions, Data, Time, and Number Sense',
  'Grade 2 Math strand review: students revisit equal parts of a whole, unit fractions, pictographs with a key, calendars, comparing durations, ordinal numbers past ten, slides and flips and turns, Canadian coin values, and writing numbers in word form.',
  [('For a fraction to be shown correctly, a shape must be divided into ___.', ['Equal parts', 'Random sized pieces', 'Only two pieces', 'Different sized pieces'], 0),
   ('What is a unit fraction?', ['A fraction with a numerator of one', 'A fraction with a denominator of one', 'A whole number', 'A fraction with no parts'], 0),
   ('What does a key on a pictograph tell the reader?', ['How many items each picture represents', 'The title of the graph only', 'The colour of the picture', 'Nothing important'], 0),
   ('How many days are in one week?', ['7', '5', '10', '30'], 0),
   ('What happens to a shape during a slide?', ['It moves without turning', 'It becomes a mirror image', 'It rotates around a point', 'It disappears'], 0)]),
Sc('Science Review: Animals, Habitats, and Earth Events',
   'Grade 2 Science strand review: students revisit earthworms, octopuses, turtles, dinosaurs and fossils, mountain habitats, caves, glaciers, earthquakes, and ants.',
   [('Where do earthworms usually live?', ['Underground in soil', 'In the ocean', 'In trees', 'In the sky'], 0),
    ('How many arms does an octopus have?', ['Eight', 'Four', 'Six', 'Two'], 0),
    ('What protects a turtles soft body?', ['A hard shell', 'Feathers', 'Fur', 'Scales alone with no shell'], 0),
    ('How do scientists learn about dinosaurs today?', ['By studying fossils', 'By watching them in person', 'By reading old newspapers', 'By guessing with no evidence'], 0),
    ('What is an earthquake?', ['A sudden shaking of the ground', 'A type of storm', 'A kind of ocean wave', 'A change in air temperature'], 0)]),
SS('Social Studies Review: Government, Culture, and Canadian Places',
   'Grade 2 Social Studies strand review: students revisit the Supreme Court of Canada, Canadas national motto, the poppy, lacrosse, the Great Lakes, Canadian Thanksgiving, public transit, farmers markets, and the CN Tower.',
   [('What is the Supreme Court of Canada?', ['The highest court in the country', 'A local library', 'A type of school', 'A city council'], 0),
    ('What does Canadas national motto mean in English?', ['From sea to sea', 'From coast to mountain', 'From north to south only', 'From city to city'], 0),
    ('What does the poppy symbolize?', ['Remembrance of those who served and died in wars', 'A type of currency', 'A community sport', 'A kind of weather'], 0),
    ('What is lacrosse recognized as in Canada?', ['The national summer sport', 'The national winter sport', 'A type of food', 'A type of currency'], 0),
    ('In which city is the CN Tower located?', ['Toronto', 'Vancouver', 'Montreal', 'Ottawa'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_161_170)
    append_to(2, g2_161_170)
