#!/usr/bin/env python3
"""Phase 3 extension: Grade 10, Days 61-70 (fourth Grade 10 batch). Topics
chosen to avoid any overlap with the existing Day 1-60 set (see
data/grade10.ts): the literary anti-hero, setting and atmosphere, active
and passive voice, editorial cartoons, active listening, historical
fiction, the process analysis essay, foreshadowing and suspense, and
theme across multiple texts in English; inverse functions, radical
functions, expected value and probability distributions, matrices,
absolute value functions, trigonometric identities, set theory and Venn
diagrams, linear programming, and congruence/similarity proofs in Math;
redox reactions, the endocrine system, electromagnetic induction, the
rock cycle, intermolecular forces, the immune system, fluid mechanics,
the water cycle, and taxonomy in Science; and the Great Depression and
Regina Riot, the Komagata Maru incident, Tommy Douglas and Medicare, the
Official Languages Act, the White Paper of 1969, Africville, the Air
India bombing, the Trans-Canada Highway, and the 1972 Summit Series in
History.

Subject keys for Grade 10 are "English", "Math", "Science", and
"History" (confirmed via data/grade10.ts), same as
gen_grade10_days51_60.py.

videoUrl is intentionally left unset for every subject -- fetch_video_ids.py
fills these in automatically on its next daily run. No embedded ASCII
double-quote characters are used anywhere in question/summary/option
text; apostrophes and quotation marks use the curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

E10 = 'https://tvolearn.com/pages/grade-10-english'
M10 = 'https://tvolearn.com/pages/grade-10-mathematics'
S10 = 'https://tvolearn.com/pages/grade-10-science'
H10 = 'https://tvolearn.com/pages/grade-10-history'
RE, RM, RS, RH = (
    'TVO Learn: Grade 10 English',
    'TVO Learn: Grade 10 Mathematics',
    'TVO Learn: Grade 10 Science',
    'TVO Learn: Grade 10 History',
)


def E(t, s, q):
    return sub('English', t, s, RE, E10, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M10, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S10, q)


def H(t, s, q):
    return sub('History', t, s, RH, H10, q)


g10_61_70 = [
day(61, [
E('Literature: The Anti-Hero in Modern Fiction',
  'Grade 10 English strand: an anti-hero is a central character who lacks conventional heroic qualities, such as moral clarity or courage, yet still drives the narrative and often earns the reader’s sympathy.',
  [('An anti-hero is best described as a central character who ___.', ['Lacks conventional heroic qualities but still drives the narrative', 'Always displays perfect moral clarity and courage', 'Never appears as the main character of a story', 'Is identical to a traditional villain in every way'], 0),
   ('Why might readers still sympathize with an anti-hero despite their flaws?', ['Their flaws and struggles can feel more relatable and human than a flawless traditional hero', 'Readers never sympathize with any flawed character', 'Sympathy has no connection to how a character is portrayed', 'Anti-heroes are always portrayed as entirely unlikeable'], 0),
   ('Which is a common trait of an anti-hero?', ['A morally ambiguous or ethically inconsistent set of choices', 'A consistently selfless and noble set of actions', 'A trait unrelated to characterization', 'A complete absence of any internal conflict'], 0),
   ('Why might an author choose to centre a story on an anti-hero rather than a traditional hero?', ['It can create more complex, realistic tension around questions of morality and choice', 'Anti-heroes never add complexity to a narrative', 'A reason unrelated to character development', 'Traditional heroes are always a more effective narrative choice'], 0),
   ('Why is the anti-hero considered a useful figure for exploring modern themes like moral ambiguity?', ['Their contradictions can mirror the complicated, imperfect choices people face in real life', 'The anti-hero has no connection to real-world moral questions', 'Modern literature never explores morally complex themes', 'This character type is only ever used in unrealistic fantasy stories'], 0)]),
M('Functions: Introduction to Inverse Functions',
  'Grade 10 Functions strand (extension): an inverse function reverses the effect of the original function, mapping each output value back to its corresponding input value.',
  [('An inverse function reverses the effect of the original function by ___.', ['Mapping each output value back to its corresponding input value', 'Mapping every input to the same output value', 'A process unrelated to functions', 'Doubling every output value of the original function'], 0),
   ('If f(3) = 7 for a function f, what must be true about its inverse function, f⁻¹?', ['f⁻¹(7) = 3', 'f⁻¹(3) = 7', 'A relationship unrelated to inverse functions', 'f⁻¹(7) = 0'], 0),
   ('The graph of a function and its inverse are reflections of each other across the line ___.', ['y = x', 'The x-axis only, with no connection to y = x', 'A line unrelated to inverse functions', 'The y-axis only, with no connection to y = x'], 0),
   ('Why must a function be one-to-one for its inverse to also be a function?', ['If two different inputs shared one output, the inverse would have to map that single output to two different values, which is not a function', 'One-to-one functions never have an inverse', 'This requirement has no connection to inverse functions', 'Every function automatically has a valid inverse regardless of this property'], 0),
   ('Why are inverse functions useful in real-world contexts, such as converting between units or currencies?', ['They allow a relationship to be reversed, letting a result be converted back to its original input value', 'Inverse functions have no real-world applications', 'Converting between units never requires reversing a relationship', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Chemistry: Redox Reactions and Oxidation Numbers',
   'Grade 10 Chemistry strand: a redox (reduction-oxidation) reaction involves the transfer of electrons between substances, with oxidation numbers used to track how each atom’s charge changes during the reaction.',
   [('A redox reaction involves the transfer of ___ between substances.', ['Electrons', 'Protons', 'A particle unrelated to chemical reactions', 'Entire atoms, with no connection to electrons'], 0),
    ('Oxidation refers to a process in which a substance ___.', ['Loses electrons', 'Gains electrons', 'A process unrelated to redox reactions', 'Loses protons'], 0),
    ('Reduction refers to a process in which a substance ___.', ['Gains electrons', 'Loses electrons', 'A process unrelated to redox reactions', 'Gains protons'], 0),
    ('Why are oxidation numbers a useful tool when analyzing a redox reaction?', ['They help track how the charge on each atom changes, revealing which substances are oxidized or reduced', 'Oxidation numbers provide no useful information about a reaction', 'A reason unrelated to redox chemistry', 'Oxidation numbers never change during a chemical reaction'], 0),
    ('Why are redox reactions important in everyday applications, such as batteries or metal corrosion?', ['They involve the electron transfer that generates electrical energy or gradually breaks down metals', 'Redox reactions have no connection to batteries or corrosion', 'Batteries and corrosion never involve any chemical reactions', 'This concept only applies to purely theoretical chemistry problems'], 0)]),
H('The Great Depression in Canada: Relief Camps and the Regina Riot',
  'Grade 10 History strand: during the 1930s Great Depression, widespread unemployment led the federal government to establish relief camps for single men, whose harsh conditions helped spark protests, including the 1935 Regina Riot.',
  [('The Great Depression in Canada took place primarily during which decade?', ['The 1930s', 'The 1910s', 'The 1950s', 'The 1970s'], 0),
   ('Relief camps were established by the federal government primarily for ___.', ['Unemployed single men', 'Retired government officials', 'A group entirely unrelated to unemployment', 'Only skilled tradespeople with steady work'], 0),
   ('The Regina Riot in 1935 arose out of protests connected to ___.', ['Harsh conditions in federal relief camps', 'A dispute unrelated to the Depression', 'A conflict with no connection to unemployment', 'A disagreement over provincial election results'], 0),
   ('Why is the Regina Riot considered historically significant?', ['It highlighted growing public frustration with government responses to unemployment and poverty during the Depression', 'This event had no connection to the Great Depression', 'The Regina Riot has no lasting significance in Canadian history', 'This topic has no relevance to understanding 1930s Canada'], 0),
   ('Why do historians study relief camps and events like the Regina Riot together?', ['They reveal how economic hardship and government policy shaped social unrest during the 1930s', 'Relief camps have no connection to broader Depression-era history', 'Government policy never influenced social unrest in this period', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(62, [
E('Reading: Analyzing Setting and Atmosphere',
  'Grade 10 English strand: setting establishes the time and place of a story, while atmosphere is the emotional mood created through descriptive details, both shaping how readers experience a narrative.',
  [('Setting establishes the ___ of a story.', ['Time and place', 'Central conflict only, with no connection to time or place', 'A concept unrelated to narrative structure', 'List of characters only'], 0),
   ('Atmosphere is best described as ___.', ['The emotional mood created through descriptive details', 'A synonym for a story’s plot events', 'A concept unrelated to setting', 'The physical location alone, with no emotional quality'], 0),
   ('Which technique might a writer use to build a tense atmosphere?', ['Describing dim lighting, silence, and a sense of unease', 'Describing only bright, cheerful colours with no tension at all', 'A technique unrelated to atmosphere', 'Avoiding any sensory description entirely'], 0),
   ('Why might a story’s setting change over the course of a narrative?', ['A shifting setting can reflect changes in a character’s circumstances or emotional state', 'Settings never change within a single narrative', 'A reason unrelated to setting and atmosphere', 'Changing a setting always weakens a story’s structure'], 0),
   ('Why is atmosphere considered an important element for readers to analyze?', ['It shapes how readers emotionally respond to and interpret the events of a story', 'Atmosphere has no effect on how a reader experiences a story', 'This concept has no connection to reading comprehension', 'Only plot events, not mood, ever influence a reader’s response'], 0)]),
M('Radical Functions and Equations',
  'Grade 10 Functions strand (extension): a radical function contains a variable inside a root, such as a square root, and solving a radical equation typically involves isolating the radical and raising both sides to a power.',
  [('A radical function contains a variable inside a ___.', ['Root, such as a square root', 'Denominator only, with no connection to roots', 'A concept unrelated to functions', 'Exponent only, with no connection to roots'], 0),
   ('Solving a radical equation typically involves isolating the radical and then ___.', ['Raising both sides of the equation to a power', 'Dividing both sides by zero', 'A step unrelated to solving radical equations', 'Ignoring the radical entirely'], 0),
   ('What is the domain restriction for the function f(x) = √x, assuming real-number outputs?', ['x must be greater than or equal to 0', 'x can be any real number, with no restriction', 'A restriction unrelated to this function', 'x must be less than 0'], 0),
   ('Why must solutions to a radical equation be checked in the original equation?', ['Raising both sides to a power can introduce extraneous solutions that do not actually satisfy the original equation', 'Radical equations never produce extraneous solutions', 'Checking a solution has no connection to solving radical equations', 'Every solution found is automatically guaranteed to be valid'], 0),
   ('Why are radical functions useful for modelling real-world situations, such as the relationship between a pendulum’s length and period?', ['Some real-world quantities relate to each other through a root relationship rather than a linear one', 'Radical functions have no real-world applications', 'Pendulum motion never involves any root-based relationship', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Biology: The Endocrine System and Hormonal Regulation',
   'Grade 10 Biology strand: the endocrine system uses glands to release hormones directly into the bloodstream, regulating body processes such as growth, metabolism, and the response to stress over a longer timescale than the nervous system.',
   [('The endocrine system regulates the body using ___.', ['Hormones released into the bloodstream', 'Electrical impulses sent through neurons', 'A process unrelated to body regulation', 'Only mechanical movement, with no chemical signalling'], 0),
    ('Hormones are released directly into the ___.', ['Bloodstream', 'Digestive tract only, with no connection to circulation', 'A structure unrelated to the endocrine system', 'Surrounding air, with no connection to the body'], 0),
    ('Compared to the nervous system, the endocrine system generally regulates the body over a ___ timescale.', ['Longer', 'Identical', 'A timescale unrelated to body regulation', 'Instantaneous, with no delay at all'], 0),
    ('Which of these is an example of a process regulated by the endocrine system?', ['Growth and metabolism', 'A process entirely unrelated to hormone regulation', 'Only voluntary muscle movement, with no connection to hormones', 'A process that never involves any body system'], 0),
    ('Why is understanding the endocrine system useful for studying certain medical conditions, such as diabetes?', ['Many conditions are linked to imbalances in how hormones are produced or regulated', 'The endocrine system has no connection to any medical conditions', 'Medical conditions are never related to hormone regulation', 'This field of study has no relevance to human health'], 0)]),
H('The Komagata Maru Incident and Immigration Restriction',
  'Grade 10 History strand: in 1914, the ship Komagata Maru carrying South Asian passengers was denied entry to Canada under discriminatory immigration laws, an incident that remains a significant example of exclusionary policy in Canadian history.',
  [('The Komagata Maru incident took place in which year?', ['1914', '1945', '1970', '1988'], 0),
   ('The Komagata Maru was a ship carrying passengers primarily from ___.', ['South Asia', 'Western Europe', 'A region entirely unrelated to the incident', 'East Asia, with no connection to South Asia'], 0),
   ('Passengers aboard the Komagata Maru were largely denied entry to Canada because of ___.', ['Discriminatory immigration laws', 'A lack of any interest in immigrating to Canada', 'A reason entirely unrelated to immigration policy', 'A decision made with no connection to government policy'], 0),
   ('Why is the Komagata Maru incident considered historically significant?', ['It stands as a stark example of exclusionary immigration policy in early twentieth-century Canada', 'This incident had no impact on Canadian immigration history', 'The Komagata Maru has no connection to Canadian immigration policy', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why might the Komagata Maru incident be studied alongside other examples of discriminatory policy, like the Chinese Head Tax?', ['Together they illustrate a broader pattern of racially restrictive immigration policy in early Canadian history', 'These events have no meaningful connection to one another', 'Discriminatory immigration policy was never a pattern in Canadian history', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(63, [
E('Grammar: Active and Passive Voice',
  'Grade 10 English strand: in the active voice the subject performs the action, while in the passive voice the subject receives the action, a distinction that affects clarity, emphasis, and tone in writing.',
  [('In the active voice, the subject of a sentence ___.', ['Performs the action', 'Receives the action', 'A concept unrelated to sentence structure', 'Is always omitted from the sentence'], 0),
   ('In the passive voice, the subject of a sentence ___.', ['Receives the action', 'Always performs the action', 'A concept unrelated to grammar', 'Is never mentioned in the sentence'], 0),
   ('Which sentence is written in the active voice?', ['The committee approved the proposal.', 'The proposal was approved by the committee.', 'A sentence unrelated to active or passive voice', 'The proposal had been being approved.'], 0),
   ('Why might a writer choose the passive voice when the person performing an action is unknown or unimportant?', ['It allows the focus to remain on the action or the result rather than on who performed it', 'The passive voice always makes a sentence clearer than the active voice', 'This choice has no effect on how a sentence is interpreted', 'The passive voice is never an appropriate stylistic choice'], 0),
   ('Why is the active voice generally preferred in most academic and persuasive writing?', ['It tends to be more direct, concise, and engaging for the reader', 'The active voice is always grammatically incorrect', 'Voice has no effect on the clarity or tone of writing', 'The passive voice is always the stronger stylistic choice'], 0)]),
M('Probability: Expected Value and Probability Distributions',
  'Grade 10 Data Management strand (extension): expected value is the long-run average outcome of a probability experiment, calculated by summing each outcome multiplied by its probability, and a probability distribution organizes all possible outcomes and their likelihoods.',
  [('Expected value represents the ___ of a probability experiment.', ['Long-run average outcome', 'Highest possible single outcome', 'A concept unrelated to probability', 'Lowest possible single outcome'], 0),
   ('Expected value is calculated by ___.', ['Summing each outcome multiplied by its probability', 'Adding together only the possible outcomes, ignoring probability', 'A method unrelated to expected value', 'Multiplying the total number of outcomes by zero'], 0),
   ('A probability distribution organizes ___.', ['All possible outcomes and their likelihoods', 'Only the most likely outcome, with no others considered', 'A concept unrelated to probability', 'A single outcome with no connection to likelihood'], 0),
   ('If a game pays $10 with probability 0.2 and $0 otherwise, what is its expected value?', ['$2', '$10', 'A value unrelated to this calculation', '$0'], 0),
   ('Why is expected value useful for making decisions involving risk, such as in insurance or gambling?', ['It provides a way to compare the long-run average outcome of different choices under uncertainty', 'Expected value has no real-world application to decision-making', 'Risk-based decisions never involve any mathematical calculation', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Physics: Electromagnetic Induction and Generators',
   'Grade 10 Physics strand: electromagnetic induction occurs when a changing magnetic field produces an electric current in a nearby conductor, a principle that underlies how electrical generators convert motion into electricity.',
   [('Electromagnetic induction occurs when a changing magnetic field produces ___.', ['An electric current in a nearby conductor', 'A change in the conductor’s mass', 'A phenomenon unrelated to magnetism', 'A permanent change in the conductor’s colour'], 0),
    ('An electrical generator primarily converts ___ into electrical energy.', ['Motion (mechanical energy)', 'Sound energy', 'A form of energy unrelated to generators', 'Chemical energy exclusively, with no connection to motion'], 0),
    ('Which of these actions could induce a current in a coil of wire?', ['Moving a magnet through the coil', 'Holding a magnet perfectly still near the coil', 'An action unrelated to electromagnetic induction', 'Removing all magnets from the vicinity of the coil'], 0),
    ('Why does moving a magnet more quickly through a coil typically increase the induced current?', ['A faster-changing magnetic field induces a greater electromotive force in the coil', 'The speed of the magnet’s motion has no effect on the induced current', 'A reason unrelated to electromagnetic induction', 'Induced current only depends on the size of the magnet, not its speed'], 0),
    ('Why is electromagnetic induction considered essential to modern electricity generation?', ['It provides the underlying principle that allows generators to convert mechanical motion into a usable electric current', 'Electromagnetic induction has no connection to how electricity is generated', 'Electricity generation never relies on magnetic fields', 'This concept only applies to purely theoretical physics problems'], 0)]),
H('Tommy Douglas and the Birth of Medicare',
  'Grade 10 History strand: as Premier of Saskatchewan, Tommy Douglas introduced North America’s first universal public health insurance program in 1962, laying the foundation for Canada’s national Medicare system.',
  [('Tommy Douglas served as Premier of which province?', ['Saskatchewan', 'Ontario', 'A province unrelated to the founding of Medicare', 'British Columbia'], 0),
   ('Saskatchewan introduced North America’s first universal public health insurance program in which year?', ['1962', '1919', '1945', '1988'], 0),
   ('Tommy Douglas’s health insurance program in Saskatchewan laid the foundation for ___.', ['Canada’s national Medicare system', 'A policy unrelated to health care', 'A program that had no lasting influence on Canada', 'A private, for-profit insurance model'], 0),
   ('Why is Tommy Douglas often cited as a significant figure in Canadian political history?', ['His leadership on public health insurance shaped a defining feature of the modern Canadian social safety net', 'Tommy Douglas had no lasting influence on Canadian policy', 'This figure has no connection to the development of Medicare', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians connect the introduction of Medicare in Saskatchewan to broader debates about the role of government?', ['It reflects ongoing questions about how far government should go in providing services like health care', 'Medicare has no connection to debates about government’s role', 'The size and role of government have never been debated in Canadian history', 'This topic has no relevance to Canadian political history'], 0)])]),

day(64, [
E('Media Literacy: Analyzing Editorial Cartoons',
  'Grade 10 English strand: editorial cartoons use visual symbolism, exaggeration, and caption text to comment on current events or political issues, condensing a persuasive argument into a single striking image.',
  [('Editorial cartoons use visual symbolism and exaggeration to ___.', ['Comment on current events or political issues', 'Present a purely neutral, opinion-free account of events', 'A concept unrelated to visual media', 'Provide a fully detailed, factual news report'], 0),
   ('Why might a cartoonist exaggerate a public figure’s features in an editorial cartoon?', ['Exaggeration can emphasize a particular trait or characteristic the cartoonist wants to critique', 'Exaggeration is never used in editorial cartoons', 'A reason unrelated to visual persuasion', 'Exaggerating a figure’s features always makes a cartoon less persuasive'], 0),
   ('Which is a common visual technique used in editorial cartoons?', ['Symbolic imagery, such as an animal representing a country or idea', 'Long paragraphs of unbiased, factual explanation with no imagery', 'A technique unrelated to editorial cartoons', 'Avoiding any exaggeration or symbolism entirely'], 0),
   ('Why is captioning often an important element to analyze in an editorial cartoon?', ['A caption can clarify or sharpen the cartoon’s intended argument or message', 'Captions never influence how a cartoon is interpreted', 'Editorial cartoons never include any caption text', 'This element has no connection to persuasive visual media'], 0),
   ('Why is it valuable to critically analyze editorial cartoons as part of media literacy?', ['It helps readers recognize how a single image can be used to persuade or shape opinion on an issue', 'Critical analysis of editorial cartoons has no value for media literacy', 'Editorial cartoons always present a completely neutral point of view', 'This skill has no connection to understanding media today'], 0)]),
M('Matrices: Introduction and Basic Operations',
  'Grade 10 Algebra strand (extension): a matrix is a rectangular array of numbers organized into rows and columns, and matrices can be added, subtracted, or multiplied following specific rules based on their dimensions.',
  [('A matrix is best described as a rectangular array of numbers organized into ___.', ['Rows and columns', 'A single row only, with no columns', 'A concept unrelated to organizing numbers', 'A single column only, with no rows'], 0),
   ('To add two matrices together, they must ___.', ['Have the same dimensions', 'Contain entirely different values', 'A requirement unrelated to matrix addition', 'Have a different number of rows and columns from each other'], 0),
   ('The dimensions of a matrix are typically described as ___.', ['Number of rows by number of columns', 'Only the total number of entries, with no distinction between rows and columns', 'A description unrelated to matrices', 'The sum of all entries in the matrix'], 0),
   ('Why must the number of columns in the first matrix match the number of rows in the second matrix when multiplying two matrices?', ['This condition is required by the way matrix multiplication combines rows and columns to produce each entry', 'Matrix dimensions never need to match for multiplication', 'This requirement has no connection to matrix multiplication', 'Any two matrices can always be multiplied regardless of their dimensions'], 0),
   ('Why are matrices useful for organizing and solving real-world problems, such as systems of equations or transforming graphics?', ['They provide an efficient, structured way to represent and manipulate large sets of related numbers', 'Matrices have no real-world modelling applications', 'Systems of equations and graphics transformations never involve organized numerical data', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Earth Science: The Rock Cycle and Mineral Formation',
   'Grade 10 Earth Science strand: the rock cycle describes the continuous transformation of rocks between igneous, sedimentary, and metamorphic forms through processes such as melting, cooling, compaction, and heat and pressure.',
   [('The rock cycle describes the continuous transformation of rocks between which three forms?', ['Igneous, sedimentary, and metamorphic', 'Solid, liquid, and gas', 'A set of forms unrelated to rock classification', 'Crystalline, organic, and synthetic'], 0),
    ('Igneous rock forms when ___.', ['Molten rock cools and solidifies', 'Sediment is compacted and cemented together', 'A process unrelated to rock formation', 'Existing rock is transformed by heat and pressure with no melting'], 0),
    ('Sedimentary rock typically forms through the process of ___.', ['Compaction and cementation of sediment layers', 'Molten rock cooling and solidifying', 'A process unrelated to sedimentary rock', 'Extreme heat and pressure transforming existing rock'], 0),
    ('Metamorphic rock forms when existing rock is transformed by ___.', ['Heat and pressure, without fully melting', 'Cooling and solidifying from a fully molten state', 'A process unrelated to metamorphic rock', 'Compaction of loose sediment alone'], 0),
    ('Why is the rock cycle considered a continuous, ongoing process rather than a one-time event?', ['Rocks can be transformed repeatedly between forms over long timescales as conditions like heat, pressure, and weathering change', 'The rock cycle only ever occurs once for any given rock', 'This process has no connection to changing environmental conditions', 'Rocks never change form once they are initially created'], 0)]),
H('The Official Languages Act and Canadian Bilingualism',
  'Grade 10 History strand: the 1969 Official Languages Act made English and French the official languages of the Canadian federal government, aiming to promote national unity and equal status for both linguistic communities.',
  [('The Official Languages Act was introduced in which year?', ['1969', '1919', '1945', '1988'], 0),
   ('The Official Languages Act declared English and French to be the official languages of ___.', ['The Canadian federal government', 'Only the province of Quebec', 'A level of government unrelated to language policy', 'Only the province of Ontario'], 0),
   ('One of the main aims of the Official Languages Act was to ___.', ['Promote national unity and equal status for English and French speakers', 'Eliminate the use of French in Canada entirely', 'A goal entirely unrelated to language policy', 'Restrict federal services to English speakers only'], 0),
   ('Why is the Official Languages Act often connected to broader efforts to address Quebec’s place within Confederation?', ['It responded to concerns about the status and representation of French-speaking Canadians within federal institutions', 'This legislation has no connection to Quebec’s relationship with the rest of Canada', 'Quebec’s place within Confederation was never a subject of federal policy', 'This topic has no relevance to Canadian history'], 0),
   ('Why do historians study the Official Languages Act alongside other efforts to define Canadian identity?', ['It illustrates how language policy became a key part of shaping a bilingual national identity', 'Language policy has no connection to Canadian identity', 'Canadian identity has never been shaped by federal legislation', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(65, [
E('Oral Communication: Active Listening and Note-Taking',
  'Grade 10 English strand: active listening involves fully concentrating on and engaging with a speaker, while effective note-taking uses strategies such as abbreviation and organization to capture key ideas efficiently.',
  [('Active listening involves ___.', ['Fully concentrating on and engaging with a speaker', 'Only hearing a speaker without any focused attention', 'A concept unrelated to oral communication', 'Preparing a response while ignoring the speaker entirely'], 0),
   ('Which is an example of a strategy used in effective note-taking?', ['Using abbreviations and symbols to capture ideas quickly', 'Writing down every single word a speaker says verbatim', 'A strategy unrelated to note-taking', 'Avoiding any organization or structure in one’s notes'], 0),
   ('Why might a listener ask a clarifying question during a discussion?', ['To confirm understanding of a speaker’s point before responding or moving on', 'Clarifying questions are never useful in a discussion', 'A reason unrelated to active listening', 'Asking questions always signals a lack of attention'], 0),
   ('Why is organizing notes under clear headings or categories a useful note-taking strategy?', ['It makes it easier to review and locate key information later', 'Organization has no effect on how useful notes are later', 'This strategy has no connection to effective note-taking', 'Notes are always equally useful regardless of how they are organized'], 0),
   ('Why is active listening considered an important skill beyond the classroom?', ['Many real-world situations, such as interviews or collaborative work, depend on genuinely understanding others', 'This skill has no application outside of a classroom setting', 'Active listening is never a realistic or useful skill', 'A reason unrelated to communication or collaboration'], 0)]),
M('Absolute Value Functions and Equations',
  'Grade 10 Functions strand (extension): an absolute value function measures the distance of a value from zero, producing a distinctive V-shaped graph, and solving an absolute value equation often requires considering two separate cases.',
  [('An absolute value function measures ___.', ['The distance of a value from zero', 'The exact sign of a value, with no connection to distance', 'A concept unrelated to functions', 'Only negative values, with no connection to positive ones'], 0),
   ('The graph of a basic absolute value function has a distinctive ___ shape.', ['V', 'S', 'A shape unrelated to absolute value functions', 'U'], 0),
   ('Solving an absolute value equation like |x| = 5 typically requires considering ___.', ['Two separate cases, x = 5 and x = -5', 'Only a single possible solution', 'A method unrelated to absolute value equations', 'Three separate cases with no clear pattern'], 0),
   ('Why does an absolute value equation often produce two possible solutions?', ['Both a positive and a negative value can have the same distance from zero', 'Absolute value equations never produce more than one solution', 'This outcome has no connection to how absolute value is defined', 'Only positive numbers can ever satisfy an absolute value equation'], 0),
   ('Why might absolute value functions be useful for modelling real-world situations, such as measuring error or tolerance?', ['They can represent a quantity’s distance from a target value, regardless of whether it is above or below that value', 'Absolute value functions have no real-world modelling applications', 'Measuring error or tolerance never involves considering distance from a target', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Chemistry: Intermolecular Forces and Physical Properties',
   'Grade 10 Chemistry strand: intermolecular forces are attractions between molecules that influence a substance’s physical properties, such as boiling point and solubility, and are generally weaker than the bonds within a molecule.',
   [('Intermolecular forces are best described as attractions ___.', ['Between molecules', 'Within a single atom only', 'A concept unrelated to molecular interactions', 'Between protons and neutrons in a nucleus'], 0),
    ('Compared to the covalent bonds within a molecule, intermolecular forces are generally ___.', ['Weaker', 'Stronger', 'A comparison unrelated to intermolecular forces', 'Identical in strength'], 0),
    ('Which physical property is directly influenced by the strength of a substance’s intermolecular forces?', ['Boiling point', 'Atomic number', 'A property unrelated to intermolecular forces', 'The number of protons in the nucleus'], 0),
    ('Why do substances with stronger intermolecular forces generally have higher boiling points?', ['More energy is required to overcome the stronger attractions between molecules during a phase change', 'Stronger intermolecular forces always lower a substance’s boiling point', 'Boiling point has no connection to intermolecular forces', 'Intermolecular forces never affect how much energy a phase change requires'], 0),
    ('Why is understanding intermolecular forces useful for predicting whether two substances will dissolve in one another?', ['Similar types of intermolecular forces between substances tend to make them more soluble in each other', 'Intermolecular forces have no connection to solubility', 'Solubility is never influenced by the forces between molecules', 'This concept only applies to purely theoretical chemistry problems'], 0)]),
H('The White Paper of 1969 and Indigenous Policy',
  'Grade 10 History strand: the 1969 federal White Paper proposed abolishing the Indian Act and existing legal status for Indigenous peoples, a policy widely rejected by Indigenous communities and withdrawn after significant opposition.',
  [('The White Paper on Indigenous policy was introduced in which year?', ['1969', '1919', '1945', '1990'], 0),
   ('The 1969 White Paper proposed abolishing ___.', ['The Indian Act and existing legal status for Indigenous peoples', 'A policy entirely unrelated to Indigenous peoples', 'Provincial governments across Canada', 'The federal government’s power to make any policy at all'], 0),
   ('The 1969 White Paper was ultimately ___.', ['Widely rejected by Indigenous communities and withdrawn', 'Immediately and enthusiastically implemented with no opposition', 'A policy with no connection to Indigenous rights', 'Approved by all Indigenous communities without any debate'], 0),
   ('Why is the White Paper of 1969 considered a significant moment in the history of Indigenous political organizing?', ['Opposition to the policy helped unite and mobilize Indigenous leaders and communities across Canada', 'This policy had no effect on Indigenous political organizing', 'The White Paper has no connection to Indigenous rights history', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians study the White Paper alongside other Indigenous rights and land claims issues in Canada?', ['It illustrates a key turning point in the ongoing relationship between the federal government and Indigenous peoples', 'The White Paper has no connection to other Indigenous rights issues', 'The federal government’s relationship with Indigenous peoples has never changed over time', 'This topic has no relevance to Canadian history'], 0)])]),

day(66, [
E('Literature: Historical Fiction and Its Purpose',
  'Grade 10 English strand: historical fiction blends invented characters and plot with real historical settings and events, allowing writers to explore the past while illuminating universal human experiences.',
  [('Historical fiction blends invented characters and plot with ___.', ['Real historical settings and events', 'Only entirely fictional settings, with no real-world basis', 'A concept unrelated to storytelling', 'A setting with no connection to any particular time period'], 0),
   ('Why might an author use historical fiction to explore a real historical event?', ['It can make the past feel immediate and emotionally resonant through a personal, human perspective', 'Historical fiction never engages with real historical events', 'A reason unrelated to this genre', 'Fiction can never help readers understand real history'], 0),
   ('Which is a challenge an author might face when writing historical fiction?', ['Balancing historical accuracy with the demands of an engaging invented plot', 'Historical fiction requires no research or accuracy at all', 'A challenge unrelated to this genre', 'Avoiding any connection to a real time period entirely'], 0),
   ('Why might historical fiction be considered a valuable complement to studying history through non-fiction texts?', ['It can offer emotional and personal insight into how historical events may have been experienced by individuals', 'Historical fiction has no connection to understanding history', 'Non-fiction and fiction can never be studied together', 'This genre never adds any insight beyond a textbook account'], 0),
   ('Why must readers be cautious about treating historical fiction as a fully accurate historical record?', ['Authors often take creative liberties with characters, dialogue, or events to serve the story', 'Historical fiction is always completely factually accurate', 'This caution has no connection to reading historical fiction critically', 'Fiction and fact are always identical in this genre'], 0)]),
M('Trigonometry: Basic Trigonometric Identities',
  'Grade 10 Trigonometry strand (extension): a trigonometric identity is an equation involving trigonometric ratios that holds true for all valid angle values, such as the Pythagorean identity relating sine and cosine.',
  [('A trigonometric identity is an equation that holds true for ___.', ['All valid angle values', 'Only a single specific angle', 'A concept unrelated to trigonometry', 'No angle values at all'], 0),
   ('The Pythagorean identity relates which two trigonometric ratios?', ['Sine and cosine', 'Only tangent, with no other ratio involved', 'A relationship unrelated to trigonometric identities', 'Secant and cosecant exclusively'], 0),
   ('The Pythagorean identity states that sin²(θ) + cos²(θ) equals ___.', ['1', '0', 'A value unrelated to this identity', 'θ'], 0),
   ('Why might trigonometric identities be used to simplify a complex trigonometric expression?', ['They allow an expression to be rewritten in an equivalent, often simpler, form', 'Trigonometric identities always make an expression more complicated', 'This use has no connection to trigonometric identities', 'Identities can never be used to rewrite an expression'], 0),
   ('Why is the Pythagorean identity considered a foundational relationship in trigonometry?', ['It connects sine and cosine directly to the Pythagorean theorem applied to a right triangle in the unit circle', 'This identity has no connection to the Pythagorean theorem', 'Sine and cosine have no relationship to one another', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Biology: The Immune System and Disease Defense',
   'Grade 10 Biology strand: the immune system defends the body against pathogens using barriers, white blood cells, and antibodies, with the immune response becoming faster and more effective after repeated exposure to a specific pathogen.',
   [('The immune system primarily defends the body against ___.', ['Pathogens', 'A process unrelated to disease', 'Only physical injuries, with no connection to disease', 'Changes in body temperature alone'], 0),
    ('White blood cells play a key role in the immune system by ___.', ['Identifying and destroying pathogens', 'Transporting oxygen throughout the body', 'A role unrelated to immune defense', 'Producing hormones that regulate metabolism'], 0),
    ('Antibodies are proteins that ___.', ['Help identify and neutralize specific pathogens', 'Have no role in the body’s immune response', 'A concept unrelated to immune defense', 'Only function outside of the human body'], 0),
    ('Why does the immune system typically respond more quickly to a pathogen after a repeated exposure?', ['The immune system can retain a memory of previous pathogens, allowing for a faster, more targeted response', 'Repeated exposure to a pathogen never affects the speed of the immune response', 'A reason unrelated to immune function', 'The immune system loses its ability to respond after the first exposure to any pathogen'], 0),
    ('Why is understanding the immune system important for developing vaccines?', ['Vaccines work by safely exposing the immune system to a pathogen so it can build a protective memory response', 'The immune system has no connection to how vaccines function', 'Vaccines never involve any interaction with the immune system', 'This concept only applies to purely theoretical biology with no real-world use'], 0)]),
H('Africville and the Destruction of a Black Canadian Community',
  'Grade 10 History strand: Africville was a historic Black community in Halifax, Nova Scotia, that was demolished by the city in the 1960s despite residents’ objections, an event now widely recognized as an example of systemic racial injustice.',
  [('Africville was a historic Black community located in which city?', ['Halifax, Nova Scotia', 'Toronto, Ontario', 'A city entirely unrelated to this community', 'Vancouver, British Columbia'], 0),
   ('Africville was demolished by the city primarily during which decade?', ['The 1960s', 'The 1910s', 'The 1930s', 'The 1990s'], 0),
   ('The destruction of Africville occurred despite ___.', ['Objections from many of its residents', 'The unanimous support of every resident', 'A situation entirely unrelated to community objections', 'A formal vote in which residents chose demolition'], 0),
   ('Why is the destruction of Africville widely recognized today as an example of systemic racial injustice?', ['A historic Black community was displaced with inadequate consultation or compensation, reflecting broader patterns of racial inequity', 'This event had no connection to issues of race or injustice', 'Africville’s demolition has been entirely forgotten with no historical record', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians and community advocates continue to study Africville’s history today?', ['It offers important lessons about the treatment of Black Canadian communities and the need for historical accountability', 'This community has no lasting relevance to Canadian history', 'Africville’s history has no connection to broader civil rights issues in Canada', 'This topic has no relevance to understanding Canadian history'], 0)])]),

day(67, [
E('Writing: The Process Analysis Essay',
  'Grade 10 English strand: a process analysis essay explains how to complete a task or how something works by breaking it down into a clear, logically ordered sequence of steps.',
  [('A process analysis essay explains how to complete a task by breaking it down into ___.', ['A clear, logically ordered sequence of steps', 'A single unordered list with no logical sequence', 'A concept unrelated to explanatory writing', 'A random collection of unrelated details'], 0),
   ('Why is it important for the steps in a process analysis essay to be presented in a logical order?', ['Readers need to follow the sequence accurately to understand or complete the process themselves', 'Order never matters when explaining a process to a reader', 'A reason unrelated to process analysis writing', 'This type of essay works equally well with steps in any order'], 0),
   ('Which is an example of a transition word commonly used in a process analysis essay?', ['Next', 'A word unrelated to sequencing steps', 'Although', 'However'], 0),
   ('Why might a writer include a brief explanation of why a particular step matters in a process analysis essay?', ['It can help readers understand the purpose behind each step, not just the action itself', 'Explaining the reason behind a step never helps a reader', 'A reason unrelated to process analysis writing', 'This type of essay should never explain the purpose of any step'], 0),
   ('Why is precise, specific language especially important in a process analysis essay?', ['Vague instructions can cause a reader to misunderstand or incorrectly complete a step', 'Precision has no effect on how well a process is explained', 'This type of essay works equally well with vague or general language', 'A reason unrelated to explanatory writing'], 0)]),
M('Data Management: Set Theory and Venn Diagrams in Probability',
  'Grade 10 Data Management strand (extension): set theory describes relationships between groups of items, and a Venn diagram visually represents these relationships, helping calculate probabilities involving overlapping events.',
  [('A Venn diagram is used to visually represent ___.', ['Relationships between sets, including overlapping groups', 'A single number with no connection to grouping', 'A concept unrelated to set theory', 'Only sets that share no elements in common'], 0),
   ('The overlapping region of two circles in a Venn diagram represents ___.', ['Elements common to both sets', 'Elements found in neither set', 'A region unrelated to set theory', 'Elements found only in the first set'], 0),
   ('In set notation, the symbol ∪ generally represents the ___ of two sets.', ['Union', 'Intersection', 'A concept unrelated to set operations', 'Difference'], 0),
   ('Why is a Venn diagram a useful tool for calculating the probability of two overlapping events?', ['It visually clarifies which outcomes belong to each event and which are shared, helping avoid double-counting', 'Venn diagrams have no connection to calculating probability', 'Overlapping events can never be represented visually', 'This tool only applies to sets with no shared elements'], 0),
   ('Why is set theory useful for organizing real-world data, such as survey results about overlapping preferences?', ['It provides a clear framework for identifying shared and distinct groups within a larger data set', 'Set theory has no real-world data organization applications', 'Survey results can never involve any overlapping categories', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Physics: Fluid Mechanics — Pressure and Buoyancy',
   'Grade 10 Physics strand: fluid mechanics examines how liquids and gases behave under pressure, including the concept of buoyancy, the upward force a fluid exerts on an object that allows some objects to float.',
   [('Fluid mechanics examines how liquids and gases behave under ___.', ['Pressure', 'A concept unrelated to fluids', 'Only extremely low temperatures', 'A factor unrelated to physical forces'], 0),
    ('Buoyancy is best described as ___.', ['The upward force a fluid exerts on an object', 'A downward force that always sinks an object', 'A concept unrelated to fluid mechanics', 'A force that only acts on solids, with no connection to fluids'], 0),
    ('An object will float in a fluid if the buoyant force acting on it is ___ the object’s weight.', ['Greater than or equal to', 'Always less than', 'A comparison unrelated to floating', 'Exactly zero'], 0),
    ('Why does pressure in a fluid increase with depth?', ['The weight of the fluid above a given point increases as depth increases', 'Pressure in a fluid never changes with depth', 'A reason unrelated to fluid mechanics', 'Depth has no connection to the weight of the fluid above a point'], 0),
    ('Why is understanding buoyancy useful for designing objects like ships or submarines?', ['It helps engineers ensure a vessel displaces enough fluid to generate sufficient upward force to float or control its depth', 'Buoyancy has no connection to how ships or submarines are designed', 'These vessels never need to account for any fluid forces', 'This concept only applies to purely theoretical physics problems'], 0)]),
H('The Air India Bombing and Its Legacy',
  'Grade 10 History strand: the 1985 bombing of Air India Flight 182, planned in Canada, killed all 329 people aboard and remains the deadliest terrorist attack in Canadian history, prompting lasting debate over airport security and the treatment of victims’ families.',
  [('The Air India bombing took place in which year?', ['1985', '1945', '1970', '1919'], 0),
   ('The bombing of Air India Flight 182 was planned primarily in ___.', ['Canada', 'A country entirely unrelated to the attack', 'A location with no connection to Canadian history', 'A country outside of North America with no Canadian involvement'], 0),
   ('The Air India bombing remains widely described as ___.', ['The deadliest terrorist attack in Canadian history', 'An event with no lasting historical significance', 'A minor incident with no connection to Canadian history', 'An attack with no connection to any victims'], 0),
   ('Why is the Air India bombing often discussed in relation to airport and aviation security?', ['The attack raised significant questions about gaps in security procedures that allowed the bombing to occur', 'This event had no connection to airport or aviation security', 'Airport security has never been a topic of public debate in Canada', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians and policymakers continue to study the Air India bombing and its aftermath?', ['It raises lasting questions about intelligence failures, victim support, and how Canada responds to acts of terrorism', 'This event has no lasting relevance to Canadian history', 'The Air India bombing has been entirely forgotten with no historical record', 'This topic has no relevance to Canadian public policy'], 0)])]),

day(68, [
E('Reading: Foreshadowing and Suspense in Fiction',
  'Grade 10 English strand: foreshadowing is a technique in which an author hints at future events, building suspense and encouraging readers to anticipate what will happen next in a narrative.',
  [('Foreshadowing is a technique in which an author ___.', ['Hints at future events in a narrative', 'Reveals the entire ending at the very beginning of a story', 'A concept unrelated to narrative technique', 'Avoids giving readers any hints about future events'], 0),
   ('Why might an author use foreshadowing rather than directly stating what will happen?', ['It builds suspense and encourages readers to actively anticipate and interpret upcoming events', 'Foreshadowing never affects how a reader experiences suspense', 'A reason unrelated to narrative technique', 'Directly stating future events always creates more suspense than foreshadowing'], 0),
   ('Which is an example of a technique an author might use to foreshadow a dramatic event?', ['A brief, ominous comment made by a character earlier in the story', 'A random detail with absolutely no connection to later plot events', 'A technique unrelated to foreshadowing', 'Removing all tension from a scene entirely'], 0),
   ('Why might rereading a story reveal foreshadowing that was not obvious on a first reading?', ['Knowing how the story ends allows a reader to notice subtle earlier hints they may have missed', 'Foreshadowing is always equally obvious on every reading of a story', 'A reason unrelated to reading comprehension', 'Rereading a story never changes how a reader interprets earlier details'], 0),
   ('Why is suspense considered an important tool for keeping readers engaged with a narrative?', ['It creates anticipation and uncertainty that motivates readers to continue reading to find out what happens', 'Suspense has no effect on how engaged a reader feels with a story', 'This concept has no connection to reading motivation', 'Readers are never motivated by uncertainty about future plot events'], 0)]),
M('Linear Programming: Optimization with Constraints',
  'Grade 10 Algebra strand (extension): linear programming finds the maximum or minimum value of a linear expression subject to a system of linear constraints, often solved by evaluating a feasible region’s corner points.',
  [('Linear programming finds the maximum or minimum value of a linear expression subject to ___.', ['A system of linear constraints', 'No constraints of any kind', 'A concept unrelated to optimization', 'A single, unrelated equation with no connection to the expression'], 0),
   ('The region that satisfies all constraints in a linear programming problem is called the ___.', ['Feasible region', 'Impossible region', 'A concept unrelated to linear programming', 'Undefined region'], 0),
   ('In a linear programming problem, the maximum or minimum value typically occurs at a ___ of the feasible region.', ['Corner point', 'Location outside the feasible region entirely', 'A point unrelated to linear programming', 'Random interior point chosen without any calculation'], 0),
   ('Why is evaluating the corner points of the feasible region an effective strategy for solving a linear programming problem?', ['The optimal value of a linear expression over a feasible region always occurs at one of its corner points', 'Corner points never provide any useful information for this type of problem', 'This strategy has no connection to solving linear programming problems', 'The optimal value can only occur at a point outside the feasible region'], 0),
   ('Why is linear programming useful for real-world decision-making, such as maximizing profit or minimizing cost under limited resources?', ['It provides a systematic way to find the best possible outcome while respecting practical limitations', 'Linear programming has no real-world decision-making applications', 'Maximizing profit or minimizing cost never involves any limited resources', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Earth Science: The Water Cycle and Watershed Management',
   'Grade 10 Earth Science strand: the water cycle describes the continuous movement of water through evaporation, condensation, and precipitation, and a watershed is the land area that drains water into a common outlet like a lake or river.',
   [('The water cycle describes the continuous movement of water through processes including ___.', ['Evaporation, condensation, and precipitation', 'A process unrelated to water movement', 'Only freezing, with no other processes involved', 'Combustion and oxidation'], 0),
    ('A watershed is best described as ___.', ['The land area that drains water into a common outlet, like a lake or river', 'A structure built to store drinking water', 'A concept unrelated to the water cycle', 'A single, isolated body of water with no surrounding land'], 0),
    ('Condensation in the water cycle refers to the process of water vapour ___.', ['Turning into liquid water droplets', 'Turning directly into a solid', 'A process unrelated to the water cycle', 'Evaporating into the atmosphere'], 0),
    ('Why is understanding watershed boundaries important for managing water resources?', ['Human activities anywhere within a watershed can affect the water quality and supply of the entire drainage area', 'Watershed boundaries have no connection to water quality or supply', 'Human activity never affects water resources within a watershed', 'This concept has no relevance to managing natural resources'], 0),
    ('Why is the water cycle considered essential to sustaining ecosystems and human communities?', ['It continuously redistributes fresh water, supporting living things and replenishing water supplies', 'The water cycle has no connection to supporting ecosystems or communities', 'Ecosystems and communities never depend on any water supply', 'This concept only applies to purely theoretical Earth science with no real-world use'], 0)]),
H('The Trans-Canada Highway and Postwar National Infrastructure',
  'Grade 10 History strand: completed in stages through the 1950s and 1960s, the Trans-Canada Highway was a major federal infrastructure project intended to physically connect the country and support postwar economic growth.',
  [('The Trans-Canada Highway was primarily built during which decades?', ['The 1950s and 1960s', 'The 1910s and 1920s', 'The 1980s and 1990s', 'The 1930s and 1940s'], 0),
   ('The Trans-Canada Highway was intended to physically connect ___.', ['The country from coast to coast', 'Only a single province, with no national connection', 'A network unrelated to national infrastructure', 'Canada to the United States exclusively, with no domestic connection'], 0),
   ('The construction of the Trans-Canada Highway is closely associated with supporting ___.', ['Postwar economic growth', 'A decline in national economic activity', 'A goal entirely unrelated to Canada’s economy', 'Only military transportation, with no connection to the economy'], 0),
   ('Why is the Trans-Canada Highway often cited as a significant example of postwar Canadian nation-building?', ['It reflected a federal effort to physically and economically unite a vast and geographically diverse country', 'This project had no connection to Canadian nation-building', 'The Trans-Canada Highway has no lasting significance in Canadian history', 'This topic has no relevance to understanding postwar Canada'], 0),
   ('Why might historians compare the Trans-Canada Highway to other major infrastructure projects, like the transcontinental railway?', ['Both projects illustrate how large-scale infrastructure has been used to connect and unify Canada across its history', 'Infrastructure projects have no connection to Canadian unity', 'The transcontinental railway has no connection to Canadian history', 'This topic has no relevance to understanding Canadian economic development'], 0)])]),

day(69, [
E('Reading: Analyzing Theme Across Multiple Texts',
  'Grade 10 English strand: analyzing theme across multiple texts involves identifying a shared central idea or message and comparing how different authors develop that idea through their own distinct characters, settings, and structures.',
  [('Analyzing theme across multiple texts involves identifying a shared ___.', ['Central idea or message', 'Setting, with no connection to meaning or message', 'A concept unrelated to literary analysis', 'List of characters with no connection to meaning'], 0),
   ('Why might two different authors develop a similar theme in very different ways?', ['Each author brings their own perspective, characters, and structure to how they explore an idea', 'Different authors always develop themes in an identical way', 'A reason unrelated to comparative literary analysis', 'Themes can only ever be explored in one single way'], 0),
   ('Which is a useful strategy for comparing how theme is developed across two texts?', ['Identifying specific passages in each text that relate to the shared theme', 'Ignoring the text entirely and relying only on personal opinion', 'A strategy unrelated to thematic analysis', 'Comparing only the covers or titles of each text'], 0),
   ('Why might comparing theme across texts from different time periods or cultures be valuable?', ['It can reveal both universal human concerns and ideas shaped by a specific context', 'Comparing texts from different periods or cultures never reveals anything meaningful', 'A reason unrelated to literary analysis', 'Themes never differ based on time period or culture'], 0),
   ('Why is analyzing theme across multiple texts considered a valuable culminating literary skill?', ['It builds on close reading, comparison, and synthesis skills developed throughout the course', 'This skill has no connection to earlier reading and writing skills', 'Analyzing multiple texts together provides no additional insight', 'A reason unrelated to English studies'], 0)]),
M('Geometry: Congruence and Similarity Proofs',
  'Grade 10 Geometry strand (extension): congruent figures are identical in shape and size, while similar figures share the same shape but may differ in size, and formal proofs use established criteria to justify these relationships.',
  [('Congruent figures are identical in ___.', ['Shape and size', 'Shape only, with no connection to size', 'A concept unrelated to geometry', 'Colour, with no connection to shape or size'], 0),
   ('Similar figures share the same ___ but may differ in size.', ['Shape', 'Colour, with no connection to shape', 'A concept unrelated to similarity', 'Exact location on a coordinate plane'], 0),
   ('Which of these is a common criterion used to prove that two triangles are congruent?', ['Side-Angle-Side (SAS)', 'A criterion unrelated to triangle congruence', 'Colour-Colour-Colour (CCC)', 'Size-Size-Size, with no reference to angles'], 0),
   ('Why must corresponding angles be equal for two figures to be considered similar?', ['Equal corresponding angles ensure the figures have the exact same overall shape', 'Corresponding angles never need to be equal for figures to be similar', 'A reason unrelated to similarity', 'Similarity depends only on colour, not on any angle measurements'], 0),
   ('Why are formal congruence and similarity proofs useful in fields like architecture or engineering?', ['They provide a rigorous way to confirm that scaled models or repeated structural elements maintain the intended shape and proportions', 'Congruence and similarity proofs have no real-world applications', 'Architecture and engineering never involve maintaining consistent shapes or proportions', 'This concept only applies to purely abstract mathematics with no real-world use'], 0)]),
Sc('Biology: Taxonomy and Classification of Living Things',
   'Grade 10 Biology strand: taxonomy is the scientific system for classifying living things into a hierarchy of groups, from broad categories like kingdom down to specific species, based on shared characteristics and evolutionary relationships.',
   [('Taxonomy is best described as the scientific system for ___.', ['Classifying living things into a hierarchy of groups', 'Measuring the size of an organism', 'A concept unrelated to biology', 'Naming individual organisms with no connection to grouping'], 0),
    ('In the taxonomic hierarchy, which of these is the broadest category?', ['Kingdom', 'Species', 'A category unrelated to taxonomy', 'Genus'], 0),
    ('Species is generally considered the ___ category in the taxonomic hierarchy.', ['Most specific', 'Broadest', 'A category unrelated to taxonomy', 'Second broadest, after kingdom'], 0),
    ('Why are living things classified based on shared characteristics and evolutionary relationships?', ['This approach reflects how closely related organisms actually are, based on common ancestry', 'Classification has no connection to evolutionary relationships', 'Shared characteristics never provide any useful information about relatedness', 'A reason unrelated to taxonomy'], 0),
    ('Why is a standardized taxonomic system valuable for scientists around the world?', ['It provides a consistent, universally understood way to identify and communicate about organisms across different languages and regions', 'A standardized system has no benefit for global scientific communication', 'Taxonomy has no practical use for scientists studying living things', 'This concept only applies to purely theoretical biology with no real-world use'], 0)]),
H('The 1972 Summit Series: Hockey, Identity, and the Cold War',
  'Grade 10 History strand: the 1972 Summit Series, a hockey competition between Canada and the Soviet Union, became a symbol of Cold War rivalry and national pride, with Canada’s dramatic final victory remembered as a defining moment in Canadian identity.',
  [('The 1972 Summit Series was a hockey competition between Canada and ___.', ['The Soviet Union', 'The United States', 'A country entirely unrelated to the series', 'A team from within Canada only, with no international opponent'], 0),
   ('The Summit Series is often described as a symbol of ___.', ['Cold War rivalry and national pride', 'A conflict entirely unrelated to international relations', 'A purely local, community-level sporting event', 'A dispute with no connection to national identity'], 0),
   ('Canada’s performance in the 1972 Summit Series is remembered largely for ___.', ['A dramatic final victory', 'A decisive, one-sided loss', 'An event with no lasting cultural significance', 'A series that was cancelled before completion'], 0),
   ('Why is the 1972 Summit Series often studied as more than just a sporting event?', ['It reflected broader Cold War tensions and became closely tied to a sense of Canadian identity and pride', 'This event had no connection to Cold War politics or Canadian identity', 'The Summit Series has no lasting cultural significance in Canada', 'This topic has no relevance to understanding Canadian history'], 0),
   ('Why do historians connect the Summit Series to broader Cold War-era cultural competition between nations?', ['Sporting events like this one were often viewed as a symbolic contest between differing political and social systems', 'Sporting events were never connected to Cold War politics', 'Cultural competition between nations never occurred during the Cold War', 'This topic has no relevance to understanding twentieth-century history'], 0)])]),

day(70, [
E('Review: Character, Craft, and Rhetorical Analysis',
  'Grade 10 English strand: this review lesson revisits the anti-hero, setting and atmosphere, active and passive voice, editorial cartoons, active listening, historical fiction, the process analysis essay, foreshadowing and suspense, and theme across texts covered across Days 61-69.',
  [('An anti-hero is best described as a central character who ___.', ['Lacks conventional heroic qualities but still drives the narrative', 'Always displays perfect moral clarity and courage', 'Never appears as the main character of a story', 'Is identical to a traditional villain in every way'], 0),
   ('Atmosphere is best described as ___.', ['The emotional mood created through descriptive details', 'A synonym for a story’s plot events', 'A concept unrelated to setting', 'The physical location alone, with no emotional quality'], 0),
   ('In the active voice, the subject of a sentence ___.', ['Performs the action', 'Receives the action', 'A concept unrelated to sentence structure', 'Is always omitted from the sentence'], 0),
   ('Foreshadowing is a technique in which an author ___.', ['Hints at future events in a narrative', 'Reveals the entire ending at the very beginning of a story', 'A concept unrelated to narrative technique', 'Avoids giving readers any hints about future events'], 0),
   ('Why is it useful to review these varied literary and communication skills together?', ['It reinforces how different narrative techniques and communication strategies shape meaning and understanding', 'These topics have no connection to each other', 'Review is never useful in English studies', 'Each topic must be studied with no connection to the others'], 0)]),
M('Review: Functions, Matrices, Probability, and Geometry',
  'Grade 10 Math strand review: this lesson revisits inverse functions, radical functions, expected value, matrices, absolute value functions, trigonometric identities, set theory, linear programming, and congruence/similarity proofs covered across Days 61-69.',
  [('An inverse function reverses the effect of the original function by ___.', ['Mapping each output value back to its corresponding input value', 'Mapping every input to the same output value', 'A process unrelated to functions', 'Doubling every output value of the original function'], 0),
   ('Expected value is calculated by ___.', ['Summing each outcome multiplied by its probability', 'Adding together only the possible outcomes, ignoring probability', 'A method unrelated to expected value', 'Multiplying the total number of outcomes by zero'], 0),
   ('The graph of a basic absolute value function has a distinctive ___ shape.', ['V', 'S', 'A shape unrelated to absolute value functions', 'U'], 0),
   ('In a linear programming problem, the maximum or minimum value typically occurs at a ___ of the feasible region.', ['Corner point', 'Location outside the feasible region entirely', 'A point unrelated to linear programming', 'Random interior point chosen without any calculation'], 0),
   ('Why is it valuable to review these connected mathematical concepts together?', ['It reinforces how these skills build on and relate to one another', 'These concepts have no connection to each other', 'Review is never useful in math', 'Each concept must be understood with no connection to the others'], 0)]),
Sc('Review: Chemistry, Biology, Physics, and Earth Science Applications',
   'Grade 10 Science strand review: this lesson revisits redox reactions, the endocrine system, electromagnetic induction, the rock cycle, intermolecular forces, the immune system, fluid mechanics, the water cycle, and taxonomy covered across Days 61-69.',
   [('A redox reaction involves the transfer of ___ between substances.', ['Electrons', 'Protons', 'A particle unrelated to chemical reactions', 'Entire atoms, with no connection to electrons'], 0),
    ('Electromagnetic induction occurs when a changing magnetic field produces ___.', ['An electric current in a nearby conductor', 'A change in the conductor’s mass', 'A phenomenon unrelated to magnetism', 'A permanent change in the conductor’s colour'], 0),
    ('Antibodies are proteins that ___.', ['Help identify and neutralize specific pathogens', 'Have no role in the body’s immune response', 'A concept unrelated to immune defense', 'Only function outside of the human body'], 0),
    ('A watershed is best described as ___.', ['The land area that drains water into a common outlet, like a lake or river', 'A structure built to store drinking water', 'A concept unrelated to the water cycle', 'A single, isolated body of water with no surrounding land'], 0),
    ('Why is it valuable to review these connected science concepts together?', ['It reinforces how these scientific ideas relate to and build on one another', 'These concepts have no connection to each other', 'Review is never useful at the end of a unit', 'Each concept must be understood with no connection to the others'], 0)]),
H('Review: Mid-Century Canadian Society, Policy, and Identity',
  'Grade 10 History strand review: this lesson revisits the Great Depression and Regina Riot, the Komagata Maru incident, Tommy Douglas and Medicare, the Official Languages Act, the White Paper of 1969, Africville, the Air India bombing, the Trans-Canada Highway, and the 1972 Summit Series covered across Days 61-69.',
  [('The Regina Riot in 1935 arose out of protests connected to ___.', ['Harsh conditions in federal relief camps', 'A dispute unrelated to the Depression', 'A conflict with no connection to unemployment', 'A disagreement over provincial election results'], 0),
   ('Saskatchewan introduced North America’s first universal public health insurance program in which year?', ['1962', '1919', '1945', '1988'], 0),
   ('The 1969 White Paper proposed abolishing ___.', ['The Indian Act and existing legal status for Indigenous peoples', 'A policy entirely unrelated to Indigenous peoples', 'Provincial governments across Canada', 'The federal government’s power to make any policy at all'], 0),
   ('The Air India bombing remains widely described as ___.', ['The deadliest terrorist attack in Canadian history', 'An event with no lasting historical significance', 'A minor incident with no connection to Canadian history', 'An attack with no connection to any victims'], 0),
   ('Why is it valuable to review these mid-to-late twentieth-century developments in Canadian society together?', ['It reinforces how policy, social change, and national identity have interacted throughout Canadian history', 'These events have no meaningful connections to each other', 'Review is never useful in history', 'Each event must be studied with no connection to the others'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260817):
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
    _rebalance_answer_positions(g10_61_70)
    append_to(10, g10_61_70)
