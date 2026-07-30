#!/usr/bin/env python3
"""Grade 9, Days 111-120 -- extends Grade 9 from 110 to 120 days. Topics
chosen after grepping the existing Day 1-110 title list (data/grade9.json)
extensively to avoid any overlap: cumulative and periodic sentences,
portmanteau words, anaphora and repetition, PSA scripts, native
advertising, the four sentence types, anti-heroes, letters of
recommendation, round and flat characters; the binomial theorem, the unit
circle, complex numbers, the remainder and factor theorems, an
introduction to the derivative, conic sections (ellipses/hyperbolas), the
Fibonacci sequence and golden ratio, parametric equations, geometric
probability; the human eye, the human ear, antibiotic resistance,
symbiosis, robotics and mechatronics, forensic science, materials science
(polymers/composites), AI and machine learning, sustainable agriculture;
small island developing states, e-waste and electronic recycling, the gig
economy and ride-sharing, the Silk Road, coffee and cocoa production,
urban parks and green space, global shipping ports and freight, the
Panama and Suez Canals, and wildlife corridors/habitat fragmentation.

Subject keys for Grade 9 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 9 batches); SocialStudies
content is Geography-focused, matching the existing convention.

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L9 = 'https://tvolearn.com/pages/grade-9-english'
M9 = 'https://tvolearn.com/pages/grade-9-mathematics'
S9 = 'https://tvolearn.com/pages/grade-9-science'
SS9 = 'https://tvolearn.com/pages/grade-9-geography'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 9 English',
    'TVO Learn: Grade 9 Mathematics',
    'TVO Learn: Grade 9 Science',
    'TVO Learn: Grade 9 Geography',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L9, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M9, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S9, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS9, q)


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


g9_111_120 = [
day(111, [
L('Grammar: Cumulative and Periodic Sentences',
  'Grade 9 Language strand: a cumulative sentence starts with the main idea and adds details afterward, while a periodic sentence delays the main idea until the very end, creating suspense or emphasis.',
  [('What is a cumulative sentence?', ['A sentence that starts with the main idea and adds details afterward', 'A sentence with no main idea at all', 'A sentence that always begins with a question', 'A sentence with only one word'], 0),
   ('What is a periodic sentence?', ['A sentence that delays the main idea until the very end', 'A sentence that repeats the same word many times', 'A sentence with no punctuation', 'A sentence that is always short'], 0),
   ('What effect can a periodic sentence create?', ['Suspense or emphasis by delaying the key point', 'Immediate clarity with no build-up', 'Confusion with no clear purpose', 'A complete lack of meaning'], 0),
   ('Which is an example of a periodic sentence?', ['After years of preparation, countless sacrifices, and endless practice, she finally won.', 'She won after years of preparation.', 'She won.', 'Years passed and she won eventually, somehow, finally.'], 0),
   ('Why might a writer choose a cumulative sentence structure?', ['To state the main idea clearly before elaborating with details', 'To hide the main idea entirely', 'To avoid using any details', 'To make the sentence ungrammatical'], 0)]),
M('Algebra: An Introduction to the Binomial Theorem',
  'Grade 9 Math strand: the Binomial Theorem provides a formula for expanding expressions of the form (a+b)^n without multiplying repeatedly, using coefficients from Pascals Triangle.',
  [('What does the Binomial Theorem help you do?', ['Expand expressions of the form (a+b)^n without multiplying repeatedly', 'Solve any linear equation instantly', 'Find the area of a circle', 'Simplify fractions only'], 0),
   ('What structure provides the coefficients used in the Binomial Theorem?', ['Pascals Triangle', 'A number line', 'A Venn diagram', 'A coordinate plane'], 0),
   ('Using the Binomial Theorem, what is the expansion of (a+b)^2?', ['a^2 + 2ab + b^2', 'a^2 + b^2', 'a + b', '2a + 2b'], 0),
   ('As the exponent n increases, what happens to the number of terms in the expansion of (a+b)^n?', ['It increases, with n+1 terms total', 'It always stays at exactly two terms', 'It decreases to zero', 'It becomes undefined'], 0),
   ('The Binomial Theorem is especially useful when expanding expressions with ___.', ['Large exponents that would be tedious to multiply out by hand', 'Only an exponent of zero', 'No variables at all', 'Only single numbers with no addition'], 0)]),
Sc('The Human Eye and the Physics of Vision',
   'Grade 9 Science strand: the eye uses a lens to focus light onto the retina, where light-sensitive cells convert it into electrical signals that the brain interprets as images.',
   [('What structure in the eye focuses light onto the retina?', ['The lens', 'The eardrum', 'The trachea', 'The epidermis'], 0),
    ('What does the retina contain that responds to light?', ['Light-sensitive cells', 'Muscle fibres only', 'Digestive enzymes', 'Bone tissue'], 0),
    ('How does the brain use signals from the retina?', ['It interprets them to form images we perceive as vision', 'It converts them into sound', 'It ignores them completely', 'It uses them only to regulate heart rate'], 0),
    ('Why might a persons vision be blurry if their eyes lens does not focus light correctly?', ['Light does not converge properly on the retina', 'The retina has too much light-sensitive tissue', 'The eye produces no light at all', 'The brain refuses to process any images'], 0),
    ('The study of how light interacts with the eye is an example of ___.', ['Applied physics (optics)', 'Pure chemistry with no physics', 'Astronomy', 'Geology'], 0)]),
SS('Social Studies: The Geography of Small Island Developing States',
   'Grade 9 Social Studies (Geography) strand: Small Island Developing States, or SIDS, face unique geographic challenges such as vulnerability to sea level rise, limited land area, and reliance on imports and tourism.',
   [('What does SIDS stand for?', ['Small Island Developing States', 'Southern International Development Sector', 'Sustainable Island Data System', 'Sea Ice Distribution Study'], 0),
    ('What is one major geographic challenge facing many small island states?', ['Vulnerability to sea level rise', 'Unlimited available land', 'No connection to the ocean at all', 'Excessive freshwater resources with no scarcity'], 0),
    ('Why might small island states rely heavily on imports?', ['Their limited land area restricts local production of many goods', 'They produce far more than they could ever use', 'Imports are banned in these regions', 'They have no need for any resources'], 0),
    ('What economic sector is often especially important to small island states?', ['Tourism', 'Heavy manufacturing', 'Large-scale mining', 'Deep-sea oil drilling only'], 0),
    ('Why do small island states often advocate strongly for climate action?', ['They are especially vulnerable to the effects of rising sea levels', 'Climate change has no effect on islands', 'They are the least affected regions in the world', 'They have unlimited resources to adapt'], 0)]),
]),
day(112, [
L('Vocabulary: Portmanteau Words and Blends',
  'Grade 9 Language strand: a portmanteau word blends the sounds and meanings of two existing words into a new one, such as motel (motor plus hotel), reflecting how language evolves to describe new ideas.',
  [('What is a portmanteau word?', ['A word that blends the sounds and meanings of two existing words', 'A word borrowed directly from another language unchanged', 'A word with no meaning at all', 'A type of punctuation mark'], 0),
   ('Which of these is a portmanteau word?', ['Motel', 'Table', 'Quickly', 'Happiness'], 0),
   ('The word motel is a blend of which two words?', ['Motor and hotel', 'Move and travel', 'Mode and tell', 'Motion and tell'], 0),
   ('Why do portmanteau words continue to appear in modern language?', ['They efficiently describe new concepts by combining familiar words', 'New words are never created in modern language', 'Portmanteau words are always considered incorrect', 'They replace the need for all other vocabulary'], 0),
   ('Which is a modern example of a portmanteau word?', ['Podcast (iPod plus broadcast)', 'Table', 'Run', 'Blue'], 0)]),
M('Trigonometry: An Introduction to the Unit Circle',
  'Grade 9 Math strand: the unit circle is a circle with radius 1 centred at the origin, used to define sine and cosine values for any angle and connect trigonometry to coordinate geometry.',
  [('What is the radius of the unit circle?', ['1', '0', '2', 'It has no fixed radius'], 0),
   ('Where is the unit circle centred?', ['At the origin (0, 0)', 'At the point (1, 1)', 'At the point (5, 5)', 'It has no defined centre'], 0),
   ('What two trigonometric values can be defined using coordinates on the unit circle?', ['Sine and cosine', 'Only the radius and diameter', 'Only the area and circumference', 'Only the slope and y-intercept'], 0),
   ('What is the significance of the unit circle in trigonometry?', ['It provides a way to define sine and cosine for any angle', 'It only works for angles less than 90 degrees', 'It replaces the need for angles entirely', 'It cannot be used for any calculations'], 0),
   ('The unit circle helps connect which two branches of mathematics?', ['Trigonometry and coordinate geometry', 'Only arithmetic and probability', 'Only statistics and data management', 'Only geometry and financial literacy'], 0)]),
Sc('The Human Ear and the Physics of Hearing',
   'Grade 9 Science strand: the ear captures sound waves and converts their vibrations into electrical signals through structures like the eardrum and cochlea, which the brain then interprets as sound.',
   [('What does the ear capture and convert into signals?', ['Sound waves', 'Light waves', 'Chemical signals', 'Magnetic fields'], 0),
    ('What structure vibrates when sound waves first enter the ear?', ['The eardrum', 'The cochlea alone', 'The optic nerve', 'The retina'], 0),
    ('What part of the inner ear helps convert vibrations into electrical signals?', ['The cochlea', 'The pupil', 'The trachea', 'The epidermis'], 0),
    ('How does the brain use the electrical signals sent from the ear?', ['It interprets them as sound', 'It ignores them completely', 'It converts them into images', 'It uses them only to control digestion'], 0),
    ('Studying the physics of sound and hearing connects biology to which field of physics?', ['Acoustics (the study of sound)', 'Optics (the study of light)', 'Thermodynamics (the study of heat)', 'Astronomy (the study of space)'], 0)]),
SS('Social Studies: The Geography of E-Waste and Electronic Recycling',
   'Grade 9 Social Studies (Geography) strand: e-waste refers to discarded electronic devices, and its global geography involves complex patterns of disposal, recycling, and shipment, often from wealthier nations to developing regions.',
   [('What is e-waste?', ['Discarded electronic devices', 'Waste generated only from farming', 'Waste produced solely by factories', 'A type of renewable energy source'], 0),
    ('What is a common geographic pattern in the disposal of e-waste?', ['It is often shipped from wealthier nations to developing regions', 'It never crosses any international borders', 'It is always processed in the same country it was produced', 'It is banned from being shipped anywhere'], 0),
    ('Why is e-waste recycling geographically and environmentally significant?', ['Improper disposal can release harmful materials into the environment', 'E-waste has no environmental impact at all', 'E-waste always disappears naturally with no processing needed', 'Recycling e-waste has no benefits'], 0),
    ('What materials can sometimes be recovered from recycling e-waste?', ['Valuable metals like gold and copper', 'Only worthless materials with no value', 'Only water', 'Only wood'], 0),
    ('Why might developing regions receive large amounts of e-waste for processing?', ['Lower labour and regulatory costs make processing cheaper there', 'These regions produce the most e-waste themselves', 'E-waste cannot be processed in developed nations at all', 'International law requires it to be sent there'], 0)]),
]),
day(113, [
L('Reading: Analyzing Anaphora and Repetition for Effect',
  'Grade 9 Language strand: anaphora repeats a word or phrase at the beginning of successive clauses or sentences, building rhythm and emphasis, as seen in many famous speeches.',
  [('What is anaphora?', ['The repetition of a word or phrase at the beginning of successive clauses', 'A word that imitates a sound', 'A punctuation mark used in dialogue', 'A citation format for essays'], 0),
   ('What effect does anaphora typically create?', ['Rhythm and emphasis', 'Confusion with no clear pattern', 'A complete lack of structure', 'An immediate end to the sentence'], 0),
   ('Which is an example of anaphora?', ['We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields.', 'The dog ran quickly through the park.', 'She opened the door slowly.', 'They finished their homework before dinner.'], 0),
   ('Where is anaphora commonly used for persuasive effect?', ['In famous speeches and persuasive writing', 'Only in technical manuals', 'Only in grocery lists', 'Only in mathematical proofs'], 0),
   ('Why might a speaker use repetition like anaphora?', ['To reinforce a key idea and make it memorable', 'To confuse the audience intentionally', 'To avoid making any clear point', 'To remove all emotional impact from a speech'], 0)]),
M('Algebra: An Introduction to Complex Numbers',
  'Grade 9 Math strand: a complex number combines a real part and an imaginary part, written as a+bi, where i represents the square root of negative one, extending the number system beyond real numbers.',
  [('What is a complex number?', ['A number combining a real part and an imaginary part', 'Only a whole number', 'Only a negative number', 'A number with no value'], 0),
   ('What does the symbol i represent in a complex number?', ['The square root of negative one', 'The number ten', 'A type of fraction', 'A geometric shape'], 0),
   ('How is a complex number typically written?', ['a + bi', 'a - b', 'a times b', 'a divided by b'], 0),
   ('Why were complex numbers introduced into mathematics?', ['To allow solutions to equations that have no real number solutions', 'To eliminate the need for real numbers entirely', 'To replace fractions completely', 'They serve no mathematical purpose'], 0),
   ('Complex numbers extend the real number system to include ___.', ['Square roots of negative numbers', 'Only positive whole numbers', 'Only numbers between zero and one', 'Nothing beyond whole numbers'], 0)]),
Sc('Antibiotic Resistance: A Modern Challenge',
   'Grade 9 Science strand: antibiotic resistance occurs when bacteria evolve mechanisms to survive medicines designed to kill them, a growing global health concern driven by overuse and misuse of antibiotics.',
   [('What is antibiotic resistance?', ['When bacteria evolve to survive medicines designed to kill them', 'When a medicine becomes stronger the more it is used', 'When a virus becomes weaker over time', 'When bacteria disappear completely from the body'], 0),
    ('What is a major driver of increasing antibiotic resistance?', ['Overuse and misuse of antibiotics', 'Using antibiotics too rarely', 'Regular vaccination', 'Eating a balanced diet'], 0),
    ('Why is antibiotic resistance a significant global health concern?', ['It makes some bacterial infections much harder to treat effectively', 'It has no impact on human health', 'It only affects a single country', 'It makes all infections easier to cure'], 0),
    ('What can reduce the development of antibiotic resistance?', ['Using antibiotics only when prescribed and completing the full course', 'Taking antibiotics for every illness, including viral infections', 'Sharing leftover antibiotics with others', 'Stopping antibiotics as soon as symptoms improve'], 0),
    ('Antibiotic resistance is a direct example of which biological process?', ['Natural selection acting on bacterial populations', 'A process unrelated to evolution', 'A process that only affects viruses', 'A permanently fixed trait with no change over time'], 0)]),
SS('Social Studies: The Geography of the Gig Economy and Ride-Sharing',
   'Grade 9 Social Studies (Geography) strand: the gig economy, including ride-sharing services, has reshaped urban transportation geography by relying on flexible, app-based labour and reshaping how people move through cities.',
   [('What is the gig economy?', ['A labour market characterized by flexible, short-term, often app-based work', 'A traditional economy based only on permanent full-time jobs', 'An economy with no workers at all', 'A type of government-run employment program'], 0),
    ('How have ride-sharing services affected urban transportation geography?', ['They have reshaped how people move through and access cities', 'They have had no effect on urban transportation at all', 'They eliminated the need for any roads', 'They only operate in rural farmland'], 0),
    ('What technology enables the modern gig economy, like ride-sharing?', ['Smartphone apps connecting workers and customers', 'Only landline telephones', 'Only printed newspapers', 'Only physical mail'], 0),
    ('What is one geographic critique of ride-sharing services in cities?', ['They can increase traffic congestion in certain areas', 'They always eliminate all traffic everywhere', 'They have no effect on city streets', 'They only operate in areas with no roads'], 0),
    ('The rise of the gig economy reflects broader changes in ___.', ['How and where people work in a digital, connected world', 'A return to entirely agricultural economies', 'The complete elimination of all cities', 'A rejection of all technology'], 0)]),
]),
day(114, [
L('Writing: Writing a Public Service Announcement (PSA) Script',
  'Grade 9 Language strand: a public service announcement script delivers an important message to a wide audience concisely, using persuasive and clear language to encourage a specific action or awareness.',
  [('What is the purpose of a public service announcement?', ['To deliver an important message to a wide audience', 'To sell a specific product for profit', 'To entertain with no informative purpose', 'To confuse the audience intentionally'], 0),
   ('What kind of language does a PSA script typically use?', ['Persuasive and clear language', 'Extremely technical jargon only', 'Language with no clear purpose', 'Language designed to confuse listeners'], 0),
   ('Why must a PSA script be concise?', ['To effectively deliver the message within a short time frame', 'PSAs are always extremely long with no time limit', 'Length does not matter in a PSA', 'Concise writing is never valued in media'], 0),
   ('What is a common goal of a PSA?', ['Encouraging a specific action or raising awareness', 'Avoiding any call to action', 'Selling a specific brand of product', 'Providing only entertainment with no message'], 0),
   ('Which is an example of an effective PSA closing line?', ['Buckle up — it only takes a second to save a life.', 'This message means nothing.', 'No action is needed from anyone.', 'This has no purpose at all.'], 0)]),
M('Algebra: The Remainder Theorem and Factor Theorem',
  'Grade 9 Math strand: the Remainder Theorem states that dividing a polynomial by (x-a) gives a remainder equal to the polynomial evaluated at a, and the Factor Theorem uses this to determine whether (x-a) is a factor.',
  [('What does the Remainder Theorem state?', ['Dividing a polynomial by (x-a) gives a remainder equal to the polynomial evaluated at a', 'Every polynomial has no remainder when divided', 'Polynomials cannot be divided by binomials', 'The remainder is always zero for every polynomial'], 0),
   ('According to the Factor Theorem, when is (x-a) a factor of a polynomial?', ['When the polynomial evaluated at a equals zero', 'When the polynomial evaluated at a equals one', 'Only when a is a negative number', 'Factors cannot be determined this way'], 0),
   ('If P(3) = 0 for a polynomial P(x), what can you conclude?', ['(x-3) is a factor of P(x)', '(x+3) is a factor of P(x)', 'P(x) has no factors at all', 'P(x) is undefined'], 0),
   ('Why are the Remainder and Factor Theorems useful?', ['They provide a quicker way to test for factors without full division', 'They eliminate the need to ever factor a polynomial', 'They only work for linear equations, never polynomials', 'They have no practical mathematical use'], 0),
   ('The Remainder Theorem connects division of polynomials to ___.', ['Evaluating the polynomial at a specific value', 'Only graphing linear equations', 'Only simplifying fractions', 'Only measuring angles'], 0)]),
Sc('Symbiosis: Mutualism, Commensalism, and Parasitism',
   'Grade 9 Science strand: symbiosis describes close, long-term relationships between different species, classified as mutualism (both benefit), commensalism (one benefits, one is unaffected), or parasitism (one benefits, one is harmed).',
   [('What is symbiosis?', ['A close, long-term relationship between different species', 'A relationship that only occurs within a single species', 'A type of chemical reaction', 'A process only found in plants'], 0),
    ('In mutualism, how are both species affected?', ['Both species benefit', 'One benefits while the other is harmed', 'Neither species is affected at all', 'Both species are harmed'], 0),
    ('What defines commensalism?', ['One species benefits while the other is unaffected', 'Both species benefit equally', 'Both species are harmed equally', 'One species is destroyed completely'], 0),
    ('What defines parasitism?', ['One species benefits while the other is harmed', 'Both species benefit equally', 'Neither species is affected', 'Both species disappear'], 0),
    ('Which is an example of a mutualistic relationship?', ['Bees pollinating flowers while gaining nectar', 'A tapeworm living inside and harming a host animal', 'Barnacles attaching to a whale with no effect on the whale', 'A shark and a fish with no interaction at all'], 0)]),
SS('Social Studies: The Geography of the Silk Road',
   'Grade 9 Social Studies (Geography) strand: the Silk Road was a historic network of trade routes connecting Asia, the Middle East, and Europe, shaping the geography of trade, culture, and the spread of ideas for centuries.',
   [('What was the Silk Road?', ['A historic network of trade routes connecting Asia, the Middle East, and Europe', 'A single modern highway system', 'A type of railway built in the 20th century', 'A shipping canal in South America'], 0),
    ('What did the Silk Road primarily enable, besides the trade of goods?', ['The spread of ideas and cultural exchange', 'The complete isolation of connected regions', 'The prevention of any cultural contact', 'The end of all international trade'], 0),
    ('Which goods were commonly traded along the Silk Road?', ['Silk, spices, and other valuable goods', 'Only modern electronics', 'Only oil and natural gas', 'Only automobiles'], 0),
    ('How did the geography of the Silk Road influence the growth of certain cities?', ['Cities along the route grew as important trading hubs', 'Geography had no effect on any cities along the route', 'All cities along the route disappeared entirely', 'The Silk Road avoided all cities completely'], 0),
    ('Why do geographers and historians still study the Silk Road today?', ['It illustrates how trade routes shape culture, economies, and history', 'It has no relevance to modern geography', 'It was purely a modern invention', 'No trade ever occurred along this route'], 0)]),
]),
day(115, [
L('Media Literacy: Analyzing Native Advertising and Sponsored Content',
  'Grade 9 Language strand: native advertising and sponsored content are designed to blend in with regular articles or posts, so critical readers must learn to identify when content is actually paid promotion.',
  [('What is native advertising?', ['Paid content designed to blend in with regular articles or posts', 'Content that is always clearly labeled as an advertisement in bold letters', 'A type of grammar rule', 'A form of punctuation'], 0),
   ('Why can native advertising be difficult to identify?', ['It is designed to look like regular editorial content', 'It always appears in a completely different format from articles', 'It is required by law to be clearly marked in giant red text', 'It never appears near real articles'], 0),
   ('What skill helps readers identify sponsored content?', ['Media literacy and critical reading', 'Ignoring all content on a webpage', 'Reading only headlines and nothing else', 'Believing all content is equally trustworthy'], 0),
   ('Why do companies use native advertising?', ['To promote products in a way that feels less like a traditional ad', 'To ensure their content is entirely and obviously an advertisement', 'Because they are legally required to disguise their promotions', 'To avoid attracting any customers'], 0),
   ('What should readers look for to identify sponsored content?', ['Small labels like Sponsored or Paid Content near the article', 'Nothing, since sponsored content cannot be identified', 'Only the length of the article', 'Only the colour of the website'], 0)]),
M('Geometry: An Introduction to Conic Sections — Ellipses and Hyperbolas',
  'Grade 9 Math strand: conic sections are curves formed by slicing a cone at different angles, including circles, ellipses, parabolas, and hyperbolas, each with distinct equations and real-world applications.',
  [('What are conic sections?', ['Curves formed by slicing a cone at different angles', 'A type of algebraic expression only', 'A type of matrix', 'A method for solving linear equations'], 0),
   ('Which of these is a type of conic section?', ['An ellipse', 'A trapezoid', 'A rhombus', 'A pentagon'], 0),
   ('What shape does an ellipse resemble?', ['A stretched or elongated circle', 'A perfect square', 'A straight line', 'A triangle'], 0),
   ('What distinguishes a hyperbola from an ellipse?', ['A hyperbola consists of two separate curves that open away from each other', 'A hyperbola is always a closed shape like a circle', 'A hyperbola has no equation at all', 'A hyperbola is identical to a straight line'], 0),
   ('Conic sections have real-world applications in fields such as ___.', ['Astronomy, describing the orbits of planets', 'Only cooking and recipes', 'Only music composition', 'Only language arts'], 0)]),
Sc('Robotics and Mechatronics: An Introduction',
   'Grade 9 Science strand: mechatronics combines mechanical engineering, electronics, and computer science to design robots and automated systems that sense, process information, and act on their environment.',
   [('What fields does mechatronics combine?', ['Mechanical engineering, electronics, and computer science', 'Only biology and chemistry', 'Only astronomy and geology', 'Only art and music'], 0),
    ('What are three basic capabilities a robot typically needs?', ['Sensing, processing information, and acting', 'Only sensing, with no other capability', 'Only acting, with no sensing or processing', 'None of these capabilities are needed'], 0),
    ('What might a sensor allow a robot to detect?', ['Light, distance, or temperature in its environment', 'Nothing at all', 'Only the robots own internal battery level', 'Only the colour of its own body'], 0),
    ('Why are robots often used in manufacturing?', ['They can perform repetitive tasks with precision and consistency', 'Robots cannot perform any physical tasks', 'Robots are always slower than humans at every task', 'Robots have no practical industrial use'], 0),
    ('Mechatronics and robotics are examples of applying science to ___.', ['Solve real-world engineering problems', 'Purely theoretical ideas with no application', 'Only artistic expression', 'Only historical research'], 0)]),
SS('Social Studies: The Geography of Coffee and Cocoa Production',
   'Grade 9 Social Studies (Geography) strand: coffee and cocoa are grown mainly in tropical regions near the equator, and their global trade connects rural farming communities to consumers around the world through complex supply chains.',
   [('In what type of climate are coffee and cocoa typically grown?', ['Tropical regions near the equator', 'Arctic and polar regions', 'Desert regions with almost no rainfall', 'Regions with permanent snow cover'], 0),
    ('What connects rural farming communities that grow coffee and cocoa to global consumers?', ['Complex international supply chains', 'No connection exists between farmers and consumers', 'Farmers only sell their crops locally with no exports', 'A single global government agency'], 0),
    ('Why might coffee and cocoa farmers sometimes receive a small share of the final product price?', ['Multiple steps in the supply chain, like processing and shipping, add costs', 'Farmers always receive the largest share of profits', 'Coffee and cocoa require no processing at all', 'These crops are given away for free'], 0),
    ('What movement aims to ensure fairer prices for coffee and cocoa farmers?', ['The Fair Trade movement', 'The Free Trade Agreement only', 'The National Policy', 'The Green Revolution only'], 0),
    ('The geography of coffee and cocoa production illustrates the connection between ___.', ['Physical climate conditions and global economic trade', 'Weather patterns and space exploration', 'Ocean currents and manufacturing', 'Urban design and mining'], 0)]),
]),
day(116, [
L('Grammar: The Four Sentence Types',
  'Grade 9 Language strand: English sentences fall into four types based on structure — simple, compound, complex, and compound-complex — each combining independent and dependent clauses differently.',
  [('What are the four sentence types based on structure?', ['Simple, compound, complex, and compound-complex', 'Only simple and complex', 'Only short and long', 'Only formal and informal'], 0),
   ('What defines a simple sentence?', ['One independent clause with a subject and verb', 'Two independent clauses joined by a comma', 'A sentence with no verb at all', 'A sentence with only dependent clauses'], 0),
   ('What defines a compound sentence?', ['Two or more independent clauses joined together', 'Only one independent clause', 'A sentence with no subject', 'A sentence with only one word'], 0),
   ('What defines a complex sentence?', ['An independent clause combined with at least one dependent clause', 'Two independent clauses with no connecting word', 'A sentence with no clauses at all', 'A sentence that must always be a question'], 0),
   ('What defines a compound-complex sentence?', ['At least two independent clauses and at least one dependent clause', 'Only one independent clause with no dependent clauses', 'A sentence with no punctuation', 'A sentence that must be exactly five words long'], 0)]),
M('Calculus Preview: An Introduction to the Derivative as a Rate of Change',
  'Grade 9 Math strand: the derivative measures the instantaneous rate of change of a function at a given point, extending the idea of slope from straight lines to curves, a foundational concept in calculus.',
  [('What does a derivative measure?', ['The instantaneous rate of change of a function at a point', 'The total area under a curve', 'A fixed value that never changes', 'Only the maximum value of a function'], 0),
   ('The concept of a derivative extends which earlier idea?', ['Slope, from straight lines to curves', 'Only the concept of area', 'Only the concept of volume', 'Only basic addition'], 0),
   ('Why is the derivative considered a foundational concept in calculus?', ['It provides a way to analyze how functions change at any given instant', 'It has no connection to any other mathematical concept', 'It only applies to whole numbers', 'It eliminates the need to study functions'], 0),
   ('If a functions derivative is positive at a point, what does this suggest?', ['The function is increasing at that point', 'The function is always decreasing everywhere', 'The function has no value at that point', 'The function is undefined everywhere'], 0),
   ('Derivatives are used in real-world contexts to analyze things like ___.', ['Velocity, which is the rate of change of position', 'Only the colour of an object', 'Only the taste of food', 'Only historical dates'], 0)]),
Sc('Forensic Science: Applying the Scientific Method to Investigation',
   'Grade 9 Science strand: forensic science applies scientific methods, such as analyzing physical evidence and following controlled procedures, to investigate crimes and answer questions in a legal context.',
   [('What does forensic science apply to investigations?', ['Scientific methods and analysis of physical evidence', 'Only guesses with no evidence', 'Only opinions with no factual basis', 'Only historical records with no science'], 0),
    ('Why is following a controlled, consistent procedure important in forensic investigations?', ['It helps ensure evidence is reliable and not contaminated', 'Procedures have no effect on the reliability of evidence', 'Consistency is never important in scientific investigation', 'Evidence never needs to be handled carefully'], 0),
    ('What type of physical evidence might a forensic scientist analyze?', ['Fingerprints or DNA samples', 'Only the weather on the day of an incident', 'Only unrelated historical documents', 'Only opinions from bystanders'], 0),
    ('Why is forensic science considered an application of the scientific method?', ['It uses observation, evidence, and testing to draw conclusions', 'It relies entirely on guesswork with no evidence', 'It never involves any scientific analysis', 'It is unrelated to any scientific principles'], 0),
    ('Forensic science is often used in which real-world context?', ['Criminal investigations and legal proceedings', 'Only cooking and recipe development', 'Only weather forecasting', 'Only space exploration'], 0)]),
SS('Social Studies: The Geography of Urban Parks and Green Space',
   'Grade 9 Social Studies (Geography) strand: urban parks and green spaces provide environmental, health, and social benefits to cities, and their distribution often reflects broader patterns of urban planning and inequality.',
   [('What are some benefits of urban parks and green spaces?', ['Environmental, health, and social benefits', 'They provide no benefits to city residents', 'They only exist to take up unused land', 'They are always harmful to city environments'], 0),
    ('How can the distribution of green space in a city reflect inequality?', ['Wealthier neighbourhoods may have significantly more access to green space than others', 'Green space is always distributed perfectly equally in every city', 'Green space has no connection to social or economic factors', 'Every neighbourhood in every city has identical access to parks'], 0),
    ('What environmental benefit can urban green spaces provide?', ['Helping reduce urban heat and improve air quality', 'Increasing pollution levels significantly', 'Eliminating all wildlife from a city', 'Raising city temperatures dramatically'], 0),
    ('What health benefit might urban parks offer city residents?', ['Opportunities for physical activity and mental well-being', 'No health benefits whatsoever', 'Only benefits for professional athletes', 'Increased risk of illness with no benefit'], 0),
    ('Urban planners often consider green space access when addressing ___.', ['Equity and quality of life across different neighbourhoods', 'Only the design of highways', 'Only the construction of skyscrapers', 'Only industrial zoning with no residential concerns'], 0)]),
]),
day(117, [
L('Reading: Analyzing Anti-Heroes in Literature',
  'Grade 9 Language strand: an anti-hero is a main character who lacks traditional heroic qualities, such as moral clarity or bravery, yet still drives the story forward and often earns the readers sympathy.',
  [('What is an anti-hero?', ['A main character who lacks traditional heroic qualities', 'A character with no flaws whatsoever', 'A minor character with no role in the plot', 'A villain who never appears in the story'], 0),
   ('Which trait might an anti-hero commonly lack compared to a traditional hero?', ['Clear moral certainty or conventional bravery', 'A name in the story', 'Any dialogue at all', 'A physical appearance'], 0),
   ('Why might readers still sympathize with an anti-hero?', ['Their flaws and struggles can feel relatable and human', 'Anti-heroes are always portrayed as perfect and flawless', 'Readers never form any connection to anti-heroes', 'Anti-heroes never have any relatable qualities'], 0),
   ('Which is an example of an anti-hero-type character?', ['A morally complicated character who breaks rules but has understandable motives', 'A perfectly virtuous character with no flaws', 'A character who never takes any action', 'A character who exists only in the background with no development'], 0),
   ('Why might authors choose to write an anti-hero as a protagonist?', ['To explore complex, realistic themes of morality and human nature', 'To avoid creating any conflict in the story', 'Anti-heroes cannot serve as protagonists', 'To remove all character development from the story'], 0)]),
M('Number Patterns: The Fibonacci Sequence and the Golden Ratio',
  'Grade 9 Math strand: the Fibonacci sequence is formed by adding the two previous numbers to get the next, and the ratio between consecutive terms approaches the golden ratio, a number that appears throughout nature and art.',
  [('How is each new number in the Fibonacci sequence generated?', ['By adding the two previous numbers together', 'By multiplying the previous number by two', 'By subtracting one from the previous number', 'By squaring the previous number'], 0),
   ('What are the first several numbers of the Fibonacci sequence?', ['0, 1, 1, 2, 3, 5, 8...', '1, 2, 3, 4, 5, 6...', '2, 4, 6, 8, 10...', '1, 10, 100, 1000...'], 0),
   ('What value does the ratio between consecutive Fibonacci numbers approach?', ['The golden ratio', 'Zero', 'Negative one', 'A number that changes randomly each time'], 0),
   ('Where does the golden ratio commonly appear in the real world?', ['In patterns found in nature and art, like flower petals and shell spirals', 'It never appears anywhere in nature', 'Only in man-made machines', 'Only in randomly generated numbers'], 0),
   ('Why do mathematicians find the Fibonacci sequence interesting?', ['It reveals surprising connections between simple patterns and complex natural forms', 'It has no real mathematical significance', 'It only applies to a single unrelated equation', 'It was discovered only very recently with no historical value'], 0)]),
Sc('Materials Science: Polymers and Composites',
   'Grade 9 Science strand: polymers are large molecules made of repeating units, and composites combine two or more materials to create a substance with properties better than either material alone.',
   [('What is a polymer?', ['A large molecule made of repeating units', 'A single, indivisible atom', 'A type of pure element', 'A liquid with no molecular structure'], 0),
    ('What is a composite material?', ['A material made by combining two or more different materials', 'A material made of only one pure substance', 'A material with no physical properties at all', 'A gas with no solid components'], 0),
    ('Why might engineers use a composite material instead of a single material?', ['To combine the best properties of each material used', 'Composites always perform worse than a single material', 'Composites cannot be manufactured', 'Composites have no practical applications'], 0),
    ('Which of these is an example of a common polymer?', ['Plastic', 'Pure gold', 'Pure oxygen gas', 'Granite rock'], 0),
    ('Materials science, including the study of polymers and composites, is important for developing ___.', ['Stronger, lighter, and more efficient materials for engineering', 'Only materials with no practical use', 'Materials that never interact with the environment', 'Materials with no measurable properties'], 0)]),
SS('Social Studies: The Geography of Global Shipping Ports and Freight',
   'Grade 9 Social Studies (Geography) strand: major shipping ports are strategically located to connect global trade routes, moving the vast majority of the worlds freight and shaping the economic geography of coastal regions.',
   [('What role do major shipping ports play in global trade?', ['They connect global trade routes and move most of the worlds freight', 'They have no connection to international trade', 'They only handle local, small-scale trade', 'They exclusively transport passengers, never goods'], 0),
    ('Why are shipping ports often located along coastlines?', ['To provide direct access for large cargo ships', 'Coastlines have no advantage for shipping', 'Ports are never located near water', 'Coastal access makes shipping impossible'], 0),
    ('How can a major port affect the economic geography of a region?', ['It can drive economic growth and job creation in surrounding areas', 'Ports have no economic impact on nearby regions', 'Ports always cause economic decline wherever they are built', 'Ports only affect regions located far inland'], 0),
    ('What percentage of global trade by volume is estimated to move by sea shipping?', ['The vast majority of global trade by volume', 'Almost none of global trade', 'Only trade within a single country', 'Only trade of digital goods'], 0),
    ('Why might geographers study the location and development of shipping ports?', ['To understand patterns of global economic connectivity', 'Ports have no relevance to the study of geography', 'Shipping ports are identical everywhere with nothing to study', 'Geography only studies natural landforms, never infrastructure'], 0)]),
]),
day(118, [
L('Writing: Writing a Letter of Recommendation',
  'Grade 9 Language strand: a letter of recommendation highlights a persons strengths, skills, and achievements through specific examples, written to support their application for a job, program, or opportunity.',
  [('What is the purpose of a letter of recommendation?', ['To highlight a persons strengths and support their application', 'To criticize a person without any specific reason', 'To provide unrelated general information', 'To replace the persons own application entirely'], 0),
   ('What should a strong letter of recommendation include?', ['Specific examples of the persons skills and achievements', 'Only vague, general praise with no examples', 'No mention of the persons abilities at all', 'Only negative comments about the person'], 0),
   ('Who typically writes a letter of recommendation?', ['Someone who knows the persons work or character well, like a teacher or employer', 'A random stranger with no connection to the person', 'The person being recommended, about themselves', 'An anonymous source with no name'], 0),
   ('Why is specificity important in a letter of recommendation?', ['Specific examples make the praise more credible and convincing', 'Specific details are never useful in this type of letter', 'Vague statements are always more persuasive', 'Specificity makes the letter less believable'], 0),
   ('A letter of recommendation is often required for which of these?', ['A job application, scholarship, or academic program', 'A grocery list', 'A weather report', 'A restaurant menu'], 0)]),
M('Data Management: An Introduction to Geometric Probability',
  'Grade 9 Math strand: geometric probability calculates the likelihood of an event based on area, length, or volume rather than counting discrete outcomes, such as finding the chance a randomly thrown dart lands in a specific region.',
  [('What does geometric probability use to calculate likelihood?', ['Area, length, or volume rather than counting discrete outcomes', 'Only the number of people in a room', 'Only the colour of an object', 'Only the time of day'], 0),
   ('Which scenario is a good example of geometric probability?', ['Finding the chance a randomly thrown dart lands in a specific region of a board', 'Rolling a single six-sided die', 'Flipping a coin once', 'Choosing a card from a standard deck'], 0),
   ('If a small target region takes up 25% of a larger boards area, what is the geometric probability of landing in that region with a random hit?', ['25%', '100%', '0%', '75%'], 0),
   ('How does geometric probability differ from counting-based probability?', ['It uses continuous measurements like area instead of counting individual outcomes', 'It never involves any numbers', 'It is identical in every way to counting-based probability', 'It can only be used with whole numbers'], 0),
   ('Geometric probability problems are often visualized using ___.', ['Diagrams showing regions and their relative areas', 'Only word problems with no diagrams', 'Only historical data with no visuals', 'Only sound recordings'], 0)]),
Sc('Artificial Intelligence and Machine Learning: An Introduction',
   'Grade 9 Science strand: artificial intelligence enables computers to perform tasks that typically require human intelligence, and machine learning is a method where systems improve their performance by learning patterns from data.',
   [('What does artificial intelligence enable computers to do?', ['Perform tasks that typically require human intelligence', 'Only perform basic arithmetic with no other function', 'Operate without any programming at all', 'Function identically to a simple calculator'], 0),
    ('What is machine learning?', ['A method where systems improve performance by learning patterns from data', 'A method where systems never change their behaviour', 'A type of hardware component only', 'A process unrelated to computer science'], 0),
    ('What do machine learning systems typically use to improve over time?', ['Large amounts of data', 'No data at all', 'Only random guessing with no data', 'Only manual reprogramming with no learning involved'], 0),
    ('Which of these is a real-world application of AI or machine learning?', ['Voice assistants recognizing spoken commands', 'A rock sitting on the ground', 'A wooden chair', 'A glass of water'], 0),
    ('Why is understanding AI and machine learning increasingly important today?', ['These technologies are becoming widely used across many industries', 'AI has no real-world applications at all', 'Machine learning is only a theoretical concept with no use', 'These technologies are expected to disappear soon'], 0)]),
SS('Social Studies: The Geography of the Panama and Suez Canals',
   'Grade 9 Social Studies (Geography) strand: the Panama and Suez Canals are engineered waterways that dramatically shorten global shipping routes, making them critical points in the geography of international trade.',
   [('What do the Panama and Suez Canals allow ships to do?', ['Take dramatically shorter shipping routes between regions', 'Avoid the ocean entirely', 'Travel only within a single country', 'Increase travel time significantly for all ships'], 0),
    ('Which two oceans does the Panama Canal connect?', ['The Atlantic and Pacific Oceans', 'The Arctic and Indian Oceans', 'The Pacific and Southern Oceans only', 'It connects no oceans at all'], 0),
    ('What does the Suez Canal connect?', ['The Mediterranean Sea and the Red Sea', 'Two lakes with no ocean access', 'The Pacific and Arctic Oceans', 'Two rivers in South America'], 0),
    ('Why are these canals considered critical to global trade?', ['They significantly reduce shipping time and costs for international trade', 'They have no impact on global shipping routes', 'They are used only for local fishing boats', 'They increase the length of every shipping route'], 0),
    ('What can happen to global trade if a canal like the Suez is blocked?', ['Significant delays and disruptions to international shipping', 'No effect on global trade whatsoever', 'Immediate improvement in shipping times', 'Global trade would increase dramatically'], 0)]),
]),
day(119, [
L('Reading: Analyzing Round and Flat Characters',
  'Grade 9 Language strand: a round character is complex and multidimensional, capable of change, while a flat character is simpler, often defined by a single trait and used to support the story without much development.',
  [('What defines a round character?', ['A complex, multidimensional character capable of change', 'A character with no personality traits at all', 'A character who never appears in the story', 'A character defined only by their physical appearance'], 0),
   ('What defines a flat character?', ['A simpler character often defined by a single trait', 'A character who is always the protagonist', 'A character with the most complex development in the story', 'A character who narrates the entire story'], 0),
   ('Why might an author include flat characters in a story?', ['To support the plot without requiring extensive development', 'Flat characters always take over as the main character', 'Flat characters are never used in effective storytelling', 'To confuse readers about who the protagonist is'], 0),
   ('Which is an example of a round character?', ['A protagonist who grows, struggles, and changes throughout the story', 'A background character who appears for one line with no development', 'A character who is only ever described by their job title', 'A character with no name or role in the plot'], 0),
   ('Why is it useful for readers to distinguish between round and flat characters?', ['It helps readers understand which characters drive change and complexity in a story', 'This distinction has no effect on understanding a story', 'All characters in every story are exactly the same', 'Only flat characters ever matter to a story'], 0)]),
M('Algebra: An Introduction to Parametric Equations',
  'Grade 9 Math strand: parametric equations express the x and y coordinates of a curve separately in terms of a third variable, called a parameter, allowing more flexible descriptions of motion and curves than a single equation.',
  [('What do parametric equations use to describe a curve?', ['Separate equations for x and y in terms of a third parameter', 'Only a single equation with no parameter', 'Only whole numbers with no variables', 'Only the slope of a line'], 0),
   ('What is the third variable in parametric equations often called?', ['The parameter', 'The determinant', 'The coefficient', 'The exponent'], 0),
   ('Why might parametric equations be useful for describing motion?', ['They can show how both x and y positions change over time', 'They can only describe a single fixed point', 'They eliminate the need to track any position', 'They cannot be used to describe any motion'], 0),
   ('If x = t and y = t^2, what shape would this parametric equation likely trace?', ['A parabola', 'A straight horizontal line only', 'A perfect circle', 'A single point with no movement'], 0),
   ('Parametric equations are especially useful in fields such as ___.', ['Physics, for describing the path of a moving object', 'Only basic arithmetic', 'Only simple counting problems', 'Only measuring temperature'], 0)]),
Sc('Sustainable Agriculture and Food Technology',
   'Grade 9 Science strand: sustainable agriculture uses practices like crop rotation and precision farming technology to produce food efficiently while minimizing environmental impact and preserving resources for the future.',
   [('What is the goal of sustainable agriculture?', ['Producing food efficiently while minimizing environmental impact', 'Maximizing environmental damage with no regard for resources', 'Eliminating all farming practices completely', 'Ignoring the needs of future generations'], 0),
    ('What is crop rotation?', ['Growing different crops in the same field across different seasons or years', 'Growing the exact same crop forever with no changes', 'A method of watering crops only once a year', 'A method that eliminates the need for soil'], 0),
    ('What is precision farming technology used for?', ['Using data and technology to optimize resource use and crop yields', 'Randomly applying resources with no data or planning', 'Eliminating the need for any farming equipment', 'Ignoring soil and weather conditions entirely'], 0),
    ('Why is minimizing environmental impact important in agriculture?', ['It helps preserve resources like soil and water for future generations', 'Environmental impact has no connection to farming', 'Farming practices never affect the environment', 'Resources are unlimited and require no preservation'], 0),
    ('Sustainable agriculture connects science to which broader global concern?', ['Long-term food security and environmental stewardship', 'Only space exploration', 'Only urban architecture', 'Only ocean navigation'], 0)]),
SS('Social Studies: The Geography of Wildlife Corridors and Habitat Fragmentation',
   'Grade 9 Social Studies (Geography) strand: habitat fragmentation occurs when human development divides natural habitats into smaller, isolated patches, and wildlife corridors are designed to reconnect these patches and support animal movement.',
   [('What is habitat fragmentation?', ['When human development divides natural habitats into smaller, isolated patches', 'When wildlife habitats grow larger and more connected', 'A natural process unrelated to human development', 'The complete disappearance of all habitats worldwide'], 0),
    ('What is a wildlife corridor designed to do?', ['Reconnect fragmented habitats and support animal movement', 'Permanently separate animal populations from each other', 'Eliminate the need for any natural habitat', 'Increase the isolation of wildlife populations'], 0),
    ('What often causes habitat fragmentation?', ['Roads, cities, and other human development', 'Only natural disasters with no human involvement', 'Wildlife migration patterns alone', 'Ocean currents'], 0),
    ('Why is habitat fragmentation a concern for biodiversity?', ['Isolated populations can struggle to find food, mates, or genetic diversity', 'Fragmentation always improves an ecosystems health', 'Isolated populations always thrive with no challenges', 'Fragmentation has no effect on wildlife populations'], 0),
    ('Wildlife corridors are an example of ___.', ['Geographic planning aimed at supporting biodiversity conservation', 'A concept with no real-world application', 'A purely historical idea no longer used today', 'A tool used only for building highways'], 0)]),
]),
day(120, [
L('Language Review: Grammar, Vocabulary, and Reading Analysis',
  'Grade 9 Language strand review: students revisit cumulative and periodic sentences, portmanteau words, anaphora, the four sentence types, anti-heroes, letters of recommendation, and round vs flat characters.',
  [('What is a cumulative sentence?', ['A sentence that starts with the main idea and adds details afterward', 'A sentence with no main idea at all', 'A sentence that always begins with a question', 'A sentence with only one word'], 0),
   ('What is anaphora?', ['The repetition of a word or phrase at the beginning of successive clauses', 'A word that imitates a sound', 'A punctuation mark used in dialogue', 'A citation format for essays'], 0),
   ('What defines a compound-complex sentence?', ['At least two independent clauses and at least one dependent clause', 'Only one independent clause with no dependent clauses', 'A sentence with no punctuation', 'A sentence that must be exactly five words long'], 0),
   ('What is an anti-hero?', ['A main character who lacks traditional heroic qualities', 'A character with no flaws whatsoever', 'A minor character with no role in the plot', 'A villain who never appears in the story'], 0),
   ('What defines a round character?', ['A complex, multidimensional character capable of change', 'A character with no personality traits at all', 'A character who never appears in the story', 'A character defined only by their physical appearance'], 0)]),
M('Math Review: Advanced Algebra, Trigonometry, and Data',
  'Grade 9 Math strand review: students revisit the Binomial Theorem, the unit circle, complex numbers, the Remainder and Factor Theorems, derivatives, conic sections, the Fibonacci sequence, parametric equations, and geometric probability.',
  [('What does the Binomial Theorem help you do?', ['Expand expressions of the form (a+b)^n without multiplying repeatedly', 'Solve any linear equation instantly', 'Find the area of a circle', 'Simplify fractions only'], 0),
   ('What is a complex number?', ['A number combining a real part and an imaginary part', 'Only a whole number', 'Only a negative number', 'A number with no value'], 0),
   ('What does a derivative measure?', ['The instantaneous rate of change of a function at a point', 'The total area under a curve', 'A fixed value that never changes', 'Only the maximum value of a function'], 0),
   ('What are conic sections?', ['Curves formed by slicing a cone at different angles', 'A type of algebraic expression only', 'A type of matrix', 'A method for solving linear equations'], 0),
   ('How is each new number in the Fibonacci sequence generated?', ['By adding the two previous numbers together', 'By multiplying the previous number by two', 'By subtracting one from the previous number', 'By squaring the previous number'], 0)]),
Sc('Science Review: Senses, Technology, and Modern Applications',
   'Grade 9 Science strand review: students revisit the human eye and ear, antibiotic resistance, symbiosis, robotics, forensic science, materials science, artificial intelligence, and sustainable agriculture.',
   [('What structure in the eye focuses light onto the retina?', ['The lens', 'The eardrum', 'The trachea', 'The epidermis'], 0),
    ('What structure vibrates when sound waves first enter the ear?', ['The eardrum', 'The cochlea alone', 'The optic nerve', 'The retina'], 0),
    ('What defines commensalism?', ['One species benefits while the other is unaffected', 'Both species benefit equally', 'Both species are harmed equally', 'One species is destroyed completely'], 0),
    ('What fields does mechatronics combine?', ['Mechanical engineering, electronics, and computer science', 'Only biology and chemistry', 'Only astronomy and geology', 'Only art and music'], 0),
    ('What is machine learning?', ['A method where systems improve performance by learning patterns from data', 'A method where systems never change their behaviour', 'A type of hardware component only', 'A process unrelated to computer science'], 0)]),
SS('Social Studies Review: Global Geography and Trade',
   'Grade 9 Social Studies (Geography) strand review: students revisit small island states, e-waste, the gig economy, the Silk Road, coffee and cocoa production, urban green space, shipping ports, the Panama and Suez Canals, and habitat fragmentation.',
   [('What does SIDS stand for?', ['Small Island Developing States', 'Southern International Development Sector', 'Sustainable Island Data System', 'Sea Ice Distribution Study'], 0),
    ('What is e-waste?', ['Discarded electronic devices', 'Waste generated only from farming', 'Waste produced solely by factories', 'A type of renewable energy source'], 0),
    ('What was the Silk Road?', ['A historic network of trade routes connecting Asia, the Middle East, and Europe', 'A single modern highway system', 'A type of railway built in the 20th century', 'A shipping canal in South America'], 0),
    ('Which two oceans does the Panama Canal connect?', ['The Atlantic and Pacific Oceans', 'The Arctic and Indian Oceans', 'The Pacific and Southern Oceans only', 'It connects no oceans at all'], 0),
    ('What is habitat fragmentation?', ['When human development divides natural habitats into smaller, isolated patches', 'When wildlife habitats grow larger and more connected', 'A natural process unrelated to human development', 'The complete disappearance of all habitats worldwide'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g9_111_120)
    append_to(9, g9_111_120)
