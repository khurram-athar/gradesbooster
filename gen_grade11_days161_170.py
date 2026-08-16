#!/usr/bin/env python3
"""Grade 11, Days 161-170 -- extends Grade 11 from 160 to 170 days. Topics
chosen after dumping the existing Day 1-160 title list (data/grade11.json)
in full and cross-checking against it to avoid any overlap: the haiku and
tanka, verbals (gerunds, participles, infinitives), the family saga novel,
photo manipulation and digital image ethics, the panel discussion, the
proposal argument, blank verse and iambic pentameter, stage directions, and
the serial novel; higher-order derivatives, curve sketching with the first
and second derivative tests, generating functions, perfect and amicable
numbers, currency exchange and arbitrage, the equation of a sphere, complex
conjugates, Boolean algebra and logic gates, and the F-distribution;
grassland and savanna ecosystems, the liver and detoxification,
nondisjunction and aneuploidy, biofilms and bacterial communities, sexual
selection, mycorrhizal associations, sleep architecture, protein structure
(primary/secondary/tertiary/quaternary), and genetic bottlenecks; caffeine
and alkaloid extraction, chewing gum polymer chemistry, water electrolysis
and hydrogen fuel, tattoo ink pigment chemistry, radiopharmaceuticals,
chocolate tempering and cocoa butter crystals, triboelectric charging and
static electricity, molecular gastronomy and spherification, and blood
buffering and pH homeostasis. Every one of these topics was verified
against the full Day 1-160 title dump and does not repeat any earlier day.
Day 170 is a lighter cross-subject review day, matching the structure of
the Day 150 and Day 160 review days (one review lesson per subject, each
reusing five first-questions verbatim from the batch, drawn from Days 161,
163, 165, 167, and 169).

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


def _rebalance_answer_positions(days, seed=20260816):
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


g11_161_170 = [
day(161, [
E('Poetry: The Haiku and Tanka — Compression and Natural Imagery',
  'Grade 11 English strand: a haiku is a compressed three-line poetic form built around a fixed syllable pattern and a single vivid image drawn from nature, while a tanka extends the same tradition to five lines and adds a personal or emotional turn after the natural image has been established.',
  [('What structural feature defines a haiku?', ['A compressed three-line form built around a single natural image', 'A twelve-line form with no fixed structure at all', 'A rhymed couplet describing an urban skyline', 'A form that forbids any reference to nature'], 0),
   ('How many lines does a tanka typically have?', ['Five lines', 'Two lines', 'Fourteen lines', 'A tanka has no fixed number of lines at all'], 0),
   ('What often follows the natural image in a tanka that a haiku does not usually include?', ['A personal or emotional turn', 'A second, unrelated natural image with no connection to the first', 'A list of historical dates', 'A formal legal argument'], 0),
   ('Why might a poet choose the compressed form of a haiku to describe a single moment?', ['The brevity forces the poet to distill the moment to its most essential image', 'A longer form always captures a moment more effectively than a short one', 'Compression removes all imagery from a poem', 'Haiku are required to describe multiple unrelated moments at once'], 0),
   ('What poetic tradition do both the haiku and the tanka descend from?', ['A Japanese poetic tradition centered on natural imagery', 'A tradition with no connection to nature imagery', 'An ancient Roman tradition of epic verse', 'A tradition that forbids any fixed syllable pattern'], 0)]),
F('Calculus: Higher-Order Derivatives and Rates of Change of Rates of Change',
  'Grade 11 Functions strand: a higher-order derivative is found by differentiating a function more than once, so the third derivative measures how the rate of change of the rate of change is itself changing, and higher-order derivatives reveal increasingly subtle features of a functions behaviour beyond slope and concavity.',
  [('How is a higher-order derivative found?', ['By differentiating a function more than once', 'By integrating a function a single time', 'By setting the function equal to zero and solving', 'By graphing the function with no further calculation'], 0),
   ('What does the third derivative of a function measure?', ['How the rate of change of the rate of change is itself changing', 'The exact y-intercept of the original function', 'The total area under the original curve', 'A quantity with no relationship to the original function'], 0),
   ('What do higher-order derivatives reveal beyond slope and concavity?', ['Increasingly subtle features of a functions behaviour', 'Nothing beyond what the first derivative already shows', 'Only the colour of the functions graph', 'The exact domain of the original function'], 0),
   ('What is another name for the second derivative of a position function in physics?', ['Acceleration', 'Velocity', 'Displacement', 'Momentum, with no connection to the second derivative'], 0),
   ('Why might an engineer care about the third derivative of a position function, sometimes called jerk?', ['It measures how abruptly acceleration itself is changing, which affects comfort and mechanical stress', 'The third derivative has no physical meaning of any kind', 'It measures only the total distance travelled', 'It replaces the need to know velocity or acceleration entirely'], 0)]),
B('Ecology: Grassland and Savanna Ecosystems',
  'Grade 11 Biology strand: grassland and savanna ecosystems are dominated by grasses with scattered trees or none at all, shaped by seasonal rainfall, periodic fire, and grazing pressure that together prevent woody plants from overtaking the landscape and maintain the open structure characteristic of these biomes.',
  [('What plant type dominates grassland and savanna ecosystems?', ['Grasses', 'Coniferous trees exclusively', 'Mosses and lichens exclusively', 'Coral and other marine organisms'], 0),
   ('Name one factor that helps maintain the open structure of a savanna.', ['Periodic fire', 'Total absence of any rainfall year-round', 'Permanent ice cover', 'Complete absence of any grazing animals'], 0),
   ('What role does grazing pressure play in a grassland ecosystem?', ['It helps prevent woody plants from overtaking the landscape', 'It has no effect on the balance between grasses and trees', 'It guarantees that trees will always dominate the landscape', 'It eliminates all grasses from the ecosystem entirely'], 0),
   ('What pattern of rainfall typically shapes a savanna ecosystem?', ['A seasonal pattern with distinct wet and dry periods', 'Constant, unvarying rainfall every day of the year', 'A complete absence of rainfall in every season', 'Rainfall that occurs only as snow'], 0),
   ('Why do scattered trees rather than dense forest typically characterize a savanna?', ['Fire, grazing, and seasonal drought limit the growth of woody plants', 'Savannas receive more rainfall than any rainforest', 'Trees are entirely absent from every savanna on Earth', 'Grazing animals always promote dense forest growth'], 0)]),
C('Chemistry: Caffeine and Alkaloid Extraction Chemistry',
  'Grade 11 Chemistry strand: caffeine is a naturally occurring alkaloid, a nitrogen-containing organic compound, and its extraction from coffee beans or tea leaves typically relies on differences in solubility between polar water and a nonpolar solvent to separate caffeine from the other plant compounds surrounding it.',
  [('What class of organic compound is caffeine?', ['An alkaloid', 'A noble gas', 'A pure metal', 'An ionic salt with no carbon present'], 0),
   ('What element, in addition to carbon, defines an alkaloid such as caffeine?', ['Nitrogen', 'Helium', 'Argon', 'Pure sodium metal'], 0),
   ('What property difference is often exploited to extract caffeine from plant material?', ['Differences in solubility between a polar and a nonpolar solvent', 'Differences in colour alone, with no chemical basis', 'Differences in electrical conductivity of solid metals', 'Differences in radioactive decay rate'], 0),
   ('Why is a nonpolar solvent often useful in caffeine extraction?', ['It can selectively dissolve caffeine while leaving many polar plant compounds behind', 'It dissolves every compound in the plant material equally', 'It reacts explosively with caffeine and destroys it', 'It has no ability to dissolve any organic compound'], 0),
   ('What kind of source is caffeine naturally extracted from?', ['Coffee beans or tea leaves', 'Pure quartz crystal', 'Distilled water with no plant material present', 'A sample of inert noble gas'], 0)]),
]),
day(162, [
E('Grammar: Verbals — Gerunds, Participles, and Infinitives in Complex Sentences',
  'Grade 11 English strand: a verbal is a verb form that functions as another part of speech, so a gerund acts as a noun, a participle acts as an adjective, and an infinitive can act as a noun, adjective, or adverb, letting a writer pack additional action into a sentence without adding a full clause.',
  [('What is a verbal?', ['A verb form that functions as another part of speech', 'A verb that can never appear in a sentence', 'A noun that has been converted into a proper adjective', 'A punctuation mark used only in dialogue'], 0),
   ('What part of speech does a gerund function as?', ['A noun', 'A preposition', 'A conjunction', 'An interjection with no grammatical function'], 0),
   ('What part of speech does a participle typically function as?', ['An adjective', 'A pronoun', 'A coordinating conjunction', 'A verbal with no descriptive function at all'], 0),
   ('What roles can an infinitive play in a sentence?', ['A noun, an adjective, or an adverb', 'Only a preposition, never anything else', 'Only a proper noun', 'No grammatical role of any kind'], 0),
   ('Why might a writer use a verbal phrase instead of a full clause?', ['To pack additional action into a sentence without adding a separate clause', 'Verbals always make a sentence longer and less clear', 'Verbals are forbidden in formal academic writing', 'A verbal phrase always changes the tense of the entire sentence'], 0)]),
F('Calculus: Curve Sketching Using the First and Second Derivative Tests',
  'Grade 11 Functions strand: curve sketching combines the first derivative test, which locates local maxima and minima by tracking where a function changes from increasing to decreasing or back, with the second derivative test, which confirms concavity, to build an accurate picture of a functions shape without plotting every point.',
  [('What does the first derivative test locate?', ['Local maxima and minima', 'The exact y-intercept of a function', 'The total area under a curve', 'The colour of a functions graph'], 0),
   ('What does the first derivative test track to identify a local maximum or minimum?', ['Where a function changes from increasing to decreasing or back', 'Where a function remains completely constant forever', 'Where a function is undefined at every point', 'Where the y-intercept crosses the x-axis'], 0),
   ('What does the second derivative test confirm about a critical point?', ['Its concavity', 'The exact numerical value of the function at that point', 'The total number of terms in the function', 'The colour of the point on a graph'], 0),
   ('Why is curve sketching useful compared to plotting every point on a graph?', ['It builds an accurate picture of a functions shape using key features rather than exhaustive plotting', 'Plotting every point is always faster than curve sketching', 'Curve sketching removes the need to know anything about a function', 'Curve sketching only works for functions with no derivative'], 0),
   ('What combination of tools does curve sketching typically rely on?', ['The first and second derivative tests together', 'Only a ruler and no calculus at all', 'A single derivative test used in isolation with no other information', 'A test that ignores concavity entirely'], 0)]),
B('Physiology: The Liver — Detoxification and Metabolic Functions',
  'Grade 11 Biology strand: the liver filters blood arriving from the digestive tract, breaking down or neutralizing toxins and metabolic waste products, storing glucose as glycogen, and producing bile that aids in the digestion and absorption of dietary fats, making it central to both detoxification and metabolism.',
  [('What does the liver do to blood arriving from the digestive tract?', ['Filters it, breaking down or neutralizing toxins', 'Immediately discards it without any filtration', 'Converts it directly into bone tissue', 'Has no effect on blood arriving from digestion'], 0),
   ('What form of stored energy does the liver produce from glucose?', ['Glycogen', 'Pure oxygen gas', 'Bone marrow', 'A form of stored energy that does not exist'], 0),
   ('What substance does the liver produce to aid in fat digestion?', ['Bile', 'Insulin exclusively', 'Stomach acid exclusively', 'A substance with no role in digestion'], 0),
   ('Why is the liver considered central to detoxification?', ['It breaks down or neutralizes toxins and metabolic waste products', 'It has no ability to interact with toxins of any kind', 'It only processes water, with no role in toxin removal', 'Detoxification occurs exclusively in the lungs, not the liver'], 0),
   ('What happens to bile after the liver produces it?', ['It aids in the digestion and absorption of dietary fats', 'It is immediately expelled from the body with no further use', 'It converts directly into glucose for storage', 'It has no connection to the digestive process'], 0)]),
C('Chemistry: The Chemistry of Chewing Gum — Polymer Base and Flavour Release',
  'Grade 11 Chemistry strand: chewing gum consists of an insoluble polymer base that remains chewable because it does not dissolve in saliva, combined with soluble sugars, flavour compounds, and softeners that dissolve and diffuse out during chewing, which is why sweetness and flavour fade well before the gum itself breaks down.',
  [('Why does the base of chewing gum remain chewable rather than dissolving?', ['The polymer base is insoluble in saliva', 'The polymer base dissolves instantly in saliva', 'Chewing gum contains no polymer of any kind', 'Saliva has no interaction with the gum base at all'], 0),
   ('What happens to the soluble sugars and flavour compounds in gum during chewing?', ['They dissolve and diffuse out of the gum', 'They become permanently locked inside the polymer base', 'They convert into an insoluble solid', 'They have no interaction with saliva whatsoever'], 0),
   ('Why does the flavour of chewing gum fade before the gum itself breaks down?', ['The soluble flavour compounds leave the gum well before the insoluble polymer base does', 'The polymer base dissolves first, before any flavour is released', 'Flavour compounds and the polymer base leave the gum at the exact same rate', 'Chewing gum releases no flavour compounds at any point'], 0),
   ('What type of material forms the base of chewing gum?', ['An insoluble polymer', 'A pure ionic salt', 'A block of solid metal', 'A sample of liquid mercury'], 0),
   ('What role do softeners play in a chewing gum formulation?', ['They help keep the polymer base pliable and chewable', 'They cause the polymer base to become instantly rigid', 'They dissolve the polymer base completely within seconds', 'They have no functional role in the gum formulation'], 0)]),
]),
day(163, [
E('Literature: The Family Saga Novel Across Generations',
  'Grade 11 English strand: a family saga novel traces a family across multiple generations, following how inherited wealth, trauma, tradition, or ambition are passed down and reshaped by each successive generation, using the family itself as a lens for exploring broader historical and social change.',
  [('What does a family saga novel typically trace?', ['A family across multiple generations', 'A single character across a single afternoon', 'A nation with no reference to any individual family', 'A single generation with no reference to the past or future'], 0),
   ('What might a family saga novel show being passed down across generations?', ['Inherited wealth, trauma, tradition, or ambition', 'Nothing at all, since generations are treated as unconnected', 'Only the exact same physical house, with no other inheritance', 'A single unchanging opinion shared by every character'], 0),
   ('What does a family saga novel often use the family as a lens for exploring?', ['Broader historical and social change', 'A single isolated event with no wider significance', 'A topic entirely unrelated to any family member', 'A subject that has no connection to history or society'], 0),
   ('Why might a family saga novel shift focus between different generations?', ['To show how patterns, conflicts, or values are reshaped over time', 'Shifting between generations is forbidden in this novel form', 'A family saga must remain fixed on a single generation only', 'Generational shifts always remove any sense of continuity'], 0),
   ('What structural feature distinguishes a family saga from a novel focused on a single protagonist?', ['Its broader scope across multiple generations of one family', 'A complete absence of any named characters', 'A refusal to include any family relationships at all', 'A structure limited to a single day of events'], 0)]),
F('Discrete Math: An Introduction to Generating Functions',
  'Grade 11 Functions strand: a generating function encodes an entire sequence of numbers as the coefficients of a single power series, turning problems about counting or recurrence relations into problems about algebraic manipulation of that series, a technique that connects discrete sequences to continuous algebraic tools.',
  [('What does a generating function encode?', ['An entire sequence of numbers as the coefficients of a power series', 'A single isolated number with no connection to any sequence', 'The exact colour of a graph', 'A sequence that has no numerical values at all'], 0),
   ('What kind of mathematical object is a generating function built from?', ['A power series', 'A single linear equation with no series involved', 'A geometric shape with no algebraic description', 'A matrix with only zero entries'], 0),
   ('What kinds of problems can generating functions help turn into algebraic manipulation?', ['Problems about counting or recurrence relations', 'Problems with no numerical content of any kind', 'Only problems involving geometric shapes', 'Problems that have already been fully solved with no further work needed'], 0),
   ('What broader connection do generating functions illustrate?', ['A connection between discrete sequences and continuous algebraic tools', 'A connection between two entirely unrelated fields with no mathematical link', 'A connection that proves discrete sequences do not exist', 'A connection limited only to geometry, with no algebra involved'], 0),
   ('Why might a generating function make a recurrence relation easier to analyze?', ['It converts the recurrence into an algebraic equation involving the power series', 'It removes all information about the original sequence', 'It makes the recurrence relation impossible to solve', 'It has no relationship to recurrence relations at all'], 0)]),
B('Genetics: Nondisjunction and Aneuploidy',
  'Grade 11 Biology strand: nondisjunction occurs when chromosomes fail to separate properly during meiosis, producing gametes with an abnormal number of chromosomes, and when such a gamete is fertilized, the resulting condition, called aneuploidy, can lead to a chromosome count that differs from the typical number for the species.',
  [('What is nondisjunction?', ['A failure of chromosomes to separate properly during meiosis', 'A perfectly normal separation of chromosomes during meiosis', 'A process that occurs only during mitosis, never meiosis', 'A process with no connection to chromosome number at all'], 0),
   ('What does nondisjunction produce in the resulting gametes?', ['An abnormal number of chromosomes', 'A perfectly normal, typical chromosome number in every case', 'Gametes with no chromosomes at all', 'Gametes that are genetically identical to the parent cell'], 0),
   ('What is aneuploidy?', ['A condition in which a chromosome count differs from the typical number for the species', 'A condition in which every chromosome count is identical across all species', 'A condition that has no relationship to chromosome number', 'A condition found only in single-celled organisms'], 0),
   ('When does nondisjunction occur in the cell cycle?', ['During meiosis, when chromosomes are meant to separate', 'Only after fertilization has already occurred', 'Only in cells that never divide at all', 'During a process unrelated to cell division'], 0),
   ('How can a gamete affected by nondisjunction lead to aneuploidy in offspring?', ['If it is fertilized, the resulting individual inherits an abnormal chromosome number', 'Fertilization always corrects any abnormal chromosome number automatically', 'Nondisjunction has no possible effect on offspring', 'Aneuploidy can only occur without any fertilization taking place'], 0)]),
C('Chemistry: Water Electrolysis and Hydrogen as a Fuel Source',
  'Grade 11 Chemistry strand: electrolysis of water uses an electric current to split water molecules into hydrogen gas at the cathode and oxygen gas at the anode, and the hydrogen produced can later be recombined with oxygen in a fuel cell to release energy, making water electrolysis a route to storing electrical energy as chemical fuel.',
  [('What does electrolysis of water use to split water molecules?', ['An electric current', 'A stream of pressurized air with no electric current', 'Gravity alone, with no external energy input', 'A magnetic field with no current involved'], 0),
   ('What gas is produced at the cathode during water electrolysis?', ['Hydrogen gas', 'Oxygen gas', 'Nitrogen gas', 'Chlorine gas exclusively'], 0),
   ('What gas is produced at the anode during water electrolysis?', ['Oxygen gas', 'Hydrogen gas', 'Helium gas', 'Argon gas exclusively'], 0),
   ('How can hydrogen produced by electrolysis later release energy?', ['By recombining with oxygen in a fuel cell', 'By being permanently stored with no further chemical use', 'By converting directly into a solid metal', 'Hydrogen produced this way cannot release any energy'], 0),
   ('Why is water electrolysis considered a way to store electrical energy?', ['It converts electrical energy into chemical energy stored in hydrogen fuel', 'It destroys electrical energy with no useful product remaining', 'It converts water directly into electricity with no intermediate step', 'Electrolysis has no connection to energy storage of any kind'], 0)]),
]),
day(164, [
E('Media Literacy: Photo Manipulation and the Ethics of the Digital Image',
  'Grade 11 English strand: digital editing tools make it possible to alter a photograph in ways that are difficult for a viewer to detect, from removing an object to reshaping a persons body, raising ethical questions about how much manipulation a viewer should expect and when an altered image crosses from enhancement into deception.',
  [('What do digital editing tools make possible with a photograph?', ['Altering it in ways that are difficult for a viewer to detect', 'Nothing at all, since digital photographs cannot be altered', 'Only converting a photograph into black and white', 'Restoring a photograph to a state that never existed in the original scene, but only by accident'], 0),
   ('Give an example of a photo manipulation mentioned as a concern.', ['Reshaping a persons body', 'Printing the photograph on paper', 'Placing the photograph in a frame', 'Taking the photograph in the first place'], 0),
   ('What ethical question does photo manipulation raise?', ['When an altered image crosses from enhancement into deception', 'Whether cameras should be banned from all public spaces', 'Whether photographs should always be printed in black and white', 'Whether editing software should be entirely free of charge'], 0),
   ('Why might undetectable photo manipulation be more ethically concerning than obvious manipulation?', ['A viewer may accept a misleading image as accurate reality without realizing it was altered', 'Undetectable manipulation always makes an image more accurate', 'Viewers can always tell instantly when any image has been edited', 'Manipulation that is easy to detect is more deceptive than manipulation that is not'], 0),
   ('What does the line between enhancement and deception in photo editing depend on?', ['What the viewer reasonably expects the image to represent', 'A rule that applies identically to every image with no exceptions', 'Nothing at all, since all editing is equally acceptable', 'The physical size of the printed photograph'], 0)]),
F('Number Theory: Perfect Numbers and Amicable Numbers',
  'Grade 11 Functions strand: a perfect number equals the sum of its proper divisors, as with six, which equals one plus two plus three, while a pair of amicable numbers consists of two different numbers, each of which equals the sum of the proper divisors of the other, a relationship known since antiquity.',
  [('What defines a perfect number?', ['It equals the sum of its proper divisors', 'It has no divisors of any kind other than itself', 'It is always an odd number with no exceptions', 'It equals the product, not the sum, of its proper divisors'], 0),
   ('What are the proper divisors of six that make it a perfect number?', ['One, two, and three', 'Six and twelve', 'Only the number six itself', 'Two and four'], 0),
   ('What defines a pair of amicable numbers?', ['Each number equals the sum of the proper divisors of the other', 'Both numbers must be identical to each other', 'Neither number can have any divisors at all', 'Each number equals its own square root'], 0),
   ('How long has the concept of amicable numbers been studied?', ['Since antiquity', 'Only since the twenty-first century', 'Amicable numbers have never been studied at any point in history', 'Only within the last decade'], 0),
   ('What operation is used to test whether a number is perfect?', ['Summing its proper divisors and comparing the sum to the number itself', 'Multiplying the number by itself', 'Dividing the number by zero', 'Comparing the number to every prime number simultaneously'], 0)]),
B('Microbiology: Biofilms and Bacterial Communities',
  'Grade 11 Biology strand: a biofilm forms when bacteria attach to a surface and secrete a protective matrix of extracellular material, creating a structured community that is often far more resistant to antibiotics and disinfectants than the same bacteria would be if they were free-floating and isolated.',
  [('What happens when bacteria form a biofilm?', ['They attach to a surface and secrete a protective matrix', 'They immediately die upon contact with any surface', 'They convert entirely into a different species', 'They lose the ability to reproduce in any way'], 0),
   ('What does the protective matrix in a biofilm consist of?', ['Extracellular material secreted by the bacteria', 'A layer of pure metal with no biological origin', 'A vacuum with no material present at all', 'A single bacterial cell wall with nothing surrounding it'], 0),
   ('How does bacterial resistance in a biofilm typically compare to free-floating bacteria?', ['Biofilm bacteria are often far more resistant to antibiotics and disinfectants', 'Biofilm bacteria are always less resistant than free-floating bacteria', 'Resistance is identical whether bacteria are in a biofilm or free-floating', 'Biofilms eliminate any need for bacteria to resist anything'], 0),
   ('What structural quality distinguishes a biofilm from a random scattering of bacteria?', ['Its organized, structured community held together by a protective matrix', 'A complete absence of any organization among the bacteria present', 'The fact that a biofilm contains no bacteria at all', 'A structure that dissolves instantly upon formation'], 0),
   ('Why might biofilms be a significant concern in medical settings?', ['Their resistance to antibiotics and disinfectants can make bacterial infections harder to treat', 'Biofilms have no relevance to human health in any setting', 'Biofilms always make bacteria easier to eliminate with standard antibiotics', 'Medical settings are entirely free of any bacterial biofilms'], 0)]),
C('Chemistry: The Chemistry of Tattoo Ink and Pigment Permanence in Skin',
  'Grade 11 Chemistry strand: tattoo ink consists of insoluble pigment particles suspended in a carrier liquid, and once injected into the dermis these particles are too large for the bodys immune cells to fully remove, allowing the pigment to remain visible beneath the skin for years or decades.',
  [('What are the pigment particles in tattoo ink suspended in?', ['A carrier liquid', 'A block of solid metal', 'A sample of pure gas', 'Nothing, since tattoo ink contains no carrier at all'], 0),
   ('Why does tattoo pigment remain visible in skin for years or decades?', ['The pigment particles are too large for immune cells to fully remove', 'The pigment particles dissolve completely within a few days', 'Immune cells have no interaction with tattoo pigment at all', 'The pigment particles are smaller than a single atom'], 0),
   ('Where in the skin is tattoo ink typically deposited?', ['The dermis', 'The outermost layer of dead skin cells only', 'A layer entirely outside the body', 'Muscle tissue beneath the skin, never the skin itself'], 0),
   ('What property of tattoo pigment particles makes them resist dissolving in the body?', ['Their insolubility', 'Their extremely high solubility in water', 'Their complete lack of any physical structure', 'Their tendency to evaporate rapidly at body temperature'], 0),
   ('What role do the bodys immune cells play in relation to tattoo pigment?', ['They attempt to remove the pigment but cannot fully clear particles that are too large', 'They completely and instantly remove all tattoo pigment', 'They have no interaction whatsoever with foreign particles in the skin', 'They convert the pigment into a different colour entirely'], 0)]),
]),
day(165, [
E('Oral Communication: The Panel Discussion and Group Facilitation',
  'Grade 11 English strand: a panel discussion brings together several speakers with different perspectives on a shared topic, guided by a moderator who manages turn-taking, keeps the conversation focused, and draws out disagreement or nuance rather than letting a single voice dominate the exchange.',
  [('What does a panel discussion bring together?', ['Several speakers with different perspectives on a shared topic', 'A single speaker addressing an empty room', 'A written document with no spoken component', 'A group of speakers who all share an identical opinion'], 0),
   ('What role does a moderator play in a panel discussion?', ['Managing turn-taking and keeping the conversation focused', 'Speaking for the entire length of the discussion with no other speakers', 'Preventing every panelist from speaking at any point', 'Reading a prepared script with no interaction from panelists'], 0),
   ('What might a skilled moderator draw out of a panel discussion?', ['Disagreement or nuance among the panelists', 'Complete silence from every panelist present', 'A single repeated answer from every speaker', 'A discussion with no connection to the original topic'], 0),
   ('Why is turn-taking important in a panel discussion?', ['It prevents a single voice from dominating the exchange', 'Turn-taking always eliminates any useful discussion', 'Panel discussions are more effective when only one person ever speaks', 'Turn-taking has no effect on how a discussion unfolds'], 0),
   ('What distinguishes a panel discussion from a single formal speech?', ['Multiple speakers with differing perspectives interact under a moderators guidance', 'A panel discussion always involves exactly one speaker', 'A formal speech always involves several speakers responding to each other', 'There is no meaningful difference between the two formats'], 0)]),
F('Financial Mathematics: Currency Exchange Rates and Arbitrage',
  'Grade 11 Functions strand: a currency exchange rate expresses the value of one currency in terms of another, and arbitrage exploits small inconsistencies between exchange rates across different markets to generate a profit by converting currency through a sequence of trades that returns more of the original currency than was started with.',
  [('What does a currency exchange rate express?', ['The value of one currency in terms of another', 'The total population of a country', 'The exact interest rate charged by a single bank', 'A value with no connection to currency at all'], 0),
   ('What does arbitrage exploit?', ['Small inconsistencies between exchange rates across different markets', 'A single exchange rate that never changes in any market', 'A complete absence of any exchange rate differences', 'A rule that forbids converting between currencies'], 0),
   ('What is the goal of a currency arbitrage strategy?', ['To generate a profit by converting currency through a sequence of trades', 'To lose as much currency value as possible', 'To keep a single currency permanently unconverted', 'To eliminate all currency exchange rates worldwide'], 0),
   ('What must the final amount of currency exceed for an arbitrage sequence of trades to be profitable?', ['The original amount of currency that was started with', 'The exact same amount, with no change at all', 'A random unrelated numerical value', 'The total value of every currency in the world combined'], 0),
   ('Why do arbitrage opportunities in currency markets tend to be short-lived?', ['Traders quickly act on the inconsistency, which causes exchange rates to adjust and close the gap', 'Exchange rates never change once an arbitrage opportunity appears', 'Arbitrage opportunities are permanent and never disappear', 'Currency markets are entirely closed to any form of trading'], 0)]),
B('Evolution: Sexual Selection and Mate Choice',
  'Grade 11 Biology strand: sexual selection favours traits that increase an individuals success at attracting mates or competing with rivals for access to them, which can produce elaborate features such as bright plumage or large antlers even when those traits provide no direct survival advantage or actively hinder it.',
  [('What does sexual selection favour?', ['Traits that increase success at attracting mates or competing for access to them', 'Traits that have no connection to mating success at all', 'Only traits that improve an individuals ability to digest food', 'Traits that always reduce an individuals chance of reproducing'], 0),
   ('Give an example of a trait that sexual selection can produce.', ['Bright plumage', 'A complete absence of any colouration', 'A trait found equally in every species on Earth', 'A trait with no connection to mate attraction'], 0),
   ('Can a trait favoured by sexual selection provide no direct survival advantage?', ['Yes, some traits favoured by sexual selection provide no survival advantage or even hinder survival', 'No, every trait favoured by sexual selection always improves survival', 'Sexual selection never produces any trait of any kind', 'Sexual selection only ever removes existing traits, never adds new ones'], 0),
   ('What might large antlers help an individual do in the context of sexual selection?', ['Compete with rivals for access to mates', 'Digest food more efficiently', 'Regulate body temperature exclusively', 'Avoid all forms of predation entirely'], 0),
   ('How does sexual selection differ from natural selection based purely on survival?', ['Sexual selection can favour traits that aid reproduction even at some cost to survival', 'Sexual selection and natural selection always produce identical outcomes', 'Sexual selection has no connection to reproduction of any kind', 'Natural selection only ever concerns mate attraction, not survival'], 0)]),
C('Chemistry: Radiopharmaceuticals — Isotopes in Medical Diagnostic Imaging',
  'Grade 11 Chemistry strand: a radiopharmaceutical combines a radioactive isotope with a molecule that targets a specific tissue or organ, and the emitted radiation is detected from outside the body to produce a diagnostic image, allowing doctors to observe processes such as blood flow or metabolic activity without invasive surgery.',
  [('What does a radiopharmaceutical combine?', ['A radioactive isotope with a molecule that targets a specific tissue or organ', 'Two chemically inert gases with no radioactive component', 'A solid metal bar with no targeting molecule at all', 'A compound with no medical application whatsoever'], 0),
   ('How is a diagnostic image produced from a radiopharmaceutical inside the body?', ['Emitted radiation is detected from outside the body', 'The patient must be surgically opened to view the isotope directly', 'The isotope is removed from the body before any image is taken', 'No radiation of any kind is involved in the imaging process'], 0),
   ('What can radiopharmaceutical imaging allow doctors to observe?', ['Processes such as blood flow or metabolic activity', 'Only the exact height of a patient', 'A patients complete genetic sequence', 'Nothing related to any bodily process'], 0),
   ('What advantage does radiopharmaceutical imaging offer over invasive surgery?', ['It allows internal processes to be observed without surgery', 'It always requires more invasive surgery than any alternative method', 'It provides no diagnostic information of any kind', 'It can only be used after surgery has already been performed'], 0),
   ('Why is targeting important in the design of a radiopharmaceutical?', ['It directs the radioactive isotope to the specific tissue or organ being studied', 'Targeting has no effect on where the isotope accumulates in the body', 'Radiopharmaceuticals spread completely evenly with no targeting at all', 'Targeting removes the need for any radioactive isotope'], 0)]),
]),
day(166, [
E('Writing: The Proposal Argument — Identifying a Problem and Proposing a Solution',
  'Grade 11 English strand: a proposal argument identifies a specific problem, establishes why it matters to the intended audience, and then argues for a concrete, feasible solution, anticipating objections and explaining why the proposed course of action is more workable than the alternatives.',
  [('What does a proposal argument begin by identifying?', ['A specific problem', 'A solution with no stated problem behind it', 'An unrelated historical event', 'A list of random statistics with no context'], 0),
   ('What must a proposal argument establish about the problem it identifies?', ['Why it matters to the intended audience', 'That the problem does not actually exist', 'That the audience should ignore the problem entirely', 'That the problem cannot be solved under any circumstance'], 0),
   ('What does a proposal argument ultimately argue for?', ['A concrete, feasible solution', 'A solution with no practical steps of any kind', 'The permanent continuation of the problem', 'A solution deliberately kept vague and undefined'], 0),
   ('What should an effective proposal argument anticipate?', ['Objections to the proposed solution', 'Nothing at all, since objections are irrelevant', 'Only objections raised by the writer themselves', 'A total absence of any possible counterargument'], 0),
   ('Why might a proposal argument compare its solution to alternatives?', ['To explain why the proposed course of action is more workable than other options', 'Comparing solutions is forbidden in a proposal argument', 'Alternatives are always identical to the proposed solution', 'A proposal argument must never mention any other possible solution'], 0)]),
F('Geometry: The Equation of a Sphere in Three Dimensions',
  'Grade 11 Functions strand: the equation of a sphere in three dimensions extends the equation of a circle by relating the coordinates of every point on the surface to a fixed centre point and a constant radius, so that the sum of the squared differences in each coordinate direction equals the square of the radius.',
  [('What does the equation of a sphere in three dimensions extend?', ['The equation of a circle', 'The equation of a straight line', 'The equation of a single point with no radius', 'An equation with no geometric meaning at all'], 0),
   ('What two quantities define a sphere in three-dimensional space?', ['A fixed centre point and a constant radius', 'Two unrelated points with no centre defined', 'A single coordinate with no radius involved', 'A radius with no defined centre point'], 0),
   ('What does the sum of the squared coordinate differences equal in the equation of a sphere?', ['The square of the radius', 'The radius itself, with no squaring involved', 'Zero, in every possible case', 'The diameter of an unrelated circle'], 0),
   ('How many coordinates does a point on the surface of a sphere in three dimensions require?', ['Three', 'One', 'Two', 'Four'], 0),
   ('Why is the equation of a sphere considered a natural extension of the equation of a circle?', ['It applies the same distance relationship to points in three dimensions instead of two', 'A sphere and a circle share no mathematical relationship of any kind', 'The equation of a sphere ignores distance entirely', 'A circle is defined using four dimensions rather than two'], 0)]),
B('Plant Biology: Mycorrhizal Associations and Nutrient Exchange',
  'Grade 11 Biology strand: a mycorrhizal association is a mutualistic partnership between a fungus and a plants roots, in which the fungus extends the roots effective surface area to absorb water and minerals such as phosphorus, while the plant supplies the fungus with sugars produced through photosynthesis.',
  [('What kind of relationship is a mycorrhizal association?', ['A mutualistic partnership between a fungus and a plants roots', 'A purely parasitic relationship that harms the plant', 'A relationship in which neither organism benefits', 'A relationship that occurs only between two plants, with no fungus involved'], 0),
   ('What does the fungus in a mycorrhizal association help the plant absorb?', ['Water and minerals such as phosphorus', 'Only carbon dioxide from the atmosphere', 'Only oxygen produced by the plant itself', 'Nothing, since the fungus provides no benefit to the plant'], 0),
   ('What does the plant supply to the fungus in this partnership?', ['Sugars produced through photosynthesis', 'Water absorbed directly from the fungus', 'Minerals extracted from deep bedrock', 'Nothing, since the plant provides no benefit to the fungus'], 0),
   ('How does the fungus increase the effectiveness of the plants root system?', ['By extending the roots effective surface area', 'By shrinking the roots surface area to a fraction of its original size', 'By replacing the roots entirely with fungal tissue', 'By preventing the roots from absorbing any water at all'], 0),
   ('Why is a mycorrhizal association considered mutualistic rather than one-sided?', ['Both the fungus and the plant receive a benefit from the exchange', 'Only the fungus benefits, while the plant receives nothing', 'Only the plant benefits, while the fungus receives nothing', 'Neither organism benefits in any way from the association'], 0)]),
C('Chemistry: The Chemistry of Chocolate — Tempering and Cocoa Butter Crystal Forms',
  'Grade 11 Chemistry strand: cocoa butter can solidify into several different crystal forms, and tempering chocolate involves carefully controlling temperature to encourage the formation of a single stable crystal form that gives finished chocolate its glossy surface, firm snap, and resistance to melting at room temperature.',
  [('What can cocoa butter solidify into?', ['Several different crystal forms', 'A single crystal form with no variation possible', 'A liquid that never solidifies under any conditions', 'A gas at room temperature'], 0),
   ('What does tempering chocolate involve?', ['Carefully controlling temperature to encourage a stable crystal form', 'Randomly heating and cooling chocolate with no control at all', 'Removing all cocoa butter from the chocolate', 'Adding water to the chocolate mixture'], 0),
   ('What visual quality does properly tempered chocolate typically have?', ['A glossy surface', 'A dull, cloudy surface with no shine', 'No visible surface at all, since it remains a liquid', 'A surface that is always opaque white'], 0),
   ('What textural quality does the stable crystal form give tempered chocolate?', ['A firm snap', 'A texture that never solidifies at any temperature', 'A texture identical to liquid honey', 'A texture with no measurable firmness'], 0),
   ('Why does poorly tempered chocolate often develop a dull, streaky surface?', ['Unstable cocoa butter crystal forms create an uneven surface structure', 'Poorly tempered chocolate always looks identical to properly tempered chocolate', 'Cocoa butter crystal form has no effect on chocolates appearance', 'A dull surface only occurs when no cocoa butter is present'], 0)]),
]),
day(167, [
E('Poetry: Blank Verse and the Rhythm of Iambic Pentameter',
  'Grade 11 English strand: blank verse is unrhymed poetry written in iambic pentameter, a rhythm of five unstressed-stressed syllable pairs per line, and its flexible structure, free of a rhyme scheme but still metrically patterned, has made it a favoured form for dramatic and narrative verse in English for centuries.',
  [('What defines blank verse?', ['Unrhymed poetry written in iambic pentameter', 'Rhymed poetry with no fixed meter at all', 'Poetry written entirely in prose with no meter', 'A form that forbids any use of rhythm'], 0),
   ('What rhythmic pattern does iambic pentameter follow?', ['Five unstressed-stressed syllable pairs per line', 'A single stressed syllable repeated infinitely with no variation', 'Ten unrelated syllables with no stress pattern at all', 'Three stressed-unstressed pairs per line'], 0),
   ('What does blank verse lack that many other poetic forms include?', ['A rhyme scheme', 'Any rhythmic pattern whatsoever', 'Any use of syllables at all', 'A defined number of lines per stanza'], 0),
   ('Why has blank verse been a favoured form for dramatic and narrative verse in English?', ['Its flexible, metrically patterned structure suits extended storytelling without the constraint of rhyme', 'Blank verse forbids any storytelling of any kind', 'Rhyme is required for any dramatic verse, making blank verse unusable', 'Blank verse has no metrical pattern to guide its rhythm'], 0),
   ('What remains constant in blank verse even though rhyme is absent?', ['A consistent metrical pattern', 'Nothing at all remains constant', 'The exact same words repeated in every line', 'A strict requirement that every line rhyme with the next'], 0)]),
F('Complex Numbers: Complex Conjugates and Their Properties',
  'Grade 11 Functions strand: the complex conjugate of a number reverses the sign of its imaginary part while leaving the real part unchanged, and multiplying a complex number by its conjugate always produces a real, non-negative result, a property used to simplify expressions and to divide by a complex number.',
  [('What does the complex conjugate of a number do to its imaginary part?', ['Reverses its sign', 'Doubles it in magnitude', 'Removes it entirely, leaving only zero', 'Converts it into a real number with no imaginary component remaining defined'], 0),
   ('What happens to the real part of a complex number when its conjugate is taken?', ['It remains unchanged', 'It is reversed in sign', 'It is doubled', 'It is removed entirely'], 0),
   ('What kind of result does multiplying a complex number by its conjugate always produce?', ['A real, non-negative result', 'An imaginary result with no real component', 'A negative real number in every case', 'A result that is always exactly zero'], 0),
   ('What common use does multiplying by a conjugate serve in working with complex numbers?', ['Dividing by a complex number', 'Multiplying two real numbers together', 'Converting a real number into an imaginary one', 'Eliminating the real part of a complex number entirely'], 0),
   ('If a complex number is written as a plus bi, what is its conjugate?', ['a minus bi', 'a plus bi, unchanged', 'negative a plus bi', 'negative a minus bi'], 0)]),
B('Human Biology: Sleep Architecture and the Stages of Sleep',
  'Grade 11 Biology strand: sleep architecture refers to the cyclical pattern of distinct sleep stages a person moves through each night, alternating between non-REM stages of progressively deeper sleep and REM sleep, during which the brain is highly active and most vivid dreaming occurs, with each full cycle repeating several times per night.',
  [('What does sleep architecture refer to?', ['The cyclical pattern of distinct sleep stages a person moves through each night', 'A single unchanging state that lasts the entire night', 'The physical structure of the bedroom where a person sleeps', 'A pattern that occurs only once in a persons lifetime'], 0),
   ('What are the two broad categories of sleep stages mentioned?', ['Non-REM and REM sleep', 'Only REM sleep, with no other category', 'Only non-REM sleep, with no other category', 'Deep sleep and daytime wakefulness'], 0),
   ('During which stage does most vivid dreaming occur?', ['REM sleep', 'The deepest stage of non-REM sleep', 'A stage that does not exist in human sleep', 'Every stage equally, with no difference between them'], 0),
   ('What characterizes brain activity during REM sleep?', ['It is highly active', 'It is completely inactive, with no measurable brain activity', 'It matches waking activity exactly with no distinction', 'It ceases entirely until the person wakes up'], 0),
   ('How many times does a full sleep cycle typically repeat in one night?', ['Several times', 'Exactly once, with no repetition', 'Zero times, since sleep is not cyclical', 'A number that has no relationship to a full nights sleep'], 0)]),
C('Chemistry: Triboelectric Charging and the Chemistry of Static Electricity',
  'Grade 11 Chemistry strand: triboelectric charging occurs when two different materials are rubbed together and electrons transfer from the surface of one material to the other, leaving one material with a net negative charge and the other with a net positive charge, an imbalance that later discharges as static electricity.',
  [('What happens when two different materials are rubbed together in triboelectric charging?', ['Electrons transfer from the surface of one material to the other', 'Protons transfer freely between the two materials', 'No charge transfer of any kind occurs', 'The two materials instantly fuse into a single substance'], 0),
   ('What charge does the material that loses electrons end up with?', ['A net positive charge', 'A net negative charge', 'No charge at all', 'A charge that is always exactly neutral'], 0),
   ('What charge does the material that gains electrons end up with?', ['A net negative charge', 'A net positive charge', 'No charge at all', 'A charge equal to the positive material'], 0),
   ('What eventually happens to the charge imbalance created by triboelectric charging?', ['It discharges as static electricity', 'It remains permanently locked in place with no discharge ever occurring', 'It converts directly into a different chemical element', 'It has no observable effect of any kind'], 0),
   ('What is required for triboelectric charging to occur between two materials?', ['The two different materials must be rubbed together', 'The two materials must be completely identical to each other', 'The materials must never come into contact with each other', 'The materials must be submerged in water before contact'], 0)]),
]),
day(168, [
E('Drama: Stage Directions and the Language of the Performance Text',
  'Grade 11 English strand: stage directions are the playwrights instructions describing setting, movement, tone, or gesture that accompany the dialogue of a play, guiding how a script should be staged and performed while remaining, unlike the dialogue itself, unspoken by the actors on stage.',
  [('What do stage directions describe?', ['Setting, movement, tone, or gesture', 'Only the exact ticket price of a performance', 'The biography of the playwright', 'A summary of the entire plot written after the play ends'], 0),
   ('Who writes the stage directions in a play?', ['The playwright', 'The audience, after watching a performance', 'A director who never reads the original script', 'An actor improvising without any script'], 0),
   ('What is true of stage directions in relation to the dialogue actors speak aloud?', ['Stage directions are typically unspoken by the actors on stage', 'Stage directions are always spoken aloud exactly like dialogue', 'Stage directions replace all dialogue in a play', 'Stage directions and dialogue are identical in every play'], 0),
   ('What do stage directions guide?', ['How a script should be staged and performed', 'The financial budget of a theatrical production', 'The seating chart of the audience', 'The colour of the theatre curtains exclusively'], 0),
   ('Why might a playwright include detailed stage directions rather than leaving staging entirely open?', ['To communicate a specific vision for how a scene should look and feel when performed', 'Detailed stage directions always prevent a play from ever being performed', 'Stage directions are forbidden in professional playwriting', 'Leaving staging open always produces an identical result to detailed directions'], 0)]),
F('Discrete Math: Boolean Algebra and Logic Gates',
  'Grade 11 Functions strand: Boolean algebra manipulates logical values of true and false using operations such as AND, OR, and NOT, and these operations are physically implemented in computing hardware as logic gates, making Boolean algebra the mathematical foundation underlying how digital circuits process information.',
  [('What two values does Boolean algebra manipulate?', ['True and false', 'Only positive real numbers', 'Only negative integers', 'A continuous range of values between zero and one'], 0),
   ('Name one basic operation used in Boolean algebra.', ['AND', 'Square root', 'Integration', 'Differentiation'], 0),
   ('How are Boolean operations physically implemented in computing hardware?', ['As logic gates', 'As mechanical gears with no electronic component', 'As a single unchanging wire with no logic involved', 'As a printed page with no physical circuitry'], 0),
   ('What does Boolean algebra provide the mathematical foundation for?', ['How digital circuits process information', 'How ancient civilizations recorded historical events', 'How biological cells divide during mitosis', 'How rivers erode surrounding rock over time'], 0),
   ('Why is Boolean algebra considered fundamental to computing?', ['Digital circuits rely on true/false logic operations to process and store information', 'Computing has no reliance on true/false logic of any kind', 'Boolean algebra only applies to paper-based calculations, never circuits', 'Digital circuits operate using continuous values rather than true/false logic'], 0)]),
B('Biochemistry: Protein Structure — Primary, Secondary, Tertiary, and Quaternary Levels',
  'Grade 11 Biology strand: a proteins primary structure is its linear sequence of amino acids, its secondary structure consists of local folding patterns such as alpha helices and beta sheets, its tertiary structure is the overall three-dimensional shape of a single folded chain, and its quaternary structure describes how multiple folded chains assemble together.',
  [('What is a proteins primary structure?', ['Its linear sequence of amino acids', 'Its overall three-dimensional shape', 'A pattern found only in secondary structure', 'A structure that exists only in quaternary proteins'], 0),
   ('Name a folding pattern found in a proteins secondary structure.', ['The alpha helix', 'A single straight line with no folding at all', 'A structure found only at the primary level', 'A pattern that never occurs in any protein'], 0),
   ('What does a proteins tertiary structure describe?', ['The overall three-dimensional shape of a single folded chain', 'The linear sequence of amino acids only', 'The assembly of multiple separate protein chains', 'A structure that applies only to DNA, not protein'], 0),
   ('What does a proteins quaternary structure describe?', ['How multiple folded chains assemble together', 'The sequence of amino acids in a single chain', 'A folding pattern found only within a single amino acid', 'A structure that never involves more than one chain'], 0),
   ('Why is understanding all four levels of protein structure important for understanding protein function?', ['A proteins final shape at every level determines how it interacts with other molecules', 'Protein structure has no connection to protein function of any kind', 'Only the primary structure has any relevance to how a protein functions', 'All four levels of structure are always identical for every protein'], 0)]),
C('Chemistry: Molecular Gastronomy — Spherification and Gel Chemistry in Cooking',
  'Grade 11 Chemistry strand: spherification is a molecular gastronomy technique in which a liquid containing sodium alginate is dropped into a calcium chloride bath, triggering a chemical reaction that forms a thin gel membrane around the droplet and produces a sphere with a liquid centre and a delicate solid outer shell.',
  [('What ingredient in the liquid is essential for spherification?', ['Sodium alginate', 'Pure table salt with no other chemical role', 'A solid metal shaving', 'Distilled water with no dissolved compound present'], 0),
   ('What solution is the sodium alginate liquid dropped into during spherification?', ['A calcium chloride bath', 'A bath of pure distilled water with no dissolved ions', 'A container of liquid nitrogen with no chemical reaction', 'A bath of vegetable oil with no reactive component'], 0),
   ('What forms around the droplet as a result of the reaction in spherification?', ['A thin gel membrane', 'A solid metal coating', 'No structural change occurs at all', 'A layer of ice regardless of temperature'], 0),
   ('What is the resulting structure of a sphere produced by this technique?', ['A liquid centre surrounded by a delicate solid outer shell', 'A completely solid sphere with no liquid centre at all', 'A sphere that is entirely gas-filled', 'A flat, two-dimensional shape with no sphere formed'], 0),
   ('What type of chemical process is responsible for forming the gel membrane in spherification?', ['A reaction between sodium alginate and calcium ions', 'A purely physical process with no chemical reaction involved', 'A nuclear reaction between two isotopes', 'A reaction that requires no calcium of any kind'], 0)]),
]),
day(169, [
E('Literature: The Serial Novel and Publication in Instalments',
  'Grade 11 English strand: a serial novel is published in regular instalments rather than as a single complete volume, a format that shaped nineteenth-century fiction by encouraging cliffhangers and episodic pacing designed to keep readers subscribing to the next instalment rather than losing interest between releases.',
  [('How is a serial novel published?', ['In regular instalments rather than as a single complete volume', 'Only once, as a single complete volume with no instalments', 'Anonymously, with no authors name ever attached', 'Exclusively as an audio recording with no written text'], 0),
   ('What pacing technique did serial publication encourage in nineteenth-century fiction?', ['Cliffhangers and episodic pacing', 'A single unbroken scene with no change in pacing at all', 'An immediate resolution of every plot point in the first instalment', 'A refusal to include any tension or suspense'], 0),
   ('Why might a serial novel be structured around cliffhangers?', ['To keep readers subscribing to the next instalment', 'Cliffhangers were strictly forbidden in serial fiction', 'To ensure readers stop reading immediately after the first instalment', 'Cliffhangers have no effect on reader interest of any kind'], 0),
   ('What risk did a serial novel face between the release of each instalment?', ['Losing reader interest before the next instalment appeared', 'Gaining an infinite number of new readers automatically', 'Losing the ability to be printed in any format', 'Facing no risk at all, since interest was always guaranteed'], 0),
   ('How does the serial format differ from a novel released as a single complete volume?', ['It divides the story into regular instalments spaced out over time', 'A serial novel is always shorter than a single-volume novel', 'A single complete volume is always released in instalments as well', 'There is no meaningful difference between the two formats'], 0)]),
F('Statistics: The F-Distribution and Comparing Two Variances',
  'Grade 11 Functions strand: the F-distribution is used to compare the variances of two independent samples by examining the ratio of their sample variances, and a ratio far from one suggests the two populations being compared do not share the same underlying variance.',
  [('What does the F-distribution help compare?', ['The variances of two independent samples', 'The means of a single sample only', 'The exact median of an unrelated data set', 'A single data point with no comparison involved'], 0),
   ('What ratio does the F-distribution examine?', ['The ratio of two sample variances', 'The ratio of two unrelated sample sizes only', 'The ratio of a mean to a median', 'A ratio that has no connection to variance'], 0),
   ('What does a ratio far from one suggest when using the F-distribution?', ['The two populations being compared do not share the same underlying variance', 'The two populations are guaranteed to be identical', 'The sample sizes must be reported incorrectly', 'No conclusion can ever be drawn from the F-distribution'], 0),
   ('How many samples does a typical F-distribution comparison involve?', ['Two independent samples', 'Only a single sample with no comparison', 'An unlimited number of samples with no defined count', 'Zero samples, since no data is required'], 0),
   ('Why might a researcher use the F-distribution before applying certain other statistical tests?', ['To check whether an assumption of equal variances between two groups holds', 'The F-distribution has no relevance to any other statistical test', 'It replaces the need to collect any data at all', 'It only applies to data with no numerical values'], 0)]),
B('Evolution: Genetic Bottlenecks and the Loss of Genetic Diversity',
  'Grade 11 Biology strand: a genetic bottleneck occurs when a population is sharply reduced in size by an event such as a natural disaster or disease outbreak, and the surviving individuals carry only a fraction of the original populations genetic diversity, leaving the recovered population more vulnerable to future environmental change.',
  [('What is a genetic bottleneck?', ['A sharp reduction in population size that reduces genetic diversity', 'A steady, gradual increase in population size over centuries', 'An event that always increases genetic diversity', 'A process that has no connection to population size at all'], 0),
   ('Give an example of an event that can cause a genetic bottleneck.', ['A natural disaster', 'A period of unusually abundant food supply', 'A steady, unchanging environment with no disruption', 'An increase in the populations total genetic diversity'], 0),
   ('What do surviving individuals after a bottleneck carry, compared to the original population?', ['Only a fraction of the original genetic diversity', 'The exact same amount of genetic diversity as before', 'More genetic diversity than the original population', 'No genetic material at all'], 0),
   ('Why does a population that has gone through a bottleneck become more vulnerable to future environmental change?', ['Reduced genetic diversity limits the range of traits available for natural selection to act on', 'Reduced genetic diversity always makes a population immune to environmental change', 'Genetic diversity has no connection to a populations ability to adapt', 'A bottleneck always increases a populations resilience to change'], 0),
   ('How does a genetic bottleneck differ from ordinary genetic drift in a stable population?', ['A bottleneck involves a sudden, sharp reduction in population size rather than gradual random change', 'A genetic bottleneck and genetic drift are entirely unrelated concepts', 'A bottleneck always increases population size dramatically', 'Genetic drift only occurs in populations that never change in size'], 0)]),
C('Chemistry: Blood Buffering and pH Homeostasis in the Human Body',
  'Grade 11 Chemistry strand: blood pH is kept within a narrow range by chemical buffer systems, most notably the bicarbonate buffer, which can absorb excess acid or base by shifting the balance between dissolved carbon dioxide, carbonic acid, and bicarbonate ion, preventing the small pH swings that would otherwise disrupt normal cell function.',
  [('What keeps blood pH within a narrow range?', ['Chemical buffer systems', 'A complete absence of any chemical regulation', 'A single unchanging chemical with no buffering capacity', 'A process that has no connection to pH at all'], 0),
   ('Name the buffer system most notably responsible for regulating blood pH.', ['The bicarbonate buffer', 'A buffer made entirely of pure water with no ions', 'A buffer based only on table salt', 'A system with no chemical components at all'], 0),
   ('What three related substances does the bicarbonate buffer shift the balance between?', ['Dissolved carbon dioxide, carbonic acid, and bicarbonate ion', 'Oxygen, nitrogen, and argon', 'Glucose, fructose, and sucrose', 'Sodium, potassium, and calcium only'], 0),
   ('What can the bicarbonate buffer absorb to help maintain stable blood pH?', ['Excess acid or base', 'Only excess water, with no acid or base involved', 'Only excess oxygen gas', 'Nothing, since the buffer has no absorptive capacity'], 0),
   ('Why is maintaining a stable blood pH important for normal cell function?', ['Small pH swings can disrupt the proteins and enzymes cells depend on to function normally', 'Blood pH has no connection to how cells function', 'Cells function identically no matter how much blood pH changes', 'A stable pH always harms normal cellular processes'], 0)]),
]),
day(170, [
E('English Review: Haiku, Verbals, Panels, and Proposal Writing',
  'Grade 11 English strand review: students revisit the haiku and tanka, verbals, the family saga novel, photo manipulation ethics, the panel discussion, the proposal argument, blank verse, stage directions, and the serial novel.',
  [('What structural feature defines a haiku?', ['A compressed three-line form built around a single natural image', 'A twelve-line form with no fixed structure at all', 'A rhymed couplet describing an urban skyline', 'A form that forbids any reference to nature'], 0),
   ('What does a family saga novel typically trace?', ['A family across multiple generations', 'A single character across a single afternoon', 'A nation with no reference to any individual family', 'A single generation with no reference to the past or future'], 0),
   ('What does a panel discussion bring together?', ['Several speakers with different perspectives on a shared topic', 'A single speaker addressing an empty room', 'A written document with no spoken component', 'A group of speakers who all share an identical opinion'], 0),
   ('What defines blank verse?', ['Unrhymed poetry written in iambic pentameter', 'Rhymed poetry with no fixed meter at all', 'Poetry written entirely in prose with no meter', 'A form that forbids any use of rhythm'], 0),
   ('How is a serial novel published?', ['In regular instalments rather than as a single complete volume', 'Only once, as a single complete volume with no instalments', 'Anonymously, with no authors name ever attached', 'Exclusively as an audio recording with no written text'], 0)]),
F('Functions Review: Higher-Order Calculus, Discrete Structures, and Complex Numbers',
  'Grade 11 Functions strand review: students revisit higher-order derivatives, generating functions, currency exchange and arbitrage, complex conjugates, and the F-distribution.',
  [('How is a higher-order derivative found?', ['By differentiating a function more than once', 'By integrating a function a single time', 'By setting the function equal to zero and solving', 'By graphing the function with no further calculation'], 0),
   ('What does a generating function encode?', ['An entire sequence of numbers as the coefficients of a power series', 'A single isolated number with no connection to any sequence', 'The exact colour of a graph', 'A sequence that has no numerical values at all'], 0),
   ('What does a currency exchange rate express?', ['The value of one currency in terms of another', 'The total population of a country', 'The exact interest rate charged by a single bank', 'A value with no connection to currency at all'], 0),
   ('What does the complex conjugate of a number do to its imaginary part?', ['Reverses its sign', 'Doubles it in magnitude', 'Removes it entirely, leaving only zero', 'Converts it into a real number with no imaginary component remaining defined'], 0),
   ('What does the F-distribution help compare?', ['The variances of two independent samples', 'The means of a single sample only', 'The exact median of an unrelated data set', 'A single data point with no comparison involved'], 0)]),
B('Biology Review: Biomes, Genetics, and Molecular Physiology',
  'Grade 11 Biology strand review: students revisit grassland and savanna ecosystems, nondisjunction and aneuploidy, sexual selection, sleep architecture, and genetic bottlenecks.',
  [('What plant type dominates grassland and savanna ecosystems?', ['Grasses', 'Coniferous trees exclusively', 'Mosses and lichens exclusively', 'Coral and other marine organisms'], 0),
   ('What is nondisjunction?', ['A failure of chromosomes to separate properly during meiosis', 'A perfectly normal separation of chromosomes during meiosis', 'A process that occurs only during mitosis, never meiosis', 'A process with no connection to chromosome number at all'], 0),
   ('What does sexual selection favour?', ['Traits that increase success at attracting mates or competing for access to them', 'Traits that have no connection to mating success at all', 'Only traits that improve an individuals ability to digest food', 'Traits that always reduce an individuals chance of reproducing'], 0),
   ('What does sleep architecture refer to?', ['The cyclical pattern of distinct sleep stages a person moves through each night', 'A single unchanging state that lasts the entire night', 'The physical structure of the bedroom where a person sleeps', 'A pattern that occurs only once in a persons lifetime'], 0),
   ('What is a genetic bottleneck?', ['A sharp reduction in population size that reduces genetic diversity', 'A steady, gradual increase in population size over centuries', 'An event that always increases genetic diversity', 'A process that has no connection to population size at all'], 0)]),
C('Chemistry Review: Everyday Chemistry, Energy, and Human Physiology',
  'Grade 11 Chemistry strand review: students revisit caffeine extraction, water electrolysis, radiopharmaceuticals, triboelectric charging, and blood buffering and pH homeostasis.',
  [('What class of organic compound is caffeine?', ['An alkaloid', 'A noble gas', 'A pure metal', 'An ionic salt with no carbon present'], 0),
   ('What does electrolysis of water use to split water molecules?', ['An electric current', 'A stream of pressurized air with no electric current', 'Gravity alone, with no external energy input', 'A magnetic field with no current involved'], 0),
   ('What does a radiopharmaceutical combine?', ['A radioactive isotope with a molecule that targets a specific tissue or organ', 'Two chemically inert gases with no radioactive component', 'A solid metal bar with no targeting molecule at all', 'A compound with no medical application whatsoever'], 0),
   ('What happens when two different materials are rubbed together in triboelectric charging?', ['Electrons transfer from the surface of one material to the other', 'Protons transfer freely between the two materials', 'No charge transfer of any kind occurs', 'The two materials instantly fuse into a single substance'], 0),
   ('What keeps blood pH within a narrow range?', ['Chemical buffer systems', 'A complete absence of any chemical regulation', 'A single unchanging chemical with no buffering capacity', 'A process that has no connection to pH at all'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g11_161_170)
    append_to(11, g11_161_170)
