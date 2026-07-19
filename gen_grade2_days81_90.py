#!/usr/bin/env python3
"""Grade 2, Days 81-90 -- SIXTH batch, extending Grade 2 through Day 90.
Self-contained script modeled exactly on gen_grade2_days71_80.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-80 topics (see data/grade2.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely (or
rewritten without the apostrophe) to keep the generated .ts string
literals valid.
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


# ─── DAY 81 ─────────────────────────────────────────────────────────────────
d81_lang = sub('Language', 'Compound Sentences: Joining Ideas with Or and So',
  'Students learn that two related sentences can be joined into one compound sentence using the joining words or or so, such as combining You can walk and You can bike into You can walk or you can bike.',
  [('Name a joining word that can combine two sentences, like or or so.', ['or', 'so']),
   ('Join these ideas with so: It was raining. We stayed inside.', ['It was raining, so we stayed inside.', 'It was raining so we stayed inside']),
   ('Does joining two related sentences with or or so make one longer sentence?', ['yes'])],
  [('Which word can join two sentences to show a choice?', ['Or', 'The', 'A', 'An'], 0),
   ('Which word can join two sentences to show a result?', ['So', 'Or', 'The', 'A'], 0),
   ('Which sentence correctly joins two ideas with so?', ['It was cold, so I wore a coat.', 'It was cold I wore a coat so.', 'So cold it was, I wore a coat.', 'It was cold wore I a coat so.'], 0),
   ('Why might a writer combine two short sentences into one compound sentence?', ['It can make writing flow more smoothly', 'Combining sentences always makes writing confusing', 'Short sentences should never be combined', 'This concept has no connection to writing'], 0),
   ('Which sentence correctly joins two ideas with or?', ['You can have juice or you can have milk.', 'Juice milk or you can have you can have.', 'Or juice milk have can you.', 'You can have juice you can have milk or.'], 0)])

d81_math = sub('Math', 'Multiplication Facts: 6s and 7s',
  'Students practise and memorize multiplication facts for the 6 and 7 times tables, building on earlier work with the 2s, 3s, 4s, 5s, and 10s times tables.',
  [('What is 6 times 3?', ['18', 'eighteen']),
   ('What is 7 times 2?', ['14', 'fourteen']),
   ('What is 6 times 6?', ['36', 'thirty-six'])],
  [('What is 6 times 4?', ['24', '20', '28', '18'], 0),
   ('What is 7 times 3?', ['21', '18', '24', '14'], 0),
   ('What is 6 times 5?', ['30', '25', '35', '20'], 0),
   ('What is 7 times 5?', ['35', '30', '40', '25'], 0),
   ('What is 6 times 7?', ['42', '36', '48', '35'], 0)])

d81_sci = sub('Science', 'Our Skeleton and Joints: How We Bend and Move',
  'Students learn that our skeleton is made of bones that support our body, and that joints, such as our elbows and knees, are the places where two bones meet and allow us to bend and move.',
  [('What do we call the places where two bones meet and allow us to bend?', ['joints']),
   ('Name one joint in your body, like your elbow or knee.', ['elbow', 'knee']),
   ('Does our skeleton help support our whole body?', ['yes'])],
  [('What do we call the places where two bones meet?', ['Joints', 'Muscles', 'Veins', 'Nerves'], 0),
   ('Which of these is an example of a joint in the body?', ['The knee', 'The hair', 'The skin', 'The tongue'], 0),
   ('Why are joints important for how our body moves?', ['They allow our bones to bend at certain points', 'Joints have no connection to movement', 'Bones can bend anywhere without joints', 'Joints only exist to hold blood'], 0),
   ('What is our skeleton made of?', ['Bones', 'Only skin', 'Only muscle', 'Only blood'], 0),
   ('Our skeleton is best described as the structure that ___ our body.', ['Supports', 'Waters', 'Feeds', 'Colours'], 0)])

d81_ss = sub('SocialStudies', 'How Laws Are Made and Enforced',
  'Students learn that laws are made by elected governments to keep people safe and treated fairly, and that police and courts help make sure laws are followed and enforced.',
  [('Who helps make laws for a country or province?', ['government', 'elected government']),
   ('Name one group that helps make sure laws are followed, like police or courts.', ['police', 'courts']),
   ('Do laws help keep people safe and treated fairly?', ['yes'])],
  [('Who is responsible for making laws?', ['Elected governments', 'A single random citizen', 'No one at all', 'Only children'], 0),
   ('Which of these helps enforce laws in a community?', ['Police officers', 'Bakers', 'Farmers', 'Artists'], 0),
   ('Why are laws important for a community?', ['They help keep people safe and treated fairly', 'Laws have no real purpose', 'Laws only benefit one single person', 'Communities function better without any laws'], 0),
   ('What might happen if a community had no laws at all?', ['People could be treated unfairly or unsafely', 'Nothing would change at all', 'Communities always run better without laws', 'Laws have no connection to safety'], 0),
   ('Courts help make sure that laws are ___.', ['Followed fairly', 'Ignored completely', 'Never enforced', 'Written by only one person'], 0)])

# ─── DAY 82 ─────────────────────────────────────────────────────────────────
d82_lang = sub('Language', 'Figurative Language: Metaphors',
  'Students learn that a metaphor describes one thing by saying it is another thing, without using like or as, such as saying the classroom was a zoo to describe a noisy room.',
  [('Does a metaphor use the words like or as?', ['no']),
   ('What does the metaphor the classroom was a zoo suggest about the classroom?', ['it was noisy or chaotic', 'noisy']),
   ('Is the sentence Her smile was as bright as the sun a metaphor or a simile?', ['simile'])],
  [('What is a metaphor?', ['A comparison that says one thing is another thing', 'A comparison that always uses like or as', 'A sentence with no comparison at all', 'A type of punctuation mark'], 0),
   ('Which of these sentences is a metaphor?', ['The playground was a beehive of activity.', 'The playground was as busy as a beehive.', 'The playground had many students.', 'The playground was empty today.'], 0),
   ('What does the metaphor time is money suggest?', ['Time is valuable, like money', 'Time can be spent like real coins', 'Time has no value at all', 'Money and time have no connection'], 0),
   ('How is a metaphor different from a simile?', ['A metaphor does not use like or as, while a simile does', 'A metaphor and a simile are exactly the same thing', 'A metaphor always uses like or as', 'A simile never makes any comparison'], 0),
   ('Why might an author use a metaphor in their writing?', ['To create a vivid picture in the readers mind', 'Metaphors make writing less interesting', 'Metaphors have no purpose in writing', 'Metaphors are never used by authors'], 0)])

d82_math = sub('Math', 'Division Facts: Related to Multiplication',
  'Students learn that division facts are closely related to multiplication facts, such as knowing that if 6 times 4 equals 24, then 24 divided by 6 equals 4.',
  [('If 6 times 4 equals 24, what does 24 divided by 6 equal?', ['4', 'four']),
   ('If 5 times 3 equals 15, what does 15 divided by 5 equal?', ['3', 'three']),
   ('If 7 times 2 equals 14, what does 14 divided by 7 equal?', ['2', 'two'])],
  [('If 4 times 5 equals 20, what does 20 divided by 4 equal?', ['5', '4', '20', '10'], 0),
   ('If 3 times 6 equals 18, what does 18 divided by 3 equal?', ['6', '3', '18', '9'], 0),
   ('If 8 times 2 equals 16, what does 16 divided by 8 equal?', ['2', '8', '16', '4'], 0),
   ('Knowing multiplication facts can help us solve ___ facts.', ['Division', 'Addition', 'Subtraction', 'Only fraction'], 0),
   ('If 9 times 3 equals 27, what does 27 divided by 9 equal?', ['3', '9', '27', '6'], 0)])

d82_sci = sub('Science', 'Deserts: Life in a Dry Habitat',
  'Students learn that a desert is a very dry habitat that gets little rain, and that plants and animals living there, such as cacti and camels, have special features to survive with little water.',
  [('Is a desert habitat usually very dry or very wet?', ['very dry', 'dry']),
   ('Name one plant that can survive in a desert, like a cactus.', ['cactus']),
   ('Name one animal that can survive in a desert, like a camel.', ['camel'])],
  [('What kind of habitat is a desert?', ['A very dry habitat with little rain', 'A very wet habitat with lots of rain', 'A cold, icy habitat', 'An underwater habitat'], 0),
   ('Which plant is well known for surviving in the desert?', ['Cactus', 'Water lily', 'Seaweed', 'Fern'], 0),
   ('Which animal is well known for surviving in the desert?', ['Camel', 'Polar bear', 'Whale', 'Penguin'], 0),
   ('Why can cacti survive with very little water?', ['They can store water inside their thick stems', 'Cacti never need any water at all', 'Cacti absorb water only from the air', 'This concept has no connection to desert survival'], 0),
   ('A desert is best described as a habitat that is ___.', ['Dry with little rainfall', 'Wet with lots of rainfall', 'Frozen year-round', 'Underwater'], 0)])

d82_ss = sub('SocialStudies', 'Trade Between Countries: Imports and Exports',
  'Students learn that countries trade goods with each other, sending exports to other countries and receiving imports from other countries, so people can access products not made locally.',
  [('What do we call goods a country sends to another country?', ['exports']),
   ('What do we call goods a country receives from another country?', ['imports']),
   ('Does trade help countries access products not made locally?', ['yes'])],
  [('What are exports?', ['Goods a country sends to another country', 'Goods a country only keeps for itself', 'Money a country never uses', 'Goods a country never sells'], 0),
   ('What are imports?', ['Goods a country receives from another country', 'Goods a country only sends away', 'Money with no real value', 'Goods that are never traded'], 0),
   ('Why do countries trade goods with each other?', ['To access products that may not be made locally', 'Trade has no benefit to any country', 'Countries never need goods from elsewhere', 'This concept has no connection to daily life'], 0),
   ('If Canada sends maple syrup to another country, is that an import or an export for Canada?', ['An export', 'An import', 'Neither', 'Both at the same time'], 0),
   ('Trading goods between countries is an example of ___.', ['Working together to share resources', 'Countries refusing to work together', 'Ignoring other countries needs', 'Something that never actually happens'], 0)])

# ─── DAY 83 ─────────────────────────────────────────────────────────────────
d83_lang = sub('Language', 'Analogies: Comparing Word Relationships',
  'Students learn that an analogy compares two pairs of words that share a similar relationship, such as hot is to cold as up is to down, both showing opposite pairs.',
  [('In the analogy hot is to cold as up is to ___, what word completes the pattern?', ['down']),
   ('What kind of relationship do hot/cold and up/down share?', ['opposites', 'they are opposites']),
   ('Is an analogy a way of comparing word relationships?', ['yes'])],
  [('What is an analogy?', ['A comparison of two pairs of words that share a relationship', 'A word with no meaning at all', 'A single word with two meanings', 'A punctuation mark'], 0),
   ('Complete the analogy: bird is to nest as bee is to ___.', ['Hive', 'Web', 'Den', 'Burrow'], 0),
   ('Complete the analogy: finger is to hand as toe is to ___.', ['Foot', 'Arm', 'Ear', 'Head'], 0),
   ('What relationship do the words puppy and dog share in an analogy about baby animals and adult animals?', ['A puppy is a baby dog', 'A puppy is unrelated to a dog', 'A puppy is bigger than a dog', 'A puppy and dog are the same age'], 0),
   ('Solving analogies helps students understand ___.', ['How words and ideas relate to each other', 'Only how to spell words correctly', 'Only how to count numbers', 'Nothing useful about language'], 0)])

d83_math = sub('Math', 'Fact Family Triangles: Multiplication and Division',
  'Students learn to use a fact family triangle, showing three related numbers, to see how one multiplication fact and its related division facts connect, such as 3, 4, and 12.',
  [('In the fact family with 3, 4, and 12, what is 3 times 4?', ['12', 'twelve']),
   ('In the fact family with 3, 4, and 12, what is 12 divided by 4?', ['3', 'three']),
   ('In the fact family with 3, 4, and 12, what is 12 divided by 3?', ['4', 'four'])],
  [('In the fact family with 5, 6, and 30, what is 5 times 6?', ['30', '11', '25', '36'], 0),
   ('In the fact family with 5, 6, and 30, what is 30 divided by 5?', ['6', '5', '30', '25'], 0),
   ('In the fact family with 7, 8, and 56, what is 56 divided by 8?', ['7', '8', '56', '48'], 0),
   ('A fact family triangle shows how many related number facts?', ['Four', 'One', 'Two', 'Ten'], 0),
   ('A fact family triangle uses three numbers to show connected ___ and ___ facts.', ['Multiplication and division', 'Addition and subtraction', 'Fraction and decimal', 'Time and money'], 0)])

d83_sci = sub('Science', 'Rainforests: A Warm, Wet Habitat',
  'Students learn that a rainforest is a warm, wet habitat that gets a huge amount of rain each year, supporting a great variety of plants and animals such as monkeys, parrots, and frogs.',
  [('Is a rainforest habitat usually warm and wet or cold and dry?', ['warm and wet', 'warm, wet']),
   ('Name one animal that lives in the rainforest, like a monkey or parrot.', ['monkey', 'parrot', 'frog']),
   ('Do rainforests support a great variety of plants and animals?', ['yes'])],
  [('What kind of habitat is a rainforest?', ['A warm, wet habitat with lots of rain', 'A cold, icy habitat', 'A dry, sandy habitat', 'An underwater habitat only'], 0),
   ('Which animal is well known for living in the rainforest?', ['Monkey', 'Polar bear', 'Camel', 'Penguin'], 0),
   ('Why do rainforests support so many different plants and animals?', ['The warm, wet climate provides lots of food and shelter', 'Rainforests have no food or shelter at all', 'Rainforests are always frozen solid', 'Very few living things can survive there'], 0),
   ('Which of these is a feature of a rainforest?', ['Tall trees and lots of rainfall', 'Sand dunes with almost no rain', 'Ice covering the ground year-round', 'Deep ocean water covering the land'], 0),
   ('A rainforest is best described as a habitat with a huge amount of ___.', ['Rainfall', 'Snow', 'Sand', 'Ice'], 0)])

d83_ss = sub('SocialStudies', 'Canadian Confederation: How Canada Became a Country',
  'Students learn that Canadian Confederation was the joining together of separate colonies in 1867 to form the country of Canada, with its own government to make decisions.',
  [('In what year did Canadian Confederation happen?', ['1867']),
   ('What word describes separate colonies joining together to form one country?', ['confederation']),
   ('Did Canada gain its own government to make decisions after Confederation?', ['yes'])],
  [('What was Canadian Confederation?', ['Separate colonies joining together to form the country of Canada', 'A war between two countries', 'A single citys founding', 'A type of sporting event'], 0),
   ('In what year did Canadian Confederation take place?', ['1867', '1776', '1900', '1812'], 0),
   ('What happened to Canadas government after Confederation?', ['Canada gained its own government to make decisions', 'Canada lost its ability to make any decisions', 'No government existed after Confederation', 'Another country took over completely'], 0),
   ('Why is Confederation an important event in Canadian history?', ['It marks when Canada became its own country', 'It has no connection to Canadian history', 'It only affected one small town', 'It happened in a different country entirely'], 0),
   ('Confederation is best described as colonies joining to form ___.', ['One country', 'Two separate countries', 'No country at all', 'A single small city'], 0)])

# ─── DAY 84 ─────────────────────────────────────────────────────────────────
d84_lang = sub('Language', 'Proofreading Symbols: Marking Up Writing',
  'Students learn simple proofreading symbols, such as a caret to add a missing word or a line through a word to remove it, used to mark corrections in a piece of writing.',
  [('What symbol is often used to show a missing word should be added?', ['caret']),
   ('What can a line through a word show a writer should do?', ['remove it', 'delete it']),
   ('Do proofreading symbols help writers mark corrections in their writing?', ['yes'])],
  [('What is a proofreading symbol used for?', ['Marking corrections in a piece of writing', 'Drawing a picture on a page', 'Colouring in a word', 'Erasing an entire page'], 0),
   ('What does a caret symbol usually show in proofreading?', ['A missing word should be added there', 'A word should be made bigger', 'A word should be coloured', 'A sentence should be deleted entirely'], 0),
   ('What does drawing a line through a word usually mean?', ['The word should be removed', 'The word should be kept exactly as is', 'The word should be repeated twice', 'The word is spelled correctly'], 0),
   ('Why are proofreading symbols useful when editing writing?', ['They help writers quickly mark exact corrections', 'They make writing harder to understand', 'They have no real purpose in writing', 'They are only used for drawing pictures'], 0),
   ('Using proofreading symbols is part of the writing step called ___.', ['Editing', 'Drawing', 'Publishing only', 'Ignoring mistakes'], 0)])

d84_math = sub('Math', 'Measuring Angles: Right, Acute, and Obtuse',
  'Students learn to identify three kinds of angles: a right angle, which looks like the corner of a square, an acute angle, which is smaller than a right angle, and an obtuse angle, which is larger.',
  [('What kind of angle looks like the corner of a square?', ['right angle']),
   ('Is an acute angle smaller or larger than a right angle?', ['smaller']),
   ('Is an obtuse angle smaller or larger than a right angle?', ['larger'])],
  [('What is a right angle?', ['An angle that looks like the corner of a square', 'An angle that is always curved', 'An angle with no size at all', 'An angle only found in circles'], 0),
   ('Which of these describes an acute angle?', ['Smaller than a right angle', 'Larger than a right angle', 'Exactly equal to a right angle', 'The same as a straight line'], 0),
   ('Which of these describes an obtuse angle?', ['Larger than a right angle', 'Smaller than a right angle', 'Exactly equal to a right angle', 'The same as no angle at all'], 0),
   ('Which of these shapes has four right angles?', ['A square', 'A circle', 'A triangle with all different angles', 'A curved line'], 0),
   ('Learning to identify angles helps us describe ___.', ['The corners of shapes', 'The colour of shapes', 'The weight of shapes', 'The smell of shapes'], 0)])

d84_sci = sub('Science', 'Ocean Zones: Sunlight, Twilight, and Midnight',
  'Students learn that the ocean has different zones based on depth and light, with the sunlit zone near the top, the twilight zone getting dim light, and the dark midnight zone far below.',
  [('What do we call the top ocean zone that gets the most sunlight?', ['sunlit zone']),
   ('Does the twilight zone get bright sunlight or dim light?', ['dim light', 'dim']),
   ('Is the midnight zone bright or completely dark?', ['completely dark', 'dark'])],
  [('What is the sunlit zone of the ocean?', ['The top zone that gets the most sunlight', 'The deepest, darkest zone', 'A zone found only on land', 'A zone with no water at all'], 0),
   ('What is the twilight zone of the ocean?', ['A middle zone that gets only dim light', 'The top zone with bright sunlight', 'The very deepest, completely dark zone', 'A zone found only near the shore'], 0),
   ('What is the midnight zone of the ocean?', ['The deepest zone, which is completely dark', 'The top zone with the brightest sunlight', 'A zone found only near the surface', 'A zone that never has any water'], 0),
   ('Why does light decrease as you go deeper into the ocean?', ['Sunlight cannot travel very far through deep water', 'Sunlight always reaches every part of the ocean equally', 'The ocean has no connection to sunlight at all', 'Water makes light brighter the deeper you go'], 0),
   ('The three ocean zones are organized based on their depth and ___.', ['Amount of light', 'Amount of sand', 'Number of fish', 'Water temperature only'], 0)])

d84_ss = sub('SocialStudies', 'Non-Profit Organizations: Helping Communities in Need',
  'Students learn that a non-profit organization is a group that works to help people or causes, such as a food bank or animal shelter, using donations instead of trying to earn a profit.',
  [('What do we call a group that helps people or causes using donations?', ['non-profit organization', 'non-profit']),
   ('Name one example of a non-profit organization, like a food bank.', ['food bank', 'animal shelter']),
   ('Does a non-profit organization try to earn money for itself, or help others?', ['help others'])],
  [('What is a non-profit organization?', ['A group that uses donations to help people or causes', 'A store that only tries to earn money', 'A government building', 'A type of school subject'], 0),
   ('Which of these is an example of a non-profit organization?', ['A food bank', 'A grocery store', 'A toy factory', 'A car dealership'], 0),
   ('How does a non-profit organization usually get the resources it needs?', ['Through donations from people in the community', 'By selling products for the highest possible price', 'Non-profits never need any resources', 'By taking money from the government only'], 0),
   ('Why might a community value having a non-profit organization like a food bank?', ['It helps people in the community who need food', 'Food banks never actually help anyone', 'Non-profits have no connection to community needs', 'This concept has no relevance to social studies'], 0),
   ('Non-profit organizations are focused on helping others rather than ___.', ['Earning a profit for themselves', 'Serving their community', 'Collecting donations', 'Working together with volunteers'], 0)])

# ─── DAY 85 ─────────────────────────────────────────────────────────────────
d85_lang = sub('Language', 'Story Conflict: The Problem in a Story',
  'Students learn that most stories have a conflict, a problem the main character must face and try to solve, which often drives the events of the story forward.',
  [('What word describes the problem a main character must face in a story?', ['conflict']),
   ('Does a storys conflict often drive the events of the story forward?', ['yes']),
   ('If a character is lost in a forest and must find their way home, is that a story conflict?', ['yes'])],
  [('What is a story conflict?', ['The problem a main character must face and try to solve', 'The title of the book', 'The name of the illustrator', 'The colour of the book cover'], 0),
   ('Which of these is an example of a story conflict?', ['A character is lost and must find their way home', 'A character eats breakfast with no problems', 'A character has a calm, uneventful day', 'A character reads a book quietly'], 0),
   ('Why is conflict an important part of most stories?', ['It often drives the events of the story forward', 'Conflict has no connection to how a story unfolds', 'Stories are always better with no conflict at all', 'Conflict only appears in the very last page'], 0),
   ('At the end of a story, what usually happens to the conflict?', ['It is often solved or resolved', 'It always stays exactly the same', 'It disappears with no explanation at all', 'It has no ending at all'], 0),
   ('Recognizing a storys conflict helps readers understand ___.', ['What problem the character is trying to solve', 'Only the books price', 'Only the number of pages', 'Nothing about the story'], 0)])

d85_math = sub('Math', 'Data: Choosing the Best Graph to Show Information',
  'Students learn to think about which type of graph, such as a bar graph, pictograph, or line plot, best shows a certain kind of information clearly.',
  [('Which type of graph uses pictures to represent data?', ['pictograph']),
   ('Which type of graph uses bars to compare amounts?', ['bar graph']),
   ('Should the type of graph chosen depend on the kind of information being shown?', ['yes'])],
  [('Which graph type uses pictures to show data?', ['A pictograph', 'A bar graph', 'A line plot', 'A number line'], 0),
   ('Which graph type uses bars to compare different amounts?', ['A bar graph', 'A pictograph', 'A Venn diagram', 'A calendar'], 0),
   ('Why might someone choose a bar graph over a pictograph?', ['A bar graph can more precisely show exact amounts', 'Bar graphs are never useful for showing data', 'Pictographs always show more precise data', 'The type of graph never actually matters'], 0),
   ('If you wanted to show how many students chose each favourite colour, which graph could help?', ['A bar graph', 'A single number', 'A blank page', 'A calendar'], 0),
   ('Choosing the best graph for data helps information become ___.', ['Clearer and easier to understand', 'More confusing', 'Impossible to read', 'Completely hidden'], 0)])

d85_sci = sub('Science', 'Compound Machines: Combining Simple Machines',
  'Students learn that a compound machine is made by combining two or more simple machines, such as a wheelbarrow, which uses a wheel and axle together with a lever.',
  [('What do we call a machine made by combining two or more simple machines?', ['compound machine']),
   ('Name one example of a compound machine, like a wheelbarrow.', ['wheelbarrow']),
   ('Does a wheelbarrow combine a wheel and axle with a lever?', ['yes'])],
  [('What is a compound machine?', ['A machine made by combining two or more simple machines', 'A machine with only one single part', 'A machine that never actually works', 'A type of animal'], 0),
   ('Which of these is an example of a compound machine?', ['A wheelbarrow', 'A single nail', 'A plain rock', 'A single wheel with nothing else'], 0),
   ('Which simple machines combine to make a wheelbarrow work?', ['A wheel and axle with a lever', 'Only a single pulley', 'Only a single screw', 'A magnet and a spring'], 0),
   ('Why might combining simple machines create a more useful tool?', ['Combining them can make certain tasks even easier to do', 'Combining machines always makes tasks harder', 'Simple machines can never be combined', 'This concept has no connection to tools'], 0),
   ('A pair of scissors is a compound machine made of two combined ___.', ['Levers', 'Wheels', 'Pulleys', 'Screws'], 0)])

d85_ss = sub('SocialStudies', 'Natural Resources: What Canada Provides',
  'Students learn that Canada has many natural resources, such as forests, fresh water, and minerals, which provide materials that people use and that support many jobs.',
  [('What word describes materials from nature that people use, like forests or water?', ['natural resources']),
   ('Name one natural resource found in Canada, like forests or fresh water.', ['forests', 'fresh water', 'minerals']),
   ('Do natural resources support many jobs in Canada?', ['yes'])],
  [('What are natural resources?', ['Materials from nature that people use', 'Only objects made in a factory', 'Only items found in a store', 'Materials that do not exist in nature'], 0),
   ('Which of these is an example of a Canadian natural resource?', ['Forests', 'Plastic toys', 'Video games', 'Paved roads'], 0),
   ('How do natural resources support jobs in Canada?', ['Many people work in industries that use these resources', 'Natural resources have no connection to any jobs', 'No jobs exist because of natural resources', 'Natural resources only exist in other countries'], 0),
   ('Why is it important to use natural resources carefully?', ['So they remain available for the future', 'Careful use of resources has no benefit', 'Natural resources can never run out', 'This concept has no relevance to Canada'], 0),
   ('Natural resources like forests and fresh water come directly from ___.', ['Nature', 'Factories only', 'Stores only', 'Imagination only'], 0)])

# ─── DAY 86 ─────────────────────────────────────────────────────────────────
d86_lang = sub('Language', 'Word Endings: Adding -tion and -ness',
  'Students learn that adding -tion to some words can turn an action into a noun, like adding to inform to make information, and adding -ness can turn an adjective into a noun, like kind into kindness.',
  [('Add -ness to the word kind. What new word do you make?', ['kindness']),
   ('Add -tion to the word inform. What new word do you make?', ['information']),
   ('Does adding -ness to an adjective usually turn it into a noun?', ['yes'])],
  [('What does adding -ness to a word like kind create?', ['Kindness, a noun', 'Kindly, a different adjective', 'Kinding, a verb', 'No real word at all'], 0),
   ('What does adding -tion to a word like inform create?', ['Information, a noun', 'Informly, an adverb', 'Informed, a different verb form only', 'No real word at all'], 0),
   ('Which word means the state of being happy?', ['Happiness', 'Happily', 'Happier', 'Happied'], 0),
   ('Add -tion to the word educate. What new word do you make?', ['Education', 'Educative', 'Educated', 'Educately'], 0),
   ('Adding endings like -tion and -ness often changes a word into a ___.', ['Noun', 'Verb', 'Question', 'Number'], 0)])

d86_math = sub('Math', 'Money: Different Combinations for the Same Total',
  'Students practise finding different combinations of coins and bills that add up to the same total amount of money, such as making 50 cents using different sets of coins.',
  [('Name two different ways to make 10 cents using coins, like two nickels or ten pennies.', ['two nickels', 'ten pennies']),
   ('If a nickel is 5 cents, how many nickels make 25 cents?', ['5', 'five']),
   ('Can two different combinations of coins add up to the exact same total?', ['yes'])],
  [('Which combination of coins could make exactly 25 cents?', ['One quarter', 'Two dimes', 'One nickel', 'One penny'], 0),
   ('Which combination of coins could make exactly 15 cents?', ['One dime and one nickel', 'One quarter', 'Two pennies', 'One nickel only'], 0),
   ('If you have 3 dimes, how many cents do you have in total?', ['30', '10', '13', '3'], 0),
   ('Why might it be useful to know different ways to make the same total?', ['It helps when paying with the coins you actually have', 'There is never more than one way to make a total', 'Coins can only ever be combined in one way', 'This concept has no connection to money'], 0),
   ('Finding different coin combinations for the same total is an example of ___.', ['Flexible thinking with numbers', 'Ignoring numbers completely', 'ForgETting how coins work', 'Avoiding math altogether'], 0)])

d86_sci = sub('Science', 'The Rock Cycle: Igneous, Sedimentary, and Metamorphic',
  'Students learn that rocks can slowly change from one type to another over a very long time, forming igneous rock from cooled melted rock, sedimentary rock from layers of sediment, and metamorphic rock from heat and pressure.',
  [('Name one of the three main types of rock, like igneous, sedimentary, or metamorphic.', ['igneous', 'sedimentary', 'metamorphic']),
   ('Does igneous rock form from cooled melted rock?', ['yes']),
   ('Does sedimentary rock form from layers of sediment?', ['yes'])],
  [('What is igneous rock?', ['Rock formed from cooled melted rock', 'Rock formed only from sand blowing in wind', 'Rock formed only underwater', 'Rock that never actually forms'], 0),
   ('What is sedimentary rock?', ['Rock formed from layers of sediment', 'Rock formed only from lava', 'Rock formed only from ice', 'Rock that has no connection to layers'], 0),
   ('What is metamorphic rock?', ['Rock changed by heat and pressure', 'Rock that never changes at all', 'Rock formed only from wind', 'Rock found only in the ocean'], 0),
   ('Why is this process called a rock cycle?', ['Rocks can slowly change from one type into another over time', 'Rocks never change from one type to another', 'The rock cycle has no connection to time', 'Only one type of rock has ever existed'], 0),
   ('The rock cycle shows that rocks are always ___.', ['Slowly changing over long periods of time', 'Exactly the same forever', 'Disappearing completely with no trace', 'Unrelated to one another'], 0)])

d86_ss = sub('SocialStudies', 'Our Postal System: From Sender to Receiver',
  'Students learn the steps a letter or package takes through the postal system, from being dropped off, sorted at a postal facility, and delivered by a carrier to its receiver.',
  [('What do we call the system that collects, sorts, and delivers mail?', ['postal system']),
   ('Name one step a letter takes, like being sorted or delivered.', ['sorted', 'delivered']),
   ('Does a postal carrier help deliver mail to its receiver?', ['yes'])],
  [('What is the postal system?', ['The system that collects, sorts, and delivers mail', 'A system that only sells groceries', 'A system with no real purpose', 'A system that fights fires'], 0),
   ('Which of these is a step in how mail travels?', ['Being sorted at a postal facility', 'Being cooked in an oven', 'Being planted in a garden', 'Being sold at a store'], 0),
   ('Who helps deliver mail to its final receiver?', ['A postal carrier', 'A firefighter', 'A dentist', 'A farmer'], 0),
   ('Why is the postal system important for a community?', ['It helps people send and receive letters and packages', 'It has no connection to communication', 'Mail never actually needs to be delivered', 'This concept has no relevance to communities'], 0),
   ('The postal system connects a sender to a ___.', ['Receiver', 'Random stranger', 'Nobody at all', 'A completely different country only'], 0)])

# ─── DAY 87 ─────────────────────────────────────────────────────────────────
d87_lang = sub('Language', 'Formal and Informal Language: How We Talk in Different Places',
  'Students learn that formal language, used in places like a classroom presentation, is more polite and careful, while informal language, used with friends, is more relaxed and casual.',
  [('Would you use formal or informal language during a classroom presentation?', ['formal']),
   ('Would you use formal or informal language chatting with a close friend?', ['informal']),
   ('Is formal language usually more polite and careful than informal language?', ['yes'])],
  [('What is formal language?', ['Polite and careful language used in serious situations', 'Language only used with close friends', 'Language with no rules at all', 'A type of punctuation mark'], 0),
   ('What is informal language?', ['Relaxed, casual language used with friends', 'Language only used in a courtroom', 'Language that is always written, never spoken', 'A kind of math equation'], 0),
   ('Which situation calls for formal language?', ['Giving a presentation to the whole class', 'Chatting with a best friend at recess', 'Playing a game with a sibling', 'Joking around with a close friend'], 0),
   ('Which situation calls for informal language?', ['Talking with a close friend at recess', 'Presenting a report to the class', 'Speaking at a formal event', 'Writing a serious letter to a mayor'], 0),
   ('Choosing formal or informal language depends on ___.', ['The situation and who you are talking to', 'Nothing at all', 'Only the time of day', 'Only the weather outside'], 0)])

d87_math = sub('Math', 'Time: Converting Hours to Minutes',
  'Students learn that one hour is equal to 60 minutes, and practise converting between hours and minutes, such as figuring out that 2 hours equals 120 minutes.',
  [('How many minutes are in 1 hour?', ['60', 'sixty']),
   ('How many minutes are in 2 hours?', ['120', 'one hundred twenty']),
   ('How many minutes are in half an hour?', ['30', 'thirty'])],
  [('How many minutes are in 1 hour?', ['60', '100', '30', '12'], 0),
   ('How many minutes are in 3 hours?', ['180', '160', '190', '150'], 0),
   ('How many minutes are in half an hour?', ['30', '60', '15', '45'], 0),
   ('If an activity lasts 90 minutes, how many hours and minutes is that?', ['1 hour and 30 minutes', '2 hours', '90 hours', '1 hour and 90 minutes'], 0),
   ('Converting hours to minutes means multiplying the number of hours by ___.', ['60', '24', '30', '100'], 0)])

d87_sci = sub('Science', 'Our Immune System: Fighting Off Germs',
  'Students learn that our immune system is a team of body parts and cells that work together to fight off germs, helping us recover when we get sick.',
  [('What do we call the team of body parts and cells that fight off germs?', ['immune system']),
   ('Does our immune system help us recover when we get sick?', ['yes']),
   ('Can washing our hands help stop germs from making us sick?', ['yes'])],
  [('What is our immune system?', ['A team of body parts and cells that fight off germs', 'A single bone in our body', 'A type of food we eat', 'A part of our skeleton only'], 0),
   ('What does our immune system help us do?', ['Fight off germs and recover when we get sick', 'Grow taller every day', 'Taste our food better', 'See colours more clearly'], 0),
   ('Which of these helps support a healthy immune system?', ['Washing our hands and eating healthy food', 'Never washing our hands at all', 'Avoiding all healthy food', 'Ignoring germs completely'], 0),
   ('Why is it helpful to rest when we are sick?', ['Resting helps our immune system fight off germs', 'Resting has no connection to getting better', 'Our immune system never needs any help', 'Rest makes germs multiply faster'], 0),
   ('Our immune system is best described as our bodys ___.', ['Defense against germs', 'Only decoration', 'Least important system', 'System for tasting food'], 0)])

d87_ss = sub('SocialStudies', 'City Planning: Designing Where We Live',
  'Students learn that city planning involves deciding where to build homes, roads, parks, and schools, so that a community is organized and works well for the people who live there.',
  [('What do we call deciding where to build homes, roads, and parks in a community?', ['city planning']),
   ('Name one thing city planners might decide the location of, like a park or school.', ['park', 'school', 'road']),
   ('Does city planning help a community work well for the people who live there?', ['yes'])],
  [('What is city planning?', ['Deciding where to build homes, roads, parks, and schools', 'A rule about how to bake bread', 'A type of sport played outdoors', 'A story written by an author'], 0),
   ('Which of these might a city planner help decide?', ['Where a new park should be built', 'What a family should eat for dinner', 'What clothes a person should wear', 'What book a student should read'], 0),
   ('Why is city planning important for a community?', ['It helps organize a community so it works well for its people', 'City planning has no benefit to a community', 'Communities work better with absolutely no planning', 'This concept has no connection to daily life'], 0),
   ('If a city planner wants to reduce traffic near a school, what might they plan?', ['A safer road design near the school', 'A brand new ocean nearby', 'A taller building far away', 'Nothing at all needs to be planned'], 0),
   ('City planning helps make sure a community has enough ___.', ['Homes, roads, parks, and schools', 'Only homes and nothing else', 'Only roads and nothing else', 'No buildings of any kind'], 0)])

# ─── DAY 88 ─────────────────────────────────────────────────────────────────
d88_lang = sub('Language', 'Skimming and Scanning: Reading Strategies for Finding Information',
  'Students learn two reading strategies: skimming, which means quickly looking over a text to get its general idea, and scanning, which means quickly searching for a specific piece of information.',
  [('What reading strategy means quickly looking over a text to get its general idea?', ['skimming']),
   ('What reading strategy means quickly searching for one specific piece of information?', ['scanning']),
   ('Would scanning help you quickly find a specific date in a long article?', ['yes'])],
  [('What is skimming?', ['Quickly looking over a text to get its general idea', 'Reading every single word very slowly', 'Ignoring a text completely', 'Memorizing an entire book word for word'], 0),
   ('What is scanning?', ['Quickly searching for a specific piece of information', 'Reading a book from cover to cover slowly', 'Colouring in the pictures of a book', 'Writing a brand new story'], 0),
   ('Which strategy would help you quickly find a phone number in a long list?', ['Scanning', 'Skimming', 'Memorizing the entire list', 'Ignoring the list completely'], 0),
   ('Which strategy would help you get a general idea of what an article is about before reading it fully?', ['Skimming', 'Scanning', 'Skipping the article entirely', 'Reading only the very last word'], 0),
   ('Skimming and scanning are useful reading strategies because they help readers ___.', ['Find information quickly and efficiently', 'Avoid reading altogether', 'Forget the topic of a text', 'Make reading take much longer'], 0)])

d88_math = sub('Math', 'Patterns: Finding the Rule',
  'Students learn to look at a number pattern, such as 3, 6, 9, 12, and figure out the rule that explains how each number connects to the next, such as add 3 each time.',
  [('In the pattern 3, 6, 9, 12, what is the rule?', ['add 3', 'add 3 each time']),
   ('In the pattern 5, 10, 15, 20, what is the rule?', ['add 5', 'add 5 each time']),
   ('Using the rule add 3, what comes after 12 in the pattern 3, 6, 9, 12?', ['15', 'fifteen'])],
  [('What is the rule for the pattern 2, 4, 6, 8?', ['Add 2 each time', 'Add 4 each time', 'Subtract 2 each time', 'Multiply by 2 each time'], 0),
   ('What is the rule for the pattern 10, 20, 30, 40?', ['Add 10 each time', 'Add 5 each time', 'Subtract 10 each time', 'Multiply by 10 each time'], 0),
   ('Using the rule add 4, what comes after 16 in the pattern 4, 8, 12, 16?', ['20', '18', '22', '24'], 0),
   ('Finding the rule of a pattern helps us ___.', ['Predict what number comes next', 'Forget the whole pattern', 'Make the pattern completely random', 'Ignore the numbers entirely'], 0),
   ('What is the rule for the pattern 20, 17, 14, 11?', ['Subtract 3 each time', 'Add 3 each time', 'Subtract 7 each time', 'Add 7 each time'], 0)])

d88_sci = sub('Science', 'Chemical and Physical Changes: How Matter Can Change',
  'Students learn that a physical change, like tearing paper, changes how something looks without making a new substance, while a chemical change, like burning wood, creates a new substance entirely.',
  [('Does tearing a piece of paper create a new substance, or just change its shape?', ['just change its shape', 'change its shape']),
   ('Does burning wood create a new substance?', ['yes']),
   ('What kind of change creates a brand new substance?', ['chemical change'])],
  [('What is a physical change?', ['A change in how something looks, without creating a new substance', 'A change that always creates a brand new substance', 'A change that never actually happens', 'A change only found in outer space'], 0),
   ('What is a chemical change?', ['A change that creates a brand new substance', 'A change that never creates anything new', 'A change that only affects the colour of an object', 'A change that only happens to liquids'], 0),
   ('Which of these is an example of a physical change?', ['Tearing a piece of paper', 'Burning a piece of paper', 'Rusting metal', 'Baking a cake'], 0),
   ('Which of these is an example of a chemical change?', ['Burning wood', 'Folding paper', 'Cutting a piece of string', 'Bending a paperclip'], 0),
   ('Chemical changes are different from physical changes because they ___.', ['Create an entirely new substance', 'Never actually change anything', 'Only change the size of an object', 'Only happen once a year'], 0)])

d88_ss = sub('SocialStudies', 'Global Citizenship: Being a Responsible World Citizen',
  'Students learn that a global citizen thinks beyond their own community and considers how their actions, such as recycling or being kind to others, can affect people around the world.',
  [('What word describes someone who thinks about how their actions affect the whole world?', ['global citizen']),
   ('Name one action a global citizen might take, like recycling.', ['recycling', 'being kind to others']),
   ('Can our actions in our own community affect people in other parts of the world?', ['yes'])],
  [('What is a global citizen?', ['Someone who considers how their actions affect people around the world', 'Someone who only thinks about their own street', 'Someone who ignores every other country', 'A person with no connection to other people'], 0),
   ('Which of these is an action a responsible global citizen might take?', ['Recycling to help protect the environment', 'Wasting resources on purpose', 'Ignoring people in other countries completely', 'Refusing to help anyone at all'], 0),
   ('Why might recycling in your own community help the whole world?', ['Protecting the environment can benefit people everywhere', 'Recycling only ever affects one single street', 'Recycling has no connection to the environment', 'This concept has no relevance to global citizenship'], 0),
   ('How can being kind to newcomers show global citizenship?', ['It shows care for people no matter where they come from', 'Kindness has no connection to global citizenship', 'Global citizens should never be kind to newcomers', 'This concept only applies within one single country'], 0),
   ('Being a global citizen means caring about people ___.', ['Around the world, not just in your own community', 'Only in your own school', 'Only in your own house', 'Nowhere at all'], 0)])

# ─── DAY 89 ─────────────────────────────────────────────────────────────────
d89_lang = sub('Language', 'Writing a Book Review: Sharing Your Opinion of a Book',
  'Students learn to write a simple book review, sharing their opinion about a book they read, along with reasons for their opinion, such as liking the characters or the exciting plot.',
  [('What kind of writing shares your opinion about a book you read?', ['book review']),
   ('Should a book review include reasons that support your opinion?', ['yes']),
   ('Name one reason you might like a book, like exciting characters or an exciting plot.', ['exciting characters', 'exciting plot', 'interesting characters'])],
  [('What is a book review?', ['Writing that shares your opinion about a book, with reasons', 'A summary with no opinions at all', 'A list of every word in a book', 'A drawing of the book cover only'], 0),
   ('Why should a book review include reasons for your opinion?', ['It helps explain why you feel that way about the book', 'Reasons are never needed in a review', 'A review should never include any opinions', 'This concept has no connection to writing'], 0),
   ('Which of these is an example of a reason in a book review?', ['I liked how brave the main character was', 'The book has one hundred pages', 'The book was published last year', 'The book has a blue cover'], 0),
   ('A book review is different from a summary because a review also includes ___.', ['Your opinion and reasons', 'Only the exact same words from the book', 'Only the title of the book', 'Nothing extra at all'], 0),
   ('Writing a book review can help other readers decide whether to ___.', ['Read the book themselves', 'Never read any book again', 'Ignore the book completely', 'Avoid reading altogether'], 0)])

d89_math = sub('Math', 'Estimating Products: Rounding Before Multiplying',
  'Students learn to estimate the product of a multiplication problem by rounding one or both numbers to a friendly number first, making the multiplication easier to do quickly.',
  [('To estimate 6 times 9, what friendly number could 9 be rounded to?', ['10']),
   ('Using 6 times 10 as an estimate, what is a reasonable estimate for 6 times 9?', ['60', 'sixty']),
   ('Is an estimate an exact answer or an approximate answer?', ['approximate answer', 'approximate'])],
  [('To estimate 4 times 11, what friendly number could 11 be rounded to?', ['10', '11', '15', '20'], 0),
   ('Using 4 times 10 as an estimate, what is a reasonable estimate for 4 times 11?', ['40', '44', '400', '4'], 0),
   ('What is a reasonable estimate for 5 times 21?', ['About 100', 'About 10', 'About 1000', 'About 5'], 0),
   ('Why might someone estimate a product before finding the exact answer?', ['An estimate can help check whether the exact answer is reasonable', 'Estimating a product is never useful', 'An estimate is always exactly the same as the real answer', 'Estimating has no connection to multiplication'], 0),
   ('Estimating products is a useful skill because it can help us ___.', ['Solve problems more quickly and check our work', 'Make multiplication impossible to understand', 'Avoid learning multiplication facts', 'Replace the need for exact answers completely'], 0)])

d89_sci = sub('Science', 'Biomes of the World: Comparing Different Habitats',
  'Students learn that a biome is a large natural area with its own climate, plants, and animals, and that comparing biomes, like deserts, rainforests, and grasslands, shows how living things adapt to different conditions.',
  [('What word describes a large natural area with its own climate, plants, and animals?', ['biome']),
   ('Name one example of a biome, like a desert or rainforest.', ['desert', 'rainforest', 'grassland']),
   ('Do living things adapt differently depending on the biome they live in?', ['yes'])],
  [('What is a biome?', ['A large natural area with its own climate, plants, and animals', 'A single tree found in a forest', 'A type of ocean wave', 'A kind of rock formation only'], 0),
   ('Which of these is an example of a biome?', ['A rainforest', 'A single classroom', 'A grocery store', 'A birthday party'], 0),
   ('Why do animals in a desert biome look different from animals in an Arctic biome?', ['Each biome has different conditions that animals must adapt to', 'All biomes have the exact same conditions', 'Animals never adapt to their biome at all', 'This concept has no connection to biomes'], 0),
   ('Comparing different biomes helps scientists understand ___.', ['How living things adapt to different environments', 'Nothing useful about the natural world', 'Only how one single biome works', 'Only the weather in one single place'], 0),
   ('A biomes climate, plants, and animals are all closely ___.', ['Connected to each other', 'Completely unrelated', 'Chosen at random', 'Impossible to compare'], 0)])

d89_ss = sub('SocialStudies', 'Comparing Rural, Urban, and Suburban Jobs',
  'Students learn that the kinds of jobs people do can differ between rural areas, such as farming, urban areas, such as office work, and suburban areas, which often blend both kinds of jobs.',
  [('Name one job common in a rural area, like farming.', ['farming']),
   ('Name one job common in an urban area, like office work.', ['office work']),
   ('Do suburban areas often blend jobs from both rural and urban areas?', ['yes'])],
  [('Which job is most common in a rural area?', ['Farming', 'Office work in a skyscraper', 'Subway operator', 'Skyscraper construction'], 0),
   ('Which job is more common in a busy urban area?', ['Office work', 'Farming large fields', 'Fishing on a small lake', 'Herding livestock'], 0),
   ('Why might job types differ between rural and urban areas?', ['Each area has different land, resources, and population needs', 'Job types are always exactly the same everywhere', 'Rural and urban areas never have any differences', 'This concept has no connection to communities'], 0),
   ('What might make suburban jobs unique compared to rural or urban jobs?', ['They often blend features of both rural and urban work', 'Suburban areas never have any jobs at all', 'Suburban jobs are always identical to rural jobs', 'Suburban jobs have no connection to communities'], 0),
   ('Comparing jobs across rural, urban, and suburban areas helps us understand ___.', ['How communities and their needs can differ', 'That every community is exactly the same', 'That jobs never change based on location', 'That location has no effect on community life'], 0)])

# ─── DAY 90 (Review) ────────────────────────────────────────────────────────
d90_lang = sub('Language', 'Language Review: Sentences, Figurative Language, and Reading Strategies',
  'Students review recent Language skills: compound sentences, metaphors, analogies, proofreading symbols, story conflict, word endings, formal and informal language, skimming and scanning, and book reviews.',
  [('Which word can join two sentences to show a choice?', ['or']),
   ('What is a metaphor?', ['a comparison that says one thing is another thing', 'a comparison']),
   ('What is a story conflict?', ['the problem a main character must face and try to solve', 'a problem'])],
  [('Which word can join two sentences to show a result?', ['So', 'Or', 'The', 'A'], 0),
   ('Which of these sentences is a metaphor?', ['The playground was a beehive of activity.', 'The playground was as busy as a beehive.', 'The playground had many students.', 'The playground was empty today.'], 0),
   ('What does a caret symbol usually show in proofreading?', ['A missing word should be added there', 'A word should be made bigger', 'A word should be coloured', 'A sentence should be deleted entirely'], 0),
   ('Which situation calls for formal language?', ['Giving a presentation to the whole class', 'Chatting with a best friend at recess', 'Playing a game with a sibling', 'Joking around with a close friend'], 0),
   ('What is skimming?', ['Quickly looking over a text to get its general idea', 'Reading every single word very slowly', 'Ignoring a text completely', 'Memorizing an entire book word for word'], 0)])

d90_math = sub('Math', 'Math Review: Multiplication, Division, and Measurement',
  'Students review recent Math skills: multiplication facts for 6s and 7s, division facts, fact family triangles, measuring angles, choosing graphs, coin combinations, converting time, patterns, and estimating products.',
  [('What is 6 times 3?', ['18', 'eighteen']),
   ('If 6 times 4 equals 24, what does 24 divided by 6 equal?', ['4', 'four']),
   ('How many minutes are in 1 hour?', ['60', 'sixty'])],
  [('What is 7 times 3?', ['21', '18', '24', '14'], 0),
   ('In the fact family with 5, 6, and 30, what is 30 divided by 5?', ['6', '5', '30', '25'], 0),
   ('Which of these describes an acute angle?', ['Smaller than a right angle', 'Larger than a right angle', 'Exactly equal to a right angle', 'The same as a straight line'], 0),
   ('What is the rule for the pattern 2, 4, 6, 8?', ['Add 2 each time', 'Add 4 each time', 'Subtract 2 each time', 'Multiply by 2 each time'], 0),
   ('What is a reasonable estimate for 5 times 21?', ['About 100', 'About 10', 'About 1000', 'About 5'], 0)])

d90_sci = sub('Science', 'Science Review: Bodies, Habitats, and Matter',
  'Students review recent Science topics: our skeleton and joints, deserts, rainforests, ocean zones, compound machines, the rock cycle, our immune system, chemical and physical changes, and biomes.',
  [('What do we call the places where two bones meet?', ['joints']),
   ('What kind of habitat is a desert?', ['a very dry habitat with little rain', 'a dry habitat']),
   ('What is our immune system?', ['a team of body parts and cells that fight off germs', 'fights off germs'])],
  [('Which of these is an example of a joint in the body?', ['The knee', 'The hair', 'The skin', 'The tongue'], 0),
   ('Which animal is well known for living in the rainforest?', ['Monkey', 'Polar bear', 'Camel', 'Penguin'], 0),
   ('What is sedimentary rock?', ['Rock formed from layers of sediment', 'Rock formed only from lava', 'Rock formed only from ice', 'Rock that has no connection to layers'], 0),
   ('Which of these is an example of a chemical change?', ['Burning wood', 'Folding paper', 'Cutting a piece of string', 'Bending a paperclip'], 0),
   ('What is a biome?', ['A large natural area with its own climate, plants, and animals', 'A single tree found in a forest', 'A type of ocean wave', 'A kind of rock formation only'], 0)])

d90_ss = sub('SocialStudies', 'Social Studies Review: Laws, Trade, and Community Planning',
  'Students review recent Social Studies topics: how laws are made, trade between countries, Canadian Confederation, non-profit organizations, natural resources, our postal system, city planning, global citizenship, and comparing jobs.',
  [('Who is responsible for making laws?', ['elected governments', 'governments']),
   ('What was Canadian Confederation?', ['separate colonies joining together to form the country of Canada', 'colonies joining together']),
   ('What is a non-profit organization?', ['a group that uses donations to help people or causes', 'a group that helps people'])],
  [('What are exports?', ['Goods a country sends to another country', 'Goods a country only keeps for itself', 'Money a country never uses', 'Goods a country never sells'], 0),
   ('Which of these is an example of a Canadian natural resource?', ['Forests', 'Plastic toys', 'Video games', 'Paved roads'], 0),
   ('What is city planning?', ['Deciding where to build homes, roads, parks, and schools', 'A rule about how to bake bread', 'A type of sport played outdoors', 'A story written by an author'], 0),
   ('What is a global citizen?', ['Someone who considers how their actions affect people around the world', 'Someone who only thinks about their own street', 'Someone who ignores every other country', 'A person with no connection to other people'], 0),
   ('Which job is most common in a rural area?', ['Farming', 'Office work in a skyscraper', 'Subway operator', 'Skyscraper construction'], 0)])


g2_81_90 = [
    day(81, [d81_lang, d81_math, d81_sci, d81_ss]),
    day(82, [d82_lang, d82_math, d82_sci, d82_ss]),
    day(83, [d83_lang, d83_math, d83_sci, d83_ss]),
    day(84, [d84_lang, d84_math, d84_sci, d84_ss]),
    day(85, [d85_lang, d85_math, d85_sci, d85_ss]),
    day(86, [d86_lang, d86_math, d86_sci, d86_ss]),
    day(87, [d87_lang, d87_math, d87_sci, d87_ss]),
    day(88, [d88_lang, d88_math, d88_sci, d88_ss]),
    day(89, [d89_lang, d89_math, d89_sci, d89_ss]),
    day(90, [d90_lang, d90_math, d90_sci, d90_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_81_90)
    append_worksheet_days(2, g2_81_90)
