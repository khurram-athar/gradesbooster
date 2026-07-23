#!/usr/bin/env python3
"""Grade 2, Days 101-110 -- EIGHTH batch, extending Grade 2 through Day 110.
Self-contained script modeled on gen_grade2_days91_100.py, but uses the
sub()/day()/append_to() helpers imported directly from gen_curriculum.py
(no local worksheet field, no local append function):

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- no worksheet field

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-100 topics (see data/grade2.ts / data/grade2.json). No embedded ASCII
double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz text -- contractions and possessives are avoided
entirely (or rewritten without the apostrophe) to keep the generated .ts
string literals valid.
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


def _rebalance_answer_positions(days, seed=20260921):
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


# ─── DAY 101 ────────────────────────────────────────────────────────────────
d101_lang = mk('Language', 'Subjects and Predicates: The Two Parts of a Sentence',
  'Ontario Grade 2 Language strand: students learn that every complete sentence has two main parts, a subject that names who or what the sentence is about, and a predicate that tells what the subject does or is.',
  [('What is the subject of a sentence?', ['The part that names who or what the sentence is about', 'The part that tells what the subject does', 'A punctuation mark at the end', 'A describing word only'], 0),
   ('What is the predicate of a sentence?', ['The part that tells what the subject does or is', 'The part that names who the sentence is about', 'The first word of the sentence', 'A question mark'], 0),
   ('In the sentence The dog ran fast, what is the subject?', ['The dog', 'ran fast', 'fast', 'ran'], 0),
   ('In the sentence The dog ran fast, what is the predicate?', ['ran fast', 'The dog', 'dog', 'fast only'], 0),
   ('Why does a sentence need both a subject and a predicate?', ['To be a complete thought', 'To be a longer sentence', 'To use more punctuation', 'To sound louder'], 0)])

d101_math = mk('Math', 'Multiplication Facts: 0s, 1s, and 10s',
  'Ontario Grade 2 Number strand: students practise and memorize multiplication facts for the 0, 1, and 10 times tables, learning that any number multiplied by 0 equals 0, any number multiplied by 1 stays the same, and multiplying by 10 adds a zero.',
  [('What is 5 times 0?', ['0', '5', '10', '50'], 0),
   ('What is 7 times 1?', ['7', '0', '8', '17'], 0),
   ('What is 6 times 10?', ['60', '16', '6', '610'], 0),
   ('What is 9 times 0?', ['0', '9', '90', '19'], 0),
   ('What happens when you multiply any number by 1?', ['The number stays the same', 'The number becomes 0', 'The number doubles', 'The number becomes 10'], 0)])

d101_sci = mk('Science', 'Weathering: How Rocks Slowly Break Down',
  'Ontario Grade 2 Earth and Space Systems strand: students learn that weathering is the slow breaking down of rocks by wind, water, ice, and changes in temperature over a long period of time.',
  [('What is weathering?', ['The slow breaking down of rocks by wind, water, and ice', 'The movement of soil from one place to another', 'A type of severe storm', 'The melting of snow in spring'], 0),
   ('Which of these can cause weathering?', ['Wind and water', 'A calm, sunny day', 'A quiet forest', 'A clear night sky'], 0),
   ('Does weathering happen quickly or slowly?', ['Slowly, over a long time', 'Instantly, in one second', 'Only during an earthquake', 'Only underwater'], 0),
   ('How can freezing and thawing water crack a rock?', ['Water seeps into cracks, freezes, expands, and breaks the rock apart', 'Water always makes rocks stronger', 'Freezing has no effect on rocks', 'Rocks never contain any cracks'], 0),
   ('Weathering is best described as a process that ___.', ['Breaks rocks into smaller pieces over time', 'Builds new mountains instantly', 'Turns rocks into water', 'Has no effect on the Earth crust'], 0)])

d101_ss = mk('SocialStudies', 'Terry Fox: A Canadian Hero and His Marathon of Hope',
  'Ontario Grade 2 Social Studies Heritage and Identity strand: students learn about Terry Fox, a young Canadian who ran across much of Canada to raise money for cancer research in a journey called the Marathon of Hope.',
  [('What did Terry Fox call his run across Canada?', ['The Marathon of Hope', 'The Race for Canada', 'The Great Canadian Walk', 'The Freedom Run'], 0),
   ('Why did Terry Fox run across Canada?', ['To raise money for cancer research', 'To win a race', 'To visit every province for fun', 'To become famous'], 0),
   ('What challenge did Terry Fox face during his run?', ['He ran with one leg after losing the other to cancer', 'He could not swim', 'He had never travelled before', 'He ran only around his own house'], 0),
   ('Communities across Canada still honour Terry Fox by ___.', ['Holding an annual run to raise money for cancer research', 'Ignoring his story completely', 'Only remembering him in one city', 'Forgetting his journey each year'], 0),
   ('Why is Terry Fox considered a Canadian hero?', ['He showed courage and inspired others to help a cause bigger than himself', 'He was the fastest runner in the world', 'He never faced any challenges', 'He only ran for his own benefit'], 0)])

# ─── DAY 102 ────────────────────────────────────────────────────────────────
d102_lang = mk('Language', 'Articles: Using A, An, and The Correctly',
  'Ontario Grade 2 Language strand: students learn that the articles a and an come before a noun to mean any one example, using a before a consonant sound and an before a vowel sound, while the comes before a noun to mean one specific thing.',
  [('Which article is used before a word that starts with a vowel sound, like apple?', ['an', 'a', 'the', 'no article needed'], 0),
   ('Which article is used before a word that starts with a consonant sound, like dog?', ['a', 'an', 'the', 'no article needed'], 0),
   ('Which sentence uses the correct article?', ['She ate an apple.', 'She ate a apple.', 'She ate the apple an.', 'She ate apple a.'], 0),
   ('Which sentence uses the correct article?', ['He read a book.', 'He read an book.', 'He read book a.', 'He read the a book.'], 0),
   ('When do we use the word the before a noun?', ['When we mean one specific thing', 'When we mean any example at all', 'Only before vowel sounds', 'Only at the start of a sentence'], 0)])

d102_math = mk('Math', 'Composing and Decomposing 2D Shapes',
  'Ontario Grade 2 Geometry strand: students learn to compose new shapes by combining smaller two-dimensional shapes, and decompose a larger shape into smaller shapes, such as building a square from two triangles.',
  [('What does it mean to compose a shape?', ['To combine smaller shapes to make a new shape', 'To draw a shape with no sides', 'To erase a shape completely', 'To colour a shape a single colour'], 0),
   ('What does it mean to decompose a shape?', ['To break a larger shape into smaller shapes', 'To combine shapes into a bigger one', 'To make a shape disappear', 'To measure the perimeter of a shape'], 0),
   ('Two triangles put together can compose which shape?', ['A square or rectangle', 'A circle', 'A single point', 'A straight line only'], 0),
   ('If you cut a rectangle in half diagonally, what shapes do you get?', ['Two triangles', 'Two circles', 'Two squares only', 'Two hexagons'], 0),
   ('Composing and decomposing shapes helps students understand ___.', ['How shapes relate to and can form other shapes', 'That shapes never change', 'That only one shape exists', 'That shapes cannot be combined'], 0)])

d102_sci = mk('Science', 'Animal Movement: Fins, Wings, and Legs',
  'Ontario Grade 2 Life Systems strand: students learn that animals have different body structures, such as fins, wings, and legs, that help them move in the specific environment where they live.',
  [('What body part helps a fish move through water?', ['Fins', 'Wings', 'Legs', 'Feathers'], 0),
   ('What body part helps a bird fly through the air?', ['Wings', 'Fins', 'Gills', 'Roots'], 0),
   ('What body part helps most mammals walk and run on land?', ['Legs', 'Fins', 'Wings', 'Scales'], 0),
   ('Why do different animals have different movement structures?', ['To help them move well in the place they live', 'All animals move in the exact same way', 'Movement structures have no real purpose', 'Only birds are able to move at all'], 0),
   ('A frog has strong back legs mainly to help it ___.', ['Jump long distances', 'Fly through the air', 'Swim using fins only', 'Stay still forever'], 0)])

d102_ss = mk('SocialStudies', 'What Is a Democracy? Citizens Have a Voice in Decisions',
  'Ontario Grade 2 Social Studies strand: students learn that in a democracy, citizens have a say in decisions and choose their leaders through voting, and that Canada is a democratic country.',
  [('What is a democracy?', ['A system where citizens have a voice and vote for their leaders', 'A system with no leaders at all', 'A place where only one person makes every decision', 'A system where citizens cannot vote'], 0),
   ('Is Canada a democratic country?', ['Yes, Canada is a democracy', 'No, Canada has never been a democracy', 'Only some Canadian cities are democracies', 'Canada stopped being a democracy long ago'], 0),
   ('How do citizens in a democracy have a say in decisions?', ['By voting in elections', 'By never taking part in anything', 'By letting only one family decide', 'By ignoring all elections'], 0),
   ('Why is voting an important part of a democracy?', ['It lets citizens choose who represents them', 'Voting has no effect on decisions', 'Only leaders are allowed to vote', 'Voting is not connected to democracy'], 0),
   ('In a democracy, decisions are usually made by ___.', ['Listening to the voice of many citizens', 'One single unelected ruler', 'Ignoring what citizens want', 'A small group with no elections'], 0)])

# ─── DAY 103 ────────────────────────────────────────────────────────────────
d103_lang = mk('Language', 'Verb Tenses: Talking About Past, Present, and Future',
  'Ontario Grade 2 Language strand: students learn that verbs change form to show when an action happens, using past tense for something already done, present tense for something happening now, and future tense for something that will happen.',
  [('Which sentence is in the past tense?', ['She walked to school.', 'She walks to school.', 'She will walk to school.', 'She is walking to school.'], 0),
   ('Which sentence is in the present tense?', ['He plays soccer every day.', 'He played soccer yesterday.', 'He will play soccer tomorrow.', 'He had played soccer.'], 0),
   ('Which sentence is in the future tense?', ['They will visit the zoo tomorrow.', 'They visited the zoo yesterday.', 'They visit the zoo often.', 'They were visiting the zoo.'], 0),
   ('Which word signals that a sentence is talking about the future?', ['will', 'yesterday', 'now', 'already'], 0),
   ('Changing a verb tense helps a reader understand ___.', ['When an action happens', 'What colour something is', 'How many people are in a story', 'Where a story takes place'], 0)])

d103_math = mk('Math', 'Number Patterns on a Hundred Chart',
  'Ontario Grade 2 Patterning strand: students explore a hundred chart to find and describe number patterns, such as columns increasing by 10 going down and rows increasing by 1 going across.',
  [('On a hundred chart, what happens to a number as you move down one row?', ['It increases by 10', 'It increases by 1', 'It decreases by 10', 'It stays the same'], 0),
   ('On a hundred chart, what happens to a number as you move one space to the right?', ['It increases by 1', 'It increases by 10', 'It decreases by 1', 'It stays the same'], 0),
   ('On a hundred chart, if you are on 24 and move down one row, what number do you land on?', ['34', '25', '23', '14'], 0),
   ('On a hundred chart, if you are on 47 and move one space to the right, what number do you land on?', ['48', '57', '46', '37'], 0),
   ('A hundred chart helps students see number patterns because ___.', ['Numbers are arranged in a clear, organized grid', 'Numbers are placed in random order', 'It only shows odd numbers', 'It only shows even numbers'], 0)])

d103_sci = mk('Science', 'Food Webs: Connecting Many Food Chains',
  'Ontario Grade 2 Life Systems strand: students learn that a food web shows how many food chains connect together, because most animals eat more than one kind of food and are eaten by more than one predator.',
  [('What is a food web?', ['Many connected food chains showing how animals eat different things', 'A single line showing one animal eating one plant', 'A spider web found in a garden', 'A chart of animal habitats only'], 0),
   ('Why do scientists use a food web instead of just one food chain?', ['Most animals eat more than one kind of food', 'Every animal eats the exact same food', 'Food chains never connect to each other', 'A food web only shows plants'], 0),
   ('In a food web, an animal that eats both plants and other animals is called a ___.', ['Omnivore', 'Producer only', 'Decomposer only', 'Non-living thing'], 0),
   ('What might happen to a food web if one type of animal disappeared?', ['It could affect the other animals connected to it', 'Nothing would change at all', 'Every other animal would disappear instantly', 'Food webs cannot be affected by changes'], 0),
   ('A food web is best described as a way to show ___.', ['How living things in an ecosystem depend on each other for food', 'That animals never depend on other living things', 'A single unrelated fact about one animal', 'That plants have no role in an ecosystem'], 0)])

d103_ss = mk('SocialStudies', 'Provincial and Territorial Capital Cities',
  'Ontario Grade 2 Social Studies strand: students learn that each Canadian province and territory has its own capital city, such as Toronto for Ontario and Ottawa as the capital of the whole country.',
  [('What is the capital city of Ontario?', ['Toronto', 'Ottawa', 'Vancouver', 'Montreal'], 0),
   ('What is the capital city of Canada?', ['Ottawa', 'Toronto', 'Calgary', 'Winnipeg'], 0),
   ('What do we call the main city where the government of a province or country is based?', ['A capital city', 'A border town', 'A suburb', 'A rural area'], 0),
   ('Why does each province and territory have its own capital city?', ['It is where the provincial or territorial government meets and works', 'Capital cities have no real purpose', 'Every province shares the exact same capital', 'Capitals are chosen at random every year'], 0),
   ('Is Ottawa located in the province of Ontario?', ['Yes, Ottawa is located in Ontario', 'No, Ottawa is located in Quebec', 'Ottawa is not located in any province', 'Ottawa is a separate country'], 0)])

# ─── DAY 104 ────────────────────────────────────────────────────────────────
d104_lang = mk('Language', 'Using Illustrations to Understand a Story',
  'Ontario Grade 2 Reading strand: students learn to use illustrations and pictures alongside the words in a text to build and confirm their understanding of characters, setting, and events.',
  [('Why might a reader look at the illustrations in a book?', ['To help understand the story better', 'Illustrations never help understanding', 'To ignore the words completely', 'Pictures have no connection to the story'], 0),
   ('If the words in a story do not explain what a character looks like, where might a reader find clues?', ['The illustrations', 'The back cover only', 'The table of contents', 'The title page only'], 0),
   ('Illustrations can help a reader understand ___.', ['The setting, characters, and mood of a story', 'Only the title of the book', 'Only the price of the book', 'Nothing about the story at all'], 0),
   ('If a picture shows dark clouds and rain, what might that tell a reader about the setting?', ['The weather is stormy', 'The weather is sunny and warm', 'The story takes place indoors only', 'The picture has no meaning'], 0),
   ('Using illustrations along with the text is a strategy that helps readers ___.', ['Understand and enjoy a story more fully', 'Ignore important story details', 'Skip reading the words entirely', 'Avoid understanding the story'], 0)])

d104_math = mk('Math', 'Estimating Length Before Measuring',
  'Ontario Grade 2 Measurement strand: students learn to make a reasonable estimate of an object length before measuring it with a ruler or measuring tape, then compare the estimate to the actual measurement.',
  [('What does it mean to estimate a length?', ['To make a reasonable guess before measuring', 'To measure something perfectly the first time', 'To ignore the size of an object', 'To draw a picture of an object'], 0),
   ('Why is it useful to estimate before measuring?', ['It helps you check if your measurement makes sense', 'Estimating always gives the exact answer', 'Estimating replaces the need to measure', 'Estimating has no purpose in math'], 0),
   ('Which tool would you use to check an estimate of length?', ['A ruler or measuring tape', 'A clock', 'A thermometer', 'A scale for mass'], 0),
   ('If you estimate a pencil is about 15 centimetres long, what should you do next?', ['Measure it with a ruler to check your estimate', 'Never measure it at all', 'Assume your estimate is always exact', 'Throw away the pencil'], 0),
   ('A good estimate of length should be ___.', ['Reasonably close to the actual measurement', 'Always exactly correct', 'Always much too large', 'Always much too small'], 0)])

d104_sci = mk('Science', 'Tundra Habitats: Life in the Cold',
  'Ontario Grade 2 Life Systems strand: students learn that the tundra is a cold habitat with very few trees, where specially adapted plants and animals, such as arctic foxes and caribou, survive harsh winters.',
  [('What is a tundra?', ['A cold habitat with very few trees', 'A hot, wet rainforest', 'A warm desert habitat', 'A deep ocean habitat'], 0),
   ('Which animal is adapted to live in the tundra?', ['Arctic fox', 'Elephant', 'Monkey', 'Parrot'], 0),
   ('Why do few trees grow in the tundra?', ['The ground is frozen and the climate is very cold', 'The tundra is always too hot for trees', 'Tundra soil has too much sunlight', 'Trees are not affected by climate'], 0),
   ('How might a thick white coat help an animal survive in the tundra?', ['It keeps the animal warm and helps it blend into the snow', 'It makes the animal colder', 'It has no useful purpose', 'It helps the animal swim faster'], 0),
   ('The tundra is best described as a habitat where living things must adapt to ___.', ['Very cold temperatures and short growing seasons', 'Extremely hot and humid weather', 'Deep ocean water pressure', 'Constant heavy rainfall'], 0)])

d104_ss = mk('SocialStudies', 'First Nations, Inuit, and Metis: Three Distinct Indigenous Peoples',
  'Ontario Grade 2 Social Studies Heritage and Identity strand: students learn that Indigenous peoples in Canada include three distinct groups, First Nations, Inuit, and Metis, each with its own history, languages, and traditions.',
  [('What are the three distinct groups of Indigenous peoples in Canada?', ['First Nations, Inuit, and Metis', 'Settlers, explorers, and traders', 'Farmers, teachers, and mayors', 'Provinces, cities, and towns'], 0),
   ('Do First Nations, Inuit, and Metis peoples each have their own history and traditions?', ['Yes, each group has its own history and traditions', 'No, all three groups are exactly the same', 'Only First Nations have traditions', 'Only Inuit have traditions'], 0),
   ('Which Indigenous group has traditionally lived in the Arctic regions of Canada?', ['Inuit', 'Only First Nations', 'Only Metis', 'None of these groups'], 0),
   ('Why is it important to learn that Indigenous peoples are not all the same group?', ['Each group has its own distinct culture and identity', 'All Indigenous peoples are identical', 'Learning about differences is not useful', 'Only one Indigenous group exists in Canada'], 0),
   ('The word Metis describes people who have ___.', ['Mixed Indigenous and European ancestry and their own distinct culture', 'No connection to Indigenous history at all', 'Only European ancestry', 'Only recently arrived in Canada'], 0)])

# ─── DAY 105 ────────────────────────────────────────────────────────────────
d105_lang = mk('Language', 'Compare and Contrast: How Two Things Are Alike and Different',
  'Ontario Grade 2 Reading strand: students learn to compare and contrast two texts, characters, or ideas by describing how they are alike and how they are different.',
  [('What does it mean to compare two things?', ['To describe how they are alike', 'To describe how they are different only', 'To ignore both things', 'To draw a picture of them'], 0),
   ('What does it mean to contrast two things?', ['To describe how they are different', 'To describe how they are exactly the same', 'To combine them into one thing', 'To measure their size'], 0),
   ('Which of these is an example of comparing two story characters?', ['Both characters are brave and kind', 'One character is a girl and one is a boy', 'One story is short and one is long', 'One book has pictures and one does not'], 0),
   ('Which of these is an example of contrasting two story characters?', ['One character is shy while the other is outgoing', 'Both characters like to read', 'Both characters live in the same town', 'Both characters have a pet dog'], 0),
   ('Comparing and contrasting helps readers ___.', ['Understand how ideas or characters relate to each other', 'Ignore important details in a text', 'Avoid thinking about a story', 'Read only one book at a time'], 0)])

d105_math = mk('Math', 'Interpreting Bar Graphs with a Scale of More Than One',
  'Ontario Grade 2 Data strand: students learn to read a bar graph where each square or unit on the scale represents more than one item, such as a scale where each square stands for two or five objects.',
  [('On a bar graph where each square represents 2 items, how many items does a bar of 3 squares show?', ['6', '3', '2', '5'], 0),
   ('On a bar graph where each square represents 5 items, how many items does a bar of 4 squares show?', ['20', '9', '15', '25'], 0),
   ('Why might a bar graph use a scale where each square represents more than one item?', ['To fit larger amounts of data on the graph clearly', 'To make the graph impossible to read', 'Scales never represent more than one item', 'To make the data smaller than it really is'], 0),
   ('If a bar graph scale shows each square equals 10, and a bar has 5 squares, what total does the bar represent?', ['50', '15', '5', '10'], 0),
   ('Before reading the bars on a graph, what should you check first?', ['The scale, to see what each square represents', 'The colour of the bars only', 'The title of the classroom', 'The time of day'], 0)])

d105_sci = mk('Science', 'The Skin: Protecting Our Bodies',
  'Ontario Grade 2 Life Systems strand: students learn that the skin is the outer covering of our body that protects us from germs and injury, helps control body temperature, and lets us feel touch.',
  [('What is one important job of the skin?', ['Protecting the body from germs and injury', 'Pumping blood through the body', 'Breaking down food for energy', 'Sending messages to the brain only'], 0),
   ('How does the skin help us sense the world around us?', ['It lets us feel touch, such as heat, cold, and pressure', 'It lets us see colours', 'It lets us hear sounds', 'It lets us taste flavours'], 0),
   ('How does the skin help control body temperature?', ['By sweating to cool us down when we are hot', 'By making us hungry', 'By helping us digest food', 'By helping us breathe air'], 0),
   ('Why is it important to keep a cut on the skin clean?', ['To help prevent germs from entering the body', 'Cuts on skin are never a concern', 'Cleaning a cut has no purpose', 'Germs cannot enter through skin'], 0),
   ('The skin is best described as the body organ that ___.', ['Covers and protects the body', 'Pumps blood to every organ', 'Digests the food we eat', 'Only controls how we move'], 0)])

d105_ss = mk('SocialStudies', 'National Emblems of Canada: The Coat of Arms and Other Symbols',
  'Ontario Grade 2 Social Studies strand: students learn that Canada has official national emblems, including the Coat of Arms, that represent the history and identity of the country beyond the more familiar flag and anthem.',
  [('What is the Coat of Arms of Canada?', ['An official emblem that represents the history and identity of Canada', 'A type of Canadian clothing', 'A famous Canadian mountain', 'A Canadian sports team logo'], 0),
   ('Which of these is an example of a Canadian national emblem?', ['The Coat of Arms', 'A students favourite toy', 'A single citys local logo', 'A private company logo'], 0),
   ('Why do countries have official emblems like a Coat of Arms?', ['To represent the history and values of the country', 'Emblems have no real meaning', 'Only provinces are allowed emblems', 'Countries are not allowed emblems'], 0),
   ('National emblems are different from a national flag because they ___.', ['Can include more detailed symbols and images', 'Are always exactly the same as a flag', 'Have no connection to a country at all', 'Cannot be used by a country'], 0),
   ('Learning about national emblems helps students understand ___.', ['Symbols that represent Canadian history and identity', 'That Canada has no symbols at all', 'That symbols are unimportant', 'That only flags represent countries'], 0)])

# ─── DAY 106 ────────────────────────────────────────────────────────────────
d106_lang = mk('Language', 'Following Multi-Step Written Directions',
  'Ontario Grade 2 Reading and Writing strands: students learn to read and follow written directions that have more than one step, completing each step in the correct order to finish a task successfully.',
  [('What is a multi-step direction?', ['A direction with more than one step to follow', 'A direction with only one step', 'A direction with no steps at all', 'A direction that never needs to be followed'], 0),
   ('Why is it important to follow the steps of a direction in order?', ['Completing steps out of order can lead to mistakes', 'Order never matters when following directions', 'Steps should always be skipped', 'Directions do not need to be read carefully'], 0),
   ('If a direction says first colour the circle, then cut it out, what should you do first?', ['Colour the circle', 'Cut it out', 'Skip both steps', 'Do both steps at the same time'], 0),
   ('What is a good strategy before starting a multi-step task?', ['Read all the directions carefully before beginning', 'Start immediately without reading anything', 'Ignore the directions completely', 'Only read the very last step'], 0),
   ('Following multi-step directions carefully helps you ___.', ['Complete a task correctly and in the right order', 'Finish a task incorrectly', 'Skip important steps', 'Avoid understanding the task'], 0)])

d106_math = mk('Math', 'Ordering Numbers to 1000',
  'Ontario Grade 2 Number strand: students learn to order a set of three-digit numbers from least to greatest or greatest to least by comparing the hundreds, tens, and ones digits.',
  [('Which set of numbers is ordered from least to greatest?', ['214, 356, 489', '489, 356, 214', '356, 214, 489', '214, 489, 356'], 0),
   ('Which number is the greatest: 342, 423, or 234?', ['423', '342', '234', 'They are all equal'], 0),
   ('Which number is the least: 567, 675, or 756?', ['567', '675', '756', 'They are all equal'], 0),
   ('When ordering three-digit numbers, which digit should you compare first?', ['The hundreds digit', 'The ones digit', 'The tens digit', 'The last letter'], 0),
   ('Which set of numbers is ordered from greatest to least?', ['812, 623, 415', '415, 623, 812', '623, 415, 812', '812, 415, 623'], 0)])

d106_sci = mk('Science', 'Camouflage vs Mimicry: Two Ways Animals Stay Safe',
  'Ontario Grade 2 Life Systems strand: students learn that camouflage lets an animal blend into its surroundings to hide, while mimicry lets a harmless animal look like a dangerous one to scare away predators.',
  [('What is camouflage?', ['When an animal blends into its surroundings to hide', 'When an animal looks like a different, dangerous animal', 'When an animal changes its habitat', 'When an animal grows larger'], 0),
   ('What is mimicry?', ['When a harmless animal looks like a dangerous one to stay safe', 'When an animal blends perfectly into a rock', 'When an animal grows a new colour every day', 'When an animal hides underground forever'], 0),
   ('A stick insect that looks like a twig is an example of ___.', ['Camouflage', 'Mimicry', 'Migration', 'Hibernation'], 0),
   ('A harmless fly that looks like a stinging wasp is an example of ___.', ['Mimicry', 'Camouflage', 'Migration', 'Hibernation'], 0),
   ('Both camouflage and mimicry help animals ___.', ['Avoid being caught by predators', 'Fly faster through the air', 'Grow bigger more quickly', 'Find water more easily'], 0)])

d106_ss = mk('SocialStudies', 'Languages of the World: How People Communicate Differently',
  'Ontario Grade 2 Social Studies People and Environments strand: students learn that people around the world speak many different languages, and that Canada itself has two official languages, English and French.',
  [('What are the two official languages of Canada?', ['English and French', 'English and Spanish', 'French and German', 'English and Mandarin'], 0),
   ('Why do different countries around the world often speak different languages?', ['Language is often connected to a country history and culture', 'Every country in the world speaks the exact same language', 'Language has no connection to culture', 'Countries are not allowed different languages'], 0),
   ('What is one way people can communicate even if they do not speak the same language?', ['Using gestures, pictures, or a translator', 'It is impossible to communicate at all', 'By refusing to interact', 'By speaking louder in their own language'], 0),
   ('Learning about different languages around the world helps students understand ___.', ['That people communicate in many different ways', 'That only one language exists', 'That language does not matter', 'That every language sounds the same'], 0),
   ('In Canada, French is especially widely spoken in which province?', ['Quebec', 'British Columbia', 'Alberta', 'Newfoundland and Labrador'], 0)])

# ─── DAY 107 ────────────────────────────────────────────────────────────────
d107_lang = mk('Language', 'Story Mood: How a Story Makes Us Feel',
  'Ontario Grade 2 Reading strand: students learn that mood is the feeling a story creates for the reader, such as happy, scary, or calm, built through word choice, setting, and events.',
  [('What is the mood of a story?', ['The feeling a story creates for the reader', 'The title of the story', 'The number of characters in a story', 'The length of the story'], 0),
   ('Which words might create a scary mood in a story?', ['Dark, creaking, and shadowy', 'Sunny, cheerful, and bright', 'Warm, friendly, and calm', 'Colourful, happy, and playful'], 0),
   ('Which words might create a happy mood in a story?', ['Bright, cheerful, and sunny', 'Dark, gloomy, and cold', 'Silent, empty, and grey', 'Frightening, eerie, and strange'], 0),
   ('How can a writer create mood in a story?', ['By choosing specific words and details', 'By using no words at all', 'By avoiding all descriptions', 'Mood cannot be created by a writer'], 0),
   ('Understanding the mood of a story helps readers ___.', ['Connect more deeply with how the story feels', 'Ignore the events of the story', 'Skip reading the story entirely', 'Avoid understanding the characters'], 0)])

d107_math = mk('Math', 'Locating Numbers on a Number Line to 1000',
  'Ontario Grade 2 Number strand: students learn to locate and compare three-digit numbers on a number line, understanding that numbers further to the right are greater in value.',
  [('On a number line, numbers further to the right are ___.', ['Greater in value', 'Smaller in value', 'Always negative', 'Always equal'], 0),
   ('On a number line from 0 to 1000, which number would be closer to 1000: 850 or 350?', ['850', '350', 'They are equally close', 'Neither number fits on the line'], 0),
   ('If you locate 400 and 600 on a number line, which number is further to the right?', ['600', '400', 'Both are in the same spot', 'Neither can be placed'], 0),
   ('A number line can help you find a number that is ___.', ['Between two other numbers', 'Impossible to compare', 'Always the smallest number', 'Always the largest number'], 0),
   ('Where would the number 500 be located on a number line from 0 to 1000?', ['Exactly in the middle', 'At the very end', 'At the very start', 'Off the number line completely'], 0)])

d107_sci = mk('Science', 'Life Cycle of an Insect: From Egg to Adult',
  'Ontario Grade 2 Life Systems strand: students learn that many insects go through a life cycle with several stages, such as egg, larva, pupa, and adult, changing form as they grow.',
  [('What is usually the first stage in an insect life cycle?', ['Egg', 'Adult', 'Pupa', 'Larva'], 0),
   ('What is the larva stage of an insect life cycle?', ['A young, worm-like stage that hatches from an egg', 'The final adult stage', 'The stage where the insect lays eggs', 'A stage that never actually happens'], 0),
   ('During the pupa stage, what is happening inside the insect?', ['Its body is changing into its adult form', 'It is laying new eggs', 'It is hunting for food actively', 'It is migrating to a new country'], 0),
   ('Which of these correctly orders the stages of many insect life cycles?', ['Egg, larva, pupa, adult', 'Adult, egg, larva, pupa', 'Pupa, adult, egg, larva', 'Larva, adult, egg, pupa'], 0),
   ('Why is learning about insect life cycles useful?', ['It helps us understand how insects grow and change over time', 'Insects never actually change form', 'All insects look the same their entire life', 'Life cycles have no connection to insects'], 0)])

d107_ss = mk('SocialStudies', 'The Underground Railroad: A Journey to Freedom',
  'Ontario Grade 2 Social Studies Heritage and Identity strand: students learn that the Underground Railroad was a secret network of routes and safe houses that helped freedom seekers travel to Canada to escape slavery.',
  [('What was the Underground Railroad?', ['A secret network of routes and safe houses to help freedom seekers reach Canada', 'An actual railroad built underground', 'A modern subway system', 'A type of Canadian sports league'], 0),
   ('Why did freedom seekers travel along the Underground Railroad?', ['To escape slavery and reach freedom in Canada', 'To visit family for a short trip', 'To attend a school in another country', 'To go on a vacation'], 0),
   ('Did the Underground Railroad involve an actual train running underground?', ['No, it was a network of secret routes and safe houses', 'Yes, it was a real underground train', 'It was a type of airplane route', 'It was a type of Canadian highway'], 0),
   ('Why might people helping freedom seekers along the route need to keep it secret?', ['To protect the freedom seekers from being caught', 'Secrecy was not important at all', 'Everyone already knew every detail', 'It was not dangerous for anyone involved'], 0),
   ('The Underground Railroad is an important part of history because it shows ___.', ['People helping others reach freedom and safety', 'That freedom was never an important idea', 'That helping others was not valued', 'That Canada played no role in this history'], 0)])

# ─── DAY 108 ────────────────────────────────────────────────────────────────
d108_lang = mk('Language', 'Using Transition Words: First, Next, Then, Finally',
  'Ontario Grade 2 Writing strand: students learn to use transition words such as first, next, then, and finally to show the order of events clearly when writing instructions or telling a story.',
  [('What is a transition word?', ['A word that shows the order of events', 'A word that names a person', 'A word that describes a colour', 'A word used only in math'], 0),
   ('Which transition word would you use to show what happens at the very beginning?', ['First', 'Finally', 'Then', 'Before that'], 0),
   ('Which transition word would you use to show what happens at the very end?', ['Finally', 'First', 'Next', 'Before'], 0),
   ('Why are transition words helpful in writing instructions?', ['They help the reader follow the correct order of steps', 'They make instructions harder to follow', 'They are never used in writing', 'They only belong in math problems'], 0),
   ('Which sentence correctly uses a transition word?', ['First, mix the flour and sugar together.', 'Mix flour sugar first the together.', 'The first together mix flour sugar.', 'Sugar flour first mix together the.'], 0)])

d108_math = mk('Math', 'Mental Math Strategies: Doubling and Halving',
  'Ontario Grade 2 Number strand: students learn mental math strategies for doubling a number, such as thinking of 7 plus 7, and for halving a number, such as sharing 14 into two equal groups.',
  [('What does it mean to double a number?', ['To add the number to itself', 'To cut the number in half', 'To multiply the number by 0', 'To subtract 1 from the number'], 0),
   ('What is double 6?', ['12', '8', '10', '6'], 0),
   ('What does it mean to halve a number?', ['To split the number into two equal parts', 'To add the number to itself', 'To multiply the number by 10', 'To round the number up'], 0),
   ('What is half of 16?', ['8', '6', '10', '12'], 0),
   ('Doubling and halving are useful mental math strategies because they help you ___.', ['Solve problems quickly in your head', 'Never solve a problem correctly', 'Only work with written calculations', 'Avoid using numbers at all'], 0)])

d108_sci = mk('Science', 'Exoskeletons and Endoskeletons: Two Kinds of Body Support',
  'Ontario Grade 2 Life Systems strand: students learn that some animals, like insects, have a hard outer covering called an exoskeleton for support, while other animals, like humans, have an internal skeleton called an endoskeleton.',
  [('What is an exoskeleton?', ['A hard outer covering that supports and protects an animal body', 'A skeleton found inside the body', 'A type of plant root', 'A soft, flexible skin only'], 0),
   ('What is an endoskeleton?', ['A skeleton found inside the body', 'A hard covering found outside the body', 'A type of leaf', 'A body covering made of feathers'], 0),
   ('Which of these animals has an exoskeleton?', ['An insect', 'A dog', 'A human', 'A bird'], 0),
   ('Which of these animals has an endoskeleton?', ['A human', 'An insect', 'A crab', 'A spider'], 0),
   ('Both exoskeletons and endoskeletons help an animal by ___.', ['Providing support and protection for the body', 'Making the animal invisible', 'Helping the animal breathe underwater only', 'Preventing the animal from moving at all'], 0)])

d108_ss = mk('SocialStudies', 'Map Scale: Understanding How Maps Show Real Distances',
  'Ontario Grade 2 Social Studies strand: students learn that a map scale shows how a distance on a map compares to the real distance in the world, helping map readers estimate how far apart places actually are.',
  [('What is a map scale?', ['A tool that shows how map distance compares to real distance', 'A drawing of a mountain', 'A list of city names', 'A picture of a compass'], 0),
   ('Why do maps include a scale?', ['To help readers estimate real distances between places', 'Scales have no purpose on a map', 'To make the map more colourful', 'To replace the map legend'], 0),
   ('If a map scale shows that 1 centimetre equals 10 kilometres, what does 3 centimetres on the map represent?', ['30 kilometres', '10 kilometres', '3 kilometres', '13 kilometres'], 0),
   ('Which map tool helps you understand what symbols mean, working alongside the scale?', ['The map legend', 'The compass rose only', 'The title only', 'The border only'], 0),
   ('Understanding map scale helps students ___.', ['Estimate how far apart real places are', 'Ignore distances between places', 'Make maps less useful', 'Avoid using maps altogether'], 0)])

# ─── DAY 109 ────────────────────────────────────────────────────────────────
d109_lang = mk('Language', 'Writing a Descriptive Paragraph Using the Five Senses',
  'Ontario Grade 2 Writing strand: students learn to write a descriptive paragraph that uses details from the five senses, sight, sound, smell, taste, and touch, to help readers picture what is being described.',
  [('What is a descriptive paragraph?', ['A paragraph that uses details to help readers picture something', 'A paragraph with no details at all', 'A list of math facts', 'A paragraph that only asks questions'], 0),
   ('Which sense would help you describe how fresh bread smells?', ['Smell', 'Sight', 'Hearing', 'Taste'], 0),
   ('Which sentence uses a sense detail about sound?', ['The leaves crunched loudly under our feet.', 'The leaves were bright orange.', 'The leaves felt dry and crisp.', 'The leaves tasted bitter.'], 0),
   ('Why do writers use sensory details in descriptive writing?', ['To help readers imagine the experience more vividly', 'Sensory details make writing less interesting', 'Descriptive writing should avoid all details', 'Sensory details have no purpose in writing'], 0),
   ('Which of these uses the sense of touch in a description?', ['The blanket felt soft and warm.', 'The blanket was bright red.', 'The blanket smelled like flowers.', 'The blanket made a rustling sound.'], 0)])

d109_math = mk('Math', 'Congruent Shapes: Same Size and Same Shape',
  'Ontario Grade 2 Geometry strand: students learn that two shapes are congruent when they are exactly the same size and the same shape, even if they are turned or flipped in a different direction.',
  [('What does it mean for two shapes to be congruent?', ['They are exactly the same size and shape', 'They are the same colour only', 'They have different sizes but the same shape', 'They have the same size but different shapes'], 0),
   ('If you flip a congruent shape over, is it still congruent to the original?', ['Yes, flipping does not change its size or shape', 'No, flipping always changes the shape', 'Flipping always makes it larger', 'Flipping always makes it smaller'], 0),
   ('Which pair of shapes would be congruent?', ['Two triangles that are the exact same size and shape', 'A large square and a small square', 'A triangle and a circle', 'A rectangle and a square'], 0),
   ('Turning a shape to face a different direction ___ its congruence to the original.', ['Does not change', 'Always changes', 'Always doubles', 'Always erases'], 0),
   ('Identifying congruent shapes helps students understand ___.', ['That shapes can be equal in size and shape even when turned', 'That all shapes are always congruent', 'That size never matters when comparing shapes', 'That congruent shapes must be different colours'], 0)])

d109_sci = mk('Science', 'Seed Dispersal: How Plants Spread Their Seeds',
  'Ontario Grade 2 Life Systems strand: students learn that plants disperse, or spread, their seeds in different ways, such as wind carrying light seeds, water carrying floating seeds, and animals carrying seeds in fur or after eating fruit.',
  [('What does it mean for a plant to disperse its seeds?', ['To spread its seeds to new places', 'To keep all its seeds in one spot forever', 'To stop making seeds completely', 'To turn its seeds into flowers'], 0),
   ('How might wind help disperse seeds?', ['By carrying light seeds through the air to new places', 'Wind never affects seeds at all', 'By burying seeds underground', 'By turning seeds into water'], 0),
   ('How might an animal help disperse the seeds of a plant?', ['By carrying seeds in its fur or eating fruit and dropping seeds elsewhere', 'Animals never interact with seeds', 'By destroying every seed it touches', 'By keeping seeds in one exact spot'], 0),
   ('Why is seed dispersal important for a plant?', ['It helps new plants grow in new places without overcrowding the parent plant', 'Seed dispersal has no benefit to a plant', 'It stops new plants from ever growing', 'It only helps animals, not plants'], 0),
   ('Which of these is a way that water can disperse seeds?', ['Carrying floating seeds downstream to a new location', 'Water never carries seeds anywhere', 'Water always destroys every seed', 'Water only affects fully grown plants'], 0)])

d109_ss = mk('SocialStudies', 'How Communities Help Each Other After a Disaster',
  'Ontario Grade 2 Social Studies strand: students learn that when a disaster such as a flood or storm affects a community, neighbours, volunteers, and organizations often work together to help people recover and rebuild.',
  [('What is one way communities help each other after a disaster?', ['Neighbours and volunteers work together to help people recover', 'Communities always ignore people in need', 'Disasters never affect communities', 'No one is ever able to help after a disaster'], 0),
   ('Which of these is an example of a natural disaster?', ['A flood', 'A quiet sunny afternoon', 'A calm lake', 'A regular school day'], 0),
   ('Why might volunteers collect food and supplies after a disaster?', ['To help people who lost their homes or belongings', 'Volunteers never collect supplies', 'Supplies are not needed after a disaster', 'Only governments are allowed to help'], 0),
   ('What is one way people can prepare before a disaster happens?', ['Making an emergency plan and kit', 'Ignoring the possibility of a disaster', 'Refusing to plan for emergencies', 'Avoiding all safety information'], 0),
   ('Communities that help each other after a disaster show the importance of ___.', ['Cooperation and caring for one another', 'Working alone with no help from others', 'Ignoring people who need assistance', 'Avoiding community involvement'], 0)])

# ─── DAY 110 (Review) ───────────────────────────────────────────────────────
d110_lang = mk('Language', 'Language Review: Sentences, Grammar, and Story Comprehension',
  'Students review recent Language skills: subjects and predicates, articles a/an/the, verb tenses, using illustrations to understand a story, comparing and contrasting texts, following multi-step directions, story mood, transition words, and writing descriptive paragraphs using the five senses.',
  [('What is the subject of a sentence?', ['The part that names who or what the sentence is about', 'The part that tells what the subject does', 'A punctuation mark at the end', 'A describing word only'], 0),
   ('Which sentence uses the correct article?', ['She ate an apple.', 'She ate a apple.', 'She ate the apple an.', 'She ate apple a.'], 0),
   ('Which sentence is in the future tense?', ['They will visit the zoo tomorrow.', 'They visited the zoo yesterday.', 'They visit the zoo often.', 'They were visiting the zoo.'], 0),
   ('What does it mean to contrast two things?', ['To describe how they are different', 'To describe how they are exactly the same', 'To combine them into one thing', 'To measure their size'], 0),
   ('Why do writers use sensory details in descriptive writing?', ['To help readers imagine the experience more vividly', 'Sensory details make writing less interesting', 'Descriptive writing should avoid all details', 'Sensory details have no purpose in writing'], 0)])

d110_math = mk('Math', 'Math Review: Multiplication, Geometry, and Number Sense',
  'Students review recent Math skills: multiplication facts for 0s, 1s, and 10s, composing and decomposing 2D shapes, number patterns on a hundred chart, estimating length, interpreting bar graphs with a scale, ordering numbers to 1000, locating numbers on a number line, doubling and halving, and congruent shapes.',
  [('What is 6 times 10?', ['60', '16', '6', '610'], 0),
   ('On a hundred chart, what happens to a number as you move down one row?', ['It increases by 10', 'It increases by 1', 'It decreases by 10', 'It stays the same'], 0),
   ('Which number is the greatest: 342, 423, or 234?', ['423', '342', '234', 'They are all equal'], 0),
   ('What is half of 16?', ['8', '6', '10', '12'], 0),
   ('What does it mean for two shapes to be congruent?', ['They are exactly the same size and shape', 'They are the same colour only', 'They have different sizes but the same shape', 'They have the same size but different shapes'], 0)])

d110_sci = mk('Science', 'Science Review: Earth, Animals, and Plants',
  'Students review recent Science topics: weathering, animal movement, food webs, tundra habitats, the skin, camouflage and mimicry, insect life cycles, exoskeletons and endoskeletons, and seed dispersal.',
  [('What is weathering?', ['The slow breaking down of rocks by wind, water, and ice', 'The movement of soil from one place to another', 'A type of severe storm', 'The melting of snow in spring'], 0),
   ('What is a food web?', ['Many connected food chains showing how animals eat different things', 'A single line showing one animal eating one plant', 'A spider web found in a garden', 'A chart of animal habitats only'], 0),
   ('What is one important job of the skin?', ['Protecting the body from germs and injury', 'Pumping blood through the body', 'Breaking down food for energy', 'Sending messages to the brain only'], 0),
   ('What is mimicry?', ['When a harmless animal looks like a dangerous one to stay safe', 'When an animal blends perfectly into a rock', 'When an animal grows a new colour every day', 'When an animal hides underground forever'], 0),
   ('What is an exoskeleton?', ['A hard outer covering that supports and protects an animal body', 'A skeleton found inside the body', 'A type of plant root', 'A soft, flexible skin only'], 0)])

d110_ss = mk('SocialStudies', 'Social Studies Review: Canadian Heritage, Government, and Geography',
  'Students review recent Social Studies topics: Terry Fox, democracy, provincial and territorial capital cities, First Nations, Inuit, and Metis peoples, national emblems, languages of the world, the Underground Railroad, map scale, and communities helping after a disaster.',
  [('What did Terry Fox call his run across Canada?', ['The Marathon of Hope', 'The Race for Canada', 'The Great Canadian Walk', 'The Freedom Run'], 0),
   ('What is a democracy?', ['A system where citizens have a voice and vote for their leaders', 'A system with no leaders at all', 'A place where only one person makes every decision', 'A system where citizens cannot vote'], 0),
   ('What are the three distinct groups of Indigenous peoples in Canada?', ['First Nations, Inuit, and Metis', 'Settlers, explorers, and traders', 'Farmers, teachers, and mayors', 'Provinces, cities, and towns'], 0),
   ('What was the Underground Railroad?', ['A secret network of routes and safe houses to help freedom seekers reach Canada', 'An actual railroad built underground', 'A modern subway system', 'A type of Canadian sports league'], 0),
   ('What is one way communities help each other after a disaster?', ['Neighbours and volunteers work together to help people recover', 'Communities always ignore people in need', 'Disasters never affect communities', 'No one is ever able to help after a disaster'], 0)])


g2_101_110 = [
    day(101, [d101_lang, d101_math, d101_sci, d101_ss]),
    day(102, [d102_lang, d102_math, d102_sci, d102_ss]),
    day(103, [d103_lang, d103_math, d103_sci, d103_ss]),
    day(104, [d104_lang, d104_math, d104_sci, d104_ss]),
    day(105, [d105_lang, d105_math, d105_sci, d105_ss]),
    day(106, [d106_lang, d106_math, d106_sci, d106_ss]),
    day(107, [d107_lang, d107_math, d107_sci, d107_ss]),
    day(108, [d108_lang, d108_math, d108_sci, d108_ss]),
    day(109, [d109_lang, d109_math, d109_sci, d109_ss]),
    day(110, [d110_lang, d110_math, d110_sci, d110_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_101_110)
    append_to(2, g2_101_110)
