#!/usr/bin/env python3
"""Grade 12, Days 111-120 -- extends Grade 12 from 110 to 120 days. Topics
chosen after grepping the existing Day 1-110 title list (data/grade12.json)
extensively to avoid any overlap: structuralism and semiotics, New
Criticism and close reading, ecofeminism, prosody and meter, the sublime
in Romantic literature, Artaud and the Theatre of Cruelty, biographical
criticism, disability studies in fiction, and pastiche; the Goldbach
Conjecture, the Twin Prime Conjecture, Pell's Equation, Fermat's Last
Theorem, the Collatz Conjecture, Gaussian integers, the Prime Number
Theorem, Farey sequences, and Zeckendorf's Theorem; triple integrals in
spherical coordinates, the Beta function, Fubini's Theorem, the
Cauchy-Riemann equations, the Residue Theorem, the Dirac delta function,
the heat equation, the wave equation, and the Brachistochrone problem;
the Davisson-Germer experiment, the Foucault pendulum, the Cavendish
experiment, the Hall effect, the Coriolis effect, Brownian motion, the
Faraday effect, the Peltier effect, and the kinetic theory of gases.

Subject keys for Grade 12 are "English", "AdvancedFunctions",
"Calculus", "Physics" (same as all earlier Grade 12 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided or use the curly
Unicode form.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E12 = 'https://tvolearn.com/pages/grade-12-english'
AF12 = 'https://tvolearn.com/pages/grade-12-advanced-functions'
CA12 = 'https://tvolearn.com/pages/grade-12-calculus-and-vectors'
PH12 = 'https://tvolearn.com/pages/grade-12-physics'
RE, RAF, RCA, RPH = (
    'TVO Learn: Grade 12 English',
    'TVO Learn: Grade 12 Advanced Functions',
    'TVO Learn: Grade 12 Calculus and Vectors',
    'TVO Learn: Grade 12 Physics',
)


def E(t, s, q):
    return sub('English', t, s, RE, E12, q)


def AF(t, s, q):
    return sub('AdvancedFunctions', t, s, RAF, AF12, q)


def CA(t, s, q):
    return sub('Calculus', t, s, RCA, CA12, q)


def PH(t, s, q):
    return sub('Physics', t, s, RPH, PH12, q)


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


g12_111_120 = [
day(111, [
E('Literary Theory: Structuralism and Semiotics',
  'Grade 12 English strand: structuralism analyzes literature by examining underlying systems of signs and structures that generate meaning, drawing on semiotics, the study of how signs and symbols create meaning within a system.',
  [('What does structuralism examine in a text?', ['Underlying systems of signs and structures that generate meaning', 'Only the authors personal biography', 'Only the historical period a text was written in', 'Only the emotional response of individual readers'], 0),
   ('What is semiotics?', ['The study of how signs and symbols create meaning within a system', 'The study of chemical reactions in nature', 'A method for citing sources in an essay', 'A grammar rule about verb tense'], 0),
   ('According to structuralist thinking, meaning in a text often arises from ___.', ['Relationships and patterns between elements, rather than the elements alone', 'The authors mood while writing', 'Random chance with no underlying system', 'The physical weight of the book'], 0),
   ('Structuralism was influenced by which field studying language systems?', ['Linguistics', 'Astronomy', 'Chemistry', 'Geology'], 0),
   ('Why might a structuralist critic compare multiple myths or stories from different cultures?', ['To identify shared underlying structures or patterns across narratives', 'Structuralists never compare texts across cultures', 'To prove that all stories are entirely unrelated to one another', 'To focus only on a single authors biography'], 0)]),
AF('Number Theory: The Goldbach Conjecture',
   'Grade 12 Advanced Functions strand: the Goldbach Conjecture proposes that every even integer greater than 2 can be expressed as the sum of two prime numbers, a statement verified for enormous numbers but still unproven in general.',
   [('What does the Goldbach Conjecture propose?', ['Every even integer greater than 2 can be written as the sum of two primes', 'Every odd integer can be written as the sum of two primes', 'No even number can ever be written as a sum of primes', 'All prime numbers are even'], 0),
    ('Has the Goldbach Conjecture been proven for all even numbers?', ['No, it remains unproven in general despite extensive verification', 'Yes, it was proven centuries ago', 'It has been disproven completely', 'It only applies to numbers less than ten'], 0),
    ('Which even number is the smallest example the conjecture applies to?', ['4 (which equals 2 + 2)', '2', '1', '0'], 0),
    ('What field of mathematics does the Goldbach Conjecture belong to?', ['Number theory', 'Trigonometry', 'Geometry', 'Statistics'], 0),
    ('Why is the Goldbach Conjecture considered a famous unsolved problem?', ['It has been tested extensively for huge numbers with no exception found, yet no general proof exists', 'It was easily solved using basic arithmetic', 'It has no connection to prime numbers', 'Mathematicians have shown it to be false'], 0)]),
CA('Calculus: Triple Integrals in Spherical Coordinates',
   'Grade 12 Calculus strand: triple integrals in spherical coordinates use the variables rho, theta, and phi to describe points in three-dimensional space, making them especially useful for integrating over spheres and spherically symmetric regions.',
   [('What three variables are used in spherical coordinates?', ['Rho, theta, and phi', 'Only x, y, and z', 'Only r and theta', 'Only length and width'], 0),
    ('What does the variable rho typically represent in spherical coordinates?', ['The distance from the origin to the point', 'The angle from the positive x-axis', 'The height above the xy-plane', 'The area of a cross-section'], 0),
    ('Why are spherical coordinates especially useful for certain triple integrals?', ['They simplify integration over spheres and spherically symmetric regions', 'They make every integral more complicated with no benefit', 'They can only be used for two-dimensional problems', 'They eliminate the need for any coordinate system'], 0),
    ('What extra factor must be included in the integrand when converting to spherical coordinates?', ['The Jacobian factor, rho squared times sine of phi', 'No adjustment is ever needed', 'Only a factor of pi', 'Only a factor of the radius squared with no other terms'], 0),
    ('Triple integrals in spherical coordinates are commonly used to calculate ___.', ['The volume or mass of spherical objects', 'Only the perimeter of a two-dimensional shape', 'Only the slope of a line', 'Only a single point value with no volume'], 0)]),
PH('Physics: The Davisson-Germer Experiment and Electron Diffraction',
   'Grade 12 Physics strand: the Davisson-Germer experiment demonstrated that electrons produce diffraction patterns when scattered off a crystal, providing direct experimental evidence for the wave nature of matter predicted by de Broglies hypothesis.',
   [('What did the Davisson-Germer experiment demonstrate?', ['That electrons produce diffraction patterns, showing wave-like behaviour', 'That electrons have no measurable properties at all', 'That light behaves only as a particle with no wave nature', 'That protons are the only particles with wave properties'], 0),
    ('What material did the experiment use to scatter electrons?', ['A nickel crystal', 'A block of pure water', 'A vacuum with no material at all', 'A sample of liquid mercury'], 0),
    ('Which earlier hypothesis did this experiment provide evidence for?', ['The de Broglie hypothesis of matter waves', 'Newtons laws of motion', 'The law of conservation of energy', 'Keplers laws of planetary motion'], 0),
    ('Why was the Davisson-Germer experiment significant for quantum physics?', ['It provided direct experimental confirmation that particles can behave like waves', 'It disproved the existence of electrons entirely', 'It showed that electrons behave purely as classical particles with no wave nature', 'It had no connection to quantum theory'], 0),
    ('The diffraction pattern observed in this experiment is similar to what other well-known phenomenon?', ['The diffraction of light waves through a crystal lattice', 'The reflection of light off a flat mirror', 'The refraction of sound through air', 'The absorption of heat by a metal rod'], 0)]),
]),
day(112, [
E('Literary Theory: New Criticism and Close Reading',
  'Grade 12 English strand: New Criticism emphasizes close reading of a text on its own terms, focusing on elements like structure, imagery, and language while deliberately setting aside the authors biography and historical context.',
  [('What does New Criticism emphasize when analyzing a text?', ['Close reading of the text on its own terms', 'Only the authors personal life and biography', 'Only the historical period surrounding the text', 'Only the readers personal emotional reaction'], 0),
   ('Which elements does New Criticism typically focus on?', ['Structure, imagery, and language within the text itself', 'Only sales figures and popularity of the book', 'Only the publishers marketing strategy', 'Only unrelated political events of the time'], 0),
   ('What does New Criticism deliberately set aside when analyzing a text?', ['The authors biography and historical context', 'The words used within the text', 'The structure of the sentences', 'The imagery found in the writing'], 0),
   ('Why might a New Critic focus so closely on the words of a text itself?', ['To understand meaning as something built directly within the language of the work', 'Because words in a text have no connection to meaning', 'To avoid reading the text at all', 'Because close reading is considered unnecessary in literary study'], 0),
   ('New Criticism is often associated with a technique known as ___.', ['Close reading', 'Only skimming a text quickly', 'Ignoring the text entirely', 'Reading only book reviews instead of the original text'], 0)]),
AF('Number Theory: The Twin Prime Conjecture',
   'Grade 12 Advanced Functions strand: the Twin Prime Conjecture proposes that there are infinitely many pairs of prime numbers that differ by exactly two, such as 11 and 13, a claim still unproven despite significant progress by mathematicians.',
   [('What does the Twin Prime Conjecture propose?', ['There are infinitely many pairs of primes that differ by exactly two', 'There are only a finite number of prime numbers in total', 'No two prime numbers can ever differ by two', 'Every prime number has exactly one twin'], 0),
    ('Which of these is an example of twin primes?', ['11 and 13', '2 and 7', '4 and 6', '9 and 12'], 0),
    ('Has the Twin Prime Conjecture been proven?', ['No, it remains unproven despite significant mathematical progress', 'Yes, it was proven centuries ago', 'It has been definitively disproven', 'It only applies to numbers less than 100'], 0),
    ('What field of mathematics does the Twin Prime Conjecture belong to?', ['Number theory', 'Trigonometry', 'Geometry', 'Financial mathematics'], 0),
    ('Why do mathematicians find the Twin Prime Conjecture compelling?', ['It reveals a simple yet deeply unresolved pattern within the prime numbers', 'It has no connection to prime numbers whatsoever', 'It was already fully solved using basic algebra', 'Prime numbers become more common as numbers increase, disproving the idea entirely'], 0)]),
CA('Calculus: The Beta Function — A Companion to the Gamma Function',
   'Grade 12 Calculus strand: the Beta function is a special integral closely related to the Gamma function, often used to evaluate certain definite integrals and expressed in terms of Gamma function values.',
   [('What is the Beta function closely related to?', ['The Gamma function', 'The sine function only', 'The exponential function only', 'A simple linear equation'], 0),
    ('What can the Beta function help mathematicians do?', ['Evaluate certain definite integrals that would otherwise be difficult', 'Only add two whole numbers together', 'Only measure the area of a rectangle', 'Only solve basic linear equations'], 0),
    ('How is the Beta function typically expressed in relation to the Gamma function?', ['As a ratio involving Gamma function values', 'As a function completely unrelated to the Gamma function', 'Only as a sum of two prime numbers', 'Only as a whole number with no formula'], 0),
    ('The Beta function is defined using what kind of mathematical expression?', ['A definite integral', 'A simple algebraic equation with no integral', 'A single geometric shape', 'A basic arithmetic operation only'], 0),
    ('Where might the Beta function be applied in advanced mathematics?', ['In probability theory and statistical distributions', 'Only in basic elementary arithmetic', 'Only in simple counting problems', 'It has no real mathematical application'], 0)]),
PH('Physics: The Foucault Pendulum and Proof of Earths Rotation',
   'Grade 12 Physics strand: the Foucault pendulum demonstrated Earths rotation by showing that its swinging plane appears to gradually rotate over time relative to the ground, providing direct physical evidence without needing to observe the stars.',
   [('What did the Foucault pendulum famously demonstrate?', ['Earths rotation', 'The existence of gravity', 'The speed of light', 'The structure of the atom'], 0),
    ('What is observed about the swinging plane of a Foucault pendulum over time?', ['It appears to gradually rotate relative to the ground', 'It remains perfectly fixed with no change at all', 'It stops swinging entirely after a few minutes', 'It swings faster and faster with no explanation'], 0),
    ('Why does the pendulums swinging plane appear to rotate?', ['The Earth is rotating beneath the pendulum, which maintains its plane of motion', 'The pendulum itself is designed to rotate on its own', 'The rotation is caused by wind resistance alone', 'The rotation is an optical illusion with no physical basis'], 0),
    ('What made the Foucault pendulum significant when first demonstrated?', ['It provided direct physical evidence of Earths rotation without observing the stars', 'It disproved that the Earth rotates at all', 'It showed no connection to Earths motion', 'It could only be observed from outer space'], 0),
    ('The rate at which a Foucault pendulums plane appears to rotate depends on ___.', ['The latitude at which the pendulum is located', 'The colour of the pendulum bob', 'The material the pendulum string is made of', 'The time of day only, with no other factor'], 0)]),
]),
day(113, [
E('Literature: Ecofeminism — Gender and the Environment in Text',
  'Grade 12 English strand: ecofeminism examines the connections between the domination of women and the domination of nature within literature, exploring how texts represent gender and environmental exploitation as interconnected issues.',
  [('What does ecofeminism examine in literature?', ['Connections between the domination of women and the domination of nature', 'Only the physical setting of a story with no thematic analysis', 'Only grammar and sentence structure', 'Only the historical publication date of a text'], 0),
   ('What two forms of domination does ecofeminist criticism often connect?', ['The domination of women and the exploitation of the natural environment', 'The domination of animals and the domination of machines', 'The domination of language and the domination of music', 'The domination of mathematics and the domination of art'], 0),
   ('Why might an ecofeminist critic analyze how nature is described in a text?', ['To explore parallels between how nature and women are represented or controlled', 'Ecofeminist critics never discuss the natural environment', 'To ignore gender entirely in the analysis', 'To focus solely on unrelated economic data'], 0),
   ('Ecofeminism combines which two broader areas of critical thought?', ['Feminist theory and environmental thought', 'Only mathematics and physics', 'Only ancient history and archaeology', 'Only music theory and visual art'], 0),
   ('Which of these might an ecofeminist reading highlight in a novel?', ['Language that frames land as something to be conquered, paralleling attitudes toward women', 'Only the number of chapters in the book', 'Only the price of the book when published', 'Only unrelated grammatical errors in the text'], 0)]),
AF('Number Theory: Pells Equation',
   'Grade 12 Advanced Functions strand: Pells equation is a Diophantine equation of the form x^2 - Dy^2 = 1, where D is a non-square positive integer, and finding integer solutions connects number theory to continued fractions.',
   [('What is the general form of Pells equation?', ['x^2 - Dy^2 = 1', 'x + y = D', 'x^2 + y^2 = D', 'xy = D'], 0),
    ('What type of number must D be in Pells equation for it to have interesting solutions?', ['A non-square positive integer', 'Always exactly zero', 'Always a negative fraction', 'Always equal to one'], 0),
    ('What kind of solutions are sought when solving Pells equation?', ['Integer solutions for x and y', 'Only solutions equal to zero', 'Only solutions involving imaginary numbers', 'No solutions are ever sought'], 0),
    ('What earlier mathematical concept is closely connected to solving Pells equation?', ['Continued fractions', 'Basic multiplication tables', 'The Pythagorean theorem', 'Simple linear graphing'], 0),
    ('Pells equation is an example of which broader category of equation?', ['A Diophantine equation, which seeks integer solutions', 'A linear equation with a single unknown', 'An equation with no real-world mathematical significance', 'A simple percentage calculation'], 0)]),
CA('Calculus: Fubinis Theorem and Reversing the Order of Integration',
   'Grade 12 Calculus strand: Fubinis Theorem states that under suitable conditions, a double integral over a rectangular region can be evaluated as an iterated integral in either order, allowing mathematicians to choose whichever order simplifies the calculation.',
   [('What does Fubinis Theorem allow for a double integral over a suitable region?', ['Evaluating it as an iterated integral in either order', 'Only evaluating it in one fixed, unchangeable order', 'Eliminating the need to integrate at all', 'Only applying to integrals with no variables'], 0),
    ('Why might a mathematician want to reverse the order of integration?', ['To simplify a calculation that is difficult in the original order', 'Reversing the order is never useful for simplifying calculations', 'It always produces an incorrect final answer', 'Order never affects the difficulty of an integral'], 0),
    ('Under what general condition does Fubinis Theorem typically apply?', ['When the function is well-behaved (such as continuous) over the region of integration', 'It applies to every possible function with no conditions', 'It never applies to any function', 'Only when the function equals zero everywhere'], 0),
    ('Fubinis Theorem is especially useful when working with which type of integral?', ['Double and triple integrals', 'Only single-variable integrals', 'Only integrals with no bounds', 'Only integrals of constant functions'], 0),
    ('If reversing the order of integration under Fubinis Theorem, what generally must also change?', ['The limits of integration, to correctly describe the same region', 'Nothing else needs to change at all', 'The function itself must be entirely replaced', 'The final answer will always become undefined'], 0)]),
PH('Physics: The Cavendish Experiment and Measuring the Gravitational Constant',
   'Grade 12 Physics strand: the Cavendish experiment used a sensitive torsion balance to measure the tiny gravitational attraction between lead spheres, allowing the first accurate determination of the gravitational constant, G.',
   [('What device did the Cavendish experiment use to measure gravitational attraction?', ['A torsion balance', 'A simple spring scale', 'A telescope', 'A voltmeter'], 0),
    ('What force was the Cavendish experiment designed to measure?', ['The gravitational attraction between two masses', 'The electric force between two charges', 'The magnetic force between two magnets', 'The frictional force between two surfaces'], 0),
    ('What important physical constant did the Cavendish experiment help determine?', ['The gravitational constant, G', 'The speed of light', 'The charge of an electron', 'The mass of a proton'], 0),
    ('Why was measuring gravitational attraction between everyday objects considered so challenging?', ['Gravitational forces between small masses are extremely weak', 'Gravity between small objects is actually very strong and easy to measure', 'Gravitational force has no measurable effect at all', 'The experiment required no precision instruments whatsoever'], 0),
    ('The results of the Cavendish experiment allowed scientists to later calculate what other important quantity?', ['The mass of the Earth', 'The temperature of the sun', 'The age of the universe', 'The speed of sound'], 0)]),
]),
day(114, [
E('Poetry: Prosody and Meter — The Music of Verse',
  'Grade 12 English strand: prosody is the study of the rhythmic and sonic qualities of poetry, including meter, the patterned arrangement of stressed and unstressed syllables that gives a poem its underlying musical structure.',
  [('What does prosody study in poetry?', ['The rhythmic and sonic qualities of verse', 'Only the plot of a poem', 'Only the historical context of a poem', 'Only the punctuation used in a poem'], 0),
   ('What is meter in poetry?', ['The patterned arrangement of stressed and unstressed syllables', 'The total number of words in a poem', 'A type of poem with no rhythm at all', 'A citation style used in essays'], 0),
   ('What effect does meter give to a poem?', ['An underlying musical or rhythmic structure', 'It removes any sense of rhythm entirely', 'It has no effect on how the poem sounds', 'It only affects the poems visual appearance on a page'], 0),
   ('Which term describes a common meter pattern consisting of an unstressed syllable followed by a stressed syllable?', ['Iambic', 'Alphabetic', 'Numeric', 'Chromatic'], 0),
   ('Why might a poet deliberately vary the meter within a poem?', ['To create emphasis or reflect a shift in tone or meaning', 'Variation in meter always ruins a poems meaning entirely', 'Meter can never be varied within a single poem', 'Meter has no relationship to tone or meaning'], 0)]),
AF('Number Theory: Fermats Last Theorem — A Historical Overview',
   'Grade 12 Advanced Functions strand: Fermats Last Theorem states that no three positive integers a, b, and c can satisfy a^n + b^n = c^n for any integer value of n greater than 2, a claim that remained unproven for over 350 years until Andrew Wiles solved it in 1994.',
   [('What does Fermats Last Theorem state?', ['No three positive integers can satisfy a^n + b^n = c^n for n greater than 2', 'Every equation of this form has infinitely many solutions', 'The equation only has solutions when n equals 1', 'All positive integers satisfy this equation for any value of n'], 0),
    ('Roughly how long did Fermats Last Theorem remain unproven?', ['Over 350 years', 'Only a few days', 'Less than one year', 'It has never been proven at all'], 0),
    ('Who finally proved Fermats Last Theorem?', ['Andrew Wiles', 'Isaac Newton', 'Pythagoras', 'Leonhard Euler'], 0),
    ('In what year was Fermats Last Theorem finally proven?', ['1994', '1700', '1850', '2020'], 0),
    ('Why is Fermats Last Theorem considered one of the most famous problems in mathematics?', ['Its simple statement contrasted sharply with the extreme difficulty of proving it', 'It was proven within days of being proposed', 'It has no historical significance in mathematics', 'It applies only to a single specific value of a, b, and c'], 0)]),
CA('Calculus: An Introduction to the Cauchy-Riemann Equations',
   'Grade 12 Calculus strand: the Cauchy-Riemann equations are a pair of partial differential equations that a complex function must satisfy to be differentiable in the complex sense, forming a foundation for the study of complex analysis.',
   [('What must a complex function satisfy to be differentiable in the complex sense?', ['The Cauchy-Riemann equations', 'Only the standard rules of real-number multiplication', 'Only the Pythagorean theorem', 'No conditions are required at all'], 0),
    ('What type of equations are the Cauchy-Riemann equations?', ['A pair of partial differential equations', 'A single linear equation with one variable', 'A basic arithmetic equation with whole numbers only', 'An equation with no variables at all'], 0),
    ('The Cauchy-Riemann equations form a foundation for which branch of mathematics?', ['Complex analysis', 'Basic geometry', 'Elementary statistics', 'Financial mathematics'], 0),
    ('If a complex function satisfies the Cauchy-Riemann equations at a point, what can be said about that point?', ['The function is complex differentiable there', 'The function is undefined there', 'The function must be a constant with no variation', 'The function has no real or imaginary parts'], 0),
    ('The Cauchy-Riemann equations relate the partial derivatives of a functions ___.', ['Real and imaginary parts', 'Only its numerator and denominator', 'Only its domain and range', 'Only its x and y intercepts'], 0)]),
PH('Physics: The Hall Effect',
   'Grade 12 Physics strand: the Hall effect occurs when a magnetic field applied perpendicular to a current-carrying conductor produces a measurable voltage across the conductor, useful for determining charge carrier type and concentration.',
   [('What causes the Hall effect?', ['A magnetic field applied perpendicular to a current-carrying conductor', 'Sound waves passing through a solid', 'Light shining directly on a conductor', 'Heat applied to a conductor with no magnetic field'], 0),
    ('What is produced across the conductor in the Hall effect?', ['A measurable voltage, called the Hall voltage', 'A measurable change in mass', 'A measurable change in colour', 'A measurable change in temperature only'], 0),
    ('What can the Hall effect help scientists determine about a material?', ['The type and concentration of charge carriers', 'The exact age of the material', 'The taste of the material', 'The material weight in a vacuum'], 0),
    ('In what direction is the magnetic field applied relative to the current in the Hall effect?', ['Perpendicular to the current', 'Parallel to the current', 'In the exact opposite direction of the current', 'The direction has no effect on the outcome'], 0),
    ('The Hall effect has practical applications in devices such as ___.', ['Sensors that measure magnetic fields', 'Only devices that measure sound', 'Only devices that measure taste', 'Only devices with no electrical components'], 0)]),
]),
day(115, [
E('Literature: The Sublime in Romantic Literature',
  'Grade 12 English strand: the sublime describes an overwhelming sense of awe, vastness, or terror often evoked by nature in Romantic literature, blending beauty with a feeling that exceeds ordinary human comprehension.',
  [('What does the sublime describe in Romantic literature?', ['An overwhelming sense of awe, vastness, or terror', 'A calm, ordinary, everyday feeling', 'A purely comedic tone in a text', 'A strictly mathematical concept'], 0),
   ('What natural settings commonly evoke the sublime in Romantic writing?', ['Vast mountains, storms, and other overwhelming landscapes', 'Only small, quiet gardens', 'Only indoor domestic settings', 'Only urban city streets'], 0),
   ('How does the sublime differ from simple beauty in Romantic aesthetics?', ['The sublime combines beauty with an overwhelming or even terrifying vastness', 'The sublime is identical to simple beauty with no distinction', 'The sublime refers only to small, delicate objects', 'The sublime has no connection to emotion at all'], 0),
   ('Why might Romantic writers be drawn to depicting the sublime?', ['To express emotions and experiences that exceed ordinary human comprehension', 'To avoid any emotional content in their writing', 'The sublime was never a concern for Romantic writers', 'To focus exclusively on mundane, everyday events'], 0),
   ('The concept of the sublime is often associated with which broader literary and philosophical movement?', ['Romanticism', 'Modernism', 'Realism', 'Naturalism'], 0)]),
AF('Discrete Math: The Collatz Conjecture',
   'Grade 12 Advanced Functions strand: the Collatz Conjecture proposes that starting from any positive integer and repeatedly applying a simple rule (halve if even, triple and add one if odd) will always eventually reach the number 1, though this remains unproven.',
   [('What rule does the Collatz Conjecture apply to a number?', ['Halve it if even, triple it and add one if odd', 'Always add one, regardless of the number', 'Always multiply by two, regardless of the number', 'Always subtract one, regardless of the number'], 0),
    ('According to the Collatz Conjecture, where does this process always eventually lead?', ['The number 1', 'The number 0', 'A number that increases forever with no end', 'A negative number'], 0),
    ('Has the Collatz Conjecture been proven for all positive integers?', ['No, it remains unproven despite extensive computational verification', 'Yes, it was proven immediately when first proposed', 'It has been shown to be false for most numbers', 'It only applies to numbers less than five'], 0),
    ('What happens when you apply the Collatz rule to the number 6?', ['It becomes 3, since 6 is even', 'It becomes 19, since 6 is treated as odd', 'It becomes 12, by doubling instead of halving', 'It becomes 0 immediately'], 0),
    ('The Collatz Conjecture is a well-known example of ___.', ['A simply stated mathematical problem that remains famously difficult to prove', 'A basic arithmetic fact proven in elementary school', 'A theorem with no connection to number sequences', 'An equation with a known, published counterexample'], 0)]),
CA('Calculus: The Residue Theorem — An Introduction to Complex Integration',
   'Grade 12 Calculus strand: the Residue Theorem provides a powerful method for evaluating certain complex integrals by summing the residues, or key coefficients, at the singular points enclosed within a contour.',
   [('What does the Residue Theorem help evaluate?', ['Certain complex integrals along a closed contour', 'Only simple real-number addition problems', 'Only the area of a basic rectangle', 'Only the slope of a straight line'], 0),
    ('What is summed together when applying the Residue Theorem?', ['The residues at the singular points enclosed by the contour', 'Only the real parts of a complex number', 'Only whole numbers with no complex component', 'Only positive integers less than ten'], 0),
    ('What is a singular point of a complex function?', ['A point where the function is not well-behaved or defined normally', 'A point where the function equals exactly one', 'A point located only on the real number line', 'A point that never affects any integral calculation'], 0),
    ('Why is the Residue Theorem considered powerful for certain integrals?', ['It can simplify integrals that would be extremely difficult to evaluate using standard real-number methods', 'It only applies to integrals that were already trivial to solve', 'It has no practical use in mathematics', 'It cannot be applied to any complex function'], 0),
    ('The Residue Theorem is a key tool within which area of mathematics?', ['Complex analysis', 'Basic algebra', 'Elementary geometry', 'Simple arithmetic'], 0)]),
PH('Physics: The Coriolis Effect',
   'Grade 12 Physics strand: the Coriolis effect is an apparent deflection of moving objects observed in a rotating reference frame, such as Earth, causing winds and ocean currents to curve rather than travel in perfectly straight paths.',
   [('What is the Coriolis effect?', ['An apparent deflection of moving objects in a rotating reference frame', 'A force that only exists in outer space', 'A type of magnetic field around Earth', 'A change in an objects mass due to motion'], 0),
    ('What causes the Coriolis effect on Earth?', ['Earths rotation', 'Earths gravitational pull alone', 'Ocean temperature changes only', 'Solar radiation striking the Earths surface'], 0),
    ('How does the Coriolis effect influence wind and ocean currents?', ['It causes them to curve rather than travel in perfectly straight paths', 'It has no influence on wind or ocean currents at all', 'It causes them to instantly stop moving', 'It only affects currents in a single, fixed direction everywhere'], 0),
    ('In which hemisphere does the Coriolis effect typically deflect moving objects to the right of their motion?', ['The Northern Hemisphere', 'The Southern Hemisphere', 'Neither hemisphere experiences any deflection', 'Only at the equator, with no deflection elsewhere'], 0),
    ('The Coriolis effect is an example of a ___ force, observed only within a rotating frame of reference.', ['Fictitious (or apparent)', 'Purely gravitational', 'Purely magnetic', 'Purely nuclear'], 0)]),
]),
day(116, [
E('Drama: Artaud and the Theatre of Cruelty',
  'Grade 12 English strand: Antonin Artauds Theatre of Cruelty sought to shock audiences out of complacency through intense, visceral sensory experiences, rejecting traditional narrative and dialogue in favour of raw physical and emotional impact.',
  [('Who developed the concept known as the Theatre of Cruelty?', ['Antonin Artaud', 'William Shakespeare', 'Bertolt Brecht', 'Henrik Ibsen'], 0),
   ('What was the main goal of the Theatre of Cruelty?', ['To shock audiences out of complacency through intense sensory experience', 'To gently reassure audiences with familiar, comforting stories', 'To rely entirely on quiet, minimalist dialogue', 'To avoid any emotional impact on the audience'], 0),
   ('What did Artauds approach often reject in favour of raw physical impact?', ['Traditional narrative and conventional dialogue', 'All forms of performance entirely', 'The presence of any actors on stage', 'The use of any stage lighting'], 0),
   ('How does the Theatre of Cruelty differ from Brechtian alienation techniques?', ['It seeks to immerse and overwhelm the audience emotionally, rather than create critical distance', 'The two approaches are exactly identical with no differences', 'It focuses only on comedic elements, unlike Brechtian theatre', 'It avoids any audience reaction whatsoever'], 0),
   ('Why might the term cruelty in Artauds theory be considered misleading if taken too literally?', ['It refers more to intense sensory and emotional confrontation than to literal violence', 'It refers only to physical violence with no other meaning', 'Artaud intended the term to mean nothing at all', 'The term was used only to describe stage lighting'], 0)]),
AF('Number Theory: Gaussian Integers and Complex Factorization',
   'Grade 12 Advanced Functions strand: Gaussian integers are complex numbers of the form a+bi, where a and b are integers, forming a number system in which certain primes can be factored further than they can within the ordinary integers.',
   [('What is a Gaussian integer?', ['A complex number of the form a+bi, where a and b are integers', 'Only a whole number with no imaginary part', 'Only a fraction between zero and one', 'A number with no defined value'], 0),
    ('What can happen to certain prime numbers when working within the Gaussian integers?', ['They can be factored further than within the ordinary integers', 'They always remain completely unfactorable', 'They cease to be numbers entirely', 'They automatically become negative numbers'], 0),
    ('Which of these is an example of a Gaussian integer?', ['3 + 2i', 'Only the number pi', 'Only a percentage value', 'Only a negative fraction'], 0),
    ('Gaussian integers extend which more familiar number system?', ['The ordinary integers', 'Only fractions between zero and one', 'Only irrational numbers', 'Only negative decimals'], 0),
    ('Studying Gaussian integers connects number theory to which other branch of mathematics?', ['Complex numbers', 'Basic geometry with no complex numbers', 'Elementary statistics', 'Simple financial mathematics'], 0)]),
CA('Calculus: The Dirac Delta Function',
   'Grade 12 Calculus strand: the Dirac delta function is a special mathematical object used to model an idealized point source or impulse, defined so that it is zero everywhere except at a single point, yet integrates to one over the entire real line.',
   [('What does the Dirac delta function model in mathematics and physics?', ['An idealized point source or impulse', 'A gradual, smooth change over a wide interval', 'A constant value with no variation', 'A function with no defined properties at all'], 0),
    ('Where is the Dirac delta function equal to zero?', ['Everywhere except at a single point', 'Everywhere, with no exceptions', 'Only at the single point where it is centred', 'Nowhere, since it is never equal to zero'], 0),
    ('What is the total integral of the Dirac delta function over the entire real line?', ['One', 'Zero', 'Infinity, with no finite value', 'Negative one'], 0),
    ('In what fields is the Dirac delta function commonly used?', ['Physics and engineering, to model instantaneous impulses', 'Only elementary arithmetic, with no advanced application', 'Only basic geometry, with no calculus application', 'It has no practical applications at all'], 0),
    ('The Dirac delta function is often described as a ___.', ['Generalized function or distribution, rather than a function in the traditional sense', 'A simple polynomial function', 'A basic trigonometric function', 'An ordinary linear function'], 0)]),
PH('Physics: Brownian Motion and Einsteins Explanation',
   'Grade 12 Physics strand: Brownian motion is the random, erratic movement of small particles suspended in a fluid, and Einsteins 1905 explanation showed that this motion results from countless collisions with fast-moving molecules, providing strong evidence for the existence of atoms.',
   [('What is Brownian motion?', ['The random, erratic movement of small particles suspended in a fluid', 'A steady, predictable motion in a straight line', 'A type of motion found only in solids', 'A motion that occurs only in a vacuum'], 0),
    ('What did Einstein propose as the cause of Brownian motion in 1905?', ['Countless collisions with fast-moving molecules in the fluid', 'A hidden magnetic field acting on the particles', 'Sound waves pushing the particles around', 'Gravity alone, with no molecular involvement'], 0),
    ('Why was Einsteins explanation of Brownian motion scientifically significant?', ['It provided strong evidence for the existence of atoms and molecules', 'It disproved the existence of atoms entirely', 'It had no connection to atomic theory', 'It showed that fluids contain no moving particles at all'], 0),
    ('What type of particles is Brownian motion typically observed in?', ['Small particles suspended in a liquid or gas', 'Only extremely large, heavy objects', 'Only particles found in outer space', 'Only particles frozen in solid ice'], 0),
    ('Brownian motion helped confirm which broader scientific theory?', ['The kinetic theory of matter', 'The theory of general relativity', 'The theory of electromagnetism', 'The theory of continental drift'], 0)]),
]),
day(117, [
E('Literary Theory: Biographical Criticism — Reading the Author into the Text',
  'Grade 12 English strand: biographical criticism interprets a literary work by examining connections between the text and the authors life experiences, beliefs, and historical circumstances, while remaining cautious about reducing a text entirely to biography.',
  [('What does biographical criticism examine when interpreting a text?', ['Connections between the text and the authors life experiences', 'Only the physical appearance of the printed book', 'Only unrelated events from a different century', 'Only the readers personal opinions with no textual evidence'], 0),
   ('What might a biographical critic explore about an author?', ['Their beliefs and historical circumstances', 'Only their favourite colour', 'Only their handwriting style', 'Only their taste in food'], 0),
   ('What caution do scholars often raise about biographical criticism?', ['The risk of reducing a text entirely to the authors biography, ignoring other interpretations', 'That biography should always be the only valid approach to a text', 'That an authors life never has any relevance to their work', 'That biographical criticism should replace all close reading of a text'], 0),
   ('Why might knowing an authors historical circumstances be useful when reading their work?', ['It can provide context that deepens understanding of the texts themes or choices', 'Historical context is always completely irrelevant to a text', 'It replaces the need to read the text at all', 'It guarantees a single, definitive interpretation of every text'], 0),
   ('Biographical criticism is often used alongside other approaches, such as ___.', ['Historical or formalist analysis, to build a fuller picture of a text', 'Only mathematical analysis, with no literary connection', 'Only analysis of unrelated scientific data', 'No other critical approaches are ever combined with it'], 0)]),
AF('Number Theory: The Prime Number Theorem',
   'Grade 12 Advanced Functions strand: the Prime Number Theorem describes the approximate distribution of prime numbers, stating that the number of primes less than a given number n is approximately n divided by the natural logarithm of n.',
   [('What does the Prime Number Theorem describe?', ['The approximate distribution of prime numbers', 'The exact location of every prime number', 'A method for factoring any polynomial', 'A rule for solving quadratic equations'], 0),
    ('According to the theorem, the number of primes less than n is approximately equal to ___.', ['n divided by the natural logarithm of n', 'n multiplied by 2', 'The square root of n', 'A fixed constant, regardless of n'], 0),
    ('As numbers get larger, what generally happens to the density of prime numbers?', ['Primes become relatively less frequent, though still infinite in number', 'Primes become increasingly more frequent with no limit', 'The number of primes suddenly stops entirely', 'Prime density remains exactly constant forever'], 0),
    ('The Prime Number Theorem connects number theory to which mathematical function?', ['The natural logarithm', 'The sine function', 'The tangent function', 'The absolute value function'], 0),
    ('Why is the Prime Number Theorem considered an important result in mathematics?', ['It gives mathematicians a way to estimate how primes are distributed among all integers', 'It proves that no prime numbers exist beyond a certain point', 'It has no connection to prime numbers at all', 'It only applies to even numbers'], 0)]),
CA('Calculus: The Heat Equation — Modelling Diffusion',
   'Grade 12 Calculus strand: the heat equation is a partial differential equation that models how temperature or another diffusing quantity spreads through a region over time, connecting calculus to physical processes like heat conduction.',
   [('What does the heat equation model?', ['How temperature or another diffusing quantity spreads through a region over time', 'The exact colour of an object at a fixed moment', 'The total mass of an object with no time dependence', 'A single, unchanging value with no variation over time'], 0),
    ('What type of equation is the heat equation?', ['A partial differential equation', 'A simple linear equation with one variable', 'A basic arithmetic equation with whole numbers', 'An equation with no variables at all'], 0),
    ('The heat equation connects calculus to which real-world physical process?', ['Heat conduction and diffusion', 'The reflection of light off a mirror', 'The motion of a planet around the sun', 'The vibration of a plucked string'], 0),
    ('What does the heat equation typically involve, in terms of derivatives?', ['Derivatives with respect to both time and spatial position', 'Only a derivative with respect to time, with no spatial component', 'Only a derivative with respect to space, with no time component', 'No derivatives are involved in the heat equation'], 0),
    ('Why might engineers use the heat equation in practical applications?', ['To predict how heat will spread through materials over time', 'The heat equation has no practical engineering applications', 'It can only describe objects that never change temperature', 'It is used exclusively for measuring sound waves'], 0)]),
PH('Physics: The Faraday Effect — Magneto-Optic Rotation',
   'Grade 12 Physics strand: the Faraday effect occurs when a strong magnetic field applied to certain materials causes the plane of polarization of light passing through them to rotate, revealing a direct interaction between magnetism and light.',
   [('What does the Faraday effect describe?', ['The rotation of the plane of polarization of light in a magnetic field', 'The bending of light due to gravity alone', 'The complete absorption of all light by a material', 'The reflection of light off a flat mirror'], 0),
    ('What is required to observe the Faraday effect in a material?', ['A strong magnetic field applied to the material', 'Only complete darkness with no light present', 'Only extremely high temperatures', 'Only a vacuum with no material present'], 0),
    ('What does the Faraday effect reveal about the relationship between light and magnetism?', ['A direct interaction between magnetic fields and the polarization of light', 'That light and magnetism never interact under any circumstances', 'That magnetism has no effect on light whatsoever', 'That light always travels in a perfectly straight, unaffected path near magnets'], 0),
    ('The Faraday effect is distinct from the earlier-studied Faraday cage because it involves ___.', ['The interaction of light with a magnetic field, rather than blocking electric fields', 'The exact same phenomenon with a different name only', 'Sound waves instead of light or electric fields', 'Gravity instead of magnetism'], 0),
    ('Why might scientists use the Faraday effect in modern technology?', ['To build optical devices that control or measure light using magnetic fields', 'The Faraday effect has no practical application in technology', 'It can only be observed in outer space', 'It is used exclusively to generate electricity from sunlight'], 0)]),
]),
day(118, [
E('Literature: Disability Studies and Representation in Fiction',
  'Grade 12 English strand: disability studies examines how literature represents disabled characters and experiences, questioning stereotypes and considering how narratives can either reinforce or challenge societal assumptions about disability.',
  [('What does disability studies examine in literature?', ['How literature represents disabled characters and experiences', 'Only the physical size of a printed book', 'Only unrelated statistics about book sales', 'Only the grammar used within a text'], 0),
   ('What might a disability studies critic question in a text?', ['Stereotypes and assumptions about disabled characters', 'Only the colour of the books cover', 'Only the number of pages in a novel', 'Only the authors preferred writing software'], 0),
   ('How can narratives potentially reinforce societal assumptions about disability?', ['By relying on limited or stereotypical portrayals of disabled characters', 'Narratives can never influence societal assumptions in any way', 'By always presenting complex, three-dimensional disabled characters with no exceptions', 'By avoiding any representation of disability altogether'], 0),
   ('Why might disability studies scholars value narratives written by disabled authors?', ['They can offer authentic perspectives often missing from mainstream portrayals', 'Authorship has no connection to how disability is represented', 'Disabled authors are never interested in writing about disability', 'These narratives are considered entirely irrelevant to literary study'], 0),
   ('Disability studies in literature connects to broader questions of ___.', ['Representation, identity, and social inclusion', 'Only unrelated topics in mathematics', 'Only the physical construction of buildings', 'Only historical weather patterns'], 0)]),
AF('Discrete Math: Farey Sequences and Mediants',
   'Grade 12 Advanced Functions strand: a Farey sequence lists all reduced fractions between 0 and 1 with denominators up to a given limit in increasing order, and the mediant of two neighbouring fractions provides a way to generate new fractions between them.',
   [('What does a Farey sequence list?', ['All reduced fractions between 0 and 1 with denominators up to a given limit', 'Only whole numbers between 0 and 100', 'Only negative fractions', 'Only fractions equal to exactly one half'], 0),
    ('How are the fractions arranged within a Farey sequence?', ['In increasing order', 'In completely random order', 'In decreasing order only', 'Grouped only by denominator with no numerical order'], 0),
    ('What is the mediant of two fractions a/b and c/d?', ['(a+c)/(b+d)', 'a/b multiplied by c/d', '(a/b) minus (c/d)', 'The average of the two denominators only'], 0),
    ('What can the mediant of two neighbouring fractions in a Farey sequence help generate?', ['A new fraction that lies between them', 'A fraction identical to one of the original two', 'A number outside the range of 0 to 1', 'A completely unrelated whole number'], 0),
    ('Farey sequences are studied within which broader area of mathematics?', ['Number theory', 'Only basic geometry', 'Only elementary statistics', 'Only trigonometry'], 0)]),
CA('Calculus: The Wave Equation — Modelling Vibration',
   'Grade 12 Calculus strand: the wave equation is a partial differential equation describing how disturbances, such as vibrations on a string or sound waves, propagate through space and time.',
   [('What does the wave equation model?', ['How disturbances, like vibrations, propagate through space and time', 'A single fixed value with no motion involved', 'The exact colour of a material', 'The total mass of a stationary object'], 0),
    ('What type of equation is the wave equation?', ['A partial differential equation', 'A simple linear equation with one variable', 'A basic arithmetic equation with whole numbers', 'An equation with no variables at all'], 0),
    ('Which of these physical phenomena can the wave equation help describe?', ['Vibrations on a string or the propagation of sound', 'The freezing point of water only', 'The colour of visible light only', 'The mass of a solid object at rest'], 0),
    ('The wave equation typically involves derivatives with respect to which two quantities?', ['Time and spatial position', 'Only colour and brightness', 'Only mass and volume', 'Only temperature and pressure'], 0),
    ('Why is the wave equation an important tool in physics and engineering?', ['It helps model and predict how waves behave and travel through different media', 'It has no real-world scientific application', 'It only applies to objects that never move', 'It can only describe completely silent, motionless systems'], 0)]),
PH('Physics: The Peltier Effect and Thermoelectric Cooling',
   'Grade 12 Physics strand: the Peltier effect occurs when an electric current flowing across a junction of two different materials causes heat to be absorbed on one side and released on the other, enabling thermoelectric cooling devices with no moving parts.',
   [('What happens during the Peltier effect?', ['An electric current across a junction causes heat to be absorbed on one side and released on the other', 'Heat is generated equally on both sides of a junction with no difference', 'A magnetic field is created with no thermal effect', 'Light is emitted from the junction with no heat transfer'], 0),
    ('What is required to produce the Peltier effect?', ['An electric current flowing across a junction of two different materials', 'Only sunlight, with no electrical current needed', 'Only a strong magnetic field, with no current required', 'Only extremely low pressure, with no current involved'], 0),
    ('What practical application relies on the Peltier effect?', ['Thermoelectric cooling devices', 'Devices that generate sound only', 'Devices that produce visible light only', 'Devices that measure gravitational force'], 0),
    ('What advantage do thermoelectric coolers based on the Peltier effect have over traditional refrigeration methods?', ['They can operate with no moving parts', 'They always require large amounts of moving mechanical parts', 'They cannot be powered by electricity', 'They can only function in outer space'], 0),
    ('The Peltier effect is closely related to which broader field of physics?', ['Thermoelectricity, the interaction between temperature and electricity', 'Only optics, the study of light', 'Only acoustics, the study of sound', 'Only nuclear physics, the study of atomic nuclei'], 0)]),
]),
day(119, [
E('Literature: Pastiche and Postmodern Imitation',
  'Grade 12 English strand: pastiche is a work that imitates the style of another author, genre, or period, often blending multiple influences together, distinguished from parody by its tendency to imitate without necessarily mocking its source.',
  [('What is pastiche?', ['A work that imitates the style of another author, genre, or period', 'A work that always mocks or ridicules its source', 'A completely original style with no outside influence', 'A type of punctuation used in formal writing'], 0),
   ('How does pastiche typically differ from parody?', ['Pastiche imitates without necessarily mocking its source, while parody often satirizes it', 'Pastiche and parody are identical with no distinction between them', 'Parody never involves any imitation of style', 'Pastiche always contains harsh criticism of its source'], 0),
   ('What might a postmodern pastiche blend together?', ['Multiple stylistic or genre influences within a single work', 'Only one single unchanging style throughout', 'No stylistic influences whatsoever', 'Only mathematical formulas with no literary content'], 0),
   ('Why might a postmodern author choose to write in pastiche?', ['To playfully engage with literary tradition and blend multiple voices or styles', 'Pastiche is never used by postmodern authors', 'To completely erase any connection to earlier literary works', 'To avoid any stylistic choices in their writing'], 0),
   ('Pastiche is often associated with which broader literary movement?', ['Postmodernism', 'Medieval literature', 'Ancient epic poetry', 'Victorian sentimental fiction exclusively'], 0)]),
AF('Number Theory: Zeckendorfs Theorem and Fibonacci Representations',
   'Grade 12 Advanced Functions strand: Zeckendorfs Theorem states that every positive integer can be represented uniquely as a sum of non-consecutive Fibonacci numbers, connecting the Fibonacci sequence to a distinctive form of number representation.',
   [('What does Zeckendorfs Theorem state?', ['Every positive integer can be uniquely represented as a sum of non-consecutive Fibonacci numbers', 'No integer can ever be represented using Fibonacci numbers', 'Only even numbers can be represented using Fibonacci numbers', 'Every integer has infinitely many different Fibonacci representations'], 0),
    ('What restriction does Zeckendorfs Theorem place on the Fibonacci numbers used?', ['They must be non-consecutive Fibonacci numbers', 'They must always be consecutive Fibonacci numbers', 'Only even-indexed Fibonacci numbers may be used', 'There is no restriction on which Fibonacci numbers can be used'], 0),
    ('What earlier sequence does Zeckendorfs Theorem rely on?', ['The Fibonacci sequence', 'The sequence of prime numbers', 'The sequence of perfect squares', 'The sequence of even numbers only'], 0),
    ('Why is the uniqueness of the Zeckendorf representation notable?', ['It means there is exactly one valid non-consecutive Fibonacci sum for each positive integer', 'It means there are infinitely many valid representations for every integer', 'It means no representation exists for most integers', 'Uniqueness has no mathematical significance in this context'], 0),
    ('Zeckendorfs Theorem is an example of connecting number theory to ___.', ['A specific, structured way of representing numbers', 'A completely unrelated branch of geometry', 'A rule with no mathematical basis', 'A method used only in basic arithmetic with whole numbers'], 0)]),
CA('Calculus: The Brachistochrone Problem and the Calculus of Variations',
   'Grade 12 Calculus strand: the brachistochrone problem asks for the curve along which a particle slides fastest between two points under gravity alone, famously solved to be a cycloid, and it helped launch the calculus of variations, a field concerned with finding functions that optimize a quantity.',
   [('What does the brachistochrone problem ask for?', ['The curve along which a particle slides fastest between two points', 'The shortest possible straight-line distance between two points', 'The curve with the largest possible area underneath it', 'A curve that never changes in shape'], 0),
    ('What shape is the solution to the classic brachistochrone problem?', ['A cycloid', 'A perfect circle', 'A straight line', 'A parabola'], 0),
    ('What field of mathematics did the brachistochrone problem help establish?', ['The calculus of variations', 'Basic arithmetic', 'Elementary geometry', 'Simple linear algebra'], 0),
    ('What is the calculus of variations generally concerned with?', ['Finding functions that optimize (maximize or minimize) a certain quantity', 'Only solving basic single-variable equations', 'Only measuring simple, fixed lengths', 'Only counting whole numbers'], 0),
    ('Why might a straight line not be the fastest path in the brachistochrone problem, even though it is the shortest?', ['A curved path can allow the particle to gain speed more quickly under gravity', 'A straight line is always both the shortest and fastest path with no exception', 'Gravity has no effect on the speed of the particle', 'The particle never moves at all along a straight path'], 0)]),
PH('Physics: The Kinetic Theory of Gases',
   'Grade 12 Physics strand: the kinetic theory of gases explains the macroscopic properties of gases, such as pressure and temperature, as arising from the constant, random motion and collisions of countless individual gas particles.',
   [('What does the kinetic theory of gases explain?', ['Macroscopic gas properties as arising from the motion of individual particles', 'Only the colour of a gas at room temperature', 'Only the taste of a gas', 'Only the exact number of particles in a container'], 0),
    ('According to kinetic theory, what are gas particles constantly doing?', ['Moving randomly and colliding with each other and their container', 'Remaining perfectly still with no motion at all', 'Only moving in a single straight line with no collisions', 'Only vibrating in place with no translational motion'], 0),
    ('How does kinetic theory explain gas pressure?', ['As the result of particles colliding with the walls of their container', 'Pressure has no connection to particle motion at all', 'Pressure is caused only by the colour of the gas', 'Pressure exists only in solids, never in gases'], 0),
    ('How does kinetic theory relate particle motion to temperature?', ['Higher temperature generally corresponds to greater average particle kinetic energy', 'Temperature has no relationship to particle motion whatsoever', 'Higher temperature always means particles move more slowly', 'Temperature depends only on the colour of the container'], 0),
    ('The kinetic theory of gases provides a microscopic explanation for which macroscopic gas laws?', ['Laws like Boyles Law and Charless Law', 'Only laws related to solids, never gases', 'Only laws related to light and optics', 'Only laws related to magnetism'], 0)]),
]),
day(120, [
E('English Review: Literary Theory and Poetic Form',
  'Grade 12 English strand review: students revisit structuralism, New Criticism, ecofeminism, prosody and meter, the Romantic sublime, the Theatre of Cruelty, biographical criticism, disability studies, and pastiche.',
  [('What does structuralism examine in a text?', ['Underlying systems of signs and structures that generate meaning', 'Only the authors personal biography', 'Only the historical period a text was written in', 'Only the emotional response of individual readers'], 0),
   ('What does New Criticism emphasize when analyzing a text?', ['Close reading of the text on its own terms', 'Only the authors personal life and biography', 'Only the historical period surrounding the text', 'Only the readers personal emotional reaction'], 0),
   ('What is meter in poetry?', ['The patterned arrangement of stressed and unstressed syllables', 'The total number of words in a poem', 'A type of poem with no rhythm at all', 'A citation style used in essays'], 0),
   ('Who developed the concept known as the Theatre of Cruelty?', ['Antonin Artaud', 'William Shakespeare', 'Bertolt Brecht', 'Henrik Ibsen'], 0),
   ('What is pastiche?', ['A work that imitates the style of another author, genre, or period', 'A work that always mocks or ridicules its source', 'A completely original style with no outside influence', 'A type of punctuation used in formal writing'], 0)]),
AF('AdvancedFunctions Review: Famous Conjectures and Number Theory',
   'Grade 12 Advanced Functions strand review: students revisit the Goldbach Conjecture, the Twin Prime Conjecture, Pells Equation, Fermats Last Theorem, the Collatz Conjecture, Gaussian integers, the Prime Number Theorem, Farey sequences, and Zeckendorfs Theorem.',
   [('What does the Goldbach Conjecture propose?', ['Every even integer greater than 2 can be written as the sum of two primes', 'Every odd integer can be written as the sum of two primes', 'No even number can ever be written as a sum of primes', 'All prime numbers are even'], 0),
    ('Which of these is an example of twin primes?', ['11 and 13', '2 and 7', '4 and 6', '9 and 12'], 0),
    ('Who finally proved Fermats Last Theorem?', ['Andrew Wiles', 'Isaac Newton', 'Pythagoras', 'Leonhard Euler'], 0),
    ('According to the Collatz Conjecture, where does this process always eventually lead?', ['The number 1', 'The number 0', 'A number that increases forever with no end', 'A negative number'], 0),
    ('What does Zeckendorfs Theorem state?', ['Every positive integer can be uniquely represented as a sum of non-consecutive Fibonacci numbers', 'No integer can ever be represented using Fibonacci numbers', 'Only even numbers can be represented using Fibonacci numbers', 'Every integer has infinitely many different Fibonacci representations'], 0)]),
CA('Calculus Review: Multivariable Techniques and Special Functions',
   'Grade 12 Calculus strand review: students revisit triple integrals in spherical coordinates, the Beta function, Fubinis Theorem, the Cauchy-Riemann equations, the Residue Theorem, the Dirac delta function, the heat equation, the wave equation, and the brachistochrone problem.',
   [('What three variables are used in spherical coordinates?', ['Rho, theta, and phi', 'Only x, y, and z', 'Only r and theta', 'Only length and width'], 0),
    ('What does Fubinis Theorem allow for a double integral over a suitable region?', ['Evaluating it as an iterated integral in either order', 'Only evaluating it in one fixed, unchangeable order', 'Eliminating the need to integrate at all', 'Only applying to integrals with no variables'], 0),
    ('What must a complex function satisfy to be differentiable in the complex sense?', ['The Cauchy-Riemann equations', 'Only the standard rules of real-number multiplication', 'Only the Pythagorean theorem', 'No conditions are required at all'], 0),
    ('What does the Dirac delta function model in mathematics and physics?', ['An idealized point source or impulse', 'A gradual, smooth change over a wide interval', 'A constant value with no variation', 'A function with no defined properties at all'], 0),
    ('What shape is the solution to the classic brachistochrone problem?', ['A cycloid', 'A perfect circle', 'A straight line', 'A parabola'], 0)]),
PH('Physics Review: Historic Experiments and Classical Effects',
   'Grade 12 Physics strand review: students revisit the Davisson-Germer experiment, the Foucault pendulum, the Cavendish experiment, the Hall effect, the Coriolis effect, Brownian motion, the Faraday effect, the Peltier effect, and the kinetic theory of gases.',
   [('What did the Davisson-Germer experiment demonstrate?', ['That electrons produce diffraction patterns, showing wave-like behaviour', 'That electrons have no measurable properties at all', 'That light behaves only as a particle with no wave nature', 'That protons are the only particles with wave properties'], 0),
    ('What did the Foucault pendulum famously demonstrate?', ['Earths rotation', 'The existence of gravity', 'The speed of light', 'The structure of the atom'], 0),
    ('What important physical constant did the Cavendish experiment help determine?', ['The gravitational constant, G', 'The speed of light', 'The charge of an electron', 'The mass of a proton'], 0),
    ('What did Einstein propose as the cause of Brownian motion in 1905?', ['Countless collisions with fast-moving molecules in the fluid', 'A hidden magnetic field acting on the particles', 'Sound waves pushing the particles around', 'Gravity alone, with no molecular involvement'], 0),
    ('According to kinetic theory, what are gas particles constantly doing?', ['Moving randomly and colliding with each other and their container', 'Remaining perfectly still with no motion at all', 'Only moving in a single straight line with no collisions', 'Only vibrating in place with no translational motion'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g12_111_120)
    append_to(12, g12_111_120)
