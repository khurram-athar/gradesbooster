#!/usr/bin/env python3
"""Grade 11, Days 91-100 -- extends Grade 11 from 90 to 100 days. Topics
chosen to avoid any overlap with the existing Day 1-90 set (see
data/grade11.json): the postcolonial novel, the personal diary and journal
as literary form, the sonnet (Petrarchan and Shakespearean), rhetorical
schemes (anaphora, chiasmus, parallelism), the parable and fable, the
public service announcement and advocacy writing, feminist literary
criticism, spoken word and performance poetry, and allusion and
intertextuality; operations on functions (sum/difference/product/
quotient), synthetic division and the remainder theorem, sum and
difference trigonometric identities, matrix determinants and the inverse
of a 2x2 matrix, the law of large numbers and simulation, laws of
exponents and rational exponents, linear programming with systems of
inequalities, finite differences for polynomial functions, and prime
factorization/the fundamental theorem of arithmetic; thermoregulation in
endotherms and ectotherms, the operon model and prokaryotic gene
regulation, chemical/structural plant defences against herbivory,
exponential and logistic population growth models, bioaccumulation and
biomagnification, convergent and divergent evolution, linked genes and
genetic recombination, lytic and lysogenic viral replication cycles, and
the special senses of hearing and balance; electron configuration and
orbital diagrams, the chemistry of sunscreen and UV photoprotection,
semiconductors and doping, chirality and optical isomers, carbon
allotropes (graphite, diamond, graphene), acid-base indicators and colour
change theory, metallurgy and ore extraction, the Haber-Bosch process, and
agricultural chemistry (fertilizers and soil nutrients).

Topics were checked closely against near-neighbours already on the books
to avoid overlap: "Thermoregulation in Endotherms and Ectotherms" is a
distinct physiological topic from Day 34's excretory system/homeostasis;
"The Operon Model and Prokaryotic Gene Regulation" narrows in on a
specific mechanism distinct from Day 36's general gene expression and
regulation and Day 84's epigenetics; "Population Growth Models" is
distinct from Day 9's general population dynamics and community ecology,
focusing specifically on the exponential/logistic mathematical models;
"Linked Genes and Genetic Recombination" is distinct from Day 61's
sex-linked inheritance and Day 42's polygenic inheritance; "Viral
Replication Cycles" is distinct from Day 31's general microbiology and Day
56's antibiotic resistance; "Matrices: Determinants and the Inverse"
extends Day 72's introduction to matrices the way Day 71's ellipses and
hyperbolas extended Day 69's circles; "Synthetic Division and the
Remainder Theorem" is a distinct algebraic technique from Day 3's general
polynomial factoring and solving; "Metallurgy" and "The Haber-Bosch
Process" are distinct industrial applications from Day 82's industrial
catalysis and Day 9's/Day 43's general chemical equilibrium.

Subject keys for Grade 11 are "English", "Functions", "Biology",
"Chemistry" (same as all earlier Grade 11 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

E11 = 'https://tvolearn.com/pages/grade-11-english'
F11 = 'https://tvolearn.com/pages/grade-11-functions'
B11 = 'https://tvolearn.com/pages/grade-11-biology'
C11 = 'https://tvolearn.com/pages/grade-11-chemistry'
RE, RF, RB, RC = (
    'TVO Learn: Grade 11 English',
    'TVO Learn: Grade 11 Functions',
    'TVO Learn: Grade 11 Biology',
    'TVO Learn: Grade 11 Chemistry',
)


def E(t, s, q):
    return sub('English', t, s, RE, E11, q)


def F(t, s, q):
    return sub('Functions', t, s, RF, F11, q)


def B(t, s, q):
    return sub('Biology', t, s, RB, B11, q)


def C(t, s, q):
    return sub('Chemistry', t, s, RC, C11, q)


def _rebalance_answer_positions(days, seed=20260930):
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


g11_91_100 = [
day(91, [
E('Literature: The Postcolonial Novel and Writing Back to Empire',
  'Grade 11 English strand: postcolonial literature examines the lasting cultural, political, and psychological effects of colonialism, often reclaiming narrative voice from the perspective of formerly colonized peoples.',
  [('What does postcolonial literature often examine?', ['The lasting cultural, political, and psychological effects of colonialism', 'Only the geography of a fictional setting', 'A concept unrelated to literature', 'The exact publication date of a novel'], 0),
   ('Does postcolonial literature often reclaim narrative voice from the perspective of formerly colonized peoples?', ['Yes', 'No, postcolonial literature never considers whose perspective is centred', 'A concept unrelated to postcolonial literature', 'Colonialism has no connection to this genre of literature'], 0),
   ('Why might a postcolonial author retell a well-known story from the perspective of a colonized character rather than the colonizer?', ['To challenge a dominant narrative and offer a perspective that had previously been silenced or marginalized', 'Retelling a story from a different perspective never changes its meaning', 'This concept has no connection to literature', 'Postcolonial authors never revisit existing stories or narratives'], 0),
   ('Which of these would most likely appear in a postcolonial novel?', ['A character grappling with how colonial rule reshaped her homeland’s language, land, and identity.', 'A detailed recipe for baking bread.', 'A weather report for the upcoming week.', 'A user manual for assembling furniture.'], 0),
   ('Why is postcolonial literature considered valuable for understanding global history?', ['It offers perspectives often excluded from traditional historical accounts, deepening understanding of colonialism’s lasting impact', 'Postcolonial literature has no connection to understanding history', 'This concept has no relevance to literature', 'Colonialism has never had any lasting cultural or political effects'], 0)]),
F('Functions: Operations on Functions — Sum, Difference, Product, and Quotient',
  'Grade 11 Functions strand: functions can be combined using the operations of addition, subtraction, multiplication, and division to create new functions, with the domain of the result restricted by any original domain restrictions.',
  [('Which operations can be used to combine two functions into a new function?', ['Addition, subtraction, multiplication, and division', 'Only addition, with no other operation permitted', 'A concept unrelated to functions', 'None, since functions can never be combined'], 0),
   ('If f of x equals x plus 2, and g of x equals x minus 2, what is the sum function, f plus g, evaluated at x?', ['2x', '4', 'x squared minus 4', '0'], 0),
   ('If f of x equals 2x, and g of x equals x plus 3, what is the product function, f times g, evaluated at x?', ['2x squared plus 6x', '2x plus 3', 'x squared plus 3', '6x'], 0),
   ('Why must the domain of the quotient function, f divided by g, exclude values where g of x equals zero?', ['Division by zero is undefined, so those x-values cannot be part of the quotient function’s domain', 'The domain of a quotient function is never affected by the value of g of x', 'This concept has no connection to functions', 'Quotient functions are always defined for every possible value of x'], 0),
   ('Why might combining two functions through addition be useful when modelling total revenue as the sum of two income sources?', ['Adding the two functions produces a single function representing the combined total at every value of x', 'Adding two functions together never produces a meaningful new function', 'This concept has no relevance to functions', 'Revenue from two different sources can never be modelled using functions'], 0)]),
B('Biology: Thermoregulation in Endotherms and Ectotherms',
  'Grade 11 Biology strand: endotherms generate their own body heat internally to maintain a stable body temperature, while ectotherms rely primarily on external environmental sources to regulate their body temperature.',
  [('What do endotherms use to maintain a stable body temperature?', ['Heat generated internally by their own metabolism', 'Only heat absorbed from the surrounding environment', 'A concept unrelated to biology', 'Nothing at all related to temperature regulation'], 0),
   ('Do ectotherms rely primarily on external sources of heat to regulate their body temperature?', ['Yes', 'No, ectotherms always generate all of their own body heat internally', 'A concept unrelated to thermoregulation', 'Body temperature regulation is never relevant to ectotherms'], 0),
   ('Why might a reptile bask in the sun during cool mornings before becoming active?', ['As an ectotherm, it needs external heat to raise its body temperature enough for its muscles and metabolism to function efficiently', 'Reptiles never need any external heat source to become active', 'This concept has no connection to biology', 'Basking in the sun has no effect on a reptile’s body temperature'], 0),
   ('Which of these animals would most likely be classified as an endotherm?', ['A mammal that generates heat internally to stay warm even in cold winter temperatures.', 'A lizard that must move to a sunny rock to warm up before moving.', 'A snake that becomes sluggish and inactive in cold weather.', 'A frog whose body temperature always matches its surroundings.'], 0),
   ('Why might endothermy allow an animal to remain active across a wider range of environmental temperatures than ectothermy?', ['Generating heat internally lets an endotherm maintain a stable body temperature regardless of surrounding conditions', 'Endothermy never provides any advantage over ectothermy in varying temperatures', 'This concept has no relevance to biology', 'Body temperature has no connection to how active an animal can be'], 0)]),
C('Chemistry: Atomic Structure — Electron Configuration and Orbital Diagrams',
  'Grade 11 Chemistry strand: electron configuration describes how electrons are arranged within an atom’s orbitals, following the aufbau principle, Hund’s rule, and the Pauli exclusion principle.',
  [('What does electron configuration describe?', ['How electrons are arranged within an atom’s orbitals', 'Only the mass of an atom’s nucleus', 'A concept unrelated to chemistry', 'The exact colour an element appears in solid form'], 0),
   ('Does the aufbau principle state that electrons fill the lowest-energy orbitals first?', ['Yes', 'No, the aufbau principle has no connection to how orbitals are filled', 'A concept unrelated to electron configuration', 'Electrons always fill the highest-energy orbitals first'], 0),
   ('According to the Pauli exclusion principle, can two electrons in the same orbital have identical sets of quantum numbers?', ['No', 'Yes, two electrons in the same orbital always share identical quantum numbers', 'A concept unrelated to the Pauli exclusion principle', 'Quantum numbers have no connection to electrons within an orbital'], 0),
   ('Why does Hund’s rule state that electrons fill separate orbitals within a subshell individually before pairing up?', ['Electrons repel each other, so occupying separate orbitals singly first minimizes repulsion and results in a lower-energy, more stable configuration', 'Electrons always pair up in the same orbital before filling any other orbital', 'This concept has no connection to chemistry', 'Hund’s rule has no relationship to how electrons are distributed among orbitals'], 0),
   ('Why is understanding electron configuration useful for predicting an element’s chemical behaviour?', ['The arrangement of valence electrons largely determines how an atom will bond and react with other atoms', 'Electron configuration has no connection to how an atom behaves chemically', 'This concept has no relevance to chemistry', 'An element’s chemical behaviour is never related to its electron arrangement'], 0)]),
]),

day(92, [
E('Writing: The Personal Diary and Journal as Literary Form',
  'Grade 11 English strand: the personal diary or journal is a literary form built on intimate, first-person reflection, often unfolding without a predetermined audience and capturing a writer’s immediate thoughts and reactions over time.',
  [('What does the personal diary or journal typically capture?', ['A writer’s immediate thoughts and reactions over time', 'Only a summary of unrelated news events', 'A concept unrelated to writing', 'A formal argument intended for publication'], 0),
   ('Is a diary usually written from a first-person perspective?', ['Yes', 'No, diaries are never written from a first-person perspective', 'A concept unrelated to diaries or journals', 'First-person perspective has no connection to this literary form'], 0),
   ('Why might a diary entry feel more raw or unfiltered than a polished personal essay?', ['A diary is often written without the expectation of a wide audience, allowing for more immediate, unedited reflection', 'Diary entries are always more polished and formal than personal essays', 'This concept has no connection to writing', 'A diary entry is never written with any personal reflection at all'], 0),
   ('Which of these best exemplifies a diary entry?', ['Today I could not stop thinking about the argument we had, and I still do not know what to say to her.', 'The chemical formula for methane is CH4.', 'Add 12 and 8 to get 20.', 'The train departs at exactly noon.'], 0),
   ('Why might historians value diaries written during significant historical events?', ['They can offer an intimate, first-hand perspective on how ordinary individuals experienced and reacted to those events', 'Diaries provide no useful information to historians studying past events', 'This concept has no relevance to writing', 'Historical events are never reflected in personal diaries or journals'], 0)]),
F('Algebra: Synthetic Division and the Remainder Theorem',
  'Grade 11 Functions strand: synthetic division offers a streamlined method for dividing a polynomial by a linear binomial, and the remainder theorem states that the remainder of this division equals the polynomial evaluated at the binomial’s root.',
  [('What does synthetic division streamline?', ['Dividing a polynomial by a linear binomial', 'Multiplying two large polynomials together', 'A concept unrelated to functions', 'Graphing a function on a coordinate plane'], 0),
   ('According to the remainder theorem, does the remainder of dividing a polynomial by (x minus a) equal the polynomial evaluated at x equals a?', ['Yes', 'No, the remainder theorem has no connection to evaluating a polynomial', 'A concept unrelated to synthetic division', 'The remainder is always zero regardless of the polynomial or divisor'], 0),
   ('If a polynomial P of x is divided by (x minus 2) and the remainder is 0, is (x minus 2) a factor of P of x?', ['Yes', 'No, a remainder of zero never indicates a factor of the polynomial', 'A concept unrelated to the remainder theorem', 'Factors of a polynomial are never related to division remainders'], 0),
   ('Why is synthetic division typically faster than long division when dividing a polynomial by a simple linear binomial?', ['It uses only the coefficients of the polynomial and a streamlined series of arithmetic steps rather than the full long-division process', 'Synthetic division is never faster than standard long division', 'This concept has no connection to functions', 'Synthetic division requires more steps than traditional long division'], 0),
   ('Why is the remainder theorem useful for testing whether a given value is a root of a polynomial without fully factoring it?', ['Evaluating the polynomial at that value instantly reveals whether the remainder is zero, indicating a root', 'The remainder theorem never helps identify whether a value is a root', 'This concept has no relevance to functions', 'Testing for a root always requires fully factoring the entire polynomial first'], 0)]),
B('Molecular Biology: The Operon Model and Prokaryotic Gene Regulation',
  'Grade 11 Biology strand: the operon model explains how prokaryotic cells switch groups of related genes on or off together in response to environmental conditions, using a shared promoter and operator to control transcription.',
  [('What does the operon model explain in prokaryotic cells?', ['How groups of related genes are switched on or off together', 'How a single unrelated protein is broken down', 'A concept unrelated to biology', 'How cells physically divide during mitosis'], 0),
   ('Does an operon typically include a shared promoter and operator controlling nearby genes?', ['Yes', 'No, an operon never involves any shared promoter or operator', 'A concept unrelated to the operon model', 'Promoters and operators have no connection to gene regulation'], 0),
   ('In the classic lac operon, does the presence of lactose typically switch on the genes needed to digest it?', ['Yes', 'No, lactose has no connection to activating the lac operon', 'A concept unrelated to prokaryotic gene regulation', 'The lac operon genes are always active regardless of lactose presence'], 0),
   ('Why is it efficient for a bacterium to regulate several related genes together as a single operon rather than individually?', ['Genes involved in the same metabolic pathway are needed at the same time, so controlling them together allows a faster, coordinated response', 'Regulating genes together as an operon never provides any efficiency benefit', 'This concept has no connection to biology', 'Bacteria never need to coordinate the expression of multiple genes at once'], 0),
   ('Why is the operon model considered a foundational concept in understanding prokaryotic gene regulation?', ['It reveals how bacteria efficiently respond to changing environmental conditions by coordinating gene expression', 'The operon model has no connection to how bacteria respond to their environment', 'This concept has no relevance to biology', 'Prokaryotic gene regulation never involves any environmental response'], 0)]),
C('Chemistry: Sunscreen and UV Photoprotection',
  'Grade 11 Chemistry strand: sunscreens rely on chemical compounds that either absorb ultraviolet radiation and release it as heat or physically reflect and scatter it away from the skin.',
  [('What do chemical sunscreen compounds primarily do with absorbed ultraviolet radiation?', ['Absorb it and release it as heat', 'Convert it directly into visible light', 'A concept unrelated to chemistry', 'Store it permanently within the skin'], 0),
   ('Do physical, or mineral, sunscreens work primarily by reflecting and scattering ultraviolet radiation?', ['Yes', 'No, physical sunscreens never reflect or scatter any radiation', 'A concept unrelated to sunscreen chemistry', 'Physical sunscreens work by absorbing radiation exclusively, never reflecting it'], 0),
   ('Can prolonged exposure to unprotected ultraviolet radiation damage skin cells?', ['Yes', 'No, ultraviolet radiation never causes any damage to skin cells', 'A concept unrelated to UV photoprotection', 'Skin cells are never affected by any type of radiation'], 0),
   ('Why might a sunscreen combine multiple active ingredients to protect against both UVA and UVB radiation?', ['Different compounds absorb or block different wavelength ranges, so combining them provides broader protection', 'Combining multiple ingredients in a sunscreen never improves its protective ability', 'This concept has no connection to chemistry', 'UVA and UVB radiation are always blocked equally well by any single ingredient'], 0),
   ('Why is the chemical stability of a sunscreen’s active ingredients important for its effectiveness over time?', ['An unstable compound could break down under sunlight exposure, reducing its ability to continue absorbing or blocking UV radiation', 'Chemical stability has no connection to how well a sunscreen continues to work', 'This concept has no relevance to chemistry', 'Sunscreen ingredients never break down or change under sunlight exposure'], 0)]),
]),

day(93, [
E('Poetry: The Sonnet Form — Petrarchan and Shakespearean',
  'Grade 11 English strand: the sonnet is a fourteen-line poem with a fixed rhyme scheme, traditionally following either the Petrarchan structure of an octave and sestet or the Shakespearean structure of three quatrains and a closing couplet.',
  [('How many lines does a traditional sonnet contain?', ['Fourteen', 'Ten', 'A concept unrelated to poetry', 'Twenty'], 0),
   ('Does the Shakespearean sonnet traditionally end with a closing couplet?', ['Yes', 'No, the Shakespearean sonnet never ends with a couplet', 'A concept unrelated to the sonnet form', 'A closing couplet has no connection to sonnet structure'], 0),
   ('Is the Petrarchan sonnet traditionally divided into an octave and a sestet?', ['Yes', 'No, the Petrarchan sonnet has no fixed structural divisions', 'A concept unrelated to Petrarchan sonnets', 'An octave and sestet only ever appear in Shakespearean sonnets'], 0),
   ('Why might a poet choose the Shakespearean sonnet form’s closing couplet to deliver a surprising twist or resolution?', ['The couplet’s compact, rhymed final statement can create a sharp shift in tone or meaning after the preceding quatrains', 'A closing couplet never creates any shift in tone or meaning', 'This concept has no connection to poetry', 'The closing couplet always simply repeats the sonnet’s opening line'], 0),
   ('Why has the sonnet remained a popular poetic form across centuries?', ['Its fixed structure offers a disciplined framework that many poets have adapted to explore a wide range of themes', 'The sonnet form has no connection to any themes explored by poets', 'This concept has no relevance to poetry', 'Poets have never adapted the sonnet form for any new purpose'], 0)]),
F('Trigonometry: Sum and Difference Identities',
  'Grade 11 Functions strand: sum and difference identities express the sine, cosine, or tangent of the sum or difference of two angles in terms of the trigonometric functions of each individual angle.',
  [('What do sum and difference identities express?', ['The sine, cosine, or tangent of the sum or difference of two angles, in terms of the individual angles', 'Only the value of a single, unrelated angle', 'A concept unrelated to trigonometry', 'The area of a triangle with two known angles'], 0),
   ('What is the sum identity for cosine of A plus B, in terms of the trigonometric functions of A and B individually?', ['cosine A cosine B minus sine A sine B', 'sine A cosine B plus cosine A sine B', 'cosine A plus cosine B', 'sine A sine B plus cosine A cosine B'], 0),
   ('Can sum and difference identities be used to find the exact value of sine of 75 degrees using sine and cosine of 45 and 30 degrees?', ['Yes', 'No, sum and difference identities can never be used to find exact trigonometric values', 'A concept unrelated to trigonometric identities', 'Exact trigonometric values can only ever be found using a calculator'], 0),
   ('Why are sum and difference identities useful for finding exact trigonometric values of angles that are not standard reference angles?', ['They allow such an angle to be rewritten as a sum or difference of two angles whose exact trigonometric values are already known', 'These identities never help in finding the exact value of any angle', 'This concept has no connection to trigonometry', 'Sum and difference identities only work for angles that are already standard reference angles'], 0),
   ('Why must a student keep careful track of positive and negative signs when applying the sum and difference identities?', ['A sign error would produce an entirely different value, since the identities involve both addition and subtraction of terms', 'Signs never affect the outcome when applying these trigonometric identities', 'This concept has no relevance to trigonometry', 'Sum and difference identities never involve any subtraction of terms'], 0)]),
B('Plant Biology: Chemical and Structural Defences Against Herbivory',
  'Grade 11 Biology strand: plants have evolved chemical defences, such as toxins and deterrent compounds, alongside structural defences, such as thorns and tough leaves, to reduce damage from herbivores.',
  [('What are two broad categories of plant defences against herbivory?', ['Chemical defences and structural defences', 'Only defences based on colour and scent', 'A concept unrelated to biology', 'Only defences involving rapid movement'], 0),
   ('Might a plant produce toxic compounds to deter herbivores from eating its leaves?', ['Yes', 'No, plants never produce any chemical compounds to deter herbivores', 'A concept unrelated to plant defences', 'Toxic compounds have no connection to plant herbivore defence'], 0),
   ('Are thorns considered a structural defence against herbivory?', ['Yes', 'No, thorns have no defensive function in plants', 'A concept unrelated to structural defences', 'Thorns are only ever used by plants to attract pollinators'], 0),
   ('Why might a plant evolve a bitter-tasting chemical compound in its leaves over many generations?', ['Herbivores that avoid bitter-tasting leaves would leave more of the plant intact, favouring the survival of plants producing that compound', 'Bitter-tasting compounds never provide any survival advantage to a plant', 'This concept has no connection to biology', 'Herbivores are never influenced by the taste of the plants they eat'], 0),
   ('Why might some herbivores evolve resistance to a plant’s chemical defences over time?', ['An evolutionary arms race can occur, where herbivores that tolerate a toxin gain access to a food source that competitors cannot use', 'Herbivores can never evolve any resistance to a plant’s chemical defences', 'This concept has no relevance to biology', 'Plant chemical defences never create any evolutionary pressure on herbivores'], 0)]),
C('Materials Chemistry: Semiconductors and Doping',
  'Grade 11 Chemistry strand: semiconductors are materials with electrical conductivity between that of conductors and insulators, and doping introduces small amounts of impurity atoms to precisely control that conductivity.',
  [('Where does a semiconductor’s electrical conductivity typically fall?', ['Between that of a conductor and an insulator', 'Always exactly equal to that of a perfect conductor', 'A concept unrelated to chemistry', 'Always exactly equal to that of a perfect insulator'], 0),
   ('Does doping involve introducing small amounts of impurity atoms into a semiconductor?', ['Yes', 'No, doping never involves adding any impurity atoms', 'A concept unrelated to semiconductors', 'Impurity atoms have no connection to a semiconductor’s properties'], 0),
   ('Can doping be used to increase a semiconductor’s electrical conductivity?', ['Yes', 'No, doping always decreases a semiconductor’s conductivity to zero', 'A concept unrelated to doping', 'Conductivity is never affected by doping a semiconductor'], 0),
   ('Why might adding an impurity atom with an extra valence electron increase a semiconductor’s conductivity?', ['The additional electron is not needed for bonding and becomes free to move, carrying electrical current more readily', 'An extra valence electron never has any effect on conductivity', 'This concept has no connection to chemistry', 'Valence electrons have no relationship to how electrical current moves through a material'], 0),
   ('Why are semiconductors, rather than pure conductors or insulators, essential to modern electronic devices?', ['Their conductivity can be precisely controlled through doping, allowing engineers to build components like transistors that switch and amplify signals', 'Semiconductors have no practical application in modern electronic devices', 'This concept has no relevance to chemistry', 'Conductors and insulators are always more useful than semiconductors in every electronic application'], 0)]),
]),

day(94, [
E('Rhetoric: Anaphora, Chiasmus, and Parallelism',
  'Grade 11 English strand: rhetorical schemes such as anaphora, chiasmus, and parallelism use deliberate patterns of repetition and structure to make a speaker’s or writer’s language more memorable and persuasive.',
  [('What do rhetorical schemes like anaphora and parallelism rely on?', ['Deliberate patterns of repetition and structure', 'Only unrelated facts and statistics', 'A concept unrelated to rhetoric', 'Random, unstructured word choices'], 0),
   ('Does anaphora involve repeating a word or phrase at the beginning of successive clauses or sentences?', ['Yes', 'No, anaphora never involves repeating any word or phrase', 'A concept unrelated to rhetorical schemes', 'Repetition has no connection to anaphora as a rhetorical device'], 0),
   ('Does chiasmus involve reversing the grammatical structure of a phrase in its second half?', ['Yes', 'No, chiasmus never involves reversing any grammatical structure', 'A concept unrelated to chiasmus', 'Grammatical structure has no connection to chiasmus'], 0),
   ('Which of these best illustrates anaphora?', ['We shall fight on the beaches, we shall fight on the landing grounds, we shall fight in the fields.', 'The chemical symbol for sodium is Na.', 'Add 12 and 8 to get 20.', 'The train departs the station at nine o’clock.'], 0),
   ('Why might a speaker use parallelism when listing several related ideas in a persuasive speech?', ['The repeated grammatical structure creates rhythm and makes the ideas easier for an audience to follow and remember', 'Parallelism never has any effect on how an audience follows or remembers ideas', 'This concept has no connection to rhetoric', 'A persuasive speech is always more effective without any repeated structure'], 0)]),
F('Discrete Math: Matrices — Determinants and the Inverse of a 2×2 Matrix',
  'Grade 11 Functions strand: the determinant of a 2×2 matrix is a single value calculated from its entries, and a matrix has an inverse only when its determinant is non-zero.',
  [('What is the determinant of a 2 by 2 matrix?', ['A single value calculated from the matrix’s entries', 'A completely new matrix with unrelated entries', 'A concept unrelated to matrices', 'Always equal to zero regardless of the matrix'], 0),
   ('Does a 2 by 2 matrix have an inverse only when its determinant is non-zero?', ['Yes', 'No, every matrix has an inverse regardless of its determinant', 'A concept unrelated to matrix determinants', 'A matrix’s inverse is never related to its determinant'], 0),
   ('For a 2 by 2 matrix with entries a and b in the top row and c and d in the bottom row, what is the formula for its determinant?', ['ad minus bc', 'ac minus bd', 'ab minus cd', 'ad plus bc'], 0),
   ('Why does a matrix with a determinant of zero fail to have an inverse?', ['A zero determinant means the matrix inverse formula would require dividing by zero, which is undefined', 'A matrix with a determinant of zero always has an inverse just like any other matrix', 'This concept has no connection to matrices', 'Determinants have no relationship to whether a matrix inverse exists'], 0),
   ('Why is the ability to find a matrix’s inverse useful for solving a system of linear equations written in matrix form?', ['Multiplying both sides of the matrix equation by the inverse isolates the variable matrix, revealing the solution', 'A matrix inverse is never useful for solving any system of linear equations', 'This concept has no relevance to functions', 'Systems of linear equations can never be represented using matrices'], 0)]),
B('Ecology: Population Growth Models — Exponential and Logistic Growth',
  'Grade 11 Biology strand: exponential growth models describe a population increasing without limit under ideal conditions, while logistic growth models incorporate a carrying capacity that slows growth as resources become limited.',
  [('What does an exponential growth model assume about a population’s growth?', ['That it increases without limit under ideal conditions', 'That it always decreases steadily over time', 'A concept unrelated to biology', 'That population size never changes at all'], 0),
   ('Does a logistic growth model incorporate a carrying capacity?', ['Yes', 'No, logistic growth models never incorporate a carrying capacity', 'A concept unrelated to population growth models', 'Carrying capacity has no connection to any population growth model'], 0),
   ('Does population growth typically slow down as a population approaches its environment’s carrying capacity in a logistic model?', ['Yes', 'No, population growth always accelerates near the carrying capacity', 'A concept unrelated to logistic growth', 'Carrying capacity never has any effect on the rate of population growth'], 0),
   ('Why might a population’s growth curve shift from exponential to logistic as resources like food and space become limited?', ['Competition for limited resources increases as population size grows, slowing the rate of increase', 'Limited resources never have any effect on a population’s rate of growth', 'This concept has no connection to biology', 'A population’s growth rate is always constant regardless of available resources'], 0),
   ('Why is the logistic growth model generally considered more realistic than the exponential model for most natural populations?', ['Real environments have finite resources, which eventually limit population growth rather than allowing it to increase indefinitely', 'The logistic growth model has no connection to how real populations actually grow', 'This concept has no relevance to biology', 'Natural populations can always grow indefinitely without any resource limitations'], 0)]),
C('Organic Chemistry: Chirality and Optical Isomers',
  'Grade 11 Chemistry strand: a chiral molecule has a non-superimposable mirror image, producing optical isomers, called enantiomers, that can rotate plane-polarized light in opposite directions.',
  [('What does a chiral molecule have?', ['A non-superimposable mirror image', 'No mirror image whatsoever', 'A concept unrelated to chemistry', 'An identical structure to every other molecule of its kind'], 0),
   ('Are the two mirror-image forms of a chiral molecule called enantiomers?', ['Yes', 'No, mirror-image forms of a chiral molecule have no special name', 'A concept unrelated to chirality', 'Enantiomers have no connection to chiral molecules'], 0),
   ('Can enantiomers rotate plane-polarized light in opposite directions from one another?', ['Yes', 'No, enantiomers never have any effect on plane-polarized light', 'A concept unrelated to optical isomers', 'Enantiomers always rotate plane-polarized light in exactly the same direction'], 0),
   ('Why might a carbon atom bonded to four different groups typically create a chiral centre in a molecule?', ['Such an arrangement usually has no internal symmetry, so its mirror image cannot be rotated to match the original', 'A carbon atom bonded to four different groups never creates a chiral centre', 'This concept has no connection to chemistry', 'Chirality has no relationship to the arrangement of groups bonded to a carbon atom'], 0),
   ('Why is chirality an important consideration in the development of pharmaceutical drugs?', ['Two enantiomers of the same drug can have very different biological effects in the body, so their distinct behaviour must be tested separately', 'Chirality has no connection to how a pharmaceutical drug behaves in the body', 'This concept has no relevance to chemistry', 'Enantiomers of the same drug always have identical effects on the body'], 0)]),
]),

day(95, [
E('Literature: The Parable and the Fable as Moral Narrative',
  'Grade 11 English strand: parables and fables are brief narrative forms that use a simple story, often featuring animals or ordinary people, to illustrate a moral lesson or universal truth.',
  [('What do parables and fables typically use a simple story to illustrate?', ['A moral lesson or universal truth', 'Only an unrelated historical event', 'A concept unrelated to literature', 'A detailed scientific process'], 0),
   ('Do fables often feature animals as characters that behave like humans?', ['Yes', 'No, fables never feature animals as characters', 'A concept unrelated to fables', 'Animal characters have no connection to this narrative form'], 0),
   ('Are parables and fables generally brief narrative forms?', ['Yes', 'No, parables and fables are always extremely long narratives', 'A concept unrelated to parables and fables', 'Length has no connection to how these narrative forms are defined'], 0),
   ('Which of these best exemplifies a fable?', ['A tortoise defeats a boastful hare in a race by moving slowly and steadily.', 'A detailed recipe for baking bread.', 'A weather report for the upcoming week.', 'A user manual for assembling furniture.'], 0),
   ('Why might a writer choose to teach a moral lesson through a fable rather than stating it directly as advice?', ['A memorable story can make an abstract lesson more engaging and easier to understand than a direct statement', 'A fable never makes a moral lesson easier to understand', 'This concept has no connection to literature', 'Stating a lesson directly as advice is always more memorable than telling a story'], 0)]),
F('Statistics: The Law of Large Numbers and Simulation',
  'Grade 11 Functions strand: the law of large numbers states that as the number of trials in a random experiment increases, the experimental probability tends to converge toward the theoretical probability.',
  [('What does the law of large numbers describe?', ['How experimental probability tends to converge toward theoretical probability as trials increase', 'How theoretical probability changes with every single trial', 'A concept unrelated to statistics', 'How a single trial always determines the exact probability'], 0),
   ('Does flipping a fair coin many more times generally bring the experimental proportion of heads closer to 50 percent?', ['Yes', 'No, flipping a coin more times never brings the results closer to the theoretical probability', 'A concept unrelated to the law of large numbers', 'The number of coin flips never affects the observed proportion of heads'], 0),
   ('Can a simulation be used to estimate a probability that would be difficult to calculate directly?', ['Yes', 'No, simulations are never useful for estimating probabilities', 'A concept unrelated to simulation', 'Simulations only ever produce completely inaccurate probability estimates'], 0),
   ('Why might the experimental probability from only 10 coin flips differ noticeably from the theoretical probability of 50 percent?', ['With a small number of trials, random variation has a much larger relative effect on the observed results', 'A small number of trials always produces results identical to the theoretical probability', 'This concept has no connection to statistics', 'Random variation never has any effect on the outcome of a small number of trials'], 0),
   ('Why is the law of large numbers an important justification for using simulations to estimate probabilities?', ['It shows that running a very large number of trials produces results that reliably approximate the true probability', 'The law of large numbers has no connection to why simulations are considered reliable', 'This concept has no relevance to statistics', 'Simulations never become more accurate no matter how many trials are run'], 0)]),
B('Ecology: Bioaccumulation and Biomagnification in Food Webs',
  'Grade 11 Biology strand: bioaccumulation describes how a toxin builds up within an individual organism over time, while biomagnification describes how that toxin’s concentration increases at each successive trophic level in a food web.',
  [('What does bioaccumulation describe?', ['How a toxin builds up within an individual organism over time', 'How a toxin instantly disappears from an organism’s body', 'A concept unrelated to biology', 'How energy flows between different ecosystems'], 0),
   ('Does biomagnification describe increasing toxin concentration at higher trophic levels?', ['Yes', 'No, biomagnification has no connection to trophic levels', 'A concept unrelated to biomagnification', 'Toxin concentration never changes between trophic levels'], 0),
   ('Are top predators generally at greater risk from biomagnified toxins than organisms lower on the food chain?', ['Yes', 'No, top predators are never at any greater risk from biomagnified toxins', 'A concept unrelated to bioaccumulation and biomagnification', 'Risk from toxins is always identical across every trophic level'], 0),
   ('Why might a toxin like mercury reach dangerously high concentrations in large predatory fish, even in relatively clean water?', ['Each predator eats many smaller organisms containing the toxin, causing it to accumulate at increasingly higher concentrations up the food chain', 'Mercury concentrations never increase as they move up a food chain', 'This concept has no connection to biology', 'Predatory fish are never affected by toxins present in their prey'], 0),
   ('Why is understanding biomagnification important for setting guidelines on fish consumption?', ['It helps identify which species, often top predators, are more likely to contain unsafe concentrations of accumulated toxins', 'Biomagnification has no connection to fish consumption guidelines', 'This concept has no relevance to biology', 'All fish species contain exactly the same concentration of toxins regardless of diet'], 0)]),
C('Materials Chemistry: Carbon Allotropes — Graphite, Diamond, and Graphene',
  'Grade 11 Chemistry strand: carbon allotropes such as graphite, diamond, and graphene are composed entirely of carbon atoms, but their differing bonding arrangements give them dramatically different physical properties.',
  [('What are carbon allotropes composed entirely of?', ['Carbon atoms', 'A mixture of several different elements', 'A concept unrelated to chemistry', 'Only hydrogen and oxygen atoms'], 0),
   ('Do graphite, diamond, and graphene have dramatically different physical properties despite being made of the same element?', ['Yes', 'No, these three carbon allotropes always have identical physical properties', 'A concept unrelated to carbon allotropes', 'Physical properties have no connection to how carbon atoms are bonded'], 0),
   ('Is diamond, with its rigid three-dimensional bonding structure, extremely hard?', ['Yes', 'No, diamond is actually one of the softest known materials', 'A concept unrelated to diamond’s structure', 'Hardness has no connection to a material’s bonding structure'], 0),
   ('Why does graphite conduct electricity while diamond does not, despite both being pure carbon?', ['Graphite’s layered structure includes delocalized electrons that can move freely, while diamond’s electrons are all locked into fixed covalent bonds', 'Graphite and diamond always conduct electricity in exactly the same way', 'This concept has no connection to chemistry', 'Electrical conductivity has no relationship to how carbon atoms are bonded together'], 0),
   ('Why is graphene, a single layer of graphite, considered a material of significant scientific interest?', ['Its unique two-dimensional structure gives it exceptional strength and electrical conductivity for its minimal thickness', 'Graphene has no unusual properties compared to ordinary graphite', 'This concept has no relevance to chemistry', 'A single layer of graphite is never considered scientifically significant'], 0)]),
]),

day(96, [
E('Writing: The Public Service Announcement and Advocacy Writing',
  'Grade 11 English strand: a public service announcement uses concise, persuasive language and a clear call to action to raise awareness of a social issue and encourage a specific audience response.',
  [('What does a public service announcement use to raise awareness of a social issue?', ['Concise, persuasive language and a clear call to action', 'Only lengthy, unrelated statistics with no clear message', 'A concept unrelated to writing', 'A neutral tone with no persuasive intent at all'], 0),
   ('Does an effective public service announcement typically include a clear call to action?', ['Yes', 'No, public service announcements never include any call to action', 'A concept unrelated to advocacy writing', 'A call to action is never relevant to this type of writing'], 0),
   ('Is a public service announcement generally intended to encourage a specific audience response?', ['Yes', 'No, public service announcements are never intended to influence audience behaviour', 'A concept unrelated to public service announcements', 'Audience response is never a consideration in this form of writing'], 0),
   ('Why might a public service announcement about road safety use a brief, urgent tone rather than a long, detailed explanation?', ['A short, urgent message is more likely to capture attention and be remembered quickly by a broad audience', 'A brief, urgent tone never helps a message capture an audience’s attention', 'This concept has no connection to writing', 'Long, detailed explanations are always more effective in this type of writing'], 0),
   ('Why is identifying a target audience important when writing an effective public service announcement?', ['Language, tone, and examples can be tailored to resonate with a specific audience, increasing the message’s persuasive impact', 'Identifying a target audience never affects how persuasive a message is', 'This concept has no relevance to writing', 'A public service announcement is always equally effective regardless of its intended audience'], 0)]),
F('Functions: Laws of Exponents and Rational Exponents',
  'Grade 11 Functions strand: the laws of exponents describe how to simplify expressions involving powers, and a rational exponent expresses a root, such as a square or cube root, using fractional notation.',
  [('What do the laws of exponents describe?', ['How to simplify expressions involving powers', 'How to graph a linear equation', 'A concept unrelated to functions', 'How to convert a fraction into a decimal'], 0),
   ('Does a rational exponent express a root using fractional notation?', ['Yes', 'No, rational exponents have no connection to expressing roots', 'A concept unrelated to rational exponents', 'Fractional notation is never used to express a root'], 0),
   ('What does x raised to the power of one-half represent?', ['The square root of x', 'The cube root of x', 'x multiplied by one-half', 'x squared'], 0),
   ('Why does multiplying two powers with the same base result in adding their exponents?', ['Multiplying repeated factors of the same base combines the total count of that factor being multiplied together', 'Multiplying powers with the same base never involves adding the exponents', 'This concept has no connection to functions', 'The exponents of two powers being multiplied are always subtracted, never added'], 0),
   ('Why is rewriting a radical expression using a rational exponent often useful when simplifying complex algebraic expressions?', ['Rational exponents allow the standard laws of exponents to be applied directly, rather than working with radical notation', 'Rewriting a radical expression as a rational exponent never simplifies an algebraic expression', 'This concept has no relevance to functions', 'Radical expressions can never be rewritten using exponent notation'], 0)]),
B('Evolution: Convergent and Divergent Evolution',
  'Grade 11 Biology strand: convergent evolution occurs when unrelated species independently evolve similar traits in response to similar environmental pressures, while divergent evolution occurs when related species evolve increasingly different traits over time.',
  [('What does convergent evolution describe?', ['Unrelated species independently evolving similar traits', 'A single species remaining completely unchanged over time', 'A concept unrelated to biology', 'Two species merging into a single new species'], 0),
   ('Does divergent evolution describe related species evolving increasingly different traits over time?', ['Yes', 'No, divergent evolution has no connection to how related species change over time', 'A concept unrelated to divergent evolution', 'Related species always remain identical to one another over time'], 0),
   ('Are the wings of bats and the wings of birds often cited as an example of convergent evolution?', ['Yes', 'No, bat and bird wings share no evolutionary similarities worth studying', 'A concept unrelated to convergent evolution', 'Bats and birds are always considered closely related species with shared ancestry'], 0),
   ('Why might unrelated species living in similar environments, such as sharks and dolphins, independently evolve a similar streamlined body shape?', ['Similar environmental pressures, like moving efficiently through water, can favour similar adaptations even in unrelated lineages', 'Unrelated species living in similar environments never develop any similar traits', 'This concept has no connection to biology', 'Body shape has no connection to how an organism moves through its environment'], 0),
   ('Why is comparing convergent and divergent evolution useful for understanding how environmental pressures shape species over time?', ['It highlights how similar pressures can produce similar traits in unrelated species, while shared ancestry can still lead to divergence under different pressures', 'Comparing convergent and divergent evolution provides no insight into how species change over time', 'This concept has no relevance to biology', 'Environmental pressures never have any influence on how a species evolves'], 0)]),
C('Analytical Chemistry: Acid-Base Indicators and Colour Change Theory',
  'Grade 11 Chemistry strand: an acid-base indicator is a weak acid or base that changes colour over a specific pH range because its protonated and deprotonated forms absorb different wavelengths of light.',
  [('What is an acid-base indicator?', ['A weak acid or base that changes colour over a specific pH range', 'A strong acid that never changes colour under any conditions', 'A concept unrelated to chemistry', 'A neutral compound with no relationship to pH'], 0),
   ('Do an indicator’s protonated and deprotonated forms typically absorb different wavelengths of light?', ['Yes', 'No, an indicator’s protonated and deprotonated forms always absorb identical wavelengths of light', 'A concept unrelated to acid-base indicators', 'Wavelength absorption has no connection to why an indicator changes colour'], 0),
   ('Can different indicators change colour at different pH ranges?', ['Yes', 'No, every acid-base indicator changes colour at exactly the same pH', 'A concept unrelated to indicator chemistry', 'pH has no connection to when an indicator changes colour'], 0),
   ('Why might a chemist choose a specific indicator, like phenolphthalein, for a particular titration?', ['The indicator’s colour-change range should closely match the pH at the titration’s equivalence point for an accurate result', 'The choice of indicator never affects the accuracy of a titration', 'This concept has no connection to chemistry', 'Every indicator produces identical results regardless of the titration being performed'], 0),
   ('Why is understanding the chemical mechanism behind an indicator’s colour change useful for interpreting titration results accurately?', ['It helps explain why the colour change occurs at a specific pH, allowing more precise determination of the endpoint', 'The chemical mechanism behind an indicator’s colour change has no connection to titration accuracy', 'This concept has no relevance to chemistry', 'Titration endpoints can never be determined using a colour-change indicator'], 0)]),
]),

day(97, [
E('Literary Criticism: Introduction to Feminist Reading',
  'Grade 11 English strand: a feminist reading of a text examines how gender roles, power dynamics, and the representation of women shape the story’s meaning, characters, and themes.',
  [('What does a feminist reading of a text examine?', ['How gender roles, power dynamics, and the representation of women shape the text’s meaning', 'Only the exact publication date of a text', 'A concept unrelated to literary criticism', 'The font and formatting used in a printed edition'], 0),
   ('Might a feminist reading consider how female characters are represented compared to male characters?', ['Yes', 'No, a feminist reading never compares how different characters are represented', 'A concept unrelated to feminist literary criticism', 'Character representation is never relevant to this critical approach'], 0),
   ('Can a feminist reading of a historical text reveal assumptions about gender that reflect the era in which it was written?', ['Yes', 'No, historical texts never reflect any assumptions about gender', 'A concept unrelated to feminist reading', 'The era in which a text was written has no connection to its portrayal of gender'], 0),
   ('Which of these questions would a feminist critic likely ask about a novel?', ['How are the female characters’ choices and agency portrayed compared to the male characters?', 'What font was used in the original printed edition?', 'How many chapters does this novel contain?', 'What year was the author born?'], 0),
   ('Why might feminist literary criticism be considered a valuable lens for re-examining classic works of literature?', ['It can reveal previously overlooked assumptions about gender roles and power embedded within a text', 'Feminist literary criticism has no connection to how gender roles are portrayed in literature', 'This concept has no relevance to literary criticism', 'Classic works of literature never contain any assumptions about gender worth examining'], 0)]),
F('Optimization: Linear Programming with Systems of Inequalities',
  'Grade 11 Functions strand: linear programming uses a system of linear inequalities to define a feasible region, within which the maximum or minimum value of an objective function typically occurs at a vertex.',
  [('What does a system of linear inequalities define in linear programming?', ['A feasible region', 'A single fixed point with no other possible solutions', 'A concept unrelated to functions', 'An equation with no possible solution at all'], 0),
   ('Does the maximum or minimum value of the objective function in linear programming typically occur at a vertex of the feasible region?', ['Yes', 'No, the maximum or minimum value is never located at a vertex', 'A concept unrelated to linear programming', 'The objective function’s extreme values are always found at the exact centre of the feasible region'], 0),
   ('Can linear programming be used to find the most cost-effective combination of resources given certain constraints?', ['Yes', 'No, linear programming has no application in resource allocation problems', 'A concept unrelated to linear programming', 'Cost-effectiveness can never be determined using systems of inequalities'], 0),
   ('Why is graphing the system of inequalities a useful first step in solving a linear programming problem?', ['It visually identifies the feasible region, narrowing down the possible solutions to a manageable set of vertices to test', 'Graphing a system of inequalities never helps identify possible solutions', 'This concept has no connection to functions', 'The feasible region can never be represented graphically'], 0),
   ('Why might a manufacturing company use linear programming to determine how many units of two products to produce?', ['It can find the combination that maximizes profit while respecting constraints like available materials, labour, or time', 'Linear programming has no practical application for a manufacturing company', 'This concept has no relevance to functions', 'Production decisions are never influenced by constraints on materials or labour'], 0)]),
B('Genetics: Linked Genes and Genetic Recombination',
  'Grade 11 Biology strand: linked genes are located close together on the same chromosome and tend to be inherited together, though genetic recombination during meiosis can separate them, with recombination frequency related to their physical distance apart.',
  [('What are linked genes?', ['Genes located close together on the same chromosome that tend to be inherited together', 'Genes located on completely different chromosomes', 'A concept unrelated to biology', 'Genes that never affect any inherited trait'], 0),
   ('Can genetic recombination during meiosis separate linked genes?', ['Yes', 'No, genetic recombination never separates linked genes', 'A concept unrelated to genetic recombination', 'Meiosis has no connection to the separation of linked genes'], 0),
   ('Is recombination frequency between two linked genes generally related to how physically close together they are on a chromosome?', ['Yes', 'No, recombination frequency has no connection to a gene’s physical location', 'A concept unrelated to linked genes', 'Physical distance between genes never affects how often they are separated'], 0),
   ('Why are genes located very close together on a chromosome less likely to be separated by recombination than genes located far apart?', ['Crossing over is less likely to occur between two points that are physically close together on the same chromosome', 'Genes located close together are always separated by recombination just as often as distant genes', 'This concept has no connection to biology', 'Crossing over occurs at exactly the same rate regardless of a gene’s physical location'], 0),
   ('Why is recombination frequency useful to geneticists constructing a chromosome map?', ['It provides an estimate of the relative distance between genes, helping to determine their order and spacing along a chromosome', 'Recombination frequency has no connection to mapping the location of genes on a chromosome', 'This concept has no relevance to biology', 'Chromosome maps can never be constructed using information about gene recombination'], 0)]),
C('Chemistry: Metallurgy — Extracting Metals from Their Ores',
  'Grade 11 Chemistry strand: metallurgy involves extracting metals from their ores through processes such as roasting, smelting, and electrolysis, often requiring a reduction reaction to convert metal compounds into pure metal.',
  [('What does metallurgy involve?', ['Extracting metals from their ores', 'Only measuring the temperature of a chemical reaction', 'A concept unrelated to chemistry', 'Growing crystals from a saturated solution'], 0),
   ('Can smelting be used as a process to extract metal from its ore?', ['Yes', 'No, smelting has no connection to extracting metal from ore', 'A concept unrelated to metallurgy', 'Smelting only ever separates two liquids, never extracts a metal'], 0),
   ('Does extracting a pure metal from its compound in an ore often require a reduction reaction?', ['Yes', 'No, extracting a metal from its ore never involves any reduction reaction', 'A concept unrelated to metallurgy', 'Reduction reactions are never relevant to metal extraction'], 0),
   ('Why might a highly reactive metal, such as aluminum, require electrolysis rather than simple heating to be extracted from its ore?', ['Highly reactive metals form very stable compounds that require a strong external source of energy, like an electric current, to reduce them to pure metal', 'Highly reactive metals never require any special process to be extracted from their ores', 'This concept has no connection to chemistry', 'Simple heating is always sufficient to extract any metal, regardless of its reactivity'], 0),
   ('Why is efficient metallurgical extraction important for industries that rely on large quantities of refined metal?', ['More efficient extraction processes can reduce energy use, cost, and environmental impact while producing usable metal from raw ore', 'Efficient metallurgical extraction has no connection to industrial cost or environmental impact', 'This concept has no relevance to chemistry', 'Metal extraction processes never have any effect on the environment'], 0)]),
]),

day(98, [
E('Oral Communication: Spoken Word and Performance Poetry',
  'Grade 11 English strand: spoken word and performance poetry are composed to be delivered aloud, relying on rhythm, vocal emphasis, and physical delivery to convey meaning alongside the words themselves.',
  [('What are spoken word and performance poetry composed to be?', ['Delivered aloud', 'Only read silently by a single reader', 'A concept unrelated to oral communication', 'Printed exclusively in academic textbooks'], 0),
   ('Does performance poetry rely on rhythm and vocal emphasis to help convey meaning?', ['Yes', 'No, performance poetry never relies on rhythm or vocal emphasis', 'A concept unrelated to spoken word poetry', 'Rhythm and vocal emphasis have no connection to conveying meaning in this art form'], 0),
   ('Can physical delivery, such as gesture and pacing, affect how a performance poem is understood by an audience?', ['Yes', 'No, physical delivery never affects how an audience understands a poem', 'A concept unrelated to performance poetry', 'Gesture and pacing are never relevant to performance poetry'], 0),
   ('Why might a spoken word poet repeat a key phrase with increasing intensity throughout a performance?', ['Vocal repetition and rising intensity can build emotional momentum and emphasize the phrase’s central importance', 'Repeating a phrase with increasing intensity never has any effect on a performance', 'This concept has no connection to oral communication', 'Emotional momentum is never something a spoken word performance can build'], 0),
   ('Why is performance poetry sometimes considered a distinct art form from poetry meant primarily to be read silently on a page?', ['Its meaning depends heavily on the live, aural, and physical elements of delivery, not just the words themselves', 'Performance poetry has no meaningful difference from poetry read silently on a page', 'This concept has no relevance to oral communication', 'The words themselves are always the only element that matters in any form of poetry'], 0)]),
F('Functions: Rate of Change of Polynomial Functions — Finite Differences',
  'Grade 11 Functions strand: the method of finite differences uses a table of equally spaced values to determine the degree of a polynomial function, since the nth differences of an nth-degree polynomial are constant.',
  [('What does the method of finite differences use to determine a polynomial’s degree?', ['A table of equally spaced values', 'A single isolated data point with no surrounding values', 'A concept unrelated to functions', 'The exact colour of a graphed function’s line'], 0),
   ('For an nth-degree polynomial, are the nth differences constant?', ['Yes', 'No, the nth differences of an nth-degree polynomial are never constant', 'A concept unrelated to finite differences', 'The degree of a polynomial has no connection to its finite differences'], 0),
   ('If the first differences in a table of values are constant, is the underlying function linear?', ['Yes', 'No, constant first differences never indicate a linear function', 'A concept unrelated to finite differences', 'Constant first differences always indicate a quadratic function instead'], 0),
   ('Why does finding constant second differences in a table of values indicate that the underlying function is quadratic?', ['A quadratic function’s rate of change itself changes at a constant rate, so taking differences of the differences produces a constant value', 'Constant second differences never indicate anything about the type of underlying function', 'This concept has no connection to functions', 'Second differences are never used to identify the degree of a polynomial function'], 0),
   ('Why is the method of finite differences useful when working with a table of data rather than an explicit function equation?', ['It allows the degree of the underlying polynomial to be identified directly from patterns in the data, without needing to know the function’s equation in advance', 'Finite differences are never useful when only a table of data is available', 'This concept has no relevance to functions', 'Identifying a polynomial’s degree always requires knowing its equation beforehand'], 0)]),
B('Microbiology: Viral Replication Cycles — Lytic and Lysogenic',
  'Grade 11 Biology strand: viruses replicate within a host cell through either the lytic cycle, which quickly destroys the host cell to release new viruses, or the lysogenic cycle, which integrates viral genetic material into the host genome before later becoming active.',
  [('What does the lytic cycle of viral replication do to the host cell?', ['Quickly destroys it to release new viruses', 'Leaves it completely unaffected and unchanged', 'A concept unrelated to biology', 'Permanently repairs any existing cell damage'], 0),
   ('Does the lysogenic cycle involve integrating viral genetic material into the host genome?', ['Yes', 'No, the lysogenic cycle never integrates any genetic material into the host', 'A concept unrelated to viral replication', 'The host genome is never involved in the lysogenic cycle'], 0),
   ('Can a virus in the lysogenic cycle remain dormant within a host for an extended period before becoming active?', ['Yes', 'No, a virus in the lysogenic cycle is always immediately active', 'A concept unrelated to lysogenic replication', 'Dormancy is never a feature of viral replication cycles'], 0),
   ('Why might a virus following the lysogenic cycle eventually switch to the lytic cycle under certain conditions, such as host cell stress?', ['Environmental triggers can activate the dormant viral genetic material, prompting it to begin actively replicating and producing new viruses', 'A virus following the lysogenic cycle can never switch to the lytic cycle under any circumstances', 'This concept has no connection to biology', 'Host cell stress never has any effect on dormant viral genetic material'], 0),
   ('Why is understanding the difference between the lytic and lysogenic cycles important for developing antiviral treatments?', ['Different replication strategies may require different approaches to detect, prevent, or interrupt viral activity within the host', 'The lytic and lysogenic cycles have no connection to how antiviral treatments are developed', 'This concept has no relevance to biology', 'All viruses replicate using exactly the same strategy regardless of species'], 0)]),
C('Chemistry: The Haber-Bosch Process and Industrial Equilibrium',
  'Grade 11 Chemistry strand: the Haber-Bosch process synthesizes ammonia from nitrogen and hydrogen gas, applying principles of chemical equilibrium and Le Chatelier’s principle to maximize industrial yield under carefully controlled temperature and pressure.',
  [('What does the Haber-Bosch process synthesize?', ['Ammonia, from nitrogen and hydrogen gas', 'Pure oxygen gas from water', 'A concept unrelated to chemistry', 'Table salt from sodium and chlorine only'], 0),
   ('Does the Haber-Bosch process apply principles of chemical equilibrium to maximize yield?', ['Yes', 'No, the Haber-Bosch process has no connection to chemical equilibrium', 'A concept unrelated to industrial chemistry', 'Chemical equilibrium is never relevant to industrial ammonia production'], 0),
   ('Is temperature and pressure carefully controlled in the Haber-Bosch process to improve ammonia yield?', ['Yes', 'No, temperature and pressure have no effect on ammonia yield', 'A concept unrelated to the Haber-Bosch process', 'Ammonia yield is never affected by reaction conditions'], 0),
   ('Why might increasing pressure help shift the Haber-Bosch equilibrium toward producing more ammonia?', ['According to Le Chatelier’s principle, increasing pressure favours the side of the reaction with fewer gas molecules, which is the ammonia product side', 'Increasing pressure never has any effect on the position of a chemical equilibrium', 'This concept has no connection to chemistry', 'Le Chatelier’s principle has no relationship to how pressure affects a reaction at equilibrium'], 0),
   ('Why is the Haber-Bosch process considered one of the most significant achievements in industrial chemistry?', ['It enabled the large-scale production of ammonia for fertilizer, dramatically increasing global agricultural output', 'The Haber-Bosch process has no connection to agricultural production', 'This concept has no relevance to chemistry', 'Ammonia produced by this process has never been used for any practical purpose'], 0)]),
]),

day(99, [
E('Literature: Allusion and Intertextuality in Fiction',
  'Grade 11 English strand: allusion is a brief reference to another text, event, or figure, and intertextuality describes how texts gain meaning through their relationships and connections with other texts.',
  [('What is an allusion?', ['A brief reference to another text, event, or figure', 'A complete retelling of an entire unrelated story', 'A concept unrelated to literature', 'A footnote explaining a word’s dictionary definition'], 0),
   ('Does intertextuality describe how texts gain meaning through connections with other texts?', ['Yes', 'No, intertextuality has no connection to how texts relate to one another', 'A concept unrelated to intertextuality', 'Texts never gain meaning through any relationship with other texts'], 0),
   ('Might recognizing an allusion deepen a reader’s understanding of a passage’s meaning?', ['Yes', 'No, recognizing an allusion never affects how a reader understands a passage', 'A concept unrelated to allusion', 'A passage’s meaning is never influenced by references to other texts'], 0),
   ('Which of these sentences contains a clear literary allusion?', ['Their journey felt like a modern odyssey, full of unexpected trials at every turn.', 'The chemical formula for methane is CH4.', 'Add 12 and 8 to get 20.', 'The train departs at exactly noon.'], 0),
   ('Why might an author use allusion to reference a well-known myth rather than fully explaining the connection they intend?', ['A concise reference can evoke rich, shared associations for readers already familiar with the original source, adding depth without lengthy explanation', 'Allusion never adds any depth or meaning to a piece of writing', 'This concept has no connection to literature', 'Authors always fully explain every reference they make within a text'], 0)]),
F('Number Theory: Prime Factorization and the Fundamental Theorem of Arithmetic',
  'Grade 11 Functions strand: the fundamental theorem of arithmetic states that every integer greater than 1 can be expressed as a unique product of prime factors, forming the basis of prime factorization.',
  [('What does the fundamental theorem of arithmetic state?', ['Every integer greater than 1 can be expressed as a unique product of prime factors', 'Every integer can be divided evenly by exactly two other numbers', 'A concept unrelated to number theory', 'Prime numbers cannot be multiplied together under any circumstances'], 0),
   ('Is the prime factorization of a given integer unique, aside from the order of the factors?', ['Yes', 'No, a single integer can have many completely different prime factorizations', 'A concept unrelated to prime factorization', 'Prime factorization is never unique for any given integer'], 0),
   ('What is the prime factorization of 60?', ['2 squared times 3 times 5', '2 times 3 squared times 5', '2 times 3 times 5 squared', '2 times 5 times 7'], 0),
   ('Why is 1 excluded from being considered a prime number in the context of the fundamental theorem of arithmetic?', ['Including 1 as a prime would allow infinitely many different factorizations of the same integer, violating the uniqueness of prime factorization', '1 is always classified as the smallest prime number in every mathematical context', 'This concept has no connection to number theory', 'Excluding 1 from the primes has no effect on the uniqueness of prime factorization'], 0),
   ('Why is prime factorization a useful tool for finding the greatest common factor of two integers?', ['Comparing the shared prime factors between two factorizations reveals the largest factor common to both integers', 'Prime factorization has no connection to finding a greatest common factor', 'This concept has no relevance to functions', 'The greatest common factor of two integers can never be determined using their prime factorizations'], 0)]),
B('Human Biology: The Special Senses — Hearing and Balance',
  'Grade 11 Biology strand: the inner ear contains structures responsible for both hearing, through the cochlea’s conversion of sound vibrations into nerve impulses, and balance, through the vestibular system’s detection of head position and movement.',
  [('What structure in the inner ear converts sound vibrations into nerve impulses?', ['The cochlea', 'The eardrum alone', 'A concept unrelated to biology', 'The outer ear canal'], 0),
   ('Does the vestibular system help detect head position and movement?', ['Yes', 'No, the vestibular system has no connection to detecting head position or movement', 'A concept unrelated to the special senses', 'Head position and movement are never detected by any structure in the ear'], 0),
   ('Is the sense of balance controlled by structures located in the inner ear?', ['Yes', 'No, balance is controlled entirely by structures located outside the ear', 'A concept unrelated to human biology', 'The inner ear has no connection to a person’s sense of balance'], 0),
   ('Why might damage to the inner ear affect both a person’s hearing and their sense of balance?', ['The cochlea and the vestibular system are both located within the inner ear, so damage to this region can disrupt either or both functions', 'Damage to the inner ear never affects hearing or balance in any way', 'This concept has no connection to biology', 'Hearing and balance are controlled by completely separate, unrelated organs'], 0),
   ('Why is understanding the structures of the inner ear important for diagnosing conditions that cause dizziness or vertigo?', ['Many balance disorders originate from disruptions in the vestibular system, so identifying the affected structure can guide accurate diagnosis and treatment', 'The structures of the inner ear have no connection to conditions causing dizziness or vertigo', 'This concept has no relevance to biology', 'Balance disorders are never related to any structure located within the ear'], 0)]),
C('Chemistry: Agricultural Chemistry — Fertilizers and Soil Nutrients',
  'Grade 11 Chemistry strand: fertilizers supply essential plant nutrients, particularly nitrogen, phosphorus, and potassium, in chemical forms that plant roots can readily absorb from the soil.',
  [('What three essential nutrients do many fertilizers supply, abbreviated NPK?', ['Nitrogen, phosphorus, and potassium', 'Carbon, hydrogen, and oxygen', 'A concept unrelated to chemistry', 'Sodium, chlorine, and calcium'], 0),
   ('Are fertilizer nutrients typically provided in chemical forms that plant roots can readily absorb?', ['Yes', 'No, fertilizer nutrients are never in a form that plant roots can absorb', 'A concept unrelated to agricultural chemistry', 'Plant roots are never able to absorb any nutrients from fertilizer'], 0),
   ('Can excessive fertilizer use contribute to nutrient runoff into nearby water systems?', ['Yes', 'No, fertilizer use never has any effect on nearby water systems', 'A concept unrelated to agricultural chemistry', 'Nutrient runoff has no connection to how much fertilizer is applied'], 0),
   ('Why might a farmer test soil nutrient levels before applying fertilizer to a field?', ['Testing reveals which nutrients are already sufficient and which are lacking, allowing more precise and efficient fertilizer application', 'Testing soil nutrient levels never provides any useful information for a farmer', 'This concept has no connection to chemistry', 'Fertilizer should always be applied in the same amount regardless of existing soil nutrients'], 0),
   ('Why is nutrient runoff from over-fertilized fields a significant concern for nearby aquatic ecosystems?', ['Excess nutrients entering waterways can trigger algal blooms that deplete oxygen and harm aquatic life', 'Nutrient runoff has no connection to the health of nearby aquatic ecosystems', 'This concept has no relevance to chemistry', 'Algal blooms are never linked to excess nutrients entering a body of water'], 0)]),
]),

day(100, [
E('Review: Postcolonialism, Rhetoric, and Literary Form (Days 91-99)',
  'Grade 11 English strand review: students revisit the postcolonial novel, the personal diary and journal, the sonnet form, rhetorical schemes, the parable and fable, public service announcements, feminist reading, spoken word poetry, and allusion.',
  [('What does postcolonial literature often examine?', ['The lasting cultural, political, and psychological effects of colonialism', 'Only the geography of a fictional setting', 'A concept unrelated to literature', 'The exact publication date of a novel'], 0),
   ('How many lines does a traditional sonnet contain?', ['Fourteen', 'Ten', 'A concept unrelated to poetry', 'Twenty'], 0),
   ('Does anaphora involve repeating a word or phrase at the beginning of successive clauses or sentences?', ['Yes', 'No, anaphora never involves repeating any word or phrase', 'A concept unrelated to rhetorical schemes', 'Repetition has no connection to anaphora as a rhetorical device'], 0),
   ('What does a feminist reading of a text examine?', ['How gender roles, power dynamics, and the representation of women shape the text’s meaning', 'Only the exact publication date of a text', 'A concept unrelated to literary criticism', 'The font and formatting used in a printed edition'], 0),
   ('What is an allusion?', ['A brief reference to another text, event, or figure', 'A complete retelling of an entire unrelated story', 'A concept unrelated to literature', 'A footnote explaining a word’s dictionary definition'], 0)]),
F('Review: Functions, Matrices, and Number Theory (Days 91-99)',
  'Grade 11 Functions strand review: students revisit operations on functions, synthetic division and the remainder theorem, sum and difference identities, matrix determinants, the law of large numbers, laws of exponents, linear programming, finite differences, and prime factorization.',
  [('Which operations can be used to combine two functions into a new function?', ['Addition, subtraction, multiplication, and division', 'Only addition, with no other operation permitted', 'A concept unrelated to functions', 'None, since functions can never be combined'], 0),
   ('What does synthetic division streamline?', ['Dividing a polynomial by a linear binomial', 'Multiplying two large polynomials together', 'A concept unrelated to functions', 'Graphing a function on a coordinate plane'], 0),
   ('For a 2 by 2 matrix with entries a and b in the top row and c and d in the bottom row, what is the formula for its determinant?', ['ad minus bc', 'ac minus bd', 'ab minus cd', 'ad plus bc'], 0),
   ('What does a system of linear inequalities define in linear programming?', ['A feasible region', 'A single fixed point with no other possible solutions', 'A concept unrelated to functions', 'An equation with no possible solution at all'], 0),
   ('What does the fundamental theorem of arithmetic state?', ['Every integer greater than 1 can be expressed as a unique product of prime factors', 'Every integer can be divided evenly by exactly two other numbers', 'A concept unrelated to number theory', 'Prime numbers cannot be multiplied together under any circumstances'], 0)]),
B('Review: Physiology, Genetics, and Ecology (Days 91-99)',
  'Grade 11 Biology strand review: students revisit thermoregulation, the operon model, plant defences against herbivory, population growth models, bioaccumulation and biomagnification, convergent and divergent evolution, linked genes, viral replication cycles, and the special senses.',
  [('What do endotherms use to maintain a stable body temperature?', ['Heat generated internally by their own metabolism', 'Only heat absorbed from the surrounding environment', 'A concept unrelated to biology', 'Nothing at all related to temperature regulation'], 0),
   ('What does the operon model explain in prokaryotic cells?', ['How groups of related genes are switched on or off together', 'How a single unrelated protein is broken down', 'A concept unrelated to biology', 'How cells physically divide during mitosis'], 0),
   ('What does bioaccumulation describe?', ['How a toxin builds up within an individual organism over time', 'How a toxin instantly disappears from an organism’s body', 'A concept unrelated to biology', 'How energy flows between different ecosystems'], 0),
   ('What are linked genes?', ['Genes located close together on the same chromosome that tend to be inherited together', 'Genes located on completely different chromosomes', 'A concept unrelated to biology', 'Genes that never affect any inherited trait'], 0),
   ('What structure in the inner ear converts sound vibrations into nerve impulses?', ['The cochlea', 'The eardrum alone', 'A concept unrelated to biology', 'The outer ear canal'], 0)]),
C('Review: Atomic Structure, Materials, and Industrial Chemistry (Days 91-99)',
  'Grade 11 Chemistry strand review: students revisit electron configuration, sunscreen chemistry, semiconductors and doping, chirality, carbon allotropes, acid-base indicators, metallurgy, the Haber-Bosch process, and agricultural chemistry.',
  [('What does electron configuration describe?', ['How electrons are arranged within an atom’s orbitals', 'Only the mass of an atom’s nucleus', 'A concept unrelated to chemistry', 'The exact colour an element appears in solid form'], 0),
   ('Where does a semiconductor’s electrical conductivity typically fall?', ['Between that of a conductor and an insulator', 'Always exactly equal to that of a perfect conductor', 'A concept unrelated to chemistry', 'Always exactly equal to that of a perfect insulator'], 0),
   ('What does a chiral molecule have?', ['A non-superimposable mirror image', 'No mirror image whatsoever', 'A concept unrelated to chemistry', 'An identical structure to every other molecule of its kind'], 0),
   ('What does metallurgy involve?', ['Extracting metals from their ores', 'Only measuring the temperature of a chemical reaction', 'A concept unrelated to chemistry', 'Growing crystals from a saturated solution'], 0),
   ('What three essential nutrients do many fertilizers supply, abbreviated NPK?', ['Nitrogen, phosphorus, and potassium', 'Carbon, hydrogen, and oxygen', 'A concept unrelated to chemistry', 'Sodium, chlorine, and calcium'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_91_100)
    append_to(11, g11_91_100)
