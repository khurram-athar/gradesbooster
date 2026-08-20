#!/usr/bin/env python3
"""Grade 10 standalone optional-worksheet content (Project Plan item 8).

This is a NEW, separate content pipeline from data/grade10.ts (the 187-day
day-based lesson sequence) -- these worksheets are supplementary practice
material, not new lessons, and are allowed to reinforce/overlap topics
already covered across the 187 days. Grade 10 uses multiple-choice only
(mc()), matching the existing daily-quiz style.

Structure: exactly 10 worksheets per subject x 4 subjects (English, Math,
Science, History -- Grade 10 subject keys, not Language/SocialStudies) =
40 worksheets, each with exactly 15 mc() questions (60 questions per
subject, 600 total). Within each subject the 10 worksheets are organized
around 10 distinct practice themes/strands spanning the grade, roughly
progressing from foundational to more advanced, so each worksheet has a
clear, distinct focus. Titles are distinct within each subject (titles may
repeat across subjects).

No embedded ASCII double-quote or apostrophe characters anywhere in
title/q/option text -- contractions and possessives are dropped or
reworded entirely (e.g. "does not" not "doesnt", "Canadas" not "Canada's"),
matching the convention used throughout the day-based curriculum scripts
and the hard assert()s in gen_worksheets.py's mc()/worksheet() helpers.

Authoring approach (same as gen_grade5_worksheets.py): each question is
authored as a (question_text, correct_answer_text, [wrong1, wrong2,
wrong3]) tuple via qd(), always with the correct answer conceptually
"first" for ease of writing. build_mc_list() then rebalances the
correct-answer position across indices 0-3 within each worksheet (using a
per-worksheet seed) before handing questions to mc(), so there is no bias
toward any one option letter.
"""
import random
import sys
sys.path.insert(0, '.')
from gen_worksheets import mc, worksheet, write_worksheets


def qd(text, correct, wrongs):
    """One authored question: text, the correct answer string, and exactly
    3 wrong answer strings. Position is assigned later by build_mc_list()."""
    assert len(wrongs) == 3, f'expected exactly 3 wrong answers, got {len(wrongs)}: {text!r}'
    return (text, correct, wrongs)


def build_mc_list(items, seed, offset=0):
    """Turns a list of qd() tuples into a list of mc() questions, spreading
    the correct-answer index roughly evenly across 0-3 within this list.
    Since 15 questions does not divide evenly by 4 options, one index gets
    only 3 occurrences per worksheet instead of 4 -- offset rotates which
    index that is (per worksheet), so across a subjects 10 worksheets no
    single option letter is systematically shortchanged."""
    assert len(items) == 15, f'expected exactly 15 items, got {len(items)}'
    rng = random.Random(seed)
    n = len(items)
    targets = [(i + offset) % 4 for i in range(n)]
    rng.shuffle(targets)
    out = []
    for (text, correct, wrongs), target in zip(items, targets):
        opts = [None, None, None, None]
        opts[target] = correct
        remaining = list(wrongs)
        rng.shuffle(remaining)
        wi = 0
        for slot in range(4):
            if opts[slot] is None:
                opts[slot] = remaining[wi]
                wi += 1
        out.append(mc(text, opts, target))
    return out


def ws(subject, number, title, items, seed):
    offset = (number - 1) % 4
    return worksheet(subject, number, title, build_mc_list(items, seed, offset))


all_worksheets = []

# ============================================================
# ENGLISH
# ============================================================

all_worksheets.append(ws('English', 1, 'Elements of Fiction', [
    qd('The sequence of events in a story is called the ___.', 'plot', ['theme', 'setting', 'tone']),
    qd('The struggle between opposing forces in a story is the ___.', 'conflict', ['climax', 'exposition', 'resolution']),
    qd('The time and place in which a story occurs is the ___.', 'setting', ['plot', 'theme', 'motif']),
    qd('The central message or insight about life in a story is the ___.', 'theme', ['setting', 'plot', 'foreshadowing']),
    qd('A character who does not change over the course of a story is called ___.', 'a static character', ['a dynamic character', 'a round character', 'an antagonist']),
    qd('A character who undergoes significant internal change is called ___.', 'a dynamic character', ['a static character', 'a flat character', 'a foil']),
    qd('The vantage point from which a story is told is its ___.', 'point of view', ['setting', 'theme', 'plot']),
    qd('In first person narration, the narrator ___.', 'is a character in the story using I', ['knows the thoughts of every character', 'is outside the story entirely', 'never uses pronouns']),
    qd('The turning point of highest tension in a story is the ___.', 'climax', ['exposition', 'rising action', 'denouement']),
    qd('Hints planted early in a story about later events are called ___.', 'foreshadowing', ['flashback', 'irony', 'symbolism']),
    qd('A scene that interrupts the present action to show an earlier event is a ___.', 'flashback', ['foreshadowing', 'motif', 'epilogue']),
    qd('An object, person, or place that represents an abstract idea is a ___.', 'symbol', ['setting', 'motif only', 'protagonist']),
    qd('The struggle between a character and nature, society, or another character is ___ conflict.', 'external', ['internal', 'imaginary', 'passive']),
    qd('A struggle occurring within a characters own mind is ___ conflict.', 'internal', ['external', 'social', 'physical']),
    qd('The character who opposes the protagonist is the ___.', 'antagonist', ['narrator', 'foil', 'confidant']),
], seed=101))

all_worksheets.append(ws('English', 2, 'Grammar and Sentence Structure', [
    qd('A sentence with one independent clause and no dependent clauses is a ___ sentence.', 'simple', ['compound', 'complex', 'compound-complex']),
    qd('A sentence joining two independent clauses with a coordinating conjunction is a ___ sentence.', 'compound', ['simple', 'complex', 'fragment']),
    qd('A sentence with one independent clause and at least one dependent clause is a ___ sentence.', 'complex', ['simple', 'compound', 'run-on']),
    qd('A group of words that expresses a complete thought and can stand alone is called ___.', 'an independent clause', ['a dependent clause', 'a phrase only', 'a fragment']),
    qd('A group of words with a subject and verb that cannot stand alone is called ___.', 'a dependent clause', ['an independent clause', 'a run-on', 'a comma splice']),
    qd('Two independent clauses joined with only a comma and no conjunction form ___.', 'a comma splice', ['a complex sentence', 'a correct compound sentence', 'a fragment']),
    qd('An incomplete sentence missing a subject or verb is called a ___.', 'fragment', ['clause', 'compound sentence', 'phrase']),
    qd('In the sentence Sarah quickly finished her homework, the word quickly is ___.', 'an adverb', ['a noun', 'a preposition', 'a conjunction']),
    qd('A word that describes or modifies a noun is called ___.', 'an adjective', ['an adverb', 'a pronoun', 'a conjunction']),
    qd('The subject and verb in a sentence must agree in ___.', 'number', ['tense only', 'length', 'punctuation']),
    qd('Words such as and, but, and or that join clauses of equal rank are ___ conjunctions.', 'coordinating', ['subordinating', 'correlative', 'relative']),
    qd('Words such as because, although, and when that begin a dependent clause are ___ conjunctions.', 'subordinating', ['coordinating', 'correlative', 'demonstrative']),
    qd('The active voice construction The dog chased the ball places the doer of the action ___.', 'as the subject', ['as the object', 'after the verb only', 'nowhere in the sentence']),
    qd('In passive voice, the ball was chased by the dog, the subject of the sentence is ___.', 'the ball', ['the dog', 'chased', 'by']),
    qd('A word that renames or describes the subject after a linking verb is called ___.', 'a predicate adjective or noun', ['a direct object', 'an indirect object', 'a preposition']),
], seed=102))

all_worksheets.append(ws('English', 3, 'Vocabulary and Word Roots', [
    qd('The root word bene, as in benefit and benevolent, means ___.', 'good or well', ['bad', 'life', 'water']),
    qd('The prefix anti- generally means ___.', 'against', ['before', 'after', 'within']),
    qd('The root word chron, as in chronological, relates to ___.', 'time', ['color', 'writing', 'sound']),
    qd('The suffix -ology generally means ___.', 'the study of', ['able to be', 'without', 'full of']),
    qd('The prefix trans- generally means ___.', 'across or beyond', ['together', 'against', 'under']),
    qd('A word that means the same or nearly the same as another word is called a ___.', 'synonym', ['antonym', 'homophone', 'homonym']),
    qd('A word that means the opposite of another word is called a ___.', 'antonym', ['synonym', 'homograph', 'idiom']),
    qd('Two words that sound alike but have different meanings and spellings, such as their and there, are ___.', 'homophones', ['synonyms', 'antonyms', 'connotations']),
    qd('The emotional association a word carries beyond its literal meaning is its ___.', 'connotation', ['denotation', 'syntax', 'etymology']),
    qd('The exact dictionary meaning of a word is its ___.', 'denotation', ['connotation', 'inflection', 'idiom']),
    qd('An expression whose meaning cannot be understood from the literal words, such as spill the beans, is ___.', 'an idiom', ['a synonym', 'a denotation', 'a homograph']),
    qd('The root word vis or vid, as in visible and video, relates to ___.', 'seeing', ['hearing', 'speaking', 'moving']),
    qd('The prefix mal-, as in malfunction, generally means ___.', 'bad', ['good', 'again', 'within']),
    qd('The suffix -ify, as in clarify, generally means ___.', 'to make', ['full of', 'without', 'the study of']),
    qd('The root word script, as in manuscript, relates to ___.', 'writing', ['seeing', 'hearing', 'building']),
], seed=103))

all_worksheets.append(ws('English', 4, 'Reading Comprehension Strategies', [
    qd('Making a reasonable guess based on text evidence and prior knowledge is called ___.', 'inferring', ['skimming', 'summarizing', 'annotating']),
    qd('Restating the main ideas of a passage in fewer words is called ___.', 'summarizing', ['inferring', 'predicting', 'previewing']),
    qd('Reading quickly to get the general idea of a text is called ___.', 'skimming', ['close reading', 'annotating', 'paraphrasing']),
    qd('Reading carefully to locate a specific fact or detail is called ___.', 'scanning', ['skimming', 'summarizing', 'inferring']),
    qd('Writing notes or marks in the margins of a text while reading is called ___.', 'annotating', ['scanning', 'previewing', 'predicting']),
    qd('Forming an idea about what will happen next in a text is ___.', 'predicting', ['inferring', 'summarizing', 'annotating']),
    qd('Restating text in your own words while keeping the original meaning is called ___.', 'paraphrasing', ['quoting', 'skimming', 'scanning']),
    qd('A fact that can be proven true or false is a ___.', 'statement of fact', ['statement of opinion', 'thesis', 'summary']),
    qd('A personal belief or judgment that cannot be proven is a ___.', 'statement of opinion', ['statement of fact', 'citation', 'paraphrase']),
    qd('The overall purpose of a text, such as to inform, persuade, or entertain, is its ___.', 'purpose', ['tone', 'setting', 'theme']),
    qd('The authors attitude toward the subject as shown through word choice is the ___.', 'tone', ['purpose', 'plot', 'setting']),
    qd('Evidence used from the text to support an interpretation is called ___.', 'textual evidence', ['a personal anecdote', 'an unrelated fact', 'a summary only']),
    qd('Identifying the cause and effect relationships in a passage helps a reader understand ___.', 'why events happen', ['only the setting', 'only character names', 'only the title']),
    qd('Comparing and contrasting two texts involves identifying ___.', 'similarities and differences', ['only similarities', 'only differences', 'neither similarities nor differences']),
    qd('Reviewing titles, headings, and images before reading a text is called ___.', 'previewing', ['annotating', 'paraphrasing', 'scanning']),
], seed=104))

all_worksheets.append(ws('English', 5, 'Persuasive and Argumentative Writing', [
    qd('A clear statement of the writers position on an issue is called a ___.', 'thesis statement', ['summary', 'counterclaim', 'anecdote']),
    qd('An appeal to logic and reasoning in persuasive writing is called ___.', 'logos', ['pathos', 'ethos', 'kairos']),
    qd('An appeal to emotion in persuasive writing is called ___.', 'pathos', ['logos', 'ethos', 'diction']),
    qd('An appeal to the credibility of the speaker or writer is called ___.', 'ethos', ['pathos', 'logos', 'syntax']),
    qd('An opposing viewpoint that a writer addresses and refutes is a ___.', 'counterargument', ['thesis', 'conclusion', 'anecdote']),
    qd('Evidence such as statistics, expert opinions, and examples used to support a claim is called ___.', 'supporting evidence', ['a counterclaim', 'a rebuttal', 'a hook']),
    qd('The opening sentence or two designed to capture the reader attention is called the ___.', 'hook', ['thesis', 'conclusion', 'transition']),
    qd('Directly disproving an opposing argument with evidence is called a ___.', 'rebuttal', ['hook', 'summary', 'anecdote']),
    qd('An argument that unfairly attacks a persons character instead of their argument is a ___ fallacy.', 'ad hominem', ['slippery slope', 'straw man', 'bandwagon']),
    qd('A fallacy that misrepresents an opponent argument to make it easier to attack is a ___ fallacy.', 'straw man', ['ad hominem', 'false dilemma', 'circular reasoning']),
    qd('A fallacy claiming something must be true because many people believe it is the ___ fallacy.', 'bandwagon', ['straw man', 'ad hominem', 'slippery slope']),
    qd('A fallacy presenting only two options when more actually exist is a ___.', 'false dilemma', ['bandwagon fallacy', 'ad hominem attack', 'circular argument']),
    qd('Words chosen deliberately for their persuasive effect and connotation are examples of ___.', 'loaded diction', ['neutral diction', 'objective reporting', 'a direct quotation']),
    qd('A concluding paragraph in a persuasive essay should ___.', 'restate the thesis and call for action', ['introduce a brand new argument', 'contradict the thesis', 'list unrelated facts']),
    qd('Organizing an argument from least to most convincing point is called ___ order.', 'climactic', ['chronological', 'random', 'spatial']),
], seed=105))

all_worksheets.append(ws('English', 6, 'Media Literacy and Advertising Techniques', [
    qd('The intended audience for a media text is the group ___.', 'it is designed to reach and influence', ['that created the text', 'that funds the text', 'mentioned in the credits']),
    qd('A technique using a celebrity to promote a product is called ___.', 'celebrity endorsement', ['bandwagon appeal', 'plain folks appeal', 'card stacking']),
    qd('An advertising technique suggesting everyone else already owns the product is ___ appeal.', 'bandwagon', ['celebrity endorsement', 'plain folks', 'testimonial']),
    qd('An advertising technique that presents only favourable information and omits drawbacks is called ___.', 'card stacking', ['bandwagon appeal', 'glittering generalities', 'plain folks appeal']),
    qd('Vague, emotionally positive words used without real evidence, such as amazing or the best, are ___.', 'glittering generalities', ['card stacking', 'testimonials', 'statistics']),
    qd('An advertisement designed to make a product seem ordinary and relatable to average people uses ___ appeal.', 'plain folks', ['bandwagon', 'celebrity endorsement', 'card stacking']),
    qd('A statement from a satisfied customer used to promote a product is called a ___.', 'testimonial', ['glittering generality', 'card stacking technique', 'bandwagon appeal']),
    qd('The company or individual responsible for creating and distributing a media text is its ___.', 'producer', ['audience', 'genre', 'medium']),
    qd('The channel through which a media message is delivered, such as television or a website, is the ___.', 'medium', ['audience', 'producer', 'purpose']),
    qd('Analyzing who benefits from a media message and who is left out is examining its ___.', 'bias', ['format', 'genre', 'runtime']),
    qd('The specific visual and technical choices, such as camera angle and lighting, used to create meaning are called ___.', 'production techniques', ['plot devices', 'literary devices', 'grammar rules']),
    qd('A close-up camera shot in an advertisement is typically used to ___.', 'draw attention to detail or emotion', ['show a wide setting', 'hide the product', 'confuse the viewer']),
    qd('Repetition of a slogan across many advertisements is meant to increase ___.', 'brand recognition', ['production cost', 'runtime', 'font size']),
    qd('Information presented as neutral fact but that actually promotes a viewpoint is called ___.', 'propaganda', ['satire', 'parody', 'a citation']),
    qd('Evaluating whether a source is reliable involves checking its ___.', 'author, purpose, and evidence', ['color scheme only', 'file size only', 'title length only']),
], seed=106))

all_worksheets.append(ws('English', 7, 'Poetry Devices and Analysis', [
    qd('The repetition of consonant sounds at the beginning of nearby words is called ___.', 'alliteration', ['assonance', 'onomatopoeia', 'consonance']),
    qd('The repetition of vowel sounds within nearby words is called ___.', 'assonance', ['alliteration', 'rhyme scheme', 'meter']),
    qd('A word that imitates the sound it describes, such as buzz or clang, is called ___.', 'onomatopoeia', ['a simile', 'a metaphor', 'personification']),
    qd('A comparison using like or as is called a ___.', 'simile', ['metaphor', 'personification', 'hyperbole']),
    qd('A direct comparison stating one thing is another is called a ___.', 'metaphor', ['simile', 'onomatopoeia', 'alliteration']),
    qd('Giving human qualities to a nonhuman object or idea is called ___.', 'personification', ['metaphor', 'simile', 'irony']),
    qd('Extreme exaggeration used for effect is called ___.', 'hyperbole', ['understatement', 'personification', 'assonance']),
    qd('The rhythmic pattern of stressed and unstressed syllables in a line of poetry is its ___.', 'meter', ['rhyme scheme', 'stanza', 'tone']),
    qd('A group of lines forming a unit in a poem, similar to a paragraph, is called a ___.', 'stanza', ['couplet', 'refrain', 'meter']),
    qd('The pattern of end rhymes in a poem, often labelled with letters like ABAB, is the ___.', 'rhyme scheme', ['meter', 'stanza', 'free verse']),
    qd('Poetry that does not follow a regular rhyme scheme or meter is called ___.', 'free verse', ['a sonnet', 'a couplet', 'blank verse']),
    qd('A fourteen line poem with a formal rhyme scheme, often about love, is called a ___.', 'sonnet', ['haiku', 'limerick', 'ballad']),
    qd('A line or group of lines repeated throughout a poem, especially in songs, is called a ___.', 'refrain', ['stanza', 'meter', 'sonnet']),
    qd('When the meaning of a line continues onto the next line without a pause, this is called ___.', 'enjambment', ['a caesura', 'a refrain', 'a couplet']),
    qd('A pause or break in the middle of a line of poetry is called a ___.', 'caesura', ['enjambment', 'refrain', 'meter']),
], seed=107))

all_worksheets.append(ws('English', 8, 'Essay Structure and Thesis Statements', [
    qd('The paragraph that introduces the topic and states the thesis is the ___ paragraph.', 'introductory', ['body', 'concluding', 'transitional']),
    qd('A clear, arguable statement expressing the main point of an essay is the ___.', 'thesis statement', ['topic sentence', 'hook', 'summary']),
    qd('The sentence that states the main idea of a single body paragraph is the ___.', 'topic sentence', ['thesis statement', 'hook', 'conclusion']),
    qd('Sentences that connect ideas smoothly between paragraphs are called ___.', 'transitions', ['topic sentences', 'citations', 'thesis statements']),
    qd('Specific details, quotations, and examples that support a topic sentence are called ___.', 'supporting evidence', ['a hook', 'a thesis', 'a transition']),
    qd('The final paragraph that restates the thesis and leaves a lasting impression is the ___ paragraph.', 'concluding', ['introductory', 'body', 'transitional']),
    qd('An essay structured to compare and contrast two subjects is organized using a ___ pattern.', 'compare and contrast', ['cause and effect', 'chronological', 'descriptive']),
    qd('An essay explaining why something happens and what results from it uses a ___ pattern.', 'cause and effect', ['compare and contrast', 'spatial', 'narrative']),
    qd('Presenting events or steps in the order they occur is called ___ organization.', 'chronological', ['spatial', 'climactic', 'compare and contrast']),
    qd('An outline created before drafting an essay helps the writer plan the ___.', 'structure and order of ideas', ['final grade', 'font and margins', 'page count only']),
    qd('Reviewing and improving word choice, sentence variety, and clarity is called ___.', 'revising', ['outlining', 'proofreading for spelling only', 'drafting']),
    qd('Checking a final draft for spelling, punctuation, and grammar errors is called ___.', 'proofreading', ['revising ideas', 'outlining', 'brainstorming']),
    qd('A properly formatted reference list crediting sources used in an essay is called a ___.', 'works cited or bibliography', ['thesis statement', 'topic sentence', 'hook']),
    qd('Using another writers exact words without credit is called ___.', 'plagiarism', ['paraphrasing', 'summarizing', 'quoting properly']),
    qd('Restating information in your own words while crediting the source is called proper ___.', 'paraphrasing', ['plagiarism', 'quoting without citation', 'copying']),
], seed=108))

all_worksheets.append(ws('English', 9, 'Shakespeare and Dramatic Literature', [
    qd('A play intended to explore serious themes and often ends with the death of the protagonist is a ___.', 'tragedy', ['comedy', 'history play', 'farce']),
    qd('A play with humorous elements that typically ends happily is a ___.', 'comedy', ['tragedy', 'elegy', 'epic']),
    qd('A speech given by a character alone on stage, revealing inner thoughts, is called a ___.', 'soliloquy', ['aside', 'chorus', 'prologue']),
    qd('A short remark a character makes to the audience that other characters do not hear is called ___.', 'an aside', ['a soliloquy', 'a monologue', 'a stage direction']),
    qd('A flaw in a tragic hero that leads to their downfall is called ___.', 'a tragic flaw', ['a foil', 'comic relief', 'dramatic irony']),
    qd('A character whose traits contrast with and highlight another character traits is called ___.', 'a foil', ['a tragic hero', 'a chorus', 'a narrator']),
    qd('When the audience knows something a character does not, this creates ___.', 'dramatic irony', ['comic relief', 'foreshadowing only', 'a soliloquy']),
    qd('A humorous scene or character inserted into a serious play to ease tension is called ___.', 'comic relief', ['dramatic irony', 'a tragic flaw', 'exposition']),
    qd('Instructions in a play script describing actions, movement, or set details are called ___.', 'stage directions', ['dialogue', 'soliloquy', 'a prologue']),
    qd('An introductory speech that sets up the story before a play begins is called a ___.', 'prologue', ['epilogue', 'soliloquy', 'aside']),
    qd('A closing speech given after the main action of a play has ended is called an ___.', 'epilogue', ['prologue', 'aside', 'monologue']),
    qd('Iambic pentameter, a meter common in Shakespeare, consists of five pairs of ___ syllables per line.', 'unstressed and stressed', ['only stressed', 'only unstressed', 'silent']),
    qd('The exchange of spoken lines between characters in a play is called ___.', 'dialogue', ['stage direction', 'a soliloquy', 'exposition']),
    qd('The opening part of a play that introduces characters, setting, and background is the ___.', 'exposition', ['climax', 'resolution', 'epilogue']),
    qd('A long speech by one character to other characters who are present on stage is called ___.', 'a monologue', ['a soliloquy', 'an aside', 'a prologue']),
], seed=109))

all_worksheets.append(ws('English', 10, 'Research Skills and Citing Sources', [
    qd('A source written by someone who directly experienced or witnessed an event is a ___ source.', 'primary', ['secondary', 'tertiary', 'unreliable']),
    qd('A source that analyzes or interprets primary sources, such as a textbook, is a ___ source.', 'secondary', ['primary', 'tertiary', 'unverified']),
    qd('Checking a sources author, date, and publisher to judge reliability is called evaluating its ___.', 'credibility', ['font size', 'length', 'page count']),
    qd('A list at the end of a paper crediting all sources used is called a ___.', 'works cited page', ['thesis statement', 'abstract', 'index']),
    qd('Marking exact words taken from a source with quotation punctuation and a citation is called ___.', 'direct quoting', ['paraphrasing', 'summarizing', 'plagiarizing']),
    qd('A short note in the body of an essay identifying the source of information is called an ___.', 'in text citation', ['abstract', 'appendix', 'index']),
    qd('Combining information from multiple sources into a new, organized understanding is called ___.', 'synthesizing', ['plagiarizing', 'quoting only', 'skimming']),
    qd('A focused question that guides the direction of a research project is called a ___.', 'research question', ['thesis restatement', 'works cited entry', 'abstract']),
    qd('Search terms narrowed with specific words to find more relevant results are called ___.', 'keywords', ['citations', 'abstracts', 'appendices']),
    qd('A website ending in dot gov or dot edu is often considered more reliable because it is ___.', 'affiliated with a government or educational institution', ['always free to access', 'always the newest source', 'always written by students']),
    qd('Presenting someone else research or ideas as your own without credit is ___.', 'plagiarism', ['synthesis', 'citation', 'paraphrase']),
    qd('A note taking method where a researcher records source information alongside key points is called ___.', 'annotated note taking', ['skimming only', 'guessing', 'copying verbatim without notes']),
    qd('Using several different reliable sources to support one claim strengthens an arguments ___.', 'credibility', ['length', 'font', 'page margins']),
    qd('A brief summary of a longer research paper placed at the beginning is called an ___.', 'abstract', ['appendix', 'index', 'citation']),
    qd('Additional supporting material, such as raw data or charts, placed at the end of a paper is called an ___.', 'appendix', ['abstract', 'introduction', 'thesis']),
], seed=110))

# ============================================================
# MATH
# ============================================================

all_worksheets.append(ws('Math', 1, 'Solving Linear Systems', [
    qd('Solve by substitution: y = 2x + 1 and 3x + y = 11', 'x = 2, y = 5', ['x = 3, y = 7', 'x = 1, y = 3', 'x = 4, y = 9']),
    qd('Solve by elimination: 2x + y = 8 and x minus y = 1', 'x = 3, y = 2', ['x = 2, y = 4', 'x = 4, y = 0', 'x = 1, y = 6']),
    qd('A system of two linear equations with exactly one solution corresponds graphically to lines that ___.', 'intersect at one point', ['are parallel', 'are identical', 'never touch']),
    qd('A system of two linear equations with no solution corresponds graphically to lines that are ___.', 'parallel with different intercepts', ['intersecting once', 'identical', 'perpendicular']),
    qd('A system of two linear equations with infinite solutions corresponds graphically to lines that are ___.', 'identical', ['parallel and distinct', 'intersecting once', 'perpendicular']),
    qd('Solve by elimination: x + y = 10 and x minus y = 4', 'x = 7, y = 3', ['x = 6, y = 4', 'x = 5, y = 5', 'x = 8, y = 2']),
    qd('In the equation y = mx + b, the value m represents the ___.', 'slope', ['y-intercept', 'x-intercept', 'origin']),
    qd('In the equation y = mx + b, the value b represents the ___.', 'y-intercept', ['slope', 'x-intercept', 'domain']),
    qd('Solve by substitution: x = y + 2 and 2x + 3y = 19', 'x = 5, y = 3', ['x = 4, y = 2', 'x = 6, y = 4', 'x = 3, y = 1']),
    qd('A system representing cost and revenue lines intersects at a point commonly called the ___.', 'break-even point', ['origin', 'vertex', 'discriminant']),
    qd('The solution to a linear system is the ordered pair that satisfies ___.', 'both equations at once', ['only the first equation', 'only the second equation', 'neither equation']),
    qd('Solve by elimination: 3x + 2y = 16 and 3x minus y = 4', 'x = 4, y = 2', ['x = 2, y = 5', 'x = 3, y = 4', 'x = 5, y = 1']),
    qd('When solving a system, multiplying one equation by a constant before adding is done to ___.', 'eliminate one variable', ['change the solution', 'remove both variables', 'create a new system with no relation to the first']),
    qd('Two lines with the same slope but different y-intercepts will ___.', 'never intersect', ['intersect once', 'intersect infinitely', 'be the same line']),
    qd('A word problem asking to find two numbers with a given sum and difference can be solved using a ___.', 'linear system', ['single quadratic equation', 'trigonometric ratio', 'exponent law']),
], seed=201))

all_worksheets.append(ws('Math', 2, 'Analytic Geometry: Lines and Distances', [
    qd('The slope formula between points (x1, y1) and (x2, y2) is ___.', '(y2 minus y1) divided by (x2 minus x1)', ['(x2 minus x1) divided by (y2 minus y1)', '(y2 plus y1) divided by (x2 plus x1)', '(x2 times x1) divided by (y2 times y1)']),
    qd('The distance formula between two points is derived directly from the ___.', 'Pythagorean theorem', ['quadratic formula', 'slope formula', 'midpoint formula']),
    qd('The midpoint formula between (x1, y1) and (x2, y2) gives ___.', 'the average of the x-values and the average of the y-values', ['the sum of both coordinates', 'the difference of both coordinates', 'the product of both coordinates']),
    qd('Find the slope of the line through (1, 2) and (4, 11).', '3', ['9', '1/3', '4']),
    qd('Find the midpoint of the segment joining (2, 6) and (8, 2).', '(5, 4)', ['(6, 4)', '(4, 5)', '(10, 8)']),
    qd('Two lines are parallel when their slopes are ___.', 'equal', ['negative reciprocals', 'opposite in sign only', 'zero']),
    qd('Two lines are perpendicular when their slopes are ___.', 'negative reciprocals of each other', ['equal', 'both zero', 'both undefined']),
    qd('The equation of a line in slope point form is written as ___.', 'y minus y1 = m(x minus x1)', ['y = mx', 'ax + by = c only', 'x = my + b']),
    qd('Find the distance between (0, 0) and (3, 4).', '5', ['7', '6', '4']),
    qd('A vertical line has a slope that is ___.', 'undefined', ['zero', 'negative one', 'positive one']),
    qd('A horizontal line has a slope of ___.', 'zero', ['undefined', 'one', 'negative one']),
    qd('The equation of a circle centered at the origin with radius r is ___.', 'x squared plus y squared equals r squared', ['x plus y equals r', 'x squared minus y squared equals r', 'x times y equals r squared']),
    qd('To determine whether a triangle is isosceles using coordinates, a student should compare the ___ of its sides.', 'lengths', ['slopes only', 'midpoints only', 'y-intercepts only']),
    qd('To verify that a quadrilateral is a rectangle using coordinates, a student should check that adjacent sides are ___.', 'perpendicular', ['parallel to each other', 'equal in slope', 'both vertical']),
    qd('The median of a triangle connects a vertex to the ___ of the opposite side.', 'midpoint', ['endpoint', 'reflection', 'perpendicular bisector only']),
], seed=202))

all_worksheets.append(ws('Math', 3, 'Factoring Quadratic Expressions', [
    qd('Factor: x squared plus 5x plus 6', '(x plus 2)(x plus 3)', ['(x plus 1)(x plus 6)', '(x minus 2)(x minus 3)', '(x plus 6)(x minus 1)']),
    qd('Factor: x squared minus 9', '(x plus 3)(x minus 3)', ['(x minus 9)(x plus 1)', '(x plus 9)(x minus 1)', '(x minus 3) squared']),
    qd('The greatest common factor of 12x squared and 18x is ___.', '6x', ['3x', '12x', '2x squared']),
    qd('Factor by taking out the common factor: 4x squared plus 8x', '4x(x plus 2)', ['2x(2x plus 4)', '4(x squared plus 2x)', 'x(4x plus 8)']),
    qd('Factor: x squared minus 7x plus 12', '(x minus 3)(x minus 4)', ['(x plus 3)(x plus 4)', '(x minus 2)(x minus 6)', '(x plus 2)(x minus 6)']),
    qd('A trinomial in the form x squared plus bx plus c factors easily when two numbers multiply to c and add to ___.', 'b', ['c', 'zero', 'the square root of c']),
    qd('Factor: 2x squared plus 7x plus 3', '(2x plus 1)(x plus 3)', ['(2x plus 3)(x plus 1)', '(x plus 1)(x plus 3)', '(2x plus 7)(x plus 1)']),
    qd('A difference of squares expression such as a squared minus b squared always factors as ___.', '(a plus b)(a minus b)', ['(a minus b) squared', '(a plus b) squared', 'a(a minus b)']),
    qd('Factor: x squared plus 10x plus 25', '(x plus 5) squared', ['(x plus 5)(x minus 5)', '(x plus 25)(x plus 1)', '(x minus 5) squared']),
    qd('An expression that cannot be factored using integers over the reals is called ___.', 'prime or irreducible', ['a perfect square', 'a difference of squares', 'a common factor']),
    qd('Factor: 3x squared minus 12', '3(x plus 2)(x minus 2)', ['3(x minus 2) squared', '(3x plus 12)(x minus 1)', '3(x plus 4)(x minus 3)']),
    qd('Factor: x squared minus x minus 6', '(x minus 3)(x plus 2)', ['(x plus 3)(x minus 2)', '(x minus 6)(x plus 1)', '(x plus 6)(x minus 1)']),
    qd('When factoring by grouping, terms are typically split into ___ pairs before factoring each pair.', 'two', ['three', 'four', 'five']),
    qd('Factor: 4x squared minus 25', '(2x plus 5)(2x minus 5)', ['(4x plus 25)(x minus 1)', '(2x minus 5) squared', '(4x minus 5)(x plus 5)']),
    qd('Factor: x squared plus 2x plus 1', '(x plus 1) squared', ['(x minus 1) squared', '(x plus 1)(x minus 1)', '(x plus 2)(x minus 1)']),
], seed=203))

all_worksheets.append(ws('Math', 4, 'Graphing Quadratic Relations', [
    qd('The graph of a quadratic relation is called a ___.', 'parabola', ['hyperbola', 'straight line', 'circle']),
    qd('In vertex form y = a(x minus h) squared plus k, the vertex of the parabola is ___.', '(h, k)', ['(minus h, k)', '(h, minus k)', '(k, h)']),
    qd('If the value of a in vertex form is positive, the parabola opens ___.', 'upward', ['downward', 'sideways', 'in both directions']),
    qd('If the value of a in vertex form is negative, the parabola opens ___.', 'downward', ['upward', 'sideways', 'never']),
    qd('The vertical line that divides a parabola into two mirror image halves is called the ___.', 'axis of symmetry', ['directrix', 'asymptote', 'tangent line']),
    qd('The points where a parabola crosses the x-axis are called the ___.', 'x-intercepts or zeros', ['y-intercept', 'vertex', 'domain']),
    qd('The minimum or maximum point of a parabola is called the ___.', 'vertex', ['zero', 'y-intercept', 'axis']),
    qd('For y = 2(x minus 3) squared plus 4, the vertex is ___.', '(3, 4)', ['(minus 3, 4)', '(3, minus 4)', '(4, 3)']),
    qd('Increasing the value of a in y = a x squared makes the parabola ___.', 'narrower', ['wider', 'shift left', 'shift right']),
    qd('The value k in vertex form y = a(x minus h) squared plus k shifts the graph ___.', 'up or down', ['left or right', 'diagonally only', 'not at all']),
    qd('The value h in vertex form y = a(x minus h) squared plus k shifts the graph ___.', 'left or right', ['up or down', 'diagonally only', 'not at all']),
    qd('The domain of a typical quadratic relation is ___.', 'all real numbers', ['only positive numbers', 'only integers', 'restricted to the vertex']),
    qd('The range of a parabola that opens upward with vertex (2, 5) is ___.', 'y is greater than or equal to 5', ['y is less than or equal to 5', 'all real numbers', 'x is greater than or equal to 2']),
    qd('A parabola with no real x-intercepts lies entirely ___ the x-axis.', 'above or below', ['on', 'crossing', 'parallel to and touching']),
    qd('Converting standard form to vertex form is commonly done by ___.', 'completing the square', ['factoring only', 'graphing by trial and error', 'using the slope formula']),
], seed=204))

all_worksheets.append(ws('Math', 5, 'Solving Quadratic Equations', [
    qd('The quadratic formula solves equations in the form ___.', 'a x squared plus b x plus c equals 0', ['a x plus b equals 0', 'a x squared equals b', 'x squared equals a plus b']),
    qd('In the quadratic formula, the expression under the square root, b squared minus 4ac, is called the ___.', 'discriminant', ['coefficient', 'vertex', 'axis of symmetry']),
    qd('A discriminant greater than zero means the quadratic equation has ___.', 'two distinct real roots', ['one real root', 'no real roots', 'infinite roots']),
    qd('A discriminant equal to zero means the quadratic equation has ___.', 'exactly one real root', ['two distinct real roots', 'no real roots', 'infinite roots']),
    qd('A discriminant less than zero means the quadratic equation has ___.', 'no real roots', ['two real roots', 'one real root', 'three real roots']),
    qd('Solve by factoring: x squared minus 5x plus 6 equals 0', 'x = 2 or x = 3', ['x = minus 2 or x = minus 3', 'x = 1 or x = 6', 'x = 5 or x = 6']),
    qd('Solve by factoring: x squared minus 16 equals 0', 'x = 4 or x = minus 4', ['x = 8 or x = minus 8', 'x = 16 or x = minus 1', 'x = 4 only']),
    qd('Using the quadratic formula, the roots of x squared minus 3x minus 4 equals 0 are ___.', 'x = 4 or x = minus 1', ['x = 3 or x = minus 4', 'x = 1 or x = minus 4', 'x = 4 or x = 1']),
    qd('Completing the square on x squared plus 6x is done by adding ___.', '9', ['6', '3', '36']),
    qd('The zeros of a quadratic relation represent the values where the graph ___.', 'crosses the x-axis', ['crosses the y-axis', 'reaches its vertex', 'is undefined']),
    qd('A quadratic equation modelling projectile height can be solved to find the time when the object ___.', 'hits the ground', ['reaches maximum speed', 'changes color', 'stops accelerating']),
    qd('Solve: 2x squared minus 8 equals 0', 'x = 2 or x = minus 2', ['x = 4 or x = minus 4', 'x = 8 or x = minus 1', 'x = 16 or x = minus 16']),
    qd('The maximum height of a projectile modelled by a downward opening parabola occurs at the ___.', 'vertex', ['x-intercepts', 'y-intercept', 'origin']),
    qd('When a quadratic equation cannot be factored easily, the most reliable method to solve it is ___.', 'the quadratic formula', ['guessing values', 'graphing only', 'ignoring the constant term']),
    qd('Solve: x squared plus 4x plus 4 equals 0', 'x = minus 2', ['x = 2', 'x = minus 4', 'x = 4']),
], seed=205))

all_worksheets.append(ws('Math', 6, 'Right Triangle Trigonometry', [
    qd('In a right triangle, the sine ratio is defined as ___.', 'opposite divided by hypotenuse', ['adjacent divided by hypotenuse', 'opposite divided by adjacent', 'hypotenuse divided by opposite']),
    qd('In a right triangle, the cosine ratio is defined as ___.', 'adjacent divided by hypotenuse', ['opposite divided by hypotenuse', 'opposite divided by adjacent', 'hypotenuse divided by adjacent']),
    qd('In a right triangle, the tangent ratio is defined as ___.', 'opposite divided by adjacent', ['adjacent divided by opposite', 'opposite divided by hypotenuse', 'hypotenuse divided by adjacent']),
    qd('The longest side of a right triangle, opposite the right angle, is called the ___.', 'hypotenuse', ['adjacent side', 'opposite side', 'base']),
    qd('The Pythagorean theorem applies specifically to ___ triangles.', 'right', ['equilateral', 'obtuse', 'isosceles only']),
    qd('Find the hypotenuse of a right triangle with legs 6 and 8.', '10', ['12', '14', '9']),
    qd('To find a missing angle in a right triangle when two sides are known, a student should use ___.', 'an inverse trigonometric ratio', ['the sine law only', 'the cosine law only', 'the distance formula']),
    qd('The angle of elevation is measured from the horizontal ___ to the line of sight.', 'upward', ['downward', 'sideways', 'through the ground']),
    qd('The angle of depression is measured from the horizontal ___ to the line of sight.', 'downward', ['upward', 'sideways', 'vertically only']),
    qd('If sin(theta) equals 0.5, the angle theta is closest to ___.', '30 degrees', ['45 degrees', '60 degrees', '90 degrees']),
    qd('A ladder leaning against a wall forming a right triangle with the ground uses trigonometry to find ___.', 'the height reached or the angle formed', ['only the color of the wall', 'only the weight of the ladder', 'the ladder material']),
    qd('The three primary trigonometric ratios sine, cosine, and tangent apply only to ___ triangles.', 'right', ['scalene', 'obtuse', 'any triangle without exception']),
    qd('Find the missing leg of a right triangle with hypotenuse 13 and one leg 5.', '12', ['10', '8', '9']),
    qd('The mnemonic SOH CAH TOA helps students remember the ___.', 'three trigonometric ratios', ['sine law', 'cosine law', 'Pythagorean theorem only']),
    qd('If a right triangle has a 30 degree angle and hypotenuse 10, the side opposite that angle is ___.', '5', ['10', '8.7', '3']),
], seed=206))

all_worksheets.append(ws('Math', 7, 'Similar Triangles and Ratios', [
    qd('Two triangles are similar when their corresponding angles are equal and their corresponding sides are ___.', 'proportional', ['equal in length', 'perpendicular', 'parallel only']),
    qd('The criterion stating two triangles are similar if two pairs of corresponding angles are equal is called ___.', 'angle angle similarity', ['side side side congruence', 'side angle side congruence', 'hypotenuse leg congruence']),
    qd('If two triangles are similar with a scale factor of 2, their areas differ by a factor of ___.', '4', ['2', '8', '6']),
    qd('If two similar triangles have a scale factor of 3, their perimeters differ by a factor of ___.', '3', ['9', '6', '1']),
    qd('A ratio comparing corresponding sides of two similar figures is called the ___.', 'scale factor', ['area ratio', 'angle sum', 'perimeter only']),
    qd('Shadow problems that use similar triangles typically compare the height of an object to the length of its ___.', 'shadow', ['weight', 'angle of elevation only', 'color']),
    qd('In similar triangles, corresponding angles are always ___.', 'congruent', ['supplementary', 'complementary', 'proportional but not equal']),
    qd('A map scale such as 1 centimetre equals 5 kilometres is an example of a ___.', 'scale ratio', ['similarity theorem', 'trigonometric ratio', 'proportionality constant of zero']),
    qd('Two similar polygons have corresponding sides in the ratio 2 is to 5. Their areas are in the ratio ___.', '4 is to 25', ['2 is to 5', '4 is to 10', '2 is to 25']),
    qd('If triangle ABC is similar to triangle DEF, side AB corresponds to side ___.', 'DE', ['EF', 'FD', 'DF']),
    qd('The height of a tree can be found using similar triangles by comparing it to the height and shadow of a ___.', 'known object such as a person or pole', ['different tree species', 'unrelated building only', 'random guess']),
    qd('When solving for an unknown side in similar triangles, a student sets up a ___.', 'proportion', ['single equation with no ratio', 'random guess', 'quadratic formula']),
    qd('Similar triangles that share an angle and have a side that creates a smaller triangle inside a larger one form a ___ overlap.', 'nested', ['separate', 'unrelated', 'perpendicular']),
    qd('Two triangles with all three pairs of corresponding sides in the same ratio are similar by the ___ criterion.', 'side side side', ['angle angle', 'angle side angle', 'hypotenuse leg']),
    qd('Congruent triangles are a special case of similar triangles where the scale factor equals ___.', '1', ['0', '2', 'infinity']),
], seed=207))

all_worksheets.append(ws('Math', 8, 'Exponent Laws and Applications', [
    qd('The product rule for exponents states that x to the a times x to the b equals ___.', 'x to the (a plus b)', ['x to the (a times b)', 'x to the (a minus b)', 'x to the (a divided by b)']),
    qd('The quotient rule for exponents states that x to the a divided by x to the b equals ___.', 'x to the (a minus b)', ['x to the (a plus b)', 'x to the (a times b)', 'x to the (b minus a)']),
    qd('The power of a power rule states that (x to the a) to the b equals ___.', 'x to the (a times b)', ['x to the (a plus b)', 'x to the (a minus b)', 'x to the (a divided by b)']),
    qd('Any nonzero number raised to the power of zero equals ___.', '1', ['0', 'itself', 'undefined always']),
    qd('A negative exponent, such as x to the negative n, is equivalent to ___.', '1 divided by x to the n', ['x to the n', 'negative x to the n', 'zero']),
    qd('Simplify: 2 to the 3 times 2 to the 4', '2 to the 7', ['2 to the 12', '2 to the 1', '4 to the 7']),
    qd('Simplify: 5 to the 6 divided by 5 to the 2', '5 to the 4', ['5 to the 3', '5 to the 8', '5 to the 12']),
    qd('Simplify: (3 to the 2) to the 3', '3 to the 6', ['3 to the 5', '3 to the 9', '3 to the 8']),
    qd('A number written as a decimal times a power of ten between 1 and 10 is in ___.', 'scientific notation', ['exponential decay form', 'standard form only', 'radical form']),
    qd('Simplify: x to the 0', '1', ['0', 'x', 'undefined']),
    qd('An exponential growth function has the general form y equals a times b to the x, where b is ___.', 'greater than 1', ['equal to 1', 'between 0 and 1', 'negative']),
    qd('An exponential decay function has the general form y equals a times b to the x, where b is ___.', 'between 0 and 1', ['greater than 1', 'equal to 1', 'negative']),
    qd('Simplify: (2x) to the 3', '8x to the 3', ['6x to the 3', '2x to the 3', '8x']),
    qd('A fractional exponent such as x to the one half represents ___.', 'the square root of x', ['x divided by 2', 'x squared', 'twice x']),
    qd('A population growing by 5 percent each year can be modelled using an exponential function with base ___.', '1.05', ['0.05', '5', '1.5']),
], seed=208))

all_worksheets.append(ws('Math', 9, 'Circle Geometry', [
    qd('A line segment from the center of a circle to any point on the circle is called a ___.', 'radius', ['chord', 'diameter', 'tangent']),
    qd('A line segment passing through the center of a circle with both endpoints on the circle is a ___.', 'diameter', ['radius', 'chord', 'secant']),
    qd('A line segment with both endpoints on a circle that does not pass through the center is a ___.', 'chord', ['radius', 'diameter', 'tangent']),
    qd('A line that touches a circle at exactly one point is called a ___.', 'tangent', ['chord', 'secant', 'radius']),
    qd('A tangent to a circle is always ___ to the radius drawn to the point of tangency.', 'perpendicular', ['parallel', 'equal in length', 'twice the length of']),
    qd('The perpendicular from the center of a circle to a chord always ___ the chord.', 'bisects', ['doubles', 'ignores', 'extends']),
    qd('The circumference of a circle is calculated using the formula ___.', '2 pi r', ['pi r squared', 'pi d squared', 'r squared over 2']),
    qd('The area of a circle is calculated using the formula ___.', 'pi r squared', ['2 pi r', 'pi d', '2 r squared']),
    qd('An angle formed at the center of a circle by two radii is called a ___ angle.', 'central', ['inscribed', 'tangent', 'exterior']),
    qd('An angle formed by two chords with a vertex on the circle itself is called an ___ angle.', 'inscribed', ['central', 'exterior', 'tangent']),
    qd('An inscribed angle is always ___ the central angle that subtends the same arc.', 'half of', ['equal to', 'double', 'unrelated to']),
    qd('An inscribed angle that subtends a semicircle always measures ___.', '90 degrees', ['45 degrees', '180 degrees', '60 degrees']),
    qd('Two tangent segments drawn to a circle from the same external point are always ___ in length.', 'equal', ['different', 'proportional to the radius only', 'perpendicular']),
    qd('A polygon with all vertices on a circle is called a ___ polygon.', 'cyclic', ['regular', 'convex', 'tangent']),
    qd('The portion of a circle between a chord and the arc it subtends is called a ___.', 'segment', ['sector', 'radius', 'tangent line']),
], seed=209))

all_worksheets.append(ws('Math', 10, 'Applied Word Problems', [
    qd('A cell phone plan charges a flat fee plus a rate per gigabyte. This relationship is best modelled by a ___ function.', 'linear', ['quadratic', 'exponential', 'circular']),
    qd('The height of a ball thrown into the air over time is best modelled by a ___ function.', 'quadratic', ['linear', 'constant', 'circular']),
    qd('A savings account earning compound interest each year is best modelled by an ___ function.', 'exponential', ['linear', 'quadratic', 'constant']),
    qd('A rectangular garden with a fixed perimeter has an area that changes according to a ___ relationship as one side varies.', 'quadratic', ['linear', 'exponential', 'inverse']),
    qd('If a taxi charges a base fare plus a cost per kilometre, the total fare as a function of distance is ___.', 'linear', ['quadratic', 'exponential', 'undefined']),
    qd('A ladder problem where the ladder length, wall height, and ground distance form a right triangle is solved using ___.', 'the Pythagorean theorem or trigonometry', ['the quadratic formula only', 'exponent laws', 'circle geometry']),
    qd('Break-even analysis in business finds the point where cost and revenue functions ___.', 'are equal', ['are both zero', 'are both maximum', 'never meet']),
    qd('A problem asking for the maximum area enclosed by a fixed length of fencing is solved by finding the ___ of a quadratic function.', 'vertex', ['x-intercepts', 'y-intercept', 'slope']),
    qd('A population that doubles every fixed number of years is an example of ___ growth.', 'exponential', ['linear', 'quadratic', 'zero']),
    qd('Finding the time it takes an object dropped from a height to hit the ground involves solving a ___ equation.', 'quadratic', ['linear', 'exponential', 'trigonometric only']),
    qd('A shadow length problem involving the sun angle and a building height is typically solved with ___.', 'trigonometric ratios', ['the quadratic formula', 'exponent laws', 'circle theorems']),
    qd('Two moving vehicles starting at different points and speeds that eventually meet can be modelled with a ___.', 'linear system', ['single quadratic equation', 'circle equation', 'exponent rule']),
    qd('A rectangular box design problem that minimizes surface area for a fixed volume typically requires ___.', 'setting up and analyzing an equation for surface area', ['ignoring the volume constraint', 'using only linear equations', 'measuring only one dimension']),
    qd('Interest earned yearly without compounding, based only on the original principal, is called ___ interest.', 'simple', ['compound', 'exponential', 'negative']),
    qd('A scale drawing problem uses the concept of ___ to find real world dimensions.', 'similar figures and ratios', ['circle theorems', 'quadratic roots', 'exponent laws']),
], seed=210))

# ============================================================
# SCIENCE
# ============================================================

all_worksheets.append(ws('Science', 1, 'Atomic Theory and the Periodic Table', [
    qd('Rutherford gold foil experiment led to the discovery of the ___.', 'small, dense, positively charged nucleus', ['electron cloud only', 'neutron', 'periodic law']),
    qd('In the Bohr model, electrons occupy specific ___ around the nucleus.', 'energy levels or shells', ['random positions', 'the nucleus itself', 'a solid sphere']),
    qd('Atomic number refers to the number of ___ in an atom.', 'protons', ['neutrons', 'protons plus neutrons', 'electrons only when charged']),
    qd('Mass number refers to the number of ___ in an atom.', 'protons plus neutrons', ['protons only', 'electrons only', 'neutrons only']),
    qd('Elements in the same column, or group, of the periodic table share similar ___.', 'chemical properties', ['atomic masses', 'number of neutrons', 'colors']),
    qd('Elements in the same row, or period, of the periodic table have the same number of ___.', 'electron shells', ['protons', 'valence electrons', 'neutrons']),
    qd('Atoms of the same element with different numbers of neutrons are called ___.', 'isotopes', ['ions', 'compounds', 'molecules']),
    qd('An atom that has gained or lost electrons and carries a charge is called an ___.', 'ion', ['isotope', 'element', 'compound']),
    qd('Metals are generally found on the ___ side of the periodic table.', 'left', ['right', 'top only', 'bottom only']),
    qd('Nonmetals are generally found on the ___ side of the periodic table.', 'right', ['left', 'top only', 'center only']),
    qd('The number of electrons in the outermost shell of an atom are called ___ electrons.', 'valence', ['core', 'inner', 'nuclear']),
    qd('Thomson plum pudding model proposed that atoms were made of electrons embedded in a ___.', 'positively charged mass', ['dense nucleus', 'vacuum', 'negative cloud only']),
    qd('The modern periodic table arranges elements primarily by increasing ___.', 'atomic number', ['atomic mass only', 'color', 'melting point']),
    qd('Elements called metalloids have properties that are ___.', 'intermediate between metals and nonmetals', ['identical to metals', 'identical to nonmetals', 'purely gaseous']),
    qd('Dalton atomic theory proposed that all matter is composed of tiny, indivisible particles called ___.', 'atoms', ['molecules only', 'ions', 'isotopes only']),
], seed=301))

all_worksheets.append(ws('Science', 2, 'Chemical Bonding and Reactions', [
    qd('A bond formed by the transfer of electrons between atoms is called an ___ bond.', 'ionic', ['covalent', 'metallic', 'hydrogen']),
    qd('A bond formed by the sharing of electrons between atoms is called a ___ bond.', 'covalent', ['ionic', 'metallic', 'nuclear']),
    qd('Ionic compounds typically form between a ___ and a nonmetal.', 'metal', ['another metal', 'noble gas', 'metalloid only']),
    qd('In a chemical equation, the substances on the left side before reacting are called the ___.', 'reactants', ['products', 'catalysts', 'solutes']),
    qd('In a chemical equation, the substances formed after the reaction are called the ___.', 'products', ['reactants', 'catalysts', 'solvents']),
    qd('The law of conservation of mass states that mass in a chemical reaction is ___.', 'neither created nor destroyed', ['always increasing', 'always decreasing', 'irrelevant']),
    qd('Balancing a chemical equation involves adjusting ___ so atoms are equal on both sides.', 'coefficients', ['subscripts', 'element symbols', 'the reaction type entirely']),
    qd('A reaction where a single compound breaks down into two or more simpler substances is a ___ reaction.', 'decomposition', ['synthesis', 'single displacement', 'combustion']),
    qd('A reaction where two or more substances combine to form one product is a ___ reaction.', 'synthesis', ['decomposition', 'double displacement', 'combustion']),
    qd('A reaction where a fuel combines with oxygen and releases energy is a ___ reaction.', 'combustion', ['synthesis', 'decomposition', 'single displacement']),
    qd('A reaction where one element replaces another in a compound is a ___ reaction.', 'single displacement', ['double displacement', 'synthesis', 'combustion']),
    qd('A reaction where the positive and negative ions of two compounds switch partners is a ___ reaction.', 'double displacement', ['single displacement', 'decomposition', 'synthesis']),
    qd('A substance that speeds up a chemical reaction without being consumed is called a ___.', 'catalyst', ['reactant', 'product', 'solvent']),
    qd('A solution with a pH below 7 is considered ___.', 'acidic', ['basic', 'neutral', 'saturated']),
    qd('A solution with a pH above 7 is considered ___.', 'basic', ['acidic', 'neutral', 'unsaturated']),
], seed=302))

all_worksheets.append(ws('Science', 3, 'Cell Division and Reproduction', [
    qd('The process by which a single cell divides into two identical daughter cells is called ___.', 'mitosis', ['meiosis', 'fertilization', 'osmosis']),
    qd('The process that produces sex cells with half the normal chromosome number is called ___.', 'meiosis', ['mitosis', 'cytokinesis', 'diffusion']),
    qd('Mitosis is used by the body primarily for ___.', 'growth and repair', ['producing sperm and egg cells only', 'digesting food', 'transporting oxygen']),
    qd('Meiosis results in ___ daughter cells from one original cell.', 'four genetically different', ['two identical', 'one', 'eight identical']),
    qd('The division of the cytoplasm at the end of cell division is called ___.', 'cytokinesis', ['mitosis', 'interphase', 'meiosis']),
    qd('The phase of the cell cycle where a cell grows and copies its DNA before dividing is called ___.', 'interphase', ['prophase', 'metaphase', 'anaphase']),
    qd('During which stage of mitosis do chromosomes line up along the center of the cell.', 'metaphase', ['prophase', 'anaphase', 'telophase']),
    qd('During which stage of mitosis do sister chromatids separate and move to opposite poles.', 'anaphase', ['metaphase', 'prophase', 'telophase']),
    qd('Sexual reproduction increases genetic variation because offspring receive DNA from ___.', 'two parents', ['one parent only', 'no parents', 'identical clones']),
    qd('Asexual reproduction produces offspring that are ___ to the parent.', 'genetically identical', ['completely different', 'half identical', 'unrelated']),
    qd('Fertilization occurs when a sperm cell and an egg cell combine to form a ___.', 'zygote', ['gamete', 'somatic cell', 'stem cell']),
    qd('Cells that are not sex cells, making up most of the body, are called ___ cells.', 'somatic', ['gamete', 'haploid only', 'zygote']),
    qd('A cell with a full set of paired chromosomes is described as ___.', 'diploid', ['haploid', 'triploid', 'aploid']),
    qd('A cell with only half the normal number of chromosomes, such as a sperm or egg cell, is described as ___.', 'haploid', ['diploid', 'triploid', 'somatic']),
    qd('Uncontrolled cell division that can lead to tumours is associated with ___.', 'cancer', ['normal aging', 'meiosis only', 'fertilization']),
], seed=303))

all_worksheets.append(ws('Science', 4, 'Genetics and Heredity', [
    qd('A segment of DNA that codes for a specific trait is called a ___.', 'gene', ['chromosome', 'allele pair', 'genome']),
    qd('Different versions of the same gene are called ___.', 'alleles', ['genotypes', 'phenotypes', 'chromosomes']),
    qd('The genetic makeup of an organism, in terms of its alleles, is its ___.', 'genotype', ['phenotype', 'pedigree', 'karyotype']),
    qd('The observable physical traits of an organism are its ___.', 'phenotype', ['genotype', 'genome', 'allele']),
    qd('An allele that is expressed even when only one copy is present is called ___.', 'dominant', ['recessive', 'codominant', 'incomplete']),
    qd('An allele that is only expressed when two copies are present is called ___.', 'recessive', ['dominant', 'codominant', 'sex linked always']),
    qd('An organism with two identical alleles for a trait is described as ___ for that trait.', 'homozygous', ['heterozygous', 'hybrid', 'mutant']),
    qd('An organism with two different alleles for a trait is described as ___ for that trait.', 'heterozygous', ['homozygous', 'pure breeding', 'diploid only']),
    qd('A Punnett square is used to predict the ___ of offspring from a genetic cross.', 'probable genotypes and phenotypes', ['exact height', 'lifespan', 'diet']),
    qd('A cross between two heterozygous parents for a single trait, such as Aa times Aa, typically produces offspring in a ratio of ___.', '3 dominant to 1 recessive', ['1 to 1', 'all dominant', 'all recessive']),
    qd('A diagram showing the inheritance of a trait across generations of a family is called a ___.', 'pedigree', ['karyotype', 'genome map', 'Punnett square only']),
    qd('A change in the DNA sequence of an organism is called a ___.', 'mutation', ['allele', 'genotype', 'phenotype']),
    qd('Traits controlled by genes located on the X or Y chromosome are called ___ traits.', 'sex linked', ['dominant only', 'recessive only', 'codominant only']),
    qd('When both alleles are expressed equally and blended in the phenotype, this is called ___.', 'incomplete dominance', ['codominance', 'simple dominance', 'mutation']),
    qd('When both alleles are fully and separately expressed in the phenotype, this is called ___.', 'codominance', ['incomplete dominance', 'simple dominance', 'recessive expression']),
], seed=304))

all_worksheets.append(ws('Science', 5, 'Light and Optics', [
    qd('The bending of light as it passes from one medium to another is called ___.', 'refraction', ['reflection', 'diffraction', 'absorption']),
    qd('The bouncing back of light off a surface is called ___.', 'reflection', ['refraction', 'diffraction', 'transmission']),
    qd('The law of reflection states that the angle of incidence equals the ___.', 'angle of reflection', ['angle of refraction', 'critical angle', 'focal length']),
    qd('A lens that curves outward and causes light rays to converge is called a ___ lens.', 'convex', ['concave', 'flat', 'diverging']),
    qd('A lens that curves inward and causes light rays to spread apart is called a ___ lens.', 'concave', ['convex', 'flat', 'converging']),
    qd('The point where parallel light rays meet after passing through a convex lens is called the ___.', 'focal point', ['vertex', 'center of curvature', 'normal line']),
    qd('An image that can be projected onto a screen because light rays actually meet there is called a ___ image.', 'real', ['virtual', 'inverted only', 'magnified only']),
    qd('An image that cannot be projected onto a screen because light rays only appear to meet is called a ___ image.', 'virtual', ['real', 'inverted always', 'reduced always']),
    qd('The separation of white light into its component colors is called ___.', 'dispersion', ['reflection', 'absorption', 'polarization']),
    qd('The visible spectrum of light ranges in color from ___.', 'red to violet', ['black to white', 'blue to yellow only', 'green to orange only']),
    qd('An imaginary line perpendicular to a surface at the point of contact, used in optics diagrams, is called the ___.', 'normal', ['focal line', 'axis of symmetry', 'horizon line']),
    qd('The human eye focuses light onto the ___ at the back of the eye.', 'retina', ['cornea', 'pupil', 'lens only']),
    qd('A concave mirror used in a flashlight or headlight focuses light to make it more ___.', 'concentrated in one direction', ['scattered randomly', 'invisible', 'colored only']),
    qd('Total internal reflection occurs when light traveling in a denser medium hits a boundary at an angle greater than the ___.', 'critical angle', ['normal line', 'focal point', 'angle of incidence only']),
    qd('Optical fibres transmit light over long distances using repeated ___.', 'total internal reflection', ['refraction only', 'dispersion', 'absorption']),
], seed=305))

all_worksheets.append(ws('Science', 6, 'Electricity and Circuits', [
    qd('Electric current is measured in units called ___.', 'amperes', ['volts', 'ohms', 'watts']),
    qd('Voltage, or electric potential difference, is measured in units called ___.', 'volts', ['amperes', 'ohms', 'joules']),
    qd('Resistance in a circuit is measured in units called ___.', 'ohms', ['volts', 'amperes', 'watts']),
    qd('Ohm law states that voltage equals current multiplied by ___.', 'resistance', ['power', 'time', 'charge']),
    qd('In a series circuit, if one bulb burns out, the rest of the circuit ___.', 'stops working', ['continues working normally', 'gets brighter', 'is unaffected']),
    qd('In a parallel circuit, if one branch fails, the other branches ___.', 'continue to operate', ['also stop working', 'become short circuited', 'reverse current direction']),
    qd('A material that allows electric current to flow easily is called a ___.', 'conductor', ['insulator', 'resistor only', 'capacitor']),
    qd('A material that resists the flow of electric current is called an ___.', 'insulator', ['conductor', 'battery', 'switch']),
    qd('The rate at which electrical energy is transferred or used is called ___.', 'power', ['current', 'voltage', 'resistance']),
    qd('Electrical power is calculated using the formula ___.', 'voltage times current', ['voltage divided by current', 'current divided by resistance', 'resistance times time']),
    qd('A device that stores and provides electrical energy through a chemical reaction is a ___.', 'battery', ['resistor', 'switch', 'conductor']),
    qd('In a circuit diagram, a zigzag line symbol typically represents a ___.', 'resistor', ['battery', 'switch', 'wire only']),
    qd('Static electricity results from an imbalance of ___ on an object surface.', 'electric charge', ['magnetic force', 'current flow', 'resistance']),
    qd('A short circuit occurs when current takes an unintended path with very ___ resistance.', 'low', ['high', 'infinite', 'variable only']),
    qd('Total resistance in a series circuit is found by ___ the individual resistances.', 'adding', ['multiplying', 'averaging', 'subtracting']),
], seed=306))

all_worksheets.append(ws('Science', 7, 'Climate Change and the Atmosphere', [
    qd('Gases in the atmosphere that trap heat and warm the planet are called ___ gases.', 'greenhouse', ['inert', 'noble', 'ozone depleting only']),
    qd('The primary greenhouse gas released by burning fossil fuels is ___.', 'carbon dioxide', ['oxygen', 'nitrogen', 'hydrogen']),
    qd('The overall long term rise in global temperatures linked to human activity is called ___.', 'global warming', ['weather variability', 'the water cycle', 'ozone depletion only']),
    qd('The layer of the atmosphere that protects Earth from harmful ultraviolet radiation is the ___ layer.', 'ozone', ['troposphere', 'greenhouse', 'ionosphere']),
    qd('Deforestation contributes to climate change primarily by reducing the number of trees that absorb ___.', 'carbon dioxide', ['oxygen', 'nitrogen', 'methane only']),
    qd('The process by which the sun energy warms the Earth and some heat is trapped by gases is called the ___ effect.', 'greenhouse', ['albedo', 'ozone', 'photosynthesis']),
    qd('Rising sea levels due to climate change are caused mainly by melting ice and ___ of ocean water.', 'thermal expansion', ['evaporation only', 'freezing', 'condensation only']),
    qd('A renewable energy source that does not produce greenhouse gases during operation is ___.', 'solar power', ['coal', 'natural gas', 'oil']),
    qd('The measurement of long term patterns of temperature and precipitation in a region is called ___.', 'climate', ['weather', 'humidity only', 'pressure only']),
    qd('Short term atmospheric conditions such as todays temperature and rainfall describe the ___.', 'weather', ['climate', 'season only', 'biome']),
    qd('Human activities that release large amounts of carbon dioxide are referred to as ___ emissions.', 'carbon', ['oxygen', 'nitrogen', 'water vapor only']),
    qd('An individual or country carbon footprint measures the total amount of ___ produced by their activities.', 'greenhouse gases', ['solid waste only', 'fresh water used', 'electricity generated']),
    qd('International efforts such as emissions reduction targets aim to limit global ___.', 'temperature increase', ['population growth', 'industrial output entirely', 'ocean depth']),
    qd('Extreme weather events becoming more frequent, such as heat waves and storms, are linked to ___.', 'climate change', ['normal seasonal variation only', 'ozone layer thickness', 'lunar cycles']),
    qd('Reducing energy consumption and switching to renewable sources are examples of climate change ___ strategies.', 'mitigation', ['acceleration', 'ignoring', 'reversal by nature alone']),
], seed=307))

all_worksheets.append(ws('Science', 8, 'Astronomy and the Solar System', [
    qd('The center of our solar system around which all planets orbit is the ___.', 'sun', ['moon', 'Earth', 'nearest star cluster']),
    qd('The force that keeps planets in orbit around the sun is ___.', 'gravity', ['magnetism', 'friction', 'solar wind']),
    qd('A celestial body that orbits a planet, such as the moon orbiting Earth, is called a ___.', 'natural satellite', ['comet', 'asteroid', 'meteor']),
    qd('A small rocky body that orbits the sun, mostly found in the belt between Mars and Jupiter, is called an ___.', 'asteroid', ['comet', 'meteor', 'natural satellite']),
    qd('An icy body that develops a glowing tail as it approaches the sun is called a ___.', 'comet', ['asteroid', 'meteor', 'planet']),
    qd('A meteor that survives its trip through the atmosphere and lands on Earth is called a ___.', 'meteorite', ['comet', 'asteroid', 'meteoroid while in space']),
    qd('The four inner, rocky planets of our solar system are Mercury, Venus, Earth, and ___.', 'Mars', ['Jupiter', 'Saturn', 'Neptune']),
    qd('The large outer planets made mostly of gas are called the ___ planets.', 'gas giant', ['terrestrial', 'dwarf', 'rocky']),
    qd('Earth axial tilt is the main reason Earth experiences ___.', 'seasons', ['day and night', 'tides only', 'earthquakes']),
    qd('The rotation of Earth on its axis causes the cycle of ___.', 'day and night', ['seasons only', 'tides', 'eclipses']),
    qd('The moon phases are caused by changing ___ of the moon as seen from Earth.', 'illuminated portions', ['distance from Earth only', 'color', 'size']),
    qd('A solar eclipse occurs when the moon passes between the sun and ___.', 'Earth', ['another planet', 'a comet', 'an asteroid belt']),
    qd('A star life cycle typically begins in a large cloud of gas and dust called a ___.', 'nebula', ['supernova', 'black hole', 'white dwarf']),
    qd('An extremely dense object formed from the collapse of a massive star, from which not even light escapes, is a ___.', 'black hole', ['nebula', 'red giant', 'asteroid']),
    qd('The Milky Way, which contains our solar system, is an example of a ___.', 'galaxy', ['nebula', 'solar system only', 'comet cluster']),
], seed=308))

all_worksheets.append(ws('Science', 9, 'Chemical Quantities and Stoichiometry', [
    qd('The amount of substance containing 6.02 times 10 to the 23 particles is called a ___.', 'mole', ['gram', 'liter', 'atom']),
    qd('The number 6.02 times 10 to the 23 is known as ___ number.', 'Avogadro', ['Dalton', 'Bohr', 'Rutherford']),
    qd('The mass of one mole of a substance, expressed in grams, is called its ___.', 'molar mass', ['atomic number', 'density', 'volume']),
    qd('Molar mass is calculated by summing the atomic masses of all atoms in a ___.', 'chemical formula', ['reaction only', 'solution volume', 'periodic table row']),
    qd('In a balanced chemical equation, the coefficients represent the ratio of ___ of each substance.', 'moles', ['grams only', 'liters only', 'individual atoms only, never moles']),
    qd('Stoichiometry uses balanced equations to calculate the amounts of ___ in a chemical reaction.', 'reactants and products', ['only reactants', 'only products', 'only catalysts']),
    qd('The reactant that is completely used up first in a reaction, limiting the amount of product formed, is called the ___ reactant.', 'limiting', ['excess', 'spectator', 'catalytic']),
    qd('A reactant that remains after a reaction is complete because there was more than needed is the ___ reactant.', 'excess', ['limiting', 'spectator', 'catalytic']),
    qd('Concentration of a solution is often expressed in units of moles per liter, called ___.', 'molarity', ['molality', 'density', 'volume percent']),
    qd('To convert grams of a substance to moles, a student divides by the substance ___.', 'molar mass', ['density', 'volume', 'atomic number']),
    qd('At standard temperature and pressure, one mole of any gas occupies approximately ___.', '22.4 litres', ['1 litre', '100 litres', '6.02 litres']),
    qd('Percent yield compares the actual yield of a reaction to the ___ yield.', 'theoretical', ['limiting', 'excess', 'molar']),
    qd('A reaction producing less product than predicted may be due to incomplete reactions or ___.', 'loss of product during the process', ['too much catalyst only', 'excess oxygen always', 'perfect conditions']),
    qd('Dimensional analysis in stoichiometry problems relies on converting between units using ___.', 'conversion factors from the balanced equation', ['random estimation', 'guessing ratios', 'ignoring units entirely']),
    qd('The molar mass of water, H2O, is approximately ___ grams per mole.', '18', ['16', '20', '2']),
], seed=309))

all_worksheets.append(ws('Science', 10, 'Environmental Science and Sustainability', [
    qd('A resource that can be replenished naturally over a relatively short time is called ___.', 'renewable', ['nonrenewable', 'finite', 'depleted']),
    qd('A resource that takes millions of years to form and is used faster than it forms is called ___.', 'nonrenewable', ['renewable', 'sustainable', 'inexhaustible']),
    qd('Practices that meet present needs without compromising the ability of future generations to meet their own needs are called ___.', 'sustainable', ['unsustainable', 'nonrenewable', 'linear only']),
    qd('The variety of living organisms in an ecosystem is called ___.', 'biodiversity', ['population density', 'carrying capacity', 'trophic level']),
    qd('The maximum population size an environment can support long term is called its ___.', 'carrying capacity', ['biodiversity index', 'trophic level', 'ecological footprint']),
    qd('The total impact of human demand on Earth resources is called an ecological ___.', 'footprint', ['niche', 'succession', 'biome']),
    qd('Reducing waste by reusing materials before recycling them is part of the waste hierarchy known as reduce, reuse, and ___.', 'recycle', ['discard', 'incinerate', 'landfill']),
    qd('The gradual process by which ecosystems change and develop over time is called ecological ___.', 'succession', ['footprint', 'niche', 'carrying capacity']),
    qd('The specific role and position a species occupies in its environment is called its ecological ___.', 'niche', ['succession', 'footprint', 'biome']),
    qd('A large scale terrestrial community, such as a desert or forest, defined by climate and vegetation, is called a ___.', 'biome', ['niche', 'population', 'watershed']),
    qd('An invasive species is a non native organism that ___ a new ecosystem it enters.', 'disrupts', ['always benefits', 'has no effect on', 'immediately goes extinct in']),
    qd('The removal of large areas of forest, often for agriculture, is called ___.', 'deforestation', ['afforestation', 'conservation', 'reforestation only']),
    qd('Programs that plant new trees in areas that previously had forest are examples of ___.', 'reforestation', ['deforestation', 'urbanization', 'desertification']),
    qd('Water, air, and soil contamination caused by harmful substances is broadly called ___.', 'pollution', ['conservation', 'sustainability', 'biodiversity']),
    qd('Protecting natural resources through careful management and limited use is called ___.', 'conservation', ['pollution', 'deforestation', 'overconsumption']),
], seed=310))

# ============================================================
# HISTORY
# ============================================================

all_worksheets.append(ws('History', 1, 'Canada and the First World War', [
    qd('Canada entered World War I in 1914 automatically because ___.', 'Britain declared war and Canada was part of the British Empire', ['Canada was directly invaded', 'Canada declared war independently first', 'the United States asked Canada to join'])
    ,
    qd('The battle where Canadian troops fought together as a unified corps for the first time, in April 1917, was ___.', 'Vimy Ridge', ['Ypres', 'the Somme', 'Passchendaele']),
    qd('Canadian troops were among the first to face chemical weapons at the Battle of ___.', 'Ypres', ['Vimy Ridge', 'the Somme', 'Passchendaele']),
    qd('The system requiring men to enlist for military service, introduced in Canada in 1917, was called ___.', 'conscription', ['appeasement', 'internment', 'suffrage']),
    qd('Conscription during World War I created deep tension between English and French Canada mainly because ___.', 'many in Quebec opposed mandatory service', ['Quebec wanted to fight sooner', 'Ontario opposed the war entirely', 'the west supported conscription least of all regions'])
    ,
    qd('Women contributed to the war effort on the home front by ___.', 'working in factories and farms', ['serving exclusively as combat soldiers', 'remaining entirely uninvolved', 'only working overseas as nurses'])
    ,
    qd('Many Canadian women gained the right to vote federally as a direct result of contributions during ___.', 'World War I', ['the Great Depression', 'World War II', 'the Cold War']),
    qd('The trench warfare style of World War I was characterized by ___.', 'long stalemates and heavy casualties for small gains', ['fast moving mobile battles', 'entirely naval combat', 'no use of artillery'])
    ,
    qd('The War Measures Act gave the Canadian government the power to ___.', 'restrict civil liberties during wartime', ['end the war immediately', 'grant full independence to Canada', 'abolish the military'])
    ,
    qd('Recent immigrants from enemy nations, such as Ukrainians and Germans, faced ___ during World War I.', 'internment and restrictions', ['full citizenship rights', 'immediate deportation only', 'no impact at all'])
    ,
    qd('The Halifax Explosion of 1917 was caused by ___.', 'a collision between two ships, one carrying munitions', ['a German naval attack', 'an accidental bombing raid', 'a mining disaster']),
    qd('Canada participation in the Paris Peace Conference and signing of the Treaty of Versailles as a separate signatory reflected growing Canadian ___.', 'autonomy', ['dependence on Britain', 'isolation from world affairs', 'military weakness'])
    ,
    qd('The main cause of the alliance system leading into World War I was ___.', 'competing military and political alliances across Europe', ['a single trade dispute', 'a natural disaster', 'a religious conflict only'])
    ,
    qd('The assassination that triggered the start of World War I involved ___.', 'Archduke Franz Ferdinand of Austria-Hungary', ['the King of Britain', 'the President of France', 'the Tsar of Russia'])
    ,
    qd('Canadian soldiers were part of the larger force known as the ___.', 'British Expeditionary Force and Allied armies', ['Central Powers', 'Ottoman army', 'neutral peacekeeping force']),
], seed=401))

all_worksheets.append(ws('History', 2, 'The Interwar Years and the Great Depression', [
    qd('The stock market crash that triggered the Great Depression occurred in ___.', 'October 1929', ['1918', '1939', '1945']),
    qd('During the Great Depression, unemployed men who traveled the country seeking work were often called ___.', 'riding the rails', ['flappers', 'bootleggers', 'suffragists']),
    qd('Government relief camps set up during the Great Depression were intended to ___.', 'provide work and reduce unrest among unemployed men', ['immediately end the depression', 'increase immigration', 'fund overseas wars'])
    ,
    qd('The On to Ottawa Trek was a protest march by unemployed workers demanding ___.', 'better wages and conditions in relief camps', ['an end to World War I', 'immediate independence from Britain', 'new provincial borders'])
    ,
    qd('The economic policy of protecting domestic industries through high tariffs during the Depression is known as ___.', 'protectionism', ['free trade', 'socialism', 'appeasement'])
    ,
    qd('The Regina Riot of 1935 arose from tensions between police and participants of the ___.', 'On to Ottawa Trek', ['Winnipeg General Strike', 'conscription crisis', 'suffrage movement'])
    ,
    qd('The Winnipeg General Strike of 1919 was primarily a protest for ___.', 'better wages and working conditions', ['an end to conscription', 'voting rights for women', 'independence from Britain'])
    ,
    qd('The economic policy known as the New Deal, introduced in the United States, aimed to ___.', 'create jobs and stimulate the economy through government programs', ['increase military conscription', 'reduce trade with all nations', 'abolish banks entirely'])
    ,
    qd('Prairie farmers were especially hard hit during the Great Depression due to a combination of low crop prices and ___.', 'severe drought conditions known as the Dust Bowl', ['overproduction of oil', 'excessive rainfall', 'new technology shortages'])
    ,
    qd('The Roaring Twenties, the decade before the Depression, was known for economic growth and ___.', 'new consumer culture and social change', ['widespread famine', 'global war', 'strict rationing'])
    ,
    qd('Prohibition in the 1920s refers to the banning of the ___.', 'sale and consumption of alcohol', ['sale of automobiles', 'right to vote', 'right to own land'])
    ,
    qd('R B Bennett, prime minister during much of the Depression, initially believed the crisis could be solved by ___.', 'raising tariffs to protect Canadian industry', ['immediate massive government spending', 'joining a new international alliance', 'abolishing Parliament'])
    ,
    qd('New political parties, such as the Cooperative Commonwealth Federation, emerged during the Depression to advocate for ___.', 'social welfare programs and workers rights', ['a return to monarchy', 'increased military spending only', 'stricter immigration bans only'])
    ,
    qd('Soup kitchens and bread lines during the Great Depression were established to ___.', 'provide food for the unemployed and poor', ['sell goods at higher prices', 'train soldiers', 'support export industries'])
    ,
    qd('By the late 1930s, the Great Depression in Canada was eased largely due to ___.', 'increased industrial production connected to preparations for war', ['a sudden return of high crop prices', 'the end of all government relief programs', 'a new gold rush'])
    ,
], seed=402))

all_worksheets.append(ws('History', 3, 'Canada and the Second World War', [
    qd('Canada declared war on Germany in September 1939 about a week after Britain, reflecting Canadian ___.', 'growing independence in foreign policy', ['complete control by Britain', 'refusal to participate in the war', 'alliance with Germany'])
    ,
    qd('The Royal Canadian Navy played a major role protecting supply convoys during the ___.', 'Battle of the Atlantic', ['Battle of Britain', 'invasion of Sicily', 'Pacific campaign only'])
    ,
    qd('Canadian troops played a major role in the amphibious invasion of Europe on ___.', 'D-Day, June 1944', ['Armistice Day, 1918', 'VE Day, 1945', 'Pearl Harbor Day, 1941'])
    ,
    qd('The Holocaust refers to the systematic Nazi genocide targeting ___.', 'Jewish people and other persecuted groups', ['only soldiers in combat', 'only political leaders', 'civilians in Canada'])
    ,
    qd('During World War II, thousands of Japanese Canadians were forcibly relocated and interned due to ___.', 'wartime prejudice and fear following the attack on Pearl Harbor', ['a direct request from Japan', 'a Canadian court ruling protecting their rights', 'their own voluntary request'])
    ,
    qd('Women contributions to the World War II effort included working in ___.', 'munitions factories and auxiliary military services', ['combat infantry roles only', 'no roles at all', 'only clerical roles overseas'])
    ,
    qd('The system of rationing during World War II was introduced to ___.', 'ensure fair distribution of scarce goods for the war effort', ['increase luxury consumption', 'eliminate all trade', 'reduce factory production'])
    ,
    qd('Canada declaration of war separately from Britain in 1939 was significant because it showed ___.', 'growing Canadian sovereignty in international affairs', ['Canada opposition to the war', 'Canada forced participation', 'no real change from World War I'])
    ,
    qd('The Battle of Britain was primarily fought using ___.', 'air power', ['naval blockades only', 'trench warfare', 'chemical weapons only'])
    ,
    qd('Canadian forces suffered heavy losses in a failed raid on the French coast in 1942 known as ___.', 'the Dieppe Raid', ['D-Day', 'the Italian Campaign', 'the Battle of the Atlantic'])
    ,
    qd('The dropping of atomic bombs on Hiroshima and Nagasaki in 1945 led directly to ___.', 'the surrender of Japan and the end of World War II', ['the start of World War II', 'the invasion of Germany', 'the Battle of Britain'])
    ,
    qd('VE Day in May 1945 marked ___.', 'victory in Europe over Germany', ['the start of the war', 'the surrender of Japan', 'the beginning of the Cold War'])
    ,
    qd('Canadian industry during World War II shifted significantly toward producing ___.', 'military equipment and supplies', ['only consumer goods', 'agricultural exports exclusively', 'no manufactured goods'])
    ,
    qd('The Mackenzie King government policy of conscription during World War II, decided partly by a national plebiscite, dealt with ___.', 'whether to send conscripts overseas', ['ending the war early', 'joining the League of Nations', 'trade with the United States']),
    qd('Canada contribution of troops, resources, and industry during World War II helped establish it as a ___ on the world stage.', 'middle power with growing international influence', ['a colony fully controlled by Britain', 'a neutral country', 'an isolated nation']),
], seed=403))

all_worksheets.append(ws('History', 4, 'Canada in the Cold War Era', [
    qd('The Cold War was primarily a rivalry between the United States and ___.', 'the Soviet Union', ['Germany', 'Japan', 'China alone']),
    qd('Canada joined a military alliance in 1949 designed to counter Soviet influence, called ___.', 'NATO', ['the League of Nations', 'the United Nations Security Council alone', 'the Warsaw Pact']),
    qd('Lester B Pearson won a Nobel Peace Prize for his role in resolving the ___.', 'Suez Crisis', ['Cuban Missile Crisis', 'Korean War', 'Vietnam War'])
    ,
    qd('Pearson response to the Suez Crisis led to the creation of the modern concept of ___.', 'United Nations peacekeeping', ['a new military alliance', 'a nuclear weapons treaty', 'a trade agreement'])
    ,
    qd('During the Cold War, Canada joined NORAD, a joint defence agreement with the United States, mainly to ___.', 'monitor and defend North American airspace', ['expand trade in Asia', 'colonize new territory', 'end the United Nations'])
    ,
    qd('The Cuban Missile Crisis of 1962 brought the world close to ___.', 'nuclear war', ['a trade war only', 'a stock market crash', 'a border dispute with Mexico'])
    ,
    qd('The threat of mutual nuclear destruction between superpowers during the Cold War is often referred to by the acronym ___.', 'MAD, mutually assured destruction', ['NATO', 'UN', 'GDP'])
    ,
    qd('Canada involvement in the Korean War in the early 1950s was part of a broader effort to ___.', 'contain the spread of communism', ['support Japanese expansion', 'end all foreign alliances', 'withdraw from world affairs']),
    qd('The Avro Arrow cancellation in 1959 is often cited as an example of ___.', 'a controversial Cold War era defence decision', ['a peacekeeping mission', 'a trade agreement', 'a civil rights victory'])
    ,
    qd('Canada acceptance of nuclear warheads on Canadian soil in the 1960s caused significant public ___.', 'debate and protest', ['unanimous support', 'complete indifference', 'immediate approval by all parties'])
    ,
    qd('The Berlin Wall, built in 1961, physically divided ___.', 'East and West Berlin', ['North and South Korea', 'East and West Germany governments only', 'Canada and the United States'])
    ,
    qd('The fall of the Berlin Wall in 1989 symbolized the beginning of the end of the ___.', 'Cold War', ['First World War', 'Great Depression', 'Vietnam War'])
    ,
    qd('Canada role during the Cold War was often described as that of a ___ between the superpowers.', 'middle power and mediator', ['dominant superpower', 'colony of the Soviet Union', 'neutral non-participant with no alliances'])
    ,
    qd('The arms race during the Cold War referred to the competition to build up ___.', 'nuclear and military arsenals', ['agricultural exports', 'space tourism programs', 'international trade routes only'])
    ,
    qd('Canadian peacekeepers were deployed to various global conflicts during the Cold War under the authority of the ___.', 'United Nations', ['Warsaw Pact', 'Soviet government', 'League of Nations, which no longer existed by then']),
], seed=404))

all_worksheets.append(ws('History', 5, 'Postwar Immigration and Multiculturalism', [
    qd('After World War II, Canada experienced a significant wave of immigration mainly from ___.', 'Europe, including displaced persons', ['only Asia', 'only Africa', 'only South America']),
    qd('The points system introduced in 1967 changed Canadian immigration policy by ___.', 'evaluating applicants based on skills and education rather than country of origin', ['banning all immigration', 'restricting immigration to British citizens only', 'requiring a religious test'])
    ,
    qd('Canada adopted an official policy of multiculturalism in 1971 under Prime Minister ___.', 'Pierre Trudeau', ['Lester Pearson', 'John Diefenbaker', 'Mackenzie King'])
    ,
    qd('The Immigration Act of 1976 established Canada modern approach by emphasizing ___.', 'family reunification, economic needs, and refugee protection', ['a total ban on refugees', 'a single country quota system', 'mandatory return migration'])
    ,
    qd('Prior to the 1960s, Canadian immigration policy was often criticized for favouring immigrants from ___.', 'Britain and other European nations', ['every country equally', 'only Asia', 'only the Caribbean'])
    ,
    qd('The concept of Canada as a cultural mosaic contrasts with the American idea of a ___.', 'melting pot', ['single ethnic identity', 'closed border policy', 'monoculture by law'])
    ,
    qd('Refugee resettlement programs, such as those welcoming people fleeing Vietnam in the late 1970s, reflected Canada growing role in ___.', 'international humanitarian response', ['military expansion', 'trade protectionism', 'isolationist policy'])
    ,
    qd('Multiculturalism policy in Canada aims to ___.', 'encourage cultural diversity while promoting national unity', ['force assimilation into one culture', 'eliminate immigration entirely', 'separate ethnic groups permanently'])
    ,
    qd('The Canadian Charter of Rights and Freedoms, enacted in 1982, helped protect ___.', 'individual rights and cultural diversity', ['only property rights', 'only the rights of the majority group', 'corporate rights exclusively'])
    ,
    qd('Chain migration refers to the pattern where ___.', 'immigrants sponsor family members to join them after settling', ['immigration numbers decrease over time', 'only single individuals are allowed entry', 'migration happens randomly with no pattern'])
    ,
    qd('Ethnic enclaves that developed in major Canadian cities after large waves of immigration often provided newcomers with ___.', 'community support and cultural familiarity', ['isolation with no support', 'immediate full assimilation', 'guaranteed wealth'])
    ,
    qd('Canada acceptance of Hong Kong immigrants in the years surrounding 1997 was influenced by ___.', 'the transfer of Hong Kong sovereignty to China', ['a natural disaster in Hong Kong', 'a trade war with Britain', 'a Canadian military campaign'])
    ,
    qd('Language and settlement services for new immigrants are an example of government support for ___.', 'integration', ['deportation', 'assimilation by force', 'exclusion'])
    ,
    qd('Critics of early twentieth century Canadian immigration policy point to discriminatory measures such as the ___.', 'Chinese Head Tax', ['Immigration Act of 1976', 'Charter of Rights and Freedoms', 'Multiculturalism Act only'])
    ,
    qd('The shift in source countries for Canadian immigrants over the twentieth century moved increasingly toward ___.', 'Asia, Africa, and the Caribbean', ['only Western Europe', 'only the United States', 'only Australia']),
], seed=405))

all_worksheets.append(ws('History', 6, 'Quebec Nationalism and the Quiet Revolution', [
    qd('The Quiet Revolution of the 1960s in Quebec involved rapid ___.', 'modernization and secularization of society', ['military expansion', 'population decline', 'return to traditional rule by the church'])
    ,
    qd('Before the Quiet Revolution, Quebec society and institutions such as education were heavily influenced by the ___.', 'Catholic Church', ['federal government exclusively', 'United Nations', 'British monarchy directly'])
    ,
    qd('The slogan Maitres chez nous, meaning masters in our own house, reflected Quebec desire for ___.', 'greater control over its own economy and resources', ['full separation immediately', 'closer ties with France only', 'a return to old traditions'])
    ,
    qd('The Front de Liberation du Quebec, or FLQ, was a group that used ___ to pursue Quebec independence.', 'violence and terrorism', ['peaceful referendums only', 'international diplomacy only', 'economic boycotts only'])
    ,
    qd('The October Crisis of 1970 led the federal government to invoke the ___.', 'War Measures Act', ['Immigration Act', 'Multiculturalism Act', 'Charter of Rights and Freedoms'])
    ,
    qd('The Parti Quebecois, founded in 1968, campaigned primarily for ___.', 'Quebec sovereignty', ['stronger ties with English Canada', 'increased immigration', 'military expansion'])
    ,
    qd('The 1980 Quebec referendum on sovereignty association resulted in ___.', 'a majority voting to remain in Canada', ['a majority voting for independence', 'a tie with no result', 'the cancellation of the vote'])
    ,
    qd('The 1995 Quebec referendum on sovereignty was decided by an extremely ___ margin.', 'narrow', ['overwhelming', 'unanimous', 'irrelevant, since it was not held'])
    ,
    qd('Bill 101, passed in Quebec in 1977, made French the ___ language of the province.', 'official', ['secondary', 'banned', 'optional'])
    ,
    qd('The Quiet Revolution led to major growth in the role of the Quebec provincial government in areas such as ___.', 'education and social services', ['military defence only', 'foreign trade with Europe only', 'federal elections only'])
    ,
    qd('Quebec nationalism in the twentieth century was fueled partly by concerns over preserving ___.', 'French language and culture', ['English language dominance', 'Catholic Church control', 'ties with the British monarchy'])
    ,
    qd('The Meech Lake Accord of the late 1980s attempted, and ultimately failed, to ___.', 'recognize Quebec as a distinct society within the constitution', ['grant Quebec full independence', 'abolish the Quebec provincial government', 'remove French as an official language'])
    ,
    qd('Quiet Revolution reforms included the nationalization of the ___ industry in Quebec.', 'electricity, forming Hydro-Quebec', ['automobile', 'agricultural', 'mining only'])
    ,
    qd('The debate over Quebec place within Canada is often referred to as the issue of Canadian ___.', 'national unity', ['military alliance', 'trade policy', 'immigration policy'])
    ,
    qd('Rene Levesque, a key figure in the Quiet Revolution era, later became premier and led the movement for ___.', 'Quebec sovereignty', ['stronger federalism', 'reunification with France', 'abolishing provincial government'])
    ,
], seed=406))

all_worksheets.append(ws('History', 7, 'Indigenous Peoples in Twentieth Century Canada', [
    qd('Residential schools operated in Canada throughout much of the twentieth century with the goal of ___.', 'forcibly assimilating Indigenous children into settler culture', ['preserving Indigenous languages', 'providing equal opportunity education identical to public schools', 'promoting Indigenous self-government'])
    ,
    qd('The Indian Act, first passed in 1876 and amended many times, governs many aspects of ___.', 'Indigenous peoples legal status and governance', ['immigration policy', 'provincial boundaries', 'international trade'])
    ,
    qd('Indigenous peoples were not permitted to vote in federal elections without losing status until ___.', '1960', ['1867', '1918', '1982'])
    ,
    qd('The 1969 White Paper proposed by the federal government sought to ___, but was strongly opposed by Indigenous groups.', 'eliminate the Indian Act and special status', ['expand treaty rights', 'create new reserves', 'return more land immediately'])
    ,
    qd('Treaties signed between Indigenous nations and the Crown were intended to establish ___.', 'agreements over land and resources', ['permanent military alliances only', 'trade routes with Europe only', 'international borders with the United States'])
    ,
    qd('The Sixties Scoop refers to the practice of ___.', 'removing Indigenous children from their families and placing them in non-Indigenous homes', ['relocating entire Indigenous communities to cities', 'granting Indigenous peoples the right to vote', 'creating new reserves in the 1960s']),
    qd('The Truth and Reconciliation Commission was established to document the impacts of ___.', 'the residential school system', ['the October Crisis', 'the Quiet Revolution', 'World War II internment'])
    ,
    qd('Indigenous self-government movements in the late twentieth century sought greater control over ___.', 'their own governance, land, and resources', ['federal elections only', 'provincial boundaries only', 'international trade agreements'])
    ,
    qd('The creation of Nunavut as a separate territory in 1999 was a significant step in ___.', 'Inuit self-governance', ['ending all treaties', 'abolishing provincial governments', 'increasing immigration'])
    ,
    qd('Land claims negotiations between Indigenous nations and governments often address unresolved issues from ___.', 'historical treaties and unceded territory', ['World War II alliances', 'the Quiet Revolution', 'the Cold War arms race'])
    ,
    qd('The reserve system established under the Indian Act was intended by the government to ___.', 'confine Indigenous peoples to designated lands', ['expand Indigenous territory freely', 'grant full provincial status to Indigenous nations', 'end all government involvement in Indigenous affairs'])
    ,
    qd('Indigenous veterans who served in World War I and World War II often returned home to face ___.', 'continued discrimination and loss of status', ['immediate full citizenship rights', 'automatic land grants larger than promised', 'complete equality with other veterans'])
    ,
    qd('The term unceded territory refers to land that ___.', 'was never formally surrendered by Indigenous peoples through treaty', ['was fully purchased through treaty', 'belongs to no one', 'was granted entirely to the provinces'])
    ,
    qd('Indigenous activism in the late twentieth century, including protests and legal challenges, aimed to secure ___.', 'recognition of rights and title to land', ['new provincial borders', 'increased conscription', 'trade tariffs'])
    ,
    qd('The relationship between Indigenous peoples and the Canadian government is often described using the term ___.', 'nation to nation', ['fully assimilated', 'entirely separate with no interaction', 'identical to provincial relations']),
], seed=407))

all_worksheets.append(ws('History', 8, 'Human Rights and Social Change in Canada', [
    qd('The Canadian Charter of Rights and Freedoms, part of the Constitution since 1982, protects ___.', 'fundamental individual rights and freedoms', ['only property rights', 'only provincial powers', 'only military rights'])
    ,
    qd('The Canadian Bill of Rights, passed in 1960, was an early federal effort to protect ___.', 'individual rights', ['only economic rights', 'only rights for veterans', 'provincial boundaries'])
    ,
    qd('The womens movement of the 1960s and 1970s in Canada campaigned for issues including ___.', 'equal pay and reproductive rights', ['ending all education for women', 'reducing voting rights', 'removing women from the workforce'])
    ,
    qd('The Royal Commission on the Status of Women, established in 1967, examined ___.', 'the status and rights of women in Canadian society', ['immigration policy only', 'military spending only', 'provincial boundaries only'])
    ,
    qd('Human rights legislation in Canada increasingly protected groups from discrimination based on factors such as ___.', 'race, gender, and religion', ['income level only', 'political party only', 'province of residence only'])
    ,
    qd('The legalization of same sex marriage across Canada was achieved nationally in ___.', '2005', ['1982', '1960', '1995']),
    qd('The disability rights movement in Canada pushed for changes such as ___.', 'improved accessibility and anti-discrimination protections', ['reduced access to public services', 'removal of all legal protections', 'segregation from public spaces'])
    ,
    qd('Labour unions in twentieth century Canada advocated for improvements such as ___.', 'better wages, safer conditions, and shorter work hours', ['longer work hours', 'lower wages', 'fewer legal protections'])
    ,
    qd('The civil rights movement in the United States influenced Canadian activism related to ___.', 'racial equality and anti-discrimination efforts', ['military expansion', 'trade policy only', 'provincial redistricting only'])
    ,
    qd('Employment equity policies in Canada are designed to address ___.', 'historic discrimination against underrepresented groups in the workforce', ['reducing overall employment', 'favouring one political party', 'eliminating provincial jurisdiction over labour'])
    ,
    qd('Section 15 of the Canadian Charter of Rights and Freedoms specifically addresses ___.', 'equality rights', ['military authority', 'provincial taxation', 'international trade'])
    ,
    qd('Social movements advocating for LGBTQ rights in Canada worked toward goals including ___.', 'legal recognition and protection from discrimination', ['increased criminalization', 'removal of existing protections', 'exclusion from public life'])
    ,
    qd('The persons case of 1929 was significant because it established that women were legally considered ___.', 'persons eligible for appointment to the Senate', ['ineligible to vote', 'ineligible for any public office', 'unable to own property'])
    ,
    qd('Access to universal healthcare in Canada, expanded through the twentieth century, is considered by many an example of ___.', 'social policy promoting equality', ['a purely private industry', 'a provincial only benefit with no federal role', 'a benefit limited to veterans only'])
    ,
    qd('Human rights tribunals and commissions in Canada exist to investigate complaints related to ___.', 'discrimination', ['immigration quotas only', 'trade disputes only', 'provincial budgets only'])
    ,
], seed=408))

all_worksheets.append(ws('History', 9, 'Canadian Foreign Policy and Peacekeeping', [
    qd('Canada tradition of peacekeeping is often traced back to the actions of Lester B Pearson during the ___.', 'Suez Crisis of 1956', ['Cuban Missile Crisis', 'Korean War', 'Gulf War'])
    ,
    qd('Canadian peacekeepers typically operate under the authority of the ___.', 'United Nations', ['NATO exclusively', 'a single foreign government', 'no international organization'])
    ,
    qd('Canada foreign policy after World War II generally favoured ___.', 'multilateral cooperation through international organizations', ['complete isolation from world affairs', 'unilateral military action', 'alliance with the Soviet Union'])
    ,
    qd('Canada became a founding member of the United Nations in ___.', '1945', ['1919', '1939', '1957']),
    qd('The concept of Canada as a middle power reflects its role as a country that ___.', 'exercises influence through diplomacy and cooperation rather than military dominance', ['controls a global empire', 'refuses all foreign alliances', 'has the largest military in the world'])
    ,
    qd('Canada joined NATO in 1949 primarily to ___.', 'provide collective defence against the Soviet threat', ['expand trade with Asia', 'end the United Nations', 'colonize new territory'])
    ,
    qd('Canadian involvement in international peacekeeping missions has occurred in regions including ___.', 'the Middle East, Africa, and the Balkans', ['only within Canadian borders', 'only in Europe', 'only in South America'])
    ,
    qd('Canada decision not to join the United States invasion of Iraq in 2003 reflected its foreign policy emphasis on ___.', 'multilateral United Nations support before military action', ['automatic support for all United States actions', 'complete military isolation', 'alliance with Iraq'])
    ,
    qd('Canadian foreign aid programs are generally intended to ___.', 'support development and humanitarian needs in other countries', ['fund only Canadian military expansion', 'restrict trade with developing nations', 'increase global military conflict'])
    ,
    qd('Canada relationship with the United States, its largest trading partner, has generally been characterized by ___.', 'close economic ties alongside occasional policy disagreements', ['complete economic separation', 'no trade relationship at all', 'constant military conflict'])
    ,
    qd('The Order of Canada and similar honours recognize contributions that may include ___.', 'humanitarian and diplomatic service', ['only athletic achievement', 'only military rank', 'only business profit'])
    ,
    qd('Canada support for international treaties, such as those on climate and human rights, reflects its foreign policy value of ___.', 'multilateralism', ['isolationism', 'unilateral action only', 'military expansion'])
    ,
    qd('Canadian troops served in Afghanistan in the 2000s and 2010s as part of a mission authorized by ___.', 'NATO and the United Nations', ['a purely Canadian decision with no allies', 'the Soviet Union', 'the League of Nations, which no longer existed'])
    ,
    qd('The Colombo Plan, which Canada joined in the 1950s, aimed to provide ___.', 'economic and technical aid to developing Commonwealth nations', ['military bases for foreign powers', 'trade barriers against Asia', 'refugee resettlement exclusively'])
    ,
    qd('Canadian diplomacy often emphasizes the value of ___ in resolving international conflicts.', 'negotiation and international cooperation', ['unilateral military force', 'complete withdrawal from world affairs', 'ignoring international law']),
], seed=409))

all_worksheets.append(ws('History', 10, 'Canadian Identity and Culture in the Twentieth Century', [
    qd('Canada adopted its current national flag, featuring the maple leaf, in ___.', '1965', ['1867', '1931', '1982']),
    qd('The patriation of the Canadian Constitution in 1982 meant that Canada gained the power to ___.', 'amend its own constitution without approval from Britain', ['join the United Nations', 'declare war independently for the first time', 'elect a monarch'])
    ,
    qd('The Statute of Westminster in 1931 granted Canada greater ___.', 'legislative independence from Britain', ['military control over Britain', 'territory in Europe', 'control over United States policy'])
    ,
    qd('Canadian content regulations for broadcasting were introduced to ___.', 'support Canadian culture and artists in media', ['ban all foreign media entirely', 'promote only American programming', 'eliminate public broadcasting'])
    ,
    qd('The Canadian Broadcasting Corporation was established to provide ___.', 'a national public broadcasting service', ['a private American owned network', 'a purely regional service with no national reach', 'a service exclusively for government use']),
    qd('National symbols such as the beaver, maple leaf, and O Canada help express Canadian ___.', 'identity', ['military policy', 'trade agreements', 'immigration law'])
    ,
    qd('Bilingualism became official federal policy in Canada with the Official Languages Act of ___.', '1969', ['1867', '1931', '1982']),
    qd('The Royal Commission on Bilingualism and Biculturalism in the 1960s examined the relationship between ___.', 'English and French speaking Canadians', ['Canada and the United States', 'Indigenous nations and the federal government only', 'provinces and territories only'])
    ,
    qd('Canadian literature and art in the twentieth century increasingly explored themes of ___.', 'national identity and regional diversity', ['exclusively European history', 'only military conflict', 'only economic policy'])
    ,
    qd('Hosting international events such as the Expo 67 world fair and the Olympics helped shape Canada image as a ___.', 'modern, welcoming nation on the world stage', ['closed off, isolated country', 'purely agricultural economy', 'military superpower'])
    ,
    qd('Canadian identity is often described as a mosaic because it emphasizes ___.', 'the coexistence of diverse cultures', ['a single dominant culture', 'the elimination of regional differences', 'strict cultural assimilation'])
    ,
    qd('Regional identities within Canada, such as those of the Maritimes, Quebec, and the West, reflect differences in ___.', 'history, economy, and culture', ['identical provincial laws', 'a single shared language only', 'uniform population size'])
    ,
    qd('The growth of Canadian nationalism in the twentieth century was partly a response to concerns about ___.', 'excessive American cultural and economic influence', ['excessive influence from Indigenous nations', 'too much independence from Britain too early', 'a lack of any foreign relations'])
    ,
    qd('Public healthcare, introduced nationally in the 1960s, became an important part of Canadian identity by promoting ___.', 'universal access to medical care', ['private only medical access', 'reduced access for rural areas', 'coverage for veterans exclusively'])
    ,
    qd('Canada growing sense of independent identity through the twentieth century is reflected in its shift from colony to ___.', 'sovereign nation with its own foreign policy', ['a more dependent relationship with Britain', 'a province of the United States', 'a territory without self-government'])
    ,
], seed=410))


if __name__ == '__main__':
    write_worksheets(10, all_worksheets)











