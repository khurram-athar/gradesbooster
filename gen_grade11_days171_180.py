#!/usr/bin/env python3
"""Grade 11, Days 171-180 -- extends Grade 11 from 170 to 180 days. Topics
chosen after dumping the existing Day 1-170 title list (data/grade11.json)
in full and cross-checking against it to avoid any overlap: free verse, the
road novel, the ellipsis, the letter to the editor, reading aloud and
recitation, the filter bubble and algorithmic echo chambers, the campus
novel, the limerick, and the restaurant review; derivatives of exponential
and logarithmic functions, big O notation, Wilsons theorem and primality
testing, the multinomial distribution, real versus nominal interest rates,
the intersection of a line and a plane, the Argand plane, antiderivatives
and an introduction to integration, and Latin squares; hemostasis and the
blood clotting cascade, punctuated equilibrium versus gradualism, the
pancreas, amphibian metamorphosis, predator-prey coevolution, antibiotic
mechanisms, genomic libraries and DNA cloning, human ecological footprint,
and sensory adaptation and habituation; Lewis structures and formal charge,
the contact process, the chemistry of glass, the chemistry of cement and
concrete, photovoltaic cells, chemical sensors, enzymes versus industrial
catalysts, the chemistry of rust, and osmotic pressure. Every one of these
topics was verified against the full Day 1-170 title dump and does not
repeat any earlier day.

Day 180 is a lighter cross-subject review day, matching the structure of
the Day 160 and Day 170 review days (one review lesson per subject, each
reusing five first-questions verbatim from the batch, drawn from Days 171,
173, 175, 177, and 179). The four Day 180 review titles -- English Review:
Free Verse, Ellipsis, Recitation, and Campus Fiction; Functions Review: Log
Derivatives, Number Theory, Finance, and Complex Numbers; Biology Review:
Hemostasis, Endocrine Physiology, Coevolution, and Biotechnology; Chemistry
Review: Bonding, Materials, Energy, and Catalysis -- were checked against
every earlier review-day title in Days 1-170 and are textually distinct
from all of them.

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


g11_171_180 = [
day(171, [
E('Poetry: Free Verse — Rhythm Without Meter or Rhyme',
  'Grade 11 English strand: free verse abandons a fixed meter and a regular rhyme scheme in favour of rhythms shaped by natural speech patterns, line breaks, and the internal logic of the poems images, giving a poet flexible control over pacing and emphasis without the constraints of a traditional form.',
  [('What does free verse abandon compared to traditional poetic forms?', ['A fixed meter and a regular rhyme scheme', 'All use of line breaks of any kind', 'Every reference to natural speech patterns', 'The ability to use imagery at all'], 0),
   ('What often shapes the rhythm of a free verse poem?', ['Natural speech patterns and line breaks', 'A strict syllable count applied to every line', 'A rhyme scheme repeated in every stanza', 'A metrical pattern borrowed from a sonnet'], 0),
   ('What control does free verse give a poet over a poem?', ['Flexible control over pacing and emphasis', 'No control whatsoever over how a poem is read', 'Control only over rhyme, never pacing', 'A rigid structure identical to blank verse'], 0),
   ('Why might a poet choose free verse rather than a fixed form such as the sonnet?', ['To let the poems structure grow from its content rather than fit a preset pattern', 'Free verse always produces a fixed number of lines identical to a sonnet', 'Free verse is required to rhyme in every line', 'A fixed form always allows more flexibility than free verse'], 0),
   ('What remains true of free verse even though it lacks a regular meter?', ['It can still use deliberate rhythm through line breaks and word choice', 'It contains no deliberate rhythm of any kind', 'It must always be written in complete prose sentences', 'It forbids the use of any imagery or figurative language'], 0)]),
F('Calculus: Derivatives of Exponential and Logarithmic Functions',
  'Grade 11 Functions strand: the derivative of the natural exponential function equals the function itself, while the derivative of the natural logarithm of x equals one divided by x, and these two results extend differentiation beyond polynomial functions into functions that model growth, decay, and many real-world processes.',
  [('What is notable about the derivative of the natural exponential function?', ['It equals the function itself', 'It always equals zero', 'It equals the square of the original function', 'It is undefined at every point'], 0),
   ('What is the derivative of the natural logarithm of x?', ['One divided by x', 'x itself', 'Zero for every value of x', 'The natural logarithm of x squared'], 0),
   ('What kinds of functions do exponential and logarithmic derivatives allow a student to analyze beyond polynomials?', ['Functions that model growth, decay, and many real-world processes', 'Only functions with a constant value at every point', 'Functions that have no real-world application of any kind', 'Only functions restricted to a single input value'], 0),
   ('Why is the derivative of the exponential function considered unusual compared to other derivative rules?', ['Differentiating it does not change its form at all', 'Differentiating it always produces a constant', 'Differentiating it removes the variable entirely', 'Differentiating it always produces a negative result'], 0),
   ('What real-world process might be modelled using the derivative of a logarithmic function?', ['The instantaneous rate of change of a quantity that grows logarithmically, such as sound intensity', 'A quantity that never changes over time', 'A quantity with no numerical value of any kind', 'A process that cannot be represented mathematically'], 0)]),
B('Biology: Hemostasis — The Blood Clotting Cascade',
  'Grade 11 Biology strand: hemostasis is the process that stops bleeding after an injury, beginning when platelets gather at a damaged vessel wall and release chemical signals that trigger a cascade of clotting factors, ultimately converting the soluble protein fibrinogen into a mesh of fibrin that stabilizes the clot.',
  [('What is hemostasis?', ['The process that stops bleeding after an injury', 'A process that causes bleeding to increase after an injury', 'A process with no connection to blood vessels at all', 'A process that only occurs in bone tissue'], 0),
   ('What do platelets do at the site of a damaged vessel wall?', ['They gather at the site and release chemical signals', 'They immediately dissolve and disappear', 'They convert directly into red blood cells', 'They have no role in the clotting process at all'], 0),
   ('What protein is converted into a stabilizing mesh during clot formation?', ['Fibrinogen, converted into fibrin', 'Hemoglobin, converted into oxygen', 'Insulin, converted into glucose', 'A protein with no role in clotting whatsoever'], 0),
   ('What triggers the cascade of clotting factors in hemostasis?', ['Chemical signals released by platelets at the injury site', 'A signal released only from bone marrow with no connection to injury', 'A random process unrelated to any injury', 'A cascade that begins only after a wound has fully healed'], 0),
   ('Why is a cascade, rather than a single step, useful for the clotting process?', ['It amplifies a small initial signal into a rapid, coordinated response at the injury site', 'A cascade always slows down the response to an injury', 'A single step would always be faster and more effective', 'Cascades prevent any clot from ever forming'], 0)]),
C('Chemistry: Lewis Structures and Formal Charge',
  'Grade 11 Chemistry strand: a Lewis structure represents the arrangement of valence electrons around bonded atoms using dots for lone pairs and lines for shared bonds, and calculating the formal charge on each atom helps chemists judge which of several possible Lewis structures is the most reasonable representation of a molecule.',
  [('What does a Lewis structure represent?', ['The arrangement of valence electrons around bonded atoms', 'The total mass of a molecule', 'The physical state of a substance at room temperature', 'A structure with no connection to electrons at all'], 0),
   ('What symbols are used to show shared bonds in a Lewis structure?', ['Lines', 'Only numbers, with no lines or dots used', 'Coloured shading with no symbols at all', 'Arrows pointing away from the molecule'], 0),
   ('What does calculating formal charge help a chemist judge?', ['Which of several possible Lewis structures is the most reasonable', 'The exact temperature at which a substance boils', 'The colour a substance will appear as a solid', 'The total number of atoms in an unrelated molecule'], 0),
   ('What do dots typically represent in a Lewis structure?', ['Lone pairs of valence electrons', 'The nucleus of an atom', 'A bond between two unrelated molecules', 'The total mass number of an atom'], 0),
   ('Why is comparing formal charges useful when more than one Lewis structure can be drawn for a molecule?', ['The structure with formal charges closest to zero and placed on the most electronegative atoms is usually favoured', 'Formal charge has no bearing on which structure is more likely', 'The structure with the largest formal charges is always correct', 'Only one Lewis structure can ever be drawn for any molecule'], 0)]),
]),
day(172, [
E('Literature: The Road Novel — Journey as Narrative Structure',
  'Grade 11 English strand: a road novel organizes its plot around a physical journey, using the changing landscape and the string of encounters along the way to reveal a characters inner transformation, so that movement through space becomes a structural device for tracking psychological or emotional change.',
  [('What does a road novel organize its plot around?', ['A physical journey', 'A single unchanging setting with no movement at all', 'A courtroom trial with no travel involved', 'A story told entirely through letters with no physical movement'], 0),
   ('What does the changing landscape in a road novel often help reveal?', ['A characters inner transformation', 'The exact population of every town visited', 'A characters complete indifference to change', 'A landscape with no connection to character development'], 0),
   ('What role do encounters along the way typically play in a road novel?', ['They accumulate to shape the protagonists development', 'They have no effect on the protagonist whatsoever', 'They are always identical to one another with no variation', 'They occur only after the journey has already ended'], 0),
   ('What does movement through space function as in a road novel?', ['A structural device for tracking psychological or emotional change', 'A device with no connection to the plot at all', 'A replacement for any character development', 'A structure used only in poetry, never in the novel form'], 0),
   ('Why might a road novel favour episodic chapters over a single continuous scene?', ['Episodic chapters mirror the discrete stops and encounters of an ongoing journey', 'Episodic chapters are forbidden in a road novel', 'A road novel must always take place in a single location', 'A continuous scene always suits a journey better than episodes'], 0)]),
F('Discrete Math: Big O Notation and Algorithmic Growth Rates',
  'Grade 11 Functions strand: big O notation describes how the running time or resource use of an algorithm grows as the size of its input increases, focusing on the dominant term of that growth and ignoring constant factors, which lets mathematicians and programmers compare the efficiency of different algorithms in general terms.',
  [('What does big O notation describe?', ['How the running time or resource use of an algorithm grows as input size increases', 'The exact number of lines of code in a program', 'The colour scheme of a programming language', 'A quantity with no connection to algorithms at all'], 0),
   ('What part of an algorithms growth rate does big O notation focus on?', ['The dominant term of that growth', 'Every constant factor with no simplification at all', 'A term chosen at random with no mathematical basis', 'Only the smallest possible input size'], 0),
   ('What does big O notation typically ignore when describing growth?', ['Constant factors', 'The size of the input entirely', 'Every term in the growth function', 'The algorithm itself'], 0),
   ('What can big O notation be used to compare?', ['The efficiency of different algorithms in general terms', 'The colour of two different computer screens', 'The physical size of two different computers', 'A quantity that has no relevance to computer science'], 0),
   ('Why might an algorithm described as growing linearly be preferred over one that grows exponentially for large inputs?', ['A linear growth rate increases resource use far more slowly as input size grows', 'Exponential growth always uses fewer resources than linear growth', 'Both growth rates always require an identical amount of resources', 'Growth rate has no effect on how an algorithm performs on large inputs'], 0)]),
B('Biology: Punctuated Equilibrium versus Gradualism in the Fossil Record',
  'Grade 11 Biology strand: gradualism describes evolutionary change as a slow, steady accumulation of small modifications over long periods, while punctuated equilibrium proposes that species instead remain largely stable for long stretches and then undergo relatively rapid bursts of change, often linked to speciation events, a pattern some fossil records appear to support.',
  [('How does gradualism describe evolutionary change?', ['As a slow, steady accumulation of small modifications over long periods', 'As a process that occurs in a single instantaneous event', 'As a process with no connection to time at all', 'As a pattern that only ever reverses previous change'], 0),
   ('What does punctuated equilibrium propose about most of a species existence?', ['Species remain largely stable for long stretches', 'Species change dramatically every single generation', 'Species never remain stable at any point', 'Species disappear entirely between periods of change'], 0),
   ('What does punctuated equilibrium associate rapid bursts of change with?', ['Speciation events', 'A complete absence of any environmental pressure', 'Events that have no connection to evolution at all', 'A permanent halt in all evolutionary processes'], 0),
   ('What kind of evidence has been used to support the punctuated equilibrium model?', ['Some fossil records that show long periods of stability followed by sudden change', 'Fossil records that show absolutely no variation at any point in time', 'A complete absence of any fossil evidence whatsoever', 'Evidence drawn only from living species, never fossils'], 0),
   ('How does punctuated equilibrium differ from strict gradualism?', ['It proposes uneven pacing, with long stability punctuated by rapid change, rather than constant slow change', 'It proposes that evolutionary change never occurs at any pace', 'It proposes the exact same constant rate of change as gradualism', 'It rejects the idea that species can change at all'], 0)]),
C('Chemistry: The Contact Process — Industrial Production of Sulfuric Acid',
  'Grade 11 Chemistry strand: the contact process manufactures sulfuric acid on an industrial scale by oxidizing sulfur dioxide to sulfur trioxide over a catalyst, then dissolving the sulfur trioxide in concentrated sulfuric acid before diluting the product with water, a sequence designed to avoid the dangerous fog that direct reaction with water would otherwise produce.',
  [('What acid does the contact process manufacture on an industrial scale?', ['Sulfuric acid', 'Hydrochloric acid', 'Acetic acid', 'Nitric acid'], 0),
   ('What gas is oxidized over a catalyst in the early stage of the contact process?', ['Sulfur dioxide, oxidized to sulfur trioxide', 'Carbon dioxide, oxidized to carbon monoxide', 'Nitrogen gas, oxidized to ammonia', 'Oxygen gas, oxidized to ozone with no other reactant'], 0),
   ('What is sulfur trioxide dissolved into during the contact process?', ['Concentrated sulfuric acid', 'Pure distilled water directly', 'A solution of table salt', 'A bath of liquid nitrogen'], 0),
   ('Why is sulfur trioxide not dissolved directly in water during the contact process?', ['Direct reaction with water would produce a dangerous, hard-to-control fog', 'Water has no reaction with sulfur trioxide of any kind', 'Direct reaction with water produces no acid at all', 'Sulfur trioxide is incapable of dissolving in any liquid'], 0),
   ('What role does the catalyst play in the oxidation step of the contact process?', ['It speeds up the conversion of sulfur dioxide into sulfur trioxide', 'It prevents any reaction from occurring at all', 'It converts the product back into raw sulfur', 'It has no effect on the rate of the reaction'], 0)]),
]),
day(173, [
E('Grammar: The Ellipsis and the Rhetoric of the Unsaid',
  'Grade 11 English strand: an ellipsis, shown as three spaced periods, signals an intentional omission from a quoted passage or trails a sentence off to suggest hesitation, uncertainty, or an unfinished thought, letting a writer communicate meaning through silence as deliberately as through the words that are actually printed.',
  [('How is an ellipsis typically shown in a printed sentence?', ['As three spaced periods', 'As a single exclamation mark', 'As a colon followed by a dash', 'As a capitalized word in brackets'], 0),
   ('What can an ellipsis signal when used within a quoted passage?', ['An intentional omission from the original text', 'That the entire quotation has been invented', 'That no words have been removed at all', 'That the passage must be read aloud twice'], 0),
   ('What effect can a trailing ellipsis have at the end of a sentence?', ['It suggests hesitation, uncertainty, or an unfinished thought', 'It always indicates that the sentence is grammatically complete and certain', 'It removes all emotional tone from a sentence', 'It signals that a new chapter is about to begin'], 0),
   ('What does the rhetorical use of an ellipsis allow a writer to communicate?', ['Meaning through silence, as deliberately as through printed words', 'Nothing at all, since silence carries no meaning in writing', 'Only factual information, never emotional tone', 'A complete list of every omitted word'], 0),
   ('Why might a writer use an ellipsis rather than simply ending a sentence with a period?', ['To leave a thought open-ended rather than firmly resolved', 'A period and an ellipsis always create an identical effect', 'An ellipsis is required at the end of every sentence in formal writing', 'Ending a sentence with a period is grammatically impossible'], 0)]),
F('Number Theory: Wilsons Theorem and Tests for Primality',
  'Grade 11 Functions strand: Wilsons theorem states that a whole number greater than one is prime exactly when the factorial of one less than that number, increased by one, is divisible by the number itself, giving a precise algebraic test for primality even though it becomes computationally impractical for very large numbers.',
  [('What does Wilsons theorem provide a test for?', ['Primality', 'Divisibility by ten only', 'The square root of a number', 'The sum of a numbers digits'], 0),
   ('According to Wilsons theorem, what quantity is examined for a number greater than one?', ['The factorial of one less than the number, increased by one', 'The square of the number itself', 'The cube root of the number', 'The sum of every number smaller than it'], 0),
   ('What must be true of that quantity for the original number to be prime, according to Wilsons theorem?', ['It must be divisible by the number itself', 'It must always equal exactly one', 'It must always equal zero', 'It must be divisible by every smaller number simultaneously'], 0),
   ('Why is Wilsons theorem described as computationally impractical for very large numbers?', ['Calculating a large factorial quickly becomes an enormous computation', 'Factorials become smaller as numbers increase, making calculation trivial', 'Wilsons theorem cannot be applied to any number larger than ten', 'Large numbers have no factorial defined at all'], 0),
   ('What kind of test does Wilsons theorem give for whether a number is prime?', ['A precise algebraic test', 'A test based only on visual inspection of the number', 'A test that only works for even numbers', 'A test with no mathematical basis whatsoever'], 0)]),
B('Biology: The Pancreas — Exocrine and Endocrine Roles',
  'Grade 11 Biology strand: the pancreas performs two distinct functions, an exocrine role in which it secretes digestive enzymes into the small intestine to help break down carbohydrates, fats, and proteins, and an endocrine role in which clusters of cells called the islets of Langerhans release insulin and glucagon directly into the bloodstream to regulate blood glucose.',
  [('What is the exocrine role of the pancreas?', ['Secreting digestive enzymes into the small intestine', 'Releasing insulin directly into the bloodstream', 'Producing red blood cells', 'Filtering toxins out of the blood'], 0),
   ('What structures within the pancreas are responsible for its endocrine role?', ['The islets of Langerhans', 'The alveoli', 'The nephrons', 'The villi of the small intestine'], 0),
   ('Name one hormone released by the endocrine portion of the pancreas.', ['Insulin', 'Bile', 'Pepsin', 'Amylase, released only as a digestive enzyme with no hormonal role'], 0),
   ('What do the digestive enzymes secreted by the exocrine pancreas help break down?', ['Carbohydrates, fats, and proteins', 'Only water, with no other nutrient involved', 'Bone tissue exclusively', 'Only oxygen absorbed from the lungs'], 0),
   ('Why is the pancreas described as having two distinct functions?', ['It performs both an exocrine digestive role and an endocrine hormonal role', 'It performs only a single function with no distinction at all', 'It has no connection to digestion or hormone regulation', 'Both of its functions are entirely identical to each other'], 0)]),
C('Chemistry: The Chemistry of Glass — Amorphous Solids and Silicate Networks',
  'Grade 11 Chemistry strand: glass is an amorphous solid formed by cooling molten silica so quickly that its atoms are locked into a disordered, non-crystalline network rather than the neatly repeating lattice of a true crystal, which is why glass lacks a sharp melting point and instead softens gradually as it is heated.',
  [('What type of solid is glass classified as?', ['An amorphous solid', 'A perfect crystalline solid', 'A pure metal', 'A gas at room temperature'], 0),
   ('What raw material is typically melted and rapidly cooled to form glass?', ['Silica', 'Pure carbon', 'Table salt', 'Liquid mercury'], 0),
   ('Why does glass lack the neatly repeating structure of a true crystal?', ['Its atoms are locked into a disordered network as it cools too quickly to form a regular lattice', 'Its atoms always form a perfectly repeating lattice identical to a crystal', 'Glass contains no atoms of any kind', 'Glass is cooled so slowly that it always forms a crystal'], 0),
   ('What happens to glass as it is heated, in contrast to a crystalline solid with a sharp melting point?', ['It softens gradually rather than melting at one exact temperature', 'It melts instantly at a single precise temperature identical to ice', 'It remains perfectly rigid at every temperature', 'It converts directly into a gas with no intermediate softening'], 0),
   ('Why is the disordered atomic structure of glass significant for its physical properties?', ['It explains why glass behaves differently from crystalline solids when heated or stressed', 'A disordered structure has no effect on any physical property', 'Glass and crystalline solids always behave identically when heated', 'Disordered structure only affects the colour of a material, not its melting behaviour'], 0)]),
]),
day(174, [
E('Writing: The Letter to the Editor — Concise Public Argument',
  'Grade 11 English strand: a letter to the editor responds to a specific article or issue with a tightly focused argument, stating a clear position early, supporting it with a small number of well-chosen pieces of evidence, and staying within a strict word limit that forces every sentence to earn its place.',
  [('What does a letter to the editor typically respond to?', ['A specific article or issue', 'A topic with no connection to current events at all', 'A private conversation with no public relevance', 'A random subject chosen without reference to any publication'], 0),
   ('When should a letter to the editor state its clear position?', ['Early in the letter', 'Only in the final sentence, with no earlier indication', 'It should never state a clear position at all', 'Only after the word limit has already been exceeded'], 0),
   ('What kind of evidence does a letter to the editor typically use to support its position?', ['A small number of well-chosen pieces of evidence', 'An unlimited amount of unrelated evidence', 'No evidence of any kind', 'Evidence that contradicts the letters own stated position'], 0),
   ('What constraint does a letter to the editor typically operate under?', ['A strict word limit', 'No length restriction of any kind', 'A requirement to be exactly one page long', 'A rule forbidding any mention of the original article'], 0),
   ('Why does a strict word limit shape how a letter to the editor is written?', ['It forces every sentence to be purposeful and support the argument efficiently', 'A word limit has no effect on how the letter is written', 'It allows the writer to include unlimited unrelated detail', 'It requires the letter to avoid stating any argument at all'], 0)]),
F('Statistics: The Multinomial Distribution and Categorical Outcomes',
  'Grade 11 Functions strand: the multinomial distribution extends the binomial distribution from two possible outcomes to three or more categories, modelling the probability of observing a specific combination of counts across those categories when a fixed number of independent trials is repeated, such as rolling a die a set number of times and counting each face.',
  [('What distribution does the multinomial distribution extend?', ['The binomial distribution', 'The normal distribution', 'The Poisson distribution', 'A distribution with no connection to probability at all'], 0),
   ('How many possible outcome categories does the multinomial distribution allow, compared to the binomial distribution?', ['Three or more categories, compared to only two for the binomial distribution', 'Exactly two categories, identical to the binomial distribution', 'Only a single category with no variation', 'An undefined number that cannot be specified'], 0),
   ('What does the multinomial distribution model the probability of?', ['Observing a specific combination of counts across several categories', 'A single unrepeated event with no trials involved', 'An outcome that has no numerical probability at all', 'A quantity that never changes between trials'], 0),
   ('Give an example of a scenario the multinomial distribution could model.', ['Rolling a die a set number of times and counting each face', 'Flipping a single coin exactly once', 'Measuring the height of a single person', 'A scenario with no repeated trials of any kind'], 0),
   ('What condition is required for the trials underlying a multinomial distribution?', ['A fixed number of independent trials', 'An unlimited, undefined number of dependent trials', 'Exactly one trial with no repetition', 'Trials that must always produce the same outcome'], 0)]),
B('Biology: Amphibian Metamorphosis and Endocrine Control',
  'Grade 11 Biology strand: amphibian metamorphosis transforms an aquatic, gill-breathing larva such as a tadpole into an air-breathing adult with limbs, a process driven primarily by rising levels of the hormone thyroxine, which triggers tissue remodelling including tail resorption, limb development, and the replacement of gills with lungs.',
  [('What does amphibian metamorphosis transform a larva into?', ['An air-breathing adult with limbs', 'A permanently aquatic organism with no further change', 'A completely different species entirely', 'An organism that never develops limbs of any kind'], 0),
   ('What hormone primarily drives amphibian metamorphosis?', ['Thyroxine', 'Insulin', 'Adrenaline', 'A hormone that plays no role in metamorphosis'], 0),
   ('Name one tissue change that occurs during amphibian metamorphosis.', ['Tail resorption', 'Growth of a permanent tail with no resorption at all', 'Loss of all limbs entirely', 'Complete disappearance of the digestive system'], 0),
   ('What respiratory change occurs as a tadpole becomes an adult amphibian?', ['Gills are replaced with lungs', 'Lungs are replaced with gills', 'No respiratory change occurs at any point', 'The organism stops breathing entirely during metamorphosis'], 0),
   ('Why is rising thyroxine level considered the primary trigger of amphibian metamorphosis?', ['It coordinates the timing of tissue remodelling throughout the transformation', 'Thyroxine has no measurable effect on amphibian development', 'Thyroxine only affects mammals, never amphibians', 'Metamorphosis occurs at a fixed age regardless of hormone levels'], 0)]),
C('Chemistry: The Chemistry of Cement and Concrete — Hydration Reactions',
  'Grade 11 Chemistry strand: cement hardens through a hydration reaction in which its calcium silicate compounds react with water to form an interlocking network of calcium silicate hydrate crystals, and mixing this cement paste with sand and gravel produces concrete, whose strength depends on how completely this hydration reaction proceeds.',
  [('What type of reaction causes cement to harden?', ['A hydration reaction', 'A combustion reaction', 'A radioactive decay reaction', 'A reaction that requires no water at all'], 0),
   ('What compounds in cement react with water during hydration?', ['Calcium silicate compounds', 'Pure carbon compounds only', 'Noble gases with no reactivity', 'Compounds containing no calcium at all'], 0),
   ('What structure forms as a result of the hydration reaction in cement?', ['An interlocking network of calcium silicate hydrate crystals', 'A single uniform liquid with no solid structure', 'A gas that escapes immediately from the mixture', 'A structure containing no crystals of any kind'], 0),
   ('What is produced when cement paste is mixed with sand and gravel?', ['Concrete', 'Pure limestone', 'Glass', 'A substance identical to unmixed cement'], 0),
   ('What does the strength of concrete depend on?', ['How completely the hydration reaction proceeds', 'The colour of the sand used in the mixture', 'A factor with no connection to any chemical reaction', 'The exact temperature of the surrounding air alone, with no reaction involved'], 0)]),
]),
day(175, [
E('Oral Communication: Reading Aloud — Prosody and Performance in Recitation',
  'Grade 11 English strand: prosody refers to the rhythm, stress, and intonation a speaker brings to a text when reading aloud, and a skilled recitation uses pacing, pause, and vocal emphasis to reveal meaning that might stay hidden on the silent page, turning written words into a shaped, audible performance.',
  [('What does prosody refer to when reading a text aloud?', ['The rhythm, stress, and intonation a speaker brings to the reading', 'The exact spelling of every word in the text', 'The physical size of the printed page', 'A quality that applies only to written text, never spoken performance'], 0),
   ('What can a skilled recitation reveal that might stay hidden on the silent page?', ['Meaning conveyed through pacing, pause, and vocal emphasis', 'Nothing at all, since reading aloud adds no new meaning', 'Only the authors name and publication date', 'A meaning that contradicts the original written text'], 0),
   ('What does recitation turn written words into?', ['A shaped, audible performance', 'A silent, unchanging document', 'A physical object with no sound involved', 'A text that can no longer be read silently afterward'], 0),
   ('Name one tool a speaker can use to shape meaning during a recitation.', ['Pause', 'Font size, since fonts affect spoken performance', 'Page number, since numbering shapes meaning', 'Margin width, since margins control emphasis'], 0),
   ('Why might the same written passage sound different when read aloud by two different speakers?', ['Each speaker brings a distinct prosody through their own pacing, stress, and intonation choices', 'Spoken performance always sounds identical no matter who reads it', 'Only the words on the page matter, with no role for the speaker', 'Reading aloud removes all possible variation in meaning'], 0)]),
F('Financial Mathematics: Real versus Nominal Interest Rates and Inflation',
  'Grade 11 Functions strand: a nominal interest rate is the stated rate on an investment or loan before accounting for inflation, while the real interest rate adjusts that stated rate to reflect actual purchasing power, so that a nominal rate that looks attractive can still represent a loss in real terms if inflation rises faster than the nominal rate itself.',
  [('What is a nominal interest rate?', ['The stated rate on an investment or loan before accounting for inflation', 'A rate that already accounts fully for inflation', 'A rate that applies only to loans, never investments', 'A rate that has no connection to money at all'], 0),
   ('What does the real interest rate adjust for?', ['Actual purchasing power, accounting for inflation', 'The exact number of years remaining on a loan', 'The colour of the currency used', 'A factor with no connection to inflation'], 0),
   ('What can happen to a nominal interest rate that looks attractive if inflation rises faster than that rate?', ['It can still represent a loss in real terms', 'It always guarantees a real gain regardless of inflation', 'Inflation has no effect on the value of a nominal rate', 'The nominal rate automatically adjusts itself to cancel out inflation'], 0),
   ('Why is distinguishing between nominal and real interest rates useful for an investor?', ['It shows whether an investment actually increases purchasing power after inflation is considered', 'The distinction has no practical use for any investor', 'Nominal and real rates are always numerically identical', 'Real interest rates apply only to loans, never to investments'], 0),
   ('What relationship connects the nominal rate, the real rate, and inflation?', ['The real rate approximates the nominal rate minus the inflation rate', 'The real rate is always higher than the nominal rate', 'Inflation has no mathematical relationship to either rate', 'The nominal rate is always lower than the real rate'], 0)]),
B('Ecology: Predator-Prey Coevolution and the Evolutionary Arms Race',
  'Grade 11 Biology strand: predator-prey coevolution occurs when adaptations that improve a predators ability to capture prey exert selective pressure that favours prey with better defences, and those improved defences in turn favour predators with better hunting adaptations, producing an ongoing evolutionary arms race in which neither side gains a lasting advantage.',
  [('What is predator-prey coevolution?', ['A reciprocal evolutionary process in which predator and prey adaptations drive one another', 'A process in which only the predator ever changes over time', 'A process in which only the prey ever changes over time', 'A process with no connection to natural selection at all'], 0),
   ('What does an improved predator adaptation exert on a prey population?', ['Selective pressure favouring prey with better defences', 'No pressure of any kind on the prey population', 'Pressure that always eliminates the prey population entirely', 'Pressure that has no connection to evolution'], 0),
   ('What happens to predator adaptations after prey develop improved defences?', ['Selective pressure then favours predators with better hunting adaptations', 'Predators stop evolving entirely once prey improve their defences', 'Predators immediately go extinct once prey improve their defences', 'Predator adaptations have no relationship to prey defences'], 0),
   ('What term describes the ongoing cycle of reciprocal adaptation between predator and prey?', ['An evolutionary arms race', 'A one-time event with no ongoing cycle', 'A process limited strictly to a single generation', 'A relationship with no long-term evolutionary pattern'], 0),
   ('Why does neither predator nor prey typically gain a lasting advantage in this arms race?', ['Each improvement in one species tends to be matched over time by a counter-improvement in the other', 'Predators always gain a permanent advantage over prey', 'Prey always gain a permanent advantage over predators', 'Neither species is capable of adapting at all'], 0)]),
C('Chemistry: Photovoltaic Cells and the Chemistry of Solar Energy Conversion',
  'Grade 11 Chemistry strand: a photovoltaic cell converts sunlight directly into electricity using a semiconductor material, typically silicon treated to create a junction between regions with different electrical properties, so that absorbed light energy frees electrons that are then driven through an external circuit as a usable current.',
  [('What does a photovoltaic cell convert sunlight into?', ['Electricity', 'Heat with no electrical output at all', 'Pure water', 'A gas with no other product formed'], 0),
   ('What type of material is central to how a photovoltaic cell works?', ['A semiconductor material', 'A pure insulator with no conductivity at all', 'A liquid with no solid component', 'A noble gas'], 0),
   ('What semiconductor is commonly used in photovoltaic cells?', ['Silicon', 'Pure gold', 'Table salt', 'Liquid mercury'], 0),
   ('What happens to electrons when light energy is absorbed by the semiconductor in a photovoltaic cell?', ['They are freed and driven through an external circuit as a usable current', 'They remain completely fixed in place with no movement at all', 'They are destroyed and cease to exist', 'They convert directly into photons with no electrical effect'], 0),
   ('What structural feature within the semiconductor helps generate a directional flow of current?', ['A junction between regions with different electrical properties', 'A single uniform region with no junction of any kind', 'A junction that only exists in the absence of light', 'A structure identical throughout the entire cell with no variation'], 0)]),
]),
day(176, [
E('Media Literacy: The Filter Bubble and the Algorithmic Echo Chamber',
  'Grade 11 English strand: a filter bubble forms when a personalized recommendation algorithm repeatedly shows a user content that matches their existing preferences, gradually narrowing the range of viewpoints they encounter until opposing perspectives become rare, a dynamic that can reinforce existing beliefs and reduce exposure to alternative ideas.',
  [('What causes a filter bubble to form?', ['A personalized recommendation algorithm repeatedly showing content that matches existing preferences', 'A random selection process with no personalization involved', 'A single unchanging list of content shown to every user identically', 'An algorithm designed specifically to show only opposing viewpoints'], 0),
   ('What happens to the range of viewpoints a user encounters inside a filter bubble?', ['It gradually narrows until opposing perspectives become rare', 'It expands infinitely with no limit at all', 'It remains exactly the same no matter how long the user engages with the platform', 'It always includes an equal balance of every possible viewpoint'], 0),
   ('What is a filter bubble also commonly compared to?', ['An algorithmic echo chamber', 'A public library with no personalization at all', 'A printed newspaper with no algorithm involved', 'A source that guarantees full exposure to every viewpoint'], 0),
   ('What effect can a filter bubble have on existing beliefs?', ['It can reinforce existing beliefs by limiting exposure to alternative ideas', 'It always weakens existing beliefs by exposing users to every viewpoint', 'It has no measurable effect on a users beliefs at all', 'It guarantees that a user will change their beliefs completely'], 0),
   ('Why might understanding filter bubbles be important for evaluating information encountered online?', ['Recognizing a filter bubble helps a reader seek out perspectives the algorithm might otherwise hide', 'Filter bubbles have no relevance to evaluating information at all', 'Filter bubbles only affect printed media, never online platforms', 'Understanding filter bubbles guarantees a reader will never encounter biased content again'], 0)]),
F('Geometry: The Intersection of a Line and a Plane in Three Dimensions',
  'Grade 11 Functions strand: finding where a line intersects a plane in three dimensions involves substituting the parametric equations of the line into the equation of the plane and solving for the parameter, and depending on the result the line may cross the plane at exactly one point, lie entirely within it, or run parallel to it with no intersection at all.',
  [('What equations are substituted into a planes equation to find where a line intersects it?', ['The parametric equations of the line', 'The equation of an unrelated circle', 'A single fixed coordinate with no equation involved', 'The equation of a second, unrelated plane'], 0),
   ('What is solved for after substituting the lines equations into the planes equation?', ['The parameter', 'The radius of the plane', 'The slope of the plane', 'The colour of the intersection point'], 0),
   ('What is one possible outcome when a line meets a plane in three dimensions?', ['The line crosses the plane at exactly one point', 'The line always passes through every point in space', 'The line always lies exactly on top of every other line', 'The line always intersects the plane at an infinite number of unrelated points with no pattern'], 0),
   ('What does it mean if a line lies entirely within a plane?', ['Every point on the line also satisfies the equation of the plane', 'No point on the line ever satisfies the equation of the plane', 'The line and plane share no relationship at all', 'The line must be perpendicular to the plane at every point'], 0),
   ('What does it mean if a line runs parallel to a plane with no intersection?', ['The line never meets the plane at any point', 'The line meets the plane at every possible point', 'The line and plane are identical to each other', 'The line always meets the plane at exactly one point'], 0)]),
B('Biology: Antibiotic Mechanisms — Disrupting the Bacterial Cell Wall',
  'Grade 11 Biology strand: many antibiotics such as penicillin work by interfering with the enzymes bacteria use to build their rigid cell wall, so that as the bacterium grows and attempts to divide, the weakened wall cannot withstand internal pressure and the cell ruptures, a mechanism that exploits a structural feature human cells do not share.',
  [('What structure do antibiotics such as penicillin typically target?', ['The bacterial cell wall', 'The human nucleus', 'A structure that does not exist in bacteria', 'The bacterial nucleus, which bacteria do not actually possess'], 0),
   ('What do these antibiotics interfere with in order to disrupt the cell wall?', ['The enzymes bacteria use to build their cell wall', 'The DNA sequence of a human cell', 'A structure found only in viruses', 'An enzyme with no connection to the cell wall'], 0),
   ('What happens to a bacterium once its cell wall is weakened by such an antibiotic?', ['It ruptures under internal pressure as it attempts to grow and divide', 'It becomes permanently immune to any further antibiotic exposure', 'It immediately converts into a different species of bacteria', 'It develops a stronger cell wall than before'], 0),
   ('Why can antibiotics that target the bacterial cell wall be selective for bacteria over human cells?', ['Human cells do not have the same rigid cell wall structure that bacteria depend on', 'Human cells and bacterial cells share an identical cell wall structure', 'Antibiotics affect every type of cell equally, with no selectivity', 'Human cells lack any structure that could be affected by antibiotics'], 0),
   ('What happens during bacterial growth and division that makes a weakened cell wall especially dangerous to the bacterium?', ['Internal pressure builds and the compromised wall cannot contain it', 'Internal pressure disappears entirely once the wall is weakened', 'Growth and division stop having any effect on internal pressure', 'The bacterium becomes completely immune to internal pressure changes'], 0)]),
C('Chemistry: Chemical Sensors — How pH and Gas Sensors Work',
  'Grade 11 Chemistry strand: a chemical sensor converts the presence or concentration of a target substance into a measurable signal, so a pH sensor typically measures the voltage generated across a special glass membrane sensitive to hydrogen ion concentration, while a gas sensor may rely on a chemical reaction at its surface that changes electrical resistance in the presence of a specific gas.',
  [('What does a chemical sensor convert the presence of a target substance into?', ['A measurable signal', 'A substance that cannot be detected at all', 'A completely random and unrelated output', 'A signal that has no connection to concentration'], 0),
   ('What does a typical pH sensor measure to determine hydrogen ion concentration?', ['A voltage generated across a special glass membrane', 'The exact colour of the surrounding air', 'The temperature of the solution alone, with no other measurement', 'The mass of the solution being tested'], 0),
   ('What might change in a gas sensor when a specific gas is present at its surface?', ['Its electrical resistance', 'Its physical size, which never changes in any sensor', 'The colour of the surrounding room', 'The sensor immediately stops functioning altogether'], 0),
   ('What triggers the response of a gas sensor that relies on surface chemistry?', ['A chemical reaction occurring at the sensor surface', 'A process with no chemical reaction involved at all', 'A reaction that occurs only in the absence of any gas', 'A purely mechanical process with no chemistry involved'], 0),
   ('Why is converting a chemical property into an electrical signal useful for a sensor?', ['It allows the concentration of a substance to be measured quickly and read electronically', 'Electrical signals cannot be measured or interpreted in any practical way', 'Converting chemical properties into signals prevents any measurement from occurring', 'Electrical signals have no connection to chemical concentration'], 0)]),
]),
day(177, [
E('Literature: The Campus Novel and the World of Higher Education',
  'Grade 11 English strand: a campus novel is set within the enclosed world of a college or university, often using the tension between intellectual ambition and personal or institutional politics to satirize academic life, following students or faculty as they navigate rivalry, status, and the pressure to succeed within that self-contained community.',
  [('Where is a campus novel typically set?', ['Within the enclosed world of a college or university', 'On a remote island with no institution present', 'Entirely within a single family household', 'In a courtroom with no academic setting involved'], 0),
   ('What tension does a campus novel often use to satirize academic life?', ['The tension between intellectual ambition and personal or institutional politics', 'A tension that has no connection to intellectual life at all', 'The tension between two unrelated nations at war', 'A tension found only in fairy tales, never in realistic fiction'], 0),
   ('Who might a campus novel typically follow as its central characters?', ['Students or faculty', 'Only characters with no connection to any school', 'Exclusively young children in elementary school', 'Characters who never interact with any academic institution'], 0),
   ('What pressures do characters in a campus novel often navigate?', ['Rivalry, status, and the pressure to succeed', 'A complete absence of any conflict or pressure', 'Only physical, non-academic challenges', 'Pressures entirely unrelated to their academic environment'], 0),
   ('Why is the campus setting well suited to satire in this genre?', ['Its self-contained community concentrates ambition, hierarchy, and politics in one setting', 'A campus setting removes all possibility of conflict or ambition', 'Satire requires a setting with no defined community at all', 'A university setting has no connection to hierarchy or politics'], 0)]),
F('Complex Numbers: The Argand Plane and Geometric Representations',
  'Grade 11 Functions strand: the Argand plane represents a complex number as a point whose horizontal coordinate is the real part and whose vertical coordinate is the imaginary part, turning algebraic operations on complex numbers into geometric transformations such as reflections, rotations, and translations that can be visualized directly on the plane.',
  [('What does the horizontal coordinate represent for a complex number plotted on the Argand plane?', ['The real part of the complex number', 'The imaginary part of the complex number', 'The magnitude of an unrelated vector', 'A value with no connection to the complex number at all'], 0),
   ('What does the vertical coordinate represent for a complex number plotted on the Argand plane?', ['The imaginary part of the complex number', 'The real part of the complex number', 'The angle of an unrelated triangle', 'A value that has no defined meaning'], 0),
   ('What does the Argand plane turn algebraic operations on complex numbers into?', ['Geometric transformations that can be visualized directly', 'Operations that cannot be represented visually in any way', 'A single unchanging point with no transformation involved', 'A transformation limited only to real numbers'], 0),
   ('Name one type of geometric transformation associated with complex number operations on the Argand plane.', ['Rotation', 'A transformation that does not exist in geometry', 'A transformation limited strictly to three dimensions', 'A transformation that removes the imaginary part entirely'], 0),
   ('Why is visualizing complex numbers on the Argand plane useful?', ['It provides geometric intuition for operations that might otherwise seem purely abstract', 'Visualizing complex numbers removes all mathematical meaning from them', 'The Argand plane can only represent real numbers, never complex ones', 'Geometric intuition has no relevance to understanding complex numbers'], 0)]),
B('Biology: Genomic Libraries and DNA Cloning Techniques',
  'Grade 11 Biology strand: a genomic library is a collection of DNA fragments from an organisms entire genome, each fragment inserted into a separate vector such as a plasmid and introduced into host bacteria, so that as the bacteria multiply they produce many identical copies of each fragment, preserving the complete genome in a form that researchers can search and retrieve piece by piece.',
  [('What is a genomic library?', ['A collection of DNA fragments from an organisms entire genome', 'A single unbroken strand of DNA with no fragments at all', 'A physical building that stores printed books about genetics', 'A collection containing no DNA of any kind'], 0),
   ('What is each DNA fragment inserted into when a genomic library is constructed?', ['A separate vector such as a plasmid', 'A single shared vector containing every fragment at once', 'A structure with no connection to DNA insertion', 'A fragment of RNA rather than any vector'], 0),
   ('What organism is commonly used to multiply the inserted DNA fragments?', ['Host bacteria', 'A fully grown human being', 'A plant with no bacterial component involved', 'An organism incapable of reproduction'], 0),
   ('What happens to each DNA fragment as the host bacteria multiply?', ['Many identical copies of the fragment are produced', 'The fragment is destroyed completely', 'The fragment converts into a completely different gene', 'No copies of the fragment are ever produced'], 0),
   ('Why is a genomic library useful to researchers?', ['It preserves the complete genome in a form that can be searched and retrieved piece by piece', 'It has no practical research application of any kind', 'It destroys all genetic information rather than preserving it', 'It only stores information about a single gene, never a complete genome'], 0)]),
C('Chemistry: Enzymes as Biological Catalysts Compared to Industrial Catalysts',
  'Grade 11 Chemistry strand: enzymes are biological catalysts that speed up specific reactions inside living cells by lowering activation energy through a precisely shaped active site, and comparing them with industrial catalysts such as those used in the Haber process highlights how enzymes achieve remarkable specificity and efficiency at the mild temperatures and pressures found in living organisms.',
  [('What are enzymes classified as?', ['Biological catalysts', 'Structural proteins with no catalytic role', 'A type of inorganic mineral', 'A substance with no effect on reaction rate'], 0),
   ('What do enzymes lower in order to speed up a reaction?', ['Activation energy', 'The total mass of the reactants', 'The temperature of the surrounding environment permanently', 'The number of atoms present in a reactant'], 0),
   ('What structural feature of an enzyme allows it to act on a specific reactant?', ['Its precisely shaped active site', 'A feature that applies equally to every possible reactant with no selectivity', 'A random shape that changes with every reaction', 'An active site identical in every enzyme'], 0),
   ('What condition do enzymes typically operate under, compared to many industrial catalysts?', ['Mild temperatures and pressures found in living organisms', 'Extremely high temperatures and pressures identical to industrial reactors', 'A complete vacuum with no surrounding conditions at all', 'Conditions with no defined temperature or pressure'], 0),
   ('What quality do enzymes demonstrate that is often highlighted when comparing them to industrial catalysts such as those in the Haber process?', ['Remarkable specificity and efficiency', 'A complete lack of specificity for any reaction', 'An inability to catalyze any reaction at all', 'A requirement for extremely high pressure to function'], 0)]),
]),
day(178, [
E('Poetry: The Limerick and the Comic Verse Tradition',
  'Grade 11 English strand: a limerick is a five-line comic poem with a distinctive AABBA rhyme scheme and a bouncing anapestic rhythm, traditionally building toward a punchline or absurd twist in its final line, making it a compact form well suited to wordplay, exaggeration, and light satire.',
  [('How many lines does a limerick have?', ['Five', 'Fourteen', 'Three', 'Eight'], 0),
   ('What rhyme scheme is characteristic of a limerick?', ['AABBA', 'ABAB', 'AAAA', 'A rhyme scheme that is never fixed in a limerick'], 0),
   ('What kind of rhythm does a limerick traditionally use?', ['A bouncing anapestic rhythm', 'A rhythm with no defined pattern at all', 'The exact rhythm of a Shakespearean sonnet', 'A rhythm identical to free verse'], 0),
   ('What does a limerick traditionally build toward in its final line?', ['A punchline or absurd twist', 'A solemn, tragic conclusion', 'A detailed historical account', 'A line with no connection to the rest of the poem'], 0),
   ('Why is the limerick well suited to wordplay and light satire?', ['Its compact, rhythmic, comic structure invites exaggeration and a punchline twist', 'A limerick forbids any humour or wordplay of any kind', 'Its structure is identical to a serious elegy', 'Limericks are always written about tragic subjects only'], 0)]),
F('Calculus: An Introduction to Antiderivatives and Integration',
  'Grade 11 Functions strand: an antiderivative of a function reverses the process of differentiation, finding a function whose derivative matches the original one, and this idea underlies integration, a tool used to determine quantities such as total accumulated change or the area beneath a curve.',
  [('What does an antiderivative of a function do?', ['It reverses the process of differentiation', 'It always produces the same function unchanged', 'It only applies to constant functions', 'It removes all variables from a function entirely'], 0),
   ('What must be true of the derivative of an antiderivative?', ['It must match the original function', 'It must always equal zero', 'It must always equal a different unrelated function', 'It must be undefined at every point'], 0),
   ('What broader mathematical tool does the idea of an antiderivative underlie?', ['Integration', 'Multiplication of matrices', 'The quadratic formula', 'A tool with no connection to calculus'], 0),
   ('Name one quantity that integration can be used to determine.', ['The area beneath a curve', 'The exact colour of a graph', 'The number of terms in an unrelated sequence', 'The slope of a single fixed point with no curve involved'], 0),
   ('Why is finding an antiderivative sometimes described as the reverse of finding a derivative?', ['Differentiating the antiderivative returns the original function you started with', 'Antiderivatives and derivatives are entirely unrelated operations', 'Finding an antiderivative always produces a numerical constant with no function attached', 'Differentiation and integration always produce identical results'], 0)]),
B('Ecology: Human Ecological Footprint and Carrying Capacity',
  'Grade 11 Biology strand: an ecological footprint estimates the amount of biologically productive land and water a population requires to produce the resources it consumes and absorb the waste it generates, and comparing that footprint to the carrying capacity of the available land highlights whether current human resource use is sustainable over the long term.',
  [('What does an ecological footprint estimate?', ['The amount of biologically productive land and water a population requires', 'The exact number of people living in a single city', 'A measurement with no connection to resource use', 'The total number of species found in a single ecosystem'], 0),
   ('What two things does an ecological footprint account for in a population resource use?', ['The resources it consumes and the waste it generates', 'Only the resources it consumes, with no reference to waste', 'Only the waste it generates, with no reference to resources', 'Neither resource consumption nor waste generation'], 0),
   ('What does comparing an ecological footprint to carrying capacity help reveal?', ['Whether current resource use is sustainable over the long term', 'The exact temperature of a given ecosystem', 'A comparison with no practical meaning at all', 'The total number of predators in an ecosystem'], 0),
   ('What happens when a populations ecological footprint exceeds the carrying capacity of its available land?', ['Resource use becomes unsustainable over time', 'Resource use automatically becomes more sustainable', 'The population immediately disappears with no further effect', 'Carrying capacity has no relationship to ecological footprint at all'], 0),
   ('Why is the concept of an ecological footprint useful for evaluating sustainability?', ['It converts complex resource use into a single land-based measure that can be compared across populations', 'It has no practical application in evaluating sustainability', 'It only applies to non-human species, never to humans', 'It ignores all forms of resource consumption entirely'], 0)]),
C('Chemistry: The Chemistry of Rust — Iron Oxidation and Corrosion Mechanisms',
  'Grade 11 Chemistry strand: rust forms when iron reacts with oxygen and water in an electrochemical process, in which iron atoms lose electrons to become iron ions at one region of the metal surface while oxygen is reduced at another, and the resulting iron oxide product is a flaky, porous compound that fails to protect the underlying metal from further corrosion.',
  [('What two substances does iron react with to form rust?', ['Oxygen and water', 'Only nitrogen gas, with no other reactant', 'Pure carbon dioxide alone', 'A noble gas with no reactivity at all'], 0),
   ('What type of process is rust formation classified as?', ['An electrochemical process', 'A purely mechanical process with no chemical reaction', 'A nuclear process involving isotopes', 'A process that occurs with no reaction of any kind'], 0),
   ('What happens to iron atoms at one region of the metal surface during rust formation?', ['They lose electrons to become iron ions', 'They gain electrons and become neutral oxygen', 'They remain completely unchanged throughout the process', 'They convert directly into rust with no electron transfer at all'], 0),
   ('What physical property of rust makes it a poor protective layer for the underlying metal?', ['It is flaky and porous', 'It is perfectly smooth and completely impermeable', 'It is denser than the original iron metal', 'It forms a layer that never separates from the metal surface'], 0),
   ('Why does rust fail to prevent further corrosion, unlike some other metal oxide coatings?', ['Its flaky, porous structure lets oxygen and water continue reaching the metal underneath', 'Rust always forms a perfectly sealed layer that blocks all further reaction', 'Rust prevents any further contact between the metal and its environment', 'Rust formation stops permanently after the first layer forms'], 0)]),
]),
day(179, [
E('Writing: The Restaurant Review as Evaluative Writing',
  'Grade 11 English strand: a restaurant review evaluates a dining experience across categories such as food quality, service, and atmosphere, combining specific sensory detail with a clearly stated overall judgment, so that a reader can both picture the experience and understand exactly how the writer weighed its strengths against its weaknesses.',
  [('What categories does a restaurant review typically evaluate?', ['Food quality, service, and atmosphere', 'Only the price of the parking lot outside', 'The architectural style of unrelated nearby buildings', 'A single category with no further detail given'], 0),
   ('What kind of detail does a restaurant review combine with its overall judgment?', ['Specific sensory detail', 'No detail at all, only a numeric score', 'Detail unrelated to the dining experience', 'A summary of the restaurants complete financial history'], 0),
   ('Why does a restaurant review need a clearly stated overall judgment?', ['So a reader understands how the writer weighed strengths against weaknesses', 'A restaurant review should never state any judgment at all', 'An overall judgment would make the review less useful to a reader', 'A restaurant review must remain entirely neutral with no evaluation'], 0),
   ('What allows a reader to picture the dining experience described in a review?', ['Specific sensory detail about food, service, and atmosphere', 'A complete absence of any descriptive language', 'A list of unrelated statistics with no sensory content', 'A review written with no reference to the actual meal'], 0),
   ('Why is evaluative writing like a restaurant review useful practice for other forms of argument?', ['It requires supporting a judgment with specific, concrete evidence', 'Evaluative writing never requires any supporting evidence', 'It has no connection to argumentative writing of any kind', 'A restaurant review must avoid forming any judgment whatsoever'], 0)]),
F('Discrete Math: Latin Squares and Combinatorial Design',
  'Grade 11 Functions strand: a Latin square is an n by n grid filled with n different symbols so that each symbol appears exactly once in every row and every column, a combinatorial structure related to Sudoku puzzles that is also used in the design of statistical experiments to balance out the effect of unwanted variables.',
  [('What defines a Latin square?', ['An n by n grid where each symbol appears exactly once in every row and column', 'A grid where every symbol appears in only one single row', 'A grid that allows a symbol to repeat freely within a row', 'A grid with no restriction on symbol placement at all'], 0),
   ('What familiar puzzle is structurally related to the Latin square?', ['Sudoku', 'Chess', 'A crossword puzzle with no grid restriction', 'A jigsaw puzzle with no symbols involved'], 0),
   ('Where are Latin squares used outside of recreational puzzles?', ['In the design of statistical experiments', 'Only in decorative art, with no mathematical use', 'In a context with no connection to mathematics at all', 'Exclusively in poetry, with no numerical structure'], 0),
   ('What do Latin squares help balance out in the design of an experiment?', ['The effect of unwanted variables', 'The total number of participants in a study', 'The colour scheme of a research report', 'A factor with no connection to experimental design'], 0),
   ('Why is the constraint that each symbol appears exactly once per row and column useful in experimental design?', ['It ensures every treatment is tested evenly across different conditions, reducing bias', 'The constraint has no useful application outside of puzzles', 'It guarantees that only one treatment is ever tested at all', 'It removes the need to control for any variable whatsoever'], 0)]),
B('Biology: Sensory Adaptation and Habituation in Nervous Systems',
  'Grade 11 Biology strand: sensory adaptation is a decrease in a sensory receptors response to a constant, unchanging stimulus, while habituation is a related but distinct decrease in behavioural response that occurs within the nervous system itself after repeated exposure to a stimulus, together explaining why a constant background smell or sound gradually fades from conscious awareness.',
  [('What is sensory adaptation?', ['A decrease in a sensory receptors response to a constant, unchanging stimulus', 'An increase in a sensory receptors response to every stimulus', 'A process that only affects vision, never any other sense', 'A process with no connection to sensory receptors at all'], 0),
   ('What is habituation?', ['A decrease in behavioural response within the nervous system after repeated exposure to a stimulus', 'An increase in behavioural response after a single exposure to a stimulus', 'A process identical in every way to muscle contraction', 'A process that has no connection to repeated stimulus exposure'], 0),
   ('Where does habituation occur, distinguishing it from sensory adaptation at the receptor level?', ['Within the nervous system itself', 'Only within muscle tissue, with no nervous involvement', 'Entirely outside the body, with no biological basis', 'In bone tissue exclusively'], 0),
   ('What everyday experience can sensory adaptation and habituation together help explain?', ['Why a constant background smell or sound gradually fades from conscious awareness', 'Why a sudden loud noise always goes completely unnoticed', 'Why every stimulus becomes more noticeable the longer it is present', 'A phenomenon with no connection to everyday sensory experience'], 0),
   ('Why might sensory adaptation and habituation be considered biologically useful?', ['They allow an organism to filter out unchanging background stimuli and focus attention on new or changing information', 'They prevent an organism from ever detecting any stimulus again', 'They have no adaptive value to an organism at all', 'They cause every stimulus to become permanently more intense over time'], 0)]),
C('Chemistry: Osmotic Pressure and Its Role Among the Colligative Properties',
  'Grade 11 Chemistry strand: osmotic pressure is the pressure that must be applied to a solution to stop the net inward flow of solvent across a semipermeable membrane from a region of lower solute concentration, and like boiling point elevation and freezing point depression it is classified as a colligative property because it depends on the number of dissolved particles rather than their identity.',
  [('What is osmotic pressure?', ['The pressure needed to stop the net inward flow of solvent across a semipermeable membrane', 'A pressure with no connection to solvent movement at all', 'The pressure inside a sealed container of pure gas', 'A pressure that only applies to solids, never to solutions'], 0),
   ('What kind of membrane is involved in the phenomenon of osmotic pressure?', ['A semipermeable membrane', 'A membrane that blocks every substance completely', 'A membrane that allows every substance to pass equally', 'A structure that is not a membrane at all'], 0),
   ('What category of property is osmotic pressure classified under?', ['A colligative property', 'A property with no defined classification', 'A property that depends only on the identity of the solute', 'A purely physical property unrelated to solute concentration'], 0),
   ('What determines the size of a colligative property such as osmotic pressure?', ['The number of dissolved particles, rather than their identity', 'The colour of the dissolved particles', 'The exact chemical identity of the solute, rather than particle count', 'A factor entirely unrelated to the solute'], 0),
   ('Name another colligative property besides osmotic pressure mentioned as a comparison.', ['Boiling point elevation', 'Electrical conductivity of a pure metal', 'The radioactive half-life of an isotope', 'The colour of a transition metal complex'], 0)]),
]),
day(180, [
E('English Review: Free Verse, Ellipsis, Recitation, and Campus Fiction',
  'Grade 11 English strand review: students revisit free verse, the ellipsis, reading aloud and recitation, the campus novel, and the restaurant review.',
  [('What does free verse abandon compared to traditional poetic forms?', ['A fixed meter and a regular rhyme scheme', 'All use of line breaks of any kind', 'Every reference to natural speech patterns', 'The ability to use imagery at all'], 0),
   ('How is an ellipsis typically shown in a printed sentence?', ['As three spaced periods', 'As a single exclamation mark', 'As a colon followed by a dash', 'As a capitalized word in brackets'], 0),
   ('What does prosody refer to when reading a text aloud?', ['The rhythm, stress, and intonation a speaker brings to the reading', 'The exact spelling of every word in the text', 'The physical size of the printed page', 'A quality that applies only to written text, never spoken performance'], 0),
   ('Where is a campus novel typically set?', ['Within the enclosed world of a college or university', 'On a remote island with no institution present', 'Entirely within a single family household', 'In a courtroom with no academic setting involved'], 0),
   ('What categories does a restaurant review typically evaluate?', ['Food quality, service, and atmosphere', 'Only the price of the parking lot outside', 'The architectural style of unrelated nearby buildings', 'A single category with no further detail given'], 0)]),
F('Functions Review: Log Derivatives, Number Theory, Finance, and Complex Numbers',
  'Grade 11 Functions strand review: students revisit derivatives of exponential and logarithmic functions, Wilsons theorem, real versus nominal interest rates, the Argand plane, and Latin squares.',
  [('What is notable about the derivative of the natural exponential function?', ['It equals the function itself', 'It always equals zero', 'It equals the square of the original function', 'It is undefined at every point'], 0),
   ('What does Wilsons theorem provide a test for?', ['Primality', 'Divisibility by ten only', 'The square root of a number', 'The sum of a numbers digits'], 0),
   ('What is a nominal interest rate?', ['The stated rate on an investment or loan before accounting for inflation', 'A rate that already accounts fully for inflation', 'A rate that applies only to loans, never investments', 'A rate that has no connection to money at all'], 0),
   ('What does the horizontal coordinate represent for a complex number plotted on the Argand plane?', ['The real part of the complex number', 'The imaginary part of the complex number', 'The magnitude of an unrelated vector', 'A value with no connection to the complex number at all'], 0),
   ('What defines a Latin square?', ['An n by n grid where each symbol appears exactly once in every row and column', 'A grid where every symbol appears in only one single row', 'A grid that allows a symbol to repeat freely within a row', 'A grid with no restriction on symbol placement at all'], 0)]),
B('Biology Review: Hemostasis, Endocrine Physiology, Coevolution, and Biotechnology',
  'Grade 11 Biology strand review: students revisit hemostasis, the pancreas, predator-prey coevolution, genomic libraries, and sensory adaptation and habituation.',
  [('What is hemostasis?', ['The process that stops bleeding after an injury', 'A process that causes bleeding to increase after an injury', 'A process with no connection to blood vessels at all', 'A process that only occurs in bone tissue'], 0),
   ('What is the exocrine role of the pancreas?', ['Secreting digestive enzymes into the small intestine', 'Releasing insulin directly into the bloodstream', 'Producing red blood cells', 'Filtering toxins out of the blood'], 0),
   ('What is predator-prey coevolution?', ['A reciprocal evolutionary process in which predator and prey adaptations drive one another', 'A process in which only the predator ever changes over time', 'A process in which only the prey ever changes over time', 'A process with no connection to natural selection at all'], 0),
   ('What is a genomic library?', ['A collection of DNA fragments from an organisms entire genome', 'A single unbroken strand of DNA with no fragments at all', 'A physical building that stores printed books about genetics', 'A collection containing no DNA of any kind'], 0),
   ('What is sensory adaptation?', ['A decrease in a sensory receptors response to a constant, unchanging stimulus', 'An increase in a sensory receptors response to every stimulus', 'A process that only affects vision, never any other sense', 'A process with no connection to sensory receptors at all'], 0)]),
C('Chemistry Review: Bonding, Materials, Energy, and Catalysis',
  'Grade 11 Chemistry strand review: students revisit Lewis structures and formal charge, the chemistry of glass, photovoltaic cells, enzymes compared with industrial catalysts, and osmotic pressure.',
  [('What does a Lewis structure represent?', ['The arrangement of valence electrons around bonded atoms', 'The total mass of a molecule', 'The physical state of a substance at room temperature', 'A structure with no connection to electrons at all'], 0),
   ('What type of solid is glass classified as?', ['An amorphous solid', 'A perfect crystalline solid', 'A pure metal', 'A gas at room temperature'], 0),
   ('What does a photovoltaic cell convert sunlight into?', ['Electricity', 'Heat with no electrical output at all', 'Pure water', 'A gas with no other product formed'], 0),
   ('What are enzymes classified as?', ['Biological catalysts', 'Structural proteins with no catalytic role', 'A type of inorganic mineral', 'A substance with no effect on reaction rate'], 0),
   ('What is osmotic pressure?', ['The pressure needed to stop the net inward flow of solvent across a semipermeable membrane', 'A pressure with no connection to solvent movement at all', 'The pressure inside a sealed container of pure gas', 'A pressure that only applies to solids, never to solutions'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_171_180)
    append_to(11, g11_171_180)
