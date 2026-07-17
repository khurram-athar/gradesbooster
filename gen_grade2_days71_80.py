#!/usr/bin/env python3
"""Grade 2, Days 71-80 -- FIFTH and FINAL Grade 2 batch.
This is the LAST batch in the whole curriculum project: after this,
Grade 2 has Days 1-80 complete, and every grade from Kindergarten
through 12 has Days 1-80 complete.
Self-contained script modeled exactly on gen_grade2_days61_70.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} grade 2 educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 2 Days
1-70 topics (see data/grade2.ts). No embedded ASCII double-quote or
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


def _rebalance_answer_positions(days, seed=20260913):
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


# ─── DAY 71 ─────────────────────────────────────────────────────────────────
d71_lang = sub('Language', 'Similes: Comparing with Like and As',
  'Students learn that a simile is a figure of speech that compares two different things using the words like or as, helping readers picture an idea more clearly, such as as brave as a lion.',
  [('What do we call a phrase that compares two things using like or as?', ['a simile', 'simile']),
   ('Finish the simile: as quiet as a ___.', ['mouse', 'a mouse']),
   ('Which two words are most often used to signal a simile?', ['like and as', 'like, as'])],
  [('What do we call a phrase that compares two things using like or as?', ['A simile', 'A synonym', 'An antonym', 'A caption'], 0),
   ('Which sentence contains a simile?', ['The kitten was as fluffy as a cloud.', 'The kitten was fluffy.', 'The kitten sat down.', 'The kitten is small.'], 0),
   ('Finish the simile: as busy as a ___.', ['Bee', 'Rock', 'Chair', 'Cloud'], 0),
   ('Which word is most often used along with like to form a simile?', ['As', 'The', 'And', 'But'], 0),
   ('Writers use similes to ___.', ['Help readers picture an idea by comparing it to something familiar', 'Remove all description from writing', 'Make sentences shorter', 'Confuse the reader on purpose'], 0)])

d71_math = sub('Math', 'Three-Digit Addition with Regrouping',
  'Students learn to add two three-digit numbers that require regrouping, carrying a group of ten ones into the tens place or a group of ten tens into the hundreds place.',
  [('What is 236 + 148?', ['384']),
   ('What is 275 + 126?', ['401']),
   ('When do we regroup while adding, when a column adds to ten or more, or when it adds to less than ten?', ['ten or more', 'when a column adds to ten or more'])],
  [('What is 236 + 148?', ['384', '374', '394', '284'], 0),
   ('What is 275 + 126?', ['401', '391', '411', '301'], 0),
   ('What is 359 + 172?', ['531', '521', '541', '431'], 0),
   ('When adding two three-digit numbers, we regroup when a column adds up to ___.', ['Ten or more', 'Exactly one', 'Zero', 'Always, no matter what'], 0),
   ('What is 418 + 265?', ['683', '673', '693', '583'], 0)])

d71_sci = sub('Science', 'Parts of a Plant: Roots, Stem, Leaves, and Flower',
  'Students learn to identify the main parts of a plant, including the roots that absorb water, the stem that supports the plant, the leaves that capture sunlight, and the flower that helps make seeds.',
  [('Which part of a plant absorbs water from the soil?', ['the roots', 'roots']),
   ('Which part of a plant supports it and carries water upward?', ['the stem', 'stem']),
   ('Which part of a plant captures sunlight to make food?', ['the leaves', 'leaves'])],
  [('Which part of a plant absorbs water from the soil?', ['The roots', 'The stem', 'The leaves', 'The flower'], 0),
   ('Which part of a plant supports it and carries water upward?', ['The stem', 'The roots', 'The petals', 'The seeds'], 0),
   ('Which part of a plant captures sunlight to help make food?', ['The leaves', 'The roots', 'The stem', 'The seeds'], 0),
   ('Which part of a plant helps it make seeds?', ['The flower', 'The roots', 'The stem', 'The soil'], 0),
   ('Roots grow ___.', ['Underground to anchor the plant and absorb water', 'In the sky to catch sunlight', 'Only on the flower', 'Only in water, never in soil'], 0)])

d71_ss = sub('SocialStudies', 'Where Our Clothes and Toys Come From',
  'Students learn that many of the clothes and toys we use are made in factories, sometimes in other countries, using materials that started as raw resources like cotton or plastic.',
  [('Where are many clothes and toys made before they reach a store?', ['a factory', 'factory', 'factories']),
   ('Name one raw material that clothing can be made from, like cotton.', ['cotton', 'wool']),
   ('Are all the clothes and toys we use always made in the same country we live in?', ['no'])],
  [('Where are many clothes and toys made before they reach a store?', ['A factory', 'A farm only', 'A forest', 'A lake'], 0),
   ('Which of these is a raw material that clothing can be made from?', ['Cotton', 'Glass', 'Metal only', 'Water only'], 0),
   ('Are all the clothes and toys people use always made in the same country they live in?', ['No, many are made in other countries and shipped', 'Yes, always', 'Clothes are never made anywhere', 'Toys are never shipped anywhere'], 0),
   ('Why might a toy be made in one country and sold in another?', ['Companies often make products where it is efficient, then ship them to stores worldwide', 'Toys can only be sold in the country where they are made', 'Shipping does not exist', 'Toys are only made by hand at home'], 0),
   ('Learning where products come from helps us understand ___.', ['How different countries and communities are connected', 'That every product magically appears in stores', 'That factories do not exist', 'That all toys grow on trees'], 0)])

# ─── DAY 72 ─────────────────────────────────────────────────────────────────
d72_lang = sub('Language', 'Prepositions: Words That Show Where',
  'Students learn that a preposition is a word that shows the location or position of one thing in relation to another, such as in, on, under, and beside.',
  [('What do we call a word that shows the position of one thing compared to another, like under or beside?', ['a preposition', 'preposition']),
   ('Which preposition tells that the ball is inside the box?', ['in', 'in the box']),
   ('Name one preposition that tells where something is, such as under or beside.', ['under', 'beside', 'on', 'in', 'above', 'below'])],
  [('What do we call a word that shows the position of one thing compared to another?', ['A preposition', 'A verb', 'An adjective', 'A pronoun'], 0),
   ('Which sentence uses a preposition correctly to show location?', ['The cat is under the table.', 'The cat is table.', 'The cat under.', 'Table the cat is.'], 0),
   ('Which word is a preposition in the sentence: the book is on the shelf?', ['On', 'Book', 'Shelf', 'The'], 0),
   ('Which of these is an example of a preposition?', ['Beside', 'Quickly', 'Jumped', 'Happy'], 0),
   ('Prepositions help readers understand ___.', ['Where something is located', 'How a character feels', 'When a story ends', 'Who wrote the story'], 0)])

d72_math = sub('Math', 'Three-Digit Subtraction with Regrouping',
  'Students learn to subtract three-digit numbers that require regrouping, borrowing a group of ten from the tens place or hundreds place when a digit is too small to subtract from.',
  [('What is 342 - 158?', ['184']),
   ('What is 500 - 267?', ['233']),
   ('When subtracting, if the top digit is smaller than the bottom digit in a column, what do we do?', ['regroup', 'borrow from the next column', 'regroup from the next place value'])],
  [('What is 342 - 158?', ['184', '194', '174', '284'], 0),
   ('What is 500 - 267?', ['233', '243', '223', '333'], 0),
   ('What is 623 - 348?', ['275', '285', '265', '375'], 0),
   ('When the top digit in a column is smaller than the bottom digit, what do we do to subtract?', ['Regroup from the next place value', 'Add instead of subtract', 'Ignore that column', 'Skip the whole problem'], 0),
   ('What is 415 - 289?', ['126', '136', '116', '226'], 0)])

d72_sci = sub('Science', 'Levers: Lifting with Less Effort',
  'Students learn that a lever is a simple machine made of a bar that rests on a fixed point called a fulcrum, which helps lift or move heavy objects with less effort.',
  [('What do we call the fixed point that a lever rests on?', ['a fulcrum', 'fulcrum']),
   ('Name one tool that works as a lever, like a seesaw or a shovel.', ['a seesaw', 'seesaw', 'a shovel', 'shovel']),
   ('Does a lever make lifting a heavy object easier or harder?', ['easier'])],
  [('What do we call the fixed point that a lever rests on?', ['A fulcrum', 'An axle', 'A pulley', 'A wedge'], 0),
   ('Which of these tools is an example of a lever?', ['A seesaw', 'A magnet', 'A thermometer', 'A funnel'], 0),
   ('A lever is a type of ___.', ['Simple machine', 'Living thing', 'Weather pattern', 'Food group'], 0),
   ('Using a lever to lift a heavy rock makes the task ___.', ['Easier', 'Impossible', 'Slower and harder', 'Dangerous only'], 0),
   ('Which part of a lever stays still while the bar moves up and down?', ['The fulcrum', 'The handle', 'The load', 'The tip'], 0)])

d72_ss = sub('SocialStudies', 'Advertising: How Companies Try to Sell Us Things',
  'Students learn that advertisements are messages created by companies to convince people to buy a product, often using bright colours, catchy words, or famous characters to grab attention.',
  [('What do we call a message created by a company to convince people to buy a product?', ['an advertisement', 'advertisement', 'an ad']),
   ('Name one technique advertisements use to grab attention, like bright colours.', ['bright colours', 'catchy words', 'famous characters']),
   ('Why is it a good idea to think carefully before buying something you saw in an advertisement?', ['to make sure you really need it', 'to decide if it is a good choice', 'to avoid spending money on things you do not need'])],
  [('What do we call a message created by a company to convince people to buy a product?', ['An advertisement', 'A biography', 'A weather report', 'A map'], 0),
   ('Which of these is a technique advertisements often use to grab attention?', ['Bright colours and catchy words', 'Blank pages with no pictures', 'Silence and no sound at all', 'Tiny grey text no one can read'], 0),
   ('Why is it helpful to think carefully before buying something seen in an advertisement?', ['To decide if it is something you really need or want', 'Because advertisements are always true', 'Because advertisements never try to persuade anyone', 'To avoid ever buying anything at all'], 0),
   ('Where might a child see an advertisement?', ['On television, a website, or a billboard', 'Only inside a locked box', 'Only in outer space', 'Nowhere at all'], 0),
   ('Advertisements often try to ___.', ['Persuade people that they need or want a product', 'Teach a math lesson', 'Give a weather forecast', 'Explain a science experiment'], 0)])

# ─── DAY 73 ─────────────────────────────────────────────────────────────────
d73_lang = sub('Language', 'Interjections: Showing Strong Feelings',
  'Students learn that an interjection is a short word or phrase that expresses strong feeling, such as wow, oh no, or hooray, and is often followed by an exclamation mark.',
  [('What do we call a short word that expresses strong feeling, like wow?', ['an interjection', 'interjection']),
   ('What punctuation mark often follows an interjection?', ['an exclamation mark', 'exclamation mark', 'exclamation point']),
   ('Give one example of an interjection that shows excitement.', ['wow', 'hooray', 'yay', 'oh no', 'ouch'])],
  [('What do we call a short word or phrase that expresses strong feeling?', ['An interjection', 'A preposition', 'A synonym', 'A pronoun'], 0),
   ('Which of these is an example of an interjection?', ['Hooray', 'Table', 'Under', 'Quietly'], 0),
   ('What punctuation mark most often follows an interjection?', ['An exclamation mark', 'A question mark', 'A comma', 'A period'], 0),
   ('Which sentence begins with an interjection?', ['Wow, that is a huge dinosaur!', 'That is a huge dinosaur.', 'A huge dinosaur is here.', 'Is that a huge dinosaur?'], 0),
   ('Interjections are used in writing to ___.', ['Show strong feelings like surprise or excitement', 'Show the location of an object', 'Name a person or place', 'Connect two sentences together'], 0)])

d73_math = sub('Math', 'Multiplication Facts: 3s and 4s',
  'Students learn and practice basic multiplication facts for the 3 times table and 4 times table, such as 3 times 4 equals 12.',
  [('What is 3 times 4?', ['12']),
   ('What is 4 times 5?', ['20']),
   ('What is 3 times 6?', ['18'])],
  [('What is 3 times 4?', ['12', '10', '14', '16'], 0),
   ('What is 4 times 5?', ['20', '16', '24', '18'], 0),
   ('What is 3 times 6?', ['18', '15', '21', '12'], 0),
   ('What is 4 times 4?', ['16', '12', '20', '14'], 0),
   ('What is 3 times 7?', ['21', '18', '24', '20'], 0)])

d73_sci = sub('Science', 'The Heart: Pumping Blood Through Our Body',
  'Students learn that the heart is a muscle that pumps blood through the body, delivering oxygen and nutrients to every part, and that exercise helps keep the heart strong.',
  [('What organ pumps blood through the body?', ['the heart', 'heart']),
   ('What does blood deliver to every part of the body?', ['oxygen and nutrients', 'oxygen', 'nutrients']),
   ('Name one activity that helps keep the heart strong, like exercise.', ['exercise', 'running', 'playing sports', 'being active'])],
  [('What organ pumps blood through the body?', ['The heart', 'The lungs', 'The stomach', 'The brain'], 0),
   ('What does blood deliver to every part of the body?', ['Oxygen and nutrients', 'Only water', 'Only air', 'Only sound'], 0),
   ('Which of these activities helps keep the heart strong?', ['Regular exercise', 'Sitting still all day', 'Skipping meals', 'Avoiding all movement'], 0),
   ('The heart is made mostly of ___.', ['Muscle', 'Bone', 'Skin', 'Hair'], 0),
   ('Why is the heart an important organ?', ['It pumps blood that carries oxygen through the body', 'It helps us see', 'It helps us hear', 'It helps us smell'], 0)])

d73_ss = sub('SocialStudies', 'Levels of Government: Town, Province, and Country',
  'Students learn that Canada has three levels of government, municipal government that looks after a town or city, provincial government that looks after a province, and federal government that looks after the whole country.',
  [('What do we call the level of government that looks after a town or city?', ['municipal government', 'municipal']),
   ('What do we call the level of government that looks after the whole country?', ['federal government', 'federal']),
   ('Name one thing a provincial government might be responsible for, like schools or highways.', ['schools', 'highways', 'hospitals'])],
  [('What do we call the level of government that looks after a town or city?', ['Municipal government', 'Federal government', 'Provincial government', 'No government'], 0),
   ('What do we call the level of government that looks after the whole country?', ['Federal government', 'Municipal government', 'Provincial government', 'Town council only'], 0),
   ('Which level of government looks after an entire province, like Ontario?', ['Provincial government', 'Municipal government', 'Federal government', 'School government'], 0),
   ('Which of these is usually a responsibility of a municipal government?', ['Local roads and garbage collection', 'The entire national defence', 'Choosing the countrywide currency', 'Setting the whole country border'], 0),
   ('Canada has how many main levels of government?', ['Three', 'One', 'Five', 'Ten'], 0)])

# ─── DAY 74 ─────────────────────────────────────────────────────────────────
d74_lang = sub('Language', 'Persuasive Writing: Convincing Your Reader',
  'Students learn that persuasive writing tries to convince a reader to agree with an idea or take an action by giving strong reasons and using words like should or must.',
  [('What is the goal of persuasive writing?', ['to convince the reader', 'convince the reader', 'to persuade the reader']),
   ('Name one word often used in persuasive writing, like should or must.', ['should', 'must']),
   ('What should a persuasive writer give to support an idea?', ['strong reasons', 'reasons', 'a reason'])],
  [('What is the main goal of persuasive writing?', ['To convince the reader to agree with an idea', 'To describe a setting only', 'To tell what time it is', 'To list random facts'], 0),
   ('Which sentence is an example of persuasive writing?', ['You should recycle to help protect the earth.', 'The earth is a planet.', 'Recycling bins are blue.', 'Paper comes from trees.'], 0),
   ('Which word is commonly used in persuasive writing to urge the reader to act?', ['Should', 'Was', 'Has', 'The'], 0),
   ('A strong piece of persuasive writing includes ___.', ['Clear reasons that support the opinion of the writer', 'Random unrelated facts', 'No opinion at all', 'Only questions and no reasons'], 0),
   ('Why might a student write a persuasive letter to their school?', ['To convince the school to make a positive change', 'To describe the weather', 'To retell a story', 'To list the alphabet'], 0)])

d74_math = sub('Math', 'Fractions of a Group: Sharing a Set of Objects',
  'Students learn to find a fraction of a group of objects, such as finding one half of a group of 8 apples by splitting the group into two equal parts.',
  [('What is one half of a group of 8 apples?', ['4']),
   ('What is one quarter of a group of 12 stickers?', ['3']),
   ('If a group of 6 balloons is split into two equal parts, how many balloons are in each part?', ['3'])],
  [('What is one half of a group of 8 apples?', ['4', '2', '6', '8'], 0),
   ('What is one quarter of a group of 12 stickers?', ['3', '4', '6', '2'], 0),
   ('If a group of 6 balloons is split into two equal parts, how many balloons are in each part?', ['3', '2', '4', '6'], 0),
   ('What is one third of a group of 9 marbles?', ['3', '2', '4', '9'], 0),
   ('To find a fraction of a group, we ___.', ['Split the group into equal parts', 'Multiply the group by ten', 'Add one to the group', 'Ignore the group size'], 0)])

d74_sci = sub('Science', 'How Our Body Digests Food',
  'Students learn that digestion is the process the body uses to break down food into nutrients, starting in the mouth and continuing through the stomach and intestines.',
  [('What do we call the process the body uses to break down food?', ['digestion']),
   ('Where does digestion begin?', ['the mouth', 'mouth']),
   ('Name one organ that helps digest food, like the stomach.', ['the stomach', 'stomach', 'the intestines', 'intestines'])],
  [('What do we call the process the body uses to break down food?', ['Digestion', 'Respiration', 'Circulation', 'Reflection'], 0),
   ('Where does digestion of food begin?', ['The mouth', 'The stomach', 'The intestines', 'The lungs'], 0),
   ('Which organ helps break down food after it leaves the mouth?', ['The stomach', 'The heart', 'The lungs', 'The brain'], 0),
   ('Why does our body need to digest food?', ['To break it down into nutrients the body can use', 'To make food disappear completely', 'To change food into water', 'To stop the body from growing'], 0),
   ('After food leaves the stomach, where does it travel next?', ['The intestines', 'The lungs', 'The heart', 'The brain'], 0)])

d74_ss = sub('SocialStudies', 'Canadian Holidays: Canada Day and Remembrance Day',
  'Students learn about two important Canadian holidays: Canada Day on July 1st, which celebrates the birthday of Canada, and Remembrance Day on November 11th, when Canadians honour those who served in the armed forces.',
  [('On what date is Canada Day celebrated?', ['july 1', 'july 1st']),
   ('On what date is Remembrance Day observed?', ['november 11', 'november 11th']),
   ('What symbol do Canadians often wear in November to honour those who served?', ['a poppy', 'poppy'])],
  [('On what date is Canada Day celebrated?', ['July 1st', 'December 25th', 'November 11th', 'January 1st'], 0),
   ('On what date is Remembrance Day observed?', ['November 11th', 'July 1st', 'October 31st', 'September 1st'], 0),
   ('What does Canada Day celebrate?', ['The birthday of Canada', 'The end of winter', 'A famous hockey game', 'The start of school'], 0),
   ('What symbol do many Canadians wear in November to honour those who served?', ['A poppy', 'A maple leaf pin', 'A snowflake', 'A flag pin'], 0),
   ('Why do communities across Canada hold ceremonies on Remembrance Day?', ['To honour and remember those who served the country', 'To celebrate a hockey championship', 'To welcome the new school year', 'To celebrate a harvest festival'], 0)])

# ─── DAY 75 ─────────────────────────────────────────────────────────────────
d75_lang = sub('Language', 'Nonfiction Text Features: Diagrams and Labels',
  'Students learn that nonfiction books often include diagrams and labels, which are pictures with words pointing to specific parts, to help readers understand information more clearly.',
  [('What do we call a picture with labels pointing to specific parts?', ['a diagram', 'diagram']),
   ('What do we call the words that point to and name parts of a diagram?', ['labels', 'a label']),
   ('Why do nonfiction books use diagrams and labels?', ['to help readers understand information', 'to explain information clearly', 'to show information visually'])],
  [('What do we call a picture with labels pointing to specific parts?', ['A diagram', 'A caption', 'A heading', 'A glossary'], 0),
   ('What do we call the words that point to and name parts of a diagram?', ['Labels', 'Chapters', 'Titles', 'Rhymes'], 0),
   ('Why do nonfiction books often include diagrams?', ['To help readers understand information more clearly', 'To make the book longer', 'To confuse the reader', 'To replace all the words in a book'], 0),
   ('Which of these would most likely include a labelled diagram?', ['A nonfiction book about the parts of a plant', 'A poem about the moon', 'A fairy tale about a dragon', 'A birthday card'], 0),
   ('A label on a diagram usually points to ___.', ['A specific part being named', 'A random unrelated word', 'The title of the book', 'The page number'], 0)])

d75_math = sub('Math', 'Comparing Fractions: Which Is Greater',
  'Students learn to compare simple fractions with the same denominator, such as comparing three quarters and one quarter, to decide which fraction represents a greater amount.',
  [('Which is greater, one half or one quarter?', ['one half']),
   ('Which is greater, three quarters or one quarter?', ['three quarters']),
   ('When two fractions have the same denominator, how do we know which is greater?', ['the one with the bigger numerator is greater', 'compare the numerators', 'the larger top number is greater'])],
  [('Which is greater, one half or one quarter?', ['One half', 'One quarter', 'They are equal', 'Cannot tell'], 0),
   ('Which is greater, three quarters or one quarter?', ['Three quarters', 'One quarter', 'They are equal', 'Cannot tell'], 0),
   ('When two fractions have the same denominator, which fraction is greater?', ['The one with the larger numerator', 'The one with the smaller numerator', 'They are always equal', 'The one written first'], 0),
   ('Which is greater, two thirds or one third?', ['Two thirds', 'One third', 'They are equal', 'Cannot tell'], 0),
   ('A fraction with a larger numerator and the same denominator represents ___.', ['A greater amount', 'A smaller amount', 'The same amount', 'No amount at all'], 0)])

d75_sci = sub('Science', 'Types of Precipitation: Rain, Snow, Sleet, and Hail',
  'Students learn that precipitation is water that falls from clouds in different forms, including rain, snow, sleet, and hail, depending on the temperature of the air.',
  [('What word describes water that falls from clouds, such as rain or snow?', ['precipitation']),
   ('Name one form of precipitation that falls in cold winter weather.', ['snow', 'hail', 'sleet']),
   ('What usually causes water to fall as snow instead of rain?', ['cold air', 'cold temperatures', 'freezing temperatures'])],
  [('What word describes water that falls from clouds in different forms?', ['Precipitation', 'Evaporation', 'Condensation', 'Pollination'], 0),
   ('Which of these is a form of precipitation?', ['Snow', 'Wind', 'Sunshine', 'A rainbow'], 0),
   ('What usually causes precipitation to fall as snow instead of rain?', ['Cold temperatures', 'Hot temperatures', 'No clouds at all', 'Strong sunshine'], 0),
   ('Which type of precipitation falls as small balls of ice, often during a thunderstorm?', ['Hail', 'Snow', 'Rain', 'Fog'], 0),
   ('Precipitation is an important part of ___.', ['The water cycle', 'The rock cycle', 'The food chain', 'The solar system'], 0)])

d75_ss = sub('SocialStudies', 'Family Heritage: Learning Where We Come From',
  'Students learn that heritage means the traditions, language, and history passed down through a family, and that people can learn about their heritage by talking to relatives or looking at old photographs.',
  [('What word describes the traditions, language, and history passed down through a family?', ['heritage']),
   ('Name one way a person could learn about their family heritage, like talking to relatives.', ['talking to relatives', 'asking relatives', 'looking at old photographs']),
   ('Name one thing that might be part of a family heritage, like a language or a recipe.', ['a language', 'language', 'a recipe', 'recipe', 'a tradition', 'tradition'])],
  [('What word describes the traditions, language, and history passed down through a family?', ['Heritage', 'Geography', 'Government', 'Currency'], 0),
   ('Which of these is a good way to learn about family heritage?', ['Talking with relatives about family stories', 'Ignoring all family members', 'Only reading science books', 'Watching random cartoons'], 0),
   ('Which of these could be part of a family heritage?', ['A special recipe passed down for generations', 'A brand new invention with no history', 'A stranger encountered yesterday', 'A rule made up on the spot'], 0),
   ('Why might someone look at old family photographs?', ['To learn about family history and heritage', 'To learn how to cook', 'To learn about outer space', 'To learn a new sport'], 0),
   ('Learning about family heritage helps a person understand ___.', ['Where their family traditions and history come from', 'How to build a house', 'How to tell time', 'How to measure length'], 0)])

# ─── DAY 76 ─────────────────────────────────────────────────────────────────
d76_lang = sub('Language', 'Making Connections: Text to Self',
  'Students learn to make text-to-self connections by relating events or feelings in a story to their own life experiences, which helps deepen understanding of what they read.',
  [('What do we call connecting a story to something in your own life?', ['a text-to-self connection', 'text-to-self connection']),
   ('Why do readers make text-to-self connections?', ['to understand the story better', 'to deepen understanding', 'it helps understanding']),
   ('Name one thing a reader might connect a story to, like a memory or a feeling.', ['a memory', 'a feeling', 'an experience'])],
  [('What do we call connecting a story to something in your own life?', ['A text-to-self connection', 'A caption', 'A rhyme', 'A summary'], 0),
   ('Why might a reader make a text-to-self connection while reading?', ['It helps them understand the story more deeply', 'It makes the book disappear', 'It changes the ending of the story', 'It removes all the pictures'], 0),
   ('Which is an example of a text-to-self connection?', ['This story reminds me of the time I lost my favourite toy.', 'This book has ten chapters.', 'This book was written by a famous author.', 'This book has a red cover.'], 0),
   ('Making connections while reading can help a reader ___.', ['Understand and remember a story better', 'Forget the story completely', 'Skip the whole book', 'Read more slowly with no purpose'], 0),
   ('A text-to-self connection links a story to ___.', ['Something the reader has experienced in their own life', 'The title of another book', 'A math equation', 'A map of the world'], 0)])

d76_math = sub('Math', 'Faces, Edges, and Vertices of 3D Shapes',
  'Students learn to identify and count the flat faces, straight edges, and pointed vertices of three-dimensional shapes, such as cubes and pyramids.',
  [('How many faces does a cube have?', ['6']),
   ('What do we call the corner point where edges of a 3D shape meet?', ['a vertex', 'vertex', 'corner']),
   ('How many edges does a cube have?', ['12'])],
  [('How many faces does a cube have?', ['6', '4', '8', '12'], 0),
   ('What do we call the corner point where edges of a 3D shape meet?', ['A vertex', 'A face', 'An edge', 'A base'], 0),
   ('How many edges does a cube have?', ['12', '6', '8', '10'], 0),
   ('What do we call a flat surface on a 3D shape?', ['A face', 'A vertex', 'An edge', 'A line'], 0),
   ('How many vertices does a cube have?', ['8', '6', '12', '4'], 0)])

d76_sci = sub('Science', 'Stars and Constellations',
  'Students learn that stars are giant balls of hot gas that give off their own light, and that a constellation is a group of stars that forms a pattern in the night sky.',
  [('What do we call a giant ball of hot gas that gives off its own light in space?', ['a star', 'star']),
   ('What do we call a group of stars that forms a pattern in the sky?', ['a constellation', 'constellation']),
   ('Name one famous constellation, like the Big Dipper.', ['the big dipper', 'big dipper', 'orion'])],
  [('What do we call a giant ball of hot gas that gives off its own light in space?', ['A star', 'A planet', 'A comet', 'A moon'], 0),
   ('What do we call a group of stars that forms a pattern in the night sky?', ['A constellation', 'A galaxy', 'An orbit', 'An eclipse'], 0),
   ('Which of these is an example of a constellation?', ['The Big Dipper', 'Earth', 'The sun', 'The moon'], 0),
   ('Stars appear to twinkle in the night sky because ___.', ['Their light travels through moving air in our atmosphere', 'They turn on and off', 'They are very close to Earth', 'They are actually moving very slowly across the sky'], 0),
   ('When is it easiest to see stars in the sky?', ['At night, away from bright city lights', 'At noon on a sunny day', 'During a thunderstorm', 'Only in the summer'], 0)])

d76_ss = sub('SocialStudies', 'Famous Landmarks Around the World',
  'Students learn about famous landmarks from other countries, such as the Eiffel Tower in France and the Great Wall in China, and how landmarks help people recognize and remember a place.',
  [('In which country would you find the Eiffel Tower?', ['france']),
   ('In which country would you find the Great Wall?', ['china']),
   ('What do we call a well-known structure or place that helps people recognize a location?', ['a landmark', 'landmark'])],
  [('In which country would you find the Eiffel Tower?', ['France', 'China', 'Egypt', 'Canada'], 0),
   ('In which country would you find the Great Wall?', ['China', 'France', 'Egypt', 'Canada'], 0),
   ('What do we call a well-known structure or place that helps people recognize a location?', ['A landmark', 'A province', 'A currency', 'A government'], 0),
   ('Why are famous landmarks important to a country?', ['They help represent the culture and history of a place', 'They have no meaning at all', 'They are only used for parking', 'They stop tourists from visiting'], 0),
   ('Which of these is an example of a famous landmark?', ['The Great Wall', 'A random empty field', 'An ordinary street sign', 'A plain brick wall'], 0)])

# ─── DAY 77 ─────────────────────────────────────────────────────────────────
d77_lang = sub('Language', 'Summarizing a Story in a Few Sentences',
  'Students learn to summarize a story by telling the most important events in just a few sentences, leaving out small details that are not essential to the main plot.',
  [('What does it mean to summarize a story?', ['to tell the most important events in a few sentences', 'to tell the main events briefly', 'retelling the main events shortly']),
   ('Should a summary include every small detail or just the most important events?', ['the most important events', 'just the most important events']),
   ('Why is summarizing a story a useful skill?', ['it helps readers remember the main events', 'it helps understanding', 'to check understanding of the story'])],
  [('What does it mean to summarize a story?', ['To tell the most important events in a few sentences', 'To copy the whole story word for word', 'To draw a picture instead of writing', 'To read the story out loud'], 0),
   ('A good summary should include ___.', ['Only the most important events', 'Every single detail from the story', 'No events at all', 'Only the title of the story'], 0),
   ('Which of these is closest to a summary of a story about a lost dog?', ['A dog gets lost, a family searches, and they find the dog.', 'Dogs are mammals with four legs.', 'The cover of the book is blue.', 'The author lives in Ontario.'], 0),
   ('Why might a student summarize a chapter before starting a new one?', ['To remember what happened so far', 'To forget the story completely', 'To make the chapter longer', 'To change the ending'], 0),
   ('A summary is usually ___ than the original story.', ['Much shorter', 'Much longer', 'Exactly the same length', 'Written only in pictures'], 0)])

d77_math = sub('Math', 'Quarter Past and Quarter To: Telling Time in Detail',
  'Students learn to read clocks that show quarter past the hour, when the minute hand points to the 3, and quarter to the hour, when the minute hand points to the 9.',
  [('When the minute hand points to the 3, what do we call that time, quarter past or quarter to?', ['quarter past']),
   ('When the minute hand points to the 9, what do we call that time?', ['quarter to']),
   ('How many minutes are in a quarter of an hour?', ['15'])],
  [('When the minute hand points to the 3, what time is it, quarter past or quarter to the hour?', ['Quarter past', 'Quarter to', 'Half past', 'On the hour'], 0),
   ('When the minute hand points to the 9, what time is it?', ['Quarter to the next hour', 'Quarter past the hour', 'Half past the hour', 'On the hour'], 0),
   ('How many minutes are in a quarter of an hour?', ['15', '30', '45', '10'], 0),
   ('If it is quarter past 4, where does the minute hand point?', ['The 3', 'The 6', 'The 9', 'The 12'], 0),
   ('If it is quarter to 5, how many minutes remain until the hour of 5?', ['15', '30', '45', '10'], 0)])

d77_sci = sub('Science', 'Animal Life Spans: How Long Animals Live',
  'Students learn that different animals have different life spans, the length of time they typically live, such as a mouse living only a few years while a tortoise can live over one hundred years.',
  [('What word describes the length of time an animal typically lives?', ['life span', 'a life span']),
   ('Name one animal that has a very long life span, like a tortoise.', ['a tortoise', 'tortoise', 'an elephant', 'elephant']),
   ('Does a mouse usually have a longer or shorter life span than a tortoise?', ['shorter'])],
  [('What word describes the length of time an animal typically lives?', ['Life span', 'Habitat', 'Camouflage', 'Migration'], 0),
   ('Which of these animals is known for having a very long life span?', ['A tortoise', 'A mouse', 'A housefly', 'A mayfly'], 0),
   ('Does a small mouse usually have a longer or shorter life span than a large tortoise?', ['Shorter', 'Longer', 'Exactly the same', 'Mice do not have a life span'], 0),
   ('Which of these could affect how long an animal lives?', ['Its size, habitat, and species', 'The colour of the sky', 'The day of the week', 'The season only'], 0),
   ('Learning about animal life spans helps scientists understand ___.', ['How long different animals typically live', 'How to build a house', 'How to bake bread', 'How to tell time'], 0)])

d77_ss = sub('SocialStudies', 'Reading a Map Legend: Symbols and Keys',
  'Students learn that a map legend, also called a key, explains what the symbols and colours on a map represent, such as a blue line for a river or a green square for a park.',
  [('What do we call the part of a map that explains what symbols and colours represent?', ['a legend', 'legend', 'a key', 'key']),
   ('What might a blue line on a map represent?', ['a river', 'river', 'water']),
   ('Why is a map legend useful?', ['it explains what the symbols mean', 'it helps readers understand the map', 'to understand map symbols'])],
  [('What do we call the part of a map that explains what symbols and colours represent?', ['A legend', 'A compass', 'A border', 'A scale'], 0),
   ('What might a blue line on a map most likely represent?', ['A river or body of water', 'A mountain', 'A desert', 'A road'], 0),
   ('Why is a map legend useful to someone reading a map?', ['It explains what the symbols and colours mean', 'It changes the size of the map', 'It removes all symbols from the map', 'It tells you the time of day'], 0),
   ('If a map legend shows a green square means a park, what does a green square on the map represent?', ['A park', 'A hospital', 'A school', 'A river'], 0),
   ('A map legend is also sometimes called a ___.', ['Key', 'Border', 'Compass rose', 'Scale bar'], 0)])

# ─── DAY 78 ─────────────────────────────────────────────────────────────────
d78_lang = sub('Language', 'Editing Your Writing: Checking for Mistakes',
  'Students learn that editing means rereading their writing to check for and fix mistakes in spelling, punctuation, and capital letters before sharing a finished piece.',
  [('What do we call rereading writing to check for and fix mistakes?', ['editing', 'edit']),
   ('Name one thing a writer checks for while editing, like spelling or punctuation.', ['spelling', 'punctuation', 'capital letters']),
   ('Why is editing an important step in writing?', ['to fix mistakes', 'to make writing clearer', 'it helps writing become clearer'])],
  [('What do we call rereading writing to check for and fix mistakes?', ['Editing', 'Publishing', 'Illustrating', 'Skipping'], 0),
   ('Which of these is something a writer checks for while editing?', ['Spelling and punctuation', 'The colour of the paper', 'The size of the desk', 'The time of day'], 0),
   ('When should editing usually happen during the writing process?', ['After a first draft is written, before sharing the final piece', 'Before any writing begins', 'Only after the piece is published', 'Never, editing is not needed'], 0),
   ('Which sentence needs editing because of a capitalization mistake?', ['my dog likes to run in the park.', 'My dog likes to run in the park.', 'The dog ran fast.', 'She has a small dog.'], 0),
   ('Editing helps a writer ___.', ['Make their writing clearer and more correct', 'Add random mistakes on purpose', 'Erase the whole piece of writing', 'Ignore spelling completely'], 0)])

d78_math = sub('Math', 'Estimating Sums and Differences',
  'Students learn to estimate a sum or difference by rounding numbers before adding or subtracting, which gives a quick, reasonable answer without exact calculation.',
  [('What do we do to numbers before estimating a sum?', ['round them', 'round the numbers']),
   ('Estimate the sum of 42 and 39 by rounding each to the nearest ten first.', ['80']),
   ('Why is estimating a useful skill?', ['it gives a quick reasonable answer', 'to check if an exact answer makes sense', 'it helps check work quickly'])],
  [('What do we do to numbers before estimating a sum?', ['Round them to a nearby ten', 'Multiply them by ten', 'Divide them in half', 'Ignore them completely'], 0),
   ('Estimate the sum of 42 and 39 by rounding each to the nearest ten first.', ['80', '70', '90', '60'], 0),
   ('Estimate the difference of 81 and 19 by rounding each to the nearest ten first.', ['60', '50', '70', '40'], 0),
   ('Why might someone estimate before solving an exact math problem?', ['To quickly check if the exact answer seems reasonable', 'To avoid all math forever', 'To make the problem harder', 'To get a random answer'], 0),
   ('An estimate is ___.', ['A close, reasonable answer found by rounding', 'Always the exact answer', 'Never useful in math', 'Always wrong'], 0)])

d78_sci = sub('Science', 'Renewable and Nonrenewable Energy Sources',
  'Students learn that renewable energy sources, like sunlight and wind, can be used again and again without running out, while nonrenewable energy sources, like coal and oil, take millions of years to form and can run out.',
  [('Name one renewable energy source, like the sun or wind.', ['the sun', 'sun', 'wind', 'water']),
   ('Name one nonrenewable energy source, like coal or oil.', ['coal', 'oil']),
   ('Which type of energy source can run out, renewable or nonrenewable?', ['nonrenewable'])],
  [('Which of these is a renewable energy source?', ['Sunlight', 'Coal', 'Oil', 'Natural gas'], 0),
   ('Which of these is a nonrenewable energy source?', ['Coal', 'Wind', 'Sunlight', 'Water'], 0),
   ('What does it mean for an energy source to be renewable?', ['It can be used again and again without running out', 'It runs out after one use', 'It takes millions of years to form', 'It cannot be used at all'], 0),
   ('Why do many scientists encourage using more renewable energy?', ['Because it will not run out like nonrenewable sources can', 'Because it is always more expensive', 'Because it never produces any energy', 'Because it is illegal to use nonrenewable energy'], 0),
   ('Wind turbines and solar panels are used to capture ___.', ['Renewable energy from wind and sunlight', 'Nonrenewable energy from coal', 'Energy from underground oil', 'Energy from ocean salt only'], 0)])

d78_ss = sub('SocialStudies', 'Fair Play: Following Rules When We Play',
  'Students learn that fair play means following the rules of a game, taking turns, and treating others with respect, whether a team wins or loses.',
  [('What do we call following the rules of a game and treating others with respect?', ['fair play']),
   ('Name one example of fair play, like taking turns.', ['taking turns', 'following the rules', 'sharing']),
   ('How should players treat each other whether their team wins or loses?', ['with respect', 'fairly', 'kindly'])],
  [('What do we call following the rules of a game and treating others with respect?', ['Fair play', 'Cheating', 'Arguing', 'Ignoring the rules'], 0),
   ('Which of these is an example of fair play?', ['Taking turns and following the rules', 'Cheating to win', 'Yelling at teammates', 'Breaking the rules on purpose'], 0),
   ('How should players treat each other after a game, whether they win or lose?', ['With respect and good sportsmanship', 'With anger', 'By ignoring the other team', 'By breaking the rules'], 0),
   ('Why is fair play important in games and sports?', ['It helps everyone enjoy the game and be treated fairly', 'It makes the game longer', 'It lets one team cheat', 'It stops anyone from playing'], 0),
   ('Which of these shows good sportsmanship after losing a game?', ['Congratulating the other team', 'Yelling and refusing to shake hands', 'Breaking the game equipment', 'Blaming a teammate unfairly'], 0)])

# ─── DAY 79 ─────────────────────────────────────────────────────────────────
d79_lang = sub('Language', 'Word Choice: How Writers Choose Strong Words',
  'Students learn that writers choose strong, specific words on purpose, such as replacing happy with thrilled, to create a clearer picture and stronger feeling for the reader.',
  [('What do we call the specific words a writer chooses on purpose?', ['word choice']),
   ('Which is a stronger word choice than happy: glad or thrilled?', ['thrilled']),
   ('Why do writers choose strong, specific words?', ['to create a clearer picture', 'to make writing more interesting', 'to give the reader a stronger feeling'])],
  [('What do we call the specific words a writer chooses on purpose to create an effect?', ['Word choice', 'Punctuation', 'A title', 'A caption'], 0),
   ('Which word is a stronger, more specific choice than the word happy?', ['Thrilled', 'Good', 'Nice', 'Fine'], 0),
   ('Why might a writer replace the word big with enormous?', ['To create a stronger, clearer picture for the reader', 'To make the sentence confusing', 'To remove all meaning', 'To make the word shorter'], 0),
   ('Which sentence uses the strongest word choice?', ['The enormous dinosaur stomped through the forest.', 'The big dinosaur walked.', 'The dinosaur moved.', 'A dinosaur was there.'], 0),
   ('Strong word choice helps writing become ___.', ['More vivid and interesting for the reader', 'Harder to understand', 'Completely silent', 'Shorter than a single word'], 0)])

d79_math = sub('Math', 'Venn Diagrams: Sorting Objects by Attributes',
  'Students learn to use a Venn diagram, two overlapping circles, to sort objects by shared and different attributes, placing items that share both attributes in the overlapping middle section.',
  [('What do we call a diagram with two overlapping circles used to sort objects?', ['a venn diagram', 'venn diagram']),
   ('Where do we place an object that fits into both circles of a Venn diagram?', ['in the overlapping middle section', 'the middle', 'in the middle']),
   ('Name one attribute we might use to sort shapes in a Venn diagram, like colour or number of sides.', ['colour', 'number of sides', 'shape', 'size'])],
  [('What do we call a diagram with two overlapping circles used to sort objects?', ['A Venn diagram', 'A bar graph', 'A line plot', 'A tally chart'], 0),
   ('Where do we place an object that shares both attributes in a Venn diagram?', ['In the overlapping middle section', 'Outside both circles', 'Only in the left circle', 'Only in the right circle'], 0),
   ('Which of these could be an attribute used to sort shapes in a Venn diagram?', ['Number of sides', 'The weather today', 'A favourite song', 'The time of day'], 0),
   ('If a shape is red and has four sides, and the circles show red shapes and four-sided shapes, where does it go?', ['In the overlapping middle section', 'Outside both circles', 'Only in the red circle', 'Only in the four-sided circle'], 0),
   ('A Venn diagram helps us understand ___.', ['How groups of objects are similar and different', 'How to measure temperature', 'How to tell time', 'How to add two numbers'], 0)])

d79_sci = sub('Science', 'Scientific Method: Asking Questions and Testing Ideas',
  'Students learn that scientists use the scientific method, a set of steps that includes asking a question, making a prediction, testing the idea, and recording what happens, to learn about the world.',
  [('What is the first step of the scientific method, before testing an idea?', ['asking a question', 'ask a question']),
   ('What do we call the guess a scientist makes about what will happen before testing an idea?', ['a prediction', 'prediction']),
   ('Why do scientists record what happens during a test?', ['to remember the results', 'to see what happened', 'to learn from the results'])],
  [('What is usually the first step of the scientific method?', ['Asking a question', 'Recording results', 'Building a robot', 'Skipping the test'], 0),
   ('What do we call the guess a scientist makes about what will happen before testing an idea?', ['A prediction', 'A fossil', 'A habitat', 'A constellation'], 0),
   ('Why do scientists test their ideas?', ['To see if their prediction was correct', 'To make the question disappear', 'To avoid learning anything new', 'To skip recording results'], 0),
   ('Why is it important for scientists to record what happens during a test?', ['So they can remember and learn from the results', 'So they can forget the test happened', 'So the test becomes a secret', 'So no one else can see the results'], 0),
   ('Using the scientific method helps scientists ___.', ['Learn about the world in a careful, organized way', 'Guess randomly with no testing', 'Avoid asking any questions', 'Ignore what they observe'], 0)])

d79_ss = sub('SocialStudies', 'How People Told Time Before Clocks and Watches',
  'Students learn that before mechanical clocks and watches were common, people told time using tools like sundials, which used the position of the sun shadow, and hourglasses filled with falling sand.',
  [('What tool used the position of a shadow from the sun to tell time?', ['a sundial', 'sundial']),
   ('What tool used falling sand to measure time?', ['an hourglass', 'hourglass']),
   ('Name one way people long ago knew it was time to wake up without an alarm clock, like the sunrise.', ['the sunrise', 'sunrise', 'a rooster crowing', 'rooster crowing'])],
  [('What tool used the position of a shadow from the sun to tell time?', ['A sundial', 'A calendar', 'A compass', 'A thermometer'], 0),
   ('What tool used falling sand to measure time?', ['An hourglass', 'A sundial', 'A map', 'A globe'], 0),
   ('Why did a sundial stop working well at night?', ['There was no sunlight to make a shadow', 'Sand ran out', 'The moon was too bright', 'Clocks needed batteries'], 0),
   ('Before alarm clocks, what natural event often helped people know it was time to wake up?', ['The sunrise', 'A thunderstorm', 'A full moon', 'A rainbow'], 0),
   ('Learning about tools like sundials and hourglasses helps us understand ___.', ['How people measured time long ago before modern clocks', 'How to build a computer', 'How to grow food', 'How to travel by airplane'], 0)])

# ─── DAY 80 (Final Review) ──────────────────────────────────────────────────
d80_lang = sub('Language', 'Final Review: Language Skills (Days 71-79)',
  'Students review Language skills from Days 71 to 79: similes, prepositions, interjections, persuasive writing, nonfiction text features, making connections, summarizing, editing, and word choice.',
  [('What do we call a phrase that compares two things using like or as?', ['a simile', 'simile']),
   ('What do we call a word that shows the position of one thing compared to another, like under or beside?', ['a preposition', 'preposition']),
   ('What do we call rereading writing to check for and fix mistakes?', ['editing', 'edit'])],
  [('What do we call a phrase that compares two things using like or as?', ['A simile', 'A synonym', 'An antonym', 'A caption'], 0),
   ('What do we call a word that shows the position of one thing compared to another?', ['A preposition', 'A verb', 'An adjective', 'A pronoun'], 0),
   ('What do we call a short word or phrase that expresses strong feeling?', ['An interjection', 'A preposition', 'A synonym', 'A pronoun'], 0),
   ('What is the main goal of persuasive writing?', ['To convince the reader to agree with an idea', 'To describe a setting only', 'To tell what time it is', 'To list random facts'], 0),
   ('What do we call rereading writing to check for and fix mistakes?', ['Editing', 'Publishing', 'Illustrating', 'Skipping'], 0)])

d80_math = sub('Math', 'Final Review: Math Skills (Days 71-79)',
  'Students review Math skills from Days 71 to 79: three-digit addition and subtraction with regrouping, multiplication facts for 3s and 4s, fractions of a group, comparing fractions, 3D shape attributes, quarter past and quarter to, estimating sums and differences, and Venn diagrams.',
  [('What is 236 + 148?', ['384']),
   ('What is 3 times 4?', ['12']),
   ('How many faces does a cube have?', ['6'])],
  [('What is 236 + 148?', ['384', '374', '394', '284'], 0),
   ('What is 342 - 158?', ['184', '194', '174', '284'], 0),
   ('What is 3 times 4?', ['12', '10', '14', '16'], 0),
   ('Which is greater, one half or one quarter?', ['One half', 'One quarter', 'They are equal', 'Cannot tell'], 0),
   ('How many faces does a cube have?', ['6', '4', '8', '12'], 0)])

d80_sci = sub('Science', 'Final Review: Science Skills (Days 71-79)',
  'Students review Science topics from Days 71 to 79: parts of a plant, levers, the heart, digestion, precipitation, stars and constellations, animal life spans, renewable and nonrenewable energy, and the scientific method.',
  [('Which part of a plant absorbs water from the soil?', ['the roots', 'roots']),
   ('What organ pumps blood through the body?', ['the heart', 'heart']),
   ('What word describes water that falls from clouds in different forms?', ['precipitation'])],
  [('Which part of a plant absorbs water from the soil?', ['The roots', 'The stem', 'The leaves', 'The flower'], 0),
   ('What do we call the fixed point that a lever rests on?', ['A fulcrum', 'An axle', 'A pulley', 'A wedge'], 0),
   ('What organ pumps blood through the body?', ['The heart', 'The lungs', 'The stomach', 'The brain'], 0),
   ('What word describes water that falls from clouds in different forms?', ['Precipitation', 'Evaporation', 'Condensation', 'Pollination'], 0),
   ('What do we call a group of stars that forms a pattern in the night sky?', ['A constellation', 'A galaxy', 'An orbit', 'An eclipse'], 0)])

d80_ss = sub('SocialStudies', 'Final Review: Social Studies Skills (Days 71-79)',
  'Students review Social Studies topics from Days 71 to 79: where products come from, advertising, levels of government, Canadian holidays, family heritage, world landmarks, map legends, fair play, and how people told time long ago.',
  [('Where are many clothes and toys made before they reach a store?', ['a factory', 'factory', 'factories']),
   ('What do we call the level of government that looks after a town or city?', ['municipal government', 'municipal']),
   ('On what date is Canada Day celebrated?', ['july 1', 'july 1st'])],
  [('Where are many clothes and toys made before they reach a store?', ['A factory', 'A farm only', 'A forest', 'A lake'], 0),
   ('What do we call a message created by a company to convince people to buy a product?', ['An advertisement', 'A biography', 'A weather report', 'A map'], 0),
   ('What do we call the level of government that looks after a town or city?', ['Municipal government', 'Federal government', 'Provincial government', 'No government'], 0),
   ('On what date is Canada Day celebrated?', ['July 1st', 'December 25th', 'November 11th', 'January 1st'], 0),
   ('What do we call the part of a map that explains what symbols and colours represent?', ['A legend', 'A compass', 'A border', 'A scale'], 0)])


g2_71_80 = [
    day(71, [d71_lang, d71_math, d71_sci, d71_ss]),
    day(72, [d72_lang, d72_math, d72_sci, d72_ss]),
    day(73, [d73_lang, d73_math, d73_sci, d73_ss]),
    day(74, [d74_lang, d74_math, d74_sci, d74_ss]),
    day(75, [d75_lang, d75_math, d75_sci, d75_ss]),
    day(76, [d76_lang, d76_math, d76_sci, d76_ss]),
    day(77, [d77_lang, d77_math, d77_sci, d77_ss]),
    day(78, [d78_lang, d78_math, d78_sci, d78_ss]),
    day(79, [d79_lang, d79_math, d79_sci, d79_ss]),
    day(80, [d80_lang, d80_math, d80_sci, d80_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g2_71_80, seed=20260913)
    append_worksheet_days(2, g2_71_80)
