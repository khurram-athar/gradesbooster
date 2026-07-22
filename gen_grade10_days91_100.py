#!/usr/bin/env python3
"""Grade 10, Days 91-100 -- extends Grade 10 from 90 to 100 days (the
first batch of the full-year expansion beyond the original 90-day
program). Topics chosen to avoid any overlap with the existing Day 1-90
set (see data/grade10.json): satire and parody, the elegy, conditional
sentences, the road novel, ceremonial speeches, multiple narrators,
historical fiction short stories, the subjunctive mood, eco-fiction;
determinants and inverses of 2x2 matrices, double-angle trig identities,
geometric series, correlation vs causation, probability tree diagrams,
composition of functions, similar triangles and indirect measurement,
exponential/logarithmic equations, mortgages and amortization; types of
chemical reactions, the ideal gas law, buffer solutions, the digestive
system, the excretory system, world biomes, protein synthesis, electric
power and energy consumption, the photoelectric effect, the carbon cycle,
weather systems and air masses, the layers of the atmosphere; the Riel
Rebellions, the National Policy, the Klondike Gold Rush, the Underground
Railroad in Canada, the Fenian Raids, Canada's role in the Boer War, the
Regina Manifesto and the CCF, the Pacific Scandal, and Canada's role in
the League of Nations.

Subject keys for Grade 10 are "English", "Math", "Science", "History"
(same as all earlier Grade 10 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes use the curly Unicode form
(’).
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
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


def _rebalance_answer_positions(days, seed=20260722):
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


g10_91_100 = [
day(91, [
E('Reading: Analyzing Satire and Parody',
  'Grade 10 English strand: satire uses humour, irony, or exaggeration to criticize human folly or societal flaws, while parody imitates a specific work or style for comic or critical effect.',
  [('What does satire typically use to criticize human folly or societal flaws?', ['Humour, irony, or exaggeration', 'Only strictly factual, neutral reporting', 'A concept unrelated to reading', 'Silence and blank pages'], 0),
   ('What does a parody typically imitate?', ['A specific work or style, for comic or critical effect', 'Nothing at all; it is entirely original', 'A concept unrelated to satire', 'Only non-fiction textbooks'], 0),
   ('Can satire be used to critique political or social issues?', ['Yes', 'No, satire never engages with political or social issues', 'A concept unrelated to satire', 'Satire only ever discusses unrelated fictional worlds'], 0),
   ('Why might a writer choose satire instead of a direct, serious essay to critique a social issue?', ['Exaggeration and humour can make a critique more memorable and engaging while still making a serious point', 'Satire can never actually communicate a serious point', 'This concept has no connection to reading', 'Direct essays are always more effective than satire at critiquing an issue'], 0),
   ('Why is recognizing parody important when reading a text that closely imitates another well-known work?', ['Recognizing the imitation helps a reader understand the humour or critique being made through the comparison', 'Parody never depends on the reader recognizing an imitated work', 'This concept has no relevance to reading comprehension', 'A parody is always completely unrelated to any other existing work'], 0)]),
M('Matrices: Determinants and Inverses of 2x2 Matrices',
  'Grade 10 Math strand: the determinant of a 2x2 matrix is calculated as ad minus bc, and a matrix has an inverse only when its determinant is not zero.',
  [('For a 2x2 matrix with entries a, b, c, d, how is the determinant calculated?', ['ad minus bc', 'a plus d minus b minus c', 'A concept unrelated to matrices', 'Always exactly zero'], 0),
   ('Does a 2x2 matrix have an inverse when its determinant equals zero?', ['No', 'Yes, every matrix always has an inverse', 'A concept unrelated to determinants', 'The determinant never affects whether an inverse exists'], 0),
   ('What is the determinant of the matrix with a=4, b=2, c=3, d=1?', ['-2', '2', '10', '0'], 0),
   ('Why is checking the determinant an important first step before trying to find a matrix inverse?', ['If the determinant is zero, the matrix has no inverse, so calculating further would be pointless', 'The determinant never has any connection to whether an inverse exists', 'This concept has no connection to math', 'Every matrix inverse can be found regardless of its determinant value'], 0),
   ('Why are matrix inverses useful for solving systems of linear equations written in matrix form?', ['Multiplying by the inverse matrix isolates the variable matrix, similar to dividing in ordinary algebra', 'Matrix inverses have no connection to solving systems of equations', 'This concept has no connection to matrices', 'Systems of equations can never be represented using matrices'], 0)]),
Sc('Chemistry: Types of Chemical Reactions',
   'Grade 10 Science strand: chemical reactions can be classified into types such as synthesis, decomposition, single displacement, double displacement, and combustion, based on how reactants rearrange into products.',
   [('Name one type of chemical reaction, such as synthesis.', ['Synthesis', 'A concept unrelated to chemistry', 'Photosynthesis only', 'Osmosis'], 0),
    ('In a synthesis reaction, do two or more substances combine to form a single product?', ['Yes', 'No, synthesis reactions never combine substances', 'A concept unrelated to synthesis reactions', 'Synthesis reactions only ever break a single substance apart'], 0),
    ('What happens in a decomposition reaction?', ['A single compound breaks down into two or more simpler substances', 'Two elements combine to form a single compound', 'A concept unrelated to chemistry', 'Nothing changes at all'], 0),
    ('Why is classifying a reaction type useful before predicting its products?', ['Recognizing the reaction type helps predict how the reactants will rearrange into products', 'Classifying a reaction type never helps predict its products', 'This concept has no connection to chemistry', 'All chemical reactions always produce identical products regardless of type'], 0),
    ('Why is combustion considered a special type of chemical reaction in everyday life?', ['It releases energy quickly, typically as heat and light, and commonly involves a fuel reacting with oxygen', 'Combustion reactions never release any energy', 'This concept has no relevance to chemistry', 'Combustion reactions never involve oxygen as a reactant'], 0)]),
H('The Riel Rebellions and the Métis Resistance',
  'Grade 10 History strand: Louis Riel led the Métis in the Red River Resistance of 1869-70 and the North-West Rebellion of 1885, resisting the loss of Métis land and rights as Canada expanded westward.',
  [('Who led the Métis resistance movements in 1869-70 and 1885?', ['Louis Riel', 'A concept unrelated to Canadian history', 'A figure with no connection to the Métis', 'A British colonial governor'], 0),
   ('What were the Métis resisting as Canada expanded westward?', ['The loss of their land and rights', 'A change in the national flag', 'A concept unrelated to the Riel Rebellions', 'An increase in taxes on eastern provinces only'], 0),
   ('Did the Red River Resistance take place around 1869-70?', ['Yes', 'No, it took place in the 1950s', 'A concept unrelated to Canadian history', 'The Red River Resistance never actually occurred'], 0),
   ('Why might the westward expansion of Canada in the late 1800s have created tension with Métis communities?', ['Expansion threatened Métis land, way of life, and political control in the region', 'Westward expansion had no effect on Métis communities', 'This concept has no relevance to Canadian history', 'Métis communities were never affected by any government policy'], 0),
   ('Why is Louis Riel a significant and debated figure in Canadian history?', ['He is remembered both as a rebel executed for treason and as a founder of Manitoba and defender of Métis rights', 'Louis Riel has no lasting significance in Canadian history', 'This concept has no relevance to history', 'Louis Riel is remembered only as a minor, unimportant historical figure'], 0)]),
]),

day(92, [
E('Writing: The Elegy and Tribute Writing',
  'Grade 10 English strand: an elegy is a reflective piece of writing, often a poem, that mourns or honours someone who has died, balancing grief with celebration of their life.',
  [('What does an elegy typically mourn or honour?', ['Someone who has died', 'A future event that has not yet happened', 'A concept unrelated to writing', 'A fictional character with no real-world basis'], 0),
   ('Does an elegy often balance grief with celebration of a person’s life?', ['Yes', 'No, an elegy only ever expresses celebration with no grief at all', 'A concept unrelated to elegies', 'An elegy never reflects on a person’s life in any way'], 0),
   ('Which of these is most likely to be a line from an elegy?', ['Though you are gone, your kindness still lights every room we shared.', 'Add 12 and 9 to find the sum.', 'The mitochondria is the powerhouse of the cell.', 'Turn left at the second traffic light.'], 0),
   ('Why might a writer include specific personal memories when writing a tribute to someone who has died?', ['Specific memories help capture the person’s unique character and the impact they had on others', 'Specific personal memories never add anything meaningful to a tribute', 'This concept has no connection to writing', 'Tributes should always avoid mentioning any personal details'], 0),
   ('Why is tone especially important to consider when writing an elegy or tribute?', ['A thoughtful tone can honour the person’s memory while still feeling genuine and heartfelt', 'Tone has no effect on how a tribute or elegy is received', 'This concept has no connection to writing', 'An elegy should always sound completely detached and impersonal'], 0)]),
M('Trigonometric Identities: Double-Angle Formulas',
  'Grade 10 Math strand: double-angle formulas express trigonometric functions of twice an angle, such as sin(2x) equals 2 sin(x) cos(x), in terms of functions of the original angle.',
  [('What does the double-angle formula for sine express?', ['sin(2x) in terms of sin(x) and cos(x)', 'Only the value of x itself', 'A concept unrelated to trigonometry', 'The area of a triangle'], 0),
   ('What is the double-angle identity for sine?', ['sin(2x) = 2 sin(x) cos(x)', 'sin(2x) = sin(x) + cos(x)', 'sin(2x) = 2 sin(x)', 'sin(2x) = cos(x) squared'], 0),
   ('Can double-angle formulas help simplify a trigonometric expression involving 2x?', ['Yes', 'No, double-angle formulas never simplify any expression', 'A concept unrelated to trigonometric identities', 'Double-angle formulas only apply to angles smaller than 2x'], 0),
   ('Why might a double-angle formula be useful when solving a trigonometric equation that contains both sin(x) and sin(2x)?', ['Rewriting sin(2x) in terms of sin(x) and cos(x) allows the whole equation to be expressed using a single angle', 'Double-angle formulas never help when solving equations with multiple angle measures', 'This concept has no connection to math', 'Equations with sin(2x) can never be simplified using any identity'], 0),
   ('Why are trigonometric identities like the double-angle formulas useful tools in calculus and physics applications?', ['They allow complex trigonometric expressions to be rewritten in simpler, more manageable forms', 'Trigonometric identities have no application outside of pure geometry problems', 'This concept has no relevance to trigonometry', 'Calculus and physics never involve any trigonometric expressions'], 0)]),
Sc('Biology: The Digestive System',
   'Grade 10 Science strand: the digestive system breaks down food into nutrients through mechanical and chemical processes across organs including the stomach, small intestine, and large intestine.',
   [('What does the digestive system break food down into?', ['Nutrients', 'Only heat energy', 'A concept unrelated to biology', 'Solid bone tissue'], 0),
    ('Name one organ involved in digestion, such as the stomach.', ['The stomach', 'A concept unrelated to the digestive system', 'The lungs', 'The kidneys'], 0),
    ('Does digestion involve both mechanical and chemical processes?', ['Yes', 'No, digestion is purely a mechanical process with no chemical component', 'A concept unrelated to digestion', 'Digestion never involves any chemical breakdown of food'], 0),
    ('Why does food need to be broken down into smaller nutrient molecules before the body can use it?', ['Smaller molecules can be absorbed into the bloodstream and used by cells for energy and growth', 'Food never needs to be broken down for the body to use it', 'This concept has no connection to biology', 'The body can absorb whole, unbroken pieces of food directly'], 0),
    ('Why is the small intestine considered the primary site of nutrient absorption?', ['Its large surface area, created by structures like villi, allows for efficient absorption into the bloodstream', 'The small intestine has no role in absorbing any nutrients', 'This concept has no relevance to biology', 'Nutrient absorption occurs entirely within the stomach instead'], 0)]),
H('The National Policy and Canadian Economic Nationalism',
  'Grade 10 History strand: introduced by Sir John A. Macdonald in 1879, the National Policy used protective tariffs, railway expansion, and western settlement to build a self-sufficient Canadian economy.',
  [('Who introduced the National Policy in 1879?', ['Sir John A. Macdonald', 'A concept unrelated to Canadian history', 'A figure with no connection to Canadian economic policy', 'A foreign head of state'], 0),
   ('Name one tool used by the National Policy, such as protective tariffs.', ['Protective tariffs', 'A concept unrelated to the National Policy', 'An immediate free trade agreement with Britain', 'A ban on all Canadian manufacturing'], 0),
   ('Did the National Policy aim to build a more self-sufficient Canadian economy?', ['Yes', 'No, the National Policy aimed to weaken the Canadian economy', 'A concept unrelated to the National Policy', 'Economic self-sufficiency was never a goal of Canadian policy'], 0),
   ('Why might protective tariffs have been used to encourage the growth of Canadian manufacturing?', ['Tariffs raised the cost of imported goods, making domestically made products more competitive', 'Protective tariffs never had any effect on domestic manufacturing', 'This concept has no relevance to Canadian history', 'Tariffs only ever applied to goods leaving Canada, not entering it'], 0),
   ('Why was railway expansion considered a key part of the National Policy’s vision for Canada?', ['A transcontinental railway could connect settlers, resources, and markets across the young country', 'Railway expansion had no connection to Canada’s economic development', 'This concept has no relevance to history', 'The National Policy focused exclusively on foreign policy, not infrastructure'], 0)]),
]),

day(93, [
E('Grammar: Conditional Sentences and Hypotheticals',
  'Grade 10 English strand: conditional sentences express a cause-and-effect relationship using an if-clause and a result clause, ranging from real possibilities to purely hypothetical situations.',
  [('What does a conditional sentence typically express?', ['A cause-and-effect relationship using an if-clause', 'A list of unrelated facts', 'A concept unrelated to grammar', 'A question with no possible answer'], 0),
   ('Which sentence is an example of a hypothetical conditional?', ['If I had studied harder, I would have passed the exam.', 'I studied for the exam yesterday.', 'The exam starts at nine o’clock.', 'She passed the exam easily.'], 0),
   ('Do conditional sentences always describe situations that are guaranteed to happen?', ['No', 'Yes, every conditional sentence describes a guaranteed outcome', 'A concept unrelated to conditional sentences', 'Conditional sentences never describe any kind of possibility'], 0),
   ('Why might a writer use a hypothetical conditional sentence to explore an alternate outcome in a story?', ['It allows the writer to explore what might have happened under different circumstances', 'Hypothetical conditionals never add anything meaningful to a story', 'This concept has no connection to writing', 'Alternate outcomes can never be expressed using conditional sentences'], 0),
   ('Why is verb tense important to get right within a conditional sentence?', ['Correct tense usage clarifies whether the situation is realistic, hypothetical, or impossible', 'Verb tense has no effect on the meaning of a conditional sentence', 'This concept has no connection to grammar', 'All conditional sentences use the exact same verb tense regardless of meaning'], 0)]),
M('Geometric Series: Sum to n Terms',
  'Grade 10 Math strand: a geometric series is the sum of terms in a geometric sequence, calculated using the formula S(n) equals a times (1 minus r to the n) divided by (1 minus r), where r is the common ratio.',
  [('What is a geometric series?', ['The sum of terms in a geometric sequence', 'A single isolated term in a sequence', 'A concept unrelated to sequences', 'A sequence that has no defined pattern'], 0),
   ('In the geometric series formula, what does r represent?', ['The common ratio between terms', 'The number of terms in the sequence', 'A concept unrelated to geometric series', 'The first term of the sequence'], 0),
   ('What is the sum of the first three terms of the geometric sequence 2, 4, 8?', ['14', '8', '16', '6'], 0),
   ('Why is the common ratio an essential piece of information when calculating a geometric series sum?', ['The ratio determines how quickly each term grows or shrinks, directly affecting the total sum', 'The common ratio has no effect on the sum of a geometric series', 'This concept has no connection to math', 'A geometric series can be summed without knowing its common ratio'], 0),
   ('Why might understanding geometric series be useful for calculating total compound interest earned over several years?', ['Compound interest grows by a constant ratio each period, matching the structure of a geometric series', 'Geometric series have no connection to compound interest calculations', 'This concept has no connection to sequences', 'Compound interest always grows by a constant amount, not a constant ratio'], 0)]),
Sc('Physics: The Photoelectric Effect and Quantum Physics Basics',
   'Grade 10 Science strand: the photoelectric effect occurs when light striking a metal surface ejects electrons, providing early evidence that light behaves as discrete packets of energy called photons.',
   [('What happens during the photoelectric effect?', ['Light striking a metal surface ejects electrons', 'A metal surface absorbs sound waves', 'A concept unrelated to physics', 'A magnet attracts a piece of metal'], 0),
    ('What name is given to the discrete packets of energy that make up light, evidenced by the photoelectric effect?', ['Photons', 'Neutrons', 'A concept unrelated to quantum physics', 'Protons'], 0),
    ('Did the photoelectric effect provide early evidence that light has particle-like properties?', ['Yes', 'No, it provided no evidence about the nature of light at all', 'A concept unrelated to the photoelectric effect', 'It proved light behaves only as a continuous wave with no particle properties'], 0),
    ('Why was the photoelectric effect difficult to explain using only a classical wave model of light?', ['A pure wave model could not account for the immediate ejection of electrons regardless of light intensity at certain frequencies', 'The wave model of light perfectly explained every aspect of the photoelectric effect', 'This concept has no connection to physics', 'The photoelectric effect has nothing to do with how light behaves'], 0),
    ('Why is the photoelectric effect considered an important foundation for the development of quantum physics?', ['It helped demonstrate that energy can be transferred in discrete quantized packets rather than continuously', 'The photoelectric effect had no influence on the development of quantum physics', 'This concept has no relevance to physics', 'Quantum physics developed with no connection to any experimental evidence'], 0)]),
H('The Klondike Gold Rush',
  'Grade 10 History strand: the Klondike Gold Rush of 1896-99 drew tens of thousands of prospectors to the Yukon, spurring rapid settlement, infrastructure development, and Yukon’s creation as a separate territory in 1898.',
  [('In what region did the Klondike Gold Rush take place?', ['The Yukon', 'A concept unrelated to Canadian history', 'Southern Ontario', 'The Maritime provinces'], 0),
   ('What drew tens of thousands of prospectors to the Yukon in the late 1890s?', ['The discovery of gold', 'A newly built university', 'A concept unrelated to the Klondike Gold Rush', 'A major sporting event'], 0),
   ('Did the Yukon become a separate territory partly because of the Gold Rush’s rapid population growth?', ['Yes', 'No, the Yukon’s territorial status had no connection to the Gold Rush', 'A concept unrelated to Canadian history', 'The Yukon has never been recognized as a distinct territory'], 0),
   ('Why might the sudden arrival of tens of thousands of prospectors have created urgent infrastructure challenges in the Yukon?', ['Existing settlements were not prepared to house, feed, and transport such a rapid and massive increase in population', 'A rapid population increase never creates any infrastructure challenges', 'This concept has no relevance to Canadian history', 'The Yukon already had extensive infrastructure in place before the Gold Rush began'], 0),
   ('Why is the Klondike Gold Rush often studied alongside its impact on Indigenous peoples of the Yukon?', ['The rapid influx of newcomers significantly disrupted the land, resources, and ways of life of local Indigenous communities', 'The Gold Rush had no effect on Indigenous peoples living in the Yukon', 'This concept has no relevance to history', 'Indigenous communities were not present in the Yukon before the Gold Rush'], 0)]),
]),

day(94, [
E('Literature: The Road Novel and Journey Narratives',
  'Grade 10 English strand: the road novel follows a character’s physical journey, often paralleling an internal journey of self-discovery, growth, or transformation.',
  [('What kind of journey does a road novel typically follow?', ['A physical journey that often parallels an internal one', 'A journey that takes place entirely in a single room', 'A concept unrelated to literature', 'A journey with no characters involved at all'], 0),
   ('Can a road novel’s physical journey parallel a character’s internal growth or transformation?', ['Yes', 'No, a road novel’s journey never connects to internal growth', 'A concept unrelated to road novels', 'Physical and internal journeys are always completely unrelated in fiction'], 0),
   ('Why might a road novel use travel through unfamiliar places to reveal something about a character?', ['New environments and challenges can force a character to confront their assumptions and grow', 'Unfamiliar places never reveal anything meaningful about a character', 'This concept has no connection to literature', 'A road novel’s setting never has any effect on its characters'], 0),
   ('Which of these best reflects a common structure of a road novel?', ['A character sets out on a journey and returns changed by what they experienced along the way.', 'A character never leaves their home throughout the entire story.', 'A story told entirely through a series of unrelated recipes.', 'A textbook chapter listing historical dates with no narrative.'], 0),
   ('Why might studying the road novel genre help readers understand how setting can shape a story’s themes?', ['The changing landscapes and encounters along the journey often directly connect to the novel’s central themes', 'Setting never has any connection to a story’s themes in a road novel', 'This concept has no relevance to literature', 'Road novels never actually involve any change in setting'], 0)]),
M('Statistics: Correlation vs Causation',
  'Grade 10 Math strand: correlation describes a relationship between two variables, but correlation alone does not prove that one variable causes the other to change.',
  [('What does correlation describe between two variables?', ['A relationship or pattern between them', 'A guarantee that one variable causes the other', 'A concept unrelated to statistics', 'The exact numerical value of both variables'], 0),
   ('Does correlation alone prove that one variable causes changes in the other?', ['No', 'Yes, correlation always proves causation', 'A concept unrelated to correlation', 'Causation can never be studied using statistics'], 0),
   ('If ice cream sales and drowning incidents both rise in summer, what does this most likely represent?', ['A correlation caused by a third factor (warm weather), not direct causation', 'Proof that ice cream sales cause drowning incidents', 'A concept unrelated to statistics', 'Proof that drowning incidents cause ice cream sales'], 0),
   ('Why is it important to consider other possible explanations before concluding that one variable causes another?', ['A third, unconsidered variable might actually be responsible for changes in both variables being studied', 'Considering other explanations never matters when analyzing a correlation', 'This concept has no connection to statistics', 'Every correlation always has a single, obvious direct cause'], 0),
   ('Why might scientists design controlled experiments rather than relying only on correlational data to establish causation?', ['Controlled experiments can isolate variables and rule out other explanations in a way correlational data alone cannot', 'Controlled experiments never provide any advantage over correlational data', 'This concept has no connection to statistics', 'Correlational data always provides definitive proof of causation on its own'], 0)]),
Sc('Earth Science: The Carbon Cycle',
   'Grade 10 Science strand: the carbon cycle describes how carbon moves between the atmosphere, oceans, living organisms, and the earth through processes such as photosynthesis, respiration, and combustion.',
   [('What does the carbon cycle describe?', ['How carbon moves between the atmosphere, oceans, organisms, and the earth', 'How electricity flows through a circuit', 'A concept unrelated to earth science', 'How rocks form deep underground only'], 0),
    ('Name one process involved in the carbon cycle, such as photosynthesis.', ['Photosynthesis', 'A concept unrelated to the carbon cycle', 'Magnetism', 'Refraction'], 0),
    ('Does burning fossil fuels release carbon into the atmosphere?', ['Yes', 'No, burning fossil fuels never releases carbon into the atmosphere', 'A concept unrelated to the carbon cycle', 'Fossil fuels contain no carbon at all'], 0),
    ('Why might increased combustion of fossil fuels disrupt the natural balance of the carbon cycle?', ['It releases stored carbon into the atmosphere faster than natural processes can absorb it, increasing atmospheric carbon dioxide', 'Combustion of fossil fuels never affects the balance of the carbon cycle', 'This concept has no connection to earth science', 'The carbon cycle is entirely unaffected by any human activity'], 0),
    ('Why are oceans and forests often described as important carbon sinks?', ['They absorb and store significant amounts of atmospheric carbon dioxide, helping regulate the carbon cycle', 'Oceans and forests never absorb or store any carbon', 'This concept has no relevance to earth science', 'Carbon sinks have no connection to the overall carbon cycle'], 0)]),
H('The Underground Railroad and Early Black Communities in Canada',
  'Grade 10 History strand: the Underground Railroad was a network of secret routes and safe houses that helped freedom seekers escape enslavement in the United States, with many settling and building communities in Canada.',
  [('What was the Underground Railroad?', ['A network of secret routes and safe houses helping freedom seekers escape enslavement', 'A literal underground train system built in Canada', 'A concept unrelated to Canadian history', 'A government program to build new highways'], 0),
   ('Where did many freedom seekers who used the Underground Railroad settle?', ['In Canada', 'A concept unrelated to the Underground Railroad', 'Nowhere; freedom seekers never actually reached any destination', 'Exclusively in the southern United States'], 0),
   ('Did some freedom seekers build lasting Black communities in Canada after arriving?', ['Yes', 'No, no lasting communities were ever established in Canada', 'A concept unrelated to the Underground Railroad', 'All freedom seekers immediately returned to the United States'], 0),
   ('Why might Canada have been an appealing destination for freedom seekers travelling the Underground Railroad?', ['Slavery had been abolished across the British Empire, offering freedom seekers legal protection from enslavement', 'Canada offered no legal protection or safety for freedom seekers at the time', 'This concept has no relevance to Canadian history', 'The Underground Railroad had no connection to Canada whatsoever'], 0),
   ('Why is studying the history of early Black communities in Canada important for understanding the country’s full history?', ['It reveals a significant part of Canada’s past often underrepresented in broader historical narratives', 'Early Black communities in Canada have no historical significance', 'This concept has no relevance to history', 'Black Canadian history has no connection to the broader story of Canada'], 0)]),
]),

day(95, [
E('Oral Communication: The Toast and Ceremonial Speech',
  'Grade 10 English strand: a ceremonial speech, such as a toast, marks a special occasion by honouring a person or event, typically balancing sincerity, brevity, and an appropriate tone.',
  [('What does a ceremonial speech, such as a toast, typically mark?', ['A special occasion, honouring a person or event', 'A routine, everyday announcement', 'A concept unrelated to oral communication', 'A formal complaint about a product'], 0),
   ('Should a ceremonial speech generally balance sincerity, brevity, and an appropriate tone?', ['Yes', 'No, ceremonial speeches should always be as long as possible', 'A concept unrelated to ceremonial speeches', 'Tone never matters in a ceremonial speech'], 0),
   ('Which of these would most likely appear in a wedding toast?', ['I have watched their friendship grow into something truly special, and I could not be prouder to celebrate them today.', 'The mitochondria is the powerhouse of the cell.', 'Please submit your assignment by Friday at noon.', 'Turn to page forty-two in your textbook.'], 0),
   ('Why might a speaker share a brief, specific anecdote in a toast rather than only general praise?', ['A specific anecdote can make the tribute feel more personal, genuine, and memorable to the audience', 'Specific anecdotes never add anything meaningful to a toast', 'This concept has no connection to oral communication', 'General praise is always more effective than a specific story'], 0),
   ('Why is knowing your audience especially important when preparing a ceremonial speech?', ['Understanding the audience helps the speaker choose appropriate tone, references, and length for the occasion', 'The audience never affects how a ceremonial speech should be prepared', 'This concept has no relevance to oral communication', 'Every ceremonial speech should be delivered in exactly the same way regardless of audience'], 0)]),
M('Probability: Tree Diagrams and Compound Events',
  'Grade 10 Math strand: a probability tree diagram visually maps out all possible outcomes of a sequence of events, making it easier to calculate the probability of compound events.',
  [('What does a probability tree diagram help visualize?', ['All possible outcomes of a sequence of events', 'Only the outcome of a single isolated event', 'A concept unrelated to probability', 'The area of a geometric shape'], 0),
   ('If a coin is flipped twice, how many total outcome branches appear at the end of a tree diagram?', ['Four', 'Two', 'Eight', 'One'], 0),
   ('To find the probability of a specific path through a tree diagram, what operation is typically used on the branch probabilities?', ['Multiplication', 'Addition', 'A concept unrelated to tree diagrams', 'Subtraction'], 0),
   ('Why might a tree diagram be especially helpful when calculating the probability of a specific sequence of independent events?', ['It organizes each stage of the event clearly, making it easier to multiply the correct branch probabilities together', 'Tree diagrams never help with calculating probabilities of a sequence of events', 'This concept has no connection to math', 'Sequences of events can never be represented visually'], 0),
   ('Why might a tree diagram become impractical for events with a very large number of possible outcomes?', ['The diagram would need so many branches that it becomes difficult to draw and read clearly', 'Tree diagrams work equally well no matter how many outcomes are involved', 'This concept has no connection to probability', 'The number of outcomes never affects how practical a tree diagram is'], 0)]),
Sc('Biology: World Biomes',
   'Grade 10 Science strand: a biome is a large region characterized by its climate, and the plant and animal communities adapted to it, such as tundra, taiga, grassland, desert, and rainforest.',
   [('What is a biome primarily characterized by?', ['Its climate, and the plants and animals adapted to it', 'Only the colour of its soil', 'A concept unrelated to biology', 'The number of humans who live there'], 0),
    ('Name one type of biome, such as tundra.', ['Tundra', 'A concept unrelated to biomes', 'A concept unrelated to Earth’s regions', 'A single species of animal'], 0),
    ('Are organisms in a specific biome typically adapted to survive its particular climate conditions?', ['Yes', 'No, organisms are never adapted to their biome’s climate', 'A concept unrelated to biomes', 'Climate has no connection to which organisms live in a biome'], 0),
    ('Why might animals in a desert biome have adaptations for conserving water?', ['Desert biomes typically receive very little rainfall, so water conservation improves an organism’s chance of survival', 'Desert animals never need any special adaptations to survive', 'This concept has no connection to biology', 'Deserts always receive plentiful rainfall throughout the year'], 0),
    ('Why is understanding biomes useful for predicting how climate change might affect different regions of the world?', ['Since biomes are defined by climate, shifting climate patterns could alter which species can survive in a given region', 'Biomes have no connection to climate and are therefore unaffected by climate change', 'This concept has no relevance to biology', 'Every biome responds to climate change in exactly the same way'], 0)]),
H('The Fenian Raids and Pre-Confederation Defence',
  'Grade 10 History strand: the Fenian Raids of the 1860s, a series of small-scale attacks by Irish-American militants along the Canadian border, heightened concerns about defence and helped push the colonies toward Confederation.',
  [('Who carried out the Fenian Raids of the 1860s?', ['Irish-American militants', 'A concept unrelated to Canadian history', 'The British Royal Navy', 'French colonial forces'], 0),
   ('Where did the Fenian Raids generally take place?', ['Along the Canadian border', 'Deep within the Arctic', 'A concept unrelated to the Fenian Raids', 'Exclusively in British Columbia'], 0),
   ('Did the Fenian Raids heighten concerns about colonial defence in British North America?', ['Yes', 'No, the raids caused no concern about defence at all', 'A concept unrelated to the Fenian Raids', 'Defence was never a consideration for the colonies at this time'], 0),
   ('Why might the threat posed by the Fenian Raids have encouraged the British North American colonies to consider uniting?', ['A larger, united colony could organize a stronger, more coordinated defence than several separate small colonies', 'The threat of the raids had no influence on colonial unification efforts', 'This concept has no relevance to Canadian history', 'Individual colonies were always better equipped for defence than a unified one'], 0),
   ('Why are the Fenian Raids often mentioned alongside the broader story of Confederation in 1867?', ['They are considered one of several factors that pushed the colonies toward seeking greater unity and security', 'The Fenian Raids have no connection to the story of Confederation', 'This concept has no relevance to history', 'Confederation occurred with no external pressures influencing the decision'], 0)]),
]),

day(96, [
E('Reading: Analyzing Multiple Narrators',
  'Grade 10 English strand: stories told through multiple narrators present the same events from different perspectives, allowing readers to compare viewpoints and assess each narrator’s reliability.',
  [('What can multiple narrators present in a story?', ['The same events from different perspectives', 'Only a single, unchanging viewpoint', 'A concept unrelated to reading', 'A story with no characters at all'], 0),
   ('Can comparing multiple narrators help readers assess each narrator’s reliability?', ['Yes', 'No, comparing narrators never reveals anything about reliability', 'A concept unrelated to multiple narrators', 'All narrators are always equally reliable by default'], 0),
   ('Why might an author use multiple narrators instead of a single narrator to tell a story?', ['It allows readers to see a fuller, more complex picture of events and characters', 'Multiple narrators never add anything meaningful to how a story is told', 'This concept has no connection to reading', 'A single narrator always provides a more complete picture than multiple narrators'], 0),
   ('If two narrators describe the same conversation very differently, what might a careful reader conclude?', ['At least one narrator’s perspective, memory, or bias is shaping how they describe the event', 'The two descriptions must both be entirely accurate with no difference at all', 'This concept has no connection to reading comprehension', 'Differences between narrators never provide any useful insight'], 0),
   ('Why is tracking whose perspective is being presented important when reading a multi-narrator novel?', ['Understanding which narrator is speaking helps readers correctly interpret events, tone, and bias in that section', 'It never matters whose perspective is being presented in a multi-narrator novel', 'This concept has no relevance to reading comprehension', 'Every narrator in a novel always presents the exact same interpretation of events'], 0)]),
M('Functions: Composition of Functions',
  'Grade 10 Math strand: function composition combines two functions by applying one function to the output of another, written as f(g(x)), evaluating g(x) first.',
  [('In the composition f(g(x)), which function is evaluated first?', ['g(x)', 'f(x)', 'A concept unrelated to function composition', 'Neither function is ever evaluated'], 0),
   ('If f(x) = x + 3 and g(x) = 2x, what is f(g(2))?', ['7', '10', '5', '4'], 0),
   ('Does function composition combine two functions by using the output of one as the input of the other?', ['Yes', 'No, function composition never uses one function’s output as another’s input', 'A concept unrelated to function composition', 'Composition always adds the two functions together instead'], 0),
   ('Why is the order of functions important when evaluating a composition like f(g(x))?', ['Changing the order can produce a completely different result, since g(x) is evaluated before applying f', 'The order of functions never affects the result of a composition', 'This concept has no connection to math', 'f(g(x)) and g(f(x)) always produce exactly the same result'], 0),
   ('Why might function composition be useful for modelling a real-world process with multiple sequential steps, such as a discount followed by a tax?', ['Each function can represent one step, and composing them models applying the steps in the correct sequential order', 'Function composition has no application to modelling multi-step real-world processes', 'This concept has no connection to functions', 'Multi-step processes can never be represented using function composition'], 0)]),
Sc('Physics: Electric Power and Energy Consumption',
   'Grade 10 Science strand: electric power, measured in watts, describes the rate at which electrical energy is transferred or converted, and energy consumption over time is often billed in kilowatt-hours.',
   [('In what unit is electric power typically measured?', ['Watts', 'Litres', 'A concept unrelated to physics', 'Metres'], 0),
    ('What does electric power describe?', ['The rate at which electrical energy is transferred or converted', 'The total distance travelled by an electric current', 'A concept unrelated to electric power', 'The colour of an electrical wire'], 0),
    ('Is electricity consumption on a household bill commonly measured in kilowatt-hours?', ['Yes', 'No, household electricity bills never use any unit of measurement', 'A concept unrelated to energy consumption', 'Electricity bills are always measured only in watts, never kilowatt-hours'], 0),
    ('Why might leaving a high-power appliance running for many hours significantly increase an electricity bill?', ['Total energy consumed depends on both the power rating and the length of time the appliance runs', 'The length of time an appliance runs never affects total energy consumption', 'This concept has no connection to physics', 'Electricity bills are calculated using only the appliance’s power rating, ignoring time'], 0),
    ('Why is understanding electric power and energy consumption useful for making decisions about home energy efficiency?', ['It helps identify which appliances use the most energy, informing choices that can reduce electricity costs', 'Electric power has no connection to household energy efficiency decisions', 'This concept has no relevance to physics', 'Energy consumption is identical for every appliance regardless of its power rating'], 0)]),
H('Canada’s Role in the Boer War',
  'Grade 10 History strand: Canada sent volunteer troops to support Britain in the South African (Boer) War of 1899-1902, marking one of the first times Canada contributed forces to a British imperial conflict overseas.',
  [('Which country did Canada send troops to support during the Boer War?', ['Britain', 'A concept unrelated to Canadian history', 'A country with no connection to the Boer War', 'The United States'], 0),
   ('In what years did the Boer War take place?', ['1899-1902', '1812-1815', 'A concept unrelated to the Boer War', '1945-1948'], 0),
   ('Was the Boer War one of the first conflicts in which Canada sent troops overseas as part of a British imperial effort?', ['Yes', 'No, Canada had already sent troops overseas many times before this', 'A concept unrelated to the Boer War', 'Canada never sent any troops to support Britain in this conflict'], 0),
   ('Why might Canada’s decision to send volunteer troops to the Boer War have sparked debate at home?', ['Some Canadians felt a strong loyalty to Britain, while others questioned involvement in a conflict distant from Canadian interests', 'No Canadians held any opinion at all about sending troops overseas', 'This concept has no relevance to Canadian history', 'The decision to send troops was entirely uncontroversial and unanimous'], 0),
   ('Why is Canada’s involvement in the Boer War often seen as an early step in the development of Canadian foreign policy?', ['It raised early questions about how much independence Canada should exercise in decisions about overseas military involvement', 'The Boer War had no connection to the development of Canadian foreign policy', 'This concept has no relevance to history', 'Canadian foreign policy has never been influenced by military involvement decisions'], 0)]),
]),

day(97, [
E('Writing: The Historical Fiction Short Story',
  'Grade 10 English strand: historical fiction blends invented characters and plot with accurate historical settings and events, requiring research to balance creativity with authenticity.',
  [('What does historical fiction typically blend?', ['Invented characters and plot with accurate historical settings and events', 'Only real events with no invented elements at all', 'A concept unrelated to writing', 'Random, unrelated topics with no research involved'], 0),
   ('Does writing historical fiction typically require research into a real historical period?', ['Yes', 'No, historical fiction requires no research whatsoever', 'A concept unrelated to historical fiction', 'Research is only needed for non-fiction, never fiction'], 0),
   ('Why might a writer research small, everyday details of a historical period, such as clothing or food, before writing a story set in that era?', ['Accurate details help create a believable, immersive setting for readers', 'Small details about daily life never matter when writing historical fiction', 'This concept has no connection to writing', 'Readers never notice or care about historical accuracy in fiction'], 0),
   ('Why must a historical fiction writer balance creative invention with factual accuracy?', ['Straying too far from established facts can undermine the story’s credibility, while too little creativity can feel like a dry report', 'Historical accuracy never matters as long as the story is entertaining', 'This concept has no connection to writing', 'Creative invention and factual accuracy are never both required at the same time'], 0),
   ('Why might historical fiction be a valuable way to help readers connect emotionally with a past event?', ['Following an individual character’s experience can make a distant historical event feel personal and relatable', 'Historical fiction never helps readers connect emotionally with the past', 'This concept has no relevance to writing', 'Emotional connection is only ever possible through non-fiction writing'], 0)]),
M('Geometry: Similar Triangles and Indirect Measurement',
  'Grade 10 Math strand: similar triangles have equal corresponding angles and proportional sides, allowing indirect measurement of heights or distances that are difficult to measure directly.',
  [('What is true of the corresponding angles in similar triangles?', ['They are equal', 'They always add up to 180 degrees combined', 'A concept unrelated to geometry', 'They are always right angles'], 0),
   ('What is true of the corresponding sides in similar triangles?', ['They are proportional', 'They are always exactly equal in length', 'A concept unrelated to similar triangles', 'They have no relationship to each other'], 0),
   ('Can similar triangles be used to indirectly measure the height of a tall object, like a tree?', ['Yes', 'No, similar triangles can never be used for indirect measurement', 'A concept unrelated to indirect measurement', 'Indirect measurement is only possible using a measuring tape'], 0),
   ('Why is the shadow method, using similar triangles, a practical way to measure the height of a very tall building?', ['It avoids the need to physically climb or directly measure the building by comparing proportional shadow lengths instead', 'The shadow method never provides an accurate estimate of height', 'This concept has no connection to geometry', 'Similar triangles have no connection to measuring shadows or heights'], 0),
   ('Why must the ground be level and the sun’s angle be accounted for when using shadows and similar triangles to estimate height?', ['Uneven ground or an inconsistent light angle could distort the shadow lengths, leading to an inaccurate proportional comparison', 'Ground conditions and light angle never have any effect on this measurement method', 'This concept has no connection to math', 'Shadows are always exactly proportional regardless of any outside conditions'], 0)]),
Sc('Chemistry: The Ideal Gas Law',
   'Grade 10 Science strand: the ideal gas law, PV equals nRT, relates a gas’s pressure, volume, amount, and temperature, extending the individual gas laws into a single combined relationship.',
   [('What four quantities does the ideal gas law relate?', ['Pressure, volume, amount of gas, and temperature', 'Only mass and colour', 'A concept unrelated to chemistry', 'Only the size and shape of the container'], 0),
    ('What does the letter R represent in the ideal gas law equation?', ['The universal gas constant', 'The mass of the gas sample', 'A concept unrelated to the ideal gas law', 'The exact temperature of the gas'], 0),
    ('Does the ideal gas law combine relationships found in the individual gas laws, like Boyle’s and Charles’s laws?', ['Yes', 'No, the ideal gas law has no connection to the individual gas laws', 'A concept unrelated to the ideal gas law', 'The individual gas laws are completely unrelated to pressure, volume, or temperature'], 0),
    ('Why is the ideal gas law considered more broadly useful than any single individual gas law on its own?', ['It allows multiple variables to be related and solved for at once, rather than holding all but two quantities constant', 'The ideal gas law is never more useful than the individual gas laws', 'This concept has no connection to chemistry', 'The ideal gas law can only be applied when every variable is already known'], 0),
    ('Why might real gases behave slightly differently from what the ideal gas law predicts under very high pressure or low temperature?', ['Real gas particles have volume and intermolecular forces that the ideal gas law’s simplified assumptions do not fully account for', 'Real gases always behave in exactly the same way the ideal gas law predicts under every condition', 'This concept has no relevance to chemistry', 'Pressure and temperature never have any effect on how closely a gas follows the ideal gas law'], 0)]),
H('The Regina Manifesto and the Founding of the CCF',
  'Grade 10 History strand: the Co-operative Commonwealth Federation, founded in 1932 and outlined in the 1933 Regina Manifesto, called for economic planning and social welfare reforms in response to the hardships of the Great Depression.',
  [('What political movement was outlined in the 1933 Regina Manifesto?', ['The Co-operative Commonwealth Federation (CCF)', 'A concept unrelated to Canadian history', 'A movement with no connection to Canadian politics', 'A regional business association'], 0),
   ('What economic hardship influenced the founding of the CCF?', ['The Great Depression', 'A concept unrelated to the CCF', 'A period of Canadian economic prosperity with no hardship at all', 'A temporary shortage of imported goods'], 0),
   ('Did the Regina Manifesto call for economic planning and social welfare reforms?', ['Yes', 'No, it called for the elimination of all government involvement in the economy', 'A concept unrelated to the Regina Manifesto', 'Social welfare reform was never part of the CCF’s platform'], 0),
   ('Why might widespread economic hardship during the Great Depression have encouraged support for a new political movement like the CCF?', ['Many Canadians facing unemployment and poverty sought new political solutions beyond the existing major parties', 'Economic hardship never influences interest in new political movements', 'This concept has no relevance to Canadian history', 'The Great Depression had no connection to the founding of the CCF'], 0),
   ('Why is the CCF considered significant in the broader history of Canadian social policy?', ['Many of its early proposals influenced later Canadian social programs, including aspects of the welfare state', 'The CCF had no lasting influence on later Canadian social policy', 'This concept has no relevance to history', 'Canadian social programs developed with no connection to earlier political movements'], 0)]),
]),

day(98, [
E('Grammar: The Subjunctive Mood',
  'Grade 10 English strand: the subjunctive mood expresses wishes, hypothetical situations, or demands, often appearing after phrases like if I were or it is important that.',
  [('What does the subjunctive mood typically express?', ['Wishes, hypothetical situations, or demands', 'Only simple, factual statements', 'A concept unrelated to grammar', 'Questions with a definite yes or no answer'], 0),
   ('Which sentence correctly uses the subjunctive mood?', ['If I were taller, I would join the basketball team.', 'If I was taller, I would join the basketball team.', 'If I am taller, I would join the basketball team.', 'If I will be taller, I would join the basketball team.'], 0),
   ('Does the subjunctive mood often appear after phrases like it is important that?', ['Yes', 'No, the subjunctive mood never follows such phrases', 'A concept unrelated to the subjunctive mood', 'That phrase always requires the simple past tense instead'], 0),
   ('Why might a writer use the subjunctive mood when describing a wish or an unreal situation?', ['The subjunctive mood signals to readers that the situation being described is hypothetical, not factual', 'The subjunctive mood never signals anything different from a regular factual statement', 'This concept has no connection to grammar', 'Wishes and hypothetical situations are always expressed using the simple present tense'], 0),
   ('Why might correctly using the subjunctive mood strengthen formal or academic writing?', ['It shows precise control over grammar and clearly distinguishes hypothetical ideas from stated facts', 'The subjunctive mood has no effect on the quality or clarity of formal writing', 'This concept has no connection to writing', 'Formal writing should always avoid using the subjunctive mood entirely'], 0)]),
M('Exponential and Logarithmic Equations: Solving Techniques',
  'Grade 10 Math strand: exponential equations can be solved by matching bases or applying logarithms to both sides, while logarithmic equations are often solved by rewriting them in exponential form.',
  [('What is one method for solving an exponential equation when both sides can be written with the same base?', ['Matching bases and setting the exponents equal', 'Ignoring the exponents completely', 'A concept unrelated to exponential equations', 'Always assuming the answer is zero'], 0),
   ('Solve for x: 2 to the power of x equals 8.', ['3', '4', '2', '8'], 0),
   ('What is one common method for solving a logarithmic equation?', ['Rewriting it in exponential form', 'Ignoring the logarithm entirely', 'A concept unrelated to logarithmic equations', 'Always assuming x equals one'], 0),
   ('Why might applying a logarithm to both sides of an exponential equation be useful when the bases cannot easily be matched?', ['Logarithms allow the variable exponent to be brought down and solved using regular algebraic steps', 'Applying a logarithm never helps solve an exponential equation', 'This concept has no connection to math', 'Exponential equations can only ever be solved by guessing and checking'], 0),
   ('Why is checking a solution important after solving a logarithmic equation?', ['Logarithms are undefined for zero or negative values, so a solution must be checked to ensure it is valid', 'Solutions to logarithmic equations never need to be checked for validity', 'This concept has no connection to logarithms', 'Every possible numerical solution is always valid for a logarithmic equation'], 0)]),
Sc('Biology: Protein Synthesis',
   'Grade 10 Science strand: protein synthesis occurs through transcription, where DNA is copied into messenger RNA, and translation, where that RNA is used to assemble a specific sequence of amino acids into a protein.',
   [('What are the two main stages of protein synthesis?', ['Transcription and translation', 'Digestion and absorption', 'A concept unrelated to biology', 'Mitosis and meiosis'], 0),
    ('What happens during transcription?', ['DNA is copied into messenger RNA', 'A protein is broken down into amino acids', 'A concept unrelated to protein synthesis', 'A cell divides into two identical cells'], 0),
    ('Does translation involve assembling amino acids into a protein based on an RNA sequence?', ['Yes', 'No, translation never involves assembling amino acids', 'A concept unrelated to translation', 'Amino acids are assembled with no connection to RNA at all'], 0),
    ('Why is the order of amino acids assembled during translation so important to a protein’s final function?', ['The specific sequence determines how the protein folds and functions, so errors can disrupt that function', 'The order of amino acids never has any effect on how a protein functions', 'This concept has no connection to biology', 'Proteins function identically regardless of their amino acid sequence'], 0),
    ('Why is understanding protein synthesis important for understanding how genetic mutations can affect an organism?', ['A mutation in DNA can change the RNA sequence and ultimately the protein produced, potentially altering its function', 'Genetic mutations never have any connection to protein synthesis', 'This concept has no relevance to biology', 'Proteins are produced identically regardless of any change in the underlying DNA'], 0)]),
H('The Pacific Scandal and Early Political Corruption',
  'Grade 10 History strand: the Pacific Scandal of 1873 involved allegations that Sir John A. Macdonald’s government accepted funds in exchange for railway contracts, leading to his government’s resignation.',
  [('What did the Pacific Scandal of 1873 involve allegations of?', ['Accepting funds in exchange for railway contracts', 'A dispute over provincial boundaries', 'A concept unrelated to Canadian history', 'A disagreement about the national anthem'], 0),
   ('Who was the prime minister whose government was implicated in the Pacific Scandal?', ['Sir John A. Macdonald', 'A concept unrelated to the Pacific Scandal', 'A prime minister with no connection to this scandal', 'A provincial premier, not a prime minister'], 0),
   ('Did the Pacific Scandal lead to the resignation of Macdonald’s government?', ['Yes', 'No, the government faced no consequences at all', 'A concept unrelated to the Pacific Scandal', 'The scandal had no effect on Macdonald’s government whatsoever'], 0),
   ('Why might allegations of accepting funds in exchange for railway contracts have been especially damaging to public trust in government at the time?', ['It suggested that major national infrastructure decisions could be influenced by private financial interests rather than the public good', 'Allegations like this never affect public trust in government', 'This concept has no relevance to Canadian history', 'Railway contracts had no connection to public trust in government decisions'], 0),
   ('Why is the Pacific Scandal often referenced when discussing the importance of political accountability in Canadian history?', ['It illustrates an early example of a government facing real consequences for alleged corruption', 'The Pacific Scandal has no connection to discussions of political accountability', 'This concept has no relevance to history', 'Canadian governments have never faced any consequences for alleged wrongdoing'], 0)]),
]),

day(99, [
E('Literature: Environmental and Eco-Fiction',
  'Grade 10 English strand: eco-fiction explores humanity’s relationship with the natural world, often examining environmental crisis, conservation, or the consequences of humanity’s impact on ecosystems.',
  [('What does eco-fiction typically explore?', ['Humanity’s relationship with the natural world', 'Only unrelated fantasy worlds with no connection to nature', 'A concept unrelated to literature', 'Historical battles with no environmental themes'], 0),
   ('Can eco-fiction examine the consequences of humanity’s impact on ecosystems?', ['Yes', 'No, eco-fiction never addresses humanity’s impact on ecosystems', 'A concept unrelated to eco-fiction', 'Environmental themes are never present in eco-fiction'], 0),
   ('Why might an author write eco-fiction to raise awareness about an environmental issue rather than write a non-fiction article?', ['A compelling story can create emotional engagement that makes an environmental issue feel more urgent and personal', 'Fiction can never raise awareness about a real environmental issue', 'This concept has no connection to literature', 'Non-fiction articles are always more effective than fiction at raising awareness'], 0),
   ('Which of these best reflects a typical theme found in eco-fiction?', ['A community grapples with the long-term consequences of a polluted river on their way of life.', 'A recipe for baking bread from scratch.', 'A step-by-step guide to assembling furniture.', 'A weather forecast for the coming week.'], 0),
   ('Why might studying eco-fiction be valuable for understanding both literary techniques and real-world environmental issues?', ['It combines careful analysis of storytelling with meaningful engagement in pressing real-world environmental concerns', 'Eco-fiction has no connection to real-world environmental issues', 'This concept has no relevance to literature', 'Literary techniques and environmental issues can never be studied together'], 0)]),
M('Financial Literacy: Mortgages and Loan Amortization Schedules',
  'Grade 10 Math strand: a mortgage is a long-term loan for purchasing property, and an amortization schedule shows how each payment is split between interest and principal over the life of the loan.',
  [('What is a mortgage generally used for?', ['Purchasing property', 'Buying groceries', 'A concept unrelated to financial literacy', 'Paying for a single meal at a restaurant'], 0),
   ('What does an amortization schedule show?', ['How each payment is split between interest and principal over time', 'Only the total number of payments remaining', 'A concept unrelated to amortization', 'The exact market value of a home'], 0),
   ('In the early years of a typical mortgage, does a larger portion of each payment usually go toward interest rather than principal?', ['Yes', 'No, the payment is always split evenly between interest and principal every month', 'A concept unrelated to amortization schedules', 'Every payment goes entirely toward the principal from the very first month'], 0),
   ('Why is understanding an amortization schedule useful for someone considering paying extra toward their mortgage principal?', ['It shows how extra principal payments can reduce total interest paid and shorten the loan’s overall length', 'Amortization schedules never show any connection between extra payments and total interest', 'This concept has no connection to financial literacy', 'Paying extra toward the principal never has any effect on a loan'], 0),
   ('Why might comparing mortgages with different interest rates and terms be an important skill for making a major financial decision?', ['Small differences in rate or term can significantly change the total amount of interest paid over the life of the loan', 'Interest rate and loan term never affect the total cost of a mortgage', 'This concept has no relevance to financial literacy', 'Every mortgage costs exactly the same regardless of its rate or term'], 0)]),
Sc('Earth Science: Weather Systems and Air Masses',
   'Grade 10 Science strand: weather systems form from the interaction of air masses with different temperature and moisture characteristics, with fronts marking the boundaries where these air masses meet.',
   [('What forms when air masses with different temperature and moisture characteristics interact?', ['Weather systems', 'Only ocean currents', 'A concept unrelated to earth science', 'Volcanic eruptions'], 0),
    ('What term describes the boundary where two different air masses meet?', ['A front', 'A biome', 'A concept unrelated to weather systems', 'A watershed'], 0),
    ('Can a cold front bring sudden, intense weather changes as it passes through a region?', ['Yes', 'No, cold fronts never cause any noticeable weather changes', 'A concept unrelated to weather systems', 'Weather is never affected by the movement of air masses'], 0),
    ('Why might a warm front typically bring more gradual weather changes compared to a fast-moving cold front?', ['Warm air tends to rise slowly over the retreating cooler air, producing a more gradual transition', 'Warm fronts never produce any noticeable difference from cold fronts', 'This concept has no connection to earth science', 'All fronts move and behave in exactly the same way'], 0),
    ('Why is tracking the movement of air masses and fronts important for weather forecasting?', ['Understanding how air masses interact helps predict upcoming changes in temperature, precipitation, and storms', 'Air masses and fronts have no connection to predicting future weather', 'This concept has no relevance to earth science', 'Weather forecasting never relies on tracking any atmospheric patterns'], 0)]),
H('Canada’s Role in the League of Nations',
  'Grade 10 History strand: Canada joined the League of Nations after the First World War as a founding member with its own seat, marking an early step toward greater independence in Canadian foreign policy.',
  [('What international organization did Canada join as a founding member after the First World War?', ['The League of Nations', 'A concept unrelated to Canadian history', 'An organization with no connection to postwar diplomacy', 'The Commonwealth of Nations, founded at the same time'], 0),
   ('Did Canada have its own seat in the League of Nations, separate from Britain?', ['Yes', 'No, Canada was never granted its own seat', 'A concept unrelated to the League of Nations', 'Only Britain was permitted to represent Canada at the League'], 0),
   ('Is Canada’s membership in the League of Nations often seen as an early step toward greater independence in foreign policy?', ['Yes', 'No, it had no connection to Canadian independence in foreign affairs', 'A concept unrelated to Canadian history', 'Canadian foreign policy remained entirely controlled by Britain regardless of this membership'], 0),
   ('Why might having its own seat in the League of Nations have been significant for Canada’s international status?', ['It signalled growing recognition of Canada as a distinct international actor, separate from Britain', 'Having a separate seat had no effect on how Canada was viewed internationally', 'This concept has no relevance to Canadian history', 'Canada’s international status remained completely unchanged by this membership'], 0),
   ('Why is Canada’s early involvement in the League of Nations often studied alongside its later role in founding the United Nations?', ['It shows a continuing pattern of Canadian engagement in international cooperation and diplomacy across the twentieth century', 'Canada’s involvement in the League of Nations has no connection to its later role in the United Nations', 'This concept has no relevance to history', 'Canada played no role at all in founding the United Nations'], 0)]),
]),

day(100, [
E('Review: Satire, Style, and Narrative Craft (Days 91-99)',
  'Grade 10 English strand review: students revisit satire and parody, the elegy, conditional sentences, the road novel, ceremonial speeches, multiple narrators, historical fiction, the subjunctive mood, and eco-fiction.',
  [('What literary technique uses humour, irony, or exaggeration to criticize society?', ['Satire', 'A concept unrelated to literature', 'A strictly factual news report', 'A blank page'], 0),
   ('What type of writing mourns or honours someone who has died?', ['An elegy', 'A concept unrelated to writing', 'A weather report', 'A grocery list'], 0),
   ('What kind of sentence uses an if-clause to express a hypothetical situation?', ['A conditional sentence', 'A concept unrelated to grammar', 'A sentence with no verb at all', 'A single-word sentence'], 0),
   ('What genre of fiction follows a physical journey that often parallels internal growth?', ['The road novel', 'A concept unrelated to literature', 'A cookbook', 'A phone directory'], 0),
   ('What grammatical mood expresses wishes or hypothetical situations, as in if I were?', ['The subjunctive mood', 'A concept unrelated to grammar', 'The indicative mood only', 'No mood exists in English grammar'], 0)]),
M('Review: Matrices, Trigonometry, Series, and Functions (Days 91-99)',
  'Grade 10 Math strand review: students revisit matrix determinants, double-angle trig identities, geometric series, correlation versus causation, probability trees, function composition, similar triangles, exponential/logarithmic equations, and mortgages.',
  [('For a 2x2 matrix with entries a, b, c, d, how is the determinant calculated?', ['ad minus bc', 'a plus d', 'A concept unrelated to matrices', 'Always exactly one'], 0),
   ('What is the double-angle identity for sine?', ['sin(2x) = 2 sin(x) cos(x)', 'sin(2x) = sin(x) + cos(x)', 'A concept unrelated to trigonometry', 'sin(2x) = cos(x) squared'], 0),
   ('Does correlation alone prove that one variable causes another to change?', ['No', 'Yes, correlation always proves causation', 'A concept unrelated to statistics', 'Causation can never be studied at all'], 0),
   ('In the composition f(g(x)), which function is evaluated first?', ['g(x)', 'f(x)', 'A concept unrelated to function composition', 'Neither function is evaluated'], 0),
   ('What is true of the corresponding sides in similar triangles?', ['They are proportional', 'They are always exactly equal', 'A concept unrelated to geometry', 'They have no relationship to each other'], 0)]),
Sc('Review: Chemistry, Biology, Physics, and Earth Science (Days 91-99)',
   'Grade 10 Science strand review: students revisit reaction types, the digestive system, the photoelectric effect, the carbon cycle, world biomes, electric power, the ideal gas law, protein synthesis, and weather systems.',
   [('Name one type of chemical reaction, such as synthesis.', ['Synthesis', 'A concept unrelated to chemistry', 'Photosynthesis only', 'Osmosis'], 0),
    ('What does the digestive system break food down into?', ['Nutrients', 'Only heat energy', 'A concept unrelated to biology', 'Solid bone tissue'], 0),
    ('What happens during the photoelectric effect?', ['Light striking a metal surface ejects electrons', 'A metal surface absorbs sound waves', 'A concept unrelated to physics', 'A magnet attracts a piece of metal'], 0),
    ('What are the two main stages of protein synthesis?', ['Transcription and translation', 'Digestion and absorption', 'A concept unrelated to biology', 'Mitosis and meiosis'], 0),
    ('What term describes the boundary where two different air masses meet?', ['A front', 'A biome', 'A concept unrelated to weather systems', 'A watershed'], 0)]),
H('Review: Confederation-Era to Interwar Canadian History (Days 91-99)',
  'Grade 10 History strand review: students revisit the Riel Rebellions, the National Policy, the Klondike Gold Rush, the Underground Railroad in Canada, the Fenian Raids, the Boer War, the Regina Manifesto and CCF, the Pacific Scandal, and the League of Nations.',
  [('Who led the Métis resistance movements in 1869-70 and 1885?', ['Louis Riel', 'A concept unrelated to Canadian history', 'A figure with no connection to the Métis', 'A British colonial governor'], 0),
   ('What economic policy did Sir John A. Macdonald introduce in 1879?', ['The National Policy', 'A concept unrelated to Canadian history', 'A policy with no connection to the economy', 'A free trade agreement with France'], 0),
   ('What discovery drew tens of thousands of prospectors to the Yukon in the 1890s?', ['Gold', 'A concept unrelated to the Klondike Gold Rush', 'Oil', 'Coal'], 0),
   ('What political movement was outlined in the 1933 Regina Manifesto?', ['The Co-operative Commonwealth Federation (CCF)', 'A concept unrelated to Canadian history', 'A movement with no connection to Canadian politics', 'A regional business association'], 0),
   ('What international organization did Canada join as a founding member after the First World War?', ['The League of Nations', 'A concept unrelated to Canadian history', 'An organization with no connection to postwar diplomacy', 'The Commonwealth of Nations'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g10_91_100)
    append_to(10, g10_91_100)
