#!/usr/bin/env python3
"""Grade 8, Days 121-130 -- extends Grade 8 from 120 to 130 days. Topics
chosen after dumping the existing Day 1-120 title list (data/grade8.json)
in full to avoid any overlap: apostrophes and possessive forms, archaisms
and obsolete words, foils and antagonists, public service announcement
scripts, infographics and data visualization, allusion in literature,
interjections and direct address, malapropisms, and persuasion using
ethos, pathos, and logos; the correlation coefficient, perfect/deficient/
abundant numbers, radian measure, an introduction to derivatives, an
introduction to hypothesis testing, Cramers Rule, the Chinese Remainder
Theorem, conic sections, and fractals/self-similarity; the skeletal
system, the chemistry of soap and surfactants, bioluminescence, the
physics of magnetism, the respiratory system, invasive species, acid-base
titration, earthquake-resistant engineering, and the physics of sound
insulation; the fur trade and the voyageurs, the Charlottetown and Quebec
Conferences of 1864, the Pacific Scandal of 1873, the Cypress Hills
Massacre and the North-West Mounted Police, the Numbered Treaties, the
Canadian National Railway, the formation of the RCMP in 1920, the
Trans-Canada Highway, and the Rebellion Losses Bill. Day 130 is a review
day across all four subjects.

Subject keys for Grade 8 are "Language", "Math", "Science", "History"
(same as all earlier Grade 8 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII apostrophe or double-quote characters are used
anywhere in title/question/summary/option text; apostrophes are dropped
entirely, matching the convention used in gen_grade8_days111_120.py.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from gen_curriculum import sub, day, append_to

L8 = 'https://tvolearn.com/pages/grade-8-language'
M8 = 'https://tvolearn.com/pages/grade-8-mathematics'
S8 = 'https://tvolearn.com/pages/grade-8-science-and-technology'
H8 = 'https://tvolearn.com/pages/grade-8-history'
RL, RM, RS, RH = (
    'TVO Learn: Grade 8 Language',
    'TVO Learn: Grade 8 Mathematics',
    'TVO Learn: Grade 8 Science and Technology',
    'TVO Learn: Grade 8 History',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L8, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M8, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S8, q)


def H(t, s, q):
    return sub('History', t, s, RH, H8, q)


def _rebalance_answer_positions(days, seed=20260730):
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


g8_121_130 = [
day(121, [
L('Grammar: Apostrophes and Possessive Forms',
  'Grade 8 Language strand: apostrophes indicate possession or mark a contraction, with singular nouns typically adding an apostrophe and an s while plural nouns already ending in s add only an apostrophe.',
  [('What is the purpose of an apostrophe in a possessive noun?', ['To show ownership or a relationship between two nouns', 'To end a question', 'To join two independent clauses', 'To indicate plural number'], 0),
   ('How is a possessive typically formed for a singular noun such as the word cat?', ['Add an apostrophe followed by the letter s', 'Add only an s with no apostrophe', 'Add an apostrophe after a final s', 'Remove the final letter entirely'], 0),
   ('How is a possessive typically formed for a plural noun already ending in s, such as the word students?', ['Add only an apostrophe after the final s', 'Add an apostrophe followed by another s', 'Remove the apostrophe entirely', 'Add an s with no apostrophe'], 0),
   ('What is a common error when forming the possessive of the pronoun it?', ['Confusing the possessive form its with the contraction meaning it is', 'Using no punctuation at all', 'Capitalizing the word unnecessarily', 'Adding an extra syllable'], 0),
   ('Why is correct apostrophe placement important in formal writing?', ['Incorrect placement can confuse a reader about whether a word is plural, possessive, or a contraction', 'Apostrophes never affect the meaning of a sentence', 'Formal writing never uses possessive nouns', 'Apostrophes are always optional in every context'], 0)]),
M('Statistics: The Correlation Coefficient (r) and Strength of Relationships',
  'Grade 8 Math strand: the correlation coefficient, represented by r, is a value between negative one and positive one that measures both the strength and direction of a linear relationship between two variables.',
  [('What range of values can the correlation coefficient r take?', ['Between negative one and positive one', 'Between zero and one hundred', 'Any whole number', 'Only positive integers'], 0),
   ('What does a correlation coefficient close to positive one indicate?', ['A strong positive linear relationship between two variables', 'No relationship at all between the variables', 'A strong negative relationship', 'An undefined relationship'], 0),
   ('What does a correlation coefficient close to zero suggest?', ['Little to no linear relationship between the two variables', 'A perfect positive relationship', 'A perfect negative relationship', 'An impossible result'], 0),
   ('If r equals negative point nine, what does this suggest about the relationship between the variables?', ['A strong negative linear relationship', 'A strong positive linear relationship', 'No relationship whatsoever', 'An undefined value'], 0),
   ('Why is the correlation coefficient useful when analyzing a scatter plot?', ['It gives a precise numerical measure of how closely the data points follow a linear pattern', 'It has no connection to scatter plots', 'It always describes causation rather than correlation', 'It can only be calculated for categorical data'], 0)]),
Sc('The Skeletal System: Bones, Joints, and Movement',
   'Grade 8 Science strand: the skeletal system provides structural support for the body, protects internal organs, and works with joints and muscles to enable a wide range of movement.',
   [('What is one major function of the skeletal system?', ['Providing structural support and protecting internal organs', 'Digesting food in the stomach', 'Pumping blood through the body', 'Producing sound for speech'], 0),
    ('What role do joints play in the skeletal system?', ['They connect bones and allow different types of movement', 'They produce new blood cells exclusively', 'They filter waste from the blood', 'They have no connection to movement'], 0),
    ('Which organs are protected by the rib cage?', ['The heart and lungs', 'The stomach only', 'The kidneys only', 'The skin'], 0),
    ('How do bones and muscles work together to create movement?', ['Muscles contract and pull on bones connected at joints', 'Bones move entirely independently of muscles', 'Muscles have no connection to the skeletal system', 'Joints prevent all movement between bones'], 0),
    ('Why is bone density important for overall skeletal health?', ['Higher bone density generally means stronger, more fracture-resistant bones', 'Bone density has no effect on the strength of a bone', 'Bones with low density are always stronger', 'Bone density only affects the colour of a bone'], 0)]),
H('The Fur Trade and the Voyageurs',
  'Grade 8 History strand: the fur trade was a foundational economic activity in early Canada, driven by the demand for beaver pelts in Europe and carried out largely by voyageurs, skilled canoe travelers who transported furs and supplies across vast wilderness trade routes.',
  [('What resource primarily drove the early Canadian fur trade?', ['Beaver pelts', 'Gold deposits', 'Cod fisheries', 'Timber exports'], 0),
   ('Who were the voyageurs?', ['Skilled canoe travelers who transported furs and supplies', 'Government officials who regulated trade prices', 'Soldiers stationed at coastal forts', 'Teachers in early colonial schools'], 0),
   ('Why was the fur trade considered economically important to early Canada?', ['It generated significant wealth and shaped trade relationships across the continent', 'It had no significant economic impact on the colonies', 'Fur was never in demand in Europe', 'The fur trade only operated for a single year'], 0),
   ('Which group played an essential role in guiding and supporting the fur trade through their knowledge of the land?', ['Indigenous peoples', 'European monarchs', 'Distant colonial governors with no local knowledge', 'Only workers with no connection to the land'], 0),
   ('Why is the fur trade considered a foundation for Canadas early economic development?', ['It established trade routes and partnerships that shaped later settlement and commerce', 'The fur trade had no lasting influence on Canadas development', 'It occurred long after Canada was already fully settled', 'Fur trading routes never connected different regions of the country'], 0)]),
]),
day(122, [
L('Vocabulary: Archaisms and Obsolete Words',
  'Grade 8 Language strand: an archaism is a word or phrase that was once common but has fallen out of everyday use, often appearing in older literature, religious texts, or works striving for a formal or historical tone.',
  [('What is an archaism?', ['A word or phrase that was once common but is no longer used in everyday language', 'A newly invented word describing modern technology', 'A grammatical rule about verb tense', 'A citation format used in essays'], 0),
   ('Which word is an example of an archaism?', ['Thou, meaning you', 'Selfie', 'Internet', 'Podcast'], 0),
   ('Where might a reader most commonly encounter archaisms today?', ['In older literature, religious texts, or works imitating a historical style', 'In modern text messages', 'In scientific lab reports', 'In social media captions'], 0),
   ('Why might a contemporary author deliberately use archaisms in a story?', ['To create a sense of history, formality, or a particular time period', 'Archaisms always make writing easier for modern readers to understand', 'Archaisms are required in every piece of formal writing', 'Archaisms have no stylistic effect on a text'], 0),
   ('Why is it useful for readers to recognize archaisms when studying older texts?', ['Recognizing them helps readers understand meanings that have shifted or disappeared from modern usage', 'Archaisms are always identical in meaning to their modern equivalents', 'Older texts never contain any archaic language', 'Archaisms make a text impossible to interpret in any way'], 0)]),
M('Number Theory: Perfect, Deficient, and Abundant Numbers',
  'Grade 8 Math strand: a perfect number equals the sum of its proper divisors, a deficient number has a divisor sum less than itself, and an abundant number has a divisor sum greater than itself, classifications that reveal patterns within number theory.',
  [('What defines a perfect number?', ['It equals the sum of its proper divisors', 'It has no divisors other than one', 'It is always an odd number', 'It is always a prime number'], 0),
   ('What are the proper divisors of the number 6?', ['1, 2, and 3', '1 and 6', '2 and 3 only', '6 only'], 0),
   ('Why is 6 considered a perfect number?', ['Its proper divisors, 1, 2, and 3, sum to exactly 6', 'Its proper divisors sum to a number greater than 6', 'Its proper divisors sum to a number less than 6', 'It has no proper divisors at all'], 0),
   ('What is a deficient number?', ['A number whose proper divisors sum to less than the number itself', 'A number whose proper divisors sum to more than the number itself', 'A number with no divisors at all', 'A number that is always prime'], 0),
   ('What is an abundant number?', ['A number whose proper divisors sum to more than the number itself', 'A number whose proper divisors sum to exactly the number itself', 'A number whose proper divisors sum to less than the number itself', 'A number with only one divisor'], 0)]),
Sc('The Chemistry of Soap and Surfactants',
   'Grade 8 Science strand: soap molecules act as surfactants, having one end that attracts water and one end that attracts grease and oil, allowing soap to lift dirt away from a surface and suspend it in water for rinsing.',
   [('What is a surfactant?', ['A substance with one end that attracts water and one end that attracts oil or grease', 'A substance that only ever repels water', 'A type of enzyme found in the digestive system', 'A gas released during combustion'], 0),
    ('How does soap help remove grease from a surface?', ['Its oil-attracting end binds to grease while its water-attracting end allows it to rinse away', 'Soap only ever repels both water and oil equally', 'Soap has no chemical interaction with grease at all', 'Soap dissolves grease by freezing it'], 0),
    ('What term describes the water-attracting end of a soap molecule?', ['Hydrophilic', 'Hydrophobic', 'Photosynthetic', 'Radioactive'], 0),
    ('What term describes the oil-attracting end of a soap molecule?', ['Hydrophobic', 'Hydrophilic', 'Magnetic', 'Conductive'], 0),
    ('Why is soap more effective at cleaning than water alone?', ['Soap can bind to grease and oil, which water alone cannot dissolve effectively', 'Water alone always removes grease more effectively than soap', 'Soap has no chemical properties different from water', 'Grease dissolves instantly in water without any assistance'], 0)]),
H('The Charlottetown and Quebec Conferences of 1864',
  'Grade 8 History strand: the Charlottetown and Quebec Conferences of 1864 brought together colonial leaders to discuss uniting British North America, laying the groundwork for the specific terms and structure that would shape Confederation in 1867.',
  [('What was the main purpose of the Charlottetown Conference of 1864?', ['To discuss uniting British North American colonies', 'To negotiate a peace treaty ending a war', 'To establish a new national anthem', 'To settle a border dispute with the United States'], 0),
   ('What followed the Charlottetown Conference later in 1864?', ['The Quebec Conference, which developed more detailed terms for union', 'An immediate declaration of full independence', 'The signing of the Treaty of Versailles', 'The creation of the Canadian Pacific Railway'], 0),
   ('What eventually resulted from the discussions held at these two conferences?', ['The foundation for Confederation in 1867', 'The permanent division of the colonies', 'A rejection of any future union', 'The annexation of the colonies by the United States'], 0),
   ('Why were multiple conferences needed before Confederation could be finalized?', ['Leaders needed to negotiate details such as representation, powers, and structure among the colonies', 'A single meeting was always sufficient with no further discussion needed', 'The colonies agreed on every detail immediately', 'Conferences had no connection to the eventual union'], 0),
   ('Why are the Charlottetown and Quebec Conferences considered foundational events in Canadian history?', ['They established the framework of ideas and agreements that shaped the eventual Confederation of Canada', 'These conferences had no lasting significance for Canada', 'They resulted in colonies permanently remaining separate', 'They occurred after Confederation had already taken place'], 0)]),
]),
day(123, [
L('Reading: Analyzing Foils and Antagonists',
  'Grade 8 Language strand: a foil is a character whose traits contrast with those of another character, often the protagonist, to highlight specific qualities, while an antagonist is a character or force that directly opposes the protagonist and drives conflict.',
  [('What is a foil in literature?', ['A character whose contrasting traits highlight qualities in another character', 'A character who narrates the entire story', 'A type of punctuation mark', 'A citation style used in essays'], 0),
   ('What is an antagonist?', ['A character or force that directly opposes the protagonist', 'The main character around whom the story centers', 'A minor character with no effect on the plot', 'A type of setting description'], 0),
   ('Can a character serve as both a foil and an antagonist in the same story?', ['Yes, a character can highlight contrasting traits while also opposing the protagonist', 'No, these two roles can never overlap in any story', 'A concept unrelated to characterization', 'Only narrators can serve either role'], 0),
   ('Why might an author create a foil for the protagonist?', ['To emphasize particular strengths or weaknesses in the protagonist through comparison', 'Foils never add any meaning to a story', 'This concept has no connection to reading comprehension', 'A foil always shares identical traits with the protagonist'], 0),
   ('Why is identifying the antagonist important when analyzing a storys central conflict?', ['The antagonist often represents the primary source of tension the protagonist must overcome', 'Every story lacks any antagonist or opposing force', 'This concept has no relevance to reading', 'The antagonist and protagonist always want the same outcome'], 0)]),
M('Geometry: Introduction to Radian Measure',
  'Grade 8 Math strand: a radian is a unit for measuring angles based on the radius of a circle, defined so that an angle of one radian corresponds to an arc length equal to the circles radius, with a full circle measuring two pi radians.',
  [('How is one radian defined?', ['The angle formed when the arc length equals the circles radius', 'The angle formed by exactly one degree', 'An angle that always equals ninety degrees', 'An angle with no defined arc length'], 0),
   ('How many radians are in a full circle?', ['Two pi radians', 'Ninety radians', 'One radian', 'Three hundred sixty radians'], 0),
   ('How many degrees are approximately equal to one radian?', ['About 57.3 degrees', 'Exactly 1 degree', 'Exactly 90 degrees', 'Exactly 180 degrees'], 0),
   ('Why might radians be preferred over degrees in advanced mathematics, such as calculus?', ['Radians connect angle measure directly to arc length and simplify many formulas', 'Radians never simplify any mathematical formulas', 'Degrees are always the only unit used in higher mathematics', 'Radians cannot be used to measure any angle larger than one full circle'], 0),
   ('How many radians correspond to a straight angle of 180 degrees?', ['Pi radians', 'Two pi radians', 'Half of pi radians', 'Zero radians'], 0)]),
Sc('Bioluminescence: Living Light in Nature',
   'Grade 8 Science strand: bioluminescence is the production of light by living organisms through a chemical reaction, typically involving a light-emitting molecule called luciferin and an enzyme called luciferase, and is used by many deep-sea creatures for communication, hunting, or defense.',
   [('What is bioluminescence?', ['The production of light by living organisms through a chemical reaction', 'The absorption of light by plants during photosynthesis', 'A type of radioactive decay', 'A reflection of sunlight off an animals skin'], 0),
    ('What molecule commonly reacts with an enzyme to produce bioluminescent light?', ['Luciferin', 'Chlorophyll', 'Hemoglobin', 'Glucose'], 0),
    ('What enzyme is typically involved in triggering the bioluminescent reaction?', ['Luciferase', 'Amylase', 'Catalase', 'Pepsin'], 0),
    ('Why might a deep-sea creature use bioluminescence for hunting?', ['Producing light can lure prey closer or help the creature see in a dark environment', 'Bioluminescence never has any use for finding food', 'Deep-sea creatures never produce their own light', 'Light production always warns prey away instead of attracting it'], 0),
    ('Why is bioluminescence especially common among organisms living in the deep ocean?', ['Little to no sunlight reaches those depths, so organisms rely on their own light for survival functions', 'Sunlight is extremely bright at those depths, making extra light unnecessary', 'Bioluminescence only occurs in organisms that live on land', 'Deep-sea organisms never need to communicate or hunt'], 0)]),
H('The Pacific Scandal of 1873',
  'Grade 8 History strand: the Pacific Scandal of 1873 was a political corruption controversy in which Prime Minister John A. Macdonalds government was accused of accepting campaign funds in exchange for awarding the Canadian Pacific Railway contract, ultimately forcing his resignation.',
  [('What was the Pacific Scandal of 1873 primarily about?', ['Accusations that the government accepted campaign funds in exchange for a railway contract', 'A dispute over international fishing rights', 'A disagreement about provincial school funding', 'An argument over a proposed national anthem'], 0),
   ('Which railway contract was at the center of the Pacific Scandal?', ['The Canadian Pacific Railway contract', 'The St. Lawrence Seaway contract', 'The Trans-Canada Highway contract', 'The Canadian National Railway contract'], 0),
   ('What was the political outcome for Prime Minister John A. Macdonald following the scandal?', ['His government was forced to resign', 'He was immediately re-elected with no consequences', 'He was declared innocent with no political impact', 'He received an even larger majority government'], 0),
   ('Why did the Pacific Scandal damage public trust in the government?', ['It suggested that a major infrastructure contract was awarded based on corrupt financial dealings rather than merit', 'The public was never made aware of the scandal', 'The scandal had no connection to government contracts', 'Trust in government was completely unaffected by the accusations'], 0),
   ('Why is the Pacific Scandal significant in the history of Canadian political accountability?', ['It illustrated the risks of corruption in awarding major public contracts and highlighted a need for political accountability', 'The scandal had no lasting effect on how Canadians viewed their government', 'It resulted in the immediate cancellation of the railway project', 'Political corruption was never considered an issue after this event'], 0)]),
]),
day(124, [
L('Writing: Writing a Public Service Announcement Script',
  'Grade 8 Language strand: a public service announcement, or PSA, is a short piece of persuasive media designed to raise awareness about an important issue and motivate an audience to take a specific action, typically combining a clear message with a memorable call to action.',
  [('What is the main purpose of a public service announcement?', ['To raise awareness about an issue and motivate an audience to act', 'To sell a specific commercial product', 'To entertain with a fictional story only', 'To report daily weather conditions'], 0),
   ('What is a call to action in a PSA?', ['A clear statement urging the audience to take a specific step', 'A section listing unrelated statistics', 'A formal citation of sources', 'A description of the setting only'], 0),
   ('Why do PSAs typically use a concise, focused message?', ['Audiences are more likely to remember and act on a short, clear message', 'Long, unfocused messages always persuade audiences more effectively', 'PSAs are never meant to be remembered', 'Conciseness has no effect on persuasive writing'], 0),
   ('Which topic would be well suited to a public service announcement?', ['Encouraging people to conserve water during a drought', 'A detailed technical manual for repairing an engine', 'A private diary entry with no audience', 'A purely fictional story about dragons'], 0),
   ('Why might a PSA combine factual information with an emotional appeal?', ['Facts build credibility while emotion helps motivate the audience to care and act', 'Emotional appeals are never appropriate in persuasive writing', 'PSAs should never include any factual information', 'Combining facts and emotion always confuses an audience'], 0)]),
M('Calculus Preview: An Introduction to Derivatives and Rates of Change',
  'Grade 8 Math strand: a derivative measures the instantaneous rate of change of a function at a given point, building on the concept of a limit to describe how steeply a function is increasing or decreasing.',
  [('What does a derivative measure?', ['The instantaneous rate of change of a function at a given point', 'The total area under a curve', 'A fixed value that never changes', 'The average of a data set'], 0),
   ('What earlier mathematical concept does the derivative build upon?', ['The limit', 'The Pythagorean theorem', 'Set notation', 'Matrix multiplication'], 0),
   ('If a functions derivative is positive at a point, what does this indicate?', ['The function is increasing at that point', 'The function is decreasing at that point', 'The function has no value at that point', 'The function is undefined everywhere'], 0),
   ('What does a derivative of zero at a point often indicate about a functions graph?', ['A possible maximum, minimum, or flat point on the graph', 'The function is increasing rapidly', 'The function is undefined at every point', 'The function has no graph at all'], 0),
   ('Why are derivatives useful in fields such as physics?', ['They can describe quantities like velocity, which is the rate of change of position over time', 'Derivatives have no real-world applications', 'Physics never involves any rates of change', 'Velocity can never be described using calculus'], 0)]),
Sc('The Physics of Magnetism and Magnetic Fields',
   'Grade 8 Science strand: magnetism is a force produced by moving electric charges that causes certain materials to attract or repel one another, with a magnetic field describing the region of space around a magnet where this force can be detected.',
   [('What produces a magnetic force?', ['Moving electric charges', 'Only stationary electric charges', 'Only sound waves', 'Only visible light'], 0),
    ('What is a magnetic field?', ['The region of space around a magnet where its force can be detected', 'A solid material with no measurable properties', 'A type of chemical reaction', 'A unit used only to measure temperature'], 0),
    ('What happens when two like magnetic poles, such as two north poles, are brought close together?', ['They repel each other', 'They always attract each other', 'They cancel out and produce no force', 'They instantly become non-magnetic'], 0),
    ('What happens when two opposite magnetic poles are brought close together?', ['They attract each other', 'They always repel each other', 'They produce no force at all', 'They combine into a single pole with no properties'], 0),
    ('Why are electromagnets useful in devices like electric motors?', ['Their magnetic strength can be controlled by adjusting the electric current flowing through them', 'Electromagnets always have a fixed, unchangeable strength', 'Electromagnets have no practical applications in technology', 'Electric current has no connection to magnetism'], 0)]),
H('The Cypress Hills Massacre and the Creation of the North-West Mounted Police',
  'Grade 8 History strand: the Cypress Hills Massacre of 1873, in which American traders killed a group of Assiniboine people, alarmed the Canadian government and helped prompt the creation of the North-West Mounted Police to establish law and order in the western territories.',
  [('What happened during the Cypress Hills Massacre of 1873?', ['American traders killed a group of Assiniboine people', 'A large peaceful trade agreement was signed', 'A railway was completed ahead of schedule', 'A new provincial government was formed'], 0),
   ('What Canadian government response followed the Cypress Hills Massacre?', ['The creation of the North-West Mounted Police', 'The immediate independence of the western territories', 'The cancellation of all westward settlement', 'The signing of a treaty with the United States'], 0),
   ('What was one main purpose of the newly formed North-West Mounted Police?', ['To establish law and order in the western territories', 'To operate solely as a postal delivery service', 'To manage international trade agreements', 'To build railways across the prairies'], 0),
   ('Why did the Cypress Hills Massacre alarm the Canadian government?', ['It highlighted the lack of law enforcement and government authority in the western territories', 'The government had no interest in events occurring in the west', 'The massacre had no connection to future government policy', 'Canada had no territorial claims in the region at the time'], 0),
   ('Why is the Cypress Hills Massacre considered a turning point in the governance of western Canada?', ['It directly contributed to the establishment of a formal policing presence in the territories', 'The massacre had no influence on how the west was governed', 'Law enforcement in the west was already fully established before this event', 'The event led to the west being abandoned by the government entirely'], 0)]),
]),
day(125, [
L('Media Literacy: Analyzing Infographics and Data Visualization',
  'Grade 8 Language strand: an infographic combines images, charts, and concise text to present information or data visually, and analyzing one critically involves checking whether the visual choices accurately represent the underlying data or distort it for effect.',
  [('What is an infographic?', ['A visual combining images, charts, and concise text to present information', 'A lengthy academic essay with no visuals', 'A type of punctuation mark', 'A purely fictional narrative'], 0),
   ('Why might a critical reader examine the scale of a chart within an infographic?', ['A distorted scale can exaggerate or minimize differences in the data', 'Scale never has any effect on how data appears', 'Infographics never contain any charts', 'Charts are always presented with perfectly accurate scales'], 0),
   ('What is one risk of poorly designed data visualization?', ['It can mislead viewers about the true relationships within the data', 'Poorly designed visuals always communicate data more clearly', 'Data visualization never influences a viewers understanding', 'Infographics have no connection to persuasion'], 0),
   ('Why do infographics often use colour and icons strategically?', ['To draw attention to key information and make complex data easier to understand quickly', 'Colour and icons never affect how a viewer interprets information', 'Infographics are required to be entirely black and white', 'Icons always replace the need for any data at all'], 0),
   ('Why is it important to check the original source of the data behind an infographic?', ['Verifying the source helps confirm whether the information is accurate and unbiased', 'The original source of data is never relevant to its accuracy', 'Infographics never rely on any outside data', 'Sources are only necessary for written essays, not visuals'], 0)]),
M('Statistics: An Introduction to Hypothesis Testing',
  'Grade 8 Math strand: hypothesis testing is a statistical method for deciding whether there is enough evidence in a sample of data to support a specific claim about a larger population, typically comparing a null hypothesis against an alternative hypothesis.',
  [('What is the purpose of hypothesis testing?', ['To decide whether sample evidence supports a specific claim about a population', 'To calculate the exact value of every individual data point', 'To replace the need for collecting any data', 'To draw a Venn diagram of overlapping sets'], 0),
   ('What is a null hypothesis?', ['A statement assuming no effect or no difference exists', 'A statement that is always assumed to be true with no testing', 'A type of geometric proof', 'A rule for graphing quadratic functions'], 0),
   ('What is an alternative hypothesis?', ['A statement proposing that an effect or difference does exist', 'A statement identical to the null hypothesis', 'A rule about triangle congruence', 'A method for simplifying fractions'], 0),
   ('Why do researchers rely on a sample rather than testing an entire population?', ['Testing an entire population is often impractical, so a representative sample is used to draw conclusions', 'Samples are always identical to the entire population in every way', 'Populations never need to be studied using statistics', 'Sampling always produces completely certain, error-free conclusions'], 0),
   ('Why is hypothesis testing widely used in scientific research?', ['It provides a structured method for evaluating whether observed results are likely due to chance or reflect a real effect', 'Hypothesis testing has no connection to scientific research', 'Scientific claims never require any statistical evidence', 'Hypothesis testing eliminates the need for any data collection'], 0)]),
Sc('The Human Respiratory System: Gas Exchange and Breathing',
   'Grade 8 Science strand: the respiratory system moves air into and out of the lungs, where oxygen is exchanged for carbon dioxide across tiny air sacs called alveoli, supplying the bloodstream with the oxygen needed for cellular respiration.',
   [('Where does gas exchange occur in the lungs?', ['In tiny air sacs called alveoli', 'In the trachea only', 'In the diaphragm only', 'In the nasal passages only'], 0),
    ('What gas does the respiratory system supply to the bloodstream?', ['Oxygen', 'Nitrogen', 'Carbon dioxide only', 'Helium'], 0),
    ('What waste gas is removed from the blood and exhaled by the lungs?', ['Carbon dioxide', 'Oxygen', 'Hydrogen', 'Nitrogen'], 0),
    ('Why do alveoli have very thin walls and a large surface area?', ['These features allow oxygen and carbon dioxide to be exchanged efficiently with the blood', 'Thin walls prevent any gas exchange from occurring', 'Alveoli are designed to store air permanently with no exchange', 'A large surface area has no effect on gas exchange'], 0),
    ('How is breathing connected to cellular respiration?', ['Breathing supplies the oxygen cells need to release energy through cellular respiration', 'Breathing and cellular respiration are completely unrelated processes', 'Cellular respiration produces the oxygen used for breathing', 'Cells never require any oxygen supplied by breathing'], 0)]),
H('The Numbered Treaties and Indigenous-Crown Relations',
  'Grade 8 History strand: the Numbered Treaties were a series of agreements signed between the Canadian government and Indigenous nations between 1871 and 1921, intended to define land use, reserve boundaries, and government obligations, though their terms were often interpreted very differently by each side.',
  [('What were the Numbered Treaties?', ['A series of agreements between the Canadian government and Indigenous nations', 'A set of provincial election laws', 'A collection of railway construction contracts', 'A series of treaties between Canada and Britain only'], 0),
   ('Over roughly what period were the Numbered Treaties signed?', ['Between 1871 and 1921', 'Between 1600 and 1650', 'Between 1980 and 1990', 'Between 1812 and 1815'], 0),
   ('What were the Numbered Treaties generally intended to address?', ['Land use, reserve boundaries, and government obligations', 'International trade tariffs', 'The design of the Canadian flag', 'Naval defence policy'], 0),
   ('Why have the Numbered Treaties been a continuing source of historical and legal debate?', ['The Canadian government and Indigenous nations often interpreted the treaty terms very differently', 'Both sides always agreed completely on every treaty term', 'The treaties were never actually signed by either side', 'The treaties had no connection to land or governance'], 0),
   ('Why is the study of the Numbered Treaties important for understanding modern Indigenous-Crown relations?', ['These historical agreements continue to shape legal and political discussions about land and rights today', 'The treaties have no relevance to any modern issue', 'The treaties were fully resolved with no lasting impact', 'Indigenous nations were never involved in any treaty negotiations'], 0)]),
]),
day(126, [
L('Reading: Analyzing Allusion in Literature',
  'Grade 8 Language strand: an allusion is a brief, indirect reference to a person, event, or work from history, literature, or culture that an author expects readers to recognize, adding layers of meaning without lengthy explanation.',
  [('What is an allusion?', ['A brief, indirect reference to a person, event, or work the author expects readers to recognize', 'A detailed explanation of every historical event mentioned in a text', 'A type of punctuation mark', 'A citation style used in essays'], 0),
   ('Why do authors use allusions instead of fully explaining a reference?', ['Allusions let a writer add meaning efficiently by relying on a readers existing knowledge', 'Allusions always require lengthy explanation to be understood', 'This concept has no connection to reading', 'Authors never expect readers to recognize any outside reference'], 0),
   ('Which of these is an example of an allusion?', ['Describing someone as having the strength of Hercules', 'Describing the weather on a particular day', 'Listing the chapters of a book', 'Defining a scientific term'], 0),
   ('What might happen if a reader does not recognize an allusion in a text?', ['The reader may miss a layer of meaning the author intended to convey', 'The text automatically becomes impossible to read at all', 'Allusions have no effect on a readers understanding regardless', 'The story will change entirely for that reader'], 0),
   ('Why is recognizing allusions especially useful when reading classic or literary texts?', ['Many classic works reference mythology, history, or earlier literature to deepen their themes', 'Classic texts never include any references to outside works', 'This concept has no relevance to reading comprehension', 'Allusions only appear in modern, informal writing'], 0)]),
M('Algebra: Solving Systems of Equations Using Cramers Rule',
  'Grade 8 Math strand: Cramers Rule uses the determinants of matrices formed from a system of linear equations to solve directly for each variable, offering an alternative to substitution, elimination, or graphing.',
  [('What mathematical tool does Cramers Rule rely on to solve a system of equations?', ['Determinants of matrices', 'Only graphing techniques', 'Only the quadratic formula', 'Only sigma notation'], 0),
   ('What alternative methods can also be used to solve a system of linear equations?', ['Substitution, elimination, and graphing', 'Only counting on fingers', 'Only measuring angles', 'Only calculating probability'], 0),
   ('For Cramers Rule to give a unique solution, what must be true about the main determinant of the system?', ['It must not equal zero', 'It must always equal zero', 'It must always be negative', 'It must always be an even number'], 0),
   ('Why might Cramers Rule be considered useful for larger systems of equations compared to substitution?', ['It provides a direct, systematic formula for finding each variable without repeated substitution steps', 'Cramers Rule never actually helps solve any system of equations', 'Substitution is always faster for every possible system', 'Cramers Rule can only ever be used for a single equation'], 0),
   ('What happens if the determinant used in Cramers Rule equals zero?', ['The system does not have a single unique solution', 'The system always has exactly one solution', 'The equations become impossible to write down', 'The variables automatically equal zero'], 0)]),
Sc('Invasive Species and Ecosystem Disruption',
   'Grade 8 Science strand: an invasive species is a non-native organism introduced to a new environment where it spreads rapidly and causes ecological or economic harm, often by outcompeting native species for resources or introducing new diseases.',
   [('What is an invasive species?', ['A non-native organism that spreads rapidly and causes ecological harm in a new environment', 'A native species that has always lived in a particular ecosystem', 'A species that has gone extinct', 'A species found only in a laboratory setting'], 0),
    ('How might an invasive species harm native populations?', ['By outcompeting native species for food, space, or other resources', 'By always cooperating peacefully with every native species', 'Invasive species never interact with native populations', 'By providing unlimited resources to native species'], 0),
    ('How are invasive species often introduced to a new environment?', ['Through human activities like trade, travel, or the release of pets', 'Only through natural migration with no human involvement', 'Invasive species never actually move between environments', 'Through processes entirely unrelated to human activity'], 0),
    ('Why can invasive species sometimes spread rapidly in a new ecosystem?', ['They may lack natural predators or competitors in their new environment', 'New environments always have more predators for invasive species', 'Invasive species always spread more slowly than native species', 'Ecosystems automatically prevent any new species from spreading'], 0),
    ('Why are invasive species considered a significant economic as well as ecological concern?', ['They can damage crops, fisheries, and infrastructure, leading to costly control and prevention efforts', 'Invasive species never have any economic impact', 'Ecological harm and economic harm are always entirely unrelated', 'Governments never need to spend money addressing invasive species'], 0)]),
H('The Building of the Canadian National Railway',
  'Grade 8 History strand: the Canadian National Railway was formed in the early 1920s when the federal government consolidated several financially struggling private railway lines into a single publicly owned company, creating a second transcontinental rail system alongside the Canadian Pacific Railway.',
  [('How was the Canadian National Railway formed?', ['By consolidating several struggling private railway lines into one publicly owned company', 'By privatizing an existing government-run railway', 'By merging with a railway company in the United States', 'By constructing an entirely new railway with no prior lines involved'], 0),
   ('Roughly when was the Canadian National Railway formed?', ['In the early 1920s', 'In the 1860s', 'In the 1950s', 'In the 1990s'], 0),
   ('What other major Canadian railway did the Canadian National Railway operate alongside?', ['The Canadian Pacific Railway', 'The Trans-Canada Highway', 'The St. Lawrence Seaway', 'The Alaska Highway'], 0),
   ('Why did the government choose to consolidate the struggling railway lines rather than let them fail?', ['Maintaining reliable rail transportation was seen as vital to the countrys economy and unity', 'Railways were considered unimportant to the Canadian economy', 'The government had no interest in transportation infrastructure', 'The struggling lines had no economic value at all'], 0),
   ('Why is the creation of the Canadian National Railway considered significant in Canadian economic history?', ['It ensured continued transcontinental rail service and reflected growing government involvement in infrastructure', 'It had no lasting impact on Canadian transportation', 'It marked the end of all railway service in Canada', 'Canadian National Railway was dissolved almost immediately after forming'], 0)]),
]),
day(127, [
L('Grammar: Interjections and Direct Address',
  'Grade 8 Language strand: an interjection is a word or phrase that expresses strong emotion and is often set off by an exclamation mark or comma, while direct address names the person or group being spoken to and is typically separated from the rest of the sentence by a comma.',
  [('What does an interjection typically express?', ['Strong emotion, such as surprise or excitement', 'A grammatical rule about verb tense', 'A citation format', 'A type of question'], 0),
   ('Which word functions as an interjection in the sentence Wow, that was an incredible finish?', ['Wow', 'That', 'Was', 'Finish'], 0),
   ('What is direct address in a sentence?', ['Naming the person or group being spoken to', 'A method for citing sources', 'A type of punctuation used only in poetry', 'A word that replaces a verb'], 0),
   ('Which sentence correctly uses a comma to set off direct address?', ['Please pass the salt, Maria.', 'Please pass the salt Maria.', 'Please, pass the salt Maria.', 'Please pass, the salt Maria'], 0),
   ('Why is punctuation important when separating an interjection or direct address from the rest of a sentence?', ['It clarifies meaning and prevents the sentence from becoming confusing to read', 'Punctuation never has any effect on how a sentence is understood', 'Interjections and direct address never require any punctuation', 'These elements always attach directly to the following word with no separation'], 0)]),
M('Number Theory: An Introduction to the Chinese Remainder Theorem',
  'Grade 8 Math strand: the Chinese Remainder Theorem provides a method for solving a system of simultaneous modular congruences, finding a single number that satisfies multiple remainder conditions at once when the moduli involved share no common factors.',
  [('What does the Chinese Remainder Theorem help solve?', ['A system of simultaneous modular congruences', 'A single linear equation with one variable', 'The area of a triangle', 'The volume of a sphere'], 0),
   ('What condition must the moduli in the system typically satisfy for the theorem to guarantee a unique solution?', ['The moduli must share no common factors', 'The moduli must all be equal to each other', 'The moduli must always be negative', 'The moduli must always be prime'], 0),
   ('What kind of answer does the Chinese Remainder Theorem ultimately provide?', ['A single number that satisfies every given remainder condition simultaneously', 'A list of infinitely many unrelated answers', 'An answer that ignores all but one condition', 'A geometric shape rather than a number'], 0),
   ('In which modern field is the Chinese Remainder Theorem particularly useful?', ['Computer science and cryptography', 'Only ancient astronomy with no modern use', 'Only music theory', 'Only art history'], 0),
   ('Why is the Chinese Remainder Theorem considered an elegant result in number theory?', ['It efficiently combines multiple separate conditions into one guaranteed solution', 'It always produces zero as the only possible solution', 'It has no practical or theoretical significance', 'It only works for a single modulus at a time'], 0)]),
Sc('Acid-Base Titration and pH Indicators',
   'Grade 8 Science strand: titration is a laboratory technique used to determine the concentration of an acid or base by carefully adding a solution of known concentration until a chemical indicator signals that neutralization has occurred.',
   [('What is the purpose of an acid-base titration?', ['To determine the concentration of an unknown acid or base solution', 'To measure the temperature of a solution', 'To separate a mixture into its individual elements', 'To generate electricity from a chemical reaction'], 0),
    ('What signals that neutralization has occurred during a titration?', ['A colour change produced by a chemical indicator', 'A sudden drop in temperature', 'The solution turning solid', 'An audible sound from the container'], 0),
    ('What must be known about one of the solutions used in a titration for the calculation to work?', ['Its exact concentration', 'Its exact colour before the reaction begins', 'Its exact temperature at all times', 'Its exact mass in kilograms'], 0),
    ('Why is a chemical indicator, such as phenolphthalein, useful in a titration?', ['It changes colour at a specific pH, signalling the endpoint of the reaction', 'It permanently changes the chemical identity of the acid or base', 'Indicators have no visible effect during a titration', 'Indicators are only used to add flavour to a solution'], 0),
    ('Why is titration a valuable technique in both industry and scientific research?', ['It allows precise measurement of unknown concentrations, which is important for quality control and experimentation', 'Titration never produces any useful or precise information', 'Titration can only be used with solid substances, never liquids', 'Titration has no real-world applications outside a classroom'], 0)]),
H('The Formation of the Royal Canadian Mounted Police in 1920',
  'Grade 8 History strand: the Royal Canadian Mounted Police was formed in 1920 through the merger of the North-West Mounted Police and the Dominion Police, creating a single national police force responsible for federal law enforcement across Canada.',
  [('In what year was the Royal Canadian Mounted Police formed?', ['1920', '1867', '1873', '1949'], 0),
   ('Which two organizations merged to create the Royal Canadian Mounted Police?', ['The North-West Mounted Police and the Dominion Police', 'The Canadian Army and the Royal Canadian Navy', 'Provincial police forces from every province', 'The Canadian Pacific Railway police and a municipal force'], 0),
   ('What was the primary role of the newly formed Royal Canadian Mounted Police?', ['Federal law enforcement across Canada', 'Managing international trade negotiations', 'Operating the countrys railway system', 'Overseeing provincial school curricula'], 0),
   ('Why might the Canadian government have wanted to merge multiple police organizations into one national force?', ['A single unified force could provide more consistent law enforcement across the entire country', 'Merging police forces was expected to eliminate the need for any law enforcement', 'Multiple separate forces were considered more efficient than one national force', 'The merger had no connection to national law enforcement needs'], 0),
   ('Why is the formation of the Royal Canadian Mounted Police considered a significant milestone in Canadian institutional history?', ['It created a lasting national symbol and law enforcement body still in operation today', 'The organization was disbanded shortly after it was created', 'It had no lasting influence on Canadian institutions', 'The force never expanded beyond a single small region'], 0)]),
]),
day(128, [
L('Vocabulary: Malapropisms and Word Confusion',
  'Grade 8 Language strand: a malapropism occurs when a speaker or writer mistakenly substitutes a word for another word that sounds similar but has a very different meaning, often creating an unintentionally humorous effect.',
  [('What is a malapropism?', ['The mistaken substitution of a word for a similar-sounding word with a different meaning', 'A word borrowed directly from another language', 'A grammatical rule about sentence structure', 'A citation style used in essays'], 0),
   ('Which sentence contains a malapropism?', ['She used a diagram to illustrate the point, but he called it a dire gram.', 'She used a diagram to illustrate the point clearly.', 'He explained the process step by step.', 'They discussed the results of the experiment.'], 0),
   ('Why do malapropisms often create humour?', ['The mismatch between the intended word and the word actually used produces an unexpected meaning', 'Malapropisms always convey the exact intended meaning with no confusion', 'Humour never results from any kind of word confusion', 'Malapropisms are identical in meaning to the correct word'], 0),
   ('Why might writers use malapropisms deliberately in dialogue?', ['To develop a characters voice or create comic effect', 'Malapropisms can never be used intentionally by a writer', 'This concept has no connection to vocabulary', 'Dialogue should never include any word errors'], 0),
   ('Why is understanding malapropisms useful for improving ones own vocabulary?', ['Recognizing commonly confused words helps a writer avoid similar mistakes in their own work', 'Malapropisms have no connection to vocabulary development', 'This concept has no relevance to writing', 'Confused words are always interchangeable with no difference in meaning'], 0)]),
M('Geometry: Introduction to Conic Sections',
  'Grade 8 Math strand: conic sections are the curves formed when a plane intersects a double cone at different angles, producing circles, ellipses, parabolas, and hyperbolas depending on the angle and position of the intersecting plane.',
  [('What are conic sections?', ['Curves formed when a plane intersects a double cone', 'Curves formed only by intersecting two flat planes', 'A type of matrix operation', 'A method for simplifying fractions'], 0),
   ('Which of these is NOT one of the four basic conic sections?', ['Trapezoid', 'Circle', 'Ellipse', 'Parabola'], 0),
   ('What shape results when a plane slices straight across a cone, perpendicular to its axis?', ['A circle', 'A hyperbola', 'A straight line', 'A cube'], 0),
   ('How does a parabola form as a conic section?', ['A plane intersects the cone at an angle parallel to one side of the cone', 'A plane intersects the cone perpendicular to its axis', 'A plane never actually produces a parabola', 'A parabola is unrelated to conic sections entirely'], 0),
   ('Why are conic sections important in fields like astronomy?', ['Orbital paths of planets and comets can often be modeled using conic sections like ellipses', 'Conic sections have no application to astronomy', 'Orbits are always perfectly circular with no variation', 'Astronomy never involves geometric modeling of any kind'], 0)]),
Sc('Earthquake-Resistant Engineering and Building Design',
   'Grade 8 Science strand: earthquake-resistant engineering uses design strategies, such as flexible foundations and reinforced structural frames, to help buildings absorb and dissipate the seismic energy released during an earthquake, reducing damage and protecting occupants.',
   [('What is the main goal of earthquake-resistant engineering?', ['To help buildings absorb and dissipate seismic energy, reducing damage', 'To make buildings completely immovable during any earthquake', 'To eliminate the need for any structural design considerations', 'To prevent earthquakes from occurring at all'], 0),
    ('What is one design strategy used to make buildings more earthquake-resistant?', ['Flexible foundations that allow some movement during shaking', 'Foundations that are rigidly fixed with no flexibility whatsoever', 'Removing all structural supports from a building', 'Building exclusively with materials that shatter easily'], 0),
    ('Why might engineers reinforce a buildings structural frame in earthquake-prone regions?', ['A reinforced frame helps the building withstand shaking without collapsing', 'Reinforcement always makes a building weaker during an earthquake', 'Structural frames have no connection to a buildings earthquake safety', 'Reinforcement is only useful for buildings unaffected by earthquakes'], 0),
    ('Why do engineers study the seismic energy released during past earthquakes?', ['Understanding seismic energy helps engineers design structures that can better withstand future events', 'Past earthquakes provide no useful information for future building design', 'Seismic energy has no connection to how buildings are designed', 'Every earthquake releases exactly the same amount of energy'], 0),
    ('Why is earthquake-resistant engineering especially important in densely populated, seismically active cities?', ['Effective design can significantly reduce damage and protect large numbers of people during an earthquake', 'Earthquake-resistant engineering only matters in cities with very few people', 'Densely populated cities are never affected by earthquakes', 'Building design has no effect on the safety of a citys residents'], 0)]),
H('The Trans-Canada Highway and Postwar Infrastructure',
  'Grade 8 History strand: the Trans-Canada Highway, officially opened in 1962 after years of construction, is a transcontinental road system that connected communities across the country and reflected a broader postwar push to modernize Canadian infrastructure.',
  [('In what year was the Trans-Canada Highway officially opened?', ['1962', '1867', '1920', '1949'], 0),
   ('What does the Trans-Canada Highway connect?', ['Communities across the entire country', 'Only a single province', 'Only major international borders', 'Only coastal fishing villages'], 0),
   ('What broader trend does the construction of the Trans-Canada Highway reflect?', ['A postwar push to modernize Canadian infrastructure', 'A decision to reduce all transportation funding', 'A rejection of automobile travel in Canada', 'An effort to disconnect rural communities from cities'], 0),
   ('Why might a nationwide highway system have been considered important for Canadas economy after World War II?', ['It could improve the movement of goods, people, and services between distant regions', 'Highways were believed to have no economic benefit at the time', 'Canada already had a fully connected road network before this project', 'Economic growth was considered unrelated to transportation infrastructure'], 0),
   ('Why is the Trans-Canada Highway considered an important part of Canadian infrastructure history?', ['It represents a major national effort to physically connect a vast and geographically diverse country', 'The highway was never completed and remains unfinished today', 'It had no effect on trade or travel within Canada', 'The project was cancelled before any construction began'], 0)]),
]),
day(129, [
L('Writing: Persuasion Using Ethos, Pathos, and Logos',
  'Grade 8 Language strand: ethos, pathos, and logos are three classical persuasive appeals, with ethos establishing the writers credibility, pathos appealing to the audiences emotions, and logos relying on logic and evidence to support an argument.',
  [('What does ethos appeal to in an argument?', ['The credibility and trustworthiness of the writer or speaker', 'The audiences emotions', 'Logical evidence and reasoning', 'The setting of the argument'], 0),
   ('What does pathos appeal to?', ['The audiences emotions', 'The writers credentials', 'Statistical evidence only', 'A type of punctuation'], 0),
   ('What does logos rely on to persuade an audience?', ['Logic, facts, and evidence', 'Emotional stories only', 'The writers personal reputation only', 'Random unrelated opinions'], 0),
   ('Which of these is an example of an appeal to ethos?', ['A doctor citing years of medical experience to support a health claim', 'A story designed to make readers feel sad', 'A chart showing statistical data', 'A loud, dramatic tone of voice'], 0),
   ('Why might an effective persuasive essay use all three appeals together?', ['Combining credibility, emotion, and logic can make an argument more convincing to a broader audience', 'Using more than one appeal always weakens an argument', 'Effective persuasion never relies on logic or evidence', 'Ethos, pathos, and logos are always identical in effect'], 0)]),
M('Geometry: Introduction to Fractals and Self-Similarity',
  'Grade 8 Math strand: a fractal is a complex geometric shape that displays self-similarity, meaning smaller sections of the shape resemble the whole, a property often generated by repeating a simple pattern at increasingly smaller scales.',
  [('What is self-similarity in a fractal?', ['Smaller sections of the shape resemble the whole shape', 'Every section of the shape is a perfect circle', 'The shape never repeats any pattern', 'The shape has only one possible size'], 0),
   ('How are many fractals generated?', ['By repeating a simple pattern at increasingly smaller scales', 'By randomly assigning shapes with no repeating pattern', 'By using only straight lines with no repetition', 'By measuring the volume of a sphere'], 0),
   ('Which of these is a well-known example of a fractal pattern?', ['The Koch snowflake', 'A perfect square', 'A single straight line', 'A basic right triangle'], 0),
   ('Why might fractal patterns appear in nature, such as in snowflakes, ferns, or coastlines?', ['Natural growth processes often repeat similar branching or layering patterns at different scales', 'Nature never displays any patterns resembling fractals', 'Fractals only exist as abstract mathematical concepts with no natural examples', 'Coastlines and ferns always have perfectly smooth, non-repeating shapes'], 0),
   ('Why do fractals challenge the idea of measuring a shapes length using traditional methods?', ['Zooming into a fractal reveals increasing detail, which can make measured length increase without an upper limit', 'Fractals always have a single, easily measured length with no complications', 'Traditional measurement methods always work perfectly on any fractal', 'Fractals have no geometric properties worth measuring'], 0)]),
Sc('The Physics of Sound Insulation and Noise Reduction',
   'Grade 8 Science strand: sound insulation reduces the transmission of sound energy between spaces by absorbing, blocking, or dampening sound waves, often using dense or porous materials designed to minimize vibration and reflection.',
   [('What is the main purpose of sound insulation?', ['To reduce the transmission of sound energy between spaces', 'To increase the volume of sound passing through a wall', 'To eliminate the need for any building materials', 'To convert sound waves into visible light'], 0),
    ('How do porous materials often help reduce noise?', ['They absorb sound energy, converting it into small amounts of heat', 'They reflect all sound waves perfectly with no absorption', 'Porous materials always amplify sound waves', 'They block light rather than sound'], 0),
    ('What property of a material often makes it effective at blocking sound transmission?', ['High density, which resists the vibration needed to transmit sound', 'Extremely low density with many open gaps', 'Bright colour with no connection to sound', 'High electrical conductivity'], 0),
    ('Why might a recording studio use both absorptive and dense materials together?', ['Absorptive materials reduce echo while dense materials block outside noise from entering', 'Absorptive and dense materials always have identical effects on sound', 'Combining materials always increases unwanted noise', 'Recording studios never require any sound control'], 0),
    ('Why is sound insulation an important consideration in apartment building design?', ['It can reduce noise transmission between units, improving comfort and privacy for residents', 'Sound insulation has no effect on residents comfort or privacy', 'Apartment buildings never transmit sound between separate units', 'Noise levels have no connection to building material choices'], 0)]),
H('The Rebellion Losses Bill and the Growth of Responsible Government',
  'Grade 8 History strand: the Rebellion Losses Bill of 1849 compensated residents of Lower Canada for property damaged during the Rebellions of 1837-38, and the governments decision to sign it despite public outrage demonstrated an early and significant expansion of responsible government in the colonies.',
  [('What did the Rebellion Losses Bill of 1849 provide?', ['Compensation for residents whose property was damaged during the Rebellions of 1837-38', 'Funding for a new national railway', 'A formal declaration of independence from Britain', 'A plan for creating a new provincial border'], 0),
   ('In which colony did the events surrounding the Rebellion Losses Bill primarily take place?', ['Lower Canada', 'British Columbia', 'Newfoundland', 'Prince Edward Island'], 0),
   ('How did some members of the public react to the passing of the Rebellion Losses Bill?', ['With significant outrage, including violent protests', 'With complete indifference and no reaction at all', 'With immediate and universal approval', 'By demanding the bill be expanded further'], 0),
   ('Why is the governments decision to sign the Rebellion Losses Bill despite public backlash considered historically significant?', ['It demonstrated that the elected government, not colonial officials alone, held real decision-making power', 'The decision had no effect on how government authority was understood', 'The bill was immediately reversed due to the backlash', 'It proved that responsible government would never be achieved'], 0),
   ('Why is the Rebellion Losses Bill connected to the broader growth of responsible government in Canada?', ['It showed the governors willingness to accept the decisions of an elected government, a key principle of responsible government', 'The bill had no connection to the concept of responsible government', 'Responsible government was fully established long before this event occurred', 'The governor overturned the bill personally, rejecting the elected governments authority'], 0)]),
]),
day(130, [
L('Language Review: Grammar, Vocabulary, and Persuasive Writing (Days 121-129)',
  'Grade 8 Language strand review: students revisit apostrophes and possessives, archaisms, foils and antagonists, public service announcements, infographics, allusion, interjections, malapropisms, and persuasion using ethos, pathos, and logos.',
  [('What is the purpose of an apostrophe in a possessive noun?', ['To show ownership or a relationship between two nouns', 'To end a question', 'To join two independent clauses', 'To indicate plural number'], 0),
   ('What is an archaism?', ['A word or phrase that was once common but is no longer used in everyday language', 'A newly invented word describing modern technology', 'A grammatical rule about verb tense', 'A citation format used in essays'], 0),
   ('What is a foil in literature?', ['A character whose contrasting traits highlight qualities in another character', 'A character who narrates the entire story', 'A type of punctuation mark', 'A citation style used in essays'], 0),
   ('What is an allusion?', ['A brief, indirect reference to a person, event, or work the author expects readers to recognize', 'A detailed explanation of every historical event mentioned in a text', 'A type of punctuation mark', 'A citation style used in essays'], 0),
   ('What does ethos appeal to in an argument?', ['The credibility and trustworthiness of the writer or speaker', 'The audiences emotions', 'Logical evidence and reasoning', 'The setting of the argument'], 0)]),
M('Math Review: Statistics, Number Theory, and Geometry (Days 121-129)',
  'Grade 8 Math strand review: students revisit the correlation coefficient, perfect and abundant numbers, radian measure, derivatives, hypothesis testing, Cramers Rule, the Chinese Remainder Theorem, conic sections, and fractals.',
  [('What range of values can the correlation coefficient r take?', ['Between negative one and positive one', 'Between zero and one hundred', 'Any whole number', 'Only positive integers'], 0),
   ('What defines a perfect number?', ['It equals the sum of its proper divisors', 'It has no divisors other than one', 'It is always an odd number', 'It is always a prime number'], 0),
   ('How is one radian defined?', ['The angle formed when the arc length equals the circles radius', 'The angle formed by exactly one degree', 'An angle that always equals ninety degrees', 'An angle with no defined arc length'], 0),
   ('What does a derivative measure?', ['The instantaneous rate of change of a function at a given point', 'The total area under a curve', 'A fixed value that never changes', 'The average of a data set'], 0),
   ('What is self-similarity in a fractal?', ['Smaller sections of the shape resemble the whole shape', 'Every section of the shape is a perfect circle', 'The shape never repeats any pattern', 'The shape has only one possible size'], 0)]),
Sc('Science Review: Human Body, Chemistry, and Physics (Days 121-129)',
   'Grade 8 Science strand review: students revisit the skeletal system, soap chemistry, bioluminescence, magnetism, the respiratory system, invasive species, acid-base titration, earthquake-resistant engineering, and sound insulation.',
   [('What is one major function of the skeletal system?', ['Providing structural support and protecting internal organs', 'Digesting food in the stomach', 'Pumping blood through the body', 'Producing sound for speech'], 0),
    ('What is a surfactant?', ['A substance with one end that attracts water and one end that attracts oil or grease', 'A substance that only ever repels water', 'A type of enzyme found in the digestive system', 'A gas released during combustion'], 0),
    ('What is bioluminescence?', ['The production of light by living organisms through a chemical reaction', 'The absorption of light by plants during photosynthesis', 'A type of radioactive decay', 'A reflection of sunlight off an animals skin'], 0),
    ('Where does gas exchange occur in the lungs?', ['In tiny air sacs called alveoli', 'In the trachea only', 'In the diaphragm only', 'In the nasal passages only'], 0),
    ('What is the main goal of earthquake-resistant engineering?', ['To help buildings absorb and dissipate seismic energy, reducing damage', 'To make buildings completely immovable during any earthquake', 'To eliminate the need for any structural design considerations', 'To prevent earthquakes from occurring at all'], 0)]),
H('History Review: Confederation, Institutions, and Infrastructure (Days 121-129)',
  'Grade 8 History strand review: students revisit the fur trade, the Charlottetown and Quebec Conferences, the Pacific Scandal, the Cypress Hills Massacre, the Numbered Treaties, the Canadian National Railway, the Royal Canadian Mounted Police, the Trans-Canada Highway, and the Rebellion Losses Bill.',
  [('What resource primarily drove the early Canadian fur trade?', ['Beaver pelts', 'Gold deposits', 'Cod fisheries', 'Timber exports'], 0),
   ('What was the main purpose of the Charlottetown Conference of 1864?', ['To discuss uniting British North American colonies', 'To negotiate a peace treaty ending a war', 'To establish a new national anthem', 'To settle a border dispute with the United States'], 0),
   ('What was the Pacific Scandal of 1873 primarily about?', ['Accusations that the government accepted campaign funds in exchange for a railway contract', 'A dispute over international fishing rights', 'A disagreement about provincial school funding', 'An argument over a proposed national anthem'], 0),
   ('In what year was the Royal Canadian Mounted Police formed?', ['1920', '1867', '1873', '1949'], 0),
   ('In what year was the Trans-Canada Highway officially opened?', ['1962', '1867', '1920', '1949'], 0)]),
]),
]

if __name__ == '__main__':
    _rebalance_answer_positions(g8_121_130)
    append_to(8, g8_121_130)
