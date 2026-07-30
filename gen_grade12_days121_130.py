#!/usr/bin/env python3
"""Grade 12, Days 121-130 -- extends Grade 12 from 120 to 130 days. Topics
chosen after reviewing the full existing Day 1-120 title list (see
data/grade12.json) to avoid any overlap: the sonnet, the ode, the
picaresque novel, autofiction, Russian Formalism and defamiliarization,
Noh and Kabuki theatre, the book proposal, video game narrative, and
parallelism and the rhetorical triad; Carmichael numbers, the Ackermann
function, the Lambert W function, Latin squares, the Cauchy functional
equation, quadratic residues and the Legendre symbol, the twelvefold
way, Padé approximants, and the Frobenius coin problem; the envelope
theorem, the Hessian matrix and the multivariable second-derivative
test, gradient vectors and directional derivatives, arc length of a
polar curve, the limit comparison test, Abel's Theorem, the midpoint
rule, Bessel functions, and the Leibniz rule for differentiating under
the integral sign; the Pauli exclusion principle, the Mössbauer effect,
the Gibbs paradox, nuclear magnetic resonance, piezoelectricity, the
physics of rainbows, sonic booms, magnetohydrodynamics, and the
barometric formula. Day 130 is a comprehensive review day across all
four subjects.

Subject keys for Grade 12 are "English", "AdvancedFunctions",
"Calculus", "Physics" (same as all earlier Grade 12 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote or straight-apostrophe characters are
used anywhere in title/question/summary/option text; apostrophes are
avoided entirely, matching the convention used in the Days 111-120
batch.
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


g12_121_130 = [
day(121, [
E('Poetry: The Sonnet — Form, Volta, and the Petrarchan Tradition',
  'Grade 12 English strand: the sonnet is a fourteen-line poem traditionally built around a turn in argument or feeling called the volta, with the Petrarchan form dividing into an octave and sestet and the Shakespearean form closing with a rhymed couplet.',
  [('How many lines does a traditional sonnet contain?', ['Fourteen', 'Ten', 'Twelve', 'Sixteen'], 0),
   ('What is the volta in a sonnet?', ['A turn in argument or feeling partway through the poem', 'The title of the poem', 'A rhyme scheme with no meaning', 'A type of stanza break with no thematic function'], 0),
   ('How does the Petrarchan sonnet typically divide?', ['Into an octave and a sestet', 'Into three quatrains only', 'Into a single unbroken stanza', 'Into twenty short lines'], 0),
   ('How does the Shakespearean sonnet typically end?', ['With a rhymed couplet', 'With a question mark and no resolution', 'With a chorus repeated from the octave', 'With a stage direction'], 0),
   ('Why might a poet choose the sonnet form for a poem about conflicted feelings?', ['Its turn, or volta, mirrors a shift or tension within the thought itself', 'The sonnet form forbids any change in tone', 'Sonnets can never address emotional conflict', 'The form has no relationship to the content of a poem'], 0)]),
AF('Number Theory: Carmichael Numbers and Pseudoprimes',
   'Grade 12 Advanced Functions strand: a Carmichael number is a composite number that nonetheless satisfies Fermats Little Theorem for every base coprime to it, making it a pseudoprime that can fool simple primality tests.',
   [('What is a Carmichael number?', ['A composite number that satisfies Fermats Little Theorem for every coprime base', 'A prime number with no special properties', 'A number that is always divisible by two', 'A fraction between zero and one'], 0),
    ('Why are Carmichael numbers called pseudoprimes?', ['They can pass certain primality tests despite not actually being prime', 'They are always confirmed to be truly prime', 'They have no relationship to primality testing', 'They are only ever equal to zero'], 0),
    ('Which theorem do Carmichael numbers satisfy despite being composite?', ['Fermats Little Theorem', 'The Pythagorean theorem', 'The binomial theorem', 'The fundamental theorem of algebra'], 0),
    ('Why are Carmichael numbers significant for computer science and cryptography?', ['They reveal limitations of simple primality tests based on Fermats Little Theorem', 'They have no relevance to computer science at all', 'They guarantee that every primality test is completely accurate', 'They are used only in elementary arithmetic classes'], 0),
    ('What must be true of the base numbers used when testing a Carmichael number against Fermats Little Theorem?', ['The base must be coprime to the Carmichael number', 'The base must always equal the Carmichael number itself', 'The base must always be an even number', 'The base has no requirement whatsoever'], 0)]),
CA('Calculus: The Envelope Theorem in Constrained Optimization',
   'Grade 12 Calculus strand: the envelope theorem describes how the optimal value of a constrained optimization problem changes as a parameter of the problem changes, showing that this rate of change can be computed directly from the partial derivative of the objective (or Lagrangian) function, without re-solving the entire optimization.',
   [('What does the envelope theorem describe?', ['How the optimal value of a constrained optimization problem changes as a parameter changes', 'The exact solution of any equation with no parameters', 'A method for graphing a single linear function', 'A rule for counting whole numbers only'], 0),
    ('According to the envelope theorem, how can the rate of change of the optimal value often be found?', ['Directly from the partial derivative of the objective or Lagrangian function', 'Only by re-solving the entire optimization problem from scratch every time', 'By ignoring the constraint entirely', 'By measuring the problem with a physical ruler'], 0),
    ('In what type of problem does the envelope theorem commonly appear?', ['Constrained optimization problems, such as those using Lagrange multipliers', 'Simple single-variable arithmetic with no optimization', 'Basic counting problems with no calculus involved', 'Problems with no parameters of any kind'], 0),
    ('Why is the envelope theorem useful in economics and applied optimization?', ['It allows analysts to see how the optimal outcome responds to changing conditions without fully resolving the problem each time', 'It has no application outside of pure mathematics', 'It always requires ignoring the objective function', 'It eliminates the need for any optimization at all'], 0),
    ('The envelope theorem builds most directly on which earlier optimization technique from this course?', ['Lagrange multipliers', 'The power rule for basic derivatives', 'The trapezoid rule for numerical integration', 'The ratio test for series'], 0)]),
PH('Physics: The Pauli Exclusion Principle and the Structure of Matter',
   'Grade 12 Physics strand: the Pauli exclusion principle states that no two identical fermions, such as electrons within a single atom, can occupy the same quantum state simultaneously, a rule that underlies the shell structure of atoms and the stability of ordinary matter.',
   [('What does the Pauli exclusion principle state?', ['No two identical fermions can occupy the same quantum state simultaneously', 'All particles must occupy exactly the same quantum state', 'Only protons are affected by exclusion rules', 'Exclusion rules apply only to photons'], 0),
    ('Which category of particles does the Pauli exclusion principle apply to?', ['Fermions, such as electrons', 'Only massless particles such as photons', 'Only particles with no charge', 'Only particles found outside of atoms'], 0),
    ('What atomic feature does the Pauli exclusion principle help explain?', ['The shell structure of electrons within an atom', 'The colour of an atoms nucleus', 'The total mass of a proton', 'The existence of magnetic fields in empty space'], 0),
    ('Why is the Pauli exclusion principle important for the stability of ordinary matter?', ['It prevents electrons from collapsing into the same lowest-energy state, giving atoms their structure and volume', 'It causes all matter to instantly collapse into a single point', 'It has no effect on the structure of atoms', 'It applies only to stars, never to ordinary atoms'], 0),
    ('The Pauli exclusion principle is closely connected to which broader physical property of electrons?', ['Spin, a quantum property that helps define their quantum state', 'Their exact position at every instant, known with total certainty', 'Their colour, which varies from atom to atom', 'Their temperature, which determines exclusion'], 0)]),
]),
day(122, [
E('Poetry: The Ode — Public Voice and Elevated Address',
  'Grade 12 English strand: the ode is a lyric poem written in an elevated, formal style to praise or meditate on a person, event, or abstract idea, often adopting a public voice distinct from more private lyric forms.',
  [('What does an ode typically do?', ['Praises or meditates on a person, event, or abstract idea in an elevated style', 'Tells a long adventure story with a plot', 'Provides step-by-step instructions', 'Lists facts with no emotional tone'], 0),
   ('What kind of voice does an ode often adopt?', ['A public, formal voice, distinct from more private lyric address', 'A voice that only whispers private secrets', 'A voice with no distinct tone at all', 'A strictly comedic, mocking voice'], 0),
   ('Which classical tradition strongly influenced the English ode?', ['The Greek and Roman lyric tradition', 'The medieval epic tradition alone', 'Twentieth-century free verse alone', 'The tradition of prose fiction'], 0),
   ('An ode addressed to an abstract idea, such as beauty or autumn, treats that idea as ___.', ['Worthy of direct, formal address, almost as though it could listen', 'Something too trivial to write about', 'A character with a full narrative plot', 'A rule of grammar'], 0),
   ('How does the tone of an ode typically differ from a casual, conversational poem?', ['The ode is more formal and elevated in diction and structure', 'There is no difference in tone between the two', 'The ode is always comedic and irreverent', 'The ode avoids any emotional content whatsoever'], 0)]),
AF('Discrete Math: The Ackermann Function and Uncomputable Growth',
   'Grade 12 Advanced Functions strand: the Ackermann function is a recursively defined function that grows dramatically faster than any exponential or polynomial function, providing a classic example of a function that is computable yet not primitive recursive.',
   [('How is the Ackermann function typically defined?', ['Recursively, using nested applications of itself', 'As a simple linear equation', 'As a function with a fixed, constant output', 'Only through a lookup table with no formula'], 0),
    ('How does the growth rate of the Ackermann function compare to exponential functions?', ['It grows dramatically faster than exponential or polynomial functions', 'It grows more slowly than a linear function', 'It grows at exactly the same rate as a constant function', 'It never grows at all'], 0),
    ('What is the Ackermann function a classic example of in computability theory?', ['A function that is computable but not primitive recursive', 'A function that cannot be computed under any circumstances', 'A function identical to simple addition', 'A function with no mathematical definition'], 0),
    ('Why might the Ackermann function be used to test computer algorithms?', ['Its explosive growth rate stresses recursive computation and memory limits', 'It has no practical use in testing computation', 'It always produces the same small output regardless of input', 'It is unrelated to recursion entirely'], 0),
    ('The Ackermann function is often introduced alongside which broader topic?', ['Recursion and the limits of computable functions', 'Basic addition facts for young learners', 'Simple linear graphing', 'Elementary geometry'], 0)]),
CA('Calculus: The Hessian Matrix and the Second-Derivative Test for Multivariable Functions',
   'Grade 12 Calculus strand: the Hessian matrix collects the second-order partial derivatives of a multivariable function, and examining its properties at a critical point extends the familiar single-variable second-derivative test to classify that point as a local maximum, local minimum, or saddle point.',
   [('What does the Hessian matrix collect?', ['The second-order partial derivatives of a multivariable function', 'Only the first-order partial derivatives', 'A list of the functions input values', 'The constants found within the function'], 0),
    ('What can examining the Hessian matrix at a critical point help classify?', ['Whether the point is a local maximum, local minimum, or saddle point', 'The exact numerical value of the function everywhere', 'The domain of the function only', 'The colour used in a graph of the function'], 0),
    ('What earlier single-variable concept does the Hessian-based test extend?', ['The second-derivative test for concavity and extrema', 'The chain rule for derivatives', 'The trapezoid rule for numerical integration', 'The ratio test for series convergence'], 0),
    ('What is a saddle point, as classified using the Hessian matrix?', ['A critical point that is neither a local maximum nor a local minimum', 'A point where the function is always undefined', 'A point identical to a local maximum in every case', 'A point that only occurs in one-variable functions'], 0),
    ('Why is the Hessian matrix especially useful for functions of two or more variables?', ['Curvature in multiple directions must be considered simultaneously to classify a critical point', 'Multivariable functions never have critical points', 'A single derivative is always sufficient for any multivariable function', 'The Hessian matrix only applies to linear functions'], 0)]),
PH('Physics: The Mössbauer Effect and Nuclear Resonance Fluorescence',
   'Grade 12 Physics strand: the Mössbauer effect occurs when atomic nuclei bound within a solid crystal emit or absorb gamma rays without loss of energy to recoil, enabling extremely precise measurements of small energy shifts, including tests of gravitational redshift.',
   [('What does the Mössbauer effect involve?', ['Nuclei bound in a solid crystal emitting or absorbing gamma rays without energy loss to recoil', 'The complete absorption of all visible light by a crystal', 'A magnetic field generated by a rotating nucleus', 'A change in the mass of a nucleus over time'], 0),
    ('Why is recoil normally a problem when a free nucleus emits a gamma ray?', ['Recoil carries away some of the gamma ray energy, shifting its frequency away from resonance', 'Recoil always increases the gamma ray energy without limit', 'Recoil has no effect on emitted radiation whatsoever', 'Recoil only affects visible light, never gamma rays'], 0),
    ('Why does being bound within a crystal lattice reduce the effect of recoil?', ['The recoil momentum is absorbed by the much more massive crystal as a whole rather than the single nucleus', 'Being bound in a crystal has no effect on nuclear recoil', 'Crystals eliminate gamma ray emission entirely', 'Crystals always increase the recoil energy of a nucleus'], 0),
    ('What historic type of experiment famously used the Mössbauer effect to test a prediction of general relativity?', ['A test of gravitational redshift', 'A test of the speed of sound in solids', 'A test of the charge of the electron', 'A test of Newtons third law'], 0),
    ('What makes the Mössbauer effect valuable for precision measurement?', ['It allows extremely small shifts in gamma ray energy to be detected reliably', 'It removes the need for any precise measurement at all', 'It only works with visible light, never gamma rays', 'It cannot detect any change in energy whatsoever'], 0)]),
]),
day(123, [
E('Literature: The Picaresque Novel — The Rogues Journey',
  'Grade 12 English strand: the picaresque novel follows a roguish, low-born protagonist through a loosely connected series of episodic adventures, using satire and social observation to expose the corruption of the society the protagonist travels through.',
  [('What kind of protagonist is typical of a picaresque novel?', ['A roguish, low-born character who lives by wit rather than status', 'A noble hero destined to rule a kingdom', 'A detective solving a single central mystery', 'A narrator who never interacts with other characters'], 0),
   ('How is the plot of a picaresque novel typically structured?', ['As a loosely connected series of episodic adventures', 'As a single, tightly unified three-act plot', 'As a strict chronological courtroom drama', 'As a poem with no narrative content'], 0),
   ('What social function does the picaresque form often serve?', ['Satirizing and exposing corruption in the society the protagonist travels through', 'Celebrating the nobility with no criticism', 'Avoiding any commentary on society whatsoever', 'Providing a technical manual for a trade'], 0),
   ('Why might episodic structure suit the picaresque novel?', ['It allows the rogue protagonist to move through many different social settings and encounters', 'Episodic structure prevents any social commentary', 'A picaresque novel can only describe a single location', 'Episodic structure removes the need for a protagonist'], 0),
   ('The term picaresque comes from a Spanish word associated with which kind of figure?', ['A picaro, or rogue', 'A king or queen', 'A saint', 'A soldier'], 0)]),
AF('Functions: The Lambert W Function and Inverse Exponentials',
   'Grade 12 Advanced Functions strand: the Lambert W function is defined as the inverse of the function f(w) equals w times e to the power w, providing a way to solve equations in which the unknown appears both inside and outside an exponential expression.',
   [('The Lambert W function is defined as the inverse of which expression?', ['w times e to the power w', 'w plus e', 'w divided by e', 'e raised to the power of w squared'], 0),
    ('What kind of equations can the Lambert W function help solve?', ['Equations where the unknown appears both inside and outside an exponential expression', 'Only simple linear equations with one term', 'Only equations with no exponential component', 'Only equations involving whole numbers less than ten'], 0),
    ('Why is the Lambert W function considered useful in advanced function study?', ['It extends the toolkit for solving equations that ordinary algebra cannot isolate directly', 'It has no practical use in solving equations', 'It only applies to equations with a single constant term', 'It eliminates the need for exponential functions entirely'], 0),
    ('What relationship does the Lambert W function have to the exponential function?', ['It acts as an inverse in a specific sense, undoing an expression involving an exponential', 'It has no relationship to exponential functions at all', 'It is identical to the exponential function in every case', 'It only applies to logarithms, never exponentials'], 0),
    ('In which types of real-world problems might the Lambert W function appear?', ['Problems involving growth processes where a variable multiplies its own exponential', 'Problems involving only whole-number counting', 'Problems with no variables at all', 'Problems limited strictly to geometry'], 0)]),
CA('Calculus: Gradient Vectors and Directional Derivatives',
   'Grade 12 Calculus strand: the gradient of a multivariable function is a vector of its partial derivatives that points in the direction of steepest increase, and the directional derivative measures the rate of change of the function along any chosen direction, computed as the dot product of the gradient with a unit vector.',
   [('What does the gradient vector of a function consist of?', ['A vector of the functions partial derivatives', 'A single number representing the functions maximum value', 'A list of the functions input variables only', 'A matrix of second-order derivatives'], 0),
    ('In which direction does the gradient vector point?', ['The direction of steepest increase of the function', 'The direction of steepest decrease of the function, always', 'A fixed direction unrelated to the function', 'No particular direction at all'], 0),
    ('What does a directional derivative measure?', ['The rate of change of a function along a chosen direction', 'The total area under a curve', 'The maximum value a function can ever reach', 'The number of critical points of a function'], 0),
    ('How is the directional derivative computed using the gradient?', ['As the dot product of the gradient with a unit vector in the chosen direction', 'As the sum of every partial derivative with no direction considered', 'As the product of the gradient with itself', 'As the square root of the gradient vector'], 0),
    ('Why is the gradient useful in optimization problems, such as gradient descent methods?', ['Moving opposite to the gradient decreases the function most rapidly, guiding a search for a minimum', 'The gradient has no relevance to finding minimum or maximum values', 'The gradient always points toward the origin regardless of the function', 'Gradient-based methods cannot be applied to multivariable functions'], 0)]),
PH('Physics: The Gibbs Paradox and the Entropy of Mixing',
   'Grade 12 Physics strand: the Gibbs paradox arises in classical statistical mechanics when calculating the entropy of mixing two samples of the same gas, appearing to predict a nonzero increase in entropy even though mixing identical, indistinguishable gases should produce no real physical change, a puzzle resolved by properly accounting for particle indistinguishability.',
   [('What situation gives rise to the Gibbs paradox?', ['Calculating the entropy of mixing two samples of the same, identical gas', 'Calculating the entropy of two entirely different, distinguishable gases', 'Measuring the temperature of a single isolated particle', 'Measuring the pressure of a vacuum'], 0),
    ('What does the naive classical calculation in the Gibbs paradox seem to predict?', ['A nonzero increase in entropy even when mixing identical gases', 'Zero change in entropy under all circumstances', 'A decrease in entropy when mixing any two gases', 'An undefined entropy value with no numerical meaning'], 0),
    ('Why is this prediction considered paradoxical?', ['Mixing identical, indistinguishable gas samples should produce no real physical change', 'Mixing identical gases always produces an obvious physical change', 'Entropy is never expected to change during any physical process', 'The paradox has no connection to physical reasoning'], 0),
    ('What key idea resolves the Gibbs paradox?', ['Properly accounting for the indistinguishability of identical particles', 'Assuming that all gas particles are entirely distinguishable from one another', 'Ignoring entropy calculations entirely', 'Assuming that gases never actually mix'], 0),
    ('The Gibbs paradox is most closely associated with which branch of physics?', ['Statistical mechanics and thermodynamics', 'Optics and the study of light', 'Nuclear physics and radioactive decay', 'Electromagnetism and circuit theory'], 0)]),
]),
day(124, [
E('Literature: Autofiction — Blurring Author and Narrator',
  'Grade 12 English strand: autofiction is a hybrid literary form in which an author writes fiction that draws directly on their own lived experience, deliberately blurring the boundary between autobiography and invented narrative.',
  [('What does autofiction blend together?', ['Autobiography and invented, fictional narrative', 'Poetry and technical writing', 'Drama and journalism with no overlap', 'History textbooks and legal documents'], 0),
   ('How does autofiction typically treat the relationship between author and narrator?', ['It deliberately blurs the line between the two', 'It always keeps them entirely separate and unrelated', 'It removes the narrator from the text completely', 'It requires the narrator to be a different gender than the author'], 0),
   ('Why might a writer choose autofiction rather than straightforward autobiography?', ['Fiction allows shaping, invention, and reflection that strict factual memoir may not', 'Autofiction is required to contain zero true events', 'Autofiction eliminates the need for a narrator', 'Autofiction can never include the authors own experiences'], 0),
   ('What effect can autofiction have on a reader?', ['Uncertainty about how much of the narrative reflects real events', 'Complete certainty that every detail is invented', 'Complete certainty that every detail is strictly factual', 'No effect, since readers ignore the authors identity entirely'], 0),
   ('Autofiction is often discussed alongside which broader literary trend?', ['Contemporary experiments with narrative form and identity', 'Medieval epic conventions', 'Strict adherence to traditional genre boundaries', 'The complete absence of a narrator'], 0)]),
AF('Discrete Math: Latin Squares and Combinatorial Designs',
   'Grade 12 Advanced Functions strand: a Latin square is an n by n grid filled with n different symbols so that each symbol appears exactly once in every row and every column, forming the basis for combinatorial designs used in experiment planning and puzzle construction.',
   [('What defines a Latin square?', ['An n by n grid where each symbol appears exactly once in every row and column', 'A grid where symbols may repeat freely within a row', 'A triangular arrangement of numbers', 'A grid with only one row and one column'], 0),
    ('How many times does each symbol appear in a single row of a Latin square?', ['Exactly once', 'Exactly twice', 'As many times as there are columns', 'Zero times'], 0),
    ('What everyday puzzle is closely related to the structure of a Latin square?', ['Sudoku', 'Crossword puzzles', 'Word searches', 'Anagram puzzles'], 0),
    ('In what field are Latin squares used to help plan fair experiments?', ['Statistics and experimental design', 'Elementary arithmetic', 'Basic geometry', 'Musical composition'], 0),
    ('Why might a researcher use a Latin square design when testing multiple treatments and subjects?', ['It helps control for confounding factors by balancing treatments across rows and columns', 'Latin squares always introduce unnecessary bias', 'Latin square designs cannot be used with more than one treatment', 'They have no use in experimental design'], 0)]),
CA('Calculus: Arc Length of a Polar Curve',
   'Grade 12 Calculus strand: the arc length of a curve given in polar coordinates is found by integrating an expression involving both the radius r as a function of theta and its derivative with respect to theta, extending arc length calculations beyond curves expressed in Cartesian form.',
   [('In what coordinate system is a polar curve expressed?', ['Polar coordinates, using radius and angle', 'Only Cartesian coordinates, using x and y', 'Only spherical coordinates', 'Only cylindrical coordinates'], 0),
    ('What two quantities appear in the formula for the arc length of a polar curve?', ['The radius r as a function of theta and its derivative with respect to theta', 'Only the angle theta, with no radius involved', 'Only the x and y coordinates, with no polar terms', 'Only a constant with no variable quantities'], 0),
    ('How does finding arc length in polar coordinates relate to the Cartesian arc length formula studied earlier?', ['Both integrate an expression built from a curves rate of change, adapted to the relevant coordinate system', 'The two formulas are entirely unrelated to one another', 'Polar arc length never requires any integration', 'Cartesian arc length cannot be extended to polar curves under any circumstances'], 0),
    ('Why might arc length in polar coordinates be useful when studying a curve such as a spiral?', ['Spirals are naturally and simply described using polar coordinates, making the polar arc length formula convenient', 'Spirals cannot be described using polar coordinates at all', 'Arc length has no meaning for a spiral shape', 'Polar coordinates can only describe straight lines'], 0),
    ('What must typically be done before applying the polar arc length formula to a curve given in Cartesian form?', ['Convert the curve into polar coordinates first', 'Nothing, since the formula applies without any conversion', 'The curve must be converted into a single point', 'The curve must be proven to have no length'], 0)]),
PH('Physics: Nuclear Magnetic Resonance and Spin Precession',
   'Grade 12 Physics strand: nuclear magnetic resonance occurs when certain atomic nuclei placed in a strong magnetic field absorb and re-emit radio-frequency energy as their spin precesses around the field direction, a phenomenon that underlies medical magnetic resonance imaging.',
   [('What is required to produce nuclear magnetic resonance in a sample?', ['A strong external magnetic field applied to nuclei with a suitable spin', 'Only visible light, with no magnetic field required', 'Only extremely high pressure, with no magnetic field involved', 'A complete absence of any external field'], 0),
    ('What does the term precession describe in this context?', ['The wobbling motion of a nuclear spin around the direction of an applied magnetic field', 'A nucleus moving in a perfectly straight line with no rotation', 'A nucleus that remains entirely motionless', 'A change in the electric charge of a nucleus'], 0),
    ('What type of energy do nuclei absorb and re-emit during nuclear magnetic resonance?', ['Radio-frequency electromagnetic energy', 'Gamma-ray energy exclusively', 'Purely mechanical sound energy', 'Only thermal energy with no electromagnetic component'], 0),
    ('What widely used medical technology relies on the principles of nuclear magnetic resonance?', ['Magnetic resonance imaging (MRI)', 'X-ray radiography', 'Ultrasound imaging', 'Positron emission tomography using only gamma detection'], 0),
    ('Why is nuclear magnetic resonance sensitive to the chemical environment surrounding a nucleus?', ['Nearby electrons and atoms slightly shift the effective magnetic field experienced by the nucleus', 'The chemical environment has no effect on nuclear spin behaviour', 'Only the total mass of the sample affects the resonance signal', 'Resonance only depends on the colour of the sample'], 0)]),
]),
day(125, [
E('Literary Theory: Russian Formalism and Defamiliarization',
  'Grade 12 English strand: Russian Formalism approached literature as a set of specific artistic devices and techniques, introducing the concept of defamiliarization, whereby familiar objects or experiences are presented in an unfamiliar way to renew perception.',
  [('What did Russian Formalist critics focus on when studying literature?', ['Specific artistic devices and techniques used within a text', 'Only the biography of the author', 'Only the historical period of publication', 'Only the readers emotional response'], 0),
   ('What is defamiliarization?', ['Presenting familiar objects or experiences in an unfamiliar way to renew perception', 'Making a text as familiar and predictable as possible', 'Removing all imagery from a text', 'A term unrelated to literary technique'], 0),
   ('Why might a Formalist critic value defamiliarization in literature?', ['It disrupts habitual perception and makes readers notice a subject freshly', 'It ensures readers never notice anything new', 'It removes all artistic devices from a text', 'It guarantees a text will be forgettable'], 0),
   ('Russian Formalism was an important precursor to which later critical movement discussed elsewhere in this course?', ['Structuralism', 'Romanticism', 'Victorian sentimentalism', 'Medieval allegory'], 0),
   ('According to Formalist thinking, what makes a text literary rather than ordinary language?', ['The deliberate, patterned use of devices that set it apart from everyday speech', 'Literary and ordinary language are considered identical', 'A texts length alone determines its literariness', 'Only the authors fame determines literariness'], 0)]),
AF('Functions: The Cauchy Functional Equation',
   'Grade 12 Advanced Functions strand: the Cauchy functional equation, f(x + y) equals f(x) plus f(y), characterizes linear functions of the form f(x) equals kx among well-behaved (such as continuous) functions, while admitting far stranger solutions if continuity is not assumed.',
   [('What is the general form of the Cauchy functional equation?', ['f(x + y) = f(x) + f(y)', 'f(x times y) = f(x) plus f(y)', 'f(x) = x squared', 'f(x + y) = f(x) times f(y)'], 0),
    ('Among continuous functions, what form do solutions to the Cauchy functional equation take?', ['f(x) = kx, a linear function through the origin', 'f(x) = x squared, a quadratic function', 'f(x) = the constant one, for every input', 'No continuous solutions exist at all'], 0),
    ('What happens to the set of possible solutions if continuity is not assumed?', ['Far stranger, highly irregular solutions become possible', 'The only possible solution becomes f(x) = 0', 'No solutions exist under any condition', 'The equation becomes impossible to define'], 0),
    ('What kind of equation is the Cauchy functional equation?', ['A functional equation, relating a functions values rather than solving for a number', 'A basic linear equation with one unknown number', 'A geometric equation describing a circle', 'An equation with no functions involved'], 0),
    ('Why is the Cauchy functional equation a useful case study in advanced function theory?', ['It shows how an assumption such as continuity can dramatically restrict the possible solutions', 'It demonstrates that functional equations never have interesting properties', 'It shows that all functions are always linear regardless of assumptions', 'It has no connection to the broader study of functions'], 0)]),
CA('Calculus: The Limit Comparison Test for Series',
   'Grade 12 Calculus strand: the limit comparison test determines the convergence or divergence of a series by comparing it to a second series of known behaviour, concluding that both series converge or both diverge whenever the limit of their term ratio is a finite, positive number.',
   [('What does the limit comparison test determine?', ['Whether a series converges or diverges by comparing it to a series of known behaviour', 'The exact numerical sum of any series', 'The derivative of a series term by term', 'The domain of a function'], 0),
    ('Under what condition does the limit comparison test conclude that two series share the same convergence behaviour?', ['When the limit of the ratio of their terms is a finite, positive number', 'When the limit of the ratio of their terms is exactly zero', 'When the limit of the ratio of their terms is infinite', 'When the two series have a different number of terms'], 0),
    ('How does the limit comparison test differ from the basic (direct) comparison test?', ['It uses a limit of a ratio rather than requiring a strict term-by-term inequality', 'It requires no comparison series whatsoever', 'It can only be applied to divergent series', 'It replaces the need for any known reference series'], 0),
    ('Why is the limit comparison test often more convenient than the direct comparison test?', ['It avoids the need to prove a strict inequality between every pair of terms', 'It always gives a different answer than the direct comparison test', 'It cannot be used with any known series, such as a p-series', 'It requires computing an integral rather than a limit'], 0),
    ('Which type of series is commonly used as the known reference series when applying the limit comparison test?', ['A p-series with a similar term structure', 'A series with no defined terms', 'A series that always diverges to infinity regardless of behaviour', 'A finite sequence with exactly five terms'], 0)]),
PH('Physics: Piezoelectricity — Mechanical Stress and Electric Polarization',
   'Grade 12 Physics strand: piezoelectricity is the property of certain crystals, such as quartz, to generate an electric voltage when subjected to mechanical stress, and conversely to deform slightly when an electric field is applied across them.',
   [('What does a piezoelectric material generate when subjected to mechanical stress?', ['An electric voltage', 'A visible colour change', 'A sudden increase in temperature only', 'A permanent change in chemical composition'], 0),
    ('Which common crystal is well known for exhibiting piezoelectric behaviour?', ['Quartz', 'Table salt', 'Pure water ice', 'Ordinary window glass'], 0),
    ('What happens to a piezoelectric material when an electric field is applied across it?', ['It deforms slightly', 'It instantly melts', 'It becomes perfectly transparent', 'It loses all electrical properties permanently'], 0),
    ('In which everyday device might piezoelectric materials commonly be used to generate a spark or signal?', ['Electric lighters and certain microphones', 'Household light bulbs, using only filament heating', 'Simple mechanical pendulum clocks', 'Ordinary glass windows'], 0),
    ('Why is the relationship in piezoelectricity described as reversible between mechanical and electrical effects?', ['Mechanical stress produces voltage, and an applied voltage produces mechanical deformation, in both directions', 'Piezoelectric materials only respond to mechanical stress and never to electric fields', 'Piezoelectric materials only respond to electric fields and never to mechanical stress', 'There is no relationship between mechanical and electrical effects in these materials'], 0)]),
]),
day(126, [
E('Drama: Noh and Kabuki — Japanese Theatrical Tradition',
  'Grade 12 English strand: Noh theatre uses slow, stylized movement, masks, and chant to evoke a meditative, spiritual atmosphere, while the later Kabuki tradition developed bold makeup, dynamic staging, and popular appeal, together offering a non-Western counterpoint to the Western dramatic traditions studied elsewhere in this course.',
  [('What theatrical elements are characteristic of Noh theatre?', ['Slow, stylized movement, masks, and chant', 'Rapid-fire dialogue with no staging', 'Purely improvised scenes with no tradition', 'Realistic sets designed to mimic everyday life exactly'], 0),
   ('What atmosphere does Noh theatre typically aim to evoke?', ['A meditative, spiritual atmosphere', 'A loud, chaotic atmosphere', 'A strictly comedic atmosphere', 'An atmosphere with no emotional intention'], 0),
   ('How does Kabuki differ from Noh in its general style?', ['Kabuki favours bold makeup, dynamic staging, and broader popular appeal', 'Kabuki and Noh are identical in every respect', 'Kabuki rejects the use of any makeup or costume', 'Kabuki has no connection to Japanese performance tradition'], 0),
   ('Why might a comparative drama unit include Noh and Kabuki alongside Western traditions such as the Theatre of Cruelty?', ['To offer a non-Western counterpoint that broadens understanding of theatrical possibility', 'Comparative study of world theatre is never useful', 'Noh and Kabuki have no relationship to dramatic theory', 'Only Western traditions can be meaningfully analyzed'], 0),
   ('Which theatrical element commonly distinguishes Noh performers?', ['The use of carved masks to represent certain characters', 'The complete absence of costume', 'The use of modern digital projection', 'The requirement that performers remain seated throughout'], 0)]),
AF('Number Theory: Quadratic Residues and the Legendre Symbol',
   'Grade 12 Advanced Functions strand: an integer is a quadratic residue modulo a prime p if it is congruent to some perfect square modulo p, and the Legendre symbol offers a compact notation for indicating whether a given integer is a quadratic residue for that prime.',
   [('What does it mean for an integer to be a quadratic residue modulo a prime p?', ['It is congruent to some perfect square modulo p', 'It is always divisible evenly by p with no remainder', 'It is always equal to p itself', 'It can never be a whole number'], 0),
    ('What does the Legendre symbol indicate?', ['Whether a given integer is a quadratic residue for a particular prime', 'The exact square root of a given integer', 'The sum of all divisors of a given integer', 'The number of primes less than a given integer'], 0),
    ('What branch of mathematics does the study of quadratic residues belong to?', ['Number theory', 'Basic geometry', 'Elementary statistics', 'Financial mathematics'], 0),
    ('Why might quadratic residues be relevant to cryptography?', ['Certain cryptographic systems rely on the difficulty of determining quadratic residues for large primes', 'Quadratic residues have no application in cryptography', 'Cryptography never uses modular arithmetic', 'Quadratic residues make every encryption system trivially easy to break'], 0),
    ('For a given odd prime p, roughly what fraction of the nonzero residues modulo p are quadratic residues?', ['About half', 'All of them', 'None of them', 'Exactly one'], 0)]),
CA('Calculus: Abels Theorem and the Boundary Behaviour of Power Series',
   'Grade 12 Calculus strand: Abels Theorem addresses what happens at the boundary of a power series interval of convergence, showing that if a power series converges at an endpoint, its sum there equals the limit of the function as it is approached from within the interval.',
   [('What does Abels Theorem address?', ['The behaviour of a power series at the boundary of its interval of convergence', 'The behaviour of a power series far outside its interval of convergence', 'The derivative of a power series at its centre', 'The radius of convergence of a geometric series alone'], 0),
    ('According to Abels Theorem, if a power series converges at an endpoint, what is true of its sum there?', ['It equals the limit of the function approached from within the interval', 'It is always undefined at that endpoint', 'It is always equal to zero regardless of the series', 'It bears no relationship to the function inside the interval'], 0),
    ('What term describes the values at which a power series may or may not converge, situated exactly at the edge of its interval of convergence?', ['The endpoints of the interval of convergence', 'The centre of the interval of convergence', 'The radius of convergence itself', 'The derivative of the series'], 0),
    ('Why is boundary behaviour of a power series considered a subtle question in calculus?', ['Convergence at an endpoint is not guaranteed by convergence within the open interval, and must be checked separately', 'Every power series behaves identically at every point within and beyond its interval', 'Boundary behaviour is always identical to behaviour at the centre', 'Power series never converge at their endpoints under any circumstances'], 0),
    ('Abels Theorem builds on which earlier calculus topic concerning infinite sums of terms involving powers of a variable?', ['Power series and radius of convergence', 'The trapezoid rule for numerical integration', 'The chain rule for derivatives', 'The concept of a definite integral alone'], 0)]),
PH('Physics: The Physics of Rainbows — Primary and Secondary Bows',
   'Grade 12 Physics strand: a rainbow forms when sunlight is refracted, internally reflected, and dispersed within countless raindrops, with the bright primary bow arising from a single internal reflection and the fainter, colour-reversed secondary bow arising from an additional internal reflection within each drop.',
   [('What three optical processes combine to produce a rainbow within a raindrop?', ['Refraction, internal reflection, and dispersion of sunlight', 'Only absorption, with no reflection or refraction involved', 'Only diffraction, with no other optical process', 'Only polarization, with no colour separation'], 0),
    ('How many internal reflections occur within a raindrop to produce the primary rainbow?', ['One', 'Zero', 'Two', 'Three'], 0),
    ('How does the secondary rainbow differ from the primary rainbow?', ['It arises from an additional internal reflection and appears fainter with reversed colour order', 'It is always brighter than the primary rainbow', 'It involves no reflection within the raindrop at all', 'It has an identical colour order to the primary rainbow'], 0),
    ('What causes the separation of sunlight into distinct colours within a raindrop?', ['Dispersion, since different wavelengths of light refract by slightly different amounts', 'All wavelengths of light always refract by exactly the same amount', 'Only red light is refracted, with no other colours involved', 'Dispersion has no role in forming a rainbow'], 0),
    ('Why must an observer generally face away from the sun to see a rainbow?', ['Sunlight must be refracted and reflected back toward the observer from within raindrops in front of them', 'Rainbows only form when facing directly toward the sun', 'Sunlight has no role in forming a rainbow', 'Rainbows can be seen equally well in any direction relative to the sun'], 0)]),
]),
day(127, [
E('Writing: The Book Proposal — Pitching a Long-Form Work',
  'Grade 12 English strand: a book proposal is a persuasive document written to convince a publisher or agent of the value of a long-form work, typically combining an overview, market analysis, and sample material into a single professional pitch.',
  [('What is the purpose of a book proposal?', ['To persuade a publisher or agent of the value of a long-form work', 'To provide a full, final draft of a completed novel', 'To summarize a single newspaper article', 'To replace the need for any sample writing'], 0),
   ('What elements does a book proposal typically combine?', ['An overview, market analysis, and sample material', 'Only a list of the authors previous jobs', 'Only a table of contents with no other content', 'Only a bibliography with no persuasive content'], 0),
   ('Why might a book proposal include a market analysis?', ['To show the audience and comparable works, demonstrating why the book would sell', 'Market analysis is never relevant to book proposals', 'To replace the need for any writing sample entirely', 'To avoid discussing the books actual content'], 0),
   ('How does writing a book proposal differ from writing the book itself?', ['A proposal persuades an audience of the books value before it is fully written', 'A proposal and a finished book are identical in purpose', 'A proposal must always be longer than the finished book', 'A proposal requires no persuasive writing at all'], 0),
   ('Which skill from earlier in this course is directly useful when drafting a book proposal?', ['Rhetorical and persuasive writing techniques', 'Only mathematical calculation', 'Only skills related to stage lighting', 'Only skills related to translating a text'], 0)]),
AF('Discrete Math: The Twelvefold Way — Counting Functions Between Sets',
   'Grade 12 Advanced Functions strand: the twelvefold way is a unifying framework in combinatorics that organizes twelve related counting problems describing functions between a set of size n and a set of size m, varying by whether elements are distinguishable and whether the functions must be injective or surjective.',
   [('What does the twelvefold way organize?', ['Twelve related combinatorial counting problems describing functions between two sets', 'A single formula with no variation', 'Twelve unrelated geometry problems', 'A list of prime numbers'], 0),
    ('What two properties commonly vary among the twelve counting problems in the twelvefold way?', ['Whether elements are distinguishable and whether functions must be injective or surjective', 'The colour and size of the sets involved', 'The country in which the problem was first studied', 'The final numeric answer alone, with no underlying structure'], 0),
    ('What is an injective function, as relevant to the twelvefold way?', ['A function where distinct inputs always map to distinct outputs', 'A function where every output is identical', 'A function with no defined inputs', 'A function that only maps numbers to themselves'], 0),
    ('Why is the twelvefold way considered a useful organizing framework?', ['It connects many seemingly separate counting problems under a single unified structure', 'It only applies to a single, narrow counting problem', 'It has no relationship to combinatorics', 'It eliminates the need to count anything at all'], 0),
    ('The twelvefold way belongs to which broader branch of mathematics?', ['Combinatorics', 'Trigonometry', 'Calculus', 'Financial mathematics'], 0)]),
CA('Calculus: The Midpoint Rule and Comparing Numerical Integration Methods',
   'Grade 12 Calculus strand: the midpoint rule approximates a definite integral by evaluating the integrand at the midpoint of each subinterval rather than at an endpoint, generally producing a more accurate estimate than simple left or right Riemann sums for a comparable number of subintervals.',
   [('Where does the midpoint rule evaluate the integrand within each subinterval?', ['At the midpoint of the subinterval', 'At the left endpoint only', 'At the right endpoint only', 'At a randomly chosen point each time'], 0),
    ('How does the accuracy of the midpoint rule generally compare to simple left or right Riemann sums?', ['It generally produces a more accurate estimate for a comparable number of subintervals', 'It always produces a less accurate estimate', 'It produces an identical estimate in every case', 'Accuracy cannot be compared between these methods'], 0),
    ('What earlier numerical integration technique from this course is the midpoint rule most naturally compared to?', ['The trapezoid rule', 'The chain rule for derivatives', 'The ratio test for series', 'The method of partial fractions'], 0),
    ('Why might increasing the number of subintervals improve the accuracy of the midpoint rule?', ['Smaller subintervals allow the function to be approximated more closely by a constant value near each midpoint', 'Increasing subintervals always makes the estimate less accurate', 'The number of subintervals has no effect on accuracy', 'The midpoint rule requires exactly one subinterval to work correctly'], 0),
    ('Numerical integration methods such as the midpoint rule are especially useful when ___.', ['An antiderivative cannot easily be found in closed form', 'Every integral always has a simple closed-form antiderivative', 'A function has no defined value anywhere', 'Integration is never needed to solve a real problem'], 0)]),
PH('Physics: Sonic Booms and the Physics of Shock Waves',
   'Grade 12 Physics strand: a sonic boom is the sharp, thunder-like sound produced when an object travels faster than the speed of sound, generating a cone-shaped shock wave in which compressed sound waves pile up along the objects direction of travel.',
   [('What causes a sonic boom?', ['An object travelling faster than the speed of sound in the surrounding medium', 'An object travelling slower than the speed of sound', 'An object that produces no sound whatsoever', 'A sudden, unrelated change in air temperature alone'], 0),
    ('What shape does the shock wave produced by a supersonic object typically take?', ['A cone shape trailing behind the object', 'A perfectly flat, planar wavefront with no shape', 'A spherical shape centred on the observer', 'A shape unrelated to the objects motion'], 0),
    ('Why do sound waves pile up ahead of an object travelling faster than sound?', ['The object outruns the sound waves it produces, so they compress together rather than spreading ahead of it', 'Sound waves always spread out evenly regardless of an objects speed', 'The object slows down all nearby sound waves to a stop', 'Sound waves cannot be produced by a moving object at all'], 0),
    ('What term describes the ratio of an objects speed to the speed of sound?', ['The Mach number', 'The Reynolds number', 'The refractive index', 'The wavelength ratio'], 0),
    ('Why might a sonic boom be heard as a sudden, sharp sound rather than a gradual buildup?', ['The shock wave passes a stationary observer nearly all at once as a compressed pressure front', 'Shock waves always arrive extremely gradually over many minutes', 'A sonic boom is identical to an ordinary quiet sound with no sudden change', 'Sonic booms only occur when an object is completely silent'], 0)]),
]),
day(128, [
E('Media Analysis: Video Game Narrative and Interactive Storytelling',
  'Grade 12 English strand: video game narrative examines how interactive media shapes storytelling through player choice, branching structure, and environmental detail, raising questions about authorship and meaning when a reader becomes a participant in the story.',
  [('What distinguishes video game narrative from traditional linear storytelling?', ['Player choice and interactivity can shape how the story unfolds', 'Video game narrative never involves any storytelling at all', 'Player choice has no effect on interactive narrative', 'Video games are identical in structure to printed novels'], 0),
   ('What is branching structure in interactive storytelling?', ['A narrative design where different choices lead to different story paths', 'A narrative that always follows exactly one fixed path', 'A structure used only in poetry, never in games', 'A term unrelated to interactive media'], 0),
   ('How can environmental detail contribute to storytelling in a video game?', ['By conveying narrative information through setting and objects rather than dialogue alone', 'Environmental detail can never communicate narrative meaning', 'Environmental detail always replaces the need for any characters', 'Environmental detail is limited strictly to background colour'], 0),
   ('What question does interactive storytelling raise about authorship?', ['Whether meaning is shaped jointly by the designer and the player who makes choices', 'Authorship questions never apply to interactive media', 'Only the player can be considered the author, never the designer', 'Only the designer can be considered the author, with no player influence'], 0),
   ('Why might a media literacy unit include video game narrative alongside older media forms such as film and podcasts?', ['To examine how emerging interactive media reshapes storytelling conventions', 'Video games have no relationship to storytelling or narrative theory', 'Interactive media is considered entirely outside the scope of media literacy', 'Video game narrative is identical to television narrative in every way'], 0)]),
AF('Functions: Padé Approximants and Rational Function Approximation',
   'Grade 12 Advanced Functions strand: a Padé approximant approximates a function using a ratio of two polynomials rather than a single polynomial, often matching the behaviour of the original function, including near singularities, more closely than a Taylor polynomial of comparable degree.',
   [('What form does a Padé approximant take?', ['A ratio of two polynomials', 'A single polynomial with no denominator', 'A trigonometric expression only', 'A constant value with no variables'], 0),
    ('How can a Padé approximant differ in usefulness from a Taylor polynomial of similar degree?', ['It can more closely match the original function, including near singularities', 'It can never approximate a function as well as a Taylor polynomial', 'It only works for functions with no singularities anywhere', 'It removes the need for polynomials entirely'], 0),
    ('What is a rational function, in the context of Padé approximants?', ['A function expressed as the ratio of two polynomials', 'A function with no defined denominator', 'A function limited strictly to whole-number outputs', 'A function that is always undefined'], 0),
    ('Why might engineers or scientists prefer a Padé approximant over a simple polynomial approximation in some situations?', ['It can capture certain function behaviours, such as asymptotes, more accurately', 'Padé approximants are always less accurate than polynomials', 'Padé approximants cannot be evaluated numerically', 'They have no practical scientific use'], 0),
    ('Padé approximants extend ideas most closely related to which earlier calculus concept?', ['Taylor and Maclaurin series approximation', 'Basic arithmetic addition', 'Simple counting problems', 'Elementary geometry'], 0)]),
CA('Calculus: Bessel Functions and Solutions to Bessels Equation',
   'Grade 12 Calculus strand: Bessel functions arise as solutions to Bessels differential equation, a second-order equation that appears when solving problems with cylindrical symmetry, such as vibrations of a circular drumhead, and are often found using the method of Frobenius near a singular point.',
   [('Bessel functions arise as solutions to which type of equation?', ['Bessels differential equation, a second-order differential equation', 'A simple first-order linear equation with no special structure', 'A basic algebraic equation with no derivatives', 'An equation with no variables at all'], 0),
    ('In what kind of physical problems does Bessels equation commonly appear?', ['Problems with cylindrical symmetry, such as vibrations of a circular drumhead', 'Problems involving only straight-line motion', 'Problems with no physical application whatsoever', 'Problems limited strictly to financial mathematics'], 0),
    ('What earlier method from this course is often used to find solutions to Bessels equation near a singular point?', ['The method of Frobenius', 'The trapezoid rule for numerical integration', 'The ratio test for series convergence alone, with no series solution', 'Newtons method for root approximation'], 0),
    ('Why are Bessel functions particularly useful for describing circularly symmetric systems?', ['Their oscillatory, decaying behaviour matches vibrations and waves in circular or cylindrical geometries', 'They apply only to systems with no symmetry at all', 'Bessel functions cannot describe any oscillatory behaviour', 'They are limited strictly to describing straight-line motion'], 0),
    ('What order of differential equation is Bessels equation?', ['Second-order', 'First-order', 'Third-order', 'Zero-order, meaning it contains no derivatives'], 0)]),
PH('Physics: Magnetohydrodynamics and the Behaviour of Plasma',
   'Grade 12 Physics strand: magnetohydrodynamics studies the behaviour of electrically conducting fluids, such as plasma, as they interact with magnetic fields, describing phenomena from the confinement of plasma in fusion reactors to the dynamics of the solar wind.',
   [('What does magnetohydrodynamics study?', ['The behaviour of electrically conducting fluids interacting with magnetic fields', 'The behaviour of solid crystals under mechanical stress', 'The behaviour of sound waves in a vacuum', 'The behaviour of light in a lens system'], 0),
    ('Which state of matter is most commonly studied within magnetohydrodynamics?', ['Plasma', 'Solid crystal', 'Ordinary liquid water', 'Ideal gas with no charged particles'], 0),
    ('What practical application relies on magnetohydrodynamic principles to contain extremely hot plasma?', ['Magnetic confinement in fusion reactors', 'Ordinary household refrigeration', 'Standard incandescent light bulbs', 'Mechanical pendulum clocks'], 0),
    ('What large-scale astrophysical phenomenon is often described using magnetohydrodynamics?', ['The dynamics of the solar wind', 'The freezing point of water', 'The refraction of light through glass', 'The vibration of a plucked guitar string'], 0),
    ('Why must a fluid be electrically conducting for magnetohydrodynamic effects to apply?', ['Only a conducting fluid can carry currents that interact meaningfully with a magnetic field', 'Electrical conductivity has no relevance to magnetic interactions', 'Magnetohydrodynamics applies equally to fluids that cannot conduct electricity', 'Conductivity only matters for solids, never fluids'], 0)]),
]),
day(129, [
E('Grammar and Style: Parallelism and the Rhetorical Triad',
  'Grade 12 English strand: parallelism repeats a grammatical structure across a series of words, phrases, or clauses to create rhythm and emphasis, with the rhetorical triad, or grouping of three, forming one especially memorable and persuasive pattern of parallel structure.',
  [('What does parallelism repeat across a series of words, phrases, or clauses?', ['A grammatical structure', 'A random assortment of unrelated structures', 'Only punctuation marks', 'Only capital letters'], 0),
   ('What effect does parallelism typically create in a sentence?', ['Rhythm and emphasis', 'Confusion and disorder', 'The complete removal of meaning', 'A strictly comedic tone in every case'], 0),
   ('What is the rhetorical triad?', ['A grouping of three parallel elements, often used for persuasive emphasis', 'A rule requiring exactly one clause per sentence', 'A term for a poem with three stanzas only', 'A citation format used in academic essays'], 0),
   ('Why might a public speaker use a rhetorical triad?', ['Groups of three are often especially memorable and persuasive to an audience', 'Groups of three are considered the least memorable pattern possible', 'Triads eliminate the need for any other rhetorical device', 'Triads are only used in casual, private conversation'], 0),
   ('Which of these sentences demonstrates parallelism?', ['We came, we saw, we conquered', 'We came and there was seeing and we also won', 'We came, seeing occurred, and then conquest', 'Coming happened, then we saw, conquering was done'], 0)]),
AF('Number Theory: The Frobenius Coin Problem',
   'Grade 12 Advanced Functions strand: the Frobenius coin problem asks for the largest amount that cannot be formed using only coins of two or more given denominations, with the two-denomination case having a known closed-form solution when the denominations share no common factor.',
   [('What does the Frobenius coin problem ask for?', ['The largest amount that cannot be formed using given coin denominations', 'The smallest amount that can be formed using any coins', 'The total number of coins in a given collection', 'The average value of a set of coins'], 0),
    ('For exactly two coin denominations with no common factor, what kind of solution does the Frobenius coin problem have?', ['A known closed-form solution', 'No solution under any circumstances', 'A solution that changes randomly each time', 'A solution requiring an infinite number of coins'], 0),
    ('Why must the two coin denominations share no common factor for the classic formula to apply?', ['If they shared a common factor, infinitely many amounts (all multiples of that factor missed) could never be formed', 'Common factors have no effect on which amounts can be formed', 'A common factor always makes every amount formable', 'The problem cannot be defined unless the denominations are equal'], 0),
    ('The Frobenius coin problem is also sometimes called by what other informal name, referencing a hypothetical food-based version of the problem?', ['The chicken nugget problem', 'The apple pie problem', 'The birthday problem', 'The travelling salesman problem'], 0),
    ('What area of mathematics does the Frobenius coin problem belong to?', ['Number theory', 'Basic geometry', 'Elementary probability with no number theory involved', 'Trigonometry'], 0)]),
CA('Calculus: The Leibniz Rule for Differentiating Under the Integral Sign',
   'Grade 12 Calculus strand: the Leibniz rule allows the derivative of an integral whose integrand depends on a parameter to be found by differentiating the integrand with respect to that parameter and then integrating the result, turning some otherwise difficult integrals into more manageable differentiation problems.',
   [('What does the Leibniz rule allow a mathematician to find?', ['The derivative of an integral whose integrand depends on a parameter', 'The exact numerical value of any definite integral', 'The radius of convergence of a power series', 'The area under a curve with no reference to a parameter'], 0),
    ('According to the Leibniz rule, in what order are differentiation and integration typically applied?', ['Differentiate the integrand with respect to the parameter, then integrate the result', 'Integrate first, then differentiate the final numerical answer', 'Neither operation is actually needed', 'Differentiate and integrate simultaneously with no defined order'], 0),
    ('Why might the Leibniz rule turn a difficult integral into a more manageable problem?', ['Differentiating under the integral sign can simplify an integrand that was otherwise hard to integrate directly', 'It always makes every integral impossible to solve', 'It removes the parameter from the problem entirely with no benefit', 'It has no effect on the difficulty of an integral'], 0),
    ('What must an integrand generally satisfy for the Leibniz rule to apply straightforwardly?', ['Reasonable smoothness conditions, such as continuity, in both the variable of integration and the parameter', 'No conditions whatsoever, since the rule always applies universally', 'The integrand must be a constant with no parameter at all', 'The integrand must have no variable of integration'], 0),
    ('The Leibniz rule is a useful technique in which broader area of mathematical practice?', ['Evaluating parameter-dependent integrals in advanced calculus and physics', 'Elementary arithmetic with whole numbers only', 'Basic geometry with no calculus involved', 'Simple counting and combinatorics alone'], 0)]),
PH('Physics: The Barometric Formula and Atmospheric Pressure with Altitude',
   'Grade 12 Physics strand: the barometric formula describes how atmospheric pressure decreases approximately exponentially with increasing altitude, reflecting the decreasing weight of air above a given point as altitude increases.',
   [('According to the barometric formula, how does atmospheric pressure generally change with increasing altitude?', ['It decreases approximately exponentially', 'It increases approximately exponentially', 'It remains exactly constant at every altitude', 'It changes randomly with no consistent pattern'], 0),
    ('Why does atmospheric pressure decrease as altitude increases?', ['There is less air, and therefore less weight of air, above a given point at higher altitude', 'There is more air pressing down at higher altitude', 'Altitude has no effect on the weight of air above a point', 'Pressure is unrelated to the weight of the atmosphere'], 0),
    ('What type of mathematical function best approximates the decrease of pressure with altitude in the barometric formula?', ['An exponential decay function', 'A simple linear function', 'A quadratic function with a maximum value', 'A constant function with no variation'], 0),
    ('Why might the barometric formula be relevant to pilots and mountaineers?', ['It helps predict the change in air pressure, and therefore oxygen availability, at different altitudes', 'It has no relevance to altitude-related physiology or aviation', 'It only applies to underwater pressure, never atmospheric pressure', 'It describes only the colour of the sky at different altitudes'], 0),
    ('The barometric formula is derived using principles from which broader area of physics?', ['Thermodynamics and the physics of gases', 'Optics and the study of light', 'Nuclear physics and radioactive decay', 'Electromagnetism and circuit theory'], 0)]),
]),
day(130, [
E('English Review: Poetic Form, Prose Traditions, and Rhetoric',
  'Grade 12 English strand review: students revisit the sonnet, the ode, the picaresque novel, autofiction, Russian Formalism, Noh and Kabuki theatre, the book proposal, video game narrative, and parallelism.',
  [('What is the volta in a sonnet?', ['A turn in argument or feeling partway through the poem', 'The title of the poem', 'A rhyme scheme with no meaning', 'A type of stanza break with no thematic function'], 0),
   ('What does an ode typically do?', ['Praises or meditates on a person, event, or abstract idea in an elevated style', 'Tells a long adventure story with a plot', 'Provides step-by-step instructions', 'Lists facts with no emotional tone'], 0),
   ('What kind of protagonist is typical of a picaresque novel?', ['A roguish, low-born character who lives by wit rather than status', 'A noble hero destined to rule a kingdom', 'A detective solving a single central mystery', 'A narrator who never interacts with other characters'], 0),
   ('What does autofiction blend together?', ['Autobiography and invented, fictional narrative', 'Poetry and technical writing', 'Drama and journalism with no overlap', 'History textbooks and legal documents'], 0),
   ('What theatrical elements are characteristic of Noh theatre?', ['Slow, stylized movement, masks, and chant', 'Rapid-fire dialogue with no staging', 'Purely improvised scenes with no tradition', 'Realistic sets designed to mimic everyday life exactly'], 0)]),
AF('AdvancedFunctions Review: Number Theory, Discrete Math, and Special Functions',
   'Grade 12 Advanced Functions strand review: students revisit Carmichael numbers, the Ackermann function, the Lambert W function, Latin squares, the Cauchy functional equation, quadratic residues, the twelvefold way, Padé approximants, and the Frobenius coin problem.',
   [('What is a Carmichael number?', ['A composite number that satisfies Fermats Little Theorem for every coprime base', 'A prime number with no special properties', 'A number that is always divisible by two', 'A fraction between zero and one'], 0),
    ('How does the growth rate of the Ackermann function compare to exponential functions?', ['It grows dramatically faster than exponential or polynomial functions', 'It grows more slowly than a linear function', 'It grows at exactly the same rate as a constant function', 'It never grows at all'], 0),
    ('What kind of equations can the Lambert W function help solve?', ['Equations where the unknown appears both inside and outside an exponential expression', 'Only simple linear equations with one term', 'Only equations with no exponential component', 'Only equations involving whole numbers less than ten'], 0),
    ('What defines a Latin square?', ['An n by n grid where each symbol appears exactly once in every row and column', 'A grid where symbols may repeat freely within a row', 'A triangular arrangement of numbers', 'A grid with only one row and one column'], 0),
    ('What does the Frobenius coin problem ask for?', ['The largest amount that cannot be formed using given coin denominations', 'The smallest amount that can be formed using any coins', 'The total number of coins in a given collection', 'The average value of a set of coins'], 0)]),
CA('Calculus Review: Multivariable Extensions and Advanced Techniques',
   'Grade 12 Calculus strand review: students revisit the envelope theorem, the Hessian matrix and second-derivative test, gradient vectors and directional derivatives, arc length of a polar curve, the limit comparison test, Abels Theorem, the midpoint rule, Bessel functions, and the Leibniz rule.',
   [('What does the envelope theorem describe?', ['How the optimal value of a constrained optimization problem changes as a parameter changes', 'The exact solution of any equation with no parameters', 'A method for graphing a single linear function', 'A rule for counting whole numbers only'], 0),
    ('What does the Hessian matrix collect?', ['The second-order partial derivatives of a multivariable function', 'Only the first-order partial derivatives', 'A list of the functions input values', 'The constants found within the function'], 0),
    ('What does the gradient vector of a function consist of?', ['A vector of the functions partial derivatives', 'A single number representing the functions maximum value', 'A list of the functions input variables only', 'A matrix of second-order derivatives'], 0),
    ('What does the limit comparison test determine?', ['Whether a series converges or diverges by comparing it to a series of known behaviour', 'The exact numerical sum of any series', 'The derivative of a series term by term', 'The domain of a function'], 0),
    ('Bessel functions arise as solutions to which type of equation?', ['Bessels differential equation, a second-order differential equation', 'A simple first-order linear equation with no special structure', 'A basic algebraic equation with no derivatives', 'An equation with no variables at all'], 0)]),
PH('Physics Review: Quantum, Thermal, and Wave Phenomena',
   'Grade 12 Physics strand review: students revisit the Pauli exclusion principle, the Mössbauer effect, the Gibbs paradox, nuclear magnetic resonance, piezoelectricity, the physics of rainbows, sonic booms, magnetohydrodynamics, and the barometric formula.',
   [('What does the Pauli exclusion principle state?', ['No two identical fermions can occupy the same quantum state simultaneously', 'All particles must occupy exactly the same quantum state', 'Only protons are affected by exclusion rules', 'Exclusion rules apply only to photons'], 0),
    ('What does the Mössbauer effect involve?', ['Nuclei bound in a solid crystal emitting or absorbing gamma rays without energy loss to recoil', 'The complete absorption of all visible light by a crystal', 'A magnetic field generated by a rotating nucleus', 'A change in the mass of a nucleus over time'], 0),
    ('What situation gives rise to the Gibbs paradox?', ['Calculating the entropy of mixing two samples of the same, identical gas', 'Calculating the entropy of two entirely different, distinguishable gases', 'Measuring the temperature of a single isolated particle', 'Measuring the pressure of a vacuum'], 0),
    ('What does a piezoelectric material generate when subjected to mechanical stress?', ['An electric voltage', 'A visible colour change', 'A sudden increase in temperature only', 'A permanent change in chemical composition'], 0),
    ('What three optical processes combine to produce a rainbow within a raindrop?', ['Refraction, internal reflection, and dispersion of sunlight', 'Only absorption, with no reflection or refraction involved', 'Only diffraction, with no other optical process', 'Only polarization, with no colour separation'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g12_121_130)
    append_to(12, g12_121_130)
