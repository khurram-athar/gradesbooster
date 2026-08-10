#!/usr/bin/env python3
"""Grade 11, Days 151-160 -- extends Grade 11 from 150 to 160 days. Topics
chosen after dumping the existing Day 1-150 title list (data/grade11.json)
in full and cross-checking against it to avoid any overlap. Many initially
drafted topics turned out to already exist in the Day 1-150 corpus (this
Grade 11 course is unusually dense), so the final topic list below was
re-selected and re-verified against the full title dump before being
written into quizzes: the aubade, the picaresque novel, correlative
conjunctions, the soliloquy, satirical news and the line between parody
and misinformation, nonverbal communication and body language, the cover
letter, sound devices (alliteration, assonance, onomatopoeia), and
foreshadowing and dramatic irony; related rates, concavity and inflection
points, implicit differentiation, cryptography and the RSA algorithm, the
traveling salesman problem, the t-distribution, tax brackets and marginal
versus average tax rate, the scalar triple product, and calculus-based
optimization; wetland ecosystems, restriction enzymes and recombinant DNA,
gel electrophoresis and DNA fingerprinting, phylogenetics and cladograms,
C3/C4/CAM photosynthetic pathways, DNA repair mechanisms, the menstrual
cycle and hormonal regulation, twin studies and the nature-nurture debate,
and allometric scaling of metabolic rate; electronegativity and bond
polarity, azo dyes and colour chemistry, vapor pressure and Raoults law,
bleach and oxidizing household cleaners, thiols and skunk spray,
amphoteric substances, rocket propellants and oxidizer chemistry, solvent
polarity (like dissolves like), and nonstick cookware and fluoropolymer
chemistry. Day 160 is a lighter cross-subject review day, matching the
structure of the Day 140 and Day 150 review days (one review lesson per
subject, each reusing five first-questions verbatim from the batch, drawn
from Days 151, 153, 155, 157, and 159).

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


def _rebalance_answer_positions(days, seed=20260809):
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


g11_151_160 = [
day(151, [
E('Poetry: The Aubade — the Dawn Song of Parting Lovers',
  'Grade 11 English strand: an aubade is a poem set at dawn that mourns the coming separation of lovers as night ends, using the arrival of morning light as a symbol of loss, urgency, and the fragile boundary between private intimacy and the return of the ordinary world.',
  [('What does an aubade typically mourn?', ['The coming separation of lovers as dawn arrives', 'A victory in battle celebrated at noon', 'The death of a monarch decades earlier', 'A harvest festival held in autumn'], 0),
   ('What symbol does an aubade often use to represent loss and urgency?', ['The arrival of morning light', 'A river flowing backward', 'A locked door with no key', 'A blank page with no writing'], 0),
   ('What boundary does an aubade often explore?', ['The boundary between private intimacy and the return of the ordinary world', 'The boundary between two rival nations', 'The boundary between prose and legal writing', 'The boundary between painting and sculpture'], 0),
   ('Why might a poet set an aubade specifically at dawn rather than at night?', ['Dawn marks the moment lovers must part, giving the poem its central tension', 'Dawn has no symbolic meaning in poetry of any kind', 'Nighttime scenes are forbidden in the aubade form', 'Dawn removes all urgency from a poems subject'], 0),
   ('What emotional tone is most associated with the aubade form?', ['A bittersweet sense of loss as a shared night comes to an end', 'A tone of complete indifference to the passage of time', 'A purely comic tone with no emotional weight', 'A tone of triumphant celebration with no sense of loss'], 0)]),
F('Calculus: Related Rates Problems',
  'Grade 11 Functions strand: a related rates problem uses the chain rule to connect the rates of change of two or more quantities that are linked by an equation, letting you find how fast one quantity is changing at a given instant from the known rate of change of another.',
  [('What technique do related rates problems rely on to connect changing quantities?', ['The chain rule', 'The quadratic formula', 'The Pythagorean Theorem alone with no calculus', 'A method that ignores any equation linking the quantities'], 0),
   ('What must two or more quantities in a related rates problem share?', ['An equation that links them together', 'No relationship of any kind', 'Identical numerical values at every instant', 'A shared unit of measurement and nothing else'], 0),
   ('What can a related rates problem let you find once one rate is known?', ['How fast a linked quantity is changing at a given instant', 'The exact value of a completely unrelated constant', 'The total distance traveled over an entire day', 'The colour of the object being measured'], 0),
   ('Why is differentiating both sides of an equation with respect to time useful in a related rates problem?', ['It reveals how the rates of change of the linked quantities are related to each other', 'It removes all variables from the equation entirely', 'It changes the equation into an unrelated geometric formula', 'Differentiating with respect to time has no effect on the equation'], 0),
   ('Which of these is a classic example of a related rates problem?', ['Finding how fast the radius of a balloon changes as it is inflated at a known rate', 'Finding the average of a list of unrelated numbers', 'Finding the exact colour of a balloon', 'Finding the total surface area of a fixed, unchanging cube'], 0)]),
B('Ecology: Wetland Ecosystems and Ecosystem Services',
  'Grade 11 Biology strand: wetlands are ecosystems saturated with water for at least part of the year, and they provide critical ecosystem services such as filtering pollutants, storing floodwater, and supporting high levels of biodiversity, making them among the most productive habitats on Earth.',
  [('What defines a wetland ecosystem?', ['An ecosystem saturated with water for at least part of the year', 'An ecosystem that never contains any water at all', 'An ecosystem found only at extremely high altitudes', 'An ecosystem defined solely by its average temperature'], 0),
   ('Name one ecosystem service wetlands provide.', ['Filtering pollutants from water', 'Producing large amounts of desert sand', 'Preventing all plant growth in the area', 'Eliminating biodiversity from the surrounding region'], 0),
   ('How do wetlands help reduce flood damage?', ['By storing floodwater and slowing its release', 'By immediately releasing all stored water at once', 'By having no effect on water flow whatsoever', 'By evaporating all rainfall before it can accumulate'], 0),
   ('Why are wetlands considered among the most productive habitats on Earth?', ['They support unusually high levels of biodiversity relative to their area', 'They support no living organisms of any kind', 'They are always larger in area than any other habitat type', 'Productivity has no relationship to biodiversity in a wetland'], 0),
   ('What might happen to nearby communities if a wetland is drained or destroyed?', ['Increased flood risk and reduced natural water filtration', 'Guaranteed protection from all future flooding', 'No change of any kind to surrounding water systems', 'An automatic improvement in local water quality'], 0)]),
C('Chemistry: Electronegativity and Bond Polarity',
  'Grade 11 Chemistry strand: electronegativity measures how strongly an atom attracts shared electrons in a covalent bond, and a large difference in electronegativity between two bonded atoms produces a polar bond with partial positive and negative charges, while a small difference produces a nonpolar bond.',
  [('What does electronegativity measure?', ['How strongly an atom attracts shared electrons in a covalent bond', 'The total mass of an atoms nucleus', 'The exact number of neutrons in an atom', 'The colour an element appears in visible light'], 0),
   ('What forms when there is a large electronegativity difference between two bonded atoms?', ['A polar bond with partial positive and negative charges', 'A bond with no charge distribution of any kind', 'A purely metallic bond with free-flowing electrons', 'A bond that instantly breaks apart'], 0),
   ('What kind of bond forms when two bonded atoms have similar electronegativity?', ['A nonpolar bond', 'An extremely polar ionic bond', 'A bond with no shared electrons at all', 'A bond that cannot exist under any conditions'], 0),
   ('What do the partial charges in a polar bond represent?', ['An uneven sharing of electron density between the two atoms', 'A complete transfer of an entire electron from one atom to the other', 'An equal sharing of electron density with no imbalance', 'A charge that has no connection to electron distribution'], 0),
   ('Why is electronegativity difference useful for predicting a bonds character?', ['It indicates whether electrons are shared evenly or pulled toward one atom', 'It has no relationship to how electrons are shared in a bond', 'It only applies to bonds between identical atoms', 'It determines the physical colour of a compound exclusively'], 0)]),
]),
day(152, [
E('Literature: The Picaresque Novel and the Roguish Protagonist',
  'Grade 11 English strand: a picaresque novel follows a resourceful, low-born rogue protagonist through a loosely connected series of episodic adventures, using satire and social observation to expose the corruption or hypocrisy of the society the protagonist travels through.',
  [('What kind of protagonist does a picaresque novel typically follow?', ['A resourceful, low-born rogue', 'A wealthy monarch with no flaws', 'A narrator who never appears in the story', 'A committee of unnamed characters acting as one'], 0),
   ('How are the events of a picaresque novel typically structured?', ['As a loosely connected series of episodic adventures', 'As a single, tightly unified plot with no separate episodes', 'As a strict legal argument with numbered clauses', 'As a single unbroken scene with no passage of time'], 0),
   ('What does a picaresque novel often use its roguish protagonist to expose?', ['The corruption or hypocrisy of the surrounding society', 'The exact population of the protagonists home village', 'A purely private matter with no social relevance', 'The protagonists complete and total innocence in every situation'], 0),
   ('What literary technique does a picaresque novel commonly rely on to critique society?', ['Satire and social observation', 'Strict legal citation', 'Mathematical proof', 'Silence, with no commentary of any kind'], 0),
   ('Why might a low-born rogue make an effective narrator for social critique?', ['Their outsider status lets them move through and comment on many levels of society', 'Low-born characters are forbidden from narrating any story', 'An outsider status prevents any commentary on society', 'Only wealthy narrators are capable of social critique'], 0)]),
F('Calculus: Concavity, Inflection Points, and the Second Derivative',
  'Grade 11 Functions strand: the second derivative of a function reveals its concavity, with a positive second derivative indicating the graph curves upward and a negative second derivative indicating it curves downward, and an inflection point marks where concavity switches from one to the other.',
  [('What does the second derivative of a function reveal?', ['Its concavity', 'The exact y-intercept of the function', 'The total number of terms in the function', 'The colour of the functions graph'], 0),
   ('What does a positive second derivative indicate about a graph?', ['The graph curves upward', 'The graph curves downward', 'The graph is a perfectly straight line', 'The graph has no defined shape at all'], 0),
   ('What does a negative second derivative indicate about a graph?', ['The graph curves downward', 'The graph curves upward', 'The graph repeats itself infinitely', 'The graph has no second derivative at all'], 0),
   ('What is an inflection point?', ['A point where concavity switches from upward to downward or downward to upward', 'A point where the function is undefined in every case', 'The single highest point on the entire graph', 'A point where the graph crosses the y-axis exclusively'], 0),
   ('Why is concavity useful information beyond just knowing where a function increases or decreases?', ['It describes how the rate of change itself is changing, revealing the shape of the curve', 'Concavity provides no additional information about a functions shape', 'Concavity only applies to functions with no derivative', 'Concavity replaces the need to know where a function increases or decreases'], 0)]),
B('Biology: Restriction Enzymes and Recombinant DNA Technology',
  'Grade 11 Biology strand: restriction enzymes cut DNA at specific recognition sequences, allowing scientists to splice a gene of interest into a plasmid vector and insert the resulting recombinant DNA into a host cell, a foundational technique behind much of modern genetic engineering.',
  [('What do restriction enzymes do to DNA?', ['Cut it at specific recognition sequences', 'Permanently destroy all DNA they contact', 'Convert DNA directly into a protein with no intermediate steps', 'Have no effect on DNA of any kind'], 0),
   ('What is a plasmid vector used for in recombinant DNA technology?', ['Carrying a gene of interest into a host cell', 'Destroying a host cells entire genome', 'Measuring the exact temperature of a reaction', 'Producing energy for the host cell exclusively'], 0),
   ('What is recombinant DNA?', ['DNA formed by combining genetic material from different sources', 'DNA that has never been altered in any way', 'A type of DNA found only in viruses', 'DNA with no genetic information of any kind'], 0),
   ('Why are restriction enzymes considered a foundational tool of genetic engineering?', ['They allow precise cutting and splicing of DNA at known sequences', 'They have no practical application in genetic engineering', 'They can only be used to destroy DNA, never to modify it usefully', 'They function identically to antibodies in the immune system'], 0),
   ('What must happen to a gene of interest before it can be inserted into a host cell using this technique?', ['It must be spliced into a vector such as a plasmid', 'It must first be converted into a completely different gene', 'It must be removed from all cellular contexts permanently', 'Nothing, since genes can be inserted with no preparation at all'], 0)]),
C('Chemistry: Dyes and Pigments — Azo Compounds and Colour Chemistry',
  'Grade 11 Chemistry strand: azo compounds contain a nitrogen-nitrogen double bond linking two aromatic rings, and this extended conjugated system absorbs specific wavelengths of visible light, making azo compounds one of the most widely used classes of synthetic dye in textiles and food colouring.',
  [('What functional group defines an azo compound?', ['A nitrogen-nitrogen double bond linking two aromatic rings', 'A single carbon-hydrogen bond with no nitrogen present', 'A pure metal-metal bond', 'A bond found only in noble gases'], 0),
   ('What structural feature of azo compounds allows them to absorb visible light?', ['Their extended conjugated system', 'Their complete lack of any bonding electrons', 'A rigid, non-conjugated single bond structure', 'Their extremely small overall molecular size'], 0),
   ('What common application are azo compounds widely used for?', ['Synthetic dyes in textiles and food colouring', 'Building structural steel beams', 'Producing pure oxygen gas', 'Insulating electrical wiring'], 0),
   ('Why does the conjugated system in an azo dye affect the colour observed?', ['It determines which wavelengths of visible light are absorbed', 'Conjugation has no relationship to colour in any compound', 'It converts the compound into a colourless gas', 'It only affects the compounds melting point, never its colour'], 0),
   ('What links the two aromatic rings in a typical azo compound?', ['A nitrogen-nitrogen double bond', 'A single oxygen atom with no other bonds', 'A chain of carbon atoms with no nitrogen at all', 'A metallic bridge between the two rings'], 0)]),
]),
day(153, [
E('Grammar: Correlative Conjunctions and Balanced Sentence Structure',
  'Grade 11 English strand: correlative conjunctions such as either-or, neither-nor, and not only-but also work in pairs to link balanced grammatical elements, and keeping the paired elements parallel in structure gives a sentence rhythm and clarity that a single conjunction cannot achieve alone.',
  [('What is distinctive about correlative conjunctions?', ['They work in pairs to link balanced grammatical elements', 'They can only be used at the very start of a paragraph', 'They never appear more than once in an entire essay', 'They eliminate the need for any punctuation whatsoever'], 0),
   ('Give an example of a correlative conjunction pair.', ['Either and or', 'Quickly and slowly', 'Red and blue', 'Before and after, used only as prepositions'], 0),
   ('What must the elements joined by a correlative conjunction pair maintain?', ['Parallel grammatical structure', 'Completely different grammatical structures', 'No grammatical relationship at all', 'Identical spelling in every joined word'], 0),
   ('What effect can correctly balanced correlative conjunctions have on a sentence?', ['They give the sentence rhythm and clarity', 'They always make a sentence harder to understand', 'They remove all meaning from a sentence', 'They are grammatically forbidden in formal writing'], 0),
   ('What might happen if the two elements joined by a correlative conjunction pair are not grammatically parallel?', ['The sentence can sound awkward or unbalanced', 'The sentence automatically becomes more sophisticated', 'Nothing changes, since parallel structure is never required', 'The sentence becomes impossible to punctuate'], 0)]),
F('Calculus: Implicit Differentiation',
  'Grade 11 Functions strand: implicit differentiation finds the derivative of a relation in which y is not isolated on one side of the equation, by differentiating both sides with respect to x and applying the chain rule whenever a term involving y appears.',
  [('When is implicit differentiation needed?', ['When y is not isolated on one side of an equation', 'Only when a function has no variables at all', 'Only when an equation contains no y term whatsoever', 'When a function is already fully solved for y'], 0),
   ('What rule must be applied whenever a term involving y is differentiated with respect to x?', ['The chain rule', 'The Pythagorean Theorem', 'A rule that applies only to constants', 'No rule is needed when differentiating a term involving y'], 0),
   ('What does implicit differentiation ultimately find?', ['The derivative of a relation between x and y', 'The exact numerical value of x only', 'The area enclosed by a curve', 'The colour of a graphed curve'], 0),
   ('Why cannot every equation involving x and y be solved for y before differentiating?', ['Some relations cannot be rearranged into a simple function of x alone', 'Every equation can always be solved for y with no difficulty', 'Solving for y is never possible under any circumstance', 'Implicit differentiation is only used when y does not exist'], 0),
   ('What is a classic example of a curve that requires implicit differentiation?', ['A circle defined by x squared plus y squared equals a constant', 'A single point plotted with no equation at all', 'A straight horizontal line with a constant y-value', 'A function with no y term present anywhere'], 0)]),
B('Biology: Gel Electrophoresis and DNA Fingerprinting',
  'Grade 11 Biology strand: gel electrophoresis separates DNA fragments by size as an electric current pulls negatively charged DNA through a porous gel, with smaller fragments migrating farther, producing a banding pattern unique enough to individuals to be used in DNA fingerprinting.',
  [('What property of DNA fragments does gel electrophoresis separate by?', ['Size', 'Colour', 'Exact age of the sample', 'Taste'], 0),
   ('What pulls DNA fragments through the gel during electrophoresis?', ['An electric current', 'A strong magnetic field with no electric current', 'Gravity alone, with no external force applied', 'A stream of pressurized air'], 0),
   ('Which fragments migrate farther through the gel, smaller or larger ones?', ['Smaller fragments', 'Larger fragments', 'Both migrate an identical distance in every case', 'Neither size of fragment ever migrates at all'], 0),
   ('What does gel electrophoresis produce that can be used to identify an individual?', ['A unique banding pattern', 'A single unchanging colour with no pattern', 'An audible sound unique to each sample', 'A permanent chemical bond between all samples tested'], 0),
   ('Why is DNA able to migrate through a gel under an electric current?', ['DNA is negatively charged and moves toward the positive electrode', 'DNA carries no charge and is pushed by air pressure instead', 'DNA is positively charged and repelled by both electrodes', 'DNA has no ability to move under an electric current'], 0)]),
C('Chemistry: Vapor Pressure and Raoults Law',
  'Grade 11 Chemistry strand: vapor pressure is the pressure exerted by a substances vapour when it is in equilibrium with its liquid phase, and Raoults law describes how adding a nonvolatile solute lowers a solvents vapor pressure in proportion to the solutes concentration in the mixture.',
  [('What is vapor pressure?', ['The pressure exerted by a substances vapour in equilibrium with its liquid phase', 'The total pressure of an entire closed room', 'The pressure exerted only by a solid at absolute zero', 'A pressure that exists only in outer space'], 0),
   ('What does adding a nonvolatile solute do to a solvents vapor pressure?', ['It lowers the vapor pressure', 'It raises the vapor pressure dramatically', 'It has no effect on vapor pressure whatsoever', 'It converts the solvent into a solid instantly'], 0),
   ('What does Raoults law relate the drop in vapor pressure to?', ['The concentration of the dissolved solute', 'The colour of the solvent only', 'The exact temperature of the room in every case', 'The container material used to hold the solution'], 0),
   ('Why does a nonvolatile solute lower a solvents vapor pressure?', ['Solute particles occupy space at the surface, reducing the rate at which solvent molecules escape', 'Solute particles increase the rate at which solvent molecules escape', 'Nonvolatile solutes always evaporate faster than the solvent itself', 'Solute particles have no effect on the solvents surface at all'], 0),
   ('What phase equilibrium is vapor pressure defined in terms of?', ['Equilibrium between a substances liquid and vapour phases', 'Equilibrium between two completely different elements', 'Equilibrium between a solid and a plasma phase', 'A condition that involves no phase equilibrium at all'], 0)]),
]),
day(154, [
E('Drama: The Soliloquy and Interior Thought on Stage',
  'Grade 11 English strand: a soliloquy is a dramatic speech in which a character alone on stage speaks their private thoughts aloud, giving the audience direct access to motives, doubts, or plans that other characters in the play cannot hear.',
  [('What is a soliloquy?', ['A dramatic speech in which a character alone on stage speaks private thoughts aloud', 'A conversation between two characters with no audience present', 'A stage direction printed only in the margins of a script', 'A song performed by an entire chorus of characters'], 0),
   ('Who can hear the words of a true soliloquy within the world of the play?', ['No other character, only the audience', 'Every character on stage at that moment', 'Only the playwright, never the audience', 'A single silent character standing offstage'], 0),
   ('What does a soliloquy give the audience direct access to?', ['A characters motives, doubts, or plans', 'The exact date the play was first performed', 'A list of props used later in the play', 'The names of every actor in the cast'], 0),
   ('Why might a playwright use a soliloquy rather than dialogue to reveal a characters plan?', ['It lets the audience understand private thoughts no other character could realistically hear', 'Soliloquies are required to contain no meaningful information', 'Dialogue is always a more private form of speech than a soliloquy', 'A soliloquy must always be spoken by more than one character'], 0),
   ('What must be true of a characters position on stage for a speech to count as a soliloquy?', ['The character must be alone, with no other characters present to hear', 'The character must be surrounded by the entire cast', 'The character must be offstage and unseen by the audience', 'The character must be reading directly from a printed script'], 0)]),
F('Discrete Math: An Introduction to Cryptography and the RSA Algorithm',
  'Grade 11 Functions strand: the RSA algorithm encrypts messages using a public key built from two large prime numbers, and decrypting the message requires a private key derived from those same primes, a security scheme whose strength rests on how difficult it is to factor the product of two large primes.',
  [('What is a public key in the RSA algorithm built from?', ['Two large prime numbers', 'A single even number chosen at random', 'A list of common English words', 'A fixed constant that never changes between users'], 0),
   ('What is required to decrypt an RSA-encrypted message?', ['A private key derived from the same two primes', 'Nothing at all, since RSA messages decrypt themselves automatically', 'Only the public key, with no private key needed', 'A key that has no mathematical relationship to the primes used'], 0),
   ('What mathematical difficulty does the security of RSA rest on?', ['The difficulty of factoring the product of two large primes', 'The ease of factoring any number instantly', 'The impossibility of multiplying two prime numbers together', 'A difficulty that has no connection to prime numbers at all'], 0),
   ('Why can the public key be shared openly while the private key must stay secret?', ['Only the private key, derived from the original primes, can reverse the encryption', 'Both keys are always identical, so secrecy makes no difference', 'The public key alone can reverse the encryption just as easily', 'Neither key needs to remain secret under any circumstance'], 0),
   ('What earlier number theory concepts does RSA encryption depend on?', ['Prime numbers and modular arithmetic', 'Only basic addition and subtraction', 'Geometric proofs involving triangles', 'Trigonometric identities exclusively'], 0)]),
B('Evolution: Phylogenetics and the Construction of Cladograms',
  'Grade 11 Biology strand: phylogenetics reconstructs the evolutionary relationships among species based on shared characteristics, and a cladogram is a branching diagram that represents these relationships, with each branch point marking a common ancestor shared by all species descending from it.',
  [('What does phylogenetics reconstruct?', ['The evolutionary relationships among species', 'The exact diet of a single individual organism', 'The precise geographic coordinates of a species habitat', 'A list of every mutation in a single genome'], 0),
   ('What is a cladogram?', ['A branching diagram representing evolutionary relationships among species', 'A table listing the average weight of several species', 'A photograph of a single fossil specimen', 'A map showing only modern political borders'], 0),
   ('What does each branch point on a cladogram represent?', ['A common ancestor shared by all descending species', 'A location where a species went permanently extinct', 'The exact birth date of an individual organism', 'A point with no biological significance at all'], 0),
   ('What kind of evidence is used to build a cladogram?', ['Shared characteristics among species', 'Only the colour of each species fur or scales', 'Random guesses with no supporting evidence', 'The alphabetical order of species names'], 0),
   ('Why might two species appear close together on a cladogram?', ['They share a more recent common ancestor than species placed farther apart', 'They live in the exact same city or town', 'They were both discovered in the same calendar year', 'Placement on a cladogram is entirely random'], 0)]),
C('Chemistry: Bleach and Oxidizing Household Cleaners',
  'Grade 11 Chemistry strand: household bleach works as an oxidizing agent, breaking apart the conjugated pigment molecules responsible for stains and killing microorganisms by disrupting proteins and cell membranes through the same oxidation reactions that give bleach its cleaning and disinfecting power.',
  [('What type of chemical agent is household bleach?', ['An oxidizing agent', 'A reducing agent with no oxidizing ability', 'A completely inert substance with no reactivity', 'A pure acid with no oxidizing properties'], 0),
   ('How does bleach remove stains at the molecular level?', ['By breaking apart the conjugated pigment molecules responsible for the stain colour', 'By adding new pigment molecules to the fabric', 'By physically scrubbing the stain away with no chemical reaction', 'By dissolving the fabric itself completely'], 0),
   ('How does bleach act as a disinfectant?', ['By disrupting proteins and cell membranes through oxidation', 'By providing nutrients that microorganisms need to thrive', 'By having no effect on microorganisms whatsoever', 'By freezing microorganisms at room temperature'], 0),
   ('What single type of reaction explains both bleachs stain removal and disinfecting action?', ['Oxidation reactions', 'Simple physical dissolution with no chemical change', 'Nuclear fission reactions', 'Photosynthesis reactions'], 0),
   ('Why might mixing bleach with certain other cleaning products be dangerous?', ['Reactions between bleach and other chemicals can release hazardous gases', 'Mixing bleach with other cleaners always makes cleaning safer', 'Bleach cannot react with any other household chemical', 'Mixing chemicals always eliminates any safety risk'], 0)]),
]),
day(155, [
E('Media Literacy: Satirical News and the Line Between Parody and Misinformation',
  'Grade 11 English strand: satirical news outlets use exaggeration and irony to mock real events for comic or critical effect, but when a satirical headline is shared without its original context, readers may mistake parody for genuine reporting, raising questions about how a text signals its own satirical intent.',
  [('What technique do satirical news outlets rely on to mock real events?', ['Exaggeration and irony', 'Strict, unembellished factual reporting only', 'Complete silence on any current event', 'Random, unrelated numerical data'], 0),
   ('What can happen when a satirical headline is shared without its original context?', ['Readers may mistake the parody for genuine reporting', 'Readers always immediately recognize it as satire', 'The headline automatically becomes illegal to share', 'Nothing changes, since context never affects interpretation'], 0),
   ('What question does the spread of decontextualized satire raise for media literacy?', ['How a text signals its own satirical intent', 'Whether satire should be banned from all media entirely', 'Whether headlines should always be exactly one word long', 'Whether satire has ever existed as a literary form'], 0),
   ('Why might a satirical article be mistaken for real news?', ['Its exaggeration may not be obvious once removed from its original satirical source', 'Satirical articles always include a disclaimer in every possible context', 'Real news and satire are always printed in different fonts', 'Readers can never be confused by any form of media'], 0),
   ('What purpose does satirical news typically serve beyond humour?', ['Offering comic or critical commentary on real events', 'Providing only entertainment with no commentary of any kind', 'Replacing the need for factual news entirely', 'Avoiding any connection to real-world events'], 0)]),
F('Discrete Math: The Traveling Salesman Problem and Computational Complexity',
  'Grade 11 Functions strand: the traveling salesman problem asks for the shortest possible route that visits a set of cities exactly once and returns to the start, and the number of possible routes grows so quickly with each added city that finding a guaranteed optimal solution becomes computationally impractical for large sets.',
  [('What does the traveling salesman problem ask for?', ['The shortest possible route visiting a set of cities exactly once and returning to the start', 'The longest possible route that avoids every city entirely', 'A route that visits only a single city forever', 'The average distance between two randomly chosen cities'], 0),
   ('What happens to the number of possible routes as cities are added to the problem?', ['It grows extremely quickly', 'It stays exactly the same no matter how many cities are added', 'It decreases toward zero as cities are added', 'It becomes undefined once more than one city is included'], 0),
   ('Why does the traveling salesman problem become computationally impractical for large sets of cities?', ['Finding a guaranteed optimal solution requires checking an enormous number of possible routes', 'Large sets of cities always have exactly one possible route', 'Computers cannot process any information about cities at all', 'The problem becomes trivially easy once more cities are added'], 0),
   ('What field of study examines problems like the traveling salesman problem in terms of how quickly they can be solved?', ['Computational complexity', 'Ancient history', 'Musical theory', 'Botany'], 0),
   ('What must a valid solution route do with respect to each city?', ['Visit each city exactly once before returning to the start', 'Visit each city an unlimited number of times', 'Avoid visiting any city at all', 'Visit only cities with names starting with the same letter'], 0)]),
B('Plant Biology: C3, C4, and CAM Photosynthetic Pathways',
  'Grade 11 Biology strand: C3 plants fix carbon dioxide directly through the standard Calvin cycle, C4 plants first concentrate carbon dioxide in specialized cells to reduce losses in hot dry climates, and CAM plants open their stomata only at night to conserve water, each pathway representing an adaptation to different environmental pressures.',
  [('How do C3 plants fix carbon dioxide?', ['Directly through the standard Calvin cycle', 'By opening their stomata only at night', 'By avoiding the Calvin cycle entirely', 'By absorbing carbon dioxide through their roots only'], 0),
   ('Why do C4 plants first concentrate carbon dioxide in specialized cells?', ['To reduce losses in hot, dry climates', 'To increase water loss as much as possible', 'To prevent any photosynthesis from occurring', 'Concentrating carbon dioxide serves no functional purpose'], 0),
   ('When do CAM plants open their stomata?', ['Only at night', 'Only at the hottest point of midday', 'Continuously, at every hour of the day', 'Never, since CAM plants have no stomata'], 0),
   ('Why is opening stomata at night advantageous for a CAM plant?', ['It conserves water by reducing evaporation during the heat of the day', 'It maximizes water loss during the hottest part of the day', 'Nighttime stomata opening has no effect on water conservation', 'It prevents the plant from absorbing any carbon dioxide at all'], 0),
   ('What do the differences between C3, C4, and CAM pathways represent?', ['Adaptations to different environmental pressures', 'Random variations with no adaptive significance', 'Differences that only affect flower colour', 'A single identical pathway described in three different ways'], 0)]),
C('Chemistry: Thiols and the Chemistry of Skunk Spray',
  'Grade 11 Chemistry strand: thiols are organic compounds containing a sulfur-hydrogen functional group, and their sulfur atoms give many thiols an intensely unpleasant odour detectable by the human nose at extremely low concentrations, which is why the thiol-based compounds in skunk spray are so difficult to remove.',
  [('What functional group defines a thiol?', ['A sulfur-hydrogen group', 'A pure carbon-carbon triple bond', 'A nitrogen-oxygen double bond', 'A group containing only hydrogen and oxygen'], 0),
   ('What property of many thiols makes them so noticeable to the human nose?', ['An intensely unpleasant odour detectable at extremely low concentrations', 'A complete lack of any odour whatsoever', 'A pleasant, sweet fragrance detectable only at high concentrations', 'An odour that only animals, never humans, can detect'], 0),
   ('What element gives thiols their characteristic strong odour?', ['Sulfur', 'Sodium', 'Helium', 'Calcium'], 0),
   ('Why is skunk spray so difficult to eliminate once it contacts skin or fabric?', ['Its thiol-based compounds are detectable by smell at extremely low concentrations', 'Skunk spray contains no chemical compounds capable of producing an odour', 'Skunk spray evaporates completely within a few seconds', 'Thiols are always odourless once exposed to air'], 0),
   ('What type of compound, based on its functional group, is responsible for skunk spray odour?', ['A thiol', 'A noble gas', 'A pure metal', 'An ionic salt with no organic component'], 0)]),
]),
day(156, [
E('Oral Communication: Nonverbal Communication and Body Language in Presentations',
  'Grade 11 English strand: nonverbal communication, including posture, gesture, eye contact, and facial expression, shapes how an audience receives a spoken message just as much as the words themselves, and a speaker whose body language contradicts their words can undermine the credibility of an otherwise strong presentation.',
  [('Name one element of nonverbal communication in a presentation.', ['Eye contact', 'The exact word count of the speech', 'The font used on any accompanying slides', 'The publication date of the source material'], 0),
   ('How much can nonverbal communication shape an audiences reception of a message?', ['As much as the words themselves', 'Nonverbal communication has no effect on how a message is received', 'Only slightly less than the colour of the speakers shoes', 'Nonverbal communication can only ever weaken a message'], 0),
   ('What can happen if a speakers body language contradicts their spoken words?', ['It can undermine the credibility of the presentation', 'It always makes the presentation more persuasive', 'It has no effect on how the audience perceives the speaker', 'It automatically improves the audiences understanding'], 0),
   ('Why might a speaker practice maintaining eye contact during a presentation?', ['To build a stronger connection with and credibility with the audience', 'Eye contact always distracts an audience from the message', 'Maintaining eye contact is forbidden in formal presentations', 'Eye contact has no relationship to audience connection'], 0),
   ('What kind of signal does posture send to an audience during a speech?', ['A nonverbal signal about the speakers confidence and engagement', 'No signal of any kind, since posture is irrelevant to communication', 'A signal about the exact temperature of the room', 'A signal that only affects the speakers own hearing'], 0)]),
F('Statistics: The t-Distribution and Small-Sample Inference',
  'Grade 11 Functions strand: the t-distribution is used instead of the normal distribution when estimating a population mean from a small sample with unknown population standard deviation, since its wider, flatter shape accounts for the extra uncertainty that comes with a limited amount of data.',
  [('When is the t-distribution used instead of the normal distribution?', ['When estimating a population mean from a small sample with unknown population standard deviation', 'Only when the population standard deviation is known exactly', 'Only when the sample size is extremely large', 'Only when no data has been collected at all'], 0),
   ('How does the shape of the t-distribution compare to the normal distribution?', ['It is wider and flatter', 'It is narrower and taller', 'The two distributions are always identical in shape', 'The t-distribution has no defined shape at all'], 0),
   ('What does the wider, flatter shape of the t-distribution account for?', ['The extra uncertainty that comes with a limited amount of data', 'A complete absence of any uncertainty in the estimate', 'An error in how the sample was originally collected', 'A guarantee that the estimate is exactly correct'], 0),
   ('What must be unknown about the population for the t-distribution to be the appropriate choice?', ['The population standard deviation', 'The total population size only', 'The sample mean exclusively', 'Nothing about the population needs to be unknown'], 0),
   ('Why does a small sample size increase the uncertainty in an estimate of the population mean?', ['A small sample provides less information about the true population, widening the margin of error', 'A small sample always provides more information than a large sample', 'Sample size has no relationship to the uncertainty of an estimate', 'Small samples eliminate all uncertainty from an estimate'], 0)]),
B('Genetics: DNA Repair Mechanisms and Genomic Stability',
  'Grade 11 Biology strand: cells rely on a set of DNA repair mechanisms to detect and correct damage such as mismatched bases or broken strands, and failures in these repair pathways allow mutations to accumulate, which is why defective DNA repair genes are linked to a higher risk of cancer.',
  [('What do DNA repair mechanisms detect and correct?', ['Damage such as mismatched bases or broken strands', 'Only damage to the cell membrane, never to DNA itself', 'Errors in an organisms diet', 'Damage to bones and muscle tissue exclusively'], 0),
   ('What can happen to a cell when its DNA repair pathways fail?', ['Mutations accumulate', 'All mutations are instantly and permanently prevented', 'The cell becomes completely immune to any further change', 'DNA repair failure has no effect on the cell whatsoever'], 0),
   ('Why are defective DNA repair genes linked to a higher risk of cancer?', ['Failed repair allows mutations to accumulate unchecked', 'Defective repair genes always prevent cancer entirely', 'DNA repair genes have no connection to cancer risk', 'Cancer only develops when DNA repair works perfectly'], 0),
   ('What kind of damage might a DNA repair mechanism target?', ['A mismatched base pair', 'A change in the colour of the cell membrane', 'An increase in the cells overall size', 'A shift in the organisms body temperature'], 0),
   ('Why is genomic stability important for a cell?', ['It helps prevent the accumulation of mutations that can disrupt normal cell function', 'Genomic stability has no relevance to normal cell function', 'Genomic instability always improves a cells performance', 'Stability only matters for cells that never divide'], 0)]),
C('Chemistry: Amphoteric Substances — Acting as Both Acid and Base',
  'Grade 11 Chemistry strand: an amphoteric substance can act as either an acid or a base depending on what it reacts with, donating a proton to a stronger base or accepting a proton from a stronger acid, with water and aluminum hydroxide serving as classic examples of this dual behaviour.',
  [('What defines an amphoteric substance?', ['It can act as either an acid or a base depending on what it reacts with', 'It can only ever act as a strong acid', 'It can only ever act as a strong base', 'It has no acidic or basic properties of any kind'], 0),
   ('What does an amphoteric substance do when it reacts with a stronger base?', ['Donates a proton, acting as an acid', 'Accepts a proton, acting as a base', 'Refuses to react under any circumstance', 'Converts instantly into a noble gas'], 0),
   ('What does an amphoteric substance do when it reacts with a stronger acid?', ['Accepts a proton, acting as a base', 'Donates a proton, acting as an acid', 'Remains completely unreactive', 'Converts the acid into a solid precipitate immediately'], 0),
   ('Name a classic example of an amphoteric substance.', ['Water', 'A pure noble gas', 'A solid metal bar', 'A strand of DNA'], 0),
   ('Why is aluminum hydroxide considered amphoteric?', ['It can react as either an acid or a base depending on the conditions', 'It can only ever react as a base, never as an acid', 'It is completely unreactive under all conditions', 'It reacts only with other metals, never with acids or bases'], 0)]),
]),
day(157, [
E('Writing: The Cover Letter and Professional Correspondence',
  'Grade 11 English strand: a cover letter introduces a job or program applicant to a reader who has not yet seen their full application, using a concise, tailored argument to connect the applicants specific experience to the specific opportunity rather than repeating a resume in sentence form.',
  [('What is the purpose of a cover letter?', ['To introduce an applicant to a reader who has not yet seen their full application', 'To replace the need for a resume entirely', 'To provide a full transcript of academic grades', 'To list every job the applicant has ever held in exhaustive detail'], 0),
   ('What should a strong cover letter connect?', ['The applicants specific experience to the specific opportunity', 'The applicants unrelated hobbies to a random topic', 'Nothing in particular, since content does not matter', 'The reader to a completely unrelated organization'], 0),
   ('What mistake does an effective cover letter avoid?', ['Simply repeating the resume in sentence form', 'Mentioning the applicants relevant experience at all', 'Addressing the specific opportunity being applied for', 'Using complete sentences throughout the letter'], 0),
   ('Why should a cover letter be tailored to a specific opportunity rather than written generically?', ['A tailored letter shows the reader exactly why the applicant fits that particular role', 'Generic letters are always more persuasive than tailored ones', 'Tailoring a letter to a specific role is against professional convention', 'Cover letters are never read by the people who receive them'], 0),
   ('What tone is generally expected in professional correspondence like a cover letter?', ['Concise and professional', 'Casual and filled with slang', 'Aggressive and confrontational', 'Entirely humorous with no serious content'], 0)]),
F('Financial Mathematics: Tax Brackets and Marginal versus Average Tax Rate',
  'Grade 11 Functions strand: a progressive tax system applies increasing tax rates to successive brackets of income, so the marginal tax rate taxes only the portion of income within the highest bracket reached, while the average tax rate is the total tax paid divided by total income, and the two rates are rarely equal.',
  [('What does a progressive tax system apply to successive brackets of income?', ['Increasing tax rates', 'A single fixed tax rate with no brackets at all', 'Decreasing tax rates as income rises', 'No tax whatsoever, regardless of income'], 0),
   ('What does the marginal tax rate apply to?', ['Only the portion of income within the highest bracket reached', 'The entire income at a single flat rate', 'Only income earned before the age of eighteen', 'A rate that has no connection to income brackets'], 0),
   ('How is the average tax rate calculated?', ['Total tax paid divided by total income', 'Total income divided by the number of tax brackets', 'The highest marginal rate multiplied by two', 'The lowest possible tax bracket rate alone'], 0),
   ('Why are the marginal and average tax rates rarely equal in a progressive system?', ['Only the top portion of income is taxed at the marginal rate, while lower portions are taxed at lower rates', 'All portions of income are always taxed at the exact same rate', 'The average tax rate is always higher than the marginal rate', 'Marginal and average tax rates are mathematically identical by definition'], 0),
   ('What kind of tax system increases its rate as income rises?', ['A progressive tax system', 'A regressive tax system', 'A system with no defined structure at all', 'A system that only applies to corporations'], 0)]),
B('Human Biology: The Menstrual Cycle and Hormonal Regulation',
  'Grade 11 Biology strand: the menstrual cycle is regulated by a shifting balance of hormones, including estrogen, progesterone, and pituitary hormones that trigger ovulation, coordinating the buildup and shedding of the uterine lining across a roughly monthly cycle in preparation for a possible pregnancy.',
  [('What regulates the menstrual cycle?', ['A shifting balance of hormones', 'A fixed, unchanging hormone level with no variation', 'The digestive system exclusively', 'A process with no hormonal involvement at all'], 0),
   ('Name one hormone involved in regulating the menstrual cycle.', ['Estrogen', 'Insulin', 'Melatonin exclusively', 'Adrenaline exclusively'], 0),
   ('What pituitary-triggered event releases an egg during the menstrual cycle?', ['Ovulation', 'Fertilization, which always occurs automatically', 'Menstruation, occurring at the very start of the cycle', 'Implantation, which happens before ovulation'], 0),
   ('What happens to the uterine lining across the menstrual cycle?', ['It builds up and then sheds if pregnancy does not occur', 'It remains completely unchanged throughout the entire cycle', 'It is permanently removed after a single cycle', 'It builds up only once in a persons lifetime'], 0),
   ('What is the overall biological purpose of the hormonal changes across the menstrual cycle?', ['Preparing the body for a possible pregnancy', 'Regulating body temperature exclusively, with no reproductive role', 'Controlling the digestive system with no reproductive role', 'Producing energy for muscular movement exclusively'], 0)]),
C('Chemistry: Rocket Propellants and Oxidizer Chemistry',
  'Grade 11 Chemistry strand: a rocket propellant system pairs a fuel with an oxidizer that supplies the oxygen needed for combustion even in the vacuum of space, and the choice of fuel-oxidizer combination determines the thrust, efficiency, and storage challenges of a given rocket design.',
  [('What does an oxidizer supply in a rocket propellant system?', ['The oxygen needed for combustion', 'A source of pure nitrogen gas only', 'A structural support for the rocket body', 'A coolant with no chemical reactivity'], 0),
   ('Why must a rocket carry its own oxidizer rather than relying on the atmosphere?', ['Rockets must be able to combust fuel even in the vacuum of space', 'The atmosphere always provides more than enough oxygen for a rocket', 'Rockets never require oxygen for combustion at any stage', 'Oxidizers are only needed while a rocket remains on the ground'], 0),
   ('What determines the thrust and efficiency of a given rocket design?', ['The choice of fuel-oxidizer combination', 'The colour of the rockets exterior paint', 'The exact number of windows on the rocket', 'The name given to the rocket by its engineers'], 0),
   ('What two components make up a rocket propellant system?', ['A fuel and an oxidizer', 'Two identical fuels with no oxidizer present', 'A single inert gas with no fuel at all', 'A solid metal frame and a battery'], 0),
   ('Why can fuel-oxidizer combinations present storage challenges for rocket engineers?', ['Some oxidizers and fuels are highly reactive or require extreme storage conditions', 'Fuels and oxidizers never react with each other under any conditions', 'Storage of rocket propellants presents no challenges whatsoever', 'Oxidizers are always safe to store at any temperature'], 0)]),
]),
day(158, [
E('Poetry: Sound Devices — Alliteration, Assonance, and Onomatopoeia',
  'Grade 11 English strand: poets use sound devices such as alliteration, the repetition of initial consonant sounds, assonance, the repetition of vowel sounds within nearby words, and onomatopoeia, words that imitate the sounds they describe, to shape a poems rhythm and reinforce its meaning through how it sounds aloud.',
  [('What is alliteration?', ['The repetition of initial consonant sounds', 'The repetition of an entire sentence word for word', 'A rhyme scheme that never repeats any sound', 'A poem with no sound devices at all'], 0),
   ('What is assonance?', ['The repetition of vowel sounds within nearby words', 'The repetition of an identical rhyme at the end of every line', 'A device that only applies to punctuation', 'The complete absence of any vowel sounds in a poem'], 0),
   ('What is onomatopoeia?', ['Words that imitate the sounds they describe', 'Words with no sound-based meaning of any kind', 'A term for the physical layout of a poem on the page', 'A device used only in formal legal writing'], 0),
   ('Why might a poet use sound devices like alliteration and assonance?', ['To shape a poems rhythm and reinforce its meaning through sound', 'Sound devices always remove all meaning from a poem', 'To eliminate the need for any imagery in the poem', 'Sound devices are forbidden in poetry written in English'], 0),
   ('Which of these best defines onomatopoeia?', ['A word whose sound imitates the sound it describes', 'A word that rhymes with the line before it', 'A word borrowed directly from a foreign language', 'A word used only in scientific writing'], 0)]),
F('Calculus: Solving Optimization Problems with the Derivative',
  'Grade 11 Functions strand: solving an optimization problem with calculus involves writing a quantity to be maximized or minimized as a function of a single variable, then finding where its derivative equals zero to locate the critical points that produce the largest or smallest possible value.',
  [('What does an optimization problem ask you to find?', ['The maximum or minimum value of a quantity', 'The exact midpoint of an unrelated data set', 'The colour of a graphed function', 'The total number of terms in a polynomial'], 0),
   ('What must a quantity to be optimized be expressed as before calculus can be applied?', ['A function of a single variable', 'A list of unrelated constants', 'A fixed number with no variable at all', 'A geometric shape with no algebraic description'], 0),
   ('What condition identifies a critical point of a function?', ['The derivative equals zero', 'The function itself equals zero', 'The function is undefined everywhere', 'The second derivative is always negative'], 0),
   ('Why are critical points important in solving an optimization problem?', ['They locate the points where the function may reach a maximum or minimum value', 'Critical points have no relevance to maximum or minimum values', 'Critical points always indicate where a function is undefined', 'Critical points only exist for functions with no derivative'], 0),
   ('What is the first step in setting up a calculus-based optimization problem?', ['Writing the quantity to be maximized or minimized as a function of one variable', 'Immediately setting the second derivative equal to zero', 'Graphing the function using only technology, with no algebra', 'Ignoring the relationship between the variables involved'], 0)]),
B('Behavioural Genetics: Twin Studies and the Nature-Nurture Debate',
  'Grade 11 Biology strand: twin studies compare identical twins, who share nearly all their genes, to fraternal twins, who share about half, allowing researchers to estimate how much of a given trait is explained by genetics versus environment in the ongoing nature-nurture debate.',
  [('What do twin studies compare?', ['Identical twins to fraternal twins', 'Siblings born decades apart', 'Only children with no siblings at all', 'Twins raised on entirely different planets'], 0),
   ('About what proportion of genes do identical twins share?', ['Nearly all of their genes', 'None of their genes', 'Exactly one quarter of their genes', 'A proportion that changes randomly each year'], 0),
   ('About what proportion of genes do fraternal twins share?', ['About half', 'All of their genes', 'None of their genes', 'Exactly one tenth of their genes'], 0),
   ('What can researchers estimate using twin studies?', ['How much of a trait is explained by genetics versus environment', 'The exact birth weight of every twin ever studied', 'The precise number of twins born each year worldwide', 'Nothing meaningful about genetics or environment'], 0),
   ('What broader scientific debate do twin studies help inform?', ['The nature-nurture debate', 'A debate about the shape of the Earth', 'A debate about the age of the universe', 'A debate with no connection to genetics or environment'], 0)]),
C('Chemistry: Solvent Polarity — Like Dissolves Like',
  'Grade 11 Chemistry strand: the principle of like dissolves like predicts that polar solvents readily dissolve polar or ionic solutes while nonpolar solvents dissolve nonpolar solutes, because similar intermolecular forces between solvent and solute allow the solute particles to separate and become surrounded by solvent molecules.',
  [('What does the principle of like dissolves like predict?', ['Polar solvents dissolve polar solutes, and nonpolar solvents dissolve nonpolar solutes', 'All solvents dissolve all solutes equally well', 'Polar solvents can never dissolve any solute at all', 'Only nonpolar solvents are capable of dissolving anything'], 0),
   ('What type of solute do polar solvents readily dissolve?', ['Polar or ionic solutes', 'Only solutes with no charge distribution at all', 'Only solid metals with no polarity', 'Only solutes that are chemically identical to noble gases'], 0),
   ('Why does similarity in intermolecular forces between solvent and solute matter for dissolving?', ['It allows solute particles to separate and become surrounded by solvent molecules', 'Similar intermolecular forces always prevent any dissolving from occurring', 'Intermolecular forces have no connection to solubility', 'Dissolving only occurs when solvent and solute forces are completely opposite'], 0),
   ('Would a nonpolar solvent be expected to dissolve an ionic solute well?', ['No, because their intermolecular forces are too different', 'Yes, nonpolar solvents always dissolve ionic solutes easily', 'Yes, but only at extremely low temperatures', 'Solubility has no relationship to polarity in any case'], 0),
   ('What kind of solute would a nonpolar solvent be expected to dissolve effectively?', ['A nonpolar solute', 'A strongly ionic solute', 'A solute with no chemical structure at all', 'Only solutes that are also solvents themselves'], 0)]),
]),
day(159, [
E('Literature: Foreshadowing and Dramatic Irony',
  'Grade 11 English strand: foreshadowing plants early hints of events that will happen later in a narrative, while dramatic irony occurs when the audience knows something a character does not, and both techniques create suspense by shaping what a reader anticipates and how they interpret a characters choices.',
  [('What does foreshadowing do?', ['Plants early hints of events that will happen later in a narrative', 'Removes all sense of anticipation from a narrative', 'Reveals the entire ending in the very first sentence', 'Has no connection to later events in a story'], 0),
   ('What is dramatic irony?', ['When the audience knows something a character does not', 'When a character knows everything the audience does not', 'When neither the audience nor any character knows anything', 'A technique that only appears in comedic writing'], 0),
   ('What effect can foreshadowing and dramatic irony both create?', ['Suspense', 'Complete confusion with no narrative purpose', 'An immediate end to the story', 'A total absence of reader engagement'], 0),
   ('How does dramatic irony shape a readers interpretation of a characters choices?', ['It lets the reader judge those choices with knowledge the character lacks', 'It prevents the reader from forming any judgment at all', 'It ensures the reader always agrees completely with the character', 'It has no effect on how a reader interprets any choice'], 0),
   ('Why might an author plant a subtle early hint that only makes sense after a later event?', ['To reward attentive readers and add coherence to the narrative in hindsight', 'Subtle hints always confuse readers with no later payoff', 'Early hints are required to reveal the ending immediately', 'Foreshadowing removes the need for any later event to occur'], 0)]),
F('Geometry: The Scalar Triple Product and Volume of a Parallelepiped',
  'Grade 11 Functions strand: the scalar triple product combines three vectors by taking the dot product of one vector with the cross product of the other two, and its absolute value equals the volume of the parallelepiped formed by the three vectors as edges.',
  [('How is the scalar triple product of three vectors formed?', ['By taking the dot product of one vector with the cross product of the other two', 'By adding all three vectors together with no other operation', 'By taking the cross product of all three vectors at once', 'By dividing one vector by the sum of the other two'], 0),
   ('What geometric quantity does the absolute value of the scalar triple product equal?', ['The volume of the parallelepiped formed by the three vectors', 'The surface area of a sphere with the same radius', 'The perimeter of a triangle formed by the vectors', 'A quantity with no geometric meaning at all'], 0),
   ('How many vectors are combined in a scalar triple product?', ['Three', 'One', 'Two', 'Four'], 0),
   ('What type of quantity does a scalar triple product produce, a scalar or a vector?', ['A scalar', 'A vector with the same direction as the first input', 'A matrix of numbers', 'A vector perpendicular to all three inputs simultaneously'], 0),
   ('What shape is formed when three vectors are used as edges meeting at a common vertex?', ['A parallelepiped', 'A perfect sphere', 'A single straight line', 'A flat, two-dimensional triangle only'], 0)]),
B('Physiology: Metabolic Rate and Body Size — Allometric Scaling',
  'Grade 11 Biology strand: allometric scaling describes how an organisms metabolic rate does not increase in direct proportion to its body mass, since larger animals typically have a lower metabolic rate per unit of body mass than smaller animals, a relationship first described mathematically by Max Kleiber.',
  [('What does allometric scaling describe?', ['How an organisms metabolic rate relates to its body mass', 'The exact colour pattern of an animals fur', 'A relationship that applies only to plants, never animals', 'The number of offspring an animal produces annually'], 0),
   ('Does metabolic rate increase in direct proportion to body mass?', ['No, larger animals have a lower metabolic rate per unit of body mass', 'Yes, metabolic rate always increases in exact direct proportion to body mass', 'Body mass has no relationship to metabolic rate at all', 'Metabolic rate decreases to zero as body mass increases'], 0),
   ('Which tend to have a higher metabolic rate per unit of body mass, larger or smaller animals?', ['Smaller animals', 'Larger animals', 'Both have an identical metabolic rate per unit of mass', 'Neither, since metabolic rate is unrelated to body mass'], 0),
   ('Who is credited with first describing this metabolic scaling relationship mathematically?', ['Max Kleiber', 'Charles Darwin', 'Gregor Mendel', 'Isaac Newton'], 0),
   ('Why might a smaller animal need a proportionally higher metabolic rate than a larger animal?', ['Smaller animals lose heat more quickly relative to their body mass and must generate more energy to compensate', 'Smaller animals never need to generate any body heat', 'Body size has no effect on the rate of heat loss', 'Larger animals always lose heat more quickly than smaller ones'], 0)]),
C('Chemistry: Non-Stick Cookware and Fluoropolymer Chemistry',
  'Grade 11 Chemistry strand: nonstick cookware coatings rely on fluoropolymers, long carbon-chain molecules bonded to fluorine atoms whose strong carbon-fluorine bonds resist chemical reaction and create an extremely low-friction surface that food will not readily stick to or react with.',
  [('What class of material do nonstick cookware coatings rely on?', ['Fluoropolymers', 'Pure silver metal', 'Uncoated ceramic with no polymer content', 'A layer of table salt crystals'], 0),
   ('What element is bonded to the carbon chain in a fluoropolymer?', ['Fluorine', 'Helium', 'Sodium', 'Argon'], 0),
   ('Why do fluoropolymers resist chemical reaction?', ['Their carbon-fluorine bonds are very strong', 'They contain no chemical bonds of any kind', 'Their bonds break apart at room temperature', 'They react instantly with any substance they contact'], 0),
   ('What surface property makes a fluoropolymer coating useful for cookware?', ['An extremely low-friction surface that food will not readily stick to', 'An extremely rough, high-friction surface', 'A surface that dissolves completely when heated', 'A surface with no measurable properties at all'], 0),
   ('What kind of bond gives a fluoropolymer its chemical stability?', ['The carbon-fluorine bond', 'A weak hydrogen bond only', 'An unstable, easily broken ionic bond', 'A bond that exists only in theory'], 0)]),
]),
day(160, [
E('English Review: Poetic Craft, Narrative Devices, and Professional Writing',
  'Grade 11 English strand review: students revisit the aubade, the picaresque novel, correlative conjunctions, the soliloquy, satirical news and misinformation, nonverbal communication, the cover letter, sound devices, and foreshadowing and dramatic irony.',
  [('What does an aubade typically mourn?', ['The coming separation of lovers as dawn arrives', 'A victory in battle celebrated at noon', 'The death of a monarch decades earlier', 'A harvest festival held in autumn'], 0),
   ('What is distinctive about correlative conjunctions?', ['They work in pairs to link balanced grammatical elements', 'They can only be used at the very start of a paragraph', 'They never appear more than once in an entire essay', 'They eliminate the need for any punctuation whatsoever'], 0),
   ('What technique do satirical news outlets rely on to mock real events?', ['Exaggeration and irony', 'Strict, unembellished factual reporting only', 'Complete silence on any current event', 'Random, unrelated numerical data'], 0),
   ('What is the purpose of a cover letter?', ['To introduce an applicant to a reader who has not yet seen their full application', 'To replace the need for a resume entirely', 'To provide a full transcript of academic grades', 'To list every job the applicant has ever held in exhaustive detail'], 0),
   ('What does foreshadowing do?', ['Plants early hints of events that will happen later in a narrative', 'Removes all sense of anticipation from a narrative', 'Reveals the entire ending in the very first sentence', 'Has no connection to later events in a story'], 0)]),
F('Functions Review: Advanced Calculus, Cryptography, and Statistical Inference',
  'Grade 11 Functions strand review: students revisit related rates, concavity and inflection points, implicit differentiation, cryptography and the RSA algorithm, the traveling salesman problem, the t-distribution, tax brackets, the scalar triple product, and calculus-based optimization.',
  [('What technique do related rates problems rely on to connect changing quantities?', ['The chain rule', 'The quadratic formula', 'The Pythagorean Theorem alone with no calculus', 'A method that ignores any equation linking the quantities'], 0),
   ('When is implicit differentiation needed?', ['When y is not isolated on one side of an equation', 'Only when a function has no variables at all', 'Only when an equation contains no y term whatsoever', 'When a function is already fully solved for y'], 0),
   ('What does the traveling salesman problem ask for?', ['The shortest possible route visiting a set of cities exactly once and returning to the start', 'The longest possible route that avoids every city entirely', 'A route that visits only a single city forever', 'The average distance between two randomly chosen cities'], 0),
   ('What does a progressive tax system apply to successive brackets of income?', ['Increasing tax rates', 'A single fixed tax rate with no brackets at all', 'Decreasing tax rates as income rises', 'No tax whatsoever, regardless of income'], 0),
   ('How is the scalar triple product of three vectors formed?', ['By taking the dot product of one vector with the cross product of the other two', 'By adding all three vectors together with no other operation', 'By taking the cross product of all three vectors at once', 'By dividing one vector by the sum of the other two'], 0)]),
B('Biology Review: Biotechnology, Physiology, and Ecosystems',
  'Grade 11 Biology strand review: students revisit wetland ecosystems, restriction enzymes and recombinant DNA, gel electrophoresis, phylogenetics and cladograms, C3/C4/CAM photosynthesis, DNA repair mechanisms, the menstrual cycle, twin studies, and allometric scaling.',
  [('What defines a wetland ecosystem?', ['An ecosystem saturated with water for at least part of the year', 'An ecosystem that never contains any water at all', 'An ecosystem found only at extremely high altitudes', 'An ecosystem defined solely by its average temperature'], 0),
   ('What property of DNA fragments does gel electrophoresis separate by?', ['Size', 'Colour', 'Exact age of the sample', 'Taste'], 0),
   ('How do C3 plants fix carbon dioxide?', ['Directly through the standard Calvin cycle', 'By opening their stomata only at night', 'By avoiding the Calvin cycle entirely', 'By absorbing carbon dioxide through their roots only'], 0),
   ('What regulates the menstrual cycle?', ['A shifting balance of hormones', 'A fixed, unchanging hormone level with no variation', 'The digestive system exclusively', 'A process with no hormonal involvement at all'], 0),
   ('What does allometric scaling describe?', ['How an organisms metabolic rate relates to its body mass', 'The exact colour pattern of an animals fur', 'A relationship that applies only to plants, never animals', 'The number of offspring an animal produces annually'], 0)]),
C('Chemistry Review: Polarity, Household Chemistry, and Acid-Base Extensions',
  'Grade 11 Chemistry strand review: students revisit electronegativity and bond polarity, azo dyes, vapor pressure and Raoults law, bleach and oxidizing cleaners, thiols and skunk spray, amphoteric substances, rocket propellants, solvent polarity, and fluoropolymer chemistry.',
  [('What does electronegativity measure?', ['How strongly an atom attracts shared electrons in a covalent bond', 'The total mass of an atoms nucleus', 'The exact number of neutrons in an atom', 'The colour an element appears in visible light'], 0),
   ('What is vapor pressure?', ['The pressure exerted by a substances vapour in equilibrium with its liquid phase', 'The total pressure of an entire closed room', 'The pressure exerted only by a solid at absolute zero', 'A pressure that exists only in outer space'], 0),
   ('What functional group defines a thiol?', ['A sulfur-hydrogen group', 'A pure carbon-carbon triple bond', 'A nitrogen-oxygen double bond', 'A group containing only hydrogen and oxygen'], 0),
   ('What does an oxidizer supply in a rocket propellant system?', ['The oxygen needed for combustion', 'A source of pure nitrogen gas only', 'A structural support for the rocket body', 'A coolant with no chemical reactivity'], 0),
   ('What class of material do nonstick cookware coatings rely on?', ['Fluoropolymers', 'Pure silver metal', 'Uncoated ceramic with no polymer content', 'A layer of table salt crystals'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_151_160)
    append_to(11, g11_151_160)
