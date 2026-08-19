#!/usr/bin/env python3
"""Grade 12, Days 181-187 -- the FINAL batch for this grade, completing the
full 187-day Ontario curriculum target (180 existing days + 7 new days =
187). Structured as 6 new content days (181-186, one new topic per subject
per day) plus Day 187 as a single final cross-subject review day, since
187 = 180 + 7 rather than the usual +10.

Topics chosen after dumping the complete existing Day 1-180 title list
(data/grade12.json, 720 subject entries -- Grade 12 has now been mined
across eighteen prior batches) and checking every candidate title and key
term against that full dump before writing any content. New topics for
this batch:

English (literary forms/genres/theory/writing/media/drama angles not yet
covered): the masque as a Renaissance courtly dramatic form (distinct from
the already-covered morality play, closet drama, and revenge tragedy);
Horatian versus Juvenalian satire as two tonal modes of satiric writing
(distinct from the already-covered general satire unit and Menippean
satire, which is defined by its target rather than its tone); cyberpunk as
a science-fiction subgenre (distinct from the already-covered climate
fiction / cli-fi and general speculative fiction); ecocriticism as a
literary-theoretical lens (distinct from the already-covered ecofeminism,
which specifically foregrounds gender); radio drama as an audio broadcast
storytelling form (distinct from the already-covered podcast / serial
audio storytelling, which is a later, on-demand digital form); and the
video essay as a contemporary audiovisual analytical form (distinct from
the already-covered video game narrative and podcast topics).

Advanced Functions (statistics/discrete math/number theory/functions
angles not yet covered): the bootstrap method / resampling (distinct from
the already-covered confidence intervals, which it complements); the
Kolmogorov-Smirnov test (distinct from the already-covered chi-squared
goodness of fit test); Kuratowskis theorem on graph planarity (distinct
from the already-covered Eulers formula for planar graphs -- a different
theorem about a related but separate question); Halls marriage theorem on
bipartite matching (distinct from the already-covered stable marriage
problem / Gale-Shapley algorithm, which adds a preference-stability
condition Halls theorem does not address); primitive roots and
multiplicative order modulo n (distinct from the already-covered Eulers
totient function, quadratic residues, and Fermats little theorem, though
related to all three); and the Dirichlet function (distinct from the
already-covered Weierstrass function -- continuous-nowhere-differentiable
versus discontinuous-everywhere are different pathological examples). Note:
an initial candidate, "Chebyshevs inequality," was dropped after the dedup
dump turned up "Chebyshev Polynomials" (Day 139) -- different concept, but
close enough in name to risk confusion -- and replaced with the bootstrap
method instead.

Calculus (differential equations/multivariable/series/numerical methods
angles not yet covered): the Riccati equation (distinct from the
already-covered Bernoulli, Clairaut, and Cauchy-Euler equations); reduction
of order (distinct from the already-covered Wronskian and variation of
parameters, which assume a different starting point); Picard iteration
(distinct from the already-covered existence and uniqueness theorem, which
it underlies but does not duplicate); Newton-Cotes quadrature as the
general framework unifying the already-covered trapezoid rule, Simpsons
rule, and midpoint rule (a genuinely distinct topic: the unifying
polynomial-degree framework itself, not a repeat of any single rule); the
surface area of a parametric surface (distinct from the already-covered
surface integrals, which measure flux rather than area, and from arc
length of a parametric curve, a lower-dimensional analogue); and the
Cauchy condensation test (distinct from the already-covered comparison,
ratio, root, integral, alternating series, limit comparison, Dirichlet,
and Abel tests). Note: an initial candidate, "the finite difference
method," was dropped after the dedup dump turned up Day 82, "Numerical
Differentiation Methods," which already covers finite-difference
derivative estimates -- replaced with Picard iteration instead.

Physics (mechanics/EM/optics/quantum/astro/condensed-matter angles not yet
covered): Keplers three laws of orbital motion (distinct from the
already-covered general circular motion/gravitation unit and the
already-covered satellites/orbital mechanics day, neither of which names
the three laws or covers elliptical orbits specifically); Gauss law and
electric flux (distinct from the already-covered electric fields/potential
introduction); Youngs double-slit experiment (distinct from the
already-covered general wave superposition/interference unit and
diffraction day -- this is the specific historic two-slit experiment);
quantum decoherence (distinct from the already-covered quantum
entanglement and uncertainty principle); Hubbles law (distinct from the
already-covered cosmic microwave background/Big Bang and dark energy
topics, though related to all of them as a complementary line of
evidence); and crystal structure/unit cells (distinct from the
already-covered band theory of solids and phonons, which describe
electronic and vibrational behaviour rather than the underlying lattice
geometry itself).

Every one of these 24 titles and their key terms was checked against the
full Day 1-180 dump (grep -i across all four subjects) and confirmed
absent before being written into this file.

Day 187 is the single final review day for this grade, following the
exact per-subject review pattern used on every prior review day (Day 180,
170, 160, etc.): one review lesson per subject, each reusing the first
quiz question verbatim from each of that subjects five Day 181-185
lessons (mirroring the "first five of nine" pattern from Day 180, scaled
to "first five of six" here since this batch has six new days rather than
nine). Each of the four Day 187 review titles was checked against every
one of the 45 prior review titles for this grade (Days 11-180) and is
textually distinct from all of them. Because Day 187 is the very last day
of the entire 187-day K-12 curriculum build for Grade 12, its four review
lesson summaries acknowledge that this is a capstone, end-of-program
review, while the quiz content itself follows the identical mechanical
review format used throughout every prior batch.

Subject keys for Grade 12 are "English", "AdvancedFunctions", "Calculus",
"Physics" (same as all earlier Grade 12 batches).

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote or straight-apostrophe characters are used anywhere in
title/question/summary/option text; apostrophes and accented characters
are avoided entirely, matching the convention used since the Days 131-140
batch and followed exactly by the Days 171-180 batch immediately before
this one.
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


def _rebalance_answer_positions(days, seed=20260818):
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


g12_181_187 = [
day(181, [
E('Drama: The Masque and Courtly Spectacle on the Renaissance Stage',
  'Grade 12 English strand: a masque is a lavish, invitation-only Renaissance court entertainment that combines dance, music, elaborate costume and stage machinery, and allegorical poetry, typically staged once to mark a specific court occasion, with courtiers themselves often among the masked performers.',
  [('What combination of elements does a masque typically bring together?', ['Dance, music, elaborate costume and stage machinery, and allegorical poetry', 'Only spoken dialogue with no music, dance, or costume of any kind', 'A single unaccompanied song with no other performance element', 'Silent physical movement with no poetry, music, or spectacle'], 0),
   ('Who, besides professional performers, often took part in a masque?', ['Courtiers themselves, appearing among the masked performers', 'Only paid professional actors, with no courtier participation', 'Exclusively foreign ambassadors with no connection to the court', 'No performers ever wore masks in a masque'], 0),
   ('For what kind of occasion was a masque typically staged?', ['A specific court occasion, such as a wedding or royal visit, often performed only once', 'A recurring weekly public performance open to any paying audience', 'An occasion entirely unconnected to the royal court', 'A funeral exclusively, with no other occasion ever marked by a masque'], 0),
   ('How does the masque compare to the morality play studied in an earlier batch?', ['Both use allegorical figures to convey meaning, but the masque is a lavish court entertainment built around spectacle and celebration, while the morality play stages a moral allegory for a broader audience', 'The two forms are identical in audience, purpose, and staging', 'The morality play was performed exclusively for royal courts with elaborate stage machinery', 'The masque contains no allegorical content of any kind'], 0),
   ('Why is the masque considered significant in the history of theatrical spectacle?', ['Its integration of music, dance, elaborate design, and courtly performance influenced the later development of staged spectacle and opera', 'It had no influence on any later form of staged performance', 'The masque eliminated the need for any further development of theatrical spectacle', 'Masques were purely literary texts never actually staged or performed'], 0)]),
AF('Statistics: The Bootstrap Method and Resampling for Statistical Inference',
   'Grade 12 Advanced Functions strand: the bootstrap method estimates the sampling distribution of a statistic by repeatedly resampling, with replacement, from an observed data set, building an empirical picture of variability without relying on a known theoretical distribution.',
   [('What does the bootstrap method use to estimate the sampling distribution of a statistic?', ['Repeated resampling, with replacement, from an observed data set', 'A single fixed theoretical formula with no resampling involved', 'Resampling without replacement performed exactly once', 'An entirely new, independent experiment collected each time'], 0),
    ('What advantage does the bootstrap method offer compared to methods that rely on a known theoretical distribution?', ['It builds an empirical picture of variability without assuming a specific theoretical distribution', 'It requires assuming the data follows a normal distribution exactly', 'It removes any need to ever collect an original data sample', 'It guarantees a result identical to the true population parameter'], 0),
    ('What is distinctive about how a bootstrap sample is drawn from the original data?', ['The same observation can appear more than once because sampling is done with replacement', 'Each observation may be used only once across every resample combined', 'A bootstrap sample never draws from the original observed data', 'A bootstrap sample must always be larger than the original data set'], 0),
    ('How does the bootstrap method relate to confidence intervals studied in an earlier batch?', ['Both aim to quantify uncertainty around a sample estimate, though the bootstrap builds an interval empirically from resampled data rather than from a theoretical formula', 'The two concepts have no relationship to quantifying uncertainty', 'Confidence intervals can only ever be constructed through resampling', 'The bootstrap method removes the need to ever consider a sample estimate'], 0),
    ('Why is the bootstrap method especially useful for a statistic such as the median, where a simple theoretical formula for sampling variability is not readily available?', ['It provides a general, distribution-free way to approximate the variability of a statistic directly from the data itself', 'It only works for a statistic that already has a well-known theoretical formula', 'The bootstrap method cannot be applied to any statistic other than the mean', 'It removes the need to consider variability in any statistic'], 0)]),
CA('Differential Equations: The Riccati Equation and Its Link to Linear Second-Order Equations',
   'Grade 12 Calculus strand: a Riccati equation is a first-order differential equation containing a quadratic term in the unknown function, and a well-chosen substitution transforms it into a linear second-order differential equation, connecting a nonlinear first-order problem to more familiar linear theory.',
   [('What distinctive term appears in a Riccati equation that is not present in a standard linear first-order equation?', ['A quadratic term in the unknown function', 'A term involving no function of any kind', 'A term that is always identically zero', 'A term involving only the independent variable raised to the first power'], 0),
    ('What kind of equation can a Riccati equation be transformed into using a well-chosen substitution?', ['A linear second-order differential equation', 'A purely algebraic equation with no derivative present', 'An equation with no defined solution of any kind', 'A first-order equation with an identical quadratic term'], 0),
    ('What broader benefit does transforming a Riccati equation into a linear second-order equation provide?', ['It connects a nonlinear first-order problem to more familiar and well-developed linear theory', 'It removes any possibility of finding a solution to the original equation', 'It shows that the Riccati equation never had a solution to begin with', 'It eliminates the need to consider the equation as a differential equation at all'], 0),
    ('How does the Riccati equation compare to the Bernoulli differential equation studied in an earlier batch?', ['Both are nonlinear first-order equations solved through a strategic substitution, though the Riccati equation is reduced to a linear second-order form while the Bernoulli equation is reduced to a linear first-order form', 'The two equations require exactly the same substitution and produce the same type of resulting equation', 'The Bernoulli equation always contains a quadratic term identical to the Riccati equation', 'Neither equation can be solved using any substitution technique'], 0),
    ('Why is the Riccati equation considered an important bridge between nonlinear and linear differential equation theory?', ['It shows that a specific class of nonlinear equations can be fully understood through the well-established tools developed for linear equations', 'It proves that nonlinear and linear differential equations can never be related to one another', 'The Riccati equation has no known method of solution of any kind', 'It applies only to equations with no quadratic term present'], 0)]),
PH('Keplers Laws and the Geometry of Orbital Motion',
   'Grade 12 Physics strand: Keplers three laws of planetary motion describe orbits as ellipses with the Sun at one focus, state that a planet sweeps out equal areas in equal times, and relate the square of a planets orbital period to the cube of its average orbital distance.',
   [('According to Keplers first law, what shape does a planets orbit take, and where is the Sun located?', ['An ellipse, with the Sun at one focus', 'A perfect circle, with the Sun at its exact centre', 'A straight line passing directly through the Sun', 'A shape with no defined geometric form at all'], 0),
    ('What does Keplers second law state about the area a planet sweeps out as it orbits?', ['A planet sweeps out equal areas in equal times', 'A planet sweeps out a constantly increasing area regardless of time elapsed', 'A planet never sweeps out any measurable area', 'The area swept out depends only on the planets colour'], 0),
    ('What relationship does Keplers third law establish?', ['The square of a planets orbital period is proportional to the cube of its average orbital distance', 'The orbital period has no relationship whatsoever to orbital distance', 'The orbital period is always exactly equal to the orbital distance', 'The cube of the orbital period equals the square of the planets mass'], 0),
    ('How do Keplers laws relate to the general treatment of orbital mechanics studied in an earlier batch?', ['Keplers laws give the precise geometric and timing description of orbital motion, including elliptical orbits, that the earlier general treatment of satellites and orbital balance builds upon', 'Keplers laws and orbital mechanics describe entirely unrelated physical phenomena', 'Keplers laws apply only to circular orbits and never to any elliptical path', 'Orbital mechanics was developed with no reference to elliptical motion of any kind'], 0),
    ('Why are Keplers laws considered a foundational achievement in the history of physics?', ['They provided an accurate, purely geometric description of planetary motion that later motivated Newtons law of universal gravitation', 'They have no connection to the later development of gravitational theory', 'Keplers laws were derived entirely from Newtons law of gravitation and added no new information', 'They describe only the motion of stars and have no application to planets'], 0)]),
]),
day(182, [
E('Writing: Horatian and Juvenalian Satire -- Two Modes of Satiric Tone',
  'Grade 12 English strand: Horatian satire uses a light, witty, good-humoured tone to gently mock human folly, while Juvenalian satire uses a harsh, indignant, and often bitter tone to attack vice and corruption, giving satirists two distinct rhetorical registers for the same critical purpose.',
  [('What tone characterizes Horatian satire?', ['A light, witty, good-humoured tone that gently mocks human folly', 'A harsh, bitter tone aimed at severe moral condemnation', 'A tone entirely devoid of any humour or wit', 'A tone that avoids commenting on human behaviour altogether'], 0),
   ('What tone characterizes Juvenalian satire?', ['A harsh, indignant, and often bitter tone that attacks vice and corruption', 'A gentle, affectionate tone with no critical edge', 'A tone limited strictly to praise with no criticism at all', 'A tone that never addresses any moral or social failing'], 0),
   ('What do Horatian and Juvenalian satire share despite their different tones?', ['Both use satire for the same broad critical purpose of exposing human folly or vice', 'Both avoid any critical or corrective purpose whatsoever', 'Both are written exclusively in formal academic prose with no wit', 'Neither mode has any connection to satire as a genre'], 0),
   ('How does the Horatian and Juvenalian distinction compare to Menippean satire studied in an earlier batch?', ['All three are satiric modes, but Horatian and Juvenalian describe a spectrum of tone from gentle to harsh, while Menippean satire is defined instead by its target of mocking intellectual attitudes rather than specific persons', 'The three modes describe the exact same satiric technique with no distinction', 'Menippean satire is simply another name for the Horatian mode', 'Juvenalian satire and Menippean satire share an identical tone in every case'], 0),
   ('Why is it useful for a writer or reader to distinguish between Horatian and Juvenalian satiric tone?', ['Recognizing the intended tone shapes how sharply a satire is meant to sting and how an audience is meant to respond to its criticism', 'The distinction has no bearing on how a satirical text should be read or written', 'Every satirical work uses exactly the same tone regardless of its author or purpose', 'Tone is irrelevant to the effectiveness of satire as a literary mode'], 0)]),
AF('Statistics: The Kolmogorov-Smirnov Test for Comparing Distributions',
   'Grade 12 Advanced Functions strand: the Kolmogorov-Smirnov test compares an observed data set to a reference distribution, or compares two data sets to each other, by measuring the largest gap between their cumulative distribution functions, providing a nonparametric way to test whether the data plausibly came from that distribution.',
   [('What quantity does the Kolmogorov-Smirnov test measure to compare two distributions?', ['The largest gap between their cumulative distribution functions', 'The average of every individual data point in both sets', 'The total number of data points collected in each set', 'The colour or category label assigned to each observation'], 0),
    ('What two kinds of comparisons can the Kolmogorov-Smirnov test perform?', ['Comparing an observed data set to a reference distribution, or comparing two data sets to each other', 'Comparing a single number to itself with no data set involved', 'Comparing only categorical labels with no numerical values', 'Comparing a data set to a value that is always exactly zero'], 0),
    ('What kind of statistical test is the Kolmogorov-Smirnov test, in terms of its assumptions about the data?', ['A nonparametric test, since it does not assume a specific parametric form for the underlying distribution', 'A test that requires assuming the data is drawn from a normal distribution', 'A test that can only be applied to a data set of exactly one observation', 'A test that assumes every observation in the data set is identical'], 0),
    ('How does the Kolmogorov-Smirnov test relate to the chi-squared goodness of fit test studied in an earlier batch?', ['Both test whether observed data is consistent with a reference distribution, though the chi-squared test compares binned counts while the Kolmogorov-Smirnov test compares cumulative distribution functions directly', 'The two tests are identical in every computational detail', 'The chi-squared test can only be applied to continuous, unbinned data', 'The Kolmogorov-Smirnov test requires grouping data into categories before it can be used'], 0),
    ('Why is the Kolmogorov-Smirnov test a useful tool alongside parametric tests such as the t-test studied in an earlier batch?', ['It allows a comparison of distributions without assuming the data follows a specific parametric form, which is valuable when that assumption is doubtful', 'It always produces exactly the same conclusion as every parametric test', 'It can only be used when the data is already known to be normally distributed', 'It removes any need to ever compare an observed data set to a reference distribution'], 0)]),
CA('Reduction of Order for Second-Order Linear Differential Equations',
   'Grade 12 Calculus strand: reduction of order finds a second, independent solution to a second-order linear differential equation once one solution is already known, by substituting a product of the known solution and an unknown function and solving the resulting simpler equation for that function.',
   [('What does reduction of order require to already be known before it can be applied?', ['One solution to the second-order linear differential equation', 'Both solutions to the differential equation', 'The exact numerical value of every constant in the equation', 'No information about the differential equation at all'], 0),
    ('What substitution does reduction of order use to find a second, independent solution?', ['A product of the known solution and an unknown function', 'A substitution involving no reference to the known solution', 'A constant multiple of the known solution alone', 'A substitution that eliminates the known solution entirely'], 0),
    ('What kind of equation results after this substitution is applied?', ['A simpler equation that can be solved for the previously unknown function', 'An equation identical in complexity to the original problem', 'An equation with no defined unknown function remaining', 'An algebraic equation containing no derivatives whatsoever'], 0),
    ('How does reduction of order relate to the Wronskian studied in an earlier batch?', ['The Wronskian can be used to confirm that the solution produced by reduction of order is genuinely independent from the originally known solution', 'The Wronskian has no relevance to confirming independence of solutions', 'Reduction of order always produces a solution identical to the one already known', 'The Wronskian can only be computed when just one solution is known'], 0),
    ('Why is reduction of order a valuable technique when solving a second-order linear differential equation?', ['It extends a single known solution into a complete general solution by systematically constructing a second, independent one', 'It has no practical use once a single solution to an equation is already known', 'The technique can only be applied to equations with no known solution at all', 'It always produces a solution that is a constant multiple of the first, offering no new information'], 0)]),
PH('Gauss Law and Electric Flux Through a Closed Surface',
   'Grade 12 Physics strand: Gauss law relates the total electric flux passing through any closed surface to the net electric charge enclosed within that surface, offering a powerful shortcut for finding the electric field of highly symmetric charge distributions.',
   [('What does Gauss law relate the total electric flux through a closed surface to?', ['The net electric charge enclosed within that surface', 'The colour and material of the surface itself', 'The total surface area of the enclosing shape alone', 'The distance of the surface from the nearest magnet'], 0),
    ('For what kind of charge distribution does Gauss law offer a particularly powerful shortcut for finding the electric field?', ['Highly symmetric charge distributions', 'Distributions with no symmetry of any kind', 'Only a single stationary point charge in complete isolation from any surface', 'Distributions that produce no electric field whatsoever'], 0),
    ('What is meant by electric flux through a surface, in this context?', ['A measure of how much electric field passes through that surface', 'A measure of the surfaces temperature', 'A measure of the surfaces electrical resistance', 'A measure with no connection to the electric field at all'], 0),
    ('How does Gauss law relate to the concept of the electric field and potential studied in an earlier batch?', ['Gauss law provides an alternative, flux-based method for determining the electric field, complementing the direct field and potential calculations studied earlier, especially for symmetric charge arrangements', 'Gauss law has no connection to the electric field of a charge distribution', 'Electric potential can only ever be found using Gauss law and no other method', 'Gauss law applies only to magnetic fields and never to electric fields'], 0),
    ('Why is Gauss law considered a powerful problem-solving tool in electrostatics?', ['It can determine the electric field of a symmetric charge distribution far more directly than summing the contributions of individual charges', 'It provides no computational advantage over any other method of finding an electric field', 'Gauss law can only be applied to a single isolated point charge with no surrounding surface', 'It relates electric flux to a quantity that has no connection to enclosed charge'], 0)]),
]),
day(183, [
E('Literature: Cyberpunk and the Aesthetics of Corporate Dystopia',
  'Grade 12 English strand: cyberpunk is a science fiction subgenre that combines advanced computer and biotechnology with a gritty, high-tech-low-life urban setting, typically depicting powerful corporations, decaying social order, and characters navigating a world where technology has outpaced its ethical or political control.',
  [('What two elements does cyberpunk combine as central features of its setting?', ['Advanced computer and biotechnology with a gritty, high-tech-low-life urban setting', 'Medieval technology with a rural agricultural setting', 'An absence of any technology with a peaceful pastoral setting', 'Ancient mythology with no reference to technology of any kind'], 0),
   ('What kind of institutions typically hold power in a cyberpunk setting?', ['Powerful corporations, often exceeding the influence of traditional governments', 'Small independent farms with no broader influence', 'Institutions with no interest in technology or control', 'A single unified world government with no corporate influence at all'], 0),
   ('What tension is often central to a cyberpunk narrative?', ['A world where technology has outpaced its ethical or political control', 'A world where technology has never developed beyond the most basic tools', 'A tension with no connection to technology or its consequences', 'A perfectly ordered society with no social decay of any kind'], 0),
   ('How does cyberpunk compare to climate fiction, or cli-fi, studied in an earlier batch?', ['Both are speculative genres imagining near-future consequences of present-day forces, though cyberpunk centres on technology and corporate power while cli-fi centres on environmental change', 'The two genres are identical in setting, theme, and central concern', 'Climate fiction always depicts a high-tech-low-life urban setting dominated by corporations', 'Cyberpunk has no connection to imagining any kind of future society'], 0),
   ('Why might cyberpunk be considered a genre well suited to critiquing contemporary anxieties about technology and corporate power?', ['Its exaggerated near-future setting allows writers to dramatize present-day concerns about surveillance, inequality, and unchecked technological growth', 'The genre avoids any commentary on real-world technological or social concerns', 'Cyberpunk narratives are set so far in the past that they cannot reflect on modern technology', 'Corporate power and technology have no relevance to the genres central concerns'], 0)]),
AF('Discrete Math: Kuratowskis Theorem and the Planarity of Graphs',
   'Grade 12 Advanced Functions strand: Kuratowskis theorem states that a graph is planar, meaning it can be drawn in the plane with no edges crossing, if and only if it contains no subdivision of the two specific forbidden graphs known as K5 and K3,3, giving a precise structural test for planarity.',
   [('What does it mean for a graph to be planar?', ['It can be drawn in the plane with no edges crossing', 'It must contain at least one pair of crossing edges', 'It has no vertices or edges of any kind', 'It can only be drawn using exactly two dimensions of colour'], 0),
    ('According to Kuratowskis theorem, what determines whether a graph is planar?', ['Whether the graph contains no subdivision of the two forbidden graphs K5 and K3,3', 'Whether the graph has an even number of vertices', 'Whether every vertex in the graph has exactly the same degree', 'Whether the graph contains any edges at all'], 0),
    ('What kind of test does Kuratowskis theorem provide for determining planarity?', ['A precise structural test based on forbidden subgraphs', 'A test that relies entirely on counting the number of colours needed', 'A test with no connection to the structure of the graph', 'A test that can only be applied to graphs with no edges'], 0),
    ('How does Kuratowskis theorem relate to Eulers formula for planar graphs studied in an earlier batch?', ['Both concern planar graphs, though Eulers formula relates the counts of vertices, edges, and faces for a planar graph, while Kuratowskis theorem gives a structural criterion for determining planarity in the first place', 'The two results state exactly the same relationship between vertices and edges', 'Eulers formula determines planarity using the same forbidden subgraphs as Kuratowskis theorem', 'Kuratowskis theorem has no connection to the study of planar graphs'], 0),
    ('Why is Kuratowskis theorem considered a foundational result in graph theory?', ['It gives a complete and precise characterization of exactly which graphs can be drawn without any crossing edges', 'It shows that every graph, without exception, is planar', 'The theorem provides no way to determine whether a given graph is planar', 'It applies only to graphs with a single vertex and no edges'], 0)]),
CA('Numerical Methods: Picard Iteration and Successive Approximation for Initial Value Problems',
   'Grade 12 Calculus strand: Picard iteration approximates the solution to an initial value problem by converting the differential equation into an equivalent integral equation and repeatedly substituting an improving approximation into that integral, generating a sequence of functions that converges toward the exact solution.',
   [('What does Picard iteration convert a differential equation into before beginning its approximation process?', ['An equivalent integral equation', 'A purely algebraic equation with no integral or derivative present', 'A system of unrelated equations with no connection to the original problem', 'A differential equation of a strictly higher order'], 0),
    ('What does Picard iteration repeatedly do to generate successive approximations?', ['Substitute an improving approximation into the integral equation', 'Discard every previous approximation and start from a new random guess', 'Differentiate the original equation repeatedly with no integration involved', 'Ignore the initial condition entirely at every step'], 0),
    ('What does the sequence of functions generated by Picard iteration do under suitable conditions?', ['Converge toward the exact solution of the initial value problem', 'Diverge without bound regardless of the starting approximation', 'Remain fixed at the initial guess with no further change', 'Oscillate forever with no defined limiting function'], 0),
    ('How does Picard iteration relate to the existence and uniqueness theorem for differential equations studied in an earlier batch?', ['Picard iteration provides a constructive method whose convergence underlies the proof of the existence and uniqueness theorem for a well-posed initial value problem', 'The two concepts have no relationship to one another', 'The existence and uniqueness theorem guarantees that Picard iteration will never converge', 'Picard iteration can only be applied to equations already known to have no solution'], 0),
    ('Why is Picard iteration a valuable theoretical tool, even though it is rarely used for direct numerical computation compared to methods such as Runge-Kutta?', ['Its convergence argument helps justify that a solution to an initial value problem exists and is unique, providing a theoretical foundation for the numerical methods used in practice', 'It has no connection to justifying the existence of a solution', 'Picard iteration always converges instantly to the exact solution in a single step', 'The method is used exclusively for problems with no initial condition specified'], 0)]),
PH('Youngs Double-Slit Experiment and the Wave Nature of Light',
   'Grade 12 Physics strand: Youngs double-slit experiment passes light through two closely spaced narrow slits and observes the resulting pattern of bright and dark fringes on a screen, providing decisive early evidence that light behaves as a wave capable of interference.',
   [('What experimental setup does Youngs double-slit experiment use?', ['Light passed through two closely spaced narrow slits', 'A single wide opening with no second slit present', 'A solid opaque barrier with no opening of any kind', 'Light reflected from a single flat mirror with no slits involved'], 0),
    ('What pattern appears on a screen behind the two slits in Youngs experiment?', ['A pattern of alternating bright and dark fringes', 'A single uniform patch of light with no variation at all', 'Complete darkness across the entire screen', 'A pattern that changes colour but shows no variation in brightness'], 0),
    ('What did the fringe pattern observed in Youngs experiment provide early evidence for?', ['That light behaves as a wave capable of interference', 'That light travels only in perfectly straight lines with no wave behaviour', 'That light has no measurable speed', 'That light cannot pass through any narrow opening'], 0),
    ('How does Youngs double-slit experiment relate to wave superposition and interference studied in an earlier batch?', ['Youngs experiment is a specific, historically decisive demonstration of the general principle of wave interference and superposition applied to light', 'The two topics describe entirely unrelated wave phenomena', 'Wave superposition applies only to sound and never to light', 'Youngs experiment shows that light does not interfere with itself under any circumstance'], 0),
    ('Why is Youngs double-slit experiment considered a landmark result in the history of optics?', ['It provided compelling experimental support for the wave theory of light at a time when a purely particle-based view was widely favoured', 'It had no impact on the historical debate over the nature of light', 'The experiment proved conclusively that light has no wave properties whatsoever', 'It was performed after wave theory had already been universally accepted with no remaining debate'], 0)]),
]),
day(184, [
E('Literary Theory: Ecocriticism and Reading Literature Through an Environmental Lens',
  'Grade 12 English strand: ecocriticism examines how literature represents the natural world and the relationship between humans and their environment, asking how texts shape, reflect, or challenge cultural attitudes toward nature, land, and ecological crisis.',
  [('What does ecocriticism primarily examine in a literary text?', ['How the text represents the natural world and the relationship between humans and their environment', 'Only the texts publication date, with no reference to its content', 'The economic sales figures of the text with no reference to its themes', 'The biography of the author with no reference to environmental themes'], 0),
   ('What kind of questions does an ecocritical reading typically ask of a text?', ['How the text shapes, reflects, or challenges cultural attitudes toward nature, land, and ecological crisis', 'Questions concerned only with a texts rhyme scheme', 'Questions with no connection to the natural world at all', 'Questions concerned only with a texts publication history'], 0),
   ('What broad concern can motivate an ecocritical approach to reading literature?', ['A concern with ecological crisis and how literature represents human relationships to land and nature', 'A concern exclusively with grammar and sentence-level style', 'A concern with a texts commercial success alone', 'A concern that excludes any interest in the natural world'], 0),
   ('How does ecocriticism compare to ecofeminism, studied in an earlier batch?', ['Both examine the representation of the natural world in literature, though ecofeminism specifically foregrounds the intersection of gender and environment while ecocriticism addresses environmental representation more broadly', 'The two approaches are simply two different names for an identical critical method', 'Ecofeminism has no connection to environmental themes in literature', 'Ecocriticism only ever considers questions of gender and never questions of land or nature'], 0),
   ('Why might ecocriticism be considered an increasingly relevant critical lens for reading literature today?', ['Growing concern about ecological crisis has made how literature represents nature and human responsibility toward it a pressing critical question', 'Environmental themes have no relevance to how a literary text can be interpreted', 'Ecocriticism is a lens that can only be applied to texts written before any environmental concern existed', 'Literature has never engaged with questions of nature or the environment in any way'], 0)]),
AF('Discrete Math: Halls Marriage Theorem and Bipartite Matching',
   'Grade 12 Advanced Functions strand: Halls marriage theorem gives a precise condition, that every subset of one side of a bipartite graph has enough neighbours on the other side, under which a perfect matching pairing every vertex on one side with a distinct vertex on the other must exist.',
   [('What kind of graph does Halls marriage theorem concern?', ['A bipartite graph, with vertices divided into two distinct sides', 'A graph with no division into separate sides of any kind', 'A graph containing exactly one vertex in total', 'A graph with no edges connecting any vertices'], 0),
    ('What condition does Halls marriage theorem require of every subset of one side of the graph?', ['That the subset has enough neighbours on the other side', 'That the subset contains no vertices at all', 'That the subset is connected to every vertex in the entire graph', 'That the subset has strictly fewer neighbours than its own size'], 0),
    ('What does Halls marriage theorem guarantee when this condition is satisfied?', ['A perfect matching, pairing every vertex on one side with a distinct vertex on the other', 'That the graph contains no edges whatsoever', 'That every vertex on one side is paired with the same single vertex', 'That the graph cannot be described as bipartite'], 0),
    ('How does Halls marriage theorem relate to the stable marriage problem and the Gale-Shapley algorithm, studied in an earlier batch?', ['Both concern pairing elements from two groups, though Halls theorem states a condition guaranteeing a perfect matching exists, while the Gale-Shapley algorithm constructs a matching that is additionally stable with respect to preferences', 'The two results describe exactly the same theorem with no distinction', 'The Gale-Shapley algorithm proves Halls theorem is always false', 'Halls marriage theorem has no connection to matching problems of any kind'], 0),
    ('Why is Halls marriage theorem a useful result beyond its original matchmaking framing?', ['Its condition for a perfect matching applies broadly to resource allocation and assignment problems modelled as bipartite graphs', 'It has no application to any problem beyond pairing romantic partners', 'The theorem guarantees a perfect matching exists in every possible graph with no condition required', 'Bipartite graphs can never be used to model any real assignment problem'], 0)]),
CA('Numerical Methods: Newton-Cotes Quadrature and the Family of Integration Rules',
   'Grade 12 Calculus strand: Newton-Cotes quadrature is a general framework for numerical integration that approximates a definite integral by fitting a polynomial through equally spaced sample points, with familiar rules such as the trapezoid and Simpsons rule arising as specific low-order cases within this same framework.',
   [('What does Newton-Cotes quadrature use to approximate a definite integral?', ['A polynomial fitted through equally spaced sample points', 'A single randomly chosen sample point with no polynomial fitting', 'An exact algebraic antiderivative with no approximation involved', 'A polynomial fitted through points that are never equally spaced'], 0),
    ('What is the relationship between the Newton-Cotes framework and rules such as the trapezoid rule?', ['Familiar rules such as the trapezoid and Simpsons rule arise as specific low-order cases within the same Newton-Cotes framework', 'The trapezoid rule has no connection to the Newton-Cotes framework at all', 'Newton-Cotes quadrature and the trapezoid rule are unrelated methods developed independently with no shared structure', 'Simpsons rule uses unequally spaced points, unlike every Newton-Cotes formula'], 0),
    ('What determines the specific Newton-Cotes rule being used, such as whether it corresponds to the trapezoid or Simpsons rule?', ['The degree of the polynomial fitted through the sample points', 'The colour of the graph being integrated', 'The number of times the interval is renamed', 'A choice that has no effect on the resulting numerical rule'], 0),
    ('How does viewing Newton-Cotes quadrature as a unifying framework relate to the trapezoid rule and Simpsons rule studied in earlier batches?', ['It reframes those previously separate rules as specific instances of one general polynomial-fitting principle applied at different polynomial degrees', 'It shows that the trapezoid rule and Simpsons rule are entirely unrelated numerical techniques', 'The framework proves that neither the trapezoid rule nor Simpsons rule can ever approximate a definite integral', 'Newton-Cotes quadrature was developed with no reference to any previously known integration rule'], 0),
    ('Why is it valuable to understand Newton-Cotes quadrature as a general framework rather than only memorizing individual rules?', ['It reveals the shared principle behind several numerical integration methods and clarifies how increasing polynomial degree can improve approximation accuracy', 'Understanding the general framework provides no benefit over memorizing each rule in isolation', 'The general framework applies only to a single specific rule with no broader relevance', 'Numerical integration rules have no relationship to the degree of any polynomial'], 0)]),
PH('Quantum Decoherence and the Quantum-to-Classical Transition',
   'Grade 12 Physics strand: quantum decoherence describes how the fragile superposition of states in a quantum system becomes effectively lost through unavoidable interaction with its surrounding environment, offering a physical explanation for why everyday macroscopic objects do not display obvious quantum behaviour.',
   [('What does quantum decoherence describe happening to the superposition of states in a quantum system?', ['It becomes effectively lost through unavoidable interaction with the surrounding environment', 'It becomes permanently stronger the longer the system is left undisturbed', 'It has no relationship to any interaction with the surrounding environment', 'It instantly disappears the moment a quantum system is first created'], 0),
    ('What is responsible for causing decoherence in a quantum system?', ['Unavoidable interaction between the system and its surrounding environment', 'A deliberate measurement performed only once, with no further interaction', 'A process that requires no interaction of any kind with anything external', 'The system being placed in a perfectly isolated vacuum with no environment present'], 0),
    ('What everyday observation does quantum decoherence help explain?', ['Why everyday macroscopic objects do not display obvious quantum behaviour', 'Why every macroscopic object displays constant, obvious quantum superposition', 'Why quantum mechanics applies only to objects larger than a planet', 'Why classical physics has no relationship to quantum mechanics at all'], 0),
    ('How does quantum decoherence relate to quantum entanglement studied in an earlier batch?', ['Both concern how quantum correlations between a system and its surroundings evolve, though entanglement describes correlated states while decoherence describes how environmental interaction destroys observable superposition', 'The two concepts describe exactly the same physical process with no distinction', 'Quantum entanglement is caused entirely by decoherence with no other mechanism involved', 'Decoherence has no relationship to any interaction between quantum systems'], 0),
    ('Why is quantum decoherence considered important for understanding the boundary between quantum and classical physics?', ['It offers a physical mechanism explaining why quantum effects, though fundamental, are not directly observed in large everyday objects', 'It shows that quantum mechanics has no relevance to any physical system, large or small', 'Decoherence proves that classical physics is entirely incorrect at every scale', 'It has no bearing on why macroscopic objects behave classically'], 0)]),
]),
day(185, [
E('Media Analysis: Radio Drama and Storytelling for the Ear',
  'Grade 12 English strand: radio drama tells a complete story using only sound, dialogue, music, and sound effects, relying on a listeners imagination to construct setting and action that a visual medium would otherwise show directly, and flourished as a dominant storytelling form in the early decades of broadcasting.',
  [('What elements does radio drama rely on to tell a complete story?', ['Only sound, dialogue, music, and sound effects', 'Visual sets, costumes, and lighting with no sound at all', 'Printed text with no audio component whatsoever', 'Silent physical gesture with no sound of any kind'], 0),
   ('What must a radio drama listener do that a viewer of a visual medium does not need to do to the same extent?', ['Use their imagination to construct setting and action from sound alone', 'Read subtitles printed on a physical page', 'Watch a fully rendered visual set with no sound at all', 'Ignore the dialogue entirely while watching only visual cues'], 0),
   ('During which period did radio drama flourish as a dominant storytelling form?', ['The early decades of broadcasting', 'A period entirely after television had already replaced radio', 'A period before any form of sound recording existed', 'A period with no organized broadcasting of any kind'], 0),
   ('How does radio drama compare to the podcast and serial audio storytelling studied in an earlier batch?', ['Both are audio-only storytelling forms relying on sound rather than image, though radio drama flourished within scheduled broadcast programming while the podcast emerged later as an on-demand digital form', 'The two forms are identical in their era, distribution method, and technology', 'Podcasts rely primarily on visual images with almost no spoken audio', 'Radio drama and the podcast have no shared reliance on sound as a storytelling medium'], 0),
   ('Why might the absence of a visual component be considered a creative strength of radio drama rather than only a limitation?', ['It invites a listener to actively imagine setting and character, often producing a more personal and vivid mental picture than a fixed visual image would', 'A story told only through sound can never engage an audiences imagination', 'Radio drama is incapable of creating any sense of setting or atmosphere', 'The absence of images makes radio drama identical in every respect to a purely printed story'], 0)]),
AF('Number Theory: Primitive Roots and the Multiplicative Order Modulo n',
   'Grade 12 Advanced Functions strand: the multiplicative order of an integer modulo n is the smallest positive power to which it must be raised to return to one, and a primitive root modulo n is an integer whose powers generate every nonzero residue modulo n, meaning its order equals the size of the multiplicative group itself.',
   [('What does the multiplicative order of an integer modulo n measure?', ['The smallest positive power to which it must be raised to return to one', 'The largest power to which it can ever be raised', 'The total number of integers smaller than n', 'A quantity with no connection to powers of the integer at all'], 0),
    ('What defines a primitive root modulo n?', ['Its powers generate every nonzero residue modulo n', 'It is always equal to n itself', 'Its powers generate only the number one, with no other residue', 'It is defined only for even values of n'], 0),
    ('How does the order of a primitive root modulo n compare to the size of the multiplicative group modulo n?', ['The order of a primitive root equals the size of the multiplicative group itself', 'The order of a primitive root is always exactly one, regardless of n', 'The order of a primitive root always exceeds the size of the multiplicative group', 'A primitive roots order has no defined relationship to the group size'], 0),
    ('How does the concept of a primitive root relate to Eulers totient function studied in an earlier batch?', ['The totient function counts the size of the multiplicative group modulo n, which equals the order of any primitive root modulo n when one exists', 'The totient function and primitive roots describe entirely unrelated ideas in number theory', 'A primitive root always has an order strictly greater than the value given by the totient function', 'Eulers totient function can only be computed once a primitive root has first been found'], 0),
    ('Why are primitive roots a useful concept beyond pure number theory?', ['Their generating property underlies practical applications such as constructing certain cryptographic and pseudorandom number systems', 'Primitive roots have no application whatsoever outside of abstract number theory', 'They are used exclusively to prove that no integer can ever be a perfect square', 'Primitive roots exist for every possible value of n with no exception'], 0)]),
CA('Multivariable Calculus: Surface Area of a Parametric Surface',
   'Grade 12 Calculus strand: the surface area of a parametric surface is found by integrating the magnitude of the cross product of its two partial derivative vectors over the parameter domain, a formula that extends the familiar idea of arc length to a two-dimensional surface embedded in three-dimensional space.',
   [('What two vectors are combined, using a cross product, to compute the surface area of a parametric surface?', ['The two partial derivative vectors of the parametrization', 'Two vectors that are entirely unrelated to the surfaces parametrization', 'A single vector multiplied by itself, with no second vector involved', 'The gradient vector and a vector with a magnitude of zero'], 0),
    ('What operation is performed on the magnitude of this cross product to find the total surface area?', ['Integrating it over the parameter domain', 'Differentiating it with respect to a third, unrelated variable', 'Setting it equal to zero and solving for a constant', 'Multiplying it by the number of parameters used in the surface'], 0),
    ('In what kind of space is a parametric surface, as described here, typically embedded?', ['Three-dimensional space', 'A space with no dimensions at all', 'A purely one-dimensional line', 'A space defined using only a single parameter'], 0),
    ('How does this surface area formula relate to the arc length of a parametric curve, studied in an earlier batch?', ['Both extend an integral-based length or area computation from a parametrization, with arc length integrating the magnitude of a single derivative vector along a curve, while surface area integrates the magnitude of a cross product of two derivative vectors across a surface', 'The two formulas are computed using exactly the same integral with no distinction', 'Arc length applies only to three-dimensional surfaces and never to a one-dimensional curve', 'Surface area of a parametric surface requires no derivative of any kind'], 0),
    ('Why is the cross product a natural tool for measuring the area swept out by two partial derivative vectors on a surface?', ['The magnitude of the cross product of two vectors gives the area of the parallelogram they span, providing a local measure of area that can be integrated across the whole surface', 'The cross product has no connection to measuring area in any geometric context', 'Cross products can only be computed for vectors that point in the exact same direction', 'The magnitude of a cross product is always equal to zero for any two distinct vectors'], 0)]),
PH('Hubbles Law and the Expansion of the Universe',
   'Grade 12 Physics strand: Hubbles law states that a distant galaxys recession speed, inferred from the redshift of its light, is proportional to its distance from an observer, providing key observational evidence that the universe is expanding uniformly in every direction.',
   [('What quantity does Hubbles law relate to a distant galaxys distance from an observer?', ['Its recession speed, inferred from the redshift of its light', 'Its exact chemical composition', 'Its total mass compared to the observers galaxy', 'Its surface temperature measured directly'], 0),
    ('What proportional relationship does Hubbles law describe?', ['Recession speed is proportional to distance from the observer', 'Recession speed is always exactly the same for every galaxy regardless of distance', 'Recession speed decreases as distance increases, in every case', 'Distance has no measurable relationship to recession speed'], 0),
    ('What broader conclusion about the universe does Hubbles law provide key observational evidence for?', ['That the universe is expanding uniformly in every direction', 'That the universe is perfectly static and unchanging in size', 'That the universe is shrinking uniformly in every direction', 'That only a single galaxy is moving, with all others stationary'], 0),
    ('How does Hubbles law relate to the cosmic microwave background and the Big Bang, studied in an earlier batch?', ['Both provide independent observational support for an expanding universe with a hot, dense early state, with Hubbles law tracking present-day expansion through galaxy redshifts', 'The two lines of evidence contradict one another about whether the universe is expanding', 'The cosmic microwave background was discovered as a direct consequence of measuring Hubbles law', 'Hubbles law has no connection to any evidence for the Big Bang'], 0),
    ('Why is Hubbles law considered a foundational result in modern cosmology?', ['It gave the first strong observational evidence that the universe is expanding, reshaping the scientific understanding of the universes history and scale', 'It has had no lasting influence on the scientific understanding of the universe', 'Hubbles law proves that galaxies do not actually move relative to one another', 'The law applies only to galaxies within our own galactic cluster and no others'], 0)]),
]),
day(186, [
E('Media Analysis: The Video Essay -- Argument in Audiovisual Form',
  'Grade 12 English strand: a video essay presents a sustained, structured argument or analysis using a combination of narration, edited footage, on-screen text, and sound, adapting the persuasive and analytical structure of a written essay to an audiovisual medium built for online distribution.',
  [('What combination of elements does a video essay typically use to build its argument?', ['Narration, edited footage, on-screen text, and sound', 'Only silent still images with no narration, sound, or text of any kind', 'A single unedited video clip with no narration or additional editing', 'Printed text alone with no video or audio component'], 0),
   ('What written form does the video essay adapt its persuasive and analytical structure from?', ['The written essay', 'A recipe with no persuasive or analytical structure', 'A weather report with no argumentative content', 'A private, unpublished diary entry'], 0),
   ('For what kind of distribution is the video essay typically built?', ['Online distribution', 'Distribution exclusively through printed newspapers', 'Distribution limited to a single in-person live performance with no recording', 'A medium with no possibility of being shared or viewed by an audience'], 0),
   ('How does the video essay compare to the podcast and serial audio storytelling studied in an earlier batch?', ['Both are relatively recent media forms built for online distribution that adapt older narrative or essayistic structures, though the video essay is built around edited visual footage while the podcast relies on audio alone', 'The two forms are identical in every respect, including their reliance on visual footage', 'The podcast is built primarily around edited video footage with almost no spoken audio', 'The video essay has no relationship to any earlier form of essay writing'], 0),
   ('Why might the video essay be considered an effective form for contemporary media analysis and criticism?', ['Combining spoken argument with directly shown audiovisual evidence lets a creator illustrate and support a claim in ways a purely written essay cannot', 'A video essay is incapable of making any kind of sustained argument', 'The form has no advantage over a purely written essay for analyzing audiovisual media', 'Video essays never include narration, relying only on unexplained footage'], 0)]),
AF('Functions: The Dirichlet Function and the Limits of Continuity',
   'Grade 12 Advanced Functions strand: the Dirichlet function assigns one value to every rational number and a different value to every irrational number, producing a function that is discontinuous at every single point, a striking example used to probe the boundary between continuity and discontinuity in real analysis.',
   [('What rule defines the Dirichlet function?', ['It assigns one value to every rational number and a different value to every irrational number', 'It assigns the same single value to every real number without exception', 'It is defined only for negative numbers, with no output for positive numbers', 'It assigns a different value to every individual rational number separately'], 0),
    ('At how many points is the Dirichlet function continuous?', ['It is discontinuous at every single point', 'It is continuous at every single point', 'It is continuous only at the number zero', 'It is continuous everywhere except at exactly one point'], 0),
    ('What broader mathematical purpose does the Dirichlet function serve?', ['It provides a striking example used to probe the boundary between continuity and discontinuity in real analysis', 'It is used exclusively for basic arithmetic calculations with no theoretical purpose', 'It has no role in illustrating any property of functions', 'It is used only to compute the area under a simple polynomial curve'], 0),
    ('How does the Dirichlet function compare to the Weierstrass function studied in an earlier batch?', ['Both are notable pathological examples in real analysis, though the Weierstrass function is continuous everywhere but differentiable nowhere, while the Dirichlet function is discontinuous at every point', 'The two functions behave in exactly the same way at every point', 'The Weierstrass function is discontinuous everywhere, just like the Dirichlet function', 'Neither function has any relevance to the study of continuity or differentiability'], 0),
    ('Why is a function like the Dirichlet function valuable for students of real analysis, despite having no simple graph that can be sketched by hand?', ['It sharpens understanding of the precise definitions of continuity and limit by presenting a case where ordinary graphical intuition fails completely', 'Such a function has no value for developing a rigorous understanding of continuity', 'The Dirichlet function can be sketched easily using only a ruler and no other tool', 'It shows that every function encountered in mathematics must be continuous everywhere'], 0)]),
CA('Series: The Cauchy Condensation Test for Series Convergence',
   'Grade 12 Calculus strand: the Cauchy condensation test determines the convergence of a series with positive, non-increasing terms by comparing it to a related, sparser condensed series built from terms at doubling indices, often turning a difficult series into one that is straightforward to analyze.',
   [('What kind of series does the Cauchy condensation test apply to?', ['A series with positive, non-increasing terms', 'A series whose terms are always increasing without bound', 'A series containing exactly one term in total', 'A series with terms that alternate strictly between positive and negative values'], 0),
    ('What does the Cauchy condensation test compare the original series to?', ['A related, sparser condensed series built from terms at doubling indices', 'An entirely unrelated series with no connection to the original terms', 'A series consisting only of the number zero repeated indefinitely', 'The original series compared only to itself with no transformation'], 0),
    ('What practical benefit does forming the condensed series often provide?', ['It can turn a difficult series into one that is straightforward to analyze', 'It always makes a convergent series diverge instead', 'It removes the need to consider convergence at all', 'It guarantees that the original series has no defined terms remaining'], 0),
    ('How does the Cauchy condensation test relate to the comparison test and integral test studied in earlier batches?', ['All three establish convergence by relating a series to another, better-understood series or function, though the condensation test specifically exploits a non-increasing terms doubling-index structure', 'The three tests are completely unrelated in their underlying strategy', 'The integral test requires forming a condensed series identical to the one used in the condensation test', 'The comparison test can only be applied to a series with negative terms'], 0),
    ('Why is the Cauchy condensation test a useful addition to the toolkit of series convergence tests?', ['It can efficiently resolve the convergence of certain series, such as those involving logarithms, where other standard tests are awkward to apply directly', 'It is incapable of determining the convergence of any series whatsoever', 'The test can only be applied to series that are already known to diverge', 'It duplicates exactly the same information as every other convergence test with no distinct advantage'], 0)]),
PH('Crystal Structures and Unit Cells in Solids',
   'Grade 12 Physics strand: a crystal structure describes the regular, repeating three-dimensional arrangement of atoms in a solid, characterized by a unit cell, the smallest repeating block whose geometry and packing determine many of the materials mechanical, thermal, and electronic properties.',
   [('What does a crystal structure describe about the atoms in a solid?', ['Their regular, repeating three-dimensional arrangement', 'A completely random and disordered arrangement with no repeating pattern', 'An arrangement found only in liquids and never in solids', 'An arrangement that changes unpredictably from moment to moment'], 0),
    ('What is a unit cell, in the context of crystal structure?', ['The smallest repeating block whose geometry defines the overall crystal structure', 'The single largest possible piece of the entire solid', 'A region of the solid containing no atoms at all', 'A block that never repeats anywhere else in the solid'], 0),
    ('What kinds of material properties can be influenced by the geometry and packing of a unit cell?', ['Mechanical, thermal, and electronic properties', 'Only the materials colour, with no other property affected', 'Properties that have no connection to the arrangement of atoms', 'Only the materials smell, with no other measurable property affected'], 0),
    ('How does the concept of crystal structure relate to band theory of solids, studied in an earlier batch?', ['The regular, repeating atomic arrangement described by crystal structure is the underlying geometric basis that gives rise to the electron energy bands described by band theory', 'Crystal structure and band theory describe entirely unrelated aspects of a solid', 'Band theory applies only to materials with no repeating atomic arrangement', 'A materials unit cell has no influence on its electronic energy band structure'], 0),
    ('Why is understanding a materials crystal structure important for explaining its physical behaviour?', ['The geometric arrangement of atoms in a crystal directly shapes how a material conducts heat and electricity, how strong it is, and how it responds to stress', 'Crystal structure has no bearing on any measurable physical property of a material', 'Every solid material has an identical crystal structure with no variation', 'Physical behaviour of a solid depends entirely on its colour and never on atomic arrangement'], 0)]),
]),
day(187, [
E('English Review: A Capstone Survey of Drama, Satire, Genre, and Media',
  'Grade 12 English review: revisiting the masque, Horatian and Juvenalian satire, cyberpunk, ecocriticism, and radio drama from Days 181-185 -- the final English review of the complete 187-day Grade 12 curriculum.',
  [('What combination of elements does a masque typically bring together?', ['Dance, music, elaborate costume and stage machinery, and allegorical poetry', 'Only spoken dialogue with no music, dance, or costume of any kind', 'A single unaccompanied song with no other performance element', 'Silent physical movement with no poetry, music, or spectacle'], 0),
   ('What tone characterizes Horatian satire?', ['A light, witty, good-humoured tone that gently mocks human folly', 'A harsh, bitter tone aimed at severe moral condemnation', 'A tone entirely devoid of any humour or wit', 'A tone that avoids commenting on human behaviour altogether'], 0),
   ('What two elements does cyberpunk combine as central features of its setting?', ['Advanced computer and biotechnology with a gritty, high-tech-low-life urban setting', 'Medieval technology with a rural agricultural setting', 'An absence of any technology with a peaceful pastoral setting', 'Ancient mythology with no reference to technology of any kind'], 0),
   ('What does ecocriticism primarily examine in a literary text?', ['How the text represents the natural world and the relationship between humans and their environment', 'Only the texts publication date, with no reference to its content', 'The economic sales figures of the text with no reference to its themes', 'The biography of the author with no reference to environmental themes'], 0),
   ('What elements does radio drama rely on to tell a complete story?', ['Only sound, dialogue, music, and sound effects', 'Visual sets, costumes, and lighting with no sound at all', 'Printed text with no audio component whatsoever', 'Silent physical gesture with no sound of any kind'], 0)]),
AF('AdvancedFunctions Review: The Capstone Survey of Statistics, Discrete Math, and Number Theory',
   'Grade 12 Advanced Functions review: revisiting the bootstrap method, the Kolmogorov-Smirnov test, Kuratowskis theorem, Halls marriage theorem, and primitive roots from Days 181-185 -- the final Advanced Functions review of the complete 187-day Grade 12 curriculum.',
   [('What does the bootstrap method use to estimate the sampling distribution of a statistic?', ['Repeated resampling, with replacement, from an observed data set', 'A single fixed theoretical formula with no resampling involved', 'Resampling without replacement performed exactly once', 'An entirely new, independent experiment collected each time'], 0),
    ('What quantity does the Kolmogorov-Smirnov test measure to compare two distributions?', ['The largest gap between their cumulative distribution functions', 'The average of every individual data point in both sets', 'The total number of data points collected in each set', 'The colour or category label assigned to each observation'], 0),
    ('What does it mean for a graph to be planar?', ['It can be drawn in the plane with no edges crossing', 'It must contain at least one pair of crossing edges', 'It has no vertices or edges of any kind', 'It can only be drawn using exactly two dimensions of colour'], 0),
    ('What kind of graph does Halls marriage theorem concern?', ['A bipartite graph, with vertices divided into two distinct sides', 'A graph with no division into separate sides of any kind', 'A graph containing exactly one vertex in total', 'A graph with no edges connecting any vertices'], 0),
    ('What does the multiplicative order of an integer modulo n measure?', ['The smallest positive power to which it must be raised to return to one', 'The largest power to which it can ever be raised', 'The total number of integers smaller than n', 'A quantity with no connection to powers of the integer at all'], 0)]),
CA('Calculus Review: The Capstone Survey of Differential Equations and Numerical Methods',
   'Grade 12 Calculus review: revisiting the Riccati equation, reduction of order, Picard iteration, Newton-Cotes quadrature, and surface area of a parametric surface from Days 181-185 -- the final Calculus review of the complete 187-day Grade 12 curriculum.',
   [('What distinctive term appears in a Riccati equation that is not present in a standard linear first-order equation?', ['A quadratic term in the unknown function', 'A term involving no function of any kind', 'A term that is always identically zero', 'A term involving only the independent variable raised to the first power'], 0),
    ('What does reduction of order require to already be known before it can be applied?', ['One solution to the second-order linear differential equation', 'Both solutions to the differential equation', 'The exact numerical value of every constant in the equation', 'No information about the differential equation at all'], 0),
    ('What does Picard iteration convert a differential equation into before beginning its approximation process?', ['An equivalent integral equation', 'A purely algebraic equation with no integral or derivative present', 'A system of unrelated equations with no connection to the original problem', 'A differential equation of a strictly higher order'], 0),
    ('What does Newton-Cotes quadrature use to approximate a definite integral?', ['A polynomial fitted through equally spaced sample points', 'A single randomly chosen sample point with no polynomial fitting', 'An exact algebraic antiderivative with no approximation involved', 'A polynomial fitted through points that are never equally spaced'], 0),
    ('What two vectors are combined, using a cross product, to compute the surface area of a parametric surface?', ['The two partial derivative vectors of the parametrization', 'Two vectors that are entirely unrelated to the surfaces parametrization', 'A single vector multiplied by itself, with no second vector involved', 'The gradient vector and a vector with a magnitude of zero'], 0)]),
PH('Physics Review: The Capstone Survey of Orbits, Fields, Optics, and the Cosmos',
   'Grade 12 Physics review: revisiting Keplers laws, Gauss law, Youngs double-slit experiment, quantum decoherence, and Hubbles law from Days 181-185 -- the final Physics review of the complete 187-day Grade 12 curriculum, and the very last lesson of the full K-12 curriculum build for this grade.',
   [('According to Keplers first law, what shape does a planets orbit take, and where is the Sun located?', ['An ellipse, with the Sun at one focus', 'A perfect circle, with the Sun at its exact centre', 'A straight line passing directly through the Sun', 'A shape with no defined geometric form at all'], 0),
    ('What does Gauss law relate the total electric flux through a closed surface to?', ['The net electric charge enclosed within that surface', 'The colour and material of the surface itself', 'The total surface area of the enclosing shape alone', 'The distance of the surface from the nearest magnet'], 0),
    ('What experimental setup does Youngs double-slit experiment use?', ['Light passed through two closely spaced narrow slits', 'A single wide opening with no second slit present', 'A solid opaque barrier with no opening of any kind', 'Light reflected from a single flat mirror with no slits involved'], 0),
    ('What does quantum decoherence describe happening to the superposition of states in a quantum system?', ['It becomes effectively lost through unavoidable interaction with the surrounding environment', 'It becomes permanently stronger the longer the system is left undisturbed', 'It has no relationship to any interaction with the surrounding environment', 'It instantly disappears the moment a quantum system is first created'], 0),
    ('What quantity does Hubbles law relate to a distant galaxys distance from an observer?', ['Its recession speed, inferred from the redshift of its light', 'Its exact chemical composition', 'Its total mass compared to the observers galaxy', 'Its surface temperature measured directly'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g12_181_187)
    append_to(12, g12_181_187)
