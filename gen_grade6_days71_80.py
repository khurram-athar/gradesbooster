#!/usr/bin/env python3
"""Phase 3 extension: Grade 6, Days 71-80 (continuing past the Day 70
milestone reached in gen_grade6_days61_70.py, toward the full 157-day
year). Topics chosen to avoid any overlap with the existing Day 1-70
set (see data/grade6.json): adverbs and figurative language through
giving clear oral instructions, decimal powers of ten through sampling
bias, the digestive system through the integumentary system, and the
War of 1812 through 19th/20th-century immigration waves to Canada.

Subject keys for Grade 6 are "Language", "Math", "Science",
"SocialStudies" (same as all earlier Grade 6 batches).

videoUrl is intentionally left unset for every subject --
fetch_video_ids.py fills these in automatically on its next daily run.
No embedded ASCII double-quote characters are used anywhere in
question/summary/option text; apostrophes and quotation marks use the
curly Unicode form (’ “ ”).
"""
import sys
sys.path.insert(0, '/sessions/happy-laughing-ritchie/mnt/gradesbooster')
from gen_curriculum import sub, day, append_to

L6 = 'https://tvolearn.com/pages/grade-6-language'
M6 = 'https://tvolearn.com/pages/grade-6-mathematics'
S6 = 'https://tvolearn.com/pages/grade-6-science-and-technology'
SS6 = 'https://tvolearn.com/pages/grade-6-social-studies'
RL, RM, RS, RSS = (
    'TVO Learn: Grade 6 Language',
    'TVO Learn: Grade 6 Mathematics',
    'TVO Learn: Grade 6 Science & Technology',
    'TVO Learn: Grade 6 Social Studies',
)


def L(t, s, q):
    return sub('Language', t, s, RL, L6, q)


def M(t, s, q):
    return sub('Math', t, s, RM, M6, q)


def Sc(t, s, q):
    return sub('Science', t, s, RS, S6, q)


def SS(t, s, q):
    return sub('SocialStudies', t, s, RSS, SS6, q)


g6_71_80 = [
day(71, [
L('Grammar: Adverbs and Adverbial Phrases',
  'Grade 6 Language strand: an adverb modifies a verb, adjective, or other adverb, often telling how, when, where, or to what extent something happens, and an adverbial phrase is a group of words serving the same function.',
  [('An adverb typically modifies a ___.', ['Verb, adjective, or other adverb', 'Noun or pronoun only', 'A concept unrelated to adverbs', 'Punctuation mark'], 0),
   ('Which word in the sentence “She sang beautifully” is the adverb?', ['Beautifully', 'She', 'A word unrelated to this sentence', 'Sang'], 0),
   ('Which of these adverbial phrases tells when an action happened?', ['After the bell rang', 'Very quickly', 'A phrase unrelated to adverbial phrases', 'Under the table'], 0),
   ('Many adverbs are formed by adding which suffix to an adjective?', ['-ly', '-ing', 'A suffix unrelated to forming adverbs', '-est'], 0),
   ('Why might a writer use an adverb such as “cautiously” instead of just “walked”?', ['It adds detail about how an action was performed', 'Adverbs never add any detail to a sentence', 'A reason unrelated to adverbs', 'Adverbs can only describe nouns, never actions'], 0)]),
M('Multiplying and Dividing Decimals by Powers of Ten',
  'Grade 6 Math strand: multiplying a decimal by a power of ten moves the decimal point to the right, while dividing by a power of ten moves the decimal point to the left, with the number of places matching the power’s exponent.',
  [('When you multiply a decimal by 10, the decimal point moves ___.', ['One place to the right', 'One place to the left', 'A direction unrelated to multiplying by ten', 'Two places to the right'], 0),
   ('What is 3.42 × 100?', ['342', '34.2', 'A value unrelated to the calculation', '3420'], 0),
   ('What is 56.7 ÷ 10?', ['5.67', '567', 'A value unrelated to the calculation', '0.567'], 0),
   ('What is 0.08 × 1000?', ['80', '8', 'A value unrelated to the calculation', '800'], 0),
   ('Why is it useful to recognize the pattern of moving the decimal point when multiplying or dividing by powers of ten?', ['It allows quick mental calculations without long multiplication or division', 'This pattern never applies to decimal numbers', 'A reason unrelated to place value', 'Powers of ten have no effect on decimal numbers'], 0)]),
Sc('The Digestive System and Nutrient Absorption',
   'Grade 6 Science strand: the digestive system breaks down food into nutrients that the body can absorb and use for energy, growth, and repair, through organs including the stomach, small intestine, and large intestine.',
   [('The main purpose of the digestive system is to ___.', ['Break down food into nutrients the body can absorb and use', 'Pump blood throughout the body', 'A concept unrelated to the digestive system', 'Filter air before it reaches the lungs'], 0),
    ('Which organ mixes food with acid to begin breaking down proteins?', ['The stomach', 'The lungs', 'An organ unrelated to digestion', 'The heart'], 0),
    ('Most nutrient absorption into the bloodstream happens in the ___.', ['Small intestine', 'Large intestine', 'An organ unrelated to nutrient absorption', 'Esophagus'], 0),
    ('What is the main role of the large intestine in digestion?', ['Absorbing water and forming solid waste', 'Breaking down proteins with acid', 'A role unrelated to the large intestine', 'Pumping digested food to the heart'], 0),
    ('Why does the body need to break large food molecules into smaller nutrients during digestion?', ['Smaller nutrient molecules can pass into the bloodstream and be used by cells', 'Breaking down food serves no useful purpose for the body', 'A reason unrelated to digestion', 'Large food molecules are already able to enter cells directly'], 0)]),
SS('The War of 1812: Defending British North America',
   'Grade 6 Social Studies strand: the War of 1812 was fought between the United States and Britain (including its colonies in British North America), and its outcome helped shape a distinct identity for the colonies that would later become Canada.',
   [('The War of 1812 was fought primarily between Britain (with its colonies) and ___.', ['The United States', 'France', 'A country unrelated to the War of 1812', 'Spain'], 0),
    ('The War of 1812 took place in and around which region?', ['British North America (including present-day Ontario and Quebec)', 'A region unrelated to the War of 1812', 'Continental Europe', 'The Caribbean islands exclusively'], 0),
    ('Which group, alongside British soldiers and colonial militia, played an important role in defending British North America during the war?', ['Indigenous allies, such as those led by Tecumseh', 'A group unrelated to the War of 1812', 'Volunteers from countries outside North America only', 'No additional groups were involved in the defence'], 0),
    ('Why is the War of 1812 often seen as important to the development of a Canadian identity?', ['Successfully defending the colonies helped foster pride and a sense of shared identity', 'The war had no effect on the colonies’ sense of identity', 'A reason unrelated to Canadian history', 'The colonies were conquered and lost all self-governance'], 0),
    ('What was one major outcome of the War of 1812?', ['Borders between British North America and the United States remained largely unchanged', 'The United States permanently annexed all of British North America', 'A concept unrelated to the war’s outcome', 'Britain lost control of all its remaining North American colonies'], 0)])]),
day(72, [
L('Writing: Procedural Writing — How-To Texts',
  'Grade 6 Language strand: procedural writing gives step-by-step instructions for completing a task, typically using a list of materials, sequential steps, and clear, imperative verbs.',
  [('Procedural writing is best described as ___.', ['Step-by-step instructions for completing a task', 'A story with characters and a setting', 'A concept unrelated to procedural writing', 'A poem describing personal feelings'], 0),
   ('Which of these sentences uses an imperative verb typical of procedural writing?', ['Pour the flour into the bowl.', 'The flour was poured into the bowl by someone.', 'A sentence unrelated to procedural writing', 'Flour, bowls, and pouring are sometimes related.'], 0),
   ('Why do procedural texts often include a list of materials at the beginning?', ['So the reader can gather everything needed before starting the steps', 'Materials lists are never included in procedural writing', 'A reason unrelated to procedural writing', 'To make the text longer with no real purpose'], 0),
   ('Which transition word would most likely appear in a procedural text to show order?', ['Next', 'Meanwhile', 'A word unrelated to sequencing steps', 'Although'], 0),
   ('Why is it important for the steps in a procedural text to be written in the correct order?', ['Following steps out of order could cause the task to fail or turn out incorrectly', 'The order of steps never affects the outcome of a task', 'A reason unrelated to procedural writing', 'Procedural texts are not meant to be followed in any specific order'], 0)]),
M('Angle Relationships: Complementary, Supplementary, and Vertical Angles',
  'Grade 6 Math strand: complementary angles sum to 90 degrees, supplementary angles sum to 180 degrees, and vertical angles are formed by intersecting lines and are always equal to each other.',
  [('Two angles are complementary if their measures add up to ___.', ['90 degrees', '180 degrees', 'A sum unrelated to complementary angles', '360 degrees'], 0),
   ('Two angles are supplementary if their measures add up to ___.', ['180 degrees', '90 degrees', 'A sum unrelated to supplementary angles', '45 degrees'], 0),
   ('If one angle measures 35 degrees, what does its complementary angle measure?', ['55 degrees', '145 degrees', 'A measure unrelated to the calculation', '35 degrees'], 0),
   ('Vertical angles, formed when two lines cross, are always ___.', ['Equal to each other', 'Supplementary to each other', 'A relationship unrelated to vertical angles', 'Impossible to measure'], 0),
   ('Why is understanding angle relationships useful when solving geometry problems?', ['It allows missing angle measures to be calculated without a protractor', 'Angle relationships provide no useful information for solving problems', 'A reason unrelated to geometry', 'Every angle in a diagram must be measured directly with a protractor'], 0)]),
Sc('The Circulatory System: Heart, Blood, and Vessels',
   'Grade 6 Science strand: the circulatory system, made up of the heart, blood, and blood vessels, transports oxygen and nutrients throughout the body while carrying away waste products.',
   [('The main function of the circulatory system is to ___.', ['Transport oxygen, nutrients, and waste throughout the body', 'Break down food into nutrients', 'A concept unrelated to the circulatory system', 'Filter air before it reaches the lungs'], 0),
    ('Which organ pumps blood throughout the circulatory system?', ['The heart', 'The stomach', 'An organ unrelated to circulation', 'The liver'], 0),
    ('Which blood vessels carry oxygen-rich blood away from the heart to the body?', ['Arteries', 'Veins', 'A vessel unrelated to circulation', 'Capillaries only carry waste, never oxygen'], 0),
    ('What is the role of tiny blood vessels called capillaries?', ['Allowing oxygen and nutrients to pass between blood and body cells', 'Pumping blood directly out of the heart', 'A role unrelated to capillaries', 'Storing digested food for later use'], 0),
    ('Why is the circulatory system considered essential for nearly every cell in the body?', ['Cells rely on the blood supply for oxygen and nutrients to survive and function', 'Most cells in the body do not need oxygen or nutrients', 'A reason unrelated to the circulatory system', 'The circulatory system only serves the heart itself'], 0)]),
SS('The Underground Railroad and Its Connection to Canada',
   'Grade 6 Social Studies strand: the Underground Railroad was a secret network of routes and safe houses that helped enslaved people in the United States escape to freedom, with many settling in British North America (present-day Canada).',
   [('The Underground Railroad was best described as ___.', ['A secret network of routes and safe houses helping enslaved people escape to freedom', 'An actual railway built underground', 'A concept unrelated to the Underground Railroad', 'A government program run openly by the United States'], 0),
    ('Why did many freedom seekers travel all the way to British North America (present-day Canada)?', ['Slavery had been abolished there, offering greater safety and legal protection', 'Canada offered no additional safety compared to the United States', 'A reason unrelated to the Underground Railroad', 'British North America required freedom seekers to remain enslaved'], 0),
    ('People who helped guide freedom seekers along the Underground Railroad were sometimes called ___.', ['Conductors', 'Passengers only, with no guides involved', 'A term unrelated to the Underground Railroad', 'Engineers who built physical railways'], 0),
    ('Which of these communities in present-day Ontario became known as a settlement point for people who arrived via the Underground Railroad?', ['Buxton', 'A community unrelated to the Underground Railroad', 'A settlement located outside of Canada', 'A city that refused to accept any new settlers'], 0),
    ('Why is the story of the Underground Railroad an important part of Canadian history?', ['It highlights Canada’s role in offering freedom and safety to those escaping enslavement', 'The Underground Railroad had no connection to Canadian history', 'A reason unrelated to this history', 'No freedom seekers ever settled permanently in Canada'], 0)])]),
day(73, [
L('Reading: Similes, Metaphors, and Personification',
  'Grade 6 Language strand: a simile compares two things using “like” or “as,” a metaphor states that one thing is another to suggest a comparison, and personification gives human qualities to something non-human.',
  [('A simile compares two things using which words?', ['Like or as', 'Metaphor or simile', 'Words unrelated to similes', 'Because or therefore'], 0),
   ('Which sentence is an example of a metaphor?', ['Her smile was sunshine on a cloudy day.', 'Her smile was as bright as the sun.', 'A sentence unrelated to metaphors', 'Her smile appeared briefly on her face.'], 0),
   ('Which sentence uses personification?', ['The wind whispered through the trees.', 'The wind blew at ten kilometres per hour.', 'A sentence unrelated to personification', 'The trees were tall and green.'], 0),
   ('Unlike a simile, a metaphor ___.', ['States directly that one thing is another, without using “like” or “as”', 'Always uses the word “like” to make a comparison', 'A description unrelated to metaphors', 'Never compares two different things'], 0),
   ('Why might an author use personification when describing a storm?', ['It can make the storm feel more vivid, powerful, or alive to the reader', 'Personification always makes writing harder to understand', 'A reason unrelated to personification', 'Personification can only be used to describe human characters'], 0)]),
M('Least Common Multiple and Greatest Common Factor',
  'Grade 6 Math strand: the least common multiple (LCM) is the smallest number that is a multiple of two or more numbers, while the greatest common factor (GCF) is the largest number that divides evenly into two or more numbers.',
  [('The least common multiple of two numbers is ___.', ['The smallest number that is a multiple of both numbers', 'The largest number that divides evenly into both numbers', 'A concept unrelated to least common multiple', 'Always equal to one of the two original numbers'], 0),
   ('What is the least common multiple of 4 and 6?', ['12', '24', 'A value unrelated to the calculation', '10'], 0),
   ('The greatest common factor of two numbers is ___.', ['The largest number that divides evenly into both numbers', 'The smallest number that is a multiple of both numbers', 'A concept unrelated to greatest common factor', 'Always equal to one of the two original numbers'], 0),
   ('What is the greatest common factor of 18 and 24?', ['6', '3', 'A value unrelated to the calculation', '12'], 0),
   ('Why is finding the greatest common factor useful when simplifying fractions?', ['Dividing both the numerator and denominator by it reduces a fraction to lowest terms', 'The greatest common factor has no connection to simplifying fractions', 'A reason unrelated to fractions', 'Simplifying fractions never requires finding common factors'], 0)]),
Sc('The Respiratory System: Breathing and Gas Exchange',
   'Grade 6 Science strand: the respiratory system brings oxygen into the body and removes carbon dioxide, using the lungs as the main site of gas exchange between air and blood.',
   [('The main function of the respiratory system is to ___.', ['Bring oxygen into the body and remove carbon dioxide', 'Pump blood throughout the body', 'A concept unrelated to the respiratory system', 'Break down food into usable nutrients'], 0),
    ('Where does gas exchange mainly occur in the respiratory system?', ['In tiny air sacs called alveoli, inside the lungs', 'In the stomach', 'A location unrelated to gas exchange', 'In the heart’s chambers'], 0),
    ('When a person inhales, which gas mainly enters the bloodstream from the lungs?', ['Oxygen', 'Carbon dioxide', 'A gas unrelated to breathing', 'Nitrogen is absorbed in the largest amount'], 0),
    ('What role does the diaphragm play in breathing?', ['It contracts and relaxes to help air move in and out of the lungs', 'It filters food before it enters the stomach', 'A role unrelated to the diaphragm', 'It pumps blood to the lungs'], 0),
    ('Why is the respiratory system’s connection to the circulatory system important for the body?', ['Oxygen absorbed by the lungs must be carried by the blood to cells throughout the body', 'The respiratory and circulatory systems have no connection to one another', 'A reason unrelated to these body systems', 'Oxygen never needs to reach cells outside the lungs'], 0)]),
SS('Treaties and Indigenous-Crown Relations in Canada',
   'Grade 6 Social Studies strand: treaties are formal agreements made between Indigenous peoples and the Crown, historically involving land, resources, and rights, and they remain an important part of Indigenous-Crown relations in Canada today.',
   [('A treaty between Indigenous peoples and the Crown is best described as ___.', ['A formal agreement involving matters such as land, resources, or rights', 'An informal conversation with no lasting effect', 'A concept unrelated to treaties', 'A type of holiday celebrated across Canada'], 0),
    ('Why were many historical treaties in Canada focused on land?', ['They often set out how land would be shared or used by Indigenous peoples and settlers', 'Land was never a topic addressed in Canadian treaties', 'A reason unrelated to treaties', 'Treaties in Canada have never mentioned land in any way'], 0),
    ('Why is it important for treaties to be honoured by all parties involved?', ['Treaties represent legal and moral commitments that affect rights and relationships today', 'Treaties have no legal or lasting significance once signed', 'A reason unrelated to treaties', 'Only one side of a treaty is ever expected to follow its terms'], 0),
    ('Which of these best describes the ongoing relationship between Indigenous peoples and the Crown today?', ['It continues to evolve through dialogue, land claims, and treaty rights discussions', 'It ended completely once historical treaties were signed', 'A description unrelated to Indigenous-Crown relations', 'No relationship of any kind currently exists'], 0),
    ('Why do students study historical treaties as part of Canadian social studies?', ['Understanding treaties helps explain present-day rights, land use, and reconciliation efforts', 'Treaties have no connection to present-day Canadian society', 'A reason unrelated to studying Canadian history', 'Treaties are considered unimportant to Canadian history'], 0)])]),
day(74, [
L('Vocabulary: Using a Thesaurus and Dictionary Effectively',
  'Grade 6 Language strand: a dictionary provides a word’s definition, pronunciation, and part of speech, while a thesaurus offers synonyms and antonyms to help writers choose more precise or varied words.',
  [('A dictionary is a resource that provides a word’s ___.', ['Definition, pronunciation, and part of speech', 'List of synonyms only, with no definitions', 'A concept unrelated to dictionaries', 'Only its spelling, with no other information'], 0),
   ('A thesaurus is most useful for finding ___.', ['Synonyms and antonyms for a word', 'A word’s exact pronunciation only', 'A concept unrelated to a thesaurus', 'The number of letters in a word'], 0),
   ('Why might a writer consult a thesaurus while revising a paragraph?', ['To replace an overused word with a more precise or varied synonym', 'A thesaurus can only be used before any writing begins', 'A reason unrelated to using a thesaurus', 'Thesauruses never provide alternative word choices'], 0),
   ('Which of these would most likely be found first in a dictionary entry?', ['The word’s pronunciation and part of speech', 'A list of the word’s antonyms only', 'A concept unrelated to dictionary entries', 'A paragraph written entirely by the reader'], 0),
   ('Why is it important to consider context when choosing a synonym from a thesaurus?', ['Not all synonyms carry the exact same tone or meaning in every situation', 'All synonyms for a word always mean exactly the same thing in every context', 'A reason unrelated to using a thesaurus', 'Context has no effect on which word is most appropriate'], 0)]),
M('Estimation Strategies for Multi-Step Problems',
  'Grade 6 Math strand: estimation strategies, such as rounding numbers before calculating, help predict a reasonable answer to a multi-step problem and check whether a final calculated answer makes sense.',
  [('Estimation in math is best described as ___.', ['Finding an approximate, reasonable answer rather than an exact one', 'Calculating an answer with complete precision every time', 'A concept unrelated to estimation', 'Ignoring a problem entirely rather than solving it'], 0),
   ('To estimate 297 + 512, which rounded numbers might you use?', ['300 + 500', '250 + 550', 'A pair of numbers unrelated to this estimation', '200 + 500'], 0),
   ('Why is estimation especially useful before solving a multi-step problem?', ['It helps predict a reasonable range for the final answer', 'Estimation always provides the single, exact final answer', 'A reason unrelated to estimation', 'Estimating makes multi-step problems impossible to solve'], 0),
   ('If you estimate an answer to be about 450, but your exact calculation gives 4,500, what does this suggest?', ['A calculation error likely occurred somewhere in the steps', 'The exact calculation must be correct with no need to check further', 'A conclusion unrelated to estimation', 'Estimation is never useful for checking calculations'], 0),
   ('Why might a shopper use estimation while adding up the cost of several items in a store?', ['It provides a quick check of whether they have enough money before reaching the checkout', 'Estimation provides no useful information while shopping', 'A reason unrelated to estimation', 'Shoppers are required to calculate exact totals mentally at all times'], 0)]),
Sc('States of Matter and Changes of State',
   'Grade 6 Science strand: matter exists in states such as solid, liquid, and gas, and changes of state — like melting, freezing, evaporation, and condensation — occur when energy is added to or removed from a substance.',
   [('Which of these is a change of state that occurs when a solid becomes a liquid?', ['Melting', 'Freezing', 'A process unrelated to changes of state', 'Condensation'], 0),
    ('Which process describes a liquid changing into a gas?', ['Evaporation', 'Melting', 'A process unrelated to changes of state', 'Freezing'], 0),
    ('What generally happens to the particles in a substance as it is heated and changes from solid to liquid to gas?', ['They gain energy and move faster and farther apart', 'They lose energy and move closer together', 'A concept unrelated to particle movement', 'They stop moving completely'], 0),
    ('Condensation occurs when a gas ___.', ['Loses energy and changes into a liquid', 'Gains energy and changes into a solid', 'A process unrelated to condensation', 'Remains a gas with no change occurring'], 0),
    ('Why does water vapour on a cold glass of lemonade turn into visible droplets?', ['The vapour loses heat energy near the cold surface and condenses into liquid water', 'The glass produces new water that was not present before', 'A reason unrelated to changes of state', 'Water vapour never changes into liquid water'], 0)]),
SS('The Canadian Charter of Rights and Freedoms',
   'Grade 6 Social Studies strand: the Canadian Charter of Rights and Freedoms, part of Canada’s Constitution since 1982, guarantees fundamental rights and freedoms to people in Canada, including equality, expression, and legal rights.',
   [('The Canadian Charter of Rights and Freedoms is best described as ___.', ['A part of Canada’s Constitution that guarantees fundamental rights and freedoms', 'A document with no legal significance in Canada', 'A concept unrelated to Canadian rights', 'A set of rules that apply only to elected officials'], 0),
    ('The Canadian Charter of Rights and Freedoms became part of Canada’s Constitution in which year?', ['1982', '1867', 'A year unrelated to the Charter', '1945'], 0),
    ('Which of these is an example of a right protected under the Charter?', ['Freedom of expression', 'The right to ignore all laws', 'A concept unrelated to the Charter', 'The right to prevent others from voting'], 0),
    ('Why is the equality guarantee in the Charter considered significant?', ['It affirms that everyone is entitled to equal protection and benefit of the law', 'The equality guarantee applies to no one in Canada', 'A reason unrelated to the Charter', 'It allows certain groups to be treated unfairly under the law'], 0),
    ('Why is the Charter considered an important part of Canadian identity and government?', ['It sets out core rights and freedoms that shape how laws and society operate', 'The Charter has no influence on Canadian laws or society', 'A reason unrelated to the Charter’s significance', 'The Charter has been removed from Canada’s Constitution'], 0)])]),
day(75, [
L('Grammar: Coordinating and Subordinating Conjunctions',
  'Grade 6 Language strand: coordinating conjunctions (like “and,” “but,” and “or”) join equal ideas, while subordinating conjunctions (like “because,” “although,” and “since”) join a dependent clause to an independent clause.',
  [('Coordinating conjunctions are used to ___.', ['Join two equal ideas or clauses', 'Only join a subject to a verb', 'A concept unrelated to coordinating conjunctions', 'Replace punctuation marks entirely'], 0),
   ('Which of these is a coordinating conjunction?', ['But', 'Although', 'A word unrelated to conjunctions', 'Because'], 0),
   ('Which of these is a subordinating conjunction?', ['Because', 'And', 'A word unrelated to conjunctions', 'Or'], 0),
   ('In the sentence “Although it was raining, we went outside,” which word introduces the dependent clause?', ['Although', 'We', 'A word unrelated to this sentence', 'Went'], 0),
   ('Why might a writer choose a subordinating conjunction instead of simply joining two ideas with “and”?', ['It can show a specific relationship, such as cause, contrast, or time, between the ideas', 'Subordinating conjunctions never show a relationship between ideas', 'A reason unrelated to conjunctions', 'Subordinating conjunctions must always come at the end of a sentence'], 0)]),
M('Probability: Sample Space and Outcomes',
  'Grade 6 Math strand: a sample space is the set of all possible outcomes of an experiment, and probability compares the number of favourable outcomes to the total number of outcomes in that sample space.',
  [('The sample space of an experiment is best described as ___.', ['The set of all possible outcomes', 'Only the outcomes that are considered favourable', 'A concept unrelated to sample space', 'A single guaranteed outcome'], 0),
   ('What is the sample space when rolling a standard six-sided die?', ['{1, 2, 3, 4, 5, 6}', '{1, 2, 3}', 'A set unrelated to this sample space', '{0, 1}'], 0),
   ('If a bag contains 3 red marbles and 2 blue marbles, what is the probability of picking a red marble?', ['3/5', '2/5', 'A probability unrelated to the calculation', '1/5'], 0),
   ('When flipping a fair coin, what is the probability of landing on heads?', ['1/2', '1/4', 'A probability unrelated to the calculation', '1'], 0),
   ('Why is it useful to identify the full sample space before calculating a probability?', ['It ensures every possible outcome is accounted for when comparing favourable outcomes to the total', 'The sample space has no effect on calculating probability', 'A reason unrelated to probability', 'Probability can be calculated accurately without knowing all possible outcomes'], 0)]),
Sc('Soil Composition and Formation',
   'Grade 6 Science strand: soil forms over long periods of time as rock is broken down by weathering and mixed with organic matter, water, and air, creating layers that support plant growth.',
   [('Soil is formed largely through the weathering of ___.', ['Rock, combined with organic matter over time', 'Metal objects buried underground', 'A concept unrelated to soil formation', 'Only water, with no solid material involved'], 0),
    ('Which of these is considered organic matter that can become part of soil?', ['Decomposed plant and animal material', 'Large boulders with no decomposition', 'A material unrelated to soil composition', 'Metal fragments from human structures'], 0),
    ('Why does soil formation typically take a very long time?', ['Weathering rock into small particles and mixing in organic material is a slow, gradual process', 'Soil forms instantly whenever rock is exposed to air', 'A reason unrelated to soil formation', 'Soil requires no weathering or organic material to form'], 0),
    ('Which layer of soil is typically richest in nutrients and organic matter, supporting plant growth?', ['Topsoil', 'Bedrock', 'A layer unrelated to soil composition', 'A layer made entirely of ice'], 0),
    ('Why is soil considered an important natural resource for ecosystems and agriculture?', ['It provides nutrients, water, and support that plants need to grow', 'Soil provides no benefit to plants or ecosystems', 'A reason unrelated to soil’s importance', 'Plants can grow equally well with no soil at all'], 0)]),
SS('The Fur Trade and the Voyageurs',
   'Grade 6 Social Studies strand: the fur trade was a major economic activity in early Canada, relying on voyageurs — skilled canoe travellers — and partnerships with Indigenous peoples to transport furs across vast distances.',
   [('The fur trade in early Canada was centred mainly around which resource?', ['Beaver pelts and other furs', 'Gold and silver', 'A resource unrelated to the fur trade', 'Grain and other crops'], 0),
    ('Voyageurs were best known for their skill in ___.', ['Paddling canoes over long distances to transport furs and goods', 'Building large stone structures', 'A skill unrelated to voyageurs', 'Farming large areas of land'], 0),
    ('Why were partnerships between European traders and Indigenous peoples important to the fur trade?', ['Indigenous peoples had knowledge of the land, trapping, and trade routes essential to the trade’s success', 'These groups never worked together in the fur trade', 'A reason unrelated to the fur trade', 'European traders required no assistance to succeed in the fur trade'], 0),
    ('Which companies competed for control of the fur trade in what is now Canada?', ['The Hudson’s Bay Company and the North West Company', 'Companies unrelated to the fur trade', 'Only companies based outside of North America', 'A single company that faced no competition at all'], 0),
    ('Why is the fur trade considered a significant part of early Canadian economic history?', ['It shaped exploration, trade routes, and relationships between European settlers and Indigenous peoples', 'The fur trade had no lasting effect on Canada’s development', 'A reason unrelated to the fur trade’s significance', 'The fur trade took place entirely outside of Canada’s territory'], 0)])]),
day(76, [
L('Writing: Revising for Clarity and Conciseness',
  'Grade 6 Language strand: revising for clarity and conciseness means removing unnecessary words, combining repetitive ideas, and choosing precise language so that writing communicates its meaning as clearly as possible.',
  [('Revising for conciseness mainly involves ___.', ['Removing unnecessary words while keeping the meaning clear', 'Adding as many extra words as possible', 'A concept unrelated to conciseness', 'Rewriting a text in a completely different language'], 0),
   ('Which of these sentences is more concise while keeping the same meaning?', ['She quickly finished her homework before dinner.', 'She, in a very fast and quick manner, finished up completing all of her homework before the time came for dinner.', 'A sentence unrelated to conciseness', 'Homework dinner she quick finish before.'], 0),
   ('Why might a writer combine two repetitive sentences into one clearer sentence during revision?', ['It removes redundancy and helps the writing flow more smoothly', 'Combining sentences always makes writing more confusing', 'A reason unrelated to revising for clarity', 'Repetitive sentences are always preferred over concise ones'], 0),
   ('Which of these phrases could most likely be shortened for conciseness?', ['Due to the fact that', 'The dog ran', 'A phrase unrelated to conciseness', 'She smiled'], 0),
   ('Why is clarity an important goal when revising a piece of writing?', ['Clear writing helps the reader understand the intended meaning without confusion', 'Clarity has no effect on how well a reader understands a text', 'A reason unrelated to revising writing', 'Confusing writing is always more effective than clear writing'], 0)]),
M('Unit Rates and Comparing Best Buys',
  'Grade 6 Math strand: a unit rate expresses a quantity per single unit, such as price per item, and comparing unit rates helps determine which of two or more options offers the better value.',
  [('A unit rate expresses a quantity ___.', ['Per single unit, such as price per one item', 'As a fraction with no connection to a single unit', 'A concept unrelated to unit rates', 'Only in terms of time, never price'], 0),
   ('If 4 apples cost $2.00, what is the unit rate (price per apple)?', ['$0.50 per apple', '$2.00 per apple', 'A rate unrelated to the calculation', '$8.00 per apple'], 0),
   ('A box of 8 granola bars costs $4.00, and a box of 10 granola bars costs $4.50. Which box offers the better unit rate?', ['The box of 10, at $0.45 per bar', 'The box of 8, at $0.50 per bar', 'Both boxes offer exactly the same unit rate', 'A comparison unrelated to this calculation'], 0),
   ('Why is comparing unit rates more useful than comparing total prices alone when shopping?', ['It accounts for differences in quantity, showing which option is truly the better value', 'Total price always shows the better value regardless of quantity', 'A reason unrelated to comparing unit rates', 'Unit rates provide no useful information for comparing prices'], 0),
   ('If a car travels 240 kilometres in 3 hours, what is its unit rate of speed?', ['80 kilometres per hour', '60 kilometres per hour', 'A rate unrelated to the calculation', '720 kilometres per hour'], 0)]),
Sc('Freshwater and Saltwater Ecosystems',
   'Grade 6 Science strand: freshwater ecosystems, such as lakes and rivers, and saltwater ecosystems, such as oceans, support different communities of organisms adapted to their specific water conditions.',
   [('Which of these is an example of a freshwater ecosystem?', ['A river', 'An ocean', 'A concept unrelated to freshwater ecosystems', 'A saltwater coral reef'], 0),
    ('Which of these is an example of a saltwater ecosystem?', ['An ocean', 'A freshwater lake', 'A concept unrelated to saltwater ecosystems', 'A small freshwater pond'], 0),
    ('Why can most freshwater fish not survive if placed directly into a saltwater ecosystem?', ['Their bodies are adapted to a much lower salt concentration than ocean water contains', 'Freshwater and saltwater fish always have identical adaptations', 'A reason unrelated to freshwater and saltwater ecosystems', 'Freshwater fish are never adapted to any specific water conditions'], 0),
    ('Which of these organisms is specifically adapted to live in a saltwater ecosystem?', ['A clownfish living among ocean coral reefs', 'A frog living in a small freshwater pond', 'An organism unrelated to saltwater ecosystems', 'A trout living only in a freshwater stream'], 0),
    ('Why is it important for scientists to study both freshwater and saltwater ecosystems?', ['Each supports unique organisms and plays a distinct role in the health of the planet', 'Freshwater and saltwater ecosystems are identical, so studying both is unnecessary', 'A reason unrelated to studying ecosystems', 'Only one type of water ecosystem exists on Earth'], 0)]),
SS('The Métis Nation and the Red River Resistance',
   'Grade 6 Social Studies strand: the Métis Nation, descended from First Nations and European ancestry, developed a distinct culture in the Red River area, and the Red River Resistance of 1869-1870, led by Louis Riel, arose to protect Métis land and rights.',
   [('The Métis Nation developed from a blend of ___.', ['First Nations and European ancestry and culture', 'Only European settlers, with no Indigenous connection', 'A concept unrelated to the Métis Nation', 'Only Indigenous groups with no European connection'], 0),
    ('The Red River Resistance took place in the region now known as ___.', ['Manitoba', 'British Columbia', 'A region unrelated to the Red River Resistance', 'Newfoundland and Labrador'], 0),
    ('Who was the key Métis leader during the Red River Resistance?', ['Louis Riel', 'A leader unrelated to the Red River Resistance', 'A leader from an entirely different region of Canada', 'A leader who represented only the federal government'], 0),
    ('What was a major goal of the Red River Resistance?', ['Protecting Métis land, rights, and way of life as settlers moved westward', 'Expanding Métis territory into other countries', 'A concept unrelated to the Red River Resistance', 'Removing all settlers from Canada entirely'], 0),
    ('Why is the Red River Resistance considered an important event in Canadian history?', ['It led to the creation of Manitoba as a province and highlighted Métis rights', 'The resistance had no lasting impact on Canadian history', 'A reason unrelated to its historical significance', 'It occurred in a region that never became part of Canada'], 0)])]),
day(77, [
L('Reading: Mood and Atmosphere in Fiction',
  'Grade 6 Language strand: mood is the feeling or atmosphere a piece of writing creates for the reader, often shaped by word choice, setting, and descriptive imagery.',
  [('Mood in a story is best described as ___.', ['The feeling or atmosphere the writing creates for the reader', 'The order in which events occur', 'A concept unrelated to mood', 'The exact number of characters in a story'], 0),
   ('Which of these word choices would most likely create a mysterious mood?', ['Shadowy, silent, and eerie', 'Bright, cheerful, and sunny', 'Words unrelated to creating a mysterious mood', 'Loud, festive, and colourful'], 0),
   ('How does setting often contribute to a story’s mood?', ['Details like weather, time, and location can shape how a scene feels to the reader', 'Setting has no connection to a story’s mood', 'A reason unrelated to mood', 'Mood can only be created through dialogue, never setting'], 0),
   ('Which of these sentences most strongly creates a tense, suspenseful mood?', ['The floorboards creaked as a shadow moved slowly closer.', 'The kitchen smelled like fresh cookies on a sunny afternoon.', 'A sentence unrelated to creating mood', 'The book had two hundred pages.'], 0),
   ('Why might an author carefully choose descriptive imagery to build a story’s mood?', ['Strong imagery can immerse the reader in the emotional tone of a scene', 'Imagery has no connection to how a reader experiences a story’s mood', 'A reason unrelated to mood in fiction', 'Mood is entirely unaffected by an author’s descriptive choices'], 0)]),
M('Long Division with Multi-Digit Divisors',
  'Grade 6 Math strand: long division with a multi-digit divisor uses repeated steps of dividing, multiplying, subtracting, and bringing down digits to find a quotient, extending single-digit division strategies to larger numbers.',
  [('The steps of long division are generally repeated in which order?', ['Divide, multiply, subtract, bring down', 'Multiply, divide, bring down, subtract', 'An order unrelated to long division', 'Subtract, divide, bring down, multiply'], 0),
   ('What is 936 ÷ 12?', ['78', '87', 'A value unrelated to the calculation', '68'], 0),
   ('What is 1,244 ÷ 22?', ['56', '54', 'A value unrelated to the calculation', '62'], 0),
   ('When dividing 875 by 25, what does the remainder equal?', ['0, since 25 divides evenly into 875', '5, since the division does not come out evenly', 'A remainder unrelated to the calculation', '25, matching the divisor itself'], 0),
   ('Why is estimating a quotient first often helpful before completing long division with a multi-digit divisor?', ['It gives a reasonable range to check whether the final quotient makes sense', 'Estimating never provides useful information about a division problem', 'A reason unrelated to long division', 'Long division cannot be checked using estimation'], 0)]),
Sc('Fossils and What They Reveal About Earth’s History',
   'Grade 6 Science strand: fossils are the preserved remains or traces of ancient organisms, and studying them helps scientists understand how life and environments on Earth have changed over millions of years.',
   [('A fossil is best described as ___.', ['The preserved remains or traces of an ancient organism', 'A rock that has never contained any living material', 'A concept unrelated to fossils', 'A type of soil found only in deserts'], 0),
    ('Fossils most commonly form when an organism is ___.', ['Quickly buried by sediment that later hardens into rock', 'Left exposed to air and sunlight indefinitely', 'A process unrelated to fossil formation', 'Placed underwater for only a few minutes'], 0),
    ('Why are fossils useful to scientists studying Earth’s past environments?', ['They provide evidence of what organisms and conditions existed at a certain time', 'Fossils provide no information about past environments', 'A reason unrelated to fossils', 'All fossils are exactly the same age, regardless of location'], 0),
    ('What can scientists learn by studying layers of rock that contain different fossils?', ['A general timeline of how life on Earth has changed over long periods', 'Layers of rock never contain any fossil evidence', 'A concept unrelated to studying fossils', 'The exact weather conditions of the present day'], 0),
    ('Why might the discovery of a new fossil species be considered scientifically significant?', ['It can provide new evidence about how life evolved and adapted over time', 'New fossil discoveries never add to scientific understanding', 'A reason unrelated to fossils', 'Fossils have no connection to the study of evolution'], 0)]),
SS('Nunavut and Canada’s Northern Territories',
   'Grade 6 Social Studies strand: Canada’s three northern territories — Yukon, the Northwest Territories, and Nunavut — cover a vast area, with Nunavut created in 1999 as a homeland with significant Inuit self-government.',
   [('Canada’s three northern territories are ___.', ['Yukon, the Northwest Territories, and Nunavut', 'Ontario, Quebec, and Manitoba', 'A grouping unrelated to Canada’s northern territories', 'British Columbia, Alberta, and Saskatchewan'], 0),
    ('Nunavut was created as a separate territory in which year?', ['1999', '1867', 'A year unrelated to Nunavut’s creation', '1949'], 0),
    ('Nunavut was established largely to provide ___.', ['A homeland with significant self-government for the Inuit', 'A territory with no connection to any Indigenous peoples', 'A concept unrelated to Nunavut’s creation', 'An area intended only for southern Canadian settlement'], 0),
    ('What is the capital city of Nunavut?', ['Iqaluit', 'Whitehorse', 'A city unrelated to Nunavut', 'Yellowknife'], 0),
    ('Why are Canada’s northern territories often considered geographically and culturally distinct from the provinces?', ['They have vast, sparsely populated land, unique climates, and significant Indigenous populations and governance', 'The territories are identical to the provinces in every way', 'A reason unrelated to Canada’s northern territories', 'The territories have no distinct population or government structures'], 0)])]),
day(78, [
L('Media Literacy: Evaluating Online Sources for Reliability',
  'Grade 6 Language strand: evaluating online sources for reliability involves checking the author’s credentials, the publication date, and whether the information can be verified by other trustworthy sources.',
  [('When evaluating an online source, a reader should check ___.', ['The author’s credentials, the publication date, and whether it can be verified elsewhere', 'Only how visually appealing the website looks', 'A concept unrelated to evaluating sources', 'Nothing, since all online sources are equally reliable'], 0),
   ('Why might checking a website’s publication date be important when researching a topic?', ['Outdated information may no longer be accurate, especially for fast-changing topics', 'Publication dates never affect how accurate information is', 'A reason unrelated to evaluating sources', 'Older sources are always more reliable than newer ones'], 0),
   ('Which of these is a sign that an online source might be less reliable?', ['It provides no author, sources, or way to verify its claims', 'It cites clear sources and identifies a credible author', 'A sign unrelated to evaluating reliability', 'It is regularly updated with verified information'], 0),
   ('Why is it helpful to compare information across multiple reliable sources?', ['It helps confirm accuracy and reveals whether a claim is widely supported by evidence', 'Comparing sources never helps determine whether information is accurate', 'A reason unrelated to evaluating sources', 'A single online source is always sufficient for verifying any claim'], 0),
   ('Why is evaluating online sources an important skill in today’s digital world?', ['Being able to identify reliable information helps prevent the spread of misinformation', 'Evaluating sources has no real-world importance', 'A reason unrelated to media literacy', 'All information found online is automatically accurate'], 0)]),
M('Classifying and Naming Prisms and Pyramids',
  'Grade 6 Math strand: prisms have two parallel, congruent bases connected by rectangular faces, while pyramids have a single base connected to triangular faces that meet at a point called the apex.',
  [('A prism is a 3D figure with ___.', ['Two parallel, congruent bases connected by rectangular faces', 'A single base connected only to triangular faces', 'A concept unrelated to prisms', 'No flat faces of any kind'], 0),
   ('A pyramid is a 3D figure with ___.', ['A single base connected to triangular faces that meet at an apex', 'Two parallel bases connected by rectangular faces', 'A concept unrelated to pyramids', 'No faces that meet at a single point'], 0),
   ('A triangular prism has which two-shaped bases?', ['Triangles', 'Rectangles', 'A shape unrelated to a triangular prism’s bases', 'Circles'], 0),
   ('A square pyramid has how many triangular faces?', ['4', '2', 'A number unrelated to a square pyramid', '6'], 0),
   ('Why is it useful to classify 3D figures as prisms or pyramids based on their base and faces?', ['It helps identify and compare figures accurately using consistent geometric properties', 'Classifying 3D figures provides no useful information', 'A reason unrelated to geometry', 'All 3D figures are identical, making classification unnecessary'], 0)]),
Sc('Forces of Motion: Friction and Air Resistance',
   'Grade 6 Science strand: friction is a force that resists motion between two surfaces in contact, and air resistance is a type of friction caused by air pushing against a moving object.',
   [('Friction is best described as ___.', ['A force that resists motion between two surfaces in contact', 'A force that always speeds up a moving object', 'A concept unrelated to friction', 'A force that only exists in outer space'], 0),
    ('Air resistance is a type of friction caused by ___.', ['Air pushing against a moving object', 'Water pushing against a moving object', 'A concept unrelated to air resistance', 'Gravity pulling an object downward'], 0),
    ('Why does a parachute slow a falling skydiver down?', ['Its large surface area increases air resistance against the fall', 'Parachutes eliminate all forces acting on the skydiver', 'A reason unrelated to air resistance', 'Parachutes increase the effect of gravity on the skydiver'], 0),
    ('Why might a rough surface create more friction than a smooth surface?', ['Rough surfaces have more contact points that resist sliding motion', 'Rough surfaces always eliminate friction completely', 'A reason unrelated to friction', 'Smooth and rough surfaces always produce identical amounts of friction'], 0),
    ('Why do engineers design cars with smooth, streamlined shapes?', ['To reduce air resistance and improve fuel efficiency at higher speeds', 'Streamlined shapes have no effect on a car’s movement through air', 'A reason unrelated to friction and air resistance', 'Smooth shapes are designed only for appearance, with no functional benefit'], 0)]),
SS('The Great Depression in Canada',
   'Grade 6 Social Studies strand: the Great Depression of the 1930s brought widespread unemployment, poverty, and hardship to Canada, prompting government relief efforts and long-term changes to economic and social policy.',
   [('The Great Depression brought widespread ___.', ['Unemployment, poverty, and economic hardship', 'Economic prosperity with no hardship at all', 'A concept unrelated to the Great Depression', 'A sudden increase in average wages across Canada'], 0),
    ('The Great Depression is generally associated with which decade?', ['The 1930s', 'The 1950s', 'A decade unrelated to the Great Depression', 'The 1980s'], 0),
    ('Which of these was a hardship many Canadians faced during the Great Depression?', ['Difficulty finding steady work and providing for their families', 'An abundance of well-paying jobs for everyone', 'A concept unrelated to the Great Depression', 'No effect at all on Canadian households'], 0),
    ('How did the Canadian government respond to widespread hardship during the Great Depression?', ['It introduced relief efforts and work programs to help struggling citizens', 'It refused to take any action to help struggling citizens', 'A response unrelated to the Great Depression', 'It eliminated all forms of government assistance'], 0),
    ('Why is the Great Depression considered an important turning point in Canadian economic and social policy?', ['It led to lasting changes in how government supports citizens during economic hardship', 'The Great Depression had no lasting effect on Canadian policy', 'A reason unrelated to its historical significance', 'Government policy remained completely unchanged after this period'], 0)])]),
day(79, [
L('Oral Communication: Giving Clear Instructions and Directions',
  'Grade 6 Language strand: giving clear oral instructions involves using precise, sequential language, checking for understanding, and adjusting explanations based on a listener’s questions or reactions.',
  [('Clear oral instructions should generally be ___.', ['Precise and given in a logical, sequential order', 'Vague, with details left out on purpose', 'A concept unrelated to giving instructions', 'Given all at once with no order at all'], 0),
   ('Why might a speaker pause and ask “Does that make sense?” while giving instructions?', ['To check the listener’s understanding before continuing', 'This question always confuses the listener further', 'A reason unrelated to giving instructions', 'Speakers should never check for understanding'], 0),
   ('Which of these is an example of clear, sequential instructional language?', ['First, gather your materials; next, follow each step in order.', 'Materials, steps, maybe, whenever, some things.', 'A sentence unrelated to giving instructions', 'Just do it however you want, in any order.'], 0),
   ('Why might a speaker need to adjust their explanation if a listener looks confused?', ['Adjusting helps ensure the listener understands the instructions being given', 'A confused listener’s reaction should always be ignored', 'A reason unrelated to oral communication', 'Instructions never need to be adjusted once they are spoken'], 0),
   ('Why is giving clear instructions considered an important everyday communication skill?', ['It helps ensure tasks are completed correctly and reduces misunderstandings', 'Clear instructions have no real effect on how well a task is completed', 'A reason unrelated to oral communication', 'Confusing instructions are always just as effective as clear ones'], 0)]),
M('Data Management: Sampling Methods and Bias in Surveys',
  'Grade 6 Math strand: a sample is a smaller group selected to represent a larger population in a survey, and bias occurs when a sample or survey question unfairly favours certain results over others.',
  [('A sample in data management is best described as ___.', ['A smaller group selected to represent a larger population', 'The entire population being studied, with nothing left out', 'A concept unrelated to sampling', 'A single random guess with no connection to data'], 0),
   ('Bias in a survey occurs when ___.', ['A sample or question unfairly favours certain results over others', 'Every group in a population has an equal chance of being selected', 'A concept unrelated to survey bias', 'A survey collects information from the entire population'], 0),
   ('Which of these sampling methods would most likely produce a fair, representative sample?', ['Randomly selecting students from every grade in a school', 'Surveying only students in one specific class', 'A method unrelated to fair sampling', 'Surveying only the survey creator’s close friends'], 0),
   ('Why might the survey question “Don’t you agree that recess should be longer?” be considered biased?', ['Its wording leads respondents toward a particular answer instead of asking neutrally', 'The question is worded in a completely neutral way', 'A reason unrelated to survey bias', 'Biased wording never affects how people respond to a survey'], 0),
   ('Why is it important to use a representative sample when conducting a survey?', ['It helps ensure the results reflect the opinions or characteristics of the larger population', 'A representative sample has no effect on how accurate survey results are', 'A reason unrelated to data management', 'Surveys are always accurate regardless of who is sampled'], 0)]),
Sc('The Integumentary System: Skin as an Organ',
   'Grade 6 Science strand: the skin is the body’s largest organ, forming the integumentary system, which protects the body from injury and infection, helps regulate temperature, and senses touch.',
   [('The skin is considered the body’s largest ___.', ['Organ', 'Bone', 'A concept unrelated to the skin', 'Muscle'], 0),
    ('Which of these is a main function of the skin?', ['Protecting the body from injury and infection', 'Pumping blood throughout the body', 'A function unrelated to the skin', 'Breaking down food into nutrients'], 0),
    ('How does the skin help regulate body temperature?', ['Through processes like sweating, which cools the body as moisture evaporates', 'The skin has no role in regulating body temperature', 'A process unrelated to temperature regulation', 'By preventing the body from ever losing heat'], 0),
    ('Which of these senses is closely associated with the skin?', ['Touch', 'Taste', 'A sense unrelated to the skin', 'Hearing'], 0),
    ('Why is it important for the skin to act as a barrier against germs and injury?', ['It helps prevent harmful bacteria and other pathogens from entering the body', 'The skin provides no protection against germs or injury', 'A reason unrelated to the skin’s function', 'Bacteria are always able to enter the body regardless of the skin'], 0)]),
SS('Immigration Waves: Irish, Ukrainian, and Chinese Settlers in Canada',
   'Grade 6 Social Studies strand: throughout the 19th and early 20th centuries, waves of immigrants, including Irish, Ukrainian, and Chinese settlers, came to Canada and contributed to its growth, often while facing significant hardship and discrimination.',
   [('Many Irish immigrants came to Canada in the 19th century partly due to ___.', ['The Great Famine in Ireland, which caused widespread hunger and hardship', 'An abundance of food and prosperity in Ireland at the time', 'A reason unrelated to Irish immigration', 'A government requirement that all Irish citizens relocate'], 0),
    ('Many Ukrainian immigrants settled in which region of Canada to farm the land?', ['The Canadian Prairies', 'The Arctic coastline exclusively', 'A region unrelated to Ukrainian settlement', 'Downtown areas of major cities only'], 0),
    ('Chinese immigrants made significant contributions to Canada, notably including labour on ___.', ['The Canadian Pacific Railway', 'A project unrelated to Chinese immigration', 'Only local farms, with no connection to major infrastructure', 'Government buildings exclusively'], 0),
    ('Which of these did many immigrant groups, including Chinese immigrants, face in Canada during this period?', ['Discriminatory laws and unfair treatment, such as the Chinese Head Tax', 'Complete equality and fair treatment upon arrival', 'A concept unrelated to immigrant experiences', 'No barriers of any kind to settling in Canada'], 0),
    ('Why is it important to study the experiences of Irish, Ukrainian, and Chinese immigrants in Canadian history?', ['It highlights both their contributions to Canada’s growth and the hardships they overcame', 'These groups made no meaningful contributions to Canadian history', 'A reason unrelated to studying immigration history', 'Studying immigration history serves no educational purpose'], 0)])]),
day(80, [
L('Review: Language Days 71-79',
  'Grade 6 Language strand: this review lesson revisits key ideas from Days 71-79, including adverbs, procedural writing, figurative language, vocabulary resources, conjunctions, revising for clarity, mood, evaluating online sources, and giving clear instructions.',
  [('An adverb typically modifies a ___.', ['Verb, adjective, or other adverb', 'Noun or pronoun only', 'A concept unrelated to adverbs', 'Punctuation mark'], 0),
   ('A simile compares two things using which words?', ['Like or as', 'Metaphor or simile', 'Words unrelated to similes', 'Because or therefore'], 0),
   ('Coordinating conjunctions are used to ___.', ['Join two equal ideas or clauses', 'Only join a subject to a verb', 'A concept unrelated to coordinating conjunctions', 'Replace punctuation marks entirely'], 0),
   ('Mood in a story is best described as ___.', ['The feeling or atmosphere the writing creates for the reader', 'The order in which events occur', 'A concept unrelated to mood', 'The exact number of characters in a story'], 0),
   ('Why is it useful to review grammar, writing, and reading strategies together?', ['It reinforces how these language skills connect and support one another', 'These skills have no connection to each other', 'A reason unrelated to reviewing language concepts', 'Review never helps strengthen understanding of language skills'], 0)]),
M('Review: Math Days 71-79',
  'Grade 6 Math strand: this review lesson revisits key ideas from Days 71-79, including multiplying and dividing decimals by powers of ten, angle relationships, LCM and GCF, probability, unit rates, long division, 3D figure classification, and sampling.',
  [('When you multiply a decimal by 10, the decimal point moves ___.', ['One place to the right', 'One place to the left', 'A direction unrelated to multiplying by ten', 'Two places to the right'], 0),
   ('Two angles are complementary if their measures add up to ___.', ['90 degrees', '180 degrees', 'A sum unrelated to complementary angles', '360 degrees'], 0),
   ('The least common multiple of two numbers is ___.', ['The smallest number that is a multiple of both numbers', 'The largest number that divides evenly into both numbers', 'A concept unrelated to least common multiple', 'Always equal to one of the two original numbers'], 0),
   ('A unit rate expresses a quantity ___.', ['Per single unit, such as price per one item', 'As a fraction with no connection to a single unit', 'A concept unrelated to unit rates', 'Only in terms of time, never price'], 0),
   ('Why is it useful to review number, geometry, and data concepts together?', ['It reinforces how these math skills connect and build on one another', 'These topics have no connection to each other', 'A reason unrelated to reviewing math', 'Review never helps strengthen understanding of a subject'], 0)]),
Sc('Review: Science Days 71-79',
   'Grade 6 Science strand: this review lesson revisits key ideas from Days 71-79, including the digestive, circulatory, respiratory, and integumentary systems, states of matter, soil formation, freshwater and saltwater ecosystems, fossils, and friction.',
   [('The main purpose of the digestive system is to ___.', ['Break down food into nutrients the body can absorb and use', 'Pump blood throughout the body', 'A concept unrelated to the digestive system', 'Filter air before it reaches the lungs'], 0),
    ('The main function of the circulatory system is to ___.', ['Transport oxygen, nutrients, and waste throughout the body', 'Break down food into nutrients', 'A concept unrelated to the circulatory system', 'Filter air before it reaches the lungs'], 0),
    ('Which of these is a change of state that occurs when a solid becomes a liquid?', ['Melting', 'Freezing', 'A process unrelated to changes of state', 'Condensation'], 0),
    ('Friction is best described as ___.', ['A force that resists motion between two surfaces in contact', 'A force that always speeds up a moving object', 'A concept unrelated to friction', 'A force that only exists in outer space'], 0),
    ('Why is it useful to review body systems, matter, and Earth science concepts together?', ['It reinforces how these interconnected science concepts relate to one another', 'These topics have no connection to each other', 'Review is never useful in science', 'Each topic must be studied with no connection to the others'], 0)]),
SS('Review: Social Studies Days 71-79',
   'Grade 6 Social Studies strand: this review lesson revisits key ideas from Days 71-79, including the War of 1812, the Underground Railroad, Indigenous treaties, the Charter of Rights and Freedoms, the fur trade, the Red River Resistance, Nunavut, the Great Depression, and immigration waves.',
   [('The War of 1812 was fought primarily between Britain (with its colonies) and ___.', ['The United States', 'France', 'A country unrelated to the War of 1812', 'Spain'], 0),
    ('The Underground Railroad was best described as ___.', ['A secret network of routes and safe houses helping enslaved people escape to freedom', 'An actual railway built underground', 'A concept unrelated to the Underground Railroad', 'A government program run openly by the United States'], 0),
    ('The Canadian Charter of Rights and Freedoms became part of Canada’s Constitution in which year?', ['1982', '1867', 'A year unrelated to the Charter', '1945'], 0),
    ('Nunavut was created as a separate territory in which year?', ['1999', '1867', 'A year unrelated to Nunavut’s creation', '1949'], 0),
    ('Why is it useful to review Canadian history topics like treaties, migration, and government together?', ['It reinforces how historical events connect to shape Canadian identity and society today', 'These topics have no connection to one another', 'A reason unrelated to social studies learning', 'Review is never useful when studying history'], 0)])]),
]

def _rebalance_answer_positions(days, seed=20260904):
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
    _rebalance_answer_positions(g6_71_80)
    append_to(6, g6_71_80)
