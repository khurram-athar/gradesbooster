#!/usr/bin/env python3
"""Grade 10, Days 111-120 -- extends Grade 10 from 110 to 120 days. Topics
chosen after grepping the existing Day 1-110 title list (data/grade10.json)
extensively to avoid any overlap: ellipsis and omission, juxtaposition,
letters of apology, memes and internet culture, emphatic pronouns, foil
characters, monologue writing, and round vs flat characters; limits, the
unit circle, De Moivre's Theorem, parametric equations, the fundamental
theorem of algebra, continued fractions, graph theory, the central limit
theorem, and continuity; the human eye, the human ear, antibiotic
resistance, colloids and emulsions, comets/meteors/asteroids, the physics
of roller coasters, bird migration, the excretory system, and desert
ecosystems; Newfoundland joining Confederation in 1949, the Balfour
Declaration, the Naval Service Act of 1910, the British Commonwealth Air
Training Plan, the St. Lawrence Seaway, the Alaska Boundary Dispute, the
Sixties Scoop, the Nisga'a Treaty, and Clifford Sifton's settlement of
the Prairies.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E10 = 'https://tvolearn.com/pages/grade-10-english'
M10 = 'https://tvolearn.com/pages/grade-10-mathematics'
S10 = 'https://tvolearn.com/pages/grade-10-science'
H10 = 'https://tvolearn.com/pages/grade-10-history'
RE, RM, RS, RH = (
    'TVO Learn: Grade 10 English',
    'TVO Learn: Grade 10 Mathematics',
    'TVO Learn: Grade 10 Science',
    'TVO Learn: Grade 10 History',
)


def E(t, s, q):
    return sub('English', t, s, RE, E10, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M10, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S10, q)


def H(t, s, q):
    return sub('History', t, s, RH, H10, q)


def _rebalance_answer_positions(days, seed=20260730):
    import random
    rng = random.Random(seed)
    quizzes = [sub_entry[5] for _, subs in days for sub_entry in subs]
    n = sum(len(q) for q in quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in quizzes:
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


g10_111_120 = [
day(111, [
E('Grammar: Ellipsis and Omission in Writing',
  'Grade 10 English strand: an ellipsis shows an omission of words from a quotation or indicates a trailing off in thought, and using it correctly helps writers condense or shape meaning without distorting the original text.',
  [('What does an ellipsis indicate when used in a direct quotation?', ['That words have been omitted from the original text', 'That the entire quotation is false', 'That the sentence has ended with a question', 'That the writer disagrees with the quotation'], 0),
   ('An ellipsis can also show what in dialogue?', ['A pause or trailing off in thought', 'A shout or exclamation only', 'A grammatical error', 'A complete stop with no further meaning'], 0),
   ('How many dots typically make up a standard ellipsis?', ['Three', 'Two', 'Five', 'One'], 0),
   ('Why must writers be careful when omitting words from a quotation with an ellipsis?', ['Omitting words could distort the original meaning if done carelessly', 'Ellipses always make quotations more accurate', 'Omitting words is never allowed under any circumstance', 'Ellipses have no effect on meaning'], 0),
   ('In academic writing, an ellipsis is often used to ___.', ['Shorten a long quotation while preserving its essential meaning', 'Replace all punctuation in an essay', 'Indicate the end of an entire essay', 'Show that a source is completely unreliable'], 0)]),
M('Calculus Foundations: An Introduction to Limits',
  'Grade 10 Math strand: a limit describes the value a function approaches as its input approaches a certain number, a foundational idea used to formally define the derivative and analyze function behaviour.',
  [('What does a limit describe in mathematics?', ['The value a function approaches as its input gets closer to a certain number', 'The exact value of a function at every point', 'A fixed number that never changes', 'The total area under a curve only'], 0),
   ('Why are limits considered foundational to calculus?', ['They are used to formally define the derivative', 'They have no connection to any other calculus concept', 'They only apply to whole numbers', 'They eliminate the need to study functions'], 0),
   ('As x approaches 3, if f(x) gets closer and closer to 9, what is the limit of f(x) as x approaches 3?', ['9', '3', '0', 'Undefined in all cases'], 0),
   ('Can a limit exist at a point even if the function is undefined there?', ['Yes, a limit can exist even if the function itself is undefined at that point', 'No, a limit only exists where the function is defined', 'Limits never exist for undefined functions under any circumstance', 'Limits are unrelated to function values'], 0),
   ('Understanding limits helps mathematicians analyze ___.', ['How a function behaves as it approaches specific values', 'Only the colour of a graph', 'Only whole number arithmetic', 'Only basic geometry'], 0)]),
Sc('The Human Eye: Structure and the Physics of Vision',
   'Grade 10 Science strand: the eye uses a lens to focus light onto the retina, where light-sensitive cells convert it into electrical signals interpreted by the brain, combining biology with the physics of optics.',
   [('What structure in the eye focuses light onto the retina?', ['The lens', 'The eardrum', 'The trachea', 'The epidermis'], 0),
    ('What does the retina contain that responds to light?', ['Light-sensitive cells', 'Muscle fibres only', 'Digestive enzymes', 'Bone tissue'], 0),
    ('How does the brain use signals sent from the retina?', ['It interprets them to form the images we perceive as vision', 'It converts them into sound', 'It ignores them entirely', 'It uses them only to regulate heart rate'], 0),
    ('Why might a persons vision be blurry if the eyes lens does not focus light correctly?', ['Light does not converge properly onto the retina', 'The retina contains too much light-sensitive tissue', 'The eye produces no light at all', 'The brain refuses to process any images'], 0),
    ('The study of how light interacts with the eye combines biology with which branch of physics?', ['Optics', 'Thermodynamics', 'Astronomy', 'Nuclear physics'], 0)]),
H('Newfoundland Joins Confederation in 1949',
  'Grade 10 History strand: Newfoundland became Canadas tenth province in 1949 after a close referendum vote, joining Confederation over 80 years after the original four provinces united in 1867.',
  [('In what year did Newfoundland join Confederation?', ['1949', '1867', '1905', '1999'], 0),
   ('How did Newfoundland decide to join Canada?', ['Through a close referendum vote', 'Through a unilateral government decision with no vote', 'Through a military conflict', 'Through a coin flip'], 0),
   ('What number province did Newfoundland become?', ['The tenth province', 'The first province', 'The fifth province', 'The last territory'], 0),
   ('How many years after the original Confederation of 1867 did Newfoundland join?', ['Over 80 years later', 'Immediately in 1867', 'Only 5 years later', 'Over 200 years later'], 0),
   ('Why is Newfoundlands entry into Confederation historically significant?', ['It completed a major stage of Canadas territorial expansion', 'It had no impact on Canadian history', 'It caused Canada to lose a province', 'It happened before Canada existed'], 0)]),
]),
day(112, [
E('Reading: Analyzing Juxtaposition in Literature',
  'Grade 10 English strand: juxtaposition places two contrasting elements side by side in a text, highlighting their differences and creating deeper meaning, tension, or emphasis for the reader.',
  [('What is juxtaposition?', ['Placing two contrasting elements side by side', 'Combining two similar ideas into one', 'A type of punctuation mark', 'A grammar rule for verb tense'], 0),
   ('What effect does juxtaposition typically create in a text?', ['It highlights differences and creates deeper meaning or tension', 'It removes all meaning from a text', 'It always confuses the reader with no purpose', 'It eliminates the need for description'], 0),
   ('Which is an example of juxtaposition in a novel?', ['Describing a lavish celebration immediately followed by a scene of poverty', 'Describing only one setting throughout the story', 'Listing facts with no comparison', 'Using only dialogue with no description'], 0),
   ('Why might an author juxtapose two characters?', ['To emphasize how different the characters are from each other', 'To make the characters seem identical', 'To avoid describing either character', 'To remove conflict from the story'], 0),
   ('Juxtaposition is often used by authors to explore contrasts such as ___.', ['Wealth and poverty, or innocence and corruption', 'Only numbers and equations', 'Only weather patterns', 'Only geographic locations with no thematic meaning'], 0)]),
M('Trigonometry: An Introduction to the Unit Circle',
  'Grade 10 Math strand: the unit circle is a circle with radius 1 centred at the origin, used to define sine and cosine for any angle and to connect trigonometry with coordinate geometry.',
  [('What is the radius of the unit circle?', ['1', '0', '2', 'It has no fixed radius'], 0),
   ('Where is the unit circle centred?', ['At the origin (0, 0)', 'At the point (1, 1)', 'At the point (5, 5)', 'It has no defined centre'], 0),
   ('What two trigonometric values can be defined using coordinates on the unit circle?', ['Sine and cosine', 'Only the radius and diameter', 'Only the area and circumference', 'Only the slope and y-intercept'], 0),
   ('What is the significance of the unit circle in trigonometry?', ['It provides a way to define sine and cosine for any angle', 'It only works for angles less than 90 degrees', 'It replaces the need for angles entirely', 'It cannot be used for any calculations'], 0),
   ('The unit circle helps connect which two branches of mathematics?', ['Trigonometry and coordinate geometry', 'Only arithmetic and probability', 'Only statistics and data management', 'Only geometry and financial literacy'], 0)]),
Sc('The Human Ear: Structure and the Physics of Hearing',
   'Grade 10 Science strand: the ear captures sound waves and converts their vibrations into electrical signals through structures like the eardrum and cochlea, which the brain interprets as sound, connecting biology to acoustics.',
   [('What does the ear capture and convert into signals?', ['Sound waves', 'Light waves', 'Chemical signals', 'Magnetic fields'], 0),
    ('What structure vibrates when sound waves first enter the ear?', ['The eardrum', 'The cochlea alone', 'The optic nerve', 'The retina'], 0),
    ('What part of the inner ear helps convert vibrations into electrical signals?', ['The cochlea', 'The pupil', 'The trachea', 'The epidermis'], 0),
    ('How does the brain use the electrical signals sent from the ear?', ['It interprets them as sound', 'It ignores them completely', 'It converts them into images', 'It uses them only to control digestion'], 0),
    ('Studying the physics of sound and hearing connects biology to which field of physics?', ['Acoustics (the study of sound)', 'Optics (the study of light)', 'Thermodynamics (the study of heat)', 'Astronomy (the study of space)'], 0)]),
H('The Balfour Declaration of 1926 and Canadian Autonomy',
  'Grade 10 History strand: the Balfour Declaration of 1926 recognized Canada and other dominions as equal in status to Britain, laying important groundwork for the later Statute of Westminster and full Canadian legislative independence.',
  [('What did the Balfour Declaration of 1926 recognize about Canada?', ['That Canada was equal in status to Britain', 'That Canada was a colony with no rights', 'That Canada should be governed entirely by Britain', 'That Canada had no relationship with Britain at all'], 0),
   ('What later, more formal law built on the Balfour Declaration?', ['The Statute of Westminster', 'The Canadian Bill of Rights', 'The Charter of Rights and Freedoms', 'The Indian Act'], 0),
   ('In what year was the Balfour Declaration issued?', ['1926', '1867', '1949', '1999'], 0),
   ('Why is the Balfour Declaration considered a milestone in Canadian history?', ['It was an important step toward full Canadian legislative independence', 'It ended all of Canadas ties to Britain immediately', 'It had no lasting significance for Canada', 'It occurred after Canada already had full independence'], 0),
   ('The Balfour Declaration applied to Canada as one of several ___.', ['British dominions seeking greater self-governance', 'Foreign enemy nations', 'United Nations member states', 'Provinces within Canada'], 0)]),
]),
day(113, [
E('Writing: Writing a Letter of Apology',
  'Grade 10 English strand: a letter of apology clearly acknowledges a mistake, expresses genuine regret, and often includes a plan to make things right, using a sincere and thoughtful tone throughout.',
  [('What should a letter of apology clearly acknowledge?', ['The mistake that was made', 'Only unrelated topics', 'Nothing specific at all', 'Only the recipients own faults'], 0),
   ('What tone should a letter of apology typically have?', ['Sincere and genuine', 'Sarcastic and joking', 'Angry and blaming', 'Cold and indifferent'], 0),
   ('Why might a letter of apology include a plan to make things right?', ['It shows genuine commitment to correcting the mistake', 'Plans are never appropriate in an apology', 'It shifts all blame onto someone else', 'It replaces the need for an apology'], 0),
   ('Which is an example of a sincere apology statement?', ['I am sorry for missing our meeting, and I will confirm plans earlier next time.', 'It was not really my fault anyway.', 'Sorry, but you overreacted.', 'I do not need to apologize for anything.'], 0),
   ('A well-written apology letter helps to ___.', ['Repair trust and take responsibility', 'Avoid all responsibility', 'Blame someone else entirely', 'Ignore the mistake completely'], 0)]),
M('Complex Numbers: De Moivres Theorem',
  'Grade 10 Math strand: De Moivres Theorem provides a method for raising a complex number in polar form to a power, using the formula (r(cos θ + i sin θ))^n = r^n(cos nθ + i sin nθ).',
  [('What does De Moivres Theorem help calculate?', ['A complex number in polar form raised to a power', 'The area of a triangle', 'The slope of a line', 'The volume of a sphere'], 0),
   ('De Moivres Theorem builds on which earlier concept?', ['Complex numbers in polar form', 'Basic addition of whole numbers', 'The Pythagorean Theorem', 'Simple linear equations'], 0),
   ('In De Moivres formula, what happens to the angle θ when raising to the power n?', ['It is multiplied by n', 'It is divided by n', 'It stays exactly the same', 'It becomes zero'], 0),
   ('Why is De Moivres Theorem useful for working with complex numbers?', ['It simplifies the process of raising complex numbers to large powers', 'It eliminates the need for complex numbers entirely', 'It only works for real numbers, never complex ones', 'It has no mathematical application'], 0),
   ('De Moivres Theorem connects which two areas of mathematics?', ['Trigonometry and complex numbers', 'Only basic arithmetic and geometry', 'Only statistics and probability', 'Only financial literacy and algebra'], 0)]),
Sc('Antibiotic Resistance: A Modern Challenge',
   'Grade 10 Science strand: antibiotic resistance occurs when bacteria evolve mechanisms to survive medicines designed to kill them, a growing global health concern driven by the overuse and misuse of antibiotics.',
   [('What is antibiotic resistance?', ['When bacteria evolve to survive medicines designed to kill them', 'When a medicine becomes stronger the more it is used', 'When a virus becomes weaker over time', 'When bacteria disappear completely from the body'], 0),
    ('What is a major driver of increasing antibiotic resistance?', ['Overuse and misuse of antibiotics', 'Using antibiotics too rarely', 'Regular vaccination', 'Eating a balanced diet'], 0),
    ('Why is antibiotic resistance a significant global health concern?', ['It makes some bacterial infections much harder to treat effectively', 'It has no impact on human health', 'It only affects a single country', 'It makes all infections easier to cure'], 0),
    ('What can reduce the development of antibiotic resistance?', ['Using antibiotics only when prescribed and completing the full course', 'Taking antibiotics for every illness, including viral infections', 'Sharing leftover antibiotics with others', 'Stopping antibiotics as soon as symptoms improve'], 0),
    ('Antibiotic resistance is a direct example of which biological process?', ['Natural selection acting on bacterial populations', 'A process unrelated to evolution', 'A process that only affects viruses', 'A permanently fixed trait with no change over time'], 0)]),
H('The Naval Service Act of 1910 and the Creation of the Royal Canadian Navy',
  'Grade 10 History strand: the Naval Service Act of 1910 established the Royal Canadian Navy, sparking political debate over Canadas military obligations to Britain and its growing independence in defence policy.',
  [('What did the Naval Service Act of 1910 establish?', ['The Royal Canadian Navy', 'The Royal Canadian Air Force', 'The Canadian Army', 'A national police force'], 0),
   ('What debate did the Naval Service Act spark in Canada?', ['A debate over Canadas military obligations to Britain', 'A debate over Canadian currency design', 'A debate over provincial boundaries', 'A debate over railway construction'], 0),
   ('In what year was the Naval Service Act passed?', ['1910', '1867', '1949', '1999'], 0),
   ('Why is the Naval Service Act significant in the context of Canadian independence?', ['It reflected Canadas growing role in shaping its own defence policy', 'It had no connection to Canadian independence', 'It placed Canadas entire military fully under British control with no change', 'It ended all Canadian military activity'], 0),
   ('The creation of the Royal Canadian Navy is an example of ___.', ['Canada developing its own national defence institutions', 'Canada abandoning any military development', 'A purely British institution with no Canadian involvement', 'A modern 21st-century development'], 0)]),
]),
day(114, [
E('Media Literacy: Analyzing Memes and Internet Culture',
  'Grade 10 English strand: memes spread ideas and humour quickly through images, text, and repetition, and analyzing them critically helps readers understand how internet culture shapes communication and public opinion.',
  [('What is a meme?', ['An image, video, or piece of text that spreads ideas or humour quickly online', 'A formal academic essay', 'A type of legal document', 'A printed newspaper article'], 0),
   ('How do memes typically spread?', ['Through sharing, repetition, and adaptation across the internet', 'Only through printed newspapers', 'They cannot spread at all', 'Only through formal presentations'], 0),
   ('Why is it useful to analyze memes critically?', ['To understand how internet culture shapes communication and opinion', 'Memes have no influence on culture or opinion', 'Critical analysis is never useful for internet content', 'Memes are always completely factual'], 0),
   ('What technique do memes often use to convey meaning quickly?', ['Combining a familiar image with concise text', 'Long, detailed paragraphs with no images', 'Complex legal language', 'Silence with no content at all'], 0),
   ('Memes can be considered a form of ___.', ['Modern digital communication and cultural commentary', 'Ancient handwritten manuscripts', 'Formal government documents', 'Scientific research papers only'], 0)]),
M('Algebra: An Introduction to Parametric Equations',
  'Grade 10 Math strand: parametric equations express the x and y coordinates of a curve separately in terms of a third variable, called a parameter, allowing flexible descriptions of motion and curves.',
  [('What do parametric equations use to describe a curve?', ['Separate equations for x and y in terms of a third parameter', 'Only a single equation with no parameter', 'Only whole numbers with no variables', 'Only the slope of a line'], 0),
   ('What is the third variable in parametric equations often called?', ['The parameter', 'The determinant', 'The coefficient', 'The exponent'], 0),
   ('Why might parametric equations be useful for describing motion?', ['They can show how both x and y positions change over time', 'They can only describe a single fixed point', 'They eliminate the need to track any position', 'They cannot be used to describe any motion'], 0),
   ('If x = t and y = t^2, what shape would this parametric equation likely trace?', ['A parabola', 'A straight horizontal line only', 'A perfect circle', 'A single point with no movement'], 0),
   ('Parametric equations are especially useful in fields such as ___.', ['Physics, for describing the path of a moving object', 'Only basic arithmetic', 'Only simple counting problems', 'Only measuring temperature'], 0)]),
Sc('Chemistry: Colloids and Emulsions',
   'Grade 10 Science strand: a colloid is a mixture where tiny particles are dispersed throughout another substance without dissolving, and an emulsion is a colloid formed from two liquids that would not normally mix, like oil and water.',
   [('What is a colloid?', ['A mixture where tiny particles are dispersed without fully dissolving', 'A solution where particles fully dissolve', 'A pure element with no mixture at all', 'A gas with no other substance present'], 0),
    ('What is an emulsion?', ['A colloid formed from two liquids that would not normally mix', 'A solid dissolved completely in water', 'A single pure liquid with no mixture', 'A gas dissolved in a solid'], 0),
    ('Which of these is a common example of an emulsion?', ['Mayonnaise, made from oil and water-based ingredients', 'Pure distilled water', 'A block of solid ice', 'Oxygen gas'], 0),
    ('Why do the particles in a colloid not settle out over time like in a simple mixture?', ['The particles are small enough to remain evenly dispersed', 'The particles are too large to move at all', 'Colloids contain no particles whatsoever', 'Gravity has no effect on any mixtures'], 0),
    ('What might be added to help stabilize an emulsion, like in salad dressing?', ['An emulsifier', 'A stronger acid only', 'Pure oxygen gas', 'A radioactive isotope'], 0)]),
H('The British Commonwealth Air Training Plan',
  'Grade 10 History strand: during World War II, Canada hosted the British Commonwealth Air Training Plan, training tens of thousands of Allied aircrew using Canadas wide open spaces and relative safety from enemy attack.',
  [('What was the British Commonwealth Air Training Plan?', ['A program that trained Allied aircrew in Canada during World War II', 'A trade agreement between Canada and Britain', 'A railway construction project', 'A postwar immigration program'], 0),
   ('Why was Canada chosen to host this training program?', ['Its wide open spaces and relative safety from enemy attack', 'Canada had no involvement in World War II', 'Canada had no open land available', 'Canada was under direct enemy occupation'], 0),
   ('Roughly how many Allied aircrew were trained through this program?', ['Tens of thousands', 'Only a dozen', 'None at all', 'Several hundred thousand million'], 0),
   ('What historical period does the British Commonwealth Air Training Plan belong to?', ['World War II', 'World War I', 'The Cold War', 'Confederation era'], 0),
   ('Why is the training plan significant in Canadian military history?', ['It demonstrated Canadas major contribution to the Allied war effort', 'It shows Canada had no role in World War II', 'It had no lasting impact on Canadian history', 'It only trained Canadian civilians with no military purpose'], 0)]),
]),
day(115, [
E('Grammar: Emphatic Pronouns and Intensifiers',
  'Grade 10 English strand: emphatic pronouns like myself or himself add emphasis to a noun already mentioned, while intensifiers such as very or extremely strengthen the meaning of an adjective or adverb.',
  [('What is the purpose of an emphatic pronoun?', ['To add emphasis to a noun or pronoun already mentioned', 'To replace a verb entirely', 'To act as a question word', 'To function as a preposition'], 0),
   ('Which sentence correctly uses an emphatic pronoun?', ['The principal herself announced the news.', 'The principal announced herself the news.', 'Herself the principal announced the news.', 'The principal announced the news herself very.'], 0),
   ('What is an intensifier?', ['A word that strengthens the meaning of an adjective or adverb', 'A word that replaces a noun', 'A punctuation mark', 'A type of conjunction'], 0),
   ('Which word functions as an intensifier in the sentence She was extremely tired?', ['Extremely', 'Was', 'She', 'Tired'], 0),
   ('Why should writers use intensifiers sparingly in formal writing?', ['Overusing them can weaken the precision and impact of the writing', 'Intensifiers always strengthen writing no matter how often used', 'Formal writing requires intensifiers in every sentence', 'Intensifiers are grammatically forbidden in all writing'], 0)]),
M('Algebra: The Fundamental Theorem of Algebra',
  'Grade 10 Math strand: the Fundamental Theorem of Algebra states that every polynomial equation of degree n has exactly n roots when counting complex and repeated roots, connecting algebra to complex numbers.',
  [('What does the Fundamental Theorem of Algebra state?', ['A polynomial of degree n has exactly n roots, counting complex and repeated roots', 'A polynomial always has zero roots', 'Only linear equations have any roots', 'Polynomials never have complex roots'], 0),
   ('How many roots does a degree-4 polynomial have according to this theorem?', ['Four', 'One', 'Zero', 'Infinite'], 0),
   ('What earlier math concept does this theorem connect to?', ['Complex and imaginary numbers', 'Only whole numbers', 'Only fractions', 'Only negative integers'], 0),
   ('Can a polynomials roots include complex numbers?', ['Yes, according to the Fundamental Theorem of Algebra', 'No, roots must always be whole numbers', 'No, roots must always be negative', 'Only irrational roots are allowed'], 0),
   ('Why is the Fundamental Theorem of Algebra considered important in mathematics?', ['It guarantees a predictable number of solutions for polynomial equations', 'It proves that polynomials have no solutions', 'It only applies to equations with no variables', 'It disproves the existence of complex numbers'], 0)]),
Sc('Earth Science: Comets, Meteors, and Asteroids',
   'Grade 10 Science strand: comets, meteors, and asteroids are distinct types of small bodies in space, differing in composition and behaviour, from icy comets that develop tails to rocky asteroids and burning meteors entering the atmosphere.',
   [('What are comets primarily made of?', ['Ice, dust, and rocky material', 'Pure solid metal', 'Only liquid water', 'Only gas with no solid material'], 0),
    ('What causes a comets visible tail?', ['Ice and dust vaporizing as the comet nears the sun', 'The comet reflecting moonlight only', 'The comet burning fuel like a rocket', 'A tail forms only when comets collide with planets'], 0),
    ('What is an asteroid primarily made of?', ['Rock and metal', 'Only ice', 'Only gas', 'Only liquid'], 0),
    ('What is a meteor?', ['A small piece of debris burning up as it enters a planets atmosphere', 'A fully formed planet', 'A type of star', 'A permanent moon of Earth'], 0),
    ('Where are most asteroids in our solar system located?', ['In the asteroid belt between Mars and Jupiter', 'Inside the sun', 'On the surface of Earth only', 'Beyond the orbit of Pluto only'], 0)]),
H('The St. Lawrence Seaway',
  'Grade 10 History strand: completed in 1959 as a joint project between Canada and the United States, the St. Lawrence Seaway created a deep waterway connecting the Great Lakes to the Atlantic Ocean, transforming trade and industry.',
  [('What did the St. Lawrence Seaway create?', ['A deep waterway connecting the Great Lakes to the Atlantic Ocean', 'A new railway line across the Prairies', 'A highway system in Northern Canada', 'A new international airport'], 0),
   ('Which two countries jointly built the St. Lawrence Seaway?', ['Canada and the United States', 'Canada and Britain', 'Canada and France', 'The United States and Mexico'], 0),
   ('In what year was the St. Lawrence Seaway completed?', ['1959', '1867', '1999', '1949'], 0),
   ('How did the St. Lawrence Seaway affect trade and industry?', ['It allowed large ships greater access to inland ports, boosting trade', 'It completely ended all shipping in the region', 'It had no effect on Canadian industry', 'It closed off the Great Lakes from international shipping'], 0),
   ('The St. Lawrence Seaway is an example of ___.', ['International cooperation on major infrastructure projects', 'A purely domestic Canadian project with no international involvement', 'A project that was never completed', 'A conflict between Canada and the United States'], 0)]),
]),
day(116, [
E('Reading: Analyzing Foil Characters',
  'Grade 10 English strand: a foil character has traits that contrast sharply with a main character, and this contrast helps highlight and clarify the main characters own qualities and choices.',
  [('What is a foil character?', ['A character whose traits contrast with a main character to highlight them', 'A character identical to the main character', 'A character who never appears in the story', 'A type of narrator'], 0),
   ('What is the purpose of a foil character?', ['To highlight and clarify the main characters qualities through contrast', 'To confuse the reader about the plot', 'To replace the main character entirely', 'To remove all conflict from the story'], 0),
   ('If a protagonist is impulsive, a foil character might be ___.', ['Deliberate and cautious', 'Also impulsive in the exact same way', 'Nonexistent in the story', 'A narrator only'], 0),
   ('Foil characters are most useful for revealing ___.', ['Personality traits through comparison', 'Only the setting of a story', 'Only the time period of a story', 'Nothing about the characters'], 0),
   ('Which is an example of a foil relationship?', ['A reckless character paired with a cautious character', 'Two identical characters with no differences', 'A character and the weather', 'A character and a map'], 0)]),
M('Number Theory: An Introduction to Continued Fractions',
  'Grade 10 Math strand: a continued fraction expresses a number as a whole number plus a fraction whose denominator is itself a sum involving another fraction, offering an alternative way to represent and approximate numbers.',
  [('What is a continued fraction?', ['A number expressed as a whole number plus a nested fraction', 'A fraction with no denominator', 'A whole number with no fractional part', 'A type of matrix'], 0),
   ('What can continued fractions be used to approximate?', ['Irrational numbers with increasing accuracy', 'Only whole numbers', 'Only negative numbers', 'Nothing meaningful'], 0),
   ('Continued fractions provide an alternative way to represent which type of numbers?', ['Real numbers, including irrational ones', 'Only imaginary numbers', 'Only matrices', 'Only angles'], 0),
   ('Why might mathematicians use continued fractions instead of decimals?', ['They can reveal patterns and provide highly accurate rational approximations', 'They are always less accurate than decimals', 'They cannot represent any numbers at all', 'They eliminate the need for fractions entirely'], 0),
   ('A simple continued fraction typically uses which type of numbers in its structure?', ['Whole numbers (integers)', 'Only complex numbers', 'Only negative decimals', 'Only percentages'], 0)]),
Sc('The Physics of Roller Coasters: Energy Transformations',
   'Grade 10 Science strand: roller coasters convert gravitational potential energy at the top of hills into kinetic energy as cars accelerate downward, illustrating the conservation and transformation of mechanical energy.',
   [('What type of energy does a roller coaster car have at the top of a hill?', ['Gravitational potential energy', 'Only sound energy', 'Only chemical energy', 'No energy at all'], 0),
    ('What happens to potential energy as the car speeds down a hill?', ['It converts into kinetic energy', 'It disappears completely', 'It converts into sunlight', 'It stays exactly the same amount as potential energy'], 0),
    ('What is kinetic energy?', ['The energy of motion', 'The energy stored due to height', 'The energy of sound only', 'The energy of light only'], 0),
    ('Why do roller coasters usually have their highest hill first?', ['To build up the maximum potential energy needed for the ride', 'Height has no effect on the ride', 'To make the ride slower overall', 'To eliminate all kinetic energy'], 0),
    ('Roller coasters demonstrate what general scientific principle?', ['The conservation and transformation of energy', 'That energy can be created from nothing', 'That energy disappears permanently during motion', 'That motion requires no energy at all'], 0)]),
H('The Alaska Boundary Dispute of 1903',
  'Grade 10 History strand: the Alaska Boundary Dispute was an early 20th-century disagreement between Canada and the United States over the border of the Alaska Panhandle, settled by a tribunal in a decision many Canadians saw as unfair.',
  [('What was the Alaska Boundary Dispute about?', ['A disagreement over the border of the Alaska Panhandle', 'A dispute over fishing rights in the Pacific Ocean', 'A disagreement about a railway route', 'A dispute over the Great Lakes'], 0),
   ('Which two countries were involved in the Alaska Boundary Dispute?', ['Canada and the United States', 'Canada and Russia', 'Canada and Britain only', 'The United States and Mexico'], 0),
   ('When was the Alaska Boundary Dispute settled?', ['1903', '1867', '1950', '1999'], 0),
   ('How did many Canadians view the outcome of the dispute?', ['As unfair to Canadian interests', 'As entirely fair and favourable to Canada', 'As having no effect on Canada', 'As a complete victory for Canada'], 0),
   ('The Alaska Boundary Dispute is often cited as an example of ___.', ['Canadas limited independence in foreign affairs at the time', 'Canadas complete independence from Britain by 1903', 'A conflict resolved through war', 'An issue unrelated to Canadian sovereignty'], 0)]),
]),
day(117, [
E('Writing: Writing a Monologue',
  'Grade 10 English strand: a monologue is an extended speech by a single character revealing their thoughts, motivations, or emotions, requiring a consistent and believable voice throughout.',
  [('What is a monologue?', ['An extended speech by a single character', 'A conversation between two or more characters', 'A short list of stage directions', 'A type of grammar rule'], 0),
   ('What can a monologue reveal about a character?', ['Their thoughts, motivations, or emotions', 'Only their physical appearance', 'Nothing meaningful about the character', 'Only unrelated background information'], 0),
   ('What is essential for a monologue to feel believable?', ['A consistent and authentic voice throughout', 'Constantly shifting perspectives with no consistency', 'Complete silence with no words spoken', 'A voice identical to every other character'], 0),
   ('In which context might a monologue commonly appear?', ['A play, film, or piece of dramatic writing', 'A grocery list', 'A weather report', 'A mathematical proof'], 0),
   ('Why might a writer use a monologue instead of dialogue?', ['To give deep insight into a single characters internal perspective', 'Monologues never provide any character insight', 'To avoid revealing anything about a character', 'Monologues always involve multiple speaking characters'], 0)]),
M('Discrete Math: An Introduction to Graph Theory',
  'Grade 10 Math strand: graph theory studies networks made of nodes (or vertices) connected by edges, used to model relationships and connections in systems like social networks, transportation maps, and computer networks.',
  [('What are the two basic components of a graph in graph theory?', ['Nodes (vertices) and edges', 'Only numbers', 'Only angles', 'Only fractions'], 0),
   ('What does an edge in a graph represent?', ['A connection between two nodes', 'A single isolated point', 'The colour of the graph', 'The total size of the graph'], 0),
   ('Which real-world system could be modeled using graph theory?', ['A transportation network showing routes between cities', 'The freezing point of water', 'The colour of the sky', 'The taste of a food'], 0),
   ('In graph theory, a node with many connecting edges is often called ___.', ['A highly connected or high-degree node', 'An isolated node', 'A deleted node', 'An imaginary node'], 0),
   ('Graph theory is especially useful in fields such as ___.', ['Computer science and network design', 'Only painting and drawing', 'Only cooking and recipes', 'Only music composition'], 0)]),
Sc('Bird Migration and Animal Navigation',
   'Grade 10 Science strand: many animals, especially migratory birds, travel long distances using cues like the position of the sun and stars, Earths magnetic field, and landmarks to navigate accurately.',
   [('What is bird migration?', ['The seasonal, long-distance travel of birds between habitats', 'A permanent move with no return', 'A type of hibernation', 'A method of finding food only within one location'], 0),
    ('What is one cue animals use to navigate during migration?', ['Earths magnetic field', 'The colour of nearby buildings', 'Random guessing with no cues', 'The price of local food sources'], 0),
    ('Why might birds migrate seasonally?', ['To find better food sources and breeding conditions', 'Migration serves no biological purpose', 'To avoid other birds entirely', 'To permanently leave their habitat forever'], 0),
    ('Besides Earths magnetic field, what other cues can animals use to navigate?', ['The position of the sun and stars', 'Only the colour of the sky', 'Only nearby traffic sounds', 'Only human-made maps'], 0),
    ('What term describes an animals ability to sense Earths magnetic field for navigation?', ['Magnetoreception', 'Echolocation', 'Photosynthesis', 'Osmosis'], 0)]),
H('The Sixties Scoop',
  'Grade 10 History strand: the Sixties Scoop refers to the mass removal of Indigenous children from their families and placement into non-Indigenous foster or adoptive homes from the 1960s through the 1980s, causing lasting harm to Indigenous communities.',
  [('What was the Sixties Scoop?', ['The mass removal of Indigenous children into non-Indigenous foster or adoptive homes', 'A government program to build new schools', 'A trade agreement between Canada and other countries', 'A celebration of Indigenous culture'], 0),
   ('Roughly during what period did the Sixties Scoop occur?', ['From the 1960s through the 1980s', 'Only during a single year in the 1800s', 'It has not happened yet', 'Only during World War II'], 0),
   ('What lasting impact did the Sixties Scoop have on Indigenous communities?', ['It caused significant harm, including loss of cultural connection and identity', 'It had no lasting impact on any community', 'It strengthened Indigenous family structures', 'It only affected non-Indigenous families'], 0),
   ('How is the Sixties Scoop now widely viewed by historians and the Canadian government?', ['As a harmful policy that caused significant trauma', 'As a completely positive and beneficial policy', 'As an event that never actually took place', 'As a policy with no lasting consequences'], 0),
   ('The Sixties Scoop is often studied alongside which related historical topic?', ['Residential schools and their legacy', 'The Klondike Gold Rush', 'The construction of the Avro Arrow', 'The Halifax Explosion'], 0)]),
]),
day(118, [
E('Reading: Analyzing Round and Flat Characters',
  'Grade 10 English strand: a round character is complex and multidimensional, capable of change, while a flat character is simpler, often defined by a single trait and used to support the story without extensive development.',
  [('What defines a round character?', ['A complex, multidimensional character capable of change', 'A character with no personality traits at all', 'A character who never appears in the story', 'A character defined only by their physical appearance'], 0),
   ('What defines a flat character?', ['A simpler character often defined by a single trait', 'A character who is always the protagonist', 'A character with the most complex development in the story', 'A character who narrates the entire story'], 0),
   ('Why might an author include flat characters in a story?', ['To support the plot without requiring extensive development', 'Flat characters always take over as the main character', 'Flat characters are never used in effective storytelling', 'To confuse readers about who the protagonist is'], 0),
   ('Which is an example of a round character?', ['A protagonist who grows, struggles, and changes throughout the story', 'A background character who appears for one line with no development', 'A character who is only ever described by their job title', 'A character with no name or role in the plot'], 0),
   ('Why is it useful for readers to distinguish between round and flat characters?', ['It helps readers understand which characters drive change and complexity in a story', 'This distinction has no effect on understanding a story', 'All characters in every story are exactly the same', 'Only flat characters ever matter to a story'], 0)]),
M('Statistics: An Introduction to the Central Limit Theorem',
  'Grade 10 Math strand: the Central Limit Theorem states that the distribution of sample means tends to become approximately normal as sample size increases, regardless of the shape of the original population distribution.',
  [('What does the Central Limit Theorem describe?', ['How the distribution of sample means becomes approximately normal as sample size grows', 'A rule that applies only to whole numbers', 'A theorem about the area of circles', 'A method for factoring polynomials'], 0),
   ('According to the Central Limit Theorem, what happens as sample size increases?', ['The distribution of sample means becomes more normal in shape', 'The distribution becomes more random with no pattern', 'The sample means always become identical to the population mean', 'The theorem no longer applies at all'], 0),
   ('Does the Central Limit Theorem depend on the shape of the original population?', ['No, it generally holds true regardless of the original distributions shape', 'Yes, it only works if the population is already normal', 'It only works for extremely small populations', 'It cannot be applied to any real data'], 0),
   ('Why is the Central Limit Theorem important in statistics?', ['It allows statisticians to make inferences using the normal distribution even with non-normal data', 'It has no practical use in statistics', 'It only applies to a single specific data set', 'It eliminates the need for any sampling'], 0),
   ('The Central Limit Theorem is especially useful when working with ___.', ['Sample means drawn from a larger population', 'Only a single data point', 'Only categorical, non-numeric data', 'Only data with no variation at all'], 0)]),
Sc('The Excretory System: Kidneys and Waste Removal',
   'Grade 10 Science strand: the excretory system, especially the kidneys, filters waste products and excess water from the blood, producing urine and helping maintain the bodys fluid and chemical balance.',
   [('What is the main function of the excretory system?', ['Filtering waste products and excess water from the blood', 'Pumping blood throughout the body', 'Digesting food in the stomach', 'Producing sound for speech'], 0),
    ('Which organs are the primary filters in the excretory system?', ['The kidneys', 'The lungs', 'The liver only', 'The heart'], 0),
    ('What waste product do the kidneys help remove from the body?', ['Urine, containing filtered waste and excess water', 'Only carbon dioxide', 'Only sweat', 'Only saliva'], 0),
    ('Why is maintaining fluid and chemical balance in the body important?', ['It supports proper function of cells and organs', 'Fluid balance has no effect on the body', 'The body never needs to balance fluids', 'Only muscles are affected by fluid balance'], 0),
    ('The excretory system works to keep the bodys internal environment ___.', ['Stable and balanced (homeostasis)', 'Constantly changing with no regulation', 'Completely dependent on outside temperature', 'Unrelated to overall health'], 0)]),
H('The Nisgaa Treaty and Modern Land Claims',
  'Grade 10 History strand: the Nisgaa Treaty of 2000 was a landmark modern land claims agreement recognizing Nisgaa self-government and land rights in British Columbia, setting an important precedent for later Indigenous treaties in Canada.',
  [('What did the Nisgaa Treaty recognize?', ['Nisgaa self-government and land rights', 'A complete end to all Indigenous land claims', 'A new provincial boundary', 'A new national park with no Indigenous involvement'], 0),
   ('In what year was the Nisgaa Treaty finalized?', ['2000', '1867', '1949', '1999'], 0),
   ('In which province was the Nisgaa Treaty signed?', ['British Columbia', 'Ontario', 'Quebec', 'Nova Scotia'], 0),
   ('Why is the Nisgaa Treaty considered a landmark agreement?', ['It set an important precedent for later Indigenous treaties in Canada', 'It had no effect on any future negotiations', 'It ended all Indigenous rights in Canada', 'It only applied to a single unrelated town'], 0),
   ('The Nisgaa Treaty is an example of ___.', ['A modern land claims agreement with Indigenous peoples', 'A 19th-century treaty', 'A treaty with no legal recognition', 'An agreement unrelated to Indigenous rights'], 0)]),
]),
day(119, [
M('Algebra: Advanced Applications of Continued Fractions and Approximation',
  'Grade 10 Math strand: building on continued fractions, this lesson explores how truncating a continued fraction at different points produces increasingly accurate rational approximations of irrational numbers like the square root of two.',
  [('What happens when a continued fraction is truncated at an earlier point?', ['It produces a less accurate, simpler rational approximation', 'It always produces the exact original number', 'It becomes undefined', 'It has no effect on the approximation'], 0),
   ('What happens as more terms of a continued fraction are included?', ['The approximation typically becomes more accurate', 'The approximation always becomes less accurate', 'The value becomes undefined', 'Nothing changes at all'], 0),
   ('Continued fraction approximations are especially useful for representing ___.', ['Irrational numbers, like the square root of two', 'Only whole numbers', 'Only negative numbers', 'Only numbers equal to zero'], 0),
   ('Why might engineers historically have used continued fraction approximations?', ['To find simple, accurate fractions to represent irrational measurements', 'Continued fractions have no real-world engineering use', 'They always produce completely inaccurate results', 'They can only represent whole numbers'], 0),
   ('A key property of continued fractions is that they can represent numbers with ___.', ['Increasing levels of precision as more terms are added', 'A fixed, unchangeable level of precision only', 'No connection to the actual value being approximated', 'Only integer values with no fractions involved'], 0)]),
E('Reading: Analyzing Circular and Non-Linear Structure',
  'Grade 10 English strand: a circular or non-linear narrative structure disrupts standard chronological order, moving between past, present, or multiple perspectives to create suspense, reveal information strategically, or mirror a characters state of mind.',
  [('What does a non-linear narrative structure do?', ['Disrupts standard chronological order in storytelling', 'Always follows events in perfect chronological order', 'Removes the need for any structure at all', 'Uses only dialogue with no narration'], 0),
   ('What might a circular narrative structure do at the end of a story?', ['Return to an idea, image, or scene from the beginning', 'Never reference the beginning of the story at all', 'End with no connection to any earlier part of the story', 'Remove the ending entirely'], 0),
   ('Why might an author use a non-linear structure?', ['To create suspense or strategically reveal information', 'To make the story completely impossible to follow with no purpose', 'Non-linear structures are never used in effective storytelling', 'To remove all meaning from the plot'], 0),
   ('A non-linear structure might move between which of the following?', ['Past, present, and multiple perspectives', 'Only a single unchanging moment in time', 'Only numbers and equations', 'Only unrelated grammar rules'], 0),
   ('How can a non-linear structure mirror a characters state of mind?', ['By reflecting memory, trauma, or confusion through disordered storytelling', 'It can never reflect a characters internal state', 'It always simplifies a characters emotions', 'It removes the character from the story entirely'], 0)]),
Sc('Desert Ecosystems and Adaptations',
   'Grade 10 Science strand: desert ecosystems receive very little precipitation, and the plants and animals that live there have evolved specialized adaptations, such as water storage and nocturnal behaviour, to survive extreme conditions.',
   [('What defines a desert ecosystem?', ['Very little precipitation', 'Extremely high precipitation', 'Constant freezing temperatures only', 'No sunlight at all'], 0),
    ('What is one adaptation desert plants often have?', ['The ability to store water', 'The need for constant flooding', 'A requirement for extremely cold temperatures', 'An inability to survive any sunlight'], 0),
    ('Why might many desert animals be nocturnal?', ['To avoid the extreme heat of the day', 'Nocturnal behaviour has no survival advantage', 'To avoid finding food entirely', 'Because deserts have no daytime at all'], 0),
    ('Which of these is a well-known desert plant adaptation?', ['A cactuss thick, water-storing stem', 'A water lilys floating leaves', 'A pine trees needle-shaped leaves for cold climates', 'A palm trees tolerance for constant rain'], 0),
    ('Desert ecosystems can be found on which types of land?', ['Both hot and cold regions with low precipitation', 'Only underwater locations', 'Only areas with constant rainfall', 'Only areas near the equator'], 0)]),
H('Clifford Sifton and the Settlement of the Canadian Prairies',
  'Grade 10 History strand: as Minister of the Interior in the early 1900s, Clifford Sifton led an aggressive immigration campaign to settle the Canadian Prairies, dramatically increasing the regions population and agricultural output.',
  [('What government position did Clifford Sifton hold?', ['Minister of the Interior', 'Prime Minister', 'Governor General', 'Minister of Defence'], 0),
   ('What was Clifford Siftons main policy goal?', ['To attract immigrants to settle the Canadian Prairies', 'To close Canadas borders to all immigration', 'To reduce agricultural production in Canada', 'To build a new national railway from scratch'], 0),
   ('What effect did Siftons immigration campaign have on the Prairies?', ['It dramatically increased population and agricultural output', 'It caused the Prairies to become completely uninhabited', 'It had no effect on the regions population', 'It ended all farming in the region'], 0),
   ('Roughly when was Clifford Sifton active in this role?', ['In the early 1900s', 'In the 1990s', 'In the 1700s', 'After World War II'], 0),
   ('Siftons policies are often studied as part of a larger effort to ___.', ['Encourage settlement and economic development in Western Canada', 'Prevent any settlement of Western Canada', 'Isolate the Prairies from the rest of Canada', 'Discourage all immigration to Canada'], 0)]),
]),
day(120, [
E('English Review: Grammar, Vocabulary, and Reading Analysis',
  'Grade 10 English strand review: students revisit ellipsis, juxtaposition, letters of apology, memes, emphatic pronouns, foil characters, monologues, and round vs flat characters.',
  [('What does an ellipsis indicate when used in a direct quotation?', ['That words have been omitted from the original text', 'That the entire quotation is false', 'That the sentence has ended with a question', 'That the writer disagrees with the quotation'], 0),
   ('What is juxtaposition?', ['Placing two contrasting elements side by side', 'Combining two similar ideas into one', 'A type of punctuation mark', 'A grammar rule for verb tense'], 0),
   ('What is a foil character?', ['A character whose traits contrast with a main character to highlight them', 'A character identical to the main character', 'A character who never appears in the story', 'A type of narrator'], 0),
   ('What is a monologue?', ['An extended speech by a single character', 'A conversation between two or more characters', 'A short list of stage directions', 'A type of grammar rule'], 0),
   ('What defines a round character?', ['A complex, multidimensional character capable of change', 'A character with no personality traits at all', 'A character who never appears in the story', 'A character defined only by their physical appearance'], 0)]),
M('Math Review: Limits, Complex Numbers, and Advanced Concepts',
  'Grade 10 Math strand review: students revisit limits, the unit circle, De Moivres Theorem, parametric equations, the Fundamental Theorem of Algebra, continued fractions, graph theory, and the Central Limit Theorem.',
  [('What does a limit describe in mathematics?', ['The value a function approaches as its input gets closer to a certain number', 'The exact value of a function at every point', 'A fixed number that never changes', 'The total area under a curve only'], 0),
   ('What does De Moivres Theorem help calculate?', ['A complex number in polar form raised to a power', 'The area of a triangle', 'The slope of a line', 'The volume of a sphere'], 0),
   ('What does the Fundamental Theorem of Algebra state?', ['A polynomial of degree n has exactly n roots, counting complex and repeated roots', 'A polynomial always has zero roots', 'Only linear equations have any roots', 'Polynomials never have complex roots'], 0),
   ('What are the two basic components of a graph in graph theory?', ['Nodes (vertices) and edges', 'Only numbers', 'Only angles', 'Only fractions'], 0),
   ('What does the Central Limit Theorem describe?', ['How the distribution of sample means becomes approximately normal as sample size grows', 'A rule that applies only to whole numbers', 'A theorem about the area of circles', 'A method for factoring polynomials'], 0)]),
Sc('Science Review: Senses, Chemistry, and Earth Science',
   'Grade 10 Science strand review: students revisit the human eye and ear, antibiotic resistance, colloids and emulsions, comets/meteors/asteroids, roller coaster physics, bird migration, the excretory system, and desert ecosystems.',
   [('What structure in the eye focuses light onto the retina?', ['The lens', 'The eardrum', 'The trachea', 'The epidermis'], 0),
    ('What structure vibrates when sound waves first enter the ear?', ['The eardrum', 'The cochlea alone', 'The optic nerve', 'The retina'], 0),
    ('What is an emulsion?', ['A colloid formed from two liquids that would not normally mix', 'A solid dissolved completely in water', 'A single pure liquid with no mixture', 'A gas dissolved in a solid'], 0),
    ('What is a meteor?', ['A small piece of debris burning up as it enters a planets atmosphere', 'A fully formed planet', 'A type of star', 'A permanent moon of Earth'], 0),
    ('Which organs are the primary filters in the excretory system?', ['The kidneys', 'The lungs', 'The liver only', 'The heart'], 0)]),
H('History Review: Canadian Autonomy and Modern Land Claims',
  'Grade 10 History strand review: students revisit Newfoundlands entry into Confederation, the Balfour Declaration, the Naval Service Act, the Commonwealth Air Training Plan, the St. Lawrence Seaway, the Alaska Boundary Dispute, the Sixties Scoop, the Nisgaa Treaty, and Clifford Sifton.',
  [('In what year did Newfoundland join Confederation?', ['1949', '1867', '1905', '1999'], 0),
   ('What did the Balfour Declaration of 1926 recognize about Canada?', ['That Canada was equal in status to Britain', 'That Canada was a colony with no rights', 'That Canada should be governed entirely by Britain', 'That Canada had no relationship with Britain at all'], 0),
   ('What did the Naval Service Act of 1910 establish?', ['The Royal Canadian Navy', 'The Royal Canadian Air Force', 'The Canadian Army', 'A national police force'], 0),
   ('What was the Sixties Scoop?', ['The mass removal of Indigenous children into non-Indigenous foster or adoptive homes', 'A government program to build new schools', 'A trade agreement between Canada and other countries', 'A celebration of Indigenous culture'], 0),
   ('What government position did Clifford Sifton hold?', ['Minister of the Interior', 'Prime Minister', 'Governor General', 'Minister of Defence'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_111_120)
    append_to(10, g10_111_120)
