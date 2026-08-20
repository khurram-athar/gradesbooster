#!/usr/bin/env python3
"""Grade 3 standalone optional-worksheet content (Project Plan item 8).

Generates data/grade3_worksheets.ts: 10 worksheets per subject x 4 subjects
(Language, Math, Science, SocialStudies) = 40 worksheets, 15 multiple-choice
questions each (600 questions total). This is a NEW, separate pipeline from
the day-based curriculum in data/grade3.ts / gen_grade3_days*.py -- it does
not touch that file or its 187-day sequence.

These are supplementary practice worksheets, not new lessons, so topics are
allowed to reinforce/overlap material already covered across the 187 days.
Each subject is organized around 10 distinct practice themes/strands
progressing loosely from foundational to more advanced within that subject.

Grade 3 is multiple choice only (per Project Plan scoping), so every
question uses gen_worksheets.mc() via the local Q() helper below, which
always puts the correct answer in slot 0 while drafting -- _rebalance()
then shuffles each worksheet's answer positions across A/B/C/D afterward
so there is no bias toward one index, matching the convention used in
gen_grade3_days181_187.py's _rebalance_answer_positions().

No embedded straight double-quotes or apostrophes anywhere in title/q/
options text -- contractions and possessives are dropped entirely (e.g.
"does not" not "doesnt", "oclock" not "o'clock", "Canadas" not "Canada's"),
matching the convention established across the day-based Grade 3 content.

Invocation:
  cd ~/gradesbooster && python3 gen_grade3_worksheets.py
followed by:
  cd ~/gradesbooster && python3 build_worksheets_json.py --grade 3
"""
import sys
sys.path.insert(0, '.')
from gen_worksheets import mc, worksheet, write_worksheets


def Q(q, c, w1, w2, w3):
    """One mc() question drafted with the correct answer in slot 0;
    _rebalance() shuffles positions across the whole worksheet set later."""
    return mc(q, [c, w1, w2, w3], 0)


# ---------------------------------------------------------------------------
# LANGUAGE
# ---------------------------------------------------------------------------

L1 = worksheet('Language', 1, 'Nouns and Pronouns Practice', [
    Q('Which word is a common noun?', 'dog', 'Toronto', 'Monday', 'Sarah'),
    Q('Which word is a proper noun?', 'Ottawa', 'city', 'river', 'teacher'),
    Q('Which word is a pronoun?', 'she', 'jump', 'quickly', 'table'),
    Q('What does a pronoun do in a sentence?', 'replaces a noun', 'describes an action', 'joins two clauses', 'names a place'),
    Q('Which sentence uses a pronoun correctly?', 'She walked to the store.', 'Store the she walked to.', 'Walked she to the store.', 'To store she the walked.'),
    Q('Which word could replace the noun Jack in a sentence?', 'he', 'run', 'blue', 'quickly'),
    Q('Which is a plural noun?', 'cats', 'cat', 'running', 'happy'),
    Q('Which is a singular noun?', 'box', 'boxes', 'children', 'geese'),
    Q('Which word is an irregular plural noun?', 'children', 'dogs', 'cats', 'books'),
    Q('Which pronoun could replace the boy and the girl?', 'they', 'it', 'he', 'she'),
    Q('Which word is a collective noun naming a group?', 'team', 'player', 'ball', 'coach'),
    Q('Which sentence has the noun used correctly as the subject?', 'The dog barked loudly.', 'Barked loudly the dog.', 'Loudly barked the dog.', 'Dog the barked loudly.'),
    Q('Which word is a possessive pronoun?', 'his', 'run', 'jump', 'quick'),
    Q('What is the plural form of the noun leaf?', 'leaves', 'leafs', 'leaf', 'leafes'),
    Q('Which noun names a place?', 'park', 'jump', 'happy', 'quickly'),
])

L2 = worksheet('Language', 2, 'Verbs and Simple Tenses', [
    Q('Which word is a verb?', 'run', 'blue', 'happy', 'slowly'),
    Q('Which sentence uses the past tense correctly?', 'She walked to school yesterday.', 'She walk to school yesterday.', 'She walks to school tomorrow.', 'She will walked to school.'),
    Q('Which sentence uses the future tense correctly?', 'He will visit his cousin tomorrow.', 'He visit his cousin tomorrow.', 'He visited his cousin tomorrow.', 'He visiting his cousin tomorrow.'),
    Q('Which word is the present tense verb in this sentence: The birds sing every morning?', 'sing', 'birds', 'every', 'morning'),
    Q('What is the past tense of the verb jump?', 'jumped', 'jumping', 'jumps', 'jump'),
    Q('What is the past tense of the verb run?', 'ran', 'runned', 'running', 'runs'),
    Q('Which sentence is written in the present tense?', 'The sun shines brightly today.', 'The sun shone brightly yesterday.', 'The sun will shine brightly tomorrow.', 'The sun had shone brightly.'),
    Q('Which word is a helping verb in this sentence: She is reading a book?', 'is', 'reading', 'book', 'she'),
    Q('Which word is a verb that shows action?', 'swim', 'green', 'tall', 'happy'),
    Q('What is the past tense of the verb see?', 'saw', 'seed', 'seeing', 'sees'),
    Q('Which sentence uses a verb correctly to show something happening now?', 'I am eating lunch.', 'I eating lunch tomorrow.', 'I ate lunch will.', 'I eat lunch yesterday.'),
    Q('Which word is the verb in this sentence: The children played outside all afternoon?', 'played', 'children', 'outside', 'afternoon'),
    Q('What is the past tense of the verb go?', 'went', 'goed', 'going', 'goes'),
    Q('Which sentence correctly uses the verb to be in the present tense?', 'They are happy today.', 'They was happy today.', 'They be happy today.', 'They is happy today.'),
    Q('What do we call a word that describes when an action already happened?', 'past tense', 'future tense', 'present tense', 'no tense'),
])

L3 = worksheet('Language', 3, 'Adjectives and Adverbs', [
    Q('Which word is an adjective?', 'tall', 'run', 'quickly', 'jump'),
    Q('Which word describes the noun in this sentence: The fluffy cat slept all day?', 'fluffy', 'cat', 'slept', 'day'),
    Q('Which word is an adverb?', 'quickly', 'happy', 'green', 'table'),
    Q('Which word tells how an action is done in this sentence: She sang loudly at the concert?', 'loudly', 'sang', 'concert', 'she'),
    Q('Which adjective would best describe a mountain that is very tall?', 'towering', 'tiny', 'quiet', 'soft'),
    Q('Which sentence uses an adverb correctly?', 'He ran quickly to catch the bus.', 'He ran quick to catch the bus.', 'He quick ran to the bus catch.', 'Quickly he to catch ran bus the.'),
    Q('Which word compares two things and ends in -er?', 'taller', 'tall', 'tallest', 'tallness'),
    Q('Which word compares three or more things and ends in -est?', 'fastest', 'fast', 'faster', 'fastly'),
    Q('Which word is an adjective that describes colour?', 'purple', 'jump', 'walk', 'sing'),
    Q('Which word is an adverb that tells when something happens?', 'yesterday', 'green', 'soft', 'loud'),
    Q('Which sentence has an adjective describing the noun ball?', 'The red ball rolled away.', 'The ball rolled the red away.', 'Red rolled away the ball.', 'Away the red rolled ball.'),
    Q('Which word describes how something feels to touch?', 'soft', 'quickly', 'slowly', 'often'),
    Q('Which word is an adverb telling where something happens?', 'outside', 'green', 'tall', 'quiet'),
    Q('Which sentence uses an adjective before a noun correctly?', 'She wore a bright yellow jacket.', 'She wore a jacket bright yellow.', 'Bright she wore yellow a jacket.', 'Yellow bright a jacket she wore.'),
    Q('Which word describes a sound that is very loud?', 'thunderous', 'whispering', 'gentle', 'quiet'),
])

L4 = worksheet('Language', 4, 'Sentence Types and End Punctuation', [
    Q('Which punctuation mark ends a statement?', 'a period', 'a question mark', 'an exclamation mark', 'a comma'),
    Q('Which punctuation mark ends a question?', 'a question mark', 'a period', 'an exclamation mark', 'a comma'),
    Q('Which punctuation mark shows strong feeling?', 'an exclamation mark', 'a period', 'a question mark', 'a comma'),
    Q('Which sentence is a question?', 'Where is the library?', 'The library is closed today.', 'Go to the library now.', 'What a great library this is!'),
    Q('Which sentence is a command?', 'Please close the door.', 'Is the door closed?', 'The door is closed.', 'What a big door!'),
    Q('Which sentence is an exclamation?', 'What a beautiful sunset!', 'The sunset is beautiful.', 'Is the sunset beautiful?', 'Watch the sunset carefully.'),
    Q('Which sentence is a statement?', 'The library opens at nine.', 'Does the library open at nine?', 'Open the library now.', 'What time does the library open!'),
    Q('What do we call a group of words that expresses a complete thought?', 'a sentence', 'a fragment', 'a paragraph', 'a syllable'),
    Q('Which sentence begins with a capital letter and is punctuated correctly?', 'The dog ran fast.', 'the dog ran fast.', 'THE DOG ran fast', 'the Dog ran Fast.'),
    Q('Which word begins every sentence with a capital letter?', 'the first word', 'the last word', 'a random word', 'no word'),
    Q('Which sentence uses a comma correctly in a list?', 'I packed apples, bananas, and grapes.', 'I packed apples bananas and, grapes.', 'I, packed apples bananas and grapes.', 'I packed, apples bananas and grapes.'),
    Q('What type of sentence gives an order or a request?', 'an imperative sentence', 'a question', 'an exclamation', 'a statement'),
    Q('Which sentence correctly asks a question?', 'Can you help me with this?', 'You can help me with this.', 'Help me with this now.', 'What great help this is!'),
    Q('Which end mark best fits: I cannot believe we won the game', 'an exclamation mark', 'a period', 'a question mark', 'a comma'),
    Q('What is the purpose of a period at the end of a sentence?', 'to show the sentence has ended', 'to show excitement', 'to ask a question', 'to separate items in a list'),
])

L5 = worksheet('Language', 5, 'Reading for Main Idea and Details', [
    Q('What is the main idea of a paragraph?', 'the most important point the writer is making', 'a small unimportant detail', 'the title of the story', 'the last word in the paragraph'),
    Q('What are supporting details used for?', 'to give more information about the main idea', 'to confuse the reader', 'to change the topic completely', 'to end the story'),
    Q('Where is the main idea often found in a paragraph?', 'in the first or last sentence', 'in the middle of a random word', 'only in the title', 'it is never written down'),
    Q('If a paragraph is about how bees make honey, what is likely the main idea?', 'bees work together to make honey', 'bees are afraid of flowers', 'bees never leave their hive', 'bees cannot fly'),
    Q('Which is an example of a supporting detail rather than a main idea?', 'bees visit many flowers to collect nectar', 'bees make honey', 'this paragraph is about honey', 'bees are insects'),
    Q('Why do readers look for the main idea when reading?', 'to understand what the passage is mostly about', 'to skip the entire passage', 'to find spelling mistakes', 'to count the words'),
    Q('What skill helps a reader summarize a story in a few sentences?', 'identifying the main idea and key details', 'memorizing every single word', 'ignoring the ending', 'reading only the title'),
    Q('If a passage lists three reasons why trees are helpful, what would be a good main idea sentence?', 'trees provide many benefits', 'trees are always green', 'trees never grow tall', 'trees have no roots'),
    Q('What is a detail?', 'a small piece of information that supports the main idea', 'the entire passage', 'a made up fact', 'the name of the author'),
    Q('Which strategy helps identify the main idea in a nonfiction article?', 'asking what the article is mostly about', 'counting the number of pages', 'looking only at the pictures', 'skipping the introduction'),
    Q('Why are headings helpful when reading nonfiction text?', 'they hint at the main idea of a section', 'they replace the need to read', 'they are always incorrect', 'they contain no useful information'),
    Q('What might happen if a reader only remembers small details and not the main idea?', 'they may not understand the overall point of the text', 'they will remember everything perfectly', 'the text will make more sense', 'they will read faster'),
    Q('Which sentence best states a main idea rather than a detail?', 'Dogs make loyal and helpful pets.', 'A dog has four legs.', 'Some dogs are brown.', 'A puppy is a baby dog.'),
    Q('What can readers do after finishing a passage to check they understood the main idea?', 'summarize the passage in their own words', 'forget the passage completely', 'memorize every word exactly', 'read a different book instead'),
    Q('Why is finding the main idea an important reading skill?', 'it helps readers understand and remember what they read', 'it has no real purpose', 'it only matters for math', 'it replaces the need to read carefully'),
])

L6 = worksheet('Language', 6, 'Story Elements and Characters', [
    Q('Who is the main character in a story?', 'the character the story mostly focuses on', 'a character who appears only once', 'the author of the story', 'the title of the book'),
    Q('What is the setting of a story?', 'the time and place where the story happens', 'the list of characters', 'the main problem in the story', 'the final sentence of the story'),
    Q('What is the plot of a story?', 'the sequence of events that happen in the story', 'the cover of the book', 'the name of the author', 'the price of the book'),
    Q('What is a problem in a story often called?', 'the conflict', 'the setting', 'the resolution', 'the title'),
    Q('What is the resolution of a story?', 'how the problem gets solved at the end', 'the very first sentence', 'the name of the main character', 'the cover illustration'),
    Q('Which word describes a character who helps the main character?', 'a supporting character', 'the setting', 'the theme', 'the title'),
    Q('What is a theme in a story?', 'the underlying message or lesson of the story', 'the exact number of pages', 'the name of the illustrator', 'the price of the book'),
    Q('Which of these is an example of a setting?', 'a small village during winter', 'a brave young girl', 'a hidden treasure', 'a difficult decision'),
    Q('What do we call the character who often causes the problem in a story?', 'the antagonist', 'the protagonist', 'the narrator', 'the illustrator'),
    Q('What do we call the main character who the story follows?', 'the protagonist', 'the antagonist', 'the setting', 'the theme'),
    Q('Why do authors include a setting in a story?', 'to help readers picture where and when the story takes place', 'to make the story shorter', 'settings are never included in stories', 'to confuse the reader'),
    Q('What might a character learn by the end of a story that shows the theme?', 'an important lesson about life or people', 'the exact date the story was written', 'the price of the book', 'the name of the publisher'),
    Q('What is dialogue in a story?', 'the words characters speak to each other', 'the title of the book', 'the setting description', 'the name of the author'),
    Q('Which part of a story usually introduces the characters and setting?', 'the beginning', 'the resolution', 'the climax', 'the final sentence'),
    Q('Why is understanding story elements helpful to a reader?', 'it helps readers understand how a story is built and what it means', 'it makes reading longer and harder', 'it has no real use', 'it only matters for the author'),
])

L7 = worksheet('Language', 7, 'Vocabulary and Context Clues', [
    Q('What is a context clue?', 'a hint in the surrounding text that helps explain a word meaning', 'a picture with no words', 'a random number in the text', 'the title of the book'),
    Q('If a sentence says the enormous elephant was the biggest animal at the zoo, what does enormous likely mean?', 'very large', 'very small', 'very loud', 'very quiet'),
    Q('What is a synonym?', 'a word that means almost the same as another word', 'a word that means the opposite of another word', 'a word with no meaning', 'a punctuation mark'),
    Q('What is an antonym?', 'a word that means the opposite of another word', 'a word that means the same as another word', 'a type of noun', 'a type of verb'),
    Q('Which word is a synonym for happy?', 'joyful', 'sad', 'angry', 'tired'),
    Q('Which word is an antonym for fast?', 'slow', 'quick', 'speedy', 'rapid'),
    Q('What is a homophone?', 'a word that sounds the same as another word but has a different meaning', 'a word that is spelled the same and means the same thing', 'a punctuation mark', 'a type of sentence'),
    Q('Which pair of words are homophones?', 'flower and flour', 'big and small', 'happy and sad', 'run and walk'),
    Q('What can help a reader figure out an unfamiliar word without a dictionary?', 'looking at clues in the surrounding sentence', 'skipping the word forever', 'closing the book', 'ignoring the sentence completely'),
    Q('If a sentence says the frigid winter air made everyone shiver, what does frigid likely mean?', 'very cold', 'very warm', 'very colourful', 'very quiet'),
    Q('What is a base word?', 'the simplest form of a word before adding endings', 'a punctuation mark', 'a type of sentence', 'a made up word'),
    Q('What is added to the base word play to show it happened in the past?', 'an -ed ending, making played', 'an -ing ending', 'an -s ending', 'an -er ending'),
    Q('Which word means almost the same as the word tiny?', 'small', 'huge', 'giant', 'enormous'),
    Q('Why is building vocabulary important for a reader?', 'it helps readers understand more words and ideas in what they read', 'it makes reading impossible', 'it has no benefit to readers', 'it only helps with math'),
    Q('What is a prefix?', 'a group of letters added to the beginning of a word to change its meaning', 'a group of letters added to the end of a word', 'a type of punctuation', 'a type of sentence'),
])

L8 = worksheet('Language', 8, 'Paragraph Writing and Topic Sentences', [
    Q('What is a topic sentence?', 'a sentence that tells the main idea of a paragraph', 'the last word in a paragraph', 'a sentence with no meaning', 'a question with no answer'),
    Q('Where is a topic sentence usually placed in a paragraph?', 'at the beginning', 'only at the very end', 'in the middle of a word', 'it is never included'),
    Q('What do supporting sentences do in a paragraph?', 'add details that explain the topic sentence', 'change the topic completely', 'repeat the title over and over', 'end the paragraph early'),
    Q('What is a closing sentence used for?', 'to wrap up the ideas in a paragraph', 'to introduce a brand new topic', 'to ask an unrelated question', 'to end the paragraph mid word'),
    Q('Which is an example of a strong topic sentence for a paragraph about dogs?', 'Dogs make wonderful and loyal pets.', 'The sky was cloudy that day.', 'Numbers can be added together.', 'My favourite colour is green.'),
    Q('What should every sentence in a paragraph relate to?', 'the main topic of the paragraph', 'a completely different topic', 'nothing at all', 'only the last sentence'),
    Q('Why do writers plan their paragraph before writing?', 'to organize their ideas clearly', 'to make the paragraph confusing', 'planning is never useful', 'to avoid writing anything'),
    Q('What is the purpose of revising a paragraph after writing it?', 'to improve and fix mistakes', 'to make it longer with random words', 'to remove the topic sentence', 'revising is never necessary'),
    Q('Which sentence would not belong in a paragraph about the ocean?', 'My favourite pizza topping is cheese.', 'The ocean is home to many fish.', 'Waves crash against the shore.', 'The ocean covers most of the earth.'),
    Q('What does it mean for a paragraph to be well organized?', 'the ideas flow logically from one to the next', 'the sentences are in a random order', 'the paragraph has no topic sentence', 'every sentence is about a different topic'),
    Q('What is the first step in the writing process?', 'planning or brainstorming ideas', 'publishing the final copy', 'ignoring the topic', 'skipping straight to editing'),
    Q('What does editing a paragraph involve?', 'checking for spelling and grammar mistakes', 'adding random unrelated sentences', 'deleting the whole paragraph', 'ignoring all mistakes'),
    Q('Why might a writer use describing words in a paragraph?', 'to help the reader picture what is being described', 'describing words are never useful', 'to make the paragraph shorter', 'to confuse the reader on purpose'),
    Q('What is a paragraph?', 'a group of sentences about one main topic', 'a single word', 'a list of unrelated topics', 'a type of punctuation mark'),
    Q('Why is it helpful to reread a paragraph after writing it?', 'to check that it makes sense and flows well', 'rereading is never helpful', 'to find a completely new topic', 'to make it longer with no purpose'),
])

L9 = worksheet('Language', 9, 'Spelling Patterns and Word Families', [
    Q('Which word belongs to the same word family as cat, hat, and bat?', 'mat', 'dog', 'pen', 'run'),
    Q('What sound do the letters ch make in the word chair?', 'a ch sound like in chip', 'a k sound like in cat', 'a sh sound like in ship', 'a silent sound'),
    Q('Which word has a long a sound?', 'cake', 'cat', 'cap', 'can'),
    Q('Which word has a short vowel sound?', 'bag', 'cake', 'rain', 'gate'),
    Q('What is added to the end of most words to make them plural?', 'an -s or -es ending', 'an -ed ending', 'an -ing ending', 'a silent letter'),
    Q('Which word is spelled correctly?', 'friend', 'freind', 'frend', 'friand'),
    Q('Which word rhymes with night?', 'light', 'nose', 'tree', 'cup'),
    Q('What do we call two letters that work together to make one sound, like sh or ch?', 'a digraph', 'a suffix', 'a prefix', 'a syllable'),
    Q('Which word has a silent letter?', 'knee', 'jump', 'run', 'swim'),
    Q('What is a syllable?', 'a beat or chunk of sound in a word', 'a punctuation mark', 'a type of sentence', 'a made up word'),
    Q('How many syllables are in the word elephant?', 'three', 'one', 'two', 'five'),
    Q('Which word ends with the same sound as the word jump?', 'stump', 'jam', 'juice', 'jelly'),
    Q('Which word is in the same word family as the word play?', 'day', 'run', 'swim', 'jump'),
    Q('What happens to the word hop when you add -ing?', 'the p is doubled to make hopping', 'nothing changes, it stays hop', 'the h is removed', 'the o becomes an a'),
    Q('Which word uses the correct spelling pattern for a long e sound?', 'beach', 'baech', 'beech', 'bech'),
])

L10 = worksheet('Language', 10, 'Oral Communication and Listening Skills', [
    Q('What does it mean to be an active listener?', 'paying close attention to the speaker', 'talking the entire time', 'ignoring the speaker', 'looking at a phone while someone talks'),
    Q('Why is eye contact helpful when listening to someone speak?', 'it shows the speaker you are paying attention', 'it has no effect on communication', 'it is considered rude in every situation', 'it stops you from hearing anything'),
    Q('What should you do before speaking during a group discussion?', 'wait for your turn to speak', 'interrupt whenever you want', 'speak over everyone else', 'refuse to let anyone else speak'),
    Q('What is the purpose of asking a clarifying question?', 'to better understand what someone said', 'to confuse the speaker', 'to change the subject completely', 'to end the conversation immediately'),
    Q('What does it mean to speak clearly during a presentation?', 'using a good pace and volume so others can understand', 'mumbling quietly', 'speaking as fast as possible', 'whispering the entire time'),
    Q('Why is it important to take turns during a conversation?', 'so everyone has a chance to share their ideas', 'so only one person ever speaks', 'taking turns is not important', 'to make the conversation shorter'),
    Q('What is a good way to show you are listening to a partner?', 'nodding and responding to what they say', 'looking away and staying silent', 'talking about something unrelated', 'walking away while they speak'),
    Q('What should a speaker do to help an audience understand a presentation?', 'speak clearly and organize their ideas', 'mumble and speak very fast', 'use no organization at all', 'avoid looking at the audience'),
    Q('Why might a speaker use gestures during a presentation?', 'to help emphasize their ideas', 'gestures are never helpful', 'to confuse the audience', 'to avoid speaking clearly'),
    Q('What is the purpose of a group discussion?', 'to share ideas and learn from one another', 'to argue without listening', 'to avoid sharing any ideas', 'to speak over everyone else'),
    Q('What should you do if you disagree with someone during a discussion?', 'respectfully share your different opinion', 'yell at the other person', 'ignore them completely', 'refuse to let them speak again'),
    Q('Why is it helpful to summarize what a speaker said?', 'it shows understanding and helps remember key points', 'summarizing is never useful', 'it always confuses the listener', 'it replaces the need to listen at all'),
    Q('What does volume mean when speaking to a group?', 'how loud or soft your voice is', 'how fast you speak', 'how many words you use', 'the topic you are speaking about'),
    Q('Why should a listener avoid interrupting a speaker?', 'it allows the speaker to finish their complete thought', 'interrupting is always encouraged', 'it helps the speaker speak faster', 'it has no effect on communication'),
    Q('What is one benefit of practising a presentation before giving it?', 'it helps the speaker feel more confident and prepared', 'practising has no benefit', 'it makes the presentation worse', 'it is a waste of time'),
])

# ---------------------------------------------------------------------------
# MATH
# ---------------------------------------------------------------------------

M1 = worksheet('Math', 1, 'Place Value to Thousands', [
    Q('In the number 4726, what digit is in the tens place?', '2', '4', '7', '6'),
    Q('In the number 3581, what digit is in the hundreds place?', '5', '3', '8', '1'),
    Q('In the number 9052, what digit is in the thousands place?', '9', '0', '5', '2'),
    Q('What is the value of the digit 6 in the number 6420?', 'six thousand', 'six hundred', 'six tens', 'six ones'),
    Q('Which number has a 7 in the hundreds place?', '1732', '1372', '1273', '1327'),
    Q('What is 3000 plus 400 plus 20 plus 5 written as a standard number?', '3425', '3245', '3452', '3524'),
    Q('Which number is greater, 4521 or 4512?', '4521', '4512', 'they are equal', 'cannot be determined'),
    Q('What is the expanded form of 5236?', '5000 plus 200 plus 30 plus 6', '500 plus 20 plus 3 plus 6', '5000 plus 20 plus 300 plus 6', '50 plus 200 plus 30 plus 6'),
    Q('Which digit has the greatest value in the number 8134?', '8', '1', '3', '4'),
    Q('How many hundreds are in the number 2500?', '25 hundreds', '250 hundreds', '2 hundreds', '5 hundreds'),
    Q('What is 7000 plus 90 plus 3 written in standard form?', '7093', '7930', '7903', '793'),
    Q('Rounding 4867 to the nearest hundred gives which number?', '4900', '4800', '4870', '5000'),
    Q('Rounding 3241 to the nearest thousand gives which number?', '3000', '4000', '3200', '3500'),
    Q('Which number comes between 2999 and 3001?', '3000', '2998', '3002', '3010'),
    Q('What is the place value of the digit 4 in the number 1489?', 'hundreds', 'tens', 'ones', 'thousands'),
])

M2 = worksheet('Math', 2, 'Addition and Subtraction Strategies', [
    Q('What is 245 plus 132?', '377', '367', '387', '357'),
    Q('What is 528 minus 214?', '314', '324', '304', '334'),
    Q('Which strategy involves breaking numbers into tens and ones to add them?', 'decomposing', 'multiplying', 'dividing', 'skip counting'),
    Q('What is 430 minus 120?', '310', '300', '320', '340'),
    Q('What is 275 plus 125?', '400', '390', '410', '380'),
    Q('Which number sentence shows the correct way to check subtraction using addition?', 'If 15 minus 7 equals 8, then 8 plus 7 equals 15.', 'If 15 minus 7 equals 8, then 8 minus 7 equals 15.', 'If 15 minus 7 equals 8, then 15 plus 7 equals 8.', 'If 15 minus 7 equals 8, then 7 minus 8 equals 15.'),
    Q('What is the sum of 356 and 214?', '570', '560', '580', '550'),
    Q('When adding 199 plus 47, which strategy makes the problem easier?', 'adding 200 and 47 then subtracting 1', 'multiplying both numbers', 'ignoring the ones digit', 'rounding both numbers down'),
    Q('What is 900 minus 356?', '544', '554', '534', '564'),
    Q('What is 128 plus 349?', '477', '467', '487', '478'),
    Q('Estimate the sum of 298 and 403 by rounding to the nearest hundred.', '700', '600', '800', '750'),
    Q('What is 763 minus 289?', '474', '484', '464', '494'),
    Q('If you have 8 tens and 5 ones, what number do you have?', '85', '58', '805', '850'),
    Q('What is 500 minus 275?', '225', '235', '215', '245'),
    Q('Which is the correct way to regroup when subtracting 62 minus 38?', 'regroup 1 ten into 10 ones', 'regroup 1 one into 10 tens', 'no regrouping is needed', 'regroup the tens into hundreds'),
])

M3 = worksheet('Math', 3, 'Multiplication Facts to Ten', [
    Q('What is 3 times 4?', '12', '7', '10', '15'),
    Q('What is 6 times 5?', '30', '25', '35', '20'),
    Q('What is 7 times 2?', '14', '12', '16', '9'),
    Q('What is 8 times 3?', '24', '21', '27', '18'),
    Q('What is 9 times 4?', '36', '32', '40', '27'),
    Q('What is 5 times 5?', '25', '20', '30', '15'),
    Q('What is 10 times 6?', '60', '50', '70', '16'),
    Q('What is 4 times 4?', '16', '12', '20', '8'),
    Q('What is 7 times 7?', '49', '42', '56', '40'),
    Q('What is 2 times 9?', '18', '16', '20', '11'),
    Q('Which multiplication fact matches an array of 3 rows with 6 in each row?', '3 times 6 equals 18', '3 plus 6 equals 9', '6 times 6 equals 36', '3 times 3 equals 9'),
    Q('What is 8 times 8?', '64', '56', '72', '48'),
    Q('What is 6 times 6?', '36', '30', '42', '24'),
    Q('What is 9 times 9?', '81', '72', '90', '63'),
    Q('What is 5 times 8?', '40', '35', '45', '30'),
])

M4 = worksheet('Math', 4, 'Division Facts and Sharing Equally', [
    Q('What is 12 divided by 3?', '4', '3', '6', '5'),
    Q('What is 20 divided by 4?', '5', '4', '6', '8'),
    Q('What is 18 divided by 2?', '9', '8', '10', '6'),
    Q('What is 24 divided by 6?', '4', '3', '6', '8'),
    Q('What is 30 divided by 5?', '6', '5', '7', '10'),
    Q('If 15 candies are shared equally among 3 friends, how many candies does each friend get?', '5', '3', '4', '6'),
    Q('What is 27 divided by 3?', '9', '6', '8', '12'),
    Q('What is 40 divided by 8?', '5', '4', '6', '8'),
    Q('What is 36 divided by 4?', '9', '8', '7', '12'),
    Q('If 21 stickers are shared equally among 7 students, how many stickers does each student get?', '3', '2', '4', '5'),
    Q('What is 45 divided by 5?', '9', '8', '10', '7'),
    Q('What is 16 divided by 2?', '8', '6', '9', '7'),
    Q('What is 49 divided by 7?', '7', '6', '8', '9'),
    Q('If 32 apples are packed equally into 4 boxes, how many apples go in each box?', '8', '6', '7', '9'),
    Q('What is 63 divided by 9?', '7', '6', '8', '9'),
])

M5 = worksheet('Math', 5, 'Understanding Fractions', [
    Q('What fraction represents one part out of four equal parts?', 'one fourth', 'one half', 'one third', 'one whole'),
    Q('What is the bottom number of a fraction called?', 'the denominator', 'the numerator', 'the whole number', 'the remainder'),
    Q('What is the top number of a fraction called?', 'the numerator', 'the denominator', 'the whole number', 'the remainder'),
    Q('Which fraction is equal to one half?', 'two fourths', 'one fourth', 'three fourths', 'one third'),
    Q('Which fraction is greater, one half or one fourth?', 'one half', 'one fourth', 'they are equal', 'cannot be determined'),
    Q('If a pizza is cut into 6 equal slices and 2 are eaten, what fraction was eaten?', 'two sixths', 'two thirds', 'one sixth', 'six halves'),
    Q('What does the denominator tell you about a fraction?', 'how many equal parts the whole is divided into', 'how many parts are shaded', 'the value of the whole number', 'nothing important'),
    Q('Which fraction represents a whole shape divided into 3 equal parts with all parts shaded?', 'three thirds', 'one third', 'two thirds', 'one half'),
    Q('What is one whole written as a fraction with a denominator of 4?', 'four fourths', 'one fourth', 'two fourths', 'three fourths'),
    Q('Which fraction is the same as half of a whole?', 'two fourths', 'one fourth', 'three fourths', 'one third'),
    Q('If you shade 3 out of 8 equal parts of a shape, what fraction is shaded?', 'three eighths', 'three fourths', 'eight thirds', 'one eighth'),
    Q('Which is smaller, one third or one sixth?', 'one sixth', 'one third', 'they are equal', 'cannot be determined'),
    Q('What do we call a fraction where the numerator and denominator are the same number?', 'one whole', 'one half', 'zero', 'an improper number'),
    Q('Which fraction shows a whole divided into two equal parts with one part shaded?', 'one half', 'one third', 'one fourth', 'two thirds'),
    Q('What is the fraction name for one part out of three equal parts?', 'one third', 'one fourth', 'one half', 'one fifth'),
])

M6 = worksheet('Math', 6, 'Measuring Length and Mass', [
    Q('Which unit would you use to measure the length of a pencil?', 'centimetres', 'kilometres', 'kilograms', 'litres'),
    Q('Which unit would you use to measure the distance between two cities?', 'kilometres', 'centimetres', 'grams', 'millilitres'),
    Q('Which tool is used to measure length?', 'a ruler', 'a scale', 'a thermometer', 'a clock'),
    Q('Which unit is used to measure how heavy an object is?', 'grams', 'centimetres', 'metres', 'litres'),
    Q('Which tool is used to measure mass?', 'a balance scale', 'a ruler', 'a thermometer', 'a measuring cup'),
    Q('How many centimetres are in one metre?', '100', '10', '1000', '50'),
    Q('Which object is likely to have a mass measured in kilograms rather than grams?', 'a large bag of rice', 'a paperclip', 'a single grape', 'a small feather'),
    Q('Which unit would best measure the height of a door?', 'metres', 'kilometres', 'grams', 'litres'),
    Q('If a book has a mass of 500 grams, about how many grams would two identical books have together?', '1000 grams', '500 grams', '250 grams', '2000 grams'),
    Q('Which is longer, 1 metre or 90 centimetres?', '1 metre', '90 centimetres', 'they are equal', 'cannot be determined'),
    Q('Which unit would you use to measure the mass of an apple?', 'grams', 'kilometres', 'litres', 'metres'),
    Q('What tool would help you compare the mass of two objects?', 'a balance scale', 'a ruler', 'a clock', 'a thermometer'),
    Q('Which is a reasonable length for a school bus?', 'about 12 metres', 'about 12 centimetres', 'about 12 kilometres', 'about 12 millimetres'),
    Q('If a string is 45 centimetres long, about how many metres is that?', 'less than 1 metre', 'more than 2 metres', 'exactly 1 metre', 'exactly 4 metres'),
    Q('Which unit is smaller, a centimetre or a metre?', 'a centimetre', 'a metre', 'they are the same size', 'cannot be determined'),
])

M7 = worksheet('Math', 7, 'Telling Time and Counting Money', [
    Q('How many minutes are in one hour?', '60', '30', '100', '12'),
    Q('If the short hand points to 3 and the long hand points to 12, what time is it?', '3 oclock', '12 oclock', '6 oclock', '9 oclock'),
    Q('How many hours are in one day?', '24', '12', '60', '7'),
    Q('If it is 2 oclock and 30 minutes pass, what time is it?', '2:30', '3:00', '2:00', '1:30'),
    Q('What coin is worth 25 cents?', 'a quarter', 'a dime', 'a nickel', 'a penny'),
    Q('What coin is worth 10 cents?', 'a dime', 'a quarter', 'a nickel', 'a penny'),
    Q('What coin is worth 5 cents?', 'a nickel', 'a dime', 'a quarter', 'a penny'),
    Q('How many pennies make one dollar?', '100', '10', '25', '50'),
    Q('If you have 2 quarters and 1 dime, how much money do you have?', '60 cents', '50 cents', '70 cents', '35 cents'),
    Q('How many minutes are in half an hour?', '30', '15', '45', '60'),
    Q('If a movie starts at 4:00 and lasts 1 hour, what time does it end?', '5:00', '4:30', '3:00', '6:00'),
    Q('How many days are in one week?', '7', '5', '10', '30'),
    Q('If you buy an item for 3 dollars and pay with a 5 dollar bill, how much change should you get?', '2 dollars', '1 dollar', '3 dollars', '5 dollars'),
    Q('What is a reasonable amount of time to brush your teeth?', 'about 2 minutes', 'about 2 hours', 'about 2 seconds', 'about 2 days'),
    Q('How many months are in one year?', '12', '10', '6', '24'),
])

M8 = worksheet('Math', 8, 'Two Dimensional Shapes', [
    Q('How many sides does a triangle have?', '3', '4', '5', '6'),
    Q('How many sides does a rectangle have?', '4', '3', '5', '6'),
    Q('What is a shape with 5 sides called?', 'a pentagon', 'a hexagon', 'a triangle', 'an octagon'),
    Q('What is a shape with 6 sides called?', 'a hexagon', 'a pentagon', 'a heptagon', 'a square'),
    Q('What makes a square different from a rectangle that is not a square?', 'a square has four equal sides', 'a square has three sides', 'a square has no sides', 'a square has no corners'),
    Q('How many corners does a triangle have?', '3', '4', '2', '5'),
    Q('Which shape has no straight sides?', 'a circle', 'a square', 'a triangle', 'a rectangle'),
    Q('What is a shape with 8 sides called?', 'an octagon', 'a hexagon', 'a pentagon', 'a heptagon'),
    Q('How many sides does an octagon have?', '8', '6', '7', '9'),
    Q('What do we call the straight line that makes up part of a shape?', 'a side', 'a corner', 'a curve', 'an angle'),
    Q('What do we call the point where two sides of a shape meet?', 'a vertex, or corner', 'a side', 'a curve', 'an edge'),
    Q('Which of these shapes is a quadrilateral?', 'a rectangle', 'a triangle', 'a pentagon', 'a hexagon'),
    Q('How many sides does a quadrilateral have?', '4', '3', '5', '6'),
    Q('Which shape has all sides and angles equal?', 'a square', 'a rectangle that is not a square', 'a triangle with different sides', 'a random four sided shape'),
    Q('What is the name for a closed shape made of straight sides?', 'a polygon', 'a circle', 'a curve', 'a line'),
])

M9 = worksheet('Math', 9, 'Patterns and Simple Equations', [
    Q('What comes next in the pattern 2, 4, 6, 8?', '10', '9', '12', '7'),
    Q('What comes next in the pattern 5, 10, 15, 20?', '25', '22', '30', '24'),
    Q('What is the missing number in 3 plus a number equals 10?', '7', '6', '8', '13'),
    Q('What is the missing number in a number minus 5 equals 12?', '17', '7', '15', '20'),
    Q('What comes next in the pattern 100, 90, 80, 70?', '60', '50', '65', '75'),
    Q('What is the rule for the pattern 1, 3, 5, 7, 9?', 'add 2 each time', 'add 1 each time', 'subtract 2 each time', 'multiply by 2 each time'),
    Q('What is the missing number in 4 times a number equals 20?', '5', '4', '6', '16'),
    Q('What comes next in the pattern 1, 2, 4, 8, 16?', '32', '24', '20', '18'),
    Q('What is the missing number in 15 divided by a number equals 3?', '5', '3', '4', '45'),
    Q('What is the rule for the pattern 20, 17, 14, 11?', 'subtract 3 each time', 'subtract 2 each time', 'add 3 each time', 'divide by 2 each time'),
    Q('If a pattern grows by adding 4 each time starting at 3, what are the first four terms?', '3, 7, 11, 15', '3, 4, 8, 12', '3, 6, 9, 12', '3, 7, 10, 14'),
    Q('What is the missing number in 9 plus a number equals 15?', '6', '5', '7', '24'),
    Q('What comes next in the pattern 2, 4, 8, 16?', '32', '20', '24', '18'),
    Q('What is the missing value in the equation 6 times 3?', '18', '16', '21', '9'),
    Q('What comes next in the shrinking pattern 50, 40, 30, 20?', '10', '15', '25', '0'),
])

M10 = worksheet('Math', 10, 'Data, Graphs, and Probability', [
    Q('What is a bar graph used for?', 'comparing amounts using bars of different heights', 'writing a story', 'measuring temperature', 'telling time'),
    Q('What is a pictograph used for?', 'showing data using pictures or symbols', 'measuring length', 'telling time', 'writing sentences'),
    Q('What does the key on a pictograph explain?', 'what each picture or symbol represents', 'the title of the graph', 'the names of the students', 'the date the graph was made'),
    Q('If a bar graph shows that 8 students like apples and 5 like oranges, how many more students like apples?', '3 more students', '13 more students', '5 more students', '8 more students'),
    Q('What is the title of a graph used for?', 'telling the reader what the graph is about', 'showing the exact numbers', 'decorating the graph', 'replacing the key'),
    Q('In probability, what does it mean for an event to be certain?', 'it will definitely happen', 'it will never happen', 'it might happen', 'it happened yesterday'),
    Q('In probability, what does it mean for an event to be impossible?', 'it will never happen', 'it will definitely happen', 'it happens sometimes', 'it already happened'),
    Q('If a bag has 5 red marbles and 5 blue marbles, what is the chance of picking a red marble?', 'an equal or fair chance', 'it is impossible', 'it is certain', 'there is no chance at all'),
    Q('What is a tally chart used for?', 'counting and recording data using tally marks', 'measuring mass', 'telling time', 'drawing pictures'),
    Q('How many tally marks are grouped together before drawing a line across them?', '5', '4', '10', '3'),
    Q('If a spinner has 4 equal sections and only 1 is red, what is the chance of landing on red?', 'a low, one out of four chance', 'a certain chance', 'an impossible chance', 'a one out of two chance'),
    Q('What does the horizontal line on a bar graph usually show?', 'the categories being compared', 'the exact temperature', 'the time of day', 'the title only'),
    Q('What does the vertical line on a bar graph usually show?', 'the number or amount for each category', 'the categories being compared', 'the date the data was collected', 'the name of the graph maker'),
    Q('If more people chose pizza than any other food on a graph, what can you conclude?', 'pizza was the most popular choice', 'pizza was the least popular choice', 'no one chose pizza', 'every food was chosen equally'),
    Q('Why do we collect and organize data into graphs?', 'to make information easier to read and compare', 'to make information harder to understand', 'graphs have no real purpose', 'to hide information from readers'),
])

# ---------------------------------------------------------------------------
# SCIENCE
# ---------------------------------------------------------------------------

Sc1 = worksheet('Science', 1, 'Plant Growth and Needs', [
    Q('What do plants need to grow?', 'sunlight, water, air, and soil', 'only darkness', 'only water', 'nothing at all'),
    Q('What part of the plant absorbs water from the soil?', 'the roots', 'the leaves', 'the petals', 'the stem tip'),
    Q('What part of the plant makes food using sunlight?', 'the leaves', 'the roots', 'the petals', 'the seeds'),
    Q('What is the process called when plants make their own food using sunlight?', 'photosynthesis', 'respiration', 'germination', 'pollination'),
    Q('What is the first stage of a plant growing from a seed called?', 'germination', 'pollination', 'photosynthesis', 'decomposition'),
    Q('What part of the plant carries water from the roots to the leaves?', 'the stem', 'the petals', 'the seeds', 'the fruit'),
    Q('Why do plants need sunlight?', 'to make food through photosynthesis', 'to stay cold', 'to grow underground only', 'plants do not need sunlight'),
    Q('What do we call the coloured part of a flower that attracts insects?', 'the petals', 'the roots', 'the stem', 'the seeds'),
    Q('What happens inside a seed before it germinates?', 'it stays dormant until it gets water and warmth', 'it grows a full plant instantly', 'nothing ever happens inside a seed', 'it turns into soil'),
    Q('Why is soil important for most plants?', 'it provides nutrients and support for roots', 'soil has no purpose for plants', 'plants never use soil', 'soil blocks sunlight from plants'),
    Q('What do we call a plant that completes its life cycle in one growing season?', 'an annual plant', 'a perennial plant', 'a fossil plant', 'a mineral plant'),
    Q('What might happen to a plant that does not get enough water?', 'it may wilt or die', 'it will grow faster than normal', 'nothing will happen', 'it will change into a different plant'),
    Q('Why do some plants grow toward a window?', 'they grow toward sunlight', 'they grow away from sunlight', 'plants cannot sense light', 'windows attract roots'),
    Q('What is pollination?', 'the transfer of pollen that helps a plant produce seeds', 'the process of a plant absorbing water', 'the process of a leaf changing colour', 'the process of soil forming'),
    Q('Why might a gardener rotate crops in a garden?', 'to keep the soil healthy for future plants', 'to make the soil less healthy', 'crop rotation has no purpose', 'to prevent any plants from growing'),
])

Sc2 = worksheet('Science', 2, 'Animal Life Cycles', [
    Q('What is a life cycle?', 'the stages an animal goes through from birth to death', 'only the moment an animal is born', 'only the moment an animal dies', 'a type of animal habitat'),
    Q('What is the second stage of a frogs life cycle after the egg?', 'a tadpole', 'an adult frog', 'a caterpillar', 'a chrysalis'),
    Q('What is the stage between a caterpillar and an adult butterfly called?', 'a chrysalis, or pupa', 'a tadpole', 'an egg', 'a larva with no other name'),
    Q('What comes first in a butterflys life cycle?', 'an egg', 'a caterpillar', 'a chrysalis', 'an adult butterfly'),
    Q('What do we call an animal that lays eggs?', 'oviparous', 'viviparous', 'carnivorous', 'herbivorous'),
    Q('What do we call an animal that gives birth to live young?', 'viviparous', 'oviparous', 'carnivorous', 'herbivorous'),
    Q('Which animal undergoes complete metamorphosis?', 'a butterfly', 'a human', 'a dog', 'a bird'),
    Q('What is metamorphosis?', 'a dramatic change in body form during an animal life cycle', 'the process of an animal eating', 'a type of animal habitat', 'a type of animal food'),
    Q('What is a young frog called before it grows legs?', 'a tadpole', 'a kit', 'a cub', 'a fawn'),
    Q('What do we call a baby dog?', 'a puppy', 'a kitten', 'a cub', 'a fawn'),
    Q('What do we call a baby cat?', 'a kitten', 'a puppy', 'a calf', 'a joey'),
    Q('What do we call a baby kangaroo?', 'a joey', 'a puppy', 'a fawn', 'a cub'),
    Q('What stage comes right after an egg hatches for many birds?', 'a chick', 'an adult bird', 'a pupa', 'a tadpole'),
    Q('Why do animals go through different stages in a life cycle?', 'each stage helps them grow and change into an adult', 'life cycles have no purpose', 'animals never change', 'all animals look the same at every stage'),
    Q('Which of these correctly orders a butterflys life cycle from start to finish?', 'egg, caterpillar, chrysalis, adult butterfly', 'adult butterfly, egg, chrysalis, caterpillar', 'chrysalis, egg, caterpillar, adult butterfly', 'caterpillar, adult butterfly, egg, chrysalis'),
])

Sc3 = worksheet('Science', 3, 'Properties of Everyday Materials', [
    Q('What are the three main states of matter?', 'solid, liquid, and gas', 'hot, cold, and warm', 'big, medium, and small', 'light, dark, and colourful'),
    Q('What state of matter has a fixed shape and volume?', 'a solid', 'a liquid', 'a gas', 'none of these'),
    Q('What state of matter takes the shape of its container but keeps the same volume?', 'a liquid', 'a solid', 'a gas', 'none of these'),
    Q('What state of matter spreads out to fill its entire container?', 'a gas', 'a solid', 'a liquid', 'none of these'),
    Q('What happens to water when it freezes?', 'it changes from a liquid into a solid', 'it changes from a gas into a liquid', 'it disappears completely', 'it changes colour permanently'),
    Q('What happens to water when it boils?', 'it changes from a liquid into a gas called water vapour', 'it changes from a solid into a liquid', 'it disappears completely', 'it turns into ice'),
    Q('Which material would be best described as flexible?', 'rubber', 'glass', 'stone', 'brick'),
    Q('Which material is a good conductor of heat?', 'metal', 'wood', 'plastic', 'rubber'),
    Q('Which material would float on water?', 'a wooden block', 'a heavy steel bolt', 'a large rock', 'a metal spoon'),
    Q('What property describes how heavy an object is for its size?', 'density', 'colour', 'texture', 'temperature'),
    Q('Which material is transparent, meaning light passes through it clearly?', 'glass', 'wood', 'brick', 'cardboard'),
    Q('What do we call a material that does not let light pass through it at all?', 'opaque', 'transparent', 'translucent', 'magnetic'),
    Q('Which of these materials is magnetic?', 'iron', 'wood', 'plastic', 'rubber'),
    Q('What happens to most materials when they are heated?', 'they can expand or change state', 'they always disappear', 'they always shrink', 'nothing ever happens'),
    Q('Why might a scientist test the properties of a material before building something?', 'to make sure the material is suitable for its purpose', 'properties have no effect on how materials are used', 'testing materials is never useful', 'to make the material heavier'),
])

Sc4 = worksheet('Science', 4, 'Forces and Stable Structures', [
    Q('What is a force?', 'a push or a pull', 'a type of material', 'a type of animal', 'a type of plant'),
    Q('What force pulls objects toward the earth?', 'gravity', 'friction', 'magnetism', 'tension'),
    Q('What force slows down or stops moving objects when two surfaces rub together?', 'friction', 'gravity', 'magnetism', 'tension'),
    Q('What makes a structure stable and less likely to fall over?', 'a wide, strong base', 'a very narrow base', 'no base at all', 'a base made only of paper'),
    Q('Why do engineers use triangles when building strong structures?', 'triangles keep their shape well under pressure', 'triangles are the weakest shape', 'triangles have no strength at all', 'triangles cannot be used in structures'),
    Q('What is the purpose of a foundation in a building?', 'to support the structure and keep it stable', 'to make the building lighter', 'foundations have no purpose', 'to decorate the building'),
    Q('Which force pulls a magnet toward a piece of metal?', 'magnetism', 'friction', 'gravity', 'tension'),
    Q('What happens to a structure with a heavy top and a narrow base?', 'it may become unstable and tip over', 'it becomes more stable', 'nothing changes', 'it becomes lighter'),
    Q('Why might builders test a model before building a full sized structure?', 'to check that the design is stable and safe', 'testing models is never useful', 'to make the structure weaker', 'models have no connection to real structures'),
    Q('What is tension in a structure?', 'a pulling or stretching force', 'a pushing force only', 'a type of material', 'a type of energy'),
    Q('What is compression in a structure?', 'a squeezing or pushing force', 'a pulling force only', 'a type of material', 'a type of energy'),
    Q('Why do bridges often use triangular supports?', 'triangles help distribute weight and add strength', 'triangles make bridges weaker', 'triangles have no effect on bridges', 'bridges never use triangles'),
    Q('What force allows a ball to roll down a ramp?', 'gravity', 'magnetism', 'friction alone', 'tension'),
    Q('Why might a wide base help a tower resist strong winds?', 'it increases stability and balance', 'a wide base makes a tower fall over faster', 'wide bases have no effect on stability', 'a wide base makes the tower lighter'),
    Q('What can increase friction between two surfaces?', 'a rougher surface texture', 'a smoother surface texture', 'removing all contact between surfaces', 'gravity increasing'),
])

Sc5 = worksheet('Science', 5, 'Light and Sound Energy', [
    Q('What is needed to see an object?', 'light', 'darkness', 'silence', 'gravity'),
    Q('What happens when light hits a mirror?', 'it reflects', 'it disappears', 'it turns into sound', 'it stops existing'),
    Q('What is a shadow?', 'a dark area formed when an object blocks light', 'a bright area formed by light', 'a type of sound', 'a type of material'),
    Q('What is sound caused by?', 'vibrations', 'light', 'gravity', 'darkness'),
    Q('How does sound travel to our ears?', 'through vibrations moving through the air', 'through complete silence', 'sound cannot travel at all', 'through darkness only'),
    Q('What happens to a shadow when an object moves closer to a light source?', 'the shadow gets bigger', 'the shadow disappears completely', 'the shadow gets smaller', 'nothing changes'),
    Q('What is pitch in sound?', 'how high or low a sound is', 'how loud a sound is', 'the colour of a sound', 'the speed of light'),
    Q('What is volume in sound?', 'how loud or soft a sound is', 'how high or low a sound is', 'the colour of a sound', 'the speed of light'),
    Q('Which material would let the most light pass through it?', 'clear glass', 'cardboard', 'wood', 'brick'),
    Q('What do we call a material that light cannot pass through at all?', 'opaque', 'transparent', 'translucent', 'magnetic'),
    Q('What causes an echo?', 'sound waves bouncing off a surface and returning', 'light bouncing off a mirror', 'gravity pulling on an object', 'friction between two surfaces'),
    Q('Why can you hear a friend talking across a room?', 'sound vibrations travel through the air to your ears', 'sound cannot travel through air', 'light carries all sound', 'vibrations never move through air'),
    Q('What happens to light when it passes through a translucent material?', 'it passes through but the material blurs what is seen', 'it is completely blocked', 'it disappears entirely', 'it turns into a sound wave'),
    Q('Why do we use light to see colours?', 'light reflects off objects and shows their colour to our eyes', 'colours exist without any light', 'darkness reveals colour better than light', 'sound waves carry colour information'),
    Q('What might happen to the pitch of a sound if a vibrating object moves faster?', 'the pitch may become higher', 'the pitch always becomes lower', 'the pitch never changes', 'the sound disappears completely'),
])

Sc6 = worksheet('Science', 6, 'Weather and the Seasons', [
    Q('What instrument measures temperature?', 'a thermometer', 'a ruler', 'a scale', 'a compass'),
    Q('What instrument measures how much rain has fallen?', 'a rain gauge', 'a thermometer', 'a compass', 'a scale'),
    Q('What instrument shows wind direction?', 'a wind vane', 'a thermometer', 'a rain gauge', 'a scale'),
    Q('How many seasons are there in a year in most of Canada?', 'four', 'two', 'three', 'six'),
    Q('What season comes after winter?', 'spring', 'summer', 'fall', 'winter again'),
    Q('What season comes after summer?', 'fall', 'winter', 'spring', 'summer again'),
    Q('What happens to many trees in the fall?', 'their leaves change colour and fall off', 'their leaves turn green for the first time', 'trees disappear completely', 'trees only grow in the fall'),
    Q('What is precipitation?', 'water that falls from clouds, such as rain or snow', 'a type of temperature', 'a type of wind', 'a type of cloud shape'),
    Q('Why does it often snow in winter rather than rain?', 'the temperature is cold enough to freeze the precipitation', 'snow only falls in summer', 'temperature has no effect on precipitation', 'snow falls because of wind alone'),
    Q('What causes wind?', 'moving air, often caused by differences in temperature', 'moving water only', 'gravity pulling on clouds', 'sound waves in the sky'),
    Q('What might a meteorologist study?', 'weather patterns and forecasts', 'only ocean animals', 'only rocks and minerals', 'only plant growth'),
    Q('Why do people wear warmer clothing in winter?', 'to stay warm in colder temperatures', 'warmer clothing makes people colder', 'clothing has no effect on temperature', 'winter is always warm'),
    Q('What is the water cycle?', 'the continuous movement of water through evaporation, condensation, and precipitation', 'a cycle that only happens in winter', 'a process with no connection to weather', 'a cycle that only involves ice'),
    Q('What happens during evaporation in the water cycle?', 'liquid water changes into water vapour', 'water vapour changes into ice', 'rain falls from clouds', 'clouds disappear completely'),
    Q('Why might farmers pay close attention to seasonal weather patterns?', 'to plan when to plant and harvest crops', 'weather has no effect on farming', 'farmers never consider weather', 'seasons never affect crops'),
])

Sc7 = worksheet('Science', 7, 'Habitats and Living Things', [
    Q('What is a habitat?', 'the natural environment where a plant or animal lives', 'a type of food', 'a type of weather', 'a type of rock'),
    Q('What do we call all the living and nonliving things interacting in an area?', 'an ecosystem', 'a food chain only', 'a habitat map', 'a weather system'),
    Q('What is a food chain?', 'a sequence showing who eats whom in a habitat', 'a list of an animals favourite foods', 'a type of weather pattern', 'a chain used to build shelters'),
    Q('What do we call an animal that only eats plants?', 'an herbivore', 'a carnivore', 'an omnivore', 'a decomposer'),
    Q('What do we call an animal that only eats other animals?', 'a carnivore', 'an herbivore', 'an omnivore', 'a decomposer'),
    Q('What do we call an animal that eats both plants and animals?', 'an omnivore', 'a carnivore', 'an herbivore', 'a decomposer'),
    Q('What role do decomposers play in a habitat?', 'they break down dead plants and animals to return nutrients to the soil', 'they only eat living plants', 'they only eat living animals', 'they have no role in a habitat'),
    Q('Why might an animal be well suited to its habitat?', 'it has adaptations that help it survive there', 'habitats have no connection to survival', 'animals never adapt to their surroundings', 'every animal is suited to every habitat equally'),
    Q('What is an adaptation?', 'a feature that helps a living thing survive in its environment', 'a type of weather', 'a type of rock', 'a type of food chain'),
    Q('What might happen if a habitat is destroyed?', 'the plants and animals living there may struggle to survive', 'nothing would change for the living things there', 'new habitats appear instantly', 'destroying habitats always helps animals'),
    Q('Which of these is an example of a wetland habitat?', 'a marsh', 'a desert', 'a mountain peak', 'a city sidewalk'),
    Q('Why are producers, such as plants, important in a food chain?', 'they make their own food and provide energy for other living things', 'producers have no role in a food chain', 'producers only eat other animals', 'producers never provide energy to others'),
    Q('What is a predator?', 'an animal that hunts other animals for food', 'an animal that is hunted by others', 'a type of plant', 'a type of weather'),
    Q('What is prey?', 'an animal that is hunted by a predator', 'an animal that hunts others', 'a type of plant', 'a type of decomposer'),
    Q('Why is biodiversity, or having many different species, important to a habitat?', 'it helps keep the ecosystem balanced and healthy', 'biodiversity has no effect on an ecosystem', 'having only one species is always better', 'biodiversity always harms a habitat'),
])

Sc8 = worksheet('Science', 8, 'The Human Body: Basic Systems', [
    Q('What is the main job of the skeletal system?', 'to support and protect the body', 'to pump blood', 'to digest food', 'to carry oxygen'),
    Q('What is the main job of the muscular system?', 'to help the body move', 'to protect the brain', 'to digest food', 'to filter blood'),
    Q('What organ pumps blood through the body?', 'the heart', 'the lungs', 'the stomach', 'the brain'),
    Q('What organs help you breathe?', 'the lungs', 'the heart', 'the stomach', 'the kidneys'),
    Q('What system controls the whole body and includes the brain?', 'the nervous system', 'the digestive system', 'the skeletal system', 'the circulatory system'),
    Q('What is the main job of the digestive system?', 'to break down food for the body to use', 'to pump blood', 'to control thinking', 'to protect bones'),
    Q('What organ is the control centre of the nervous system?', 'the brain', 'the heart', 'the stomach', 'the lungs'),
    Q('What do we call the hard structures that protect the brain and organs?', 'bones', 'muscles', 'blood vessels', 'skin'),
    Q('What is the largest organ of the human body?', 'the skin', 'the heart', 'the brain', 'the liver'),
    Q('Why is exercise important for the muscular and skeletal systems?', 'it helps keep muscles and bones strong and healthy', 'exercise weakens muscles and bones', 'exercise has no effect on the body', 'exercise only helps the digestive system'),
    Q('What carries blood throughout the body?', 'blood vessels', 'bones', 'muscles', 'skin'),
    Q('What is the job of the respiratory system?', 'to bring oxygen into the body and remove carbon dioxide', 'to digest food', 'to protect bones', 'to control emotions only'),
    Q('Why do we need a skeleton?', 'it supports the body and protects important organs', 'a skeleton has no purpose', 'it only helps with digestion', 'it prevents the body from moving'),
    Q('What happens when muscles and bones work together?', 'they allow the body to move', 'they stop all movement', 'they only help with breathing', 'they have no connection to each other'),
    Q('Why is it important to eat healthy foods for the digestive system?', 'it helps the body get the nutrients it needs to stay healthy', 'food has no effect on the body', 'healthy foods harm the digestive system', 'the digestive system does not need food'),
])

Sc9 = worksheet('Science', 9, 'Simple Machines at Work', [
    Q('What is a simple machine?', 'a tool that makes work easier', 'a tool that makes work harder', 'a type of animal', 'a type of weather'),
    Q('Which simple machine is a flat surface that is higher on one end, like a ramp?', 'an inclined plane', 'a lever', 'a pulley', 'a wheel and axle'),
    Q('Which simple machine uses a bar that pivots on a fixed point to lift objects?', 'a lever', 'a pulley', 'a wedge', 'a screw'),
    Q('Which simple machine uses a rope and wheel to lift objects?', 'a pulley', 'a lever', 'a wedge', 'an inclined plane'),
    Q('Which simple machine has a round shape that turns around a central rod?', 'a wheel and axle', 'a lever', 'a wedge', 'a pulley'),
    Q('Which simple machine is thin and pointed, used to split or cut things?', 'a wedge', 'a lever', 'a pulley', 'a wheel and axle'),
    Q('Which simple machine has a spiral shape and is used to hold things together?', 'a screw', 'a lever', 'a pulley', 'an inclined plane'),
    Q('What is the fixed point on a lever called?', 'the fulcrum', 'the axle', 'the wedge', 'the pulley wheel'),
    Q('Why might someone use a ramp to move a heavy box into a truck?', 'it makes lifting the box easier by spreading out the effort', 'a ramp makes the box heavier', 'ramps have no use for moving objects', 'a ramp removes the need for any effort at all'),
    Q('Which simple machine would you find in a pair of scissors?', 'a lever combined with wedges', 'a wheel and axle only', 'a pulley only', 'a screw only'),
    Q('Which simple machine would you find on a flagpole to raise a flag?', 'a pulley', 'a wedge', 'an inclined plane', 'a lever'),
    Q('Why are simple machines useful in everyday life?', 'they make many tasks require less effort', 'they make tasks require more effort', 'simple machines have no real use', 'they only work in factories'),
    Q('Which simple machine would you find in a doorknob?', 'a wheel and axle', 'a pulley', 'a wedge', 'an inclined plane'),
    Q('What is an example of a lever used in everyday life?', 'a seesaw', 'a doorknob', 'a flagpole rope', 'a spiral staircase'),
    Q('How can combining simple machines create a compound machine?', 'by joining two or more simple machines together to do more complex work', 'compound machines cannot be created', 'by removing all simple machines', 'simple machines can never be combined'),
])

Sc10 = worksheet('Science', 10, 'Caring for the Environment', [
    Q('What does it mean to reduce waste?', 'using fewer materials and creating less garbage', 'throwing away more items', 'using as many materials as possible', 'ignoring waste completely'),
    Q('What does it mean to reuse an item?', 'using it again instead of throwing it away', 'throwing it away immediately', 'using it only once', 'burning it right away'),
    Q('What does it mean to recycle a material?', 'processing it so it can be made into something new', 'throwing it into a landfill', 'burning it in a fire', 'using it only one time'),
    Q('Why is conserving water important?', 'fresh water is a limited resource that all living things need', 'water is never in limited supply', 'conserving water has no benefit', 'wasting water helps the environment'),
    Q('What can happen to habitats when pollution enters the water or air?', 'it can harm the plants and animals living there', 'pollution always helps habitats', 'pollution has no effect on living things', 'habitats are never affected by pollution'),
    Q('What is one way people can conserve energy at home?', 'turning off lights when leaving a room', 'leaving all lights on all day', 'using more electricity than needed', 'ignoring energy use completely'),
    Q('Why might a community plant trees along a street?', 'trees help clean the air and provide shade', 'trees have no benefit to a community', 'planting trees always harms the environment', 'trees only grow in forests'),
    Q('What is composting?', 'turning food scraps and plant waste into nutrient rich soil', 'throwing all waste into the ocean', 'burning food scraps immediately', 'a way to create more garbage'),
    Q('Why is it important to properly dispose of litter?', 'litter can harm wildlife and pollute the environment', 'litter always helps the environment', 'litter has no effect on wildlife', 'littering is encouraged for a clean environment'),
    Q('What is a renewable resource?', 'a resource that can be replaced naturally over time, like wind or sunlight', 'a resource that can never be replaced', 'a resource found only underground', 'a resource that harms the environment'),
    Q('What is a nonrenewable resource?', 'a resource that takes a very long time to form and can run out, like oil', 'a resource that never runs out', 'a resource that forms in seconds', 'a resource with no real use'),
    Q('Why might riding a bike instead of driving a car help the environment?', 'it produces less pollution', 'it produces more pollution', 'biking has no effect on pollution', 'cars never produce pollution'),
    Q('What can happen if too much garbage is sent to a landfill?', 'it can take up space and harm the surrounding environment', 'it always helps the surrounding environment', 'landfills have no effect on the environment', 'garbage disappears instantly in a landfill'),
    Q('Why is protecting endangered animals important?', 'it helps maintain balance and biodiversity in ecosystems', 'endangered animals have no role in an ecosystem', 'protecting animals always harms the environment', 'ecosystems do not need biodiversity'),
    Q('What can individuals do to help take care of the environment?', 'reduce, reuse, and recycle whenever possible', 'waste as many resources as possible', 'ignore the environment completely', 'use only nonrenewable resources'),
])

# ---------------------------------------------------------------------------
# SOCIAL STUDIES
# ---------------------------------------------------------------------------

SS1 = worksheet('SocialStudies', 1, 'Urban and Rural Communities', [
    Q('What is an urban community?', 'a busy community with a large population, such as a city', 'a small farming community', 'a community with no people', 'a community found only underwater'),
    Q('What is a rural community?', 'a community with fewer people, often surrounded by farmland or open space', 'a large busy city', 'a community with no land at all', 'a community found only in the mountains'),
    Q('Which is more likely to be found in an urban community?', 'tall apartment buildings and busy streets', 'large open farmland', 'small isolated cabins', 'no roads at all'),
    Q('Which is more likely to be found in a rural community?', 'farms and open fields', 'skyscrapers', 'subway systems', 'busy downtown traffic'),
    Q('What is a suburb?', 'a residential area located near a larger city', 'a type of farmland', 'a type of mountain', 'a type of ocean'),
    Q('Why might a city have more public transportation options than a rural area?', 'cities have larger populations that need to travel around a smaller area', 'cities have no need for transportation', 'rural areas always have more transportation', 'population size has no effect on transportation'),
    Q('What type of jobs might be more common in a rural community?', 'farming and agriculture', 'only office jobs in skyscrapers', 'only subway operation jobs', 'only large factory jobs'),
    Q('Why might someone choose to live in an urban community?', 'to be close to jobs, services, and entertainment', 'urban communities have no jobs available', 'urban areas have no services at all', 'cities have no entertainment options'),
    Q('Why might someone choose to live in a rural community?', 'to enjoy open space and a quieter lifestyle', 'rural areas are always the busiest', 'rural communities have no open space', 'rural areas always have the most traffic'),
    Q('What is population density?', 'how many people live in a certain area of land', 'the amount of farmland in an area', 'the height of buildings in a city', 'the number of roads in a community'),
    Q('Which community would likely have higher population density?', 'an urban community', 'a rural community', 'they are always equal', 'population density does not apply to communities'),
    Q('What might a rural community rely on for transportation over long distances?', 'cars or trucks on roads and highways', 'only subways', 'only city buses', 'only walking'),
    Q('Why might urban communities have more schools close together?', 'to serve the large number of people living in a small area', 'urban communities never need schools', 'schools are only found in rural areas', 'population size has no effect on the number of schools'),
    Q('What is one challenge a rural community might face?', 'being far from certain services, such as hospitals', 'having too many people in a small area', 'too much traffic congestion', 'too many tall buildings'),
    Q('What is one challenge an urban community might face?', 'traffic congestion and crowding', 'having too much open farmland', 'having too few people nearby', 'having no services available'),
])

SS2 = worksheet('SocialStudies', 2, 'Reading Maps and Finding Locations', [
    Q('What does a map key or legend explain?', 'what the symbols on a map represent', 'the exact temperature of a place', 'the population of a country', 'the history of a location'),
    Q('What is a compass rose used for on a map?', 'to show directions such as north, south, east, and west', 'to show the temperature', 'to show the population', 'to show the time zone'),
    Q('Which direction is opposite of north?', 'south', 'east', 'west', 'north again'),
    Q('Which direction is opposite of east?', 'west', 'north', 'south', 'east again'),
    Q('What does a scale on a map help you determine?', 'the real distance between two places', 'the population of a place', 'the weather in a place', 'the exact colours of the land'),
    Q('What type of map shows the shape of the land, such as mountains and valleys?', 'a physical map', 'a political map', 'a weather map', 'a population map'),
    Q('What type of map shows borders between countries, provinces, or states?', 'a political map', 'a physical map', 'a weather map', 'a road map only'),
    Q('What symbol might represent a capital city on a map?', 'a star', 'a triangle', 'a wavy line', 'a solid black square'),
    Q('What do blue lines or shapes on a map usually represent?', 'bodies of water', 'mountains', 'roads', 'cities'),
    Q('Why is a map key important when reading a map?', 'it helps the reader understand what each symbol means', 'a map key has no purpose', 'it shows the exact population', 'it replaces the need for a compass rose'),
    Q('What is a globe?', 'a three dimensional model of the earth', 'a flat paper map only', 'a type of compass', 'a type of weather chart'),
    Q('Why might a map be more useful than a globe for showing a small area in detail?', 'a map can zoom in and show more detail of a small area', 'a globe always shows more detail than a map', 'maps can never show detail', 'globes are always more useful for small areas'),
    Q('What are latitude and longitude used for?', 'to help pinpoint exact locations on the earth', 'to show the temperature of a location', 'to show the population of a location', 'to show the history of a location'),
    Q('If you are travelling from your home toward the top of a standard map, which direction are you likely heading?', 'north', 'south', 'east', 'west'),
    Q('Why is it useful to know how to read a map?', 'it helps you find locations and understand distances', 'maps have no real use', 'reading maps is never helpful', 'maps only show pictures with no useful information'),
])

SS3 = worksheet('SocialStudies', 3, 'Canadian Provinces and Territories', [
    Q('How many provinces does Canada have?', '10', '13', '7', '5'),
    Q('How many territories does Canada have?', '3', '10', '5', '1'),
    Q('What is the capital city of Canada?', 'Ottawa', 'Toronto', 'Vancouver', 'Montreal'),
    Q('Which province is located on the west coast of Canada?', 'British Columbia', 'Nova Scotia', 'Ontario', 'Prince Edward Island'),
    Q('Which province has the largest population?', 'Ontario', 'Prince Edward Island', 'Nova Scotia', 'New Brunswick'),
    Q('Which is the smallest province in Canada by area?', 'Prince Edward Island', 'Ontario', 'Quebec', 'British Columbia'),
    Q('Which territory is located in the far north and shares its name with a famous gold rush river?', 'Yukon', 'Nunavut', 'Northwest Territories', 'Alberta'),
    Q('Which province is known for the French language being widely spoken?', 'Quebec', 'Alberta', 'Manitoba', 'Saskatchewan'),
    Q('Which two provinces are known as Prairie provinces along with Manitoba?', 'Alberta and Saskatchewan', 'Quebec and Ontario', 'British Columbia and Yukon', 'Nova Scotia and New Brunswick'),
    Q('Which province is home to the city of Toronto?', 'Ontario', 'Quebec', 'Manitoba', 'Alberta'),
    Q('Which territory has the largest Inuit population in Canada?', 'Nunavut', 'Yukon', 'Northwest Territories', 'British Columbia'),
    Q('Which ocean borders the eastern provinces of Canada?', 'the Atlantic Ocean', 'the Pacific Ocean', 'the Arctic Ocean', 'the Indian Ocean'),
    Q('Which ocean borders British Columbia?', 'the Pacific Ocean', 'the Atlantic Ocean', 'the Arctic Ocean', 'the Indian Ocean'),
    Q('Which ocean borders the northern territories of Canada?', 'the Arctic Ocean', 'the Pacific Ocean', 'the Atlantic Ocean', 'the Indian Ocean'),
    Q('What do we call the regions of Canada that are not provinces but are still part of the country?', 'territories', 'states', 'counties', 'districts'),
])

SS4 = worksheet('SocialStudies', 4, 'Early Settlers in Canada', [
    Q('Who were some of the first European explorers to arrive in what is now Canada?', 'French and British explorers', 'Australian explorers', 'South American explorers', 'explorers from Antarctica'),
    Q('Why did many early settlers come to Canada?', 'to find new land, resources, and opportunities', 'to avoid all forms of travel', 'settlers never had a reason to come', 'to find warmer weather only'),
    Q('What was the fur trade an important part of for early settlers?', 'the economy, through trading furs such as beaver pelts', 'a type of early transportation only', 'a type of early school system', 'a type of early government building'),
    Q('What type of home did many early pioneer families build when they settled on new land?', 'a log cabin', 'a skyscraper', 'a subway station', 'a shopping mall'),
    Q('Why was farming important to early settler communities?', 'it provided food for families and communities to survive', 'farming had no importance to early settlers', 'settlers never grew their own food', 'farming was banned in early communities'),
    Q('What natural resource did early settlers rely on for building homes and tools?', 'wood from forests', 'plastic', 'steel beams', 'electricity'),
    Q('What is a pioneer?', 'an early settler who moved to a new, undeveloped area', 'a type of animal', 'a type of weather', 'a type of map'),
    Q('Why might early settlers have settled near rivers?', 'rivers provided water, transportation, and often fertile land', 'rivers had no benefit to settlers', 'settlers always avoided rivers', 'rivers made travel impossible'),
    Q('What tools might early settlers have used to farm the land?', 'simple hand tools and animal powered equipment', 'modern tractors and computers', 'no tools were used at all', 'only electric machines'),
    Q('How did early settlers typically travel long distances before modern transportation?', 'by foot, horse, canoe, or wagon', 'by airplane', 'by subway', 'by car'),
    Q('Why did communities often form around a central area, such as a church or trading post?', 'it gave people a shared place to gather, trade, and support one another', 'communities never had a central gathering place', 'central areas had no purpose', 'people always avoided gathering together'),
    Q('What role did Indigenous peoples often play in helping early European settlers?', 'sharing knowledge of the land, including farming and survival skills', 'Indigenous peoples had no contact with settlers', 'Indigenous peoples never shared any knowledge', 'settlers never interacted with Indigenous peoples'),
    Q('Why might life have been difficult for early settler families?', 'they often faced harsh weather and had to build everything themselves', 'life was always easy for early settlers', 'settlers had access to modern conveniences', 'difficulty was never part of settler life'),
    Q('What did early settlers often trade for goods they could not produce themselves?', 'furs, crops, or handmade goods', 'modern electronics', 'nothing, trade did not exist', 'plastic products'),
    Q('Why is learning about early settlers helpful for understanding Canada today?', 'it shows how communities and traditions in Canada began to form', 'early settlers have no connection to modern Canada', 'this history has no importance today', 'early settlement never affected how Canada developed'),
])

SS5 = worksheet('SocialStudies', 5, 'Indigenous Peoples and Traditions', [
    Q('What term describes the original peoples of what is now Canada?', 'Indigenous peoples', 'recent immigrants', 'early European settlers only', 'visitors from other countries'),
    Q('What are the three main groups recognized as Indigenous peoples in Canada?', 'First Nations, Metis, and Inuit', 'only First Nations', 'only Inuit', 'only Metis'),
    Q('Which Indigenous group traditionally lived in the Arctic regions of Canada?', 'the Inuit', 'the Metis', 'First Nations from the prairies', 'coastal fishing nations only'),
    Q('What is oral storytelling traditionally used for among many Indigenous communities?', 'passing down history, culture, and lessons through generations', 'oral storytelling has no purpose', 'it was only used for entertainment', 'it replaced the need for community gatherings'),
    Q('What is a powwow?', 'a gathering that celebrates Indigenous culture through dance, music, and community', 'a type of Indigenous food only', 'a type of building material', 'a type of early transportation'),
    Q('Why is land often considered important in many Indigenous traditions?', 'it is deeply connected to identity, culture, and ways of life', 'land has no importance in Indigenous traditions', 'Indigenous peoples never lived on the land', 'land was never used for any purpose'),
    Q('What might Indigenous peoples traditionally have used birchbark for?', 'building canoes and containers', 'building modern skyscrapers', 'making electronics', 'paving roads'),
    Q('Why is it respectful to learn about Indigenous history and traditions?', 'it helps build understanding and respect for the first peoples of this land', 'learning about this history is not important', 'Indigenous history has no connection to Canada', 'it is unnecessary to learn about other cultures'),
    Q('What are traditional teachings sometimes called that share lessons about respect and the natural world?', 'teachings passed down by Elders', 'rules written only in modern books', 'teachings with no connection to nature', 'teachings that ignore community values'),
    Q('What is the Metis nation historically known for its connection to?', 'a mixed First Nations and European heritage and culture', 'having no connection to Canadian history', 'being unrelated to any other group', 'arriving only in modern times'),
    Q('Why might many Indigenous communities have strong connections to rivers, lakes, and forests?', 'these resources were essential for food, travel, and daily life', 'these resources had no importance to Indigenous communities', 'water and forests were always avoided', 'Indigenous communities never depended on natural resources'),
    Q('What is one way Indigenous cultures are celebrated in Canada today?', 'through cultural events, art, and educational programs', 'Indigenous cultures are not recognized in Canada today', 'Indigenous cultures have disappeared completely', 'there are no ways to learn about Indigenous cultures'),
    Q('Why is it important for students to learn about residential schools as part of Canadian history?', 'to understand a difficult part of history and support reconciliation', 'this part of history should be ignored', 'residential schools have no connection to Canadian history', 'learning about this history serves no purpose'),
    Q('What does the word reconciliation mean in the context of Indigenous and non-Indigenous relations in Canada?', 'working to build understanding, respect, and repair relationships', 'ignoring the past completely', 'avoiding any communication between groups', 'erasing Indigenous history from records'),
    Q('Why might traditional knowledge about the land be valuable today?', 'it can teach sustainable ways of caring for the environment', 'traditional knowledge has no value today', 'it has nothing to do with the environment', 'modern methods have replaced the need for any traditional knowledge'),
])

SS6 = worksheet('SocialStudies', 6, 'Government and Community Leaders', [
    Q('Who is the leader of a Canadian city or town often called?', 'a mayor', 'a premier', 'a prime minister', 'a governor'),
    Q('Who is the leader of a Canadian province called?', 'a premier', 'a mayor', 'a prime minister', 'a president'),
    Q('Who is the leader of the entire country of Canada called?', 'the prime minister', 'a premier', 'a mayor', 'a president'),
    Q('What is the role of a city council?', 'to make decisions and rules for the local community', 'to control the weather', 'to run schools in every province', 'to lead the entire country'),
    Q('Why do communities elect leaders such as mayors?', 'to represent the community and make decisions on its behalf', 'leaders are never elected', 'elections have no purpose', 'communities never need leaders'),
    Q('What is a law?', 'a rule that everyone in a community or country must follow', 'a rule that only some people must follow', 'a suggestion with no consequences', 'a type of holiday'),
    Q('Why are laws important in a community?', 'they help keep people safe and communities running smoothly', 'laws have no purpose', 'laws only apply to leaders', 'communities function better with no rules at all'),
    Q('What is a vote?', 'a way for people to choose their leaders or make a decision', 'a type of tax', 'a type of law', 'a type of holiday'),
    Q('Why is voting an important part of a democracy?', 'it allows citizens to have a say in who represents them', 'voting has no effect on government', 'only leaders are allowed to vote', 'voting is not part of a democracy'),
    Q('What is a responsibility citizens have in their community?', 'following laws and helping others', 'ignoring all rules', 'avoiding the community completely', 'refusing to help anyone'),
    Q('What might a local government be responsible for, such as roads and parks?', 'providing and maintaining community services', 'only providing entertainment', 'local governments have no responsibilities', 'only the national government provides services'),
    Q('Why might communities have both local and national governments?', 'different levels of government handle different responsibilities', 'governments never work at different levels', 'only one level of government is ever needed', 'local and national governments always do the exact same job'),
    Q('What is a right that Canadian citizens have?', 'the right to vote in elections', 'the right to ignore all laws', 'the right to avoid paying any attention to the community', 'rights do not exist for citizens'),
    Q('Why might a community hold a town hall meeting?', 'to let residents share ideas and concerns with local leaders', 'town hall meetings have no purpose', 'residents are never allowed to share ideas', 'meetings only happen to make decisions in secret'),
    Q('What is the purpose of the Canadian Parliament?', 'to create and pass laws for the country', 'to control the weather', 'to run every local school', 'parliament has no purpose'),
])

SS7 = worksheet('SocialStudies', 7, 'Natural Resources in Canada', [
    Q('What is a natural resource?', 'something found in nature that people use, such as water or trees', 'something made only in a factory', 'a type of holiday', 'a type of government'),
    Q('Which natural resource is used to make paper and lumber?', 'trees', 'oil', 'water', 'rocks only'),
    Q('Which natural resource is essential for drinking, farming, and many industries?', 'water', 'coal', 'gold', 'sand only'),
    Q('What is mining used to collect?', 'minerals and metals from the ground', 'only trees', 'only water', 'only wind'),
    Q('Which resource is used to generate hydroelectric power?', 'flowing water', 'coal', 'sunlight only', 'wind only'),
    Q('Which natural resource comes from underground and is used to make gasoline?', 'oil', 'trees', 'water', 'wind'),
    Q('Why is Canada known for having many natural resources?', 'it has vast forests, waterways, minerals, and farmland', 'Canada has no natural resources', 'natural resources are only found in cities', 'Canada has no forests or waterways'),
    Q('What is a renewable natural resource?', 'one that can be replaced naturally over time, such as trees or wind', 'one that can never be replaced', 'one that is only found underground', 'one that has no use'),
    Q('What is a nonrenewable natural resource?', 'one that takes a very long time to form and is limited, such as oil', 'one that never runs out', 'one found only in the ocean', 'one that has no economic use'),
    Q('Why might a community near a forest rely on the logging industry?', 'trees provide jobs and materials for building and paper products', 'forests have no economic value', 'logging never provides any jobs', 'trees are never used for building materials'),
    Q('Why is protecting natural resources important for the future?', 'so they remain available for future generations', 'protecting resources has no benefit', 'resources can never run out', 'future generations will not need any resources'),
    Q('What resource is especially important to the fishing industry in coastal provinces?', 'fish and other seafood from the ocean', 'coal from mines', 'gold from rivers', 'wind from storms'),
    Q('Why might Canada export natural resources to other countries?', 'to trade resources for goods, services, or money', 'exporting resources has no economic benefit', 'Canada never trades with other countries', 'natural resources cannot be exported'),
    Q('What is one way people can help conserve natural resources?', 'using resources wisely and avoiding waste', 'using as many resources as possible', 'ignoring conservation completely', 'resources do not need to be conserved'),
    Q('Why are farmland and fertile soil considered important natural resources?', 'they allow food to be grown for communities', 'farmland has no connection to food production', 'soil is never considered a resource', 'fertile soil has no economic value'),
])

SS8 = worksheet('SocialStudies', 8, 'Rules, Rights, and Responsibilities', [
    Q('What is a rule?', 'a guideline that helps people know how to behave in a certain place', 'a suggestion that no one needs to follow', 'a type of celebration', 'a type of natural resource'),
    Q('Why do schools have rules?', 'to keep students safe and help everyone learn', 'rules have no purpose in schools', 'schools function better without any rules', 'rules are only meant to punish students'),
    Q('What is a right?', 'something a person is entitled to, such as an education', 'a punishment for breaking a rule', 'a type of natural resource', 'a type of holiday'),
    Q('What is a responsibility?', 'a duty or task a person is expected to do', 'a reward for doing nothing', 'a type of natural resource', 'a type of celebration'),
    Q('What is one responsibility students have at school?', 'following classroom rules and respecting others', 'ignoring all classroom rules', 'avoiding schoolwork completely', 'being disrespectful to classmates'),
    Q('Why is it important to respect the rights of others in a community?', 'it helps everyone feel safe, valued, and treated fairly', 'respecting others has no benefit', 'rights only matter for some people', 'communities function better when rights are ignored'),
    Q('What is a consequence?', 'a result that happens because of an action, especially breaking a rule', 'a reward given for no reason', 'a type of natural resource', 'a type of holiday'),
    Q('Why might a community create rules about littering?', 'to keep the environment clean and safe for everyone', 'littering rules have no purpose', 'communities prefer a littered environment', 'rules about littering only apply to visitors'),
    Q('What is one right that all Canadian children have?', 'the right to an education', 'the right to ignore all rules', 'the right to avoid all responsibilities', 'children have no rights'),
    Q('Why is it a shared responsibility to take care of community spaces, such as parks?', 'because everyone benefits from a clean and safe shared space', 'only the government benefits from parks', 'shared spaces have no connection to responsibility', 'parks do not need to be cared for'),
    Q('What might happen if people in a community ignored all the rules?', 'the community could become unsafe or unfair for everyone', 'the community would always improve', 'ignoring rules has no effect on a community', 'rules have no connection to safety'),
    Q('Why is fairness an important value in a classroom or community?', 'it helps ensure everyone is treated equally and with respect', 'fairness has no importance in a community', 'unfair treatment always helps a community', 'fairness only matters for adults'),
    Q('What is one way students can show responsibility at home?', 'helping with chores and following family rules', 'refusing to help with anything at home', 'ignoring family rules completely', 'responsibility does not apply at home'),
    Q('Why do communities create laws in addition to school and family rules?', 'to keep everyone safe and treated fairly on a larger scale', 'laws have no connection to safety', 'communities do not need laws', 'laws only apply inside of a single school'),
    Q('What is citizenship?', 'being a member of a community with certain rights and responsibilities', 'a type of natural resource', 'a type of holiday', 'a type of weather pattern'),
])

SS9 = worksheet('SocialStudies', 9, 'Canadian Symbols and Celebrations', [
    Q('What is the national symbol found on the Canadian flag?', 'a maple leaf', 'a beaver', 'an eagle', 'a moose'),
    Q('What colours are on the Canadian flag?', 'red and white', 'blue and white', 'green and gold', 'black and white'),
    Q('What is Canada Day and when is it celebrated?', 'a holiday celebrating the founding of Canada, celebrated on July 1', 'a holiday celebrated only in December', 'a holiday with no connection to Canada', 'a holiday celebrated every month'),
    Q('What animal is considered an important symbol of Canada, known for building dams?', 'the beaver', 'the lion', 'the tiger', 'the kangaroo'),
    Q('What is the name of the national anthem of Canada?', 'O Canada', 'God Save the King only', 'America the Beautiful', 'Amazing Grace'),
    Q('What sport is often considered a beloved national pastime in Canada?', 'hockey', 'cricket', 'rugby', 'baseball only'),
    Q('What is Remembrance Day used to honour?', 'members of the military who served and died for their country', 'a celebration of the new year', 'a celebration of summer', 'a holiday about maple syrup'),
    Q('On what date is Remembrance Day observed in Canada?', 'November 11', 'July 1', 'December 25', 'October 31'),
    Q('What food is closely associated with Canadian tradition, made from the sap of a tree?', 'maple syrup', 'olive oil', 'coconut milk', 'peanut butter'),
    Q('What is the significance of the loonie as a Canadian symbol?', 'it is a coin featuring a loon, representing Canadian wildlife', 'it is a type of Canadian holiday', 'it is a type of Canadian mountain', 'it has no connection to Canada'),
    Q('What might communities do to celebrate Canada Day?', 'attend fireworks, parades, and community events', 'stay indoors with no celebration', 'ignore the holiday completely', 'celebrate only in other countries'),
    Q('Why are national symbols, such as the flag, important to a country?', 'they represent shared identity and pride', 'national symbols have no meaning', 'symbols are only used for decoration', 'flags have no connection to a countrys identity'),
    Q('What well known Canadian symbol appears in nature imagery and on Canadian coins?', 'the maple leaf', 'a cactus', 'a palm tree', 'a desert scene'),
    Q('Why might different cultural celebrations be important in Canadian communities?', 'they celebrate the diversity and traditions of the people who live there', 'cultural celebrations have no place in Canada', 'diversity has no connection to community life', 'celebrations should only reflect one single culture'),
    Q('What is one way Canadians might show respect during a Remembrance Day ceremony?', 'observing a moment of silence', 'talking loudly throughout the ceremony', 'ignoring the ceremony completely', 'celebrating with fireworks'),
])

SS10 = worksheet('SocialStudies', 10, 'Community Helpers and Services', [
    Q('What is the job of a firefighter?', 'to respond to fires and other emergencies to keep people safe', 'to teach students in a classroom', 'to deliver mail', 'to grow crops on a farm'),
    Q('What is the job of a police officer?', 'to help keep communities safe and enforce laws', 'to fix broken pipes', 'to deliver newspapers', 'to teach at a school'),
    Q('What is the job of a doctor?', 'to diagnose and treat illnesses and injuries', 'to build houses', 'to deliver mail', 'to grow food'),
    Q('What is the job of a librarian?', 'to help people find books and information at a library', 'to fight fires', 'to repair cars', 'to deliver mail'),
    Q('Why are community helpers important?', 'they provide essential services that keep a community safe and running smoothly', 'community helpers have no real purpose', 'communities function better without any helpers', 'helpers only work for themselves'),
    Q('What is the job of a paramedic?', 'to provide emergency medical care and transport patients to a hospital', 'to teach at a school', 'to deliver mail', 'to grow crops'),
    Q('What is the job of a teacher?', 'to help students learn new skills and knowledge', 'to put out fires', 'to deliver mail', 'to repair roads'),
    Q('What service does a mail carrier provide to a community?', 'delivering letters and packages to homes and businesses', 'fighting fires', 'teaching students', 'repairing water pipes'),
    Q('Why might a community need a wide variety of community helpers?', 'different helpers meet different needs, from safety to health to education', 'one type of helper can meet every need', 'communities do not need any helpers', 'variety among helpers has no benefit'),
    Q('What is the job of a sanitation worker?', 'to collect and dispose of garbage and recycling', 'to teach students', 'to treat illnesses', 'to deliver mail'),
    Q('Why might community helpers need special training?', 'to safely and effectively perform their important jobs', 'training has no connection to their jobs', 'community helpers require no training at all', 'special training makes helpers less effective'),
    Q('What service might a public works department provide to a community?', 'maintaining roads, water systems, and other infrastructure', 'teaching in classrooms', 'practicing medicine', 'delivering mail'),
    Q('Why is it helpful to know the community helpers available in an emergency, such as calling 911?', 'knowing who to contact can help get quick assistance during an emergency', 'emergencies never require any help', '911 has no connection to community helpers', 'knowing this information is never useful'),
    Q('What is the job of a veterinarian?', 'to care for the health of animals', 'to care for city roads', 'to deliver mail', 'to teach in a classroom'),
    Q('Why might students thank community helpers for their work?', 'to show appreciation for the important services they provide', 'community helpers do not deserve any recognition', 'thanking helpers has no value', 'their work has no impact on the community'),
])


all_worksheets = [
    L1, L2, L3, L4, L5, L6, L7, L8, L9, L10,
    M1, M2, M3, M4, M5, M6, M7, M8, M9, M10,
    Sc1, Sc2, Sc3, Sc4, Sc5, Sc6, Sc7, Sc8, Sc9, Sc10,
    SS1, SS2, SS3, SS4, SS5, SS6, SS7, SS8, SS9, SS10,
]


def _rebalance_answer_positions(worksheets, seed=20260820):
    """Shuffles each worksheet's mc() answer index across A/B/C/D so there
    is no bias toward one position, mirroring the approach used in
    gen_grade3_days181_187.py's _rebalance_answer_positions()."""
    import random
    rng = random.Random(seed)
    out = []
    for subject, number, title, questions in worksheets:
        n = len(questions)
        targets = [i % 4 for i in range(n)]
        rng.shuffle(targets)
        new_questions = []
        for i, q in enumerate(questions):
            kind, qtext, opts, a = q
            correct_text = opts[a]
            wrong_texts = [o for j, o in enumerate(opts) if j != a]
            rng.shuffle(wrong_texts)
            target = targets[i]
            new_opts = [None, None, None, None]
            new_opts[target] = correct_text
            wi = 0
            for slot in range(4):
                if new_opts[slot] is None:
                    new_opts[slot] = wrong_texts[wi]
                    wi += 1
            new_questions.append(('mc', qtext, new_opts, target))
        out.append((subject, number, title, new_questions))
    return out


if __name__ == '__main__':
    all_worksheets = _rebalance_answer_positions(all_worksheets)
    write_worksheets(3, all_worksheets)
