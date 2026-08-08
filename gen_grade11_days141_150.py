#!/usr/bin/env python3
"""Grade 11, Days 141-150 -- extends Grade 11 from 140 to 150 days. Topics
chosen after dumping the existing Day 1-140 title list (data/grade11.json)
in full and cross-checking against it to avoid any overlap: the sestina and
fixed poetic forms, the fairy tale retelling, conditional sentences, climate
fiction, political cartoons, vocal delivery, the palimpsest, the white
paper, and the concrete poem; the product rule, the quotient rule, the
chain rule, network flow and max-flow min-cut, Fermats little theorem, the
geometric distribution, bonds and yield to maturity, the fundamental
theorem of algebra, and the dot product; horizontal gene transfer, seed
dormancy, cell signaling, ecological niches and competitive exclusion,
ABO/Rh blood types, embryonic development, antibody structure and the
humoral response, bioindicator species, and prions; zeolites, ionic
liquids, hydrogel polymers, nanoparticles and surface area effects,
transition metal colour, atmospheric aerosols, fire retardant chemistry,
invisible ink redox chemistry, and piezoelectric materials. Day 150 is a
lighter cross-subject review day, matching the structure of the Day 130 and
Day 140 review days (one review lesson per subject, each reusing five
first-questions verbatim from the batch).

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


g11_141_150 = [
day(141, [
E('Poetry: The Sestina and the Discipline of Fixed Forms',
  'Grade 11 English strand: a sestina is a fixed 39-line poem built on six end-words repeated in a rotating pattern across six stanzas plus a shorter three-line envoi, and the discipline of hitting every rotation while still saying something new tests a poets control of language.',
  [('What defines a sestina?', ['A fixed 39-line poem that repeats six end-words in a rotating pattern across six stanzas plus an envoi', 'A poem with no fixed length or repeated words', 'A poem written entirely in prose', 'A single rhymed couplet repeated indefinitely'], 0),
   ('How many end-words does a sestina rotate through its six main stanzas?', ['Six', 'Fourteen', 'Three', 'Twelve'], 0),
   ('What is the short final stanza of a sestina called?', ['The envoi', 'The chorus', 'The prologue', 'The stanza break'], 0),
   ('What makes writing a sestina especially challenging for a poet?', ['Repeating the same six end-words in a fixed rotation while keeping meaning fresh', 'Sestinas forbid the poet from using any end-word twice', 'Sestinas have no required structure at all', 'Sestinas must rhyme every line with every other line'], 0),
   ('Why might a poet choose a fixed form like the sestina rather than free verse?', ['The formal constraint can push the poet toward unexpected connections and disciplined craft', 'Fixed forms remove all creative choices from the poet', 'Free verse is always considered a fixed form', 'Fixed forms guarantee a poem will be published'], 0)]),
F('Calculus: The Product Rule for Derivatives',
  'Grade 11 Functions strand: the product rule states that the derivative of a product of two functions equals the derivative of the first function times the second, plus the first function times the derivative of the second, letting you differentiate products without expanding them first.',
  [('What does the product rule let you differentiate?', ['A product of two functions, without expanding the product first', 'Only a single function with no multiplication involved', 'Only the sum of two functions', 'Only a function divided by a constant'], 0),
   ('According to the product rule, the derivative of f times g equals what?', ['The derivative of f times g, plus f times the derivative of g', 'The derivative of f times the derivative of g', 'f times g with no derivatives taken at all', 'The sum of f and g with no multiplication'], 0),
   ('Why is the product rule needed instead of just multiplying the derivatives of each factor?', ['Multiplying the individual derivatives together does not give the correct derivative of the product', 'Multiplying the individual derivatives always gives the correct answer', 'The product rule is optional and never affects the result', 'Derivatives cannot be applied to any product of functions'], 0),
   ('What must you identify before applying the product rule to an expression?', ['The two separate functions being multiplied together', 'The exact numerical value of the function at one point only', 'The degree of the final derivative in advance', 'The sum of all constants in the expression'], 0),
   ('How does the product rule relate to the earlier power rule?', ['The product rule extends differentiation to products of functions, while the power rule handles a single power of x', 'The product rule replaces the power rule in every case', 'The power rule can only be used for products, never single terms', 'The two rules are entirely unrelated and never used together'], 0)]),
B('Biology: Horizontal Gene Transfer in Bacteria',
  'Grade 11 Biology strand: horizontal gene transfer is the movement of genetic material between organisms of the same generation rather than from parent to offspring, and in bacteria it occurs through transformation, transduction, and conjugation, spreading traits such as antibiotic resistance rapidly through a population.',
  [('What is horizontal gene transfer?', ['The movement of genetic material between organisms of the same generation, rather than from parent to offspring', 'The transfer of genetic material only from parent to offspring', 'A process that never occurs in bacteria', 'The complete destruction of genetic material within a cell'], 0),
   ('Name one mechanism bacteria use for horizontal gene transfer.', ['Conjugation', 'Photosynthesis', 'Meiosis exclusively', 'Mitosis exclusively'], 0),
   ('What trait can spread rapidly through a bacterial population via horizontal gene transfer?', ['Antibiotic resistance', 'Eye colour', 'Leaf shape', 'Fur pattern'], 0),
   ('How does horizontal gene transfer differ from normal vertical inheritance?', ['It moves genes between organisms of the same generation instead of from parent to offspring', 'It is identical to vertical inheritance in every way', 'It only occurs across different species of animals', 'It never involves the movement of genetic material at all'], 0),
   ('Why is horizontal gene transfer significant for public health?', ['It can spread antibiotic resistance genes quickly across a bacterial population', 'It has no connection to antibiotic resistance whatsoever', 'It only affects viruses, never bacteria', 'It eliminates the need for any antibiotics at all'], 0)]),
C('Chemistry: Zeolites and Molecular Sieves in Catalysis and Purification',
  'Grade 11 Chemistry strand: zeolites are microporous aluminosilicate minerals whose uniform, cage-like pores act as molecular sieves, selectively trapping or excluding molecules by size, which makes them useful as catalysts in industrial reactions and as agents for water and gas purification.',
  [('What type of material is a zeolite?', ['A microporous aluminosilicate mineral', 'A pure metal with no porous structure', 'A type of simple organic solvent', 'A noble gas used only in lighting'], 0),
   ('How do zeolites act as molecular sieves?', ['Their uniform, cage-like pores selectively trap or exclude molecules by size', 'They dissolve every molecule that touches them', 'They repel all molecules regardless of size', 'They have no pores of any kind'], 0),
   ('What industrial role can zeolites play beyond purification?', ['They can act as catalysts in industrial reactions', 'They can only be used as decorative building materials', 'Zeolites have no industrial applications at all', 'They function only as electrical insulators'], 0),
   ('What property of zeolites makes them useful for water purification?', ['Their pores can selectively trap contaminant molecules by size', 'They instantly evaporate any water they contact', 'They chemically convert water into a different compound', 'They have no effect on water composition at all'], 0),
   ('What structural feature gives zeolites their selective trapping ability?', ['Their uniform, cage-like pore structure', 'A complete absence of any internal structure', 'A single large cavity with no defined shape', 'A random, constantly changing pore size'], 0)]),
]),
day(142, [
E('Literature: The Fairy Tale Retelling and Revisionist Fiction',
  'Grade 11 English strand: a fairy tale retelling takes a familiar traditional story and reworks its point of view, setting, or values, often to question the original tales assumptions about gender, power, or morality, turning a childhood tale into a vehicle for adult critique.',
  [('What does a fairy tale retelling typically do to a familiar traditional story?', ['Reworks its point of view, setting, or values', 'Repeats the original story word for word with no changes', 'Removes every character from the original tale', 'Converts the tale into a strictly factual historical record'], 0),
   ('What might a revisionist fairy tale question about the original story?', ['Its assumptions about gender, power, or morality', 'The spelling of the original title only', 'The publication date of the earliest printed version', 'The number of pages in the original text'], 0),
   ('Why might an author retell a story from a minor or villainous characters point of view?', ['To reveal a perspective the original tale left out or dismissed', 'Doing so always shortens the story to a single sentence', 'Minor characters have no perspective worth exploring', 'It guarantees the retelling will be identical to the original'], 0),
   ('What effect can a revisionist retelling have on a readers view of a familiar tale?', ['It can unsettle assumptions the reader took for granted in the original', 'It always makes the reader forget the original story entirely', 'It has no effect on how the reader interprets the original', 'It proves the original tale was factually inaccurate'], 0),
   ('What genre most commonly supplies source material for these retellings?', ['Traditional fairy tales and folklore', 'Contemporary financial reports', 'Scientific lab manuals', 'Legal contracts'], 0)]),
F('Calculus: The Quotient Rule for Derivatives',
  'Grade 11 Functions strand: the quotient rule gives the derivative of one function divided by another as the derivative of the numerator times the denominator minus the numerator times the derivative of the denominator, all divided by the denominator squared.',
  [('What does the quotient rule find the derivative of?', ['One function divided by another function', 'Only the sum of two functions', 'Only a single constant term', 'Only the product of two functions'], 0),
   ('What is the denominator of the result produced by the quotient rule?', ['The original denominator function, squared', 'The original numerator function, squared', 'A constant equal to one', 'The sum of the numerator and denominator'], 0),
   ('In the quotient rule, what is subtracted in the numerator of the result?', ['The numerator function times the derivative of the denominator', 'The denominator function times itself', 'A constant with no relation to either function', 'The derivative of the numerator times the derivative of the denominator'], 0),
   ('Why cannot you simply divide the derivative of the numerator by the derivative of the denominator?', ['That shortcut does not produce the correct derivative of a quotient', 'That shortcut always produces the correct derivative of a quotient', 'Division of derivatives is undefined in every case', 'The quotient rule forbids any use of division'], 0),
   ('When might the quotient rule be especially useful in Grade 11 Functions?', ['When differentiating a rational function expressed as one polynomial divided by another', 'Only when differentiating a single constant', 'Only when no denominator is present at all', 'Only for functions with no variables'], 0)]),
B('Biology: Seed Dormancy and Germination Triggers',
  'Grade 11 Biology strand: seed dormancy is a temporary suspension of active growth that allows a seed to survive unfavourable conditions until specific environmental triggers, such as adequate moisture, suitable temperature, or exposure to light, signal that conditions are right for germination.',
  [('What is seed dormancy?', ['A temporary suspension of active growth that allows a seed to survive unfavourable conditions', 'A permanent state that a seed can never leave', 'Rapid growth that occurs immediately after a seed forms', 'The complete death of a seed embryo'], 0),
   ('Name one environmental trigger that can signal a dormant seed to germinate.', ['Adequate moisture', 'A complete absence of any water', 'Total darkness with no light at any point', 'Freezing the seed permanently'], 0),
   ('Why is seed dormancy advantageous for a plant species?', ['It lets seeds survive unfavourable conditions until conditions improve', 'It guarantees every seed will germinate immediately regardless of conditions', 'It prevents a seed from ever germinating under any circumstance', 'It has no survival advantage of any kind'], 0),
   ('What happens to a seed once the right combination of environmental triggers is present?', ['It begins to germinate', 'It enters a deeper state of permanent dormancy', 'It immediately dies', 'It reverses its development back to a single cell'], 0),
   ('How might exposure to light act as a germination trigger for certain seed species?', ['Light can signal that a seed is near the soil surface, a favourable position for a seedling to grow', 'Light always prevents germination in every seed species', 'Light has no relationship to germination in any species', 'Seeds cannot detect light in any way'], 0)]),
C('Chemistry: Ionic Liquids — Properties and Green Chemistry Applications',
  'Grade 11 Chemistry strand: an ionic liquid is a salt that remains liquid near room temperature because its bulky, asymmetric ions resist packing into a solid crystal lattice, and its negligible vapour pressure makes it attractive as a safer, less volatile solvent in green chemistry applications.',
  [('What is an ionic liquid?', ['A salt that remains liquid near room temperature', 'A gas composed entirely of neutral molecules', 'A solid metal alloy with no ionic character', 'A pure covalent compound with no charged particles'], 0),
   ('Why do ionic liquids resist forming a solid crystal lattice at room temperature?', ['Their bulky, asymmetric ions resist packing into an ordered structure', 'Their ions are perfectly symmetric and pack together instantly', 'They contain no ions of any kind', 'They are chemically identical to water'], 0),
   ('What property of ionic liquids makes them attractive as safer solvents?', ['Their negligible vapour pressure', 'Their extremely high vapour pressure', 'Their complete lack of any solvent properties', 'Their tendency to explode at room temperature'], 0),
   ('What field commonly explores ionic liquids as an alternative to volatile organic solvents?', ['Green chemistry', 'Astronomy', 'Musicology', 'Competitive athletics'], 0),
   ('Why might a low vapour pressure reduce the risk associated with a solvent?', ['It lowers the chance of harmful vapours evaporating into the surrounding air', 'A low vapour pressure always increases the risk of an explosion', 'Vapour pressure has no relationship to solvent safety', 'A low vapour pressure guarantees a solvent is edible'], 0)]),
]),
day(143, [
E('Grammar: Conditional Sentences and Hypothetical Reasoning',
  'Grade 11 English strand: conditional sentences pair an if-clause with a result clause to express real possibilities, hypothetical situations, or outcomes contrary to fact, and choosing the right conditional pattern lets a writer signal exactly how likely or how imaginary a scenario is.',
  [('What two parts make up a conditional sentence?', ['An if-clause and a result clause', 'A subject and a verb with no clause structure at all', 'Two independent clauses joined only by a semicolon', 'A question followed by a one-word answer'], 0),
   ('What does a conditional sentence about an outcome contrary to fact typically signal?', ['A hypothetical situation that did not actually happen', 'An event that is certain to happen tomorrow', 'A simple statement of present fact', 'A command directed at the reader'], 0),
   ('Why might a writer choose a conditional sentence over a direct statement?', ['To signal how likely or imaginary a scenario is rather than asserting it as fact', 'Conditional sentences always sound less formal than direct statements', 'Conditional sentences remove all meaning from a sentence', 'Direct statements are grammatically forbidden in academic writing'], 0),
   ('Which verb form commonly appears in the if-clause of a hypothetical past conditional?', ['A past perfect verb form', 'The imperative mood only', 'A future tense verb form', 'No verb at all'], 0),
   ('What kind of reasoning do conditional sentences allow a writer to express?', ['Reasoning about possible, hypothetical, or contrary-to-fact outcomes', 'Reasoning limited only to historical facts', 'Reasoning that cannot involve cause and effect', 'Reasoning expressed only through single-word exclamations'], 0)]),
F('Calculus: The Chain Rule for Composite Functions',
  'Grade 11 Functions strand: the chain rule differentiates a composite function by multiplying the derivative of the outer function, evaluated at the inner function, by the derivative of the inner function, allowing nested functions to be differentiated layer by layer.',
  [('What kind of function does the chain rule differentiate?', ['A composite function, made of one function nested inside another', 'Only a function with a single, unnested term', 'Only a constant function', 'Only a function with no variables at all'], 0),
   ('What two derivatives does the chain rule multiply together?', ['The derivative of the outer function and the derivative of the inner function', 'The derivative of the outer function and the outer function itself', 'Two unrelated constants with no connection to the function', 'The sum of the inner and outer functions'], 0),
   ('What does the phrase differentiating layer by layer describe about the chain rule?', ['Working from the outermost function inward through each nested layer', 'Differentiating only the innermost layer and ignoring the rest', 'Differentiating every layer at the exact same time with no order', 'Removing all layers before differentiating anything'], 0),
   ('Why is the chain rule essential for a function like the square of a polynomial?', ['The polynomial inside must be treated as the inner function nested inside the squaring operation', 'Squaring a polynomial never requires any nested differentiation', 'The chain rule only applies to trigonometric functions', 'The inner polynomial can always be ignored during differentiation'], 0),
   ('How does the chain rule relate to the product and quotient rules?', ['All three are differentiation techniques for combining or nesting functions, used together as needed', 'The chain rule replaces the need for the product and quotient rules entirely', 'The chain rule can only be used when no other differentiation rule applies', 'The product, quotient, and chain rules are never used in the same problem'], 0)]),
B('Biology: Cell Signaling — Ligands, Receptors, and Signal Transduction',
  'Grade 11 Biology strand: cell signaling begins when a signaling molecule called a ligand binds to a specific receptor on or in a target cell, triggering a signal transduction pathway that relays and amplifies the message inside the cell to produce a specific cellular response.',
  [('What is a ligand in the context of cell signaling?', ['A signaling molecule that binds to a specific receptor', 'A structural protein found only in the cell wall', 'A type of carbohydrate stored for energy', 'An enzyme that breaks down DNA exclusively'], 0),
   ('What does a ligand bind to on or in a target cell?', ['A specific receptor', 'Any random molecule inside the cell', 'The cell nucleus exclusively, with no receptor involved', 'Nothing, since ligands do not bind to anything'], 0),
   ('What is a signal transduction pathway?', ['A series of steps that relay and amplify a signal inside the cell', 'A pathway that immediately destroys the incoming signal', 'A structure used only for cell division', 'A pathway with no connection to cellular response'], 0),
   ('What is the end result of a completed signal transduction pathway?', ['A specific cellular response', 'The complete destruction of the target cell in every case', 'No change to the cell whatsoever', 'The permanent removal of all receptors from the cell'], 0),
   ('Why is receptor specificity important in cell signaling?', ['It ensures that a ligand triggers a response only in the appropriate target cells', 'Receptor specificity guarantees every cell responds identically to every ligand', 'Specificity has no role in determining which cells respond', 'Receptors bind to every ligand in the body equally'], 0)]),
C('Chemistry: Hydrogel Polymers and Contact Lens Chemistry',
  'Grade 11 Chemistry strand: a hydrogel is a network of cross-linked polymer chains that can absorb and retain large amounts of water while keeping its shape, a property that soft contact lenses rely on to stay flexible, permeable to oxygen, and comfortable against the eye.',
  [('What is a hydrogel?', ['A network of cross-linked polymer chains that can absorb and retain large amounts of water', 'A solid metal with no polymer content at all', 'A gas that cannot hold any water', 'A liquid solvent with no polymer structure'], 0),
   ('What property of hydrogels makes soft contact lenses flexible and comfortable?', ['Their ability to absorb and retain large amounts of water while keeping their shape', 'Their complete inability to hold any water', 'Their extremely rigid, glass-like structure', 'Their tendency to dissolve completely in the eye'], 0),
   ('What structural feature allows a hydrogel to hold its shape despite absorbing water?', ['Cross-links between its polymer chains', 'A complete absence of any polymer chains', 'A single, unbranched chain with no cross-links', 'A rigid metal frame embedded in the material'], 0),
   ('Why is oxygen permeability important for a soft contact lens material?', ['It allows oxygen to reach the surface of the eye through the lens', 'Oxygen permeability has no relevance to eye health', 'It prevents any light from passing through the lens', 'It causes the lens to dissolve upon contact with air'], 0),
   ('What class of material does a soft contact lens belong to, based on its water-absorbing polymer network?', ['A hydrogel', 'A pure metal alloy', 'A noble gas', 'An ionic crystal with no polymer content'], 0)]),
]),
day(144, [
E('Independent Reading: Climate Fiction and Environmental Storytelling',
  'Grade 11 English strand: climate fiction, often called cli-fi, imagines characters and societies confronting environmental change and its consequences, using narrative to make abstract scientific projections feel immediate, personal, and morally urgent.',
  [('What does climate fiction typically imagine?', ['Characters and societies confronting environmental change and its consequences', 'A world with no environmental concerns of any kind', 'Purely historical events with no connection to climate', 'A setting entirely disconnected from any scientific concept'], 0),
   ('What is another common name for climate fiction?', ['Cli-fi', 'Hard-boiled fiction', 'Epistolary fiction', 'Detective fiction'], 0),
   ('What effect can narrative have on abstract scientific projections about climate change?', ['It can make the projections feel immediate, personal, and morally urgent', 'It always makes scientific projections seem less believable', 'Narrative has no effect on how readers process scientific information', 'It removes any moral dimension from the topic'], 0),
   ('Why might an author set a climate fiction story in a near-future version of a real city?', ['To make the environmental consequences feel plausible and close to the readers own experience', 'Doing so guarantees the story cannot be read as fiction', 'Near-future settings remove all stakes from a narrative', 'Real cities cannot appear in works of fiction'], 0),
   ('What kind of urgency does climate fiction often aim to create in its readers?', ['A moral and emotional urgency about environmental change', 'An urgency to memorize scientific formulas', 'No urgency of any kind, since the genre is purely decorative', 'An urgency limited strictly to questions of grammar'], 0)]),
F('Discrete Math: Network Flow and the Max-Flow Min-Cut Idea',
  'Grade 11 Functions strand: a flow network models capacity-limited connections between a source and a sink, and the max-flow min-cut idea states that the greatest possible flow through the network equals the smallest total capacity of any set of edges that, if removed, would disconnect the source from the sink.',
  [('What does a flow network model?', ['Capacity-limited connections between a source and a sink', 'A network with no limits of any kind on any connection', 'A single isolated point with no connections at all', 'A network where every edge has infinite capacity'], 0),
   ('According to the max-flow min-cut idea, what does the maximum possible flow equal?', ['The smallest total capacity of any cut that disconnects the source from the sink', 'The largest total capacity of every edge in the entire network combined', 'The number of vertices in the network', 'The average capacity of all edges in the network'], 0),
   ('What is a cut in a flow network?', ['A set of edges that, if removed, disconnects the source from the sink', 'A single vertex with no edges attached', 'The entire network with no edges removed', 'A path that never reaches the sink'], 0),
   ('What two special vertices does a flow network typically identify?', ['The source and the sink', 'The maximum and minimum vertices by label only', 'Two vertices chosen completely at random each time', 'The first and last vertices added to the network historically'], 0),
   ('Why is the max-flow min-cut idea useful in applications like transportation or supply networks?', ['It identifies the bottleneck that limits the total flow through the whole network', 'It guarantees every edge in the network has identical capacity', 'It has no practical application to transportation or supply problems', 'It proves that no network can ever have a bottleneck'], 0)]),
B('Ecology: Ecological Niches and Competitive Exclusion',
  'Grade 11 Biology strand: a species ecological niche describes its full role in an ecosystem, including the resources it uses and the conditions it tolerates, and the competitive exclusion principle holds that two species cannot indefinitely occupy the exact same niche in the same habitat without one outcompeting the other.',
  [('What does a species ecological niche describe?', ['Its full role in an ecosystem, including the resources it uses and conditions it tolerates', 'Only the geographic location where a species was first discovered', 'Only the physical size of an individual organism', 'The exact number of offspring a species produces each year'], 0),
   ('What does the competitive exclusion principle state?', ['Two species cannot indefinitely occupy the exact same niche in the same habitat', 'Two species can always occupy the exact same niche forever without conflict', 'Competition between species never affects their long-term survival', 'Only predators are ever subject to competitive exclusion'], 0),
   ('What typically happens when two species compete for the exact same niche in the same habitat?', ['One species eventually outcompetes and displaces the other', 'Both species always thrive equally forever with no change', 'The habitat immediately becomes uninhabitable for both species', 'The two species instantly merge into a single species'], 0),
   ('What resources might be included as part of a species niche?', ['Food sources, habitat space, and other resources the species depends on', 'Only the colour of the species fur or feathers', 'Only the exact date the species was named by scientists', 'Nothing related to resources at all'], 0),
   ('How might two similar species avoid competitive exclusion when living in the same area?', ['By using slightly different resources or occupying slightly different niches', 'By becoming genetically identical to one another', 'By eliminating all other species from the habitat', 'Competitive exclusion cannot be avoided under any circumstance'], 0)]),
C('Chemistry: Nanoparticles and the Surface Area to Volume Effect',
  'Grade 11 Chemistry strand: as a particle shrinks toward the nanoscale, its surface area to volume ratio increases dramatically, exposing a much larger fraction of its atoms at the surface, which can make nanoparticles far more chemically reactive or catalytically active than the same mass of bulk material.',
  [('What happens to the surface area to volume ratio of a particle as it shrinks toward the nanoscale?', ['It increases dramatically', 'It decreases dramatically', 'It stays exactly the same regardless of size', 'It becomes impossible to measure'], 0),
   ('What does a higher surface area to volume ratio expose at a nanoparticles surface?', ['A much larger fraction of its atoms', 'No atoms at all, since surface atoms disappear at small sizes', 'Only the atoms located at the very center of the particle', 'An identical fraction of atoms compared to a large chunk of material'], 0),
   ('How can this increased surface exposure affect a nanoparticles chemical behaviour?', ['It can make the nanoparticle far more chemically reactive or catalytically active', 'It always makes the nanoparticle completely chemically inert', 'It has no effect on chemical reactivity whatsoever', 'It converts the nanoparticle into a different element'], 0),
   ('How does the reactivity of a nanoparticle typically compare to the same mass of bulk material?', ['The nanoparticle is often far more reactive', 'The nanoparticle is always far less reactive', 'The two are always identical in reactivity', 'Reactivity cannot be compared between different particle sizes'], 0),
   ('Why might nanoparticles be used as catalysts in industrial chemistry?', ['Their high surface area to volume ratio provides more active sites for reactions to occur', 'Nanoparticles have no surface area at all', 'Catalysts must always be as large as possible to function', 'Nanoparticles cannot participate in any chemical reaction'], 0)]),
]),
day(145, [
E('Media Literacy: Political Cartoons and the Grammar of Visual Satire',
  'Grade 11 English strand: a political cartoon compresses commentary on a public issue into symbolic imagery, exaggerated caricature, and brief text, relying on a shared visual vocabulary of labels, symbols, and irony to make a persuasive argument in a single frame.',
  [('What does a political cartoon typically compress into a single frame?', ['Commentary on a public issue using symbolic imagery and caricature', 'A complete, unabridged transcript of a news broadcast', 'A purely decorative image with no argument at all', 'A detailed scientific diagram with no commentary'], 0),
   ('What technique does a political cartoonist often use to exaggerate a public figures features?', ['Caricature', 'Verbatim quotation with no visual alteration', 'Strict photographic realism', 'Blank, empty panels with no imagery'], 0),
   ('What shared visual vocabulary do political cartoons often rely on?', ['Labels, symbols, and irony', 'Complex mathematical notation', 'Musical notation', 'Legal citations'], 0),
   ('Why might a cartoonist label an object or figure directly within the image?', ['To make the symbolic meaning of the image unambiguous to the viewer', 'Labels are required by law on every published image', 'Labels always remove all meaning from a cartoon', 'Cartoonists label images only to credit the printer'], 0),
   ('What persuasive goal does a political cartoon typically pursue?', ['Making an argument about a public issue through a single striking image', 'Presenting a perfectly neutral, opinion-free record of events', 'Avoiding any commentary on public issues whatsoever', 'Providing a complete academic bibliography'], 0)]),
F('Number Theory: Fermats Little Theorem',
  'Grade 11 Functions strand: Fermats little theorem states that if p is a prime number and a is any integer not divisible by p, then a raised to the power p minus 1 leaves a remainder of 1 when divided by p, a result used in number theory and modern cryptography.',
  [('What does Fermats little theorem require p to be?', ['A prime number', 'Any even number, prime or not', 'A negative integer only', 'A perfect square'], 0),
   ('According to Fermats little theorem, what remainder does a raised to the power p minus 1 leave when divided by p?', ['A remainder of 1', 'A remainder of 0 in every case', 'A remainder equal to p itself', 'A remainder that is always negative'], 0),
   ('What condition must the integer a satisfy for Fermats little theorem to apply?', ['a must not be divisible by p', 'a must always be exactly equal to p', 'a must always be a prime number itself', 'a must always be negative'], 0),
   ('In what modern field is Fermats little theorem applied?', ['Cryptography', 'Landscape painting', 'Musical composition', 'Competitive swimming'], 0),
   ('What branch of mathematics does Fermats little theorem belong to?', ['Number theory', 'Trigonometry exclusively', 'Coordinate geometry exclusively', 'Probability exclusively'], 0)]),
B('Biology: Blood Types and the ABO/Rh Blood Group Systems',
  'Grade 11 Biology strand: the ABO blood group system classifies blood by the presence or absence of A and B antigens on red blood cells, while the Rh system adds a positive or negative marker, and mismatched transfusions can trigger a dangerous immune reaction against foreign antigens.',
  [('What does the ABO blood group system classify?', ['Blood based on the presence or absence of A and B antigens on red blood cells', 'Blood based on its exact volume in the body', 'Blood based on the persons age at donation', 'Blood based on the persons eye colour'], 0),
   ('What does the Rh system add to a blood type classification?', ['A positive or negative marker', 'A numeric score from one to ten', 'A colour code with no biological meaning', 'An exact percentage of water content'], 0),
   ('What can happen if a person receives a transfusion of a mismatched blood type?', ['A dangerous immune reaction against the foreign antigens', 'No effect of any kind on the recipient', 'An automatic conversion of the donated blood to the recipients type', 'Immediate improvement in the recipients blood pressure only'], 0),
   ('What are antigens, in the context of the ABO blood group system?', ['Molecules on the surface of red blood cells that the immune system can recognize as foreign', 'Molecules found only in bone marrow, never on red blood cells', 'A type of white blood cell responsible for digestion', 'A hormone that regulates blood sugar'], 0),
   ('Why is blood typing important before a transfusion is given?', ['To prevent an immune reaction caused by incompatible antigens', 'Blood typing has no effect on the safety of a transfusion', 'All blood types are always compatible with one another', 'Blood typing is only relevant for organ transplants, not transfusions'], 0)]),
C('Chemistry: Transition Metal Colour and d-Orbital Electron Transitions',
  'Grade 11 Chemistry strand: many transition metal compounds appear coloured because electrons absorb specific wavelengths of visible light while jumping between split d-orbital energy levels, and the colour observed is the complement of the wavelengths absorbed, changing with the metal, its oxidation state, and the surrounding ligands.',
  [('Why do many transition metal compounds appear coloured?', ['Electrons absorb specific wavelengths of visible light while jumping between split d-orbital energy levels', 'They emit radio waves instead of visible light', 'They contain no electrons capable of absorbing light', 'Colour in transition metals has no connection to electrons at all'], 0),
   ('What is the relationship between the colour observed and the wavelengths absorbed?', ['The observed colour is the complement of the absorbed wavelengths', 'The observed colour is identical to the absorbed wavelengths', 'Absorbed wavelengths have no relationship to observed colour', 'The compound always appears completely colourless regardless of absorption'], 0),
   ('Name one factor that can change the colour of a transition metal compound.', ['The identity of the surrounding ligands', 'The compounds exact physical weight', 'The time of day the compound is observed', 'The shape of the container holding the compound'], 0),
   ('What electron transition is responsible for the colour of many transition metal compounds?', ['A transition between split d-orbital energy levels', 'A transition between two separate atomic nuclei', 'A transition that occurs only within the innermost electron shell', 'A transition that has no connection to orbital energy at all'], 0),
   ('Why might changing a metals oxidation state change the colour of its compound?', ['A different oxidation state changes the electron configuration and the d-orbital energy gaps involved', 'Oxidation state has no effect on colour in any transition metal compound', 'Oxidation state only affects the compounds mass, never its colour', 'Every oxidation state of a given metal produces an identical colour'], 0)]),
]),
day(146, [
E('Oral Communication: Vocal Delivery — Pace, Pitch, and Emphasis',
  'Grade 11 English strand: effective vocal delivery uses pace, pitch, and emphasis to shape how an audience experiences a spoken message, since varying speaking rate, raising or lowering pitch, and stressing key words can communicate meaning that the words alone do not carry.',
  [('What three vocal elements does effective delivery typically vary?', ['Pace, pitch, and emphasis', 'Font size, colour, and margin width', 'Word count, page number, and paragraph length', 'Spelling, punctuation, and citation style'], 0),
   ('What can varying speaking pace communicate to an audience?', ['A shift in urgency, importance, or emotional tone', 'Nothing at all, since pace has no communicative value', 'Only the exact time remaining in a speech', 'The speakers reading level'], 0),
   ('Why might a speaker stress a particular word in a sentence?', ['To emphasize the most important idea in that sentence', 'Stressing a word always changes its dictionary spelling', 'Emphasis has no effect on how a listener interprets a sentence', 'Every word in a sentence must receive identical stress'], 0),
   ('What can a rise or fall in vocal pitch signal to a listener?', ['A question, a shift in emotion, or a change in emphasis', 'The exact number of pages in a written script', 'A change in the color of the speakers clothing', 'Nothing measurable at all'], 0),
   ('Why is vocal delivery considered part of oral communication skill, separate from word choice?', ['How something is said can shape meaning just as much as the words themselves', 'Vocal delivery has no connection to how a message is understood', 'Word choice is the only element that ever affects meaning', 'Oral communication excludes any consideration of vocal delivery'], 0)]),
F('Statistics: The Geometric Distribution',
  'Grade 11 Functions strand: the geometric distribution models the number of independent trials needed to obtain the first success in a sequence of yes-or-no trials that each share the same probability of success, such as the number of coin flips until the first heads appears.',
  [('What does the geometric distribution model?', ['The number of independent trials needed to obtain the first success', 'The total number of successes in a fixed number of trials', 'The average value of a continuous data set', 'The exact midpoint of a data set'], 0),
   ('What must be true of the probability of success across the trials modelled by a geometric distribution?', ['It stays the same for every trial', 'It must increase after every trial', 'It must decrease after every trial', 'It must always equal exactly one half'], 0),
   ('What classic example illustrates the geometric distribution?', ['The number of coin flips until the first heads appears', 'The average height of a group of people', 'The exact sum of two dice rolled once', 'The total distance travelled by a car in one trip'], 0),
   ('What kind of trials does the geometric distribution apply to?', ['Independent yes-or-no trials with the same probability of success', 'Trials that are always dependent on the previous outcome', 'Trials with a different probability of success every time', 'Trials that can only ever succeed, never fail'], 0),
   ('How does the geometric distribution differ from the binomial distribution?', ['It counts trials until the first success rather than counting successes in a fixed number of trials', 'It applies only to continuous data, never discrete outcomes', 'It requires the probability of success to change every trial', 'It is identical to the binomial distribution in every respect'], 0)]),
B('Biology: Embryonic Development — Cleavage, Gastrulation, and Differentiation',
  'Grade 11 Biology strand: early embryonic development proceeds through cleavage, rapid cell division that partitions the fertilized egg into many smaller cells, followed by gastrulation, which establishes the three primary germ layers, and cellular differentiation, in which cells become specialized for distinct roles.',
  [('What happens during cleavage in early embryonic development?', ['Rapid cell division partitions the fertilized egg into many smaller cells', 'The embryo stops dividing entirely for an extended period', 'Specialized organs form immediately without any cell division', 'The fertilized egg is destroyed and replaced'], 0),
   ('What does gastrulation establish in a developing embryo?', ['The three primary germ layers', 'A single, undifferentiated layer of cells with no further structure', 'The adult skeletal system directly, with no intermediate stages', 'A fully formed nervous system'], 0),
   ('What is cellular differentiation?', ['The process by which cells become specialized for distinct roles', 'The process by which all cells become identical to one another', 'A process that only occurs after an organism reaches adulthood', 'The complete cessation of all cell activity'], 0),
   ('In what order do cleavage, gastrulation, and differentiation typically proceed?', ['Cleavage first, then gastrulation, then further differentiation', 'Differentiation first, followed by cleavage, then gastrulation', 'Gastrulation first, followed by differentiation, then cleavage', 'All three occur simultaneously with no particular order'], 0),
   ('Why is gastrulation considered a critical stage in embryonic development?', ['It establishes the basic body plan by forming the three germ layers that later tissues and organs develop from', 'Gastrulation has no effect on the embryos later development', 'Gastrulation only occurs in plants, not animals', 'Gastrulation permanently halts all further embryonic development'], 0)]),
C('Chemistry: Aerosols and Atmospheric Particulate Matter',
  'Grade 11 Chemistry strand: atmospheric aerosols are tiny solid or liquid particles suspended in air, produced by both natural sources such as sea spray and human activities such as combustion, and fine particulate matter can scatter sunlight, seed cloud formation, and pose serious respiratory health risks.',
  [('What are atmospheric aerosols?', ['Tiny solid or liquid particles suspended in air', 'Pure gases with no solid or liquid particles present', 'Large, visible chunks of solid rock', 'A single type of gas found only in laboratories'], 0),
   ('Name one natural source of atmospheric aerosols.', ['Sea spray', 'Only synthetic laboratory chemicals', 'Only electronic devices', 'Only underground mining equipment'], 0),
   ('Name one human activity that produces atmospheric particulate matter.', ['Combustion', 'Photosynthesis in plants', 'Simple evaporation of pure water', 'Freezing of pure water into ice'], 0),
   ('What atmospheric effect can fine particulate matter have on sunlight and clouds?', ['It can scatter sunlight and seed cloud formation', 'It has no measurable effect on sunlight or clouds', 'It permanently blocks all sunlight from reaching the ground', 'It eliminates cloud formation entirely'], 0),
   ('What health risk is associated with fine particulate matter in the air?', ['Serious respiratory health risks', 'No health risk of any kind to humans', 'Improved lung function with prolonged exposure', 'A guaranteed cure for existing respiratory disease'], 0)]),
]),
day(147, [
E('Literature: The Palimpsest — Layered Meaning in Adaptation and Revision',
  'Grade 11 English strand: a palimpsest was originally a manuscript scraped clean and reused, leaving faint traces of the earlier text beneath the new one, and literary critics use the term for any work that visibly layers a new story over an older one the reader can still sense underneath.',
  [('What was a palimpsest originally?', ['A manuscript scraped clean and reused, leaving faint traces of the earlier text beneath the new one', 'A printing press used only for legal documents', 'A type of fixed poetic form with a strict rhyme scheme', 'A modern digital file format'], 0),
   ('How do literary critics use the term palimpsest today?', ['For a work that layers a new story over an older one the reader can still sense underneath', 'For any work published in more than one language', 'For a story with absolutely no connection to earlier texts', 'For a text that has never been revised'], 0),
   ('What can a reader sense in a work described as a literary palimpsest?', ['Traces of an earlier text beneath the surface of the new one', 'A complete absence of any earlier influence', 'Only the authors handwriting style', 'The exact publication date of the earlier work'], 0),
   ('Why might an author deliberately write a palimpsestic adaptation of an older story?', ['To let readers experience the new story in dialogue with the one it is built on', 'To ensure no reader can ever recognize the earlier story', 'Adaptations are never in dialogue with their source material', 'Doing so guarantees the earlier story is erased entirely'], 0),
   ('What does the concept of a palimpsest suggest about the relationship between old and new texts?', ['That the old text can remain faintly visible beneath the new one', 'That old texts are always completely erased by new ones', 'That old and new texts can never share any thematic connection', 'That only the newest version of a story has any meaning'], 0)]),
F('Financial Mathematics: Bonds and Yield to Maturity',
  'Grade 11 Functions strand: a bond is a loan an investor makes to a government or corporation in exchange for regular interest payments and repayment of the principal at maturity, and its yield to maturity is the effective annual return an investor earns if the bond is held until it matures.',
  [('What is a bond, from an investors perspective?', ['A loan the investor makes to a government or corporation', 'A share of ownership in a company with no repayment obligation', 'A physical asset with no connection to lending', 'A type of insurance policy against loss'], 0),
   ('What does a bond issuer typically pay to the bondholder at regular intervals?', ['Interest payments', 'A single lump sum with no regular payments at all', 'Dividends tied to company profit only', 'No payments of any kind until maturity'], 0),
   ('What happens to the principal of a bond at maturity?', ['It is repaid to the bondholder', 'It is permanently forfeited by the bondholder', 'It doubles automatically regardless of terms', 'It is converted into company shares'], 0),
   ('What does yield to maturity represent?', ['The effective annual return an investor earns if the bond is held until it matures', 'The exact price the bond was originally issued at', 'The total number of years remaining before maturity', 'A fixed government tax rate applied to all bonds'], 0),
   ('Why might an investor compare the yield to maturity of different bonds before investing?', ['To evaluate which bond offers the better effective return for a similar level of risk', 'Yield to maturity has no relevance to comparing investment options', 'All bonds always have an identical yield to maturity', 'Yield to maturity only applies to bonds issued by one specific country'], 0)]),
B('Biology: Antibody Structure and the Humoral Immune Response',
  'Grade 11 Biology strand: antibodies are Y-shaped proteins produced by B cells that bind specifically to antigens on a pathogen, marking it for destruction, and this antibody-mediated defence is called the humoral immune response, distinct from the cell-mediated response carried out directly by T cells.',
  [('What shape are antibody proteins typically described as having?', ['Y-shaped', 'Perfectly spherical', 'Long and thread-like with no branching', 'Cube-shaped'], 0),
   ('What type of cell produces antibodies?', ['B cells', 'Red blood cells', 'Skin cells', 'Muscle cells'], 0),
   ('What do antibodies bind to specifically?', ['Antigens on a pathogen', 'Any random molecule in the bloodstream', 'Only molecules found in the persons own healthy tissue', 'Nothing, since antibodies do not bind to anything'], 0),
   ('What is the antibody-mediated immune defence called?', ['The humoral immune response', 'The skeletal immune response', 'The digestive immune response', 'The purely mechanical immune response'], 0),
   ('How does the humoral immune response differ from the cell-mediated response?', ['The humoral response relies on antibodies, while the cell-mediated response is carried out directly by T cells', 'The two responses are identical in every respect', 'The humoral response is carried out directly by T cells with no antibodies', 'The cell-mediated response relies entirely on antibodies'], 0)]),
C('Chemistry: Fire Retardant Chemistry and Flame-Resistant Materials',
  'Grade 11 Chemistry strand: fire retardant chemicals slow or prevent combustion by interfering with the chemical chain reactions of burning, insulating a material from heat, or releasing water and non-flammable gases that dilute oxygen at the surface, and are applied to textiles, furniture, and building materials to improve fire safety.',
  [('What is the general purpose of a fire retardant chemical?', ['To slow or prevent combustion', 'To accelerate combustion as quickly as possible', 'To eliminate all oxygen from the entire building', 'To permanently change the colour of a material with no other effect'], 0),
   ('Name one mechanism by which fire retardants can slow combustion.', ['Interfering with the chemical chain reactions of burning', 'Increasing the amount of oxygen available at the surface', 'Adding pure fuel directly to the flame', 'Removing all insulation from the material'], 0),
   ('How can a fire retardant dilute oxygen at a materials surface during a fire?', ['By releasing water and non-flammable gases', 'By releasing pure oxygen gas directly into the flame', 'By removing all water from the surrounding environment', 'By converting the material into a highly flammable gas'], 0),
   ('Name one type of material fire retardants are commonly applied to.', ['Textiles', 'Only substances that cannot burn under any circumstance', 'Only liquids with no solid surface', 'Only materials found exclusively underwater'], 0),
   ('Why might a building code require fire retardant treatment on certain furniture?', ['To improve fire safety by slowing the spread of flames', 'Fire retardants have no connection to building fire safety', 'Building codes never address furniture materials', 'Fire retardant treatment always makes furniture more flammable'], 0)]),
]),
day(148, [
E('Writing: The White Paper — Persuasive Technical Writing',
  'Grade 11 English strand: a white paper presents a detailed, evidence-based argument about a technical, policy, or business problem, combining research and data with a clear recommendation, aimed at persuading an informed reader to adopt a particular solution.',
  [('What does a white paper typically present?', ['A detailed, evidence-based argument about a technical, policy, or business problem', 'A short poem with no argument at all', 'A purely fictional narrative with invented characters', 'A single-sentence advertising slogan'], 0),
   ('What combination does a white paper rely on to build its argument?', ['Research and data combined with a clear recommendation', 'Rhyme and meter with no supporting evidence', 'Random opinions with no supporting research', 'Images alone with no written analysis'], 0),
   ('Who is the typical intended reader of a white paper?', ['An informed reader considering a technical, policy, or business decision', 'A young child with no background in the subject', 'An audience expecting only entertainment', 'A reader who never makes any decisions'], 0),
   ('What is the persuasive goal of a white paper?', ['To persuade the reader to adopt a particular solution or recommendation', 'To avoid taking any position on the problem discussed', 'To entertain the reader with an invented story', 'To summarize unrelated topics with no central argument'], 0),
   ('How does a white paper typically differ from a purely narrative essay?', ['It relies on technical evidence and a formal recommendation rather than storytelling', 'A white paper always uses rhymed verse throughout', 'A white paper never includes any data or evidence', 'A white paper is defined by having no clear topic'], 0)]),
F('Complex Numbers: The Fundamental Theorem of Algebra',
  'Grade 11 Functions strand: the fundamental theorem of algebra states that every non-constant polynomial with complex coefficients has at least one complex root, which implies that a polynomial of degree n has exactly n complex roots when counted with multiplicity.',
  [('What does the fundamental theorem of algebra guarantee for every non-constant polynomial with complex coefficients?', ['At least one complex root', 'Exactly zero roots of any kind', 'Only real roots and never complex ones', 'An infinite number of distinct roots'], 0),
   ('How many complex roots does a polynomial of degree n have, counted with multiplicity?', ['Exactly n', 'Always exactly one, regardless of degree', 'Always exactly two, regardless of degree', 'A number unrelated to the degree of the polynomial'], 0),
   ('What kind of coefficients does the fundamental theorem of algebra assume the polynomial has?', ['Complex coefficients', 'Only coefficients equal to zero', 'Only irrational coefficients', 'Coefficients that must all be prime numbers'], 0),
   ('Why is the fundamental theorem of algebra important for factoring polynomials?', ['It guarantees a polynomial can always be fully factored into linear complex factors', 'It proves that most polynomials cannot be factored at all', 'It applies only to polynomials of degree one', 'It guarantees every polynomial has zero roots'], 0),
   ('What does counting roots with multiplicity mean?', ['A repeated root is counted as many times as it repeats', 'Every root is counted only once no matter how many times it repeats', 'Multiplicity refers only to the degree of the polynomial', 'Repeated roots are excluded entirely from the count'], 0)]),
B('Biology: Bioindicator Species and Water Quality Assessment',
  'Grade 11 Biology strand: a bioindicator species is an organism whose presence, absence, or abundance reflects the health of its environment, and aquatic biologists often survey sensitive invertebrates in a stream to assess water quality without relying solely on chemical testing.',
  [('What is a bioindicator species?', ['An organism whose presence, absence, or abundance reflects the health of its environment', 'A species that has no relationship to environmental conditions', 'A species found only in laboratory settings', 'A species that only exists in fossil records'], 0),
   ('What might aquatic biologists survey in a stream to assess water quality?', ['Sensitive invertebrates', 'Only the colour of the streambed rocks', 'Only the temperature of the air above the stream', 'Only the width of the stream channel'], 0),
   ('Why are sensitive invertebrates useful as bioindicators of water quality?', ['Their presence or absence reflects pollution levels and habitat health over time', 'They have no sensitivity to pollution of any kind', 'Invertebrates never live in streams under any conditions', 'Their numbers are always constant regardless of water quality'], 0),
   ('What advantage does using a bioindicator species offer over chemical testing alone?', ['It can reflect the cumulative, long-term health of an ecosystem rather than a single moment in time', 'Bioindicators provide no information that chemical testing cannot already provide', 'Bioindicators can only be used in laboratory tanks, never in the field', 'Chemical testing is always completely unnecessary once a bioindicator is found'], 0),
   ('What might a sudden decline in a sensitive bioindicator species suggest about a stream?', ['A decline in water quality or an increase in pollution', 'An improvement in water quality with no other cause needed', 'No meaningful information about the stream at all', 'An increase in water temperature only, with no other implication'], 0)]),
C('Chemistry: The Chemistry of Invisible Ink and Redox Indicators',
  'Grade 11 Chemistry strand: many invisible inks rely on colourless organic compounds that become visible after a chemical change, such as an acid-base reaction revealed with an indicator or an oxidation reaction triggered by heat, illustrating how redox and acid-base chemistry can be used to hide and reveal a written message.',
  [('What property do many invisible ink compounds share before they are revealed?', ['They are colourless organic compounds', 'They are bright, highly visible pigments', 'They are metallic solids with no organic component', 'They glow permanently under any lighting condition'], 0),
   ('What can trigger an invisible ink message to become visible through oxidation?', ['Heat', 'Complete darkness with no light or heat applied', 'Freezing the paper solid', 'Submerging the paper in a vacuum'], 0),
   ('What type of chemical reaction can an indicator reveal in certain invisible inks?', ['An acid-base reaction', 'A nuclear fission reaction', 'A reaction with no chemical basis at all', 'A purely physical change with no chemistry involved'], 0),
   ('What does this use of invisible ink illustrate about redox and acid-base chemistry?', ['That these chemical changes can be used to hide and reveal a written message', 'That redox and acid-base chemistry have no practical applications', 'That chemical reactions can never produce a visible colour change', 'That invisible ink relies entirely on nuclear reactions'], 0),
   ('Why does heating certain invisible ink compounds reveal the hidden message?', ['Heat can trigger an oxidation reaction that produces a visible coloured compound', 'Heat destroys the paper entirely, revealing nothing', 'Heat has no chemical effect on the ink compound', 'Heat converts the ink into a completely different, unrelated substance'], 0)]),
]),
day(149, [
E('Poetry: The Concrete Poem — Visual Form and Meaning',
  'Grade 11 English strand: a concrete poem arranges its words, letters, and spacing on the page so that the poems visual shape reinforces or embodies its subject, making the physical layout of the text an active part of the poems meaning rather than a neutral container for it.',
  [('What does a concrete poem arrange to reinforce its subject?', ['Its words, letters, and spacing on the page', 'Only its rhyme scheme, with no visual arrangement', 'Only its title, with no attention to the body text', 'Only its punctuation marks, arranged alphabetically'], 0),
   ('What role does the physical layout play in a concrete poem?', ['It becomes an active part of the poems meaning', 'It is a neutral container with no effect on meaning', 'Layout is chosen entirely at random by a printer', 'Layout has no relationship to a poems subject in any form'], 0),
   ('What might a concrete poem about a tree look like on the page?', ['Its lines could be shaped to visually resemble a tree', 'It would always be printed as a plain, unbroken paragraph', 'It would contain no words related to trees at all', 'It would be identical in shape to every other poem'], 0),
   ('Why might a poet choose the concrete poem form over a conventional stanza structure?', ['The visual shape can add a layer of meaning that words alone would not convey', 'Concrete poems are required to follow strict conventional stanzas', 'Visual shape can never add meaning to a poem', 'Conventional stanza structure is forbidden in all poetry'], 0),
   ('What makes a poem count as concrete rather than purely conventional?', ['The visual arrangement of text is deliberately shaped to embody the subject', 'It is written entirely in a foreign language', 'It contains no visual arrangement of any kind', 'It is defined solely by its length in lines'], 0)]),
F('Geometry: The Dot Product and the Angle Between Vectors',
  'Grade 11 Functions strand: the dot product of two vectors is found by multiplying corresponding components and summing the results, and it relates directly to the angle between the vectors, since a dot product of zero indicates that the two vectors are perpendicular.',
  [('How is the dot product of two vectors calculated?', ['By multiplying corresponding components and summing the results', 'By dividing one vector by the other component-wise', 'By subtracting corresponding components and summing the results', 'By multiplying only the first components of each vector'], 0),
   ('What does a dot product of zero indicate about two vectors?', ['The two vectors are perpendicular', 'The two vectors are identical in every component', 'The two vectors point in exactly the same direction', 'One of the vectors must have zero magnitude'], 0),
   ('What geometric quantity does the dot product help calculate between two vectors?', ['The angle between the two vectors', 'The exact length of a completely unrelated third vector', 'The area of a circle with the same radius as one vector', 'The number of dimensions in the coordinate system'], 0),
   ('What type of quantity does a dot product produce, a scalar or a vector?', ['A scalar', 'A vector with the same direction as the first input', 'A vector perpendicular to both input vectors', 'A matrix of numbers'], 0),
   ('How does the dot product differ from the cross product introduced earlier in the vectors strand?', ['The dot product produces a scalar, while the cross product produces a vector perpendicular to both inputs', 'The dot product and the cross product always produce identical results', 'The cross product only applies to two-dimensional vectors', 'The dot product is undefined for any pair of vectors'], 0)]),
B('Biology: Prions and Protein Misfolding Disease',
  'Grade 11 Biology strand: a prion is an infectious agent made entirely of misfolded protein, with no genetic material of its own, that causes disease by inducing normal proteins in the brain to adopt the same abnormal shape, leading to progressive neurodegeneration.',
  [('What is a prion made of?', ['Misfolded protein, with no genetic material of its own', 'DNA exclusively, with no protein component', 'A complete virus particle with RNA', 'A carbohydrate molecule with no protein at all'], 0),
   ('How does a prion cause disease?', ['By inducing normal proteins to adopt the same abnormal, misfolded shape', 'By inserting its own genetic material into a host cell', 'By producing toxins that have no connection to protein shape', 'By dividing rapidly like a bacterial cell'], 0),
   ('Where in the body do prion diseases typically cause damage?', ['The brain, leading to progressive neurodegeneration', 'The fingernails, with no effect elsewhere', 'The hair follicles exclusively', 'The tooth enamel exclusively'], 0),
   ('What makes prions unusual compared to viruses and bacteria as infectious agents?', ['They contain no genetic material and are made entirely of misfolded protein', 'They contain more genetic material than any virus or bacterium', 'They are visible to the naked eye, unlike viruses and bacteria', 'They can only infect plant cells, never animal cells'], 0),
   ('What happens to normal proteins when they come into contact with a prion?', ['They can be induced to misfold into the same abnormal shape', 'They immediately destroy the prion on contact', 'They are completely unaffected by any contact with a prion', 'They convert the prion back into a normal, correctly folded protein'], 0)]),
C('Chemistry: Piezoelectric Materials and Mechanical-Electrical Energy Conversion',
  'Grade 11 Chemistry strand: piezoelectric materials generate an electric charge when mechanically stressed, because deforming their crystal structure shifts the internal distribution of positive and negative charge, a reversible effect also used to convert an applied voltage back into precise mechanical motion.',
  [('What happens when a piezoelectric material is mechanically stressed?', ['It generates an electric charge', 'It instantly melts into a liquid', 'It becomes chemically inert with no further reactivity', 'It loses all of its mass'], 0),
   ('What internal change in a piezoelectric material produces the electric charge?', ['Deforming its crystal structure shifts the internal distribution of positive and negative charge', 'The material spontaneously changes into a different element', 'All electrons are permanently removed from the material', 'The materials temperature drops to absolute zero'], 0),
   ('Is the piezoelectric effect reversible?', ['Yes, an applied voltage can be converted back into precise mechanical motion', 'No, the piezoelectric effect can only occur in one direction', 'No, piezoelectric materials cannot respond to any applied voltage', 'Yes, but only when the material is completely destroyed first'], 0),
   ('What kind of energy conversion does a piezoelectric material perform?', ['Mechanical to electrical energy conversion, and the reverse', 'Only conversion between two different chemical elements', 'Only conversion of light energy into sound energy', 'No energy conversion of any kind'], 0),
   ('What structural property must a piezoelectric material have for this effect to occur?', ['A crystal structure whose charge distribution shifts when deformed', 'A completely amorphous structure with no crystal order', 'A structure with no internal charge distribution at all', 'A structure that cannot be deformed under any stress'], 0)]),
]),
day(150, [
E('English Review: Fixed Forms, Revision, and Persuasive Voice',
  'Grade 11 English strand review: students revisit the sestina, fairy tale retellings, conditional sentences, climate fiction, political cartoons, vocal delivery, the palimpsest, the white paper, and the concrete poem.',
  [('What defines a sestina?', ['A fixed 39-line poem that repeats six end-words in a rotating pattern across six stanzas plus an envoi', 'A poem with no fixed length or repeated words', 'A poem written entirely in prose', 'A single rhymed couplet repeated indefinitely'], 0),
   ('What does a fairy tale retelling typically do to a familiar traditional story?', ['Reworks its point of view, setting, or values', 'Repeats the original story word for word with no changes', 'Removes every character from the original tale', 'Converts the tale into a strictly factual historical record'], 0),
   ('What does climate fiction typically imagine?', ['Characters and societies confronting environmental change and its consequences', 'A world with no environmental concerns of any kind', 'Purely historical events with no connection to climate', 'A setting entirely disconnected from any scientific concept'], 0),
   ('What does a political cartoon typically compress into a single frame?', ['Commentary on a public issue using symbolic imagery and caricature', 'A complete, unabridged transcript of a news broadcast', 'A purely decorative image with no argument at all', 'A detailed scientific diagram with no commentary'], 0),
   ('What does a concrete poem arrange to reinforce its subject?', ['Its words, letters, and spacing on the page', 'Only its rhyme scheme, with no visual arrangement', 'Only its title, with no attention to the body text', 'Only its punctuation marks, arranged alphabetically'], 0)]),
F('Functions Review: Derivative Rules, Networks, and Number Theory',
  'Grade 11 Functions strand review: students revisit the product rule, the quotient rule, the chain rule, network flow and max-flow min-cut, Fermats little theorem, the geometric distribution, bonds and yield to maturity, the fundamental theorem of algebra, and the dot product.',
  [('What does the product rule let you differentiate?', ['A product of two functions, without expanding the product first', 'Only a single function with no multiplication involved', 'Only the sum of two functions', 'Only a function divided by a constant'], 0),
   ('What kind of function does the chain rule differentiate?', ['A composite function, made of one function nested inside another', 'Only a function with a single, unnested term', 'Only a constant function', 'Only a function with no variables at all'], 0),
   ('What does a flow network model?', ['Capacity-limited connections between a source and a sink', 'A network with no limits of any kind on any connection', 'A single isolated point with no connections at all', 'A network where every edge has infinite capacity'], 0),
   ('What does Fermats little theorem require p to be?', ['A prime number', 'Any even number, prime or not', 'A negative integer only', 'A perfect square'], 0),
   ('How is the dot product of two vectors calculated?', ['By multiplying corresponding components and summing the results', 'By dividing one vector by the other component-wise', 'By subtracting corresponding components and summing the results', 'By multiplying only the first components of each vector'], 0)]),
B('Biology Review: Gene Transfer, Development, and Immunity',
  'Grade 11 Biology strand review: students revisit horizontal gene transfer, seed dormancy, cell signaling, ecological niches, ABO and Rh blood types, embryonic development, antibody structure, bioindicator species, and prions.',
  [('What is horizontal gene transfer?', ['The movement of genetic material between organisms of the same generation, rather than from parent to offspring', 'The transfer of genetic material only from parent to offspring', 'A process that never occurs in bacteria', 'The complete destruction of genetic material within a cell'], 0),
   ('What is a ligand in the context of cell signaling?', ['A signaling molecule that binds to a specific receptor', 'A structural protein found only in the cell wall', 'A type of carbohydrate stored for energy', 'An enzyme that breaks down DNA exclusively'], 0),
   ('What does a species ecological niche describe?', ['Its full role in an ecosystem, including the resources it uses and conditions it tolerates', 'Only the geographic location where a species was first discovered', 'Only the physical size of an individual organism', 'The exact number of offspring a species produces each year'], 0),
   ('What happens during cleavage in early embryonic development?', ['Rapid cell division partitions the fertilized egg into many smaller cells', 'The embryo stops dividing entirely for an extended period', 'Specialized organs form immediately without any cell division', 'The fertilized egg is destroyed and replaced'], 0),
   ('What is a prion made of?', ['Misfolded protein, with no genetic material of its own', 'DNA exclusively, with no protein component', 'A complete virus particle with RNA', 'A carbohydrate molecule with no protein at all'], 0)]),
C('Chemistry Review: Zeolites, Nanomaterials, and Colour Chemistry',
  'Grade 11 Chemistry strand review: students revisit zeolites, ionic liquids, hydrogel polymers, nanoparticles and surface area effects, transition metal colour, atmospheric aerosols, fire retardant chemistry, invisible ink redox chemistry, and piezoelectric materials.',
  [('What type of material is a zeolite?', ['A microporous aluminosilicate mineral', 'A pure metal with no porous structure', 'A type of simple organic solvent', 'A noble gas used only in lighting'], 0),
   ('What happens to the surface area to volume ratio of a particle as it shrinks toward the nanoscale?', ['It increases dramatically', 'It decreases dramatically', 'It stays exactly the same regardless of size', 'It becomes impossible to measure'], 0),
   ('Why do many transition metal compounds appear coloured?', ['Electrons absorb specific wavelengths of visible light while jumping between split d-orbital energy levels', 'They emit radio waves instead of visible light', 'They contain no electrons capable of absorbing light', 'Colour in transition metals has no connection to electrons at all'], 0),
   ('What is the general purpose of a fire retardant chemical?', ['To slow or prevent combustion', 'To accelerate combustion as quickly as possible', 'To eliminate all oxygen from the entire building', 'To permanently change the colour of a material with no other effect'], 0),
   ('What happens when a piezoelectric material is mechanically stressed?', ['It generates an electric charge', 'It instantly melts into a liquid', 'It becomes chemically inert with no further reactivity', 'It loses all of its mass'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_141_150)
    append_to(11, g11_141_150)
