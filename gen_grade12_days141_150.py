#!/usr/bin/env python3
"""Grade 12, Days 141-150 -- extends Grade 12 from 140 to 150 days. Topics
chosen after reading the full existing Day 1-140 title list (see
data/grade12.json) to avoid any overlap. Grade 12 has been very heavily
mined across thirteen prior batches (especially named physics effects and
number theory/discrete math in Advanced Functions), so this batch hunts for
genuinely fresh angles: the mock-epic, the pastoral tradition, detective
fiction and the golden age whodunit, literary naturalism, memoir and life
writing, the ballad tradition, concrete poetry, weird fiction and cosmic
horror, and the serial novel; the Poisson distribution, quadratic
reciprocity, group theory, Boolean algebra, Pearson correlation,
combinatorial game theory and Nim, Fermats two squares theorem, the central
limit theorem, and spanning trees/Kruskals algorithm; Cauchy-Euler
equations, exact differential equations, the secant method, Romberg
integration, the inverse Laplace transform, the scalar triple product,
variation of parameters, equilibrium/stability of differential equations,
and the improved Euler (Heun) method; the Magnus effect, the Venturi effect,
total internal reflection, Newtons rings, the Tyndall effect, the Kerr
effect, the Larmor formula, the Rayleigh criterion, and the Thomson effect.
Day 150 is a review day, following the exact per-subject review pattern
used on Day 130/140: one review lesson per subject, each quizzing the first
five of that subject's nine new topics.

Subject keys for Grade 12 are "English", "AdvancedFunctions",
"Calculus", "Physics" (same as all earlier Grade 12 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote or straight-apostrophe characters are used
anywhere in title/question/summary/option text; apostrophes are avoided
entirely, matching the convention used in the Days 131-140 batch.
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


def _rebalance_answer_positions(days, seed=20260807):
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


g12_141_150 = [
day(141, [
E('The Mock-Epic: Heroic Form Turned to Comic Purpose',
  'Grade 12 English strand: the mock-epic borrows the elevated conventions of epic poetry, such as invocations, extended similes, and grand battle scenes, and applies them to a trivial subject, generating satire through the mismatch between grand form and petty content.',
  [('What does a mock-epic typically do with the grand conventions of epic poetry?', ['Applies them to a trivial or minor subject to create a comic, satirical effect', 'Uses them only to describe genuine historical battles', 'Removes all poetic devices from the epic form', 'Turns the epic into a private diary with no audience'], 0),
   ('What effect is created by using elevated epic language to describe a trivial event?', ['A comic mismatch between grand form and petty content', 'A serious, tragic tone throughout', 'A completely literal, unremarkable description', 'An effect identical to that of a straightforward epic'], 0),
   ('Which epic convention might a mock-epic parody, such as calling on a muse for a trivial subject?', ['The invocation to a muse', 'The use of complete silence', 'The absence of any narrator', 'A ban on figurative language'], 0),
   ('What is the primary purpose of the mock-epic as a literary mode?', ['To satirize a subject by treating it with exaggerated, undeserved grandeur', 'To document real historical events with total accuracy', 'To eliminate humour from serious poetry', 'To replace the epic tradition entirely'], 0),
   ('Why might a poet choose the mock-epic form to critique fashionable high society?', ['Its exaggerated grandeur exposes the triviality of the behaviour being described', 'The form requires total seriousness with no exaggeration', 'It cannot be applied to social behaviour', 'It only works when describing real wars'], 0)]),
AF('Statistics: The Poisson Distribution and Modelling Rare Events',
   'Grade 12 Advanced Functions strand: the Poisson distribution models the number of times a rare, independent event occurs in a fixed interval of time or space, given a known average rate, and is widely applied to phenomena such as call arrivals or radioactive decay counts.',
   [('What kind of events does the Poisson distribution typically model?', ['Rare, independent events occurring a certain number of times in a fixed interval', 'Events that always occur at exactly the same time', 'Events with no possible variation whatsoever', 'Only events with a probability of exactly one half'], 0),
    ('What single parameter primarily characterizes a Poisson distribution?', ['The average rate at which events occur in the interval', 'The total population size only', 'The number of trials in a binomial experiment', 'The standard deviation of a normal distribution'], 0),
    ('Which of these is a classic example of a Poisson-distributed quantity?', ['The number of phone calls received by a call centre in an hour', 'The exact height of a randomly chosen adult', 'The outcome of a single coin flip', 'The colour of a randomly chosen car'], 0),
    ('How does the Poisson distribution relate to the binomial distribution studied earlier in this course?', ['It can approximate a binomial distribution when trials are many and the success probability is small', 'The two distributions have no mathematical relationship', 'The Poisson distribution only applies to continuous data', 'The binomial distribution cannot model rare events at all'], 0),
    ('What assumption is made about events in a Poisson process?', ['Events occur independently of one another at a constant average rate', 'Every event depends heavily on the previous event', 'Only two events can ever occur in total', 'The rate of events changes randomly with no pattern'], 0)]),
CA('Cauchy-Euler Equations and Variable-Coefficient Differential Equations',
   'Grade 12 Calculus strand: a Cauchy-Euler equation is a linear differential equation whose coefficients are powers of the independent variable rather than constants, solved by substituting a trial solution of the form x raised to a power r to reduce the equation to a polynomial characteristic equation.',
   [('What distinguishes a Cauchy-Euler equation from the constant-coefficient equations studied earlier?', ['Its coefficients are powers of the independent variable rather than constants', 'It has no derivatives of any kind', 'It can only be solved numerically, never analytically', 'It is always a first-order equation'], 0),
    ('What trial solution is typically substituted to solve a Cauchy-Euler equation?', ['x raised to an unknown power r', 'A constant function with no variable', 'The sine of x only', 'A trial solution is never used for this type of equation'], 0),
    ('What kind of equation for r results after substituting the trial solution into a Cauchy-Euler equation?', ['A polynomial characteristic equation in r', 'A first-degree equation with no solutions', 'An equation with no relationship to r', 'A differential equation identical to the original'], 0),
    ('Why might a Cauchy-Euler equation arise in physical applications despite having variable coefficients?', ['Certain physical systems, such as some involving radial symmetry, naturally produce equations with power-law coefficients', 'Physical systems never produce variable-coefficient equations', 'Cauchy-Euler equations only arise in purely abstract mathematics with no application', 'Every physical system produces exactly the same differential equation'], 0),
    ('How does solving a Cauchy-Euler equation compare to solving a constant-coefficient linear equation studied earlier?', ['Both reduce to finding roots of a characteristic equation, though the substitution differs', 'The two methods share no similarities whatsoever', 'Cauchy-Euler equations require no characteristic equation at all', 'Constant-coefficient equations cannot be solved using a characteristic equation'], 0)]),
PH('The Magnus Effect and the Physics of Spinning Projectiles',
   'Grade 12 Physics strand: the Magnus effect describes the curved path taken by a spinning object moving through a fluid, arising because the spin creates a pressure difference across the object as it drags fluid faster on one side and slower on the other, producing a sideways lift force.',
   [('What is the Magnus effect?', ['The curved path taken by a spinning object moving through a fluid, caused by a sideways lift force', 'The tendency of an object to fall in a perfectly straight line', 'The complete absence of drag on a spinning object', 'A magnetic force acting on any moving object'], 0),
    ('What causes the sideways force responsible for the Magnus effect?', ['A pressure difference created as the spinning surface drags fluid faster on one side than the other', 'A change in the objects mass as it spins', 'An external magnetic field acting on the object', 'The complete absence of air around the object'], 0),
    ('Which everyday example commonly demonstrates the Magnus effect?', ['A spinning ball curving in flight, as in soccer or baseball', 'A ball dropped straight down with no spin', 'A stationary object sitting on a table', 'A block sliding without any rotation'], 0),
    ('How does increasing the spin rate of a projectile typically affect the strength of the Magnus effect?', ['It generally increases the sideways force and the resulting curve', 'It has no effect on the force at all', 'It always reduces the curve to zero', 'It reverses the direction of gravity'], 0),
    ('What broader fluid dynamics principle underlies the pressure difference in the Magnus effect?', ['Faster-moving fluid exerts lower pressure than slower-moving fluid on the objects surface', 'Fluid pressure is always identical regardless of its speed', 'The effect depends only on the objects colour', 'Spinning objects experience no interaction with surrounding fluid'], 0)]),
]),
day(142, [
E('The Pastoral Tradition: Idealized Nature and Rural Life in Literature',
  'Grade 12 English strand: the pastoral tradition idealizes rural life and nature, often through the voices of shepherds or rustic figures, contrasting the simplicity and harmony of the countryside with the corruption or complexity of court and city life.',
  [('What does the pastoral tradition typically idealize?', ['Rural life and nature, often voiced through shepherd or rustic figures', 'The complexity and noise of city life', 'Industrial machinery and urban commerce', 'The corruption of royal courts with no counterpoint'], 0),
   ('What contrast does pastoral literature often draw?', ['The simplicity of the countryside against the corruption or complexity of court and city life', 'Two equally corrupt cities with no rural setting at all', 'Modern technology against ancient technology', 'A comparison between two shepherds with identical views'], 0),
   ('Which kind of figure commonly voices pastoral poetry?', ['A shepherd or other rustic character', 'A king addressing his court', 'A scientist explaining a discovery', 'A soldier narrating a battle'], 0),
   ('Why might a poet use a pastoral setting to comment indirectly on court life?', ['The rural distance allows an indirect, often gentler critique of courtly behaviour', 'Pastoral settings cannot comment on anything beyond farming', 'Court life and pastoral settings are considered identical', 'Indirect critique is impossible in pastoral poetry'], 0),
   ('How does the pastoral tradition differ from the pathetic fallacy studied earlier, which projects emotion onto nature?', ['Pastoral idealizes the rural world itself as a setting and theme rather than only projecting emotion onto it', 'The two techniques are entirely identical in every respect', 'The pathetic fallacy always requires a rural setting', 'Pastoral literature never involves nature imagery at all'], 0)]),
AF('Number Theory: The Law of Quadratic Reciprocity',
   'Grade 12 Advanced Functions strand: the law of quadratic reciprocity relates whether p is a quadratic residue modulo q to whether q is a quadratic residue modulo p, for distinct odd primes p and q, forming one of the most celebrated results in classical number theory.',
   [('What does the law of quadratic reciprocity relate?', ['Whether p is a quadratic residue modulo q to whether q is a quadratic residue modulo p', 'The sum of two unrelated even numbers', 'The number of divisors of a composite number only', 'The value of an unrelated trigonometric identity'], 0),
    ('What kind of numbers p and q does the law of quadratic reciprocity concern?', ['Distinct odd primes', 'Any two even numbers', 'Only the number one and itself', 'Non-integer real numbers'], 0),
    ('What is a quadratic residue modulo n?', ['A number congruent to a perfect square modulo n', 'Any number that is not an integer', 'A number that is always negative', 'A number with no relationship to squares at all'], 0),
    ('Which earlier-studied concept does quadratic reciprocity build directly on?', ['Quadratic residues and the Legendre symbol', 'The concept of derangements', 'The birthday problem', 'Chebyshev polynomials'], 0),
    ('Why is quadratic reciprocity considered significant in the history of number theory?', ['It provides an efficient way to determine quadratic residues without exhaustive testing and is a celebrated deep result', 'It has no practical or theoretical significance whatsoever', 'It only applies to the number zero', 'It was proven to be false and later discarded'], 0)]),
CA('Exact Differential Equations and the Test for Exactness',
   'Grade 12 Calculus strand: a first-order differential equation is exact when it can be written as the differential of some function, a property checked using a partial-derivative test, after which the equation is solved directly by finding that underlying function.',
   [('What does it mean for a first-order differential equation to be exact?', ['It can be written as the differential of some underlying function', 'It has no solution under any circumstances', 'It must always be solved using only numerical methods', 'It requires no partial derivatives to analyze'], 0),
    ('What test determines whether a given differential equation is exact?', ['A partial-derivative test comparing mixed partial derivatives of its two terms', 'A test that only checks whether the equation is linear', 'A test that requires graphing the equation first', 'There is no reliable test for exactness'], 0),
    ('What is found once an equation is confirmed to be exact?', ['The underlying function whose differential produced the equation', 'A random constant with no mathematical meaning', 'The equations degree only, with no further work', 'A numerical approximation with no closed form'], 0),
    ('How does solving an exact equation differ from applying an integrating factor to a general first-order linear equation?', ['An exact equation is solved directly by recovering its underlying function, while a general linear equation is transformed using a separate factor', 'The two methods are mathematically identical in every step', 'Exact equations always require the same integrating factor used for linear equations', 'Integrating factors can never be applied outside exact equations'], 0),
    ('Why is checking exactness a useful first step before attempting a general solution method?', ['It quickly reveals whether a simpler, direct solution technique will succeed', 'It guarantees a solution exists for every possible differential equation', 'It replaces the need for any other solution method entirely', 'It only applies to second-order equations'], 0)]),
PH('The Venturi Effect and Bernoullis Principle in Fluid Flow',
   'Grade 12 Physics strand: the Venturi effect describes the drop in fluid pressure that occurs as a fluid speeds up while flowing through a constricted section of a pipe, a direct consequence of Bernoullis principle, which relates pressure, speed, and height along a streamline.',
   [('What does the Venturi effect describe?', ['A drop in fluid pressure as the fluid speeds up through a constricted section of a pipe', 'A rise in fluid pressure whenever a pipe widens', 'The complete stopping of fluid flow at a constriction', 'A change in fluid temperature with no change in pressure'], 0),
    ('What broader physical principle explains the pressure drop in the Venturi effect?', ['Bernoullis principle', 'Newtons third law alone', 'The law of conservation of charge', 'The ideal gas law exclusively'], 0),
    ('What happens to fluid speed as it passes through a constriction in a pipe?', ['It increases', 'It decreases', 'It stays exactly the same', 'It becomes zero'], 0),
    ('Which everyday device commonly applies the Venturi effect?', ['A carburetor or atomizer that uses fast-moving air to draw in fuel or liquid', 'A stationary water tank with no moving fluid', 'A solid metal rod with no fluid flow', 'A device with no connection to fluid speed'], 0),
    ('How does Bernoullis principle relate pressure and speed along a streamline?', ['As fluid speed increases along a streamline, its pressure decreases', 'Pressure and speed are always exactly equal to one another', 'Increasing speed always increases pressure at the same point', 'Bernoullis principle relates only temperature and volume'], 0)]),
]),
day(143, [
E('Detective Fiction and the Golden Age of the Whodunit',
  'Grade 12 English strand: golden age detective fiction, exemplified by writers such as Agatha Christie, presents a puzzle-like mystery solved through logical deduction from carefully planted clues, typically culminating in a formal revelation scene that identifies the culprit.',
  [('What structure typically defines golden age detective fiction?', ['A puzzle-like mystery solved through logical deduction from carefully planted clues', 'A story with no crime or mystery of any kind', 'A tale told entirely without a detective figure', 'A narrative that reveals the culprit before any investigation begins'], 0),
   ('What convention often closes a golden age detective novel?', ['A formal revelation scene that identifies the culprit', 'An ending that leaves the crime permanently unexplained', 'A chapter with no connection to the mystery at all', 'A scene describing only the weather'], 0),
   ('What must clues in a fair-play detective story generally do?', ['Be made available to the reader before the solution is revealed', 'Remain hidden from the reader until after the story ends', 'Have no connection to the eventual solution', 'Be invented only in the final chapter'], 0),
   ('Why is the detective figure central to golden age detective fiction?', ['The detective embodies rational deduction that restores order by solving the puzzle', 'The detective plays no active role in solving the crime', 'The detective is typically the culprit in every story', 'The detective exists only to narrate unrelated events'], 0),
   ('How does the whodunit differ from crime fiction focused mainly on graphic violence?', ['It emphasizes the intellectual puzzle and process of deduction over graphic action', 'It contains no crime of any kind', 'It always avoids describing a detective altogether', 'It focuses exclusively on courtroom procedure'], 0)]),
AF('Abstract Algebra: An Introduction to Group Theory',
   'Grade 12 Advanced Functions strand: a group is a set equipped with a single operation that is closed, associative, has an identity element, and gives every element an inverse, a structure that generalizes the arithmetic of numbers, matrices, and symmetries studied earlier in the course.',
   [('What four properties define a group under its operation?', ['Closure, associativity, an identity element, and inverses for every element', 'Only closure, with no other requirements', 'Commutativity alone, with no identity element required', 'A requirement that the set contain exactly one element'], 0),
    ('What does closure mean for a group operation?', ['Combining any two elements of the set always yields another element of the set', 'The set must contain infinitely many elements', 'The operation must always produce zero', 'Every element must be its own inverse'], 0),
    ('What is an identity element in a group?', ['An element that leaves other elements unchanged when combined with them', 'An element that changes every other element into itself', 'An element that must always equal zero', 'An element that has no inverse'], 0),
    ('Which familiar set forms a group under an operation studied earlier in the course?', ['The integers under addition', 'The set of all colours under no defined operation', 'A single point with no operation', 'A set with no elements at all'], 0),
    ('Why is group theory considered a generalization of arithmetic studied earlier in this course?', ['It abstracts structural properties shared by numbers, matrices, and symmetries under a common set of rules', 'It has no relationship to numbers, matrices, or symmetries', 'It only applies to a single specific number', 'It replaces arithmetic entirely with an unrelated field'], 0)]),
CA('The Secant Method for Root Approximation',
   'Grade 12 Calculus strand: the secant method approximates a root of a function by drawing a line through two nearby points on the curve and using the x-intercept of that line as the next approximation, avoiding the need for a derivative required by Newtons method.',
   [('What line does the secant method use to generate its next root approximation?', ['A line through two nearby points on the curve', 'A vertical line through a single point', 'A line tangent to the curve at one point only', 'A line with no relationship to the curve'], 0),
    ('What advantage does the secant method have over Newtons method?', ['It does not require computing a derivative of the function', 'It always converges faster than every other method', 'It requires exactly one initial guess rather than two', 'It guarantees an exact answer after a single step'], 0),
    ('What quantity from the secant line gives the next root approximation?', ['Its x-intercept', 'Its y-intercept', 'Its slope alone, with no intercept used', 'The midpoint of the two original points'], 0),
    ('How many previous approximations does the secant method use to generate the next one?', ['Two', 'Zero', 'One', 'An unlimited number, all at once'], 0),
    ('How does the secant method generally compare to the bisection method studied earlier in terms of convergence speed?', ['It generally converges faster than bisection, though convergence is not guaranteed', 'It always converges more slowly than bisection', 'The two methods have identical convergence behaviour in every case', 'Bisection converges without ever needing two initial points'], 0)]),
PH('Total Internal Reflection and Fiber-Optic Communication',
   'Grade 12 Physics strand: total internal reflection occurs when light travelling in a denser medium strikes a boundary with a less dense medium at an angle greater than the critical angle, reflecting entirely back into the denser medium, a principle exploited by fiber-optic cables to transmit light signals with minimal loss.',
   [('What is total internal reflection?', ['Light reflecting entirely back into a denser medium when it strikes a boundary at an angle greater than the critical angle', 'Light passing completely unaffected through any boundary', 'The complete absorption of light at any surface', 'A phenomenon that only occurs with sound waves'], 0),
    ('What condition on the angle of incidence causes total internal reflection to occur?', ['The angle of incidence must be greater than the critical angle', 'The angle of incidence must be exactly zero degrees', 'The angle of incidence has no effect on the outcome', 'The angle must be measured from a less dense to a denser medium'], 0),
    ('What technology exploits total internal reflection to transmit signals over long distances?', ['Fiber-optic cables', 'Ordinary copper telephone wire', 'A simple glass window with no coating', 'A device with no connection to light at all'], 0),
    ('Why must light travel from a denser to a less dense medium for total internal reflection to be possible?', ['A critical angle, beyond which total internal reflection occurs, exists only when moving toward a lower refractive index', 'Total internal reflection occurs equally in every direction of travel', 'Light must first stop moving entirely for reflection to occur', 'Refractive index has no role in this phenomenon'], 0),
    ('What advantage does fiber-optic transmission gain from total internal reflection?', ['The light signal is transmitted with minimal loss along the length of the fiber', 'The signal is destroyed at every bend in the fiber', 'The fiber must be perfectly straight with no curves allowed', 'The signal converts entirely into sound during transmission'], 0)]),
]),
day(144, [
E('Literary Naturalism: Determinism and the Novel',
  'Grade 12 English strand: literary naturalism extends realism by portraying characters as shaped largely by heredity, environment, and social forces beyond their control, presenting human behaviour with a scientific, often pessimistic determinism associated with writers such as Emile Zola.',
  [('What forces do naturalist novels typically emphasize as shaping character?', ['Heredity, environment, and social forces beyond the characters control', 'Pure random chance with no underlying pattern at all', 'Only the characters own free choices, with no outside influence', 'Supernatural forces such as ghosts and spirits'], 0),
   ('How does literary naturalism extend the realism studied in earlier literary traditions?', ['It adds a scientific, deterministic view of human behaviour beyond typical realistic detail', 'It removes all realistic detail from the narrative entirely', 'It focuses exclusively on fantastical, magical events', 'It rejects any connection to observable human behaviour'], 0),
   ('What tone often characterizes naturalist fiction?', ['A pessimistic determinism', 'An unrelentingly cheerful, optimistic outlook', 'A tone of pure comic absurdity throughout', 'A tone with no emotional quality whatsoever'], 0),
   ('Which nineteenth-century writer is closely associated with literary naturalism?', ['Emile Zola', 'William Wordsworth', 'Jonathan Swift', 'Geoffrey Chaucer'], 0),
   ('How does determinism in naturalist fiction typically affect a characters sense of agency?', ['Characters have limited control, being largely shaped by forces beyond them', 'Characters have complete, unlimited control over every outcome', 'Agency plays no role in naturalist fiction at all', 'Naturalist characters are entirely free of environmental influence'], 0)]),
AF('Discrete Math: Boolean Algebra and Logic Gates',
   'Grade 12 Advanced Functions strand: Boolean algebra manipulates true and false values using operations such as AND, OR, and NOT, providing the mathematical foundation for logic gates and digital circuits that underlie modern computing.',
   [('What values does Boolean algebra fundamentally operate on?', ['True and false (or one and zero) values', 'Only irrational numbers', 'Complex numbers exclusively', 'Negative fractions only'], 0),
    ('Which three operations form the basic building blocks of Boolean algebra?', ['AND, OR, and NOT', 'Addition, subtraction, and multiplication', 'Sine, cosine, and tangent', 'Integration, differentiation, and limits'], 0),
    ('What physical devices implement Boolean operations inside a computer?', ['Logic gates', 'Ordinary resistors with no logical function', 'Simple wires with no components', 'Mechanical gears with no electrical component'], 0),
    ('What does the AND operation output when both of its inputs are true?', ['True', 'False', 'A value that is neither true nor false', 'An undefined result'], 0),
    ('Why is Boolean algebra considered foundational to modern computing?', ['It underlies the design of digital circuits and the logic gates used inside computers', 'It has no connection to computers or digital devices', 'It only applies to purely abstract, unused mathematics', 'It was replaced entirely by a different number system in modern computers'], 0)]),
CA('Romberg Integration and Richardson Extrapolation',
   'Grade 12 Calculus strand: Romberg integration improves the accuracy of the trapezoid rule by combining successive trapezoid-rule estimates using Richardson extrapolation, systematically eliminating leading error terms to converge rapidly to the true value of a definite integral.',
   [('What numerical integration method does Romberg integration build upon and improve?', ['The trapezoid rule', 'The method of undetermined coefficients', 'Lagrange interpolation alone', 'The bisection method for root-finding'], 0),
    ('What technique combines successive estimates to improve accuracy in Romberg integration?', ['Richardson extrapolation', 'A simple average with no weighting applied', 'Random sampling of the integrand', 'Direct substitution with no combination of estimates'], 0),
    ('What does Richardson extrapolation systematically eliminate in Romberg integration?', ['Leading error terms in the trapezoid-rule estimates', 'The entire integral itself', 'All numerical estimates without producing a final result', 'The functions original definition'], 0),
    ('How does Romberg integrations accuracy typically compare to a single trapezoid-rule estimate?', ['It converges more rapidly to the true value of the integral', 'It is always exactly as accurate and no more', 'It is always less accurate than a single trapezoid estimate', 'It cannot be compared to the trapezoid rule at all'], 0),
    ('Why might Romberg integration be preferred over simply halving the step size repeatedly in the plain trapezoid rule?', ['It combines estimates cleverly, achieving faster convergence than simple refinement alone', 'It requires no calculation of trapezoid-rule estimates whatsoever', 'It only works for a single, fixed step size', 'It produces a less accurate result than repeated halving'], 0)]),
PH('Newtons Rings and Thin-Film Interference',
   'Grade 12 Physics strand: Newtons rings are a pattern of concentric bright and dark circular fringes produced by the interference of light reflected between a curved lens surface and a flat plate, arising from the varying thickness of the thin air film trapped between them.',
   [('What pattern do Newtons rings form?', ['Concentric bright and dark circular fringes', 'A single straight bright line with no pattern', 'A random, non-repeating scatter of colour', 'A uniform, unchanging field of one colour'], 0),
    ('What produces the interference pattern seen in Newtons rings?', ['Light reflected between a curved lens surface and a flat plate, with a varying air-film thickness between them', 'Light passing through a completely opaque solid block', 'Sound waves reflecting off a curved surface', 'A magnetic field acting directly on light'], 0),
    ('What varies across the trapped air film to produce the ring pattern?', ['Its thickness', 'Its electric charge', 'Its temperature alone, with no thickness variation', 'Its colour, independent of any physical property'], 0),
    ('What broader wave phenomenon explains the formation of Newtons rings?', ['Thin-film interference', 'Simple reflection with no interference involved', 'The photoelectric effect', 'Nuclear decay'], 0),
    ('Why do Newtons rings appear circular rather than in some other shape?', ['The air-film thickness varies symmetrically around the point of contact of the curved lens', 'The rings are drawn intentionally with no physical cause', 'Circular shapes are the only shapes light can ever form', 'The flat plate is always perfectly circular in shape'], 0)]),
]),
day(145, [
E('Memoir and the Art of Life Writing',
  'Grade 12 English strand: memoir is a nonfiction form of life writing that reconstructs a specific period or theme from the authors own life, shaping remembered experience into narrative through selection, reflection, and a controlling perspective distinct from a comprehensive autobiography.',
  [('What does memoir typically reconstruct?', ['A specific period or theme from the authors own life', 'A complete, chronological record of an entire life from birth to the present', 'A purely fictional life invented for entertainment', 'A biography of a person the author has never met'], 0),
   ('How does memoir differ from a comprehensive autobiography?', ['It focuses on a selected period or theme rather than the whole of a life', 'It must always cover every year of the authors life in equal detail', 'It is always written by someone other than the subject', 'It cannot include any reflection or interpretation'], 0),
   ('What shapes remembered experience into a coherent narrative in memoir?', ['Selection, reflection, and a controlling perspective', 'Pure, unfiltered transcription with no shaping at all', 'A total absence of any narrative structure', 'Random, disconnected fragments with no unifying thread'], 0),
   ('To which broader genre category does memoir belong?', ['Nonfiction life writing', 'Pure fantasy fiction', 'Formal scientific reporting', 'Dramatic verse composed for the stage'], 0),
   ('Why might a memoirist rely on a controlling perspective when shaping their material?', ['To shape scattered memory into a coherent, meaningful narrative', 'To avoid including any personal experience whatsoever', 'Because memoir requires no interpretation of events', 'Because a controlling perspective is forbidden in nonfiction'], 0)]),
AF('Statistics: Correlation and the Pearson Correlation Coefficient',
   'Grade 12 Advanced Functions strand: the Pearson correlation coefficient measures the strength and direction of the linear relationship between two quantitative variables, producing a value between negative one and positive one that indicates how closely the data follow a straight line.',
   [('What does the Pearson correlation coefficient measure?', ['The strength and direction of the linear relationship between two quantitative variables', 'The exact mean of a single data set', 'The total number of data points collected', 'The mode of a categorical variable'], 0),
    ('What range of values can the Pearson correlation coefficient take?', ['From negative one to positive one', 'From zero to positive one hundred', 'Only the values zero and one', 'Any real number with no upper or lower bound'], 0),
    ('What does a Pearson correlation coefficient close to zero indicate?', ['Little to no linear relationship between the two variables', 'A perfect positive linear relationship', 'A perfect negative linear relationship', 'That the two variables are identical'], 0),
    ('What does a Pearson correlation coefficient of positive one indicate?', ['A perfect positive linear relationship between the two variables', 'A perfect negative linear relationship', 'No relationship of any kind', 'An undefined relationship'], 0),
    ('Why is correlation not the same as causation, an important caution when interpreting a Pearson coefficient?', ['A strong correlation does not necessarily mean one variable causes changes in the other', 'A strong correlation always proves direct causation', 'Correlation and causation are mathematically identical concepts', 'Causation can never be studied using correlation at all'], 0)]),
CA('The Inverse Laplace Transform and Solving Initial Value Problems',
   'Grade 12 Calculus strand: the inverse Laplace transform converts a function of s back into a function of t, allowing a differential equation solved in the transformed domain using the Laplace transform to be translated back into its original time-domain solution.',
   [('What does the inverse Laplace transform do?', ['Converts a function of s back into a function of t', 'Converts a function of t into an unrelated function of x', 'Removes all variables from a function entirely', 'Doubles the degree of a polynomial function'], 0),
    ('Why is the inverse Laplace transform applied after solving an equation in the s-domain?', ['To translate the solution back into its original time-domain form', 'To eliminate the need for any differential equation entirely', 'To convert the solution into a purely graphical representation only', 'To remove the s-domain solution without producing a final answer'], 0),
    ('Which earlier-studied tool is the inverse Laplace transform paired with?', ['The Laplace transform', 'The bisection method', 'The chain rule for multivariable functions', 'The trapezoid rule'], 0),
    ('What type of problem is commonly solved using the Laplace transform and its inverse together?', ['Initial value problems for differential equations', 'Problems involving only static, unchanging quantities', 'Purely geometric problems with no equations involved', 'Problems with no reference to time at all'], 0),
    ('Why can transforming a differential equation into the s-domain make it easier to solve?', ['It converts differential equations into algebraic equations, which are generally easier to manipulate', 'It makes the equation impossible to solve by any method', 'It removes all information about the original problem', 'It converts algebraic equations into differential equations instead'], 0)]),
PH('The Tyndall Effect and Light Scattering in Colloids',
   'Grade 12 Physics strand: the Tyndall effect is the scattering of light by particles suspended in a colloid, making a beam of light passing through the mixture visible from the side, distinguished from Rayleigh scattering by the larger size of the scattering particles relative to atmospheric molecules.',
   [('What is the Tyndall effect?', ['The scattering of light by particles suspended in a colloid, making a beam of light visible from the side', 'The complete absorption of all light by a transparent solution', 'A phenomenon that only occurs in a perfect vacuum', 'The bending of light as it passes through a single flat pane of glass'], 0),
    ('What makes a light beam visible when it passes through a colloid?', ['Light scattered sideways by particles suspended in the mixture', 'The beam gaining additional energy from the colloid', 'A chemical reaction that produces new light', 'The complete absence of any particles in the mixture'], 0),
    ('How does the Tyndall effect differ from the Rayleigh scattering studied earlier in this course?', ['It involves larger particles than the molecules responsible for Rayleigh scattering', 'It involves no particles of any kind', 'It occurs only in a perfect vacuum, unlike Rayleigh scattering', 'The two phenomena are identical in every respect'], 0),
    ('Which everyday scene commonly demonstrates the Tyndall effect?', ['A visible beam of light shining through fog or a dusty room', 'A perfectly clear glass of water with no visible beam', 'A beam of light travelling through total darkness with no scattering', 'A completely opaque solid block with no light passing through'], 0),
    ('Why can the Tyndall effect be used to distinguish a colloid from a true solution?', ['Colloidal particles scatter light visibly, while the much smaller particles in a true solution generally do not', 'True solutions always scatter light more strongly than colloids', 'Colloids and true solutions scatter light in exactly the same way', 'Neither colloids nor true solutions can scatter light at all'], 0)]),
]),
day(146, [
E('The Ballad Tradition: Narrative Song and Folk Verse',
  'Grade 12 English strand: the ballad is a narrative folk poem originally meant to be sung, typically composed in quatrains with a simple rhyme scheme, recounting a dramatic story of love, tragedy, or adventure through compressed, often repetitive language.',
  [('What is a ballad in its traditional form?', ['A narrative folk poem originally meant to be sung', 'A purely visual poem with no words at all', 'A formal legal document with no poetic content', 'A prose essay with no narrative elements'], 0),
   ('What stanza form do ballads typically use?', ['Quatrains with a simple rhyme scheme', 'Fourteen-line stanzas with an intricate rhyme scheme', 'Stanzas with no consistent line count at all', 'A single unbroken line with no stanza breaks'], 0),
   ('What kinds of stories do ballads commonly recount?', ['Dramatic stories of love, tragedy, or adventure', 'Detailed technical instructions for a craft', 'Purely abstract mathematical concepts', 'A list of unrelated historical dates'], 0),
   ('What stylistic feature often marks ballad language?', ['Compressed, often repetitive language, including refrains', 'Extremely long, unbroken sentences with no repetition', 'A total absence of rhythm or musicality', 'Language borrowed entirely from formal legal writing'], 0),
   ('How does the ballads oral, musical origin shape its form?', ['It favours memorable rhythm, repetition, and simple structure suited to singing', 'It requires the poem to be entirely unrhymed and unmetered', 'It has no influence on the poems structure at all', 'It requires the poem to be read silently and never performed'], 0)]),
AF('Discrete Math: Combinatorial Game Theory and the Game of Nim',
   'Grade 12 Advanced Functions strand: combinatorial game theory analyzes two-player games of perfect information with no chance element, and the game of Nim, in which players remove objects from piles, provides a classic example whose winning strategy is determined using the binary XOR of pile sizes.',
   [('What kind of games does combinatorial game theory study?', ['Two-player games of perfect information with no chance element', 'Games decided purely by rolling dice with no strategy involved', 'Games with an unlimited number of players and no defined rules', 'Games where information is always hidden from both players'], 0),
    ('What is the basic action taken by players in the game of Nim?', ['Removing objects from piles', 'Placing new objects onto an empty board', 'Rolling a die to determine the next move', 'Drawing cards from a shuffled deck'], 0),
    ('What operation determines the winning strategy in the game of Nim?', ['The binary XOR of the pile sizes', 'A simple sum of the pile sizes with no further calculation', 'The largest pile size alone, with no other calculation', 'A random guess with no calculation involved'], 0),
    ('What does it mean for a game to have perfect information?', ['Both players can see the entire state of the game at all times', 'Only one player can ever see the game state', 'Neither player has any knowledge of the game at all', 'The game state changes randomly with no visibility'], 0),
    ('Why is Nim considered a classic example within combinatorial game theory?', ['It has a fully solved, elegant winning strategy that illustrates the fields core ideas', 'It has never been solved and remains a complete mystery', 'It involves no strategy of any kind', 'It cannot be analyzed mathematically in any way'], 0)]),
CA('The Scalar Triple Product and the Volume of a Parallelepiped',
   'Grade 12 Calculus and Vectors strand: the scalar triple product combines three vectors using a cross product and a dot product to produce a single number whose absolute value equals the volume of the parallelepiped formed by the three vectors.',
   [('What operations combine to form the scalar triple product?', ['A cross product followed by a dot product', 'Two separate dot products with no cross product', 'Division of one vector by another', 'A single addition of three vectors with no multiplication'], 0),
    ('What geometric quantity does the absolute value of the scalar triple product equal?', ['The volume of the parallelepiped formed by the three vectors', 'The area of a triangle formed by two of the vectors', 'The length of a single vector alone', 'The angle between two of the vectors'], 0),
    ('How many vectors are combined to form a scalar triple product?', ['Three', 'One', 'Two', 'Four'], 0),
    ('What does a scalar triple product of zero indicate about the three vectors involved?', ['The vectors are coplanar, meaning they are linearly dependent', 'The vectors are mutually perpendicular with maximum volume', 'The vectors have no defined direction at all', 'The vectors must all have zero magnitude'], 0),
    ('How does the scalar triple product build on the cross product studied earlier in this course?', ['It uses the cross product of two vectors, then takes the dot product of that result with the third vector', 'It has no relationship to the cross product whatsoever', 'It replaces the cross product with simple scalar multiplication', 'It requires computing four separate cross products'], 0)]),
PH('The Kerr Effect and Electro-Optic Modulation',
   'Grade 12 Physics strand: the Kerr effect is a change in the refractive index of a material in response to an applied electric field, proportional to the square of the field strength, a property exploited in electro-optic modulators to control light using electrical signals.',
   [('What does the Kerr effect describe?', ['A change in the refractive index of a material in response to an applied electric field', 'A change in the mass of a material when heated', 'The complete absorption of all electric fields by a material', 'A change in a materials colour with no relation to any field'], 0),
    ('How does the change in refractive index in the Kerr effect relate to the applied field strength?', ['It is proportional to the square of the field strength', 'It is entirely independent of the field strength', 'It decreases linearly as the field strength increases', 'It is proportional to the inverse of the field strength'], 0),
    ('What technology exploits the Kerr effect to control light using electrical signals?', ['Electro-optic modulators', 'Ordinary incandescent light bulbs', 'A simple mechanical shutter with no electrical component', 'A device with no relationship to electric fields'], 0),
    ('Why is the Kerr effect described as a nonlinear optical effect?', ['Its response depends on the square rather than a simple direct proportion to field strength', 'Its response is always exactly proportional to the field strength', 'It has no mathematical relationship to the applied field', 'It only occurs in the complete absence of any field'], 0),
    ('What general category of physical effects does the Kerr effect belong to, alongside the Faraday effect studied earlier?', ['Electro-optic and magneto-optic effects', 'Purely mechanical effects with no optical component', 'Nuclear decay processes', 'Effects with no connection to light at all'], 0)]),
]),
day(147, [
E('Concrete Poetry: Shape and Typography as Meaning',
  'Grade 12 English strand: concrete poetry arranges words, letters, and typography on the page so that the visual shape of the poem itself contributes directly to its meaning, treating the poems physical layout as inseparable from its verbal content.',
  [('What does concrete poetry emphasize alongside its words?', ['The visual shape and typographic arrangement of the poem on the page', 'Only the sound of the words when read aloud, with no visual element', 'A complete absence of any typography or layout', 'A strict, unvarying rhyme scheme with no visual concerns'], 0),
   ('How does the visual shape of a concrete poem typically relate to its meaning?', ['It contributes directly to and reinforces the poems meaning', 'It has no connection to the poems meaning whatsoever', 'It always contradicts and undermines the poems stated subject', 'It exists purely by accident with no intended effect'], 0),
   ('What is treated as inseparable from verbal content in concrete poetry?', ['The poems physical layout on the page', 'The poems title alone, with no reference to the body text', 'The publishers logo on the page', 'The font size used in an unrelated document'], 0),
   ('How does concrete poetry differ from a conventional lyric poem read primarily for its sound and sense?', ['It also relies on visual, spatial arrangement as a source of meaning', 'It rejects the use of words entirely', 'It cannot be printed or displayed visually at all', 'It is identical in every respect to a conventional lyric poem'], 0),
   ('Why might a poet arrange words into a visual shape to represent an abstract idea?', ['Visual form can mirror or enact the poems subject in ways plain text alone cannot', 'Visual form always obscures a poems meaning entirely', 'Abstract ideas cannot be represented through any visual arrangement', 'Typography has no effect on how a poem is interpreted'], 0)]),
AF('Number Theory: Fermats Two Squares Theorem',
   'Grade 12 Advanced Functions strand: Fermats two squares theorem states that an odd prime can be written as the sum of two perfect squares if and only if it leaves a remainder of one when divided by four, connecting modular arithmetic to the representation of numbers as sums of squares.',
   [('What does Fermats two squares theorem state about an odd prime number?', ['It can be written as the sum of two perfect squares if and only if it is congruent to one modulo four', 'It can never be written as the sum of two perfect squares under any condition', 'It must always be an even number', 'It can only be expressed as the sum of three perfect squares'], 0),
    ('What must an odd prime be congruent to modulo four to be expressible as a sum of two squares?', ['One', 'Two', 'Three', 'Zero'], 0),
    ('Which primes cannot be written as the sum of two perfect squares, according to this theorem?', ['Primes congruent to three modulo four', 'Primes congruent to one modulo four', 'All prime numbers without exception', 'Only the number two'], 0),
    ('Which branch of mathematics connects to Fermats two squares theorem through congruences?', ['Modular arithmetic', 'Trigonometric identities', 'Financial mathematics', 'Basic set theory with no arithmetic involved'], 0),
    ('How does Fermats two squares theorem extend ideas from quadratic residues studied earlier in this course?', ['It uses conditions on residues modulo four to determine whether a prime is representable as a sum of two squares', 'It has no connection whatsoever to quadratic residues', 'It replaces quadratic residues with an unrelated geometric concept', 'It only applies to even numbers, unlike quadratic residues'], 0)]),
CA('Variation of Parameters for Non-Homogeneous Differential Equations',
   'Grade 12 Calculus strand: variation of parameters solves a non-homogeneous linear differential equation by replacing the constants in the homogeneous solution with unknown functions, determined by a system derived from the original equation, producing a particular solution even when undetermined coefficients does not apply cleanly.',
   [('What does variation of parameters replace in the homogeneous solution of a differential equation?', ['The constants, replacing them with unknown functions', 'The independent variable itself', 'The order of the differential equation', 'The entire homogeneous solution, discarding it completely'], 0),
    ('What type of differential equation does variation of parameters solve?', ['Non-homogeneous linear differential equations', 'Purely algebraic equations with no derivatives', 'Only first-order separable equations', 'Equations with no solution of any kind'], 0),
    ('How are the unknown functions in variation of parameters determined?', ['By solving a system of equations derived from the original differential equation', 'By guessing a constant value with no further calculation', 'By ignoring the original equation entirely', 'By setting them all equal to zero automatically'], 0),
    ('What advantage does variation of parameters have over the method of undetermined coefficients?', ['It applies more generally, even in cases where undetermined coefficients does not work cleanly', 'It only works for a single, very specific type of equation', 'It requires no knowledge of the homogeneous solution at all', 'It cannot be used for any linear differential equation'], 0),
    ('What must be found first before applying variation of parameters to a non-homogeneous equation?', ['The homogeneous solution to the associated equation', 'The final numerical answer, before any other work is done', 'A random particular solution with no justification', 'The Laplace transform of an unrelated function'], 0)]),
PH('The Larmor Formula and Radiation from Accelerating Charges',
   'Grade 12 Physics strand: the Larmor formula gives the power radiated by a non-relativistic accelerating point charge, showing that acceleration, not merely motion, is required for a charged particle to emit electromagnetic radiation.',
   [('What does the Larmor formula calculate?', ['The power radiated by an accelerating point charge', 'The total mass of a charged particle', 'The exact position of a charge at a given time', 'The wavelength of visible light alone'], 0),
    ('What property of a charged particles motion is required for it to radiate, according to the Larmor formula?', ['Acceleration, not merely motion at a constant velocity', 'A constant velocity with absolutely no acceleration', 'A complete absence of any electric charge', 'A fixed, unchanging position with no motion at all'], 0),
    ('Why does a charge moving at a constant velocity not radiate energy according to this principle?', ['Radiation requires acceleration, and uniform motion involves no acceleration', 'Charges moving at constant velocity always radiate the most energy', 'Radiation depends only on the charges mass, not its motion', 'Constant velocity motion is physically impossible for a charge'], 0),
    ('To which kind of charge does the Larmor formula, in its basic form, strictly apply?', ['A non-relativistic charge', 'Only a charge moving at the speed of light', 'A charge with absolutely no mass', 'A charge that is entirely stationary at all times'], 0),
    ('How does the Larmor formula connect to the study of electromagnetic waves earlier in this course?', ['It explains the physical origin of electromagnetic radiation emitted by accelerating charges', 'It has no connection to electromagnetic waves whatsoever', 'It shows that electromagnetic waves can only be produced by magnets', 'It proves that radiation cannot be produced by any charge'], 0)]),
]),
day(148, [
E('Weird Fiction and the Aesthetics of Cosmic Horror',
  'Grade 12 English strand: weird fiction evokes a sense of cosmic horror by suggesting the existence of vast, indifferent, and unknowable forces beyond human comprehension, emphasizing dread and awe over conventional monsters or explainable threats.',
  [('What sense does weird fiction primarily aim to evoke in its readers?', ['Cosmic horror, or dread at vast, unknowable forces', 'Light comic relief with no sense of unease', 'A purely romantic, sentimental mood', 'A calm, reassuring sense of order and safety'], 0),
   ('What kind of forces does weird fiction typically suggest lie beyond human comprehension?', ['Vast, indifferent, unknowable cosmic forces', 'Small, easily understood household objects', 'Forces that are always fully explained by the story', 'Forces limited strictly to ordinary human emotions'], 0),
   ('What does weird fiction emphasize over a conventional, fully explainable monster?', ['Dread and awe at something fundamentally incomprehensible', 'A detailed scientific explanation for every event', 'A cheerful resolution with no lingering unease', 'A monster whose motives are entirely clear'], 0),
   ('How does weird fictions cosmic horror differ from a typical ghost story with a clearly resolved cause?', ['It emphasizes the incomprehensibility and indifference of the universe rather than offering a resolvable threat', 'It always provides a complete, tidy explanation for every event', 'It contains no sense of fear or dread at all', 'It focuses entirely on realistic, everyday concerns'], 0),
   ('Why might a writer of weird fiction leave the central threat vague or only partially explained?', ['To preserve a sense of the unknowable that generates cosmic dread', 'Because fully explaining a threat always increases its horror', 'Because vague threats are required by law in this genre', 'Because leaving details vague eliminates all sense of atmosphere'], 0)]),
AF('Statistics: The Central Limit Theorem',
   'Grade 12 Advanced Functions strand: the central limit theorem states that the distribution of sample means drawn from a population approaches a normal distribution as the sample size grows large, regardless of the shape of the original population distribution.',
   [('What does the central limit theorem describe?', ['The distribution of sample means approaching a normal distribution as sample size grows large', 'The exact height of a single randomly chosen individual', 'A rule that applies only to perfectly normal populations', 'The total sum of every value in an entire population'], 0),
    ('What happens to the sampling distribution of the mean as sample size increases, according to the theorem?', ['It approaches a normal distribution', 'It becomes increasingly unpredictable with no pattern', 'It always becomes perfectly uniform', 'It shrinks to a single fixed point with no variation'], 0),
    ('Does the central limit theorem require the original population to already be normally distributed?', ['No, it holds regardless of the shape of the original population', 'Yes, it only applies when the population is already normal', 'Yes, and it fails completely for any other population shape', 'The theorem does not apply to any real population'], 0),
    ('Why is the central limit theorem considered foundational to inferential statistics?', ['It justifies using normal-distribution-based methods for sample means even from non-normal populations', 'It proves that no statistical inference is ever possible', 'It only applies to a single specific data set with no generalization', 'It eliminates the need for any sampling at all'], 0),
    ('How does the central limit theorem connect to the normal distribution studied earlier in this course?', ['It shows that sample means tend toward that same normal distribution as sample size grows', 'It shows the normal distribution can never describe sample means', 'It has no connection to the normal distribution at all', 'It replaces the normal distribution with the Poisson distribution entirely'], 0)]),
CA('Equilibrium Solutions and the Stability of Differential Equations',
   'Grade 12 Calculus strand: an equilibrium solution of a differential equation is a constant solution at which the rate of change is zero, and its stability describes whether nearby solutions move toward or away from it over time, a key idea in analyzing models such as population growth.',
   [('What defines an equilibrium solution of a differential equation?', ['A constant solution at which the rate of change is zero', 'A solution that changes at the fastest possible rate', 'A solution defined only for negative values of time', 'A solution with no relationship to the rate of change'], 0),
    ('What does the stability of an equilibrium solution describe?', ['Whether nearby solutions move toward or away from it over time', 'The exact numerical value of the equilibrium alone', 'Whether the differential equation has any solution at all', 'The colour used to graph the solution curve'], 0),
    ('What characterizes a stable equilibrium in terms of nearby solutions?', ['Nearby solutions move toward the equilibrium over time', 'Nearby solutions move away from the equilibrium over time', 'Nearby solutions remain exactly on the equilibrium at all times', 'Nearby solutions have no relationship to the equilibrium at all'], 0),
    ('In which earlier-studied model do equilibrium solutions naturally arise?', ['Logistic growth models', 'A model with no rate of change involved', 'A purely static geometric shape', 'A model that never reaches a constant value'], 0),
    ('Why is analyzing equilibrium and stability useful when studying a population model?', ['It reveals the long-term behaviour of the population without solving the full equation explicitly', 'It provides no information about the models long-term behaviour', 'It requires discarding the original differential equation entirely', 'It only applies to models with no population involved'], 0)]),
PH('The Rayleigh Criterion and the Resolving Power of Optical Instruments',
   'Grade 12 Physics strand: the Rayleigh criterion defines the minimum angular separation at which two point sources can be distinguished as separate by an optical instrument, based on the diffraction pattern produced by the instruments aperture, setting a fundamental limit on resolving power.',
   [('What does the Rayleigh criterion define?', ['The minimum angular separation at which two point sources can be resolved as separate', 'The exact colour of light emitted by a star', 'The total mass of an optical instrument', 'The maximum possible speed of light in any medium'], 0),
    ('What physical phenomenon underlies the resolution limit described by the Rayleigh criterion?', ['Diffraction produced by the instruments aperture', 'The complete absence of any light entering the instrument', 'Gravitational lensing around a distant star', 'Radioactive decay within the instrument itself'], 0),
    ('What does resolving power describe for an optical instrument?', ['Its ability to distinguish closely spaced objects as separate', 'Its total weight and physical size', 'Its ability to change the colour of incoming light', 'Its capacity to store electrical energy'], 0),
    ('How does aperture size generally affect resolving power according to the Rayleigh criterion?', ['A larger aperture generally improves resolving power', 'Aperture size has no effect on resolving power at all', 'A larger aperture always worsens resolving power', 'Resolving power depends only on the colour of the instrument'], 0),
    ('Why does diffraction, rather than lens imperfection alone, set a fundamental limit on resolution?', ['Diffraction is an intrinsic wave effect present even in a perfect, flawless optical system', 'Diffraction only occurs in instruments with significant lens defects', 'Diffraction can always be eliminated by using a larger lens', 'Diffraction has no connection to the wave nature of light'], 0)]),
]),
day(149, [
E('The Serial Novel: Dickens and Publication in Instalments',
  'Grade 12 English strand: the serial novel was published in regular instalments, often monthly, in newspapers or magazines, a format popularized by writers such as Charles Dickens that shaped narrative pacing through cliffhangers and episodic structure suited to a paying, ongoing readership.',
  [('How was a serial novel typically published?', ['In regular instalments, often monthly, in newspapers or magazines', 'As a single complete volume with no instalments at all', 'Only after the authors death, with no instalments', 'Exclusively as a private, unpublished manuscript'], 0),
   ('Which nineteenth-century writer is closely associated with popularizing the serial novel format?', ['Charles Dickens', 'Emily Dickinson', 'Sophocles', 'Homer'], 0),
   ('What narrative device did serial publication commonly encourage at the end of an instalment?', ['A cliffhanger', 'A complete resolution with no remaining tension', 'A detailed appendix of footnotes', 'A blank page with no content at all'], 0),
   ('How did serial publication shape a novels overall structure?', ['It encouraged an episodic structure suited to the pacing of each instalment', 'It required the entire novel to be written and revealed at once', 'It eliminated the need for any structure whatsoever', 'It forced every novel to have exactly one chapter'], 0),
   ('Why might serial publication have influenced an authors relationship with their readers?', ['An ongoing, paying readership could shape the reception and even the direction of the unfolding story', 'Readers had no access to a serialized novel until it was fully finished', 'Serial publication removed all contact between author and reader', 'Authors were legally forbidden from responding to reader reaction'], 0)]),
AF('Discrete Math: Spanning Trees and Kruskals Algorithm',
   'Grade 12 Advanced Functions strand: a spanning tree of a connected graph is a subgraph that includes every vertex and is itself a tree, and Kruskals algorithm constructs a minimum-weight spanning tree by repeatedly adding the cheapest edge that does not create a cycle.',
   [('What is a spanning tree of a connected graph?', ['A subgraph that includes every vertex of the graph and is itself a tree', 'A subgraph that excludes most of the graphs vertices', 'A single isolated vertex with no edges at all', 'A graph that contains every possible cycle'], 0),
    ('What does Kruskals algorithm construct?', ['A minimum-weight spanning tree', 'The graph with the maximum possible number of cycles', 'A list of every vertex with no edges included', 'A completely disconnected version of the original graph'], 0),
    ('What rule does Kruskals algorithm follow when selecting edges to add?', ['It repeatedly adds the cheapest edge that does not create a cycle', 'It adds every edge in the graph regardless of weight', 'It selects edges at random with no rule at all', 'It always removes the most expensive edge first'], 0),
    ('Why must a valid spanning tree contain no cycles?', ['A tree, by definition, is connected and acyclic', 'Cycles are required for a graph to be considered a tree', 'Spanning trees are permitted to contain any number of cycles', 'Acyclic graphs cannot be connected under any circumstances'], 0),
    ('How does Kruskals algorithm build on the graph theory basics of vertices and edges studied earlier?', ['It builds directly on that vertex and edge structure to select a minimal connecting subset of edges', 'It has no relationship to vertices or edges at all', 'It only applies to graphs with no edges whatsoever', 'It replaces vertices and edges with an entirely different structure'], 0)]),
CA('The Improved Euler (Heun) Method for Numerical Differential Equations',
   'Grade 12 Calculus strand: the improved Euler method, also called Heuns method, refines the basic Euler method for numerically solving differential equations by averaging the slope at the beginning and estimated end of each step, improving accuracy over a single-slope approximation.',
   [('What does the improved Euler (Heun) method refine?', ['The basic Euler method for numerically solving differential equations', 'The trapezoid rule for definite integrals', 'The method of undetermined coefficients', 'The bisection method for finding roots'], 0),
    ('What does the improved Euler method average to compute each step of its solution?', ['The slope at the beginning and the estimated slope at the end of the step', 'The value of the function at two entirely unrelated points', 'The step size alone, with no reference to slope', 'The initial condition and the final answer, with no intermediate steps'], 0),
    ('Why does averaging two slope estimates improve accuracy over the basic Euler method?', ['It better approximates the curves changing slope across the step rather than relying on only the initial slope', 'Averaging always makes a numerical method less accurate', 'It removes the need for an initial condition entirely', 'It requires no calculation of any slope at all'], 0),
    ('How does the improved Euler method relate to the Runge-Kutta methods studied earlier in this course?', ['It is a simpler, lower-order relative of the more general Runge-Kutta family', 'It has no mathematical relationship to Runge-Kutta methods', 'It is a far more advanced and complex method than any Runge-Kutta method', 'Runge-Kutta methods were derived without any reference to Eulers method'], 0),
    ('What type of problem is the improved Euler method typically applied to?', ['Initial value problems for ordinary differential equations', 'Purely algebraic equations with no derivatives', 'Static geometry problems involving no rates of change', 'Problems with no numerical component at all'], 0)]),
PH('The Thomson Effect and Thermoelectric Circuits',
   'Grade 12 Physics strand: the Thomson effect describes the heating or cooling that occurs when an electric current flows through a conductor along which a temperature gradient already exists, a third thermoelectric phenomenon alongside the Seebeck and Peltier effects studied earlier in this course.',
   [('What does the Thomson effect describe?', ['Heating or cooling that occurs when current flows through a conductor with an existing temperature gradient', 'The complete absence of heat transfer in any conductor', 'A change in a materials colour caused by an electric current', 'A phenomenon that occurs only in a perfect vacuum with no conductor'], 0),
    ('What must already exist along a conductor for the Thomson effect to occur?', ['A temperature gradient', 'A perfectly uniform temperature throughout', 'A complete absence of any electric current', 'An external magnetic field with no current involved'], 0),
    ('Alongside which two thermoelectric effects studied earlier does the Thomson effect belong?', ['The Seebeck effect and the Peltier effect', 'The Doppler effect and the Compton effect', 'The photoelectric effect and the Zeeman effect', 'The Hall effect and the Coriolis effect'], 0),
    ('What direction of energy transfer can the Thomson effect produce in a current-carrying conductor?', ['Either heating or cooling, depending on the direction of current relative to the temperature gradient', 'Only heating, under every possible condition', 'Only cooling, under every possible condition', 'No energy transfer of any kind, regardless of conditions'], 0),
    ('Why are the Seebeck, Peltier, and Thomson effects grouped together as thermoelectric phenomena?', ['Each describes a distinct interaction between heat flow and electric current in a conductor', 'They describe entirely unrelated phenomena with no shared theme', 'They only apply to conductors at absolute zero temperature', 'They describe interactions between light and matter, not heat and current'], 0)]),
]),
day(150, [
E('English Review: Detective Fiction, Naturalism, and Popular Forms',
  'Grade 12 English strand review: students revisit the mock-epic, the pastoral tradition, detective fiction and the golden age whodunit, literary naturalism, and memoir and the art of life writing.',
  [('What does a mock-epic typically do with the grand conventions of epic poetry?', ['Applies them to a trivial or minor subject to create a comic, satirical effect', 'Uses them only to describe genuine historical battles', 'Removes all poetic devices from the epic form', 'Turns the epic into a private diary with no audience'], 0),
   ('What does the pastoral tradition typically idealize?', ['Rural life and nature, often voiced through shepherd or rustic figures', 'The complexity and noise of city life', 'Industrial machinery and urban commerce', 'The corruption of royal courts with no counterpoint'], 0),
   ('What structure typically defines golden age detective fiction?', ['A puzzle-like mystery solved through logical deduction from carefully planted clues', 'A story with no crime or mystery of any kind', 'A tale told entirely without a detective figure', 'A narrative that reveals the culprit before any investigation begins'], 0),
   ('What forces do naturalist novels typically emphasize as shaping character?', ['Heredity, environment, and social forces beyond the characters control', 'Pure random chance with no underlying pattern at all', 'Only the characters own free choices, with no outside influence', 'Supernatural forces such as ghosts and spirits'], 0),
   ('What does memoir typically reconstruct?', ['A specific period or theme from the authors own life', 'A complete, chronological record of an entire life from birth to the present', 'A purely fictional life invented for entertainment', 'A biography of a person the author has never met'], 0)]),
AF('AdvancedFunctions Review: Statistics, Algebra, and Graph Theory',
   'Grade 12 Advanced Functions strand review: students revisit the Poisson distribution, the law of quadratic reciprocity, group theory, Boolean algebra and logic gates, and correlation and the Pearson correlation coefficient.',
   [('What kind of events does the Poisson distribution typically model?', ['Rare, independent events occurring a certain number of times in a fixed interval', 'Events that always occur at exactly the same time', 'Events with no possible variation whatsoever', 'Only events with a probability of exactly one half'], 0),
    ('What does the law of quadratic reciprocity relate?', ['Whether p is a quadratic residue modulo q to whether q is a quadratic residue modulo p', 'The sum of two unrelated even numbers', 'The number of divisors of a composite number only', 'The value of an unrelated trigonometric identity'], 0),
    ('What four properties define a group under its operation?', ['Closure, associativity, an identity element, and inverses for every element', 'Only closure, with no other requirements', 'Commutativity alone, with no identity element required', 'A requirement that the set contain exactly one element'], 0),
    ('What values does Boolean algebra fundamentally operate on?', ['True and false (or one and zero) values', 'Only irrational numbers', 'Complex numbers exclusively', 'Negative fractions only'], 0),
    ('What does the Pearson correlation coefficient measure?', ['The strength and direction of the linear relationship between two quantitative variables', 'The exact mean of a single data set', 'The total number of data points collected', 'The mode of a categorical variable'], 0)]),
CA('Calculus Review: Differential Equations and Numerical Methods',
   'Grade 12 Calculus strand review: students revisit Cauchy-Euler equations, exact differential equations, the secant method, Romberg integration, and the inverse Laplace transform.',
   [('What distinguishes a Cauchy-Euler equation from the constant-coefficient equations studied earlier?', ['Its coefficients are powers of the independent variable rather than constants', 'It has no derivatives of any kind', 'It can only be solved numerically, never analytically', 'It is always a first-order equation'], 0),
    ('What does it mean for a first-order differential equation to be exact?', ['It can be written as the differential of some underlying function', 'It has no solution under any circumstances', 'It must always be solved using only numerical methods', 'It requires no partial derivatives to analyze'], 0),
    ('What line does the secant method use to generate its next root approximation?', ['A line through two nearby points on the curve', 'A vertical line through a single point', 'A line tangent to the curve at one point only', 'A line with no relationship to the curve'], 0),
    ('What numerical integration method does Romberg integration build upon and improve?', ['The trapezoid rule', 'The method of undetermined coefficients', 'Lagrange interpolation alone', 'The bisection method for root-finding'], 0),
    ('What does the inverse Laplace transform do?', ['Converts a function of s back into a function of t', 'Converts a function of t into an unrelated function of x', 'Removes all variables from a function entirely', 'Doubles the degree of a polynomial function'], 0)]),
PH('Physics Review: Fluid, Optical, and Electromagnetic Effects',
   'Grade 12 Physics strand review: students revisit the Magnus effect, the Venturi effect and Bernoullis principle, total internal reflection, Newtons rings, and the Tyndall effect.',
   [('What is the Magnus effect?', ['The curved path taken by a spinning object moving through a fluid, caused by a sideways lift force', 'The tendency of an object to fall in a perfectly straight line', 'The complete absence of drag on a spinning object', 'A magnetic force acting on any moving object'], 0),
    ('What does the Venturi effect describe?', ['A drop in fluid pressure as the fluid speeds up through a constricted section of a pipe', 'A rise in fluid pressure whenever a pipe widens', 'The complete stopping of fluid flow at a constriction', 'A change in fluid temperature with no change in pressure'], 0),
    ('What is total internal reflection?', ['Light reflecting entirely back into a denser medium when it strikes a boundary at an angle greater than the critical angle', 'Light passing completely unaffected through any boundary', 'The complete absorption of light at any surface', 'A phenomenon that only occurs with sound waves'], 0),
    ('What pattern do Newtons rings form?', ['Concentric bright and dark circular fringes', 'A single straight bright line with no pattern', 'A random, non-repeating scatter of colour', 'A uniform, unchanging field of one colour'], 0),
    ('What is the Tyndall effect?', ['The scattering of light by particles suspended in a colloid, making a beam of light visible from the side', 'The complete absorption of all light by a transparent solution', 'A phenomenon that only occurs in a perfect vacuum', 'The bending of light as it passes through a single flat pane of glass'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g12_141_150)
    append_to(12, g12_141_150)
