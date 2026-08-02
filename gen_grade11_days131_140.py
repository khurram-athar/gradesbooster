#!/usr/bin/env python3
"""Grade 11, Days 131-140 -- extends Grade 11 from 130 to 140 days. Topics
chosen after dumping the existing Day 1-130 title list (data/grade11.json)
in full and cross-checking against it to avoid any overlap: the ode,
utopian fiction, the rhetorical precis, modal verbs and certainty, the
roman-fleuve, astroturfing, the lyric essay, the doppelganger motif, and
handling audience questions; the power rule for derivatives, tangent
lines, Eulers formula for planar graphs, linear congruences and modular
inverses, the chi-square test, the rule of 72, polar/exponential form of
complex numbers, graph isomorphism, and continued fractions; epistasis,
vestigial structures, photosynthetic pigments and chromatography,
chemoreception, countercurrent exchange, autoimmune disorders,
detritivores, the renin-angiotensin system, and genomic imprinting;
isomerism in coordination compounds, saponification, water softening,
silicone polymers, the sol-gel process, fluoride chemistry, hemoglobin
and iron coordination, freezing point depression, and shape-memory
alloys. Day 140 is a lighter cross-subject review day, matching the
structure of the Day 120 and Day 130 review days (one review lesson per
subject, each reusing five first-questions verbatim from the batch).

Subject keys for Grade 11 are "English", "Functions", "Biology",
"Chemistry" (same as all earlier Grade 11 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes are avoided entirely.
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


def _rebalance_answer_positions(days, seed=20260801):
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


g11_131_140 = [
day(131, [
E('Poetry: The Ode — Form and Address to a Subject',
  'Grade 11 English strand: an ode is a formal, often elevated lyric poem that directly addresses and celebrates a person, object, or abstract quality, traditionally using a structured stanza pattern to build sustained praise or reflection.',
  [('What does an ode typically do?', ['Directly addresses and celebrates a person, object, or abstract quality', 'Presents a purely factual news report with no emotional content', 'Avoids any direct address to its subject', 'Functions only as a legal or contractual document'], 0),
   ('What tone does an ode traditionally use?', ['A formal, elevated tone of sustained praise or reflection', 'A casual, joking tone with no serious content', 'A tone of complete indifference to its subject', 'A purely instructional, step-by-step tone'], 0),
   ('Which of these could be the subject of an ode?', ['A beloved object, achievement, or abstract idea, addressed directly', 'Only geometric shapes, and nothing else', 'Only historical dates with no emotional content', 'Only grammar rules'], 0),
   ('How does an ode typically address its subject?', ['Speaking to it directly, often as if it could listen', 'Never mentioning the subject by name', 'Describing the subject only in the third person with no direct address', 'Ignoring the subject entirely after the title'], 0),
   ('Why might a poet choose the ode form rather than a shorter lyric?', ['Its structured stanza pattern supports sustained, developed reflection on a single subject', 'The ode form forbids any reflection on a single subject', 'Odes must always be shorter than a single sentence', 'The ode form has no structure of any kind'], 0)]),
F('Calculus Preview: The Power Rule for Derivatives',
  'Grade 11 Functions strand: the power rule states that the derivative of x raised to an exponent n is n times x raised to the exponent n minus 1, giving a quick algebraic shortcut for differentiating polynomial terms without returning to the limit definition each time.',
  [('What does the power rule provide?', ['A quick algebraic shortcut for differentiating polynomial terms', 'A method for factoring quadratic equations', 'A way to calculate the area under any curve exactly', 'A rule for simplifying fractions only'], 0),
   ('According to the power rule, what is the derivative of x to the power n?', ['n times x raised to the power n minus 1', 'x raised to the power n plus 1', 'n plus x', 'The reciprocal of x raised to the power n'], 0),
   ('What method does the power rule let you avoid repeating for every polynomial term?', ['Returning to the limit definition of the derivative each time', 'Multiplying every term by zero', 'Graphing the function by hand', 'Substituting random values into the function'], 0),
   ('What is the derivative of a constant term, according to the power rule family of results?', ['Zero', 'The constant itself', 'One', 'Infinity'], 0),
   ('How does the power rule relate to the earlier limit definition of the derivative?', ['It is a shortcut result that can itself be proven using the limit definition', 'It has no connection to the limit definition at all', 'It replaces the need for limits in every branch of mathematics', 'The power rule was discovered before the concept of a limit existed'], 0)]),
B('Genetics: Epistasis — Gene Interactions and Modified Ratios',
  'Grade 11 Biology strand: epistasis occurs when the expression of one gene is masked or modified by the effect of a different, non-allelic gene, producing phenotypic ratios that depart from the classic patterns predicted by simple Mendelian inheritance.',
  [('What is epistasis?', ['When the expression of one gene is masked or modified by a different, non-allelic gene', 'A process where a single gene has no effect on phenotype at all', 'A type of cell division unrelated to genetics', 'A disease caused only by environmental factors'], 0),
   ('What kind of phenotypic ratios does epistasis often produce?', ['Ratios that depart from the classic patterns predicted by simple Mendelian inheritance', 'Ratios that are always identical to simple Mendelian predictions', 'No measurable ratios of any kind', 'Ratios that depend only on environmental temperature'], 0),
   ('How many genes are involved in a typical epistatic interaction?', ['At least two different, non-allelic genes', 'Only a single gene acting alone', 'Every gene in the entire genome simultaneously', 'Zero genes, since epistasis is purely environmental'], 0),
   ('Why might epistasis make predicting offspring phenotypes more complex than a single-gene cross?', ['One gene can hide or alter the phenotypic effect of another gene entirely', 'Epistasis always makes phenotype prediction simpler than a single-gene cross', 'Epistasis has no effect on phenotype prediction at all', 'Only environmental factors affect phenotype when epistasis is present'], 0),
   ('Which of these best describes an epistatic gene?', ['A gene whose alleles can suppress or modify the phenotype produced by a different gene', 'A gene that has no interaction with any other gene', 'A gene found exclusively in bacteria', 'A gene that only affects eye colour'], 0)]),
C('Chemistry: Isomerism in Coordination Compounds — Geometric and Optical Isomers',
  'Grade 11 Chemistry strand: coordination compounds can display geometric isomerism, where ligands occupy different spatial arrangements around a central metal ion, and optical isomerism, where two non-superimposable mirror-image forms rotate polarized light in opposite directions.',
  [('What is geometric isomerism in a coordination compound?', ['Ligands occupying different spatial arrangements around the central metal ion', 'A change in the total number of electrons in the compound', 'A difference in the mass of the central metal ion', 'A reaction that produces an entirely different chemical formula'], 0),
   ('What defines optical isomers of a coordination compound?', ['Two non-superimposable mirror-image forms of the same compound', 'Two compounds with completely different chemical formulas', 'Two compounds that differ only in their physical state', 'Two identical compounds with no structural difference at all'], 0),
   ('How do optical isomers of a coordination compound interact with polarized light?', ['They rotate polarized light in opposite directions', 'They have no effect on polarized light at all', 'They absorb all light completely with no rotation', 'They rotate polarized light in the exact same direction'], 0),
   ('What part of a coordination compound do ligands surround in these isomeric arrangements?', ['The central metal ion', 'A separate, unrelated organic molecule', 'The outer electron shell of a noble gas', 'A carbon atom with no metal present'], 0),
   ('Why can two coordination compounds with the same chemical formula have different properties?', ['Their ligands can be arranged differently in space around the metal ion, creating distinct isomers', 'Identical chemical formulas always guarantee identical properties with no exceptions', 'Coordination compounds never share the same chemical formula', 'Only the colour of a compound can ever differ, never its properties'], 0)]),
]),
day(132, [
E('Literature: Utopian Fiction and the Ideal Society',
  'Grade 11 English strand: utopian fiction imagines a society organized around an idealized vision of order, equality, or harmony, often serving as a foil to dystopian fiction by exploring what a perfected world might require and whether it is achievable.',
  [('What does utopian fiction typically imagine?', ['An idealized society organized around order, equality, or harmony', 'A society with no organization of any kind', 'A society identical in every way to the authors own', 'A purely historical account with no imagined elements'], 0),
   ('How does utopian fiction often relate to dystopian fiction?', ['It serves as a contrasting foil exploring an idealized rather than a failed society', 'The two genres are identical with no meaningful difference', 'Utopian fiction always depicts total societal collapse', 'Dystopian fiction always depicts a perfect society'], 0),
   ('What central question do many utopian narratives explore?', ['Whether a truly perfected society is achievable and what it would require', 'Whether grammar rules should be abolished', 'Whether poetry should rhyme', 'Whether novels should have chapters'], 0),
   ('Which of these might a utopian narrative depict?', ['A community structured to eliminate poverty, conflict, or inequality', 'A community with no structure or planning whatsoever', 'A community deliberately designed to maximize suffering', 'A community with no relationship to social organization at all'], 0),
   ('Why might an author use a utopian setting to offer social commentary?', ['An idealized world lets the author highlight what is missing or flawed in real societies', 'A utopian setting removes any possibility of social commentary', 'Utopian settings are always purely decorative with no thematic purpose', 'Social commentary is impossible within a fictional setting'], 0)]),
F('Calculus Preview: Finding Equations of Tangent Lines Using Derivatives',
  'Grade 11 Functions strand: once the derivative of a function is known, its value at a specific point gives the slope of the tangent line there, which combined with the point itself allows a full equation of the tangent line to be written.',
  [('What does the derivative of a function at a specific point give?', ['The slope of the tangent line at that point', 'The total area under the entire curve', 'The y-intercept of the function', 'The maximum value of the function everywhere'], 0),
   ('What two pieces of information are needed to write the equation of a tangent line?', ['The slope from the derivative and a point on the curve', 'Only the y-intercept, with no slope required', 'Two unrelated points chosen at random', 'The area under the curve and its perimeter'], 0),
   ('Why is finding a tangent line equation a natural application of derivatives?', ['It directly uses the derivatives geometric meaning as an instantaneous slope', 'Tangent lines have no relationship to derivatives at all', 'Tangent lines can only be found using integration', 'Finding a tangent line requires no knowledge of slope'], 0),
   ('If a functions derivative at x = 2 is 5, what does that tell you about the tangent line there?', ['The tangent line at that point has a slope of 5', 'The tangent line at that point is horizontal', 'The function has a maximum value of 5 everywhere', 'The tangent line passes through the origin only'], 0),
   ('What form is commonly used to write a tangent line equation once slope and a point are known?', ['Point-slope form', 'Standard form of a circle', 'Quadratic formula', 'Pythagorean Theorem'], 0)]),
B('Biology: Vestigial Structures as Evidence for Evolution',
  'Grade 11 Biology strand: vestigial structures are anatomical features that have lost most or all of their original function through evolutionary history, persisting in reduced form as evidence of an organisms ancestry and shared descent with species in which the structure remains functional.',
  [('What are vestigial structures?', ['Anatomical features that have lost most or all of their original function over evolutionary history', 'Structures that appear only in embryos and never in adults of any species', 'New structures that have never existed in any ancestor', 'Structures found only in single-celled organisms'], 0),
   ('What do vestigial structures provide evidence for?', ['An organisms ancestry and shared descent with other species', 'The complete absence of evolutionary change in a species', 'A brand-new function unrelated to any ancestral trait', 'The idea that species never share common ancestors'], 0),
   ('Why might a vestigial structure persist even though it no longer serves its original function?', ['Reduced structures with little cost are not always strongly selected against', 'Natural selection always removes any structure with no function immediately', 'Vestigial structures always provide a major survival advantage', 'Vestigial structures are required for reproduction in every species'], 0),
   ('Which of these would be an example of a vestigial structure?', ['Small, non-functional hip bones in some whale species', 'A fully functional wing used for powered flight', 'A fully functional eye used for normal vision', 'A muscle used constantly for essential daily movement'], 0),
   ('How do vestigial structures differ from structures that were never present in an ancestral lineage?', ['Vestigial structures were once functional in an ancestor before becoming reduced', 'There is no difference between the two categories', 'Vestigial structures always appear only in the most recently evolved species', 'Structures never present in an ancestor are always larger than vestigial ones'], 0)]),
C('Chemistry: Saponification — The Chemistry of Soap Making',
  'Grade 11 Chemistry strand: saponification is the hydrolysis reaction of a fat or oil with a strong base that breaks triglycerides into glycerol and fatty acid salts, the fatty acid salts being the soap molecules that can bind both grease and water to lift dirt away.',
  [('What is saponification?', ['The hydrolysis reaction of a fat or oil with a strong base to form soap', 'A reaction that converts soap back into a fat or oil', 'A purely physical process with no chemical reaction involved', 'A reaction that only occurs between two acids'], 0),
   ('What two products does saponification break a triglyceride into?', ['Glycerol and fatty acid salts', 'Carbon dioxide and water only', 'Two identical fatty acid molecules with no glycerol', 'Oxygen gas and a metal oxide'], 0),
   ('Which product of saponification acts as soap?', ['The fatty acid salts', 'The glycerol byproduct', 'The strong base used in the reaction', 'Water released during the reaction'], 0),
   ('Why can soap molecules lift grease away using water?', ['They can bind both grease and water at the same time', 'They repel water completely and bind only to grease', 'They dissolve grease into a gas that evaporates instantly', 'They convert grease directly into glycerol'], 0),
   ('What type of reactant is required alongside a fat or oil to carry out saponification?', ['A strong base', 'A noble gas', 'A weak organic acid only', 'A pure metal with no other compound'], 0)]),
]),
day(133, [
E('Writing: The Rhetorical Precis — Structured Summary and Analysis',
  'Grade 11 English strand: a rhetorical precis is a highly structured four-sentence summary that identifies a texts main claim, its supporting method, its stated purpose and audience, and the rhetorical strategies the author uses to achieve that purpose.',
  [('What is a rhetorical precis?', ['A highly structured, condensed summary that analyzes both content and rhetorical strategy', 'A lengthy, unstructured retelling of an entire text', 'A purely emotional response to a text with no analysis', 'A list of grammar corrections for a text'], 0),
   ('What does the first sentence of a rhetorical precis typically identify?', ['The texts main claim and its author', 'The page number of the final paragraph', 'A list of unrelated vocabulary words', 'The publishers address'], 0),
   ('Besides summarizing content, what else does a rhetorical precis analyze?', ['The rhetorical strategies the author uses to achieve their purpose', 'The font size used in the original publication', 'The number of paragraphs in the text', 'The colour of the books cover'], 0),
   ('Why is a rhetorical precis useful for close reading?', ['It forces a reader to distinguish what a text says from how and why it says it', 'It eliminates the need to read the text closely at all', 'It focuses only on counting the number of sentences', 'It requires no analysis of the texts purpose'], 0),
   ('What element does a rhetorical precis typically identify about a texts audience?', ['The intended audience and the authors purpose in addressing them', 'The audiences favourite colour', 'The exact number of readers a text has had', 'Nothing regarding audience is ever considered'], 0)]),
F('Discrete Math: Eulers Formula for Planar Graphs',
  'Grade 11 Functions strand: for any connected planar graph, Eulers formula states that the number of vertices minus the number of edges plus the number of faces always equals 2, a relationship that connects graph theory to the structure of polyhedra.',
  [('What does Eulers formula state for a connected planar graph?', ['Vertices minus edges plus faces always equals 2', 'Vertices plus edges always equals faces', 'Edges minus vertices always equals 0', 'Faces always equal twice the number of vertices'], 0),
   ('What is a planar graph?', ['A graph that can be drawn on a plane with no edges crossing', 'A graph that must contain at least one cycle of crossing edges', 'A graph with no vertices at all', 'A graph that can only exist in three dimensions'], 0),
   ('What broader mathematical structures does Eulers formula connect graph theory to?', ['Polyhedra', 'Prime numbers', 'Trigonometric ratios', 'Probability distributions'], 0),
   ('If a connected planar graph has 5 vertices and 7 edges, how many faces does it have?', ['4', '2', '12', '3'], 0),
   ('Why must a graph be planar for the standard form of Eulers formula to apply directly?', ['The formula relies on counting faces formed by a crossing-free drawing in the plane', 'Planarity has no connection to how the formula is derived', 'The formula only applies to graphs with no edges', 'Non-planar graphs always have exactly two faces'], 0)]),
B('Biology: Photosynthetic Pigments and Paper Chromatography',
  'Grade 11 Biology strand: leaves contain multiple photosynthetic pigments, including chlorophyll a, chlorophyll b, and carotenoids, each absorbing different wavelengths of light, and paper chromatography separates these pigments by exploiting their differing solubility as they travel up a solvent-soaked strip.',
  [('Which of these is a photosynthetic pigment found in leaves?', ['Chlorophyll a', 'Hemoglobin', 'Insulin', 'Keratin'], 0),
   ('Why do leaves typically contain more than one type of photosynthetic pigment?', ['Different pigments absorb different wavelengths of light, broadening the range used for photosynthesis', 'Extra pigments have no functional purpose in photosynthesis', 'Multiple pigments exist only to change the colour of flowers', 'Leaves contain only a single pigment, never more than one'], 0),
   ('What does paper chromatography use to separate plant pigments?', ['Differing pigment solubility as they travel up a solvent-soaked strip', 'A high-powered microscope with no solvent involved', 'A process that destroys all pigments before separation', 'An electrical current passed directly through the leaf'], 0),
   ('Which pigment type often produces the yellow and orange colours seen in chromatography separations of leaf extract?', ['Carotenoids', 'Chlorophyll a exclusively', 'Melanin', 'Keratin'], 0),
   ('Why do different pigments end up at different positions on a chromatography strip?', ['They travel at different rates depending on their solubility in the solvent', 'All pigments always travel at exactly the same rate', 'Pigments are sorted by weight using a centrifuge instead', 'Position on the strip depends only on the pigments colour, not solubility'], 0)]),
C('Chemistry: Water Softening and Ion Exchange Resins',
  'Grade 11 Chemistry strand: water softening removes dissolved calcium and magnesium ions responsible for hard water using ion exchange resins, which swap these hardness ions for sodium or potassium ions bound to the resin, preventing mineral scale buildup and improving soap effectiveness.',
  [('What ions are primarily responsible for water hardness?', ['Calcium and magnesium ions', 'Sodium and chlorine ions', 'Hydrogen and oxygen ions', 'Potassium and fluorine ions'], 0),
   ('What does an ion exchange resin swap hardness ions for?', ['Sodium or potassium ions bound to the resin', 'Pure oxygen gas', 'Carbon dioxide molecules', 'Chlorine gas dissolved in the water'], 0),
   ('What problem does water softening help prevent?', ['Mineral scale buildup', 'An increase in water temperature', 'A decrease in water volume', 'The complete evaporation of water'], 0),
   ('How does softened water affect soap effectiveness compared to hard water?', ['Softened water allows soap to work more effectively', 'Softened water always prevents soap from forming any lather', 'Softened water has no effect on how soap performs', 'Softened water dissolves soap instantly before it can be used'], 0),
   ('What general process describes how an ion exchange resin removes hardness ions from water?', ['Hardness ions are exchanged for other ions already bound to the resin', 'Hardness ions are boiled away completely', 'Hardness ions are converted directly into pure water molecules', 'Hardness ions are filtered out using only a physical mesh screen'], 0)]),
]),
day(134, [
E('Grammar: Modal Verbs and Degrees of Certainty in Academic Writing',
  'Grade 11 English strand: modal verbs such as may, might, could, should, and must allow a writer to signal varying degrees of certainty, obligation, or possibility, a crucial tool for hedging claims precisely in academic and analytical writing.',
  [('What do modal verbs allow a writer to signal?', ['Varying degrees of certainty, obligation, or possibility', 'The exact tense of every verb in a sentence', 'The physical length of a sentence', 'The number of syllables in a word'], 0),
   ('Which of these is an example of a modal verb?', ['Might', 'Running', 'Quickly', 'Beautiful'], 0),
   ('Why are modal verbs especially useful in academic writing?', ['They let a writer hedge claims precisely rather than overstating certainty', 'They remove all nuance from a claim', 'They are grammatically forbidden in formal writing', 'They always make a claim sound more certain than it is'], 0),
   ('Which modal verb expresses the strongest degree of obligation or necessity?', ['Must', 'Might', 'Could', 'May'], 0),
   ('How does choosing might instead of will change the meaning of a claim?', ['It signals possibility rather than certainty', 'It has no effect on the meaning of the claim at all', 'It makes the claim more certain than will would', 'It removes the claim entirely from the sentence'], 0)]),
F('Number Theory: Linear Congruences and Modular Inverses',
  'Grade 11 Functions strand: a linear congruence has the form ax is congruent to b modulo m, and solving it often requires finding the modular inverse of a, a value that plays the same role modulo m that a reciprocal plays in ordinary arithmetic.',
  [('What is the general form of a linear congruence?', ['ax is congruent to b modulo m', 'ax equals b with no modulus involved', 'a plus x equals b times m', 'x squared is congruent to a modulo b'], 0),
   ('What is a modular inverse of a, with respect to modulus m?', ['A value that plays the same role as a reciprocal, but within modular arithmetic', 'A value that is always equal to zero', 'The negative of a with no other property', 'A value that always equals m itself'], 0),
   ('What earlier tool helps determine whether a modular inverse of a exists modulo m?', ['The Euclidean algorithm and the greatest common divisor of a and m', 'The Pythagorean Theorem', 'The quadratic formula', 'Basic long division with no reference to gcd'], 0),
   ('Under what condition does a have a modular inverse modulo m?', ['The greatest common divisor of a and m must equal 1', 'The value of a must always be negative', 'The modulus m must always be a prime number greater than 100', 'A modular inverse never exists under any condition'], 0),
   ('Why are modular inverses useful for solving linear congruences?', ['Multiplying both sides by the modular inverse isolates the variable, similar to dividing in ordinary arithmetic', 'They have no practical use in solving congruences', 'They only apply to equations with no variables', 'They eliminate the need for any modulus in the equation'], 0)]),
B('Biology: Chemoreception — Taste and Smell',
  'Grade 11 Biology strand: chemoreception is the sensory process by which specialized receptor cells detect dissolved or airborne chemical molecules, underlying both taste on the tongue and smell in the nasal cavity, and allowing organisms to identify food, danger, and chemical signals in their environment.',
  [('What is chemoreception?', ['The sensory process of detecting dissolved or airborne chemical molecules', 'The process of detecting light using the retina', 'The process of detecting sound waves using the ear', 'The process of detecting temperature changes in the skin only'], 0),
   ('Which two senses are both forms of chemoreception?', ['Taste and smell', 'Sight and hearing', 'Touch and balance', 'Hearing and balance'], 0),
   ('Where are taste receptor cells primarily located?', ['On the tongue', 'In the inner ear', 'In the retina of the eye', 'In the skin of the fingertips only'], 0),
   ('Where are smell receptor cells primarily located?', ['In the nasal cavity', 'On the surface of the tongue only', 'In the cochlea of the inner ear', 'In the lens of the eye'], 0),
   ('Why is chemoreception important for an organisms survival?', ['It helps identify food, danger, and chemical signals in the environment', 'It has no role in an organisms ability to survive', 'It only functions in plants, never in animals', 'It prevents any interaction with the surrounding environment'], 0)]),
C('Chemistry: Silicone Polymers and Their Properties',
  'Grade 11 Chemistry strand: silicone polymers are built from an alternating backbone of silicon and oxygen atoms rather than the carbon backbone typical of organic polymers, giving them notable heat resistance, flexibility, and stability across a wide range of temperatures.',
  [('What forms the backbone of a silicone polymer?', ['An alternating chain of silicon and oxygen atoms', 'A chain made entirely of carbon atoms', 'A chain made entirely of nitrogen atoms', 'A single metal atom with no chain at all'], 0),
   ('How does a silicone polymer backbone differ from that of a typical organic polymer?', ['It uses silicon and oxygen atoms rather than a carbon backbone', 'It contains no atoms other than hydrogen', 'It is always shorter than an organic polymer backbone', 'There is no difference between the two types of backbone'], 0),
   ('Which property is silicone particularly known for compared to many carbon-based polymers?', ['Heat resistance across a wide range of temperatures', 'Extreme reactivity with water at room temperature', 'Complete instability at any temperature', 'A tendency to dissolve instantly in air'], 0),
   ('Besides heat resistance, what other property is characteristic of silicone polymers?', ['Flexibility', 'Extreme brittleness with no flexibility', 'A strong tendency to conduct electricity like a metal', 'Radioactivity'], 0),
   ('Why might silicone be chosen over a typical organic polymer for a high-temperature application?', ['Its silicon-oxygen backbone remains stable at temperatures that would degrade many carbon-based polymers', 'Silicone always melts at a lower temperature than carbon-based polymers', 'Silicone has no practical advantage over organic polymers', 'Organic polymers are always more heat-resistant than silicone'], 0)]),
]),
day(135, [
E('Literature: The Roman-Fleuve — The Novel Sequence',
  'Grade 11 English strand: a roman-fleuve is a sequence of related, often self-contained novels that follow the same characters, family, or community across an extended timeline, allowing an author to trace change and continuity over a much larger scope than a single novel permits.',
  [('What is a roman-fleuve?', ['A sequence of related novels following the same characters or community over time', 'A single short poem with no narrative content', 'A type of formal legal contract', 'A novel written entirely in a single afternoon'], 0),
   ('What does the roman-fleuve form allow an author to trace that a single novel often cannot?', ['Change and continuity across a much larger timeline', 'Nothing, since a single novel can always do the same thing equally well', 'The exact word count of each chapter', 'A single characters actions within one afternoon only'], 0),
   ('What commonly links the separate novels within a roman-fleuve?', ['Recurring characters, a family, or a community followed across the sequence', 'Nothing at all connects the separate novels', 'Only a shared publisher, with no connection in content', 'A shared cover colour and nothing else'], 0),
   ('Why might a reader experience a roman-fleuve differently from a single stand-alone novel?', ['Themes and characters can develop and echo across multiple connected volumes', 'A roman-fleuve always contains fewer words than a single novel', 'Roman-fleuves never allow character development of any kind', 'Each volume of a roman-fleuve must ignore all previous volumes completely'], 0),
   ('What does the term roman-fleuve literally suggest about this form?', ['A novel that flows like a river across multiple connected volumes', 'A novel that ends abruptly with no continuation', 'A novel written only in verse', 'A novel with a single, extremely short chapter'], 0)]),
F('Statistics: The Chi-Square Test for Independence',
  'Grade 11 Functions strand: the chi-square test for independence compares observed frequencies in categorical data to the frequencies expected if two variables were unrelated, producing a statistic used to judge whether any observed association is likely genuine or due to chance.',
  [('What does the chi-square test for independence compare?', ['Observed frequencies to the frequencies expected if two variables were unrelated', 'The mean and median of a single numeric data set', 'Two unrelated sets of continuous measurements only', 'The standard deviation of two samples'], 0),
   ('What type of data is the chi-square test for independence designed to analyze?', ['Categorical data', 'Only data measured in kilograms', 'Only data collected over exactly one year', 'Only data with a normal distribution'], 0),
   ('What does a large chi-square statistic suggest about the two variables being tested?', ['The observed association is less likely to be due to chance alone', 'The two variables are definitely completely unrelated', 'The sample size was too small to calculate any statistic', 'No conclusion can ever be drawn from the statistic'], 0),
   ('What earlier statistical concept does the chi-square test build on to judge significance?', ['Hypothesis testing', 'The Pythagorean Theorem', 'The binomial theorem', 'Vector projections'], 0),
   ('Why is the chi-square test for independence useful in analyzing survey or categorical data?', ['It provides a way to test whether two categorical variables are related rather than independent', 'It can only be used with data that has no categories at all', 'It removes the need for collecting any survey data', 'It only applies to a single categorical variable with no comparison'], 0)]),
B('Biology: Countercurrent Exchange Systems in Animals',
  'Grade 11 Biology strand: countercurrent exchange is a biological arrangement in which two fluids flow in opposite directions past each other, maintaining a concentration or temperature gradient along the entire length of the exchange surface and greatly increasing the efficiency of processes such as gas exchange in fish gills.',
  [('What is countercurrent exchange?', ['An arrangement where two fluids flow in opposite directions past each other to increase exchange efficiency', 'A system where two fluids always flow in the exact same direction', 'A process that stops all fluid flow completely', 'An arrangement used only for storing waste products'], 0),
   ('What does the opposite-direction flow in countercurrent exchange maintain?', ['A concentration or temperature gradient along the entire exchange surface', 'A gradient only at a single point, nowhere else', 'Complete equilibrium with no gradient at all', 'A gradient that reverses randomly with no consistent pattern'], 0),
   ('In which animal structure is countercurrent exchange well known for increasing oxygen uptake from water?', ['Fish gills', 'The mammalian stomach', 'The human liver', 'Bird feathers'], 0),
   ('Why is countercurrent exchange more efficient than a system where both fluids flow in the same direction?', ['A gradient is maintained along the whole exchange surface rather than only at the start', 'Same-direction flow always transfers more material overall', 'Countercurrent exchange eliminates the need for any gradient whatsoever', 'Efficiency has no relationship to the direction of fluid flow'], 0),
   ('Besides gas exchange, what other kind of exchange can a countercurrent system help conserve in some animals?', ['Heat, helping limbs conserve body temperature', 'Sound, helping animals communicate over long distances', 'Light, helping animals see in the dark', 'Electrical signals in the nervous system'], 0)]),
C('Chemistry: The Sol-Gel Process and Ceramic Materials',
  'Grade 11 Chemistry strand: the sol-gel process converts a liquid suspension of small particles, called a sol, into a solid, interconnected network, called a gel, allowing ceramic and glass materials to be synthesized at lower temperatures than traditional melting-based methods.',
  [('What does the sol-gel process convert a liquid suspension of particles into?', ['A solid, interconnected network called a gel', 'A pure gas with no solid material remaining', 'A liquid with no particles remaining at all', 'A crystal identical to table salt'], 0),
   ('What is a sol in the sol-gel process?', ['A liquid suspension of small particles', 'A fully hardened solid material', 'A gas released during the reaction', 'A type of strong acid used only for cleaning'], 0),
   ('What advantage does the sol-gel process offer over traditional melting-based ceramic synthesis?', ['It allows materials to be synthesized at lower temperatures', 'It requires significantly higher temperatures than melting methods', 'It eliminates the need for any starting material', 'It can only be used to produce liquids, never solids'], 0),
   ('What general category of materials is commonly produced using the sol-gel process?', ['Ceramic and glass materials', 'Pure metals with no ceramic content', 'Organic polymers exclusively', 'Radioactive isotopes'], 0),
   ('What structural change occurs to the particles as a sol transforms into a gel?', ['They link together into a solid, interconnected network', 'They separate completely and disperse into a gas', 'They dissolve entirely and disappear from the mixture', 'They shrink to a size too small to detect'], 0)]),
]),
day(136, [
E('Media Literacy: Astroturfing and Manufactured Grassroots Campaigns',
  'Grade 11 English strand: astroturfing is a media manipulation tactic in which an organized, well-funded campaign is deliberately disguised as spontaneous grassroots public opinion, requiring readers to question who benefits from a message before accepting it as authentic.',
  [('What is astroturfing?', ['An organized campaign disguised as spontaneous grassroots public opinion', 'A genuine, entirely spontaneous grassroots movement with no organization', 'A formal government policy announcement', 'A type of academic citation style'], 0),
   ('What does astroturfing conceal from the public?', ['The organized, often well-funded source behind a supposedly grassroots message', 'Nothing, since astroturfing campaigns are always fully transparent', 'The weather forecast for the following week', 'The publication date of a news article'], 0),
   ('Why should readers ask who benefits from a message before trusting it?', ['Because a hidden sponsor may be manufacturing the appearance of public support', 'Because the identity of a messages sponsor is always irrelevant', 'Because all messages online are equally trustworthy by default', 'Because asking this question has no bearing on media literacy'], 0),
   ('Which of these would be a warning sign of astroturfing?', ['Many nearly identical posts appearing to come from unconnected ordinary people at once', 'A single, clearly labelled opinion piece with a named author', 'A government press release with an official letterhead', 'A peer-reviewed academic study with cited sources'], 0),
   ('How does astroturfing differ from a genuine grassroots movement?', ['A genuine movement arises organically from real individuals rather than being manufactured by a hidden sponsor', 'There is no meaningful difference between the two', 'A genuine grassroots movement is always funded by a hidden corporation', 'Astroturfing always involves fewer participants than a grassroots movement'], 0)]),
F('Financial Mathematics: The Rule of 72 and Estimating Exponential Growth',
  'Grade 11 Functions strand: the rule of 72 is a quick estimation technique that divides 72 by an annual interest rate to approximate the number of years needed for an investment to double, offering fast mental insight into exponential growth without a full logarithmic calculation.',
  [('What does the rule of 72 estimate?', ['The number of years needed for an investment to double in value', 'The exact interest rate of any loan', 'The total value of an investment after exactly one year', 'The number of payments in a mortgage'], 0),
   ('How is the rule of 72 applied to an annual interest rate?', ['Dividing 72 by the interest rate percentage', 'Multiplying 72 by the interest rate percentage', 'Subtracting the interest rate from 72', 'Adding 72 to the interest rate percentage'], 0),
   ('What advantage does the rule of 72 offer over a full logarithmic calculation?', ['It gives a fast mental estimate without needing to solve a logarithmic equation', 'It always gives a more precise answer than logarithms', 'It eliminates the need for any interest rate at all', 'It applies only to decreasing, not growing, quantities'], 0),
   ('Approximately how many years would it take an investment to double at an annual rate of 8 percent, using the rule of 72?', ['9 years', '72 years', '8 years', '36 years'], 0),
   ('What kind of growth does the rule of 72 approximate the doubling time for?', ['Exponential growth, such as compound interest', 'Purely linear growth with a constant addition each year', 'Growth that immediately stops after one year', 'Growth that decreases every year'], 0)]),
B('Biology: Autoimmune Disorders and Immune System Dysfunction',
  'Grade 11 Biology strand: an autoimmune disorder occurs when the immune system fails to distinguish the bodys own cells from foreign invaders and mistakenly attacks healthy tissue, leading to chronic inflammation and damage in the affected organs or systems.',
  [('What causes an autoimmune disorder?', ['The immune system fails to distinguish the bodys own cells from foreign invaders', 'A complete absence of any immune system activity', 'An excess of vitamin intake over a short period', 'A purely mechanical injury to a single organ'], 0),
   ('What happens to healthy tissue in an autoimmune disorder?', ['It is mistakenly attacked by the bodys own immune system', 'It is deliberately removed by a surgeon', 'It grows uncontrollably with no immune involvement', 'It becomes completely immune to any future disease'], 0),
   ('What is a common consequence of ongoing autoimmune attack on tissue?', ['Chronic inflammation and damage in the affected organs or systems', 'Immediate and complete regeneration of the affected tissue', 'A permanent increase in the bodys overall energy levels', 'Total immunity to all future infections'], 0),
   ('Which of these is an example of an autoimmune disorder?', ['Type 1 diabetes, where the immune system attacks insulin-producing cells', 'A broken bone caused by a fall', 'A common cold caused by a virus', 'A sunburn caused by UV exposure'], 0),
   ('Why are autoimmune disorders often difficult to treat?', ['Suppressing the immune response to protect healthy tissue can also reduce the bodys ability to fight infection', 'Autoimmune disorders have no known treatments being researched', 'Treating autoimmune disorders always cures them within a single day', 'The immune system plays no role in autoimmune disease treatment'], 0)]),
C('Chemistry: Fluoride Chemistry and Tooth Remineralization',
  'Grade 11 Chemistry strand: fluoride ions from toothpaste or drinking water can replace hydroxide ions in tooth enamels hydroxyapatite crystal structure, forming fluorapatite, a more acid-resistant mineral that helps remineralize weakened enamel and slow the progress of tooth decay.',
  [('What mineral makes up the crystal structure of tooth enamel?', ['Hydroxyapatite', 'Calcium carbonate exclusively', 'Sodium chloride', 'Silicon dioxide'], 0),
   ('What does fluoride form when it replaces hydroxide ions in tooth enamel?', ['Fluorapatite', 'Calcium fluoride gas', 'A completely different, unrelated mineral with no calcium', 'Pure elemental fluorine'], 0),
   ('Why is fluorapatite beneficial compared to the original enamel mineral?', ['It is more resistant to acid attack', 'It dissolves more easily in acidic conditions', 'It has no effect on enamel strength at all', 'It immediately weakens the tooth structure'], 0),
   ('What process does fluoride support that helps repair weakened tooth enamel?', ['Remineralization', 'Complete decalcification', 'Permanent enamel removal', 'Total tooth replacement'], 0),
   ('Where might a person be exposed to fluoride that protects their teeth?', ['Toothpaste or fluoridated drinking water', 'Only through sunlight exposure', 'Only through eating pure table salt', 'Only through breathing outdoor air'], 0)]),
]),
day(137, [
E('Writing: The Lyric Essay — Blending Poetry and Prose in Nonfiction',
  'Grade 11 English strand: a lyric essay is a hybrid nonfiction form that borrows the imagery, white space, and associative logic of poetry while retaining the essays grounding in reflection and factual material, often favouring fragmented structure over linear argument.',
  [('What is a lyric essay?', ['A hybrid nonfiction form that blends poetic technique with essayistic reflection', 'A strictly factual news report with no reflection', 'A form of formal legal writing', 'A type of multiple-choice test'], 0),
   ('Which poetic qualities does a lyric essay often borrow?', ['Imagery, white space, and associative logic', 'Strict legal terminology and citations', 'Mathematical formulas and equations', 'A rigid five-paragraph structure with no flexibility'], 0),
   ('How does a lyric essay typically differ from a traditional linear essay?', ['It often favours fragmented structure over a single continuous argument', 'It always follows a strict, unbroken chronological argument', 'It never includes any reflection or imagery', 'It is required to be exactly one paragraph long'], 0),
   ('What does a lyric essay retain from the essay tradition despite its poetic qualities?', ['A grounding in reflection and factual material', 'A complete absence of any factual content', 'A requirement to rhyme throughout', 'A strict prohibition on personal reflection'], 0),
   ('Why might associative logic suit the lyric essay form?', ['It allows ideas and images to connect by resonance rather than strict linear argument', 'Associative logic requires every idea to follow a strict numbered outline', 'It eliminates the need for any connection between ideas', 'Associative logic is forbidden in nonfiction writing'], 0)]),
F('Complex Numbers: Polar Form and Eulers Formula',
  'Grade 11 Functions strand: Eulers formula expresses a complex number in exponential form as e raised to i theta, connecting the polar form of a complex number to the exponential function and providing a compact way to represent magnitude and angle together.',
  [('What does Eulers formula express a complex number in terms of?', ['An exponential function involving the imaginary unit and an angle', 'A simple linear equation with no imaginary component', 'Only real numbers, with no reference to angles', 'A polynomial with no complex terms'], 0),
   ('What two pieces of information does the exponential form of a complex number represent together?', ['Magnitude and angle', 'Only the real part, with no imaginary part', 'The degree of a polynomial and its roots', 'The slope and y-intercept of a line'], 0),
   ('What earlier form of a complex number is directly connected to the exponential form through Eulers formula?', ['Polar form', 'Standard form of a linear equation', 'Vertex form of a parabola', 'Slope-intercept form'], 0),
   ('Why is exponential form often convenient for multiplying complex numbers?', ['Multiplying exponential forms simply adds the angles and multiplies the magnitudes', 'Exponential form makes multiplication of complex numbers impossible', 'Exponential form only allows addition, never multiplication', 'Multiplying in exponential form requires converting to a matrix first'], 0),
   ('What does the angle theta represent in the exponential form of a complex number?', ['The direction of the complex number measured from the positive real axis', 'The magnitude of the complex number only', 'The real part of the complex number only', 'A value that has no geometric meaning'], 0)]),
B('Biology: Detritivores and Decomposer Food Webs',
  'Grade 11 Biology strand: detritivores are organisms that consume dead organic matter directly, breaking it into smaller fragments that decomposer microorganisms then chemically break down further, together recycling nutrients back into an ecosystem and supporting the base of many food webs.',
  [('What do detritivores consume?', ['Dead organic matter', 'Only living prey that they actively hunt', 'Sunlight, through a process similar to photosynthesis', 'Only inorganic minerals from rock'], 0),
   ('What role do detritivores play alongside decomposer microorganisms?', ['Breaking dead matter into smaller fragments that microorganisms can further break down', 'Preventing microorganisms from accessing dead matter entirely', 'Producing oxygen through photosynthesis', 'Hunting decomposer microorganisms as prey'], 0),
   ('Which of these is an example of a detritivore?', ['An earthworm', 'A hawk hunting live prey', 'A rose bush', 'A photosynthetic alga'], 0),
   ('What is the ecological benefit of detritivores and decomposers working together?', ['Recycling nutrients back into the ecosystem', 'Permanently removing all nutrients from an ecosystem', 'Preventing any plant growth in an area', 'Eliminating the need for any producers in a food web'], 0),
   ('How do detritivores differ from decomposer microorganisms in how they process dead matter?', ['Detritivores physically consume and fragment matter, while decomposers chemically break it down further', 'Detritivores and decomposers process matter in an identical way with no differences', 'Only decomposers can physically move through an ecosystem', 'Detritivores use photosynthesis while decomposers do not'], 0)]),
C('Chemistry: Hemoglobin — Iron Coordination and Oxygen Transport',
  'Grade 11 Chemistry strand: hemoglobin contains an iron ion held within a porphyrin ring through coordinate covalent bonds, and this iron coordination centre reversibly binds a single oxygen molecule, allowing hemoglobin to pick up oxygen in the lungs and release it in the bodys tissues.',
  [('What metal ion is held within hemoglobins porphyrin ring?', ['Iron', 'Calcium', 'Sodium', 'Copper'], 0),
   ('What type of bonds hold the iron ion within the porphyrin ring in hemoglobin?', ['Coordinate covalent bonds', 'Ionic bonds only', 'Metallic bonds only', 'Hydrogen bonds only'], 0),
   ('What does the iron coordination centre in hemoglobin reversibly bind?', ['A single oxygen molecule', 'A single carbon atom permanently', 'A glucose molecule', 'A sodium ion'], 0),
   ('Why must the binding of oxygen to hemoglobins iron centre be reversible?', ['Oxygen needs to be released again once it reaches the bodys tissues', 'Oxygen should remain permanently bound and never released', 'Reversibility has no importance for hemoglobins function', 'Hemoglobin only binds oxygen once during its entire lifetime'], 0),
   ('Where does hemoglobin typically pick up oxygen, according to its transport role?', ['In the lungs', 'In the stomach', 'In the kidneys', 'In the skin'], 0)]),
]),
day(138, [
E('Literature: The Doppelganger Motif in Fiction',
  'Grade 11 English strand: a doppelganger is a double or mirror-self figure who resembles the protagonist, often externalizing a hidden or repressed side of that characters identity and creating tension between the self a character presents and the self they conceal.',
  [('What is a doppelganger in fiction?', ['A double or mirror-self figure who closely resembles the protagonist', 'A minor character who appears only once with no significance', 'A narrator who exists outside the story entirely', 'A type of formal poem with a fixed rhyme scheme'], 0),
   ('What does a doppelganger often externalize within a narrative?', ['A hidden or repressed side of the protagonists identity', 'A characters grocery list', 'The authors biography', 'A completely unrelated subplot with no thematic connection'], 0),
   ('What kind of tension does a doppelganger figure often create?', ['Tension between the self a character presents and the self they conceal', 'Tension between two unrelated minor characters only', 'No tension at all, since doppelgangers are purely decorative', 'Tension over which city a story takes place in'], 0),
   ('Why might an author introduce a doppelganger rather than simply describing a characters inner conflict?', ['Embodying the conflict in a separate character makes an internal struggle visible and dramatic', 'Doppelgangers remove all conflict from a narrative entirely', 'Describing inner conflict directly is always forbidden in fiction', 'A doppelganger has no relationship to a characters inner life'], 0),
   ('Which of these best describes the effect of a doppelganger on a story?', ['It unsettles the reader by suggesting a hidden, opposing version of a familiar character', 'It reassures the reader that no character has any hidden depth', 'It has no emotional or thematic effect on the reader', 'It simplifies the story by removing the need for character development'], 0)]),
F('Discrete Math: Graph Isomorphism — Comparing Graph Structures',
  'Grade 11 Functions strand: two graphs are isomorphic if their vertices can be matched up so that connections between corresponding vertices are perfectly preserved, meaning the graphs have identical structure even if they are drawn or labelled differently.',
  [('What does it mean for two graphs to be isomorphic?', ['Their vertices can be matched so that connections are perfectly preserved between them', 'They must have a completely different number of vertices', 'They can never be drawn using the same number of edges', 'One graph must always be a subset of the other with fewer vertices'], 0),
   ('What can differ between two isomorphic graphs even though their structure is identical?', ['How they are drawn or labelled', 'The number of edges each graph contains', 'The number of vertices each graph contains', 'Whether the graphs are connected at all'], 0),
   ('What must be true of corresponding vertices in two isomorphic graphs?', ['They must have the same degree and connection pattern', 'They must have completely different degrees', 'They must be labelled with the same letters in both graphs', 'They must be positioned at identical coordinates on the page'], 0),
   ('Why is checking vertex degree sequences a useful first step in testing for graph isomorphism?', ['Graphs with different degree sequences cannot possibly be isomorphic', 'Degree sequences have no relationship to graph isomorphism', 'Matching degree sequences alone always proves two graphs are isomorphic', 'Degree sequences can only be calculated for planar graphs'], 0),
   ('Why is determining graph isomorphism sometimes computationally difficult for large graphs?', ['The number of possible vertex matchings to check can grow extremely quickly with graph size', 'Large graphs never have more than one possible vertex matching', 'Graph isomorphism becomes trivial once a graph has more than ten vertices', 'Computational difficulty has no connection to the number of vertices'], 0)]),
B('Biology: The Renin-Angiotensin System and Blood Pressure Regulation',
  'Grade 11 Biology strand: the renin-angiotensin system is a hormonal pathway in which the kidneys release renin in response to low blood pressure, triggering a cascade that produces angiotensin II, a potent hormone that raises blood pressure by constricting blood vessels and promoting sodium and water retention.',
  [('What organ releases renin in response to low blood pressure?', ['The kidneys', 'The liver', 'The pancreas', 'The lungs'], 0),
   ('What hormone does the renin-angiotensin cascade ultimately produce to raise blood pressure?', ['Angiotensin II', 'Insulin', 'Adrenaline exclusively', 'Melatonin'], 0),
   ('How does angiotensin II raise blood pressure?', ['By constricting blood vessels and promoting sodium and water retention', 'By dilating blood vessels and increasing water loss', 'By stopping the heart from beating temporarily', 'By reducing the total volume of blood in the body'], 0),
   ('What condition triggers the kidneys to release renin?', ['Low blood pressure', 'High blood pressure that is already elevated', 'A sudden increase in body temperature', 'A decrease in heart rate only'], 0),
   ('Why is the renin-angiotensin system considered a hormonal feedback pathway?', ['A drop in blood pressure triggers a hormone cascade that acts to restore blood pressure toward normal', 'It operates with no connection between blood pressure and hormone release', 'It only responds to changes in blood sugar, not blood pressure', 'It permanently raises blood pressure with no regulatory feedback'], 0)]),
C('Chemistry: Freezing Point Depression and Road Deicing',
  'Grade 11 Chemistry strand: dissolving a solute such as road salt in water lowers the freezing point of the resulting solution, a colligative property called freezing point depression, allowing icy roads treated with salt to remain liquid at temperatures below waters normal freezing point.',
  [('What is freezing point depression?', ['The lowering of a solutions freezing point caused by a dissolved solute', 'The raising of a solutions freezing point caused by a dissolved solute', 'A process that has no relationship to dissolved solutes', 'The boiling of a solution at a lower temperature than pure water'], 0),
   ('What type of property is freezing point depression, based on the number of dissolved particles rather than their identity?', ['A colligative property', 'A nuclear property', 'A property unrelated to solutions', 'An exclusively organic chemistry property'], 0),
   ('Why does salting an icy road help melt the ice?', ['It lowers the freezing point of the water so it can remain liquid below zero degrees Celsius', 'It raises the freezing point so water freezes more easily', 'Salt has no chemical effect on the freezing point of water', 'Salt instantly evaporates any ice on contact'], 0),
   ('What common solute is spread on roads to achieve freezing point depression?', ['Road salt', 'Pure sugar', 'Liquid nitrogen', 'Baking soda exclusively'], 0),
   ('What happens to a solutions freezing point as more solute particles are dissolved in it?', ['The freezing point continues to decrease', 'The freezing point always increases instead', 'The freezing point remains completely unchanged', 'The solution stops freezing under any condition'], 0)]),
]),
day(139, [
E('Oral Communication: Handling Audience Questions and Extemporaneous Response',
  'Grade 11 English strand: responding effectively to unplanned audience questions after a presentation requires active listening, brief clarifying restatement, and organized extemporaneous speaking that stays composed and on topic without the benefit of a prepared script.',
  [('What does handling audience questions well require beyond a prepared script?', ['Active listening and organized extemporaneous speaking', 'Reading directly from a script with no deviation', 'Ignoring the audience entirely', 'Refusing to answer any unplanned question'], 0),
   ('Why might a speaker briefly restate a question before answering it?', ['To confirm understanding and give themselves a moment to organize a response', 'To avoid answering the question at all', 'Restating a question always confuses the audience further', 'It is a required legal formality with no practical purpose'], 0),
   ('What is extemporaneous speaking?', ['Speaking that is organized and delivered without a fully scripted text', 'Speaking that is read word-for-word from a prepared script', 'Speaking that avoids any organization whatsoever', 'A form of speaking used only in written essays'], 0),
   ('Why is staying composed important when answering an unexpected or challenging question?', ['It helps the speaker respond thoughtfully rather than defensively', 'Composure has no effect on how an answer is received', 'Staying composed guarantees the question will not be asked again', 'Only written responses benefit from composure, not spoken ones'], 0),
   ('What skill helps a speaker understand exactly what an audience member is really asking?', ['Active listening', 'Speaking louder than the audience member', 'Ignoring the audience members tone entirely', 'Answering before the question is fully asked'], 0)]),
F('Number Theory: An Introduction to Continued Fractions',
  'Grade 11 Functions strand: a continued fraction expresses a number as a whole number plus a fraction whose denominator is itself a whole number plus another fraction, a nested structure that can represent both rational numbers exactly and irrational numbers through an infinite pattern.',
  [('What structure does a continued fraction use to express a number?', ['A nested sequence of whole numbers plus fractions within fractions', 'A single, unbroken decimal with no fractions', 'A list of unrelated prime numbers', 'A single whole number with no fractional part at all'], 0),
   ('Can a continued fraction represent a rational number exactly?', ['Yes, a rational number corresponds to a finite continued fraction', 'No, continued fractions can only represent irrational numbers', 'No, continued fractions cannot represent any number exactly', 'Only negative rational numbers can be represented this way'], 0),
   ('How does a continued fraction typically represent an irrational number?', ['Through an infinite, non-terminating nested pattern', 'Through a single terminating fraction only', 'Irrational numbers cannot be approximated by continued fractions at all', 'Through a whole number with no fractional part'], 0),
   ('What earlier algorithm is closely connected to computing continued fraction expansions?', ['The Euclidean algorithm', 'The quadratic formula', 'Synthetic division', 'The binomial theorem'], 0),
   ('Why might continued fractions be useful for finding good rational approximations of irrational numbers?', ['Truncating the nested pattern early produces increasingly accurate rational approximations', 'Continued fractions always produce worse approximations than simple decimals', 'They can only be used with whole numbers, never approximations', 'Truncating a continued fraction always produces the exact irrational value'], 0)]),
B('Biology: Genomic Imprinting and Parent-of-Origin Gene Expression',
  'Grade 11 Biology strand: genomic imprinting is an epigenetic phenomenon in which certain genes are expressed differently depending on whether they were inherited from the mother or the father, with one parental copy chemically silenced while the other remains active.',
  [('What is genomic imprinting?', ['An epigenetic phenomenon where certain genes are expressed differently depending on parental origin', 'A permanent mutation in the DNA sequence of a gene', 'A process that always silences every gene equally regardless of origin', 'A form of asexual reproduction with no parental contribution'], 0),
   ('In genomic imprinting, what happens to one of the two parental gene copies?', ['It is chemically silenced while the other copy remains active', 'It is physically deleted from the chromosome', 'Both copies are always expressed equally with no silencing', 'It is duplicated many times over'], 0),
   ('What determines which parental copy of an imprinted gene is silenced?', ['Whether the gene copy was inherited from the mother or the father', 'The colour of the offsprings eyes', 'The order in which the gene was discovered by scientists', 'The physical size of the chromosome carrying the gene'], 0),
   ('Is genomic imprinting a change to the underlying DNA sequence itself?', ['No, it is an epigenetic modification rather than a change to the DNA sequence', 'Yes, it always permanently alters the DNA sequence', 'Yes, it deletes the gene from the genome entirely', 'It replaces the DNA sequence with RNA permanently'], 0),
   ('Why does genomic imprinting complicate simple predictions based on Mendelian inheritance alone?', ['The parent of origin of a gene copy can affect whether it is expressed, not just which allele is inherited', 'Genomic imprinting has no effect on inheritance patterns at all', 'Mendelian inheritance already accounts fully for parent-of-origin effects', 'Imprinting only affects traits that are never inherited at all'], 0)]),
C('Chemistry: Shape-Memory Alloys and Solid-State Phase Transitions',
  'Grade 11 Chemistry strand: a shape-memory alloy such as nitinol can be deformed at a lower temperature and then return to its original engineered shape when heated, a behaviour driven by a reversible solid-state phase transition between two distinct crystal structures.',
  [('What is a shape-memory alloy?', ['A metal alloy that can return to its original shape when heated after being deformed', 'A metal alloy that permanently loses its shape once bent', 'A metal alloy with no ability to change shape at all', 'A non-metal material used only in electronics'], 0),
   ('What is nitinol an example of?', ['A shape-memory alloy', 'A pure element with no alloying', 'A type of ceramic material', 'A radioactive isotope'], 0),
   ('What drives the shape-recovering behaviour of a shape-memory alloy?', ['A reversible solid-state phase transition between two crystal structures', 'A chemical reaction that permanently destroys the metal', 'An external magnetic field with no relation to crystal structure', 'A process identical to simple thermal expansion in any metal'], 0),
   ('Under what condition is a shape-memory alloy typically deformed before it later recovers its shape?', ['At a lower temperature', 'Only while submerged in water', 'Only after being melted completely', 'At an extremely high temperature above its melting point'], 0),
   ('What happens to a deformed shape-memory alloy when it is heated?', ['It returns to its original engineered shape', 'It melts completely into a liquid', 'It becomes permanently more deformed', 'It shatters into small fragments'], 0)]),
]),
day(140, [
E('English Review: Ode, Utopia, Rhetoric, and Media Literacy',
  'Grade 11 English strand review: students revisit the ode, utopian fiction, the rhetorical precis, modal verbs and certainty, the roman-fleuve, astroturfing, the lyric essay, the doppelganger motif, and handling audience questions.',
  [('What does an ode typically do?', ['Directly addresses and celebrates a person, object, or abstract quality', 'Presents a purely factual news report with no emotional content', 'Avoids any direct address to its subject', 'Functions only as a legal or contractual document'], 0),
   ('What does utopian fiction typically imagine?', ['An idealized society organized around order, equality, or harmony', 'A society with no organization of any kind', 'A society identical in every way to the authors own', 'A purely historical account with no imagined elements'], 0),
   ('What do modal verbs allow a writer to signal?', ['Varying degrees of certainty, obligation, or possibility', 'The exact tense of every verb in a sentence', 'The physical length of a sentence', 'The number of syllables in a word'], 0),
   ('What is astroturfing?', ['An organized campaign disguised as spontaneous grassroots public opinion', 'A genuine, entirely spontaneous grassroots movement with no organization', 'A formal government policy announcement', 'A type of academic citation style'], 0),
   ('What is a doppelganger in fiction?', ['A double or mirror-self figure who closely resembles the protagonist', 'A minor character who appears only once with no significance', 'A narrator who exists outside the story entirely', 'A type of formal poem with a fixed rhyme scheme'], 0)]),
F('Functions Review: Calculus, Discrete Math, Number Theory, and Statistics',
  'Grade 11 Functions strand review: students revisit the power rule for derivatives, tangent line equations, Eulers formula for planar graphs, linear congruences, the chi-square test, the rule of 72, polar form and Eulers formula for complex numbers, graph isomorphism, and continued fractions.',
  [('What does the power rule provide?', ['A quick algebraic shortcut for differentiating polynomial terms', 'A method for factoring quadratic equations', 'A way to calculate the area under any curve exactly', 'A rule for simplifying fractions only'], 0),
   ('What does Eulers formula state for a connected planar graph?', ['Vertices minus edges plus faces always equals 2', 'Vertices plus edges always equals faces', 'Edges minus vertices always equals 0', 'Faces always equal twice the number of vertices'], 0),
   ('What does the chi-square test for independence compare?', ['Observed frequencies to the frequencies expected if two variables were unrelated', 'The mean and median of a single numeric data set', 'Two unrelated sets of continuous measurements only', 'The standard deviation of two samples'], 0),
   ('What does the rule of 72 estimate?', ['The number of years needed for an investment to double in value', 'The exact interest rate of any loan', 'The total value of an investment after exactly one year', 'The number of payments in a mortgage'], 0),
   ('What does it mean for two graphs to be isomorphic?', ['Their vertices can be matched so that connections are perfectly preserved between them', 'They must have a completely different number of vertices', 'They can never be drawn using the same number of edges', 'One graph must always be a subset of the other with fewer vertices'], 0)]),
B('Biology Review: Genetics, Physiology, and Ecology',
  'Grade 11 Biology strand review: students revisit epistasis, vestigial structures, photosynthetic pigments, chemoreception, countercurrent exchange, autoimmune disorders, detritivores, the renin-angiotensin system, and genomic imprinting.',
  [('What is epistasis?', ['When the expression of one gene is masked or modified by a different, non-allelic gene', 'A process where a single gene has no effect on phenotype at all', 'A type of cell division unrelated to genetics', 'A disease caused only by environmental factors'], 0),
   ('What are vestigial structures?', ['Anatomical features that have lost most or all of their original function over evolutionary history', 'Structures that appear only in embryos and never in adults of any species', 'New structures that have never existed in any ancestor', 'Structures found only in single-celled organisms'], 0),
   ('What is chemoreception?', ['The sensory process of detecting dissolved or airborne chemical molecules', 'The process of detecting light using the retina', 'The process of detecting sound waves using the ear', 'The process of detecting temperature changes in the skin only'], 0),
   ('What causes an autoimmune disorder?', ['The immune system fails to distinguish the bodys own cells from foreign invaders', 'A complete absence of any immune system activity', 'An excess of vitamin intake over a short period', 'A purely mechanical injury to a single organ'], 0),
   ('What is genomic imprinting?', ['An epigenetic phenomenon where certain genes are expressed differently depending on parental origin', 'A permanent mutation in the DNA sequence of a gene', 'A process that always silences every gene equally regardless of origin', 'A form of asexual reproduction with no parental contribution'], 0)]),
C('Chemistry Review: Isomerism, Materials Chemistry, and Applied Reactions',
  'Grade 11 Chemistry strand review: students revisit isomerism in coordination compounds, saponification, water softening, silicone polymers, the sol-gel process, fluoride chemistry, hemoglobin, freezing point depression, and shape-memory alloys.',
  [('What is geometric isomerism in a coordination compound?', ['Ligands occupying different spatial arrangements around the central metal ion', 'A change in the total number of electrons in the compound', 'A difference in the mass of the central metal ion', 'A reaction that produces an entirely different chemical formula'], 0),
   ('What is saponification?', ['The hydrolysis reaction of a fat or oil with a strong base to form soap', 'A reaction that converts soap back into a fat or oil', 'A purely physical process with no chemical reaction involved', 'A reaction that only occurs between two acids'], 0),
   ('What ions are primarily responsible for water hardness?', ['Calcium and magnesium ions', 'Sodium and chlorine ions', 'Hydrogen and oxygen ions', 'Potassium and fluorine ions'], 0),
   ('What forms the backbone of a silicone polymer?', ['An alternating chain of silicon and oxygen atoms', 'A chain made entirely of carbon atoms', 'A chain made entirely of nitrogen atoms', 'A single metal atom with no chain at all'], 0),
   ('What metal ion is held within hemoglobins porphyrin ring?', ['Iron', 'Calcium', 'Sodium', 'Copper'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_131_140)
    append_to(11, g11_131_140)
