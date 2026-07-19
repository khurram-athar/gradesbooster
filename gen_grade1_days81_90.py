#!/usr/bin/env python3
"""Grade 1, Days 81-90 -- SIXTH batch, extending Grade 1 through Day 90.
Self-contained script modeled exactly on gen_grade1_days71_80.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 1 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 1 Days
1-80 topics (see data/grade1.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely to
keep the generated .ts string literals valid.
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
            ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{ti} grade 1 educational')
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


def _rebalance_answer_positions(days, seed=20260920):
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
d81_lang = sub('Language', 'Vowel Teams: oo in Book and Moon',
  'Students learn that the letters oo can make two different sounds, a short sound as in book and foot, and a long sound as in moon and spoon.',
  [('Does the oo in book make a short sound or a long sound?', ['short sound', 'short']),
   ('Does the oo in moon make a short sound or a long sound?', ['long sound', 'long']),
   ('Name one more word with the long oo sound, like moon or spoon.', ['moon', 'spoon', 'soon', 'zoo'])],
  [('Which word has the short oo sound, like in book?', ['Foot', 'Moon', 'Spoon', 'Zoo'], 0),
   ('Which word has the long oo sound, like in moon?', ['Spoon', 'Foot', 'Book', 'Wood'], 0),
   ('The letters oo can make how many different sounds?', ['Two', 'One', 'Three', 'Four'], 0),
   ('Which word has the same oo sound as book?', ['Good', 'Zoo', 'Food', 'Room'], 0),
   ('Knowing that oo can sound two different ways helps readers ___.', ['Try both sounds until a word makes sense', 'Always guess without trying either sound', 'Skip every word with oo in it', 'Only ever use the long sound'], 0)])

d81_math = sub('Math', 'Skip Counting by 8s and 9s',
  'Students practise skip counting forward by 8s and by 9s, extending earlier skip-counting work with smaller numbers to these larger jumps.',
  [('If you skip count by 8s starting at 8, what comes after 16?', ['24', 'twenty-four']),
   ('If you skip count by 9s starting at 9, what comes after 18?', ['27', 'twenty-seven']),
   ('What number comes right after 8 when skip counting by 8s?', ['16', 'sixteen'])],
  [('If you skip count by 8s, what comes after 8?', ['16', '9', '18', '10'], 0),
   ('If you skip count by 9s, what comes after 9?', ['18', '10', '19', '16'], 0),
   ('If you skip count by 8s starting at 8, what comes after 24?', ['32', '30', '28', '34'], 0),
   ('Skip counting by 9s means adding ___ each time.', ['9', '8', '10', '1'], 0),
   ('Which of these numbers would you say while skip counting by 8s?', ['32', '30', '34', '33'], 0)])

d81_sci = sub('Science', 'The Layers of Soil: What Is Underground',
  'Students learn that soil is made of different layers, with topsoil near the surface holding nutrients for plants, and deeper layers made mostly of rock and minerals.',
  [('What do we call the top layer of soil where plants get nutrients?', ['topsoil']),
   ('Is topsoil found near the surface or very deep underground?', ['near the surface', 'surface']),
   ('Do the deeper layers of soil contain mostly rock and minerals?', ['yes'])],
  [('What is topsoil?', ['The top layer of soil where plants get nutrients', 'A kind of cloud', 'A type of animal', 'A layer found only in the ocean'], 0),
   ('Where is topsoil usually found?', ['Near the surface of the ground', 'Deep in the ocean', 'High in the sky', 'Inside a volcano only'], 0),
   ('What are the deeper layers of soil mostly made of?', ['Rock and minerals', 'Clouds and rain', 'Leaves and branches only', 'Nothing at all'], 0),
   ('Why is topsoil important for plants?', ['It holds nutrients that plants need to grow', 'Topsoil has no connection to plants', 'Plants never need soil to grow', 'Topsoil removes nutrients from plants'], 0),
   ('Soil is best described as being made of ___.', ['Different layers', 'Only one single layer', 'Water only', 'Air only'], 0)])

d81_ss = sub('SocialStudies', 'Our Fire Department: Firefighters Keeping Us Safe',
  'Students learn about the fire department, a community building where firefighters work, train, and keep their trucks and equipment ready to respond to emergencies.',
  [('Where do firefighters work, train, and keep their trucks ready?', ['fire department', 'firehall']),
   ('Name one piece of equipment firefighters might use, like a hose or truck.', ['hose', 'truck', 'ladder']),
   ('Do firefighters help keep our community safe?', ['yes'])],
  [('What is a fire department?', ['A place where firefighters work and keep equipment ready', 'A place that sells bread', 'A place that delivers mail', 'A place with no purpose in a community'], 0),
   ('Which of these might you find at a fire department?', ['A fire truck', 'A cash register', 'A library book', 'A mailbox'], 0),
   ('Why do firefighters practise and train regularly?', ['So they are ready to respond quickly to emergencies', 'Training is not useful for firefighters', 'Firefighters never need to train', 'Practising has no connection to safety'], 0),
   ('How does a fire department help a community?', ['It keeps people safe by responding to fires and emergencies', 'It has no effect on community safety', 'It only sells baked goods', 'It only delivers packages'], 0),
   ('A fire department is an example of a place that provides ___ for a community.', ['Safety', 'Entertainment only', 'Groceries', 'Mail service'], 0)])

# ─── DAY 82 ─────────────────────────────────────────────────────────────────
d82_lang = sub('Language', 'Text Features: Titles, Headings, and Bold Words',
  'Students learn that non-fiction books often use text features, such as a title, headings, and bold words, to help readers find and understand important information.',
  [('What text feature usually appears at the very top of a book, naming what it is about?', ['title']),
   ('What text feature helps break a book into smaller sections with labels?', ['heading', 'headings']),
   ('Do bold words in a book often show an important word or idea?', ['yes'])],
  [('What is the title of a book?', ['The name that tells what the book is about', 'A picture on the last page', 'A list of every word in the book', 'The name of the reader'], 0),
   ('What do headings help readers do?', ['Find and understand different sections of a book', 'Skip the entire book', 'Colour in the pictures', 'Ignore the important information'], 0),
   ('Why might a word appear in bold print in a non-fiction book?', ['To show that it is an important word or idea', 'Bold print never has any meaning', 'It means the word should be skipped', 'It shows the word is a mistake'], 0),
   ('Which of these is a text feature found in non-fiction books?', ['A heading', 'A dragon', 'A fairy godmother', 'A talking animal'], 0),
   ('Text features like titles and headings help readers ___.', ['Find information more easily', 'Get confused more easily', 'Avoid reading altogether', 'Forget the topic of the book'], 0)])

d82_math = sub('Math', 'Numbers to 150: Reading Larger Numbers',
  'Students extend their number sense beyond 100, learning to read, write, and count numbers up to 150 using their knowledge of tens and ones.',
  [('What number comes right after 119?', ['120', 'one hundred twenty']),
   ('What number comes right after 149?', ['150', 'one hundred fifty']),
   ('Is 132 greater than or less than 123?', ['greater than', 'greater'])],
  [('What number comes right after 109?', ['110', '111', '100', '119'], 0),
   ('What number comes right after 139?', ['140', '141', '130', '149'], 0),
   ('Which number is greater, 145 or 154?', ['154', '145', 'They are equal', 'Cannot tell'], 0),
   ('The number 150 has how many tens?', ['15', '5', '1', '50'], 0),
   ('Reading numbers up to 150 builds on our understanding of ___.', ['Tens and ones', 'Only colours', 'Only shapes', 'Only time'], 0)])

d82_sci = sub('Science', 'Volcanoes: Mountains That Erupt',
  'Students learn that a volcano is a mountain with an opening that can erupt, sending hot melted rock called lava, ash, and gas up from deep inside the Earth.',
  [('What do we call a mountain with an opening that can erupt?', ['volcano']),
   ('What is the name for the hot melted rock that comes out of a volcano?', ['lava']),
   ('Does lava come from deep inside the Earth?', ['yes'])],
  [('What is a volcano?', ['A mountain with an opening that can erupt', 'A mountain made entirely of ice', 'A type of ocean animal', 'A kind of cloud'], 0),
   ('What is lava?', ['Hot melted rock that erupts from a volcano', 'Cold snow found on mountains', 'A kind of plant', 'A type of cloud'], 0),
   ('Where does lava come from?', ['Deep inside the Earth', 'High up in the sky', 'The bottom of the ocean only', 'Outer space'], 0),
   ('Besides lava, what else can a volcano send into the air?', ['Ash and gas', 'Only snow', 'Only rain', 'Only leaves'], 0),
   ('A volcano is best described as a mountain that can ___.', ['Erupt with lava, ash, and gas', 'Never change at all', 'Only produce snow', 'Float in the ocean'], 0)])

d82_ss = sub('SocialStudies', 'Recycling Centres: Where Our Bottles and Cans Go',
  'Students learn that a recycling centre is a place where materials like bottles, cans, and paper are collected and processed so they can be turned into new products.',
  [('What is a place called where bottles, cans, and paper are collected to be reused?', ['recycling centre']),
   ('Name one material that might be sent to a recycling centre, like a bottle.', ['bottle', 'can', 'paper']),
   ('Can recycled materials be turned into new products?', ['yes'])],
  [('What is a recycling centre?', ['A place where materials are collected to be turned into new products', 'A place that sells fresh bread', 'A place that delivers letters', 'A place that fights fires'], 0),
   ('Which of these materials might go to a recycling centre?', ['A glass bottle', 'A banana peel', 'A fallen leaf', 'A puddle of rainwater'], 0),
   ('What happens to materials after they are processed at a recycling centre?', ['They are turned into new products', 'They disappear completely', 'They are always destroyed', 'Nothing happens to them at all'], 0),
   ('Why is recycling helpful for our community and the Earth?', ['It reduces waste and reuses materials instead of throwing them away', 'Recycling creates more waste', 'Recycling harms the environment', 'Recycling has no real purpose'], 0),
   ('Sorting recyclable materials is an example of ___.', ['Caring for our environment', 'Ignoring our environment', 'Wasting valuable resources', 'Harming our community'], 0)])

# ─── DAY 83 ─────────────────────────────────────────────────────────────────
d83_lang = sub('Language', 'Story Mood: How a Story Makes Us Feel',
  'Students learn that a story can have a mood, or overall feeling, such as happy, scary, or calm, created by the words an author chooses and the events that happen.',
  [('What word describes the overall feeling a story gives its reader?', ['mood']),
   ('Would a story about a spooky, dark forest likely have a scary mood or a happy mood?', ['scary mood', 'scary']),
   ('Can the words an author chooses help create a storys mood?', ['yes'])],
  [('What is the mood of a story?', ['The overall feeling the story gives its reader', 'The name of the main character', 'The number of pages in the book', 'The colour of the book cover'], 0),
   ('Which of these words might describe a scary story mood?', ['Spooky', 'Cheerful', 'Sunny', 'Silly'], 0),
   ('How does an author often create a storys mood?', ['By choosing certain words and describing certain events', 'Mood has no connection to the words in a story', 'Authors never think about mood at all', 'Mood is only shown through pictures, never words'], 0),
   ('A story about a birthday party with balloons and cake most likely has a ___ mood.', ['Happy', 'Scary', 'Gloomy', 'Frightening'], 0),
   ('Recognizing a storys mood helps readers understand ___.', ['How the story is meant to feel', 'Only the page numbers', 'Only the authors name', 'Nothing about the story'], 0)])

d83_math = sub('Math', 'Fractions: Recognizing a Whole',
  'Students learn that a whole is one complete object or shape, and that understanding a whole helps them make sense of fractions like halves and quarters, which are parts of that whole.',
  [('What do we call one complete object or shape before it is divided?', ['whole', 'a whole']),
   ('If a pizza is cut into 4 equal slices, do all 4 slices together make one whole pizza?', ['yes']),
   ('Is a whole apple bigger or smaller than half an apple?', ['bigger'])],
  [('What is a whole?', ['One complete object or shape', 'Only half of an object', 'Only a quarter of an object', 'Nothing at all'], 0),
   ('If a sandwich is cut into 2 equal pieces, do both pieces together make one whole sandwich?', ['Yes', 'No', 'Only one piece is needed', 'Cannot tell'], 0),
   ('Which is larger, a whole orange or half of that same orange?', ['A whole orange', 'Half of the orange', 'They are the same size', 'Cannot tell'], 0),
   ('Understanding a whole helps us understand fractions because fractions describe ___.', ['Equal parts of a whole', 'Numbers with no connection to wholes', 'Only whole numbers', 'Shapes with no size at all'], 0),
   ('If you put all the equal slices of a cut pizza back together, what do you get?', ['The whole pizza', 'Half a pizza', 'No pizza at all', 'A different food entirely'], 0)])

d83_sci = sub('Science', 'Earthquakes: When the Ground Shakes',
  'Students learn that an earthquake happens when the ground suddenly shakes because of movement deep underground, and that scientists study earthquakes to help keep people safe.',
  [('What natural event happens when the ground suddenly shakes?', ['earthquake']),
   ('Does an earthquake happen because of movement deep underground?', ['yes']),
   ('Do scientists study earthquakes to help keep people safe?', ['yes'])],
  [('What is an earthquake?', ['A sudden shaking of the ground', 'A type of rainstorm', 'A kind of ocean wave only', 'A cloud formation'], 0),
   ('What causes an earthquake?', ['Movement deep underground', 'Movement of clouds in the sky', 'Animals running on the surface', 'Wind blowing very hard'], 0),
   ('Why do scientists study earthquakes?', ['To help keep people safe', 'Earthquakes are not worth studying', 'Studying earthquakes has no benefit', 'Scientists never study earthquakes'], 0),
   ('Which of these might happen during a strong earthquake?', ['Buildings and the ground can shake', 'The sky always turns bright green', 'Every ocean disappears', 'Nothing at all changes'], 0),
   ('Earthquakes are best described as sudden ___.', ['Shaking of the ground', 'Rainfall from clouds', 'Changes in ocean colour', 'Growth of new plants'], 0)])

d83_ss = sub('SocialStudies', 'City Hall: Where Local Leaders Work',
  'Students learn that city hall is a building where local leaders, such as a mayor and council members, work together to make decisions that help their town or city.',
  [('What do we call the building where local leaders work to help a town or city?', ['city hall']),
   ('Name one person who might work at city hall, like a mayor.', ['mayor', 'council member']),
   ('Do leaders at city hall make decisions that help their community?', ['yes'])],
  [('What is city hall?', ['A building where local leaders work to help their town or city', 'A place that sells groceries', 'A place that delivers mail', 'A place with no real purpose'], 0),
   ('Who might work at city hall?', ['A mayor and council members', 'Only firefighters', 'Only bakers', 'Only postal workers'], 0),
   ('What kind of decisions might leaders at city hall make?', ['Decisions that help the whole community', 'Decisions about only one persons house', 'No decisions of any kind', 'Decisions about outer space'], 0),
   ('Why is city hall an important building in a community?', ['It is where local leaders work to help the community', 'It has no real importance', 'It only stores old books', 'It is only used for baking'], 0),
   ('City hall helps a community in a similar way to how a principal helps a ___.', ['School', 'Ocean', 'Forest', 'Desert'], 0)])

# ─── DAY 84 ─────────────────────────────────────────────────────────────────
d84_lang = sub('Language', 'Word Endings: Adding -ful and -less',
  'Students learn that adding -ful to a word often means full of something, like helpful meaning full of help, while adding -less often means without something, like helpless meaning without help.',
  [('Add -ful to the word help. What new word do you make?', ['helpful']),
   ('Add -less to the word help. What new word do you make?', ['helpless']),
   ('Does the ending -ful usually mean full of something or without something?', ['full of something', 'full of']),
  ],
  [('What does adding -ful to a word usually mean?', ['Full of something', 'Without something', 'Before something', 'After something'], 0),
   ('What does adding -less to a word usually mean?', ['Without something', 'Full of something', 'Twice as much', 'Only a little'], 0),
   ('Which word means full of care?', ['Careful', 'Careless', 'Carer', 'Caring only'], 0),
   ('Which word means without care?', ['Careless', 'Careful', 'Carer', 'Caring only'], 0),
   ('Add -ful to the word joy. What new word do you make?', ['Joyful', 'Joyless', 'Joying', 'Joyed'], 0)])

d84_math = sub('Math', 'Measuring with Non-Standard Units: Paper Clips and Cubes',
  'Students practise measuring the length of objects using non-standard units, such as paper clips or connecting cubes, lining them up end to end and counting how many fit.',
  [('If a pencil is 6 paper clips long, how many paper clips did you count?', ['6', 'six']),
   ('When measuring with paper clips, should they be lined up end to end with no gaps?', ['yes']),
   ('If a book is longer than a pencil, will it need more or fewer paper clips to measure?', ['more'])],
  [('When measuring length with paper clips, how should they be placed?', ['End to end with no gaps', 'Scattered randomly', 'Stacked on top of each other', 'Placed far apart'], 0),
   ('If a crayon measures 4 cubes long and a marker measures 7 cubes long, which is longer?', ['The marker', 'The crayon', 'They are equal', 'Cannot tell'], 0),
   ('Why might two people get slightly different measurements using paper clips of different sizes?', ['Non-standard units like paper clips can vary in size', 'All paper clips are always the exact same size', 'Measuring length never gives different results', 'This concept has no connection to measurement'], 0),
   ('Which of these is an example of a non-standard unit of measurement?', ['A paper clip', 'A centimetre', 'A metre', 'A kilometre'], 0),
   ('Measuring with non-standard units like cubes helps us understand the idea of ___ before using rulers.', ['Length', 'Colour', 'Sound', 'Taste'], 0)])

d84_sci = sub('Science', 'Coral Reefs: Colourful Ocean Habitats',
  'Students learn that a coral reef is a colourful underwater habitat built by tiny living creatures called coral, providing a home for many different kinds of fish and sea animals.',
  [('What tiny living creatures build a coral reef?', ['coral']),
   ('Is a coral reef found on land or underwater?', ['underwater']),
   ('Do coral reefs provide a home for many fish and sea animals?', ['yes'])],
  [('What is a coral reef?', ['A colourful underwater habitat built by coral', 'A mountain found on land', 'A type of cloud', 'A kind of desert'], 0),
   ('What builds a coral reef?', ['Tiny living creatures called coral', 'Large rocks that fall from mountains', 'Trees growing underwater', 'Ice from the Arctic'], 0),
   ('Where is a coral reef found?', ['Underwater in the ocean', 'On top of a mountain', 'In a desert', 'In the sky'], 0),
   ('Why are coral reefs important to ocean life?', ['They provide a home for many different fish and sea animals', 'Coral reefs have no connection to ocean animals', 'No animals ever live near a coral reef', 'Coral reefs only exist on dry land'], 0),
   ('A coral reef is best described as a colourful ___.', ['Underwater habitat', 'Desert habitat', 'Mountain habitat', 'Cloud formation'], 0)])

d84_ss = sub('SocialStudies', 'Indigenous Traditions: Storytelling and the Land',
  'Students learn that Indigenous Peoples in Canada have long traditions of storytelling passed down through generations, along with deep knowledge and respect for the land.',
  [('What word describes stories passed down through generations?', ['storytelling', 'traditions']),
   ('Do Indigenous Peoples in Canada have deep knowledge and respect for the land?', ['yes']),
   ('Are storytelling traditions an important part of Indigenous cultures?', ['yes'])],
  [('What is storytelling?', ['Sharing stories, often passed down through generations', 'A type of building', 'A kind of food', 'A rule about traffic safety'], 0),
   ('What do storytelling traditions often help pass down?', ['Knowledge, history, and values', 'Nothing of importance', 'Only made-up nonsense', 'Rules about driving cars'], 0),
   ('How do many Indigenous cultures view the land?', ['With deep knowledge and respect', 'With no connection at all', 'As unimportant', 'As something to ignore completely'], 0),
   ('Why is it valuable to learn about Indigenous storytelling traditions?', ['It helps us understand and respect Indigenous history and culture', 'These traditions have no value to learn about', 'Storytelling has no connection to culture', 'This concept has no relevance to Canada'], 0),
   ('Indigenous Peoples have lived in Canada for a very long time, with traditions that connect them to ___.', ['The land and their communities', 'Nothing at all', 'Only modern cities', 'Only other countries'], 0)])

# ─── DAY 85 ─────────────────────────────────────────────────────────────────
d85_lang = sub('Language', 'Comparing Two Stories: How They Are Alike and Different',
  'Students learn to compare two stories by noticing how their characters, settings, or events are alike and different, often using a chart to organize their ideas.',
  [('What word describes noticing how two stories are alike and different?', ['comparing']),
   ('If two stories both have a brave main character, is that a similarity or a difference?', ['similarity']),
   ('Can a chart help organize how two stories are alike and different?', ['yes'])],
  [('What does it mean to compare two stories?', ['To notice how they are alike and different', 'To read only one story at a time', 'To ignore both stories completely', 'To copy one story exactly'], 0),
   ('If one story is set in a forest and another is set in a city, is that a similarity or a difference?', ['A difference', 'A similarity', 'Neither', 'Impossible to tell'], 0),
   ('What tool can help organize ideas when comparing two stories?', ['A chart', 'A paintbrush', 'A musical instrument', 'A cooking pan'], 0),
   ('Why is comparing two stories a useful reading skill?', ['It helps readers think more deeply about both stories', 'Comparing stories has no benefit at all', 'Readers should never think about more than one story', 'This concept has no connection to reading'], 0),
   ('When comparing stories, noticing that both have a happy ending is an example of a ___.', ['Similarity', 'Difference', 'Title', 'Cover'], 0)])

d85_math = sub('Math', 'Data: Venn Diagrams for Sorting into Two Groups',
  'Students learn to use a Venn diagram, two overlapping circles, to sort objects into two groups, showing what belongs only to one group, only to the other, or to both.',
  [('What do we call a diagram with two overlapping circles used for sorting?', ['Venn diagram']),
   ('In a Venn diagram, where would something go if it belongs to both groups?', ['the overlapping part', 'the middle', 'where the circles overlap']),
   ('Can a Venn diagram help us sort objects into two groups?', ['yes'])],
  [('What is a Venn diagram?', ['Two overlapping circles used to sort objects into groups', 'A single straight line', 'A list of random numbers', 'A picture with no purpose'], 0),
   ('In a Venn diagram, where does something go if it belongs to both groups?', ['In the overlapping part where the circles meet', 'Outside both circles', 'Only in the left circle', 'Only in the right circle'], 0),
   ('If sorting animals into a Venn diagram of Has Fur and Can Fly, where would a bat go?', ['In the overlapping part, since a bat has fur and can fly', 'Only in the Has Fur circle', 'Only in the Can Fly circle', 'Outside both circles'], 0),
   ('A Venn diagram helps us see which items belong to ___.', ['One group, the other group, or both groups', 'No group at all', 'Only the largest group', 'A completely random group'], 0),
   ('Sorting objects with a Venn diagram is a way of organizing ___.', ['Data', 'Music', 'Recipes', 'Weather'], 0)])

d85_sci = sub('Science', 'Hibernation: How Animals Sleep Through Winter',
  'Students learn that some animals, like bears, go into a deep sleep called hibernation during the cold winter months, using stored body fat for energy until spring arrives.',
  [('What do we call the deep sleep some animals go into during winter?', ['hibernation']),
   ('Name one animal that hibernates during winter, like a bear.', ['bear']),
   ('Do hibernating animals use stored body fat for energy?', ['yes'])],
  [('What is hibernation?', ['A deep sleep some animals go into during winter', 'A type of summer activity', 'A kind of food animals eat', 'A dance that animals perform'], 0),
   ('Which animal is well known for hibernating in winter?', ['A bear', 'A bird flying south', 'A fish swimming in the ocean', 'An insect that stays awake all winter'], 0),
   ('What do hibernating animals use for energy while they sleep?', ['Stored body fat', 'Fresh food they hunt every day', 'Sunlight only', 'Nothing at all'], 0),
   ('Why might hibernation help an animal survive winter?', ['Food can be scarce in winter, so sleeping saves energy', 'Hibernation has no benefit to survival', 'Animals hibernate only in the summer heat', 'Hibernating animals need more food than usual'], 0),
   ('Hibernation usually ends when which season arrives?', ['Spring', 'Winter', 'Autumn', 'It never ends'], 0)])

d85_ss = sub('SocialStudies', 'Our National Anthem: O Canada',
  'Students learn that O Canada is the national anthem, a special song sung to honour and celebrate the country of Canada, often heard at school and public events.',
  [('What do we call a special song that honours a country?', ['national anthem']),
   ('What is the name of Canadas national anthem?', ['O Canada']),
   ('Might we hear the national anthem sung at school or public events?', ['yes'])],
  [('What is a national anthem?', ['A special song that honours a country', 'A rule about traffic safety', 'A type of food', 'A kind of building'], 0),
   ('What is the name of Canadas national anthem?', ['O Canada', 'Happy Birthday', 'The Alphabet Song', 'Row Your Boat'], 0),
   ('Where might you hear the national anthem sung?', ['At school and public events', 'Only inside a grocery store', 'Only in a private home', 'Nowhere at all'], 0),
   ('Why do people sing the national anthem?', ['To honour and celebrate their country', 'Singing it has no meaning at all', 'It is only sung by mistake', 'It has nothing to do with Canada'], 0),
   ('O Canada is an example of a Canadian ___.', ['Symbol', 'Food', 'Animal', 'Landmark'], 0)])

# ─── DAY 86 ─────────────────────────────────────────────────────────────────
d86_lang = sub('Language', 'Giving an Opinion: I Think, I Believe',
  'Students learn to share an opinion, their own idea about something, using phrases like I think or I believe, and to give one reason that supports their opinion.',
  [('What word describes your own idea about something, like whether you liked a book?', ['opinion']),
   ('Name one phrase you could use to share an opinion, like I think or I believe.', ['I think', 'I believe']),
   ('Should you give a reason to support your opinion?', ['yes'])],
  [('What is an opinion?', ['Your own idea or feeling about something', 'A fact that is always true for everyone', 'A rule that everyone must follow', 'A number in a math problem'], 0),
   ('Which of these phrases could start an opinion?', ['I think', 'The sky is blue', 'Water is wet', 'Two plus two equals four'], 0),
   ('Why should you give a reason after sharing an opinion?', ['It helps explain why you feel that way', 'Reasons are never needed for opinions', 'Opinions never need any explanation', 'Giving a reason makes an opinion less clear'], 0),
   ('Which of these is an example of an opinion?', ['I believe dogs make the best pets', 'A dog has four legs', 'A dog is a kind of animal', 'Some dogs have fur'], 0),
   ('Sharing an opinion with a reason helps other people understand ___.', ['Why you feel the way you do', 'Nothing useful at all', 'Only facts, never feelings', 'A completely unrelated topic'], 0)])

d86_math = sub('Math', 'Addition: Making Ten to Add',
  'Students learn a mental math strategy called making ten, where they break apart one addend to complete a ten first, such as turning 8 plus 5 into 8 plus 2 plus 3.',
  [('To solve 8 plus 5 using making ten, what number completes 8 to make 10?', ['2', 'two']),
   ('After making 10 from 8 plus 2, how many are left over from the 5?', ['3', 'three']),
   ('What is 10 plus 3?', ['13', 'thirteen'])],
  [('To solve 9 plus 4 using making ten, what number completes 9 to make 10?', ['1', '4', '9', '0'], 0),
   ('After making 10 from 9 plus 1, how many are left over from the 4?', ['3', '4', '1', '0'], 0),
   ('What is 10 plus 3?', ['13', '10', '3', '14'], 0),
   ('The making ten strategy helps us add by first building a ___.', ['Ten', 'Hundred', 'One', 'Zero'], 0),
   ('Using making ten, what is 7 plus 5?', ['12', '11', '13', '10'], 0)])

d86_sci = sub('Science', 'The Northern Lights: Colourful Skies',
  'Students learn that the northern lights, also called the aurora, are colourful lights that sometimes glow and dance in the night sky, especially in places far to the north.',
  [('What do we call the colourful, dancing lights sometimes seen in the night sky?', ['northern lights', 'aurora']),
   ('Are the northern lights usually seen during the day or at night?', ['at night', 'night']),
   ('Are the northern lights more commonly seen in places far to the north?', ['yes'])],
  [('What are the northern lights?', ['Colourful lights that glow and dance in the night sky', 'Streetlights found in every city', 'A kind of daytime rainbow', 'Lights found only underwater'], 0),
   ('When are the northern lights usually seen?', ['At night', 'Only at noon', 'Only during a thunderstorm', 'Never at all'], 0),
   ('Where are the northern lights most commonly seen?', ['In places far to the north', 'Only near the equator', 'Only underwater', 'Only inside caves'], 0),
   ('Why might people travel far to see the northern lights?', ['They are a beautiful and rare natural sight', 'The northern lights are never worth seeing', 'They can be seen every night everywhere', 'They have no connection to the sky'], 0),
   ('The northern lights are also known by the name ___.', ['Aurora', 'Eclipse', 'Sunrise', 'Rainbow'], 0)])

d86_ss = sub('SocialStudies', 'Our Provincial Flag and Symbols',
  'Students learn that in addition to national symbols, each Canadian province has its own flag and symbols, such as a special flower or animal, that represent its identity.',
  [('Does each Canadian province have its own flag?', ['yes']),
   ('Name one kind of provincial symbol, like a flower or animal.', ['flower', 'animal']),
   ('Do provincial symbols help represent a provinces identity?', ['yes'])],
  [('Does each Canadian province have its own flag?', ['Yes', 'No', 'Only one province has a flag', 'Only cities have flags'], 0),
   ('Which of these could be a provincial symbol?', ['A special flower', 'A random number', 'A type of car', 'A cooking recipe'], 0),
   ('Why might a province choose a special flower or animal as a symbol?', ['To represent something unique about that provinces identity', 'Symbols have no connection to a provinces identity', 'Provinces are not allowed to have symbols', 'This concept has no relevance to Canada'], 0),
   ('How are provincial symbols similar to national symbols like the maple leaf?', ['Both represent identity and pride in a place', 'They have no similarities at all', 'National symbols are the only kind that exist', 'Provincial symbols always look identical to national ones'], 0),
   ('Learning about provincial symbols helps us understand that Canada is made up of ___.', ['Provinces with their own unique identities', 'Only one single identity', 'No provinces at all', 'Countries outside of Canada'], 0)])

# ─── DAY 87 ─────────────────────────────────────────────────────────────────
d87_lang = sub('Language', 'Reading with Expression: Using Our Voice When We Read',
  'Students practise reading aloud with expression, changing their voice to match the punctuation and feeling of a sentence, such as sounding excited for an exclamation mark.',
  [('Should your voice sound excited when reading a sentence that ends with an exclamation mark?', ['yes']),
   ('What word describes changing your voice to match a sentences feeling?', ['expression']),
   ('Should your voice go up at the end of a sentence that ends with a question mark?', ['yes'])],
  [('What does it mean to read with expression?', ['Changing your voice to match a sentences feeling', 'Reading every sentence in exactly the same flat voice', 'Skipping every punctuation mark', 'Reading as quietly as possible at all times'], 0),
   ('How might your voice sound when reading a sentence ending in an exclamation mark?', ['Excited', 'Completely silent', 'Confused', 'Sleepy'], 0),
   ('How might your voice change when reading a sentence ending in a question mark?', ['It might rise at the end, like asking a question', 'It should always get quieter', 'It should always stop completely', 'It never changes at all'], 0),
   ('Why is reading with expression helpful for listeners?', ['It helps bring the story to life and shows its feeling', 'Expression never affects how a story sounds', 'Listeners prefer a completely flat, emotionless voice', 'This concept has no connection to reading aloud'], 0),
   ('Reading with expression means paying attention to a sentences ___.', ['Punctuation and feeling', 'Page number only', 'Font colour only', 'Number of words only'], 0)])

d87_math = sub('Math', 'Subtraction: Counting Back Strategy',
  'Students learn the counting back strategy for subtraction, where they start at the larger number and count backward one at a time for each number being subtracted.',
  [('To solve 9 minus 3 using counting back, do you start at 9 and count backward or forward?', ['backward', 'count backward']),
   ('Counting back 3 from 9: 8, 7, 6. What is 9 minus 3?', ['6', 'six']),
   ('What is 7 minus 2 using counting back?', ['5', 'five'])],
  [('To solve 8 minus 2 using counting back, where do you start counting?', ['At 8, and count backward 2 times', 'At 2, and count forward', 'At 0', 'At 10'], 0),
   ('Counting back 2 from 8: 7, 6. What is 8 minus 2?', ['6', '7', '5', '8'], 0),
   ('What is 10 minus 3 using counting back?', ['7', '6', '8', '9'], 0),
   ('The counting back strategy works best for subtracting ___ numbers.', ['Small', 'Very large', 'Negative', 'Fraction'], 0),
   ('What is 6 minus 4 using counting back?', ['2', '3', '1', '4'], 0)])

d87_sci = sub('Science', 'Renewable and Non-Renewable Energy: Where Our Power Comes From',
  'Students learn that renewable energy, like sunlight and wind, can be used again and again, while non-renewable energy, like coal and oil, is limited and takes a very long time to form.',
  [('Can renewable energy, like sunlight, be used again and again?', ['yes']),
   ('Name one example of renewable energy, like sunlight or wind.', ['sunlight', 'wind', 'the sun']),
   ('Is non-renewable energy, like coal, limited or unlimited?', ['limited'])],
  [('What is renewable energy?', ['Energy that can be used again and again, like sunlight or wind', 'Energy that runs out after one single use', 'Energy that never exists at all', 'A kind of food'], 0),
   ('Which of these is an example of renewable energy?', ['Wind', 'Coal', 'Oil', 'Gasoline'], 0),
   ('Which of these is an example of non-renewable energy?', ['Coal', 'Sunlight', 'Wind', 'Water flowing in a river'], 0),
   ('Why is non-renewable energy considered limited?', ['It takes a very long time to form and can eventually run out', 'It can be remade instantly whenever needed', 'It never runs out under any circumstances', 'This concept has no connection to energy sources'], 0),
   ('Choosing renewable energy sources, like sunlight and wind, can help ___.', ['Protect our limited resources for the future', 'Use up all our resources faster', 'Harm the environment more than other choices', 'Has no real effect on the environment'], 0)])

d87_ss = sub('SocialStudies', 'Bake Sales and Fundraisers: Helping Our Community',
  'Students learn that a fundraiser, such as a bake sale, is an event where a community works together to raise money for a shared goal, like helping a local charity.',
  [('What do we call an event where people work together to raise money for a goal?', ['fundraiser']),
   ('Name one example of a fundraiser, like a bake sale.', ['bake sale']),
   ('Can money raised at a fundraiser help a local charity?', ['yes'])],
  [('What is a fundraiser?', ['An event where a community raises money for a shared goal', 'A store that sells only toys', 'A place that delivers mail', 'A rule about traffic safety'], 0),
   ('Which of these is an example of a fundraiser?', ['A bake sale', 'A grocery store', 'A dentist office', 'A fire hall'], 0),
   ('Why might a school or community hold a fundraiser?', ['To raise money to help a shared goal, like a local charity', 'Fundraisers never help anyone', 'Raising money is never a helpful goal', 'This concept has no connection to helping others'], 0),
   ('Which of these shows working together as a community?', ['Everyone baking treats for a bake sale', 'Everyone ignoring a shared goal', 'Refusing to help with a fundraiser', 'Working completely alone with no shared purpose'], 0),
   ('Fundraisers help teach us that communities can work together to ___.', ['Support a shared goal', 'Ignore people in need', 'Waste money for no reason', 'Avoid helping others'], 0)])

# ─── DAY 88 ─────────────────────────────────────────────────────────────────
d88_lang = sub('Language', 'Idioms: Sayings That Do Not Mean What They Say',
  'Students learn that an idiom is a saying whose words do not mean exactly what they say, such as it is raining cats and dogs, which really means it is raining very hard.',
  [('What do we call a saying whose words do not mean exactly what they say?', ['idiom']),
   ('Does the idiom raining cats and dogs really mean animals are falling from the sky?', ['no']),
   ('What does the idiom raining cats and dogs really mean?', ['it is raining very hard', 'raining hard'])],
  [('What is an idiom?', ['A saying whose words do not mean exactly what they say', 'A word that is spelled backward', 'A number used in math', 'A kind of punctuation mark'], 0),
   ('What does the idiom raining cats and dogs really mean?', ['It is raining very hard', 'Animals are falling from the sky', 'It is a sunny day', 'Cats and dogs are outside playing'], 0),
   ('If someone says break a leg before a play, what do they likely mean?', ['Good luck', 'Please hurt your leg', 'Stop performing immediately', 'Walk very slowly'], 0),
   ('Why can idioms be tricky for readers to understand?', ['Their words do not match their real meaning', 'Idioms always mean exactly what they say', 'Idioms are never used in everyday language', 'This concept has no connection to language'], 0),
   ('Learning idioms helps readers understand that language can have ___.', ['Meanings beyond the literal words', 'Only one possible meaning ever', 'No meaning at all', 'Meanings that never change'], 0)])

d88_math = sub('Math', 'Time: Elapsed Time and How Long Did It Take?',
  'Students learn to figure out elapsed time, or how much time has passed between a starting time and an ending time, such as finding how long an activity lasted.',
  [('What do we call the amount of time that passes between a start time and an end time?', ['elapsed time']),
   ('If an activity starts at 2 oclock and ends at 3 oclock, how much time has passed?', ['1 hour', 'one hour']),
   ('If an activity starts at 10 oclock and ends at 12 oclock, how many hours passed?', ['2', 'two'])],
  [('What is elapsed time?', ['The amount of time that passes between a start and end time', 'The exact time on a clock right now', 'A type of calendar', 'A kind of number pattern'], 0),
   ('If a movie starts at 4 oclock and ends at 6 oclock, how long is the movie?', ['2 hours', '1 hour', '3 hours', '4 hours'], 0),
   ('If recess starts at 10 oclock and ends at 10:30, how much time passed?', ['30 minutes', '1 hour', '15 minutes', '60 minutes'], 0),
   ('Finding elapsed time helps us answer questions like ___.', ['How long did an activity take?', 'What day of the week is it?', 'What colour is the clock?', 'How many clocks are in the room?'], 0),
   ('If school starts at 9 oclock and ends at 3 oclock, how many hours long is the school day?', ['6 hours', '5 hours', '7 hours', '3 hours'], 0)])

d88_sci = sub('Science', 'Our Lungs: Breathing In and Out',
  'Students learn that our lungs are two body parts inside our chest that help us breathe, taking in air when we inhale and pushing air out when we exhale.',
  [('What body part helps us breathe, taking in and pushing out air?', ['lungs']),
   ('Where are our lungs located?', ['chest', 'inside our chest']),
   ('Do our lungs take in air when we inhale?', ['yes'])],
  [('What body part helps us breathe?', ['Lungs', 'Elbow', 'Ear', 'Hair'], 0),
   ('Where are our lungs located?', ['Inside our chest', 'Inside our foot', 'Outside our body', 'Inside our hand'], 0),
   ('What happens to our lungs when we inhale?', ['They take in air', 'They shrink completely', 'They stop working', 'They push out all the air'], 0),
   ('What happens to our lungs when we exhale?', ['They push air out', 'They take in more air', 'They disappear', 'Nothing happens at all'], 0),
   ('Our lungs are best described as the body parts that help us ___.', ['Breathe', 'Taste food', 'Hear sounds', 'See colours'], 0)])

d88_ss = sub('SocialStudies', 'Weather Emergencies: Staying Safe in a Storm',
  'Students learn simple safety steps to follow during a weather emergency, such as a thunderstorm or snowstorm, like staying indoors and listening to a trusted adult.',
  [('Should we stay indoors during a strong thunderstorm?', ['yes']),
   ('Name one weather emergency, like a thunderstorm or snowstorm.', ['thunderstorm', 'snowstorm']),
   ('Should we listen to a trusted adult during a weather emergency?', ['yes'])],
  [('What should you do during a strong thunderstorm?', ['Stay indoors and listen to a trusted adult', 'Go outside and play', 'Stand under a tall tree', 'Ignore the storm completely'], 0),
   ('Which of these is an example of a weather emergency?', ['A snowstorm', 'A sunny afternoon', 'A calm evening', 'A light breeze'], 0),
   ('Why is it important to listen to a trusted adult during a weather emergency?', ['They can help keep you safe with the right instructions', 'Trusted adults never know how to help', 'Listening to adults is never necessary', 'This concept has no connection to safety'], 0),
   ('Which of these is a safe choice during a weather emergency?', ['Staying inside away from windows', 'Standing outside in the open', 'Ignoring any safety warnings', 'Wandering far from home alone'], 0),
   ('Knowing what to do during a weather emergency helps keep our community ___.', ['Safe', 'Confused', 'In danger', 'Unprepared'], 0)])

# ─── DAY 89 ─────────────────────────────────────────────────────────────────
d89_lang = sub('Language', 'Building Vocabulary: Learning New Words While Reading',
  'Students practise noticing new or unfamiliar words while reading, using pictures and nearby sentences to make a good guess about what the new word might mean.',
  [('What can help you guess the meaning of a new word while reading, like a picture?', ['picture', 'pictures']),
   ('Should you look at the sentences around a new word to help guess its meaning?', ['yes']),
   ('What do we call learning and collecting new words while reading?', ['building vocabulary', 'vocabulary'])],
  [('What can help you figure out a new words meaning while reading?', ['Pictures and nearby sentences', 'Ignoring the word completely', 'Closing the book immediately', 'Skipping to the very last page'], 0),
   ('Why is it helpful to notice new words while reading?', ['It helps build your vocabulary and understanding', 'Noticing new words is never helpful', 'New words should always be ignored', 'This concept has no connection to reading'], 0),
   ('If you see an unfamiliar word next to a picture of a large animal with a trunk, what might that word mean?', ['Elephant', 'Butterfly', 'Ladybug', 'Goldfish'], 0),
   ('Building vocabulary means growing your knowledge of ___.', ['Words and their meanings', 'Only numbers', 'Only shapes', 'Only colours'], 0),
   ('Which strategy helps most when you find a word you do not know?', ['Using clues from pictures and nearby sentences', 'Immediately stopping all reading forever', 'Ignoring the rest of the sentence', 'Guessing with no clues at all'], 0)])

d89_math = sub('Math', 'Money: Making Change from a Dollar',
  'Students learn how to figure out how much change they should receive back after paying with a dollar for something that costs less than a dollar.',
  [('If something costs 60 cents and you pay with a dollar, how much change should you get back?', ['40 cents', '40']),
   ('If something costs 25 cents and you pay with a dollar, how much change should you get back?', ['75 cents', '75']),
   ('A dollar is worth how many cents?', ['100', 'one hundred'])],
  [('If something costs 70 cents and you pay with a dollar, how much change should you get?', ['30 cents', '70 cents', '100 cents', '10 cents'], 0),
   ('If something costs 45 cents and you pay with a dollar, how much change should you get?', ['55 cents', '45 cents', '65 cents', '35 cents'], 0),
   ('A dollar is worth how many cents?', ['100', '10', '50', '1000'], 0),
   ('If something costs exactly one dollar, how much change should you get?', ['0 cents', '100 cents', '50 cents', '10 cents'], 0),
   ('Figuring out change helps us understand ___.', ['How to subtract the cost from the amount paid', 'How to multiply large numbers', 'How to tell time', 'How to measure length'], 0)])

d89_sci = sub('Science', 'Our Nose and Taste Buds: Smelling and Tasting Together',
  'Students learn that our sense of smell and sense of taste work closely together, and that our nose can help us notice flavours we might not fully taste with our tongue alone.',
  [('Name the two senses that work closely together to help us enjoy food.', ['smell and taste', 'smelling and tasting']),
   ('What body part helps us smell?', ['nose']),
   ('Can our nose help us notice flavours in food?', ['yes'])],
  [('Which two senses work closely together when we eat food?', ['Smell and taste', 'Sight and hearing', 'Touch and hearing', 'Sight and touch'], 0),
   ('What body part helps us smell?', ['Nose', 'Tongue', 'Ear', 'Elbow'], 0),
   ('Why might food taste different when your nose is blocked, like during a cold?', ['Smell helps us notice flavours, so a blocked nose can change how food tastes', 'Smell has no connection to how food tastes', 'A blocked nose never changes how food tastes', 'Taste and smell are never related at all'], 0),
   ('Which of these might our nose help us notice about food?', ['Its smell and some of its flavour', 'Its exact weight', 'Its exact price', 'Its shape only'], 0),
   ('Our sense of smell and sense of taste working together help us ___.', ['Fully enjoy the flavour of our food', 'Ignore our food completely', 'Only see our food, never taste it', 'Have no connection to eating at all'], 0)])

d89_ss = sub('SocialStudies', 'Being a Good Neighbour: Kindness Close to Home',
  'Students learn what it means to be a good neighbour, such as being friendly, respecting others property, and offering to help when someone nearby needs it.',
  [('What word describes someone who lives near you, like next door?', ['neighbour']),
   ('Name one way to be a good neighbour, like being friendly or helpful.', ['friendly', 'helpful']),
   ('Should we respect a neighbours property, like not stepping on their garden?', ['yes'])],
  [('What does it mean to be a good neighbour?', ['Being friendly, respectful, and helpful to people who live nearby', 'Ignoring everyone who lives nearby', 'Being unkind to people close to home', 'Never speaking to anyone in the neighbourhood'], 0),
   ('Which of these shows being a good neighbour?', ['Helping an elderly neighbour carry groceries', 'Damaging a neighbours garden on purpose', 'Ignoring a neighbour who waves hello', 'Making loud noise late at night on purpose'], 0),
   ('Why is respecting a neighbours property important?', ['It shows care and consideration for the people around us', 'Property never needs to be respected', 'Neighbours do not deserve any consideration', 'This concept has no connection to community life'], 0),
   ('How might being a good neighbour help build a stronger community?', ['It helps everyone feel safe, respected, and cared for', 'It has no effect on the community at all', 'Good neighbours make communities weaker', 'Kindness never affects a community'], 0),
   ('Being a good neighbour is an example of showing ___ close to home.', ['Kindness', 'Carelessness', 'Rudeness', 'Disrespect'], 0)])

# ─── DAY 90 (Review) ────────────────────────────────────────────────────────
d90_lang = sub('Language', 'Language Review: Vowel Teams, Text Features, and Word Meaning',
  'Students review recent Language skills: the oo vowel team, text features, story mood, word endings, comparing stories, giving opinions, reading with expression, idioms, and building vocabulary.',
  [('Does the oo in moon make a short sound or a long sound?', ['long sound', 'long']),
   ('What is the mood of a story?', ['the overall feeling the story gives its reader', 'overall feeling']),
   ('What do we call a saying whose words do not mean exactly what they say?', ['idiom'])],
  [('Which word has the long oo sound, like in moon?', ['Spoon', 'Foot', 'Book', 'Wood'], 0),
   ('What is the mood of a story?', ['The overall feeling the story gives its reader', 'The name of the main character', 'The number of pages in the book', 'The colour of the book cover'], 0),
   ('Which word means full of care?', ['Careful', 'Careless', 'Carer', 'Caring only'], 0),
   ('What does the idiom raining cats and dogs really mean?', ['It is raining very hard', 'Animals are falling from the sky', 'It is a sunny day', 'Cats and dogs are outside playing'], 0),
   ('What can help you figure out a new words meaning while reading?', ['Pictures and nearby sentences', 'Ignoring the word completely', 'Closing the book immediately', 'Skipping to the very last page'], 0)])

d90_math = sub('Math', 'Math Review: Numbers, Fractions, and Time',
  'Students review recent Math skills: skip counting by 8s and 9s, numbers to 150, recognizing a whole, non-standard measurement, Venn diagrams, making ten, counting back, elapsed time, and making change.',
  [('If you skip count by 8s, what comes after 8?', ['16', 'sixteen']),
   ('What number comes right after 119?', ['120', 'one hundred twenty']),
   ('A dollar is worth how many cents?', ['100', 'one hundred'])],
  [('If you skip count by 9s, what comes after 9?', ['18', '10', '19', '16'], 0),
   ('Which number is greater, 145 or 154?', ['154', '145', 'They are equal', 'Cannot tell'], 0),
   ('If a crayon measures 4 cubes long and a marker measures 7 cubes long, which is longer?', ['The marker', 'The crayon', 'They are equal', 'Cannot tell'], 0),
   ('What is 10 plus 3?', ['13', '10', '3', '14'], 0),
   ('If something costs 70 cents and you pay with a dollar, how much change should you get?', ['30 cents', '70 cents', '100 cents', '10 cents'], 0)])

d90_sci = sub('Science', 'Science Review: Earth, Habitats, and Our Bodies',
  'Students review recent Science topics: soil layers, volcanoes, earthquakes, coral reefs, hibernation, the northern lights, renewable energy, our lungs, and our nose and taste buds.',
  [('What is topsoil?', ['the top layer of soil where plants get nutrients', 'top layer of soil']),
   ('What is lava?', ['hot melted rock that erupts from a volcano', 'hot melted rock']),
   ('What body part helps us breathe?', ['lungs'])],
  [('What is an earthquake?', ['A sudden shaking of the ground', 'A type of rainstorm', 'A kind of ocean wave only', 'A cloud formation'], 0),
   ('What is a coral reef?', ['A colourful underwater habitat built by coral', 'A mountain found on land', 'A type of cloud', 'A kind of desert'], 0),
   ('What is hibernation?', ['A deep sleep some animals go into during winter', 'A type of summer activity', 'A kind of food animals eat', 'A dance that animals perform'], 0),
   ('What are the northern lights?', ['Colourful lights that glow and dance in the night sky', 'Streetlights found in every city', 'A kind of daytime rainbow', 'Lights found only underwater'], 0),
   ('Which two senses work closely together when we eat food?', ['Smell and taste', 'Sight and hearing', 'Touch and hearing', 'Sight and touch'], 0)])

d90_ss = sub('SocialStudies', 'Social Studies Review: Leaders, Traditions, and Community Care',
  'Students review recent Social Studies topics: fire departments, recycling centres, city hall, Indigenous traditions, our national anthem, provincial symbols, fundraisers, weather emergencies, and being a good neighbour.',
  [('What is a fire department?', ['a place where firefighters work and keep equipment ready', 'a place where firefighters work']),
   ('What is the name of Canadas national anthem?', ['O Canada']),
   ('What word describes someone who lives near you, like next door?', ['neighbour'])],
  [('What is city hall?', ['A building where local leaders work to help their town or city', 'A place that sells groceries', 'A place that delivers mail', 'A place with no real purpose'], 0),
   ('How do many Indigenous cultures view the land?', ['With deep knowledge and respect', 'With no connection at all', 'As unimportant', 'As something to ignore completely'], 0),
   ('What is a fundraiser?', ['An event where a community raises money for a shared goal', 'A store that sells only toys', 'A place that delivers mail', 'A rule about traffic safety'], 0),
   ('What should you do during a strong thunderstorm?', ['Stay indoors and listen to a trusted adult', 'Go outside and play', 'Stand under a tall tree', 'Ignore the storm completely'], 0),
   ('Which of these shows being a good neighbour?', ['Helping an elderly neighbour carry groceries', 'Damaging a neighbours garden on purpose', 'Ignoring a neighbour who waves hello', 'Making loud noise late at night on purpose'], 0)])


g1_81_90 = [
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
    _rebalance_answer_positions(g1_81_90)
    append_worksheet_days(1, g1_81_90)
