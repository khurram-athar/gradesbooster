#!/usr/bin/env python3
"""Grade 2, Days 91-100 -- SEVENTH batch, extending Grade 2 through Day 100.
Self-contained script modeled exactly on gen_grade2_days81_90.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-90 topics (see data/grade2.ts / data/grade2.json). No embedded ASCII
double-quote or straight apostrophe characters are used anywhere in
title/summary/quiz/worksheet text -- contractions and possessives are
avoided entirely (or rewritten without the apostrophe) to keep the
generated .ts string literals valid.
"""
import os
import urllib.parse
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import lbl

DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')


def sub(subject_key, title, summary, worksheet, quiz):
    return [subject_key, title, summary, worksheet, quiz]


def day(n, subs):
    return [n, subs]


def append_worksheet_days(grade, days):
    p = f'{DIR}/grade{grade}.ts'
    content = open(p).read().rstrip()
    if content.endswith('export default curriculum;'):
        content = content[:-len('export default curriculum;')].rstrip()
    if content.endswith('];'):
        content = content[:-len('];')].rstrip()
    if content.endswith(']}'):
        content += ','
    extra = []
    for d in days:
        n, subs = d
        extra.append(f'{{day:{n}, label:"{lbl(n)}", subjects:[')
        for s in subs:
            sk, ti, su, ws, quiz = s
            rl = f'YouTube: {ti}'
            ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{ti} grade 2 educational')
            extra.append(f'  {{subject:"{sk}", title:"{ti}", summary:"{su}",')
            extra.append(f'   resourceLabel:"{rl}", resourceUrl:"{ru}",')
            extra.append('   quiz:[')
            for i, (q, opts, a) in enumerate(quiz):
                sep = ',' if i < len(quiz) - 1 else ''
                os2 = ','.join(f'"{o}"' for o in opts)
                extra.append(f'     {{q:"{q}", options:[{os2}], answer:{a}}}{sep}')
            extra.append('   ],')
            extra.append('   worksheet:[')
            for i, (prompt, answers) in enumerate(ws):
                sep = ',' if i < len(ws) - 1 else ''
                ans2 = ','.join(f'"{a}"' for a in answers)
                extra.append(f'     {{prompt:"{prompt}", answers:[{ans2}]}}{sep}')
            extra.append('   ]},')
        extra.append(']},')
    extra += ['];', '', 'export default curriculum;']
    open(p, 'w').write(content + '\n' + '\n'.join(extra))
    print(f'grade{grade}.ts appended {len(days)} days (with worksheets)')


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


# ─── DAY 91 ─────────────────────────────────────────────────────────────────
d91_lang = sub('Language', 'Personification: Giving Human Traits to Objects',
  'Ontario Grade 2 Language strand: students learn that personification gives human qualities to an animal, object, or idea, such as saying the wind whispered or the sun smiled, to make writing more vivid.',
  [('What do we call it when a writer gives human qualities to an object, like saying the wind whispered?', ['personification']),
   ('In the sentence the leaves danced in the breeze, what human action is given to the leaves?', ['dancing', 'danced']),
   ('Does personification make writing more vivid and interesting?', ['yes'])],
  [('What is personification?', ['Giving human qualities to an object, animal, or idea', 'A word that names a person only', 'A type of punctuation mark', 'A sentence with no meaning at all'], 0),
   ('Which sentence is an example of personification?', ['The stars winked at us from the sky.', 'The stars are far away in the sky.', 'The sky was dark and clear.', 'The sky has many stars in it.'], 0),
   ('In the sentence the old car groaned as it started, what is being given a human quality?', ['The car', 'The driver', 'The road', 'The key'], 0),
   ('Why might a writer use personification in a story?', ['To make objects and animals feel more alive and interesting', 'Personification makes writing harder to understand', 'Personification has no purpose in writing', 'Personification is only used in math'], 0),
   ('Which of these gives a human trait to the wind?', ['The wind howled angrily through the trees.', 'The wind is a type of weather.', 'The wind can be strong or gentle.', 'The wind blows from the west today.'], 0)])

d91_math = sub('Math', 'Multiplication Facts: 8s and 9s',
  'Ontario Grade 2 Number strand: students practise and memorize multiplication facts for the 8 and 9 times tables, building on earlier work with the 2s, 3s, 4s, 5s, 6s, 7s, and 10s times tables.',
  [('What is 8 times 3?', ['24', 'twenty-four']),
   ('What is 9 times 2?', ['18', 'eighteen']),
   ('What is 8 times 5?', ['40', 'forty'])],
  [('What is 8 times 4?', ['32', '28', '36', '24'], 0),
   ('What is 9 times 3?', ['27', '24', '30', '18'], 0),
   ('What is 8 times 6?', ['48', '42', '54', '40'], 0),
   ('What is 9 times 5?', ['45', '40', '50', '36'], 0),
   ('What is 9 times 9?', ['81', '72', '90', '99'], 0)])

d91_sci = sub('Science', 'Vertebrates and Invertebrates: Animals With and Without Backbones',
  'Ontario Grade 2 Life Systems strand: students learn that animals with a backbone are called vertebrates, such as fish and birds, while animals without a backbone, such as insects and worms, are called invertebrates.',
  [('What do we call an animal that has a backbone?', ['vertebrate']),
   ('What do we call an animal that does not have a backbone?', ['invertebrate']),
   ('Is a worm a vertebrate or an invertebrate?', ['invertebrate'])],
  [('What is a vertebrate?', ['An animal that has a backbone', 'An animal that has no bones at all', 'An animal that lives only in water', 'A plant with a stem'], 0),
   ('What is an invertebrate?', ['An animal that does not have a backbone', 'An animal that always has fur', 'An animal that can fly', 'A type of rock'], 0),
   ('Which of these is a vertebrate?', ['A fish', 'A worm', 'A spider', 'A snail'], 0),
   ('Which of these is an invertebrate?', ['An insect', 'A bird', 'A dog', 'A fish'], 0),
   ('Vertebrates and invertebrates are grouped based on whether they have a ___.', ['Backbone', 'Tail', 'Colour', 'Home'], 0)])

d91_ss = sub('SocialStudies', 'Provincial and Territorial Symbols: Flowers, Birds, and Flags',
  'Ontario Grade 2 Social Studies strand: students learn that each Canadian province and territory has its own symbols, such as an official flower, bird, and flag, that represent its identity.',
  [('Name one kind of symbol a province might have, like a flower or a flag.', ['flower', 'flag', 'bird']),
   ('Does each Canadian province and territory have its own set of symbols?', ['yes']),
   ('What is the official flower of Ontario?', ['trillium'])],
  [('Which of these is an example of a provincial symbol?', ['An official provincial flower', 'A type of homework', 'A national anthem only', 'A single citys nickname'], 0),
   ('Why might a province choose an official bird or flower?', ['To represent something special about that province', 'Provinces are not allowed to have symbols', 'Symbols have no connection to a province', 'Every province must use the exact same symbols'], 0),
   ('What is the official flower of Ontario?', ['The trillium', 'The rose', 'The tulip', 'The sunflower'], 0),
   ('Provincial flags are usually flown alongside the ___.', ['Canadian flag', 'Flag of another country', 'Flag of a different city only', 'No other flag at all'], 0),
   ('Learning about provincial symbols helps us understand ___.', ['What makes each province unique', 'That every province is identical', 'That symbols are not important', 'That only Ontario has symbols'], 0)])

# ─── DAY 92 ─────────────────────────────────────────────────────────────────
d92_lang = sub('Language', 'Irregular Plural Nouns: Special Cases Like Mice and Geese',
  'Ontario Grade 2 Language strand: students learn that some plural nouns do not simply add -s or -es, but change in a special way, such as mouse becoming mice, goose becoming geese, and child becoming children.',
  [('What is the plural form of the word mouse?', ['mice']),
   ('What is the plural form of the word child?', ['children']),
   ('What is the plural form of the word goose?', ['geese'])],
  [('What is the plural of mouse?', ['Mice', 'Mouses', 'Mousees', 'Mices'], 0),
   ('What is the plural of tooth?', ['Teeth', 'Tooths', 'Teeths', 'Toothes'], 0),
   ('What is the plural of foot?', ['Feet', 'Foots', 'Feets', 'Footes'], 0),
   ('What is the plural of child?', ['Children', 'Childs', 'Childes', 'Childrens'], 0),
   ('Words like mice and geese are called irregular plurals because they ___.', ['Do not simply add -s or -es', 'Always add -s at the end', 'Never change at all', 'Are not real words'], 0)])

d92_math = sub('Math', 'Division with Remainders: When Sharing Does Not Come Out Even',
  'Ontario Grade 2 Number strand: students learn that when a group of objects cannot be shared equally, there may be some left over, called a remainder, such as sharing 10 stickers among 3 friends leaving 1 remainder.',
  [('If 10 stickers are shared equally among 3 friends, how many are left over as a remainder?', ['1', 'one']),
   ('What do we call the amount left over when a group cannot be shared equally?', ['remainder']),
   ('If 7 apples are shared equally among 2 people, how many apples are left over?', ['1', 'one'])],
  [('If 9 cookies are shared equally among 4 people, how many cookies are left over?', ['1', '2', '3', '0'], 0),
   ('If 13 marbles are shared equally among 3 people, how many marbles are left over?', ['1', '2', '3', '0'], 0),
   ('What do we call the amount left over after sharing equally?', ['A remainder', 'A product', 'A sum', 'A factor'], 0),
   ('If 8 crayons are shared equally among 2 people, is there a remainder?', ['No, they share evenly', 'Yes, there is 1 left over', 'Yes, there are 2 left over', 'Yes, there are 3 left over'], 0),
   ('If 11 grapes are shared equally among 5 people, how many grapes are left over?', ['1', '2', '0', '3'], 0)])

d92_sci = sub('Science', 'The Nervous System: How Our Brain Sends Messages',
  'Ontario Grade 2 Life Systems strand: students learn that our nervous system, made up of the brain, spinal cord, and nerves, sends messages through our body so we can think, feel, and move.',
  [('What organ is the control centre of our nervous system?', ['brain']),
   ('Name one part of the nervous system besides the brain, like the spinal cord or nerves.', ['spinal cord', 'nerves']),
   ('Does our nervous system help us feel, think, and move?', ['yes'])],
  [('What is the main job of the nervous system?', ['To send messages through the body', 'To pump blood through the body', 'To digest our food', 'To help us breathe only'], 0),
   ('Which organ is the control centre of the nervous system?', ['The brain', 'The stomach', 'The lungs', 'The skin'], 0),
   ('What connects the brain to the rest of the body to send messages?', ['Nerves', 'Muscles only', 'Bones only', 'Blood only'], 0),
   ('If you touch something hot, what helps you feel pain and pull your hand away quickly?', ['Your nervous system', 'Your digestive system', 'Your skeletal system only', 'Your circulatory system only'], 0),
   ('The spinal cord is best described as a pathway that ___.', ['Carries messages between the brain and body', 'Pumps blood to the heart', 'Breaks down food for energy', 'Filters air we breathe'], 0)])

d92_ss = sub('SocialStudies', 'Levels of Leadership: Prime Minister, Premier, and Mayor',
  'Ontario Grade 2 Social Studies strand: students learn that Canada has leaders at different levels of government, including the Prime Minister for the country, a Premier for each province, and a mayor for a city or town.',
  [('Who is the leader of the whole country of Canada?', ['prime minister']),
   ('Who is the leader of a province, like Ontario?', ['premier']),
   ('Who is the leader of a city or town?', ['mayor'])],
  [('Who leads the entire country of Canada?', ['The prime minister', 'The mayor', 'The premier', 'The principal'], 0),
   ('Who leads a province, such as Ontario?', ['The premier', 'The prime minister', 'The mayor', 'The governor'], 0),
   ('Who leads a city or town?', ['The mayor', 'The premier', 'The prime minister', 'The principal'], 0),
   ('Why does Canada have leaders at different levels?', ['Different levels of government handle different responsibilities', 'Only one leader is needed for everything', 'Leaders at different levels never work together', 'This concept has no connection to Canada'], 0),
   ('Which leader is responsible for decisions about a single city, like fixing local roads?', ['The mayor', 'The prime minister', 'The premier', 'A senator'], 0)])

# ─── DAY 93 ─────────────────────────────────────────────────────────────────
d93_lang = sub('Language', 'Making Inferences: Reading Between the Lines',
  'Ontario Grade 2 Reading strand: students learn to make an inference by using clues from the text along with what they already know to figure out something the author does not state directly.',
  [('What do we call figuring out something the author does not state directly, using clues?', ['inference', 'making an inference']),
   ('If a character is shivering and wearing a coat, what might you infer about the weather?', ['it is cold', 'cold']),
   ('Do readers use clues from the text and what they already know to make an inference?', ['yes'])],
  [('What is an inference?', ['A conclusion made using text clues and what you already know', 'A word written in bold letters', 'A sentence copied exactly from the text', 'The title of a book'], 0),
   ('If a character is smiling and jumping up and down, what might you infer about how they feel?', ['They feel happy or excited', 'They feel sick', 'They feel angry', 'They feel nothing at all'], 0),
   ('Which clue would help you infer that it is raining outside?', ['Characters are carrying umbrellas and wearing raincoats', 'Characters are wearing sunglasses', 'Characters are building a snowman', 'Characters are swimming in a pool'], 0),
   ('Why is making inferences an important reading skill?', ['It helps readers understand ideas the author does not state directly', 'It has no connection to understanding a story', 'Inferences are always stated directly by the author', 'Making inferences means ignoring the text completely'], 0),
   ('Making an inference is different from a fact because an inference is ___.', ['A conclusion based on clues, not something directly stated', 'Always written in the text exactly as shown', 'Never based on any clues at all', 'The same thing as a fact'], 0)])

d93_math = sub('Math', 'Naming Fraction Parts: Numerator and Denominator',
  'Ontario Grade 2 Number strand: students learn the vocabulary for the parts of a fraction, where the denominator shows how many equal parts a whole is divided into, and the numerator shows how many of those parts are being counted.',
  [('In the fraction 3 over 4, what number is the numerator?', ['3', 'three']),
   ('In the fraction 3 over 4, what number is the denominator?', ['4', 'four']),
   ('Does the denominator show how many equal parts a whole is divided into?', ['yes'])],
  [('In the fraction 2 over 5, what is the numerator?', ['2', '5', '7', '3'], 0),
   ('In the fraction 2 over 5, what is the denominator?', ['5', '2', '7', '3'], 0),
   ('What does the denominator of a fraction tell us?', ['How many equal parts the whole is divided into', 'How many parts are shaded or counted', 'The exact colour of the shape', 'The total number of shapes'], 0),
   ('What does the numerator of a fraction tell us?', ['How many of the equal parts are being counted', 'How many parts the whole is divided into', 'The size of the whole shape', 'The name of the shape'], 0),
   ('In the fraction 1 over 2, what does the number 2 represent?', ['The whole is divided into 2 equal parts', 'Only 2 parts are shaded', 'The shape has 2 corners', 'The shape is 2 centimetres long'], 0)])

d93_sci = sub('Science', 'Layers of the Earth: Crust, Mantle, and Core',
  'Ontario Grade 2 Earth and Space Systems strand: students learn that the Earth is made of layers, including the outer crust we live on, the hot mantle beneath it, and the core at the very centre.',
  [('What is the outer layer of the Earth called, the one we live on?', ['crust']),
   ('What is the very centre layer of the Earth called?', ['core']),
   ('Is the mantle located between the crust and the core?', ['yes'])],
  [('What is the outermost layer of the Earth called?', ['The crust', 'The mantle', 'The core', 'The atmosphere'], 0),
   ('What is the layer at the very centre of the Earth called?', ['The core', 'The crust', 'The mantle', 'The surface'], 0),
   ('Which layer of the Earth is located between the crust and the core?', ['The mantle', 'The atmosphere', 'The ocean', 'The soil'], 0),
   ('Which layer of the Earth do people, animals, and plants live on?', ['The crust', 'The core', 'The mantle', 'The ocean floor only'], 0),
   ('The layers of the Earth are best described as being arranged from the ___ to the very centre.', ['Outside surface inward', 'Centre outward only', 'Sky downward', 'Ocean upward'], 0)])

d93_ss = sub('SocialStudies', 'Voting and Elections: How We Choose Our Leaders',
  'Ontario Grade 2 Social Studies strand: students learn that in an election, people vote to choose their leaders, such as a mayor or prime minister, and that the person with the most votes usually wins.',
  [('What do we call the event where people choose their leaders by voting?', ['election']),
   ('What do we call marking a choice for a leader during an election?', ['voting', 'a vote']),
   ('Does the leader with the most votes usually win an election?', ['yes'])],
  [('What is an election?', ['An event where people vote to choose their leaders', 'A type of holiday celebration', 'A game played at recess', 'A kind of school assignment'], 0),
   ('What does it mean to vote?', ['To mark your choice for a leader or decision', 'To ignore an important decision', 'To build something out of blocks', 'To draw a picture of a leader'], 0),
   ('In most elections, who usually wins?', ['The person with the most votes', 'The tallest person', 'The person who votes last', 'The person who does not run at all'], 0),
   ('Why is voting an important part of choosing leaders?', ['It lets many people have a say in who leads them', 'Voting has no effect on who becomes a leader', 'Only one single person is allowed to decide', 'Elections never actually happen'], 0),
   ('Elections allow citizens to ___.', ['Help choose who represents them', 'Avoid all responsibility for their community', 'Ignore their communitys leadership', 'Prevent leaders from ever changing'], 0)])

# ─── DAY 94 ─────────────────────────────────────────────────────────────────
d94_lang = sub('Language', 'Using a Table of Contents and Index',
  'Ontario Grade 2 Reading strand: students learn that a table of contents at the front of a book lists chapters and page numbers, while an index at the back lists topics in alphabetical order to help readers find information quickly.',
  [('Where in a book would you usually find a table of contents, the front or the back?', ['front']),
   ('Where in a book would you usually find an index, the front or the back?', ['back']),
   ('Is an index organized in alphabetical order?', ['yes'])],
  [('What is a table of contents?', ['A list of chapters and page numbers at the front of a book', 'A list of every word in a book', 'A drawing on the cover of a book', 'A summary of the whole book'], 0),
   ('What is an index?', ['An alphabetical list of topics and their page numbers at the back of a book', 'A list of chapters at the front of a book', 'The name of the author', 'A picture of the main character'], 0),
   ('If you wanted to quickly find which chapter starts on page 20, which part of the book would help?', ['The table of contents', 'The index', 'The back cover', 'The title page'], 0),
   ('If you wanted to find every page that mentions volcanoes, which part of the book would help most?', ['The index', 'The table of contents', 'The front cover', 'The dedication page'], 0),
   ('Both a table of contents and an index help readers ___.', ['Find information in a book quickly', 'Memorize the entire book', 'Ignore the book completely', 'Draw new pictures for the book'], 0)])

d94_math = sub('Math', 'Rounding to the Nearest Hundred',
  'Ontario Grade 2 Number strand: students learn to round three-digit numbers to the nearest hundred by looking at the tens digit, building on earlier work rounding to the nearest ten.',
  [('What is 340 rounded to the nearest hundred?', ['300', 'three hundred']),
   ('What is 470 rounded to the nearest hundred?', ['500', 'five hundred']),
   ('What is 250 rounded to the nearest hundred?', ['300', 'three hundred'])],
  [('What is 180 rounded to the nearest hundred?', ['200', '100', '180', '190'], 0),
   ('What is 620 rounded to the nearest hundred?', ['600', '700', '650', '500'], 0),
   ('What is 750 rounded to the nearest hundred?', ['800', '700', '750', '600'], 0),
   ('To round a number to the nearest hundred, which digit do we look at?', ['The tens digit', 'The ones digit', 'The thousands digit', 'The first letter'], 0),
   ('What is 910 rounded to the nearest hundred?', ['900', '1000', '800', '910'], 0)])

d94_sci = sub('Science', 'Volcanoes: When Earth Crust Erupts',
  'Ontario Grade 2 Earth and Space Systems strand: students learn that a volcano is an opening in the Earth crust where hot melted rock, called magma, can erupt onto the surface as lava.',
  [('What do we call an opening in the Earth crust where hot melted rock can erupt?', ['volcano']),
   ('What do we call hot melted rock while it is still underground?', ['magma']),
   ('What do we call hot melted rock once it erupts onto the surface?', ['lava'])],
  [('What is a volcano?', ['An opening in the Earth crust where melted rock can erupt', 'A type of large lake', 'A very tall, cold mountain only', 'A kind of ocean current'], 0),
   ('What is magma?', ['Hot melted rock found underground', 'Cold hard rock found on the surface', 'A type of cloud', 'A kind of soil'], 0),
   ('What do we call magma once it erupts onto the surface?', ['Lava', 'Ash only', 'Mist', 'Sediment'], 0),
   ('Why might a volcanic eruption be dangerous?', ['Hot lava and ash can spread over a wide area', 'Volcanoes never actually erupt', 'Lava is always cool to the touch', 'Eruptions have no effect on the surrounding area'], 0),
   ('A volcano is best described as a place where the Earth crust can ___.', ['Release hot melted rock', 'Freeze completely solid', 'Turn into water', 'Disappear entirely'], 0)])

d94_ss = sub('SocialStudies', 'The Fur Trade: An Early Canadian Industry',
  'Ontario Grade 2 Social Studies strand: students learn that the fur trade was an early industry in Canadian history, where Indigenous peoples and European traders exchanged furs, such as beaver pelts, for goods.',
  [('What animal fur was especially valuable during the fur trade?', ['beaver']),
   ('Did Indigenous peoples and European traders exchange goods during the fur trade?', ['yes']),
   ('What word describes trading goods like furs for other items?', ['trade', 'trading'])],
  [('What was the fur trade?', ['An early industry where furs were exchanged for goods', 'A modern clothing store', 'A type of Canadian sport', 'A kind of school subject'], 0),
   ('Which animal fur was especially important during the fur trade?', ['The beaver', 'The elephant', 'The lion', 'The kangaroo'], 0),
   ('Who took part in the fur trade in early Canada?', ['Indigenous peoples and European traders', 'Only people living in cities today', 'Only modern-day shoppers', 'No one actually took part'], 0),
   ('Why was the fur trade important to early Canadian history?', ['It shaped trade relationships and early settlements', 'It has no connection to Canadian history', 'It only happened in a different country', 'It never actually involved any trading'], 0),
   ('The fur trade is an example of people exchanging goods, which we call ___.', ['Trading', 'Farming', 'Voting', 'Building'], 0)])

# ─── DAY 95 ─────────────────────────────────────────────────────────────────
d95_lang = sub('Language', 'Prefixes: dis- and mis-',
  'Ontario Grade 2 Language strand: students learn that adding the prefix dis- or mis- to a word can change its meaning to the opposite or to something done incorrectly, such as agree becoming disagree and spell becoming misspell.',
  [('Add dis- to the word agree. What new word do you make?', ['disagree']),
   ('Add mis- to the word spell. What new word do you make?', ['misspell']),
   ('Does adding dis- to a word often make it mean the opposite?', ['yes'])],
  [('What does adding dis- to the word agree create?', ['Disagree, meaning the opposite of agree', 'Agreeing, a different verb form', 'A word with no real meaning', 'Agreement, a completely unrelated noun'], 0),
   ('What does adding mis- to the word spell create?', ['Misspell, meaning to spell incorrectly', 'Spelling, a different verb form', 'A word with no real meaning', 'Spellful, an unrelated word'], 0),
   ('Which word means the opposite of obey?', ['Disobey', 'Reobey', 'Obeyful', 'Obeyness'], 0),
   ('Which word means to understand something incorrectly?', ['Misunderstand', 'Reunderstand', 'Disunderstand', 'Understandful'], 0),
   ('Adding dis- or mis- to a word usually changes its meaning to show ___.', ['The opposite or an incorrect action', 'A larger size', 'A brighter colour', 'A faster speed'], 0)])

d95_math = sub('Math', 'Equivalent Fractions: Different Names for the Same Amount',
  'Ontario Grade 2 Number strand: students learn that two fractions can be equivalent, meaning they name the same amount, such as one half being the same amount as two quarters.',
  [('Is one half the same amount as two quarters?', ['yes']),
   ('What word describes two fractions that name the same amount?', ['equivalent']),
   ('Is two quarters equivalent to one half?', ['yes'])],
  [('Which fraction is equivalent to one half?', ['Two quarters', 'One quarter', 'Three quarters', 'One third'], 0),
   ('What does it mean for two fractions to be equivalent?', ['They name the same amount', 'They always look exactly the same on paper', 'They can never be compared', 'One fraction must be larger'], 0),
   ('If a pizza is cut into 4 equal slices and you eat 2, what fraction is equivalent to what you ate?', ['One half', 'One quarter', 'Three quarters', 'One third'], 0),
   ('Two fractions can look different but still be ___.', ['Equivalent, naming the same amount', 'Always unrelated to each other', 'Impossible to compare', 'Always the exact same numbers'], 0),
   ('Which of these shows an equivalent fraction pair?', ['One half and two quarters', 'One half and one quarter', 'One third and one half', 'One quarter and three quarters'], 0)])

d95_sci = sub('Science', 'Animal Body Coverings: Fur, Feathers, Scales, and Skin',
  'Ontario Grade 2 Life Systems strand: students learn that animals have different body coverings, such as fur, feathers, scales, or smooth skin, which help protect them and suit the environment they live in.',
  [('Name one type of body covering an animal might have, like fur or feathers.', ['fur', 'feathers', 'scales', 'skin']),
   ('Do birds usually have feathers as their body covering?', ['yes']),
   ('Do fish usually have scales as their body covering?', ['yes'])],
  [('Which animal body covering do birds usually have?', ['Feathers', 'Fur', 'Scales', 'Shells'], 0),
   ('Which animal body covering do fish usually have?', ['Scales', 'Fur', 'Feathers', 'Wool'], 0),
   ('Which animal body covering do mammals like bears usually have?', ['Fur', 'Feathers', 'Scales', 'Shells'], 0),
   ('Why do animals have different body coverings?', ['To help protect them and suit their environment', 'Body coverings have no real purpose', 'All animals have the exact same body covering', 'Body coverings only affect how an animal looks'], 0),
   ('A frog usually has what kind of body covering?', ['Smooth, moist skin', 'Thick fur', 'Feathers', 'Hard scales like a fish'], 0)])

d95_ss = sub('SocialStudies', 'Treaties: Agreements Between Indigenous Peoples and Newcomers',
  'Ontario Grade 2 Social Studies strand: students learn that a treaty is a formal agreement, often about sharing land and resources, that was made between Indigenous peoples and newcomers to Canada.',
  [('What word describes a formal agreement about sharing land and resources?', ['treaty']),
   ('Were treaties made between Indigenous peoples and newcomers to Canada?', ['yes']),
   ('Do treaties often involve agreements about land?', ['yes'])],
  [('What is a treaty?', ['A formal agreement, often about sharing land and resources', 'A type of Canadian sport', 'A kind of school subject', 'A holiday celebrated in December'], 0),
   ('Who were treaties in Canadian history often made between?', ['Indigenous peoples and newcomers', 'Only people living in one single city', 'Only people from a different country entirely', 'No one, they never actually happened'], 0),
   ('What might a treaty be an agreement about?', ['Sharing land and resources', 'What food to eat for breakfast', 'Which sports team wins a game', 'What clothes to wear each day'], 0),
   ('Why are treaties an important part of Canadian history?', ['They shaped relationships between Indigenous peoples and newcomers', 'They have no connection to Canadian history', 'They only affected people outside of Canada', 'They were never actually followed by anyone'], 0),
   ('Learning about treaties helps students understand ___.', ['Important agreements in Canadian history', 'Nothing relevant about Canada', 'Only modern-day sports rules', 'Only how to read a map'], 0)])

# ─── DAY 96 ─────────────────────────────────────────────────────────────────
d96_lang = sub('Language', 'Suffixes: Adding -ly to Turn Adjectives into Adverbs',
  'Ontario Grade 2 Language strand: students learn that adding the suffix -ly to many adjectives creates an adverb, describing how an action is done, such as quiet becoming quietly and slow becoming slowly.',
  [('Add -ly to the word quiet. What new word do you make?', ['quietly']),
   ('Add -ly to the word slow. What new word do you make?', ['slowly']),
   ('Does an adverb ending in -ly usually describe how an action is done?', ['yes'])],
  [('What does adding -ly to the word slow create?', ['Slowly, an adverb describing how something is done', 'Slower, a comparing word', 'Slowness, a different noun', 'Sloth, an unrelated word'], 0),
   ('Which word is an adverb formed by adding -ly?', ['Quietly', 'Quiet', 'Quieter', 'Quietness'], 0),
   ('In the sentence she ran quickly, what does the word quickly describe?', ['How she ran', 'What she is wearing', 'Where she is going', 'Who she is'], 0),
   ('Add -ly to the word careful. What new word do you make?', ['Carefully', 'Carefuler', 'Carefulness', 'Careless'], 0),
   ('Adding -ly to an adjective usually creates a word that describes ___.', ['How an action happens', 'A person or place', 'A number of objects', 'A colour only'], 0)])

d96_math = sub('Math', 'Multi-Step Word Problems: Addition and Subtraction Together',
  'Ontario Grade 2 Number strand: students learn to solve word problems that require more than one step, such as adding two amounts together and then subtracting a third amount, to find a final answer.',
  [('If you have 5 apples, get 4 more, then give away 3, how many apples do you have left?', ['6', 'six']),
   ('What does a multi-step word problem require you to do?', ['more than one step', 'more than one operation']),
   ('If you start with 10 stickers, get 5 more, then use 2, how many stickers are left?', ['13', 'thirteen'])],
  [('A boy has 6 marbles, finds 5 more, then loses 4. How many marbles does he have now?', ['7', '6', '8', '11'], 0),
   ('A class has 12 pencils, gets 8 more, then gives away 6. How many pencils are left?', ['14', '12', '20', '6'], 0),
   ('A farmer has 20 eggs, sells 9, then collects 5 more. How many eggs does the farmer have now?', ['16', '15', '11', '25'], 0),
   ('What is the first step when solving a multi-step word problem?', ['Figuring out what the problem is asking and what steps are needed', 'Skipping the problem entirely', 'Guessing the answer with no plan', 'Only reading the last sentence'], 0),
   ('A store has 15 toys, sells 7, then receives 10 more. How many toys does the store have now?', ['18', '15', '25', '8'], 0)])

d96_sci = sub('Science', 'Symbiosis: When Living Things Help Each Other',
  'Ontario Grade 2 Life Systems strand: students learn that symbiosis is a close relationship between two different living things, such as bees and flowers, where one or both living things benefit.',
  [('What word describes a close relationship between two different living things?', ['symbiosis']),
   ('Name one pair of living things that help each other, like bees and flowers.', ['bees and flowers']),
   ('Can symbiosis benefit one or both living things involved?', ['yes'])],
  [('What is symbiosis?', ['A close relationship between two different living things', 'A type of rock formation', 'A kind of weather pattern', 'A single living thing with no relationships'], 0),
   ('Which of these is an example of symbiosis?', ['Bees collecting nectar and pollinating flowers', 'A rock sitting in a field', 'A cloud floating in the sky', 'A river flowing downhill'], 0),
   ('How do flowers benefit when bees visit them?', ['Bees help spread pollen so flowers can make seeds', 'Flowers are harmed every time a bee visits', 'Bees never actually visit flowers', 'Flowers have no connection to bees'], 0),
   ('How do bees benefit from visiting flowers?', ['Bees collect nectar from flowers for food', 'Bees are harmed by visiting flowers', 'Bees gain nothing at all from flowers', 'Bees only visit flowers for shelter'], 0),
   ('Symbiosis shows that living things in nature are often ___.', ['Connected and can help each other', 'Completely unrelated to each other', 'Always in danger from each other', 'Never able to interact at all'], 0)])

d96_ss = sub('SocialStudies', 'The United Nations: Countries Working Together',
  'Ontario Grade 2 Social Studies strand: students learn that the United Nations is a group made up of many countries, including Canada, that work together to solve world problems and keep peace.',
  [('What do we call the group made up of many countries working together?', ['United Nations']),
   ('Is Canada a member of the United Nations?', ['yes']),
   ('Does the United Nations try to help keep peace around the world?', ['yes'])],
  [('What is the United Nations?', ['A group of many countries that work together to solve world problems', 'A single countrys government only', 'A type of sports league', 'A kind of school club'], 0),
   ('Is Canada a member of the United Nations?', ['Yes, Canada is a member', 'No, Canada has never joined', 'Only some Canadian cities are members', 'Canada left the United Nations long ago'], 0),
   ('What is one goal of the United Nations?', ['To help keep peace around the world', 'To make every country identical', 'To stop countries from ever meeting', 'To end all forms of cooperation'], 0),
   ('Why might countries choose to work together through an organization like the United Nations?', ['Working together can help solve problems that affect many countries', 'Countries never benefit from working together', 'This concept has no connection to global citizenship', 'Only one single country can solve world problems alone'], 0),
   ('The United Nations is best described as an organization that helps countries ___.', ['Cooperate on shared world problems', 'Compete against each other constantly', 'Ignore problems in other countries', 'Avoid working together at all costs'], 0)])

# ─── DAY 97 ─────────────────────────────────────────────────────────────────
d97_lang = sub('Language', 'Sentence Variety: Combining Short and Long Sentences',
  'Ontario Grade 2 Writing strand: students learn that mixing short and long sentences in a piece of writing creates sentence variety, which can make writing more interesting to read.',
  [('What do we call mixing short and long sentences in writing?', ['sentence variety']),
   ('Can using only short sentences over and over make writing sound choppy?', ['yes']),
   ('Does sentence variety help make writing more interesting to read?', ['yes'])],
  [('What is sentence variety?', ['Mixing short and long sentences in writing', 'Using only short sentences', 'Using only long sentences', 'Never using any punctuation'], 0),
   ('Why might a writer use sentence variety?', ['To make writing more interesting to read', 'Sentence variety makes writing harder to read', 'Sentence variety has no purpose in writing', 'Writers should always use the exact same sentence length'], 0),
   ('Which set of sentences shows good sentence variety?', ['The dog ran. Excited and full of energy, it bounded across the yard chasing the ball.', 'The dog ran. The dog jumped. The dog barked. The dog played.', 'The dog ran fast fast fast fast fast.', 'Dog. Dog ran. Dog jumped. Dog barked.'], 0),
   ('What might happen if a writer only uses short, choppy sentences?', ['The writing might sound repetitive or robotic', 'The writing always sounds more interesting', 'Short sentences are always better than long ones', 'This has no effect on how writing sounds'], 0),
   ('Using a mix of sentence lengths can help writing sound more ___.', ['Natural and engaging', 'Confusing and unclear', 'Repetitive and boring', 'Impossible to read'], 0)])

d97_math = sub('Math', 'Conducting a Survey and Graphing the Results',
  'Ontario Grade 2 Data strand: students learn to collect data by asking classmates a survey question, then organize and display the results using a graph, such as a bar graph or pictograph.',
  [('What do we call asking people a question to collect information?', ['a survey']),
   ('After collecting survey data, what can be used to display the results?', ['a graph', 'a bar graph', 'a pictograph']),
   ('Does a survey help us collect information from a group of people?', ['yes'])],
  [('What is a survey?', ['A question asked to collect information from people', 'A type of graph only', 'A kind of math equation', 'A drawing of a shape'], 0),
   ('After conducting a survey about favourite fruits, what is a good next step?', ['Organize the results and display them on a graph', 'Throw away all the answers', 'Ignore what people said', 'Ask the exact same question forever'], 0),
   ('Which of these could be a good survey question for a class?', ['What is your favourite season?', 'What is the capital of France?', 'What is 5 plus 5?', 'What colour is the sky today?'], 0),
   ('Why is it useful to graph the results of a survey?', ['A graph makes the results easier to see and compare', 'Graphs make survey results harder to understand', 'Surveys should never be graphed', 'Graphing has no connection to data'], 0),
   ('Collecting survey data and graphing it is part of the ___ strand in math.', ['Data', 'Geometry', 'Measurement', 'Patterning'], 0)])

d97_sci = sub('Science', 'How Animals Communicate: Sounds, Signals, and Body Language',
  'Ontario Grade 2 Life Systems strand: students learn that animals communicate with each other using sounds, body language, and signals, such as a dog wagging its tail or a bird singing a song.',
  [('Name one way an animal might communicate, like making a sound or using body language.', ['sound', 'body language']),
   ('Can a wagging tail be a way a dog communicates?', ['yes']),
   ('Do animals use sounds to communicate with each other?', ['yes'])],
  [('Which of these is a way animals communicate?', ['Making sounds', 'Reading a book', 'Writing a letter', 'Using a telephone'], 0),
   ('What might a dog wagging its tail be communicating?', ['That it feels happy or excited', 'That it is asleep', 'That it cannot see anything', 'That it is a different animal'], 0),
   ('Why might a bird sing a song?', ['To communicate with other birds', 'Birds never make any sounds', 'Singing has no purpose for birds', 'Only humans can communicate with sound'], 0),
   ('Which of these is an example of animal body language?', ['A cat arching its back when scared', 'A cat sleeping quietly', 'A cat eating its food', 'A cat with closed eyes'], 0),
   ('Animal communication helps animals ___.', ['Warn others, find mates, or protect their group', 'Never interact with other animals', 'Ignore danger completely', 'Avoid all other animals forever'], 0)])

d97_ss = sub('SocialStudies', 'Canadian Agriculture Regions: What Grows Where',
  'Ontario Grade 2 Social Studies strand: students learn that different regions of Canada grow different crops and raise different animals based on their climate and land, such as wheat on the Prairies and fruit in Ontario.',
  [('Name one crop grown in a Canadian region, like wheat on the Prairies.', ['wheat']),
   ('Does the type of crop grown in a region depend on its climate and land?', ['yes']),
   ('Name one fruit or crop commonly grown in Ontario.', ['fruit', 'corn', 'apples'])],
  [('Which crop is commonly grown on the Canadian Prairies?', ['Wheat', 'Bananas', 'Pineapples', 'Coconuts'], 0),
   ('Why does the Prairie region grow so much wheat?', ['Its flat land and climate are well suited to growing grain crops', 'The Prairies have no farmland at all', 'Wheat cannot grow anywhere in Canada', 'The Prairies are covered entirely in ice year-round'], 0),
   ('What helps farmers decide what crops to grow in a region?', ['The climate and type of land in that region', 'The colour of the sky', 'The name of the province only', 'Farmers never consider climate or land'], 0),
   ('Which of these is grown in parts of Ontario?', ['Fruit, such as apples and peaches', 'Only bananas', 'Only rice', 'Only coconuts'], 0),
   ('Comparing farming across Canadian regions helps us understand ___.', ['How climate and land affect what people grow', 'That every region grows the exact same crops', 'That farming does not exist in Canada', 'That climate has no effect on farming'], 0)])

# ─── DAY 98 ─────────────────────────────────────────────────────────────────
d98_lang = sub('Language', 'Personal Narrative Writing: Telling a True Story About Yourself',
  'Ontario Grade 2 Writing strand: students learn to write a personal narrative, a true story about something that happened to them, told in order with a beginning, middle, and end, and including their own feelings.',
  [('What kind of writing tells a true story about something that happened to you?', ['personal narrative']),
   ('Should a personal narrative be told in order, with a beginning, middle, and end?', ['yes']),
   ('Can a personal narrative include how you felt during the event?', ['yes'])],
  [('What is a personal narrative?', ['A true story about something that happened to the writer', 'A made-up story about dragons', 'A list of math facts', 'A drawing with no words'], 0),
   ('Which of these would be a good topic for a personal narrative?', ['A time you visited your grandparents', 'The life cycle of a butterfly', 'The capital city of Ontario', 'How to multiply two numbers'], 0),
   ('Why might a writer include their own feelings in a personal narrative?', ['It helps readers understand the experience more fully', 'Feelings should never be included in writing', 'Personal narratives cannot include any feelings', 'This concept has no connection to narrative writing'], 0),
   ('A personal narrative is different from a book review because a narrative ___.', ['Tells a true story about the writer', 'Only reviews someone elses book', 'Never includes any events', 'Is always about a made-up character'], 0),
   ('A well organized personal narrative usually has a ___.', ['Beginning, middle, and end', 'Only a middle', 'No clear order at all', 'Only a title page'], 0)])

d98_math = sub('Math', 'Problem Solving: Choosing the Right Operation',
  'Ontario Grade 2 Number strand: students learn to read a word problem carefully and decide whether to add, subtract, multiply, or divide based on the clues and the question being asked.',
  [('If a word problem asks how many are left, which operation might you use?', ['subtraction', 'subtract']),
   ('If a word problem asks for a total when joining groups together, which operation might you use?', ['addition', 'add']),
   ('If a word problem asks how many equal groups can be made from a total, which operation might you use?', ['division', 'divide'])],
  [('If a problem asks how many items are left after some are given away, which operation should you use?', ['Subtraction', 'Addition', 'Multiplication', 'Division'], 0),
   ('If a problem asks for the total after combining two groups, which operation should you use?', ['Addition', 'Subtraction', 'Division', 'Comparison'], 0),
   ('If a problem asks how many items are in 4 equal groups of 5, which operation should you use?', ['Multiplication', 'Subtraction', 'Division', 'Addition of only one number'], 0),
   ('If a problem asks how many equal groups can be made when sharing 20 items among 4 friends, which operation should you use?', ['Division', 'Multiplication', 'Subtraction', 'Addition'], 0),
   ('Why is it important to read a word problem carefully before solving it?', ['It helps you choose the correct operation to use', 'The words in a problem never matter', 'Every problem always uses the same operation', 'Reading carefully has no effect on solving problems'], 0)])

d98_sci = sub('Science', 'Extreme Weather: Storms and Severe Conditions',
  'Ontario Grade 2 Earth and Space Systems strand: students learn about extreme weather events, such as thunderstorms, blizzards, and high winds, and how people can stay safe when severe weather happens.',
  [('Name one type of extreme weather, like a thunderstorm or blizzard.', ['thunderstorm', 'blizzard']),
   ('Can extreme weather include very strong winds?', ['yes']),
   ('Is it important to stay safe during severe weather?', ['yes'])],
  [('Which of these is an example of extreme weather?', ['A thunderstorm', 'A calm, sunny day', 'A gentle breeze', 'A light cloud'], 0),
   ('What is a blizzard?', ['A severe snowstorm with strong winds', 'A warm, sunny day', 'A light rain shower', 'A calm winter morning'], 0),
   ('Why is it important to know about extreme weather?', ['So people can prepare and stay safe', 'Extreme weather never actually happens', 'Knowing about weather has no benefit', 'Extreme weather is never dangerous'], 0),
   ('Which of these is a safe action during a thunderstorm?', ['Staying indoors away from windows', 'Standing under a tall tree outside', 'Swimming in an open lake', 'Flying a kite outside'], 0),
   ('Extreme weather events can include storms with ___.', ['Strong winds, heavy snow, or thunder and lightning', 'Only clear blue skies', 'Only gentle breezes', 'No weather at all'], 0)])

d98_ss = sub('SocialStudies', 'Canada and Its Neighbour: Sharing a Border with the United States',
  'Ontario Grade 2 Social Studies strand: students learn that Canada shares a long border with the United States, its neighbouring country to the south, and that people, goods, and ideas often cross between the two countries.',
  [('What country is located just south of Canada, sharing a long border?', ['United States']),
   ('Do people and goods sometimes cross the border between Canada and the United States?', ['yes']),
   ('Is the United States a neighbouring country of Canada?', ['yes'])],
  [('Which country shares a long border with Canada to the south?', ['The United States', 'Mexico', 'France', 'Brazil'], 0),
   ('What might cross the border between Canada and the United States?', ['People, goods, and ideas', 'Nothing ever crosses the border', 'Only animals cross the border', 'Only mail crosses the border'], 0),
   ('Why might Canada and the United States work together on some issues?', ['They are close neighbours who share a long border', 'The two countries have no connection at all', 'They are located on opposite sides of the world', 'Neighbouring countries never work together'], 0),
   ('Sharing a border with another country can lead to shared ___.', ['Trade and travel between the two countries', 'A complete lack of any connection', 'Two countries becoming exactly identical', 'No interaction of any kind'], 0),
   ('Canada is located ___ of the United States.', ['North', 'South', 'East', 'West'], 0)])

# ─── DAY 99 ─────────────────────────────────────────────────────────────────
d99_lang = sub('Language', 'Comparing Fiction and Nonfiction Texts',
  'Ontario Grade 2 Reading strand: students learn to compare fiction texts, which tell made-up stories, with nonfiction texts, which give true facts and information about real topics.',
  [('Does a fiction text tell a made-up story or give true facts?', ['made-up story', 'a made-up story']),
   ('Does a nonfiction text give true facts about a real topic?', ['yes']),
   ('Is a book about dragons flying likely to be fiction or nonfiction?', ['fiction'])],
  [('What is fiction?', ['A made-up story that is not literally true', 'A text that gives only true facts', 'A list of numbers', 'A drawing with no text'], 0),
   ('What is nonfiction?', ['A text that gives true facts and information', 'A made-up story about talking animals', 'A poem with no real meaning', 'A story that is always false'], 0),
   ('Which of these is most likely a nonfiction book?', ['A book about how volcanoes form', 'A book about a talking dragon', 'A book about a magic castle', 'A book about a wizard school'], 0),
   ('Which of these is most likely a fiction book?', ['A story about a superhero with magic powers', 'A book explaining the water cycle', 'A book about famous Canadian inventors', 'A book about how plants grow'], 0),
   ('Comparing fiction and nonfiction helps readers understand ___.', ['The difference between made-up stories and true information', 'That every book is exactly the same', 'That fiction and nonfiction have no differences', 'That only fiction books exist'], 0)])

d99_math = sub('Math', 'Problem Solving: Choosing the Right Operation (Applied Practice)',
  'Ontario Grade 2 Number strand: students apply their understanding of addition, subtraction, multiplication, and division to solve a variety of real-life word problems by first identifying what operation is needed.',
  [('If a problem asks how many stickers 3 friends have altogether if each has 4, which operation would you use?', ['multiplication', 'multiply']),
   ('If a problem asks how many are left after some are used, which operation would you use?', ['subtraction', 'subtract']),
   ('Why is it helpful to identify the operation before solving a word problem?', ['it helps you solve it correctly', 'to solve correctly'])],
  [('If 3 friends each have 4 stickers, how many stickers do they have altogether?', ['12', '7', '9', '15'], 0),
   ('If a baker makes 24 muffins and sells 15, how many muffins are left?', ['9', '39', '15', '24'], 0),
   ('If 18 crayons are shared equally among 3 children, how many crayons does each child get?', ['6', '15', '21', '3'], 0),
   ('A problem states a class collected 45 cans on Monday and 30 more on Tuesday. What operation finds the total?', ['Addition', 'Subtraction', 'Division', 'Multiplication'], 0),
   ('Applying the correct operation to a real-life problem helps us find the ___.', ['Accurate and reasonable answer', 'Least accurate answer possible', 'Answer with no connection to the problem', 'Longest possible answer'], 0)])

d99_sci = sub('Science', 'Ecosystems: How Living and Non-Living Things Work Together',
  'Ontario Grade 2 Life Systems strand: students learn that an ecosystem is made up of living things, such as plants and animals, and non-living things, such as water, air, and soil, all interacting together in one place.',
  [('What word describes living and non-living things interacting together in one place?', ['ecosystem']),
   ('Name one non-living part of an ecosystem, like water or soil.', ['water', 'air', 'soil']),
   ('Do living things in an ecosystem depend on non-living things like water and air?', ['yes'])],
  [('What is an ecosystem?', ['Living and non-living things interacting together in one place', 'Only the living things in a forest', 'Only the rocks and water in a place', 'A single plant growing alone'], 0),
   ('Which of these is a non-living part of an ecosystem?', ['Soil', 'A tree', 'A bird', 'A fish'], 0),
   ('Which of these is a living part of an ecosystem?', ['A plant', 'Sunlight', 'Water', 'Air'], 0),
   ('Why do living things in an ecosystem depend on non-living things?', ['They need things like water, air, and sunlight to survive', 'Living things need nothing from their surroundings', 'Non-living things have no effect on living things', 'This concept has no connection to ecosystems'], 0),
   ('An ecosystem is best described as a place where living and non-living things ___.', ['Interact and depend on each other', 'Never interact with each other at all', 'Exist completely separately', 'Have no connection whatsoever'], 0)])

d99_ss = sub('SocialStudies', 'Canadian Peacekeeping: Helping Keep the Peace Around the World',
  'Ontario Grade 2 Social Studies strand: students learn that Canada has a history of sending peacekeepers to help calm conflicts and support peace in other parts of the world.',
  [('What word describes people sent to help calm conflict and support peace?', ['peacekeepers']),
   ('Has Canada sent peacekeepers to help in other parts of the world?', ['yes']),
   ('Does peacekeeping aim to support peace during a conflict?', ['yes'])],
  [('What is a peacekeeper?', ['A person sent to help calm conflict and support peace', 'A person who starts conflicts', 'A person who ignores world events', 'A type of weather forecaster'], 0),
   ('Has Canada historically taken part in peacekeeping missions?', ['Yes, Canada has a history of peacekeeping', 'No, Canada has never taken part', 'Only other countries take part in peacekeeping', 'Peacekeeping has never existed'], 0),
   ('Why might a country send peacekeepers to another region?', ['To help support peace during a conflict', 'To make a conflict worse', 'Peacekeepers have no real purpose', 'To ignore problems happening elsewhere'], 0),
   ('Peacekeeping is connected to which broader idea learned in social studies?', ['Countries working together, like through the United Nations', 'Countries always working alone', 'Ignoring problems in other countries', 'Avoiding all international cooperation'], 0),
   ('Canadian peacekeepers are best described as people who help ___.', ['Support peace in other parts of the world', 'Create new conflicts around the world', 'Avoid helping anyone at all', 'Stay only within Canadian borders'], 0)])

# ─── DAY 100 (Review) ───────────────────────────────────────────────────────
d100_lang = sub('Language', 'Language Review: Figurative Language, Word Parts, and Text Types',
  'Students review recent Language skills: personification, irregular plural nouns, making inferences, using a table of contents and index, prefixes dis- and mis-, suffixes -ly, sentence variety, personal narrative writing, and comparing fiction and nonfiction.',
  [('What do we call giving human qualities to an object, like saying the wind whispered?', ['personification']),
   ('What is the plural form of the word mouse?', ['mice']),
   ('What is an inference?', ['a conclusion made using text clues and what you already know', 'a conclusion using clues'])],
  [('Which sentence is an example of personification?', ['The stars winked at us from the sky.', 'The stars are far away in the sky.', 'The sky was dark and clear.', 'The sky has many stars in it.'], 0),
   ('What is the plural of tooth?', ['Teeth', 'Tooths', 'Teeths', 'Toothes'], 0),
   ('Which word means the opposite of obey?', ['Disobey', 'Reobey', 'Obeyful', 'Obeyness'], 0),
   ('What is a personal narrative?', ['A true story about something that happened to the writer', 'A made-up story about dragons', 'A list of math facts', 'A drawing with no words'], 0),
   ('Which of these is most likely a nonfiction book?', ['A book about how volcanoes form', 'A book about a talking dragon', 'A book about a magic castle', 'A book about a wizard school'], 0)])

d100_math = sub('Math', 'Math Review: Multiplication, Fractions, and Problem Solving',
  'Students review recent Math skills: multiplication facts for 8s and 9s, division with remainders, naming fraction parts, rounding to the nearest hundred, equivalent fractions, multi-step word problems, surveys and graphing, and choosing the right operation.',
  [('What is 8 times 4?', ['32', 'thirty-two']),
   ('What do we call the amount left over when a group cannot be shared equally?', ['remainder']),
   ('In the fraction 3 over 4, what number is the numerator?', ['3', 'three'])],
  [('What is 9 times 3?', ['27', '24', '30', '18'], 0),
   ('What is 620 rounded to the nearest hundred?', ['600', '700', '650', '500'], 0),
   ('Which fraction is equivalent to one half?', ['Two quarters', 'One quarter', 'Three quarters', 'One third'], 0),
   ('A boy has 6 marbles, finds 5 more, then loses 4. How many marbles does he have now?', ['7', '6', '8', '11'], 0),
   ('If a problem asks for the total after combining two groups, which operation should you use?', ['Addition', 'Subtraction', 'Division', 'Comparison'], 0)])

d100_sci = sub('Science', 'Science Review: Animals, Earth, and Ecosystems',
  'Students review recent Science topics: vertebrates and invertebrates, the nervous system, layers of the Earth, volcanoes, animal body coverings, symbiosis, how animals communicate, extreme weather, and ecosystems.',
  [('What do we call an animal that has a backbone?', ['vertebrate']),
   ('What is the outer layer of the Earth called, the one we live on?', ['crust']),
   ('What word describes a close relationship between two different living things?', ['symbiosis'])],
  [('Which of these is a vertebrate?', ['A fish', 'A worm', 'A spider', 'A snail'], 0),
   ('What is a volcano?', ['An opening in the Earth crust where melted rock can erupt', 'A type of large lake', 'A very tall, cold mountain only', 'A kind of ocean current'], 0),
   ('Which animal body covering do birds usually have?', ['Feathers', 'Fur', 'Scales', 'Shells'], 0),
   ('Which of these is an example of extreme weather?', ['A thunderstorm', 'A calm, sunny day', 'A gentle breeze', 'A light cloud'], 0),
   ('What is an ecosystem?', ['Living and non-living things interacting together in one place', 'Only the living things in a forest', 'Only the rocks and water in a place', 'A single plant growing alone'], 0)])

d100_ss = sub('SocialStudies', 'Social Studies Review: Government, History, and Geography',
  'Students review recent Social Studies topics: provincial and territorial symbols, levels of leadership, voting and elections, the fur trade, treaties, the United Nations, Canadian agriculture regions, Canada and the United States, and peacekeeping.',
  [('Who leads the entire country of Canada?', ['prime minister']),
   ('What is an election?', ['an event where people vote to choose their leaders', 'people vote to choose leaders']),
   ('What is a treaty?', ['a formal agreement, often about sharing land and resources', 'a formal agreement'])],
  [('Who leads a province, such as Ontario?', ['The premier', 'The prime minister', 'The mayor', 'The governor'], 0),
   ('Which animal fur was especially important during the fur trade?', ['The beaver', 'The elephant', 'The lion', 'The kangaroo'], 0),
   ('What is the United Nations?', ['A group of many countries that work together to solve world problems', 'A single countrys government only', 'A type of sports league', 'A kind of school club'], 0),
   ('Which crop is commonly grown on the Canadian Prairies?', ['Wheat', 'Bananas', 'Pineapples', 'Coconuts'], 0),
   ('Which country shares a long border with Canada to the south?', ['The United States', 'Mexico', 'France', 'Brazil'], 0)])


g2_91_100 = [
    day(91, [d91_lang, d91_math, d91_sci, d91_ss]),
    day(92, [d92_lang, d92_math, d92_sci, d92_ss]),
    day(93, [d93_lang, d93_math, d93_sci, d93_ss]),
    day(94, [d94_lang, d94_math, d94_sci, d94_ss]),
    day(95, [d95_lang, d95_math, d95_sci, d95_ss]),
    day(96, [d96_lang, d96_math, d96_sci, d96_ss]),
    day(97, [d97_lang, d97_math, d97_sci, d97_ss]),
    day(98, [d98_lang, d98_math, d98_sci, d98_ss]),
    day(99, [d99_lang, d99_math, d99_sci, d99_ss]),
    day(100, [d100_lang, d100_math, d100_sci, d100_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_91_100)
    append_worksheet_days(2, g2_91_100)
