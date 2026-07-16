#!/usr/bin/env python3
"""Kindergarten (Grade 0), Days 51-60 -- third batch extending Grade 0 past
the Days 41-50 batch. This is a self-contained script (does NOT use
gen_curriculum.py's sub()/day()/append_to() helpers, since those do not
support a worksheet field) modeled exactly on gen_grade0_days41_50.py:

- resourceLabel = f"YouTube: {title}"
- resourceUrl = "https://www.youtube.com/results?search_query=" +
  urllib.parse.quote(f"{title} kindergarten educational")
- no videoUrl field (filled in later by a separate script)
- worksheet (exactly 3 free-response items) is REQUIRED on every subject

Topics were chosen to avoid any overlap with the existing Grade 0 Days
1-50 topics (see data/grade0.ts). No embedded ASCII double-quote or
straight apostrophe characters are used anywhere in title/summary/quiz/
worksheet text -- contractions and possessives are avoided entirely for
kindergarten readability and to keep the generated .ts string literals
valid.
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
            ru = 'https://www.youtube.com/results?search_query=' + urllib.parse.quote(f'{ti} kindergarten educational')
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


def _rebalance_answer_positions(days, seed=20260822):
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


# ─── DAY 51 ─────────────────────────────────────────────────────────────────
d51_lang = sub('Language', 'Adjectives: Describing Words',
  'Students learn that an adjective is a word that describes a noun, such as big, small, soft, or shiny, and practise picking adjectives to describe objects.',
  [('Name one describing word for a ball, like big or small.', ['big', 'small', 'round', 'red']),
   ('Is the word soft an adjective or a verb?', ['adjective']),
   ('In the phrase a fluffy dog, which word describes the dog?', ['fluffy'])],
  [('What is an adjective?', ['A word that shows action', 'A word that describes a noun', 'A word that names a place', 'A number word'], 1),
   ('Which word is an adjective in the phrase a big red apple?', ['Apple', 'Big', 'A', 'The'], 1),
   ('Which word could describe a kitten?', ['Run', 'Jump', 'Fluffy', 'Sing'], 2),
   ('In the sentence The tall tree swayed, which word is the adjective?', ['Tree', 'Swayed', 'Tall', 'The'], 2),
   ('Adjectives help us ___.', ['Describe how things look or feel', 'Count objects', 'Name places only', 'Show action only'], 0)])

d51_math = sub('Math', 'Comparing Groups: Which Has More',
  'Students compare two small groups of objects by counting each group and deciding which group has more, fewer, or the same amount.',
  [('A group has 4 apples and another has 2 apples. Which group has more?', ['4 apples', 'the group with 4', 'first group']),
   ('If two groups both have 3 blocks, do they have the same amount or a different amount?', ['same']),
   ('A group has 5 stars and another has 7 stars. Which group has fewer?', ['5 stars', 'the group with 5', 'first group'])],
  [('A group has 6 balls and another has 3 balls. Which group has more?', ['The group with 3', 'The group with 6', 'They are equal', 'Cannot tell'], 1),
   ('A group has 2 fish and another has 8 fish. Which group has fewer?', ['The group with 8', 'The group with 2', 'They are equal', 'Cannot tell'], 1),
   ('If one group has 5 cars and another group also has 5 cars, the groups are ___.', ['Equal', 'Unequal', 'Bigger', 'Smaller'], 0),
   ('To compare two groups, what should you do first?', ['Guess', 'Count each group', 'Close your eyes', 'Draw a picture'], 1),
   ('A group has 9 blocks and another has 4 blocks. Which group has more?', ['The group with 4', 'The group with 9', 'They are equal', 'Cannot tell'], 1)])

d51_sci = sub('Science', 'Our Five Fingers and Toes: Counting Body Parts',
  'Students count and name parts of their body, such as fingers, toes, ears, and eyes, and learn that most people have matching pairs of many body parts.',
  [('How many fingers do most people have on one hand?', ['5', 'five']),
   ('How many eyes do most people have?', ['2', 'two']),
   ('How many toes do most people have on one foot?', ['5', 'five'])],
  [('How many fingers are on one hand?', ['3', '4', '5', '6'], 2),
   ('How many ears does a person usually have?', ['1', '2', '3', '4'], 1),
   ('How many toes are on one foot?', ['4', '5', '6', '10'], 1),
   ('Which body part do we use to smell?', ['Ears', 'Nose', 'Elbow', 'Knee'], 1),
   ('Most people have body parts that come in matching ___.', ['Squares', 'Pairs', 'Circles', 'Triangles'], 1)])

d51_ss = sub('SocialStudies', 'My Body Belongs to Me: Personal Safety',
  'Students learn that their body belongs to them, that they can say no to touches that feel wrong, and that they should tell a trusted adult if something feels unsafe.',
  [('Whose body is your body?', ['mine', 'my own', 'yours']),
   ('If a touch feels wrong, what word can you say to stop it?', ['no']),
   ('If something feels unsafe, who should you tell?', ['a trusted adult', 'trusted adult', 'parent', 'teacher'])],
  [('Whose body belongs to you?', ['Your friend', 'Your own', 'A stranger', 'No one'], 1),
   ('If a touch feels wrong, what can you say?', ['Yes', 'No', 'Maybe', 'Nothing'], 1),
   ('If something feels unsafe, what should you do?', ['Keep it a secret', 'Tell a trusted adult', 'Ignore it', 'Run far away alone'], 1),
   ('Who could be a trusted adult you tell about an unsafe feeling?', ['A parent or teacher', 'A stranger', 'No one at all', 'A cartoon character'], 0),
   ('It is okay to say no to a touch that ___.', ['Feels wrong or unsafe', 'Is a high five', 'Is a handshake', 'Is a hug from a parent'], 0)])

# ─── DAY 52 ─────────────────────────────────────────────────────────────────
d52_lang = sub('Language', 'Alphabetical Order: A Comes Before B',
  'Students practise putting a small group of letters in alphabetical order, learning that the alphabet always follows the same fixed sequence from A to Z.',
  [('Which letter comes first in the alphabet, A or B?', ['a', 'A']),
   ('Which letter comes right after C in the alphabet?', ['d', 'D']),
   ('Put these letters in order: C, A, B. What is the first letter in alphabetical order?', ['a', 'A'])],
  [('Which letter comes first in the alphabet?', ['B', 'A', 'C', 'D'], 1),
   ('Which letter comes right after D in the alphabet?', ['C', 'E', 'F', 'B'], 1),
   ('Put these letters in order: B, A, C. What comes first?', ['B', 'A', 'C', 'None'], 1),
   ('Alphabetical order means letters are arranged ___.', ['Randomly', 'In their fixed A to Z sequence', 'By colour', 'By size'], 1),
   ('Which letter comes last of these three: M, A, G?', ['M', 'A', 'G', 'None'], 0)])

d52_math = sub('Math', 'Even and Odd: Sharing into Two Groups',
  'Students explore even and odd numbers by trying to split a small group of objects into two equal groups, learning that even numbers split evenly and odd numbers leave one extra.',
  [('If you split 4 blocks into two equal groups, does each group get the same amount?', ['yes']),
   ('If you split 5 blocks into two equal groups, is there one block left over?', ['yes']),
   ('Is the number 2 an even number or an odd number?', ['even'])],
  [('If you split 6 counters into two equal groups, does one get left over?', ['Yes', 'No', 'Cannot tell', 'Only sometimes'], 1),
   ('If you split 7 counters into two equal groups, does one get left over?', ['No', 'Yes', 'Cannot tell', 'Only sometimes'], 1),
   ('Is the number 4 even or odd?', ['Odd', 'Even', 'Neither', 'Both'], 1),
   ('Is the number 3 even or odd?', ['Even', 'Odd', 'Neither', 'Both'], 1),
   ('An even number can always be split into two groups that are ___.', ['Unequal', 'Equal', 'Empty', 'Triangular'], 1)])

d52_sci = sub('Science', 'Where Food Comes From: Farm to Table',
  'Students learn that much of our food comes from plants and animals on farms, and trace the simple journey of foods such as milk, apples, and bread to our table.',
  [('Where does milk come from?', ['cow', 'a cow']),
   ('Where do apples grow?', ['tree', 'apple tree']),
   ('What crop is often ground up to make bread?', ['wheat'])],
  [('Where does milk come from?', ['A cow', 'A tree', 'The ground', 'A river'], 0),
   ('Where do apples grow?', ['Underground', 'On a tree', 'In water', 'On a bush'], 1),
   ('What crop is often used to make bread?', ['Wheat', 'Cotton', 'Grass', 'Sand'], 0),
   ('Which of these foods comes from a plant?', ['Milk', 'Carrot', 'Egg', 'Cheese'], 1),
   ('Why is it helpful to know where food comes from?', ['It is not helpful', 'It helps us understand and appreciate our food', 'Food does not come from anywhere', 'Only farmers need to know'], 1)])

d52_ss = sub('SocialStudies', 'Waiting and Patience: Taking Our Turn in Line',
  'Students learn why waiting patiently and standing in line is important for fairness, such as waiting for the slide, the washroom, or a turn to speak.',
  [('What word means staying calm while you wait for your turn?', ['patience', 'patient']),
   ('Why do we form a line at the slide or the water fountain?', ['to be fair', 'so everyone gets a turn']),
   ('Is it fair to skip ahead of others in a line?', ['no'])],
  [('What does it mean to be patient?', ['Staying calm while waiting', 'Yelling loudly', 'Pushing others', 'Running away'], 0),
   ('Why do people form a line at a water fountain?', ['So everyone gets a fair turn', 'Lines are not needed', 'To confuse people', 'To slow everyone down forever'], 0),
   ('Is it fair to push ahead of others in a line?', ['Yes', 'No', 'Sometimes', 'Only on Fridays'], 1),
   ('Waiting patiently in line shows that you are being ___.', ['Rude', 'Fair and respectful', 'Careless', 'Selfish'], 1),
   ('If you really want a turn but must wait, what is a good choice?', ['Wait calmly for your turn', 'Cut in line', 'Cry loudly', 'Push someone'], 0)])

# ─── DAY 53 ─────────────────────────────────────────────────────────────────
d53_lang = sub('Language', 'Print Concepts: Reading Left to Right',
  'Students learn basic print concepts, such as reading a page from left to right and top to bottom, and that words are separated by spaces.',
  [('When reading English, do our eyes move left to right or right to left?', ['left to right']),
   ('Do we read the top of the page first or the bottom of the page first?', ['top']),
   ('What separates one word from another word on a page?', ['space', 'a space'])],
  [('When reading English, which way do our eyes move across the page?', ['Right to left', 'Left to right', 'Bottom to top', 'In circles'], 1),
   ('Which part of the page do we usually read first?', ['The bottom', 'The top', 'The middle', 'The very last line'], 1),
   ('What separates one word from the next word on a page?', ['A space', 'A number', 'A colour', 'Nothing'], 0),
   ('When we finish reading one line, where do our eyes go next?', ['Back to the very top', 'Down to the start of the next line', 'Off the page', 'To a different book'], 1),
   ('Knowing how print works helps us ___.', ['Read smoothly', 'Draw pictures', 'Count numbers', 'Sing songs'], 0)])

d53_math = sub('Math', 'Positional Numbers: Counting Objects in a Row',
  'Students count a row of objects and identify how many objects there are in total, as well as which object is in a certain counted position, reinforcing one-to-one counting.',
  [('If there are 6 ducks in a row, how many ducks are there in total?', ['6', 'six']),
   ('Count the row: apple, apple, apple. How many apples are there?', ['3', 'three']),
   ('If you count 8 blocks one by one, what is the last number you say?', ['8', 'eight'])],
  [('If there are 7 birds in a row, how many birds are there in total?', ['5', '6', '7', '8'], 2),
   ('Count the row: star, star, star, star. How many stars are there?', ['3', '4', '5', '6'], 1),
   ('If you count 9 blocks one by one, what is the last number you say?', ['7', '8', '9', '10'], 2),
   ('When counting objects, each object should be counted ___.', ['Twice', 'Only one time', 'Zero times', 'Randomly'], 1),
   ('If there are 5 cars in a row, how many cars are there in total?', ['4', '5', '6', '7'], 1)])

d53_sci = sub('Science', 'Hot and Cold: Temperature All Around Us',
  'Students explore hot and cold temperatures in everyday life, sorting items and places such as ice, soup, snow, and sunshine into hot or cold categories.',
  [('Is ice hot or cold?', ['cold']),
   ('Is hot soup hot or cold?', ['hot']),
   ('Is snow hot or cold?', ['cold'])],
  [('Is ice hot or cold?', ['Hot', 'Cold', 'Neither', 'Both'], 1),
   ('Is a bowl of hot soup hot or cold?', ['Cold', 'Hot', 'Neither', 'Both'], 1),
   ('Which of these is usually cold?', ['Snow', 'A campfire', 'Hot soup', 'The summer sun'], 0),
   ('Which of these is usually hot?', ['Ice cubes', 'Snow', 'A campfire', 'A cold drink'], 2),
   ('Why is it useful to know if something is hot or cold?', ['To help us stay safe and comfortable', 'It is not useful', 'Temperature does not matter', 'Only chefs need to know'], 0)])

d53_ss = sub('SocialStudies', 'Our Senior Neighbours: Respecting Older People',
  'Students learn about older people in the community, such as grandparents and senior neighbours, and discuss ways to show them respect and kindness.',
  [('Name one older family member you might have, like a grandparent.', ['grandparent', 'grandma', 'grandpa']),
   ('What is one kind way to treat an older neighbour, like helping carry something?', ['helping', 'being kind', 'being polite']),
   ('Should we be respectful and kind to older people in our community?', ['yes'])],
  [('Which of these is an example of an older family member?', ['A baby', 'A grandparent', 'A toddler', 'A puppy'], 1),
   ('What is a kind way to treat an older neighbour?', ['Ignore them', 'Help them and speak politely', 'Be rude to them', 'Run away from them'], 1),
   ('Why might older people have interesting stories to share?', ['They have lived through many experiences over time', 'Older people know nothing', 'Stories are not important', 'Only children have stories'], 0),
   ('Showing respect to older people means ___.', ['Being kind and listening to them', 'Ignoring them completely', 'Being loud around them', 'Avoiding them always'], 0),
   ('Which is a polite way to greet an older neighbour?', ['Saying hello and smiling', 'Walking away silently', 'Yelling', 'Pointing rudely'], 0)])

# ─── DAY 54 ─────────────────────────────────────────────────────────────────
d54_lang = sub('Language', 'Onset and Rime: Word Families',
  'Students explore word families by changing the first sound, or onset, of a word while keeping the ending, or rime, the same, such as changing cat to hat to mat.',
  [('Change the first sound of cat to h. What new word do you make?', ['hat']),
   ('Change the first sound of hat to m. What new word do you make?', ['mat']),
   ('Cat, hat, and mat all belong to which word family?', ['at family', '-at', 'at'])],
  [('Change the first sound of cat to b. What new word do you make?', ['Cab', 'Bat', 'Bad', 'Ban'], 1),
   ('Cat, hat, and mat all end in the same sound. This is called a ___.', ['Rime', 'Prefix', 'Number', 'Colour'], 0),
   ('Change the first sound of dog to l. What new word do you make?', ['Log', 'Dot', 'Lot', 'Dig'], 0),
   ('Which word belongs to the same word family as sun and fun?', ['Run', 'Sit', 'Cat', 'Top'], 0),
   ('Word families help us learn to read by ___.', ['Recognizing patterns in word endings', 'Ignoring letters', 'Memorizing colours', 'Counting numbers'], 0)])

d54_math = sub('Math', 'Long and Short: Comparing Lengths of Three',
  'Students compare three objects by length, placing them in order from shortest to longest, using words such as short, shorter, and shortest.',
  [('Between a pencil and a crayon, which is usually longer?', ['pencil']),
   ('If you have a short pencil, a longer crayon, and a long ruler, which one is the shortest?', ['pencil', 'short pencil']),
   ('If you have a short pencil, a longer crayon, and a long ruler, which one is the longest?', ['ruler', 'long ruler'])],
  [('Between a paperclip and a ruler, which is usually longer?', ['Paperclip', 'Ruler', 'They are the same', 'Cannot tell'], 1),
   ('If you order a short pencil, a medium crayon, and a long ruler from shortest to longest, what comes first?', ['Ruler', 'Crayon', 'Pencil', 'None'], 2),
   ('Which word describes the object with the least length among three objects?', ['Longest', 'Shortest', 'Widest', 'Tallest'], 1),
   ('Which word describes the object with the most length among three objects?', ['Shortest', 'Longest', 'Smallest', 'Narrowest'], 1),
   ('To compare the length of three objects, you should line them up ___.', ['At one end and compare', 'In a pile', 'Randomly scattered', 'Underwater'], 0)])

d54_sci = sub('Science', 'Taking Care of Our Skin: Sun Safety',
  'Students learn simple ways to protect their skin from the sun, such as wearing sunscreen, a hat, and sunglasses, and seeking shade on hot sunny days.',
  [('What can you put on your skin to protect it from the sun?', ['sunscreen']),
   ('What can you wear on your head to block the sun?', ['hat']),
   ('Where can you go on a very sunny day to stay cool and protected?', ['shade', 'the shade'])],
  [('What can protect your skin from the sun?', ['Sunscreen', 'Mud', 'Paint', 'Ice'], 0),
   ('What can you wear on your head to block the sun?', ['Mittens', 'A hat', 'Boots', 'A scarf only'], 1),
   ('Where is a cool, protected place to go on a very sunny day?', ['Direct sunlight', 'The shade', 'A hot car', 'Nowhere'], 1),
   ('Why is it important to protect our skin from too much sun?', ['To help keep our skin healthy', 'Sun never affects skin', 'It is not important', 'Only adults need protection'], 0),
   ('Which of these items helps protect your eyes from the sun?', ['Sunglasses', 'Mittens', 'A scarf', 'Boots'], 0)])

d54_ss = sub('SocialStudies', 'Public Places: Behaving in the Library',
  'Students learn about behaviour expectations in shared public places such as a library, including using quiet voices and taking care of shared books.',
  [('Should you use a loud voice or a quiet voice in the library?', ['quiet voice', 'quiet']),
   ('What should we do carefully with library books so others can enjoy them too?', ['take care of them', 'be gentle with them']),
   ('Is the library a place we share with other people?', ['yes'])],
  [('What kind of voice should you use in the library?', ['Loud voice', 'Quiet voice', 'Shouting voice', 'No voice needed'], 1),
   ('Why should we take good care of library books?', ['So other people can enjoy them too', 'Books do not matter', 'Only new books need care', 'Library books are not shared'], 0),
   ('The library is an example of a ___.', ['Private house', 'Shared public place', 'Forest', 'Farm'], 1),
   ('Which behaviour shows respect in a shared public place?', ['Being loud and messy', 'Being quiet and careful', 'Running around', 'Ignoring the rules'], 1),
   ('Why do public places like libraries have rules?', ['So everyone can enjoy the space fairly', 'Rules are not needed', 'To make visiting harder', 'Only adults must follow rules'], 0)])

# ─── DAY 55 ─────────────────────────────────────────────────────────────────
d55_lang = sub('Language', 'Story Characters: Who Is in the Story',
  'Students learn that characters are the people or animals a story is about, and practise naming the characters in a story they have read or heard.',
  [('What word describes the people or animals a story is about?', ['characters', 'character']),
   ('In a story about a rabbit and a fox, name one character.', ['rabbit', 'fox']),
   ('Can an animal be a character in a story?', ['yes'])],
  [('What is a character in a story?', ['A place in the story', 'A person or animal the story is about', 'The title of the book', 'The last page'], 1),
   ('In a story about a bear and a bird, which of these is a character?', ['The bear', 'The forest', 'The title', 'The cover'], 0),
   ('Can a story have more than one character?', ['No, only one', 'Yes, many characters', 'Stories have no characters', 'Only animals can be characters'], 1),
   ('Which of these could be a story character?', ['A talking fox', 'A page number', 'A book cover', 'A title'], 0),
   ('Knowing the characters in a story helps us ___.', ['Understand who the story is about', 'Count pages', 'Ignore the plot', 'Skip reading'], 0)])

d55_math = sub('Math', 'Counting On: Starting from a Number',
  'Students practise counting on from a given number instead of always starting at one, such as starting at 5 and counting 6, 7, 8.',
  [('Start counting at 4. What number comes next?', ['5', 'five']),
   ('Start counting at 7. Say the next two numbers.', ['8, 9', '8 9', 'eight, nine']),
   ('If you start counting on from 10, what is the next number?', ['11', 'eleven'])],
  [('If you start counting on from 6, what number comes next?', ['5', '6', '7', '8'], 2),
   ('If you start counting on from 9, what are the next two numbers?', ['7, 8', '8, 9', '10, 11', '11, 12'], 2),
   ('Counting on means you ___.', ['Always start over at one', 'Start from a given number and keep going', 'Count backward only', 'Skip every number'], 1),
   ('If you start counting on from 13, what number comes next?', ['12', '13', '14', '15'], 2),
   ('Counting on is a useful skill because it helps us ___.', ['Add numbers more quickly', 'Forget numbers', 'Slow down counting', 'Avoid math'], 0)])

d55_sci = sub('Science', 'Trees Through the Seasons',
  'Students observe how many trees change throughout the year, growing leaves in spring, staying green in summer, changing colour and dropping leaves in autumn, and standing bare in winter.',
  [('In which season do many trees grow new leaves?', ['spring']),
   ('In which season do many tree leaves turn colours and fall off?', ['autumn', 'fall']),
   ('In which season are many trees bare, without leaves?', ['winter'])],
  [('In which season do many trees grow new leaves?', ['Winter', 'Spring', 'Autumn', 'Never'], 1),
   ('In which season do many tree leaves change colour and fall?', ['Spring', 'Summer', 'Autumn', 'Never'], 2),
   ('In which season are many trees bare, without leaves?', ['Summer', 'Spring', 'Winter', 'Autumn'], 2),
   ('During which season are tree leaves usually fully green?', ['Summer', 'Winter', 'Late autumn', 'Early spring'], 0),
   ('Why do trees change throughout the year?', ['They respond to changing seasons and weather', 'Trees never change', 'Trees change only at night', 'Trees do not need seasons'], 0)])

d55_ss = sub('SocialStudies', 'My Culture: Foods, Music, and Clothing',
  'Students share and celebrate parts of their own culture, such as special foods, music, or clothing, and learn that different families celebrate in different ways.',
  [('Name one special food your family might eat, like a favourite dish.', ['rice', 'noodles', 'bread', 'soup', 'pasta']),
   ('What word describes the shared customs, foods, and traditions of a group of people?', ['culture']),
   ('Do all families around the world share the exact same culture?', ['no'])],
  [('What is culture?', ['A type of weather', 'The shared customs, foods, and traditions of a group', 'A math tool', 'A single food'], 1),
   ('Which of these could be part of a family culture?', ['Special foods', 'A math problem', 'A weather report', 'A traffic light'], 0),
   ('Do all families around the world celebrate in the exact same way?', ['Yes, always', 'No, families celebrate in different ways', 'Only some families celebrate', 'Culture does not exist'], 1),
   ('Sharing our culture with friends helps us ___.', ['Learn about and respect each other', 'Ignore differences', 'Hide who we are', 'Avoid our classmates'], 0),
   ('Which of these is an example of cultural music?', ['A traditional family song', 'A math worksheet', 'A rain gauge', 'A traffic sign'], 0)])

# ─── DAY 56 ─────────────────────────────────────────────────────────────────
d56_lang = sub('Language', 'Story Setting: Where and When',
  'Students learn that the setting of a story is the place and time where the story happens, such as a forest in the daytime or a house at night.',
  [('What word describes the place and time where a story happens?', ['setting']),
   ('If a story happens in a forest, what is the setting?', ['forest', 'a forest', 'the forest']),
   ('Can a story setting be at night?', ['yes'])],
  [('What is the setting of a story?', ['The characters in the story', 'The place and time where the story happens', 'The title of the book', 'The last page'], 1),
   ('If a story happens on a farm during the day, what is the setting?', ['A farm during the day', 'A city at night', 'The moon', 'A classroom'], 0),
   ('Which of these could be a story setting?', ['A quiet forest', 'A character named Sam', 'A page number', 'The word the'], 0),
   ('Can a story have more than one setting, such as a house and then a park?', ['No, never', 'Yes, a story can have more than one setting', 'Stories have no settings', 'Only animals have settings'], 1),
   ('Knowing the setting of a story helps us understand ___.', ['Where and when the story takes place', 'How to add numbers', 'How to draw shapes', 'How to sing songs'], 0)])

d56_math = sub('Math', 'Comparing Numbers with Symbols: Greater and Less',
  'Students compare two numbers and describe which is greater and which is less, beginning to connect the ideas of more and fewer to number comparisons within 20.',
  [('Between 8 and 3, which number is greater?', ['8', 'eight']),
   ('Between 8 and 3, which number is less?', ['3', 'three']),
   ('Are the numbers 6 and 6 equal or different?', ['equal'])],
  [('Between 12 and 7, which number is greater?', ['7', '12', 'They are equal', 'Cannot tell'], 1),
   ('Between 15 and 19, which number is less?', ['19', '15', 'They are equal', 'Cannot tell'], 1),
   ('Are 9 and 9 equal or different?', ['Different', 'Equal', 'Greater', 'Less'], 1),
   ('Between 4 and 14, which number is greater?', ['4', '14', 'They are equal', 'Cannot tell'], 1),
   ('If one number is greater than another, the smaller number is ___ the bigger one.', ['Equal to', 'Less than', 'Bigger than', 'The same as'], 1)])

d56_sci = sub('Science', 'Baby Animals: Growing Up',
  'Students learn the special names for baby animals, such as puppy, kitten, calf, and chick, and observe how baby animals grow and change over time.',
  [('What is a baby dog called?', ['puppy']),
   ('What is a baby cat called?', ['kitten']),
   ('What is a baby cow called?', ['calf'])],
  [('What is a baby dog called?', ['Kitten', 'Puppy', 'Calf', 'Chick'], 1),
   ('What is a baby cat called?', ['Puppy', 'Kitten', 'Cub', 'Chick'], 1),
   ('What is a baby cow called?', ['Foal', 'Calf', 'Cub', 'Kid'], 1),
   ('What is a baby chicken called?', ['Chick', 'Calf', 'Kitten', 'Cub'], 0),
   ('As baby animals grow up, do they usually change size and appearance?', ['No, never', 'Yes, they grow and change', 'They stay exactly the same', 'Only some animals grow'], 1)])

d56_ss = sub('SocialStudies', 'Home Safety: Staying Safe Indoors',
  'Students learn simple home safety rules, such as staying away from hot stoves, not touching sharp objects, and asking an adult for help with dangerous items.',
  [('Should you touch a hot stove by yourself?', ['no']),
   ('Who should help you with sharp or dangerous items at home?', ['an adult', 'a grown up', 'parent']),
   ('Is it safe to play near a hot stove without an adult?', ['no'])],
  [('Should young children touch a hot stove by themselves?', ['Yes', 'No', 'Only sometimes', 'It does not matter'], 1),
   ('Who should help with sharp or dangerous items at home?', ['A trusted adult', 'A stranger', 'No one', 'A pet'], 0),
   ('Which of these is a home safety rule?', ['Play with matches alone', 'Ask an adult before using sharp tools', 'Touch a hot stove', 'Run near hot pots'], 1),
   ('Why do we have safety rules at home?', ['To keep us safe from getting hurt', 'Rules are not needed at home', 'To make home boring', 'Only for adults'], 0),
   ('If you see something dangerous at home, what should you do?', ['Touch it right away', 'Tell a trusted adult', 'Ignore it', 'Hide it from everyone'], 1)])

# ─── DAY 57 ─────────────────────────────────────────────────────────────────
d57_lang = sub('Language', 'Middle Sounds: Listening for the Vowel',
  'Students practise listening for the middle sound in short words, identifying the vowel sound between the first and last consonant, such as the short a in cat.',
  [('What is the middle sound in the word cat?', ['a']),
   ('What is the middle sound in the word dog?', ['o']),
   ('What is the middle sound in the word pin?', ['i'])],
  [('What is the middle sound in the word cat?', ['C', 'A', 'T', 'None'], 1),
   ('What is the middle sound in the word hop?', ['H', 'O', 'P', 'None'], 1),
   ('What is the middle sound in the word pig?', ['P', 'I', 'G', 'None'], 1),
   ('Listening for the middle sound helps us hear the ___ in a word.', ['Vowel sound', 'First letter', 'Last letter', 'Whole sentence'], 0),
   ('What is the middle sound in the word bug?', ['B', 'U', 'G', 'None'], 1)])

d57_math = sub('Math', 'Making Shapes with Sticks: Sides and Corners',
  'Students build simple shapes using straight sticks or lines and count the number of sides and corners on shapes such as triangles, squares, and rectangles.',
  [('How many sides does a triangle have?', ['3', 'three']),
   ('How many corners does a square have?', ['4', 'four']),
   ('How many sides does a rectangle have?', ['4', 'four'])],
  [('How many sides does a triangle have?', ['2', '3', '4', '5'], 1),
   ('How many corners does a square have?', ['3', '4', '5', '6'], 1),
   ('How many sides does a rectangle have?', ['3', '4', '5', '6'], 1),
   ('A shape with three straight sides is called a ___.', ['Square', 'Triangle', 'Circle', 'Rectangle'], 1),
   ('A circle has how many straight sides?', ['0', '1', '2', '4'], 0)])

d57_sci = sub('Science', 'Our Ears: Hearing Loud and Quiet Sounds',
  'Students explore how our ears help us hear sounds, and sort sounds into loud sounds, like thunder, and quiet sounds, like a whisper.',
  [('What body part do we use to hear sounds?', ['ears']),
   ('Is thunder a loud sound or a quiet sound?', ['loud']),
   ('Is a whisper a loud sound or a quiet sound?', ['quiet'])],
  [('What body part helps us hear sounds?', ['Eyes', 'Ears', 'Nose', 'Hands'], 1),
   ('Is thunder a loud sound or a quiet sound?', ['Quiet', 'Loud', 'Neither', 'Both'], 1),
   ('Is a whisper a loud sound or a quiet sound?', ['Loud', 'Quiet', 'Neither', 'Both'], 1),
   ('Which of these is usually a loud sound?', ['A whisper', 'A drum being banged', 'A soft breeze', 'A quiet nap'], 1),
   ('Why is it important to protect our ears from very loud sounds?', ['To help keep our hearing healthy', 'Ears do not need protection', 'Loud sounds never matter', 'Only adults have ears'], 0)])

d57_ss = sub('SocialStudies', 'Volunteering: Helping Without Being Asked',
  'Students learn what it means to volunteer, offering to help someone or the community without expecting anything in return, such as picking up litter or helping a classmate.',
  [('What word means offering to help without being asked or paid?', ['volunteering', 'volunteer']),
   ('Name one way you could volunteer to help your classroom.', ['pick up litter', 'help a classmate', 'clean up', 'tidy up']),
   ('Do volunteers usually expect payment for helping?', ['no'])],
  [('What does it mean to volunteer?', ['Only helping when paid', 'Offering to help without expecting payment', 'Never helping anyone', 'Doing chores only for yourself'], 1),
   ('Which of these is an example of volunteering?', ['Picking up litter in the park', 'Ignoring a mess', 'Demanding payment for help', 'Refusing to help others'], 0),
   ('Why might someone choose to volunteer?', ['To help others and their community', 'Volunteering is never helpful', 'To get rich', 'To avoid people'], 0),
   ('If a classmate drops their crayons, a good volunteer action would be to ___.', ['Walk away', 'Help pick them up', 'Laugh at them', 'Ignore them'], 1),
   ('Volunteering helps build a ___ community.', ['Selfish', 'Kind and caring', 'Unfriendly', 'Careless'], 1)])

# ─── DAY 58 ─────────────────────────────────────────────────────────────────
d58_lang = sub('Language', 'Story Problems: What Went Wrong',
  'Students learn that many stories include a problem the characters must solve, and practise identifying the problem and how the characters try to fix it.',
  [('What word describes a challenge a character must solve in a story?', ['problem']),
   ('If a character loses their toy in a story, what is the problem?', ['losing the toy', 'lost toy', 'they lost their toy']),
   ('Do most stories include a problem the character needs to solve?', ['yes'])],
  [('What is a problem in a story?', ['A challenge the character must solve', 'The title of the book', 'A picture on the cover', 'The last word'], 0),
   ('If a character is lost in the woods, what is the story problem?', ['Being lost', 'Eating lunch', 'Singing a song', 'Taking a nap'], 0),
   ('Why do stories often include a problem?', ['To make the story interesting and show how it gets solved', 'Problems are not needed', 'To confuse readers', 'Stories never have problems'], 0),
   ('Which of these is an example of a story problem?', ['A character cannot find their lost puppy', 'A character eats breakfast', 'A character says hello', 'A character sits down'], 0),
   ('How is a story problem usually resolved?', ['It is never resolved', 'The characters find a solution', 'The story simply ends with no solution', 'It disappears with no reason'], 1)])

d58_math = sub('Math', 'Halves and Quarters: Cutting Shapes',
  'Students explore cutting shapes into two equal halves or four equal quarters, building on earlier fraction ideas by comparing halves to quarters.',
  [('If you cut a square into two equal parts, what is each part called?', ['half', 'a half']),
   ('If you cut a square into four equal parts, what is each part called?', ['quarter', 'a quarter']),
   ('Which is smaller, a half or a quarter of the same whole shape?', ['quarter', 'a quarter'])],
  [('If you cut a circle into two equal parts, each part is called a ___.', ['Quarter', 'Half', 'Whole', 'Third'], 1),
   ('If you cut a circle into four equal parts, each part is called a ___.', ['Half', 'Quarter', 'Whole', 'Double'], 1),
   ('Which is a bigger piece of the same whole shape, a half or a quarter?', ['A quarter', 'A half', 'They are the same size', 'Cannot tell'], 1),
   ('How many quarters make one whole shape?', ['2', '3', '4', '5'], 2),
   ('How many halves make one whole shape?', ['1', '2', '3', '4'], 1)])

d58_sci = sub('Science', 'Clouds in the Sky: Watching the Weather',
  'Students observe clouds in the sky and learn that clouds can look different, such as fluffy white clouds on a sunny day or dark grey clouds before rain.',
  [('What do we call the fluffy white or grey shapes we see in the sky?', ['clouds']),
   ('What colour are clouds often before it rains?', ['grey', 'dark grey']),
   ('Do clouds ever change shape as the wind blows them?', ['yes'])],
  [('What do we call the fluffy shapes we see in the sky?', ['Stars', 'Clouds', 'Puddles', 'Rainbows'], 1),
   ('What colour might clouds be right before it rains?', ['Bright yellow', 'Dark grey', 'Pink', 'Green'], 1),
   ('Do clouds ever change shape as wind blows them?', ['No, never', 'Yes, they can change shape', 'Only at night', 'Clouds do not move'], 1),
   ('Fluffy white clouds on a sunny day often mean the weather is ___.', ['Very stormy', 'Calm and pleasant', 'Snowing heavily', 'Foggy everywhere'], 1),
   ('Why do people look at clouds to help guess the weather?', ['Clouds can give hints about upcoming weather', 'Clouds never mean anything', 'Clouds cannot be seen', 'Only pilots need to look at clouds'], 0)])

d58_ss = sub('SocialStudies', 'Signs Around Us: Reading Everyday Symbols',
  'Students learn to recognize common signs and symbols in their community, such as a stop sign, a washroom sign, or an exit sign, and what each one means.',
  [('What shape is a stop sign?', ['octagon', 'eight sided shape']),
   ('What colour is a stop sign?', ['red']),
   ('What does a stop sign tell drivers and walkers to do?', ['stop'])],
  [('What shape is a stop sign?', ['Circle', 'Octagon', 'Triangle', 'Square'], 1),
   ('What colour is a stop sign?', ['Green', 'Red', 'Blue', 'Yellow'], 1),
   ('What does a stop sign tell people to do?', ['Go faster', 'Stop', 'Turn around', 'Sing a song'], 1),
   ('Why are signs and symbols important in our community?', ['They help keep everyone informed and safe', 'Signs are not important', 'Only adults need signs', 'Signs are just decorations'], 0),
   ('Which of these is an example of a community sign?', ['An exit sign', 'A birthday cake', 'A pillow', 'A shoe'], 0)])

# ─── DAY 59 ─────────────────────────────────────────────────────────────────
d59_lang = sub('Language', 'Story Feelings: How Characters Feel',
  'Students learn to notice how a story character feels, such as happy, sad, scared, or excited, by looking at clues in the pictures and words.',
  [('If a character is smiling and laughing, how might they feel?', ['happy']),
   ('If a character is crying, how might they feel?', ['sad']),
   ('Name one feeling a story character might have, like happy or scared.', ['happy', 'sad', 'scared', 'excited', 'angry'])],
  [('If a character is smiling and laughing, how do they likely feel?', ['Sad', 'Happy', 'Scared', 'Tired'], 1),
   ('If a character is crying with tears, how do they likely feel?', ['Happy', 'Sad', 'Excited', 'Calm'], 1),
   ('What clues can help us know how a character feels?', ['Pictures and words in the story', 'The colour of the book cover', 'The page numbers', 'The size of the book'], 0),
   ('If a character is jumping and clapping at a birthday party, how might they feel?', ['Excited', 'Bored', 'Angry', 'Sleepy'], 0),
   ('Understanding how characters feel helps readers ___.', ['Connect with and understand the story', 'Ignore the story', 'Skip pages', 'Forget the book'], 0)])

d59_math = sub('Math', 'Calendar Basics: Days of the Week',
  'Students learn the names of the seven days of the week in order, and practise identifying today, yesterday, and tomorrow on a simple calendar.',
  [('What day comes right after Monday?', ['tuesday', 'Tuesday']),
   ('How many days are there in one week?', ['7', 'seven']),
   ('What day comes right before Sunday?', ['saturday', 'Saturday'])],
  [('What day comes right after Monday?', ['Sunday', 'Tuesday', 'Friday', 'Wednesday'], 1),
   ('How many days are in one week?', ['5', '6', '7', '8'], 2),
   ('What day comes right before Sunday?', ['Friday', 'Monday', 'Saturday', 'Thursday'], 2),
   ('Which of these is a day of the week?', ['January', 'Friday', 'Summer', 'Spring'], 1),
   ('A calendar helps us keep track of ___.', ['Weight', 'Days, weeks, and months', 'Colours', 'Sounds'], 1)])

d59_sci = sub('Science', 'Floating in Air: How Birds Fly',
  'Students learn that birds have special features, such as wings and feathers, that help them fly, and compare birds to other animals that cannot fly.',
  [('What body part helps a bird fly?', ['wings']),
   ('What covers a bird body and helps it fly?', ['feathers']),
   ('Can most fish fly like birds?', ['no'])],
  [('What body part helps a bird fly?', ['Fins', 'Wings', 'Paws', 'Hooves'], 1),
   ('What covers most of a bird body?', ['Fur', 'Feathers', 'Scales', 'Shells'], 1),
   ('Can most fish fly the way birds do?', ['Yes', 'No', 'Sometimes', 'Always'], 1),
   ('Which of these animals can fly using wings and feathers?', ['A robin', 'A cow', 'A fish', 'A snake'], 0),
   ('Why are feathers helpful for a flying bird?', ['They help the bird fly and stay warm', 'Feathers slow birds down only', 'Feathers are not useful at all', 'Only water animals need feathers'], 0)])

d59_ss = sub('SocialStudies', 'Comparing Homes: Apartments and Houses',
  'Students compare different types of homes people live in, such as houses, apartments, and townhouses, and learn that families live in many different kinds of homes.',
  [('Name one type of home a family might live in, like a house or apartment.', ['house', 'apartment', 'townhouse']),
   ('Do all families live in the exact same type of home?', ['no']),
   ('Is an apartment usually one home inside a bigger building with many homes?', ['yes'])],
  [('Which of these is a type of home?', ['An apartment', 'A cloud', 'A river', 'A mountain'], 0),
   ('Do all families live in the exact same type of home?', ['Yes, always', 'No, homes can be different', 'Only houses exist', 'Homes do not exist'], 1),
   ('An apartment is usually found inside ___.', ['A bigger building with many homes', 'A forest', 'A boat only', 'A cave'], 0),
   ('Why might families choose different types of homes?', ['Different homes fit different family needs', 'All homes are identical', 'Homes never differ', 'Only rich families have homes'], 0),
   ('Which of these is an example of comparing homes fairly?', ['Noticing that homes can be different but all are someone special place', 'Saying one type of home is bad', 'Making fun of a home', 'Ignoring that homes differ'], 0)])

# ─── DAY 60 (Review) ────────────────────────────────────────────────────────
d60_lang = sub('Language', 'Language Review: Describing, Stories, and Sounds',
  'Students review recent Language skills: adjectives, alphabetical order, print concepts, onset and rime, story characters, story setting, middle sounds, story problems, and story feelings.',
  [('What is a word that describes a noun called?', ['adjective']),
   ('What word describes the people or animals a story is about?', ['characters', 'character']),
   ('What is the middle sound in the word cat?', ['a'])],
  [('Which word is an adjective in the phrase a big red apple?', ['Apple', 'Big', 'A', 'The'], 1),
   ('When reading English, which way do our eyes move across the page?', ['Right to left', 'Left to right', 'Bottom to top', 'In circles'], 1),
   ('What is the setting of a story?', ['The characters in the story', 'The place and time where the story happens', 'The title of the book', 'The last page'], 1),
   ('What is a problem in a story?', ['A challenge the character must solve', 'The title of the book', 'A picture on the cover', 'The last word'], 0),
   ('If a character is smiling and laughing, how do they likely feel?', ['Sad', 'Happy', 'Scared', 'Tired'], 1)])

d60_math = sub('Math', 'Math Review: Comparing, Shapes, and Time',
  'Students review recent Math skills: comparing groups, even and odd numbers, counting rows, comparing lengths, comparing numbers, shapes, halves and quarters, and days of the week.',
  [('Between 8 and 3, which number is greater?', ['8', 'eight']),
   ('How many sides does a triangle have?', ['3', 'three']),
   ('How many days are in one week?', ['7', 'seven'])],
  [('A group has 6 balls and another has 3 balls. Which group has more?', ['The group with 3', 'The group with 6', 'They are equal', 'Cannot tell'], 1),
   ('Is the number 4 even or odd?', ['Odd', 'Even', 'Neither', 'Both'], 1),
   ('How many corners does a square have?', ['3', '4', '5', '6'], 1),
   ('If you cut a circle into four equal parts, each part is called a ___.', ['Half', 'Quarter', 'Whole', 'Double'], 1),
   ('How many days are in one week?', ['5', '6', '7', '8'], 2)])

d60_sci = sub('Science', 'Science Review: Our Bodies, Animals, and Weather',
  'Students review recent Science topics: body parts, food sources, hot and cold, baby animals, our ears, clouds, and how birds fly.',
  [('How many fingers are on one hand?', ['5', 'five']),
   ('What is a baby dog called?', ['puppy']),
   ('What body part helps a bird fly?', ['wings'])],
  [('How many ears does a person usually have?', ['1', '2', '3', '4'], 1),
   ('Where does milk come from?', ['A cow', 'A tree', 'The ground', 'A river'], 0),
   ('Is ice hot or cold?', ['Hot', 'Cold', 'Neither', 'Both'], 1),
   ('What is a baby cat called?', ['Puppy', 'Kitten', 'Cub', 'Chick'], 1),
   ('What covers most of a bird body?', ['Fur', 'Feathers', 'Scales', 'Shells'], 1)])

d60_ss = sub('SocialStudies', 'Social Studies Review: Safety, Kindness, and Community',
  'Students review recent Social Studies topics: personal safety, waiting patiently, respecting seniors, culture, home safety, volunteering, community signs, and comparing homes.',
  [('If a touch feels wrong, what can you say?', ['no']),
   ('What word means offering to help without expecting payment?', ['volunteering', 'volunteer']),
   ('What shape is a stop sign?', ['octagon', 'eight sided shape'])],
  [('If something feels unsafe, what should you do?', ['Keep it a secret', 'Tell a trusted adult', 'Ignore it', 'Run far away alone'], 1),
   ('Why do people form a line at a water fountain?', ['So everyone gets a fair turn', 'Lines are not needed', 'To confuse people', 'To slow everyone down forever'], 0),
   ('What is culture?', ['A type of weather', 'The shared customs, foods, and traditions of a group', 'A math tool', 'A single food'], 1),
   ('Who should help with sharp or dangerous items at home?', ['A trusted adult', 'A stranger', 'No one', 'A pet'], 0),
   ('What colour is a stop sign?', ['Green', 'Red', 'Blue', 'Yellow'], 1)])


g0_51_60 = [
    day(51, [d51_lang, d51_math, d51_sci, d51_ss]),
    day(52, [d52_lang, d52_math, d52_sci, d52_ss]),
    day(53, [d53_lang, d53_math, d53_sci, d53_ss]),
    day(54, [d54_lang, d54_math, d54_sci, d54_ss]),
    day(55, [d55_lang, d55_math, d55_sci, d55_ss]),
    day(56, [d56_lang, d56_math, d56_sci, d56_ss]),
    day(57, [d57_lang, d57_math, d57_sci, d57_ss]),
    day(58, [d58_lang, d58_math, d58_sci, d58_ss]),
    day(59, [d59_lang, d59_math, d59_sci, d59_ss]),
    day(60, [d60_lang, d60_math, d60_sci, d60_ss]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g0_51_60)
    append_worksheet_days(0, g0_51_60)
