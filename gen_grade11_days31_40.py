#!/usr/bin/env python3
"""Phase 3: Grade 11, Days 31-40 (first Grade 11 batch, continuing the
10-day pattern used for Grades 3-10). Topics chosen to avoid any overlap
with the existing Day 1-30 set (see data/grade11.json): symbolism and
allegory, the bildungsroman, piecewise functions, the unit circle,
annuities, microbiology, CRISPR, gas laws, VSEPR theory, and
calorimetry.

IMPORTANT: Grade 11's subject keys are "English", "Functions",
"Biology", "Chemistry" -- confirmed via
grep -o 'subject:"[^"]*"' data/grade11.ts | sort -u -- a completely
different set from the Language/Math/Science/SocialStudies pattern used
in Grades 3-9, since Ontario Grade 11 splits science/math into
individual university-prep courses.

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys
sys.path.insert(0, '/sessions/modest-compassionate-lamport/mnt/gradesbooster')
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


g11_31_40 = [
day(31, [
E('Literary Analysis: Symbolism and Allegory in the Novel',
  'Grade 11 English strand: symbolism uses objects or images to represent deeper ideas, while allegory extends this technique so that an entire narrative carries a second, often moral or political, meaning.',
  [('Symbolism uses objects or images to represent ___.', ['Deeper ideas beyond their literal meaning', 'Only their literal, surface-level meaning', 'Nothing beyond their physical description', 'A concept unrelated to meaning'], 0),
   ('An allegory extends symbolism so that ___.', ['An entire narrative carries a second, deeper meaning', 'Only a single object carries any symbolic weight', 'No part of the narrative has any additional meaning', 'The story’s literal plot is its only meaning'], 0),
   ('Why might an author choose allegory to comment on a real-world political or moral issue?', ['It allows commentary on sensitive topics through a layer of fictional distance', 'Allegory removes any possibility of commentary on real issues', 'This technique has no connection to political or moral themes', 'Allegorical narratives can never be interpreted on more than one level'], 0),
   ('Which is an example of a symbol that might appear in a novel?', ['A caged bird representing lost freedom', 'A random object with no connection to the story’s themes', 'A character’s name with no symbolic meaning', 'A setting description with no thematic purpose'], 0),
   ('Why is recognizing allegory important when analyzing certain novels?', ['It reveals a deeper layer of meaning beyond the literal events of the story', 'Allegory has no effect on how a novel should be interpreted', 'Recognizing allegory never changes a reader’s understanding of a text', 'Allegorical meaning is always identical to the literal plot'], 0)]),
F('Piecewise Functions and Their Applications',
  'Grade 11 Functions strand: a piecewise function is defined by different expressions over different intervals of its domain, often used to model real-world situations that behave differently under different conditions.',
  [('A piecewise function is defined by ___.', ['Different expressions over different intervals of its domain', 'A single expression that applies to the entire domain', 'No defined expression at all', 'A concept unrelated to domain intervals'], 0),
   ('Which is an example of a real-world situation that could be modelled with a piecewise function?', ['A cell phone plan with different rates based on usage tiers', 'A situation with a constant rate that never changes', 'A scenario with no connection to changing conditions', 'A situation that can only ever be modelled with one single equation'], 0),
   ('Why is it important to identify the domain restrictions for each piece of a piecewise function?', ['Each expression only applies within its specified interval', 'Domain restrictions have no effect on how a piecewise function is evaluated', 'A piecewise function has no domain restrictions at all', 'Every piece of the function applies across the entire domain'], 0),
   ('When graphing a piecewise function, what might indicate a boundary between two pieces?', ['An open or closed circle marking where one piece ends and another begins', 'Piecewise functions are always graphed with no boundaries shown', 'A boundary has no visual representation on a graph', 'The entire graph is drawn as a single continuous line with no breaks'], 0),
   ('Why might piecewise functions be useful for modelling tax brackets?', ['Tax rates often change at specific income thresholds, matching the structure of a piecewise function', 'Tax brackets can never be represented using a piecewise function', 'This type of function has no real-world financial applications', 'Tax rates always remain identical regardless of income level'], 0)]),
B('Microbiology: Bacteria, Viruses, and Immunity',
  'Grade 11 Biology strand: microbiology examines the structure and function of bacteria and viruses, along with how the immune system responds to and defends against these pathogens.',
  [('Microbiology examines the structure and function of ___.', ['Bacteria and viruses', 'Only large mammals, with no connection to microorganisms', 'A field unrelated to biology', 'Only plants, with no connection to microorganisms'], 0),
   ('A key structural difference between bacteria and viruses is that bacteria are ___.', ['Living cells, while viruses require a host cell to reproduce', 'Never able to reproduce under any circumstances', 'Identical in structure to viruses in every way', 'Not made of any cells at all, unlike viruses'], 0),
   ('The immune system defends against pathogens partly through ___.', ['White blood cells that identify and attack foreign invaders', 'A process entirely unrelated to pathogens', 'Structures that only respond to physical injury', 'Cells that have no role in fighting disease'], 0),
   ('Why might a vaccine help the immune system respond more effectively to a future infection?', ['It exposes the immune system to a harmless form of a pathogen, helping it recognize the real one later', 'Vaccines have no effect on how the immune system responds', 'The immune system never learns to recognize new pathogens', 'This process has no connection to immunity or disease prevention'], 0),
   ('Why is understanding microbiology important for public health?', ['It helps explain how diseases spread and how they can be prevented or treated', 'Microbiology has no connection to public health', 'Disease prevention never relies on understanding microorganisms', 'This field of study has no practical, real-world applications'], 0)]),
C('Gas Laws: Boyle’s, Charles’s, and the Combined Gas Law',
  'Grade 11 Chemistry strand: gas laws describe the mathematical relationships between a gas’s pressure, volume, and temperature, with Boyle’s Law, Charles’s Law, and the Combined Gas Law each describing specific relationships.',
  [('Boyle’s Law describes the relationship between a gas’s ___.', ['Pressure and volume, at constant temperature', 'Only temperature, with no connection to pressure', 'Mass and colour', 'A relationship unrelated to gas behaviour'], 0),
   ('Charles’s Law describes the relationship between a gas’s ___.', ['Volume and temperature, at constant pressure', 'Only pressure, with no connection to temperature', 'Colour and mass', 'A relationship unrelated to gas behaviour'], 0),
   ('According to Boyle’s Law, if the volume of a gas decreases at constant temperature, its pressure will generally ___.', ['Increase', 'Decrease', 'Remain completely unchanged', 'Become impossible to determine'], 0),
   ('The Combined Gas Law allows you to relate ___.', ['Pressure, volume, and temperature all at once', 'Only pressure and colour, with no other variables', 'A single variable with no other relationships considered', 'Mass and density exclusively'], 0),
   ('Why are gas laws useful for understanding real-world situations, like how a hot air balloon rises?', ['They explain how changes in temperature, pressure, or volume affect gas behaviour', 'Gas laws have no connection to real-world physical phenomena', 'These laws can only be applied to purely theoretical, abstract problems', 'Gas behaviour never follows any predictable mathematical pattern'], 0)])]),

day(32, [
E('Writing: The University-Style Research Proposal',
  'Grade 11 English strand: a research proposal outlines a planned area of inquiry, including a clear research question, its significance, and an initial approach for investigating it.',
  [('A research proposal outlines ___.', ['A planned area of inquiry, including a research question', 'A completed research project with no further steps planned', 'A topic entirely unrelated to research', 'A summary of someone else’s already-published research'], 0),
   ('Why should a research proposal clearly state its research question?', ['It defines the specific focus and direction of the planned investigation', 'A research question is unnecessary in a proposal', 'Research proposals should never include a specific question', 'Stating a clear question always makes a proposal weaker'], 0),
   ('Why might a research proposal explain the significance of its topic?', ['It helps justify why the research is worth pursuing', 'Significance has no role in a research proposal', 'A proposal should never explain why its topic matters', 'Explaining significance always weakens a proposal'], 0),
   ('Which is an example of an appropriate initial approach described in a research proposal?', ['An outline of the sources and methods that will be used to investigate the question', 'A proposal with no plan for how the research will proceed', 'A description entirely unrelated to research methodology', 'A promise to avoid using any sources at all'], 0),
   ('Why is developing skill in writing research proposals valuable for future academic work?', ['It builds the ability to plan and justify an independent investigation, a skill needed at the university level', 'This skill has no connection to future academic work', 'Research proposals are never used beyond a high school English class', 'This type of writing has no practical value'], 0)]),
F('Trigonometry: The Unit Circle and Radian Measure',
  'Grade 11 Functions strand: the unit circle is a circle with a radius of one used to define trigonometric ratios for any angle, and radian measure is an alternative way of measuring angles based on arc length.',
  [('The unit circle has a radius of ___.', ['One', 'Zero', 'A value that varies depending on the angle', 'A value unrelated to trigonometry'], 0),
   ('Radian measure defines an angle based on ___.', ['Arc length relative to the circle’s radius', 'The colour of the angle', 'A measurement unrelated to circles', 'Only the number of degrees, with no connection to arc length'], 0),
   ('One full rotation around a circle is equal to how many radians?', ['2π', 'π', '360', '90'], 0),
   ('Why is the unit circle useful for defining trigonometric ratios for any angle, including angles greater than 90 degrees?', ['It provides a consistent way to determine sine, cosine, and tangent values at any point around the circle', 'The unit circle can only be used for angles between 0 and 90 degrees', 'This tool has no connection to trigonometric ratios', 'Trigonometric ratios cannot be defined using the unit circle'], 0),
   ('Why might radian measure be preferred over degree measure in more advanced mathematics, like calculus?', ['Radian measure simplifies many mathematical relationships involving circular and periodic functions', 'Radian measure has no advantages over degree measure in any context', 'Degree measure is always the only appropriate choice in advanced mathematics', 'This distinction has no relevance to how angles are used in mathematics'], 0)]),
B('Genetics: Genetic Engineering and CRISPR',
  'Grade 11 Biology strand: CRISPR is a genetic engineering technology that allows scientists to precisely edit DNA sequences, offering powerful applications in medicine, agriculture, and research.',
  [('CRISPR is a technology used to ___.', ['Precisely edit DNA sequences', 'Only observe DNA, with no ability to change it', 'A process entirely unrelated to genetics', 'Replace the need for any genetic material'], 0),
   ('Which is a potential application of CRISPR technology?', ['Correcting a genetic mutation that causes disease', 'An application entirely unrelated to genetics or medicine', 'A use with no connection to DNA editing', 'A technology that has no practical applications'], 0),
   ('Why does CRISPR raise ethical questions, particularly regarding its use in humans?', ['Editing DNA has the potential for significant and lasting effects, raising questions about appropriate use', 'CRISPR raises no ethical questions of any kind', 'This technology has no connection to human genetics', 'Ethical considerations are irrelevant to genetic engineering research'], 0),
   ('Why is CRISPR considered a significant advancement compared to earlier genetic engineering methods?', ['It allows for much more precise and efficient editing of specific DNA sequences', 'CRISPR provides no advantage over earlier genetic engineering techniques', 'This technology is identical to all previous genetic engineering methods', 'CRISPR has no connection to precision or efficiency in gene editing'], 0),
   ('Why might CRISPR be useful in agriculture?', ['It can help develop crops with desirable traits, like improved resistance to disease', 'CRISPR has no applications outside of human medicine', 'Agricultural applications of genetic engineering do not exist', 'This technology cannot be applied to plants in any way'], 0)]),
C('Chemical Bonding: Molecular Shapes and VSEPR Theory',
  'Grade 11 Chemistry strand: VSEPR (Valence Shell Electron Pair Repulsion) theory predicts the three-dimensional shape of a molecule based on the repulsion between electron pairs surrounding a central atom.',
  [('VSEPR theory predicts a molecule’s ___.', ['Three-dimensional shape', 'Colour', 'Mass', 'A property unrelated to molecular structure'], 0),
   ('VSEPR theory is based on the idea that electron pairs around a central atom ___.', ['Repel each other and arrange themselves to minimize this repulsion', 'Always attract each other with no repulsion involved', 'Have no effect on a molecule’s shape', 'Never influence how a molecule is arranged'], 0),
   ('Which factor does VSEPR theory consider when predicting molecular shape?', ['The number of bonding and lone electron pairs around the central atom', 'Only the colour of the atoms involved', 'A factor entirely unrelated to electron arrangement', 'The temperature of the surrounding environment only'], 0),
   ('Why is understanding a molecule’s three-dimensional shape important in chemistry?', ['Molecular shape can significantly influence a substance’s physical and chemical properties', 'Molecular shape has no connection to a substance’s properties', 'This concept has no practical relevance to chemistry', 'Shape has no effect on how molecules interact with each other'], 0),
   ('Why might VSEPR theory be useful for predicting the shape of water molecules?', ['It accounts for the lone electron pairs on the oxygen atom, which affect the molecule’s bent shape', 'VSEPR theory cannot be applied to water molecules', 'Water’s shape has no connection to its electron arrangement', 'This theory only applies to molecules with no lone electron pairs'], 0)])]),

day(33, [
E('Media Literacy: Analyzing Documentary Film',
  'Grade 11 English strand: documentary films present real events and information, but filmmakers make deliberate choices in editing, narration, and framing that shape how audiences interpret the subject matter.',
  [('Documentary films present ___.', ['Real events and information', 'Only entirely fictional events with no factual basis', 'A genre unrelated to real-world subjects', 'Content with no connection to any actual events'], 0),
   ('Why might a documentary filmmaker’s choices in editing shape how audiences interpret the subject?', ['Editing decisions can influence pacing, emphasis, and the overall narrative presented', 'Editing has no effect on how a documentary is understood', 'Documentary filmmakers never make deliberate editing choices', 'These choices have no connection to audience interpretation'], 0),
   ('Which is an example of a technique a documentary might use to shape audience perception?', ['Selecting specific interview clips to support a particular perspective', 'Presenting information with absolutely no editorial choices involved', 'A technique entirely unrelated to filmmaking', 'Avoiding any use of narration or interviews'], 0),
   ('Why is it valuable to critically analyze a documentary rather than accepting its content at face value?', ['Even factual content can be presented in a way that reflects a particular point of view', 'Documentaries always present information with no possible bias', 'Critical analysis has no value when studying documentary film', 'Documentaries never involve any filmmaker perspective or choices'], 0),
   ('Why might understanding a documentary’s intended audience help in analyzing its purpose?', ['The intended audience can influence the tone, content, and framing choices used', 'The audience has no connection to how a documentary is made', 'This factor is irrelevant to understanding a documentary’s purpose', 'Documentaries are always made with no audience in mind'], 0)]),
F('Rational Functions: Solving Rational Equations',
  'Grade 11 Functions strand: solving a rational equation involves eliminating the denominators to form a simpler equation, while checking for any restrictions that would make the original denominators equal to zero.',
  [('Solving a rational equation typically involves ___.', ['Eliminating the denominators to form a simpler equation', 'Ignoring the denominators entirely', 'A method unrelated to fractions or denominators', 'Adding denominators without ever removing them'], 0),
   ('Why is it important to check for restrictions when solving a rational equation?', ['A solution that makes any original denominator equal to zero must be excluded', 'Restrictions have no effect on the solutions of a rational equation', 'Rational equations never have any restricted values', 'All possible solutions are always valid for a rational equation'], 0),
   ('If solving a rational equation produces a solution that makes the original denominator zero, this solution is ___.', ['An extraneous solution that must be rejected', 'Always a valid solution with no exceptions', 'Impossible to identify through any method', 'A solution unrelated to the original equation’s domain'], 0),
   ('Why might multiplying both sides of a rational equation by the least common denominator be a useful strategy?', ['It clears the fractions, making the equation easier to solve using standard algebraic methods', 'This strategy has no effect on solving a rational equation', 'Rational equations can never be simplified using this method', 'Multiplying by the denominator always makes an equation impossible to solve'], 0),
   ('Why are rational equations useful for modelling situations involving combined work rates, like two people completing a task together?', ['They can represent how combined rates affect the total time needed to complete a task', 'Rational equations have no real-world modelling applications', 'Work rate problems can never be represented using equations', 'This type of equation only applies to purely abstract mathematics'], 0)]),
B('Ecology: Biomes and Global Ecosystems',
  'Grade 11 Biology strand: a biome is a large geographic region characterized by a distinct climate and community of plants and animals adapted to those specific conditions.',
  [('A biome is best described as ___.', ['A large geographic region with a distinct climate and community of organisms', 'A single, isolated organism with no connection to its environment', 'A concept unrelated to geography or climate', 'A term with no connection to plant or animal life'], 0),
   ('Organisms within a biome are typically adapted to ___.', ['The specific climate conditions of that region', 'No particular environmental conditions at all', 'Conditions entirely unrelated to their biome', 'A climate completely different from their own biome'], 0),
   ('Which is an example of a biome?', ['A tropical rainforest', 'A concept unrelated to any specific region', 'A term with no connection to climate or ecosystems', 'A single tree with no broader ecological context'], 0),
   ('Why might different biomes have very different types of plant and animal life?', ['Organisms evolve adaptations suited to the specific climate and conditions of their biome', 'All biomes have identical climate conditions, resulting in similar organisms', 'Biomes have no influence on the types of organisms found within them', 'This concept has no connection to evolution or adaptation'], 0),
   ('Why is studying global biomes important for understanding the impact of climate change?', ['Changes in climate can significantly alter the conditions that define and support each biome', 'Biomes have no connection to climate or environmental change', 'Climate change has no effect on global ecosystems', 'This topic has no relevance to environmental science'], 0)]),
C('Reaction Rates: Factors Affecting Rate of Reaction',
  'Grade 11 Chemistry strand: the rate of a chemical reaction can be influenced by factors such as temperature, concentration, surface area, and the presence of a catalyst.',
  [('Which factor can influence the rate of a chemical reaction?', ['Temperature', 'The colour of the container used', 'The time of day the reaction takes place', 'A factor entirely unrelated to chemical reactions'], 0),
   ('Increasing the temperature of a reaction generally ___ its rate.', ['Increases', 'Decreases', 'Has no effect on', 'Makes impossible to determine'], 0),
   ('A catalyst affects a reaction’s rate by ___.', ['Providing an alternative pathway with lower activation energy', 'Being consumed completely during the reaction', 'Having no effect on the reaction whatsoever', 'Increasing the amount of reactants needed'], 0),
   ('Why might increasing the surface area of a solid reactant increase the rate of a reaction?', ['More surface area allows for more collisions between reactant particles', 'Surface area has no effect on the rate of a chemical reaction', 'Increasing surface area always decreases the number of particle collisions', 'This factor has no connection to how reactions occur'], 0),
   ('Why is understanding factors that affect reaction rate useful in industries like food preservation?', ['Controlling these factors can help slow down unwanted reactions, like spoilage', 'Reaction rate factors have no application in food preservation', 'Food preservation never involves controlling chemical reaction rates', 'This concept only applies to purely theoretical chemistry'], 0)])]),

day(34, [
E('Grammar and Style: Advanced Syntax for Impact',
  'Grade 11 English strand: advanced syntax involves deliberately varying sentence structure and length to create specific effects, such as emphasis, tension, or a particular rhythm in writing.',
  [('Advanced syntax involves deliberately varying ___.', ['Sentence structure and length', 'Only the topic of a piece of writing', 'The font used in a written document', 'A factor unrelated to sentence construction'], 0),
   ('Why might a writer use a short, abrupt sentence after a series of longer ones?', ['It can create emphasis or a sense of tension for the reader', 'Short sentences always weaken the impact of a piece of writing', 'Sentence length has no effect on how writing is experienced', 'This technique has no connection to creating emphasis'], 0),
   ('Which is an example of a syntactic technique used to create rhythm in writing?', ['Repeating a similar sentence structure across several sentences', 'Using completely random, unrelated sentence structures throughout', 'Avoiding any variation in sentence length', 'A technique unrelated to sentence construction'], 0),
   ('Why is understanding advanced syntax valuable for a writer aiming for a specific tone or effect?', ['Deliberate sentence choices can reinforce the emotional or rhetorical impact of the writing', 'Syntax has no connection to tone or emotional effect in writing', 'Advanced syntax should always be avoided in effective writing', 'Sentence structure has no influence on how a piece of writing is received'], 0),
   ('Why might analyzing an author’s syntax be a valuable part of literary analysis?', ['It can reveal how sentence-level choices contribute to meaning and effect', 'Syntax has no connection to literary meaning', 'Analyzing sentence structure provides no useful insight into a text', 'This element of a text is never worth close analysis'], 0)]),
F('Exponential Functions: Modelling Population and Decay',
  'Grade 11 Functions strand: exponential functions can model population growth, which increases by a consistent percentage rate, and radioactive decay, which decreases by a consistent percentage rate over time.',
  [('Exponential population growth models a population that increases by ___.', ['A consistent percentage rate over time', 'A fixed, identical amount each time period', 'A completely random and unpredictable amount', 'No growth at all, remaining constant'], 0),
   ('Radioactive decay is modelled using an exponential function that ___.', ['Decreases by a consistent percentage rate over time', 'Increases by a fixed amount each time period', 'Remains completely unchanged over time', 'Changes at a completely random rate'], 0),
   ('Why might exponential growth eventually become unrealistic as a long-term model for a population?', ['Real populations often face limiting factors, like resources, that slow growth over time', 'Populations can grow exponentially forever with no limiting factors', 'Exponential growth always accurately predicts population changes indefinitely', 'This concept has no connection to real-world population dynamics'], 0),
   ('The half-life of a radioactive substance refers to ___.', ['The time it takes for half of the substance to decay', 'The total amount of time before any decay begins', 'A period with no connection to radioactive decay', 'The complete disappearance of the substance'], 0),
   ('Why are exponential models useful for predicting future values in situations like population growth or radioactive decay?', ['They capture the pattern of percentage-based change common in these real-world processes', 'Exponential models have no real-world predictive value', 'These situations can never be accurately modelled mathematically', 'This type of function only applies to purely abstract mathematics'], 0)]),
B('Physiology: Excretory System and Homeostasis',
  'Grade 11 Biology strand: the excretory system removes metabolic waste products from the body, playing a key role in maintaining homeostasis by regulating water balance and filtering the blood.',
  [('The excretory system’s primary role is to ___.', ['Remove metabolic waste products from the body', 'Produce new waste products for the body to use', 'A role entirely unrelated to waste removal', 'Have no connection to maintaining bodily functions'], 0),
   ('The excretory system contributes to homeostasis by regulating ___.', ['Water balance and filtering the blood', 'A factor entirely unrelated to internal body processes', 'Only external temperature, with no other function', 'A process with no connection to bodily fluids'], 0),
   ('Which organ plays a central role in the excretory system?', ['The kidney', 'The heart', 'The stomach', 'An organ unrelated to waste filtration'], 0),
   ('Why is maintaining proper water balance important for overall body function?', ['Imbalances can affect cell function and the concentration of substances in the blood', 'Water balance has no connection to how cells or organs function', 'The body never needs to regulate its water balance', 'This concept has no relevance to homeostasis'], 0),
   ('Why might kidney dysfunction significantly affect a person’s overall health?', ['The kidneys play a critical role in filtering waste and maintaining fluid and electrolyte balance', 'Kidney function has no connection to overall health', 'The excretory system has no significant role in the body', 'This organ system has no connection to homeostasis'], 0)]),
C('Solutions: Colligative Properties',
  'Grade 11 Chemistry strand: colligative properties, such as boiling point elevation and freezing point depression, depend on the number of dissolved particles in a solution rather than their specific identity.',
  [('Colligative properties depend on ___.', ['The number of dissolved particles in a solution', 'The specific chemical identity of the dissolved particles', 'The colour of the solution only', 'A factor unrelated to dissolved substances'], 0),
   ('Boiling point elevation refers to ___.', ['An increase in a solution’s boiling point compared to the pure solvent', 'A decrease in a solution’s boiling point compared to the pure solvent', 'No change at all in a solution’s boiling point', 'A concept unrelated to dissolved substances'], 0),
   ('Why does adding salt to water lower its freezing point?', ['The dissolved particles disrupt the formation of the solid’s regular structure, requiring a lower temperature to freeze', 'Salt has no effect on the freezing point of water', 'Adding salt always raises the freezing point of water', 'This effect has no connection to the number of dissolved particles'], 0),
   ('Why might colligative properties be relevant to using salt on icy roads in winter?', ['Salt lowers the freezing point of water, helping prevent ice formation at colder temperatures', 'Salt has no practical application for managing icy conditions', 'Colligative properties have no real-world relevance', 'This concept only applies to purely theoretical chemistry'], 0),
   ('Why is it useful to understand that colligative properties depend on particle count rather than particle identity?', ['It helps predict how different solutes will affect properties like freezing and boiling points based on concentration', 'This distinction has no relevance to predicting solution properties', 'Colligative properties are always identical regardless of particle count', 'Only certain specific solutes ever affect colligative properties'], 0)])]),

day(35, [
E('Literature: The Bildungsroman -- Coming-of-Age Narratives',
  'Grade 11 English strand: a bildungsroman is a novel that focuses on a protagonist’s psychological and moral growth from youth to adulthood, often centred on themes of identity and self-discovery.',
  [('A bildungsroman is a novel focused on a protagonist’s ___.', ['Psychological and moral growth from youth to adulthood', 'A journey with no connection to personal growth', 'A single, unchanging characteristic throughout the story', 'A plot entirely unrelated to identity or self-discovery'], 0),
   ('Common themes explored in a bildungsroman include ___.', ['Identity and self-discovery', 'Themes entirely unrelated to personal development', 'Only historical events with no personal focus', 'A concept unrelated to character growth'], 0),
   ('Why might readers connect strongly with bildungsroman narratives?', ['The themes of growth and self-discovery often resonate with universal human experiences', 'These narratives have no connection to relatable human experiences', 'Readers never form a connection with coming-of-age stories', 'This type of narrative offers no emotional resonance for readers'], 0),
   ('Which is an example of an event that might occur in a bildungsroman?', ['The protagonist facing a significant challenge that changes their understanding of themselves', 'A story with no meaningful character development at all', 'An event entirely unrelated to personal growth', 'A plot that remains completely unchanged from beginning to end'], 0),
   ('Why is the bildungsroman considered a significant and enduring literary form?', ['It captures a universal experience of growth and change that continues to resonate across generations', 'This literary form has no lasting significance', 'Coming-of-age narratives are rarely explored in literature', 'This genre has no connection to broader literary traditions'], 0)]),
F('Sequences: Recursive Formulas and Applications',
  'Grade 11 Functions strand: a recursive formula defines each term of a sequence based on one or more previous terms, requiring the value of prior terms to calculate subsequent ones.',
  [('A recursive formula defines each term of a sequence based on ___.', ['One or more previous terms', 'No connection to any other term in the sequence', 'Only the very first term, with no other relationship', 'A term unrelated to the sequence itself'], 0),
   ('To find a specific term using a recursive formula, you generally need to ___.', ['Calculate all preceding terms in order', 'Skip directly to that term with no other calculation needed', 'Ignore all previous terms in the sequence', 'Use a method entirely unrelated to the sequence’s pattern'], 0),
   ('Which is an example of a well-known sequence often defined recursively?', ['The Fibonacci sequence', 'A sequence with no defined mathmatical pattern', 'A sequence unrelated to recursive definitions', 'Any sequence with a constant, unchanging value'], 0),
   ('Why might a recursive formula be more suitable than an explicit formula for describing certain real-world processes, like compound interest calculated annually?', ['These processes often naturally depend on the previous period’s value to determine the next', 'Recursive formulas are never useful for modelling real-world processes', 'Compound interest can never be represented using a recursive relationship', 'This concept has no connection to sequences or patterns'], 0),
   ('Why is understanding recursive formulas useful in computer science and programming?', ['Many programming techniques rely on defining a process in terms of smaller, similar steps', 'Recursive formulas have no connection to computer science', 'Programming never involves any form of repeated or step-based calculation', 'This mathematical concept has no practical application in technology'], 0)]),
B('Animal Physiology: Muscular and Skeletal Systems',
  'Grade 11 Biology strand: the muscular and skeletal systems work together to provide the body with structure, support, and the ability to move, with muscles contracting to pull on bones connected at joints.',
  [('The muscular and skeletal systems work together to provide the body with ___.', ['Structure, support, and the ability to move', 'No structural support of any kind', 'A function entirely unrelated to movement', 'Only protection, with no role in movement'], 0),
   ('Muscles enable movement by ___.', ['Contracting to pull on bones connected at joints', 'Expanding permanently with no ability to contract', 'A process entirely unrelated to bones or joints', 'Remaining completely still at all times'], 0),
   ('A joint is best described as ___.', ['A point where two or more bones meet, allowing movement', 'A type of muscle tissue', 'A structure unrelated to the skeletal system', 'A point where bones are permanently fused with no movement possible'], 0),
   ('Why is the skeletal system important beyond just supporting movement?', ['It also protects internal organs and plays a role in processes like blood cell production', 'The skeletal system has no function beyond supporting movement', 'Bones have no connection to protecting internal organs', 'This system has no role in any bodily process besides movement'], 0),
   ('Why might understanding the muscular and skeletal systems be important for fields like physiotherapy?', ['It helps professionals diagnose and treat injuries or conditions affecting movement and structure', 'These systems have no relevance to physiotherapy or injury treatment', 'Physiotherapy never involves an understanding of muscles or bones', 'This knowledge has no practical, real-world application'], 0)]),
C('Organic Chemistry: Isomers and Naming Conventions',
  'Grade 11 Chemistry strand: isomers are compounds with the same molecular formula but different structural arrangements, and organic naming conventions provide a systematic way to name these compounds based on their structure.',
  [('Isomers are compounds that share the same ___.', ['Molecular formula but have different structural arrangements', 'Molecular formula and identical structural arrangement in every case', 'Physical appearance, with no connection to their chemical formula', 'Chemical properties, with no variation between them at all'], 0),
   ('Organic naming conventions provide a systematic way to ___.', ['Name compounds based on their structure', 'Randomly assign names with no connection to structure', 'A process unrelated to naming chemical compounds', 'Identify only the colour of a compound'], 0),
   ('Why might two isomers with the same molecular formula have different physical or chemical properties?', ['Their different structural arrangements can affect how the molecules interact and behave', 'Isomers always have identical properties regardless of structure', 'Structural arrangement has no effect on a molecule’s properties', 'This concept has no connection to molecular structure'], 0),
   ('Why is a systematic naming system important in organic chemistry?', ['It allows chemists to communicate clearly and consistently about specific molecular structures', 'A systematic naming system provides no benefit to chemists', 'Organic compounds require no formal naming system', 'This system has no connection to identifying molecular structures'], 0),
   ('Why might isomerism be relevant in fields like pharmaceuticals?', ['Different isomers of the same drug can sometimes have significantly different effects on the body', 'Isomerism has no relevance to how pharmaceuticals function', 'All isomers of a compound always behave identically in the body', 'This concept only applies to purely theoretical chemistry'], 0)])]),

day(36, [
E('Oral Communication: Impromptu Speaking and Critical Response',
  'Grade 11 English strand: impromptu speaking requires organizing and delivering a coherent response to a topic with little to no preparation time, drawing on quick critical thinking skills.',
  [('Impromptu speaking requires responding to a topic with ___.', ['Little to no preparation time', 'Extensive preparation over several weeks', 'No connection to critical thinking at all', 'A fully written and memorized script'], 0),
   ('Why is quick critical thinking important for effective impromptu speaking?', ['It helps the speaker organize their thoughts and respond coherently under time pressure', 'Critical thinking has no role in impromptu speaking', 'Impromptu speeches require no organization of thought at all', 'This skill is only relevant to prepared, scripted speeches'], 0),
   ('Which is a useful strategy for organizing an impromptu response quickly?', ['Briefly outlining two or three key points before speaking', 'Speaking with no plan or structure at all', 'Avoiding any structure or organization', 'Repeating the same point multiple times with no development'], 0),
   ('Why might practising impromptu speaking build confidence in other communication situations?', ['It develops the ability to think and respond clearly under pressure, a skill useful in many contexts', 'Impromptu speaking practice has no connection to other communication skills', 'This skill is only useful in a formal debate setting', 'Confidence in communication has no connection to this type of practice'], 0),
   ('Why is critical response an important component of impromptu speaking?', ['It requires the speaker to genuinely evaluate and form a thoughtful position on the topic', 'Critical response has no role in impromptu speaking', 'A response can be effective with no actual evaluation of the topic', 'This element has no connection to quick, effective communication'], 0)]),
F('Financial Mathematics: Annuities and Present Value',
  'Grade 11 Functions strand (Financial Applications): an annuity is a series of equal payments made at regular intervals, and present value calculates what a series of future payments is worth in today’s dollars.',
  [('An annuity is best described as ___.', ['A series of equal payments made at regular intervals', 'A single, one-time payment with no repetition', 'A concept unrelated to regular payments', 'A payment made at completely random, irregular intervals'], 0),
   ('Present value calculates what a series of future payments is worth in ___.', ['Today’s dollars', 'A currency unrelated to the original payments', 'Only the exact value of the very last payment', 'A value with no connection to the timing of payments'], 0),
   ('Why is the concept of present value useful when comparing different financial options?', ['It allows for a fair comparison of amounts of money received at different points in time', 'Present value has no use in comparing financial options', 'Money is always worth the exact same amount regardless of when it is received', 'This concept only applies to purely theoretical mathematics'], 0),
   ('Which is an example of a real-world application of an annuity?', ['Regular retirement savings contributions', 'A single, one-time lottery payout with no further payments', 'A concept unrelated to personal finance', 'A payment structure that never involves any regular schedule'], 0),
   ('Why might understanding annuities and present value be valuable in personal financial planning?', ['These concepts help evaluate the true value of savings, loans, and investment options over time', 'Financial mathematics has no practical relevance to personal life', 'Annuities and present value calculations serve no useful financial purpose', 'This knowledge has no connection to making informed financial decisions'], 0)]),
B('Genetics: Gene Expression and Regulation',
  'Grade 11 Biology strand: gene expression is the process by which information in a gene is used to produce a functional product, and gene regulation controls when and how much a gene is expressed.',
  [('Gene expression is the process by which ___.', ['Information in a gene is used to produce a functional product', 'A gene is permanently deactivated with no further function', 'A concept unrelated to genetic information', 'DNA is entirely removed from a cell'], 0),
   ('Gene regulation controls ___.', ['When and how much a gene is expressed', 'Only the physical location of a gene within a cell', 'A factor entirely unrelated to gene activity', 'Whether a gene exists within an organism’s DNA'], 0),
   ('Why might not all genes in a cell be actively expressed at the same time?', ['Different genes are needed for different cell functions or at different developmental stages', 'All genes in every cell are always expressed identically at all times', 'Gene regulation has no connection to when genes are active', 'This concept has no relevance to how cells function'], 0),
   ('Which is an example of a factor that might influence gene regulation?', ['Environmental signals affecting a cell', 'A factor entirely unrelated to genetics', 'The colour of the organism’s exterior only', 'A concept unrelated to cellular processes'], 0),
   ('Why is understanding gene expression and regulation important in fields like cancer research?', ['Abnormal gene expression can contribute to uncontrolled cell growth seen in cancer', 'Gene expression has no connection to cancer research', 'This concept has no relevance to understanding disease', 'Cancer research never considers how genes are expressed or regulated'], 0)]),
C('Acids and Bases: Titration Curves',
  'Grade 11 Chemistry strand: a titration curve graphs the pH of a solution as an acid or base is gradually added, showing key points like the equivalence point where the reaction is complete.',
  [('A titration curve graphs a solution’s ___.', ['pH as an acid or base is gradually added', 'Colour as it changes over time with no connection to pH', 'Temperature as it changes with no connection to the reaction', 'Volume with no connection to pH change'], 0),
   ('The equivalence point on a titration curve represents ___.', ['The point where the acid-base reaction is complete', 'The very beginning of the titration process', 'A point with no chemical significance', 'The moment the reaction stops occurring entirely'], 0),
   ('Why might the shape of a titration curve differ between a strong acid and a weak acid?', ['Their differing degrees of ionization affect how pH changes throughout the titration', 'Titration curves are always identical regardless of acid strength', 'Acid strength has no effect on the shape of a titration curve', 'This concept has no connection to acid-base chemistry'], 0),
   ('Why is identifying the equivalence point useful in a titration experiment?', ['It helps determine the exact concentration of the unknown solution being tested', 'The equivalence point provides no useful information about a solution', 'Titration experiments never require identifying a specific point on the curve', 'This concept has no connection to determining concentration'], 0),
   ('Why might an indicator be used alongside a titration curve in a laboratory setting?', ['An indicator can visually signal when the equivalence point has been reached', 'Indicators have no connection to titration experiments', 'A titration curve alone always provides all necessary information with no indicator needed', 'This tool has no practical use in chemistry experiments'], 0)])]),

day(37, [
E('Writing: The Personal Essay -- Voice and Vulnerability',
  'Grade 11 English strand: a personal essay explores the writer’s own experiences and reflections with an honest, distinctive voice, often embracing vulnerability to create a genuine connection with readers.',
  [('A personal essay explores ___.', ['The writer’s own experiences and reflections', 'A completely fictional and unrelated topic', 'Only factual information with no personal reflection', 'A subject entirely disconnected from the writer’s own life'], 0),
   ('Why might embracing vulnerability strengthen a personal essay?', ['It can create a more genuine and relatable connection with readers', 'Vulnerability always weakens the impact of a personal essay', 'Readers never respond to honest or vulnerable writing', 'This quality has no connection to how an essay is received'], 0),
   ('Why is a distinctive voice important in a personal essay?', ['It reflects the writer’s unique perspective, making the essay feel authentic', 'A distinctive voice has no role in personal essay writing', 'All personal essays should sound identical, with no unique voice', 'Voice has no effect on how an essay is experienced by readers'], 0),
   ('Which is an example of an effective personal essay topic?', ['A meaningful challenge that shaped the writer’s perspective', 'A topic with no connection to the writer’s own experience', 'A subject entirely unrelated to personal reflection', 'An essay that avoids any personal connection to its content'], 0),
   ('Why might reflecting honestly on a difficult experience be valuable when writing a personal essay?', ['Honest reflection can lead to deeper insight and a more meaningful piece of writing', 'Honesty has no connection to the quality of a personal essay', 'Personal essays should always avoid discussing any difficult experiences', 'Reflection provides no benefit to this type of writing'], 0)]),
F('Statistics: Standard Deviation and Data Interpretation',
  'Grade 11 Functions strand (Data Management): standard deviation quantifies how spread out a set of data values is, helping interpret whether data is tightly clustered or widely dispersed around the mean.',
  [('Standard deviation quantifies ___.', ['How spread out a set of data values is', 'The exact total sum of all values in a data set', 'The single highest value in a data set', 'A value unrelated to data spread'], 0),
   ('A high standard deviation suggests that data values are ___.', ['Widely dispersed from the mean', 'Tightly clustered around the mean', 'Completely unrelated to the mean', 'Impossible to measure accurately'], 0),
   ('Why is standard deviation a useful measure alongside the mean when interpreting a data set?', ['It provides additional context about the consistency or variability of the data', 'Standard deviation provides no additional useful information', 'The mean alone always fully describes a data set', 'This measure has no connection to interpreting data'], 0),
   ('Which is an example of a situation where understanding standard deviation would be useful?', ['Comparing the consistency of test scores between two different classes', 'A situation with no connection to data analysis', 'A scenario that requires no interpretation of numerical data', 'A situation where only the total sum of values matters'], 0),
   ('Why might two data sets have the same mean but very different standard deviations?', ['The individual data values can be spread out very differently even if their average is the same', 'The mean and standard deviation are always identical for any two data sets', 'Standard deviation has no connection to how data values are distributed', 'This situation could never occur in real data sets'], 0)]),
B('Biotechnology: Genetic Testing and Ethics',
  'Grade 11 Biology strand: genetic testing analyzes an individual’s DNA to identify potential genetic conditions or traits, raising important ethical questions about privacy, consent, and the use of this information.',
  [('Genetic testing analyzes an individual’s DNA to identify ___.', ['Potential genetic conditions or traits', 'A factor entirely unrelated to genetics', 'Only external physical characteristics, with no genetic connection', 'Information unrelated to a person’s health'], 0),
   ('Genetic testing raises ethical questions related to ___.', ['Privacy, consent, and the use of genetic information', 'No ethical considerations of any kind', 'A topic entirely unrelated to personal information', 'Concerns with no connection to genetics or health'], 0),
   ('Why might privacy be a significant ethical concern related to genetic testing?', ['Genetic information can reveal sensitive details about a person’s health and even their family members', 'Genetic information has no connection to personal privacy', 'Privacy concerns have no relevance to genetic testing', 'This type of information is never considered sensitive'], 0),
   ('Why is informed consent important before someone undergoes genetic testing?', ['It ensures the individual understands the potential implications of the test results', 'Consent has no relevance to genetic testing procedures', 'Genetic testing never requires any form of consent', 'This concept has no connection to ethical considerations in genetics'], 0),
   ('Why might genetic testing be relevant to decisions about future health care?', ['Results can help identify risks for certain conditions, informing preventative care or treatment decisions', 'Genetic testing has no connection to health care decisions', 'This type of testing provides no useful information for health care', 'Genetic information is never used to inform medical decisions'], 0)]),
C('Redox Reactions: Balancing and Applications',
  'Grade 11 Chemistry strand: a redox (oxidation-reduction) reaction involves the transfer of electrons between substances, with oxidation involving electron loss and reduction involving electron gain.',
  [('In a redox reaction, oxidation involves ___.', ['The loss of electrons', 'The gain of electrons', 'No change in electrons at all', 'A process unrelated to electron transfer'], 0),
   ('In a redox reaction, reduction involves ___.', ['The gain of electrons', 'The loss of electrons', 'No change in electrons at all', 'A process unrelated to electron transfer'], 0),
   ('Why must a redox reaction always involve both oxidation and reduction occurring together?', ['Electrons lost by one substance must be gained by another', 'Oxidation and reduction can each occur completely independently, with no connection to each other', 'Redox reactions never involve any transfer of electrons', 'This pairing has no connection to how electron transfer works'], 0),
   ('Which is an example of a practical application of redox reactions?', ['Batteries generating electric current', 'A process entirely unrelated to electron transfer', 'A concept with no real-world applications', 'An application unrelated to chemistry'], 0),
   ('Why is balancing a redox equation important in chemistry?', ['It ensures the number of electrons lost equals the number of electrons gained', 'Balancing has no effect on the accuracy of a redox equation', 'Redox equations never require any balancing', 'This concept has no connection to accurately representing a reaction'], 0)])]),

day(38, [
E('Independent Reading: Speculative Fiction',
  'Grade 11 English strand: speculative fiction imagines alternative realities, futures, or worlds governed by different rules, often used to explore complex social, ethical, or philosophical questions.',
  [('Speculative fiction imagines ___.', ['Alternative realities, futures, or worlds', 'Only realistic, present-day settings with no imaginative elements', 'A genre unrelated to imaginative storytelling', 'Stories that must always be set in the past'], 0),
   ('Authors often use speculative fiction to explore ___.', ['Complex social, ethical, or philosophical questions', 'A topic entirely unrelated to real-world concerns', 'Only lighthearted, comedic subject matter with no deeper meaning', 'Themes with no connection to society or ethics'], 0),
   ('Which is an example of a subgenre that falls under speculative fiction?', ['Science fiction', 'A genre entirely unrelated to imaginative storytelling', 'Only strictly historical, factual writing', 'A category with no connection to alternative worlds'], 0),
   ('Why might readers find speculative fiction a useful lens for examining real-world issues?', ['Imagining alternative scenarios can highlight and critique aspects of the real world in a new way', 'Speculative fiction has no connection to real-world issues', 'This genre never engages with any meaningful themes', 'Readers gain no insight from exploring imagined worlds'], 0),
   ('Why is world-building often an important skill for authors of speculative fiction?', ['A well-developed alternative world can make the story’s themes and ideas more compelling and believable', 'World-building has no connection to how a speculative story is received', 'Authors of speculative fiction never need to develop a story’s setting', 'This skill has no relevance to this genre of writing'], 0)]),
F('Functions: Inverse Functions and Their Graphs',
  'Grade 11 Functions strand: an inverse function reverses the input-output relationship of the original function, and its graph is a reflection of the original function’s graph across the line y equals x.',
  [('An inverse function reverses ___.', ['The input-output relationship of the original function', 'No relationship at all with the original function', 'Only the colour of the original function’s graph', 'A concept unrelated to functions'], 0),
   ('The graph of an inverse function is a reflection of the original function’s graph across ___.', ['The line y equals x', 'The x-axis only', 'The y-axis only', 'A line unrelated to the original graph'], 0),
   ('If a function has an ordered pair (2, 5), its inverse function will have the ordered pair ___.', ['(5, 2)', '(2, 5)', '(-2, -5)', '(5, -2)'], 0),
   ('Why must a function be one-to-one for its inverse to also be a function?', ['A one-to-one function ensures each output corresponds to exactly one input, which the inverse relationship requires', 'One-to-one functions have no connection to inverse functions', 'Every function automatically has an inverse that is also a function', 'This property has no relevance to determining whether an inverse exists'], 0),
   ('Why might understanding inverse functions be useful for converting between units, like Celsius and Fahrenheit?', ['An inverse function allows you to reverse a known conversion relationship to go in the opposite direction', 'Inverse functions have no practical use for unit conversion', 'Converting between units never involves any functional relationship', 'This concept only applies to purely abstract mathematics'], 0)]),
B('Evolution: Evidence from the Fossil Record',
  'Grade 11 Biology strand: the fossil record provides physical evidence of past life forms, helping scientists trace evolutionary changes and relationships between species over long periods of time.',
  [('The fossil record provides physical evidence of ___.', ['Past life forms', 'Only currently living organisms, with no connection to the past', 'A concept unrelated to biological history', 'Modern organisms exclusively, with no historical evidence'], 0),
   ('Scientists use the fossil record to trace ___.', ['Evolutionary changes and relationships between species', 'A topic entirely unrelated to biology', 'Only the current population size of a species', 'A concept with no connection to species relationships'], 0),
   ('Why might transitional fossils be considered particularly significant evidence for evolution?', ['They can show intermediate characteristics between two different groups of organisms', 'Transitional fossils have no scientific significance', 'These fossils provide no evidence related to evolutionary change', 'This type of fossil has no connection to species relationships'], 0),
   ('Why is the fossil record sometimes considered incomplete by scientists?', ['Not all organisms fossilize well, and many fossils may not yet have been discovered', 'The fossil record is always considered completely comprehensive with no gaps', 'Fossilization occurs for every single organism that has ever lived', 'This concept has no connection to the limitations of fossil evidence'], 0),
   ('Why do scientists use multiple types of evidence, including fossils and DNA comparisons, to study evolution?', ['Combining different types of evidence strengthens conclusions about evolutionary relationships', 'Fossil evidence alone is always sufficient with no other evidence required', 'DNA evidence has no connection to studying evolutionary history', 'Using multiple types of evidence provides no additional scientific benefit'], 0)]),
C('Thermochemistry: Calorimetry and Hess’s Law',
  'Grade 11 Chemistry strand: calorimetry measures the heat exchanged during a chemical reaction, and Hess’s Law states that the total enthalpy change for a reaction is the same regardless of the number of steps taken.',
  [('Calorimetry is used to measure ___.', ['The heat exchanged during a chemical reaction', 'The exact colour of a chemical reaction', 'The mass of the reactants only, with no connection to heat', 'A property entirely unrelated to energy changes'], 0),
   ('Hess’s Law states that the total enthalpy change for a reaction ___.', ['Is the same regardless of the number of steps taken', 'Always changes depending on how many steps are involved', 'Has no connection to the number of reaction steps', 'Cannot be determined using any method'], 0),
   ('Why is Hess’s Law useful for reactions where direct measurement of enthalpy change is difficult?', ['It allows the enthalpy change to be calculated indirectly using a series of known reactions', 'Hess’s Law provides no useful method for calculating enthalpy change', 'Reactions with difficult-to-measure enthalpy changes can never be analyzed', 'This law has no connection to determining energy changes in reactions'], 0),
   ('A calorimeter is best described as ___.', ['A device used to measure heat changes in a reaction', 'A device used to measure the colour of a solution', 'A tool unrelated to measuring energy changes', 'An instrument used only to measure mass'], 0),
   ('Why might calorimetry be useful in fields like food science, such as determining the caloric content of food?', ['It can measure the amount of heat energy released when a substance is broken down', 'Calorimetry has no practical application outside of a chemistry laboratory', 'Food science never involves measuring heat or energy content', 'This technique has no connection to measuring energy in a substance'], 0)])]),

day(39, [
E('Literature: Irony and Ambiguity in Modern Fiction',
  'Grade 11 English strand: modern fiction often employs irony and deliberate ambiguity, leaving certain meanings open to interpretation and inviting readers to actively engage with a text’s complexity.',
  [('Modern fiction often employs irony and ___.', ['Deliberate ambiguity', 'Only completely clear, unambiguous meaning throughout', 'A style with no connection to complexity', 'Themes with only one single, obvious interpretation'], 0),
   ('Deliberate ambiguity in a text leaves certain meanings ___.', ['Open to interpretation', 'Entirely fixed with only one possible reading', 'Completely absent from the text', 'A concept unrelated to how a text can be read'], 0),
   ('Why might an author intentionally use ambiguity in their writing?', ['It can invite readers to actively engage with and interpret the text’s deeper complexity', 'Ambiguity always makes a text less meaningful or engaging', 'Authors should always avoid any ambiguity in their writing', 'This technique has no effect on how readers engage with a text'], 0),
   ('Why might a story with an ambiguous ending be considered more thought-provoking than one with a clear resolution?', ['It can prompt readers to continue reflecting on and interpreting the story’s meaning', 'An ambiguous ending always makes a story less effective', 'Readers never continue thinking about a story after finishing it', 'This technique has no connection to how a reader experiences a text'], 0),
   ('Why is recognizing irony important when interpreting a modern work of fiction?', ['It can reveal a gap between what is stated and what is actually meant, adding depth to the text', 'Irony has no connection to a text’s deeper meaning', 'Recognizing irony never affects how a text is understood', 'Modern fiction never makes use of irony'], 0)]),
F('Trigonometric Identities: Proving and Applying',
  'Grade 11 Functions strand: a trigonometric identity is an equation involving trigonometric functions that is true for all values of the variable, and proving one involves manipulating one side to match the other.',
  [('A trigonometric identity is an equation that is true for ___.', ['All values of the variable', 'Only a single specific value of the variable', 'No values of the variable at all', 'A concept unrelated to trigonometric functions'], 0),
   ('Proving a trigonometric identity typically involves ___.', ['Manipulating one side of the equation to match the other', 'Simply guessing whether the equation is true with no proof', 'Ignoring one entire side of the equation completely', 'A method unrelated to algebraic manipulation'], 0),
   ('Which is a commonly used fundamental trigonometric identity?', ['Sine squared plus cosine squared equals one', 'Sine plus cosine always equals zero', 'Tangent is always equal to sine', 'An identity unrelated to sine or cosine'], 0),
   ('Why might rewriting a trigonometric expression using an identity be useful when solving an equation?', ['It can simplify the expression into a more manageable or solvable form', 'Rewriting an expression using an identity never simplifies a problem', 'Trigonometric identities have no practical use for solving equations', 'This method has no connection to simplifying trigonometric expressions'], 0),
   ('Why is practising the application of trigonometric identities valuable for solving more advanced problems?', ['It builds flexibility in manipulating trigonometric expressions in different problem-solving contexts', 'This practice has no connection to solving advanced trigonometric problems', 'Trigonometric identities are never useful beyond simple, isolated proofs', 'This skill has no relevance to more complex mathematical applications'], 0)]),
B('Plant Hormones: Auxins, Gibberellins, and Tropic Responses',
  'Grade 11 Biology strand: plant hormones regulate growth and development, coordinating responses to environmental stimuli such as light, gravity, and touch.',
  [('Plant hormones play a key role in regulating ___.', ['Growth and development', 'A process entirely unrelated to plant biology', 'Only the colour of a plant’s leaves', 'A function unrelated to environmental response'], 0),
   ('Plant hormones help coordinate responses to environmental stimuli such as ___.', ['Light, gravity, and touch', 'No environmental factors at all', 'A stimulus entirely unrelated to a plant’s surroundings', 'Only sound, with no other environmental factors'], 0),
   ('A plant’s growth toward a light source is an example of a response called ___.', ['Phototropism', 'Gravitropism', 'Thigmotropism', 'A response unrelated to environmental stimuli'], 0),
   ('Why might understanding plant hormones be useful in agriculture?', ['It can help optimize plant growth, flowering, and fruit development for crop production', 'Plant hormones have no practical application in agriculture', 'Agriculture never involves any understanding of plant biology', 'This knowledge has no connection to improving crop yields'], 0),
   ('Why do plants need to respond to environmental stimuli like gravity and light?', ['These responses help plants orient themselves for optimal growth and resource access', 'Plants have no need to respond to their environment in any way', 'Environmental stimuli have no effect on how plants grow', 'This concept has no relevance to plant survival'], 0)]),
C('Environmental Chemistry: Ozone and Greenhouse Gases',
  'Grade 11 Chemistry strand: the ozone layer protects Earth from harmful ultraviolet radiation, while greenhouse gases trap heat in the atmosphere, both playing significant roles in Earth’s environmental chemistry.',
  [('The ozone layer primarily protects Earth from ___.', ['Harmful ultraviolet radiation', 'Only visible light, with no connection to radiation', 'A factor entirely unrelated to solar radiation', 'Excess oxygen in the atmosphere'], 0),
   ('Greenhouse gases contribute to climate change by ___.', ['Trapping heat in the atmosphere', 'Releasing heat completely out of the atmosphere', 'Having no effect on atmospheric temperature', 'A process entirely unrelated to atmospheric heat'], 0),
   ('Which is an example of a greenhouse gas?', ['Carbon dioxide', 'Nitrogen', 'A gas entirely unrelated to the atmosphere', 'Only pure oxygen, with no other gases considered'], 0),
   ('Why has the depletion of the ozone layer been a significant environmental concern?', ['Reduced ozone allows more harmful ultraviolet radiation to reach Earth’s surface', 'Ozone depletion has no connection to ultraviolet radiation exposure', 'The ozone layer has no protective function for Earth', 'This concern has no relevance to environmental chemistry'], 0),
   ('Why is understanding the chemistry of greenhouse gases important for addressing climate change?', ['It helps identify the specific compounds contributing to atmospheric heat trapping, guiding solutions', 'Greenhouse gas chemistry has no connection to addressing climate change', 'Climate change has no relationship to atmospheric chemical composition', 'This knowledge provides no useful information for environmental policy'], 0)])]),

day(40, [
E('Writing: Editing and Proofreading for Precision',
  'Grade 11 English strand: editing focuses on improving a piece of writing’s clarity, organization, and word choice, while proofreading involves a final, careful check for grammar, spelling, and punctuation errors.',
  [('Editing focuses on improving a piece of writing’s ___.', ['Clarity, organization, and word choice', 'Only its physical page length', 'A factor entirely unrelated to writing quality', 'The font style used throughout the document'], 0),
   ('Proofreading involves a final, careful check for ___.', ['Grammar, spelling, and punctuation errors', 'Only the overall length of a piece of writing', 'A factor unrelated to writing accuracy', 'Changing the entire argument of the piece'], 0),
   ('Why is it useful to complete editing before proofreading, rather than the other way around?', ['Editing addresses larger structural and content issues first, before focusing on smaller, surface-level errors', 'The order of these two steps has no effect on the writing process', 'Proofreading should always be completed before any editing takes place', 'These two processes are always identical, with no meaningful distinction'], 0),
   ('Which is an example of an editing change, as opposed to a proofreading change?', ['Reorganizing a paragraph for clearer logical flow', 'Correcting a single misspelled word', 'Fixing a missing comma', 'Correcting a simple subject-verb agreement error'], 0),
   ('Why is careful proofreading important before submitting a final piece of writing?', ['Small errors can distract readers and undermine the credibility of the writing', 'Proofreading has no effect on how a piece of writing is received', 'Errors in grammar or spelling never affect a reader’s impression of a text', 'This final step is unnecessary once editing is complete'], 0)]),
F('Review: Functions, Trigonometry, and Financial Math',
  'Grade 11 Functions strand review: this lesson revisits piecewise functions, the unit circle, rational equations, exponential modelling, recursive sequences, annuities, standard deviation, inverse functions, and trigonometric identities.',
  [('A piecewise function is defined by ___.', ['Different expressions over different intervals of its domain', 'A single expression that applies to the entire domain', 'No defined expression at all', 'A concept unrelated to domain intervals'], 0),
   ('An annuity is best described as ___.', ['A series of equal payments made at regular intervals', 'A single, one-time payment with no repetition', 'A concept unrelated to regular payments', 'A payment made at completely random, irregular intervals'], 0),
   ('The graph of an inverse function is a reflection of the original function’s graph across ___.', ['The line y equals x', 'The x-axis only', 'The y-axis only', 'A line unrelated to the original graph'], 0),
   ('A trigonometric identity is an equation that is true for ___.', ['All values of the variable', 'Only a single specific value of the variable', 'No values of the variable at all', 'A concept unrelated to trigonometric functions'], 0),
   ('Why is it useful to review functions, trigonometry, and financial math together?', ['These related math concepts reinforce each other for stronger overall understanding', 'These topics have no connection to each other', 'Review is never useful in math', 'Each topic must be learned in complete isolation'], 0)]),
B('Review: Genetics, Ecology, and Physiology',
  'Grade 11 Biology strand review: this lesson revisits microbiology and immunity, CRISPR, biomes, the excretory system, gene expression, genetic testing ethics, the fossil record, and plant hormones.',
  [('CRISPR is a technology used to ___.', ['Precisely edit DNA sequences', 'Only observe DNA, with no ability to change it', 'A process entirely unrelated to genetics', 'Replace the need for any genetic material'], 0),
   ('A biome is best described as ___.', ['A large geographic region with a distinct climate and community of organisms', 'A single, isolated organism with no connection to its environment', 'A concept unrelated to geography or climate', 'A term with no connection to plant or animal life'], 0),
   ('Gene regulation controls ___.', ['When and how much a gene is expressed', 'Only the physical location of a gene within a cell', 'A factor entirely unrelated to gene activity', 'Whether a gene exists within an organism’s DNA'], 0),
   ('The fossil record provides physical evidence of ___.', ['Past life forms', 'Only currently living organisms, with no connection to the past', 'A concept unrelated to biological history', 'Modern organisms exclusively, with no historical evidence'], 0),
   ('Why is it useful to review genetics, ecology, and physiology topics together?', ['It reinforces how these interconnected biological concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in biology', 'Each topic must be studied with no connection to the others'], 0)]),
C('Review: Gas Laws, Bonding, and Reaction Rates',
  'Grade 11 Chemistry strand review: this lesson revisits gas laws, VSEPR theory, factors affecting reaction rate, colligative properties, isomers, titration curves, redox reactions, calorimetry, and environmental chemistry.',
  [('Boyle’s Law describes the relationship between a gas’s ___.', ['Pressure and volume, at constant temperature', 'Only temperature, with no connection to pressure', 'Mass and colour', 'A relationship unrelated to gas behaviour'], 0),
   ('VSEPR theory predicts a molecule’s ___.', ['Three-dimensional shape', 'Colour', 'Mass', 'A property unrelated to molecular structure'], 0),
   ('In a redox reaction, oxidation involves ___.', ['The loss of electrons', 'The gain of electrons', 'No change in electrons at all', 'A process unrelated to electron transfer'], 0),
   ('Hess’s Law states that the total enthalpy change for a reaction ___.', ['Is the same regardless of the number of steps taken', 'Always changes depending on how many steps are involved', 'Has no connection to the number of reaction steps', 'Cannot be determined using any method'], 0),
   ('Why is it useful to review gas laws, bonding, and reaction rates together?', ['It reinforces how these interconnected chemistry concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in chemistry', 'Each topic must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260725):
    """Same technique used for the earlier Phase 3 batches -- reassigns
    each question's correct-answer slot via a shuffled round-robin (even
    across 0-3) and shuffles the wrong options into the remaining slots.
    Question and option TEXT is never changed. Mutates `days` in place."""
    import random
    rng = random.Random(seed)
    all_quizzes = [quiz for _, subs in days for *_, quiz in subs]
    n = sum(len(quiz) for quiz in all_quizzes)
    targets = [i % 4 for i in range(n)]
    rng.shuffle(targets)
    idx = 0
    for quiz in all_quizzes:
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


if __name__ == '__main__':
    _rebalance_answer_positions(g11_31_40)
    append_to(11, g11_31_40)
