#!/usr/bin/env python3
"""Generates data/grade9_worksheets.ts: 10 standalone optional-practice
worksheets per subject (Language, Math, Science, SocialStudies), 15
multiple-choice questions each, per Project Plan item 8. Separate pipeline
from data/grade9.ts (the 187-day lesson sequence) -- not touched here.
"""
import sys
sys.path.insert(0, '.')
from gen_worksheets import mc, worksheet, write_worksheets


def rot(q, opts, idx):
    """opts[0] is the correct answer; rotate so the correct answer lands
    at position idx (0-3), keeping distractor relative order otherwise."""
    correct = opts[0]
    distractors = opts[1:]
    new_opts = distractors[:]
    new_opts.insert(idx, correct)
    return mc(q, new_opts, idx)


def make_ws(subject, number, title, items):
    """items: list of exactly 15 (q, [correct, d1, d2, d3]) tuples."""
    offset = (number - 1) % 4
    questions = []
    for i, (q, opts) in enumerate(items):
        idx = (offset + i) % 4
        questions.append(rot(q, opts, idx))
    return worksheet(subject, number, title, questions)


all_worksheets = []

# ==================== LANGUAGE ====================

all_worksheets.append(make_ws('Language', 1, 'Grammar Foundations: Parts of Speech and Sentence Structure', [
    ('Identify the noun in: The dog barked loudly.', ['Dog', 'Barked', 'Loudly', 'The']),
    ('Identify the verb in: She sings every morning.', ['Sings', 'She', 'Every', 'Morning']),
    ('An adjective is a word that:', ['Describes a noun', 'Names a person place or thing', 'Shows action', 'Connects clauses']),
    ('Identify the adverb in: He ran quickly to school.', ['Quickly', 'He', 'Ran', 'School']),
    ('A pronoun replaces:', ['A noun', 'A verb', 'An adjective', 'A preposition']),
    ('Identify the preposition in: The book is on the table.', ['On', 'Book', 'Is', 'Table']),
    ('A conjunction is used to:', ['Join words or clauses', 'Describe a noun', 'Replace a noun', 'Show possession']),
    ('Identify the subject in: The tall student answered the question.', ['Student', 'Tall', 'Answered', 'Question']),
    ('Identify the direct object in: Maria wrote a letter.', ['A letter', 'Maria', 'Wrote', 'None']),
    ('Which word is an interjection?', ['Wow', 'Table', 'Quickly', 'Because']),
    ('A common noun names:', ['Any general person place or thing', 'A specific person or place', 'Only actions', 'Only feelings']),
    ('Identify the proper noun.', ['Toronto', 'city', 'building', 'river']),
    ('Which sentence uses correct subject-verb agreement?', ['The students are happy', 'The student are happy', 'The students is happy', 'The student were is happy']),
    ('A collective noun refers to:', ['A group treated as one unit', 'A single item', 'An action', 'A quality']),
    ('Identify the article in: A cat sat on the mat.', ['A', 'Cat', 'Sat', 'On']),
]))

all_worksheets.append(make_ws('Language', 2, 'Complex Sentences and Clauses', [
    ('An independent clause:', ['Can stand alone as a sentence', 'Cannot stand alone', 'Has no verb', 'Has no subject']),
    ('A dependent clause:', ['Cannot stand alone as a sentence', 'Always forms a complete sentence', 'Has no subject or verb', 'Is always the main idea']),
    ('Identify the subordinating conjunction: Although it rained, we played outside.', ['Although', 'It', 'Rained', 'Played']),
    ('A complex sentence contains:', ['An independent and a dependent clause', 'Only one independent clause', 'No clauses at all', 'Only dependent clauses']),
    ('Which is a subordinating conjunction?', ['Because', 'Or', 'And', 'But']),
    ('A compound sentence joins:', ['Two independent clauses', 'Two dependent clauses', 'A phrase and a word', 'Nothing at all']),
    ('Identify the coordinating conjunction: She studied, and she passed.', ['And', 'She', 'Studied', 'Passed']),
    ('A run-on sentence occurs when:', ['Clauses are joined without proper punctuation', 'A sentence is correctly punctuated', 'A sentence is too short', 'There are no clauses']),
    ('A comma splice happens when:', ['Two independent clauses are joined only by a comma', 'A sentence has no clauses', 'Punctuation is fully correct', 'A paragraph ends properly']),
    ('Fix this fragment: Because she was late.', ['Because she was late, she missed the bus', 'Because. She was late', 'She was late because', 'Late she because was']),
    ('Identify the relative clause: The book that I read was excellent.', ['That I read', 'The book', 'Was excellent', 'I read']),
    ('A relative pronoun such as who or which introduces:', ['A relative clause', 'A main clause', 'A prepositional phrase', 'An interjection']),
    ('Which sentence is a simple sentence?', ['The dog slept', 'Although the dog slept, it woke later', 'The dog slept, and the cat ran', 'Because the dog slept, no noise was heard']),
    ('Combine using a subordinating conjunction: She left. It was raining.', ['She left because it was raining', 'She left, it was raining', 'She left it was raining', 'Raining she left']),
    ('A sentence fragment is:', ['An incomplete thought punctuated as a sentence', 'A complete sentence', 'A sentence with two clauses', 'A question']),
]))

all_worksheets.append(make_ws('Language', 3, 'Punctuation and Mechanics', [
    ('Which sentence uses a comma correctly?', ['After the game, we went home', 'After the game we, went home', 'After, the game we went home', 'After the game we went, home']),
    ('A semicolon can be used to:', ['Join two related independent clauses', 'End a question', 'Start a sentence', 'Replace a period always']),
    ('When should a colon be used?', ['To introduce a list', 'To end a sentence casually', 'To replace a comma always', 'To join two nouns']),
    ('Which title is correctly capitalized?', ['The Lord of the Flies', 'the lord of the flies', 'The lord Of The flies', 'THE LORD of the flies']),
    ('Quotation marks are used to:', ['Show exact spoken or quoted words', 'End a sentence', 'Join two clauses', 'Show possession']),
    ('Which sentence has correct capitalization?', ['We visited Toronto in July', 'we visited toronto in July', 'We visited Toronto in july', 'we Visited Toronto In July']),
    ('An apostrophe is commonly used to show:', ['Possession or a contraction', 'The end of a sentence', 'A list of items', 'A question']),
    ('Which is the correctly punctuated sentence?', ['Wait, he said, before you leave.', 'Wait he said before you leave', 'wait, he said, before you leave', 'Wait he, said before, you leave']),
    ('A hyphen is often used to:', ['Join words into a compound modifier', 'End a paragraph', 'Replace a period', 'Start a list']),
    ('Choose the correctly punctuated list.', ['We need milk, eggs, and bread', 'We need milk eggs and bread', 'We need, milk, eggs and, bread', 'We need milk; eggs; and, bread']),
    ('Which sentence correctly uses a question mark?', ['Are we leaving soon?', 'Are we leaving soon.', 'Are we leaving soon!', 'Are we leaving soon,']),
    ('Parentheses are used to:', ['Add extra or clarifying information', 'End a sentence', 'Begin a list', 'Replace a comma always']),
    ('Which words should be capitalized in: we study english on monday?', ['English and Monday', 'english', 'monday', 'we']),
    ('An ellipsis indicates:', ['An omission or a trailing thought', 'The end of a question', 'A strong command', 'A new paragraph']),
    ('Choose the sentence with correct end punctuation for a command.', ['Close the door', 'Close the door?', 'Close the door,', 'close the Door']),
]))

all_worksheets.append(make_ws('Language', 4, 'Vocabulary and Word Choice', [
    ('A synonym for happy is:', ['Joyful', 'Sad', 'Angry', 'Tired']),
    ('An antonym for ancient is:', ['Modern', 'Old', 'Ageless', 'Historic']),
    ('Choosing precise words instead of vague ones helps writing become:', ['Clearer and more specific', 'Longer', 'Harder to read', 'More repetitive']),
    ('A word with multiple meanings depending on context is called:', ['A homonym', 'A synonym', 'An antonym', 'A conjunction']),
    ('Formal vocabulary is most appropriate in:', ['An academic essay', 'A text message to a friend', 'A casual chat', 'A diary entry']),
    ('The connotation of a word refers to:', ['Its emotional or implied meaning', 'Its dictionary definition only', 'Its spelling', 'Its part of speech']),
    ('The denotation of a word refers to:', ['Its literal dictionary meaning', 'Its emotional association', 'Its sound', 'Its length']),
    ('Choose the most precise word for walked slowly.', ['Trudged', 'Moved', 'Went', 'Traveled']),
    ('A thesaurus is used to find:', ['Synonyms and antonyms', 'Definitions only', 'Spelling rules', 'Grammar rules']),
    ('Which word has a negative connotation?', ['Stubborn', 'Determined', 'Persistent', 'Confident']),
    ('A cliche is:', ['An overused expression', 'A brand new idea', 'A grammar rule', 'A type of clause']),
    ('Jargon refers to:', ['Specialized terms used within a field', 'Everyday casual speech', 'Formal punctuation', 'A type of sentence']),
    ('Which sentence uses the most vivid word choice?', ['The storm shattered the windows', 'The storm affected the windows', 'The storm hit the windows', 'The storm was near the windows']),
    ('A prefix added to a word usually:', ['Changes its meaning at the beginning', 'Changes its meaning at the end', 'Has no effect', 'Adds punctuation']),
    ('The suffix -less generally means:', ['Without', 'Full of', 'Before', 'After']),
]))

all_worksheets.append(make_ws('Language', 5, 'Reading Comprehension Strategies', [
    ('Making an inference means:', ['Drawing a conclusion from clues in the text', 'Copying text exactly', 'Ignoring the text', 'Skipping the ending']),
    ('The main idea of a passage is:', ['The central point the writer is making', 'A minor detail', 'The title only', 'The last sentence only']),
    ('Skimming a text is used to:', ['Quickly get a general sense of content', 'Memorize every word', 'Analyze grammar', 'Translate the text']),
    ('Scanning a text is used to:', ['Locate specific information quickly', 'Read every word slowly', 'Summarize the whole text', 'Analyze tone']),
    ('A supporting detail:', ['Provides evidence for the main idea', 'Replaces the main idea', 'Is always the title', 'Is unrelated to the topic']),
    ('Context clues help readers:', ['Determine the meaning of unfamiliar words', 'Ignore unfamiliar words', 'Skip difficult sentences', 'Avoid rereading']),
    ('Summarizing a text means:', ['Restating the key points briefly', 'Copying the text word for word', 'Adding new information', 'Ignoring the main idea']),
    ('The purpose of a persuasive text is usually to:', ['Convince the reader of a viewpoint', 'Entertain only', 'Give step by step instructions', 'List random facts']),
    ('Predicting outcomes while reading involves:', ['Using clues to guess what happens next', 'Ignoring the plot', 'Rereading only the ending', 'Skipping the introduction']),
    ('A text structure that compares two subjects is called:', ['Compare and contrast', 'Cause and effect', 'Chronological order', 'Problem and solution']),
    ('Cause and effect structure explains:', ['Why something happened and its result', 'Two similar ideas', 'A sequence of steps only', 'A list of facts']),
    ('Visualizing while reading helps a reader:', ['Form mental pictures of the text', 'Skip difficult words', 'Avoid summarizing', 'Memorize spelling']),
    ('The tone of a text is best described as:', ['The attitude the writer expresses toward the subject', 'The length of the text', 'The font used', 'The number of paragraphs']),
    ('Rereading a confusing passage is a strategy used to:', ['Improve understanding', 'Waste time', 'Avoid the main idea', 'Skip important details']),
    ('A graphic organizer helps readers:', ['Visually organize information from a text', 'Replace reading entirely', 'Add unrelated ideas', 'Avoid taking notes']),
]))

all_worksheets.append(make_ws('Language', 6, 'Literary Devices and Figurative Language', [
    ('A metaphor:', ['Compares two things without using like or as', 'Compares using like or as', 'Gives human traits to objects', 'Repeats consonant sounds']),
    ('A simile:', ['Compares two things using like or as', 'Compares without like or as', 'Exaggerates for effect', 'Uses sound repetition']),
    ('Personification gives:', ['Human qualities to non-human things', 'Objects a size comparison', 'A story its setting', 'A poem its rhyme']),
    ('Hyperbole is:', ['An extreme exaggeration', 'A quiet understatement', 'A direct comparison', 'A sound device']),
    ('Alliteration is the repetition of:', ['Initial consonant sounds', 'Vowel sounds in the middle of words', 'Entire words', 'Rhyming endings']),
    ('Onomatopoeia refers to words that:', ['Imitate sounds', 'Compare two unlike things', 'Exaggerate meaning', 'Contradict themselves']),
    ('Symbolism is when:', ['An object represents a deeper meaning', 'A sentence is repeated', 'A character speaks directly', 'A setting is described literally']),
    ('Irony occurs when:', ['The opposite of what is expected happens', 'Everything happens as expected', 'A story has no conflict', 'A character never changes']),
    ('Foreshadowing is used to:', ['Hint at events that will happen later', 'Summarize the plot at the end', 'Describe the setting only', 'Introduce new characters late in the story']),
    ('An idiom is:', ['An expression whose meaning differs from its literal words', 'A type of rhyme', 'A grammar rule', 'A punctuation mark']),
    ('Imagery appeals mainly to:', ['The five senses', 'Only logic', 'Only grammar rules', 'Only punctuation']),
    ('A theme in literature is:', ['The central message or lesson', 'The setting of the story', 'The name of the writer', 'The number of chapters']),
    ('Identify the simile: Her smile was like sunshine.', ['Her smile was like sunshine', 'The sun smiled brightly', 'Sunshine spread quietly', 'The bright, warm sun']),
    ('Identify the metaphor: Time is a thief.', ['Time is a thief', 'Time flies like a jet', 'Time ticks loudly', 'Time waits patiently, like a friend']),
    ('A paradox is a statement that:', ['Seems contradictory but reveals a truth', 'Is always literally true', 'Uses only rhyme', 'Has no meaning']),
]))

all_worksheets.append(make_ws('Language', 7, 'Persuasive and Argumentative Writing', [
    ('A thesis statement in a persuasive essay:', ['States the writer main argument', 'Lists random facts', 'Summarizes an unrelated topic', 'Is always a question']),
    ('A counterargument:', ['Presents an opposing viewpoint', 'Repeats the main claim', 'Ignores the topic', 'Is always false']),
    ('Rebutting a counterargument means:', ['Responding to it with evidence', 'Ignoring it completely', 'Agreeing without explanation', 'Changing the topic']),
    ('Ethos in persuasive writing appeals to:', ['Credibility and trust', 'Emotion', 'Logic and reason', 'Humor']),
    ('Pathos in persuasive writing appeals to:', ['Emotion', 'Credibility', 'Logic', 'Statistics only']),
    ('Logos in persuasive writing appeals to:', ['Logic and evidence', 'Emotion', 'Trustworthiness', 'Humor']),
    ('A call to action:', ['Urges the reader to do something', 'Summarizes the essay', 'Introduces a counterargument', 'States the topic only']),
    ('Strong persuasive writing uses evidence such as:', ['Facts, statistics, and expert opinions', 'Only personal opinions', 'Random guesses', 'Unrelated stories']),
    ('A biased argument:', ['Unfairly favors one side without balance', 'Presents all sides equally', 'Uses no evidence at all', 'Is always persuasive']),
    ('Which sentence is the strongest thesis statement?', ['Schools should extend recess to improve student focus', 'Recess is sometimes fun', 'Some students like recess', 'Recess happens every day']),
    ('A logical fallacy is:', ['A flawed piece of reasoning', 'A strong piece of evidence', 'A type of citation', 'A grammar error']),
    ('An appeal to emotion that ignores logic can be:', ['Manipulative if overused', 'Always the best approach', 'Required in every essay', 'Illegal to use']),
    ('A well-organized persuasive essay typically includes:', ['An introduction, body arguments, and a conclusion', 'Only a conclusion', 'Random unordered paragraphs', 'No clear structure']),
    ('Citing a source in persuasive writing helps:', ['Build credibility', 'Weaken the argument', 'Confuse the reader', 'Replace the thesis']),
    ('The tone of a persuasive essay should generally be:', ['Confident and reasoned', 'Angry and dismissive', 'Uncertain and vague', 'Sarcastic throughout']),
]))

all_worksheets.append(make_ws('Language', 8, 'Essay Structure and Paragraph Development', [
    ('A topic sentence:', ['States the main idea of a paragraph', 'Ends a paragraph', 'Is always a question', 'Lists citations']),
    ('The introduction of an essay usually includes:', ['A hook and thesis statement', 'Only the conclusion', 'Random facts', 'A bibliography']),
    ('A body paragraph should:', ['Support the thesis with evidence', 'Contradict the thesis', 'Repeat the introduction', 'Contain no evidence']),
    ('A conclusion paragraph should:', ['Restate the thesis and summarize key points', 'Introduce brand new arguments', 'Repeat the essay word for word', 'Ask unrelated questions']),
    ('Transition words help:', ['Connect ideas smoothly between sentences', 'Confuse the reader', 'Replace evidence', 'End an essay abruptly']),
    ('Which is a strong topic sentence?', ['Recycling programs reduce landfill waste significantly', 'Recycling is a word', 'Some people recycle sometimes', 'Landfills exist in many places']),
    ('A hook at the start of an essay is meant to:', ['Capture reader interest', 'Summarize the whole essay', 'List sources', 'End the introduction abruptly']),
    ('Coherence in an essay refers to:', ['Logical flow between ideas', 'Random paragraph order', 'Long sentences only', 'Short essays only']),
    ('Unity in a paragraph means:', ['All sentences relate to one main idea', 'Sentences can be off topic', 'Every sentence is a question', 'Paragraphs have no order']),
    ('Evidence in a body paragraph should be:', ['Relevant and clearly explained', 'Random and unexplained', 'Left out completely', 'Contradictory to the thesis']),
    ('A well-structured essay typically has:', ['An introduction, several body paragraphs, and a conclusion', 'Only one paragraph', 'No clear order', 'Random headings only']),
    ('Which sentence best restates a thesis in a conclusion?', ['Overall, reducing plastic use helps protect our oceans', 'Plastic exists', 'Oceans are big', 'Some people like plastic']),
    ('A run-on paragraph often lacks:', ['Clear organization', 'Any words', 'A title', 'Punctuation only']),
    ('Peer editing helps writers by:', ['Providing feedback for revision', 'Replacing the writing process', 'Guaranteeing a perfect grade', 'Removing the need for a thesis']),
    ('Revising an essay mainly focuses on:', ['Improving content, clarity, and organization', 'Fixing spelling only', 'Changing the font', 'Adding more pages']),
]))

all_worksheets.append(make_ws('Language', 9, 'Media Literacy and Critical Viewing', [
    ('Media literacy involves:', ['Critically analyzing media messages', 'Believing all media without question', 'Ignoring media entirely', 'Only watching entertainment']),
    ('Bias in a news source can be identified by:', ['Comparing multiple sources and checking for balance', 'Reading only one source', 'Trusting headlines alone', 'Ignoring the writer']),
    ('A credible source typically:', ['Provides evidence and cites reliable information', 'Uses no evidence', 'Is always anonymous', 'Contains only opinions']),
    ('The purpose of an advertisement is usually to:', ['Persuade consumers to buy a product', 'Inform without persuasion', 'Entertain only', 'Educate about history']),
    ('Fake news often:', ['Spreads misinformation to mislead readers', 'Always cites verified sources', 'Is always clearly labeled as false', 'Never spreads online']),
    ('Analyzing camera angles in film helps viewers understand:', ['How the director shapes perspective and mood', 'Only the actors names', 'The budget of the film', 'The film release date']),
    ('A target audience is:', ['The specific group a media message is designed for', 'Everyone equally', 'Only children', 'Only critics']),
    ('Sensationalism in media refers to:', ['Exaggerating stories to provoke strong reactions', 'Reporting calm, balanced facts', 'Ignoring emotional appeal', 'Using no images']),
    ('Fact-checking is important because it helps:', ['Verify the accuracy of information', 'Slow down the reading process', 'Add unnecessary opinions', 'Replace the need for sources']),
    ('Social media algorithms often:', ['Show content based on user engagement patterns', 'Show completely random content', 'Ignore user preferences', 'Remove all bias automatically']),
    ('A primary source is:', ['An original firsthand account or document', 'A summary written by someone else', 'Always fictional', 'Never reliable']),
    ('A secondary source:', ['Interprets or analyzes primary sources', 'Is always more accurate than a primary source', 'Cannot be trusted', 'Has no author']),
    ('Editing techniques in film, such as quick cuts, can create a feeling of:', ['Tension or excitement', 'Boredom only', 'Silence only', 'Confusion with no purpose']),
    ('When evaluating a website, readers should check:', ['The author, date, and purpose of the site', 'Only the color scheme', 'The number of ads', 'The font size']),
    ('Media convergence refers to:', ['The merging of different media forms and technologies', 'The disappearance of all media', 'A single television channel', 'A printing technique only']),
]))

all_worksheets.append(make_ws('Language', 10, 'Oral Communication and Presentation Skills', [
    ('Eye contact during a presentation helps:', ['Engage the audience and show confidence', 'Distract the speaker', 'Replace preparation', 'Confuse listeners']),
    ('Effective public speaking requires:', ['Clear organization and confident delivery', 'Reading silently to yourself', 'Avoiding eye contact', 'Speaking as quietly as possible']),
    ('Active listening involves:', ['Fully focusing on and understanding the speaker', 'Interrupting frequently', 'Thinking about unrelated topics', 'Ignoring body language']),
    ('Nonverbal cues include:', ['Gestures, posture, and facial expressions', 'Only written words', 'Only punctuation', 'Only vocabulary choice']),
    ('A presentation outline helps speakers:', ['Organize ideas logically before speaking', 'Memorize every single word', 'Avoid preparing visuals', 'Skip the introduction']),
    ('Pacing in a speech refers to:', ['The speed and rhythm of delivery', 'The topic chosen', 'The visual aids used', 'The length of the room']),
    ('Filler words such as um and like should be:', ['Minimized for clearer delivery', 'Used as often as possible', 'Required in every sentence', 'Ignored by the audience']),
    ('Visual aids in a presentation should:', ['Support and clarify the spoken content', 'Replace the entire speech', 'Be ignored by the audience', 'Contain no relevant information']),
    ('Group discussions are most effective when participants:', ['Listen respectfully and share ideas', 'Talk over each other constantly', 'Refuse to share opinions', 'Ignore the topic']),
    ('Tone of voice during a speech can convey:', ['Emotion and emphasis', 'Nothing important', 'Only volume', 'Only speed']),
    ('Rehearsing a presentation helps speakers:', ['Build confidence and improve delivery', 'Memorize unrelated topics', 'Avoid using visual aids', 'Skip audience engagement']),
    ('A strong speech introduction should:', ['Capture attention and state the purpose', 'List every source immediately', 'Be the longest part of the speech', 'Avoid mentioning the topic']),
    ('Adjusting language for a specific audience is called:', ['Audience awareness', 'Formal punctuation', 'Grammar correction', 'Media convergence']),
    ('Constructive feedback after a presentation should be:', ['Specific and helpful for improvement', 'Vague and unhelpful', 'Purely negative', 'Focused only on appearance']),
    ('Posture during a presentation can affect:', ['How confident a speaker appears', 'Only the topic chosen', 'The color of visual aids', 'The room temperature']),
]))

# ==================== MATH ====================

all_worksheets.append(make_ws('Math', 1, 'Order of Operations and Number Sense', [
    ('Evaluate: 3 + 4 x 2', ['11', '14', '10', '9']),
    ('Evaluate: (5 + 3) x 2', ['16', '11', '13', '10']),
    ('Evaluate: 20 divided by 4 + 1', ['6', '5', '4', '24']),
    ('Evaluate: 2 to the power of 3, plus 1', ['9', '8', '7', '6']),
    ('Evaluate: 10 minus 2 x 3', ['4', '24', '8', '6']),
    ('Which operation is performed first in 6 + 2 x (5 minus 3)?', ['The bracket', 'The addition', 'The multiplication', 'It does not matter']),
    ('Evaluate: 15 divided by 3 x 2', ['10', '5', '2', '12']),
    ('A rational number can be written as:', ['A fraction of two integers', 'Only a whole number', 'Only a decimal', 'Never as a fraction']),
    ('Which of these is an integer?', ['-7', '2.5', 'One half', 'Square root of 2']),
    ('The absolute value of -8 is:', ['8', '-8', '0', '16']),
    ('Evaluate: 4 squared minus 3 squared', ['7', '1', '25', '49']),
    ('Which set includes all natural numbers, whole numbers, and integers?', ['Rational numbers', 'Irrational numbers', 'Imaginary numbers', 'None of these']),
    ('Evaluate: 2 x (3 + 4) minus 5', ['9', '14', '5', '19']),
    ('Estimate the value of 39 x 21 by rounding.', ['800', '400', '900', '700']),
    ('Evaluate: 100 divided by (5 x 2)', ['10', '20', '50', '2']),
]))

all_worksheets.append(make_ws('Math', 2, 'Algebraic Expressions Practice', [
    ('Simplify: 3x + 5x', ['8x', '15x', '2x', '8x squared']),
    ('Simplify: 7y minus 2y', ['5y', '9y', '5', '14y']),
    ('Evaluate 2x + 3 when x = 4', ['11', '9', '10', '14']),
    ('Simplify: 4(2x + 3)', ['8x + 12', '8x + 3', '6x + 12', '8x + 7']),
    ('Simplify: 3(x + 2) + 2x', ['5x + 6', '3x + 6', '5x + 2', '6x + 6']),
    ('Simplify: 5a + 3b minus 2a + b', ['3a + 4b', '3a + 2b', '8a + 4b', '3a + 3b']),
    ('Expand: -2(x minus 3)', ['-2x + 6', '-2x - 6', '2x + 6', '-2x - 3']),
    ('Evaluate 3x squared when x = 2', ['12', '6', '9', '36']),
    ('Simplify: 6x divided by 2', ['3x', '12x', '3', '4x']),
    ('Combine like terms: 4m + 2n + 3m minus n', ['7m + n', '7m + 2n', '4m + 3n', '6m + n']),
    ('Simplify: 2(x + y) + 3(x - y)', ['5x - y', '5x + y', 'x - y', '5x - 5y']),
    ('Evaluate 5 minus 2x when x = -3', ['11', '1', '-1', '-11']),
    ('Simplify: x times x times x', ['x cubed', '3x', 'x squared', 'x']),
    ('Which expression is equivalent to 3x + 3x + 3x?', ['9x', '3x cubed', '6x', '27x']),
    ('Simplify: 10x minus 4x + 2', ['6x + 2', '6x', '14x + 2', '6x - 2']),
]))

all_worksheets.append(make_ws('Math', 3, 'Solving Linear Equations', [
    ('Solve: x + 5 = 12', ['x = 7', 'x = 17', 'x = 5', 'x = -7']),
    ('Solve: 3x = 15', ['x = 5', 'x = 45', 'x = 3', 'x = 18']),
    ('Solve: x minus 4 = 10', ['x = 14', 'x = 6', 'x = -14', 'x = 40']),
    ('Solve: 2x + 3 = 11', ['x = 4', 'x = 7', 'x = 8', 'x = 14']),
    ('Solve: x divided by 3 = 6', ['x = 18', 'x = 2', 'x = 9', 'x = 3']),
    ('Solve: 4x minus 5 = 11', ['x = 4', 'x = 6', 'x = 1.5', 'x = 16']),
    ('Solve: 2(x + 3) = 14', ['x = 4', 'x = 8', 'x = 7', 'x = 11']),
    ('Solve: 5x + 2 = 3x + 10', ['x = 4', 'x = 2', 'x = 8', 'x = -4']),
    ('Solve: 3x minus 7 = 2x + 1', ['x = 8', 'x = 6', 'x = -8', 'x = -6']),
    ('Solve: x/2 + 3 = 7', ['x = 8', 'x = 2', 'x = 14', 'x = 20']),
    ('Solve: -2x = 10', ['x = -5', 'x = 5', 'x = -20', 'x = 20']),
    ('Solve: 7 minus x = 2', ['x = 5', 'x = 9', 'x = -5', 'x = -9']),
    ('Solve: 3(x minus 2) = 9', ['x = 5', 'x = 3', 'x = 7', 'x = 1']),
    ('Which equation represents: a number increased by 6 equals 20?', ['x + 6 = 20', 'x - 6 = 20', '6x = 20', 'x/6 = 20']),
    ('Solve: 6x + 4 = 4x + 10', ['x = 3', 'x = 6', 'x = 1', 'x = 7']),
]))

all_worksheets.append(make_ws('Math', 4, 'Graphing Linear Relations', [
    ('The slope of a line measures:', ['Steepness and direction', 'Only the y-intercept', 'Only the x-intercept', 'The length of the line']),
    ('The y-intercept is the point where a line crosses:', ['The y-axis', 'The x-axis', 'The origin only', 'Neither axis']),
    ('Find the slope between points (0,0) and (2,4).', ['2', '4', '0.5', '8']),
    ('The equation y = mx + b is called:', ['Slope-intercept form', 'Standard form', 'Point-slope form', 'Vertex form']),
    ('In y = 3x + 2, the slope is:', ['3', '2', '5', '-3']),
    ('In y = 3x + 2, the y-intercept is:', ['2', '3', '0', '5']),
    ('A line with slope 0 is:', ['Horizontal', 'Vertical', 'Diagonal', 'Undefined']),
    ('A vertical line has a slope that is:', ['Undefined', 'Zero', 'Positive', 'Negative']),
    ('Find the slope between points (1,2) and (3,6).', ['2', '4', '0.5', '8']),
    ('Which point lies on the line y = 2x + 1?', ['(1,3)', '(1,2)', '(2,3)', '(0,2)']),
    ('A line rising from left to right has a slope that is:', ['Positive', 'Negative', 'Zero', 'Undefined']),
    ('A line falling from left to right has a slope that is:', ['Negative', 'Positive', 'Zero', 'Undefined']),
    ('The x-intercept of a line is where it crosses:', ['The x-axis', 'The y-axis', 'The slope', 'The origin only']),
    ('Parallel lines have:', ['The same slope', 'Different slopes', 'Slopes that multiply to -1', 'No slope at all']),
    ('Find the y-intercept of y = -4x + 7', ['7', '-4', '4', '-7']),
]))

all_worksheets.append(make_ws('Math', 5, 'Exponent Laws and Polynomials', [
    ('Simplify: x squared times x cubed', ['x to the fifth', 'x to the sixth', 'x to the first', '2x to the fifth']),
    ('Simplify: x to the fifth divided by x squared', ['x cubed', 'x to the seventh', 'x squared', 'x']),
    ('Simplify: (x squared) cubed', ['x to the sixth', 'x to the fifth', 'x to the eighth', 'x squared']),
    ('Any nonzero number to the power of 0 equals:', ['1', '0', 'The number itself', 'Undefined']),
    ('Simplify: 2 to the power of -1', ['One half', '-2', '2', '-1']),
    ('Add the polynomials: (2x + 3) + (5x - 1)', ['7x + 2', '7x + 4', '3x + 2', '10x + 2']),
    ('Subtract the polynomials: (4x + 6) minus (2x + 1)', ['2x + 5', '2x + 7', '6x + 5', '2x - 5']),
    ('Multiply: (x + 2)(x + 3)', ['x squared + 5x + 6', 'x squared + 6', 'x squared + 5x', 'x squared + 6x + 5']),
    ('Multiply: 3x times 4x', ['12x squared', '7x', '12x', '7x squared']),
    ('Simplify: (3x squared)(2x)', ['6x cubed', '6x squared', '5x cubed', '6x']),
    ('Expand: (x - 4)(x + 4)', ['x squared minus 16', 'x squared plus 16', 'x squared minus 8x minus 16', 'x squared minus 4']),
    ('The degree of the polynomial 3x cubed + 2x minus 5 is:', ['3', '2', '5', '1']),
    ('Identify the leading coefficient of 4x squared minus 3x + 1', ['4', '-3', '1', '2']),
    ('Simplify: (2x) squared', ['4x squared', '2x squared', '4x', '2x to the fourth']),
    ('Combine: 3x squared + 2x squared', ['5x squared', '6x to the fourth', '5x', '6x squared']),
]))

all_worksheets.append(make_ws('Math', 6, 'Ratios, Rates, and Proportional Reasoning', [
    ('A ratio compares:', ['Two quantities by division', 'Two quantities by addition', 'Only whole numbers', 'Only percentages']),
    ('Simplify the ratio 12:16', ['3:4', '4:3', '6:8', '2:3']),
    ('A rate compares quantities measured in:', ['Different units', 'The same unit only', 'Whole numbers only', 'Percentages only']),
    ('If a car travels 240 km in 4 hours, its rate is:', ['60 km per hour', '40 km per hour', '240 km per hour', '4 km per hour']),
    ('Solve the proportion: 3/4 = x/12', ['x = 9', 'x = 8', 'x = 16', 'x = 6']),
    ('A unit rate expresses a quantity per:', ['One unit', 'Ten units', 'A hundred units', 'An unknown amount']),
    ('If 5 apples cost 2 dollars, how much do 15 apples cost?', ['6 dollars', '4 dollars', '10 dollars', '3 dollars']),
    ('Two ratios that are equal form a:', ['Proportion', 'Percentage', 'Fraction', 'Rate']),
    ('A map scale of 1:100000 means 1 cm represents:', ['100000 cm in reality', '1 cm in reality', '100 cm in reality', '1000 cm in reality']),
    ('If the ratio of boys to girls is 3:5 in a class of 24, how many boys are there?', ['9', '15', '8', '12']),
    ('Solve the proportion: 6/x = 2/5', ['x = 15', 'x = 12', 'x = 10', 'x = 3']),
    ('A recipe uses a ratio of 2 cups flour to 3 cups sugar. For 6 cups flour, how much sugar is needed?', ['9 cups', '6 cups', '4 cups', '12 cups']),
    ('Which ratio is equivalent to 2:5?', ['4:10', '5:2', '10:20', '3:6']),
    ('Speed is an example of a:', ['Rate', 'Ratio only', 'Percentage', 'Whole number']),
    ('If 8 workers finish a job in 6 days, how many days for 4 workers at the same rate?', ['12 days', '3 days', '24 days', '6 days']),
]))

all_worksheets.append(make_ws('Math', 7, 'Measurement: Perimeter, Area, and Volume', [
    ('The perimeter of a rectangle with length 8 and width 5 is:', ['26', '40', '13', '20']),
    ('The area of a rectangle with length 8 and width 5 is:', ['40', '26', '13', '20']),
    ('The area of a triangle with base 10 and height 6 is:', ['30', '60', '16', '20']),
    ('The circumference of a circle is found using:', ['2 times pi times radius', 'Pi times radius squared', '2 times radius', 'Pi times diameter squared']),
    ('The area of a circle is found using:', ['Pi times radius squared', '2 times pi times radius', 'Pi times diameter', '2 times radius squared']),
    ('The volume of a rectangular prism with dimensions 3, 4, and 5 is:', ['60', '12', '20', '47']),
    ('The volume of a cylinder is found using:', ['Pi times radius squared times height', '2 times pi times radius times height', 'Length times width times height', 'Pi times diameter times height']),
    ('Convert 2.5 meters to centimeters.', ['250 cm', '25 cm', '2500 cm', '0.25 cm']),
    ('The surface area of a cube with side length 4 is:', ['96', '64', '16', '24']),
    ('A rectangular prism has volume 120 and base area 20. Its height is:', ['6', '5', '24', '100']),
    ('The perimeter of a square with side length 7 is:', ['28', '49', '14', '21']),
    ('The area of a parallelogram with base 9 and height 4 is:', ['36', '13', '18', '72']),
    ('Convert 3000 milliliters to liters.', ['3 liters', '30 liters', '0.3 liters', '300 liters']),
    ('The volume of a cube with side length 5 is:', ['125', '25', '15', '100']),
    ('The area of a trapezoid with parallel sides 6 and 10 and height 4 is:', ['32', '40', '16', '24']),
]))

all_worksheets.append(make_ws('Math', 8, 'Analytic Geometry: Slope and Line Equations', [
    ('The slope formula between two points (x1,y1) and (x2,y2) is:', ['(y2-y1)/(x2-x1)', '(x2-x1)/(y2-y1)', '(y2+y1)/(x2+x1)', '(x2+y2)/(x1+y1)']),
    ('Find the slope between (2,3) and (5,9).', ['2', '3', '6', '0.5']),
    ('The equation of a line with slope 4 and y-intercept -2 is:', ['y = 4x - 2', 'y = -2x + 4', 'y = 4x + 2', 'y = 2x - 4']),
    ('Two lines are perpendicular if their slopes:', ['Multiply to -1', 'Are equal', 'Multiply to 1', 'Add to zero']),
    ('Find the midpoint of (2,4) and (6,8).', ['(4,6)', '(8,12)', '(2,4)', '(4,4)']),
    ('The distance formula is derived from:', ['The Pythagorean theorem', 'The slope formula', 'The midpoint formula', 'The area formula']),
    ('Find the distance between (0,0) and (3,4).', ['5', '7', '12', '25']),
    ('A line passing through the origin has an equation of the form:', ['y = mx', 'y = mx + b where b is not 0', 'x = constant only', 'y = constant only']),
    ('The point-slope form of a line is:', ['y - y1 = m(x - x1)', 'y = mx + b', 'Ax + By = C', 'y1 = mx1 + b']),
    ('Find the equation of a line through (1,2) with slope 3.', ['y = 3x - 1', 'y = 3x + 2', 'y = x + 2', 'y = 3x - 3']),
    ('If two lines have the same slope but different y-intercepts, they are:', ['Parallel', 'Perpendicular', 'Identical', 'Intersecting at one point only']),
    ('Convert y = 2x + 5 to standard form.', ['2x - y = -5', '2x + y = 5', 'x - 2y = 5', '2x - y = 5']),
    ('Find the slope of the line 3x + y = 6', ['-3', '3', '6', '-6']),
    ('The midpoint formula is:', ['((x1+x2)/2, (y1+y2)/2)', '(x2-x1, y2-y1)', '(x1x2, y1y2)', '((x1-x2)/2, (y1-y2)/2)']),
    ('A line with an undefined slope is:', ['Vertical', 'Horizontal', 'Diagonal', 'Curved']),
]))

all_worksheets.append(make_ws('Math', 9, 'Financial Literacy: Percent and Interest', [
    ('Convert 0.25 to a percent.', ['25 percent', '2.5 percent', '250 percent', '0.25 percent']),
    ('What is 20 percent of 150?', ['30', '20', '15', '130']),
    ('Simple interest is calculated using:', ['Principal times rate times time', 'Principal plus rate', 'Rate divided by time', 'Principal times time only']),
    ('If you invest 1000 dollars at 5 percent simple interest for 2 years, the interest earned is:', ['100 dollars', '50 dollars', '1000 dollars', '200 dollars']),
    ('A 15 percent discount on a 200 dollar item saves:', ['30 dollars', '15 dollars', '20 dollars', '185 dollars']),
    ('Sales tax of 13 percent on a 50 dollar item adds:', ['6.50 dollars', '13 dollars', '5 dollars', '63 dollars']),
    ('If a price increases from 80 to 100 dollars, the percent increase is:', ['25 percent', '20 percent', '80 percent', '100 percent']),
    ('Compound interest differs from simple interest because it:', ['Earns interest on interest already earned', 'Only applies to loans', 'Is always lower', 'Never changes over time']),
    ('A commission of 10 percent on 500 dollars in sales equals:', ['50 dollars', '10 dollars', '100 dollars', '5 dollars']),
    ('What percent is 45 out of 60?', ['75 percent', '60 percent', '45 percent', '80 percent']),
    ('A budget allocates 30 percent of 2000 dollars to rent. How much is that?', ['600 dollars', '300 dollars', '60 dollars', '200 dollars']),
    ('A loan has a 6 percent annual simple interest rate. Over 3 years, the total interest rate factor is:', ['18 percent total', '6 percent total', '9 percent total', '3 percent total']),
    ('A price drops from 50 to 40 dollars. The percent decrease is:', ['20 percent', '10 percent', '25 percent', '40 percent']),
    ('Net income equals:', ['Gross income minus deductions', 'Gross income plus deductions', 'Gross income only', 'Deductions only']),
    ('Which is the best strategy for saving money over time?', ['Setting a budget and saving regularly', 'Spending before saving', 'Ignoring interest rates', 'Avoiding all planning']),
]))

all_worksheets.append(make_ws('Math', 10, 'Data Management and Statistics', [
    ('The mean of a data set is:', ['The sum of values divided by the number of values', 'The most frequent value', 'The middle value', 'The largest value']),
    ('The median of a data set is:', ['The middle value when ordered', 'The average of all values', 'The most frequent value', 'The range']),
    ('The mode of a data set is:', ['The most frequently occurring value', 'The middle value', 'The average', 'The difference between highest and lowest']),
    ('The range of a data set is:', ['The difference between the highest and lowest values', 'The average value', 'The most common value', 'The middle value']),
    ('Find the mean of: 4, 8, 6, 10, 2', ['6', '8', '10', '4']),
    ('Find the median of: 3, 7, 9, 2, 5', ['5', '7', '9', '3']),
    ('A bar graph is best used to:', ['Compare categories of data', 'Show change over continuous time', 'Show parts of a whole only', 'Show correlation only']),
    ('A line graph is best used to:', ['Show trends over time', 'Compare unrelated categories', 'Show a single value', 'Show percentages only']),
    ('A circle graph, or pie chart, shows:', ['Parts of a whole as percentages', 'Change over time', 'The correlation between two variables', 'Only raw counts']),
    ('An outlier in a data set is:', ['A value far from the other values', 'The average value', 'The most common value', 'The middle value']),
    ('A scatter plot is used to show:', ['The relationship between two variables', 'A single category total', 'Data over time only', 'Percentages of a whole']),
    ('Probability is expressed as a number between:', ['0 and 1', '-1 and 1', '1 and 100', '0 and 100 only']),
    ('The probability of flipping heads on a fair coin is:', ['One half', 'One quarter', 'One third', 'Zero']),
    ('A survey sample should be:', ['Representative of the population', 'As small as possible', 'Biased toward one group', 'Ignored after collection']),
    ('If a die is rolled, the probability of rolling a 4 is:', ['One sixth', 'One fourth', 'One third', 'One half']),
]))

# ==================== SCIENCE ====================

all_worksheets.append(make_ws('Science', 1, 'Scientific Method and Lab Safety', [
    ('The first step of the scientific method is usually:', ['Asking a question or identifying a problem', 'Forming a conclusion', 'Publishing results', 'Skipping observation']),
    ('A hypothesis is:', ['A testable prediction', 'A proven fact', 'A random guess with no reasoning', 'The final conclusion']),
    ('An independent variable is:', ['The factor that is deliberately changed', 'The factor being measured', 'Always time', 'Never controlled']),
    ('A dependent variable is:', ['The factor being measured or observed', 'The factor being changed', 'Always constant', 'Irrelevant to the experiment']),
    ('A controlled variable is:', ['Kept constant to ensure a fair test', 'Always changed', 'Never measured', 'The main result']),
    ('Safety goggles should be worn in a lab to:', ['Protect eyes from chemicals and debris', 'Improve vision permanently', 'Replace lab coats', 'Block out light only']),
    ('If a chemical spills on skin, the first step should be:', ['Rinse with water immediately', 'Wait and observe', 'Cover with a bandage', 'Ignore it']),
    ('A control group in an experiment:', ['Does not receive the experimental treatment', 'Always receives the treatment', 'Is not needed', 'Is the same as the variable']),
    ('Data should be recorded during an experiment to:', ['Ensure accuracy and allow analysis', 'Slow down the process', 'Replace observation', 'Avoid drawing conclusions']),
    ('A conclusion in a lab report should:', ['Be based on the collected data', 'Ignore the data collected', 'Always confirm the hypothesis', 'Be written before the experiment']),
    ('Long hair should be tied back in a lab to:', ['Prevent it from catching fire or contaminating samples', 'Look more professional only', 'Save time', 'Improve results']),
    ('Which of these is proper lab equipment cleanup?', ['Washing and returning equipment to its place', 'Leaving equipment out', 'Throwing equipment away', 'Ignoring cleanup']),
    ('A scientific theory is:', ['A well-supported explanation based on repeated evidence', 'An unproven guess', 'The same as a hypothesis', 'Always eventually disproven']),
    ('Repeating an experiment multiple times helps:', ['Confirm the reliability of results', 'Waste materials', 'Change the hypothesis each time', 'Avoid analysis']),
    ('Reading chemical labels before use helps prevent:', ['Accidents from unknown hazards', 'Faster results', 'Better organization only', 'Increased cost']),
]))

all_worksheets.append(make_ws('Science', 2, 'Ecosystems and Sustainability', [
    ('An ecosystem includes:', ['Living organisms and their nonliving environment', 'Only living organisms', 'Only nonliving factors', 'Only plants']),
    ('A producer in an ecosystem:', ['Makes its own food through photosynthesis', 'Eats other organisms only', 'Breaks down dead matter', 'Cannot survive without prey']),
    ('A consumer in an ecosystem:', ['Obtains energy by eating other organisms', 'Makes its own food', 'Is always a plant', 'Never moves']),
    ('A decomposer breaks down:', ['Dead organic matter into nutrients', 'Only living organisms', 'Sunlight into energy', 'Water into oxygen']),
    ('Energy in an ecosystem generally flows:', ['From producers to consumers to decomposers', 'From decomposers to producers only', 'In a closed loop with no loss', 'Backwards from consumers to the sun']),
    ('A food web shows:', ['Multiple interconnected food chains', 'A single unrelated chain', 'Only predators', 'Only producers']),
    ('Biodiversity refers to:', ['The variety of life in an ecosystem', 'The size of an ecosystem', 'The number of decomposers only', 'The climate of a region']),
    ('Sustainability means meeting present needs:', ['Without compromising future generations ability to meet their needs', 'By using all resources immediately', 'Without considering the future', 'By ignoring the environment']),
    ('An invasive species can:', ['Disrupt native ecosystems by outcompeting native species', 'Always help native species', 'Have no ecological impact', 'Only exist in water']),
    ('A limiting factor in an ecosystem:', ['Restricts the growth of a population', 'Always increases population size', 'Has no effect on population', 'Only applies to plants']),
    ('Carrying capacity refers to:', ['The maximum population an environment can sustain', 'The minimum population needed', 'The total area of a habitat', 'The number of predators only']),
    ('Human activities such as deforestation can:', ['Reduce biodiversity and disrupt ecosystems', 'Always improve ecosystems', 'Have no effect on ecosystems', 'Only affect oceans']),
    ('A keystone species:', ['Has a large effect on ecosystem stability relative to its abundance', 'Has no ecological importance', 'Is always a predator', 'Is always extinct']),
    ('Renewable resources:', ['Can be replenished naturally over time', 'Cannot be replenished at all', 'Are always fossil fuels', 'Never run out under any use']),
    ('Conservation efforts aim to:', ['Protect and sustainably manage natural resources', 'Use all resources as quickly as possible', 'Ignore endangered species', 'Increase pollution']),
]))

all_worksheets.append(make_ws('Science', 3, 'Atomic Theory and the Periodic Table', [
    ('An atom consists mainly of:', ['Protons, neutrons, and electrons', 'Only protons', 'Only electrons', 'Only neutrons']),
    ('Protons are located in the:', ['Nucleus', 'Electron cloud', 'Outside the atom', 'Between atoms']),
    ('Electrons are located:', ['In the electron cloud surrounding the nucleus', 'In the nucleus', 'Outside the atom entirely', 'Fused with protons']),
    ('The atomic number of an element represents:', ['The number of protons', 'The number of neutrons', 'The total mass', 'The number of isotopes']),
    ('Isotopes of an element have:', ['The same number of protons but different neutrons', 'Different protons', 'The same mass always', 'No neutrons']),
    ('Elements in the same group of the periodic table:', ['Share similar chemical properties', 'Always have the same mass', 'Are always metals', 'Have no relationship']),
    ('Metals are generally located on the periodic table:', ['On the left and center', 'On the far right', 'Only in the middle row', 'Nowhere specific']),
    ('Noble gases are known for being:', ['Mostly unreactive', 'Highly reactive with metals', 'Always liquids', 'Always radioactive']),
    ('The periodic table is organized by increasing:', ['Atomic number', 'Alphabetical order', 'Color', 'Random order']),
    ('A period on the periodic table is a:', ['Horizontal row', 'Vertical column', 'Diagonal line', 'Single element']),
    ('A group on the periodic table is a:', ['Vertical column', 'Horizontal row', 'Random cluster', 'A single period']),
    ('Valence electrons are:', ['Electrons in the outermost energy level', 'Electrons in the nucleus', 'Only found in noble gases', 'Always equal to atomic number']),
    ('Atomic mass is primarily determined by:', ['The number of protons and neutrons', 'The number of electrons only', 'The charge of the atom', 'The atomic number alone']),
    ('Metalloids have properties that are:', ['Between metals and nonmetals', 'Identical to noble gases', 'Purely metallic', 'Purely nonmetallic']),
    ('The nucleus of an atom is:', ['Small, dense, and positively charged', 'Large and negatively charged', 'Spread throughout the atom', 'Always neutral in charge only']),
]))

all_worksheets.append(make_ws('Science', 4, 'Chemical Reactions and Balancing Equations', [
    ('In a chemical reaction, mass is:', ['Conserved, staying the same before and after', 'Always lost', 'Always gained', 'Converted into pure energy only']),
    ('A synthesis reaction combines:', ['Two or more substances into one compound', 'One compound into elements', 'Two acids together only', 'Nothing at all']),
    ('A decomposition reaction breaks down:', ['One compound into two or more substances', 'Two elements into a compound', 'A gas into a liquid only', 'Nothing at all']),
    ('In the equation 2H2 + O2 to 2H2O, the coefficient 2 in front of H2 indicates:', ['Two molecules of hydrogen gas', 'Two atoms of oxygen', 'Two moles of water only', 'Two electrons']),
    ('Balancing chemical equations ensures:', ['The same number of atoms of each element on both sides', 'Different numbers of atoms on each side', 'Only mass on the reactant side counts', 'Reactions never balance']),
    ('A combustion reaction typically produces:', ['Carbon dioxide and water', 'Only oxygen', 'Only metal oxides', 'Only salts']),
    ('An exothermic reaction:', ['Releases energy, often as heat', 'Absorbs energy only', 'Has no energy change', 'Only occurs in living things']),
    ('An endothermic reaction:', ['Absorbs energy from its surroundings', 'Releases energy only', 'Never occurs naturally', 'Always explosive']),
    ('A single replacement reaction occurs when:', ['One element replaces another in a compound', 'Two compounds swap parts', 'A compound breaks into elements', 'Two elements combine only']),
    ('A double replacement reaction occurs when:', ['Two compounds exchange ions to form new compounds', 'One element replaces another', 'A compound decomposes', 'Two gases combine only']),
    ('Balance the equation: N2 + H2 to NH3. The correct coefficients are:', ['N2 + 3H2 to 2NH3', 'N2 + H2 to NH3', '2N2 + H2 to NH3', 'N2 + 2H2 to NH3']),
    ('A precipitate formed in a reaction is:', ['An insoluble solid formed from a solution', 'A gas released', 'A color change only', 'A temperature change']),
    ('Signs of a chemical reaction include:', ['Gas production, color change, and precipitate formation', 'Only a change in shape', 'Only a change in size', 'No observable changes ever']),
    ('The law of conservation of mass states that mass:', ['Cannot be created or destroyed in a chemical reaction', 'Is always created in reactions', 'Is always destroyed in reactions', 'Doubles during reactions']),
    ('A catalyst in a reaction:', ['Speeds up the reaction without being consumed', 'Slows down the reaction always', 'Is always consumed completely', 'Has no effect on rate']),
]))

all_worksheets.append(make_ws('Science', 5, 'Static and Current Electricity', [
    ('Static electricity results from:', ['A buildup of electric charge on a surface', 'Continuous flow of charge', 'Magnetism only', 'Heat transfer only']),
    ('Current electricity is:', ['The continuous flow of electric charge through a conductor', 'A stationary charge', 'Only found in batteries', 'Never measurable']),
    ('An electric circuit requires:', ['A closed conducting path for current to flow', 'An open path only', 'No power source', 'Only insulators']),
    ('A conductor is a material that:', ['Allows electric current to flow easily', 'Blocks electric current completely', 'Only conducts heat', 'Never conducts anything']),
    ('An insulator is a material that:', ['Resists the flow of electric current', 'Allows current to flow freely', 'Is always metal', 'Generates its own current']),
    ('In a series circuit, if one component fails:', ['The entire circuit stops working', 'Only that component stops', 'Nothing changes', 'All components work harder']),
    ('In a parallel circuit, if one branch fails:', ['The other branches can continue working', 'The entire circuit stops', 'No current flows anywhere', 'All branches fail']),
    ('Voltage is a measure of:', ['Electrical potential difference', 'Current flow rate', 'Resistance only', 'Power only']),
    ('Current is measured in:', ['Amperes', 'Volts', 'Ohms', 'Watts']),
    ('Resistance is measured in:', ['Ohms', 'Volts', 'Amperes', 'Watts']),
    ('Ohm law relates voltage, current, and resistance as:', ['Voltage equals current times resistance', 'Voltage equals current divided by resistance', 'Current equals voltage times resistance', 'Resistance equals voltage times current']),
    ('A battery provides electrical energy through:', ['A chemical reaction', 'Mechanical motion only', 'Static friction', 'Light absorption only']),
    ('Grounding an electrical system helps:', ['Prevent electric shock and overload', 'Increase voltage', 'Remove all resistance', 'Stop all current permanently']),
    ('Electric charge that builds up and suddenly discharges causes:', ['A spark', 'Constant current flow', 'Magnetism only', 'No effect']),
    ('A circuit diagram uses symbols to represent:', ['Components such as batteries, switches, and resistors', 'Only wires', 'Only the power source', 'Only the current direction']),
]))

all_worksheets.append(make_ws('Science', 6, 'Circuit Calculations and Electromagnetism', [
    ('Using Ohm law, if voltage is 12V and resistance is 4 ohms, the current is:', ['3 amperes', '48 amperes', '8 amperes', '16 amperes']),
    ('Using Ohm law, if current is 2A and resistance is 5 ohms, the voltage is:', ['10 volts', '2.5 volts', '7 volts', '3 volts']),
    ('Total resistance in a series circuit is found by:', ['Adding all resistances together', 'Averaging the resistances', 'Multiplying the resistances', 'Taking the smallest resistance']),
    ('Total resistance in a parallel circuit is:', ['Less than the smallest individual resistance', 'Equal to the sum of resistances', 'Always infinite', 'Equal to the largest resistance']),
    ('Power in a circuit is calculated as:', ['Voltage times current', 'Voltage divided by current', 'Current divided by voltage', 'Resistance times current only']),
    ('Power is measured in units of:', ['Watts', 'Volts', 'Amperes', 'Ohms']),
    ('An electromagnet is created by:', ['Passing current through a coiled wire around a core', 'Rubbing two magnets together', 'Heating a magnet', 'Freezing a wire']),
    ('Increasing the number of coils in an electromagnet:', ['Increases its magnetic strength', 'Decreases its magnetic strength', 'Has no effect', 'Reverses its polarity only']),
    ('A generator converts:', ['Mechanical energy into electrical energy', 'Electrical energy into mechanical energy only', 'Heat directly into light', 'Sound into electricity']),
    ('A motor converts:', ['Electrical energy into mechanical energy', 'Mechanical energy into electrical energy only', 'Light into sound', 'Heat into static']),
    ('Electromagnetic induction occurs when:', ['A changing magnetic field creates an electric current', 'Two wires touch directly', 'A battery is disconnected', 'Current flows without a circuit']),
    ('A fuse in a circuit is designed to:', ['Break the circuit if current is too high', 'Increase current when overloaded', 'Store electrical energy', 'Generate additional voltage']),
    ('If two 4 ohm resistors are connected in series, the total resistance is:', ['8 ohms', '2 ohms', '4 ohms', '16 ohms']),
    ('If two 4 ohm resistors are connected in parallel, the total resistance is:', ['2 ohms', '8 ohms', '4 ohms', '1 ohm']),
    ('Transformers are used to:', ['Change voltage levels in AC circuits', 'Store chemical energy', 'Generate static electricity only', 'Convert AC into permanent magnets']),
]))

all_worksheets.append(make_ws('Science', 7, 'Earth and Space Science', [
    ('The solar system is held together by:', ['Gravity', 'Magnetism', 'Electric charge', 'Wind']),
    ('The Sun is classified as a:', ['Star', 'Planet', 'Moon', 'Asteroid']),
    ('The order of planets outward from the sun starts with:', ['Mercury', 'Venus', 'Earth', 'Mars']),
    ('A planet orbit around the sun is generally shaped like:', ['An ellipse', 'A perfect circle always', 'A straight line', 'A random, unpredictable path']),
    ('The Moon phases are caused by:', ['The changing angle of sunlight reflecting off the Moon', 'The Moon changing shape', 'The Earth blocking the sun daily', 'The Moon producing its own light']),
    ('A solar eclipse occurs when:', ['The Moon passes between the Earth and the Sun', 'The Earth passes between the Sun and Moon', 'The Sun passes behind the Earth', 'The Moon disappears completely']),
    ('A lunar eclipse occurs when:', ['The Earth passes between the Sun and the Moon', 'The Moon passes between the Earth and Sun', 'The Sun blocks the Moon directly', 'The Moon blocks itself']),
    ('Earth rotation on its axis causes:', ['Day and night', 'The seasons', 'Tides only', 'Eclipses only']),
    ('Earth revolution around the sun, combined with axial tilt, causes:', ['The seasons', 'Day and night', 'Ocean currents only', 'Moon phases']),
    ('A light-year measures:', ['The distance light travels in one year', 'The brightness of a star', 'The time it takes to orbit the sun', 'The temperature of a star']),
    ('A galaxy is:', ['A massive collection of stars, gas, and dust bound by gravity', 'A single star system only', 'The same as a solar system', 'A type of asteroid']),
    ('The layer of the Earth atmosphere closest to the surface is called the:', ['Troposphere', 'Stratosphere', 'Mesosphere', 'Thermosphere']),
    ('Comets are made mostly of:', ['Ice, dust, and rock', 'Pure metal', 'Pure gas only', 'Liquid water only']),
    ('An asteroid belt in our solar system is located mainly between:', ['Mars and Jupiter', 'Earth and Mars', 'Venus and Earth', 'Jupiter and Saturn']),
    ('Stars produce energy primarily through:', ['Nuclear fusion', 'Chemical combustion', 'Gravitational collapse alone', 'Radioactive decay only']),
]))

all_worksheets.append(make_ws('Science', 8, 'Cell Biology and Photosynthesis', [
    ('The basic unit of life is the:', ['Cell', 'Tissue', 'Organ', 'Organ system']),
    ('The function of the cell membrane is to:', ['Control what enters and exits the cell', 'Produce energy only', 'Store genetic information only', 'Build proteins only']),
    ('The nucleus of a cell:', ['Contains genetic material and controls cell activities', 'Produces energy directly', 'Digests waste only', 'Provides structural support only']),
    ('Mitochondria are known as the:', ['Powerhouse of the cell', 'Control center of the cell', 'Storage unit of the cell', 'Protein factory of the cell']),
    ('Chloroplasts are found in:', ['Plant cells', 'Animal cells only', 'Bacteria only', 'Neither plant nor animal cells']),
    ('Photosynthesis converts:', ['Light energy into chemical energy stored in glucose', 'Chemical energy into light energy', 'Oxygen into carbon dioxide only', 'Water into oxygen only, with no other products']),
    ('The general equation for photosynthesis produces:', ['Glucose and oxygen', 'Carbon dioxide and water', 'Only oxygen', 'Only carbon dioxide']),
    ('Cellular respiration converts:', ['Glucose and oxygen into usable energy', 'Energy into glucose directly', 'Only carbon dioxide into oxygen', 'Only water into glucose']),
    ('The products of cellular respiration include:', ['Carbon dioxide, water, and energy', 'Oxygen and glucose only', 'Only chlorophyll', 'Only nitrogen']),
    ('A cell wall, found in plant cells, provides:', ['Structural support and protection', 'Genetic storage only', 'Energy production only', 'Waste removal only']),
    ('The function of the ribosome is to:', ['Build proteins', 'Store energy', 'Control the cell', 'Digest waste']),
    ('Diffusion in cells refers to:', ['Movement of particles from high to low concentration', 'Movement from low to high concentration only', 'Active transport requiring energy always', 'The storage of genetic material']),
    ('Osmosis specifically refers to the movement of:', ['Water across a membrane', 'Proteins across a membrane', 'Genetic material only', 'Oxygen only']),
    ('Unicellular organisms consist of:', ['A single cell', 'Many specialized cells', 'Only plant cells', 'Only animal cells']),
    ('The organelle responsible for breaking down waste in a cell is the:', ['Lysosome', 'Nucleus', 'Chloroplast', 'Ribosome']),
]))

all_worksheets.append(make_ws('Science', 9, 'Plate Tectonics and the Rock Cycle', [
    ('Plate tectonics theory explains:', ['The movement of large sections of the Earth crust', 'Only volcanic eruptions', 'Only earthquakes', 'Only mountain height']),
    ('A convergent boundary occurs when plates:', ['Move toward each other', 'Move apart', 'Slide past each other', 'Remain stationary']),
    ('A divergent boundary occurs when plates:', ['Move apart from each other', 'Move toward each other', 'Slide past each other', 'Collide directly']),
    ('A transform boundary occurs when plates:', ['Slide past each other', 'Move apart', 'Move toward each other', 'Merge completely']),
    ('Earthquakes are most commonly caused by:', ['Sudden movement along a fault', 'Volcanic ash only', 'Ocean currents', 'Wind erosion']),
    ('Volcanoes often form near:', ['Convergent or divergent plate boundaries', 'The center of continents only', 'Transform boundaries exclusively', 'Areas with no tectonic activity']),
    ('Igneous rock forms from:', ['Cooled and solidified magma or lava', 'Compressed sediment', 'Heat and pressure on existing rock', 'Dissolved minerals only']),
    ('Sedimentary rock forms from:', ['Compacted and cemented sediment layers', 'Cooled magma', 'Extreme heat and pressure', 'Volcanic ash only']),
    ('Metamorphic rock forms from:', ['Existing rock changed by heat and pressure', 'Cooled lava only', 'Loose sediment only', 'Ocean minerals only']),
    ('The rock cycle describes:', ['The continuous transformation between rock types', 'A one-way process with no change', 'Only volcanic activity', 'Only erosion']),
    ('Weathering is the process of:', ['Breaking down rocks at the surface', 'Forming new magma', 'Compressing sediment into rock', 'Melting rock underground']),
    ('Erosion involves:', ['The transport of weathered materials', 'The formation of magma', 'The cooling of lava', 'The compression of rock layers']),
    ('Continental drift evidence includes:', ['Matching fossil and coastline patterns across continents', 'Uniform rock ages worldwide', 'A lack of matching fossils', 'Consistent continent shapes over time']),
    ('The Earth outer layer, where tectonic plates exist, is called the:', ['Lithosphere', 'Core', 'Mantle only', 'Atmosphere']),
    ('Mountain ranges commonly form at:', ['Convergent plate boundaries', 'Divergent boundaries only', 'Transform boundaries only', 'Areas without tectonic activity']),
]))

all_worksheets.append(make_ws('Science', 10, 'Climate Change and Environmental Issues', [
    ('The greenhouse effect occurs when:', ['Gases trap heat in the atmosphere', 'Heat escapes the atmosphere completely', 'The atmosphere blocks all sunlight', 'Oxygen levels increase heat']),
    ('A major greenhouse gas produced by burning fossil fuels is:', ['Carbon dioxide', 'Nitrogen', 'Oxygen', 'Helium']),
    ('Climate change refers to:', ['Long-term shifts in temperature and weather patterns', 'Daily weather changes only', 'A single storm event', 'Seasonal changes only']),
    ('Deforestation contributes to climate change by:', ['Reducing the number of trees that absorb carbon dioxide', 'Increasing oxygen absorption', 'Cooling the atmosphere', 'Reducing carbon dioxide emissions']),
    ('Renewable energy sources include:', ['Solar and wind power', 'Coal and oil only', 'Natural gas only', 'Only nuclear power']),
    ('Non-renewable energy sources include:', ['Fossil fuels such as coal, oil, and natural gas', 'Solar power', 'Wind power', 'Hydropower']),
    ('Ocean acidification is primarily caused by:', ['Increased absorption of carbon dioxide by oceans', 'Increased salt levels only', 'Decreased water temperature', 'Increased oxygen levels']),
    ('Rising global temperatures can lead to:', ['Melting ice caps and rising sea levels', 'Permanently stable sea levels', 'Cooling of the oceans', 'No change to ecosystems']),
    ('Air pollution can be reduced by:', ['Using cleaner energy sources and reducing emissions', 'Increasing fossil fuel use', 'Removing all environmental regulations', 'Ignoring emission sources']),
    ('The carbon footprint of an individual or activity refers to:', ['The total greenhouse gas emissions produced', 'The size of land used', 'The amount of water consumed only', 'The number of trees planted']),
    ('Recycling helps the environment by:', ['Reducing waste and conserving resources', 'Increasing landfill use', 'Increasing raw material extraction', 'Having no environmental benefit']),
    ('Acid rain is primarily caused by:', ['Sulfur and nitrogen oxide emissions reacting with water in the atmosphere', 'Excess oxygen in the air', 'Ocean evaporation', 'Volcanic ash alone']),
    ('Biodiversity loss is often linked to:', ['Habitat destruction and climate change', 'Increased conservation efforts', 'Stable ecosystems', 'Reduced human population only']),
    ('Sustainable practices aim to:', ['Reduce environmental impact while meeting human needs', 'Maximize resource extraction', 'Ignore future generations', 'Increase pollution levels']),
    ('International climate agreements aim to:', ['Reduce global greenhouse gas emissions collaboratively', 'Increase fossil fuel use', 'Eliminate all environmental regulation', 'Focus only on individual countries']),
]))

# ==================== SOCIAL STUDIES ====================

all_worksheets.append(make_ws('SocialStudies', 1, 'Geographic Inquiry Skills and Map Reading', [
    ('The geographic inquiry process typically begins with:', ['Formulating a question', 'Drawing conclusions', 'Presenting final results', 'Skipping analysis']),
    ('A topographic map primarily shows:', ['Elevation and landforms', 'Political boundaries only', 'Population density only', 'Climate zones only']),
    ('Map scale is used to:', ['Convert map distance into real-world distance', 'Show political boundaries', 'Indicate climate', 'Show population only']),
    ('A legend on a map:', ['Explains the symbols used', 'Shows the compass direction only', 'Lists the map title only', 'Shows elevation only']),
    ('Latitude lines run:', ['East to west, parallel to the equator', 'North to south only', 'Diagonally', 'Randomly']),
    ('Longitude lines run:', ['North to south, through the poles', 'East to west only', 'Parallel to the equator only', 'Randomly']),
    ('GIS stands for:', ['Geographic Information System', 'General Information Survey', 'Geographic Index Symbol', 'Global Inquiry System']),
    ('A choropleth map uses color shading to represent:', ['Data values across regions', 'Only political borders', 'Only physical landforms', 'Only road networks']),
    ('Primary geographic data is collected through:', ['Field observation and surveys', 'Only secondary textbooks', 'Guessing', 'Ignoring the field']),
    ('A thematic map focuses on:', ['A specific topic such as climate or population', 'All geographic features equally', 'Only borders', 'Only elevation']),
    ('The prime meridian is located at:', ['0 degrees longitude', '0 degrees latitude', '90 degrees longitude', '180 degrees latitude']),
    ('The equator is located at:', ['0 degrees latitude', '0 degrees longitude', '90 degrees latitude', '180 degrees longitude']),
    ('Remote sensing involves:', ['Collecting data about Earth from satellites or aircraft', 'Only ground level surveys', 'Interviewing residents only', 'Drawing maps by hand only']),
    ('A physical map primarily displays:', ['Landforms such as mountains and rivers', 'Political boundaries only', 'Population statistics only', 'Road networks only']),
    ('Geographic inquiry skills help students:', ['Analyze spatial patterns and relationships', 'Memorize capital cities only', 'Avoid using evidence', 'Ignore data sources']),
]))

all_worksheets.append(make_ws('SocialStudies', 2, 'Natural Resources and Industries', [
    ('A renewable resource:', ['Can be replenished over time', 'Is always limited and finite', 'Cannot be reused', 'Only refers to minerals']),
    ('A non-renewable resource:', ['Exists in a finite supply and cannot be quickly replenished', 'Regenerates quickly', 'Is always abundant', 'Refers only to water']),
    ('Canada primary industries include:', ['Forestry, mining, and fishing', 'Only technology services', 'Only banking', 'Only tourism']),
    ('Secondary industries involve:', ['Manufacturing raw materials into finished products', 'Extracting raw materials directly', 'Providing services only', 'Research only']),
    ('Tertiary industries provide:', ['Services rather than physical goods', 'Raw material extraction', 'Manufacturing only', 'Farming only']),
    ('The Canadian Shield is known for its abundance of:', ['Minerals', 'Fertile farmland', 'Oil reserves only', 'Coral reefs']),
    ('Hydroelectric power is generated using:', ['The energy of flowing water', 'Burning coal', 'Nuclear fission', 'Wind turbines']),
    ('Sustainable resource management aims to:', ['Balance economic use with environmental protection', 'Maximize extraction with no limits', 'Ignore future supply', 'Eliminate all resource use']),
    ('Boreal forest resources support industries such as:', ['Forestry and paper production', 'Only fishing', 'Only mining', 'Only tourism']),
    ('A resource-based economy relies heavily on:', ['Extracting and exporting natural resources', 'Only financial services', 'Only technology exports', 'Only imports']),
    ('Overexploitation of a resource can lead to:', ['Depletion and long-term shortages', 'Guaranteed abundance forever', 'No environmental impact', 'Increased biodiversity always']),
    ('Agriculture is classified as a:', ['Primary industry', 'Secondary industry', 'Tertiary industry', 'Quaternary industry']),
    ('Mining in Canada primarily extracts resources such as:', ['Gold, nickel, and potash', 'Only oil', 'Only fish', 'Only lumber']),
    ('Value-added processing refers to:', ['Turning raw materials into more valuable finished goods', 'Selling raw materials unprocessed', 'Reducing product value', 'Ignoring manufacturing']),
    ('Diversifying an economy away from a single resource helps:', ['Reduce economic vulnerability', 'Increase dependence on one industry', 'Guarantee resource abundance', 'Eliminate the need for trade']),
]))

all_worksheets.append(make_ws('SocialStudies', 3, 'Population Geography and Urbanization', [
    ('Population density refers to:', ['The number of people per unit of area', 'The total population of a country', 'The birth rate only', 'The death rate only']),
    ('Urbanization refers to:', ['The growth of cities as populations shift from rural areas', 'The decline of city populations', 'Rural population growth only', 'A decrease in overall population']),
    ('A push factor in migration:', ['Encourages people to leave a location', 'Attracts people to a new location', 'Has no effect on migration', 'Only applies to animals']),
    ('A pull factor in migration:', ['Attracts people to a new location', 'Forces people to leave', 'Has no effect on migration', 'Only applies within one city']),
    ('The natural increase rate of a population is calculated from:', ['Birth rate minus death rate', 'Birth rate plus death rate', 'Immigration minus emigration', 'Total population divided by area']),
    ('A population pyramid displays:', ['Age and gender distribution of a population', 'Only total population', 'Only birth rates', 'Only migration patterns']),
    ('Countries with a high proportion of young people typically have:', ['Rapid population growth potential', 'Declining populations', 'No population change', 'Only urban populations']),
    ('Urban sprawl refers to:', ['The uncontrolled expansion of urban areas into surrounding land', 'The shrinking of city boundaries', 'Rural population increase only', 'Decreased land use']),
    ('Megacities are generally defined as urban areas with populations exceeding:', ['10 million people', '10 thousand people', '1 million people exactly', '100 thousand people']),
    ('Suburbanization involves:', ['Population movement from cities to surrounding residential areas', 'Movement from suburbs into city centers only', 'Rural to rural migration only', 'International migration only']),
    ('A demographic transition model describes:', ['Changes in birth and death rates as a country develops', 'Only migration patterns', 'Only urban planning', 'Only resource use']),
    ('Emigration refers to:', ['People leaving a country', 'People entering a country', 'Movement within a city only', 'Seasonal travel only']),
    ('Immigration refers to:', ['People entering a country to settle', 'People leaving a country', 'Daily commuting only', 'Tourism only']),
    ('Population growth in developing regions is often driven by:', ['Higher birth rates', 'Higher death rates', 'Lower birth rates', 'Population decline']),
    ('Urban planning aims to:', ['Manage growth and improve quality of life in cities', 'Prevent all city growth', 'Ignore infrastructure needs', 'Eliminate green spaces entirely']),
]))

all_worksheets.append(make_ws('SocialStudies', 4, 'Climate Zones and Natural Hazards', [
    ('A tropical climate zone is generally characterized by:', ['High temperatures and significant rainfall', 'Freezing temperatures year round', 'Very low precipitation always', 'Constant snow cover']),
    ('A polar climate zone is characterized by:', ['Very cold temperatures year round', 'High humidity and heat', 'Frequent tropical storms', 'Dense rainforest vegetation']),
    ('A desert biome typically receives:', ['Very little precipitation', 'Abundant year round rainfall', 'Constant snowfall', 'Frequent flooding']),
    ('Latitude affects climate primarily by influencing:', ['The angle and intensity of sunlight received', 'Ocean salinity only', 'Soil composition only', 'Local industry']),
    ('A natural hazard is:', ['A natural event that poses a risk to people or property', 'An event with no risk at all', 'Only man made', 'Always predictable with certainty']),
    ('An earthquake risk zone is often located near:', ['Tectonic plate boundaries', 'The equator only', 'Polar regions only', 'Areas with no geological activity']),
    ('A hurricane forms over:', ['Warm ocean waters', 'Cold polar waters', 'Dry desert land', 'Mountain ranges']),
    ('Flooding risk increases in areas with:', ['Heavy rainfall and poor drainage', 'No precipitation', 'High elevation only', 'Dense forest cover only']),
    ('A drought is best described as:', ['An extended period of below-average precipitation', 'A single heavy rainstorm', 'A sudden flood', 'A temperature drop only']),
    ('Wildfire risk increases during conditions that are:', ['Hot, dry, and windy', 'Cold and wet', 'Humid and calm', 'Snowy and still']),
    ('Climate zones are largely determined by:', ['Latitude, elevation, and proximity to water', 'Population density', 'Political borders', 'Language distribution']),
    ('A temperate climate zone typically experiences:', ['Four distinct seasons', 'Constant heat', 'Constant cold', 'No precipitation']),
    ('Mitigation strategies for natural hazards aim to:', ['Reduce the impact of potential disasters', 'Increase vulnerability', 'Ignore risk assessment', 'Eliminate all natural events']),
    ('Elevation affects climate by generally causing temperatures to:', ['Decrease as elevation increases', 'Increase as elevation increases', 'Stay constant regardless of elevation', 'Have no relationship to elevation']),
    ('A tsunami is most commonly triggered by:', ['An underwater earthquake or landslide', 'Heavy rainfall', 'Wind patterns', 'Volcanic ash in the atmosphere']),
]))

all_worksheets.append(make_ws('SocialStudies', 5, 'Globalization and Trade Networks', [
    ('Globalization refers to:', ['The increasing interconnection of economies and cultures worldwide', 'The isolation of individual countries', 'A decline in international trade', 'Only local trade']),
    ('A trade route is:', ['A path used to transport goods between regions', 'A political boundary', 'A climate zone', 'A population center only']),
    ('Free trade agreements aim to:', ['Reduce barriers such as tariffs between trading countries', 'Increase tariffs significantly', 'Eliminate all trade', 'Restrict imports completely']),
    ('A tariff is:', ['A tax placed on imported goods', 'A type of currency', 'A trade route', 'A population statistic']),
    ('Outsourcing refers to:', ['Contracting work to companies in other countries', 'Producing everything domestically only', 'Ending all trade relationships', 'Increasing tariffs']),
    ('Global supply chains involve:', ['Production and distribution processes spanning multiple countries', 'Production within one factory only', 'No international cooperation', 'Only local suppliers']),
    ('Multinational corporations operate:', ['In multiple countries around the world', 'In only one country', 'Without any employees', 'Without global influence']),
    ('Economic interdependence means countries:', ['Rely on each other for goods, services, and resources', 'Are fully self sufficient', 'Avoid trade entirely', 'Never interact economically']),
    ('Containerization revolutionized trade by:', ['Making shipping goods faster and more efficient', 'Slowing down global trade', 'Eliminating the need for ports', 'Increasing shipping costs uncontrollably']),
    ('A trade deficit occurs when a country:', ['Imports more than it exports', 'Exports more than it imports', 'Has equal imports and exports', 'Stops all trade']),
    ('A trade surplus occurs when a country:', ['Exports more than it imports', 'Imports more than it exports', 'Has no trade activity', 'Only trades domestically']),
    ('Global trade networks are supported by infrastructure such as:', ['Ports, railways, and shipping routes', 'Only local roads', 'Only air travel', 'Only walking paths']),
    ('Cultural globalization can lead to:', ['The spread of ideas, media, and traditions across borders', 'Complete cultural isolation', 'The elimination of all local traditions immediately', 'No cultural exchange at all']),
    ('Fair trade practices aim to:', ['Ensure fair wages and conditions for producers', 'Maximize profit regardless of worker conditions', 'Eliminate international trade', 'Increase exploitation of labor']),
    ('A special economic zone is created to:', ['Attract investment through favorable trade and tax policies', 'Restrict all foreign investment', 'Eliminate manufacturing', 'Reduce trade activity']),
]))

all_worksheets.append(make_ws('SocialStudies', 6, 'Migration Patterns and Cultural Geography', [
    ('Internal migration refers to movement:', ['Within a country', 'Between countries', 'Only across oceans', 'Only during wartime']),
    ('International migration refers to movement:', ['Between countries', 'Within a single city', 'Within a single province', 'Only for tourism']),
    ('Refugees are people who:', ['Are forced to flee their country due to conflict or persecution', 'Voluntarily relocate for career reasons', 'Travel for tourism', 'Migrate seasonally for work only']),
    ('Economic migrants typically move in search of:', ['Better employment or living opportunities', 'Political asylum only', 'Tourism experiences', 'Educational tourism only']),
    ('Cultural geography studies:', ['How culture varies and is expressed across places', 'Only landforms', 'Only climate', 'Only economic systems']),
    ('A diaspora refers to:', ['A population dispersed from its original homeland', 'A single ethnic group in one location', 'A type of landform', 'A climate zone']),
    ('Language distribution across a region can be influenced by:', ['Historical migration and colonization patterns', 'Only current weather', 'Only soil type', 'Only elevation']),
    ('Religious geography examines:', ['The spatial distribution of religious beliefs and practices', 'Only economic activity', 'Only political systems', 'Only climate patterns']),
    ('Chain migration occurs when:', ['Migrants follow family or community members who moved earlier', 'Migration happens randomly', 'No prior connections exist', 'Migration is always government forced']),
    ('Seasonal migration is often linked to:', ['Agricultural work cycles', 'Permanent relocation only', 'Political asylum only', 'Tourism exclusively']),
    ('Assimilation refers to:', ['Adopting the customs of a new culture', 'Rejecting all new customs', 'Physical relocation only', 'Trade between countries']),
    ('Multiculturalism promotes:', ['The coexistence of diverse cultural groups within a society', 'A single dominant culture only', 'Cultural isolation', 'Elimination of minority cultures']),
    ('Ethnic enclaves are:', ['Neighborhoods where a particular ethnic group is concentrated', 'Randomly distributed populations', 'Always rural areas', 'Government administrative zones']),
    ('Urban migration is often driven by:', ['The search for employment and services in cities', 'A desire to leave cities', 'Random chance only', 'Climate change exclusively']),
    ('Cultural diffusion is the process by which:', ['Cultural traits spread from one group or region to another', 'Cultures remain completely isolated', 'Only physical goods are traded', 'Population density decreases']),
]))

all_worksheets.append(make_ws('SocialStudies', 7, 'Food Security and Agriculture', [
    ('Food security exists when people have:', ['Reliable access to sufficient, safe, and nutritious food', 'No access to food at all', 'Only luxury food options', 'Excess food waste only']),
    ('Subsistence farming primarily produces food for:', ['The farmer own family and local consumption', 'Large scale international export only', 'Industrial processing only', 'Luxury markets only']),
    ('Commercial farming is primarily oriented toward:', ['Producing crops for sale and profit', 'Personal consumption only', 'Non-food products exclusively', 'Subsistence needs only']),
    ('Arable land refers to land that is:', ['Suitable for growing crops', 'Covered entirely by forest', 'Permanently frozen', 'Underwater']),
    ('Crop rotation is used to:', ['Maintain soil fertility and reduce pest buildup', 'Deplete soil nutrients quickly', 'Increase erosion', 'Reduce crop yield intentionally']),
    ('Irrigation is the process of:', ['Artificially supplying water to land for crop growth', 'Removing water from farmland', 'Harvesting crops', 'Fertilizing soil only']),
    ('Food deserts are areas where residents have:', ['Limited access to affordable, nutritious food', 'Excess access to fresh food', 'Only luxury grocery stores', 'Unlimited agricultural land']),
    ('Genetically modified crops are often developed to:', ['Increase yield or resistance to pests and disease', 'Decrease nutritional value', 'Eliminate the need for farming', 'Increase susceptibility to disease']),
    ('Soil erosion can be reduced through:', ['Practices such as terracing and cover cropping', 'Removing all vegetation', 'Increasing water runoff', 'Ignoring land management']),
    ('Global food distribution challenges are often linked to:', ['Poverty, conflict, and infrastructure limitations', 'Excess food in every region', 'A complete absence of agriculture', 'Universal food abundance']),
    ('Monoculture farming involves:', ['Growing a single crop over a large area', 'Growing many different crops together', 'Raising only livestock', 'Avoiding all crop production']),
    ('Agribusiness refers to:', ['Large scale commercial agricultural operations', 'Small family gardens only', 'Non-agricultural industries', 'Government food aid only']),
    ('Climate change can affect agriculture by:', ['Altering growing seasons and increasing extreme weather', 'Having no impact on crop yields', 'Guaranteeing consistent harvests', 'Eliminating the need for irrigation']),
    ('Vertical farming is an approach that:', ['Grows crops in stacked layers, often indoors', 'Requires vast horizontal land only', 'Eliminates the need for water', 'Only works in polar regions']),
    ('Food sovereignty refers to:', ['The right of people to define their own food and agriculture systems', 'Complete dependence on food imports', 'Government control of all farming', 'The elimination of local food production']),
]))

all_worksheets.append(make_ws('SocialStudies', 8, 'Energy Resources and Sustainability', [
    ('Fossil fuels include:', ['Coal, oil, and natural gas', 'Solar and wind power', 'Hydropower only', 'Geothermal power only']),
    ('Solar energy is generated by:', ['Converting sunlight into electricity', 'Burning organic material', 'Nuclear fission', 'Wind turbines']),
    ('Wind energy is generated using:', ['Turbines that convert wind motion into electricity', 'Solar panels', 'Water turbines', 'Burning coal']),
    ('Geothermal energy relies on:', ['Heat from within the Earth', 'Sunlight only', 'Wind currents only', 'Ocean tides only']),
    ('Nuclear energy is produced through:', ['Nuclear fission reactions', 'Burning fossil fuels', 'Solar panels', 'Wind turbines']),
    ('A major environmental concern with fossil fuel use is:', ['Greenhouse gas emissions contributing to climate change', 'Zero emissions', 'Complete renewability', 'No impact on air quality']),
    ('Energy conservation refers to:', ['Reducing energy consumption through efficient practices', 'Increasing energy waste', 'Ignoring energy use', 'Maximizing fossil fuel extraction']),
    ('Energy security refers to:', ['A reliable and affordable supply of energy', 'Complete energy independence for every household', 'Unlimited fossil fuel reserves', 'The absence of any energy policy']),
    ('Hydropower is generated primarily using:', ['The movement of water, often through dams', 'Burning biomass', 'Solar panels', 'Wind turbines']),
    ('A transition to renewable energy can help:', ['Reduce dependence on finite fossil fuel resources', 'Increase greenhouse gas emissions', 'Guarantee unlimited fossil fuels', 'Eliminate the need for electricity']),
    ('Energy grids distribute electricity from:', ['Power generation sources to consumers', 'Consumers back to nature only', 'Only rural areas', 'Only industrial zones']),
    ('Biomass energy is produced by:', ['Burning organic materials such as wood or waste', 'Nuclear fission', 'Wind currents', 'Ocean tides']),
    ('Off-grid energy systems:', ['Operate independently of the main power grid', 'Always rely on the main grid', 'Cannot use renewable sources', 'Are illegal in most regions']),
    ('Energy poverty refers to:', ['A lack of access to reliable and affordable energy', 'An excess of energy resources', 'A situation affecting only wealthy nations', 'A surplus of renewable energy']),
    ('Government energy policy can influence:', ['The types of energy sources developed and used', 'Only local weather patterns', 'Only population growth', 'Only agricultural output']),
]))

all_worksheets.append(make_ws('SocialStudies', 9, 'Development Indicators and Global Issues', [
    ('The Human Development Index measures:', ['Life expectancy, education, and income', 'Only economic output', 'Only population size', 'Only land area']),
    ('Gross Domestic Product measures:', ['The total value of goods and services produced in a country', 'Only exports', 'Only imports', 'Only population']),
    ('Literacy rate is an indicator of:', ['The percentage of people who can read and write', 'Average income only', 'Population density only', 'Land use only']),
    ('Life expectancy refers to:', ['The average number of years a person is expected to live', 'The total population of a country', 'The birth rate only', 'The literacy rate only']),
    ('A developed country typically has:', ['High income and strong infrastructure', 'No infrastructure', 'Low education levels only', 'No industry at all']),
    ('A developing country often faces challenges related to:', ['Limited infrastructure and access to services', 'Excess industrial capacity only', 'Complete economic stability', 'Zero population growth']),
    ('Income inequality refers to:', ['The uneven distribution of income within a population', 'Equal income for all citizens', 'The total national income only', 'Population size only']),
    ('The infant mortality rate measures:', ['The number of infant deaths per set number of births', 'The number of births per year', 'The total population growth', 'The literacy rate']),
    ('Access to clean water is an important indicator of:', ['Public health and quality of life', 'Only economic output', 'Only industrial capacity', 'Only land area']),
    ('Global inequality between regions can be influenced by:', ['Historical, economic, and political factors', 'Random chance only', 'Climate alone', 'Population size alone']),
    ('Foreign aid is intended to:', ['Support development and address humanitarian needs', 'Increase poverty', 'Eliminate international cooperation', 'Reduce infrastructure']),
    ('The gender gap in education refers to:', ['Differences in educational access or outcomes between genders', 'Equal access for all genders', 'A type of currency', 'A climate indicator']),
    ('Poverty is often measured using indicators such as:', ['Income level and access to basic needs', 'Only population size', 'Only land area', 'Only climate zone']),
    ('Global health initiatives often aim to:', ['Improve access to healthcare and reduce disease', 'Increase disease spread', 'Eliminate healthcare access', 'Ignore public health data']),
    ('Sustainable development goals aim to:', ['Balance economic, social, and environmental progress', 'Focus only on economic growth', 'Ignore environmental impact', 'Eliminate international cooperation']),
]))

all_worksheets.append(make_ws('SocialStudies', 10, 'Geospatial Technology and Conservation', [
    ('GPS stands for:', ['Global Positioning System', 'General Positioning Survey', 'Geographic Placement System', 'Global Political System']),
    ('GPS technology is primarily used to:', ['Determine precise location on Earth', 'Measure temperature only', 'Predict weather only', 'Measure population only']),
    ('Remote sensing satellites are used to:', ['Collect data about the Earth surface from a distance', 'Only broadcast television', 'Only measure ocean depth', 'Only track weather balloons']),
    ('GIS is commonly used by geographers to:', ['Analyze and visualize spatial data', 'Predict stock markets', 'Translate languages', 'Compose music']),
    ('A protected area or conservation area is established to:', ['Preserve natural ecosystems and biodiversity', 'Maximize resource extraction', 'Encourage urban development', 'Eliminate wildlife habitats']),
    ('Habitat destruction is a leading cause of:', ['Biodiversity loss', 'Population growth', 'Economic development', 'Climate stability']),
    ('A national park is an example of:', ['A protected conservation area', 'An industrial zone', 'A trade route', 'A population center']),
    ('Satellite imagery can help track:', ['Deforestation and land use change over time', 'Only ocean color', 'Only cloud shapes', 'Only star positions']),
    ('Environmental monitoring using geospatial tools helps:', ['Detect changes in ecosystems and natural resources', 'Increase pollution', 'Eliminate the need for conservation', 'Ignore environmental change']),
    ('A wildlife corridor is designed to:', ['Connect habitats and allow animal movement between them', 'Block animal movement completely', 'Serve as a trade route', 'Increase habitat fragmentation']),
    ('Circular economy principles focus on:', ['Reducing waste through reuse and recycling', 'Maximizing single use products', 'Increasing landfill waste', 'Ignoring resource limits']),
    ('Conservation biology aims to:', ['Protect species and ecosystems from decline', 'Accelerate species extinction', 'Increase habitat destruction', 'Ignore biodiversity loss']),
    ('Geographic Information Systems can layer data such as:', ['Population, land use, and elevation together', 'Only text documents', 'Only images with no data', 'Only historical dates']),
    ('Drones are increasingly used in geography for:', ['Aerial surveying and environmental monitoring', 'Underwater mapping exclusively', 'Only military purposes', 'Only recreational use']),
    ('Sustainable land use planning aims to:', ['Balance development needs with environmental protection', 'Maximize urban sprawl', 'Ignore ecological impact', 'Eliminate all green spaces']),
]))

if __name__ == '__main__':
    write_worksheets(9, all_worksheets)
